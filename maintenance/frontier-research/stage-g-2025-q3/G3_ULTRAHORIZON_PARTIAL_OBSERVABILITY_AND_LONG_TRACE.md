# G3 — UltraHorizon: Partial Observability and Very Long Agent Traces

## Question
What changes when evaluation tasks are long enough and partially observable enough that memory, planning, and intermediate state dominate the result?

## Object
- Research object: UltraHorizon
- arXiv: `2509.21766`
- Publication window: late September 2025
- Source type: long-horizon agent benchmark paper
- Accessed: 2026-09-26

## Primary source
- https://arxiv.org/abs/2509.21766

## Reported evidence
The paper describes long-horizon, partially observable tasks whose standard configurations can require very large context and many tool calls, with heavier instances extending to hundreds of tool calls. It frames sustained planning, memory, exploration, and tool management as central to performance and reports a material gap between agent and human performance in its evaluation.

This Stage uses the paper as a research object; no benchmark rollout was reproduced.

## Interpretation
The trajectory has now become long enough that "the transcript" and "the state" are no longer interchangeable.

```text
partial observation
-> internal/retained memory state
-> hypothesis / plan
-> tool action
-> new observation
-> memory update
-> plan revision
-> ... repeated many times ...
-> bounded outcome
```

A long trace raises evidence questions that short tasks can hide:
- which facts were still available when a decision was made;
- whether memory was stale, compressed, or lost;
- whether a plan was revised because of evidence or drift;
- which tool call changed the world state;
- whether the final success/failure can be attributed to one identifiable transition.

## Boundary
Trace length is not trace quality. Large context/tool-call counts do not by themselves establish competent reasoning, and benchmark partial observability is not proof of production-world equivalence.

## Finding
`G3_FINDING`: by late Q3 2025, long-horizon evaluation makes temporal evidence and memory state first-class: an epistemic record must preserve not just what the agent eventually answered, but what it could observe, remember, and justify at each consequential transition.
