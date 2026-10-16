# [2610.14709v1] Vela: User Behavior as Supervision Sparks LLM Intelligence

## Problem
Current LLM models are trained on static text or synthetic data, neither of which captures how user behavior evolves over time. Yet real-world applications (personal assistants, recommendation and advertising systems) demand the user dimension of LLM intelligence: the ability to infer a person's preferences, intent, and likely future actions from weeks to years of user behavior data.

## Contribution
- Propose user behavior as supervision: the training signal for LLMs comes from the user's real behavior on content platforms.
- Introduce Vela: a framework that operationalizes this paradigm by converting real user behavior data into trainable tasks and trajectories.
- From 100,000 anonymized behavior records of users, Vela generates 100,000 tasks across 91 real-world task templates.
- Difficulty-based filtering and trajectory acceptance criteria jointly retain appropriate tasks.

## Method (core summary)
Vela takes 100,000 anonymized behavior records of users, splits into visible histories and hidden futures. Each behavior record is organized into 6 categories: Views, Searches, Purchases, Posts, Follows, Dislikes. Vela generates tasks and trajectories from these records, applying difficulty-based filtering and trajectory acceptance criteria. Then fine-tune LLM on these tasks.

## Key Findings
- From 100,000 anonymized behavior records → 100,000 tasks across 91 real-world task templates.
- Vela-35B-A3B improves over base model by 11.5 points on VelaBench and up to 11.2 points on user-related OOD benchmarks.
- Average improvement on general OOD benchmarks: 4 points.
- Reinforcement learning after fine-tuning outperforms RL from base model by 7.7 points on both VelaBench and ProfileSummary.
- VelaBench: 982 held-out evaluation tasks from the same 91 task templates.
- User-related OOD benchmarks: PurchaseIntent, ProfileSummary, PersonaBench, AdRecommendation.
- General OOD benchmarks: AIME 2026, GPQA-Diamond, IFBench, CL-bench, CL-bench Life.

## Actionable Insights
- Use real user behavior as training signal (supervision) instead of only static text or synthetic data. Apply: solopreneur with user behavior data (views, searches, purchases) should convert into tasks to fine-tune LLM, helping LLM understand user preferences and intent better.
- Use difficulty-based filtering and trajectory acceptance criteria to filter high-quality tasks. Apply: when generating training data from user behavior, filter by difficulty and trajectory acceptance criteria to ensure quality.

## Assumptions & Limitations
- Requires real user behavior data (anonymized behavior records); doesn't apply without behavior data.
- Paper admits: evaluation on specific benchmarks (VelaBench, PurchaseIntent, etc.); may differ on other tasks.
- Limitation paper doesn't mention: not evaluated on many domains beyond recommendation and personal assistants, not tested on real training cost.

## Metadata
- Year: 2026
- Authors: AllSpark Team
- arXiv category: cs.AI
- PDF link: https://arxiv.org/pdf/2610.14709
- Code: https://github.com/AllSpark-Research/Vela
