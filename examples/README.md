# Epistemic Pipeline Examples

These examples show actual repository entry points. They are not GitHub workflow instructions and do not imply scientific validation.

## Validate and run

```bash
python3 core/engine.py validate graphs/linear.yaml
python3 core/engine.py run graphs/linear.yaml
```

Graph validation is structural. The default MockProvider is a deterministic synthetic fixture, not real-model performance evidence.

## Produce the evidence bundle

```bash
python3 core/run_bundle.py graphs/linear.yaml \
  --human-review partial \
  --upstream-artifact-ref ../auto-doc-engine/output/report.artifact.json
```

Typical paths:

```text
traces/<run>.jsonl
checkpoints/<run>/checkpoint.json
provenance/<run>.prov.json
claim-audits/<run>.claim-audit.json
evidence/<run>.evidence.json
```

## Claim verification with observation basis

A bounded claim record can look like:

```json
{
  "claim_id": "c1",
  "source_refs": ["src_001"],
  "evidence_refs": ["src_001#seg_001"],
  "observation_basis": {
    "claim_identity": "structured-analyze-output",
    "evidence_refs": "structured-analyze-output",
    "consistency": "structured-verify-output",
    "conflicts": "structured-verify-output",
    "heuristic_scores": "structured-state-output",
    "basis_inferred": false
  },
  "audit_state": "structurally_checked_with_conflict"
}
```

```text
structured-verify-output != external scientific verification
```

## Dimensional claim audit coverage

The sidecar also records separate coverage dimensions:

```json
{
  "audit_coverage": {
    "counts": {
      "claims_indexed": 10,
      "claims_with_source_refs": 10,
      "claims_with_evidence_refs": 8,
      "claims_with_conflicts": 2
    },
    "ratios": {
      "evidence_refs_ratio": 0.8
    },
    "aggregate_score": null
  }
}
```

Interpretation:

```text
0.8 = 80% of indexed claims carry evidence refs
0.8 != 80% probability of truth
0.8 != provenance soundness
0.8 != evidence sufficiency
```

## Provider disclosure basis

A custom provider may describe only what it really knows:

```python
from core.llm_harness import LLMProvider

class MyProvider(LLMProvider):
    def complete(self, system, user, schema=None):
        return {"...": "structured output"}

    def describe(self):
        return {
            "provider_class": type(self).__name__,
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

Leave unknown metadata unknown. Provider metadata is not AI-text detection or output validation.

## Evidence Envelope upstream coverage

If upstream references are supplied, the Envelope can preserve resolution coverage:

```json
{
  "artifact_ref_coverage": {
    "reference_count": 2,
    "by_resolution": {
      "local-file": 1,
      "opaque-uri-not-dereferenced": 1
    },
    "local_file_ratio": 0.5,
    "aggregate_score": null
  }
}
```

This is environment/reference coverage only:

```text
local_file_ratio != source credibility
opaque URI != invalid evidence
```

## Runtime policy

```yaml
runtime_policies:
  - id: verification_coverage
    check: numeric_min
    field: coverage
    min: 0.95
```

The prose `rule` field is descriptive only. Runtime-policy success is not scientific validation.

## Score semantics

```text
0.8 heuristic score != 80% probability
converged=true != scientific certainty
```

## Reproducibility

Evidence artifacts can support traceability/replay addressing. They do not establish R3 without a separate rerun and declared comparison criterion.

## No CI assumption

These commands are local operational examples only. The repository does not require GitHub Actions, CodeQL or merge gates as part of its research architecture.
