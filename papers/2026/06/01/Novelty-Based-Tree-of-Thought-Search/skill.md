# Skill: Novelty Pruning Tree-of-Thought
Source: 2605.06040
Type: workflow

## Khi nào dùng skill này

- Khi dùng Tree of Thoughts (ToT) cho reasoning tasks mà token cost quá cao — branching factor dẫn đến hundreds of thousands tokens per task
- Khi reasoning problems có inherent low width (<3) — chỉ cần 2-3 truly different approaches, không cần exhaustive branching
- Khi có budget constraints cho LLM API calls — need to reduce cost while maintaining quality

- KHÔNG dùng khi: problems có high inherent width (cần exhaustive search); LLM too weak for reliable novelty estimation; tree depth <3 (overhead not worth it)

## Input cần có

- Reasoning problem with clear state representation
- LLM for thought generation + novelty estimation
- Novelty threshold parameter (tune per domain)
- Token budget constraint

## Các bước thực hiện

1. **Define State Space** — Represent reasoning problem as state space: initial state s₀, actions (operations/transformations), successor function via LLM prompting. Define goal condition.

2. **Standard ToT Expansion** — At each node, prompt LLM to generate k successor thoughts. Each thought = new state in reasoning tree.

3. **Novelty Estimation** — For each new thought, prompt LLM: "Compare this thought with previously explored thoughts: {list of explored thoughts}. How novel/unique is this thought? Score 0-1." Use pre-trained knowledge for comparison.

4. **Novelty-Based Pruning** — If novelty score < threshold → prune branch (don't explore children). If ≥ threshold → continue expansion. Aggressive pruning for low-width problems (width <3).

5. **Token Budget Management** — Track total tokens used. If approaching budget, increase pruning threshold (more aggressive). Goal: maximize problem-solving rate within budget.

## Output mong đợi

- 10-20× token cost reduction for same performance
- Same or slightly lower success rate (within 5% of standard ToT)
- Faster problem solving (fewer states explored)

## Ví dụ áp dụng

Scenario: Math competition problem with ToT. (1) Initial state: problem statement; (2) Generate 4 approach thoughts: algebraic manipulation, geometric interpretation, numerical testing, pattern recognition; (3) Estimate novelty: algebraic (0.8), geometric (0.7), numerical (0.3 - similar to algebraic), pattern (0.6); (4) Prune numerical (low novelty), explore top 3; (5) At depth 2, again estimate novelty among expanded thoughts; (6) Result: 60% fewer tokens, same correct answer.

## Gotchas

- Novelty threshold tuning: too aggressive → miss valid approaches; too conservative → no savings. Start at 0.5, tune per domain.
- LLM novelty estimation unreliable for domain-specific problems — may need few-shot examples of "novel vs. similar" thoughts.
- Token overhead: novelty estimation adds 1 prompt per thought. Only saves when tree is large (depth >3, branching >3).
- Novelty ≠ quality: a novel thought may still be wrong. Don't prune based on novelty alone — combine with heuristic quality estimation.
