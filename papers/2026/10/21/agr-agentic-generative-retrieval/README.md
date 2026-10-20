# 2610.26831 AGR: Agentic Generative Retrieval with Tool-Augmented Search

## Problem
- Generative retrieval (GR — truy xuất sinh) biểu diễn item bằng hierarchical Semantic ID (SID — định danh ngữ nghĩa phân cấp), nhưng hệ thống search/recommendation quy mô lớn sống nhờ feature (đặc trưng) phong phú: user profile, behavioral history, freshness cue (tín hiệu mới). Cách hiện tại hoặc nhồi mọi signal vào input (tăng serving cost (chi phí phục vụ), nhiễu) hoặc inject theo scheme (lược đồ) cố định — không adaptively quyết định khi nào cần feature, feature nào, ảnh hưởng vào đâu trong quá trình sinh SID.

## Contribution
- AGR: paradigm (mô hình) tool-augmented (tăng cường bằng tool) đan xen SID generation với on-demand feature acquisition (thu nhận feature theo nhu cầu).
- Conditioned on request + decoded SID prefix, AGR quyết định: có invoke tool (gọi công cụ) không, acquire feature nào, observation (quan sát) ảnh hưởng decoding ở đâu → steering (dẫn dắt) generation về branch (nhánh) SID feature-consistent.
- Supervision (giám sát): tool-augmented trajectory (quỹ đạo) xây từ feature applicability (tính áp dụng) + information gain (lợi ích thông tin) dọc theo SID hierarchy.

## Method
- Mở rộng vocabulary V = S ∪ T ∪ O (SID tokens + tool tokens + observation tokens): mỗi tool token t kích hoạt function call f_t(q, u, s≤i), kết quả là observation token o_t — thống nhất SID generation và tool invocation trong 1 autoregressive process (quá trình tự hồi quy).
- Inference (suy luận): tương tác model–tool cho từng beam candidate (ứng viên chùm tia) trong decoding.
- Training: SID pretraining (tiền huấn luyện) rồi tool-augmented fine-tuning (tinh chỉnh tăng cường tool).
- Tools: CF (categorical features — đặc trưng phân loại), GSU (General Search Unit — chuỗi hành vi user), QU (query text + user features).

## Key Findings
- 4 datasets (1 industrial + 3 public benchmarks — tiêu chuẩn đánh giá): AGR best Recall và MRR mọi cutoff; cải thiện tương đối so TIGER: Recall +6.4% đến +14.0%, MRR +5.2% đến +19.7%.
- So direct encoding 400 GSU tokens: Recall@50 0.3237 vs 0.3241 (ngang nhau) nhưng training time 1.969 vs 10.794 sec/step (−81.8%), serving cost 4.76 vs 8.33 GPUs/1K requests (−42.9%).
- Online A/B test tại Kuaishou production search (latency (độ trễ) trung bình 35ms, 7-day A/A + 7-day A/B, 10% traffic mỗi nhánh): Relevance (top-4 results strongly relevant) +0.205% [+0.12%, +0.28%]; Query reformulation rate (tỷ lệ viết lại truy vấn) −0.690% [−1.13%, −0.20%]; Search penetration rate +0.060% [+0.03%, +0.14%].

## Actionable Insights
1. Đừng nhồi mọi feature vào prompt/input — để agent fetch theo nhu cầu. Ví dụ: agent gợi ý sản phẩm chỉ query history tool khi SID prefix cho thấy cần behavioral signal, thay vì gửi toàn bộ profile mỗi lần → chất lượng ngang, cost giảm ~43–82%.
2. Dạy model "khi nào gọi tool" bằng trajectory có information gain, không phải quy tắc mù. Ví dụ: log mỗi lần fetch feature kèm delta chất lượng (ΔPPL) để tạo dữ liệu giám sát.
3. Chạy A/A test 7 ngày trước A/B test để xác nhận traffic split (chia traffic) không bias (thiên kiến). Ví dụ: chỉ tin chênh lệch có 95% CI (khoảng tin cậy) không chứa 0.

## Assumptions & Limitations
- Trajectory training dùng predefined rules (quy tắc định trước), không phải learned policy (chính sách học) → future work: agentic reinforcement learning (học tăng cường tác nhân) với sparse rewards (phần thưởng thưa).
- Tool ecosystem hiện hạn chế; cần mở rộng thêm tool và retrieval domain.
- Trajectory xây dọc golden SID prefix (prefix chuẩn) bằng target-side agreement → exposure bias (thiên kiến phơi nhiễm).
- AGR vẫn tốn ~2× serving cost so no-feature baseline — cần budget (ngân sách) GPU.

## Metadata
- Năm 2026; tác giả: Ming Yang (Fudan University), Yaqi Yin, Zhibo Wang, Xiaoze Jiang, Jingwei Zhuo, Chao Zhang, Quanzhi Zhu, Weiguo Zheng, Liang Zeng, Yunfeng Zhao, Jiaqiang Liu, Kefeng Wang, Yupeng Huang, Kaiqiao Zhan, Xuanping Li (Kuaishou Technology); category: cs.IR; PDF: https://arxiv.org/pdf/2610.26831; citation count: [NO DATA — paper mới 2026-10-19]
