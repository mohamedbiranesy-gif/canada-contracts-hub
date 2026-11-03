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
if os.path.exists(CACHE) and time.time() - os.path.getmtime(CACHE) < 14 * 86400:
    rows = json.load(open(CACHE))
else:
    q = """SELECT DISTINCT ?c ?cLabel ?web ?countryLabel ?emp WHERE {
      ?c wdt:P31/wdt:P279* wd:Q4830453 ; wdt:P856 ?web ; wdt:P1128 ?emp .
      FILTER(?emp >= %d)
      OPTIONAL { ?c wdt:P17 ?country . }
      SERVICE wikibase:label { bd:serviceParam wikibase:language "en,fr,de,es". }
    } LIMIT 40000""" % a.min_employees
    url = "https://query.wikidata.org/sparql?format=json&query=" + urllib.parse.quote(q)
    req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept": "application/sparql-results+json"})
    with urllib.request.urlopen(req, timeout=300) as r:
        data = json.loads(r.read().decode("utf-8"))
    rows = [{"qid": b["c"]["value"].rsplit("/", 1)[-1], "name": b["cLabel"]["value"], "web": b["web"]["value"],
             "country": (b.get("countryLabel") or {}).get("value", ""), "emp": int(float(b["emp"]["value"]))} for b in data["results"]["bindings"]]
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
