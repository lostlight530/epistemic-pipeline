# Evidence Chart — J/2026-Q2

- Extraction date 2026-10-19. Variables: `tagged_object`, `release_publication_date`, `upstream_observation`, `analysis`, `independence`, `local_verification`, `unresolved`.
- Units: unique upstream versions; multiple observations of the same release would not add independent objects.

| Finding ID | Object/source | Claimed/observed upstream release change | Bounded analytic inference | Independence | Current local evidence |
|---|---|---|---|---|---|
| F1 | O1 / S1 | beta Sandbox Agents with manifests, mounts, snapshots, session resume and persisted workspace memory | Execution context is more than a prompt: manifest, mounted resources, sandbox provider, saved state and memory govern which files/actions an agent can encounter. | Same-origin publisher release | NOT_RUN / NOT_AUDITED |
| F2 | O2 / S2 | ModelRefusalError surfaces refusal as explicit SDK state | A refusal should be represented as an epistemically distinct outcome rather than empty output or repeated retries; the evaluator should not grade it as an ordinary answer. | Same-origin publisher release | NOT_RUN / NOT_AUDITED |
| F3 | O3 / S3 | pre-approval tool input guardrails | Guardrail evaluation before human approval gives validation and authorization distinct temporal positions; a later approval must be interpreted against validated inputs. | Same-origin publisher release | NOT_RUN / NOT_AUDITED |

## Counterevidence matrix
- Official upstream change descriptions do not demonstrate local compatibility, scientific/benchmark truth or downstream correctness.
- A later patch/version may correct earlier behavior without proving that all older artifacts were wrong.
- No executed independent disconfirmation search or cross-version reproduction; **absence of observed contradiction is not corroboration**.

## Negative space
- No native instrumented run, precise dependency lock replay, benchmark execution or cross-version output-comparison performed for this research.
- No source-family census, systematic-scoping coverage or quantitative adoption inference.
