# Skill: Validated Agent-Economy Simulation — conserved ledger + matched-seed ablation + horizon check
Source: 2609.11108v1
Type: evaluation-method

## When to use this skill
- You are building a simulation of multiple LLM agents in an economic/marketplace environment and need trustworthy results, not just "plausible on paper".
- You want to test a shock (demand, cash transfer, policy) and measure how it propagates through the system.
- You are about to report that a system is "stable/frozen" and need to be sure that is not an artifact of too short an observation window.

## When NOT to use this skill
- Single-agent tasks with no economic interaction or transactions between agents.
- You only need per-episode accuracy benchmarks — use AgentBench/WebArena-style evaluation instead.

## Required input
- Environment definition: agents, trading venues, tools, the single source/sink of money.
- Inference budget for multiple runs × seeds × horizons.
- Pre-registration: conditions, seed list, exclusion rule — committed BEFORE data collection.

## Steps to execute
1. Design a closed economy with money conservation as the invariant: ledger every transaction; total system money = sum of all agent wallets + bank balances at each pulse; money enters/exits only through two ledgered external accounts.
2. Run two independent validators: a live validator (TypeScript) plus an offline recomputation in a second language (Python), including per-agent ledger reconciliation: Δ balance of an agent = the signed sum of that agent's own transactions.
3. Design treatments with a manipulation check: confirm the shock landed (δ = 1.00 separation, p_adj < 0.001) before measuring downstream effects — a downstream null cannot be blamed on a weak shock.
4. Decompose the response into extensive margin (how many units participate) + intensive margin (how much each participating unit earns); verify the multiplication identity: 1.504 × 3.067 ≈ 4.62.
5. Matched-seed ablation: seeds shared across arms; run placebo (layout), no-memory, cross-model; report Δ% + p (Wilcoxon signed-rank).
6. Horizon ladder: run ≥3 horizons (e.g., 2/12/26 weeks); measure persistence ρ + quintile mobility at each level before concluding "frozen".
7. Report per-tool failure rates, not just aggregate success rate; log the frequency of each error reason.

## Expected output
- Simulation results with an audit trail: every headline number recomputable from raw CSV exports.
- An identified mechanism (e.g., monetary transmission stops at the firm) with an exact decomposition + a randomized transfer experiment corroborating it.
- Conclusions labeled with their horizon; dataset released for reanalysis.

## Example application
You simulate 50 agent customers for a loyalty program: ledger every loyalty-point transaction, run a shock "gift 5,000 points to 10 random agents", measure that 96% of points are still held after 300 pulses → MPC 3–4% → conclude "promotions do not circulate" instead of "program is 96% successful".

## Gotchas
- A 96% aggregate success rate can hide one action class failing 94–100% (paper: invite_to_talk fails 94–97% while economic tools succeed 96%) — always split per-tool.
- Self-hosted serving quirks: FP8 KV-cache quantization causes garbage tokens (6.0% → 3.3% when disabled); tool-name normalization rescued 16–35% of actions — replay recorded production requests when probing reliability.
- Pre-commit the exclusion rule before collecting data: the paper dropped 1 run on a pre-committed 3σ floor even though it completed — the rule decides, not the analyst.
- A null result with 6 seeds means "not detected", NOT "no effect" (paper: memory null underpowered).
