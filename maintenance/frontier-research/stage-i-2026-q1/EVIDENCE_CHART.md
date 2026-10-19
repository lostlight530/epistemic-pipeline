# Frontier Research Stage I / 2026-Q1 — structured evidence chart
- Extracted 2026-10-19; no invented flow counts, effect size or universal quality score.
| Versioned object | Direct publisher observation | Research interpretation | Competing interpretation / limitation |
|---|---|---|---|
| I-O1 / v0.7.0 | Agents SDK changes nested handoff history to opt-in and introduces a multi-MCP-server manager. | Run history and connected tool surfaces are part of what an evaluator can observe; SDK defaults should be versioned. | No local SDK run, MCP connection or historical trace was observed. |
| I-O2 / v0.8.0 | Agents SDK introduces needs_approval, tool interruptions and serialized RunState approve/reject/resume. | An attempted action, pending approval, rejection, and executed tool effect are different transition/evidence states. | Feature examples are not a tested guarantee of application policy safety. |
| I-O3 / v0.12.1 | Agents SDK records a fix preserving explicit rejection messages across resumed approvals. | A rejection message can influence future planning; a Boolean outcome is insufficient to reconstruct why an action was denied. | No target RunState replay or confidentiality review was executed. |
Finding class: upstream version statement supported by one publisher-family source; downstream execution, independence and current repository drift remain `NOT_ASSESSED`.
