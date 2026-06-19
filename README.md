# Epistemic Pipeline

[🇨🇳 简体中文](#简体中文) | [🇺🇸 English](#english)

---

<a id="简体中文"></a>
## 🇨🇳 简体中文

> 认知流水线 — 状态机驱动的动态科研分析系统

Epistemic Pipeline 彻底颠覆了传统的固定角色 Agent 框架。它将科学研究过程抽象为一台严密的“认知机器”，通过**状态机 (State Machine)** 控制流转，利用 **DAG (有向无环图)** 实现动态调度，并通过**贝叶斯信念传播 (Belief Propagation)** 解决信息冲突与幻觉。

### 核心差异 (vs 传统流水线)

| 维度 | 传统 Agent 流水线 | Epistemic Pipeline |
|------|----------------|-------------------|
| **执行单元** | 固定 N 个 Agent 顺序传递文件 | **动态状态机** (5大状态 × 动态角色挂载) |
| **角色分配** | 硬编码 (Hardcoded) | **事找人** (根据任务状态动态加载能力包) |
| **依赖调度** | 固定的线性流程 | **DAG 图计算** (支持运行时自动并行与回退) |
| **可信度评估**| 粗暴的标签判定 (如 🟢🟡🔴) | **连续置信度网络** (基于数学的交叉印证与收敛) |
| **质量控制** | 依赖大模型自身的 Prompt | **硬性质量门 (Gatekeeper)** (强规则前置阻断) |
| **价值体系** | 系统内置标准 | **完全可插拔的认知框架** (用户自定义求真规则) |

### 核心架构层级
1. **调度与控制层 (Control Plane)**: `engine.py`, `dependency_graph.py`, `gatekeeper.py` —— 负责运行时拓扑计算、状态流转与质量拦截。
2. **知识与认知层 (Cognitive Plane)**: `confidence_net.py`, `validators/` —— 负责知识图谱提取与多源冲突的数学收敛。
3. **代理与执行层 (Agent Plane)**: `llm_harness.py`, `roles/` —— 负责大模型能力的动态组装与结构化数据对齐。

### 快速开始
```bash
# 验证并执行一条线性流水线
python3 core/engine.py run graphs/linear.yaml
```

---

<a id="english"></a>
## 🇺🇸 English

> Epistemic Pipeline — State-machine driven dynamic research analysis system

Epistemic Pipeline completely revolutionizes traditional fixed-role Agent frameworks. It abstracts the scientific research process into a rigorous "cognitive machine", utilizing a **State Machine** for flow control, **DAG (Directed Acyclic Graph)** for dynamic scheduling, and **Bayesian Belief Propagation** to resolve information conflicts and hallucinations.

### Key Differences (vs Traditional Pipelines)

| Dimension | Traditional Agent Pipeline | Epistemic Pipeline |
|-----------|----------------------------|--------------------|
| **Execution Unit** | Fixed N Agents passing files sequentially | **Dynamic State Machine** (5 states × dynamic role binding) |
| **Role Assignment**| Hardcoded | **Task-driven** (Dynamically load capability packs based on state) |
| **Dependency** | Fixed linear flow | **DAG Computation** (Supports runtime auto-parallelism and fallback) |
| **Confidence** | Rough tagging (e.g., 🟢🟡🔴) | **Continuous Confidence Network** (Math-based cross-validation & convergence) |
| **Quality Control**| Relies on LLM's own Prompt | **Strict Quality Gates (Gatekeeper)** (Hard-rule upfront blocking) |
| **Value System** | Built-in system standards | **Pluggable Epistemic Framework** (User-defined truth-seeking rules) |

### Core Architecture Layers
1. **Control Plane**: `engine.py`, `dependency_graph.py`, `gatekeeper.py` — Responsible for runtime topology computation, state transition, and quality interception.
2. **Cognitive Plane**: `confidence_net.py`, `validators/` — Responsible for knowledge graph extraction and mathematical convergence of multi-source conflicts.
3. **Agent Plane**: `llm_harness.py`, `roles/` — Responsible for dynamic assembly of LLM capabilities and structured data alignment.

### Quick Start
```bash
# Validate and execute a linear pipeline
python3 core/engine.py run graphs/linear.yaml
```
