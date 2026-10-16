# 2610.09593 — Structured Pre-generation Elicitation vs Single-shot Prompting in AI-assisted Enterprise Decision-making

## Problem
- "Cognitive surrender (đầu hàng nhận thức)": user delegate cả production lẫn evaluation cho AI → chấp nhận output yếu, không engage với reasoning. Prior intervention (unassisted practice, slow adoption) nằm NGOÀI working task — không sửa được interaction itself.

## Contribution
- RCT đầu tiên test metacognitive scaffolding (lớp hỗ trợ siêu nhận thức) tích hợp TRONG task: trước khi AI generate, user trả lời clarifying questions, chọn strategic direction, giải thích lý do
- Cognistance (prototype, Oxford Centre for Impact Research): 3 clarification questions + scaffold cards + free-text rationale → synthesis step

## Method
- RCT trên Prolific: 400 sessions (196 control / 204 treatment), task mô phỏng enterprise data-sovereignty crisis (Apex Global, launch Singapore/Malaysia, regulator yêu cầu server nội địa, kiến trúc tập trung Frankfurt). Control: single prompt → Gemini 3 1 Pro tạo action plan. Treatment: scaffold 3 bước trên.
- Deliverable chấm 4 dimension (1–10, tổng 4–40): strategic coherence, technical/regulatory specificity, trade-off articulation, information density. Raters: ChatGPT 6.1, Claude Sonnet 5.5, 1 human — blind với condition.

## Key Findings
- Composite quality +32.2% (15.48→20.48; +4.99, 95% CI [4.03,5.96], d=1.02); cùng hướng mọi rater (ChatGPT +7.19, human +9.15, Claude +2.79).
- Gain tập trung: trade-off articulation +1.90 (d=1.57), strategic coherence +1.94 (d=1.28), information density +0.89; technical specificity KHÔNG cải thiện (+0.26, p=.300).
- Cứu weak prompt: floor-scored (off-task) deliverable 34.2%→4.9% (~59% aggregate effect). Nhóm prompt đã nêu vấn đề vẫn +20.9% (d=1.15).
- Involvement d=0.59, effort d=0.36, thời gian +2.4 phút (10.46 phút). Self-rating quality không track rated quality cả hai condition.

## Actionable Insights
- Elicit trước khi generate: 3 câu hỏi (ưu tiên vận hành, infra, audience) + chọn posture + viết rationale trước khi AI viết — áp dụng ngay cho mọi workflow content/strategy: đừng single-shot prompt, chèn 1 bước structured elicitation.
- Scaffold cứu prompt yếu nhưng vẫn giúp prompt tốt (+20.9%) — không chỉ dành cho user yếu; trade-off articulation là dimension được cải thiện nhiều nhất.
- Đừng tin self-rating: user tự đánh giá quality không tương quan rated quality — cần rubric客观 + rater blind, không hỏi user "thấy hay không".

## Assumptions & Limitations
- So sánh whole workflow — không tách được component nào đóng góp; không có unaided arm / AI-alone arm / faulty-output trial.
- Rubric domain-specific, do study team viết, đặt tên split architecture làm example (trùng scaffold option) — có mechanical bias.
- Immediate recall only (không robust với sensitivity); Prolific professionals, task mô phỏng; 165/204 treatment chọn cùng posture → output diversity hẹp lại.

## Metadata
- 2026, William Scott-Jackson (Oxford Centre for Impact Research), cs.HC/cs.AI, working paper, https://arxiv.org/pdf/2610.09593
