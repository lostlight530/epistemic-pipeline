# Epistemic Pipeline

[🇨🇳 简体中文](#简体中文) | [🇺🇸 English](#english)

---

<a id="简体中文"></a>
## 🇨🇳 简体中文

> 认知流水线 — 状态机驱动的动态科研分析系统

Epistemic Pipeline 彻底颠覆了传统的固定角色 Agent 框架。它将科学研究过程抽象为一台严密的“认知机器”，通过**状态机 (State Machine)** 控制流转，利用 **DAG (有向无环图)** 实现**多线程动态并行调度**，并通过**贝叶斯信念传播 (Belief Propagation)** 解决信息冲突与幻觉。

### 核心差异 (vs 传统流水线/LangGraph/MetaGPT)

| 维度 | 传统 Agent 流水线 / LangChain | Epistemic Pipeline |
|------|----------------|-------------------|
| **执行单元** | 固定 N 个 Agent 顺序传递文件 | **动态状态机** (5大状态 × 动态角色挂载) |
| **依赖调度** | 固定的线性流程 | **并发 DAG 图计算** (支持运行时自动并发、线程池加速与状态回退) |
| **结构化输出** | 弱约束，易发散 | **强约束** (所有 Agent 文档内嵌严格的 JSON/YAML Schema) |
| **可信度评估**| 粗暴的标签判定 (如 🟢🟡🔴) | **连续置信度网络** (基于数学的交叉印证与收敛) |
| **质量控制** | 依赖大模型自身的 Prompt | **硬性质量门 (Gatekeeper)** (严格的 Schema 拦截与校验) |


### 严格的规则约束 (Strict Rule Constraints)
- **DAG 严格校验**：拒绝任何包含循环依赖（Cycle）或不可达节点（Unreachable Node）的图。
- **质量门 (Gatekeeper)**：缺少输入字段的验证会直接抛出 `MISSING_GATE_INPUT`，严格阻断伪造输出。
- **置信度收敛**：所有信念传播（Belief Propagation）置信度被强制要求在 `[0, 1]` 之间，未收敛的状态将显式抛出 `CONFIDENCE_NOT_CONVERGED`。

### 快速开始
```bash
# 执行支持并发的 DAG 并行组
python3 core/engine.py run graphs/parallel.yaml
```

---

<a id="english"></a>
## 🇺🇸 English

> Epistemic Pipeline — State-machine driven dynamic research analysis system

Epistemic Pipeline completely revolutionizes traditional fixed-role Agent frameworks. It abstracts the scientific research process into a rigorous "cognitive machine", utilizing a **State Machine** for flow control, **DAG (Directed Acyclic Graph)** for **multi-threaded dynamic parallel scheduling**, and **Bayesian Belief Propagation** to resolve information conflicts and hallucinations.

### Key Differences (vs LangChain/MetaGPT)

| Dimension | Traditional Agent Pipeline | Epistemic Pipeline |
|-----------|----------------------------|--------------------|
| **Execution Unit** | Fixed N Agents passing files sequentially | **Dynamic State Machine** (5 states × dynamic role binding) |
| **Dependency** | Fixed linear flow | **Concurrent DAG Computation** (Auto-parallelism via ThreadPool, fallback support) |
| **Structured Output** | Weak constraints, prone to drift | **Strict Constraints** (JSON/YAML Schemas strictly embedded in all Agent docs) |
| **Confidence** | Rough tagging (e.g., 🟢🟡🔴) | **Continuous Confidence Network** (Math-based cross-validation) |
| **Quality Control**| Relies on LLM's own Prompt | **Strict Quality Gates (Gatekeeper)** (Hard Schema blocking) |


### Strict Rule Constraints
- **Strict DAG Validation**: Rejects any graph containing cyclic dependencies or unreachable nodes.
- **Gatekeeper**: Verification lacking input fields will directly throw `MISSING_GATE_INPUT`, strictly blocking forged outputs.
- **Confidence Convergence**: All Belief Propagation confidences are forced to be within `[0, 1]`. Unconverged states will explicitly throw `CONFIDENCE_NOT_CONVERGED`.

### Quick Start
```bash
# Execute DAG parallel groups concurrently
python3 core/engine.py run graphs/parallel.yaml
```
