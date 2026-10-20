# 2610.24383 IF-MAP: Influence-Function-Inspired Agent Prioritization in Multi-Agent Systems

## Problem
- Cải thiện mọi agent trong multi-agent system (hệ thống đa tác nhân) quá tốn kém → cần biết ưu tiên agent nào để gain (lợi nhuận) system-level lớn nhất với resource (nguồn lực) hạn chế.
- Failure attribution (gán lỗi thất bại) cho biết agent nào chịu trách nhiệm thất bại, nhưng responsibility (trách nhiệm) KHÔNG trực tiếp tiết lộ system-level gain khả thi nếu cải thiện agent đó.

## Contribution
- IF-MAP: method (phương pháp) lấy cảm hứng từ influence function (hàm ảnh hưởng) để nhận diện agent có potential (tiềm năng) cải thiện hệ thống cao nhất.
- Với mỗi agent: đo end-to-end loss change (biến đổi loss đầu-cuối) dưới controlled semantic prompt perturbations (nhiễu loạn prompt ngữ nghĩa có kiểm soát); fit regularized local response model (mô hình phản hồi địa phương chính quy) trong low-dimensional prompt-embedding subspace (không gian con nhúng prompt số chiều thấp); response norm (chuẩn phản hồi) = priority score (điểm ưu tiên).
- Black-box (hộp đen): không cần model parameters (tham số mô hình) hay gradients (gradient).

## Method
- Mỗi agent: tối đa 10 formal perturbations (nhiễu loạn hình thức) — static, adaptive, structure-preserving (giữ cấu trúc) — giữ role (vai trò) và output interface (giao diện output); structural checks (kiểm tra cấu trúc) loại prompt không dùng được/trùng.
- Mỗi probe chỉ đổi prompt agent i, chạy full system → đo response bao gồm thay đổi truyền qua agent interaction (tương tác).
- Signed effect (hiệu ứng có dấu) Δ = L0 − L(m) (dương = cải thiện). Embedding model cố định E: displacement v = E(p(m)) − E(p); direction u = v/||v||; y = (L(m) − L0)/||v|| (loss change mỗi đơn vị khoảng cách embedding).
- Priority = norm của local response ước lượng trong subspace.

## Key Findings
- 6 workflows AFlow-derived: HumanEval, MBPP (code), NQ (QA factoid), HotpotQA (multi-hop QA), DROP (discrete reasoning), MATH. Execution model Qwen3-8B; prompt operations DeepSeek-V3.2.
- Prompt optimization trên selected agents: macro-average gain +3.81 percentage points vs +1.85 uniform selection.
- Model upgrades (5 targets: Qwen3-32B, Qwen3-235B-A22B Instruct-2507, Qwen3.7-Plus, DeepSeek-V3.2, GPT-5 nano): macro-average gain +7.62 đến +16.42 pp vs +3.81 đến +8.62 uniform. Panel Qwen3-32B/235B/3.7-Plus: IF-MAP +12.52 pp (Kendall τ 0.775) vs baseline tốt nhất Who&When-AAO/A2P +10.32, uniform +6.57.
- Token use: Qwen3-8B −74.2%, DeepSeek-V3.2 −35.2% so optimizing every agent; target-model tokens −63.6–64.9% so upgrading every agent.

## Actionable Insights
1. Đo "potential to improve", không chỉ "ai gây lỗi". Ví dụ: pipeline 4 agent (triage, research, draft, verify) — thay vì sửa agent lỗi nhất, probe từng agent bằng 10 biến thể prompt, nâng cấp agent có response norm cao nhất → gain hệ thống gấp ~2 lần chọn ngẫu nhiên.
2. Black-box probing hoạt động không cần trọng số model. Ví dụ: dùng API-only agents vẫn áp dụng được — chỉ cần chạy hệ thống với prompt perturbation và đo metric đầu-cuối.
3. Tập trung budget upgrade: upgrade 1 agent chọn lọc thay vì tất cả. Ví dụ: thay GPT-5 nano cho đúng 1 agent → +7.62–16.42 pp macro mà tiết kiệm 63.6–64.9% target-model tokens.

## Assumptions & Limitations
- Gain thực tế phụ thuộc embedding model, local linearity (tuyến tính địa phương), probe coverage (phủ sóng probe), alignment giữa intervention khả dụng và hướng giảm loss đã fit.
- Probe overhead (chi phí dò): mỗi agent ≤10 probe × full-system runs — vẫn rẻ hơn tối ưu mọi agent nhưng không miễn phí.
- Response direction liên tục → cần translate thành discrete improvement (future work: direction-conditioned generation, iterative edit-and-measure).
- 6 workflows AFlow-derived — kết quả trên workflow tự thiết kế có thể khác.

## Metadata
- Năm 2026; tác giả: Jie Mao, Pingchen Lu, Zikun Qu, Jiahang Sun, Xiangyi Wang, Zhiwei Shang, Zhongxiang Dai (The Chinese University of Hong Kong, Shenzhen), Zhiyong Wang (Harbin Institute of Technology), Guojun Xiong (Harvard University); code: https://github.com/s1412/IF-MAS; category: cs.AI, cs.MA; PDF: https://arxiv.org/pdf/2610.24383; citation count: [NO DATA — paper mới 2026-10-17]
