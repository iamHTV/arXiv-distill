# Skill: jev-litemas-multi-agent-decision-routing
Source: 2610.21411v1
Type: framework

## When to use this skill
- AI pipeline has multiple specialist agents in sequence, each producing an artifact passed to the next.
- Want to cut LLM cost because routing (picking next agent) and review (checking artifact) take 30%+ of tokens.
- Can predefine expert roles and legal actions (pass/escalate, accept/revise).

## When NOT to use
- Task requires creating new experts or reconfiguring roles for unseen tasks.
- Single-agent workflow, no multi-agent coordination needed.

## Required input
- List of available expert roles and legal actions.
- Task rubric for Jev to screen artifacts.
- Generative backbone model (e.g. DeepSeek-V4-Flash, GPT-5) for expert execution and LLM review.
- Jev decision model (can be a fine-tuned small SLM).

## Steps
1. Build Jev decision model taking task + accumulated context, selects next expert from pool, decides PASS/ESCALATE for intermediate artifact.
2. If PASS, forward artifact to selected expert via handoff; if ESCALATE, call LLM review for ACCEPT/REVISE + semantic feedback.
3. Update shared state after each step so next agent receives artifact and prior work.
4. Only enable generative review for artifacts that truly need revision; avoid LLM call for every coordination step.

## Expected output
- Reduce 12.7–54.6% generative-LLM tokens vs all-generative baseline (e.g. LAS), accuracy within 1.34 percentage points.
- Lower latency; Jev takes only 2.92–6.85% of end-to-end latency.

## Example application
Solopreneur runs multi-channel content pipeline: agent 1 writes article, agent 2 edits SEO, agent 3 publishes. Instead of large LLM picking next agent and reviewing every draft, use small Jev to route article from agent 1 to agent 2 only when draft passes criteria, and only call large LLM to review when Jev flags revision needed.

## Gotchas
- Dropping semantic feedback on REVISE drops accuracy sharply (75.33% → 57.33% on IDRBench I3).
- When more artifacts need revision, token savings decrease.
