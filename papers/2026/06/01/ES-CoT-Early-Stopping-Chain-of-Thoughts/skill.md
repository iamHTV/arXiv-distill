# Skill: ES-CoT — Dừng Sớm Chain-of-Thought
Nguồn: 2509.14004
Loại: workflow

## Khi nào dùng skill này
- Khi deploy (triển khai) reasoning LLMs cần reduce inference costs
- Khi CoT reasoning quá dài và tốn kém
- Khi cần maintain accuracy while reducing tokens

## KHÔNG nên dùng khi
- Short reasoning tasks (không cần CoT dài)
- Tasks không có clear convergence pattern
- White-box models không available

## Input cần có
- Reasoning LLM (QwQ, Qwen3, DeepSeek-R1, etc.)
- Linguistic marker definitions ("wait", "but", "however")
- Minimum run-length threshold (d_min=10 recommended)

## Các bước thực hiện

### Bước 1 — Detect Linguistic Markers (phát hiện dấu hiệu ngôn ngữ)
1. Monitor CoT generation for markers: "wait", "but", "however", "actually"
2. At each marker → trigger step answer extraction
3. Prompt LLM: "Based on your reasoning so far, what is your current answer?"

### Bước 2 — Track Step Answers (theo dõi câu trả lời từng bước)
1. Record step answer at each marker
2. Compare consecutive step answers
3. Track run length of identical answers
4. Output: run length sequence

### Bước 3 — Detect Convergence (phát hiện hội tụ)
1. When run length > d_min (10 recommended) → converged
2. Large run-length jump = convergence signal
3. Stop generation when converged
4. Output: final answer with reduced tokens

### Bước 4 — Validate (xác minh)
1. Compare accuracy: ES-CoT vs standard CoT
2. Expected: comparable accuracy, 41% token reduction
3. Test across multiple datasets
4. Output: efficiency metrics

## Output mong đợi
- 41% average token reduction
- Comparable accuracy to standard CoT
- Faster inference times
- Cost savings

## Ví dụ áp dụng
**Tình huống**: Deploy reasoning AI assistant. CoT quá dài, tốn kém.

**Áp dụng**:
1. Monitor CoT for "wait" markers
2. At marker → extract step answer
3. Track: 10 consecutive identical answers → converged
4. Stop early
5. Result: 41% fewer tokens, same accuracy

## Lưu ý quan trọng
1. **41% savings**: Significant cost reduction. Apply immediately
2. **Linguistic markers are key**: "Wait", "but", however" signal refinement points
3. **Run length threshold matters**: d_min=10 recommended. Tune for your task
4. **Composable**: Works with self-consistency prompting
5. **Not all tasks converge**: Some reasoning may not have clear convergence
6. **May miss corrections**: Early stopping may miss late-stage fixes
