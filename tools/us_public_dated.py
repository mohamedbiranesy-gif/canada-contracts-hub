#!/usr/bin/env python3
"""Dated buyer leads from US public records whose own vendor address says Canada (one tool, --source flag). No AI.

Every source below prints the vendor's location in the same record (or, for TX DIR, in the same publisher's archive of
the same contract sales), so "vendor in Canada" is proven by the source itself, never inferred from a name. Buyer = the
public body named in the record. Kept: records dated on or after 2023-11-02 (WINDOW). One output line per
(buyer, vendor) pair, the most recent record kept, in ~/cch-leads/socrata_<key>.jsonl (overwritten on each run).
Bulk files are downloaded once into ~/cch-sources/<source>/ (rerun with --refresh to fetch again). At most 2 requests
per second per host, identified User-Agent; a 401/403/429 or a challenge page marks the source blocked (no retries
around it). Persons are dropped (payees that look like "FIRST M LAST" / "LAST, FIRST" with no organisation word), and
so are refunds (WyOpen rows with a Revenue Source, ND rows whose expenditure category says refund).

Sources (key -> output file):
  tx1295  Texas Ethics Commission Form 1295 certificates, bulk CSV (no header), recordType BOX123:
          https://www.ethics.texas.gov/data/search/1295/1295Certificates_2026_to_2030.csv and ..._2021_to_2025.csv
          buyer governmentName (+governmentTypeCd); Canada = businessCountryCode == "CAN" (businessStateCode is junk for
          Canadian filers and is ignored); date acknowledgeDate. Rows whose governmentName equals the businessName are
          dropped; CAN rows with a US city / "US Inc" name get qa_flag. Buyer website: DIR customer list
          (data.texas.gov 4v6c-qfkr customer_website) on an exact name match, else Wikidata.
          -> socrata_tx1295.jsonl
  walni2  Washington L&I prevailing-wage Intents (data.wa.gov t9je-9qwa) and Affidavits (9ncw-tqjn): buyer agencyname;
          Canada = companystate / state is a province or territory (code or name), or the postal code is Canadian, or
          the address text says CANADA (not "La Canada"); date application_received_date (else cntrct_award_dt) for
          intents, formreceiveddate for affidavits. -> socrata_walni2.jsonl
  ndcheck North Dakota OMB checkbook mass downloads (xlsx, FY24, FY25, FY26 and FY27-to-date):
          https://www.omb.nd.gov/sites/default/files/documents/financial-transparency/transparency/mass_download_*.xlsx
          columns Biennium, Fiscal Year, Date (month end), Agency, Vendor, City, State, ...; Canada = State is a province
          or City ends in CANADA. -> socrata_ndcheck.jsonl
  wyopen  WyOpen (Wyoming State Auditor checkbook): POST https://www.wyopen.gov/search/results with startdate/enddate and
          location=<province code>, then the session's CSV export https://www.wyopen.gov/search/csv; Canada = the State
          column equals the province code (location is a substring search, so other rows are discarded); date Check
          Date; rows with a Revenue Source (refunds, licence refunds) and payees suffixed "-REF" (refunds) dropped. -> socrata_wyopen.jsonl
  sdcheck South Dakota BFM checkbook CSVs: https://bfm.sd.gov/ledger/VendorPmts.csv (vendor_number, vendor_group_number,
          city, state) joined on (vendor_number, vendor_group_number) to CheckbookDetailCurrentYear.csv,
          CheckbookDetailPriorYear1.csv, CheckbookDetailPriorYear2.csv (agency code, ap_payment_date, amt). Agency codes
          named from the BFM budget agency listing (https://bfm.sd.gov/budget/rec14/expTOC.HTM, current department
          names; code 25 is not in it and is skipped); Canada = vendor state is a province. Payments with amt <= 0
          skipped. bfm.sd.gov timed out from the owner's Mac on 2026-11-02 (no HTTP answer), so that day's output was
          built by the same tool from the cloud session's copy of the files. -> socrata_sdcheck.jsonl
  mdpay   Maryland "State of Maryland Payments Data" (opendata.maryland.gov 7syw-q4cy: agency_name, vendor_name,
          vendor_zip, fiscal_year; fiscal_period / date are placeholders) and "County Board of Education - Spending
          Disclosures" (t6vk-rvwe: agency_name, payee_name, payee_zip, fiscal_year). Canada = the zip field is a Canadian
          postal code (A9A...). Fiscal-year-only records: only fiscal years that start inside the window are kept
          (FY2025+, Maryland FY starts July 1) and record_date is the first day of that fiscal year (never overstates
          recency). -> socrata_mdpay.jsonl
  txdir   Texas DIR cooperative contract sales: archive data.texas.gov w64c-ndf7 (FY2010-FY2025, vendor_address /
          vendor_city / vendor_state / vendor_zip in each row) plus current VSR a743-wj72 (FY2026+, no vendor address),
          joined on the exact vendor name to the archive's Canadian address (same publisher). Canada = vendor_zip is a
          Canadian postal code, or vendor_state is a province with a non-US zip. Date: archive shipped_date / purchase
          month, VSR invoice_date. -> socrata_txdir.jsonl
  (WA DES statewide contract sales, data.wa.gov n8q6-4twj, was checked: no DES table on data.wa.gov gives a vendor
  address (Agency Contracts FY2019-2025 tables have none), so it yields nothing under the Canada rule.)

Buyer website when the source has none: Wikidata item whose label or alias equals the buyer name (cleaned variants:
"X, CITY OF" -> "City of X", "X ISD" -> "X Independent School District"), with an official website (P856) and the
state's name in its description or label; one request per second; cache ~/cch-sources/wikidata_sites.json.

Counts seen on 2026-11-02 are printed by each run and kept in ~/cch-leads/socrata_<key>.jsonl.stats.

  python3 tools/us_public_dated.py --source all|tx1295|walni2|ndcheck|wyopen|sdcheck|mdpay|txdir [--refresh] [--no-wikidata]
"""
import argparse, csv, datetime, io, json, os, re, sys, time, unicodedata, urllib.error, urllib.parse, urllib.request, zipfile
import http.cookiejar
import xml.etree.ElementTree as ET

UA = "canada-contracts-hub-crawler/1.0 (+https://github.com/mohamedbiranesy-gif/canada-contracts-hub)"
SOURCES = os.path.expanduser("~/cch-sources")
LEADS = os.path.expanduser("~/cch-leads")
WINDOW = "2023-11-02"
RECENT = "2025-11-02"
TODAY = datetime.date.today().isoformat()
PROV = {"AB", "BC", "MB", "NB", "NL", "NS", "NT", "NU", "ON", "PE", "QC", "SK", "YT"}
PROV_NAMES = {"ALBERTA", "BRITISH COLUMBIA", "MANITOBA", "NEW BRUNSWICK", "NEWFOUNDLAND", "NEWFOUNDLAND AND LABRADOR",
              "NOVA SCOTIA", "NORTHWEST TERRITORIES", "NUNAVUT", "ONTARIO", "PRINCE EDWARD ISLAND", "QUEBEC", "QUÉBEC",
              "SASKATCHEWAN", "YUKON", "PQ"}
POSTAL = re.compile(r"^[ABCEGHJ-NPRSTVXY]\d[ABCEGHJ-NPRSTV-Z](?:[ -]?\d(?:[ABCEGHJ-NPRSTV-Z]\d?)?)?$", re.I)
ORG = re.compile(r"\b(inc|incorporated|ltd|ltee|ltée|limited|llc|llp|lp|ulc|corp|corporation|co|company|plc|gmbh|ag|sa|"
                 r"group|services?|systems?|solutions?|technolog\w*|tech|software|consult\w*|engineer\w*|associates?|"
                 r"international|industr\w*|enterprises?|partners?|society|association|universit\w*|college|institute|"
                 r"foundation|cent(?:re|er)|canad\w*|labs?|laborator\w*|research|press|media|products?|manufactur\w*|"
                 r"marine|wireless|electric\w*|construction|contract\w*|design|networks?|communications?|scien\w*|"
                 r"health|medical|pharm\w*|energy|resources|environment\w*|holdings?|bank|insurance|publish\w*|books?|"
                 r"learning|education|training|drones?|steel\w*|works|studios?|management|development|data|digital|"
                 r"analytics|global|america|academy|agency|club|council|board|authority|ministry|government|city|county|"
                 r"district|school|hospital|clinic|supply|supplies|equipment|instruments?|machin\w*|sensors?|dynamics|"
                 r"aerospace|aviation|air|transport\w*|logistics|freight|safety|security|benchmarking|software|turf|"
                 r"fabrication|controls?|automation|innovations?|ventures?|imaging|optics|robotics|devices?|apparel|"
                 r"foods?|farms?|seeds?|genetics|telemetry|wildlife|fisheries|lab|signs?|graphics|printing|"
                 r"interactive|games?|entertainment|productions?|films?|music|records|arts?|museum|library|"
                 r"&|and sons|bros|brothers|mfg|intl|assn|dba|d/b/a)\b", re.I)
PRIVATE_TRUST = re.compile(r"\b(irrevocable|estate of|living trust|family trust|revocable)\b", re.I)
NOT_CANADA = re.compile(r"\b(LA\s+CA[NÑ]ADA|LITTLE\s+CANADA|CANADA\s+(DE|DEL)\b)", re.I)   # La Canada Flintridge CA, Little Canada MN
_last = {}


class Blocked(Exception):
    pass


def norm(s):
    return re.sub(r"[^a-z0-9]+", " ", unicodedata.normalize("NFKD", s or "").encode("ascii", "ignore").decode().lower()).strip()


def buyer_key(name):
    """Same body, different spellings: "Harris County, Texas" / "HARRIS COUNTY"; "Lewisville ISD" / "... Independent School District"."""
    n = norm(name)
    n = re.sub(r"^the ", "", n)
    n = re.sub(r"\b(texas|tx|washington|wa|maryland|md)$", "", n).strip()
    n = re.sub(r"\bcisd\b", "consolidated independent school district", n)
    n = re.sub(r"\bisd\b", "independent school district", n)
    m = re.match(r"^(county|city|town|village|port) of (.+)$", n)
    if m and m.group(1) == "county":
        n = "%s county" % m.group(2)
    m = re.match(r"^(.+) (city|town|port|village) of$", n)
    if m:
        n = "%s of %s" % (m.group(2), m.group(1))
    return n.strip()


LEGAL_END = re.compile(r"(\s+(inc|incorporated|ltd|limited|ltee|corp|corporation|co|company|llc|ulc|lp|plc))+$")


def vendor_key(name):
    return LEGAL_END.sub("", norm(name)).strip()


def is_person(name):
    n = (name or "").strip()
    if not n or norm(n) in ("n a", "na", "none", "unknown", "various"):
        return True
    if PRIVATE_TRUST.search(n):
        return True
    if ORG.search(n) or re.search(r"\d", n):
        return False
    if re.fullmatch(r"[A-Za-z'.-]+,\s*[A-Za-z'.-]+(\s+[A-Za-z]\.?)?(\s+[A-Za-z'.-]+)?", n):
        return True          # "SCHWAB, TIMOTHY V"
    toks = n.replace(".", " ").split()
    return 2 <= len(toks) <= 4 and all(re.fullmatch(r"[A-Za-z'-]+", t) for t in toks)


def canadian_postal(z):
    return bool(POSTAL.match((z or "").strip()))


def wait(host, gap=0.5):
    w = _last.get(host, 0) + gap - time.time()
    if w > 0:
        time.sleep(w)
    _last[host] = time.time()


def fetch(url, data=None, opener=None, gap=0.5, timeout=120, tries=3):
    host = urllib.parse.urlparse(url).hostname
    for i in range(tries):
        wait(host, gap)
        req = urllib.request.Request(url, data=data, headers={"User-Agent": UA, "Accept": "*/*"})
        try:
            with (opener.open(req, timeout=timeout) if opener else urllib.request.urlopen(req, timeout=timeout)) as r:
                body = r.read()
            if b"cf-chl" in body[:5000] or b"captcha" in body[:5000].lower():
                raise Blocked("challenge page at %s" % url)
            return body
        except urllib.error.HTTPError as e:
            if e.code in (401, 403, 429):
                raise Blocked("HTTP %d at %s" % (e.code, url))
            if i == tries - 1 or e.code < 500:
                raise
        except (urllib.error.URLError, TimeoutError, ConnectionError):
            if i == tries - 1:
                raise
        time.sleep(5 * (i + 1))


def cached(source, url, refresh=False, name=None):
    d = os.path.join(SOURCES, source)
    os.makedirs(d, exist_ok=True)
    path = os.path.join(d, name or url.rstrip("/").split("/")[-1].split("?")[0])
    if refresh or not os.path.exists(path) or os.path.getsize(path) == 0:
        print("download", url, flush=True)
        host = urllib.parse.urlparse(url).hostname
        wait(host)
        req = urllib.request.Request(url, headers={"User-Agent": UA})
        try:
            with urllib.request.urlopen(req, timeout=600) as r, open(path + ".part", "wb") as f:
                while True:
                    b = r.read(1 << 20)
                    if not b:
                        break
                    f.write(b)
        except urllib.error.HTTPError as e:
            if e.code in (401, 403, 429):
                raise Blocked("HTTP %d at %s" % (e.code, url))
            raise
        os.replace(path + ".part", path)
    return path


def soda(domain, ds, params, page=50000):
    """All rows of a SODA query (paged with $offset)."""
    out, off = [], 0
    while True:
        q = dict(params, **{"$limit": page, "$offset": off})
        rows = json.loads(fetch("https://%s/resource/%s.json?%s" % (domain, ds, urllib.parse.urlencode(q))))
        out += rows
        if len(rows) < page:
            return out
        off += page


def iso(d):
    d = (d or "").strip()
    m = re.match(r"(\d{4})-?(\d\d)-?(\d\d)", d)
    if m:
        return "%s-%s-%s" % m.groups()
    m = re.match(r"(\d{1,2})/(\d{1,2})/(\d{4})", d)
    if m:
        return "%s-%02d-%02d" % (m.group(3), int(m.group(1)), int(m.group(2)))
    return ""


def state_prefix(state, agency):
    a = re.sub(r"\s+", " ", agency or "").strip()
    return a if norm(state) in norm(a) else "%s %s" % (state, a)


# ---------------------------------------------------------------- output
class Out:
    def __init__(self, key):
        self.key, self.pairs, self.stats = key, {}, {"source_rows_seen": 0, "canada_rows": 0, "in_window": 0,
                                                     "dropped_person": 0, "dropped_refund": 0, "dropped_self": 0}

    def add(self, rec):
        rd = rec["row"].get("record_date", "")
        if not rd or rd < WINDOW or rd > TODAY:
            return
        self.stats["in_window"] += 1
        k = (buyer_key(rec["publisher"]), vendor_key(rec["vendor"]))
        old = self.pairs.get(k)
        n = (old["row"].get("pair_records", 1) if old else 0) + 1
        if not old or rd >= old["row"]["record_date"]:
            self.pairs[k] = rec
        self.pairs[k]["row"]["pair_records"] = n

    def write(self, sites):
        os.makedirs(LEADS, exist_ok=True)
        path = os.path.join(LEADS, "socrata_%s.jsonl" % self.key)
        with open(path + ".tmp", "w", encoding="utf-8") as f:
            for k, r in sorted(self.pairs.items()):
                if not r.get("website"):
                    w = sites.get(r["publisher"], "")
                    if w:
                        r["website"], r["domain"] = w, re.sub(r"^www\.", "", urllib.parse.urlparse(w).hostname or "")
                        r["row"]["website_source"] = "wikidata"
                f.write(json.dumps(r, ensure_ascii=False) + "\n")
        os.replace(path + ".tmp", path)
        buyers = {buyer_key(r["publisher"]) for r in self.pairs.values()}
        recent = {buyer_key(r["publisher"]) for r in self.pairs.values() if r["row"]["record_date"] >= RECENT}
        withsite = {buyer_key(r["publisher"]) for r in self.pairs.values() if r.get("website")}
        self.stats.update(rows=len(self.pairs), buyers=len(buyers), buyers_last12=len(recent), buyers_with_website=len(withsite))
        json.dump(self.stats, open(path + ".stats", "w"), indent=1)
        print(self.key, json.dumps(self.stats), flush=True)
        return self.pairs.values()


def rec(platform, dataset, url, publisher, vendor, cfield, cvalue, row, website="", unit=""):
    host = re.sub(r"^www\.", "", urllib.parse.urlparse(website).hostname or "") if website else ""
    return {"platform": platform, "domain": host, "dataset_id": row.get("_id", ""), "dataset": dataset, "dataset_url": url,
            "publisher": re.sub(r"\s+", " ", publisher).strip(), "buyer_unit": unit, "website": website,
            "vendor": re.sub(r"\s+", " ", vendor or "").strip(), "canada_field": cfield, "canada_value": cvalue,
            "row": {k: v for k, v in row.items() if k != "_id"}}


# ---------------------------------------------------------------- Wikidata websites
WD = "https://www.wikidata.org/w/api.php?"


def wd_get(params):
    try:
        return json.loads(fetch(WD + urllib.parse.urlencode(dict(params, format="json")), gap=1.0, timeout=30, tries=2))
    except Blocked:
        raise
    except Exception:
        return {}


def variants(name):
    n = re.sub(r"\s+", " ", name).strip()
    n = re.sub(r"\s*(#|no\.?\s*)\s*\d+[a-z]?\b", "", n, flags=re.I).strip(" ,-")
    n = re.sub(r",?\s+(texas|tx)$", "", n, flags=re.I).strip(" ,")
    out = [n]
    m = re.match(r"^(.*?),\s*(city|town|port|county|village) of$", n, re.I)
    if m:
        out = ["%s of %s" % (m.group(2).title(), m.group(1).strip())]
    m = re.match(r"^(.*)\s+(c?isd)$", out[0], re.I)
    if m:
        out.append("%s %sIndependent School District" % (m.group(1), "Consolidated " if m.group(2).lower() == "cisd" else ""))
    m = re.match(r"^(city|town|village) of (.+)$", out[0], re.I)
    place = m.group(2) if m else ""
    return list(dict.fromkeys(out)), place


def wikidata_sites(buyers, cache_path):
    """buyers: {publisher: state_name}. Returns {publisher: website}."""
    try:
        cache = json.load(open(cache_path))
    except (OSError, ValueError):
        cache = {}
    out = {}
    for name, state in sorted(buyers.items()):
        ck = "%s|%s" % (name, state)
        if ck not in cache:
            cache[ck] = ""
            names, place = variants(name)
            cands = [(v, False) for v in names] + ([(place, True)] if place else [])
            for v, is_place in cands:
                if len(norm(v)) < 4:
                    continue
                res = wd_get({"action": "wbsearchentities", "search": v, "language": "en", "limit": 10, "type": "item"}).get("search", [])
                ids = [x["id"] for x in res if norm(x.get("label")) == norm(v) or norm((x.get("match") or {}).get("text")) == norm(v)]
                desc = {x["id"]: (x.get("description") or "") for x in res}
                if not ids:
                    continue
                ents = wd_get({"action": "wbgetentities", "ids": "|".join(ids[:6]), "props": "claims|descriptions|labels", "languages": "en"}).get("entities", {})
                hit = ""
                for qid in ids[:6]:
                    e = ents.get(qid) or {}
                    d = desc.get(qid) or ((e.get("descriptions") or {}).get("en") or {}).get("value", "")
                    lab = ((e.get("labels") or {}).get("en") or {}).get("value", "")
                    if norm(state) not in norm(d) and norm(state) not in norm(lab) and norm(state) not in norm(name):
                        continue
                    if is_place and not re.search(r"\b(city|town|village|municipality|borough)\b", d, re.I):
                        continue
                    sites = [(x["mainsnak"].get("datavalue") or {}).get("value") for x in (e.get("claims") or {}).get("P856", [])]
                    sites = [s for s in sites if isinstance(s, str) and s.startswith("http")]
                    if sites:
                        hit = sites[0]
                        break
                if hit:
                    cache[ck] = hit
                    break
            json.dump(cache, open(cache_path, "w"), indent=0)
        if cache[ck]:
            out[name] = cache[ck]
    return out


# ---------------------------------------------------------------- tx1295
TEC = "https://www.ethics.texas.gov/data/search/1295/"
US_CITY = re.compile(r"^(los angeles|new york|lehi|chicago|houston|dallas|austin|san antonio|atlanta|boston|seattle|denver|"
                     r"phoenix|miami|san francisco|san diego|tampa|orlando|minneapolis|detroit|philadelphia|nashville)$", re.I)


def dir_customer_sites():
    """{normalized customer name: website} from the DIR customer list. A website listed for several customers is kept only
    for the customer whose name it spells (the list gives Collin County's site to Montgomery County too)."""
    rows = soda("data.texas.gov", "4v6c-qfkr", {"$select": "customer_name,customer_aka,customer_website"})
    pairs, users = [], {}
    for r in rows:
        w = (r.get("customer_website") or {}).get("url", "") if isinstance(r.get("customer_website"), dict) else ""
        if not w.startswith("http"):
            continue
        host = (urllib.parse.urlparse(w).hostname or "").lower()
        users.setdefault(host, set()).add(tx_norm(r.get("customer_name")))
        for n in (r.get("customer_name"), r.get("customer_aka")):
            if n:
                pairs.append((tx_norm(n), w, host))
    out = {}
    generic = {"county", "city", "independent", "school", "district", "texas", "consolidated", "of", "the", "department",
               "authority", "public", "library", "college", "community", "university", "state"}
    for n, w, host in pairs:
        toks = [t for t in n.split() if len(t) >= 4 and t not in generic]
        if len(users[host]) > 1 and not any(t in host.replace("-", "") for t in toks):
            continue
        out.setdefault(n, w)
    return out


def tx_norm(n):
    n = norm(n)
    n = re.sub(r"\bcisd\b", "consolidated independent school district", n)
    n = re.sub(r"\bisd\b", "independent school district", n)
    n = re.sub(r"\s+(texas|tx)$", "", n)
    return n.strip()


def src_tx1295(o, refresh):
    files = [TEC + "1295Certificates_2026_to_2030.csv", TEC + "1295Certificates_2021_to_2025.csv"]
    try:
        sites = dir_customer_sites()
    except Exception as e:
        print("DIR customer list failed:", e, flush=True)
        sites = {}
    for url in files:
        path = cached("tx1295", url, refresh)
        with open(path, encoding="utf-8", errors="replace", newline="") as f:
            for row in csv.reader(f):
                o.stats["source_rows_seen"] += 1
                if len(row) < 12 or row[0] != "BOX123" or row[9].strip().upper() != "CAN":
                    continue
                o.stats["canada_rows"] += 1
                keys = ["recordType", "certificateNumber", "reportNumber", "acknowledgeDate", "governmentName", "governmentTypeCd",
                        "businessName", "businessCityName", "businessStateCode", "businessCountryCode", "govtContractNumber",
                        "goodsServicesDescr"]
                r = dict(zip(keys, row[:12]))
                gov, biz = r["governmentName"].strip(), r["businessName"].strip()
                if (not gov or norm(gov) in ("n a", "na", "none") or norm(gov) == norm(biz) or vendor_key(gov) == vendor_key(biz)
                        or vendor_key(biz).startswith(vendor_key(gov)) or LEGAL_END.search(norm(gov))):
                    o.stats["dropped_self"] += 1
                    continue
                if is_person(biz):
                    o.stats["dropped_person"] += 1
                    continue
                r["record_date"] = iso(r["acknowledgeDate"])
                r["source_file"] = url
                flags = []
                if US_CITY.match(r["businessCityName"].strip()):
                    flags.append("us_city_with_country_CAN")
                if re.search(r"\b(us|usa|u\.s\.a?\.?)\b", biz, re.I):
                    flags.append("us_entity_name")
                if flags:
                    r["qa_flag"] = ",".join(flags)
                r["_id"] = r["certificateNumber"]
                o.add(rec("us_tx_form1295", "Texas Ethics Commission Form 1295 Certificates of Interested Parties (bulk CSV)", url,
                          gov, biz, "businessCountryCode (TEC Form 1295 CSV)",
                          "%s, %s, %s" % (r["businessCityName"].strip(), r["businessStateCode"].strip(), r["businessCountryCode"].strip()),
                          r, website=sites.get(tx_norm(gov), "")))
    return "Texas"


# ---------------------------------------------------------------- walni2
def wa_canadian(state, zipc, *texts):
    s = (state or "").strip().upper()
    if s in PROV or s in PROV_NAMES:
        return True
    if canadian_postal(zipc):
        return True
    t = " ".join(x or "" for x in texts).upper()
    return bool(re.search(r"\bCANADA\b", t)) and not NOT_CANADA.search(t)


def src_walni2(o, refresh):
    provs = ",".join("'%s'" % p for p in sorted(PROV | PROV_NAMES))
    jobs = [("t9je-9qwa", "intent_id", "companystate", "companyzip", ("companyaddress1", "companycity"),
             "(upper(companystate) in (%s) or upper(companyaddress1) like '%%CANADA%%' or upper(companycity) like '%%CANADA%%' "
             "or companyzip like '_#_%%') and (application_received_date >= '%s' or cntrct_award_dt >= '%s')" % (provs, WINDOW, WINDOW),
             "Washington L&I prevailing wage Intents to Pay", "companyname", ("application_received_date", "cntrct_award_dt")),
            ("9ncw-tqjn", "id", "state", "zipcode", ("address1", "companycity"),
             "(upper(state) in (%s) or upper(address1) like '%%CANADA%%' or upper(companycity) like '%%CANADA%%') "
             "and (formreceiveddate >= '%s' or awarddate >= '%s')" % (provs, WINDOW, WINDOW),
             "Washington L&I prevailing wage Affidavits of Wages Paid", "name", ("formreceiveddate", "awarddate"))]
    for ds, idf, sf, zf, tf, where, title, vf, datef in jobs:
        try:
            rows = soda("data.wa.gov", ds, {"$where": where})
        except urllib.error.HTTPError:
            rows = soda("data.wa.gov", ds, {"$where": where.replace(" or companyzip like '_#_%'", "")})
        for r in rows:
            o.stats["source_rows_seen"] += 1
            if not wa_canadian(r.get(sf), r.get(zf), *[r.get(x) for x in tf]):
                continue
            o.stats["canada_rows"] += 1
            if is_person(r.get(vf)):
                o.stats["dropped_person"] += 1
                continue
            r = {k: (v if isinstance(v, str) else json.dumps(v)) for k, v in r.items()}
            r["record_date"] = next((iso(r.get(d)) for d in datef if iso(r.get(d))), "")
            r["_id"] = "%s:%s" % (ds, r.get(idf, ""))
            addr = ", ".join(x for x in [r.get(tf[0], "").replace("\n", " "), r.get(tf[1], ""), r.get(sf, ""), r.get(zf, "")] if x)
            o.add(rec("us_wa_lni_prevailing_wage", title + " (data.wa.gov %s)" % ds,
                      "https://data.wa.gov/resource/%s.json?%s=%s" % (ds, idf, urllib.parse.quote(r.get(idf, ""))),
                      r.get("agencyname", ""), r.get(vf, ""), "%s (data.wa.gov %s)" % (sf, ds), addr, r))
    return "Washington"


# ---------------------------------------------------------------- ndcheck (stdlib xlsx reader)
NS = "{http://schemas.openxmlformats.org/spreadsheetml/2006/main}"
RNS = "{http://schemas.openxmlformats.org/officeDocument/2006/relationships}"


def col_idx(ref):
    n = 0
    for ch in re.match(r"[A-Z]+", ref).group(0):
        n = n * 26 + ord(ch) - 64
    return n - 1


def xlsx_rows(path):
    z = zipfile.ZipFile(path)
    shared = []
    if "xl/sharedStrings.xml" in z.namelist():
        for ev, el in ET.iterparse(z.open("xl/sharedStrings.xml")):
            if el.tag == NS + "si":
                shared.append("".join(t.text or "" for t in el.iter(NS + "t")))
                el.clear()
    wb = ET.fromstring(z.read("xl/workbook.xml"))
    rels = ET.fromstring(z.read("xl/_rels/workbook.xml.rels"))
    target = {r.get("Id"): r.get("Target") for r in rels}
    for sh in wb.iter(NS + "sheet"):
        t = target[sh.get(RNS + "id")]
        p = t.lstrip("/") if t.startswith("/") else "xl/" + t
        for ev, el in ET.iterparse(z.open(p)):
            if el.tag != NS + "row":
                continue
            vals = {}
            for c in el.iter(NS + "c"):
                typ, v = c.get("t"), c.find(NS + "v")
                if typ == "inlineStr":
                    x = "".join(t.text or "" for t in c.iter(NS + "t"))
                elif v is None:
                    continue
                elif typ == "s":
                    x = shared[int(v.text)]
                else:
                    x = v.text or ""
                vals[col_idx(c.get("r"))] = x
            el.clear()
            if vals:
                yield sh.get("name"), [vals.get(i, "") for i in range(max(vals) + 1)]


ND = "https://www.omb.nd.gov/sites/default/files/documents/financial-transparency/transparency/"


def excel_date(x):
    x = (x or "").strip()
    if re.fullmatch(r"\d+(\.\d+)?", x):
        return (datetime.date(1899, 12, 30) + datetime.timedelta(days=int(float(x)))).isoformat()
    return iso(x)


def src_ndcheck(o, refresh):
    for fn in ("mass_download_checkbook.xlsx", "mass_download_fy26.xlsx", "mass_download_fy25.xlsx", "mass_download_fy24.xlsx"):
        url = ND + fn
        path = cached("ndcheck", url, refresh)
        hdr = None
        for sheet, vals in xlsx_rows(path):
            if "Agency" in vals and "Vendor" in vals:
                hdr = [v.strip() for v in vals]
                continue
            if not hdr:
                continue
            o.stats["source_rows_seen"] += 1
            r = dict(zip(hdr, [v.strip() if isinstance(v, str) else v for v in vals]))
            st, city = (r.get("State") or "").upper(), (r.get("City") or "")
            if not (st in PROV or (not st and re.search(r"\bCANADA$", city.upper()) and not NOT_CANADA.search(city))):
                continue
            o.stats["canada_rows"] += 1
            vendor = r.get("Vendor", "")
            if is_person(vendor):
                o.stats["dropped_person"] += 1
                continue
            if re.search(r"refund", "%s %s" % (r.get("Expenditure Category", ""), r.get("Detailed Expenditure Category", "")), re.I):
                o.stats["dropped_refund"] += 1
                continue
            r["Date"] = excel_date(r.get("Date"))
            r["record_date"], r["source_file"], r["sheet"] = r["Date"], url, sheet
            o.add(rec("us_nd_omb_checkbook", "North Dakota OMB checkbook mass download (%s)" % fn, url,
                      state_prefix("North Dakota", r.get("Agency", "")), vendor, "State (ND OMB checkbook)",
                      "%s, %s" % (city, r.get("State", "")), r))
    return "North Dakota"


# ---------------------------------------------------------------- wyopen
def src_wyopen(o, refresh):
    start = datetime.date.fromisoformat(WINDOW).strftime("%m/%d/%Y")
    end = datetime.date.today().strftime("%m/%d/%Y")
    d = os.path.join(SOURCES, "wyopen")
    os.makedirs(d, exist_ok=True)
    for prov in sorted(PROV):
        path = os.path.join(d, "wyopen_%s_%s_%s.csv" % (prov, start.replace("/", ""), end.replace("/", "")))
        if refresh or not os.path.exists(path):
            jar = http.cookiejar.CookieJar()
            op = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(jar))
            form = urllib.parse.urlencode({"startdate": start, "enddate": end, "agencyid": "", "objectid": "", "subobjectid": "",
                                           "vendorname": "", "location": prov, "MySubmit": "Search"}).encode()
            fetch("https://www.wyopen.gov/search/results", data=form, opener=op)
            body = fetch("https://www.wyopen.gov/search/csv", opener=op, timeout=300)
            open(path, "wb").write(body)
        qurl = "https://www.wyopen.gov/search/results?" + urllib.parse.urlencode({"startdate": start, "enddate": end, "location": prov})
        with open(path, encoding="utf-8", errors="replace", newline="") as f:
            for r in csv.DictReader(f):
                o.stats["source_rows_seen"] += 1
                if (r.get("State") or "").strip().upper() != prov:
                    continue
                o.stats["canada_rows"] += 1
                if (r.get("Revenue Source") or "").strip() not in ("", "NA"):
                    o.stats["dropped_refund"] += 1
                    continue
                vendor = (r.get("Vendor Name") or "").strip()
                if re.search(r"[-\s]REF\.?$", vendor, re.I):   # "IHAUL FREIGHT LTD-REF": a refund payee record
                    o.stats["dropped_refund"] += 1
                    continue
                if is_person(vendor):
                    o.stats["dropped_person"] += 1
                    continue
                r = {k: (v or "").strip() for k, v in r.items() if k}
                r["record_date"] = iso(r.get("Check Date"))
                r["search_form"] = "POST https://www.wyopen.gov/search/results location=%s startdate=%s enddate=%s; CSV export /search/csv" % (prov, start, end)
                o.add(rec("us_wy_wyopen", "WyOpen, Wyoming State Auditor online checkbook (search + CSV export)", qurl,
                          state_prefix("Wyoming", r.get("Agency Name", "")), vendor, "State (WyOpen checkbook)", r.get("State", ""), r))
    return "Wyoming"


# ---------------------------------------------------------------- sdcheck
SD = "https://bfm.sd.gov/ledger/"
SD_AGENCY = {  # BFM budget agency listing codes; names as the departments are called today
    "010": "South Dakota Governor's Office", "011": "South Dakota Bureau of Finance and Management",
    "012": "South Dakota Bureau of Administration", "013": "South Dakota Bureau of Information and Telecommunications",
    "014": "South Dakota Bureau of Human Resources", "02": "South Dakota Department of Revenue",
    "03": "South Dakota Department of Agriculture and Natural Resources", "04": "South Dakota Department of Tourism",
    "06": "South Dakota Department of Game, Fish and Parks", "07": "South Dakota Department of Tribal Relations",
    "08": "South Dakota Department of Social Services", "09": "South Dakota Department of Health",
    "10": "South Dakota Department of Labor and Regulation", "11": "South Dakota Department of Transportation",
    "12": "South Dakota Department of Education", "14": "South Dakota Department of Public Safety",
    "16": "South Dakota Department of the Military", "17": "South Dakota Department of Veterans Affairs",
    "18": "South Dakota Department of Corrections", "19": "South Dakota Department of Human Services",
    "26": "South Dakota Public Utilities Commission", "27": "South Dakota Unified Judicial System",
    "281": "South Dakota Legislative Research Council", "288": "South Dakota Auditor General",
    "29": "South Dakota Attorney General", "30": "South Dakota Office of School and Public Lands",
    "31": "South Dakota Secretary of State", "320": "South Dakota State Treasurer", "321": "South Dakota Investment Council",
    "33": "South Dakota State Auditor"}


def src_sdcheck(o, refresh):
    vend = {}
    with open(cached("sdcheck", SD + "VendorPmts.csv", refresh), encoding="latin-1", newline="") as f:
        for r in csv.DictReader(f):
            if (r.get("state") or "").strip().upper() in PROV:
                vend[(r["vendor_number"].strip(), r["vendor_group_number"].strip())] = r
    unknown = set()
    for fn in ("CheckbookDetailCurrentYear.csv", "CheckbookDetailPriorYear1.csv", "CheckbookDetailPriorYear2.csv"):
        url = SD + fn
        with open(cached("sdcheck", url, refresh), encoding="latin-1", newline="") as f:
            for r in csv.DictReader(f):
                o.stats["source_rows_seen"] += 1
                v = vend.get((r["vendor_number"].strip(), r["vendor_group_number"].strip()))
                if not v:
                    continue
                o.stats["canada_rows"] += 1
                try:
                    if float(r.get("amt") or 0) <= 0:
                        continue
                except ValueError:
                    pass
                if is_person(v["vendor_name"]):
                    o.stats["dropped_person"] += 1
                    continue
                ag = SD_AGENCY.get(r["agency"].strip())
                if not ag:
                    unknown.add(r["agency"].strip())
                    continue
                row = dict(r)
                row.update({"vendor_city": v["city"], "vendor_state": v["state"], "vendor_file": SD + "VendorPmts.csv",
                            "agency_name": ag, "agency_code_list": "https://bfm.sd.gov/budget/rec14/expTOC.HTM",
                            "record_date": iso(r.get("ap_payment_date")), "source_file": url})
                o.add(rec("us_sd_bfm_checkbook", "South Dakota BFM checkbook detail (%s) joined to VendorPmts.csv" % fn, url,
                          ag, v["vendor_name"], "state (SD BFM VendorPmts.csv)", "%s, %s" % (v["city"], v["state"]), row))
    if unknown:
        print("sdcheck: agency codes without a published name, skipped:", sorted(unknown), flush=True)
        o.stats["skipped_unknown_agency_codes"] = sorted(unknown)
    return "South Dakota"


# ---------------------------------------------------------------- mdpay
def src_mdpay(o, refresh):
    fy_min = int(WINDOW[:4]) + (1 if WINDOW[5:] > "07-01" else 0) + 1   # first FY that starts (Jul 1) inside the window
    for ds, zf, vf, title in (("7syw-q4cy", "vendor_zip", "vendor_name", "State of Maryland Payments Data"),
                              ("t6vk-rvwe", "payee_zip", "payee_name", "County Board of Education - Spending Disclosures")):
        fyq = "fiscal_year >= %d" % fy_min if ds == "7syw-q4cy" else "fiscal_year >= '%d'" % fy_min   # t6vk stores it as text
        zips = soda("opendata.maryland.gov", ds, {"$select": "%s,count(*)" % zf, "$group": zf, "$where": fyq})
        can = sorted({z[zf] for z in zips if canadian_postal(z.get(zf)) and not re.fullmatch(r"X+", z.get(zf, ""), re.I)})
        rows = []
        for i in range(0, len(can), 40):
            rows += soda("opendata.maryland.gov", ds, {"$where": "%s and %s in (%s)" % (
                fyq, zf, ",".join("'%s'" % z.replace("'", "''") for z in can[i:i + 40]))})
        for r in rows:
            o.stats["source_rows_seen"] += 1
            o.stats["canada_rows"] += 1
            if is_person(r.get(vf)):
                o.stats["dropped_person"] += 1
                continue
            r["record_date"] = "%d-07-01" % (int(r["fiscal_year"]) - 1)
            r["record_date_basis"] = "first day of Maryland fiscal year %s (the record gives the fiscal year only)" % r["fiscal_year"]
            url = "https://opendata.maryland.gov/resource/%s.json?%s" % (ds, urllib.parse.urlencode(
                {"agency_name": r.get("agency_name", ""), vf: r.get(vf, ""), "fiscal_year": r["fiscal_year"]}))
            pub = r.get("agency_name", "")
            o.add(rec("us_md_payments", "%s (opendata.maryland.gov %s)" % (title, ds), url,
                      state_prefix("Maryland", pub) if ds == "7syw-q4cy" else pub, r.get(vf, ""),
                      "%s (opendata.maryland.gov %s)" % (zf, ds), r.get(zf, ""), r))
    return "Maryland"


# ---------------------------------------------------------------- txdir
def tx_dir_canadian(r):
    z, s = (r.get("vendor_zip") or "").strip(), (r.get("vendor_state") or "").strip().upper()
    t = "%s %s" % (r.get("vendor_address", ""), r.get("vendor_city", ""))
    return canadian_postal(z) or (s in PROV and not re.match(r"^\d{5}", z)) or (
        bool(re.search(r"\bCANADA\b", t, re.I)) and not NOT_CANADA.search(t) and not re.match(r"^\d{5}", z))


def src_txdir(o, refresh):
    try:
        sites = dir_customer_sites()
    except Exception:
        sites = {}
    vend = soda("data.texas.gov", "w64c-ndf7", {"$select": "vendor_name,vendor_address,vendor_city,vendor_state,vendor_zip,max(fiscal_year) as fy",
                                                 "$group": "vendor_name,vendor_address,vendor_city,vendor_state,vendor_zip"})
    can = {}
    for v in vend:
        if tx_dir_canadian(v):
            k = norm(v["vendor_name"])
            if k not in can or v.get("fy", "") > can[k].get("fy", ""):
                can[k] = v
    print("txdir: Canadian-address vendors in the archive:", sorted(v["vendor_name"] for v in can.values()), flush=True)
    names = sorted({v["vendor_name"] for v in can.values()})
    q = lambda n: "'%s'" % n.replace("'", "''")
    # archive rows (vendor address in the same row), FY2024-FY2025
    for i in range(0, len(names), 20):
        rows = soda("data.texas.gov", "w64c-ndf7", {"$where": "fiscal_year >= 2024 and vendor_name in (%s)" % ",".join(q(n) for n in names[i:i + 20])})
        for r in rows:
            o.stats["source_rows_seen"] += 1
            if not tx_dir_canadian(r):
                continue
            o.stats["canada_rows"] += 1
            d = iso(r.get("shipped_date")) or (r.get("purchase_month", "")[:4] + "-" + r.get("purchase_month", "")[4:6] + "-01" if len(r.get("purchase_month", "")) >= 6 else "")
            r["record_date"] = d
            url = "https://data.texas.gov/resource/w64c-ndf7.json?" + urllib.parse.urlencode({"vendor_name": r["vendor_name"], "customer_name": r.get("customer_name", "")})
            o.add(rec("us_tx_dir_sales", "Texas DIR cooperative contract sales archive (data.texas.gov w64c-ndf7)", url,
                      r.get("customer_name", ""), r["vendor_name"], "vendor_state / vendor_zip (data.texas.gov w64c-ndf7)",
                      ", ".join(x for x in [r.get("vendor_address", ""), r.get("vendor_city", ""), r.get("vendor_state", ""), r.get("vendor_zip", "")] if x),
                      r, website=sites.get(tx_norm(r.get("customer_name", "")), "")))
    # current VSR (FY2026+), vendor address from the archive row of the same vendor name
    for i in range(0, len(names), 20):
        rows = soda("data.texas.gov", "a743-wj72", {"$where": "invoice_date >= '%s' and vendor_name in (%s)" % (WINDOW, ",".join(q(n) for n in names[i:i + 20]))})
        for r in rows:
            o.stats["source_rows_seen"] += 1
            v = can.get(norm(r.get("vendor_name")))
            if not v:
                continue
            o.stats["canada_rows"] += 1
            r["record_date"] = iso(r.get("invoice_date"))
            r.update({"archive_vendor_address": v.get("vendor_address", ""), "archive_vendor_city": v.get("vendor_city", ""),
                      "archive_vendor_state": v.get("vendor_state", ""), "archive_vendor_zip": v.get("vendor_zip", ""),
                      "archive_dataset": "https://data.texas.gov/resource/w64c-ndf7.json?vendor_name=" + urllib.parse.quote(v["vendor_name"])})
            url = "https://data.texas.gov/resource/a743-wj72.json?" + urllib.parse.urlencode({"vendor_name": r["vendor_name"], "customer_name": r.get("customer_name", "")})
            o.add(rec("us_tx_dir_sales", "Texas DIR cooperative contract sales VSR (data.texas.gov a743-wj72) + vendor address from archive w64c-ndf7", url,
                      r.get("customer_name", ""), r["vendor_name"], "vendor_state / vendor_zip (data.texas.gov w64c-ndf7, same vendor)",
                      ", ".join(x for x in [v.get("vendor_address", ""), v.get("vendor_city", ""), v.get("vendor_state", ""), v.get("vendor_zip", "")] if x),
                      r, website=sites.get(tx_norm(r.get("customer_name", "")), "")))
    return "Texas"


SRC = {"tx1295": src_tx1295, "walni2": src_walni2, "ndcheck": src_ndcheck, "wyopen": src_wyopen, "sdcheck": src_sdcheck,
       "mdpay": src_mdpay, "txdir": src_txdir}


def main():
    a = argparse.ArgumentParser()
    a.add_argument("--source", default="all", choices=["all"] + list(SRC))
    a.add_argument("--refresh", action="store_true", help="download the bulk files again")
    a.add_argument("--no-wikidata", action="store_true")
    args = a.parse_args()
    keys = list(SRC) if args.source == "all" else [args.source]
    done, blocked = [], []
    for k in keys:
        o = Out(k)
        try:
            state = SRC[k](o, args.refresh)
        except Blocked as e:
            print("BLOCKED", k, e, flush=True)
            blocked.append(k)
            continue
        sites = {}
        if not args.no_wikidata:
            need = {r["publisher"]: state for r in o.pairs.values() if not r.get("website")}
            try:
                sites = wikidata_sites(need, os.path.join(SOURCES, "wikidata_sites.json"))
            except Blocked as e:
                print("wikidata blocked:", e, flush=True)
        done += list(o.write(sites))
    buyers = {buyer_key(r["publisher"]) for r in done}
    recent = {buyer_key(r["publisher"]) for r in done if r["row"]["record_date"] >= RECENT}
    site = {buyer_key(r["publisher"]) for r in done if r.get("website")}
    print("us_public_dated: %d, %d, %d, %d; blocked: %s" % (len(done), len(buyers), len(recent), len(site), ", ".join(blocked) or "none"), flush=True)


if __name__ == "__main__":
    main()
