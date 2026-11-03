#!/usr/bin/env python3
"""Crawl task list of the world's larger companies (Wikidata: 3,000+ employees, or listed, with an official website).
Large companies publish supplier / invoicing pages far more often than small ones, and their sites carry the Canadian
SaaS signatures tools/tech_relationships.py --reverse looks for (Shopify, Coveo, Unbounce, Lightspeed, Benevity links).
Output: ~/cch-crawl-some/big_companies.csv in tools/crawl_some.py's task format (buyer_key wd:<QID>).
  python3 contrib/claude/org_task_lists/big_companies.py [--min-employees 3000]
"""
import argparse, csv, json, os, re, time, urllib.parse, urllib.request

UA = "canada-contracts-hub-crawler/1.0 (+https://github.com/mohamedbiranesy-gif/canada-contracts-hub)"
OUT = os.path.expanduser("~/cch-crawl-some/big_companies.csv")
CACHE = os.path.expanduser("~/cch-crawler-state/wikidata_big_companies.json")
a = argparse.ArgumentParser()
a.add_argument("--min-employees", type=int, default=3000)
a = a.parse_args()
def sparql(q):
    url = "https://query.wikidata.org/sparql?format=json&query=" + urllib.parse.quote(q)
    req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept": "application/sparql-results+json"})
    with urllib.request.urlopen(req, timeout=300) as r:
        return json.loads(r.read().decode("utf-8"))["results"]["bindings"]


if os.path.exists(CACHE) and time.time() - os.path.getmtime(CACHE) < 14 * 86400:
    rows = json.load(open(CACHE))
else:
    rows, seen_q = [], set()
    # small queries (one instance-of class, one employee band each) keep under the endpoint's 60 s limit
    classes = ("Q4830453", "Q891723", "Q6881511", "Q783794", "Q1058914", "Q161726", "Q18388277", "Q134161", "Q1589009")
    bands = [(a.min_employees, 5000), (5000, 10000), (10000, 20000), (20000, 50000), (50000, 100000), (100000, 10 ** 8)]
    for cls in classes:
        for lo, hi in bands:
            q = """SELECT DISTINCT ?c ?cLabel ?web ?countryLabel ?emp WHERE {
              ?c wdt:P31 wd:%s ; wdt:P856 ?web ; wdt:P1128 ?emp . FILTER(?emp >= %d && ?emp < %d)
              OPTIONAL { ?c wdt:P17 ?country . }
              SERVICE wikibase:label { bd:serviceParam wikibase:language "en,fr,de,es". } } LIMIT 20000""" % (cls, lo, hi)
            try:
                bs = sparql(q)
            except Exception as e:
                print("sparql %s %d-%d: %s" % (cls, lo, hi, e))
                time.sleep(10)
                continue
            for b in bs:
                qid = b["c"]["value"].rsplit("/", 1)[-1]
                if qid in seen_q:
                    continue
                seen_q.add(qid)
                rows.append({"qid": qid, "name": b["cLabel"]["value"], "web": b["web"]["value"],
                             "country": (b.get("countryLabel") or {}).get("value", ""), "emp": int(float(b["emp"]["value"]))})
            time.sleep(2)
    json.dump(rows, open(CACHE, "w"))
seen, out = set(), []
for r in sorted(rows, key=lambda x: -x["emp"]):
    h = (urllib.parse.urlparse(r["web"]).hostname or "").lower().removeprefix("www.")
    if not h or h in seen or re.fullmatch(r"Q\d+", r["name"]):
        continue
    seen.add(h)
    out.append(r)
os.makedirs(os.path.dirname(OUT), exist_ok=True)
with open(OUT, "w", newline="", encoding="utf-8") as f:
    w = csv.writer(f)
    w.writerow(["task_id", "org_group", "buyer_key", "buyer_name", "other_spellings", "country", "known_website",
                "known_general_email", "known_procurement_email", "contracts_in_dataset"])
    for i, r in enumerate(out, 1):
        h = (urllib.parse.urlparse(r["web"]).hostname or "").lower()
        w.writerow(["CL-BIG-%05d" % i, "", "wd:" + r["qid"], r["name"][:120], "", r["country"][:40], "https://%s/" % h, "", "", 0])
print("companies: %d -> %s" % (len(out), OUT))
