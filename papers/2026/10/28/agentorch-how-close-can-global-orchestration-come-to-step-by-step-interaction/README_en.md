# 2610.33375v1 AgentOrch: How Close Can Global Orchestration Come to Step-by-Step Interaction?

## Core Value (1 sentence)
Global orchestration generates a complete executable workflow before execution (no LLM calls during runtime) and has narrowed the accuracy gap to Step-by-Step interaction to ~8.5 pp with the newest model, while reducing LLM calls by 23.2× and completion tokens by 3.64× — techniques like incremental workflow construction, execution-feedback revision, and targeted training further narrow this gap.

## Problem
Enterprise workflow agents typically rely on step-by-step interaction (Step-by-Step): the agent executes an action, observes its result, and invokes an LLM again to decide the next step. Global orchestration (Global) instead generates a complete executable workflow in advance and executes it without further LLM calls, substantially reducing inference overhead, but it remains less accurate than Step-by-Step. It was unclear how close Global can come to Step-by-Step and what narrows the remaining gap. Prior work typically evaluated workflow generation in isolation rather than directly comparing against step-by-step interaction on the same workflows, tools, execution environment, and criteria.

## Contribution
1. AgentOrch benchmark: direct comparison of Global and Step-by-Step on 650 enterprise SOPs and 3,220 runtime variants under matched tools, environments, and evaluation criteria.
2. Test-time orchestration improvement: incremental workflow construction and execution-feedback revision as routes to stronger Global orchestration. Construction improves models without runtime execution feedback; revision improves all eight evaluated models, including on held-out variants.
3. Training for Global Orchestration: training models on 3,000 separate source recipes to generate complete workflows. Taking the better of SFT and RL for each base model, Orchestration Accuracy improves by an average of 12.18 pp across all five trained models.
4. The Global–Step-by-Step gap has shrunk by about 79% from early models (40.67 pp for GPT-3.5 Turbo) to the strongest recent model (8.53 pp for Claude Opus 5 Thinking).
5. Global uses 23.2× fewer LLM calls and 3.64× fewer completion tokens than Step-by-Step, on average.

## Method
The AgentOrch pipeline has these main steps:
1. Build benchmark from executable enterprise workflows: each SOP has a reference workflow and multiple runtime variants.
2. Task specification: fixed task description, public input/output schemas, execution context, workspace resources, communication templates, and 64 tool interfaces. Requirements in non-causal order.
3. Execution environment and runtime variants: 64 tool interfaces across Slack, Jira, Salesforce, Google Sheets, Google Drive, Snowflake, Workato. Real and simulated backends behind same interfaces.
4. Two orchestration protocols:
   - Global: model generates complete workflow before execution and before observing concrete runtime inputs; workflow fixed and reused across all variants without further LLM interaction.
   - Step-by-Step: action–observation loop (ReAct-style); each variant is an independent episode; model produces one tool call, observes result, selects next action until termination.
   - Local: incremental workflow construction via append-only editor with validator feedback; no runtime input or execution results observed.
   - Replan: execute Global workflow on runtime variants, provide execution feedback to model, model generates revised complete workflow.
5. Evaluation metrics: Orchestration Accuracy (average of Execution Trace Accuracy and Side-Effect Accuracy), Final Accuracy, Error Rate.

## KNOWLEDGE — Data & Concepts
- Global orchestration: LLM constructs complete executable workflow before observing concrete runtime inputs; workflow executes without further LLM calls.
- Step-by-Step interaction: model selects an action, observes execution result, then decides next action.
- Runtime variant: instantiates concrete inputs and execution conditions, exercising different control-flow paths, loop cardinalities, and error conditions.
- Orchestration Accuracy: average of Execution Trace Accuracy and Side-Effect Accuracy per runtime variant.
- Execution Trace Accuracy: agreement with reference trace, averaged over 5 binary components: tool selection, tool order, tool execution, required arguments, control path.
- Side-Effect Accuracy: whether execution produces required state changes without missing, duplicated, or unintended effects.
- Local: incremental workflow construction with validator feedback, no runtime input or execution results.
- Replan: revise complete workflow using execution feedback, execute without further LLM calls at runtime.
- 650 enterprise SOPs, 3,220 runtime variants, 64 tool interfaces.
- 3,000 training source recipes, disjoint from AgentOrch benchmark.
- 1,033 tool operations spanning 305 namespaces in training set.
- Gap shrunk 79% from 40.67 pp (GPT-3.5 Turbo) to 8.53 pp (Claude Opus 5 Thinking).
- Local (incremental construction): +9.98 pp average Orchestration Accuracy without runtime feedback.
- Replan (execution-feedback revision): +6.18 pp average across 8 models, +6.13 pp on held-out variants.
- Targeted training: +12.18 pp average (6.84–19.88 pp) across 5 trained models.
- Error Rate reduction: 13.02–40.99 pp after training.
- 92.6% of aggregate Replan gain comes from fixing initially invalid workflows.

## INSIGHT — Mechanism & Why
- [Model scale doesn't consistently narrow gap] occurs because Global Orchestration Accuracy and gap don't change monotonically with scale (e.g., Qwen2.5 Global Accuracy drops from 16.18% at 32B to 9.91% at 72B). Simply using larger models is not sufficient — need to change how workflows are constructed.
- [Runtime input access alone doesn't explain gap] occurs because Input-Conditioned Global (receives runtime input but generates workflow before execution) changes average gap from 30.92 pp to 31.09 pp — essentially unchanged. Intermediate execution results are the key factor, not just runtime input.
- [Most Replan gains from fixing invalid workflows] occurs because 92.6% of aggregate Replan gain comes from turning initially invalid workflows into valid ones. Global must specify tool arguments and references before execution, while Step-by-Step can use observed results for subsequent calls. Getting specifications right before execution is the key lever.

## IDEA — Actionable Applications
1. Apply Local (incremental workflow construction) to enterprise workflow systems: instead of generating entire workflow at once, build it incrementally via append-only editor with validator checking after each edit. First step: implement workflow editor with validator checking schema, type, and reference constraints for tool arguments before execution.
2. Apply Replan (execution-feedback revision): execute Global workflow on a few runtime variants, collect execution feedback (tool calls, arguments, results, errors), and ask model to revise complete workflow. First step: pick 2 representative variants per SOP, execute Global workflow, provide feedback to model, generate revised workflow.
3. Apply targeted training: train models on 3,000 source recipes pairing task specification with complete reference workflow. Take better of SFT and RL per base model. First step: collect 3,000 source recipes from successfully executed enterprise workflows, create training pairs (task specification → reference workflow).

## WISDOM — General Principle
- Principle: Global orchestration requires not only selecting the right tools but also specifying before execution how each tool is called and how data flows between calls — getting these specifications right is the key lever for enterprise orchestrator work.
- When to use: When deploying enterprise workflow agents wanting to reduce LLM calls while maintaining high accuracy.
- When NOT to use: When workflows have too many control-flow branches depending on unpredictable runtime results (dynamic decisions based on unpredictable external feedback).

## Assumptions & Limitations
- Required condition: Need reference workflow for each SOP and a simulatable execution environment for reproducible evaluation.
- Paper-acknowledged limitations: Gap not fully closed — Step-by-Step still retains accuracy advantage on all evaluated models. Model scale doesn't consistently narrow gap. Reasoning doesn't provide consistent absolute benefit to Global nor consistent gap reduction.
- Limitations the paper does NOT state: Does not evaluate training cost vs. cost savings from reduced LLM calls during execution.

## Metadata
- Year: 2026
- Authors: Zijie Liu, Yueh Che Lee, Qi Yang Huang, Zayne Turner, Adam Seligman, Tianlong Chen, Zhaozhuo Xu, Jinhao Duan, Thomas A. Joseph
- arXiv category: cs.AI
- PDF link: https://arxiv.org/pdf/2610.33375v1
- Classification: [applied]