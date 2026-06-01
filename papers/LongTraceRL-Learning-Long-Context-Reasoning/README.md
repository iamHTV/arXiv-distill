# [2605.31584v1] LongTraceRL: Học Reasoning Context Dài từ Search Agent Trajectory với Rubric Reward

## Vấn đề
Prior work chưa giải quyết được long-context reasoning vì 2 lý do: (1) training data dùng distractor ngẫu nhiên, dễ lọc, không tạo đủ challenge — model học cách "lọc nhiễu" quá dễ nên không phát triển khả năng reasoning sâu; (2) reward signal chỉ có outcome (đúng/sai cuối cùng), không supervise intermediate reasoning steps — model có thể đoán đúng bằng may mắn mà không thực sự hiểu reasoning chain.

## Đóng góp
1. **Tiered distractor từ search agent trajectory**: Thay vì random distractor, dùng hành vi thật của search agent — documents agent đọc nhưng không trích dẫn (Tier-1, high confusability) và documents hiện trong kết quả nhưng agent không mở (Tier-2, low confusability). Distractor này khó hơn 50% so với random.
2. **Rubric reward — entity-level process supervision**: Dùng gold entities trong reasoning chain làm reward signal, không chỉ outcome. Reward chỉ áp dụng cho câu trả lời đúng (positive-only) để tránh reward hacking.
3. **Cải thiện đồng đều trên nhiều scale**: Test trên 3 model (4B-30B), 5 benchmarks, luôn cải thiện.

## Phương pháp (tóm tắt cốt lõi)
Pipeline 4 bước: (1) Random walk trên Wikipedia knowledge graph để tạo multi-hop questions với 8 bước reasoning; (2) Deploy search agent, ghi lại toàn bộ trajectory (search → open → cite); (3) Chia documents thành Tier-1 (agent đọc nhưng không cite) và Tier-2 (hiện trong kết quả nhưng không mở) làm distractors; (4) Assemble context 128K tokens, shuffle. RL training dùng GRPO với composite reward: r = (1-α)·r_outcome + α·r_rubric, trong đó r_rubric = recall của gold entities trong response. Positive-only: chỉ trả reward > 0 khi outcome đúng.

## Kết quả chính
- Qwen3-4B đạt average 59.0 trên 5 benchmarks, cải thiện +5.7 so với base model, +2.5 so với baseline mạnh nhất (LongRLVR)
- AA-LCR benchmark: 33.2 → 41.8 (+8.6 điểm)
- DeepSeek-R1-8B: 42.7 → 43.8
- Qwen3-30B: 60.5 → 63.7 (+3.2)
- Ablation: bỏ rubric reward → average drop từ 59.0 xuống 53.7 (rubric reward là driver chính)
- Distractor difficulty ranking: random (1.35% entity overlap) < search (15.0%) < traj-random (42.16%) < traj-tiered (50.03%)
- α=0.3 là optimal; α=0.5 quá cao → model học shortcut enumerate entities
- Training: 2,815 examples, 32×H800 GPUs, 200 iterations

## Insight có thể áp dụng ngay
1. **Dùng agent behavior làm training signal**: Khi build RL training data cho LLM, thay vì random noise, hãy dùng hành vi thật của agent (documents đã đọc, đã skip) để tạo distractor. Ví dụ: khi train chatbot trả lời câu hỏi phức tạp, lấy logs từ retrieval system — những document user click vào nhưng không dùng — làm hard negative examples.

2. **Process reward hơn outcome reward**: Chỉ reward kết quả cuối đúng/sai là không đủ. Cần supervise intermediate steps. Ví dụ: khi đánh giá AI viết báo cáo, không chỉ check kết quả cuối mà còn check từng step reasoning — có trích dẫn đúng nguồn không, có bỏ qua thông tin quan trọng không.

3. **Positive-only reward防止hacking**: Khi dùng process reward, chỉ áp dụng cho responses đúng. Nếu áp dụng cho tất cả, model sẽ học cách liệt kê entities mà không reasoning thật. Ví dụ: KPI cho nhân viên — chỉ thưởng process tốt khi kết quả đúng, nếu không nhân viên sẽ optimize quy trình mà không quan tâm outcome.

## Giả định & Hạn chế
**Điều kiện để phương pháp work:**
- Cần knowledge graph với multi-hop paths (ở đây dùng Wikipedia)
- Cần search agent capable để generate meaningful trajectories
- Cần đủ compute (32×H800 GPUs cho 2,815 examples)

**Hạn chế paper thừa nhận:**
- Chỉ dùng KILT Wikipedia snapshot → reasoning patterns có thể thiếu diversity
- Distractor quality phụ thuộc vào capability của search agent — agent yếu hơn → distractor kém chất lượng

**Hạn chế paper KHÔNG nói:**
- Không test trên non-English languages — không rõ transferability
- 8-hop questions có thể quá artificial, không reflect real-world queries
- Context 128K tokens vẫn thấp hơn nhiều real-world scenarios (1M+ tokens)
- Không compare cost-effectiveness — 32×H800 GPUs có practical cho most teams?

## Metadata
- Năm: 2026
- Tác giả: Nianyi Lin, Jiajie Zhang, Lei Hou, Juanzi Li (Tsinghua University)
- Category: cs.CL, cs.AI, cs.LG
- Link PDF: https://arxiv.org/pdf/2605.31584v1
- GitHub: https://github.com/THU-KEG/LongTraceRL
- Citation count: [EXTRACTION FAILED]
