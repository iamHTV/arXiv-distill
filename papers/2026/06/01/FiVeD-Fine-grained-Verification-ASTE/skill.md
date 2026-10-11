# Skill: FiVeD — Xác minh Chi tiết cho Sentiment Triplet Extraction
Nguồn: 2605.31446v1
Loại: workflow

## Khi nào dùng skill này
- Khi build (xây dựng) AI extraction pipeline cho sentiment, entities, relations
- Khi cần verify (xác minh) extracted outputs không chỉ extract
- Khi muốn adjustable precision-recall tradeoffs

## KHÔNG nên dùng khi
- Task đơn giản, extraction accuracy đã đủ cao
- Không có gold annotations cho supervision
- Không có LLM available cho rubric-based scoring

## Input cần có
- Base extractor producing candidate triplets
- Gold annotations (ít nhất subset) cho supervision
- Task-specific error categories definition
- LLM cho rubric-based quality scoring

## Các bước thực hiện

### Bước 1 — Define Error Categories (định nghĩa loại lỗi)
1. Hierarchical error types cho your task:
   - Boundary errors (lỗi ranh giới)
   - Single element errors (lỗi phần tử đơn)
   - Compound errors (lỗi phức hợp)
2. Define plausible incorrect candidates per category
3. Create semantic/syntactic constraints cho counterfactual mining

### Bước 2 — Construct Verification Supervision (xây dựng giám sát xác minh)
1. Counterfactual candidate mining: synthesize plausible invalid triplets
2. Assign hierarchical error types to each candidate
3. LLM with task-specific rubrics generates quality scores + rationales
4. Output: labeled verification dataset

### Bước 3 — Train Multi-Task Verifier (huấn luyện trình xác minh đa nhiệm)
1. Main tasks: validity classification + quality score estimation
2. Auxiliary tasks: error type classification + rationale generation
3. Auto-learned task weights
4. Train on verification supervision dataset

### Step 4 — Apply Verification (áp dụng xác minh)
1. Run base extractor → candidate triplets
2. Verifier scores each candidate: validity + quality
3. Filter: remove low-quality candidates
4. Rerank: sort by quality score
5. Adjustable threshold: precision-recall tradeoff

## Output mong đợi
- Improved extraction F1 score (+3.53 points typical)
- Adjustable precision-recall control
- Diagnostic error information per candidate
- Plug-and-play integration with existing extractors

## Ví dụ áp dụng
**Tình huống**: Build review analysis system. Extract sentiment triplets từ customer reviews.

**Áp dụng**:
1. Base extractor: generative model extracts (aspect, opinion, sentiment) triplets
2. Error categories: boundary error, aspect error, opinion error, polarity error
3. FiVeD verifier: scores each triplet
4. Filter: remove low-quality triplets
5. Result: +3.5 F1, fewer false positives

## Lưu ý quan trọng
1. **Plug-and-play**: FiVeD works with ANY base extractor — model-agnostic
2. **Adjustable threshold**: Tune quality score threshold cho precision vs recall balance
3. **LLM as scorer**: LLM-generated scores có bias — validate on your data
4. **Error categories matter**: Define domain-specific error types cho best results
5. **Counterfactual quality**: Synthesized incorrect triplets must be plausible — poor synthesis = poor verifier
6. **Multi-task weight tuning**: Auto-learned weights may不稳定 — monitor training
