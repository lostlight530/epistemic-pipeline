# 01 — Source and Explanation

## 中文技术对应 / Chinese subject counterpart

**具体责任 / Owning subject:** 本目录负责定位真实实现与研究说明，目录索引不是软件执行证明

**English owner:** 01 — Source and Explanation

**可重复检查 / Reproducibility:** 应先固定 Graph/profile、state、checkpoint 及上下游 sidecar 的精确版本和 bytes，再按原文命令判断返回结果，不能把测试定义、Provider 说明或高分视为已经独立复现 / Freeze actual source and sidecar identity, execution inputs, real receipts and unknown outcomes, a declared audit cannot certify truth

| English chapter / 原章节 | 中文对应定位 / Chinese meaning |
| --- | --- |
| Implementation map | 该合同的实际规则、证据和失败范围 |
| Architecture and explanation | 该合同的实际规则、证据和失败范围 |
| Core epistemic boundaries | 该合同的实际规则、证据和失败范围 |
| Cross-layer reading | 该合同的实际规则、证据和失败范围 |

**保存不确定性 / Preserve unknowns:** 原始冲突、缺失来源、非概率 score 与失败注入观察保持各自身份，本节不新增科学或外部效果验证 / Historical and local evidence states are not silently promoted


This class answers three durable questions:

1. **What does epistemic-pipeline actually execute or validate?**
2. **Where are claim, state, graph, role, and provider boundaries explained?**
3. **Which observed results are structural/runtime evidence rather than scientific truth?**

## Implementation map

| Surface | Repository role | Boundary |
|---|---|---|
| `core/` | pipeline orchestration and repository-owned execution semantics | source defines implemented behavior; contract prose cannot add a missing runtime feature |
| `graphs/` | graph representations and graph-related evidence/state structures | graph presence or reachability does not establish claim truth |
| `states/` | explicit execution/claim lifecycle state | a state transition is repository control state, not external factual validation |
| `roles/` | repository role/actor abstractions | role labels do not establish external identity or authority |
| `validators/` | machine-readable structural/policy validation | validator success supports only the implemented rule being checked |
| `tests/` | revision-scoped regression/contract evidence | passing tests do not prove evidence sufficiency or scientific correctness |
| `Makefile` | supported engineering command entry points | command presence != command execution |

The maintenance scanner remains implementation source even when it supports class 03 materials. Its source presence is not scanner execution.

## Architecture and explanation

- root [`README.md`](../../README.md) — public repository entry point and capability overview.
- [`ARCHITECTURE.md`](./ARCHITECTURE.md) — current architecture, execution layers, evidence/claim separation, provider boundaries, and cross-repository interfaces.

Implementation and revision-matched execution evidence own actual behavior. README and Architecture explain that behavior; they do not override it.

## Core epistemic boundaries

Use the repository with these separations intact:

```text
claim indexed != claim true
evidence linked != evidence sufficient
validator PASS != scientific verification
runtime-policy PASS != truth
heuristic score != calibrated probability
provider-reported identity != vendor authentication
```

When a result is cited, identify the exact revision, input/evidence envelope, configuration/profile, command or execution surface, result, and untested boundary when material.

## Cross-layer reading

The documents under [`../02-examples-and-contracts/`](../02-examples-and-contracts/) define how claims, evidence, assertion basis, audit coverage, and cross-repository transfer are represented and interpreted.

A contract may constrain meaning; it does not prove that an external claim is correct or that a run occurred.

Current document taxonomy is routed from [`../README.md`](../README.md). Maintenance/audit material belongs to class 03 and remains separate from the repository's primary claim/evidence architecture.
