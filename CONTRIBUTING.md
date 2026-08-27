# Contributing — Epistemic Pipeline

Changes should strengthen explicit research-execution semantics, evidence traceability or honest boundaries rather than merely increase module count.

## Setup

```bash
python -m pip install pyyaml
```

Existing local checks may be used when useful, but they are optional maintenance aids. They are not GitHub merge gates or scientific validation.

## Contribution principles

1. Change the smallest layer that owns the requirement.
2. Keep graph/state/provider/policy/score/trace/provenance/claim-audit/handoff concerns separate.
3. Fail explicitly for unsupported machine checks and ambiguous recovery identity.
4. Keep provider/model/version metadata unknown when it is unknown.
5. Never infer scientific truth from structural success.
6. Keep experimental modules labelled experimental until deliberately integrated.
7. Update authoritative documentation when public semantics change.

## Stable internal identifiers

Do not introduce decorative project versions such as `@1`, `@2`, `/v1`, or fake fixture/model versions.

Use stable project identifiers such as:

```text
epistemic-pipeline/engine
epistemic-pipeline/runtime-policy
epistemic-pipeline/trace
epistemic-pipeline/prov
epistemic-pipeline/claim-verification
epistemic-pipeline/evidence-envelope
```

Preserve actual external standard versions where those standards define versions.

## Claim/evidence changes

When changing claim/evidence structures:

- retain claim IDs separately from prose;
- never manufacture missing evidence refs;
- keep conflict records distinct from adjudication;
- do not turn claim audit into `verified=true`;
- update `CLAIM_AUDIT_CONTRACT.md` and examples.

## Score changes

Any new score semantics must say whether values are heuristic, empirically calibrated, probabilistic or something else. `[0,1]` alone is not evidence of probability semantics.

## Provider integrations

Real providers belong behind `LLMProvider`. Their `describe()` metadata must reflect what the integration actually knows. Do not guess model versions.

## Trace/provenance changes

OpenTelemetry naming alignment must not be described as an OTel exporter unless an exporter is actually implemented. PROV-aligned JSON must not be described as PROV-O RDF unless a real serializer exists.

## Cross-repository changes

Preferred loose handoff:

```text
auto-doc-engine/artifact-record
        ↓
epistemic-pipeline/evidence-envelope
        ↓
sci-render-kit/figure-evidence
```

References do not inherit truth or scientific validity.

## Governance boundary

Do not add GitHub Actions, CI, CodeQL, dependency bots, branch protection or merge-gate architecture as ordinary maintenance for this repository unless explicitly requested.
