# Skill: avri-vulnerability-reasoning-interface
Source: 2610.11602v1
Type: framework

## When to use this skill
- Building vulnerability discovery agents that need to reduce token cost and time without sacrificing success and recall.
- Agent runs long, consuming millions of tokens, needs to reuse evidence rather than repeatedly retrieve and reconstruct.
- Can access source repository and analysis tools (gdb, radare2, strace, objdump).

## When NOT to use this skill
- Vulnerability discovery without source code access (binary-only analysis).
- No need to reduce inference cost, only care about absolute success rate.
- No ability to build persistent Bidirectional Evidence Trace (BET).

## Input needed
- Vulnerable source repository, target program, fuzz-driver entry point.
- Input-format guidance.
- Analysis tools: gdb, radare2, strace, objdump.
- Agent capable of calling shell commands and manipulating files in workspace.

## Steps to execute
1. Build persistent Bidirectional Evidence Trace (BET) — connects harness input consumption with conditions required to make a selected operation unsafe.
2. Retain source-supported correspondences alongside the agent's hypotheses and open questions.
3. Provide reading, analysis, and persistence commands to help agents build and reuse evidence rather than repeatedly retrieve and reconstruct.
4. Keep responses within output budget — prioritize requested code and relations needed to interpret it; return large results as excerpts with omitted ranges or continuation information.
5. Keep conditions grouped so shortening a response does not silently remove an alternative.
6. Separate shared instructions from changing work records so the stable prompt prefix can be reused.
7. Log tool outputs and content supplied to the model (timing, cache status, usage) to distinguish backend reuse, evidence recovery, and billed tokens.
8. Evaluate cost of complete runs and vulnerability discovery outcomes; use interaction records to explain results.

## Expected output
- Reduces total cost by 18.0% for Codex and 23.7% for OpenCode vs baseline, preserving success and improving/maintaining recall.
- Reduces runtime (Codex: 50,968s → 33,313s; OpenCode: 25,324s → 24,017s).

## Application example
- Vulnerability discovery agent on an open-source C/C++ project: instead of repeatedly retrieving related functions, agent uses BET to store evidence about unsafe functions, input constraint hypotheses, and open questions; when prior evidence is needed, agent retrieves from BET instead of regenerating full context.

## Gotchas
- Cost of complete runs and vulnerability discovery outcomes must be evaluated together, not just a single number.
- Unsuitable signals and auxiliary overhead limit existing methods' benefits — only 24.4% of matched comparisons preserve success at lower cost.
- One run per configuration does not establish robustness to run-to-run variation.
