# Evidence Chart — I/2026-Q1

- Extraction date 2026-10-19. Variables: `tagged_object`, `release_publication_date`, `upstream_observation`, `analysis`, `independence`, `local_verification`, `unresolved`.
- Units: unique upstream versions; multiple observations of the same release would not add independent objects.

| Finding ID | Object/source | Claimed/observed upstream release change | Bounded analytic inference | Independence | Current local evidence |
|---|---|---|---|---|---|
| F1 | O1 / S1 | nested handoff history switches to opt-in | A handoff may preserve less or more previous context based on an explicit configuration choice; a transferred agent claim must carry this delegation-history identity. | Same-origin publisher release | NOT_RUN / NOT_AUDITED |
| F2 | O2 / S2 | human-in-the-loop tool approvals, interrupts and serializable RunState resume | The approval decision and paused/resumed state become first-class trace events; a final answer no longer suffices to determine whether a sensitive tool invocation was authorized. | Same-origin publisher release | NOT_RUN / NOT_AUDITED |
| F3 | O3 / S3 | immutable tool-invocation metadata and tool context accessors on run results | Stable tool-call metadata improves identification of what was invoked, but immutable metadata alone cannot show whether a tool's external side effects succeeded. | Same-origin publisher release | NOT_RUN / NOT_AUDITED |

## Counterevidence matrix
- Official upstream change descriptions do not demonstrate local compatibility, scientific/benchmark truth or downstream correctness.
- A later patch/version may correct earlier behavior without proving that all older artifacts were wrong.
- No executed independent disconfirmation search or cross-version reproduction; **absence of observed contradiction is not corroboration**.

## Negative space
- No native instrumented run, precise dependency lock replay, benchmark execution or cross-version output-comparison performed for this research.
- No source-family census, systematic-scoping coverage or quantitative adoption inference.
