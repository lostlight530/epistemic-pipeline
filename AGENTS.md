# Agent Guide — Epistemic Pipeline

This guide defines how coding/research agents should modify the repository without overstating scientific authority.

Implementation in `core/`, `states/`, `graphs/`, `validators/` plus active contracts define current semantics. If docs disagree with code or machine rules, correct the owning layer explicitly and never invent a capability to reconcile them.

## Document authority

Read `docs/03-maintenance-and-audit/DOCUMENT_STATUS.md` before broad documentation or governance work.

Use `docs/03-maintenance-and-audit/history/JULES_CORRECTION_RECORD.md` only when interpreting early Jules task/PR prose as historical evidence. It is a dated correction record, not a current authority layer.

Historical consolidation snapshots remain time-scoped records, not current contracts.

```text
historical snapshot != current contract
later terminology != permission to rewrite history
historical agent PR narrative != current evidence contract
```

## Recovery orders

Do not collapse maintenance-control recovery and claim/evidence/runtime semantic authority.

### Maintenance-control recovery

```text
current merged main implementation
> MANIFEST.yaml / validators / current machine-readable configuration
> latest relevant dated repair or current maintenance record
> docs/03-maintenance-and-audit/DOCUMENT_STATUS.md
> AGENTS.md
> active subject-specific contracts
> docs/03-maintenance-and-audit/MAINTENANCE_CADENCE.md / maintenance/cadence.yaml
> current Architecture / README explanation
> historical snapshots / superseded plans / PR-task narratives
```

### Subject-specific semantics

```text
current implementation
> current validator / machine-readable contract / configuration for the subject
> active subject-specific contract
> executable/operational evidence for supported use
> current explanatory documentation
> maintenance evidence
> historical records
```

A maintenance record may be newer without becoming stronger authority for claim truth, evidence sufficiency, provider identity, or scientific validity.

## Maintenance task identity

Record, when applicable:

```text
repository
+ owning surface / task
+ logical period or evidence window
+ producer / maintainer
+ exact base revision
+ run identity when available
```

Before any write, inspect open PRs/live branches for the same owning surface and logical period.

```text
overlap -> COORDINATE
no confirmed defect -> NO_CHANGE_REQUIRED
confirmed current drift -> REPAIR
unsafe or unrecoverable evidence/access -> BLOCKED
```

Do not create repository objects to test write access. **Write never probes.**

## Stable internal identifiers

Project-owned profile names are unversioned semantic names. Do not add decorative `@1/@2`, `/v1`, fake fixture/model versions, or similar pseudo-version suffixes. Preserve real external standard/runtime versions when genuinely applicable.

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

repository state
  -> daily / weekly / monthly maintenance
       └─ current-document / calendar / stage / delivery reconciliation
```

## Epistemic invariants

```text
claim indexed != claim true
evidence linked != evidence sufficient
structured verification != external scientific verification
heuristic score != probability
runtime-policy pass != truth
claim transfer != acceptance
identity ambiguity != scientific contradiction
conflict preservation != conflict adjudication
assertion basis != correctness
coverage != quality
coverage ratio != probability
R1 != R3
```

Never silently remove conflicts, upgrade audit states, convert heuristic scores into probabilities, authenticate a provider from adapter prose, or manufacture a missing requested claim ID.

## Provider identity

`LLMProvider.describe()` may contain only metadata actually known by the integration.

- unknown vendor/model/version -> `null` or omitted;
- never infer model identity from prompt style, class name, environment-variable name, or marketing copy;
- MockProvider remains a synthetic fixture;
- provider descriptions preserve assertion basis;
- automatic AI detection is not part of the canonical path.

## Claim verification / transfer

`core/claim_audit.py` records audit dimensions, not scientific verdicts. Allowed structural states do not imply `verified=true`.

`core/claim_transfer.py` may select existing claim records for downstream handoff, but transfer is not acceptance. Preserve source/evidence refs, audit state, conflicts, score semantics, and non-inheritance constraints.

## Assertion basis / coverage / score

Never upgrade basis into correctness. Coverage remains dimensional and does not become provenance soundness, scientific validity, probability, or evidence sufficiency. `aggregate_score` remains `null` absent a separately validated evaluation regime.

`[0,1]` alone is not probability semantics; convergence is not certainty; score movement is not a Bayesian update by default.

## Provenance / trace / policy

`core/provenance.py` is PROV-aligned project JSON, not PROV-O RDF conformance. `core/run_tracer.py` is project JSONL tracing, not OpenTelemetry export or a tamper-proof ledger.

Machine behavior comes from implemented checks and explicit parameters. Human-readable rule text is documentation only. Unknown checks fail explicitly.

## Evidence-stack separation

```text
trace -> chronology
checkpoint -> recovery state
provenance -> lineage
claim audit -> claim observations/basis/coverage
claim transfer -> selected portable claim handoff
evidence envelope -> compact run-level handoff + ref coverage
```

Do not merge them into one proof object.

## Coding-agent provenance

1. Jules/Codex/other task descriptions, PR bodies, summaries, framework comparisons, and completion claims are proposal/delivery metadata, not automatic current authority.
2. Historical `tests passed`, engine execution, convergence, `fully aligned`, `complete`, or similar assertions require current re-verification before reuse.
3. Structured JSON, verifier roles, gatekeepers, validators, or confidence networks must not be promoted rhetorically into scientific verification, probability, or certainty.
4. Later `main` or active contracts supersede an old narrative through current evidence; preserve the old PR as history.

## Maintenance cadence

The active maintenance system is jointly owned by:

```text
docs/03-maintenance-and-audit/DOCUMENT_STATUS.md
docs/03-maintenance-and-audit/MAINTENANCE_CADENCE.md
docs/03-maintenance-and-audit/README.md
docs/03-maintenance-and-audit/independent-gpt/README.md
maintenance/cadence.yaml
core/maintenance_cadence.py
```

The `.py` scanner is executable implementation. It is not changed merely because governance prose changes, and its source/config inspection is not execution evidence.

Local scanner:

```bash
python core/maintenance_cadence.py daily
python core/maintenance_cadence.py weekly
python core/maintenance_cadence.py monthly --as-of YYYY-MM-DD
```

Daily maintenance corrects demonstrated runtime/claim/evidence/profile/governance drift only and permits `NO_CHANGE_REQUIRED` without branch/PR churn.

Weekly maintenance reconciles implementation, Manifest, validators, active contracts, README/Architecture, Agent/Contributor/Customization guidance, examples, document status, maintenance config/records, checker ownership, and cross-repository profile names.

Monthly/phase-close derives calendar/phase status from the actual date and never converts closure into scientific validation or reproduction.

If Daily and Weekly own the same real correction, use one branch and one final Draft PR whenever practical.

## Execution evidence

```text
scanner/checker source present != executed
executed != passed
passed != scientific validity
historical pass != current pass
contract inspection != runtime verification
```

Unrun checks are `NOT_EXECUTED`. Unobserved scheduler/workflow execution is `EXECUTION_NOT_OBSERVED` when material.

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

References and transfers are not runtime imports or inherited truth claims.

## Experimental modules and R3

Experimental modules remain experimental until deliberately integrated; metaphorical names are not capability evidence.

Metadata, checkpoints, provenance, provider disclosure, coverage, claim audit/transfer, maintenance reports, demonstrations, and hash baselines never count as independent reproduction. R3 requires an actual separate rerun plus a declared comparison criterion.

## Delivery boundary

For a confirmed maintenance repair:

1. branch from the exact observed current `main`;
2. synchronize owning control surfaces and true dependencies only;
3. inspect the aggregate branch diff;
4. refresh current-main/open-PR overlap;
5. record executed and unexecuted checks separately;
6. open one bounded **Draft PR**;
7. stop for maintainer review.

Do not auto-merge, force-push, or write maintenance repairs directly to `main`. Final doctrine and merge authority remains with the maintainer.

## Governance boundary

Do not add GitHub Actions, CI, CodeQL, dependency bots, branch-protection assumptions, or merge-gate architecture as ordinary repository maintenance.

Do not publish private Jules prompts, repository memory, hidden reasoning, credentials, or unrelated operator context. Public governance may preserve the effect of a rule without copying private control text.
