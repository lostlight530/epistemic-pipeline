# Research Contract — Epistemic Pipeline

**Calibration:** 2026-08-29  
**Status:** active research-engineering contract  
**Scope:** runtime semantics, evidence relations, recovery identity, provenance, claim verification, claim transfer, assertion basis, audit coverage, process disclosure and cross-repository handoff

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
  -> optional claim-transfer
       ├─ explicit claim selection
       └─ non-inheritance constraints
  -> evidence-envelope
       └─ upstream-reference coverage
```

## Stable project identifiers

Project-owned identifiers are unversioned semantic names. Real external standard/runtime versions remain explicit only when genuinely defined/observed.

Key handoff profiles now include:

```text
epistemic-pipeline/claim-verification
epistemic-pipeline/claim-transfer
epistemic-pipeline/evidence-envelope
```

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

Per claim it may preserve identity/hash, source refs, evidence refs/relations, internal-consistency observation, cross-source observation, conflicts, initial/final heuristic scores, descriptive audit state and assertion/observation basis.

Allowed audit states remain non-verdict states:

```text
indexed_only
evidence_bound
structurally_checked
conflict_recorded
structurally_checked_with_conflict
```

No `verified=true`, `accepted`, `rejected` or equivalent scientific-review verdict is emitted because the repository has no independent domain scientific-review authority.

## Claim-transfer contract

`epistemic-pipeline/claim-transfer` creates a bounded downstream view over an existing claim-verification sidecar.

A caller may explicitly select claim IDs. A requested claim ID that does not exist fails explicitly rather than being manufactured.

The transfer preserves:

```text
claim identity/hash
source refs
evidence refs / relations
structural observations
conflicts
initial/final heuristic-score observations
audit state
```

and attaches mandatory non-inheritance constraints:

```text
scientific_validity_inherited: false
evidence_sufficiency_inherited: false
peer_review_inherited: false
conflicts_must_remain_visible: true
heuristic_scores_must_retain_non_probability_semantics: true
```

Hard rules:

```text
claim transfer != acceptance
inheritance != validation
conflict preservation != conflict adjudication
copied sidecar record != independently reverified record
```

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
copied-from-local-claim-verification-sidecar
```

Hard rule:

```text
assertion basis != correctness
structured-verify-output != external scientific verification
provider-adapter-reported != vendor certification
```

Process disclosure records `automatic_ai_detection_used: false`; this repository does not infer AI authorship/use from text.

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

`claim-transfer` separately reports selected-claim count plus evidence/conflict/observation/final-score coverage for the transferred subset.

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

`epistemic-pipeline/evidence-envelope` is a compact run-level handoff index referencing graph, trace, checkpoint, provenance, claim index, claim verification, process disclosure and optional upstream artifact/evidence refs.

It records upstream reference-resolution coverage but does not duplicate the full claim audit or claim-transfer records.

```text
local resolution != source credibility
reference coverage != evidence quality
opaque URI != invalid evidence
```

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
        ↓
auto-doc-engine/artifact-lineage
        ↓
epistemic-pipeline/claim-verification
        ↓ optional selected handoff
epistemic-pipeline/claim-transfer
        ↓
epistemic-pipeline/evidence-envelope
        ↓
sci-render-kit/figure-claim-audit
sci-render-kit/figure-evidence
sci-render-kit/communication-transfer
```

Interoperability is reference/transfer based and optional; no direct runtime import or inherited scientific validity is required.

## Reproducibility levels

- **R0 Traceable** — identity/source pointers exist.
- **R1 Replay-addressable** — intended run/input/config identities can be located.
- **R2 Environment-bounded** — relevant environment/dependency assumptions recorded.
- **R3 Reproduced** — a separate rerun actually occurred and was compared under a declared criterion.

No trace/checkpoint/provenance/claim-verification/claim-transfer/envelope artifact self-awards R3.

## Six-day external calibration

The design is informed by work on re-openable autonomous-science provenance, transparent AI use/human oversight, artifact-centered claim-aware observability, trajectory-to-evidence qualification, Brain Researcher evidence-bounded claims, EarthVerse end-to-end consistency, claim-level auditability, **Praxist** solution/evidence lineages (arXiv:2608.25955) and **ReproAgent** persistent implementation/reference contracts (arXiv:2608.24291).

Borrowed: explicit audit objects, dimensional coverage, contradiction visibility, assertion provenance, evidence-bounded qualification and persistence of constraints across long research trajectories.

Not claimed: provenance soundness, citation correctness, scientific-review authority, calibrated truth probability, AI-content detection, peer review or independent reproduction.

## Forbidden implications

```text
run success -> scientific validity
runtime policy pass -> truth
claim indexed -> claim true
evidence linked -> evidence sufficient
claim transferred -> accepted
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
