# Skill: Rubric Reward (phần thưởng theo tiêu chí) cho Long-Context RL Training (huấn luyện học tăng cường trên ngữ cảnh dài)
Nguồn: 2605.31584v1
Loại: framework (khung phương pháp)

## Khi nào dùng skill này
- Khi train (huấn luyện) LLM reasoning (suy luận) trên long-context (ngữ cảnh dài, 10K+ tokens) với nhiều distractor (tài liệu nhiễu)
- Khi cần fine-grained process supervision (giám sát quy trình chi tiết), không chỉ outcome reward (phần thưởng kết quả)
- Khi build (xây dựng) RL training data (dữ liệu huấn luyện học tăng cường) cho multi-hop question answering (trả lời câu hỏi đa bước)

## KHÔNG nên dùng khi
- Task đơn giản, short-context (ngữ cảnh ngắn, < 4K tokens)
- Không có knowledge graph (đồ thị tri thức) hoặc structured data source (nguồn dữ liệu có cấu trúc)
- Không đủ compute budget (ngân sách tính toán, < 8 GPUs)

## Input cần có
- Knowledge graph (đồ thị tri thức) hoặc structured data source (nguồn dữ liệu có cấu trúc) — Wikipedia, internal KB (cơ sở tri thức nội bộ)
- Search agent (tác nhân tìm kiếm) hoặc retrieval system (hệ thống truy xuất) có logging capability (khả năng ghi log)
- Base reasoning LLM (mô hình ngôn lý luận gốc, 4B+ parameters — tham số)
- Target context length (độ dài ngữ cảnh mục tiêu) — đề xuất 128K tokens
- Multi-hop questions (câu hỏi đa bước) hoặc ability to generate them (khả năng tạo ra chúng)

## Các bước thực hiện

### Bước 1 — Tạo Multi-Hop Questions (câu hỏi đa bước)
1. Build knowledge graph (xây dựng đồ thị tri thức) từ data source (dùng hyperlinks — siêu liên kết, entity relations — quan hệ thực thể)
2. Random walk (đi ngẫu nhiên) trên graph, 8 bước, mỗi bước LLM chọn entity (thực thể) tiếp theo relevant nhất (liên quan nhất)
3. Prompt powerful LLM (GPT-4+) tạo câu hỏi yêu cầu reasoning qua tất cả entities
4. Constraint (ràng buộc): phải paraphrase (diễn đạt lại) identifying info (thông tin nhận diện), answer phải unique (duy nhất)
5. Output: question + answer + list gold entities {e1, e2, ..., ek}

### Bước 2 — Collect Search Agent Trajectories (thu thập lượt tìm kiếm của tác nhân)
1. Deploy search agent (triển khai tác nhân tìm kiếm) với capabilities: search → open → cite (tìm kiếm → mở → trích dẫn)
2. Sample K=5 trajectories (lấy mẫu 5 lượt) per question
3. Filter (lọc): chỉ giữ trajectories agent trả lời đúng
4. Record complete trajectory (ghi lại lượt đầy đủ): τ = [(action_type — loại hành động, document — tài liệu), ...]

### Bước 3 — Extract Tiered Distractors (trích xuất tài liệu nhiễu phân tầng)
1. Tier-1 (high confusability — dễ gây nhầm): documents agent opened & read nhưng KHÔNG cite trong response (phản hồi)
2. Tier-2 (low confusability — ít gây nhầm): documents hiện trong search results nhưng agent KHÔNG mở
3. Ưu tiên Tier-1 trước khi fill context (điền ngữ cảnh)

### Bước 4 — Assemble Training Context (lắp ráp ngữ cảnh huấn luyện)
1. Start với gold evidence passages (đoạn văn bằng chứng chuẩn)
2. Add Tier-1 distractors trước (challenging hơn — thử thách hơn)
3. Nếu chưa đủ target length → thêm Tier-2
4. Shuffle toàn bộ documents (xáo trộn để tránh positional shortcuts — lối tắt vị trí)
5. Target: 128K tokens per example

### Bước 5 — RL Training với Rubric Reward
1. Algorithm (thuật toán): GRPO (Group Relative Policy Optimization — tối ưu chính sách tương đối theo nhóm), group size G=8
2. Outcome reward (phần thưởng kết quả): binary (nhị phân — 1 nếu answer đúng, 0 nếu sai)
3. Rubric reward: r_rubric = |gold entities appear in response| / |total gold entities| (tỷ lệ thực thể chuẩn xuất hiện trong phản hồi)
4. Group-level normalization (chuẩn hóa theo nhóm): chia cho max trong group
5. Positive-only (chỉ dương): chỉ apply rubric reward khi outcome = 1
6. Combined (kết hợp): r = (1-α)·r_outcome + α·r_rubric, α=0.3
7. Train 200 iterations (vòng lặp), learning rate (tốc độ học) 2e-6

## Output mong đợi
- Model reasoning tốt hơn trên long-context benchmarks (bài kiểm tra chuẩn)
- Response grounded in evidence hơn (phản hồi dựa trên bằng chứng hơn, higher entity recall — tỷ lệ nhớ thực thể cao hơn)
- Longer, more deliberate reasoning chains (chuỗi suy luận dài hơn, có chủ đích hơn)
- Cải thiện: +3-6 điểm average trên long-context benchmarks

## Ví dụ áp dụng
**Tình huống**: Company có internal knowledge base (cơ sở tri thức nội bộ) 10K documents. Muốn train AI assistant trả lời câu hỏi phức tạp cần thông tin từ nhiều documents.

**Áp dụng**:
1. Build KG từ internal docs (entity extraction — trích xuất thực thể + linking — liên kết)
2. Generate multi-hop questions: "What is the revenue growth rate of the division that acquired Company X in Q3?"
3. Deploy search agent, collect trajectories khi agent cố trả lời
4. Tier-1: docs agent đọc nhưng không cite (cùng topic, dễ confuse)
5. Tier-2: docs hiện trong search nhưng agent không mở
6. Train với rubric reward: check model có mention đúng entities (division name — tên bộ phận, acquisition date — ngày mua lại, revenue figure — số liệu doanh thu) không

## Lưu ý quan trọng
1. **α quá cao (≥0.5)**: Model học enumerate entities (liệt kê thực thể) thay vì reasoning thật → giữ α=0.3
2. **Distractor quá dễ**: Random distractor không challenge đủ → phải dùng agent trajectory
3. **Reward hacking (lạm dụng phần thưởng)**: Nếu apply rubric cho cả wrong answers → model liệt kê entities lung tung → positive-only strategy (chiến lược chỉ dương)
4. **Context length**: 128K tokens cần nhiều GPU memory (bộ nhớ) → có thể cần gradient checkpointing (lưu điểm kiểm tra gradient)
5. **Agent quality**: Agent yếu → distractor kém chất lượng → training signal yếu
6. **Data size**: Chỉ 2,815 examples nhưng đủ vì quality cao; không cần data lớn nếu distractor khó
