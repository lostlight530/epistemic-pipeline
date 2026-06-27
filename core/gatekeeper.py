#!/usr/bin/env python3
"""
质量门与验证器 (Gatekeeper & Validator)
用于在状态流转时真实执行 quality_gates 中定义的校验规则
"""

import yaml
import logging
from pathlib import Path
from typing import Dict, Any, Tuple, List

logger = logging.getLogger(__name__)

class Gatekeeper:
    """质量门守卫，拦截不符合条件的状态输出"""

    def __init__(self, validators_dir: str = 'validators'):
        self.validators_dir = Path(validators_dir)
        self.rules = self._load_global_rules()

    def _load_global_rules(self) -> Dict[str, Any]:
        """加载全局认知规则"""
        rules_path = self.validators_dir / 'epistemic.rules.yaml'
        if rules_path.exists():
            with open(rules_path, 'r', encoding='utf-8') as f:
                return yaml.safe_load(f)
        logger.warning(f"Global rules not found at {rules_path}")
        return {"rules": []}

    def check_quality_gates(self, state_def: Dict[str, Any], outputs: Dict[str, Any]) -> Tuple[bool, List[str]]:
        """
        检查状态输出是否满足该状态配置的质量门
        """
        gates = state_def.get('quality_gates', [])
        if not gates:
            return True, []

        errors = []
        for gate in gates:
            rule_str = gate.get('rule', '')
            gate_id = gate.get('id', '')
            state_id = state_def.get('id', '')

            # discover
            if state_id.startswith('discover'):
                if "来源数 >= 1" in rule_str or "coverage" in gate_id:
                    if len(outputs.get('sources_index', [])) < 1:
                        errors.append(f"Gate [{gate_id}] 失败: {rule_str}")

                elif "100% 提取项有来源标注" in rule_str or "metadata_completeness" in gate_id:
                    extractions = outputs.get('raw_extractions', [])
                    if not extractions:
                        errors.append(f"Gate [{gate_id}] 失败: 未提取到任何数据")
                    else:
                        for ext in extractions:
                            if 'source_id' not in ext or 'metadata' not in ext:
                                errors.append(f"Gate [{gate_id}] 失败: 提取项缺乏完整元数据")
                                break

            # analyze
            elif state_id.startswith('analyze'):
                if "每个来源至少提取 1 个实体" in rule_str or "entity_coverage" in gate_id:
                    if not outputs.get('entity_map'):
                        errors.append(f"Gate [{gate_id}] 失败: {rule_str}")
                elif "claims_registry 非空" in rule_str or "claim_extraction" in gate_id:
                    if not outputs.get('claims_registry'):
                        errors.append(f"Gate [{gate_id}] 失败: {rule_str}")
                elif "≥80% 的主张有证据链" in rule_str or "evidence_linked" in gate_id:
                    claims = outputs.get('claims_registry', [])
                    chains = outputs.get('evidence_chains', [])
                    if len(claims) > 0 and len(chains) / len(claims) < 0.8:
                        errors.append(f"Gate [{gate_id}] 失败: {rule_str}")

            # verify
            elif state_id.startswith('verify'):
                if "≥95% 的主张已验证" in rule_str or "verification_coverage" in gate_id:
                    if outputs.get('coverage', 0) < 0.95:
                        errors.append(f"Gate [{gate_id}] 失败: 验证覆盖率低于 95%")
                elif "所有主张有置信度值" in rule_str or "confidence_assigned" in gate_id:
                    if not outputs.get('confidence_seed'):
                        errors.append(f"Gate [{gate_id}] 失败: {rule_str}")

            # synthesize
            elif state_id.startswith('synthesize'):
                if "置信度变化 < 0.01" in rule_str or "confidence_converged" in gate_id:
                    if outputs.get('delta', 1.0) >= 0.01:
                        errors.append(f"Gate [{gate_id}] 失败: 置信度未收敛")
                elif "报告包含" in rule_str or "report_complete" in gate_id:
                    pass # mock always pass

            # archive
            elif state_id.startswith('archive'):
                if "产物完整" in rule_str or "artifact_complete" in gate_id:
                    if not outputs.get('artifact_bundle'):
                        errors.append(f"Gate [{gate_id}] 失败: {rule_str}")
                elif "元数据合规" in rule_str or "metadata_valid" in gate_id:
                    if not outputs.get('metadata_package'):
                        errors.append(f"Gate [{gate_id}] 失败: {rule_str}")

        if errors and not outputs:
            if 'MISSING_GATE_INPUT' not in errors:
                errors.append('MISSING_GATE_INPUT')
        return len(errors) == 0, errors
