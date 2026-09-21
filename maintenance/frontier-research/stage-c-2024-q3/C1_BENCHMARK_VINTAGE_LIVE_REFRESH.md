# Frontier Research Part C1 — Benchmark Vintage and Live Refresh

## Identity

- Stage: `C / 2024-Q3`
- Coverage: `SEARCH_BOUNDED`
- Status: `COMPLETE`

## Question

When a benchmark deliberately replaces questions and changes task composition, what remains comparable across the same benchmark name

## Object and sources

- O1 LiveBench Q3 benchmark-vintage sequence
- S1 LiveBench changelog: https://github.com/LiveBench/LiveBench/blob/main/changelog.md
- S2 LiveBench README: https://github.com/LiveBench/LiveBench
- S3 LiveBench paper, first posted 2024-06-27, used as pre-Q3 method context: https://arxiv.org/abs/2406.19314

One source family

## Q3 observations

### 2024-07-26

LiveBench added new coding-completion/LCB-generation questions and a new spatial-reasoning task

The changelog says the total reached 1000 questions and future updates would add/remove the same number to keep 1000 total

### 2024-08-31

All three math-task sources were refreshed

Olympiad questions moved from 2023 to IMO/USAMO 2024, AMPS_Hard was changed for difficulty/ambiguity, and AMC questions were rewritten/reordered

### 2024-09-30 snapshot

The project README preserves a leaderboard snapshot “as of 30th September 2024”

This is a dated project snapshot, not evidence that question content stayed fixed through the whole quarter

## Analysis

A benchmark can preserve its name while its measurement surface changes

Therefore:

```text
LiveBench July vintage
!= LiveBench August vintage
```

even when task-family labels overlap

Comparability should be explicit:

- `COMPARABLE` when question/task/scoring vintage is materially equivalent
- `PARTIALLY_COMPARABLE` when a declared subset/aggregation remains interpretable
- `NOT_COMPARABLE` when task/question changes invalidate the intended comparison

The Stage does not compute which historical leaderboard rows satisfy each class because no row-level rerun/diff was executed

## Counterevidence

LiveBench intentionally maintains stable high-level categories and objective scoring goals

That supports continuity at benchmark-family level

It does not prove score equivalence across vintages

## Conclusion

`SUPPORTED_OBSERVATION`

Benchmark vintage is part of evidence identity whenever benchmark content is refreshed

```text
same benchmark family
!= same measurement instance
```
