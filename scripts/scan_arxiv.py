#!/usr/bin/env python3
"""
scan_arxiv.py — Quét paper arXiv mới theo watermark, lọc category, chấm điểm LLM.

Chạy:  python3 scan_arxiv.py [--dry-run] [--max-llm N]
Output: scans/<ngày>.json  +  state/last_scan.json (cập nhật watermark)
"""
import argparse
import datetime as dt
import json
import os
import re
import sys
import time
import urllib.parse
import urllib.request

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
STATE_FILE = os.path.join(REPO, "state", "last_scan.json")
SCANS_DIR = os.path.join(REPO, "scans")
ENV_FILE = os.path.expanduser("~/.hermes/profiles/research-arxiv/.env")

# ── Cấu hình ────────────────────────────────────────────────────────────────
CATS_KEEP = ["cs.AI", "cs.CL", "cs.LG", "cs.MA", "cs.IR", "cs.SE", "cs.HC"]
CATS_BLOCK = [
    "physics.", "math.", "q-bio.", "q-fin.", "stat.", "eess.",
    "cond-mat", "astro-ph", "gr-qc", "hep-", "nucl-",
]
# Heuristic CHỈ để loại bài rõ ràng ngoài chủ đề — KHÔNG lọc mạnh.
# Máy chạy 24/7 + token free → không cần tiết kiệm. Thà chấm thừa còn hơn bỏ sót.
HEURISTIC_MIN = 4           # rất thấp: chỉ loại bài hoàn toàn lạc đề
LLM_MODEL = "inclusionai/ling-3.1-flash"
LLM_MAX = 10000             # gần như không trần — token free, chạy 24/7

API = "https://export.arxiv.org/api/query"
USER_AGENT = "arxiv-distill-research/1.0 (personal use)"


def load_key():
    key = None
    for line in open(ENV_FILE):
        s = line.strip()
        if s.startswith("OPENROUTER_API_KEY" + chr(61)):
            key = s.split(chr(61), 1)[1].strip().strip('"').strip("'")
            break
    if not key:
        sys.exit("Không tìm thấy OPENROUTER_API_KEY trong " + ENV_FILE)
    return key


def load_watermark():
    if os.path.exists(STATE_FILE):
        try:
            return json.load(open(STATE_FILE)).get("last_scan")
        except Exception:
            pass
    # Mặc định: 3 ngày trước
    return (dt.datetime.now(dt.timezone.utc) - dt.timedelta(days=3)).strftime("%Y-%m-%dT%H:%M:%SZ")


def save_watermark(ts):
    os.makedirs(os.path.dirname(STATE_FILE), exist_ok=True)
    json.dump({"last_scan": ts, "updated": dt.datetime.now(dt.timezone.utc).isoformat()},
              open(STATE_FILE, "w"), indent=2)


def fetch_cat(cat, max_results=200):
    q = urllib.parse.quote("cat:%s" % cat)
    url = ("%s?search_query=%s&sortBy=submittedDate&sortOrder=descending"
           "&max_results=%d" % (API, q, max_results))
    req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    with urllib.request.urlopen(req, timeout=60) as r:
        return r.read().decode()


def parse_entries(xml):
    out = []
    for e in re.findall(r"<entry>(.*?)</entry>", xml, re.S):
        def g(tag):
            m = re.search(r"<%s>(.*?)</%s>" % (tag, tag), e, re.S)
            return re.sub(r"\s+", " ", m.group(1)).strip() if m else ""
        cats = re.findall(r'<category term="([^"]+)"', e)
        out.append({
            "id": g("id").split("/")[-1],
            "title": g("title"),
            "abstract": g("summary"),
            "published": g("published"),
            "updated": g("updated"),
            "cats": cats,
            "link": g("id"),
        })
    return out


KW_CORE = ["llm", "language model", "agent", "transformer", "rag", "retrieval",
           "prompt", "fine-tun", "reasoning", "inference", "multi-agent",
           "tool use", "embedding", "attention", "neural", "deep learning",
           "foundation model", "diffusion", "reinforcement"]
KW_APPLIED = ["experiment", "benchmark", "dataset", "evaluation", "we evaluate",
              "we test", "results show", "outperform", "accuracy", "baseline",
              "case study"]
KW_BIZ = ["business", "marketing", "customer", "commerce", "e-commerce", "sales",
          "advertising", "decision", "consumer", "enterprise", "revenue",
          "pricing", "recommendation", "personaliz", "workflow", "productivity"]


def heuristic_score(p):
    text = (p["title"] + " " + p["abstract"]).lower()
    core = sum(1 for k in KW_CORE if k in text)
    appl = sum(1 for k in KW_APPLIED if k in text)
    biz = sum(1 for k in KW_BIZ if k in text)
    nums = len(re.findall(r"\d+\.?\d*\s?%", p["abstract"]))
    return core * 4 + appl * 3 + biz * 4 + nums * 2, core, appl, biz, nums


def _group_from_score(s):
    """Phân nhóm dự phòng khi LLM không trả 'group'."""
    if s >= 75:
        return "high"
    if s >= 55:
        return "mid"
    if s >= 35:
        return "fuzzy"
    if s >= 0:
        return "drop"
    return "error"


def _call_llm(p, key, body):
    """Gọi LLM 1 lần, parse JSON vào p. Dùng chung cho chấm điểm + retry."""
    req = urllib.request.Request(
        "https://openrouter.ai/api/v1/chat/completions", data=body,
        headers={"Authorization": "Bearer " + key, "Content-Type": "application/json"})
    try:
        with urllib.request.urlopen(req, timeout=120) as r:
            d = json.load(r)
        msg = d["choices"][0]["message"]
        txt = msg.get("content") or ""
        # Fallback: ling đôi khi trả JSON trong "reasoning" thay vì "content"
        if not txt.strip() and msg.get("reasoning"):
            txt = msg["reasoning"]
        m = re.search(r"\{[^{}]*\"score\"[^{}]*\}", txt, re.S)
        if not m:
            m = re.search(r"\{.*\}", txt, re.S)
        j = json.loads(m.group(0)) if m else {}
        if not j or "score" not in j:
            p["llm_score"] = -1
            p["llm_summary"] = ""
            p["llm_reason"] = "PARSE_FAIL: %s" % (txt[:60].replace("\n", " "))
            p["group"] = "error"
        else:
            p["llm_score"] = int(j.get("score", 0))
            p["llm_summary"] = j.get("summary", "")
            p["llm_reason"] = j.get("reason", "")
            p["group"] = j.get("group") or _group_from_score(p["llm_score"])
    except Exception as ex:
        p["llm_score"] = -1
        p["llm_summary"] = ""
        p["llm_reason"] = "LLM_FAIL: %s" % str(ex)[:60]
        p["group"] = "error"
    return p


def llm_score_batch(papers, key, max_llm):
    """Chấm điểm bằng LLM, tuần tự với adaptive sleep chống 429."""
    scored = []
    consec_429 = 0
    for i, p in enumerate(papers[:max_llm]):
        prompt = (
            "Bạn chấm điểm mức độ liên quan của paper arXiv cho một solopreneur "
            "làm content/business về AI. Chấm 0-100 theo 4 tiêu chí:\n"
            "- Liên quan cốt lõi (0-35): AI/LLM/agent/multi-agent/tool-use?\n"
            "- Ứng dụng thực tiễn (0-25): có experiment/benchmark thật?\n"
            "- Liên quan business/content (0-20): áp dụng được cho business/marketing/content?\n"
            "- Insight hành động được (0-20): đọc xong làm được gì cụ thể?\n\n"
            "TITLE: %s\n\nABSTRACT: %s\n\n"
            "Trả về DUY NHẤT JSON: {\"score\": <0-100>, "
            "\"summary\": \"<1 câu nói paper LÀM GÌ, tiếng Việt>\", "
            "\"reason\": \"<1 câu vì sao điểm này>\", "
            "\"group\": \"<high|mid|fuzzy|drop>\"}" % (p["title"], p["abstract"][:1500])
        )
        body = json.dumps({
            "model": LLM_MODEL,
            "messages": [{"role": "user", "content": prompt}],
            "max_tokens": 2000,   # PHẢI lớn: ling là model reasoning, dồn token vào
                                  # reasoning trước khi trả content. 300 → content rỗng.
        }).encode()
        _call_llm(p, key, body)
        scored.append(p)
        print("  [%d/%d] %s -> %s" % (i + 1, min(max_llm, len(papers)),
                                      p["id"], p.get("llm_score")))

        # Adaptive sleep: càng gặp 429 liên tiếp, nghỉ càng lâu (giảm dần khi OK).
        if p.get("llm_score", -1) == -1:
            consec_429 += 1
            wait = min(5 * consec_429, 30)
        else:
            consec_429 = 0
            wait = 4
        time.sleep(wait)

    # Retry các bài lỗi (-1) — thường do 429. Chờ lâu rồi thử lại, tối đa 2 vòng.
    for attempt in (1, 2):
        failed = [p for p in scored if p.get("llm_score", -1) == -1]
        if not failed:
            break
        wait = 15 * attempt
        print("  Retry vòng %d: %d bài lỗi (chờ %ds)..." % (attempt, len(failed), wait))
        time.sleep(wait)
        for p in failed:
            _score_one(p, key)
            time.sleep(4)
    return scored


def _score_one(p, key):
    """Chấm điểm 1 paper (dùng cho retry)."""
    prompt = (
        "Chấm điểm paper arXiv cho solopreneur content/business về AI, thang 0-100.\n"
        "- Liên quan cốt lõi AI/LLM/agent: 0-35\n"
        "- Ứng dụng thực tiễn (experiment/benchmark): 0-25\n"
        "- Liên quan business/marketing/content: 0-20\n"
        "- Insight hành động được: 0-20\n\n"
        "TITLE: %s\n\nABSTRACT: %s\n\n"
        "Trả về DUY NHẤT JSON: {\"score\": <0-100>, "
        "\"summary\": \"<1 câu nói paper LÀM GÌ, tiếng Việt>\", "
        "\"reason\": \"<1 câu vì sao điểm này>\", "
        "\"group\": \"<high|mid|fuzzy|drop>\"}" % (p["title"], p["abstract"][:1500])
    )
    body = json.dumps({"model": LLM_MODEL,
                       "messages": [{"role": "user", "content": prompt}],
                       "max_tokens": 2000}).encode()
    return _call_llm(p, key, body)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--dry-run", action="store_true", help="Không gọi LLM")
    ap.add_argument("--max-llm", type=int, default=LLM_MAX)
    args = ap.parse_args()

    wm = load_watermark()
    print("Watermark lần quét trước: %s" % wm)

    # 1) Quét
    all_papers, seen = [], set()
    for cat in CATS_KEEP:
        try:
            xml = fetch_cat(cat)
            entries = parse_entries(xml)
            for p in entries:
                if p["id"] in seen:
                    continue
                seen.add(p["id"])
                all_papers.append(p)
            print("  %-8s -> %d bài" % (cat, len(entries)))
            time.sleep(3)  # arXiv rate limit
        except Exception as e:
            print("  %-8s -> LỖI: %s" % (cat, str(e)[:80]))

    print("\nTổng unique: %d bài" % len(all_papers))

    # 2) Lọc theo watermark
    fresh = [p for p in all_papers if p["published"] >= wm]
    print("Sau watermark (%s): %d bài" % (wm, len(fresh)))

    # 3) Lọc category (bỏ block)
    kept = []
    for p in fresh:
        if any(any(b in c for b in CATS_BLOCK) for c in p["cats"]):
            continue
        if not any(c in CATS_KEEP for c in p["cats"]):
            continue
        kept.append(p)
    print("Sau lọc category: %d bài" % len(kept))

    # 4) Heuristic lọc thô
    passed = []
    for p in kept:
        hs, core, appl, biz, nums = heuristic_score(p)
        p["heuristic"] = hs
        if hs >= HEURISTIC_MIN:
            passed.append(p)
    passed.sort(key=lambda x: -x["heuristic"])
    print("Sau heuristic (>=%d): %d bài" % (HEURISTIC_MIN, len(passed)))

    # 5) LLM chấm điểm
    if args.dry_run:
        print("\n[DRY-RUN] Bỏ qua LLM. Top 10 theo heuristic:")
        for p in passed[:10]:
            print("  %3d  %s  %s" % (p["heuristic"], p["id"], p["title"][:60]))
        result = passed
    else:
        print("\nChấm điểm LLM (tối đa %d bài)..." % args.max_llm)
        key = load_key()
        result = llm_score_batch(passed, key, args.max_llm)
        result.sort(key=lambda x: -x.get("llm_score", 0))

    # 6) Lưu
    os.makedirs(SCANS_DIR, exist_ok=True)
    today = dt.datetime.now().strftime("%Y-%m-%d")
    outfile = os.path.join(SCANS_DIR, today + ".json")
    json.dump({
        "date": today,
        "watermark_from": wm,
        "total_fetched": len(all_papers),
        "after_watermark": len(fresh),
        "after_category": len(kept),
        "after_heuristic": len(passed),
        "papers": result,
    }, open(outfile, "w"), ensure_ascii=False, indent=2)
    print("\nĐã lưu: %s" % outfile)

    # 7) Cập nhật watermark — CHỈ khi có bài MỚI (fresh), không phải mọi lần quét.
    # Nếu fresh=0 (chưa có bài mới / arXiv nghỉ / lỗi mạng), GIỮ nguyên watermark
    # để lần sau quét lại từ mốc đó — tránh bỏ sót bài.
    if len(fresh) > 0:
        save_watermark(dt.datetime.now(dt.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"))
        print("Watermark mới: %s" % dt.datetime.now(dt.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"))
    else:
        print("Không có bài mới (fresh=0) → GIỮ nguyên watermark.")

    # 8) Tóm tắt nhóm
    if not args.dry_run:
        groups = {}
        for p in result:
            groups.setdefault(p.get("group", "?"), []).append(p)
        print("\n=== PHÂN NHÓM ===")
        for g in ["high", "mid", "fuzzy", "drop", "error"]:
            print("  %-6s: %d" % (g, len(groups.get(g, []))))


if __name__ == "__main__":
    main()
