# 架构设计与核心机制 / Architecture Design & Core Mechanisms

[🇨🇳 简体中文](#简体中文) | [🇺🇸 English](#english)

---

<a id="简体中文"></a>
## 🇨🇳 简体中文

### 1. 核心定位
Epistemic Pipeline 是一个**状态机驱动的动态科研认知引擎**。
传统的 Agent 框架侧重于“人（角色）”和“任务传递”，而本系统将复杂的认知过程抽象为一台能够自我纠错、动态演进的机器。这台机器关注的核心不再是“谁来做”，而是认知发展到了哪个**状态（State）**、知识之间具有怎样的**依赖（DAG）**以及如何进行**相互印证（Confidence Network）**。

### 2. 整体架构
系统可划分为三个深度解耦且相互配合的核心层：

#### 2.1 调度与控制层 (Control Plane)
*   **组件**: `core/engine.py`, `core/dependency_graph.py`, `core/gatekeeper.py`
*   **职责**: 负责控制工作流的宏观走向。
    *   **动态图计算**: 支持基于前置任务的 DAG 解析，找出能够完全并行的任务（如 `diamond.yaml` 和 `adaptive.yaml`）。
    *   **动态状态流转 (Event Loop)**: 摒弃静态的拓扑执行，使用事件驱动的引擎。当触发回退条件（如 Verify 阶段发现致命矛盾）时，系统能够动态重定向和回滚。
    *   **质量门 (Gatekeeper)**: 在状态转移前实施严格拦截。只有数据结构符合 `epistemic.rules.yaml` 和节点 `quality_gates` 要求时，才允许放行。

#### 2.2 代理与执行层 (Agent Plane)
*   **组件**: `core/llm_harness.py`, `roles/*.md`, `states/*.yaml`
*   **职责**: 负责大模型（LLM）的实例化与能力调用。
    *   **动态角色挂载**: 引擎运行到对应状态时，动态提取主副角色（如 `verifier` / `auditor`）的能力包约束，转化为 System Prompt。
    *   **结构化输出解析**: 强制将 LLM 自由发散的文本输出解析并对齐为特定的 JSON 结构，从源头扼杀非结构化的废话。

#### 2.3 知识与认知层 (Cognitive Plane)
*   **组件**: `core/confidence_net.py`, `core/knowledge_extractor.py`, `validators/*`
*   **职责**: 负责知识的交叉验证和真伪收敛。
    *   **网络桥接**: 将 LLM 提取的知识断言（Claims）和逻辑冲突（Conflicts）转化为贝叶斯传播网络中的节点和边。
    *   **数学收敛**: 利用连续值的置信度在网络中进行迭代（Belief Propagation），让相互支持的节点置信度上升，相互矛盾的节点置信度下降，最终沉淀出高可靠认知图谱。

### 3. 工作流演进闭环
1.  **发现 (Discover)**: 扫描来源，提取原始文本，强制补充绝对无损的元数据。
2.  **分析 (Analyze)**: 将非结构化文本拆解为知识断言（Claims）和实体网络。
3.  **验证 (Verify)**: LLM 交叉验证并指出冲突，Gatekeeper 拦截覆盖率不达标的数据。
4.  **综合 (Synthesize)**: 置信度网络运行并收敛，过滤低分数据，生成高维洞察（Insights）。
5.  **归档 (Archive)**: 沉淀结构化知识库，保留一条可供溯源的完整证据链（Provenance Chain）。

---

<a id="english"></a>
## 🇺🇸 English

### 1. Core Positioning
The Epistemic Pipeline is a **State-machine Driven Dynamic Epistemic Engine**.
While traditional Agent frameworks focus on "personas" and "task passing," this system abstracts complex cognitive processes into a self-correcting, dynamically evolving machine. The core focus is no longer "who does it," but rather what **State** the cognition has reached, the **Dependency (DAG)** between knowledge units, and how they cross-validate via a **Confidence Network**.

### 2. Overall Architecture
The system is divided into three deeply decoupled yet collaborative core layers:

#### 2.1 Control Plane
*   **Components**: `core/engine.py`, `core/dependency_graph.py`, `core/gatekeeper.py`
*   **Responsibilities**: Controls the macro workflow trajectory.
    *   **Dynamic Graph Computation**: Parses DAG based on prerequisites to identify fully parallelizable tasks.
    *   **Dynamic State Transition (Event Loop)**: Replaces static topology execution with an event-driven engine. Supports dynamic redirection and fallback when conditions trigger (e.g., fatal contradictions found in Verify).
    *   **Gatekeeper**: Enforces strict interception before state transitions, ensuring outputs meet `epistemic.rules.yaml` and `quality_gates` requirements.

#### 2.2 Agent Plane
*   **Components**: `core/llm_harness.py`, `roles/*.md`, `states/*.yaml`
*   **Responsibilities**: Handles LLM instantiation and capability invocation.
    *   **Dynamic Role Binding**: Dynamically loads capability constraints of primary/secondary roles (e.g., `verifier` / `auditor`) into System Prompts based on the current state.
    *   **Structured Output Parsing**: Forces free-form LLM text into rigid JSON structures, eliminating unstructured hallucination at the source.

#### 2.3 Cognitive Plane
*   **Components**: `core/confidence_net.py`, `core/knowledge_extractor.py`, `validators/*`
*   **Responsibilities**: Manages knowledge cross-validation and truth convergence.
    *   **Network Bridging**: Translates LLM-extracted Claims and Conflicts into nodes and edges for the Bayesian propagation network.
    *   **Mathematical Convergence**: Uses continuous confidence values in Belief Propagation iterations. Mutually supportive nodes increase in confidence, while contradicting ones decrease, yielding a highly reliable knowledge graph.

### 3. Workflow Evolution Loop
1.  **Discover**: Scans sources, extracts raw text, and mandates absolute lossless metadata.
2.  **Analyze**: Deconstructs unstructured text into Knowledge Claims and entity networks.
3.  **Verify**: Cross-validates via LLM to spot conflicts; Gatekeeper blocks sub-standard coverage.
4.  **Synthesize**: Executes Confidence Network convergence, filters low-score data, and generates high-dimensional Insights.
5.  **Archive**: Persists the structured knowledge base alongside an auditable Provenance Chain.
