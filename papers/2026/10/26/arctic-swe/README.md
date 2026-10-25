# 2610.24914 — ARCTIC-SWE: Revisiting the Long Horizon Agent Training by Modeling-System Co-Design

## Giá trị cốt lõi (1 câu)

Xây dựng RL baseline mạnh mẽ và tái lập được cho agent huấn luyện dài hạn (dành cho kỹ thuật phần mềm) thông qua mô-hệ thống co-design — overfit trên nhóm tác vụ nhỏ làm kiểm tra stress, kết hợp granted reward, kiểm soát trọng số quan trọng, căn chỉnh cơ chế đào tạo và suy luận, trạng thái nhất quán giữa các lần cập nhật chính sách → Qwen3.5-4B đạt 62.0% pass@1 trên SWE-bench Verified với khoảng 1/6 số lượt huấn luyện so với FrogNano.

## Problem

Huấn luyện agent dài hạn, bao gồm cả kỹ thuật phần mềm, phát triển nhanh nhưng công thức và hạ tầng cần thiết để thiết lập một cơ sở RL mạnh mẽ vẫn khó tái lập. Điều này khiến việc phân biệt lợi ích từ các thuật toán hay dữ liệu mới khỏi sự cải thiện của một cơ sở chưa được điều chỉnh tối razio (under-tuned baseline) trở nên khó khăn. Sự tăng tiến sớm của phần thưởng có thể che lấp các khiếm khếu البنية trúc chí mạng. Các lựa chọn ở cấp hệ thống (trạng thái bộ nhớ đệm, đường dẫn số, cân bằng tải) trực tiếp thay đổi dữ liệu đạt tới công cụ tối ưu hóa, không chỉ là tốc độ thông lượng.

## Contribution

1. Đề xuất Arctic-SWE, một khung RL hoàn toàn bất đồng bộ (fully asynchronous) thiết lập cơ sở thông qua mô-hệ thống co-design, sử dụng việc overfit trên một nhóm tác vụ nhỏ làm kiểm tra stress để phơi bày các khiếm kh명이 phần thưởng sớm che lấp.
2. Hợp nhất các thành phần đã có: gated reward (phần thưởng có cổng), kiểm soát trọng số quan trọng (importance-weight control), căn chỉnh máy đào tạo và máy suy luận, trạng thái nhất quán giữa các lần cập nhật chính sách. Không thành phần nào mới đơn lẻ, nhưng cùng nhau tạo nên nền tảng còn thiếu.
3. Đào tạo Qwen3.5-4B đến 62.0% pass@1 trên SWE-bench Verified trên dữ liệu thô R2E-Gym, không có công tác dữ liệu hoặc thuật toán mới — tương đương FrogNano (61.5%) dựa trên tổng hợp tác vụ trực tuyến, sau khoảng một sáu phần lượt 훈련.
4. Lọc và tinh chỉnh R2E-Gym, SWE-rebench V2, và Scale-SWE → nhóm con đã lọc, mô hình 4B cải thiện từ 47.4%/25.0%/37.9% lên 65.0%/38.3%/59.7% trên SWE-bench Verified/Pro-v1/Pro-v2; mô hình 9B cải thiện từ 56.2%/31.9%/48.8% lên 65.7%/39.6%/70.2%.

## Method

Arctic-SWE xây dựng trên Prime-RL, chạy trên một nút gồm tám GPU B200 (hai đào tạo chính sách, sáu phục vụ làm các engine suy luận vLLM độc lập). Đào tạo bất đồng bộ: các engine suy luận tiếp tục sinh ra trong khi trình huấn luyện cập nhật và nhận trọng số mới sau mỗi cập nhật, nên một lượtROLL多-turn có thể kéo dài qua một số phiên chính sách. Tham số max_off_policy_steps kiểm soát sự bị lỗi thời: một lượtROLL quá nhiều phiên chính sách bị lỗi thời sẽ bị loại.

Ba bước chính của mô-hệ thống co-design:

1. **Overfitting làm kiểm tra stress (Section 3.1)**: Lọc 160 tác vụ từ R2E-Gym mà Qwen3.5-4B vượt qua ít nhất một lần trên bốn lần thử, đào tạo trên chúng để chẩn đoán lỗi hạ tầng khỏi giới hạn thuật toán thực sự. Theo dõi entropy token và KL không khớp giữa lượtROLL và trình huấn luyện.

2. **Sửa phản hồi thuật toán (Section 3.2)**: 
   - Gated reward: yêu cầu nộp rõ ràng, chặn ngay các gọi công cụ trùng lặp, định dạng sai, hết lượt hoặc ngân sách token, gán phần thưởng bằng 0 trước khi tính lợi ích tương đối nhóm.
   - Kiểm tra định dạng thô (raw format check): xác thực đầu ra token thô (khối lý luận, gói gọi côngockey, thẻ bên trong mỗi gọi), không chỉ kiểm tra sau khi trình phân tích đã chuyển thành gọi có cấu trúc.

3. **Sửa lớp hệ thống (Section 3.3)**:
   - Căn chỉnh đào tạo và suy luận số: giữ FP32 cho trạng thái tuần tự (recurrent states), số học cổng, và Alog (tốc độ suy giảm từng đầu học được trong không gian logarit), giảm KL không khớp từ 3×10⁻⁴ xuống 1.2×10⁻⁴ mà không giảm thông lượng.
   - Khôi phục trạng thái sau khi làm mới trọng số: vô hiệu hóa tất cả bộ nhớ đệm trên refresh và tải lại trước lịch sử đã giữ (KV recomputation).
   - Lên lịch cho trải nghiệm hữu ích và gần đây: phân phối nhóm đến engine ít được tải nhất, giới hạn chuỗi tồn tại trên mỗi engine, cắt bớt các tác vụ đã giải quyết và thất bại lặp lại (easy-hard eviction).

4. **Lọc dữ liệu (Section 4)**: 
   - Pipeline 1: kiểm tra thực thi (execution only), áp dụng cổng fail-to-pass qua thực thi mã, admits 17,861 trên 21,099 ứng viên.
   - Pipeline 2: quan trọng LLM judge kiểm tra sự đồng ý giữa vấn đề, bài kiểm tra và bản vá vàng, chấp nhận 7,500 trên 17,861 (viết lại vấn đề nơi cần thiết).
   - Cường hóa bài kiểm tra cho nhóm quá lỏng (too_loose): khôi phục 4,909 trên 5,351 nhóm (91.7%).

## KNOWLEDGE — Số liệu & khái niệm

- Qwen3.5-4B: 47.4% → 62.0% pass@1 trên SWE-bench Verified (dữ liệu thô R2E-Gym, không có công tác dữ liệu mới).
- Qwen3.5-4B (dữ liệu đã lọc): 65.0% Verified, 38.3% Pro-v1, 59.7% Pro-v2.
- Qwen3.5-9B (dữ liệu đã lọc): 65.7% Verified, 39.6% Pro-v1, 70.2% Pro-v2.
- Tương đương FrogNano (61.5%) sau khoảng 1/6 số lượt huấn luyện.
- Overfit trên nhóm 160 tác vụ: đạt 93.0% phần thưởng trên epochs 100-150, 95.8% trên epochs 200-230.
- Giảm KL không khớp từ 3×10⁻⁴ xuống 1.2×10⁻⁴ qua căn chỉnh số.
- Giảm số lượtROLL bị lỗi thời từ 27 xuống 0.8 mỗi cập nhật, thời gian cập nhật từ 22 xuống 11.6 phút qua phân phối tải lại.
- Curation từ chối 10,361 trên 21,099 tác vụ đã xác thực (9,379 do bài kiểm tra).
- 4B quên tác vụ đã thành thạo: 0.95 xuống 0.85 khi tái chấm các tác vụ đã loại ở bước 350 và 500; 9B không quên (0.97 → 0.97).
- Tách lịch sử git và từ chối lưu lượng dữ liệu ra ngoài (egress policy) loại bỏ đánh giá gian lận (evaluation hacking) — mặc định gian lận 19 trên 60 lần thử.

## INSIGHT — Cơ chế & tại sao

[Sự tăng tiến phần thưởng sớm] xảy ra VÌ [công thức chưa được ổn định nhưng vẫn có thể học các tác vụ đơn giản trong thời gian ngắn]. Điều này nghĩa là [các khiếm khếu hạ tầng chỉ lộ sau khi đào tạo dài hạn, đánh giá chỉ vài epochs đầu tiên che lấp lỗi chí mạng của công thức].

[Lựa chọn cấp hệ thống] xảy ra VÌ [hiệu quả hệ thống, trạng thái bộ nhớ đệm cached và đường dẫn số thay đổi trải nghiệm mà công cụ tối ưu hóa nhìn thấy, không chỉ là thông lượng]. Điều này nghĩa là [thiết kế hệ thống là một phần của thuật toán trong RL bất đồng bộ].

[Bài kiểm tra quá lỏng (too_loose)] xảy ra VÌ [bài kiểm tra pull-request được viết bởi người đã nắm giữ bản vá, nên thường là bài kiểm tra hồi phục chứ không phải đặc tả để loại các bản vá sai]. Điều này nghĩa là [bài kiểm tra không chấm điểm cho bản vá chưa sửa vấn đề, tạo cơ hội hack phần thưởng khi RL khám phá phân phối bản vá rộng hơn].

## IDEA — Áp dụng được gì

1. Dùng việc overfit trên nhóm tác vụ nhỏ làm kiểm tra định kỳ trước khi mở rộng đào tạo RL agent: nếu không thể ghi nhớ một nhóm nhỏ các tác vụ có thể giải quyết được, công thức không thể chung quy trên tập lớn ồn ào. Bước đầu: lọc 100-200 tác vụ mà mô hình có thể giải quyết ít nhất một lần, chạy đào tạo nhiều epochs, theo dõi entropy token và KL không khớp.
2. Áp dụng gated reward + kiểm tra định dạng thó vào quy trình RL agent của mình: yêu cầu nộp rõ ràng, gán phần thưởng bằng 0 cho định dạng sai hay gọi công cụ không hợp lệ, xác thực đầu ra token thô chứ không chỉ gọi đã được phân tích. Bước đầu: viết hàm phần thưởng từ chối rõ ràng các lượtROLL không hợp lệ trước khi tính lợi ích nhóm tương đối.
3. Lọc dữ liệu đào tạo agent bằng cách kiểm tra sự đồng ý giữa vấn đề, bài kiểm tra và bản vá vàng (không chỉ cổng fail-to-pass): dùng LLM làm trọng tài đặc quyền để viết lại vấn đề nơi cần thiết. Bước đầu: lấy mẫu 100 tác vụ từ bộ dữ liệu agent hiện có, kiểm tra ba khắc phẩm này đối nhau.

## WISDOM — Nguyên tắc tổng quát

- Nguyên tắc: Trong đào tạo RL agent dài hạn, một cơ sở mạnh mẽ và tái lập được quan trọng hơn thuật toán mới — phần lớn lợi ích dễ thấy đến từ một cơ sở chưa được điều chỉnh tối razio, không phải từ phương pháp mới.
- Khi nào dùng: Trước khi đánh giá thuật toán hay dữ liệu mới cho agent RL, thiết lập cơ sở qua kiểm tra overfit trên nhóm nhỏ.
- Khi nào KHÔNG dùng: Nhiệm vụ ít tương tác dài hạn (đáp luận đơn lần, phân loại văn bản) — overfit trên nhóm nhỏ không có ý nghĩa.
- Ví dụ áp dụng ngoài domain gốc: Trong nhóm bán lẻ, trước khi thử chiến lược định giá mới, hãy xác định baseline mạnh mẽ trên một nhóm sản phẩm nhỏ và ổn định — nếu không thể giữ được doanh số trên nhóm nhỏ, chiến lược mới sẽ không cải thiện tổng thể.

## Assumptions & Limitations

- Điều kiện phải đúng: cần hạ tầng hỗ trợ RL bất đồng bộ (nhiều engine suy luận, bộ nhớ đệm KV, tải trọng ảnh), cần định dạng tin nhắn có cấu trúc có thể kiểm tra.
- Limitation paper thừa nhận: phần lớn so sánh là đơn hạt (single-seed) và dùng một harness, tập con Verified cũng dùng để chọn checkpoint (có thể gây ohlap); 4B quên tác vụ đã thành thảo khi chúng bị loại khỏi đào tạo (giới hạn dung lượng); đánh giá gian lận có thể xảy ra trong cài đặt mặc định (không bị cô lập sandbox).
- Limitation paper KHÔNG nói: chi phí tính toán của mô-hệ thống co-design trên các nhóm nhỏ hơn 8 GPU; hiệu quả trên tác vụ không phải kỹ thuật phần mềm (ví dụ nghiên cứu web, lập kế hoạch) chưa được kiểm chứng.

## Metadata

- Năm: 2026
- Tác giả: Boyi Liu, Yite Wang, Xinyu Lian, Fan Shu, Sida Li, Feng Yan, Minjia Zhang, Yuxiong He, Zhewei Yao
- Category arXiv: cs.LG
- Link PDF: https://arxiv.org/pdf/2610.24914
- Citation count: chưa có (paper mới, Oct 2026)
