# WORKFLOW HẰNG NGÀY — Profile `research-arxiv`

Mục tiêu: **distill paper arXiv chạy tự động**, bạn chỉ cần khởi động + kiểm tra kết quả.
Việc ra tiền của profile này = số paper chất lượng hoàn thành, KHÔNG phải tinh chỉnh config.

---

## 1. BUỔI SÁNG — Khởi động (2 phút)

```bash
# Mở tmux để agent sống qua SSH disconnect
tmux new -s distill

# Khởi động supervisor (tự chạy + tự khởi động lại khi chết)
~/work/arXiv-distill/run-distill.sh

# Rời tmux nhưng ĐỂ NÓ CHẠY NỀN: nhấn Ctrl+B rồi D
```

Agent tự: đọc report.md → biết tới paper nào → distill tiếp → commit+push từng paper.

---

## 2. TRONG NGÀY — Thăm nom (30 giây/lần, 1-2 lần)

```bash
# Xem tiến độ (không vào tmux)
tail -30 ~/work/arXiv-distill/logs/watchdog.log

# Đếm paper đã xong
ls ~/work/arXiv-distill/papers/ | wc -l

# Xem commit mới nhất (bằng chứng thật đã push)
git -C ~/work/arXiv-distill log --oneline -5
```

Nếu thấy `Rate limited. Waiting...` trong log → **bình thường**, agent đang tự chờ. Đừng can thiệp.

---

## 3. KHI CÓ VIỆC ĐỘT XUẤT — Vào tmux trực tiếp

```bash
tmux attach -t distill      # xem agent đang làm gì real-time
# (muốn thoát ra lại: Ctrl+B rồi D)
```

---

## 4. CUỐI NGÀY — Kiểm tra & dừng (2 phút)

```bash
# Dừng supervisor (an toàn, không mất dữ liệu — paper đã commit rồi)
~/work/arXiv-distill/run-distill.sh --stop

# Kiểm tra mọi thứ đã push
git -C ~/work/arXiv-distill status
git -C ~/work/arXiv-distill log --oneline -10

# Đếm thành quả hôm nay
git -C ~/work/arXiv-distill log --since="1 day ago" --oneline | wc -l
```

---

## 5. CHECKLIST SỨC KHỎE (làm khi agent có vẻ đứng)

| Triệu chứng | Nguyên nhân | Cách xử lý |
|---|---|---|
| Log ngừng ghi > 10 phút | Agent treo / API hết tiền | Xem `logs/supervisor-*.log` |
| `API call failed after 8 retries` | 429 kéo dài / hết credit | Kiểm tra số dư OpenRouter |
| README/skill rỗng | Điểm yếu ling (nhả rỗng) | Agent tự retry; nếu lặp → xem file thủ công |
| Supervisor dừng sau 12 lỗi | Loop vô ích | Sửa nguyên nhân gốc rồi chạy lại |
| Không thấy paper mới | Agent dừng hỏi | Kiểm tra SOUL/rule — phải chạy không dừng |

---

## 6. LỆNH THƯỜNG DÙNG (copy nhanh)

```bash
# Chạy tự động cả ngày
tmux new -s distill '~/work/arXiv-distill/run-distill.sh'

# Chạy 1 lần (không supervisor)
cd ~/work/arXiv-distill && hermes --profile research-arxiv chat

# Resume session gần nhất (nếu agent chết)
cd ~/work/arXiv-distill && hermes --profile research-arxiv chat --continue

# Dừng
~/work/arXiv-distill/run-distill.sh --stop

# Xem log
tail -f ~/work/arXiv-distill/logs/watchdog.log
```

---

## 7. NGUYÊN TẮC VÀNG

1. **Đừng nghịch config khi chưa cần.** Config đã chuẩn (max_turns 500, retry 8, streaming off).
2. **Số paper là thước đo duy nhất.** Không phải "config đẹp" hay "model xịn".
3. **429 không phải lỗi.** Agent tự chờ + retry. Chỉ can thiệp nếu quá 10 phút không tiến.
4. **Commit+push sau mỗi paper.** Đã tự động. Không cần làm tay.
5. **Sáng khởi động, tối kiểm tra.** Ở giữa để nó tự chạy.

---

## 8. CHẠY BẰNG CRONJOB (nếu muốn tự khởi động mỗi ngày)

Nếu không muốn nhớ khởi động tay, đặt cronjob Hermes chạy mỗi sáng.
**CẢNH BÁO:** Hermes cron vẫn cần MÁY BẬT. Tắt máy = không chạy.

```
hermes cronjob tạo job: mỗi sáng 7h, chạy supervisor script
```
