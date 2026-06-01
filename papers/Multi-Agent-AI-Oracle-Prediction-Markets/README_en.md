# [2605.30802v1] Multi-Agent AI Oracle Systems for Prediction Market Resolution

## Problem
Prediction markets aggregate collective intelligence to forecast uncertain events, but their utility depends on reliable outcome resolution. Existing oracle systems trade off fast but brittle automation against accurate but costly human arbitration. Single-LLM oracles inherit all failure modes of their underlying model with no self-correction mechanism.

## Contribution
1. **Independent aggregation better than deliberative consensus**: Confidence-weighted voting achieves 83.43% accuracy, outperforms best single model (DeepSeek 82.42%) by 1.01 percentage points. Deliberative consensus DEGRADES to ~76% — below every single-model baseline.
2. **Error correlation limits ensemble gains**: Error correlations across models 0.529-0.689 → aggregation gains fall short of theoretical Condorcet ceiling (~90%). Shared training data creates correlated failures.
3. **Hybrid AI-human escalation framework**: Unanimous high-confidence questions → 97.87% accuracy on 47% of dataset. Inter-agent disagreement flags remainder for human review.

## Method (core summary)
Test on 1,189 resolved prediction market questions from KalshiBench. 3 LLM agents: GPT-5 Nano, DeepSeek-V3, Llama-3.3-70B. Common evidence layer via Exa, retrieval filtered by publication date. Architecture A: Independent Aggregation — each model resolves independently, majority vote or confidence-weighted vote. Architecture B: Deliberative Consensus — structured debate over 2 rounds, models view each other's reasoning before submitting. Escalation signals: inter-agent agreement (unanimous vs split) + average confidence → composite score.

## Key Findings
- Independent aggregation (confidence-weighted): 83.43% accuracy — best overall
- Best single model (DeepSeek): 82.42%
- Deliberative consensus: ~76% — BELOW every single-model baseline
- Unanimous (3-0 agreement): 88.34% accuracy (978 questions)
- Split (2-1 vote): 57.82% accuracy (211 questions) — barely above chance
- Unanimous + high confidence (≥0.91): 97.87% accuracy on 563 questions (47% of dataset)
- Error correlations: r=0.529-0.689 across model pairs
- Category tier: Sports, Financials >92%; Crypto, Companies <67%
- 14% of questions resist correction by any multi-agent architecture

## Actionable Insights
1. **Don't use deliberative debate for evidence-based tasks**: When shared evidence exists, deliberation HURTS accuracy because confidently wrong models flip correct ones. Only use deliberation when exploring diverse perspectives, not when ground truth exists. Example: financial oracle — use independent aggregation, not debate.

2. **Inter-agent disagreement is the strongest signal**: When 3 models independently disagree (2-1 vote), accuracy drops to 57.82% — barely above chance. Use disagreement as escalation trigger. Example: AI advisory system — when multiple models disagree, flag for human review instead of auto-resolving.

3. **Hybrid routing: auto-resolve high-confidence, escalate rest**: Unanimous + high confidence → 97.87% accuracy. Use composite score = unanimous + confidence to route. Example: customer support AI — auto-resolve when all models agree with confidence >0.9, escalate when disagreement exists.

## Assumptions & Limitations
**Conditions for method to work:**
- Need multiple diverse LLMs (not same architecture/training data)
- Common evidence layer must be available
- Questions must have binary/clear resolution criteria

**Limitations the paper acknowledges:**
- Error correlations 0.529-0.689 limit theoretical gains
- 14% of questions resist any multi-agent correction
- Deliberative consensus degrades performance — not always useful
- KalshiBench specific — generalizability unclear

**Limitations the paper does NOT mention:**
- Only tests 3 models — doesn't explore larger ensembles
- No cost-effectiveness tested — 3x API cost vs single model
- Evidence quality (Exa retrieval) may vary
- No dynamic markets addressed — questions evolve over time
- Binary resolution only — no continuous outcomes tested
- No comparison with fine-tuned single models

## Metadata
- Year: 2026
- Author: Tarun Kota
- Category: cs.MA, cs.AI
- PDF: https://arxiv.org/pdf/2605.30802v1
- Citation count: [EXTRACTION FAILED]
