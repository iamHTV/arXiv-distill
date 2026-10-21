# 2610.17953 Agent-Reflex: Dạy language agent hành động có phản xạ (reflective)

## Problem
- LLM đã thành interactive agent (tác nhân tương tác) long-horizon (tầm nhìn xa), nhưng deployment (triển khai) thực tế: MCP tool service trả noisy feedback (phản hồi nhiễu), user can thiệp sửa agent bất kỳ lúc nào — existing methods (phương pháp hiện có) thiếu supervision (giám sát) cho reflection learning (học phản xạ) và failure recovery (phục hồi thất bại).
- Môi trường hiện tại giả định clean feedback (phản hồi sạch); GPT-5.2 và Claude-4.5-Sonnet suy giảm rõ rệt dưới user/tool noise (nhiễu).

## Contribution
- Agent-Reflex: training framework (khung huấn luyện) chung incentivizing (khuyến khích) proactive reflection (phản xạ chủ động) trong agent, 3 stages (giai đoạn).
- Stage 1 — RSD (Environment Reflection Skill Discovery — khám phá kỹ năng phản xạ môi trường): inject grounded tool-feedback perturbations (nhiễu loạn phản hồi tool có căn cứ) vào environment scaling (mở rộng môi trường), sample capability-diverse LLM pool (bộ LLM đa dạng năng lực), mine matched success–failure pairs (cặp thành công–thất bại khớp), summarize reusable reflection meta-skills (siêu kỹ năng phản xạ tái dùng).
- Stage 2 — ReSFT (Reflective Supervised Fine-Tuning — tinh chỉnh có giám sát phản xạ): mỗi skill thành supervision cho self-reflection (tự phản xạ), skill recovery (phục hồi kỹ năng), user-centric correction (sửa lỗi hướng user).
- Stage 3 — ORPO (On-Policy Reflective Policy Optimization — tối ưu hóa chính sách phản xạ on-policy): agentic reinforcement learning (học tăng cường tác nhân) dưới noisy interactions + reflection-guided on-policy distillation (chưng cất on-policy hướng phản xạ).

## Method
- Dữ liệu: 8 tool-error families (họ lỗi tool) mined từ 24,510 real error returns (lỗi trả về thực).
- Backbone: Qwen3-8B; evaluation: MCP format chuẩn, official metric mỗi benchmark.
- ORPO kết hợp RL under noise với distillation từ reflection meta-skills — skill tóm tắt từ failure thật transfer tốt hơn experience ước lượng từ rollouts.

## Key Findings
- 5 long-horizon tool-use benchmarks (BFCL-v4, ACEBench, ToolSandbox 200 tasks, τ²-Bench, VitaBench): overall 58.6 — cao nhất among strong baselines.
- VitaBench: 17.5% vs Reflexion-8B 6.8%. ACEBench: 78.0% vs NoisyAgent-8B 52.0%; turn-level 73.3% trong khi baseline vẫn 85.0% step-level → gain đến từ multi-turn interaction.
- τ²-Bench: 62.1% vs EnvScaler-8B 54.6%.
- AgentNoiseBench (noisy interaction): overall 29.1% vs NoisyAgent-8B 25.9% — cao nhất among 8B methods; clean foundation models: GPT-5.2 81.0/61.0, Claude-4.5-Sonnet 73.0/57.0, Gemini-2.5-Pro 60.0/37.0, Qwen3-8B 26.2/14.1 (τ²/Vita).
- ORPO giữ ưu thế ổn định hơn GRPO, DAPO, REINFORCE++, SEED, noisy Agent RL qua 100 RL steps trên BFCL-v4, τ²-Bench, real interaction noise.
- Bảng noise chi tiết: extraction partial (pdfminer mangled) — chỉ dùng số prose-verified.

## Actionable Insights
1. Dạy recovery behavior, không chỉ đưa advice lúc inference. Ví dụ: thay vì bảo agent "hãy kiểm tra lại khi tool lỗi" trong prompt, fine-tune trên các cặp success–failure thật → agent tự sửa lỗi mà không cần critique text.
2. Tóm tắt meta-skill từ failure thật, tái dùng跨 task. Ví dụ: log 8 họ lỗi tool (timeout, schema mismatch, permission denied...) → viết 8 recovery skill → train agent dùng chúng.
3. RL under noise > RL clean. Ví dụ: khi train agent hỗ trợ khách hàng, inject nhiễu tool/user từ đầu — agent robust hơn là train clean rồi deploy vào môi trường nhiễu.

## Assumptions & Limitations
- Cần mined success–failure pairs từ environment scaling — phụ thuộc chất lượng perturbation grounded.
- ORPO cần on-policy distillation — tốn compute (tính toán) hơn SFT thuần.
- Benchmark tool-use domain; generalization sang domain khác chưa chứng minh.
- ACEBench gain chủ yếu multi-turn — single-turn gain nhỏ.

## Metadata
- Năm 2026; tác giả: Guanting Dong, Xinyu Yang, Jiajie Jin, Yuyang Hu, Xiaoshuai Song, Yifei Chen, Xiaoxi Li, Jiejun Tan, Yutao Zhu, Ji-Rong Wen, Zhicheng Dou (Gaoling School of AI, Renmin University of China), Tat-Seng Chua (NUS); code: https://github.com/RUC-NLPIR/Agent-Reflex; models & data: HuggingFace collection dongguanting/agent-reflex; category: cs.CL; PDF: https://arxiv.org/pdf/2610.17953; citation count: [NO DATA — paper 2026-10-13]
