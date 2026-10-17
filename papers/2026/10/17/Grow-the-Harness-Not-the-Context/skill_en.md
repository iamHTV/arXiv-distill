# Skill: grow-the-harness-reusable-specialist-agents
Source: 2609.26760v2
Type: framework

## When to use this skill
- Building agents that need to handle streams of related tasks of the same type.
- Need to reduce LLM calls and inference cost for agent running repeatedly on same task type.
- Have trajectory data from previous agent runs on related tasks.

## When NOT to use this skill
- Single tasks not related to each other.
- No trajectory data from previous runs available.
- Don't need to reduce LLM calls and inference cost.

## Input needed
- Trajectories from previous agent runs on related tasks.
- Embedding model to generate numerical representations from trajectories.
- LLM model to generate control code.

## Steps to execute
1. Analyze trajectories from previous agent runs on related tasks.
2. Build persistent Bidirectional Evidence Trace (BET) — connects how harness consumes input with conditions required to make a selected operation unsafe.
3. Retain source-supported correspondences alongside agent's hypotheses and open questions.
4. Provide reading, analysis, and persistence commands to help agent build and reuse this evidence rather than repeatedly retrieve and reconstruct.
5. Evaluate on benchmarks and two backbones like Growing Harness did on BrowseComp-Plus and WebArena-Verified.

## Expected output
- Agent system handling related tasks with significantly reduced LLM calls and inference cost.
- Growing Harness achieves highest mean success in five of six benchmark-model settings and trails best mean by 0.7 pp. in the sixth.
- Relative to Tool-Calling agent, it reduces LLM calls by 76.0–91.8% and deployed-agent inference cost by 74.4–98.6%.
- On WebArena-Verified, its success remains 44.7–45.3% across model scales, whereas Tool-Calling falls to 6.7% with 4B model.

## Application example
- Build an agent to handle related tasks on same type of data (e.g., processing invoices, checking documents, etc.). Use Grow the Harness to turn feedback into reusable control code, reducing LLM calls by 76.0–91.8% and inference cost by 74.4–98.6%.

## Gotchas
- Evaluated on BrowseComp-Plus and WebArena-Verified with three deployment models from 4B to 120B parameters.
- No detailed information about training time and computational cost.
- Do not default to multi-agent — lightweight configurations are often Pareto-optimal.
