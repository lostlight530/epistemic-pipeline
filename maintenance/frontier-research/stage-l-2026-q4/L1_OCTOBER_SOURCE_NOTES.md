# Frontier Research Stage L / 2026-Q4 — October Part candidate, OPEN
- Date 2026-10-19; status `IN_PROGRESS`; bounded to October 1–19, no quarter close.
## MCP annotations and compaction
- First-party source: [openai/openai-agents-python v0.24.0](https://github.com/openai/openai-agents-python/releases/tag/v0.24.0), released 2026-10-15.
- Observed: Agents SDK reports exposing converted MCP tool annotations and deferring automatic compaction for pending approvals.
- Analysis: Annotations are metadata, not permission; compaction must not erase the context that conditioned an unresolved approval.
- Limit: No local MCP or compaction replay performed.
- Research question: Can an annotation or compacted summary inherit tool authority?

Independent review and repository runtime were not performed. Later October/November/December sources require a new dated update.
