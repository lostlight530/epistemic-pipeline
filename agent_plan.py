#!/usr/bin/env python3
"""Bounded, explicit-approval execution of caller-provided agent tool plans.

A plan is declarative tool-call data, not autonomous reasoning. The caller
controls authorization, durable storage and any model-provider integration.
Preview never invokes a tool; approval is a caller flag, not authenticated IAM.
"""
from __future__ import annotations

from typing import Any
from agent_tools import PROFILE, TOOL_SPECS, _check_arguments, execute_tool_call

MAX_PLAN_STEPS = 16


def _plan_error(code: str, message: str) -> dict:
    return {"profile": PROFILE, "tool": "agent_plan", "status": "error",
            "result": None, "error": {"code": code, "message": message},
            "approval_granted": False, "scientific_validity_claim": False,
            "remote_provider_called": False}


def _preflight(plan: Any) -> dict:
    if not isinstance(plan, dict):
        raise ValueError("plan must be an object")
    allowed = {"steps", "purpose", "on_error"}
    if set(plan) - allowed:
        raise ValueError("unexpected plan keys: " + ", ".join(sorted(set(plan)-allowed)))
    purpose = plan.get("purpose")
    if purpose is not None and (not isinstance(purpose, str) or not purpose.strip()):
        raise ValueError("purpose must be a nonempty string when present")
    policy = plan.get("on_error", "stop")
    if policy not in {"stop", "continue"}:
        raise ValueError("on_error must be stop or continue")
    steps = plan.get("steps")
    if not isinstance(steps, list) or not 1 <= len(steps) <= MAX_PLAN_STEPS:
        raise ValueError("steps must contain 1 to 16 tool calls")
    normalized = []
    for index, step in enumerate(steps):
        if not isinstance(step, dict) or set(step) != {"tool", "arguments"}:
            raise ValueError(f"steps[{index}] must contain exactly tool and arguments")
        name = step["tool"]
        if not isinstance(name, str) or name not in TOOL_SPECS:
            raise ValueError(f"steps[{index}] tool is not allowlisted")
        try:
            arguments = _check_arguments(name, step["arguments"])
        except ValueError as exc:
            raise ValueError(f"steps[{index}]: {exc}") from exc
        normalized.append({"tool": name, "arguments": dict(arguments)})
    return {"purpose": purpose, "on_error": policy, "steps": normalized}


def _domain_failed(response: dict) -> bool:
    if response.get("status") != "ok":
        return True
    result = response.get("result")
    return isinstance(result, dict) and (
        result.get("valid") is False
        or result.get("diagnostic_exit_code", 0) != 0
        or result.get("check_status") == "failed"
    )


def run_plan(plan: dict, *, approved: bool = False) -> dict:
    """Preview by default; execute no more than 16 calls after explicit approval.

    No automatic parallelism, hidden retry, state mutation or tool discovery.
    An unapproved plan never reads tool-target files.
    """
    if not isinstance(approved, bool):
        return _plan_error("INVALID_ARGUMENT", "approved must be a boolean")
    try:
        normalized = _preflight(plan)
    except ValueError as exc:
        return _plan_error("INVALID_PLAN", str(exc))
    metadata = {"purpose": normalized["purpose"], "on_error": normalized["on_error"],
                "step_count": len(normalized["steps"])}
    if not approved:
        return {"profile": PROFILE, "tool": "agent_plan",
                "status": "approval_required",
                "result": {**metadata, "proposed_steps": normalized["steps"],
                           "executed": False},
                "error": {"code": "APPROVAL_REQUIRED",
                          "message": "review the plan and set approved=True before any tool call"},
                "approval_granted": False,
                "scientific_validity_claim": False, "remote_provider_called": False}

    results = []
    failed_at = None
    for index, step in enumerate(normalized["steps"]):
        response = execute_tool_call(step["tool"], step["arguments"])
        failed = _domain_failed(response)
        results.append({"index": index, "tool": step["tool"],
                        "domain_check_failed": failed, "response": response})
        if failed and failed_at is None:
            failed_at = index
            if normalized["on_error"] == "stop":
                break
    return {"profile": PROFILE, "tool": "agent_plan",
            "status": "error" if failed_at is not None else "ok",
            "result": {**metadata, "executed": True, "completed_steps": len(results),
                       "failed_at": failed_at, "step_results": results},
            "error": {"code": "STEP_FAILED", "message": f"tool step {failed_at} failed"}
                     if failed_at is not None else None,
            "approval_granted": True,
            "scientific_validity_claim": False, "remote_provider_called": False}
