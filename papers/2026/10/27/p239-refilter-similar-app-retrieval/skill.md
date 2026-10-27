# Skill: Retrieve-then-Filter — pipeline similar-item retrieval precision cao
Source: 2609.25306
Type: workflow (retrieval pipeline)

## Khi nào dùng skill này
- Bạn cần tìm "items tương đương chức năng" (functional substitutes — items user sẵn sàng đổi cho nhau, same user need), KHÔNG chỉ items topic gần: competitor analysis, related-content recommendation, product alternatives, dedup catalog.
- Embedding-only retrieval precision/F1 không đủ (ceiling ~60% F1 trong paper) nhưng bạn không afford LLM pairwise trên toàn corpus.
- Bạn muốn output count DYNAMIC (0..k) thay vì fixed top-k — items không có substitute thì trả về 0.

## Khi KHÔNG nên dùng
- Task cần semantic/topical similarity thuần (tag clouds, topic clustering) — embedding-only đủ, LLM filter thừa cost.
- Corpus quá nhỏ (<100 items) — filter từng pair trực tiếp bằng LLM, không cần retrieval stage.
- Không có khả năng define annotation guideline cho "substitute" — filter không có ground truth để calibrate few-shot examples.

## Input cần có
- Corpus items có TEXT description chất lượng (câu đầu tiên chứa core purpose — BGE-FIRST evidence cho thấy functional cues ở đầu description); ảnh/screenshot KHÔNG cần (multimodal thêm noise).
- Embedding model text-only LLM-class (Linq-Embed-Mistral hoặc tương đương); cosine similarity + ANN index (FAISS/ScaNN class).
- LLM filter (GPT-5 class) với ability output verdict + justification; 2-shot examples.
- Annotation guideline cho functional similarity (primary user-facing purpose + same user need; secondary-only sharing = NOT substitute).
- Budget ~$0,04/query + 4,2 s/query (GPT-5 scale) cho filter stage; embedding stage one-time cost.

## Các bước thực hiện
1. **Preprocess corpus** (replicate paper): filter non-English, remove privacy-policy/subscription/contact noise, strip emojis, lowercase, remove HTML, drop items description <200 chars hoặc popularity <100. → clean corpus (paper: 34,364 seed → 20,635).
2. **Embed + candidate retrieval**: embed full text mỗi item (no truncation); cosine similarity target vs corpus; lấy top-k candidates (k≈45 tested best balance; precision peak tại k=5 — chọn k theo recall need của bạn).
3. **LLM filter 0-shot trước**: prompt list k candidates + descriptions, yêu cầu verdict "functional substitute YES/NO" + justification per item; KHÔNG fix output count.
4. **Error analysis**: manual review ~75 false negatives 0-shot (hoặc 50–100 với scale bạn), categorize lỗi into 5 paper classes — (a) core feature secondary in candidate (28/75), (b) same goal different implementation method (18/75), (c) candidate fulfills part of core feature (11/75), (d) misidentified core feature (10/75), (e) different purpose same core feature (8/75).
5. **Chọn 2-shot examples** cover recurring categories (a)+(b) trước (chiếm 46/75 = 61% errors), KHÔNG random picks. Re-run filter 2-shot (precision 97%, recall 84%, F1 90% conditional class). KHÔNG go 4/6-shot (flat/decline).
6. **Stability**: nếu LLM không support temperature=0 → chạy 3 lần/query, average kết quả (paper method).
7. **Đánh giá**: precision / conditional recall / pooled recall / F1 (conditional + pooled); pooled recall là LOWER BOUND (union top-k all methods) — note trong report. So sánh vs platform built-in "similar items" nếu có (Wilcoxon signed-rank).
8. **Deploy**: embedding stage one-time offline; filter stage per-query online (~$0,04/query); log output count distribution per category → review dynamic density (Personalization/Social/Photography dense; Business/Tools/Sports sparse — paper pattern).

## Output mong đợi
- Per target: list 0..k functional substitutes (dynamic count, zero khi không có), mỗi kèm justification; aggregate metrics precision ≥90% / CR-F1 ~90% / PR-F1 ~86% trên held-out test; count-distribution table theo category.

## Ví dụ áp dụng
- Blog content site 500 bài: reader đọc bài "cách viết CV" → embed 500 bài, cosine top-45, GPT filter 2-shot ("reader bài này có chấp nhận bài kia làm thay thế không — same user need viết CV, không phải topic 'career advice' chung") → trả 12 bài liên quan thật (thay vì 40 bài top cosine chứa nhiều bài career-generic), F1 ~90%; bài "10 Bí quyết nấu phở" không có substitute → trả 0 thay vì gượng 10 bài.

## Gotchas
- **Define substitute trước**: KHÔNG có annotation guideline rõ ràng → filter drift (κ annotation paper 0,79); guideline phải say "primary user-facing purpose" + "same user need", secondary features không count.
- **Recall là lower bound**: pooled recall denominator = union top-k của all methods → never claim absolute recall; dùng conditional recall cho filter quality.
- **Multimodal hại nhiều hơn lợi**: screenshots/permissions/UI layouts conflate descriptive similarity (password manager vs expense tracker same list UI); text-only wins — skip image embedding cost.
- **Câu đầu description quyết định**: BGE-FIRST (first chunk) > BGE-AVG → functional cues Ở ĐẦU text; put core purpose sentence 1, truncation-friendly.
- **>2-shot examples không gain**: 4-shot/6-shot flat hoặc giảm nhẹ — 2 examples covering recurring error patterns là sweet spot, thêm examples phí context window.
- **Descriptions có thể marketing-flawed**: falsified feature claims → filter over-trust description; nếu data bạn có real usage logs, ưu tiên signal từ logs.
- **Dynamic count cần monitoring**: output 0–45/target → UI phải handle empty result gracefully; log density theo category để biết category nào intrinsically sparse (Business/Tools/Sports).
- **Cost scales linear**: $0,04/query × query volume — cache filter results cho hot targets (items hot), chỉ filter cold items on-demand.
- **Platform lists ≠ substitutes**: Google Play-style "similar items" mean 93 vs functional 21 (p<0,001) — không dùng platform list làm ground truth hay fallback cho substitution task.
