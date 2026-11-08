#!/usr/bin/env python3
"""Official directories of public organisations → data/incoming/claude/claude_org_directories.csv (same schema as
claude_municipal_directory.csv), for legal names, addresses, phones and websites of school boards, hospitals, colleges, universities,
federal / UK / Australian / US public bodies (downstream §3.1: "buyer_legal_name_as_published is the single biggest unlock").

Sources are found through the open-data portals' own CKAN APIs (package_search) so no URL is guessed, then downloaded and parsed
generically (columns recognised by header words). Each row keeps the file URL as evidence and its own line as quote. Static APIs:
GOV.UK organisations, BC open-maps WFS for local-government offices. Polite: 1 request/second, identified user agent.
  python3 tools/gov_directories.py [--repo ~/cch-crawler] [--workdir ~/cch-tasks/dirs2]
"""
import argparse, csv, datetime, io, json, os, re, sys, time, urllib.parse, urllib.request

UA = "canada-contracts-hub-crawler/1.0 (+https://github.com/mohamedbiranesy-gif/canada-contracts-hub)"
TODAY = datetime.date.today().isoformat()
COLS = ["province", "legal_name", "designation", "municipal_tier", "upper_tier_or_mrc", "address", "postal_code", "phone", "website", "general_email", "population", "mayor_or_head",
        "source_url", "retrieved_date", "source_quote"]
# (portal CKAN base, query, province/country code, designation, must-match words in resource/package title)
CKAN = [
    ("https://data.ontario.ca", "school board contact information", "ON", "school board", r"school board|board.*contact"),
    ("https://data.ontario.ca", "hospital locations", "ON", "hospital", r"hospital"),
    ("https://data.ontario.ca", "Ontario hospitals", "ON", "hospital", r"hospital"),
    ("https://open.alberta.ca", "health facilities", "AB", "health facility", r"facilit"),
    ("https://data.ontario.ca", "colleges of applied arts and technology", "ON", "college", r"college"),
    ("https://data.ontario.ca", "universities", "ON", "university", r"universit"),
    ("https://www.donneesquebec.ca/recherche", "répertoire des établissements de santé et de services sociaux", "QC", "établissement de santé", r"r[ée]pertoire.*(tablissement|installation)|(tablissement|installation).*(sant|r[ée]pertoire)"),
    ("https://www.donneesquebec.ca/recherche", "liste des établissements publics santé services sociaux", "QC", "établissement de santé", r"liste.*tablissement|tablissements? publics"),
    ("https://www.donneesquebec.ca/recherche", "organismes scolaires", "QC", "centre de services scolaire", r"organisme|scolaire"),
    ("https://www.donneesquebec.ca/recherche", "cégeps", "QC", "cégep", r"c[ée]gep|coll[èe]ge"),
    ("https://open.alberta.ca", "school authority contact information", "AB", "school authority", r"school|authorit"),
    ("https://open.alberta.ca", "municipal officials", "AB", "municipality", r"municipal"),
    ("https://catalogue.data.gov.bc.ca", "school district contact information", "BC", "school district", r"school"),
    ("https://open.canada.ca/data", "Registry of Applied Titles", "FED", "federal organisation", r"applied titles|titres d'usage"),
    ("https://open.canada.ca/data", "designated learning institutions", "CA", "post-secondary institution", r"designated|dli"),
    ("https://data.gov.au/data", "Australian Government Organisations Register", "AU", "Australian Government body", r"organisations register|agor"),
    ("https://catalog.data.gov", "Government Units Survey", "US", "US government unit", r"government units"),
]
NAME_RX = re.compile(r"legal name|organi[sz]ation name|organisation|organization|board name|school board|district name|institution|establishment|nom de l|nom officiel|nom|^name$|^title$|entity|agency name|body name|municipality|government name|unit name", re.I)
WEB_RX = re.compile(r"web|url|site", re.I)
ADDR_RX = re.compile(r"address|adresse|street|rue", re.I)
PHONE_RX = re.compile(r"phone|t[ée]l[ée]phone|^tel", re.I)
CITY_RX = re.compile(r"^city|ville|municipalit[ée]$|town$", re.I)
PC_RX = re.compile(r"postal|zip|code postal", re.I)
EMAIL_RX = re.compile(r"e-?mail|courriel", re.I)
TYPE_RX = re.compile(r"type|designation|category|cat[ée]gorie|status", re.I)
_last = [0.0]


def get(url, timeout=120):
    now = time.time()
    if now - _last[0] < 1.0:
        time.sleep(1.0 - (now - _last[0]))
    _last[0] = time.time()
    req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept": "*/*"})
    with urllib.request.urlopen(req, timeout=timeout) as r:
        return r.read()


def pick_col(cols, rx, avoid=()):
    for c in cols:
        if rx.search(c or "") and not any(a.search(c) for a in avoid):
            return c
    return None


def parse_csv(data, src, prov, desi):
    text = data.decode("utf-8-sig", "replace").replace("\0", "")
    if text.lstrip().startswith(("<", "{")):
        return []  # HTML or JSON, not a CSV
    rows = []
    for dialect in (None, csv.excel, "semicolon", "tab"):
        try:
            if dialect is None:
                dialect = csv.Sniffer().sniff(text[:5000], delimiters=",;\t|")
            kw = {"delimiter": ";"} if dialect == "semicolon" else {"delimiter": "\t"} if dialect == "tab" else {"dialect": dialect}
            rows = list(csv.DictReader(io.StringIO(text, newline=""), **kw))
            if rows and len(rows[0]) > 1:
                break
        except Exception:
            rows = []
    if not rows:
        return []
    if not rows:
        return []
    cols = list(rows[0].keys())
    rows = [{(k or "").replace("_", " ").strip(): v for k, v in r.items()} for r in rows]
    cols = [(c or "").replace("_", " ").strip() for c in cols]
    ncol = pick_col(cols, NAME_RX, avoid=(re.compile(r"contact name|first|last|director|principal|mayor|cao|clerk|official name of contact", re.I),))
    if not ncol:
        return []
    wcol, acol, pcol, ccol, zcol, ecol, tcol = pick_col(cols, WEB_RX), pick_col(cols, ADDR_RX), pick_col(cols, PHONE_RX, (re.compile("fax", re.I),)), pick_col(cols, CITY_RX), pick_col(cols, PC_RX), pick_col(cols, EMAIL_RX), pick_col(cols, TYPE_RX)
    out = []
    for r in rows:
        name = (r.get(ncol) or "").strip()
        if len(name) < 3 or "@" in name:
            continue
        addr = ", ".join(v.strip() for v in ((r.get(acol) if acol else ""), (r.get(ccol) if ccol else "")) if v and v.strip())
        email = (r.get(ecol) or "").strip().lower() if ecol else ""
        if email and re.match(r"^[a-z]+\.[a-z]+@", email):
            email = ""  # a person's mailbox in a directory is never copied
        out.append({"province": prov, "legal_name": re.sub(r"\s+", " ", name)[:200], "designation": ((r.get(tcol) or "").strip()[:80] if tcol else desi) or desi, "municipal_tier": "", "upper_tier_or_mrc": "",
                    "address": addr[:200], "postal_code": (r.get(zcol) or "").strip()[:12] if zcol else "", "phone": (r.get(pcol) or "").strip()[:40] if pcol else "",
                    "website": (r.get(wcol) or "").strip()[:200] if wcol else "", "general_email": email[:120], "population": "", "mayor_or_head": "",
                    "source_url": src, "retrieved_date": TODAY, "source_quote": ("%s; %s; %s; %s" % (name, addr, (r.get(pcol) if pcol else "") or "", (r.get(wcol) if wcol else "") or ""))[:300]})
    return out


def ckan(base, query, prov, desi, must, workdir):
    try:
        d = json.loads(get("%s/api/3/action/package_search?q=%s&rows=10" % (base, urllib.parse.quote(query))))
    except Exception as e:
        print("  ckan search failed:", base, query, type(e).__name__, flush=True); return []
    for pkg in (d.get("result") or {}).get("results") or []:
        title = pkg.get("title") or ""
        for res in pkg.get("resources") or []:
            fmt = (res.get("format") or "").upper(); url = res.get("url") or ""
            if fmt not in ("CSV",) and not url.lower().endswith(".csv"):
                continue
            if not re.search(must, title + " " + (res.get("name") or ""), re.I):
                continue
            if re.search(r"rapport|financ|AS-471|statisti|d[ée]pense|budget|indicat|survey|enqu[êe]te|program standards|strategic mandate|researcher|chercheur|confidence in|graduate|enrol|salar", title + " " + (res.get("name") or ""), re.I):
                continue  # financial / statistical tables, not directories
            try:
                data = get(url, timeout=300)
            except Exception as e:
                print("  download failed:", url[:100], type(e).__name__, flush=True); continue
            rows = parse_csv(data, url, prov, desi)
            print("  %s | %s | %s → %d rows" % (base.split("//")[1][:28], title[:50], (res.get("name") or "")[:40], len(rows)), flush=True)
            if rows:
                return rows
    return []


def govuk():
    out, page = [], 1
    while page < 60:
        try:
            d = json.loads(get("https://www.gov.uk/api/organisations?page=%d" % page))
        except Exception as e:
            print("  gov.uk failed:", type(e).__name__, flush=True); break
        for o in d.get("results") or []:
            det = o.get("details") or {}
            out.append({"province": "UK", "legal_name": o.get("title") or "", "designation": o.get("format") or "UK public body", "municipal_tier": "", "upper_tier_or_mrc": (o.get("parent_organisations") or [{}])[0].get("id", "").rsplit("/", 1)[-1] if o.get("parent_organisations") else "",
                        "address": "", "postal_code": "", "phone": "", "website": o.get("web_url") or "", "general_email": "", "population": "", "mayor_or_head": "",
                        "source_url": "https://www.gov.uk/api/organisations?page=%d" % page, "retrieved_date": TODAY,
                        "source_quote": ("%s; %s; %s; status %s" % (o.get("title") or "", o.get("format") or "", o.get("web_url") or "", det.get("govuk_status") or ""))[:300]})
        if not d.get("next_page_url"):
            break
        page += 1
    print("  gov.uk organisations:", len(out), flush=True)
    return out


def bc_local_gov():
    url = ("https://openmaps.gov.bc.ca/geo/pub/WHSE_IMAGERY_AND_BASE_MAPS.GSR_LOCAL_GOVT_OFFICES_SV/ows?service=WFS&version=2.0.0&request=GetFeature"
           "&typeName=WHSE_IMAGERY_AND_BASE_MAPS.GSR_LOCAL_GOVT_OFFICES_SV&outputFormat=json&srsName=EPSG:4326")
    try:
        d = json.loads(get(url, timeout=300))
    except Exception as e:
        print("  bc wfs failed:", type(e).__name__, flush=True); return []
    out = []
    for f in d.get("features") or []:
        p = f.get("properties") or {}
        name = p.get("LOCAL_GOVT_NAME") or p.get("OFFICE_NAME") or p.get("NAME") or ""
        if not name:
            continue
        addr = ", ".join(v for v in (p.get("STREET_ADDRESS") or p.get("PHYSICAL_ADDRESS"), p.get("LOCALITY") or p.get("CITY")) if v)
        out.append({"province": "BC", "legal_name": name, "designation": p.get("LOCAL_GOVT_TYPE") or p.get("OFFICE_TYPE") or "local government", "municipal_tier": "", "upper_tier_or_mrc": p.get("REGIONAL_DISTRICT") or "",
                    "address": addr, "postal_code": p.get("POSTAL_CODE") or "", "phone": p.get("PHONE_NUMBER") or p.get("PHONE") or "", "website": p.get("WEBSITE_URL") or p.get("WEBSITE") or "",
                    "general_email": (p.get("EMAIL_ADDRESS") or "").lower() if not re.match(r"^[a-z]+\.[a-z]+@", (p.get("EMAIL_ADDRESS") or "").lower()) else "", "population": "", "mayor_or_head": "",
                    "source_url": url, "retrieved_date": TODAY, "source_quote": ("%s; %s; %s; %s" % (name, addr, p.get("PHONE_NUMBER") or "", p.get("WEBSITE_URL") or ""))[:300]})
    print("  bc local government offices:", len(out), flush=True)
    return out


def main():
    a = argparse.ArgumentParser()
    a.add_argument("--repo", default=os.path.expanduser("~/cch-crawler"))
    a.add_argument("--workdir", default=os.path.expanduser("~/cch-tasks/dirs2"))
    a = a.parse_args()
    os.makedirs(a.workdir, exist_ok=True)
    rows = []
    for base, q, prov, desi, must in CKAN:
        print("CKAN:", base, "|", q, flush=True)
        try:
            rows += ckan(base, q, prov, desi, must, a.workdir)
        except Exception as e:
            print("  failed:", type(e).__name__, e, flush=True)
    for fn in (govuk, bc_local_gov):
        try:
            rows += fn()
        except Exception as e:
            print("  failed:", fn.__name__, type(e).__name__, e, flush=True)
    out = os.path.join(a.repo, "data/incoming/claude/claude_org_directories.csv")
    with open(out, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=COLS); w.writeheader(); w.writerows(rows)
    print("wrote", out, len(rows), flush=True)


if __name__ == "__main__":
    main()
