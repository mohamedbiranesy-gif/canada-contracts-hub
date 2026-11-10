#!/usr/bin/env python3
"""Row factory, tenant edition (cloud): organisations that hold a LIVE, PAID account with a Canada-headquartered software vendor.

The idea (owner 2026-11-09 20:42 EST: "a Canadian vendor and someone external … do that, cloud only"): many Canadian software companies
give every paying customer its own address — <clinic>.janeapp.com (Jane Software Inc., North Vancouver), pub-<city>.escribemeetings.com
(eScribe Software Ltd., Markham), <library>.bibliocommons.com, <org>.brightspace.com (D2L), <org>.docebosaas.com, <store>.myshopify.com
(Shopify Inc., Ottawa) … That address exists only while the customer pays, so it is evidence, published on the vendor's own platform, of an
active relationship between a named organisation and a Canada-located vendor. tools/tech_relationships.py already holds the vetted vendor
table (HQ address quoted from each vendor's own site, free-plan vendors excluded, 2026-11-02) and found ~5,500 such buyers from the owner's
Mac; this engine enumerates the customers from Common Crawl's columnar URL index instead, on GitHub runners.

  index   --shard K/N   portal pages of every vetted vendor (index subset=warc) and <store>.myshopify.com redirects to the store's own
                        domain (subset=crawldiagnostics)                                   -> out/tenant_pages_<K>.csv, out/shopify_redirects_<K>.csv
  merge-index DIR       -> data/incoming/claude/claude_cc_tenant_pages.csv.gz, claude_cc_shopify_redirects.csv.gz
  extract --shard K/N   read each portal page from the archive (one range request; tech_relationships.portal_info reads the organisation's
                        name and its own website from it; the free single-practitioner Jane plan is dropped there) -> out/tenant_cands_<K>.jsonl
  merge DIR             -> data/incoming/claude/claude_tenant_candidates.csv.gz   (candidates, NOT leads yet)
  merge-accepted DIR    candidates accepted by tools/lead_crawl.py --candidates -> claude_buyer_leads_cc.csv + claude_lead_details_cc.jsonl.gz
A candidate becomes a lead only after tools/lead_crawl.py has read the organisation's OWN site and found (1) a role mailbox on its own domain
and (2) a postal address in a country the vendor's Canadian company contracts with: Canada for every vendor; Canada or the United States for
Shopify, whose terms say "United States or Canada: Shopify Inc., a Canadian corporation" (tools/tech_relationships.py VENDORS["shopify"]).
For Shopify the organisation's live pages must also still load Shopify (seen on the buyer's own site, today).
"""
import argparse, collections, csv, glob, gzip, hashlib, json, os, random, re, sys, threading, time, urllib.parse
from concurrent.futures import ThreadPoolExecutor

csv.field_size_limit(1 << 30)
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import cc_clients as CCL  # noqa: E402  (index access, archive reads)
import tech_relationships as T  # noqa: E402  (vetted vendor table, portal reader)

INC = CCL.INC
TPAGES = os.path.join(INC, "claude_cc_tenant_pages.csv.gz")
SHOPR = os.path.join(INC, "claude_cc_shopify_redirects.csv.gz")
CANDS = os.path.join(INC, "claude_tenant_candidates.csv.gz")
TDONE = os.path.join(INC, "claude_cc_tenant_extract_done.tsv")
CAND_COLS = ["cand_key", "vendor_key", "name", "website", "evidence_url", "capture", "name_basis", "website_basis", "slug", "extra"]
SCOPE = {"shopify": ("CA", "US")}  # countries whose customers contract with the vendor's Canadian company; default: Canada only (until the vendor's terms are read)
# registered domains of the vetted customer portals (from the vendor table) + the extra TLD forms its host patterns accept
EXTRA = {"jane": ["janeapp.co.uk", "janeapp.com.au"], "absorb": ["myabsorb.com.au"], "d2l": ["desire2learn.com"]}


def portal_domains():
    out = {}
    for k, v in T.VENDORS.items():
        if v.get("kind") != "portal":
            continue
        for pat in v.get("cc") or []:
            if pat.startswith("*."):
                out[pat[2:].lower()] = k
            else:  # path form, e.g. app.amilia.com/store/
                h = pat.split("/")[0].lower()
                out[".".join(h.split(".")[-2:])] = k
        for d in EXTRA.get(k, []):
            out[d] = k
    return out


def duck():
    import duckdb
    con = duckdb.connect()
    ver = tuple(int(x) for x in re.findall(r"\d+", duckdb.__version__)[:2])
    for st in ("INSTALL httpfs", "LOAD httpfs", "SET threads=4", "SET http_retries=8", "SET http_retry_wait_ms=2000",
               "SET http_timeout=%d" % (300 if ver >= (1, 1) else 300000), "SET enable_progress_bar=false", "SET enable_object_cache=true"):
        try:
            con.execute(st)
        except Exception as e:
            print("duckdb setting skipped: %s (%s)" % (st, str(e)[:80]), flush=True)
    return con


def file_range(con, url, col):
    """(min, max) of a column over the whole file from the parquet footer, or (None, None)"""
    try:
        r = con.execute("SELECT min(stats_min_value), max(stats_max_value) FROM parquet_metadata('%s') WHERE path_in_schema = '%s'" % (url, col)).fetchone()
        return r[0], r[1]
    except Exception as e:
        print("metadata failed:", str(e)[:120], flush=True)
        return None, None


def index(a):
    """one or several crawls ('last:N'): the shard files are appended to, and merge-index unions them"""
    for spec in CCL.crawl_ids(a.crawl):
        try:
            cid, wpaths = CCL.newest_crawl(spec)
        except SystemExit as e:
            print("crawl %s skipped: %s" % (spec, e), flush=True)
            continue
        _index_one(a, cid, wpaths)


def _index_one(a, cid, wpaths):
    k, n = CCL.shard_of(a)
    raw = CCL.http_get(CCL.CC + "crawl-data/%s/cc-index-table.paths.gz" % cid, tries=3)
    dpaths = sorted(l.strip() for l in gzip.decompress(raw).decode().split("\n") if "subset=crawldiagnostics/" in l and l.strip().endswith(".parquet"))
    con = duck()
    doms = portal_domains()
    os.makedirs("out", exist_ok=True)
    print("crawl %s: %d warc parts, %d diagnostics parts; shard %d/%d; portal domains: %s" % (cid, len(wpaths), len(dpaths), k, n, ", ".join(sorted(doms))), flush=True)
    # 1. portal pages. Every registered domain sits in one index part; the footer statistics of a part say whether a domain can be in it.
    # The archive refuses requests for minutes at a time (first run 2026-11-10: 5 of 300 parts unread, eScribe and Absorb missing), so a part
    # that fails is put back in the queue and read again after a pause, up to 6 rounds.
    want = {v.strip() for v in (a.vendors or "").split(",") if v.strip()}
    if want:
        doms = {d: v for d, v in doms.items() if v in want}
    best, t0, nrows = {}, time.time(), 0
    queue, unread = [(i, p, None) for i, p in enumerate(wpaths[k::n])], []
    for rnd in range(6):
        if not queue:
            break
        if rnd:
            print("round %d: %d parts to read again after a pause" % (rnd + 1, len(queue)), flush=True)
            time.sleep(60 * rnd + random.uniform(0, 30))
        nxt = []
        for i, p, todo in queue:
            url = CCL.CC + p
            if todo is None:
                lo, hi = file_range(con, url, "url_host_registered_domain")
                if lo is None:
                    nxt.append((i, p, None))
                    continue
                todo = [d for d in doms if lo <= d <= hi]
            left = []
            for d in todo:
                q = ("SELECT url, url_host_name, url_path, CAST(fetch_time AS VARCHAR), warc_filename, warc_record_offset, warc_record_length FROM read_parquet('%s') "
                     "WHERE url_host_registered_domain = '%s' AND fetch_status = 200 AND content_mime_detected = 'text/html' AND length(url_path) <= 80") % (url, d)
                try:
                    got = con.execute(q).fetchall()
                except Exception as e:
                    print("part %d %s failed (round %d): %s" % (i, d, rnd + 1, str(e)[:140]), flush=True)
                    left.append(d)
                    time.sleep(10)
                    continue
                nrows += len(got)
                for r in got:
                    for vkey, slug, purl in T.portal_hits(r[0]):
                        key = (vkey, slug)
                        path = r[2] or "/"
                        rank = (0 if path in ("/", "") else 1 if (vkey == "d2l" and path.startswith("/d2l/login")) else 2, len(path))
                        if key not in best or rank < best[key][0]:
                            best[key] = (rank, [vkey, slug, purl] + list(r) + [cid])
                if got:
                    print("%s part %d: %s %d pages (portals so far %d, %.0f s)" % (time.strftime("%H:%M:%S"), i, d, len(got), len(best), time.time() - t0), flush=True)
            if left:
                nxt.append((i, p, left))
        queue = nxt
    unread = ["%d:%s" % (i, ",".join(todo) if todo else "all") for i, p, todo in queue]
    if unread:
        print("UNREAD after 6 rounds (run the index again for these): %s" % "; ".join(unread), flush=True)
    first = not os.path.exists("out/tenant_pages_%d.csv" % k)
    with open("out/tenant_pages_%d.csv" % k, "a", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        if first:
            w.writerow(["vendor_key", "slug", "portal_url", "url", "host", "path", "fetch_time", "warc_filename", "warc_record_offset", "warc_record_length", "crawl"])
        for _, row in best.values():
            w.writerow(row)
    print("shard %d: %d portal pages read from the index, %d distinct customer portals: %s" % (k, nrows, len(best), dict(collections.Counter(v[1][0] for v in best.values()))), flush=True)
    # 2. Shopify: <store>.myshopify.com answering with a redirect to the store's own domain
    red, t0 = {}, time.time()
    queue = [(i, p) for i, p in enumerate(dpaths[k::n])] if (not want or "shopify" in want) else []
    for rnd in range(6):
        if not queue:
            break
        if rnd:
            print("round %d: %d diagnostics parts to read again after a pause" % (rnd + 1, len(queue)), flush=True)
            time.sleep(60 * rnd + random.uniform(0, 30))
        nxt = []
        for i, p in queue:
            url = CCL.CC + p
            lo, hi = file_range(con, url, "url_host_registered_domain")
            if lo is None:
                nxt.append((i, p))
                continue
            if not (lo <= "myshopify.com" <= hi):
                continue
            q = ("SELECT url_host_name, fetch_redirect, CAST(fetch_time AS VARCHAR), fetch_status FROM read_parquet('%s') "
                 "WHERE url_host_registered_domain = 'myshopify.com' AND fetch_status IN (301, 302, 307, 308) AND length(url_path) <= 1 AND fetch_redirect IS NOT NULL") % url
            try:
                got = con.execute(q).fetchall()
            except Exception as e:
                print("diagnostics part %d failed (round %d): %s" % (i, rnd + 1, str(e)[:160]), flush=True)
                nxt.append((i, p))
                time.sleep(10)
                continue
            for h, target, ft, st in got:
                th = CCL.base((urllib.parse.urlparse(target or "").hostname or "").lower())
                if not th or "." not in th or th.endswith("myshopify.com") or th.endswith("shopify.com") or th.endswith("shopifypreview.com"):
                    continue
                red.setdefault(h, (h, target, th, ft, st, cid))
            if got:
                print("%s diagnostics part %d: %d redirect rows (stores with their own domain so far %d, %.0f s)" % (time.strftime("%H:%M:%S"), i, len(got), len(red), time.time() - t0), flush=True)
        queue = nxt
    if queue:
        print("UNREAD diagnostics parts after 6 rounds: %s" % ", ".join(str(i) for i, p in queue), flush=True)
    first = not os.path.exists("out/shopify_redirects_%d.csv" % k)
    with open("out/shopify_redirects_%d.csv" % k, "a", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        if first:
            w.writerow(["store_host", "redirect", "own_host", "fetch_time", "status", "crawl"])
        w.writerows(red.values())
    print("shard %d: %d Shopify stores redirecting to their own domain" % (k, len(red)), flush=True)


def merge_index(a):
    rows, red = {}, {}
    if os.path.exists(TPAGES):  # union with the pages already on main: a re-run for a few vendors or parts adds, never replaces
        with gzip.open(TPAGES, "rt", encoding="utf-8", newline="") as fh:
            for r in csv.DictReader(fh):
                rows[(r["vendor_key"], r["slug"])] = r
    if os.path.exists(SHOPR):
        with gzip.open(SHOPR, "rt", encoding="utf-8", newline="") as fh:
            for r in csv.DictReader(fh):
                red[r["own_host"]] = r
    for f in sorted(glob.glob(os.path.join(a.dir, "tenant_pages_*.csv"))):
        for r in csv.DictReader(open(f, encoding="utf-8")):
            key = (r["vendor_key"], r["slug"])
            if key not in rows or len(r["path"] or "/") < len(rows[key]["path"] or "/"):
                rows[key] = r
    for f in sorted(glob.glob(os.path.join(a.dir, "shopify_redirects_*.csv"))):
        for r in csv.DictReader(open(f, encoding="utf-8")):
            red.setdefault(r["own_host"], r)
    if rows:
        with gzip.open(TPAGES, "wt", encoding="utf-8", newline="") as fh:
            w = csv.DictWriter(fh, fieldnames=list(next(iter(rows.values())).keys()))
            w.writeheader()
            for key in sorted(rows):
                w.writerow(rows[key])
    if red:
        with gzip.open(SHOPR, "wt", encoding="utf-8", newline="") as fh:
            w = csv.DictWriter(fh, fieldnames=list(next(iter(red.values())).keys()))
            w.writeheader()
            for key in sorted(red):
                w.writerow(red[key])
    print("tenant index: %d customer portals (%s); %d Shopify stores with their own domain" % (len(rows), dict(collections.Counter(k[0] for k in rows)), len(red)))


_local = threading.local()


def _fake_fetch(url, gap=1.0, limit=2_000_000, _hops=0):
    b = getattr(_local, "pages", {}).get(url)
    return (200, url, b, "text/html") if b is not None else (0, url, "", "")


def extract(a):
    """portal pages -> candidates (organisation name + its own website, as the portal page itself shows them)"""
    k, n = CCL.shard_of(a)
    T.fetch, T.allowed = _fake_fetch, (lambda u: True)  # portal_info reads the archived page; nothing is requested from the vendor's platform
    done = set()
    if os.path.exists(TDONE):
        for l in open(TDONE, encoding="utf-8"):
            q = l.rstrip("\n").split("\t")
            if len(q) > 2 and (q[2] != "unreadable" or (len(q) > 3 and q[3].isdigit() and int(q[3]) >= 4)):
                done.add(q[0])
    tries = {}
    if os.path.exists(TDONE):
        for l in open(TDONE, encoding="utf-8"):
            q = l.rstrip("\n").split("\t")
            tries[q[0]] = int(q[3]) if len(q) > 3 and q[3].isdigit() else 1
    pages = []
    if os.path.exists(TPAGES):
        with gzip.open(TPAGES, "rt", encoding="utf-8", newline="") as fh:
            for r in csv.DictReader(fh):
                ck = "t:%s:%s" % (r["vendor_key"], r["slug"])
                if ck in done or int(hashlib.sha1(ck.encode()).hexdigest(), 16) % n != k:
                    continue
                pages.append((ck, r))
    random.Random(11).shuffle(pages)
    if a.limit:
        pages = pages[:a.limit]
    os.makedirs("out", exist_ok=True)
    deadline = time.time() + a.minutes * 60
    stats, lock = collections.Counter(), threading.Lock()
    fc = open("out/tenant_cands_%d.jsonl" % k, "a", encoding="utf-8")
    fd = open("out/tenant_extract_done_%d.tsv" % k, "a", encoding="utf-8")
    print("shard %d/%d: %d customer portals to read" % (k, n, len(pages)), flush=True)

    def one(item):
        ck, r = item
        if time.time() > deadline:
            return
        page, why = CCL.warc_html(r["warc_filename"], int(r["warc_record_offset"]), int(r["warc_record_length"]))
        info, res = None, "unreadable"
        if page is not None:
            _local.pages = {r["portal_url"]: page}
            try:
                info, res = T.portal_info(r["vendor_key"], r["portal_url"])
            except Exception as e:
                info, res = None, "error:" + type(e).__name__
            _local.pages = {}
        with lock:
            stats["portals"] += 1
            stats[res if page is not None else "unreadable:" + why] += 1
            if info and info.get("website"):
                stats["with_website"] += 1
                fc.write(json.dumps({"cand_key": ck, "vendor_key": r["vendor_key"], "name": info["name"], "website": info["website"], "evidence_url": r["url"],
                                     "capture": (r.get("fetch_time") or "")[:10], "name_basis": info.get("name_basis") or "", "website_basis": info.get("website_basis") or "",
                                     "slug": info.get("slug") or r["slug"],
                                     "extra": json.dumps({"page_title": info.get("page_title"), "practitioners_listed": info.get("practitioners_listed"),
                                                          "warc": "%s:%s:%s" % (r["warc_filename"], r["warc_record_offset"], r["warc_record_length"])}, ensure_ascii=False)}, ensure_ascii=False) + "\n")
            fd.write("%s\t%s\t%s\t%d\n" % (ck, CCL.TODAY, "unreadable" if page is None else res, tries.get(ck, 0) + 1))
            if stats["portals"] % 500 == 0:
                print(time.strftime("%H:%M:%S"), dict(stats), flush=True)
    with ThreadPoolExecutor(a.workers) as ex:
        list(ex.map(one, pages))
    fc.close(); fd.close()
    print("finished", dict(stats), flush=True)


def known_domains():
    """registrable-ish hosts we already hold as a lead or a delivered buyer: not worth a second crawl"""
    known = set()
    for p in (os.path.join(INC, "claude_buyer_leads.csv"), CCL.LEADS_CC):
        if os.path.exists(p):
            for r in csv.DictReader(open(p, encoding="utf-8", errors="replace")):
                h = CCL.base((urllib.parse.urlparse(r.get("website") or "").hostname or "").lower())
                if h:
                    known.add(h)
    rp = os.path.join(CCL.ROOT, "coord/results/ranked/ranked_buyers.csv.gz")
    if os.path.exists(rp):
        with gzip.open(rp, "rt", encoding="utf-8", newline="") as fh:
            rd = csv.reader(fh)
            head = next(rd)
            i = head.index("buyer_website") if "buyer_website" in head else -1
            for row in rd:
                if i >= 0 and i < len(row) and row[i]:
                    h = CCL.base((urllib.parse.urlparse(row[i] if "//" in row[i] else "https://" + row[i]).hostname or "").lower())
                    if h:
                        known.add(h)
    return known


def merge(a):
    seen = {}
    for f in [TDONE] + sorted(glob.glob(os.path.join(a.dir, "tenant_extract_done_*.tsv"))):
        if os.path.exists(f):
            for l in open(f, encoding="utf-8"):
                q = l.rstrip("\n").split("\t")
                if q and q[0]:
                    seen[q[0]] = l.rstrip("\n")
    if seen:
        with open(TDONE, "w", encoding="utf-8") as f:
            for u in sorted(seen):
                f.write(seen[u] + "\n")
    cands = {}
    if os.path.exists(CANDS):
        with gzip.open(CANDS, "rt", encoding="utf-8", newline="") as fh:
            cands = {r["cand_key"]: r for r in csv.DictReader(fh)}
    before = len(cands)
    by_host = {CCL.base((urllib.parse.urlparse(r["website"]).hostname or "").lower()): k for k, r in cands.items()}
    known = known_domains()
    add = collections.Counter()
    for f in sorted(glob.glob(os.path.join(a.dir, "tenant_cands_*.jsonl"))):  # portal customers first: they carry the organisation's name
        for l in open(f, encoding="utf-8"):
            try:
                r = json.loads(l)
            except ValueError:
                continue
            h = CCL.base((urllib.parse.urlparse(r["website"]).hostname or "").lower())
            if not h or h in known or h in by_host or r["cand_key"] in cands:
                add["skipped (known or duplicate)"] += 1
                continue
            cands[r["cand_key"]] = {c: r.get(c, "") for c in CAND_COLS}
            by_host[h] = r["cand_key"]
            add[r["vendor_key"]] += 1
    if os.path.exists(SHOPR):
        with gzip.open(SHOPR, "rt", encoding="utf-8", newline="") as fh:
            for r in csv.DictReader(fh):
                h, store = r["own_host"], r["store_host"].split(".")[0]
                ck = "t:shopify:" + store
                if not h or h in known or h in by_host or ck in cands or CCL.VENDOR_SKIP.search(h) or CCL.SKIP.search(h):
                    continue
                cands[ck] = {"cand_key": ck, "vendor_key": "shopify", "name": "", "website": "https://%s/" % h, "evidence_url": "https://%s/" % r["store_host"],
                             "capture": (r.get("fetch_time") or "")[:10], "name_basis": "", "website_basis": "the store's myshopify.com address redirects to this domain (archive, HTTP %s)" % r.get("status"),
                             "slug": store, "extra": json.dumps({"redirect": r.get("redirect"), "crawl": r.get("crawl")}, ensure_ascii=False)}
                by_host[h] = ck
                add["shopify"] += 1
    with gzip.open(CANDS, "wt", encoding="utf-8", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=CAND_COLS)
        w.writeheader()
        for k in sorted(cands):
            w.writerow({c: cands[k].get(c, "") for c in CAND_COLS})
    print("tenant candidates: %d (+%d this run: %s); portals read so far %d" % (len(cands), len(cands) - before, dict(add), len(seen)))


def lead_row(rec):
    """the row tools/lead_scanner.py --bridge would write for this lead (same key, same columns)"""
    name = rec["publisher"].strip()
    key = "lead:" + hashlib.sha1(("%s|%s" % (rec["domain"], name.lower())).encode()).hexdigest()[:16]
    return key, {"buyer_key": key, "buyer_name": name, "website": rec["website"], "canadian_vendor_rows": 1, "example_vendor": rec["vendor"],
                 "canada_field_value": "%s=%s" % (rec["canada_field"], rec["canada_value"]), "evidence_dataset": rec["dataset_url"],
                 "latest_record_date": (rec.get("row") or {}).get("record_date") or ""}


def merge_accepted(a):
    recs = []
    for f in sorted(glob.glob(os.path.join(a.dir, "tenant_leads_*.jsonl"))):
        for l in open(f, encoding="utf-8"):
            try:
                recs.append(json.loads(l))
            except ValueError:
                pass
    prev, pdet = {}, {}
    if os.path.exists(CCL.LEADS_CC):
        prev = {r["buyer_key"]: r for r in csv.DictReader(open(CCL.LEADS_CC, encoding="utf-8"))}
    if os.path.exists(CCL.DETAILS_CC):
        for l in gzip.open(CCL.DETAILS_CC, "rt", encoding="utf-8"):
            try:
                o = json.loads(l)
                pdet[o["key"]] = o
            except (ValueError, KeyError):
                pass
    main = set()
    mp = os.path.join(INC, "claude_buyer_leads.csv")
    if os.path.exists(mp):
        main = {r["buyer_key"] for r in csv.DictReader(open(mp, encoding="utf-8", errors="replace"))}
    new = collections.Counter()
    for rec in recs:
        key, row = lead_row(rec)
        if key in main or key in prev:
            continue
        prev[key] = row
        rr = rec.get("row") or {}
        pdet[key] = {"key": key, "platform": "tech_tenant_cc", "record_url": rec["dataset_url"], "vendor": rec["vendor"], "record_date": rr.get("record_date") or "", "title": "",
                     "vendor_address": "%s (as printed on %s)" % (rr.get("vendor_hq_quote") or "", rr.get("vendor_hq_url") or ""), "vendor_trade_name": rr.get("vendor_trade_name") or "",
                     "buyer_address_evidence": rr.get("buyer_address_quote") or "", "buyer_address_evidence_url": rr.get("buyer_address_url") or "", "buyer_country_evidence": rr.get("buyer_country") or "",
                     "contracting_scope": rr.get("contracting_scope") or "", "service_seen": rr.get("service_seen") or "", "portal_slug": rr.get("portal_slug") or "", "capture": rr.get("capture") or ""}
        new[rr.get("vendor_key") or "?"] += 1
    with open(CCL.LEADS_CC, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=CCL.LEAD_COLS)
        w.writeheader()
        for k in sorted(prev):
            w.writerow({c: prev[k].get(c, "") for c in CCL.LEAD_COLS})
    with gzip.open(CCL.DETAILS_CC, "wt", encoding="utf-8") as f:
        for k in sorted(pdet):
            f.write(json.dumps(pdet[k], ensure_ascii=False) + "\n")
    print("tenant leads accepted this run: %d (%s); %d buyers in %s" % (sum(new.values()), dict(new), len(prev), os.path.basename(CCL.LEADS_CC)))


def main():
    ap = argparse.ArgumentParser()
    sub = ap.add_subparsers(dest="cmd", required=True)
    p = sub.add_parser("index"); p.add_argument("--shard", default="0/1"); p.add_argument("--crawl", default="auto"); p.add_argument("--vendors", default="", help="comma-separated vendor keys (default: every vetted portal vendor + Shopify redirects)")
    p = sub.add_parser("merge-index"); p.add_argument("dir")
    p = sub.add_parser("extract"); p.add_argument("--shard", default="0/1"); p.add_argument("--minutes", type=float, default=120); p.add_argument("--workers", type=int, default=4); p.add_argument("--limit", type=int, default=0)
    p = sub.add_parser("merge"); p.add_argument("dir")
    p = sub.add_parser("merge-accepted"); p.add_argument("dir")
    a = ap.parse_args()
    {"index": index, "merge-index": merge_index, "extract": extract, "merge": merge, "merge-accepted": merge_accepted}[a.cmd](a)


if __name__ == "__main__":
    main()
