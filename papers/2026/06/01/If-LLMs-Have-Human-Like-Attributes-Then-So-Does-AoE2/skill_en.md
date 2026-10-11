# Skill: Null Assumption for LLM Evaluation
Source: 2605.31514v1
Type: evaluation-method

## When to use this skill
- When evaluating AI capabilities and need to avoid anthropomorphic bias
- When vendor or research claims LLM "understands", "reasons", "creates" — need verification framework
- When designing experiments to evaluate AI systems

## When NOT to use
- Evaluating pure technical performance (accuracy, latency, throughput)
- Already have clear operational definition for the attribute to measure
- Task only needs behavioral benchmark, no need to interpret internal states

## Required inputs
- AI system to evaluate
- Attribute X to verify (e.g., understanding, reasoning, creativity, planning)
- Baseline systems for comparison (e.g., rule-based, random, simple NN)
- Clear behavioral metrics that can be measured

## Steps

### Step 1 — Define Attribute Operationally
1. Select attribute X to verify (e.g., "understanding")
2. Define X in behavioral terms: "X = ability to do Y with Z% accuracy on unseen data"
3. Do NOT define X via human analogy: "X = AI understands like humans"
4. Output: operational definition that can be tested

### Step 2 — Apply Null Assumption
1. Default assumption: AI does NOT have attribute X
2. Burden of proof: must demonstrate the inverse
3. Ask: "Is X unique to this AI system, or can other substrates exhibit X?"

### Step 3 — Substrate Comparison
1. Build/choose baseline systems on different substrates:
   - Rule-based system
   - Simple neural network
   - Random baseline
   - Human baseline (if applicable)
2. Run same behavioral test on all systems
3. If baselines achieve comparable performance → X is NOT unique to LLM

### Step 4 — Measure Substrate-Independently
1. Define measurement criteria BEFORE interpreting behavior
2. Use objective metrics, not subjective interpretation
3. Report: "System A achieves X% on metric M, System B achieves Y% — difference is Z%"
4. Do NOT report: "System A understands better than System B"

### Step 5 — Draw Conclusion
1. If LLM uniquely outperforms all baselines on operational definition → attribute may exist
2. If baselines match LLM → attribute is substrate-dependent, not unique
3. If no clear operational definition possible → attribute is non-measurable, suspend judgment

## Expected output
- Clear verdict: is attribute X unique to LLM?
- Evidence-based conclusion, no circular reasoning
- Actionable decision for business/AI adoption

## Example application
**Scenario**: Vendor claims AI chatbot "understands" customer intent and recommends products.

**Application**:
1. Define "understanding" = correctly identify customer intent with >85% accuracy on unseen queries
2. Null assumption: chatbot does NOT understand, only pattern matches
3. Substrate comparison: rule-based keyword system vs simple classifier vs LLM chatbot
4. Results: rule-based 60%, classifier 72%, LLM 88%
5. Conclusion: LLM uniquely outperforms → "understanding" (operationally defined) exists. But: if classifier achieves 85% → "understanding" is not unique, just better pattern matching

## Gotchas
1. **Avoid circular reasoning**: "AI understands because it answers correctly" → circular. Must define "understand" independent of output
2. **Substrate choice matters**: Baselines too weak → unfair comparison. Baselines too strong → attribute dismissed unfairly
3. **Operational definition quality**: Definition too narrow → attribute always exists. Too broad → never exists. Balance
4. **Scale consideration**: Paper ignores that LLMs have emergent capabilities at scale that small NNs don't → substrate comparison may be unfair
5. **Practical vs philosophical**: Null assumption useful for critical evaluation but can slow down innovation if applied too strictly
