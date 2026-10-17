# Skill: avri-vulnerability-reasoning-interface
Source: 2610.11602v1
Type: framework

## Khi nào dùng skill này
- Xây dựng agent khám phá lỗ hổng (vulnerability discovery agent) cần giảm chi phí token và thời gian mà không làm suy giảm thành công (success) và nhớ lại (recall).
- Agent chạy lâu, tiêu thụ hàng triệu token, cần tái sử dụng bằng chứng (evidence) thay vì liên tục truy xuất và tái cấu trúc lại.
- Có thể truy cập mã nguồn kho lưu trữ và công cụ phân tích (gdb, radare2, strace, objdump).

## Tình huống KHÔNG nên dùng
- Khám phá lỗ hổng không cần truy cập mã nguồn (ví dụ: chỉ phân tích nhị phân).
- Không cần giảm chi phí suy luận, chỉ quan tâm đến tỷ lệ thành công tuyệt đối.
- Không có khả năng xây dựng Bidirectional Evidence Trace (BET) bền vững.

## Input cần có
- Kho lưu trữ mã nguồn vulnerable (repository), chương trình mục tiêu, entry point fuzz-driver.
- Hướng dẫn định dạng đầu vào (input-format guidance).
- Công cụ phân tích: gdb, radare2, strace, objdump.
- Agent có thể gọi lệnh shell và thao tác tệp trong không gian làm việc.

## Các bước thực hiện
1. Xây dựng Bidirectional Evidence Trace (BET) bền vững — kết nối cách harness tiêu thụ đầu vào với điều kiện cần để một thao tác được chọn trở nên không an toàn.
2. Giữ các tương quan được nguồn minh chứng (source-supported correspondences) cùng với giả thiết (hypotheses) và câu hỏi mở (open questions) của agent.
3. Cung cấp lệnh đọc (reading), phân tích (analysis), và lưu trữ (persistence) để agent xây dựng và tái sử dụng bằng chứng thay vì liên tục truy xuất và tái cấu trúc lại.
4. Giữ phản hồi trong ngân sách đầu ra (output budget) — ưu tiên mã được yêu cầu và các quan hệ cần thiết để diễn giải; trả về kết quả lớn dưới dạng trích đoạn với phạm vi bị bỏ hoặc thông tin tiếp tục.
5. Giữ các điều kiện nhóm nhau (conditions grouped) để việc rút gọn phản hồi không lặng lẽ xóa bỏ một phương án thay thế.
6. Tách hướng dẫn chung (shared instructions) khỏi bản ghi công việc thay đổi (changing work records) để tiền tố prompt ổn định có thể tái sử dụng.
7. Ghi nhật ký đầu ra công cụ và nội dung cung cấp cho model (thời gian, trạng thái bộ nhớ đệm, sử dụng token) để phân biệt việc tái sử dụng backend, khôi phục bằng chứng, và token đã tính phí.
8. Đánh giá chi phí của toàn bộ lần chạy và kết quả của khám phá lỗ hổng, dùng bản ghi tương tác để giải thích kết quả.

## Output mong đợi
- Giảm tổng chi phí 18.0% cho Codex và 23.7% cho OpenCode so với cơ bản, đồng thời bảo toàn tỷ lệ thành công và cải thiện hoặc duy trì tỷ lệ nhớ lại.
- Giảm thời gian chạy (Codex: 50,968s → 33,313s; OpenCode: 25,324s → 24,017s).

## Ví dụ áp dụng
- Agent tìm lỗ hổng trong dự án C/C++ opensource: thay vì liên tục truy xuất lại các hàm liên quan, agent dùng BET để lưu trữ bằng chứng về hàm bất an, giả thiết về ràng buộc đầu vào, và câu hỏi mở; khi cần lại bằng chứng trước đó, agent truy xuất từ BET thay vì sinh lại toàn bộ ngữ cảnh.

## Gotchas
- Chi phí của lần chạy đầy đủ và kết quả khám phá lỗ hổng phải được đánh giá cùng nhau, không chỉ nhìn vào một số đơn lẻ.
- Tín hiệu không phù hợp và chi phí phụ trợ hạn chế lợi ích của các phương pháp hiệu quả hiện có — chỉ 24.4% so sánh dopp duy trì thành công với chi phí thấp hơn.
- Một lần chạy mỗi cấu hình không thiết lập độ mạnh mäßige trước sự thay đổi giữa các lần chạy.
