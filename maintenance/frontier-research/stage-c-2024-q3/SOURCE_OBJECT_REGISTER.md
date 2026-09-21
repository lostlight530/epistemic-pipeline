# Source and Research-Object Register — Stage C / 2024-Q3

## Identity

- Repository: `lostlight530/epistemic-pipeline`
- Stage: `C / 2024-Q3`
- Specification: `2026-09-19-first-batch`
- Register date: `2026-09-22`
- Coverage: `SEARCH_BOUNDED`

## Identity rules

```text
benchmark family != benchmark vintage
benchmark vintage != immutable question set
judge identity != universal judge authority
judge agreement != ground truth
repository issue != confirmed defect
later refresh != rewrite of earlier score
```

## Research objects

| ID | Object | Type | Q3 state |
|---|---|---|---|
| O1 | LiveBench Q3 benchmark-vintage sequence | living benchmark | 2024-07-26 + 2024-08-31 refreshes; 2024-09-30 snapshot |
| O2 | Domain-specific evaluation-set paper | evaluator-method research | submitted 2024-08-16 |
| O3 | CodeJudge-Eval | judge benchmark | submitted 2024-08-20, revised 2024-09-16 |
| O4 | Judge/reward-model limits paper | evaluator-boundary research | submitted 2024-09-17 |
| O5 | MMLU-Redux issue #2 | project-state report | opened 2024-09-19 |

## Sources

| ID | Source | Family | Authority | Limitation |
|---|---|---|---|---|
| S1 | https://github.com/LiveBench/LiveBench/blob/main/changelog.md | LiveBench | dated benchmark refresh log | living project source |
| S2 | https://github.com/LiveBench/LiveBench | LiveBench | dated project snapshot context | same family as S1 |
| S3 | https://arxiv.org/abs/2406.19314 | LiveBench | method context | pre-Q3 paper context |
| S4 | https://arxiv.org/abs/2408.08808 | independent research team | domain-specific evaluator-set study | producer research, no local rerun |
| S5 | https://arxiv.org/abs/2408.10718 | independent research team | code-judging benchmark/method | producer research, no local rerun |
| S6 | https://arxiv.org/abs/2409.11239 | independent research team | judge/reward-model limitations | producer research, no local rerun |
| S7 | https://github.com/aryopg/mmlu-redux/issues/2 | MMLU-Redux project/community | reported configuration ambiguity | issue report, not adjudicated defect |
| S8 | https://arxiv.org/abs/2406.04127 | MMLU-Redux | project/paper context | pre-Q3 method context |

## Source-family map

- SF1: S1-S3 — LiveBench
- SF2: S4 — domain-specific evaluator-set research
- SF3: S5 — CodeJudge-Eval
- SF4: S6 — judge/reward-model limits
- SF5: S7-S8 — MMLU-Redux project/paper

No family is counted as independent reproduction of another

## Temporal register

| Object | Q3 event | Treatment |
|---|---|---|
| LiveBench | 2024-07-26 question/task expansion | new benchmark vintage |
| LiveBench | 2024-08-31 math-source refresh | new benchmark vintage |
| LiveBench | 2024-09-30 dated leaderboard snapshot | point-in-time view, not timeless state |
| MMLU-Redux | issue opened 2024-09-19 | unresolved project-state evidence |

## Runtime boundary

No benchmark rerun, judge reproduction, contamination test, dataset diff or scoring recomputation was executed
