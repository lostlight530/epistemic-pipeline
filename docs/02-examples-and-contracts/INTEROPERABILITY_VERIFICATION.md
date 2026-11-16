# Interoperability and Failure Verification — epistemic-pipeline

**Status:** current runtime/contract verification, not a historical-stage record

## Owned producer and consumers

`core/evidence_envelope.py` carries explicit upstream artifact/evidence references, including an optional local byte hash, without opening or scientifically verifying their payloads. `core/claim_transfer.py` consumes exactly `epistemic-pipeline/claim-verification` sidecars and preserves claim identity/origin ambiguity, conflicts, references and non-probability heuristic-score context

`sci-render-kit` can carry an `epistemic-pipeline/evidence-envelope` and claim-verification reference through declared recipe `research_context`. This is a reference-only handoff, **not** a shared durable runtime, cross-repository provider execution, or claim acceptance

`tests/test_cross_repo_contract.py` creates ephemeral upstream artifact and claim-verification fixtures, exercises the **actual** evidence-envelope and claim-transfer producers, verifies reference identity and ambiguity preservation, and rejects unknown claim IDs. Fixtures are not complete cross-repo replay

## 声明身份与跨仓传递门禁 / Claim identity and cross-repository transfer gates

| 证据层 / Evidence object | 可保留的事实 / Preserved fact | 不允许的推论 / Forbidden inference |
| --- | --- | --- |
| Upstream artifact / 上游产物 | `core/evidence_envelope.py` 保留上游路径及可选本地 byte hash / Carries a path and optional local byte hash | 已打开源产物、完成源认证或产物科学正确 / Source retrieval, authentication or scientific correctness |
| Claim identity / 声明身份 | `core/claim_transfer.py` 只读取精确 `epistemic-pipeline/claim-verification` profile，保留 claim origin、歧义、冲突与引用 / Exact-profile transfer preserves origin, ambiguity, conflicts and references | `claim_id` 单独表示唯一命题或审计状态等于真值 / A claim ID is universally unique or an audit state establishes truth |
| Figure reference / 图形引用 | `sci-render-kit` 可从 recipe 的 `research_context` 携带 envelope 和 claim-ref / Figure recipes may carry these references | 三仓执行了共同持久运行时、验证了因果或允许声明晋级 / A shared durable runtime, causal validation or claim promotion |

**反例设计 / Falsification conditions:** duplicate one `claim_id` across distinct originating claim bodies, corrupt an upstream byte digest while keeping the declaration, erase the source/evidence provenance, supply the wrong sidecar profile, or resume from a checkpoint with a stale graph digest / 要观察实际拒绝或歧义保留，而不是仅检查预期 JSON 标签

**执行记录 / Execution record required:** retain producer and consumer revision, exact source/sidecar bytes, profile, graph/checkpoint identity, environment, command, real stdout/stderr and exit code, failure classification, and separately implemented verifier result / 同一测试 oracle 不得被重复称为独立验证

**Status / 本轮状态:** This addition specifies a review protocol, not a newly executed end-to-end pipeline or external effect recovery test / 新增的联合跨仓回放、生产商调用和非幂等副作用试验均为 `NOT_EXECUTED`

## Failure-injection matrix

| Case | Executed local mechanism | What it does **not** establish |
|---|---|---|
| Thread timeout | `run_with_timeout` raises after caller timeout, worker is released in the test | Forced termination/cancellation of external effects |
| Transient retry | Explicit `ConnectionError` is retried within bounded attempts | Exactly-once external delivery |
| Unknown failure | Unclassified `RuntimeError` is not retried | Complete provider exception taxonomy |
| Resume digest | Checkpoint graph digest mismatch fails closed | Durable transaction/atomicity across external systems |
| Legacy resume | Missing graph digest is rejected | Migration of legacy checkpoints |

`tests/test_runtime_failure_injection.py` performs the five bounded scenarios without real providers or external side effects. Timeouts can leave worker threads running; retries are not safe for non-idempotent effects without a caller-owned idempotency key and effect ledger. Successful checkpoint writes do not imply a fully durable distributed execution engine

## Verification scope and environment

Python verification baseline: **Python 3.13** and `requirements-python313.txt`, with both direct and observed transitive distribution versions pinned

```bash
python3.13 -m venv .venv
. .venv/bin/activate
python -m pip install -r requirements-python313.txt
python scripts/check_python_environment.py
make test
```

The version checker emits a JSON result and a nonzero exit code on mismatch. This is a bounded **version-set snapshot**, not a PEP 751 `pylock.toml`, a wheel-hash lock, a cross-platform guarantee, a validated new installation, or scientific reproduction. Reconcile a fresh Python 3.13 resolver output and archive package hashes/environment provenance when stronger byte-level replay is needed

The pre-existing optional `.github/workflows/tool-cli-agent-smoke.yml` runs the same bounded checks when matching PR paths trigger it. Workflow definition is not run evidence; inspect the workflow run and commit SHA before claiming execution success

## Scholarly metadata migration

`codemeta.json` uses the official CodeMeta 4.0 context `https://w3id.org/codemeta/4.0` (released 2026-09-29) rather than 3.1. Existing publication DOI, author, license and repository metadata are not rewritten. CodeMeta 4 changes the CodeMeta namespace and schema.org's HTTP/HTTPS mapping, and removes `relatedSoftware` (unused here). The local contract test verifies syntax and CITATION.cff field identity, **not** a remotely expanded JSON-LD graph, external repository index, or citation resolver

Official release: https://github.com/codemeta/codemeta/releases/tag/4.0

## Protocol boundaries

No MCP server, A2A agent service, OTel exporter, independently authenticated approval workflow, publisher certification, scientific truth verification, or R3 independent reproduction is created by these tests

