#!/usr/bin/env python3
"""Find NEW buyers that pay Canadian vendors in CKAN open-data portals (data.gov harvests thousands of US cities,
counties, states and agencies; plus Canadian federal, provincial and municipal portals). No AI.

Each published CSV of payments / contracts / purchase orders is streamed; a row counts only when its own vendor
state/province field is a Canadian province or its country field says CAN/CANADA ("CA" is never read as Canada).
  python3 tools/ckan_scanner.py --shard I --of N
Leads go to ~/cch-leads/socrata_ckan_<I>.jsonl (same format as tools/lead_scanner.py, so its --bridge picks them up).
Polite: one request per second per host; CSVs read up to 150 MB; the catalog is fetched once (lock file).
"""
import argparse, codecs, csv, hashlib, json, os, re, sys, time, urllib.parse, urllib.request
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from lead_scanner import PROV, VENDOR, COUNTRY, STATE, UNIT, LEADS, UA, get

PORTALS = ["https://catalog.data.gov", "https://data.ca.gov", "https://open.canada.ca/data/en", "https://data.ontario.ca",
           "https://open.alberta.ca", "https://catalogue.data.gov.bc.ca", "https://www.donneesquebec.ca/recherche",
           "https://donnees.montreal.ca", "https://ckan0.cf.opendata.inter.prod-toronto.ca", "https://data.wprdc.org",
           "https://opendata.nhsbsa.net", "https://data.gov.ie", "https://data.gov.uk"]
QUERIES = ["vendor payments", "payments to vendors", "checkbook", "expenditures", "purchase orders", "contracts awarded",
           "vendor", "payee", "supplier payments", "accounts payable", "spending", "procurement", "contrats octroyés",
           "fournisseurs", "paiements", "disbursements", "warrants", "contract awards", "invoices paid", "transparency"]
PROVSET = set(PROV)


def catalog():
    path = os.path.join(LEADS, "ckan_catalog.json")
    lock = path + ".lock"
    while not os.path.exists(path):
        try:
            fd = os.open(lock, os.O_CREAT | os.O_EXCL)
        except FileExistsError:
            time.sleep(30)
            if os.path.exists(lock) and time.time() - os.path.getmtime(lock) > 4 * 3600:
                os.remove(lock)
            continue
        found = {}
        for base in PORTALS:
            for q in QUERIES:
                for start in range(0, 3000, 1000):
                    d = get("%s/api/3/action/package_search?%s" % (base, urllib.parse.urlencode({"q": q, "rows": 1000, "start": start})))
                    res = ((d or {}).get("result") or {}).get("results") or []
                    for p in res:
                        org = (p.get("organization") or {}).get("title") or p.get("author") or p.get("maintainer") or ""
                        for r in p.get("resources") or []:
                            u = (r.get("url") or "").strip()
                            if u.startswith("http") and ((r.get("format") or "").lower() == "csv" or u.lower().split("?")[0].endswith(".csv")):
                                found[u] = {"url": u, "publisher": org, "dataset": p.get("title"), "portal": base,
                                            "dataset_url": "%s/dataset/%s" % (base, p.get("name"))}
                    if len(res) < 1000:
                        break
        json.dump(list(found.values()), open(path + ".tmp", "w"))
        os.replace(path + ".tmp", path)
        os.close(fd)
        os.remove(lock)
    return json.load(open(path))


def scan(shard, of):
    out = os.path.join(LEADS, "socrata_ckan_%02d.jsonl" % shard)
    done = set(l.split("\t")[0] for l in open(out + ".done")) if os.path.exists(out + ".done") else set()
    mine = [r for r in catalog() if int(hashlib.sha1((urllib.parse.urlparse(r["url"]).hostname or "").encode()).hexdigest(), 16) % of == shard]
    print("shard %d: %d CSV files" % (shard, len(mine)), flush=True)
    last = {}
    for res in mine:
        if res["url"] in done:
            continue
        host = urllib.parse.urlparse(res["url"]).hostname or ""
        time.sleep(max(0, last.get(host, 0) + 1.0 - time.time()))
        last[host] = time.time()
        hits = 0
        try:
            req = urllib.request.Request(res["url"], headers={"User-Agent": UA})
            with urllib.request.urlopen(req, timeout=60) as r:
                lines = codecs.iterdecode(iter(lambda: r.readline(1_000_000), b""), "utf-8", errors="replace")
                rd = csv.reader(lines)
                head = [h.strip() for h in next(rd, [])]
                cc = [i for i, h in enumerate(head) if COUNTRY.search(h)]
                sc = [i for i, h in enumerate(head) if STATE.search(h.replace(" ", "_")) and not re.search(r"statu|statement", h, re.I)]
                vc = next((i for i, h in enumerate(head) if VENDOR.search(h)), None)
                uc = next((i for i, h in enumerate(head) if UNIT.search(h) and not VENDOR.search(h)), None)
                if vc is not None and (cc or sc):
                    read = 0
                    with open(out, "a", encoding="utf-8") as f:
                        for row in rd:
                            read += len(",".join(row)) + 1
                            if read > 150_000_000 or hits >= 2000:
                                break
                            hit = next(((head[i], row[i]) for i in cc if i < len(row) and row[i].strip().upper() in ("CAN", "CANADA")), None) or \
                                  next(((head[i], row[i]) for i in sc if i < len(row) and row[i].strip().upper() in PROVSET), None)
                            if hit:
                                hits += 1
                                f.write(json.dumps({"platform": "ckan", "domain": host, "dataset_id": res["url"], "dataset": res["dataset"],
                                                    "dataset_url": res["dataset_url"], "publisher": res["publisher"] or host,
                                                    "buyer_unit": (row[uc] if uc is not None and uc < len(row) else "") or "",
                                                    "website": "" if re.search(r"amazonaws|cloudfront|blob\.core|googleapis|github|azureedge|socrata|arcgis", host) else "https://%s/" % re.sub(r"^(data|opendata|open|www)\.", "", host),
                                                    "vendor": row[vc] if vc < len(row) else "", "canada_field": hit[0], "canada_value": hit[1],
                                                    "row": dict(zip(head, row))}, ensure_ascii=False) + "\n")
        except Exception as e:
            print("shard %d: skip %s (%s)" % (shard, res["url"][:90], type(e).__name__), flush=True)
        open(out + ".done", "a").write("%s\t%d\n" % (res["url"], hits))
        if hits:
            print("shard %d: %s -> %d Canadian-vendor rows (%s)" % (shard, res["url"][:90], hits, res["publisher"]), flush=True)
    print("shard %d finished" % shard, flush=True)


if __name__ == "__main__":
    a = argparse.ArgumentParser()
    a.add_argument("--shard", type=int, default=0)
    a.add_argument("--of", type=int, default=1)
    a = a.parse_args()
    os.makedirs(LEADS, exist_ok=True)
    scan(a.shard, a.of)
