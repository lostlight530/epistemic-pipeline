# Maintenance Cadence — epistemic-pipeline

**Status:** active maintenance contract  
**Calibrated:** 2026-09-17  
**Current closed stage:** 2026-08-24 through 2026-08-31

This contract separates Daily, Weekly, and Monthly maintenance for the research-execution and evidence layer. It is not a scheduler, scientific-review authority, provider authenticator, or GitHub merge gate.

## Authority recovery before every pass

For maintenance-control recovery use:

```text
current merged main implementation
> MANIFEST.yaml / validators / current machine-readable configuration for the subject
> latest relevant dated repair or current maintenance record
> docs/03-maintenance-and-audit/DOCUMENT_STATUS.md
> AGENTS.md
> active subject-specific contracts
> maintenance/cadence.yaml and this cadence contract
> current Architecture / README explanation
> historical snapshots / superseded plans / PR-task narratives
```

For a claim/evidence/runtime semantic question, use the most specific implementation, machine rule, and active subject contract. Maintenance recency is not scientific authority.

## Maintenance identity and idempotency

Record when applicable:

```text
repository
owning surface / task
logical period or evidence window
producer / maintainer
exact base revision
run identity when available
```

Before any write, inspect open PRs and live branches for the same owning surface and logical period.

```text
overlap -> COORDINATE
no confirmed defect -> NO_CHANGE_REQUIRED
confirmed current drift -> REPAIR
unsafe or unrecoverable evidence/access -> BLOCKED
```

`NO_CHANGE_REQUIRED` follows real inspection. Do not create an activity-only branch or PR. **Write never probes.**

## Cadence model

```text
daily
  local runtime / claim / evidence drift
        ↓
weekly
  cross-day evidence-stack / authority / maintenance reconciliation
        ↓
monthly or explicit phase-close
  calendar baseline / complete current evidence-document inventory
```

Cadence labels do not require duplicate delivery. One real correction may satisfy Daily and Weekly scope in one branch and one Draft PR.

## Daily

Required behavior:

- start from current merged `main`;
- use `DOCUMENT_STATUS.md` to identify current authority and retained history;
- read the latest relevant dated repair/current maintenance record before older snapshots when relevant;
- inspect claim-verification, claim-transfer, Evidence Envelope, provider disclosure, trace/checkpoint/provenance names, validator rules, and maintenance ownership for drift;
- preserve claim identity/origin ambiguity rather than collapsing it;
- preserve unknown provider/model/version values as unknown;
- preserve heuristic-score non-probability semantics;
- preserve conflicts during transfer;
- keep unsupported composite quality scores absent or null;
- treat coding-agent PR/task narratives as proposal/delivery metadata unless current evidence independently supports them;
- record checks actually executed separately from checks merely available;
- create at most one bounded Draft PR when a real repair exists.

Daily maintenance must not rewrite historical snapshots or PR prose, promote audit states into scientific verdicts, convert coverage into provenance soundness, treat structured output as scientific verification, or manufacture a change merely to satisfy cadence.

## Weekly

Weekly maintenance includes Daily checks plus complete current-evidence reconciliation:

- implementation ↔ `MANIFEST.yaml` ↔ validators ↔ active evidence contracts;
- README / Architecture / Contributor / Customization / Examples consistency;
- `DOCUMENT_STATUS.md` against files actually present;
- current maintenance configuration, recovery kernel, and operator/delivery surfaces;
- trace / checkpoint / provenance / claim audit / claim transfer / Evidence Envelope separation;
- provider assertion basis and unknown-value handling;
- score/interval semantics;
- previous maintenance/correction window and retained historical snapshots without rewriting them;
- cross-repository handoff names;
- whether agent narratives are being treated as current runtime/scientific authority without current evidence;
- SHA-256 baselines only when the local scanner is actually used.

### Daily + Weekly coalescing

```text
one evidence-backed correction
!= two required PRs because two cadence labels apply
```

## Monthly / explicit phase-close

Monthly maintenance performs the strongest non-destructive evidence-stack review.

Required behavior:

- derive calendar status from the actual date;
- use `month-to-date` before natural month close and `calendar-month-close` only at natural month close;
- reconcile the complete current document/evidence-control set;
- inventory historical records non-destructively;
- review current / experimental / proposed / not-integrated states;
- verify that structural states have not been rhetorically promoted into truth verdicts;
- never convert calendar closure into scientific validation or reproduction.

The August 2026 evidence-infrastructure phase remains closed after 2026-08-31.

## Deterministic local scanner

```bash
python core/maintenance_cadence.py daily
python core/maintenance_cadence.py weekly
python core/maintenance_cadence.py monthly --as-of YYYY-MM-DD
```

Optional report output:

```bash
python core/maintenance_cadence.py daily --as-of YYYY-MM-DD --output output/evidence-maintenance-YYYY-MM-DD.json
```

The scanner enforces its declared repository-local structural scope. It does not execute the research workflow, call an LLM, run tests, verify citations, judge evidence sufficiency, evaluate provenance soundness, scientifically adjudicate identity ambiguity, inspect GitHub PR ownership, or validate historical Jules claims.

## Execution evidence

```text
scanner source present != scanner executed
scanner executed != scanner passed
scanner passed != scientific validity
historical pass != current pass
structured state != scientific verdict
contract inspection != runtime verification
```

If a relevant check was not run, record `NOT_EXECUTED`. If execution itself was not observed, use `EXECUTION_NOT_OBSERVED` when material.

## Dated maintenance evidence

The August demonstration, 2026-09-01 repair, 2026-09-06 reconciliation, frontier refresh, and 2026-09-13 month-to-date reconciliation remain dated point-in-time evidence. They are not silently rewritten into current runtime or scientific-validation evidence.

`MANIFEST.yaml` / external-research capability calibration changes only when actual evidence-contract semantics or machine capability change. Maintenance freshness alone does not authorize that bump.

## History and correction discipline

Preserve closed-stage consolidations, frontier alignment, Jules correction, and superseded design evidence.

```text
historical snapshot != current contract
historical != invalid
later success != earlier success
correction != history rewrite
path relocation != semantic change
```

Correct forward through a current owning file or later dated reconciliation.

## Delivery contract

When a repair is confirmed:

1. branch from the exact observed current `main`;
2. modify only owning control surfaces and true synchronized dependencies;
3. inspect the aggregate `main...branch` diff;
4. refresh current-main and overlap state;
5. record executed and unexecuted checks separately;
6. open one bounded **Draft PR**;
7. stop for maintainer review.

Do not auto-merge, force-push, or write maintenance repairs directly to `main`.

## Shared boundaries

```text
maintenance clean != scientific validity
weekly consistency != evidence sufficiency
calendar-month close != reproduction
identity ambiguity != scientific contradiction
claim indexed != claim true
evidence linked != evidence sufficient
coverage != provenance soundness
heuristic score != probability
runtime-policy pass != truth
claim transfer != acceptance
structured output != scientific verification
report written != evidence validated
agent task / PR narrative != current repository truth
claimed test pass != current runtime verification
cadence label != duplicate PR requirement
maintenance calibration != evidence-contract transition
Draft PR != validation success
```
