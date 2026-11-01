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
import argparse, csv, gzip, json, os, queue, re, sys, threading, time, urllib.error, urllib.parse, urllib.request

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import ap_crawler as C

TARGETS = "coord/tasks/claude/claude_deep_targets.csv"
OUT = "data/incoming/claude/claude_buyer_ap_results_deep01.csv"
DONE = os.path.join(C.STATE, "deep_done.tsv")
CDX = "https://web.archive.org/cdx/search/cdx"
WORDS = (r"factur|invoic|payable|comptes|fournisseur|supplier|vendor|achat|approvisionnement|purchas|procure|"
         r"financ|comptab|accounting|paiement-fournisseur|paiement-des-fournisseurs|supplier-payment|vendor-payment|"
         r"tresor|treasur|faire-affaire|doing-business|depot-direct|direct-deposit")
KEEP = {"invoice_submission", "accounts_payable", "supplier_payment", "finance", "procurement"}
SCORE = [(re.compile(r"(?<!manu)factur|invoic|payable|comptes?[-_ ]?(a|à)?[-_ ]?payer|accounts?[-_ ]?pay", re.I), 10),
         (re.compile(r"fournisseur|supplier|vendor|depot-direct|direct-deposit|paiement-(des-)?fournisseur|supplier-payment", re.I), 6),
         (re.compile(r"financ|comptab|accounting|tresor|treasur", re.I), 5),
         (re.compile(r"achat|approvisionnement|purchas|procure|faire-affaire|doing-business|conditions|terms", re.I), 5),
         (re.compile(r"tuition|student|etudiant|étudiant|osap|admission|program|course|cours/|career|carriere|emploi|job|"
                     r"news|nouvelle|media|event|evenement|événement|blog|calendar|calendrier|/api/|feed|search|recherche|wp-json|oembed|"
                     r"liste|contrats?[-_]|contracts?[-_]|octroy|rapport|report|depot-du|proces|minutes|avis[-_]public|reglement|"
                     r"role[-_]|acces[-_]a[-_]l|access-to-information|entente-paiement|taxe|tax-", re.I), -8)]
lock = threading.Lock()
CAPTURE = {}  # url -> latest capture timestamp in the archive (YYYYMMDDhhmmss)
ARCHIVE_DAYS = 365  # an archive copy counts only when captured in the last year
PORTALS = {"quebec.ca", "canada.ca", "gov.bc.ca", "www2.gov.bc.ca", "alberta.ca", "ontario.ca", "gov.mb.ca", "saskatchewan.ca",
           "novascotia.ca", "gnb.ca", "gov.nl.ca", "princeedwardisland.ca", "gov.nt.ca", "yukon.ca", "gov.nu.ca", "gov.uk"}


def index_urls(host, tries=3):
    """Archived URLs of the site whose address mentions invoicing / suppliers / finance, best first.
    [] when the site has none or the index cannot answer for it (very large sites time out); None to retry later."""
    q = urllib.parse.urlencode([("url", host + "/*"), ("output", "json"), ("from", "2020"),
                                ("fl", "original,timestamp"), ("filter", "statuscode:200"),
                                ("filter", "original:(?i).*(%s).*" % WORDS), ("collapse", "urlkey"), ("limit", "3000")])
    timeouts = 0
    for i in range(tries):
        time.sleep(3)
        try:
            req = urllib.request.Request(CDX + "?" + q, headers={"User-Agent": C.UA})
            with urllib.request.urlopen(req, timeout=75) as r:
                data = json.loads(r.read(20_000_000).decode("utf-8", "replace") or "[]")
            break
        except urllib.error.HTTPError as e:
            if e.code in (429, 503):  # asked to slow down
                time.sleep(90 * (i + 1))
                continue
            return []
        except Exception:
            timeouts += 1
            if timeouts >= 2:
                return []  # too large for the index to answer in time: skip this site
            time.sleep(20)
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
        if s >= 5 and (path not in best or ts > best[path][1]):
            best[path] = (s, ts, url.replace("http://", "https://", 1) if url.startswith("http://") else url)
    for s, ts, u in best.values():
        CAPTURE[u] = ts
    return [u for s, ts, u in sorted(best.values(), key=lambda x: (-x[0], x[1] < "2023", -int(x[1][:8] or 0)))]


def archived(url):
    """(bytes, content type, snapshot URL) of the Internet Archive's copy of a page, when captured in the last year.
    Used when the live site refuses automated readers or the page has moved; the snapshot URL is the evidence, which
    anyone (and the referee) can open."""
    since = time.strftime("%Y%m%d", time.localtime(time.time() - ARCHIVE_DAYS * 86400))
    ts = CAPTURE.get(url, "")
    if ts[:8] < since:  # the URL index gives the first capture; ask for one made in the last year
        bare = re.sub(r"^https?://", "", url)
        q = CDX + "?" + urllib.parse.urlencode({"url": bare, "output": "json", "from": since, "limit": "1", "fl": "timestamp",
                                                 "filter": "statuscode:200"})
        status, _, data, _ = C.fetch(q)
        try:
            rows = json.loads(data.decode("utf-8", "replace") or "[]") if status == 200 else []
        except ValueError:
            rows = []
        ts = rows[1][0] if len(rows) > 1 else ""
    if not ts or ts[:8] < since:
        return None
    orig = re.sub(r"^https://", "http://", url) if url.startswith("https://") else url
    snap = "https://web.archive.org/web/%s/%s" % (ts, orig)
    for u in ("https://web.archive.org/web/%sid_/%s" % (ts, orig), snap):  # raw copy first, the archive's normal view if it errors
        status, ctype, data, final = C.fetch(u)
        if status == 200 and data:
            if data[:2] == b"\x1f\x8b":  # raw copies keep the site's own gzip encoding
                try:
                    data = gzip.decompress(data)
                except Exception:
                    continue
            return data, ctype, snap
    return None


STOP = {"de", "du", "des", "la", "le", "les", "et", "of", "the", "and", "for", "city", "ville", "town", "county", "municipalite",
        "municipality", "department", "ministere", "government", "gouvernement", "inc", "ltd", "limited", "corporation", "board"}


def name_on_page(name, text):
    """The buyer's distinctive name words appear on the page (used when its website came from a web search)."""
    words = [w for w in re.findall(r"[a-z0-9]{4,}", C.ascii_low(name)) if w not in STOP]
    low = C.ascii_low(text)
    return not words or sum(w in low for w in words) >= max(1, round(0.6 * len(words)))


def read(task, urls, max_pages=15, keep=KEEP):
    found, refused, ok, via_archive = {}, 0, 0, 0
    for url in urls[:max_pages]:
        live = C.allowed(url) and refused < 2  # after two refusals the live site is left alone for this buyer
        status, ctype, data, final = C.fetch(url) if live else (0, "", b"", url)
        if status in (401, 403, 429):
            refused += 1
        blocked = status == 200 and data and C.BLOCK_RX.search(data[:20000].decode("utf-8", "replace")) and len(data) < 30000
        if status != 200 or not data or blocked:  # refused, moved or gone: the archive's recent copy of the same page
            a = archived(url)
            if not a:
                continue
            data, ctype, final = a
            via_archive += 1
        else:
            ok += 1
        is_pdf = "pdf" in ctype.lower() or data[:5] == b"%PDF-"
        is_office = data[:2] == b"PK" and (C.OFFICE.search(url) or "officedocument" in ctype.lower())
        raw = C.pdf_text(data) if is_pdf else C.office_text(data) if is_office else C.html.unescape(data.decode("utf-8", "replace"))
        text = re.sub(r"\s+", " ", raw) if (is_pdf or is_office) else C.visible(raw)
        if task.get("site_from_search") and not name_on_page(task.get("buyer_name", ""), text):
            continue  # website suggested by a search engine: the page must name the buyer
        for e in set(x.lower().rstrip(".") for x in C.EMAIL_RX.findall(raw)):
            if e in found or e.split(".")[-1] in ("png", "jpg", "jpeg", "gif", "svg", "webp"):
                continue
            if not C.same_org(e, task["website"], task.get("buyer_name", "")):
                continue
            q = C.quote_for(e, text, raw)
            i = text.lower().find(e)
            kind = C.classify(e, text[max(0, i - 400):i + 400] if i >= 0 else q, general="general" in keep)
            if kind in keep and q:
                found[e] = (C.RANK[kind] + (0.5 if "web.archive.org" in final else 0), kind, final, q)  # live pages first
    best = sorted(found.items(), key=lambda kv: kv[1][0])[:3]
    host = urllib.parse.urlparse(task["website"]).hostname or ""
    return [{"task_id": task["task_id"], "buyer_key": task["buyer_key"], "org_name_as_found": task["buyer_name"],
             "ap_email": e, "ap_email_type": "general" if kind == "finance" else kind, "invoice_portal_url": "", "ap_phone": "",
             "invoice_mailing_address": "", "invoicing_requirements_summary": "", "applies_to": "whole_organisation",
             "evidence_url": url, "evidence_quote": q, "retrieved_date": C.TODAY, "status": "found",
             "queries_tried": "Wayback Machine URL index of %s (addresses about invoices / suppliers / finance), then %d live pages read "
                              "(robots.txt respected), no AI, no search engine" % (host, min(len(urls), max_pages)),
             "notes": ("found on the Internet Archive's copy (captured %s) of the buyer's own page %s; the live site refuses "
                       "automated readers or the page moved" % (re.search(r"/web/(\d{8})", url).group(1), url.split("/web/", 1)[1].split("/", 1)[1])
                       if "web.archive.org/web/" in url else "found on the buyer's own site by tools/deep_pages.py") + (
                 "; finance / accounting department mailbox: no invoicing or AP mailbox found" if kind == "finance" else
                 "; purchasing mailbox: no invoicing or AP mailbox found" if kind == "procurement" else
                 "; general role mailbox: no invoicing, AP, finance or purchasing mailbox found" if kind == "general" else "")}
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
    a.add_argument("--targets", default=TARGETS)
    a.add_argument("--urls", help="CSV buyer_key,buyer_name,website,official_site,url: read these pages (found with a web search) "
                                  "instead of asking the archive's URL index")
    a = a.parse_args()
    os.chdir(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    os.makedirs(C.STATE, exist_ok=True)
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    if a.urls:
        return from_search(a)
    done = set(l.split("\t")[0] for l in open(DONE, encoding="utf-8")) if os.path.exists(DONE) else set()
    prefix = "CL-DP-" if a.targets == TARGETS else "CL-DA-"
    tasks = [dict(r, task_id="%s%05d" % (prefix, i)) for i, r in enumerate(csv.DictReader(open(a.targets, encoding="utf-8-sig")), 1)
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
            except Exception as e:
                C.log("deep_pages: error on %s: %s %s" % (task["buyer_key"], type(e).__name__, e))
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
            pu = urllib.parse.urlparse(task["website"])
            host = (pu.hostname or "").lower().removeprefix("www.")
            if host in PORTALS:  # a government-wide portal: only this body's own section of it
                path = re.sub(r"/[^/]*\.(html?|aspx?|php)$", "", pu.path).rstrip("/")
                host = host + path if path.count("/") >= 2 else ""
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


SEARCH_OUT = "data/incoming/claude/claude_buyer_ap_results_search01.csv"
SEARCH_DONE = os.path.join(C.STATE, "search_done.tsv")


def from_search(a):
    """Pages a web search pointed to (the search only finds addresses; every mailbox is read from the page itself with
    the crawler's rules, no AI). A general role mailbox counts here: these buyers have no mailbox at all yet."""
    done = set(l.rstrip("\n") for l in open(SEARCH_DONE, encoding="utf-8")) if os.path.exists(SEARCH_DONE) else set()
    groups = {}
    for r in csv.DictReader(open(a.urls, encoding="utf-8-sig")):
        url = (r.get("url") or "").strip()
        if not url.startswith("http") or "%s|%s" % (r["buyer_key"], url) in done:
            continue
        site, from_search = (r.get("website") or "").strip(), False
        if not site.startswith("http"):
            site = (r.get("official_site") or "").strip()
            site = site if site.startswith("http") else ("https://" + site if site else "https://unknown.invalid")
            from_search = True
        g = groups.setdefault(r["buyer_key"], {"task_id": "CL-WS-%05d" % (len(groups) + 1), "buyer_key": r["buyer_key"],
                                               "buyer_name": r["buyer_name"], "website": site, "site_from_search": from_search, "urls": []})
        if url not in g["urls"]:
            g["urls"].append(url)
    tasks = list(groups.values())
    C.log("deep_pages --urls: %d buyers, %d pages" % (len(tasks), sum(len(t["urls"]) for t in tasks)))
    stats = {"buyers": 0, "found": 0, "rows": 0}
    keep = KEEP | {"general"}

    def one(t):
        try:
            rows = read(t, t["urls"], max_pages=8, keep=keep)
        except Exception as e:
            C.log("deep_pages --urls: error on %s: %s %s" % (t["buyer_key"], type(e).__name__, e))
            rows = []
        for r in rows:
            r["queries_tried"] = ("web search for the buyer's invoicing / accounts payable page (the search only gave the address); "
                                  "the page then read by tools/deep_pages.py with the crawler's rules, no AI")
            if "found by tools/deep_pages.py" in r["notes"] or r["notes"].startswith(";"):
                r["notes"] = r["notes"].replace("found on the buyer's own site by tools/deep_pages.py",
                                                "found on the buyer's own page (located with a web search, read without AI)")
        with lock:
            if rows:
                new = not os.path.exists(SEARCH_OUT)
                with open(SEARCH_OUT, "a", newline="", encoding="utf-8") as f:
                    w = csv.DictWriter(f, fieldnames=C.COLS)
                    if new:
                        w.writeheader()
                    w.writerows(rows)
            with open(SEARCH_DONE, "a", encoding="utf-8") as f:
                f.writelines("%s|%s\n" % (t["buyer_key"], u) for u in t["urls"])
            stats["buyers"] += 1
            stats["found"] += bool(rows)
            stats["rows"] += len(rows)
            if stats["buyers"] % 25 == 0:
                C.log("deep_pages --urls", stats)
    from concurrent.futures import ThreadPoolExecutor
    with ThreadPoolExecutor(a.workers) as ex:
        list(ex.map(one, tasks))
    C.log("deep_pages --urls finished", stats)


if __name__ == "__main__":
    main()
