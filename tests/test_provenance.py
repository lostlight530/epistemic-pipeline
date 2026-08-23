#!/usr/bin/env python3
"""Optional local contract checks for provenance and evidence handoff.

These checks describe repository artifact semantics. They are not GitHub merge
policy and do not establish scientific validity or independent reproduction.
"""

from __future__ import annotations

import json
import os
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from core.evidence_envelope import (
    PROFILE as EVIDENCE_PROFILE,
    build_evidence_envelope,
    write_evidence_envelope,
)
from core.provenance import (
    PROFILE as PROV_PROFILE,
    PROV_NAMESPACE,
    build_run_provenance,
    write_provenance,
)
from core.run_bundle import run_bundle


class TestProvenanceProfile(unittest.TestCase):
    def test_builds_bounded_lineage_without_payload_copy(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            graph_path = root / "g.yaml"
            graph_path.write_text(
                "id: g\nnodes:\n"
                "  - id: discover\n    stage: discover\n    dependencies: []\n"
                "  - id: analyze\n    stage: analyze\n    dependencies: [discover]\n",
                encoding="utf-8",
            )
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
                    "discover": {
                        "status": "success",
                        "stage": "discover",
                        "outputs": {"secret": "payload-a"},
                    },
                    "analyze": {
                        "status": "success",
                        "stage": "analyze",
                        "outputs": {"claim": "payload-b"},
                    },
                },
            }

            record = build_run_provenance(str(graph_path), graph, result)

            self.assertEqual(record["profile"], PROV_PROFILE)
            self.assertEqual(PROV_PROFILE, "epistemic-pipeline/prov@2")
            self.assertEqual(record["prov_namespace"], PROV_NAMESPACE)
            self.assertFalse(record["scientific_validity_claim"])
            self.assertFalse(record["privacy"]["payloads_embedded"])
            self.assertTrue(record["relations"]["used"])
            self.assertTrue(record["relations"]["wasGeneratedBy"])
            self.assertTrue(record["relations"]["wasDerivedFrom"])
            self.assertTrue(record["relations"]["wasAssociatedWith"])

            graph_entities = [
                entity
                for entity in record["entities"].values()
                if entity.get("kind") == "dependency-graph"
            ]
            self.assertEqual(len(graph_entities), 1)
            self.assertTrue(graph_entities[0]["canonical_sha256"].startswith("sha256:"))
            self.assertTrue(graph_entities[0]["file_sha256"].startswith("sha256:"))

            rendered = json.dumps(record, ensure_ascii=False)
            self.assertNotIn("payload-a", rendered)
            self.assertNotIn("payload-b", rendered)
            self.assertIn("sha256:", rendered)

    def test_atomic_provenance_writer_creates_sidecar(self):
        with tempfile.TemporaryDirectory() as tmp:
            record = {"run_id": "r1", "profile": PROV_PROFILE}
            path = write_provenance(record, tmp)
            parsed = json.loads(Path(path).read_text(encoding="utf-8"))
            self.assertEqual(parsed["run_id"], "r1")
            self.assertEqual(parsed["profile"], PROV_PROFILE)


class TestEvidenceEnvelope(unittest.TestCase):
    def test_envelope_is_separate_handoff_contract(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            graph = root / "graph.yaml"
            provenance = root / "run.prov.json"
            graph.write_text("id: g\n", encoding="utf-8")
            provenance.write_text('{"profile":"epistemic-pipeline/prov@2"}\n', encoding="utf-8")

            envelope = build_evidence_envelope(
                run_id="r1",
                graph_id="g",
                status="success",
                graph_path=str(graph),
                graph_sha256="sha256:canonical-graph-placeholder",
                trace_path=None,
                checkpoint_path=None,
                provenance_path=str(provenance),
                trace_chain_internal_valid=None,
            )

            self.assertEqual(envelope["profile"], EVIDENCE_PROFILE)
            self.assertEqual(EVIDENCE_PROFILE, "epistemic-pipeline/evidence-envelope@1")
            self.assertEqual(envelope["reproducibility"]["level"], "R1")
            self.assertFalse(envelope["scientific_validity_claim"])
            self.assertFalse(envelope["payloads_embedded"])
            self.assertIn("not calibrated probability", envelope["confidence_semantics"])
            kinds = {artifact["kind"] for artifact in envelope["artifacts"]}
            self.assertIn("graph", kinds)
            self.assertIn("provenance", kinds)

            path = write_evidence_envelope(envelope, str(root / "evidence"))
            parsed = json.loads(Path(path).read_text(encoding="utf-8"))
            self.assertEqual(parsed["profile"], EVIDENCE_PROFILE)


class TestRunBundle(unittest.TestCase):
    def test_linear_mock_run_emits_provenance_and_evidence_sidecars(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            result = run_bundle(
                "graphs/linear.yaml",
                trace_dir=str(root / "traces"),
                checkpoint_dir=str(root / "checkpoints"),
                provenance_dir=str(root / "provenance"),
                evidence_dir=str(root / "evidence"),
            )

            self.assertEqual(result["status"], "success")
            self.assertTrue(result["graph_sha256"].startswith("sha256:"))

            provenance_path = Path(result["provenance_path"])
            evidence_path = Path(result["evidence_envelope_path"])
            self.assertTrue(provenance_path.exists())
            self.assertTrue(evidence_path.exists())

            provenance = json.loads(provenance_path.read_text(encoding="utf-8"))
            evidence = json.loads(evidence_path.read_text(encoding="utf-8"))

            self.assertEqual(provenance["profile"], PROV_PROFILE)
            self.assertEqual(provenance["run_id"], result["run_id"])
            self.assertEqual(
                provenance.get("integrity", {}).get("trace_chain_internal_valid"),
                True,
            )
            self.assertIn(
                "internal hash/link consistency",
                provenance.get("integrity", {}).get("semantics", ""),
            )

            self.assertEqual(evidence["profile"], EVIDENCE_PROFILE)
            self.assertEqual(evidence["run_id"], result["run_id"])
            self.assertEqual(evidence["reproducibility"]["level"], "R1")
            self.assertFalse(evidence["scientific_validity_claim"])
            kinds = {artifact["kind"] for artifact in evidence["artifacts"]}
            self.assertTrue({"graph", "trace", "checkpoint", "provenance"}.issubset(kinds))


if __name__ == "__main__":
    unittest.main()
