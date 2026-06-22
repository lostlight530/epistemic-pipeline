#!/usr/bin/env python3
"""epistemic-pipeline 测试套件"""

import sys, os
try:
    import yaml
except ImportError:
    print("⚠️ 需要安装 PyYAML: pip install pyyaml")
    sys.exit(1)
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

def test_manifest_exists():
    assert os.path.exists('MANIFEST.yaml'), "MANIFEST 必须存在"
    print("  [OK] MANIFEST 存在")

def test_states_complete():
    states = ['discover', 'analyze', 'verify', 'synthesize', 'archive']
    for s in states:
        path = f'states/{s}.yaml'
        assert os.path.exists(path), f"state {s} 必须存在"
        with open(path, 'r') as f:
            data = yaml.safe_load(f)
        assert 'id' in data, f"state {s} 必须有 id"
        assert 'activities' in data, f"state {s} 必须有 activities"
    print("  [OK] 所有 5 个状态定义完整")

def test_roles_complete():
    roles = ['explorer', 'analyst', 'verifier', 'synthesizer', 'auditor']
    for r in roles:
        path = f'roles/{r}.md'
        assert os.path.exists(path), f"role {r} 必须存在"
    print("  [OK] 所有 5 个角色模板存在")

def test_graphs_exist():
    graphs = ['linear', 'parallel', 'diamond', 'adaptive']
    for g in graphs:
        path = f'graphs/{g}.yaml'
        assert os.path.exists(path), f"graph {g} 必须存在"
    print("  [OK] 所有 4 个依赖图存在")

def test_validators_exist():
    assert os.path.exists('validators/confidence.schema.yaml'), "confidence schema 必须存在"
    assert os.path.exists('validators/epistemic.rules.yaml'), "epistemic rules 必须存在"
    print("  [OK] 验证器存在")

def test_core_engine():
    from core.engine import StateMachineEngine
    from core.dependency_graph import DependencyGraph
    
    # 测试线性图
    engine = StateMachineEngine('graphs/linear.yaml')
    valid, errors = engine.validate()
    assert valid, f"线性图应验证通过: {errors}"
    
    order = engine.compute_execution_order()
    assert len(order) == 5, "线性图应有 5 个节点"
    assert order[0] == 'discover', "第一个应是 discover"
    assert order[-1] == 'archive', "最后一个应是 archive"
    
    print("  [OK] 引擎核心功能正确")

def test_confidence_net():
    from core.confidence_net import ConfidenceNetwork
    
    net = ConfidenceNetwork(threshold=0.01, max_iterations=50)
    net.add_node("claim_A", 0.7)
    net.add_node("claim_B", 0.6)
    net.add_node("claim_C", 0.5)
    net.add_edge("claim_A", "claim_B", 0.8, "supports")
    net.add_edge("claim_B", "claim_C", 0.6, "supports")
    
    final, iterations, stable = net.converge()
    assert stable, "简单网络应收敛"
    assert iterations <= 50, "应在最大迭代内收敛"
    assert 0 <= final['claim_A'] <= 1, "置信度在 [0,1] 内"
    
    print("  [OK] 置信度传播网络正确")

def test_dependency_graph():
    from core.dependency_graph import DependencyGraph
    
    nodes = [
        {'id': 'A', 'dependencies': []},
        {'id': 'B', 'dependencies': ['A']},
        {'id': 'C', 'dependencies': ['A']},
        {'id': 'D', 'dependencies': ['B', 'C']},
    ]
    
    graph = DependencyGraph(nodes)
    order = graph.topological_sort()
    assert order.index('A') < order.index('B'), "A 在 B 前"
    assert order.index('A') < order.index('C'), "A 在 C 前"
    assert order.index('B') < order.index('D'), "B 在 D 前"
    assert order.index('C') < order.index('D'), "C 在 D 前"
    
    groups = graph.find_parallel_groups()
    assert any('B' in g and 'C' in g for g in groups), "B 和 C 应可并行"
    
    print("  [OK] 依赖图计算正确")

def test_confidence_schema():
    with open('validators/confidence.schema.yaml', 'r') as f:
        schema = yaml.safe_load(f)
    
    assert 'required' in schema
    assert 'nodes' in schema['required']
    assert 'edges' in schema['required']
    assert 'convergence' in schema['required']
    print("  [OK] Confidence Schema 定义正确")

def test_epistemic_rules():
    with open('validators/epistemic.rules.yaml', 'r') as f:
        rules = yaml.safe_load(f)
    
    assert 'rules' in rules
    assert len(rules['rules']) >= 5, "应至少 5 条规则"
    
    severities = [r['severity'] for r in rules['rules']]
    assert 'blocker' in severities, "应有 blocker 级别规则"
    print("  [OK] 认知规则定义正确")

def test_adaptive_graph():
    with open('graphs/adaptive.yaml', 'r') as f:
        graph = yaml.safe_load(f)
    
    assert 'rules' in graph
    assert len(graph['rules']) >= 2, "应至少 2 条自适应规则"
    
    for rule in graph['rules']:
        assert 'condition' in rule
        assert 'graph' in rule
    print("  [OK] 自适应图定义正确")

if __name__ == '__main__':
    tests = [v for k, v in globals().items() if k.startswith('test_')]
    passed = 0
    failed = 0
    for t in tests:
        try:
            t()
            passed += 1
        except Exception as e:
            print(f"  [FAIL] {t.__name__}: {e}")
            failed += 1
    print(f"\n  {passed}/{passed + failed} passed")
    sys.exit(0 if failed == 0 else 1)
