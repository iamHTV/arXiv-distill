# [2610.35082] CoSA: The Conflict of Skills Attack in Real-World LLM Agent Ecosystems

## Problem
- Kiểm tra bảo mật Agent Skill (gói khả năng tái sử dụng cho agent) hiện nay xét từng package riêng lẻ: scan tĩnh/ngữ nghĩa, kiểm soát runtime theo manifest. Prior work chưa giải quyết được risk khi ghép Skill vì unit phân tích là package đơn lẻ — trong khi output của Skill này bị Skill khác tái sử dụng mà không mang theo restriction (điều kiện giới hạn) và authorization (sự cho phép) của mục đích gốc. Ví dụ motivating case: 3 Skill riêng benign (đọc trạng thái CI, chuẩn bị vật liệu reproduce, chạy workflow validation) ghép lại → agent thực thi code từ package đã submit mà không được phép.

## Contribution
- Định nghĩa Conflict of Skills (CoS — xung đột kỹ năng): vi phạm policy (quy tắc hành vi) từ reuse artifact (sản phẩm trung gian) hoặc decision (quyết định) giữa các Skill đều pass kiểm tra riêng, qua 4 cơ chế: security-context attenuation (suy giảm ngữ cảnh bảo mật), semantic interface bridging (cầu nối giao diện ngữ nghĩa), semantic authority promotion (thăng quyền ngữ nghĩa), target/action binding drift (trôi dạt liên kết đích–hành động).
- CoSA: khung tấn công thêm Skill locally-admitted (pass scanner đơn lẻ) tối đa 5% pool, bằng capability supplementation (bổ sung năng lực) hoặc relationship reshaping (tái cấu trúc quan hệ) — không sửa Skill cũ, không đổi permission.
- CoSA-Bench: 288 business task, 4 domain (recruiting, finance, IT, business), 3 risk category: data leakage (rò rỉ dữ liệu), unauthorized state modification (đổi trạng thái không được phép), unsafe execution (thực thi không an toàn).
- CoSA-Guard: pre-action hook (móc trước hành động) kiểm information flow (luồng thông tin) + authorization.

## Method (tóm tắt cốt lõi)
- Task τ=(u, e0, Γ); mỗi thao tác Skill gán 1 trong 6 vai trò: READ, TRANSFORM, ASSESS, EXTERNALIZE, MUTATE, EXECUTE.
- Artifact dependency (phụ thuộc sản phẩm) Arth và decision dependency (phụ thuộc quyết định) Dech yêu cầu bằng chứng reuse trong trajectory (dấu vết thực thi) — thứ tự thời gian đơn thuần không đủ.
- Witness CoS (công thức 1): ∃ constraint c, chuỗi w: c(Ω)=0, Depc(w,h)=1, |S(w)|≥2, mọi Skill trong w pass Π. Risk increment (mức tăng rủi ro) ∆D = E[R(V_D∪I_D) − R(V_D)] (công thức 2).
- Pipeline: discovery (phân tích operation-level contract) → LLM đề xuất candidate theo 4 cơ chế → lọc consistency với contract + local admission Π → chọn budgeted maximum coverage (phủ tối đa có ngân sách) tất định → paired run V_D vs V_D∪I_D với autonomous Skill selection (tự chọn kỹ năng); LLM judge chỉ đếm vi phạm khi có hiệu ứng cụ thể.

## Key Findings
- Vi phạm policy: 35.02% (1513/4320) → 58.45% (2525/4320), +23.43 percentage point (điểm phần trăm, pp) chỉ với ≤5% Skill thêm.
- OpenClaw 31.94→54.24 (+22.29pp), OpenHands 40.07→66.11 (+26.04pp), OpenCode 33.06→55.00 (+21.94pp); tăng ở 159/180 nhóm model–harness–domain–risk.
- 5 model: Qwen3.6, MiniMax-M3, DeepSeek-V4, GPT-5.6, GLM-5.1; 3 harness: OpenClaw, OpenHands, OpenCode. GPT-5.6 robust nhất (+8.33pp) nhưng vẫn 29.86–34.03% vi phạm sau augment (bổ sung).
- Data leakage tăng nhiều nhất mọi harness: +25.00/+31.04/+25.21pp; UA +18.13–25.83pp, UE +20.00–23.75pp.
- Retrieval proxy yếu: ITR (injected-Skill trigger rate — tỷ lệ kích hoạt Skill thêm) tương quan yếu với ∆ASR (r=0.058); GPT-5.6 và MiniMax-M3 ITR gần giống (83.45% vs 83.33%) nhưng ∆ASR cách xa (10.88 vs 29.51pp).
- Ablation OpenClaw: random benign injection 26.39% (−5.55pp), random candidate selection 43.40% (+11.46pp), full CoSA 54.24% — cao hơn random ~10.8pp cùng budget.
- CoSA-Guard (OpenClaw recruiting, 5 model): ASR (attack success rate — tỷ lệ thành công tấn công) 65.28% (235/360) → 6.67% (24/360), −58.61pp; Risk Coverage (phủ rủi ro) 82.73% (115/139); PCTC (Policy Compliant Task Completion — hoàn thành task tuân thủ policy) 66.67%→65.00%; FBR (False Block Rate — tỷ lệ chặn sai) 3.33%.
- Scanner Cisco AI Defense: severe-alert count không đổi sau augmentation — alert tĩnh không phân biệt realized risk (rủi ro thực tế hóa).

## Actionable Insights
1. Audit composition, không audit từng Skill: trước khi thêm Skill/plugin mới vào agent, chạy paired test cùng 10–20 task với và không có Skill mới, đếm side effect (hiệu ứng phụ) vi phạm policy. Ví dụ: thêm skill "soạn invoice" vào agent CSKH → chạy 20 ticket giống nhau ở 2 cấu hình, so sánh số lần ghi DB/gửi email ngoài phép.
2. Cài pre-action gate: trước mọi hành động write/send/execute, hook kiểm provenance (nguồn gốc dữ liệu) của payload và authorization gắn với action+target cụ thể. Ví dụ: trong workflow automation, node "gửi email khách hàng" phải xác minh content mang approval flag (cờ phê duyệt) từ hệ thống ticket.
3. Đo risk change trực tiếp: đừng dùng retrieval rate (tần suất Skill được gọi) làm thước an toàn. Ví dụ: báo cáo an toàn plugin nên ghi chênh lệch vi phạm giữa 2 cấu hình, không ghi tần suất kích hoạt.

## Assumptions & Limitations
- Điều kiện: Skill thêm pass scanner đơn lẻ, budget ≤5% pool, domain relevance (liên quan lĩnh vực), sandbox với controlled services (dịch vụ kiểm soát).
- Paper thừa nhận: giới hạn domain/model/harness/risk category; budget bound; model/tool/permission cố định; chưa cover long-horizon dependency (phụ thuộc tầm xa).
- Mày thấy thêm: mỗi task chạy 1 lần/điều kiện → không có ước lượng variance (phương sai); random baseline chỉ 1 realization; không ablation riêng capability supplementation vs relationship reshaping; Guard dùng GPT-5 phán đoán bằng chứng mơ hồ → phụ thuộc LLM thứ hai; chỉ test hệ sinh thái ClawHub.

## Metadata
- Năm: 2026 (26/10/2026). Tác giả: Yujia Zheng (USTB/ZODA), Tianhao Li (OWASP), Shangzhi Xu, Yuekai Huang, Ziyou Jiang, Zhaoyang Li, Yuyao Ge, Junran Peng, Mingyang Li (ISCAS). Category: cs.CL, cs.AI, cs.CR. Link: https://arxiv.org/abs/2610.35082. Citation count: [NOT FOUND — paper 2 ngày tuổi].
