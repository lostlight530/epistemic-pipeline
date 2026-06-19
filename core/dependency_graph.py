#!/usr/bin/env python3
"""
依赖图工具 — DAG 计算、并行分组、执行调度
"""

from typing import List, Dict, Set, Tuple
from collections import deque, defaultdict

class DependencyGraph:
    """依赖图计算引擎"""
    
    def __init__(self, nodes: List[dict]):
        self.nodes = {n['id']: n for n in nodes}
        self._build_adjacency()
    
    def _build_adjacency(self):
        """构建邻接表和反向邻接表"""
        self.adj = defaultdict(list)      # 正向：A -> [B, C]（A 完成后 B,C 可以开始）
        self.rev_adj = defaultdict(list)  # 反向：B -> [A]（B 依赖 A）
        
        for nid, node in self.nodes.items():
            for dep in node.get('dependencies', []):
                self.adj[dep].append(nid)
                self.rev_adj[nid].append(dep)
    
    def topological_sort(self) -> List[str]:
        """拓扑排序，返回执行顺序"""
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
            raise ValueError("图中存在循环依赖")
        
        return order
    
    def compute_levels(self) -> Dict[str, int]:
        """计算每个节点所在的层级（最长路径长度）"""
        levels = {}
        
        for nid in self.topological_sort():
            if not self.rev_adj[nid]:
                levels[nid] = 0
            else:
                levels[nid] = max(levels[dep] for dep in self.rev_adj[nid]) + 1
        
        return levels
    
    def find_parallel_groups(self) -> List[List[str]]:
        """找出可以并行执行的节点组"""
        levels = self.compute_levels()
        max_level = max(levels.values()) if levels else 0
        
        groups = []
        for level in range(max_level + 1):
            group = [nid for nid, lvl in levels.items() if lvl == level]
            if group:
                groups.append(group)
        
        return groups
    
    def get_critical_path(self) -> List[str]:
        """计算关键路径（最长路径）"""
        order = self.topological_sort()
        dist = {nid: 0 for nid in self.nodes}
        predecessor = {nid: None for nid in self.nodes}
        
        for nid in order:
            for neighbor in self.adj[nid]:
                if dist[neighbor] < dist[nid] + 1:
                    dist[neighbor] = dist[nid] + 1
                    predecessor[neighbor] = nid
        
        # 回溯最长路径
        end = max(dist, key=dist.get)
        path = []
        cur = end
        while cur is not None:
            path.append(cur)
            cur = predecessor[cur]
        
        return list(reversed(path))
    
    def detect_cycles(self) -> List[List[str]]:
        """检测所有环路（用于错误报告）"""
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
                    # 发现环路
                    cycle_start = path.index(neighbor)
                    cycle = path[cycle_start:] + [neighbor]
                    cycles.append(cycle)
            
            path.pop()
            rec_stack.remove(nid)
        
        for nid in self.nodes:
            if nid not in visited:
                dfs(nid, [])
        
        return cycles
    
    def validate(self) -> Tuple[bool, List[str]]:
        """验证图是否有效"""
        errors = []
        
        # 检查循环
        cycles = self.detect_cycles()
        if cycles:
            for cycle in cycles:
                errors.append(f"循环依赖: {' -> '.join(cycle)}")
        
        # 检查所有节点可达
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
            errors.append(f"不可达节点: {unreachable}")
        
        return len(errors) == 0, errors

def demo():
    """演示依赖图功能"""
    nodes = [
        {'id': 'A', 'dependencies': []},
        {'id': 'B', 'dependencies': ['A']},
        {'id': 'C', 'dependencies': ['A']},
        {'id': 'D', 'dependencies': ['B', 'C']},
        {'id': 'E', 'dependencies': ['D']},
    ]
    
    graph = DependencyGraph(nodes)
    
    print("=== 依赖图演示 ===")
    print(f"拓扑排序: {graph.topological_sort()}")
    print(f"层级: {graph.compute_levels()}")
    print(f"并行组: {graph.find_parallel_groups()}")
    print(f"关键路径: {graph.get_critical_path()}")
    
    valid, errors = graph.validate()
    print(f"验证: {'通过' if valid else '失败'}")
    if errors:
        for e in errors:
            print(f"  - {e}")

if __name__ == '__main__':
    demo()
