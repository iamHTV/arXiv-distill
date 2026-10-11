# [2605.31545v1] PARL: Preference-Aware Rubric Learning for Personalized Evaluation

## Problem
LLMs evolve from general-purpose assistants to user-centric agents — personalization becomes central. But evaluation of personalized alignment is a critical bottleneck. Existing evaluation methods — automatic metrics, LLM-as-a-judge — fail to capture subjective, user-specific preferences embedded in long-term interaction histories.

## Contribution
1. **Personalized Evaluation as Learning paradigm**: Formulates personalized evaluation as learning problem, not static judgment. 3 principles: Representativeness, User-Consistency, Discriminativeness.
2. **PARL framework**: Preference-Aware Rubric Learning — learns evaluation rubrics from raw user histories. Self-validation mechanism for consistency. Discriminative RL objective contrasts user-authored vs model outputs.
3. **Results**: High-fidelity rubrics, reliable identification of user-aligned responses, generalizes across users/tasks.

## Method (core summary)
PARL: (1) Rubric Induction: learn multi-dimensional evaluation rubrics from raw user histories — not static prompts; (2) Self-Validation: ensure rubrics consistent with user preferences; (3) Discriminative RL: contrast user-authored responses vs model outputs — capture user-specific decision boundaries. Reference-free: no fixed references needed. Decouples evaluation from generation.

## Key Findings
- GT user-level accuracy: PARL achieves highest across 3 personalized text generation tasks
- Discriminative power: clear margin between authentic user responses and AI outputs
- Hand-crafted static prompts inadequate — GT accuracy can be lower than generic baselines
- PARL-0 (without Discriminative Margin Product): no discriminative capability — overly permissive rubrics
- PARL-A and PARL-B: robust discriminative power, high-fidelity rubrics
- Generalizes across users and tasks

## Actionable Insights
1. **Personalized evaluation needs learning, not static judgment**: Use user history to learn evaluation criteria. Don't rely on hand-crafted prompts. Example: when evaluating AI-generated content for specific user, learn from user's past preferences — what they liked, disliked, style preferences.

2. **Discriminative objective is key**: Contrast user-authored vs model outputs. Captures user-specific decision boundaries. Example: when training personalized AI assistant, use discriminative RL to distinguish user's authentic style from AI imitation.

3. **Reference-free evaluation**: No fixed references needed. Rubrics learned from user behavior. Example: when evaluating personalized email drafts, don't compare to template — learn what this specific user considers good email from their history.

## Assumptions & Limitations
**Conditions for method to work:**
- User behavioral history available
- Sufficient history quality and quantity
- Personalized text generation tasks

**Limitations the paper acknowledges:**
- Cold-start scenarios: sparse history → struggle to induce detailed rubrics
- Static preferences assumed — no temporal evolution modeling
- Focused on text generation — multimodal extensions open
- GT user-level accuracy hasn't reached 1.0 — inconsistent users still challenging

**Limitations the paper does NOT mention:**
- Privacy concerns with user history data
- Computational cost of rubric learning per user
- Scalability to millions of users
- Cross-domain transferability
- User preference drift over time

## Metadata
- Year: 2026
- Authors: Yilun Qiu, Xiaoyan Zhao, Yang Zhang, et al.
- Category: cs.CL
- PDF: https://arxiv.org/pdf/2605.31545v1
- Citation count: [EXTRACTION FAILED]
