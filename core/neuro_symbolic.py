"""Rule Dispatch Bridge
[EXPERIMENTAL] Not integrated into the main execution engine.

Historical compatibility name: ``NeuroSymbolicBridge``.

The implementation does not run a neural network and it is not a theorem
prover. It accepts a caller-supplied pattern record, evaluates caller-supplied
Python predicates in priority order, and returns the first matching action.
The numeric ``confidence`` field is therefore an opaque upstream score unless
the caller separately provides calibrated semantics.
"""

from __future__ import annotations

import time
from dataclasses import dataclass, field
from typing import Any, Callable, Dict, List, Optional


@dataclass
class NeuralOutput:
    """Compatibility record for an externally produced pattern/score."""

    pattern_id: str
    confidence: float
    features: Dict[str, float] = field(default_factory=dict)
    raw_output: Any = None
    score_semantics: str = "opaque_upstream_score_not_calibrated_probability"


@dataclass
class SymbolicRule:
    """Caller-supplied predicate/action pair."""

    rule_id: str
    condition: Callable[[Dict[str, Any]], bool]
    action: str
    priority: int = 0
    description: str = ""


@dataclass
class BridgedResult:
    """Result of local predicate dispatch."""

    neural_pattern: str
    symbolic_action: str
    confidence: float
    rule_id: Optional[str] = None
    reasoning: str = ""
    score_semantics: str = "opaque_upstream_score_not_calibrated_probability"
    rule_errors: List[str] = field(default_factory=list)
    timestamp: float = field(default_factory=time.time)


class NeuroSymbolicBridge:
    """Compatibility facade for priority-ordered local rule dispatch."""

    def __init__(self):
        self._rules: List[SymbolicRule] = []
        self._neural_history: List[NeuralOutput] = []
        self._bridged_results: List[BridgedResult] = []
        self._pattern_to_rules: Dict[str, List[str]] = {}

    def register_rule(self, rule: SymbolicRule) -> None:
        if not rule.rule_id:
            raise ValueError("rule_id must be non-empty")
        self._rules = [existing for existing in self._rules if existing.rule_id != rule.rule_id]
        self._rules.append(rule)
        self._rules.sort(key=lambda item: (-item.priority, item.rule_id))

    def map_pattern_to_rule(self, pattern_id: str, rule_id: str) -> None:
        if not pattern_id or not rule_id:
            raise ValueError("pattern_id and rule_id must be non-empty")
        mapped = self._pattern_to_rules.setdefault(pattern_id, [])
        if rule_id not in mapped:
            mapped.append(rule_id)

    def bridge(
        self, neural_output: NeuralOutput, context: Optional[Dict[str, Any]] = None
    ) -> BridgedResult:
        """Evaluate eligible rules without mutating the caller's context mapping."""
        if not neural_output.pattern_id:
            raise ValueError("pattern_id must be non-empty")
        score = float(neural_output.confidence)
        if not 0.0 <= score <= 1.0:
            raise ValueError("confidence compatibility score must be within [0, 1]")

        self._neural_history.append(neural_output)
        local_context = dict(context or {})
        local_context.update(neural_output.features)
        local_context["_confidence"] = score
        local_context["_pattern"] = neural_output.pattern_id

        mapped_rule_ids = set(self._pattern_to_rules.get(neural_output.pattern_id, []))
        errors: List[str] = []

        for rule in self._rules:
            if mapped_rule_ids and rule.rule_id not in mapped_rule_ids:
                continue
            try:
                matched = bool(rule.condition(local_context))
            except Exception as exc:  # caller predicate failure is evidence, not silent success
                errors.append(f"{rule.rule_id}: {type(exc).__name__}: {exc}")
                continue
            if matched:
                result = BridgedResult(
                    neural_pattern=neural_output.pattern_id,
                    symbolic_action=rule.action,
                    confidence=score,
                    rule_id=rule.rule_id,
                    reasoning=(
                        f"Local rule '{rule.description or rule.rule_id}' matched "
                        f"pattern '{neural_output.pattern_id}'"
                    ),
                    score_semantics=neural_output.score_semantics,
                    rule_errors=errors,
                )
                self._bridged_results.append(result)
                return result

        result = BridgedResult(
            neural_pattern=neural_output.pattern_id,
            symbolic_action="default",
            confidence=score,
            rule_id=None,
            reasoning="No eligible local rule matched; default action selected.",
            score_semantics=neural_output.score_semantics,
            rule_errors=errors,
        )
        self._bridged_results.append(result)
        return result

    def batch_bridge(
        self, outputs: List[NeuralOutput], context: Optional[Dict[str, Any]] = None
    ) -> List[BridgedResult]:
        return [self.bridge(output, context) for output in outputs]

    def get_results(self, pattern: Optional[str] = None) -> List[BridgedResult]:
        if pattern:
            return [result for result in self._bridged_results if result.neural_pattern == pattern]
        return list(self._bridged_results)

    def rule_coverage(self) -> Dict[str, Any]:
        observed = {output.pattern_id for output in self._neural_history}
        mapped = observed.intersection(self._pattern_to_rules)
        return {
            "observed_patterns": len(observed),
            "mapped_observed_patterns": len(mapped),
            "unmapped_observed_patterns": len(observed - mapped),
            "coverage": len(mapped) / len(observed) if observed else 0.0,
            "registered_rules": len(self._rules),
            "semantics": "local_predicate_dispatch_not_formal_reasoning",
        }
