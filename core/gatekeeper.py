#!/usr/bin/env python3
"""Runtime policy evaluation for state outputs.

``RuntimePolicyEvaluator`` is the active API. The historical ``Gatekeeper``
class name and ``check_quality_gates`` method are retained only as compatibility
aliases for older callers.

State YAML should use ``runtime_policies``. The legacy ``quality_gates`` key is
accepted only when ``runtime_policies`` is absent. Human-readable ``rule`` text
is descriptive; behavior is driven exclusively by machine-readable ``check``
and parameters.
"""

from __future__ import annotations

import logging
from pathlib import Path
from typing import Any, Dict, List, Tuple

import yaml

logger = logging.getLogger(__name__)
PROFILE = "epistemic-pipeline/runtime-policy@1"


class RuntimePolicyEvaluator:
    """Evaluate explicit state-output predicates declared in state YAML."""

    def __init__(self, validators_dir: str = "validators"):
        self.validators_dir = Path(validators_dir)
        self.rules = self._load_global_rules()

    def _load_global_rules(self) -> Dict[str, Any]:
        path = self.validators_dir / "epistemic.rules.yaml"
        if not path.exists():
            logger.warning("Global reference rules not found at %s", path)
            return {"rules": []}
        with path.open("r", encoding="utf-8") as handle:
            data = yaml.safe_load(handle) or {}
        return data if isinstance(data, dict) else {"rules": []}

    @staticmethod
    def _value(outputs: Dict[str, Any], field: str) -> Any:
        value: Any = outputs
        for part in str(field).split("."):
            if not isinstance(value, dict) or part not in value:
                return None
            value = value[part]
        return value

    @staticmethod
    def _non_empty(value: Any) -> bool:
        if value is None:
            return False
        if isinstance(value, (str, list, tuple, set, dict)):
            return len(value) > 0
        return True

    def _evaluate_rule(
        self, rule: Dict[str, Any], outputs: Dict[str, Any]
    ) -> Tuple[bool, str]:
        rule_id = str(rule.get("id") or "unnamed")
        check = str(rule.get("check") or "").strip()
        field = str(rule.get("field") or "")
        human = str(rule.get("rule") or rule.get("name") or rule_id)

        if check == "min_items":
            value = self._value(outputs, field)
            minimum = int(rule.get("min", 1))
            passed = isinstance(value, (list, tuple, set, dict)) and len(value) >= minimum
        elif check == "non_empty":
            passed = self._non_empty(self._value(outputs, field))
        elif check == "every_item_fields":
            value = self._value(outputs, field)
            required = list(rule.get("required_fields") or [])
            require_non_empty = bool(rule.get("require_non_empty", True))
            passed = isinstance(value, list) and (bool(value) or not require_non_empty)
            if passed:
                passed = all(
                    isinstance(item, dict)
                    and all(name in item and item[name] is not None for name in required)
                    for item in value
                )
        elif check == "claim_evidence_ratio":
            claims = self._value(outputs, str(rule.get("claims_field") or "claims_registry"))
            evidence = self._value(outputs, str(rule.get("evidence_field") or "evidence_chains"))
            id_field = str(rule.get("id_field") or "claim_id")
            minimum = float(rule.get("min_ratio", 0.8))
            if not isinstance(claims, list) or not claims:
                passed = False
            else:
                claim_ids = {
                    item.get(id_field)
                    for item in claims
                    if isinstance(item, dict) and item.get(id_field)
                }
                evidence_ids = {
                    item.get(id_field)
                    for item in (evidence or [])
                    if isinstance(item, dict) and item.get(id_field)
                }
                passed = bool(claim_ids) and len(claim_ids & evidence_ids) / len(claim_ids) >= minimum
        elif check == "numeric_min":
            value = self._value(outputs, field)
            try:
                passed = float(value) >= float(rule["min"])
            except (TypeError, ValueError, KeyError):
                passed = False
        elif check == "numeric_max_exclusive":
            value = self._value(outputs, field)
            try:
                passed = float(value) < float(rule["max"])
            except (TypeError, ValueError, KeyError):
                passed = False
        elif check == "conflicts_have_fields":
            value = self._value(outputs, field)
            required = list(rule.get("required_fields") or [])
            passed = isinstance(value, list) and all(
                isinstance(item, dict)
                and all(name in item and item[name] is not None for name in required)
                for item in value
            )
        elif check == "mapping_required_keys":
            value = self._value(outputs, field)
            required = list(rule.get("required_keys") or [])
            passed = isinstance(value, dict) and all(
                key in value and value[key] is not None for key in required
            )
        else:
            return (
                False,
                f"Policy [{rule_id}] unsupported check={check!r}; rule was not silently accepted",
            )

        return passed, f"Policy [{rule_id}] failed: {human}"

    @staticmethod
    def _policy_definitions(state_def: Dict[str, Any]) -> Tuple[List[dict], str]:
        if "runtime_policies" in state_def:
            rules = state_def.get("runtime_policies") or []
            source = "runtime_policies"
        else:
            rules = state_def.get("quality_gates") or []
            source = "quality_gates_legacy"
        if not isinstance(rules, list):
            raise TypeError(f"{source} must be a list")
        return rules, source

    def evaluate(
        self, state_def: Dict[str, Any], outputs: Dict[str, Any]
    ) -> Tuple[bool, List[str]]:
        if not isinstance(outputs, dict):
            return False, ["MISSING_POLICY_INPUT: outputs must be a mapping"]
        try:
            rules, _source = self._policy_definitions(state_def)
        except TypeError as exc:
            return False, [f"INVALID_POLICY_DEFINITION: {exc}"]

        errors: List[str] = []
        for rule in rules:
            if not isinstance(rule, dict):
                errors.append("INVALID_POLICY_DEFINITION: policy must be a mapping")
                continue
            passed, message = self._evaluate_rule(rule, outputs)
            if not passed:
                errors.append(message)
        if errors and not outputs:
            errors.append("MISSING_POLICY_INPUT")
        return not errors, errors

    def describe(self, state_def: Dict[str, Any]) -> dict:
        rules, source = self._policy_definitions(state_def)
        return {
            "profile": PROFILE,
            "source_key": source,
            "policy_ids": [str(rule.get("id") or "unnamed") for rule in rules if isinstance(rule, dict)],
        }

    def check_quality_gates(
        self, state_def: Dict[str, Any], outputs: Dict[str, Any]
    ) -> Tuple[bool, List[str]]:
        """Deprecated compatibility wrapper; use ``evaluate``."""
        return self.evaluate(state_def, outputs)


class Gatekeeper(RuntimePolicyEvaluator):
    """Deprecated compatibility class name for ``RuntimePolicyEvaluator``."""

    pass
