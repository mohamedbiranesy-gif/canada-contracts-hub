#!/usr/bin/env python3
"""Fetch bids&tenders Tender/Detail pages for awarded bids listed in listing.jsonl and
extract everything the public page publishes:
  * the Bid Details table (all label/value rows)
  * every Ext.NET PagingMemoryProxy store on the page (Awarded, Submitted, PlanTakers,
    Advertisements, Documents, Addendums, PurchasingReps, Meetings ...) as JSON
Writes one JSON line per tender to <outdir>/details.jsonl (resumable: tenders already
present are skipped). Reads the listing progressively (listing.jsonl may still be growing).
Usage: python3 -I crawl_details.py <outdir> [max_details] [workers]
"""
import sys, os, re, json, time, html, datetime, threading, queue
import requests

UA = "contracts-research/1.0"
outdir = sys.argv[1]
max_details = int(sys.argv[2]) if len(sys.argv) > 2 else 10**9
workers = int(sys.argv[3]) if len(sys.argv) > 3 else 3
GLOBAL_RATE = float(os.environ.get("BT_RATE", "3.0"))  # requests per second across all workers

listing_path = os.path.join(outdir, "listing.jsonl")
details_path = os.path.join(outdir, "details.jsonl")
log_path = os.path.join(outdir, "crawl_details.log")
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
    s = html.unescape(s).replace("\xa0", " ")
    s = re.sub(r"[ \t\r]+", " ", s)
    s = re.sub(r"\s*\n\s*", "\n", s)
    return s.strip()


TR_RE = re.compile(r"<tr>\s*<th[^>]*>(.*?)</th>\s*<td[^>]*>(.*?)</td>\s*</tr>", re.S)
STORE_RE = re.compile(r'proxyId:"([A-Za-z0-9_]+)"')
dec = json.JSONDecoder()


def extract_stores(h):
    stores = {}
    for m in re.finditer(r'new Ext\.data\.PagingMemoryProxy\(', h):
        start = m.end()
        # find the proxyId that precedes this proxy (nearest before)
        pre = h[max(0, m.start() - 4000):m.start()]
        ids = STORE_RE.findall(pre)
        name = ids[-1] if ids else f"store_{m.start()}"
        j = start
        while j < len(h) and h[j] in " \t\r\n":
            j += 1
        try:
            obj, end = dec.raw_decode(h[j:])
        except Exception as e:
            obj = {"_parse_error": str(e), "_snippet": h[j:j + 300]}
        if name in stores:
            name = f"{name}_{m.start()}"
        stores[name] = obj
    return stores


def parse_detail(h, url):
    rec = {"detail_url": url}
    # bid details table
    i = h.find("aria-label='Bid Details'")
    if i < 0:
        i = h.find('aria-label="Bid Details"')
    details = {}
    if i >= 0:
        j = h.find("</table>", i)
        seg = h[i:j]
        for m in TR_RE.finditer(seg):
            label = clean(m.group(1)).rstrip(":").strip()
            val_html = m.group(2)
            if label == "Description":
                details["Description_html"] = val_html.strip()
            if label == "Categories":
                cats = re.findall(r"<li[^>]*>(.*?)</li>", val_html, re.S)
                if cats:
                    details["Categories"] = [clean(c) for c in cats]
                    continue
            val = clean(val_html)
            if label in details and details[label] != val:
                k = 2
                while f"{label}_{k}" in details:
                    k += 1
                label = f"{label}_{k}"
            details[label] = val
    rec["bid_details"] = details
    # other visible headings/text outside table: title
    t = re.search(r"<title[^>]*>(.*?)</title>", h, re.S)
    rec["page_title"] = clean(t.group(1)) if t else None
    rec["stores"] = extract_stores(h)
    # login-only flags
    rec["restricted_sections"] = len(re.findall(r"only available to invited bidders and registered plan takers", h))
    org = re.search(r'<meta name="description" content="[^"]*with ([^"]+)\."', h)
    rec["portal_org_meta"] = html.unescape(org.group(1)) if org else None
    return rec


def load_done():
    done = set()
    if os.path.exists(details_path):
        with open(details_path) as f:
            for line in f:
                try:
                    done.add(json.loads(line)["tender_id"])
                except Exception:
                    pass
    return done


def worker(q, sess, counter):
    while True:
        item = q.get()
        if item is None:
            q.task_done()
            return
        url = item["detail_url"]
        rec = None
        for attempt in range(3):
            throttle()
            try:
                r = sess.get(url, timeout=60)
                if r.status_code == 200:
                    rec = parse_detail(r.text, url)
                    rec["http_status"] = 200
                    break
                elif r.status_code in (404, 410):
                    rec = {"detail_url": url, "http_status": r.status_code}
                    break
                else:
                    log(f"{url} HTTP {r.status_code} attempt {attempt}")
            except Exception as e:
                log(f"{url} error {e!r} attempt {attempt}")
            time.sleep(2 + 2 * attempt)
        if rec is None:
            rec = {"detail_url": url, "http_status": None, "failed": True}
        rec["tender_id"] = item.get("tender_id")
        rec["portal"] = item.get("portal")
        rec["listing"] = item
        rec["retrieved_at"] = datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
        with write_lock:
            with open(details_path, "a") as f:
                f.write(json.dumps(rec, ensure_ascii=False) + "\n")
            counter[0] += 1
            if counter[0] % 200 == 0:
                log(f"details written {counter[0]} (queue {q.qsize()})")
        q.task_done()


def main():
    done = load_done()
    log(f"start; already done {len(done)}; max {max_details}; workers {workers}")
    sess = requests.Session()
    sess.headers["User-Agent"] = UA
    q = queue.Queue(maxsize=200)
    counter = [0]
    threads = [threading.Thread(target=worker, args=(q, sess, counter), daemon=True) for _ in range(workers)]
    for t in threads:
        t.start()
    queued = 0
    pos = 0
    idle_rounds = 0
    seen = set(done)
    while queued < max_details:
        new = 0
        with open(listing_path) as f:
            f.seek(pos)
            while True:
                line = f.readline()
                if not line:
                    break
                if not line.endswith("\n"):
                    break  # partial line, re-read later
                pos = f.tell()
                try:
                    item = json.loads(line)
                except Exception:
                    continue
                tid = item.get("tender_id")
                if not tid or tid in seen or not item.get("detail_url"):
                    continue
                seen.add(tid)
                q.put(item)
                queued += 1
                new += 1
                if queued >= max_details:
                    break
        if new == 0:
            idle_rounds += 1
            # listing crawler finished?
            if os.path.exists(os.path.join(outdir, "crawl_listing.log")):
                with open(os.path.join(outdir, "crawl_listing.log")) as lf:
                    if "done" in lf.read().split("\n")[-2:][0] and idle_rounds > 3:
                        break
            if idle_rounds > 600:
                break
            time.sleep(5)
        else:
            idle_rounds = 0
    for _ in threads:
        q.put(None)
    q.join()
    log(f"finished; queued {queued}; written {counter[0]}")


if __name__ == "__main__":
    main()
