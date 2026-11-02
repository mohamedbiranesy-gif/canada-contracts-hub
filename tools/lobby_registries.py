#!/usr/bin/env python3
"""Buyers that pay a consultant lobbyist located in Canada, from public lobbyist registries' open data. No AI.

A consultant lobbyist is, by the registries' own legal definition, paid by its client to lobby on the client's behalf
(City of Toronto Municipal Code ch. 140; BC Lobbyists Transparency Act). Each consultant registration is therefore a
public record of a paid engagement that names the client organisation (buyer), the lobbying firm (vendor) with the
firm's business address, and the engagement dates. In-house and voluntary registrations (the lobbyist is the client's
own employee / unpaid) are skipped.

Sources (both open data, no login, no CAPTCHA; each bulk file downloaded once per run-day into ~/cch-sources/lobby/):
  toronto  City of Toronto Lobbyist Registry, CKAN package `lobbyist-registry`, resource "Lobbyist Registry Activity"
           https://ckan0.cf.opendata.inter.prod-toronto.ca/api/3/action/package_show?id=lobbyist-registry
           -> lobbyactivity.zip (lobbyactivity-active.xml + lobbyactivity-closed.xml, refreshed daily).
           Record = ROWSET/ROW/SMXML/SM (subject-matter registration), kept when SM/Type == 'Consultant'.
           Buyer   = Beneficiaries/BENEFICIARY[Type='Client']/Name (TradeName when Name is a person and the trade name
                     is an organisation). Parent / subsidiary / other beneficiaries are kept in row only.
           Vendor  = Firms/Firm/Name; Canada proof = Firms/Firm/BusinessAddress/Country in (Canada, CA, CAN), address
                     text = AddressLine1, AddressLine2, City, Province, Country, PostalCode joined with ", ".
           Dates   = record_date = max(InitialApprovalDate, EffectiveDate) (registration start / last amendment);
                     end = ProposedEndDate (used as a published end only while Status == 'Active').
           Public per-record search https://secure.toronto.ca/lobbyistsearch/ answers 403 (cloud and Mac), so the
           dataset_url is the open-data zip that holds the SMNumber.
  bc       Office of the Registrar of Lobbyists for British Columbia, open dataset (weekly):
           https://www.lobbyistsregistrar.bc.ca/app/secure/orl/lrs/do/mssDtstRprt?file=ORL_Registration_Data.zip
           -> Registration_Primary_Export.csv. Kept: REG_TYPE == 'Cons', latest version of each registration chain
           (REG_ID not referenced by any PREVIOUS_VERSION_REG_ID).
           Buyer   = CLIENT_ORG_NAME, website CLIENT_ORG_WEB_ADDRESS.
           Vendor  = FIRM_NAME with FIRM_ADDRESS ("..., CAN"); sole consultants without a firm (FIRM_NAME 'null'):
                     the consultant (FILER_FIRST_NAME FILER_LAST_NAME) with FILER_ADDRESS (row.vendor_is_individual).
           Dates   = record_date = REG_START_DATE of the latest version (= last update / renewal); first_start_date =
                     REG_START_DATE of the first version; end = REG_END_DATE, else REG_PROJECTED_END_DATE.
           Public page per record: https://www.lobbyistsregistrar.bc.ca/app/secure/orl/lrs/do/vwRg?cno=<CLIENT_ORG_NUM>&regId=<REG_ID without R->

Filters (both): vendor address country must be Canada (from the source field, never the name); the client must be a
named organisation: clients that look like a person (no organisation word, no digit, 2-4 name tokens, first token is a
first name, or the last a surname, seen among the
registries' own lobbyists; or a Mr/Mrs/Dr title) are dropped; client == firm (self) dropped. Window: record_date
>= today-3y, or (still active and published end >= today). One line per (buyer, vendor) pair, most recent record kept.
Buyer website: the source's (BC), else Wikidata (exact label/alias = name, official website P856, item in Canada/US or
a domain that spells the name; 1 request/second; cached in ~/cch-sources/lobby/wikidata_cache.json).

Other registries tested from the Mac on 2026-11-02 (normal curl GET, our User-Agent): see notes in BLOCKED below.

Counts seen 2026-11-02: Toronto active file 2,110 SM (705 consultant), closed 12,505 (6,574 consultant);
BC 27,257 registrations, 6,679 latest versions, 4,868 consultant latest versions. Output counts: printed at the end.

Output: ~/cch-leads/socrata_lobby.jsonl (overwritten), platform 'lobby', row.registry = 'toronto' | 'bc'.
    python3 tools/lobby_registries.py [--no-wikidata] [--today YYYY-MM-DD]
"""
import argparse, csv, datetime, io, json, os, re, sys, time, unicodedata, urllib.error, urllib.parse, urllib.request, zipfile
import xml.etree.ElementTree as ET

UA = "canada-contracts-hub-crawler/1.0 (+https://github.com/mohamedbiranesy-gif/canada-contracts-hub)"
CACHE = os.path.expanduser("~/cch-sources/lobby")
OUT = os.path.expanduser("~/cch-leads/socrata_lobby.jsonl")
TOR_PKG = "https://ckan0.cf.opendata.inter.prod-toronto.ca/api/3/action/package_show?id=lobbyist-registry"
TOR_PAGE = "https://open.toronto.ca/dataset/lobbyist-registry/"
BC_ZIP = "https://www.lobbyistsregistrar.bc.ca/app/secure/orl/lrs/do/mssDtstRprt?file=ORL_Registration_Data.zip"
BC_VIEW = "https://www.lobbyistsregistrar.bc.ca/app/secure/orl/lrs/do/vwRg?cno=%s&regId=%s"
WD_API = "https://www.wikidata.org/w/api.php?"
BLOCKED = {  # tested from the Mac 2026-11-02 (curl GET, our UA); skipped (rule: no getting around blocks) or no bulk data
    "toronto public search secure.toronto.ca/lobbyistsearch": "403 (open-data zip used instead)",
    "federal OCL lobbycanada.gc.ca registrations zip": "Cloudflare challenge (known)",
    "quebec carrefourlobby.quebec": "403 (known)",
    "ontario lobbyist.oico.on.ca": "redirects to Pages/Public/Login.aspx; no bulk file; data.ontario.ca has no lobbyist dataset",
    "ottawa lobbyist.ottawa.ca": "200, Incapsula-fronted ASP.NET search form only (search/searchlobbyist.aspx); no bulk file; not built",
    "alberta albertalobbyistregistry.ca": "APEX app, 302 chain to a CMS page; search is session-bound APEX; no bulk file; not built",
    "manitoba registry.lobbyistregistrar.mb.ca": "200, Java web search (lra/index.do); no bulk file; not built",
    "saskatchewan sasklobbyistregistry.ca": "200, WordPress site with a search page; no bulk file; not built",
    "nova scotia": "data.novascotia.ca 9ncn-d5ih is ARCHIVED (rows last updated 2016, no client/firm addresses); "
                   "lobbyist.novascotia.ca is a JS app; not built",
    "newfoundland and labrador cado.eservices.gov.nl.ca/Lobbyist": "ASP.NET search only; no bulk file; not built",
    "new brunswick lobbyistregistry.gnb.ca": "no answer (connection failed)",
    "edmonton / winnipeg open data": "meeting logs (data.edmonton.ca 3dkh-9hnu, data.winnipeg.ca vuvx-6wag); no consultant-client "
                                     "pairs with a firm address",
}
CANADA = {"canada", "ca", "can"}
ORG = re.compile(r"(?i)(\b(inc|incorporated|ltd|ltee|ltée|limited|llc|l\.l\.c|llp|lp|l\.p|ulc|gp|plc|corp|corporation|co|"
                 r"company|cie|compagnie|group|groupe|holdings?|association|assoc|society|societe|société|council|conseil|"
                 r"foundation|fondation|trust|partners|partnership|properties|property|developments?|development|homes|"
                 r"realty|capital|ventures|enterprises?|international|canada|canadian|services|systems|technologies|"
                 r"technology|tech|university|universit[eé]|college|school|hospital|church|city|town|township|region|"
                 r"regional|county|municipality|district|board|union|federation|fédération|institute|institut|centre|"
                 r"center|network|alliance|coalition|club|agency|authority|ministry|department|bank|credit|fund|"
                 r"investments?|management|consulting|consultants|solutions|industries|industry|energy|resources|mining|"
                 r"pharma|pharmaceuticals?|health|healthcare|media|communications|construction|builders|estates?|"
                 r"apartments|residences|living|care|farms?|foods?|motors?|airlines?|airways|airport|port|railway|"
                 r"transit|transport|logistics|insurance|financial|finance|bancorp|labs?|laboratories|studios?|"
                 r"entertainment|sports|hotel|hotels|restaurants?|bar|cafe|market|markets|store|stores|retail|"
                 r"brands?|products|manufacturing|chamber|league|committee|commission|cooperative|co-operative|coop|"
                 r"co-op|nation|first|band|tribe|museum|gallery|theatre|theater|festival|church|parish|mosque|temple|"
                 r"synagogue|clinic|medical|dental|pharmacy|bia|condominium|corporate|developer|land|lands|"
                 r"infrastructure|power|electric|hydro|gas|oil|water|waste|recycling|environmental|engineering|"
                 r"architects?|law|legal|lawyers|consortium|collective|project|projects|initiative|program|"
                 r"network|platform|labs|ai|government|gouvernement|house|communities|outdoor|hospitality|chapel|aviation|"
                 r"shipyards?|sugar|packaging|publishing|reit|gaming|residence|contracting|contractors|constructors|"
                 r"lifestyles?|aggregates|supplies|supply|metals?|advertising|wreckers|mobility|shelter|destination|"
                 r"urban|kids|phone|youth|seniors?|students?|wireless|telecom|software|digital|cannabis|automotive|"
                 r"auto|parking|signs?|cinemas?|theatres|developers|investors|ontario|toronto|vancouver|victoria|"
                 r"british|columbia|quebec|alberta|national|global|america|american|north|united|world|air|tire|solar|"
                 r"newspapers?|daily|gardens?|village|groceries|grocery|bistro|shoppe|shop|design|build|"
                 r"inc\.)\b|&\s*co\b|\.com\b|\.ca\b|s\.a\.|s\.e\.c\.|\bsa\b|\bag\b|\bgmbh\b|\bbv\b)")
LEGAL = re.compile(r"[,\s]+(inc|incorporated|l\.?l\.?c|llc|ltd|limited|corp|corporation|co|company|plc|lp|l\.?p|ulc|ltee|ltée)\.?$", re.I)
_wd_last = [0.0]
_wd_blocked = [False]  # set on HTTP 429 / "too many requests": stop Wikidata lookups for this run (no retry storms)


def log(*a):
    print(*a, flush=True)


def norm(s):
    return re.sub(r"[^a-z0-9]+", " ", unicodedata.normalize("NFKD", s or "").encode("ascii", "ignore").decode().lower()).strip()


def clean_val(v):
    v = re.sub(r"\s+", " ", (v or "").strip())
    return "" if v.lower() in ("null", "n/a", "na", "none", "-") else v


def fetch(url, path, max_age_h=20.0):
    """Download url to path once (re-download only when the cached copy is older than max_age_h hours)."""
    if os.path.exists(path) and time.time() - os.path.getmtime(path) < max_age_h * 3600:
        return path
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    with urllib.request.urlopen(req, timeout=300) as r:
        data = r.read()
    tmp = path + ".part"
    with open(tmp, "wb") as f:
        f.write(data)
    os.replace(tmp, path)
    log("downloaded", url, len(data))
    time.sleep(0.6)
    return path


def website(raw):
    w = (raw or "").strip().lower()
    if not w or w in ("null", "n/a", "none"):
        return "", ""
    w = re.sub(r"^(https?://)?", "", w).split("/")[0].split("?")[0].strip(" .,;")
    host = w
    if not re.fullmatch(r"[a-z0-9]([a-z0-9-]*[a-z0-9])?(\.[a-z0-9]([a-z0-9-]*[a-z0-9])?)*\.[a-z]{2,}", host):
        return "", ""
    dom = re.sub(r"^www\d?\.", "", host)
    return dom, "https://%s/" % host


def is_person(name, names):
    """names = (first names, surnames) learned from the registries' own lobbyists (persons)."""
    firstnames, surnames = names
    raw = (name or "").strip()
    titled = re.match(r"(?i)^(mr|mrs|ms|miss|dr|hon|the honourable|honourable)\.?\s+", raw) is not None
    n = re.sub(r"(?i)^(mr|mrs|ms|miss|dr|hon|the honourable|honourable)\.?\s+", "", raw)
    n = re.sub(r"(?i)\s*,?\s*in trust$", "", n)
    if not n or re.search(r"\d", n) or ORG.search(n):
        return False
    if n.count(",") == 1:
        a, b = [p.strip() for p in n.split(",")]
        if a and b and len(a.split()) <= 2 and len(b.split()) <= 2:
            n = b + " " + a
    toks = [t for t in n.replace("&", " & ").split() if t.lower() not in ("&", "and", "et")]
    if not 2 <= len(toks) <= 4:
        return False
    if not all(re.fullmatch(r"[A-Za-zÀ-ÿ][A-Za-zÀ-ÿ'.\-]*", t) for t in toks):
        return False
    if any(len(t) >= 2 and t.isupper() for t in toks) and not raw.isupper():  # acronym token: "Nitta Gelatin NA"
        return False
    if titled or toks[0].lower().strip(".") in firstnames:
        return True
    return len(toks) <= 3 and toks[-1].lower().strip(".") in surnames


def addr(el, prefix=""):
    """Toronto structured address -> (text joined with ', ', country, fields dict)."""
    keys = ("AddressLine1", "AddressLine2", "City", "Province", "Country", "PostalCode")
    if el is None:
        return "", "", {}
    vals = {k: clean_val(el.findtext(k)) for k in keys}
    if el.find("Phone") is not None:
        vals["Phone"] = clean_val(el.findtext("Phone"))
    text = ", ".join(vals[k] for k in keys if vals[k])
    return text, vals["Country"], {prefix + k: v for k, v in vals.items()}


# ---------------------------------------------------------------- Toronto
def toronto_files():
    pkg = os.path.join(CACHE, "tor_pkg.json")
    fetch(TOR_PKG, pkg)
    res = [r for r in json.load(open(pkg))["result"]["resources"] if r.get("format", "").upper() == "ZIP"]
    url = res[0]["url"]
    return url, fetch(url, os.path.join(CACHE, "tor_lobbyactivity.zip"))


def toronto_names(zpath):
    fn, sn = set(), set()
    with zipfile.ZipFile(zpath) as z:
        for member in z.namelist():
            with z.open(member) as f:
                for ev, el in ET.iterparse(f):
                    if el.tag in ("FirstName", "LobbyistFirstName") and el.text:
                        t = el.text.strip().split()
                        if t and len(t[0]) > 1:
                            fn.add(t[0].lower().strip("."))
                    elif el.tag in ("LastName", "LobbyistLastName") and el.text:
                        t = el.text.strip().split()
                        if t and len(t[-1]) > 1:
                            sn.add(t[-1].lower().strip("."))
                    elif el.tag == "SM":
                        el.clear()
    return fn, sn


def toronto(zurl, zpath, firstnames, since, today, stats):
    best = {}
    with zipfile.ZipFile(zpath) as z:
        for member in sorted(z.namelist()):
            with z.open(member) as f:
                for ev, el in ET.iterparse(f):
                    if el.tag != "SM":
                        continue
                    stats["toronto_sm"] += 1
                    if (el.findtext("Type") or "").strip() == "Consultant":
                        stats["toronto_consultant"] += 1
                        rec = toronto_one(el, member, zurl, firstnames, since, today, stats)
                        if rec:
                            k = rec["dataset_id"]
                            if k not in best or rec["row"]["record_date"] > best[k]["row"]["record_date"]:
                                best[k] = rec
                    el.clear()
    return list(best.values())


def toronto_one(sm, member, zurl, firstnames, since, today, stats):
    g = lambda p: clean_val(sm.findtext(p))
    smn, status = g("SMNumber"), g("Status")
    firm = sm.find("Firms/Firm")
    if firm is None:
        stats["toronto_no_firm"] += 1
        return None
    ftext, fcountry, ffields = addr(firm.find("BusinessAddress"), "firm_")
    vendor = clean_val(firm.findtext("Name"))
    canada_field = "Firms/Firm/BusinessAddress (City of Toronto Lobbyist Registry open data)"
    if not ftext:  # firm without address: fall back to the consultant's own business address
        ftext, fcountry, _ = addr(sm.find("Registrant/BusinessAddress"))
        canada_field = "Registrant/BusinessAddress (City of Toronto Lobbyist Registry open data)"
    if fcountry.lower() not in CANADA:
        stats["toronto_vendor_not_canada"] += 1
        return None
    client = None
    others = []
    for b in sm.findall("Beneficiaries/BENEFICIARY"):
        if clean_val(b.findtext("Type")) == "Client" and client is None:
            client = b
        else:
            others.append("%s: %s" % (clean_val(b.findtext("Type")), clean_val(b.findtext("Name"))))
    if client is None:
        stats["toronto_no_client"] += 1
        return None
    cname, ctrade = clean_val(client.findtext("Name")), clean_val(client.findtext("TradeName"))
    publisher = cname
    if is_person(cname, firstnames):
        if ctrade and ORG.search(ctrade) and not is_person(ctrade, firstnames):
            publisher = ctrade
        else:
            stats["toronto_client_person"] += 1
            return None
    if not publisher or norm(publisher) == norm(vendor):
        stats["toronto_client_self_or_empty"] += 1
        return None
    dates = [d for d in (g("InitialApprovalDate"), g("EffectiveDate")) if re.fullmatch(r"\d{4}-\d{2}-\d{2}", d)]
    if not dates:
        stats["toronto_no_date"] += 1
        return None
    record_date, end = max(dates), g("ProposedEndDate")
    comm = sorted(d for d in (clean_val(c.findtext("CommunicationDate")) for c in sm.findall("Communications/Communication")) if d)
    active = status == "Active"
    if not (record_date >= since or (active and end >= today)):
        stats["toronto_out_of_window"] += 1
        return None
    ctext, _, cfields = addr(client.find("BusinessAddress"), "client_")
    rtext, _, _ = addr(sm.find("Registrant/BusinessAddress"))
    reg = sm.find("Registrant")
    row = {"registry": "toronto", "file": member, "SMNumber": smn, "Status": status, "Type": g("Type"),
           "SubjectMatter": g("SubjectMatter"), "Particulars": g("Particulars"),
           "InitialApprovalDate": g("InitialApprovalDate"), "EffectiveDate": g("EffectiveDate"),
           "ProposedStartDate": g("ProposedStartDate"), "ProposedEndDate": end,
           "registrant_number": clean_val(reg.findtext("RegistrationNUmberWithSoNum")) if reg is not None else "",
           "registrant_name": " ".join(x for x in (clean_val(reg.findtext(k)) for k in ("FirstName", "MiddleInitials", "LastName")) if x) if reg is not None else "",
           "registrant_position": clean_val(reg.findtext("PositionTitle")) if reg is not None else "",
           "registrant_business_address": rtext,
           "firm_name": vendor, "firm_trade_name": clean_val(firm.findtext("TradeName")),
           "firm_business_type": clean_val(firm.findtext("BusinessType")), "firm_description": clean_val(firm.findtext("Description")),
           "client_name": cname, "client_trade_name": ctrade, "client_business_address": ctext,
           "other_beneficiaries": others, "communications": len(comm),
           "first_communication_date": comm[0] if comm else "", "last_communication_date": comm[-1] if comm else "",
           "end_date": end, "dataset_page": TOR_PAGE,
           "evidence_note": "public search secure.toronto.ca/lobbyistsearch returns 403; record = SMNumber in the open-data zip",
           "vendor_address_missing": False, "record_date": record_date}
    row.update(ffields)
    row.update(cfields)
    return {"platform": "lobby", "domain": "", "dataset_id": "toronto:" + smn,
            "dataset": "City of Toronto Lobbyist Registry (open data): consultant lobbyist registration", "dataset_url": zurl,
            "publisher": publisher, "buyer_unit": "", "website": "", "vendor": vendor, "canada_field": canada_field,
            "canada_value": ftext, "row": row}


# ---------------------------------------------------------------- British Columbia
def bc_rows(zpath, member):
    with zipfile.ZipFile(zpath) as z:
        with z.open(member) as f:
            return list(csv.DictReader(io.TextIOWrapper(f, encoding="utf-8-sig", newline="")))


def bc_names(zpath):
    fn, sn = set(), set()
    for member, first, last in (("Registration_ConsultantLobbyists_Export.csv", "LOBBYIST_FIRST_NAME", "LOBBYIST_LAST_NAME"),
                                ("Registration_InHouseLobbyists_Export.csv", "LOBBYIST_FIRST_NAME", "LOBBYIST_LAST_NAME"),
                                ("Registration_Primary_Export.csv", "FILER_FIRST_NAME", "FILER_LAST_NAME")):
        try:
            for r in bc_rows(zpath, member):
                t = clean_val(r.get(first)).split()
                if t and len(t[0]) > 1:
                    fn.add(t[0].lower().strip("."))
                t = clean_val(r.get(last)).split()
                if t and len(t[-1]) > 1:
                    sn.add(t[-1].lower().strip("."))
        except KeyError:
            pass
    return fn, sn


def bc(zpath, firstnames, since, today, stats):
    rows = bc_rows(zpath, "Registration_Primary_Export.csv")
    stats["bc_registrations"] = len(rows)
    by = {r["REG_ID"]: r for r in rows}
    prev = {r["PREVIOUS_VERSION_REG_ID"] for r in rows if clean_val(r["PREVIOUS_VERSION_REG_ID"])}
    out = []
    for r in rows:
        if r["REG_ID"] in prev:
            continue
        stats["bc_latest_versions"] += 1
        if r["REG_TYPE"] != "Cons":
            continue
        stats["bc_consultant_latest"] += 1
        first, versions, p, seen = r, 1, clean_val(r["PREVIOUS_VERSION_REG_ID"]), set()
        while p and p in by and p not in seen:
            seen.add(p)
            first, versions = by[p], versions + 1
            p = clean_val(by[p]["PREVIOUS_VERSION_REG_ID"])
        firm, faddr = clean_val(r["FIRM_NAME"]), clean_val(r["FIRM_ADDRESS"])
        individual = False
        canada_field = "FIRM_ADDRESS (BC Registrar of Lobbyists open data, Registration_Primary_Export.csv)"
        if not firm:
            individual = True
            firm = " ".join(x for x in (clean_val(r["FILER_FIRST_NAME"]), clean_val(r["FILER_MIDDLE_NAME"]), clean_val(r["FILER_LAST_NAME"])) if x)
            faddr = clean_val(r["FILER_ADDRESS"])
            canada_field = "FILER_ADDRESS (BC Registrar of Lobbyists open data, Registration_Primary_Export.csv; consultant without a firm)"
        if not faddr or faddr.rsplit(",", 1)[-1].strip().upper() not in ("CAN", "CANADA"):
            stats["bc_vendor_not_canada"] += 1
            continue
        client = clean_val(r["CLIENT_ORG_NAME"])
        if not client or (is_person(client, firstnames) and not website(r["CLIENT_ORG_WEB_ADDRESS"])[0]):
            stats["bc_client_person_or_empty"] += 1
            continue
        if norm(client) == norm(firm):
            stats["bc_client_self"] += 1
            continue
        start, pend, rend = clean_val(r["REG_START_DATE"]), clean_val(r["REG_PROJECTED_END_DATE"]), clean_val(r["REG_END_DATE"])
        end = rend or pend
        if not (start >= since or (not rend and pend >= today) or (rend and rend >= today)):
            stats["bc_out_of_window"] += 1
            continue
        dom, site = website(r["CLIENT_ORG_WEB_ADDRESS"])
        row = {"registry": "bc"}
        row.update({k: (v if v is not None else "") for k, v in r.items()})
        row.update({"first_start_date": clean_val(first["REG_START_DATE"]), "first_reg_id": first["REG_ID"], "versions": versions,
                    "end_date": end, "vendor_is_individual": individual, "vendor_address_missing": False,
                    "website_source": "CLIENT_ORG_WEB_ADDRESS" if site else "", "record_date": start})
        out.append({"platform": "lobby", "domain": dom, "dataset_id": "bc:" + r["REG_ID"],
                    "dataset": "Office of the Registrar of Lobbyists for British Columbia (open data): consultant lobbyist registration",
                    "dataset_url": BC_VIEW % (clean_val(r["CLIENT_ORG_NUM"]), r["REG_ID"].replace("R-", "")),
                    "publisher": client, "buyer_unit": "", "website": site, "vendor": firm, "canada_field": canada_field,
                    "canada_value": faddr, "row": row})
    return out


# ---------------------------------------------------------------- Wikidata (official website P856)
def wd_get(params):
    wait = _wd_last[0] + 1.05 - time.time()
    if wait > 0:
        time.sleep(wait)
    _wd_last[0] = time.time()
    if _wd_blocked[0]:
        return None
    try:
        req = urllib.request.Request(WD_API + urllib.parse.urlencode(dict(params, format="json")), headers={"User-Agent": UA})
        body = urllib.request.urlopen(req, timeout=30).read()
    except urllib.error.HTTPError as e:
        if e.code in (403, 429):
            _wd_blocked[0] = True
            log("wikidata refused (HTTP %d): lookups stopped for this run" % e.code)
        return None
    except Exception:
        return None
    try:
        return json.loads(body)
    except ValueError:
        if b"too many requests" in body.lower():
            _wd_blocked[0] = True
            log("wikidata rate limit page: lookups stopped for this run")
        return None


def wd_clean(name):
    n = re.sub(r"(?i)^the\s+", "", re.split(r"\s+\(|\s+-\s+|\s+c/o\s+", name)[0].strip())
    for _ in range(2):
        n = LEGAL.sub("", n).strip(" ,.")
    return n


def wikidata_site(name, cache):
    """One search per name (legal suffix removed); a hit is an item whose label or alias equals the cleaned or the full
    name, with an official website (P856), located in Canada or the US or with a domain that spells the name."""
    key = norm(name)
    if key in cache:
        return cache[key]
    v = wd_clean(name)
    targets = {norm(v), key}
    if len(norm(v)) < 4:
        cache[key] = None
        return None
    res = wd_get({"action": "wbsearchentities", "search": v, "language": "en", "limit": 10, "type": "item"})
    if res is None:
        return None
    ids = [x["id"] for x in res.get("search", []) if norm(x.get("label")) in targets or norm((x.get("match") or {}).get("text")) in targets]
    hit = None
    if ids:
        ents = wd_get({"action": "wbgetentities", "ids": "|".join(ids[:5]), "props": "claims"})
        if ents is None:
            return None
        for qid in ids[:5]:
            c = (ents.get("entities", {}).get(qid) or {}).get("claims", {})
            sites = [(x["mainsnak"].get("datavalue") or {}).get("value") for x in c.get("P856", [])]
            if not sites or not sites[0]:
                continue
            countries = {((x["mainsnak"].get("datavalue") or {}).get("value") or {}).get("id") for x in c.get("P17", [])}
            host = (urllib.parse.urlparse(sites[0]).hostname or "").lower()
            if countries & {"Q16", "Q30"} or norm(v).replace(" ", "") in host.replace("-", "").replace(".", ""):
                hit = [sites[0], qid]
                break
    cache[key] = hit
    return hit


def add_websites(recs, use_wd):
    cpath = os.path.join(CACHE, "wikidata_cache.json")
    cache = json.load(open(cpath)) if os.path.exists(cpath) else {}
    known = {}
    for r in recs:  # a website the source gives for a client is reused for the same client in the other registry
        if r["website"]:
            known.setdefault(norm(r["publisher"]), (r["domain"], r["website"], r["row"].get("website_source") or "source"))
    latest = {}
    for r in recs:
        if not r["website"] and norm(r["publisher"]) not in known:
            latest[r["publisher"]] = max(latest.get(r["publisher"], ""), r["row"]["record_date"])
    names = sorted(latest, key=lambda n: (latest[n], n), reverse=True)  # most recent buyers first
    if use_wd:
        log("wikidata lookups:", len([n for n in names if norm(n) not in cache]), "of", len(names))
        for i, n in enumerate(names, 1):
            if _wd_blocked[0]:
                break
            hit = wikidata_site(n, cache)
            if hit:
                dom, site = website(hit[0])
                if site:
                    known[norm(n)] = (dom, site, "Wikidata %s P856" % hit[1])
            if i % 50 == 0:
                json.dump(cache, open(cpath, "w"))
                log("  wikidata", i, "/", len(names), "found", sum(1 for k in known.values() if k[2].startswith("Wikidata")))
        json.dump(cache, open(cpath, "w"))
    else:  # cached hits only
        for n in names:
            hit = cache.get(norm(n))
            if hit:
                dom, site = website(hit[0])
                if site:
                    known[norm(n)] = (dom, site, "Wikidata %s P856" % hit[1])
    for r in recs:
        if not r["website"] and norm(r["publisher"]) in known:
            r["domain"], r["website"], r["row"]["website_source"] = known[norm(r["publisher"])]


def write(recs, path):
    tmp = path + ".part"
    with open(tmp, "w", encoding="utf-8") as f:
        for r in recs:
            f.write(json.dumps(r, ensure_ascii=False) + "\n")
    os.replace(tmp, path)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--no-wikidata", action="store_true", help="skip new Wikidata lookups (cached hits still used)")
    ap.add_argument("--today", default=datetime.date.today().isoformat())
    ap.add_argument("--out", default=OUT)
    a = ap.parse_args()
    os.makedirs(CACHE, exist_ok=True)
    os.makedirs(os.path.dirname(a.out), exist_ok=True)
    today = a.today
    t = datetime.date.fromisoformat(today)
    since = t.replace(year=t.year - 3).isoformat()
    last12 = t.replace(year=t.year - 1).isoformat()
    stats = __import__("collections").Counter()

    zurl, tzip = toronto_files()
    bzip = fetch(BC_ZIP, os.path.join(CACHE, "bc_ORL_Registration_Data.zip"))
    (f1, s1), (f2, s2) = toronto_names(tzip), bc_names(bzip)
    firstnames = (f1 | f2, s1 | s2)
    log("first names / surnames learned from the registries' lobbyists:", len(firstnames[0]), len(firstnames[1]))

    recs = toronto(zurl, tzip, firstnames, since, today, stats) + bc(bzip, firstnames, since, today, stats)
    best = {}
    for r in recs:  # one line per (buyer, vendor) pair, most recent record kept
        k = (norm(r["publisher"]), norm(r["vendor"]))
        if k not in best or (r["row"]["record_date"], r["row"].get("end_date", "")) > (best[k]["row"]["record_date"], best[k]["row"].get("end_date", "")):
            best[k] = r
    recs = sorted(best.values(), key=lambda r: (r["row"]["registry"], r["publisher"].lower(), r["vendor"].lower()))
    add_websites(recs, False)  # source websites + cached Wikidata hits; the file is written now, then again after lookups
    write(recs, a.out)
    if not a.no_wikidata:
        add_websites(recs, True)
        write(recs, a.out)

    buyers = {}
    for r in recs:
        b = buyers.setdefault(norm(r["publisher"]), {"date": "", "site": False, "reg": set()})
        b["date"] = max(b["date"], r["row"]["record_date"])
        b["site"] = b["site"] or bool(r["website"])
        b["reg"].add(r["row"]["registry"])
    for k in sorted(stats):
        log("  %-32s %d" % (k, stats[k]))
    for reg in ("toronto", "bc"):
        sub = [r for r in recs if r["row"]["registry"] == reg]
        log("  %s: rows %d, buyers %d" % (reg, len(sub), len({norm(r["publisher"]) for r in sub})))
    log("wrote", a.out)
    log("lobby_registries: %d rows, %d distinct buyers, %d buyers dated in last 12 months, %d with website" % (
        len(recs), len(buyers), sum(1 for b in buyers.values() if b["date"] >= last12), sum(1 for b in buyers.values() if b["site"])))


if __name__ == "__main__":
    main()
