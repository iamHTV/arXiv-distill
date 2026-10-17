# Skill: Audit-Boundary Report Schema (tách observation khỏi conclusion trong report của agent)
Source: 2609.07680v1
Type: workflow

## Khi nào dùng skill này
- Xây dựng lớp accountability/audit (kiểm toán) cho pipeline multi-agent (nhiều tác nhân) mà auditor chỉ nhận được report (báo cáo) của agent, không có full execution trace (dấu vết thực thi đầy đủ).
- Pipeline xuyên tổ chức (multi-vendor): mỗi bước do một bên khác nhau kiểm soát, cần quy kết lỗi về đúng bước.
- KHÔNG nên dùng: auditor đã có quyền truy cập raw log/trace đầy đủ (full-trace attributor đã thắng output-only rồi); hoặc pipeline 1 bước đơn lẻ không có upstream (thượng nguồn).

## Input cần có
- Schema report hiện tại của agent (các field: escalation flag, anomaly type, suspected origin, free-text evidence).
- Validation data (dữ liệu kiểm định) đại diện: tập episode có ground truth về bước lỗi, đủ lớn (paper dùng 480 base case × replications).
- Một auditor model khác model của chain agent (tránh same-model coupling).

## Các bước thực hiện
1. **Inventory (kiểm kê) schema:** đánh dấu mỗi field là observation (quan sát) hay conclusion (kết luận). Field mang kết luận ("Suspected origin: step N") chính là carrier (vùng mang) phụ thuộc — target của skill.
2. **Đo upstream reliability (độ tin cậy thượng nguồn) ngoại tuyến:** trên validation data, tính P(agent đề xuất đúng origin) — tần suất tập đề xuất của agent chứa true origin. Paper đo: 40.5% (GPT chain) và 65.3% (Claude chain) episode có origin đúng được đề xuất.
3. **Đo hai điều kiện (conditional magnitudes):** chạy auditor trên 2 phiên bản report — đủ field và xóa clause conclusion — tách theo stratum (tầng con): suggestion wrong vs suggestion correct. Tính ∆|wrong và ∆|correct (paper: +41.2 pp và -14.7 pp trên GPT chain).
4. **Tính dấu của trade-off (đánh đổi):** ∆ = P(wrong)·∆|wrong + P(correct)·∆|correct. Nếu upstream yếu (P(wrong) cao) → xóa conclusion là lời; nếu upstream mạnh → giữ.
5. **Thiết kế schema 2 vùng:** field observation và field conclusion tách biệt; conclusion có thể suppress (triệt tiêu) tại audit boundary — available cho consumer cần, withholdable khỏi component cần độc lập.
6. **Verify independence (xác minh tính độc lập) của auditor:** đo mutual information (thông tin tương hỗ) giữa output auditor và thông tin khả dụng (paper: 0.065 bits vs 1.073 bits — gần 0 nghĩa là relay); chạy clean-episode origination test (0 allegation trên episode sạch mới đạt); so với fixed-link accuser baseline (đường cơ sở buộc tội link cố định) và uniform guess.

## Output mong đợi
- Quyết định carry/suppress per-field cho schema report, kèm estimate ∆ kỳ vọng.
- Báo cáo mutual information của auditor + tỷ lệ origination trên episode sạch — chứng minh auditor là check chứ không phải relay.

## Ví dụ áp dụng
- Pipeline content 3 agent (writer → editor → publisher): editor report có field "Suspected origin: writer". Đo trên 200 validation case: writer đề xuất đúng 45% → P(wrong)=0.55. Auditor đọc full report đạt 30% accuracy trên stratum wrong, 70% trên stratum correct; xóa clause: 65% (+35) và 58% (-12). ∆ = 0.55×35 + 0.45×(-12) = +13.85 pp → bật chế độ suppress conclusion cho auditor, tách field trong schema.

## Gotchas
- Abstention confound (nhiễu từ chối trả lời): kiểm tra tỷ lệ abstention ở 2 điều kiện — nếu xóa clause làm auditor abstention nhiều hơn, accuracy tăng có thể là artifact. Paper: abstention giảm 34.8%→26.2%, nên không phải confound.
- Free-text leakage (rò rỉ qua text tự do): report free-text vẫn có thể tên đúng origin — loại các episode có leak rồi tính lại (paper: gain vẫn +41.2 GPT, +20.1 Claude).
- Prompt asserting (prompt khẳng định có lỗi): đừng viết trong auditor prompt "a defect was introduced" — làm auditor tệ hơn (38.2% neutral vs 26.0% asserting); dùng neutral prompt stating defect may or may not exist.
- Stratification (phân tầng) theo hành vi model làm skew vị trí thật (link 1 bị over-accuse) → dùng within-stratum comparator, đừng mang baseline 20% thiết kế sang stratum.
- Re-collect interleaved (thu thập xen kẽ) 2 điều kiện trong 1 execution để loại trừ run-date drift (model/API thay đổi giữa 2 lần chạy).
