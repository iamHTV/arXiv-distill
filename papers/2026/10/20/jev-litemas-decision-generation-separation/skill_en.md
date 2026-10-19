# Skill: Capability-Matched Agent Coordination (feedback-driven routing + gated review)
Source: 2610.21411v2 (Jev-LiteMAS)
Type: framework / workflow

## When to use this skill
- Multi-step agent pipelines where routing (choosing the next step) + review (judging artifacts) exceed ~30% of generative-LLM tokens — the paper's profiling measured 31.7–43.5%.
- You have ≥2 fixed expert roles and intermediate artifacts with a clear quality rubric (pass/escalate criteria).
- Do NOT use: workflows that need to dynamically create new experts/roles for unseen tasks; pipelines where most artifacts are broken (the gate saves nothing); single-step tasks with no coordination.

## Required inputs
- Expert role list: capability description + backend (model) + role instructions per expert.
- Rubric for intermediate artifacts (task-specific pass/escalate criteria).
- A small choice-based decision model (Jev-class) for routing + screening — do NOT use a generic zero-shot SLM (TPR 44.67–61.33% is far too low).
- Per-operation token + latency logs (to measure baseline and verify savings).
- A test set with injected artifact errors (to measure gate TPR/FPR).

## Steps
1. Profile the pipeline: measure token and latency share of routing + review on representative tasks. If each is <~15%, stop — not worth changing.
2. Replace the planner-generated plan with feedback-driven routing: router prompt contains {task, summary of the latest artifact, expert descriptions, legal actions including STOP}; router returns an expert ID or STOP; the dispatched expert receives task + artifacts through shared state.
3. Install a screening gate at review points: the screener (decision model) evaluates the artifact against the rubric → pass (proceed with NO LLM review call) or escalate.
4. On escalate → LLM reviewer: verdict (accept/revise) + corrective feedback; the repair expert receives state ⊕ feedback; the new artifact is re-screened as a new artifact (cap the review–repair loop).
5. Verify gate quality: inject errors into one random expert's artifact; measure screener TPR/FPR vs the LLM judge — require TPR ≥~90% of the LLM judge; remember low FPR ≠ reliable detection.
6. Re-measure end-to-end token/latency/accuracy: accept if accuracy stays within ±1.34 points and tokens/latency drop; if artifact fail-rate is high, re-threshold the gate or use adaptive review policies.

## Expected output
- Pipeline with generative-LLM tokens down 12.7–54.6%, latency lower in 7/8 configurations, accuracy within ±1.34 pp; gate TPR close to the LLM judge (95.33%/91.33% vs 96.67%/92.00%); decision layer only ~1.5–2.1% of model cost and ~3–7% of E2E latency; robustness: attack success rate drops from ~50% to 3.33–4.00% under injected artifact errors.

## Example application
- 3-expert content pipeline: researcher → writer → editor. The router picks the next expert from the current artifact (no pre-generated trajectory); the gate checks the draft against an editorial rubric (facts present, no AI-slop) → pass goes straight to the next step, failures go to the editor with specific feedback. Baseline: full-LLM review ~35% of tokens → after the gate ~10%, accuracy within ±1 point.

## Gotchas
- Content-blind routing (router sees only names/metadata) costs up to 18.0 accuracy points: ALWAYS pass summaries of substantive outputs to the router.
- Generic SLMs (e.g., zero-shot Qwen3-1.7B) reach only 44.67–61.33% TPR — weak gates; low false-alarm rate (FPR 0.00%) does NOT mean the gate is good.
- Savings collapse when the artifact quality distribution is bad — artifacts needing repeated repair.
- Fixed expert pool: the skill cannot handle tasks requiring unconfigured new roles.
- Don't ignore the decision layer's own latency (1.13–2.21s/unit) — up to 6.85% of E2E on MATH when experts are fast.

## Self-check + Dry run (Step 5)
- SELF-CHECK: can someone who hasn't read the paper follow it? YES — 6 concrete steps, inputs fully listed, gotchas explicit. Most ambiguous step was step 5's TPR ≥~90% threshold — now anchored to the paper's LLM-judge standard. Inputs sufficient.
- DRY RUN: hypothetical 3-expert pipeline (researcher/writer/editor), 100 tasks; baseline routing+review = 38% of tokens, ACC 72.0%. After the skill: router sees real artifacts (not content-blind) → ACC 73.3% (within ±1.34); gate on 30 injected-error artifacts: TPR 91% vs LLM judge 93%; tokens −33%, latency −28%; decision cost 2.1% of total. Output is meaningful: the gate preserves quality while cutting tokens clearly.
- VERDICT: [SKILL VALID]
