# Skill: Offline RL for Code Generation
Source: 2605.28409
Type: workflow

## When to use this skill
- When training code LLMs with RL without expensive online inference
- When existing code datasets are available
- When deploying small code models needing performance boost

## When NOT to use
- No existing code datasets
- Need online exploration for better performance
- Code quality beyond correctness needed

## Required inputs
- Existing code datasets with test cases
- Base code LLM
- Verifiable rewards (functional correctness)

## Steps

### Step 1 — Prepare Code Datasets
1. Collect existing code solutions with test cases
2. Balance dataset if imbalanced
3. Include challenging problems
4. Output: curated code dataset

### Step 2 — Apply Offline RL
1. Use on-policy algorithms in offline setting
2. Verifiable rewards: code passes tests
3. Train without online inference loops
4. Output: improved code model

### Step 3 — Evaluate
1. Test pass@1 and pass@10
2. Focus on challenging problems
3. Compare with baseline
4. Output: performance metrics

## Expected output
- Improved pass@1 and pass@10
- Better performance on challenging problems
- Cost-effective training

## Example application
**Scenario**: Train code assistant for complex algorithms. Limited compute budget.

**Application**:
1. Collect code dataset with algorithm solutions + test cases
2. Apply offline RL — no online inference needed
3. Train small model (3B parameters)
4. Result: improved pass@1 on challenging algorithms

## Gotchas
1. **Offline = cheaper**: No online inference costs. Use existing datasets
2. **Small models benefit more**: Biggest gains on smaller models
3. **Challenging problems benefit most**: Hard tasks see biggest improvement
4. **Dataset quality matters**: Imbalanced datasets need careful handling
5. **Functional correctness only**: Current approach only checks correctness, not quality
6. **No online exploration**: May miss solutions discoverable through online RL
