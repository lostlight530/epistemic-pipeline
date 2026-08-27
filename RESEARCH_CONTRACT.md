# Research Contract — Epistemic Pipeline

**Calibration:** 2026-08-27  
**Status:** active research-engineering contract  
**Scope:** runtime semantics, evidence relations, recovery identity, provenance, claim verification, process disclosure and cross-repository handoff

This is a scientific-integrity contract, not a GitHub merge policy.

## 1. Repository role

Epistemic Pipeline is the **evidence-aware research execution plane**:

```text
validated graph
  -> structured provider outputs
  -> runtime policy
  -> claim/evidence/conflict structures
  -> bounded heuristic score propagation
  -> trace/checkpoint
  -> provenance
  -> claim verification record
  -> evidence envelope
```

## 2. Stable project profile names

Project-owned identifiers are unversioned:

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

Internal identifiers are semantic names, not pseudo-release numbers. External standard versions remain explicit only when they are real external versions.

## 3. Runtime-policy contract

A runtime-policy pass establishes only that explicit machine predicates passed over the available output structure.

It does not establish:

- source credibility;
- factual truth;
- statistical validity;
- causal validity;
- peer review;
- scientific acceptance.

Unknown checks fail explicitly.

## 4. Claim/evidence contract

Claims and evidence remain distinguishable objects. A claim can be indexed with zero evidence refs; this is visible rather than silently filled in.

`evidence_chains` record declared links. They do not independently prove that the linked evidence is sufficient or correctly interpreted.

## 5. Claim verification contract

`epistemic-pipeline/claim-verification` is an audit record, not a truth oracle.

For each claim the record may carry:

- claim identity/hash;
- declared source refs;
- declared evidence refs/relations;
- internal-consistency observations;
- cross-source observations;
- conflict records;
- initial and final heuristic scores;
- descriptive audit state;
- provider and human-review context.

Allowed audit states are deliberately non-verdict states:

```text
indexed_only
evidence_bound
structurally_checked
conflict_recorded
structurally_checked_with_conflict
```

The repository does not emit `verified=true`, `accepted`, `rejected` or equivalent scientific-review verdicts because it does not contain an independent domain scientific-review authority.

## 6. Score contract

Any bounded score produced by the default network is a heuristic value in `[0,1]`.

```text
heuristic score != calibrated probability
final score != probability posterior
score increase != stronger scientific truth
numerical convergence != certainty
```

A temperature transform that was not fitted/evaluated on labelled data remains a transform and must not be presented as empirical probability calibration.

## 7. Trace contract

`epistemic-pipeline/trace` records project events and internal correlation. Reused OpenTelemetry GenAI field names are scoped naming alignment only.

The SHA-256 previous-record chain demonstrates internal linkage for the records present. It is not an externally anchored immutable ledger.

## 8. Checkpoint contract

`epistemic-pipeline/checkpoint` binds successful node results to graph ID and canonical graph SHA-256.

Resume identity checks prevent ambiguous graph mismatch. They do not prove that non-deterministic providers will replay the same output.

## 9. Provenance contract

`epistemic-pipeline/prov` uses W3C PROV concepts in project JSON.

It can establish declared lineage relationships and byte/structural identities. It does not claim:

- PROV-O RDF serialization;
- complete W3C PROV conformance;
- scientific truth;
- independent reproduction.

## 10. Evidence Envelope contract

`epistemic-pipeline/evidence-envelope` is the compact handoff object. It can reference:

```text
graph
trace
checkpoint
provenance
claim-index
claim-verification
process disclosure
upstream artifact refs
upstream evidence refs
```

It does not duplicate full research payloads by default.

A local upstream file can be hashed. An opaque URI/reference is retained without dereferencing. Neither case imports scientific validity from upstream.

## 11. Provider disclosure contract

Provider metadata describes the execution route only. Unknown fields remain unknown.

The built-in synthetic fixture declares:

```text
model: null
version: null
mode: synthetic_fixture
external_model_call: false
```

No version is invented for a fixture that has no externally meaningful release identity.

## 12. Human-review contract

Current values:

```text
reviewed
partial
not_reviewed
not_declared
```

These record declared human involvement only.

```text
human review != peer review
human review != scientific validation
```

## 13. Upstream/downstream handoff

Preferred upstream artifact profile:

```text
auto-doc-engine/artifact-record
```

Preferred downstream communication profiles:

```text
sci-render-kit/figure-claim-audit
sci-render-kit/figure-evidence
```

Cross-repository interoperability is reference-based and optional; no direct runtime import is required.

## 14. Reproducibility levels

- **R0 Traceable** — identity/source pointers exist.
- **R1 Replay-addressable** — intended run/input/config identities can be located.
- **R2 Environment-bounded** — relevant environment/dependency assumptions are recorded.
- **R3 Reproduced** — a separate rerun actually occurred and was compared under a declared criterion.

Trace, checkpoint, provenance, claim verification or Evidence Envelope artifacts can support auditability; none automatically establishes R3.

## 15. External research calibration

The 2026-08-27 design is informed by recent work on:

- provenance-grounded trust in autonomous science;
- transparent/responsible AI use in scientific publishing;
- artifact-centered claim-aware observability;
- evidence-constrained claim qualification;
- trajectory-to-evidence conversion;
- strict end-to-end evaluation of scientific agents.

The repository borrows design principles only. The referenced publications do not validate this implementation.

## 16. Non-inference rules

The following implications are forbidden:

```text
run success -> scientific validity
runtime policy pass -> truth
claim indexed -> claim true
evidence linked -> evidence sufficient
no conflict -> corroborated truth
heuristic score -> probability
convergence -> certainty
provider identity -> output validity
human review -> peer review
provenance -> truth
metadata -> reproduction
```

## 17. Governance boundary

GitHub Actions, CI, CodeQL, dependency bots, branch protection and merge gates are outside this research architecture. Existing tests/local checks remain optional maintenance aids and are not the completion criterion for the 2026-08-27 consolidation.
