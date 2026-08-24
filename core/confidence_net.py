#!/usr/bin/env python3
"""Bounded heuristic claim-score propagation network.

The historical ``ConfidenceNetwork`` name is retained for API continuity. The
algorithm is a small weighted iterative heuristic over values in ``[0, 1]``;
it is not Bayesian belief propagation, a posterior-probability calculator, or a
calibration method. Numerical convergence means only that the update rule moved
by less than the configured threshold.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Dict, List, Tuple

EDGE_TYPES = {"supports", "contradicts", "related", "derives"}


@dataclass
class ConfidenceNode:
    claim_id: str
    initial: float
    current: float
    previous: float
    iterations: int = 0
    stable: bool = False


@dataclass
class ConfidenceEdge:
    source: str
    target: str
    weight: float
    edge_type: str


class ConfidenceNetwork:
    """Synchronous bounded score propagation over an undirected influence graph."""

    def __init__(self, threshold: float = 0.01, max_iterations: int = 100):
        if threshold <= 0:
            raise ValueError("threshold must be > 0")
        if max_iterations < 1:
            raise ValueError("max_iterations must be >= 1")
        self.threshold = float(threshold)
        self.max_iterations = int(max_iterations)
        self.last_delta: float = 0.0
        self.nodes: Dict[str, ConfidenceNode] = {}
        self.edges: List[ConfidenceEdge] = []
        self.adjacency: Dict[str, List[Tuple[str, float, str]]] = {}

    def add_node(self, claim_id: str, initial_confidence: float) -> None:
        if not claim_id:
            raise ValueError("claim_id must be non-empty")
        value = float(initial_confidence)
        if not 0.0 <= value <= 1.0:
            raise ValueError(f"score must be within [0, 1], got {initial_confidence}")
        self.nodes[claim_id] = ConfidenceNode(
            claim_id=claim_id,
            initial=value,
            current=value,
            previous=value,
        )
        self.adjacency.setdefault(claim_id, [])

    def add_edge(
        self,
        source: str,
        target: str,
        weight: float,
        edge_type: str = "supports",
    ) -> None:
        if source not in self.nodes or target not in self.nodes:
            raise KeyError("both edge endpoints must already exist")
        if edge_type not in EDGE_TYPES:
            raise ValueError(f"unsupported edge_type: {edge_type}")
        if source == target:
            raise ValueError("self edges are not supported")
        numeric_weight = float(weight)
        self.edges.append(ConfidenceEdge(source, target, numeric_weight, edge_type))
        self.adjacency[source].append((target, numeric_weight, edge_type))
        self.adjacency[target].append((source, numeric_weight, edge_type))

    @staticmethod
    def _effective_influence(value: float, weight: float, edge_type: str) -> Tuple[float, float]:
        magnitude = abs(float(weight))
        if edge_type == "contradicts":
            return 1.0 - value, magnitude
        if edge_type == "derives":
            return value, magnitude * 0.8
        if edge_type == "related":
            return value, magnitude * 0.5
        return value, magnitude

    def _propagate_once(self) -> float:
        """Compute one synchronous update and return the maximum absolute change."""
        previous = {claim_id: node.current for claim_id, node in self.nodes.items()}
        proposed: Dict[str, float] = {}
        max_delta = 0.0

        for claim_id, node in self.nodes.items():
            neighbors = self.adjacency.get(claim_id, [])
            if not neighbors:
                proposed[claim_id] = node.current
                continue
            weighted_sum = 0.0
            total_weight = 0.0
            for neighbor_id, weight, edge_type in neighbors:
                influence, effective_weight = self._effective_influence(
                    previous[neighbor_id], weight, edge_type
                )
                weighted_sum += influence * effective_weight
                total_weight += effective_weight
            if total_weight == 0:
                proposed[claim_id] = node.current
                continue
            next_value = (node.initial + weighted_sum) / (1.0 + total_weight)
            proposed[claim_id] = min(max(float(next_value), 0.0), 1.0)

        for claim_id, next_value in proposed.items():
            node = self.nodes[claim_id]
            delta = abs(next_value - node.current)
            max_delta = max(max_delta, delta)
            node.previous = node.current
            node.current = next_value
            node.iterations += 1
        return max_delta

    def converge(self) -> Tuple[Dict[str, float], int, bool]:
        """Iterate until the update delta is below threshold or the budget ends."""
        for node in self.nodes.values():
            if not 0.0 <= node.initial <= 1.0:
                raise ValueError(f"initial score out of bounds: {node.initial}")
            node.stable = False

        if not self.nodes:
            self.last_delta = 0.0
            return {}, 0, True

        for iteration in range(1, self.max_iterations + 1):
            delta = self._propagate_once()
            self.last_delta = delta
            if delta < self.threshold:
                for node in self.nodes.values():
                    node.stable = True
                return {claim_id: node.current for claim_id, node in self.nodes.items()}, iteration, True

        return (
            {claim_id: node.current for claim_id, node in self.nodes.items()},
            self.max_iterations,
            False,
        )

    def get_report(self) -> dict:
        final, iterations, converged = self.converge()
        return {
            "profile": "epistemic-pipeline/confidence-heuristic@1",
            "semantics": "bounded_weighted_heuristic_not_calibrated_probability",
            "converged": converged,
            "iterations": iterations,
            "threshold": self.threshold,
            "last_delta": self.last_delta,
            "max_iterations": self.max_iterations,
            "nodes": {
                claim_id: {
                    "initial": node.initial,
                    "final": final[claim_id],
                    "change": final[claim_id] - node.initial,
                    "stable": node.stable,
                }
                for claim_id, node in self.nodes.items()
            },
        }


def demo() -> None:
    net = ConfidenceNetwork(threshold=0.01, max_iterations=50)
    net.add_node("claim_A", 0.7)
    net.add_node("claim_B", 0.6)
    net.add_node("claim_C", 0.5)
    net.add_edge("claim_A", "claim_B", 0.8, "supports")
    net.add_edge("claim_B", "claim_C", 0.6, "supports")
    net.add_edge("claim_A", "claim_C", 0.3, "related")
    report = net.get_report()
    print("=== 启发式 score propagation demo ===")
    print("converged:", report["converged"])
    print("iterations:", report["iterations"])
    print("semantics:", report["semantics"])
    for claim_id, data in report["nodes"].items():
        print(f"  {claim_id}: {data['initial']:.3f} -> {data['final']:.3f}")


if __name__ == "__main__":
    demo()
