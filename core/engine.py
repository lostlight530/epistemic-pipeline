#!/usr/bin/env python3
"""State-machine execution engine for epistemic-pipeline.

The engine coordinates DAG scheduling, provider execution, runtime-policy
assessment, bounded score propagation, tracing and checkpoint/resume. It does
not interpret a completed run as scientific truth.
"""

from __future__ import annotations

import argparse
import concurrent.futures
import hashlib
import json
import os
import sys
import time
import uuid
from pathlib import Path
from typing import Dict, List, Optional, Tuple

import yaml

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from core.calibration import calibrate_confidence_map
from core.confidence_net import ConfidenceNetwork
from core.dependency_graph import DependencyGraph
from core.gatekeeper import RuntimePolicyEvaluator
from core.knowledge_extractor import KnowledgeExtractor
from core.llm_harness import LLMHarness
from core.resilience import RetryPolicy, classify_error, run_with_retry, run_with_timeout
from core.run_tracer import RunTracer


ENGINE_PROFILE = "epistemic-pipeline/engine"


def canonical_sha256(value: object) -> str:
    encoded = json.dumps(
        value,
        ensure_ascii=False,
        sort_keys=True,
        separators=(",", ":"),
    ).encode("utf-8")
    return "sha256:" + hashlib.sha256(encoded).hexdigest()


class StateMachineEngine:
    """Execute one validated research DAG through canonical state definitions."""

    def __init__(
        self,
        graph_path: str,
        mock_llm: bool = True,
        use_gatekeeper: bool = True,
        use_confidence_net: bool = True,
        harness: Optional[LLMHarness] = None,
        trace_dir: Optional[str] = "traces",
        checkpoint_dir: Optional[str] = "checkpoints",
        calibration_temperature: Optional[float] = None,
        use_runtime_policy: Optional[bool] = None,
    ):
        self.graph_path = str(graph_path)
        self.graph_data = self._load_graph(graph_path)
        self.graph_sha256 = canonical_sha256(self.graph_data)
        self.nodes = {node["id"]: node for node in self.graph_data["nodes"]}
        self.dep_graph = DependencyGraph(self.graph_data["nodes"])
        self.execution_order: List[str] = []
        self.current_state = None
        self.outputs: Dict[str, dict] = {}
        self.mock_llm = mock_llm
        self.use_confidence_net = use_confidence_net
        self.harness = harness or LLMHarness()

        policy_enabled = use_gatekeeper if use_runtime_policy is None else use_runtime_policy
        self.use_runtime_policy = bool(policy_enabled)
        self.policy_evaluator = RuntimePolicyEvaluator() if self.use_runtime_policy else None
        self.gatekeeper = self.policy_evaluator

        self.trace_dir = trace_dir
        self.checkpoint_dir = checkpoint_dir
        self.calibration_temperature = calibration_temperature
        self.last_run_id: Optional[str] = None

    @staticmethod
    def _load_graph(path: str) -> dict:
        with open(path, "r", encoding="utf-8") as handle:
            data = yaml.safe_load(handle)
        if not isinstance(data, dict) or "nodes" not in data:
            graph_type = data.get("type", "unknown") if isinstance(data, dict) else "unknown"
            raise ValueError(
                f"图文件 {path} 不包含可执行的 nodes 定义 (type: {graph_type})。"
                "主引擎仅支持含 nodes 的 DAG；adaptive 等实验性拓扑尚未接入执行链。"
            )
        if not isinstance(data["nodes"], list) or not data["nodes"]:
            raise ValueError("graph nodes must be a non-empty list")
        return data

    def validate(self) -> Tuple[bool, List[str]]:
        return self.dep_graph.validate()

    def compute_execution_order(self) -> List[str]:
        self.execution_order = self.dep_graph.topological_sort()
        return self.execution_order

    def _checkpoint_path(self, run_id: str) -> Path:
        if not self.checkpoint_dir:
            raise ValueError("checkpoint_dir is disabled")
        return Path(self.checkpoint_dir) / run_id / "checkpoint.json"

    def _write_checkpoint(self, run_id: str, results: dict) -> None:
        if not self.checkpoint_dir:
            return
        path = self._checkpoint_path(run_id)
        path.parent.mkdir(parents=True, exist_ok=True)
        payload = {
            "profile": "epistemic-pipeline/checkpoint",
            "run_id": run_id,
            "graph_id": self.graph_data.get("id"),
            "graph_sha256": self.graph_sha256,
            "updated_at": time.time(),
            "completed": [
                node_id
                for node_id, result in results.items()
                if result.get("status") == "success"
            ],
            "results": results,
        }
        tmp_path = path.with_suffix(".json.tmp")
        with tmp_path.open("w", encoding="utf-8") as handle:
            json.dump(payload, handle, ensure_ascii=False, indent=2)
        os.replace(tmp_path, path)

    def _load_checkpoint(self, run_id: str) -> dict:
        path = self._checkpoint_path(run_id)
        if not path.exists():
            raise ValueError(f"检查点不存在: {path}（run_id={run_id}）")
        with path.open("r", encoding="utf-8") as handle:
            data = json.load(handle)

        recorded_hash = data.get("graph_sha256")
        if not recorded_hash:
            raise ValueError("legacy checkpoint lacks graph_sha256; refusing ambiguous resume")
        if recorded_hash != self.graph_sha256:
            raise ValueError(
                "checkpoint graph digest mismatch: "
                f"checkpoint={recorded_hash!r} current={self.graph_sha256!r}"
            )
        if data.get("graph_id") != self.graph_data.get("id"):
            raise ValueError(
                f"checkpoint graph id mismatch: {data.get('graph_id')!r} "
                f"vs {self.graph_data.get('id')!r}"
            )
        return {
            node_id: result
            for node_id, result in (data.get("results") or {}).items()
            if isinstance(result, dict) and result.get("status") == "success"
        }

    def _execute_node(
        self,
        state_id: str,
        results_dict: dict,
        tracer: Optional[RunTracer] = None,
    ) -> dict:
        node = self.nodes[state_id]
        stage = node["stage"]

        print(f"\n▶️ 执行状态: {state_id} (stage: {stage})")
        if tracer:
            tracer.start_node(state_id, stage)
        try:
            result = self._execute_node_core(state_id, results_dict)
        except Exception as exc:
            if tracer:
                tracer.end_node(state_id, stage, "failed", error_type=type(exc).__name__)
            raise

        if tracer:
            error_type = None
            if result["status"] == "failed" and result.get("failure_kind") == "runtime_policy":
                error_type = "RuntimePolicyError"
            tracer.end_node(state_id, stage, result["status"], error_type=error_type)
        return result

    def _execute_node_core(self, state_id: str, results_dict: dict) -> dict:
        node = self.nodes[state_id]
        stage = node["stage"]
        state_def = self._load_state(stage)

        dependencies = node.get("dependencies", []) or []
        for dependency in dependencies:
            result = results_dict.get(dependency)
            if not isinstance(result, dict) or result.get("status") != "success":
                return {
                    "status": "failed",
                    "state_id": state_id,
                    "stage": stage,
                    "failure_kind": "dependency",
                    "errors": [f"依赖 {dependency} 未成功完成"],
                }

        inputs = {
            dependency: results_dict[dependency].get("outputs")
            for dependency in dependencies
        }
        role_bindings = state_def.get("role_bindings", {"primary": stage})
        retry_policy = RetryPolicy.from_node_spec(node.get("retry"))
        timeout_seconds = node.get("timeout_seconds")

        def invoke_provider():
            return run_with_timeout(
                lambda: self.harness.execute(
                    state_id,
                    role_bindings,
                    inputs,
                    mock=self.mock_llm,
                ),
                timeout_seconds,
            )

        def log_retry(attempt, exc, delay):
            print(
                f"  🔁 节点 {state_id} 第 {attempt} 次尝试失败 "
                f"({classify_error(exc)}: {exc})，{delay:.2f}s 后重试"
            )

        outputs = run_with_retry(invoke_provider, retry_policy, on_retry=log_retry)
        if not isinstance(outputs, dict):
            raise TypeError("provider output must be a mapping")

        if self.use_confidence_net and stage == "synthesize":
            outputs.update(self._run_confidence_network(results_dict))

        policy_evaluated = self.policy_evaluator is not None
        if self.policy_evaluator is not None:
            passed, policy_errors = self.policy_evaluator.evaluate(state_def, outputs)
            if not passed:
                for error in policy_errors:
                    print(f"  ⛔ 运行时约束未满足: {error}")
                return {
                    "status": "failed",
                    "state_id": state_id,
                    "stage": stage,
                    "failure_kind": "runtime_policy",
                    "runtime_policy_profile": "epistemic-pipeline/runtime-policy",
                    "runtime_policy_passed": False,
                    "errors": policy_errors,
                }

        result = {
            "status": "success",
            "state_id": state_id,
            "stage": stage,
            "completed": True,
            "outputs": outputs,
            "runtime_policy_evaluated": policy_evaluated,
            "runtime_policy_passed": True if policy_evaluated else None,
        }
        print(f"  ✅ {state_id} 完成")
        return result

    def _run_confidence_network(self, results_dict: dict) -> dict:
        claims_by_id: Dict[str, dict] = {}
        conflicts: List[dict] = []
        score_seed: Dict[str, float] = {}

        for result in results_dict.values():
            outputs = result.get("outputs") or {}
            for claim in outputs.get("claims_registry") or []:
                if isinstance(claim, dict) and claim.get("claim_id"):
                    claims_by_id[claim["claim_id"]] = dict(claim)
            conflicts.extend(
                item for item in (outputs.get("conflict_registry") or []) if isinstance(item, dict)
            )
            seed = outputs.get("confidence_seed") or outputs.get("score_seed") or {}
            if isinstance(seed, dict):
                score_seed.update(seed)

        for claim_id, value in score_seed.items():
            if claim_id in claims_by_id:
                claims_by_id[claim_id]["initial_confidence"] = value

        network_input = KnowledgeExtractor.extract_to_network_format(
            list(claims_by_id.values()), conflicts
        )
        net = ConfidenceNetwork()
        for node in network_input["nodes"]:
            net.add_node(node["claim_id"], node["initial_confidence"])
        for edge in network_input["edges"]:
            net.add_edge(
                edge["source"], edge["target"], edge["weight"], edge["edge_type"]
            )

        if not net.nodes:
            return {
                "confidence_network": {
                    "converged": True,
                    "iterations": 0,
                    "final": {},
                    "score_semantics": "bounded_weighted_heuristic_not_calibrated_probability",
                },
                "delta": 0.0,
            }

        final, iterations, converged = net.converge()
        report = {
            "converged": converged,
            "iterations": iterations,
            "final": final,
            "score_semantics": "bounded_weighted_heuristic_not_calibrated_probability",
        }
        if self.calibration_temperature:
            report["uncalibrated"] = final
            report["final"] = calibrate_confidence_map(final, self.calibration_temperature)
            report["calibration_transform"] = {
                "method": "temperature_scaling_transform",
                "temperature": self.calibration_temperature,
                "fitted_on_labelled_data": False,
                "probability_calibration_claim": False,
            }
        print(
            f"  🧠 score network numerical convergence: {converged} "
            f"(iterations={iterations}, delta={net.last_delta:.4f})"
        )
        return {"confidence_network": report, "delta": net.last_delta}

    def run(self, resume_from: Optional[str] = None) -> dict:
        valid, errors = self.validate()
        if not valid:
            return {
                "status": "failed",
                "errors": errors,
                "graph_sha256": self.graph_sha256,
                "engine_profile": ENGINE_PROFILE,
            }

        run_id = resume_from or uuid.uuid4().hex[:12]
        self.last_run_id = run_id
        tracer = RunTracer(run_id, self.trace_dir) if self.trace_dir else None

        results: Dict[str, dict] = {}
        if resume_from:
            results = self._load_checkpoint(resume_from)
            self.outputs.update(results)
            print(
                f"♻️ 从检查点续跑 run_id={run_id}，复用 {len(results)} 个成功节点: "
                f"{sorted(results)}"
            )

        parallel_groups = self.dep_graph.find_parallel_groups()
        total_nodes_executed = 0

        for group in parallel_groups:
            pending = [node_id for node_id in group if node_id not in results]
            if not pending:
                continue

            if len(pending) == 1:
                state_id = pending[0]
                result = self._execute_node(state_id, results, tracer)
                results[state_id] = result
                self.outputs[state_id] = result
                if result["status"] == "failed":
                    self._write_checkpoint(run_id, results)
                    return self._run_result("failed", run_id, results, result.get("errors", []))
                total_nodes_executed += 1
            else:
                print(f"\n🚀 并行执行组: {pending}")
                group_errors: List[str] = []
                with concurrent.futures.ThreadPoolExecutor(max_workers=len(pending)) as executor:
                    future_to_node = {
                        executor.submit(self._execute_node, state_id, results, tracer): state_id
                        for state_id in pending
                    }
                    for future in concurrent.futures.as_completed(future_to_node):
                        state_id = future_to_node[future]
                        try:
                            result = future.result()
                            results[state_id] = result
                            self.outputs[state_id] = result
                            if result["status"] == "failed":
                                group_errors.extend(result.get("errors", []))
                            else:
                                total_nodes_executed += 1
                        except Exception as exc:
                            group_errors.append(f"{state_id}: {type(exc).__name__}: {exc}")
                if group_errors:
                    self._write_checkpoint(run_id, results)
                    return self._run_result("failed", run_id, results, group_errors)

            self._write_checkpoint(run_id, results)

        order = self.compute_execution_order()
        self._write_checkpoint(run_id, results)
        print(f"\n🎉 流水线执行完成，共 {total_nodes_executed} 个状态 (run_id={run_id})")
        result = self._run_result("success", run_id, results, [])
        result["order"] = order
        return result

    def _run_result(self, status: str, run_id: str, results: dict, errors: List[str]) -> dict:
        return {
            "status": status,
            "run_id": run_id,
            "graph_id": self.graph_data.get("id"),
            "graph_sha256": self.graph_sha256,
            "engine_profile": ENGINE_PROFILE,
            "results": results,
            "errors": errors,
        }

    @staticmethod
    def _load_state(stage_name: str) -> dict:
        state_path = Path("states") / f"{stage_name}.yaml"
        with state_path.open("r", encoding="utf-8") as handle:
            data = yaml.safe_load(handle)
        if not isinstance(data, dict):
            raise ValueError(f"invalid state definition: {state_path}")
        return data


def main() -> None:
    parser = argparse.ArgumentParser(description="Epistemic Pipeline execution engine")
    parser.add_argument("action", choices=["run", "validate"])
    parser.add_argument("graph")
    parser.add_argument("--resume-from", metavar="RUN_ID")
    parser.add_argument("--checkpoint-dir", default="checkpoints")
    parser.add_argument("--trace-dir", default="traces")
    args = parser.parse_args()

    engine = StateMachineEngine(
        args.graph,
        checkpoint_dir=args.checkpoint_dir,
        trace_dir=args.trace_dir,
    )

    if args.action == "validate":
        valid, errors = engine.validate()
        print(json.dumps({"valid": valid, "errors": errors}, ensure_ascii=False, indent=2))
        raise SystemExit(0 if valid else 1)

    result = engine.run(resume_from=args.resume_from)
    print(
        json.dumps(
            {
                "status": result["status"],
                "run_id": result.get("run_id"),
                "graph_sha256": result.get("graph_sha256"),
                "errors": result.get("errors", []),
            },
            ensure_ascii=False,
            indent=2,
        )
    )
    raise SystemExit(0 if result["status"] == "success" else 1)


if __name__ == "__main__":
    main()
