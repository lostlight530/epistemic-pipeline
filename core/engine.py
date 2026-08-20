#!/usr/bin/env python3
"""
状态机执行引擎 — 解析依赖图并执行状态流转
"""

import yaml
import json
import os
import sys
import time
import uuid
import concurrent.futures
from pathlib import Path
from typing import Dict, List, Set, Tuple, Optional
from collections import deque

# 修复模块导入路径
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from core.dependency_graph import DependencyGraph
from core.gatekeeper import Gatekeeper
from core.llm_harness import LLMHarness
from core.confidence_net import ConfidenceNetwork
from core.knowledge_extractor import KnowledgeExtractor
from core.run_tracer import RunTracer
from core.resilience import RetryPolicy, run_with_retry, run_with_timeout, classify_error
from core.calibration import calibrate_confidence_map

class StateMachineEngine:
    """状态机执行引擎"""

    def __init__(self, graph_path: str, mock_llm: bool = True,
                 use_gatekeeper: bool = True, use_confidence_net: bool = True,
                 harness: LLMHarness = None,
                 trace_dir: Optional[str] = 'traces',
                 checkpoint_dir: Optional[str] = 'checkpoints',
                 calibration_temperature: Optional[float] = None):
        self.graph_data = self._load_graph(graph_path)
        self.nodes = {n['id']: n for n in self.graph_data['nodes']}
        self.dep_graph = DependencyGraph(self.graph_data['nodes'])
        self.execution_order = []
        self.current_state = None
        self.outputs = {}
        self.mock_llm = mock_llm
        self.use_gatekeeper = use_gatekeeper
        self.use_confidence_net = use_confidence_net
        self.harness = harness or LLMHarness()
        self.gatekeeper = Gatekeeper() if use_gatekeeper else None
        self.trace_dir = trace_dir            # None = 关闭轨迹记录
        self.checkpoint_dir = checkpoint_dir  # None = 关闭检查点
        self.calibration_temperature = calibration_temperature  # None = 不校准

    def _load_graph(self, path: str) -> dict:
        with open(path, 'r', encoding='utf-8') as f:
            data = yaml.safe_load(f)
        if not isinstance(data, dict) or 'nodes' not in data:
            graph_type = data.get('type', 'unknown') if isinstance(data, dict) else 'unknown'
            raise ValueError(
                f"图文件 {path} 不包含可执行的 nodes 定义 (type: {graph_type})。"
                "主引擎仅支持含 nodes 的 DAG 图 (linear/parallel/diamond)；"
                "adaptive 等实验性拓扑尚未接入执行链。")
        return data

    def validate(self) -> Tuple[bool, List[str]]:
        return self.dep_graph.validate()

    def compute_execution_order(self) -> List[str]:
        """计算拓扑排序的执行顺序"""
        self.execution_order = self.dep_graph.topological_sort()
        return self.execution_order

    # ------------------------------------------------------------------
    # 检查点 (LangGraph 风格节点级 checkpoint：每层完成后落盘，可断点续跑)
    # ------------------------------------------------------------------

    def _checkpoint_path(self, run_id: str) -> Path:
        return Path(self.checkpoint_dir) / run_id / 'checkpoint.json'

    def _write_checkpoint(self, run_id: str, results: dict):
        """每层完成后将成功节点结果原子落盘（状态为纯 dict，天然可序列化）"""
        if not self.checkpoint_dir:
            return
        path = self._checkpoint_path(run_id)
        path.parent.mkdir(parents=True, exist_ok=True)
        payload = {
            "run_id": run_id,
            "graph": self.graph_data.get('id'),
            "updated_at": time.time(),
            "completed": [nid for nid, r in results.items() if r.get('status') == 'success'],
            "results": results,
        }
        tmp_path = path.with_suffix('.json.tmp')
        with open(tmp_path, 'w', encoding='utf-8') as f:
            json.dump(payload, f, ensure_ascii=False, indent=2)
        os.replace(tmp_path, path)  # 原子替换，避免半写状态

    def _load_checkpoint(self, run_id: str) -> dict:
        """加载检查点中已成功完成的节点结果；失败及未执行节点将被重跑"""
        if not self.checkpoint_dir:
            raise ValueError("checkpoint_dir 已关闭，无法断点续跑")
        path = self._checkpoint_path(run_id)
        if not path.exists():
            raise ValueError(f"检查点不存在: {path}（run_id={run_id}），无法 resume")
        with open(path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        if data.get('graph') != self.graph_data.get('id'):
            raise ValueError(
                f"检查点图标识不匹配: 检查点={data.get('graph')!r} vs "
                f"当前={self.graph_data.get('id')!r}，拒绝跨图续跑")
        return {nid: res for nid, res in data.get('results', {}).items()
                if res.get('status') == 'success'}

    # ------------------------------------------------------------------
    # 节点执行
    # ------------------------------------------------------------------

    def _execute_node(self, state_id: str, results_dict: dict,
                      tracer: Optional[RunTracer] = None) -> dict:
        """执行单个节点逻辑（含轨迹记录、重试、超时、质量门）"""
        node = self.nodes[state_id]
        stage = node['stage']

        print(f"\n▶️ 执行状态: {state_id} (stage: {stage})")
        if tracer:
            tracer.start_node(state_id, stage)
        try:
            result = self._execute_node_core(state_id, results_dict)
        except Exception as exc:
            if tracer:
                tracer.end_node(state_id, stage, 'failed',
                                error_type=type(exc).__name__)
            raise
        if tracer:
            tracer.end_node(
                state_id, stage, result['status'],
                error_type='QualityGateError' if result['status'] == 'failed' else None)
        return result

    def _execute_node_core(self, state_id: str, results_dict: dict) -> dict:
        node = self.nodes[state_id]
        stage = node['stage']

        # 加载状态定义
        state_def = self._load_state(stage)

        # 检查进入条件
        deps = node.get('dependencies', [])
        for dep in deps:
            if dep not in results_dict or results_dict[dep]['status'] != 'success':
                print(f"  ⚠️ 依赖 {dep} 尚未成功完成")
                return {"status": "failed", "errors": [f"依赖 {dep} 未完成"]}

        # 通过 LLM Harness 按角色绑定执行，获得结构化输出（默认 mock 模式）。
        # 节点可声明 retry{max_attempts, base_delay, factor} 与 timeout_seconds：
        # transient 错误（超时/连接等）指数退避重试，permanent 错误（未实现/参数错）立即失败。
        inputs = {dep: results_dict[dep].get('outputs') for dep in deps}
        role_bindings = state_def.get('role_bindings', {'primary': stage})
        retry_policy = RetryPolicy.from_node_spec(node.get('retry'))
        timeout_seconds = node.get('timeout_seconds')

        def invoke_llm():
            return run_with_timeout(
                lambda: self.harness.execute(state_id, role_bindings, inputs, mock=self.mock_llm),
                timeout_seconds)

        def log_retry(attempt, exc, delay):
            print(f"  🔁 节点 {state_id} 第 {attempt} 次尝试失败 "
                  f"({classify_error(exc)}: {exc})，{delay:.2f}s 后重试")

        outputs = run_with_retry(invoke_llm, retry_policy, on_retry=log_retry)

        # synthesize 阶段：将上游主张/冲突接入置信度传播网络，计算真实收敛结果
        if self.use_confidence_net and stage == 'synthesize':
            outputs.update(self._run_confidence_network(results_dict))

        # Gatekeeper 质量门拦截：输出不符合质量门则节点失败
        if self.gatekeeper is not None:
            passed, gate_errors = self.gatekeeper.check_quality_gates(state_def, outputs)
            if not passed:
                for e in gate_errors:
                    print(f"  🚫 质量门拦截: {e}")
                return {"status": "failed", "errors": gate_errors}

        result = {
            "status": "success",
            "state_id": state_id,
            "stage": stage,
            "completed": True,
            "outputs": outputs,
            "quality_gates_passed": self.gatekeeper is not None
        }
        print(f"  ✅ {state_id} 完成")
        return result

    def _run_confidence_network(self, results_dict: dict) -> dict:
        """
        汇总上游 analyze/verify 产出的主张与冲突，
        通过 KnowledgeExtractor 桥接进 ConfidenceNetwork 并迭代至收敛。
        若构造时给定 calibration_temperature，对收敛结果做 temperature scaling
        （单调保序变换，不改变收敛判据 delta 的计算口径）。
        """
        claims_by_id = {}
        conflicts = []
        confidence_seed = {}

        for res in results_dict.values():
            outs = res.get('outputs') or {}
            for claim in outs.get('claims_registry') or []:
                cid = claim.get('claim_id')
                if cid:
                    claims_by_id[cid] = claim
            conflicts.extend(outs.get('conflict_registry') or [])
            seed = outs.get('confidence_seed') or {}
            confidence_seed.update(seed)

        # 验证阶段的置信度种子优先作为初始置信度
        for cid, value in confidence_seed.items():
            if cid in claims_by_id:
                claims_by_id[cid]['initial_confidence'] = value

        network_input = KnowledgeExtractor.extract_to_network_format(
            list(claims_by_id.values()), conflicts)

        net = ConfidenceNetwork()
        for n in network_input['nodes']:
            net.add_node(n['claim_id'], n['initial_confidence'])
        for e in network_input['edges']:
            # 冲突可能引用未登记的主张，补默认置信度 0.5 的节点以保证传播完整
            for endpoint in (e['source'], e['target']):
                if endpoint not in net.nodes:
                    net.add_node(endpoint, 0.5)
            net.add_edge(e['source'], e['target'], e['weight'], e['edge_type'])

        if not net.nodes:
            return {"confidence_network": {"converged": True, "iterations": 0, "final": {}}, "delta": 0.0}

        final, iterations, converged = net.converge()
        report = {
            "converged": converged,
            "iterations": iterations,
            "final": final
        }
        if self.calibration_temperature:
            report["uncalibrated"] = final
            report["final"] = calibrate_confidence_map(final, self.calibration_temperature)
            report["calibration"] = {
                "method": "temperature_scaling",
                "temperature": self.calibration_temperature,
                "note": "单调保序变换；mock 阶段置信度为启发值而非校准概率"
            }
        print(f"  🧠 置信度网络收敛: {converged} (迭代 {iterations} 次, delta={net.last_delta:.4f})")
        return {"confidence_network": report, "delta": net.last_delta}

    # ------------------------------------------------------------------
    # 流水线执行
    # ------------------------------------------------------------------

    def run(self, resume_from: Optional[str] = None) -> dict:
        """
        执行完整流水线。
        resume_from: 指定既有 run_id 时从其检查点断点续跑——已成功的节点
        直接复用结果，仅重跑失败及未执行的节点（LangGraph 检查点模式）。
        注：permanent 异常（如真实 LLM 未接入的 NotImplementedError）按
        fail-fast 原则直接抛出；此前各层检查点已落盘，可用 self.last_run_id 续跑。
        """
        valid, errors = self.validate()
        if not valid:
            print("❌ 图验证失败:")
            for e in errors:
                print(f"  - {e}")
            return {"status": "failed", "errors": errors}

        run_id = resume_from or uuid.uuid4().hex[:12]
        self.last_run_id = run_id  # 异常 fail-fast 抛出时，调用方仍可凭此续跑已落盘层
        tracer = RunTracer(run_id, self.trace_dir) if self.trace_dir else None

        results = {}
        if resume_from:
            results = self._load_checkpoint(resume_from)
            self.outputs.update(results)
            print(f"♻️ 从检查点续跑 run_id={run_id}，复用 {len(results)} 个已成功节点: "
                  f"{sorted(results)}")

        parallel_groups = self.dep_graph.find_parallel_groups()
        print(f"✅ 图验证通过，并行执行组: {parallel_groups} (run_id={run_id})")

        total_nodes_executed = 0

        # 按层级并行执行
        for group in parallel_groups:
            pending = [nid for nid in group if nid not in results]
            if not pending:
                continue  # 整层已在检查点中成功完成
            if len(pending) == 1:
                state_id = pending[0]
                result = self._execute_node(state_id, results, tracer)
                results[state_id] = result
                self.outputs[state_id] = result
                if result['status'] == 'failed':
                    self._write_checkpoint(run_id, results)
                    return {"status": "failed", "errors": result['errors'],
                            "results": results, "run_id": run_id}
                total_nodes_executed += 1
            else:
                print(f"\n🚀 并行执行组: {pending}")
                group_errors = []
                with concurrent.futures.ThreadPoolExecutor(max_workers=len(pending)) as executor:
                    future_to_node = {executor.submit(self._execute_node, state_id, results, tracer): state_id for state_id in pending}

                    # 收集整组结果后再判定：任一失败不再丢弃兄弟节点的已完成结果
                    for future in concurrent.futures.as_completed(future_to_node):
                        state_id = future_to_node[future]
                        try:
                            result = future.result()
                            results[state_id] = result
                            self.outputs[state_id] = result
                            if result['status'] == 'failed':
                                group_errors.extend(result['errors'])
                            else:
                                total_nodes_executed += 1
                        except Exception as exc:
                            print(f"  ❌ 节点 {state_id} 产生异常: {exc}")
                            group_errors.append(f"{state_id}: {exc}")
                if group_errors:
                    self._write_checkpoint(run_id, results)
                    return {"status": "failed", "errors": group_errors,
                            "results": results, "run_id": run_id}

            self._write_checkpoint(run_id, results)

        order = self.compute_execution_order()
        print(f"\n🎉 流水线执行完成，共 {total_nodes_executed} 个状态 (run_id={run_id})")
        self._write_checkpoint(run_id, results)
        return {"status": "success", "results": results, "order": order, "run_id": run_id}

    def _load_state(self, stage_name: str) -> dict:
        state_path = Path('states') / f'{stage_name}.yaml'
        with open(state_path, 'r', encoding='utf-8') as f:
            return yaml.safe_load(f)

def main():
    import argparse
    parser = argparse.ArgumentParser(description='Epistemic Pipeline 执行引擎')
    parser.add_argument('action', choices=['run', 'validate'], help='操作')
    parser.add_argument('graph', help='依赖图文件路径')
    parser.add_argument('--resume-from', metavar='RUN_ID',
                        help='从指定 run_id 的检查点断点续跑（仅重跑失败及未执行节点）')
    parser.add_argument('--checkpoint-dir', default='checkpoints',
                        help='检查点目录（默认 checkpoints/）')
    parser.add_argument('--trace-dir', default='traces',
                        help='运行轨迹 JSONL 目录（默认 traces/）')
    args = parser.parse_args()

    engine = StateMachineEngine(args.graph,
                                checkpoint_dir=args.checkpoint_dir,
                                trace_dir=args.trace_dir)

    if args.action == 'validate':
        valid, errors = engine.validate()
        print(f"{'✅' if valid else '❌'} 验证结果: {'通过' if valid else '失败'}")
        if errors:
            for e in errors:
                print(f"  - {e}")
    elif args.action == 'run':
        result = engine.run(resume_from=args.resume_from)
        print(f"\n最终状态: {result['status']} (run_id={result.get('run_id', 'n/a')})")

if __name__ == '__main__':
    main()
