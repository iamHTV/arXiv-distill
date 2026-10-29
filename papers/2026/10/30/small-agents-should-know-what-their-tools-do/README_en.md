# [2610.35981] Small agents should know what their tools do

## Core Value (1 sentence)

Training small open language models to understand what each tool does to the world, via effect declarations, achieves 99% in-distribution task success with about one-third of the output tokens, instead of only checking call syntax like public benchmarks.

## Problem

Small tool-calling agents can invoke tools but do not reason about what a call does to the world: they delete without asking, repeat writes, re-read state they already hold, and issue one call per turn where a short program would suffice. Public benchmarks such as BFCL (Berkeley Function-Calling Leaderboard) only score whether a call is well-formed; they do not score whether the agent re-reads data it already has, serialises independent look-ups, or cancels a meeting without asking. Tools are already annotated as read-only, destructive, or idempotent (calling multiple times has the same effect as calling once), but small open models are not trained to act on those annotations, and the annotations often never reach the model at all.

## Contribution

1. EffectWorld: an effect-typed executable tool world with a replay verifier (checks correctness by replaying the recorded trace), a scripted user (programmed user with deterministic replies), one training domain, and two test-only splits: a hard split with unseen task kinds and distractor tools, and a commerce domain (online shopping).
2. Tool programs: a minimal $ref convention that lets one assistant turn express a dependency graph of calls inside native tool-call blocks, so existing parsers and benchmarks keep working.
3. A compiler-style trace optimizer with footprint-based legality (legality determined by the read/write footprint of each call), and a taxonomy of 19 negative classes (labelled examples of wrong actions) derived from its diffs.
4. A controlled comparison of two suppression objectives (UL — unlikelihood training, NPO — negative preference optimisation) against DPO (direct preference optimisation) and an SFT control (supervised fine-tuning baseline), all continued from the same SFT adapter. None of them beats the control on any held-out split.
5. Two data findings: refusal templates (templated decline phrases) in public tool-use data collapse a small model's willingness to call tools on BFCL, and filtering them restores performance.

## Method

EffectWorld builds tools with effect declarations: each tool has an effect type (pure — computes from arguments alone, touches no state; read — reads state without changing it; write — changes state in a correctable way; destructive — cannot be undone: deletes data, reaches people, moves money), an idempotence flag (whether calling twice with the same arguments equals calling once), and a footprint (the resources it reads and writes, as patterns over its arguments). These declarations enable: (1) a replay verifier that decides whether a trace is effect-safe without labels or a judge model, (2) an executor that runs tool programs of several dependent calls in one turn, and (3) a compiler-style optimizer that converts wasteful traces into verified training signal. A LoRA adapter (low-rank adapter added to the model) is trained on EffectWorld data.

The model is told only the tool's name, description, and parameters (it does not see the effect declarations by default). The system prompt states five policies: confirm before any irreversible action, never repeat a non-idempotent write, read current data before modifying it, ask when required information is missing, and do not call tools when none is needed.

## KNOWLEDGE — Data & Concepts

- On the test split (498 tasks), Qwen3-4B starts at 53% task success; SFT (supervised fine-tuning) raises it to 99% in distribution (on tasks of the same kind as training data).
- On the hard split (775 tasks with unseen task kinds and distractor tools), success rises from 52% to 81% (+29 percentage points).
- On the commerce split (547 tasks with tools never seen in training), success rises from 74% to 83%.
- Output uses about one-third of the tokens of the base model (untuned model).
- On BFCL, the adapter matches the base model's live accuracy (accuracy on live user-contributed prompts) and raises multi-turn accuracy from 21.9 to 26.6; a recipe with near-miss declines lifts the BFCL average to 70.0 versus 68.7 for the base model.
- Refusal templates in public tool-use data cut BFCL non-live accuracy (accuracy on fixed benchmark-written prompts) from 88.0 to 31.4; filtering them restores 84.8.
- Three model families (Qwen3-1.7B, Phi-4-mini, Falcon3-3B) are lifted from 4–25% to 69–99% in distribution and +26 to 55 points on held-out splits (data not used in training).
- On the hard split, SFTclean (81.5%) and other variants reach 77.8–83.7% in program mode (multiple dependent calls in one turn).

## INSIGHT — Mechanism & Why

[Small agents call tools clumsily — delete without asking, repeat writes, re-read known state] happens BECAUSE [they are trained on data that only scores call syntax, without declarations of what each call does to the world]. This means [syntax checking is not enough; the agent needs to understand the effect of each tool before calling].

[Refusal templates in public data teach small models not to call tools] happens BECAUSE [small models generalize from stylized refusal phrases]. This means [in-domain metrics can look perfect while real tool-calling ability is destroyed; only an external benchmark exposes it].

[Positive examples carry the behaviour they show, not the label] happens BECAUSE [declining when a tool is missing does not teach declining when an offered tool cannot serve the request]. This means [you need positive examples for every decision the agent must make — declining, asking, confirming — rather than relying on negatives to carve them out].

[Effect declarations make safety and efficiency checkable properties of a trace] happens BECAUSE [the replay verifier can decide whether a trace is effect-safe by replaying calls against the declarations, without labels or a judge model]. This means [safety does not need human evaluation or a judge model, just tool declarations].

## IDEA — Actionable Applications

1. Apply effect declarations to agent tools: each tool in the schema should have an effect type (pure/read/write/destructive), an idempotence flag, and a footprint (resources read/written). For whom: a solopreneur building tool-calling agents (e.g. an agent handling orders, appointments, email). First step: add an effect field to the tool definition in MCP (Model Context Protocol — standard for connecting agents to tools).

2. Apply a confirmation-before-destructive-call rule: the agent must propose and wait for user confirmation before deleting, sending email, or cancelling an order. For whom: agents performing irreversible actions. First step: write a system prompt with the paper's five policies (confirm before destructive, never repeat non-idempotent write, read before write, ask when missing info, don't call when none needed).

3. Apply a refusal filter before mixing public tool-use data into agent training. For whom: teams preparing training data for tool-calling agents. First step: scan training data for templated refusal phrases like "I don't have access to a tool that can do that" and remove them.

## WISDOM — General Principle

- Principle: Checking call syntax is not enough; the agent must know what each call does to the world. Apply when designing tool-calling agents in environments with irreversible actions. Do not apply when the agent only retrieves read-only information and has no actions outside the system.

## Assumptions & Limitations

- Conditions that must hold: tools have clear effect declarations, a user is available to confirm destructive calls, the small model is trained on data with effect annotations.
- Limitations acknowledged by the paper: EffectWorld is small (9 task kinds, one training domain, one test-only domain), the scripted user never changes its mind and confirms every proposal it recognises, the verifier checks by replaying recorded traces rather than proving for all states, detailed analysis uses only one backbone (Qwen3-4B), all models have at most 4B parameters, models are trained from a single training seed.
- Limitations the paper does NOT state: effect declarations on real tools outside simulation (e.g. public APIs) may be inconsistent; operational cost of the replay verifier at scale is not evaluated; effect declarations are not tested on agents larger than 4B parameters.

## Metadata

- Year: 2026
- Authors: Alexander Kovalenko, Artem Redchych (Czech Technical University in Prague)
- arXiv category: cs.SE
- PDF link: https://arxiv.org/pdf/2610.35981v1
- Citation count: [not found]