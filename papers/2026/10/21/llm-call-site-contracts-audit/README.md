# 2610.24545 When Code Becomes an LLM Call: Call-Site Contracts trong hệ thống agentic

## Problem
- Phần mềm truyền thống dựa vào specification (đặc tả): pre-condition (điều kiện trước), post-condition (điều kiện sau). Hệ thống agentic thay logic (chọn tool, xét hành động, viết code chạy) bằng LLM call (lời gọi mô hình) — behavior (hành vi) không cố định, thay đổi mỗi run → guarantee (bảo đảm) phải đến từ contract (hợp đồng) quanh mỗi call site (điểm gọi).

## Contribution
- Empirical study (nghiên cứu thực nghiệm) đầu tiên về call-site contract: 496 LLM call site trong 40 hệ thống agentic nguồn mở (13.4 MLOC, 4 ngôn ngữ).
- Pipeline multi-agent (đa tác nhân) validate bởi 17,428 human judgment (phán đoán người): trace (truy vết) mọi model output, derive (suy diễn) expected contract mỗi call site mà KHÔNG đọc code, so với contract code cài.
- 10 gap pattern (mẫu lỗi) giải thích 99% gaps; 38 mechanism (cơ chế) trigger được; 1 code fix nhỏ enforcing constraint dừng cả 38.

## Method
- Stage I: 917 typed output, 1,222 consumption relation (quan hệ tiêu thụ). Stage II: reconstruction contract — 5,017 implemented constraints, 2,699 expected constraints. Stage III: exploitability (khả năng khai thác) + fix validation (xác nhận sửa).
- Assurance level (mức bảo đảm): capability-bound (ràng buộc năng lực) > code-checked > prompt-only.

## Key Findings
- 48% LLM output đến control flow (luồng điều khiển) hoặc execution (thực thi), 40% là free text (văn bản tự do); 73% output decision-relevant (liên quan quyết định) không bao giờ đến người.
- 78% constraints được enforce (bắt buộc) bằng code, nhưng 67% prompt-phase constraints chỉ "yêu cầu" model — 268 syntactic constraints (ràng buộc cú pháp) code quyết định được nằm chỉ trong prompt.
- 82% call site có check trước+sau call, nhưng 63% expected constraints unmet (không thỏa); chỉ 5.3% thỏa mãn toàn contract, median (trung vị) thỏa 1/3.
- Gap rate (tỷ lệ lỗi): post-condition 72%, pre 62%, prompt 47%; 29% constraints enforced yếu hơn yêu cầu.
- 10 patterns: unchecked call inputs (330), partial format check (249), unchecked content (253), underspecified prompt (242), faulty request assembly (168), fail-open handling (146), unvalidated action (138), path-dependent check (101), over-broad authority (90), prompt-only check (43).
- Fail-open handling (xử lý lỗi mở) = 44% conflicting verdicts — Gemini CLI có 5/6 return paths trả ALLOW.
- 17% gaps exploitable (290), 114 trên threat chain (chuỗi tấn công): CVSS 9 critical, 21 high; 38/60 mechanism trigger thực tế (JARVIS chọn tool ngoài candidate pool cả 5 run), code fix nhỏ dừng cả 38.

## Actionable Insights
1. Đừng đếm "có check" — đo "contract thỏa mãn bao nhiêu". Ví dụ: audit (kiểm toán) agent theo 3 phase (pre/prompt/post), liệt kê expected constraints, tính % thỏa mãn — mục tiêu 100%, không phải "có guard".
2. Fail-open giết hàng rào phòng thủ. Ví dụ: mọi exception trong security gate (cổng bảo mật) phải trả DENY hoặc ask-user, không trả ALLOW mặc định.
3. Unvalidated action tập trung ở decision-relevant site (73%). Ví dụ: sau mỗi LLM call chọn tool/action, code phải kiểm tra action ∈ offered set (tập đã đề xuất) trước khi dispatch (gửi chạy).

## Assumptions & Limitations
- 40 hệ thống nguồn mở, 4 ngôn ngữ — code riêng tư có thể khác.
- Expected contract do pipeline derive rồi human-validate — vẫn có chủ quan.
- Stage III loại 83% gaps ở screening (sàng lọc) → exploitable fraction là upper bound (cận trên) của risk.
- Fix validation dừng 38 triggered exploits, không chứng minh dừng mọi attack.

## Metadata
- Năm 2026; tác giả: Shihao Weng, Longtian Wang, Yang Feng, Mingfei Cheng, Jia Liu, Chao Shen (Nanjing University, Xi'an Jiaotong University), He Ye, Federica Sarro (UCL), Xiaofei Xie (SMU); category: cs.SE, cs.AI, cs.CR; PDF: https://arxiv.org/pdf/2610.24545; citation count: [NO DATA — paper mới 2026-10-17]
