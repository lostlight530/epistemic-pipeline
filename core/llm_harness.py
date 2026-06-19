#!/usr/bin/env python3
"""
LLM 执行网关 (Agent Harness)
负责大模型的实例化、能力调用与结构化输出解析
"""

import json
from pathlib import Path
from typing import Dict, Any

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
        return f"You are a helpful {role_name} assistant."

    def build_prompt(self, state_id: str, role_bindings: Dict[str, str], inputs: Any) -> Dict[str, str]:
        """组装完整的请求 Prompt"""
        primary_role = role_bindings.get('primary', 'assistant')
        system_prompt = self.load_role_prompt(primary_role)

        user_prompt = f"Current State: {state_id}\n\nInputs:\n{json.dumps(inputs, ensure_ascii=False, indent=2)}\n\nPlease provide structured output based on your role constraints."

        return {
            "system": system_prompt,
            "user": user_prompt
        }

    def execute(self, state_id: str, role_bindings: Dict[str, str], inputs: Any, mock: bool = True) -> Dict[str, Any]:
        """执行模型调用并返回结构化数据 (模拟)"""
        prompts = self.build_prompt(state_id, role_bindings, inputs)

        if mock:
            print(f"  [LLM] 模拟调用大模型扮演 {role_bindings.get('primary')} 执行 {state_id} 任务...")
            if state_id == 'discover':
                return {
                    "sources_index": [{"id": "src_001", "source": "mock_file.txt", "type": "paper", "extracted_at": "2023-10-01", "content_summary": "Summary"}],
                    "raw_extractions": [{"source_id": "src_001", "segment_id": "seg1", "raw_text": "Earth is flat.", "metadata": {"page": 1}}]
                }
            elif state_id == 'analyze':
                return {
                    "entity_map": {"src_001": ["Earth"]},
                    "claims_registry": [{"claim_id": "c1", "text": "Earth is flat"}],
                    "evidence_chains": [{"claim_id": "c1", "evidence": "Looks flat from here"}],
                    "coverage": 1.0
                }
            elif state_id == 'verify':
                return {
                    "internal_consistency_report": {},
                    "cross_source_matrix": {},
                    "conflict_registry": [{"source": "c1", "target": "c2", "relation": "contradicts", "weight": 0.9}],
                    "confidence_seed": {"c1": 0.5},
                    "coverage": 0.96
                }
            elif state_id == 'synthesize':
                return {
                    "confidence_network": {},
                    "comparison_matrix": {},
                    "insight_list": ["The claim is highly debated."],
                    "synthesis_report": {},
                    "delta": 0.005
                }
            elif state_id == 'archive':
                return {"provenance_chain": {}, "archived_data": True}

        return {"error": "Real LLM calling not implemented."}
