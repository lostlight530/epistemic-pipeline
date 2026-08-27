#!/usr/bin/env python3
"""Claim-level verification records for epistemic-pipeline research runs.

``epistemic-pipeline/claim-verification@1`` is a project-owned audit profile
built from structures the canonical pipeline already emits. It deliberately
keeps different verification dimensions separate:

- claim identity and declared source/evidence bindings;
- internal-consistency and cross-source observations;
- conflict records;
- bounded heuristic score signals;
- provider/process disclosure and declared human-review state.

The profile never collapses those dimensions into ``verified = true``. A claim
can be structurally checked and still be wrong, weakly sourced, contradicted,
misinterpreted, or outside the competence of the provider/verifier.
"""

from __future__ import annotations

import json
import os
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, Iterable, Mapping, Optional

from core.provenance import canonical_sha256

PROFILE = "epistemic-pipeline/claim-verification@1"
HUMAN_REVIEW_VALUES = {"reviewed", "partial", "not_reviewed", "not_declared"}


def _now() -> str:
    return datetime.now(timezone.utc).isoformat()


def _string_list(value: Any) -> list[str]:
    if not isinstance(value, (list, tuple, set)):
        return []
    result: list[str] = []
    seen = set()
    for item in value:
        text = str(item).strip()
        if text and text not in seen:
            result.append(text)
            seen.add(text)
    return result


def _minimal_provider_disclosure(value: Optional[Mapping[str, Any]]) -> dict:
    if not isinstance(value, Mapping):
        return {
            "provider_class": None,
            "provider": None,
            "model": None,
            "version": None,
            "mode": "not_declared",
            "external_model_call": None,
        }
    return {
        key: value.get(key)
        for key in (
            "provider_class",
            "provider",
            "model",
            "version",
            "mode",
            "external_model_call",
        )
    }


def _conflict_record(claim_id: str, conflict: dict) -> Optional[dict]:
    source = str(conflict.get("source") or "").strip()
    target = str(conflict.get("target") or "").strip()
    if claim_id not in {source, target}:
        return None
    other_ref = target if source == claim_id else source
    relation = str(conflict.get("relation") or "").strip() or None
    severity = str(conflict.get("severity") or "").strip() or None
    return {
        "other_ref": other_ref or None,
        "relation": relation,
        "severity": severity,
        "conflict_record_sha256": canonical_sha256(conflict),
    }


def _audit_state(
    *,
    evidence_refs: list[str],
    has_structural_observation: bool,
    conflicts: list[dict],
) -> str:
    if conflicts and has_structural_observation:
        return "structurally_checked_with_conflict"
    if conflicts:
        return "conflict_recorded"
    if has_structural_observation:
        return "structurally_checked"
    if evidence_refs:
        return "evidence_bound"
    return "indexed_only"


def build_claim_verification(
    run_result: dict,
    *,
    provider_disclosure: Optional[Mapping[str, Any]] = None,
    human_review: str = "not_declared",
) -> dict:
    """Build claim-level audit records from one engine run result.

    Full claim prose is intentionally not copied into the audit sidecar. The
    canonical execution/checkpoint artifacts remain the place where provider
    payloads live.
    """
    if human_review not in HUMAN_REVIEW_VALUES:
        raise ValueError(
            f"human_review must be one of {sorted(HUMAN_REVIEW_VALUES)}, got {human_review!r}"
        )

    claims: Dict[str, dict] = {}
    evidence_refs: Dict[str, set[str]] = {}
    relations: Dict[str, set[str]] = {}
    internal_observations: Dict[str, Any] = {}
    cross_source_observations: Dict[str, Any] = {}
    heuristic_scores: Dict[str, Any] = {}
    conflicts: list[dict] = []
    verification_coverage: list[Any] = []

    results = run_result.get("results") or {}
    if not isinstance(results, dict):
        results = {}

    for state_id, node_result in results.items():
        if not isinstance(node_result, dict):
            continue
        outputs = node_result.get("outputs") or {}
        if not isinstance(outputs, dict):
            continue

        for claim in outputs.get("claims_registry") or []:
            if not isinstance(claim, dict):
                continue
            claim_id = str(claim.get("claim_id") or "").strip()
            if not claim_id:
                continue
            entry = claims.setdefault(
                claim_id,
                {
                    "claim_id": claim_id,
                    "origin_state_id": str(state_id),
                    "claim_record_sha256": canonical_sha256(claim),
                    "source_refs": set(),
                },
            )
            entry["source_refs"].update(_string_list(claim.get("source_refs")))

        for chain in outputs.get("evidence_chains") or []:
            if not isinstance(chain, dict):
                continue
            claim_id = str(chain.get("claim_id") or "").strip()
            if not claim_id:
                continue
            evidence_refs.setdefault(claim_id, set()).update(
                _string_list(chain.get("evidence_refs"))
            )
            relation = str(chain.get("relation") or "").strip()
            if relation:
                relations.setdefault(claim_id, set()).add(relation)

        internal = outputs.get("internal_consistency_report")
        if isinstance(internal, dict):
            for claim_id, observation in internal.items():
                claim_text = str(claim_id).strip()
                if claim_text:
                    internal_observations[claim_text] = observation

        cross_source = outputs.get("cross_source_matrix")
        if isinstance(cross_source, dict):
            for claim_id, observation in cross_source.items():
                claim_text = str(claim_id).strip()
                if claim_text:
                    cross_source_observations[claim_text] = observation

        seed = outputs.get("confidence_seed") or outputs.get("score_seed")
        if isinstance(seed, dict):
            for claim_id, score in seed.items():
                claim_text = str(claim_id).strip()
                if claim_text:
                    heuristic_scores[claim_text] = score

        registry = outputs.get("conflict_registry")
        if isinstance(registry, list):
            conflicts.extend(item for item in registry if isinstance(item, dict))

        if "coverage" in outputs:
            verification_coverage.append(outputs.get("coverage"))

    all_claim_ids = sorted(
        set(claims)
        | set(evidence_refs)
        | set(internal_observations)
        | set(cross_source_observations)
        | set(heuristic_scores)
    )

    claim_records: list[dict] = []
    state_counts: Dict[str, int] = {}
    for claim_id in all_claim_ids:
        base = claims.get(
            claim_id,
            {
                "claim_id": claim_id,
                "origin_state_id": None,
                "claim_record_sha256": None,
                "source_refs": set(),
            },
        )
        claim_conflicts = [
            record
            for conflict in conflicts
            if (record := _conflict_record(claim_id, conflict)) is not None
        ]
        internal = internal_observations.get(claim_id)
        cross_source = cross_source_observations.get(claim_id)
        has_structural_observation = claim_id in internal_observations or claim_id in cross_source_observations
        refs = sorted(evidence_refs.get(claim_id, set()))
        state = _audit_state(
            evidence_refs=refs,
            has_structural_observation=has_structural_observation,
            conflicts=claim_conflicts,
        )
        state_counts[state] = state_counts.get(state, 0) + 1

        score = heuristic_scores.get(claim_id)
        score_record = None
        if isinstance(score, (int, float)) and not isinstance(score, bool):
            score_record = {
                "value": float(score),
                "semantics": "bounded heuristic score; not calibrated probability or truth score",
            }
        elif score is not None:
            score_record = {
                "value": score,
                "semantics": "uninterpreted provider/runtime score value; no probability claim",
            }

        claim_records.append(
            {
                "claim_id": claim_id,
                "origin_state_id": base.get("origin_state_id"),
                "claim_record_sha256": base.get("claim_record_sha256"),
                "source_refs": sorted(base.get("source_refs") or []),
                "evidence_refs": refs,
                "evidence_relations": sorted(relations.get(claim_id, set())),
                "observations": {
                    "internal_consistency": internal,
                    "cross_source": cross_source,
                    "observation_semantics": (
                        "provider/runtime observations retained as audit context; not external scientific verification"
                    ),
                },
                "conflicts": claim_conflicts,
                "heuristic_score": score_record,
                "audit_state": state,
                "truth_claim": False,
                "citation_verification_claim": False,
            }
        )

    coverage_values = [
        value
        for value in verification_coverage
        if isinstance(value, (int, float)) and not isinstance(value, bool)
    ]

    return {
        "profile": PROFILE,
        "generated_at": _now(),
        "run_id": run_result.get("run_id"),
        "run_status": run_result.get("status"),
        "graph_id": run_result.get("graph_id"),
        "graph_sha256": run_result.get("graph_sha256"),
        "claims": claim_records,
        "claim_count": len(claim_records),
        "audit_state_counts": state_counts,
        "verification_coverage_observations": coverage_values,
        "process_context": {
            "provider": _minimal_provider_disclosure(provider_disclosure),
            "human_review": human_review,
            "semantics": (
                "declared execution/review context; provider identity and human review do not establish correctness or peer review"
            ),
        },
        "semantics": {
            "evidence_binding": "records declared links, not evidence sufficiency",
            "consistency_observation": "records runtime/provider observations, not truth",
            "conflict": "records disagreement/limitation structure, not automatic adjudication",
            "heuristic_score": "not calibrated probability",
            "audit_state": "descriptive process state, never a truth label",
        },
        "payload_text_embedded": False,
        "scientific_validity_claim": False,
        "peer_review_claim": False,
        "external_verification_claim": False,
    }


def write_claim_verification(record: dict, output_dir: str = "claim-audits") -> str:
    """Atomically write ``<run_id>.claim-audit.json`` and return its path."""
    run_id = str(record.get("run_id") or "unknown")
    directory = Path(output_dir)
    directory.mkdir(parents=True, exist_ok=True)
    path = directory / f"{run_id}.claim-audit.json"
    temp = path.with_suffix(".claim-audit.json.tmp")
    temp.write_text(
        json.dumps(record, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    os.replace(temp, path)
    return str(path)
