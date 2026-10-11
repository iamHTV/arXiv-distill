# Skill: Safety Self-Play Alignment
Source: 2601.10589
Type: workflow

## When to use this skill

- When needing proactive safety alignment — model auto-discovers and patches vulnerabilities
- When static adversarial datasets overfit — need evolving defense
- When wanting safety-usability balance — minimize over-blocking

- Do NOT use when: no RL infrastructure; model too weak for dual roles; external red team mandated

## Input needed

- LLM to align
- Harmful request dataset
- RL training infrastructure
- Safety benchmarks (HarmBench, OR-Bench)

## Steps

1. **Initialize Roles** — Single LLM alternates Attacker/Defender. RL rewards: Attacker for bypasses, Defender for refusals.
2. **Self-Play Loop** — Alternating episodes: Attacker generates jailbreaks, Defender evaluates, update via RL.
3. **Reflective Experience Replay** — UCB sampling prioritizes failure cases (successful attacks).
4. **Evaluate Balance** — Low ASR on HarmBench + low refusal rate on OR-Bench.
5. **Iterate Until Convergence** — ASR stabilizes, no new patterns, refusal rate stable.

## Expected output

- Lower ASR than static training
- Lower refusal rate than over-defensive methods
- Diverse attacks without explicit diversity reward

## Example application

Healthcare chatbot: self-play 1000 episodes → Attacker discovers "ask for friend" bypass → Defender learns → ASR 35% → 8%, refusal rate stays 3%.

## Gotchas

- Model capability bound — supplement with external red teaming
- May need 1000+ episodes
- Tune UCB exploration constant
- Balance Attacker-Defender capabilities
