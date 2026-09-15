# Research Contract — Epistemic Pipeline

**Calibration:** 2026-08-31  
**Status:** active research-engineering contract  
**Closed stage:** 2026-08-24 through 2026-08-31  
**Scope:** runtime semantics, evidence relations, recovery identity, provenance, claim verification, claim transfer, assertion basis, audit coverage, process disclosure, maintenance/document governance, and cross-repository handoff

This is a scientific-integrity contract, not a GitHub merge policy

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

repository state
  -> daily / weekly / monthly maintenance
       ├─ current-document authority
       ├─ evidence-stack reconciliation
       ├─ calendar/stage status
       └─ optional canonical SHA-256 baseline
```

## Stable project identifiers

Project-owned identifiers are unversioned semantic names. Real external standard/runtime versions remain explicit only when genuinely defined/observed

Key current profiles include

```text
epistemic-pipeline/claim-verification
epistemic-pipeline/claim-transfer
epistemic-pipeline/evidence-envelope
epistemic-pipeline/maintenance-cadence
epistemic-pipeline/maintenance-report
```

## Document-authority contract

`DOCUMENT_STATUS.md` classifies current authoritative documents, historical snapshots, examples/customization guidance, and external/citation metadata

Historical consolidation files remain time-scoped evidence and are not current contracts

```text
historical snapshot != current contract
current contract != permission to rewrite history
```

Routine maintenance must not rewrite `FOUR_DAY_CONSOLIDATION.md`, `FIVE_DAY_CONSOLIDATION.md`, or `SIX_DAY_CONSOLIDATION.md` merely because later terminology changed

## Runtime-policy contract

A runtime-policy pass establishes only that explicit machine predicates passed over available output structure

```text
runtime-policy pass != source credibility
runtime-policy pass != factual truth
runtime-policy pass != statistical/causal validity
runtime-policy pass != peer review
```

Unknown checks fail explicitly

## Claim/evidence contract

Claims and evidence remain distinguishable objects. A claim may be indexed with zero evidence refs; that absence is preserved rather than fabricated

`evidence_chains` are declared/structured links, not independent proof of evidence sufficiency or correct interpretation

## Claim-verification contract

`epistemic-pipeline/claim-verification` is an audit record, not a truth oracle

Per claim it may preserve identity/hash, source refs, evidence refs/relations, internal-consistency observation, cross-source observation, conflicts, initial/final heuristic scores, descriptive audit state, and assertion/observation basis

Allowed audit states remain non-verdict states

```text
indexed_only
evidence_bound
structurally_checked
conflict_recorded
structurally_checked_with_conflict
```

No `verified=true`, `accepted`, `rejected`, or equivalent scientific-review verdict is emitted because the repository has no independent domain scientific-review authority

## Claim-transfer contract

`epistemic-pipeline/claim-transfer` creates a bounded downstream view over an existing claim-verification sidecar

A caller may explicitly select claim IDs. A requested claim ID that does not exist fails explicitly rather than being manufactured

The source JSON must carry the expected `epistemic-pipeline/claim-verification` profile

The transfer preserves

```text
claim identity/hash
source refs
evidence refs / relations
structural observations
conflicts
initial/final heuristic-score observations
audit state
```

Mandatory non-inheritance constraints

```text
scientific_validity_inherited: false
evidence_sufficiency_inherited: false
peer_review_inherited: false
conflicts_must_remain_visible: true
heuristic_scores_must_retain_non_probability_semantics: true
```

```text
claim transfer != acceptance
inheritance != validation
conflict preservation != conflict adjudication
copied sidecar record != independently reverified record
```

## Assertion / observation basis contract

Important audit fields carry acquisition basis such as

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

```text
assertion basis != correctness
structured-verify-output != external scientific verification
provider-adapter-reported != vendor certification
```

Process disclosure records `automatic_ai_detection_used: false`; this repository does not infer AI authorship/use from text

## Audit-coverage contract

`claim-verification` computes dimensional coverage over indexed claims

```text
claims with source refs
claims with evidence refs
claims with internal-consistency observations
claims with cross-source observations
claims with conflict records
claims with initial heuristic scores
claims with final heuristic scores
```

`claim-transfer` separately reports selected-claim count plus evidence/conflict/observation/final-score coverage for the transferred subset

No aggregate quality score is produced

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

A transform not fitted/evaluated on labelled data remains a transform, not empirical probability calibration

## Trace contract

`epistemic-pipeline/trace` records project events/correlation. Reused OpenTelemetry GenAI field names are scoped naming alignment only

The internal SHA-256 link chain is not an externally anchored immutable ledger

## Checkpoint contract

Checkpoint graph ID/canonical SHA-256 guards against ambiguous graph mismatch during resume. It does not prove deterministic external-provider replay

## Provenance contract

`epistemic-pipeline/prov` uses W3C PROV concepts in project JSON

```text
PROV-aligned != PROV-O RDF conformance
lineage != truth
lineage != independent reproduction
```

## Evidence Envelope contract

`epistemic-pipeline/evidence-envelope` is a compact run-level handoff index referencing graph, trace, checkpoint, provenance, claim index, claim verification, process disclosure, and optional upstream artifact/evidence refs

It records upstream reference-resolution coverage but does not duplicate full claim-audit or claim-transfer records

```text
local resolution != source credibility
reference coverage != evidence quality
opaque URI != invalid evidence
```

## Provider disclosure contract

Provider metadata describes the execution route only and includes assertion basis

```text
base injected provider -> provider-adapter-reported
MockProvider           -> synthetic-fixture-runtime
no provider configured -> runtime-harness-state
```

Unknown model/version remains `null`. No fake version is invented

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

When supplied, review state is caller-declared

```text
human review != peer review
human review != scientific validation
```

## Maintenance contract

`MAINTENANCE_CADENCE.md`, `maintenance/cadence.yaml`, `DOCUMENT_STATUS.md`, and `STAGE_2026_08_MAINTENANCE.md` define current repository-maintenance/document-governance semantics

The local scanner is read-only and reports date-derived calendar status plus configured stage status

For 2026-08-31

```text
calendar_month: calendar-month-close
stage: closed
```

Daily maintenance addresses demonstrated local runtime/claim/evidence/document drift

Weekly maintenance reconciles the complete current evidence/document stack and inventories historical snapshots without rewriting them

Monthly or explicit phase-close maintenance records canonical baselines and reviews current/experimental/not-integrated/document status without automatic deletion

```text
maintenance clean != scientific validity
weekly consistency != evidence sufficiency
calendar-month close != reproduction
history inventory != deprecation decision
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

Interoperability is reference/transfer based and optional; no direct runtime import or inherited scientific validity is required

## Reproducibility levels

- **R0 Traceable** — identity/source pointers exist
- **R1 Replay-addressable** — intended run/input/config identities can be located
- **R2 Environment-bounded** — relevant environment/dependency assumptions recorded
- **R3 Reproduced** — a separate rerun actually occurred and was compared under a declared criterion

No trace/checkpoint/provenance/claim-verification/claim-transfer/envelope/maintenance artifact self-awards R3

## Stage-close external calibration

The closed 2026-08-24 → 2026-08-31 design is informed by work on

- re-openable autonomous-science provenance
- transparent AI use/human oversight
- artifact-centered claim-aware observability
- trajectory-to-evidence qualification
- evidence-bounded claims/review
- end-to-end scientific-agent consistency
- claim-level auditability
- Praxist-style solution/evidence lineages
- ReproAgent-style persistent implementation/reference contracts
- long-horizon research phase behavior and regime-aware re-validation
- ScienceFlow-style persistent research segments and recovery
- process-level long-horizon evaluation beyond final scores
- persistent-runtime patterns for durable project state and reviewed routes

Borrowed: explicit audit objects, dimensional coverage, contradiction visibility, assertion provenance, evidence-bounded qualification, persistent constraints, and phase-aware review

Not claimed: provenance soundness, citation correctness, scientific-review authority, calibrated truth probability, AI-content detection, peer review, or independent reproduction

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
maintenance clean -> scientific validity
calendar-month close -> reproduction
metadata -> reproduction
```

## Governance boundary

GitHub Actions, CI, CodeQL, dependency bots, branch protection, and merge gates remain outside this research architecture. Local/manual checks are optional maintenance aids and are not the completion criterion for this stage-close reconciliation
