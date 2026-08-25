# Claim-aware Audit Contract — epistemic-pipeline

**Calibration:** 2026-08-26  
**Status:** implemented companion contract for `epistemic-pipeline/evidence-envelope@2`  
**Scope:** claim identity, evidence references, provider-process disclosure, human-review declaration, and privacy-minimizing handoff

## 1. Problem

A run-level trace can answer when operations happened, but scientific auditing often needs another layer:

```text
Which claim was produced?
Which source/evidence references were attached to it?
Which run/provider path produced the surrounding outputs?
Was human review declared?
Can downstream tools inspect those relationships without copying all model payloads?
```

`evidence-envelope@2` adds that layer while keeping full claim prose and node payloads outside the envelope.

## 2. Claim index

The run bundle scans structured node outputs for:

```text
claims_registry
evidence_chains
```

and emits a compact `claim_observability` section using profile:

```text
epistemic-pipeline/claim-index@1
```

Each indexed claim can carry:

```text
claim_id
state_id
claim_record_sha256
source_refs[]
evidence_refs[]
relations[]
```

The hash identifies the canonical structured claim record observed in the run. The envelope intentionally does **not** embed claim text.

### Boundary

```text
claim index != truth graph
claim hash != semantic truth
source ref != source credibility
attached evidence != sufficient evidence
relation label != verified entailment
```

The index exists for discoverability, audit, and cross-tool handoff.

## 3. Provider disclosure

`LLMProvider.describe()` is an optional provider hook. The base implementation only knows the Python provider class and leaves vendor/model/version unset.

An external integration may override it to declare fields such as:

```json
{
  "provider_class": "ExampleProvider",
  "provider": "example-vendor",
  "model": "example-model",
  "version": "deployment-or-model-version",
  "mode": "injected_provider",
  "external_model_call": true
}
```

Unknown fields should remain unknown rather than being guessed.

The built-in `MockProvider` explicitly declares itself as a deterministic synthetic fixture with `external_model_call: false`.

### Boundary

```text
provider identity != output authenticity proof
model name != model capability proof
version label != reproducibility
provider metadata != scientific validity
```

## 4. Human-review declaration

`core/run_bundle.py` accepts:

```bash
--human-review reviewed|partial|not_reviewed|not_declared
```

This value is copied into the Evidence Envelope process disclosure.

It describes only the declared review state of the run/artifact handoff.

```text
human review != peer review
human review != expert validation
human review != factual correctness
human review != journal acceptance
```

The default is `not_declared` so the repository never infers oversight that was not explicitly supplied.

## 5. Evidence Envelope v2

`epistemic-pipeline/evidence-envelope@2` keeps the existing graph/artifact/integrity/reproducibility fields and adds:

```text
claim_observability
process_disclosure
```

The envelope remains payload-minimizing:

```text
payloads_embedded: false
claim_observability.payload_text_embedded: false
```

This design allows a downstream system such as `sci-render-kit` to bind a figure to claim IDs without forcing the entire provider transcript or scientific payload into the figure package.

## 6. Why this exists now

Three 2026 signals converge on the same engineering requirement:

1. **Artifact-centered Claim-aware Observability for Autonomous Scientific Agents** argues that logging model calls is insufficient and proposes portable claim/artifact lineage as an audit layer complementary to telemetry and standards such as PROV-O and RO-Crate.
2. **EarthVerse** evaluates scientific agents on package-scoped investigations and finds a substantial gap between completing individual answer units and maintaining an end-to-end consistent chain across evidence, scales, units, calculations, and physical interpretation.
3. Nature Computational Science's August 2026 editorial position emphasizes transparency, accountability, and human oversight as AI becomes embedded across research and publishing.

These sources motivate the audit surface. They do not define or certify this project's profile.

## 7. Relation to existing layers

```text
OpenTelemetry-like trace names
    -> operation/runtime observability

W3C PROV-aligned project JSON
    -> entity/activity/agent lineage

claim-index@1
    -> claim/source/evidence discoverability

process-disclosure@1
    -> provider + declared human-review context

Evidence Envelope @2
    -> portable cross-tool handoff
```

No single layer substitutes for the others.

## 8. References

- https://arxiv.org/abs/2608.18312
- https://arxiv.org/abs/2608.23525
- https://www.nature.com/articles/s43588-026-01043-4
- https://www.nature.com/articles/s43588-026-01035-4
- https://www.w3.org/TR/prov-overview/
