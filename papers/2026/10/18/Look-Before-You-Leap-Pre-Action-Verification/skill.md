# Skill: Pre-Action Verification Gate cho LLM Agent (shell + code edit)
Source: 2609.11957v1 (Look Before You Leap)
Type: framework (oversight guard)

## Khi nào dùng skill này
- Agent thực thi shell command hoặc apply code edit vào file thật, và 1 silent failure (action tưởng thành công nhưng sai đích) có thể phá hỏng toàn bộ trajectory sau đó.
- Cần guard model-agnostic, cost ~ms, không gọi model — wrap quanh agent hiện có (kể cả frontier agent đóng).
- KHÔNG nên dùng khi: action không có checkable surface (raw byte offset, opaque handle — nên đổi interface thay vì guard); cần đánh giá semantic correctness (edit đúng chỗ nhưng logic sai — cần test/reviewer riêng).

## Input cần có
- Action text (command string hoặc edit spec) + local environment (installed tools qua PATH, current file content).
- Với command: flag set extract sẵn per tool (từ --help, -h, man), cache 1 lần (cold cost p95 2.85 s/tool).
- Với edit: anchor content + params Robust-Apply (Kmin, τhi, δ), đề xuất (2, 0.90, 0.20).
- Quyết định deployment: safety floor (chấp nhận bao nhiêu warn/refuse) và có downstream check (test/review) hay không.

## Các bước thực hiện
1. Phân loại representation: content-anchored (search/replace, unified diff) hay location-anchored (line range, function name). Ưu tiên content-anchored; nếu agent emit location-anchored → chuyển đổi hoặc đánh dấu ungroundable.
2. Chạy oracle-exact core (block, 0% false positive): command → bash -n + which (subcommand-aware); edit → exact rồi whitespace-normalized match, unique match thì apply luôn.
3. Chạy soft check có abstention (không block, chỉ warn): flag validity (membership in extracted flag set — abstain nếu tool không extract được flags hoặc token single-dash multi-char); fuzzy match chỉ chấp nhận khi s1 ≥ τhi VÀ s1 − s2 ≥ δ.
4. Two-tier gate: oracle-exact fail → BLOCK (recoverable signal cho agent retry); soft-check suspicion → WARN không chặn (7.0% warn-rate ở shell).
5. Apply edit qua Robust-Apply: anchor < Kmin → clean-fail; unique exact/wsnorm match → apply; fuzzy đạt floor + margin → commit qua real patch; còn lại → REFUSE (clean-fail, never guess).
6. Trả structured signal khi refuse/warn: suspected flag, ambiguous match + runner-up — agent có thể act trên đó, không phải bare rejection.
7. Đo silent rate theo taxonomy: success / clean failure / silent failure trên admitted actions — dùng 1 scalar silent rate làm safety axis, applicability làm axis còn lại.

## Output mong đợi
- Command gate: recall 0.958 @ FPR 0.070 (selective grounding), oracle-exact core recall 0.500 @ 0% FP, median 2.55 ms/command (warm).
- Edit gate: silent misapplication 0.01% (1/8,320) qua mọi format/perturbation, giữ 60% applies của fuzzy, applicability 0.51 vs 0.98 trên perturbed single-hunk.

## Ví dụ áp dụng
- Coding agent muốn edit `config.py`: thay vì emit "replace lines 40–52" (location-anchored — corrupt 99.1% file nếu file lệch 1 dòng), agent emit search/replace block; gate chạy exact match → unique → apply. Nếu anchor trùng 2 chỗ (ambiguous) → gate refuse, agent nhận signal "2 candidates: line 40 vs line 88" và chọn lại.

## Gotchas
- Không bao giờ kết hợp aggressive fuzzy matching với KHÔNG có downstream check — silent corruption tích lũy thầm lặng (fuzzy multi-hunk silent 39.3%).
- bash -n reject incomplete fragments, which miss aliases/shell functions/session-updated PATH — treat các case này là abstention, không phải block.
- Flag check chỉ tốt bằng extraction coverage (91.1% tools); 9% tools còn lại verifier luôn abstain → không guard được, cần completion spec per tool.
- Guard realizability, không guard semantics: command hợp lệ nhưng harmful effect, hoặc edit đúng chỗ nhưng logic sai — nằm ngoài tầm guard, cần test/reviewer.
- Silent failure KHÔNG trigger rollback (rollback chỉ fire trên observed error) — defense-in-depth: pre-action guard + differential testing + second-model reviewer.
