# Skill: oa-rag-grounded-answer (trả lời có neo bằng chứng ontology)
Source: 2610.36335
Type: framework / workflow

## Khi nào dùng skill này
- Xây dựng Q&A bot (bot hỏi đáp) hoặc AI agent (tác nhân) phục vụ domain (lĩnh vực) chuyên biệt mà câu trả lời PHẢI trung thực với knowledge base (kho kiến thức) — ví dụ FAQ sản phẩm, tra cứu quy định nội bộ, support khách hàng.
- Domain đã có dữ liệu có cấu trúc (ontology (bản thể học), knowledge graph (đồ thị kiến thức), hoặc schema (lược đồ) quan hệ rõ ràng) và cần kiểm soát hallucination (ảo tưởng).
- KHÔNG nên dùng: chat open-domain (mở) không có knowledge base; domain không có ontology/schema chuẩn nào để query (truy vấn); chỉ cần tóm tắt tài liệu tự do không cần verify (kiểm chứng) form (hình thức).

## Input cần có
- Knowledge base có cấu trúc: ontology OWL hoặc tương đương (entities (thực thể), relations (quan hệ), axioms (tiên đề) như A ⊑ ∃r.B), hoặc export (xuất) được thành concept card (thẻ khái niệm).
- Query endpoint (điểm truy vấn) SPARQL hoặc reasoner (bộ suy luận) có thể kiểm tra entailment (suy diễn chứa), hoặc mô phỏng 2 việc này bằng code (exact match + graph traversal (duyệt đồ thị)).
- LLM access (quyền truy cập mô hình) + ngân sách interaction (tương tác) ReAct: paper dùng ~5.8 LLM call/question, context window (cửa sổ ngữ cảnh) 8,192 token là đủ.
- Danh sách question (câu hỏi) cần trả lời.

## Các bước thực hiện
1. Pre-tool draft (nháp trước công cụ): prompt LLM trả lời câu hỏi CHỈ từ ngữ cảnh đầu vào + parametric knowledge (kiến thức tham số), lưu làm draft ỹ. Mục đích: nếu ngữ cảnh đã đủ, bỏ qua ontology để tiết kiệm cost (chi phí).
2. Xây concept card cho mỗi entity trong ontology: bản ghi key:value fixed order — name, definition (định nghĩa), parents (cha — inferred direct), children (con — inferred direct), stated relations (quan hệ khai báo, dạng "r -> B"), comments, annotations (chú thích). Đây là đơn vị retrieval (truy xuất) dạng text.
3. ReAct loop (vòng hành động–quan sát), mỗi lượt sinh 1 action là SPARQL query:
   - DESCRIBE "A": lấy concept card của A.
   - ASK {"A" "r" "B"}: kiểm tra O |= A ⊑ ∃r.B có entailed (suy diễn được) bởi reasoner không → trả "ENTAILED" / "NOT ENTAILED". Prompt PHẢI cảnh báo open-world assumption (giả định thế giới mở): NOT ENTAILED ≠ false (ontology có thể incomplete — không đầy đủ).
   - SELECT ?x WHERE {conditions}: lấy entities/relations thỏa điều kiện.
   - Query fallback: SELECT rỗng → so sánh câu hỏi với concept card bằng BM25, lấy top-k candidate để agent DESCRIBE tiếp.
   - Name linking: exact match (khớp chính xác sau normalize (chuẩn hóa) case/whitespace/underscore) → ambiguous (mơ hồ: trả candidate list để disambiguate (gỡ mơ hồ)) → unknown-name fallback (BM25 pool 200 tên + rerank (xếp lại) bằng string similarity (độ tương tự chuỗi), lấy top-5 gợi ý để agent sửa query).
   Dừng khi có final answer hoặc hết interaction budget.
4. Lọc observation (quan sát): loại bỏ observation từ tool call thất bại/lỗi execution (thực thi)/SELECT rỗng → evidence digest (bản tóm tắt bằng chứng) E.
5. Answer (trả lời): nếu E ≠ ∅ → prompt P_fin với question + E + draft ỹ; nếu E = ∅ → prompt P_own trả lời từ parametric knowledge.
6. Attribution turn (lượt gán nguồn): tiếp cùng hội thoại với prompt P_att yêu cầu LLM (a) chọn cited evidence Ĉ ⊆ E (bằng chứng thực sự được dùng) và (b) gán grounding level (mức neo) ĝ: entailed (logic chứa câu trả lời) / supported (hỗ trợ, cần thêm parametric knowledge) / related (liên quan nhưng không đủ) / unrelated (không liên quan). Xuất cả 3 thứ: câu trả lời + Ĉ + ĝ.

## Output mong đợi
- Câu trả lời cuối cùng kèm bằng chứng ontology được trích dẫn (Ĉ) và grounding level (ĝ) 4 bậc.
- Báo cáo reliability (độ tin cậy) có thể action (hành động) được: auto-publish (xuất bản tự động) câu entailed/supported; related/unrelated route vào review human (duyệt người).
- Hệ quả đã verify trong paper: bậc grounding cao → accuracy (độ chính xác) cao (Qwen Test 3: entailed 94.9% đúng, supported 82.1%, còn lại 72.1%).

## Ví dụ áp dụng
- Bot tư vấn sản phẩm cho shop online: customer hỏi "Laptop X có dùng được cho dựng video 4K không?". Bước 1 draft từ knowledge chung ("có lẽ được"). Bước 3 DESCRIBE "Laptop X" → concept card cho thấy stated relation "target use -> video editing 4K" và ASK {"Laptop X" "target use" "video editing 4K"} → ENTAILED. Bước 5-6 trả lời "Có, Laptop X được nhà sản xuất liệt kê cho dựng video 4K" grounding=entailed, cite evidence card → xuất bản luôn không cần duyệt.

## Gotchas
- ASK "NOT ENTAILED" KHÔNG có nghĩa câu trả lời sai (open-world assumption) — phải instruct LLM điều này trong agent prompt, nếu không agent sẽ phủ nhận câu đúng.
- Grounding level là self-assessment (tự đánh giá) của LLM, KHÔNG phải formal guarantee (bảo đảm hình thức) về correctness — vẫn cần sample audit (kiểm toán mẫu) bởi người.
- Retrieval (truy xuất) là bottleneck (nút cổ chai) chính: OQ (open question — câu hỏi mở) fully retrieved gold evidence chỉ 23.6% vs MCQ 61.7%. Với câu hỏi không có options (lựa chọn) gợi ý, cần nhiều lượt DESCRIBE + fallback BM25 hơn.
- Definition-heavy information (thông tin nặng định nghĩa) kém accessible với exact SPARQL — Test 2 OQ là trường hợp khó nhất; hãy bổ sung informal annotation (định nghĩa, đồng nghĩa) vào concept card, đừng chỉ rely vào axioms.
- Ontology coverage (phạm vi phủ) quyết định giới hạn: câu hỏi ngoài vocabulary (từ vựng) ontology → unrelated grounding, đừng ép trả lời từ evidence.
- Cap interaction budget (ngân sách tương tác) — paper dùng ~5.8 call/question; không giới hạn sẽ phát sinh cost (chi phí) token vô ích.
