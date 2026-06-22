#!/usr/bin/env python3
"""
状态机执行引擎 — 解析依赖图并执行状态流转
"""

import yaml
import json
import os
import sys
import concurrent.futures
from pathlib import Path
from typing import Dict, List, Set, Tuple
from collections import deque

# 修复模块导入路径
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from core.dependency_graph import DependencyGraph

class StateMachineEngine:
    """状态机执行引擎"""
    
    def __init__(self, graph_path: str):
        self.graph_data = self._load_graph(graph_path)
        self.nodes = {n['id']: n for n in self.graph_data['nodes']}
        self.dep_graph = DependencyGraph(self.graph_data['nodes'])
        self.execution_order = []
        self.current_state = None
        self.outputs = {}
        
    def _load_graph(self, path: str) -> dict:
        with open(path, 'r', encoding='utf-8') as f:
            return yaml.safe_load(f)
    
    def validate(self) -> Tuple[bool, List[str]]:
        return self.dep_graph.validate()
    
    def compute_execution_order(self) -> List[str]:
        """计算拓扑排序的执行顺序"""
        self.execution_order = self.dep_graph.topological_sort()
        return self.execution_order

    def _execute_node(self, state_id: str, results_dict: dict) -> dict:
        """执行单个节点逻辑"""
        node = self.nodes[state_id]
        stage = node['stage']
        
        print(f"\n▶️ 执行状态: {state_id} (stage: {stage})")
        
        # 加载状态定义
        state_def = self._load_state(stage)
        
        # 检查进入条件
        deps = node.get('dependencies', [])
        for dep in deps:
            if dep not in results_dict or results_dict[dep]['status'] != 'success':
                print(f"  ⚠️ 依赖 {dep} 尚未成功完成")
                return {"status": "failed", "errors": [f"依赖 {dep} 未完成"]}

        # 模拟执行（实际执行需要调用角色模板）
        result = {
            "status": "success",
            "state_id": state_id,
            "stage": stage,
            "completed": True,
            "outputs": state_def.get('activities', []),
            "quality_gates_passed": True
        }
        print(f"  ✅ {state_id} 完成")
        return result

    def run(self) -> dict:
        """执行完整流水线"""
        valid, errors = self.validate()
        if not valid:
            print("❌ 图验证失败:")
            for e in errors:
                print(f"  - {e}")
            return {"status": "failed", "errors": errors}
        
        parallel_groups = self.dep_graph.find_parallel_groups()
        print(f"✅ 图验证通过，并行执行组: {parallel_groups}")
        
        results = {}
        total_nodes_executed = 0

        # 按层级并行执行
        for group in parallel_groups:
            if len(group) == 1:
                state_id = group[0]
                result = self._execute_node(state_id, results)
                if result['status'] == 'failed':
                    return {"status": "failed", "errors": result['errors']}
                results[state_id] = result
                self.outputs[state_id] = result
                total_nodes_executed += 1
            else:
                print(f"\n🚀 并行执行组: {group}")
                with concurrent.futures.ThreadPoolExecutor(max_workers=len(group)) as executor:
                    future_to_node = {executor.submit(self._execute_node, state_id, results): state_id for state_id in group}

                    for future in concurrent.futures.as_completed(future_to_node):
                        state_id = future_to_node[future]
                        try:
                            result = future.result()
                            if result['status'] == 'failed':
                                return {"status": "failed", "errors": result['errors']}
                            results[state_id] = result
                            self.outputs[state_id] = result
                            total_nodes_executed += 1
                        except Exception as exc:
                            print(f"  ❌ 节点 {state_id} 产生异常: {exc}")
                            return {"status": "failed", "errors": [str(exc)]}
        
        order = self.compute_execution_order()
        print(f"\n🎉 流水线执行完成，共 {total_nodes_executed} 个状态")
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
