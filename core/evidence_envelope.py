#!/usr/bin/env python3
"""Stable evidence envelope for epistemic-pipeline research runs.

The envelope is a small project-owned interchange object that references the
run's graph, trace, checkpoint, provenance and claim-verification artifacts
without duplicating node payloads. It is intentionally separate from W3C PROV
semantics: PROV expresses lineage relationships, while this envelope expresses
the repository's cross-tool handoff contract and scientific-integrity
boundaries.

Day-5 additions preserve assertion basis and dimensional upstream-reference
coverage without turning the envelope into a research database or quality
score. None of these surfaces establishes truth, authorship, peer review,
source credibility, model validity, or scientific correctness.
"""

from __future__ import annotations

import json
import os
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, Iterable, Optional
from urllib.parse import urlsplit

from core.provenance import file_sha256

PROFILE = "epistemic-pipeline/evidence-envelope"
CLAIM_INDEX_PROFILE = "epistemic-pipeline/claim-index"
CLAIM_VERIFICATION_PROFILE = "epistemic-pipeline/claim-verification"
PROCESS_DISCLOSURE_PROFILE = "epistemic-pipeline/process-disclosure"
UPSTREAM_REFERENCE_PROFILE = "epistemic-pipeline/upstream-reference"
HUMAN_REVIEW_VALUES = {"reviewed", "partial", "not_reviewed", "not_declared"}


def _now() -> str:
    return datetime.now(timezone.utc).isoformat()


def _artifact_ref(kind: str, path: Optional[str]) -> Optional[dict]:
    if not path:
        return None
    digest = file_sha256(path)
    if not digest:
        return None
    return {
        "kind": kind,
        "path": str(path),
        "file_sha256": digest,
        "identity_basis": "runtime-observed-local-bytes",
    }


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
        record["resolution_basis"] = "runtime-observed-local-filesystem"
        return record
    parsed = urlsplit(text)
    record["resolution"] = (
        "opaque-uri-not-dereferenced" if parsed.scheme else "opaque-reference-not-resolved"
    )
    record["resolution_basis"] = "declared-reference"
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


def _reference_coverage(records: list[dict]) -> dict:
    counts: Dict[str, int] = {}
    for record in records:
        state = str(record.get("resolution") or "not-recorded")
        counts[state] = counts.get(state, 0) + 1
    total = len(records)
    local_count = counts.get("local-file", 0)
    return {
        "reference_count": total,
        "by_resolution": counts,
        "local_file_ratio": (local_count / total) if total else None,
        "aggregate_score": None,
        "semantics": (
            "reference-resolution coverage at envelope-generation time; not source credibility, evidence quality, "
            "citation verification, network availability, or scientific validity"
        ),
    }


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
                "assertion_basis": "structured-run-output",
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
            "assertion_basis": "not_declared",
            "metadata_semantics": "provider/model process metadata was not declared",
        }
    result = dict(value)
    result.setdefault("assertion_basis", "provider-adapter-reported")
    result.setdefault("basis_inferred", False)
    return result


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
    upstream_artifacts = _reference_list("upstream-artifact", upstream_artifact_refs)
    upstream_evidence = _reference_list("upstream-evidence", upstream_evidence_refs)

    return {
        "profile": PROFILE,
        "generated_at": _now(),
        "run_id": run_id,
        "graph": {
            "id": graph_id,
            "path": graph_path,
            "canonical_sha256": graph_canonical_sha256,
            "file_sha256": graph_file_sha256,
            "identity_basis": "runtime-observed-local-file-and-canonical-serialization",
            "identity_semantics": (
                "canonical_sha256 identifies parsed graph structure; file_sha256 identifies source file bytes"
            ),
        },
        "status": status,
        "artifacts": artifacts,
        "profiles": {
            "engine": "epistemic-pipeline/engine",
            "runtime_policy": "epistemic-pipeline/runtime-policy",
            "trace": "epistemic-pipeline/trace",
            "checkpoint": "epistemic-pipeline/checkpoint",
            "provenance": "epistemic-pipeline/prov",
            "confidence": "epistemic-pipeline/confidence-heuristic",
            "claim_index": CLAIM_INDEX_PROFILE,
            "claim_verification": CLAIM_VERIFICATION_PROFILE,
            "process_disclosure": PROCESS_DISCLOSURE_PROFILE,
            "upstream_reference": UPSTREAM_REFERENCE_PROFILE,
        },
        "integrity": {
            "trace_chain_internal_valid": trace_chain_internal_valid,
            "observation_basis": "runtime-trace-validation" if trace_chain_internal_valid is not None else "not_observed",
            "semantics": (
                "internal sequence/hash consistency over records currently present; not externally anchored tamper-proof logging"
            ),
        },
        "upstream_inputs": {
            "profile": UPSTREAM_REFERENCE_PROFILE,
            "artifact_refs": upstream_artifacts,
            "evidence_refs": upstream_evidence,
            "artifact_ref_coverage": _reference_coverage(upstream_artifacts),
            "evidence_ref_coverage": _reference_coverage(upstream_evidence),
            "assertion_basis": "caller-declared-with-optional-local-resolution",
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
            "assertion_basis": "structured-run-output",
            "semantics": (
                "claim identities plus declared source/evidence references for audit and handoff; the separate "
                "verification record preserves checks/conflicts without converting them into truth labels"
            ),
        },
        "process_disclosure": {
            "profile": PROCESS_DISCLOSURE_PROFILE,
            "provider": _normalize_provider_disclosure(provider_disclosure),
            "human_review": human_review,
            "human_review_basis": "caller-declared" if human_review != "not_declared" else "not_declared",
            "automatic_ai_detection_used": False,
            "semantics": (
                "execution/review context with explicit assertion basis; provider identity and human review do not "
                "establish authorship, AI-content detection, peer review, correctness, or scientific validity"
            ),
        },
        "confidence_semantics": (
            "bounded weighted heuristic score in [0,1], not calibrated probability"
        ),
        "reproducibility": {
            "level": "R1",
            "semantics": (
                "replay-addressable project evidence; R3 requires a separate rerun and declared comparison"
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
