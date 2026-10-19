# Skill: tracer-trace-regularized-training
Source: 2610.19133v1
Type: framework

## Khi nào dùng skill này
- Hệ thống LLM/RAG/agent nhận nội dung không tin cậy qua nhiều kênh (retrieved document, tool output, agent message, tin nhắn tiếp theo).
- Muốn giảm tỉ lệ tấn công thành công (ASR) của间接 prompt injection mà không làm giảm độ chính xác trên tác vụ sạch (clean accuracy).
- Có sẵn tập dữ liệu tác vụ (ví dụ GSM8K) và mẫu tấn công间接 template-based.

## Tình huống KHÔNG nên dùng
- Chỉ cần đánh giá trong một kênh duy nhất (bỏ qua rủi ro xuyên kênh).
- Đối thủ là optimization-based hoặc đa luân (multi-turn) không bị bao quát bởi template-based.

## Input cần có
- 1 mô hình ngôn ngữ cơ sở (ví dụ Qwen2.5-3B-Instruct).
- Tập dữ liệu tác vụ với input và đáp án vàng (gold answer).
- Mẫu nội dung tấn công间接 (adversarial payload) và các kênh trình bày: follow-up, rag, tool, agent.
- Công cụ GRPO (hoặc tương đương), 4-bit QLoRA, vLLM cho rollout.
- Verifier trích xuất neo (anchor propositions) từ trace lý luận sạch.

## Các bước thực hiện
1. Thu thập mẫu tác vụ (xi, yi) và payload tấn công (ai).
2. Mỗi tập huấn luyện (three-turn game): mô hình tạo trace lý luận sạch (τ0) và đáp án sạch (ŷ0) từ tác vụ sạch.
3. Lấy mẫu một kênh (ci) từ phân phối pS(c) (ví dụ follow-up/rag/tool/agent), render payload qua kênh đó thành ρci(ai).
4. Mô hình tạo trace lý luận sau khi bị tấn công (τci) và đáp án sau khi bị tấn công (ŷci) từ tiền tố sạch + nội dung đã render.
5. Tính phần thưởng hợp hợp sau khi tấn công: đáp án chính xác (ans, trọng số 0.25), chất lượng quy trình (proc, 0.25), giữ neo (anc, 0.20), khả năng sửa gated bằng chứng (corr, 0.20), kiểm soát độ dài (len, 0.10).
6. Khi cờ evidence gate active (đáp án sạch đúng và bằng chứng châm không hợp lệ), áp dụng ATRC: căn chỉnh phân phối token sau khi tấn công về phân phối sạch qua KL divergence và phục hồi token sạch cam kết trên các vị trí đã cam kết (committed spans).
7. Cập nhật mô hình bằng GRPO với KL regularization và ATRC regularization.
8. Đánh giá xuyên kênh: cùng payload, đổi wrapper (follow-up → rag → tool → agent), đo ASR và clean accuracy trên mỗi kênh.

## Output mong đợi
- Mô hình giảm ASR attacks間接 đáng kể (ví dụ từ 65.5% xuống 6.1% ở RAG) đồng thời giữ clean accuracy cao (78–82%), và độ mạnh chuyển qua các kênh tốt hơn so với đào tạo theo một kênh duy nhất.

## Ví dụ áp dụng
- Hệ thống RAG nội bộ của doanh nghiệp: thu thập mẫu châm injeciton qua retrieved document, tool output, agent message; huấn luyện Qwen2.5-3B bằng TRACER 3 epochs; đánh giá trên 4 kênh; ASR trung bình giảm xuống ~13.9% (multi-framing RAG+tool).

## Gotchas
- Không chỉ đánh giá trong một wrapper — độ mạnh theo kênh không chuyển qua kênh khác.
- Không dùng phần thưởng chỉ theo đáp án đúng (answer-only) — đạt 21.3% ASR vs 6.1% của full TRACER; phần thưởng composite giữ suy luận sạch.
- Không bắt buộc mô hình giữ trace sạch khi bằng chứng châm hợp lệ — corrigibility term phải evidence-gated để tránh blanket refusal.
- Không coi TRACER là ranh giới bảo mật đầy đủ — kết hợp với runtime safeguards (retrieval filtering, tool-output parsing, monitoring, sandboxing).

## Kiểm tra kỹ năng (self-check)
- Người không đọc paper gốc có follow được 8 bước trên không? [YES] — từng bước là action cụ thể.
- Bước nào mơ hồ nhất? Bước 6 (ATRC trên committed spans) cần chi tiết align logits theo response-relative position.
- Input section có đủ không? [YES] — cơ sở mô hình, tập dữ liệu, payload tấn công, các kênh, GRPO/QLoRA/vLLM, verifier neo.

## Dry run (tình huống giả)
- Tình huống: Doanh nghiệp nhỏ có chatbot RAG lấy tài liệu內 bộ; attacker có thể châm injeciton vào retrieved document.
- Chạy skill: (1) Thu thập 2,000 mẫu tác vụ GSM8K và payload châm; (2) huấn luyện Qwen2.5-3B 3 epochs, lấy mẫu kênh ngẫu nhiên (follow-up/rag/tool/agent); (3) tính phần thưởng hợp hợp sau mỗi tấn công; (4) áp dụng ATRC khi cờ gate active; (5) cập nhật qua GRPO; (6) đánh giá ASR trên 4 kênh; (7) nếu RAG ASR giảm từ 65.5% xuống dưới 10% và clean accuracy giữ 78–82% → triển khai.

## Verdict: [SKILL VALID]
