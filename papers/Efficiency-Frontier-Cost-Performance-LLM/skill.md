# Skill: Efficiency Frontier — Tối ưu Chi phí-Hiệu suất LLM
Nguồn: 2605.23071
Loại: evaluation-method (phương pháp đánh giá)

## Khi nào dùng skill này
- Khi choose (chọn) context strategy cho LLM systems
- Khi optimize (tối ưu) cost-performance trade-off
- Khi compare (so sánh) retrieval vs preprocessing strategies

## KHÔNG nên dùng khi
- Cost không phải concern
- Simple tasks không cần context management
- Token cost không measurable

## Input cần có
- Task performance metrics (F1, accuracy)
- Token cost measurements
- Available context strategies (retrieval, preprocessing, full-context)
- Deployment preference (w parameter: performance vs cost)

## Các bước thực hiện

### Bước 1 — Define Cost Model (định nghĩa mô hình chi phí)
1. Measure preprocessing cost (T_stage1)
2. Measure per-query inference cost (T_stage2)
3. Estimate reuse factor (N = number of queries)
4. EffectiveTokens = T_stage2 + T_stage1/N

### Bước 2 — Compute Efficiency Score (tính điểm hiệu quả)
1. Choose w ∈ [0,1]: performance vs cost preference
2. EfficiencyScore = w·F1 - (1-w)·log(EffectiveTokens)
3. Higher w = prioritize accuracy
4. Lower w = prioritize cost

### Bước 3 — Build Efficiency Frontier (xây dựng biên hiệu quả)
1. For each strategy, compute (F1, EffectiveTokens) pairs
2. Plot F1 vs log(EffectiveTokens)
3. Frontier = strategies with best F1 at each cost level
4. Choose strategy on frontier for your w

### Step 4 — Deploy (triển khai)
1. Select strategy on frontier
2. Monitor performance và cost
3. Adjust w if preferences change
4. Output: optimized context management

## Output mong đợi
- ~25% token reduction at comparable performance
- >50% lower token cost with amortized compression
- Clear strategy selection guidelines

## Ví dụ áp dụng
**Tình huống**: RAG system processing 10K queries/day. Need to balance accuracy và cost.

**Áp dụng**:
1. Strategies: full-context, retrieval, memory compression
2. Compute: F1 và token cost per strategy
3. Frontier: retrieval optimal at low cost, memory compression at high performance
4. Choose: w=0.7 (prioritize accuracy) → memory compression
5. Result: 50% lower cost than full-context, similar F1

## Lưu ý quan trọng
1. **Deployment-aware**: Jointly optimize performance + cost + reuse
2. **Amortization matters**: High reuse = lower effective cost
3. **Frontier selection**: Always choose strategy on frontier
4. **w parameter**: Tune based on your priorities
5. **Latency not modeled**: Consider separately
