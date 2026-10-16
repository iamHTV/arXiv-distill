# Skill: Pre-generation Elicitation Scaffold
Source: 2610.09593
Type: prompt-pattern (metacognitive scaffolding layer cho AI-assisted decision workflow)

## Khi nào dùng skill này
- Dùng AI tạo deliverable chiến lược/decision (action plan, strategy doc, analysis) mà quality phụ thuộc vào context user biết nhưng prompt thường thiếu
- Lo ngại cognitive surrender (user nhận output yếu vì không đánh giá) — cần giữ user engage với reasoning
- KHÔNG nên dùng: task sự vụ đơn giản, factual lookup, hoặc khi user đã là expert viết prompt đầy đủ (vẫn được +20.9% nhưng cost-benefit thấp hơn)

## Input cần có
- Task description (scenario, constraint, deadline)
- 3 clarification dimensions phù hợp domain (paper dùng: operational priority, infrastructure, primary audience)
- 2–4 strategic posture options (scaffold cards) cho task — có ví dụ cụ thể, không trùng một đáp án "đúng" duy nhất
- AI generator (paper dùng Gemini 3 1 Pro)

## Các bước thực hiện
1. User viết prompt ban đầu (giữ nguyên — baseline cho mọi arm).
2. Hỏi 3 câu clarification: operational priority (ưu tiên vận hành), context/infrastructure, primary audience — mỗi câu 1 lựa chọn.
3. Hiển thị scaffold cards: user chọn 1 strategic posture (e.g., decisive split-system vs cautious phased rollout).
4. User viết free-text rationale giải thích tại sao chọn posture đó (bước này giữ user engage với reasoning).
5. Synthesis step: truyền prompt + 3 câu trả lời + posture + rationale vào generator; AI tạo deliverable từ đầy đủ input đó.
6. Đánh giá output bằng rubric 4 dimension (strategic coherence, trade-off articulation, information density, technical specificity) với rater blind condition; theo dõi floor-scored rate (off-task).

## Output mong đợi
- Deliverable quality +~32% composite (d=1.02), gain lớn ở trade-off articulation + strategic coherence; off-task output giảm 34%→5%; cost +2.4 phút/user.

## Ví dụ áp dụng
- Content strategy: trước khi AI viết brief campaign, hỏi priority (awareness/conversion), channel context, audience; chọn posture (aggressive vs conservative tone); viết rationale → brief sâu hơn, ít off-task.

## Gotchas
- Technical/regulatory specificity KHÔNG cải thiện (p=.300) — scaffold không thay thế domain expertise; vẫn cần review chuyên môn.
- ~59% effect đến từ việc cứu prompt yếu — nhưng nhóm prompt tốt vẫn được +20.9%, nên vẫn nên chạy cho mọi user.
- Self-rating không đáng tin: user tự đánh giá không track quality thật — dùng rubric客观, đừng hỏi "bạn thấy thế nào".
- Diversity hẹp: 165/204 chọn cùng posture — randomize thứ tự cards, thêm option để tránh hội tụ.
- Rubric phải trung lập với option (paper bị bias vì rubric đặt tên split architecture làm ví dụ).
