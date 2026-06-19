#!/usr/bin/env python3
"""
状态机执行引擎 — 解析依赖图并执行状态流转
"""

import yaml
import json
from pathlib import Path
from typing import Dict, List, Set, Tuple
from collections import deque

class DAGValidator:
    """DAG 验证器"""
    
    @staticmethod
    def validate(nodes: List[dict]) -> Tuple[bool, List[str]]:
        """验证图无环且所有节点可达"""
        errors = []
        
        # 构建邻接表
        adj = {n['id']: set() for n in nodes}
        for n in nodes:
            for dep in n.get('dependencies', []):
                adj[dep].add(n['id'])
        
        # 拓扑排序检测环路
        in_degree = {n['id']: len(n.get('dependencies', [])) for n in nodes}
        queue = deque([nid for nid, d in in_degree.items() if d == 0])
        visited = 0
        topo_order = []
        
        while queue:
            nid = queue.popleft()
            visited += 1
            topo_order.append(nid)
            for neighbor in adj[nid]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)
        
        if visited != len(nodes):
            errors.append("图中存在循环依赖")
        
        # 检查所有节点可达
        all_ids = {n['id'] for n in nodes}
        reachable = set()
        for start in [n['id'] for n in nodes if not n.get('dependencies', [])]:
            # BFS from start
            q = deque([start])
            visited_bfs = {start}
            while q:
                cur = q.popleft()
                for neighbor in adj[cur]:
                    if neighbor not in visited_bfs:
                        visited_bfs.add(neighbor)
                        q.append(neighbor)
            reachable.update(visited_bfs)
        
        unreachable = all_ids - reachable
        if unreachable:
            errors.append(f"不可达节点: {unreachable}")
        
        return len(errors) == 0, errors

class StateMachineEngine:
    """状态机执行引擎"""
    
    def __init__(self, graph_path: str):
        self.graph = self._load_graph(graph_path)
        self.nodes = {n['id']: n for n in self.graph['nodes']}
        self.execution_order = []
        self.current_state = None
        self.outputs = {}
        
    def _load_graph(self, path: str) -> dict:
        with open(path, 'r', encoding='utf-8') as f:
            return yaml.safe_load(f)
    
    def validate(self) -> Tuple[bool, List[str]]:
        return DAGValidator.validate(self.graph['nodes'])
    
    def compute_execution_order(self) -> List[str]:
        """计算拓扑排序的执行顺序"""
        nodes = self.graph['nodes']
        adj = {n['id']: set() for n in nodes}
        for n in nodes:
            for dep in n.get('dependencies', []):
                adj[dep].add(n['id'])
        
        in_degree = {n['id']: len(n.get('dependencies', [])) for n in nodes}
        queue = deque([nid for nid, d in in_degree.items() if d == 0])
        order = []
        
        while queue:
            nid = queue.popleft()
            order.append(nid)
            for neighbor in adj[nid]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)
        
        self.execution_order = order
        return order
    
    def run(self) -> dict:
        """执行完整流水线"""
        valid, errors = self.validate()
        if not valid:
            print("❌ 图验证失败:")
            for e in errors:
                print(f"  - {e}")
            return {"status": "failed", "errors": errors}
        
        order = self.compute_execution_order()
        print(f"✅ 图验证通过，执行顺序: {order}")
        
        results = {}
        for state_id in order:
            node = self.nodes[state_id]
            stage = node['stage']
            
            print(f"\n▶️ 执行状态: {state_id} (stage: {stage})")
            
            # 加载状态定义
            state_def = self._load_state(stage)
            
            # 检查进入条件
            deps = node.get('dependencies', [])
            for dep in deps:
                if dep not in results:
                    print(f"  ⚠️ 依赖 {dep} 尚未完成")
                    return {"status": "failed", "errors": [f"依赖 {dep} 未完成"]}
            
            # 模拟执行（实际执行需要调用角色模板）
            result = {
                "state_id": state_id,
                "stage": stage,
                "completed": True,
                "outputs": state_def.get('activities', []),
                "quality_gates_passed": True
            }
            results[state_id] = result
            self.outputs[state_id] = result
            
            print(f"  ✅ {state_id} 完成")
        
        print(f"\n🎉 流水线执行完成，共 {len(order)} 个状态")
        return {"status": "success", "results": results, "order": order}
    
    def _load_state(self, stage_name: str) -> dict:
        state_path = Path('states') / f'{stage_name}.yaml'
        with open(state_path, 'r', encoding='utf-8') as f:
            return yaml.safe_load(f)

def main():
    import argparse
    parser = argparse.ArgumentParser(description='Epistemic Pipeline 执行引擎')
    parser.add_argument('action', choices=['run', 'validate'], help='操作')
    parser.add_argument('graph', help='依赖图文件路径')
    args = parser.parse_args()
    
    engine = StateMachineEngine(args.graph)
    
    if args.action == 'validate':
        valid, errors = engine.validate()
        print(f"{'✅' if valid else '❌'} 验证结果: {'通过' if valid else '失败'}")
        if errors:
            for e in errors:
                print(f"  - {e}")
    elif args.action == 'run':
        result = engine.run()
        print(f"\n最终状态: {result['status']}")

if __name__ == '__main__':
    main()
