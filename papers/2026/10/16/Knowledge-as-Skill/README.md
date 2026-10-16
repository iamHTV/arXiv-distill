# [2609.25991v1] Knowledge-as-Skill: A Structural Design for Autonomous Knowledge-Base Use by LLM Agents

## Problem
RAG (Retrieval-Augmented Generation - sinh tăng cường truy xuất) là phương pháp dominante để cho LLM truy cập kiến thức bên ngoài. Tuy nhiên, pipeline truyền thống "retrieve-concatenate-generate" (trích xuất-noi liên kết-tạo sinh) đưa ra quyết định truy xuất thay mặt mô hình: evidence (bằng chứng) được truy xuất vàInject (tiêm) cho dù câu hỏi có cần hay không. Khi tool use và agent loops (vòng lặp agent) trở nên đáng tin cậy, quyết định về việc truy xuất, kiểm tra gì, và khi nào dừng có thể được ủy thác cho model. Điều này lộ ra bottleneck mới: agent không biết kiến thức nào có trong kho.

## Contribution
- Đề xuất tổ chức knowledge base theo 3 lớp (SKILL.md, index.md, frontmatter YAML) để LLM agent tự quyết định truy vấn-gì-khi-nào.
- Kèm pipeline chuyển PDF/Word/web thành cấu trúc này.
- Beating RAG trên WixQA: Factuality 0.889, Context Recall 0.816, Hallucination Rate 4.5%, 4.015 average interaction turns.

## Method (tóm cốt lõi)
Knowledge-as-Skill tổ chức kiến thức thành 3 lớp: SKILL.md (mô tả kỹ năng/kiến thức), index.md (chỉ mục), frontmatter YAML (siêu dữ liệu). Agent tự quyết định khi nào truy vấn, kiểm tra đoạn nào, và khi nào dừng, thay vì RAG tự tiêm evidence. Pipeline chuyển đổi tài liệu PDF/Word/web thành cấu trúc 3 lớp này.

## Key Findings
- Knowledge-as-Skill đạt 0.889 Factuality (độ chính xác sự thật), 0.816 Context Recall (gọi lại ngữ cảnh), 4.5% Hallucination Rate (tỷ lệ ảo thuật), 4.015 turns (lượt tương tác trung bình) trên WixQA.
- Beating RAG trên WixQA (benchmark WixQA).
- Đánh giá còn preliminary (đầu tiên/ban đầu).

## Actionable Insights
- Không nên để RAG tự tiêm toàn bộ evidence vào context: hãy để agent tự quyết định khi nào truy xuất và kiểm tra đoạn nào. Áp dụng: solopreneur xây hệ thống knowledge base cho agent nên tổ chức kiến thức theo cấu trúc 3 lớp (SKILL.md, index.md, YAML) và để agent chủ động truy vấn.
- Dùng cấu trúc knowledge base dạng skill (kỹ năng) thay vì chỉ là tài liệu thô: agent biết "kỹ năng này làm gì, khi nào dùng". Áp dụng: khi xây content-KB cho agent, mỗi mục kiến thức nên có SKILL.md mô tả mục đích và điều kiện sử dụng.

## Assumptions & Limitations
- Điều kiện: agent cần có khả năng quyết định truy vấn tự chủ; không áp dụng nếu agent chỉ được tiêm context bằng RAG đơn thuần.
- Paper thừa nhận: đánh giá còn preliminary (chưa đầy đủ).
- Limitation paper không nói: chưa đánh giá trên nhiều domain khác ngoài WixQA, chưa test chi phí token thực tế so với RAG.

## Metadata
- Năm: 2026
- Tác giả: Jiangxu Wu (Sun Yat-sen University)
- Category arXiv: cs.AI
- Link PDF: https://arxiv.org/pdf/2609.25991
