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


# ----------------------------------------------------------------------
# Round 3 — 前沿校准：RunTracer / Provider 协议 / 弹性执行 / 检查点 / 校准钩子
# ----------------------------------------------------------------------

def _tmp_dir():
    import tempfile
    return tempfile.mkdtemp(prefix='ep_test_')


def test_run_tracer_otel_fields_and_hash_chain():
    """RunTracer 写入 OTel GenAI 命名字段，哈希链可校验且防篡改"""
    import json
    from core.run_tracer import RunTracer

    tmp = _tmp_dir()
    tracer = RunTracer('run_test_1', output_dir=tmp)
    tracer.start_node('discover', 'discover')
    tracer.end_node('discover', 'discover', 'success')
    tracer.start_node('analyze', 'analyze')
    tracer.end_node('analyze', 'analyze', 'failed', error_type='QualityGateError')

    path = os.path.join(tmp, 'run_test_1.jsonl')
    with open(path, 'r', encoding='utf-8') as f:
        records = [json.loads(l) for l in f if l.strip()]
    assert len(records) == 4, "两个节点应产生 start/end 共 4 条记录"
    for r in records:
        assert r['gen_ai.operation.name'] == 'invoke_agent', "应对齐 OTel GenAI 操作命名"
        assert r['gen_ai.conversation.id'] == 'run_test_1', "应以 run_id 关联同次运行"
        assert 'prev_hash' in r and 'hash' in r, "每条记录应携带哈希链指针"
    end_records = [r for r in records if r['event'] == 'end']
    assert all(r['duration_ms'] is not None for r in end_records), "end 事件应含耗时"
    failed = [r for r in end_records if r['status'] == 'failed'][0]
    assert failed['error.type'] == 'QualityGateError', "失败事件应记录 error.type"
    assert RunTracer.verify_chain(path), "原始轨迹哈希链应校验通过"

    # 篡改任一字段必须断链
    tampered = records.copy()
    tampered[1] = dict(tampered[1]); tampered[1]['status'] = 'failed'
    tampered_path = os.path.join(tmp, 'tampered.jsonl')
    with open(tampered_path, 'w', encoding='utf-8') as f:
        for r in tampered:
            f.write(json.dumps(r, ensure_ascii=False) + '\n')
    assert not RunTracer.verify_chain(tampered_path), "篡改后的轨迹应校验失败"
    print("  [OK] RunTracer 输出 OTel GenAI 命名轨迹且哈希链防篡改")


def test_engine_run_produces_trace():
    """引擎执行应产出与 run_id 关联的完整轨迹文件"""
    from core.engine import StateMachineEngine
    from core.run_tracer import RunTracer

    tmp = _tmp_dir()
    engine = StateMachineEngine('graphs/linear.yaml', trace_dir=tmp,
                                checkpoint_dir=None)
    result = engine.run()
    assert result['status'] == 'success', f"流水线应成功: {result.get('errors')}"
    run_id = result['run_id']
    trace_path = os.path.join(tmp, f'{run_id}.jsonl')
    assert os.path.exists(trace_path), "应生成 traces/<run_id>.jsonl"
    assert RunTracer.verify_chain(trace_path), "引擎轨迹哈希链应完整"
    with open(trace_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    assert len(lines) == 10, "5 个节点应产生 10 条 start/end 记录"
    print("  [OK] 引擎执行产出 run_id 关联的完整防篡改轨迹")


def test_mock_provider_contract():
    """MockProvider 契约测试：各阶段输出满足 STAGE_CONTRACTS 声明的键，且可 JSON 序列化。
    未来真实 provider 接入时复用同一契约断言。"""
    import json
    from core.llm_harness import LLMHarness, MockProvider

    harness = LLMHarness()
    provider = MockProvider()
    for stage, required_keys in MockProvider.STAGE_CONTRACTS.items():
        prompts = harness.build_prompt(f'{stage}_x', {'primary': stage}, {})
        out = provider.complete(prompts['system'], prompts['user'])
        assert isinstance(out, dict), f"{stage} 输出应为 dict"
        for key in required_keys:
            assert key in out, f"{stage} 输出缺少契约键 {key}"
        json.dumps(out)  # 必须可 JSON 序列化（检查点/轨迹依赖此性质）
    print("  [OK] MockProvider 满足全部 5 阶段输出契约（可序列化）")


def test_provider_dependency_injection():
    """注入自定义 provider 时，harness 应路由到 provider.complete 而非内置 mock"""
    from core.llm_harness import LLMHarness, LLMProvider

    calls = []

    class SpyProvider(LLMProvider):
        def complete(self, system, user, schema=None):
            calls.append({'system': system, 'user': user, 'schema': schema})
            return {"sources_index": [{"id": "s1"}], "raw_extractions": [
                {"source_id": "s1", "metadata": {}}], "annotated_corpus": []}

    harness = LLMHarness(provider=SpyProvider())
    out = harness.execute('discover_1', {'primary': 'explorer'}, {}, mock=False)
    assert len(calls) == 1, "provider.complete 应被调用恰好一次"
    assert 'Current State: discover_1' in calls[0]['user'], "应传递组装的 user prompt"
    assert 'sources_index' in out, "应返回 provider 的结构化输出"
    print("  [OK] LLMProvider 依赖注入路由正确（协议抽象生效）")


def test_retry_transient_recovers():
    """transient 错误（ConnectionError）应按指数退避重试并最终恢复"""
    from core.engine import StateMachineEngine
    from core.llm_harness import LLMHarness, MockProvider

    discover_calls = {'n': 0}

    class FlakyProvider(MockProvider):
        def complete(self, system, user, schema=None):
            if 'Current State: discover' in user:
                discover_calls['n'] += 1
                if discover_calls['n'] == 1:
                    raise ConnectionError("mock 瞬时连接故障")
            return super().complete(system, user, schema)

    engine = StateMachineEngine('graphs/linear.yaml', trace_dir=None,
                                checkpoint_dir=None,
                                harness=LLMHarness(provider=FlakyProvider()))
    # 给 discover 节点注入重试策略
    engine.nodes['discover']['retry'] = {'max_attempts': 3, 'base_delay': 0.01, 'factor': 2.0}
    result = engine.run()
    assert result['status'] == 'success', f"transient 故障重试后应成功: {result.get('errors')}"
    assert discover_calls['n'] == 2, \
        f"discover 应在第 2 次尝试恢复，实际尝试 {discover_calls['n']} 次"
    print("  [OK] transient 错误经指数退避重试后恢复")


def test_retry_permanent_not_retried():
    """permanent 错误（NotImplementedError）必须 fail-fast，不得重试"""
    from core.engine import StateMachineEngine
    from core.llm_harness import LLMHarness, LLMProvider

    attempts = {'n': 0}

    class BrokenProvider(LLMProvider):
        def complete(self, system, user, schema=None):
            attempts['n'] += 1
            raise NotImplementedError("真实通道未接入")

    engine = StateMachineEngine('graphs/linear.yaml', trace_dir=None,
                                checkpoint_dir=None,
                                harness=LLMHarness(provider=BrokenProvider()))
    engine.nodes['discover']['retry'] = {'max_attempts': 5, 'base_delay': 0.01}
    try:
        engine.run()
        assert False, "permanent 错误应直接抛出"
    except NotImplementedError:
        pass
    assert attempts['n'] == 1, f"permanent 错误不应重试，实际尝试 {attempts['n']} 次"
    print("  [OK] permanent 错误 fail-fast 不重试（错误分类生效）")


def test_node_timeout():
    """timeout_seconds 触发 NodeTimeoutError（transient），重试耗尽后节点失败"""
    import time
    from core.engine import StateMachineEngine
    from core.llm_harness import LLMHarness, LLMProvider
    from core.resilience import NodeTimeoutError

    class SlowProvider(LLMProvider):
        def complete(self, system, user, schema=None):
            time.sleep(1.0)
            return {}

    engine = StateMachineEngine('graphs/linear.yaml', trace_dir=None,
                                checkpoint_dir=None,
                                harness=LLMHarness(provider=SlowProvider()))
    engine.nodes['discover']['timeout_seconds'] = 0.1
    engine.nodes['discover']['retry'] = {'max_attempts': 2, 'base_delay': 0.01}
    start = time.monotonic()
    try:
        engine.run()
        assert False, "超时节点应抛出 NodeTimeoutError"
    except NodeTimeoutError:
        pass
    elapsed = time.monotonic() - start
    assert elapsed < 1.0, f"超时应快速失败而非等待 provider 完成，实际 {elapsed:.2f}s"
    print("  [OK] 每节点超时按 timeout_seconds 限时并快速失败")


def test_parallel_failure_keeps_sibling_results():
    """并行组中任一节点失败时，兄弟节点的已完成结果必须保留在失败负载中"""
    from core.engine import StateMachineEngine
    from core.llm_harness import MockProvider

    class PartialHarness:
        """analyze_group_2 返回空输出（被质量门拦截），其余节点走正常 mock"""
        def __init__(self):
            self.mock = MockProvider()
        def execute(self, state_id, role_bindings, inputs, mock=True):
            if state_id == 'analyze_group_2':
                return {}
            prompts = self._prompts(state_id)
            return self.mock.complete(*prompts)
        def _prompts(self, state_id):
            return ("sys", f"Current State: {state_id}\n")

    engine = StateMachineEngine('graphs/parallel.yaml', trace_dir=None,
                                checkpoint_dir=None,
                                harness=PartialHarness())
    result = engine.run()
    assert result['status'] == 'failed', "组内失败应使流水线失败"
    kept = result.get('results', {})
    assert kept.get('analyze_group_1', {}).get('status') == 'success', \
        "兄弟节点 analyze_group_1 的结果必须保留"
    assert kept.get('analyze_group_3', {}).get('status') == 'success', \
        "兄弟节点 analyze_group_3 的结果必须保留"
    assert kept.get('analyze_group_2', {}).get('status') == 'failed', \
        "失败节点本身也应记录在结果中"
    print("  [OK] 并行组失败不再丢弃兄弟节点结果（as_completed 修复）")


def test_checkpoint_resume():
    """失败后断点续跑：已成功节点不重跑，仅重跑失败及下游节点"""
    from core.engine import StateMachineEngine
    from core.llm_harness import MockProvider

    tmp = _tmp_dir()
    executed = []

    class FailAtVerifyHarness:
        """fail_verify=True 时 verify 返回空输出，被质量门拦截（结果级失败）"""
        def __init__(self, fail_verify):
            self.fail_verify = fail_verify
            self.mock = MockProvider()
        def execute(self, state_id, role_bindings, inputs, mock=True):
            executed.append(state_id)
            if self.fail_verify and state_id == 'verify':
                return {}
            return self.mock.complete("sys", f"Current State: {state_id}\n")

    # 第一次运行：verify 失败
    engine1 = StateMachineEngine('graphs/linear.yaml', trace_dir=None,
                                 checkpoint_dir=tmp,
                                 harness=FailAtVerifyHarness(fail_verify=True))
    result1 = engine1.run()
    assert result1['status'] == 'failed', "首次运行应在 verify 失败"
    run_id = result1['run_id']
    first_round = list(executed)
    assert 'archive' not in first_round, "失败下游不应执行"

    # 断点续跑：修复后仅重跑 verify 及下游
    executed.clear()
    engine2 = StateMachineEngine('graphs/linear.yaml', trace_dir=None,
                                 checkpoint_dir=tmp,
                                 harness=FailAtVerifyHarness(fail_verify=False))
    result2 = engine2.run(resume_from=run_id)
    assert result2['status'] == 'success', f"续跑应成功: {result2.get('errors')}"
    assert result2['run_id'] == run_id, "续跑应复用同一 run_id"
    assert 'discover' not in executed and 'analyze' not in executed, \
        "已成功节点不得重跑"
    assert executed == ['verify', 'synthesize', 'archive'], \
        f"应仅重跑失败及下游节点，实际: {executed}"
    print("  [OK] 检查点断点续跑：复用成功节点，仅重跑失败及下游")


def test_checkpoint_resume_rejects_mismatched_graph():
    """跨图续跑必须 fail-closed 拒绝"""
    from core.engine import StateMachineEngine

    tmp = _tmp_dir()
    engine1 = StateMachineEngine('graphs/linear.yaml', trace_dir=None, checkpoint_dir=tmp)
    result1 = engine1.run()
    engine2 = StateMachineEngine('graphs/parallel.yaml', trace_dir=None, checkpoint_dir=tmp)
    try:
        engine2.run(resume_from=result1['run_id'])
        assert False, "图标识不匹配应拒绝续跑"
    except ValueError as e:
        assert '不匹配' in str(e)
    print("  [OK] 跨图续跑被 fail-closed 拒绝")


def test_temperature_scaling_calibration():
    """temperature scaling：T=1 恒等，T>1 向 0.5 收缩，T<1 锐化，全程保 [0,1] 边界"""
    from core.calibration import temperature_scale, calibrate_confidence_map

    assert abs(temperature_scale(0.8, 1.0) - 0.8) < 1e-6, "T=1 应近似恒等"
    assert abs(temperature_scale(0.5, 2.0) - 0.5) < 1e-9, "0.5 是不动点"
    assert temperature_scale(0.8, 2.0) < 0.8, "T>1 应向 0.5 收缩"
    assert temperature_scale(0.8, 2.0) > 0.5, "收缩不应越过 0.5"
    assert temperature_scale(0.8, 0.5) > 0.8, "T<1 应锐化"
    for t in (0.1, 0.5, 1.0, 2.0, 10.0):
        for c in (0.0, 0.01, 0.5, 0.99, 1.0):
            v = temperature_scale(c, t)
            assert 0.0 <= v <= 1.0, f"校准结果越界: c={c}, T={t} -> {v}"
    # 保序性：单调变换
    vals = calibrate_confidence_map({'a': 0.3, 'b': 0.6, 'c': 0.9}, 3.0)
    assert vals['a'] < vals['b'] < vals['c'], "校准应保持置信度排序"
    try:
        temperature_scale(0.5, 0)
        assert False, "非正温度应被拒绝"
    except ValueError:
        pass
    print("  [OK] temperature scaling 校准钩子数值性质正确")


def test_engine_calibration_disclosure():
    """引擎校准钩子：synthesize 报告披露 calibration 元数据与未校准原值"""
    from core.engine import StateMachineEngine

    engine = StateMachineEngine('graphs/linear.yaml', trace_dir=None,
                                checkpoint_dir=None, calibration_temperature=2.0)
    result = engine.run()
    assert result['status'] == 'success', f"校准流水线应成功: {result.get('errors')}"
    cn = result['results']['synthesize']['outputs']['confidence_network']
    assert 'calibration' in cn, "应披露校准元数据"
    assert cn['calibration']['method'] == 'temperature_scaling'
    assert cn['calibration']['temperature'] == 2.0
    assert 'uncalibrated' in cn, "应保留未校准原值以便审计"
    for cid, v in cn['final'].items():
        raw = cn['uncalibrated'][cid]
        assert 0.0 <= v <= 1.0, "校准值应在 [0,1] 内"
        if raw > 0.5:
            assert v <= raw, "T>1 时高置信度应向 0.5 收缩"
    print("  [OK] 校准钩子接入 synthesize 并完整披露变换信息")

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
