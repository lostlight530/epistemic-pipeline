#!/usr/bin/env python3
"""Audited research-run wrapper: engine execution + trace/checkpoint + provenance.

`core/engine.py` remains the low-level execution engine. This wrapper is the
recommended entry point when a run must leave a single auditable bundle.
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
from core.provenance import build_run_provenance, canonical_sha256, write_provenance
from core.run_tracer import RunTracer


def _load_graph(path: str) -> dict:
    with open(path, "r", encoding="utf-8") as handle:
        return yaml.safe_load(handle)


def run_bundle(graph_path: str, resume_from: Optional[str] = None,
               trace_dir: str = "traces", checkpoint_dir: str = "checkpoints",
               provenance_dir: str = "provenance") -> dict:
    graph_data = _load_graph(graph_path)
    engine = None
    result = None

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
            run_id = "rejected-" + canonical_sha256(graph_data).split(":", 1)[1][:12]
        result = {
            "status": "failed",
            "run_id": run_id,
            "errors": [f"{type(exc).__name__}: {exc}"],
            "results": dict(getattr(engine, "outputs", {}) or {}),
        }

    run_id = result.get("run_id") or ("run-" + uuid.uuid4().hex[:12])
    result["run_id"] = run_id
    trace_path = Path(trace_dir) / f"{run_id}.jsonl"
    checkpoint_path = Path(checkpoint_dir) / run_id / "checkpoint.json"

    provenance = build_run_provenance(
        graph_path,
        graph_data,
        result,
        trace_path=str(trace_path) if trace_path.exists() else None,
        checkpoint_path=str(checkpoint_path) if checkpoint_path.exists() else None,
    )
    if trace_path.exists():
        try:
            provenance["integrity"] = {"trace_hash_chain_valid": RunTracer.verify_chain(str(trace_path))}
        except (OSError, ValueError, json.JSONDecodeError):
            provenance["integrity"] = {"trace_hash_chain_valid": False}

    result["provenance_path"] = write_provenance(provenance, provenance_dir)
    return result


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description="Run an epistemic graph and emit an auditable PROV-aligned bundle")
    parser.add_argument("graph", help="path to an executable graph YAML")
    parser.add_argument("--resume-from", metavar="RUN_ID", help="resume from an existing checkpoint")
    parser.add_argument("--trace-dir", default="traces")
    parser.add_argument("--checkpoint-dir", default="checkpoints")
    parser.add_argument("--provenance-dir", default="provenance")
    args = parser.parse_args(argv)

    result = run_bundle(
        args.graph,
        resume_from=args.resume_from,
        trace_dir=args.trace_dir,
        checkpoint_dir=args.checkpoint_dir,
        provenance_dir=args.provenance_dir,
    )
    print(json.dumps({
        "status": result.get("status"),
        "run_id": result.get("run_id"),
        "provenance_path": result.get("provenance_path"),
        "errors": result.get("errors", []),
    }, ensure_ascii=False, indent=2))
    return 0 if result.get("status") == "success" else 1


if __name__ == "__main__":
    raise SystemExit(main())
