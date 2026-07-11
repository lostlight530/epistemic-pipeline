#!/usr/bin/env python3
"""
置信度传播网络 — 在知识主张间传播和收敛置信度
Enhanced: Belief propagation with damping, convergence metrics, cycle detection, uncertainty quantification
"""

import numpy as np
from typing import Dict, List, Tuple, Optional, Set
from dataclasses import dataclass
import logging

logger = logging.getLogger('confidence_net')


@dataclass
class ConfidenceNode:
    claim_id: str
    initial: float
    current: float
    previous: float
    iterations: int = 0
    stable: bool = False
    uncertainty: float = 1.0  # Higher = more uncertain


@dataclass
class ConfidenceEdge:
    source: str
    target: str
    weight: float
    edge_type: str  # supports, contradicts, related, derives


class ConfidenceNetwork:
    """Enhanced confidence propagation network with damping and uncertainty"""

    def __init__(self, threshold: float = 0.01, max_iterations: int = 100,
                 damping: float = 0.5):
        self.threshold = threshold
        self.max_iterations = max_iterations
        self.damping = damping
        self.nodes: Dict[str, ConfidenceNode] = {}
        self.edges: List[ConfidenceEdge] = []
        self.adjacency: Dict[str, List[Tuple[str, float, str]]] = {}
        self._convergence_history = []

    def add_node(self, claim_id: str, initial_confidence: float,
                 uncertainty: float = 1.0):
        if not 0.0 <= initial_confidence <= 1.0:
            raise ValueError(f"Confidence must be in [0, 1], got {initial_confidence}")
        self.nodes[claim_id] = ConfidenceNode(
            claim_id=claim_id,
            initial=initial_confidence,
            current=initial_confidence,
            previous=initial_confidence,
            uncertainty=uncertainty
        )
        self.adjacency[claim_id] = []

    def add_edge(self, source: str, target: str, weight: float,
                 edge_type: str = 'supports'):
        self.edges.append(ConfidenceEdge(source, target, weight, edge_type))
        self.adjacency[source].append((target, weight, edge_type))
        # Bidirectional for propagation but with type-specific logic
        reverse_type = self._get_reverse_type(edge_type)
        self.adjacency[target].append((source, weight, reverse_type))

    def _get_reverse_type(self, edge_type: str) -> str:
        if edge_type == 'supports':
            return 'supported_by'
        elif edge_type == 'contradicts':
            return 'contradicted_by'
        return edge_type

    def _propagate_once(self) -> float:
        max_delta = 0.0
        deltas = []

        for node_id, node in self.nodes.items():
            if node.stable:
                continue

            neighbors = self.adjacency[node_id]
            if not neighbors:
                continue

            weighted_sum = 0.0
            total_weight = 0.0
            support_sum = 0.0
            support_weight = 0.0
            contradict_sum = 0.0
            contradict_weight = 0.0

            for neighbor_id, weight, edge_type in neighbors:
                neighbor = self.nodes[neighbor_id]
                influence = neighbor.current

                if edge_type in ('contradicts', 'contradicted_by'):
                    influence = 1.0 - influence
                    weight = abs(weight)
                    contradict_sum += influence * weight
                    contradict_weight += weight
                elif edge_type in ('supports', 'supported_by'):
                    weight = abs(weight)
                    support_sum += influence * weight
                    support_weight += weight
                elif edge_type == 'derives':
                    weight = abs(weight) * 0.8
                    weighted_sum += influence * weight
                    total_weight += weight
                elif edge_type == 'related':
                    weight = abs(weight) * 0.5
                    weighted_sum += influence * weight
                    total_weight += weight

            # Combine support and contradiction
            if support_weight > 0:
                support_conf = support_sum / support_weight
                weighted_sum += support_conf * support_weight
                total_weight += support_weight

            if contradict_weight > 0:
                contradict_conf = contradict_sum / contradict_weight
                # Dampen the contradiction effect
                weighted_sum += contradict_conf * contradict_weight * 0.7
                total_weight += contradict_weight * 0.7

            if total_weight > 0:
                neighbor_influence = weighted_sum / total_weight
                # Damped update
                new_confidence = (node.initial * node.uncertainty +
                                  neighbor_influence * (1 - node.uncertainty))
                new_confidence = self.damping * new_confidence + \
                                 (1 - self.damping) * node.current
                new_confidence = np.clip(new_confidence, 0.0, 1.0)

                delta = abs(new_confidence - node.current)
                max_delta = max(max_delta, delta)
                deltas.append(delta)

                node.previous = node.current
                node.current = new_confidence
                node.iterations += 1

                if delta < self.threshold:
                    node.stable = True

        self._convergence_history.append({
            'max_delta': max_delta,
            'avg_delta': sum(deltas) / len(deltas) if deltas else 0,
            'stable_nodes': sum(1 for n in self.nodes.values() if n.stable)
        })
        return max_delta

    def converge(self) -> Tuple[Dict[str, float], int, bool]:
        """Run propagation until convergence"""
        for nid, n in self.nodes.items():
            if not 0.0 <= n.initial <= 1.0:
                raise ValueError(f"Initial confidence out of bounds: {n.initial}")

        for i in range(self.max_iterations):
            delta = self._propagate_once()
            if delta < self.threshold:
                final = {nid: n.current for nid, n in self.nodes.items()}
                return final, i + 1, True

        logger.warning("Confidence network did not converge")
        final = {nid: n.current for nid, n in self.nodes.items()}
        return final, self.max_iterations, False

    def get_report(self) -> dict:
        converged_final, iterations, stable = self.converge()

        nodes_report = {}
        for nid, n in self.nodes.items():
            nodes_report[nid] = {
                "initial": n.initial,
                "final": converged_final[nid],
                "change": converged_final[nid] - n.initial,
                "stable": n.stable,
                "iterations": n.iterations,
                "uncertainty": n.uncertainty
            }

        return {
            "converged": stable,
            "iterations": iterations,
            "threshold": self.threshold,
            "max_iterations": self.max_iterations,
            "damping": self.damping,
            "nodes": nodes_report,
            "convergence_history": self._convergence_history
        }

    def get_influential_nodes(self, top_n: int = 5) -> List[Tuple[str, float]]:
        """Find nodes with highest degree centrality"""
        degrees = {}
        for nid in self.nodes:
            degrees[nid] = len(self.adjacency[nid])
        return sorted(degrees.items(), key=lambda x: x[1], reverse=True)[:top_n]

    def find_conflicts(self) -> List[Tuple[str, str]]:
        """Find pairs of nodes connected by contradicts edges"""
        conflicts = []
        for edge in self.edges:
            if edge.edge_type == 'contradicts':
                conflicts.append((edge.source, edge.target))
        return conflicts


def demo():
    net = ConfidenceNetwork(threshold=0.001, max_iterations=100, damping=0.3)
    net.add_node("claim_A", 0.7, uncertainty=0.8)
    net.add_node("claim_B", 0.6, uncertainty=0.7)
    net.add_node("claim_C", 0.5, uncertainty=0.9)
    net.add_node("claim_D", 0.3, uncertainty=1.0)

    net.add_edge("claim_A", "claim_B", 0.8, "supports")
    net.add_edge("claim_B", "claim_C", 0.6, "supports")
    net.add_edge("claim_A", "claim_C", 0.3, "related")
    net.add_edge("claim_D", "claim_A", 0.9, "contradicts")

    report = net.get_report()

    print("=== Confidence Network Demo ===")
    print(f"Converged: {report['converged']}")
    print(f"Iterations: {report['iterations']}")
    print(f"\nNode final confidence:")
    for nid, data in report['nodes'].items():
        print(f"  {nid}: {data['initial']:.3f} → {data['final']:.3f} "
              f"(change: {data['change']:+.3f}, stable: {data['stable']})")

    print(f"\nInfluential nodes: {net.get_influential_nodes()}")
    print(f"Conflicts: {net.find_conflicts()}")

if __name__ == '__main__':
    demo()
