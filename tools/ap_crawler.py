#!/usr/bin/env python3
"""No-AI crawler for buyers' invoicing / accounts-payable mailboxes. Built to run for days on the owner's Mac.

For every buyer in the research queues that has a known website (largest buyers first) it reads the buyer's own site
the way a visitor would: robots.txt respected, at most one request per second per site, a page budget per site, and
only links about invoicing, accounts payable, suppliers, purchasing, finance or contact. Role mailboxes for invoicing,
AP, supplier payment or purchasing found on those pages (HTML and PDF) are saved as buyer_ap rows with the page URL
and a quote, and pushed to GitHub, where the referee re-opens every page before anything enters the dataset.
No AI, no search engine. Blocked sites (401/403/429, CAPTCHA, bot checks) are skipped, never worked around.
Protected (obfuscated) e-mails are never decoded. Named people's mailboxes are dropped (same rule as the referee).

Run it in its own clone:  python3 tools/ap_crawler.py [--days 7] [--workers 8] [--limit N] [--max-seconds S]
State and log: ~/cch-crawler-state/.  Output: data/incoming/claude/claude_buyer_ap_results_crawl01.csv
Pass 1 reads up to 25 pages per site; pass 2 re-reads sites with nothing found, up to 60 pages. Then it checks for new
queue batches every 6 hours until --days is over.
"""
import argparse, csv, datetime, glob, heapq, html, io, json, os, re, shutil, subprocess, sys, threading, time
import urllib.error, urllib.parse, urllib.request, urllib.robotparser
from concurrent.futures import ThreadPoolExecutor

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from validate_returns import EMAIL, PERSONAL, ROLE_HINT  # same mailbox rules as the referee

STATE = os.path.expanduser("~/cch-crawler-state")
OUT = "data/incoming/claude/claude_buyer_ap_results_crawl01.csv"
UA = "canada-contracts-hub-crawler/1.0 (+https://github.com/mohamedbiranesy-gif/canada-contracts-hub)"
COLS = ["task_id", "buyer_key", "org_name_as_found", "ap_email", "ap_email_type", "invoice_portal_url", "ap_phone",
        "invoice_mailing_address", "invoicing_requirements_summary", "applies_to", "evidence_url", "evidence_quote",
        "retrieved_date", "status", "queries_tried", "notes"]
LINK_KW = [(re.compile(r"factur|invoice|payable|comptes?[-_ ]?(a|à)[-_ ]?payer|accounts?[-_ ]?pay|e-?invoic", re.I), 10),
           (re.compile(r"fournisseur|supplier|vendor|approvisionnement|purchas|procure|achats?\b|faire[-_ ]affaire|"
                       r"doing[-_ ]business|business[-_ ]with|appels?[-_ ]d|tender|bid", re.I), 6),
           (re.compile(r"financ|tr[ée]sor|treasur|comptab|accounting|paiement|payment", re.I), 5),
           (re.compile(r"nous[-_ ]joindre|contact|coordonn|directory|bottin|annuaire|services", re.I), 2)]
SKIP_EXT = re.compile(r"\.(jpe?g|png|gif|svg|webp|ico|mp4|mov|mp3|zip|docx?|xlsx?|pptx?|ics|css|js|xml|rss)(\?|$)", re.I)
EMAIL_RX = re.compile(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9-]+(?:\.[A-Za-z0-9-]+)*\.[A-Za-z]{2,}")
AP_LOCAL = re.compile(r"factur|invoice|bill|payable|compt|account|^ap$|^ap[._-]|[._-]ap$|[._-]cap$|financ|fourniss|"
                      r"supplier|vendor|approv|achat|purchas|procure|paiement|payment|tresor|treasur|acquisition", re.I)
NOT_AP = re.compile(r"plainte|complaint|recevable|receivable|patient|usager|emploi|career|job|media|presse|press|"
                    r"benevol|volunteer|fondation|foundation|donat|webmaster|privacy|confidential|rh[._-]|^rh$|hr[._-]|^hr$", re.I)
CONTEXT_AP = re.compile(r"factur|invoice|payable|comptes? (à|a) payer|paiement|payment|fournisseur|supplier|vendor", re.I)
BLOCK_RX = re.compile(r"captcha|cf-challenge|challenge-platform|attention required|access denied|are you a robot", re.I)
RANK = {"invoice_submission": 0, "accounts_payable": 1, "supplier_payment": 2, "procurement": 3, "general": 4}
GENERAL = re.compile(r"^(info|contact|contactus|reception|admin|administration|general|greffe|mairie|municipalite|townhall|cityhall|clerk|office|bureau|secretariat|accueil|hello|inquiries|enquiries|renseignements)([._-]|$)", re.I)
TODAY = datetime.date.today().isoformat()

host_lock, host_next, robots = threading.Lock(), {}, {}
out_lock, state_lock = threading.Lock(), threading.Lock()
stats = {"sites": 0, "pages": 0, "found_sites": 0, "rows": 0, "blocked": 0}


def log(*a):
    print(time.strftime("%Y-%m-%d %H:%M:%S"), *a, flush=True)


def fetch(url, limit=6_000_000):
    """(status, content_type, bytes, final_url); one request per second per host across all threads."""
    host = urllib.parse.urlparse(url).hostname or ""
    while True:
        with host_lock:
            wait = host_next.get(host, 0) - time.time()
            if wait <= 0:
                host_next[host] = time.time() + 1.0
                break
        time.sleep(min(wait, 1.0))
    req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept-Language": "fr-CA,fr;q=0.9,en;q=0.8"})
    try:
        with urllib.request.urlopen(req, timeout=20) as r:
            return r.status, r.headers.get("content-type", ""), r.read(limit), r.geturl()
    except urllib.error.HTTPError as e:
        return e.code, "", b"", url
    except Exception:
        return 0, "", b"", url


def allowed(url):
    p = urllib.parse.urlparse(url)
    key = "%s://%s" % (p.scheme, p.netloc)
    if key not in robots:
        rp = urllib.robotparser.RobotFileParser()
        status, _, data, _ = fetch(key + "/robots.txt", 500_000)
        if status in (401, 403):
            rp.disallow_all = True
        elif status == 200:
            rp.parse(data.decode("utf-8", "replace").splitlines())
        else:
            rp.allow_all = True
        robots[key] = rp
    return robots[key].can_fetch(UA, url)


def pdf_text(data):
    if shutil.which("pdftotext"):
        try:
            r = subprocess.run(["pdftotext", "-layout", "-", "-"], input=data, capture_output=True, timeout=60)
            if r.stdout.strip():
                return r.stdout.decode("utf-8", "replace")
        except Exception:
            pass
    try:
        import pypdf
        return "\n".join((pg.extract_text() or "") for pg in pypdf.PdfReader(io.BytesIO(data)).pages[:40])
    except Exception:
        return ""


def visible(raw):
    t = re.sub(r"(?is)<(script|style|noscript)[^>]*>.*?</\1>", " ", raw)
    t = re.sub(r"(?s)<[^>]+>", " ", t)
    return re.sub(r"\s+", " ", t)


def quote_for(email, text, raw):
    for src in (text, re.sub(r"\s+", " ", raw)):
        i = src.lower().find(email)
        if i >= 0:
            a = max(0, i - 140)
            q = src[a:a + 290]
            j = q.lower().find(email)
            for m in EMAIL_RX.finditer(q):  # keep other people's addresses out of the quote
                if m.group(0).lower() != email:
                    if m.start() > j:
                        q = q[:m.start()]
                        break
                    q, j = q[m.end():], j - m.end()
            q = q.strip()
            if email in q.lower():
                return q
    return ""


def classify(email, context, general=False):
    local = email.split("@")[0]
    if NOT_AP.search(local):
        return None
    if not AP_LOCAL.search(local):  # owner rule (2026-10-28): a general role mailbox only when no AP/procurement one
        return "general" if general and GENERAL.search(local) and EMAIL.match(email) else None
    if not EMAIL.match(email) or (PERSONAL.match(local) and not ROLE_HINT.search(local)):
        return None
    if re.search(r"factur|invoice|bill", local, re.I):
        return "invoice_submission"
    if re.search(r"payable|compt.*pay|^ap$|^ap[._-]|[._-]ap$|[._-]cap$", local, re.I):
        return "accounts_payable"
    if re.search(r"paiement|payment", local, re.I):
        return "supplier_payment"
    if re.search(r"fourniss|supplier|vendor|approv|achat|purchas|procure|acquisition", local, re.I):
        return "procurement"
    if CONTEXT_AP.search(context):  # finance@, comptabilite@, tresorerie@ ... only when the page talks about invoicing
        return "accounts_payable"
    return None


def links(raw, base):
    for m in re.finditer(r"(?is)<a\s[^>]*?href\s*=\s*[\"']([^\"'#>]+)[\"'][^>]*>(.*?)</a>", raw[:2_000_000]):
        href, label = m.group(1).strip(), visible(m.group(2))[:120]
        if href.lower().startswith(("mailto:", "tel:", "javascript:")):
            continue
        yield urllib.parse.urljoin(base, href), label


def crawl(task, max_pages, general=False):
    start = task["known_website"].strip()
    if not start.startswith("http"):
        start = "https://" + start
    host0 = (urllib.parse.urlparse(start).hostname or "").lower()
    if not host0:
        return "no_website", 0, []
    base = host0[4:] if host0.startswith("www.") else host0
    same = lambda h: bool(h) and (h.lower() == base or h.lower().endswith("." + base))
    heap, seen, pages, found = [(-100, 0, start), (-90, 0, "https://%s/" % host0)], set(), 0, {}
    while heap and pages < max_pages:
        neg, depth, url = heapq.heappop(heap)
        url = url.split("#")[0]
        if url in seen:
            continue
        seen.add(url)
        if not allowed(url):
            continue
        status, ctype, data, final = fetch(url)
        pages += 1
        stats["pages"] += 1
        head = data[:20000].decode("utf-8", "replace")
        if status in (401, 403, 429) or (status == 503 and BLOCK_RX.search(head)) or (pages <= 2 and BLOCK_RX.search(head) and len(data) < 30000):
            if pages <= 2:
                return "blocked", pages, []
            continue
        if status != 200 or not data:
            continue
        is_pdf = "pdf" in ctype.lower() or data[:5] == b"%PDF-"
        raw = pdf_text(data) if is_pdf else html.unescape(data.decode("utf-8", "replace"))
        text = re.sub(r"\s+", " ", raw) if is_pdf else visible(raw)
        for e in set(x.lower().rstrip(".") for x in EMAIL_RX.findall(raw)):
            if e.split(".")[-1] in ("png", "jpg", "jpeg", "gif", "svg", "webp") or e in found:
                continue
            q = quote_for(e, text, raw)
            i = text.lower().find(e)
            kind = classify(e, text[max(0, i - 400):i + 400] if i >= 0 else q, general)
            if kind and q:
                found[e] = (RANK[kind] * 100 + neg, kind, final, q)
        if is_pdf or depth >= 3:
            continue
        for link, label in links(raw, final):
            p = urllib.parse.urlparse(link)
            if p.scheme not in ("http", "https") or not same(p.hostname) or link in seen or SKIP_EXT.search(p.path):
                continue
            score = sum(w for rx, w in LINK_KW if rx.search(p.path + " " + p.query + " " + label))
            if p.path.lower().endswith(".pdf") and score < 5:
                continue
            if score > 0:
                heapq.heappush(heap, (-score * 10 + depth, depth + 1, link))
    best = sorted(found.items(), key=lambda kv: kv[1][0])[:3]
    rows = [{"task_id": task["task_id"], "buyer_key": task["buyer_key"], "org_name_as_found": task["buyer_name"],
             "ap_email": e, "ap_email_type": kind, "invoice_portal_url": "", "ap_phone": "", "invoice_mailing_address": "",
             "invoicing_requirements_summary": "", "applies_to": "whole_organisation", "evidence_url": url,
             "evidence_quote": q, "retrieved_date": TODAY, "status": "found",
             "queries_tried": "site crawl of %s (%d pages, robots.txt respected), no AI, no search engine" % (host0, pages),
             "notes": "found on the buyer's own site by tools/ap_crawler.py" + ("; general role mailbox: no invoicing, AP or purchasing mailbox found on the site" if kind == "general" else "")} for e, (_, kind, url, q) in best]
    return ("found" if rows else "nothing_found"), pages, rows


def load_tasks():
    tasks, sites = {}, {}
    p = os.path.join(STATE, "websites.tsv")  # written by tools/site_finder.py for buyers without a known website
    if os.path.exists(p):
        for line in open(p, encoding="utf-8"):
            k, _, url = line.rstrip("\n").partition("\t")
            sites[k] = url.split("\t")[0]
    for f in sorted(glob.glob("coord/tasks/*/*_buyer_ap_batch*.csv")):
        if "_verify_" in f:
            continue
        for r in csv.DictReader(open(f, encoding="utf-8-sig")):
            if not (r.get("known_website") or "").strip() and sites.get(r.get("buyer_key")):
                r["known_website"] = sites[r["buyer_key"]]
            if (r.get("known_website") or "").strip() and r.get("buyer_key") and r["buyer_key"] not in tasks:
                tasks[r["buyer_key"]] = r
    verified = set()
    if os.path.exists("coord/results/team_buyers.jsonl"):
        for line in open("coord/results/team_buyers.jsonl", encoding="utf-8"):
            o = json.loads(line)
            if (o.get("ap_contact_team") or {}).get("emails"):
                verified.add(o["buyer_key"])
    def size(r):
        try:
            return -int(float(r.get("contracts_in_dataset") or 0))
        except ValueError:
            return 0
    return sorted((t for k, t in tasks.items() if k not in verified), key=size)


def load_done():
    done = {}
    p = os.path.join(STATE, "done.tsv")
    if os.path.exists(p):
        for line in open(p, encoding="utf-8"):
            parts = line.rstrip("\n").split("\t")
            if len(parts) >= 3:
                done[parts[0]] = (int(parts[1]), parts[2])
    return done


def save(task, pass_no, result, pages, rows):
    with out_lock:
        new = not os.path.exists(OUT)
        os.makedirs(os.path.dirname(OUT), exist_ok=True)
        with open(OUT, "a", newline="", encoding="utf-8") as f:
            w = csv.DictWriter(f, fieldnames=COLS)
            if new:
                w.writeheader()
            w.writerows(rows)
        with open(os.path.join(STATE, "done.tsv"), "a", encoding="utf-8") as f:
            f.write("%s\t%d\t%s\t%d\t%s\n" % (task["buyer_key"], pass_no, result, pages, task["known_website"]))
        stats["sites"] += 1
        stats["rows"] += len(rows)
        stats["found_sites"] += bool(rows)
        stats["blocked"] += result == "blocked"


def git(*a):
    return subprocess.run(["git"] + list(a), capture_output=True, text=True, timeout=300)


def sync(final=False):
    """Commit new rows and push to main (rebased on the latest main); retried on the next cycle when it fails."""
    with out_lock:
        if not git("status", "--porcelain", "data/incoming/claude").stdout.strip():
            return
        git("add", "data/incoming/claude")
        git("commit", "-q", "-m", "[claude] ap_crawler: buyer invoicing contacts (%d sites read, %d rows so far)"
            % (stats["sites"], stats["rows"]))
    for attempt in range(3):
        git("pull", "-q", "--rebase", "origin", "main")
        if git("push", "-q", "origin", "HEAD:main").returncode == 0:
            log("pushed", stats)
            return
        time.sleep(20 * (attempt + 1))
    log("push failed, will retry", stats)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--days", type=float, default=7)
    ap.add_argument("--workers", type=int, default=8)
    ap.add_argument("--limit", type=int, default=0)
    ap.add_argument("--max-seconds", type=float, default=0)
    a = ap.parse_args()
    os.makedirs(STATE, exist_ok=True)
    os.chdir(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    deadline = time.time() + (a.max_seconds or a.days * 86400)
    stop = threading.Event()

    def syncer():
        while not stop.wait(900):
            sync()
    threading.Thread(target=syncer, daemon=True).start()
    log("start", {"days": a.days, "workers": a.workers, "pdf": bool(shutil.which("pdftotext")) or "pypdf"})
    while time.time() < deadline:
        git("pull", "-q", "--rebase", "origin", "main")
        tasks, done = load_tasks(), load_done()
        if a.limit:
            tasks = tasks[:a.limit]
        for pass_no, max_pages in ((1, 25), (2, 60), (3, 40)):
            todo = [t for t in tasks if (pass_no == 1 and t["buyer_key"] not in done) or
                    (pass_no > 1 and done.get(t["buyer_key"], (0, ""))[0] < pass_no and done.get(t["buyer_key"], (0, ""))[1] == "nothing_found")]
            log("pass %d: %d sites" % (pass_no, len(todo)))

            def one(t, pass_no=pass_no, max_pages=max_pages):
                if time.time() >= deadline:
                    return
                try:
                    result, pages, rows = crawl(t, max_pages, general=(pass_no == 3))
                except Exception as e:
                    result, pages, rows = "error:%s" % type(e).__name__, 0, []
                save(t, pass_no, result, pages, rows)
                done[t["buyer_key"]] = (pass_no, result)
                if stats["sites"] % 50 == 0:
                    log(stats)
            with ThreadPoolExecutor(a.workers) as ex:
                list(ex.map(one, todo))
            sync()
        if a.limit or a.max_seconds:
            break
        log("queue done; checking for new buyers in 1 hour", stats)
        stop.wait(min(3600, max(0, deadline - time.time())))
    stop.set()
    sync(final=True)
    log("finished", stats)


if __name__ == "__main__":
    main()
