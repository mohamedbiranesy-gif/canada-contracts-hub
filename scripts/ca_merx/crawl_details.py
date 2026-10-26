#!/usr/bin/env python3
"""Fetch MERX public award (and optionally notice) tabs for awarded solicitations in listing.jsonl.

  award tab : https://www.merx.com/public/solicitations/<merx_id>/abstract/award
  notice tab: https://www.merx.com/public/solicitations/<merx_id>/abstract/notice
Only rows with row_type == "solicitation" have public abstracts (row_type "notice" rows are
MERX "interception" mirrors of other portals and redirect to login).
Writes one JSON line per solicitation to <outdir>/details.jsonl (resumable), fields:
  merx_id, listing, award_html_fields (list of awardee blocks), notice_fields, raw html saved under pages/.
Usage: python3 -I crawl_details.py <outdir> <tabs: award|award,notice> [max] [workers]
"""
import sys, os, re, json, time, html, datetime, threading, queue
import requests

UA = "contracts-research/1.0"
outdir = sys.argv[1]
tabs = sys.argv[2].split(",") if len(sys.argv) > 2 else ["award"]
max_n = int(sys.argv[3]) if len(sys.argv) > 3 else 10**9
workers = int(sys.argv[4]) if len(sys.argv) > 4 else 3
GLOBAL_RATE = float(os.environ.get("MERX_RATE", "3.0"))

listing_path = os.path.join(outdir, "listing.jsonl")
details_path = os.path.join(outdir, "details.jsonl")
log_path = os.path.join(outdir, "crawl_details.log")
pages_dir = os.path.join(outdir, "detail_pages")
os.makedirs(pages_dir, exist_ok=True)
write_lock = threading.RLock()
rate_lock = threading.Lock()
last_req = [0.0]


def log(msg):
    with write_lock:
        with open(log_path, "a") as f:
            f.write(f"{datetime.datetime.now(datetime.timezone.utc).isoformat()} {msg}\n")


def throttle():
    with rate_lock:
        now = time.time()
        wait = last_req[0] + 1.0 / GLOBAL_RATE - now
        if wait > 0:
            time.sleep(wait)
        last_req[0] = time.time()


def clean(s):
    s = re.sub(r"<br\s*/?>", "\n", s)
    s = re.sub(r"<[^>]+>", " ", s)
    s = html.unescape(s).replace("\xa0", " ").replace(" ", " ")
    s = re.sub(r"[ \t\r]+", " ", s)
    s = re.sub(r"\s*\n\s*", "\n", s)
    return s.strip()


def inner_html(page_html):
    m = re.search(r'\$\("#innerTabContent"\)\.html\(\'(.*?)\'\);', page_html, re.S)
    if not m:
        return None
    s = m.group(1)
    try:
        s = s.encode("utf-8").decode("unicode_escape")
        s = s.encode("latin-1").decode("utf-8", errors="replace")
    except Exception:
        pass
    return s.replace("\\/", "/").replace("\\'", "'")


FIELD_RE = re.compile(r'<div id="[^"]*"\s+class="mets-field mets-field-view[^"]*">\s*<span\s+class="mets-field-label">(.*?)</span>\s*<div class="mets-field-body[^"]*">(.*?)</div>\s*</div>', re.S)


def parse_fields(seg):
    out = []
    for m in FIELD_RE.finditer(seg):
        label = clean(m.group(1))
        body = m.group(2)
        out.append((label, clean(body), body.strip()))
    return out


def parse_award(s):
    rec = {"awardees": [], "fields": {}}
    # top-level fields before awardee blocks
    blocks = re.split(r'<div class="fieldset awardeeItem content-block">', s)
    head = blocks[0]
    for label, val, raw in parse_fields(head):
        rec["fields"][label] = val
    for b in blocks[1:]:
        a = {}
        for label, val, raw in parse_fields(b):
            if label == "Address":
                a["Address"] = val
                a["Address_lines"] = [clean(x) for x in re.split(r"<br\s*/?>", raw) if clean(x)]
            else:
                a[label] = val
        d = re.search(r'<h3 class="awardeeSubTitle">Description</h3>\s*<span[^>]*>(.*?)</span>\s*<button', b, re.S)
        if d:
            a["Description"] = clean(d.group(1))
            a["Description_html"] = d.group(1).strip()
        rec["awardees"].append(a)
    return rec


def parse_notice(s):
    rec = {"fields": {}, "sections": {}}
    for label, val, raw in parse_fields(s):
        if label in rec["fields"] and rec["fields"][label] != val:
            k = 2
            while f"{label}_{k}" in rec["fields"]:
                k += 1
            label = f"{label}_{k}"
        rec["fields"][label] = val
    d = re.search(r'id="descriptionText"[^>]*>(.*?)</span>\s*<button', s, re.S)
    if d:
        rec["description"] = clean(d.group(1))
        rec["description_html"] = d.group(1).strip()
    cats = re.findall(r'<li[^>]*class="[^"]*category[^"]*"[^>]*>(.*?)</li>', s, re.S)
    if cats:
        rec["categories"] = [clean(c) for c in cats]
    return rec


def fetch(sess, url):
    for attempt in range(5):
        throttle()
        try:
            r = sess.get(url, timeout=60, allow_redirects=False)
            if r.status_code == 200:
                return r.status_code, r.text
            if r.status_code in (301, 302, 404, 410):
                return r.status_code, None
            if r.status_code == 202:
                # MERX answers 202 with an empty body when requests overlap; back off and retry
                time.sleep(2 + 2 * attempt)
                continue
            log(f"{url} HTTP {r.status_code} attempt {attempt}")
            if r.status_code == 403 and attempt >= 1:
                return 403, None  # persistent plain-nginx 403 for this solicitation (restricted), not a challenge
        except Exception as e:
            log(f"{url} error {e!r} attempt {attempt}")
        time.sleep(2 + 2 * attempt)
    return None, None


def worker(q, sess, counter):
    while True:
        item = q.get()
        if item is None:
            q.task_done()
            return
        mid = item["merx_id"]
        rec = {"merx_id": mid, "listing": item, "tabs": {}}
        for tab in tabs:
            url = f"https://www.merx.com/public/solicitations/{mid}/abstract/{tab}"
            code, text = fetch(sess, url)
            t = {"url": url, "http_status": code}
            if text:
                with open(os.path.join(pages_dir, f"{mid}_{tab}.html"), "w", encoding="utf-8") as f:
                    f.write(text)
                inner = inner_html(text)
                if inner is None:
                    t["no_inner_content"] = True
                else:
                    t["parsed"] = parse_award(inner) if tab == "award" else parse_notice(inner)
            rec["tabs"][tab] = t
        rec["retrieved_at"] = datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
        with write_lock:
            with open(details_path, "a") as f:
                f.write(json.dumps(rec, ensure_ascii=False) + "\n")
            counter[0] += 1
            if counter[0] % 200 == 0:
                log(f"details written {counter[0]} (queue {q.qsize()}) last award {item.get('award_date')}")
        q.task_done()


def main():
    done = set()
    if os.path.exists(details_path):
        with open(details_path) as f:
            for line in f:
                try:
                    done.add(json.loads(line)["merx_id"])
                except Exception:
                    pass
    log(f"start tabs={tabs} already done {len(done)} workers {workers}")
    sess = requests.Session()
    sess.headers["User-Agent"] = UA
    q = queue.Queue(maxsize=100)
    counter = [0]
    threads = [threading.Thread(target=worker, args=(q, sess, counter), daemon=True) for _ in range(workers)]
    for t in threads:
        t.start()
    queued = 0
    idle = 0
    seen = set(done)
    # Priority order: newest award date first. Re-read the (growing) listing each round, pick the
    # pending rows with the latest award_date, queue a batch, repeat.
    while queued < max_n:
        pending = {}
        with open(listing_path) as f:
            for line in f:
                if not line.endswith("\n"):
                    break
                try:
                    item = json.loads(line)
                except Exception:
                    continue
                if item.get("row_type") != "solicitation":
                    continue
                mid = item.get("merx_id")
                if not mid or mid in seen or mid in pending:
                    continue
                pending[mid] = item
        if not pending:
            idle += 1
            lp = os.path.join(outdir, "crawl_listing.log")
            if os.path.exists(lp) and open(lp).read().rstrip().endswith("done") and idle > 2:
                break
            if idle > 600:
                break
            time.sleep(5)
            continue
        idle = 0
        batch = sorted(pending.values(), key=lambda it: (it.get("award_date") or "")[:10] if (it.get("award_date") or "")[:4].isdigit() and int(it["award_date"][:4]) < 2100 else "0000", reverse=True)[:60]
        for item in batch:
            seen.add(item["merx_id"])
            q.put(item)
            queued += 1
            if queued >= max_n:
                break
        q.join()
    for _ in threads:
        q.put(None)
    q.join()
    log(f"finished; queued {queued}; written {counter[0]}")


if __name__ == "__main__":
    main()
