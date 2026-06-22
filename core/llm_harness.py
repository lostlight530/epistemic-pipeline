#!/usr/bin/env python3
"""
LLM 执行网关 (Agent Harness)
负责大模型的实例化、能力调用与结构化输出解析
"""

import json
import logging
from pathlib import Path
from typing import Dict, Any

logger = logging.getLogger(__name__)

class LLMHarness:
    """LLM 驱动器，组装 Prompt 并获取结构化输出"""

    def __init__(self, roles_dir: str = 'roles'):
        self.roles_dir = Path(roles_dir)

    def load_role_prompt(self, role_name: str) -> str:
        """加载角色能力包作为 System Prompt"""
        role_path = self.roles_dir / f"{role_name}.md"
        if role_path.exists():
            with open(role_path, 'r', encoding='utf-8') as f:
                return f.read()
        logger.warning(f"Role file for {role_name} not found. Using fallback prompt.")
        return f"You are a helpful {role_name} assistant."

    def build_prompt(self, state_id: str, role_bindings: Dict[str, str], inputs: Any) -> Dict[str, str]:
        """组装完整的请求 Prompt"""
        primary_role = role_bindings.get('primary', 'assistant')
        secondary_role = role_bindings.get('secondary', '')

        system_prompt = self.load_role_prompt(primary_role)
        if secondary_role:
            system_prompt += f"\n\nSecondary Role/Auditor Perspective: {self.load_role_prompt(secondary_role)}"

        user_prompt = f"Current State: {state_id}\n\nInputs:\n{json.dumps(inputs, ensure_ascii=False, indent=2)}\n\nPlease provide strictly structured JSON/YAML output based on your role constraints and schema definitions."

        return {
            "system": system_prompt,
            "user": user_prompt
        }

    def execute(self, state_id: str, role_bindings: Dict[str, str], inputs: Any, mock: bool = True) -> Dict[str, Any]:
        """执行模型调用并返回结构化数据 (支持模拟)"""
        prompts = self.build_prompt(state_id, role_bindings, inputs)

        if mock:
            print(f"  [LLM] 模拟调用大模型扮演 {role_bindings.get('primary')} 执行 {state_id} 任务...")
            if state_id.startswith('discover'):
                return {
                    "sources_index": [{"id": "src_001", "source": "mock_file.txt", "type": "paper", "extracted_at": "2023-10-01", "content_summary": "Summary"}],
                    "raw_extractions": [{"source_id": "src_001", "segment_id": "seg1", "raw_text": "Earth is flat.", "metadata": {"page": 1}}],
                    "annotated_corpus": [{"segment_id": "seg1", "annotation": "mock"}]
                }
            elif state_id.startswith('analyze'):
                return {
                    "entity_map": {"src_001": ["Earth"]},
                    "claims_registry": [{"claim_id": "c1", "text": "Earth is flat"}],
                    "evidence_chains": [{"claim_id": "c1", "evidence": "Looks flat from here"}],
                    "methodology_index": {"c1": "observation"},
                    "coverage": 1.0
                }
            elif state_id.startswith('verify'):
                return {
                    "internal_consistency_report": {"c1": "consistent"},
                    "cross_source_matrix": {"c1": "supported"},
                    "conflict_registry": [{"source": "c1", "target": "c2", "relation": "contradicts", "weight": 0.9}],
                    "confidence_seed": {"c1": 0.5},
                    "coverage": 0.96
                }
            elif state_id.startswith('synthesize'):
                return {
                    "confidence_network": {"c1": 0.9},
                    "comparison_matrix": {"c1": "high_confidence"},
                    "insight_list": ["The claim is highly debated."],
                    "synthesis_report": {"summary": "done", "details": "all done"},
                    "delta": 0.005
                }
            elif state_id.startswith('archive'):
                return {
                    "artifact_bundle": {"c1": "data"},
                    "provenance_chain": {"c1": "src_001"},
                    "metadata_package": {"author": "system"},
                    "audit_report": {"status": "passed", "details": "All good."}
                }

        raise NotImplementedError("Real LLM calling not implemented.")
