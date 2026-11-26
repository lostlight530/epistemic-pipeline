"""Downstream-facing claim and evidence handoff contracts, without truth transfer."""
import hashlib
import json
import subprocess
import sys
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


    def test_claim_transfer_distinguishes_omitted_and_empty_selection(self):
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            source = root / "claim-verification.json"
            claims = [{"claim_id": "c1"}, {"claim_id": "c2"}]
            source.write_text(json.dumps({
                "profile": "epistemic-pipeline/claim-verification",
                "run_id": "selection-fixture",
                "claims": claims,
            }), encoding="utf-8")

            all_claims = build_claim_transfer(source)
            self.assertEqual(
                [item["claim_id"] for item in all_claims["claims"]],
                ["c1", "c2"],
            )

            for invalid_selection in ([], [""], ["c1", ""], "c1"):
                with self.subTest(invalid_selection=invalid_selection):
                    with self.assertRaisesRegex(ValueError, "claim_ids"):
                        build_claim_transfer(source, claim_ids=invalid_selection)

            rejected_output = root / "rejected.json"
            rejected = subprocess.run(
                [
                    sys.executable, str(ROOT / "core" / "claim_transfer.py"),
                    str(source), "--claim-id", "", "--output", str(rejected_output),
                ],
                cwd=ROOT, capture_output=True, text=True,
            )
            self.assertEqual(rejected.returncode, 1)
            self.assertIn("claim-transfer: claim_ids", rejected.stderr)
            self.assertNotIn("Traceback", rejected.stderr)
            self.assertFalse(rejected_output.exists())

            all_output = root / "all.json"
            omitted = subprocess.run(
                [
                    sys.executable, str(ROOT / "core" / "claim_transfer.py"),
                    str(source), "--output", str(all_output),
                ],
                cwd=ROOT, capture_output=True, text=True,
            )
            self.assertEqual(omitted.returncode, 0, omitted.stderr)
            transferred = json.loads(all_output.read_text(encoding="utf-8"))
            self.assertEqual(
                [item["claim_id"] for item in transferred["claims"]],
                ["c1", "c2"],
            )

    def test_claim_transfer_rejects_malformed_source_shapes_without_data_loss(self):
        malformed = [
            ("claims-object", {"claims": {"c1": {"claim_id": "c1"}}}, "claims"),
            ("claim-item", {"claims": ["not-an-object"]}, "claims\\[0\\]"),
            ("claim-id", {"claims": [{"claim_id": ""}]}, "claim_id"),
            ("conflict-item", {"claims": [{"claim_id": "c1", "conflicts": [7]}]},
             "conflicts"),
            ("observations", {"claims": [{"claim_id": "c1", "observations": [1]}]},
             "observations"),
            ("heuristic-scores", {"claims": [{"claim_id": "c1", "heuristic_scores": 7}]},
             "heuristic_scores"),
            ("conflicts", {"claims": [{"claim_id": "c1", "conflicts": {"other": "c2"}}]},
             "conflicts"),
            ("origins-string", {"claims": [{"claim_id": "c1", "origin_state_ids": "verify"}]},
             "origin_state_ids"),
            ("hash-null-item", {"claims": [{"claim_id": "c1", "claim_record_sha256s": [None]}]},
             "claim_record_sha256s"),
            ("source-refs-string", {"claims": [{"claim_id": "c1", "source_refs": "source:1"}]},
             "source_refs"),
            ("evidence-refs-object", {"claims": [{"claim_id": "c1", "evidence_refs": {"id": "e:1"}}]},
             "evidence_refs"),
            ("evidence-relations-number", {"claims": [{"claim_id": "c1", "evidence_relations": [7]}]},
             "evidence_relations"),
            ("origin-ambiguity-string", {"claims": [{"claim_id": "c1", "claim_origin_ambiguous": "false"}]},
             "claim_origin_ambiguous"),
            ("identity-ambiguity-null", {"claims": [{"claim_id": "c1", "claim_identity_ambiguous": None}]},
             "claim_identity_ambiguous"),
        ]
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            source = root / "claim-verification.json"
            output = root / "claim-transfer.json"
            for name, malformed_fields, message in malformed:
                with self.subTest(name=name):
                    source.write_text(json.dumps({
                        "profile": "epistemic-pipeline/claim-verification",
                        **malformed_fields,
                    }), encoding="utf-8")
                    with self.assertRaisesRegex(ValueError, message):
                        build_claim_transfer(source)
                    result = subprocess.run(
                        [sys.executable, str(ROOT / "core" / "claim_transfer.py"),
                         str(source), "--output", str(output)],
                        cwd=ROOT, capture_output=True, text=True,
                    )
                    self.assertEqual(result.returncode, 1, result.stderr)
                    self.assertNotIn("Traceback", result.stderr)
                    self.assertFalse(output.exists())

            # An explicitly empty or absent collection remains valid
            for payload in ({"claims": []}, {"claims": None}, {}):
                source.write_text(json.dumps({
                    "profile": "epistemic-pipeline/claim-verification", **payload,
                }), encoding="utf-8")
                result = build_claim_transfer(source)
                self.assertEqual(result["claims"], [])
                self.assertEqual(result["transfer_coverage"]["selected_claim_count"], 0)
                self.assertIsNone(result["transfer_coverage"]["evidence_reference_ratio"])

    def test_claim_transfer_preserves_valid_reference_and_ambiguity_shapes(self):
        with tempfile.TemporaryDirectory() as td:
            source = Path(td) / "claim-verification.json"
            references = {
                "origin_state_ids": ["verify", "synthesize"],
                "claim_record_sha256s": ["sha256:a", "sha256:b"],
                "source_refs": ["source:1"],
                "evidence_refs": ["evidence:1"],
                "evidence_relations": ["supports"],
                "claim_origin_ambiguous": True,
                "claim_identity_ambiguous": False,
            }
            source.write_text(json.dumps({
                "profile": "epistemic-pipeline/claim-verification",
                "claims": [{"claim_id": "c1", **references}, {
                    "claim_id": "c2", "origin_state_ids": None, "evidence_refs": None,
                }],
            }), encoding="utf-8")
            first, second = build_claim_transfer(source)["claims"]
            for field, value in references.items():
                self.assertEqual(first[field], value, field)
            self.assertEqual(second["origin_state_ids"], [])
            self.assertEqual(second["evidence_refs"], [])
            self.assertFalse(second["claim_origin_ambiguous"])
            self.assertFalse(second["claim_identity_ambiguous"])

    def test_envelope_claim_index_preserves_duplicate_record_identity(self):
        from core.provenance import canonical_sha256
        from core.run_bundle import _build_claim_index
        from core.claim_audit import build_claim_verification

        first = {"claim_id": "reused", "statement": "version A",
                 "source_refs": ["source:a"]}
        second = {"claim_id": "reused", "statement": "version B",
                  "source_refs": ["source:b"]}
        unique = {"claim_id": "unique", "statement": "stable"}
        run_result = {"results": {
            "analyze": {"outputs": {"claims_registry": [first, unique]}},
            "verify": {"outputs": {
                "claims_registry": [second],
                "evidence_chains": [{"claim_id": "reused",
                                     "evidence_refs": ["evidence:1"]}],
            }},
        }}
        audited = {entry["claim_id"]: entry
                   for entry in build_claim_verification(run_result)["claims"]}
        indexed = {entry["claim_id"]: entry for entry in _build_claim_index(run_result)}
        self.assertEqual(set(indexed), {"reused", "unique"})
        ambiguous = indexed["reused"]
        self.assertEqual(ambiguous["origin_state_ids"], ["analyze", "verify"])
        self.assertEqual(ambiguous["origin_state_ids"], audited["reused"]["origin_state_ids"])
        self.assertTrue(ambiguous["claim_origin_ambiguous"])
        self.assertIsNone(ambiguous["state_id"])
        self.assertEqual(
            ambiguous["claim_record_sha256s"],
            sorted([canonical_sha256(first), canonical_sha256(second)]),
        )
        self.assertTrue(ambiguous["claim_identity_ambiguous"])
        self.assertEqual(ambiguous["claim_record_sha256s"], audited["reused"]["claim_record_sha256s"])
        self.assertIsNone(ambiguous["claim_record_sha256"])
        self.assertEqual(ambiguous["source_refs"], ["source:a", "source:b"])
        self.assertEqual(ambiguous["evidence_refs"], ["evidence:1"])

        stable = indexed["unique"]
        self.assertEqual(stable["origin_state_ids"], ["analyze"])
        self.assertEqual(stable["state_id"], "analyze")
        self.assertEqual(stable["claim_record_sha256s"], [canonical_sha256(unique)])
        self.assertEqual(stable["claim_record_sha256"], canonical_sha256(unique))
        self.assertFalse(stable["claim_origin_ambiguous"])
        self.assertFalse(stable["claim_identity_ambiguous"])

        with tempfile.TemporaryDirectory() as td:
            graph = Path(td) / "graph.yaml"
            graph.write_text("id: fixture\nnodes: []\n", encoding="utf-8")
            envelope = build_evidence_envelope(
                run_id="identity-fixture", graph_id="fixture", status="success",
                graph_path=str(graph), graph_canonical_sha256=None,
                graph_file_sha256=None, trace_path=None, checkpoint_path=None,
                provenance_path=None, trace_chain_internal_valid=None,
                claim_index=indexed.values(),
            )
        envelope_claims = {
            entry["claim_id"]: entry
            for entry in envelope["claim_observability"]["claims"]
        }
        self.assertEqual(envelope_claims["reused"]["origin_state_ids"],
                         ["analyze", "verify"])
        self.assertEqual(envelope_claims["reused"]["claim_record_sha256s"],
                         ambiguous["claim_record_sha256s"])
        self.assertTrue(envelope_claims["reused"]["claim_origin_ambiguous"])
        self.assertTrue(envelope_claims["reused"]["claim_identity_ambiguous"])
        self.assertIsNone(envelope_claims["reused"]["state_id"])
        self.assertIsNone(envelope_claims["reused"]["claim_record_sha256"])
        self.assertFalse(envelope["scientific_validity_claim"])

    def test_codemeta_v4_citation_identity_stays_consistent(self):
        meta = json.loads((ROOT / "codemeta.json").read_text(encoding="utf-8"))
        cff = yaml.safe_load((ROOT / "CITATION.cff").read_text(encoding="utf-8"))
        self.assertEqual(meta["@context"], "https://w3id.org/codemeta/4.0")
        self.assertEqual(meta["codeRepository"], cff["repository-code"])
        self.assertEqual(meta["identifier"], "https://doi.org/" + cff["identifiers"][0]["value"])
        self.assertNotIn("relatedSoftware", meta)


if __name__ == "__main__":
    unittest.main()
