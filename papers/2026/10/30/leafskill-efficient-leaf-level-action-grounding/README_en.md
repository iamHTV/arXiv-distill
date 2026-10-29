# [2610.32412] LeafSkill: Efficient Leaf-Level Action Grounding for Recursive LLM Agents

## Core Value (1 sentence)

Instead of calling the large host model (27B) every time a leaf task must be translated into an executable action, use an external retrieve–bind–select grounding layer that chooses within a state-bound admissible action set — saving 23.1–41.3% host tokens while preserving the host's recursive planning logic.

## Problem

Recursive LLM agents solve long-horizon tasks by decomposing goals into progressively smaller task nodes, but decomposition does not eliminate expensive host-model inference. Even after a leaf task becomes explicit, the agent may still invoke the same large model merely to translate that task into one action accepted by the current environment. For example, once the planner produces "pick up onion1 from board1", the remaining decision is no longer how to solve the overall goal, but how to ground this local instruction into an executable command. Leaf-level action grounding maps an already specified task node to one currently admissible environment action, without altering decomposition, parent plans, or completion state. This operation recurs throughout a trajectory and accounts for 22.9–44.5% of host-model tokens. Reusing these decisions is not equivalent to exact-string caching: semantically equivalent tasks may be expressed by different phrases, while similar phrases may encode different intents. Retrieved arguments may be absent from the current state, and the same task may ground to different actions under different observations.

## Contribution

1. Problem formulation and measurement: formulates leaf-level action grounding as a distinct delegation boundary in recursive LLM agents and shows it accounts for 22.9–44.5% of host-model tokens in source traces.
2. Constrained grounding architecture: develops a retrieve–bind–select layer that converts reusable task–action experience into state-bound admissible candidates, while preserving host-owned planning and recovery through explicit abstention.
3. Cross-environment evidence: across Robotouille and ALFWorld, demonstrates substantial host-token reductions on jointly solved tasks, identifies complementary roles of retrieval, binding, and selection, and shows that post-training library growth can further increase savings without selector retraining.

## Method

LeafSkill has an offline construction stage and an online grounding stage. Offline, host trajectories are converted into canonical task–action templates and selector supervision. Online, LeafSkill is invoked only at adapter-eligible leaf tasks: it retrieves related templates, binds them to the current admissible action set, and either selects one action or abstains. Each skill s in library L is a canonical-task/action-template pair with observed surface forms and provenance. Multiple skills may share one canonical task key. For an eligible request, semantic retrieval ranks canonical task keys against the current task and returns the top-k keys above similarity threshold gamma. All templates associated with those keys proceed to binding. State-bound binding instantiates typed template slots with entities from the current request and retains only concrete commands that exactly match an action in the admissible set At. It merges duplicate skill–action pairs, producing the finite candidate set Ct. Candidates receive request-local identifiers and are shuffled before presentation to the selector. The selector chooses one identifier or bottom (abstain); it cannot generate a free-form command. The selected identifier is resolved through the request-local mapping and checked against At again before execution. The selector is not a policy over the full admissible set: retrieval and binding define its request-local support, and an empty support returns control to the host.

## KNOWLEDGE — Data & Concepts

- Leaf-level grounding consumes 22.9% (synchronous Robotouille), 23.7% (asynchronous Robotouille), and 44.5% (ALFWorld) of host-model tokens.
- With the same ReCAP planner and Qwen3.5-27B host, LeafSkill reduces host tokens on jointly solved tasks by 23.1% on Robotouille and 41.3% on ALFWorld, averaged over all nine cross-run pairings of three independent repeats; the nine pairing-specific reductions span 16.8–29.7% and 36.7–45.2% respectively. An independent Robotouille evaluation yields a further 14.4% reduction (95% CI [3.0, 24.5]) and 14.1% call reduction (95% CI [3.6, 23.3]).
- Mean observed success is numerically higher for LeafSkill in both environments: 6.0–9.0 points higher on Robotouille B and 8.0 points higher on Robotouille C (137/200 vs 121/200, p = .0259).
- A disjoint growth study expands the library from 446 to 588 skills without selector retraining or test trajectories; on tasks solved by all systems, host-token savings deepen from 18.3% to 25.6%.
- Retriever: BGE-small-en-v1.5; Selector: Qwen3-1.7B (LoRA rank 16); Host: Qwen3.5-27B; Planner: ReCAP.
- Controller overhead: 6,900–9,952 tokens per episode (714–1,034 per call), reported separately because controller and host have different tokenizers and scale.
- On 100 Robotouille tasks solved by both BGE Top-1 and LeafSkill, Top-5 selection provides a further 14.9% host-token reduction.
- SFT raises mixed-rank selection accuracy from 81.9% to 93.3%. On the all-negative OOD diagnostic, SFT returns FALLBACK_RECAP in only 7.5% of cases.
- Robotouille library: 413 task keys and 446 skills from 200 Group-A source trees; expanded library contains 527 keys and 588 skills after merging with 200 Group-B trees, adding 114 keys and 142 skills without controller updates.

## INSIGHT — Mechanism & Why

[Leaf-level grounding consumes 22.9–44.5% of host tokens] happens BECAUSE [each time the planner produces a leaf task, the large host model is called merely to translate that task into one executable action, and this operation recurs throughout a trajectory]. This means [a narrow but substantial target for reducing expensive host inference].

[The retrieve–bind–select layer reduces tokens without changing planning] happens BECAUSE [retrieval only proposes, binding only maintains executability, and the selector only chooses within a finite state-bound candidate set or abstains — delegated authority is kept narrow, while planning and recovery remain entirely host-owned]. This means [experience reuse does not need to take over planning from the host model].

[State-bound binding is safer than model-generated commands] happens BECAUSE [binding instantiates typed template slots with entities from the current request and retains only concrete commands that exactly match an action in At, rather than asking a model to synthesize slot values]. This means [validation before execution prevents inadmissible commands].

[Request-local identifiers plus shuffling prevent the selector from memorizing global skill IDs] happens BECAUSE [candidates receive request-local identifiers and are shuffled, so the selector must read candidate content rather than rely on a fixed global label]. This means [compatible skills can be added without changing the selector's output space].

[The library can grow at read time without retraining] happens BECAUSE [request-local identifiers remove a fixed output vocabulary]. This means [compatible new skills can be incorporated at inference time within one interface and template family].

## IDEA — Actionable Applications

1. Apply an external retrieve–bind–select grounding layer to recursive agents: after the planner has decomposed to a leaf task, use a skill library instead of calling the large host model. For whom: teams building recursive LLM agents that call large models many times. First step: build a task–action template library from the host model's trajectory history.

2. Apply state-bound binding: before executing an action, check whether it is in the environment's current admissible action set At. For whom: agents interacting with environments with discrete valid action lists. First step: write a function that checks whether an action exists in At before execution.

3. Apply safe abstention: when no skill fits or binding fails, return control to the planner host instead of guessing. For whom: agents that need safe action in uncertain environments. First step: add a rule "if unsure, return to host" in the action selection layer.

## WISDOM — General Principle

- Principle: Separate remembering experience (retrieval) from executing (execution) — the external layer is only allowed to choose within a finite, state-bound set of actions, and must not generate free-form commands. Apply when a recursive agent calls the large model too many times for leaf tasks. Do not apply when actions are continuous or there is no discrete action interface.

## Assumptions & Limitations

- Conditions that must hold: recurring parameterizable leaf tasks, a discrete admissible-action interface, and an environment adapter.
- Limitations acknowledged by the paper: LeafSkill assumes recurring parameterizable leaves, a discrete admissible-action interface, and an environment adapter; new action grammars require corresponding adapters and binders, while open-ended or continuous actions may need richer executable-action interfaces; the present evidence covers one planner, one host, two environments, and one selector family.
- Limitations the paper does NOT state: effectiveness on hosts larger than 27B, controller operational cost at scale, and scalability to real-world environments beyond Robotouille and ALFWorld.

## Metadata

- Year: 2026
- Authors: Shen Liu, Ze Zhou, Zhenguo Xu, Shaopu Wang, Yike Gao, Chunlei Wang
- arXiv category: cs.AI
- PDF link: https://arxiv.org/pdf/2610.32412v1
- Citation count: [not found]