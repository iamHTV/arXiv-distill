# 2608.18473 Khung đa agent LLM cục bộ cho phân tích và báo cáo phát thải methane

## Problem
Giám sát trường methane đòi hỏi tích hợp thiết kế lấy mẫu, diễn giải khí hậu, xử lý cảm biến, phân tích cột羽 (plume), trực quan hóa và báo cáo — nhưng các bước này thường được phân tán trong các quy trình chuyên gia riêng rẽ, đòi hỏi công sức thủ công lớn trước và sau đo đạc trường.

## Contribution
- Khung đa agent LLM cục bộ, dựa trên công cụ (tool-grounded — không trực tiếp ước lượng nồng độ methane, mà dùng agent LLM làm điều phối quy trình kết nối đo đạc trường, dữ liệu khí hậu, các thao tác xử lý cảm biến xác định (deterministic), ngả ngược cột羽 Gaussian, và tạo báo cáo).
- Đánh giá triển khai thực tế trên nhiều môi trường (trạm xử lý nước thải, khu rác thải, mặt bằng dầu khí): đạt 92.0% độ chính xác điều phối quy trình và trích xuất tham số, 85.0% thành công ước lượng tốc độ phát thải và dự báo cột羽, 95.0% thành công tạo báo cáo có thể chỉnh sửa.
- Giảm thời gian quy trình từ cấp giờ xuống cấp phút, giảm yêu cầu phối hợp thủ công và thiết kế lệnh nhắc (prompt engineering), giữ đầu ra cột feather có thể truy xuất (traceable plume-based outputs).
- Hầu hết xử lý cục bộ, giảm lộ thông tin cơ sở sở hữu và dữ liệu trường nhạy cảm đến dịch vụ đám mây.

## Method
Hệ thống tổ chức thành bốn lớp: lớp nhập dữ liệu (lệnh tự nhiên hoặc file CSV), lớp lập kế hoạch trutica (trích xuất thời gian, vị trí mục tiêu, loại cơ sở; lấy điều kiện khí khí tượng; ước kê khu vực dưới gió), lớp phân tích dữ liệu (truy xuất đo đạc methane qua MQTT hoặc CSV, tiền xử lý đơn vị/nền, mô hình cột feather Gaussian stead-state cho định vị nguồn và ước lực phát thải), lớp hỗ trợ quyết định và tạo báo cáo (Validity Agent đánh giá độ tin cậy, Report Generator Agent tạo báo cáo có thể chỉnh sửa).

Agent LLM không tính toán trực tiếp nồng độ methane; thay vào đó điều phối các thao tác xử lý cảm biến và mô hình vật lý cột feather, giữ kết quả định lượng có thể truy xuất và dựa trên vật lý.

Triển khai cục bộ trên trạm làm việc: Intel Core i9-13900KF (24 lõi), 64 GB RAM, NVIDIA GeForce RTX 4090 (24 GB VRAM), 3 TB SSD. Mô hình cục bộ qua Ollama: Llama 3.1 8B (tương tác chung, điều phối tác vụ), Qwen 30B (suy luận văn bản phức tạp), Qwen-VL 8B (diễn giải hình ảnh).

## KNOWLEDGE — Số liệu & khái niệm
- 92.0% độ chính xác điều phối quy trình và trích xuất tham số (trên 50 lệnh nhắc).
- 85.0% thành công ước lượng tốc độ phát thải và dự báo cột feather.
- 95.0% thành công tạo báo cáo có thể chỉnh sửa (20 trường hợp).
- Thời gian quy trình giảm từ cấp giờ xuống cấp phút (ví dụ lập kế hoạch trường: thủ công 30 phút, LLM chung 5–10 phút, AIMNet agent dưới 1 phút; xử lý và tạo báo cáo: thủ công 1–2 giờ, AIMNet agent dưới 15 phút).
- Điểm số báo cáo: chất lượng ngôn ngữ 9,3, trực quan hóa 9,2, định dạng báo cáo 8,4, trung bình tổng thể 9,0 (theo Gemini Judge, ChatGPT 5.5 Judge, và chuyên gia).
- Mô hình: Llama 3.1 8B, Qwen 30B, Qwen-VL 8B qua Ollama cục bộ.

## INSIGHT — Cơ chế & tại sao
[LLM dùng làm điều phối quy trình chứ không phải trực tiếp tính toán methane] xảy ra VÌ việc tách biệt điều phối (do LLM) và tính toán định lượng (do các thao tác xử lý cảm biến xác định + mô hình cột feather Gaussian) giữ kết quả định lượng có thể truy xuất và dựa trên vật lý, tránh LLM発行 các con số không có căn cứ. Điều này nghĩa là [khung kết nối các quy trình giám sát bị mảnh liệt thành một lớp điều phối bị ràng buộc (constrained coordination layer), không phải thay thế phân tích môi trường].
[Xử lý cục bộ] xảy ra VÌ dữ liệu giám sát methane có thể chứa thông tin nhạy cảm về cơ sở và vị trí, và truy cập Internet không tin cậy trong chiến dịch trường. Điều này nghĩa là [độ phơi bày dữ liệu nhạy cảm đến dịch vụ đám mây được giảm thiểu, phù hợp triển khai trường].

## IDEA — Áp dụng được gì
1. Áp dụng mô hình điều phối công cụ (tool-grounded coordination) vào hệ thống phân tích dữ liệu trường doanh nghiệp: bước đầu là xác định các thành phần xác định (deterministic routines) hiện có và để agent LLM điều phối thay vì thay thế chúng.
2. Áp dụng Validity Agent (đánh giá độ tin cậy) vào hệ thống báo cáo tự động: bước đầu là tính điểm số độ tin cậy từ các yếu tố chẩn đoán (RMSE, phạm vi GPS, số điểm cao, khoảng cách đến nguồn dự đoán, độ lớn tốc độ phát thải, độ tin cậy nguồn) và khuyến nghị lấy mẫu tiếp theo khi độ tin cậy thấp.

## WISDOM — Nguyên tắc tổng quát
Nguyên tắc: Trong hệ thống agent cho lĩnh vực định lượng (khoa học môi trường, phân tích doanh nghiệp), LLM nên điều phối chứ không phải thay thế các thao tác tính toán xác định — giữ kết quả có thể truy xuất và dựa trên nguyên lý. Khi nào dùng: khi cần tự động hóa quy trình đa bước có thành phần định lượng và dữ liệu nhạy cảm cần xử lý cục bộ. Khi nào KHÔNG: khi cần quyết định tự động cuối cùng mà không cần xem xét của con người, hoặc khi mô hình phân tán không phù hợp với môi trường (ví dụ cột feather Gaussian trong khu đông kết cấu).

## Assumptions & Limitations
- Định vị nguồn kém hơn trong môi trườngBuilt (cơ sở xử lý nước thải đạt chỉ 50%) do edifici, cây cối, cấu trúc cơ sở làm{gây làm}gại gió và chuyển vận cột feather.
- Kết quả nên được hiểu là thông tin hỗ trợ quyết định và được xác thực bằng đo đạc trường bổ sung, không phải quyết định tự động cuối cùng.
- Phụ thuộc vào chất lượng đo đạc và tính hợp lệ của mô hình phân tán dưới-jacent.
- Mã và dữ liệu sẽ được công bố công khai sau khi xuất bản (một số tọa độ cơ sở và thông tin nhận diện địa điểm không công bố do bảo mật).

## Metadata
- Năm 2026; tác giả: Yang Yan, Zifan Zhou, Xuan Wang, Erum Hassan, Bilguunzaya Mijiddorj, Jie Cao, Bin Li, Binbin Weng (University of Oklahoma, Pennsylvania State University); category: cs.MA; PDF: https://arxiv.org/pdf/2608.18473v1; citation count: [NO DATA — paper 2026-08-19]