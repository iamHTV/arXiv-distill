# 2610.13668 — (When) Should a Software Factory be Lights-off? Benchmarking Code Review Agents on Bug Detection

## Problem
- Review velocity của human không theo kịp agentic code generation → tempt "lights-off software factory" (AI vừa viết vừa review, không có human). Benchmark cũ lấy human comments làm ground truth — poor proxy: comment tùy tiện, nitpicking, bị social dynamics chấp nhận, hoặc quá hẹp bỏ điểm hợp lệ.

## Contribution
- CRBugBench: bug-grounded code review benchmark — 1,800 tasks (1,000 trên 98 GitHub OSS repo + 800 proprietary industry repo tại 1 công ty lớn), 5 ngôn ngữ. Pipeline: (1) bug từ human comment trong PR discussion đã được fix trước merge; (2) bug từ bug-fix PR trace ngược về PR gây bug (escape sau merge).
- Evaluation protocol: agent nhận sandboxed repo tại introducing commit, explore + experiment, viết review.md self-rank theo severity; panel LLM judges match từng finding với ground-truth bug.

## Method
- Đo recall@5 (bugs caught trong top-5 comments) qua nhiều model/harness; logistic regression trên feature repo/PR/bug (RQ2); phân tích trajectory (RQ3); ablation design choice (RQ4: prompt, multi-agent, reasoning effort).

## Key Findings
- Best (claude-opus-5 + copilot-cli) catch 71.9% bugs top-5; từ 47.7% (opus-4.6) → 71.9% (opus-5) trong 5 tháng (Feb→Jul 2026). Opus-5-xhigh: 79.6% bug catch-before-merge, 64.2% catch-after-merge.
- Vẫn miss 20%+ bug human tìm thấy → cần human-in-the-loop. Proprietary repo: drop đến 25.5% — bug cần project context, không infer từ diff.
- RQ2: yếu hơn trên PR lớn/heterogeneous, bug-fixing PR, bug non-functional/ít severe, bug cần non-local reasoning.
- RQ3: agent dành phần lớn turn đọc/search, hiếm execute (opus-5: 9.7% turn; gpt-5.6-sol: 6.9%); half opus-5 runs kết thúc turn 35 vs 17 (gpt-5.6-sol); agent tin misleading PR description, bỏ repository-wide behavior + external library semantics.
- RQ4: exploration-nudging prompt +5.8% (1.10× cost); multi-agent +4.7% (5.55× cost); reasoning effort 36%→57% (23.22× cost). Pareto: gpt-5.6-luna rẻ, opus-4.8/5 mạnh nhất.

## Actionable Insights
- Scale review effort theo PR complexity: PR nhỏ homogeneous → config rẻ; PR lớn heterogeneous → model mạnh + reasoning cao + human review; tách unrelated change thành PR nhỏ.
- Steer agent bằng custom instruction theo priority (usability, portability, backward compatibility, maintainability) — default agent focus vào severe functional bug.
- Feed repository knowledge cho agent khi review proprietary/large repo — bug cần project context là nơi agent yếu nhất (-25.5%).

## Assumptions & Limitations
- Benchmark đo bug-finding (objective), không đo subjective/domain-specific review aspect — human vẫn giữ project values + maintainability.
- Proprietary portion từ 1 công ty; recall@5 có thể overstate nếu chỉ check top comment.
- Không nói: LLM judge panel có thể miss finding diễn đạt khác; model evolution nhanh → số liệu date nhanh.

## Metadata
- 2026, Chenyang Yang (CMU), Hao He, Ti-Chung Cheng, Jenna Butler, Emerson Murphy-Hill, Carmen Badea, Christian Bird (Microsoft/Microsoft Research), cs.SE, https://arxiv.org/pdf/2610.13668
