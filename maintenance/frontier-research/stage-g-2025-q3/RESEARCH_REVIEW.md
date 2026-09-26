# Frontier Research Review — Stage G / 2025-Q3

- Review date: 2026-09-26
- Independence: `SAME_PRODUCER_REVIEW`

## Temporal integrity
- ART security/public-competition paper: 2025-07-28.
- LiveMCP-101: August 2025.
- UltraHorizon: late September 2025.

Reconstruction date is 2026-09-26 and is not substituted for the objects' event/publication windows.

## Method comparability
The three objects are comparable at the level of trajectory evidence and evaluation state, not as a pooled benchmark score:
- ART: adversarial policy-violation trajectory;
- LiveMCP-101: multi-tool execution-plan trajectory;
- UltraHorizon: partially observable long-horizon trajectory.

## Boundary review
No attacks, benchmark episodes, MCP tasks, model inference, judge/evaluator replay, statistical meta-analysis, long-horizon rollout, or independent reproduction was executed.

## Findings
| ID | Class | Severity | Action |
|---|---|---|---|
| R1 | REVIEW_INDEPENDENCE | NON_MATERIAL | retain SAME_PRODUCER_REVIEW |
| R2 | BENCHMARK_GENERALIZATION | CONTROLLED | benchmark result != production/general competence |
| R3 | TRAJECTORY_COMPLETENESS | CONTROLLED | trace != complete causal/world-state record |
| R4 | EVALUATOR_AUTHORITY | CONTROLLED | plan/policy evaluator != scientific truth |
| R5 | EXECUTION_GAP | NON_MATERIAL | keep all benchmark runs NOT_EXECUTED |

Disposition: `RESEARCH_READY_FOR_STAGE_CLOSE`.
