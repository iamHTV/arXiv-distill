#!/usr/bin/env python3
"""
send_telegram.py — Gửi danh sách paper đã chấm điểm lên Telegram.

Chờ user setup bot: đặt TELEGRAM_BOT_TOKEN và TELEGRAM_CHAT_ID vào .env
Chạy:  python3 send_telegram.py scans/<ngày>.json
"""
import json
import os
import sys
import urllib.parse
import urllib.request

ENV_FILE = os.path.expanduser("~/.hermes/profiles/research-arxiv/.env")


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


def build_message(scan):
    papers = scan.get("papers", [])
    high = [p for p in papers if p.get("group") == "high"]
    fuzzy = [p for p in papers if p.get("group") == "fuzzy"]

    lines = []
    lines.append("*arXiv scan %s*" % scan.get("date", "?"))
    lines.append("Quét %d → lọc %d → chấm %d bài" % (
        scan.get("total_fetched", 0), scan.get("after_category", 0), len(papers)))
    lines.append("")

    if high:
        lines.append("*🔥 DISTILL NGAY (%d bài)*" % len(high))
        for p in high[:12]:
            lines.append("`%d` [%s](%s)" % (
                p.get("llm_score", 0), p["title"][:80], p.get("link", "")))
            if p.get("llm_reason"):
                lines.append("   _%s_" % p["llm_reason"][:90])
        lines.append("")

    if fuzzy:
        lines.append("*❓ CẦN BẠN DUYỆT (%d bài)*" % len(fuzzy))
        for p in fuzzy[:12]:
            lines.append("`%d` [%s](%s)" % (
                p.get("llm_score", 0), p["title"][:80], p.get("link", "")))
        lines.append("")

    if not high and not fuzzy:
        lines.append("_Không có paper đáng chú ý hôm nay._")

    return "\n".join(lines)


def main():
    if len(sys.argv) < 2:
        sys.exit("Dùng: python3 send_telegram.py scans/<ngày>.json")
    scan = json.load(open(sys.argv[1]))
    env = load_env()
    token = env.get("TELEGRAM_BOT_TOKEN")
    chat = env.get("TELEGRAM_CHAT_ID")
    if not token or not chat:
        print("CHƯA SETUP TELEGRAM. Cần thêm vào %s:" % ENV_FILE)
        print("  TELEGRAM_BOT_TOKEN=<token từ @BotFather>")
        print("  TELEGRAM_CHAT_ID=<chat id của bạn>")
        print("\n--- Nội dung SẼ gửi ---")
        print(build_message(scan))
        sys.exit(0)
    msg = build_message(scan)
    r = send(msg, token, chat)
    print("Đã gửi:", r.get("ok"), "| message_id:", r.get("result", {}).get("message_id"))


if __name__ == "__main__":
    main()
