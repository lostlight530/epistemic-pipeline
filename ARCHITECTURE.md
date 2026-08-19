# 架构设计与核心机制 / Architecture Design & Core Mechanisms

[🇨🇳 简体中文](#简体中文) | [🇺🇸 English](#english)

---

<a id="简体中文"></a>
## 🇨🇳 简体中文

### 1. 核心定位
Epistemic Pipeline 是一个**状态机驱动的动态科研认知引擎**。
传统的 Agent 框架（如早期的 LangChain 或简单的 AutoGPT）侧重于“人（角色）”和“任务传递”，而本系统将复杂的认知过程抽象为一台能够自我纠错、动态演进的机器。这台机器不仅关注**状态（State）**和**知识交叉印证（Confidence Network）**，更重要的是，它原生支持 **并发执行的 DAG**。

### 2. 整体架构
系统可划分为三个深度解耦且相互配合的核心层：

#### 2.1 调度与控制层 (Control Plane)
*   **组件**: `core/engine.py`, `core/dependency_graph.py`, `core/gatekeeper.py`
*   **动态图计算与多线程并行**: 支持基于前置任务的 DAG 解析，找出能够完全并行的任务（如 `parallel.yaml` 中的 `analyze` 组），并通过 `ThreadPoolExecutor` 真正实现并发加速。并行组内任一节点失败时，兄弟节点的已完成结果完整保留在失败负载中。
*   **质量门 (Gatekeeper)**: 在状态转移前实施严格拦截。只有数据结构符合 `epistemic.rules.yaml` 和节点 `quality_gates` 要求时，才允许放行。
*   **弹性执行 (`core/resilience.py`)**: 节点可声明 `retry{max_attempts, base_delay, factor}` 与 `timeout_seconds`；异常被分类为 transient（超时/连接，指数退避 + jitter 重试）或 permanent（未实现/参数错误，fail-fast 不重试）。超时经 `future.result(timeout=)` 实现——Python 线程无法强杀，超时后调用方立即失败，后台线程自然结束。
*   **节点级检查点**: 每层完成后将成功节点结果原子落盘至 `checkpoints/<run_id>/checkpoint.json`（状态为纯 dict，天然可序列化）；`run(resume_from=run_id)` 复用成功节点、仅重跑失败及下游，跨图续跑 fail-closed 拒绝。

#### 2.2 代理与执行层 (Agent Plane)
*   **组件**: `core/llm_harness.py`, `roles/*.md`, `states/*.yaml`
*   **Provider 协议抽象**: `LLMHarness` 通过依赖注入的 `LLMProvider.complete(system, user, schema) -> dict` 获取结构化输出；`MockProvider` 承载确定性桩数据并声明 5 阶段输出契约（`STAGE_CONTRACTS`），真实 provider 接入时复用同一套契约测试。
*   **结构化输出解析**: 为了彻底解决幻觉和格式漂移，所有的 `roles/*.md` 中都直接内嵌了 `JSON Schema`。大模型输出会被强制约束到这些数据结构中。

#### 2.3 知识与认知层 (Cognitive Plane)
*   **组件**: `core/confidence_net.py`, `core/knowledge_extractor.py`, `core/calibration.py`, `validators/*`
*   **数学收敛**: 利用连续值的置信度在网络中进行迭代（Belief Propagation），让相互支持的节点置信度上升，沉淀出高可靠认知图谱。
*   **校准钩子**: 可选 temperature scaling 对收敛置信度做单调保序变换，报告披露 `calibration` 元数据与 `uncalibrated` 原值；mock 阶段置信度为启发值而非概率，不做真实校准宣称。

#### 2.4 可观测性层 (Observability Plane)
*   **组件**: `core/run_tracer.py`
*   **结构化运行轨迹**: 每节点 start/end 写入 `traces/<run_id>.jsonl`，字段命名对齐 OTel GenAI 语义约定（Development 级，仅对齐命名不依赖 SDK）：`gen_ai.operation.name=invoke_agent`、`gen_ai.agent.name=state_id`、`gen_ai.conversation.id=run_id`、`error.type`、`duration_ms`。
*   **防篡改审计**: 每条记录携带 SHA-256 `prev_hash`/`hash` 哈希链，`RunTracer.verify_chain()` 可检测任何篡改、删除或重排；断点续跑时哈希链在同一 run_id 上延续。

---

<a id="english"></a>
## 🇺🇸 English

### 1. Core Positioning
The Epistemic Pipeline is a **State-machine Driven Dynamic Epistemic Engine**.
Unlike early LangChain or AutoGPT frameworks, this system focuses on **State**, **Confidence Networks**, and native **Concurrent DAG Execution**.

### 2. Overall Architecture

#### 2.1 Control Plane
*   **Components**: `core/engine.py`, `core/dependency_graph.py`, `core/gatekeeper.py`
*   **Dynamic Graph Computation & Multi-threading**: Parses DAG to identify fully parallelizable tasks (e.g., `analyze` groups in `parallel.yaml`) and executes them concurrently using `ThreadPoolExecutor`. When a node in a parallel group fails, completed sibling results are preserved in the failure payload.
*   **Gatekeeper**: Enforces strict interception before state transitions, ensuring outputs meet `epistemic.rules.yaml`.
*   **Resilient Execution (`core/resilience.py`)**: Nodes may declare `retry{max_attempts, base_delay, factor}` and `timeout_seconds`; exceptions are classified as transient (timeout/connection — retried with exponential backoff + jitter) or permanent (not-implemented/bad-args — fail-fast, never retried). Timeouts use `future.result(timeout=)`; Python threads cannot be killed, so the caller fails immediately while the background thread finishes naturally.
*   **Node-level Checkpoints**: Successful node results are atomically persisted to `checkpoints/<run_id>/checkpoint.json` after each layer (state is a plain dict, natively serializable); `run(resume_from=run_id)` reuses successful nodes and re-runs only failures and downstream; cross-graph resume is rejected fail-closed.

#### 2.2 Agent Plane
*   **Components**: `core/llm_harness.py`, `roles/*.md`, `states/*.yaml`
*   **Provider Protocol**: `LLMHarness` obtains structured output through a dependency-injected `LLMProvider.complete(system, user, schema) -> dict`; `MockProvider` carries the deterministic stub data and declares a 5-stage output contract (`STAGE_CONTRACTS`) reused by contract tests for any future real provider.
*   **Structured Output Parsing**: To completely resolve hallucinations and format drift, all `roles/*.md` documents have strict `JSON Schema` definitions embedded natively.

#### 2.3 Cognitive Plane
*   **Components**: `core/confidence_net.py`, `core/knowledge_extractor.py`, `core/calibration.py`, `validators/*`
*   **Mathematical Convergence**: Uses continuous confidence values in Belief Propagation iterations to yield a highly reliable knowledge graph.
*   **Calibration Hook**: Optional temperature scaling applies a monotonic order-preserving transform to converged confidences, with `calibration` metadata and `uncalibrated` originals disclosed in the report; mock-stage confidences are heuristics, not probabilities, and no real calibration is claimed.

#### 2.4 Observability Plane
*   **Components**: `core/run_tracer.py`
*   **Structured Run Traces**: Per-node start/end records in `traces/<run_id>.jsonl`, field names aligned with OTel GenAI semantic conventions (Development-grade — naming alignment only, no SDK): `gen_ai.operation.name=invoke_agent`, `gen_ai.agent.name=state_id`, `gen_ai.conversation.id=run_id`, `error.type`, `duration_ms`.
*   **Tamper-evident Audit**: Every record carries a SHA-256 `prev_hash`/`hash` chain; `RunTracer.verify_chain()` detects any tampering, deletion, or reordering; resuming a run extends the chain on the same run_id.
