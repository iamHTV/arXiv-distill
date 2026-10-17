# Skill: tagr-temporally-adaptive-recommendation
Source: 2608.24034v1
Type: framework

## When to use this skill
- Building live-streaming advertising recommendation systems on e-commerce platforms.
- Need to adapt to constantly changing live-streaming ads (live scene and promoted products change within minutes).
- Want to improve live-room entry rate, shopping-cart click rate, and revenue.

## When NOT to use this skill
- Static ad recommendation systems that don't change over time.
- No data about live scene and promoted products.
- Don't need temporal adaptation.

## Input needed
- Live scene and promoted products for each live-streaming ad.
- User live-room entry histories.
- Auxiliary behavior sequences of users.
- Post-request intent evidence and business value.
- Generative recommendation model.

## Steps to execute
1. Live-ad tokenization: periodically update SID of each active live ad based on current live scene and promoted products, while retaining stable hierarchical token vocabulary.
2. User intent modeling: model live-room entry histories at multiple temporal granularities as primary intent sequence, preserve auxiliary behavior sequences as separate input channels, weight next-token prediction using post-request intent evidence and business value.
3. Preference alignment: periodically sample fresh candidate groups from current policy and perform behavior- and value-aligned preference updates interleaved with supervised NTP maintenance.
4. Deploy on e-commerce live-stream advertising platform and evaluate live-room entry rate, shopping-cart click rate, and revenue.

## Expected output
- Live-streaming advertising recommendation system improving live-room entry rate by 8.5% and shopping-cart click rates by 7.4%.
- Revenue lift of 16.1% vs production baseline.

## Application example
- Build a live-streaming advertising recommendation system for an e-commerce platform: periodically update SID of each live ad based on live scene and promoted products, model user intent at multiple temporal granularities, and perform preference updates interleaved with supervised NTP maintenance.

## Gotchas
- Evaluated on a single e-commerce live-streaming platform (Kuaishou); results may not transfer to other platforms.
- No detailed information about training time and computational cost.
- Need to run periodically to update SID assignments and user intent models.
