# [2610.26438v1] Fake News, Real Crashes: Information Injection Attacks on LLM Financial Trading Agents

## Core Value (1 sentence)
Information injection attacks on LLM trading agents achieve 62% mean ASR, 4.5× more effective than prompt injection (14%); two 30-word fact-poisoning templates reach 100% on all 15 stocks, and only hierarchical aggregation (star pipeline) reduces ASR to 9–10%.

## Problem
Prior LLM security work focuses on the control plane (system prompt, role, tool routing, jailbreak), leaving the data plane — information the agent is built to act on — undefended. A single fabricated headline can push many agents reading the same feed into the same trade at the same moment, causing real financial harm.

## Contribution
1. Formulate information injection as a distinct data-plane threat to LLM agents, separate from control-plane prompt injection, and build a systematic attack framework for it.
2. Large-scale measurement: across the benchmark, information injection is 4.5× more effective than control injection, generalizes across model vendors, and remains effective under realistic unlabeled blending into real news feeds.
3. Build a 62-template benchmark crossing five vectors (V1–V5) with seven event categories, and establish the defense criterion: score content conditional on agent posture and report ASR at a fixed false-positive rate.

## Method
The attack framework operates along two orthogonal axes: the vector axis (V1–V5: how content is corrupted) and the event axis (seven categories: CA corporate actions, GI governance/insider/short, RG regulatory/legal, EA earnings/analyst/operations, MS market structure/options, MA macro/geopolitical, NA narrative/sentiment). The reference agent is a single-shot trend-following trader on GPT-4o-mini, receiving a market snapshot (OHLCV, RSI, MACD, Bollinger bands, EMA20/50/100/200, ATR, VWAP) plus free-text news context, and emitting a structured BUY/SELL/HOLD decision. The attacker has only a public posting capability (e.g., on X), with no knowledge of agent prompt/model/weights, no ability to alter code/training data/system prompt, and no capital or broker access. ASR measures the fraction of decisions changed from the benign baseline (temperature 0 vs 0.1, R=10 repetitions). The benchmark comprises 62 templates (25 vector-grounded, 37 event-grounded), evaluated on 15 U.S. stocks over ~10,000 trading decisions. Three multi-agent topologies are tested: Linear (NewsAnalyst→RiskEvaluator→Trader), Star ({Fundamental, Technical, Sentiment} analysts→Aggregator→Trader), Debate (three independent analysts, two-round exchange, trader acts on full debate record).

## KNOWLEDGE — Data & Concepts
- Information injection (II) mean ASR: 62%; Control injection (CI) mean ASR: 14%; 4.5× gap (3.8× conservative)
- Two 30-word V1 fact-poisoning templates ("CEO arrested overnight", "CFO resigned after admitting revenue inflation"): 100% ASR on all 15 tickers, zero variance
- Per-ticker ASR: MSFT 34% (most resistant) to AMZN 87% (most exposed); 6 HOLD-baseline tickers avg 68%, 5 BUY-baseline tickers avg 48%
- Vector V4 (structured-signal poisoning, fake indicator panel): 91% ASR vs HOLD-agent, 12% vs BUY-agent (7.6× gap)
- Vector V1 (fact poisoning): 69% vs HOLD, 100% vs BUY (only vector strong on both baselines)
- Credibility surface cues: removing source noun or urgency cue ("BREAKING") drops ASR from 100% to 0% with unchanged fake claim
- Event categories: RG 67%, GI 64%, CA 58%, MS 54%, EA 49%, MA 46%, NA 26%
- Steerability: 87% of successful flips match intended direction (474/543)
- Entity grounding: untailored reuse across tickers transfers at 7% mean ASR
- Feed rate limiting: padding 12–240 extra headlines, ASR remains 100% in all 12 configurations
- Model scaling: GPT-4o reduces V4/V5 to 0% but V1 stays at 93%; GPT-5 reasoning model at 45% mean ASR
- Cross-vendor blended injection: 46–72% across 4 models, 3 vendors
- Economic impact: each injection drives $16K induced notional (~80% of $20K buying power) in attacker-chosen direction
- Defenses: Star pipeline (hierarchical aggregation) reduces ASR to 9%; Linear to 28%; Debate to 74% (no protection); only hierarchical aggregation significantly reduces ASR

## INSIGHT — Mechanism & Why
[Information injection is 4.5× more effective than prompt injection] BECAUSE [instruction-style payloads cannot override the fixed objective the trading policy pursues, while adversarial information is precisely the content the policy is built to act on, so it passes through the policy without breaking any rules]. This means [control-plane security benchmarks do not make a model safe to deploy as a trader].
[100% ASR fact-poisoning templates] BECAUSE [the agent responds to surface credibility markers (named source, urgency cue) rather than verifiable evidence, and LLM-generated fake news reproduces these markers at near-zero marginal cost]. This means [the agent verifies which entity a claim concerns but does not verify the claim itself].
[Success depends on agent state] BECAUSE [a fake indicator panel easily creates a decision where the agent planned no trade (HOLD), but cannot contradict a BUY that real in-context indicators already justify]. This means [attacker chooses vector matching agent posture: V4 to manufacture a new decision, V1 to reverse a planned entry].
[Hierarchical aggregation works, peer debate does not] BECAUSE [the star pipeline's aggregation/risk-review stage cross-checks the injected claim against other analysts' independent assessments and real in-context indicators, while symmetric two-round debate manufactures apparent consensus around the injected narrative]. This means [architectural complexity only protects when deliberation is hierarchical and cross-checking; symmetric debate provides essentially no protection].

## IDEA — Actionable Applications
1. Apply [Star/hierarchical aggregation topology] to [protecting high-stakes LLM agent decisions]: first step is to deploy three independent analysts (fundamental, technical, sentiment) + an aggregator that cross-checks claims before the trader acts, instead of letting one agent handle everything.
2. Apply [entity grounding] to [detecting corrupted content]: first step is to configure the agent to verify which entity a claim concerns and refuse to act if the claim targets a different entity.
3. Apply [action-conditioned gating] to [limiting damage from a single attack]: first step is to set higher evidentiary thresholds as position delta grows, so no single unattested item can change the portfolio by more than a fixed fraction.

## WISDOM — General Principles
1. Principle: The data plane (information the agent is built to act on) is a larger attack surface than the control plane (system instructions). Apply when: evaluating security for high-stakes LLM agents (finance, healthcare, legal, operational). Do not apply when: only needing basic prompt injection benchmarks.
2. Principle: Hierarchical aggregation with cross-checking is the only measured defense that significantly reduces ASR; larger models only help partially. Apply when: designing architecture for financial trading or decision agents. Do not apply when: considering symmetric peer debate as sufficient protection.

## Assumptions & Limitations
- Conditions that must hold: agent reads unauthenticated public news sources, agent has a fixed trading policy (trend-following), attacker has only public posting capability.
- Limitations acknowledged by paper: online experiments only in one specific scenario; reference agent is simple (130-line Python, GPT-4o-mini); no real broker or capital; no data on number of automated readers in the 2013 AP crash.
- Limitations paper does NOT mention: real inference cost of hierarchical aggregation vs single agent; added latency from aggregation/cross-checking steps; no evaluation on non-finance tasks (healthcare, legal, etc.).

## Metadata
- Year: 2026
- Authors: Mengxiao Wang, Nitesh Saxena (Texas A&M University)
- arXiv Category: cs.CR
- PDF Link: https://arxiv.org/pdf/2610.26438
- arXiv ID: 2610.26438v1
- Label: [applied]
- Citation count: [not found]