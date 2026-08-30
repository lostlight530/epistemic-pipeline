# Architecture — Epistemic Pipeline

> Calibrated 2026-08-31. This document describes implemented runtime semantics, evidence-transfer boundaries, maintenance/document governance, and research-integrity constraints. It does not define GitHub platform governance.

## Architectural thesis

Research execution is modeled as an **evidence-bearing state-transition system**. The repository separates dependency structure, provider execution, runtime-policy predicates, claim/evidence/conflict structures, heuristic scores, recovery identity, tracing, provenance, claim-level verification observations, claim transfer, assertion basis, dimensional audit coverage, compact handoff, and maintenance evidence

A single agent-success flag would collapse materially different properties, so the architecture does not use one as a scientific claim

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
optional claim-transfer
    ├─ selected portable claim context
    ├─ conflicts preserved
    └─ explicit non-inheritance constraints
  ↓
evidence-envelope
    ├─ upstream-reference coverage
    └─ compact cross-tool handoff

repository state
  ↓
daily / weekly / monthly maintenance
    ├─ current-document authority
    ├─ evidence-stack reconciliation
    ├─ calendar / stage status
    └─ optional canonical SHA-256 baseline
```

`discover -> analyze -> verify -> synthesize -> archive` is the default semantic progression; executable ordering comes from graph dependencies

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
epistemic-pipeline/claim-transfer
epistemic-pipeline/process-disclosure
epistemic-pipeline/upstream-reference
epistemic-pipeline/evidence-envelope
epistemic-pipeline/reference-rules
epistemic-pipeline/maintenance-cadence
epistemic-pipeline/maintenance-report
```

Internal project identifiers are unversioned; real external standard/runtime versions remain explicit when genuinely applicable

## Dependency graph

`core/dependency_graph.py` validates duplicate IDs, missing dependencies, cycles, and reachability, then produces deterministic topological ordering / parallel groups

```text
graph validity != research validity
```

## Provider boundary and assertion basis

`LLMProvider` is a provider-neutral structured-output interface. The repository ships only `MockProvider` as a deterministic synthetic fixture

Provider metadata provenance is explicit

```text
injected provider describe() -> provider-adapter-reported
MockProvider                -> synthetic-fixture-runtime
no provider configured      -> runtime-harness-state
```

Unknown model/version fields remain `null`

```text
provider-adapter-reported != vendor certification
provider identity != output validity
provider metadata != AI-text detection
```

The provider path records `automatic_ai_detection_used: false`; it does not infer AI authorship/use from output prose

## Runtime policy

`RuntimePolicyEvaluator` executes only explicit machine-readable checks. Human `rule` descriptions are documentation, not code. Historical Gatekeeper naming remains compatibility-only

```text
runtime-policy success != scientific validity
runtime-policy success != evidence credibility
```

## Score layer

`ConfidenceNetwork` performs bounded weighted heuristic propagation. `core/calibration.py` provides a monotone transform, not empirical probability calibration without separate labelled fitting/evaluation

```text
score in [0,1] != calibrated probability
convergence != certainty
score change != Bayesian update
```

## Trace and checkpoint

`RunTracer` writes project JSONL with internal SHA-256 linkage. Selected OpenTelemetry GenAI names may be borrowed where semantically appropriate, but this is not an OTel exporter or span-conformance claim

Checkpoint graph identity protects bounded resume from mismatched graph definitions. It cannot guarantee deterministic replay of external providers/tools

## PROV-aligned lineage

`core/provenance.py` emits payload-minimizing project JSON using PROV concepts. It is not PROV-O RDF serialization or complete standards conformance

```text
lineage != truth
hash identity != semantic equivalence
```

## Claim-verification architecture

`core/claim_audit.py` separates

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

Audit states remain descriptive

```text
indexed_only
evidence_bound
structurally_checked
conflict_recorded
structurally_checked_with_conflict
```

No universal `verified=true`, accepted/rejected scientific verdict, or truth label is emitted

## Claim assertion / observation basis

| Surface | Basis |
|---|---|
| claim/source/evidence refs | `structured-analyze-output` |
| consistency observations | `structured-verify-output` |
| conflicts | `structured-verify-output` |
| heuristic scores | `structured-state-output` |
| provider metadata | provider-adapter / fixture runtime |
| human review | caller-declared when supplied |

This is provenance of the recorded assertion/observation, not external validation

```text
assertion basis != correctness
structured-verify-output != scientific verification
```

## Dimensional claim audit coverage

`claim-verification` computes separate counts and ratios over indexed claims for

```text
source refs
evidence refs
internal consistency observations
cross-source observations
conflicts
initial heuristic scores
final heuristic scores
```

No aggregate quality score is computed

```json
{"aggregate_score": null}
```

```text
coverage != scientific validity
coverage ratio != probability
coverage != provenance soundness
```

The repository implements coverage only where its own structured artifacts support it

## Claim-transfer architecture

`core/claim_transfer.py` creates a bounded portable view over an existing `epistemic-pipeline/claim-verification` sidecar

Wrong-profile source JSON and missing requested claim IDs fail explicitly

The transfer preserves source/evidence refs, relations, structural observations, conflicts, heuristic-score observations, and audit state without copying full claim prose

Required transfer constraints

```text
scientific_validity_inherited: false
evidence_sufficiency_inherited: false
peer_review_inherited: false
conflicts_must_remain_visible: true
heuristic_scores_must_retain_non_probability_semantics: true
```

```text
transfer != acceptance
inheritance != validation
conflict preservation != conflict adjudication
```

## Evidence Envelope

The Evidence Envelope references graph, trace, checkpoint, provenance, claim audit/index, process disclosure, and optional upstream artifact/evidence refs

Reference-resolution coverage remains dimensional

```text
reference_count
by_resolution
local_file_ratio
aggregate_score: null
```

A local-file ratio indicates local resolvability/hashing at envelope-generation time, not source credibility or evidence quality

The Envelope stays compact and does not duplicate claim-verification or transfer payloads

## Evidence stack

```text
Trace              -> chronology
Checkpoint         -> recovery state
PROV lineage       -> derivation relationships
Claim verification -> per-claim observations/basis/coverage
Claim transfer     -> selected portable claim context + constraints
Evidence Envelope  -> compact run/cross-tool index
```

These artifacts are complementary, not interchangeable proof objects

## Maintenance and document-governance plane

`core/maintenance_cadence.py` emits `epistemic-pipeline/maintenance-report`

`maintenance/cadence.yaml` defines canonical current paths, scan paths, cadence behavior, and the configured research stage

`DOCUMENT_STATUS.md` classifies current authority, historical snapshots, examples/customization guidance, and external metadata

The scanner can report

```text
canonical path presence
decorative project profile versions
Manifest calibration age
historical snapshot inventory
canonical SHA-256 baseline
calendar-month status
configured stage status
```

For 2026-08-31

```text
calendar_month: calendar-month-close
stage: closed
```

The maintenance scanner is read-only. It does not execute the research workflow, call an LLM, verify citations, judge evidence sufficiency, run tests, delete history, or establish provenance soundness/scientific validity

## Cross-repository architecture

```text
auto-doc-engine
  artifact-record + artifact-lineage
        ↓
epistemic-pipeline
  claim-verification + claim-transfer + evidence-envelope
        ↓
sci-render-kit
  figure-claim-audit + figure-evidence + communication-transfer
```

Repositories are loosely coupled through references, not imports or inherited scientific validity

## Reproducibility

```text
R0 traceable
R1 replay-addressable
R2 environment-bounded
R3 actual separate rerun + declared comparison
```

Evidence sidecars, transfers, and maintenance baselines support bookkeeping; they do not self-award R3

## Document history

Current document authority is mapped in `DOCUMENT_STATUS.md`

Historical

```text
FOUR_DAY_CONSOLIDATION.md
FIVE_DAY_CONSOLIDATION.md
SIX_DAY_CONSOLIDATION.md
```

remain time-scoped records rather than current runtime contracts

```text
historical snapshot != current contract
later terminology != permission to rewrite history
```

## Stage-close global calibration

The 2026-08-24 → 2026-08-31 architecture is informed by

- re-openable autonomous-science provenance
- transparent AI use / human oversight
- artifact-centered claim-aware observability
- trajectory-to-evidence qualification
- evidence-bounded claim review
- end-to-end scientific-agent consistency evaluation
- claim-level auditability separating coverage, soundness, contradiction transparency, and audit effort
- Praxist-style solution/evidence lineage
- ReproAgent-style persistent contracts
- long-horizon research phase behavior and regime-aware re-validation
- ScienceFlow-style persistent research segments and recovery
- process-level evaluation beyond final scores
- persistent-runtime patterns for stable project state and reviewed routes

Borrowed: explicit audit objects, dimensional coverage, assertion provenance, contradiction visibility, persistent transfer constraints, and phase-aware review

Not claimed: provenance soundness, scientific-review authority, citation correctness, calibrated truth probability, peer review, or independent reproduction

## Non-goals

- scientific truth adjudication
- external citation-content verification by itself
- provenance soundness validation
- calibrated probabilities by default
- automatic AI-text detection
- automatic peer review
- tamper-proof external ledger
- PROV-O RDF serialization
- built-in production LLM providers
- automatic repository scheduler/history deletion
- GitHub CI/merge governance

## Hard invariants

```text
Assertion basis != correctness
Audit coverage != scientific validity
Coverage ratio != probability
Evidence ref != evidence sufficiency
Claim transfer != acceptance
Conflict absent != corroboration
Provider identity != output validity
Human review != peer review
Runtime-policy pass != scientific validation
Convergence != certainty
Provenance != truth
Maintenance clean != scientific validity
Calendar-month close != reproduction
```

## Maintenance rule

When code and docs disagree, correct implementation/documentation explicitly. New capability claims require a real code path or clear planned/experimental label. GitHub Actions, CI, CodeQL, dependency bots, branch-protection assumptions, and merge gates remain outside the research architecture
