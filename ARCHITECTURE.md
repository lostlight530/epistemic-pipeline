# Architecture — Epistemic Pipeline

> Calibrated 2026-08-27. This document describes implemented runtime semantics and research-integrity boundaries. It does not define GitHub platform governance.

## 1. Architectural thesis

Research execution is modeled as an **evidence-bearing state-transition system**. The repository separates:

1. dependency structure;
2. provider execution;
3. runtime-policy predicates;
4. claim/evidence/conflict structures;
5. bounded heuristic scores;
6. recovery identity;
7. run tracing;
8. provenance lineage;
9. claim-level verification observations;
10. cross-tool handoff.

The system deliberately avoids a single “agent success” flag because execution completion, structural validity, evidence support and scientific validity are different properties.

## 2. Canonical runtime

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
run result
```

`discover -> analyze -> verify -> synthesize -> archive` is the default semantic progression, while the actual executable ordering is derived from graph dependencies.

## 3. Stable project identifiers

Internal profile names are stable semantic identifiers and carry no decorative release suffixes:

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

Schema evolution is documented through contracts and fields rather than arbitrary `@1/@2` labels. External standards retain their actual published versions where applicable.

## 4. Dependency graph

`core/dependency_graph.py` validates structural properties such as duplicate IDs, missing dependencies, cycles and reachability, and produces deterministic topological ordering / parallel groups.

This is graph validity, not research validity.

## 5. Provider boundary

`LLMProvider` is a small interface:

```text
system prompt + user prompt + optional schema
          ↓
structured mapping
```

The repository contains only `MockProvider`, a deterministic synthetic fixture. It declares no model and no invented version. Real model/provider integrations must be injected by callers.

Provider metadata is process context only.

## 6. Runtime policy

`RuntimePolicyEvaluator` executes only explicit machine-readable checks in state definitions. Human `rule` descriptions are never parsed into executable logic.

The legacy names `Gatekeeper`, `check_quality_gates` and the fallback `quality_gates` state key remain compatibility surfaces, not the active conceptual model.

```text
runtime-policy success = declared structural/output predicates passed
runtime-policy success != scientific validity
```

## 7. Score layer

`ConfidenceNetwork` performs synchronous bounded weighted propagation. The historical class name remains for compatibility, but its semantics are explicitly heuristic.

`core/calibration.py` provides a monotone transform, not empirical probability calibration unless a caller separately fits and evaluates it on labelled data.

## 8. Trace layer

`RunTracer` writes JSONL records with project correlation fields and an internal SHA-256 previous-record chain.

OpenTelemetry GenAI naming is borrowed only where semantically appropriate, notably `gen_ai.operation.name`. The implementation is not an OpenTelemetry SDK exporter and project run IDs are not presented as provider conversation IDs.

Internal chain verification demonstrates consistency over the records currently present; without an external anchor/count it is not tamper-proof.

## 9. Checkpoint and recovery identity

Checkpoint data records:

```text
profile: epistemic-pipeline/checkpoint
run_id
graph_id
graph_sha256
completed nodes
results
```

Resume refuses a checkpoint whose graph ID or canonical graph digest does not match the current graph.

This guards against ambiguous recovery; it cannot guarantee deterministic external-provider replay.

## 10. PROV-aligned lineage

`core/provenance.py` emits a payload-minimizing project JSON using W3C PROV concepts. Node outputs are represented through identities and structural metadata rather than duplicated payload text.

It is not a PROV-O RDF serializer and does not claim complete W3C PROV serialization conformance.

## 11. Claim verification architecture

`core/claim_audit.py` exists because “verify stage executed” is too coarse to describe research status.

For each claim it records independent dimensions:

```text
identity
source refs
evidence refs
relations
internal consistency observation
cross-source observation
conflicts
initial heuristic score
final heuristic score
audit state
```

Audit states are descriptive process states only:

```text
indexed_only
evidence_bound
structurally_checked
conflict_recorded
structurally_checked_with_conflict
```

No `verified=true`, accepted/rejected verdict or scientific truth label is emitted.

## 12. Evidence Envelope

The Evidence Envelope is a compact project-owned interchange index. It references rather than duplicates:

```text
graph
trace
checkpoint
provenance
claim audit
claim index
process disclosure
upstream artifact/evidence refs
```

Local upstream files are hashed; opaque or URI references are retained without network dereference. Scientific validity is never inherited automatically from upstream metadata.

## 13. Evidence stack

The canonical post-run evidence stack is:

```text
RunTracer
    │ execution chronology
    ▼
Checkpoint
    │ recovery state
    ▼
PROV-aligned lineage
    │ derivation relationships
    ▼
Claim verification record
    │ claim-level observations/conflicts/scores
    ▼
Evidence Envelope
      cross-tool index/handoff
```

These artifacts are complementary, not interchangeable.

## 14. Cross-repository architecture

```text
auto-doc-engine
artifact-record + process context
        ↓
epistemic-pipeline
claim/evidence structure + claim verification + lineage
        ↓
sci-render-kit
claim-to-visual communication + communication audit
```

The repositories are loosely coupled through references and stable semantic identifiers. They do not need direct imports.

## 15. Reproducibility

R0–R3 are local project terms, not external standards:

```text
R0 traceable
R1 replay-addressable
R2 environment-bounded
R3 reproduced by a separate rerun and declared comparison
```

Evidence sidecars can support R0/R1 bookkeeping. They cannot self-declare a run R3 without an actual separate rerun.

## 16. Current global design calibration

The architecture is consistent with several 2026 research directions:

- re-openable provenance for autonomous science;
- transparent AI use and human responsibility in scientific publishing;
- artifact-centered claim-aware observability;
- distinguishing completed trajectories from defensible evidence;
- evidence-constrained claim qualification;
- evaluating end-to-end scientific consistency rather than only local task success.

The repository borrows these design lessons, not external authority. None of these publications certifies this implementation.

## 17. Non-goals

The architecture does not currently provide:

- scientific truth adjudication;
- citation-content verification against external literature by itself;
- calibrated probabilities by default;
- automatic peer review;
- a tamper-proof external ledger;
- PROV-O RDF serialization;
- built-in production LLM providers;
- GitHub CI/merge governance.

## 18. Maintenance rule

When implementation, README, Architecture, Research Contract, Manifest and examples disagree, implementation plus explicit contracts are authoritative and documentation must be corrected. New capability claims require an actual code path or an explicit `planned/experimental` label.
