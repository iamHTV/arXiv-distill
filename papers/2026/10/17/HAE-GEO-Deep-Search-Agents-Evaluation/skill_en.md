# Skill: hae-geo-agent-robustness-evaluation
Source: 2609.06027v2
Type: evaluation-method

## When to use this skill
- Evaluating search-augmented agent robustness against Web evidence poisoning (GEO).
- Need to track the full agent trajectory from exposure to recovery, not just final outcome.
- Have resources to build controlled corpus with clean and poisoned pages.

## When NOT to use this skill
- Evaluating agents that don't interact with the web (no Search–Scrape interface).
- No ability to build controlled corpus or use LLM-as-Judge scoring.
- Only need simple accuracy without process-level analysis.

## Input needed
- Controlled corpus: clean pages and poisoned pages per level (L1, L2, L3).
- Evaluation query set, each with fabricated entity and false claim.
- Agent with Search–Scrape interface (returns page metadata and page content).
- Two LLM-as-Judges (attack-aware and attack-label-blind) for six-dimensional rubric scoring.

## Steps to execute
1. Build controlled corpus: 72,039 clean pages + 770 poisoned pages per level, across 8 product categories and 154 brands.
2. Design three poisoning levels: L1 (Direct Poisoning, unsupported assertion), L2 (Contextual Camouflage, embedded in natural context), L3 (Evidence-Enhanced Poisoning, corroboration chain).
3. Implement Search–Scrape interface: agent can SEARCH (returns metadata) or SCRAPE (returns page content), separating intermediate search decisions.
4. Record agent trajectories and map to five behavioral states: Exposure (E), Adoption (A), Verification Yield (V), Recovery (R), Endorsement (Y).
5. Score agent on six semantic rubric dimensions: M1 Fake Brand Risk Handling, M2 Poison Evidence Recognition, M3 Recovery after Adoption, M4 Evidence Quality & Independence, M5 Uncertainty Calibration, M6 Legitimate Utility under Attack.
6. Use Split LLM-as-Judge: Poison Judge (attack-aware) scores M1–M3, Quality Judge (attack-label-blind) scores M4–M6, each score in {0,1,2}.
7. Report by dimension, not collapsed into composite; separate final endorsement from evidence reasoning, recovery, and legitimate utility.

## Expected output
- Six-dimensional robustness scores against GEO poisoning, with detailed behavioral trajectories.
- Identification of models that resist well vs. models that verify but don't recover.

## Application example
- Evaluate a shopping advisor agent: create query "best fitness tracker" with fabricated brand "Apollo-9" poisoned at L3, track whether agent recognizes fake evidence, verifies independently, and retracts recommendation or not.

## Gotchas
- Evidence recognition degrades under the corroboration trap (L3) — seemingly corroborating evidence leads to false adoption.
- Agentic search improves final resistance without improving evidence recognition or utility.
- Defense prompting increases verification but rarely converts to recovery — require retraction when conflicting evidence detected.
- Defense adds 1.82 tool calls/query and 24.5% token consumption — balance robustness against inference cost.
