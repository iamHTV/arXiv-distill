#!/usr/bin/env bash
# ============================================================================
# arXiv-distill SUPERVISOR — chạy Hermes distill LIÊN TỤC, tự khởi động lại
# khi gặp lỗi (429, mất mạng, hết retry, crash...).
#
# Mục đích: "thử lại mãi cho đến khi gọi được" — không bao giờ chết hẳn.
#
# Cách dùng:
#   ~/work/arXiv-distill/run-distill.sh              # chạy nền giám sát
#   ~/work/arXiv-distill/run-distill.sh --once       # chạy 1 lần, không lặp
#   ~/work/arXiv-distill/run-distill.sh --stop       # dừng supervisor
#
# Log: ~/work/arXiv-distill/logs/supervisor-<ngày>.log
# Chạy trong tmux/screen để sống qua SSH disconnect:
#   tmux new -s distill '~/work/arXiv-distill/run-distill.sh'
# ============================================================================
set -uo pipefail

REPO="$HOME/work/arXiv-distill"
PROFILE="research-arxiv"
LOGDIR="$REPO/logs"
PIDFILE="$LOGDIR/supervisor.pid"
DAY="$(date +%Y%m%d_%H%M%S)"
LOG="$LOGDIR/supervisor-$DAY.log"
WATCH_LOG="$LOGDIR/watchdog.log"

# Số giây chờ giữa các lần khởi động lại (tăng dần nếu lỗi liên tiếp)
INITIAL_WAIT=5
MAX_WAIT=300
CONSEC_FAIL=0
MAX_CONSEC_FAIL=12   # 12 lần lỗi liên tiếp (~tổng chờ > 30 phút) → dừng, tránh loop vô ích

mkdir -p "$LOGDIR"

log() { echo "[$(date '+%Y-%m-%d %H:%M:%S')] $*" | tee -a "$WATCH_LOG"; }

# ── --stop ──────────────────────────────────────────────────────────────────
if [[ "${1:-}" == "--stop" ]]; then
    if [[ -f "$PIDFILE" ]]; then
        PID="$(cat "$PIDFILE")"
        if kill -0 "$PID" 2>/dev/null; then
            kill "$PID" && log "Đã dừng supervisor (PID $PID) và tiến trình con."
            pkill -P "$PID" 2>/dev/null || true
        else
            log "PID $PID không còn chạy. Dọn pidfile."
        fi
        rm -f "$PIDFILE"
    else
        log "Không có supervisor nào đang chạy (thiếu $PIDFILE)."
    fi
    exit 0
fi

# ── --once: chạy 1 lần, không lặp ──────────────────────────────────────────
ONCE=0
[[ "${1:-}" == "--once" ]] && ONCE=1

# ── Ghi pidfile ────────────────────────────────────────────────────────────
if [[ -f "$PIDFILE" ]] && kill -0 "$(cat "$PIDFILE")" 2>/dev/null; then
    log "Supervisor đã chạy (PID $(cat "$PIDFILE")). Thoát để tránh trùng."
    exit 1
fi
echo $$ > "$PIDFILE"
trap 'log "Nhận tín hiệu dừng. Thoát supervisor."; rm -f "$PIDFILE"; exit 0' INT TERM

log "=== SUPERVISOR BẮT ĐẦU (PID $$) ==="
log "Profile: $PROFILE | Repo: $REPO | Log: $LOG"
log "Cờ: --once=${ONCE} | Chờ đầu: ${INITIAL_WAIT}s | Chờ tối đa: ${MAX_WAIT}s"

cd "$REPO" || { log "FATAL: không vào được $REPO"; exit 1; }

# ── Vòng lặp giám sát ──────────────────────────────────────────────────────
FIRST_RUN=1
while true; do
    # Lần đầu chạy mới; các lần sau RESUME session gần nhất để tiếp tục đúng chỗ
    # LƯU Ý: KHÔNG dùng -Q (quiet suppress stdout khi không phải TTY → log rỗng)
    if [[ $FIRST_RUN -eq 1 ]]; then
        log "--- Lần chạy #1: bắt đầu session mới ---"
        hermes --profile "$PROFILE" chat \
            -q "Đọc report.md để biết đã distill tới paper nào. Tiếp tục distill paper tiếp theo theo protocol arxiv-distill-protocol (load skill trước). Chạy liên tục, KHÔNG dừng hỏi." \
            2>&1 | tee -a "$LOG"
        EXIT=${PIPESTATUS[0]}
        FIRST_RUN=0
    else
        log "--- Lần chạy tiếp: resume session gần nhất ---"
        hermes --profile "$PROFILE" chat --continue \
            -q "Tiếp tục distill paper tiếp theo. Chạy liên tục, KHÔNG dừng hỏi." \
            2>&1 | tee -a "$LOG"
        EXIT=${PIPESTATUS[0]}
    fi

    log "Hermes thoát với mã $EXIT"

    # Kiểm tra có phải user chủ động dừng (SIGINT) không
    if [[ -f "$PIDFILE" ]] && ! kill -0 $$ 2>/dev/null; then
        break
    fi

    if [[ $ONCE -eq 1 ]]; then
        log "Cờ --once: kết thúc sau 1 lần chạy."
        break
    fi

    # Đếm lỗi liên tiếp để backoff
    if [[ $EXIT -ne 0 ]]; then
        CONSEC_FAIL=$((CONSEC_FAIL + 1))
        WAIT=$(( INITIAL_WAIT * (2 ** (CONSEC_FAIL - 1)) ))
        [[ $WAIT -gt $MAX_WAIT ]] && WAIT=$MAX_WAIT
        log "Lỗi liên tiếp #$CONSEC_FAIL. Chờ ${WAIT}s rồi thử lại..."
        if [[ $CONSEC_FAIL -ge $MAX_CONSEC_FAIL ]]; then
            log "Đã lỗi $MAX_CONSEC_FAIL lần liên tiếp. DỪNG supervisor để tránh loop vô ích."
            log "Kiểm tra: key còn tiền? mạng OK? rồi chạy lại script."
            break
        fi
    else
        # Thoát sạch (mã 0) thường do hết turn hoặc agent dừng → khởi động lại nhẹ nhàng
        CONSEC_FAIL=0
        WAIT=$INITIAL_WAIT
        log "Thoát sạch. Nghỉ ${WAIT}s rồi tiếp tục turn mới..."
    fi

    sleep "$WAIT"
done

rm -f "$PIDFILE"
log "=== SUPERVISOR KẾT THÚC ==="
