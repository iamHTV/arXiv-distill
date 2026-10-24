# Skill: Đánh giá tác tử thương mại tự trị qua benchmark môi trường mô phỏng (E-Commerce Bench)

Source: 2608.30730v1
Type: evaluation-method

## Khi nào dùng skill này

- Cần đánh giá tác tử AI cho vận hành thương mại, bán lẻ hoặc bất kỳ ứng dụng nào liên quan đến ra quyết định liên tiếp trên ngang dài với hậu quả tài chính.
- Muốn biết tác tử mạnh hay yếu ở từng chiều (lợi nhuận, đàm phán, tránh gian lận, dòng tiền, hiệu quả, thực thi, học tập) chứ không chỉ có một điểm số tổng hợp.
- Cần môi trường đánh giá deterministik cho cùng chuỗi hành động.

## Tình huống KHÔNG nên dùng

- Tác tử chỉ cần thực hiện các tác vụ ngắn hạn, có thể xác minh mà không cần quản lý vốn dài hạn hoặc thích ứng với sự kiện động.
- Không có dữ liệu thương mại thực hoặc có thể tổng hợp được.
- Không cần đánh giá chi phí tài chính của các quyết định tác tử.

## Input cần có

- Dữ liệu thương mại thực hoặc có thể tổng hợp từ nhật ký phân tích (danh mục sản phẩm, nhà cung cấp, lịch sử mua bán).
- Môi trường mô phỏng thị trường deterministik (nhà cung cấp, khách hàng, đối thủ hoạt động độc lập với tác tử).
- 18 công cụ làm văn phòng sau của thương nhân, chia 7 nhóm, mỗi công cụ tốn phút mô phỏng.
- Mô hình LLM backbone có khả năng gọi hàm và lập kế hoạch multi-bước.
- Bối cảnh 128,000 token với đào thải bám nhóm, không gian lưu trữ liên tục tối đa 20 mục.

## Các bước thực hiện

1. Thiết lập môi trường mô phỏng thương mại: 6,886 sản phẩm trong 60 danh mục, 576 nhà cung cấp (424 trung thành, 152 gian lận), 12 loại cửa hàng, tối đa 4 cửa hàng đồng thời.
2. Cung cấp 18 công cụ cho tác tử (mở cửa hàng, tìm kiếm nhà cung cấp, đàm phán giá, đặt hàng, định giá, giao hàng, dịch vụ khách hàng, tài chính).
3. Chạy sự kiện 365 ngày: tác tử khai báo trọng tâm cửa hàng, nhập kho, định giá, đáp lại khách hàng và nhà cung cấp, cải thiện ngày theo ngày.
4. Thu thập tài sản cuối năm (tài khoản ngân hàng + ví nền tảng + escrow chưa thanh toán), báo cáo dưới dạng hệ số so với vốn ¥100,000.
5. Tính chỉ số trên 7 chiều: chất lượng đàm phán (CSE+), tránh gian lận (BadSpend%), dòng tiền và khả năng thanh toán (drawdown trên đỉnh), hiệu quả vận hành (lợi nhuận trên mỗi lệnh gọi công cụ), thực thi vận hành (lãi suất trả hàng có thể kiểm soát), học theo ngang dài (AnchorRatio).
6. Thực hiện chap ngân sách: 10 ngày liên tiếp số dư ngân hàng âm dừng sự kiện.
7. Phân tích đa chiều: so sánh tác tử trên mỗi chiều chứ không chỉ điểm tổng hợp.

## Output mong đợi

- Một báo cáo đánh giá tác tử thương mại với tài sản cuối năm, hồ sơ đa chiều, và gán giá trị hành động.
- Nhận ra được tác tử mạnh hay yếu ở từng chiều kinh doanh.
- Cơ sở cho dữ liệu huấn luyện và học khích cường hóa trong tương lai.

## Ví dụ áp dụng

Solopreneur tại Việt Nam muốn đánh giá tác tử hỗ trợ bán hàng trực tuyến: tạo môi trường mô phỏng cửa hàng trên năm, tác tử phải nhập sản phẩm từ nhà cung cấp, đàm phán giá, định giá, giao hàng, xử lý trả hàng, quản lý dòng tiền. Chạy 5 sự kiện, đo tài sản cuối năm trung bình. Phân tích đa chiều cho thấy tác tử mạnh về lợi nhuận (14,3× vốn) nhưng yếu về tránh gian lận (xếp hạng 16/18). Học theo ngang dài cho thấy tác tử không giảm giá mua trên các lần đặt lại cùng nhà cung cấp.

## Gotchas

- Hệ số 1,264 giữa mô hình tốt nhất và kém nhất — không có mô hình nào thống trị mọi chiều.
- 10/90 sự kiện chap ngân sách — quản lý dòng tiền quan trọng như lợi nhuận.
- Một điểm số tổng hợp có thể che giấu điểm yếu quan trọng — cần phân tích đa chiều.
- Không có Limitations section rõ rệt trong paper (kết thúc tại Conclusion rồi sang References).
- Không đánh giá trên các mô hình nhỏ hơn, không đánh giá chi phí chạy benchmark, không đánh giá trên ngôn ngữ ngoài tiếng Trung.