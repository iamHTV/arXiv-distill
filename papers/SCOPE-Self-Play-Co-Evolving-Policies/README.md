# [2605.31433v1] SCOPE: Self-Play qua Chính sách Đồng tiến hóa cho Tác vụ Mở

## Vấn đề
Self-play (tự chơi) có thể train language models mà không cần external supervision (giám sát bên ngoài). Nhưng existing methods require rule-checkable answers (câu trả lời có thể kiểm tra bằng quy tắc), leaving open-ended tasks (tác vụ mở) dependent trên curated prompts (prompt được tuyển chọn) hoặc frontier-model judges (mô hình đánh giá tiên tiến). Prior work chưa có data-free self-play framework cho open-ended tasks.

## Đóng góp
1. **SCOPE framework**: Data-free self-play cho open-ended tasks. Co-evolves (đồng tiến hóa) 2 policies: Challenger (tạo document-grounded tasks) và Solver (trả lời qua multi-turn retrieval)
2. **Self-judge với rubrics**: Frozen copy của initial model làm self-judge, viết task-specific rubrics từ source document, grade Solver responses
3. **Results**: +10.4 points trên 8 benchmarks, match/exceed GRPO_data trên ~9K curated prompts. Also improves held-out short-form QA +13.8 points

## Phương pháp (tóm tắt cốt lõi)
SCOPE: (1) Challenger generates document-grounded tasks từ source documents; (2) Solver answers tasks qua multi-turn retrieval; (3) Frozen self-judge writes task-specific rubrics từ source document, grades Solver responses against rubrics; (4) Co-evolve: update Challenger based on Solver performance, keep tasks near Solver's frontier. Quality gates filter ill-formed tasks. Iterative: 3 iterations improve progressively.

## Kết quả chính
- Qwen2.5-7B: baseline 24.4 → SCOPE iter3 34.9 (+10.5 points)
- GRPO_data (9K curated): 33.4 → SCOPE iter3 34.9 (match/exceed)
- Qwen3-8B: +10.4 points improvement
- OLMo-3: +5.4 points
- Held-out short-form QA: +13.8 points improvement (transfer beyond training domain)
- Co-evolution necessary: frozen Challenger fails to propose learning-value tasks
- Rubric generation quality is bottleneck, not grading capacity

## Insight có thể áp dụng ngay
1. **Data-free self-play cho open-ended tasks**: Khi không có curated training data, dùng self-play với co-evolving policies. Challenger generates tasks, Solver answers, self-judge evaluates. Ví dụ: train AI customer service — Challenger generates customer questions từ product docs, Solver answers, self-judge evaluates quality.

2. **Rubrics từ source documents**: Self-judge viết rubrics từ source documents — task-specific, grounded. Không cần human-written rubrics. Ví dụ: khi train AI report writer, self-judge creates rubrics từ source data: "Does response include Q3 revenue? Does response cite source?"

3. **Co-evolution là necessary**: Frozen Challenger không adapt → tasks không có learning value. Phải update Challenger based on Solver performance. Ví dụ: khi train AI tutor, nếu student improves → increase task difficulty. Frozen difficulty = no learning.

## Giả định & Hạn chế
**Điều kiện để method work:**
- Source documents available cho task generation
- Models 7-8B — larger scale unclear
- Multi-stage pipeline cần more compute than single-stage GRPO

**Hạn chế paper thừa nhận:**
- Compute overhead: multi-stage pipeline > single-stage GRPO
- Limited to 7-8B models — larger scales untested
- Self-play targets post-data regime

**Hạn chế paper KHÔNG nói:**
- Rubric generation quality bottleneck — nhưng không propose solution
- Content safety risk: Challenger may generate harmful tasks
- 3 iterations arbitrary — optimal iteration count unclear
- Không address domain transfer deeply
- Quality gates don't screen harmful content explicitly

## Metadata
- Năm: 2026
- Tác giả: Wai-Chung Kwan, Aryo Pradipta Gema, Joshua Ong Jun Leang, Pasquale Minervini
- Category: cs.CL
- Link PDF: https://arxiv.org/pdf/2605.31433v1
- Citation count: [EXTRACTION FAILED]
