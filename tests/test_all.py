#!/usr/bin/env python3
"""epistemic-pipeline 测试套件"""

import sys, os
try:
    import yaml
except ImportError:
    print("⚠️ 需要安装 PyYAML: pip install pyyaml")
    sys.exit(1)
try:
    import numpy
except ImportError:
    print("⚠️ 需要安装 NumPy: pip install numpy")
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


def test_engine_rejects_cyclic_graph():
    from core.dependency_graph import DependencyGraph
    nodes = [
        {'id': 'A', 'dependencies': ['C']},
        {'id': 'B', 'dependencies': ['A']},
        {'id': 'C', 'dependencies': ['B']}
    ]
    graph = DependencyGraph(nodes)
    valid, errors = graph.validate()
    assert not valid, "循环图验证应失败"
    assert any("循环依赖" in e for e in errors), "应报告循环依赖错误"
    print("  [OK] 成功检测到并拒绝了循环图")

def test_engine_rejects_unreachable_node():
    from core.dependency_graph import DependencyGraph
    nodes = [
        {'id': 'A', 'dependencies': []},
        {'id': 'B', 'dependencies': ['A']},
        {'id': 'C', 'dependencies': ['B']},
        {'id': 'D', 'dependencies': ['E']}, # E is unreachable from any source
        {'id': 'E', 'dependencies': ['D']}  # E and D form an unreachable cycle
    ]
    graph = DependencyGraph(nodes)
    valid, errors = graph.validate()
    assert not valid, "包含不可达节点的图验证应失败"
    assert any("不可达节点" in e for e in errors), "应报告不可达节点错误"
    print("  [OK] 成功检测到并拒绝了不可达节点")

def test_gatekeeper_missing_input():
    from core.gatekeeper import Gatekeeper
    gk = Gatekeeper()
    state_def = {
        'id': 'discover_1',
        'quality_gates': [{'id': 'coverage', 'rule': '来源数 >= 1'}]
    }
    outputs = {} # intentionally missing inputs
    passed, errors = gk.check_quality_gates(state_def, outputs)
    assert not passed, "缺少输入的 gate 验证应失败"
    assert "MISSING_GATE_INPUT" in errors, "应包含 MISSING_GATE_INPUT 错误"
    print("  [OK] Gatekeeper 正确处理了丢失的输入 (MISSING_GATE_INPUT)")

def test_confidence_bounds_enforced():
    from core.confidence_net import ConfidenceNetwork
    net = ConfidenceNetwork()
    try:
        net.add_node("claim_out", 1.5)
        assert False, "应该拒绝越界的置信度"
    except ValueError:
        pass
    print("  [OK] 成功拦截越界的置信度值")

def test_confidence_not_converged():
    from core.confidence_net import ConfidenceNetwork
    net = ConfidenceNetwork(threshold=0.0001, max_iterations=2)
    net.add_node("claim_A", 0.5)
    net.add_node("claim_B", 0.6)
    # create oscillation or slow convergence
    net.add_edge("claim_A", "claim_B", 1.0, "contradicts")
    net.add_edge("claim_B", "claim_A", 1.0, "contradicts")

    final, iterations, stable = net.converge()
    assert not stable, "短迭代和高振荡情况下不应收敛"
    print("  [OK] 正确检测到 CONFIDENCE_NOT_CONVERGED 状态")

def test_engine_full_run_mock():
    from core.engine import StateMachineEngine
    engine = StateMachineEngine('graphs/linear.yaml')
    result = engine.run()
    assert result['status'] == 'success', f"线性图应端到端执行成功: {result.get('errors')}"
    assert len(result['results']) == 5, "应执行全部 5 个节点"
    for nid, res in result['results'].items():
        assert res['quality_gates_passed'], f"节点 {nid} 应通过质量门"
        assert isinstance(res['outputs'], dict), f"节点 {nid} 应产出结构化输出"
    print("  [OK] 引擎端到端执行成功（mock 模式 + 质量门拦截）")

def test_engine_parallel_run_mock():
    from core.engine import StateMachineEngine
    engine = StateMachineEngine('graphs/parallel.yaml')
    result = engine.run()
    assert result['status'] == 'success', f"并行图应端到端执行成功: {result.get('errors')}"
    assert len(result['results']) == 7, "并行图应执行全部 7 个节点"
    print("  [OK] 并行 DAG 端到端执行成功")

def test_engine_gatekeeper_blocks_bad_output():
    from core.engine import StateMachineEngine

    class EmptyHarness:
        """模拟返回空输出的 Harness，应被质量门拦截"""
        def execute(self, state_id, role_bindings, inputs, mock=True):
            return {}

    engine = StateMachineEngine('graphs/linear.yaml', harness=EmptyHarness())
    result = engine.run()
    assert result['status'] == 'failed', "空输出应被 Gatekeeper 拦截导致流水线失败"
    assert any('MISSING_GATE_INPUT' in e for e in result['errors']), "应包含 MISSING_GATE_INPUT"
    print("  [OK] 引擎通过 Gatekeeper 拦截了不合规输出")

def test_engine_confidence_network_wired():
    from core.engine import StateMachineEngine
    engine = StateMachineEngine('graphs/linear.yaml')
    result = engine.run()
    assert result['status'] == 'success', f"流水线应执行成功: {result.get('errors')}"
    syn_outputs = result['results']['synthesize']['outputs']
    cn = syn_outputs.get('confidence_network')
    assert cn is not None, "synthesize 应产出置信度网络报告"
    assert cn['converged'], "置信度网络应收敛"
    assert 'c1' in cn['final'], "传播结果应包含上游主张 c1"
    assert all(0.0 <= v <= 1.0 for v in cn['final'].values()), "最终置信度应在 [0,1] 内"
    assert syn_outputs['delta'] < 0.01, "收敛后 delta 应小于阈值 0.01"
    print("  [OK] 置信度网络已接入主引擎并在 synthesize 阶段收敛")

def test_engine_mock_disabled_raises():
    """mock_llm=False 时引擎必须如实抛出 NotImplementedError，不得伪造 LLM 能力"""
    from core.engine import StateMachineEngine
    engine = StateMachineEngine('graphs/linear.yaml', mock_llm=False)
    try:
        engine.run()
        assert False, "mock 关闭且未接入真实 LLM 时应抛出 NotImplementedError"
    except NotImplementedError:
        pass
    print("  [OK] mock 关闭时引擎如实抛出 NotImplementedError（无伪造 LLM 能力）")

def test_engine_adaptive_graph_fails_clearly():
    """adaptive 为实验性拓扑（无 nodes），引擎应给出明确错误而非栈追踪"""
    from core.engine import StateMachineEngine
    try:
        StateMachineEngine('graphs/adaptive.yaml')
        assert False, "无 nodes 的图应被拒绝"
    except ValueError as e:
        assert 'nodes' in str(e), "错误信息应指明缺少 nodes 定义"
    print("  [OK] 实验性 adaptive 图被明确拒绝（fail-closed，无 KeyError 泄漏）")

def test_engine_confidence_not_converged_fails_gate():
    """置信度网络不收敛时，synthesize 的 confidence_converged 质量门按设计失败"""
    import core.engine as engine_mod
    from core.confidence_net import ConfidenceNetwork

    class NonConvergingNetwork(ConfidenceNetwork):
        """强制不收敛的网络桩：末次 delta 远高于阈值"""
        def converge(self):
            self.last_delta = 0.5
            return {nid: n.current for nid, n in self.nodes.items()}, self.max_iterations, False

    original = engine_mod.ConfidenceNetwork
    engine_mod.ConfidenceNetwork = NonConvergingNetwork
    try:
        engine = engine_mod.StateMachineEngine('graphs/linear.yaml')
        result = engine.run()
    finally:
        engine_mod.ConfidenceNetwork = original

    assert result['status'] == 'failed', "置信度不收敛应导致流水线失败"
    assert any('confidence_converged' in e for e in result['errors']), \
        "失败原因应来自 confidence_converged 质量门"
    print("  [OK] 置信度不收敛时 synthesize 质量门按设计拦截流水线")

def test_engine_gatekeeper_disabled_empty_network():
    """use_gatekeeper=False 且上游无主张时，synthesize 走空网络路径 (delta=0.0)"""
    from core.engine import StateMachineEngine

    class MinimalHarness:
        """返回空输出的 Harness（仅在质量门关闭时可通行）"""
        def execute(self, state_id, role_bindings, inputs, mock=True):
            return {}

    engine = StateMachineEngine('graphs/linear.yaml', use_gatekeeper=False,
                                harness=MinimalHarness())
    result = engine.run()
    assert result['status'] == 'success', f"质量门关闭时空输出流水线应成功: {result.get('errors')}"
    syn = result['results']['synthesize']['outputs']
    assert syn['confidence_network']['converged'] is True, "空网络应视为已收敛"
    assert syn['delta'] == 0.0, "空网络 delta 应为 0.0"
    assert result['results']['synthesize']['quality_gates_passed'] is False, \
        "use_gatekeeper=False 时质量门标记应为 False"
    print("  [OK] 质量门可关闭，空置信度网络按设计收敛于 delta=0.0")

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
