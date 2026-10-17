# Skill: energy-efficient-llm-code-prompting
Source: 2610.02571v1
Type: framework

## When to use this skill
- Generating code with LLMs for production and wanting to reduce execution energy of generated code.
- Need to evaluate energy efficiency of LLM-generated code, not just functional correctness.
- Can measure execution energy of Python or C++ programs.

## When NOT to use this skill
- Output is not runnable code whose energy can be measured (e.g., text, structured data).
- No tool to measure execution energy for Python/C++.
- Applying to programming languages other than Python and C++ (experiments limited to these two).

## Input needed
- Set of solvable programming problems (e.g., from EffiBench or LeetCode).
- Test cases to check functional correctness of generated code.
- Tool to measure execution energy for Python/C++ programs.
- Access to at least one LLM API for code generation.

## Steps to execute
1. Select a set of solvable programming problems with standard test cases for functional correctness.
2. Build a baseline prompt for code generation on each problem.
3. Design 21 different prompting strategies, including the baseline prompt as reference.
4. Run initial analysis stage: evaluate on a stratified subset of 110 problems (10 per algorithmic category), 3 models, Python only.
5. Filter to problems where all prompting strategies (including baseline) produce functionally correct solutions across all evaluated models.
6. Select the 8 most consistently energy-reducing prompting strategies from stage 1.
7. Run extended evaluation: 8 selected strategies + baseline on the full evaluation set, both Python and C++, 10 models.
8. Measure fine-grained execution energy for each generated program.
9. Compare execution energy of each prompting strategy vs baseline; select strategies consistently reducing energy across models and languages.

## Expected output
- List of prompting strategies reducing execution energy of LLM-generated code (up to 25% Python, 17% C++).
- Understanding of how strategy effectiveness varies by model and programming language.

## Application example
- Generating Python code for revenue apportionment: use Prompt 21 (−49% energy vs baseline in initial stage) instead of a simple prompt, measure execution energy on standard test set, select strategy consistently reducing energy across models.

## Gotchas
- Prompting strategies require significantly more tokens, increasing inference energy cost — overall efficiency must account for both inference energy and execution energy.
- Effectiveness not consistent across models, languages, or strategies — some reduce energy, others increase it vs baseline.
- Experiments limited to Python and C++; does not include other languages.
- Evaluation benchmark has imbalanced difficulty distribution (more Medium than Easy/Hard).
