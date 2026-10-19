#!/usr/bin/env python3
"""Local Tool / CLI / agent-plan adapter for the repository's existing core.

This is a bounded JSON invocation protocol, NOT an MCP transport/server.
It does not invoke a language model or run arbitrary shell commands.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
import sys
import tempfile
from pathlib import Path
from typing import Any

REPOSITORY = "epistemic-pipeline"
PROFILE = REPOSITORY + "/tool-execution"
TOOL_DEFINITIONS = [
    {
        "name": "graph.inspect",
        "description": "Validate a declared dependency graph; output DAG structure only, not scientific correctness.",
        "inputSchema": {
            "type": "object",
            "properties": {
                "nodes": {
                    "type": "array",
                    "items": {
                        "type": "object"
                    }
                }
            },
            "required": [
                "nodes"
            ],
            "additionalProperties": false
        }
    },
    {
        "name": "claim.transfer",
        "description": "In-memory bounded claim-transfer from an existing claim-audit JSON file.",
        "inputSchema": {
            "type": "object",
            "properties": {
                "claim_audit_path": {
                    "type": "string"
                },
                "claim_ids": {
                    "type": "array",
                    "items": {
                        "type": "string"
                    }
                },
                "purpose": {
                    "type": "string"
                }
            },
            "required": [
                "claim_audit_path"
            ],
            "additionalProperties": false
        }
    }
]


def _digest(value: Any) -> str:
    raw = json.dumps(value, sort_keys=True, ensure_ascii=False,
                     separators=(",", ":"), default=str).encode("utf-8")
    return "sha256:" + hashlib.sha256(raw).hexdigest()


def _validate_args(name: str, args: Any) -> None:
    spec = next((item for item in TOOL_DEFINITIONS if item["name"] == name), None)
    if spec is None:
        raise ValueError(f"tool not allowlisted: {name}")
    if not isinstance(args, dict):
        raise TypeError("tool arguments must be a JSON object")
    schema = spec["inputSchema"]
    unknown = set(args) - set(schema["properties"])
    if unknown:
        raise ValueError(f"unknown tool arguments: {sorted(unknown)}")
    missing = [key for key in schema["required"] if key not in args]
    if missing:
        raise ValueError(f"missing required arguments: {missing}")
    types = {"string": str, "boolean": bool, "array": list, "object": dict}
    for key, value in args.items():
        kind = schema["properties"][key]["type"]
        if not isinstance(value, types[kind]):
            raise TypeError(f"{key} must be {kind}")
        if kind == "string" and not value.strip():
            raise ValueError(f"{key} must be nonempty")


def _dispatch(name: str, args: dict) -> dict:

    if name == "graph.inspect":
        from core.dependency_graph import DependencyGraph
        graph = DependencyGraph(args["nodes"])
        valid, errors = graph.validate()
        data = {
            "profile": "epistemic-pipeline/graph-inspection",
            "valid": valid,
            "errors": errors,
            "node_count": len(graph.nodes),
            "cycles": graph.detect_cycles(),
            "scientific_validity_claim": False,
        }
        if valid:
            data["topological_order"] = graph.topological_sort()
            data["parallel_groups"] = graph.find_parallel_groups()
            data["critical_path"] = graph.get_critical_path()
        return data
    if name == "claim.transfer":
        from core.claim_transfer import build_claim_transfer
        return build_claim_transfer(
            args["claim_audit_path"],
            claim_ids=args.get("claim_ids"),
            purpose=args.get("purpose"),
        )
    raise ValueError(f"tool not allowlisted: {name}")


def invoke(name: str, args: Any) -> dict:
    """One typed receipt: local invocation result, not a truth verdict."""
    receipt = {
        "profile": PROFILE,
        "repository": REPOSITORY,
        "tool": name,
        "input_sha256": _digest(args),
        "status": "failed",
        "assertion_basis": "local-tool-invocation",
        "scientific_validity_claim": False,
        "independent_reproduction_claim": False,
    }
    try:
        _validate_args(name, args)
        receipt["output"] = _dispatch(name, args)
        receipt["status"] = "success"
    except Exception as exc:  # Core/schema failures remain structured tool errors.
        receipt["error"] = {"type": type(exc).__name__, "message": str(exc)}
    return receipt


def run_plan(plan: Any) -> dict:
    """Bounded deterministic coordinator; no model or implicit approval."""
    if not isinstance(plan, dict) or set(plan) != {"steps"}:
        raise ValueError("plan must contain only a steps array")
    steps = plan["steps"]
    if not isinstance(steps, list) or not 1 <= len(steps) <= 32:
        raise ValueError("plan must contain between 1 and 32 steps")
    ids: set[str] = set()
    results = []
    for index, step in enumerate(steps):
        if not isinstance(step, dict) or set(step) != {"id", "tool", "arguments"}:
            raise ValueError(f"step[{index}] requires id, tool and arguments")
        step_id = step["id"]
        if not isinstance(step_id, str) or not step_id or step_id in ids:
            raise ValueError(f"step[{index}] has blank or duplicate id")
        if not isinstance(step["tool"], str):
            raise ValueError(f"step[{index}] tool must be a string")
        ids.add(step_id)
        receipt = invoke(step["tool"], step["arguments"])
        results.append({"id": step_id, "receipt": receipt})
        if receipt["status"] != "success":
            break
    return {
        "profile": REPOSITORY + "/agent-plan",
        "repository": REPOSITORY,
        "plan_sha256": _digest(plan),
        "status": "failed" if results[-1]["receipt"]["status"] != "success" else "success",
        "completed_steps": len(results),
        "requested_steps": len(steps),
        "steps": results,
        "execution_mode": "deterministic-declared-plan-no-model",
        "scientific_validity_claim": False,
    }


def _read_input(path: str) -> Any:
    text = sys.stdin.read() if path == "-" else Path(path).read_text(encoding="utf-8")
    return json.loads(text)


def _write_atomic(path: str, content: str) -> None:
    target = Path(path)
    target.parent.mkdir(parents=True, exist_ok=True)
    fd, temporary = tempfile.mkstemp(dir=str(target.parent), prefix="." + target.name + ".")
    try:
        with os.fdopen(fd, "w", encoding="utf-8") as handle:
            handle.write(content)
            handle.flush()
            os.fsync(handle.fileno())
        os.replace(temporary, target)
    finally:
        if os.path.exists(temporary):
            os.unlink(temporary)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Local bounded Tool/CLI/agent-plan interface")
    parser.add_argument("command", choices=("list", "call", "agent"))
    parser.add_argument("tool", nargs="?", help="allowlisted tool for call")
    parser.add_argument("--input", default="-", help="JSON file or stdin (-)")
    parser.add_argument("--output", help="optional explicit atomic JSON receipt output")
    args = parser.parse_args(argv)
    try:
        if args.command == "list":
            if args.tool:
                raise ValueError("list takes no tool argument")
            result = {"profile": REPOSITORY + "/tool-catalog", "tools": TOOL_DEFINITIONS}
        elif args.command == "call":
            if not args.tool:
                raise ValueError("call requires a tool name")
            result = invoke(args.tool, _read_input(args.input))
        else:
            if args.tool:
                raise ValueError("agent takes no tool argument")
            result = run_plan(_read_input(args.input))
    except Exception as exc:  # Malformed JSON/plan remains a structured CLI failure.
        result = {"profile": PROFILE, "status": "failed",
                  "error": {"type": type(exc).__name__, "message": str(exc)}}
    rendered = json.dumps(result, indent=2, ensure_ascii=False, default=str) + "\n"
    if args.output:
        try:
            _write_atomic(args.output, rendered)
        except OSError as exc:
            result = {"profile": PROFILE, "status": "failed",
                      "error": {"type": type(exc).__name__, "message": str(exc)}}
            rendered = json.dumps(result, indent=2, ensure_ascii=False) + "\n"
    sys.stdout.write(rendered)
    return 1 if result.get("status") == "failed" else 0


if __name__ == "__main__":
    raise SystemExit(main())
