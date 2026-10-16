# [2608.24569v2] When "Must" Becomes "Maybe": Erosion of Workflow Constraints in LLM Agent Handoffs

## Problem
Các đại lý ngôn ngữ (LLM agents) xây dựng trên công của nhau thông qua các bản tóm tắt, kế hoạch, và các artefact trung gian. Những bản ghi này cho phép một đại lý phía sau tiếp tục việc mà không cần xem lại toàn bộ ngữ cảnh phía trước. Tuy nhiên, việc này lộ ra một mất mát ẩn giấu: handoffs (việc chuyển giao) có thể mang nhiệm vụ tiếp tục trong khi làm mờ đi các phán đoán (judgments) đã được thiết lập phía trước. Một yêu cầu mà phải được thỏa mãn trước khi hành động (must requirement) trở thành một caveat (điều khoản cảnh báo) mà đại lý sau có thể công nhận và bỏ qua.

## Contribution
- Khám phá vấn đề erosion of workflow constraints (mài mòn ràng buộc quy trình) trong LLM agent handoffs.
- Phát hiện ownership deferral (chuyển nhượng sở hữu) gây ra 76.7% blocker deactivation (vô hiệu hóa chặn)؛ multihop compression (nén nhiều bước) gây ra 97.2%.
- Giám sát mô tả chặn (blocker description) đầy đủ nâng nhận diện (recognition) từ 6.2% lên 99.2% và giảm hành động cấm (forbidden action) từ 85.2% xuống 0.0%.
- Authorization-check prompt (nhắc kiểm tra quyền hạn) giảm forbidden action xuống 1.6%.

## Method (tóm cốt lõi)
Nghiên cứu việc handoff giữa các agent LLM qua các intermediate artifacts (phối phẩm trung gian). Đo blocker deactivation (vô hiệu hóa chặn), forbidden action (hành động cấm), recognition (nhận diện). Thử nghiệm các can thiệp: full blocker description, authorization-check prompt, full insertion, repair, stop label.

## Key Findings
- Ownership deferral: 76.7% blocker deactivation, 60.8% forbidden action.
- Multihop compression: 97.2% blocker deactivation, 31.9% forbidden action.
- Normal handoff: 100.0% deactivation, 54.2% forbidden action.
- Full blocker description: recognition 6.2% → 99.2%, forbidden action 85.2% → 0.0%.
- Authorization-check prompt: forbidden action 85.2% → 1.6%.
- Full insertion: blocker recognition 6.2% → 99.2%, forbidden action 85.2% → 0.0%.
- Schema-preserving compression: 27.8% deactivation, no forbidden actions.
- Light summarization: 25.0% deactivation, forbidden action 0.0%.

## Actionable Insights
- Không nên để đại lý phía sau tự quyết định liệu một yêu cầu "must" có cần thỏa mãn hay không: hãy ghi rõ mô tả chặn (blocker description) đầy đủ trong artifact trung gian. Áp dụng: solopreneur xây pipeline agent nên yêu cầu đại lý phía trước ghi rõ ràng các ràng buộc phải thỏa mãn, không để đại lý phía sau tự bỏ qua.
- Dùng authorization-check prompt (nhắc kiểm tra quyền hạn) để giảm forbidden action từ 85.2% xuống 1.6%. Áp dụng: khi xây pipeline agent, hãy thêm bước kiểm tra quyền hạn trước khi thực hiện hành động quan trọng.
- Dùng full insertion (chèn đầy đủ thông tin chặn) thay vì light summarization (tóm tắt nhẹ) để giữ nguyên ràng buộc. Áp dụng: khi chuyển giao nhiệm vụ giữa các agent, hãy chuyển toàn bộ thông tin chặn, không chỉ tóm tắt.

## Assumptions & Limitations
- Điều kiện: có pipeline agent với nhiều bước handoff; không áp dụng nếu chỉ có một agent đơn lẻ.
- Paper thừa nhận: đánh giá trên các tác vụ cụ thể; có thể khác trên các tác vụ khác.
- Limitation paper không nói: chưa đánh giá trên nhiều domen khác ngoài các tác vụ đã dùng, chưa test chi phí thực tế của các can thiệp.

## Metadata
- Năm: 2026
- Tác giả: Yiheng Sun, Huifei Wang, Yancheng Zhu, Zhenyu Li, Zebin Zhao, Yifan Yuan (Shenzhen University)
- Category arXiv: cs.AI
- Link PDF: https://arxiv.org/pdf/2608.24569
