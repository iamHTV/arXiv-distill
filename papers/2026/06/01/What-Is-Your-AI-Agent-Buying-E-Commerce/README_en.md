# [2508.02630] What Is Your AI Agent Buying? Evaluation, Biases, Model Dependence, & Emerging Implications for Agentic E-Commerce

## Problem
Online marketplaces will be transformed by autonomous AI agents acting on behalf of consumers. But agent behavior has not been studied carefully. Specifically: do agents exhibit biases? Are preferences stable? Can sellers exploit them?

## Contribution
1. **ACES framework**: Provider-agnostic framework for auditing agent decision-making. Tests across Claude, GPT, Gemini.
2. **Choice homogeneity**: Agents concentrate demand on few "modal" products — ignoring others. Winner-take-all risk.
3. **Position biases**: Strong position biases — vary across providers/models, persist in text-only interfaces. Undermine "top" rank notion.
4. **Seller-side exploitation**: Simple query-conditional description tweaks → significant market share gains.

## Method (core summary)
ACES framework: tests AI agents on real e-commerce products across 8 categories. Rationality tests: price sensitivity, rating sensitivity, review sensitivity. Randomized controlled trials: position biases, tag effects (sponsored, endorsed). Cross-model comparison: Claude Sonnet 4/Opus 4.5, GPT-4.1/5.1, Gemini 2.0/2.5/3.0. Seller-side agent experiments.

## Key Findings
- Choice homogeneity: agents concentrate demand on few products — more pronounced in latest models
- Model heterogeneity: different models prefer different products for same query — volatility
- Position biases: strong, vary across models, persist in text-only
- Sponsored tags: agents penalize sponsored listings
- Platform endorsements: agents reward endorsed listings
- Price/rating sensitivities: vary sharply across models
- Seller agent: simple description tweaks → significant market share gains
- Agentic markets: volatile, fundamentally different from human commerce

## Actionable Insights
1. **Winner-take-all risk**: If dominant agent achieves market share → artificially induces winner-take-all. Sellers: optimize for specific agent models. Example: if Claude is dominant → optimize product descriptions for Claude's preferences.

2. **Position bias exploitation**: Agents have strong position biases. Platforms: be aware that ranking affects agent choices, not just human choices. Example: e-commerce platform — sponsored listings penalized by agents, endorsed listings rewarded. Consider agent-aware ranking.

3. **Seller-side agent optimization**: Simple description tweaks → market share gains. Example: deploy seller-side agent that dynamically adjusts product descriptions based on querying agent's model — "If Claude asking, emphasize X. If GPT asking, emphasize Y."

## Assumptions & Limitations
**Conditions for experiment to work:**
- Real e-commerce products across 8 categories
- Provider-agnostic framework (ACES)
- Randomized controlled trials

**Limitations the paper acknowledges:**
- Model-specific results may change with updates
- Limited to 3 model families

**Limitations the paper does NOT mention:**
- Ethical implications of agent manipulation
- Regulatory framework needed but not proposed
- Long-term market effects unclear
- Consumer protection when agents make bad choices
- Platform design implications not fully explored

## Metadata
- Year: 2025
- Authors: Amine Allouah, Omar Besbes, Josué D Figueroa, Yash Kanoria, Akshit Kumar
- Category: cs.AI
- PDF: https://arxiv.org/pdf/2508.02630
- Citation count: [EXTRACTION FAILED]
