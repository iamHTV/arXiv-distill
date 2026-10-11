# 2602.01011 Multi-Agent Teams Hold Experts Back

## Problem

Multi-agent LLM systems được deploy ngày càng nhiều như autonomous collaborators (cộng tác viên tự chủ), trong đó agents tương tác tự do thay vì execute fixed workflows (luồng công việc cố định). Prior work enforce coordination (ép buộc phối hợp) thông qua fixed roles, workflows, hoặc aggregation rules (quy tắc tổng hợp). Nhưng câu hỏi chưa được trả lời: self-organizing teams (nhóm tự tổ chức) perform thế nào khi coordination không constrained? Đặc biệt, liệu LLM teams có achieve strong synergy (cộng hưởng mạnh) — nơi team performance match hoặc exceed best individual member?

## Contribution

1. Discovery: LLM multi-agent teams CONSISTENTLY FAIL to match expert agent performance — ngay cả khi explicitly told who the expert is. Performance losses lên đến 41.1% trên ML benchmarks. Đây là counter-intuitive finding vì human teams match expert performance khi expertise revealed.
2. Identify primary bottleneck: expert LEVERAGING (tận dụng chuyên gia), not identification (nhận diện). Teams identify correctly nhưng fail to defer appropriately.
3. Discover "integrative compromise" behavior — LLM teams average expert và non-expert views rather than appropriately weighting expertise. Behavior này worsen với team size và correlate negatively với performance.
4. Trade-off revelation: consensus-seeking behavior improves robustness (khả năng chống chịu) to adversarial agents, suggesting trade-off giữa alignment và expertise utilization.

## Method (tóm tắt cốt lõi)

Study 2 tiers: (1) Human psychology tasks (Lost at Sea, NASA Moon Survival, Student Body President) với controlled expertise distribution — concentrated (1 expert) và distributed (multiple experts); (2) Frontier ML benchmarks với real model differences (Claude Opus 4/4.5, GPT-5, o3-mini, etc.) trên task-specific teams. 4 information conditions: No Information (control), Expert Not Mentioned, Reveal Expert, Best Individual (single expert baseline). Decompose gap thành Identification Gap (nhận diện) và Expertise Leveraging Gap (tận dụng). Conversational analysis để identify behavioral patterns. 10-30 seeds per cell.

## Key Findings

- LLM teams underperform best individual by 6.3%-41.1% across all tasks, even when expert is revealed
- Expert Leveraging Gap >> Identification Gap — bottleneck là TẬN DỤNG, không phải NHẬN DIỆN
- Integrative compromise: teams average expert + non-expert views, KHÔNG defer to expert
- This behavior worsens with team size (more agents → more compromise → worse performance)
- Contrast với human teams: humans match expert performance once expertise revealed
- Trade-off: consensus-seeking IMPROVES robustness to adversarial agents (adversarial agents can't easily sway team)
- Teams consistently achieve "weak synergy" (match average member) but NOT "strong synergy" (match best member)
- Robust across: concentrated expertise, distributed expertise, multiple model combinations

## Actionable Insights

1. KHÔNG assume multi-agent system sẽ tốt hơn single expert model — trong hầu hết cases, deploy 1 strong model tốt hơn deploy team of models. Ví dụ: medical diagnosis system — 1 Claude Opus 4.5 perform tốt hơn team 4 models vì team sẽ average expert opinion với weaker opinions.
2. Nếu PHẢI dùng multi-agent, implement expertise-aware coordination mechanism (cơ chế phối hợp nhận thức chuyên môn) — không để agents tự negotiate. Ví dụ: hardcode expert model có final decision authority (quyền quyết định cuối), agents khác chỉ contribute information, KHÔNG vote on final answer.
3. Consensus-seeking behavior có thể là feature cho adversarial robustness — nếu deployment environment có adversarial inputs (spam, jailbreak), multi-agent consensus natural resist manipulation. Ví dụ: content moderation system — team of 3 models harder to jailbreak than single model.

## Assumptions & Limitations

- Giả sử: evaluation metrics (L1 distance, accuracy) capture real performance differences
- Limitation: Study chủ yếu trên reasoning/knowledge tasks, chưa test trên creative/generation tasks
- Limitation: Fixed team size experiments (2-4 agents), chưa test larger scales
- Limitation: No training interventions — chỉ observe behavior, không propose fix
- Limitation (tự thấy): "Integrative compromise" có thể là artifact của RLHF training — models trained to be balanced/fair naturally average views. Different training (e.g., expert delegation training) có thể change behavior.

## Metadata

- Năm: 2026
- Tác giả: Aneesh Pappu, Batu El, Hancheng Cao, Carmelo di Nolfo, Yanchao Sun, Meng Cao, James Zou
- Institution: Stanford (Knight-Hennessy Scholars)
- Category: cs.AI, cs.CL, cs.MA
- Link PDF: https://arxiv.org/pdf/2602.01011
- Citation count: N/A
- Nhãn: [applied]
- Skill: N/A — observational study, no actionable workflow (cautionary finding)
