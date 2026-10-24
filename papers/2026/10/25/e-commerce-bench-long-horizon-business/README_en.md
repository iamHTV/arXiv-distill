# [2608.30730v1] E-Commerce Bench: Evaluating LLM Agents on Long-Horizon Autonomous Business Operation

## Core Value (1 sentence)

E-Commerce Bench is the first open-source benchmark that integrates multi-round counterpart negotiation and dynamic events into year-long business operation (365 days), evaluating 18 LLM models across 7 dimensions and finding a 1,264× factor between best and worst models — showing no model dominates all aspects of autonomous business operation.

## Problem

Prior work has not solved evaluating autonomous business agents on long-horizon tasks. Existing benchmarks either deviate from real-world market dynamics or rely on purely LLM-driven counterparts for multi-round negotiations, which introduces sampling noise and compromises credibility and reproducibility. Vending-Bench simulates vending machines but with mock data and prompt-based simulation yielding stochastic supplier feedback. YC-Bench runs a deterministic startup year but no supplier sourcing. MerchantBench and RetailBench have real data but drop negotiation and adversarial dynamics altogether. No benchmark combines: real data, deterministic negotiation, dynamic events, multi-store management, and a one-year horizon.

## Contribution

(i) E-Commerce Bench: the first open-source benchmark combining deterministic counterpart negotiation, dynamic events, and concurrent multi-store management over a one-year horizon.
(ii) Deterministic economy on both sides of the market: fixed demand model driving customer purchases/returns, deterministic negotiation kernel setting every pricing/concession/accept-reject decision, LLM only used to verbalize dialogue.
(iii) 6,886 products in 60 categories, 576 suppliers (424 honest, 152 fraudulent), data derived from a real e-commerce platform (Taobao & Tmall).
(iv) 18 tools across 7 groups, 128K token context window with group-wise eviction at 120K (release target 60K), persistent memory store (max 20 entries).
(v) Evaluation of 18 models across 7 dimensions: end-of-year assets, negotiation quality, fraud avoidance, cash flow/solvency, operational efficiency, operations execution, learning over horizon.
(vi) Results: GPT-5.6 Sol earns ¥1,431,425 (14.3× of ¥100,000 stake) but ranks 16/18 on fraud avoidance; Qwen3.8-Max-Preview leads open-weight tier with ¥416,252 (4.2×), places 5th overall; 1,264× factor between best and worst model; 10/90 episodes end insolvent.

## Method

E-Commerce Bench operates through 4 layers: (1) Agent loop layer: turn-based control, context management, persistent memory. Each turn the model can request multiple tools running sequentially. Each tool call (except day jump) charges simulated minutes (10 for balance check, 60 for opening store). Day runs 08:00–18:00 (600 minutes). Context eviction triggered at 120K tokens, releases down to 60K, oldest groups evicted first. Persistent memory store holds max 20 entries (title + content), fully curated by the agent. (2) Tool layer: 18 tools covering merchant back office across 7 groups, each with minute cost. (3) Environment layer: sales-and-economy engine beside two-layer negotiation engine. (4) Data layer: derived from real e-commerce platform.

Negotiation engine: each supplier splits into 2 layers. Layer 1 (Deterministic Negotiation Kernel): every price, concession, accept/walk-away decision comes from deterministic kernel, not a model. Layer 2 (NPC renderer): LLM turns each committed kernel decision into supplier chat, only taking tone from kernel's sentiment cue. ~1/4 of suppliers are fraudulent, running one of 5 scripted scam overlays. Price carries no fraud signal by design — decisive evidence is in the pre-deal narrative.

Demand model: demand for one SKU on one day = base category demand × 6 multipliers (price response, weekend uplift, promotion joined, month seasonality, calendar event, store reputation) × 2 capacity terms (category, store).

Evaluation: primary score = end-of-year total assets (bank account + platform wallet + unsettled escrow), reported as asset multiplier over ¥100,000 opening stake. Bankruptcy: 10 consecutive days with negative bank balance ends episode. 7 dimensions: (1) Negotiation quality (CSE+): share of bargaining range captured in closed honest deals; (2) Fraud avoidance (BadSpend%): share of order spending clearing into fraudulent supplier's account; (3) Cash flow/solvency: peak drawdown over peak total assets; (4) Operational efficiency: mean profit over mean tool calls; (5) Operations execution: controllable return rate; (6) Learning over horizon (AnchorRatio): overpayment on repeat orders vs cheapest price already won.

## KNOWLEDGE — Data & Concepts

- 18 models evaluated (8 proprietary, 10 open-weight), 5 episodes each, 90 total.
- 1,264× factor separating GPT-5.6 Sol (top) from Qwen3.5-Plus (bottom).
- GPT-5.6 Sol: ¥1,431,425 final assets (14.3× of ¥100,000), ranks 16/18 on fraud avoidance, trails Fable5 on operational efficiency.
- Qwen3.8-Max-Preview: ¥416,252 (4.2×), leads open-weight tier, 5th overall, strongest learning over horizon.
- 10/90 episodes ended insolvent, 6 under closed-source models.
- GPT-5.5, Claude Opus 4.6, Gemini 3.1 Pro, Qwen3.5-Plus account for all 10 bankruptcies.
- Claude Opus 4.7: captures most of bargaining range (0.811), leads bargaining and fraud avoidance.
- Kimi K2.6: captures least bargaining range (0.596).
- 6,886 products in 60 categories, 576 suppliers (424 honest, 152 fraudulent).
- 12 store types, max 4 concurrent stores (one per type).
- Opening store costs ¥500 + ¥60–130/day operating cost.
- Context window 128K tokens, eviction at 120K, release target 60K.
- Persistent memory store max 20 entries.
- Three-account deferred settlement: bank (costs paid immediately), escrow (revenue after shipping, minus platform commission), platform wallet (matures after 9 days, explicit withdrawal needed).
- Bankruptcy: 10 consecutive negative bank days.
- ~1/4 suppliers fraudulent, running 1 of 5 scripted scam overlays.
- Price carries no fraud signal by design.

## INSIGHT — Mechanism & Why

[1,264× factor between best and worst model] shows no model dominates all aspects of autonomous business operation — environment is deterministic given action sequence, so range belongs to agents. This means autonomous business operation is a strong differentiation environment where models vary greatly in combining capital, pricing, customer service, and operational obligations.

[No model dominates all dimensions] (GPT-5.6 Sol leads profit but ranks 16/18 on fraud avoidance; Claude Opus 4.7 leads bargaining and fraud avoidance but is mid-pack on profit). This means a single aggregate score (final assets) is insufficient to understand where an agent is strong or weak — multi-dimensional diagnosis is needed.

[Determinism on both sides of market] (fixed demand model + deterministic negotiation kernel) ensures outcome differences belong entirely to agent policy, not chance. This means benchmark can be exactly reproduced — two episodes with same action sequence end with same money.

[Learning over horizon (AnchorRatio) shows 16/18 models have no clear sign of bargaining price down over repeated orders] across 8,647 repeat purchases from same honest supplier. This means converting past experience into better future decisions is a critical deficiency in current models.

[Price carries no fraud signal by design] — decisive evidence is in pre-deal narrative, no fixed template can build it. This means agents must read dialogue context, not just prices, to detect fraud.

## IDEA — Actionable Applications

Apply [E-Commerce Bench] to evaluating business agents for Vietnamese solopreneurs: instead of just testing whether an agent can answer questions, create a simulated environment where the agent must run an online store for a year (source inventory, negotiate prices, set prices, ship orders, handle returns, manage cash flow) and measure final assets.

Apply [multi-dimensional analysis] to evaluating your own agent: instead of only tracking one aggregate score, evaluate separately across 7 dimensions (profit, negotiation, fraud avoidance, cash flow, efficiency, execution, learning) to know where your agent is strong or weak.

Apply [deterministic evaluation] to testing your agent: ensure evaluation environment is deterministic given same action sequence, so outcome differences belong entirely to agent policy, not randomness.

## WISDOM — General Principle

Principle: Evaluating autonomous business agents through final financial outcome combined with multi-dimensional diagnosis (not just one aggregate score) is more effective, because models can be strong on one dimension but weak on another, and a single score can hide important weaknesses.

When to use: When evaluating AI agents for commerce/retail operation or any application involving sequential decision-making over long horizons with financial consequences.

When NOT to use: When the agent only needs to perform short-horizon verifiable tasks without long-term capital management or adaptation to dynamic events.

Example outside original domain: Building a benchmark for automated investment agents — the agent must manage a portfolio of stocks, bonds, and cash over a year, with outcomes measured by final portfolio value and multi-dimensional analysis (risk, efficiency, learning from experience).

## Assumptions & Limitations

- Conditions for success: Real or synthesizable commerce data available; agent can use 18 tools across 7 groups; evaluation environment can run deterministically.
- Paper's acknowledged limitations: 5 episodes is a small sample, so every mean in Table 2 is printed with standard deviation; no evaluation on models smaller than frontier scale; no benchmark running cost evaluation.
- Limitations paper does NOT mention: No explicit Limitations section (paper ends at Conclusion then References); no evaluation of stability when market conditions change more severely than simulated; no evaluation on languages other than Chinese (data from Taobao & Tmall).

## Metadata

- Year: 2026
- Authors: Wei Fan, Xinjie Shen, Xudong Guo, Jianhong Tu, Yang Su, Yinger Zhang, Lianghao Deng, Fengyu Wang, Baohua Dong, Yangqiu Song, Dayiheng Liu
- arXiv category: cs.LG
- PDF link: https://arxiv.org/pdf/2608.30730v1
- Citation count: no information available