# 2609.11957v1 Look Before You Leap: Pre-Action Verification for LLM Agents

## Problem
- LLM agent hành động bằng shell command và code edit. Sai action không phải lúc nào cũng báo lỗi to: nó có thể fail silently (thất bại thầm lặng) — action tưởng thành công, không có signal, lỗi lan vào các bước sau và invalid mọi thứ phía sau. Model không tự catch được lỗi của mình bằng introspection; post-hoc repair (sửa sau) chỉ trigger khi error được quan sát — mà silent failure theo định nghĩa là không bao giờ được quan sát. Prior work (agent benchmark, tool-use, self-repair) đo end-to-end success nhưng không isolate tại sao action fail, và chỉ sửa SAU khi lỗi lộ.

## Contribution
- Khung pre-action verification chung: fix đúng effect của action by construction trước khi executor chạy → silent failure trở thành đại lượng đo được, với taxonomy success / clean failure (refused, recoverable) / silent failure (applied sai chỗ, không signal) + abstention operating points.
- Shell benchmark: 9,930 commands trên 482 real tools, construction anti-circular (invalid commands do behavioral oracle độc lập xác nhận: which, bash -n, flag set từ --help/-h/man) — verifier không bị chấm bằng chính giả định của nó.
- Edit benchmark: 640 edits trên 224 real Python files, isolate apply step (target file tổng hợp trước, render sang format rồi perturb vị trí) — 23,040 trials, exposing content-anchored vs location-anchored safety dichotomy.
- 2 guards deploy được: selective grounding (two-tier gate) cho commands và Robust-Apply (anchor-and-verify meta-applier) cho edits.

## Method
- Shell verifier: 3 checks — syntax (bash -n), binary existence (which), flag validity (membership in flag set extract từ --help/-h/man); subcommand-aware (git commit flags tách khỏi git flags); abstain khi tool không extract được flags (coverage 91.1%).
- Edit formats: content-anchored (search/replace exact, whitespace-normalized, fuzzy τ; unified diff qua real GNU patch fuzz 0/2) vs location-anchored (line range, whole-function-by-name); perturbations: reindentation + line shift.
- Robust-Apply (Algorithm 1): min anchor size Kmin → exact rồi whitespace-normalized match, unique match thì apply; nếu không, top-2 fuzzy matches, chấp nhận khi s1 ≥ τhi và s1 − s2 ≥ δ, commit qua patch;否则 refuse với clean-fail signal. Params (Kmin, τhi, δ) = (2, 0.90, 0.20).
- Operating point: sweep θ → frontier (applicability, safety); deployed guard maximize applicability subject to safety floor.

## Key Findings
- Shell: full config phát hiện 95.8% invalid commands ở 10.0% FPR (precision 0.975, F1 0.966); tool-clustered bootstrap 95% CI recall [0.944, 0.971], FPR [0.078, 0.122]; warm median 2.55 ms/command (p95 2.78 ms), one-time cold extract p95 2.85 s rồi cache.
- Decomposition: syntax+binary là oracle-exact — 0 false positive, recall 0.500 (catch nonexistent-binary và malformed-syntax hoàn hảo, recall 1.000 mỗi loại); flag check supplies phần còn lại và là nguồn của TẤT CẢ 198 false positives (đều là flag thật mà parser missed: 48.5% single-dash 1-char, 29.8% single-dash multi-char, 21.7% double-dash; 95/482 tools, ≤8 tool mỗi loại); invalid long/short flag recall 0.916 (bị giới hạn bởi 91.1% extraction coverage, không phải method).
- Selective grounding: abstain đúng class single-dash multi-char (lossless by construction — không có invalid nào thuộc class đó) → cùng recall 0.958 ở 7.0% FPR, Pareto-dominate naive. Deploy gate: oracle-exact block (recall 0.500 @ 0% FP) + flag suspicion thành non-blocking warning (7.0% warn-rate).
- Edit dichotomy: content-anchored KHÔNG BAO GIỜ silent (0.000) nhưng trade applicability (SR-exact stress success 0.571, SR-fuzzy 0.977, CI [0.972, 0.981]); location-anchored fail silently: line range dưới 1-line shift corrupt 99.1% files mà apply đúng 0%, whole-function hit nhầm function cùng tên 12.7% ngay cả khi không perturbation (duplicate-name collision).
- Policy cũng quyết định: permissive first-match nâng silent của content-anchored từ 0.000 lên 0.020 (exact) / 0.023 (wsnorm) — format vẫn áp đảo (2% vs 99%). Multi-hunk: fuzzy silent compound lên 39.3% và KHÔNG abstain bao giờ; unified diff vẫn 0.000. Replication trên 55 edits từ requests library: SR-fuzzy silent 0.025, line range 1.000 — effect nội tại ở format.
- Robust-Apply: 1 silent misapplication trong 8,320 trials (0.01%) qua mọi format/perturbation/multi-hunk/third-party, vs native rate tới 99.1%; chuyển 100% silent misapplication của aggressive fuzzy thành recoverable clean failure mà giữ 60% applies; applicability 0.51 vs 0.98 trên perturbed single-hunk; stable silent ≤ 0.05% trên τhi ∈ [0.85, 0.95], δ ∈ [0.10, 0.30]. 1 case silent duy nhất: GNU patch commit hunk ở shifted location tại fuzz khác 0 (rate 0.0005) — constrain fuzz factor là bỏ.

## Actionable Insights
- Format action quyết định khả năng catch lỗi, không phải model: biểu diễn edit dạng content-anchored (search/replace, diff) thay vì line number/function name — line range corrupt 99.1% file khi lệch 1 dòng, search/replace silent 0%. Ví dụ: coding agent nên emit search/replace block, KHÔNG emit "replace lines 40–52".
- Gate action bằng oracle-exact core + abstaining soft check: bash -n/which/exact-match block ở 0% FP và catch 50% lỗi; flag check/fuzzy thành warning không chặn — cost 2.55 ms, không gọi model. Ví dụ: wrapper quanh agent terminal check syntax+binary trước khi chạy lệnh.
- Refuse-when-unsure policy (Robust-Apply Kmin=2, τhi=0.90, δ=0.20): silent 0.01% nhưng vẫn apply được 60% trường hợp fuzzy; tránh aggressive fuzzy khi KHÔNG có downstream check (test/review) — combination nguy hiểm nhất.

## Assumptions & Limitations
- Điều kiện: non-adversarial environment (agent bug/hallucinate, không malicious), faithful executor; verifier thấy action text + local environment, KHÔNG thấy intent — chỉ guard realizability (action có thực thi được hợp lệ, unambiguous không), không guard semantic correctness.
- Limitation paper thừa nhận: invalid commands và perturbed edits là synthetic, cần không match distribution real model error (dù failure mechanism intrinsic); zero-FP claim có deployment caveat (bash -n reject incomplete fragments, which miss aliases/shell functions/session-updated PATH → nên treat là abstention); real-model probe nhẹ (42 commands, 9 edits từ 1 Anthropic Claude model, version không ghi, all valid) → chỉ nói về FP side; 1 Linux host, Python/shell tooling — rate chính xác chưa chắc transfer sang ngôn ngữ/khác.
- Limitation CHƯA nói: flag extraction coverage 91.1% nghĩa là ~9% tools verifier luôn abstain (không guard được); fuzzy τ sweep chỉ tested trên Python files; benchmark valid commands từ tldr corpus có thể lệch so với lệnh agent thực sự emit; 2.55 ms median là warm cache — cold path 2.85s mỗi tool mới.

## Metadata
- 2026, Asaad Althoubi (Oklahoma State University, Stillwater, OK USA), cs.LG, https://arxiv.org/pdf/2609.11957v1, citation count: không tìm thấy [NO BENCHMARK]
