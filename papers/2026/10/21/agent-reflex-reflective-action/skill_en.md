# Skill: Training Proactively Reflective Agents (Agent-Reflex, 3 Stages)
Source: 2610.17953
Type: framework

## When to use this skill
- Agents using tools (MCP) in real environments: tools return noisy errors, users correct mid-task.
- You need the agent to self-recover instead of relying on inference-time prompt critique.
- Do NOT use for simple single-turn agents with few tools in clean environments.

## Inputs required
- An environment-scaling pipeline for the agent's domain.
- A capability-diverse LLM pool to mine pairs.
- Real error-return logs to classify tool-error families.

## Steps
1. Stage 1 — RSD: inject grounded tool-feedback perturbations into environment scaling; sample the LLM pool; mine matched success–failure pairs; summarize reusable reflection meta-skills (one per error family).
2. Stage 2 — ReSFT: convert each skill into supervision for three behaviors: self-reflection, skill recovery, user-centric correction; fine-tune the backbone.
3. Stage 3 — ORPO: agentic RL under noisy interactions plus reflection-guided on-policy distillation from the meta-skills; train ~100 RL steps, monitoring stable training dynamics.
4. Evaluate on both clean benchmarks and a noisy benchmark (AgentNoiseBench-style: tool noise + user noise) — both must improve.

## Expected output
- An 8B backbone agent scoring above reflection/environment-scaling baselines and robust to noise (Agent-Reflex: 58.6 long-horizon overall, 29.1 on AgentNoiseBench vs NoisyAgent-8B 25.9).

## Example
- A customer-support agent with 3 MCP tools: mine 24K error returns → 8 error families (timeout, auth expired, schema mismatch...) → 8 recovery skills → ReSFT + ORPO → the agent retries with correct parameters on tool timeout instead of asking the user.

## Gotchas
- Perturbations must be grounded — meaningless noise yields useless skills.
- Success–failure pairs must be matched (same task, different outcome) — cross-task pairs don't transfer.
- ORPO costs more compute than SFT — start with ReSFT on a limited budget, add ORPO later.
