# Skill: PARL — Personalized Evaluation via Rubric Learning
Source: 2605.31545v1
Type: evaluation-method

## When to use this skill
- When evaluating personalized LLM outputs
- When needing to learn evaluation criteria from user history
- When static prompts don't capture user preferences

## When NOT to use
- No user behavioral history available
- Cold-start users with sparse history
- Non-personalized evaluation tasks

## Required inputs
- User behavioral history (past interactions, preferences)
- Personalized text generation outputs to evaluate
- User-authored reference texts (ground truth)

## Steps

### Step 1 — Collect User History
1. Gather user's past interactions, preferences, feedback
2. Include: liked/disliked content, style preferences, decision patterns
3. Ensure sufficient quality and quantity

### Step 2 — Induce Evaluation Rubrics
1. Learn multi-dimensional rubrics from user history
2. Not static prompts — learned criteria
3. Self-validation: ensure rubrics consistent with preferences
4. Output: user-specific evaluation rubrics

### Step 3 — Apply Discriminative RL
1. Contrast user-authored responses vs model outputs
2. Capture user-specific decision boundaries
3. Ensure rubrics distinguish authentic vs AI outputs
4. Output: discriminative rubrics

### Step 4 — Evaluate with Learned Rubrics
1. Apply learned rubrics to new personalized outputs
2. Score: user-level accuracy, discriminative margin
3. Identify user-aligned responses
4. Output: personalized evaluation scores

## Expected output
- User-specific evaluation rubrics
- High-fidelity personalized evaluation
- Clear discriminative margin between user and AI outputs
- Generalization across users/tasks

## Example application
**Scenario**: Evaluate AI-generated emails for specific user.

**Application**:
1. User history: past emails, tone preferences, structure patterns
2. Induce rubrics: "prefers concise openings", "uses formal tone", "includes specific data"
3. Discriminative: contrast user's real emails vs AI-generated
4. Evaluate new AI emails against learned rubrics
5. Result: high-fidelity evaluation aligned with user preferences

## Gotchas
1. **Learning > static prompts**: Hand-crafted prompts inadequate. Learn from user history
2. **Discriminative objective essential**: Without it, rubrics overly permissive
3. **Cold-start limitation**: Sparse history → poor rubrics. Need sufficient data
4. **Static preferences assumed**: User preferences may change over time
5. **Reference-free**: No fixed references needed — rubrics from behavior
6. **Privacy concerns**: User history data sensitive. Handle carefully
