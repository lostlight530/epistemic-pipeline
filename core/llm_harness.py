#!/usr/bin/env python3
"""
LLM 执行网关 (Agent Harness)
负责大模型的实例化、能力调用与结构化输出解析

Provider 协议抽象：LLMHarness 不再直接内嵌模型调用逻辑，
而是依赖注入一个满足 LLMProvider 协议的 provider：
    complete(system: str, user: str, schema: dict | None) -> dict
MockProvider 承载既有的确定性桩数据逻辑；未来接入真实 LLM
（Kimi / 百炼 / OpenAI 等）时实现同一协议即可复用全部契约测试。
"""

import json
import logging
import re
from abc import ABC, abstractmethod
from pathlib import Path
from typing import Dict, Any, Optional

logger = logging.getLogger(__name__)


class LLMProvider(ABC):
    """
    LLM Provider 协议：system/user/schema 进，结构化 dict 出。
    任何真实或模拟的模型通道都必须实现该协议才能接入执行链。
    """

    @abstractmethod
    def complete(self, system: str, user: str, schema: Optional[dict] = None) -> Dict[str, Any]:
        """执行一次模型调用并返回结构化输出字典"""
        raise NotImplementedError


class MockProvider(LLMProvider):
    """
    确定性 mock provider：产出固定桩数据，用于离线开发与测试。
    诚实声明：这些输出是启发式桩值，不代表任何真实模型的推理能力；
    其中的置信度数值是启发值而非校准概率。
    """

    #: 各阶段结构化输出的契约键（契约测试以此为准，质量门依赖同名键）
    STAGE_CONTRACTS = {
        'discover': ['sources_index', 'raw_extractions', 'annotated_corpus'],
        'analyze': ['entity_map', 'claims_registry', 'evidence_chains',
                    'methodology_index', 'coverage'],
        'verify': ['internal_consistency_report', 'cross_source_matrix',
                   'conflict_registry', 'confidence_seed', 'coverage'],
        'synthesize': ['confidence_network', 'comparison_matrix',
                       'insight_list', 'synthesis_report', 'delta'],
        'archive': ['artifact_bundle', 'provenance_chain',
                    'metadata_package', 'audit_report'],
    }

    def complete(self, system: str, user: str, schema: Optional[dict] = None) -> Dict[str, Any]:
        state_id = self._extract_state_id(user)
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
        raise ValueError(f"MockProvider 无法识别的 state_id: {state_id!r}")

    @staticmethod
    def _extract_state_id(user_prompt: str) -> str:
        """从 harness 组装的用户 Prompt 首行解析 Current State 标识"""
        match = re.search(r'^Current State:\s*(\S+)', user_prompt, re.MULTILINE)
        if not match:
            raise ValueError("用户 Prompt 缺少 'Current State:' 行，无法路由 mock 分支")
        return match.group(1)


class LLMHarness:
    """LLM 驱动器，组装 Prompt 并获取结构化输出"""

    def __init__(self, roles_dir: str = 'roles', provider: Optional[LLMProvider] = None):
        self.roles_dir = Path(roles_dir)
        self.provider = provider

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

    def execute(self, state_id: str, role_bindings: Dict[str, str], inputs: Any,
                mock: bool = True, schema: Optional[dict] = None) -> Dict[str, Any]:
        """执行模型调用并返回结构化数据 (支持模拟)"""
        prompts = self.build_prompt(state_id, role_bindings, inputs)

        if self.provider is not None:
            # 显式注入的 provider 优先（mock 标志仅作记录，不改变路由）
            return self.provider.complete(prompts['system'], prompts['user'], schema)

        if mock:
            print(f"  [LLM] 模拟调用大模型扮演 {role_bindings.get('primary')} 执行 {state_id} 任务...")
            return MockProvider().complete(prompts['system'], prompts['user'], schema)

        raise NotImplementedError("Real LLM calling not implemented.")
