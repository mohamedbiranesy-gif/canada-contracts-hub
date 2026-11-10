#!/usr/bin/env python3
"""Row factory, cloud edition: NEW buyers from the client / case-study / portfolio pages of Canada-located vendors, at web scale, read from
the Common Crawl archive. No AI, no search engine, no request to the vendors' own sites.

Why (owner 2026-11-09 19:18 EST: "the 63,000 rows have not moved … the goal is 200,000"): the lead scanners that produced the relationship rows
(client_lists*.py, logo_walls.py, customer_stories.py) only ever ran on the owner's Mac, from vendor lists kept on that Mac. With the Mac off,
nothing produced a new buyer. This engine needs no local list and no Mac: Common Crawl's columnar URL index names every captured page of every
.ca host whose PATH is a client page (the same path rule contrib/claude/rank_buyers/rank.py uses for a "client listing"), and the page itself
is read from the archive with one HTTP range request to data.commoncrawl.org.

  index   --shard K/N            scan the index parts K mod N of the newest crawl                      -> out/cc_rel_pages_<K>.csv
  extract --shard K/N            read each page of the shard, keep its outbound client links           -> out/cc_leads_<K>.jsonl (+ noaddr, done)
  merge   SHARD_DIR              shard files + what is on main -> data/incoming/claude/claude_buyer_leads_cc.csv, claude_lead_details_cc.jsonl.gz,
                                 claude_cc_extract_done.tsv
Rules kept:
  1. Vendor in Canada (AGENTS.md hard rule 1): only when the vendor's OWN PAGE prints a Canadian postal address (province + postal code; the
     quote is kept as proof). A .ca domain alone is not enough (CIRA also admits foreign trademark owners): such pages go to a side file.
  2. Buyer named: the linked organisation's own domain and the label the vendor gave it; links without a label, generic labels, platforms,
     social networks, "website by" credits and directory pages (more than 150 linked sites) are dropped. A domain linked by more than 15
     vendors is a platform or a badge, not a client (same rule as tools/lead_scanner.py).
  3. Evidence: the vendor page URL, its capture date in the archive, the label, the address quote. The buyer's mailbox is NOT taken here: it
     is read on the buyer's own site by tools/lead_crawl.py and re-fetched by the referee like every other mailbox.
Polite: only data.commoncrawl.org is contacted, a few requests at a time, identified user agent, retries with back-off.
"""
import argparse, collections, csv, glob, gzip, hashlib, html, io, json, os, random, re, sys, time, urllib.error, urllib.parse, urllib.request
from concurrent.futures import ThreadPoolExecutor

csv.field_size_limit(1 << 30)
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
INC = os.path.join(ROOT, "data/incoming/claude")
UA = "canada-contracts-hub-crawler/1.0 (+https://github.com/mohamedbiranesy-gif/canada-contracts-hub)"
CC = "https://data.commoncrawl.org/"
TODAY = time.strftime("%Y-%m-%d")
PAGES = os.path.join(INC, "claude_cc_rel_pages.csv.gz")
EXDONE = os.path.join(INC, "claude_cc_extract_done.tsv")
LEADS_CC = os.path.join(INC, "claude_buyer_leads_cc.csv")
DETAILS_CC = os.path.join(INC, "claude_lead_details_cc.jsonl.gz")
LEAD_COLS = ["buyer_key", "buyer_name", "website", "canadian_vendor_rows", "example_vendor", "canada_field_value", "evidence_dataset", "latest_record_date"]
PAGE_COLS = ["url", "host", "dom", "path", "fetch_time", "warc_filename", "warc_record_offset", "warc_record_length"]

# the path rule of rank.py (REL_PATH / NOT_REL_PATH): a page that passes it is a "client listing" there, so every lead found here ranks as one
REL_SQL = r"client|customer|case-stud|casestud|case_stud|temoignage|t%c3%a9moignage|testimonial|success-stor|portfolio|our-work|realisations?([^a-z]|$)|r%c3%a9alisations?|nos-realisations|clientele"
NOT_SQL = (r"terms|reference|support|service|product|letter|lettre|news|nouvelle|blog|article|press|media|document|conditions|bill|/loi|career|emploi|job|event|evenement|contact|about|a-propos|partner|partenaire"
           r"|login|log-in|signin|sign-in|account|compte|portal|portail|espace-client|zone-client|acces-client|clientarea|client-area|client-access|client-cent|client-zone|customer-care|customer-cent|customer/"
           r"|/tag/|/tags/|/category/|/categorie/|/author/|/page/[0-9]|/feed|wp-json|wp-content|wp-admin|/cart|/panier|/checkout|privacy|/search|/recherche|\.(pdf|jpe?g|png|gif|xml|json|css|js)$")
VENDOR_SKIP = re.compile(r"(^|\.)(gc|canada)\.ca$|\.gouv\.qc\.ca$|(^|\.)gov\.[a-z]{2}\.ca$|\.gov\.ca$|kijiji|yellowpages|pagesjaunes|canada411|indeed|eventbrite|amazon|ebay|walmart|bestbuy|costco|"
                         r"canadiantire|homedepot|(^|\.)cbc\.ca$|ctvnews|globalnews|radio-canada|lapresse|ledevoir|thestar|nationalpost|theglobeandmail|wikipedia|reddit|craigslist|linkedin|facebook|"
                         r"google|youtube|yelp|tripadvisor|booking|expedia|airbnb|realtor\.ca|centris|duproprio|autotrader|workopolis|glassdoor|monster|jobbank|canadapost|purolator|(^|\.)bell\.ca$|"
                         r"videotron|blogspot|wordpress|wixsite|weebly|squarespace|myshopify|godaddysites|webflow\.io|github\.io|tumblr|substack|medium\.com", re.I)
LABEL_SKIP = re.compile(r"\b(powered by|website by|site by|web ?site design|web design|design(?:ed)? by|developed by|built by|cr[ée]ation (?:de )?site|conception (?:de |du )?site|conception web|"
                        r"r[ée]alis[ée] par|propuls[ée] par|hosted by|h[ée]berg[ée]|theme by|template by|follow us|suivez|share|partager|privacy|confidentialit|terms|conditions|cookie|sitemap|plan du site)\b", re.I)
PROV = (r"(?:QC|Qc|ON|BC|AB|MB|SK|NS|NB|NL|PE|PEI|YT|NT|NU|Qu[ée]bec|Ontario|British Columbia|Colombie-Britannique|Alberta|Manitoba|Saskatchewan|Nova Scotia|Nouvelle-[ÉE]cosse|"
        r"New Brunswick|Nouveau-Brunswick|Newfoundland(?: and Labrador)?|Terre-Neuve(?:-et-Labrador)?|Prince Edward Island|[ÎI]le-du-Prince-[ÉE]douard|Yukon|Northwest Territories|Nunavut)")
PC = r"[ABCEGHJ-NPRSTVXY]\d[ABCEGHJ-NPRSTV-Z][  \-]?\d[ABCEGHJ-NPRSTV-Z]\d"
ADDR = re.compile(r"(?<![A-Za-z0-9])" + PROV + r"\)?[\s,. ]{0,6}(?:Canada[\s,. ]{0,4})?(" + PC + r")(?![A-Za-z0-9])")

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
try:  # the same link reader and filters as the Mac scanners, so both produce the same kind of lead
    from client_lists import anchors, SKIP, base
except Exception:  # pragma: no cover
    SKIP = re.compile(r"facebook|linkedin|twitter|x\.com|instagram|youtube|youtu\.be|tiktok|pinterest|google|goo\.gl|apple\.com|microsoft|wordpress|wix|squarespace|shopify|godaddy|w3\.org", re.I)

    def base(host):
        host = (host or "").lower()
        return host[4:] if host.startswith("www.") else host

    def anchors(page, pageurl):
        for m in re.finditer(r"(?is)<a\s[^>]*?href\s*=\s*[\"']([^\"'#>]+)[\"'][^>]*>(.*?)</a>", page[:2_000_000]):
            href, inner = urllib.parse.urljoin(pageurl, m.group(1).strip()), m.group(2)
            alt = re.search(r"(?is)(?:alt|title)\s*=\s*[\"']([^\"']{2,120})[\"']", m.group(0) + inner)
            text = re.sub(r"(?s)<[^>]+>", " ", inner)
            yield href, re.sub(r"\s+", " ", (alt.group(1) if alt else "") or text).strip()
try:
    from lead_scanner import PLATFORMS, GENERIC_LABEL
except Exception:  # pragma: no cover
    PLATFORMS = re.compile(r"genially|issuu|canva|calameo|prezi|eventbrite|surveymonkey|typeform|jotform|dropbox|box\.com", re.I)
    GENERIC_LABEL = re.compile(r"^(read more|learn more|more|visit|website|site web|click here|here|cliquez ici|en savoir plus|voir|view|link|lien|home|accueil|\W*)$", re.I)


def http_get(url, headers=None, timeout=90, tries=6):
    h = {"User-Agent": UA}
    h.update(headers or {})
    err = None
    for i in range(tries):
        try:
            with urllib.request.urlopen(urllib.request.Request(url, headers=h), timeout=timeout) as r:
                return r.read()
        except urllib.error.HTTPError as e:
            err = e
            if e.code in (400, 401, 403, 404, 416):
                raise
        except Exception as e:
            err = e
        time.sleep(min(60, 2 ** i + random.random() * 2))
    raise err


def newest_crawl(want=""):
    """(crawl id, parquet paths of its columnar index, subset=warc). The newest crawl whose index is published."""
    ids = [want] if want and want != "auto" else []
    if not ids:
        try:
            ids = [c["id"] for c in json.loads(http_get("https://index.commoncrawl.org/collinfo.json", tries=3))][:5]
        except Exception as e:
            print("collinfo not reachable (%s); falling back to the last crawl we mined" % type(e).__name__, flush=True)
        ids.append("CC-MAIN-2026-43")
    for cid in ids:
        try:
            raw = http_get(CC + "crawl-data/%s/cc-index-table.paths.gz" % cid, tries=3)
            paths = [l.strip() for l in gzip.decompress(raw).decode().split("\n") if "subset=warc/" in l and l.strip().endswith(".parquet")]
            if paths:
                return cid, sorted(paths)
        except Exception as e:
            print("index of %s not available: %s" % (cid, e), flush=True)
    sys.exit("no Common Crawl columnar index reachable")


def shard_of(a):
    k, n = (a.shard.split("/") + ["1"])[:2] if a.shard else ("0", "1")
    return int(k), max(1, int(n))


def index(a):
    import duckdb
    k, n = shard_of(a)
    cid, paths = newest_crawl(a.crawl)
    mine = paths[k::n]
    if a.limit_parts:
        mine = mine[:a.limit_parts]
    print("crawl %s: %d index parts, shard %d/%d reads %d" % (cid, len(paths), k, n, len(mine)), flush=True)
    con = duckdb.connect()
    ver = tuple(int(x) for x in re.findall(r"\d+", duckdb.__version__)[:2])
    for st in ("INSTALL httpfs", "LOAD httpfs", "SET threads=4", "SET http_retries=8", "SET http_retry_wait_ms=2000",
               "SET http_timeout=%d" % (300 if ver >= (1, 1) else 300000), "SET enable_progress_bar=false"):
        try:
            con.execute(st)
        except Exception as e:
            print("duckdb setting skipped: %s (%s)" % (st, str(e)[:80]), flush=True)
    os.makedirs("out", exist_ok=True)
    rows, t0, shown = [], time.time(), False
    for i, p in enumerate(mine):
        url = CC + p
        if not shown:
            try:
                cols = [r[0] for r in con.execute("DESCRIBE SELECT * FROM read_parquet('%s')" % url).fetchall()]
                print("index columns:", ", ".join(cols), flush=True)
            except Exception as e:
                print("describe failed:", str(e)[:300], flush=True)
            shown = True
        q = ("SELECT url, url_host_name, url_host_registered_domain, url_path, CAST(fetch_time AS VARCHAR), warc_filename, warc_record_offset, warc_record_length "
             "FROM read_parquet('%s') WHERE url_host_tld = 'ca' AND fetch_status = 200 AND content_mime_detected = 'text/html' AND url_query IS NULL "
             "AND length(url_path) BETWEEN 2 AND 90 AND regexp_matches(lower(url_path), '%s') AND NOT regexp_matches(lower(url_path), '%s')") % (url, REL_SQL.replace("'", "''"), NOT_SQL.replace("'", "''"))
        for attempt in range(3):
            try:
                got = con.execute(q).fetchall()
                rows += got
                if got or i % 25 == 0:
                    print("%s part %d/%d: %d pages (total %d, %.0f s)" % (time.strftime("%H:%M:%S"), i + 1, len(mine), len(got), len(rows), time.time() - t0), flush=True)
                break
            except Exception as e:
                print("part %d attempt %d failed: %s" % (i, attempt + 1, str(e)[:200]), flush=True)
                time.sleep(20 * (attempt + 1))
    by = collections.defaultdict(list)
    for r in rows:
        if r[2] and not VENDOR_SKIP.search(r[1] or ""):
            by[r[2]].append(r)
    with open("out/cc_rel_pages_%d.csv" % k, "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(PAGE_COLS + ["crawl"])
        kept = 0
        for dom, rs in by.items():
            for r in sorted(rs, key=lambda r: (len(r[3] or ""), r[0]))[:a.per_domain]:
                w.writerow(list(r) + [cid])
                kept += 1
    print("shard %d: %d matching pages on %d .ca domains; kept %d (at most %d per domain)" % (k, len(rows), len(by), kept, a.per_domain), flush=True)


def warc_html(fn, off, ln):
    """the captured page (decoded text, capture's HTTP status line) from one range request; None when the record cannot be read"""
    try:
        raw = http_get(CC + fn, headers={"Range": "bytes=%d-%d" % (off, off + ln - 1)}, timeout=60, tries=5)
        rec = gzip.decompress(raw)
    except Exception:
        return None
    i = rec.find(b"\r\n\r\n")
    if i < 0:
        return None
    resp = rec[i + 4:]
    j = resp.find(b"\r\n\r\n")
    if j < 0:
        return None
    head, body = resp[:j].decode("latin-1", "replace"), resp[j + 4:]
    m = re.search(r"(?i)content-type:[^\r\n]*charset=[\"']?([\w-]+)", head)
    cs = m.group(1) if m else None
    if not cs:
        m2 = re.search(rb"(?i)<meta[^>]+charset=[\"']?([\w-]+)", body[:4000])
        cs = m2.group(1).decode("ascii", "replace") if m2 else "utf-8"
    try:
        text = body[:3_000_000].decode(cs, "replace")
    except LookupError:
        text = body[:3_000_000].decode("utf-8", "replace")
    return html.unescape(text)


def visible(page):
    t = re.sub(r"(?is)<(script|style|noscript)\b.*?</\1>", " ", page[:1_500_000])
    return re.sub(r"\s+", " ", re.sub(r"(?s)<[^>]+>", " ", t))


def leads_of(page, row):
    """(hits, address quote). hits: one per linked organisation; the quote is the vendor's own Canadian postal address ('' when the page prints none)"""
    url, vhost, dom = row["url"], base(row["host"]), (row["dom"] or "").lower()
    text = visible(page)
    m = ADDR.search(text)
    quote = re.sub(r"^\S*\s", "", text[max(0, m.start() - 110):m.end()].strip())[-200:] if m else ""
    title = re.search(r"(?is)<title[^>]*>(.*?)</title>", page[:200_000])
    title = re.sub(r"\s+", " ", re.sub(r"(?s)<[^>]+>", " ", title.group(1))).strip()[:120] if title else ""
    site = re.search(r"(?is)<meta[^>]+property=[\"']og:site_name[\"'][^>]+content=[\"']([^\"']{2,80})[\"']", page[:200_000])
    hits = {}
    for href, label in anchors(page, url):
        try:
            h = base(urllib.parse.urlparse(href).hostname)
        except ValueError:
            continue
        label = (label or "").strip()
        if (not h or "." not in h or len(h) > 60 or h == vhost or h == dom or h.endswith("." + dom) or re.fullmatch(r"[\d.]+", h)
                or SKIP.search(h) or PLATFORMS.search(h) or VENDOR_SKIP.search(h)
                or not label or len(label) > 120 or GENERIC_LABEL.match(label) or LABEL_SKIP.search(label)):
            continue
        hits.setdefault(h, {"platform": "vendor_site", "domain": h, "dataset_id": url, "dataset": "client page of a Canada-located vendor (Common Crawl capture)",
                            "dataset_url": url, "publisher": h, "buyer_unit": "", "website": "https://%s/" % h, "vendor": (site.group(1).strip() if site else "") or vhost,
                            "canada_field": "vendor located in Canada (cc: .ca domain + Canadian postal address on its own page)", "canada_value": vhost,
                            "row": {"relationship_page": url, "page_title": title, "client_label": label[:120], "vendor_key": "cc:" + dom, "vendor_site": "https://%s/" % vhost,
                                    "pass": "cc_index", "capture": (row.get("fetch_time") or "")[:19], "vendor_address_quote": quote,
                                    "warc": "%s:%s:%s" % (row["warc_filename"], row["warc_record_offset"], row["warc_record_length"])}})
    return (list(hits.values()) if 0 < len(hits) <= 150 else []), quote


def extract(a):
    k, n = shard_of(a)
    done = set()
    if os.path.exists(EXDONE):
        done = {l.split("\t")[0] for l in open(EXDONE, encoding="utf-8")}
    pages = []
    with gzip.open(PAGES, "rt", encoding="utf-8", newline="") as fh:
        for r in csv.DictReader(fh):
            if r["url"] in done or int(hashlib.sha1((r["dom"] or r["host"]).encode()).hexdigest(), 16) % n != k:
                continue
            pages.append(r)
    random.Random(7).shuffle(pages)  # a time-boxed run samples all domains instead of one alphabetical slice
    if a.limit:
        pages = pages[:a.limit]
    os.makedirs("out", exist_ok=True)
    deadline = time.time() + a.minutes * 60
    stats = collections.Counter()
    fl = open("out/cc_leads_%d.jsonl" % k, "a", encoding="utf-8")
    fn = open("out/cc_leads_noaddr_%d.jsonl" % k, "a", encoding="utf-8")
    fd = open("out/cc_extract_done_%d.tsv" % k, "a", encoding="utf-8")
    import threading
    lock = threading.Lock()
    print("shard %d/%d: %d pages to read (%d done before)" % (k, n, len(pages), len(done)), flush=True)

    def one(r):
        if time.time() > deadline:
            return
        try:
            page = warc_html(r["warc_filename"], int(r["warc_record_offset"]), int(r["warc_record_length"]))
            hits, quote = leads_of(page, r) if page else ([], "")
        except Exception as e:
            page, hits, quote = None, [], ""
            with lock:
                stats["error:" + type(e).__name__] += 1
        with lock:
            stats["pages"] += 1
            stats["unreadable"] += page is None
            stats["with_links"] += bool(hits)
            stats["with_address"] += bool(hits and quote)
            stats["leads"] += len(hits) if quote else 0
            stats["leads_noaddr"] += 0 if quote else len(hits)
            out = fl if quote else fn
            for h in hits:
                out.write(json.dumps(h, ensure_ascii=False) + "\n")
            fd.write("%s\t%s\t%d\t%d\n" % (r["url"], TODAY, len(hits), 1 if quote else 0))
            if stats["pages"] % 500 == 0:
                print(time.strftime("%H:%M:%S"), dict(stats), flush=True)
    with ThreadPoolExecutor(a.workers) as ex:
        list(ex.map(one, pages))
    for f in (fl, fn, fd):
        f.close()
    print("finished", dict(stats), flush=True)


def address_from(quote):
    """the address part of the quote: from the street number to the postal code (the whole quote when no street number is seen)"""
    m = re.search(r"(?<![\w-])\d{1,6}[A-Za-z]?,?\s+(?:[a-zà-ÿ]+\.?\s+){0,2}[A-ZÀ-Ý0-9]", quote or "")
    return (quote[m.start():] if m else (quote or "")).strip()


def lead_key(domain):
    # the key tools/lead_scanner.py --bridge gives a vendor-site lead (publisher = the linked domain): the same buyer found by both gets one key
    return "lead:" + hashlib.sha1(("%s|%s" % (domain, domain.lower())).encode()).hexdigest()[:16]


def merge(a):
    d = a.dir
    recs = []
    for f in sorted(glob.glob(os.path.join(d, "cc_leads_[0-9]*.jsonl"))):
        for l in open(f, encoding="utf-8"):
            try:
                recs.append(json.loads(l))
            except ValueError:
                pass
    # extraction progress
    seen = {}
    for f in [EXDONE] + sorted(glob.glob(os.path.join(d, "cc_extract_done_*.tsv"))):
        if os.path.exists(f):
            for l in open(f, encoding="utf-8"):
                p = l.rstrip("\n").split("\t")
                if p and p[0]:
                    seen[p[0]] = l.rstrip("\n")
    with open(EXDONE, "w", encoding="utf-8") as f:
        for u in sorted(seen):
            f.write(seen[u] + "\n")
    # side file: client links of .ca vendors whose page printed no address (kept for the address pass; never delivered from here)
    na = sorted(glob.glob(os.path.join(d, "cc_leads_noaddr_*.jsonl")))
    if na:
        side = os.path.join(INC, "claude_cc_leads_noaddr.jsonl.gz")
        have = set()
        if os.path.exists(side):
            have = set(gzip.open(side, "rt", encoding="utf-8").read().split("\n"))
        for f in na:
            have |= {json.dumps({k: v for k, v in json.loads(l).items() if k in ("domain", "dataset_url", "vendor", "canada_value", "row")}, ensure_ascii=False, sort_keys=True)
                     for l in open(f, encoding="utf-8") if l.strip()}
        have.discard("")
        with gzip.open(side, "wt", encoding="utf-8") as f:
            f.write("\n".join(sorted(have)) + "\n")
    known = set()
    main = os.path.join(INC, "claude_buyer_leads.csv")
    if os.path.exists(main):
        for r in csv.DictReader(open(main, encoding="utf-8", errors="replace")):
            known.add(r["buyer_key"])
            h = base(urllib.parse.urlparse(r.get("website") or "").hostname or "")
            if h:
                known.add(h)
    prev, pdet = {}, {}
    if os.path.exists(LEADS_CC):
        prev = {r["buyer_key"]: r for r in csv.DictReader(open(LEADS_CC, encoding="utf-8"))}
    if os.path.exists(DETAILS_CC):
        for l in gzip.open(DETAILS_CC, "rt", encoding="utf-8"):
            try:
                o = json.loads(l)
                pdet[o["key"]] = o
            except (ValueError, KeyError):
                pass
    vendors_of = collections.defaultdict(set)
    for r in recs:
        vendors_of[r["domain"]].add(r["canada_value"])
    new = 0
    for r in sorted(recs, key=lambda r: (len(r["dataset_url"]), r["dataset_url"])):
        dom = r["domain"]
        key = lead_key(dom)
        if len(vendors_of[dom]) > 15 or key in known or dom in known:
            continue
        row = r.get("row") or {}
        if key not in prev:
            new += 1
            prev[key] = {"buyer_key": key, "buyer_name": dom, "website": r["website"], "canadian_vendor_rows": 0, "example_vendor": r["vendor"],
                         "canada_field_value": "%s=%s" % (r["canada_field"], r["canada_value"]), "evidence_dataset": r["dataset_url"], "latest_record_date": ""}
            pdet[key] = {"key": key, "platform": "vendor_site_cc", "record_url": r["dataset_url"], "vendor": r["vendor"], "record_date": "", "title": "",
                         "vendor_address": ("%s (as printed on %s, archive capture %s)" % (address_from(row.get("vendor_address_quote")), r["dataset_url"], (row.get("capture") or "")[:10])) if row.get("vendor_address_quote") else "",
                         "vendor_address_quote": row.get("vendor_address_quote") or "",
                         "vendor_site": row.get("vendor_site") or "", "client_label": row.get("client_label") or "", "page_title": row.get("page_title") or "", "capture": row.get("capture") or "", "warc": row.get("warc") or ""}
        prev[key]["canadian_vendor_rows"] = max(int(prev[key].get("canadian_vendor_rows") or 0), len(vendors_of[dom]))
    with open(LEADS_CC, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=LEAD_COLS)
        w.writeheader()
        for k in sorted(prev):
            w.writerow({c: prev[k].get(c, "") for c in LEAD_COLS})
    with gzip.open(DETAILS_CC, "wt", encoding="utf-8") as f:
        for k in sorted(pdet):
            f.write(json.dumps(pdet[k], ensure_ascii=False) + "\n")
    print("cc leads: %d link records read, %d new buyers, %d buyers in %s; pages read so far %d" % (len(recs), new, len(prev), os.path.basename(LEADS_CC), len(seen)))


def merge_index(a):
    rows, crawl = {}, ""
    for f in sorted(glob.glob(os.path.join(a.dir, "cc_rel_pages_*.csv"))):
        for r in csv.DictReader(open(f, encoding="utf-8")):
            rows[r["url"]] = r
            crawl = r.get("crawl") or crawl
    if not rows:
        sys.exit("no index rows in " + a.dir)
    by = collections.defaultdict(list)
    for r in rows.values():
        by[r["dom"]].append(r)
    n = 0
    with gzip.open(PAGES, "wt", encoding="utf-8", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=PAGE_COLS + ["crawl"])
        w.writeheader()
        for dom in sorted(by):
            for r in sorted(by[dom], key=lambda r: (len(r["path"] or ""), r["url"]))[:a.per_domain]:
                w.writerow(r)
                n += 1
    print("index %s: %d client pages on %d .ca domains -> %s" % (crawl, n, len(by), os.path.basename(PAGES)))


def main():
    ap = argparse.ArgumentParser()
    sub = ap.add_subparsers(dest="cmd", required=True)
    p = sub.add_parser("index"); p.add_argument("--shard", default="0/1"); p.add_argument("--crawl", default="auto"); p.add_argument("--limit-parts", type=int, default=0); p.add_argument("--per-domain", type=int, default=6)
    p = sub.add_parser("merge-index"); p.add_argument("dir"); p.add_argument("--per-domain", type=int, default=6)
    p = sub.add_parser("extract"); p.add_argument("--shard", default="0/1"); p.add_argument("--minutes", type=float, default=120); p.add_argument("--workers", type=int, default=10); p.add_argument("--limit", type=int, default=0)
    p = sub.add_parser("merge"); p.add_argument("dir")
    a = ap.parse_args()
    {"index": index, "merge-index": merge_index, "extract": extract, "merge": merge}[a.cmd](a)


if __name__ == "__main__":
    main()
