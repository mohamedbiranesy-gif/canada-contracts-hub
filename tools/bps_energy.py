#!/usr/bin/env python3
"""Ontario's broader public sector reports its own electricity: what each organisation is billed for, and about how much.

2026-11-13 (owner, 13:20 EST: "have your estimate as precise and specific to relationship as possible add as much over 5000 as possible").

Under O. Reg. 25/23 (Electricity Act, 1998) every municipality, municipal service board, school board, university, college and public hospital
of Ontario reports each year the energy of each building or facility it owns or leases — and only those "the public agency is issued the
invoices and is responsible for making the payments for" (s. 6 (1)). The Ministry of Energy and Mines publishes the reports as open data, one
row per facility with its address and the kilowatt-hours of electricity bought from the grid. So for each organisation the open data says:
  - which electricity distributor bills it (the distributor licensed for the facility's address — tools/by_location.py biller_for), and that
    the organisation itself is issued those bills (the regulation's own condition for a facility to be reported);
  - how much electricity each facility used in the year.
A bill is calculated from that use: a facility under 12,000 kWh a month at its distributor's own small-business rates (the Ontario Energy
Board's file of current rates, as tools/data/billers_by_location_on.json carries it), a larger one at the average price Hydro-Québec's yearly
"Comparison of Electricity Prices in Major North American Cities" computed for Toronto or Ottawa at the consumption levels around its use —
the lower of the two levels' prices, and outside Toronto Hydro's and Hydro Ottawa's areas the lower of the two cities'. Calculated, labelled so.

Left out, and counted: a building whose use is implausible for its floor area (more than 1,500 kWh a square metre a year: the 2024 file's
"Municipal Administration Office" of Lambton Shores, 88,473,002 kWh on 1,130 m²), a second facility of one organisation reporting the very
same kilowatt-hours as another (Peel's Lakeview water plant and A.P. Kennedy plant, 62,878,017 kWh each), a parent property whose buildings
are listed too (the larger of the parent and the sum of its buildings is kept), and a facility whose postal code names no distributor.

  python3 tools/bps_energy.py build [--cache DIR]   -> tools/data/on_bps_electricity.json.gz
  python3 tools/bps_energy.py leads [--cache DIR]   -> data/incoming/claude/lead_shards/leads_bps_<stamp>.gz (bodies whose website is not a lead
                                                       yet) + their directory address in contrib/claude/rank_buyers/org_places.csv.gz
"""
import argparse, bisect, collections, datetime, gzip, json, os, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, ".."))
sys.path.insert(0, HERE)
OUT = os.path.join(HERE, "data", "on_bps_electricity.json.gz")

DATASET_PAGE = "https://data.ontario.ca/dataset/energy-use-and-greenhouse-gas-emissions-for-the-broader-public-sector"
FILES = [(2024, "https://data.ontario.ca/dataset/5e976319-9769-4f77-aab9-d170e0131efe/resource/b6b569cf-5d3a-4b96-9972-ea428c316278/download/2024_final_data_set.xlsx"),
         (2023, "https://data.ontario.ca/dataset/5e976319-9769-4f77-aab9-d170e0131efe/resource/a2fdbdb2-3cc9-4d30-a60f-58c70f6e3f5a/download/2023_final_data_set.xlsx")]
REGULATION = "https://www.ontario.ca/laws/regulation/230025"
HQ_PDF = "https://pannes.hydroquebec.com/data/documents-donnees/pdf/comparaison-prix-2025-en.pdf"
HQ_TITLE = "Comparison of Electricity Prices in Major North American Cities — rates in effect April 1, 2025 (Hydro-Québec)"
OEB_FILE = "https://www.oeb.ca/_html/calculator/data/BillData_GS.xml"

# the consumption levels of Hydro-Québec's summary table for business customers, kWh a month (power demand, load factor): small power 10,000
# (40 kW, 35 %), medium power 100,000 (500 kW, 28 %), 400,000 (1,000 kW, 56 %), 1,170,000 (2,500 kW, 65 %), large power 3,060,000 (5,000 kW,
# 85 %), 30,600,000 (50,000 kW, 85 %). The residential column (1,000 kWh) is not used.
LEVELS = [10000, 100000, 400000, 1170000, 3060000, 30600000]
SMALL = 12000  # kWh a month: under it a facility is priced at its distributor's own small-business (< 50 kW) rates
INTENSITY_MAX = 1500.0  # kWh a square metre a year: above it, a building's reported use is implausible (2023 and 2024 files: K-12 schools at most 525, hospitals 1,897 — one, Timmins; libraries 5,883 — one)
# types whose floor area says nothing of their electricity: a plant, a pumping station, street lighting, a substation, a parking lot, a field
NO_AREA_TEST = {"Other - Public Services", "Drinking Water Treatment & Distribution", "Wastewater Treatment Plant", "Transportation Terminal/Station", "Parking",
                "Other - Utility", "Other", "Energy/Power Station", "Other - Recreation", "Other - Entertainment/Public Assembly", "Other - Stadium", "Stadium (Open)",
                "Non-Refrigerated Warehouse", "Self-Storage Facility", "Vehicle Repair Services", "Other - Services", "Manufacturing/Industrial Plant", "Data Center",
                "Distribution Center", "Other - Technology/Science", "Laboratory"}


def fetch(url, cache, name):
    """the file, from the cache or the web (robots.txt obeyed, the project's user agent, one request a second per host)"""
    p = os.path.join(cache, name)
    if os.path.exists(p) and os.path.getsize(p) > 0:
        return open(p, "rb").read()
    import ap_crawler as C
    if not C.allowed(url):
        raise SystemExit("robots.txt of %s does not allow %s" % (url.split("/")[2], url))
    st, ct, b, fu = C.fetch(url, limit=40_000_000)
    if st != 200 or not b:
        raise SystemExit("%s answered %s" % (url, st))
    os.makedirs(cache, exist_ok=True)
    open(p, "wb").write(b)
    return b


def text_of_html(b):
    t = b.decode("utf-8", "replace")
    t = re.sub(r"<script.*?</script>|<style.*?</style>", " ", t, flags=re.S | re.I)
    t = re.sub(r"<[^>]+>", " ", t)
    t = t.replace("&nbsp;", " ").replace("&amp;", "&").replace("&#8217;", "’").replace("&rsquo;", "’")
    return re.sub(r"\s+", " ", t).strip()


def quote_from(text, start, end_words, limit=300):
    """the verbatim sentence of the page that begins with `start`, cut at the last whole word before `limit` characters"""
    i = text.find(start)
    if i < 0:
        raise SystemExit("not on the page any more: %r" % start)
    q = text[i:i + limit]
    for w in end_words:
        j = q.find(w)
        if j > 0:
            return q[:j + len(w)].strip()
    return q.rsplit(" ", 1)[0].strip()


def hq_prices(pdf):
    """{city: [¢/kWh at each of LEVELS]} for Toronto and Ottawa, read from the summary table "(in ¢/kWh) … excluding taxes" of the PDF"""
    import ap_crawler as C
    t = C.pdf_text(pdf) or ""
    i = t.find("AVERAGE PRICES ON APRIL 1, 2025")
    if i < 0:
        raise SystemExit("Hydro-Québec's table of average prices on April 1, 2025 is not in the PDF")
    seg = t[i:i + 6000]
    out, lines = {}, {}
    for city, code in (("Toronto", "ON"), ("Ottawa", "ON")):
        m = re.search(r"^\s*(%s, %s)\d?\s+((?:\d+\.\d\d\s+){6}\d+\.\d\d)\s*$" % (city, code), seg, re.M)
        if not m:
            raise SystemExit("no line for %s in Hydro-Québec's table" % city)
        v = [float(x) for x in m.group(2).split()]
        out[city], lines[city] = v[1:], re.sub(r"\s+", " ", m.group(0)).strip()  # v[0] is the residential column (1,000 kWh)
    return out, lines


def oeb_small(b):
    """(fixed charges $ a month, ¢ a kWh) of the distributor's small-business rates, as its record carries them from the Board's file — or None"""
    m = re.search(r"fixed charges \$([\d,.]+) \+ 2,500 kWh × ([\d.]+) ¢", b.get("estimate") or "")
    return (float(m.group(1).replace(",", "")), float(m.group(2))) if m else None


def price_large(m, city_prices):
    """¢ a kWh for a facility using m kWh a month: the lower of the prices at the two levels around m (above the last level, the last price)"""
    i = bisect.bisect_right(LEVELS, m) - 1
    if i < 0:
        return city_prices[0], (LEVELS[0], LEVELS[0])
    if i >= len(LEVELS) - 1:
        return city_prices[-1], (LEVELS[-1], LEVELS[-1])
    return min(city_prices[i], city_prices[i + 1]), (LEVELS[i], LEVELS[i + 1])


def read_xlsx(b):
    import io
    import openpyxl
    wb = openpyxl.load_workbook(io.BytesIO(b), read_only=True)
    ws = wb.worksheets[0]
    rows = ws.iter_rows(values_only=True)
    hdr = next(rows)
    ix = {h: i for i, h in enumerate(hdr)}
    for r in rows:
        if r and r[0] is not None:
            yield {h: r[i] for h, i in ix.items()}


def num(v):
    try:
        f = float(v)
        return f if f == f else None
    except (TypeError, ValueError):
        return None


def build(a):
    import by_location as BL
    cache = a.cache
    today = datetime.date.today().isoformat()
    page = text_of_html(fetch(DATASET_PAGE, cache, "bps_dataset_page.html"))
    q_page = quote_from(page, "Under O. Reg. 25/23", ["greenhouse gas (GHG) emissions"])
    q_vol = quote_from(page, "Several BPS organizations also voluntarily reported", ["not required by regulation."])
    reg = text_of_html(fetch(REGULATION, cache, "o_reg_25_23.html"))
    q_reg = quote_from(reg, "is required only if the public agency owns or leases", ["for the building or facility’s energy consumption", "for the building or facility's energy consumption"])
    prices, hq_lines = hq_prices(fetch(HQ_PDF, cache, "hq_comparison_2025_en.pdf"))
    orgs = collections.OrderedDict()
    seen_year = {}
    for year, url in FILES:
        for r in read_xlsx(fetch(url, cache, os.path.basename(url))):
            o = (r.get("Organization") or "").strip()
            if not o:
                continue
            if seen_year.setdefault(o, year) != year:
                continue  # the organisation's latest year only
            d = orgs.setdefault(o, {"sector": (r.get("Sector") or "").strip(), "subsector": (r.get("Subsector") or "").strip(), "year": year, "url": url, "fac": []})
            d["fac"].append({"name": (r.get("Property Name") or "").strip(), "type": (r.get("Primary Property Type - Self Selected") or "").strip(),
                             "address": str(r.get("Address") or "").strip(), "city": str(r.get("City") or "").strip(),
                             "pc": re.sub(r"\s", "", str(r.get("Postal Code") or "")).upper(), "kwh": num(r.get("Electricity Use - Grid Purchase (kWh)")),
                             "gfa": num(r.get("Property GFA - Self-Reported (m²)")), "pid": str(r.get("Portfolio Manager Property ID") or ""),
                             "parent": str(r.get("Portfolio Manager Parent Property ID") or "")})
    n = collections.Counter()
    out = {}
    for o, d in orgs.items():
        fac = [f for f in d["fac"] if f["kwh"] and f["kwh"] > 0]
        n["facilities with grid electricity"] += len(fac)
        # a parent property whose buildings are listed too: the larger of the parent and the sum of its buildings (the parent is often their sum)
        by_pid = {f["pid"]: f for f in fac}
        kids = collections.defaultdict(list)
        for f in fac:
            if f["parent"] in by_pid and f["parent"] != f["pid"]:
                kids[f["parent"]].append(f)
        drop = set()
        for p, ks in kids.items():
            if by_pid[p]["kwh"] <= sum(k["kwh"] for k in ks):
                drop.add(id(by_pid[p]))
            else:
                drop.update(id(k) for k in ks)
        n["parent or child properties left out (no double count)"] += len(drop)
        fac = [f for f in fac if id(f) not in drop]
        left = collections.Counter()
        keep, seen_kwh = [], set()
        for f in sorted(fac, key=lambda f: (f["name"], f["pid"])):
            if f["type"] not in NO_AREA_TEST and f["gfa"] and f["gfa"] >= 10 and f["kwh"] / f["gfa"] > INTENSITY_MAX:
                left["use implausible for the floor area"] += 1; continue
            if f["kwh"] >= 100000 and round(f["kwh"], 1) in seen_kwh:
                left["same kilowatt-hours as another of its facilities"] += 1; continue
            seen_kwh.add(round(f["kwh"], 1))
            b = BL.biller_for(f["pc"]) if len(f["pc"]) == 6 else None
            if not b:
                left["postal code names no distributor"] += 1; continue
            keep.append((f, b))
        for k, v in left.items():
            n["facilities left out: " + k] += v
        groups = {}
        for f, b in keep:
            g = groups.setdefault(b["key"], {"distributor": b["name"], "n": 0, "kwh": 0.0, "month": 0.0, "n_small": 0, "n_small_hq": 0, "n_large": 0, "small_rate": None, "city": "",
                                             "pcs": [], "places": []})
            m = f["kwh"] / 12.0
            city = "Toronto" if b["key"] == "toronto_hydro" else "Ottawa" if b["key"] == "hydro_ottawa" else ""
            cp = prices[city] if city else [min(x, y) for x, y in zip(prices["Toronto"], prices["Ottawa"])]
            sr = oeb_small(b)
            if m < SMALL and sr:
                bill = sr[0] + m * sr[1] / 100.0
                g["n_small"] += 1; g["small_rate"] = sr
            else:
                p, _lv = price_large(m, cp)
                bill = m * p / 100.0
                if m < SMALL:
                    g["n_small_hq"] += 1  # a small facility of a distributor whose small-business rates are not in the Board's file as read: the small-power price
                else:
                    g["n_large"] += 1
            g["city"] = city or "Ottawa and Toronto"
            g["n"] += 1; g["kwh"] += f["kwh"]; g["month"] += bill
            if f["pc"] not in g["pcs"]:
                g["pcs"].append(f["pc"])
            pl = (f["city"] or "").strip().title()
            if pl and pl not in g["places"]:
                g["places"].append(pl)
        for g in groups.values():
            g["kwh"] = round(g["kwh"]); g["month"] = round(g["month"], 2)
            g["pcs"] = g["pcs"][:400]; g["places"] = g["places"][:40]
        if groups:
            out[o] = {"sector": d["sector"], "subsector": d["subsector"], "year": d["year"], "url": d["url"], "groups": groups, "left_out": dict(left),
                      "facilities": sum(g["n"] for g in groups.values())}
    for o, e in find_directory(index(out), cache).items():
        out[o]["directory"] = e  # its website and address in the province's own lists (school boards; institutions under FIPPA / MFIPPA)
    for d_ in out.values():
        for k_ in ("_fsas", "_places", "_kind"):
            d_.pop(k_, None)
    meta = {"built": today, "dataset_page": DATASET_PAGE, "dataset_quote": q_page, "dataset_quote_voluntary": q_vol, "regulation": REGULATION, "regulation_quote": q_reg,
            "files": {str(y): u for y, u in FILES}, "hq_pdf": HQ_PDF, "hq_title": HQ_TITLE, "hq_lines": hq_lines, "hq_levels": LEVELS, "hq_prices": prices,
            "oeb_file": OEB_FILE, "small_kwh": SMALL, "intensity_max": INTENSITY_MAX, "counts": dict(n)}
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    with gzip.open(OUT, "wt", encoding="utf-8") as fh:
        json.dump({"meta": meta, "orgs": out}, fh, ensure_ascii=False, sort_keys=True)
    tot = collections.Counter()
    for o, d in out.items():
        best = max(d["groups"].values(), key=lambda g: g["month"])
        tot["organisations"] += 1
        tot["of which the bill of one distributor is $5,000 a month or more"] += best["month"] >= 5000
        tot["by sector: " + d["sector"]] += 1
    print(json.dumps({"counts": dict(n), "result": dict(tot)}, indent=1, ensure_ascii=False))
    print("quotes:", q_page, "|", q_reg, "|", hq_lines)


# ---- which row of the table is which organisation of the reports (used by contrib/claude/rank_buyers/rank.py) ---------------------------------
# A municipality is named the same way everywhere but for its form of words ("The Corporation of the City of Markham" / "City of Markham",
# "Regional Municipality of Durham" / "Durham Region"): its place name and whether it is a lower or an upper tier decide. A school board, a
# university, a college or a hospital must carry the same distinctive words (the reports print some hospitals with their city in front,
# "Toronto University Health Network", "Oshawa Lakeridge Health": a first word that is one of its facilities' places is dropped). Then the row's
# own address must agree: its postal area is one of the organisation's facilities', or one of their places is in it. No address on the row: a
# municipality by name in a row of Ontario, nothing else.
_UP = {"county", "counties", "united counties", "region", "regional municipality", "district municipality", "district"}
_MUNI = re.compile(r"^(united counties|united townships|regional municipality|district municipality|separated town|city|town|township|municipality|village|county|region|district) of (.+)$")
_MUNI2 = re.compile(r"^(.+?) (region|county|township|city|town|municipality)$")
_GEN = {"the", "of", "and", "at", "inc", "corporation", "corp", "la", "le", "les", "de", "du", "des", "et", "d", "l"}
_INST = {"institute", "technology", "applied", "arts", "advanced", "learning", "polytechnic", "college", "university", "universite", "college", "colleges"}
_HOSP = {"hospital", "hospitals", "health", "healthcare", "centre", "center", "sciences", "science", "network", "system", "services", "regional", "district", "general",
         "memorial", "care", "corporation", "partners", "alliance", "group", "site", "sites", "campus", "hopital", "sante", "soins", "community", "public"}


def fold(s):
    s = unicodedata_fold(s or "").lower().replace("&", " and ").replace("’", "'")
    s = re.sub(r"'s\b", "s", s)
    return " ".join(re.sub(r"[^a-z0-9]+", " ", s).split())


def unicodedata_fold(s):
    import unicodedata
    return unicodedata.normalize("NFKD", s).encode("ascii", "ignore").decode()


def muni_key(name):
    f = re.sub(r"^(?:the )?corporation of (?:the )?", "", fold(name))
    f = re.sub(r"^the ", "", f)
    m = _MUNI.match(f)
    if m:
        t, core = m.group(1), m.group(2)
    else:
        m = _MUNI2.match(f)
        if not m:
            return None
        core, t = m.group(1), m.group(2)
    core = " ".join(w for w in core.split() if w not in ("the", "of"))
    return (core, "up" if t in _UP else "low", t)


def _kind(o, d):
    sub = (d.get("subsector") or "").lower()
    if sub.startswith("munic"):
        return "muni"
    if (d.get("sector") or "").lower().startswith("school"):
        return "school"
    if (d.get("sector") or "").lower().startswith("post"):
        return "inst"
    return "hosp"


_SAME = {"universite": "university", "hopital": "hospital", "centre": "center", "saint": "st", "ste": "st", "sainte": "st"}


def _toks(s, drop=()):
    return [_SAME.get(w, w) for w in fold(s).split() if w not in _GEN and w not in drop]


def index(orgs):
    """the organisations of the reports, ready to be matched to rows"""
    ix = {"muni": collections.defaultdict(list), "other": [], "orgs": orgs}
    for o, d in orgs.items():
        k = _kind(o, d)
        fsas = sorted({p[:3] for g in d["groups"].values() for p in g["pcs"]})
        places = sorted({fold(p) for g in d["groups"].values() for p in g["places"] if p})
        d["_fsas"], d["_places"], d["_kind"] = set(fsas), places, k
        if k == "muni":
            mk = muni_key(o)
            if mk:
                ix["muni"][mk[:2]].append((o, mk[2]))
            continue
        t = _toks(o)
        t0 = list(t)
        if k == "hosp" and len(t) > 2 and t[0] in {w for p in places for w in p.split()}:
            t = t[1:]  # "Toronto University Health Network": the city in front
        core = frozenset(w for w in t if w not in (_HOSP if k == "hosp" else _INST if k == "inst" else ()))
        if not core and t0 != t:
            t = t0  # "Hamilton Health Sciences Corporation": the city is the name — kept, and then the whole name must be the same
            core = frozenset(w for w in t if w not in (_HOSP if k == "hosp" else _INST if k == "inst" else ()))
        if core:
            # a core of place names only ("The Ottawa Hospital": ottawa) is not distinctive: there the whole name must be the same
            only_places = core <= {w for p in places for w in p.split()} | {"toronto", "ottawa", "ontario"}
            ix["other"].append((o, k, core, frozenset(t), only_places))
    return ix


_KW = {"school": re.compile(r"\b(school board|conseil scolaire|district school|catholic district|board of education)\b", re.I),
       "inst": re.compile(r"\b(universit|college|coll[eè]ge|polytechni|institute)", re.I),
       "hosp": re.compile(r"\b(hospital|h[oô]pital|health|sant[ée]|healthcare|medical cent|care cent)", re.I)}


def _dom(url_or_mail):
    from ap_crawler import registrable
    h = (url_or_mail or "").strip().lower()
    h = h.partition("@")[2] if "@" in h and "/" not in h else re.sub(r"^https?://", "", h).split("/")[0].split("?")[0]
    return (registrable(h) or h) if h else ""


_NOT_BODY = re.compile(r"\b(?:foundation|fondation|auxiliary|auxiliaire|volunteers?|b[ée]n[ée]voles|alumni|anciens|students?|[ée]tudiants?|association|union|syndicat|"
                       r"federation|f[ée]d[ée]ration|society|soci[ée]t[ée]|club|guild|research institute)\b", re.I)


def match(ix, name, address, jur, email=""):
    """the organisation of the reports this row is, or None — (organisation, how). A row without a postal code: a municipality by name in a
    row of Ontario; any body whose mailbox is on the domain of the website its province's directory gives it (City of Ottawa, ottawa.ca)"""
    if not ix or not name:
        return None
    name = re.sub(r"\s*\([^()]{1,40}\)\s*", " ", name).strip() or name  # "(DSB1)", "(HGMH)": an abbreviation in brackets is no word of the name
    pcs = re.findall(r"(?<![A-Za-z0-9])([KLMNP]\d[A-Z])\s?\d[A-Z]\d(?![A-Za-z0-9])", (address or "").upper())
    if re.search(r"(?<![A-Za-z0-9])[ABCEGHJRSTVXY]\d[A-Z]\s?\d[A-Z]\d(?![A-Za-z0-9])", (address or "").upper()) and not pcs:
        return None  # a postal code of another province
    md = _dom(email) if email else ""
    if not pcs and (jur or "") != "ON" and not md:
        return None
    fa = fold(address or "")
    def agrees(d):
        if pcs:
            return any(p in d["_fsas"] for p in pcs) or any(re.search(r"\b%s\b" % re.escape(pl), fa) for pl in d["_places"] if len(pl) > 3)
        if md and (d.get("directory") or {}).get("site_ok") and _dom(d["directory"].get("website")) == md:
            return "mailbox"
        return None  # no postal code on the row
    mk = muni_key(name)
    if mk:
        c = ix["muni"].get(mk[:2]) or []
        if len(c) > 1:
            c = [t for t in c if t[1] == mk[2]]
        if len(c) == 1:
            d = ix["orgs"][c[0][0]]
            a = agrees(d)
            if a is None and md and (jur or "") in ("ON", "CA", "") and (md.endswith(".ca") or md.endswith(".on.ca")) and \
                    not re.search(r"\.(?:bc|ab|sk|mb|qc|nb|ns|pe|nl|nf|yk|yt|nt|nu)\.ca$", md):
                # a row without a postal code: the mailbox is on a .ca domain that spells the municipality's own name ("apinvoice@toronto.ca")
                core = re.sub(r"[^a-z]", "", mk[0])
                if len(core) >= 4 and core in re.sub(r"[^a-z]", "", md.split(".")[0]):
                    a = "mailbox-name"
            if a or (a is None and jur == "ON"):
                return c[0][0], ("name and the mailbox's domain, the website Ontario's directory gives it" if a == "mailbox" else
                                 "name and the mailbox's .ca domain, which spells the municipality's name" if a == "mailbox-name" else "name and address" if a else
                                 "name, in a row of Ontario without a postal code")
        return None
    best = None
    if _NOT_BODY.search(name):
        return None  # a foundation, an auxiliary, an alumni or student body: an organisation of its own beside the body
    kinds = {k for k, rx in _KW.items() if rx.search(name)}
    if not kinds:
        return None
    t = _toks(name)
    rcores = {k: frozenset(w for w in t if w not in (_HOSP if k == "hosp" else _INST if k == "inst" else ())) for k in kinds}
    for o, k, core, full, only_places in ix["other"]:
        if k not in kinds:
            continue
        rcore = rcores[k]
        if k == "school" or only_places:
            ok = frozenset(t) == full
        else:
            ok = rcore == core or (core <= rcore and len(core) >= 2 and rcore - core <= (_HOSP | _INST | {w for p in ix["orgs"][o]["_places"] for w in p.split()}))
        if not ok and md:
            # the row's mailbox is on the website Ontario's directory gives the body ("apinvoice@uwo.ca" — the University of Western Ontario's
            # uwo.ca, a row named "Western University"), the two names share a word that is not a generic one, and the row's name says nothing
            # the body's own name does not ("University of Waterloo SAF", "University Health Network - Toronto Rehab": a unit, not the body)
            dr = ix["orgs"][o].get("directory") or {}
            extra = {w for w in t if w not in _HOSP and w not in _INST} - full
            ok = bool(dr.get("site_ok") and _dom(dr.get("website")) == md and (set(t) & (core - {"ontario", "toronto", "canada"})) and not extra)
        if not ok:
            continue
        a = agrees(ix["orgs"][o])
        if a:
            if best:
                return None  # two organisations fit: never guess
            best = (o, "name and the mailbox's domain, the website Ontario's directory gives it" if a == "mailbox" else "name and address")
    return best


# ---- the bodies the table does not hold yet: their website and address from two Ontario directories, as leads -------------------------------
# A body of the reports becomes a row when the crawler finds its own role mailbox. Its website and its address come from the province's own
# lists: the public school boards' contact list, and the directory of institutions under FIPPA / MFIPPA (municipalities, hospitals, colleges,
# universities, boards). Their e-mail column is never read (a register's e-mail is not a mailbox the organisation chose to publish for us).
BOARDS = "https://data.ontario.ca/dataset/9831236f-6e01-447a-9e28-b9c6b3348631/resource/74aa6226-7798-4130-ba44-8546e3198186/download/school_board_contact_list_september2026_en_csv.csv"
BOARDS_SRC = "Ontario's public school board contact list (data.ontario.ca, September 2026)"
DOI = "https://data.ontario.ca/dataset/ec9daf71-33de-469e-af32-05265673049b/resource/c1164f6a-1677-4b21-9ff2-5e92163e9a99/download/doi_dec2025_en.csv"
DOI_SRC = "Ontario's directory of institutions under FIPPA and MFIPPA (data.ontario.ca, December 2025)"
PLACES_FILE = os.path.join(ROOT, "contrib/claude/rank_buyers/org_places.csv.gz")
PLACE_COLS = ["buyer_key", "name", "address", "city", "province", "postal_code", "country", "source"]


def _clean(v):
    v = re.sub(r"<[^>]+>", "", str(v or "")).strip()
    return "" if v.lower() in ("not available", "n/a", "none", "-") else v


def _po(v):
    return ("" if not v else v if re.match(r"(?i)(?:p\.?\s?o\.?\s?)?box\b|postal bag|bag\b|c\.?p\.?\b", v) else "PO Box " + v)


def directory_entries(cache):
    import csv as _csv, io
    out = []
    for r in _csv.DictReader(io.StringIO(fetch(BOARDS, cache, "school_board_contact_list_en.csv").decode("utf-8-sig", "replace"))):
        out.append({"name": _clean(r.get("Board Name")), "website": _clean(r.get("Website")), "address": ", ".join(v for v in (_clean(r.get("Suite")), _po(_clean(r.get("PO Box"))), _clean(r.get("Street"))) if v),
                    "city": _clean(r.get("City")), "postal_code": _clean(r.get("Postal Code")), "source": BOARDS_SRC})
    for r in _csv.DictReader(io.StringIO(fetch(DOI, cache, "doi_en.csv").decode("utf-8-sig", "replace"))):
        out.append({"name": _clean(r.get("Name of institution")), "website": _clean(r.get("Website")),
                    "address": ", ".join(v for v in (_clean(r.get("Suite/Floor/P.O. box/Building name")), _clean(r.get("Street"))) if v),
                    "city": _clean(r.get("City")), "postal_code": _clean(r.get("Postal code")), "source": DOI_SRC, "type": _clean(r.get("Institution type"))})
    return out


def _site_fits(name, dom):
    """the directory's website is the body's own when its domain carries a word of the name (4 letters or more) or the initials of the name
    ("tvdsb.on.ca" Thames Valley District School Board, "rmh.org" Ross Memorial Hospital); a web agency's staging host does not"""
    lab = re.sub(r"[^a-z0-9]", "", (dom or "").split(".")[0])
    words = [w for w in fold(name).split() if w not in ("of", "and", "the", "de", "du", "des", "la", "le")]
    if any(len(w) >= 4 and w in lab for w in words):
        return True
    ini = "".join(w[0] for w in words)
    return any(ini[i:i + 3] in lab for i in range(max(1, len(ini) - 2)))


def find_directory(ix, cache):
    """{organisation of the reports: its entry in the school board list or the directory of institutions} — matched by name and address"""
    found = {}
    for e in directory_entries(cache):
        pc = re.sub(r"\s", "", e["postal_code"]).upper()
        m = match(ix, e["name"], "%s, %s, ON %s" % (e["address"], e["city"], pc), "ON")
        if not m:
            continue
        o = m[0]
        if o in found and found[o]["source"] == BOARDS_SRC:
            continue  # the school board list first
        e = dict(e, postal_code=pc)
        w = e["website"]
        if w:
            if not re.match(r"https?://", w, re.I):
                w = "https://" + w.lstrip("/")
            host = re.sub(r"^https?://", "", w.lower()).split("/")[0].split("?")[0]
            e["website"] = "%s://%s/" % ("http" if w.lower().startswith("http:") else "https", host)  # the directory often links its FOI page
            e["site_ok"] = _site_fits(e["name"], _dom(e["website"]))
        found[o] = e
    return found


def leads(a):
    import csv as _csv, hashlib, io
    import lead_store as LS
    from ap_crawler import registrable
    d = load()
    ix = index(d["orgs"])
    have_dom = {}
    for r in LS.rows():
        w = (r.get("website") or "").strip()
        host = re.sub(r"^https?://", "", w.lower()).split("/")[0]
        if host:
            have_dom.setdefault(registrable(host) or host, r.get("buyer_key") or "")
    n = collections.Counter()
    found = find_directory(ix, a.cache)
    n["bodies of the reports found in a directory"] = len(found)
    new_leads, places = [], {}
    stamp = datetime.datetime.now(datetime.timezone.utc).strftime("%Y%m%dT%H%M%S")
    for o, e in sorted(found.items()):
        w = e["website"]
        if not w:
            n["… without a website in the directory"] += 1
            continue
        dom = _dom(w)
        if not e.get("site_ok"):
            n["… whose directory website is not shown to be its own (no word or initials of its name in the domain)"] += 1
            continue
        k = have_dom.get(dom)
        if k:
            n["… whose website is already a lead (its key gets the directory's address)"] += 1
        else:
            k = "lead:" + hashlib.sha1(("bps|" + dom).encode()).hexdigest()[:16]
            g = max(d["orgs"][o]["groups"].values(), key=lambda g_: g_["month"])
            new_leads.append({"buyer_key": k, "buyer_name": e["name"], "website": w, "canadian_vendor_rows": 1, "example_vendor": g["distributor"],
                              "canada_field_value": "Ontario broader public sector energy report (O. Reg. 25/23): %d %s in the distributor's territory" % (g["n"], "facility" if g["n"] == 1 else "facilities"),
                              "evidence_dataset": "Ontario Broader Public Sector energy reporting, %s data set (data.ontario.ca); %s" % (d["orgs"][o]["year"], e["source"]),
                              "latest_record_date": "%s-12-31" % d["orgs"][o]["year"]})
            have_dom[dom] = k
            n["… new leads"] += 1
        if e["address"] and len(e["postal_code"]) == 6:
            places[k] = {"buyer_key": k, "name": e["name"], "address": e["address"], "city": e["city"], "province": "ON", "postal_code": e["postal_code"], "country": "CA", "source": e["source"]}
    if new_leads:
        os.makedirs(LS.SHARDS, exist_ok=True)
        p = os.path.join(LS.SHARDS, "leads_bps_%s.gz" % stamp)
        with gzip.open(p, "wt", encoding="utf-8", newline="") as fh:
            w_ = _csv.DictWriter(fh, fieldnames=LS.LEAD_COLS)
            w_.writeheader()
            for r in new_leads:
                w_.writerow(r)
        print("wrote", p, len(new_leads))
    if places:
        cur = []
        with gzip.open(PLACES_FILE, "rt", encoding="utf-8") as fh:
            cur = [r for r in _csv.DictReader(fh) if r["buyer_key"] not in places]
        with gzip.open(PLACES_FILE, "wt", encoding="utf-8", newline="") as fh:
            w_ = _csv.DictWriter(fh, fieldnames=PLACE_COLS)
            w_.writeheader()
            for r in sorted(cur + list(places.values()), key=lambda r: r["buyer_key"]):
                w_.writerow({c: r.get(c, "") for c in PLACE_COLS})
        n["registered addresses written for the ranker (org_places.csv.gz)"] = len(places)
    print(json.dumps(dict(n), indent=1, ensure_ascii=False))


def load(path=OUT):
    try:
        with gzip.open(path, "rt", encoding="utf-8") as fh:
            return json.load(fh)
    except (OSError, ValueError):
        return {"meta": {}, "orgs": {}}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("cmd", choices=["build", "leads"])
    ap.add_argument("--cache", default=os.path.expanduser("~/cch-crawler-state/bps"))
    a = ap.parse_args()
    build(a) if a.cmd == "build" else leads(a)


if __name__ == "__main__":
    main()
