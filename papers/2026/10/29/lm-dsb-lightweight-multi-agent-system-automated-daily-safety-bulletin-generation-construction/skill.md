# Skill: planner-researcher-writer-content-pipeline
Source: 2610.36433v1 (LM-DSB)
Type: framework / workflow

## Khi nào dùng skill này
- Bạn cần tạo tài liệu chuyên ngành lặp lại hàng ngày/tuần (bản tin, báo cáo, hướng dẫn) từ corpus (tập tài liệu) riêng, và muốn chạy trên máy cục bộ (GPU 12-16GB VRAM) thay vì API trả phí.
- Output cần grounded (dựa trên nguồn thật) + auto citation (trích dẫn tự động) để kiểm tra compliance (tuân thủ quy định).
- KHÔNG nên dùng khi: tác vụ chỉ 1 prompt đơn giản không cần nhiều nguồn; hoặc tác vụ yêu cầu suy luận ngầm multi-factor (nhiều yếu tố kết hợp ẩn) — model ≤8B sẽ fail, cần model lớn hơn + human review (xem lại bởi con người).

## Input cần có
- Corpus domain: tài liệu phân cấp (policy → procedure → spec), tối thiểu ~30 documents; biết trước các "standard sections" (phần chuẩn) mà output phải có (LM-DSB dùng 11 sections).
- 1 model ≤8B parameter deployable cục bộ (pattern: Llama 3-8B-Instruct, MMLU 66.6%) + GPU 12-16GB VRAM + 32GB RAM.
- Ground truth: vài tài liệu mẫu do expert (chuyên gia) viết (LM-DSB: 515-620 từ/bài) để đo length ratio (tỷ lệ độ dài) + metrics lexical overlap.
- Bộ đánh giá: form Likert 5 điểm (Độ chính xác, Độ bao quát, Độ dễ hiểu, Khả năng hành động, Tuân thủ quy định) + N≈40 người đánh giá nội bộ.
- Tooling: LangGraph (orchestration agent), ChromaDB (vector database), BGE embedding BAAI/bge-large-en-v1.5 (biểu diễn nhúng 768 chiều), GPT-4 (chỉ để sinh training data, không dùng để chạy production), LoRA + 4-bit quantization cho fine-tuning.

## Các bước thực hiện
1. Phân tích corpus: liệt kê cấu trúc phân cấp và cross-referential dependency (phụ thuộc chéo giữa tài liệu); xác định danh sách N sections chuẩn của output và loại input context cần (LM-DSB: weather data + project info + topic).
2. Xây vector DB: chunk tài liệu 1024 token, overlap 200 token → encode BGE 768-dim → lưu ChromaDB kèm metadata (tên file, trang, category). Set similarity threshold 0.65, top-3 retrieval; tune threshold bằng iterative testing (thấp → nhiễu, cao → mất chi tiết).
3. Sinh SFT data: pipeline "unstructured" phân đoạn (max 4000 ký tự / threshold 3800 / min 2000); nhóm 3 segment → 6 QA pairs (cặp hỏi-đáp) qua GPT-4 temperature 0 → attach ChunkID → quy mô kỳ vọng ~300 examples/document (LM-DSB: 10,837 từ 37 docs). Tables/images summarize bằng GPT-4-Vision.
4. LoRA fine-tune model ≤8B (chỉ vì fluency domain — KHÔNG trông đợi thêm factual knowledge): 4-bit quantization, batch 2, lr 5e-5, 3 epochs, gradient accumulation 4, cosine warmup 0.1, max samples 500. CHÚNG: standalone FT có thể làm model tệ hơn baseline (Llama-FT 0.4222 < Llama-Base 0.4870 TF-IDF) — FT phải đi cùng RAG.
5. Orchestrate graph LangGraph: Supervisor (routing + duy trì workflow state) → Planner (JSON plan N sections + research queries) → Researcher (top-3 chunks + point-form summary) → Writer (Markdown final). Ép strict phase dependency (pha tuần tự nghiêm ngặt): mỗi pha chỉ chạy khi pha trước hoàn tất; context phải truyền đầy đủ giữa các pha — KHÔNG chạy song song.
6. Đánh giá 2 pha: Phase 1 quantitative — TF-IDF, BLEU, ROUGE-1/2 + length ratio vs ground truth (target: length ratio ≥ 0.95, ROUGE-2 cao 4-5× non-RAG); Phase 2 expert Likert 5 chiều N≈40 (target: compliance + accuracy ≥ 4.0, actionability là chiều hay yếu nhất — plan cải thiện procedural specificity + responsibility assignment).

## Output mong đợi
- Pipeline tạo tài liệu domain hoàn chỉnh (length ratio ~1.01) với citation tự động trỏ source file + trang, chạy được trên PC tiêu dùng, chất lượng đạt chấp nhận thực tế từ expert (mean 3.50-4.20/5).

## Ví dụ áp dụng
Solopreneur VN viết "bản tin thị trường bất động sản hàng tuần": corpus = 30 báo cáo quy hoạch + pháp lý; planner tạo 8 sections chuẩn (tình hình giá, giao dịch, pháp lý nổi bật, dự án mới, rủi ro, khuyến nghị...); researcher truy xuất top-3 chunks mỗi section; writer ghép thành bản tin Markdown kèm trích dẫn nguồn trang/báo cáo; chạy trên RTX 4070 Ti, không tốn API fee.

## Gotchas
- Chạy các agent song song → output phân mảnh (fragmented) vì phase sau thiếu input hoàn chỉnh từ phase trước — LM-DSB cố ý ép tuần tự, đừng "tối ưu" bằng song song.
- Fine-tuning đơn lẻ (không RAG) làm output tệ hơn baseline trên model nhỏ — luôn RAG grounding trước.
- Threshold retrieval (ngưỡng truy xuất) đặt không đúng đầu ra bị lặp hoặc mất chi tiết critical — dùng representative scenario (tình huống đại diện) test quanh 0.65 rồi mới cố định.
- Model ≤8B KHÔNG tổng hợp được implicit multi-factor risk (rủi ro nhiều yếu tố kết hợp ngầm, ví dụ: đào hố + trời lạnh + sưởi diesel → CO poisoning) — bản tin an toàn đa nguy cơ phải có con người review ở bước cuối.
- Metrics lexical (đo overlap từ vựng: TF-IDF/BLEU/ROUGE) chỉ đo mức trùng lặp từ vựng với 1 ground truth duy nhất, KHÔNG chứng minh factual correctness (đúng sự thật) — phải đánh giá expert Likert song song.
- Auto-citation phụ thuộc metadata (tên file, trang) phải bảo tồn từ bước chunking — mất metadata = mất traceability (khả năng truy xuất nguồn).
