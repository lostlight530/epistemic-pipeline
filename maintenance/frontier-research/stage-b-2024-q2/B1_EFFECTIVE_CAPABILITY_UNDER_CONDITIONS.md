# Frontier Research Part B1 — Effective Capability Under Conditions

## Identity

- Stage: B / 2024-Q2
- Coverage: SEARCH_BOUNDED
- Status: COMPLETE

## Research question

How should nominal capability claims be represented when performance changes with context length and task complexity

## Object and sources

- O1 RULER
- S1 https://arxiv.org/abs/2404.06654 — submitted 2024-04-09
- S2 https://github.com/NVIDIA/RULER — public benchmark implementation

## Observation

RULER expands vanilla needle-in-a-haystack retrieval with configurable sequence length, multiple-needle variants, multi-hop tracing, and aggregation tasks

The paper evaluates 17 long-context models over 13 tasks and reports large degradation for almost all models as context length increases

Although the selected models claimed context sizes of at least 32K, only about half maintained the paper's satisfactory-performance criterion at 32K

The project also states that RULER is not comprehensive and should not replace realistic long-context tasks

## Analysis

RULER separates at least three states

    declared maximum context
    != accepted benchmark input length
    != effective task performance at that length

A capability observation therefore needs its task family, input length, task complexity, threshold, model revision, and execution context

## Counterevidence and limits

Synthetic tasks provide control but do not establish one universal effective-context number for every real workload

No RULER model execution was rerun in this Stage

## Repository relation

PARALLEL_CONVERGENCE

Stage A's evidence-envelope model is strengthened because condition coverage belongs inside the claim/evidence relation

## Conclusion

SUPPORTED_OBSERVATION

Nominal context capacity is interface/model metadata while effective capability is an observation bounded to tested tasks and conditions
