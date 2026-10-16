#!/usr/bin/env bash
# ============================================================================
# daily_scan.sh — Chạy bởi CRONJOB lúc 5h sáng (giờ VN).
# Quét arXiv → lọc → chấm điểm → ghi file tóm tắt + gửi Telegram.
# KHÔNG tự distill (user thức dậy duyệt rồi mới distill).
#
# LƯU Ý: dùng đường dẫn TUYỆT ĐỐI, KHÔNG dùng $HOME — vì khi chạy trong cronjob
# dưới profile research-arxiv, $HOME bị override thành profile home.
# ============================================================================
set -uo pipefail
REPO="/home/iamhtv/work/arXiv-distill"
cd "$REPO" || exit 1
TODAY="$(date +%F)"
LOGDIR="$REPO/logs"; mkdir -p "$LOGDIR"
LOG="$LOGDIR/daily-scan-$TODAY.log"
SCAN_JSON="scans/$TODAY.json"

{
  echo "=== DAILY SCAN $(date '+%F %T %Z') ==="
  # python3 -u: unbuffered → log ghi realtime, thấy được tiến trình khi chạy nền/cron.
  python3 -u scripts/scan_arxiv.py
  SCAN_RC=${PIPESTATUS[0]:-$?}

  # Chỉ ghi tóm tắt + gửi tele khi CÓ file scan (tránh lỗi khi scan fail giữa chừng)
  if [[ -f "$SCAN_JSON" ]]; then
    echo "--- ghi tóm tắt + gửi Telegram ---"
    python3 scripts/send_telegram.py "$SCAN_JSON"
    echo "File tóm tắt: scans/$TODAY/SUMMARY.md"
  else
    echo "!!! Không có $SCAN_JSON — scan thất bại (arXiv rate limit?). Bỏ qua tele."
    echo "!!! Sẽ thử quét lại ở lần chạy sau (watermark không đổi)."
  fi
  echo "=== XONG $(date '+%F %T %Z') ==="
} >> "$LOG" 2>&1
