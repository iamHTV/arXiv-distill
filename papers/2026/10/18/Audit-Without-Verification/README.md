# 2609.07680v1 Audit Without Verification: When LLM Accountability Layers Relay Rather Than Check

## Problem
- Pipeline tác nhân (agent) nhiều bước xuyên tổ chức: khi lỗi bề mặt, phải xác định lỗi vào ở bước nào, dưới quyền kiểm soát của ai. Prior work (failure attribution benchmark — tiêu chuẩn đánh giá quy kết lỗi) đã chứng minh "thấy bao nhiêu execution trace (dấu vết thực thi)" là quan trọng (full trace > output-only), nhưng CHƯA ai tách riêng câu hỏi: report (báo cáo) của agent có nên mang theo conclusion (kết luận) riêng của nó hay không — khi lượng observation (quan sát) giữ nguyên.

## Contribution
- Thiết kế factorial (thực nghiệm đầy đủ nhân tố) 3 nhân tố pre-registered (đăng ký trước): principals k ∈ {1,3,6} × domain {responsibility, documentation} × allocation {individual, collective}, 12 ô, clean twin (bản song sinh không lỗi) ghép cặp, chỉ số phân biệt J — và báo cáo KẾT QUẢ NULL chính thức (giả thuyết đăng ký KHÔNG được hỗ trợ).
- Đặc tả lớp accountability (trách nhiệm giải trình) bất đối xứng: gần như không tự tố cáo (0 allegation / 7,996 episode sạch), nhưng chấp nhận 34.4–62.6% false alarm (báo giả) từ upstream (thượng nguồn) — hoạt động như relay (bộ chuyển tiếp) chứ không phải check (bộ kiểm).
- Thao tác xóa MỘT clause (mệnh đề) "Suspected origin" ở observation không đổi → xác định carrier (vùng mang) nhân quả; phân rã trade-off (đánh đổi) ∆ = P(wrong)·∆|wrong + P(correct)·∆|correct với công cụ đo ngoại tuyến.

## Method
- Supply-chain (chuỗi cung ứng) 6 link, mỗi link = 1 agent chạy riêng MCP server process (process-level information boundary — ranh giới thông tin cấp tiến trình), lỗi tiêm đúng 1 link (cân bằng 96 lần/vị trí trên 480 base case), clean twin ghép cặp. 480 blocks × 12 cells × 2 twins × 5 replications × 6 links = 345,600 request/model chain → 57,600 episode. Chain model: gpt-4.1-mini, claude-haiku-4-5. Auditor: qwen3-30b-a3b-instruct (chính), gemini-2.5-flash-lite (replication), gpt-5 + claude-sonnet-5 (frontier check). Thống kê: GEE binomial/logit, cụm theo block, sandwich hiệu chỉnh Mancl-DeRouen.

## Key Findings
- Giả thuyết pre-registered (collective responsibility framing làm suy giảm escalation theo chain length): NULL — +0.0108 [-0.0305,+0.0522] và -0.0129 [-0.0411,+0.0152], CI (khoảng tin cậy) đều chứa 0.
- Auditor đọc report agent: accuracy (độ chính xác) 26.0% (GPT chain) / 63.2% (Claude chain) vs 63.9% / 63.3% từ raw documentation (tài liệu thô); mutual information (thông tin tương hỗ) 0.065 bits vs 1.073 bits (max ≈2.3 bits). Adherence (mức tuân theo) 95% — auditor đặt origin trong set agent đề xuất.
- Stratum (tầng con) không agent nào đề xuất đúng origin (59.5% episode GPT): auditor phục hồi 4.1% từ report — dưới uniform guess (đoán đều, 20%) và fixed-link accuser (31.0%) — trong khi raw documentation đạt 60.3%.
- Xóa clause "Suspected origin": stratum sai 4.1%→45.2% (+41.2 pp, CI +35.3,+46.9), stratum đúng 70.5%→55.7% (-14.7); adherence 94.4%→3.4%. Replication: auditor thứ 2 (+38.3/+25.9), frontier 4/4 condition (+8.5 đến +39.0 pp), domain 2 (software delivery toolchain) +47.7/+61.1 pp và KHÔNG còn cost.
- Layer chỉ đọc report = relay: 0 allegation trên 7,996 episode sạch-thầm-lặng; tên party vô tội 34.4%/62.6% khi agent false alarm; assertion rate (tỷ lệ khẳng định lỗi) trên clean false-alarm (74.7%) còn cao hơn episode lỗi thật (40.4%).

## Actionable Insights
- Tách field observation khỏi field conclusion trong schema report của agent; tại audit boundary (biên kiểm toán), cho phép tắt conclusion. Ví dụ: checker LLM đọc sub-agent report → strip field "I think the problem is X" trước khi forward, giữ nguyên evidence text.
- Đo reliability (độ tin cậy) của upstream proposal trên validation data trước khi quyết định: ∆ = P(wrong)·∆|wrong + P(correct)·∆|correct — upstream yếu thì suppress (triệt tiêu) conclusion, mạnh thì giữ.
- Không dùng "auditor đồng ý" làm independent verification (xác minh độc lập) khi auditor chỉ đọc report: yêu cầu evidence độc lập với chính kết luận cần kiểm — cùng auditor đạt 60.3% từ raw doc vs 4.1% từ report.

## Assumptions & Limitations
- Điều kiện: information boundary enforced cấp process, defect injection (tiêm lỗi) cân bằng, matched twin.
- Limitation paper thừa nhận: 2 domain synthetic, 2 chain model, 4 auditor; registered GEE spec không hội tụ (dùng independence working correlation); registered interface không implementable (deviation disclosed); evidence-content rubric không được validate (circular self-rating bị loại); single-rater corpus validation; stratification exploratory (định nghĩa bởi hành vi model, không randomize).
- Limitation CHƯA nói: corpus khó không chuyển xuống model yếu hơn (5/7 model trong screen fail); effect phụ thuộc schema cụ thể — chưa test schema khác; prompt assert lỗi làm auditor tệ hơn (38.2% neutral vs 26.0% asserting) — paper coi là artifact disclosed, không khai thác.

## Metadata
- 2026, Paul-Peter Arslan (Institute For Future Technologies), cs.MA, https://arxiv.org/pdf/2609.07680v1, citation count: không tìm thấy [NO BENCHMARK]
