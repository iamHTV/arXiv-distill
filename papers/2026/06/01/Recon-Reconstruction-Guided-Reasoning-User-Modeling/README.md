# [2605.26969v1] Reconstruction-Guided Reasoning Synthesis cho User Modeling (Mô hình hóa Người dùng)

## Vấn đề
User modeling (mô hình hóa người dùng) dùng language models để mimic (bắt chước) hành vi cá nhân từ corpus (kho ngữ liệu) context-action pairs (cặp ngữ cảnh-hành động). Recent approaches augment (tăng cường) corpus với synthesized reasoning traces (dấu vết suy luận tổng hợp), nhưng conditioning trên cả context và action constitutes (tạo thành) post-hoc rationalization (hợp lý hóa hậu kỳ) thay vì reasoning — trace guaranteed (đảm bảo) justify action nhưng có thể không encode (mã hóa) underlying latent causal decision paths (con đường quyết định nhân ẩn bên dưới).

## Đóng góp
1. **Recon framework**: Dùng action reconstruction (tái tạo hành động) để score reasoning traces theo predictive power (sức mạnh dự đoán). Given context + candidate reasoning → reconstruction model predicts action → reconstruction fidelity (độ trung thực tái tạo) determines reasoning quality
2. **Recon-Select**: Select reasoning traces không cần training — 54.7% win rate over Backward Synthesis baseline
3. **Recon-GRPO**: Train reasoning synthesis model với rewards từ Recon — up to 70.0% win rate. Reasoning transfers across models

## Phương pháp (tóm tắt cốt lõi)
Pipeline 3 bước: (1) Sample N=4 candidate reasoning traces từ reasoning model M_r, conditioned on context-action pair; (2) Reconstruction model M_a predicts action từ context + candidate reasoning; (3) Score reasoning bằng alignment giữa predicted action và ground-truth action. Recon-Select: chọn reasoning trace có highest reconstruction score. Recon-GRPO: dùng reconstruction score làm reward signal cho GRPO training của reasoning synthesis model. Key insight: useful reasoning phải naturally elicit (gợi ra tự nhiên) action từ context, không chỉ justify observed action.

## Kết quả chính
- Recon-Select (Qwen3-8B): 54.7% win rate over Backward Synthesis
- Recon-Select (GPT-5-mini): 53.5% win rate
- Recon-GRPO: up to 70.0% win rate over baselines
- E2E-GRPO (optimize action accuracy only): 38.4% win rate — worse than baseline
- Consistent improvements across 4 domains, 8 individuals
- Recon-synthesized reasoning transfers across models
- Human validation: 77% agreement với LM judge, Cohen's kappa 0.623

## Insight có thể áp dụng ngay
1. **Post-hoc rationalization ≠ reasoning**: Khi generate reasoning traces cho AI agents, KHÔNG chỉ justify observed actions. Reasoning phải có predictive power — có thể predict action từ context. Ví dụ: khi train AI mimic customer behavior, reasoning "customer bought because they liked the color" là rationalization. Useful reasoning: "customer typically buys items matching their style preference, và color X matches → predict purchase."

2. **Reconstruction fidelity = reasoning quality metric**: Dùng reconstruction để evaluate reasoning quality. Given context + reasoning → predict action → nếu predict đúng → reasoning có quality. Ví dụ: khi evaluate AI advisor's reasoning, test: cho context + reasoning → có predict được user's decision không? Nếu không → reasoning không có causal power.

3. **Reasoning quality > action accuracy**: Optimize cho action accuracy alone (E2E-GRPO) produces WORSE reasoning (38.4% win rate). Phải optimize cho reasoning quality qua reconstruction. Ví dụ: khi train AI sales agent, don't just optimize conversion rate — optimize reasoning quality bằng cách test: reasoning có predict customer behavior không?

## Giả định & Hạn chế
**Điều kiện để method work:**
- Cần corpus context-action pairs từ target user
- Reconstruction model phải capable enough để predict actions
- Reasoning traces phải conditioned on ground-truth action (limitation acknowledged)

**Hạn chế paper thừa nhận:**
- Chỉ evaluate trong user simulation setting — 8 individuals, 4 domains
- Recon-GRPO limited to single domain
- Additional computational cost: Recon-Select needs 2N+1 LM calls
- Still operates on rationalizations conditioned on ground-truth action

**Hạn chế paper KHÔNG nói:**
- 8 individuals quá ít cho generalization claims
- 4 domains specific — không test trên diverse user types
- LM judge bias — Gemini-3.1-Flash-Lite có systematic preferences
- Không test với very large models (>70B)
- Reconstruction model quality limits upper bound
- Không address privacy implications của user behavior modeling

## Metadata
- Năm: 2026
- Tác giả: Alan Zhu, Mihran Miroyan, Carolyn Wang, Andrew Zhou, Lisa Dunlap, Narges Norouzi, Joseph E. Gonzalez
- Category: cs.CL, cs.AI
- Link PDF: https://arxiv.org/pdf/2605.26969v1
- Citation count: [EXTRACTION FAILED]
