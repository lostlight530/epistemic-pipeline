# Source and Research-Object Register — J/2026-Q2

- Repository: `lostlight530/epistemic-pipeline`; constructed 2026-10-19; source cutoff 2026-10-19.
- Identity rule: **tagged upstream release object != release-note report**. Official release note and tag belong to one origin; separate release versions remain separate objects. Version existence does not entail local execution.

| Object ID | Canonical release object | GitHub release publication | Source ID | Original source family | URL | What is established / not established |
|---|---|---|---|---|---|---|
| O1 | openai/openai-agents-python `v0.14.0` | 2026-04-15 | S1 | `openai/openai-agents-python` | https://github.com/openai/openai-agents-python/releases/tag/v0.14.0 | Published upstream release note describing beta Sandbox Agents with manifests, mounts, snapshots, session resume and persisted workspace memory; NOT local deployment or reproduction |
| O2 | openai/openai-agents-python `v0.15.0` | 2026-05-01 | S2 | `openai/openai-agents-python` | https://github.com/openai/openai-agents-python/releases/tag/v0.15.0 | Published upstream release note describing ModelRefusalError surfaces refusal as explicit SDK state; NOT local deployment or reproduction |
| O3 | openai/openai-agents-python `v0.17.6` | 2026-06-19 | S3 | `openai/openai-agents-python` | https://github.com/openai/openai-agents-python/releases/tag/v0.17.6 | Published upstream release note describing pre-approval tool input guardrails; NOT local deployment or reproduction |

- Search/access date: 2026-10-19; release dates are upstream publication dates, not this repository's execution dates.
- Shared-origin dependence: any repeated releases from the same project remain **same-origin** even if separated by months. No independent reproducer linked/validated in this register.
- Source selection: purposefully chosen research objects from listed families; `SOURCE_BOUNDED` only, no exhaustive project-history claim.
