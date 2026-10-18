# Skill: mapl-multi-agent-preference-learning
Source: 2609.32827
Type: framework

## When to use this skill
- Multiple LLM agents collaborate on the same task and you need to coordinate output quality.
- No clear scalar reward, but you can compare two outputs to decide which is better.
- Want to improve multi-agent collaboration efficiency without hard-coded metrics.

## When NOT to use this skill
- Single-agent tasks (no multi-agent coordination needed).
- A perfect reward function already exists that accurately measures output quality.

## Required input
- A group of LLM agents working on the same task (at least 2 agents).
- A mechanism to compare two trajectories/outputs (annotator: human or AI judge).
- Preference pair dataset (winner, loser) from comparisons.

## Steps to execute
1. Collect joint histories and trajectories of agents for each task.
2. For each trajectory pair, the annotator compares quality/return, labels the winner (higher) and loser, discards ties.
3. Take top-k preference pairs with highest winning return as the replay buffer.
4. Choose MARLHF (learn reward model from preference, then optimize policy with MARL) or MADPO (directly optimize policy from preference).
5. Repeat collect-compare-train over multiple iterations.
6. Choose coordination paradigm: Dec-Dec, Cen-Cen, or Dec-Cen based on resources and information needs.

## Expected output
- Agent policies optimized from preference feedback, collaboration quality improved, approaching MARL with oracle reward.

## Example application
Two Qwen3-1.7B agents both summarize a Reddit post: agent 1 produces a high-level summary, agent 2 a detailed summary. Merged output goes to an annotator who compares two versions, uses preference to fine-tune a reward model, then MARLHF coordinates the two agents to summarize better.

## Gotchas
- MARLHF is sensitive to data coverage, agent/comparator models, MARL algorithm — don't run blindly.
- Centralized/larger comparator does not guarantee better results (information and realizability gaps).
- Raw LLMs are not inherently cooperative → initial preference data may contain many non-cooperative trajectories.