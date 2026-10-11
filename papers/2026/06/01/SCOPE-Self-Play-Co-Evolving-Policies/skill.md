# Skill: SCOPE — Data-Free Self-Play cho Open-Ended Tasks
Nguồn: 2605.31433v1
Loại: workflow

## Khi nào dùng skill này
- Khi train LLM trên open-ended tasks mà không có curated training data
- Khi cần self-improvement (tự cải thiện) mà không cần human supervision
- Khi có source documents available cho task generation

## KHÔNG nên dùng khi
- Tasks có rule-checkable answers (dùng GRPO trực tiếp)
- Không có source documents
- Compute budget quá tight (multi-stage pipeline tốn kém)

## Input cần có
- Source documents (tài liệu nguồn) cho task generation
- Base LLM 7-8B (hoặc larger)
- Self-judge model (frozen copy của initial model)
- Quality gates (cổng chất lượng) definitions

## Các bước thực hiện

### Bước 1 — Setup Challenger (thiết lập người thách đấu)
1. Initialize Challenger policy
2. Train để generate document-grounded tasks từ source docs
3. Tasks phải: grounded in document, answerable, specific
4. Quality gates: filter ill-formed, source-irrelevant tasks

### Bước 2 — Setup Solver (thiết lập người giải)
1. Initialize Solver policy
2. Train để answer tasks qua multi-turn retrieval
3. Multi-turn: search → retrieve → synthesize → answer
4. Update based on self-judge feedback

### Bước 3 — Setup Self-Judge (thiết lập tự đánh giá)
1. Freeze copy của initial model
2. For each task: write task-specific rubrics từ source document
3. Rubrics: specific, document-grounded, verifiable criteria
4. Grade Solver responses against rubrics

### Bước 4 — Co-Evolution Loop (vòng lặp đồng tiến hóa)
1. Iteration 1: Challenger generates → Solver answers → Judge grades
2. Update Solver based on Judge feedback
3. Update Challenger based on Solver performance
   - If Solver too good → increase task difficulty
   - If Solver too bad → decrease task difficulty
4. Repeat 3+ iterations

### Bước 5 — Evaluate & Transfer (đánh giá & chuyển giao)
1. Test on training domain benchmarks
2. Test on held-out benchmarks (short-form QA, creative writing)
3. Check: co-evolution gains vs frozen Challenger
4. Check: retrieval vs synthesis contribution per task

## Output mong đợi
- +5-10 points improvement on open-ended benchmarks
- Transfer to held-out domains (+13.8 points on short-form QA)
- Match/exceed GRPO_data without curated data
- Co-evolution necessary for sustained improvement

## Ví dụ áp dụng
**Tình huống**: Train AI customer service agent. No curated training data available. Have product documentation.

**Áp dụng**:
1. Source docs: product manuals, FAQ, policy documents
2. Challenger: generates customer questions from docs
3. Solver: answers via retrieval from product docs
4. Self-judge: writes rubrics ("Does response address billing issue? Does response cite correct policy?")
5. Co-evolve: Challenger adapts difficulty based on Solver performance
6. Result: AI agent improves without curated training data

## Lưu ý quan trọng
1. **Co-evolution is necessary**: Frozen Challenger → no learning value. Must adapt task difficulty
2. **Rubric quality is bottleneck**: Self-judge rubrics must be specific, document-grounded. Generic rubrics = poor signal
3. **Multi-stage compute**: More expensive than single-stage GRPO. Use when curated data unavailable
4. **Content safety risk**: Challenger may generate harmful tasks. Add safety filtering
5. **3 iterations sufficient**: 3 iterations show progressive improvement. More iterations diminishing returns
6. **Transfer beyond training domain**: Gains transfer to short-form QA, creative writing — surprising bonus
