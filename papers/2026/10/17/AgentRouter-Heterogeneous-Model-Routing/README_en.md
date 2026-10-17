# [2609.22951v1] AgentRouter: Heterogeneous Model Routing for Cost-Optimal Multi-Step Agentic Workflows

## Problem
- Enterprise agentic systems route every trajectory step to a frontier model, wasting 60–80% of inference budget on subtasks that smaller models handle equally well. Existing routing solutions optimize single-turn query assignment but ignore a property unique to agentic workflows: subtask complexity varies widely within a single trajectory. A planning step may require frontier-class reasoning while a subsequent formatting step needs only a 7B model.

## Contribution
- AgentRouter — a lightweight classifier (12M parameters, <5ms overhead per step on an A100 GPU) that maps each trajectory step to one of four model tiers using five features extractable at routing time.
- Trained on 50,000 annotated agent trajectory steps spanning planning, coding, research, and data analysis tasks.
- AgentRouter achieves 72% cost reduction relative to frontier-only baselines, retaining 97.3% of frontier-only quality (less than 3% degradation in end-to-end task completion); per-step routing accuracy reaches 91% on minimal-complexity steps and 85% on efficient-tier steps, with 76–82% on the harder mid-range and frontier tiers.
- RouteLLM and FrugalGPT (applied per-step) achieve only 31% and 44% cost reduction respectively, because their single-turn training signal misses trajectory-level quality dependencies.

## Method (core summary)
- Step-level model routing formulated as a sequential assignment problem over agent trajectories.
- Each step st in agent trajectory τ = (s1, s2, ..., sT) represents a single LLM call with defined input context, instruction, and expected output.
- Each step is routed to one of four model tiers using a feedforward classifier with two hidden layers (256 and 128 units), ReLU activations, and a 4-class softmax output corresponding to the four model tiers.
- Input features are embedded; categorical features are embedded...
- Routing features are extracted at routing time, including accumulated context size and other features.
- Step-level routing rather than per-query routing, recognizing that routing decisions at step t affect context quality at step t+1.

## Key Findings
- 2 authors from Boston University and University of Texas at Austin, arXiv category: cs.AI/cs.LG.
- Across benchmarks, AgentRouter achieves 72% cost reduction vs frontier-only baselines, retaining 97.3% of frontier-only quality.
- Per-step routing accuracy reaches 91% on minimal-complexity steps and 85% on efficient-tier steps, with 76–82% on harder mid-range and frontier tiers.
- RouteLLM and FrugalGPT achieve only 31% and 44% cost reduction respectively, because their single-turn training signal misses trajectory-level quality dependencies.
- Step-level routing instead of using frontier model for every step: use frontier model for steps requiring deep reasoning, use small model for formatting steps.

## Actionable Insights
1. Step-level model routing instead of using frontier model for every step: use frontier model for steps requiring deep reasoning, use small model for formatting steps. Application: only use frontier model for steps requiring deep reasoning, use small model for formatting steps, reducing inference cost by 72% while maintaining 97.3% quality.
2. Route based on features of each step (trajectory-aware features) rather than each step independently. Application: route each subtask to appropriate model tier (small/mid/frontier) instead of frontier for every step.

## Assumptions & Limitations
- Distributional shift: AgentRouter trains on trajectories from LangGraph and CrewAI. Testing on AutoGen (unseen framework) shows 6–9% accuracy degradation, though cost reduction still reaches 58%. Cross-framework generalization remains...
- Evaluated on specific benchmarks with specific models.

## Metadata
- Year: 2026, authors: Rudrendu Kumar Paul, Sourav Nandy (Boston University, University of Texas at Austin), arXiv category: cs.AI/cs.LG, PDF link: https://arxiv.org/pdf/2609.22951v1
