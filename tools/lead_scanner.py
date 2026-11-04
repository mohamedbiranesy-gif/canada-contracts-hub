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
import argparse, collections, csv, glob, hashlib, json, os, re, sys, time, urllib.parse, urllib.request

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


GENERIC_LABEL = re.compile(r"^(read more|learn more|more|visit|website|site web|click here|here|cliquez ici|en savoir plus|voir|view|link|lien|home|accueil|\W*)$", re.I)
PLATFORMS = re.compile(r"genially|geneanet|issuu|canva|calameo|prezi|eventbrite|surveymonkey|typeform|jotform|wufoo|dropbox|box\.com|"
                       r"sharepoint|onedrive|wetransfer|spotify|soundcloud|apple|android|play\.google|itunes|maps\.|waze|uber|doordash|"
                       r"skipthedishes|opentable|booking\.com|expedia|airbnb|indeed|glassdoor|workopolis|jobboom|imdb|archive\.org", re.I)


def vendor_site_ok(r, freq):
    row = r.get("row") or {}
    label = (row.get("client_label") or "").strip()
    if row.get("pass") in ("logo_wall", "customer_story", "logo"):  # a client logo / story page: the linked domain is the client
        return not PLATFORMS.search(r["domain"]) and freq[r["domain"]] <= 15
    return bool(label) and not GENERIC_LABEL.match(label) and not PLATFORMS.search(r["domain"]) and freq[r["domain"]] <= 15


DATE_KEY = re.compile(r"date|period|posted|paid|issued|signed|award", re.I)
DATE_VAL = re.compile(r"(20\d\d)-?(\d\d)-?(\d\d)")


def latest_date(row):
    """Latest YYYY-MM-DD found in the record's date-like fields (payment, check, award, action dates)."""
    best = ""
    for k, v in (row or {}).items():
        if isinstance(v, str) and DATE_KEY.search(k):
            m = DATE_VAL.search(v)
            if m and m.group(0)[:4] <= time.strftime("%Y"):
                d = "%s-%s-%s" % m.groups()
                best = max(best, d)
    return best


VAL_KEY = re.compile(r"amount|value|total|montant|obligat|award_amount|contract_value|valeur|payment|paid|sum\b|cost|price", re.I)
NOT_VAL = re.compile(r"date|year|count|number|no\b|id\b|code|percent|rate|qty|quantity", re.I)
CUR_KEY = re.compile(r"currency|devise", re.I)
REF_KEY = re.compile(r"award.?id|contract.?(?:id|no|number|num)|\bpo\b|purchase.?order|reference|r[ée]f[ée]rence|num[ée]ro|solicitation|tender|"
                     r"bid.?(?:no|number)|agreement.?(?:no|number)|registration|permit|declaration|internal_id|\bid$|generated_internal_id|docket|filing", re.I)
START_KEY = re.compile(r"start|begin|d[ée]but|effective|from|period_of_performance_start|signed|issue", re.I)
END_KEY = re.compile(r"end|expir|completion|fin\b|until|period_of_performance_(?:current_)?end|closing|termination", re.I)
VADDR_KEY = re.compile(r"(?:vendor|supplier|recipient|contractor|subawardee|payee|fournisseur|shipper|firm|seller)[^a-z]*(?:address|city|state|province|country|postal|zip|location)", re.I)
TITLE_KEY = re.compile(r"description|title|objet|subject|purpose|scope|commodity|service|product|category", re.I)


def record_details(row, platform=""):
    """Contract / payment details carried by the lead's record, for the ranked deliverable's columns."""
    d = {}
    if not isinstance(row, dict):
        return d
    for k, v in row.items():
        if v in (None, "", [], {}):
            continue
        sv = re.sub(r"\s+", " ", str(v)).strip()
        kl = k.lower()
        if "value" not in d and VAL_KEY.search(kl) and not NOT_VAL.search(kl):
            m = re.search(r"-?\$?\s?\d[\d,]*(?:\.\d+)?", sv)
            if m and re.sub(r"[^\d]", "", m.group(0)):
                d["value"] = m.group(0).replace("$", "").replace(" ", "")
        if "currency" not in d and CUR_KEY.search(kl) and re.fullmatch(r"[A-Za-z]{3}", sv):
            d["currency"] = sv.upper()
        if REF_KEY.search(kl) and not re.search(r"date|url|link", kl) and len(sv) <= 60:
            d.setdefault("reference", {})[k] = sv
        if "start" not in d and START_KEY.search(kl) and not END_KEY.search(kl):
            m = re.search(r"(20\d\d|19\d\d)-(\d\d)-(\d\d)", sv)
            if m:
                d["start"] = "-".join(m.groups())
        if "end" not in d and END_KEY.search(kl):
            m = re.search(r"(20\d\d|19\d\d)-(\d\d)-(\d\d)", sv)
            if m:
                d["end"] = "-".join(m.groups())
        if VADDR_KEY.search(kl) and len(sv) <= 120:
            d.setdefault("vendor_address_parts", []).append("%s: %s" % (k, sv))
        if "title" not in d and TITLE_KEY.search(kl) and 3 <= len(sv) <= 200 and not re.search(r"https?://", sv):
            d["title"] = sv
    if "reference" in d:
        d["reference"] = json.dumps(d["reference"], ensure_ascii=False)[:200]
    if "vendor_address_parts" in d:
        d["vendor_address"] = "; ".join(d.pop("vendor_address_parts"))[:200]
    return d


def bridge():
    while True:
        buyers, freq = {}, collections.Counter()
        details = {}  # lead key -> details of its most recent record (owner 2026-11-03: every field the record gives)
        sites = {}  # websites found later for lead buyers (tools/site_finder*.py, us_directories.py): key -> (website, basis)
        wp = os.path.expanduser("~/cch-crawler-state/websites.tsv")
        if os.path.exists(wp):
            for line in open(wp, encoding="utf-8", errors="replace"):
                parts = line.rstrip("\n").split("\t")
                if len(parts) >= 2 and parts[1].startswith("http"):
                    sites[parts[0]] = (parts[1], parts[2] if len(parts) > 2 else "")
        for f in glob.glob(os.path.join(LEADS, "socrata_rel_*.jsonl")):  # how many different vendors link each domain
            for line in open(f, encoding="utf-8"):
                try:
                    r = json.loads(line)
                    freq[r["domain"]] += 1
                except (ValueError, KeyError):
                    continue
        for f in glob.glob(os.path.join(LEADS, "socrata_*.jsonl")):
            for line in open(f, encoding="utf-8"):
                try:
                    r = json.loads(line)
                except ValueError:
                    continue
                if r.get("platform") == "vendor_site" and not vendor_site_ok(r, freq):
                    continue
                name = (r["publisher"] if not r["buyer_unit"] else "%s - %s" % (r["publisher"], r["buyer_unit"])).strip()
                key = "lead:" + hashlib.sha1(("%s|%s" % (r["domain"], name.lower())).encode()).hexdigest()[:16]
                b = buyers.setdefault(key, {"name": name, "website": r["website"] if not r["buyer_unit"] else "", "rows": 0,
                                            "example_vendor": r["vendor"], "dataset_url": r["dataset_url"], "canada": "%s=%s" % (r["canada_field"], r["canada_value"]),
                                            "latest": ""})
                if not b["website"] and key in sites:
                    b["website"] = sites[key][0]
                    if sites[key][1].startswith("clearbit-slug:") and len(sites[key][1]) > 14:
                        b["name"] = sites[key][1][14:].strip() or b["name"]  # a tenant portal's programme title replaced by the employer's name
                b["rows"] += 1
                d = latest_date(r.get("row")) if r.get("platform") != "vendor_site" else ""
                if d > b["latest"] or key not in details:  # keep the most recent record as the example
                    if d > b["latest"]:
                        b.update(latest=d, example_vendor=r["vendor"], dataset_url=r["dataset_url"], canada="%s=%s" % (r["canada_field"], r["canada_value"]))
                    det = record_details(r.get("row"), r.get("platform") or "")
                    if det:
                        det.update(key=key, platform=r.get("platform") or "", record_url=r.get("dataset_url") or "", vendor=r.get("vendor") or "", record_date=d)
                        details[key] = det
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
            w.writerow(["buyer_key", "buyer_name", "website", "canadian_vendor_rows", "example_vendor", "canada_field_value", "evidence_dataset", "latest_record_date"])
            for k, b in sorted(buyers.items()):
                w.writerow([k, b["name"], b["website"], b["rows"], b["example_vendor"], b["canada"], b["dataset_url"], b["latest"]])
        import gzip
        with gzip.open(os.path.join(CRAWLER, "data/incoming/claude/claude_lead_details.jsonl.gz"), "wt", encoding="utf-8") as f:
            for k in sorted(details):
                f.write(json.dumps(details[k], ensure_ascii=False) + "\n")
        print(time.strftime("%H:%M"), "bridge: %d lead buyers, %d with record details" % (len(buyers), len(details)), flush=True)
        time.sleep(1800)


if __name__ == "__main__":
    a = argparse.ArgumentParser()
    a.add_argument("--shard", type=int, default=0)
    a.add_argument("--of", type=int, default=1)
    a.add_argument("--bridge", action="store_true")
    a = a.parse_args()
    os.makedirs(LEADS, exist_ok=True)
    bridge() if a.bridge else scan(a.shard, a.of)
