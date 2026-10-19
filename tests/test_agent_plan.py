#!/usr/bin/env python3
"""Approval-first bounded plan execution contract for local Agent tools."""
from __future__ import annotations

import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from agent_tools import PROFILE, TOOL_SPECS
from agent_plan import MAX_PLAN_STEPS, run_plan


ROOT = Path(__file__).resolve().parents[1]


def fixture_plan(steps: int = 2, policy: str = "stop") -> dict:
    tool = sorted(TOOL_SPECS)[0]
    required = TOOL_SPECS[tool]["parameters"]["required"]
    args = {key: "nonexistent-local-test-path" for key in required}
    return {"purpose": "isolated test", "on_error": policy,
            "steps": [{"tool": tool, "arguments": args} for _ in range(steps)]}


def success_response() -> dict:
    return {"profile": PROFILE, "tool": "test", "status": "ok",
            "result": {"valid": True}, "error": None,
            "scientific_validity_claim": False}


class TestApprovedAgentPlan(unittest.TestCase):
    def test_preview_never_invokes_tools(self):
        with patch("agent_plan.execute_tool_call", side_effect=AssertionError("must not run")) as run:
            payload = run_plan(fixture_plan())
        run.assert_not_called()
        self.assertEqual(payload["status"], "approval_required")
        self.assertEqual(payload["error"]["code"], "APPROVAL_REQUIRED")
        self.assertFalse(payload["result"]["executed"])
        self.assertEqual(payload["result"]["step_count"], 2)

    def test_invalid_or_unbounded_plan_fails_before_tool_calls(self):
        invalid = [
            {"steps": []}, fixture_plan(MAX_PLAN_STEPS + 1),
            {"steps": [{"tool": "python_exec", "arguments": {}}]},
            {"steps": [{"tool": sorted(TOOL_SPECS)[0], "arguments": {"secret": "x"}}]},
            {"steps": "not a list"}, {"steps": fixture_plan()["steps"], "on_error": []},
            {"steps": fixture_plan()["steps"], "hidden": "run"},
        ]
        with patch("agent_plan.execute_tool_call", side_effect=AssertionError("must not run")) as run:
            for plan in invalid:
                result = run_plan(plan, approved=True)
                self.assertEqual(result["error"]["code"], "INVALID_PLAN", plan)
        run.assert_not_called()

    def test_approved_plan_executes_all_valid_steps_in_order(self):
        with patch("agent_plan.execute_tool_call", return_value=success_response()) as execute:
            result = run_plan(fixture_plan(3), approved=True)
        self.assertEqual(result["status"], "ok")
        self.assertTrue(result["approval_granted"])
        self.assertEqual(result["result"]["completed_steps"], 3)
        self.assertEqual(execute.call_count, 3)
        self.assertIsNone(result["result"]["failed_at"])

    def test_default_stop_and_explicit_continue_preserve_failures(self):
        failed = {**success_response(), "result": {"valid": False}}
        for policy, expected_calls in [("stop", 1), ("continue", 3)]:
            with patch("agent_plan.execute_tool_call", side_effect=[
                failed, success_response(), success_response()
            ]) as execute:
                result = run_plan(fixture_plan(3, policy), approved=True)
            self.assertEqual(result["status"], "error")
            self.assertEqual(result["error"]["code"], "STEP_FAILED")
            self.assertEqual(result["result"]["failed_at"], 0)
            self.assertEqual(execute.call_count, expected_calls)

    def test_cli_requires_approval_and_emits_only_json(self):
        with tempfile.TemporaryDirectory() as temp:
            path = Path(temp) / "plan.json"
            path.write_text(json.dumps(fixture_plan()), encoding="utf-8")
            proc = subprocess.run([
                sys.executable, str(ROOT / "tool_cli.py"), "plan",
                "--plan-file", str(path)
            ], text=True, capture_output=True, cwd=ROOT)
            self.assertEqual(proc.returncode, 1)
            data = json.loads(proc.stdout)
            self.assertEqual(data["status"], "approval_required")
            self.assertNotIn("\x1b", proc.stdout)
            self.assertEqual(proc.stderr, "")


if __name__ == "__main__":
    unittest.main()
