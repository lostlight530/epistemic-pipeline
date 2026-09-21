# Frontier Research Part B3 — Harder and Live Evaluation

## Identity

- Stage: B / 2024-Q2
- Coverage: SEARCH_BOUNDED
- Status: COMPLETE

## Research question

How did Q2 benchmark design respond to saturation, prompt sensitivity, contamination, and benchmark aging

## Objects and sources

- O4 MMLU-Pro
- O5 LiveBench
- S5 https://arxiv.org/abs/2406.01574 — submitted 2024-06-03
- S6 https://github.com/TIGER-AI-Lab/MMLU-Pro
- S7 https://github.com/LiveBench/LiveBench/blob/main/changelog.md — initial release recorded 2024-06-12
- S8 https://arxiv.org/abs/2406.19314 — submitted 2024-06-27

## MMLU-Pro observation

MMLU-Pro expands answer choices from four to ten, removes selected trivial or noisy questions, and emphasizes more reasoning-focused items

The paper reports accuracy reductions of 16 to 33 percentage points relative to MMLU in its experiments and tests 24 prompt styles, reporting lower score sensitivity to prompt variation

## LiveBench observation

LiveBench's initial release is recorded on 2024-06-12 with 960 questions, 17 tasks, and six categories

It uses verifiable objective answers rather than LLM judges, draws questions from recent sources, and plans monthly refreshes to limit contamination

The paper was submitted 2024-06-27

The project also records a 2024-06-24 removal of a house-traversal task after answer-parsing ambiguity was found and corrected, demonstrating that a live benchmark can itself require forward correction

## Analysis

MMLU-Pro and LiveBench respond to different failure modes

    MMLU-Pro
    -> static benchmark made harder and experimentally less prompt-sensitive

    LiveBench
    -> benchmark content intentionally refreshed over time

Benchmark identity therefore becomes temporal evidence

Two LiveBench observations using different question vintages are not automatically measurements of the same object

MMLU and MMLU-Pro are related benchmark families, not interchangeable score scales

## Counterevidence

Harder does not mean more externally valid

Objective ground truth does not remove construct-selection bias

Monthly refresh limits one contamination pathway but does not prove permanent contamination immunity

LiveBench's own June task removal shows that objective scoring and live refresh do not eliminate benchmark correction

## Conclusion

SUPPORTED_OBSERVATION

By late Q2, defensible model-comparison evidence increasingly requires benchmark family, revision or vintage, task set, prompt or judge method, scoring method, and execution date
