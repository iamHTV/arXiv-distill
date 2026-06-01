# Skill: Offline RL cho Code Generation
Nguồn: 2605.28409
Loại: workflow

## Khi nào dùng skill này
- Khi train code LLMs với RL mà không muốn expensive online inference
- Khi có existing code datasets available
- Khi deploy small code models cần performance boost

## KHÔNG nên dùng khi
- No existing code datasets
- Need online exploration for better performance
- Code quality beyond correctness needed

## Input cần có
- Existing code datasets với test cases
- Base code LLM
- Verifiable rewards (functional correctness)

## Các bước thực hiện

### Bước 1 — Prepare Code Datasets (chuẩn bị dữ liệu code)
1. Collect existing code solutions với test cases
2. Balance dataset if imbalanced
3. Include challenging problems
4. Output: curated code dataset

### Bước 2 — Apply Offline RL (áp dụng RL offline)
1. Use on-policy algorithms trong offline setting
2. Verifiable rewards: code passes tests
3. Train without online inference loops
4. Output: improved code model

### Bước 3 — Evaluate (đánh giá)
1. Test pass@1 và pass@10
2. Focus on challenging problems
3. Compare with baseline
4. Output: performance metrics

## Output mong đợi
- Improved pass@1 và pass@10
- Better performance on challenging problems
- Cost-effective training

## Ví dụ áp dụng
**Tình huống**: Train code assistant for complex algorithms. Limited compute budget.

**Áp dụng**:
1. Collect code dataset with algorithm solutions + test cases
2. Apply offline RL — no online inference needed
3. Train small model (3B parameters)
4. Result: improved pass@1 on challenging algorithms

## Lưu ý quan trọng
1. **Offline = cheaper**: No online inference costs. Use existing datasets
2. **Small models benefit more**: Biggest gains on smaller models
3. **Challenging problems benefit most**: Hard tasks see biggest improvement
4. **Dataset quality matters**: Imbalanced datasets need careful handling
5. **Functional correctness only**: Current approach only checks correctness, not quality
6. **No online exploration**: May miss solutions discoverable through online RL
