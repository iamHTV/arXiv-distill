# [2605.14062] Know When To Fold 'Em: Tạo Dữ liệu Tổng hợp Hiệu quả Token qua Từ chối Đang bay Đa giai đoạn

## Vấn đề
Synthetic data generation (tạo dữ liệu tổng hợp) với LLMs widely used trong post-training pipelines. Nhưng existing approaches generate full outputs trước khi apply quality filters — leading to substantial token waste (lãng phí token đáng kể) trên samples ultimately discarded (bị loại bỏ). Cần detect và terminate low-quality generation trajectories tại intermediate checkpoints (điểm kiểm tra trung gian).

## Đóng góp
1. **MSIFR (Multi-Stage In-Flight Rejection)**: Lightweight, training-free framework detect và terminate low-quality generation tại intermediate checkpoints
2. **Fast rule-based validators**: Kiểm tra arithmetic inconsistencies, hallucination patterns, formatting violations
3. **Formal sequential decision process**: Prove any non-trivial discard policy reduces expected token consumption

## Phương pháp (tóm tắt cốt lõi)
MSIFR: decompose generation process thành sequential stages. Tại mỗi stage, apply fast rule-based validators: arithmetic check, hallucination detection, format validation. Nếu fail → terminate early, don't complete generation. Formalized as sequential decision process. Martingale property: early rejection doesn't bias expected utility of retained samples.

## Kết quả chính
- Token reduction: 11%-77% standalone, up to 78.2% with early-exit methods
- Llama-3.1-8B: strongest efficiency profile — lowest tokens on 4/7 benchmarks
- Accuracy: meets or exceeds traditional baseline in majority of pairs
- 5× throughput improvement with LYNX combination
- No additional training or architectural changes needed

## Insight có thể áp dụng ngay
1. **Early rejection = massive savings**: Don't generate full output before filtering. Reject at intermediate checkpoints. Ví dụ: khi generate synthetic training data, validate tại 50% completion — nếu fail, terminate, save 50% tokens.

2. **Rule-based validators are fast**: Arithmetic, hallucination, format checks — lightweight, no model needed. Ví dụ: khi generate math solutions, check arithmetic consistency at each step — nếu wrong, terminate early.

3. **50% cutoff optimal**: Mid-solution cutoff consistently optimal across benchmarks. Ví dụ: when designing synthetic data pipeline, set checkpoint at 50% completion for validation.

## Giả định & Hạn chế
**Điều kiện để method work:**
- Rule-based validators defined per domain
- Sequential generation process
- Intermediate checkpoints available

**Hạn chế paper thừa nhận:**
- Task-specific validators by design
- 50% cutoff may need retuning for different domains
- Experiments on 7-8B models only

**Hạn paper KHÔNG nói:**
- Validator design effort per domain
- False rejection rate (rejecting good samples)
- Very long-form content may need different approach

## Metadata
- Năm: 2026
- Tác giả: Anjir Ahmed Chowdhury, Syed Zawad, Feng Yan
- Category: cs.AI
- Link PDF: https://arxiv.org/pdf/2605.14062
- Citation count: [EXTRACTION FAILED]
