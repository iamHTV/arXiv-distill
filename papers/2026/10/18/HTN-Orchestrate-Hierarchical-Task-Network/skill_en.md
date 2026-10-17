# Skill: HTN-Orchestrate — Two-layer Planner/Orchestrator for multi-agent research
Source: 2610.22195v1 (HTN-Orchestrate)
Type: framework (multi-agent orchestration)

## When to use this skill
- A multi-agent task needs BOTH structured decomposition (dependencies between subtasks) AND adaptive execution (findings reshape the plan).
- Research/web-investigation pipelines: tasks where subtasks depend on each other's outputs ("analyze X" needs the output of "find X").
- Do NOT use when: the task is simple, 1–2 steps (ReAct suffices); there are no dependencies between subtasks (plain Agent Team is simpler); decomposition deeper than 2 levels is required (the paper caps depth at 2 — untested beyond that).

## Inputs required
- Task q + worker roles (research, verification) + tools (web search, retrieval, scholarly search, Python, file reading).
- Budgets: max depth (2), max children per node (4), max concurrent workers per leaf (3), max orchestration rounds per epoch (12), rebuild limit (1).
- A backbone model for the Planner/Orchestrator (high reasoning effort) + workers (low reasoning effort).

## Steps
1. Initialize the task network T = (V, Eh, Ed) with root = q, evidence summary M = ∅, epoch e = 0.
2. PlanOrExecute each ready planning leaf (pending, all prerequisites completed): consider the goal, task description, ancestors, and summaries of prerequisite results → either mark for direct execution, or expand into children + sibling dependency edges. Validate coverage of the parent and acyclicity; revise if either check fails. DEPENDENT subtasks: decompose ONLY AFTER prerequisite results return (result-informed planning).
3. Dispatch ready executable leaves to their Orchestrators in parallel (a wave). Each Orchestrator: receive context C_v (task, leaf objective, ancestors, prerequisite summaries); loop dispatch/wait/finish — dispatch selects roles and task-specific instructions based on current evidence (initial investigation → focused search or verification when a report reveals a gap or a disputed claim); progressive collection (follow-up while assignments remain active); finish → SynthesizeLeaf (summary, resolved/unresolved outcome, evidence references).
4. PropagateResults: record leaf results; recursively synthesize each parent whose children have ALL returned (AND semantics — a non-leaf synthesizes only after ALL children complete).
5. Check the root: if resolved → return the synthesized result. Otherwise settle/stop ongoing work, CollectEvidence extracts supported findings from completed AND partial reports into M; e+1; if e ≥ rebuild limit or budgets exhausted → synthesize the evidence so far and report unresolved requirements (do NOT treat stopping as success).
6. Rebuild: InitializeRoot(q, M) — a new network rooted at the original task, conditioned on the evidence summary M (planning context, NOT auto-marking subtasks complete); return to step 2.
7. Termination hygiene: the output always reflects the sufficiency of evidence; unresolved requirements are reported explicitly.

## Expected output
- A final answer + evidence references; internal stats: tree depth/leaves, executed leaf instances, worker invocations, orchestrator rounds, rebuild rate. Expected gains (paper, BrowseComp): +2.45pp vs Agent Team, +15.80pp vs ReAct; faster on 67.9% of shared successes (median ratio 0.699); concurrency 2.47 vs 1.70.

## Example application
- A solopreneur research task "analyze competitor X's pricing strategy": the Planner creates "collect pricing pages" → after the result returns, decompose "compare tiers" conditioned on the actual prices found (not guessed upfront); the leaf Orchestrator dispatches a researcher + verifier; if the root is unresolved after the wave (e.g., the pricing page fails to load), CollectEvidence retains candidate pages + rejected URLs and rebuilds with "find pricing via review sites". Expected: correct target, four leaves instead of five.

## Gotchas
- Do NOT decompose dependent subtasks upfront — ablation: −1.5pp accuracy, +4.79 minutes median, more invocations. Decompose AFTER prerequisite results exist.
- AND semantics is strict: a parent synthesizes only after ALL children complete — one stuck leaf drags the whole parent; use orchestrator-round and time budgets to bound it.
- Rebuilding is NOT restarting: evidence carryover (M) is planning context, not auto-completion — without retaining partial findings, a rebuild loses all progress (case Q501: correct "Serial Killer" vs wrong "Silent Night").
- Outcome = sufficiency of evidence, not "verifier invoked" or "workers stopped" — don't game the outcome field.
- Budgets are mandatory: depth 2, ≤4 children, ≤3 workers, ≤12 rounds, 1 rebuild — without them, network growth is unbounded.
- Workers at low reasoning effort, orchestration agents at high — a cost saving; do not invert.
- Decompositions must be validated for coverage and acyclicity — LLM-generated children can miss a parent aspect or create a dependency cycle.
- Tested on only one backbone (DeepSeek-V4.1-Flash) — validate on your model before production.
