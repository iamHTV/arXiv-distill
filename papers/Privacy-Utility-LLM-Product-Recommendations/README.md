# [2505.00951] Bảo tồn Riêng tư và Hữu ích trong Đề xuất Sản phẩm dựa trên LLM

## Vấn đề
LLM-based recommendation systems process textual/contextual information, often using cloud-based infrastructure. User data transmitted to remote servers → privacy concerns (lo ngại riêng tư). Unlike traditional systems với structured data, LLM models process more personal information. Privacy risk: exposure và loss of control over personal data.

## Đóng góp
1. **Hybrid privacy-preserving framework**: Tách sensitive (nhạy cảm) từ nonsensitive data. Chỉ share nonsensitive với cloud cho LLM recommendations
2. **De-obfuscation module**: Reconstruct sensitive recommendations locally — không transmit privacy-critical data to server
3. **Results**: Almost same utility as sharing all data. Better HR@10 và category distribution alignment vs obfuscation-only

## Phương pháp (tóm tắt cốt lõi)
3 components: (1) BERT-based obfuscator identifies và removes sensitive products from purchase history; (2) Modified history (nonsensitive only) sent to cloud LLM for recommendations; (3) Local de-obfuscation module reconstructs sensitive-category recommendations on-device. Runs on consumer-grade hardware.

## Kết quả chính
- Baseline (full data): Categorical HR@10 = 0.6263, Semantic HR@10 = 0.3045, 100% privacy leakage
- Categorical Obfuscation: HR@10 = 0.4742, 0% privacy leakage — too much utility loss
- BERT Obfuscation: HR@10 = 0.5960 — better utility
- Our framework: almost same utility as baseline, large privacy preservation
- Runs on consumer-grade hardware (Llama 3.2 1B)
- Better category distribution alignment vs obfuscation-only

## Insight có thể áp dụng ngay
1. **Tách sensitive data trước khi send to cloud**: Khi build LLM recommendation system, classify products theo sensitivity, chỉ share nonsensitive với cloud. Ví dụ: health products → keep local. Electronics → share with cloud.

2. **Local de-obfuscation**: Reconstruct sensitive recommendations locally. Don't transmit privacy-critical data. Ví dụ: user bought vitamins → don't send to cloud. Local model predicts vitamin-related recommendations.

3. **Consumer-grade hardware feasible**: Privacy-preserving LLM recommendations run on standard devices. No need for specialized hardware. Ví dụ: mobile app can run de-obfuscation locally.

## Giả định & Hạn chế
**Điều kiện để method work:**
- BERT-based classifier for sensitivity detection
- Local LLM for de-obfuscation (Llama 3.2 1B)
- Cloud LLM for main recommendations

**Hạn chế paper thừa nhận:**
- Sensitivity classification errors (false negatives → leakage, false positives → utility loss)
- Fixed privacy definition (health-related only)
- Cumulative purchase history privacy leakage not addressed
- Input/output length constraints

**Hạn chế paper KHÔNG nói:**
- BERT classifier bias — may miss non-health sensitive items
- User-adaptive privacy controls not implemented
- Cross-user pattern inference not addressed
- Real-world deployment challenges
- Cost of local inference on mobile devices

## Metadata
- Năm: 2025
- Tác giả: Tina Khezresmaeilzadeh, Jiang Zhang, Dimitrios Andreadis, Konstantinos Psounis
- Category: cs.AI
- Link PDF: https://arxiv.org/pdf/2505.00951
- Citation count: [EXTRACTION FAILED]
