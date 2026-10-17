# [2610.01833v1] Continuous Process-Level Evaluation for Evolving Enterprise AI Agent Skills

## Problem
- Kỹ năng agent doanh nghiệp (enterprise AI agent skill) không phải artifact tĩnh — được chỉnh sửa liên tục khi tool API thay đổi, phiên bản LLM cập nhật, hoặc spec được tinh chỉnh từ phản hồi vận hành. Prior work chưa giải quyết được sai lệch hành vi trong quá trình tiến hóa (process-level behavioral drift) — vì chỉ kiểm tra độ chính xác đầu ra cuối cùng (final-output accuracy), bỏ sót các sai lệch quy trình như gọi API sai phạm vi, bỏ bước đọc lại database, ghi kết quả trung gian vào bảng sai.

## Contribution
- Khung đánh giá liên tục (continuous evaluation framework) kết hợp kiểm tra kết quả (outcome-level) và kiểm tra quá trình (process-level quality checks) cho kỹ năng agent doanh nghiệp.
- Pipeline năm giai đoạn độc lập với phiên agent đang được đánh giá: (1) thu thập đầu vào + phân tích dấu vết gọi công cụ, (2) tính căn cứ thực sự (ground truth) qua gọi API độc lập, (3) hóa test case mẫu (template test cases), (4) đánh giá (kết quả + quy trình), (5) báo cáo lỗi gốc (cascade attribution).
- Template test case dùng chỗ trống giải quyết tại runtime (runtime-resolved placeholders) thay vì giá trị hardcode, cung cấp phạm vi hồi quy tái sử dụng.

## Method (tóm tắt cốt lõi)
- Giai đoạn 1: Agent ghi lại tham số đầu vào vào log có cấu trúc; bắt toàn bộ dấu vết gọi công cụ (tool name, arguments, return value, turn index) từ harness execution log.
- Giai đoạn 2: Script Python độc lập gọi cùng API thực qua đường dẫn thực thi riêng, tính giá trị預 kiến cho mỗi ứng dụng.
- Giai đoạn 3: Template test case mô tả hành vi mong muốn skill dùng placeholder giải quyết tại runtime (ví dụ: $k8s_host_date_calls); liên kết phụ thuộc (depends_on) định nghĩa thất bại gốc và hiệu ứng Cascading.
- Giai đoạn 4: Ba lớp đánh giá — L1: giá trị cuối cùng định trước; L2: bảy kiểm tra trạng thái cuối cùng per skill; L3: kiểm tra quỹ đạo (trajectory checks) trên 4 chiều: tool selection, tool arguments, tool ordering, argument scope. LLM judge chỉ dùng cho các kiểm tra dễ gãy (brittle) khi khớp chính xác không ổn định.
- Giai đoạn 5: Khi kiểm tra thất bại, framework đi qua đồ thị phụ thuộc để phân biệt lỗi gốc (root failure) từ thất bại Cascading.

## Key Findings
- 240 thử thách tự động, 2 kỹ năng (Revenue: 104 test case; Productivity: 80 test case), 2 spec variant (SKILL.md, Skill.txt), 2 harness (Claude Code, Codex), 3 model (GPT-5.6-Sol, Claude Opus 4.8, Claude Sonnet 4.6).
- 175/240 vượt tất cả kiểm tra số liệu cuối cùng áp dụng; trong số đó, 162 (92.6%; Wilson 95% CI: 87.7–95.6%) vẫn có ít nhất một sự lệch phát hiện bởi evaluator → kiểm tra giá trị cuối cùng alone bỏ sót sai lệch trong 67.5% tất cả thử thách.
- 164/240 vượt tất cả bảy kiểm tra trạng thái cuối cùng; trong số đó, 151 (92.1%; 95% CI: 86.9–95.3%) vẫn vi phạm ít nhất một kiểm tra quỹ đạo.
- Thuộc tính gốc (dependency attribution) nén trung bình 6.34 kiểm tra thất bại xuống 2.65 gốc (−58%).
- Không cấu hình nào đạt 100% điểm trung bình suite; sai lệch Revenue tối đa một xu.

## Actionable Insights
1. Kết hợp kiểm tra kết quả và kiểm tra quy trình trong pipeline đánh giá để phát hiện sai lệch hành vi dù kết quả cuối vẫn đúng. Áp dụng: thêm process check layer vào pipeline đánh giá agent doanh nghiệp — kiểm tra tool selection, arguments, ordering, scope bên cạnh final value check.
2. Dùng template test case với placeholder giải quyết tại runtime thay vì hardcode giá trị để tái sử dụng suite hồi quy khi spec thay đổi. Áp dụng: viết template test case với placeholder như $k8s_host_date_calls, giải quyết tại runtime từ ground truth, cùng đồ thị phụ thuộc để quy gom kiểm tra thất bại về nguyên nhân gốc.

## Assumptions & Limitations
- Một hệ thống enterprise duy nhất và hai kỹ năng liên quan; khái quát hóa đến các loại kỹ năng khác, tool suite, hoặc đầu ra không phải định lượng vẫn còn mở.
- 10 lần thử mỗi ô hạn chế sức mạnh thống kê cho hiệu ứng nhỏ.
- Nhãn gốc (root labels) không được độc lập xác nhận là giải thích nhân quả.
- Xác thực dài hạn (longitudinal validation) dưới sự thay đổi thực tế của API vẫn là công việc tương lai.

## Metadata
- Năm: 2026, tác giả: Ngoc Phuoc An Vo (IBM), Aarya Doshi (Georgia Tech), Vadim Sheinin (IBM), category arXiv: cs.AI, link PDF: https://arxiv.org/pdf/2610.01833v1
