# [2509.14004] Early Stopping Chain-of-thoughts trong LLMs

## Vấn đề
Reasoning LLMs generate long chain-of-thoughts (CoT — chuỗi suy luận) để solve complicated problems, nhưng lengthy CoT incurs high inference costs (chi phí suy luận cao). Previous methods on inference-stage efficient reasoning either require white-box models (mô hình hộp trắng) hoặc không reliable (đáng tin cậy) through direct prompting.

## Đóng góp
1. **ES-CoT**: Inference-time method shortens CoT generation bằng cách detect answer convergence (phát hiện hội tụ câu trả lời) và stop early với almost no performance loss
2. **Linguistic markers**: Khi observe marker như "wait" trong reasoning → prompt LLM output current step answer. Track run length của consecutive identical step answers
3. **Results**: Reduces inference tokens by 41% on average, maintains accuracy

## Phương pháp (tóm tắt cốt lõi)
ES-CoT: (1) During CoT generation, detect linguistic markers ("wait", "but", "however"); (2) At markers, prompt LLM to output current final answer (step answer); (3) Track run length của consecutive identical step answers; (4) When run length exceeds threshold → answer converged → stop early. Empirical + theoretical: step answers steadily converge, large run-length jumps mark convergence.

## Kết quả chính
- Token reduction: 41% average across 6 datasets, 3 LLMs
- Olympiad + Qwen3: 10,652 → 4,624 tokens (-56.59%)
- Accuracy maintained comparable to standard CoT
- Works across QwQ 32B, Qwen3 8B, DeepSeek-R1-Distill-Llama 8B
- Composable with self-consistency prompting

## Insight có thể áp dụng ngay
1. **Early stopping cho CoT reasoning**: Khi deploy reasoning LLMs, implement ES-CoT để reduce inference costs. Ví dụ: khi AI assistant reasoning through complex problem, detect convergence và stop early — 41% token savings.

2. **Linguistic markers là convergence signals**: "Wait", "but", "however" trong CoT signal answer refinement. Use these as checkpoints. Ví dụ: khi monitor AI reasoning, trigger step answer extraction tại linguistic markers.

3. **Run length = convergence measure**: Consecutive identical step answers = converged. Track run length. Ví dụ: if 10 consecutive step answers identical → stop, no need to continue reasoning.

## Giả định & Hạn chế
**Điều kiện để method work:**
- LLM generates linguistic markers trong CoT
- Step answers converge to final answer
- Minimum run-length threshold tuned

**Hạn chế paper thừa nhận:**
- [EXTRACTION FAILED]

**Hạn chế paper KHÔNG nói:**
- Not all reasoning tasks have clear convergence
- Linguistic markers may not appear in all domains
- Threshold sensitivity
- May miss late-stage corrections

## Metadata
- Năm: 2025
- Tác giả: Minjia Mao, Bowen Yin, Yu Zhu, Xiao Fang
- Category: cs.CL
- Link PDF: https://arxiv.org/pdf/2509.14004
- Citation count: [EXTRACTION FAILED]
