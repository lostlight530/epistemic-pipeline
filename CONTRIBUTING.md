# Contributing — Epistemic Pipeline

Changes should strengthen explicit research-execution semantics, evidence traceability or honest boundaries rather than merely increase module count.

## Contribution principles

1. Change the smallest layer that owns the requirement.
2. Keep graph/state/provider/policy/score/trace/provenance/claim-audit/handoff concerns separate.
3. Fail explicitly for unsupported machine checks and ambiguous recovery identity.
4. Keep provider/model/version metadata unknown when unknown; preserve assertion basis for metadata that is known.
5. Never infer scientific truth from structural success.
6. Keep experimental modules experimental until deliberately integrated.
7. Update authoritative documentation when public semantics change.

## Stable internal identifiers

Do not introduce decorative project versions such as `@1`, `@2`, `/v1`, or fake fixture/model versions. Preserve actual external standard/runtime versions when those are real.

## Claim/evidence changes

When changing claim/evidence structures:

- retain claim IDs separately from prose;
- never manufacture missing evidence refs;
- keep conflict records distinct from adjudication;
- do not turn claim audit into `verified=true`;
- preserve assertion/observation basis for new audit fields;
- keep coverage dimensional; do not create an aggregate research-quality score;
- update `CLAIM_AUDIT_CONTRACT.md`, `ASSERTION_BASIS_AND_AUDIT_COVERAGE.md`, Manifest and examples.

## Assertion-basis rule

A new audit field should answer both:

```text
What value is recorded?
How did this repository obtain that value?
```

If the basis is only a provider report or caller declaration, say so. Do not upgrade it to vendor authentication, external verification or scientific truth.

## Coverage rule

```text
coverage != provenance soundness
coverage != scientific validity
coverage ratio != probability
```

The current repository has no validated weighting regime for a composite audit-quality score, so `aggregate_score` remains `null`.

## Score changes

Any new score semantics must state whether values are heuristic, empirically calibrated, probabilistic or something else. `[0,1]` alone is not evidence of probability semantics.

## Provider integrations

Real providers belong behind `LLMProvider`. Their `describe()` metadata must reflect what the integration actually knows and include a truthful assertion basis. Do not guess model versions or infer AI authorship/use from prose.

## Trace/provenance changes

OpenTelemetry naming alignment must not be described as an OTel exporter unless implemented. PROV-aligned JSON must not be described as PROV-O RDF unless a real serializer exists.

## Cross-repository changes

```text
auto-doc-engine/artifact-record
        ↓
epistemic-pipeline/claim-verification
        ↓
epistemic-pipeline/evidence-envelope
        ↓
sci-render-kit/figure-claim-audit
sci-render-kit/figure-evidence
```

References do not inherit truth or scientific validity.

## Governance boundary

Local checks may be used manually. Do not add GitHub Actions, CI, CodeQL, dependency bots, branch protection or merge-gate architecture as ordinary maintenance unless explicitly requested.
