#!/usr/bin/env python3
"""Official websites for lead buyers that have none (cloud; no AI, no search engine): Wikidata's "official website" claim, exact name match.

23,851 lead buyers (customers named in Canadian vendors' stories, importers, members of Canadian bodies, lobbyists' clients, counterparties
in US filings …) have a relationship with a Canada-located vendor on record but no website, so no mailbox could ever be read for them. The
owner's Mac ran tools/site_finder.py for the contract buyers; this is the same rule for the leads, on GitHub runners:
  - the name must have at least three words (one- and two-word names are too ambiguous);
  - Wikidata's search must return an item whose label or alias EQUALS the name (accents, case and punctuation ignored);
  - the item must carry an official website (P856) and a country (P17) among the countries the lead's source implies
    (Canada or the United States; Colombia for the importers of the DIAN customs data).
Nothing is guessed: no domain is built from a name. The website found is then read by tools/lead_crawl.py like any other lead site, and
the mailbox must sit on that site's own domain (ap_crawler.same_org).

  python3 tools/lead_sites.py --shard K/N [--minutes 150]     -> out/lead_sites_<K>.csv, out/lead_sites_done_<K>.tsv
  python3 tools/lead_sites.py --merge DIR                     -> data/incoming/claude/claude_lead_websites.csv, claude_lead_sites_done.tsv
Polite: one request per second per runner (at most 2 runners), identified user agent.
"""
import argparse, csv, glob, hashlib, json, os, re, sys, time, unicodedata, urllib.parse, urllib.request

csv.field_size_limit(1 << 30)
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
INC = os.path.join(ROOT, "data/incoming/claude")
OUT = os.path.join(INC, "claude_lead_websites.csv")
DONE = os.path.join(INC, "claude_lead_sites_done.tsv")
COLS = ["buyer_key", "buyer_name", "website", "basis", "qid", "date"]
UA = "canada-contracts-hub-sitefinder/1.0 (+https://github.com/mohamedbiranesy-gif/canada-contracts-hub)"
API = "https://www.wikidata.org/w/api.php?"
TODAY = time.strftime("%Y-%m-%d")
BAD_SITE = re.compile(r"facebook\.com|linkedin\.com|twitter\.com|x\.com|instagram\.com|youtube\.com|wikipedia\.org|web\.archive\.org", re.I)
_last = [0.0]


def norm(s):
    return re.sub(r"[^a-z0-9]+", " ", unicodedata.normalize("NFKD", s or "").encode("ascii", "ignore").decode().lower()).strip()


def get(params, gap=1.0):
    wait = _last[0] + gap - time.time()
    if wait > 0:
        time.sleep(wait)
    _last[0] = time.time()
    for attempt in range(3):
        try:
            req = urllib.request.Request(API + urllib.parse.urlencode(dict(params, format="json")), headers={"User-Agent": UA})
            return json.load(urllib.request.urlopen(req, timeout=30))
        except Exception as e:
            code = getattr(e, "code", 0)
            if code in (429, 503):
                time.sleep(30 * (attempt + 1))
                continue
            return {}
    return {}


def countries_for(cfv):
    return {"Q739"} if "DIAN" in (cfv or "") else {"Q16", "Q30"}


def find_site(name, allowed):
    """(website, qid) for an exact-name Wikidata item with an official website in an allowed country, or None"""
    variants = []
    for v in (name, re.split(r"\s+[-–(]\s*", name)[0]):
        v = re.sub(r"\s+", " ", v).strip()
        if v and v not in variants and len(norm(v).split()) >= 3:
            variants.append(v)
    for v in variants:
        for lang in ("en", "fr") if "Q739" not in allowed else ("es", "en"):
            res = get({"action": "wbsearchentities", "search": v, "language": lang, "limit": 7, "type": "item"}).get("search", [])
            ids = [x["id"] for x in res if norm((x.get("match") or {}).get("text")) == norm(v)]
            if not ids:
                continue
            ents = get({"action": "wbgetentities", "ids": "|".join(ids[:5]), "props": "claims"}).get("entities", {})
            for qid in ids[:5]:
                c = (ents.get(qid) or {}).get("claims", {})
                if any((x.get("mainsnak", {}).get("datavalue", {}).get("value", {}) or {}).get("id") == "Q5" for x in c.get("P31", [])):
                    continue  # a person
                countries = {(x.get("mainsnak", {}).get("datavalue", {}).get("value", {}) or {}).get("id") for x in c.get("P17", [])}
                sites = [x.get("mainsnak", {}).get("datavalue", {}).get("value") for x in c.get("P856", [])]
                sites = [u for u in sites if isinstance(u, str) and u.startswith("http") and not BAD_SITE.search(u)]
                if countries & allowed and sites:
                    return sites[0], qid
    return None


def leads_without_site():
    have = set()
    for p in glob.glob(os.path.join(ROOT, "data/incoming/*/*buyer_ap_results*.csv")):
        try:
            with open(p, encoding="utf-8", errors="replace", newline="") as f:
                for r in csv.DictReader(f):
                    if r.get("buyer_key") and (r.get("ap_email") or "").strip():
                        have.add(r["buyer_key"])
        except Exception:
            pass
    for name in ("claude_buyer_leads.csv", "claude_buyer_leads_cc.csv"):
        p = os.path.join(INC, name)
        if not os.path.exists(p):
            continue
        import lead_store as LS
        for r in LS.reader(p):
            if (r.get("website") or "").strip() or r["buyer_key"] in have:
                continue
            nm = (r.get("buyer_name") or "").strip()
            if nm and not re.fullmatch(r"[\w.-]+\.[a-z]{2,}", nm.lower()):
                yield r["buyer_key"], nm, r.get("canada_field_value") or "", (r.get("latest_record_date") or "")


def run(a):
    k, n = (int(x) for x in a.shard.split("/"))
    done = {l.split("\t")[0] for l in open(DONE, encoding="utf-8")} if os.path.exists(DONE) else set()
    tasks = [t for t in leads_without_site() if t[0] not in done and int(hashlib.sha1(t[0].encode()).hexdigest(), 16) % n == k]
    tasks.sort(key=lambda t: t[3], reverse=True)  # dated relationships first (the newest record first)
    os.makedirs("out", exist_ok=True)
    deadline = time.time() + a.minutes * 60
    found = 0
    print("shard %d/%d: %d lead buyers without a website to look up" % (k, n, len(tasks)), flush=True)
    with open("out/lead_sites_%d.csv" % k, "a", newline="", encoding="utf-8") as fo, open("out/lead_sites_done_%d.tsv" % k, "a", encoding="utf-8") as fd:
        w = csv.writer(fo)
        for i, (key, name, cfv, _d) in enumerate(tasks):
            if time.time() > deadline or (a.limit and i >= a.limit):
                break
            hit = None
            try:
                hit = find_site(name, countries_for(cfv))
            except Exception as e:
                print("error", name[:50], type(e).__name__, flush=True)
            if hit:
                found += 1
                w.writerow([key, name, hit[0], "Wikidata %s official website (P856); the item's label equals the buyer's name" % hit[1], hit[1], TODAY])
                fo.flush()
            fd.write("%s\t%s\t%s\n" % (key, TODAY, "found" if hit else "none"))
            if (i + 1) % 200 == 0:
                fd.flush()
                print(time.strftime("%H:%M:%S"), "looked up %d, websites found %d" % (i + 1, found), flush=True)
    print("finished: websites found %d" % found, flush=True)


def merge(a):
    rows = {}
    if os.path.exists(OUT):
        rows = {r["buyer_key"]: r for r in csv.DictReader(open(OUT, encoding="utf-8"))}
    n0 = len(rows)
    for p in sorted(glob.glob(os.path.join(a.merge, "lead_sites_[0-9]*.csv"))):
        for r in csv.reader(open(p, encoding="utf-8")):
            if len(r) >= 6 and r[0].startswith("lead:") and r[2].startswith("http"):
                rows.setdefault(r[0], dict(zip(COLS, r)))
    if rows:
        with open(OUT, "w", newline="", encoding="utf-8") as f:
            w = csv.DictWriter(f, fieldnames=COLS)
            w.writeheader()
            for key in sorted(rows):
                w.writerow(rows[key])
    seen = {}
    for p in [DONE] + sorted(glob.glob(os.path.join(a.merge, "lead_sites_done_*.tsv"))):
        if os.path.exists(p):
            for l in open(p, encoding="utf-8"):
                q = l.rstrip("\n").split("\t")
                if q and q[0]:
                    seen[q[0]] = l.rstrip("\n")
    with open(DONE, "w", encoding="utf-8") as f:
        for key in sorted(seen):
            f.write(seen[key] + "\n")
    print("lead websites: %d (+%d this run); names looked up so far %d" % (len(rows), len(rows) - n0, len(seen)))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--shard", default="0/1")
    ap.add_argument("--minutes", type=float, default=150)
    ap.add_argument("--limit", type=int, default=0)
    ap.add_argument("--merge", default="")
    a = ap.parse_args()
    merge(a) if a.merge else run(a)


if __name__ == "__main__":
    main()
