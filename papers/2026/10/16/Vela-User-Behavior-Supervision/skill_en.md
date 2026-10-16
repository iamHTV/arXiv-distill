# Skill: vela-user-behavior-as-supervision
Source: 2610.14709v1
Type: framework

## When to use this skill
- Training LLM to understand user preferences and intent from real behavior data.
- Have real user behavior data (view history, searches, purchases, follows, dislikes).
- Want to improve personalization and user-facing capabilities of LLM.

## When NOT to use
- No real user behavior data available.
- Only need LLM to answer from general knowledge, no need to understand specific user behavior.

## Required input
- Anonymized user behavior records: Views, Searches, Purchases, Posts, Follows, Dislikes.
- An LLM fine-tuning system that can run on generated tasks.
- Task filtering criteria (difficulty-based filtering, trajectory acceptance criteria).

## Steps
1. Collect anonymized user behavior records (view history, searches, purchases, etc.).
2. Split each record into visible histories and hidden futures.
3. Convert each record into trainable tasks and trajectories via 91 real-world task templates (or define your own templates).
4. Apply difficulty-based filtering and trajectory acceptance criteria to filter high-quality tasks.
5. Fine-tune LLM on filtered tasks; then use RL (reinforcement learning) to improve further.

## Expected output
- Improve performance on user-related tasks: +11.5 points on VelaBench, up to +11.2 points on user-related OOD benchmarks.
- RL after fine-tuning outperforms RL from base model by 7.7 points.

## Example application
Solopreneur with an online video streaming platform: collect user watch history, search, and ratings. Convert into tasks to fine-tune LLM so LLM understands each user's movie preferences and recommends movies more accurately. Use difficulty-based filtering to only take tasks with clear behavior labels.

## Gotchas
- Need enough user behavior data (100,000 records in the paper) to be effective.
- Need to design task templates suitable for your domain (91 templates in the paper are for general content).
- RL after fine-tuning helps improve further but needs more compute resources.
