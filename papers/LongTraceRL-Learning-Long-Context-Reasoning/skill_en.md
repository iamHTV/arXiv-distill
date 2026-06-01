# Skill: Rubric Reward for Long-Context RL Training
Source: 2605.31584v1
Type: framework

## When to use this skill
- When training LLM reasoning on long-context (10K+ tokens) with many distractors
- When fine-grained process supervision is needed, not just outcome reward
- When building RL training data for multi-hop question answering

## When NOT to use
- Simple, short-context tasks (< 4K tokens)
- No knowledge graph or structured data source available
- Insufficient compute budget (< 8 GPUs)

## Required inputs
- Knowledge graph or structured data source (Wikipedia, internal KB)
- Search agent or retrieval system with logging capability
- Base reasoning LLM (4B+ parameters)
- Target context length (recommended: 128K tokens)
- Multi-hop questions or ability to generate them

## Steps

### Step 1 — Generate Multi-Hop Questions
1. Build knowledge graph from data source (use hyperlinks, entity relations)
2. Random walk on graph, 8 steps, each step LLM selects most relevant next entity
3. Prompt powerful LLM (GPT-4+) to generate question requiring reasoning through all entities
4. Constraint: must paraphrase identifying info, answer must be unique
5. Output: question + answer + list of gold entities {e1, e2, ..., ek}

### Step 2 — Collect Search Agent Trajectories
1. Deploy search agent (search → open → cite capabilities)
2. Sample K=5 trajectories per question
3. Filter: keep only trajectories where agent answered correctly
4. Record complete trajectory: τ = [(action_type, document), ...]

### Step 3 — Extract Tiered Distractors
1. Tier-1 (high confusability): documents agent opened & read but did NOT cite in response
2. Tier-2 (low confusability): documents appearing in search results but agent did NOT open
3. Prioritize Tier-1 when filling context

### Step 4 — Assemble Training Context
1. Start with gold evidence passages
2. Add Tier-1 distractors first (more challenging)
3. If target length not reached → add Tier-2
4. Shuffle all documents (prevent positional shortcuts)
5. Target: 128K tokens per example

### Step 5 — RL Training with Rubric Reward
1. Algorithm: GRPO (Group Relative Policy Optimization), group size G=8
2. Outcome reward: binary (1 if answer correct, 0 if wrong)
3. Rubric reward: r_rubric = |gold entities appear in response| / |total gold entities|
4. Group-level normalization: divide by max within group
5. Positive-only: apply rubric reward only when outcome = 1
6. Combined: r = (1-α)·r_outcome + α·r_rubric, α=0.3
7. Train 200 iterations, learning rate 2e-6

## Expected output
- Model improves reasoning on long-context benchmarks
- Responses more grounded in evidence (higher entity recall)
- Longer, more deliberate reasoning chains
- Improvement: +3-6 points average on long-context benchmarks

## Example application
**Scenario**: Company has internal knowledge base of 10K documents. Want to train AI assistant to answer complex questions requiring information from multiple documents.

**Application**:
1. Build KG from internal docs (entity extraction + linking)
2. Generate multi-hop questions: "What is the revenue growth rate of the division that acquired Company X in Q3?"
3. Deploy search agent, collect trajectories as agent attempts to answer
4. Tier-1: docs agent read but didn't cite (same topic, easily confused)
5. Tier-2: docs in search results but agent didn't open
6. Train with rubric reward: check if model mentions correct entities (division name, acquisition date, revenue figure)

## Gotchas
1. **α too high (≥0.5)**: Model learns entity enumeration instead of real reasoning → keep α=0.3
2. **Distractors too easy**: Random distractors don't challenge enough → must use agent trajectories
3. **Reward hacking**: If rubric applied to wrong answers → model lists entities randomly → positive-only strategy
4. **Context length**: 128K tokens needs lots of GPU memory → may need gradient checkpointing
5. **Agent quality**: Weak agent → poor quality distractors → weak training signal
6. **Data size**: Only 2,815 examples but sufficient due to high quality; large data not needed if distractors are hard
