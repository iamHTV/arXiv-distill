# Skill: FiVeD — Fine-grained Verification for Sentiment Triplet Extraction
Source: 2605.31446v1
Type: workflow

## When to use this skill
- When building AI extraction pipelines for sentiment, entities, relations
- When needing to verify extracted outputs, not just extract
- When wanting adjustable precision-recall tradeoffs

## When NOT to use
- Simple tasks where extraction accuracy is already high enough
- No gold annotations available for supervision
- No LLM available for rubric-based scoring

## Required inputs
- Base extractor producing candidate triplets
- Gold annotations (at least a subset) for supervision
- Task-specific error categories definition
- LLM for rubric-based quality scoring

## Steps

### Step 1 — Define Error Categories
1. Hierarchical error types for your task:
   - Boundary errors
   - Single element errors
   - Compound errors
2. Define plausible incorrect candidates per category
3. Create semantic/syntactic constraints for counterfactual mining

### Step 2 — Construct Verification Supervision
1. Counterfactual candidate mining: synthesize plausible invalid triplets
2. Assign hierarchical error types to each candidate
3. LLM with task-specific rubrics generates quality scores + rationales
4. Output: labeled verification dataset

### Step 3 — Train Multi-Task Verifier
1. Main tasks: validity classification + quality score estimation
2. Auxiliary tasks: error type classification + rationale generation
3. Auto-learned task weights
4. Train on verification supervision dataset

### Step 4 — Apply Verification
1. Run base extractor → candidate triplets
2. Verifier scores each candidate: validity + quality
3. Filter: remove low-quality candidates
4. Rerank: sort by quality score
5. Adjustable threshold: precision-recall tradeoff

## Expected output
- Improved extraction F1 score (+3.53 points typical)
- Adjustable precision-recall control
- Diagnostic error information per candidate
- Plug-and-play integration with existing extractors

## Example application
**Scenario**: Build review analysis system. Extract sentiment triplets from customer reviews.

**Application**:
1. Base extractor: generative model extracts (aspect, opinion, sentiment) triplets
2. Error categories: boundary error, aspect error, opinion error, polarity error
3. FiVeD verifier: scores each triplet
4. Filter: remove low-quality triplets
5. Result: +3.5 F1, fewer false positives

## Gotchas
1. **Plug-and-play**: FiVeD works with ANY base extractor — model-agnostic
2. **Adjustable threshold**: Tune quality score threshold for precision vs recall balance
3. **LLM as scorer**: LLM-generated scores have bias — validate on your data
4. **Error categories matter**: Define domain-specific error types for best results
5. **Counterfactual quality**: Synthesized incorrect triplets must be plausible — poor synthesis = poor verifier
6. **Multi-task weight tuning**: Auto-learned weights may be unstable — monitor training
