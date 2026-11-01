#!/usr/bin/env python3
"""Find invoicing / AP mailboxes on deep pages of buyers' own sites, using the Wayback Machine URL index. No AI.

The site crawler (tools/ap_crawler.py) reads what a buyer's home page, links and sitemap lead to. Invoicing rules
often live deeper: a supplier-form PDF in /wp-content/uploads/, an "exigences de facturation" page linked from a
single tender, a purchase-order terms document. The Internet Archive's public URL index (CDX API) lists every URL it
has seen on a site, so for each buyer this script:
  1. asks the index for the site's URLs whose address mentions invoices, suppliers, accounts payable, finance,
     payments or purchasing (one request per buyer, at most one request every 3 seconds, backs off when asked);
  2. reads those pages and documents on the LIVE site (robots.txt respected, one request per second per site);
  3. keeps role mailboxes with the same rules as the crawler and the referee (invoicing / AP first, then the finance
     department, then purchasing; never a named person). The evidence URL is the live page, never the archive copy.

Targets: coord/tasks/claude/claude_deep_targets.csv (contract-proven buyers still missing an invoicing mailbox,
most valuable first). Output: data/incoming/claude/claude_buyer_ap_results_deep01.csv, committed with the crawler's
rows. Progress: ~/cch-crawler-state/deep_done.tsv (safe to stop and restart).
  python3 tools/deep_pages.py [--workers 16] [--limit N]
"""
import argparse, csv, json, os, queue, re, sys, threading, time, urllib.error, urllib.parse, urllib.request

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import ap_crawler as C

TARGETS = "coord/tasks/claude/claude_deep_targets.csv"
OUT = "data/incoming/claude/claude_buyer_ap_results_deep01.csv"
DONE = os.path.join(C.STATE, "deep_done.tsv")
CDX = "https://web.archive.org/cdx/search/cdx"
WORDS = (r"factur|invoic|payable|comptes|fournisseur|supplier|vendor|achat|approvisionnement|purchas|procure|"
         r"financ|comptab|accounting|paiement|payment|tresor|treasur|faire-affaire|doing-business|depot|deposit")
KEEP = {"invoice_submission", "accounts_payable", "supplier_payment", "finance", "procurement"}
SCORE = [(re.compile(r"factur|invoic|payable|comptes?[-_ ]?(a|à)?[-_ ]?payer|accounts?[-_ ]?pay", re.I), 10),
         (re.compile(r"fournisseur|supplier|vendor|depot|deposit|paiement|payment", re.I), 6),
         (re.compile(r"financ|comptab|accounting|tresor|treasur", re.I), 5),
         (re.compile(r"achat|approvisionnement|purchas|procure|faire-affaire|doing-business", re.I), 3)]
lock = threading.Lock()


def index_urls(host, tries=4):
    """Archived URLs of the site whose address mentions invoicing / suppliers / finance, best first."""
    q = urllib.parse.urlencode([("url", host), ("matchType", "domain"), ("output", "json"), ("from", "2020"),
                                ("fl", "original,timestamp"), ("filter", "statuscode:200"),
                                ("filter", "original:(?i).*(%s).*" % WORDS), ("collapse", "urlkey"), ("limit", "3000")])
    for i in range(tries):
        time.sleep(3)
        try:
            req = urllib.request.Request(CDX + "?" + q, headers={"User-Agent": C.UA})
            with urllib.request.urlopen(req, timeout=90) as r:
                data = json.loads(r.read(20_000_000).decode("utf-8", "replace") or "[]")
            break
        except urllib.error.HTTPError as e:
            if e.code in (429, 503, 504):
                time.sleep(60 * (i + 1))
                continue
            return []
        except Exception:
            time.sleep(10 * (i + 1))
    else:
        return None  # index unavailable: try this buyer again on the next run
    best = {}
    for row in data[1:]:
        url, ts = row[0], row[1]
        p = urllib.parse.urlparse(url)
        if C.SKIP_EXT.search(p.path) or re.search(r"\.(css|js|jpe?g|png|gif)$", p.path, re.I):
            continue
        path = (p.hostname or "").lower().removeprefix("www.") + p.path.rstrip("/").lower()
        s = sum(w for rx, w in SCORE if rx.search(urllib.parse.unquote(p.path + " " + p.query)))
        if s and (path not in best or ts > best[path][1]):
            best[path] = (s, ts, url.replace("http://", "https://", 1) if url.startswith("http://") else url)
    return [u for s, ts, u in sorted(best.values(), key=lambda x: (-x[0], x[1] < "2023", -int(x[1][:8] or 0)))]


def read(task, urls, max_pages=15):
    found = {}
    for url in urls[:max_pages]:
        if not C.allowed(url):
            continue
        status, ctype, data, final = C.fetch(url)
        if status != 200 or not data or C.BLOCK_RX.search(data[:20000].decode("utf-8", "replace")) and len(data) < 30000:
            continue
        is_pdf = "pdf" in ctype.lower() or data[:5] == b"%PDF-"
        is_office = data[:2] == b"PK" and (C.OFFICE.search(url) or "officedocument" in ctype.lower())
        raw = C.pdf_text(data) if is_pdf else C.office_text(data) if is_office else C.html.unescape(data.decode("utf-8", "replace"))
        text = re.sub(r"\s+", " ", raw) if (is_pdf or is_office) else C.visible(raw)
        for e in set(x.lower().rstrip(".") for x in C.EMAIL_RX.findall(raw)):
            if e in found or e.split(".")[-1] in ("png", "jpg", "jpeg", "gif", "svg", "webp"):
                continue
            q = C.quote_for(e, text, raw)
            i = text.lower().find(e)
            kind = C.classify(e, text[max(0, i - 400):i + 400] if i >= 0 else q)
            if kind in KEEP and q:
                found[e] = (C.RANK[kind], kind, final, q)
    best = sorted(found.items(), key=lambda kv: kv[1][0])[:3]
    host = urllib.parse.urlparse(task["website"]).hostname or ""
    return [{"task_id": task["task_id"], "buyer_key": task["buyer_key"], "org_name_as_found": task["buyer_name"],
             "ap_email": e, "ap_email_type": "general" if kind == "finance" else kind, "invoice_portal_url": "", "ap_phone": "",
             "invoice_mailing_address": "", "invoicing_requirements_summary": "", "applies_to": "whole_organisation",
             "evidence_url": url, "evidence_quote": q, "retrieved_date": C.TODAY, "status": "found",
             "queries_tried": "Wayback Machine URL index of %s (addresses about invoices / suppliers / finance), then %d live pages read "
                              "(robots.txt respected), no AI, no search engine" % (host, min(len(urls), max_pages)),
             "notes": "found on the buyer's own site by tools/deep_pages.py" + (
                 "; finance / accounting department mailbox: no invoicing or AP mailbox found" if kind == "finance" else
                 "; purchasing mailbox: no invoicing or AP mailbox found" if kind == "procurement" else "")}
            for e, (_, kind, url, q) in best]


def save(task, n, rows):
    with lock:
        new = not os.path.exists(OUT)
        with open(OUT, "a", newline="", encoding="utf-8") as f:
            w = csv.DictWriter(f, fieldnames=C.COLS)
            if new:
                w.writeheader()
            w.writerows(rows)
        with open(DONE, "a", encoding="utf-8") as f:
            f.write("%s\t%d\t%s\n" % (task["buyer_key"], n, rows[0]["ap_email_type"] if rows else "nothing_found"))


def main():
    a = argparse.ArgumentParser()
    a.add_argument("--workers", type=int, default=16)
    a.add_argument("--limit", type=int, default=0)
    a.add_argument("--index", type=int, default=2, help="URL-index lookups at a time")
    a = a.parse_args()
    os.chdir(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    os.makedirs(C.STATE, exist_ok=True)
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    done = set(l.split("\t")[0] for l in open(DONE, encoding="utf-8")) if os.path.exists(DONE) else set()
    tasks = [dict(r, task_id="CL-DP-%05d" % i) for i, r in enumerate(csv.DictReader(open(TARGETS, encoding="utf-8-sig")), 1)
             if r["buyer_key"] not in done and r["website"].startswith("http")]
    if a.limit:
        tasks = tasks[:a.limit]
    C.log("deep_pages: %d buyers to look up" % len(tasks))
    work, stats = queue.Queue(maxsize=a.workers * 2), {"buyers": 0, "with_urls": 0, "found": 0, "rows": 0}

    def reader():
        while True:
            item = work.get()
            if item is None:
                return
            task, urls = item
            try:
                rows = read(task, urls)
            except Exception:
                rows = []
            save(task, len(urls), rows)
            with lock:
                stats["found"] += bool(rows)
                stats["rows"] += len(rows)
    threads = [threading.Thread(target=reader, daemon=True) for _ in range(a.workers)]
    for t in threads:
        t.start()
    todo = queue.Queue()
    for task in tasks:
        todo.put(task)

    def indexer():  # at most --index lookups at a time (polite); the live sites are read in parallel
        while True:
            try:
                task = todo.get_nowait()
            except queue.Empty:
                return
            host = (urllib.parse.urlparse(task["website"]).hostname or "").lower().removeprefix("www.")
            urls = index_urls(host) if host else []
            if urls is None:
                continue
            with lock:
                stats["buyers"] += 1
                stats["with_urls"] += bool(urls)
                n = stats["buyers"]
            if urls:
                work.put((task, urls))
            else:
                save(task, 0, [])
            if n % 25 == 0:
                C.log("deep_pages", stats)
    idx = [threading.Thread(target=indexer, daemon=True) for _ in range(a.index)]
    for t in idx:
        t.start()
    for t in idx:
        t.join()
    for _ in threads:
        work.put(None)
    for t in threads:
        t.join()
    C.log("deep_pages finished", stats)


if __name__ == "__main__":
    main()
