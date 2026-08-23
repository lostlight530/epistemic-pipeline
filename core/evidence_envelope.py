#!/usr/bin/env python3
"""Versioned evidence envelope for epistemic-pipeline research runs.

The envelope is a small project-owned interchange object that references the
run's graph, trace, checkpoint and provenance artifacts without duplicating
node payloads. It is intentionally separate from W3C PROV semantics: PROV
expresses lineage relationships, while this envelope expresses the repository's
cross-tool handoff contract and scientific-integrity boundaries.
"""

from __future__ import annotations

import json
import os
from datetime import datetime, timezone
from pathlib import Path
from typing import Optional

from core.provenance import file_sha256

PROFILE = "epistemic-pipeline/evidence-envelope@1"


def _now() -> str:
    return datetime.now(timezone.utc).isoformat()


def _artifact_ref(kind: str, path: Optional[str]) -> Optional[dict]:
    if not path:
        return None
    digest = file_sha256(path)
    if not digest:
        return None
    return {"kind": kind, "path": str(path), "file_sha256": digest}


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
) -> dict:
    """Build the project-owned handoff envelope for one run."""
    artifacts = []
    for kind, path in (
        ("graph", graph_path),
        ("trace", trace_path),
        ("checkpoint", checkpoint_path),
        ("provenance", provenance_path),
    ):
        ref = _artifact_ref(kind, path)
        if ref:
            artifacts.append(ref)

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
        },
        "integrity": {
            "trace_chain_internal_valid": trace_chain_internal_valid,
            "semantics": (
                "internal sequence/hash consistency over records currently present; "
                "not externally anchored tamper-proof logging"
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
