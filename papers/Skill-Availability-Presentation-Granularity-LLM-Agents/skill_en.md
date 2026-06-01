# Skill: Skill Availability & Presentation Granularity for LLM Agents
Source: 2605.31408v1
Type: evaluation-method

## When to use this skill
- When designing skill documents for LLM agents
- When deciding presentation format for procedural knowledge
- When evaluating effectiveness of skill documentation

## When NOT to use
- Agents don't use skill documents
- Task doesn't need procedural knowledge
- Only 1 model — no cross-model comparison needed

## Required inputs
- Task set to evaluate
- Skill documents at different abstraction levels
- Model configurations (at least 2 models)
- Evaluation metric: pass rate, task success

## Steps

### Step 1 — Define Skill Conditions
1. No skill (baseline)
2. High-abstraction: principles, guidelines
3. Medium-abstraction: structured steps
4. Low-abstraction: detailed checklists
5. With/without worked examples

### Step 2 — Run Controlled Experiment
1. Same tasks across all conditions
2. Multiple trials per condition (5+ recommended)
3. Multiple models (2+ recommended)
4. Record: pass rate, task success per cell

### Step 3 — Analyze Skill Availability Effect
1. Compare: any skill vs no skill
2. Expected: +18-36 pp improvement
3. This is LARGEST signal — prioritize having skills

### Step 4 — Analyze Presentation Effect
1. Compare: low vs high abstraction
2. Expected: small, uncertain effects (CIs cross zero)
3. Compare: with vs without worked examples
4. Expected: small positive effect (+0.7-1.3 pp)

### Step 5 — Draw Design Implications
1. Priority 1: HAVE skill documents (biggest impact)
2. Priority 2: Choose convenient format (presentation doesn't matter much)
3. Priority 3: Add worked examples when convenient (small positive)

## Expected output
- Skill availability effect size per model
- Presentation granularity effect size (small, uncertain)
- Design recommendations: prioritize content over format

## Example application
**Scenario**: Design skill documents for AI coding assistant. Limited budget — need to prioritize.

**Application**:
1. Priority 1: Write skill documents for common tasks (biggest impact: +26-36 pp)
2. Format: use natural format — don't invest in converting to checklists
3. Add 1-2 worked examples per skill (small positive: +1-2 pp)
4. Don't over-optimize presentation — effects uncertain, model-dependent

## Gotchas
1. **Skill availability >> presentation**: Having skills matters most. Don't skip skills because format isn't perfect
2. **Presentation effects uncertain**: Low vs high abstraction CIs cross zero. Don't invest heavily in format optimization
3. **Model-dependent**: DeepSeek with thinking mode may be constrained by low-level instructions. Test on your model
4. **Worked examples are optional**: Small positive effect. Include when convenient
5. **30 tasks subset**: Results specific to this subset. Validate on your tasks
6. **Don't over-specify**: Detailed checklists may constrain model's own planning. Balance guidance with flexibility
