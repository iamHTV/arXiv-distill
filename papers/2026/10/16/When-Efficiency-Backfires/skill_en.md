# Skill: cascade-attack-awareness
Source: 2605.17288v1
Type: framework

## When to use this skill
- Building or using cascade LLM systems (lightweight model handles simple queries, powerful model handles complex queries).
- Want to evaluate cascade system robustness against adversarial attacks.
- Need to add defense mechanisms for cascade LLM systems.

## When NOT to use
- Using a single LLM model only, no cascade system.
- Don't need to evaluate robustness, only need performance.

## Required input
- A cascade LLM system (lightweight model + powerful model).
- Real or synthetic query data to test attacks.
- An adversarial attack mechanism to test with.

## Steps
1. Build cascade LLM system: lightweight model handles simple queries, powerful model handles complex queries (escalation).
2. Test the system with adversarial attacks: adversarial suffixes, jailbreak prompts, etc.
3. Measure prediction accuracy, token cost, execution time, and attack success rate before and after attack.
4. Add defense mechanisms: input sanitization, output validation, rate limiting, adversarial training.
5. Test again after adding defenses to confirm effectiveness.

## Expected output
- Reduce accuracy reduction (from 84.6% down to lower level).
- Reduce token cost inflation (from 148.9% down to lower level).
- Reduce execution time increase (from 108.9% down to lower level).
- Reduce attack success rate (from 81.4% down to lower level).

## Example application
Solopreneur building a customer support chatbot cascade LLM: lightweight model handles simple questions, powerful model handles complex questions. Test with adversarial attacks (e.g. questions with embedded commands, jailbreak prompts). Add input sanitization and output validation to reduce risk. Reduce system being fooled or producing unwanted content.

## Gotchas
- Cascade LLM systems can trigger cascade failure under adversarial attacks.
- Attack can reduce accuracy by up to 84.6%, inflate token cost by 148.9%, increase execution time by up to 108.9%.
- Should evaluate robustness before production deployment, don't assume cascade is automatically safe.
