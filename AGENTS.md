# Agent Guide — Epistemic Pipeline

This guide defines how coding/research agents should modify the repository without overstating scientific authority

Implementation in `core/`, `states/`, `graphs/`, `validators/` plus the active contracts define current semantics
If docs disagree with code, correct one explicitly and never invent a capability to reconcile them

## Stable internal identifiers

Project-owned profile names are unversioned semantic names
Do not add decorative `@1/@2`, `/v1`, fake fixture/model versions, or similar pseudo-version suffixes
Preserve real external standard/runtime versions when genuinely applicable

Current stable maintenance identifiers include

```text
epistemic-pipeline/maintenance-cadence
epistemic-pipeline/maintenance-report
```

## System identity

```text
graphs/*.yaml
  -> DependencyGraph
  -> StateMachineEngine
  -> LLMHarness / injected LLMProvider
  -> RuntimePolicyEvaluator
  -> bounded heuristic score network
  -> RunTracer + checkpoint
  -> PROV-aligned lineage
  -> claim-verification
       ├─ assertion / observation basis
       └─ dimensional audit coverage
  -> optional claim-transfer
       ├─ explicit claim selection
       └─ non-inheritance constraints
  -> evidence-envelope
       └─ upstream-reference coverage
```

## No hallucinated provider identity

`LLMProvider.describe()` may contain only metadata actually known by the provider integration

- unknown vendor/model/version -> `null` or omitted
- never infer model identity from prompt style, class name, environment-variable name, or marketing copy
- MockProvider remains a synthetic fixture with `model: null`, `version: null`, `external_model_call: false`
- provider descriptions preserve assertion basis
- the canonical path records `automatic_ai_detection_used: false`

## Claim verification rules

`core/claim_audit.py` records audit dimensions, not scientific verdicts

Allowed descriptive states

```text
indexed_only
evidence_bound
structurally_checked
conflict_recorded
structurally_checked_with_conflict
```

Do not add universal `verified=true`, accepted/rejected/proven verdicts without a separately designed and evidenced scientific-review authority

## Claim transfer rules

`core/claim_transfer.py` may select existing claim records for downstream handoff, but transfer is not acceptance

Required invariants

```text
scientific_validity_inherited: false
evidence_sufficiency_inherited: false
peer_review_inherited: false
conflicts_must_remain_visible: true
heuristic_scores_must_retain_non_probability_semantics: true
```

Never silently remove conflicts, upgrade audit states, convert heuristic scores into probabilities, or manufacture a missing requested claim ID
Missing requested claim IDs fail explicitly

## Assertion / observation basis rules

Current bases include

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

Never upgrade basis into correctness

```text
structured-verify-output != scientific verification
provider-adapter-reported != vendor certification
caller-declared review != peer review
copied-from-sidecar != independently reverified
```

## Audit coverage rules

Coverage remains dimensional
Do not create a synthetic aggregate research-quality score

```text
coverage != provenance soundness
coverage != scientific validity
coverage ratio != probability
coverage ratio != evidence sufficiency
```

`aggregate_score` remains `null` unless a future explicitly validated evaluation regime is designed and documented

## Score rules

Never describe `[0,1]` as probability by default, convergence as certainty, score change as Bayesian update, or unfitted temperature scaling as calibrated probability

## Provenance / trace rules

`core/provenance.py` is PROV-aligned project JSON, not PROV-O RDF conformance
`core/run_tracer.py` is project JSONL tracing, not an OpenTelemetry exporter or tamper-proof ledger

## Runtime policy rule

Machine behavior comes from `check` + explicit parameters
Human-readable `rule` text is documentation only
Unknown checks fail explicitly

## Evidence-stack separation

```text
trace -> chronology
checkpoint -> recovery state
provenance -> lineage
claim audit -> claim observations/basis/coverage
claim transfer -> selected portable claim handoff
evidence envelope -> compact run-level handoff + ref coverage
```

Do not merge them into one proof object

## Maintenance cadence

`MAINTENANCE_CADENCE.md` and `maintenance/cadence.yaml` define the active daily / weekly / monthly maintenance contract

Local scanner

```bash
python core/maintenance_cadence.py daily
python core/maintenance_cadence.py weekly
python core/maintenance_cadence.py monthly --as-of YYYY-MM-DD
```

Daily maintenance

- start from current `main`
- correct demonstrated runtime/claim/evidence/profile drift only
- preserve provider unknowns, conflict visibility, and heuristic non-probability semantics
- do not rewrite historical stage snapshots or manufacture daily changes

Weekly maintenance

- reconcile implementation, Manifest, Research Contract, Claim Audit Contract, Claim Transfer Contract, Agent Guide, Frontier Alignment, and cross-repository profile names
- review trace/checkpoint/provenance/claim-audit/claim-transfer/envelope separation
- inventory the prior seven days of snapshots without rewriting them

Monthly or explicit phase-close maintenance

- build a month-to-date or explicit phase-close canonical hash baseline
- inventory historical snapshots and review deprecation candidates manually
- confirm no structural state has been promoted into a truth verdict
- state explicitly whether the month or research phase is actually closed

On 2026-08-30 the August maintenance record is month-to-date, not final calendar-month close

```text
maintenance clean != scientific validity
weekly consistency != evidence sufficiency
monthly baseline != reproduction
coverage inventory != provenance soundness
```

The scanner itself does not run the research workflow, call an LLM, run tests, verify citations, or judge evidence sufficiency

## Cross-repository handoff

```text
auto-doc-engine/artifact-record
  -> auto-doc-engine/artifact-lineage
  -> epistemic-pipeline/claim-verification
  -> epistemic-pipeline/claim-transfer
  -> epistemic-pipeline/evidence-envelope
  -> sci-render-kit/figure-claim-audit
  -> sci-render-kit/figure-evidence
  -> sci-render-kit/communication-transfer
```

References and transfers are not runtime imports or inherited truth claims

## Experimental modules

`anti_entropy.py`, `convergence.py`, `infinite_regression.py`, `neuro_symbolic.py`, `perception.py`, and `thread_collapse.py` remain experimental unless deliberately integrated
Metaphorical names are not capability evidence

## R3 discipline

Metadata, checkpoint, provenance, provider disclosure, audit coverage, claim audit, claim transfer, maintenance reports, or hash baselines never count as independent reproduction
R3 requires an actual separate rerun plus a declared comparison criterion

## Governance boundary

Do not add GitHub Actions, CI, CodeQL, dependency bots, branch-protection assumptions, or merge-gate architecture as ordinary repository architecture
Local checks/tests are optional maintenance aids, not scientific validation

## Documentation synchronization

When a public research contract changes, synchronize the relevant implementation, Manifest, contracts, examples, and frontier notes
When maintenance cadence changes, synchronize `MAINTENANCE_CADENCE.md`, `maintenance/cadence.yaml`, `core/maintenance_cadence.py`, `STAGE_2026_08_MAINTENANCE.md`, Manifest, and this Agent Guide
Prefer honest `implemented / experimental / proposed / not integrated` states over aspirational wording
