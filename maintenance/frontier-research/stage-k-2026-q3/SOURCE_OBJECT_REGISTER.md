# Source and Research-Object Register — K/2026-Q3

- Repository: `lostlight530/epistemic-pipeline`; constructed 2026-10-19; source cutoff 2026-10-19.
- Identity rule: **tagged upstream release object != release-note report**. Official release note and tag belong to one origin; separate release versions remain separate objects. Version existence does not entail local execution.

| Object ID | Canonical release object | GitHub release publication | Source ID | Original source family | URL | What is established / not established |
|---|---|---|---|---|---|---|
| O1 | openai/openai-agents-python `v0.19.0` | 2026-07-27 | S1 | `openai/openai-agents-python` | https://github.com/openai/openai-agents-python/releases/tag/v0.19.0 | Published upstream release note describing Programmatic Tool Calling with caller restrictions and Runner/approval integration; NOT local deployment or reproduction |
| O2 | modelcontextprotocol/modelcontextprotocol `2026-07-28` | 2026-07-28 | S2 | `modelcontextprotocol/modelcontextprotocol` | https://github.com/modelcontextprotocol/modelcontextprotocol/releases/tag/2026-07-28 | Published upstream release note describing stable 2026-07-28 MCP specification revision; NOT local deployment or reproduction |
| O3 | openai/openai-agents-python `v0.22.0` | 2026-08-19 | S3 | `openai/openai-agents-python` | https://github.com/openai/openai-agents-python/releases/tag/v0.22.0 | Published upstream release note describing redaction of blocked tool outputs from persisted replay and RunState usage isolation; NOT local deployment or reproduction |
| O4 | openai/openai-agents-python `v0.22.3` | 2026-09-17 | S4 | `openai/openai-agents-python` | https://github.com/openai/openai-agents-python/releases/tag/v0.22.3 | Published upstream release note describing conditional tool approvals aligned with validated tool arguments; NOT local deployment or reproduction |

- Search/access date: 2026-10-19; release dates are upstream publication dates, not this repository's execution dates.
- Shared-origin dependence: any repeated releases from the same project remain **same-origin** even if separated by months. No independent reproducer linked/validated in this register.
- Source selection: purposefully chosen research objects from listed families; `SOURCE_BOUNDED` only, no exhaustive project-history claim.
