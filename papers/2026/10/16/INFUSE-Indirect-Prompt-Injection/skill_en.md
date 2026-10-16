# Skill: infuse-indirect-prompt-injection-benchmark
Source: 2610.20776v1
Type: framework

## When to use this skill
- Building or using LLM agents that execute long-horizon, end-to-end workflows (shell commands, code modification, dependency installation, interaction with remote services).
- Want to evaluate agent robustness against indirect prompt injection.
- Need to add defense mechanisms for LLM agents.

## When NOT to use
- Using a simple LLM agent only, not executing complex tasks from external content.
- Don't need to evaluate robustness, only need performance.

## Required input
- An LLM agent executing long-horizon tasks.
- Real or synthetic query data to test attacks.
- An indirect prompt injection attack mechanism to test with.

## Steps
1. Build an LLM agent executing long-horizon tasks (shell commands, code modification, etc.).
2. Test the agent with indirect prompt injection attacks (adversarial instructions embedded in external content).
3. Measure attack success rate (ASR-L by LLM evaluation, ASR-H by heuristic evaluation) before and after attack.
4. Add defense mechanisms: instructional hardening, input sanitization, output validation, rate limiting.
5. Test again after adding defenses to confirm effectiveness.

## Expected output
- Reduce attack success rate (from 19.6% LLM-based, 15.4% heuristic down to lower level).
- Reduce agent following adversarial instructions embedded in external content.
- Increase agent robustness against indirect prompt injection.

## Example application
Solopreneur building a customer support LLM agent executing shell commands and code modification: test agent with indirect prompt injection attacks (e.g. external content containing commands to delete files or send data out). Add instructional hardening and output validation to reduce risk. Reduce agent being fooled or performing unwanted actions.

## Gotchas
- LLM agents are vulnerable to indirect prompt injection: mean attack success 19.6% (LLM-based), 15.4% (heuristic).
- Per-model ASR-L from 3.2% to 41.9% — some models are much more vulnerable than others.
- Instructional hardening reduces attack success from 58.2% to 14.3% — this is an effective defense.
- Refusal (refusal to comply) is very rare (≤ 1.0% for every model) — agents usually follow adversarial instructions instead of refusing.
