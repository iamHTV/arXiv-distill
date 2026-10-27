# Skill: agentorch-global-orchestration-improvement
Source: 2610.33375v1
Type: optimization-method

## When to use this skill
- Need to reduce LLM calls in enterprise workflow systems while maintaining high accuracy.
- Want to compare global orchestration with step-by-step interaction on same workflows, tools, execution environment.
- Want to apply techniques that narrow the gap between global and step-by-step orchestration.

## When NOT to use this skill
- Workflows with too many control-flow branches depending on unpredictable runtime results.
- When LLM call cost is not a concern.

## Required inputs
- Enterprise SOPs (or your company's business workflows) with reference workflow for each SOP.
- Catalog of tool interfaces (e.g., 64 tools spanning Slack, Jira, Salesforce, Google Sheets, Google Drive, Snowflake, Workato).
- Simulatable execution environment for reproducible evaluation.
- Runtime variants for each SOP (different inputs, execution conditions).

## Steps to perform
1. Build benchmark from executable enterprise workflows: each SOP has reference workflow and multiple runtime variants.
2. Run Global orchestration: model generates complete workflow before execution, without observing concrete runtime inputs.
3. Run Step-by-Step interaction: action–observation loop, model calls LLM after each action to decide next step.
4. Apply Local (incremental workflow construction): build workflow via append-only editor; after each edit, validator accepts or rejects. No runtime input or execution results needed.
5. Apply Replan (execution-feedback revision): execute Global workflow on a few runtime variants, provide execution feedback to model, ask model to revise complete workflow.
6. Evaluate Orchestration Accuracy: average of Execution Trace Accuracy and Side-Effect Accuracy.
7. (Optional) Targeted training: train model on 3,000 source recipes pairing task specification with complete reference workflow. Take better of SFT and RL per base model.

## Expected output
- Orchestration Accuracy gap between Global and Step-by-Step.
- Number of LLM calls and completion tokens per protocol.
- Improved workflow via Local, Replan, or targeted training.

## Example application
Company has multi-step employee onboarding workflow (create Slack account, create Salesforce record, send welcome email, add to Google Sheet). Currently uses Step-by-Step, 23.2 LLM calls per onboarding. Apply Global orchestration: generate complete onboarding workflow before execution, execute without further LLM calls. If accuracy insufficient, apply Local (incremental construction with validator) and Replan (revision with execution feedback from 2 sample variants). Result: 23.2× fewer LLM calls, accuracy gap narrowed to ~8.5 pp.

## Gotchas
- Global orchestration still less accurate than Step-by-Step on all evaluated models (gap ~8.5 pp with newest model).
- Model scale doesn't consistently narrow gap — not simply using larger models.
- Reasoning doesn't provide consistent absolute benefit to Global nor consistent gap reduction.
- Need reference workflow for each SOP to evaluate — not applicable to completely new workflows never executed before.
- Need simulatable execution environment for reproducible evaluation.