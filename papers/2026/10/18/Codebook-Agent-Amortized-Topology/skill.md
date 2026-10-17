# Skill: Thiết kế Topology Multi-Agent dựa trên Codebook

Source: 2609.02264v1
Type: framework

## Khi nào dùng skill này
- Bạn xây dựng hệ thống multi-agent LLM và muốn thiết kế topology giao tiếp tối ưu cho mỗi truy vấn.
- Bạn cần giảm chi phí token và tăng độ chính xác của hệ thống multi-agent.
- Bạn muốn tránh tìm kiếm lặp đi lặp lại vào thời điểm kiểm tra (inference time).

## Tình huống KHÔNG nên dùng
- Hệ thống chỉ có một agent (không cần multi-agent topology).
- Bạn không có dữ liệu huấn luyện để xây dựng codebook topology.

## Input cần có
- Bộ dữ liệu huấn luyện chứa các cặp (truy vấn, topology, tiện ích, chi phí token).
- Máy mã hóa câu đóng băng để nhúng truy vấn và hồ sơ agent.
- Mã hóa tự động vector-lượng (VQ autoencoder) để xây dựng codebook.
- MLP cho dự đoán mã và MLP proxy cho xếp hạng lại.

## Các bước thực hiện
1. Thu thập bản ghi thực thi: cho mỗi truy vấn, chạy các topology cố định (hoàn chỉnh, chuỗi, sao, và ba mẫu Erdos-Renyi) với agent LLM thực, ghi lại (topology, nhúng truy vấn, tiện ích, chi phí token).
2. Huấn luyện VQ autoencoder nén các topology thành công (tiện ích > 0.5) vào codebook 16 mục, độc lập với truy vấn.
3. Huấn luyện MLP dự đoán mã (pθ(k|c)) ánh xạ nhúng truy vấn sang phân phối trên các mã codebook, được trọng số phần thưởng.
4. Huấn luyện MLP proxy đọc ma trận kề đã làm phẳng, hồi quy trên tiện ích đo được và chi phí token chuẩn hóa theo tác vụ.
5. Vào thời điểm kiểm tra: giải mã các mã hàng đầu từ codebook, loại trùng lặp, chấm điểm bằng MLP proxy trong một lệnh gọi một lần, chọn ứng viên tối đa hóa ˆu − λˆc.

## Output mong đợi
- Một hệ thống chọn topology multi-agent tối ưu cho mỗi truy vấn.
- Độ chính xác cao hơn các phương pháp thiết kế topology trước đó.
- Thời gian phát ra topology rất ngắn (2,4 ms).
- Giảm chi phí token LLM 21,9–33,2%.

## Ví dụ áp dụng
Bạn xây dựng hệ thống multi-agent để giải quyết tác vụ mã hóa phức tạp. Thay vì để agent tự quyết định topology giao tiếp, bạn dùng Codebook Agent: trước khi chạy, hệ thống đã xây dựng một codebook 16 topology tốt nhất từ dữ liệu huấn luyện. Khi có truy vấn mới, hệ thống nhúng truy vấn, chọn phân phối trên các mã codebook, giải mã top M mã, chấm điểm bằng MLP proxy, và thực thi topology tốt nhất. Hệ thống đạt độ chính xác cao hơn và giảm 21,9–33,2% token so với các phương pháp thiết kế topology khác.

## Gotchas
- Số cạnh không phải là chỉ số chi phí tốt — số cạnh tương quan âm với token tiêu thụ, nên làm thinned đồ thị có thể làm suy luận tốn kém hơn.
- Máy chấm điểm message-passing không thể xếp hạng ứng viên khi các agent dùng chung hồ sơ (cấu hình mặc định của benchmark).
- Không gian thiết kế thực tế rất nhỏ (khoảng sáu đồ thị duy nhất), nên việc dung lượng codebook lớn không giúp ích nhiều.