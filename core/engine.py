#!/usr/bin/env python3
"""
状态机执行引擎 — 解析依赖图并执行状态流转
"""

import yaml
import json
import os
import sys
import concurrent.futures
from pathlib import Path
from typing import Dict, List, Set, Tuple
from collections import deque

# 修复模块导入路径
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from core.dependency_graph import DependencyGraph
from core.gatekeeper import Gatekeeper
from core.llm_harness import LLMHarness
from core.confidence_net import ConfidenceNetwork
from core.knowledge_extractor import KnowledgeExtractor

class StateMachineEngine:
    """状态机执行引擎"""
    
    def __init__(self, graph_path: str, mock_llm: bool = True,
                 use_gatekeeper: bool = True, use_confidence_net: bool = True,
                 harness: LLMHarness = None):
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

    def _execute_node(self, state_id: str, results_dict: dict) -> dict:
        """执行单个节点逻辑"""
        node = self.nodes[state_id]
        stage = node['stage']
        
        print(f"\n▶️ 执行状态: {state_id} (stage: {stage})")
        
        # 加载状态定义
        state_def = self._load_state(stage)
        
        # 检查进入条件
        deps = node.get('dependencies', [])
        for dep in deps:
            if dep not in results_dict or results_dict[dep]['status'] != 'success':
                print(f"  ⚠️ 依赖 {dep} 尚未成功完成")
                return {"status": "failed", "errors": [f"依赖 {dep} 未完成"]}

        # 通过 LLM Harness 按角色绑定执行，获得结构化输出（默认 mock 模式）
        inputs = {dep: results_dict[dep].get('outputs') for dep in deps}
        role_bindings = state_def.get('role_bindings', {'primary': stage})
        outputs = self.harness.execute(state_id, role_bindings, inputs, mock=self.mock_llm)

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
        print(f"  🧠 置信度网络收敛: {converged} (迭代 {iterations} 次, delta={net.last_delta:.4f})")
        return {"confidence_network": report, "delta": net.last_delta}

    def run(self) -> dict:
        """执行完整流水线"""
        valid, errors = self.validate()
        if not valid:
            print("❌ 图验证失败:")
            for e in errors:
                print(f"  - {e}")
            return {"status": "failed", "errors": errors}
        
        parallel_groups = self.dep_graph.find_parallel_groups()
        print(f"✅ 图验证通过，并行执行组: {parallel_groups}")
        
        results = {}
        total_nodes_executed = 0

        # 按层级并行执行
        for group in parallel_groups:
            if len(group) == 1:
                state_id = group[0]
                result = self._execute_node(state_id, results)
                if result['status'] == 'failed':
                    return {"status": "failed", "errors": result['errors']}
                results[state_id] = result
                self.outputs[state_id] = result
                total_nodes_executed += 1
            else:
                print(f"\n🚀 并行执行组: {group}")
                with concurrent.futures.ThreadPoolExecutor(max_workers=len(group)) as executor:
                    future_to_node = {executor.submit(self._execute_node, state_id, results): state_id for state_id in group}

                    for future in concurrent.futures.as_completed(future_to_node):
                        state_id = future_to_node[future]
                        try:
                            result = future.result()
                            if result['status'] == 'failed':
                                return {"status": "failed", "errors": result['errors']}
                            results[state_id] = result
                            self.outputs[state_id] = result
                            total_nodes_executed += 1
                        except Exception as exc:
                            print(f"  ❌ 节点 {state_id} 产生异常: {exc}")
                            return {"status": "failed", "errors": [str(exc)]}
        
        order = self.compute_execution_order()
        print(f"\n🎉 流水线执行完成，共 {total_nodes_executed} 个状态")
        return {"status": "success", "results": results, "order": order}
    
    def _load_state(self, stage_name: str) -> dict:
        state_path = Path('states') / f'{stage_name}.yaml'
        with open(state_path, 'r', encoding='utf-8') as f:
            return yaml.safe_load(f)

def main():
    import argparse
    parser = argparse.ArgumentParser(description='Epistemic Pipeline 执行引擎')
    parser.add_argument('action', choices=['run', 'validate'], help='操作')
    parser.add_argument('graph', help='依赖图文件路径')
    args = parser.parse_args()
    
    engine = StateMachineEngine(args.graph)
    
    if args.action == 'validate':
        valid, errors = engine.validate()
        print(f"{'✅' if valid else '❌'} 验证结果: {'通过' if valid else '失败'}")
        if errors:
            for e in errors:
                print(f"  - {e}")
    elif args.action == 'run':
        result = engine.run()
        print(f"\n最终状态: {result['status']}")

if __name__ == '__main__':
    main()
