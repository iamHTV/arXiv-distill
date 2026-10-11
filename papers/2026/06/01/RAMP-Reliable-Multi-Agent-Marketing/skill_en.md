# Skill: RAMP — Marketing Multi-Agent with Memory + Reflection
Source: 2508.11120
Type: workflow

## When to use this skill
- When building AI marketing agents that need reliability
- When needing audience curation from structured data
- When agents hallucinate or add unnecessary filters

## When NOT to use
- Simple tasks that don't need multi-agent
- No structured data available
- No client-specific knowledge base

## Required inputs
- Customer data with table metadata
- Client-specific knowledge base (semantic memory)
- Past query history (episodic memory)
- Evaluation queries for testing

## Steps

### Step 1 — Setup Memory Store
1. Semantic memory: client facts, products, campaigns, audience segments
2. Episodic memory: past queries + results
3. Store in retrievable format
4. Update after each interaction

### Step 2 — Build RAMP Pipeline
1. Planner: generates step-by-step plan using table metadata
2. Actor: NL2Code — translates filters to Python functions
3. Verifier: checks output quality
4. Reflector: generates improvement suggestions

### Step 3 — Execute with Memory
1. Retrieve relevant memories before planning
2. Planner uses memories to avoid hallucination
3. Actor executes plan with memory context
4. Verify output against expectations

### Step 4 — Iterate for Ambiguous Queries
1. If query ambiguous → trigger verify/reflect loop
2. Verify: check output quality
3. Reflect: suggest improvements
4. Refine: apply suggestions
5. Repeat until quality acceptable

## Expected output
- +28 pp accuracy vs baseline
- +20 pp recall on ambiguous queries
- Higher user satisfaction
- Fewer hallucinations

## Example application
**Scenario**: Marketing team needs audience curation from customer database.

**Application**:
1. Memory: client facts (products, past campaigns)
2. Query: "Find high-value customers in NY"
3. RAMP: plan → execute → verify → reflect
4. Without memory: adds unnecessary filters → wrong audience
5. With memory: correct filters → right audience (+28 pp accuracy)

## Gotchas
1. **Semantic memory is crucial**: Without it, models hallucinate. Always provide client-specific facts
2. **Planner + Memory = best**: Combined gives +28 pp. Either alone gives less
3. **Iterative verification for ambiguous**: More iterations → better recall
4. **Memory count matters**: Recall increases with more memory, precision peaks at 6
5. **Hallucination risk**: Even with memory, possible. Verify output always
6. **User experience**: Reflect loops can be tedious. Balance quality vs speed
