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

### 实验性功能 (Experimental — Not Integrated)

以下模块存在于仓库但**尚未接入主引擎**：

- 动态角色绑定 (`roles/`)
- Gatekeeper 质量门 (`validators/`)
- 置信度网络 (`belief_propagation/`)
- 自适应工作流 (`adaptive/`)

### 快速开始

```bash
# 执行支持并发的 DAG 并行组
python3 core/engine.py run graphs/parallel.yaml
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

### Experimental Features (Not Integrated)

The following modules exist in the repo but are **not yet wired into the main engine**:

- Dynamic role binding (`roles/`)
- Gatekeeper quality gate (`validators/`)
- Belief propagation network (`belief_propagation/`)
- Adaptive workflow (`adaptive/`)

### Quick Start

```bash
# Run concurrent DAG parallel group
python3 core/engine.py run graphs/parallel.yaml
```

---

## Documentation

- [Architecture](ARCHITECTURE.md)
- [Customization](CUSTOMIZATION.md)
- [Examples](examples/)

## License

MIT License
