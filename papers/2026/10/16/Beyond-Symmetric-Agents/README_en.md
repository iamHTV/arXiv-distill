# [2609.35875v1] Beyond Symmetric Agents: Cognitive Diversity and Multi-Agent Debate in Small Language Models

## Problem
Multi-agent debate (MAD) reportedly improves reasoning and factuality over single-model inference, but prior work treats agents as symmetric peers, leaving open what drives the gains.

## Contribution
- Test the hypothesis that cognitive diversity among agents is the driver, in small open-weight models with benchmark headroom.
- Across 23 models from eleven vendor families.
- Pool spans solo accuracies from roughly 30% to 92%.

## Method (core summary)
Experiment with multi-agent debate with 23 models from 11 vendor families, small open-weight models. Compare debate ensemble vs solo generation, homogeneous teams vs mixed teams, persona teams. Measure claim precision, accuracy, wall-clock, token cost.

## Key Findings
- Solo accuracies from roughly 30% to 92%.
- Team accuracy monotone in tier composition: 93.7% (SSS all-strong) → 87.0% (MMM) → 75.6% (WWW all-weak).
- Debate loses by 1.04pp vs solo generation, winning only 83 of 320 team-task cells.
- Mixed teams overturn 63.7% of wrong round-one majorities vs 42.9% for homogeneous.
- Independent biographies pooled through same panel reach 64.6% against debate's 55.6% (+8.9pp).
- Helpful flips outnumber harmful ones roughly two to one (7.6% vs 4.0% of agent-problem pairs).
- Debate at n=3 edges solo generation (55.6% vs 54.6% claim precision), persona teams reduce to 51.8%.
- Debate benefit comes from the first exchange (84.6% at one round, 87.2 at two, flat through five).
- 3.4× wall-clock and token cost.

## Actionable Insights
- Don't treat all agents as same-tier: cognitive diversity between agents creates benefit, not number of agents. Apply: solopreneur building MAS should combine agents with different personalities/methods, not copy the same agent multiple times.
- Debate only has benefit in the first exchange, then flatlines. Apply: when using debate, limit to 1-2 rounds of exchange, don't need long debates.
- Independent teams (independent biographies pooled) better than debate (+8.9pp). Apply: instead of having agents debate, let agents work independently then pool results (voting/pooling).

## Assumptions & Limitations
- Requires small open-weight models with benchmark headroom; may differ on frontier large models.
- Paper admits: debate loses by 1.04pp vs solo generation — debate is not always better.
- Limitation paper doesn't mention: not evaluated on many tasks beyond GSM8K, MMLU, biography; not tested on real token cost of 3.4×.

## Metadata
- Year: 2026
- Authors: Leonardo Ferreira, Gardenia Liu, Kaden Zheng (Boston Children's Hospital, Harvard Medical School, Harvard SEAS, Harvard College)
- arXiv category: cs.AI
- PDF link: https://arxiv.org/pdf/2609.35875
