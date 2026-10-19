# Source and Research-Object Register — I/2026-Q1

- Repository: `lostlight530/epistemic-pipeline`; constructed 2026-10-19; source cutoff 2026-10-19.
- Identity rule: **tagged upstream release object != release-note report**. Official release note and tag belong to one origin; separate release versions remain separate objects. Version existence does not entail local execution.

| Object ID | Canonical release object | GitHub release publication | Source ID | Original source family | URL | What is established / not established |
|---|---|---|---|---|---|---|
| O1 | openai/openai-agents-python `v0.7.0` | 2026-01-23 | S1 | `openai/openai-agents-python` | https://github.com/openai/openai-agents-python/releases/tag/v0.7.0 | Published upstream release note describing nested handoff history switches to opt-in; NOT local deployment or reproduction |
| O2 | openai/openai-agents-python `v0.8.0` | 2026-02-05 | S2 | `openai/openai-agents-python` | https://github.com/openai/openai-agents-python/releases/tag/v0.8.0 | Published upstream release note describing human-in-the-loop tool approvals, interrupts and serializable RunState resume; NOT local deployment or reproduction |
| O3 | openai/openai-agents-python `v0.10.3` | 2026-03-02 | S3 | `openai/openai-agents-python` | https://github.com/openai/openai-agents-python/releases/tag/v0.10.3 | Published upstream release note describing immutable tool-invocation metadata and tool context accessors on run results; NOT local deployment or reproduction |

- Search/access date: 2026-10-19; release dates are upstream publication dates, not this repository's execution dates.
- Shared-origin dependence: any repeated releases from the same project remain **same-origin** even if separated by months. No independent reproducer linked/validated in this register.
- Source selection: purposefully chosen research objects from listed families; `SOURCE_BOUNDED` only, no exhaustive project-history claim.
