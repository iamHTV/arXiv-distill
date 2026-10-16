# Skill: Pre-generation Elicitation Scaffold
Source: 2610.09593
Type: prompt-pattern (metacognitive scaffolding layer for AI-assisted decision workflows)

## When to use this skill
- Using AI to generate strategic/decision deliverables (action plans, strategy docs, analyses) where quality depends on context the user knows but prompts usually omit
- Worried about cognitive surrender (users accepting weak output without evaluating) — need to keep users engaged with reasoning
- Do NOT use: simple factual tasks, lookups, or when the user is already an expert writing complete prompts (still gains +20.9% but lower cost-benefit)

## Inputs required
- Task description (scenario, constraints, deadline)
- 3 clarification dimensions fit to the domain (paper used: operational priority, infrastructure, primary audience)
- 2–4 strategic posture options (scaffold cards) for the task — concrete examples, not a single "correct" answer
- AI generator (paper used Gemini 3 1 Pro)

## Steps
1. User writes an initial prompt (kept as baseline across arms).
2. Ask 3 clarification questions: operational priority, context/infrastructure, primary audience — one choice each.
3. Present scaffold cards: user selects one strategic posture (e.g., decisive split-system vs cautious phased rollout).
4. User writes a free-text rationale explaining the posture choice (this step keeps the user engaged with the reasoning).
5. Synthesis step: feed prompt + 3 answers + posture + rationale into the generator; the AI drafts from the full input set.
6. Evaluate output with a 4-dimension rubric (strategic coherence, trade-off articulation, information density, technical specificity) with condition-blind raters; track the floor-scored (off-task) rate.

## Expected output
- Deliverable quality +~32% composite (d=1.02), largest gains in trade-off articulation + strategic coherence; off-task output drops 34%→5%; cost +2.4 min/user.

## Example application
- Content strategy: before AI drafts a campaign brief, ask priority (awareness/conversion), channel context, audience; choose posture (aggressive vs conservative tone); write the rationale → deeper brief, fewer off-task outputs.

## Gotchas
- Technical/regulatory specificity does NOT improve (p=.300) — the scaffold does not replace domain expertise; expert review still required.
- ~59% of the effect comes from rescuing weak prompts — but good-prompt users still gain +20.9%, so run it for everyone.
- Self-ratings are unreliable: user self-assessment does not track real quality — use an objective rubric, do not ask "did you like it".
- Diversity narrows: 165/204 picked the same posture — randomize card order and add options to avoid convergence.
- The rubric must be neutral between options (the paper was biased because its rubric named the split architecture as an example).
