# Skill: Opir — Phân loại An toàn Đa nhiệm Hiệu quả
Nguồn: 2605.29659
Loại: workflow

## Khi nào dùng skill này
- Khi deploy (triển khai) LLM applications cần real-time safety filtering
- Khi cần classify (phân loại) toxicity, jailbreak, hate speech
- Khi cần edge deployment (triển khai biên) với low latency

## KHÔNG nên dùng khi
- Non-LLM applications
- High-impact decisions (legal, employment, credit) — need human review
- Encoder architecture không available

## Input cần có
- LLM prompts và responses cần classify
- Safety taxonomy (996 categories optional)
- Opir model (multi-task hoặc edge variant)

## Các bước thực hiện

### Bước 1 — Choose Model Variant (chọn biến thể)
1. Opir-multitask-large: highest accuracy, multi-task
2. Opir edge (<100M params): fastest, binary classification
3. Choose based on: accuracy needs, latency requirements, compute budget

### Bước 2 — Setup Pipeline (thiết lập quy trình)
1. Pre-processing: text normalization
2. Inference: encoder-based classification
3. Post-processing: threshold application
4. Output: safety labels + confidence scores

### Bước 3 — Apply Safety Filtering (áp dụng lọc an toàn)
1. Real-time: classify prompts before LLM processing
2. Post-processing: classify responses after LLM generation
3. Route: safe → proceed, unsafe → block/modify
4. Output: filtered content

### Bước 4 — Monitor & Update (giám sát & cập nhật)
1. Track false positives/negatives
2. Update taxonomy as threats evolve
3. Retrain periodically
4. Output: improved safety model

## Output mong đợi
- Real-time safety classification
- Sub-10ms latency (edge model)
- 996 categories coverage
- Reduced unsafe content

## Ví dụ áp dụng
**Tình huống**: Deploy LLM chatbot for customer service. Need safety filtering.

**Áp dụng**:
1. Setup: Opir edge model (<100M params) for real-time filtering
2. User prompt → Opir classifies → safe/unsafe
3. If safe → process with LLM. If unsafe → block, log, alert
4. LLM response → Opir classifies → safe/unsafe
5. Result: sub-10ms filtering, reduced harmful content

## Lưu ý quan trọng
1. **Encoder faster than decoder**: Sub-10ms latency. Use for real-time
2. **Multi-task efficiency**: Single model for multiple safety tasks
3. **Edge deployment**: <100M params runs on devices
4. **Over-refusal risk**: May block benign sensitive content. Tune thresholds
5. **Policy-dependent**: Safety labels subjective. Align with your policies
6. **Not for high-stakes**: Don't use as sole decision-maker for legal/employment
