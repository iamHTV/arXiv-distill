# Skill: IEC Hop-Witness Audit (intent-execution correspondence check)
Source: 2610.04375
Type: evaluation-method / debugging-workflow

## When to use this skill
- A coding/CLI agent runs the correct call but fails, and it is unclear whether the model or the harness is at fault
- Benchmarking an agent on Windows/PowerShell/cmd.exe — you need to separate LLM quality from launch loss
- An agent retries a correct call multiple times and still fails (silent divergence — 80.7% of merged-backslash changes report NO error)

Do NOT use: the agent runs on Linux with the command passed as an argument to the shell (0 changed calls in 1,779+4,012+161,214 calls); the failure is clearly a generation error (the text does not parse as emitted).

## Input required
- Recorded tool calls + tool results of the run (trajectory)
- Knowledge of the launch path: harness (Claude Code, Codex, Qwen Code, OpenHands, SWE-ReX, Aider, DeepSeek Harness, Gemini CLI, Terminus-2), shell (Bash, PowerShell 5.1, cmd.exe, dash, zsh), platform (Windows/Linux)
- 20 test payloads: argument values containing quotes, backslashes, line breaks, special characters, empty strings, strings ≥8,000 chars

## Steps
1. Place a witness at each hop WITHOUT executing the call: Bash → a BASH_ENV file (Bash sources it before executing the command string); appended launch (text after `-Command`) → compute the script PowerShell would execute per powershell.exe rules and compare its parse with the parse of the text; process interface → an argv probe in place of the program; with an LLM in the loop → an argv sentry recording ancestor processes; structured tools → record the bound values.
2. Compare the received action with the sent action USING THE RECEIVER'S OWN PARSER: Bash → compare operators, words, heredoc bodies; PowerShell → compare parse trees; programs → compare argument vectors. Do NOT use string equality (it misclassifies 15/35 unchanged pairs). Changes happen via 4 mechanisms: quote consumption, re-expansion, truncation (MSYS2: 8,186 UTF-16 units; cmd.exe: first line break), arity change.
3. Attribute the failure: parse the agent's text with execution disabled — does not parse = generation error; parses but the witness sees a difference = path; an error at a line beyond the end of the text = path (wrapper-appended); parses + intact + invokes a further interpreter = nested hop.
4. Repair replay: replay the recorded run with ONLY the named hop repaired (reply cache, no LLM) — confirms path-caused losses. A launch that changes a call at 2 hops needs both repaired (later hop first).
5. Apply the IntAct rendering at the named hop: Bash wrapper → command file + `source`; PowerShell process interface → native argument rendering (Eq. 1: `\"` for a double quote, double the backslash runs before the closing quote); host wrapper → `-EncodedCommand Base64(UTF16(text))`; interactive Bash typing → switch off history expansion + completion before typing. Multi-line text under cmd.exe → REFUSE (name the hop and what was not executed).
6. Measure the effect: changed-call rate before/after, pass@1 with the exact McNemar test, tokens per passed task, false-confirmation rate (runs reported completed but failed).

## Expected output
- The first hop that changed the call (FD) + mechanism (quote consumption/re-expansion/truncation/arity) + silent or loud.
- A rendering or refusal for each call; changed-call rate → 0 on exposed calls; tokens per passed task drop ~2.4× (up to 12.3× for chains on the appended launch).
- Example: Claude Code production — 227/227 changed calls rerouted, 0/3,540 ran calls changed, +4ms per call.

## Example application
- Agent on Windows: pytest `"test_app (v2) & more.py"` — 13/13 LLMs emit it correctly, the appended launch converts it into an AmpersandNotAllowed error, 45/45 runs fail, the agent spends 2–7 steps retrying, 1.8× tokens. Apply the skill: the witness sees the wrapper append text after -Command → FD at the host wrapper → IntAct: script file + `-File` → 46/46 instructions intact, Qwen Code 6/30 on Windows (≈ 7/30 on Linux).

## Gotchas
- String equality is NOT enough: `"a\b"` and `a\\b` are the same word in Bash — string comparison flags 15/35 unchanged pairs as changed.
- Evidence in the tool result (call as sent + as received + named hop) does NOT help the agent repair the path (p≥.500) — fix the harness, don't just report to the agent.
- Requoting/encoding restores only a fraction of faults (uniform -EncodedCommand 38.9–87.5% of both-hop repair; native rendering alone 0%) — repair the exact named hop.
- The boundary-disclosed contract (describing the transport path in the tool description) makes the agent chain commands with `&&`, which PS 5.1 rejects — drops from 50 pairs to 36 while still reporting completion.
- The changed-call rate measured with the shortest wrapper is a LOWER BOUND (231/306 changed only at the longer session wrapper).
- Multi-line text under cmd.exe is outside the rendering domain — it can only be refused, not repaired.
- Reflexion/retries cost 463–1,180 retries per cell for 11.4–55.0% of IntAct's gain — retrying is NOT repairing.
