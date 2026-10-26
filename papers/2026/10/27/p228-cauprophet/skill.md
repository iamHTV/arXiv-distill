# Skill: cauprophet-causal-cognition-agent

Source: 2610.32477
Type: framework

## Khi nào dùng skill này

- Xây dựng agent cần phát triển hiểu biết nhân quả từ kinh nghiệm và áp dụng vào quyết định mới.
- Tác vụ dài hạn đòi hỏi agent ghi nhớ và sử dụng lại tri thức nhân quả qua nhiều phiên.
- Phân tích tài chính, nghiên cứu khoa học hoặc quy trình ra quyết định cần hiểu nhân quả, không chỉ tương quan.

## Tình huống KHÔNG nên dùng

- Tác vụ đơn giản chỉ cần truy xuất thông tin, không cần hiểu nhân quả.
- Không có bằng chứng đủ để kiểm tra mối quan hệ nhân quả.

## Input cần có

- Dữ liệu lịch sử về các tác vụ và kết quả đã thực hiện.
- Môi trường có thể cung cấp bằng chứng và quan sát mới liên tục.
- Công cụ suy luận nhân quả (causal inference toolbox).

## Các bước thực hiện

1. Xây dựng Triết Nhận thức Nhân Quả (Causal Cognition): tổ chức tri thức xung quanh các giải thích về cách các yếu tố ảnh hưởng lẫn nhau, cùng với điều kiện, th�oi gian, bằng chứng và câu hỏi chưa giải quyết.
2. Xây dựng Tin Tín Nhân Quả (Causal Belief): kết hợp tri thức từ Triết Nhận thức Nhân Quả với bằng chứng hiện tại để tạo tin tín có cấu trúc ghi nhận yếu tố nhân quả và tác động của các hành động có thể.
3. Dùng Causal Scout: so sánh các giải thích thay thế và gợi ý quan sát có thể phân biệt chúng.
4. Ra quyết định dựa trên Tin Tín Nhân Quả: chọn hành động dựa trên hiểu biết nhân quả, không chỉ tương quan.
5. Cập nhật liên tục: khi quan sát mới xuất hiện, sửa đổi Tin Tín Nhân Quả và cập nhật Triết Nhận thức Nhân Quả.
6. Áp dụng tri thức đã lưu vào tác vụ mới: truy xuất Triết Nhận thức Nhân Quả liên quan và kết hợp với bằng chứng hiện tại.

## Output mong đợi

- Triết Nhận thức Nhân Quả chứa các mối quan hệ nhân quả và điều kiện áp dụng.
- Tin Tín Nhân Quả cho mỗi tác vụ, định hướng quyết định.
- Tri thức nhân quả được cập nhật liên tục, tồn tại vượt quá trải nghiệm riêng lẻ.

## Ví dụ áp dụng

Đội phân tích chứng khoán dùng CauProphet: agent xây dựng Triết Nhân Quả về các yếu tố ảnh hưởng đến lợi nhuận cổ phייה (giá, khối lượng, biến động, tin tức thị trường). Trong kỳ phân tích mới, agent kết hợp tri thức đã lưu với bằng chứng hiện tại để xây dựng Tin Tín Nhân Quả, chọn công thức xếp hạng cổ phiếu, và đạt cải thiện 25,4% so với agent không có trí tuệ nhân quả.

## Gotchas

- Khi bằng chứng không đủ, agent dựa nhiều vào kiến thức tiên nghiệm của mô hình cơ sở.
- Thí nghiệm bao gồm số giai đoạn hạn chế; cần nghiên cứu dài hơn.
- Không phải mọi tác vụ đều có cấu trúc nhân quả rõ ràng.