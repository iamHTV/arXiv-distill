# Skill: ReMemR1 — Revisitable Memory for Long-Context Agents
Source: 2509.23040
Type: workflow

## When to use this skill
- When building long-context QA agents
- When needing non-linear reasoning through documents
- When "memorize while reading" loses information

## When NOT to use
- Short-context tasks
- Simple linear processing sufficient
- No RL training infrastructure

## Required inputs
- Long-context documents
- QA pairs
- GRPO training infrastructure
- Memory retrieval mechanism

## Steps

### Step 1 — Setup Memory Agent
1. Agent maintains current memory m_t
2. Agent generates callback query q_t
3. State = (m_t, q_t)
4. Output: history-augmented memory agent

### Step 2 — Implement Callback Retrieval
1. At each step, generate callback query
2. Search over entire memory history {m_i}_{i≤t}
3. Retrieve relevant past memories
4. Output: non-linear reasoning capability

### Step 3 — Train with Multi-level Rewards
1. Trajectory-level reward: final answer correctness
2. Step-level reward: relative information gain
3. Normalize across trajectories and steps
4. GRPO optimization
5. Output: trained memory agent

### Step 4 — Deploy & Evaluate
1. Process long documents with callback capability
2. Answer questions requiring multi-hop reasoning
3. Output: long-context QA answers

## Expected output
- Significantly outperforms SOTA on long-context QA
- Negligible computational overhead
- Non-linear reasoning paths

## Example application
**Scenario**: Answer questions from 100-page legal document.

**Application**:
1. Process document chunk by chunk
2. At chunk 50, question references clause in chunk 10
3. Agent generates callback query → retrieves relevant memory from chunk 10
4. Integrates past evidence → answers correctly
5. Result: correct answer without re-reading entire document

## Gotchas
1. **Look back to reason forward**: Enable memory callback
2. **Multi-level rewards**: Step-level + trajectory-level
3. **Non-linear reasoning**: Don't confine to forward-only
4. **Negligible overhead**: Callback retrieval is cheap
5. **Memory history limits**: Very long documents may need pruning
