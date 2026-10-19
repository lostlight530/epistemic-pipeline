#!/usr/bin/env python3
"""Native Tool/CLI/agent-plan contract tests; not a scientific validation."""
import json
import os
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import tool_cli

ROOT = Path(__file__).resolve().parents[1]


class ToolInterfaceTests(unittest.TestCase):
    def test_catalog_exposes_only_allowlisted_schemas(self):
        self.assertEqual(len(tool_cli.TOOL_DEFINITIONS), 2)
        self.assertTrue(all(tool["inputSchema"]["type"] == "object"
                            for tool in tool_cli.TOOL_DEFINITIONS))

    def test_unknown_tool_fails_closed(self):
        response = tool_cli.invoke("unregistered.remote_exec", {})
        self.assertEqual(response["status"], "failed")
        self.assertEqual(response["error"]["type"], "ValueError")
        self.assertFalse(response["scientific_validity_claim"])

    def test_invalid_argument_shape_fails_closed(self):
        tool = tool_cli.TOOL_DEFINITIONS[0]["name"]
        self.assertEqual(tool_cli.invoke(tool, [])["status"], "failed")
        self.assertEqual(tool_cli.invoke(tool, {"unexpected": "yes"})["status"], "failed")

    def test_agent_plan_stops_on_first_failure(self):
        result = tool_cli.run_plan({"steps": [
            {"id": "bad", "tool": "unknown", "arguments": {}},
            {"id": "not-executed", "tool": "unknown", "arguments": {}},
        ]})
        self.assertEqual(result["status"], "failed")
        self.assertEqual(result["completed_steps"], 1)
        self.assertEqual(result["requested_steps"], 2)
        self.assertEqual(result["steps"][0]["id"], "bad")

    def test_agent_rejects_duplicate_ids_and_unbounded_plans(self):
        with self.assertRaises(ValueError):
            tool_cli.run_plan({"steps": [
                {"id": "x", "tool": "x", "arguments": {}},
                {"id": "x", "tool": "x", "arguments": {}},
            ]})
        with self.assertRaises(ValueError):
            tool_cli.run_plan({"steps": []})
        with self.assertRaises(ValueError):
            tool_cli.run_plan({"steps": [
                {"id": str(i), "tool": "unknown", "arguments": {}} for i in range(33)
            ]})

    def test_cli_list_and_atomic_receipt(self):
        with tempfile.TemporaryDirectory() as root:
            output = Path(root) / "receipt.json"
            listed = subprocess.run(
                [sys.executable, "tool_cli.py", "list", "--output", str(output)],
                cwd=ROOT, capture_output=True, text=True, check=True,
            )
            self.assertEqual(json.loads(listed.stdout)["profile"],
                             tool_cli.REPOSITORY + "/tool-catalog")
            self.assertEqual(json.loads(output.read_text())["tools"],
                             tool_cli.TOOL_DEFINITIONS)

    def test_real_graph_tool_and_agent_execution(self):
        graph = [
            {"id": "a", "dependencies": []},
            {"id": "b", "dependencies": ["a"]},
            {"id": "c", "dependencies": ["a"]},
            {"id": "d", "dependencies": ["b", "c"]},
        ]
        r = tool_cli.invoke("graph.inspect", {"nodes": graph})
        self.assertEqual(r["status"], "success", r)
        self.assertEqual(r["output"]["parallel_groups"], [["a"], ["b", "c"], ["d"]])
        self.assertFalse(r["output"]["scientific_validity_claim"])
        plan = tool_cli.run_plan({"steps": [
            {"id": "graph", "tool": "graph.inspect", "arguments": {"nodes": graph}},
        ]})
        self.assertEqual(plan["status"], "success")
        self.assertEqual(plan["completed_steps"], 1)

    def test_cyclic_graph_is_reported_not_treated_as_execution_failure(self):
        result = tool_cli.invoke("graph.inspect", {"nodes": [
            {"id": "a", "dependencies": ["b"]},
            {"id": "b", "dependencies": ["a"]},
        ]})
        self.assertEqual(result["status"], "success", result)
        self.assertFalse(result["output"]["valid"])
        self.assertTrue(result["output"]["cycles"])



if __name__ == "__main__":
    unittest.main()
