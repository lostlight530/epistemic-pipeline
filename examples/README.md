# Epistemic Pipeline Examples

These examples show actual repository entry points. They are not GitHub workflow instructions and do not imply scientific validation.

## 1. Validate an executable graph

```bash
python3 core/engine.py validate graphs/linear.yaml
```

Validation checks graph structure such as dependencies/cycles/reachability. A valid graph is not a scientifically valid study.

## 2. Run the state machine

```bash
python3 core/engine.py run graphs/linear.yaml
```

The default provider path is `MockProvider`, a deterministic synthetic fixture. It is not evidence of real-model performance.

## 3. Produce the full evidence bundle

```bash
python3 core/run_bundle.py graphs/linear.yaml
```

Typical generated paths:

```text
traces/<run>.jsonl
checkpoints/<run>/checkpoint.json
provenance/<run>.prov.json
claim-audits/<run>.claim-audit.json
evidence/<run>.evidence.json
```

Stable internal profiles:

```text
epistemic-pipeline/trace
epistemic-pipeline/checkpoint
epistemic-pipeline/prov
epistemic-pipeline/claim-verification
epistemic-pipeline/evidence-envelope
```

## 4. Declare human-review context

```bash
python3 core/run_bundle.py graphs/linear.yaml \
  --human-review partial
```

`partial` records declared review context only. It does not mean peer review or scientific validation.

## 5. Link an upstream Auto Doc artifact

```bash
python3 core/run_bundle.py graphs/linear.yaml \
  --upstream-artifact-ref ../auto-doc-engine/output/report.artifact.json
```

If the path exists locally, the Evidence Envelope records its SHA-256. Otherwise an opaque ref is retained without dereferencing.

Preferred upstream profile:

```text
auto-doc-engine/artifact-record
```

## 6. Add upstream evidence/provenance references

```bash
python3 core/run_bundle.py graphs/linear.yaml \
  --upstream-evidence-ref ./inputs/source-evidence.json \
  --upstream-evidence-ref urn:example:external-record
```

Opaque URIs remain references; the repository does not fetch or certify them.

## 7. Inspect claim verification

A claim-audit record separates dimensions such as:

```json
{
  "claim_id": "c1",
  "evidence_refs": ["src_001#seg_001"],
  "audit_state": "structurally_checked_with_conflict",
  "heuristic_scores": {
    "initial": {"value": 0.5, "stage": "verify"},
    "final": {"value": 0.5, "stage": "synthesize"}
  }
}
```

This does **not** mean the claim is scientifically verified.

## 8. Runtime policy

State files use machine-readable checks. Example structure:

```yaml
runtime_policies:
  - id: verification_coverage
    check: numeric_min
    field: coverage
    min: 0.95
```

The prose `rule` field is descriptive only.

## 9. Provider integration sketch

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
        }
```

Leave unknown metadata unknown rather than guessing.

## 10. Score semantics

A score-network output in `[0,1]` remains heuristic:

```text
0.8 != 80% probability
converged=true != scientific certainty
```

## 11. Reproducibility

Evidence artifacts can make a run traceable/replay-addressable. They do not establish R3 without a separate rerun and declared comparison criterion.

## 12. No CI assumption

These commands are local operational examples only. The repository does not require GitHub Actions, CodeQL or merge gates as part of its research architecture.
