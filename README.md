# Epistemic Pipeline

[简体中文](#简体中文) | [English](#english)

---

<a id="简体中文"></a>
## 简体中文

> 认知流水线 — 状态机驱动的动态科研分析系统

Epistemic Pipeline 将科学研究过程抽象为一台严密的"认知机器"，通过**状态机 (State Machine)** 控制流转，利用 **DAG (有向无环图)** 实现**多线程动态并行调度**。

### 核心引擎 (Implemented)

| 维度 | 传统 Agent 流水线 | Epistemic Pipeline |
|------|------------------|-------------------|
| **执行单元** | 固定 N 个 Agent 顺序传递 | **动态状态机** (5大状态) |
| **依赖调度** | 固定的线性流程 | **并发 DAG 图计算** (线程池加速) |
| **结构化输出** | 弱约束，易发散 | **强约束** (JSON/YAML Schema 校验) |

### 严格约束

- **DAG 严格校验**：拒绝任何包含循环依赖或不可达节点的图
- **Schema 拦截**：缺少输入字段会直接抛出 `MISSING_GATE_INPUT`

### 已接入主引擎的执行链 (Integrated Execution Chain)

主引擎每个节点的真实执行路径为：**角色绑定加载 (`roles/*.md`) → LLM Harness 结构化输出 → Gatekeeper 质量门拦截 (`validators/`) → synthesize 阶段置信度网络传播收敛 (`core/confidence_net.py`)**。

- Gatekeeper 质量门 (`validators/`)：每个节点输出必须通过其状态的 `quality_gates`，否则节点失败并终止流水线（含 `MISSING_GATE_INPUT` 拦截）
- 置信度网络 (`core/confidence_net.py`)：`synthesize` 阶段汇总上游 `claims_registry` / `conflict_registry` / `confidence_seed`，经 `KnowledgeExtractor` 桥接后真实迭代收敛，未收敛将触发质量门失败
- 动态角色绑定 (`roles/`)：每个节点按状态定义加载主/副角色模板组装 Prompt

### 可靠性与可观测性 (Reliability & Observability)

- **结构化运行轨迹** (`core/run_tracer.py`)：每节点 start/end 写入 `traces/<run_id>.jsonl`，字段命名对齐 OTel GenAI 语义约定（`gen_ai.operation.name=invoke_agent`、`gen_ai.conversation.id=run_id`、`error.type`、耗时），并以 SHA-256 `prev_hash` 哈希链防篡改（该约定仍为 Development 级，仅对齐命名，不依赖 SDK）
- **LLM Provider 协议** (`core/llm_harness.py`)：`LLMProvider.complete(system, user, schema) -> dict` 依赖注入；`MockProvider` 承载确定性桩数据并附带 5 阶段输出契约（`STAGE_CONTRACTS`），未来真实 provider 复用同一契约测试
- **弹性执行** (`core/resilience.py`)：节点可声明 `retry{max_attempts, base_delay, factor}` 与 `timeout_seconds`；transient 错误（超时/连接）指数退避 + jitter 重试，permanent 错误（未实现/参数错）fail-fast 不重试；并行组失败不再丢弃兄弟节点结果
- **节点级检查点** (`checkpoints/<run_id>/checkpoint.json`)：每层完成原子落盘；`run(resume_from=run_id)` 复用已成功节点、仅重跑失败及下游（LangGraph 检查点模式）；跨图续跑 fail-closed 拒绝
- **置信度校准钩子** (`core/calibration.py`)：可选 temperature scaling 单参数校准（`calibration_temperature`），`synthesize` 报告披露 `calibration` 元数据与 `uncalibrated` 原值；mock 阶段置信度是启发值而非概率

### 实验性功能 (Experimental — Not Integrated)

以下模块存在于仓库但**尚未接入主引擎**：

- 自适应工作流 (`graphs/adaptive.yaml`)

> 注意：`core/llm_harness.py` 默认以 `mock=True` 运行；真实 LLM 调用仍为 `NotImplementedError`。

### 快速开始

```bash
# 安装依赖（仅 pyyaml 与 numpy，无其他第三方依赖）
pip install pyyaml numpy

# 执行支持并发的 DAG 并行组
python3 core/engine.py run graphs/parallel.yaml

# 从失败 run 的检查点断点续跑（仅重跑失败及下游节点）
python3 core/engine.py run graphs/parallel.yaml --resume-from <run_id>

# 运行测试套件
python3 tests/test_all.py
```

---

<a id="english"></a>
## English

> Epistemic Pipeline — State-machine driven dynamic research analysis system

Epistemic Pipeline abstracts the scientific research process into a rigorous "cognitive machine", utilizing a **State Machine** for flow control and **DAG (Directed Acyclic Graph)** for **multi-threaded dynamic parallel scheduling**.

### Core Engine (Implemented)

| Dimension | Traditional Agent Pipeline | Epistemic Pipeline |
|-----------|----------------------------|--------------------|
| **Execution Unit** | Fixed N Agents passing files sequentially | **Dynamic State Machine** (5 states) |
| **Dependency** | Fixed linear flow | **Concurrent DAG Computation** (ThreadPool) |
| **Structured Output** | Weak constraints, easy to diverge | **Strong Constraints** (JSON/YAML Schema validation) |

### Strict Constraints

- **DAG Strict Validation**: Rejects any graph containing cycles or unreachable nodes
- **Schema Interception**: Missing input fields directly throw `MISSING_GATE_INPUT`

### Integrated Execution Chain

Each node's real execution path in the main engine is: **role binding (`roles/*.md`) → LLM Harness structured output → Gatekeeper interception (`validators/`) → confidence network propagation at `synthesize` (`core/confidence_net.py`)**.

- Gatekeeper (`validators/`): every node output must pass its state's `quality_gates`, otherwise the node fails and aborts the pipeline (including `MISSING_GATE_INPUT` interception)
- Confidence network (`core/confidence_net.py`): at `synthesize`, upstream `claims_registry` / `conflict_registry` / `confidence_seed` are bridged via `KnowledgeExtractor` and iterated to real convergence; non-convergence triggers a quality-gate failure
- Dynamic role binding (`roles/`): each node assembles its prompt from the primary/secondary role templates defined by the state

### Reliability & Observability

- **Structured run traces** (`core/run_tracer.py`): per-node start/end records in `traces/<run_id>.jsonl`, field names aligned with OTel GenAI semantic conventions (`gen_ai.operation.name=invoke_agent`, `gen_ai.conversation.id=run_id`, `error.type`, duration), tamper-evident via a SHA-256 `prev_hash` chain (the convention is still Development-grade — we align naming only, no SDK dependency)
- **LLM Provider protocol** (`core/llm_harness.py`): dependency-injected `LLMProvider.complete(system, user, schema) -> dict`; `MockProvider` carries the deterministic stub data plus a 5-stage output contract (`STAGE_CONTRACTS`) that future real providers reuse in contract tests
- **Resilient execution** (`core/resilience.py`): nodes may declare `retry{max_attempts, base_delay, factor}` and `timeout_seconds`; transient errors (timeout/connection) retry with exponential backoff + jitter, permanent errors (not-implemented/bad-args) fail fast; parallel-group failures no longer discard sibling results
- **Node-level checkpoints** (`checkpoints/<run_id>/checkpoint.json`): atomic writes after each layer; `run(resume_from=run_id)` reuses successful nodes and re-runs only failures and downstream (LangGraph checkpoint pattern); cross-graph resume is rejected fail-closed
- **Confidence calibration hook** (`core/calibration.py`): optional single-parameter temperature scaling (`calibration_temperature`); the `synthesize` report discloses `calibration` metadata and `uncalibrated` originals; mock-stage confidences are heuristics, not probabilities

### Experimental Features (Not Integrated)

The following modules exist in the repo but are **not yet wired into the main engine**:

- Adaptive workflow (`graphs/adaptive.yaml`)

> Note: `core/llm_harness.py` runs with `mock=True` by default; real LLM calls still raise `NotImplementedError`.

### Quick Start

```bash
# Install dependencies (pyyaml and numpy only, nothing else)
pip install pyyaml numpy

# Run concurrent DAG parallel group
python3 core/engine.py run graphs/parallel.yaml

# Resume a failed run from its checkpoint (re-runs only failed + downstream nodes)
python3 core/engine.py run graphs/parallel.yaml --resume-from <run_id>

# Run the test suite
python3 tests/test_all.py
```

---

## Documentation

- [Architecture](ARCHITECTURE.md)
- [Customization Guide](CUSTOMIZATION_GUIDE.md)
- [Examples](examples/)

## License

MIT License
