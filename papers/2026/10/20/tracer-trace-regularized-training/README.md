# [2610.19133v1] TRACER: Trace-Regularized Training Against Indirect Prompt Injection

## Giá trị cốt lõi (1 câu)
Đào tạo đối kháng theo kênh (channel-aware adversarial training) cho mô hình chống間接 prompt injection: lấy mẫu kênh trưng bày (follow-up, retrieved document, tool output, agent message) trong quá trình huấn luyện, kết hợp phần thưởng gated bằng bằng chứng và ATRC trace regularization để giữ suy luận sạch khi bằng chứng được châm là không hợp lệ.

## Problem
Prior work chưa giải quyết được giả định rằng độ mạnh chống間接 prompt injection chuyển qua các kênh trưng bày — thực tế cùng một payload tấn công thành công 18% khi là tin nhắn tiếp theo nhưng 53% khi bọc dưới dạng retrieved context (RAG), và các phương án phòng thủ thường chỉ được huấn luyện và đánh giá trong một wrapper (một khung trình bày).

## Contribution
- Xác định và định lượng "khoảng cách khung trình bày" (framing gap): nội dung tấn công giống hệt trở nên thành công hơn nhiều khi trình bày qua kênh ngữ cảnh không tin cậy khác.
- Giới thiệu TRACER (Trace-Regularized Adversarial Channel Exposure with Reward-shaping): khung đào tạo đối kháng lấy mẫu kênh trong quá trình tối ưu, kết hợp phần thưởng hợp hợp (answer-anchored, evidence-gated composite reward) và ATRC (committed-span Adversarial Trace Recovery and Consistency) để giữ suy luận sạch khi bằng chứng châm không hợp lệ.
- Đánh giá xuyên khung trình bày (cross-framing evaluation): chuyển qua các wrapper là bất đối xứng, exposes trade-off độ sâu–độ rộng (depth–breadth trade-off) giữa độ mạnh trong kênh (native robustness) và khả năng tổng quát.

## Method
Mỗi tập huấn luyện là một trò chơi strong (three-turn robustness game): (1) mô hình nhận tác vụ sạch và tạo trace lý luận sạch (clean reasoning trace) + câu trả lời sạch; (2) cùng payload tấn công được hiển thị qua kênh được lấy mẫu (channel) thành dạng rendered; (3) mô hình tạo trace lý luận sau khi bị tấn công + câu trả lời sau khi bị tấn công. Kênh được lấy mẫu như một biến ngẫu nhiên trong mục tiêu huấn luyện (channel exposure). Phần thưởng sau khi tấn công (post-attack reward) là tổng hợp 5 thành phần: đáp án chính xác (ans), chất lượng quy trình (proc), giữ neo (anchor retention), khả năng sửa chứng cứ (evidence-gated corrigibility), và kiểm soát độ dài (length control), trọng số lần lượt 0.25, 0.25, 0.20, 0.20, 0.10. ATRC là trace regularizer: khi câu trả lời sạch đúng và bằng chứng châm không hợp lệ (cờ evidence gate active), ATRC căn chỉnh phân phối token sau khi tấn công về phân phối sạch qua KL divergence và phục hồi token sạch cam kết (committed-span token recovery). Mục tiêu tổng thể tối ưu bằng GRPO với KL regularization và ATRC regularization.

## KNOWLEDGE — Số liệu & khái niệm
- Cùng payload tấn công: ASR 18% (tin nhắn tiếp theo/follow-up) vs 53% (retrieved context/RAG) trên sáu mô hình trung gian chỉ huấn luyện theo kiểu follow-up (+35 pp).
- Base model authority gradient: prompt injection ASR từ 70% (follow-up casual) lên 92–96% (wrapper agent, tool, RAG).
- TRACER trên GSM8K với Qwen2.5-3B-Instruct: giảm RAG-framed ASR từ 65.5% xuống 6.1%, giữ clean accuracy 78–82%.
- RAG specialist: 6.1% ASR trên RAG nhưng 25.7% (tool) và 26.5% (agent) — đào tạo theo RAG học "độ sâu" trong kênh đó, chuyển kém sang tool/agent.
- Tool-output training: native ASR cao hơn (15.0%) nhưng gần như phẳng trên 4 khung trình bày (15.0–20.2%) — học "độ rộng".
- Multi-framing (RAG+tool) 3B: best average ASR 13.9%, cải thiện native RAG (5.2% vs 6.1%).
- 7B scaling: một epoch RAG training đạt 9.4% average ASR trên 4 khung trình bày; final 7B model 10.8% average ASR.
- Ablation mục tiêu: answer-only 21.3% ASR, composite reward 13.8%, full TRACER 6.1%.
- Held-out paraphrase: TRACER 10.0% ASR vs base 62.7%.
- Channel-aware escalation: TRACER 18.1%, defense-aware: 23.8%, baseline 68.8–70.0%.
- Mixed evidence: clean/evidence accuracy 81–83%, injection-induced flip rate từ 46.3–58.1% (base) xuống 13.8–17.5% (TRACER).
- Huấn luyện: 3 epochs, learning rate 2×10⁻⁶, batch size 1, gradient accumulation 8, group size 4, KL coefficient 0.10, ATRC weight 0.10, QLoRA 4-bit, vLLM rollouts.
- Reward weights: ans 0.25, proc 0.25, anc 0.20, corr 0.20, len 0.10.
- Các kênh (channels): {followup, rag, tool, agent}.
- Mã nguồn: https://github.com/Mishrakshitij/TRACER.git

## INSIGHT — Cơ chế & tại sao
[Cùng payload thành công 53% ở RAG vs 18% ở follow-up] VÌ [người dùng coi ngữ cảnh được truy xuất có thẩm quyền cao hơn (authority gradient) — định dạng văn bản mang ngầm uy lực mặc dù nội dung có thể không tin cậy]. Điều này nghĩa là [độ mạnh trong một wrapper không phải độ mạnh của nội dung tấn công; đánh giá trong một kênh bỏ lỡ rủi ro xuyên kênh].
[RAG specialist mạnh trong kênh RAG nhưng yếu tool/agent] VÌ [mô hình học nghiãn kênh-specific (channel-specific skepticism) chứ không phải channel-invariant robustness]. Điều này nghĩa là [đào tạo đa kênh giúp kháng chế chuyển được hơn, đặc biệt tại mô hình 3B].
[TRACER giữ clean accuracy 78–82% khi giảm ASR xuống 6.1%] VÌ [phần thưởng corrigibility là evidence-gated: khen mô hình khi giữ câu đúng dưới bằng chứng không hợp lệ, nhưng không khen khi từ chối bằng chứng hợp lệ]. Điều này nghĩa là [phòng thủ không phải từ chối toàn bộ ngữ cảnh bên ngoài, mà phân biệt bằng chứng hợp lệ và không hợp lệ].

## IDEA — Áp dụng được gì
Áp dụng TRACER vào hệ thống RAG của doanh nghiệp nhỏ: bước đầu là thu thập mẫu tấn công間接 prompt injection qua các kênh (tin nhắn tiếp theo, retrieved document, tool output, agent message), rồi huấn luyện đối kháng với kênh được lấy mẫu ngẫu nhiên và phần thưởng gated bằng bằng chứng.
Dùng đánh giá xuyên kênh (cross-channel evaluation) thay vì chỉ đánh giá trong một wrapper: bước đầu là kiểm tra mô hình đã chống injection với cùng payload nhưng bọc dưới dạng retrieved document, tool output, agent message.

## WISDOM — Nguyên tắc tổng quát
Nguyên tắc: Độ mạnh chống injection間接 phải được đào tạo và đánh giá theo kênh trưng bày (wrapper) mà không tin cậy sẽ đến mô hình trong thực tế; KHÔNG giả định độ mạnh trong một kênh chuyển sang kênh khác. Phòng thủ nên kết hợp đào tạo channel-aware với các betrieb runtime (retrieval filtering, tool-output parsing, monitoring, sandboxing).

## Assumptions & Limitations
- Điều kiện đúng: tấn công間接 prompt injection, mô hình nhận ngữ cảnh không tin cậy qua nhiều kênh, có sẵn clean trace làm neo (anchor).
- Limitation paper thừa nhận: tấn công chủ yếu là template-based, không bao quát các đối thủ tối ưu hóa (optimization-based) hoặc đa luân (multi-turn); toàn bộ TRACER training chỉ đánh giá trên Qwen2.5 tại 3B và 7B; TRACER là phòng thủ thời điểm huấn luyện (training-time), bổ sung cho các biện pháp runtime không phải thay thế.
- Limitation paper KHÔNG nói: chi phí vận hành hệ thống lấy mẫu kênh hàng ngày; tác động lên độ trễ suy luận khi kết hợp nhiều kênh; tính ổn định qua nhiều lần retraining khi catalog công cụ thay đổi.

## Metadata
- Năm: 2026
- Tác giả: Kshitij Mishra, Salem Lahlou, Nils Lukas (Mohamed bin Zayed University of Artificial Intelligence)
- Category arXiv: cs.LG
- Link PDF: https://arxiv.org/pdf/2610.19133v1
- arXiv ID: 2610.19133v1
- Nhãn: [applied]
- Skill: tracer-trace-regularized-training | Test: [SKILL VALID]
