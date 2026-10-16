# Skill: surveyagent-hka-scientific-survey
Source: 2609.05938v1
Type: framework

## Khi nào dùng skill này
- Sinh bài khảo sát khoa học hoặc tài liệu tài nguyên bằng LLM.
- Muốn cải thiện chất lượng bài khảo sát bằng cách kết hợp kiến thức của con người (human knowledge augmentation).
- Có tài liệu tham khảo và muốn tạo bài khảo sát có cấu trúc tốt.

## Tình huống KHÔNG nên dùng
- Không có tài liệu tham khảo để sinh bài khảo sát.
- Không cần bài khảo sát có cấu trúc, chỉ cần tóm tắt ngắn gọn.

## Input cần có
- Tài liệu tham khảo khoa học (papers, reports, v.v.).
- Kiến thức của con người (human knowledge) để augment (ví dụ review, chỉnh sửa của chuyên gia).
- Hệ thống LLM có thể sinh bài khảo sát.

## Các bước thực hiện
1. Thu thập tài liệu tham khảo liên quan đến chủ đề khảo sát.
2. Dùng LLM để sinh bản thảo bài khảo sát (outline, nội dung các section).
3. Kết hợp kiến thức của con người: chuyên gia review, chỉnh sửa, bổ sung nội dung (human knowledge augmentation).
4. Áp dụng các thành phần như citation expansion, re-ranking, clustering, few-shot learning để cải thiện chất lượng.
5. Đánh giá chất lượng bài khảo sát (citation quality, key-point recall, heading match).

## Output mong đợi
- Citation quality: CS (14.95% P, 19.53% R, 16.94% F1), Medicine (16.78% P, 22.95% R, 19.39% F1).
- Key-point recall: 53.85% (CS), 57.07% (medicine).
- Với human augmentation: citation F1 tăng 3.86% (CS), +2.62% (Medicine).

## Ví dụ áp dụng
Solopreneur viết bài khảo sát về "AI trong y tế": thu thập các paper liên quan, dùng LLM sinh bản thảo, sau đó mời chuyên gia y tế review và chỉnh sửa (human augmentation). Kết hợp citation expansion và re-ranking để cải thiện chất lượng trích dẫn và cấu trúc bài khảo sát.

## Gotchas
- Cần đủ tài liệu tham khảo và kiến thức của con người để augmentation có hiệu quả.
- Các thành phần như citation expansion, re-ranking, clustering, few-shot learning đều quan trọng, không nên bỏ qua.
- Chưa đánh giá chi phí thực tế của human augmentation.
