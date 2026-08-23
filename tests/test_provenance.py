#!/usr/bin/env python3
"""Tests for the PROV-aligned research-run bundle."""

import json
import os
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from core.provenance import PROFILE, PROV_NAMESPACE, build_run_provenance, write_provenance
from core.run_bundle import run_bundle


class TestProvenanceProfile(unittest.TestCase):
    def test_builds_entity_activity_agent_lineage_without_payload_copy(self):
        graph = {
            "id": "g",
            "nodes": [
                {"id": "discover", "stage": "discover", "dependencies": []},
                {"id": "analyze", "stage": "analyze", "dependencies": ["discover"]},
            ],
        }
        result = {
            "status": "success",
            "run_id": "abc123",
            "results": {
                "discover": {"status": "success", "stage": "discover", "outputs": {"secret": "payload-a"}},
                "analyze": {"status": "success", "stage": "analyze", "outputs": {"claim": "payload-b"}},
            },
        }
        record = build_run_provenance("graphs/g.yaml", graph, result)

        self.assertEqual(record["profile"], PROFILE)
        self.assertEqual(record["prov_namespace"], PROV_NAMESPACE)
        self.assertIn("agents", record)
        self.assertTrue(record["relations"]["used"])
        self.assertTrue(record["relations"]["wasGeneratedBy"])
        self.assertTrue(record["relations"]["wasDerivedFrom"])
        rendered = json.dumps(record, ensure_ascii=False)
        self.assertNotIn("payload-a", rendered)
        self.assertNotIn("payload-b", rendered)
        self.assertIn("sha256:", rendered)

    def test_atomic_writer_creates_run_sidecar(self):
        with tempfile.TemporaryDirectory() as tmp:
            record = {"run_id": "r1", "profile": PROFILE}
            path = write_provenance(record, tmp)
            self.assertTrue(Path(path).exists())
            self.assertEqual(json.loads(Path(path).read_text(encoding="utf-8"))["run_id"], "r1")


class TestRunBundle(unittest.TestCase):
    def test_linear_mock_run_emits_provenance_bundle(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            result = run_bundle(
                "graphs/linear.yaml",
                trace_dir=str(root / "traces"),
                checkpoint_dir=str(root / "checkpoints"),
                provenance_dir=str(root / "provenance"),
            )
            self.assertEqual(result["status"], "success")
            prov_path = Path(result["provenance_path"])
            self.assertTrue(prov_path.exists())
            record = json.loads(prov_path.read_text(encoding="utf-8"))
            self.assertEqual(record["run_id"], result["run_id"])
            self.assertEqual(record["status"], "success")
            self.assertTrue(any(e.get("kind") == "node-output" for e in record["entities"].values()))
            self.assertEqual(record.get("integrity", {}).get("trace_hash_chain_valid"), True)


if __name__ == "__main__":
    unittest.main()
