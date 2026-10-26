# Skill: Role- and Topology-Based Multi-Agent Red Teaming
Source: 2608.24069
Type: evaluation-method / framework

## When to use this skill
- Before deploying a multi-agent system with real action authority (trading, ordering, messaging, publishing).
- When you need to prove to yourself or stakeholders that the system is safe under a black-box threat model where the adversary only edits source data and prompts.
- Do NOT use: read-only systems with no actions; or infrastructure penetration testing (network/server) — this skill audits only the agent layer.

## Input required
- Pipeline with separated roles — at minimum: data-ingesting agent, reasoning/debating agent, acting agent, and (if present) a safety agent.
- One external LLM to play the adversary generating malicious content.
- A backtest or sandbox with post-cutoff historical data (to avoid lookahead bias) and a defined baseline portfolio (e.g. $100K) to measure $-impact.
- The list of communication topologies to compare (linear, centralized, decentralized vote, hybrid revision).

## Steps
1. Decompose roles and assign attacks by interface: source-data ingest agent -> data poisoning (adversary LLM rewrites N% of content inverting polarity) + indirect prompt injection (hidden directives in content); debate agent -> persuasive adversary (FOMO, appeal to authority); acting agent -> objective hijacking (prompt inverting the objective); final safety agent -> jailbreaking (hypothetical framing). Default poisoning ratio 10% (1:9), sweep 40%/80%.
2. Run attacks under both opposing target directions and compute ASR (Attack Success Rate) = decisions flipped to target / attackable days (where the clean decision differs from the target). Use two-proportion z-tests to compare attack tiers.
3. Build the topology matrix: keep the entry point fixed, run 4 routing/aggregation designs; compute APS (Adversarial Signal Preservation Score) = 1/(1+k(1-p)) with k = aggregation stages, p = 1 if voting — a predictive lens for robustness ordering, then verify against empirical ASR (check the correlation r).
4. Measure dollar consequences alongside ASR: per attack, compute signed EV (expected value) = mean portfolio capital change per attempt + median $ per success — rank danger by EV, NOT by ASR (a 97% ASR attack can median $0).
5. Conclude on defense placement: if the terminal node is also the decision node, split them; if using voting, ensure compromised agents stay a minority (<1/3) with independent (uncorrelated) sources; record ASR + EV + cumulative-return degradation per architecture.

## Expected output
- One ASR table by role x attack x target-direction, one ASR + EV table by architecture x backbone, an APS ordering vs the empirical ordering, and a concrete defense-placement list (split terminal role, voting threshold, independent agent sources).

## Example application
- A fintech startup with 3 agents (news analyst, sentiment analyst, trader, plus a final risk manager): a jailbreak prompt on the risk manager flips the decision on 98.9% of days (per the paper) -> conclusion: the risk manager must be an independent agent that never takes prompts from the trader, with hard constraints coded outside the LLM; the 3-analyst vote is trustworthy only while the threat model guarantees at most one poisoned channel (poisoning ratio <=10% and independent sources).

## Gotchas
- Evaluating only one backbone -> role results may not generalize; run at least two model families.
- Small attackable-day denominators (the clean system already leans one direction) -> noisy ASR; always report N and consider the unconditional target-rate change.
- Mangled PDF table extraction -> verify row mapping against prose before using numbers (conservation: each row's N must be <= 305 asset-days).
- Multi-agent reduces ASR but does NOT eliminate vulnerability — "safe because many agents" is wrong; it must come with deliberate validation, aggregation, and thresholds.
