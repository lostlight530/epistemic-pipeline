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
*   **动态图计算与多线程并行**: 支持基于前置任务的 DAG 解析，找出能够完全并行的任务（如 `parallel.yaml` 中的 `analyze` 组），并通过 `ThreadPoolExecutor` 真正实现并发加速。
*   **质量门 (Gatekeeper)**: 在状态转移前实施严格拦截。只有数据结构符合 `epistemic.rules.yaml` 和节点 `quality_gates` 要求时，才允许放行。

#### 2.2 代理与执行层 (Agent Plane)
*   **组件**: `core/llm_harness.py`, `roles/*.md`, `states/*.yaml`
*   **结构化输出解析**: 为了彻底解决幻觉和格式漂移，所有的 `roles/*.md` 中都直接内嵌了 `JSON Schema`。大模型输出会被强制约束到这些数据结构中。

#### 2.3 知识与认知层 (Cognitive Plane)
*   **组件**: `core/confidence_net.py`, `core/knowledge_extractor.py`, `validators/*`
*   **数学收敛**: 利用连续值的置信度在网络中进行迭代（Belief Propagation），让相互支持的节点置信度上升，沉淀出高可靠认知图谱。

---

<a id="english"></a>
## 🇺🇸 English

### 1. Core Positioning
The Epistemic Pipeline is a **State-machine Driven Dynamic Epistemic Engine**.
Unlike early LangChain or AutoGPT frameworks, this system focuses on **State**, **Confidence Networks**, and native **Concurrent DAG Execution**.

### 2. Overall Architecture

#### 2.1 Control Plane
*   **Components**: `core/engine.py`, `core/dependency_graph.py`, `core/gatekeeper.py`
*   **Dynamic Graph Computation & Multi-threading**: Parses DAG to identify fully parallelizable tasks (e.g., `analyze` groups in `parallel.yaml`) and executes them concurrently using `ThreadPoolExecutor`.
*   **Gatekeeper**: Enforces strict interception before state transitions, ensuring outputs meet `epistemic.rules.yaml`.

#### 2.2 Agent Plane
*   **Components**: `core/llm_harness.py`, `roles/*.md`, `states/*.yaml`
*   **Structured Output Parsing**: To completely resolve hallucinations and format drift, all `roles/*.md` documents have strict `JSON Schema` definitions embedded natively.

#### 2.3 Cognitive Plane
*   **Components**: `core/confidence_net.py`, `core/knowledge_extractor.py`, `validators/*`
*   **Mathematical Convergence**: Uses continuous confidence values in Belief Propagation iterations to yield a highly reliable knowledge graph.
