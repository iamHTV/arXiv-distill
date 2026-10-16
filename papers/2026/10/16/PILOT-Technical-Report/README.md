# [2608.18637v2] PILOT Technical Report

## Problem
Các phương pháp agentic hiện tại cho tối ưu hóa hệ thống khuyến nghị (recommendation system) vẫn mang tính responsive (phản ứng) — chúng điều chỉnh tham số theo phản ứng với các thay đổi số liệu nhưng thiếu khả năng thiết kế chính chủ các thí nghiệm kiểm soát, cá nhân hóa chiến lược theo cấp độ phân khúc người dùng, và tích lũy phương pháp luận thí nghiệm có thể tái sử dụng giữa các tác vụ.

## Contribution
- Giới thiệu PILOT (Proactive Insight Learner for Online Tree-Experiments): framework LLM-agent tổ chức ba vai trò trong một constrained control loop (vòng lặp kiểm soát có ràng buộc) nơi các deterministic services (dịch vụ xác định) thực thi tất cả ranh giới an toàn, thống kê, và quyền限限: (1) Experiment Manager điều hướng toàn bộ vòng đời thí nghiệm, (2) v.v.
- PILOT đạt lên đến +1.40% IPV, +1.60% Core IPV, +0.96% transaction count, +1.50% transaction amount.
- Cải thiện so với kết quả tốt nhất của ROAM (+1.00% IPV, +0.90% Core IPV, +0.60% transaction count, +1.13% transaction amount).
- Nâng cao search efficiency từ 53.3% lên 93.3% (+40pp), không cần can thiệp của con người trong suốt quá trình thí nghiệm.

## Method (tóm cốt lõi)
PILOT tổ chức ba vai trò agent trong một vòng lặp kiểm soát có ràng buộc: Experiment Manager (quản lý vòng đời thí nghiệm), Insight Learner (học phần định về phần định), v.v. Các deterministic services thực thi ranh giới an toàn, thống kê, và quyền hạn. PILOT tự thiết kế thí nghiệm, cá nhân hóa chiến lược theo phân khúc người dùng, và tích lũy phương pháp luận thí nghiệm.

## Key Findings
- PILOT đạt lên đến +1.40% IPV, +1.60% Core IPV, +0.96% transaction count, +1.50% transaction amount.
- Cải thiện so với ROAM's best results (+1.00% IPV, +0.90% Core IPV, +0.60% transaction count, +1.13% transaction amount).
- Nâng cao search efficiency từ 53.3% lên 93.3% (+40pp).
- Không cần can thiệp của con người trong suốt quá trình thí nghiệm.
- Best-performing bucket đạt +1.40% IPV, +1.60% Core IPV, +0.96% transaction count, +1.50% transaction amount.

## Actionable Insights
- Dùng agent để tự thiết kế và chạy thí nghiệm A/B thay vì chỉ phản ứng theo số liệu. Áp dụng: solopreneur chạy hệ thống khuyến nghị nên dùng agent tự thiết kế thí nghiệm, cá nhân hóa theo phân khúc người dùng, và tích lũy phương pháp luận thí nghiệm.
- Đặt guardrails (ranh giới an toàn) deterministik cho agent: exposure PV, transaction count, ad PVR, v.v. Áp dụng: khi dùng agent tối ưu hóa, hãy đặt ranh giới an toàn cứng rắn để agent không làm sai số liệu kinh doanh.

## Assumptions & Limitations
- Điều kiện: có hệ thống khuyến nghị và dữ liệu giao dịch thật; không áp dụng nếu không có dữ liệu thực tế.
- Paper thừa nhận: comparison in §6.2 is before/after, not randomized (so sánh trước/sau, không randomized).
- Limitation paper không nói: chưa đánh giá trên nhiều domen ngoài khuyến nghị, chưa test chi phí thực tế của agent.

## Metadata
- Năm: 2026
- Tác giả: PILOT Team
- Category arXiv: cs.AI
- Link PDF: https://arxiv.org/pdf/2608.18637
