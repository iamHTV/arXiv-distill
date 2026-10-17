#!/bin/bash
# Cron watchdog for arXiv distill - retry every 15 minutes until success
LOG_DIR="/home/iamhtv/work/arXiv-distill/logs"
LOG_FILE="$LOG_DIR/cron.log"
REPO_DIR="/home/iamhtv/work/arXiv-distill"
PROFILE="research-arxiv"
MAX_RETRIES=96  # ~24 hours at 15-minute intervals
RETRY_COUNT=0

mkdir -p "$LOG_DIR"

log() {
    echo "[$(date '+%Y-%m-%d %H:%M:%S')] $1" | tee -a "$LOG_FILE"
}

log "=== Cron watchdog started ==="

while [ $RETRY_COUNT -lt $MAX_RETRIES ]; do
    RETRY_COUNT=$((RETRY_COUNT + 1))
    log "Attempt $RETRY_COUNT/$MAX_RETRIES"

    cd "$REPO_DIR" || { log "FATAL: cannot cd to $REPO_DIR"; exit 1; }

    # Run Hermes distill session
    GIT_TERMINAL_PROMPT=0 hermes --profile "$PROFILE" chat \
        --yolo \
        -q "Đọc report.md để biết đã distill tới paper nào. Tiếp tục distill paper tiếp theo theo protocol arxiv-distill-protocol (load skill trước). Chạy liên tục, KHÔNG dừng hỏi giữa chừng." \
        2>&1 | tee -a "$LOG_FILE"

    EXIT=${PIPESTATUS[0]}

    if [ $EXIT -eq 0 ]; then
        log "=== Distill completed successfully ==="
        exit 0
    else
        log "=== Attempt failed (exit code $EXIT), retrying in 15 minutes ==="
        sleep 900
    fi
done

log "=== Max retries reached, giving up ==="
exit 1
