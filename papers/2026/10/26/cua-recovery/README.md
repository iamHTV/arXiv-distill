# 2610.27645 — CUA-Recovery: Benchmarking Error Recovery in Long-Horizon Computer-Use Agents

## Giá trị cốt lõi (1 câu)

Xây dựng tiêu chuẩn (benchmark) và tập huấn luyện cho việc khôi phục lỗi (error recovery) của agent sử dụng máy tính (CUA) trong quy trình dài hạn — từ các lỗi thực do chính chính sách agent gây ra, không phải lỗi được chọc vào thủ công → các agent hiện tại ít khôi phục hoàn toàn (EAR ≤ 44.0%, Pass@3 ≤ 25.5%), và fine-tuning trên tập train đã xác thực giúp EAR tăng từ 19.9% lên 35.2%.

## Problem

Khi agent sử dụng máy tính (CUA) chuyển sang quy trình dài hạn trải qua nhiều ứng dụng, các lỗi không được phát hiện có thể lầm thanh trạng thái tồn tại (persistent state) và gây ra sự cố lan truyền (cascading failures) trong các hành động sau. Các tiêu chuẩn hiện tại tập trung chủ yếu vào hiệu suất hoàn tác từ đầu đến cuối (end-to-end), cung cấp ít hiểu biết về việc agent có thể phát hiện và khôi phục lỗi trong quá trình thực hiện hay không. Những ít tiêu chuẩn đánh giá khôi phục lại chủ yếu dựa trên lỗi được chọc vào thủ công (manually injected errors), có thể không phản ánh các loại hoặc độ dài của sự cố do chính chính sách agent gây ra — sự khớp kém này giới hạn cả đánh giá thực tế lẫn tiến bộ hệ thống.

## Contribution

1. Đề xuất CUA-Recovery, một tiêu chuẩn đánh giá và huấn luyện cho khôi phục lỗi trong quy trình sử dụng máy tính dài hạn, được xây dựng từ các lỗi thực do chính sách agent gây ra.
2. Xây dựng ReRail, một khung tổng hợp các tác vụ dài hạn và quỹ đạo (trajectory) trong môi trường máy tính để bàn tồn tại (persistent desktop environment) — ReRail ghép các tác vụ MyPCBench thành quy trình dài hạn có thực sự land ground truth (executable ground truth), thu thập các sự cố được xác thực bởi trình xác thực (verifier-confirmed failures) từ nhiều chính sách, và biến chúng thành các quỹ đạo khôi phục đã xác thực (verified recovery trajectories).
3. CUA-Recovery bao gồm bộ kiểm tra do con người xác thực (human-verified test suite) với 2.250 trạng thái sai (erroneous states) trên 100 tác vụ và bộ huấn luyện (training suite) với 8.6K quỹ đạo trên 377 tác vụ.
4. Đánh giá trên bộ kiểm tra cho thấy agent gặp khó khăn cả trong việc nhận ra lỗi được thừa kế và hoàn thành tác vụ: trên sáu agent và sáu độ sâu tiếp수át (takeover depths), Tỷ lệ Nhận biết Lỗi (EAR) đạt cao nhất 44.0% và Pass@3 cao nhất 25.5%. Sau khi tinh chỉnh (fine-tuning) Qwen3.5-35B-A3B trên tập huấn luyện, EAR trung bình của nó tăng từ 19.9% lên 35.2% trên các trạng thái khôi phục bị giữ ra (held-out), và Điểm Tiêu chí (Rubric Score) tăng từ 5.0% lên 16.1%.

## Method

Môi trường và tác vụ: Một tác vụ sử dụng máy tính được mô hình hóa như một Quyết định Markov một phần quan sát (POMDP) (S, A, O, T, Ω). Trạng thái si là trạng thái đầy đủ của máy sau bước i: cơ sở dữ liệu ứng dụng, tệp tin và giao diện người dùng. Hành động là thao tác GUI (click, drag, scroll, nhập phím) hoặc lệnh CLI. Mỗi bước agent quan sát một chụp màn hình oi (phần nhỏ của trạng thái) và hành động cập nhật trạng thái si = T(si-1, ai).

Xây dựng tiêu chuẩn với ReRail (4 bước chính):

1. **Xây dựng tác vụ có sự phụ thuộc (Building tasks with dependencies)**: Bắt đầu từ các tác vụ trong MyPCBench. ReRail tạo một biểu diễn trung gian có thể thực thi (executable intermediate representation) ghi lại các thao tác ứng dụng, dữ liệu chúng đọc và ghi, và các kiểm tra trên đầu ra. Chạy đồ thị này trên ảnh chụp môi trường mới cho ra các giá trị trung gian mong đợi và trạng thái cuối. Để tạo quy trình dài hơn, ReRail nối hai tác vụ khi đầu ra của tác vụ đầu có thể đóng vai trò là đầu vào của tác vụ thứ hai — tạo sự phụ thuộc không sai lầm có thể lan truyền. Hồ sơ kết quả chứa 477 quy trình, với trung vị 3 tác vụ nguồn và 22 nút đồ thị mỗi quy trình.

2. **Kiểm tra tác vụ đã tạo (Checking the generated tasks)**: Thực thi từng quy trình để có các giá trị trung gian tham chiếu và trạng thái cuối, sau đó đóng băng các trình xác thực (verifiers) với giá trị vàng (gold lineage). Xao trộn các giá trị trung gian và chạy lại quy trình; một biến đổi được phát hiện nếu trình xác thực dưới luồng thất bại hoặc dữ liệu đầu ra/lưu trữ khác với giá trị vàng. Giữ các quy trình phát hiện ít nhất một nửa các biến đổi đã thực thi.

3. **Xây dựng trạng thái sai và bộ kiểm tra đánh giá (Constructing erroneous states and evaluation suite)**: Chia các quy trình đã ghép thành tác vụ huấn luyện và kiểm tra. Chạy sáu agent (GPT 5.5, Claude Opus 4.8, Kimi-K3, Qwen3.5-35B-A3B, EvoCUA-32B, OpenCUA-72B) trên các quy trình. Dành cho mỗi lượtROLL thất bại, ReRail so sánh sự thực thi được ghi lại với giá trị vàng để xác định bước gốc (root-cause step) tr, loại lỗi và bước đầu tiên lỗi trở nên rõ ràng. Các chuyên gia sửa các lỗi không liên quan trước tr để gốc là lỗi duy nhất trong tiền tố (prefix). ReRail sau đó tạo các trạng thái tiếp수át (takeover states) bằng cách chạy lại lượtROLL đến các độ sâu d ∈ {0, 5, 10, 15, 20, 25} sau gốc. Đối với bộ kiểm tra, người chú thích con người xác thực gốc, loại lỗi, ngưỡng lỗi (error horizon), tiền tố đã sửa và trạng thái đã chạy lại.

4. **Tạo tập huấn luyện (Generating the training suite)**: Dành cho từng trạng thái sai trong phần huấn luyện, mô hình cơ sở Qwen3.5-35B-A3B cố gắng hoàn thành tác vụ với hướng dẫn về lỗi trước đó. Sinh khôi phục bắt đầu với một gợi ý (hint) xác định bước sai, sau đó thêm bằng chứng xung đột và dữ liệu bị ảnh hưởng nếu các lần thử trước thất bại. Bản tiếp tục đầu tiên được trình xác thực cuối cùng chấp nhận trở thành mục tiêu huấn luyện; một mô hình giáo viên (teacher model) được dùng khi mô hình cơ sở không tạo ra bản tiếp tục nào được xác thực. Mỗi ví dụ huấn luyện chứa hướng dẫn tác vụ, lịch sử sai và bản tiếp tục đã xác thực. Các gợi ý bị loại khỏi đầu vào huấn luyện, khớp với cài đặt tiếp수át không biết (unaware takeover) dùng cho đánh giá.

## KNOWLEDGE — Số liệu & khái niệm

- Trên sáu agent và sáu độ tief tiếp수át: EAR đạt cao nhất 44.0%, Pass@3 cao nhất 25.5%.
- GPT 5.5 đạt Pass@3 cao nhất 25.5% ở d = 20; Claude Opus 4.8 đạt cao nhất 7.7%; không agent mã nguồn mở nào vượt quá 6.4%.
- Bộ kiểm tra: 2.250 trạng thái sai do con người xác thực trên 100 tác vụ, từ 619 lượtROLL thất bại của sáu agent.
- Bộ huấn luyện: 8.640 quỹ đạo khôi phục đã xác thực trên 377 tác vụ; 67.5% trải qua nhiều ứng dụng, trung bình 60 bước.
- Loại lỗi: Lập kế hoạch và nhận thức (planning and perception) chiếm 57.3% nguyên nhân gốc; chấm dứt (termination) 23.5%; thực thi (execution) 19.1%. So sánh: AgentNet 84.3% và GUI-Reflection 71.2% gán cho lỗi thực thi.
- Ngưỡng lỗi (error horizon): Trung vị 17 bước; 78.1% lỗi hiện ra ít nhất 3 bước sau; 60.0% lỗi lần đầu xuất hiện ở bước cuối cùng.
- Kimi-K3 giải quyết 66.9% tác vụ MyPCBench từ trạng thái sạch (clean start) nhưng chỉ nhận ra 7.8–18.5% lỗi được thừa kế trong các lượtROLL thất bại của mình.
- Fine-tuning Qwen3.5-35B-A3B trên tập huấn luyện: EAR từ 19.9% lên 35.2%, Rubric Score từ 5.0% lên 16.1%.
- Đạt +15.3 điểm trên MyPCBench (9.2% → 24.5% Pass@3) và +10.8 điểm trên Odysseys (24.1% → 34.9% Pass@3).
- ReRail-35B-A3B đạt 16.6% Pass@3 trên trạng thái thất bại của Kimi-K3 ở d = 0, so với 11.6% của Kimi-K3; và 12.7% trên trạng thái của EvoCUA-32B, so với 6.4%.
- Thuật toán đối lập (ablation): quỹ đạo thành công trùng token làm EAR tăng từ 19.9% lên 23.6%, còn quỹ đạo khôi phục làm tăng lên 35.2% — tiến bộ đến từ học khôi phục, không chỉ dữ liệu trong miền.

## INSIGHT — Cơ chế & tại sao

[Hiệu suất từ trạng thái sạch không dự báo được khả năng nhận biết lỗi] xảy ra VÌ [một agent có thể giải quyết tốt tác vụ từ đầu nhưng không nhận ra lỗi được thừa kế — Kimi-K3 giải quyết 66.9% MyPCBench từ sạch nhưng chỉ nhận ra 7.8–18.5% lỗi của riêng nó]. Điều này nghĩa là [điểm thành công sạch không có nghĩa là khôi phục lỗi đáng tin cậy; việc đánh giá chỉ kết quả cuối cùng không phân biệt agent đã phát hiện và sửa lỗi của mình trên đường đi hay không].

[Hầu hết lỗi là sai quyết định, không phải sai thao tác] xảy ra VÌ [lập kế hoạch và nhận thức chiếm 57.3% nguyên nhân gốc, trong khi lỗi thực thi chỉ chiếm 19.1%; ví dụ chọn hồ sơ từ năm sai, đọc sai số lượng và dùng trong đơn hàng, tạo sự kiện trong ứng dụng lịch sai]. Điều này nghĩa là [khôi phục đòi hỏi agent kiểm tra lại các quyết định sớm hơn và dữ liệu chúng sản xuất, không chỉ sửa thao tác bấm chuột sai].

[Ngưỡng lỗi dài] xảy ra VÌ [lỗi thành phần trạng thái tồn tại (persistent state) mà hiệu ứng vẫn còn hoạt động ảnh hưởng các thao tác sau; lỗi thường không hiện rõ ngay khi xảy ra, mà bề mặt nhiều bước sau]. Điều này nghĩa là [trung vị độ trễ là 17 bước, 78.1% lỗi hiện ra ít nhất 3 bước sau, 60.0% chỉ hiện ra ở bước cuối cùng — khôi phục đòi hỏi quay lại công việc sớm hơn].

[Nhận biết lỗi hiếm khi dẫn đến khôi phục] xảy ra VÌ [các agent thường xác định vấn đề nhưng để lại trạng thái bị ảnh hưởng không thay đổi hoặc không sửa tất cả hậu quả — tỷ lệ xác thực thành công là 15,6% cho các lượtROLL nhận biết và 12,2% cho các lượtROLL không nhận biết]. Điều này nghĩa là [nhận biết là điều cần thiết nhưng không đủ để khôi phục].

## IDEA — Áp dụng được gì

1. Xây dựng dữ liệu khôi phục lỗi cho agent máy tính: thu thập các sự cố thực do chính sách agent gây ra (không phải lỗi chọc vào), để agent tiếp수át từ trạng thái sai với các gợi ý dần cụ thể, giữ lại chỉ bản tiếp tục được trình xác thực chấp nhận, tinh chỉnh mà không gợi ý. Bước đầu: ghi lại các lượtROLL thất bại của agent trên quy trình máy tính để bàn, xác định bước gốc (root cause) bằng cách so sánh với thực sự land ground truth (gold lineage).
2. Áp dụng vào agent tự động hóa máy tính để bàn: sau khi agent lỗi, dừng lại tại bước gốc, yêu cầu agent mới nhận lịch sử và cố gắng sửa lỗi mà không được cảnh báo có lỗi xảy ra. Bước đầu: tạo các trạng thái tiếp수át ở độ sâu khác nhau (0, 5, 10, 15, 20, 25 bước sau gốc) và đánh giá agent có nhận biết lỗi (EAR) và hoàn thành tác vụ (Rubric Score, Pass@3).
3. Dùng quỹ đạo khôi phục đã xác thực làm dữ liệu tinh chỉnh thay vì quỹ đạo hoàn hảo — tiến bộ lớn hơn nhiều so với dữ liệu thành công trùng token. Bước đầu: tinh chỉnh một epoch trên 8.6K quỹ đạo khôi phục đã xác thực, loại bỏ gợi ý khỏi đầu vào huấn luyện.

## WISDOM — Nguyên tắc tổng quát

- Nguyên tắc: Trong hệ thống agent dài hạn, phát hiện lỗi và khôi phục quan trọng bằng với việc thực hiện tác vụ — một agent mạnh mẽ từ trạng thái sạch vẫn có thể thất bại thảm họa do một lỗi sớm không được phát hiện.
- Khi nào dùng: Quy trình agent thao tác máy tính để bàn duy trì trạng thái tồn tại qua nhiều bước và nhiều ứng dụng.
- Khi nào KHÔNG dùng: Nhiệm vụ đơn bước (nhập liệu đơn lần, truy xuất văn bản) — không có trạng thái tồn tại để hỏng, không cần khôi phục.
- Ví dụ áp dụng ngoài domain gốc: Trong vận hành bán lẻ, trước khi chấp nhận đơn hàng từ hệ thống tự động, hãy kiểm tra các quyết định sớm (chọn sản phẩm, số lượng) chứ không chỉ kiểm tra trạng thái cuối — một lỗi sớm có thể làm hỏng toàn bộ đơn mà chỉ hiện ra khi giao hàng.

## Assumptions & Limitations

- Điều kiện phải đúng: môi trường máy tính để bàn xác định (deterministic) sau khi tắt các yếu tố phá vỡ khả năng tái lập (cập nhật tự động, daemon thông báo); ngữ cảnh cửa sổ bị giới hạn (K = 20 ảnh chụp màn hình gần nhất trong đánh giá).
- Limitation paper thừa nhận: đây là preprint (chưa được đánh giá bằng đồng nghiệp); bộ kiểm tra do con người xác thực giới hạn ở 100 tác vụ; tinh chỉnh một epoch; môi trường giả định xác định.
- Limitation paper KHÔNG nói: hiệu quả trên tác vụ không phải máy tính để bàn (trình duyệt web, di động) chưa được kiểm chứng; chi phí thu con người xác thực 2.250 trạng thái sai trên quy mô lớn; tính generalize qua nhiềucaffold agent khác nhau bên ngoài sáu agent đã đánh giá.

## Metadata

- Năm: 2026
- Tác giả: Xu Hu, Haoming Li, Yuxiang Wang, Jinxin Yang, Kangshuo Li, Licheng Wang, Dingyi Kang, Jiayu Song, Tianhao Wang, Zhanhua Hu, Xu Yang, Qiannan Li, Bingzhe Li, Feng Chen
- Category arXiv: cs.AI
- Link PDF: https://arxiv.org/pdf/2610.27645
- Citation count: chưa có (paper mới, Oct 2026)
