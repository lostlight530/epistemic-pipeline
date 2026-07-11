#!/usr/bin/env python3
"""
依赖图工具 — DAG 计算、并行分组、执行调度
Enhanced: Resource-constrained scheduling, ancestor/descendant queries, caching
"""

from typing import List, Dict, Set, Tuple, Optional
from collections import deque, defaultdict


class DependencyGraph:
    """Enhanced dependency graph engine with resource scheduling"""

    def __init__(self, nodes: List[dict]):
        self.nodes = {n['id']: n for n in nodes}
        self._build_adjacency()
        self._cache = {}

    def _build_adjacency(self):
        self.adj = defaultdict(list)
        self.rev_adj = defaultdict(list)

        for nid, node in self.nodes.items():
            for dep in node.get('dependencies', []):
                self.adj[dep].append(nid)
                self.rev_adj[nid].append(dep)

    def topological_sort(self) -> List[str]:
        in_degree = {nid: len(self.rev_adj[nid]) for nid in self.nodes}
        queue = deque([nid for nid, d in in_degree.items() if d == 0])
        order = []

        while queue:
            nid = queue.popleft()
            order.append(nid)
            for neighbor in self.adj[nid]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)

        if len(order) != len(self.nodes):
            raise ValueError("Cycle detected in graph")
        return order

    def compute_levels(self) -> Dict[str, int]:
        levels = {}
        for nid in self.topological_sort():
            if not self.rev_adj[nid]:
                levels[nid] = 0
            else:
                levels[nid] = max(levels[dep] for dep in self.rev_adj[nid]) + 1
        return levels

    def find_parallel_groups(self) -> List[List[str]]:
        levels = self.compute_levels()
        if not levels:
            return []
        max_level = max(levels.values())
        return [
            [nid for nid, lvl in levels.items() if lvl == level]
            for level in range(max_level + 1)
            if [nid for nid, lvl in levels.items() if lvl == level]
        ]

    def get_critical_path(self) -> List[str]:
        order = self.topological_sort()
        dist = {nid: 0 for nid in self.nodes}
        predecessor = {nid: None for nid in self.nodes}

        for nid in order:
            for neighbor in self.adj[nid]:
                if dist[neighbor] < dist[nid] + 1:
                    dist[neighbor] = dist[nid] + 1
                    predecessor[neighbor] = nid

        end = max(dist, key=dist.get)
        path = []
        cur = end
        while cur is not None:
            path.append(cur)
            cur = predecessor[cur]
        return list(reversed(path))

    def get_ancestors(self, node_id: str) -> Set[str]:
        """Get all ancestors of a node"""
        ancestors = set()
        queue = deque([node_id])
        visited = {node_id}
        while queue:
            cur = queue.popleft()
            for dep in self.rev_adj[cur]:
                if dep not in visited:
                    visited.add(dep)
                    ancestors.add(dep)
                    queue.append(dep)
        return ancestors

    def get_descendants(self, node_id: str) -> Set[str]:
        """Get all descendants of a node"""
        descendants = set()
        queue = deque([node_id])
        visited = {node_id}
        while queue:
            cur = queue.popleft()
            for neighbor in self.adj[cur]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    descendants.add(neighbor)
                    queue.append(neighbor)
        return descendants

    def find_independent_sets(self) -> List[Set[str]]:
        """Find maximal independent sets (nodes with no dependencies between them)"""
        levels = self.compute_levels()
        groups = self.find_parallel_groups()
        return [set(g) for g in groups]

    def schedule_with_resources(self, max_workers: int = 4) -> List[List[str]]:
        """Resource-constrained scheduling"""
        order = self.topological_sort()
        in_degree = {nid: len(self.rev_adj[nid]) for nid in self.nodes}
        ready = [nid for nid in order if in_degree[nid] == 0]
        schedule = []
        completed = set()

        while ready:
            batch = ready[:max_workers]
            schedule.append(batch)
            completed.update(batch)
            ready = ready[max_workers:]

            for nid in batch:
                for neighbor in self.adj[nid]:
                    in_degree[neighbor] -= 1
                    if in_degree[neighbor] == 0 and neighbor not in completed:
                        ready.append(neighbor)

        return schedule

    def detect_cycles(self) -> List[List[str]]:
        visited = set()
        rec_stack = set()
        cycles = []

        def dfs(nid, path):
            visited.add(nid)
            rec_stack.add(nid)
            path.append(nid)
            for neighbor in self.adj[nid]:
                if neighbor not in visited:
                    dfs(neighbor, path)
                elif neighbor in rec_stack:
                    cycle_start = path.index(neighbor)
                    cycles.append(path[cycle_start:] + [neighbor])
            path.pop()
            rec_stack.remove(nid)

        for nid in self.nodes:
            if nid not in visited:
                dfs(nid, [])
        return cycles

    def validate(self) -> Tuple[bool, List[str]]:
        errors = []
        cycles = self.detect_cycles()
        if cycles:
            for cycle in cycles:
                errors.append(f"Cycle: {' -> '.join(cycle)}")

        all_ids = set(self.nodes.keys())
        reachable = set()
        for start in [nid for nid in self.nodes if not self.rev_adj[nid]]:
            q = deque([start])
            visited = {start}
            while q:
                cur = q.popleft()
                for neighbor in self.adj[cur]:
                    if neighbor not in visited:
                        visited.add(neighbor)
                        q.append(neighbor)
            reachable.update(visited)

        unreachable = all_ids - reachable
        if unreachable:
            errors.append(f"Unreachable: {unreachable}")

        return len(errors) == 0, errors


def demo():
    nodes = [
        {'id': 'A', 'dependencies': []},
        {'id': 'B', 'dependencies': ['A']},
        {'id': 'C', 'dependencies': ['A']},
        {'id': 'D', 'dependencies': ['B', 'C']},
        {'id': 'E', 'dependencies': ['D']},
    ]

    graph = DependencyGraph(nodes)
    print("=== Dependency Graph Demo ===")
    print(f"Topological: {graph.topological_sort()}")
    print(f"Levels: {graph.compute_levels()}")
    print(f"Parallel: {graph.find_parallel_groups()}")
    print(f"Critical: {graph.get_critical_path()}")
    print(f"Ancestors of D: {graph.get_ancestors('D')}")
    print(f"Resource schedule (2 workers): {graph.schedule_with_resources(2)}")
    valid, errors = graph.validate()
    print(f"Valid: {valid}")

if __name__ == '__main__':
    demo()
