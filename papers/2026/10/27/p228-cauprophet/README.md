# 2610.32477 — CauProphet: Teaching Agents to Develop Causal Cognition like Humans

## Giá trị cốt lẽ (1 câu)

CauProphet là agent phát triển và cập nhật triết nhân quả (causal knowledge) qua trải nghiệm, kết nối Triết Nhân Quả (Causal Cognition) với Tin Tín Nhân Quả (Causal Belief) để ra quyết định — trong nghiên cứu tài chính, đạt cải thiện 25,4% so với agent baseline về tương quan hạng với lợi nhuận ngày sau, và nâng độ chính xác dự đoán từ 21,3% lên 28,6% trong môi trường thực tế thay đổi.

## Problem

Các agent LLM hiện đại chủ yếu truy xuất bản tóm tắt hoặc bản ghi quá khứ, thiếu khả năng hình thành và tinh chỉnh hiểu biết nhân quả về thế giới. Khi gặp tác vụ dài hạn, agent không thể xây dựng hiểu biết nhân quả tồn tại dài hạn từ kinh nghiệm để áp dụng vào quyết định mới — chúng chỉ lấy lại các bản ghi hoặc tóm tắt, không có triết nhân quả có cấu trúc (structured causal knowledge) để định hướng hành động.

## Contribution

1. **CauProphet**: Agent phát triển và cập nhật triết nhân quả bên trong Triết Nhận thức Nhân Quả (Causal Cognition). Mỗi tác vụ, CauProphet kết hợp tri thức liên quan từ Triết Nhận thức Nhân Quả với bằng chứng hiện tại để xây dựng Tin Tín Nhân Quả (Causal Belief), một tin tín có cấu trúc ghi nhận các yếu tố nhân quả và tác động của các hành động có thể.
2. **Causal Scout**: Công cụ so sánh các giải thích cạnh tranh và gợi ý các quan sát có thể phân biệt chúng, giúp agent điều tra các giải thích competing.
3. **Cập nhật liên tục**: Causal Belief và Causal Cognition được cập nhật liên tục khi quan sát mới xuất hiện, cho phép triết nhân quả tồn tại vượt qua các trải nghiệm riêng lẻ.
4. **Thí nghiệm tài chính**: CauProphet vượt trội hơn tất cả các baseline về tương quan hạng trung bình (mean rank correlation) với lợi nhuận ngày sau, cải thiện 25,4% so với agent baseline; cải thiện độ chính xác dự đoán từ 21,3% lên 28,6% trong cài đặt thực tế động (dynamic real-world settings).

## Method

CauProphet xem mỗi tác vụ như một quá trình quyết định có thể quan sát một phần (POMDP), trong đó agent dựa vào một tin tín về môi trường mà không thể quan sát đầy đủ.

**Cấu trúc chính:**

1. **Triết Nhận thức Nhân Quả (Causal Cognition)**: Tổ chức tri thức được giữ lại xung quanh các giải thích về cách các yếu tố lặp đi lặp lại ảnh hưởng lẫn nhau, cùng với các điều kiện, th�oi gian, bằng chứng và câu hỏi chưa giải quyết. Đồ thị kết nối các yếu tố thông qua các mối quan hệ nhân quả được đề xuất.

2. **Tin Tín Nhân Quả (Causal Belief)**: Tin tín có cấu trúc ghi nhận những gì ảnh hưởng đến kết quả và cách các hành động có thể có thể thay đổi nó, định hướng quyết định của agent. Được hình thành bằng cách kết hợp tri thức từ Triết Nhận thức Nhân Quả với bằng chứng hiện tại.

3. **Causal Scout**: So sánh các giải thích thay thế và gợi ý các quan sát có thể phân biệt chúng.

4. **Causal Toolbox**: Công cụ chẩn đoán dữ liệu, suy luận nhân quả, kiểm tra giả thuyết.

**Quy trình:** Quan sát → Phân tích → Xây dựng Causal Belief → Chọn hành động → Cập nhật Causal Belief và Triết Nhận thức Nhân Quả.

## KNOWLEDGE — Số liệu & khái niệm

- Mô hình cơ sở: DeepSeek-V4-Pro (mã nguồn mở, hỗ trợ tái sản xuất, hiệu suất tổng thể mạnh với chi phí thấp).
- Baselines: ReAct, OpenCode (khuôn khỏ mã nguồn mở với hơn 200.000 sao GitHub).
- Nghiên cứu tài chính: Sử dụng AlphaBench, tác vụ tìm kiếm yếu tố (factor-search) yêu cầu agent xây dựng công thức xếp hạng cổ phiếu theo lợi nhuận ngày sau dự đoán.
- Hai nghiên cứu sáu kỳ: nghiên cứu giá-giao dịch 2014–2016 và nghiên cứu chỉ giao dịch 2017–2019.
- Cải thiện 25,4% so với agent baseline về tương quan hạng với lợi nhuận ngày sau.
- Nâng độ chính xác dự đoán từ 21,3% lên 28,6% trong cài đặt thực tế động.
- Mỗi tác vụ bắt đầu trong bối cảnh mới (fresh context); agent có bộ nhớ có thể truy xuất các phát hiện trước đó.

## INSIGHT — Cơ chế & tại sao

[Agent có thể phát triển triết nhân quả tồn tại dài hạn] xảy ra VÌ [Triết Nhận thức Nhân Quả tổ chức tri thức xung quanh các giải thích về cách các yếu tố ảnh hưởng lẫn nhau, cùng với điều kiện, th�oi gian, bằng chứng và câu hỏi chưa giải quyết; đồ thị kết nối các yếu tố thông qua mối quan hệ nhân quả]. Điều này nghĩa là [tri thức nhân quả có thể được tích lũy và sử dụng lại qua các tác vụ, không chỉ bị hạn chế trong bối cảnh hiện tại].

[Causal Belief định hướng quyết định tốt hơn] xảy ra VÌ [tin tín có cấu trúc ghi nhận yếu tố nhân quả và tác động của các hành động có thể, được hình thành từ kết hợp tri thức đã lưu và bằng chứng hiện tại]. Điều này nghĩa là [agent ra quyết định dựa trên hiểu biết nhân quả, không chỉ là tương quan bề mặt].

[Causal Scout giúp phân biệt giải thích cạnh tranh] xảy ra VÌ [công cụ so sánh các giải thích thay thế và gợi ý quan sát có thể phân biệt chúng]. Điều này nghĩa là [agent có thể điều tra và xác nhận mối quan hệ nhân quả thay vì chỉ dựa trên tương quan].

## IDEA — Áp dụng được gì

1. Xây dựng bộ nhớ nhân quả cho agent phân tích tài chính: Thay vì chỉ truy xuất tóm tắt giao dịch trước, hãy xây dựng Triết Nhận thức Nhân Quả chứa các mối quan hệ nhân quả giữa các yếu tố thị trường (ví dụ: giá giao dịch, khối lượng, biến động) và điều kiện áp dụng. Bước đầu: tạo cơ sở dữ liệu nhân quả lưu trữ các giả thuyết nhân quả và bằng chứng hỗ trợ từ các phiên phân tích trước.

2. Áp dụng Causal Belief trong quy trình ra quyết định doanh nghiệp: Trước khi ra quyết định quan trọng, agent cần xây dựng Tin Tín Nhân Quả có cấu trúc ghi nhận những yếu tố ảnh hưởng đến kết quả và cách các hành động có thể thay đổi nó. Bước đầu: thiết kế mẫu Tin Tín Nhân Quả với các trường: yếu tố nhân quả, tác động dự kiến, bằng chứng hỗ trợ, điều kiện áp dụng.

3. Dùng Causal Scout để kiểm tra giả thuyết trong nghiên cứu khoa học: Khi có nhiều giải thích cho một hiện tượng, hãy dùng công cụ so sánh các giải thích thay thế và gợi ý quan sát có thể phân biệt chúng. Bước đầu: liệt kê các giả thuyết cạnh tranh, xác định quan sát quan trọng nhất để kiểm tra từng giả thuyết.

## WISDOM — Nguyên tắc tổng quát

- Nguyên tắc: Agent thông minh không chỉ cần ghi nhớ kinh nghiệm, mà cần hình thành hiểu biết nhân quả có cấu trúc để áp dụng vào tình huống mới — tri thức nhân quả tồn tại vượt qua trải nghiệm riêng lẻ.
- Khi nào dùng: Khi xây dựng agent cho tác vụ dài hạn đòi hỏi hiểu biết về nhân quả và nguyên nhân (phân tích tài chính, nghiên cứu khoa học, quy trình ra quyết định phức tạp).
- Khi nào KHÔNG dùng: Tác vụ đơn giản chỉ cần truy xuất thông tin, không cần hiểu nhân quả.
- Ví dụ áp dụng ngoài domain gốc: Trong chẩn đoán y tế, bác sĩ không chỉ cần ghi nhớ triệu chứng của bệnh nhân trước, mà cần hiểu rõ quan hệ nhân quả giữa các yếu tố rủi ro và bệnh để đưa ra quyết định điều trị phù hợp cho bệnh nhân mới có tình trạng khác.

## Assumptions & Limitations

- Điều kiện phải đúng: bằng chứng đủ để kiểm tra các mối quan hệ nhân quả; mô hình cơ sở có kiến thức tiên nghiệm tốt khi bằng chứng không đủ.
- Limitation paper thừa nhận: Khi bằng chứng không đủ để kiểm tra quan hệ nhân quả, CauProphet dựa nhiều hơn vào kiến thức tiên nghiệm của mô hình cơ sở; thí nghiệm bao gồm số giai đoạn hạn chế; cần nghiên cứu dài hơn trong môi trường thực tế thay đổi.
- Limitation paper KHÔNG nói: Hiệu quả trên các tác vụ không có cấu trúc nhân quả rõ ràng; chi phí duy trì Triết Nhận thức Nhân Quả ở quy mô lớn; tính generalize qua các domain khác nhau bên ngoài tài chính và khoa học.

## Metadata

- Năm: 2026
- Tác giả: Kaiwen Wu, Chaochao Lu
- Category arXiv: cs.AI
- Link PDF: https://arxiv.org/pdf/2610.32477
- Citation count: chưa có (paper mới, Oct 2026)