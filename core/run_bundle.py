#!/usr/bin/env python3
"""Evidence-bearing run wrapper for engine + trace/checkpoint + audit/handoff.

``core.engine.StateMachineEngine`` remains the low-level executor. This wrapper
adds distinct evidence layers instead of collapsing every concern into one log:

- ``epistemic-pipeline/prov`` for PROV-aligned lineage relationships;
- ``epistemic-pipeline/claim-verification`` for claim-level evidence,
  consistency/conflict and heuristic-score audit dimensions;
- ``epistemic-pipeline/evidence-envelope`` for cross-repository handoff,
  including a payload-minimizing claim index, process disclosure, the separate
  claim-verification reference and optional upstream artifact/evidence refs.

Neither layer embeds full node payloads by default or claims scientific truth,
external standards certification, authorship adjudication, peer review, source
credibility, probability calibration, or independent reproduction.
"""

from __future__ import annotations

import argparse
import json
import sys
import uuid
from pathlib import Path
from typing import Any, Dict, Iterable, Optional

import yaml

if __package__ in (None, ""):
    sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from core.claim_audit import build_claim_verification, write_claim_verification
from core.engine import StateMachineEngine
from core.evidence_envelope import build_evidence_envelope, write_evidence_envelope
from core.provenance import (
    build_run_provenance,
    canonical_sha256,
    file_sha256,
    write_provenance,
)
from core.run_tracer import RunTracer

HUMAN_REVIEW_VALUES = ("reviewed", "partial", "not_reviewed", "not_declared")


def _load_graph(path: str) -> dict:
    graph_path = Path(path)
    if not graph_path.is_file():
        raise FileNotFoundError(path)
    with graph_path.open("r", encoding="utf-8") as handle:
        data = yaml.safe_load(handle)
    if not isinstance(data, dict):
        raise ValueError("graph YAML must contain a mapping")
    return data


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


def _build_claim_index(run_result: dict) -> list[dict]:
    """Extract claim identity/evidence refs without embedding claim prose."""
    claims: Dict[str, dict] = {}
    evidence_refs: Dict[str, set[str]] = {}
    relations: Dict[str, set[str]] = {}

    results = run_result.get("results") or {}
    if not isinstance(results, dict):
        return []

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
                    "state_id": str(state_id),
                    "claim_record_sha256": canonical_sha256(claim),
                    "source_refs": [],
                },
            )
            merged_sources = set(entry.get("source_refs") or [])
            merged_sources.update(_string_list(claim.get("source_refs")))
            entry["source_refs"] = sorted(merged_sources)

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

    index = []
    for claim_id in sorted(set(claims) | set(evidence_refs)):
        base = claims.get(
            claim_id,
            {
                "claim_id": claim_id,
                "state_id": None,
                "claim_record_sha256": None,
                "source_refs": [],
            },
        )
        index.append(
            {
                **base,
                "evidence_refs": sorted(evidence_refs.get(claim_id, set())),
                "relations": sorted(relations.get(claim_id, set())),
            }
        )
    return index


def _provider_disclosure(engine: Optional[StateMachineEngine]) -> dict:
    if engine is None:
        return {
            "provider_class": None,
            "provider": None,
            "model": None,
            "version": None,
            "mode": "engine_not_initialized",
            "external_model_call": None,
            "metadata_semantics": "engine initialization failed before provider disclosure was available",
        }
    try:
        return engine.harness.describe_provider(mock=engine.mock_llm)
    except Exception as exc:
        return {
            "provider_class": None,
            "provider": None,
            "model": None,
            "version": None,
            "mode": "disclosure_error",
            "external_model_call": None,
            "metadata_semantics": f"provider disclosure unavailable: {type(exc).__name__}",
        }


def run_bundle(
    graph_path: str,
    resume_from: Optional[str] = None,
    trace_dir: str = "traces",
    checkpoint_dir: str = "checkpoints",
    provenance_dir: str = "provenance",
    claim_audit_dir: str = "claim-audits",
    evidence_dir: str = "evidence",
    human_review: str = "not_declared",
    upstream_artifact_refs: Optional[Iterable[str]] = None,
    upstream_evidence_refs: Optional[Iterable[str]] = None,
) -> dict:
    """Run one graph and write bounded provenance/audit/evidence sidecars."""
    if human_review not in HUMAN_REVIEW_VALUES:
        raise ValueError(
            f"human_review must be one of {HUMAN_REVIEW_VALUES}, got {human_review!r}"
        )

    artifact_refs = [str(value) for value in (upstream_artifact_refs or [])]
    evidence_refs = [str(value) for value in (upstream_evidence_refs or [])]

    graph_data = _load_graph(graph_path)
    graph_canonical_sha256 = canonical_sha256(graph_data)
    graph_file_sha256 = file_sha256(graph_path)
    engine: Optional[StateMachineEngine] = None

    try:
        engine = StateMachineEngine(
            graph_path,
            trace_dir=trace_dir,
            checkpoint_dir=checkpoint_dir,
        )
        result = engine.run(resume_from=resume_from)
    except Exception as exc:
        run_id = getattr(engine, "last_run_id", None)
        if not run_id:
            run_id = "rejected-" + graph_canonical_sha256.split(":", 1)[1][:12]
        result = {
            "status": "failed",
            "run_id": run_id,
            "graph_id": graph_data.get("id"),
            "graph_sha256": graph_canonical_sha256,
            "errors": [f"{type(exc).__name__}: {exc}"],
            "results": dict(getattr(engine, "outputs", {}) or {}),
        }

    run_id = str(result.get("run_id") or ("run-" + uuid.uuid4().hex[:12]))
    result["run_id"] = run_id
    result.setdefault("graph_id", graph_data.get("id"))
    result.setdefault("graph_sha256", graph_canonical_sha256)

    trace_path = Path(trace_dir) / f"{run_id}.jsonl"
    checkpoint_path = Path(checkpoint_dir) / run_id / "checkpoint.json"
    trace_ref = str(trace_path) if trace_path.exists() else None
    checkpoint_ref = str(checkpoint_path) if checkpoint_path.exists() else None

    trace_chain_valid: Optional[bool] = None
    if trace_ref:
        try:
            trace_chain_valid = RunTracer.verify_chain(trace_ref)
        except (OSError, ValueError, json.JSONDecodeError):
            trace_chain_valid = False

    provenance = build_run_provenance(
        graph_path,
        graph_data,
        result,
        trace_path=trace_ref,
        checkpoint_path=checkpoint_ref,
    )
    provenance["integrity"] = {
        "trace_chain_internal_valid": trace_chain_valid,
        "semantics": "internal hash/link consistency over records currently present",
    }
    provenance_path = write_provenance(provenance, provenance_dir)

    claim_index = _build_claim_index(result)
    provider_disclosure = _provider_disclosure(engine)
    claim_audit = build_claim_verification(
        result,
        provider_disclosure=provider_disclosure,
        human_review=human_review,
    )
    claim_audit_path = write_claim_verification(claim_audit, claim_audit_dir)

    envelope = build_evidence_envelope(
        run_id=run_id,
        graph_id=graph_data.get("id"),
        status=str(result.get("status") or "unknown"),
        graph_path=graph_path,
        graph_canonical_sha256=str(result.get("graph_sha256") or graph_canonical_sha256),
        graph_file_sha256=graph_file_sha256,
        trace_path=trace_ref,
        checkpoint_path=checkpoint_ref,
        provenance_path=provenance_path,
        trace_chain_internal_valid=trace_chain_valid,
        claim_index=claim_index,
        claim_audit_path=claim_audit_path,
        provider_disclosure=provider_disclosure,
        human_review=human_review,
        upstream_artifact_refs=artifact_refs,
        upstream_evidence_refs=evidence_refs,
    )
    evidence_path = write_evidence_envelope(envelope, evidence_dir)

    result["provenance_path"] = provenance_path
    result["claim_audit_path"] = claim_audit_path
    result["evidence_envelope_path"] = evidence_path
    result["graph_file_sha256"] = graph_file_sha256
    result["claim_index_count"] = len(claim_index)
    result["claim_audit_count"] = int(claim_audit.get("claim_count") or 0)
    result["upstream_artifact_ref_count"] = len(artifact_refs)
    result["upstream_evidence_ref_count"] = len(evidence_refs)
    return result


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(
        description=(
            "Run an epistemic graph and emit PROV-aligned lineage, claim-level "
            "verification audit and a claim-aware project evidence envelope"
        )
    )
    parser.add_argument("graph", help="path to an executable graph YAML")
    parser.add_argument("--resume-from", metavar="RUN_ID", help="resume from an existing checkpoint")
    parser.add_argument("--trace-dir", default="traces")
    parser.add_argument("--checkpoint-dir", default="checkpoints")
    parser.add_argument("--provenance-dir", default="provenance")
    parser.add_argument("--claim-audit-dir", default="claim-audits")
    parser.add_argument("--evidence-dir", default="evidence")
    parser.add_argument(
        "--upstream-artifact-ref",
        action="append",
        default=[],
        help="local path or opaque URI/reference to an upstream artifact record; may be repeated",
    )
    parser.add_argument(
        "--upstream-evidence-ref",
        action="append",
        default=[],
        help="local path or opaque URI/reference to upstream evidence/provenance; may be repeated",
    )
    parser.add_argument(
        "--human-review",
        choices=HUMAN_REVIEW_VALUES,
        default="not_declared",
        help="declared human-review state for process disclosure; not peer-review status",
    )
    args = parser.parse_args(argv)

    result = run_bundle(
        args.graph,
        resume_from=args.resume_from,
        trace_dir=args.trace_dir,
        checkpoint_dir=args.checkpoint_dir,
        provenance_dir=args.provenance_dir,
        claim_audit_dir=args.claim_audit_dir,
        evidence_dir=args.evidence_dir,
        human_review=args.human_review,
        upstream_artifact_refs=args.upstream_artifact_ref,
        upstream_evidence_refs=args.upstream_evidence_ref,
    )
    print(
        json.dumps(
            {
                "status": result.get("status"),
                "run_id": result.get("run_id"),
                "graph_sha256": result.get("graph_sha256"),
                "graph_file_sha256": result.get("graph_file_sha256"),
                "provenance_path": result.get("provenance_path"),
                "claim_audit_path": result.get("claim_audit_path"),
                "evidence_envelope_path": result.get("evidence_envelope_path"),
                "claim_index_count": result.get("claim_index_count", 0),
                "claim_audit_count": result.get("claim_audit_count", 0),
                "upstream_artifact_ref_count": result.get("upstream_artifact_ref_count", 0),
                "upstream_evidence_ref_count": result.get("upstream_evidence_ref_count", 0),
                "errors": result.get("errors", []),
            },
            ensure_ascii=False,
            indent=2,
        )
    )
    return 0 if result.get("status") == "success" else 1


if __name__ == "__main__":
    raise SystemExit(main())
