# Báo cáo distill ngày 2026-10-20 — 10 paper buổi sáng (paper #175–#184)

Scan arXiv 2026-10-20 sáng, nhóm high (điểm 82–93). Mỗi paper: Làm gì / Học được gì / Áp dụng cho bạn.

### [1] Iterate on an LLM, Serve on an SLM (arXiv 2610.14576v1)
**Làm gì:** Thiết kế hành vi tác nhân (agent) trên mô hình lớn (frontier model — mô hình mạnh nhất) bằng cách lặp lệnh nhắc (prompt), rồi chưng cất (distill) hành vi đã ổn định vào mô hình ngôn ngữ nhỏ (SLM) Qwen3-8B qua dữ liệu production thật (549 batch, 11.621 mẫu huấn luyện). Ví dụ thực: tác vụ phân loại yes/no để gỡ ca làm việc nhân viên chăm sóc tại nhà.
**Học được gì:** Qwen3-8B tinh chỉnh (fine-tune) đạt 91,3% nhất quán với trace production — cao hơn chính mô hình teacher GPT-5.4-nano (chỉ tự nhất quán 72,7%). Chi phí giảm ~10 lần ($0,19–0,38 so với $1,9–7,7 trên 1.000 quyết định), nhanh 2,5 lần (2,9s so với 7,1s p50). Người điều phối chuyên nghiệp phê học trò 48 lần so với teacher 29 lần trên 77 trường hợp bất đồng.
**Áp dụng cho bạn:** Dùng mô hình lớn để thiết kế prompt phân loại lead (khách tiềm năng) hoặc email, ghi lại vết thực thi (trace) thật, rồi LoRA-tune mô hình nhỏ chạy hàng ngàn quyết định/ngày với chi phí thấp.

### [2] Tool Recommendation for Multi-Step Agents (arXiv 2610.23707v1)
**Làm gì:** Thay vì nhét toàn bộ danh mục ~8.200 công cụ (định nghĩa chiếm ~1,76 triệu token — đơn vị xử lý văn bản, vượt cửa sổ ngữ cảnh mọi mô hình) vào agent, chỉ cho agent 3 công cụ cố định (SelectTools, UseTool, ListApps) chạy tại gateway (cổng trung gian); hệ thống 1,2B tham số truy xuất và xếp lại công cụ theo từng tác vụ.
**Học được gì:** Completeness@10 (tỷ lệ truy vấn có TẤT CẢ công cụ cần trong top-10) 45,2% so với BM25 (xếp hạng từ vựng) 28,8% (+57% tương đối); Recall@10 55,2 so với 37,0. Tổng hóa đơn giảm 13,6% (khoảng tin cậy 7,4–18,4%, p=0,006), mọi phiên đều rẻ hơn; hoàn thành tác vụ tương đương (276/327 so với 273/327, p=0,80).
**Áp dụng cho bạn:** Khi agent của bạn gọi nhiều công cụ/API, đừng liệt kê tất cả tool trong ngữ cảnh — dùng lớp gợi ý tool theo tác vụ để giảm token và tiền, vẫn giữ tỷ lệ hoàn thành.

### [3] TRACER: Trace-Regularized Training Against Indirect Prompt Injection (arXiv 2610.19133v1)
**Làm gì:** Đào tạo đối kháng (adversarial training) chống prompt injection gián tiếp (tin tặc chôn lệnh tấn công vào tài liệu agent đọc) theo kênh trình bày: lấy mẫu tấn công từ 4 kênh (tin nhắn tiếp theo, tài liệu truy xuất RAG — truy xuất tăng cường sinh văn bản, output công cụ, tin nhắn agent khác) trong huấn luyện, kết hợp phần thưởng gated bằng bằng chứng và chuẩn hóa trace suy luận (ATRC).
**Học được gì:** Cùng payload (đoạn tấn công): tỷ lệ tấn công thành công (ASR) 18% ở kênh follow-up so với 53% ở kênh tài liệu truy xuất (+35 điểm phần trăm) trên mô hình chỉ huấn luyện kênh follow-up. TRACER trên GSM8K với Qwen2.5-3B: giảm ASR dạng RAG từ 65,5% xuống 6,1%, giữ clean accuracy (độ chính xác câu sạch) 78–82%; paraphrase giữ lại (held-out): 10,0% so với 62,7% base.
**Áp dụng cho bạn:** Agent đọc tài liệu/email ngoài là kênh nguy hiểm nhất — kiểm thử an toàn theo TỪNG kênh riêng, không chỉ kênh chat; khi build agent RAG, đưa payload tấn công vào tài liệu truy xuất khi red-team (kiểm thử đối kháng).

### [4] Be Careful Who You Trust (arXiv 2609.31704v1)
**Làm gì:** Đo độ phối hợp nhóm agent LLM trong trò chơi Stag Hunt (trò hợp tác) khi thông tin công khai bị hỏng (corruption — lỗi truyền tin), tách biệt lựa chọn riêng của agent, hành động công khai nhìn thấy, và kết quả thực thi — để thấy sụp đổ phối hợp có thể do lỗi cơ học chứ không phải agent đổi ý.
**Học được gì:** N=5 agent, 3 kênh công khai: thành công thật 78% ở mức hỏng 80%, trong khi thành công công khai chỉ 12%; ranh giới cơ học (mechanical boundary) 1−M/N = 40%; lực thực hiện ở 60% hỏng: 1,702 so với 3,218 trung thực. Mô hình Llama-3.1-8b yếu nhất (~0,62 tỷ lệ khớp).
**Áp dụng cho bạn:** Khi build hệ thống multi-agent (đa tác nhân), đừng kết luận "hợp tác tốt" chỉ qua log công khai — cần đo quyết định riêng từng agent; thiết kế kênh riêng cho quyết định quan trọng.

### [5] Forty Shades of Blue: MODA (arXiv 2609.14896v1)
**Làm gì:** Thuật toán học tăng cường (reinforcement learning) hậu huấn luyện trực tuyến tối ưu ĐỒNG THỜI chất lượng và đa dạng phản hồi: điều kiện mode qua token abstract trong một policy (chính sách) chia sẻ, mỗi mode là một agent MARL (học tăng cường đa tác nhân) cạnh tranh, kèm cổng chất lượng tùy prompt chống reward hacking (khai thác lỗ hổng phần thưởng).
**Học được gì:** Đa dạng ngữ nghĩa SBERT (mô hình đo tương đồng câu) +265% trên Infinite-Chat held-out đồng thời năng lực chung +10,3% so với Qwen3-8B cơ sở; so DivPO (baseline mạnh nhất): SBERT 0,274→0,482 (+75,9%), E-Vendi (đo đa dạng entropy) 2,86→4,4 (+53,8%). Test "Name a shade of blue": tạo 40 sắc xanh riêng biệt (+122% so với base, +150% so với SSoT); 7 benchmark năng lực chung không giảm.
**Áp dụng cho bạn:** Khi LLM sinh nội dung (caption, slogan, mô tả sản phẩm), chủ động chống mode collapse (sụp mode — mọi output giống nhau): yêu cầu nhiều variant/angle rõ ràng thay vì chỉ output "tốt nhất".

### [6] Believed but Not Said (arXiv 2610.22138v1)
**Làm gì:** Đo sự sụp đổ niềm tin ẩn (hidden belief collapse) trong thảo luận đa agent: theo dõi đồng thời câu trả lời riêng (private probe — thăm dò ẩn khỏi đồng đội) và tư thế công khai của mỗi agent, phát hiện nhiễm tin sai không bao giờ lộ ra transcript (bản ghi hội thoại).
**Học được gì:** 1 attacker (đối thủ cắm câu sai): tỷ lệ nhiễm niềm tin cuối (FPI) trung bình 44,8%; 3 attacker: 60,5%. Agent trung thành giữ câu sai riêng tư trong 51,6% lượt nhưng công khai tán thành chỉ 19,7% (gấp 2,6 lần). ~80% nhiễm cuối đã có vào vòng 4, sau đó không leo tiếp. Kiến thức không dự đoán độ mạnh: GPT-OSS-120B biết 85% sự thật nhưng kết thúc sai trên 80% số đó khi có 3 attacker.
**Áp dụng cho bạn:** Debate/họp đa agent không an toàn trước vài đối thủ cắm thông tin sai — dùng probe riêng tư + giới hạn số vòng (nhiễm gần xong ở vòng 4); đừng tin "agent đồng thuận" là đúng.

### [7] When Debate Helps (arXiv 2610.04686v1)
**Làm gì:** Chỉ ra debate (tranh luận) đa agent thắng bình chọn đa số CHỈ KHI cả hai điều kiện cùng xảy ra: đề xuất đúng được bề mặt (proposal supply — tạo headroom có thể phục hồi) VÀ phần đọc kết quả nhận diện đề xuất đúng đó bằng bằng chứng xác thực (LVD — Latent Verification Debate). Debate đối xứng không biết sự thật (truth-agnostic) là martingale null (không drift dương về accuracy).
**Học được gì:** Qwen3-4B: Vanilla Debate 92,69 so với self-consistency@20 91,20; AC-Greedy Debate +1,46 điểm (5 hạt giống). Probe kiểm soát: hỗ trợ đúng đưa accuracy 0,325→0,655 tại d=3; R0→R3: 76,09%→78,52%.
**Áp dụng cho bạn:** Debate đa agent chỉ đáng tiền khi có verifier (bộ xác thực) đọc bằng chứng — bình chọn đơn thuần không tạo lợi; dùng debate khi cần candidate đa dạng + xác thực, không phải mọi tác vụ.

### [8] Candidate Supply and Answer Selection (arXiv 2608.25937v2)
**Làm gì:** Phân tích giá trị LLM judging (mô hình chấm) trong hệ thống đa agent qua hai bên: cung đề xuất (câu đúng có hiện diện không, phổ biến hay thiểu số) và quy tắc chọn đáp án cuối (kết hợp tần suất bình chọn + xếp hạng judge để cứu câu đúng bị quá số).
**Học được gì:** Single response 39,88% ở 1,0× token; majority voting (bình chọn đa số) 41,06% ở 4,96×; open committee (hội đồng mở) 42,20% ở 10,73× (+1,14 điểm). Khoảng cách tạo–giữ (generation-retention gap) 13–14 điểm. Khi đáp án đúng ở thiểu số: committee chọn đáp án sai phổ biến 73,25%. Hybrid selection (vote + judge rank, t=2–4): 70,82–70,95% so với majority 63,82% (+7 điểm). 90–95% chạy xong sau 1 vòng; ép 6 vòng tốn 33–49× token mà không lợi.
**Áp dụng cho bạn:** Dùng committee/chấm điểm: (a) đảm bảo candidate đúng được TẠO ra trước, (b) chọn hybrid (vote + rank judge) thay vì majority thuần, (c) dừng sau 1–2 vòng.

### [9] RIT-RAG: Navigating Document Corpora with Retrieval-Induced Trees (arXiv 2610.11370v2)
**Làm gì:** Kết hợp lấy nội dung (content retrieval) với điều hướng cấu trúc (structure-aware navigation): truy xuất (BM25 + dense retrieval với gte-modernbert-base) tìm "nơi tìm", rồi dẫn agent đến cây con cấu trúc (trích xuất cạnh mục lục ToC bằng Qwen3-32B) xung quanh đoạn đã truy xuất để agent chọn đọc chọn lọc.
**Học được gì:** Đạt accuracy (độ chính xác do LLM phán) cao nhất trên WixQA (6.221 trang trợ giúp), QASPER (416 bài báo NLP), FinanceBench (364 báo cáo SEC), EntQABench (2,84 triệu trang): +10,5/+5,0/+4,5 điểm so với Agentic Search trên WixQA; +12,2–13,3 điểm so với PageIndex trên QASPER; FinanceBench +9,3/+8,0/+4,6 so với baseline tốt nhất. Chi phí online 5,7–13,3 cent/câu hỏi (đắt hơn Agentic Search 1,3–6,3 cent nhưng accuracy cao hơn).
**Áp dụng cho bạn:** RAG trên corpus có cấu trúc (trung tâm trợ giúp, tài liệu sản phẩm, báo cáo): trích xuất ToC/heading để xây cây, kết hợp truy xuất từ vựng + ngữ nghĩa rồi cho agent đọc chọn lọc theo cấu trúc — accuracy cao hơn agentic search thuần.

### [10] Embedding Surgery (arXiv 2609.05110v1)
**Làm gì:** Sửa lỗi xếp hạng trong truy xuất dense (vector — biểu diễn nhúng) bằng cập nhật cục bộ, tối thiểu lên embedding tài liệu tại thời điểm truy vấn, hướng dẫn bởi phản hồi (biên tập chuyên gia, tương tác người dùng, nhãn giả từ LLM), formulated thành bài toán tối ưu lồi bậc hai (convex QP) ép buộc ràng buộc thứ tự trong khi tối thiểu hóa thay đổi biểu diễn.
**Học được gì:** Cải thiện nhất quán, đến +60,64% cải thiện tương đối nDCG@10 (đo chất lượng top-k, TAS-B trên DL-Hard dưới phản hồi chuyên gia); 4 mô hình zero-shot (Contriever, TAS-B, E5, Snowflake-Arctic Embed), 7 benchmark (TREC DL'19/'20, DL-Hard, Robust'04, CAsT'19, QSharedRel, MS MARCO Dev).
**Áp dụng cho bạn:** Khi retrieval trả sai thứ tự ở vài query cụ thể, "phẫu thuật" embedding cục bộ theo feedback thay vì tinh chỉnh lại toàn bộ chỉ mục — nhẹ, thích ứng theo từng truy vấn.

## CÓ GÌ ÁP DỤNG ĐƯỢC CHO BẠN

1. **Prompt-space dev, nhỏ để chạy:** Thiết kế hành vi trên mô hình lớn, chưng cất vào mô hình nhỏ — chi phí giảm ~10×, nhanh 2,5× ([1]). → Copy: làm prototype prompt trên GPT/frontier, ghi trace thật, LoRA-tune mô hình 4–8B cho tác vụ lặp lại (phân loại lead, gợi ý trả lời).
2. **Gợi ý tool thay vì danh sách fix:** 3 công cụ cố định tại gateway, hóa đơn −13,6%, accuracy tương đương ([2]). → Copy: cho agent marketing/xếp lịch chỉ 3 công cụ vào context, đọc tool còn lại theo tác vụ qua MCP (giao thức ngữ cảnh mô hình).
3. **Kiểm thử an toàn theo kênh:** tài liệu truy xuất nguy hiểm gấp ~3× kênh chat (ASR 53% so với 18%) ([3]). → Copy: red-team agent RAG bằng cách chèn lệnh độc vào chính tài liệu nó đọc, không chỉ tin nhắn.
4. **Committee/judge: hybrid + dừng sớm:** vote + judge-rank cứu câu đúng thiểu số (+7 điểm), majority thuần chọn sai 73%; dừng sau 1–2 vòng ([7][8]). → Copy: khi nhờ LLM chấm nhiều phương án, lấy top-2 theo vote rồi để judge xếp hạng lại, không chạy quá 2 vòng.
5. **Probe riêng tư cho debate:** agent công khai đồng thuận nhưng 51,6% giữ niềm tin sai riêng; 1–3 đối thủ đủ sụp hội thoại ([6][4]). → Copy: đừng tin "nhất trí" của nhóm agent; thu thập đánh giá riêng từng agent trước khi kết luận.

---
Nguồn: scans/2026-10-20.json (scan 05:11) + distill_queue.txt. Số liệu từ README.md từng paper trong papers/2026/10/20/. Bản quyền: mỗi paper giữ license gốc (phần lớn Apache-2.0/MIT — xem metadata.json từng paper).
