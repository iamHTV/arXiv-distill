# [2610.25096v1] Toward Agentic Retrieval-Augmented Generation for Enterprise Retail Workflows over Heterogeneous Data Sources

## Giá trị cốt lõi (1 câu)

RetailRAG (khung tác tử RAG nhận thức bán lẻ) vượt tất cả 6 cơ sở RAG trên benchmark RetailBridge (1,680 truy vấn đa nguồn, 3 cấp độ phức tạp), đạt LLM-judge accuracy 0.429 trung bình so với 0.336 của cơ sở mạnh nhất (HetaRAG) và dùng ít hơn 3 lần calling API (7.45 vs 25.21).

## Problem

Prior work chưa giải quyết được đánh giá tác tử RAG cho quy trình bán lẻ doanh nghiệp (enterprise retail workflows), vì các agentic RAG hiện có hoạt động trên một tập đồng nhất (single homogeneous corpus), trong khi truy vấn bán lẻ thực tế lan truyền qua nhiều nguồn eściquelle (heterogeneous sources) kết hợp bảng có cấu trúc (structured tables) và văn bản không cấu trúc (unstructured text), yêu cầu tác tử định tuyến qua nguồn, kết nối bằng chứng tách biệt và tổng hợp câu trả lời cuối cùng.

## Contribution

(i) RetailBridge: benchmark đa nguồn bán lẻ đầu tiên, được xây dựng bằng cách mô phỏng tương tác người bán–người mua dựa trên nhân cách (persona-driven simulation) vào cơ sở dữ liệu bán lẻ doanh nghiệp đa dạng (heterogeneous), không bị ràng buộc về quyền riêng tư.
(ii) Ứng dụng tổng hợp QA thành phần (compositional QA synthesis pipeline): các toán tử liên kết thực thể (entity-linked) và liên kết đáp án (answer-linked) đệ quy sinh truy vấn bán lẻ đa nguồn, đa nhảy (multi-hop) trên 3 cấp độ độ phức tạp thành phần (Level-1 đến Level-3).
(iii) Xác thực đa cấp độ chất lượng benchmark và sự liên quan thực tế thông qua đánh giá con người (human review), đánh giá chuyên gia domaine bán lẻ, và so sánh với tập dữ liệu bán lẻ thực.
(iv) RetailRAG: khung tác tử RAG nhận thức bán lẻ đầu tiên, tích hợp tự động briefing lược đồ (auto-schema briefing), định tuyến kế hoạch theo nguồn (source-routed plan chaining), và sửa kế hoạch chẩn đoán (diagnostic plan revision).
(v) Benchmark toàn diện các cơ sở agentic RAG và LLM backbone đa dạng, phơi bày đa nguồn chaining (multi-source chaining) là Bottleneck (måg thắt cổ chai) cơ bản của tác tử bán lẻ LLM hiện tại.

## Method

Xây dựng RetailBridge qua 2 bước: (Bước 1) Tạo atomic QAs có thể trả lời từ một nguồn duy nhất: chọn bằng chứng từ một nguồn đơn, sinh câu hỏi và truy vấn tìm kiếm bằng LLM, xác thực qua 2 bộ lọc (executable verification: truy vấn phải chạy được trên nguồn; LLM verification: 2裁判 GPT-5.5 và Claude Opus 4.7 đồng ý câu hỏi và đáp án đúng). (Bước 2) Tích hợp đệ quy atomic QAs qua 2 toán tử: entity-linked composition (Oent) ẩn một thực thể đơn đằng sau cụm từ chỉ định, và answer-linked composition (Oans) ẩn một tập hoặc giá trị số đằng sau cụm từ chỉ định. Đệ quy dừng ở cấp độ tối đa L=3. Mọi truy vấn mang cấp độ suy luận, độ đa dạng nguồn và kiểu bằng chứng, phân tầng RetailBridge trên 3 chẩn đoán: khả năng suy luận (reasoning capability), đa nguồn chaining (multi-source chaining), kiểu bằng chứng (evidence modality).

RetailRAG có 3 thành phần: (i) Auto-schema briefing: kiểm định tự nhiên từng cột (numeric, categorical, free-text), LLM tổ chức thành 4 phần (tóm tắt lượcadro và siêu dữ liệu, ràng buộc giá trị phân loại, khóa căn chỉnh thực thể, chỉ số phân tích dẫn xuất) và chèn vào prompt của lập kế hoạch. (ii) Source-routed plan chaining: adaptive router đánh giá độ phức tạp truy vấn và định tuyến đơn giản trực tiếp đến một công cụ, giữ vòng lập kế hoạch cho đa nguồn; lập kế hoạch sinh toàn bộ chuỗi trong một lần đi, mỗi bước chỉ định nguồn và truy vấn tìm kiếm, các bước sau tham chiếu kết quả trước đó dưới dạng biến. (iii) Diagnostic plan revision: khi bước thất bại giữa chuỗi, chỉ sửa bước thất bại qua 2 giai đoạn (diagnose: LLM nhận diện lỗi từ tín hiệu thực thi và gán nguyên nhân kiểu; revision: LLM viết lại chỉ bước thất bại dựa trên nguyên nhân đã chẩn đoán).

## KNOWLEDGE — Số liệu & khái niệm

- Cơ sở dữ liệu bán lẻ đa dạng: 8 nguồn (5 bảng có cấu trúc TAB: 2 bảng danh mục sản phẩm và nhật ký đơn hàng, 3 bảng siêu dữ liệu quan hệ của kịch bản bán hàng, đánh giá và पूछत góp dịch vụ khách hàng; 3 bộ sưu tập văn bản TXT: kịch bản bán hàng, đánh giá,問答 dịch vụ khách hàng), được xây dựng từ mô phỏng tương tác người bán–người mua dựa trên nhân cách.
- RetailBridge: 1,680 truy vấn cuối cùng sau xác thực con người (3 chuyên gia NLP, Gwet's AC1 = 0.89), 3 cấp độ (Level-1, Level-2, Level-3), phân theoHomo/Hetero (nguồn đơn/nhiều nguồn) và SQL-only/Text-only/Composite.
- Xác thực chuyên gia domaine: 90% truy vấn được đánh giá là câu hỏi người bán sẽ hỏi thực tế (97.5% Level-1, 90.0% Level-2, 82.5% Level-3).
- RetailRAG (backbone gpt-oss-120b): LLM-judge accuracy 0.429 trung bình, Acc 0.298, 7.45 API calls/query.
- HetaRAG (cơ sở mạnh nhất): LLM-judge 0.336, Acc 0.212, 25.21 API calls.
- MAC-SQL: LLM-judge 0.263, Acc 0.175. TableRAG: 0.188. ReAct: 0.200. Dense RAG: 0.050. Text-to-SQL: 0.421 (chỉ Level-1).
- RetailRAG Level-3 Hetero: LLM-judge 0.302 vs HetaRAG 0.212 (cơ sở tốt nhất).
- Benchmark 10 LLM backbone: Qwen3.6-Plus 0.511, GPT-5.4 0.508, Gemma-4-31B-IT (mã nguồn mở) 0.498, DeepSeek-V4-Pro 0.466, GPT-oss-120B 0.429.
- Guru models chuyển khoảng 70% routing F1 thành đáp án đúng, còn mô hình yếu (Qwen3.6-35B-A3B) chuyển dưới 50%.
- Text retrieval là Bottleneck (mẫnt cổ chai) kiểu bằng chứng dominante; các mô hình suy yếu hơn nhiều trên truy vấn Text-only so với SQL-only.

## INSIGHT — Cơ chế & tại sao

[Đa nguồn chaining (multi-source chaining) là Bottleneck dominante]: hầu hết các cơ sở giảm mạnh từ Homo sang Hetero trong mỗi cấp độ, cho thấy việc kết nối bằng chứng qua nguồn thay vì truy xuất mỗi bước là yếu tố thất bại chính. Điều này nghĩa là việc mở rộng mô hình (scaling alone) không giải quyết được vấn đề; cần phối hợp đa nguồn rõ ràng (explicit cross-source orchestration).

[Auto-schema briefing và Plan Revision chiếm phần lớn giảm chênh lệch trung bình]: hai thành phần này đóng góp nhất, đặc biệt ở Level-2 nơi chuyển từ atomic sang multi-hop reasoning là đòi hỏi cao. Điều này nghĩa là hiểu lược đồ và khôi phục cục bộ từ lỗi là quan trọng hơn việc chỉ có khả năng lập kế hoạch.

[Plan Routing (định tuyến kế hoạch) cũng góp phần chất lượng đáp án]: việc bớt Plan Routing làm giảm độ chính xác trên mọi cấp độ, rõ nhất ở Level-1, cho thấy quyết định định tuyến bản thân đóng góp vào chất lượng đáp án ngoài vòng lập kế hoạch.

[Khả năng kết nối đa nguồn tăng theo quy mô mô hình]: các mô hình lớn hẹp hoặc thậm chí đảo ngược chênh lệch Homo/Hetero ở Level-3, trong khi các mô hình nhỏ vẫn dưới 0.30 trên truy vấn Hetero. Điều này nghĩa là khả năng kết nối đa nguồn là một năng lực tăng theo quy mô chứ không phải theo loại mô hình.

[Text retrieval là Bottleneck kiểu bằng chứng]: truy vấn Text-only suy yếu thấp nhất, xác định việc truy xuất văn bản đặc trưng là Bottleneck kiểu bằng chứng dominante bất kể loại mô hình hay quy mô.

## IDEA — Áp dụng được gì

Áp dụng [auto-schema briefing] vào việc xây dựng agent truy xuất dữ liệu doanh nghiệp cho solopreneur VN: trước khi để LLM lập kế hoạch truy vấn, hãy cung cấp bản tóm tắt lược dữ liệu (các bảng, cột, ràng buộc giá trị phân loại, khóa căn chỉnh thực thể, chỉ số phân tích) để LLM hiểu cấu trúc dữ liệu trước khi lập kế hoạch.

Áp dụng [diagnostic plan revision] vào việc xây dựng agent gọi hàm multi-bước: khi một bước trong chuỗi gọi hàm thất bại, hãy chỉ sửa bước thất bại thay vì bắt đầu lại từ đầu, giảm chi phí và giữ luồng bằng chứng gốc intact.

Áp dụng [source-routed plan chaining] vào việc xây dựng agent truy xuất đa nguồn: định tuyến từng bước kế hoạch đến nguồn dữ liệu phù hợp (bảng SQL hoặc văn bản) trước khi thực thi, giữ các bước trước đó intact và truyền giá trị trung gian dưới dạng biến.

## WISDOM — Nguyên tắc tổng quát

Nguyên tắc: Ph phối hợp đa nguồn rõ ràng (explicit cross-source orchestration) quan trọng hơn việc mở rộng mô hình (scaling alone) khi xây dựng tác tử truy xuất dữ liệu doanh nghiệp trên nhiều nguồn eściquelle.

Khi nào dùng: Khi cần xây dựng tác tử truy xuất dữ liệu doanh nghiệp trên nhiều nguồn dữ liệu khác nhau (bảng SQL, văn bản, API).

Khi nào KHÔNG dùng: Khi dữ liệu chỉ nằm ở một nguồn đơn nhất và truy vấn không cần kết nối bằng chứng qua nhiều nguồn.

Ví dụ áp dụng ngoài domain gốc: Xây dựng tác tử hỗ trợ quy trình y tế (healthcare) truy xuất từ hồ sơ bệnh ánElectronic Health Record (bảng có cấu trúc) và ghi chú bác sĩ (văn bản không cấu trúc) — cần định tuyến qua cả hai nguồn và kết nối bằng chứng.

## Assumptions & Limitations

- Điều kiện đúng: Có dữ liệu bán lẻ có thể mô phỏng được hoặc dữ liệu doanh nghiệp thực; có quyền truy cập vào các nguồn dữ liệu đa dạng (bảng SQL, văn bản); LLM backbone có thể gọi hàm và lập kế hoạch multi-bước.
- Limitation paper thừa nhận: Đánh giá chỉ bao gồm hồ sơ bán lẻ và các tác vụ đánh giá đã chỉ định; chuyển giao sang các domain khác, tái sử dụng tác vụ liên tiếp và ổn định dưới các bản viết lại bảo lưu ý nghĩa còn là hướng đánh giá trong tương lai. So sánh không tách biệt đóng góp của từng thành phần thiết kế.
- Limitation paper KHÔNG nói: Không có Limitations section rõ rệt trong paper (paper kết thúc tại Conclusion rồi sang References); không có đánh giá chi phí lưu trữ và bảo trì; không có đánh giá độ ổn định khi dữ liệu thay đổi theo thời gian.

## Metadata

- Năm: 2026
- Tác giả: Jeonghwan Choi, Jibin Hwang, Hayoon Park, Hyeonjae Cheon, Hwanjun Song
- Thể loại arXiv: cs.AI
- Link PDF: https://arxiv.org/pdf/2610.25096v1
- Số lượt trích dẫn: chưa có thông tin