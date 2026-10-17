# 2610.15488v1 AlphaPilot: Multi-Turn Tool-Using LLM Agents for Adaptive Alpha Mining with Reinforcement Learning

## Problem
- Formulaic alpha mining seeks interpretable expressions that rank assets by future returns. It is hard because three challenges hit at once: a combinatorial search space (operators × features × lookback windows), weak and unstable supervision (noisy returns, changing market regimes), and redundancy (a formula good in isolation may be redundant once added to a larger pool). Prior methods use only subsets of the signals: GP/symbolic regression (scalar fitness only, overfitting-prone), RL/generative (AlphaGen, AlphaForge — no language priors to interpret regimes), LLM-based (priors but no real-data evaluation feedback loop).

## Contribution
- An RL (reinforcement learning) multi-turn tool-using framework: the agent conditions on market descriptions, proposes factor expressions, queries real-data evaluator feedback, and updates a retained factor pool across turns — closing the information loop: regime-aware language priors + executable real-market data + turn-level evaluator feedback + pool-level memory in one trainable search process.
- GRPO training improves the financial decision ability embedded in a small base model while maintaining inference efficiency — learning from multi-turn evaluator feedback rather than relying on a large general-purpose model's original capability.
- A daily adaptive inference and benchmarking framework: factor pools update day by day; methods are evaluated with both factor-level diagnostics and portfolio-level backtests.

## Method
- Daily market context c_t = (q_t, S_t, O): q_t = natural-language market-regime description, S_t = seed/carried-over factor manifest, O = supported operator set (DSL).
- Multi-turn rollout: at turn k, the small LLM policy observes the context plus compact memory (recently tried factors, retained-pool state, previous tool feedback) and proposes B DSL factors (expression + factor-family label); an executable factor_evaluator validates DSL syntax, executes the factor on the rolling training window, applies universe/tradability filters, and returns compact feedback (validated expression, family, IC, RankIC, stability, execution errors); the loop runs at most H_max turns (training: 40 assistant turns, 8 rollouts per prompt).
- Retained factor pool: a light initial filter (invalid, insufficient coverage, non-positive single-factor score are discarded); meta-alpha weights fit by NNLS/ridge-style regression on the recent training segment (w* = argmin ||F(P)w - target||² + ρ||w||², w≥0); pool diagnostics computed from cross-sectional ranks.
- Training: GRPO in VERL, backbone Qwen3-4B-Instruct-2507, reward = sigmoid-mapped future-window IC/RankIC + minimum-positive-factor completeness penalty.
- Inference: day-by-day search and pool updates (adapting to shifting market regimes); recent-window NNLS/ridge-style weights; long-only top-K portfolios with 10 bps transaction costs.
- Data: daily Chinese A-share panels for CSI300 and CSI500, 3-year rolling history window; 21/63-day future windows used for offline evaluation only (unavailable to the inference policy); split 2024-01-01 validation, 2025-07-01 test; train/validation examples sampled every 5 trading days, daily test inference.
- Baselines: Qwen3-4B/30B-A3B/235B-A22B (temperature 0), AlphaGen (RL), AlphaForge (generative), GRPO single-turn controlled baseline (same backbone/algorithm/splits/terminal pool-level reward, one-shot factor pool), seed-factor linear regression, DeepSeek-R1 direct-propose.

## Key Findings
- CSI300 out-of-sample (3-run means): AlphaPilot total return 42.93%, Sharpe 2.46, MaxDD -9.34%, IC 0.0403, RankIC 0.0595 — highest mean total return, Sharpe, and RankIC. Comparisons: Qwen3-4B 0.58%/0.16, Qwen3-30B -1.72%/-0.01, Qwen3-235B 6.88%/0.55, DeepSeek-R1 22.79%/1.21, Seed+LR 34.51%/1.82, AlphaGen 25.17%/2.26, AlphaForge 2.18%/0.07.
- CSI500: AlphaPilot 54.19%, Sharpe 2.86, MaxDD -14.34%, IC 0.0624, RankIC 0.0259 — highest mean total return, Sharpe, IC, and RankIC (AlphaGen 48.85%/2.82, AlphaForge 36.32%/1.97).
- Benchmark-relative: 21.49% cumulative excess return with 1.65 excess Sharpe (CSI300); 18.22% cumulative excess with 1.36 excess Sharpe (CSI500) vs an equal-weight benchmark from the same universe.
- Controlled multi-turn vs GRPO single-turn (same backbone/algorithm/splits/terminal reward): +7.31 pp total return, +0.43 Sharpe, +6.98 pp MaxDD, +0.0099 RankIC, comparable IC (0.0403 vs 0.0407) — iterative tool-based refinement is the source of the gain, not RL training alone.
- Design ablations (CSI300, single-run): full method 5.24 turns / 48.64% / 2.74 Sharpe; no memory feedback 15.75 turns / 26.40% / 1.70 — removing memory feedback halves return and triples rollout length; no pool auxiliary 34.39% / 2.06 but the best IC/RankIC (0.0419/0.0634) → the training proxy does not align with realized portfolio return; +reward auxiliary 44.49% / 2.50 (weaker than full → keep auxiliary terms in the pool score, omit from the reward).

## Actionable Insights
- Compact tried-factor memory steers the search: feeding back "what was tried + its score + current pool" each turn — without it the agent wanders (15.75 vs 5.24 turns) and is half as effective. Example: any code/factor-optimizing agent should keep a similar compact memory.
- Evaluate candidate signals by their contribution to the pool (NNLS-weighted meta-alpha), not by isolated IC: the variant with the best RankIC had the weakest return/Sharpe — optimize pool-level utility.
- Small model + task-specific RL beats big-model prompting: Qwen3-4B + GRPO multi-turn outperformed Qwen3-235B and DeepSeek-R1 direct-propose — invest in fine-tuning a small model rather than API calls to a large one, given an executable evaluator.

## Assumptions & Limitations
- Conditions: future-window data is NOT available to the inference policy (used only for offline reward computation); long-only top-K, daily rebalancing, 10 bps stylized costs.
- Limitations acknowledged: only small open-weight models trained (multi-turn GRPO is computationally expensive); top proprietary LLMs not benchmarked in the full multi-turn tool-using setting; evaluation covers one contiguous period (July 2025–March 2026) in two Chinese equity universes — cross-market generalization untested; the reward uses short-term future-window IC/RankIC proxies rather than a full backtest inside every trajectory — may miss drawdown control, capacity, liquidity, transaction-cost sensitivity, risk exposure; the protocol is simple (recent-window factor combination, long-only top-K) — not a complete trading strategy.
- Not stated: results are on A-share CSI300/CSI500 (retail-heavy, limit-up/down rules) and may not transfer to other markets; the seed factor library (Appendix) shapes pool initialization; 3-run means for AlphaPilot/AlphaGen/AlphaForge but single-run for other baselines — variance comparison is uneven; the IC/RankIC reward proxy may encourage overfitting to short windows.

## Metadata
- 2026, Peiqi Jiang, Fan Zhang, Xin Xu, Tianhao Chen, Can Yang (Department of Mathematics, Hong Kong University of Science and Technology), cs.CL, https://arxiv.org/pdf/2610.15488v1, citation count: not found [NO BENCHMARK]
