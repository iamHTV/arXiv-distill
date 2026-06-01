# Skill: MSIFR — Từ chối Đang bay Đa giai đoạn cho Dữ liệu Tổng hợp
Nguồn: 2605.14062
Loại: workflow

## Khi nào dùng skill này
- Khi generate (tạo) synthetic data với LLMs
- Khi cần reduce (giảm) token costs trong data generation
- Khi quality filters apply sau generation quá tốn kém

## KHÔNG nên dùng khi
- One-off generation (không cần optimization)
- Quality validation requires full output
- No clear intermediate checkpoints

## Input cần có
- LLM cho generation
- Rule-based validators per domain
- Intermediate checkpoint positions (e.g., 50%)

## Các bước thực hiện

### Bước 1 — Define Stages (định nghĩa giai đoạn)
1. Decompose generation process into sequential stages
2. Set checkpoint positions (50% optimal)
3. Output: staged generation pipeline

### Bước 2 — Implement Validators (triển khai bộ kiểm tra)
1. Arithmetic consistency check
2. Hallucination pattern detection
3. Format validation
4. Output: fast rule-based validators

### Bước 3 — Apply In-Flight Rejection (áp dụng từ chối đang bay)
1. At each checkpoint, run validators
2. If fail → terminate early
3. If pass → continue to next stage
4. Output: filtered generation

### Bước 4 — Collect Results (thu thập kết quả)
1. Only completed samples retained
2. Token savings computed
3. Output: high-quality synthetic data with reduced cost

## Output mong đợi
- 11%-77% token reduction standalone
- Up to 78.2% with early-exit methods
- 5× throughput improvement
- Accuracy preserved or improved

## Ví dụ áp dụng
**Tình huống**: Generate 10K math solutions for training data.

**Áp dụng**:
1. Traditional: generate all 10K solutions fully → filter → waste 50% tokens
2. MSIFR: generate to 50% → validate arithmetic → terminate bad ones early
3. Result: 77% fewer tokens, same quality training data

## Lưu ý quan trọng
1. **50% cutoff optimal**: Set checkpoint at mid-solution
2. **Rule-based validators fast**: No model needed for validation
3. **Domain-specific validators**: Need to define per domain
4. **Accuracy preserved**: Early rejection concentrates quality
5. **Composable**: Works with early-exit methods for 78% savings
