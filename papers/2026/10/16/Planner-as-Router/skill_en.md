# Skill: planner-as-router-model-routing
Source: 2609.32917v1
Type: framework

## When to use this skill
- Multi-agent workflow has multiple steps (subtasks) with varying complexity.
- Want to cut inference cost because currently using the frontier model for every step.
- Can estimate task complexity before choosing the model.

## When NOT to use
- Single-step workflow, no multi-tier model routing needed.
- Cannot estimate task complexity before running.

## Required input
- List of available model tiers (small/mid/frontier).
- A mechanism to classify task complexity (complexity classifier).
- Workflow segmented into independent subtasks.

## Steps
1. Segment the workflow into subtasks, each with a task type.
2. Use the complexity classifier to classify each subtask as SIMPLE or COMPLEX.
3. Route SIMPLE subtasks to the small model, COMPLEX subtasks to mid/frontier models.
4. Monitor the plan mix (small/mid/frontier ratio) to adjust the classifier.
5. Only use the frontier model for subtasks that truly need deep reasoning.

## Expected output
- Reduce inference cost by about 44% vs using the frontier model for every step.
- Lose only about 2.9 accuracy points.

## Example application
Solopreneur running a business report writing pipeline: step 1 data collection (small model), step 2 trend analysis (large model), step 3 report writing (mid model). Planner-as-Router automatically routes each step to the right model tier, cutting inference cost by about 44%.

## Gotchas
- Only loses 2.9 accuracy points vs all-frontier — acceptable for many use cases.
- Needs a good complexity classifier; if classification is wrong, quality drops.
- Absolute accuracies are low (22-29%) on difficult compositional tasks.
