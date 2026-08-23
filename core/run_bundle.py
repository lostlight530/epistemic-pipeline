#!/usr/bin/env python3
"""Evidence-bearing run wrapper for engine + trace/checkpoint + lineage/handoff.

``core.engine.StateMachineEngine`` remains the low-level executor. This wrapper
adds two distinct evidence layers:

- ``epistemic-pipeline/prov@2`` for PROV-aligned lineage relationships;
- ``epistemic-pipeline/evidence-envelope@1`` for cross-repository handoff.

Neither layer embeds full node payloads by default or claims scientific truth,
external standards certification, or independent reproduction.
"""

from __future__ import annotations

import argparse
import json
import sys
import uuid
from pathlib import Path
from typing import Optional

import yaml

if __package__ in (None, ""):
    sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from core.engine import StateMachineEngine
from core.evidence_envelope import build_evidence_envelope, write_evidence_envelope
from core.provenance import (
    build_run_provenance,
    canonical_sha256,
    file_sha256,
    write_provenance,
)
from core.run_tracer import RunTracer


def _load_graph(path: str) -> dict:
    graph_path = Path(path)
    if not graph_path.is_file():
        raise FileNotFoundError(path)
    with graph_path.open("r", encoding="utf-8") as handle:
        data = yaml.safe_load(handle)
    if not isinstance(data, dict):
        raise ValueError("graph YAML must contain a mapping")
    return data


def run_bundle(
    graph_path: str,
    resume_from: Optional[str] = None,
    trace_dir: str = "traces",
    checkpoint_dir: str = "checkpoints",
    provenance_dir: str = "provenance",
    evidence_dir: str = "evidence",
) -> dict:
    """Run one graph and write bounded provenance/evidence sidecars."""
    graph_data = _load_graph(graph_path)
    graph_canonical_sha256 = canonical_sha256(graph_data)
    graph_file_sha256 = file_sha256(graph_path)
    engine = None

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
    )
    evidence_path = write_evidence_envelope(envelope, evidence_dir)

    result["provenance_path"] = provenance_path
    result["evidence_envelope_path"] = evidence_path
    result["graph_file_sha256"] = graph_file_sha256
    return result


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(
        description=(
            "Run an epistemic graph and emit PROV-aligned lineage plus a "
            "project evidence envelope"
        )
    )
    parser.add_argument("graph", help="path to an executable graph YAML")
    parser.add_argument("--resume-from", metavar="RUN_ID", help="resume from an existing checkpoint")
    parser.add_argument("--trace-dir", default="traces")
    parser.add_argument("--checkpoint-dir", default="checkpoints")
    parser.add_argument("--provenance-dir", default="provenance")
    parser.add_argument("--evidence-dir", default="evidence")
    args = parser.parse_args(argv)

    result = run_bundle(
        args.graph,
        resume_from=args.resume_from,
        trace_dir=args.trace_dir,
        checkpoint_dir=args.checkpoint_dir,
        provenance_dir=args.provenance_dir,
        evidence_dir=args.evidence_dir,
    )
    print(
        json.dumps(
            {
                "status": result.get("status"),
                "run_id": result.get("run_id"),
                "graph_sha256": result.get("graph_sha256"),
                "graph_file_sha256": result.get("graph_file_sha256"),
                "provenance_path": result.get("provenance_path"),
                "evidence_envelope_path": result.get("evidence_envelope_path"),
                "errors": result.get("errors", []),
            },
            ensure_ascii=False,
            indent=2,
        )
    )
    return 0 if result.get("status") == "success" else 1


if __name__ == "__main__":
    raise SystemExit(main())
