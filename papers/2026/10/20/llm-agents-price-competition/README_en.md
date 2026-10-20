# [2610.21711v1] How language model agents reshape price competition

## Problem
- Repeated-game theory is an existence theory, not a selection theory: it says which outcomes CAN be sustained, not which outcome a concrete adaptive process will SELECT. Standard online learners (Exp3, UCB, PPO) in homogeneous Bertrand competition almost always converge to the stage-game Nash equilibrium (price = marginal cost) — a good benchmark for consumer welfare. Which long-run price regime LLM pricing agents select was unknown.

## Contribution
- Shows the SAME foundation model selects opposite regimes (monopoly-level vs Nash-level) purely via DEPLOYMENT interface changes: output (point price vs probability distribution), history (raw vs summarized), rival-price visibility, update cadence.
- Separates two private-profit sources of LLM agents: (a) exploitation of slow-learning via undercutting (D-S-25), (b) high-price anchoring + anchor-and-harvest (P-R-1).
- Builds DBBS (downward-biased belief search), a surrogate algorithm that reconstructs D-S-25's policy on held-out data — an ordered payoff-feedback search with inertia.

## Method (core)
- Simulated markets: (a) homogeneous winner-takes-all: K=21 price grid, c=0.10, ceiling 0.36, T=2,000; (b) differentiated multinomial-logit: pNash~1.473, pmonopoly~1.925.
- 7 experiment families: round-robin of 7 standard learners (T=10^7 periods, 10 seeds); LLM vs learners; LLM self-play; protocol ablations from a control; mixed deployments (P-R-1 vs D-S-1/P-S-1, 3-4 agents, visible/hidden rival price); robustness families (prompt, GPT-5.6 Terra, demand).
- Deployment code output-history-interval: P-R-1 (point/raw-100/1), D-S-25 (distr/summary-75/25), D-S-50 (distr/summary-150/50); base model Gemini 3 Flash Preview, temperature 0.7. Measures: price-elevation index Delta (0 = Nash, 1 = joint-profit), profit share, consumer share.

## Key Findings
- Benchmark: 20/21 markets without UCB reach the competitive region after 10^7 periods; UCB self-play price index 0.93 (217 profit units — the only >5%-of-monopoly cells: UCB self-play 217, PPO-WFP 87, UCB-PPO 47; all others <=7.1).
- D-S-25 vs Exp3/BM-RM/PPO/UCB (2,000 periods, 10 seeds): 71-72% of cumulative industry profit; in final 10% it prices BELOW the learner 57-60% of periods — profiting from fast undercutting, NOT high prices.
- P-R-1 vs Exp3 (n=1, 300 periods): 63%; vs win-up-lose-down heuristic: matches price from period 3, ceiling at period 21, 50/50 split; vs coin betting: coin betting earns 71%, P-R-1 abandons its anchor ~period 200, prices fall to ~0.19.
- Self-play in the SAME homogeneous market: P-R-1 elevation 0.88 (n=5) vs D-S-25/D-S-50 0.05 (n=10) — two opposite regimes.
- Ablation: changing action representation alone (point->grid->distribution) keeps elevation high (0.97/1.05/1.03/1.01); changing the information interface: hide rival 0.56, summarize history 0.53, both 0.31, full D-S-50 bundle 0.13 (n=5 per row) — the information interface, not the output type, selects the regime.
- P-R-1-D-S-1: visible rival -> lock-in at 0.356, joint profit 98% of monopoly, D-S-1 takes 66%; hidden rival -> anchor-and-harvest cycles, average 0.26, D-S-1 takes 71%. 4xP-R-1: ceiling 0.36 from period 74, 25% each; 3xP-R-1: recurrent resets 0.11-0.35, profit 42/34/23%.
- Welfare: consumers keep 15% of surplus under P-R-1 self-play vs 95% under D-S-25/D-S-50 self-play; 72-84% when D-S-25 undercuts learners. Logit market: Fish-style control loses 12.9% of Nash welfare; the D-S-50 bundle loses 0.8%.
- Traces: opponent-facing motifs 94% (P-R-1) vs 34% (D-S-25); payoff-region motifs 98% vs 21%; raw+visible -> 96-99% opponent-facing; summarized+hidden -> 3-6%.

## Actionable Insights
- Audit the 6 deployment components (H, A, O, Delta, M, P) BEFORE launch: same model, different interface -> opposite regime. E.g. replacing raw rival-price history with summarized history + distributional output + 25-period cadence (D-S-25-style) moves self-play 0.88 -> 0.05 and consumer surplus 15% -> 95%.
- Against standard online learners (Exp3/UCB), LLM agents profit from faster adaptation (D-S-25 takes 71-72% via undercutting) — but the advantage DISAPPEARS vs full-information learners (coin betting beats P-R-1 71%). Never assume LLMs always win.
- Platform operators: offer lagged/aggregated market feedback instead of raw rival-price histories to weaken high-price conventions; require logging of model version, prompt, observation stream, memory state, price recommendation, sampling procedure, human overrides.

## Assumptions & Limitations
- Conditions: repeated market with feedback loop; grid action space; demand model known to researchers (agents are NOT told it).
- Authors admit: stylized Bertrand markets (no inventory, search, consumer heterogeneity, multi-product portfolios, platforms, asynchronous updates); traces are behavioural artefacts, not hidden computation; collusive outcomes may be invisible in chain-of-thought; single-run heterogeneous cells (n=1) are representative paths, not treatment-effect estimates; DBBS is not a no-regret guarantee.
- Not stated: only 2 base models (Gemini 3 Flash Preview, GPT-5.6 Terra) — vendor-dependent; D-S-25/D-S-50 frozen via self-play configuration screening — opponent-ecology overfitting risk; replicated P-R-1-vs-learner evidence only vs Exp3; other matchups illustrative.

## Metadata
- Year: 2026 | Authors: Martin Bichler, Philip Hierhager, Kassian Köck, Fabian Pieroth (TU Munich) | Category: cs.GT | PDF: https://arxiv.org/pdf/2610.21711v1 | Citations: [NO DATA — published 15 Oct 2026]
