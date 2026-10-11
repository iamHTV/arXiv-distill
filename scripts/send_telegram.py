#!/usr/bin/env python3
"""
send_telegram.py — Gửi danh sách paper đã chấm điểm lên Telegram.

Gửi 3 section (theo yêu cầu user — bài máy cho đúng chưa chắc user thấy đúng):
  1. 🔥 DISTILL NGAY   (điểm 75+)   — máy tự làm
  2. ⏳ LÀM SAU        (điểm 55-74) — máy tự làm sau
  3. ❓ CẦN BẠN DUYỆT  (điểm 35-54) — chờ user quyết khi dậy

Mỗi bài kèm tóm tắt gọn (1-2 câu) để user hiểu paper làm gì.

Chờ user setup bot: đặt TELEGRAM_BOT_TOKEN và TELEGRAM_CHAT_ID vào .env
Chạy:  python3 send_telegram.py scans/<ngày>.json
"""
import json
import os
import sys
import urllib.parse
import urllib.request

ENV_FILE = os.path.expanduser("~/.hermes/profiles/research-arxiv/.env")
MAX_PER_SECTION = 15   # tránh tele message quá dài


def load_env():
    env = {}
    if os.path.exists(ENV_FILE):
        for line in open(ENV_FILE):
            s = line.strip()
            if s and not s.startswith("#") and chr(61) in s:
                k, v = s.split(chr(61), 1)
                env[k.strip()] = v.strip().strip('"').strip("'")
    return env


def send(text, token, chat_id):
    url = "https://api.telegram.org/bot%s/sendMessage" % token
    data = urllib.parse.urlencode({
        "chat_id": chat_id,
        "text": text,
        "parse_mode": "Markdown",
        "disable_web_page_preview": "true",
    }).encode()
    req = urllib.request.Request(url, data=data)
    with urllib.request.urlopen(req, timeout=30) as r:
        return json.load(r)


def _short(s, n=140):
    s = " ".join((s or "").split())
    return s[:n] + ("…" if len(s) > n else "")


def build_message(scan):
    papers = scan.get("papers", [])
    high = sorted([p for p in papers if p.get("group") == "high"],
                  key=lambda x: -x.get("llm_score", 0))
    mid = sorted([p for p in papers if p.get("group") == "mid"],
                 key=lambda x: -x.get("llm_score", 0))
    fuzzy = sorted([p for p in papers if p.get("group") == "fuzzy"],
                   key=lambda x: -x.get("llm_score", 0))

    L = []
    L.append("*arXiv scan %s*" % scan.get("date", "?"))
    L.append("Quét %d → lọc %d bài → chấm %d | 🔥%d ⏳%d ❓%d" % (
        scan.get("total_fetched", 0), scan.get("after_category", 0),
        len(papers), len(high), len(mid), len(fuzzy)))

    def section(icon, title, items, note):
        if not items:
            return
        L.append("")
        L.append("%s *%s (%d)* — _%s_" % (icon, title, len(items), note))
        for p in items[:MAX_PER_SECTION]:
            L.append("")
            L.append("*%d* · [%s](%s)" % (p.get("llm_score", 0),
                                         _short(p["title"], 90), p.get("link", "")))
            # Tóm tắt gọn paper LÀM GÌ (để user hiểu), rồi lý do chấm điểm
            sm = p.get("llm_summary") or ""
            if sm:
                L.append("   📄 %s" % _short(sm, 220))
            rs = p.get("llm_reason") or ""
            if rs:
                L.append("   📝 %s" % _short(rs, 160))
            L.append("   `%s`" % p["id"])
        if len(items) > MAX_PER_SECTION:
            L.append("_…và %d bài nữa (xem scans/%s.json)_" % (
                len(items) - MAX_PER_SECTION, scan.get("date", "")))

    section("🔥", "DISTILL NGAY", high, "máy tự làm")
    section("⏳", "LÀM SAU", mid, "máy tự làm sau khi xong nhóm trên")
    section("❓", "CẦN BẠN DUYỆT", fuzzy, "mơ hồ — chờ bạn quyết khi dậy")

    if not (high or mid or fuzzy):
        L.append("")
        L.append("_Không có bài đáng chú ý — có thể arXiv nghỉ (cuối tuần) hoặc chưa có bài mới._")

    return "\n".join(L)


def main():
    if len(sys.argv) < 2:
        sys.exit("Dùng: python3 send_telegram.py scans/<ngày>.json")
    scan = json.load(open(sys.argv[1]))
    env = load_env()
    token = env.get("TELEGRAM_BOT_TOKEN")
    chat = env.get("TELEGRAM_CHAT_ID")
    msg = build_message(scan)

    if not token or not chat:
        print("CHƯA SETUP TELEGRAM. Cần thêm vào %s:" % ENV_FILE)
        print("  TELEGRAM_BOT_TOKEN=<token từ @BotFather>")
        print("  TELEGRAM_CHAT_ID=<chat id của bạn>")
        print("\n--- Nội dung SẼ gửi ---")
        print(msg)
        sys.exit(0)

    # Telegram giới hạn 4096 ký tự/message → tách nếu dài
    chunks, cur = [], ""
    for line in msg.split("\n"):
        if len(cur) + len(line) + 1 > 3900:
            chunks.append(cur)
            cur = ""
        cur += line + "\n"
    if cur.strip():
        chunks.append(cur)

    for i, c in enumerate(chunks, 1):
        r = send(c, token, chat)
        print("Đã gửi phần %d/%d: %s" % (i, len(chunks), r.get("ok")))


if __name__ == "__main__":
    main()
