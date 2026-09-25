# F3 — τ²-Bench Dual-Control State and Coordination Provenance

## Evidence
τ²-Bench was published 2025-06-09. It introduces a dual-control environment where both the AI agent and user can use tools to modify shared state. The Telecom domain is modeled as a Dec-POMDP, with a compositional task generator and a user simulator coupled to the environment. The work separates reasoning errors from communication/coordination errors through ablations.

Source: https://arxiv.org/abs/2506.07982

## Analysis
Stage E separated missing-information detection from solving. Stage F adds another distinction: the user is not only an information source but also an actor.

```text
agent action
+
user action
+
shared environment transition
-> trajectory state
```

Therefore actor identity, action authority and observed world state belong to evaluation provenance.

```text
conversation transcript
!= complete state-transition trace
successful outcome
!= reasoning-only success
```

## Outcome
`SUPPORTED_OBSERVATION / DIRECTLY_RELEVANT_TO_STATE_TRANSITION_BOUNDARY`
