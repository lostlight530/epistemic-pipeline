# Evidence Chart — K/2026-Q3

- Extraction date 2026-10-19. Variables: `tagged_object`, `release_publication_date`, `upstream_observation`, `analysis`, `independence`, `local_verification`, `unresolved`.
- Units: unique upstream versions; multiple observations of the same release would not add independent objects.

| Finding ID | Object/source | Claimed/observed upstream release change | Bounded analytic inference | Independence | Current local evidence |
|---|---|---|---|---|---|
| F1 | O1 / S1 | Programmatic Tool Calling with caller restrictions and Runner/approval integration | The model can coordinate eligible tools programmatically, enlarging the causal chain between policy, generated code, tool calls and results; allowed_callers scope is not a substitute for inspecting actions. | Same-origin publisher release | NOT_RUN / NOT_AUDITED |
| F2 | O2 / S2 | stable 2026-07-28 MCP specification revision | Protocol revision identity is a separate clock from SDK release identity and any tool-server implementation; compatibility claims require all three versions. | Same-origin publisher release | NOT_RUN / NOT_AUDITED |
| F3 | O3 / S3 | redaction of blocked tool outputs from persisted replay and RunState usage isolation | The reproducibility envelope can conflict with data minimization; redaction of rejected tool outputs changes replay observability, while checkpoint accounting defines a distinct metric boundary. | Same-origin publisher release | NOT_RUN / NOT_AUDITED |
| F4 | O4 / S4 | conditional tool approvals aligned with validated tool arguments | The arguments approved should be the same arguments whose validity was checked; a mismatch would make an approval trace ambiguous even when final execution succeeds. | Same-origin publisher release | NOT_RUN / NOT_AUDITED |

## Counterevidence matrix
- Official upstream change descriptions do not demonstrate local compatibility, scientific/benchmark truth or downstream correctness.
- A later patch/version may correct earlier behavior without proving that all older artifacts were wrong.
- No executed independent disconfirmation search or cross-version reproduction; **absence of observed contradiction is not corroboration**.

## Negative space
- No native instrumented run, precise dependency lock replay, benchmark execution or cross-version output-comparison performed for this research.
- No source-family census, systematic-scoping coverage or quantitative adoption inference.
