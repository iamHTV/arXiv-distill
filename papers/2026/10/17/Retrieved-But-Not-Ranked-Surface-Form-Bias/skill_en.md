# Skill: structural-retrieval-evaluation
Source: 2609.01556v1
Type: evaluation-method

## When to use this skill
- Evaluating retrieval systems on structural cases — targets sharing underlying structure but not wording.
- Need to check whether retrieval anchors on literal surface content or underlying structure.
- Have two different domains to evaluate on (e.g., mathematics and agent trajectories).

## When NOT to use this skill
- Only evaluating on queries where surface form and meaning align the same way.
- No structural data (semantically equivalent but different wording targets).
- Don't need to evaluate structure-awareness.

## Input needed
- Structural queries — queries where surface form and meaning are pulled apart.
- Target corpus with items sharing underlying structure but different wording.
- Gold labels for correct targets.
- Lexical reranker and LLM reranker for comparison.

## Steps to execute
1. Build structural query set with disguise tiers: easy, medium, hard.
2. Build corpus with semantically equivalent but differently-worded targets, plus near-miss decoys keeping surface form.
3. Run embedding retrieval and measure strict Hit@k and lenient Hit@10.
4. Run lexical control/reranker and observe whether it helps or hurts.
5. Run LLM reranker (with multiple judges) and measure share of recoverable gap closed.
6. Analyze results: does retrieval anchor on surface content or structure? Does lexical control flip sign?
7. Check for contamination: do reranking gains concentrate on well-known items?

## Expected output
- Strict Hit@k and lenient Hit@10 scores for the retrieval system.
- Determination of whether retrieval anchors on surface content or structure.
- Evaluation of whether lexical control helps or hurts, and what that reveals about the benchmark's surface-variation regime.

## Application example
- Evaluate a retrieval system on math questions: create queries with same mathematical structure but different wording, check whether the system picks the correct target or the lexically similar distractor.

## Gotchas
- Mathematics uses a single fixed seed; bootstrap CIs quantify within-sample uncertainty only.
- Three judges is a small sample; effect sizes vary more than eightfold among them.
- Each domain has a different outlier and tier profile.
