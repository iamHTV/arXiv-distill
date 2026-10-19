# [2610.21411v2] Jev-LiteMAS: Separating Decisions from Generation in Multi-Agent Workflows

## Problem
- Prior work (MetaGPT, AgentNet, LAS) dùng generative LLM (mô hình sinh văn bản) cho MỌI operation (thao tác) trong multi-agent workflow (quy trình đa tác nhân), kể cả routing (chọn chuyên gia tiếp theo) và review (đánh giá artifact — sản phẩm trung gian) – những thao tác chỉ cần bounded decision (quyết định có giới hạn, ví dụ: chọn 1 expert ID hoặc pass/escalate).
- Profiling (phân tích hiệu suất) 3 framework MAS đại diện (MetaGPT, AgentNet, LAS) trên backbone (nền mô hình) DeepSeek-V4-Flash: routing + review chiếm 31,7–43,5% tổng token generative-LLM, share latency (độ trễ) 29,5–46,1%. Riêng LAS: 40,4% (MATH) và 39,2% (MBPP+). Chưa ai giải quyết 2 interface gap (lỗ hổng giao diện) khi thay bằng decision model (mô hình quyết định) rẻ: planning gap (không tạo plan + handoff instruction) và review gap (không tạo corrective feedback – phản hồi sửa lỗi).

## Contribution
- Nguyên tắc capability-matched allocation (phân bổ năng lực theo yêu cầu output): operation cần sinh văn bản mở → generative model; operation chỉ cần chọn/cảm verdict → choice-based decision model (Jev).
- Jev-LiteMAS: (a) feedback-driven expert handoffs (bàn giao chuyên gia theo phản hồi) – Jev chọn expert tiếp theo từ task + artifact mới nhất + danh sách action hợp lệ, KHÔNG cần pre-generated trajectory (quỹ đạo đã sinh sẵn); (b) Jev-gated LLM re-review (duyệt lại có cổng) – Jev sàng artifact theo rubric (tiêu chí): pass → chạy tiếp KHÔNG gọi LLM, escalate → LLM reviewer cho verdict + corrective feedback, expert sửa rồi re-enter.
- Triển khai trên AutoGen (khung agent), backbone DeepSeek-V4-Flash + GPT-5, decision model Jev, SLM baseline (mô hình ngôn ngữ nhỏ) Qwen3-1.7B-Instruct.

## Method (tóm tắt cốt lõi)
- State (trạng thái) chia sẻ 𝑠𝑡 chứa task, artifact trung gian, feedback; mỗi bước: expert 𝑒𝑡 sinh 𝑦𝑡 = 𝐺𝑒𝑡(𝑠𝑡−1), state update 𝑠𝑡 = 𝑈(𝑠𝑡−1, 𝑒𝑡, 𝑦𝑡).
- Routing: 𝑎𝑡 = 𝐽route(𝑠𝑡, 𝐴𝑡) ∈ 𝐴𝑡 (𝐴𝑡 = eligible experts ∪ {STOP}); dispatch expert tiếp theo nhận task + artifacts qua state.
- Review point: 𝑑𝑡 = 𝐽screen(𝑠𝑡) ∈ {pass, escalate}; nếu escalate: (𝑣𝑡, 𝑐𝑡) = 𝐺review(𝑠𝑡) (verdict + feedback); revision: state 𝑠𝑡 ⊕ (𝑣𝑡, 𝑐𝑡) → expert sửa → artifact mới được sàng lại như artifact mới.

## Key Findings
- 4 benchmark (tiêu chuẩn đánh giá): MATH (toán), MBPP+ (code), API-Bank (dùng tool), IDRBench I3 (tích hợp ý tưởng nghiên cứu liên ngành). 5 baseline: Single-Agent, MetaGPT, AFlow, AgentNet, LAS.
- vs LAS: token generative-LLM giảm 17,5–54,6% (DeepSeek-V4-Flash) và 12,7–38,6% (GPT-5); accuracy chênh −0,67 đến +0,66 điểm phần trăm (DeepSeek), −1,34 đến +0,67 (GPT-5); latency thấp hơn 7/8 cấu hình, giảm mạnh nhất IDRBench I3 DeepSeek −45,8%, API-Bank GPT-5 −50,2% (ngoại lệ GPT-5 MATH: 30,04s vs 25,91s).
- DeepSeek: accuracy MBPP+ cao nhất 85,33%; GPT-5 IDRBench I3 +0,67 điểm so với LAS. MetaGPT cao hơn trên IDRBench I3 DeepSeek (82,67% vs 75,33%) nhưng tốn token + API calls nhiều hơn đáng kể.
- Ablation (loại bỏ thành phần): Jev Router vs LLM Router: +6,66/+0,67 điểm accuracy, token −63,1%/−36,0%; vs SLM Router (Qwen3-1.7B): +11,33/+4,94 điểm, token −24,3%/−16,1%; bỏ semantic feedback (phản hồi ngữ nghĩa): accuracy 75,33→57,33% (I3), 66,29→57,30% (API-Bank) — routing grounded trong substantive outputs (output có nội dung thật) ngăn mất đến 18,0 điểm accuracy.
- Robustness (tiêm lỗi vào artifact 1 expert ngẫu nhiên, DeepSeek): Attack-MAS accuracy 46,67%/39,33%, ASR (tỷ lệ tấn công thành công) 50,00%/48,67%; Jev-LiteMAS: 94,00%/84,67%, ASR 3,33%/4,00%; vs MAS-Shield +2,67/+6,00 điểm, token −11,2%/−14,0%; vs Jev-LLM Judge accuracy tương đương, latency −24,3%/−23,5%; Multi-agent Debate (tranh luận đa tác nhân) accuracy/ASR tốt nhất nhưng tốn tài nguyên nhiều nhất.
- Screening gate (cổng sàng lọc): Jev TPR (tỷ lệ phát hiện đúng lỗi) 95,33% (MATH) / 91,33% (MBPP+) gần LLM judge 96,67%/92,00%, trong khi SLM judge chỉ 61,33%/44,67%; SLM FPR (tỷ lệ báo giả) thấp hơn (0,00%/0,67%) nhưng Detection kém — ít báo giả ≠ phát hiện đáng tin; Jev clean-case token −29,4%/−24,2%, latency −37,6%/−28,0%.
- Overhead (chi phí phụ) decision layer: Jev thêm chỉ 1,13–2,21 giây/eval unit, chiếm 2,92–6,85% latency E2E và 1,56–2,14% chi phí model; tổng latency 30,04–75,57s, chi phí $0,00664–$0,01766/eval unit (GPT-5 experts).

## Actionable Insights
- Đo share token của routing/review trong pipeline agent trước khi tối ưu: nếu >~30% (như profiling 31,7–43,5%), chuyển coordination sang decision model là khoản tiết kiệm lớn nhất → ví dụ: content pipeline writer→editor→SEO, thay "gọi LLM chọn bước tiếp" bằng classifier/routing model nhỏ.
- Dùng gated review thay vì review toàn bộ: sàng artifact bằng decision model theo rubric, chỉ escalate artifact nghi vấn sang LLM reviewer → ví dụ: kiểm tra draft blog bằng rule-based gate + LLM chỉ duyệt các draft không đạt rubric, cắt ~25–30% token review.
- Router PHẢI thấy substantive outputs của expert (artifact thật), không chỉ metadata: content-blind routing mất 18 điểm accuracy → ví dụ: khi build orchestrator (bộ điều phối), truyền tóm tắt artifact mới nhất vào prompt router, đừng chỉ truyền tên bước.

## Assumptions & Limitations
- Điều kiện: expert pool (tập chuyên gia) + legal actions phải được định nghĩa sẵn; artifact quality distribution (phân bố chất lượng artifact) phải nghiêng về "đạt" để gate tiết kiệm (nếu nhiều artifact phải sửa, savings giảm).
- Limitation paper thừa nhận: (1) không tạo expert mới / tái cấu hình role động cho task chưa thấy; (2) savings phụ thuộc phân bố chất lượng artifact — adaptive review policy (chính sách duyệt thích ứng) là hướng future work.
- Limitation paper KHÔNG nói: template artifact (CCS Concepts placeholder "Do Not Use This Code", running header "Trovato et al." không khớp tác giả thật Kaixiang Wang, Jiong Lou, Zhaojiacheng Zhou, Jie Li — Shanghai Jiao Tong University) → chất lượng trình bày sơ sài, cần đánh giá lại reproducibility (khả năng tái tạo); Jev là model riêng (arXiv 2609.37647) chưa rõ open weights (trọng số mở).

## Metadata
- Năm: 2026 (submitted 15 Oct 2026, v2 16 Oct 2026), authors: Kaixiang Wang, Jiong Lou, Zhaojiacheng Zhou, Jie Li (Shanghai Jiao Tong University)
- Category arXiv: cs.AI, link PDF: https://arxiv.org/pdf/2610.21411v2, license: CC BY 4.0
- Citation count: [NO DATA — paper <1 week old, Semantic Scholar rate-limited]
