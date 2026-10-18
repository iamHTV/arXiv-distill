# [2609.11108v1] But How Would AI Agents Run a Town's Economy?

## Core value (1 sentence)
In a simulated economy of 100 LLM agents, money enters firms and STOPS — it never transmits to wages or prices — and the "frozen" wealth distribution is an artifact of observation horizons that are too short.

## Problem
- Prior work (AgentBench, WebArena, generative-agent societies) runs 1–2 simulated weeks, reports "human-like" behavior, and stops — never testing whether money/demand shocks actually circulate, because horizons are too short to see the wealth distribution evolve.

## Contribution
- A closed, money-conserving spatial economy of 100 memory-equipped agents on real Lakeside, Pokhara (Nepal) geography: 762 registered businesses, 3,981 menu items, a 19-action toolset, runs up to 26 simulated weeks.
- 91 validated runs, 2.44M agent decisions, 21.5B tokens, 41,328 pulses (60-sim-minute ticks); every rupee ledgered and verified by two independent validators (live TypeScript + offline Python recomputation in a second language).
- An identified mechanism for monetary transmission failure, decomposed exactly into extensive margin + intensive margin, corroborated by a randomized transfer experiment.
- The first direct evidence that study horizon changes the qualitative conclusion about wealth mobility.

## Method
Agents work shifts, run businesses, and set prices via 19 tools (navigation; local economy: buy_food/set_price/start_shift/pay_agent; memory: write_memory/search_memory/reflect; social: invite_to_talk/accept_invite/leave_conversation). Total money = sum of every agent's wallet + bank balance at each pulse, conserved exactly except through two ledgered external accounts (tourist inflow pool, government sink). Five treatment conditions: baseline, tourism-low, tourism-high, tourism-shock (12×), wealth-grant (NPR 5,000 to 20/100 agents at pulse 24); three ablation arms: layout-b (placebo), no-memory, cross-model (Qwen3.8-27B-FP8 → gpt-oss-20b). Seeds shared across arms for matched-seed pairing.

## KNOWLEDGE — Data & concepts
- 12× tourist shock → business revenue 4.62× (p<0.001) = 1.50× extensive margin (458 vs 304 of 762 businesses trading, p<0.001) × 3.07× intensive margin (revenue per business, p<0.001); 1.504 × 3.067 = 4.61 ≈ 4.62.
- Transmission stops at the firm: wages 1.03× (p=0.42); wage share of revenue collapses 0.90 → 0.45 → 0.20 (p=0.0001); only 0.27–0.32% of 3,981 menu items ever repriced (p=0.47); set_price called ~18 times/run out of ~28,000 calls.
- Windfalls do not circulate: 96.7% of the NPR 5,000 grant still held 311 pulses later; MPC (marginal propensity to consume) 3.3% and 4.0% by two independent measures, indistinguishable from zero (p=0.22, p=0.16), vs 0.2–0.5 for human households.
- Wealth persistence (Spearman ρ): 0.964 at 2 weeks (21% of agents change quintile) → 0.832 at 12 weeks (45%) → 0.752 at 26 weeks (46%); Gini relaxes 0.674 → ≈0.643 by week 16.
- Ablation: swapping the backing LLM moves EVERY outcome at the p=0.0039 floor (Gini +5.8%, median wealth −22.9%, mobility +62.4%, economic tool failure +110.4%); removing memory moves nothing detectably (p=0.56/0.69/0.16).
- Social coordination tools fail model-agnostically: invite_to_talk fails 94–97% (97.2% Qwen, 94.8% gpt-oss), accept_invite fails 100.0% of 1,413 calls, leave_conversation 97.7% — these three account for 79.6% of all tool failures; economic tools ~96% success.

## INSIGHT — Mechanism & why
- [Money stops at firms] BECAUSE agents have no incentive to raise wages/prices when demand rises — set_price is barely called — so demand growth is absorbed by the extensive + intensive margins of businesses, with no mechanical connection to wages or menu prices.
- ["Frozen" is a horizon artifact] BECAUSE the economy relaxes toward equilibrium on a ~10-week timescale — any study stopping at 2 weeks is right to report "static" but wrong to conclude "static".
- [Model choice > memory] BECAUSE the backing LLM's policy directly determines economic behavior; memory (in this configuration) changes no measured outcome — investing in memory before model choice is the wrong order.

## IDEA — Actionable applications
- When simulating a multi-agent marketplace/economy for business: ledger every transaction with a money-conservation invariant + two independent validators, then test a demand shock before trusting "plausible" results. First step: log every transaction, verify total money = sum of balances at each tick.
- Measure failure per tool/action, not aggregate success rate: 96% overall success can still hide one action class failing 94–100%. First step: log per-tool failure rates in your agent pipeline.
- Before adding memory/reflection to agents, swap the base model first — the effect is 3–10× larger. First step: A/B two models on the same task, measuring distributional outcomes (Gini, median wealth), not just accuracy.

## WISDOM — General principles
- "A distributional/stability conclusion is only as trustworthy as the horizon it was measured over" — a system that looks frozen at short horizons may be relaxing slowly; measure ≥2 horizons before concluding "stable". Applies beyond the domain: evaluate any churn/retention metric against the observation window.

## Assumptions & Limitations
- Conditions: agents follow a fixed toolset, closed economy, tourist inflow is the only money source.
- Paper acknowledges: small long-horizon sample (4 runs at 12 weeks, 1 at 26 weeks — a single path); underpowered memory null (6 matched seeds); price stickiness partly by construction (sticky menu design); one town, one seed pool, one stack (self-hosted vLLM); Mistral-Small-3.2-24B failing every pulse is stack-specific.
- Paper does NOT state: the cost of 21.5B tokens, transferability to non-spatial economies, effect of a prompting change (they state a falsifiable test but did not run it).

## Metadata
- Year: 2026, Authors: Sajal Regmi, Siddhartha Pudasaini, Chetan Phakami Pun (Karela Technologies Inc.), arXiv category: cs.MA (cs.ET), PDF link: https://arxiv.org/pdf/2609.11108v1, dataset: huggingface.co/datasets/sajalregmi4/agent-town-economy (CC BY 4.0)
