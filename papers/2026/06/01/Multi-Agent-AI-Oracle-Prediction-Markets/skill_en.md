# Skill: Multi-Agent Oracle with Hybrid Routing
Source: 2605.30802v1
Type: workflow

## When to use this skill
- When building multi-agent systems for decision resolution with financial consequences
- When needing reliable outcome resolution from multiple AI models
- When designing hybrid AI-human systems

## When NOT to use
- Simple tasks where single model suffices
- No shared evidence available — deliberation may be useful
- No access to multiple diverse LLMs
- Tasks requiring creative exploration — deliberation better

## Required inputs
- Multiple diverse LLMs (not same architecture/training data)
- Common evidence layer: retrieval system
- Questions/decisions to resolve
- Confidence calibration data
- Human reviewers for escalation cases

## Steps

### Step 1 — Setup Independent Aggregation
1. Deploy 3+ diverse LLMs (not same provider/architecture)
2. Common evidence retrieval: all models access same evidence
3. Each model resolves independently — do NOT share reasoning
4. Collect: binary decision + confidence score per model

### Step 2 — Compute Aggregation Signals
1. Majority vote: model with >50% votes → winner
2. Confidence-weighted vote: weight each model's vote by confidence
3. Inter-agent agreement: unanimous (3-0) vs split (2-1)
4. Average confidence: mean of all models' confidence scores
5. Composite score = 1[unanimous] + confidence_mean (range 0-2)

### Step 3 — Apply Routing Rules
1. Unanimous + high confidence (≥0.91) → AUTO-RESOLVE
   - Expected accuracy: ~97.87%
   - Coverage: ~47% of questions
2. Unanimous + medium confidence → AUTO-RESOLVE with monitoring
3. Split (2-1 vote) → ESCALATE to human review
   - Expected accuracy if auto-resolve: ~57.82% — too risky
4. Low confidence regardless of agreement → ESCALATE

### Step 4 — Monitor Error Correlations
1. Track error rates per model pair
2. Compute error correlation: r = correlation of failure patterns
3. If r > 0.6 → aggregation gains fundamentally limited
4. If r < 0.4 → aggregation can approach Condorcet ceiling
5. Diversify models if correlation too high

### Step 5 — Handle Escalation
1. Route escalated questions to human reviewers
2. Provide: question, evidence, all model decisions + confidence, disagreement signal
3. Do NOT provide model reasoning traces — increases acceptance regardless of correctness
4. Instead: show confidence scores + disagreement patterns (more actionable)
5. Track: human accuracy on escalated questions

## Expected output
- Auto-resolved questions: ~47% coverage, ~97.87% accuracy
- Escalated questions: ~53%, routed to human review
- Overall system accuracy: 83-90% depending on escalation threshold
- Error correlation monitoring: alert if r > 0.6

## Example application
**Scenario**: Financial prediction market needs to resolve 1,000 questions/week. Current: single LLM oracle 82% accuracy. Want to improve.

**Application**:
1. Deploy 3 diverse LLMs: GPT-5, DeepSeek, Llama
2. Common evidence: Exa retrieval, filtered by date
3. Independent resolution: each model answers independently
4. Routing:
   - 470 questions unanimous + high confidence → auto-resolve (97.87% accuracy)
   - 530 questions with disagreement → escalate to human review
5. Overall: 470 × 0.9787 + 530 × 0.95 (human accuracy) = 964/1000 = 96.4% accuracy
6. Cost: 3x API cost + human review cost for 53% of questions

## Gotchas
1. **Do NOT use deliberation for evidence-based tasks**: Debate HURTS accuracy. Confidently wrong models flip correct ones. Use only independent aggregation
2. **Error correlation is the bottleneck**: If models fail on same questions → aggregation gains limited. Diversify models
3. **Disagreement > confidence**: Inter-agent disagreement is strongest predictor of error. Use it as escalation signal
4. **Don't show reasoning traces to humans**: Explanations increase acceptance regardless of correctness. Show confidence + disagreement instead
5. **Coverage-accuracy tradeoff**: Auto-resolve more → lower accuracy. Tune threshold based on financial stakes
6. **Cost consideration**: 3x API cost + human review cost. ROI depends on question volume and stakes
