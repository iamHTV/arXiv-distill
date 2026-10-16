# [2609.22951v1] AgentRouter: Heterogeneous Model Routing for Cost-Optimal Multi-Step Agentic Workflows

## Problem
Hệ thống agent doanh nghiệp route (định tuyến) mọi bước quỹ đạo (trajectory step) đến mô hình frontier (mô hình hàng đầu, tốn kém) gây lãng phí 60–80% ngân sách inference cho những subtask (nhiệm vụ phụ) mà mô hình nhỏ xử lý cũng tốt. Các giải pháp routing hiện tại chỉ tối ưu hóa single-turn (lượt duy nhất) query assignment, bỏ qua đặc tính của agentic workflow (luồng tác vụ đa đại lý): độ phức tạp của subtask thay đổi nhiều trong một quỹ đạo duy nhất.

## Contribution
- Giới thiệu AgentRouter: lightweight classifier (máy phân loại nhẹ) 12M tham số, <5ms overhead (chi phí thêm) mỗi bước trên GPU A100, map (ánh xạ) mỗi bước quỹ đạo đến một trong bốn model tiers (cấp độ mô hình) bằng năm features (đặc trưng) có thể trích xuất tại thời điểm routing.
- Huấn luyện trên 50.000 annotated agent trajectory steps (bước quỹ đạo đa đại lý đã gán nhãn) couvrant planning, coding, research, và data analysis.

## Method (tóm cốt lõi)
AgentRouter định dạng step-level model routing như một vấn đề gán tuần tự (sequential assignment) trên các quỹ đạo agent. Mỗi bước được đánh giá bằng 5 features (đặc trưng) trích xuất được ngay khi routing, rồi classifier 12M tham số chọn model tier phù hợp (tier 1 frontal đến tier 4 minimal). Hệ thống có dependency-aware routing và budget-aware mode (chế độ theo ngân sách), fallback (dự phòng) kích hoạt trên dưới 4% quỹ đạo.

## Key Findings
- AgentRouter đạt 72% giảm chi phí so với frontier-only baseline, giữ 97.3% chất lượng (kém dưới 3% so với hoàn thành tác vụ end-to-end).
- Per-step routing accuracy: 91% trên bước minimal-complexity, 85% trên efficient-tier, 76–82% trên mid-range và frontier tiers.
- 55–70% bước quỹ đạo agent không cần frontier model; chỉ 14.2% bước thực sự cần frontier nhưng tốn 48.3% chi phí còn lại.
- So với FrugalGPT (44% giảm chi phí), RouteLLM (31%), DAAO (36%), AgentRouter vượt trội (72%, 97.3% chất lượng).
- Giảm chi phí theo lĩnh vực: document analysis 76.4%, data analysis 74.1%, research synthesis 69.2%, code generation 63.8%.

## Actionable Insights
- Không route mọi bước đến model lớn: chia nhỏ agentic workflow thành bước, chỉ dùng frontier model cho bước thực sự cần reasoning sâu, dùng model nhỏ cho bước định dạng/trình bày. Áp dụng: solopreneur chạy pipeline agent có thể cắt 70% chi phí inference.
- Dùng classifier nhẹ (12M tham số, <5ms/bước) để route mỗi bước thay vì hardcode quy tắc. Áp dụng: khi xây pipeline AI content, thêm lớp routing nhỏ trước mỗi agent để chọn model tier phù hợp.

## Assumptions & Limitations
- Điều kiện: cần có annotated trajectory data để train classifier; không hoạt động tốt nếu không có dữ liệu quỹ đạo đã gán nhãn.
- Paper thừa nhận: test trên AutoGen (framework chưa thấy) có 6–9% accuracy degradation, cross-framework generalization còn mở.
- Limitation paper không nói: chưa đánh giá trên mô hình nhỏ hơn 7B, chưa test workflow dài hơn nhiều bước.

## Metadata
- Năm: 2026
- Tác giả: Rudrendu Kumar Paul, Sourav Nandy
- Category arXiv: cs.AI
- Link PDF: https://arxiv.org/pdf/2609.22951
