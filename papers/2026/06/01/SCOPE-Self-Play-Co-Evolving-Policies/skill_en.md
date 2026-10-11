# Skill: SCOPE — Data-Free Self-Play for Open-Ended Tasks
Source: 2605.31433v1
Type: workflow

## When to use this skill
- When training LLMs on open-ended tasks without curated training data
- When needing self-improvement without human supervision
- When source documents are available for task generation

## When NOT to use
- Tasks have rule-checkable answers (use GRPO directly)
- No source documents available
- Compute budget too tight (multi-stage pipeline is expensive)

## Required inputs
- Source documents for task generation
- Base LLM 7-8B (or larger)
- Self-judge model (frozen copy of initial model)
- Quality gates definitions

## Steps

### Step 1 — Setup Challenger
1. Initialize Challenger policy
2. Train to generate document-grounded tasks from source docs
3. Tasks must be: grounded in document, answerable, specific
4. Quality gates: filter ill-formed, source-irrelevant tasks

### Step 2 — Setup Solver
1. Initialize Solver policy
2. Train to answer tasks via multi-turn retrieval
3. Multi-turn: search → retrieve → synthesize → answer
4. Update based on self-judge feedback

### Step 3 — Setup Self-Judge
1. Freeze copy of initial model
2. For each task: write task-specific rubrics from source document
3. Rubrics: specific, document-grounded, verifiable criteria
4. Grade Solver responses against rubrics

### Step 4 — Co-Evolution Loop
1. Iteration 1: Challenger generates → Solver answers → Judge grades
2. Update Solver based on Judge feedback
3. Update Challenger based on Solver performance
   - If Solver too good → increase task difficulty
   - If Solver too bad → decrease task difficulty
4. Repeat 3+ iterations

### Step 5 — Evaluate & Transfer
1. Test on training domain benchmarks
2. Test on held-out benchmarks (short-form QA, creative writing)
3. Check: co-evolution gains vs frozen Challenger
4. Check: retrieval vs synthesis contribution per task

## Expected output
- +5-10 points improvement on open-ended benchmarks
- Transfer to held-out domains (+13.8 points on short-form QA)
- Match/exceed GRPO_data without curated data
- Co-evolution necessary for sustained improvement

## Example application
**Scenario**: Train AI customer service agent. No curated training data available. Have product documentation.

**Application**:
1. Source docs: product manuals, FAQ, policy documents
2. Challenger: generates customer questions from docs
3. Solver: answers via retrieval from product docs
4. Self-judge: writes rubrics ("Does response address billing issue? Does response cite correct policy?")
5. Co-evolve: Challenger adapts difficulty based on Solver performance
6. Result: AI agent improves without curated training data

## Gotchas
1. **Co-evolution is necessary**: Frozen Challenger → no learning value. Must adapt task difficulty
2. **Rubric quality is bottleneck**: Self-judge rubrics must be specific, document-grounded. Generic rubrics = poor signal
3. **Multi-stage compute**: More expensive than single-stage GRPO. Use when curated data unavailable
4. **Content safety risk**: Challenger may generate harmful tasks. Add safety filtering
5. **3 iterations sufficient**: 3 iterations show progressive improvement. More iterations = diminishing returns
6. **Transfer beyond training domain**: Gains transfer to short-form QA, creative writing — surprising bonus
