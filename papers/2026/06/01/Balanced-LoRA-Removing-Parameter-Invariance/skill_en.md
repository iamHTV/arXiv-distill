# Skill: BaLoRA — Balanced Low-Rank Adaptation
Source: 2605.31484v1
Type: workflow

## When to use this skill
- When fine-tuning LLMs with LoRA and wanting faster convergence
- When needing stable fine-tuning with less hyperparameter tuning
- When using high-rank LoRA (r=64, 128) and wanting to optimize convergence

## When NOT to use
- Using very low rank (r=2, 4) — small advantage
- Compute budget too tight — projection step adds small overhead
- Already using other LoRA variants (QLoRA, DoRA) that work well

## Required inputs
- Pre-trained LLM to fine-tune
- LoRA configuration: rank r, target layers
- Training data
- Optimizer: AdamW recommended
- BaLoRA implementation (projection step)

## Steps

### Step 1 — Setup Standard LoRA
1. Select target layers (MLP layers recommended)
2. Select rank r (64-128 for best BaLoRA advantage)
3. Initialize A, B matrices standard
4. Setup AdamW optimizer

### Step 2 — Apply BaLoRA Projection
1. After each optimization step:
   - Compute current (A, B)
   - Project onto balanced manifold
   - Update (A, B) with balanced values
2. Projection preserves adapted matrix W + AB
3. Improves conditioning of loss landscape
4. Negligible compute overhead

### Step 3 — Train with Balanced Updates
1. Standard training loop with BaLoRA projection injected
2. Learning rate: constant (no complex schedule needed)
3. Monitor convergence: BaLoRA expected to converge faster
4. Compare with standard LoRA same config

### Step 4 — Evaluate Performance
1. Compare test loss: BaLoRA vs LoRA same iterations
2. Compare final accuracy: BaLoRA vs LoRA same compute budget
3. Check stability: BaLoRA expected more stable across hyperparameters
4. Advantage: largest at high ranks (r=64, 128)

## Expected output
- Faster convergence than standard LoRA
- More stable training across hyperparameters
- Same or better final performance
- Negligible computational overhead

## Example application
**Scenario**: Fine-tune Llama-3.2-3B for customer support chatbot. Limited compute budget.

**Application**:
1. Setup: LoRA r=64, MLP layers, AdamW
2. Standard LoRA: converge after 1000 iterations
3. BaLoRA: converge after 700 iterations (30% faster)
4. Same final accuracy, less compute
5. Bonus: less sensitive to learning rate choice

## Gotchas
1. **High ranks benefit most**: r=64, 128 have largest advantage. r=2, 4 have small advantage
2. **Negligible overhead**: Projection step is computationally lightweight — don't worry about cost
3. **More stable**: BaLoRA is more robust to high learning rates and initialization scalings
4. **Starts slower**: BaLoRA may start slower than LoRA, but converges faster eventually
5. **Preserves adapted matrix**: Projection doesn't change W + AB — same output, better optimization path
6. **Not tested >3B**: Scalability to larger models is unclear — test your use case
