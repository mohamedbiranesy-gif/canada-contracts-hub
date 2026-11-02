#!/usr/bin/env python3
"""Invoicing / AP role mailboxes at web scale, from the Common Crawl archive. No AI, no search engine.

Source: Common Crawl crawl CC-MAIN-2026-43 (https://data.commoncrawl.org/). ~/cch-sources/ccindex/scan.py reads the
columnar URL index (cc-index-table, subset=warc) and keeps every page whose PATH is about accounts payable, vendors,
suppliers, invoices, procurement or purchasing: ~/cch-sources/ccindex/parts/CC-MAIN-2026-43_NNN.parquet (url,
url_host_name, dom, tld, mime, fetch_time, warc_filename, warc_record_offset, warc_record_length; 300 parts).
This tool reads those parts as they appear (resumable: ~/cch-sources/ccindex/mine_done_<crawl>.txt) and
  1. keeps, per organisation (registrable host), at most 4 pages, best first: accounts-payable / invoice-submission
     paths, then supplier-information paths, then procurement / purchasing pages, then bare /suppliers or /vendors
     pages; blog, plugin, product, directory and news paths are dropped (they are SaaS marketing, not the
     organisation's own payables page);
  2. fetches each page's archived WARC record with an HTTP Range request (offset..offset+length-1) from
     data.commoncrawl.org (<= 2 requests/second, AGENTS.md rule 9; back-off on 429/5xx; a CloudFront 403 "Request
     blocked" pauses every thread 15 minutes and the part is retried; 8 refusals in a row stop the run), gunzips it,
     keeps HTML (and PDF via pdftotext);
  3. extracts role mailboxes with tools/ap_crawler.py's own functions (EMAIL_RX, same_org with the page's host,
     classify, quote_for; persons dropped by the referee's PERSONAL rule) and keeps per organisation the best 3,
     ranked invoice_submission > accounts_payable > supplier_payment > finance > procurement > general; a
     general-only organisation is written only when it is a known buyer or shows a tech signature;
  4. detects the Canada-HQ vendor signatures of tools/tech_relationships.py (portal links/embeds, Shopify with
     Shopify.country CA/US, Coveo, Unbounce, Lightspeed; Jane only with 2+ practitioners; a page linking 3+ tenants
     of one vendor is a directory and skipped).
Outputs
  ~/cch-crawler/data/incoming/claude/claude_buyer_ap_results_ccmine01.csv  RETURN_FORMATS buyer_ap rows (master copy
      ~/cch-sources/ccindex/ccmine01_rows.csv; rows missing from the crawler file are re-added after every part, so a
      git reset by a committer never loses rows). evidence_url = the live page URL; retrieved_date = the crawl's
      fetch date; buyer_key = an existing buyer key when the host (or its registrable domain) is a known buyer
      website (claude_buyer_leads.csv website, coord/tasks/*/*_buyer_ap_batch*.csv known_website,
      ~/cch-crawler-state/websites.tsv), else 'lead:' + sha1('<registrable host>|<registrable host>')[:16].
  ~/cch-leads/socrata_tech_cc.jsonl   one tech_relationships lead line per (organisation, vendor), publisher = domain
      = registrable host (same lead key as the mailbox rows), record_date = the crawl's fetch date.
  ~/cch-sources/ccindex/mine_orgs_<crawl>.jsonl  one line per organisation read (for counts); --report prints them.
Usage: python3 cc_mine.py [--parts N] [--follow] [--workers 4] [--rate 2] | --report
Counts (test 2026-11-02, first 20 parts): 331,496 index rows -> 3,196 organisations / 4,424 pages selected; 810 pages
read before data.commoncrawl.org answered 403 'Request blocked' (16 in flight was too fast; now 2 requests/second);
143 organisations with a role mailbox, 15 with a procurement-grade one written, 0 AP-grade, 1 tech signature, 47
hosts of known buyers. 87 parts on disk: 1.35M index rows -> 15,637 organisations / 21,534 pages selected (300 parts:
~54k organisations / ~74k pages, ~10 h at 2 requests/second). Live counts: --report.
"""
import argparse, csv, datetime, glob, gzip, hashlib, html, http.client, io, json, os, re, sys, threading, time
from concurrent.futures import ThreadPoolExecutor

HERE = os.path.dirname(os.path.abspath(__file__))
for _d in (HERE, os.path.expanduser("~/cch-crawler/tools")):
    if _d not in sys.path:
        sys.path.append(_d)
import ap_crawler as AP          # noqa: E402  mailbox rules shared with the site crawler and the referee
import tech_relationships as TR  # noqa: E402  Canada-HQ vendor signatures

CRAWL = "CC-MAIN-2026-43"
CC = os.path.expanduser("~/cch-sources/ccindex")
CRAWLER = os.path.expanduser("~/cch-crawler")
OUT = os.path.join(CRAWLER, "data/incoming/claude/claude_buyer_ap_results_ccmine01.csv")
LEADS_OUT = os.path.expanduser("~/cch-leads/socrata_tech_cc.jsonl")
UA = AP.UA
COLS = AP.COLS
AP_GRADE = {"invoice_submission", "accounts_payable", "supplier_payment"}
NOTE = "located via Common Crawl %s index, mailbox on the organisation's own page"

T0 = re.compile(r"accounts?[-_]?payables?|(^|/)payables|comptes[-_]?(a|à|%c3%a0)?[-_]?payer|(vendor|supplier|fournisseur)s?[-_]?"
                r"(invoic|payment|paiement|factur)|(submit|submitting|send|sending|soumettre|envoi|envoyer)[-_]?(an?[-_]|your[-_]|des[-_]|"
                r"vos[-_]|une[-_])?(invoic|factur)|invoic(e|es|ing)[-_]?(submission|requirement|guideline|instruction|process|polic|inquir|"
                r"enquir|address|mailing)|(^|/)e-?invoic|factur(e|es|ation)[-_]?(fournisseur|electronique|%c3%a9lectronique)")
T1 = re.compile(r"(supplier|vendor|fournisseur)s?[-_/]*(info|information|portal|registration|register|onboard|resource|guide|faq|contact|"
                r"relation|center|centre|requirement|inquir|enquir|hub|management|services)|(doing|do)[-_]business[-_]with|"
                r"become[-_]a[-_](supplier|vendor)|faire[-_]affaire|(^|/)(invoic(e|es|ing)|factur(e|es|ation))/?$")
T2 = re.compile(r"(^|/)[a-z0-9-]{0,25}(procurement|purchasing)[a-z0-9-]{0,25}/?$")
T3 = re.compile(r"(^|/)(suppliers?|vendors?|fournisseurs?)/?$")
NOISE = re.compile(r"/(wp-content|plugins?|tags?|category|categories|blog|blogs|news|article|articles|post|posts|forum|forums|"
                   r"threads?|topics?|product|products|produit|produits|shop|store|boutique|collections?|items?|listings?|"
                   r"directory|directories|template|templates|wiki|questions?|answers?|docs|documentation|api|kb|knowledge|"
                   r"learn|academy|community|stories|press|events?|jobs?|careers?|profile|profiles|members?|users?|"
                   r"author|marketplace|catalog|catalogue|search|download|downloads|apps?|integrations?|reviews?)/|"
                   r"/20\d\d/|output_format=|(^|/)[^/]*(-[^/-]+){5,}/?$")
HTML_MIME = {"text/html", "application/xhtml+xml"}


def log(*a):
    print(time.strftime("%Y-%m-%d %H:%M:%S"), *a, flush=True)


def tier(url):
    p = re.sub(r"^https?://[^/]+", "", url).lower()
    path = p.split("?")[0]
    if NOISE.search(p) or len(path) > 120:
        return 9
    for n, rx in enumerate((T0, T1, T2, T3)):
        if rx.search(path):
            return n
    return 9


def org_of(host, dom):
    """Registrable host: the more specific of Common Crawl's public-suffix domain and ap_crawler.registrable
    (x.gov.bc.ca stays x.gov.bc.ca, city.ca.us stays city.ca.us, foo.blogspot.com stays separate)."""
    host = (host or "").lower().rstrip(".")
    reg = AP.registrable(host) if host else ""
    dom = (dom or "").lower()
    best = max((x for x in (dom, reg) if x and host.endswith(x)), key=lambda x: x.count("."), default=host)
    return best


def lead_key(org):
    return "lead:" + hashlib.sha1(("%s|%s" % (org, org)).encode()).hexdigest()[:16]


# ------------------------------------------------------------------------------------------------ known buyers
def load_known():
    by_host, names = {}, {}
    def add(url, key, name, tid):
        url = (url or "").strip()
        if not url or not key:
            return
        h = TR.nowww(TR.host_of(url if "//" in url else "https://" + url))
        if h:
            by_host.setdefault(h, {})
            by_host[h].setdefault(key, (name or "", tid or ""))
    tasks = {}
    for f in sorted(glob.glob(os.path.join(CRAWLER, "coord/tasks/*/*_buyer_ap_batch*.csv"))):
        if "_verify_" in f:
            continue
        try:
            for r in csv.DictReader(open(f, encoding="utf-8-sig", errors="replace")):
                k = r.get("buyer_key") or ""
                tasks.setdefault(k, r)
                add(r.get("known_website"), k, r.get("buyer_name"), r.get("task_id"))
        except Exception:
            continue
    p = os.path.join(CRAWLER, "data/incoming/claude/claude_buyer_leads.csv")
    if os.path.exists(p):
        for r in csv.DictReader(open(p, encoding="utf-8-sig", errors="replace")):
            add(r.get("website"), r.get("buyer_key"), r.get("buyer_name"), (tasks.get(r.get("buyer_key")) or {}).get("task_id"))
    p = os.path.expanduser("~/cch-crawler-state/websites.tsv")
    if os.path.exists(p):
        for line in open(p, encoding="utf-8", errors="replace"):
            k, _, url = line.rstrip("\n").partition("\t")
            t = tasks.get(k)
            if t:
                add(url.split("\t")[0], k, t.get("buyer_name"), t.get("task_id"))
    out = {}
    for h, ks in by_host.items():
        if len(ks) > 3 or TR.base_domain(h) in TR.SKIP_BASES or TR.base_domain(h) in TR.VENDOR_BASES:
            continue  # a shared platform host cannot be attributed to one buyer
        k = sorted(ks, key=lambda x: (not x.startswith("b:"), x))[0]
        out[h] = (k,) + ks[k]
    return out


def match_known(known, hosts, org):
    for h in hosts:
        m = known.get(TR.nowww(h))
        if m:
            return m
    return known.get(org)


# ------------------------------------------------------------------------------------------------ WARC fetch
_tl = threading.local()
_pause = {"until": 0.0, "delay": 2.0, "next": 0.0, "rate": 2.0}  # rate: AGENTS.md rule 9, <= 2 requests/second per host
_plock = threading.Lock()
stats_lock = threading.Lock()
S = {}


def bump(k, n=1):
    with stats_lock:
        S[k] = S.get(k, 0) + n


def throttle():
    with _plock:
        _pause["until"] = max(_pause["until"], time.time() + _pause["delay"])
        _pause["delay"] = min(_pause["delay"] * 2, 120)
    bump("throttled")


def get_record(fn, off, ln):
    for attempt in range(7):
        if time.time() < _pause.get("blocked", 0):  # refused a moment ago: fail fast, the whole part is retried later
            return None
        w = _pause["until"] - time.time()
        if w > 0:
            time.sleep(w)
        with _plock:  # global pacing: one request start every 1/rate seconds across all threads
            t = max(time.time(), _pause["next"])
            _pause["next"] = t + 1.0 / _pause["rate"]
        if t > time.time():
            time.sleep(t - time.time())
        conn = getattr(_tl, "conn", None)
        try:
            if conn is None:
                conn = _tl.conn = http.client.HTTPSConnection("data.commoncrawl.org", timeout=40)
            conn.request("GET", "/" + fn, headers={"Range": "bytes=%d-%d" % (off, off + ln - 1), "User-Agent": UA})
            r = conn.getresponse()
            data = r.read()
            if r.status in (200, 206):
                with _plock:
                    _pause["delay"] = max(2.0, _pause["delay"] * 0.9)
                return data
            if r.status == 403:  # CloudFront "Request blocked": stop every thread for 15 minutes, the part is retried later
                with _plock:
                    _pause["blocked"] = time.time() + 900
                bump("http_403")
                return None
            if r.status in (429, 500, 502, 503, 504):
                throttle()
                continue
            bump("http_%d" % r.status)
            return None
        except Exception:
            try:
                conn.close()
            except Exception:
                pass
            _tl.conn = None
            time.sleep(1 + attempt)
    bump("fetch_gave_up")
    return None


def parse_warc(data):
    """(http_headers_text, body_bytes) of a gzipped WARC response record."""
    rec = gzip.decompress(data)
    i = rec.find(b"\r\n\r\n")
    if i < 0 or b"WARC-Type: response" not in rec[:i]:
        return "", b""
    rest = rec[i + 4:]
    j = rest.find(b"\r\n\r\n")
    if j < 0:
        return "", b""
    return rest[:j].decode("latin-1", "replace"), rest[j + 4:]


def decode(body, headers):
    m = re.search(r"charset=[\"']?([A-Za-z0-9._-]+)", headers, re.I) or re.search(rb"<meta[^>]+charset=[\"']?([A-Za-z0-9._-]+)", body[:4000], re.I)
    cs = m.group(1) if m else "utf-8"
    cs = cs.decode("ascii", "ignore") if isinstance(cs, bytes) else cs
    try:
        return body.decode(cs, "replace")
    except LookupError:
        return body.decode("utf-8", "replace")


# ------------------------------------------------------------------------------------------------ one page
def read_page(item):
    """Fetch + extract one archived page. Returns dict(found={email: (score, kind, url, quote, date)}, hits, ok)."""
    url, host, org, mime, date, fn, off, ln, t, site, oname = item
    res = {"org": org, "url": url, "ok": False, "found": {}, "hits": {}, "ap": False}
    data = get_record(fn, int(off), int(ln))
    if not data:
        return res
    try:
        headers, body = parse_warc(data)
    except Exception:
        bump("bad_record")
        return res
    if not body:
        return res
    is_pdf = "pdf" in (mime or "") or body[:5] == b"%PDF-"
    if is_pdf:
        raw = AP.pdf_text(body)
        text = re.sub(r"\s+", " ", raw)
        page_html = ""
    else:
        page_html = decode(body[:3_000_000], headers)
        if AP.BLOCK_RX.search(page_html[:20000]) and len(page_html) < 30000:
            bump("challenge_pages")
            return res
        raw = re.sub(r"\\u00[0-9a-fA-F]{2}", " ", html.unescape(page_html))  # JSON escapes such as \u003e glued to an address
        text = AP.visible(raw)
    res["ok"] = True
    for e in set(x.lower().rstrip(".") for x in AP.EMAIL_RX.findall(raw)):
        if e.split(".")[-1] in ("png", "jpg", "jpeg", "gif", "svg", "webp") or not AP.same_org(e, site, oname):
            continue
        q = AP.quote_for(e, text, raw)
        i = text.lower().find(e)
        kind = AP.classify(e, text[max(0, i - 400):i + 400] if i >= 0 else q, True)
        if kind and q:
            sc = AP.RANK[kind] * 100 + t * 10
            if e not in res["found"] or sc < res["found"][e][0]:
                res["found"][e] = (sc, kind, url, q, date)
            res["ap"] = res["ap"] or kind in AP_GRADE
    if page_html and TR.base_domain(host) not in TR.VENDOR_BASES:
        b = page_html[:2_000_000]
        for u in TR.all_urls(b, url):
            for k, slug, purl in TR.portal_hits(u):
                res["hits"].setdefault(k, {}).setdefault(slug, (url, u[:300], purl, "link/embed on the organisation's page"))
        assets = " ".join(TR.SRC_RE.findall(b) + TR.LINKTAG_RE.findall(b) + TR.INLINE_RE.findall(b)[:40])
        for k, v in TR.VENDORS.items():
            if v["kind"] == "asset" and v.get("asset_re_c"):
                m = v["asset_re_c"].search(assets)
                if m:
                    kind = "asset loaded by the organisation's own page"
                    if k == "shopify":  # Shopify Inc. contracts only with US/Canada billing addresses
                        mc = re.search(r'Shopify\.country\s*=\s*"([A-Z]{2})"', b)
                        if not mc or mc.group(1) not in ("CA", "US"):
                            continue
                        kind += " (Shopify.country=%s)" % mc.group(1)
                    ctx = assets[max(0, m.start() - 60):m.end() + 60].replace("\n", " ")
                    res["hits"].setdefault(k, {}).setdefault("asset", (url, ctx.strip(), "", kind))
    return res


# ------------------------------------------------------------------------------------------------ outputs
out_lock = threading.Lock()


def append_csv(path, rows):
    if not rows:
        return
    new = not os.path.exists(path)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "a", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=COLS)
        if new:
            w.writeheader()
        w.writerows(rows)


def sync_out(master):
    """Re-add to the crawler's file every master row it does not have (a committer's reset may have dropped some)."""
    if not os.path.exists(master):
        return 0
    mine = list(csv.reader(open(master, encoding="utf-8", newline="")))
    have = set()
    if os.path.exists(OUT):
        have = {tuple(r) for r in csv.reader(open(OUT, encoding="utf-8-sig", errors="replace", newline=""))}
    miss = [r for r in mine[1:] if tuple(r) not in have]
    if miss or not os.path.exists(OUT):
        new = not os.path.exists(OUT)
        os.makedirs(os.path.dirname(OUT), exist_ok=True)
        with open(OUT, "a", newline="", encoding="utf-8") as f:
            w = csv.writer(f)
            if new:
                w.writerow(COLS)
            w.writerows(miss)
    return len(miss)


def finish_org(org, pages, results, known, seen_rows, seen_leads, leads_f, orgs_f, master):
    hosts = sorted({p[1] for p in pages})
    kb = match_known(known, hosts, org)
    found, hits, ok = {}, {}, 0
    for r in results:
        ok += r["ok"]
        for e, v in r["found"].items():
            if e not in found or v[0] < found[e][0]:
                found[e] = v
        for k, slugs in r["hits"].items():
            for s, v in slugs.items():
                hits.setdefault(k, {}).setdefault(s, v)
    tech = {}
    for k, slugs in hits.items():
        if len(slugs) > 2:  # a page linking 3+ tenants of one vendor is a directory, not the org's own service
            bump("directory_skipped")
            continue
        if k == "jane":
            slugs = {s: v for s, v in slugs.items() if TR.portal_info("jane", v[2])[0]}
            if not slugs:
                continue
        tech[k] = slugs
    date = max((p[4] for p in pages), default="")
    best = sorted(found.items(), key=lambda kv: kv[1][0])[:3]
    kinds = [v[1] for _, v in best]
    emit = bool(best) and (kinds[0] != "general" or kb is not None or bool(tech))
    key = kb[0] if kb else lead_key(org)
    name = (kb[1] or org) if kb else org
    tid = (kb[2] if kb and kb[2] else "CL-CC-" + hashlib.sha1(org.encode()).hexdigest()[:10])
    rows = []
    if emit:
        for e, (_, kind, url, q, d) in best:
            if (key, e) in seen_rows:
                continue
            seen_rows.add((key, e))
            note = NOTE % CRAWL
            if kind == "general":
                note += "; general role mailbox: no invoicing, AP or purchasing mailbox on the archived pages read"
            elif kind == "finance":
                note += "; finance / accounting department mailbox: no invoicing or AP mailbox on the archived pages read"
            rows.append({"task_id": tid, "buyer_key": key, "org_name_as_found": name, "ap_email": e,
                         "ap_email_type": "general" if kind == "finance" else kind, "invoice_portal_url": "", "ap_phone": "",
                         "invoice_mailing_address": "", "invoicing_requirements_summary": "", "applies_to": "whole_organisation",
                         "evidence_url": url, "evidence_quote": q, "retrieved_date": d, "status": "found",
                         "queries_tried": "Common Crawl %s URL index: %d archived pages of %s whose path is about accounts payable / "
                                          "suppliers / invoices / procurement, read from the WARC archive; no AI, no search engine"
                                          % (CRAWL, ok, org),
                         "notes": note})
    with out_lock:
        append_csv(master, rows)
        for k, slugs in tech.items():
            if (org, k) in seen_leads:
                continue
            seen_leads.add((org, k))
            slug, (page, sig, purl, kind) = sorted(slugs.items())[0]
            pd = next((p[4] for p in pages if p[0] == page), date)
            h0 = next((p[1] for p in pages if p[0] == page), hosts[0])
            website = "https://%s/" % (h0 if TR.nowww(h0) == org else org)
            row = {"buyer_key": lead_key(org), "buyer_key_known": kb[0] if kb else "", "org_name_as_found": org,
                   "source_list": "Common Crawl %s" % CRAWL, "signature": sig[:300], "signature_kind": kind, "page_seen": page,
                   "portal_url": purl, "portal_slug": slug if slug != "asset" else "",
                   "slug_matches_org": bool(slug != "asset" and any(t in slug.replace("-", "") for t in TR.name_tokens(org))),
                   "other_tenants_linked": len(slugs) - 1, "crawl_fetch_date": pd}
            rec = TR.lead(k, org, website, page, row)
            rec["domain"] = org
            rec["dataset_id"] = "tech:%s:%s" % (k, org)
            rec["row"]["observed_date"] = rec["row"]["record_date"] = pd
            leads_f.write(json.dumps(rec, ensure_ascii=False) + "\n")
        leads_f.flush()
        orgs_f.write(json.dumps({"org": org, "hosts": hosts[:5], "pages": len(pages), "ok": ok,
                                 "ap_pages": sum(r["ap"] for r in results), "best": kinds, "known": kb[0] if kb else "",
                                 "tech": sorted(tech), "emitted": len(rows)}) + "\n")
        orgs_f.flush()


# ------------------------------------------------------------------------------------------------ parts
def finished_parts():
    dl = os.path.join(CC, "done_%s.txt" % CRAWL)
    n = len(open(dl).read().split()) if os.path.exists(dl) else 0
    return [(i, p) for i in range(n) for p in [os.path.join(CC, "parts", "%s_%03d.parquet" % (CRAWL, i))] if os.path.exists(p)]


def scan_finished():
    lg = os.path.join(CC, "scan.log")
    return os.path.exists(lg) and "finished" in open(lg).read()[-2000:]


def load_part(con, path):
    rows = con.execute("select url, url_host_name, dom, mime, cast(fetch_time as varchar), warc_filename, warc_record_offset, "
                       "warc_record_length from read_parquet(?) where mime in ('text/html','application/xhtml+xml','application/pdf')",
                       [path]).fetchall()
    groups = {}
    for url, host, dom, mime, ft, fn, off, ln in rows:
        t = tier(url)
        if t > 3 or (mime == "application/pdf" and t > 1):
            continue
        org = org_of(host, dom)
        groups.setdefault(org, []).append((t, "?" in url, len(url), url, host, mime, (ft or "")[:10], fn, off, ln))
    return len(rows), groups


def run(a):
    import duckdb
    con = duckdb.connect()
    con.execute("SET threads=2")
    known = load_known()
    log("known buyer hosts: %d" % len(known))
    master = os.path.join(CC, "ccmine01_rows.csv")
    seen_rows = set()
    if os.path.exists(master):
        for r in csv.DictReader(open(master, encoding="utf-8")):
            seen_rows.add((r["buyer_key"], r["ap_email"]))
    seen_leads = set()
    if os.path.exists(LEADS_OUT):
        for line in open(LEADS_OUT, encoding="utf-8"):
            try:
                o = json.loads(line)
                seen_leads.add((o["domain"], o["row"]["vendor_key"]))
            except (ValueError, KeyError):
                pass
    donef = os.path.join(CC, "mine_done_%s.txt" % CRAWL)
    done = set(open(donef).read().split()) if os.path.exists(donef) else set()
    statsf = os.path.join(CC, "mine_stats_%s.json" % CRAWL)
    if os.path.exists(statsf):
        S.update(json.load(open(statsf)))
    os.makedirs(os.path.dirname(LEADS_OUT), exist_ok=True)
    leads_f = open(LEADS_OUT, "a", encoding="utf-8")
    orgs_f = open(os.path.join(CC, "mine_orgs_%s.jsonl" % CRAWL), "a", encoding="utf-8")
    processed, blocked_parts = 0, 0
    with ThreadPoolExecutor(a.workers) as ex:
        while True:
            todo = [(i, p) for i, p in finished_parts() if str(i) not in done]
            if a.parts:
                todo = [(i, p) for i, p in todo if i < a.parts]
            if not todo:
                if not a.follow or (scan_finished() and not [1 for i, p in finished_parts() if str(i) not in done]):
                    break
                time.sleep(60)
                continue
            for i, path in todo:
                t0 = time.time()
                try:
                    n, groups = load_part(con, path)
                except Exception as e:  # a part the scan could not write (0 bytes / partial): skip it
                    log("part %03d unreadable (%s): skipped" % (i, str(e)[:120]))
                    bump("parts_unreadable")
                    done.add(str(i))
                    open(donef, "a").write("%d\n" % i)
                    continue
                items, pages_of = [], {}
                for org, lst in groups.items():
                    lst.sort()
                    sel = lst[:4]
                    kb = match_known(known, sorted({x[4] for x in sel}), org)
                    oname = kb[1] if kb and kb[1] else org
                    pages_of[org] = [(x[3], x[4], x[0], x[5], x[6]) for x in sel]
                    for t, _, _, url, host, mime, d, fn, off, ln in sel:
                        items.append((url, host, org, mime, d, fn, off, ln, t, "https://%s/" % host, oname))
                results, failed = {}, 0
                for r in ex.map(read_page, items):
                    results.setdefault(r["org"], []).append(r)
                    failed += not r["ok"]
                if failed > max(5, len(items) // 10):  # blocked or throttled: drop this pass, retry the part later
                    blocked_parts += 1
                    log("part %03d: %d of %d pages failed (%s); retry in 15 min" % (i, failed, len(items), json.dumps(S)))
                    if blocked_parts >= 8:
                        log("Common Crawl keeps refusing (403/5xx): stopping; rerun later, the run resumes")
                        leads_f.close()
                        orgs_f.close()
                        return
                    time.sleep(900)
                    break
                blocked_parts = 0
                for r in sum(results.values(), []):
                    bump("pages_read" if r["ok"] else "pages_failed")
                    bump("pages_with_ap_mailbox", r["ap"])
                for org, pages in pages_of.items():
                    finish_org(org, [(p[0], p[1], p[2], p[3], p[4]) for p in pages], results.get(org, []), known,
                               seen_rows, seen_leads, leads_f, orgs_f, master)
                bump("parts_done")
                bump("index_rows", n)
                bump("pages_selected", len(items))
                bump("orgs_selected", len(pages_of))
                added = sync_out(master)
                done.add(str(i))
                open(donef, "a").write("%d\n" % i)
                json.dump(S, open(statsf, "w"), indent=1)
                processed += 1
                log("part %03d: %d index rows, %d orgs, %d pages, %.0fs, %d rows to crawler file; %s" %
                    (i, n, len(pages_of), len(items), time.time() - t0, added, json.dumps(S)))
            if a.parts and processed >= len([1 for i, p in finished_parts() if i < a.parts]):
                break
    leads_f.close()
    orgs_f.close()
    report()


def report():
    p = os.path.join(CC, "mine_orgs_%s.jsonl" % CRAWL)
    orgs = {}
    for line in open(p, encoding="utf-8") if os.path.exists(p) else []:
        try:
            o = json.loads(line)
        except ValueError:
            continue
        x = orgs.setdefault(o["org"], {"ap": False, "tech": set(), "known": "", "emitted": 0, "any": False})
        x["ap"] = x["ap"] or any(k in AP_GRADE for k in o["best"])
        x["any"] = x["any"] or bool(o["best"])
        x["tech"] |= set(o["tech"])
        x["known"] = x["known"] or o["known"]
        x["emitted"] += o["emitted"]
    ap = [o for o in orgs.values() if o["ap"]]
    statsf = os.path.join(CC, "mine_stats_%s.json" % CRAWL)
    st = json.load(open(statsf)) if os.path.exists(statsf) else {}
    rep = {"parts_done": st.get("parts_done", 0), "index_rows": st.get("index_rows", 0), "pages_selected": st.get("pages_selected", 0),
           "pages_read": st.get("pages_read", 0), "pages_failed": st.get("pages_failed", 0), "throttled": st.get("throttled", 0),
           "pages_with_ap_mailbox": st.get("pages_with_ap_mailbox", 0), "orgs_read": len(orgs),
           "orgs_with_any_mailbox": sum(o["any"] for o in orgs.values()), "orgs_with_ap_mailbox": len(ap),
           "ap_orgs_with_tech_signature": sum(bool(o["tech"]) for o in ap),
           "orgs_with_tech_signature": sum(bool(o["tech"]) for o in orgs.values()),
           "orgs_matching_known_buyers": sum(bool(o["known"]) for o in orgs.values()),
           "known_buyers_with_ap_mailbox": sum(bool(o["known"]) for o in ap),
           "rows_written": sum(o["emitted"] for o in orgs.values())}
    print(json.dumps(rep), flush=True)
    return rep


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--parts", type=int, default=0, help="only parts with index < N (test)")
    ap.add_argument("--follow", action="store_true", help="wait for new parts until the scan has finished")
    ap.add_argument("--workers", type=int, default=4)
    ap.add_argument("--rate", type=float, default=2.0, help="requests per second to data.commoncrawl.org (AGENTS.md rule 9)")
    ap.add_argument("--report", action="store_true")
    a = ap.parse_args()
    _pause["rate"] = a.rate
    if a.report:
        report()
    else:
        run(a)


if __name__ == "__main__":
    main()
