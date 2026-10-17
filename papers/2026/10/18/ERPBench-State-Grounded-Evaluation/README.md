# [2609.17885v2] ERPBench: A State-Grounded Evaluation Paradigm for Computer-Use Agents in Enterprise Software

## Problem
Computer-use agents (CUA) hoạt động qua chụp màn hình và hành động mô phỏng đang phát triển nhanh, nhưng đánh giá vẫn gắn bó với tác vụ desktop và web chung. Hệ thống ERP (Enterprise Resource Planning) chạy tài chính, mua hàng, tồn kho, và khách hàng của tổ chức trên toàn thế giới,posing thách thức riêng biệt cho CUA: giao diện dày đặc, tương tác nhiều bước phối hợp, và lỗi thay đổi bản ghi kinh doanh lâu dài chứ không chỉ hiện trên màn hình. Các benchmark enterprise computer-use hiện có dựa trên nền tảng độc quyền hoặc trên sự xấp xỉ mô phỏng của phần mềm đó. Một tương tác thị giác có vẻ đúng không đủ: agent có thể điều hướng đến màn hình đúng, nhấn các điều khiển mong đợi, và quan sát thông báo thành công, nhưng để lại bản ghi kinh doanh sai hoặc chưa thay đổi. Thông báo kết quả chỉ cho thấy giao diện chấp nhận hành động, không phải giá trị dự định đã đến cơ sở dữ liệu.

## Contribution
- Giới thiệu ERPBench, một benchmark đánh giá agent chỉ từ chụp màn hình (screenshot-only) trên hệ thống sống và có thể tái tạo, và chấm mỗi tác vụ so với giá trị ground-truth trong cơ sở dữ liệu.
- Trình bày một harness cấp sản xuất (production-grade harness) cổng hành động agent sau sự chấp thuận từ con người để triển khai an toàn.
- Đánh giá sáu agent đóng và mã nguồn mở, chứng minh hiệu suất tổng thể mạnh không chuyển sang độ tin cậy doanh nghiệp.
- Nhận diện các mode lỗi cụnt đến workflow doanh nghiệp.

## Method
- ERPBench xây dựng trên một instance ERPNext tự lưu trữ (self-hosted), mã nguồn mở, spanning tài chính, mua hàng, tồn kho, và quản lý khách hàng.
- Agent chỉ hoạt động từ chụp màn hình, mỗi tác vụ được chấm so với giá trị ground-truth trong database.
- Ba thành phần chấm: Database grader (đọc giá trị trường mục tiêu từ ERPNext qua Frappe REST API sau khi chạy), Stage grader (chước điểm phần theo thứ tự: Navigation, Interaction, Commit, Database), Log grader (đọc log hành động và lượt cho số lần hành động, thời gian, chi phí token).
- Harness chạy ở hai chế độ: Triển khai (dành hành động commit hoặc irreversible lên phê duyệt của con người trước khi thực thi) và Đánh giá (auto-approver chấp nhận mọi hành động).
- 6 agent được đánh giá: Claude Sonnet 4.6, Qwen3-VL-32B, OpenCUA-32B, UI-TARS-1.5-7B, OpenCUA-7B, Holo3-35B-A3B.
- Ba tier độ phức tạp: T1 (20 tác vụ đơn bản ghi: chỉnh sửa văn bản, chọn/bật, tạo), T2 (phối hợp nhiều trường liên quan, 6-9 trường mỗi bản ghi), T3 (luồng làm việc nhiều màn hình liên kết, 2-4 bản ghi ERPNext phụ thuộc lẫn nhau).
- Mỗi tác vụ chạy 5 lượt độc lập trong cùng cấu hình và chấm điểm.

## Key Findings
- Claude Sonnet 4.6 đạt 94% (T1), 100% (T2), 100% (T3), gần mức tham chiếu con người.
- Holo3-35B-A3B và Qwen3-VL-32B chỉ đạt 34% và 32% ở T1, rơi xuống 0–3% ở T2 và T3.
- OpenCUA-7B thất bại mọi tác vụ.
- Một số agent lưu trong tới 85% số lần chạy nhưng ghi giá trị chính xác ở chỉ 3% số lần chạy.
- UI-TARS đạt mục tiêu trong 95% số lần chạy và nhấn lưu trong 68%, nhưng chỉ 9% để lại giá trị chính xác trong cơ sở dữ liệu.
- Hiệu suất GUI tổng thể mạnh không chuyển sang độ tin cậy doanh nghiệp.
- Con người đạt 96–100% trên T1, 90–95% trên T2, 87–100% trên T3.

## Actionable Insights
1. Đánh giá agent trên trạng thái cơ sở dữ liệu (state-grounded), không chỉ chụp màn hình. Áp dụng: khi xây dựng agent tương tác với phần mềm doanh nghiệp, hãy kiểm tra giá trị trường trong database sau khi agent thực thi, không chỉ tin tưởng vào thông báo thành công trên màn hình. Bước đầu: Thiết lập cơ sở dữ liệu test và viết script kiểm tra giá trị trường mục tiêu sau mỗi lần chạy agent.
2. Sử dụng harness có cổng phê duyệt con người cho hành động rủi ro. Áp dụng: các hành động commit hoặc irreversible (xóa bản ghi, gửi tiền) phải được con người phê duyệt trước khi thực thi. Bước đầu: Thêm bước chờ xác nhận từ người dùng trước khi thực hiện hành động ghi dữ liệu hoặc gửi thông báo.
3. Phân rã chạy agent thành các giai đoạn (Navigation, Interaction, Commit, Database) để định vị nơi thất bại. Áp dụng: khi đánh giá agent, hãy chấm điểm từng giai đoạn riêng biệt thay vì chỉ chấm thành công/thất bại tổng thể. Bước đầu: Ghi log mỗi giai đoạn của agent và định loại thất bại theo giai đoạn.

## Assumptions & Limitations
- Đánh giá trên ERPNext (mã nguồn mở), kết quả có thể khác trên hệ thống ERP độc quyền (SAP, Oracle).
- Chỉ đánh giá 6 agent, không generalize sang tất cả CUA.
- Các tác vụ là synthetic (được tạo trước), có thể không đại diện cho các tác vụ doanh nghiệp thực tế.
- Môi trường test chạy trong Docker, có thể khác với môi trường produzione thực tế.

## Metadata
- Năm: 2026, tác giả: Kratika Bhagtani, Kusha Sridhar, Maziyar Baran Pouyan, Yuying Zhao, Eugene Siow (Accenture Agentic AI Center of Excellence), category arXiv: cs.AI, link PDF: https://arxiv.org/pdf/2609.17885v2