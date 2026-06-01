# [2605.31408v1] Skill Availability and Presentation Granularity trong LLM Agents

## Vấn đề
Skill documents (tài liệu kỹ năng) cung cấp procedural knowledge (tri thức quy trình) cho LLM agents tại inference time (thời gian suy luận). Nhưng prior work chưa rõ: presentation granularity (độ chi tiết trình bày) của skill knowledge có thay đổi downstream task success (thành công tác vụ hạ nguồn) không? Cụ thể: low-abstraction checklist (danh sách kiểm tra mức thấp) vs high-abstraction principles (nguyên tắc mức cao) — cái nào tốt hơn?

## Đóng góp
1. **Skill availability là signal mạnh nhất**: So với no skill, skill conditions tăng task-mean pass rate +26.7-36.0 pp (GPT-5.5) và +18.0-26.0 pp (DeepSeek V4-Flash)
2. **Presentation granularity effects nhỏ và uncertain**: Low-abstraction vs high-abstraction: +0.7 pp (GPT-5.5), -6.7 pp (DeepSeek) — cả hai 95% CIs cross zero
3. **Worked examples effect nhỏ**: Thêm 1 worked example: +0.7-1.3 pp — quá nhỏ cho design rule

## Phương pháp (tóm tắt cốt lõi)
Controlled experiment trên SkillsBench: 30 oracle-validated tasks, 2 model configs (GPT-5.5, DeepSeek V4-Flash), 6 skill conditions (no skill, low/medium/high abstraction, with/without worked examples), 5 trials per cell. 1,800 rows total. Paired contrasts estimated over 30 tasks. Bootstrap confidence intervals.

## Kết quả chính
- Skill availability: +26.7-36.0 pp (GPT-5.5), +18.0-26.0 pp (DeepSeek) — largest signal
- Low vs high abstraction: +0.7 pp (GPT-5.5), -6.7 pp (DeepSeek) — both CIs cross zero
- Worked examples: +0.7-1.3 pp — small, directional stable
- Mean-reward robustness checks preserve same conclusion
- DeepSeek with thinking mode: low-level instructions may duplicate/constrain planning

## Insight có thể áp dụng ngay
1. **Skill availability > presentation format**: Khi build AI agents, ưu tiên CÓ skill documents hơn là optimize format. Có skill tốt hơn không có skill, regardless of presentation. Ví dụ: khi deploy customer service agent, việc có procedural knowledge về products/processes quan trọng hơn cách trình bày (checklist vs principles).

2. **Don't over-optimize presentation granularity**: Low-abstraction vs high-abstraction không có reliable advantage. Chọn format nào tiện, không cần invest quá nhiều vào presentation optimization. Ví dụ: khi viết skill documents cho AI agents, dùng format tự nhiên — không cần convert tất cả thành checklists hoặc principles.

3. **Worked examples có small positive effect**: Thêm 1 worked example có thể help (+0.7-1.3 pp) nhưng effect nhỏ. Include khi tiện, không phải priority. Ví dụ: khi write documentation cho AI coding assistant, thêm 1-2 examples — help nhẹ nhưng không phải game-changer.

## Giả định & Hạn chế
**Điều kiện để experiment work:**
- 30 oracle-validated tasks — subset-specific
- 5 trials per cell — limited samples
- 2 model configs — limited generalizability

**Hạn chế paper thừa nhận:**
- Subset-specific magnitude — SkillsBench headline average khác
- Model versions, harness settings differ
- Source of larger magnitude unresolved

**Hạn chế paper KHÔNG nói:**
- 30 tasks quá ít cho robust conclusions
- Chỉ 2 models — generalizability unclear
- Không test domain-specific skills
- Không explore example number, length, similarity variations
- Reasoning mode effect hypothesis only — not tested

## Metadata
- Năm: 2026
- Tác giả: Xiaonan Xu, Wenjing Wu
- Category: cs.CL, cs.AI, cs.LG
- Link PDF: https://arxiv.org/pdf/2605.31408v1
- Citation count: [EXTRACTION FAILED]
