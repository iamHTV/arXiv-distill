# arXiv Distill Daily Report — 2026-10-21

Summary of 10 papers distilled today (top 10 selected from arXiv scan, highest LLM score first).
Each paper went through the full 6-step distillation (read paper → classify → README → skill → skill test → report), committed and pushed to GitHub.
This report is written in plain, friendly English for a solo founder / solopreneur.

## Overview
- Total papers distilled: **10**
- All are applied ([applied]) — real experiment, real dataset, concrete benchmark.

## 10 Papers Today
1. Selling in the Wild — Sales agent fine-tuned on real commercial conversations (arXiv 2610.25461v1)
2. CHSM8 — Chess transformer following natural-language prompts (arXiv 2610.25356v1)
3. MAPS — Multi-agent personalized script-driven video advertising (arXiv 2610.25748v1)
4. Fake News, Real Crashes — Information-injection attacks on LLM financial trading agents (arXiv 2610.26438v1)
5. NIOCIS — Typed-decision next-hop routing for tool-using agents, lower inference cost (arXiv 2610.25985v1)
6. One-Pixel of Reasoning — One implicit warrant is enough to mislead LLM agents (arXiv 2610.24873v1)
7. CXBENCH — Benchmark for process-compliant LLM agents in regulated CX workflows (arXiv 2610.25954v1)
8. ScaleMAS — Scaling multi-agent intelligence with substrate-centric coordination (arXiv 2610.16120v1)
9. Ask Less, Ask Better — Allocating user attention in proactive LLM agents with interruption budgets (arXiv 2610.24411v1)
10. Explore or Confirm (Wellocate) — LLM agents misallocate measurements under noise (arXiv 2610.25111v1)

## WHAT YOU CAN APPLY TO YOUR BUSINESS
Top 5 insights, each one short sentence + one concrete example you can try today as a Vietnam solopreneur:

1. **Train an AI sales agent on your real conversations** (live chat, Zalo, Messenger) — raises revenue per visitor +10% and engaged conversion +21.6% at only 1.8% of a human salesperson's cost. → Apply today: start collecting and de-identifying 10,000+ old chat conversations from your website or fanpage, label outcomes (buy / cancel / lead), ready to fine-tune an open model (e.g. Qwen3) into a customer-care agent.

2. **Limit your support agent to 1–3 clarifying questions per session** and remember the customer's previous answers, so it never asks twice and doesn't annoy customers. → Apply today: if you use a customer-support agent, set an "interruption budget" of 1–3 questions per session and store the customer's prior answers in memory; don't re-ask what you already know.

3. **Use two independent agents to cross-check before executing important transactions** (payment, contract, money transfer) — blocks fake-info or tampered-content attacks from driving the agent astray (injection attack success 62%, cross-check system reduces to 9–10%). → Apply today: set up one analyst agent and one checker agent that must both agree before the agent executes a high-risk business action.

4. **For tool-calling agents** (order lookup, inventory check, payment), use a cheap rule for common requests and only call the large language model (LLM — costs money per call) when the request is complex or uncertain. → Apply today: cuts your monthly LLM API cost significantly.

5. **Generate ad video / ad content on demand** with multiple cooperating agents (write script → review) instead of a fixed creative inventory, for higher personalization per customer. → Apply today: use one agent to write a video ad script from the customer profile, then another agent to review it before publishing.

## Paper-by-paper details

### [1] Selling in the Wild: Sales agent fine-tuned on real commercial conversations (arXiv 2610.25461v1)
- **What it does:** Builds an AI sales agent fine-tuned on 4.6 million real commercial conversations, tested on 100 real e-commerce sites with real customers, compared against no agent, a frontier (top-tier) AI model, and human live-chat agents.
- **What you learn:** Real conversation data matters more than model size for sales tasks. The sales agent raises revenue per visitor +10% vs no agent and engaged conversion +21.6% vs the frontier model with the same scaffolding (UI, retrieval tools, prompt), at only 1.8% of a human salesperson's cost.
- **Apply to you:** Collect 10,000+ old chatlive/Zalo/Messenger conversations, label outcomes (buy/cancel/lead), then fine-tune an open model (e.g. Qwen3) into a sales or customer-care agent at near-zero cost vs hiring staff.

### [2] CHSM8: Chess transformer following natural-language prompts (arXiv 2610.25356v1)
- **What it does:** A chess transformer controlled by natural-language prompts, using DPO (direct preference optimization) to follow a playing style without a reward model.
- **What you learn:** You can steer agent behavior with plain text using DPO on paired data (same output, different conditions) — no reward model needed.
- **Apply to you:** If you use an agent to write content, prepare paired examples (same article, prompt matching vs not matching your brand style) and use DPO to make the agent write in your style, without a complex reward model.

### [3] MAPS: Multi-agent personalized script-driven video advertising (arXiv 2610.25748v1)
- **What it does:** On-demand personalized video ad system with 4 agents (Profile, Scripter, Director, Reflector), using GRPO (multi-objective reward optimization). Real A/B test at Kuaishou: CTR +2.87%, CVR +2.74%, ARPU +9.85%.
- **What you learn:** On-demand generated ads are worth more than matching ads from a fixed inventory; agents help each other via online feedback (Reflector) to improve continuously.
- **Apply to you:** Use one agent to write a video ad script from the customer profile (Profile Agent), then another agent to review it (Reflector Agent) before publishing — personalized ads without a large creative team.

### [4] Fake News, Real Crashes: Information-injection attacks on LLM financial trading agents (arXiv 2610.26438v1)
- **What it does:** An information-injection attack tricks LLM financial trading agents; attack success rate (ASR) reaches 62% (4.5x prompt injection at 14%). A hierarchical star-pipeline coordination reduces ASR to 9–10%.
- **What you learn:** The data the agent acts on (data-plane) is a bigger attack surface than system instructions (control-plane); you need multiple independent agents cross-checking before high-risk trades.
- **Apply to you:** If you use an agent for payments/transactions, set up two independent agents (one analyzes, one checks the request) that must both agree before executing — to stop fake info from tricking the agent into sending money to the wrong place.

### [5] NIOCIS: Typed-decision next-hop routing for tool-using agents, lower inference cost (arXiv 2610.25985v1)
- **What it does:** A typed-decision routing layer lets tool-using agents call tools with low inference cost: only call the LLM when uncertain, using a cheap "readout" to pick the next step in a bounded option space.
- **What you learn:** For repeated decisions, a cheap readout can replace most LLM calls, keeping the LLM only for uncertain cases.
- **Apply to you:** If you build an agent that calls many tools (order lookup, inventory check), use a cheap rule for common requests and only call the LLM (costs money) for complex or uncertain requests — cutting your LLM API bill.

### [6] One-Pixel of Reasoning: One implicit warrant is enough to mislead LLM agents (arXiv 2610.24873v1)
- **What it does:** An attack changing one implicit reasoning link (one pixel of reasoning) is enough to mislead an agent even when input evidence is correct. Multi-agent debate does not automatically fix it.
- **What you learn:** The implicit reasoning link between evidence and conclusion is an independent attack surface; check whether a small input tweak can flip the agent's conclusion.
- **Apply to you:** If you use an agent to summarize reports or make recommendations from many sources, regularly check whether a small change in input information can change the agent's mind — especially in healthcare, law, security.

### [7] CXBENCH: Benchmark for process-compliant LLM agents in regulated CX workflows (arXiv 2610.25954v1)
- **What it does:** A benchmark for agents working in regulated processes (finance, healthcare, insurance) with a hybrid grader (deterministic + LLM-as-a-Judge) and a false-pass metric (correct outcome but violated process).
- **What you learn:** Correct outcome does not mean correct process; an agent can reach a business goal while violating the process, so evaluate both process and outcome.
- **Apply to you:** If you use an agent in a regulated field (finance, insurance, healthcare), check not only the final result but also whether the agent followed the process (step order, authority) — don't just look at whether the outcome is right.

### [8] ScaleMAS: Scaling multi-agent intelligence with substrate-centric coordination (arXiv 2610.16120v1)
- **What it does:** Multi-agent coordination through a shared message store (substrate-centric): agents interact only via publish/search/visit, each read limited to k messages; messages persist after the author leaves.
- **What you learn:** Multi-agent coordination should be designed around shared data (shared datastore, bounded reads, persistent messages) rather than tightly coupled to each agent's logic — making the system scalable and resilient to agent failure.
- **Apply to you:** If you run many agents at once, let them communicate through a shared inbox with long-lived messages, so new agents can join and departing agents don't break the system.

### [9] Ask Less, Ask Better: Allocating user attention in proactive LLM agents with interruption budgets (arXiv 2610.24411v1)
- **What it does:** Limits the agent's clarifying questions (interruption budget) to 1–3 per session and measures both frequency and quality of questions, not just count.
- **What you learn:** Question count is not a good measure of user burden; measure frequency and quality, and agents should avoid re-asking questions already answered via persistent memory.
- **Apply to you:** If you use a customer-support agent that asks customers many questions, limit it to 1–3 clarifying questions per session and remember the customer's prior answers so it doesn't ask again — avoiding annoying customers.

### [10] Explore or Confirm (Wellocate): LLM agents misallocate measurements under noise (arXiv 2610.25111v1)
- **What it does:** A benchmark (Wellocate) measuring how agents allocate an experiment budget between exploration (explore) and confirmation (confirm) under noise; agents over-confirm (re-test the top candidate) and miss better candidates.
- **What you learn:** No fixed rule is best everywhere; measurement budget allocation must read the noise level and landscape; agents need an external candidate list to avoid exhausting the search space.
- **Apply to you:** If you run ad experiments or A/B tests, don't only re-test the best candidate — also explore new ones, and set up a final re-check round of the top candidate at campaign end to avoid picking the wrong one due to a lucky read.

---

*This report was rewritten per the pitfall-27 fallback after detecting that the first daily_summary.py output was contaminated with LLM internal reasoning (reasoning leakage, duplicate headers, wrong paper count). Data taken from the 10 papers distilled today.*
