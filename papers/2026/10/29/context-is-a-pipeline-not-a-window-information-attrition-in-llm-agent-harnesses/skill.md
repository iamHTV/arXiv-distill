# Skill: agent-context-pipeline-yield-audit
Source: 2610.36114
Type: evaluation-method

## Khi nào dùng skill này
- Bạn đang đánh giá hoặc vận hành một hệ thống LLM agent (máy đại diện ngôn ngữ lớn) dùng tool và muốn biết liệu harness (máy bọc agent) có cắt mất bằng chứng tool output hay không.
- Bạn nhận thấy agent chẩn đoán sai nhất quán trên một số lỗi dù accuracy tổng thể chưa giảm.
- Bạn cần báo cáo số liệu kèm accuracy (ví dụ yield, số tool call) cho leadership hoặc khách hàng.

## Tình huống KHÔNG nên dùng
- Hệ thống agent của bạn không dùng tool (không có tool output để cắt).
- Bạn chưa triển khai agent harness (máy bọc agent) và chỉ dùng model thuần túy qua API.

## Input cần có
- Danh sách các tool mà agent gọi (ví dụ liệt kê quá trình, xem log, phân tích mã).
- Bản ghi transcript (đề nghị chat) của agent chứa cả kết quả tool đầy đủ (produced) và văn bản thực sự gửi đến model (delivered).
- Ngân sách ký tự (character budget) mà harness dùng để cắt tool output (nếu biết).
- Một tập thử nghiệm có ground truth (sự thật làm grounds) về nguyên nhân lỗi (root cause) để chấm điểm chẩn đoán.

## Các bước thực hiện
1. Instrument (cài đặt công cụ đo) mỗi ranh giới pipeline (boundary) S1–S5: S1 produce→deliver, S2 deliver→act, S3 act→retain, S4 retain→transfer, S5 transfer→persist. Ghi lại số kết quả tool đã sản xuất và số đã đến model tại mỗi ranh giới.
2. Chạy replica (chạy lại) tập công cụ thực tế qua hai quy tắc cắt: cắt tiền tố (prefix slice, cắt cố định từ đầu) và cắt theo dòng (row-aware cut, cắt toàn bộ dòng). Ghi nhận mỗi kết quả nào vỡ (broken JSON) và mỗi trường nào biến mất.
3. Tính yield = số phát hiện (finding) đã ghi nhận chia cho số tính toán đã chạy. Báo cáo yield bên cạnh accuracy trên mỗi bản đánh giá agent.
4. Chạy thử nghiệm kiểm soát: giữ nguyên agent, công cụ, tác vụ, model; chỉ bật/tắt một lỗ hổng harness tại một thời điểm (ví dụ chỉ bật cắt tiền tố). Dự đoán trước mỗi bước (registered prediction) và ghi lại mọi thay đổi kế hoạch với ngày và lý do.
5. Chấm điểm chẩn đoán chỉ khi agent đặt tên chính xác nguyên nhân (culprit) trong trường câu trả lời, kiểm tra đối với ground truth, không chỉ đếm nhắc đến thành phần đó trong đoạn văn.

## Output mong đợi
- Số liệu loss (mất mát) tại mỗi ranh giới S1–S5 (số kết quả cắt, số trường mất, số JSON hỏng).
- Số yield (tỷ suất kết quả/công suất) và số tool call cho mỗi cấu hình harness.
- Kết luận liệu cắt dữ liệu gây sai chẩn đoán hay chỉ gây thêm công việc, kèm bằng chứng từ thử nghiệm kiểm soát.

## Ví dụ áp dụng
Bạn vận hành agent chẩn đoán lỗi hệ thống dùng tool liệt kê container (liệt kê chứa ứng dụng). Bạn chạy bước 1–3 và phát hiện 34% kết quả tool bị cắt, một trường bằng chứng chỉ đến model 4.7% cuộc gọi. Bạn chạy bước 4 và thấy yield giảm từ 0.61 xuống 0.31 khi bật cắt tiền tố, trong khi accuracy không giảm rõ trên lỗi sinh ra quá trình mới (spawned fault). Bạn chuyển sang cắt theo dòng (bước 2) và yield khôi phục về 0.61.

## Gotchas
- Scorer chỉ đếm nhắc đến (mention) thay vì đòi hỏi agent đặt tên nguyên nhân sẽ thổi phồng điểm (ví dụ từ 2/15 lên 14/15). Hãy kiểm tra scorer trước khi chạy thử nghiệm.
- Cắt theo vị trí không làm bằng chứng bất kỳ trường nào kém hơn, nhưng model đã chú ý không đều theo vị trí trong cửa sổ, nên harness làm trầm trọng thêm vấn đề.
- Một cửa sổ context gần trống (chỉ 5.75% được dùng) không có nghĩa là bằng chứng không bị vứt phía trên — hãy đo loss (mất mát) chứ không chỉ đo kích thước cửa sổ.
- Khả năng thu hút (capacity) trông ổn định gây lừa điều equipos: họ thêm quy trình viết (written procedure), thấy kết quả tốt hơn, và ngừng tìm ở chỗ sai — đây là sửa lý do sai vì cần ít bằng chứng đến hơn, không phải cung cấp bằng chứng tốt hơn.
