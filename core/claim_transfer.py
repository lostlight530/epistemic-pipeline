#!/usr/bin/env python3
"""Portable claim-transfer handoff for epistemic-pipeline.

This module selects claim records from an existing claim-verification sidecar
and emits a smaller downstream transfer object. It preserves source/evidence
references, conflicts, audit state, heuristic-score observations, process
context, and any source-record identity/origin ambiguity without copying claim
prose or upgrading audit state into a scientific verdict.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import os
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Iterable, Optional

PROFILE = "epistemic-pipeline/claim-transfer"
SOURCE_PROFILE = "epistemic-pipeline/claim-verification"


def _now() -> str:
    return datetime.now(timezone.utc).isoformat()


def _file_sha256(path: str | Path) -> str:
    candidate = Path(path)
    digest = hashlib.sha256()
    with candidate.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return "sha256:" + digest.hexdigest()


def _load_json(path: str | Path) -> dict:
    data = json.loads(Path(path).read_text(encoding="utf-8"))
    if not isinstance(data, dict):
        raise ValueError("claim audit must be a JSON object")
    source_profile = data.get("profile")
    if source_profile != SOURCE_PROFILE:
        raise ValueError(
            f"claim transfer requires source profile {SOURCE_PROFILE!r}, got {source_profile!r}"
        )
    return data


def _string_list(value: Any) -> list[str]:
    if not isinstance(value, (list, tuple, set)):
        return []
    result: list[str] = []
    seen: set[str] = set()
    for item in value:
        text = str(item).strip()
        if text and text not in seen:
            result.append(text)
            seen.add(text)
    return result


def _select_claims(audit: dict, claim_ids: Optional[Iterable[str]]) -> list[dict]:
    requested = {str(item).strip() for item in (claim_ids or []) if str(item).strip()}
    claims = audit.get("claims") or []
    if not isinstance(claims, list):
        claims = []

    selected: list[dict] = []
    found: set[str] = set()
    for record in claims:
        if not isinstance(record, dict):
            continue
        claim_id = str(record.get("claim_id") or "").strip()
        if not claim_id:
            continue
        if requested and claim_id not in requested:
            continue
        found.add(claim_id)
        selected.append(
            {
                "claim_id": claim_id,
                "origin_state_id": record.get("origin_state_id"),
                "origin_state_ids": _string_list(record.get("origin_state_ids")),
                "claim_origin_ambiguous": bool(record.get("claim_origin_ambiguous", False)),
                "claim_record_sha256": record.get("claim_record_sha256"),
                "claim_record_sha256s": _string_list(record.get("claim_record_sha256s")),
                "claim_identity_ambiguous": bool(record.get("claim_identity_ambiguous", False)),
                "source_refs": _string_list(record.get("source_refs")),
                "evidence_refs": _string_list(record.get("evidence_refs")),
                "evidence_relations": _string_list(record.get("evidence_relations")),
                "observations": dict(record.get("observations") or {}),
                "conflicts": [dict(item) for item in (record.get("conflicts") or []) if isinstance(item, dict)],
                "heuristic_scores": dict(record.get("heuristic_scores") or {}),
                "audit_state": record.get("audit_state"),
                "transfer_constraints": {
                    "scientific_validity_inherited": False,
                    "evidence_sufficiency_inherited": False,
                    "peer_review_inherited": False,
                    "conflicts_must_remain_visible": True,
                    "claim_origin_ambiguity_must_remain_visible": True,
                    "claim_identity_ambiguity_must_remain_visible": True,
                    "heuristic_scores_must_retain_non_probability_semantics": True,
                },
            }
        )

    missing = sorted(requested - found)
    if missing:
        raise ValueError(f"requested claim IDs not present in claim audit: {missing}")
    return selected


def _has_structural_observation(item: dict) -> bool:
    observations = item.get("observations") or {}
    if not isinstance(observations, dict):
        return False
    return (
        observations.get("internal_consistency") is not None
        or observations.get("cross_source") is not None
    )


def _coverage(claims: list[dict]) -> dict:
    total = len(claims)
    with_evidence = sum(1 for item in claims if item.get("evidence_refs"))
    with_conflicts = sum(1 for item in claims if item.get("conflicts"))
    with_observations = sum(1 for item in claims if _has_structural_observation(item))
    with_final_scores = sum(
        1 for item in claims if (item.get("heuristic_scores") or {}).get("final") is not None
    )
    with_origin_ambiguity = sum(1 for item in claims if item.get("claim_origin_ambiguous"))
    with_identity_ambiguity = sum(1 for item in claims if item.get("claim_identity_ambiguous"))
    return {
        "selected_claim_count": total,
        "claims_with_evidence_refs": with_evidence,
        "claims_with_conflicts": with_conflicts,
        "claims_with_structural_observations": with_observations,
        "claims_with_final_heuristic_score": with_final_scores,
        "claims_with_origin_ambiguity": with_origin_ambiguity,
        "claims_with_identity_ambiguity": with_identity_ambiguity,
        "evidence_reference_ratio": (with_evidence / total) if total else None,
        "origin_ambiguity_ratio": (with_origin_ambiguity / total) if total else None,
        "identity_ambiguity_ratio": (with_identity_ambiguity / total) if total else None,
        "aggregate_score": None,
        "semantics": (
            "descriptive transfer coverage only; ambiguity ratios describe source-record/origin multiplicity, "
            "not contradiction, provenance soundness, evidence sufficiency, scientific validity, review "
            "acceptance, or probability of correctness"
        ),
    }


def build_claim_transfer(
    claim_audit_path: str | Path,
    *,
    claim_ids: Optional[Iterable[str]] = None,
    purpose: Optional[str] = None,
) -> dict:
    audit_path = Path(claim_audit_path)
    audit = _load_json(audit_path)
    selected = _select_claims(audit, claim_ids)

    return {
        "profile": PROFILE,
        "generated_at": _now(),
        "source_claim_audit": {
            "path": str(audit_path),
            "file_sha256": _file_sha256(audit_path),
            "source_profile": audit.get("profile"),
            "run_id": audit.get("run_id"),
            "basis": "runtime-observed-local-bytes",
        },
        "purpose": purpose,
        "purpose_basis": "caller-declared" if purpose else "not_declared",
        "claims": selected,
        "transfer_coverage": _coverage(selected),
        "assertion_basis": {
            "claim_records": "copied-from-local-claim-verification-sidecar",
            "claim_identity_ambiguity": "copied-without-adjudication",
            "purpose": "caller-declared" if purpose else "not_declared",
            "basis_inferred": False,
        },
        "payload_text_embedded": False,
        "scientific_validity_claim": False,
        "evidence_sufficiency_claim": False,
        "peer_review_claim": False,
        "acceptance_claim": False,
    }


def write_claim_transfer(record: dict, output: str | Path) -> Path:
    path = Path(output)
    path.parent.mkdir(parents=True, exist_ok=True)
    temp = path.with_suffix(path.suffix + ".tmp")
    temp.write_text(json.dumps(record, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    os.replace(temp, path)
    return path


def main(argv: Optional[list[str]] = None) -> int:
    parser = argparse.ArgumentParser(description="Create a bounded claim-transfer handoff")
    parser.add_argument("claim_audit", help="existing <run>.claim-audit.json")
    parser.add_argument("--claim-id", action="append", default=[], help="claim ID to transfer; repeatable")
    parser.add_argument("--purpose", help="caller-declared downstream purpose")
    parser.add_argument("--output", required=True)
    args = parser.parse_args(argv)
    record = build_claim_transfer(args.claim_audit, claim_ids=args.claim_id, purpose=args.purpose)
    write_claim_transfer(record, args.output)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
