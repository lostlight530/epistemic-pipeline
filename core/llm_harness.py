#!/usr/bin/env python3
"""Provider-neutral structured-output harness for epistemic-pipeline.

``LLMHarness`` assembles role/state context and delegates completion to an
injected ``LLMProvider``. The repository ships only ``MockProvider`` as a
deterministic offline fixture. Mock outputs are test/development structures and
must never be presented as evidence of real model reasoning or scientific
validation.
"""

from __future__ import annotations

import json
import logging
import re
from abc import ABC, abstractmethod
from pathlib import Path
from typing import Any, Dict, Optional

logger = logging.getLogger(__name__)


class LLMProvider(ABC):
    """Vendor-neutral provider protocol: prompts/schema in, structured mapping out."""

    @abstractmethod
    def complete(
        self, system: str, user: str, schema: Optional[dict] = None
    ) -> Dict[str, Any]:
        raise NotImplementedError


class MockProvider(LLMProvider):
    """Deterministic offline fixture with bounded heuristic score semantics."""

    STAGE_CONTRACTS = {
        "discover": ["sources_index", "raw_extractions", "annotated_corpus"],
        "analyze": [
            "entity_map",
            "claims_registry",
            "evidence_chains",
            "methodology_index",
            "coverage",
        ],
        "verify": [
            "internal_consistency_report",
            "cross_source_matrix",
            "conflict_registry",
            "confidence_seed",
            "coverage",
        ],
        "synthesize": [
            "confidence_network",
            "comparison_matrix",
            "insight_list",
            "synthesis_report",
            "delta",
        ],
        "archive": [
            "artifact_bundle",
            "provenance_chain",
            "metadata_package",
            "audit_report",
        ],
    }

    def complete(
        self, system: str, user: str, schema: Optional[dict] = None
    ) -> Dict[str, Any]:
        del system, schema
        state_id = self._extract_state_id(user)
        if state_id.startswith("discover"):
            return {
                "sources_index": [
                    {
                        "id": "src_001",
                        "source": "mock_dataset.csv",
                        "type": "dataset",
                        "content_summary": "Synthetic tabular fixture",
                    }
                ],
                "raw_extractions": [
                    {
                        "source_id": "src_001",
                        "segment_id": "seg_001",
                        "raw_text": "Synthetic fixture contains 100 declared rows.",
                        "metadata": {"row_count_declared": 100},
                    }
                ],
                "annotated_corpus": [
                    {"segment_id": "seg_001", "annotation": "synthetic_fixture"}
                ],
            }
        if state_id.startswith("analyze"):
            return {
                "entity_map": {"src_001": ["synthetic_dataset"]},
                "claims_registry": [
                    {
                        "claim_id": "c1",
                        "text": "The synthetic fixture declares 100 rows.",
                        "source_refs": ["src_001"],
                    }
                ],
                "evidence_chains": [
                    {
                        "claim_id": "c1",
                        "evidence_refs": ["src_001#seg_001"],
                        "relation": "declared_by_fixture",
                    }
                ],
                "methodology_index": {"c1": "fixture_metadata_read"},
                "coverage": 1.0,
            }
        if state_id.startswith("verify"):
            return {
                "internal_consistency_report": {"c1": "no_internal_conflict_observed"},
                "cross_source_matrix": {"c1": "single_source_fixture"},
                "conflict_registry": [
                    {
                        "source": "c1",
                        "target": "scope_limit",
                        "relation": "limited_by",
                        "severity": "low",
                        "note": "Synthetic fixture is not external evidence.",
                    }
                ],
                "confidence_seed": {"c1": 0.5},
                "coverage": 0.96,
            }
        if state_id.startswith("synthesize"):
            return {
                "confidence_network": {"c1": 0.5},
                "comparison_matrix": {"c1": "single_fixture_only"},
                "insight_list": [
                    "The fixture is structurally traceable but provides no independent external corroboration."
                ],
                "synthesis_report": {
                    "summary": "Synthetic fixture processed.",
                    "comparison": "No independent source comparison is available in the mock fixture.",
                    "insights": ["Traceability does not establish truth."],
                    "recommendation": "Inject real evidence through an external provider/integration before scientific use.",
                    "confidence_semantics": "heuristic score in [0,1], not calibrated probability",
                },
                "delta": 0.005,
            }
        if state_id.startswith("archive"):
            return {
                "artifact_bundle": {"synthesis_report": "in-memory-mock-output"},
                "provenance_chain": {"c1": ["src_001#seg_001"]},
                "metadata_package": {
                    "profile": "epistemic-pipeline/mock-archive@1",
                    "generated_by": "MockProvider",
                    "content_semantics": "synthetic_fixture_not_external_evidence",
                },
                "audit_report": {
                    "status": "structure_complete",
                    "scientific_validity_claim": False,
                },
            }
        raise ValueError(f"MockProvider cannot route state_id={state_id!r}")

    @staticmethod
    def _extract_state_id(user_prompt: str) -> str:
        match = re.search(r"^Current State:\s*(\S+)", user_prompt, re.MULTILINE)
        if not match:
            raise ValueError("user prompt is missing the 'Current State:' routing line")
        return match.group(1)


class LLMHarness:
    """Assemble role prompts and obtain a structured mapping from a provider."""

    def __init__(self, roles_dir: str = "roles", provider: Optional[LLMProvider] = None):
        self.roles_dir = Path(roles_dir)
        self.provider = provider

    def load_role_prompt(self, role_name: str) -> str:
        path = self.roles_dir / f"{role_name}.md"
        if path.exists():
            return path.read_text(encoding="utf-8")
        logger.warning("Role file for %s not found; using bounded fallback prompt", role_name)
        return f"You are acting in the declared {role_name} role. Return only the requested structured fields."

    def build_prompt(
        self, state_id: str, role_bindings: Dict[str, str], inputs: Any
    ) -> Dict[str, str]:
        primary = role_bindings.get("primary", "assistant")
        secondary = role_bindings.get("secondary", "")
        system_prompt = self.load_role_prompt(primary)
        if secondary:
            system_prompt += (
                "\n\nSecondary review perspective:\n" + self.load_role_prompt(secondary)
            )
        user_prompt = (
            f"Current State: {state_id}\n\n"
            f"Inputs:\n{json.dumps(inputs, ensure_ascii=False, indent=2, default=str)}\n\n"
            "Return a structured mapping that follows the declared stage/role contract. "
            "Do not upgrade heuristic scores into probabilities or infer evidence that is not present in Inputs."
        )
        return {"system": system_prompt, "user": user_prompt}

    def execute(
        self,
        state_id: str,
        role_bindings: Dict[str, str],
        inputs: Any,
        mock: bool = True,
        schema: Optional[dict] = None,
    ) -> Dict[str, Any]:
        prompts = self.build_prompt(state_id, role_bindings, inputs)
        provider: Optional[LLMProvider] = self.provider
        if provider is None and mock:
            provider = MockProvider()
        if provider is None:
            raise NotImplementedError(
                "No real LLM provider is built into the repository; inject an LLMProvider implementation."
            )
        output = provider.complete(prompts["system"], prompts["user"], schema)
        if not isinstance(output, dict):
            raise TypeError("LLMProvider.complete must return a dict")
        return output
