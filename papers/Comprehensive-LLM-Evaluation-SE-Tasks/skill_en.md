# Skill: LLM SE Efficiency Evaluation
Source: 2602.07079
Type: evaluation-method

## When to use this skill
- When evaluating LLMs for software engineering tasks
- When comparing models on efficiency, not just accuracy
- When identifying inefficiency patterns in AI agents

## When NOT to use
- Non-SE tasks
- Accuracy-only evaluation sufficient
- No tool call tracking available

## Required inputs
- LLM candidates to evaluate
- SE tasks (bug fixing, feature dev, refactoring, etc.)
- Automated verification framework
- Cost tracking capability

## Steps

### Step 1 — Define SE Tasks
1. Bug fixing: fix code bugs
2. Feature development: implement new features
3. Code refactoring: improve code structure
4. Technical copywriting: write technical docs
5. Research synthesis: synthesize research findings
6. Output: 5 representative tasks

### Step 2 — Evaluate Quality + Efficiency
1. Run each model on each task
2. Measure: quality score, completion time, tool calls, cost
3. Output: performance matrix

### Step 3 — Analyze Efficiency Variance
1. Compare models with same quality scores
2. Compute: speed variance, tool efficiency variance, cost variance
3. Identify: loop inefficiency, inference inefficiency
4. Output: efficiency analysis

### Step 4 — Select Best Model
1. Rank by: quality × efficiency composite score
2. Consider: speed-quality tradeoff
3. Output: model recommendation

## Expected output
- Model ranking by efficiency, not just accuracy
- Identification of inefficiency patterns
- Cost-effective model selection

## Example application
**Scenario**: Choose LLM for code assistant deployment.

**Application**:
1. Evaluate GPT-5.1, Gemini-3, Deepseek on bug fixing
2. GPT-5.1: 18.8s, 3 tools. Gemini-3: 625s, 917 tools — same score
3. Choose GPT-5.1: 49× more efficient
4. Result: same quality, 49× lower cost

## Gotchas
1. **Efficiency > accuracy**: Same accuracy models have 49× efficiency difference
2. **More tools ≠ better**: No correlation between tool count and success
3. **Loop inefficiency**: Agent repeats tool sequences — needs stopping logic
4. **Inference inefficiency**: Model slow but correct — needs faster model
5. **OpenAI fastest**: Avg 54s, best speed-quality tradeoff
