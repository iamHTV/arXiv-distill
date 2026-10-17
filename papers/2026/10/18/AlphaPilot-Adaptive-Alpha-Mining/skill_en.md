# Skill: Multi-Turn Tool-Using Agent with Evaluator Feedback Loop (for alpha mining)
Source: 2610.15488v1 (AlphaPilot)
Type: framework (training + inference workflow)

## When to use this skill
- You need an LLM agent to iteratively propose candidates (factors, rules, queries, prompts) over multiple turns, with an executable evaluator tool providing feedback each turn.
- You need adaptation to context that shifts day by day / session by session (market regimes, data drift) rather than a one-shot search.
- Do NOT use when: there is no executable evaluator for per-turn feedback (only an LLM judge — then use a plain prompt loop); the problem needs only a single proposal (single-shot suffices).

## Inputs required
- A DSL (expression grammar) + clear operator set (e.g., alpha mining: ts_delta, ts_corr, rank, delay).
- Tabular data with a rolling training window (AlphaPilot used daily A-share CSI300/CSI500, 3-year rolling).
- An executable evaluator tool: validates syntax, executes the candidate, returns compact feedback (IC, RankIC, stability, error).
- A seed factor library (manifest) + a market-regime description for each day.
- RL infrastructure: VERL (or an equivalent GRPO framework), a small backbone (AlphaPilot used Qwen3-4B-Instruct-2507).

## Steps
1. Build daily context c_t = (q_t, S_t, O): write a natural-language market-regime description for each day, merge the seed/carried-over factor manifest, list the supported operator set.
2. Implement the factor_evaluator: check DSL syntax → execute on the rolling training window → apply universe/tradability filters → return compact feedback (expression, family, IC, RankIC, stability, error).
3. Run multi-turn rollouts: the policy observes context + compact memory (tried factors, pool state, previous feedback) → proposes B candidates per turn; loop at most H_max turns (AlphaPilot: 40 assistant turns, 8 rollouts per prompt during training).
4. Maintain the retained factor pool: light filter (drop invalid / insufficient-coverage / non-positive single-factor score) → fit NNLS/ridge-style meta-alpha weights on the recent segment (w≥0) → compute pool diagnostics from cross-sectional ranks.
5. Train with GRPO: reward = sigmoid-mapped future-window IC/RankIC + minimum-positive-factor completeness penalty; do NOT put auxiliary pool terms in the reward (they belong in the pool score).
6. Day-by-day inference: re-search and update the pool each day; combine recent-window NNLS/ridge weights; long-only top-K portfolio with 10 bps transaction costs.
7. Two-tier evaluation: factor-level diagnostics (IC/RankIC/turn statistics) AND portfolio-level backtests (total return, Sharpe, MaxDD, excess vs equal-weight benchmark); use 3-run means for stochastic methods.

## Expected output
- A retained factor pool that adapts to new regimes daily; interpretable factor expressions (e.g., "1 -rank(ts_delta(close, 1))" score 0.380); portfolio metrics like AlphaPilot CSI300: 42.93% return, Sharpe 2.46, MaxDD -9.34%.

## Example application
- A solopreneur analyzing VN stocks (HOSE): a DSL with 20 technical operators, an evaluator computing IC on rolling 3-year HOSE data, training Qwen3-4B + GRPO with 8 rollouts per prompt; each day the agent re-searches the factor pool from a hand-written regime description; combine the pool with NNLS weights → long-only top-10, 10 bps fees.

## Gotchas
- Reward proxy ≠ realized portfolio return: ablations showed the variant with the best IC/RankIC (0.0419/0.0634) had the weakest return/Sharpe (34.39%/2.06) — always check pool-level utility, do not optimize raw IC.
- Compact memory is mandatory: removing memory feedback halved return (48.64→26.40) and tripled rollout length (5.24→15.75 turns).
- Future-window data must NOT be available to the inference policy — it is only for offline reward computation, to avoid leakage.
- Multi-turn GRPO is compute-heavy: AlphaPilot could only train a 4B model; plan GPU budget before scaling.
- Evaluating on one contiguous period / one market does not prove generalization — run separate cross-market tests.
