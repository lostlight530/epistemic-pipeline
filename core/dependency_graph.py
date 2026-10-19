#!/usr/bin/env python3
"""Dependency-graph utilities for executable epistemic DAGs.

This module validates structural graph facts only: node identity, dependency
existence, acyclicity and reachability. It does not decide scientific validity
or whether a research transition is substantively justified.
"""

from __future__ import annotations

from collections import defaultdict, deque
from typing import Dict, List, Set, Tuple


class DependencyGraph:
    """Validated DAG helper for ordering, parallel levels and path inspection."""

    def __init__(self, nodes: List[dict]):
        if not isinstance(nodes, list):
            raise TypeError("nodes must be a list")
        self.input_errors: List[str] = []
        self.nodes: Dict[str, dict] = {}
        for index, node in enumerate(nodes):
            if not isinstance(node, dict):
                self.input_errors.append(f"node[{index}] must be a mapping")
                continue
            node_id = node.get("id")
            if not isinstance(node_id, str) or not node_id.strip():
                self.input_errors.append(f"node[{index}] has missing/invalid id")
                continue
            if node_id in self.nodes:
                self.input_errors.append(f"duplicate node id: {node_id}")
                continue
            self.nodes[node_id] = node
        self._build_adjacency()

    def _build_adjacency(self) -> None:
        self.adj: Dict[str, List[str]] = defaultdict(list)
        self.rev_adj: Dict[str, List[str]] = defaultdict(list)
        known = set(self.nodes)
        for node_id, node in self.nodes.items():
            dependencies = node.get("dependencies", []) or []
            if not isinstance(dependencies, list):
                self.input_errors.append(f"dependencies for {node_id} must be a list")
                continue
            seen: Set[str] = set()
            for dependency in dependencies:
                if not isinstance(dependency, str) or not dependency:
                    self.input_errors.append(f"invalid dependency on {node_id}: {dependency!r}")
                    continue
                if dependency in seen:
                    self.input_errors.append(f"duplicate dependency on {node_id}: {dependency}")
                    continue
                seen.add(dependency)
                if dependency not in known:
                    self.input_errors.append(f"missing dependency: {node_id} -> {dependency}")
                    continue
                self.adj[dependency].append(node_id)
                self.rev_adj[node_id].append(dependency)
            self.adj.setdefault(node_id, [])
            self.rev_adj.setdefault(node_id, [])

    def topological_sort(self) -> List[str]:
        """Return one deterministic topological ordering or raise on invalid DAG."""
        if self.input_errors:
            raise ValueError("invalid dependency graph: " + "; ".join(self.input_errors))
        in_degree = {node_id: len(self.rev_adj[node_id]) for node_id in self.nodes}
        queue = deque(sorted(node_id for node_id, degree in in_degree.items() if degree == 0))
        order: List[str] = []
        while queue:
            node_id = queue.popleft()
            order.append(node_id)
            for neighbor in sorted(self.adj[node_id]):
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)
        if len(order) != len(self.nodes):
            raise ValueError("dependency graph contains a cycle")
        return order

    def compute_levels(self) -> Dict[str, int]:
        """Compute longest-root-distance level for each node."""
        levels: Dict[str, int] = {}
        for node_id in self.topological_sort():
            dependencies = self.rev_adj[node_id]
            levels[node_id] = 0 if not dependencies else max(levels[d] for d in dependencies) + 1
        return levels

    def find_parallel_groups(self) -> List[List[str]]:
        """Return deterministic depth groups using one pass over computed levels."""
        levels = self.compute_levels()
        if not levels:
            return []
        buckets: Dict[int, List[str]] = defaultdict(list)
        for node_id, level in levels.items():
            buckets[level].append(node_id)
        return [sorted(buckets[level]) for level in sorted(buckets)]

    def get_critical_path(self) -> List[str]:
        """Return one longest path by node count; ties follow deterministic ordering."""
        order = self.topological_sort()
        if not order:
            return []
        distance = {node_id: 0 for node_id in self.nodes}
        predecessor = {node_id: None for node_id in self.nodes}
        for node_id in order:
            for neighbor in sorted(self.adj[node_id]):
                candidate = distance[node_id] + 1
                if candidate > distance[neighbor]:
                    distance[neighbor] = candidate
                    predecessor[neighbor] = node_id
        end = max(sorted(distance), key=lambda node_id: distance[node_id])
        path: List[str] = []
        current = end
        while current is not None:
            path.append(current)
            current = predecessor[current]
        return list(reversed(path))

    def detect_cycles(self) -> List[List[str]]:
        """Report DFS back-edge cycles without relying on Python recursion depth.

        The explicit frame stack preserves deterministic traversal and active
        path order. It avoids treating a deep *acyclic* execution graph as an
        invalid graph solely because Python's recursion limit was exceeded.
        """
        visited: Set[str] = set()
        active_positions: Dict[str, int] = {}
        cycles: List[List[str]] = []
        seen_signatures: Set[tuple[str, ...]] = set()

        for start in sorted(self.nodes):
            if start in visited:
                continue
            visited.add(start)
            path = [start]
            active_positions[start] = 0
            frames = [(start, iter(sorted(self.adj[start])))]
            while frames:
                current, neighbors = frames[-1]
                try:
                    neighbor = next(neighbors)
                except StopIteration:
                    frames.pop()
                    active_positions.pop(current)
                    path.pop()
                    continue

                if neighbor in active_positions:
                    cycle = path[active_positions[neighbor]:] + [neighbor]
                    signature = tuple(cycle)
                    if signature not in seen_signatures:
                        seen_signatures.add(signature)
                        cycles.append(cycle)
                elif neighbor not in visited:
                    visited.add(neighbor)
                    active_positions[neighbor] = len(path)
                    path.append(neighbor)
                    frames.append((neighbor, iter(sorted(self.adj[neighbor]))))

        return cycles

    def validate(self) -> Tuple[bool, List[str]]:
        """Validate graph identity, dependency existence, cycles and reachability."""
        errors = list(self.input_errors)
        cycles = self.detect_cycles()
        errors.extend("cycle: " + " -> ".join(cycle) for cycle in cycles)
        if not self.nodes:
            errors.append("graph contains no valid nodes")
            return False, errors

        roots = [node_id for node_id in self.nodes if not self.rev_adj[node_id]]
        if not roots:
            errors.append("graph has no root node")
            return False, errors
        reachable: Set[str] = set()
        queue = deque(sorted(roots))
        while queue:
            current = queue.popleft()
            if current in reachable:
                continue
            reachable.add(current)
            queue.extend(sorted(self.adj[current]))
        unreachable = sorted(set(self.nodes) - reachable)
        if unreachable:
            errors.append("unreachable nodes: " + ", ".join(unreachable))
        return not errors, errors


def demo() -> None:
    nodes = [
        {"id": "A", "dependencies": []},
        {"id": "B", "dependencies": ["A"]},
        {"id": "C", "dependencies": ["A"]},
        {"id": "D", "dependencies": ["B", "C"]},
    ]
    graph = DependencyGraph(nodes)
    print("order:", graph.topological_sort())
    print("parallel:", graph.find_parallel_groups())
    print("critical path:", graph.get_critical_path())
    print("valid:", graph.validate())


if __name__ == "__main__":
    demo()
