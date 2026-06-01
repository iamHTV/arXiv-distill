# Skill: Cascade Attack Awareness
Source: 2605.17288
Type: workflow

## When to use this skill

- When deploying cascade/routing systems needing adversarial robustness
- When monitoring cascade health — detect manipulation via escalation patterns
- When designing security-first cascade architecture

- Do NOT use when: standalone single-model deployment; purely internal systems

## Input needed

- Cascade system architecture
- Baseline escalation metrics
- Adversarial evaluation capability

## Steps

1. **Harden Front-End Models** — Add adversarial input detection before lightweight model.
2. **Monitor Escalation Rates** — Track over time. Alert at >2x baseline.
3. **Adversarial Testing** — Red team cascade system, patch vulnerabilities.
4. **Rate Limiting** — Per-user limits to prevent sequential optimization.
5. **Fallback Safety** — Bypass cascade if escalation exceeds threshold.

## Expected output

- Detection of adversarial patterns
- Hardened cascade system
- Cost efficiency maintained under normal conditions

## Example application

Customer support cascade: baseline 15% escalation → attack detected at 45% → rate limit + filter → normalized to 18%.

## Gotchas

- False positives from legitimate complex queries
- Rate limiting affects heavy users
- Bypass mode increases costs temporarily
