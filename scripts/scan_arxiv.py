#!/usr/bin/env python3
"""
scan_arxiv.py — Quét paper arXiv mới theo watermark, lọc category, chấm điểm LLM.

Chạy:  python3 scan_arxiv.py [--dry-run] [--max-llm N]
Output: scans/<ngày>.json  +  state/last_scan.json (cập nhật watermark)
"""
import argparse
import datetime as dt
import glob
import json
import os
import re
import sys
import time
import urllib.parse
import urllib.request
import urllib.error

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
STATE_FILE = os.path.join(REPO, "state", "last_scan.json")
SEEN_FILE = os.path.join(REPO, "state", "seen_ids.json")
SCANS_DIR = os.path.join(REPO, "scans")
# ĐƯỜNG DẪN TUYỆT ĐỐI — KHÔNG dùng expanduser/$HOME.
# Khi cronjob chạy dưới profile research-arxiv, $HOME bị override thành
# /home/iamhtv/.hermes/profiles/research-arxiv/home → expanduser("~/.hermes/...")
# sẽ ghép nhân đôi path và FileNotFoundError. Bug thật đã gặp 13/10 + 15/10/2026.
ENV_FILE = "/home/iamhtv/.hermes/profiles/research-arxiv/.env"

# ── Cấu hình ────────────────────────────────────────────────────────────────
CATS_KEEP = ["cs.AI", "cs.CL", "cs.LG", "cs.MA", "cs.IR", "cs.SE", "cs.HC"]
CATS_BLOCK = [
    "physics.", "math.", "q-bio.", "q-fin.", "stat.", "eess.",
    "cond-mat", "astro-ph", "gr-qc", "hep-", "nucl-",
]
# Heuristic CHỈ để loại bài rõ ràng ngoài chủ đề — KHÔNG lọc mạnh.
# Máy chạy 24/7 + token free → không cần tiết kiệm. Thà chấm thừa còn hơn bỏ sót.
HEURISTIC_MIN = 4           # rất thấp: chỉ loại bài hoàn toàn lạc đề
# Fallback chain model chấm điểm (đều giá $0).
# 3.1 bị provider Novita rate-limit nặng → tự chuyển 3.0 khi 429.
LLM_MODELS = ["inclusionai/ling-3.1-flash", "inclusionai/ling-3.0-flash"]
LLM_MODEL = LLM_MODELS[0]   # model chính (giữ tên cũ cho tương thích)
LLM_MAX = 10000             # gần như không trần — token free, chạy 24/7
BATCH_SIZE = 10             # chấm 10 bài/prompt → giảm 10x số request (chống 429)
FETCH_PER_CAT = 1000        # bài/category/lần quét. 200 chỉ phủ ~14h → hở 1 ngày là mất bài.
SEEN_KEEP = 40000           # giữ tối đa bao nhiêu ID đã xử lý (dedupe)

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
    """Sàn an toàn: mốc published cũ nhất từng được coi là 'đã xử lý'.

    Từ khi chuyển sang dedupe-theo-ID (B), watermark KHÔNG còn là nguồn chân lý
    để lọc bài mới. Nó chỉ là lưới an toàn: nếu seen_ids.json hỏng/mất, ta vẫn
    có mốc thời gian để không phải quét lại từ đầu. Mặc định 3 ngày trước.
    """
    if os.path.exists(STATE_FILE):
        try:
            wm = json.load(open(STATE_FILE)).get("last_scan")
            if wm:
                return wm
        except Exception:
            pass
    return (dt.datetime.now(dt.timezone.utc) - dt.timedelta(days=3)).strftime("%Y-%m-%dT%H:%M:%SZ")


def save_watermark(ts):
    os.makedirs(os.path.dirname(STATE_FILE), exist_ok=True)
    json.dump({"last_scan": ts, "updated": dt.datetime.now(dt.timezone.utc).isoformat()},
              open(STATE_FILE, "w"), indent=2)


def load_seen():
    """Nạp set các arXiv ID đã xử lý. Nếu file chưa có → migrate từ scans/*.json.

    Đây là NGUỒN CHÂN LÝ cho việc lọc bài mới. Lọc theo tập ID (không theo mốc
    thời gian) nên KHÔNG BAO GIỜ mất bài, bất kể cron hở bao nhiêu ngày.
    """
    if os.path.exists(SEEN_FILE):
        try:
            data = json.load(open(SEEN_FILE))
            ids = data.get("ids", []) if isinstance(data, dict) else data
            return list(ids)
        except Exception:
            pass
    # Migrate: nạp ID từ mọi scans/*.json đã có (giữ thứ tự thời gian tăng dần)
    ids = []
    for f in sorted(glob.glob(os.path.join(SCANS_DIR, "20*.json"))):
        try:
            for p in json.load(open(f)).get("papers", []):
                if p.get("id"):
                    ids.append(p["id"])
        except Exception:
            continue
    return list(dict.fromkeys(ids))


def save_seen(ids):
    """Ghi set ID, giữ tối đa SEEN_KEEP phần tử mới nhất (chống file phình vô hạn)."""
    os.makedirs(os.path.dirname(SEEN_FILE), exist_ok=True)
    ids = list(dict.fromkeys(ids))          # dedupe, giữ thứ tự
    if len(ids) > SEEN_KEEP:
        ids = ids[-SEEN_KEEP:]
    json.dump({"updated": dt.datetime.now(dt.timezone.utc).isoformat(),
               "count": len(ids), "ids": ids},
              open(SEEN_FILE, "w"), indent=1)


def fetch_cat(cat, max_results=FETCH_PER_CAT, retries=3):
    """Quét 1 category, retry khi arXiv rate limit (429)."""
    q = urllib.parse.quote("cat:%s" % cat)
    url = ("%s?search_query=%s&sortBy=submittedDate&sortOrder=descending"
           "&max_results=%d" % (API, q, max_results))
    for attempt in range(retries):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
            with urllib.request.urlopen(req, timeout=60) as r:
                return r.read().decode()
        except urllib.error.HTTPError as e:
            if e.code == 429 and attempt < retries - 1:
                wait = 15 * (attempt + 1)
                print("    (arXiv 429, chờ %ds rồi thử lại)" % wait)
                time.sleep(wait)
                continue
            raise
        except Exception:
            if attempt < retries - 1:
                time.sleep(10 * (attempt + 1))
                continue
            raise
    return ""


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


def _batch_prompt(batch):
    """Tạo prompt chấm nhiều bài cùng lúc (1 request)."""
    pr = (
        "Bạn chấm điểm mức độ liên quan của TỪNG paper arXiv cho một solopreneur "
        "làm content/business về AI (cờ tướng, content 30+, nhiều kênh). "
        "Mỗi paper chấm 0-100 theo 4 tiêu chí:\n"
        "- Liên quan cốt lõi AI/LLM/agent/multi-agent/tool-use (0-35)\n"
        "- Ứng dụng thực tiễn, có experiment/benchmark thật (0-25)\n"
        "- Liên quan business/marketing/content/decision (0-20)\n"
        "- Insight hành động được, đọc xong làm được gì (0-20)\n\n"
    )
    for p in batch:
        pr += "ID: %s\nTITLE: %s\nABSTRACT: %s\n\n" % (
            p["id"], p["title"], p["abstract"][:1400])
    pr += ("Trả về DUY NHẤT JSON MẢNG, mỗi phần tử 1 paper, đủ mọi ID:\n"
           "[{\"id\":\"<id>\",\"score\":<0-100>,"
           "\"summary\":\"<1 câu paper LÀM GÌ, tiếng Việt>\","
           "\"reason\":\"<1 câu vì sao điểm này>\"}, ...]")
    return pr


def _call_llm_batch(batch, key):
    """Chấm 1 loạt bài trong 1 request. Thử lần lượt fallback chain khi 429."""
    prompt = _batch_prompt(batch)
    for model in LLM_MODELS:
        body = json.dumps({
            "model": model,
            "messages": [{"role": "user", "content": prompt}],
            "max_tokens": 8000,   # batch → cần nhiều token cho reasoning + JSON
        }).encode()
        req = urllib.request.Request(
            "https://openrouter.ai/api/v1/chat/completions", data=body,
            headers={"Authorization": "Bearer " + key, "Content-Type": "application/json"})
        try:
            with urllib.request.urlopen(req, timeout=240) as r:
                d = json.load(r)
            msg = d["choices"][0]["message"]
            txt = msg.get("content") or msg.get("reasoning") or ""
            m = re.search(r"\[.*\]", txt, re.S)
            if not m:
                continue   # model này không trả JSON → thử model kế
            arr = json.loads(m.group(0))
            by_id = {str(x.get("id", "")): x for x in arr if isinstance(x, dict)}
            n = 0
            for p in batch:
                x = by_id.get(p["id"])
                if x and "score" in x:
                    p["llm_score"] = int(x.get("score", 0))
                    p["llm_summary"] = x.get("summary", "")
                    p["llm_reason"] = x.get("reason", "")
                    p["group"] = _group_from_score(p["llm_score"])
                    n += 1
            if n > 0:
                return n
        except urllib.error.HTTPError as e:
            if e.code == 429:
                continue   # 429 → thử model kế trong chain
            continue
        except Exception:
            continue
    # Hết chain mà không chấm được bài nào → đánh dấu LỖI cho MỌI bài trong batch.
    # Bắt buộc: nếu không set llm_score, các bài này (a) không được retry
    # (retry tìm llm_score==-1), (b) vẫn lọt vào seen_ids → MẤT VĨNH VIỄN.
    # Bug thật gặp 16/10: 8 batch 0/10 → 93 bài suýt mất.
    for p in batch:
        if "llm_score" not in p:
            p["llm_score"] = -1
            p["llm_summary"] = ""
            p["llm_reason"] = "BATCH_FAIL: hết fallback chain, không parse được JSON"
            p["group"] = "error"
    return 0


def llm_score_batch(papers, key, max_llm):
    """Chấm điểm bằng LLM theo BATCH (10 bài/request) → giảm 10x số request.

    ling qua provider Novita bị rate limit nặng (~50% 429 dù nghỉ 10s).
    Batch là cách duy nhất hiệu quả: 260 bài → 26 request thay vì 260.
    """
    todo = papers[:max_llm]
    total = len(todo)
    print("  Chấm %d bài theo batch %d bài/request (~%d request)..." %
          (total, BATCH_SIZE, (total + BATCH_SIZE - 1) // BATCH_SIZE))

    for bi in range(0, total, BATCH_SIZE):
        batch = todo[bi:bi + BATCH_SIZE]
        n = _call_llm_batch(batch, key)
        ids = ",".join(p["id"] for p in batch)
        print("  batch %d-%d: %d/%d ok" % (bi + 1, bi + len(batch), n, len(batch)))
        # sleep ngắn giữa các batch (mỗi batch là 1 request)
        time.sleep(4)

    # Retry các bài lỗi (batch nhỏ hơn để dễ thành công)
    for attempt in (1, 2):
        failed = [p for p in todo if p.get("llm_score", -1) == -1]
        if not failed:
            break
        print("  Retry vòng %d: %d bài lỗi..." % (attempt, len(failed)))
        time.sleep(10 * attempt)
        for bi in range(0, len(failed), 5):   # batch 5 khi retry
            _call_llm_batch(failed[bi:bi + 5], key)
            time.sleep(5)
    return todo


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--dry-run", action="store_true", help="Không gọi LLM")
    ap.add_argument("--max-llm", type=int, default=LLM_MAX)
    args = ap.parse_args()

    wm = load_watermark()
    seen = set(load_seen())
    print("Watermark (sàn an toàn): %s" % wm)
    print("Đã biết (seen_ids): %d ID" % len(seen))

    # 1) Quét
    all_papers, seen_batch = [], set()
    for cat in CATS_KEEP:
        try:
            xml = fetch_cat(cat)
            entries = parse_entries(xml)
            for p in entries:
                if p["id"] in seen_batch:
                    continue
                seen_batch.add(p["id"])
                all_papers.append(p)
            print("  %-8s -> %d bài" % (cat, len(entries)))
            time.sleep(8)  # arXiv rate limit: ~3 req nhanh → chặn. Giãn 8s cho an toàn
        except Exception as e:
            print("  %-8s -> LỖI: %s" % (cat, str(e)[:80]))

    print("\nTổng unique: %d bài" % len(all_papers))

    # 2) Lọc bài MỚI theo tập ID đã xử lý (nguồn chân lý).
    # Đã chấm rồi → có trong seen → bỏ. Chưa có → bài mới, đem chấm.
    # Không phụ thuộc mốc thời gian nên hở bao nhiêu ngày cũng không mất bài.
    fresh = [p for p in all_papers if p["id"] not in seen]
    print("Sau lọc seen-ID: %d bài mới" % len(fresh))

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
        backlog = len(passed) - len(result)
        if backlog > 0:
            print("  ⚠ Tồn đọng %d bài vượt trần --max-llm → sẽ chấm ở lần chạy sau "
                  "(KHÔNG mất, vì không nạp vào seen)." % backlog)

    # 6) Lưu
    os.makedirs(SCANS_DIR, exist_ok=True)
    today = dt.datetime.now().strftime("%Y-%m-%d")
    outfile = os.path.join(SCANS_DIR, today + ".json")
    json.dump({
        "date": today,
        "watermark_from": wm,
        "seen_before": len(seen),
        "total_fetched": len(all_papers),
        "after_seen": len(fresh),
        "after_category": len(kept),
        "after_heuristic": len(passed),
        "papers": result,
    }, open(outfile, "w"), ensure_ascii=False, indent=2)
    print("\nĐã lưu: %s" % outfile)

    # 7) Cập nhật state:
    #    a) seen_ids: CHỈ nạp bài đã CHẤM THÀNH CÔNG (llm_score >= 0).
    #       - Bài vượt trần --max-llm → không nạp → lần sau chấm tiếp.
    #       - Bài lỗi (llm_score == -1) → KHÔNG nạp → lần sau chấm lại.
    #       - dry-run → không nạp gì.
    #       Đây là chốt chống mất bài quan trọng nhất.
    #    b) watermark: = max(published) THẬT, KHÔNG phải giờ chạy (bug gốc).
    if args.dry_run:
        done_ids = []
    else:
        done_ids = [p["id"] for p in result if p.get("llm_score", -1) >= 0]
    n_err = sum(1 for p in result if p.get("llm_score", -1) == -1)
    all_ids = list(seen) + done_ids
    save_seen(all_ids)
    print("seen_ids: %d ID (+%d đã xử lý OK)" % (len(set(all_ids)), len(set(done_ids))))
    if n_err:
        print("  ⚠ %d bài lỗi KHÔNG nạp vào seen → sẽ chấm lại lần sau." % n_err)

    pubs = [p["published"] for p in all_papers if p.get("published")]
    if pubs and not args.dry_run:
        wm_new = max(pubs)
        save_watermark(wm_new)
        print("Watermark mới (= max published thật): %s" % wm_new)
    else:
        print("Không cập nhật watermark/seen (quét rỗng hoặc dry-run).")

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
