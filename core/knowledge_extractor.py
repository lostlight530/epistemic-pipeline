#!/usr/bin/env python3
"""Bridge structured claims/conflicts into ConfidenceNetwork input.

This helper performs structural normalization only. It does not extract facts
from free text, infer truth, create missing evidence, or calibrate scores.
"""

from __future__ import annotations

from typing import Any, Dict, List

EDGE_TYPES = {"supports", "contradicts", "related", "derives"}


class KnowledgeExtractor:
    """Normalize claim/conflict records for the bounded score network."""

    @staticmethod
    def extract_to_network_format(
        llm_claims: List[Dict[str, Any]],
        conflicts: List[Dict[str, Any]],
    ) -> Dict[str, Any]:
        if not isinstance(llm_claims, list) or not isinstance(conflicts, list):
            raise TypeError("claims and conflicts must be lists")

        nodes = []
        seen_claims = set()
        for claim in llm_claims:
            if not isinstance(claim, dict):
                raise TypeError("each claim must be a mapping")
            claim_id = claim.get("claim_id")
            if not isinstance(claim_id, str) or not claim_id.strip():
                raise ValueError("each claim must have a non-empty claim_id")
            if claim_id in seen_claims:
                raise ValueError(f"duplicate claim_id: {claim_id}")
            seen_claims.add(claim_id)
            raw_score = claim.get("initial_confidence", claim.get("initial_score", 0.5))
            score = float(raw_score)
            if not 0.0 <= score <= 1.0:
                raise ValueError(f"initial score for {claim_id} must be in [0,1]")
            nodes.append({"claim_id": claim_id, "initial_confidence": score})

        edges = []
        for conflict in conflicts:
            if not isinstance(conflict, dict):
                raise TypeError("each conflict/relation must be a mapping")
            source = conflict.get("source")
            target = conflict.get("target")
            relation = str(conflict.get("relation") or "related")
            if not source or not target:
                raise ValueError("each relation must declare source and target")
            if relation not in EDGE_TYPES:
                raise ValueError(f"unsupported relation type: {relation}")
            weight = float(conflict.get("weight", 0.5))
            edges.append(
                {
                    "source": str(source),
                    "target": str(target),
                    "weight": weight,
                    "edge_type": relation,
                }
            )

        return {
            "profile": "epistemic-pipeline/network-input@1",
            "semantics": "structural bridge only; scores are heuristic unless separately evidenced",
            "nodes": nodes,
            "edges": edges,
        }
