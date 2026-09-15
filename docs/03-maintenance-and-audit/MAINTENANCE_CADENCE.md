# Maintenance Cadence — epistemic-pipeline

**Status:** active maintenance contract  
**Calibrated:** 2026-09-15  
**Current closed stage:** 2026-08-24 through 2026-08-31

This contract separates daily, weekly, and monthly maintenance for the research-execution and evidence layer. It is not a scheduler, scientific-review authority, or GitHub merge gate.

## Authority recovery before every pass

Use the most specific current subject authority rather than document date or legacy path placement:

```text
current main implementation
> current machine-readable capability contract / schema / configuration for the subject
> active docs/02-examples-and-contracts/RESEARCH_CONTRACT.md and active specialized contract for the subject
> operational examples / configuration / test evidence for supported use
> README / docs/01-source-and-explanation/ARCHITECTURE.md / current explanatory documentation
> maintenance / audit / reconciliation evidence
> historical snapshots / superseded plans / PR-task narratives
```

The historical `docs/03-maintenance-and-audit/history/JULES_CORRECTION_RECORD.md` records the 2026-09-06 correction boundary for earlier coding-agent task/PR narratives. Its historical authority-order wording does not override the current subject-scoped order above.

## Cadence model

```text
daily
  local runtime / claim / evidence drift
        ↓
weekly
  cross-day evidence-stack and document-authority reconciliation
        ↓
monthly or explicit phase-close
  calendar baseline / complete evidence-document inventory / deprecation review
```

## Daily

Required checks:

- start from current `main`;
- use `docs/03-maintenance-and-audit/DOCUMENT_STATUS.md` to identify current authoritative documentation;
- read the latest relevant dated repair/current maintenance record before older snapshots or PR narratives;
- verify claim-verification, claim-transfer, Evidence Envelope, provider disclosure, trace/checkpoint/provenance names remain consistent;
- preserve claim identity/origin ambiguity rather than collapsing it;
- preserve unknown provider/model/version values as unknown;
- preserve heuristic score semantics as non-probability;
- preserve conflicts during claim transfer;
- keep unsupported composite quality scores absent or null;
- incorporate new research only when it changes a real evidence-contract decision;
- treat Jules/Codex/other coding-agent PR/task narratives and historical test/completeness claims as proposal/delivery metadata unless current evidence independently supports them;
- create at most one final maintenance PR for the repository.

Daily maintenance must not rewrite historical snapshots or historical PR prose, promote audit states into scientific verdicts, convert coverage into provenance soundness, treat structured output as scientific verification, or add GitHub-native merge governance.

Historical `tests passed`, engine-run, convergence, `fully aligned`, or comparable agent assertions require current re-verification before being reused as current facts.

## Weekly

Weekly maintenance includes daily checks plus complete current-evidence reconciliation:

- implementation ↔ Manifest ↔ active contracts under `docs/02-examples-and-contracts/`;
- root README / `docs/01-source-and-explanation/ARCHITECTURE.md` / Contributor / Customization / Examples consistency;
- `docs/03-maintenance-and-audit/DOCUMENT_STATUS.md` against files actually present;
- current dated correction/maintenance records;
- trace / checkpoint / provenance / claim audit / claim transfer / Evidence Envelope separation;
- cross-repository profile names;
- provider assertion basis and unknown-value handling;
- score/interval semantics;
- previous seven days of maintenance/correction history and historical snapshots without rewriting them;
- frontier calibration freshness;
- whether coding-agent narratives are being treated as current runtime/scientific authority without current evidence;
- canonical SHA-256 baseline when the local scanner is used.

### Daily + Weekly coalescing

If one real maintenance pass serves as both Daily and Weekly reconciliation, prefer one branch and one final PR for the combined work.

```text
one evidence-backed correction
!= two required PRs because two cadence labels apply
```

Both scopes must be documented; duplicate cosmetic changes or duplicate PRs must not be manufactured.

## Monthly / explicit phase-close

Monthly maintenance performs the strongest evidence-stack review while remaining non-destructive.

For the closed August stage:

```text
as_of: 2026-08-31
calendar_month: calendar-month-close
stage: closed
```

On and after 2026-09-01 that stage remains closed; post-stage hardening and later maintenance do not reopen it.

Before the natural September month boundary, a monthly maintenance pass records `month-to-date`; it must not be represented as a calendar-month close.

Historical consolidation and closed-stage inventory lives under `docs/03-maintenance-and-audit/history/`.

## Deterministic local scanner

```bash
python core/maintenance_cadence.py daily
python core/maintenance_cadence.py weekly
python core/maintenance_cadence.py monthly --as-of 2026-08-31
```

Optional report output:

```bash
python core/maintenance_cadence.py daily --as-of 2026-09-06 --output output/evidence-maintenance-2026-09-06.json
```

The scanner matches its declared repository-local scope: configured paths remain repository-relative; absolute paths, `..`, and resolutions outside the repository fail closed; repository-local config identity is SHA-256-bound; duplicate paths are warnings; and report output is only written when explicitly requested.

```text
inspected_files_mutated: false
report_output_write_requested: true | false
report_output_inside_repository: true | false | null
```

The scanner does not execute the research workflow, call an LLM, run tests, verify citations, judge evidence sufficiency, evaluate provenance soundness, scientifically adjudicate identity ambiguity, or validate historical Jules PR/task claims.

## Dated maintenance evidence

The first complete worked example remains:

```text
maintenance/FIRST_COMPLETE_CADENCE_DEMONSTRATION_2026_08_31.md
```

The post-stage repair is:

```text
maintenance/POST_STAGE_REPAIR_2026_09_01.md
```

The previous Daily/Weekly governance reconciliation is:

```text
maintenance/DAILY_WEEKLY_RECONCILIATION_2026_09_06.md
```

The current Daily/Weekly/month-to-date reconciliation record is:

```text
maintenance/DAILY_WEEKLY_MONTH_TO_DATE_RECONCILIATION_2026_09_13.md
```

These are dated maintenance records, not runtime or scientific-validation evidence. The 2026-09-13 record keeps `MANIFEST.yaml` / external-research capability calibration distinct from maintenance-layer freshness unless actual evidence-contract semantics change.

## Historical evidence

Closed-stage consolidations, frontier alignment, and the dated Jules correction live under `docs/03-maintenance-and-audit/history/`. Their paths changed; their point-in-time claims did not.

## External calibration

Long-horizon and scientific-agent evaluation increasingly shows that terminal results alone can hide intermediate errors or structural ambiguity. Current Google Jules guidance similarly preserves a human-review boundary for generated code and evaluates agent insight quality rather than assuming confidence equals correctness.

These sources calibrate maintenance design only. They do not establish optimal maintenance frequency, provenance soundness, scientific-review authority, or any historical Jules change as false.

## Shared boundaries

```text
maintenance clean != scientific validity
weekly consistency != evidence sufficiency
calendar-month close != reproduction
identity ambiguity != scientific contradiction
coverage != provenance soundness
heuristic score != probability
structured output != scientific verification
provenance != truth
report written != evidence validated
agent task / PR narrative != current repository truth
claimed test pass != current runtime verification
cadence label != requirement for duplicate PR churn
maintenance calibration != evidence-contract transition
path relocation != semantic change
```
