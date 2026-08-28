# Customization Guide — Epistemic Pipeline

## Choose the smallest owning layer

The repository separates graph topology, state definition, provider execution/disclosure, runtime policy, bounded score propagation, retry/timeout, trace, checkpoint identity, PROV-aligned lineage, claim verification, assertion basis, audit coverage and evidence handoff.

Extend only the smallest layer that owns the requirement.

## Custom graph

Add graph topology under `graphs/`. Keep IDs unique and dependencies valid. Do not encode scientific truth in graph labels.

## Custom state behavior

State semantics live in `states/*.yaml`. Runtime constraints use machine-readable `runtime_policies`. Human-readable prose is descriptive only.

## Custom provider

Implement `LLMProvider.complete(...)` and optionally `describe()`.

A truthful description can look like:

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

Do not infer vendor/model/version from prompts, class names, writing style or marketing copy.

## Custom runtime policy

Supported checks currently include:

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

Unknown checks fail explicitly.

## Custom score network

`ConfidenceNetwork` is heuristic. If extended, document mathematical semantics explicitly. Do not call a score a probability without a genuine probabilistic/calibration model and empirical evidence.

## Custom claim verification

`core/claim_audit.py` aggregates already-emitted structures into a claim-audit sidecar.

A new field should answer an inspectable question and declare its observation basis:

```text
what value/relationship was recorded?
which state/provider/caller produced that observation?
```

Useful bases include:

```text
structured-analyze-output
structured-verify-output
structured-state-output
provider-adapter-reported
caller-declared
```

Do not introduce a universal truth/verdict field.

## Custom audit coverage

Coverage should remain a set of transparent counts/ratios over known denominators. Example:

```text
claims_with_evidence_refs / claims_indexed
```

Never silently convert it to provenance soundness, evidence sufficiency, probability or aggregate research quality.

```json
{"aggregate_score": null}
```

If a future composite metric is desired, it requires an explicit validated evaluation design rather than arbitrary weights.

## Custom evidence handoff

`core/evidence_envelope.py` should remain a compact index. Prefer references to separately inspectable artifacts instead of embedding full copies.

For upstream-reference coverage, local-file resolution is only an environment observation:

```text
local resolution != source credibility
opaque reference != invalid evidence
```

## Trace customization

Project trace fields may borrow applicable OpenTelemetry GenAI names, but do not claim OTel exporter/span compliance unless that integration is actually implemented.

## Provenance customization

Current provenance is project JSON aligned with W3C PROV concepts. A future PROV-O/RDF export must be an actual serializer, not a renamed current JSON object.

## Cross-repository handoff

```text
auto-doc-engine/artifact-record
        ↓
epistemic-pipeline/claim-verification
epistemic-pipeline/evidence-envelope
        ↓
sci-render-kit/figure-claim-audit
sci-render-kit/figure-evidence
```

No direct package imports are required.

## Internal identifier rule

Project-owned identifiers are stable and unversioned. Do not add `@1/@2`, `/v1`, or synthetic provider/fixture versions. External standard/runtime versions remain explicit when real.

## Experimental work

Experimental modules remain outside canonical capabilities until deliberately integrated and documented.

## Governance

Do not wire customization through GitHub Actions/CI/merge gates as part of the research architecture unless explicitly requested. Local validation remains a maintainer choice and is not scientific validation.
