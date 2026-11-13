#!/usr/bin/env python3
"""Business licences and merchant permits (open data of Canadian cities and regulators) joined to the organisations we hold.

A business licence is a dated payment to a Canadian public body: the body's own open data gives the licence number, the trade and / or legal
name, the address, the issue and expiry dates, the status and — Vancouver — the fee paid. For an organisation whose own site we have read
(name, postal address, telephone), a licence in force is a recorded, current relationship with a named Canadian payee.

Sources (fields as the portals returned them in the probe run 42770146197, 2026-11-10; each payee's address and fee sentence opened and quoted):
  vancouver  Opendatasoft  business-licences                 licence no., legal + trade name, status, issued, expires, address with postal code, fee paid
  calgary    Socrata       vdjc-pybd                         trade name, street address (no postal code), first issue, expiry, status
  edmonton   Socrata       qhi4-bdpu                         business name, street address, original / latest issue, expiry
  toronto    CKAN          169e90ba-…  (MLS business licences) licence no., operating + client name, issued, cancel date, address with postal code, telephone
  opc        CKAN (Données Québec) c40c7af7-…                permits in force of the Office de la protection du consommateur: permit no., category, name, NEQ, address

Matching is strict. A licence is tied to an organisation only when
  (a) the postal code is the same, or the telephone number is the same, or the street number + street name are the same in the same city, AND
  (b) the names agree: every word of the shorter name is in the longer one, and what agrees identifies (three words, or one word that is not
      a generic trade / place word).
Several different licensees fitting one organisation: dropped. Licensees that are natural persons (Vancouver prints them in brackets; Toronto
client names without a legal form) are left out.

  probe                 search each portal's catalogue for licence datasets; print ids, row counts, fields, sample rows (nothing is written)
  pull [--only a,b]     download the configured datasets (licences in force) -> out/licences_<source>.csv.gz
  match DIR             join to the delivered rows and the site facts -> out/licence_leads.jsonl
  merge DIR --stamp S   -> data/incoming/claude/lead_shards/leads_lic_<S>.gz + details_lic_<S>.gz (rank.py and the mailbox crawl read lead_shards/)
No site is crawled: only the open-data portals' API / bulk endpoints, a few requests each.
"""
import argparse, collections, csv, glob, gzip, hashlib, io, json, os, re, sys, time, unicodedata, urllib.parse, urllib.request

csv.field_size_limit(1 << 30)
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
INC = os.path.join(ROOT, "data/incoming/claude")
SHARDS = os.path.join(INC, "lead_shards")
UA = "canada-contracts-hub-crawler/1.0 (+https://github.com/mohamedbiranesy-gif/canada-contracts-hub)"
TODAY = time.strftime("%Y-%m-%d")
LEAD_COLS = ["buyer_key", "buyer_name", "website", "canadian_vendor_rows", "example_vendor", "canada_field_value", "evidence_dataset", "latest_record_date"]

# portal catalogues to search (probe). kind: ods = Opendatasoft, socrata, ckan
PORTALS = [
    ("vancouver", "ods", "https://opendata.vancouver.ca"), ("calgary", "socrata", "https://data.calgary.ca"), ("edmonton", "socrata", "https://data.edmonton.ca"),
    ("toronto", "ckan", "https://ckan0.cf.opendata.inter.prod-toronto.ca"), ("winnipeg", "socrata", "https://data.winnipeg.ca"),
    ("montreal", "ckan", "https://donnees.montreal.ca"), ("quebec", "ckan", "https://www.donneesquebec.ca/recherche"), ("novascotia", "socrata", "https://data.novascotia.ca"),
    ("ottawa", "ckan", "https://open.ottawa.ca"), ("bc", "ckan", "https://catalogue.data.gov.bc.ca"), ("ontario", "ckan", "https://data.ontario.ca"), ("alberta", "ckan", "https://open.alberta.ca"),
    ("canada", "ckan", "https://open.canada.ca/data"), ("saskatoon", "ods", "https://opendata.saskatoon.ca"), ("kelowna", "ods", "https://opendata.kelowna.ca"),
    ("surrey", "ckan", "https://data.surrey.ca"), ("victoria", "ods", "https://opendata.victoria.ca"),
]
QUERIES = ["business licence", "business license", "licensed establishments", "liquor licence", "permis", "licence holders", "registered businesses"]

SOURCES = {
    "vancouver": dict(
        kind="ods", base="https://opendata.vancouver.ca", dataset="business-licences", where="status = 'Issued' AND expireddate >= date'%s'" % TODAY,
        f=dict(number="licencenumber", name="businessname", trade="businesstradename", status="status", issued="issueddate", expires="expireddate", kind="businesstype",
               unit="unit", house="house", street="street", city="city", prov="province", postal="postalcode", fee="feepaid"),
        payee="City of Vancouver", payee_address="Revenue Services, PO Box 7878, Vancouver, BC V6B 4E2", payee_site="https://vancouver.ca/",
        payee_url="https://vancouver.ca/doing-business/renew-your-business-licence.aspx", fee_quote="Your business licence expires on December 31 each year.",
        page="https://opendata.vancouver.ca/explore/dataset/business-licences/information/", list_name="the City of Vancouver's open data list of business licences", cities=("vancouver",)),
    "calgary": dict(
        kind="socrata", base="https://data.calgary.ca", dataset="vdjc-pybd", where="exp_dt >= '%sT00:00:00'" % TODAY,
        f=dict(number="getbusid", trade="tradename", status="jobstatusdesc", issued="first_iss_dt", expires="exp_dt", kind="licencetypes", addr="address"),
        payee="The City of Calgary", payee_address="PO Box 2100 Station M (#8108), Calgary, AB T2P 2M5", payee_site="https://www.calgary.ca/",
        payee_url="https://www.calgary.ca/for-business/changes-to-your-business.html", fee_quote="To remain active, business licences require an annual renewal payment.",
        page="https://data.calgary.ca/d/vdjc-pybd", list_name="The City of Calgary's open data list of business licences", cities=("calgary",)),
    "edmonton": dict(
        kind="socrata", base="https://data.edmonton.ca", dataset="qhi4-bdpu", where="expiry_date >= '%sT00:00:00'" % TODAY,
        f=dict(number="externalid", trade="business_name", issued="originalissuedate", expires="expiry_date", kind="business_licence_category", addr="business_address"),
        payee="City of Edmonton", payee_address="2nd Floor, Edmonton Tower, 10111 104 Avenue NW, Edmonton AB T5J 0J4", payee_site="https://www.edmonton.ca/",
        payee_url="https://edmonton.ca/business_economy/pay-licence-and-permit-fees", fee_quote="You must pay the fee in full when you apply or renew.",
        page="https://data.edmonton.ca/d/qhi4-bdpu", list_name="the City of Edmonton's open data list of business licences", cities=("edmonton",)),
    "toronto": dict(
        kind="ckan", base="https://ckan0.cf.opendata.inter.prod-toronto.ca", dataset="169e90ba-3ae0-43dd-8b2f-919e87002f50",
        f=dict(number="Licence No.", trade="Operating Name", name="Client Name", issued="Issued", cancel="Cancel Date", kind="Category", addr="Licence Address Line 1",
               city="Licence Address Line 2", postal="Licence Address Line 3", phone="Business Phone"),
        payee="City of Toronto", payee_address="Licence and Permit Issuing Office, 850 Coxwell Avenue, 3rd Floor, Toronto", payee_site="https://www.toronto.ca/",
        payee_url="https://www.toronto.ca/services-payments/permits-licences-bylaws/building-renovators",
        fee_quote="Your licence will expire annually on the anniversary of the date that the licence was first issued.",
        page="https://open.toronto.ca/dataset/municipal-licensing-and-standards-business-licences-and-permits/", list_name="the City of Toronto's open data list of business licences and permits",
        cities=("toronto", "north york", "scarborough", "etobicoke", "east york", "york")),
    "opc": dict(
        kind="ckan", base="https://www.donneesquebec.ca/recherche", dataset="c40c7af7-4a27-4272-be91-208994c67b7b",
        f=dict(number="NO_PERMIS", kind="CATEGORIE_PERMIS", name="NOM_COMMERCANT", neq="NEQ", unit="ETABLISSEMENT_APP", house="ETABLISSEMENT_NO", street="ETABLISSEMENT_RUE",
               postal="ETABLISSEMENT_CODE_POSTAL", city="ETABLISSEMENT_VILLE", prov="ETABLISSEMENT_PROVINCE", trade="AUTRES_NOMS"),
        payee="Office de la protection du consommateur", payee_address="400, boul. Jean-Lesage, bureau 450, Québec (Québec) G1K 8W4", payee_site="https://www.opc.gouv.qc.ca/",
        payee_url="https://cdn.opc.gouv.qc.ca/media/documents/commercant/permis-certificat/agence/AV_Guide_demande_permis.pdf",
        fee_quote="Un permis et tout duplicata du permis sont reconduits à la date d’anniversaire du permis",
        page="https://www.donneesquebec.ca/recherche/dataset/liste-des-permis-actifs", list_name="the Office de la protection du consommateur's open data list of permits in force", cities=()),
}
NCOLS = ["src", "number", "name", "trade", "status", "issued", "expires", "kind", "address", "city", "postal", "phone", "fee", "neq"]

# ---- registers described in files (2026-11-11) -------------------------------------------------------------------------------------------
# Owner, 2026-11-11: the lanes are "firms licensed by a Canadian regulator" and every other body that bills on invoice — "and more, don't limit
# yourself". A register is added by a descriptor file, not by an edit here: tools/data/registers/<key>.json (this lane) or
# contrib/<lane>/registers/<key>.json (any lane; contrib/** merges without review). The same keys as the entries of SOURCES above, plus:
#   kind      ods | socrata | ckan (as above) | csv (one file at "url"; "delimiter", "encoding" optional) | arcgis (a FeatureServer / MapServer
#             layer at "url": .../FeatureServer/0) | file (rows a lane harvested itself: "path", a glob under the repository, CSV or CSV.gz
#             whose columns are named in "f")
#   f         the register's column for each of: number, name (legal name), trade (trade / establishment name), status, issued, expires, kind,
#             addr (one-line street address) or unit / house / street, city, prov, postal, phone, fee, neq, cancel
#   payee, payee_address, payee_site, payee_url, payee_read, fee_quote   the body that is paid, its own printed address, the page that says
#             the holder pays it (a sentence of that page, at most 300 characters), the day that page was read
#   page, list_name       the register's own page and how to name it in a sentence ("the City of X's open data list of business licences")
#   cities                lower-case city names for the street-address match (empty: postal code and telephone only)
#   record_word           "Business licence" (default), "Liquor licence", "Permit", "Registration" …
#   persons_mixed         true when the register also lists natural persons: a record without a legal form in its legal name is left out
#   keep                  optional {column: [values]}: only records whose column has one of the values (e.g. {"status": ["Active"]})
# Natural persons are never delivered; a register's own e-mail column is never read (do not map it).
REG_DIRS = (os.path.join(ROOT, "tools/data/registers"), os.path.join(ROOT, "contrib/*/registers"))
NEED = ("kind", "f", "payee", "payee_address", "payee_url", "fee_quote", "page", "list_name")


def load_descriptors():
    n = 0
    for d in REG_DIRS:
        for f in sorted(glob.glob(os.path.join(d, "*.json"))):
            try:
                S = json.load(open(f, encoding="utf-8"))
            except ValueError as e:
                print("register descriptor not read (%s): %s" % (e, f), flush=True)
                continue
            key = S.get("key") or os.path.basename(f)[:-5]
            miss = [k for k in NEED if not S.get(k)]
            if miss or key in SOURCES or len(S.get("fee_quote") or "") > 300 or "email" in " ".join(str(v).lower() for v in (S.get("f") or {}).keys()):
                print("register descriptor left out (%s): %s" % ("missing " + ", ".join(miss) if miss else "key taken, a quote over 300 characters, or an e-mail column mapped", f), flush=True)
                continue
            S.setdefault("cities", []); S.setdefault("payee_site", ""); S["cities"] = tuple(c.lower() for c in S["cities"])
            if S.get("where"):
                S["where"] = S["where"].replace("{today}", TODAY)
            SOURCES[key] = S
            n += 1
    return n


def arcgis_rows(url):
    out, off = [], 0
    while True:
        res = jget("%s/query?where=1%%3D1&outFields=*&returnGeometry=false&f=json&resultOffset=%d&resultRecordCount=2000" % (url.rstrip("/"), off), timeout=300)
        feats = res.get("features") or []
        out += [f.get("attributes") or {} for f in feats]
        if len(feats) < 2000 and not res.get("exceededTransferLimit"):
            break
        off += len(feats) or 2000
        if off > 2_000_000:
            break
    return out


def file_rows(S):
    out = []
    for f in sorted(glob.glob(os.path.join(ROOT, S["path"]))):
        op = gzip.open if f.endswith(".gz") else open
        with op(f, "rt", encoding=S.get("encoding") or "utf-8-sig", errors="replace", newline="") as fh:
            out += list(csv.DictReader(fh, delimiter=S.get("delimiter") or ","))
    return out


def get(url, tries=4, timeout=180):
    err = None
    for i in range(tries):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept": "application/json, text/csv, */*"})
            with urllib.request.urlopen(req, timeout=timeout) as r:
                return r.read()
        except Exception as e:
            err = e
            if "HTTP Error 4" in str(e) or "Name or service" in str(e):
                break
            time.sleep(3 * (i + 1))
    raise err


def jget(url, **kw):
    return json.loads(get(url, **kw).decode("utf-8", "replace"))


def probe(a):
    want = re.compile(r"licen[cs]|permis|permit|business|commerc|entreprise|registr|établissement|etablissement|accredit", re.I)
    for name, kind, base in PORTALS:
        if a.only and name not in a.only.split(","):
            continue
        print("\n===== %s (%s) %s" % (name, kind, base), flush=True)
        seen = set()
        for q in QUERIES:
            try:
                if kind == "ods":
                    d = jget("%s/api/explore/v2.1/catalog/datasets?limit=20&where=%s" % (base, urllib.parse.quote('search("%s")' % q)))
                    for ds in d.get("results") or []:
                        did = ds.get("dataset_id")
                        meta = (ds.get("metas") or {}).get("default") or {}
                        if did in seen or not want.search("%s %s" % (did, meta.get("title"))):
                            continue
                        seen.add(did)
                        print("  [%s] %s | records %s | modified %s" % (did, meta.get("title"), meta.get("records_count"), meta.get("modified")), flush=True)
                        print("     fields: " + ", ".join("%s(%s)" % (f.get("name"), f.get("type")) for f in ds.get("fields") or []))
                        try:
                            for r in jget("%s/api/explore/v2.1/catalog/datasets/%s/records?limit=2" % (base, did)).get("results") or []:
                                print("     sample: " + json.dumps(r, ensure_ascii=False)[:700])
                        except Exception as e:
                            print("     (no sample: %s)" % e)
                elif kind == "socrata":
                    dom = urllib.parse.urlparse(base).netloc
                    d = jget("https://api.us.socrata.com/api/catalog/v1?domains=%s&search_context=%s&q=%s&limit=10" % (dom, dom, urllib.parse.quote(q)))
                    for res in d.get("results") or []:
                        r0 = res.get("resource") or {}
                        did = r0.get("id")
                        if did in seen or r0.get("type") not in ("dataset", "filter") or not want.search(r0.get("name") or ""):
                            continue
                        seen.add(did)
                        print("  [%s] %s | type %s | updated %s" % (did, r0.get("name"), r0.get("type"), r0.get("updatedAt")), flush=True)
                        print("     fields: " + ", ".join("%s(%s)" % (n, t) for n, t in zip(r0.get("columns_field_name") or [], r0.get("columns_datatype") or [])))
                        try:
                            print("     rows: %s" % json.dumps(jget("%s/resource/%s.json?$select=count(*)" % (base, did)))[:80])
                            for r in jget("%s/resource/%s.json?$limit=2" % (base, did)):
                                print("     sample: " + json.dumps(r, ensure_ascii=False)[:700])
                        except Exception as e:
                            print("     (no sample: %s)" % e)
                elif kind == "ckan":
                    d = jget("%s/api/3/action/package_search?q=%s&rows=10" % (base, urllib.parse.quote(q)))
                    for p in (d.get("result") or {}).get("results") or []:
                        if p.get("name") in seen or not want.search("%s %s" % (p.get("name"), p.get("title"))):
                            continue
                        seen.add(p.get("name"))
                        print("  [%s] %s | org %s | modified %s" % (p.get("name"), p.get("title"), (p.get("organization") or {}).get("title"), p.get("metadata_modified")), flush=True)
                        for r in (p.get("resources") or [])[:6]:
                            print("     resource %s | %s | %s | datastore %s | %s" % (r.get("id"), r.get("name"), r.get("format"), r.get("datastore_active"), (r.get("url") or "")[:140]))
                            if r.get("datastore_active"):
                                try:
                                    ds = jget("%s/api/3/action/datastore_search?resource_id=%s&limit=2" % (base, r.get("id")))["result"]
                                    print("       total %s | fields: %s" % (ds.get("total"), ", ".join("%s(%s)" % (f.get("id"), f.get("type")) for f in ds.get("fields") or [])))
                                    for rec in ds.get("records") or []:
                                        print("       sample: " + json.dumps(rec, ensure_ascii=False)[:700])
                                except Exception as e:
                                    print("       (no sample: %s)" % e)
            except Exception as e:
                print("  query %r failed: %s" % (q, str(e)[:160]), flush=True)
                if "Name or service" in str(e) or "HTTP Error 40" in str(e):
                    break


def norm(s):
    return re.sub(r"[^a-z0-9]+", " ", unicodedata.normalize("NFKD", s or "").encode("ascii", "ignore").decode().lower()).strip()


LEGAL_FORM = re.compile(r"\b(inc|incorporated|ltd|limited|ltee|limitee|corp|corporation|co|company|compagnie|ulc|llp|llc|lp|senc|s e n c|societe|society|association|assn|foundation|"
                        r"fondation|club|church|eglise|trust|fiducie|cooperative|coop|co-op|partnership|holdings|group|groupe|enterprises|entreprises|services|canada|ontario|quebec|"
                        r"university|college|school|hospital|centre|center|institute|institut|council|board|bank|banque|authority|agency|agence|\d{4} \d{4} quebec|\d{6,} (?:ontario|canada|alberta|b c))\b")


def pull(a):
    os.makedirs("out", exist_ok=True)
    for src, S in SOURCES.items():
        if a.only and src not in a.only.split(","):
            continue
        t0, rows = time.time(), []
        try:
            if S["kind"] == "ods":
                url = "%s/api/explore/v2.1/catalog/datasets/%s/exports/csv?delimiter=%%2C&lang=en&where=%s" % (S["base"], S["dataset"], urllib.parse.quote(S["where"]))
                rows = list(csv.DictReader(io.StringIO(get(url, timeout=900).decode("utf-8-sig", "replace"))))
            elif S["kind"] == "socrata":
                off = 0
                while True:
                    part = jget("%s/resource/%s.json?$limit=50000&$offset=%d&$order=:id&$where=%s" % (S["base"], S["dataset"], off, urllib.parse.quote(S["where"])), timeout=600)
                    rows += part
                    if len(part) < 50000:
                        break
                    off += 50000
            elif S["kind"] == "ckan":
                off = 0
                while True:
                    res = jget("%s/api/3/action/datastore_search?resource_id=%s&limit=32000&offset=%d" % (S["base"], S["dataset"], off), timeout=600)["result"]
                    rows += res.get("records") or []
                    if len(res.get("records") or []) < 32000:
                        break
                    off += 32000
            elif S["kind"] == "csv":
                rows = list(csv.DictReader(io.StringIO(get(S["url"], timeout=900).decode(S.get("encoding") or "utf-8-sig", "replace")), delimiter=S.get("delimiter") or ","))
            elif S["kind"] == "arcgis":
                rows = arcgis_rows(S["url"])
            elif S["kind"] == "file":
                rows = file_rows(S)
        except Exception as e:
            print("%s: download failed: %s" % (src, str(e)[:200]), flush=True)
            continue
        F, out, stats = S["f"], [], collections.Counter()
        g = lambda r, k: ("" if F.get(k) is None or r.get(F[k]) is None else str(r.get(F[k])).strip())
        for r in rows:
            name, trade = g(r, "name"), g(r, "trade")
            if g(r, "cancel"):
                stats["cancelled (left out)"] += 1
                continue
            if "exemption" in norm(g(r, "kind")):
                stats["exemption, not a permit (left out)"] += 1
                continue
            if any(str(r.get(c) or "").strip() not in vals for c, vals in (S.get("keep") or {}).items()):
                stats["not in force by the register's own status column (left out)"] += 1
                continue
            if name.startswith("(") or (name and (src in ("toronto",) or S.get("persons_mixed")) and not LEGAL_FORM.search(norm(name))):
                stats["licensee is a natural person or has no legal form in its name (left out)"] += 1
                continue
            addr = g(r, "addr") or " ".join(x for x in ((g(r, "unit") + "-") if g(r, "unit") else "", g(r, "house"), g(r, "street")) if x).replace("- ", "-")
            if addr.startswith("<"):
                addr = ""  # "<Home Based Business>", "<Non-Resident Business>"
            city = re.sub(r",.*$", "", g(r, "city")).strip() or (S["cities"][0].title() if len(S["cities"]) == 1 else "")
            o = dict(src=src, number=g(r, "number"), name=name, trade=re.sub(r"\s*//\s*", " | ", trade), status=g(r, "status"), issued=g(r, "issued")[:10], expires=g(r, "expires")[:10],
                     kind=g(r, "kind")[:120], address=addr, city=city, postal=re.sub(r"\s+", "", g(r, "postal").upper()), phone=re.sub(r"\D", "", g(r, "phone"))[-10:], fee=g(r, "fee"), neq=g(r, "neq"))
            if not (o["name"] or o["trade"]) or not o["number"]:
                stats["no name or no number"] += 1
                continue
            out.append(o)
        with gzip.open("out/licences_%s.csv.gz" % src, "wt", encoding="utf-8", newline="") as f:
            w = csv.DictWriter(f, fieldnames=NCOLS)
            w.writeheader()
            w.writerows(out)
        print("%s: %d records downloaded, %d kept (%.0f s); left out: %s; with postal code %d, with street address %d, with telephone %d; status %s; kinds %s" % (
            src, len(rows), len(out), time.time() - t0, dict(stats), sum(1 for o in out if len(o["postal"]) == 6), sum(1 for o in out if o["address"]), sum(1 for o in out if len(o["phone"]) == 10),
            dict(collections.Counter(o["status"] for o in out).most_common(5)), dict(collections.Counter(o["kind"] for o in out).most_common(6))), flush=True)


PC = re.compile(r"(?<![A-Za-z0-9])([ABCEGHJ-NPRSTVXY]\d[ABCEGHJ-NPRSTV-Z])\s?(\d[ABCEGHJ-NPRSTV-Z]\d)(?![A-Za-z0-9])")
# legal-form words: ignored. generic words: they count for "every word of the shorter name is in the longer one", never as the one word that identifies
STOP = set("inc ltd ltee limited corp corporation co company the and of de la le les du des et a l d llp llc lp enr senc dba".split())
GENERIC = set("""enterprises entreprises holdings group groupe services service canada canadian bc ab on qc british columbia alberta ontario quebec vancouver toronto calgary
edmonton winnipeg ottawa montreal north south east west downtown main street avenue road park city centre center plaza place mall village pacific coast western
restaurant cafe coffee bar grill pub bistro kitchen pizza sushi bakery deli foods food market grocery store shop boutique salon spa studio gallery art arts design
dental dentistry medical clinic health wellness pharmacy physiotherapy chiropractic optometry vision eye care fitness yoga gym dance music school academy college
society association foundation church club community consulting consultants management properties property realty investments development developments
construction contracting plumbing heating electric electrical mechanical roofing painting landscaping cleaning auto automotive motors cycle hotel inn suites
law legal lawyers accounting accountants financial insurance travel tours rentals rental trading international solutions systems technologies technology
media productions studios photography print printing sign signs supply supplies equipment furniture flowers florist jewellery jewelry fashion clothing
first new old best royal golden green blue red black white big little one two voyages voyage agence garage automobiles autos""".split())


def toks(s):
    return {t for t in norm(s).split() if len(t) >= 2 and t not in STOP}


def names_agree(a, b):
    """Every word of the shorter name is in the longer one, and what agrees identifies: three words or more, or one word that is not a generic trade / place word."""
    ta, tb = toks(a), toks(b)
    if not ta or not tb:
        return False
    short, long_ = (ta, tb) if len(ta) <= len(tb) else (tb, ta)
    if not short <= long_:
        return False
    return len(short) >= 3 or any(t not in GENERIC and len(t) >= 3 and not t.isdigit() for t in short)


FORMAL = set("applied governing council board governors trustees regents institution learning advancement incorporated operating division branch location head office "
             "high elementary secondary middle junior senior campus main".split())


PUBLIC_BODY = set("ville city town township municipalite municipality village canton paroisse parish county comte district region regional mrc universite university "
                  "college cegep ecole school commission hopital hospital eglise church fabrique diocese ministere ministry gouvernement government bibliotheque library "
                  "chambre chamber".split())


def agree_asym(org, lic):
    """The organisation's name against a name in a licence list. The licence name may be part of the organisation's name; when the licence name
    has MORE words, they must all be generic or formal ones — 'ARAMARK CANADA (UNIVERSITY OF CALGARY)', 'SODEXO - BOW VALLEY COLLEGE' and
    'BUCO EPCOR TOWER' are other parties at the organisation's address (first real run, 2026-11-10)."""
    to, tl = toks(org), toks(lic)
    if not to or not tl:
        return False
    ident = lambda ts: len(ts) >= 3 or any(t not in GENERIC and t not in FORMAL and len(t) >= 3 and not t.isdigit() for t in ts)
    if tl <= to:
        # 2026-11-11, first match of the Québec liquor register: the Ville d'Estérel was tied to the permit of "Estérel Inc." (a resort at the same
        # postal code). A public body, a school or a parish that carries a place's name is not the company named after the place.
        if (to - tl) & PUBLIC_BODY:
            return False
        return ident(tl)
    if to <= tl:
        return all(t in GENERIC or t in FORMAL for t in tl - to) and ident(to)
    return False


def lic_agrees(org_names, r):
    """a licence with a named legal licensee belongs to that licensee: the organisation must be it (a cafeteria licensed to Compass Group under
    the hospital's name is Compass Group's). A numbered company, or no legal name in the list: the trade name decides."""
    legal = r["name"]
    trades = [t for t in r["trade"].split(" | ") if t.strip()]
    cands = [legal] if legal and not re.match(r"\d[\d\s-]{5,}", legal) else (trades or ([legal] if legal else []))
    return any(agree_asym(n, x) for n in org_names for x in cands)


STREET_TYPE = set("st street av ave avenue rd road dr drive blvd boulevard boul way wy trail tr crescent cres cr place pl court ct lane ln gate ga highway hwy rue chemin ch rang route rte "
                  "terrace close cl square sq circle ci green gr hill hl mews link li parade pr rise ri view vw bay ba common cm cove cv heights ht manor mr landing ld passage pa "
                  "point pt villas vi walk wk garden gardens grove gv park pk row plaza pz".split())
QUAD = set("nw ne sw se n s e w".split())
UNIT = re.compile(r"(?i)(?:\b(?:suite|ste|unit|unité|unite|bureau|local|app|apt)\.?\s*#?\s*[\w-]+\s*,?\s*)|(?:#\s*[\w-]+\s*,?\s*)")


PARTICLES = set("de du des la le les l d of the".split())


def street_key(addr):
    """('5565', '56') from '5565 56 AV SE' / '#203, 5565 - 56th Avenue S.E., Calgary' — house number + the first word of the street name (ordinal suffix dropped)"""
    s = UNIT.sub(" ", addr or "")
    m0 = re.match(r"\s*#?(\d+[a-z]?)\s*-\s*(\d+[a-z]?)\s+([A-Za-zÀ-ÿ.]+)", s)
    if m0 and norm(m0.group(3)) not in STREET_TYPE:  # "1-800 Main St" is unit 1 of number 800; "10123-99 Street" is number 10123 on 99 Street
        s = s[m0.start(2):]
    t = norm(s)
    m = re.match(r"(?:(\d+[a-z]?) (?=\d+[a-z]? \d))?(\d{1,6})[a-z]? (.*)", t)  # an optional unit number in front of house + numbered street: "203 5565 56 av"
    if not m:
        return None
    house, rest = m.group(2), [w for w in m.group(3).split() if w not in QUAD]
    while len(rest) > 1 and (rest[0] in STREET_TYPE or rest[0] in PARTICLES):  # "rue de l'Église": the type and the particles come first in French
        rest = rest[1:]
    if not rest:
        return None
    w = re.sub(r"(?<=\d)(st|nd|rd|th|e|er|ere|ieme)$", "", rest[0])
    return (house, w) if w and w not in STREET_TYPE and w not in PARTICLES else None


def org_universe():
    """the organisations we hold that print an address or a telephone of their own: {host: names, addr, addr_url, phone, tier, mail} — the delivered
    rows (name, legal name, address, telephone, site), then the site facts of leads not delivered yet (tools/lead_crawl.py)"""
    import ranked_io
    orgs = {}
    for r in ranked_io.rows():
        host = (urllib.parse.urlparse(r.get("buyer_website") or "").hostname or "").lower()
        if not host or not (r.get("buyer_address") or r.get("buyer_phone")):
            continue
        names = [n for n in (r.get("buyer") or "", (r.get("buyer_legal_name_as_published") or "").split(" (")[0], (r.get("buyer_trade_name_as_published") or "").split(" (")[0]) if n and "." not in n[-5:]]
        _u = re.search(r"\(as printed on (https?://[^\s,)]+)", r.get("buyer_address") or "")
        orgs[host] = dict(names=names, addr=(r.get("buyer_address") or "").split(" (as printed")[0], addr_url=_u.group(1) if _u else "",
                          phone=re.sub(r"\D", "", (r.get("buyer_phone") or "").split(" (")[0])[-10:], tier=r.get("tier") or "", mail=bool((r.get("email") or "").strip()))
    import lead_crawl as LCF
    for o in LCF.facts_records():  # the single facts file of before 2026-11-10 and the shards of site_facts/
        host = (urllib.parse.urlparse(o.get("site") or "").hostname or "").lower()
        if host and host not in orgs and o.get("site_name") and o.get("address_quote"):
            orgs[host] = dict(names=[o["site_name"]], addr=o.get("address") or o["address_quote"], addr_url=o.get("address_url") or "", phone="", tier="", mail=False)
    return orgs


def match(a):
    import ranked_io
    os.makedirs("out", exist_ok=True)
    by_pc, by_ph, by_st = collections.defaultdict(list), collections.defaultdict(list), collections.defaultdict(list)
    n_lic = collections.Counter()
    for f in sorted(glob.glob(os.path.join(a.dir, "licences_*.csv.gz"))):
        with gzip.open(f, "rt", encoding="utf-8", newline="") as fh:
            for r in csv.DictReader(fh):
                n_lic[r["src"]] += 1
                if len(r["postal"]) == 6:
                    by_pc[r["postal"]].append(r)
                if len(r["phone"]) == 10:
                    by_ph[r["phone"]].append(r)
                sk = street_key(r["address"])
                if sk and r["city"]:
                    by_st[(norm(r["city"]),) + sk].append(r)
    orgs = org_universe()
    n_univ = len(orgs)
    try:
        # 2026-11-11: the delivered table no longer carries the .ca organisations as rows (owner: a registrar in between is not a row); they are
        # the pool a register is matched against. Every site on file that states a Canadian postal code — the home-page scan's name facts, the
        # lead readers' facts — joins the universe with the names it states for itself; the tie stays the same (same postal code AND names agree).
        import tm_register as TM
        for dom, names, pc, where in TM.site_index():
            host = dom.lower()
            if not pc or host in orgs or ("www." + host) in orgs:
                continue
            nm = [n for n in (names.get("legalName") or "", names.get("copyright line") or "", names.get("site name") or "") if n and "." not in n[-5:]]
            if nm:
                orgs[host] = dict(names=nm, addr="%s %s" % (pc[:3], pc[3:]), addr_url="", phone="", tier="", mail=False)
    except Exception as e:
        print("the scan's name facts were not read (%s): the universe is the delivered rows and the lead readers' facts" % e, flush=True)
    print("organisations a register can be tied to: %d (delivered rows and lead readers' facts: %d)" % (len(orgs), n_univ), flush=True)
    all_cities = {c for S in SOURCES.values() for c in S["cities"]}
    out, stats = [], collections.Counter()
    for host, O in orgs.items():
        if not O["names"]:
            continue
        cands, how = [], {}
        m = PC.search(O["addr"].upper())
        pc = (m.group(1) + m.group(2)) if m else ""
        for r in by_pc.get(pc, []) if pc else []:
            cands.append(r); how[id(r)] = "same postal code %s %s" % (pc[:3], pc[3:])
        for r in by_ph.get(O["phone"], []) if len(O["phone"]) == 10 else []:
            if id(r) not in how:
                cands.append(r); how[id(r)] = "same telephone number"
            else:
                how[id(r)] += " and telephone number"
        sk = street_key(O["addr"])
        if sk:
            na = norm(O["addr"])
            for city in all_cities:
                if re.search(r"\b%s\b" % re.escape(city), na):
                    for r in by_st.get((city,) + sk, []):
                        if id(r) not in how:
                            cands.append(r); how[id(r)] = "same street number and street (%s %s, %s)" % (sk[0], sk[1], city.title())
        if not cands:
            continue
        stats["organisations with a licence at their postal code / telephone / street address"] += 1
        hits = [r for r in cands if lic_agrees(O["names"], r)]
        if not hits:
            continue
        if len({norm(r["name"]) or norm(r["trade"]) for r in hits}) > 1:
            stats["several different licensees fit (dropped)"] += 1
            continue
        best = sorted(hits, key=lambda r: (r["expires"] or "", r["issued"] or ""), reverse=True)[0]
        stats["matched"] += 1
        stats["matched: %s" % best["src"]] += 1
        stats["matched, row tier %s" % (O["tier"] or "(not delivered yet)")] += 1
        # the name of the organisation that agreed with the licence comes first: it names the lead (first RACJ match, 2026-11-11: a site whose first
        # stated "name" was its copyright line's "TOUS DROITS RÉSERVÉS" was tied by its second name, and would have been delivered under the first)
        _lc = [best["name"]] if best["name"] and not re.match(r"\d[\d\s-]{5,}", best["name"]) else ([t for t in best["trade"].split(" | ") if t.strip()] or [best["name"]])
        _ag = [n for n in O["names"] if any(agree_asym(n, x) for x in _lc if x)]
        O = dict(O, names=_ag + [n for n in O["names"] if n not in _ag])
        out.append(dict(host=host, org_names=O["names"][:3], org_address=O["addr"][:200], basis="%s; names agree (%s ~ %s)" % (how[id(best)], O["names"][0][:60], (best["trade"] or best["name"])[:60]),
                        licences_of_this_licensee=len(hits), lic=best))
    with open("out/licence_leads.jsonl", "w", encoding="utf-8") as f:
        for o in out:
            f.write(json.dumps(o, ensure_ascii=False) + "\n")
    print("licences in force read: %s; organisations with an address or telephone: %d; %s" % (dict(n_lic), len(orgs), dict(sorted(stats.items()))), flush=True)
    for o in out[:25]:
        b = o["lic"]
        print("  %s | %s  <->  %s / %s | %s %s | %s → %s | %s" % (o["host"], o["org_names"][0][:40], b["trade"][:40], b["name"][:40], b["src"], b["number"], b["issued"], b["expires"], o["basis"][:90]))


def lead_of(o):
    b = o["lic"]
    S = SOURCES[b["src"]]
    key = "lead:" + hashlib.sha1(("lic|%s|%s" % (b["src"], b["number"])).encode()).hexdigest()[:16]
    trade = [t for t in b["trade"].split(" | ") if t.strip()]
    legal = b["name"] if b["name"] and LEGAL_FORM.search(norm(b["name"])) else ""
    numbered = bool(re.match(r"\d[\d\s-]{5,}", legal))  # a numbered company is known by its other name
    # the row keeps the organisation's own name (its site, the delivered row); the licence's legal and trade names go to the register facts below
    row = {"buyer_key": key, "buyer_name": (o.get("org_names") or [""])[0] or (trade[0] if trade and (not legal or numbered) else legal or b["name"]), "website": "https://%s/" % o["host"],
           "canadian_vendor_rows": 1, "example_vendor": S["payee"],
           "canada_field_value": "membership / statutory fee relationship: licence holder of the Canadian body (%s)=%s (as printed on %s, read %s); %s: “%s” (%s)"
                                 % (S["payee"], S["payee_address"], S["payee_url"], S.get("payee_read") or "2026-11-10", S["payee"], S["fee_quote"], S["payee_url"]),
           "evidence_dataset": S["page"], "latest_record_date": TODAY}
    addr = ", ".join(x for x in (b["address"], b["city"], (b["postal"][:3] + " " + b["postal"][3:]) if len(b["postal"]) == 6 else "") if x)
    det = {"key": key, "platform": "biz_licence", "record_url": S["page"], "vendor": S["payee"], "record_date": TODAY, "start": b["issued"], "end": b["expires"], "reference": b["number"],
           "title": "%s %s — %s%s" % (S.get("record_word") or ("Permit" if b["src"] == "opc" else "Business licence"), b["number"], b["kind"] or "category not stated", (" (%s)" % b["status"]) if b["status"] else ""),
           "vendor_address": "%s (as printed on %s)" % (S["payee_address"], S["payee_url"]), "vendor_site": S.get("payee_site") or "",
           "member_address_quote": addr, "register_label": "the public list of licences published by",
           "buyer_register": {"legal_name": legal, "trade_names": trade[:4], "registry_id": ("NEQ %s" % b["neq"]) if len(b.get("neq") or "") == 10 else "",
                              "phone": ("%s-%s-%s" % (b["phone"][:3], b["phone"][3:6], b["phone"][6:])) if len(b["phone"]) == 10 else "",
                              "label": "%s, %s, read %s" % (S["list_name"], S["page"], TODAY)},
           "licence_first_issued": b["issued"], "licence_in_force_until": b["expires"], "licence_issued_by": S["payee"], "licence_type": b["kind"],
           "fee_basis": "%s (%s)" % (S["fee_quote"], S["payee_url"]), "site_tied_to_holder_by": o["basis"], "licences_of_this_licensee_in_the_list": o["licences_of_this_licensee"]}
    try:
        if b["fee"] and float(b["fee"]) > 0:
            det.update(value="%.2f" % float(b["fee"]), currency="CAD", value_field="feepaid (licence fee paid, as the city's list states it)")
    except ValueError:
        pass
    return row, det


LDIR = os.path.join(INC, "licences")
ADDR = os.path.join(INC, "overture", "lic_addr_candidates.csv")  # tools/overture_names.py addr --lanes lic
ADONE = os.path.join(LDIR, "addr_done.tsv")


def addr_sites(a):
    """2026-11-13: licensees (organisations) that no organisation on file matched: the websites an Overture Maps place at the licence's own
    postal code lists. The lane's own rule decides, read on the site's own pages: the names agree (the licence's legal or trade name and the
    site's own name, title or copyright line) AND the site prints the licence's postal code, telephone or street number and street.
    -> out/licence_leads_addr.jsonl (the records `merge` reads), out/lic_addr_done.tsv"""
    import ap_crawler as C
    import lead_crawl as LC
    import tech_relationships as T
    from concurrent.futures import ThreadPoolExecutor
    import threading
    os.makedirs("out", exist_ok=True)
    os.makedirs(C.STATE, exist_ok=True)
    C.HOST_INTERVAL = 0.6
    if not os.path.exists(ADDR):
        print("no candidates (tools/overture_names.py addr --lanes lic)", flush=True)
        return
    lic = {}
    for f in sorted(glob.glob(os.path.join(a.dir, "licences_*.csv.gz"))):
        with gzip.open(f, "rt", encoding="utf-8", newline="") as fh:
            for r in csv.DictReader(fh):
                lic["%s:%s" % (r["src"], r["number"])] = r
    have = set()
    for p_ in glob.glob(os.path.join(SHARDS, "leads_lic_*.gz")):
        with gzip.open(p_, "rt", encoding="utf-8", newline="") as fh:
            have |= {r["buyer_key"] for r in csv.DictReader(fh)}
    done = {l.split("\t")[0] for l in open(ADONE, encoding="utf-8")} if os.path.exists(ADONE) else set()
    cand = collections.defaultdict(list)
    for r in csv.DictReader(open(ADDR, encoding="utf-8", newline="")):
        k = r["key"]
        if k in lic and k not in done and ("lead:" + hashlib.sha1(("lic|%s|%s" % tuple(k.split(":", 1))).encode()).hexdigest()[:16]) not in have:
            cand[k].append(r)
    todo = sorted(cand)
    if a.limit:
        todo = todo[:a.limit]
    print("licensees with a place at their own postal code that lists a website: %d" % len(todo), flush=True)
    deadline = time.time() + a.minutes * 60
    lock, stats = threading.Lock(), collections.Counter()
    fo = open("out/licence_leads_addr.jsonl", "a", encoding="utf-8")
    fd = open("out/lic_addr_done.tsv", "a", encoding="utf-8")

    def page(url):
        if not C.allowed(url):
            return "", url
        st, ct, data, final = C.fetch(url, 1_500_000)
        if st != 200 or not data:
            return "", final
        return data.decode("utf-8", "replace"), final

    def one(k):
        if time.time() > deadline:
            return
        r = lic[k]
        got = ""
        for c in cand[k]:
            dom = c["site"]
            try:
                raw, final = page("https://%s/" % dom)
                if not raw:
                    continue
                fhost = (urllib.parse.urlparse(final).hostname or dom).lower()
                title, meta = T.page_meta(raw)
                sn = LC.site_name_for(fhost, meta.get("og:site_name"), title, T) or ""
                text = C.visible(raw)
                cp = re.search(r"(?:©|&copy;|copyright)\s*(?:\d{4}\s*[-–]?\s*\d{0,4})?\s*([^|.\n]{3,80})", text, re.I)
                names = [x for x in (sn, title, cp.group(1).strip() if cp else "") if x]
                if not names or not lic_agrees(names, r):
                    continue
                pages = [text]
                for link, label in C.links(raw, final):
                    p_ = urllib.parse.urlparse(link)
                    if (p_.scheme in ("http", "https") and C.registrable((p_.hostname or "").lower()) == C.registrable(fhost)
                            and re.search(r"contact|joindre|nous-joindre|coordonn|about|propos", p_.path + " " + label, re.I)):
                        r2, f2 = page(link.split("#")[0])
                        if r2:
                            pages.append(C.visible(r2))
                        break
                proof = ""
                for t in pages:
                    if len(r["postal"]) == 6 and re.search(r"(?<![A-Za-z0-9])%s\s?%s(?![A-Za-z0-9])" % (r["postal"][:3], r["postal"][3:]), t, re.I):
                        proof = "the licence's postal code %s %s" % (r["postal"][:3], r["postal"][3:]); break
                    if len(r["phone"]) == 10 and re.search(r"(?<!\d)\(?%s\)?[\s.\-]{0,3}%s[\s.\-]{0,3}%s(?!\d)" % (r["phone"][:3], r["phone"][3:6], r["phone"][6:]), t):
                        proof = "the licence's telephone number"; break
                    sk = street_key(r["address"])
                    if sk and re.search(r"(?<![\d-])%s[A-Za-z]?\s+%s\b" % (re.escape(sk[0]), re.escape(sk[1])), norm(t)):
                        proof = "the licence's street number and street (%s %s)" % sk; break
                if not proof:
                    continue
                o = dict(host=fhost[4:] if fhost.startswith("www.") else fhost, org_names=names[:3], org_address=(r["address"] + ", " + r["city"])[:200],
                         basis="an Overture Maps place at the licence's own postal code lists this website (“%s”, place %s, release %s); its own pages print %s; names agree (%s ~ %s)" % (
                             c["place_name"], c["place_id"], c["release"], proof, names[0][:60], (r["trade"] or r["name"])[:60]),
                         licences_of_this_licensee=1, lic=r)
                with lock:
                    fo.write(json.dumps(o, ensure_ascii=False) + "\n")
                got = dom
                break
            except Exception:
                continue
        with lock:
            fd.write("%s\t%s\n" % (k, got))
            stats["asked"] += 1
            stats["tied"] += bool(got)
            stats["tied: %s" % r["src"]] += bool(got)
            if stats["asked"] % 500 == 0:
                fo.flush(); fd.flush()
                print(time.strftime("%H:%M:%S"), dict(stats), flush=True)
    with ThreadPoolExecutor(a.workers) as ex:
        list(ex.map(one, todo))
    fo.close(); fd.close()
    print("addr: %s" % dict(stats), flush=True)


def merge(a):
    os.makedirs(SHARDS, exist_ok=True)
    os.makedirs(LDIR, exist_ok=True)
    _ad = os.path.join(a.dir, "lic_addr_done.tsv")
    if os.path.exists(_ad):  # 2026-11-13: licensees asked with the places at their own postal code
        _old = set(open(ADONE, encoding="utf-8").read().splitlines()) if os.path.exists(ADONE) else set()
        with open(ADONE, "a", encoding="utf-8") as _f:
            for l in open(_ad, encoding="utf-8").read().splitlines():
                if l and l not in _old:
                    _f.write(l + "\n"); _old.add(l)
    stamp = a.stamp or time.strftime("%Y%m%dT%H%M%S", time.gmtime())
    have = set()
    for p in glob.glob(os.path.join(SHARDS, "leads_lic_*.gz")):
        with gzip.open(p, "rt", encoding="utf-8", newline="") as fh:
            have |= {r["buyer_key"] for r in csv.DictReader(fh)}
    n0, rows, dets, by = len(have), [], [], collections.Counter()
    for f in sorted(glob.glob(os.path.join(a.dir, "licence_leads*.jsonl"))):
        for l in open(f, encoding="utf-8"):
            try:
                o = json.loads(l)
                row, det = lead_of(o)
            except (ValueError, KeyError):
                continue
            if row["buyer_key"] in have:
                continue
            have.add(row["buyer_key"])
            rows.append(row); dets.append(det); by[o["lic"]["src"]] += 1
    if rows:
        with gzip.open(os.path.join(SHARDS, "leads_lic_%s.gz" % stamp), "wt", encoding="utf-8", newline="") as fh:
            w = csv.DictWriter(fh, fieldnames=LEAD_COLS)
            w.writeheader()
            w.writerows(rows)
        with gzip.open(os.path.join(SHARDS, "details_lic_%s.gz" % stamp), "wt", encoding="utf-8") as fh:
            for d in dets:
                fh.write(json.dumps(d, ensure_ascii=False) + "\n")
    print("business licences / permits tied to organisations: %d on file (+%d this run: %s)" % (len(have), len(have) - n0, dict(by)))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("cmd", choices=["probe", "pull", "match", "merge", "addr-sites"])
    ap.add_argument("dir", nargs="?", default="out")
    ap.add_argument("--only", default="")
    ap.add_argument("--stamp", default="")
    ap.add_argument("--minutes", type=float, default=40)
    ap.add_argument("--workers", type=int, default=30)
    ap.add_argument("--limit", type=int, default=0)
    a = ap.parse_args()
    n = load_descriptors()
    if n:
        print("registers described in files: %d (%s)" % (n, ", ".join(k for k, S in SOURCES.items() if S.get("payee_read") or S["kind"] in ("csv", "arcgis", "file"))), flush=True)
    {"probe": probe, "pull": pull, "match": match, "merge": merge, "addr-sites": addr_sites}[a.cmd](a)


if __name__ == "__main__":
    main()
