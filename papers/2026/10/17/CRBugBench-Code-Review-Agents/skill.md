# Skill: Bug-grounded Review Agent Evaluation (CRBugBench method)
Source: 2610.13668
Type: evaluation-method (benchmark construction + evaluation cho code review agent)

## Khi nào dùng skill này
- Đánh giá code review agent có thật sự catch bug không (thay vì so lexical với human comment)
- Build custom benchmark cho repo riêng (OSS hoặc proprietary) để đo review quality theo model evolution
- KHÔNG nên dùng: đánh giá style/subjective review aspect (conciseness, tone) — method này chỉ đo bug-finding

## Input cần có
- Repo history: PR discussion threads + bug-fix PRs (để mine ground-truth bugs)
- Sandbox environment cho agent (repo tại introducing commit, restricted internet)
- Panel LLM judges + rubric match finding ↔ ground-truth bug

## Các bước thực hiện
1. Mine bugs từ history theo 2 nguồn: (a) human review thread có bug-related comment và được address trước merge (catch-before-merge); (b) bug-fix PR trace ngược về introducing PR (catch-after-merge / escaped).
2. Tạo review task: gán agent sandboxed repo tại introducing commit + diff; agent explore/experiment rồi viết review.md, self-rank findings theo severity.
3. Panel LLM judges so sánh từng finding trong review.md với ground-truth bug, label match/không; tính recall@5.
4. Segment analysis: tách OSS vs proprietary, PR size/heterogeneity, bug severity/type, local vs non-local reasoning — dùng logistic regression để biết agent yếu ở đâu.
5. Tuning harness theo thứ tự cost-effectiveness: exploration-nudging prompt trước (+5.8% @ 1.10× cost), rồi mới multi-agent (+4.7% @ 5.55×) hoặc reasoning effort cao (36%→57% @ 23.22×).
6. Dispatch model theo PR characteristic: PR nhỏ homogeneous → model rẻ (gpt-5.6-luna class); PR lớn heterogeneous → opus-class + human review.

## Output mong đợi
- Recall@5 trên task set riêng; biết agent catch được bao nhiêu % bug human-verified; roadmap dispatch model + harness tuning theo cost-performance Pareto.

## Ví dụ áp dụng
- Team muốn dùng review agent cho monorepo: mine 200 bug từ 6 tháng history, chạy agent, đo recall@5 = 65%; thấy drop 20% trên PR >500 dòng → rule: PR lớn luôn có human review.

## Gotchas
- Human comments KHÔNG phải ground truth tốt (nitpicking, social dynamics) — dùng bug verified by fix, không phải comment.
- Agent hiếm execute code (9.7% turn) — bug cần runtime evidence dễ miss; supply repo knowledge base cho proprietary repo.
- Agent tin misleading PR description — don't let description anchor the review; kiểm tra code thực.
- recall@5 overstate nếu production chỉ check top comment — calibrate với top-1/top-3.
- Harness helper model này có thể vô dụng cho model sau (model evolution nhanh) — re-evaluate định kỳ.
