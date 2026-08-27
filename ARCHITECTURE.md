# Architecture — Epistemic Pipeline

> Calibrated 2026-08-28. This document describes implemented runtime semantics and research-integrity boundaries. It does not define GitHub platform governance.

## Architectural thesis

Research execution is modeled as an **evidence-bearing state-transition system**. The repository separates dependency structure, provider execution, runtime-policy predicates, claim/evidence/conflict structures, heuristic scores, recovery identity, tracing, provenance, claim-level verification observations, assertion basis, dimensional audit coverage and cross-tool handoff.

A single “agent success” flag would collapse materially different properties, so the architecture does not use one as a scientific claim.

## Canonical runtime and evidence path

```text
graph YAML
  ↓
DependencyGraph
  ↓
StateMachineEngine
  ↓
LLMHarness / injected provider
  ↓
RuntimePolicyEvaluator
  ↓
ConfidenceNetwork where configured
  ↓
RunTracer + checkpoint
  ↓
PROV-aligned lineage
  ↓
claim-verification
    ├─ assertion / observation basis
    └─ dimensional claim audit coverage
  ↓
evidence-envelope
    ├─ upstream-reference coverage
    └─ compact cross-tool handoff
```

`discover -> analyze -> verify -> synthesize -> archive` is the default semantic progression; executable ordering comes from graph dependencies.

## Stable project identifiers

```text
epistemic-pipeline/engine
epistemic-pipeline/runtime-policy
epistemic-pipeline/trace
epistemic-pipeline/checkpoint
epistemic-pipeline/prov
epistemic-pipeline/confidence-heuristic
epistemic-pipeline/network-input
epistemic-pipeline/claim-index
epistemic-pipeline/claim-verification
epistemic-pipeline/process-disclosure
epistemic-pipeline/upstream-reference
epistemic-pipeline/evidence-envelope
epistemic-pipeline/reference-rules
```

Internal project identifiers are unversioned; real external standard/runtime versions remain explicit when genuinely applicable.

## Dependency graph

`core/dependency_graph.py` validates duplicate IDs, missing dependencies, cycles and reachability, then produces deterministic topological ordering / parallel groups.

```text
graph validity != research validity
```

## Provider boundary and assertion basis

`LLMProvider` is a provider-neutral structured-output interface. The repository ships only `MockProvider` as a deterministic synthetic fixture.

Day 5 makes provider metadata provenance explicit:

```text
injected provider describe() -> provider-adapter-reported
MockProvider                -> synthetic-fixture-runtime
no provider configured      -> runtime-harness-state
```

Unknown model/version fields remain `null`.

```text
provider-adapter-reported != vendor certification
provider identity != output validity
provider metadata != AI-text detection
```

The provider path records `automatic_ai_detection_used: false`; it does not infer AI authorship/use from output prose.

## Runtime policy

`RuntimePolicyEvaluator` executes only explicit machine-readable checks. Human `rule` descriptions are documentation, not code. Historical Gatekeeper naming remains compatibility-only.

```text
runtime-policy success != scientific validity
runtime-policy success != evidence credibility
```

## Score layer

`ConfidenceNetwork` performs bounded weighted heuristic propagation. `core/calibration.py` provides a monotone transform, not empirical probability calibration without separate labelled fitting/evaluation.

```text
score in [0,1] != calibrated probability
convergence != certainty
score change != Bayesian update
```

## Trace and checkpoint

`RunTracer` writes project JSONL with internal SHA-256 linkage. Selected OpenTelemetry GenAI names may be borrowed where semantically appropriate, but this is not an OTel exporter or span-conformance claim.

Checkpoint graph identity protects bounded resume from mismatched graph definitions. It cannot guarantee deterministic replay of external providers/tools.

## PROV-aligned lineage

`core/provenance.py` emits payload-minimizing project JSON using PROV concepts. It is not PROV-O RDF serialization or complete standards conformance.

```text
lineage != truth
hash identity != semantic equivalence
```

## Claim-verification architecture

`core/claim_audit.py` separates:

```text
claim identity
source refs
evidence refs / relations
internal consistency observation
cross-source observation
conflicts
initial heuristic score
final heuristic score
audit state
assertion / observation basis
```

Audit states remain descriptive:

```text
indexed_only
evidence_bound
structurally_checked
conflict_recorded
structurally_checked_with_conflict
```

No `verified=true`, accepted/rejected scientific verdict or truth label is emitted.

## Claim assertion / observation basis

Day 5 adds explicit bases:

| Surface | Basis |
|---|---|
| claim/source/evidence refs | `structured-analyze-output` |
| consistency observations | `structured-verify-output` |
| conflicts | `structured-verify-output` |
| heuristic scores | `structured-state-output` |
| provider metadata | provider-adapter / fixture runtime |
| human review | caller-declared when supplied |

This is provenance of the recorded assertion/observation, not external validation.

```text
assertion basis != correctness
structured-verify-output != scientific verification
```

## Dimensional claim audit coverage

`claim-verification` computes separate counts and ratios over indexed claims for:

```text
source refs
evidence refs
internal consistency observations
cross-source observations
conflicts
initial heuristic scores
final heuristic scores
```

No aggregate quality score is computed:

```json
{"aggregate_score": null}
```

```text
coverage != scientific validity
coverage ratio != probability
coverage != provenance soundness
```

Current claim-level auditability research motivates separating coverage from soundness; this repository implements coverage only where its own structured artifacts support it.

## Evidence Envelope

The Evidence Envelope references graph, trace, checkpoint, provenance, claim audit/index, process disclosure and optional upstream artifact/evidence refs.

Day 5 adds reference-resolution coverage:

```text
reference_count
by_resolution
local_file_ratio
aggregate_score: null
```

A local-file ratio indicates local resolvability/hashing at envelope generation time, not source credibility or evidence quality.

The Envelope stays compact and does not duplicate claim-verification payloads.

## Evidence stack

```text
Trace             -> chronology
Checkpoint        -> recovery state
PROV lineage      -> derivation relationships
Claim verification-> per-claim observations/basis/coverage
Evidence Envelope -> compact cross-tool index
```

These artifacts are complementary, not interchangeable proof objects.

## Cross-repository architecture

```text
auto-doc-engine
  artifact-record + assertion basis + artifact coverage
        ↓
epistemic-pipeline
  claim-verification + audit coverage + evidence-envelope
        ↓
sci-render-kit
  figure-claim-audit + communication coverage + figure-evidence
```

Repositories are loosely coupled through references, not imports or inherited scientific validity.

## Reproducibility

```text
R0 traceable
R1 replay-addressable
R2 environment-bounded
R3 actual separate rerun + declared comparison
```

Evidence sidecars support bookkeeping; they do not self-award R3.

## Five-day global calibration

The 2026-08-24 → 2026-08-28 architecture is informed by re-openable autonomous-science provenance, transparent AI use/human oversight, artifact-centered claim-aware observability, trajectory-to-evidence qualification, Brain Researcher evidence-bounded claims, EarthVerse end-to-end consistency gaps and claim-level auditability work separating provenance coverage, soundness, contradiction transparency and audit effort.

Borrowed: explicit audit objects, dimensional coverage, assertion provenance, contradiction visibility and evidence-bounded qualification.

Not claimed: provenance soundness, scientific-review authority, citation correctness, calibrated truth probability or peer review.

## Non-goals

- scientific truth adjudication;
- external citation-content verification by itself;
- provenance soundness validation;
- calibrated probabilities by default;
- automatic AI-text detection;
- automatic peer review;
- tamper-proof external ledger;
- PROV-O RDF serialization;
- built-in production LLM providers;
- GitHub CI/merge governance.

## Hard invariants

```text
Assertion basis != correctness
Audit coverage != scientific validity
Coverage ratio != probability
Evidence ref != evidence sufficiency
Conflict absent != corroboration
Provider identity != output validity
Human review != peer review
Runtime-policy pass != scientific validation
Convergence != certainty
Provenance != truth
```

## Maintenance rule

When code and docs disagree, correct the implementation/documentation explicitly. New capability claims require a real code path or a clear planned/experimental label. GitHub Actions, CI, CodeQL, dependency bots and merge gates remain outside the research architecture.
