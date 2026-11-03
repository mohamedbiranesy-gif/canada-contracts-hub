#!/usr/bin/env python3
"""Customer portals of Canada-HQ SaaS vendors -> the customer organisation and its OWN website, verified. No AI.

Second pass after tools/tech_relationships.py --forward. That pass read the vendor-hosted portal and took the customer's
name and website from the portal page itself; for most vendors the portal names no website (D2L 4/146, Amilia 4/787,
Docebo 0/98) or no organisation at all (eSCRIBE: every portal is titled "eSCRIBE Published Meetings", 0/263).
This pass works the other way round, from the buyer's side:

  1. hosts   enumerate the vendor's customer portal hosts from the public Common Crawl URL index (index.commoncrawl.org
             CDX API only, newest --crawls crawls, one request every 2 s, back-off on 503/504; raw index pages cached
             under ~/cch-sources/tech/cc/ with the same names as tools/tech_relationships.py, so its cache is reused).
  2. resolve for each portal host, derive the customer's slug (pub-barrie.escribemeetings.com -> barrie), list candidate
             official domains spelled from the slug (barrie.ca, barrie.gov, cityofbarrie.com, barrieon.ca ...), keep the
             ones that resolve in DNS, and read each candidate's home page plus at most 4 of its own pages about
             meetings / learning / parents / payments / library. A candidate is kept ONLY when one of the organisation's
             own pages links to (or embeds, or redirects to) that exact portal host: the buyer's own website shows today
             that it uses the vendor's paid service. The name is the home page's og:site_name / <title>.
             No match = nothing written (never a guessed website).

Lead format: ~/cch-leads/socrata_tech_<vendor>2.jsonl (P01T: canada_field = "service of a Canada-HQ vendor seen on the
buyer's own site (tech)", canada_value = the vendor's own HQ quote, row.vendor_hq_url = the page it was read on).
Rules: robots.txt honoured, <= 1 request/second per registered domain (tools/tech_relationships.fetch), UA
canada-contracts-hub-crawler/1.0, 401/403/429/challenge = blocked and skipped.

    python3 tools/tech_portals2.py hosts   --vendor escribe [--crawls 8] [--max-pages 40]
    python3 tools/tech_portals2.py resolve --vendor escribe [--workers 16] [--limit N]
"""
import argparse, json, os, re, socket, sys, threading, time, urllib.parse
from concurrent.futures import ThreadPoolExecutor

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import tech_relationships as TR
try:
    import site_finder_quick as SF
    _sf_get, _sf_lock = SF.get, threading.Lock()

    def _sf_polite(params):  # Wikidata: <= 1 request per second from this tool, all threads together
        with _sf_lock:
            w = SF.last[0] + 1.0 - time.time()
            if w > 0:
                time.sleep(w)
            SF.last[0] = time.time() - 0.4
            return _sf_get(params)
    SF.get = _sf_polite
except Exception:
    SF = None

HOSTS_DIR = os.path.join(TR.CACHE, "hosts")

# Vendors with one sub-domain per customer. hq / hq_url = the vendor's own published HQ address (read 2026-11-02/03).
EXTRA = {
    # KEV: Toronto postal address of its privacy officer (no "headquarters" wording; offices also in Wilmington NC and
    # Fort Worth TX; the entity for US districts is not published) -> kept for Canadian customers (.ca sites) only.
    "kev": dict(name="SchoolCash Online (KEV Group)", legal="KEV Group Inc.", kind="portal", country_only=".ca",
                hq_url="https://kevgroup.com/privacy-policy/",
                hq="KEV Software Inc. and KEV Group Inc. (collectively, \u201cKEV Group\u201d) ... By post: Privacy Officer KEV Group "
                   "90 Eglinton Avenue East, Suite 502, Toronto, ON, M4P 2Y3",
                scope="kept for Canadian customers only: the KEV entity that contracts with US districts is not published", host_re=r"^([a-z0-9-]+)\.schoolcashonline\.com$", cc=["*.schoolcashonline.com"],
                excl={"www", "api", "help", "support", "status", "cdn", "static", "assets", "demo", "test", "staging",
                      "dev", "sandbox", "admin", "secure", "my", "login", "auth", "blog", "info", "media", "app", "uat",
                      "qa", "training"}),
}
for _k, _v in EXTRA.items():
    _v["key"] = _k
    _v["host_re_c"] = re.compile(_v["host_re"], re.I)

SLUG_STRIP = [(r"^bm-public-", ""), (r"^pub-", ""), (r"-pub$", ""), (r"publishing$", ""), (r"-?public$", ""),
              (r"-?(?:brightspace|d2l|lms|learn|elearning|online)$", ""), (r"^(?:d2l|lms|learn|elearn|online)-?", "")]
STATE_SUFFIX = re.compile(r"(?:-|)(al|ak|az|ar|ca|co|ct|de|fl|ga|hi|id|il|in|ia|ks|ky|la|me|md|ma|mi|mn|ms|mo|mt|ne|nv|nh|"
                          r"nj|nm|ny|nc|nd|oh|ok|or|pa|ri|sc|sd|tn|tx|ut|vt|va|wa|wv|wi|wy|on|ab|bc|mb|sk|ns|nb|nl|pe|qc)$")
PAGE_CATS = re.compile(r"agenda|minutes|meeting|council|board|commission|conseil|s[ée]ance|government|gouvernement|"
                       r"learn|student|parent|[ée]l[eè]ve|portal|portail|online|lms|course|training|staff|employee|"
                       r"pay|fees?\b|school cash|cash online|frais|paiement|library|biblioth|resource|quick ?links?|"
                       r"departments?|services|about|transparency|elected", re.I)
_dns, _dlock = {}, threading.Lock()
_HOME = {}  # candidate domain -> (final url, body) of its home page, read once


def vend(vkey):
    return TR.VENDORS.get(vkey) or EXTRA[vkey]


def portal_host_ok(v, h):
    m = v["host_re_c"].match(h) if v.get("host_re_c") else None
    return bool(m) and m.group(1).lower() not in v["excl"]


# ------------------------------------------------------------------------------------------------------- hosts
def hosts(vkey, args):
    v = vend(vkey)
    coll = json.loads(TR.cc_get("https://index.commoncrawl.org/collinfo.json") or "[]")
    crawls = [(c["id"], c["cdx-api"]) for c in coll[:args.crawls]]
    seen = {}
    for pat in v["cc"]:
        for cid, u in TR.cc_urls(pat, crawls, args.max_pages):
            h = TR.host_of(u)
            if portal_host_ok(v, h) and h not in seen:
                seen[h] = (cid, u)
    os.makedirs(HOSTS_DIR, exist_ok=True)
    out = os.path.join(HOSTS_DIR, "%s.tsv" % vkey)
    with open(out, "w", encoding="utf-8") as f:
        for h in sorted(seen):
            f.write("%s\t%s\t%s\n" % (h, seen[h][0], seen[h][1]))
    print("DONE hosts %s: %d portal hosts from %d crawls -> %s" % (vkey, len(seen), len(crawls), out), flush=True)


# ----------------------------------------------------------------------------------------------------- resolve
def slug_core(vkey, h):
    s = h.split(".")[0].lower()
    for a, b in SLUG_STRIP:
        s2 = re.sub(a, b, s)
        if len(s2) >= 3:
            s = s2
    return s


def candidates(core):
    """Official-domain spellings of a customer slug, most likely first. Only checked, never kept unverified."""
    c = core.replace("_", "-")
    flat = c.replace("-", "")
    bases = [flat] + ([c] if c != flat else [])
    m = STATE_SUFFIX.search(flat)
    stem = flat[:m.start()] if m and len(flat) - len(m.group(0)) >= 4 else ""
    st = m.group(1) if stem else ""
    out = []
    for b in bases:
        out += [b + ".ca", b + ".gov", b + ".org", b + ".us", b + ".com", b + ".net", b + ".edu", b + ".k12." + "us"]
    if stem:
        out += [stem + "." + st + ".us", stem + st + ".gov", stem + st + ".org", stem + ".gov", stem + ".org", stem + ".ca",
                stem + ".com", "cityof" + stem + ".com", "cityof" + stem + ".org", "cityof" + stem + ".gov",
                stem + "county.gov", stem + "county" + st + ".gov", "co." + stem + "." + st + ".us",
                "ci." + stem + "." + st + ".us", stem + ".k12." + st + ".us"]
    for p in ("cityof", "townof", "villageof", "countyof", "ville."):
        out += [p + flat + ".com", p + flat + ".org", p + flat + ".gov", p + flat + ".ca", p + flat + ".net"]
    if flat.endswith("county"):
        out += [flat[:-6] + "county.org", flat[:-6] + "co.org", flat[:-6] + "countyfl.gov", flat[:-6] + "-county.org"]
    if flat.endswith(("schools", "sd", "isd", "usd", "csd", "ccsd")):
        out += [flat + ".net", flat + ".k12.us"]
    for pre in ("www.",):
        out = [o for o in out]
    seen, res = set(), []
    for o in out:
        if o not in seen and re.match(r"^[a-z0-9.-]+$", o):
            seen.add(o)
            res.append(o)
    return res


def resolves(host):
    with _dlock:
        if host in _dns:
            return _dns[host]
    try:
        socket.setdefaulttimeout(5)
        ok = bool(socket.getaddrinfo(host, 443))
    except Exception:
        ok = False
    if not ok and not host.startswith("www."):
        try:
            ok = bool(socket.getaddrinfo("www." + host, 443))
        except Exception:
            ok = False
    with _dlock:
        _dns[host] = ok
    return ok


def links_portal(body, page_url, portal_host, vkey):
    """The first URL on the page that points at the portal host (or another host of the same customer at the vendor)."""
    core = slug_core(vkey, portal_host)
    for u in TR.all_urls(body, page_url):
        h = TR.host_of(u)
        if h == portal_host or (h.endswith(TR.base_domain(portal_host)) and slug_core(vkey, h) == core):
            return u
    return ""


def check_site(dom, portal_host, vkey, deep=True):
    """Home page + <= 4 own pages of a candidate domain; (home_final, page_with_link, link, home_body) or None."""
    home = "https://%s/" % dom
    if not TR.allowed(home):
        return None
    st, fu, body, ct = TR.fetch(home)
    if (st != 200 or not body) and not dom.startswith("www."):
        home = "https://www.%s/" % dom
        if not TR.allowed(home):
            return None
        st, fu, body, ct = TR.fetch(home)
    if TR.blocked(st, body) or st != 200 or not body:
        return None
    fh = TR.host_of(fu)
    if TR.base_domain(fh) in TR.SKIP_BASES or TR.base_domain(fh) in TR.VENDOR_BASES or \
            re.search(r"godaddy|sedo|parking|hugedomains|dan\.com|afternic|domain (?:is )?for sale", body[:5000], re.I):
        return None
    if TR.host_of(fu) == portal_host:
        return None
    _HOME[dom] = (fu, body)
    hit = links_portal(body, fu, portal_host, vkey)
    if hit:
        return fu, fu, hit, body
    if not deep:
        return None
    org_base = TR.base_domain(fh)
    used = {fu.rstrip("/")}
    MEET = re.compile(r"agenda|minutes|meeting|council|board|commission|conseil|s[ée]ance|ordre du jour|proc[eè]s|"
                      r"government|gouvernement|elected|clerk|greffe|transparen", re.I)

    def pick(page_body, page_url, rx, n):
        out = []
        for u, txt, img, alt in TR.anchors_of(page_body, page_url):
            hu = TR.host_of(u)
            if TR.base_domain(hu) != org_base or TR.NOT_PAGE.search(u):
                continue
            k = u.split("#")[0].rstrip("/")
            if k in used:
                continue
            if rx.search(txt) or rx.search(urllib.parse.urlparse(u).path):
                used.add(k)
                out.append(u.split("#")[0])
            if len(out) >= n:
                break
        return out
    level1 = pick(body, fu, MEET, 3) if vkey == "escribe" else []
    level1 += pick(body, fu, PAGE_CATS, 4 - min(len(level1), 2))
    budget, level2 = 10, []
    for u in level1:
        if budget <= 0 or not TR.allowed(u):
            continue
        budget -= 1
        st2, fu2, b2, _ = TR.fetch(u)
        if TR.host_of(fu2) == portal_host or (TR.base_domain(TR.host_of(fu2)) == TR.base_domain(portal_host)
                                              and slug_core(vkey, TR.host_of(fu2)) == slug_core(vkey, portal_host)):
            return fu, u, fu2, body
        if st2 == 200 and b2 and not TR.blocked(st2, b2):
            hit = links_portal(b2, fu2, portal_host, vkey)
            if hit:
                return fu, fu2, hit, body
            if vkey == "escribe":
                level2 += pick(b2, fu2, MEET, 2)
    for u in level2:
        if budget <= 0:
            break
        if not TR.allowed(u):
            continue
        budget -= 1
        st3, fu3, b3, _ = TR.fetch(u)
        if TR.host_of(fu3) == portal_host:
            return fu, u, fu3, body
        if st3 == 200 and b3 and not TR.blocked(st3, b3):
            hit = links_portal(b3, fu3, portal_host, vkey)
            if hit:
                return fu, fu3, hit, body
    return None


LINK_FALLBACK = {"kev", "edsby"}  # portal page often names no one: fall back to the buyer-side link check
NAME_ON_PORTAL = {"d2l", "edsby", "docebo", "kev", "bibliocommons", "absorb", "jane"}
JUNK_NAME = re.compile(r"google|microsoft|okta|surfconext|shibboleth|single sign|\badfs\b|azure|\blog ?in\b|sign ?in|"
                       r"authenticat|\bcas\b|identity|password|^wizard$|^portal$|^lms$|^learn$|^home$|official (?:web ?)?site|"
                       r"^home ?page|^site officiel|^welcome", re.I)
TEST_SLUG = re.compile(r"(?:test|sandbox|sbx|dev|stage|staging|train|training|demo|uat|qa|preview|trial)\d*$", re.I)


def portal_url(vkey, h):
    return "https://%s/d2l/login" % h if vkey == "d2l" else "https://%s/" % h


def title_names(body, name):
    """True when the home page's title / og:site_name carries the organisation's distinctive words."""
    title, meta = TR.page_meta(body)
    hay = TR.name_tokens(title, meta.get("og:site_name", ""), meta.get("og:title", ""))
    toks = TR.name_tokens(name)
    if not toks:
        return False
    hit = toks & hay
    return len(toks) >= 2 and len(hit) >= 2 and len(hit) >= 0.6 * len(toks)  # one-word names need the portal link


def resolve_one(vkey, portal_host):
    core = slug_core(vkey, portal_host)
    res = {"portal_host": portal_host, "slug": core, "website": "", "name": "", "candidates_checked": []}
    if TEST_SLUG.search(portal_host.split(".")[0]):
        res["skip"] = "test/sandbox tenant"
        return res
    pinfo = None
    if vkey in NAME_ON_PORTAL:
        pinfo, pst = TR.portal_info(vkey, portal_url(vkey, portal_host))
        res["portal_status"] = pst
        if pinfo and JUNK_NAME.search(pinfo["name"]):
            res["portal_status"], pinfo = "junk_name:" + pinfo["name"][:40], None
        if not pinfo and vkey not in LINK_FALLBACK:
            return res
    if pinfo:
        res.update(name=pinfo["name"], portal_final=pinfo["final_url"], home_title=pinfo["page_title"],
                   og_site_name=pinfo["og_site_name"], name_basis="portal " + pinfo["name_basis"])
        if pinfo["website"]:
            res.update(website=pinfo["website"], website_basis="portal: " + pinfo["website_basis"],
                       page_with_link=pinfo["final_url"], link=pinfo["final_url"])
            return res
    tried = []
    for dom in candidates(core):
        if not resolves(dom):
            continue
        tried.append(dom)
        r = check_site(dom, portal_host, vkey, deep=not pinfo)
        if r:
            home_final, page, link, body = r
            title, meta = TR.page_meta(body)
            name = res["name"] or TR.clean_name(meta.get("og:site_name")) or TR.clean_name(title) or TR.clean_name(meta.get("og:title"))
            res.update(website="https://%s/" % TR.host_of(home_final), page_with_link=page, link=link, name=name,
                       website_basis="the organisation's own page links to its vendor portal")
            if not pinfo:
                res.update(home_title=title[:200], og_site_name=meta.get("og:site_name", "")[:200],
                           name_basis="og:site_name / title of the organisation's own home page")
            res["candidates_checked"] = tried
            return res
        if pinfo and dom in _HOME:
            fu, body = _HOME[dom]
            if True:
                if title_names(body, pinfo["name"]):
                    res.update(website="https://%s/" % TR.host_of(fu), page_with_link=pinfo["final_url"], link=pinfo["final_url"],
                               website_basis="domain spelled from the portal slug '%s'; its home page title names the "
                               "organisation (%s)" % (core, TR.page_meta(body)[0][:80]))
                    res["candidates_checked"] = tried
                    return res
        if len(tried) >= 6:
            break
    res["candidates_checked"] = tried
    if pinfo and SF:
        hit = SF.find(pinfo["name"])
        if hit:
            res.update(website=hit[0] if hit[0].endswith("/") else hit[0] + "/", page_with_link=pinfo["final_url"],
                       link=pinfo["final_url"], website_basis="Wikidata %s official website (exact name match)" % hit[1])
    return res


def resolve(vkey, args):
    v = vend(vkey)
    if not v.get("hq"):
        sys.exit("vendor %s has no verified HQ quote yet" % vkey)
    rows = [l.rstrip("\n").split("\t") for l in open(os.path.join(HOSTS_DIR, "%s.tsv" % vkey), encoding="utf-8")]
    if args.limit:
        rows = rows[:args.limit]
    cache_p = os.path.join(HOSTS_DIR, "%s_resolved.jsonl" % vkey)
    done = {}
    if os.path.exists(cache_p):
        for l in open(cache_p, encoding="utf-8"):
            try:
                o = json.loads(l)
                done[o["portal_host"]] = o
            except ValueError:
                pass
    todo = [r for r in rows if r[0] not in done or (args.retry and not done[r[0]].get("website"))]
    if args.write_only:
        todo = []
    print(time.strftime("%H:%M:%S"), "%s: %d portal hosts, %d to resolve" % (vkey, len(rows), len(todo)), flush=True)
    lock = threading.Lock()
    with open(cache_p, "a", encoding="utf-8") as cf:
        def work(r):
            try:
                o = resolve_one(vkey, r[0])
            except Exception as e:
                o = {"portal_host": r[0], "website": "", "error": type(e).__name__}
            o["cc_crawl"], o["cc_url"] = (r[1], r[2]) if len(r) >= 3 else ("", "")
            with lock:
                cf.write(json.dumps(o, ensure_ascii=False) + "\n")
                cf.flush()
                done[r[0]] = o
            return o
        n = 0
        with ThreadPoolExecutor(args.workers) as ex:
            for o in ex.map(work, todo):
                n += 1
                if n % 25 == 0:
                    print(time.strftime("%H:%M:%S"), "%s %d/%d, %d with website" %
                          (vkey, n, len(todo), sum(1 for x in done.values() if x.get("website"))), flush=True)
    out_path = os.path.join(TR.LEADS, "socrata_tech_%s2.jsonl" % vkey)
    stats = {"vendor": vkey, "portal_hosts": len(rows), "resolved": 0, "leads": 0}
    seen = set()
    TR.VENDORS.setdefault(vkey, v)
    with open(out_path, "w", encoding="utf-8") as f:
        for r in rows:
            o = done.get(r[0]) or {}
            if not o.get("website") or not o.get("name") or JUNK_NAME.search(o["name"]):
                continue
            if v.get("country_only") and not TR.host_of(o["website"]).endswith(v["country_only"]):
                continue
            stats["resolved"] += 1
            key = TR.nowww(TR.host_of(o["website"]))
            if key in seen:
                continue
            seen.add(key)
            own = o.get("website_basis", "").startswith("the organisation's own page")
            row = {"portal_url": o.get("portal_final") or portal_url(vkey, o["portal_host"]), "portal_slug": o["slug"],
                   "page_title": o.get("home_title", ""), "og_site_name": o.get("og_site_name", ""),
                   "name_basis": o.get("name_basis", ""), "website_basis": o.get("website_basis", ""),
                   "signature": (o.get("link") or "")[:300],
                   "signature_kind": ("link/embed on the organisation's own page to its vendor-hosted customer portal"
                                      if own else "vendor-hosted customer portal naming the organisation") +
                                     " (portal host from Common Crawl %s)" % o.get("cc_crawl", ""),
                   "page_seen": o.get("page_with_link", ""), "common_crawl_url": o.get("cc_url", "")}
            TR.write_line(f, TR.lead(vkey, o["name"], o["website"], o.get("page_with_link") or row["portal_url"], row))
            stats["leads"] += 1
    json.dump(stats, open(out_path + ".stats", "w"), indent=1)
    print("DONE resolve", json.dumps(stats), flush=True)


def main():
    a = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    a.add_argument("mode", choices=["hosts", "resolve"])
    a.add_argument("--vendor", required=True)
    a.add_argument("--crawls", type=int, default=8)
    a.add_argument("--max-pages", type=int, default=40)
    a.add_argument("--workers", type=int, default=16)
    a.add_argument("--limit", type=int, default=0)
    a.add_argument("--retry", action="store_true", help="resolve again the hosts cached without a website")
    a.add_argument("--write-only", action="store_true", help="only write the lead file from the resolved cache")
    args = a.parse_args()
    for vk in args.vendor.split(","):
        if vk not in TR.VENDORS and vk not in EXTRA:
            sys.exit("unknown vendor %s" % vk)
        (hosts if args.mode == "hosts" else resolve)(vk, args)


if __name__ == "__main__":
    main()
