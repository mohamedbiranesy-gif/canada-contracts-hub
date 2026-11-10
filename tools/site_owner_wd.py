#!/usr/bin/env python3
"""Whose website is it? (2026-11-10, row audit)

A client page, a logo wall or a customer story proves a relationship with the organisation whose SITE it is. The Mac-era lanes tied a vendor
"located in Canada" (Wikidata, OpenStreetMap, a contract record) to a website, and for a multinational's Canadian arm that website is the group's
worldwide site: 3ds.com for "Dassault Systèmes (Canada)", ibm.com for "IBM Canada", okta.com for an OpenStreetMap office "Okta - Toronto". Their
customers all over the world were delivered as customers of a Canada-located vendor.

This tool asks Wikidata one question per site: which organisations give this site as their official website (P856), and where are their
headquarters (P159 -> country P17; else the item's own country P17)? When the best-known such organisation (most sitelinks) sits outside
Canada, or a Canadian item names a parent organisation (P749) of the same name that sits outside Canada, the site is not the Canada-located
entity's own. rank.py reads the table and keeps such a listing as tier E (a link, not shown to be a relationship with the Canada-located entity).

Sites asked: the non-.ca sites that carry a listing of a "vendor located in Canada (...)" row of the ranked file, then every vendor's own
website (not .ca). Exact official-website values
only (https/http, with and without www, with and without the final slash): an indexed look-up, 100 sites per query, identified user agent.
The query service answered HTTP 429 "rate-limiting to 1 req / min" on 2026-11-10: one query per 61 seconds; a 429 or a 5xx is waited out
once (Retry-After, at least 65 s / 120 s) and a second one ends the run — the sites left are asked at the next run. A site Wikidata does not know stays
`none` and rank.py falls back on the address the site itself prints.

    python3 tools/site_owner_wd.py --ranked coord/results/ranked/ranked_buyers.csv.gz [--refresh-days 60] [--limit 0] [--minutes 0]
    python3 tools/site_owner_wd.py --rejudge      # the rule changed: apply it to the items on file, no query
Output: data/incoming/claude/claude_site_owner_wd.csv (one row per site; single writer: the ranker's workflow).
"""
import argparse, collections, csv, datetime, gzip, json, os, re, sys, time, urllib.error, urllib.parse, urllib.request

csv.field_size_limit(1 << 30)
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, os.path.join(ROOT, "tools"))
OUT = os.path.join(ROOT, "data/incoming/claude/claude_site_owner_wd.csv")
UA = "canada-contracts-hub-crawler/1.0 (+https://github.com/mohamedbiranesy-gif/canada-contracts-hub)"
COLS = ["domain", "verdict", "owner_qid", "owner_label", "owner_hq", "owner_hq_country", "owner_sitelinks", "via", "canadian_items", "items", "retrieved_date", "evidence_url", "quote", "items_json"]
TODAY = datetime.date.today().isoformat()
QUERY = """SELECT ?url ?item ?itemLabel ?hqLabel ?hqcLabel ?cLabel ?links ?parent ?parentLabel ?phqLabel ?phqcLabel ?pcLabel WHERE {
 VALUES ?url { %s }
 ?item wdt:P856 ?url .
 OPTIONAL { ?item wdt:P159 ?hq . OPTIONAL { ?hq wdt:P17 ?hqc } }
 OPTIONAL { ?item wdt:P17 ?c }
 OPTIONAL { ?item wikibase:sitelinks ?links }
 OPTIONAL { ?item wdt:P749 ?parent . OPTIONAL { ?parent wdt:P159 ?phq . OPTIONAL { ?phq wdt:P17 ?phqc } } OPTIONAL { ?parent wdt:P17 ?pc } }
 SERVICE wikibase:label { bd:serviceParam wikibase:language "en,fr". }
}"""


def host_of(u):
    try:
        return (urllib.parse.urlparse(u if "//" in u else "https://" + u).hostname or "").lower().removeprefix("www.")
    except ValueError:
        return ""


def wanted_sites(ranked):
    """registrable domains of the non-.ca sites that carry a listing of a vendor "located in Canada" (client page, wall, story, member list),
    then of the vendors' own websites — a Counter whose order (most_common) is the order of asking"""
    from ap_crawler import registrable
    op = gzip.open if ranked.endswith(".gz") else open
    out = collections.Counter()
    second = collections.Counter()
    with op(ranked, "rt", encoding="utf-8", errors="replace", newline="") as fh:
        for r in csv.DictReader(fh):
            # every vendor's own website (not .ca): rank.py does not take a foreign organisation's legal name, address or telephone for the
            # Canada-located vendor — asked after the listing sites
            w = host_of(r.get("vendor_website") or "")
            if w and "." in w and not w.endswith(".ca") and not (r.get("vendor") or "").startswith("inferred"):
                second[registrable(w)] += 1
            if not (r.get("vendor_country_basis") or "").startswith("vendor located in Canada ("):
                continue
            h = host_of(r.get("contract_link") or "")
            if h and "." in h and not h.endswith(".ca"):
                out[registrable(h)] += 1
    top = max(second.values() or [0]) + 1
    for d, n in out.items():
        out[d] = n + top  # the listing sites first
    for d, n in second.items():
        if d not in out:
            out[d] = n
    return out


def ask(domains):
    vals = []
    for d in domains:
        if not re.fullmatch(r"[a-z0-9.-]+", d):
            continue
        for sch in ("https", "http"):
            for w in ("www.", ""):
                for sl in ("/", ""):
                    vals.append("<%s://%s%s%s>" % (sch, w, d, sl))
    if not vals:
        return []
    # POST: 100 sites are 800 values, too long for a GET line (HTTP 431)
    req = urllib.request.Request("https://query.wikidata.org/sparql", data=urllib.parse.urlencode({"query": QUERY % " ".join(vals), "format": "json"}).encode(),
                                 headers={"User-Agent": UA, "Accept": "application/sparql-results+json", "Content-Type": "application/x-www-form-urlencoded"})
    with urllib.request.urlopen(req, timeout=120) as r:
        return json.load(r)["results"]["bindings"]


def _n(s):
    import unicodedata
    s = unicodedata.normalize("NFKD", s or "").encode("ascii", "ignore").decode().lower()
    s = re.sub(r"\(canada\)|\bcanada\b|\b(?:inc|ltd|ltee|limited|corp|corporation|co|company|llc|ulc|group|groupe|sa|ag|gmbh|plc)\b\.?", " ", s)
    return re.sub(r"[^a-z0-9]", "", s)


def same_brand(a, b):
    """a parent organisation of the same name (Dassault Systèmes / Dassault Systèmes (Canada)) — not a holding or an investment fund"""
    a, b = _n(a), _n(b)
    return bool(a and b and len(min(a, b, key=len)) >= 4 and (a in b or b in a))


def is_ca(c):
    return (c or "").strip().lower() == "canada"


REGION = re.compile(r"\s*\([A-Za-z .]{2,20}\)\s*$|\s+(?:canada|europe|usa|uk|deutschland|france|australia|asia|americas?|north america|cz)\s*$", re.I)
GENERIC_TAIL = re.compile(r"(?:\s+(?:global|group|groupe|international|holdings?|worldwide|inc|ltd|llc|limited|plc|ag|sa|se|nv|company|co|corp|corporation)\.?)+\s*$", re.I)


def base_name(label):
    return REGION.sub("", label or "").strip()


def brand(label):
    """the name without its region and without the corporate words at its end: "WSP Global" -> "WSP", "Magna International (Germany)" -> "Magna" """
    return GENERIC_TAIL.sub("", base_name(label)).strip() or base_name(label)


def collect(binds):
    """{qid: item} from a query's bindings"""
    g = lambda b, k: (b.get(k) or {}).get("value", "")
    items = {}
    for b in binds:
        q = g(b, "item").rsplit("/", 1)[-1]
        it = items.setdefault(q, {"qid": q, "label": g(b, "itemLabel"), "hq": [], "hqc": [], "c": [], "links": 0, "parents": {}, "url": g(b, "url")})
        for k, v in (("hq", g(b, "hqLabel")), ("hqc", g(b, "hqcLabel")), ("c", g(b, "cLabel"))):
            if v and v not in it[k]:
                it[k].append(v)
        it["links"] = max(it["links"], int(g(b, "links") or 0))
        if g(b, "parent"):
            p = it["parents"].setdefault(g(b, "parent").rsplit("/", 1)[-1], {"label": g(b, "parentLabel"), "hq": [], "hqc": [], "c": []})
            for k, v in (("hq", g(b, "phqLabel")), ("hqc", g(b, "phqcLabel")), ("c", g(b, "pcLabel"))):
                if v and v not in p[k]:
                    p[k].append(v)
    return items


def judge(domain, items):
    """one row for the site. Whose site it is, among the organisations that give it as their official website (P856):
      - the organisation whose name is the site's name (Haivision on haivision.com, not its subsidiary Kulabyte; "Parametric Technology
        Corporation" on ptc.com by its initials); when no name fits, an organisation known well enough to trust its statement (3+ sitelinks:
        Schneider Electric on se.com) — otherwise Wikidata does not say whose site it is (`unknown`: Georgia Marble's item points at its
        parent's polycor.com);
      - a regional item ("PTC (Canada)", "WSP USA", "Genetec (United States)") yields to the organisation of the same site without a region
        in its name;
      - the organisation's seat is its same-name parent's (P749) when it has one: "Dassault Systèmes (Canada)" sits where Dassault Systèmes
        does, "WSP USA" where WSP Global does;
      - headquarters abroad while the item's only country is Canada (Grass Valley: Cergy / Canada) is a contradiction: `unknown`."""
    from lead_crawl import name_fit
    row = dict.fromkeys(COLS, "")
    row.update(domain=domain, retrieved_date=TODAY, items=str(len(items)), verdict="none",
               items_json=json.dumps(sorted(items.values(), key=lambda it: it["qid"]), ensure_ascii=False, separators=(",", ":")) if items else "")
    if not items:
        return row
    where = lambda it: it["hqc"] or it["c"]  # the countries of its headquarters; without a headquarters statement, its own countries
    def seat_of(it):
        """"CA", "abroad" or "" (it does not say): by its headquarters; without a headquarters statement by its countries, when they agree"""
        if it["hqc"]:
            return "CA" if any(is_ca(c) for c in it["hqc"]) else "abroad"
        if it["c"] and all(is_ca(c) for c in it["c"]):
            return "CA"
        return "abroad" if it["c"] and not any(is_ca(c) for c in it["c"]) else ""  # Canada among several countries (a border bridge, a union): no seat stated
    in_ca = lambda it: seat_of(it) == "CA"
    located = [it for it in items.values() if where(it)]
    row["canadian_items"] = "; ".join("%s %s" % (it["qid"], it["label"]) for it in located if in_ca(it))[:300]
    label = re.sub(r"[^a-z0-9]", "", domain.split(".")[0])
    fit = {it["qid"]: max(name_fit(base_name(it["label"]), label), name_fit(brand(it["label"]), label)) for it in located}
    pool = [it for it in located if fit[it["qid"]] >= 45] or [it for it in located if it["links"] >= 3]
    if not pool:
        row["verdict"] = "unknown"  # Wikidata knows the site, not whose it is (no place stated, or no organisation of the site's name)
        return row
    plain = [it for it in pool if not REGION.search(it["label"])]
    if not plain and len({seat_of(it) for it in pool} - {""}) > 1:
        # only national arms, in several countries, give the site ("Nortek (Canada)", "Nortek (United Kingdom)"): a group's site, no arm's own
        row.update(verdict="abroad", owner_label="; ".join(sorted(it["label"] for it in pool))[:120], owner_hq_country="; ".join(sorted({c for it in pool for c in where(it)}))[:80],
                   via="official website (P856) of %d national arms in several countries" % len(pool), evidence_url="https://www.wikidata.org/wiki/" + pool[0]["qid"])
        row["quote"] = ("Wikidata: %s all give %s as their official website" % ("; ".join("%s “%s” (%s)" % (it["qid"], it["label"], ", ".join(where(it))) for it in pool), pool[0]["url"]))[:300]
        return row
    own = max(plain or pool, key=lambda it: (it["links"], fit[it["qid"]], 1 if it["hqc"] else 0))
    seat, via = own, "official website (P856)%s" % ("; %d organisations give this site" % len(located) if len(located) > 1 else "")
    for pq, p in own["parents"].items():
        if (p["hqc"] or p["c"]) and same_brand(p["label"], own["label"]):
            seat = dict(p, qid=pq, links=0, parents={}, url=own["url"])
            via = "parent organisation (P749) of %s “%s”, which gives this site as its official website" % (own["qid"], own["label"])
            break
    if seat is own and own["hqc"] and not any(is_ca(c) for c in own["hqc"]) and own["c"] and all(is_ca(c) for c in own["c"]):
        row["verdict"] = "unknown"  # headquarters abroad, country Canada: the item contradicts itself
        return row
    w = where(seat)
    if not seat_of(seat):
        row["verdict"] = "unknown"  # no headquarters stated and Canada is one of several countries
        return row
    row.update(owner_qid=seat["qid"], owner_label=seat["label"], owner_hq="; ".join(seat["hq"])[:120], owner_hq_country="; ".join(w)[:80], owner_sitelinks=str(own["links"]),
               via=via, evidence_url="https://www.wikidata.org/wiki/" + own["qid"])
    row["verdict"] = "canada" if in_ca(seat) else "abroad"
    row["quote"] = ("Wikidata %s “%s”: official website %s; %s%s %s (%s)" % (
        own["qid"], own["label"], own["url"], ("parent organisation %s “%s”, " % (seat["qid"], seat["label"])) if seat is not own else "",
        "headquarters location" if seat["hqc"] else "country", "; ".join(seat["hq"]) if seat["hqc"] else "", "; ".join(w))).replace("  ", " ")[:300]
    return row


def main():
    a = argparse.ArgumentParser()
    a.add_argument("--ranked", default=os.path.join(ROOT, "coord/results/ranked/ranked_buyers.csv.gz"))
    a.add_argument("--refresh-days", type=int, default=60)
    a.add_argument("--limit", type=int, default=0)
    a.add_argument("--batch", type=int, default=100)
    a.add_argument("--pause", type=float, default=61.0, help="seconds between two queries (the service allowed one per minute on 2026-11-10)")
    a.add_argument("--minutes", type=float, default=0, help="stop asking after this many minutes (0 = no limit)")
    a.add_argument("--rejudge", action="store_true", help="apply the current rule to the items on file (no query)")
    a = a.parse_args()
    have = {}
    if os.path.exists(OUT):
        for r in csv.DictReader(open(OUT, encoding="utf-8")):
            have[r["domain"]] = r
    if a.rejudge:
        n = 0
        for d, r in list(have.items()):
            if r.get("items_json"):
                new = judge(d, {it["qid"]: it for it in json.loads(r["items_json"])})
                new["retrieved_date"] = r.get("retrieved_date") or TODAY
                n += new["verdict"] != r.get("verdict")
                have[d] = new
        with open(OUT, "w", encoding="utf-8", newline="") as fh:
            w = csv.DictWriter(fh, fieldnames=COLS)
            w.writeheader()
            for d in sorted(have):
                w.writerow({c: have[d].get(c, "") for c in COLS})
        print("rule applied again to %d sites on file; %d verdicts changed" % (len(have), n))
        return
    want = wanted_sites(a.ranked)
    old = (datetime.date.today() - datetime.timedelta(days=a.refresh_days)).isoformat()
    todo = [d for d, _ in want.most_common() if d not in have or (have[d].get("retrieved_date") or "") < old]
    if a.limit:
        todo = todo[:a.limit]
    print("sites of vendors located in Canada (not .ca; listing sites first, then their own websites): %d; on file: %d; to ask: %d" % (len(want), sum(1 for d in want if d in have), len(todo)), flush=True)
    asked, t0 = 0, time.time()
    from ap_crawler import registrable

    def write():
        tmp = OUT + ".tmp"
        with open(tmp, "w", encoding="utf-8", newline="") as fh:
            w = csv.DictWriter(fh, fieldnames=COLS)
            w.writeheader()
            for d in sorted(have):
                w.writerow({c: have[d].get(c, "") for c in COLS})
        os.replace(tmp, OUT)

    i = 0
    while i < len(todo):
        if a.minutes and time.time() - t0 > a.minutes * 60 - a.pause:
            break
        chunk, binds = todo[i:i + a.batch], None
        for attempt in (1, 2):
            try:
                binds = ask(chunk)
                break
            except urllib.error.HTTPError as e:
                if e.code in (429, 500, 502, 503, 504) and attempt == 1:  # the rate limit, or the service's own outage: wait once, then give up for this run
                    ra = e.headers.get("Retry-After") or ""
                    wait = max(65 if e.code == 429 else 120, int(ra) if ra.isdigit() else 0)
                    print("HTTP %s (%s); waiting %d s" % (e.code, str(e.reason)[:90], wait), flush=True)
                    time.sleep(wait)
                    continue
                print("query refused (HTTP %s %s); the run ends here" % (e.code, str(e.reason)[:90]), flush=True)
                break
            except Exception as e:
                print("query failed (%s: %s); the run ends here" % (type(e).__name__, str(e)[:120]), flush=True)
                break
        if binds is None:
            break
        by = collections.defaultdict(list)
        for b in binds:
            h = host_of((b.get("url") or {}).get("value", ""))
            if h:
                by[registrable(h)].append(b)
        for d in chunk:
            have[d] = judge(d, collect(by.get(d, [])))
        asked += len(chunk)
        i += a.batch
        write()  # after every query: a run cut short keeps what it learned
        print("  %d / %d sites asked" % (asked, len(todo)), flush=True)
        if i < len(todo):
            time.sleep(a.pause)
    failed = len(todo) - asked
    v = collections.Counter(r.get("verdict") for d, r in have.items() if d in want)
    print("asked %d sites (%d left for the next run); verdicts for the sites wanted: %s" % (asked, failed, dict(v.most_common())))


if __name__ == "__main__":
    main()
