# G2 — LiveMCP-101: Execution Plans as Multi-Tool Evaluation Evidence

## Question
What changes when MCP/tool-use tasks are graded against ground-truth execution plans rather than only final outputs or raw API responses?

## Object
- Research object: LiveMCP-101
- arXiv: `2508.15760`
- Publication window: 2025-08
- Source type: benchmark paper
- Accessed: 2026-09-26

## Primary source
- https://arxiv.org/abs/2508.15760

## Reported evidence
LiveMCP-101 describes 101 curated real-world queries requiring multiple MCP tools. Its evaluation design uses ground-truth execution plans to judge whether the agent selected and sequenced the required tool operations, rather than relying only on unstable raw API outputs.

The paper reports substantial remaining difficulty for frontier models and analyzes failure modes/tool inefficiency. These results remain benchmark-reported evidence.

## Interpretation
The important epistemic move is that **plan identity becomes part of evaluation evidence**.

```text
user task
-> expected subgoals
-> ground-truth execution plan
-> tool selection
-> argument/state propagation
-> observed tool sequence
-> final result
```

A final answer can look plausible while the action sequence is incomplete, redundant, or causally unrelated. Conversely, raw API bytes can vary even when the intended plan is correctly followed.

This creates a useful separation:

```text
final-output similarity
!= execution-plan correctness

tool called
!= required state transition completed
```

## Boundary
Plan matching does not prove scientific truth, and the benchmark's tool set/tasks do not establish general tool competence. No LiveMCP task was executed locally.

## Finding
`G2_FINDING`: Q3 2025 strengthens the case for plan-level evidence: tool identity, ordering, arguments, intermediate state, and completion conditions belong beside terminal outputs in any serious agent-evaluation trace.
