# [2609.02264v1] Codebook Agent: Amortized Topology Design for LLM Multi-Agent Systems

## Problem
Thiết kế giao tiếp (communication topology) của hệ thống multi-agent LLM cho mỗi truy vấn cải thiện cả độ chính xác và hiệu quả, nhưng các thiết kế hiện đại coi đây là tạo đồ thị có điều kiện (conditional graph generation): một decoder biến thiên, tự hồi quy, hoặc diffusion tìm trong không gian ma trận kề N×N, và một mạng proxy được huấn luyện trên tiện ích và chi phí cấu trúc (số cạnh) xếp hạng các ứng viên lấy mẫu. Ba vấn đề: (1) các topology tồn tại sau bộ lọc phần thưởng coentrência xuống khoảng sáu đồ thị riêng biệt ngay cả khi dung lượng codebook tăng từ 8 lên 64; (2) số cạnh tương quan âm với tiêu thụ token đo được (Pearson r ≈ -0.4), nên làm thinned đồ thị làm suy luận tốn kém hơn; (3) một máy chấm điểm message-passing trên các nút hồ sơ agent là không phụ thuộc vào ma trận kề khi các agent dùng chung hồ sơ — cấu hình mặc định của các benchmark công khai — nên nó không thể xếp hạng ứng viên nào trong regime đó.

## Contribution
- Giới thiệu Codebook Agent: một mã hóa tự động vector-lượng (vector-quantized autoencoder) nén các topology thành công vào một codebook độc lập với truy vấn gồm 16 mục; một MLP được trọng số phần thưởng ánh xạ nhúng truy vấn sang phân phối trên các mã; và một MLP proxy đọc ma trận kề đã làm phẳng, hồi quy trên tiện ích đo được và chi phí token chuẩn hóa theo tác vụ, xếp hạng lại các ứng viên được giải mã hàng đầu trong một bước tiến một lần (single batched forward pass).
- Không có tìm kiếm lặp đi lặp lại và không có message passing vào thời điểm kiểm tra, Codebook Agent là phương pháp chính xác nhất trên tất cả sáu benchmark so sánh (84.6 trung bình so với 83.0 cho thiết kế mạnh nhất trước đó), phát ra một topology trong 2,4 ms, và sử dụng ít hơn 21,9–33,2% token LLM.

## Method
- Axis A (máy sinh ứng viên): Codebook Agent tạo ra một codebook rời rạc với tiền chứng có điều kiện truy vấn. Máy mã hóa tự động vector-lượng nén các topology được quan sát: làm phẳng các mục ngoài đường chéo a = vec(A) ∈ {0,1}N(N-1), mã hóa ze = Encψ(a) ∈ Rdz, tìm mã k⋆ = arg min ||ze − ek||2, giải mã zq = ek⋆. Kích thước codebook K = 16, dz = 32. Codebook được cập nhật bằng trung bình động lũy thừa (decay 0.99), hệ số cam kết β = 0.25, gradient thẳng qua, và khởi tạo lại mã không dùng trong 50 batch. Huấn luyện chỉ trên các bản ghi có uj > 0.5 (topology giải quyết tác vụ). Không encoder hay decoder nào được điều kiện trên truy vấn; sau khi huấn luyện, mã k giải mã thành ma trận nhị phân A(k), và toàn bộ sự phụ thuộc vào truy vấn được chuyển cho predictor dưới đây.
- Axis B (máy chấm điểm): Một MLP dự đoán mã pθ(k | c) được.fit vào các mục tiêu mềm có trọng số phần thưởng. Một MLP proxy fϕ đọc ma trận kề đã làm phẳng và được hồi quy trên tiện ích đo được và chi phí token chuẩn hóa theo tác vụ. Vào thời điểm kiểm tra, các mã hàng đầu M được giải mã, loại trùng lặp, và được chấm điểm trong một lệnh gọi proxy một lần; ứng viên tối đa hóa ˆu − λˆc được thực thi.
- Thiết lập vấn đề: Nhóm N agent có hồ sơ văn bản p1,...,pN được nhúng thành xi = E(pi) ∈ Rd bởi máy mã hóa câu đóng băng (d = 384). Một topology là ma trận kề có hướng A ∈ {0,1}N×N không có vòng tự. Thực thi nhóm trên truy vấn q dưới A trả về tiện ích u(A,q) ∈ {0,1} và chi phí token τ(A,q). Mục tiêu là máy sinh ánh xạ c = E(q) sang topology tối đa hóa R = u − λ˜τ với ˜τ là chi phí chuẩn hóa và λ = 0.1.

## Key Findings
- Codebook Agent đạt 84.6 điểm trung bình trên sáu benchmark, vượt qua 83.0 của thiết kế mạnh nhất trước đó.
- Phát ra topology trong 2,4 ms (so với 301–396 ms cho các phương pháp lặp đi lặp lại).
- Giảm tiêu thụ token LLM 21,9–33,2%.
- Không cần tìm kiếm lặp đi lặp lại và không cần message passing vào thời điểm kiểm tra.
- Không gian thiết kế thực tế rất nhỏ: chỉ khoảng sáu đồ thị riêng biệt tồn tại sau bộ lọc phần thưởng.

## Actionable Insights
1. Không gian thiết kế topology thực tế rất nhỏ — chỉ khoảng sáu đồ thị duy nhất tồn tại sau lọc phần thưởng. Áp dụng: thay vì tìm kiếm liên tục trong không gian ma trận kề, hãy xây dựng một codebook các topology tốt nhất và chọn từ danh sách ngắn này. Bước đầu: Thu thập các topology thành công từ các tác vụ huấn luyện, nhóm chúng thành các nhóm tương tự, và chọn đại diện cho từng nhóm.
2. Số cạnh không phải là chỉ số chi phí tốt — số cạnh tương quan âm với token tiêu thụ (r ≈ -0.4), nên làm thinned đồ thị có thể làm suy luận tốn kém hơn. Áp dụng: khi thiết kế topology, hãy sử dụng chi phí token đo được thay vì số cạnh làm mục tiêu chi phí. Bước đầu: Đo số token thực tế cho mỗi cấu hình topology và dùng số đó làm mục tiêu tối ưu.
3. Không cần tìm kiếm lặp đi lặp lại vào thời điểm kiểm tra — chọn từ codebook trước đã tính toán. Áp dụng: khi triển khai multi-agent hệ thống, hãy huấn luyện một codebook topology ngoại tuyến và chỉ chọn từ codebook vào thời điểm chạy. Bước đầu: Xây dựng một hệ thống chọn topology từ codebook dựa trên nhúng truy vấn.

## Assumptions & Limitations
- Đánh giá trên sáu benchmark với hai LLM backend, có thể khác trên các tác vụ/domain khác.
- Chỉ đánh giá với các agent dùng chung hồ sơ (homogeneous teams), có thể khác trên các đội heterogeneous teams.
- Codebook có kích thước cố định 16 mục, có thể không đủ cho các tác vụ rất phức tạp.
- Không so sánh với tất cả các phương pháp thiết kế topology hiện có.

## Metadata
- Năm: 2026, tác giả: Jinxi Yu, Yubei Li, Eric Hanchen Jiang, Zhi Zhang, Dong Liu, Wenxiao Zhao, Levina Li, Kai-Wei Chang, Ying Nian Wu (University of California, Los Angeles), category arXiv: cs.AI, link PDF: https://arxiv.org/pdf/2609.02264v1