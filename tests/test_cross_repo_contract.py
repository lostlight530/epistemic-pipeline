"""Downstream-facing claim and evidence handoff contracts, without truth transfer."""
import hashlib
import json
import tempfile
import unittest
from pathlib import Path

import yaml

from core.claim_transfer import build_claim_transfer
from core.evidence_envelope import build_evidence_envelope

ROOT = Path(__file__).resolve().parents[1]


class CrossRepositoryContract(unittest.TestCase):
    def test_evidence_envelope_references_upstream_artifact_without_acceptance(self):
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            graph = root / "graph.yaml"
            graph.write_text("id: fixture\nnodes: []\n", encoding="utf-8")
            artifact = root / "auto-doc.artifact-record.json"
            artifact.write_text('{"profile":"auto-doc-engine/artifact-record"}', encoding="utf-8")
            envelope = build_evidence_envelope(
                run_id="interop-fixture", graph_id="fixture", status="success",
                graph_path=str(graph), graph_canonical_sha256="sha256:fixture",
                graph_file_sha256=None, trace_path=None, checkpoint_path=None,
                provenance_path=None, trace_chain_internal_valid=None,
                upstream_artifact_refs=[str(artifact)],
            )
            self.assertEqual(envelope["profile"], "epistemic-pipeline/evidence-envelope")
            inputs = envelope["upstream_inputs"]
            self.assertEqual(inputs["artifact_refs"][0]["file_sha256"],
                             "sha256:" + hashlib.sha256(artifact.read_bytes()).hexdigest())
            self.assertFalse(inputs["scientific_validity_inherited"])
            self.assertFalse(envelope["scientific_validity_claim"])
            self.assertIsNone(envelope["integrity"]["trace_chain_internal_valid"])

    def test_claim_transfer_preserves_ambiguity_and_disallows_truth_upgrade(self):
        with tempfile.TemporaryDirectory() as td:
            source = Path(td) / "claim-verification.json"
            claim = {
                "claim_id": "c1", "origin_state_id": "verify",
                "origin_state_ids": ["verify", "synthesize"],
                "claim_origin_ambiguous": True, "claim_record_sha256": "sha256:a",
                "claim_record_sha256s": ["sha256:a", "sha256:b"],
                "claim_identity_ambiguous": True, "source_refs": ["source:1"],
                "evidence_refs": ["evidence:1"], "conflicts": [{"kind": "unresolved"}],
                "observations": {}, "heuristic_scores": {"final": 0.7},
                "audit_state": "observed",
            }
            source.write_text(json.dumps({
                "profile": "epistemic-pipeline/claim-verification",
                "run_id": "interop-fixture", "claims": [claim],
            }), encoding="utf-8")
            handoff = build_claim_transfer(source, claim_ids=["c1"])
            self.assertEqual(handoff["profile"], "epistemic-pipeline/claim-transfer")
            selected = handoff["claims"][0]
            self.assertTrue(selected["claim_origin_ambiguous"])
            self.assertTrue(selected["claim_identity_ambiguous"])
            self.assertEqual(selected["conflicts"], claim["conflicts"])
            self.assertFalse(selected["transfer_constraints"]["scientific_validity_inherited"])
            self.assertFalse(handoff["acceptance_claim"])
            with self.assertRaises(ValueError):
                build_claim_transfer(source, claim_ids=["nonexistent"])

    def test_codemeta_v4_citation_identity_stays_consistent(self):
        meta = json.loads((ROOT / "codemeta.json").read_text(encoding="utf-8"))
        cff = yaml.safe_load((ROOT / "CITATION.cff").read_text(encoding="utf-8"))
        self.assertEqual(meta["@context"], "https://w3id.org/codemeta/4.0")
        self.assertEqual(meta["codeRepository"], cff["repository-code"])
        self.assertEqual(meta["identifier"], "https://doi.org/" + cff["identifiers"][0]["value"])
        self.assertNotIn("relatedSoftware", meta)


if __name__ == "__main__":
    unittest.main()
