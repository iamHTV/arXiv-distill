# 2609.31422 Active Provenance Gate cho Multi-Agent Debate Synthesis

## Problem
- Prior work (PROV, PROV-AGENT) coi log (nhật ký) của multi-agent debate (MAD — tranh luận đa tác nhân) là artifact (đối tượng) thụ động để kiểm tra sau, không phải cơ chế kiểm soát. Self-refine (tự sửa lỗi) cũng không ép ràng buộc cứng (hard constraint) tại biên giới tổng hợp (synthesis boundary — nơi draft debate thành báo cáo cuối).
- Hệ quả: mô hình tổng hợp tối ưu độ trôi chảy (fluency) biến các vị trí mâu thuẫn thành "consensus" (đồng thuận) bịa — không grounded (có căn cứ) trong lịch sử tranh luận. Nguy hiểm nhất ở tình huống khủng hoảng: operator tin nhầm vào đồng thuận trơn tru (automation bias — thiên kiến tin tự động hóa).

## Contribution
- Active Provenance Gate (APG — cổng nguồn gốc chủ động): layer (lớp) Phase 4 cài giữa debate và publication, chuyển provenance (truy xuất nguồn gốc) từ logging thụ động sang blocking chủ động trước khi xuất bản.
- Output chỉ là synthesis có provenance verifiable (kiểm chứng được) HOẶC Divergence Report (báo cáo phân kỳ) liệt kê claim (khẳng định) chưa giải quyết + nguồn xung đột.

## Method (tóm tắt cốt lõi)
- Testbed: mô phỏng ủy ban quản lý khủng hoảng, corpus kg_cfr_full với 90 knowledge-annotated trajectory (quỹ đạo được gắn nhãn kiến thức), framework Resilient MAS open-source.
- Assembly: gộp transcript chat công khai + document KG/RAG đã dedup (loại trùng) + private trace thành SynthesisState — corpus đóng (closed-world) với địa chỉ ổn định; Proposer chỉ được phép nén, phơi xung đột, suy luận logic.
- Proposer–Validator dị cấu trúc: PROPOSER NODE = Gemini 3 Flash (rẻ, prompt hướng đồng thuận), VALIDATOR NODE = Gemini 3.1 Pro làm engine NLI (natural language inference — suy luận ngôn ngữ tự nhiên) nghiêm ngặt, trả JSON {verdict, provenance_fidelity, unsupported_sentences}.
- PF (Provenance Fidelity — độ trung thực nguồn gốc) = tỷ lệ câu được NLI entailment (hàm chứa) nghiêm ngặt hỗ trợ / tổng câu. Hard gate (cổng cứng) PF ≥ 0.95; fail → FALLBACK NODE sinh correction hint (gợi ý sửa), retry tối đa MAX_SYNTHESIS_ITER = 3; hết budget → hard exit, xuất JSON DIVERGENCE_REPORT kèm _infer_conflicting_sources (suy luận nguồn xung đột).

## Key Findings
- Baseline synthesis: PF khởi điểm 0.288 (xung đột cao) / 0.183 (low) — hallucination rate (tỷ lệ bịa) rất cao dù trace RAG/KG grounded hoàn hảo.
- Self-healing (tự chữa) có giới hạn nâng terminal PF lên 0.617 / 0.586 (gấp đôi+ trong điều kiện khó); divergence rate (tỷ lệ phân kỳ) 75,0% dưới xung đột zero-sum vs 60,0% low-conflict.
- Ablation (loại trừ) 30-run: cấu hình symmetric (cùng Gemini 3 Flash vừa sinh vừa audit) validate sai compromise không an toàn 85,6% lần; cấu hình asymmetric (Gemini 3.1 Pro làm validator) hạ PF text tương tự xuống 0.300, reject 63,3% output không hòa giải được.
- Human study N=33 blind A/B: 66,7% đánh giá baseline "fluent and diplomatic" hơn; scenario S026 (zero-sum stalemate), 75,8% nhận output APG faithful hơn; trust (độ tin) Likert 5 điểm: APG M=3,27 SD=1,21 vs baseline M=2,45 SD=0,90, t(32)=3,12, p=0,0039. Session recovery giữ 97,3% độ dài text.

## Actionable Insights
1. Không để cùng 1 model vừa viết vừa kiểm tra tổng hợp của chính nó: symmetric setup thất bại 85,6%. Ví dụ: agent soạn email tổng hợp từ 5 nguồn → dùng model mạnh hơn (hoặc prompt hệ thống khác hẳn) làm auditor duyệt từng câu trước khi gửi khách.
2. Ep programmatic gate thay vì prompt mềm: Rule "PF ≥ 0.95" cứng + divergence report rõ ràng được 75,8% người dùng tin hơn bản trôi chảy bịa. Ví dụ: dashboard tin nhắn chăm sóc khách — thay vì tin nhắn mượt bịa số liệu, hiện "chưa đủ dữ liệu" + liệt kê 2 nguồn mâu thuẫn.
3. Retry budget = 3 rồi dừng: session fail sau 2 hint rơi vào loop dao động, retry thêm chỉ tốn compute. Ví dụ: pipeline agent của bạn giới hạn 3 lần tự sửa, lần 4 chuyển flag "cần nhân viên duyệt".

## Assumptions & Limitations
- Điều kiện: corpus đóng với địa chỉ ổn định; validator phải mạnh hơn proposer (heterogeneous capacity); NLI zero-shot (không fine-tune) khả dụng.
- Paper thừa nhận: simulation tổng hợp + shock hard-coded; closed-world (so với corpus, không phải thực tế bên ngoài); N=33 convenience sample (sinh viên STEM), không chia expert vs crowd; zero-shot NLI audit thiên vị ngôn ngữ/verbosity; metric circularity (vòng tròn đo lường) vì auditor là LLM.
- Mày thấy thêm: gate block 60–75% output dưới xung đột → cost availability vận hành; ablation chỉ Gemini, chưa generalize sang model khác; human study thiếu domain expert thật dưới time pressure.

## Metadata
- Năm: 2026 (25 Sep 2026), tác giả: Jakub Masłowski, Jarosław A. Chudziak (Warsaw University of Technology), category: cs.MA, accepted ICTAI 2026, link PDF: https://arxiv.org/pdf/2609.31422v1, citation count: không có dữ liệu (paper mới; Semantic Scholar API rate-limited)
