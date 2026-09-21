# Frontier Research Stage Brief — Stage C / 2024-Q3

## Identity

- Repository: `lostlight530/epistemic-pipeline`
- Specification: `2026-09-19-first-batch`
- Stage: `C / 2024-Q3`
- Window: `2024-07-01 through 2024-09-30`
- Record type: `RETROSPECTIVE`
- Design: `HISTORICAL_FRONTIER_RECONSTRUCTION + TARGETED_EVIDENCE_SYNTHESIS + COMPARATIVE_TECHNICAL_STUDY`
- Coverage: `SEARCH_BOUNDED`
- Reconstruction date: `2026-09-22`
- Status: `COMPLETE`

## Rationale

Stage A established that a score lives inside an evidence envelope

Stage B showed that benchmark family/vintage and contamination/revision state are themselves time-varying evidence coordinates

Stage C asks what happens when the evaluator is also a bounded research object and when a benchmark intentionally changes its task set over time

The quarter is studied through LiveBench Q3 refreshes, domain-specific judge evaluation, code-judging evaluation, September evidence about LLM judges/reward models, and a repository-level MMLU-Redux configuration ambiguity report

## Hard boundaries

- `claim indexed != claim true`
- `evidence linked != evidence sufficient`
- `benchmark name != immutable benchmark state`
- `judge output != ground truth`
- `judge agreement != universal evaluator validity`
- `domain performance != cross-domain authority`
- `repository issue != confirmed dataset defect`
- `later benchmark refresh != earlier score rewrite`

## Research questions

1. **RQ1:** When benchmark refresh changes questions/tasks, when should comparisons be versioned, partially comparable or `NOT_COMPARABLE`
2. **RQ2:** How does evaluator reliability depend on task/domain and judging contract rather than evaluator/model identity alone
3. **RQ3:** Which evaluator, dataset/config and temporal identities belong in an evidence envelope so that later corrections do not silently alter earlier evaluation meaning

## Source plan

| Family | Q3 object | Use |
|---|---|---|
| LiveBench | 2024-07-26 and 2024-08-31 benchmark refreshes + 2024-09-30 snapshot | benchmark vintage/churn |
| domain-specific judge research | arXiv:2408.08808, 2024-08-16 | domain-conditioned evaluator-set construction |
| CodeJudge-Eval | arXiv:2408.10718, 2024-08-20 | judging code correctness as distinct evaluator task |
| judge/reward-model limits | arXiv:2409.11239, 2024-09-17 | evaluator applicability/limitations |
| MMLU-Redux project | issue #2, 2024-09-19 | configuration/interface ambiguity only |

## Planned Parts

- C1 Benchmark Vintage and Live Refresh
- C2 Domain-Conditioned Evaluator Authority
- C3 Evaluator and Dataset-Configuration Identity

## Appraisal

Primary project/paper sources establish their own methods/results and project state

They do not establish independent reproduction unless a separate execution is present

## Amendments

`NONE`

## Completion

Three Parts + July/August/September reconstructions + register/chart + synthesis + review + handoff + longitudinal placement
