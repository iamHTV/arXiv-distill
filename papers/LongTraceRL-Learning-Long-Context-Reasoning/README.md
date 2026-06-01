# [2605.31584v1] LongTraceRL: Học Reasoning (suy luận) Context Dài từ Search Agent Trajectory (lượt tìm kiếm của tác nhân) với Rubric Reward (phần thưởng theo tiêu chí)

## Vấn đề
Các nghiên cứu trước chưa giải quyết được bài toán reasoning (suy luận) trên context (ngữ cảnh) dài vì 2 lý do: (1) dữ liệu huấn luyện dùng distractor (tài liệu gây nhiễu) ngẫu nhiên, dễ lọc, không tạo đủ thử thách — model học cách "lọc nhiễu" quá dễ nên không phát triển khả năng suy luận sâu; (2) reward signal (tín hiệu phần thưởng) chỉ có outcome (kết quả cuối cùng: đúng/sai), không supervise (giám sát) intermediate reasoning steps (các bước suy luận trung gian) — model có thể đoán đúng bằng may mắn mà không thực sự hiểu reasoning chain (chuỗi suy luận).

## Đóng góp
1. **Tiered distractor (tài liệu nhiễu phân tầng) từ search agent trajectory (lượt tìm kiếm của tác nhân)**: Thay vì distractor ngẫu nhiên, dùng hành vi thật của search agent (tác nhân tìm kiếm) — documents agent đọc nhưng không trích dẫn (Tier-1, high confusability — dễ gây nhầm lẫn) và documents hiện trong kết quả nhưng agent không mở (Tier-2, low confusability — ít gây nhầm hơn). Distractor này khó hơn 50% so với ngẫu nhiên.
2. **Rubric reward (phần thưởng theo tiêu chí) — entity-level process supervision (giám sát quy trình ở mức thực thể)**: Dùng gold entities (các thực thể chuẩn) trong reasoning chain (chuỗi suy luận) làm reward signal (tín hiệu phần thưởng), không chỉ outcome (kết quả). Reward chỉ áp dụng cho câu trả lời đúng (positive-only — chỉ dương) để tránh reward hacking (lạm dụng phần thưởng).
3. **Cải thiện đồng đều trên nhiều scale (quy mô)**: Test trên 3 model (4B-30B tham số), 5 benchmarks (bài kiểm tra chuẩn), luôn cải thiện.

## Phương pháp (tóm tắt cốt lõi)
Pipeline (quy trình) 4 bước: (1) Random walk (đi ngẫu nhiên) trên Wikipedia knowledge graph (đồ thị tri thức) để tạo multi-hop questions (câu hỏi đa bước) với 8 bước reasoning (suy luận); (2) Deploy search agent (triển khai tác nhân tìm kiếm), ghi lại toàn bộ trajectory (lượt tìm kiếm) (search → open → cite — tìm kiếm → mở → trích dẫn); (3) Chia documents thành Tier-1 (agent đọc nhưng không cite) và Tier-2 (hiện trong kết quả nhưng không mở) làm distractors; (4) Assemble context 128K tokens (ký tự), shuffle (xáo trộn). RL training (huấn luyện bằng học tăng cường) dùng GRPO (Group Relative Policy Optimization — tối ưu chính sách tương đối theo nhóm) với composite reward (phần thưởng kết hợp): r = (1-α)·r_outcome + α·r_rubric, trong đó r_rubric = recall (tỷ lệ nhớ lại) của gold entities trong response (phản hồi). Positive-only: chỉ trả reward > 0 khi outcome đúng.

## Kết quả chính
- Qwen3-4B đạt average (trung bình) 59.0 trên 5 benchmarks, cải thiện +5.7 so với base model (mô hình gốc), +2.5 so với baseline mạnh nhất (LongRLVR)
- AA-LCR benchmark: 33.2 → 41.8 (+8.6 điểm)
- DeepSeek-R1-8B: 42.7 → 43.8
- Qwen3-30B: 60.5 → 63.7 (+3.2)
- Ablation (kiểm nghiệm thành phần): bỏ rubric reward → average drop từ 59.0 xuống 53.7 (rubric reward là driver chính)
- Distractor difficulty ranking (xếp hạng độ khó): random (1.35% entity overlap — trùng thực thể) < search (15.0%) < traj-random (42.16%) < traj-tiered (50.03%)
- α=0.3 là optimal (tối ưu); α=0.5 quá cao → model học shortcut liệt kê entities
- Training: 2,815 examples, 32×H800 GPUs, 200 iterations (vòng lặp)

## Insight có thể áp dụng ngay
1. **Dùng agent behavior (hành vi tác nhân) làm training signal (tín hiệu huấn luyện)**: Khi build RL training data cho LLM, thay vì random noise (nhiễu ngẫu nhiên), hãy dùng hành vi thật của agent (documents đã đọc, đã skip) để tạo distractor. Ví dụ: khi train chatbot trả lời câu hỏi phức tạp, lấy logs từ retrieval system (hệ thống truy xuất) — những document user click vào nhưng không dùng — làm hard negative examples (ví dụ phủ định khó).

2. **Process reward (phần thưởng quy trình) hơn outcome reward (phần thưởng kết quả)**: Chỉ reward kết quả cuối đúng/sai là không đủ. Cần supervise (giám sát) intermediate steps (các bước trung gian). Ví dụ: khi đánh giá AI viết báo cáo, không chỉ check kết quả cuối mà còn check từng step reasoning — có trích dẫn đúng nguồn không, có bỏ qua thông tin quan trọng không.

3. **Positive-only reward (chỉ thưởng khi đúng)防止reward hacking (lạm dụng phần thưởng)**: Khi dùng process reward, chỉ áp dụng cho responses đúng. Nếu áp dụng cho tất cả, model sẽ học cách liệt kê entities mà không reasoning thật. Ví dụ: KPI cho nhân viên — chỉ thưởng process tốt khi kết quả đúng, nếu không nhân viên sẽ optimize quy trình mà không quan tâm outcome.

## Giả định & Hạn chế
**Điều kiện để phương pháp work:**
- Cần knowledge graph (đồ thị tri thức) với multi-hop paths (đường dẫn đa bước) — ở đây dùng Wikipedia
- Cần search agent capable (tác nhân tìm kiếm đủ mạnh) để generate meaningful trajectories (tạo lượt tìm kiếm có ý nghĩa)
- Cần đủ compute (tài nguyên tính toán) — 32×H800 GPUs cho 2,815 examples

**Hạn chế paper thừa nhận:**
- Chỉ dùng KILT Wikipedia snapshot (bản chụp) → reasoning patterns (khuôn mẫu suy luận) có thể thiếu diversity (đa dạng)
- Distractor quality (chất lượng) phụ thuộc vào capability (năng lực) của search agent — agent yếu hơn → distractor kém chất lượng

**Hạn chế paper KHÔNG nói:**
- Không test trên non-English languages — không rõ transferability (khả năng chuyển giao)
- 8-hop questions có thể quá artificial (nhân tạo), không reflect (phản ánh) real-world queries (truy vấn thực tế)
- Context 128K tokens vẫn thấp hơn nhiều real-world scenarios (1M+ tokens)
- Không compare cost-effectiveness (hiệu quả chi phí) — 32×H800 GPUs có practical (thực tế) cho most teams?

## Metadata
- Năm: 2026
- Tác giả: Nianyi Lin, Jiajie Zhang, Lei Hou, Juanzi Li (Tsinghua University)
- Category: cs.CL, cs.AI, cs.LG
- Link PDF: https://arxiv.org/pdf/2605.31584v1
- GitHub: https://github.com/THU-KEG/LongTraceRL
- Citation count: [EXTRACTION FAILED]
