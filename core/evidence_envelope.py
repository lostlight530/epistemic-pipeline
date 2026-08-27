#!/usr/bin/env python3
"""Versioned evidence envelope for epistemic-pipeline research runs.

The envelope is a small project-owned interchange object that references the
run's graph, trace, checkpoint, provenance and claim-verification artifacts
without duplicating node payloads. It is intentionally separate from W3C PROV
semantics: PROV expresses lineage relationships, while this envelope expresses
the repository's cross-tool handoff contract and scientific-integrity
boundaries.

Version 2 retains two bounded audit surfaces introduced in the 2026-08 refresh:

- a claim-aware index containing claim identities plus source/evidence refs,
  never full claim prose;
- process disclosure for the provider path and declared human-review state.

The 2026-08-27 consolidation adds compatible references to a separate
``claim-verification@1`` sidecar and to optional upstream artifact/evidence
records. These references are deliberately additive: the Evidence Envelope
stays an index rather than becoming another research database.

None of these surfaces establishes truth, authorship, peer review, source
credibility, model validity, or scientific correctness.
"""

from __future__ import annotations

import json
import os
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, Iterable, Optional
from urllib.parse import urlsplit

from core.provenance import file_sha256

PROFILE = "epistemic-pipeline/evidence-envelope@2"
CLAIM_INDEX_PROFILE = "epistemic-pipeline/claim-index@1"
CLAIM_VERIFICATION_PROFILE = "epistemic-pipeline/claim-verification@1"
PROCESS_DISCLOSURE_PROFILE = "epistemic-pipeline/process-disclosure@1"
UPSTREAM_REFERENCE_PROFILE = "epistemic-pipeline/upstream-reference@1"
HUMAN_REVIEW_VALUES = {"reviewed", "partial", "not_reviewed", "not_declared"}


def _now() -> str:
    return datetime.now(timezone.utc).isoformat()


def _artifact_ref(kind: str, path: Optional[str]) -> Optional[dict]:
    if not path:
        return None
    digest = file_sha256(path)
    if not digest:
        return None
    return {"kind": kind, "path": str(path), "file_sha256": digest}


def _reference(kind: str, value: Any) -> Optional[dict]:
    """Normalize local files or opaque references without network access."""
    if value is None:
        return None
    text = str(value).strip()
    if not text:
        return None
    record = {"kind": kind, "ref": text}
    digest = file_sha256(text)
    if digest:
        record["resolution"] = "local-file"
        record["file_sha256"] = digest
        return record
    parsed = urlsplit(text)
    record["resolution"] = (
        "opaque-uri-not-dereferenced" if parsed.scheme else "opaque-reference-not-resolved"
    )
    return record


def _reference_list(kind: str, values: Optional[Iterable[Any]]) -> list[dict]:
    records: list[dict] = []
    seen: set[str] = set()
    for value in values or []:
        text = str(value).strip()
        if not text or text in seen:
            continue
        record = _reference(kind, text)
        if record:
            records.append(record)
            seen.add(text)
    return records


def _string_list(value: Any) -> list[str]:
    if not isinstance(value, (list, tuple, set)):
        return []
    result = []
    seen = set()
    for item in value:
        text = str(item).strip()
        if text and text not in seen:
            result.append(text)
            seen.add(text)
    return result


def _normalize_claim_index(records: Optional[Iterable[dict]]) -> list[dict]:
    """Keep only portable claim identity/ref fields and never claim prose."""
    normalized = []
    for record in records or []:
        if not isinstance(record, dict):
            continue
        claim_id = str(record.get("claim_id") or "").strip()
        if not claim_id:
            continue
        normalized.append(
            {
                "claim_id": claim_id,
                "state_id": record.get("state_id"),
                "claim_record_sha256": record.get("claim_record_sha256"),
                "source_refs": _string_list(record.get("source_refs")),
                "evidence_refs": _string_list(record.get("evidence_refs")),
                "relations": _string_list(record.get("relations")),
            }
        )
    normalized.sort(key=lambda item: item["claim_id"])
    return normalized


def _normalize_provider_disclosure(value: Optional[Dict[str, Any]]) -> dict:
    if not isinstance(value, dict):
        return {
            "provider_class": None,
            "provider": None,
            "model": None,
            "version": None,
            "mode": "not_declared",
            "external_model_call": None,
            "metadata_semantics": "provider/model process metadata was not declared",
        }
    return dict(value)


def build_evidence_envelope(
    *,
    run_id: str,
    graph_id: Optional[str],
    status: str,
    graph_path: str,
    graph_canonical_sha256: Optional[str],
    graph_file_sha256: Optional[str],
    trace_path: Optional[str],
    checkpoint_path: Optional[str],
    provenance_path: Optional[str],
    trace_chain_internal_valid: Optional[bool],
    claim_index: Optional[Iterable[dict]] = None,
    claim_audit_path: Optional[str] = None,
    provider_disclosure: Optional[Dict[str, Any]] = None,
    human_review: str = "not_declared",
    upstream_artifact_refs: Optional[Iterable[str]] = None,
    upstream_evidence_refs: Optional[Iterable[str]] = None,
) -> dict:
    """Build the project-owned handoff envelope for one run."""
    if human_review not in HUMAN_REVIEW_VALUES:
        raise ValueError(
            f"human_review must be one of {sorted(HUMAN_REVIEW_VALUES)}, got {human_review!r}"
        )

    artifacts = []
    for kind, path in (
        ("graph", graph_path),
        ("trace", trace_path),
        ("checkpoint", checkpoint_path),
        ("provenance", provenance_path),
        ("claim-audit", claim_audit_path),
    ):
        ref = _artifact_ref(kind, path)
        if ref:
            artifacts.append(ref)

    claims = _normalize_claim_index(claim_index)
    claim_audit_ref = _reference("claim-verification", claim_audit_path)

    return {
        "profile": PROFILE,
        "generated_at": _now(),
        "run_id": run_id,
        "graph": {
            "id": graph_id,
            "path": graph_path,
            "canonical_sha256": graph_canonical_sha256,
            "file_sha256": graph_file_sha256,
            "identity_semantics": (
                "canonical_sha256 identifies parsed graph structure; "
                "file_sha256 identifies source file bytes"
            ),
        },
        "status": status,
        "artifacts": artifacts,
        "profiles": {
            "engine": "epistemic-pipeline/engine@2",
            "runtime_policy": "epistemic-pipeline/runtime-policy@1",
            "trace": "epistemic-pipeline/trace@2",
            "checkpoint": "epistemic-pipeline/checkpoint@2",
            "provenance": "epistemic-pipeline/prov@2",
            "confidence": "epistemic-pipeline/confidence-heuristic@1",
            "claim_index": CLAIM_INDEX_PROFILE,
            "claim_verification": CLAIM_VERIFICATION_PROFILE,
            "process_disclosure": PROCESS_DISCLOSURE_PROFILE,
            "upstream_reference": UPSTREAM_REFERENCE_PROFILE,
        },
        "integrity": {
            "trace_chain_internal_valid": trace_chain_internal_valid,
            "semantics": (
                "internal sequence/hash consistency over records currently present; "
                "not externally anchored tamper-proof logging"
            ),
        },
        "upstream_inputs": {
            "profile": UPSTREAM_REFERENCE_PROFILE,
            "artifact_refs": _reference_list("upstream-artifact", upstream_artifact_refs),
            "evidence_refs": _reference_list("upstream-evidence", upstream_evidence_refs),
            "resolution_semantics": (
                "existing local files are hashed; URI/opaque references are retained without dereferencing"
            ),
            "scientific_validity_inherited": False,
        },
        "claim_observability": {
            "profile": CLAIM_INDEX_PROFILE,
            "claims": claims,
            "claim_count": len(claims),
            "verification_record": claim_audit_ref,
            "verification_profile": CLAIM_VERIFICATION_PROFILE,
            "payload_text_embedded": False,
            "semantics": (
                "claim identities plus declared source/evidence references for audit and handoff; "
                "the separate verification record preserves checks/conflicts without converting them into truth labels"
            ),
        },
        "process_disclosure": {
            "profile": PROCESS_DISCLOSURE_PROFILE,
            "provider": _normalize_provider_disclosure(provider_disclosure),
            "human_review": human_review,
            "semantics": (
                "declared execution/review context only; provider identity and human review "
                "do not establish authorship, peer review, correctness, or scientific validity"
            ),
        },
        "confidence_semantics": (
            "bounded weighted heuristic score in [0,1], not calibrated probability"
        ),
        "reproducibility": {
            "level": "R1",
            "semantics": (
                "replay-addressable project evidence; R3 requires a separate rerun "
                "and declared comparison"
            ),
        },
        "scientific_validity_claim": False,
        "payloads_embedded": False,
    }


def write_evidence_envelope(record: dict, output_dir: str = "evidence") -> str:
    """Atomically write ``<run_id>.evidence.json`` and return its path."""
    run_id = str(record.get("run_id") or "unknown")
    out_dir = Path(output_dir)
    out_dir.mkdir(parents=True, exist_ok=True)
    path = out_dir / f"{run_id}.evidence.json"
    temp = path.with_suffix(".evidence.json.tmp")
    temp.write_text(
        json.dumps(record, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    os.replace(temp, path)
    return str(path)
