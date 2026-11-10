#!/usr/bin/env python3
"""Accredited businesses of the Canadian Better Business Bureaus (cloud): a business accredited by its local BBB pays it dues — BBB's own FAQ:
"Dues paid by Accredited Businesses fund our work" (https://www.bbb.org/all/faq, read 2026-11-10). Each accredited business has a public
profile that names it, gives its address and telephone, its website, the date it has been accredited since, and the local BBB that accredits
it. A dated, current, named relationship with a Canadian body, published by that body.

Access: bbb.org's robots.txt lists a sitemap of every accredited business profile and allows the profile pages ("BBB welcomes AI crawlers
accessing public business profile, category and article pages", https://www.bbb.org/llms.txt). One host: ONE runner, 2 requests per second.

  index                 the sitemap of accredited profiles -> the profile URLs under /ca/ -> out/bbb_profiles_ca.csv
  read [--minutes M]    each profile not read before -> out/bbb_leads.jsonl (lead + details), out/bbb_done.tsv; each local BBB's own page once
                        (its postal address: the proof that the accrediting body is in Canada) -> out/bbb_local.jsonl
  merge DIR --stamp S   -> data/incoming/claude/bbb/ (profiles_ca.csv.gz, local.jsonl, done_<S>.gz) and data/incoming/claude/lead_shards/
                        (leads_bbb_<S>.gz, details_bbb_<S>.gz): rank.py, the mailbox crawl and the referee's export read every file there
A profile counts only when the page itself says "<name> is BBB Accredited" and names a local BBB whose own page prints a Canadian postal
address. The business's own e-mail is not on the profile: the mailbox crawl reads the business's own site (the website the profile links).
"""
import argparse, collections, csv, glob, gzip, hashlib, html, json, os, re, sys, threading, time, urllib.parse

csv.field_size_limit(1 << 30)
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import ap_crawler as C  # noqa: E402
import cc_clients as CCL  # noqa: E402

INC = CCL.INC
DIR = os.path.join(INC, "bbb")
SHARDS = os.path.join(INC, "lead_shards")
PROFILES = os.path.join(DIR, "profiles_ca.csv.gz")
LOCAL = os.path.join(DIR, "local.jsonl")
TODAY = time.strftime("%Y-%m-%d")
SITEMAP = "https://www.bbb.org/sitemap-accredited-business-profiles-index.xml"
FAQ = "https://www.bbb.org/all/faq"
DUES_QUOTE = "Dues paid by Accredited Businesses fund our work"
LEAD_COLS = CCL.LEAD_COLS
C.HOST_INTERVAL = 0.5  # one host, one runner: 2 requests per second


def fetch(url, limit=30_000_000):
    return C.fetch(url, limit)


def index(a):
    os.makedirs("out", exist_ok=True)
    os.makedirs(C.STATE, exist_ok=True)
    st, ct, data, final = fetch(SITEMAP)
    if st != 200 or not data:
        sys.exit("sitemap index not readable: %s" % st)
    maps = re.findall(r"<loc>\s*([^<\s]+)\s*</loc>", data.decode("utf-8", "replace"))
    print("sitemap index: %d files" % len(maps), flush=True)
    urls = set()
    for i, m in enumerate(maps):
        m = html.unescape(m)
        if not C.allowed(m):
            continue
        st, ct, data, final = fetch(m)
        if st != 200 or not data:
            print("  %s: %s" % (m, st), flush=True)
            continue
        if data[:2] == b"\x1f\x8b":
            try:
                data = gzip.decompress(data)
            except Exception:
                continue
        locs = re.findall(r"<loc>\s*([^<\s]+)\s*</loc>", data.decode("utf-8", "replace"))
        ca = [html.unescape(u).split("?")[0].rstrip("/") for u in locs if "/ca/" in u and "/profile/" in u]
        urls.update(ca)
        if i % 10 == 0 or ca:
            print("  %s: %d profiles, %d under /ca/ (total %d)" % (m.rsplit("/", 1)[-1], len(locs), len(ca), len(urls)), flush=True)
    with open("out/bbb_profiles_ca.csv", "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["url"])
        for u in sorted(urls):
            w.writerow([u])
    print("accredited business profiles under /ca/: %d" % len(urls), flush=True)


def done_keys():
    out = set()
    for p in sorted(glob.glob(os.path.join(DIR, "done_*.gz"))):
        with gzip.open(p, "rt", encoding="utf-8") as fh:
            for l in fh:
                q = l.rstrip("\n").split("\t")
                if q and q[0] and (len(q) < 3 or not q[2].startswith(("http_5", "unreachable", "blocked"))):
                    out.add(q[0])
    return out


def local_bbbs():
    out = {}
    if os.path.exists(LOCAL):
        for l in open(LOCAL, encoding="utf-8"):
            try:
                o = json.loads(l)
                out[o["slug"]] = o
            except (ValueError, KeyError):
                pass
    return out


SINCE = re.compile(r"BBB Accredited Since:?\s*(\d{1,2})/(\d{1,2})/(\d{4})", re.I)
IS_ACC = re.compile(r"\bis BBB Accredited\b", re.I)
NOT_ACC = re.compile(r"\bis not BBB Accredited\b|\bnot BBB Accredited\b", re.I)
FIELD = lambda label: re.compile(label + r":?\s*([^|]{2,80}?)(?=\s{2,}|\s+(?:BBB File Opened|Business Started|Business Incorporated|Type of Entity|Business Management|Years in Business|Contact Information|Additional|Local BBB|Accredited Since|Hours|$))", re.I)
F_STARTED, F_INC, F_ENTITY = FIELD("Business Started"), FIELD("Business Incorporated"), FIELD("Type of Entity")
SOCIAL = re.compile(r"(^|\.)(bbb\.org|facebook\.com|instagram\.com|twitter\.com|x\.com|linkedin\.com|youtube\.com|tiktok\.com|pinterest\.com|google\.com|goo\.gl|apple\.com|yelp\.c[a-z]+|bit\.ly|"
                    r"bbbprograms\.org|give\.org|iabbb\.org|cloudflare\.com|onetrust\.com|cookielaw\.org)$", re.I)


def parse_profile(raw, url):
    """dict of what the profile page says, or (None, reason)"""
    un = html.unescape(raw)
    text = C.visible(un)
    m = SINCE.search(text)
    if not IS_ACC.search(text) or NOT_ACC.search(text[:200000]) and not m:
        return None, "not_accredited"
    if not m:
        return None, "no_accredited_since"
    since = "%s-%02d-%02d" % (m.group(3), int(m.group(1)), int(m.group(2)))
    h1 = re.search(r"(?is)<h1[^>]*>(.*?)</h1>", un)
    name = re.sub(r"\s+", " ", re.sub(r"(?s)<[^>]+>", " ", h1.group(1))).strip() if h1 else ""
    if not (2 <= len(name) <= 140):
        t = re.search(r"(?is)<title[^>]*>(.*?)</title>", un)
        name = re.split(r"\s+\|\s+", re.sub(r"\s+", " ", t.group(1)).strip())[0] if t else ""
    if not (2 <= len(name) <= 140):
        return None, "no_name"
    slug, bbb_name, site = "", "", ""
    for mm in re.finditer(r"(?is)<a\s[^>]*?href\s*=\s*[\"']([^\"'#>]+)[\"'][^>]*>(.*?)</a>", un[:3_000_000]):
        href, label = mm.group(1).strip(), re.sub(r"\s+", " ", re.sub(r"(?s)<[^>]+>", " ", mm.group(2))).strip()
        if "/local-bbb/" in href and not slug:
            slug, bbb_name = href.split("/local-bbb/")[-1].strip("/").split("/")[0].split("?")[0], label
        elif href.lower().startswith("http") and not site:
            h = (urllib.parse.urlparse(href).hostname or "").lower()
            h = h[4:] if h.startswith("www.") else h
            if h and "." in h and not SOCIAL.search(h) and (CCL.WEBSITE_LABEL.match(label) or re.search(r"visit\s+website|website", label, re.I)):
                site = "https://%s/" % h
    ma = CCL.ADDR.search(text)
    addr = re.sub(r"\s+", " ", text[max(0, ma.start() - 90):ma.end()]).strip() if ma else ""
    addr = (CCL.address_from(addr) or addr) if addr else ""
    tel = re.search(r"href\s*=\s*[\"']tel:([0-9+().\- ]{7,20})[\"']", un)
    g = lambda rx: (rx.search(text).group(1).strip() if rx.search(text) else "")
    bid = re.search(r"-(\d{4}-\d{3,})(?:/|$|\?)", url)
    quote = re.sub(r"\s+", " ", text[max(0, m.start() - 60):m.end()]).strip()
    return {"name": name, "since": since, "slug": slug, "bbb_name": bbb_name, "site": site, "addr": addr, "tel": tel.group(1).strip() if tel else "", "started": g(F_STARTED)[:40],
            "incorporated": g(F_INC)[:40], "entity": g(F_ENTITY)[:60], "id": bid.group(1) if bid else "", "quote": quote[-200:]}, "ok"


def read(a):
    os.makedirs("out", exist_ok=True)
    os.makedirs(C.STATE, exist_ok=True)
    if not os.path.exists(PROFILES):
        sys.exit("no profile list yet (run the index stage)")
    done = done_keys()
    with gzip.open(PROFILES, "rt", encoding="utf-8", newline="") as fh:
        urls = [r["url"] for r in csv.DictReader(fh) if r["url"] not in done]
    if a.limit:
        urls = urls[:a.limit]
    locals_ = local_bbbs()
    print("profiles to read: %d (%d read before); local BBBs known: %d" % (len(urls), len(done), len(locals_)), flush=True)
    deadline = time.time() + a.minutes * 60
    stats = collections.Counter()
    fl = open("out/bbb_leads.jsonl", "a", encoding="utf-8")
    fd = open("out/bbb_done.tsv", "a", encoding="utf-8")
    fo = open("out/bbb_local.jsonl", "a", encoding="utf-8")
    blocked_run = 0

    def local_of(slug):
        if slug in locals_:
            return locals_[slug]
        u = "https://www.bbb.org/local-bbb/%s" % slug
        o = {"slug": slug, "url": u, "date": TODAY, "status": "", "address": "", "name": ""}
        if C.allowed(u):
            st, ct, data, final = fetch(u)
            if st == 200 and data:
                un = html.unescape(data.decode("utf-8", "replace"))
                text = C.visible(un)
                m = CCL.ADDR.search(text)
                h1 = re.search(r"(?is)<h1[^>]*>(.*?)</h1>", un)
                o["name"] = re.sub(r"\s+", " ", re.sub(r"(?s)<[^>]+>", " ", h1.group(1))).strip()[:120] if h1 else ""
                if m:
                    o["status"], o["address"] = "CA", re.sub(r"^\S*\s", "", re.sub(r"\s+", " ", text[max(0, m.start() - 110):m.end()]).strip())[-200:]
                else:
                    o["status"] = "no_canadian_address"
            else:
                o["status"] = "http_%s" % st
        else:
            o["status"] = "robots"
        locals_[slug] = o
        fo.write(json.dumps(o, ensure_ascii=False) + "\n")
        fo.flush()
        return o

    for u in urls:
        if time.time() > deadline or blocked_run >= 25:
            break
        res, lead = "", None
        try:
            if not C.allowed(u):
                res = "robots"
            else:
                st, ct, data, final = fetch(u, 4_000_000)
                head = data[:20000].decode("utf-8", "replace") if data else ""
                if st in (401, 403, 429) or (C.BLOCK_RX.search(head) and len(data) < 30000):
                    res = "blocked"
                elif st != 200 or not data:
                    res = "http_%s" % st if st else "unreachable"
                else:
                    p, res = parse_profile(data.decode("utf-8", "replace"), u)
                    if p:
                        if not p["slug"]:
                            res = "no_local_bbb"
                        else:
                            lb = local_of(p["slug"])
                            if lb.get("status") != "CA":
                                res = "local_bbb_not_proven_in_canada"
                            else:
                                lead = (p, lb)
        except Exception as e:
            res = "error:" + type(e).__name__
        blocked_run = blocked_run + 1 if res == "blocked" else 0
        stats["profiles"] += 1
        stats[res.split(":")[0]] += 1
        if lead:
            p, lb = lead
            key = "lead:" + hashlib.sha1(("bbb|%s" % (p["id"] or u)).encode()).hexdigest()[:16]
            vend = p["bbb_name"] or lb.get("name") or "Better Business Bureau (%s)" % p["slug"]
            row = {"buyer_key": key, "buyer_name": p["name"], "website": p["site"], "canadian_vendor_rows": 1, "example_vendor": vend,
                   "canada_field_value": "membership / statutory fee relationship: accredited business of the Canadian body (%s)=%s (as printed on %s, read %s); BBB: “%s” (%s)"
                                         % (vend, lb["address"], lb["url"], lb.get("date") or TODAY, DUES_QUOTE, FAQ),
                   "evidence_dataset": u, "latest_record_date": TODAY}
            det = {"key": key, "platform": "bbb_accredited", "record_url": u, "vendor": vend, "record_date": TODAY, "start": p["since"], "reference": p["id"],
                   "title": "BBB accreditation of %s — “%s” (profile read %s)" % (p["name"], p["quote"], TODAY), "vendor_address": "%s (as printed on %s)" % (lb["address"], lb["url"]),
                   "vendor_site": lb["url"], "member_address_quote": p["addr"], "buyer_phone_as_printed": p["tel"], "buyer_entity_type": p["entity"], "buyer_business_started": p["started"],
                   "buyer_incorporated": p["incorporated"], "accredited_since": p["since"], "dues_basis": "%s (%s)" % (DUES_QUOTE, FAQ)}
            fl.write(json.dumps({"lead": row, "details": det}, ensure_ascii=False) + "\n")
            stats["with_website"] += bool(p["site"])
        fd.write("%s\t%s\t%s\n" % (u, TODAY, res))
        if stats["profiles"] % 500 == 0:
            for f in (fl, fd):
                f.flush()
            print(time.strftime("%H:%M:%S"), dict(stats), flush=True)
    for f in (fl, fd, fo):
        f.close()
    print("finished", dict(stats), "(stopped: 25 refusals in a row)" if blocked_run >= 25 else "", flush=True)


# ------------------------------------------------------------------------------------------------------------------- through the archive
# 2026-11-10: bbb.org refused all 25 profile requests of the first run from a GitHub runner (its bot filter; the sitemap itself was served:
# 53,088 accredited profiles under /ca/). Refused means refused — the profiles are not asked for again. bbb.org's robots.txt names CCBot in
# its allowed group, so Common Crawl holds copies of the profile pages: they are read from the archive (data.commoncrawl.org), never from bbb.org.
# A lead needs both: the archived profile ("… is BBB Accredited", "BBB Accredited Since …") and the profile's URL in the accredited sitemap
# read live (still accredited now). The local BBB's own page (its Canadian address) is read from the archive too.
CC_PAGES = os.path.join(DIR, "cc_pages.csv.gz")
CC_COLS = ["url", "fetch_time", "warc_filename", "warc_record_offset", "warc_record_length", "crawl"]


def cc_index(a):
    os.makedirs("out", exist_ok=True)
    con = CCL._duck()
    best, t0 = {}, time.time()
    for spec in CCL.crawl_ids(a.crawl):
        try:
            cid, paths = CCL.newest_crawl(spec)
        except SystemExit as e:
            print("crawl %s skipped: %s" % (spec, e), flush=True)
            continue
        print("crawl %s: %d index parts" % (cid, len(paths)), flush=True)
        for i, p in enumerate(paths):
            q = ("SELECT url, CAST(fetch_time AS VARCHAR), warc_filename, warc_record_offset, warc_record_length FROM read_parquet('%s') "
                 "WHERE url_host_registered_domain = 'bbb.org' AND fetch_status = 200 AND content_mime_detected = 'text/html' "
                 "AND (url_path LIKE '/ca/%%/profile/%%' OR url_path LIKE '/local-bbb/%%')") % (CCL.CC + p)
            for attempt in range(3):
                try:
                    got = con.execute(q).fetchall()
                    for u, ft, fn, off, ln in got:
                        u0 = u.split("?")[0].rstrip("/")
                        if u0 not in best or ft > best[u0][1]:
                            best[u0] = (u0, ft, fn, off, ln, cid)
                    if got or i % 50 == 0:
                        print("%s %s part %d/%d: %d pages (total %d, %.0f s)" % (time.strftime("%H:%M:%S"), cid, i + 1, len(paths), len(got), len(best), time.time() - t0), flush=True)
                    break
                except Exception as e:
                    print("part %d attempt %d failed: %s" % (i, attempt + 1, str(e)[:160]), flush=True)
                    time.sleep(15 * (attempt + 1))
    with open("out/bbb_cc_pages.csv", "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(CC_COLS)
        for u in sorted(best):
            w.writerow(best[u])
    print("archived bbb.org pages: %d (%d profiles under /ca/, %d local BBB pages)" % (len(best), sum(1 for u in best if "/profile/" in u), sum(1 for u in best if "/local-bbb/" in u)), flush=True)


def cc_read(a):
    from concurrent.futures import ThreadPoolExecutor
    os.makedirs("out", exist_ok=True)
    if not os.path.exists(CC_PAGES):
        sys.exit("no archive index of bbb.org yet (stage cc-index)")
    with gzip.open(CC_PAGES, "rt", encoding="utf-8", newline="") as fh:
        pages = list(csv.DictReader(fh))
    current = set()
    if os.path.exists(PROFILES):
        with gzip.open(PROFILES, "rt", encoding="utf-8", newline="") as fh:
            current = {r["url"].split("?")[0].rstrip("/") for r in csv.DictReader(fh)}
    done = done_keys()
    locals_ = local_bbbs()
    lock = threading.Lock()
    fo = open("out/bbb_local.jsonl", "a", encoding="utf-8")
    # 1. the local BBBs' own pages (the body's postal address): the newest archived copy of /local-bbb/<slug>
    for r in pages:
        m = re.search(r"/local-bbb/([a-z0-9-]+)$", r["url"])
        if not m or m.group(1) in locals_:
            continue
        slug = m.group(1)
        page, why = CCL.warc_html(r["warc_filename"], int(r["warc_record_offset"]), int(r["warc_record_length"]))
        o = {"slug": slug, "url": r["url"], "date": (r["fetch_time"] or "")[:10], "status": "", "address": "", "name": "", "via": "archive copy (Common Crawl %s)" % r["crawl"]}
        if page:
            text = C.visible(page)
            ma = CCL.ADDR.search(text)
            h1 = re.search(r"(?is)<h1[^>]*>(.*?)</h1>", page)
            o["name"] = re.sub(r"\s+", " ", re.sub(r"(?s)<[^>]+>", " ", h1.group(1))).strip()[:120] if h1 else ""
            if ma:
                o["status"], o["address"] = "CA", CCL.address_from(re.sub(r"\s+", " ", text[max(0, ma.start() - 110):ma.end()]).strip()) or ""
            else:
                o["status"] = "no_canadian_address"
        else:
            o["status"] = "unreadable:" + why
        if o["status"] == "CA" or slug not in locals_:
            locals_[slug] = o
            fo.write(json.dumps(o, ensure_ascii=False) + "\n")
    print("local BBB pages: %s" % ", ".join("%s=%s" % (s, o.get("status")) for s, o in sorted(locals_.items()))[:600], flush=True)
    todo = [r for r in pages if "/profile/" in r["url"] and r["url"] not in done and (not current or r["url"] in current)]
    if a.limit:
        todo = todo[:a.limit]
    print("archived profiles to read: %d (%d read before; %d archived in all; %d URLs in today's accredited sitemap)" % (len(todo), len(done), sum(1 for r in pages if "/profile/" in r["url"]), len(current)), flush=True)
    deadline = time.time() + a.minutes * 60
    stats = collections.Counter()
    fl = open("out/bbb_leads.jsonl", "a", encoding="utf-8")
    fd = open("out/bbb_done.tsv", "a", encoding="utf-8")

    def one(r):
        if time.time() > deadline:
            return
        u, cap = r["url"], (r["fetch_time"] or "")[:10]
        res, out = "", None
        try:
            page, why = CCL.warc_html(r["warc_filename"], int(r["warc_record_offset"]), int(r["warc_record_length"]))
            if not page:
                res = "unreadable:" + why
            else:
                p, res = parse_profile(page, u)
                if p:
                    lb = locals_.get(p["slug"]) if p["slug"] else None
                    if not p["slug"]:
                        res = "no_local_bbb"
                    elif not lb or lb.get("status") != "CA":
                        res = "local_bbb_not_proven_in_canada"
                    else:
                        out = (p, lb)
        except Exception as e:
            res = "error:" + type(e).__name__
        with lock:
            stats["profiles"] += 1
            stats[res.split(":")[0]] += 1
            if out:
                p, lb = out
                key = "lead:" + hashlib.sha1(("bbb|%s" % (p["id"] or u)).encode()).hexdigest()[:16]
                vend = p["bbb_name"] or lb.get("name") or "Better Business Bureau (%s)" % p["slug"]
                live = "; the profile is in bbb.org's sitemap of accredited businesses read %s" % TODAY if u in current else ""
                row = {"buyer_key": key, "buyer_name": p["name"], "website": p["site"], "canadian_vendor_rows": 1, "example_vendor": vend,
                       "canada_field_value": "membership / statutory fee relationship: accredited business of the Canadian body (%s)=%s (as printed on %s, %s); BBB: “%s” (%s)"
                                             % (vend, lb["address"], lb["url"], lb.get("via") or "read %s" % lb.get("date"), DUES_QUOTE, FAQ),
                       "evidence_dataset": u, "latest_record_date": TODAY if u in current else cap}
                det = {"key": key, "platform": "bbb_accredited", "record_url": u, "vendor": vend, "record_date": cap, "start": p["since"], "reference": p["id"],
                       "title": "BBB accreditation of %s — “%s” (profile as archived by Common Crawl on %s%s)" % (p["name"], p["quote"], cap, live),
                       "vendor_address": "%s (as printed on %s)" % (lb["address"], lb["url"]), "vendor_site": lb["url"], "member_address_quote": p["addr"], "buyer_phone_as_printed": p["tel"],
                       "buyer_entity_type": p["entity"], "buyer_business_started": p["started"], "buyer_incorporated": p["incorporated"], "accredited_since": p["since"],
                       "dues_basis": "%s (%s)" % (DUES_QUOTE, FAQ), "archive": "%s:%s:%s" % (r["warc_filename"], r["warc_record_offset"], r["warc_record_length"]),
                       "in_accredited_sitemap_today": "yes" if u in current else "not checked"}
                fl.write(json.dumps({"lead": row, "details": det}, ensure_ascii=False) + "\n")
                stats["with_website"] += bool(p["site"])
            fd.write("%s\t%s\t%s\n" % (u, TODAY, res))
            if stats["profiles"] % 1000 == 0:
                fl.flush(); fd.flush()
                print(time.strftime("%H:%M:%S"), dict(stats), flush=True)
    with ThreadPoolExecutor(a.workers) as ex:
        list(ex.map(one, todo))
    for f in (fl, fd, fo):
        f.close()
    print("finished", dict(stats), flush=True)


def merge(a):
    os.makedirs(DIR, exist_ok=True)
    os.makedirs(SHARDS, exist_ok=True)
    stamp = a.stamp or time.strftime("%Y%m%dT%H%M%S", time.gmtime())
    msg = []
    for f in sorted(glob.glob(os.path.join(a.dir, "bbb_profiles_ca.csv"))):
        urls = {r["url"] for r in csv.DictReader(open(f, encoding="utf-8"))}
        if os.path.exists(PROFILES):
            with gzip.open(PROFILES, "rt", encoding="utf-8", newline="") as fh:
                urls |= {r["url"] for r in csv.DictReader(fh)}
        with gzip.open(PROFILES, "wt", encoding="utf-8", newline="") as fh:
            w = csv.writer(fh)
            w.writerow(["url"])
            for u in sorted(urls):
                w.writerow([u])
        msg.append("accredited profiles under /ca/: %d" % len(urls))
    for f in sorted(glob.glob(os.path.join(a.dir, "bbb_cc_pages.csv"))):
        rows_ = {}
        if os.path.exists(CC_PAGES):
            with gzip.open(CC_PAGES, "rt", encoding="utf-8", newline="") as fh:
                rows_ = {r["url"]: r for r in csv.DictReader(fh)}
        for r in csv.DictReader(open(f, encoding="utf-8")):
            if r["url"] not in rows_ or r["fetch_time"] > rows_[r["url"]]["fetch_time"]:
                rows_[r["url"]] = r
        with gzip.open(CC_PAGES, "wt", encoding="utf-8", newline="") as fh:
            w = csv.DictWriter(fh, fieldnames=CC_COLS)
            w.writeheader()
            for u in sorted(rows_):
                w.writerow(rows_[u])
        msg.append("archived bbb.org pages indexed: %d" % len(rows_))
    loc = local_bbbs()
    for f in sorted(glob.glob(os.path.join(a.dir, "bbb_local.jsonl"))):
        for l in open(f, encoding="utf-8"):
            try:
                o = json.loads(l)
                loc[o["slug"]] = o
            except (ValueError, KeyError):
                pass
    if loc:
        with open(LOCAL, "w", encoding="utf-8") as fh:
            for s in sorted(loc):
                fh.write(json.dumps(loc[s], ensure_ascii=False) + "\n")
    lines = []
    for f in sorted(glob.glob(os.path.join(a.dir, "bbb_done.tsv"))):
        lines += [l.rstrip("\n") for l in open(f, encoding="utf-8") if l.strip()]
    if lines:
        with gzip.open(os.path.join(DIR, "done_%s.gz" % stamp), "wt", encoding="utf-8") as fh:
            fh.write("\n".join(lines) + "\n")
    have = set()
    for p in glob.glob(os.path.join(SHARDS, "leads_bbb_*.gz")):
        with gzip.open(p, "rt", encoding="utf-8", newline="") as fh:
            have |= {r["buyer_key"] for r in csv.DictReader(fh)}
    rows, dets = [], []
    for f in sorted(glob.glob(os.path.join(a.dir, "bbb_leads.jsonl"))):
        for l in open(f, encoding="utf-8"):
            try:
                o = json.loads(l)
            except ValueError:
                continue
            if o["lead"]["buyer_key"] in have:
                continue
            have.add(o["lead"]["buyer_key"])
            rows.append(o["lead"]); dets.append(o["details"])
    if rows:
        with gzip.open(os.path.join(SHARDS, "leads_bbb_%s.gz" % stamp), "wt", encoding="utf-8", newline="") as fh:
            w = csv.DictWriter(fh, fieldnames=LEAD_COLS)
            w.writeheader()
            for r in rows:
                w.writerow({c: r.get(c, "") for c in LEAD_COLS})
        with gzip.open(os.path.join(SHARDS, "details_bbb_%s.gz" % stamp), "wt", encoding="utf-8") as fh:
            for d in dets:
                fh.write(json.dumps(d, ensure_ascii=False) + "\n")
    res = collections.Counter(l.split("\t")[2].split(":")[0] for l in lines if l.count("\t") >= 2)
    msg.append("profiles read this run: %d (%s); new leads %d (with a website %d); accredited leads on file %d; local BBBs: %s"
               % (len(lines), ", ".join("%s %d" % kv for kv in res.most_common(6)), len(rows), sum(1 for r in rows if r.get("website")), len(have),
                  ", ".join("%s=%s" % (s, o.get("status")) for s, o in sorted(loc.items()))[:400]))
    print("BBB accredited businesses (Canada): " + "; ".join(msg))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("cmd", choices=["index", "read", "cc-index", "cc-read", "merge"])
    ap.add_argument("dir", nargs="?", default="shards")
    ap.add_argument("--minutes", type=float, default=150)
    ap.add_argument("--limit", type=int, default=0)
    ap.add_argument("--stamp", default="")
    ap.add_argument("--crawl", default="last:4", help="cc-index: Common Crawl ids (auto = newest; last:N = the newest N)")
    ap.add_argument("--workers", type=int, default=4, help="cc-read: readers of the archive (it throttles busy clients)")
    a = ap.parse_args()
    {"index": index, "read": read, "cc-index": cc_index, "cc-read": cc_read, "merge": merge}[a.cmd](a)


if __name__ == "__main__":
    main()
