# Skill: leafskill-retrieve-bind-select (leaf-level grounding layer for recursive agents)

Source: 2610.32412v1
Type: framework / workflow

## When to use this skill

- A recursive LLM agent calls the large host model too many times just to translate leaf tasks into executable actions.
- You want to reuse task–action experience without taking over the host model's recursive planning.
- The environment has a discrete admissible-action interface.

Do NOT use this skill when:
- Actions are continuous or there is no discrete action interface.
- There is no trajectory history to build the skill library from.

## Input needed

- Skill library: canonical task–action template pairs extracted from host trajectories.
- Semantic retriever: e.g. BGE-small-en-v1.5.
- State-bound binder: instantiates typed template slots with entities from the current request.
- Lightweight selector: e.g. Qwen3-1.7B with LoRA, chooses one candidate or abstains.
- The environment's admissible action set At at each step.
- The host model and recursive planner, kept frozen.

## Steps to execute

1. Build the skill library offline: convert host trajectories into canonical task–action template pairs, each pair is one skill.
2. At each adapter-eligible leaf task, invoke LeafSkill: retrieve top-k related templates via semantic retrieval above similarity threshold gamma.
3. State-bound binding: instantiate typed template slots with entities from the current request, retain only concrete commands that exactly match an action in At, merge duplicates into candidate set Ct.
4. Local selection: assign request-local identifiers to candidates, shuffle them, the selector chooses one identifier or bottom (abstain).
5. Resolve the selected identifier through the request-local mapping, check against At again before execution.
6. If no candidate, binding fails, or the selector abstains: return bottom, control returns to the host without changing agent state.

## Expected output

- Host model token reduction (23.1% Robotouille, 41.3% ALFWorld on jointly solved tasks).
- Host model call reduction (22.54% Robotouille, 41.75% ALFWorld).
- Success equal to or higher than host-alone (8.0 points higher on Robotouille C).
- Library growth without retraining deepens savings (18.3% → 25.6%).

## Example application

Robotouille cooking agent: the recursive planner has produced the leaf task "grab the onion". Instead of calling Qwen3.5-27B to translate it into a command, LeafSkill retrieves template "pick_up(·, ·)", binds it to "pick up onion1 from board1" (matching At), and the selector chooses or abstains. If chosen, the command is executed and feedback returned to the environment; if abstained, control returns to Qwen3.5-27B. Result: 23.1% fewer host tokens versus calling the host every time.

## Gotchas

- Assumes recurring parameterizable leaf tasks; if leaf tasks are one-off, the library is not useful.
- Requires an environment adapter and binder for each new action grammar.
- Controller overhead (6,900–9,952 tokens per episode) is reported separately because controller and host have different tokenizers.
- Abstention returns control to the host without executing any action — the host must handle this case.
- Library can grow at read time, but only with compatible skills (same action grammar and typed slots).
