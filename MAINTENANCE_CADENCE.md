# Maintenance Cadence — epistemic-pipeline

**Status:** active maintenance contract  
**Calibrated:** 2026-09-06  
**Current closed stage:** 2026-08-24 through 2026-08-31

This contract separates daily, weekly, and monthly maintenance for the research-execution and evidence layer. It is not a scheduler, scientific-review authority, or GitHub merge gate.

## Authority recovery before every pass

```text
current main implementation
> MANIFEST.yaml and current machine-readable configuration
> latest dated repair / current maintenance record
> DOCUMENT_STATUS.md
> AGENTS.md
> active evidence/scientific-integrity contracts
> this cadence contract / maintenance configuration
> Architecture / README
> historical consolidation snapshots
> historical PR / task narratives
```

Read `JULES_CORRECTION_RECORD.md` before using historical Jules task/PR text as evidence of current behavior.

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
- use `DOCUMENT_STATUS.md` to identify current authoritative documentation;
- read the latest dated repair/current maintenance record before older snapshots or PR narratives;
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

- implementation ↔ Manifest ↔ Research Contract ↔ Claim Audit Contract ↔ Claim Transfer Contract;
- README / Architecture / Contributor / Customization / Examples consistency;
- `DOCUMENT_STATUS.md` against files actually present;
- current correction/maintenance records, including `JULES_CORRECTION_RECORD.md`;
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

### 2026-09-01 portability and scope repair

The scanner matches its declared repository-local scope:

- canonical / scan / governance paths must be repository-relative;
- absolute paths, `..`, and resolutions outside the repository root fail closed as error findings;
- historical inventory uses repository-relative paths rather than machine-local absolute paths;
- repo-local configuration is recorded by relative path plus `configuration_file_sha256`;
- external configuration is labeled external without embedding the machine's full absolute path;
- duplicate configured paths are warnings;
- `repository_scope_enforced: true` is explicit.

The accurate write boundary remains:

```text
inspected_files_mutated: false
report_output_write_requested: true | false
report_output_inside_repository: true | false | null
```

The scanner does not rewrite inspected evidence/code/configuration/history. It may write only the report path explicitly requested by the caller.

## Scanner checks

The scanner reports configured paths, scope violations, forbidden governance paths, decorative internal profile versions, Manifest freshness, configuration identity, optional canonical hashes, historical snapshots, calendar-month status, and configured stage status.

It does not execute the research workflow, call an LLM, run tests, verify citations, judge evidence sufficiency, evaluate provenance soundness, scientifically adjudicate identity ambiguity, or validate historical Jules PR/task claims.

## First complete cadence demonstration

The first complete worked example remains:

```text
maintenance/FIRST_COMPLETE_CADENCE_DEMONSTRATION_2026_08_31.md
```

It is reference material, not a pre-asserted clean scanner result.

The current Daily/Weekly governance reconciliation is:

```text
maintenance/DAILY_WEEKLY_RECONCILIATION_2026_09_06.md
```

It is a dated maintenance record, not runtime or scientific-validation evidence.

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
```
