# Skill: agentrouter-step-level-model-routing
Source: 2609.22951v1
Type: framework

## When to use this skill
- Building multi-agent systems that need to reduce inference cost for orchestration decisions (routing and review).
- Have different model tiers available (small, mid, frontier).
- Need to route each step of a multi-step agentic workflow to the appropriate model tier.

## When NOT to use this skill
- Tasks that only have a single step (single-turn task).
- No small model available to route to.
- Don't need to reduce inference cost (only care about absolute quality).

## Input needed
- List of available model tiers (small, mid, frontier).
- Features of each step extractable at routing time, including accumulated context and other features.
- Lightweight classifier like AgentRouter.
- Multi-agent workflow with multiple steps.

## Steps to execute
1. Define available model tiers (small, mid, frontier).
2. Extract features of each step at routing time, including accumulated context and other features.
3. Use a lightweight classifier like AgentRouter to map each step to one of four model tiers.
4. Only call frontier model for steps requiring deep reasoning, use small model for formatting steps.
5. Monitor inference cost and accuracy.

## Expected output
- Reduces inference cost by 72% vs frontier-only baselines.
- Retains 97.3% of frontier-only quality.
- Per-step routing accuracy: 91% on minimal-complexity steps, 85% on efficient-tier steps, 76–82% on harder mid-range and frontier tiers.

## Application example
- Build a document processing agent workflow: step 1 analyzes query (needs large model), step 2 retrieves documents (can use small model), step 3 synthesizes results (needs large model), step 4 extracts fields (can use small model), step 5 creates summary (can use small model), step 6 validates format (can use small model). Apply AgentRouter to route each step to appropriate model tier.

## Gotchas
- Trained on trajectories from LangGraph and CrewAI. Testing on AutoGen (unseen framework) shows 6–9% accuracy degradation, though cost reduction still reaches 58%.
- Cross-framework generalization remains...
