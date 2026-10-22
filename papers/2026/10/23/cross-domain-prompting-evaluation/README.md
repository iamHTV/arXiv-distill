# 2610.24913 Đánh giá đa domain kỹ thuật nhắc LLM

## Problem
Các nghiên cứu hiện có về kỹ thuật nhắc (prompt engineering) thường đánh giá bằng các LLM, bộ dữ liệu, hoặc cài đặt khác nhau, làm khó so sánh trực tiếp giữa các phương pháp và domain. Không có đánh giá có chủ ý (controlled) đa domain sử dụng cùng một LLM và cài đặt thống nhất.

## Contribution
- Đánh giá có chủ ý đa domain của bốn kỹ thuật nhắc: Zero-Shot Prompting, Few-Shot Prompting, Retrieval-Augmented Generation (RAG), và tối ưu hóa nhắc tự động dựa trên PE2 — tất cả dùng cùng LLM (GPT-4o-mini) và được đánh giá trên sáu bộ dữ liệu đánh giá (benchmark) bao gồm lý tính số học, lý tính logic, tri thức phổ thông, và xác thực sự thật.
- Kết quả: Không có kỹ thuật nhắc nào luôn vượt trội hơn các kỹ thuật khác trên tất cả domain; không có sai số statiscally significant giữa cấu hình cao nhất và thứ hai (tất cả adjusted p-value = 1.000 sau điều chỉnh Holm).
- RAG đạt độ chính xác trung bình cao nhất 78.33% khi có 300 ví dụ truy xuất. Few-Shot đạt 77.83% với 200 ví dụ diễn tập. Zero-Shot đạt 90.0% trên BoolQ (cao nhất riêng lẻ). PE2 ổn định nhưng không hệ thống vượt trội (74.08%/74.25%/74.00% với 100/200/300 ví dụ tối ưu hóa).
- Tăng số lượng ví dụ theo nhiệm vụ không nhất quán cải thiện hiệu suất — chỉ ra sự phụ thuộc mạnh vào domain và nhiệm vụ.

## Method
Cấu hình thí nghiệm: Tất cả thí nghiệm dùng GPT-4o-mini qua OpenAI Chat Completions API, nhiệt độ (temperature) 0.0, mỗi instance đánh giá qua yêu cầu API riêng biệt (tránh rò rỉ ngữ cảnh). Đo lường bằng accuracy (tỷ lệ instance trả lời đúng).

Sáu bộ dữ liệu đánh giá: Elementary Math QA (lý tính số học), Logical Fallacy Detection (lý tính logic), Navigate (lý tính không gian và trừu tượng), BoolQ (trả lời câu hỏi đúng/sai và hiểu đọc), Social IQA (tri thức phổ thông xã hội), Fact Checker (xác thực sự thật). Mỗi bộ dùng 200 instance test liên tục trên mọi kỹ thuật nhắc. Các tập ví dụ diễn tập 100, 200, 300 dùng cho Few-Shot, RAG, và PE2.

Bốn kỹ thuật nhắc:
1. Zero-Shot: chỉ lệnh nhiệm vụ, không ví dụ diễn tập.
2. Few-Shot: thêm ví dụ diễn tập cố định vào ngữ cảnh nhắc (n = 100, 200, 300).
3. RAG: truy xuất tương ứng ngữ nghĩa (semantically relevant) ví dụ động từ nhóm ví dụ theo nhiệm vụ, k = 5 ví dụ được truy xuất cho mỗi instance, nhóm ví dụ 100/200/300. Dùng Azure AI Search với matching độ tương đồng nhúng (embedding-based similarity matching). RAG trong bài này là cường hóa ví dụ dựa trên truy xuất chứ không phải truy xuất từ cơ sở kiến thức bên ngoài.
4. PE2: tối ưu hóa nhắc tự động lặp lại, lấy ví dụ trả lời sai để tạo và chọn biến thể nhắc mới, giới hạn 3 vòng lặp, chiến lược chọn kiểu beam dựa trên accuracy tập xác nhận. Cả vai trò nhiệm vụ và vai trò đề xuất đều dùng GPT-4o-mini.

## KNOWLEDGE — Số liệu & khái niệm
- Không có kỹ thuật nhắc nào vượt trội nhất qua tất cả domain; không có sai số statistically significant giữa cấu hình cao nhất và thứ hai (tất cả adjusted p-value = 1.000, 8 so sánh đôi).
- RAG: trung bình cao nhất 78.33% (300 ví dụ), đạt cao nhất trên Elementary Math QA (66.0%) và Logical Fallacy Detection (85.5%).
- Few-Shot: trung bình cao nhất 77.83% (200 ví dụ diễn tập).
- Zero-Shot: cao nhất riêng lẻ trên BoolQ (90.0%), cạnh tranh trên các nhiệm vụ có đầu vào tự chứa (self-contained inputs).
- PE2: ổn định nhưng không vượt trội trung bình, đạt cao nhất trên Social IQA (79.0%).
- Tăng ví dụ từ 100→200 cải thiện Few-Shot nhẹ (76.92%→77.83%), 300 không cải thiện thêm; RAG cải thiện liên tục (75.75%→78.33% từ 100→300); PE2 ổn định (74.08/74.25/74.00).

## INSIGHT — Cơ chế & tại sao
[Không có kỹ thuật nhắc nào vượt trội trên tất cả domain] xảy ra VÌ hiệu quả của mỗi kỹ thuật phụ thuộc vào cấu trúc và đặc điểm của nhiệm vụ mục tiêu (ví dụ Zero-Shot thắng trên BoolQ vì thông tin cần thiết đã có sẵn trong instance đánh giá; Few-Shot/RAG thắng trên các nhiệm vụ lý tính có cấu trúc). Điều này nghĩa là [kỹ thuật nhắc nên được chọn thích ứng dựa trên đặc điểm nhiệm vụ chứ không coi là chiến lược tối ưu hóa áp dụng rộng rãi].
[Tăng số lượng ví dụ không nhất quán cải thiện hiệu suất] xảy ra VÌ hiệu quả của Few-Shot phụ thuộc không chỉ vào số lượng ví dụ mà còn vào sự liên quan và tương thích của chúng với nhiệm vụ; RAG có xu hướng escala tích cực hơn vì nhóm ví dụ lớn hơn tăng cơ hội truy xuất ví dụ liên quan. Điều này nghĩa là [cả lựa chọn kỹ thuật nhắc lẫn lượng thông tin ngữ cảnh nên được coi là quyết định thiết kế phụ thuộc vào nhiệm vụ chứ không phải mặc định cố định].

## IDEA — Áp dụng được gì
1. Áp dụng nguyên tắc đánh giá kỹ thuật nhắc trên nhiệm vụ mục tiêu trước khi chọn: bước đầu là chạy thử nghiệm nhỏ trên tập dữ liệu đại diện cho nhiệm vụ thực tế với các kỹ thuật Zero-Shot, Few-Shot, RAG và chọn kỹ thuật đạt kết quả tốt nhất thay vì chọn mặc định dựa trên độ phức tạp.
2. Áp dụng RAG với nhóm ví dụ lớn hơn cho nhiệm vụ lý tính có cấu trúc: bước đầu là xây dựng nhóm ví dụ theo nhiệm vụ (100–300 ví dụ) và dùng truy xuất tương ứng ngữ nghĩa (k=5) để cường hóa ví dụ diễn tập.

## WISDOM — Nguyên tắc tổng quát
Nguyên tắc: Hiệu quả của kỹ thuật nhắc phụ thuộc mạnh vào cấu trúc và domain của nhiệm vụ; không có kỹ thuật nào tối ưu hóa rộng rãi, nên đánh giá trên nhiệm vụ mục tiêu thay vì chọn dựa trên độ phức tạp. Khi nào dùng: khi cần chọn kỹ thuật nhắc cho hệ thống LLM-Based trên domain cụ thể. Khi nào KHÔNG: khi coi kỹ thuật nhắc phức tạp hơn luôn tốt hơn mà không đánh giá thực nghiệm.

## Assumptions & Limitations
- Chỉ dùng GPT-4o-mini, kết quả có thể không chuyển giao trực tiếp sang các kiến trúc và kích thước mô hình LLM khác.
- Chỉ sáu bộ dữ liệu đánh giá và 200 instance test mỗi bộ; tập đánh giá lớn hơn và domain bổ sung có thể cho kết quả mẫn bền hơn.
- Mỗi cấu hình chỉ đánh giá một lần cho mỗi instance (không tạo lại nhiều lần), temperature 0.0.
- Chỉ dùng accuracy làm chỉ số chung; không bắt nắm mô hình lỗi theo lớp hoặc sự khác biệt chất lượng về lý luận.
- RAG trong bài cường hóa ví dụ dựa trên truy xuất chứ không phải truy xuất từ cơ sở kiến thức bên ngoài.
- Triển khai PE2 được điều chỉnh riêng cho cài đặt thí nghiệm này.

## Metadata
- Năm 2026; tác giả: Kevin Krazius, Tim Schlippe, Paul Libbrecht (IU International University of Applied Sciences, Đức); category: cs.AI; PDF: https://arxiv.org/pdf/2610.24913v1; code: https://github.com/dieKrake/prompting-techniques; citation count: [NO DATA — paper 2026-10-17]