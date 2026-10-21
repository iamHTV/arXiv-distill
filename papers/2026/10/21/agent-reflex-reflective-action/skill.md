# Skill: Huấn luyện agent phản xạ chủ động (Agent-Reflex 3 stages)
Source: 2610.17953
Type: framework

## Khi nào dùng skill này
- Agent dùng tool (MCP) trong môi trường thực: tool trả lỗi nhiễu, user sửa giữa chừng.
- Cần agent tự recovery (phục hồi) thay vì phụ thuộc prompt critique lúc inference (suy luận).
- KHÔNG dùng cho agent single-turn đơn giản, ít tool, môi trường sạch.

## Input cần có
- Environment scaling pipeline (pipeline mở rộng môi trường) cho agent domain.
- Capability-diverse LLM pool (bộ LLM đa dạng năng lực) để mine pairs.
- Log error returns (lỗi trả về) thực tế để phân loại tool-error families.

## Các bước thực hiện
1. Stage 1 — RSD: inject grounded tool-feedback perturbations vào environment scaling; sample LLM pool; mine matched success–failure pairs; summarize reusable reflection meta-skills (1 skill mỗi error family).
2. Stage 2 — ReSFT: chuyển mỗi skill thành supervision cho 3 hành vi: self-reflection (tự phản xạ), skill recovery (phục hồi kỹ năng), user-centric correction (sửa lỗi hướng user); fine-tune backbone.
3. Stage 3 — ORPO: agentic RL under noisy interactions + reflection-guided on-policy distillation từ meta-skills; train ~100 RL steps, theo dõi training dynamics (động lực học) ổn định.
4. Đánh giá: clean benchmarks + noisy benchmark (AgentNoiseBench-style: tool noise + user noise) — cả hai phải cải thiện.

## Output mong đợi
- Agent backbone 8B đạt overall cao hơn baseline reflection/environment-scaling; robust với noise (Agent-Reflex: 58.6 long-horizon overall, 29.1 AgentNoiseBench vs 25.9 NoisyAgent-8B).

## Ví dụ áp dụng
- Agent hỗ trợ khách hàng dùng 3 MCP tool: mine 24K error returns → 8 error families (timeout, auth expired, schema mismatch...) → 8 recovery skills → ReSFT + ORPO → agent tự retry với parameter đúng khi tool timeout thay vì hỏi user.

## Gotchas
- Perturbation phải grounded (có căn cứ) — nhiễu vô nghĩa sinh skill vô dụng.
- Success–failure pairs phải matched (khớp) cùng task, khác outcome — khác task thì skill không transfer.
- ORPO tốn compute hơn SFT — bắt đầu với ReSFT nếu budget hạn chế, thêm ORPO sau.
