# [2509.23040] ReMemR1: Nhìn lại để Suy luận Tương lai — Bộ nhớ Có thể Truy cập lại cho LLM Agents Ngữ cảnh Dài

## Vấn đề
LLMs face challenges trong long-context QA — key evidence dispersed across millions of tokens. Existing "memorize while reading" methods: linear document scan, memory buffer dynamically updated. Nhưng suffers from: pruning of latent evidence (cắt bằng chứng tiềm ẩn), information loss through overwriting (mất thông tin do ghi đè), sparse RL signals (tín hiệu RL thưa).

## Đóng góp
1. **ReMemR1**: Integrates memory retrieval vào memory update process — enables selective callback of historical memories cho non-linear reasoning (suy luận phi tuyến)
2. **History-Augmented State**: State = (current memory, callback query) — agent searches over entire memory history, not just current memory
3. **Multi-level Reward Design**: Trajectory-level outcome rewards + dense step-level state rewards cho effective memory use

## Phương pháp (tóm tắt cốt lõi)
ReMemR1: (1) Agent maintains current memory m_t + generates callback query q_t; (2) Searches over entire memory history {m_i}_{i≤t} using word overlap retrieval; (3) State = (m_t, q_t) — non-linear reasoning paths; (4) Multi-level reward: trajectory-level (final answer correctness) + step-level (relative information gain at each step); (5) GRPO optimization with normalized rewards.

## Kết quả chính
- Significantly outperforms SOTA baselines trên long-context QA
- Negligible computational overhead
- Non-linear reasoning paths enabled
- Information degradation mitigated
- Dense step-level rewards improve supervision

## Insight có thể áp dụng ngay
1. **Look back để reason forward**: Khi build long-context agents, enable memory callback — agent có thể revisit past memories. Ví dụ: khi AI assistant processes long document, allow it to search back through previous sections khi encountering new evidence.

2. **Multi-level rewards**: Don't just reward final answer. Add dense step-level rewards cho intermediate memory use. Ví dụ: khi train reasoning agent, reward both final correctness AND quality of memory retrieval at each step.

3. **Non-linear reasoning**: Agent shouldn't be confined to forward-only processing. Enable backtracking through memory. Ví dụ: when building document QA system, allow agent to jump back to earlier sections when new context triggers relevant recall.

## Giả định & Hạn chế
**Điều kiện để method work:**
- Long-context documents với dispersed evidence
- Memory retrieval mechanism available
- GRPO training infrastructure

**Hạn chế paper thừa nhận:**
- [EXTRACTION FAILED]

**Hạn paper KHÔNG nói:**
- Memory history size limits
- Retrieval accuracy dependency
- Training cost for RL
- Very long documents (millions of tokens) scalability

## Metadata
- Năm: 2025
- Tác giả: Yaorui Shi, Yuxin Chen, Siyuan Wang, et al.
- Category: cs.AI
- Link PDF: https://arxiv.org/pdf/2509.23040
- Citation count: [EXTRACTION FAILED]
