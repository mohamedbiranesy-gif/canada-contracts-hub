#!/usr/bin/env python3
"""Find NEW buyers that pay Canadian vendors, in government open-data portals (Socrata, US + EU). No AI.

Many cities, counties, states and agencies publish their vendor payments / purchase orders / contracts on Socrata
with the vendor's state or country. A row whose own state field is a Canadian province (ON, QC, BC ...) or whose
country field says CAN/CANADA proves that the publishing body paid a vendor located in Canada (hard rule 1: the
source's own field says so; "CA" is never read as Canada).

  python3 tools/lead_scanner.py --shard I --of N     scan the portals whose domain hash falls in shard I
  python3 tools/lead_scanner.py --bridge             every 30 min: turn all leads into crawler tasks + an evidence CSV

Leads: ~/cch-leads/socrata_<I>.jsonl. Bridge output (picked up by tools/ap_crawler.py, which finds the invoicing
e-mail on each buyer's own website): coord/tasks/claude/claude_buyer_ap_batch901.csv (local) and
data/incoming/claude/claude_buyer_leads.csv (pushed with the crawler's results).
Polite: one request per second per host; the shared catalog is fetched once (by whichever shard gets the lock).
"""
import argparse, csv, glob, hashlib, json, os, re, sys, time, urllib.parse, urllib.request

LEADS = os.path.expanduser("~/cch-leads")
CRAWLER = os.path.expanduser("~/cch-crawler")
UA = "canada-contracts-hub-leads/1.0 (+https://github.com/mohamedbiranesy-gif/canada-contracts-hub)"
CATALOGS = ["https://api.us.socrata.com/api/catalog/v1", "https://api.eu.socrata.com/api/catalog/v1"]
QUERIES = ["vendor payments", "payments to vendors", "checkbook", "expenditures", "purchase orders", "contracts",
           "vendor", "payee", "supplier", "accounts payable", "spending", "procurement", "awards", "invoices",
           "warrants", "disbursements", "ledger", "purchasing card", "p-card", "contract awards"]
PROV = ["ON", "QC", "BC", "AB", "MB", "SK", "NS", "NB", "NL", "PE", "YT", "NT", "NU", "ONTARIO", "QUEBEC", "QUÉBEC",
        "BRITISH COLUMBIA", "ALBERTA", "MANITOBA", "SASKATCHEWAN", "NOVA SCOTIA", "NEW BRUNSWICK", "NEWFOUNDLAND",
        "NEWFOUNDLAND AND LABRADOR", "PRINCE EDWARD ISLAND", "YUKON", "NORTHWEST TERRITORIES", "NUNAVUT"]
VENDOR = re.compile(r"vendor|payee|supplier|merchant|contractor|recipient|company|business|firm|awardee", re.I)
COUNTRY = re.compile(r"country", re.I)
STATE = re.compile(r"(^|_)(state|province|prov|st|state_code|vendor_state|payee_state|supplier_state)(_|$)", re.I)
UNIT = re.compile(r"agency|department|dept|organization|organisation|division|entity|office|ministry", re.I)
last = {}


def get(url):
    host = urllib.parse.urlparse(url).hostname
    wait = last.get(host, 0) + 1.0 - time.time()
    if wait > 0:
        time.sleep(wait)
    last[host] = time.time()
    try:
        req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept": "application/json"})
        with urllib.request.urlopen(req, timeout=60) as r:
            return json.loads(r.read(30_000_000).decode("utf-8", "replace"))
    except Exception:
        return None


def catalog():
    path = os.path.join(LEADS, "socrata_catalog.json")
    lock = path + ".lock"
    while not os.path.exists(path):
        try:
            fd = os.open(lock, os.O_CREAT | os.O_EXCL)
        except FileExistsError:
            time.sleep(30)
            if os.path.exists(lock) and time.time() - os.path.getmtime(lock) > 4 * 3600:
                os.remove(lock)  # a builder died
            continue
        found = {}
        for api in CATALOGS:
            for q in QUERIES:
                for off in range(0, 10000, 100):
                    d = get("%s?%s" % (api, urllib.parse.urlencode({"q": q, "only": "dataset", "limit": 100, "offset": off})))
                    res = (d or {}).get("results") or []
                    for x in res:
                        r, m = x.get("resource") or {}, x.get("metadata") or {}
                        cols = r.get("columns_field_name") or []
                        if r.get("id") and any(VENDOR.search(c) for c in cols) and any(COUNTRY.search(c) or STATE.search(c) for c in cols):
                            found[r["id"]] = {"id": r["id"], "domain": m.get("domain"), "name": r.get("name"), "cols": cols,
                                              "attribution": r.get("attribution") or "", "attribution_link": r.get("attribution_link") or "",
                                              "link": x.get("permalink") or x.get("link")}
                    if len(res) < 100:
                        break
        json.dump(list(found.values()), open(path + ".tmp", "w"))
        os.replace(path + ".tmp", path)
        os.close(fd)
        os.remove(lock)
    return json.load(open(path))


def website(ds):
    if ds.get("attribution_link", "").startswith("http"):
        p = urllib.parse.urlparse(ds["attribution_link"])
        return "https://%s/" % p.hostname
    host = re.sub(r"^(data|opendata|open|datahub|datacatalog|performance|checkbook|transparency|finance)[.-]", "", ds["domain"] or "")
    return "https://%s/" % host if host else ""


def scan(shard, of):
    out = os.path.join(LEADS, "socrata_%02d.jsonl" % shard)
    done = set(l.split("\t")[0] for l in open(out + ".done")) if os.path.exists(out + ".done") else set()
    mine = [d for d in catalog() if d.get("domain") and int(hashlib.sha1(d["domain"].encode()).hexdigest(), 16) % of == shard]
    print("shard %d: %d datasets" % (shard, len(mine)), flush=True)
    for ds in mine:
        if ds["id"] in done:
            continue
        hits = 0
        for col in ds["cols"]:
            if COUNTRY.search(col):
                vals = "'CAN','CANADA'"
            elif STATE.search(col) and not re.search(r"statu|statement", col, re.I):
                vals = ",".join("'%s'" % v for v in PROV)
            else:
                continue
            where = "upper(trim(`%s`)) in (%s)" % (col, vals)
            rows = get("https://%s/resource/%s.json?%s" % (ds["domain"], ds["id"], urllib.parse.urlencode({"$where": where, "$limit": 500})))
            if not isinstance(rows, list):
                continue
            unitcol = next((c for c in ds["cols"] if UNIT.search(c) and not VENDOR.search(c)), None)
            vcol = next((c for c in ds["cols"] if VENDOR.search(c) and "name" in c.lower()), None) or next(c for c in ds["cols"] if VENDOR.search(c))
            with open(out, "a", encoding="utf-8") as f:
                for r in rows:
                    f.write(json.dumps({"platform": "socrata", "domain": ds["domain"], "dataset_id": ds["id"], "dataset": ds["name"],
                                        "dataset_url": ds.get("link"), "publisher": ds["attribution"] or ds["domain"],
                                        "buyer_unit": (r.get(unitcol) if unitcol else "") or "", "website": website(ds),
                                        "vendor": r.get(vcol, ""), "canada_field": col, "canada_value": r.get(col), "row": r},
                                       ensure_ascii=False) + "\n")
            hits += len(rows)
        open(out + ".done", "a").write("%s\t%d\n" % (ds["id"], hits))
        if hits:
            print("shard %d: %s %s -> %d Canadian-vendor rows" % (shard, ds["domain"], ds["id"], hits), flush=True)
    print("shard %d finished" % shard, flush=True)


def bridge():
    while True:
        buyers = {}
        for f in glob.glob(os.path.join(LEADS, "socrata_*.jsonl")):
            for line in open(f, encoding="utf-8"):
                try:
                    r = json.loads(line)
                except ValueError:
                    continue
                name = (r["publisher"] if not r["buyer_unit"] else "%s - %s" % (r["publisher"], r["buyer_unit"])).strip()
                key = "lead:" + hashlib.sha1(("%s|%s" % (r["domain"], name.lower())).encode()).hexdigest()[:16]
                b = buyers.setdefault(key, {"name": name, "website": r["website"] if not r["buyer_unit"] else "", "rows": 0,
                                            "example_vendor": r["vendor"], "dataset_url": r["dataset_url"], "canada": "%s=%s" % (r["canada_field"], r["canada_value"])})
                b["rows"] += 1
        os.makedirs(os.path.join(CRAWLER, "coord/tasks/claude"), exist_ok=True)
        os.makedirs(os.path.join(CRAWLER, "data/incoming/claude"), exist_ok=True)
        with open(os.path.join(CRAWLER, "coord/tasks/claude/claude_buyer_ap_batch901.csv"), "w", newline="", encoding="utf-8") as f:
            w = csv.writer(f)
            w.writerow(["task_id", "org_group", "buyer_key", "buyer_name", "other_spellings", "country", "known_website",
                        "known_general_email", "known_procurement_email", "contracts_in_dataset"])
            for i, (k, b) in enumerate(sorted(buyers.items(), key=lambda kv: -kv[1]["rows"]), 1):
                w.writerow(["CL-LD-%05d" % i, "", k, b["name"], "", "", b["website"], "", "", b["rows"]])
        with open(os.path.join(CRAWLER, "data/incoming/claude/claude_buyer_leads.csv"), "w", newline="", encoding="utf-8") as f:
            w = csv.writer(f)
            w.writerow(["buyer_key", "buyer_name", "website", "canadian_vendor_rows", "example_vendor", "canada_field_value", "evidence_dataset"])
            for k, b in sorted(buyers.items()):
                w.writerow([k, b["name"], b["website"], b["rows"], b["example_vendor"], b["canada"], b["dataset_url"]])
        print(time.strftime("%H:%M"), "bridge: %d lead buyers" % len(buyers), flush=True)
        time.sleep(1800)


if __name__ == "__main__":
    a = argparse.ArgumentParser()
    a.add_argument("--shard", type=int, default=0)
    a.add_argument("--of", type=int, default=1)
    a.add_argument("--bridge", action="store_true")
    a = a.parse_args()
    os.makedirs(LEADS, exist_ok=True)
    bridge() if a.bridge else scan(a.shard, a.of)
