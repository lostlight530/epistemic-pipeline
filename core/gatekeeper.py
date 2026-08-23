#!/usr/bin/env python3
"""Runtime policy evaluation for state outputs.

The historical ``Gatekeeper`` class name and ``check_quality_gates`` method are
retained for compatibility. The active semantics are runtime policy/constraint
evaluation, not GitHub merge gating.

State YAML keeps the historical ``quality_gates`` key but each active rule now
carries a machine-readable ``check`` plus parameters. Human ``rule`` text is
descriptive only and is never parsed to decide behavior.
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
        """Load repository-level reference rules; state checks are dispatched separately."""
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

    def _evaluate_rule(self, rule: Dict[str, Any], outputs: Dict[str, Any]) -> Tuple[bool, str]:
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
                    isinstance(item, dict) and all(name in item and item[name] is not None for name in required)
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
                claim_ids = {item.get(id_field) for item in claims if isinstance(item, dict) and item.get(id_field)}
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
                isinstance(item, dict) and all(name in item and item[name] is not None for name in required)
                for item in value
            )
        elif check == "mapping_required_keys":
            value = self._value(outputs, field)
            required = list(rule.get("required_keys") or [])
            passed = isinstance(value, dict) and all(key in value and value[key] is not None for key in required)
        else:
            return False, f"Policy [{rule_id}] unsupported check={check!r}; rule was not silently accepted"

        return passed, f"Policy [{rule_id}] failed: {human}"

    def evaluate(self, state_def: Dict[str, Any], outputs: Dict[str, Any]) -> Tuple[bool, List[str]]:
        """Evaluate all machine-readable runtime rules for one state output."""
        if not isinstance(outputs, dict):
            return False, ["MISSING_POLICY_INPUT: outputs must be a mapping"]
        rules = state_def.get("quality_gates", []) or []  # legacy key retained for compatibility
        if not isinstance(rules, list):
            return False, ["INVALID_POLICY_DEFINITION: quality_gates must be a list"]
        errors: List[str] = []
        for rule in rules:
            if not isinstance(rule, dict):
                errors.append("INVALID_POLICY_DEFINITION: rule must be a mapping")
                continue
            passed, message = self._evaluate_rule(rule, outputs)
            if not passed:
                errors.append(message)
        if errors and not outputs:
            errors.append("MISSING_POLICY_INPUT")
        return not errors, errors

    def check_quality_gates(
        self, state_def: Dict[str, Any], outputs: Dict[str, Any]
    ) -> Tuple[bool, List[str]]:
        """Backward-compatible wrapper for callers using the historical method name."""
        return self.evaluate(state_def, outputs)


class Gatekeeper(RuntimePolicyEvaluator):
    """Backward-compatible class name for ``RuntimePolicyEvaluator``."""

    pass
