# Skill: Cascade Attack Awareness
Source: 2605.17288
Type: workflow

## Khi nào dùng skill này

- Khi deploy LLM cascade/routing systems cần adversarial robustness — cascade efficiency gains có thể bị negate bởi targeted attacks
- Khi monitor cascade system health — detect adversarial manipulation qua escalation patterns
- Khi designing cascade architecture cần security-first approach

- KHÔNG dùng khi: standalone single-model deployment (no cascade); purely internal systems with no external input

## Input cần có

- Cascade system architecture (models, decision mechanisms)
- Baseline escalation rate metrics
- Adversarial robustness evaluation capability

## Các bước thực hiện

1. **Harden Front-End Models** — Lightweight models là weakest link. Add adversarial input detection before lightweight model. Filter: unexpected input patterns, known adversarial suffixes, anomalous token distributions.

2. **Monitor Escalation Rates** — Track escalation rate over time. Baseline: normal escalation ~10-20%. Alert threshold: >2x baseline → investigate. Sudden spikes may indicate adversarial attack.

3. **Adversarial Testing** — Red team cascade system: optimize adversarial queries that trigger unnecessary escalations. Measure: cost impact, accuracy degradation. Patch vulnerabilities found.

4. **Rate Limiting** — Implement per-user rate limits to prevent sequential adversarial query optimization. Attacker needs multiple queries to craft effective adversarial suffixes.

5. **Fallback Safety** — If escalation rate exceeds threshold, bypass cascade — route all queries to strongest model temporarily. Sacrifice cost efficiency for security.

## Output mong đợi

- Detection of adversarial escalation patterns
- Hardened cascade system resistant to targeted attacks
- Cost efficiency maintained under normal conditions

## Ví dụ áp dụng

Scenario: Customer support cascade (SLM → GPT-4). (1) Baseline: 15% escalation rate, $0.005/query avg; (2) Attack detected: escalation jumps to 45%, cost $0.025/query; (3) Response: rate limit suspicious user, add adversarial filter, temporarily bypass cascade for flagged queries; (4) Result: escalation back to 18%, cost normalized.

## Gotchas

- False positives: legitimate complex queries may trigger escalation alerts. Use multi-signal detection (not just rate).
- Rate limiting may affect legitimate heavy users. Implement per-user baselines.
- Bypass cascade safety mode increases costs — use temporarily only during investigation.
