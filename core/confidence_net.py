#!/usr/bin/env python3
"""
置信度传播网络 — 在知识主张间传播和收敛置信度
基于信念传播（Belief Propagation）简化版
"""

import numpy as np
from typing import Dict, List, Tuple
from dataclasses import dataclass

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
    edge_type: str  # supports, contradicts, related, derives

class ConfidenceNetwork:
    """置信度传播网络"""
    
    def __init__(self, threshold: float = 0.01, max_iterations: int = 100):
        self.threshold = threshold
        self.max_iterations = max_iterations
        self.nodes: Dict[str, ConfidenceNode] = {}
        self.edges: List[ConfidenceEdge] = []
        self.adjacency: Dict[str, List[Tuple[str, float, str]]] = {}
        
    def add_node(self, claim_id: str, initial_confidence: float):
        self.nodes[claim_id] = ConfidenceNode(
            claim_id=claim_id,
            initial=initial_confidence,
            current=initial_confidence,
            previous=initial_confidence
        )
        self.adjacency[claim_id] = []
    
    def add_edge(self, source: str, target: str, weight: float, edge_type: str = 'supports'):
        self.edges.append(ConfidenceEdge(source, target, weight, edge_type))
        self.adjacency[source].append((target, weight, edge_type))
        self.adjacency[target].append((source, weight, edge_type))  # 无向图用于传播
    
    def _propagate_once(self) -> float:
        """执行一次传播迭代，返回最大变化"""
        max_delta = 0.0
        
        for node_id, node in self.nodes.items():
            if node.stable:
                continue
                
            # 收集邻居影响
            neighbors = self.adjacency[node_id]
            if not neighbors:
                continue
            
            # 计算加权平均影响
            weighted_sum = 0.0
            total_weight = 0.0
            
            for neighbor_id, weight, edge_type in neighbors:
                neighbor = self.nodes[neighbor_id]
                influence = neighbor.current
                
                # 根据关系类型调整影响方向
                if edge_type == 'contradicts':
                    influence = 1.0 - influence  # 反对关系降低置信度
                    weight = abs(weight)
                elif edge_type == 'supports':
                    weight = abs(weight)
                elif edge_type == 'derives':
                    weight = abs(weight) * 0.8  # 推导关系影响稍弱
                elif edge_type == 'related':
                    weight = abs(weight) * 0.5  # 相关关系影响最弱
                
                weighted_sum += influence * weight
                total_weight += weight
            
            if total_weight > 0:
                new_confidence = (node.initial + weighted_sum) / (1 + total_weight)
                new_confidence = np.clip(new_confidence, 0.0, 1.0)
                
                delta = abs(new_confidence - node.current)
                max_delta = max(max_delta, delta)
                
                node.previous = node.current
                node.current = new_confidence
                node.iterations += 1
                
                if delta < self.threshold:
                    node.stable = True
        
        return max_delta
    
    def converge(self) -> Tuple[Dict[str, float], int, bool]:
        """运行传播直到收敛，返回 (最终置信度, 迭代次数, 是否收敛)"""
        for i in range(self.max_iterations):
            delta = self._propagate_once()
            
            if delta < self.threshold:
                final = {nid: n.current for nid, n in self.nodes.items()}
                return final, i + 1, True
        
        # 未收敛
        final = {nid: n.current for nid, n in self.nodes.items()}
        return final, self.max_iterations, False
    
    def get_report(self) -> dict:
        """生成传播报告"""
        converged_final, iterations, stable = self.converge()
        
        return {
            "converged": stable,
            "iterations": iterations,
            "threshold": self.threshold,
            "max_iterations": self.max_iterations,
            "nodes": {
                nid: {
                    "initial": n.initial,
                    "final": converged_final[nid],
                    "change": converged_final[nid] - n.initial,
                    "stable": n.stable
                }
                for nid, n in self.nodes.items()
            }
        }

def demo():
    """演示置信度传播"""
    net = ConfidenceNetwork(threshold=0.01, max_iterations=50)
    
    # 添加节点
    net.add_node("claim_A", 0.7)   # 初始置信度 70%
    net.add_node("claim_B", 0.6)   # 初始置信度 60%
    net.add_node("claim_C", 0.5)   # 初始置信度 50%
    
    # 添加边：A 支持 B（强），B 支持 C（中等），A 与 C 相关（弱）
    net.add_edge("claim_A", "claim_B", 0.8, "supports")
    net.add_edge("claim_B", "claim_C", 0.6, "supports")
    net.add_edge("claim_A", "claim_C", 0.3, "related")
    
    report = net.get_report()
    
    print("=== 置信度传播演示 ===")
    print(f"收敛: {'是' if report['converged'] else '否'}")
    print(f"迭代次数: {report['iterations']}")
    print(f"\n节点最终置信度:")
    for nid, data in report['nodes'].items():
        print(f"  {nid}: {data['initial']:.3f} → {data['final']:.3f} (变化: {data['change']:+.3f})")

if __name__ == '__main__':
    demo()
