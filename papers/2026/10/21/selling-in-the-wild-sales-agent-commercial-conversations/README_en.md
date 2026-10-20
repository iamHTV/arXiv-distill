# [2610.25461v1] Selling in the Wild: Benchmark and Randomized Field Evidence for a Sales Agent Trained on Commercial Conversations

## Core Value (1 sentence)
A sales agent fine-tuned on 4.6 million real commercial conversations increased revenue per visitor by +10.0% versus no agent, and outperformed a frontier model with identical scaffolding by +21.6% engaged conversion, at just 1.8% of the cost per conversation of human sales staff.

## Problem
Prior work has not tested whether a sales agent trained on real commercial conversations increases sales on live traffic — existing benchmarks use artificial customers (simulators) that can reorder the leaderboard (correlation only r=0.24 between two simulators on SalesLLM), and previous field experiments predate current models or only measure assistance to human agents, not autonomous selling.

## Contribution
1. A four-study evaluation protocol linking offline benchmark scores to randomized revenue outcomes on live traffic.
2. A battery of 100 consenting websites across 14 industries, each with a pre-specified primary metric.
3. A model-isolating comparison: Javo versus a frontier model inside identical scaffolding (interface, retrieval, catalog tools, system prompt, guardrails), so any difference is attributable to model weights.
4. A randomized comparison with each site's own live-chat associates, including cost, latency, and CSAT alongside conversion.

## Method
Javo is an open-weight model (Qwen3-32B) fine-tuned on entire commercial conversations: supervised fine-tuning on 1.65 million examples (2 epochs) to learn elicitation, recommendation, objection handling, and next-step proposals in context rather than from isolated prompts; then preference optimization on 190,000 pairs of seller turns at matched conversation states, where the preferred turn preceded progress (stated purchase intent, booking, lead) and the dispreferred turn preceded a stall or exit. A third data mix teaches constraints: no discounts or terms absent from the site's policy, no claims absent from the catalog, AI disclosure on request, and handoff to a human on request. All agent arms run in the same scaffold (widget, catalog retrieval, tools, prompt, guardrails, 8-second latency budget), differing only in model weights. The three field studies randomize visitors across 100 websites (May 1 to September 30, 2026, 14.8 million unique visitors), with each visitor assigned fixed to one arm for the duration of the study.

## KNOWLEDGE — Data & Concepts
- Training corpus: 4.6 million conversations (after filtering), 58.4 million turns (median 10 per conversation), English 68%, French 16%, Spanish 8%, other 8%, collected February 2024 to March 2026, ending before May 1, 2026; 17.4% have a joined outcome label; residual PII rate on audited sample of 2,500: 0.16%
- Training settings: base model Qwen3-32B; SFT 1.65 million examples / 2 epochs; preference pairs 190,000; constraint examples 34,000; 32 H100 GPUs, 2,240 GPU-hours; frozen model version javo-v1 on April 24, 2026
- Study 1 (SalesLLM-EN, CustomerLM): Javo 7.01 (95% CI 6.87–7.15), best frontier model 6.21, S1a threshold 6.33; Javo base model 5.73; Javo SFT only 6.51; Javo without constraint data 7.13; human sellers 1–3 years experience 6.13; human sellers 5+ years 6.88
- SmartSalesBench: Javo 0.79 vs best frontier 0.69
- τ-bench retail pass1: Javo 73.0%, best frontier 73.0% (guardrail held)
- Study 2 (vs no agent): RPV +10.0% (95% CI +5.1 to +14.9); conversion +8.0% (+4.1 to +11.9); engagement-scaled RPV illustration +123.9%
- Study 3 (vs frontier agent GPT-5.2, identical scaffolding): engaged conversion +21.6% (+16.9 to +26.3); ITT RPV +16.9% (+11.2 to +22.6)
- Study 4 (vs live-chat human associates): engaged conversion +0.5% (−5.0 to +6.0), non-inferior (margin −7%, one-sided p=0.004), no significant superiority; CSAT Javo 4.42 vs humans 4.43
- Cost per engaged conversation: Javo $0.06, frontier $0.14, human $3.40 (Javo = 1.8% of human cost)
- Guardrails (all held): return rate per order 4.0% vs no agent 4.1% (margin ≤ +0.5 pp); cancellation rate 11.9% vs 12.2%; complaints per 1,000 visitors 0.18 vs 0.20; unsupported claims 0.15% vs frontier 0.56% (margin ≤ 1.0%); unauthorized offers 0 vs frontier 3 (zero tolerance); prohibited pressure tactics 0.01% vs frontier 0.05% (margin ≤ 0.1%)
- Sales behaviors (share of engaged conversations): needs elicited before first recommendation Javo 82% vs frontier 61% vs human 81%; recommendation tied to stated need Javo 78% vs 58% vs 72%; objection raised and resolved Javo 60% vs 39% vs 57%; concrete next step proposed Javo 88% vs 68% vs 78%; median messages per conversation Javo 8 vs frontier 6 vs human 9

## INSIGHT — Mechanism & Why
[Training on entire commercial conversations] happens BECAUSE [the model learns to handle needs, objections, and next-steps in multi-turn context rather than answering from isolated prompts]. This means [data from real commercial conversations, not model scale alone, determines how well an agent sells].
[When scaffolding is held fixed, the conversation-trained model outsells the frontier model] BECAUSE [the frontier agent behaves like a passive question-answering bot rather than an active salesperson, while Javo learned from conversations where customers state needs, hesitate, object, compare, and then buy or not buy]. This means [good scaffolding cannot substitute for domain-specific data].
[Javo is non-inferior to human sales staff at 1.8% of the cost] BECAUSE [the agent does not get tired, needs no salary, responds instantly, and has low inference cost, while still achieving equivalent conversion]. This means [cost is the main competitive advantage of AI sales agents, not just conversation quality].

## IDEA — Actionable Applications
1. Apply [fine-tuning on real sales conversation transcripts] to [building a sales agent for an e-commerce website]: first step is to collect and de-identify 10,000+ old live-chat conversations from the website, label outcomes (purchase/cancel/lead), then SFT an open-weight model (e.g., Qwen3-32B) on this corpus before deploying.
2. Apply [comparing agent vs frontier model within identical scaffolding] to [testing whether fine-tuning adds value]: first step is to deploy two agents (fine-tuned model vs frontier model) with the same widget, catalog retrieval, tools, and system prompt on 10% of traffic, measuring engaged conversion and RPV over 2–4 weeks.
3. Apply [1.8% cost versus human sales staff] to [replacing or supplementing live chat outside business hours]: first step is to configure the agent to handle all messages outside business hours, hand off to a human when requested, and track CSAT and conversion rate weekly.

## WISDOM — General Principles
1. Principle: Domain-specific conversation data matters more than model scale for goal-oriented sales tasks. Apply when: building specialized agents (sales, consulting, support) with historical transcripts available. Do not apply when: the task is general Q&A without a measurable business outcome.
2. Principle: Agent comparison must hold everything constant (scaffolding, prompt, tools) and vary only model weights, otherwise you cannot know where improvement comes from. Apply when: evaluating any newly fine-tuned model. Do not apply when: only needing a quick marketing demo.

## Assumptions & Limitations
- Conditions that must hold: website has at least 20,000 sessions/month, has server-side order/booking/lead events joinable to visitor ID, has machine-readable catalog or inventory feed, no AI sales agent already live, written consent from owner to randomize visitors and share de-identified outcome data; financial advisory sites run lead-capture mode only.
- Limitations acknowledged by paper: the 100 sites are not a random sample of the web (many came through author's client/agency network); sites with heavy pre-purchase questions are over-represented by design; effects on low-consideration purchases may be smaller; frontier baseline is one model version frozen April 24, 2026; disclosure confound in Study 4; associates are typical existing staff not best salespeople; 5-month horizon does not capture lifetime value, repeat purchase, or brand effects; interference on inventory-limited sites; Study 1 depends on artificial buyers; results may not transfer to under-represented languages; no study of buyer-side agents.
- Limitations paper does NOT mention: no independent statistical review (author is Founder/CEO of AISO Boost Ltd.); no study registration or external ethics approval claimed; no data on actual average agent latency; no per-website breakdown (only pooled and by-industry).

## Metadata
- Year: 2026
- Authors: Benjamin Tannenbaum (Javo, AISO Boost Ltd., Israel)
- arXiv Category: cs.IR
- PDF Link: https://arxiv.org/pdf/2610.25461
- arXiv ID: 2610.25461v1
- Label: [applied]
- Citation count: [not found]