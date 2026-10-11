# Skill: Few-shot Optimal Selection
Source: 2509.13196
Type: prompt-pattern

## When to use this skill
- When building few-shot prompts for LLM classification tasks
- When optimizing number of examples in prompts
- When avoiding over-prompting problem

## When NOT to use
- Zero-shot sufficient (no few-shot needed)
- Large models (70B+) with strong long-context capabilities
- Non-classification tasks

## Required inputs
- Training examples pool
- LLM being used (need to know model size)
- Target task description
- Evaluation metric

## Steps

### Step 1 — Select Examples with TF-IDF
1. Compute TF-IDF vectors for all training examples
2. Compute similarity between test input and training examples
3. Select top-K most similar examples
4. Output: ranked examples by relevance

### Step 2 — Find Optimal Quantity
1. Start with 5 examples
2. Test performance
3. Gradually increase: 10, 15, 20, 25, 30
4. Find turning point: performance drops = over-prompting
5. Output: optimal K per LLM

### Step 3 — Stratified Selection
1. Ensure examples cover different classes
2. Balance representation
3. Output: balanced few-shot prompt

### Step 4 — Deploy
1. Use optimal K examples
2. Monitor performance
3. Adjust if model updates
4. Output: optimized few-shot prompt

## Expected output
- Optimal number of few-shot examples per LLM
- Better performance with fewer examples
- Avoidance of over-prompting

## Example application
**Scenario**: Classify customer support tickets. Using LLaMA-3.1-8B.

**Application**:
1. TF-IDF: find 50 most similar training tickets
2. Test: 5, 10, 15, 20, 25 examples
3. Result: 10-20 examples optimal. 25+ = performance drops
4. Deploy: use 15 TF-IDF-selected examples
5. Result: surpasses SOTA by 1%

## Gotchas
1. **Less is more**: More examples ≠ better. Find optimal K
2. **TF-IDF selection**: Better than random or semantic embedding
3. **Model size threshold**: 8B parameters may be threshold. Smaller = fewer examples
4. **Task-specific**: Optimal K varies by task. Test yours
5. **Large models more robust**: DeepSeek-V3, GPT-4o handle more examples consistently
