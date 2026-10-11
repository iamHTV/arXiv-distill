# Skill: LLM Strategic Foresight Screening
Source: 2602.01684
Type: workflow

## When to use this skill
- When screening large volume opportunities — venture deals, acquisitions, R&D projects, partnerships
- When human evaluation capacity is the bottleneck
- When needing consistent, reproducible ranking under uncertainty

## When NOT to use
- Task requires implementation capability — LLM only evaluates, does not execute
- Information environment too noisy or unstructured — LLM needs standardized summaries
- Outcomes depend on evaluator's own actions — LLM has no skin in the game

## Required inputs
- List of opportunities to evaluate
- Standardized summary for each opportunity — structured format
- Clear evaluation criteria — success/failure definition
- Access to frontier LLM (GPT-5, Gemini 2.5, Claude 4.5+)

## Steps

### Step 1 — Prepare Standardized Summaries
1. Create template for each opportunity: problem, solution, team, market, traction, financials
2. Fill information from pitch deck, financial documents, market research
3. Ensure same format for all opportunities — fair comparison
4. Constraint: do not include outcome information — only pre-decision data

### Step 2 — Pairwise Comparison Tournament
1. Create all pairs (both orders A-B and B-A to avoid order bias)
2. Prompt LLM: "Given these two ventures, which is more likely to succeed? [Summary A] vs [Summary B]"
3. Record winner for each pair
4. Aggregate into full ranking by win rate

### Step 3 — Benchmark against Humans
1. Recruited evaluators: experienced managers, domain experts
2. Same task, same information, same prompts
3. Compare rank correlations with realized outcomes

### Step 4 — Apply Screening Decision
1. LLM ranking → top N opportunities
2. Human review only top N (not all)
3. Final decision: human judgment on filtered set
4. Track: LLM accuracy vs human accuracy on same subset

## Expected output
- Ranked list of opportunities by predicted success probability
- Top N filtered set for human review
- Consistency metrics: LLM rankings stable across multiple runs
- Accuracy benchmark: LLM vs human correlations

## Example application
**Scenario**: Corporate VC receives 500 startup pitches per quarter. Currently: 5 partners review each pitch (2500 evaluations). Want to automate first-pass screening.

**Application**:
1. Standardized summary per startup: problem, solution, market size, team, traction, ask
2. Pairwise tournament: 500 startups → 124,750 pairs → LLM evaluates each pair
3. Ranking by win rate → top 25 startups
4. Partners only review 25 startups (95% workload reduction)
5. Track: LLM top-25 overlap with partners' top-25 if partners reviewed all 500

## Gotchas
1. **Augmentation trap**: Do NOT add human to AI pipeline if AI already outperforming human — may DECREASE performance. Human value lies in shaping inputs, not filtering outputs
2. **Order bias**: Must test both orders A-B and B-A — LLM may bias toward first or second option
3. **Summary quality**: Garbage in, garbage out — standardized summaries must be detailed and fair
4. **Model selection**: Frontier models (GPT-5, Gemini 2.5) outperform smaller models clearly — use frontier
5. **Domain specificity**: Results from venture screening — may not transfer to other domains (medical, legal)
6. **Cost**: 870 pairwise comparisons with frontier models costs significantly — budget first
