# Customization Guide for Agents and Bots

Welcome, AI Agent or Bot developer!

If you have cloned the **Epistemic Pipeline**, you are looking at a highly advanced, State-Machine Driven Dynamic Epistemic Engine. This pipeline is fundamentally different from static, sequential Agent frameworks (e.g., passing text from Agent A to Agent B). It uses **DAG topology for execution**, **Dynamic Role Binding**, and a **Bayesian Confidence Network** to converge truth and eliminate LLM hallucination.

This guide is written specifically for you (or the LLM powering you) to understand how to customize, extend, and adapt this framework for your specific domain (e.g., Legal Case Review, Financial Audit, Medical Literature Synthesis, Codebase Analysis).

---

## 1. How to Define Your Own Value System (Epistemic Framework)
You do not need to rewrite the core engine. The framework's core values—what is considered "true", "conflicting", or "high quality"—are completely decoupled and pluggable.

*   **File to edit:** `validators/epistemic.rules.yaml`
*   **Action:** Define the global rules for your specific domain here. For example, if you are analyzing code, you can add a rule: `id: strict_type_check`, `severity: blocker`.
*   **Why:** The `Gatekeeper` (`core/gatekeeper.py`) reads this file to intercept bad outputs globally before moving to the next state.

## 2. How to Modify the Pipeline Logic (State Machine & DAG)
The execution order is NOT hardcoded in Python. It is computed dynamically via a Directed Acyclic Graph (DAG) and transitions.

*   **Files to edit:** `graphs/*.yaml` (e.g., `graphs/linear.yaml`, `graphs/parallel.yaml`)
*   **Action:** Add, remove, or reorder nodes in the `nodes` array. Change their `dependencies`. The `DependencyGraph` will automatically calculate parallel execution groups and critical paths.
*   **Dynamic Fallbacks:** If you want a state to loop back upon failure (e.g., going back to `discover` if `verify` fails), edit the specific state file in `states/*.yaml` and update the `transitions` section.

## 3. How to Create or Modify Roles (The Brains)
The system uses "Roles" as capability constraint packs, dynamically mounted to the LLM when entering a specific state.

*   **Files to edit:** `roles/*.md`
*   **Action:** If you are analyzing financial reports, you might want to create a `roles/quant_analyst.md`.
*   **Structure Requirement:** Every role file MUST clearly define three things:
    1.  `Capability Domains`: What the role can do.
    2.  `Core Constraints`: What is strictly forbidden (e.g., "Do not hallucinate revenue numbers").
    3.  `Output Structure`: What JSON/YAML schema must be returned.
*   **Binding:** Once created, bind your new role in the corresponding state file (e.g., `states/analyze.yaml` under `role_bindings: primary: quant_analyst`).

## 4. How to Connect a Real LLM (Execution Harness)
Currently, `core/llm_harness.py` uses simulated outputs (`mock=True`) to demonstrate the structure. To plug in a real LLM (OpenAI, Claude, Llama, etc.):

*   **File to edit:** `core/llm_harness.py`
*   **Action:** Locate the `execute` function. Replace the `if mock:` block with actual API calls to your preferred LLM provider.
*   **Crucial Step:** You MUST enforce structured outputs (e.g., using OpenAI's `response_format: { "type": "json_object" }` or libraries like `instructor` / `pydantic`). The framework's `Gatekeeper` will aggressively reject unstructured or malformed text.

## 5. How to Tune the Confidence Network
The crown jewel of this pipeline is the mathematical convergence of knowledge via Belief Propagation.

*   **File to edit:** `core/confidence_net.py`
*   **Action:** You can tune the `threshold` (how strictly it converges) or `max_iterations` in the `__init__` method. You can also modify the logic in `_propagate_once` to change how different edge types (`supports`, `contradicts`, `derives`) affect the weights.

---

## 🛠️ Quick Checklist for Your First Custom Run
1. [ ] Define your custom roles in `roles/*.md`.
2. [ ] Map out your state flow and quality gates in `states/*.yaml`.
3. [ ] Connect your DAG dependencies in `graphs/my_custom_graph.yaml`.
4. [ ] Implement actual LLM API calls in `core/llm_harness.py`.
5. [ ] Run: `python3 core/engine.py run graphs/my_custom_graph.yaml`.

*End of Guide. You are now ready to build a hallucination-free, mathematically rigorous cognitive pipeline.*
