# Source and Research-Object Register — Stage B / 2024-Q2

## Identity

- Repository: lostlight530/epistemic-pipeline
- Stage: B / 2024-Q2
- Coverage: SEARCH_BOUNDED
- Registered: 2026-09-22

## Object register

| ID | Object | Type | Q2 state/date | Identity note |
|---|---|---|---|---|
| O1 | RULER | long-context benchmark | paper 2024-04-09 | benchmark + public implementation |
| O2 | WMDP | proxy benchmark / unlearning project | correction 2024-04-23 | revised dataset/method state |
| O3 | ConStat | contamination-detection method | paper 2024-05-25 | performance-based contamination evidence |
| O4 | MMLU-Pro | harder benchmark family | paper 2024-06-03 | related to MMLU, not same score scale |
| O5 | LiveBench | live benchmark | initial public batch 2024-06-12; paper 2024-06-27 | question vintage is part of benchmark identity |

## Source register

| ID | Source | Family | Date | Authority | Limit |
|---|---|---|---|---|---|
| S1 | https://arxiv.org/abs/2404.06654 | RULER authors | 2024-04-09 | method/results | not independent rerun |
| S2 | https://github.com/NVIDIA/RULER | RULER project | mutable | implementation/config | same family as S1 |
| S3 | https://github.com/centerforaisafety/wmdp | WMDP project | 2024-04-23 update | dataset/method revision | producer source |
| S4 | https://arxiv.org/abs/2405.16281 | ConStat authors | 2024-05-25 | method/results | not exact training lineage |
| S5 | https://arxiv.org/abs/2406.01574 | MMLU-Pro authors | 2024-06-03 | method/results | no independent rerun |
| S6 | https://github.com/TIGER-AI-Lab/MMLU-Pro | MMLU-Pro project | mutable | dataset/project state | same family as S5 |
| S7 | https://github.com/LiveBench/LiveBench/blob/main/changelog.md | LiveBench project | records 2024-06 events | release/task chronology | mutable changelog |
| S8 | https://arxiv.org/abs/2406.19314 | LiveBench authors | 2024-06-27 | method/results | same research family as S7 |

## Source-family map

- SF1 RULER: S1-S2
- SF2 WMDP: S3
- SF3 ConStat: S4
- SF4 MMLU-Pro: S5-S6
- SF5 LiveBench: S7-S8

Cross-family similarity does not establish identical mechanisms

## Identity rules

    benchmark name != benchmark revision
    benchmark revision != execution
    nominal capacity != effective capability
    contamination evidence != exact hidden lineage
    live benchmark release != timeless benchmark identity
    correction != history rewrite

## Limitations

No model reruns, benchmark recomputation, contamination experiment, annotation audit, or exhaustive evaluation landscape
