#!/usr/bin/env python3
"""
知识提取与对齐 (Knowledge Extractor)
将大模型输出的结构化断言转化为 ConfidenceNetwork 能够识别的节点和边
"""

from typing import Dict, Any, List

class KnowledgeExtractor:
    """提取器：桥接 LLM 文本输出与图网络"""

    @staticmethod
    def extract_to_network_format(llm_claims: List[Dict[str, Any]], conflicts: List[Dict[str, Any]]) -> Dict[str, Any]:
        """
        将 LLM 输出的 claims_registry 和 conflict_registry 转化为 network inputs
        """
        nodes = []
        for claim in llm_claims:
            nodes.append({
                "claim_id": claim.get("claim_id"),
                "initial_confidence": claim.get("initial_confidence", 0.5)
            })

        edges = []
        for conflict in conflicts:
            edges.append({
                "source": conflict.get("source"),
                "target": conflict.get("target"),
                "weight": conflict.get("weight", 0.5),
                "edge_type": conflict.get("relation", "related")
            })

        return {"nodes": nodes, "edges": edges}
