# Customization Guide — Epistemic Pipeline

## 1. Choose the smallest owning layer

The repository separates:

```text
graph topology
state definition
provider execution
provider disclosure
runtime policy
bounded score propagation
retry/timeout
trace
checkpoint identity
PROV-aligned lineage
claim verification
evidence handoff
```

Extend the smallest layer that actually owns the requirement.

## 2. Custom graph

Add a graph under `graphs/` when the change is about dependency topology. Graph nodes must remain uniquely identifiable and dependency-valid.

Do not encode scientific truth in topology labels.

## 3. Custom state behavior

State semantics live in `states/*.yaml`. Runtime constraints use machine-readable `runtime_policies` checks. Human-readable rule prose is descriptive only.

If a desired check does not exist, implement it explicitly in `RuntimePolicyEvaluator`; do not pretend prose is executable.

## 4. Custom provider

Implement `LLMProvider.complete(...)` and optionally `describe()`.

`describe()` should return only known process metadata:

```python
{
    "provider_class": "...",
    "provider": "...",   # or None
    "model": "...",      # or None
    "version": None,      # remain None when unknown
    "mode": "injected_provider",
    "external_model_call": True,
}
```

Do not infer vendor/model/version metadata from prompts or class names.

## 5. Custom runtime policy

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

## 6. Custom score network

`ConfidenceNetwork` is heuristic. If you replace or extend it, document the mathematical semantics explicitly.

Do not call a score a probability unless a real probabilistic/calibration model and empirical evidence justify that interpretation.

## 7. Custom claim verification

`core/claim_audit.py` aggregates already-emitted claim/evidence/verification structures into an audit sidecar.

A new claim audit field should answer an inspectable question such as:

```text
what source/evidence ref was declared?
what structural observation was recorded?
what conflict was recorded?
what score observation existed at which stage?
```

Do not introduce a universal truth/verdict field merely for convenience.

Stable profile:

```text
epistemic-pipeline/claim-verification
```

## 8. Custom evidence handoff

`core/evidence_envelope.py` should remain a compact index. Prefer adding references to separately inspectable artifacts instead of embedding full copies.

Stable profile:

```text
epistemic-pipeline/evidence-envelope
```

Local reference files can be hashed. Opaque/URI refs should stay unresolved unless a future explicit resolver is implemented.

## 9. Trace customization

Project trace fields may borrow applicable OpenTelemetry GenAI names, but do not claim OTel exporter/span compliance unless that integration is actually implemented.

Stable project trace profile:

```text
epistemic-pipeline/trace
```

## 10. Provenance customization

Current provenance is project JSON aligned with W3C PROV concepts. A future PROV-O/RDF export should be introduced as an actual serializer, not by renaming the current JSON.

## 11. Cross-repository handoff

Upstream artifact refs can point to:

```text
auto-doc-engine/artifact-record
```

Downstream figures can consume references to:

```text
epistemic-pipeline/claim-verification
epistemic-pipeline/evidence-envelope
```

No repository needs to import another repository's Python package to use these references.

## 12. Internal identifier rule

Project-owned profile names are stable and unversioned. Do not add `@1/@2`, `/v1`, or synthetic provider/fixture versions. External standard versions remain explicit where real standards define them.

## 13. Experimental work

Experimental modules can be refined independently, but they do not become canonical capabilities merely because they compile or have documentation.

## 14. Governance

Do not wire customization through GitHub Actions/CI/merge gates as part of the research architecture unless explicitly requested. Local validation remains a caller/maintainer choice.
