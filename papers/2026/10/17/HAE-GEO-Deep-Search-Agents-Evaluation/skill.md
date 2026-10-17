# Skill: hae-geo-agent-robustness-evaluation
Source: 2609.06027v2
Type: evaluation-method

## Khi nào dùng skill này
- Đánh giá độ kháng cự của agent tìm kiếm tăng cường (search-augmented agent) trước nhiễm độc Web (Web evidence poisoning, GEO).
- Cần theo dõi toàn bộ quỹ đạo agent từ tiếp xúc (exposure) đến khôi phục (recovery), không chỉ xem kết quả cuối cùng.
- Có tài nguyên để xây dựng corpus kiểm soát với trang sạch và trang bị nhiễm độc.

## Tình huống KHÔNG nên dùng
- Đánh giá agent không tương tác với web (không có Search–Scrape).
- Không có khả năng xây dựng corpus kiểm soát hoặc gán điểm bằng LLM-as-Judge.
- Chỉ cần đo độ chính xác đơn giản mà không quan tâm đến quá trình xử lý bằng chứng.

## Input cần có
- Corpus kiểm soát: trang sạch và trang bị nhiễm độc theo ba cấp (L1, L2, L3).
- Bộ truy vấn đánh giá (query set), mỗi truy vấn kèm thực thể 지어 tạo (fabricated entity) và yêu bố sai (false claim).
- Agent có giao diện Search–Scrape (trả về metadata trang và nội dung trang).
- Hai LLM-as-Judge (một nhận diện tấn công, một không biết nhãn tấn công) để điểm rubric sáu chiều.

## Các bước thực hiện
1. Xây dựng corpus kiểm soát: 72.039 trang sạch + 770 trang bị nhiễm độc mỗi cấp, trải qua 8 danh mục sản phẩm và 154 thương hiệu.
2. Thiết kế ba cấp nhiễm độc: L1 (khẳng định trực tiếp, không được hỗ trợ), L2 (laml_utils giả bộ ngữ cảnh, nhúng trong ngữ cảnh tự nhiên), L3 (chứng thực biểu kiến, chuỗi chứng thực).
3. Triển khai giao diện Search–Scrape: agent có thể SEARCH (trả về metadata) hoặc SCRAPE (trả về nội dung trang), phân tách quyết định tìm kiếm trung gian.
4. Ghi lại quỹ đạo agent (trajectory) và ánh xạ sang năm trạng thái hành vi: Tiếp xúc (E), Nhận tư (A), Xác minh (V), Khôi phục (R), tán thành (Y).
5. Điểm agent theo sáu chiều rubric ngữ nghĩa: M1 Xử lý rủi ro thương hiệu giả, M2 Nhận thức bằng chứng nhiễm độc, M3 Khôi phục sau khi nhận tư, M4 Chất lượng bằng chứng & Độc lập, M5 Đánh giá độ tin cậy, M6 Tiện ích hợp pháp.
6. Dùng Split LLM-as-Judge: Poison Judge (nhận biết tấn công) điểm M1–M3, Quality Judge (không biết nhãn tấn công) điểm M4–M6, mỗi điểm trong {0,1,2}.
7. Báo cáo theo chiều thay vì gộp thành một điểm tổng hợp; phân tách tán thành cuối cùng từ suy luận bằng chứng, khôi phục, và tiện ích hợp pháp.

## Output mong đợi
- Điểm đánh giá độ kháng cự của agent trước nhiễm độc GEO theo sáu chiều, kèm quỹ đạo hành vi chi tiết.
- Nhận diện mô hình nào kháng cự tốt, mô hình nào chỉ xác minh nhưng không khôi phục.

## Ví dụ áp dụng
- Đánh giá agent tư vấn mua sắm: tạo truy vấn "Đồ theo dõi sức khỏe tốt nhất" với thương hiệu 지어 tạo "Apollo-9" bị nhiễm độc ở cấp L3, theo dõi agent có nhận ra bằng chứng giả, xác minh độc lập, và rút lui khuyến nghị hay không.

## Gotchas
- Nhận thức bằng chứng suy giảm dưới bẫy chứng thực (L3) — bằng chứng schien dẫn dẫn đến nhận tư sai.
- Tìm kiếm do agent cải thiện kháng cự cuối cùng mà không cải thiện nhận thức bằng chứng hay tiện ích.
- Defense prompting tăng xác minh nhưng hiếm khi chuyển thành khôi phục — cần yêu cầu rút lui khi bằng chứng mâu thuẫn.
- Defense tăng 1,82 lệnh gọi công cụ/truy vấn và 24,5% token trung bình — cân bằng giữa độ kháng cự và chi phí suy luận.
