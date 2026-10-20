# Skill: conversation-trained-sales-agent

Source: 2610.25461v1
Type: framework / workflow

## When to use this skill
- When deploying an AI sales agent for an e-commerce or booking website and you have historical chat conversation transcripts.
- When you want to test whether fine-tuning a model on real commercial conversations improves conversion compared to a general-purpose frontier model.
- When deciding between deploying an AI agent and keeping human live-chat sales staff, based on cost and conversion.

## When NOT to use this skill
- When the task is general Q&A without a measurable business outcome (e.g., an agent answering product questions without asking for a purchase).
- When you do not have real sales conversation transcripts to train on (need at least 10,000+ labeled conversations).
- When you only need a quick marketing demo without rigorous A/B testing.

## Required inputs
- Corpus of real commercial conversation transcripts (at least 10,000 conversations, de-identified and labeled with outcomes: purchase/cancel/lead).
- List of target websites with machine-readable catalog or inventory feed.
- An open-weight base model (e.g., Qwen3-32B) and GPU resources (recommended 32 H100 or equivalent).
- Agent scaffold components: chat widget, catalog retrieval, tools (search catalog, get item, check availability, add to cart, get policy, capture lead, handoff to human), system prompt template, output guardrails.

## Steps to execute
1. Collect and filter corpus: remove conversations mentioning evaluation sites, collect with user consent, de-identify (automated PII redaction + hashed identifiers + manual QA), verify residual PII rate below 0.2%.
2. Split data: SFT examples (at least 1 million), preference pairs (at least 100,000 pairs, preferred turn leads to purchase/booking/lead progress, dispreferred turn leads to stall/exit), constraint examples (at least 30,000, teaching constraints on discounts, claims outside catalog, AI disclosure, human handoff).
3. Train model: SFT on base model (2 epochs), then preference optimization (DPO or equivalent), then train on constraint data. Estimated 2,240 GPU-hours on 32 H100 GPUs.
4. Build agent scaffold: same widget, greeting, disclosure line ("I'm an AI shopping assistant"), catalog retrieval refreshed every 24 hours, tools, per-site system prompt, guardrails (filter prices, discounts, policy statements), 8-second latency budget.
5. Deploy A/B test: randomize visitors into arms (no agent, Javo, frontier agent), each visitor assigned fixed to one arm, run at least 2–4 weeks, collect 14.8 million visitors as in the paper.
6. Measure outcomes: RPV (revenue per visitor), conversion, engaged conversion, CSAT, cost per engaged conversation, all guardrails (return rate, cancellation rate, complaints, unsupported claims, prohibited pressure tactics).
7. Compare and decide: if Javo is non-inferior to humans and outperforms frontier model on engaged conversion, deploy widely; otherwise keep frontier model or adjust training data.

## Expected output
- A fine-tuned AI sales agent trained on domain-specific commercial conversation corpus.
- A/B test report with engaged conversion, RPV, CSAT, cost per engaged conversation, and all guardrail metrics.
- Deployment decision: deploy widely, keep as-is, or stop the project.

## Example application
A beauty and personal care e-commerce website with 50,000 visitors/month wants to deploy an AI agent for consultation and sales. They collect 15,000 old live-chat transcripts, label outcomes (purchase/cancel), SFT Qwen3-32B on this corpus, then run A/B test against frontier agent GPT-5.2 with same widget and catalog on 10% of traffic for 3 weeks. Expected results: engaged conversion increases 15–25%, cost per conversation drops from $3.40 (human) to about $0.06 (AI).

## Gotchas
- Scaffold must be identical across arms: any difference in widget, prompt, tools, or guardrails will invalidate model comparison.
- AI disclosure may reduce purchases (per Luo et al., 2019); all reported effects are NET of honest disclosure.
- Do not rely on Study 1 alone — artificial buyers (simulators) can reorder leaderboards.
- Author has conflict of interest (Founder/CEO of AISO Boost Ltd.); no independent statistical review claimed.
- Results may not transfer to under-represented languages in the training corpus (weak cross-lingual consistency).
- No study of buyer-side agents (customers buying through AI agents).