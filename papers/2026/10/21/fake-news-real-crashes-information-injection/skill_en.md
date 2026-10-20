# Skill: info-injection-defense-star-pipeline

Source: 2610.26438v1
Type: framework / workflow

## When to use this skill
- When protecting high-stakes LLM agent decisions (financial trading, healthcare, legal, operational) from information injection attacks via unauthenticated public news sources.
- When wanting to design agent architecture capable of cross-checking claims before taking critical actions.
- When needing to evaluate agent risk from reading unauthenticated sources and set up appropriate defenses.

## When NOT to use this skill
- When only needing basic prompt injection benchmarks (control-plane).
- When lacking resources to run multiple agents (hierarchical topology needs at least 3 analysts + 1 aggregator + 1 trader).
- When the task doesn't involve high-stakes financial/risk actions needing protection.

## Required inputs
- Reference agent (trading policy or decision policy) with inputs: market data + free-text news context.
- Independent analysts (fundamental, technical, sentiment) to evaluate requests from multiple viewpoints.
- An aggregator to cross-check injected claims against independent assessments and in-context market indicators.
- GPU resources for multiple LLM calls before the agent may act.
- Trust score threshold and action gating process based on trust score.

## Steps to execute
1. Deploy Star topology: three independent analysts (fundamental, technical, sentiment) read the same news feed, an aggregator cross-checks injected claims against independent assessments and in-context indicators, the final trader receives a filtered summary.
2. Apply entity grounding: configure the agent to verify which entity a claim concerns (stock ticker, company), refuse to act if the claim targets a different entity.
3. Set up action-conditioned gating: set higher evidentiary thresholds as position delta grows, so no single unattested item can change the portfolio by more than a fixed fraction.
4. Evaluate defenses: replay attack templates from the 62-template benchmark, measure ASR-after-defense and FPR on benign news, plot Pareto ASR-vs-FPR curve as trust threshold sweeps.
5. Compare against two anchors: undefended reference agent (ASR = 61.7%, FPR = 0%) and star pipeline (ASR = 9.5%, FPR ≈ 0%).

## Expected output
- A multi-tier agent system capable of reducing ASR from 62% to 9–10%.
- Evaluation report: ASR-after-defense, FPR, ASR-vs-FPR curve.
- Deployment decision: deploy star pipeline, adjust trust threshold, or add supplementary protections.

## Example application
An asset management firm uses an LLM agent to place stock buy/sell orders. They deploy Star topology: fundamental analyst reads financial reports, technical analyst reads market indicators, sentiment analyst reads social media news; aggregator cross-checks whether a "CEO arrested" claim contradicts real-time indicators and other reports; trader only acts when aggregator trusts it. Expected results: ASR drops from 62% to under 10%, agent not fooled by single fake news item.

## Gotchas
- Larger models only help partially: GPT-4o reduces V4/V5 to 0% but V1 (fact poisoning) stays at 93%; GPT-5 at 45% mean ASR. Model choice is not a reliable defense.
- Online results only from one specific scenario; cannot generalize directly to all platforms.
- Hierarchical aggregation and cross-feed corroboration add model calls before the agent may act, during the wall-clock window in which news edge decays.
- Content-only defense cannot raise true-positive rate without paying matching false-positive rate on real breaking news.