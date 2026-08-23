#!/usr/bin/env python3
"""W3C PROV-aligned provenance profile for epistemic-pipeline runs.

This module uses PROV's core Entity / Activity / Agent model and relation names
as a compact JSON profile. It is *not* a PROV-O RDF serializer and does not
claim full W3C PROV serialization conformance.

The default record stores hashes and structural metadata rather than copying
research payloads into the provenance sidecar.
"""

from __future__ import annotations

import hashlib
import json
import os
from datetime import datetime, timezone
from pathlib import Path
from typing import Dict, Optional

PROFILE = "epistemic-pipeline/prov@1"
PROV_NAMESPACE = "http://www.w3.org/ns/prov#"
SOFTWARE_AGENT = "agent:epistemic-pipeline"


def _now() -> str:
    return datetime.now(timezone.utc).isoformat()


def canonical_sha256(value) -> str:
    encoded = json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":")).encode("utf-8")
    return "sha256:" + hashlib.sha256(encoded).hexdigest()


def file_sha256(path: Optional[str]) -> Optional[str]:
    if not path:
        return None
    p = Path(path)
    if not p.is_file():
        return None
    digest = hashlib.sha256()
    with p.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return "sha256:" + digest.hexdigest()


def build_run_provenance(graph_path: str, graph_data: dict, run_result: dict,
                         trace_path: Optional[str] = None,
                         checkpoint_path: Optional[str] = None) -> dict:
    """Build a privacy-minimising, PROV-aligned lineage record for one run."""
    run_id = str(run_result.get("run_id") or "unknown")
    graph_hash = canonical_sha256(graph_data)
    graph_entity = f"entity:graph:{graph_hash.split(':', 1)[1][:16]}"
    run_activity = f"activity:run:{run_id}"

    record = {
        "profile": PROFILE,
        "prov_namespace": PROV_NAMESPACE,
        "run_id": run_id,
        "status": run_result.get("status", "unknown"),
        "generated_at": _now(),
        "entities": {
            graph_entity: {
                "type": "prov:Entity",
                "kind": "dependency-graph",
                "graph_id": graph_data.get("id"),
                "source": graph_path,
                "sha256": graph_hash,
            }
        },
        "activities": {
            run_activity: {
                "type": "prov:Activity",
                "kind": "pipeline-run",
                "status": run_result.get("status", "unknown"),
            }
        },
        "agents": {
            SOFTWARE_AGENT: {
                "type": "prov:SoftwareAgent",
                "label": "epistemic-pipeline",
            }
        },
        "relations": {
            "used": [{"activity": run_activity, "entity": graph_entity}],
            "wasGeneratedBy": [],
            "wasDerivedFrom": [],
            "wasAssociatedWith": [{"activity": run_activity, "agent": SOFTWARE_AGENT}],
        },
        "privacy": {
            "payloads_embedded": False,
            "note": "Node outputs are represented by canonical SHA-256 plus structural metadata, not copied verbatim.",
        },
    }

    output_entity_by_state: Dict[str, str] = {}
    results = run_result.get("results") or {}
    nodes = {n.get("id"): n for n in graph_data.get("nodes", []) if isinstance(n, dict)}

    for state_id, result in sorted(results.items()):
        node = nodes.get(state_id, {})
        stage = result.get("stage") or node.get("stage")
        activity_id = f"activity:node:{run_id}:{state_id}"
        outputs = result.get("outputs") or {}
        output_hash = canonical_sha256(outputs)
        entity_id = f"entity:output:{run_id}:{state_id}:{output_hash.split(':', 1)[1][:16]}"
        output_entity_by_state[state_id] = entity_id

        record["activities"][activity_id] = {
            "type": "prov:Activity",
            "kind": "pipeline-node",
            "state_id": state_id,
            "stage": stage,
            "status": result.get("status", "unknown"),
        }
        record["entities"][entity_id] = {
            "type": "prov:Entity",
            "kind": "node-output",
            "state_id": state_id,
            "stage": stage,
            "sha256": output_hash,
            "keys": sorted(outputs.keys()) if isinstance(outputs, dict) else [],
        }
        record["relations"]["wasGeneratedBy"].append({"entity": entity_id, "activity": activity_id})
        record["relations"]["wasAssociatedWith"].append({"activity": activity_id, "agent": SOFTWARE_AGENT})
        record["relations"]["used"].append({"activity": activity_id, "entity": graph_entity})

    # Dependency lineage is emitted only after all output entity ids are known.
    for state_id, result in sorted(results.items()):
        activity_id = f"activity:node:{run_id}:{state_id}"
        current_entity = output_entity_by_state.get(state_id)
        for dependency in nodes.get(state_id, {}).get("dependencies", []) or []:
            dep_entity = output_entity_by_state.get(dependency)
            if not dep_entity:
                continue
            record["relations"]["used"].append({"activity": activity_id, "entity": dep_entity})
            if current_entity:
                record["relations"]["wasDerivedFrom"].append({
                    "generatedEntity": current_entity,
                    "usedEntity": dep_entity,
                })

    for kind, path in (("trace", trace_path), ("checkpoint", checkpoint_path)):
        digest = file_sha256(path)
        if not digest:
            continue
        entity_id = f"entity:{kind}:{run_id}:{digest.split(':', 1)[1][:16]}"
        record["entities"][entity_id] = {
            "type": "prov:Entity",
            "kind": kind,
            "path": str(path),
            "sha256": digest,
        }
        record["relations"]["wasGeneratedBy"].append({"entity": entity_id, "activity": run_activity})

    return record


def write_provenance(record: dict, output_dir: str = "provenance") -> str:
    """Atomically write ``<run_id>.prov.json`` and return its path."""
    out_dir = Path(output_dir)
    out_dir.mkdir(parents=True, exist_ok=True)
    path = out_dir / f"{record.get('run_id', 'unknown')}.prov.json"
    tmp = path.with_suffix(".prov.json.tmp")
    tmp.write_text(json.dumps(record, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    os.replace(tmp, path)
    return str(path)
