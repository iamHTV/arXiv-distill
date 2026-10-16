# Skill: agentrouter-step-level-model-routing
Source: 2609.22951v1
Type: framework

## When to use this skill
- Agentic workflow has multiple steps with varying complexity (planning needs large model, formatting needs small model).
- Want to cut inference cost because currently every step goes to the frontier model.
- Have labeled agent trajectory data to train a lightweight classifier.

## When NOT to use
- Single-step workflow, no multi-tier model routing needed.
- No labeled trajectory data available to train the classifier.

## Required input
- List of available model tiers (from frontier to minimal, e.g. GPT-5, 70B, 7B, 3B).
- Five routing-time features extractable per step (as described in the paper).
- A lightweight classifier model (trainable from 50,000 labeled steps).

## Steps
1. Segment agentic workflow into trajectory steps, each with a task type (planning/coding/research/data analysis).
2. Extract the 5 routing-time features for each step.
3. Use the lightweight 12M-parameter classifier to map each step to a model tier (tier 1 frontier to tier 4 minimal).
4. Call frontier model only for steps classified as needing deep reasoning; use smaller models for the rest.
5. Enable fallback to a higher tier if quality is low (activates on <4% of trajectories).

## Expected output
- Reduce 72% inference cost vs using frontier model for every step, retain 97.3% quality (<3% degradation).
- Low routing latency (<5ms/step on A100).

## Example application
Solopreneur runs multi-channel article pipeline: step 1 ideation (small model), step 2 content writing (large model), step 3 HTML formatting (small model). AgentRouter automatically routes each step to the right model tier, cutting inference cost to ~30% of using the large model for every step.

## Gotchas
- Requires labeled trajectory data to train the classifier; without it, the skill cannot run.
- On unseen frameworks (e.g. AutoGen), accuracy drops 6–9%, though cost reduction still reaches 58%.
