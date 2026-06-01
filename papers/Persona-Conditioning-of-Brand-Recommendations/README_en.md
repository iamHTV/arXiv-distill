# [2605.30207v1] Persona Conditioning of Brand Recommendations: A Prominence-Stratified Cross-Provider Audit

## Problem
The same prompt "best CRM software" reaches AI assistants from buyers in widely different contexts: solo founder, enterprise VP, UK SMB owner. Prior work has not audited how strongly contextual variation reshapes which brands the model recommends. Current measurement protocols aggregate across personas, systematically obscuring that variation.

## Contribution
1. **Prominence-stratified audit**: 2,000 runs across 10 personas × 8 prompts × 3 model configurations (OpenAI, Anthropic). Result: persona drops recommendation-set similarity (Jaccard) by Δ = -0.12 to -0.20
2. **Category leaders persona-resistant**: L1 brands have ~80% same-brand consistency across personas. L3 mid-market brands swap up to 75% of recommendation set as persona changes
3. **Cross-provider asymmetry**: Anthropic model shows larger effect — 43-52% recommendations without retrieval-layer evidence vs OpenAI 8-29%

## Method (core summary)
Audit design: 10 hand-curated personas × 8 commercial prompts × 3 model cells (OpenAI high/low, Anthropic sonnet low) × N=10 reruns. Brand extraction by 2 LLM judges (claude-haiku, gpt-5-mini) with intersection classification (count only when both judges agree). Consensus recommendation set = union of consensus-recommended brands across 10 reruns. Metric: Jaccard similarity between recommendation sets of same persona vs cross-persona.

## Key Findings
- Cross-persona Jaccard: 0.22-0.35 vs within-persona reference: 0.42-0.51
- Persona-shift effect size: Δ = -0.12 to -0.20 (clustered 95% CIs exclude zero on all 3 cells)
- L1 category leaders: 0.20-0.29 swap rate (persona-resistant)
- L3 mid-market brands: up to 0.75 swap rate (persona-sensitive)
- Anthropic sonnet/low: larger effect magnitude than OpenAI cells
- Rerun-stability baseline: 0.50-0.61 (persona effect sits outside noise floor)
- |Δ| comparable to within-provider-minus-cross-provider Jaccard gap (~0.20)

## Actionable Insights
1. **Measure AI brand perception conditioned on persona**: When auditing brand visibility on AI chatbots, do NOT use a single generic prompt. Test with multiple buyer personas. Example: CRM company wanting to know if brand appears in AI recommendations → test with 5-10 personas (startup founder, enterprise buyer, budget-conscious, feature-focused) and compare results.

2. **Mid-market brands need segment-targeted content**: Category leaders are safe (persona-resistant), but mid-market brands need content strategy per segment. Example: instead of 1 page "Best Project Management Tool", create "Best PM Tool for Startups", "Best PM Tool for Enterprise", "Best PM Tool for Remote Teams" — each page targeting 1 persona segment.

3. **AI retrieval vs priors affects persona sensitivity**: Models using more training priors (less retrieval) → larger persona effect. Models using retrieval → smaller persona effect. Example: when optimizing brand content for AI visibility, focus on retrievable content (structured data, clear claims) rather than relying on brand recognition alone.

## Assumptions & Limitations
**Conditions for audit to work:**
- 10 hand-curated personas, English-only, US/UK/EU geographic skew
- Single-day measurement — temporal drift not measured
- Persona-prefix syntax held constant

**Limitations the paper acknowledges:**
- L4 undersampled on every cell; sonnet/high and opus cells not included
- 10 personas limited — future audits should sample more broadly
- No pure-priors share co-measurement — hypothesis supported by cross-paper co-occurrence, not within-run
- Single-day measurement — temporal drift out of scope

**Limitations the paper does NOT mention:**
- Only audits 3 model configurations — no Google, Meta, open-source models
- 8 commercial prompts limited — does not cover all product categories
- Jaccard metric simplistic — doesn't capture ranking order or recommendation quality
- No non-English personas tested — global brands may differ
- Hand-curated personas may not represent real buyer diversity

## Metadata
- Year: 2026
- Authors: Will Jack, Noah Lehman, Keller Maloney, Sarah Xu
- Category: cs.AI
- PDF: https://arxiv.org/pdf/2605.30207v1
- Citation count: [EXTRACTION FAILED]
