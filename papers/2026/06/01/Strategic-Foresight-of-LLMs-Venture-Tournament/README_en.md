# [2602.01684] The Strategic Foresight of LLMs: Evidence from a Fully Prospective Venture Tournament

## Problem
Prior work fails to answer whether AI can outperform humans at strategic foresight — the capacity to form accurate judgments about uncertain, high-stakes business outcomes before they unfold. The main issue: most real-world outcomes are already known, making it hard to distinguish genuine prediction from pattern retrieval. Prior work uses retrospective or synthetic data — not tested on genuinely unknowable outcomes.

## Contribution
1. **Fully prospective prediction tournament**: Tests on 30 Kickstarter projects launched AFTER training cutoffs of all models — outcomes unknown when predictions were made
2. **Benchmark humans vs LLMs**: 346 experienced managers (Prolific) + 3 MBA-trained investors vs frontier LLMs (GPT-5, Claude 4.5, Gemini 2.5, Grok 4, etc.) on identical task
3. **Prospective benchmarking methodology**: Design template for strategy research — resolves training-data leakage problem

## Method (core summary)
30 U.S.-based technology ventures on Kickstarter, fundraising in progress. LLMs completed 870 pairwise comparisons — double round-robin tournament (every project vs every other, both orders). Humans did identical task. Compare predicted ranking vs realized outcome ranking using Spearman's rank correlation.

## Key Findings
- Gemini 2.5 Pro: ρ=0.74 (highest correlation) — correctly ordered ~79% venture pairs
- GPT-5 family: ρ=0.67-0.71
- Best human (Expert 3 — MBA investor): ρ=0.45 — correctly ordered ~60% pairs
- Prolific crowd: ρ=0.19 (near random)
- Expert 1: ρ=0.04 (random)
- LLMs captured >83% top-5 value; best human captured 50%
- Human-AI aggregation did NOT improve over best standalone model — "augmentation trap"
- Difference Gemini 2.5 Pro vs Expert 3: 0.29 points (p=0.063)
- Difference Gemini 2.5 Pro vs Prolific crowd: 0.55 points (p=0.001)

## Actionable Insights
1. **LLM as first-pass filter for deal flow**: When screening venture investments, acquisitions, or R&D projects, use LLM to rank opportunities before human review. Example: VC firm receives 1000 pitches/month → LLM filters top 50 → human only reviews those 50. LLM correctly ordered 79% pairs vs human 60%.

2. **Augmentation trap — be careful adding human to AI pipeline**: When AI already outperforms human on well-defined evaluation tasks, adding human judgment can DECREASE performance by reintroducing noise. Example: if AI screening accuracy = 79%, human = 60%, then AI+human may be < 79%. Human value lies in shaping AI inputs (questions, data), not filtering AI outputs.

3. **Consistency matters — LLMs stable, humans volatile**: Expert correlations ranged 0.04-0.45 under identical conditions — cannot identify reliable expert. LLMs produce stable rankings. Example: when hiring strategist, don't rely on single human expert — use LLM as baseline, human as challenger.

## Assumptions & Limitations
**Conditions for results to apply:**
- Task must be early-stage screening with standardized information
- Outcomes determined by external market response, not evaluator's implementation
- Structurally similar: venture scouts, corporate development, innovation committees

**Limitations the paper acknowledges:**
- Kickstarter fundraising is incomplete proxy for venture performance
- LLMs evaluated on standardized summaries, not full noisy information
- Sample 30 projects — sufficient for large differences but limited power among similar models
- Needs replication across diverse contexts

**Limitations the paper does NOT mention:**
- Not tested on non-U.S. markets — cultural bias?
- Does not address LLM training data contamination — despite post-cutoff, models may have prior Kickstarter pattern knowledge
- Does not discuss cost — running 870 comparisons with frontier models costs how much?
- Does not test sequential decision making — only one-shot ranking
- Does not address ethical implications of AI replacing human strategic judgment

## Metadata
- Year: 2026
- Authors: Felipe A. Csaszar (University of Michigan), Aticus Peterson (NYU Stern), Daniel Wilde (Indiana University)
- Category: cs.AI, econ.GN
- PDF: https://arxiv.org/pdf/2602.01684
- Citation count: [EXTRACTION FAILED]
