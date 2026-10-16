# Skill: Agent Failure Ledger Taxonomy
Source: 2609.21341
Type: evaluation-method / debugging-workflow

## When to use this skill
- A production agent fails often and blame falls on "the model is weak" — you need to know where failure really sits (model vs server/contract)
- You have tool-call logs but only exit codes / refusal codes, not the actual arguments
- Before swapping models or prompts: you want to fix failures server-side first

Do NOT use: the agent has no structured logs (no ledger) — instrument first; or failure is caused by task design, not the tool loop.

## Input required
- Agent loop with a verifier (output judged answered/unanswered — "succeeded" ≠ pass)
- A ledger recording: every tool call (arguments verbatim), refusal code, verdict, process exit, timing
- A classifier applying the fixed order in step 2

## Steps
1. Instrument: record EVERY tool call's arguments verbatim + refusal code + verdict (answered/unanswered) + exit status. A ledger that records only exit status hides the entire transport class.
2. Classify each run loss in LOAD-BEARING order: clock (timeout/turn-limit/deadline) → capability (invoked no tool) → verification (report filed but rejected) → transport (invoked tools, no timeout, no deliverable). The order changes the headline — always state which ordering was used.
3. Decompose the transport class using captured arguments: find repeated shapes — correct JSON sitting in the text channel, array closing twice, key "name"/"action" instead of schema keys, near-miss keys.
4. Fix SERVER-SIDE (touch no model, prompt, or sampling): recognize calls by naming rather than strict JSON parsing; read SQL kind from the statement; make renames unambiguous (exactly-one-absent/surplus); fix "remove <field>" instructions that contradict a sibling tool.
5. Re-read the SAME cells (same model, same task, same hardware) before/after, comparing cell by cell (e.g. x/30 → y/30). Report honest qualifications: isolated effect of each change, don't lump them.
6. Control hardware confounds: cap serving context (check the engine's own process listing with its context column — system-wide free memory reads "healthy" while one model holds most of RAM); watch swap GROWTH during runs (a full static swap costs nothing; swap being written means the machine is choosing between the model and everything else).

## Expected output
- A 4-class table with % of total losses; transport decomposition by shape; a before/after per-cell table of server changes; a conclusion on whether failure sits in the model or in the contract/server.

## Example application
- A database agent with 8,199 runs: the ledger showed 75.7% of losses from runs that DID invoke tools; 27 of 69 stopping turns contained a correct tool call written into the text channel. 5 server changes touching no model/prompt/sampling moved 6 models by 6–21 cells of 30 (cogito:8b from 0/30 to 21/30).

## Gotchas
- "succeeded" ≠ pass: an empty report still exits successfully — the verifier must separate answered/unanswered (in the corpus: 2,204 model-stopped, 1,405 unanswered).
- Recovery paths that require JSON parsing see 0 correct-but-malformed calls (none of 27 parsed).
- Classification order is load-bearing: capability-first flips capability to 24.3% — always state the ordering.
- Uncapped context creates fake "model weakness": a 3B model's planning cell read 0/5 (51 GB RAM) → 5/5 capped at 32k. Per-model rates are a LOWER BOUND.
- The run deadline is product config: a model passing at 443–444s still fails at a 450s deadline — don't "fix" it by removing the deadline.
