# 2610.33876v1 FlashScript: Compiling Recurring Agent Workflows into Reusable Neuro-Symbolic Programs

## Giá trị cốt lõi (1 câu)
FlashScript biên dịch một lần chạy agent thành công thành chương trình neuro-ký (NSP) tái sử dụng — hành động và biến đổi dữ liệu thành code, giá trị cụ thể của instance thành tham số, quyết định cần phán đoán mô hình thành lời gọi LLM (llm<T>) — giúp công việc lặp lại chạy giống hệt mọi lần, dùng ~70× ít input tokens và 1/3 thời gian so với agent có skill.

## Problem
Prior work (các nghiên cứu trước) về agent AI ngày càng thực hiện các công việc lặp lại behalf của người dùng cuối. Tuy nhiên, quy trình làm việc của agent không hoạt động như phần mềm thông thường: agent xây dựng lại quy trình trên mọi lần chạy, nên việc thực thi lặp đi lặp lại cùng một yêu cầu có thể phân biệt về đường đi và kết quả [2], [3]. Một lần chạy thành công chứa kiến thức thủ tục quý giá: công cụ nào dùng, điều gì sai, và quyết định nào tạo ra kết quả mong muốn [4], [5]. Hiện tại, kiến thức này bị chôn vùi trong phiên làm việc (session): người dùng có thể kiểm tra, sửa, và chấp nhận một lần chạy, nhưng nỗ lực đó không bao giờ chuyển vào các lần thực thi sau. Người dùng phải tiếp tục kiểm tra một quy trình đã xem xét. Các phương pháp trước (bộ nhớ dựa trên kinh nghiệm, phân phối bằng chứng minh, tự động hóa quy trình robotic) hoặc giúp tái sử dụng kinh nghiệm nhưng chạy vẫn thay đổi, hoặc bảo tồn thực thi trực tiếp nhưng generalize kém khi đầu vào hay môi trường thay đổi. Còn thiếu một quá trình nhất quán nhưng vẫn generalize được mà người dùng có thể chạy lại trên mỗi lần tái diễn của quy trình làm việc.

## Contribution
1. FlashScript — hướng dẫn viết (authoring guidance) để viết các chương trình neuro-ký (NSP) từ các lần chạy agent trước. Biên dịch lần chạy hoàn thành thành script có thao tác bổ sung llm<T>, gửi một prompt đến mô hình và trả về giá trị của kiểu được khai báo (ví dụ: chuỗi, Boolean, option). Các hành động của lần chạy thành code, còn suy luận của nó trở thành lời gọi mô hình khi lần chạy sau cần phán đoán.
2. Xác định ba tầng nơi các lời gọi mô hình thuộc về (input layer, computation layer, output layer) và ba kỹ thuật thay thế phần lớn chúng bằng code: caching giá trị quan sát được sau khi kiểm tra điều kiện (guard), codify (dịch thành quy tắc) các phán đoán lặp lại, và clubbing (gộp) các câu hỏi độc lập thành một cuộc gọi.
3. Đánh giá trên 120 WorkBench analytics tasks với Claude Haiku 4.5: NSP đúng và gọi cùng công cụ trên mọi lần chạy, dùng khoảng 70 lần ít token đầu vào hơn và một phần ba thời gian chạy của skill-guided agent chạy không nhất quán. Trên các tác vụ composite (kết hợp nhiều yêu cầu làm subtask), độ chính xác của skill-guided agent rơi xuống 23% và sự không nhất quán của đầu ra tăng, trong khi NSP vẫn đúng và giống nhau trên mọi lần chạy. NSP cũng tổng quát được tất cả 108 instance chưa thấy của cùng các mẫu (template).

## Method
Pipeline (dòng xử lý) FlashScript có các bước chính:
1. Mỗi lần chạy hoàn thành của agent trở thành điểm khởi đầu: người dùng đạt được qua một số lượt phản hồi và sửa thủ công với agent.
2. Biên dịch lượt chạy thành script có thao tác bổ sung llm<T>: các hành động trở thành code, giá trị cụ thể của instance trở thành tham số, mỗi quyết định cần phán đoán mô hình được biểu diễn dưới dạng một lời gọi gõ (typed call) llm<T>, trả về giá trị của kiểu được khai báo T, tại một điểm cố định trong code.
3. Xác định ba tầng nơi các lời gọi mô hình thuộc về: input layer (chuyển văn bản không có cấu trúc thành giá trị gõ, ví dụ: xác định "L.A." ám chỉ sheet nào), computation layer (ra quyết định sémantik khó biểu diễn dưới dạng quy tắc, ví dụ: một listing có phải scam không), output layer (render kết quả đã tính toán bằng ngôn ngữ tự nhiên cho chủ sở hữu công việc).
4. Áp dụng ba kỹ thuật để giảm số lần gọi mô hình hoặc làm cho chúng nhỏ hơn: caching giữ giá trị quan sát trong lượt chạy và kiểm tra điều kiện trước khi tái sử dụng trong lượt chạy sau; codify thay thế một phán đoán lặp lại bằng một quy tắc heuristic; clubbing đặt các câu hỏi độc lập trong một cuộc gọi hoặc chạy chúng song song.
5. Mỗi lời gọi neural được giới hạn: NSP chọn đầu vào của nó, kiểm tra phản hồi có kiểu dự kiến không, và thực hiện gọi tại một điểm cố định trong code. Lưu luồng điều khiển của NSP quyết định khi nào mô hình được truy vấn, cho cái gì, và cách phản hồi được sử dụng.

## KNOWLEDGE — Số liệu & khái niệm
- Neuro-symbolic program (NSP — chương trình neuro-ký): chương trình kết hợp code và lời gọi đến các mô hình đã học, với mỗi lời gọi có định dạng đầu vào rõ ràng, kiểu đầu ra, và penggunaan được định nghĩa trong NSP.
- llm<T>: thao tác gọi mô hình trả về giá trị của kiểu được khai báo T (string, Boolean, option...).
- Ba tầng của lời gọi mô hình: input layer (tầng đầu vào), computation layer (tầng tính toán), output layer (tầng đầu ra).
- Ba kỹ thuật giảm lời gọi mô hình: caching (lưu trữ đệm), codify (dịch thành quy tắc), clubbing (gộp câu hỏi).
- 120 WorkBench analytics tasks từ 69 mẫu yêu cầu (request templates) với 10 instance mỗi mẫu, chỉ lấy 12 mẫu Analytics (120 tasks).
- Mô hình: Claude Haiku 4.5, nhiệt độ (temperature) 1.
- NSP: đúng và gọi cùng công cụ trên mọi lần chạy; khoảng 70 lần ít token đầu vào hơn; một phần ba thời gian chạy so với skill-guided agent.
- Composite tasks: skill-guided agent accuracy 23%, NSP 100%.
- 108 instance chưa thấy của cùng các mẫu: NSP 100% accuracy vs 96% skill-guided agent.
- 69 cuộc gọi neural tổng cộng trên tất cả NSP, 49 cuộc gọi input được bảo vệ (guarded input calls) và 20 cuộc gọi phản hồi (reply calls), trung bình 1.5 cuộc gọi mỗi lần chạy.
- Caching phục vụ 37/49 cuộc gọi input được bảo vệ từ giá trị đã lưu thay vì mô hình; codify biến mỗi quyết định tầng tính toán thành quy tắc; clubbing giảm một tác vụ mười subtask từ 5.8 câu hỏi mô hình xuống 2.0.
- Ba điều kiện (C1-C3): nhất quán (consistent), tổng quát (generalizable), rẻ (cheap).

## INSIGHT — Cơ chế & tại sao
- [Agent chạy không nhất quán] xảy ra VÌ agent xây dựng lại quy trình trên mọi lần chạy, nên việc thực thi lặp đi lặp lại cùng một yêu cầu có thể phân biệt về đường đi và kết quả. Nghĩa là người dùng không thể tin tưởng một quy trình đã được xem xét sẽ chạy giống hệt lần sau.
- [Skill giúp nhưng không triệt tiêu sự không nhất quán] xảy ra VÌ skill chỉ cung cấp hướng dẫn và agent vẫn quyết định cách thực thi nó, nên các lần chạy vẫn thay đổi (skill-guided agent đạt 99% nhất quán nhưng không phải 100%). Nghĩa là chỉ cần có skill là chưa đủ — cần biên dịch thành code xác định (deterministic code).
- [NSP cục bộ hóa sự không xác định (nondeterminism)] xảy ra VÌ NSP không xóa bỏ sự không xác định mà cục bộ hóa nó, nên chương trình xác định và các lời gọi neural của nó có thể được xem xét và kiểm tra riêng biệt. Mỗi lời gọi neural có định dạng đầu vào rõ ràng, kiểu đầu ra, và sử dụng được định nghĩa trong NSP. Nghĩa là kiểm tra và bảo trì có thể tách biệt code xác định khỏi các thành phần neural.

## IDEA — Áp dụng được gì
1. Áp dụng FlashScript vào công việc lặp lại của doanh nghiệp: lấy một lần chạy agent đã thành công, biên dịch thành NSP Python với các lời gọi llm<T> được giới hạn, sau đó chạy NSP thay vì agent trên mỗi lần tái diễn. Bước đầu: chọn một công việc lặp lại (ví dụ: cập nhật báo cáo tuần), chạy agent một lần thành công, sau đó viết NSP từ lượt chạy đó theo hướng dẫn FlashScript.
2. Sử dụng caching giá trị quan sát được: giữ giá trị đã quan sát trong lượt chạy và kiểm tra điều kiện trước khi tái sử dụng trong lượt sau, chỉ gọi mô hình khi điều kiện thất bại. Bước đầu: tìm các giá trị ổn định trong prompt (ví dụ: tên sheet, mã thành phố) và lưu vào từ điển (dictionary) thay vì hỏi mô hình mỗi lần.
3. Áp dụng codify cho các phán đoán lặp lại: thay thế phán đoán lặp lại bằng quy tắc heuristic (ví dụ: regex để phát hiện yêu cầu chuyển tiền trước visitas đầu tiên là scam). Bước đầu: xác định các quyết định lặp lại trong agent và viết quy tắc thay vì gọi mô hình mỗi lần.

## WISDOM — Nguyên tắc tổng quát
- Nguyên tắc: Công việc agent lặp lại nên được biên dịch thành phần mềm có thể kiểm tra và bảo trì, không chỉ lưu thành skill hay bộ nhớ (memory) — code xác định cho tính nhất quán, lời gọi LLM được giới hạn cho chi phí kiểm soát được.
- Khi nào dùng: Khi có công việc agent lặp lại với dữ liệu mới hoặc thay đổi nhỏ mỗi lần (báo cáo tuần, xử lý đơn hàng, phân tích dữ liệu...).
- Khi nào KHÔNG dùng: Khi công việc không lặp lại (mỗi lần khác nhau hoàn toàn) hoặc khi không cần tính nhất quán (chatbot créativeness, viết văn lưu động...).

## Assumptions & Limitations
- Điều kiện phải đúng: Cần một lần chạy agent thành công làm điểm khởi đầu; người dùng đã dành thời gian làm rõ yêu cầu và sửa thủ công để đạt đầu ra muốn.
- Limitation paper thừa nhận: NSPs không loại bỏ sự không xác định (nondeterminism), chỉ cục bộ hóa nó; việc tổng quát phụ thuộc vào số quyết định còn lại để gọi mô hình (đưa nhiều quyết định hơn cho mô hình xử lý nhiều biến thiên hơn nhưng giảm tính nhất quán và hiệu quả).
- Limitation paper KHÔNG nói: Không nói rõ làm thế nào tự động sinh NSP từ lượt chạy mà không cần can thiệp con người (hiện tại cần coding agent viết NSP từ FlashScript instructions).

## Metadata
- Năm: 2026
- Tác giả: Sadra Sabouri, Hosein Hasanbeig, Adam Sage, Shreya Sinha, Cale Darling, Ashish Tiwari, Katie Garms, Souti Chattopadhyay, Sumit Gulwani
- Category arXiv: cs.HC
- Link PDF: https://arxiv.org/pdf/2610.33876v1
- Classification: [applied]