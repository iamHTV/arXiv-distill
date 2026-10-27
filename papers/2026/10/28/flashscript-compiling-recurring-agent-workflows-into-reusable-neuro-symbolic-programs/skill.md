# Skill: flashscript-nsp-compilation
Source: 2610.33876v1
Type: workflow

## Khi nào dùng skill này
- Có một công việc agent lặp lại (báo cáo tuần, xử lý đơn hàng, phân tích dữ liệu...) và muốn lần sau chạy giống hệt lần trước.
- Muốn giảm chi phí inference (token đầu vào) và thời gian chạy của agent trên công việc lặp lại.
- Muốn có phần mềm có thể kiểm tra, bảo trì, tái sử dụng thay vì chỉ lưu skill hay bộ nhớ.

## Tình huống KHÔNG nên dùng
- Công việc không lặp lại (mỗi lần hoàn toàn khác nhau).
- Không cần tính nhất quán (chatbot sáng tạo, viết văn lưu động).

## Input cần có
- Một lần chạy agent đã thành công (trajectory) trên công việc lặp lại.
- Hướng dẫn FlashScript (prompt template, mô tả công cụ, cùng trajectory agent dùng để viết skill).
- Một coding agent (ví dụ: Claude Code) để viết NSP từ hướng dẫn.
- Mô hình LLM để thực hiện các lời gọi llm<T> trong NSP.

## Các bước thực hiện
1. Chạy agent trên công việc lặp lại một lần thành công, ghi nhận toàn bộ trajectory (suy luận + hành động).
2. Viết NSP từ trajectory: các hành động thành code, giá trị cụ thể của instance thành tham số, mỗi quyết định cần phán đoán mô hình thành lời gọi llm<T> với kiểu trả về được khai báo.
3. Xác định ba tầng của lời gọi mô hình: input (văn bản không có cấu trúc → giá trị gõ), computation (quyết định sémantik), output (render kết quả bằng ngôn ngữ tự nhiên).
4. Áp dụng ba kỹ thuật giảm lời gọi mô hình: caching (lưu giá trị đã quan sát, kiểm tra điều kiện trước khi tái sử dụng), codify (thay phán đoán lặp lại bằng quy tắc heuristic), clubbing (gộp câu hỏi độc lập thành một cuộc gọi hoặc chạy song song).
5. Giới hạn mỗi lời gọi neural: NSP chọn đầu vào, kiểm tra kiểu phản hồi, thực hiện gọi tại điểm cố định trong code.
6. Chạy NSP trên mỗi lần tái diễn của công việc, chỉ gọi mô hình khi thực sự cần phán đoán.

## Output mong đợi
- NSP chạy giống hệt mọi lần (cùng công cụ, cùng đầu ra).
- Giảm khoảng 70× token đầu vào so với skill-guided agent.
- Giảm khoảng 1/3 thời gian chạy.
- Tổng quát được các instance chưa thấy của cùng mẫu.

## Ví dụ áp dụng
Nhân viên văn phòng có agent cập nhật báo cáo thuê nhà LA và gắn cờ scam mỗi tuần. Lần chạy trước: agent suy luận "LA" = Los Angeles, chọn sheet tương ứng, lấy danh sách mới, gắn cờ các listing yêu cầu chuyển tiền trước visitas, tóm tắt thay đổi. Biên dịch thành NSP: SHEETS = {'LA': 'Los Angeles'}, def rental_report(wb, city='LA'): name = SHEETS.get(city) or llm<wb.sheets>(city), new = fetch_merge(wb[name], SOURCES[name]), changes = diff(wb[name], new), scams = [r for r in new.rows if llm<bool>(f"Is this a scam? {r}")], wb[name] = highlight(new, changes, scams), return llm<str>(f"Summarize: {changes}"). Lần sau: chạy NSP, giống hệt lần trước, dùng ít token hơn.

## Gotchas
- NSP không loại bỏ sự không xác định, chỉ cục bộ hóa nó — các lời gọi LLM vẫn có thể thay đổi đầu ra nhưng chỉ trong phạm vi được giới hạn.
- Việc tổng quát phụ thuộc vào số quyết định còn lại để gọi mô hình: ủy quyền nhiều quyết định hơn cho mô hình xử lý nhiều biến thiên hơn nhưng giảm tính nhất quán và hiệu quả.
- Cần coding agent để viết NSP từ FlashScript instructions — chưa hoàn toàn tự động.
- Caching chỉ hoạt động cho giá trị quan sát được (đã có trong lượt chạy trước), không hoạt động cho giá trị mới chưa từng thấy.