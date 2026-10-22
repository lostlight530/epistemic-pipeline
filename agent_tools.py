#!/usr/bin/env python3
"""Provider-neutral, allowlisted, synchronous tool adapter.

Explicitly *not* an MCP server, arbitrary code executor, autonomous planner,
external LLM client, or scientific validation authority. No automatic writes.
"""
from __future__ import annotations

import json
from typing import Any

PROFILE = "epistemic-pipeline/tool-adapter"
_SPECS = [
  {
    "name": "graph_inspect",
    "description": "Validate a local YAML dependency graph; report structural order, levels, parallel groups and critical path only for a valid DAG.",
    "parameters": {
      "type": "object",
      "properties": {
        "graph": {
          "type": "string",
          "description": "Local graph YAML path"
        }
      },
      "required": [
        "graph"
      ],
      "additionalProperties": False
    }
  },
  {
    "name": "claim_transfer",
    "description": "Create a portable claim-selection handoff in memory from an existing claim-verification sidecar; no implicit scientific acceptance.",
    "parameters": {
      "type": "object",
      "properties": {
        "claim_audit": {
          "type": "string",
          "description": "Existing claim verification JSON sidecar"
        },
        "claim_ids": {
          "type": "array",
          "items": {
            "type": "string"
          },
          "minItems": 1,
          "description": "Optional explicit claim IDs; omission selects all indexed claims"
        },
        "purpose": {
          "type": "string",
          "description": "Caller-declared handoff purpose"
        }
      },
      "required": [
        "claim_audit"
      ],
      "additionalProperties": False
    }
  }
]


TOOL_SPECS = {item["name"]: item for item in _SPECS}


def tool_definitions() -> list[dict]:
    """JSON-Schema function declarations usable by a caller-managed Agent."""
    return [{"type": "function", "function": {
        "name": spec["name"], "description": spec["description"],
        "parameters": spec["parameters"],
    }} for spec in _SPECS]


def _check_schema_value(value: Any, schema: dict, path: str) -> None:
    """Validate declared parameter types, including nested array items."""
    kind = schema.get("type")
    if kind == "string":
        if not isinstance(value, str) or not value.strip():
            raise ValueError(f"{path} must be a nonempty string")
    elif kind == "boolean":
        if not isinstance(value, bool):
            raise ValueError(f"{path} must be a boolean")
    elif kind == "array":
        if not isinstance(value, list):
            raise ValueError(f"{path} must be an array")
        if len(value) < schema.get("minItems", 0):
            raise ValueError(f'{path} must contain at least {schema["minItems"]} items')
        if "items" in schema:
            for index, item in enumerate(value):
                _check_schema_value(item, schema["items"], f"{path}[{index}]")
    elif kind == "object":
        if not isinstance(value, dict):
            raise ValueError(f"{path} must be an object")
        properties = schema.get("properties", {})
        if schema.get("additionalProperties") is False:
            unknown = set(value) - set(properties)
            if unknown:
                raise ValueError(f'{path} has unexpected keys: {", ".join(sorted(unknown))}')
        missing = set(schema.get("required", [])) - set(value)
        if missing:
            raise ValueError(f'{path} is missing keys: {", ".join(sorted(missing))}')
        for key, item in value.items():
            if key in properties:
                _check_schema_value(item, properties[key], f"{path}.{key}")
    else:
        raise ValueError(f"unsupported parameter schema type: {kind}")
    if "enum" in schema and value not in schema["enum"]:
        raise ValueError(f"{path} must be an allowed value")


def _check_arguments(name: str, arguments: Any) -> dict:
    _check_schema_value(arguments, TOOL_SPECS[name]["parameters"], "arguments")
    return arguments


def _dispatch(name: str, a: dict) -> Any:
    if name == "graph_inspect":
        from core.dependency_graph import DependencyGraph
        import yaml
        from pathlib import Path
        graph = yaml.safe_load(Path(a["graph"]).read_text(encoding="utf-8"))
        if not isinstance(graph, dict) or not isinstance(graph.get("nodes"), list):
            raise ValueError("graph YAML requires a nodes list")
        dag = DependencyGraph(graph["nodes"])
        valid, errors = dag.validate()
        return {"graph_id": graph.get("id"), "valid": valid, "errors": errors,
                "node_count": len(dag.nodes),
                "topological_order": dag.topological_sort() if valid else None,
                "parallel_groups": dag.find_parallel_groups() if valid else None,
                "critical_path": dag.get_critical_path() if valid else None,
                "meaning": "structural DAG facts, not research validity"}
    if name == "claim_transfer":
        from core.claim_transfer import build_claim_transfer
        ids = a.get("claim_ids")
        if ids is not None and (not ids or any(not isinstance(x,str) or not x.strip() for x in ids)):
            raise ValueError("claim_ids must be a nonempty list of nonempty strings when supplied")
        return build_claim_transfer(a["claim_audit"], claim_ids=ids,
                                    purpose=a.get("purpose"))
    raise ValueError("unknown tool")


def execute_tool_call(name: str, arguments: dict | str) -> dict:
    """Dispatch an allowlisted call and return a stable JSON-serializable envelope.

    String arguments are accepted for model function-call interoperability.
    Domain findings live inside result; status=ok never means scientific truth.
    """
    envelope = {
        "profile": PROFILE, "tool": name, "status": "error",
        "result": None, "error": None,
        "scientific_validity_claim": False,
        "remote_provider_called": False,
    }
    if name not in TOOL_SPECS:
        envelope["error"] = {"code": "UNKNOWN_TOOL", "message": "tool is not allowlisted"}
        return envelope
    try:
        if isinstance(arguments, str):
            try:
                arguments = json.loads(arguments)
            except json.JSONDecodeError as exc:
                raise ValueError("arguments are not valid JSON") from exc
        checked = _check_arguments(name, arguments)
    except (ValueError, TypeError) as exc:
        envelope["error"] = {"code": "INVALID_ARGUMENT", "message": str(exc)}
        return envelope
    try:
        envelope["result"] = _dispatch(name, checked)
        envelope["status"] = "ok"
    except (OSError, ValueError, TypeError, KeyError, json.JSONDecodeError) as exc:
        envelope["error"] = {"code": "EXECUTION_FAILED", "message": str(exc)}
    except Exception as exc:
        # Third-party validators may raise domain-specific exception classes.
        # Preserve a structured failure, never emit a traceback on JSON stdout.
        envelope["error"] = {"code": "INTERNAL_ERROR", "message": type(exc).__name__ + ": " + str(exc)}
    return envelope


def list_tool_names() -> list[str]:
    return sorted(TOOL_SPECS)
