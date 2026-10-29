# Skill: qera-ask-before-answer (hỏi trước khi trả lời cho context learning)
Source: 2610.35083
Type: workflow / prompt-pattern

## Khi nào dùng skill này
- AI assistant (trợ lý AI) phải trả lời trên CONVERSATION (hội thoại) dài, messy (lộn xộn), nhiều lượt (multi-turn): group chat, community thread, activity log, revision history — nơi requirement (yêu cầu) thật sự nằm rải rác ở các lượt trước, KHÔNG có trong request cuối.
- Cần câu trả lời faithful (trung thực) với lời user, có audit trail (dấu vết kiểm toán): verdict (phán quyết) + quote (trích dẫn) cho mỗi requirement.
- KHÔNG nên dùng: question answering trên 1 document ngắn (request gần như là full specification); task cần retrieval vì context vượt context window (cửa sổ ngữ cảnh) của model (skill giữ WHOLE conversation trong mọi call); real-time latency-critical (nhạy độ trễ) không chấp nhận 3-4 LLM call.

## Input cần có
- Conversation x đầy đủ (toàn bộ hội thoại: messages, pasted materials, logs) — vừa context window model.
- Frozen LLM M (mô hình đóng băng — cùng model mọi call, high reasoning effort), ~4 call/task budget (ngân sách) + token budget ~5× direct answering (112k–131k API token/task thực tế với 19.4K-token context).
- Code runtime (môi trường chạy code) cho 3 bộ lọc/verify (không cần LLM): faithfulness filters Φ, measure m + audit E†, guard Γ.
- (KHÔNG cần: rubrics, demonstrations, training, task-specific prompt.)

## Các bước thực hiện
1. **Ask — 1 structured JSON call:** sinh requirement checklist O (mỗi requirement o_k = user's words u_k verbatim + scope s_k (people/items/period/units/criterion) + kind κ_k ∈ {list, count, compare, infer, write} + answer format + required strings + exclusions + layout reply cũ) và typed information needs N (n_j = description d_j bằng lời user + type τ_j ∈ {lookup, enumerate, count, compute, compare, judge} + requirements served R_j + where to start w_j). Requirement list/count-or-compute/timeline/summary/classification tự động thêm enumerate need.
2. **Faithfulness filters Φ (code):** xóa khỏi O, N mọi phần user's words U(x) không support: exclusion quote từ vắng mặt, required string vắng mặt, caution/brevity clause không user turn nào yêu cầu, date window user không đặt, format không yêu cầu, stale template. Thêm coverage needs cho Kset/Tset (enumerate, count, compute). Output: questions Q (7.8 needs/task thực tế).
3. **Answer — 1 call:** draft ỹ = M(x, π, Q) với fixed answer protocol π: (i) đọc mọi phần liên quan gồm corrections lượt sau; (ii) specifics materials cho, không category words; (iii) MỌI qualifying item, không tự threshold; (iv) yes/no/count/ranking mở bằng committed verdict; (v) show inputs mọi total/share/rate; (vi) giữ attributions/format/length/language/exclusions, không disclaimer. Q chỉ advisory — user's words và materials ghi đè Q.
4. **Measure (code):** m = word/sentence/item counts, user limits, missing strings/headings, excluded items, leaked labels trong ỹ.
5. **Check — 1 structured JSON call:** trả lời lại MỌI Q trên ỹ + toàn conversation → E: verdict v_k (pass/partial/fail) + quote a_k của draft cho mỗi requirement; findings F_j (fact + quote <25 words + location; 1/item cho enumerate/count, 1/input cho compute); status σ_j (correct/missing/incomplete/wrong/N/A); latent gaps, unsupported facts, format violations, edit plan ≤12 edits. 3 rules: count sai chỉ khi nêu item missed/added; inference dựa stated evidence không tính là unsupported; không edit nào hedging committed answer.
6. **Audit (code):** finding có quote KHÔNG xuất hiện trong x → flagged, repair cấm dùng; recompute typed needs: lookup → measured lengths/counts + required strings + exclusions; enumerate → 1 finding/item; count → count = #items; compute → inputs sum/average = result; compare → facts mỗi side draft chưa naming; judge → quotes + found values. E† = actionable + audit findings + m gaps. E† = ∅ → trả ỹ (3 calls total).
7. **Repair — 1 call (chỉ khi E† ≠ ∅):** patch chỉ những gì E† flag: áp fix kèm facts+quotes; skip fix materials mâu thuẫn; giữ definite answers definite; propagate changed numbers; preserve rest → ŷ.
8. **Guard Γ (code):** patch phải non-empty, không cut off; trừ khi length fix được yêu cầu: giữ ≥50% draft length và ≥30% numbers; không thêm year ngoài conversation; giữ mọi word limit/count/required string/exclusion draft đã đạt. Đạt → y = ŷ; không đạt → y = ỹ. Code pass cuối restore quotations về source text.

## Output mong đợi
- Final reply y + requirement checklist O + evidence E† (verdict + quotes + recompute numbers) — audit trail cho reviewer.
- Đã verify: solving rate cao nhất 4/4 frontier LLM (21.0% avg vs 18.2% PSCI, 14.6% direct); rubric pass 75.6%; lead trên implicit rubrics (82% classified) +2.5 điểm vs best baseline, tie explicit; Pareto-front cost (ít hơn PSCI 10–26% token, 4–5% token Ctx2Skill); draft 2-call đã beat mọi baseline.
- Số thực tế từ ablation: answer protocol +3.8 rubric points, questions +1.6 (89% gain trước khi answer); check&repair chỉ +0.9 trên numeric rubrics (47% tổng), chiếm 51–56% token → optional khi cost matters.

## Ví dụ áp dụng
- Tóm tắt group chat quyết định: user paste 200-message Zalo group + hỏi "kể lại quyết định về giá". Bước 1 Ask tìm requirement "giá báo theo USD" (rule lượt 3) + enumerate need "mọi pricing decision". Bước 3 draft committed. Bước 5 Check: verdict fail trên requirement "USD" (draft dùng VND) + missing 2 decisions, quotes kèm. Bước 6 Audit: quotes verify trong conversation ✓. Bước 7 Repair: đổi VND→USD, thêm 2 decisions. Bước 8 Guard: patch giữ 60% length, mọi limits → chấp nhận. Output: tóm tắt + checklist + quotes.

## Gotchas
- Questions phải anchored (neo) vào user's words — question user không imply làm answer hedge (mơ hồ)/narrow/reformat; Φ code filter là bắt buộc, không bỏ qua.
- Check stage tiêu tốn 51–56% token mà chỉ refine numeric → khi cost quan trọng, chạy draft-only (Ask+Answer, 2 call) đã beat baseline; bật Check/Repair cho task có numbers/counts.
- Count chỉ sửa khi check NÊU item missed/added; không edit nào hedging committed verdict — nếu không check sẽ làm hại (3 rules của paper).
- Guard reject 27/1,385 repair thực tế (patch rỗng/cụt/bỏ specifics) — luôn giữ fallback về draft, không bao giờ trả patch unchecked.
- Numbers/counts vẫn hardest (QERA pass 71.4% vs 79.2% rubric khác): task numeric-heavy (logs, tracking) cần budget check cẩn thận hơn.
- Whole conversation trong mọi call → context window là giới hạn cứng; context > window phải chunk VÀ chunk sẽ mất carried-forward rules (lúc đó skill không còn đúng thiết kế).
- Mọi stage gửi conversation tới LLM provider → kế thừa data-retention terms; personal/sensitive traces cần local hosting (tự lưu trữ) + consent (đồng thuận) handling.
