# [2605.31275v1] Personalized to Persuade: The Effects of Contextualization and Warmth on Trust and Reliance in Conversational AI

## Problem
Prior work has identified personalization as a persuasive strategy in politics and marketing. However, the persuasive effect of contextualization in everyday tasks — where users often lack prior knowledge — remains unclear. The interaction between contextualization and conversational warmth has not been studied, and the role of trust in mediation has not been tested.

## Contribution
1. **Crossover interaction**: Contextualization alone REDUCES persuasive power. But combined with warmth → RESTORES persuasiveness. Neither lever increases persuasiveness on its own.
2. **AI literacy paradox**: Users with more AI knowledge report LOWER trust but are MORE persuaded and MORE reliant. Literate users miscalibrate their ability to evaluate AI advice.
3. **Reliance invariant**: Reliance on AI present across ALL conditions — not dependent on contextualization or warmth. Design choices have limited role in shaping behavior.

## Method (core summary)
2×2 between-subjects experiment (N=380): contextualization (contextualized vs non-contextualized) × warmth (warm vs neutral). Participants read expert opinion on budgetary decision, then interact with AI assistant arguing AGAINST experts. AI tone manipulated (warm/neutral), explanations tailored to user's background (contextualized) or generic. Measures: persuasion (shift in decision), reliance (accepting AI over experts), trust (self-report scales).

## Key Findings
- Contextualization alone: REDUCES persuasive power vs non-contextualized
- Contextualization + warmth: RESTORES persuasiveness (crossover interaction)
- Reliance: present across ALL conditions, invariant to design choices
- Trust strongly predicts both persuasion (β significant) and reliance (β significant)
- BUT: contextualization and warmth do NOT operate through trust (no mediation)
- AI literacy: negative predictor of trust (r < 0) but POSITIVE predictor of persuasion (β > 0) and reliance (β > 0)
- Effect: users prone to deferring to AI over human expert judgment regardless of conversational design

## Actionable Insights
1. **Contextualization alone insufficient to persuade**: When designing AI chatbot for marketing/sales, just tailoring responses to user background is NOT enough — may even HURT persuasive power. Example: chatbot saying "based on your profile, product X fits you" → less persuasive than generic recommendation.

2. **Combine contextualization + warmth**: If personalizing, MUST combine with warm tone. Example: "Hey [name], based on your background in [field], I think you'll love this because [reason] — it's been a game-changer for people like you!" — warm + contextualized > generic > contextualized alone.

3. **AI literacy paradox — design for both literate and illiterate users**: Users with more AI knowledge are actually MORE reliant despite lower trust. They know AI can be wrong but still follow. Example: when designing AI advisory system, don't assume literate users will critically evaluate — they may overrely despite knowing limitations.

## Assumptions & Limitations
**Conditions for experiment to work:**
- Fictional budgetary decision scenario — low prior knowledge context
- AI argues AGAINST expert recommendations — creates conflict
- Participants are university students (limited demographics)

**Limitations the paper acknowledges:**
- Single task domain (budgetary decisions) — generalizability unclear
- University student sample — limited demographics
- Between-subjects design — no within-subject comparison
- Self-report trust scales — potential demand effects

**Limitations the paper does NOT mention:**
- No real-world high-stakes decisions tested (healthcare, finance)
- No long-term effects measured — single interaction only
- AI assistant text-based only — no voice/visual tested
- No different LLMs compared — only 1 model
- No cultural differences tested — Western sample only
- Persuasion measure binary (shift/no shift) — doesn't capture magnitude

## Metadata
- Year: 2026
- Authors: Mert Yazan, Suzan Verberne, Frederik Bungaran Ishak Situmeang (University of Amsterdam)
- Category: cs.HC, cs.AI
- PDF: https://arxiv.org/pdf/2605.31275v1
- Citation count: [EXTRACTION FAILED]
