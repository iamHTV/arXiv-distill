# 2610.31743 — Not Every Agent Needs the Strongest Model: Unified Prompt–Model Optimization for Heterogeneous LLM-based Multi-Agent Systems

## Giá trị cốt lẽ (1 câu)

Không phải mọi agent trong hệ thống multi-agent LLM đều cần mô hình mạnh nhất — UniMASO tối ưu hóa đồng thời prompt và phân bổ mô hình theo vai trò, đạt điểm trung bình 70,40 (tăng từ 69,79) trong khi giảm chi phí triển khai có trọng số token 85,2% so với cấu trúc đồng nhất dùng DeepSeek-V4-Pro.

## Problem

Tối ưu hóa prompt trong hệ thống multi-agent LLM thường giữ nguyên phân bổ mô hình, bỏ qua sự khác biệt trong yêu cầu vai trò và chi phí suy luận (inference cost) liên quan. Điều này dẫn đến việc dùng mô hình mạnh nhất cho mọi agent, gây ra chi phí triển khai không cần thiết mà không cải thiện đáng kể chất lượng tác vụ.

## Contribution

1. **UniMASO**: Khung làm việc thống nhất cho tối ưu hóa hệ thống multi-agent đa dạng (heterogeneous) thông qua sự thích ứng đồng thời của prompt và phân bổ mô hình (joint prompt–model adaptation).
2. **Đánh giá đa cấp (multi-level feedback)**: UniMASO đánh giá các bản cập nhật ứng viên thông qua phản hồi cục bộ (local), tiếp cận (downstream) và toàn cầu (global).
3. **Tìm kiếm Pareto có nhận thức chi phí (cost-aware Pareto search)**: Giữ lại các trade-off chất lượng–chi phí hữu ích.
4. **Sự tiến hóa chung có nhận thức cấu trúc liên lạc (topology-aware co-evolution)**: Điều phối các bản cập nhật theo vai trò agent và các phụ thuộc (dependency).
5. **Bộ nhớ quỹ đạo crosses cấp (cross-level trajectory memory)**: Cung cấp thành công và thất bại trong lịch sử để hướng dẫn tối ưu hóa tiếp theo.
6. **Kết quả thí nghiệm**: Trên 5 tiêu chuẩn (benchmarks) và 5 cấu trúc thực thi (execution topologies), UniMASO đạt hiệu suất tác vụ cạnh tranh với chi phí triển khai thấp hơn nhiều so với cấu trúc đồng nhất mạnh nhất. Thực thi tập trung (centralized execution): cải thiện điểm trung bình từ 69,79 lên 70,40 trong khi giảm chi phí triển khai có trọng số token 85,2% so với DeepSeek-V4-Pro kèm MASPO.

## Method

UniMASO hoạt động qua các thành phần chính:

1. **Đánh giá đa cấp (multi-level feedback)**: Đánh giá bản cập nhật ứng viên qua phản hồi cục bộ (tác vụ agent đơn lẻ), tiếp cận (tác vụ downstream ảnh hưởng) và toàn cầu (hệ thống 전체).

2. **Tìm kiếm Pareto có nhận thức chi phí (cost-aware Pareto search)**: Tìm kiếm các bản cập nhật tối ưu về mặt chi phí, giữ lại các trade-off chất lượng–chi phí hữu ích thay vì chỉ tối ưu hóa chất lượng.

3. **Sự tiến hóa chung có nhận thức cấu trúc liên lạc (topology-aware co-evolution)**: Điều phối các bản cập nhật theo vai trò agent và các phụ thuộc trong cấu trúc liên lạc (communication topology).

4. **Bộ nhớ quỹ đạo crosses cấp (cross-level trajectory memory)**: Lưu trữ thành công và thất bại trong lịch sử để hướng dẫn tối ưu hóa tiếp theo.

**Quy trình:** Đánh giá ứng viên → Tìm kiếm Pareto → Điều phối theo cấu trúc liên lạc → Cập nhật prompt và mô hình → Lưu quỹ đạo → Lặp lại.

## KNOWLEDGE — Số liệu & khái niệm

- 5 tiêu chuẩn đánh giá (benchmarks), 5 cấu trúc thực thi (execution topologies).
- Điểm trung bình thực thi tập trung: 69,79 (baseline) → 70,40 (UniMASO).
- Giảm chi phí triển khai có trọng số token (token-weighted deployment cost) 85,2% so với DeepSeek-V4-Pro kèm MASPO.
- Code: https://github.com/Achilles008/UniMASO_main
- Phân bổ mô hình khác nhau cho các agent khác nhau dựa trên yêu cầu vai trò.

## INSIGHT — Cơ chế & tại sao

[Không phải mọi agent đều cần mô hình mạnh nhất] xảy ra VÌ [các vai trò agent khác nhau có yêu cầu khác nhau về năng lực và chi phí suy luận; gán mô hình mạnh nhất cho mọi agent gây ra chi phí không cần thiết]. Điều này nghĩa là [phân bổ mô hình theo vai trò (heterogeneous model assignment) có thể giảm chi phí đáng kể mà không mất chất lượng].

[Tối ưu hóa đồng thời prompt và mô hình] xảy ra VÌ [prompt và mô hình tương tác với nhau — một prompt tốt có thể bù đắp cho mô hình yếu hơn, và một mô hình mạnh có thể bù đắp cho prompt kém hơn; tối ưu hóa riêng lẻ bỏ qua sự tương tác này]. Điều này nghĩa là [joint prompt–model adaptation hiệu quả hơn tối ưu hóa từng thành phần riêng rẽ].

[Tìm kiếm Pareto có nhận thức chi phí] xảy ra VÌ [cần giữ lại các trade-off chất lượng–chi phí hữu ích, không chỉ tìm điểm chất lượng cao nhất bất kể chi phí]. Điều này nghĩa là [các nhà phát triển nên xem xét cả chất lượng và chi phí khi thiết kế hệ thống multi-agent].

## IDEA — Áp dụng được gì

1. Phân bổ mô hình theo vai trò trong hệ thống multi-agent: Thay vì dùng mô hình mạnh nhất cho mọi agent, hãy gán mô hình nhỏ cho các agent chỉ xử lý định dạng (formatting) và mô hình lớn cho các agent cần suy luận sâu. Bước đầu: phân loại các agent trong hệ thống theo vai trò và yêu cầu suy luận, sau đó gán mô hình phù hợp.

2. Tối ưu hóa đồng thời prompt và mô hình: Thay vì tối ưu hóa prompt riêng rẽ sau đó mới chọn mô hình, hãy tìm kiếm đồng thời cặp (prompt, mô hình) tối ưu cho mỗi vai trò. Bước đầu: thiết lập không gian tìm kiếm chứa các cặp prompt-mô hình và dùng tìm kiếm Pareto để tìm các trade-off hữu ích.

3. Dùng bộ nhớ quỹ đạo (trajectory memory) để hướng dẫn tối ưu hóa: Lưu trữ các thành công và thất bại trong lịch sử tối ưu hóa để tham khảo cho các vòng tiếp theo. Bước đầu: ghi lại kết quả mỗi vòng tối ưu hóa (prompt, mô hình, điểm số, chi phí) và dùng để lọc các ứng dụng không tiềm năng.

## WISDOM — Nguyên tắc tổng quát

- Nguyên tắc: Trong hệ thống multi-agent LLM, không phải mọi agent đều cần mô hình mạnh nhất; phân bổ mô hình theo yêu cầu vai trò và tối ưu hóa đồng thời prompt-mô hình có thể giảm chi phí lớn mà không hy sinh chất lượng.
- Khi nào dùng: Khi xây dựng hệ thống multi-agent với nhiều agent có vai trò khác nhau và chi phí suy luận là vấn đề quan tâm.
- Khi nào KHÔNG dùng: Hệ thống chỉ có một agent hoặc tất cả agent đều cần cùng mức độ năng lực.
- Ví dụ áp dụng ngoài domain gốc: Trong đội chăm sóc khách hàng, agent xử lý câu hỏi thường dùng (FAQ) có thể dùng mô hình nhỏ và rẻ, trong khi agent xử lý khiếu nại phức tạp dùng mô hình lớn — giảm tổng chi phí vận hành mà không ảnh hưởng chất lượng dịch vụ.

## Assumptions & Limitations

- Điều kiện phải đúng: hệ thống multi-agent có nhiều agent với vai trò khác nhau; có thể đo đạc chi phí suy luận (inference cost) của từng mô hình.
- Limitation paper thừa nhận: thí nghiệm trên 5 tiêu chuẩn và 5 cấu trúc thực thi; có thể không đại diện cho tất cả các trường hợp thực tế.
- Limitation paper KHÔNG nói: hiệu quả trên hệ thống multi-agent với cấu trúc liên lạc thay đổi động (dynamic topology) ở quy mô lớn; chi phí triển khai bộ nhớ quỹ đạo crosses cấp.

## Metadata

- Năm: 2026
- Tác giả: Mingxiu Cai, Haoyang Xian, Xinyu Ma, Yutong Wang, Zhenxi Song, Jing Li, Xuebo Liu
- Category arXiv: cs.AI
- Link PDF: https://arxiv.org/pdf/2610.31743
- Citation count: chưa có (paper mới, Oct 2026)