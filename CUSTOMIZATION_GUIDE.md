# Customization Guide — Epistemic Pipeline

**Calibrated:** 2026-08-31

## Choose the smallest owning layer

The repository separates graph topology, state definition, provider execution/disclosure, runtime policy, bounded score propagation, retry/timeout, trace, checkpoint identity, PROV-aligned lineage, claim verification, claim transfer, assertion basis, audit coverage, evidence handoff, and maintenance/document governance

Extend only the smallest layer that owns the requirement

Before broad changes, read `DOCUMENT_STATUS.md` so historical snapshots are not mistaken for current extension contracts

## Custom graph

Add graph topology under `graphs/`

Keep IDs unique and dependencies valid

Do not encode scientific truth in graph labels

## Custom state behavior

State semantics live in `states/*.yaml`

Runtime constraints use machine-readable `runtime_policies`

Human-readable prose is descriptive only

## Custom provider

Implement `LLMProvider.complete(...)` and optionally `describe()`

A truthful description can look like

```python
{
    "provider_class": "MyProvider",
    "provider": "known-provider-or-none",
    "model": None,
    "version": None,
    "mode": "injected_provider",
    "external_model_call": True,
    "assertion_basis": "provider-adapter-reported",
    "basis_inferred": False,
    "automatic_ai_detection_used": False,
}
```

Do not infer vendor/model/version from prompts, class names, writing style, or marketing copy

## Custom runtime policy

Supported checks currently include

```text
min_items
non_empty
every_item_fields
claim_evidence_ratio
numeric_min
numeric_max_exclusive
conflicts_have_fields
mapping_required_keys
```

Unknown checks fail explicitly

## Custom score network

`ConfidenceNetwork` is heuristic

If extended, document mathematical semantics explicitly

Do not call a score a probability without a genuine probabilistic/calibration model and empirical evidence

## Custom claim verification

`core/claim_audit.py` aggregates already-emitted structures into a claim-audit sidecar

A new field should answer an inspectable question and declare its observation basis

```text
what value/relationship was recorded
which state/provider/caller produced that observation
```

Useful bases include

```text
structured-analyze-output
structured-verify-output
structured-state-output
provider-adapter-reported
caller-declared
```

Do not introduce a universal truth/verdict field

## Custom claim transfer

`core/claim_transfer.py` creates a bounded view over an existing `epistemic-pipeline/claim-verification` sidecar

If extended

- require the expected source profile
- fail explicitly when a requested claim ID does not exist
- preserve conflicts and original audit state
- retain heuristic score non-probability semantics
- keep scientific-validity/evidence-sufficiency/peer-review inheritance false
- do not ask a model to reinterpret copied records merely to generate the transfer

```text
transfer != acceptance
copied context != independent reverification
```

## Custom audit coverage

Coverage remains transparent counts/ratios over known denominators

Example

```text
claims_with_evidence_refs / claims_indexed
```

Never silently convert coverage to provenance soundness, evidence sufficiency, probability, or aggregate research quality

```json
{"aggregate_score": null}
```

If a future composite metric is desired, it requires an explicit validated evaluation design rather than arbitrary weights

## Custom evidence handoff

`core/evidence_envelope.py` should remain a compact index

Prefer references to separately inspectable artifacts instead of embedding full copies

For upstream-reference coverage, local-file resolution is only an environment observation

```text
local resolution != source credibility
opaque reference != invalid evidence
```

## Trace customization

Project trace fields may borrow applicable OpenTelemetry GenAI names, but do not claim OTel exporter/span compliance unless that integration is actually implemented

## Provenance customization

Current provenance is project JSON aligned with W3C PROV concepts

A future PROV-O/RDF export must be an actual serializer, not a renamed current JSON object

## Maintenance customization

Maintenance configuration lives in `maintenance/cadence.yaml`

The scanner in `core/maintenance_cadence.py` is intentionally read-only

If extending it

- keep calendar-month status date-derived
- keep research-stage status config-derived
- preserve current-vs-historical document roles from `DOCUMENT_STATUS.md`
- report findings rather than automatically deleting/re-writing files
- do not make scanner success a scientific-validity or provenance-soundness claim
- do not introduce GitHub Actions/CI/merge gates as hidden scheduling infrastructure

Current closed stage

```text
window: 2026-08-24 -> 2026-08-31
calendar_month: calendar-month-close
stage: closed
```

## Cross-repository handoff

```text
auto-doc-engine/artifact-record
auto-doc-engine/artifact-lineage
        ↓
epistemic-pipeline/claim-verification
epistemic-pipeline/claim-transfer
epistemic-pipeline/evidence-envelope
        ↓
sci-render-kit/figure-claim-audit
sci-render-kit/figure-evidence
sci-render-kit/communication-transfer
```

No direct package imports are required and no scientific validity is inherited by reference

## Internal identifier rule

Project-owned identifiers are stable and unversioned

Do not add `@1/@2`, `/v1`, or synthetic provider/fixture versions

External standard/runtime versions remain explicit when real

## Experimental work

Experimental modules remain outside canonical capabilities until deliberately integrated and documented

## Document/history rule

Historical `FOUR_DAY_CONSOLIDATION.md`, `FIVE_DAY_CONSOLIDATION.md`, and `SIX_DAY_CONSOLIDATION.md` are not extension templates for current behavior

Use current contracts instead

## Governance

Do not wire customization through GitHub Actions/CI/merge gates as part of the research architecture unless explicitly requested

Local/manual validation remains a maintainer choice and is not scientific validation
