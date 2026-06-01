# Skill: Novelty Pruning Tree-of-Thought
Source: 2605.06040
Type: workflow

## When to use this skill

- When using ToT with excessive token costs — branching factor leads to hundreds of thousands tokens
- When reasoning problems have low inherent width (<3) — only 2-3 truly different approaches needed
- When having token budget constraints

- Do NOT use when: high inherent width problems; weak LLM for novelty estimation; tree depth <3

## Input needed

- Reasoning problem with clear state space
- LLM for generation + novelty estimation
- Novelty threshold parameter
- Token budget

## Steps

1. **Define State Space** — Initial state, actions, successor via LLM prompting.
2. **Standard ToT Expansion** — Generate k successor thoughts per node.
3. **Novelty Estimation** — Compare with explored thoughts, score 0-1.
4. **Novelty Pruning** — If score < threshold → prune. Aggressive for low-width problems.
5. **Budget Management** — Track tokens, increase threshold if approaching budget.

## Expected output

- 10-20× token cost reduction
- Same success rate (within 5%)
- Faster solving (fewer states)

## Example application

Math competition with ToT: 4 approaches generated, numerical pruned (low novelty vs algebraic), explore top 3. 60% fewer tokens, same answer.

## Gotchas

- Threshold tuning: start at 0.5, tune per domain
- LLM novelty estimation may need few-shot examples
- Overhead only saves at depth >3, branching >3
- Novelty ≠ quality: combine with heuristic quality
