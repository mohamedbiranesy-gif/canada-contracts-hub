#!/usr/bin/env python3
"""Dated buyer leads from ten small/medium public sources where the source itself gives the vendor's Canadian address.
No AI. One tool, one --source flag, one output file per source: ~/cch-leads/socrata_<key>.jsonl (overwritten).

Rule for every source: vendor in Canada = the source's own address / country field for that vendor says Canada (or a
Canadian province + postal code); the exact text is kept in canada_value. Buyer = a named organisation. Kept when the
record date >= 2023-11-02 or the published end date >= 2026-11-02. One line per (buyer, vendor), most recent record.
Bulk files are downloaded once into ~/cch-sources/<key>/ (tools fetch at most 1 request/second per host).
Websites: only when the source gives one, else Wikidata (exact label/alias, official website P856; Czech buyers by
ICO = P4156), at most 1 request/second to www.wikidata.org, cached in ~/cch-sources/<key>/wikidata_cache.json.

--source  (key)        source, URL, Canada filter, counts seen on 2026-11-02 (see notes at the bottom of each function)
Counts of the 2026-11-02 run (rows = (buyer, vendor) pairs / distinct buyers / buyers dated since 2025-11-02 / with website):
 ferc_eqr 1404/658/577/11 (2,196,859 contract rows read, 2023q4-2026q2; 2026q3 not on PUDL yet)
 cor 268/268/268/10 (75 queries, 2,620 certificates, 379 owners; cor.ca then timed out three times in a row, so it stopped)
 epa_hwexport 430/175/124/1 (78,059 WIETS export rows, 66,669 consented rows to Canada, 10,930 e-Manifest exports in window)
 dol5500c 216/145/48/13 (393 Schedule C rows with a CA provider, plan-year files 2023-2025)
 cz_smlouvy 30/20/20/19 (dumps 2026-04 .. 2026-11-01 only; older months were still downloading)
 es_menores 21/13/12/9 (2026-04 .. 2026-10 only; the Mac cannot verify contrataciondelestado.es's TLS chain, so run elsewhere)
 fec 41/38/13/0 ; ctco_solicitors 5/5/1/2 ; cms_openpayments 26/16/6/4 ; doe_ng skipped (no supplier address)
 ferc_eqr              FERC Electric Quarterly Reports via PUDL parquet (s3.us-west-2.amazonaws.com/pudl.catalyst.coop/
                       ferceqr/core_ferceqr__contracts|core_ferceqr__quarterly_identity/{yyyyqN}.parquet), 2023q4..latest.
                       Seller = filer whose identity row (filer_unique_id FS*) has contact_country_name 'CA' (its company
                       contact address); buyer = customer_company_name; affiliate contracts dropped. record_date = end of
                       the report quarter (contract in force that quarter), end_date = contract_termination_date.
 cor                   COR Kashruth Council of Canada certificates: POST cor.ca/wp-admin/admin-ajax.php
                       action=cor_certificate_search (<= 50 hits per query, snowball over product words, <= 1 req/s,
                       cap --max-queries 600). Buyer = brand_owner, vendor = COR, Canadian address read from cor.ca itself.
                       Kept when expires >= 2026-11-02 (record_date = retrieval date, end_date = expires).
 epa_hwexport          US EPA RCRAInfo WIETS export notices (WT.zip -> WT_NOTICES_EXPORTS) with FINAL/IMPORTER COUNTRY
                       'Canada' and a Consent determination (record_date = CONSENT START DATE, end_date = CONSENT END DATE),
                       plus e-Manifest exports (EM.zip member EM_EXPORT.zip read by HTTP range) with FOREIGN DES FAC
                       COUNTRY CODE 'CA' (record_date = DATE WASTE LEFT US). Buyer = US exporter, vendor = Canadian facility.
 dol5500c              DOL Form 5500 Schedule C Part I items 1 and 2 (askebsa.dol.gov FOIA files, plan years 2023-2025):
                       service providers with PROV_*_FOREIGN_CNTRY 'CA'; buyer = plan sponsor (F_5500 SPONSOR_DFE_NAME, join
                       on ACK_ID); record_date = filing date (first 8 digits of ACK_ID).
 cz_smlouvy            Czech Registr smluv monthly/daily XML dumps (data.smlouvy.gov.cz): counterparty smluvniStrana/adresa
                       matching Kanada/Canada (Czech localities named Kanada rejected); buyer = subjekt; record_date =
                       datumUzavreni; evidence = smlouvy.gov.cz/smlouva/<idVerze>.
 es_menores            Spain PLACSP contratos menores (sindicacion_1143 monthly zips): WinningParty country code CA.
 fec                   FEC operating expenditures (oppexp24/26.zip): payee STATE a Canadian province code (or ZZ) with a
                       Canadian postal code in ZIP_CODE, payee ENTITY_TP not IND; buyer = committee (cm24/26.zip).
 ctco_solicitors       Connecticut paid-solicitor campaigns (data.ct.gov q7t6-9q4w): paid_solicitor_city_state with a
                       Canadian province + postal code. Colorado (ew9y-6tv9) has no solicitor address field, so it is skipped.
 cms_openpayments      CMS Open Payments research payments, program years 2023-2025, recipient_country 'Canada'; buyer =
                       paying manufacturer, vendor = recipient entity (teaching hospital / non-covered entity).
 doe_ng                DOE natural-gas imports: the file only gives the gas's country of origin, not the supplier's address,
                       so it is skipped by rule (no same-record vendor address).

    python3 tools/misc_dated_sources.py --source ferc_eqr [--no-wikidata] [--wd-max 800]
"""
import argparse, csv, fcntl, gzip, html, io, json, os, re, sys, time, unicodedata, urllib.parse, urllib.request, zipfile

UA = "canada-contracts-hub-crawler/1.0 (+https://github.com/mohamedbiranesy-gif/canada-contracts-hub)"
SRC = os.path.expanduser("~/cch-sources")
LEADS = os.path.expanduser("~/cch-leads")
FROM, END_FROM, RECENT = "2023-11-02", "2026-11-02", "2025-11-02"
TODAY = time.strftime("%Y-%m-%d")
PROV = {"AB", "BC", "MB", "NB", "NL", "NS", "NT", "NU", "ON", "PE", "QC", "SK", "YT"}
PROV_NAMES = {"ALBERTA", "BRITISH COLUMBIA", "MANITOBA", "NEW BRUNSWICK", "NEWFOUNDLAND", "NOVA SCOTIA", "ONTARIO", "QUEBEC",
              "QUÉBEC", "SASKATCHEWAN", "PRINCE EDWARD ISLAND", "YUKON", "NORTHWEST TERRITORIES", "NUNAVUT"}
POSTAL = re.compile(r"\b[ABCEGHJ-NPRSTVXY]\d[ABCEGHJ-NPRSTV-Z] ?\d[ABCEGHJ-NPRSTV-Z]\d\b", re.I)
JUNK = re.compile(r"^(n/?a|none|various|multiple|unknown|undisclosed|confidential|tbd|-+|\.+|0)$", re.I)
_last = {}
csv.field_size_limit(1 << 30)


def log(*a):
    print(time.strftime("%H:%M:%S"), *a, flush=True)


def polite(host, gap=1.0):
    w = _last.get(host, 0) + gap - time.time()
    if w > 0:
        time.sleep(w)
    _last[host] = time.time()


def http(url, data=None, timeout=120, headers=None):
    polite(urllib.parse.urlparse(url).netloc)
    h = {"User-Agent": UA}
    h.update(headers or {})
    req = urllib.request.Request(url, data=data, headers=h)
    return urllib.request.urlopen(req, timeout=timeout).read()


def cached(key, url, name=None):
    """Download url once into ~/cch-sources/<key>/; return the local path (None on HTTP error)."""
    d = os.path.join(SRC, key)
    os.makedirs(d, exist_ok=True)
    p = os.path.join(d, name or os.path.basename(urllib.parse.urlparse(url).path).replace("%20", "_"))
    if os.path.exists(p) and os.path.getsize(p) > 0:
        return p
    try:
        polite(urllib.parse.urlparse(url).netloc)
        req = urllib.request.Request(url, headers={"User-Agent": UA})
        with urllib.request.urlopen(req, timeout=600) as r, open(p + ".part", "wb") as f:
            while True:
                b = r.read(1 << 20)
                if not b:
                    break
                f.write(b)
        os.replace(p + ".part", p)
        return p
    except Exception as e:
        log("download failed", url, e)
        return None


def norm(s):
    return re.sub(r"[^a-z0-9]+", " ", unicodedata.normalize("NFKD", s or "").encode("ascii", "ignore").decode().lower()).strip()


def clean(s):
    return re.sub(r"\s+", " ", html.unescape(s or "")).strip()


def iso(v):
    """Many date spellings -> YYYY-MM-DD ('' when unknown)."""
    if v is None:
        return ""
    if hasattr(v, "strftime"):
        return v.strftime("%Y-%m-%d")
    s = str(v).strip()
    m = re.match(r"^(\d{4})-?(\d{2})-?(\d{2})", s)
    if m:
        return "%s-%s-%s" % m.groups()
    m = re.match(r"^(\d{1,2})/(\d{1,2})/(\d{4})", s)
    if m:
        return "%s-%02d-%02d" % (m.group(3), int(m.group(1)), int(m.group(2)))
    m = re.match(r"^(\d{2})(\d{2})(\d{4})$", s)       # FEC MMDDYYYY
    if m:
        return "%s-%s-%s" % (m.group(3), m.group(1), m.group(2))
    return ""


def keep(record_date, end_date=""):
    return (record_date or "") >= FROM or (end_date or "") >= END_FROM


def host_of(w):
    w = (w or "").strip().lower()
    w = re.sub(r"^(https?://)?(www\.)?", "", w).split("/")[0].strip(" .")
    return w if re.fullmatch(r"[a-z0-9]([a-z0-9-]*[a-z0-9])?(\.[a-z0-9]([a-z0-9-]*[a-z0-9])?)*\.[a-z]{2,}", w) else ""


def lead(key, dataset, dataset_url, buyer, vendor, canada_field, canada_value, row, record_id, website=""):
    h = host_of(website)
    return {"platform": key, "domain": h, "dataset_id": record_id, "dataset": dataset, "dataset_url": dataset_url,
            "publisher": clean(buyer), "buyer_unit": "", "website": ("https://%s/" % h) if h else "", "vendor": clean(vendor),
            "canada_field": canada_field, "canada_value": clean(canada_value), "row": row}


# ---------------------------------------------------------------- Wikidata (shared 1 request/second across processes)
WD = "https://www.wikidata.org/w/api.php?"
LEGAL = re.compile(r"[,\s]+(inc|incorporated|l\.?l\.?c|llc|ltd|limited|corp|corporation|co|company|plc|lp|l\.?p|s\.?a|gmbh|ag|a\.?s|s\.?r\.?o)\.?$", re.I)


def wd_get(params):
    lock = os.path.join(SRC, ".wikidata_rate")
    with open(lock, "a+") as f:
        fcntl.flock(f, fcntl.LOCK_EX)
        f.seek(0)
        try:
            last = float(f.read() or 0)
        except ValueError:
            last = 0
        w = last + 1.05 - time.time()
        if w > 0:
            time.sleep(w)
        f.seek(0)
        f.truncate()
        f.write(str(time.time()))
        fcntl.flock(f, fcntl.LOCK_UN)
    try:
        req = urllib.request.Request(WD + urllib.parse.urlencode(dict(params, format="json")), headers={"User-Agent": UA})
        return json.load(urllib.request.urlopen(req, timeout=30))
    except Exception:
        return {}


def wd_clean(name):
    n = re.sub(r"\s*\(.*?\)\s*", " ", name or "")
    n = re.sub(r"^the\s+|,\s*the$", "", n.strip(), flags=re.I)
    for _ in range(2):
        n = LEGAL.sub("", n).strip(" ,.")
    return n


def wd_site(name, countries=None, ico=None):
    """Official website from Wikidata: exact label/alias match (or Czech ICO); one unambiguous site or None."""
    ids = []
    if ico:
        r = wd_get({"action": "query", "list": "search", "srsearch": "haswbstatement:P4156=%s" % ico, "srlimit": 3})
        ids = [x["title"] for x in r.get("query", {}).get("search", [])]
    if not ids:
        for v in dict.fromkeys([name, wd_clean(name)]):
            if len(norm(v).split()) < 2:
                continue
            res = wd_get({"action": "wbsearchentities", "search": v, "language": "en", "limit": 7, "type": "item"}).get("search", [])
            ids = [x["id"] for x in res if norm((x.get("match") or {}).get("text")) == norm(v) or norm(x.get("label")) == norm(v)]
            if ids:
                break
    if not ids:
        return None
    ents = wd_get({"action": "wbgetentities", "ids": "|".join(ids[:5]), "props": "claims"}).get("entities", {})
    found = {}
    for qid in ids[:5]:
        c = (ents.get(qid) or {}).get("claims", {})
        cs = {(x["mainsnak"].get("datavalue") or {}).get("value", {}).get("id") for x in c.get("P17", [])}
        if countries and not (cs & set(countries)):
            continue
        sites = [(x["mainsnak"].get("datavalue") or {}).get("value") for x in c.get("P856", [])]
        sites = [s for s in sites if s]
        if sites:
            found[host_of(sites[0])] = (sites[0], qid)
    found.pop("", None)
    return list(found.values())[0] if len(found) == 1 else None


def add_websites(key, leads, countries=None, wd_max=800, ico_field=None):
    cache_p = os.path.join(SRC, key, "wikidata_cache.json")
    try:
        cache = json.load(open(cache_p))
    except Exception:
        cache = {}
    names = []
    for l in leads:
        if not l["website"] and l["publisher"] not in names:
            names.append(l["publisher"])
    done = 0
    for n in names:
        if n in cache:
            continue
        if done >= wd_max:
            break
        ico = next((l["row"].get(ico_field) for l in leads if l["publisher"] == n and ico_field and l["row"].get(ico_field)), None)
        hit = wd_site(n, countries, ico)
        cache[n] = list(hit) if hit else None
        done += 1
        if done % 25 == 0:
            json.dump(cache, open(cache_p, "w"))
            log("wikidata", done, "of", len(names))
    json.dump(cache, open(cache_p, "w"))
    for l in leads:
        hit = cache.get(l["publisher"])
        if not l["website"] and hit:
            h = host_of(hit[0])
            l["website"], l["domain"] = "https://%s/" % h, h
            l["row"]["website_source"] = "wikidata %s P856" % hit[1]


def write(key, leads):
    best = {}
    for l in leads:
        k = (norm(l["publisher"]), norm(l["vendor"]))
        if not k[0] or JUNK.match(l["publisher"].strip()):
            continue
        if k not in best or (l["row"].get("record_date", ""), l["row"].get("end_date", "")) > \
                (best[k]["row"].get("record_date", ""), best[k]["row"].get("end_date", "")):
            best[k] = l
    out = sorted(best.values(), key=lambda l: (l["publisher"].lower(), l["vendor"].lower()))
    os.makedirs(LEADS, exist_ok=True)
    p = os.path.join(LEADS, "socrata_%s.jsonl" % key)
    with open(p + ".tmp", "w", encoding="utf-8") as f:
        for l in out:
            f.write(json.dumps(l, ensure_ascii=False, default=str) + "\n")
    os.replace(p + ".tmp", p)
    buyers = {norm(l["publisher"]) for l in out}
    recent = {norm(l["publisher"]) for l in out if l["row"].get("record_date", "") >= RECENT}
    site = {norm(l["publisher"]) for l in out if l["website"]}
    log("%s: %d rows, %d distinct buyers, %d buyers dated in last 12 months, %d with website -> %s"
        % (key, len(out), len(buyers), len(recent), len(site), p))
    return out


# ---------------------------------------------------------------- FERC EQR
def src_ferc_eqr(a):
    import pyarrow.parquet as pq
    base = "https://s3.us-west-2.amazonaws.com/pudl.catalyst.coop/ferceqr/"
    qs = ["%dq%d" % (y, q) for y in range(2023, 2027) for q in range(1, 5)]
    qs = qs[qs.index("2023q4"):]
    out, seen_rows = [], 0
    for q in qs:
        cp = cached("ferc_eqr", base + "core_ferceqr__contracts/%s.parquet" % q, "c_%s.parquet" % q)
        ip = cached("ferc_eqr", base + "core_ferceqr__quarterly_identity/%s.parquet" % q, "i_%s.parquet" % q)
        if not cp or not ip:
            continue
        y, n = int(q[:4]), int(q[-1])
        qend = ["%d-03-31", "%d-06-30", "%d-09-30", "%d-12-31"][n - 1] % y
        sellers = {}
        for r in pq.read_table(ip).to_pylist():
            if (r.get("filer_unique_id") or "").upper().startswith("FS") and (r.get("contact_country_name") or "").upper() == "CA":
                sellers[r["company_id_ferc"]] = r
        for r in pq.read_table(cp).to_pylist():
            seen_rows += 1
            s = sellers.get(r.get("seller_company_id_ferc"))
            if not s or r.get("contract_affiliate") is True or not (r.get("customer_company_name") or "").strip():
                continue
            act = iso(r.get("actual_termination_date"))
            rd = min(qend, act) if act else qend
            end = iso(r.get("contract_termination_date")) or act
            if not keep(rd, end):
                continue
            row = {k: (iso(v) if hasattr(v, "strftime") else v) for k, v in r.items()}
            for k in ("contact_address", "contact_city", "contact_state", "contact_zip", "contact_country_name", "company_name", "filer_unique_id"):
                row["seller_identity_" + k] = s.get(k)
            row["seller_name_has_us_llc_form"] = bool(re.search(r"\bL\.?L\.?C\b", s.get("company_name") or "", re.I))
            row.update(record_date=rd, end_date=end, date_basis="end of EQR report quarter %s (contract reported in force)" % q)
            addr = "%s, %s, %s %s, %s" % (s.get("contact_address"), s.get("contact_city"), s.get("contact_state"), s.get("contact_zip"), s.get("contact_country_name"))
            out.append(lead("ferc_eqr", "FERC Electric Quarterly Report contracts (PUDL), seller filer address in Canada",
                            base + "core_ferceqr__contracts/%s.parquet" % q, r["customer_company_name"], r["seller_company_name"],
                            "contact_address/contact_country_name (FERC EQR seller identity, %s)" % q, addr, row,
                            "%s:%s:%s" % (q, r["seller_company_id_ferc"], r["contract_unique_id"])))
        log(q, "canadian sellers", len(sellers), "leads so far", len(out))
    log("contract rows seen", seen_rows)
    if not a.no_wikidata:
        add_websites("ferc_eqr", write("ferc_eqr", out), ["Q30", "Q16"], a.wd_max)
    return write("ferc_eqr", out)


# ---------------------------------------------------------------- COR
COR_SEEDS = """oil sugar flour salt butter cheese milk cream yogurt chocolate cocoa vanilla coffee tea juice water wine beer
vinegar honey syrup maple jam fruit berry apple orange lemon lime grape cherry peach pear plum mango banana coconut
almond walnut pecan cashew peanut pistachio hazelnut seed sesame flax chia quinoa rice oat barley wheat corn soy bean
lentil pea chickpea potato tomato onion garlic pepper ginger cinnamon spice herb basil oregano mint parsley dill mustard
ketchup mayonnaise sauce dressing soup broth stock pasta noodle bread bagel bun roll cracker cookie biscuit cake muffin
donut pastry pie tart pizza dough crust cereal granola bar snack chip pretzel popcorn candy gum jelly gelatin marshmallow
caramel toffee fudge licorice mint frozen ice dessert pudding custard egg tofu tempeh hummus salsa pickle olive relish
fish salmon tuna herring sardine meat beef chicken turkey sausage deli smoked kosher pareve dairy glatt passover
vitamin supplement protein powder capsule tablet extract flavour flavor natural artificial colour color emulsifier
lecithin enzyme yeast starch glucose dextrose fructose maltodextrin sweetener stevia sucralose citric acid sodium
potassium calcium magnesium phosphate carbonate chloride sulfate oxide glycerin glycerine stearate palm canola sunflower
safflower avocado shortening margarine lard tallow wax resin gum xanthan guar pectin agar carrageenan cellulose fibre
fiber inulin collagen whey casein lactose isolate concentrate hydrolyzed oleoresin essential distillate alcohol ethanol
solvent cleaning detergent soap lubricant packaging film bag container bottle cap label carton foil paper plastic
tank transport trucking cleaning sanitizer disinfectant bleach ammonia nitrogen carbon dioxide propane gas
seasoning blend mix premix batter breading coating crumb topping filling icing frosting glaze sprinkles decor
organic gluten vegan keto halal baby infant formula pet food feed animal grain malt hops kombucha soda energy drink
cocktail mixer liqueur vodka whisky rum gin tequila spirits cider mead sake""".split()
COR_STOP = {"with", "and", "the", "for", "free", "from", "size", "pack", "case", "bulk", "inc", "ltd", "llc", "corp",
            "company", "canada", "foods", "food", "products", "product", "brand", "style", "type", "grade", "white", "black",
            "green", "red", "blue", "yellow", "large", "small", "medium", "mini", "classic", "original", "premium", "regular"}


def src_cor(a):
    url = "https://cor.ca/wp-admin/admin-ajax.php"
    # COR's own address, from cor.ca itself
    addr = ""
    for page in ("https://cor.ca/", "https://cor.ca/contact-us/", "https://cor.ca/contact/"):
        try:
            t = clean(re.sub(r"<[^>]+>", " ", http(page, timeout=60).decode("utf-8", "replace")))
        except Exception as e:
            log("cor page", page, e)
            continue
        m = re.search(r"215 Ranee Ave[^|]{0,60}?M6A ?0C7", t, re.I) or re.search(r"[^.]{0,60}Toronto,? (ON|Ontario)[^.]{0,20}M\d[A-Z] ?\d[A-Z]\d", t)
        if m:
            addr, addr_page = m.group(0).strip(), page
            break
    if not addr:
        log("COR address not found on cor.ca; stopping (no proof of vendor location)")
        return []
    state_p = os.path.join(SRC, "cor", "certificates.json")
    try:
        st = json.load(open(state_p))
    except Exception:
        st = {"tried": {}, "certs": {}}
    queue = [w for w in COR_SEEDS if w not in st["tried"]]
    extra = []
    for c in st["certs"].values():
        extra += re.findall(r"[a-z]{4,}", (c.get("name") or "").lower())
    queue += [w for w in dict.fromkeys(extra) if w not in st["tried"] and w not in COR_STOP]
    queue = list(dict.fromkeys(queue))
    n = 0
    while queue and len(st["tried"]) < a.max_queries:
        term = queue.pop(0)
        if term in st["tried"]:
            continue
        try:
            d = json.loads(http(url, data=urllib.parse.urlencode({"action": "cor_certificate_search", "search": term}).encode(), timeout=60))
        except Exception as e:
            log("cor query failed", term, e)
            if "403" in str(e) or "429" in str(e):
                log("blocked; stopping")
                break
            st["tried"][term] = -1
            continue
        res = d.get("result") or [] if isinstance(d, dict) else []
        st["tried"][term] = d.get("size") if isinstance(d, dict) else 0
        new_owner = False
        owners = {norm(c.get("brand_owner")) for c in st["certs"].values()}
        for c in res:
            if c.get("ukd_id") and c["ukd_id"] not in st["certs"]:
                st["certs"][c["ukd_id"]] = c
                if norm(c.get("brand_owner")) not in owners:
                    new_owner = True
                    owners.add(norm(c.get("brand_owner")))
                words = [w for w in re.findall(r"[a-z]{4,}", (c.get("name") or "").lower()) if w not in COR_STOP and w not in st["tried"]]
                if new_owner:
                    queue[:0] = words           # words from a new owner's products first
                else:
                    queue.extend(words)
        queue = list(dict.fromkeys(queue))
        n += 1
        if n % 25 == 0:
            json.dump(st, open(state_p, "w"))
            log("cor queries", len(st["tried"]), "certs", len(st["certs"]), "owners", len(owners))
    json.dump(st, open(state_p, "w"))
    log("cor queries", len(st["tried"]), "certificates", len(st["certs"]))
    out = []
    for c in st["certs"].values():
        exp = iso(c.get("expires"))
        if not (c.get("brand_owner") or "").strip() or exp < END_FROM:
            continue
        row = dict(c, record_date=TODAY, end_date=exp, date_basis="certificate listed on cor.ca on retrieval date, expires %s" % exp,
                   vendor_address_page=addr_page)
        out.append(lead("cor", "COR (Kashruth Council of Canada) kosher certificates in force", c.get("url") or "https://cor.ca/",
                        c["brand_owner"], "COR - Kashruth Council of Canada", "address on %s (cor.ca, vendor's own site)" % addr_page,
                        addr, row, c.get("ukd_id")))
    if not a.no_wikidata:
        add_websites("cor", write("cor", out), None, a.wd_max)
    return write("cor", out)


# ---------------------------------------------------------------- EPA hazardous-waste exports
class HttpRange(io.RawIOBase):
    def __init__(self, url):
        self.url, self.pos = url, 0
        req = urllib.request.Request(url, method="HEAD", headers={"User-Agent": UA})
        self.size = int(urllib.request.urlopen(req, timeout=60).headers["Content-Length"])

    def seekable(self):
        return True

    def readable(self):
        return True

    def tell(self):
        return self.pos

    def seek(self, off, whence=0):
        self.pos = off if whence == 0 else (self.pos + off if whence == 1 else self.size + off)
        return self.pos

    def read(self, n=-1):
        if n is None or n < 0:
            n = self.size - self.pos
        if n == 0 or self.pos >= self.size:
            return b""
        end = min(self.size, self.pos + n) - 1
        polite("s3.amazonaws.com", 0.5)
        req = urllib.request.Request(self.url, headers={"User-Agent": UA, "Range": "bytes=%d-%d" % (self.pos, end)})
        b = urllib.request.urlopen(req, timeout=120).read()
        self.pos += len(b)
        return b

    def readinto(self, buf):
        b = self.read(len(buf))
        buf[:len(b)] = b
        return len(b)


def src_epa_hwexport(a):
    mods = json.loads(http("https://rcrapublic.epa.gov/rcra-hwip/api/export/modules", timeout=60))
    url = {m["fileName"]: m["url"] for m in mods}
    out = []
    wt = cached("epa_hwexport", url["WT.zip"])
    z = zipfile.ZipFile(wt)
    inner = zipfile.ZipFile(io.BytesIO(z.read("WT_NOTICES_EXPORTS.zip")))
    seen = ca = 0
    for mem in inner.namelist():
        if not mem.lower().endswith(".csv"):
            continue
        for r in csv.DictReader(io.TextIOWrapper(inner.open(mem), encoding="utf-8", errors="replace")):
            seen += 1
            if (r.get("DETERMINATION") or "").strip().lower() != "consent":
                continue
            if (r.get("FINAL COUNTRY") or "").strip().lower() == "canada":
                v, vaddr, vf = r.get("FINAL NAME"), "%s, %s" % (r.get("FINAL ADDRESS"), r.get("FINAL COUNTRY")), "FINAL ADDRESS / FINAL COUNTRY"
            elif (r.get("IMPORTER COUNTRY") or "").strip().lower() == "canada":
                v, vaddr, vf = r.get("IMPORTER NAME"), "%s, %s" % (r.get("IMPORTER ADDRESS"), r.get("IMPORTER COUNTRY")), "IMPORTER ADDRESS / IMPORTER COUNTRY"
            else:
                continue
            ca += 1
            rd, end = iso(r.get("CONSENT START DATE")) or iso(r.get("DETERMINATION ISSUED DATE")), iso(r.get("CONSENT END DATE"))
            if not keep(rd, end) or not (r.get("EXPORTER NAME") or "").strip():
                continue
            row = dict(r, record_date=rd, end_date=end, date_basis="CONSENT START DATE / CONSENT END DATE")
            out.append(lead("epa_hwexport", "US EPA WIETS hazardous-waste export notices, consented, receiving facility in Canada",
                            url["WT.zip"], r["EXPORTER NAME"], v, "%s (EPA WIETS WT_NOTICES_EXPORTS)" % vf, vaddr, row,
                            "%s:%s" % (r.get("NOTICE ID"), r.get("WASTE STREAM NUMBER"))))
    log("WIETS export rows", seen, "Canada consent rows", ca, "kept", len(out))
    try:
        em = zipfile.ZipFile(HttpRange(url["EM.zip"]))
        member = next(n for n in em.namelist() if n.upper().startswith("EM_EXPORT"))
        p = os.path.join(SRC, "epa_hwexport", "EM_EXPORT.zip")
        if not os.path.exists(p):
            open(p, "wb").write(em.read(member))
        ez = zipfile.ZipFile(p)
        n0 = len(out)
        for mem in ez.namelist():
            if not mem.lower().endswith(".csv"):
                continue
            for r in csv.DictReader(io.TextIOWrapper(ez.open(mem), encoding="utf-8", errors="replace")):
                if (r.get("FOREIGN DES FAC COUNTRY CODE") or "").strip().upper() != "CA":
                    continue
                rd = iso(r.get("DATE WASTE LEFT US"))
                if not keep(rd) or not (r.get("EXPORTER NAME") or "").strip():
                    continue
                vaddr = ", ".join(x for x in (r.get("FOREIGN DES FAC STREET"), r.get("FOREIGN DES FAC CITY"), r.get("FOREIGN DES FAC PROVINCE"),
                                              r.get("FOREIGN DES FAC POSTAL CODE"), r.get("FOREIGN DES FAC COUNTRY NAME")) if x)
                row = dict(r, record_date=rd, date_basis="DATE WASTE LEFT US")
                out.append(lead("epa_hwexport", "US EPA e-Manifest hazardous-waste exports to a facility in Canada", url["EM.zip"],
                                r["EXPORTER NAME"], r.get("FOREIGN DES FAC NAME"), "FOREIGN DES FAC STREET..COUNTRY CODE (EPA e-Manifest EM_EXPORT)",
                                vaddr, row, r.get("MANIFEST TRACKING NUMBER")))
        log("e-Manifest export leads", len(out) - n0)
    except Exception as e:
        log("e-Manifest export part failed:", e)
    if not a.no_wikidata:
        add_websites("epa_hwexport", write("epa_hwexport", out), ["Q30"], a.wd_max)
    return write("epa_hwexport", out)


# ---------------------------------------------------------------- DOL Form 5500 Schedule C
def src_dol5500c(a):
    base = "https://askebsa.dol.gov/FOIA%20Files/{y}/All/"
    hits = []
    for y in (2025, 2024, 2023):
        for item, pre in (("ITEM2", "PROVIDER_OTHER_"), ("ITEM1", "PROVIDER_ELIGIBLE_")):
            p = cached("dol5500c", (base + "F_SCH_C_PART1_%s_{y}_All.zip" % item).format(y=y))
            if not p:
                continue
            z = zipfile.ZipFile(p)
            for mem in z.namelist():
                if not mem.lower().endswith(".csv"):
                    continue
                for r in csv.DictReader(io.TextIOWrapper(z.open(mem), encoding="latin-1")):
                    cf = next((k for k in r if "FOREIGN_CNTRY" in k), None)
                    if cf and (r.get(cf) or "").strip().upper() == "CA":
                        hits.append((y, item, mem, r))
    log("Schedule C rows with a Canadian provider", len(hits))
    acks = {r["ACK_ID"] for _, _, _, r in hits}
    spons = {}
    for y in (2025, 2024, 2023):
        p = cached("dol5500c", (base + "F_5500_{y}_All.zip").format(y=y))
        if not p:
            continue
        z = zipfile.ZipFile(p)
        for mem in z.namelist():
            if not mem.lower().endswith(".csv"):
                continue
            for r in csv.DictReader(io.TextIOWrapper(z.open(mem), encoding="latin-1")):
                if r.get("ACK_ID") in acks:
                    spons[r["ACK_ID"]] = {k: v for k, v in r.items() if v not in ("", None)}
    out = []
    for y, item, mem, r in hits:
        s = spons.get(r["ACK_ID"])
        if not s:
            continue
        rd = iso(r["ACK_ID"][:8])
        if not keep(rd):
            continue
        name = next((r[k] for k in r if k.endswith("_NAME") and k.startswith("PROVIDER")), "")
        parts = [r.get(k) for k in r if "FOREIGN" in k and r.get(k)]
        row = {"schedule_c": dict(r), "form_5500": {k: s.get(k) for k in ("ACK_ID", "PLAN_NAME", "SPONSOR_DFE_NAME", "SPONS_DFE_EIN",
               "SPONS_DFE_MAIL_US_CITY", "SPONS_DFE_MAIL_US_STATE", "SPONS_DFE_MAIL_US_ZIP", "SPONS_DFE_DBA_NAME", "FORM_PLAN_YEAR_BEGIN_DATE",
               "FORM_TAX_PRD", "DATE_RECEIVED", "BUSINESS_CODE") if s.get(k)}, "plan_year_file": y, "schedule_c_item": item,
               "record_date": rd, "date_basis": "filing timestamp in ACK_ID"}
        out.append(lead("dol5500c", "DOL Form 5500 Schedule C service providers with a Canadian address",
                        (base + "F_SCH_C_PART1_%s_{y}_All.zip" % item).format(y=y), s.get("SPONSOR_DFE_NAME", ""), name,
                        "PROV_*_FOREIGN_* (DOL Form 5500 Schedule C Part I %s)" % item, ", ".join(parts), row, r["ACK_ID"]))
    if not a.no_wikidata:
        add_websites("dol5500c", write("dol5500c", out), ["Q30"], a.wd_max)
    return write("dol5500c", out)


# ---------------------------------------------------------------- Czech Registr smluv
CZ_CA = re.compile(r"\b(canada|kanada)\b", re.I)
CZ_NOT = re.compile(r"Česk|Cesk|\[CZ\]|Kanada,?\s*\d{3}\s?\d{2}|\d{3}\s?\d{2}\s+Kanada", re.I)
CZ_END = re.compile(r"\b(canada|kanada)\b[\s,.\-]*(\w{1,3}\s?\w{0,3})?[\s,.\]]*$", re.I)   # the country is the last word


def cz_tag(s, tag):
    m = re.search(r"<%s>(.*?)</%s>" % (tag, tag), s, re.S)
    return clean(m.group(1)) if m else ""


def src_cz_smlouvy(a):
    d = os.path.join(SRC, "cz_smlouvy")
    files = sorted(f for f in os.listdir(d) if re.match(r"dump_\d{4}_\d{2}(_\d{2})?\.xml$", f))
    out, recs = [], 0
    for f in files:
        buf, n0 = "", len(out)
        with open(os.path.join(d, f), encoding="utf-8", errors="replace") as fh:
            for chunk in iter(lambda: fh.read(1 << 22), ""):
                buf += chunk
                parts = buf.split("</zaznam>")
                buf = parts.pop()
                for r in parts:
                    recs += 1
                    if not CZ_CA.search(r):
                        continue
                    sub = re.search(r"<subjekt>(.*?)</subjekt>", r, re.S)
                    sub = sub.group(1) if sub else ""
                    for sp in re.findall(r"<smluvniStrana>(.*?)</smluvniStrana>", r, re.S):
                        adr = cz_tag(sp, "adresa")
                        if not adr or not CZ_CA.search(adr) or CZ_NOT.search(adr):
                            continue
                        if not (CZ_END.search(adr) or POSTAL.search(adr)):   # "Canada Square, London", "Canada do ..., Portugal"
                            continue
                        rd = iso(cz_tag(r, "datumUzavreni")) or iso(cz_tag(r, "casZverejneni"))
                        if not keep(rd) or cz_tag(r, "platnyZaznam") == "0":
                            continue
                        row = {"idSmlouvy": cz_tag(r, "idSmlouvy"), "idVerze": cz_tag(r, "idVerze"), "odkaz": cz_tag(r, "odkaz"),
                               "casZverejneni": cz_tag(r, "casZverejneni"), "predmet": cz_tag(r, "predmet"),
                               "datumUzavreni": cz_tag(r, "datumUzavreni"), "cisloSmlouvy": cz_tag(r, "cisloSmlouvy"),
                               "hodnotaBezDph": cz_tag(r, "hodnotaBezDph"), "hodnotaVcetneDph": cz_tag(r, "hodnotaVcetneDph"),
                               "ciziMena": cz_tag(r, "ciziMena"), "platnyZaznam": cz_tag(r, "platnyZaznam"),
                               "subjekt_nazev": cz_tag(sub, "nazev"), "subjekt_ico": cz_tag(sub, "ico"), "subjekt_adresa": cz_tag(sub, "adresa"),
                               "subjekt_datovaSchranka": cz_tag(sub, "datovaSchranka"), "subjekt_utvar": cz_tag(sub, "utvar"),
                               "smluvniStrana_nazev": cz_tag(sp, "nazev"), "smluvniStrana_ico": cz_tag(sp, "ico"), "smluvniStrana_adresa": adr,
                               "dump_file": f, "record_date": rd, "date_basis": "datumUzavreni"}
                        out.append(lead("cz_smlouvy", "Czech Registr smluv (public-sector contracts register)",
                                        row["odkaz"] or "https://data.smlouvy.gov.cz/%s" % f, row["subjekt_nazev"], row["smluvniStrana_nazev"],
                                        "smluvniStrana/adresa (Registr smluv)", adr, row, row["idVerze"]))
        log(f, "kept", len(out) - n0, "records so far", recs)
    if not a.no_wikidata:
        add_websites("cz_smlouvy", write("cz_smlouvy", out), ["Q213"], a.wd_max, ico_field="subjekt_ico")
    return write("cz_smlouvy", out)


# ---------------------------------------------------------------- Spain PLACSP contratos menores
def src_es_menores(a):
    d = os.path.join(SRC, "es_menores")
    ENTRY = re.compile(r"<entry>.*?</entry>", re.S)
    WIN = re.compile(r"<cac:WinningParty>.*?</cac:WinningParty>", re.S)
    CA = re.compile(r"<cac:Country>\s*<cbc:IdentificationCode[^>]*>CA</cbc:IdentificationCode>", re.S)
    out, n = [], 0
    for f in sorted(x for x in os.listdir(d) if x.endswith(".zip")):
        z = zipfile.ZipFile(os.path.join(d, f))
        for m in z.namelist():
            if not m.endswith(".atom"):
                continue
            s = z.read(m).decode("utf-8", "replace")
            for e in ENTRY.findall(s):
                n += 1
                if "WinningParty" not in e:
                    continue
                for w in WIN.findall(e):
                    if not CA.search(w):
                        continue
                    t = lambda pat, src=e: clean(re.sub(r"<[^>]+>", " ", (re.search(pat, src, re.S) or [None, ""])[1] if re.search(pat, src, re.S) else ""))
                    buyer = t(r"<cac-place-ext:LocatedContractingParty>.*?<cac:PartyName>\s*<cbc:Name>(.*?)</cbc:Name>")
                    vendor = t(r"<cac:PartyName>\s*<cbc:Name>(.*?)</cbc:Name>", w)
                    addr = ", ".join(x for x in (t(r"<cbc:StreetName>(.*?)</cbc:StreetName>", w), t(r"<cbc:CityName>(.*?)</cbc:CityName>", w),
                                                 t(r"<cbc:PostalZone>(.*?)</cbc:PostalZone>", w), t(r"<cac:Country>.*?<cbc:Name>(.*?)</cbc:Name>", w)) if x)
                    code = "CA"
                    if re.search(r"\bS\.?\s?(L|A|L\.?U|COOP)\.?$", vendor, re.I) and not POSTAL.search(addr):
                        continue                    # Spanish company keyed CA by mistake (e.g. Cadiz), no Canadian postcode
                    rd = iso(t(r"<cbc:AwardDate>(.*?)</cbc:AwardDate>")) or iso(t(r"<updated>(.*?)</updated>"))
                    if not keep(rd) or not buyer:
                        continue
                    link = (re.search(r'<link[^>]*href="([^"]+)"', e) or [None, ""])[1]
                    row = {"id": t(r"<id>(.*?)</id>"), "title": t(r"<title>(.*?)</title>"), "updated": t(r"<updated>(.*?)</updated>"),
                           "ContractFolderID": t(r"<cbc:ContractFolderID>(.*?)</cbc:ContractFolderID>"), "AwardDate": t(r"<cbc:AwardDate>(.*?)</cbc:AwardDate>"),
                           "PayableAmount": t(r"<cbc:PayableAmount[^>]*>(.*?)</cbc:PayableAmount>"), "winning_party_name": vendor,
                           "winning_party_address": addr, "winning_party_country_code": code, "buyer_name": buyer,
                           "buyer_website": t(r"<cbc:WebsiteURI>(.*?)</cbc:WebsiteURI>"), "zip": f, "member": m,
                           "record_date": rd, "date_basis": "cbc:AwardDate"}
                    out.append(lead("es_menores", "Spain PLACSP contratos menores, winning party country CA", html.unescape(link) or f, buyer,
                                    vendor, "WinningParty/PhysicalLocation/Address/Country/IdentificationCode (PLACSP)",
                                    "%s (country code CA)" % addr if addr else "country code CA", row, row["id"], row["buyer_website"]))
        log(f, "entries so far", n, "leads", len(out))
    if not a.no_wikidata:
        add_websites("es_menores", write("es_menores", out), ["Q29"], a.wd_max)
    return write("es_menores", out)


# ---------------------------------------------------------------- FEC operating expenditures
FEC_COLS = "CMTE_ID AMNDT_IND RPT_YR RPT_TP IMAGE_NUM LINE_NUM FORM_TP_CD SCHED_TP_CD NAME CITY STATE ZIP_CODE TRANSACTION_DT TRANSACTION_AMT TRANSACTION_PGI PURPOSE CATEGORY CATEGORY_DESC MEMO_CD MEMO_TEXT ENTITY_TP SUB_ID FILE_NUM TRAN_ID BACK_REF_TRAN_ID".split()
CM_COLS = "CMTE_ID CMTE_NM TRES_NM CMTE_ST1 CMTE_ST2 CMTE_CITY CMTE_ST CMTE_ZIP CMTE_DSGN CMTE_TP CMTE_PTY_AFFILIATION CMTE_FILING_FREQ ORG_TP CONNECTED_ORG_NM CAND_ID".split()


def src_fec(a):
    cms, out = {}, []
    for c in ("24", "26"):
        p = cached("fec", "https://www.fec.gov/files/bulk-downloads/20%s/cm%s.zip" % (c, c))
        z = zipfile.ZipFile(p)
        for line in io.TextIOWrapper(z.open(z.namelist()[0]), encoding="latin-1"):
            f = line.rstrip("\n").split("|")
            cms[f[0]] = dict(zip(CM_COLS, f))
    for c in ("24", "26"):
        p = cached("fec", "https://www.fec.gov/files/bulk-downloads/20%s/oppexp%s.zip" % (c, c))
        z = zipfile.ZipFile(p)
        mem = [n for n in z.namelist() if n.endswith(".txt")][0]
        for line in io.TextIOWrapper(z.open(mem), encoding="latin-1"):
            f = line.rstrip("\n").split("|")
            if len(f) < 21:
                continue
            r = dict(zip(FEC_COLS, f))
            st, zp = r["STATE"].strip().upper(), r["ZIP_CODE"].strip().upper()
            if not ((st in PROV or st == "ZZ") and POSTAL.fullmatch(zp.replace(" ", "")[:3] + " " + zp.replace(" ", "")[3:6]) and len(zp.replace(" ", "")) == 6):
                continue
            if r["ENTITY_TP"].strip().upper() == "IND" or r["MEMO_CD"].strip().upper() == "X":
                continue
            rd = iso(r["TRANSACTION_DT"])
            cm = cms.get(r["CMTE_ID"], {})
            if not keep(rd) or not cm.get("CMTE_NM"):
                continue
            row = dict(r, committee={k: cm.get(k) for k in ("CMTE_ID", "CMTE_NM", "CMTE_CITY", "CMTE_ST", "CMTE_TP", "CMTE_DSGN", "CONNECTED_ORG_NM")},
                       record_date=rd, date_basis="TRANSACTION_DT")
            out.append(lead("fec", "FEC operating expenditures to payees with a Canadian address", "https://docquery.fec.gov/cgi-bin/fecimg/?%s" % r["IMAGE_NUM"],
                            cm["CMTE_NM"], r["NAME"], "CITY/STATE/ZIP_CODE (FEC operating expenditures)", "%s, %s %s" % (r["CITY"], st, zp), row, r["SUB_ID"]))
    return write("fec", out)


# ---------------------------------------------------------------- CT paid solicitors
CA_ADDR = re.compile(r"(\b(%s)\b\.?,?\s+%s)|\bCANADA\b" % ("|".join(PROV), POSTAL.pattern), re.I)


def src_ctco_solicitors(a):
    out, off = [], 0
    while True:
        rows = json.loads(http("https://data.ct.gov/resource/q7t6-9q4w.json?$limit=5000&$offset=%d&$order=:id" % off, timeout=120))
        for r in rows:
            v = "%s, %s" % (r.get("paid_solicitor_address_line_1", ""), r.get("paid_solicitor_city_state", ""))
            if not CA_ADDR.search(r.get("paid_solicitor_city_state", "")):
                continue
            rd, end = iso(r.get("campaign_start_date")), iso(r.get("campaign_end_date"))
            if not keep(rd, end):
                continue
            row = dict(r, record_date=rd, end_date=end, date_basis="campaign_start_date / campaign_end_date")
            out.append(lead("ctco_solicitors", "Connecticut charity paid-solicitor campaigns, solicitor address in Canada",
                            "https://data.ct.gov/d/q7t6-9q4w", r.get("charitable_organization_name", ""), r.get("paid_solicitor_name", ""),
                            "paid_solicitor_address_line_1 / paid_solicitor_city_state (data.ct.gov q7t6-9q4w)", v, row, r.get("campaign_registration_no", "")))
        if len(rows) < 5000:
            break
        off += 5000
    if not a.no_wikidata:
        add_websites("ctco_solicitors", write("ctco_solicitors", out), ["Q30"], a.wd_max)
    return write("ctco_solicitors", out)


# ---------------------------------------------------------------- CMS Open Payments research
def src_cms_openpayments(a):
    base = "https://openpaymentsdata.cms.gov/api/1/"
    items = json.loads(http(base + "metastore/schemas/dataset/items", timeout=120))
    ds = [(i.get("title", ""), i["identifier"]) for i in items if re.search(r"(2023|2024|2025) Research Payment Data", i.get("title", ""), re.I)]
    log("datasets", ds)
    out = []
    for title, ident in ds:
        off = 0
        while True:
            q = urllib.parse.urlencode({"conditions[0][property]": "recipient_country", "conditions[0][value]": "Canada",
                                        "conditions[0][operator]": "=", "limit": 500, "offset": off})
            d = json.loads(http(base + "datastore/query/%s/0?%s" % (ident, q), timeout=120))
            res = d.get("results", [])
            for r in res:
                vendor = r.get("noncovered_recipient_entity_name") or r.get("teaching_hospital_name") or ""
                buyer = r.get("applicable_manufacturer_or_applicable_gpo_making_payment_name", "")
                rd = iso(r.get("date_of_payment"))
                if not vendor.strip() or not keep(rd):
                    continue
                addr = ", ".join(x for x in (r.get("recipient_primary_business_street_address_line1"), r.get("recipient_city"),
                                             r.get("recipient_province") or r.get("recipient_state"), r.get("recipient_postal_code") or r.get("recipient_zip_code"),
                                             r.get("recipient_country")) if x)
                row = {k: v for k, v in r.items() if v not in ("", None) and not k.startswith("covered_recipient_") and "principal_investigator" not in k}
                row.update(record_date=rd, date_basis="date_of_payment", dataset_title=title)
                out.append(lead("cms_openpayments", "CMS Open Payments research payments to entities in Canada",
                                "https://openpaymentsdata.cms.gov/dataset/%s" % ident, buyer, vendor,
                                "recipient address / recipient_country (CMS Open Payments)", addr, row, r.get("record_id", "")))
            if len(res) < 500:
                break
            off += 500
    if not a.no_wikidata:
        add_websites("cms_openpayments", write("cms_openpayments", out), ["Q30"], a.wd_max)
    return write("cms_openpayments", out)


def src_doe_ng(a):
    log("doe_ng skipped: the DOE file names the supplier and the gas's country of origin, never the supplier's address")
    return []


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--source", required=True, choices=[k[4:] for k in globals() if k.startswith("src_")])
    ap.add_argument("--no-wikidata", action="store_true")
    ap.add_argument("--wd-max", type=int, default=800)
    ap.add_argument("--max-queries", type=int, default=600)
    a = ap.parse_args()
    globals()["src_" + a.source](a)


if __name__ == "__main__":
    main()
