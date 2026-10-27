#!/usr/bin/env python3
"""Contract tests for the opt-in, allowlisted local Tool/CLI/Agent surface."""
from __future__ import annotations

import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from agent_tools import PROFILE, list_tool_names, tool_definitions, execute_tool_call
from tool_cli import _html_report, _human


ROOT = Path(__file__).resolve().parents[1]


class TestToolContract(unittest.TestCase):
    def test_registry_declarations_are_allowlisted(self):
        declarations = tool_definitions()
        names = [item["function"]["name"] for item in declarations]
        self.assertEqual(sorted(names), list_tool_names())
        self.assertEqual(len(names), 2)
        for item in declarations:
            schema = item["function"]["parameters"]
            self.assertEqual(item["type"], "function")
            self.assertFalse(schema["additionalProperties"])

    def test_unknown_and_invalid_arguments_fail_closed(self):
        unknown = execute_tool_call("arbitrary_python", {})
        self.assertEqual(unknown["error"]["code"], "UNKNOWN_TOOL")
        self.assertFalse(unknown["remote_provider_called"])
        self.assertFalse(unknown["scientific_validity_claim"])
        name = list_tool_names()[0]
        malformed = execute_tool_call(name, "{broken")
        self.assertEqual(malformed["error"]["code"], "INVALID_ARGUMENT")
        hidden = execute_tool_call(name, {"unsafe_cmd": "rm -rf /"})
        self.assertEqual(hidden["error"]["code"], "INVALID_ARGUMENT")

    def test_nested_claim_ids_preflight_fails_before_execution(self):
        from agent_plan import run_plan
        invalid_ids = [[7], [""], [], ["claim-1", None]]
        for claim_ids in invalid_ids:
            arguments = {"claim_audit": "not-opened.json", "claim_ids": claim_ids}
            with self.subTest(claim_ids=claim_ids):
                direct = execute_tool_call("claim_transfer", arguments)
                self.assertEqual(direct["error"]["code"], "INVALID_ARGUMENT")
                plan = {"steps": [{"tool": "claim_transfer", "arguments": arguments}]}
                preview = run_plan(plan)
                self.assertEqual(preview["error"]["code"], "INVALID_PLAN")
                self.assertFalse(preview["approval_granted"])
        valid = {"steps": [{"tool": "claim_transfer", "arguments": {
            "claim_audit": "not-opened.json", "claim_ids": ["claim-1"],
        }}]}
        self.assertEqual(run_plan(valid)["status"], "approval_required")

    def test_cli_registry_machine_json_and_offline_html(self):
        proc = subprocess.run(
            [sys.executable, str(ROOT / "tool_cli.py"), "list"],
            text=True, capture_output=True, check=True, cwd=ROOT,
        )
        parsed = json.loads(proc.stdout)
        self.assertEqual(parsed["profile"], PROFILE)
        self.assertEqual(len(parsed["result"]["tools"]), 2)
        self.assertNotIn("\x1b", proc.stdout)
        self.assertEqual(proc.stderr, "")
        with tempfile.TemporaryDirectory() as temp:
            path = Path(temp) / "report.html"
            proc = subprocess.run(
                [sys.executable, str(ROOT / "tool_cli.py"), "list",
                 "--format", "html", "--output", str(path)],
                text=True, capture_output=True, check=True, cwd=ROOT,
            )
            self.assertEqual(proc.stdout, "")
            report = path.read_text(encoding="utf-8")
            self.assertIn("<!doctype html>", report)
            self.assertIn("@media(prefers-color-scheme:dark)", report)
            self.assertNotIn("<script", report)
            malicious = _html_report({"profile": PROFILE, "tool": "<script>alert(1)</script>",
                                      "status": "error", "result": None, "error": None})
            self.assertNotIn("<script>alert(1)</script>", malicious)
            self.assertIn("&lt;script&gt;", malicious)
            self.assertNotIn("\x1b", _human(parsed, color=False))

    def test_cli_invalid_arguments_machine_failure(self):
        name = list_tool_names()[0]
        proc = subprocess.run(
            [sys.executable, str(ROOT / "tool_cli.py"), "invoke", name,
             "--args", '{"unexpected":true}'],
            text=True, capture_output=True, cwd=ROOT,
        )
        self.assertEqual(proc.returncode, 1)
        parsed = json.loads(proc.stdout)
        self.assertEqual(parsed["error"]["code"], "INVALID_ARGUMENT")


    def test_cli_output_cannot_replace_source_or_request_inputs(self):
        with tempfile.TemporaryDirectory() as temp:
            source = Path(temp) / "source.json"
            source.write_text("{\"profile\":\"epistemic-pipeline/claim-verification\",\"claims\":[]}", encoding="utf-8")
            original = source.read_bytes()
            arguments = {"claim_audit": str(source)}
            request_file = Path(temp) / "request.json"
            request_file.write_text(json.dumps(arguments), encoding="utf-8")
            request_original = request_file.read_bytes()
            base = [sys.executable, str(ROOT / "tool_cli.py"), "invoke", "claim_transfer"]
            for options, destination in (
                (["--args", json.dumps(arguments)], source),
                (["--args-file", str(request_file)], request_file),
            ):
                completed = subprocess.run(
                    base + options + ["--output", str(destination)],
                    cwd=ROOT, text=True, capture_output=True,
                )
                self.assertEqual(completed.returncode, 2, completed.stderr)
                self.assertIn("must not overwrite an input file", completed.stderr)
                self.assertEqual(source.read_bytes(), original)
                self.assertEqual(request_file.read_bytes(), request_original)

            plan_file = Path(temp) / "plan.json"
            plan_file.write_text(json.dumps({"steps": [
                {"tool": "claim_transfer", "arguments": arguments}
            ]}), encoding="utf-8")
            plan_original = plan_file.read_bytes()
            preview = subprocess.run(
                [sys.executable, str(ROOT / "tool_cli.py"), "plan",
                 "--plan-file", str(plan_file), "--output", str(plan_file)],
                cwd=ROOT, text=True, capture_output=True,
            )
            self.assertEqual(preview.returncode, 2, preview.stderr)
            self.assertIn("must not overwrite an input file", preview.stderr)
            self.assertEqual(plan_file.read_bytes(), plan_original)
            self.assertEqual(source.read_bytes(), original)



class TestRepoIntegration(unittest.TestCase):
    def test_graph_inspection_and_domain_failure(self):
        valid = execute_tool_call("graph_inspect",
                                  {"graph": str(ROOT / "graphs" / "diamond.yaml")})
        self.assertEqual(valid["status"], "ok", valid.get("error"))
        self.assertTrue(valid["result"]["valid"])
        self.assertGreater(len(valid["result"]["parallel_groups"]), 1)
        with tempfile.TemporaryDirectory() as temp:
            path = Path(temp) / "cycle.yaml"
            path.write_text(
                "id: cyclic\nnodes:\n"
                "  - id: a\n    dependencies: [b]\n"
                "  - id: b\n    dependencies: [a]\n",
                encoding="utf-8",
            )
            invalid = execute_tool_call("graph_inspect", {"graph": str(path)})
            self.assertEqual(invalid["status"], "ok")
            self.assertFalse(invalid["result"]["valid"])
            proc = subprocess.run(
                [sys.executable, str(ROOT / "tool_cli.py"), "invoke", "graph_inspect",
                 "--args", json.dumps({"graph": str(path)})],
                capture_output=True, text=True, cwd=ROOT,
            )
            self.assertEqual(proc.returncode, 1)

    def test_claim_transfer_rejects_wrong_source(self):
        with tempfile.TemporaryDirectory() as temp:
            path = Path(temp) / "wrong.json"
            path.write_text('{"profile":"wrong"}', encoding="utf-8")
            value = execute_tool_call("claim_transfer", {"claim_audit": str(path)})
            self.assertEqual(value["status"], "error")



    def test_handoff_cli_preserves_source_when_output_collides(self):
        with tempfile.TemporaryDirectory() as temp:
            source = Path(temp) / "source.json"
            original = json.dumps({"profile": "epistemic-pipeline/claim-verification"}).encode("utf-8")
            source.write_bytes(original)
            command = [sys.executable, str(ROOT / "core" / "claim_transfer.py"), str(source)]
            rejected = subprocess.run(
                command + ["--output", str(source)],
                cwd=ROOT, capture_output=True, text=True,
            )
            self.assertNotEqual(rejected.returncode, 0)
            self.assertIn("claim transfer output must not overwrite", rejected.stderr)
            self.assertEqual(source.read_bytes(), original)

            output = Path(temp) / "handoff.json"
            accepted = subprocess.run(
                command + ["--output", str(output)],
                cwd=ROOT, capture_output=True, text=True,
            )
            self.assertEqual(accepted.returncode, 0, accepted.stderr)
            self.assertTrue(output.is_file())
            self.assertEqual(source.read_bytes(), original)

    def test_handoff_cli_does_not_clobber_legacy_temp_name(self):
        with tempfile.TemporaryDirectory() as temp:
            output = Path(temp) / "handoff.json"
            source = Path(temp) / "handoff.json.tmp"
            original = json.dumps({"profile": "epistemic-pipeline/claim-verification"}).encode("utf-8")
            source.write_bytes(original)
            command = [sys.executable, str(ROOT / "core" / "claim_transfer.py"), str(source)]
            completed = subprocess.run(
                command + ["--output", str(output)],
                cwd=ROOT, capture_output=True, text=True,
            )
            self.assertEqual(completed.returncode, 0, completed.stderr)
            self.assertTrue(output.is_file())
            self.assertEqual(source.read_bytes(), original)



    def test_maintenance_report_output_cannot_overwrite_inspected_files(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            (root / "maintenance").mkdir()
            config = root / "maintenance" / "cadence.yaml"
            config.write_text(json.dumps({
                "project_profile_prefix": "epistemic-pipeline/",
                "canonical_paths": [],
                "scan_paths": [],
                "forbidden_governance_paths": [],
                "history_patterns": [],
                "cadences": {"daily": {"calibration_max_age_days": 0}},
            }), encoding="utf-8")
            manifest = root / "MANIFEST.yaml"
            manifest.write_text('calibrated: "2026-10-01"\n', encoding="utf-8")
            existing = root / "research-notes.json"
            existing.write_text('{"private":"must survive"}', encoding="utf-8")

            command = [
                sys.executable, str(ROOT / "core" / "maintenance_cadence.py"),
                "daily", "--root", str(root), "--config", "maintenance/cadence.yaml",
                "--as-of", "2026-10-26",
            ]
            for protected in (config, manifest, existing):
                with self.subTest(protected=protected.name):
                    original = protected.read_bytes()
                    attempt = subprocess.run(
                        command + ["--output", str(protected)],
                        cwd=ROOT, capture_output=True, text=True,
                    )
                    self.assertNotEqual(attempt.returncode, 0)
                    self.assertIn("not an existing maintenance report", attempt.stderr)
                    self.assertEqual(protected.read_bytes(), original)

            report = root / "maintenance-report.json"
            for _ in range(2):
                allowed = subprocess.run(
                    command + ["--output", str(report)],
                    cwd=ROOT, capture_output=True, text=True,
                )
                self.assertEqual(allowed.returncode, 0, allowed.stderr)
                self.assertEqual(json.loads(report.read_text(encoding="utf-8"))["profile"],
                                 "epistemic-pipeline/maintenance-report")
            self.assertEqual(config.read_text(encoding="utf-8"),
                             json.dumps({
                                "project_profile_prefix": "epistemic-pipeline/",
                                "canonical_paths": [],
                                "scan_paths": [],
                                "forbidden_governance_paths": [],
                                "history_patterns": [],
                                "cadences": {"daily": {"calibration_max_age_days": 0}},
                             }))


if __name__ == "__main__":
    unittest.main()
