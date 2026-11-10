#!/usr/bin/env python3
"""Row factory, step 2 (cloud): the role mailbox of every NEW buyer, read on the buyer's own site.

tools/cc_clients.py and tools/cc_tenants.py find new buyers of Canada-located vendors. A buyer becomes a delivered row only with a mailbox the
organisation publishes itself. This runs tools/ap_crawler.crawl() — the same no-AI reader that ran on the owner's Mac — from GitHub runners:
robots.txt respected, at most one request per second per site, a small page budget, invoicing / AP / supplier / purchasing / finance mailboxes
first and, when the site publishes none, its general role mailbox (owner rule 2026-10-28). Never a named person, never a pattern-built address,
blocked sites are recorded as blocked and left alone.

  python3 tools/lead_crawl.py --shard K/N [--minutes 150] [--max-pages 25] [--workers 40]            leads of claude_buyer_leads_cc.csv
  python3 tools/lead_crawl.py --candidates data/incoming/claude/claude_tenant_candidates.csv.gz --shard K/N   candidates (tools/cc_tenants.py)
  python3 tools/lead_crawl.py --merge SHARD_DIR [--tenants]                                          append shard outputs to the files on main
Leads mode      in : claude_buyer_leads_cc.csv, resume claude_lead_crawl_done.tsv            out: out/lead_rows_<K>.csv, out/lead_done_<K>.tsv
Candidates mode in : claude_tenant_candidates.csv.gz, resume claude_tenant_crawl_done.tsv    out: out/lead_rows_<K>.csv, out/tenant_leads_<K>.jsonl,
                     out/tenant_done_<K>.tsv
  A candidate (an organisation with a live account at a Canada-HQ software vendor) is ACCEPTED only when its own site gives
  (1) a role mailbox on its own domain, (2) a postal address in a country the vendor's Canadian company contracts with (Canada; Canada or the
  United States for Shopify — tools/cc_tenants.SCOPE), the address quote and page kept, (3) a name, and (4) for Shopify: the store's pages still
  load Shopify today. Everything else is recorded with its reason and never becomes a lead.
Rows go to data/incoming/claude/claude_buyer_ap_results_cccrawl01.csv, where the referee re-fetches every evidence page before a mailbox counts.
"""
import argparse, collections, csv, glob, gzip, hashlib, json, os, re, sys, threading, time, urllib.parse
from concurrent.futures import ThreadPoolExecutor, wait

csv.field_size_limit(1 << 30)
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import ap_crawler as C  # noqa: E402

INC = os.path.join(ROOT, "data/incoming/claude")
DONE = os.path.join(INC, "claude_lead_crawl_done.tsv")
TDONE = os.path.join(INC, "claude_tenant_crawl_done.tsv")
OUT = os.path.join(INC, "claude_buyer_ap_results_cccrawl01.csv")
TODAY = time.strftime("%Y-%m-%d")
US_ADDR = re.compile(r"(?<![A-Za-z0-9])([A-Z][A-Za-z.'\- ]{2,30}),?\s+(AL|AK|AZ|AR|CA|CO|CT|DE|FL|GA|HI|ID|IL|IN|IA|KS|KY|LA|ME|MD|MA|MI|MN|MS|MO|MT|NE|NV|NH|NJ|NM|NY|NC|ND|OH|OK|OR|PA|RI|SC|SD|TN|TX|UT|VT|VA|WA|WV|WI|WY|DC)"
                     r"\.?,?\s+(\d{5})(?:-\d{4})?(?![A-Za-z0-9])")
GB_ADDR = re.compile(r"(?<![A-Za-z0-9])([A-Z][A-Za-z.'\- ]{2,30}),?\s+([A-Z]{1,2}\d[A-Z\d]?\s?\d[A-Z]{2})(?![A-Za-z0-9])")
AU_ADDR = re.compile(r"(?<![A-Za-z0-9])([A-Z][A-Za-z.'\- ]{2,30}),?\s+(NSW|VIC|QLD|TAS|ACT)\s+(\d{4})(?!\d)")
SFDONE = os.path.join(INC, "claude_site_facts_done.tsv")
_tl = threading.local()


def ok_mailbox(e):
    """the validator's own rule (tools/validate_returns.py): a first.last-shaped local part without a role word is treated as a person"""
    return bool(C.EMAIL.match(e or "")) and not (C.PERSONAL.match(e.split("@")[0]) and not C.ROLE_HINT.search(e.split("@")[0]))


GENERIC_SITE_WORDS = {"home", "accueil", "welcome", "bienvenue", "services", "service", "canada", "canadian", "online", "group", "groupe", "company", "solutions", "official", "site", "website",
                      "shop", "store", "boutique", "contact", "about", "page", "best", "quality", "professional", "toronto", "montreal", "vancouver", "calgary", "ottawa", "edmonton", "quebec"}


def site_name_for(host, og, title, T):
    """the name an organisation gives itself on its own home page, kept only when it agrees with its own domain (a slogan such as
    "Best Plumber in Toronto | 24/7 Service" is not a name): og:site_name first, then the parts of <title>"""
    import unicodedata
    label = re.sub(r"[^a-z0-9]", "", (T.base_domain(T.nowww(host or "")) or "").split(".")[0].lower())
    cands = []
    for s in (og, title):
        if s:
            cands += [q.strip(" -–—|:·•") for q in re.split(r"\s+[|–—:·•]\s+|\s+-\s+|\s*\|\s*", s)]
    for c in cands:
        if not (2 <= len(c) <= 80) or T.BAD_TITLE.search(c):
            continue
        flat = unicodedata.normalize("NFKD", c).encode("ascii", "ignore").decode().lower()
        n = re.sub(r"[^a-z0-9]", "", flat)
        toks = [t for t in re.findall(r"[a-z0-9]{4,}", flat) if t not in GENERIC_SITE_WORDS]
        if (len(label) >= 4 and label in n) or (len(n) >= 4 and n in label) or any(t in label for t in toks):
            return re.sub(r"\s+", " ", c).strip()
    return ""


def install_hooks():
    """what the candidate rules need from the pages ap_crawler reads anyway: the site's own name, its postal address, the vendor's assets"""
    import cc_clients as CCL
    import tech_relationships as T
    shop_rx = T.VENDORS["shopify"]["asset_re_c"]
    orig_visible, orig_note = C.visible, C.note_ap_page

    def visible2(raw):
        st = getattr(_tl, "st", None)
        if st is not None:
            try:
                if not st.get("name") and st.get("name_tries", 0) < 3:  # the home page first; two more pages when it names nothing usable
                    st["name_tries"] = st.get("name_tries", 0) + 1
                    title, meta = T.page_meta(raw)
                    st["name"] = site_name_for(st.get("host") or "", meta.get("og:site_name"), title, T)
                    st.setdefault("title", (title or "")[:200])
                if "shopify" not in st:
                    m = shop_rx.search(raw)
                    if m:
                        st["shopify"] = re.sub(r"\s+", " ", raw[max(0, m.start() - 30):m.end() + 50])[:160]
            except Exception:
                pass
        return orig_visible(raw)

    def note2(key, name, site, final, text, is_pdf):
        st = getattr(_tl, "st", None)
        if st is not None and "addr" not in st and not is_pdf:
            try:
                m, cc = None, ""
                for cc_, rx in (("CA", CCL.ADDR), ("US", US_ADDR), ("GB", GB_ADDR), ("AU", AU_ADDR)):
                    m = rx.search(text)
                    if m:
                        cc = cc_
                        break
                if m:
                    st["addr"] = (cc, re.sub(r"^\S*\s", "", text[max(0, m.start() - 110):m.end()].strip())[-200:], final)
                if st.get("shopify") and "shopify_url" not in st:
                    st["shopify_url"] = final
            except Exception:
                pass
        return orig_note(key, name, site, final, text, is_pdf)
    C.visible, C.note_ap_page = visible2, note2
    return T


FACTS = os.path.join(INC, "claude_lead_site_facts.jsonl.gz")


def facts_line(key, site, st):
    """what the buyer's own pages say about the buyer: its name (og:site_name / title of the home page) and its postal address (quote + page).
    contrib/claude/rank_buyers/rank.py uses it for the bill-to name and address of a lead that only carried a domain."""
    import cc_clients as CCL
    o = {"key": key, "site": site, "date": TODAY, "site_name": st.get("name") or "", "title": st.get("title") or ""}
    if st.get("addr"):
        o.update(address_country=st["addr"][0], address_quote=st["addr"][1], address_url=st["addr"][2], address=CCL.address_from(st["addr"][1]))
    return json.dumps(o, ensure_ascii=False) + "\n"


def run_pool(tasks, one, a, deadline, on_timeout):
    """a few sites answer so slowly that one thread can hold a runner for an hour (first cycle, 2026-11-10). When only stragglers are left and
    nothing finished for --straggler-seconds, they are recorded as "timeout" and the run ends; sites not started by the deadline stay queued."""
    ex = ThreadPoolExecutor(a.workers)
    def timed(t):
        t["_deadline"] = time.time() + a.site_seconds  # ap_crawler.crawl stops opening pages of this site after that
        return one(t)
    futs = {ex.submit(timed, t): t for t in tasks}
    pending, last, tail = set(futs), time.time(), 0
    while pending:
        fin, pending = wait(pending, timeout=min(30, max(1, a.straggler_seconds / 3)))
        if fin:
            last = time.time()
        if len(pending) <= a.workers and not tail:
            tail = time.time()  # only sites already being read are left
        if (len(pending) <= a.workers and (time.time() - last > a.straggler_seconds or time.time() - tail > a.site_seconds + a.straggler_seconds)) or time.time() > deadline + 300:
            for f in pending:
                if f.running():
                    on_timeout(futs[f])
            break
    return len(pending)


def shard_ok(h, k, n):
    return int(hashlib.sha1(h.encode()).hexdigest(), 16) % n == k


def host_of(site):
    site = (site or "").strip()
    return (urllib.parse.urlparse(site if "//" in site else "https://" + site).hostname or "").lower() if site else ""


def leads_mode(a, k, n):
    install_hooks()
    # 2026-11-10 (rule "r2"): front-office role mailboxes (sales@, service@, orders@ …) count when a site publishes nothing better; the sites that
    # gave "nothing_found" under the first rule are read once more (their done line has no "r2" mark)
    done = set()
    if os.path.exists(DONE):
        for l in open(DONE, encoding="utf-8"):
            q = l.rstrip("\n").split("\t")
            if q and q[0] and not (len(q) > 2 and q[2] == "nothing_found" and "r2" not in q[5:]):
                done.add(q[0])
    # 2026-11-10: the leads found from the owner's Mac (claude_buyer_leads.csv) can be read here too: 33,600 of them have a website and no
    # mailbox row yet, and the Mac's own crawler is off. A lead that already has a mailbox row in any lane's results file is not read again.
    known = set()
    for p in glob.glob(os.path.join(ROOT, "data/incoming/*/*buyer_ap_results*.csv")):
        try:
            with open(p, encoding="utf-8", errors="replace", newline="") as f:
                for r in csv.DictReader(f):
                    if r.get("buyer_key") and (r.get("ap_email") or "").strip():
                        known.add(r["buyer_key"])
        except Exception:
            pass
    sites = {}  # websites found later for leads that had none (tools/lead_sites.py: Wikidata official website, exact name match)
    lw = os.path.join(INC, "claude_lead_websites.csv")
    if os.path.exists(lw):
        for r in csv.DictReader(open(lw, encoding="utf-8")):
            sites[r["buyer_key"]] = r["website"]
    tasks, hosts, skipped = [], set(), 0
    for fi, path in enumerate(x.strip() for x in a.leads.split(",") if x.strip()):
        if not os.path.exists(path):
            continue
        for r in csv.DictReader(open(path, encoding="utf-8", errors="replace")):
            h = host_of(r.get("website") or sites.get(r["buyer_key"]))
            if not h or "." not in h or r["buyer_key"] in done or h in hosts or not shard_ok(h, k, n):
                continue
            if r["buyer_key"] in known:
                skipped += 1
                continue
            hosts.add(h)
            try:
                nv = int(float(r.get("canadian_vendor_rows") or 1))
            except ValueError:
                nv = 1
            tasks.append({"task_id": "CC-" + r["buyer_key"].split(":")[-1][:10], "buyer_key": r["buyer_key"], "buyer_name": r.get("buyer_name") or h, "known_website": "https://%s/" % h,
                          "_n": nv, "_f": fi})
    tasks.sort(key=lambda t: (t["_f"], -t["_n"]))  # the first leads file first; within a file, buyers named by several Canadian vendors first
    print("leads with a mailbox row already (not read again): %d" % skipped, flush=True)
    if a.limit:
        tasks = tasks[:a.limit]
    print("shard %d/%d: %d new lead sites to read (%d done before)" % (k, n, len(tasks), len(done)), flush=True)
    deadline = time.time() + a.minutes * 60
    lock = threading.Lock()
    stats = {"sites": 0, "with_mailbox": 0, "rows": 0, "blocked": 0, "errors": 0}
    fr = open("out/lead_rows_%d.csv" % k, "a", newline="", encoding="utf-8")
    w = csv.DictWriter(fr, fieldnames=C.COLS, extrasaction="ignore")
    w.writeheader()
    fd = open("out/lead_done_%d.tsv" % k, "a", encoding="utf-8")
    ff = open("out/lead_facts_%d.jsonl" % k, "a", encoding="utf-8")

    def one(t):
        if time.time() > deadline:
            return
        st = {"host": host_of(t["known_website"])}
        _tl.st = st
        try:
            result, pages, rows = C.crawl(t, a.max_pages, general="any")
        except Exception as e:
            result, pages, rows = "error:%s" % type(e).__name__, 0, []
        _tl.st = None
        C.AP_PAGES.pop(t["buyer_key"], None)  # the walker's page memory is not needed here
        rows = [r for r in rows if ok_mailbox(r.get("ap_email"))]
        with lock:
            stats["sites"] += 1
            stats["with_mailbox"] += bool(rows)
            stats["rows"] += len(rows)
            stats["blocked"] += result == "blocked"
            stats["errors"] += str(result).startswith("error")
            w.writerows(rows)
            if rows and (st.get("name") or st.get("addr")):
                ff.write(facts_line(t["buyer_key"], t["known_website"], st))
            stats["front_office_role_only"] = stats.get("front_office_role_only", 0) + bool(rows and "front-office role mailbox" in (rows[0].get("notes") or ""))
            fd.write("%s\t%s\t%s\t%d\t%d\tr2\n" % (t["buyer_key"], TODAY, result, pages, len(rows)))
            if stats["sites"] % 200 == 0:
                fr.flush(); fd.flush()
                print(time.strftime("%H:%M:%S"), stats, flush=True)

    def on_timeout(t):
        with lock:
            fd.write("%s\t%s\ttimeout\t0\t0\tr2\n" % (t["buyer_key"], TODAY))
            stats["errors"] += 1
    left = run_pool(tasks, one, a, deadline, on_timeout)
    with lock:
        fr.close(); fd.close(); ff.close()
    print("finished", stats, "(stragglers left: %d)" % left, flush=True)


def candidates_mode(a, k, n):
    import cc_tenants as CT
    T = install_hooks()
    # candidates seen live by tools/credit_scan.py (a link to the organisation's Jane portal on its own page): the free single-practitioner
    # plan is ruled out on the portal itself, read at the end and only for candidates that passed everything else. All runners together stay
    # under 2 requests per second on the vendor's platform.
    _tfetch, _gap = T.fetch, max(1.0, n / 2.0)
    T.fetch = lambda url, gap=1.0, limit=2_000_000, _hops=0: _tfetch(url, max(gap, _gap), limit, _hops)

    def jane_ok(purl):
        try:
            info, _ = T.portal_info("jane", purl)
            return bool(info)
        except Exception:
            return False
    done = set()
    if os.path.exists(TDONE):  # candidates that gave "nothing_found" before the front-office role rule (no "r2" mark) are read once more
        for l in open(TDONE, encoding="utf-8"):
            q = l.rstrip("\n").split("\t")
            if q and q[0] and not (len(q) > 2 and q[2] == "nothing_found" and "r2" not in q[6:]):
                done.add(q[0])
    tasks, hosts = [], set()
    with gzip.open(a.candidates, "rt", encoding="utf-8", newline="") as fh:
        for r in csv.DictReader(fh):
            h = host_of(r.get("website"))
            if not h or "." not in h or r["cand_key"] in done or h in hosts or not shard_ok(h, k, n):
                continue
            if a.vendors and r["vendor_key"] not in a.vendors.split(","):
                continue
            hosts.add(h)
            tasks.append({"task_id": "TN-" + hashlib.sha1(r["cand_key"].encode()).hexdigest()[:10], "buyer_key": r["cand_key"], "buyer_name": r.get("name") or h,
                          "known_website": "https://%s/" % h, "_c": r})
    tasks.sort(key=lambda t: (t["_c"]["vendor_key"] == "shopify", t["buyer_key"]))  # customer portals (organisation named by the portal) before stores
    if a.limit:
        tasks = tasks[:a.limit]
    print("shard %d/%d: %d candidate sites to read (%d done before)" % (k, n, len(tasks), len(done)), flush=True)
    deadline = time.time() + a.minutes * 60
    lock = threading.Lock()
    stats = collections.Counter()
    fr = open("out/lead_rows_%d.csv" % k, "a", newline="", encoding="utf-8")
    w = csv.DictWriter(fr, fieldnames=C.COLS, extrasaction="ignore")
    w.writeheader()
    fl = open("out/tenant_leads_%d.jsonl" % k, "a", encoding="utf-8")
    fd = open("out/tenant_done_%d.tsv" % k, "a", encoding="utf-8")
    ff = open("out/lead_facts_%d.jsonl" % k, "a", encoding="utf-8")

    def one(t):
        if time.time() > deadline:
            return
        c, st = t["_c"], {"host": host_of(t["known_website"])}
        _tl.st = st
        try:
            result, pages, rows = C.crawl(t, a.max_pages, general="any")
        except Exception as e:
            result, pages, rows = "error:%s" % type(e).__name__, 0, []
        _tl.st = None
        C.AP_PAGES.pop(t["buyer_key"], None)
        rows = [r for r in rows if ok_mailbox(r.get("ap_email"))]
        vkey = c["vendor_key"]
        scope = CT.SCOPE.get(vkey, ("CA",))
        name = (c.get("name") or st.get("name") or "").strip()
        try:
            ex = json.loads(c.get("extra") or "{}")
        except ValueError:
            ex = {}
        if not rows:
            res = result if result != "found" else "no_role_mailbox"
        elif "addr" not in st:
            res = "no_address"
        elif st["addr"][0] not in scope:
            res = "out_of_scope:" + st["addr"][0]
        elif vkey == "shopify" and not st.get("shopify"):
            res = "service_not_seen"
        elif not name:
            res = "no_name"
        elif vkey == "jane" and ex.get("portal_check") and not jane_ok(ex.get("portal") or "https://%s/" % (c.get("slug") or "")):
            res = "free_plan_or_portal_unreadable"
        else:
            res = "accepted"
        rec = None
        if res == "accepted":
            site = t["known_website"]
            seen_url = st.get("shopify_url") or site
            row = {"portal_slug": c.get("slug") or "", "capture": c.get("capture") or "", "tenant_url": c.get("evidence_url") or "", "name_basis": c.get("name_basis") or ("og:site_name / title of the organisation's own home page" if not c.get("name") else ""),
                   "website_basis": c.get("website_basis") or "", "buyer_country": st["addr"][0], "buyer_address_quote": st["addr"][1], "buyer_address_url": st["addr"][2],
                   "service_seen": ("%s (in the page source of %s, %s)" % (st.get("shopify"), seen_url, TODAY)) if vkey == "shopify" else
                                   ("%s: %s — on the organisation's own page %s (read %s)" % (T.VENDORS[vkey]["name"], ex.get("portal") or ex.get("via") or "", ex.get("seen_on"), c.get("capture"))) if ex.get("seen_on") else
                                   "customer portal %s captured %s (Common Crawl)" % (c.get("evidence_url"), c.get("capture"))}
            rec = T.lead(vkey, name, site, seen_url if vkey == "shopify" else (c.get("evidence_url") or site), row)
            if vkey != "shopify" and c.get("capture"):  # a customer portal: the day the archive saw it; a store: today, on its own pages
                rec["row"]["observed_date"] = rec["row"]["record_date"] = c["capture"]
            key, _ = CT.lead_row(rec)
            for r in rows:
                r["buyer_key"], r["task_id"], r["org_name_as_found"] = key, "TN-" + key.split(":")[-1][:10], name
        with lock:
            stats["sites"] += 1
            stats[res.split(":")[0]] += 1
            stats["rows"] += len(rows) if rec else 0
            if rec:
                w.writerows(rows)
                fl.write(json.dumps(rec, ensure_ascii=False) + "\n")
                ff.write(facts_line(key, t["known_website"], dict(st, name=name)))
            fd.write("%s\t%s\t%s\t%d\t%d\t%s\tr2\n" % (t["buyer_key"], TODAY, res, pages, len(rows), vkey))
            if stats["sites"] % 200 == 0:
                fr.flush(); fd.flush(); fl.flush()
                print(time.strftime("%H:%M:%S"), dict(stats), flush=True)

    def on_timeout(t):
        with lock:
            fd.write("%s\t%s\ttimeout\t0\t0\t%s\tr2\n" % (t["buyer_key"], TODAY, t["_c"]["vendor_key"]))
            stats["timeout"] += 1
    left = run_pool(tasks, one, a, deadline, on_timeout)
    with lock:
        fr.close(); fd.close(); fl.close(); ff.close()
    print("finished", dict(stats), "(stragglers left: %d)" % left, flush=True)


def facts_mode(a, k, n):
    """Completeness pass over rows ALREADY delivered (owner 2026-11-09 20:48 EST: "complete data … all the details that go within an invoice"):
    33,136 delivered rows lacked a bill-to name and / or address. For every delivered row with a website and no address, read the home and
    contact pages (same polite reader) and keep what the organisation prints about itself: its name and its postal address, quoted, plus a
    better mailbox (invoicing / AP / finance / purchasing) when the row only has a general one. rank.py turns that into the bill-to block."""
    install_hooks()
    done = {l.split("\t")[0] for l in open(SFDONE, encoding="utf-8")} if os.path.exists(SFDONE) else set()
    have = set()
    if os.path.exists(FACTS):
        for l in gzip.open(FACTS, "rt", encoding="utf-8"):
            try:
                have.add(json.loads(l)["key"])
            except (ValueError, KeyError):
                pass
    tasks, hosts = [], set()
    with gzip.open(a.facts_ranked, "rt", encoding="utf-8", newline="") as fh:
        for r in csv.DictReader(fh):
            key = (r.get("keys") or "").split("|")[0]
            h = host_of(r.get("buyer_website"))
            if not r.get("email") or not key or key in done or key in have or not h or "." not in h or h in hosts or not shard_ok(h, k, n):
                continue
            if (r.get("buyer_address") or "").strip() and ((r.get("buyer_legal_name_as_published") or "").strip() or (r.get("buyer_trade_name_as_published") or "").strip()):
                continue  # bill-to already complete
            hosts.add(h)
            tasks.append({"task_id": "SF-" + hashlib.sha1(key.encode()).hexdigest()[:10], "buyer_key": key, "buyer_name": r.get("buyer") or h, "known_website": "https://%s/" % h,
                          "_general": (r.get("email_type") or "").startswith("general"), "_tier": r.get("tier") or ""})
    tasks.sort(key=lambda t: (t["_tier"] == "I", t["buyer_key"]))  # rows with a relationship record before the inferred ones
    if a.limit:
        tasks = tasks[:a.limit]
    print("shard %d/%d: %d delivered rows without a complete bill-to block to read (%d done before)" % (k, n, len(tasks), len(done)), flush=True)
    deadline = time.time() + a.minutes * 60
    lock = threading.Lock()
    stats = collections.Counter()
    fr = open("out/lead_rows_%d.csv" % k, "a", newline="", encoding="utf-8")
    w = csv.DictWriter(fr, fieldnames=C.COLS, extrasaction="ignore")
    w.writeheader()
    ff = open("out/lead_facts_%d.jsonl" % k, "a", encoding="utf-8")
    fd = open("out/site_facts_done_%d.tsv" % k, "a", encoding="utf-8")

    def one(t):
        if time.time() > deadline:
            return
        st = {"host": host_of(t["known_website"])}
        _tl.st = st
        try:
            result, pages, rows = C.crawl(t, a.max_pages, general=False)
        except Exception as e:
            result, pages, rows = "error:%s" % type(e).__name__, 0, []
        _tl.st = None
        C.AP_PAGES.pop(t["buyer_key"], None)
        better = [r for r in rows if ok_mailbox(r.get("ap_email")) and r.get("ap_email_type") != "general"] if t["_general"] else []
        with lock:
            stats["sites"] += 1
            stats["with_address"] += "addr" in st
            stats["with_name"] += bool(st.get("name"))
            stats["better_mailbox"] += bool(better)
            stats["blocked"] += result == "blocked"
            if st.get("name") or st.get("addr"):
                ff.write(facts_line(t["buyer_key"], t["known_website"], st))
            w.writerows(better)
            fd.write("%s\t%s\t%s\t%d\t%d\n" % (t["buyer_key"], TODAY, result if result != "found" else "read", pages, 1 if "addr" in st else 0))
            if stats["sites"] % 500 == 0:
                fr.flush(); ff.flush(); fd.flush()
                print(time.strftime("%H:%M:%S"), dict(stats), flush=True)

    def on_timeout(t):
        with lock:
            fd.write("%s\t%s\ttimeout\t0\t0\n" % (t["buyer_key"], TODAY))
            stats["timeout"] += 1
    left = run_pool(tasks, one, a, deadline, on_timeout)
    with lock:
        fr.close(); ff.close(); fd.close()
    print("finished", dict(stats), "(stragglers left: %d)" % left, flush=True)


def merge(a):
    """append the shard rows to the results file (never a row the validator would reject, never a duplicate) and union the done files"""
    cols, have, rows = None, set(), []
    if os.path.exists(OUT):
        with open(OUT, encoding="utf-8", newline="") as f:
            rd = csv.DictReader(f)
            cols = rd.fieldnames
            for r in rd:
                have.add((r["buyer_key"], (r.get("ap_email") or "").lower(), r.get("evidence_url") or ""))
    for p in sorted(glob.glob(os.path.join(a.merge, "lead_rows_*.csv"))):
        with open(p, encoding="utf-8", newline="") as f:
            rd = csv.DictReader(f)
            cols = cols or rd.fieldnames
            for r in rd:
                key = (r.get("buyer_key"), (r.get("ap_email") or "").lower(), r.get("evidence_url") or "")
                if not r.get("buyer_key") or r["buyer_key"] == "buyer_key" or key in have or not ok_mailbox(r.get("ap_email")):
                    continue
                if a.tenants and not r["buyer_key"].startswith("lead:"):
                    continue  # a candidate that was not accepted never reaches the results file
                have.add(key)
                rows.append(r)
    if rows:
        first = not os.path.exists(OUT)
        with open(OUT, "a", encoding="utf-8", newline="") as f:
            w = csv.DictWriter(f, fieldnames=cols, extrasaction="ignore")
            if first:
                w.writeheader()
            w.writerows(rows)
    done_path, pat = (TDONE, "tenant_done_*.tsv") if a.tenants else (SFDONE, "site_facts_done_*.tsv") if a.site_facts else (DONE, "lead_done_*.tsv")
    seen = {}
    for p in [done_path] + sorted(glob.glob(os.path.join(a.merge, pat))):
        if os.path.exists(p):
            for l in open(p, encoding="utf-8"):
                q = l.rstrip("\n").split("\t")
                if q and q[0]:
                    seen[q[0]] = l.rstrip("\n")
    with open(done_path, "w", encoding="utf-8") as f:
        for key in sorted(seen):
            f.write(seen[key] + "\n")
    facts = {}
    if os.path.exists(FACTS):
        for l in gzip.open(FACTS, "rt", encoding="utf-8"):
            try:
                o = json.loads(l)
                facts[o["key"]] = o
            except (ValueError, KeyError):
                pass
    nf = len(facts)
    for p in sorted(glob.glob(os.path.join(a.merge, "lead_facts_*.jsonl"))):
        for l in open(p, encoding="utf-8"):
            try:
                o = json.loads(l)
                facts[o["key"]] = o
            except (ValueError, KeyError):
                pass
    if facts:
        with gzip.open(FACTS, "wt", encoding="utf-8") as f:
            for key in sorted(facts):
                f.write(json.dumps(facts[key], ensure_ascii=False) + "\n")
    print("site facts (buyer's own name / address): %d (+%d)" % (len(facts), len(facts) - nf))
    res = collections.Counter((l.split("\t") + ["?", "?", "?"])[2].split(":")[0] for l in seen.values())
    print("%s sites read so far: %d (%s); mailbox rows added this run: %d; buyers with a mailbox row: %d" % (
        "candidate" if a.tenants else "delivered-row" if a.site_facts else "lead", len(seen), ", ".join("%s %d" % kv for kv in res.most_common(7)), len(rows), len({x[0] for x in have})))


def main():
    a = argparse.ArgumentParser()
    a.add_argument("--leads", default=os.path.join(INC, "claude_buyer_leads_cc.csv"))
    a.add_argument("--candidates", default="", help="claude_tenant_candidates.csv.gz (tools/cc_tenants.py): accept-or-reject mode")
    a.add_argument("--vendors", default="", help="candidates mode: only these vendor keys (comma separated)")
    a.add_argument("--merge", default="", help="directory of shard outputs to append to the files on main")
    a.add_argument("--tenants", action="store_true", help="with --merge: the shard outputs come from candidates mode")
    a.add_argument("--site-facts", action="store_true", help="with --merge: the shard outputs come from --facts-ranked mode")
    a.add_argument("--facts-ranked", default="", help="ranked_buyers.csv.gz: completeness pass over delivered rows without a bill-to name / address")
    a.add_argument("--shard", default="0/1")
    a.add_argument("--minutes", type=float, default=150)
    a.add_argument("--max-pages", type=int, default=25)
    a.add_argument("--workers", type=int, default=40)
    a.add_argument("--limit", type=int, default=0)
    a.add_argument("--straggler-seconds", type=float, default=240, help="when only slow sites are left and nothing finished for this long, stop")
    a.add_argument("--site-seconds", type=float, default=420, help="wall-clock budget for one site: no new page is opened after that (what was read so far counts)")
    a = a.parse_args()
    if a.merge:
        merge(a)
        return
    k, n = int(a.shard.split("/")[0]), max(1, int(a.shard.split("/")[1]))
    os.makedirs(C.STATE, exist_ok=True)
    os.makedirs("out", exist_ok=True)
    (candidates_mode if a.candidates else facts_mode if a.facts_ranked else leads_mode)(a, k, n)
    sys.stdout.flush()
    os._exit(0)  # do not wait for straggler threads


if __name__ == "__main__":
    main()
