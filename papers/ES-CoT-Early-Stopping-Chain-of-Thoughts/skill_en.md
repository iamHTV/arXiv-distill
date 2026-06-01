# Skill: ES-CoT — Early Stopping Chain-of-Thought
Source: 2509.14004
Type: workflow

## When to use this skill
- When deploying reasoning LLMs needing to reduce inference costs
- When CoT reasoning is too long and expensive
- When needing to maintain accuracy while reducing tokens

## When NOT to use
- Short reasoning tasks (don't need long CoT)
- Tasks without clear convergence patterns
- White-box models not available

## Required inputs
- Reasoning LLM (QwQ, Qwen3, DeepSeek-R1, etc.)
- Linguistic marker definitions ("wait", "but", "however")
- Minimum run-length threshold (d_min=10 recommended)

## Steps

### Step 1 — Detect Linguistic Markers
1. Monitor CoT generation for markers: "wait", "but", "however", "actually"
2. At each marker → trigger step answer extraction
3. Prompt LLM: "Based on your reasoning so far, what is your current answer?"

### Step 2 — Track Step Answers
1. Record step answer at each marker
2. Compare consecutive step answers
3. Track run length of identical answers
4. Output: run length sequence

### Step 3 — Detect Convergence
1. When run length > d_min (10 recommended) → converged
2. Large run-length jump = convergence signal
3. Stop generation when converged
4. Output: final answer with reduced tokens

### Step 4 — Validate
1. Compare accuracy: ES-CoT vs standard CoT
2. Expected: comparable accuracy, 41% token reduction
3. Test across multiple datasets
4. Output: efficiency metrics

## Expected output
- 41% average token reduction
- Comparable accuracy to standard CoT
- Faster inference times
- Cost savings

## Example application
**Scenario**: Deploy reasoning AI assistant. CoT too long, expensive.

**Application**:
1. Monitor CoT for "wait" markers
2. At marker → extract step answer
3. Track: 10 consecutive identical answers → converged
4. Stop early
5. Result: 41% fewer tokens, same accuracy

## Gotchas
1. **41% savings**: Significant cost reduction. Apply immediately
2. **Linguistic markers are key**: "Wait", "but", however" signal refinement points
3. **Run length threshold matters**: d_min=10 recommended. Tune for your task
4. **Composable**: Works with self-consistency prompting
5. **Not all tasks converge**: Some reasoning may not have clear convergence
6. **May miss corrections**: Early stopping may miss late-stage fixes
