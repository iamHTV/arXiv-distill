# Skill: forty-shades-of-blue-moda
Source: 2609.14896v1
Type: framework

## When to use this skill
- Need to generate multiple distinct but high-quality responses from the same prompt (content ideas, research hypotheses, creative writing).
- Want to preserve output diversity during LLM post-training, avoiding mode collapse.
- A frozen reference policy is available for per-prompt quality threshold computation.

## When NOT to use this skill
- Factual queries with a single correct answer (e.g., Einstein's birthday) → use standard mode, no diversity needed.
- No GPU resources for GRPO training with multiple role-response pairs per prompt.

## Required inputs
- A base language model (e.g., Qwen3-8B-Instruct).
- A frozen reference policy to compute reference quality scores.
- Abstract numbered role identifiers.
- A GRPO training system (verl + vLLM + FSDP or equivalent).
- A reward model to score response quality.
- A diversity metric (SBERT, E-Vendi, or discriminator).

## Steps
1. Prepare training data (4:1 Tulu3-SFT-Mixture : Infinite-Chat mixture or equivalent) and compute reference quality scores (smin, smax, µref) from the frozen reference policy per prompt.
2. Prepend abstract role identifiers to the system prompt (e.g., "You are role i."), avoiding hand-crafted personas to encourage emergent specialization.
3. Each training round, each role generates one response per prompt in the batch, forming a response group (e.g., 6 role-response pairs).
4. Compute quality score si = Sϕ(x, yi) from the reward model; compute per-prompt quality threshold τq(x) = smin + α(smax − µref) and scale σq(x) = γ(µref − smin + ϵ).
5. Apply binary quality gate g(x, yi) = 1[si ≥ τq(x)]: only responses meeting the threshold receive diversity credit.
6. Compute diversity score d(x, yi, Y) = minj≠i (1 − cosine similarity between yi and its nearest neighbor in the group).
7. Compute composite reward: quality reward (tanh-bounded) + diversity score (quality-gated) + penalties (length, language, format).
8. Update the shared policy with GRPO using group-relative advantages and KL regularization to the base policy.
9. Inference: standard mode (no role token → single response) or diverse mode (multiple role tokens → diverse candidate set).

## Expected output
- A model that generates multiple distinct, high-quality responses from the same prompt while maintaining or improving general capability (pass@1), resisting mode collapse.

## Example application
- A small business generating blog post ideas: same prompt "write 5 blog topics about marketing" — MODA produces 40 distinct shades of blue analog (40 distinct ideas) instead of one repeated topic; standard mode for factual answers, diverse mode for brainstorming.

## Gotchas
- Do not use diversity reward alone without quality gate → reward hacking (off-topic, verbosity, language switching).
- Do not over-specify hand-crafted personas; abstract role IDs encourage emergent specialization better.
- Do not apply diverse mode to factual queries with a single correct answer.
- Do not forget KL regularization to the base policy to prevent policy drift.

## Self-check
- Can someone who has not read the original paper follow these 9 steps? [YES] — each step is a concrete action.
- Which step is most vague? Steps 4-5 (per-prompt quality threshold computation) need implementation details on smin/smax/µref.
- Is the Input section sufficient? [YES] — base model, reference policy, role IDs, GRPO system, reward model, diversity metric are all covered.

## Dry run (hypothetical scenario)
- Scenario: A solopreneur wants 10 different video ideas from the same topic.
- Run the skill: (1) Prepare 10K video content prompts; (2) compute reference quality scores from frozen policy; (3) add abstract role IDs (role 1..6); (4) each role generates one response per prompt → group of 6; (5) compute quality score and per-prompt threshold; (6) grant diversity credit only to threshold-meeting responses; (7) compute diversity score as semantic distance to nearest neighbor; (8) compute composite reward with length/language/format penalties; (9) update policy via GRPO; (10) infer with 6 role tokens in diverse mode → 10 distinct video ideas.

## Verdict: [SKILL VALID]
