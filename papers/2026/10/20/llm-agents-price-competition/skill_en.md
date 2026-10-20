# Skill: LLM Pricing Deployment Audit (evaluating pricing regimes of LLM agents)
Source: 2610.21711v1
Type: evaluation-method / framework

## When to use this skill
- You build or use an LLM pricing agent for e-commerce, marketplaces, ad bidding, dynamic pricing.
- Before deploying a pricing agent to a real market — compliance check + consumer welfare audit.
- Do NOT use: agents that do not set prices (content/support agents); markets without repeated feedback loops.

## Inputs needed
- Deployment spec with 6 components: H (history representation + memory window), A (action space: continuous / grid), O (output: point price / probability distribution), Delta (update cadence), M (persistent state / scratchpad), P (prompt framing).
- Market model: demand form (logit / winner-takes-all), n firms, cost c, grid K, horizon T.
- Opponent ecology: standard learners (Exp3/UCB/PPO/FTRL...) vs LLM agents vs heuristics.
- Logging: per-period price path, profit share, consumer share.

## Steps
1. Set benchmarks: competitive region (finite-grid Nash region) + joint-profit benchmark; compute price-elevation index Delta (0 = Nash, 1 = monopoly) over the final-third window of each run.
2. Self-play with at least 2 opposing deployments — (point + raw history + rival visible) vs (distribution + summary + interval 25) — 5-10 seeds each. WARNING: point+raw self-play Delta > 0.5 = high-price regime.
3. Matchup vs standard learners (T=2,000, 10 seeds): measure share of cumulative industry profit; a D-S-style agent is expected to earn 71-72% by undercutting (pricing below the rival 57-60% of late periods), not via high prices.
4. Protocol ablation: from the control, change the information interface — hiding rival prices + summarizing history cause the largest movements (0.97 -> 0.56/0.53/0.31); changing action representation alone (point->grid->distribution) does NOT change the regime (1.01-1.05).
5. Assign regime labels: high-price lock-in, anchor-and-harvest (re-anchor high, then briefly undercut to harvest demand), competitive undercutting, Nash-like. Detect anchor-and-harvest by the reset-up -> brief undercut pattern in the price path.
6. Welfare + audit logging: measure consumer share per regime (15% P-R-1 vs 95% D-S); log model version, prompt, observation stream, memory state, price recommendation, sampling procedure, human overrides.

## Expected output
- Regime map: deployment x opponent -> regime label + elevation index + consumer share; a clear recommendation of which deployment to launch / redesign / block before market entry.

## Example application
- Vietnamese marketplace, 2 sellers using a Gemini-class agent: deployment X (point + raw 100-period rival history, every period) self-play Delta_H = 0.88, consumer share 15% -> redesign to Y (distribution + per-price summary, interval 25) -> self-play 0.05, consumer 95%; vs Exp3: X 63% / Y 71%. Launch Y, block X.

## Gotchas
- Single-run heterogeneous markets (n=1 per run) are representative paths, NOT treatment effects — replicate before concluding.
- Hiding rival prices is NOT automatically pro-competitive: in hidden P-R-1-D-S-1, D-S-1 still learns a threshold below the anchor and takes 71% of profit.
- Traces (plans/insights) are behavioural artefacts, not hidden computation: collusive outcomes may be invisible in chain-of-thought.
- High prices do NOT follow from cumulative-reward optimization: PPO still converges to Nash — never assume "long-run optimizing agent = collusion".
- The surrogate (DBBS) is not a no-regret guarantee — do not use it for worst-case pricing.

## Dry run test
- Hypothetical case (2-seller marketplace, Gemini-class agent): Step 1 benchmark: K=21, c=0.10, ceiling 0.36, competitive region {0.100, 0.113, 0.126}. Step 2: X self-play 5 seeds mean Delta_H 0.88 (ceiling lock-in); Y mean 0.08. Step 3: vs Exp3, T=2,000, 10 seeds: X 63%, Y 71% (Y lower-priced 57-60% of late periods). Step 4: ablation from X: hide rival -> 0.56; summary -> 0.53; both -> 0.31; grid-distribution-only -> 1.03 (unchanged). Step 5: X = high-price lock-in; Y = Nash-like. Step 6: consumer share X 15% vs Y 95%; logging spec emitted. Output: regime map + "launch Y, block X" — meaningful and followable -> [SKILL VALID].
