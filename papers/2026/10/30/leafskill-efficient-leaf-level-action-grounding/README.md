# [2610.32412] LeafSkill: Efficient Leaf-Level Action Grounding for Recursive LLM Agents

## Giá trị cốt lõi (1 câu)

Thay vì gọi mô hình chủ (host model lớn, 27B) mỗi lần cần dịch một tác vụ lá thành lệnh thực thi, hãy dùng lớp grounding bên ngoài (retrieve–bind–select) chọn trong một tập hành động được ràng buộc bởi trạng thái — giảm 23.1–41.3% token chủ và giữ logic lập kế hoạch đệ quy của host.

## Problem

Các tác tử LLM đệ quy giải quyết tác vụ dài hạn bằng cách phân giải thành các nút tác vụ nhỏ dần, nhưng việc phân giải không loại bỏ việc suy luận đắt tiền của mô hình chủ. Ngay sau khi một tác vụ lá đã được làm rõ, tác tử vẫn có thể gọi cùng một mô hình lớn chỉ để dịch nhiệm vụ địa phương thành một lệnh môi trường chấp nhận được. Ví dụ, sau khi lập kế hoạch đã tạo "pick up onion1 from board1", quyết định còn lại không còn là cách giải quyết mục tiêu tổng thể, mà là cách dịch chỉ thị cục bộ này thành lệnh thực thi có thể chấp nhận. Việc grounding cấp lá này lặp lại xuyên suốt quỹ đạo và tiêu tốn 22.9–44.5% token của mô hình chủ. Việc tái sử dụng quyết định không tương đương với việc lưu trữ chuỗi ký tự chính xác: các nhiệm vụ có nghĩa tương đương có thể được diễn đạt bằng nhiều cụm từ khác, và các đối số đã truy xuất có thể không có trong trạng thái hiện tại.

## Contribution

1. Công thức vấn đề và đo lường: đóng góp việc grounding cấp lá thành một ranh giới ủy quyền riêng biệt trong các tác tử LLM đệ quy và cho thấy nó chiếm 22.9–44.5% token của mô hình chủ trong các vết dấu nguồn.
2. Kiến trúc grounding ràng buộc: phát triển một lớp truy xuất–gắn kết–chọn chọn chuyển đổi trải nghiệm tác vụ/hành động có thể tái sử dụng thành các ứng viên hành động có thể chấp nhận phụ thuộc vào trạng thái, đồng thời giữ lập kế hoạch và phục hồi do chủ sở hữu thông qua sự từ chối rõ ràng.
3. Bằng chứng xuyên môi trường: trên Robotouille và ALFWorld, chứng minh việc giảm đáng kể token chủ trên các tác vụ được giải quyết chung, xác định vai trò bổ sung của truy xuất, gắn kết và chọn lựa, và cho thấy sự tăng trưởng thư viện sau huấn luyện có thể tăng thêm mức giảm trừ mà không cần huấn luyện lại trình chọn.

## Method

LeafSkill có hai giai đoạn: xây dựng ngoại tuyến (offline) và grounding trực tuyến (online). Ngoại tuyến, các quỹ đạo của mô hình chủ được chuyển thành mẫu tác vụ/hành động chuẩn và giám định cho trình chọn. Trực tuyến, LeafSkill chỉ được gọi tại các tác vụ lá đủ điều kiện: nó truy xuất các mẫu liên quan, gắn kết chúng với tập hành động chấp nhận được hiện tại, và chọn một hành động hoặc từ chối. Mỗi kỹ năng s trong thư viện L là một cặp tác vụ chuẩn/mẫu hành động. Với một yêu cầu đủ điều kiện, truy xuất ngữ nghĩa xếp hạng các khóa tác vụ chuẩn so với tác vụ hiện tại và trả về các khóa hàng đầu trên ngưỡng tương đồng γ. Gắn kết dựa trên trạng thái tạo mẫu loại bằng các thực thể từ yêu cầu hiện tại và chỉ giữ các lệnh cụ thể khớp chính xác một hành động trong tập chấp nhận được At. Các ứng viên nhận mã định dạng cục bộ yêu cầu và được tráo đổi trước khi trình bày cho trình chọn. Trình chọn chọn một mã định dạng hoặc ⊥ (từ chối), không thể sinh lệnh tự do. Mã định dạng được chọn được giải quyết qua bản đồ cục bộ yêu cầu và kiểm tra lại đối với At trước khi thực thi. Từ chối trả về quyền điều khiển cho chủ mà không thay đổi trạng thái tác tử.

## KNOWLEDGE — Số liệu & khái niệm

- Việc grounding cấp lá tiêu tốn 22.9% (Robotouille đồng bộ), 23.7% (Robotouille bất đồng bộ) và 44.5% (ALFWorld) token của mô hình chủ (Figure 1).
- Với cùng kế hoạch ReCAP và chủ Qwen3.5-27B, LeafSkill giảm token chủ trên các tác vụ được giải quyết chung bởi 23.1% trên Robotouille và 41.3% trên ALFWorld, trung bình trên chín cặp chạy lẫn nhau của ba lần lặp độc lập; các mức giảm riêng lẻ trải qua 16.8–29.7% và 36.7–45.2%.
- Đánh giá Robotouille độc lập Grupp C: giảm 14.4% token (CI 95% [3.0, 24.5]) và 14.1% lệnh gọi (CI 95% [3.6, 23.3]).
- Thành công quan sát được cao hơn 6.0–9.0 điểm trên B và 8.0 điểm trên C (137/200 so với 121/200, p = .0259).
- Nghiên cứu sự tăng trưởng rời rạc mở rộng thư viện từ 446 đến 588 kỹ năng mà không cần huấn luyện lại trình chọn hoặc quỹ đạo kiểm tra; trên các tác vụ được giải quyết bởi tất cả hệ thống, mức giảm token chủ sâu hơn từ 18.3% lên 25.6%.
- Retriever: BGE-small-en-v1.5; Trình chọn: Qwen3-1.7B (LoRA hạng 16); Chủ: Qwen3.5-27B; Lập kế hoạch: ReCAP.
- Chi phí phụ của trình chọn: 6.900–9.952 token mỗi tập sự (714–1.034 mỗi lời gọi), được báo cáo riêng biệt vì trình chọn và chủ có trình phân mã thang khác nhau.
- Trên các tác vụ được giải quyết bởi cả hai hệ thống trên Robotouille B, Top-5 chọn lựa cung cấp giảm thêm 14.9% token chủ so với Top-1.
- SFT nâng độ chính xác chọn hạng hỗn hợp từ 81.9% lên 93.3%; chẩn đoán tất cả âm (OOD stress test), SFT trả FALLBACK_RECAP trong chỉ 7.5% trường hợp.
- Thư viện Robotouille: 413 khóa tác vụ và 446 kỹ năng từ 200 cây nguồn Gr A; thư viện mở rộng 527 khóa và 588 kỹ năng sau khi hợp nhất với 200 cây Gr B.

## INSIGHT — Cơ chế & tại sao

[Việc grounding cấp lá chiếm 22.9–44.5% token chủ] xảy ra VÌ [mỗi lần planners tạo ra một tác vụ lá, mô hình chủ lớn vẫn được gọi chỉ để dịch tác vụ đó thành một lệnh thực thi, và thao tác này lặp đi lặp lại xuyên suốt quỹ đạo]. Điều này nghĩa là [một mục tiêu hẹp nhưng quan trọng để giảm suy luận chủ đắt tiền].

[Lớp retrieve–bind–select giảm token mà không thay đổi lập kế hoạch] xảy ra VÌ [truy xuất chỉ đề xuất, gắn kết duy trì tính khả thi, và trình chọn chỉ chọn trong một tập ứng viên hữu hạn hoặc từ chối — uy quyền được giới hạn hẹp, lập kế hoạch và phục hồi vẫn nằm hoàn toàn với chủ]. Điều này nghĩa là [tái sử dụng kinh nghiệm không cần lấy quá quyền lập kế hoạch từ mô hình chủ].

[Gắn kết dựa trên trạng thái an toàn hơn việc mô hình tự sinh lệnh] xảy ra VÌ [gắn kết tạo mẫu loại bằng các thực thể từ yêu cầu hiện tại và chỉ giữ các lệnh cụ thể khớp chính xác một hành động trong tập chấp nhận được At, thay vì hỏi mô hình sinh giá trị cắm]. Điều này nghĩa là [ràng buộc xác thực trước khi thực thi ngăn chặn lệnh không hợp lệ].

[Mã định dạng cục bộ yêu cầu + tráo đổi ngăn trình chọn ghi nhớ ID kỹ năng toàn cục] xảy ra VÌ [các ứng viên nhận mã định dạng cục bộ yêu cầu và được tráo đổi, trình chọn phải đọc nội dung ứng viên thay vì dựa vào nhãn kỹ năng cố định]. Điều này nghĩa là [kỹ năng tương thích có thể được thêm vào mà không thay đổi không gian đầu ra của trình chọn].

[Thư viện có thể tăng trưởng tại thời điểm đọc mà không cần huấn luyện lại] xảy ra VÌ [mã định dạng cục bộ yêu cầu loại bỏ ngôn ngữ đầu ra cố định, nhưng không cung cấp trình chọn mới hoặc ngữ nghĩa hành động mới]. Điều này nghĩa là [các kỹ năng mới tương thích có thể được thêm vào thư viện và sử dụng ngay tại thời điểm suy luận].

## IDEA — Áp dụng được gì

1. Áp dụng lớp grounding bên ngoài (retrieve–bind–select) vào tác tử đệ quy: khi lập kế hoạch đã phân giải thành tác vụ lá, dùng thư viện kỹ năng thay vì gọi mô hình chủ lớn. Cho ai: đội xây dựng tác tử LLM đệ quy gọi mô hình lớn nhiều lần. Bước đầu: xây dựng thư viện mẫu tác vụ/hành động từ lịch sử quỹ đạo của mô hình chủ.

2. Áp dụng ràng buộc state-bound (gắn kết dựa trên trạng thái): trước khi thực thi hành động, kiểm tra xem nó có trong tập hành động chấp nhận được của môi trường hay không. Cho ai: tác tử tương tác với môi trường có danh sách hành động hợp lệ rời rạc. Bước đầu: viết hàm kiểm tra hành động tồn tại trong tập At trước khi thực thi.

3. Áp dụng cơ chế abstention (từ chối an toàn): khi không có kỹ năng phù hợp hoặc gắn kết thất bại, trả quyền về lập kế hoạch chủ thay vì suy đoán. Cho ai: tác tử cần hành động an toàn trong môi trường không chắc chắn. Bước đầu: thêm quy tắc "nếu không chắc, trả về host" vào tầng chọn hành động.

## WISDOM — Nguyên tắc tổng quát

- Nguyên tắc: Phân tách việc nhớ kinh nghiệm (retrieval) khỏi việc thực thi (execution) — lớp bên ngoài chỉ được chọn trong một tập hành động hữu hạn đã được ràng buộc bởi trạng thái, không được sinh lệnh tự do. Áp dụng khi tác tử đệ quy gọi mô hình lớn quá nhiều lần cho tác vụ lá. Không áp dụng khi hành động liên tục hoặc không có giao diện hành động rời rạc.

## Assumptions & Limitations

- Điều kiện phải đúng: có các tác vụ lá xuất hiện lặp lại và có thể tham số hóa, giao diện hành động rời rạc chấp nhận được, và bộ biến đổi môi trường.
- Limitation paper thừa nhận: LeafSkill giả định các lá tham số hóa lặp lại, một giao diện hành động rời rạc và một bộ biến đổi môi trường; ngữ pháp hành động mới yêu cầu bộ biến đổi và trình gắn kết tương ứng; hành động mở hoặc liên tục có thể cần giao diện hành động thực thi phong phú hơn; bằng chứng hiện tại chỉ bao gồm một lập kế hoạch, một mô chủ, hai môi trường và một họ trình chọn.
- Limitation paper KHÔNG nói: hiệu quả trên các tác tử lớn hơn 27B, chi phí vận hành của trình chọn trên quy mô lớn, và khả năng mở rộng sang các môi trường thực tế bên ngoài Robotouille và ALFWorld.

## Metadata

- Năm: 2026
- Tác giả: Shen Liu, Ze Zhou, Zhenguo Xu, Shaopu Wang, Yike Gao, Chunlei Wang
- Category arXiv: cs.AI
- Link PDF: https://arxiv.org/pdf/2610.32412v1
- Citation count: [không tìm được]