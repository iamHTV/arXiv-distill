# Skill: IEC Hop-Witness Audit (kiểm tra intent-execution correspondence)
Source: 2610.04375
Type: evaluation-method / debugging-workflow

## Khi nào dùng skill này
- Coding/CLI agent chạy đúng call nhưng fail mà KHÔNG rõ lỗi ở model hay harness
- Benchmark score agent trên Windows/PowerShell/cmd.exe — cần tách LLM quality khỏi launch loss
- Agent retry call đúng nhiều lần mà vẫn fail (silent divergence — 80.7% merged-backslash changes KHÔNG báo lỗi)

Tình huống KHÔNG nên dùng: agent chạy trên Linux với command truyền làm argument cho shell (0 changed calls trong 1,779+4,012+161,214 calls); failure rõ ràng là generation error (text không parse được ngay khi emit).

## Input cần có
- Recorded tool calls + tool results của run (trajectory)
- Knowledge của launch path: harness (Claude Code, Codex, Qwen Code, OpenHands, SWE-ReX, Aider, DeepSeek Harness, Gemini CLI, Terminus-2), shell (Bash, PowerShell 5.1, cmd.exe, dash, zsh), platform (Windows/Linux)
- 20 payloads test: argument values chứa quotes, backslashes, line breaks, special characters, empty strings, strings ≥8,000 chars

## Các bước thực hiện
1. Đặt witness tại từng hop KHÔNG execute call: Bash → file BASH_ENV (Bash sources trước khi execute command string); appended launch (text sau `-Command`) → tính script PowerShell sẽ execute theo rules của powershell.exe, so sánh parse của script vs parse của text; process interface → argv probe thay program; có LLM in loop → argv sentry ghi ancestor processes; structured tools → ghi bound values.
2. So sánh received action vs sent action BẰNG RECEIVER'S OWN PARSER: Bash → so sánh operators, words, heredoc bodies; PowerShell → so sánh parse tree; program → so sánh argument vector. KHÔNG dùng string equality (misclassify 15/35 unchanged pairs). Đổi tại 4 mechanisms: quote consumption, re-expansion, truncation (MSYS2: 8,186 UTF-16 units; cmd.exe: line break đầu tiên), arity change.
3. Attribute failure: parse text của agent với execution disabled — không parse = generation error; parse được nhưng witness thấy khác = path; error ở line beyond end of text = path (wrapper-appended); parse được + intact + gọi interpreter khác = nested hop.
4. Repair replay: replay recorded run với CHỈ hop named được repair (reply cache, không LLM) — xác nhận path-caused losses. Đổi call ở 2 hops → repair cả hai (later hop first).
5. Áp dụng IntAct rendering tại named hop: Bash wrapper → command file + `source`; PowerShell process interface → native argument rendering (Eq. 1: `\"` cho double quote, double lại backslash runs trước closing quote); host wrapper → `-EncodedCommand Base64(UTF16(text))`; interactive Bash typing → switch off history expansion + completion trước khi type. Multi-line dưới cmd.exe → REFUSE (tên hop + cái gì không execute).
6. Đo effect: changed-call rate trước/sau, pass@1 với exact McNemar test, tokens per passed task, false-confirmation rate (runs báo completed nhưng fail).

## Output mong đợ
- Hop đầu tiên đổi call (FD) + mechanism (quote consumption/re-expansion/truncation/arity) + silent hay loud.
- Rendering hoặc refusal cho mỗi call; changed-call rate → 0 trên exposed calls; tokens per passed task giảm ~2.4× (đến 12.3× cho chains trên appended launch).
- Ví dụ: Claude Code production — 227/227 changed calls reroute, 0/3,540 ran calls đổi, +4ms/call.

## Ví dụ áp dụng
- Agent trên Windows: pytest `"test_app (v2) & more.py"` — 13/13 LLMs emit đúng, appended launch đổi thành AmpersandNotAllowed error, 45/45 runs fail, agent mất 2–7 steps retry, 1.8× tokens. Áp dụng skill: witness thấy wrapper append text sau -Command → FD tại host wrapper → IntAct: script file + `-File` → 46/46 instructions intact, Qwen Code 6/30 Windows (≈ 7/30 Linux).

## Gotchas
- String equality KHÔNG đủ: `"a\b"` và `a\\b` là cùng word trong Bash — string comparison báo 15/35 unchanged pairs là changed.
- Evidence trong tool result (call as sent + as received + named hop) KHÔNG giúp agent sửa path (p≥.500) — phải sửa harness, không phải báo cho agent.
- Requoting/encoding chỉ restore phân số faults (uniform -EncodedCommand 38.9–87.5% của both-hop repair; native rendering alone 0%) — phải repair đúng named hop.
- Boundary-disclosed contract (mô tả transport path trong tool description) làm agent chain lệnh bằng `&&` mà PS 5.1 reject — rơi 50 pairs còn 36, vẫn báo completion.
- Changed-call rate đo bằng shortest wrapper là LOWER BOUND (231/306 chỉ đổi ở longer session wrapper).
- Multi-line text dưới cmd.exe nằm ngoài rendering domain — chỉ refuse được, KHÔNG repair.
- Reflexion/retry tốn 463–1,180 retries/cell cho 11.4–55.0% gain của IntAct — retry KHÔNG phải repair.
