#!/usr/bin/env python3
"""Buyers of service providers located in Canada, from four SEC / PCAOB structured filings. No AI.

One tool, four sources (--source pcaob|advd|formd|ncen|all). Each source is a bulk file published by a US regulator in
which a filer names a paid service provider together with that provider's own location field. A provider whose
location field says Canada (or a Canadian province) is a Canada-located vendor proven by the source itself; the filer
(or the firm behind it) is its buyer. Rows dated on or after 2023-11-02 are kept (the lead scanner labels 12-36 month
old rows separately); one output line per (buyer, vendor) pair, the most recent record kept.

pcaob  PCAOB Form AP, https://pcaobus.org/assets/PCAOBFiles/FirmFilings.zip (daily, FirmFilings.csv).
       Buyer = `Issuer Name` / `Issuer CIK`. Vendor = `Firm Name` when `Firm Issuing Country` == Canada (canada_value
       = `Firm Issuing City`, `Firm Issuing State`, `Firm Issuing Country`), role issuing_office; also other firms
       taking part in the audit (`Audit Not Divided Percent Information`, JSON, `Country` == Canada), role
       other_participating_firm. Date = `Audit Report Date`. Divided-responsibility firms (they audit an investee, not
       the issuer) are skipped. Evidence: the issuer's 10-K / 20-F / 40-F on EDGAR (auditor's report city).
advd   SEC Form ADV Part 1 Schedule D 7.B.(1), registered (IA_*) and exempt reporting (ERA_*) advisers,
       https://reports.adviserinfo.sec.gov/reports/foia/reports_metadata.json -> advFilingData monthly zips.
       Provider tables 7B1A23 auditor, 7B1A24 prime broker, 7B1A25 custodian, 7B1A26 administrator, 7B1A28 marketer,
       each with `City`, `State`, `Country`; kept when `Country` == Canada and `Related Person` is not Y (auditor: and
       `Independent` is not N). Joined on (FilingID, ReferenceID) to 7B1 (`Fund Name`, buyer_unit) and on FilingID to
       IA_ADV_Base_A / ERA_ADV_Base (`1A` legal name, `1E1` CRD, `1F1-*` address, `DateSubmitted` = date). Buyer = the
       adviser (it runs the fund and pays its providers); website = Schedule D 1.I (first non-social URL).
       Evidence: https://reports.adviserinfo.sec.gov/reports/ADV/<CRD>/PDF/<CRD>.pdf (section 7.B.(1)).
formd  SEC Form D data sets, https://www.sec.gov/data-research/sec-markets-data/form-d-data-sets (quarterly zips).
       RECIPIENTS (sales-compensation recipients: placement agents, finders) with `STATEORCOUNTRY` in A0-A9, B0
       (Canadian provinces / territory codes) or Z4 (Canada); canada_value = STREET1, STREET2, CITY,
       STATEORCOUNTRYDESCRIPTION, ZIPCODE. Joined on ACCESSIONNUMBER to ISSUERS (`IS_PRIMARYISSUER_FLAG` = YES:
       `ENTITYNAME`, `CIK` = buyer) and FORMDSUBMISSION (`FILING_DATE` = date). Dropped: recipient None / N/A,
       self-issued SPV series (Hiive / HII Atoms, and any issuer whose name carries the recipient's own name).
       Evidence: https://www.sec.gov/Archives/edgar/data/<CIK>/<accession>/ (primary_doc.xml, item 12).
ncen   SEC Form N-CEN data sets, https://www.sec.gov/data-research/sec-markets-data/form-n-cen-data-sets.
       Provider tables with `COUNTRY` = CA (or CA-xx): ADVISER (sub-advisers), BROKER (commissions paid), PRICING_SERVICE,
       CUSTODIAN, ADMIN, TRANSFER_AGENT, SHAREHOLDER_SERVICING_AGENT (fund level, FUND_ID) and PUBLIC_ACCOUNTANT
       (registrant level); dropped when IS_AFFILIATED = Y or the provider is a sub-custodian / sub-admin / sub-agent.
       BROKER_DEALER (affiliated broker-dealers by definition) and PRINCIPAL_TRANSACTION (trades) are not used.
       Buyer = REGISTRANT (`REGISTRANT_NAME`, `CIK`, family `FAMILY_INVESTMENT_COMPANY_NAME`), buyer_unit = the
       series (`FUND_NAME`); website = REGISTRANT_WEBSITE. Date = SUBMISSION `REPORT_ENDING_PERIOD` (the provider
       served the fund during that year). Evidence: the EDGAR filing index of the accession.

Buyers that are the same firm as the provider (same leading distinctive name token) are dropped everywhere.
Website when the source gives none: EDGAR submissions JSON field `website` (data.sec.gov, CIK), else Wikidata P856 of
the item whose P5531 (SEC CIK) equals the CIK (one SPARQL request, cached). Never guessed.

Counts, first full run 2026-11-02 (each run also writes ~/cch-leads/socrata_<source>.jsonl.stats.json):
  pcaob 157,057 Form AP rows, 4,518 with a Canadian office, 1,137 dated >= 2023-11-02 -> 490 pairs, 444 issuers.
  advd  21 monthly zips (2025-01..2026-09; nothing older is published), 31,014 Canadian provider rows -> 1,054 pairs,
        576 advisers (3,817 funds).
  formd 12 quarters, 79,970 recipient rows, 900 Canadian, 210 self-issued dropped -> 442 pairs, 368 issuers.
  ncen  12 quarters, 26,916 Canadian provider rows, 5,036 unaffiliated -> 626 pairs, 388 registrants.
  EDGAR submissions `website` was empty for all ~800 CIKs looked up; websites come from ADV 1.I, N-CEN and Wikidata.

Output: ~/cch-leads/socrata_pcaob.jsonl, socrata_advd.jsonl, socrata_formd.jsonl, socrata_ncen.jsonl (overwritten).
Cache: ~/cch-sources/<source>/ (bulk files, downloaded once), ~/cch-sources/edgar_submissions/, ~/cch-sources/wikidata/.
Politeness: at most 2 requests/second per host; SEC hosts get a User-Agent with a contact e-mail (SEC fair-access
policy), others the crawler User-Agent. HTTP 401/403/429 = blocked: the source is skipped and reported, never bypassed.
  python3 tools/sec_canada_providers.py --source all [--offline] [--no-lookup]
"""
import argparse, csv, datetime, gzip, io, json, os, re, sys, time, urllib.error, urllib.parse, urllib.request, zipfile

UA = "canada-contracts-hub-crawler/1.0 (+https://github.com/mohamedbiranesy-gif/canada-contracts-hub)"
UA_SEC = os.environ.get("CCH_SEC_UA", "canada-contracts-hub research m.biranesy@gmail.com")
START = "2023-11-02"
RECENT = "2025-11-02"
HOME = os.path.expanduser("~")
CACHE = os.path.join(HOME, "cch-sources")
LEADS = os.path.join(HOME, "cch-leads")
RATE = 2.0  # requests per second per host

PCAOB_URL = "https://assets.pcaobus.org/firm-filings/FirmFilings.zip"  # target of pcaobus.org/assets/PCAOBFiles/FirmFilings.zip
ADV_META = "https://reports.adviserinfo.sec.gov/reports/foia/reports_metadata.json"
ADV_BASE = "https://reports.adviserinfo.sec.gov/reports/foia/advFilingData/%s/%s"
FORMD_INDEX = "https://www.sec.gov/data-research/sec-markets-data/form-d-data-sets"
NCEN_INDEX = "https://www.sec.gov/data-research/sec-markets-data/form-n-cen-data-sets"
SUBMISSIONS = "https://data.sec.gov/submissions/CIK%010d.json"
SPARQL = "https://query.wikidata.org/sparql"

FORMD_CA = {"A0": "AB", "A1": "BC", "A2": "MB", "A3": "NB", "A4": "NL", "A5": "NS", "A6": "ON", "A7": "PE",
            "A8": "QC", "A9": "SK", "B0": "YT", "Z4": "CANADA"}
SOCIAL = ("linkedin.", "twitter.", "x.com", "facebook.", "instagram.", "youtube.", "youtu.be", "vimeo.", "medium.com",
          "crunchbase.", "bloomberg.", "tiktok.", "threads.net", "github.com", "wikipedia.", "google.", "sec.gov",
          "adviserinfo", "finra.org", "pitchbook.", "glassdoor.", "substack.com", "wordpress.com", "blogspot.")
STOP = set("""inc incorporated llc llp lp lllp ltd limited corp corporation co company the of and plc sa ag nv bv
gmbh sarl pllc pc trust fund funds group holdings holding canada canadian usa us america americas north
international global capital management asset assets investment investments investors advisors advisers advisory
partners securities financial services bank markets series chartered accountants professional cpa cpas
cie ltee ltée inc. llc. de du des la le et""".split())

BLOCKED = []
_last = {}


def log(*a):
    print(time.strftime("%H:%M:%S"), *a, flush=True)


class Blocked(Exception):
    pass


def http(url, ua, timeout=180):
    host = urllib.parse.urlsplit(url).hostname
    wait = 1.0 / RATE - (time.time() - _last.get(host, 0))
    if wait > 0:
        time.sleep(wait)
    _last[host] = time.time()
    req = urllib.request.Request(url, headers={"User-Agent": ua, "Accept-Encoding": "gzip"})
    try:
        resp = urllib.request.urlopen(req, timeout=timeout)
    except urllib.error.HTTPError as e:
        if e.code in (401, 403, 429):
            raise Blocked("%s -> HTTP %s" % (url, e.code))
        raise
    return resp


def read_body(resp):
    data = resp.read()
    if resp.headers.get("Content-Encoding", "") == "gzip":
        data = gzip.decompress(data)
    return data


def ua_for(url):
    return UA_SEC if "sec.gov" in urllib.parse.urlsplit(url).hostname else UA


def fetch_text(url, path, max_age_h=20, offline=False):
    """Small page / JSON, cached; refreshed when older than max_age_h."""
    if os.path.exists(path) and (offline or time.time() - os.path.getmtime(path) < max_age_h * 3600):
        return open(path, encoding="utf-8", errors="replace").read()
    if offline:
        raise FileNotFoundError(path)
    data = read_body(http(url, ua_for(url)))
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path + ".part", "wb") as f:
        f.write(data)
    os.replace(path + ".part", path)
    return data.decode("utf-8", "replace")


def download(url, path, offline=False, max_age_h=None):
    """Bulk file, downloaded once (or refreshed after max_age_h), streamed to disk."""
    if os.path.exists(path) and os.path.getsize(path) > 0:
        if offline or max_age_h is None or time.time() - os.path.getmtime(path) < max_age_h * 3600:
            return path
    if offline:
        return None
    os.makedirs(os.path.dirname(path), exist_ok=True)
    log("download", url)
    resp = http(url, ua_for(url), timeout=600)
    gz = resp.headers.get("Content-Encoding", "") == "gzip"
    with open(path + ".part", "wb") as f:
        src = gzip.GzipFile(fileobj=resp) if gz else resp
        while True:
            b = src.read(1 << 20)
            if not b:
                break
            f.write(b)
    os.replace(path + ".part", path)
    return path


def pdate(s):
    s = (s or "").strip()
    if not s:
        return ""
    for fmt in ("%m/%d/%Y %I:%M:%S %p", "%m/%d/%Y %H:%M:%S", "%m/%d/%Y", "%d-%b-%Y", "%Y-%m-%d"):
        try:
            return datetime.datetime.strptime(s, fmt).strftime("%Y-%m-%d")
        except ValueError:
            pass
    m = re.match(r"(\d{1,2})/(\d{1,2})/(\d{4})", s)
    if m:
        return "%s-%02d-%02d" % (m.group(3), int(m.group(1)), int(m.group(2)))
    return ""


def clean(s):
    return re.sub(r"\s+", " ", (s or "")).strip()


def host_of(raw):
    w = (raw or "").strip().lower()
    w = re.sub(r"^[a-z]+://", "", w)
    w = re.sub(r"^www\d?\.", "", w).split("/")[0].split("?")[0].split("#")[0].split(":")[0].strip(" .")
    if not re.fullmatch(r"[a-z0-9]([a-z0-9-]*[a-z0-9])?(\.[a-z0-9]([a-z0-9-]*[a-z0-9])?)*\.[a-z]{2,}", w):
        return ""
    if any(s in w for s in SOCIAL) or w in ("n.a", "none.com", "na.com", "none.none"):
        return ""
    return w


def tokens(name):
    return [t for t in re.findall(r"[a-z0-9]+", (name or "").lower()) if t not in STOP and len(t) > 1]


def same_firm(a, b):
    ta, tb = tokens(a), tokens(b)
    if not ta or not tb:
        return False
    if ta[0] == tb[0] and len(ta[0]) >= 3:
        return True
    return len(ta) >= 2 and " ".join(ta[:2]) in " ".join(tb)


def nkey(name):
    return " ".join(re.findall(r"[a-z0-9]+", (name or "").lower()))


def bad_name(n):
    return nkey(n) in ("", "none", "n a", "na", "not applicable", "null", "unknown", "tbd", "various")


def csv_rows(z, prefix, delim=","):
    names = [m for m in z.namelist() if os.path.basename(m).upper().startswith(prefix.upper())
             and "WEBSITES" not in os.path.basename(m).upper()]
    for m in names:
        with z.open(m) as fh:
            t = io.TextIOWrapper(fh, encoding="utf-8", errors="replace", newline="")
            for row in csv.DictReader(t, delimiter=delim):
                yield {(k or "").strip(): (v if v is not None else "") for k, v in row.items()}


# ---------------------------------------------------------------- websites
class Sites:
    def __init__(self, offline=False, lookup=True):
        self.offline, self.lookup = offline, lookup
        self.dir = os.path.join(CACHE, "edgar_submissions")
        os.makedirs(self.dir, exist_ok=True)
        self.wd = None
        self.edgar_blocked = False
        self.fetched = 0

    def wikidata(self):
        if self.wd is None:
            self.wd = {}
            path = os.path.join(CACHE, "wikidata", "p5531_p856.csv")
            q = "SELECT ?cik ?site WHERE { ?item wdt:P5531 ?cik . ?item wdt:P856 ?site . }"
            url = SPARQL + "?" + urllib.parse.urlencode({"query": q, "format": "json"})
            try:
                if not os.path.exists(path) or time.time() - os.path.getmtime(path) > 7 * 86400:
                    if self.offline or not self.lookup:
                        raise FileNotFoundError(path)
                    data = json.loads(read_body(http(url, UA, timeout=120)))
                    os.makedirs(os.path.dirname(path), exist_ok=True)
                    with open(path, "w", newline="") as f:
                        w = csv.writer(f)
                        w.writerow(["cik", "site"])
                        for b in data["results"]["bindings"]:
                            w.writerow([b["cik"]["value"], b["site"]["value"]])
                for r in csv.DictReader(open(path, encoding="utf-8")):
                    try:
                        c = int(re.sub(r"\D", "", r["cik"]) or "x")
                    except ValueError:
                        continue
                    if host_of(r["site"]) and c not in self.wd:
                        self.wd[c] = r["site"]
            except (Blocked, FileNotFoundError, urllib.error.URLError, ValueError, KeyError) as e:
                log("wikidata unavailable:", e)
        return self.wd

    def edgar(self, cik):
        path = os.path.join(self.dir, "CIK%010d.json" % cik)
        if os.path.exists(path):
            try:
                return json.load(open(path, encoding="utf-8"))
            except ValueError:
                pass
        if self.offline or not self.lookup or self.edgar_blocked:
            return None
        try:
            d = json.loads(read_body(http(SUBMISSIONS % cik, UA_SEC, timeout=60)))
            d.pop("filings", None)
        except Blocked as e:
            self.edgar_blocked = True
            BLOCKED.append("data.sec.gov submissions (%s)" % e)
            return None
        except urllib.error.HTTPError as e:
            d = {"_http": e.code}
        except (urllib.error.URLError, ValueError, OSError) as e:
            log("edgar error", cik, e)
            return None
        with open(path, "w", encoding="utf-8") as f:
            json.dump(d, f)
        self.fetched += 1
        if self.fetched % 100 == 0:
            log("edgar submissions fetched:", self.fetched)
        return d

    def for_cik(self, cik):
        try:
            c = int(re.sub(r"\D", "", str(cik)) or "x")
        except ValueError:
            return "", ""
        d = self.edgar(c) or {}
        for k in ("website", "investorWebsite"):
            h = host_of(d.get(k) or "")
            if h:
                return h, "EDGAR submissions %s (CIK %d)" % (k, c)
        site = self.wikidata().get(c)
        if site and host_of(site):
            return host_of(site), "Wikidata P856 via P5531=%010d" % c
        return "", ""


# ---------------------------------------------------------------- output
def emit(source, recs, sites, desc):
    """recs: dict (buyer_key, vendor_key) -> record; resolves websites, writes the jsonl and stats."""
    os.makedirs(LEADS, exist_ok=True)
    out = os.path.join(LEADS, "socrata_%s.jsonl" % source)
    rows = sorted(recs.values(), key=lambda r: (r["publisher"].lower(), r["vendor"].lower()))
    cache = {}
    for r in rows:
        if not r["domain"] and r.get("_cik"):
            if r["_cik"] not in cache:
                cache[r["_cik"]] = sites.for_cik(r["_cik"])
            h, how = cache[r["_cik"]]
            if h:
                r["domain"], r["row"]["website_source"] = h, how
        r["website"] = "https://%s/" % r["domain"] if r["domain"] else ""
    with open(out + ".part", "w", encoding="utf-8") as f:
        for r in rows:
            o = {k: r[k] for k in ("platform", "domain", "dataset_id", "dataset", "dataset_url", "publisher",
                                   "buyer_unit", "website", "vendor", "canada_field", "canada_value", "row")}
            f.write(json.dumps(o, ensure_ascii=False) + "\n")
    os.replace(out + ".part", out)
    buyers = {}
    for r in rows:
        b = r["_bkey"]
        cur = buyers.setdefault(b, {"date": "", "site": ""})
        cur["date"] = max(cur["date"], r["row"]["record_date"])
        cur["site"] = cur["site"] or r["domain"]
    st = {"source": source, "dataset": desc, "rows": len(rows), "buyers": len(buyers),
          "buyers_last_12m": sum(1 for v in buyers.values() if v["date"] >= RECENT),
          "buyers_with_website": sum(1 for v in buyers.values() if v["site"]),
          "run": time.strftime("%Y-%m-%d %H:%M"), "blocked": BLOCKED[:]}
    st.update(desc_counts.get(source, {}))
    with open(out + ".stats.json", "w") as f:
        json.dump(st, f, indent=1)
    log(source, json.dumps(st))
    return st, buyers


desc_counts = {}


def keep(recs, key, rec):
    cur = recs.get(key)
    if cur is None or rec["row"]["record_date"] > cur["row"]["record_date"]:
        recs[key] = rec


# ---------------------------------------------------------------- pcaob
def run_pcaob(a, sites):
    path = download(PCAOB_URL, os.path.join(CACHE, "pcaob", "FirmFilings.zip"), a.offline, max_age_h=20)
    if not path:
        return None
    desc = "PCAOB Form AP (audit firm office that signed the issuer's audit report)"
    recs, seen = {}, {"source_rows": 0, "canada_rows": 0, "in_window": 0}
    with zipfile.ZipFile(path) as z:
        for row in csv_rows(z, "FirmFilings"):
            seen["source_rows"] += 1
            date = pdate(row.get("Audit Report Date"))
            issuer, cik = clean(row.get("Issuer Name")), re.sub(r"\D", "", row.get("Issuer CIK") or "")
            cands = []
            if clean(row.get("Firm Issuing Country")).lower() == "canada":
                val = ", ".join(x for x in (clean(row.get("Firm Issuing City")), clean(row.get("Firm Issuing State")),
                                            clean(row.get("Firm Issuing Country"))) if x)
                cands.append((clean(row.get("Firm Name")), row.get("Firm ID", ""), val,
                              "Firm Issuing City / Firm Issuing State / Firm Issuing Country (PCAOB Form AP)",
                              "issuing_office"))
            nd = row.get("Audit Not Divided Percent Information") or ""
            if "Canada" in nd:
                try:
                    for p in json.loads(nd):
                        if clean(p.get("Country")).lower() == "canada":
                            val = ", ".join(x for x in (clean(p.get("City")), clean(p.get("State")), "Canada") if x)
                            cands.append((clean(p.get("FirmName")), p.get("FirmID", ""), val,
                                          "Audit Not Divided Percent Information[].City/Country (PCAOB Form AP)",
                                          "other_participating_firm"))
                except ValueError:
                    pass
            if not cands:
                continue
            seen["canada_rows"] += 1
            if not date or date < START or bad_name(issuer):
                continue
            seen["in_window"] += 1
            for vendor, fid, val, field, role in cands:
                if bad_name(vendor) or same_firm(vendor, issuer):
                    continue
                bkey = "cik:%d" % int(cik) if cik else "n:" + nkey(issuer)
                rec = {"platform": "pcaob_form_ap", "domain": "", "dataset_id": "form_ap_%s" % row.get("Form Filing ID"),
                       "dataset": desc, "dataset_url": PCAOB_URL, "publisher": issuer, "buyer_unit": "",
                       "vendor": vendor, "canada_field": field, "canada_value": val, "_cik": cik, "_bkey": bkey,
                       "row": {"Form Filing ID": row.get("Form Filing ID", ""), "Latest Form AP Filing": row.get("Latest Form AP Filing", ""),
                               "Firm ID": fid, "Firm Name": vendor, "Firm Issuing City": row.get("Firm Issuing City", ""),
                               "Firm Issuing State": row.get("Firm Issuing State", ""),
                               "Firm Issuing Country": row.get("Firm Issuing Country", ""),
                               "Issuer Name": issuer, "Issuer CIK": row.get("Issuer CIK", ""),
                               "Issuer ID": row.get("Issuer ID", ""), "Audit Report Type": row.get("Audit Report Type", ""),
                               "Audit Fund Series": row.get("Audit Fund Series", ""),
                               "Audit Report Date": row.get("Audit Report Date", ""),
                               "Fiscal Period End Date": row.get("Fiscal Period End Date", ""),
                               "Filing Date": row.get("Filing Date", ""), "role": role, "vendor_location": val,
                               "evidence_url": ("https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=%s&type=10-K"
                                                % cik) if cik else "",
                               "record_date": date}}
                keep(recs, (bkey, nkey(vendor)), rec)
    desc_counts["pcaob"] = seen
    return emit("pcaob", recs, sites, desc)


# ---------------------------------------------------------------- adv
def adv_files(a):
    meta = json.loads(fetch_text(ADV_META, os.path.join(CACHE, "advd", "reports_metadata.json"), offline=a.offline))
    out = []
    for y, v in meta.get("advFilingData", {}).items():
        if not str(y).isdigit():
            continue
        for f in v.get("files", []):
            m = re.search(r"_(\d{8})_(\d{8})\.zip$", f.get("fileName", ""))
            if m and m.group(2) >= START.replace("-", ""):
                out.append((m.group(1), y, f["fileName"]))
    return sorted(out)


PROVIDERS = (("7B1A23", "auditor", "Name of Auditing Firm"), ("7B1A24", "prime_broker", "Name of Prime Broker"),
             ("7B1A25", "custodian", "Legal Name of Custodian"), ("7B1A26", "administrator", "Name of Administrator"),
             ("7B1A28", "marketer", "Name of Marketer"))


def run_advd(a, sites):
    desc = "SEC Form ADV Schedule D 7.B.(1) private-fund service providers (auditor, prime broker, custodian, administrator, marketer)"
    recs, seen = {}, {"zips": 0, "provider_rows": 0, "canada_rows": 0, "kept_rows": 0, "funds": 0}
    funds_by_pair = {}
    for start, y, fname in adv_files(a):
        path = download(ADV_BASE % (y, fname), os.path.join(CACHE, "advd", fname), a.offline)
        if not path:
            continue
        seen["zips"] += 1
        with zipfile.ZipFile(path) as z:
            for kind in ("IA", "ERA"):
                prov = []
                for tab, role, namecol in PROVIDERS:
                    for r in csv_rows(z, "%s_Schedule_D_%s_" % (kind, tab)):
                        seen["provider_rows"] += 1
                        if clean(r.get("Country")).lower() != "canada":
                            continue
                        seen["canada_rows"] += 1
                        if clean(r.get("Related Person")).upper() in ("Y", "YES"):
                            continue
                        if role == "auditor" and clean(r.get("Independent")).upper() in ("N", "NO"):
                            continue
                        name = clean(r.get(namecol)) or clean(r.get("Primary Business Name"))
                        if bad_name(name):
                            continue
                        prov.append((r["FilingID"], r["ReferenceID"], role, name, r))
                if not prov:
                    continue
                need_f = {(p[0], p[1]) for p in prov}
                fids = {p[0] for p in prov}
                funds, base, webs = {}, {}, {}
                for r in csv_rows(z, "%s_Schedule_D_7B1_" % kind):
                    k = (r["FilingID"], r["ReferenceID"])
                    if k in need_f:
                        funds[k] = r
                for r in csv_rows(z, "IA_ADV_Base_A_" if kind == "IA" else "ERA_ADV_Base_"):
                    if r["FilingID"] in fids:
                        base[r["FilingID"]] = r
                allw = {}
                for r in csv_rows(z, "%s_Schedule_D_1I_" % kind):
                    if r["FilingID"] in fids and host_of(r.get("Website")):
                        allw.setdefault(r["FilingID"], []).append((host_of(r.get("Website")), clean(r.get("Website"))))
                for fid, lst in allw.items():
                    # prefer the site whose host carries a distinctive word of the adviser's name, else the first listed
                    b = base.get(fid, {})
                    toks = [t for t in tokens(clean(b.get("1A")) + " " + clean(b.get("1B1"))) if len(t) >= 4]
                    best = sorted((w for w in lst if any(t in w[0].replace("-", "") for t in toks)), key=lambda w: len(w[0]))
                    webs[fid] = (best or lst)[0]
                for fid, ref, role, name, r in prov:
                    b = base.get(fid)
                    if not b:
                        continue
                    adviser = clean(b.get("1A")) or clean(b.get("1B1"))
                    date = pdate(b.get("DateSubmitted"))
                    if bad_name(adviser) or not date or date < START or same_firm(name, adviser):
                        continue
                    fund = funds.get((fid, ref), {})
                    fname_ = clean(fund.get("Fund Name"))
                    if same_firm(name, fname_):
                        continue
                    seen["kept_rows"] += 1
                    crd = clean(b.get("1E1"))
                    bkey = "crd:%s" % crd if crd else "n:" + nkey(adviser)
                    vkey = nkey(name)
                    funds_by_pair.setdefault((bkey, vkey), set()).add(fname_)
                    val = ", ".join(x for x in (clean(r.get("City")), clean(r.get("State")), clean(r.get("Country"))) if x)
                    h, wraw = webs.get(fid, ("", ""))
                    rowd = {"FilingID": fid, "ReferenceID": ref, "form": "%s ADV" % kind, "DateSubmitted": b.get("DateSubmitted", ""),
                            "adviser_legal_name": clean(b.get("1A")), "adviser_business_name": clean(b.get("1B1")),
                            "adviser_crd": crd, "adviser_sec_file": clean(b.get("1D")),
                            "adviser_address": ", ".join(x for x in (clean(b.get("1F1-Street 1")), clean(b.get("1F1-Street 2")),
                                                                     clean(b.get("1F1-City")), clean(b.get("1F1-State")),
                                                                     clean(b.get("1F1-Postal")), clean(b.get("1F1-Country"))) if x),
                            "adviser_website_raw": wraw, "Fund Name": fname_, "Fund ID": clean(fund.get("Fund ID")),
                            "Fund Type": clean(fund.get("Fund Type")), "Gross Asset Value": clean(fund.get("Gross Asset Value")),
                            "provider_table": "%s_Schedule_D_%s" % (kind, [t for t, ro, _ in PROVIDERS if ro == role][0]),
                            "role": role}
                    for k2, v2 in r.items():
                        if k2 not in ("FilingID", "ReferenceID"):
                            rowd["provider_" + k2] = clean(v2)
                    rowd["record_date"] = date
                    if h:
                        rowd["website_source"] = "Form ADV Schedule D 1.I"
                    rec = {"platform": "sec_form_adv_7b1", "domain": h, "dataset_id": "adv_%s_%s_%s" % (fid, ref, role),
                           "dataset": desc,
                           "dataset_url": ("https://reports.adviserinfo.sec.gov/reports/ADV/%s/PDF/%s.pdf" % (crd, crd)) if crd else "https://adviserinfo.sec.gov/",
                           "publisher": adviser, "buyer_unit": fname_, "vendor": name,
                           "canada_field": "City / State / Country (%s_Schedule_D_%s, SEC Form ADV)" % (kind, rowd["provider_table"].split("_")[-1]),
                           "canada_value": val, "_cik": "", "_bkey": bkey, "row": rowd}
                    keep(recs, (bkey, vkey), rec)
        log("adv", fname, "pairs so far", len(recs))
    for k, r in recs.items():
        fl = sorted(x for x in funds_by_pair.get(k, ()) if x)
        r["row"]["funds_count"] = len(fl)
        r["row"]["funds_sample"] = fl[:15]
    seen["funds"] = len({f for s in funds_by_pair.values() for f in s})
    desc_counts["advd"] = seen
    return emit("advd", recs, sites, desc)


# ---------------------------------------------------------------- form d / n-cen indexes
def quarter_zips(index_url, path, pattern, offline):
    page = fetch_text(index_url, path, offline=offline)
    out = {}
    for href, y, q in re.findall(pattern, page):
        end = "%s-%s" % (y, {"1": "03-31", "2": "06-30", "3": "09-30", "4": "12-31"}[q])
        if end >= START:
            out.setdefault("%sq%s" % (y, q), urllib.parse.urljoin(index_url, href))
    return sorted(out.items())


def run_formd(a, sites):
    desc = "SEC Form D sales-compensation recipients (placement agents / finders) with a Canadian address"
    recs, seen = {}, {"zips": 0, "recipient_rows": 0, "canada_rows": 0, "kept_rows": 0, "dropped_self_issued": 0}
    zips = quarter_zips(FORMD_INDEX, os.path.join(CACHE, "formd", "index.html"),
                        r'href="([^"]*/(\d{4})q([1-4])_d(?:_\d+)?\.zip)"', a.offline)
    for q, url in zips:
        path = download(url, os.path.join(CACHE, "formd", os.path.basename(url)), a.offline)
        if not path:
            continue
        seen["zips"] += 1
        with zipfile.ZipFile(path) as z:
            recips = []
            for r in csv_rows(z, "RECIPIENTS", "\t"):
                seen["recipient_rows"] += 1
                code = clean(r.get("STATEORCOUNTRY")).upper()
                if code not in FORMD_CA:
                    continue
                seen["canada_rows"] += 1
                recips.append(r)
            accs = {r["ACCESSIONNUMBER"] for r in recips}
            iss, sub = {}, {}
            for r in csv_rows(z, "ISSUERS", "\t"):
                if r["ACCESSIONNUMBER"] in accs and clean(r.get("IS_PRIMARYISSUER_FLAG")).upper() == "YES":
                    iss[r["ACCESSIONNUMBER"]] = r
            for r in csv_rows(z, "FORMDSUBMISSION", "\t"):
                if r["ACCESSIONNUMBER"] in accs:
                    sub[r["ACCESSIONNUMBER"]] = r
            for r in recips:
                acc = r["ACCESSIONNUMBER"]
                i, s = iss.get(acc), sub.get(acc, {})
                if not i:
                    continue
                issuer, cik = clean(i.get("ENTITYNAME")), re.sub(r"\D", "", i.get("CIK") or "")
                vendor = clean(r.get("RECIPIENTNAME"))
                bd = clean(r.get("ASSOCIATEDBDNAME"))
                if bad_name(vendor):
                    vendor = bd
                date = pdate(s.get("FILING_DATE"))
                if bad_name(vendor) or bad_name(issuer) or not date or date < START:
                    continue
                if (re.search(r"\bhiive\b|\bhii\b", issuer, re.I) or same_firm(vendor, issuer)
                        or (not bad_name(bd) and same_firm(bd, issuer))):
                    seen["dropped_self_issued"] += 1
                    continue
                seen["kept_rows"] += 1
                val = ", ".join(x for x in (clean(r.get("STREET1")), clean(r.get("STREET2")), clean(r.get("CITY")),
                                            clean(r.get("STATEORCOUNTRYDESCRIPTION")), clean(r.get("ZIPCODE"))) if x)
                bkey = "cik:%d" % int(cik) if cik else "n:" + nkey(issuer)
                rowd = {k: clean(v) for k, v in r.items()}
                rowd.update({"ISSUER_CIK": cik, "ISSUER_ENTITYNAME": issuer, "ISSUER_ENTITYTYPE": clean(i.get("ENTITYTYPE")),
                             "ISSUER_ADDRESS": ", ".join(x for x in (clean(i.get("STREET1")), clean(i.get("STREET2")), clean(i.get("CITY")),
                                                                     clean(i.get("STATEORCOUNTRYDESCRIPTION")), clean(i.get("ZIPCODE"))) if x),
                             "ISSUER_PHONE": clean(i.get("ISSUERPHONENUMBER")), "JURISDICTIONOFINC": clean(i.get("JURISDICTIONOFINC")),
                             "FILING_DATE": clean(s.get("FILING_DATE")), "SUBMISSIONTYPE": clean(s.get("SUBMISSIONTYPE")),
                             "FILE_NUM": clean(s.get("FILE_NUM")), "SIC_CODE": clean(s.get("SIC_CODE")), "quarter_file": q,
                             "record_date": date})
                rec = {"platform": "sec_form_d", "domain": "", "dataset_id": "formd_%s_%s" % (acc, r.get("RECIPIENT_SEQ_KEY", "")),
                       "dataset": desc,
                       "dataset_url": ("https://www.sec.gov/Archives/edgar/data/%d/%s/" % (int(cik), acc.replace("-", ""))) if cik else url,
                       "publisher": issuer, "buyer_unit": "", "vendor": vendor,
                       "canada_field": "RECIPIENTS.STREET1/CITY/STATEORCOUNTRY=%s (SEC Form D)" % clean(r.get("STATEORCOUNTRY")).upper(),
                       "canada_value": val, "_cik": cik, "_bkey": bkey, "row": rowd}
                keep(recs, (bkey, nkey(vendor)), rec)
        log("formd", q, "pairs so far", len(recs))
    desc_counts["formd"] = seen
    return emit("formd", recs, sites, desc)


NCEN_TABLES = (("ADVISER", "ADVISER_NAME", "sub_adviser"), ("BROKER", "BROKER_NAME", "broker"),
               ("PRICING_SERVICE", "PRICING_SERVICE_NAME", "pricing_service"), ("CUSTODIAN", "CUSTODIAN_NAME", "custodian"),
               ("ADMIN", "ADMIN_NAME", "administrator"), ("TRANSFER_AGENT", "TRANSFERAGENT_NAME", "transfer_agent"),
               ("SHAREHOLDER_SERVICING_AGENT", "AGENT_NAME", "shareholder_servicing_agent"),
               ("PUBLIC_ACCOUNTANT", "PUB_ACCOUNTANT_NAME", "public_accountant"))


def is_ca(r):
    co, st = clean(r.get("COUNTRY")).upper(), clean(r.get("STATE")).upper()
    return co == "CA" or co.startswith("CA-") or st.startswith("CA-")


def run_ncen(a, sites):
    desc = "SEC Form N-CEN registered-fund service providers (sub-advisers, brokers, pricing services, custodians, auditors)"
    recs, seen = {}, {"zips": 0, "canada_rows": 0, "kept_rows": 0}
    zips = quarter_zips(NCEN_INDEX, os.path.join(CACHE, "ncen", "index.html"),
                        r'href="([^"]*/(\d{4})q([1-4])_ncen(?:_\d+)?\.zip)"', a.offline)
    for q, url in zips:
        path = download(url, os.path.join(CACHE, "ncen", os.path.basename(url)), a.offline)
        if not path:
            continue
        seen["zips"] += 1
        with zipfile.ZipFile(path) as z:
            prov = []
            for tab, namecol, role in NCEN_TABLES:
                if not any(os.path.basename(m).upper() == tab + ".TSV" for m in z.namelist()):
                    continue
                for r in csv_rows(z, tab + ".TSV", "\t"):
                    if not is_ca(r):
                        continue
                    seen["canada_rows"] += 1
                    if clean(r.get("IS_AFFILIATED")).upper() == "Y":
                        continue
                    if any(clean(r.get(c)).upper() == "Y" for c in ("IS_SUB_CUSTODIAN", "IS_SUB_ADMIN", "IS_SUBTRANSFER_AGENT", "IS_SUBSHARE")):
                        continue
                    name = clean(r.get(namecol))
                    if bad_name(name):
                        continue
                    acc = r.get("ACCESSION_NUMBER") or (r.get("FUND_ID") or "").split("_")[0]
                    prov.append((acc, r.get("FUND_ID", ""), tab, role, name, r))
            if not prov:
                continue
            accs = {p[0] for p in prov}
            fids = {p[1] for p in prov if p[1]}
            reg, sub, web, fund = {}, {}, {}, {}
            for r in csv_rows(z, "REGISTRANT.TSV", "\t"):
                if r["ACCESSION_NUMBER"] in accs:
                    reg[r["ACCESSION_NUMBER"]] = r
            for r in csv_rows(z, "SUBMISSION.TSV", "\t"):
                if r["ACCESSION_NUMBER"] in accs:
                    sub[r["ACCESSION_NUMBER"]] = r
            for r in csv_rows(z, "REGISTRANT_WEBSITE.TSV", "\t"):
                if r["ACCESSION_NUMBER"] in accs and r["ACCESSION_NUMBER"] not in web and host_of(r.get("WEBPAGE")):
                    web[r["ACCESSION_NUMBER"]] = (host_of(r.get("WEBPAGE")), clean(r.get("WEBPAGE")))
            for r in csv_rows(z, "FUND_REPORTED_INFO.TSV", "\t"):
                if r["FUND_ID"] in fids:
                    fund[r["FUND_ID"]] = r
            for acc, fid, tab, role, name, r in prov:
                g, s = reg.get(acc), sub.get(acc, {})
                if not g:
                    continue
                registrant = clean(g.get("REGISTRANT_NAME"))
                family = clean(g.get("FAMILY_INVESTMENT_COMPANY_NAME"))
                date = pdate(s.get("REPORT_ENDING_PERIOD"))
                fname_ = clean(fund.get(fid, {}).get("FUND_NAME"))
                if bad_name(registrant) or not date or date < START:
                    continue
                if same_firm(name, registrant) or (family and same_firm(name, family)) or (fname_ and same_firm(name, fname_)):
                    continue
                seen["kept_rows"] += 1
                cik = re.sub(r"\D", "", g.get("CIK") or "")
                bkey = "cik:%d" % int(cik) if cik else "n:" + nkey(registrant)
                h, wraw = web.get(acc, ("", ""))
                val = ", ".join(x for x in (clean(r.get("STATE")), clean(r.get("COUNTRY"))) if x)
                rowd = {"ACCESSION_NUMBER": acc, "FUND_ID": fid, "FUND_NAME": fname_, "SERIES_ID": clean(fund.get(fid, {}).get("SERIES_ID")),
                        "REGISTRANT_NAME": registrant, "REGISTRANT_CIK": cik, "FAMILY_INVESTMENT_COMPANY_NAME": family,
                        "REGISTRANT_ADDRESS": ", ".join(x for x in (clean(g.get("ADDRESS1")), clean(g.get("ADDRESS2")), clean(g.get("CITY")),
                                                                    clean(g.get("STATE")), clean(g.get("ZIP")), clean(g.get("COUNTRY"))) if x),
                        "INVESTMENT_COMPANY_TYPE": clean(g.get("INVESTMENT_COMPANY_TYPE")),
                        "REGISTRANT_WEBPAGE": wraw, "FILING_DATE": clean(s.get("FILING_DATE")),
                        "REPORT_ENDING_PERIOD": clean(s.get("REPORT_ENDING_PERIOD")), "SUBMISSION_TYPE": clean(s.get("SUBMISSION_TYPE")),
                        "provider_table": tab, "role": role, "quarter_file": q}
                for k2, v2 in r.items():
                    if k2 not in ("FUND_ID", "ACCESSION_NUMBER"):
                        rowd["provider_" + k2] = clean(v2)
                rowd["record_date"] = date
                if h:
                    rowd["website_source"] = "N-CEN REGISTRANT_WEBSITE"
                rec = {"platform": "sec_form_ncen", "domain": h, "dataset_id": "ncen_%s_%s_%s" % (acc, tab, nkey(name).replace(" ", "-")[:40]),
                       "dataset": desc,
                       "dataset_url": ("https://www.sec.gov/Archives/edgar/data/%d/%s/" % (int(cik), acc.replace("-", ""))) if cik else url,
                       "publisher": registrant, "buyer_unit": fname_, "vendor": name,
                       "canada_field": "%s.STATE/COUNTRY (SEC Form N-CEN)" % tab, "canada_value": val,
                       "_cik": cik, "_bkey": bkey, "row": rowd}
                keep(recs, (bkey, nkey(name)), rec)
        log("ncen", q, "pairs so far", len(recs))
    desc_counts["ncen"] = seen
    return emit("ncen", recs, sites, desc)


RUNNERS = {"ncen": run_ncen, "advd": run_advd, "pcaob": run_pcaob, "formd": run_formd}


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--source", default="all", choices=["all"] + list(RUNNERS))
    ap.add_argument("--offline", action="store_true", help="use cached files only")
    ap.add_argument("--no-lookup", action="store_true", help="no EDGAR / Wikidata website lookups")
    a = ap.parse_args()
    csv.field_size_limit(min(sys.maxsize, 2 ** 31 - 1))
    sites = Sites(offline=a.offline, lookup=not a.no_lookup)
    names = list(RUNNERS) if a.source == "all" else [a.source]
    allb, tot = {}, 0
    for n in names:
        try:
            res = RUNNERS[n](a, sites)
        except Blocked as e:
            BLOCKED.append("%s (%s)" % (n, e))
            log("BLOCKED", n, e)
            continue
        if not res:
            continue
        st, buyers = res
        tot += st["rows"]
        for b, v in buyers.items():
            cur = allb.setdefault(b, {"date": "", "site": ""})
            cur["date"] = max(cur["date"], v["date"])
            cur["site"] = cur["site"] or v["site"]
    print("sec_canada_providers: %d rows, %d distinct buyers, %d buyers dated in last 12 months, %d with website; blocked: %s"
          % (tot, len(allb), sum(1 for v in allb.values() if v["date"] >= RECENT), sum(1 for v in allb.values() if v["site"]),
             "; ".join(BLOCKED) or "none"), flush=True)


if __name__ == "__main__":
    main()
