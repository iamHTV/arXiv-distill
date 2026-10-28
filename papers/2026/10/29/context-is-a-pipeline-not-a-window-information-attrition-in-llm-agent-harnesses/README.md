# 2610.36114 Context Is a Pipeline, Not a Window: Information Attrition in LLM Agent Harnesses

## Giá trị cốt lõi (1 câu)
Agent harness (máy bọc agent) cắt tool output (kết quả công cụ) theo vị trí ký tự, không theo giá trị, nên bằng chứng quan trọng bị xóa hoàn toàn trong khi context window (cửa sổ ngữ cảnh) vẫn trống 93% — hãy đo loss (mất mát) tại mỗi ranh giới (boundary) của pipeline (ống truyền), không chỉ đo accuracy (độ chính xác).

## Problem
Prior work tập trung vào kích thước context window và cách model attention (chú ý) bên trong nó, hoặc cách mở rộng bằng memory (bộ nhớ). Nhưng gap thực tế là: giữa tool sinh ra kết quả và model đọc nó, harness (máy bọc agent) serialize (chuỗi hóa), cắt theo ngân sách, giữ/bỏ phần qua các lượt (turn), và truyền qua các giai đoạn. Mỗi bước là một lựa chọn thiết kế và mỗi bước có thể mất thông tin. Run log chỉ ghi lại tool đã giao giao, không phải tool đã sản xuất — nên một sự mất mát trên đường vào log không thể tìm thấy trong log. Không có nghiên cứu trước đo thất bại đo lường được tại từng ranh giới của đường đi này.

## Contribution
- Mô hình hóa context của agent như một 5-stage pipeline (5 giai đoạn ống truyền), với một thất bại đo lường được tại mỗi giai đoạn, và một công cụ đo: số liệu theo từng giai đoạn + một số yield (tỷ suất kết quả/công suất), áp dụng vào harness của riêng họ (Sec. II).
- Replay bằng chứng (replay evidence), bao gồm một trường hợp cắt đã được cung cấp (shipped cut) xóa toàn bộ một lớp bằng chứng tại quy mô sản xuất (Sec. III).
- Thử nghiệm kiểm soát (controlled experiment) đăng ký trước (registered): kết quả là một bồi thường thu (compensation tax) — khi agent có đường khác để đến câu trả lời, cắt dữ liệu khiến nó tốn thêm công việc, không phải sai câu trả lời (Sec. IV).
- Khảo sát 7 agent framework (khung làm việc agent): 2 framework cắt tool output theo cách không an toàn tương tự, phần còn lại không có thay thế an toàn nhất quán (Sec. III).

## Method (tóm tắt cốt lõi)
Ý tưởng cốt lõi: mô hình hóa đường đi của thông tin từ tool đến model như năm ranh giới (boundary) liên tiếp:
- S1 produce → deliver: tool sinh ra kết quả, harness chuyển thành văn bản và ép vào ngân sách trước khi model đọc.
- S2 deliver → act: nhân viên (worker) nhận được dữ liệu, hành động theo đó lượt mỗi lượt.
- S3 act → retain: nhân viên giữ lại chỉ một phần lịch sử đối thoại trước khi các lượt cũ bị bỏ (drop).
- S4 retain → transfer: một nhân viên tính toán xong phải bàn giao cho người viết phán đoán cuối cùng; nếu không, tính toán đó bị mất dù đã xảy ra.
- S5 transfer → persist: không có gì mang sang lần chạy tiếp theo (tắt bằng thiết kế để giữ các lần chạy độc lập).

S1 và S4 phá bo bằng chứng trực tiếp (một kết quả hoặc phát hiện đơn giản biến mất); S2 cắt một nhân viên trước khi kết thúc nên một số công việc không bao giờ xảy ra; S3 chỉ làm cho một lần chạy tốn kém hơn bằng cách gửi lại lịch sử không cần thiết; S5 vắng mặt trong thiết lập của họ nhưng là một lựa chọn, không phải thất bại. Họ báo cáo yield = số phát hiện ghi nhận chia cho số tính toán chạy, một chỉ số hẹp đo lường "công việc đã đến quyết định", không phải mức độ liên quan.

## KNOWLEDGE — Số liệu & khái niệm
- Trên 720 lần chạy, kích thước prompt lớn nhất chỉ 23k token, so với cửa sổ 400k = 5.75% (window hầu như trống).
- 3,827 trên 11,189 tool result (kết quả công cụ) bị cắt trước khi đến model (34%), và mọi kết quả bị cắt đều thành JSON hỏng (JavaScript Object Notation - định dạng trao đổi dữ liệu).
- Một trường (field) trong payload đạt model chỉ 4.7% trong 742 cuộc gọi; trường thứ hai, nằm ngay cạnh trong cùng payload, đạt model 99.3% cuộc gọi.
- Độ chính xác chẩn đoán (diagnosis accuracy): lỗi sinh ra quá trình mới (spawned fault) đạt 40–55/60; lỗi ở container đang chạy (resident fault) đạt 0–24/60.
- Thử nghiệm kiểm soát: từ repaired → S1 defect → S1 reversed, số tool call tăng 53 → 68 → 76 (+28%, rồi +43%), tính toán tăng 18 → 32 → 36 (gấp gần đôi), yield giảm 0.61 → 0.34 → 0.31.
- 7 agent framework được khảo sát: langchain-core 1.6.12, langchain 1.4.6, smolagents 1.26.0, openai-agents 0.24.0, autogen-agentchat 0.7.5, pyautogen 0.10.0, crewai 0.11.2. Hai cắt không an toàn (langchain-core cắt serialized tool output xuống 500 ký tự, giữ phần trước; smolagents xóa phần giữa của mọi observation trên 20k ký tự). Ba không cắt tool output. Một chỉ cắt dữ liệu truy vết (tracing data) của chính mình. Một là cắt theo cấu trúc (structure-aware): phần mềm trung gian shell cắt theo toàn bộ dòng và tuyên bố điều đó.
- Replay 864 kết quả đã ghi nhận từ 31 lần chạy: mọi kết quả vượt ngân sách đều vỡ dưới cắt tiền tố (prefix slice), mỗi lần; không một cái nào vỡ dưới cắt theo dòng (row-aware cut). 50% cuộc gọi liệt kê quá trình (process-listing) vỡ, cùng 43% phân tích của chính agent và 1% tóm tắt nhỏ. Chỉ 2.5% tất cả cuộc gọi bị ảnh hưởng.

## INSIGHT — Cơ chế & tại sao
- [Agent chẩn đoán sai lỗi ở container đang chạy] xảy ra VÌ [harness cắt payload theo vị trí ký tự, không theo giá trị, nên bằng chứng nằm ở cuối payload bị xóa hoàn toàn trong khi trường đầu tiên vẫn intact (không bị ảnh hưởng)]. Điều này nghĩa là [sai sót có thể nằm ở harness chứ không phải model, và accuracy đơn lẻ không phát hiện được sự suy kém này].
- [Cắt dữ liệu chỉ làm tăng công việc, không gây sai câu trả lời ngay] xảy ra VÌ [khi agent có đường khác để đến câu trả lời, nó truy tìm bằng cách khác, nên tổn thất xuất hiện trước là công việc dư thừa, rồi mới là sai sót]. Điều này nghĩa là [thử nghiệm chấm điểm bằng accuracy đơn lẻ sẽ bỏ lỡ lỗi harness; cần đo yield và số công cụ gọi].
- Điều kiện: insight này chỉ đúng khi agent có đường tiếp cận thay thế. Với quiet culprit (nguyên nhân im lặng — chỉ có một bằng chứng, không có đường thay thế), cắt dữ liệu gây sai sót chắc chắn (ví dụ resident fault đạt 0–24/60).

## IDEA — Áp dụng được gì
1. Áp dụng kiểm tra cắt output harness vào hệ thống agent của riêng bạn: bước đầu là instrument (cài đặt công cụ đo) mỗi ranh giới pipeline (S1–S5), đếm số bằng chứng đã đến so với số đã sản xuất, và báo cáo yield bên cạnh accuracy trên mọi bản đánh giá agent.
2. Áp dụng thiết kế cắt theo cấu trúc (structure-aware cut) thay vì cắt theo ký tự: bước đầu là thay đổi hàm cắt tool output trong langchain/smolagents bạn dùng để cắt theo dòng hoặc theo trường JSON thay vì cắt prefix (tiền tố) cố định.
3. Áp dụng quy tắc "không cắt nếu không thể phân tích cấu trúc": bước đầu là trước khi triển khai agent production, chạy replay trên 864 kết quả tool thực tế (hoặc corpus của riêng bạn) qua cả hai quy tắc cắt (tiền tố và theo dòng) để xem bằng chứng nào biến mất.

## WISDOM — Nguyên tắc tổng quát
- Nguyên tắc: "Context không phải cửa sổ, là đầu ra của ống truyền — hãy đo loss tại mỗi ranh giới, không chỉ đo accuracy." Khi nào dùng: khi đánh giá hoặc thiết kế hệ thống LLM agent sử dụng tool. Khi nào KHÔNG dùng: khi hệ thống không có tool use hoặc không chạy qua agent harness.
- Ví dụ áp dụng ngoài domain gốc: CI log (nhật ký tích hợp liên tục) bị cắt trước khi developer đọc gây ra tình trạng bỏ lỡ lỗi build — tương tự, hãy đo log còn lại so với log đã sinh ra, không chỉ coi build pass/fail là đủ.

## Assumptions & Limitations
- Điều kiện phải đúng để method work: agent phải chạy qua một harness (máy bọc) có quyền kiểm soát dữ liệu tool trước khi truyền đến model; tool output phải có cấu trúc (JSON/dòng) để cắt theo cấu trúc có ý nghĩa.
- Limitation paper thừa nhận: một harness duy nhất, một miền duy nhất (kernel traces), một model duy nhất; chưa đo các harness khác end-to-end, chưa đo agent build-test-fix truyền thống; thử nghiệm tái tạo lỗi do chính họ viết chứ không phải câu chuyện sửa chữa; 5 bản ghi mỗi lớp với lặp lại của cùng 5 bản ghi chứ không phải 5 trường hợp lỗi độc lập; sự tách rời độ chính xác trong dữ liệu thực vẫn là tương quan (correlation), không phải nhân quả (cause).
- Limitation paper KHÔNG nói: chưa xét ảnh hưởng của cắt dữ liệu lên chi phí latency (trì hoãn) từ cuối đến cuối, chỉ nhắc đến "extra tokens are unnecessary inference cost that will not show up in end-to-end latency" nhưng chưa đo số thực; chưa đánh giá phân tích ảnh hưởng của việc cắt trên nhiều mô hình khác nhau cùng lúc (chỉ temperature 0).

## Metadata
- Năm: 2026 | Tác giả: Yuvraj Sehgal (Brock University), Mahsa Panahandeh (University of Ottawa), Naser Ezzati-Jivan (Brock University)
- Category arXiv: cs.SE (Computer Science - Software Engineering)
- Link PDF: https://arxiv.org/pdf/2610.36114v1
- Link abstract: https://arxiv.org/abs/2610.36114
- Replication package: https://doi.org/10.5281/zenodo.23614755
- Citation count: [không tìm được]
