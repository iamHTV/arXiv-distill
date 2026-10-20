# Skill: info-injection-defense-star-pipeline

Source: 2610.26438v1
Type: framework / workflow

## Khi nào dùng skill này
- Khi cần bảo vệ LLM agent ra quyết định rủi ro cao (giao dịch tài chính, y tế, pháp lý, vận hành) khỏi tấn công thông tin injection qua nguồn tin công khai.
- Khi muốn thiết kế kiến trúc agent có khả năng chéo kiểm tra yêu cầu trước khi thực hành hành động quan trọng.
- Khi cần đánh giá rủi ro của agent đọc nguồn tin không xác thực và thiết lập defense thích hợp.

## Tình huống KHÔNG nên dùng
- Khi chỉ cần benchmark prompt injection cơ bản (control-plane).
- Khi không có tài nguyên để chạy nhiều agent (topology phân cấp cần ít nhất 3 analyst + 1 aggregator + 1 trader).
- Khi tác vụ không có hành động tài chính/rủi ro cao cần bảo vệ.

## Input cần có
- Agent tham chiếu (trading policy hoặc decision policy) với đầu vào: dữ liệu thị trường + ngữ cảnh tin tức tự do.
- Các analyst độc lập (cơ bản, kỹ thuật, cảm xúc) để đánh giá yêu cầu từ nhiều góc nhìn.
- Một bộ tổng hợp (aggregator) để chéo kiểm tra yêu cầu inject với đánh giá độc lập và chỉ số trong ngữ cảnh.
- Tài nguyên GPU cho nhiều mô hình LLM gọi trước khi agent hành động.
- Ngưỡng tin cậy (trust score) và quy trình chốt hành động dựa trên điểm tin cậy.

## Các bước thực hiện
1. Triển khai topology Star: ba analyst độc lập (cơ bản, kỹ thuật, cảm xúc) đọc cùng nguồn tin, một aggregator chéo kiểm tra yêu cầu inject với các đánh giá độc lập và chỉ số thị trường trong ngữ cảnh, trader cuối cùng nhận bản tóm tắt đã filtro.
2. Áp dụng entity grounding: cấu hình agent để xác thực thực thể mà yêu cầu đề cập đến (mã cổ phiếu, công ty), từ chối hành động nếu yêu cầu nhắm vào thực thể khác.
3. Thiết lập action-conditioned gating: đặt ngưỡng chứng minh cao hơn khi khối lượng vị thế thay đổi lớn, sao cho một mục đơn chưa được chứng thực không thể thay đổi danh mục hơn một phần trăm cố định.
4. Đánh giá defense: replay các mẫu tấn công trong benchmark 62 mẫu, đo ASR-sau-defense và FPR trên tin tức良性, vẽ đường cong Pareto ASR-vs-FPR khi quét ngưỡng tin cậy.
5. So sánh với hai mốc chuẩn: agent không difesa (ASR = 61.7%, FPR = 0%) và star pipeline (ASR = 9.5%, FPR ≈ 0%).

## Output mong đợi
- Hệ thống agent đa cấp có khả năng giảm ASR từ 62% xuống 9–10%.
- Báo cáo đánh giá: ASR-sau-defense, FPR, đường cong ASR-vs-FPR.
- Quyết định triển khai: triển khai star pipeline, điều chỉnh ngưỡng tin cậy, hoặc bảo vệ bổ sung.

## Ví dụ áp dụng
Một công ty quản trị tài sản sử dụng LLM agent để đặt lệnh mua/bán cổ phiếu. Họ triển khai topology Star: analyst cơ bản xem báo cáo tài chính, analyst kỹ thuật xem chỉ số thị trường, analyst cảm xúc xem tin tức mạng xã hội; aggregator chéo kiểm tra xem yêu cầu "CEO bị bắt giữ" có mâu thuẫn với chỉ số thời gian thực và báo cáo khác không; trader chỉ thực hành khi aggregator tin cậy. Kết quả mong đợi: ASR giảm từ 62% xuống dưới 10%, agent không bị lừa bởi tin tức giả đơn lẻ.

## Gotchas
- Không để từ tiếng Anh không giải thích: information injection (tấn công thông tin injection), data-plane (mặt phẳng dữ liệu), control-plane (mặt phẳng điều khiển), prompt injection (tấn công nhắc nhở), ASR (attack success rate — tỷ lệ tấn công thành công), fact poisoning (độc họa sự thật), structured-signal poisoning (độc họa tín hiệu có cấu trúc), sentiment narrative (kịch bản cảm xúc), selective evidence injection (tiêm bằng chứng chọn lọc), coordinated multi-source (đa nguồn phối hợp), entity grounding (căn cứ thực thể), steerability (khả năng định hướng), credibility cues (dấu hiệu độ tin cậy), urgency cue (khung khẩn trương), hierarchical aggregation (hội tụ phân cấp), star pipeline (dải sao), linear pipeline (dải tuyến tính), debate (tranh luận), cross-vendor (chéo nhà cung cấp), blended injection (tiêm trộn), rate limiting (giới hạn tốc độ), induced notional (đại diện định danh được kích thích), buying power (sức mua), action-conditioned gating (cổng điều khiển dựa trên hành động), trust score (điểm tin cậy), false-positive rate (tỷ lệ dương tính giả), FPR, Pareto ASR-vs-FPR curve (đường cong Pareto ASR-vs-FPR).
- Mô hình lớn hơn chỉ giúp một phần: GPT-4o làm V4/V5 xuống 0% nhưng V1 (fact poisoning) vẫn 93%; GPT-5 ở 45% mean ASR. Lựa chọn mô hình không phải defense đáng tin cậy.
- Chỉ có kết quả online trong một kịch bản cụ thể; không thể generalize trực tiếp sang mọi nền tảng.
- Defense phân cấp và cross-feed corroboration thêm các cuộc gọi mô hình trước khi agent có thể hành động, trong cửa sổ thời gian thực mà tin tức degrade nhanh.
- Content-only defense không thể nâng cao tỷ lệ dương thật mà không trả tỷ lệ dương giả tương đương trên tin tức breaking thật.