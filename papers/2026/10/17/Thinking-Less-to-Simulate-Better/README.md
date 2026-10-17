# [2609.30563v1] Thinking Less to Simulate Better: Intuitive Prompting Improves LLM Agents Simulating Individual Social Media Reactions, Including Unfamiliar Content

## Problem
- Các chính sách nền tảng ngày càng được kiểm tra trên người dùng nhân tạo (artificial users), khiến độ trung tín (agent fidelity) quan trọng. Tuy nhiên, việc xác thực tập trung vào sự đồng thuận với hành vi con người và ít quan tâm đến liệu agent có xử lý theo hồ sơ (profile) được cho hay không. Prior work chưa giải quyết được việc cách agent sử dụng hồ sơ quan trọng bằng như nội dung hồ sơ chứa gì hay không.

## Contribution
- Nghiên cứu profiling tám người tham gia Serbia thông qua questionnaire, phỏng vấn sâu (deep interview), và bản trình bày bản thân tự viết (written self-presentation); ghi lại phản ứng của họ đối với sáu mươi tám bài viết mạng xã hội; yêu cầu bốn ngôn ngữ mô hình (language model) dự đoán những phản ứng đó dưới năm điều kiện nhắc nhở (prompt conditions) thay đổi nội dung hồ sơ và kiểu hướng dẫn (instruction style).
- Nội dung thái độ (attitudinal content) cải thiện dự đoán hơn hẳn so với mô tả nhân khẩu học (demographic backstories). Agent khớp với hồ sơ đã khai báo (stated profiles) gấp gần chín lần so với người tham gia khớp với câu trả lời survey của chính mình.
- Hướng dẫn mô hình phản hồi trực quan và ngay lập tức thay vì phân tích thiết analy (intuitive prompting) cho độ trung tín (fidelity) cao nhất và cắt giảm nén các khác biệt cá nhân (compression of individual differences) từ bảy lần mức con người xuống ba lần.

## Method (tóm tắt cốt lõi)
- Thiết kế kết hợp một nhóm chất lượng nhỏ (qualitative panel) với thí nghiệm tính toán nhân tố (factorial computational experiment). Những người tham gia được profil chuyên sâu và ghi lại phản ứng của họ đối với một bộ bài viết mạng xã hội cố định, sau đó bốn ngôn ngữ mô hình dự đoán những phản ứng giống hệt đó dưới năm điều kiện nhắc nhở.
- Tám người lớn sống ở Serbia, độ tuổi từ 22 đến 53, trung bình 31.0 năm, năm người nữ và ba người nam.
- Sáu mươi tám bài viết bằng tiếng Serbia tạo thành tập nhắc nhở (stimulus set). Ba mươi bốn bài viết về chủ đề được bao gồm trong questionnaire và ba mươi bốn bài viết về chủ đề questionnaire chưa nhắc tới, cho phép tách biệt dự đoán trong miền (in-domain) và ngoài miền (out-of-domain).
- Bốn ngôn ngữ mô hình: Claude Sonnet 5, DeepSeek Instant, GPT 5.6 Terra, Grok Fast. Mỗi mô hình nhận mỗi hồ sơ người tham gia dưới năm điều kiện nhắc nhở, mỗi điều kiện yêu cầu một phán quyết like hoặc dislike trên tất cả sáu mươi tám bài viết được trả về theo định dạng comma-separated cố định.
- Năm điều kiện tạo thành một thang thang (ladder) thay đổi nội dung hồ sơ ở ba cấp đầu tiên và kiểu hướng dẫn ở hai cấp cuối: V4 demographics (tuổi, giới tính, học vấn, tình trạng việc làm, thành phố ở), V3 questionnaire (thêm toàn bộ questionnaire bao gồm pin độ tin cậy, các mục nhân vật, danh sách hoạt động, và vị trí chính trị tự định vị), V1 interview (thêm phỏng vấn transcripts và bản trình bày bản thân tự viết — hồ sơ giàu nhất), V2 inference (nội dung như V1 cộng với hướng dẫn suy luận phản ứng từ sự kết hợp các đặc điểm khi thuộc tính trực tiếp liên quan bị vắng), V5 intuitive (nội dung như V1 nhưng hướng dẫn mô hình phản hồi ngay lập tức thay vì phân tích thiết analy, tránh cân nhắc các đặc điểm lẫn nhau, và chấp nhận rằng một số phản ứng sẽ mâu thuẫn với hồ sơ đã khai báo).
- Kết quả sáng tạo hai mươi cấu hình (configuration) và 10.880 phản ứng được dự đoán.
- Độ trung tín (fidelity) là sự đồng thuận giữa dự đoán của agent và phản ứng thực tế của người tham gia. Matthews correlation coefficient (MCC) là thước đo chính.

## Key Findings
- 6 tác giả từ các cơ quan khác nhau (Institut za Istrazivanje i Razvoj Veštačke Inteligencije Srbije, Đại học Belgrade, Đại học Vienna, Universitas Negeri Padang, Đại học Novi Sad, Đại học Nanyang Technological), category arXiv: cs.AI, cs.CL, cs.HC, cs.MA, cs.SI.
- Mỗi một trong hai mươi cấu hình dự đoán phản ứng cá nhân trên ngưỡng ngẫu nhiên, MCC từ 0.275 (Claude Sonnet 5 với demographics đơn thuần) đến 0.511 (Grok Fast dưới điều kiện interview và intuitive).
- Độ trung tín leo từ điều kiện demographics đến điều kiện questionnaire, tăng thêm một chút hơn từ tài liệu phỏng vấn, giữ nguyên khi thêm hướng dẫn suy luận, và đạt giá trị cao nhất dưới khung cảnh trực quan (intuitive framing).
- V4 demographics: MCC 0.300, Accuracy 0.650, Consistency 0.541, Compression 10.24×
- V3 questionnaire: MCC 0.406, Accuracy 0.703, Consistency 0.870, Compression 7.54×
- V1 + interview: MCC 0.434
- V2 + inference: MCC 0.434
- V5 intuitive: MCC 0.473 (cao nhất)
- Human panel: Consistency 0.717, Between-person SD 0.294, Compression 1.00×
- Nén các khác biệt cá nhân: demographics 10.24×, questionnaire 7.54×, interview 7.14×, inference 7.88×, intuitive 3.14×, human 1.00×
- Điều kiện suy luận (inference) không cải thiện độ trung tín. Trung bình hiệu suất dưới điều kiện đó khớp chính xác với điều kiện phỏng vấn ở 0.434, trong khi độ nhất quán với hồ sơ (profile-consistency) tăng từ 0.754 lên 0.826.
- Hướng dẫn các mô hình phản hồi ngay lập tức thay vì phân tích thiết analy tạo ra độ trung tín trung bình cao nhất của mọi điều kiện và kết quả tốt nhất cho ba mô hình ra bốn.

## Actionable Insights
1. Nội dung thái độ (attitudinal content) cải thiện dự đoán hơn hẳn so với mô tả nhân khẩu học (demographic backstories). Áp dụng: khi xây dựng agent mô phỏng người dùng, thu thập nội dung thái độ (niềm tin, giá trị, ý kiến) thay vì chỉ thông tin nhân khẩu học.
2. Yêu cầu agent phản hồi ngay lập tức thay vì phân tích thiết analy (intuitive prompting) cho độ trung tín cao nhất. Áp dụng: hướng dẫn agent "trả lời ngay, không cân nhắc các đặc điểm lẫn nhau" khi mô phỏng phản hồi của người dùng trên mạng xã hội.

## Assumptions & Limitations
- Tám người tham gia chỉ hỗ trợ các tuyên bố về những gì xảy ra trong một thiết kế hồ sơ giàu (rich-profile design). Các tuyên bố về tham số dân số (population parameters) sẽ cần một nghiên cứu khác.
- Thử nghiệm cấp mô hình (model-level tests) trên bốn mô hình không thể đạt ý nghĩa thống kê theo quy tắc Wilcoxon, bất kể kích thước hiệu ứng. Bằng chứng cho sự khác biệt giữa các điều kiện do đó dựa trên các so sánh ở cấp mục (item-level) coi 544 ô agent-bài viết (agent-post cells) như các quan sát.
- Tất cả người tham gia sống ở Serbia, trong khi các mô hình được biết đến là đại diện cho công chúng phương Tây giàu có chính xác hơn. Hiệu suất báo cáo ở đây có thể sott-estimate những gì các thiết kế tương tự sẽ đạt được ở nơi khác.
- Mỗi cấu hình chỉ chạy một lần, phản ứng được rút gọn thành một lựa chọn nhị phân, và hai mô hình bị loại trừ vì đầu ra của chúng không hoàn chỉnh.

## Metadata
- Năm: 2026, tác giả: Ljubisa Bojic, Tijana Stanic, Jörg Matthes, Agariadne Dwinggo Samala, Bojana Dinic, Jue Wang, category arXiv: cs.AI, link PDF: https://arxiv.org/pdf/2609.30563v1
