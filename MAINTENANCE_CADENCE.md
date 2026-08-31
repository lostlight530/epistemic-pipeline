# Maintenance Cadence — epistemic-pipeline

**Status:** active maintenance contract  
**Calibrated:** 2026-09-01  
**Current closed stage:** 2026-08-24 through 2026-08-31

This contract separates daily, weekly, and monthly maintenance for the research-execution and evidence layer. It is not a scheduler, scientific-review authority, or GitHub merge gate.

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
- verify claim-verification, claim-transfer, Evidence Envelope, provider disclosure, trace/checkpoint/provenance names remain consistent;
- preserve claim identity/origin ambiguity rather than collapsing it;
- preserve unknown provider/model/version values as unknown;
- preserve heuristic score semantics as non-probability;
- preserve conflicts during claim transfer;
- keep unsupported composite quality scores absent or null;
- incorporate new research only when it changes a real evidence-contract decision;
- create at most one final maintenance PR for the repository.

Daily maintenance must not rewrite historical snapshots, promote audit states into scientific verdicts, convert coverage into provenance soundness, or add GitHub-native merge governance.

## Weekly

Weekly maintenance includes daily checks plus complete current-evidence reconciliation:

- implementation ↔ Manifest ↔ Research Contract ↔ Claim Audit Contract ↔ Claim Transfer Contract;
- README / Architecture / Contributor / Customization / Examples consistency;
- `DOCUMENT_STATUS.md` against files actually present;
- trace / checkpoint / provenance / claim audit / claim transfer / Evidence Envelope separation;
- cross-repository profile names;
- provider assertion basis and unknown-value handling;
- score/interval semantics;
- previous seven days of historical snapshots without rewriting them;
- frontier calibration freshness;
- canonical SHA-256 baseline when the local scanner is used.

## Monthly / explicit phase-close

Monthly maintenance performs the strongest evidence-stack review while remaining non-destructive.

For the closed August stage:

```text
as_of: 2026-08-31
calendar_month: calendar-month-close
stage: closed
```

On 2026-09-01 that stage remains closed; post-stage hardening does not reopen it.

## Deterministic local scanner

```bash
python core/maintenance_cadence.py daily
python core/maintenance_cadence.py weekly
python core/maintenance_cadence.py monthly --as-of 2026-08-31
```

Optional report output:

```bash
python core/maintenance_cadence.py daily --as-of 2026-09-01 --output output/evidence-maintenance-2026-09-01.json
```

### 2026-09-01 portability and scope repair

The scanner now matches its declared repository-local scope:

- canonical / scan / governance paths must be repository-relative;
- absolute paths, `..`, and resolutions outside the repository root fail closed as error findings;
- historical inventory uses repository-relative paths rather than machine-local absolute paths;
- repo-local configuration is recorded by relative path plus `configuration_file_sha256`;
- external configuration is labeled external without embedding the machine's full absolute path;
- duplicate configured paths are warnings;
- `repository_scope_enforced: true` is explicit.

The previous “does not modify repository files” wording was too broad because explicit `--output` writes a report. The accurate boundary is:

```text
inspected_files_mutated: false
report_output_write_requested: true | false
report_output_inside_repository: true | false | null
```

The scanner does not rewrite inspected evidence/code/configuration/history. It may write only the report path explicitly requested by the caller.

## Scanner checks

The scanner reports configured paths, scope violations, forbidden governance paths, decorative internal profile versions, Manifest freshness, configuration identity, optional canonical hashes, historical snapshots, calendar-month status, and configured stage status.

It does not execute the research workflow, call an LLM, run tests, verify citations, judge evidence sufficiency, evaluate provenance soundness, or scientifically adjudicate identity ambiguity.

## First complete cadence demonstration

The first complete worked example remains:

```text
maintenance/FIRST_COMPLETE_CADENCE_DEMONSTRATION_2026_08_31.md
```

It is reference material, not a pre-asserted clean scanner result.

## External calibration

Long-horizon and scientific-agent evaluation increasingly shows that terminal results alone can hide intermediate errors or structural ambiguity. The maintenance response is narrow: make scope, identities, ambiguity, and write behavior inspectable rather than inferred.

These sources calibrate maintenance design only. They do not establish optimal maintenance frequency, provenance soundness, or scientific-review authority.

## Shared boundaries

```text
maintenance clean != scientific validity
weekly consistency != evidence sufficiency
calendar-month close != reproduction
identity ambiguity != scientific contradiction
coverage != provenance soundness
heuristic score != probability
provenance != truth
report written != evidence validated
```
