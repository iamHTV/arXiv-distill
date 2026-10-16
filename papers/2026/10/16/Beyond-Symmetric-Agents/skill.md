# Skill: cognitive-diversity-multi-agent-debate
Source: 2609.35875v1
Type: framework

## Khi nào dùng skill này
- Xây hệ thống đa đại lý (MAS) và muốn biết có nên dùng debate (tranh luận) giữa các agent hay không.
- Muốn tận dụng cognitive diversity (đa dạng nhận thức) giữa các agent thay vì sao chép cùng một agent.
- Làm việc với small open-weight models.

## Tình huống KHÔNG nên dùng
- Chỉ dùng một agent đơn lẻ, không có đa đại lý.
- Muốn dùng debate cho nhiều vòng trao đổi (debate chỉ có lợi ích trong vòng đầu tiên).

## Input cần có
- Nhiều agent có tính cách/phương pháp khác nhau (cognitive diversity).
- Các tác vụ có thể đo đạc được (measurable questions) với benchmark headroom.
- Cơ chế tổng hợp kết quả (pooling/voting) từ các agent độc lập.

## Các bước thực hiện
1. Xây dựng các agent có tính cách khác nhau (không sao chép cùng một agent).
2. Thay để các agent tranh luận dài dòng, hãy giới hạn debate ở 1-2 vòng trao đổi (lợi ích chỉ ở vòng đầu tiên).
3. Cho các agent làm độc lập (independent), sau đó tổng hợp kết quả (pooling/voting) thay để để chúng tranh luận.
4. Kết hợp các agent có độ chính xác khác nhau (mixed teams) thay vì homogeneous teams (đội đồng nhất).
5. Theo dõi claim precision và accuracy để đánh giá hiệu quả.

## Output mong đợi
- Mixed teams overturn 63.7% of wrong round-one majorities vs 42.9% for homogeneous.
- Independent biographies pooled reach 64.6% vs debate's 55.6% (+8.9pp).
- Debate benefit only in first exchange (84.6% at one round, 87.2 at two, flat through five).

## Ví dụ áp dụng
Solopreneur xây MAS viết nội dung: thay để 3 agent cùng một prompts tranh luận về nội dung, hãy tạo 3 agent có góc nhìn khác nhau (một người chú ý SEO, một người chú ý tính hấp dẫn, một người chú ý độ chính xác), để mỗi người viết độc lập, sau đó tổng hợp (pool) kết quả tốt nhất.

## Gotchas
- Debate không luôn tốt hơn solo generation (loses by 1.04pp).
- Debate chỉ có lợi ích trong vòng trao đổi đầu tiên, sau đó không cải thiện thêm.
- Persona teams (đội nhân cách) giảm claim precision xuống 51.8% — không nên over-use personas.
