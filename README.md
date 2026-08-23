# Epistemic Pipeline

> 状态机驱动、可门控、可恢复、可追踪、可溯源的科研认知执行系统  
> State-machine-driven research execution with gates, recovery, traces, and provenance

## 简体中文

### 当前定位

Epistemic Pipeline 把科研分析过程建模为 **状态机 + DAG + 契约 + 证据链**，而不是固定 N 个 Agent 顺序传文件。

规范状态为：

```text
discover -> analyze -> verify -> synthesize -> archive
```

主执行链：

```text
Role Binding
    ↓
LLM Harness (默认 deterministic mock)
    ↓
Gatekeeper
    ↓
Confidence Network (synthesize)
    ↓
Trace + Checkpoint
    ↓
Audited Run Bundle -> PROV-aligned provenance
```

### 已接入能力

- **DAG 调度**：`linear` / `parallel` / `diamond` 可执行；`adaptive` 仍是实验性路由规格，主引擎 fail-closed 拒绝
- **动态角色绑定**：按状态加载角色模板
- **LLM Provider 协议**：`LLMProvider.complete(system, user, schema) -> dict`；仓库默认仍使用确定性 `MockProvider`，不虚报内置真实 LLM
- **Gatekeeper**：节点输出必须通过对应质量门
- **置信度网络**：`synthesize` 汇总上游 claims/conflicts 并迭代收敛；mock 置信度是启发值，不是校准概率
- **弹性执行**：transient 错误指数退避+jitter，permanent 错误 fail-fast，节点支持 caller-side timeout
- **检查点**：每层原子写入 `checkpoints/<run_id>/checkpoint.json`；同图续跑只复用成功节点
- **项目轨迹**：`traces/<run_id>.jsonl` 使用 SHA-256 `prev_hash` 链；字段名参考适用的 OpenTelemetry GenAI Development 语义，但不是完整 OTel SDK/span 实现
- **科研 provenance**：`core/run_bundle.py` 在一次执行后输出 `provenance/<run_id>.prov.json`，采用 W3C PROV 核心 Entity / Activity / Agent 与关系语义形成哈希谱系

### 新的审计运行入口

低层执行仍可直接使用：

```bash
python3 core/engine.py run graphs/linear.yaml
```

需要完整科研审计包时使用：

```bash
python3 core/run_bundle.py graphs/linear.yaml
python3 core/run_bundle.py graphs/parallel.yaml --provenance-dir provenance
```

`run_bundle` 组合现有 engine、trace、checkpoint 与新的 provenance profile。它不会把节点完整研究内容复制到 provenance 文件；默认只记录规范化 SHA-256、状态、stage、依赖关系以及 trace/checkpoint 文件哈希。

### Provenance 语义边界

`epistemic-pipeline/prov@1` 是一个 **W3C PROV-aligned JSON profile**，使用：

- `prov:Entity`：依赖图、节点输出、trace、checkpoint
- `prov:Activity`：整次 run 与节点执行
- `prov:SoftwareAgent`：epistemic-pipeline
- `used`
- `wasGeneratedBy`
- `wasDerivedFrom`
- `wasAssociatedWith`

它不是 PROV-O RDF 序列化器，也不声称实现所有 W3C PROV 表达形式。这里借用的是稳定的 provenance 数据模型语义，而不是伪造格式兼容。

### OpenTelemetry 语义边界

`core/run_tracer.py` 的项目 JSONL 轨迹继续保留。适用字段名参考独立 `semantic-conventions-genai` 仓库中的 Development 级 GenAI agent conventions；项目的 `start` / `end` 记录不是 OTel Span Event API 事件，也不依赖 OTel SDK。

### 验证

```bash
python -m pip install pyyaml numpy
make test
```

`make test` 运行原有执行链测试和新的 provenance / run-bundle 契约。`.github/workflows/ci.yml` 在 PR 与 `main` push 上用 Python 3.12 运行同一套测试。

### 诚实边界

- 真实 LLM provider 仍需外部实现并注入，仓库不内置假“联网模型”
- `graphs/adaptive.yaml` 仍未接入主引擎
- 线程 timeout 让调用方快速失败，但不能强杀已经运行的 Python 线程
- temperature scaling hook 不等于真实概率校准；真实校准需要真实预测和标注数据拟合参数
- provenance 默认是哈希谱系，不是内容存档；不能从哈希恢复原研究内容
- OTel 与 PROV 都是**语义对齐边界**，不是 SDK/RDF 全规格兼容声明

### 科研软件引用

仓库新增 `CITATION.cff`，使用 Citation File Format 1.2.0。

---

## English

### Positioning

Epistemic Pipeline models research analysis as **state machine + DAG + contracts + evidence lineage**, rather than a fixed chain of N agents passing files.

Canonical states:

```text
discover -> analyze -> verify -> synthesize -> archive
```

Integrated chain:

```text
Role Binding -> LLM Harness -> Gatekeeper -> Confidence Network -> Trace/Checkpoint -> Audited Run Bundle
```

### Integrated capabilities

- executable `linear`, `parallel`, and `diamond` DAGs; `adaptive` remains experimental and is rejected fail-closed
- dynamic role templates per state
- dependency-injected `LLMProvider` protocol with deterministic mock as the repository default
- per-state quality gates
- synthesize-stage confidence propagation and convergence
- transient/permanent retry classification, exponential backoff+jitter, and caller-side node timeout
- atomic checkpoints and same-graph resume
- SHA-256 chained project JSONL traces with carefully scoped OpenTelemetry GenAI naming alignment
- `epistemic-pipeline/prov@1`, a W3C PROV-aligned provenance profile for graph, node-output, trace, and checkpoint lineage

### Audited research-run entry point

```bash
python3 core/run_bundle.py graphs/linear.yaml
```

The low-level engine remains available independently. `run_bundle.py` composes the existing engine artifacts into an auditable research run and writes `provenance/<run_id>.prov.json`.

The provenance file records canonical hashes and structural metadata by default, not full research payloads. Its model uses PROV Entity / Activity / Agent semantics and `used`, `wasGeneratedBy`, `wasDerivedFrom`, and `wasAssociatedWith` relations. It is not a PROV-O RDF serializer.

### Observability boundary

The repository JSONL trace is a project audit format. Applicable field names follow Development-grade OpenTelemetry GenAI agent semantic conventions where useful, but the project does not claim OTel SDK/span/event conformance.

### Verification

```bash
python -m pip install pyyaml numpy
make test
```

GitHub Actions runs the same contract on pull requests and `main` pushes with Python 3.12.

### Boundaries

Real LLM providers are external integrations; adaptive routing remains experimental; mock confidence is heuristic; caller timeouts cannot kill underlying threads; provenance hashes are evidence identifiers rather than content archives.

## Documentation

- [Architecture](ARCHITECTURE.md)
- [Customization Guide](CUSTOMIZATION_GUIDE.md)
- [Examples](examples/README.md)
- [Agent Guide](AGENTS.md)
- [Manifest](MANIFEST.yaml)

## License

MIT License
