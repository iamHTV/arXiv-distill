# Skill: Provenance Gate kiểm chứng tổng hợp đa tác nhân
Source: 2609.31422
Type: framework (khung phương pháp) / evaluation-method (phương pháp đánh giá)

## Khi nào dùng skill này
- Pipeline agent (tác nhân) tạo bản tổng hợp/tin nhắn/decision report (báo cáo quyết định) từ nhiều nguồn hoặc nhiều agent Tranh luận, trước khi gửi tới khách hàng hoặc operator.
- Cần publish (xuất bản) output mà độ grounded (có căn cứ nguồn) quan trọng hơn độ trôi chảy — support khách hàng, báo cáo dữ liệu, tổng hợp tranh luận.
- KHÔNG nên dùng: output sáng tạo không cần cite (trích dẫn) (quảng cáo, story); hoặc khi bạn chỉ có 1 model duy nhất và không thể phân tách vai trò validator.

## Input cần có
- Debate transcript (bản ghi tranh luận) hoặc tập nguồn đã thu thập (document KG/RAG, trace riêng).
- 2 model: 1 cheap model (rẻ) làm Proposer (soạn thảo), 1 reasoning model (mô hình suy luận mạnh) làm Validator (kiểm chứng) — KHÔNG dùng cùng model cho cả 2 vai trò.
- Ngưỡng PF (Provenance Fidelity — độ trung thực nguồn gốc), mặc định 0.95; retry budget (ngân sách thử lại) = 3.

## Các bước thực hiện
1. Freeze corpus (đóng băng kho chứng cứ): gộp tất cả artifact (transcript, document đã dedup — loại trùng, private trace) thành 1 corpus đóng với địa chỉ ổn định; Proposer chỉ được phép nén, phơi xung đột, suy luận logic — không thêm thông tin ngoài corpus.
2. Generate synthesis (tạo bản tổng hợp): Proposer (cheap model) soạn draft dưới prompt hướng đồng thuận, KHÔNG bật chế độ "không đồng thuận" — mô phỏng áp lực phải ra quyết định.
3. Audit từng câu (kiểm tra): Validator (model mạnh) chạy NLI (natural language inference — suy luận ngôn ngữ tự nhiên) entailment (hàm chứa) nghiêm ngặt từng câu vs corpus, trả JSON: verdict, provenance_fidelity = số câu được hỗ trợ / tổng câu, danh sách câu không hỗ trợ.
4. Áp dụng hard gate (cổng cứng): PF >= 0.95 → publish draft; PF < 0.95 → FALLBACK NODE sinh correction hint từ danh sách câu fail, Proposer viết lại (tối đa 3 lần). Hết 3 lần vẫn < 0.95 → hard exit.
5. Emit Divergence Report (báo cáo phân kỳ) khi fail: JSON liệt kê unresolved_claims (khẳng định chưa giải quyết) + conflicting sources (nguồn xung đột) đã suy luận ra deadlock (bế tắc), thay vì xuất bản compromise bịa.

## Output mong đợi
- Hoặc 1 bản tổng hợp với PF >= 0.95 (mỗi câu traceable — truy vết được tới corpus), hoặc 1 Divergence Report cấu trúc JSON rõ ràng mà operator có thể hành động ngay (biết claim nào disputed — tranh chấp và nguồn nào xung đột).

## Ví dụ áp dụng
- Agent chăm sóc khách tổng hợp chính sách hoàn hàng từ 3 KB (knowledge base — cơ sở tri thức) document mâu thuẫn: draft nói "hoàn trong 30 ngày" nhưng KB A nói 14 ngày → gate fail → email gửi khách: "Chúng tôi chưa thống nhất được thời hạn: nguồn A nói 14 ngày, nguồn B nói 30 ngày — đội ngũ sẽ xác nhận trong 24h" thay vì khẳng định bịa.

## Gotchas
- Dùng cùng 1 model cho Proposer và Validator: ablation cho thấy 85,6% compromise không an toàn được validate nhầm — luôn tách 2 vai trò, validator phải mạnh hơn.
- Prompt mềm (kiểu "hãy trung thực") không đủ: phải là programmatic gate (cổng lập trình) cứng với số PF cụ thể, nếu không model vẫn bịa trôi chảy.
- Retry > 3 lần: session fail sau 2 hint rơi vào loop dao động — retry thêm tốn compute mà không cải thiện PF.
- Metric circularity (vòng tròn đo lường): PF tính bởi LLM auditor nên có thiên vị verbosity (rườm rà) và ngôn ngữ; nếu có thể, validate thêm 1 mẫu nhỏ bằng annotator (người gắn nhãn) thật.
