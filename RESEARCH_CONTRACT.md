# Research Contract — Epistemic Pipeline

**Calibration:** 2026-08-28  
**Status:** active research-engineering contract  
**Scope:** runtime semantics, evidence relations, recovery identity, provenance, claim verification, assertion basis, audit coverage, process disclosure and cross-repository handoff

This is a scientific-integrity contract, not a GitHub merge policy.

## Repository role

```text
validated graph
  -> structured provider outputs
  -> runtime policy
  -> claim/evidence/conflict structures
  -> bounded heuristic score propagation
  -> trace/checkpoint
  -> PROV-aligned lineage
  -> claim-verification
       ├─ assertion/observation basis
       └─ dimensional audit coverage
  -> evidence-envelope
       └─ upstream-reference coverage
```

## Stable project identifiers

Project-owned identifiers are unversioned semantic names. Real external standard/runtime versions remain explicit only when genuinely defined/observed.

## Runtime-policy contract

A runtime-policy pass establishes only that explicit machine predicates passed over available output structure.

```text
runtime-policy pass != source credibility
runtime-policy pass != factual truth
runtime-policy pass != statistical/causal validity
runtime-policy pass != peer review
```

Unknown checks fail explicitly.

## Claim/evidence contract

Claims and evidence remain distinguishable objects. A claim may be indexed with zero evidence refs; that absence is preserved rather than fabricated.

`evidence_chains` are declared/structured links, not independent proof of evidence sufficiency or correct interpretation.

## Claim-verification contract

`epistemic-pipeline/claim-verification` is an audit record, not a truth oracle.

Per claim it may preserve:

- identity/hash;
- source refs;
- evidence refs/relations;
- internal-consistency observation;
- cross-source observation;
- conflicts;
- initial/final heuristic scores;
- descriptive audit state;
- assertion/observation basis.

Allowed audit states remain non-verdict states:

```text
indexed_only
evidence_bound
structurally_checked
conflict_recorded
structurally_checked_with_conflict
```

No `verified=true`, `accepted`, `rejected` or equivalent scientific-review verdict is emitted because the repository has no independent domain scientific-review authority.

## Assertion / observation basis contract

Important audit fields carry acquisition basis such as:

```text
structured-analyze-output
structured-verify-output
structured-state-output
provider-adapter-reported
synthetic-fixture-runtime
runtime-harness-state
caller-declared
runtime-observed-local-filesystem
```

Hard rule:

```text
assertion basis != correctness
structured-verify-output != external scientific verification
provider-adapter-reported != vendor certification
```

Process disclosure also records `automatic_ai_detection_used: false`; this repository does not infer AI authorship/use from text.

## Audit-coverage contract

`claim-verification` computes dimensional coverage over indexed claims:

```text
claims with source refs
claims with evidence refs
claims with internal-consistency observations
claims with cross-source observations
claims with conflict records
claims with initial heuristic scores
claims with final heuristic scores
```

Ratios use indexed claims as the denominator where defined.

No aggregate quality score is produced:

```json
{"aggregate_score": null}
```

```text
coverage != provenance soundness
coverage != scientific validity
coverage ratio != probability
coverage ratio != evidence sufficiency
```

Current claim-level auditability research motivates measuring coverage separately from soundness. This implementation does not claim provenance soundness.

## Score contract

```text
heuristic score != calibrated probability
final score != probability posterior
score increase != stronger scientific truth
numerical convergence != certainty
```

A transform not fitted/evaluated on labelled data remains a transform, not empirical probability calibration.

## Trace contract

`epistemic-pipeline/trace` records project events/correlation. Reused OpenTelemetry GenAI field names are scoped naming alignment only.

The internal SHA-256 link chain is not an externally anchored immutable ledger.

## Checkpoint contract

Checkpoint graph ID/canonical SHA-256 guards against ambiguous graph mismatch during resume. It does not prove deterministic external-provider replay.

## Provenance contract

`epistemic-pipeline/prov` uses W3C PROV concepts in project JSON.

```text
PROV-aligned != PROV-O RDF conformance
lineage != truth
lineage != independent reproduction
```

## Evidence Envelope contract

`epistemic-pipeline/evidence-envelope` is a compact handoff index referencing graph, trace, checkpoint, provenance, claim index, claim verification, process disclosure and optional upstream artifact/evidence refs.

Day 5 adds reference-resolution coverage:

```text
reference_count
by_resolution
local_file_ratio
aggregate_score: null
```

```text
local resolution != source credibility
reference coverage != evidence quality
opaque URI != invalid evidence
```

The Envelope references the claim-verification artifact rather than duplicating its full contents.

## Provider disclosure contract

Provider metadata describes the execution route only and includes assertion basis.

```text
base injected provider -> provider-adapter-reported
MockProvider           -> synthetic-fixture-runtime
no provider configured -> runtime-harness-state
```

Unknown model/version remains `null`. No fake version is invented.

```text
provider metadata != AI-text detection
provider identity != output validity
```

## Human-review contract

```text
reviewed
partial
not_reviewed
not_declared
```

When supplied, review state is caller-declared.

```text
human review != peer review
human review != scientific validation
```

## Cross-repository handoff

```text
auto-doc-engine/artifact-record
  assertion basis + artifact coverage
        ↓
epistemic-pipeline/claim-verification
  observation basis + claim audit coverage
        ↓
epistemic-pipeline/evidence-envelope
        ↓
sci-render-kit/figure-claim-audit
sci-render-kit/figure-evidence
```

Interoperability is reference-based and optional; no direct runtime import or inherited scientific validity is required.

## Reproducibility levels

- **R0 Traceable** — identity/source pointers exist.
- **R1 Replay-addressable** — intended run/input/config identities can be located.
- **R2 Environment-bounded** — relevant environment/dependency assumptions recorded.
- **R3 Reproduced** — a separate rerun actually occurred and was compared under a declared criterion.

No trace/checkpoint/provenance/claim-verification/envelope artifact self-awards R3.

## Five-day external calibration

The 2026-08-24 → 2026-08-28 design is informed by work on re-openable autonomous-science provenance, transparent AI use/human oversight, artifact-centered claim-aware observability, trajectory-to-evidence qualification, Brain Researcher evidence-bounded claims, EarthVerse end-to-end consistency, and claim-level auditability separating provenance coverage, soundness, contradiction transparency and audit effort.

Borrowed: explicit audit objects, dimensional coverage, contradiction visibility, assertion provenance and evidence-bounded qualification.

Not claimed: provenance soundness, citation correctness, scientific-review authority, calibrated truth probability, AI-content detection, peer review or independent reproduction.

## Forbidden implications

```text
run success -> scientific validity
runtime policy pass -> truth
claim indexed -> claim true
evidence linked -> evidence sufficient
assertion basis -> correctness
coverage -> quality
coverage ratio -> probability
no conflict -> corroborated truth
heuristic score -> probability
convergence -> certainty
provider identity -> output validity
human review -> peer review
provenance -> truth
metadata -> reproduction
```

## Governance boundary

GitHub Actions, CI, CodeQL, dependency bots, branch protection and merge gates remain outside this research architecture. Local checks are optional maintenance aids and are not the completion criterion for this consolidation.
