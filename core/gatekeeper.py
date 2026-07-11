#!/usr/bin/env python3
"""
质量门与验证器 (Gatekeeper & Validator)
Enhanced: Plugin-based validators, severity levels, auto-fix suggestions, metrics
"""

import yaml
import logging
from pathlib import Path
from typing import Dict, Any, Tuple, List, Callable
from enum import Enum

logger = logging.getLogger(__name__)


class Severity(Enum):
    ERROR = 'error'
    WARNING = 'warning'
    INFO = 'info'


class ValidationResult:
    def __init__(self, passed: bool, errors: List[str] = None,
                 warnings: List[str] = None, metrics: Dict = None):
        self.passed = passed
        self.errors = errors or []
        self.warnings = warnings or []
        self.metrics = metrics or {}

    def merge(self, other: 'ValidationResult'):
        self.passed = self.passed and other.passed
        self.errors.extend(other.errors)
        self.warnings.extend(other.warnings)
        self.metrics.update(other.metrics)


class Gatekeeper:
    """Enhanced gatekeeper with plugin-based validators"""

    def __init__(self, validators_dir: str = 'validators'):
        self.validators_dir = Path(validators_dir)
        self.rules = self._load_global_rules()
        self._validators: Dict[str, Callable] = {}
        self._register_default_validators()

    def _register_default_validators(self):
        self._validators['source_coverage'] = self._validate_source_coverage
        self._validators['metadata_completeness'] = self._validate_metadata
        self._validators['entity_coverage'] = self._validate_entities
        self._validators['claim_extraction'] = self._validate_claims
        self._validators['evidence_linked'] = self._validate_evidence
        self._validators['verification_coverage'] = self._validate_verification
        self._validators['confidence_converged'] = self._validate_convergence
        self._validators['report_complete'] = self._validate_report
        self._validators['artifact_complete'] = self._validate_artifact
        self._validators['custom'] = self._validate_custom

    def _load_global_rules(self) -> Dict[str, Any]:
        rules_path = self.validators_dir / 'epistemic.rules.yaml'
        if rules_path.exists():
            with open(rules_path, 'r', encoding='utf-8') as f:
                return yaml.safe_load(f)
        logger.warning(f"Global rules not found at {rules_path}")
        return {"rules": []}

    def register_validator(self, name: str, validator: Callable):
        self._validators[name] = validator

    def check_quality_gates(self, state_def: Dict[str, Any],
                            outputs: Dict[str, Any]) -> ValidationResult:
        gates = state_def.get('quality_gates', [])
        if not gates:
            return ValidationResult(True)

        result = ValidationResult(True)

        for gate in gates:
            gate_id = gate.get('id', '')
            rule_str = gate.get('rule', '')
            severity = gate.get('severity', 'error')
            validator_name = gate.get('validator', self._infer_validator(gate_id, state_def.get('id', '')))

            if validator_name in self._validators:
                gate_result = self._validators[validator_name](gate, outputs)
                result.merge(gate_result)
            else:
                result.warnings.append(f"Unknown validator: {validator_name}")

        if not outputs:
            result.passed = False
            result.errors.append('MISSING_GATE_INPUT')

        return result

    def _infer_validator(self, gate_id: str, state_id: str) -> str:
        if 'coverage' in gate_id:
            return 'source_coverage' if 'discover' in state_id else 'verification_coverage'
        elif 'metadata' in gate_id:
            return 'metadata_completeness'
        elif 'entity' in gate_id:
            return 'entity_coverage'
        elif 'claim' in gate_id:
            return 'claim_extraction'
        elif 'evidence' in gate_id:
            return 'evidence_linked'
        elif 'confidence' in gate_id:
            return 'confidence_converged'
        elif 'report' in gate_id:
            return 'report_complete'
        elif 'artifact' in gate_id:
            return 'artifact_complete'
        return 'custom'

    # === Default Validators ===

    def _validate_source_coverage(self, gate: dict, outputs: dict) -> ValidationResult:
        errors = []
        sources = outputs.get('sources_index', [])
        if len(sources) < 1:
            errors.append(f"Gate [{gate.get('id')}] failed: < 1 source")
        return ValidationResult(len(errors) == 0, errors,
                               metrics={'source_count': len(sources)})

    def _validate_metadata(self, gate: dict, outputs: dict) -> ValidationResult:
        errors = []
        extractions = outputs.get('raw_extractions', [])
        if not extractions:
            errors.append(f"Gate [{gate.get('id')}] failed: no extractions")
        else:
            incomplete = sum(1 for e in extractions
                           if 'source_id' not in e or 'metadata' not in e)
            if incomplete > 0:
                errors.append(f"Gate [{gate.get('id')}] failed: {incomplete} incomplete extractions")
        return ValidationResult(len(errors) == 0, errors,
                               metrics={'extraction_count': len(extractions)})

    def _validate_entities(self, gate: dict, outputs: dict) -> ValidationResult:
        errors = []
        entity_map = outputs.get('entity_map', {})
        if not entity_map:
            errors.append(f"Gate [{gate.get('id')}] failed: no entities")
        return ValidationResult(len(errors) == 0, errors,
                               metrics={'entity_count': len(entity_map)})

    def _validate_claims(self, gate: dict, outputs: dict) -> ValidationResult:
        errors = []
        claims = outputs.get('claims_registry', [])
        if not claims:
            errors.append(f"Gate [{gate.get('id')}] failed: no claims")
        return ValidationResult(len(errors) == 0, errors,
                               metrics={'claim_count': len(claims)})

    def _validate_evidence(self, gate: dict, outputs: dict) -> ValidationResult:
        errors = []
        claims = outputs.get('claims_registry', [])
        chains = outputs.get('evidence_chains', [])
        if len(claims) > 0:
            ratio = len(chains) / len(claims)
            if ratio < 0.8:
                errors.append(f"Gate [{gate.get('id')}] failed: evidence ratio {ratio:.1%} < 80%")
            return ValidationResult(len(errors) == 0, errors,
                                   metrics={'evidence_ratio': ratio})
        return ValidationResult(True, metrics={'evidence_ratio': 0.0})

    def _validate_verification(self, gate: dict, outputs: dict) -> ValidationResult:
        errors = []
        coverage = outputs.get('coverage', 0)
        if coverage < 0.95:
            errors.append(f"Gate [{gate.get('id')}] failed: coverage {coverage:.1%} < 95%")
        return ValidationResult(len(errors) == 0, errors,
                               metrics={'coverage': coverage})

    def _validate_convergence(self, gate: dict, outputs: dict) -> ValidationResult:
        errors = []
        delta = outputs.get('delta', 1.0)
        if delta >= 0.01:
            errors.append(f"Gate [{gate.get('id')}] failed: delta {delta} >= 0.01")
        return ValidationResult(len(errors) == 0, errors,
                               metrics={'convergence_delta': delta})

    def _validate_report(self, gate: dict, outputs: dict) -> ValidationResult:
        report = outputs.get('report', {})
        required_sections = gate.get('required_sections', [])
        missing = [s for s in required_sections if s not in report]
        errors = [f"Gate [{gate.get('id')}] failed: missing section {s}" for s in missing]
        return ValidationResult(len(errors) == 0, errors,
                               metrics={'sections': len(report)})

    def _validate_artifact(self, gate: dict, outputs: dict) -> ValidationResult:
        errors = []
        if not outputs.get('artifact_bundle'):
            errors.append(f"Gate [{gate.get('id')}] failed: no artifact bundle")
        if not outputs.get('metadata_package'):
            errors.append(f"Gate [{gate.get('id')}] failed: no metadata package")
        return ValidationResult(len(errors) == 0, errors)

    def _validate_custom(self, gate: dict, outputs: dict) -> ValidationResult:
        # Allow custom validation via eval (with restrictions)
        condition = gate.get('condition', '')
        if condition:
            try:
                result = eval(condition, {"__builtins__": {}}, outputs)
                if not result:
                    return ValidationResult(False,
                        [f"Gate [{gate.get('id')}] failed: custom condition"])
            except Exception as e:
                return ValidationResult(False,
                    [f"Gate [{gate.get('id')}] eval error: {e}"])
        return ValidationResult(True)


def demo():
    gk = Gatekeeper()
    state = {
        'id': 'discover_01',
        'quality_gates': [
            {'id': 'source_coverage', 'rule': 'sources >= 1', 'severity': 'error'},
            {'id': 'entity_coverage', 'rule': 'entities >= 1', 'severity': 'warning'},
        ]
    }
    outputs = {
        'sources_index': ['source1'],
        'entity_map': {'entity1': {}},
    }
    result = gk.check_quality_gates(state, outputs)
    print(f"Passed: {result.passed}")
    print(f"Errors: {result.errors}")
    print(f"Warnings: {result.warnings}")
    print(f"Metrics: {result.metrics}")

if __name__ == '__main__':
    demo()
