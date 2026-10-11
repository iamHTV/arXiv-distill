# Skill: MSIFR — Multi-Stage In-Flight Rejection for Synthetic Data
Source: 2605.14062
Type: workflow

## When to use this skill
- When generating synthetic data with LLMs
- When needing to reduce token costs in data generation
- When quality filters after generation are too expensive

## When NOT to use
- One-off generation (no optimization needed)
- Quality validation requires full output
- No clear intermediate checkpoints

## Required inputs
- LLM for generation
- Rule-based validators per domain
- Intermediate checkpoint positions (e.g., 50%)

## Steps

### Step 1 — Define Stages
1. Decompose generation process into sequential stages
2. Set checkpoint positions (50% optimal)
3. Output: staged generation pipeline

### Step 2 — Implement Validators
1. Arithmetic consistency check
2. Hallucination pattern detection
3. Format validation
4. Output: fast rule-based validators

### Step 3 — Apply In-Flight Rejection
1. At each checkpoint, run validators
2. If fail → terminate early
3. If pass → continue to next stage
4. Output: filtered generation

### Step 4 — Collect Results
1. Only completed samples retained
2. Token savings computed
3. Output: high-quality synthetic data with reduced cost

## Expected output
- 11%-77% token reduction standalone
- Up to 78.2% with early-exit methods
- 5× throughput improvement
- Accuracy preserved or improved

## Example application
**Scenario**: Generate 10K math solutions for training data.

**Application**:
1. Traditional: generate all 10K solutions fully → filter → waste 50% tokens
2. MSIFR: generate to 50% → validate arithmetic → terminate bad ones early
3. Result: 77% fewer tokens, same quality training data

## Gotchas
1. **50% cutoff optimal**: Set checkpoint at mid-solution
2. **Rule-based validators fast**: No model needed for validation
3. **Domain-specific validators**: Need to define per domain
4. **Accuracy preserved**: Early rejection concentrates quality
5. **Composable**: Works with early-exit methods for 78% savings
