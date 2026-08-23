#!/usr/bin/env python3
"""Optional local contract checks for the current epistemic-pipeline architecture.

These checks are maintenance aids only. They do not represent GitHub merge
policy or scientific validation.
"""

from __future__ import annotations

import json
import os
import sys
import tempfile
from pathlib import Path

import yaml

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))


def test_manifest_exists():
    manifest = yaml.safe_load(Path("MANIFEST.yaml").read_text(encoding="utf-8"))
    assert manifest["engine"]["profile"] == "epistemic-pipeline/engine@2"
    assert manifest["runtime_policy"]["active_state_key"] == "runtime_policies"
    assert manifest["runtime_dependencies"]["required"] == ["pyyaml"]
    print("  [OK] manifest reflects current profiles and dependencies")


def test_states_use_runtime_policies():
    for state in ["discover", "analyze", "verify", "synthesize", "archive"]:
        data = yaml.safe_load(Path(f"states/{state}.yaml").read_text(encoding="utf-8"))
        assert data["id"] == state
        assert "activities" in data
        assert "runtime_policies" in data
        assert "quality_gates" not in data
        for policy in data["runtime_policies"]:
            assert policy.get("id")
            assert policy.get("check")
    print("  [OK] active state definitions use machine-readable runtime policies")


def test_roles_and_graph_assets_exist():
    for role in ["explorer", "analyst", "verifier", "synthesizer", "auditor"]:
        assert Path(f"roles/{role}.md").is_file()
    for graph in ["linear", "parallel", "diamond", "adaptive"]:
        assert Path(f"graphs/{graph}.yaml").is_file()
    print("  [OK] role and graph assets exist")


def test_dependency_graph_validation():
    from core.dependency_graph import DependencyGraph

    valid = DependencyGraph([
        {"id": "A", "dependencies": []},
        {"id": "B", "dependencies": ["A"]},
        {"id": "C", "dependencies": ["A"]},
        {"id": "D", "dependencies": ["B", "C"]},
    ])
    ok, errors = valid.validate()
    assert ok, errors
    groups = valid.find_parallel_groups()
    assert any("B" in group and "C" in group for group in groups)

    duplicate = DependencyGraph([
        {"id": "A", "dependencies": []},
        {"id": "A", "dependencies": []},
    ])
    ok, errors = duplicate.validate()
    assert not ok
    assert any("重复" in error or "duplicate" in error.lower() for error in errors)

    missing = DependencyGraph([
        {"id": "A", "dependencies": ["missing"]},
    ])
    ok, errors = missing.validate()
    assert not ok
    assert any("missing" in error for error in errors)
    print("  [OK] dependency graph rejects duplicate/missing structural identity")


def test_runtime_policy_evaluator():
    from core.gatekeeper import Gatekeeper, RuntimePolicyEvaluator

    state = {
        "runtime_policies": [
            {"id": "sources", "check": "min_items", "field": "sources", "min": 1}
        ]
    }
    evaluator = RuntimePolicyEvaluator()
    passed, errors = evaluator.evaluate(state, {"sources": ["s1"]})
    assert passed and not errors

    passed, errors = evaluator.evaluate(state, {})
    assert not passed
    assert "MISSING_POLICY_INPUT" in errors

    legacy = Gatekeeper()
    passed, errors = legacy.check_quality_gates(
        {"quality_gates": [{"id": "x", "check": "non_empty", "field": "x"}]},
        {"x": [1]},
    )
    assert passed and not errors
    print("  [OK] runtime policy is active; historical Gatekeeper API remains compatible")


def test_confidence_network_is_bounded_heuristic():
    from core.confidence_net import ConfidenceNetwork

    net = ConfidenceNetwork(threshold=0.01, max_iterations=100)
    net.add_node("claim_A", 0.7)
    net.add_node("claim_B", 0.6)
    net.add_edge("claim_A", "claim_B", 0.8, "supports")
    final, iterations, converged = net.converge()
    assert iterations <= 100
    assert converged
    assert all(0.0 <= value <= 1.0 for value in final.values())
    report = net.get_report()
    assert "not_calibrated_probability" in report["score_semantics"]

    try:
        net.add_node("bad", 1.5)
        raise AssertionError("out-of-range score should fail")
    except ValueError:
        pass
    print("  [OK] score propagation stays bounded and explicitly heuristic")


def test_temperature_transform_has_no_probability_claim():
    from core.calibration import calibrate_confidence_map, temperature_scale

    assert abs(temperature_scale(0.5, 1.0) - 0.5) < 1e-12
    values = calibrate_confidence_map({"a": 0.2, "b": 0.8}, 2.0)
    assert 0.0 <= values["a"] <= 1.0
    assert 0.0 <= values["b"] <= 1.0
    assert values["a"] < values["b"]
    print("  [OK] temperature transform is a bounded monotonic numeric transform")


def test_engine_mock_run_uses_runtime_policy_and_graph_digest():
    from core.engine import StateMachineEngine

    engine = StateMachineEngine("graphs/linear.yaml")
    result = engine.run()
    assert result["status"] == "success", result.get("errors")
    assert result["engine_profile"] == "epistemic-pipeline/engine@2"
    assert result["graph_sha256"].startswith("sha256:")
    assert len(result["results"]) == 5
    for node_result in result["results"].values():
        assert node_result["runtime_policy_evaluated"] is True
        assert node_result["runtime_policy_passed"] is True
        assert "quality_gates_passed" not in node_result
    print("  [OK] engine uses runtime policy and content-sensitive graph identity")


def test_runtime_policy_blocks_empty_provider_output():
    from core.engine import StateMachineEngine

    class EmptyHarness:
        def execute(self, state_id, role_bindings, inputs, mock=True):
            return {}

    result = StateMachineEngine("graphs/linear.yaml", harness=EmptyHarness()).run()
    assert result["status"] == "failed"
    assert any("MISSING_POLICY_INPUT" in error for error in result["errors"])
    print("  [OK] missing structured output fails explicit runtime policy")


def test_engine_can_disable_runtime_policy_for_compatibility():
    from core.engine import StateMachineEngine

    class MinimalHarness:
        def execute(self, state_id, role_bindings, inputs, mock=True):
            return {}

    result = StateMachineEngine(
        "graphs/linear.yaml",
        use_runtime_policy=False,
        use_confidence_net=False,
        harness=MinimalHarness(),
    ).run()
    assert result["status"] == "success"
    assert all(
        node["runtime_policy_evaluated"] is False for node in result["results"].values()
    )
    print("  [OK] compatibility mode can explicitly disable runtime policy evaluation")


def test_checkpoint_binds_graph_digest():
    from core.engine import StateMachineEngine

    with tempfile.TemporaryDirectory() as tmp:
        root = Path(tmp)
        graph_a = root / "a.yaml"
        graph_b = root / "b.yaml"
        graph_a.write_text(
            "id: same\nnodes:\n  - id: discover\n    stage: discover\n    dependencies: []\n",
            encoding="utf-8",
        )
        graph_b.write_text(
            "id: same\nnodes:\n  - id: discover\n    stage: discover\n    dependencies: []\n    timeout_seconds: 1\n",
            encoding="utf-8",
        )
        checkpoint_dir = root / "checkpoints"
        first = StateMachineEngine(str(graph_a), checkpoint_dir=str(checkpoint_dir))
        first._write_checkpoint("r1", {"discover": {"status": "success", "outputs": {}}})
        second = StateMachineEngine(str(graph_b), checkpoint_dir=str(checkpoint_dir))
        try:
            second._load_checkpoint("r1")
            raise AssertionError("same graph id with different content must not resume")
        except ValueError as exc:
            assert "digest mismatch" in str(exc)
    print("  [OK] checkpoint resume binds graph id and canonical graph digest")


def test_adaptive_graph_is_explicitly_experimental():
    from core.engine import StateMachineEngine

    try:
        StateMachineEngine("graphs/adaptive.yaml")
        raise AssertionError("adaptive graph without executable nodes should be rejected")
    except ValueError as exc:
        assert "nodes" in str(exc)
    print("  [OK] adaptive specification remains outside the executable engine")


def test_experimental_boundaries_are_explicit():
    from core.infinite_regression import InfiniteRegressionLoop
    from core.neuro_symbolic import NeuralOutput, NeuroSymbolicBridge
    from core.perception import HTTPAnchor
    from core.thread_collapse import ThreadCollapseEngine

    loop = InfiniteRegressionLoop(max_depth=5)
    level = loop.run("x", lambda value, depth: value)
    assert level is not None and level.cycle_detected and not level.converged

    bridge = NeuroSymbolicBridge()
    result = bridge.bridge(NeuralOutput(pattern_id="p", confidence=0.5))
    assert "not_calibrated_probability" in result.score_semantics

    anchor = HTTPAnchor("http", {"url": "https://example.invalid"})
    import asyncio
    signals = asyncio.run(anchor.perceive())
    assert signals[0].metadata["network_io_performed"] is False

    aggregator = ThreadCollapseEngine(max_threads=2)
    thread_id = aggregator.spawn_thread("hypothesis")
    aggregator.add_evidence(thread_id, "e1", 0.2)
    assert aggregator.get_thread(thread_id).confidence == 0.2
    assert "not_probability" in aggregator.summary()["score_semantics"]
    print("  [OK] Experimental compatibility names expose bounded concrete semantics")


def main():
    tests = [value for name, value in globals().items() if name.startswith("test_")]
    passed = 0
    failed = 0
    for test in tests:
        try:
            test()
            passed += 1
        except Exception as exc:
            print(f"  [FAIL] {test.__name__}: {type(exc).__name__}: {exc}")
            failed += 1
    print(f"\n  {passed}/{passed + failed} local checks passed")
    raise SystemExit(0 if failed == 0 else 1)


if __name__ == "__main__":
    main()
