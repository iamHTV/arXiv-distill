# Skill: grad-cir-graded-relevance-retrieval

Source: 2609.24152
Type: framework

## Khi nào dùng skill này

- Xây dựng hệ thống truy xuất hình ảnh kết hợp (composed image retrieval, CIR) cho thương mại điện tử.
- Muốn cải thiện khả năng xếp hạng các ứng viên khớp phần mẫu trong tìm kiếm trực quan.
- Có dữ liệu danh mục lớn và có thể dùng VLM để quản lý dữ liệu huấn luyện.

## Tình huống KHÔNG nên dùng

- Truy vấn chỉ có một đáp án đúng rõ ràng, không có khái niệm khớp phần mẫu.
- Không có VLM hoặc không thể chi phí chạy VLM để quản lý dữ liệu.

## Input cần có

- Dữ liệu danh mục sản phẩm (hình ảnh + mô tả).
- Cặp truy vấn-sản phẩm hiện có.
- VLM để tạo truy vấn và nhãn liên quan phân cấp.
- Mô hình retriever đa phương thức để huấn luyện.

## Các bước thực hiện

1. Dùng VLM để quản lý dữ liệu huấn luyện: tạo truy vấn (phát hiện đối tượng + tổng hợp sửa đổi) và nhãn liên quan 4 cấp từ dữ liệu danh mục thô, không cần chú thích thủ công.
2. Huấn luyện retriever đa phương thức trên nhãn liên quan phân cấp bằng mục tiêu góc có nhận thức phân cấp (hierarchy-aware angular objective).
3. Áp dụng vòng phản hồi liên quan lặp lại: khai thác hard negative từ retriever đang trong quá trình huấn luyện để mở rộng tập huấn luyện.
4. Lặp lại quá trình huấn luyện và mở rộng tập dữ liệu cho đến khi đạt mức hiệu suất mong muốn.
5. Đánh giá bằng NDCG@10 trên tập kiểm tra.

## Output mong đợi

- Retriever đa phương thức được huấn luyện trên nhãn liên quan phân cấp.
- Tập dữ liệu huấn luyện có nhãn liên quan 4 cấp.
- Mức độ cải thiện NDCG@10 so với huấn luyện trên nhãn nhị phân.

## Ví dụ áp dụng

Đội xây dựng hệ thống tìm kiếm trực quan cho sàn thương mại điện tử: thay vì chỉ gán nhãn "khớp/không khớp" cho cặp ảnh-sản phẩm, hãy dùng VLM để tạo nhãn liên quan 4 cấp (hoàn toàn khớp, khớp phần lớn, khớp một phần, không khớp). Huấn luyện retriever với Grad-CIR, đạt tăng 4,9%–5,9% NDCG@10 so với nhãn nhị phân.

## Gotchas

- Nhãn liên quan phân cấp giúp xếp hạng tốt hơn các ứng viên khớp phần mẫu.
- VLM tự động tạo dữ liệu giảm chi phí chú thích thủ công.
- Vòng phản hồi liên quan khai thác hard negative cải thiện retriever liên tục.
- Mục tiêu góc phân cấp huấn luyện trực tiếp trên nhãn phân cấp thay vì sụt noi thành nhị phân.