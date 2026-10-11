# Skill: SCR — Knowledge Updating via Selective Contextual Reasoning
Source: 2503.05212
Type: workflow

## When to use this skill
- When updating LLM knowledge without wanting to edit parameters
- When external knowledge base is available
- When model editing methods are insufficient

## When NOT to use
- Simple knowledge updates can be handled by prompt
- No external knowledge base
- Parameter editing required for specific tasks

## Required inputs
- External knowledge base with updated facts
- LLM with contextual reasoning capabilities
- Query scope assessment capability

## Steps

### Step 1 — Setup External Knowledge Base
1. Maintain external KB with updated facts
2. Organize by topics/domains
3. Update independently of LLM
4. Output: current knowledge base

### Step 2 — Assess Query Scope
1. LLM assesses: does query fall within KB scope?
2. If yes → retrieve relevant knowledge
3. If no → answer directly
4. Output: scope decision

### Step 3 — Contextualize & Reason
1. If in scope: inject relevant knowledge texts into context
2. LLM reasons over contextualized knowledge
3. Generate answer based on updated information
4. Output: updated answer

## Expected output
- Updated knowledge without parameter editing
- Better than model editing methods
- Training-free, parameter-free

## Example application
**Scenario**: Company LLM has outdated product info. Products change monthly.

**Application**:
1. External KB: product catalog updated monthly
2. Query: "What's the price of Product X?"
3. SCR: query in scope → inject current price from KB
4. Answer: correct, updated price
5. No model retraining needed

## Gotchas
1. **Don't edit parameters**: Model editing has shortcomings. Use external KB
2. **Selective is key**: Only contextualize when query in scope
3. **External KB maintenance**: Update independently, frequently
4. **Context window limits**: Large KB may exceed context. Prioritize relevant facts
5. **Scope assessment accuracy**: Critical for correct behavior
