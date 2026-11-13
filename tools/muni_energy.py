#!/usr/bin/env python3
"""A municipality's electricity bill, estimated from its own population (owner 2026-11-13 13:20 EST: "have your estimate as precise and specific to
relationship as possible add as much over 5000 as possible").

A row that stands on where a municipality is (tools/by_location.py: the distributor of its town hall's address) carried the distributor's bill at
2,500 kWh a month — a small office's. A municipality's facilities (its town hall, arenas, pools, libraries, garages, water and sewage plants) are
billed by the same distributor, each on its own account, every month. How much electricity a municipality buys grows with the people it serves:
Ontario's municipalities report every facility's grid electricity under O. Reg. 25/23 (tools/bps_energy.py), and Statistics Canada counts the
residents of every municipality (2021 Census, table 98-10-0002-01: tools/data/ca_csd_population.csv.gz). The kWh a resident a year of the Ontario
municipalities of a size class — their lower quartile and their median — times the municipality's residents gives its use; Hydro-Québec's
comparison of electricity prices in Canadian cities on April 1, 2025 (tools/bps_energy.py HQ_PDF) prices it at the province's city, the lower of
its prices at 10,000 and 100,000 kWh a month. The row says all of it, and that it is an estimate; the amount mark rests on the lower quartile.
Ontario is left to the reports themselves; Alberta's customers choose their retailer (no distributor's bill); the territories are not in the table.

  python3 tools/muni_energy.py build      -> tools/data/muni_energy.json.gz
  python3 tools/muni_energy.py show NAME PROVINCE
"""
import csv, gzip, json, os, re, statistics, sys, unicodedata

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "data/muni_energy.json.gz")
CSD = os.path.join(HERE, "data/ca_csd_population.csv.gz")
BPS = os.path.join(HERE, "data/on_bps_electricity.json.gz")
CENSUS_URL = "https://www150.statcan.gc.ca/t1/tbl1/en/tv.action?pid=9810000201"
CENSUS_FILE = "https://www150.statcan.gc.ca/n1/tbl/csv/98100002-eng.zip"
CLASSES = [(0, 2500), (2500, 10000), (10000, 25000), (25000, 100000), (100000, 10 ** 9)]
# the province's city in Hydro-Québec's comparison, and the distributor whose bill that is (the main distributor of the province in tools/by_location.py)
CITY = {"QC": ("Montréal, QC", "Hydro-Québec"), "BC": ("Vancouver, BC", "BC Hydro"), "MB": ("Winnipeg, MB", "Manitoba Hydro"), "SK": ("Regina, SK", "SaskPower"),
        "NB": ("Moncton, NB", "NB Power"), "NS": ("Halifax, NS", "Nova Scotia Power"), "PE": ("Charlottetown, PE", "Maritime Electric"),
        "NL": ("St. John’s, NL", "Newfoundland Power")}
LEVELS_READ = (10000, 100000)  # the small-power (40 kW) and the first medium-power (500 kW) columns of the comparison

TYPE_WORDS = {"city", "town", "township", "village", "municipality", "municipalite", "municipal", "ville", "paroisse", "canton", "cantons", "unis", "district",
              "rural", "rm", "resort", "summer", "corporation", "of", "de", "du", "des", "la", "le", "les", "the", "d", "l", "united", "townships"}
UPPER = re.compile(r"\b(?:county|counties|regional|region|mrc|comte|metro|metropolitan|agglomeration|communaute)\b", re.I)
KIND = re.compile(r"^(?:the\s+)?(?:corporation\s+of\s+the\s+)?(?:city|town|township|village|municipality|district\s+municipality|municipal\s+district|rural\s+municipality|"
                  r"resort\s+municipality|summer\s+village|united\s+townships?|municipalite|ville|paroisse|canton|cantons\s+unis|rm)\b|\b(?:township|municipality)$", re.I)


def fold(t):
    t = unicodedata.normalize("NFKD", t or "").encode("ascii", "ignore").decode().lower()
    t = re.sub(r"[^a-z0-9]+", " ", t)
    t = re.sub(r"\bsainte\b", "ste", re.sub(r"\bsaint\b", "st", t))
    return t.strip()


def core(t):
    return "".join(w for w in fold(t).split() if w not in TYPE_WORDS)


def _csd():
    out = {}
    for r in csv.DictReader(gzip.open(CSD, "rt", encoding="utf-8")):
        if not r["population_2021"]:
            continue
        out.setdefault((r["province"], core(r["name"])), []).append({"code": r["csd_code"], "name": r["name"], "pop": int(r["population_2021"])})
    return out


def hq_city_prices():
    """{province: (city line as printed, [¢/kWh at 10,000, at 100,000])} from the comparison PDF (cached by tools/bps_energy.py)"""
    sys.path.insert(0, HERE)
    import ap_crawler as C
    pdf = os.path.expanduser("~/cch-crawler-state/bps/hq_comparison_2025_en.pdf")
    t = C.pdf_text(open(pdf, "rb").read()) or ""
    i = t.find("AVERAGE PRICES ON APRIL 1, 2025")
    seg = t[i:i + 6000]
    out = {}
    for prov, (city, _d) in CITY.items():
        m = re.search(r"^\s*(%s)\d?\s+((?:\d+\.\d\d\s+){6}\d+\.\d\d)\s*$" % re.escape(city), seg, re.M)
        if not m:
            raise SystemExit("no line for %s in Hydro-Québec's table" % city)
        v = [float(x) for x in m.group(2).split()]
        out[prov] = (re.sub(r"\s+", " ", m.group(0)).strip(), [v[1], v[2]])  # v[0] residential, v[1] 10,000 kWh, v[2] 100,000 kWh
    return out


def build():
    csd = _csd()
    bps = json.load(gzip.open(BPS, "rt", encoding="utf-8"))
    pts = []
    for name, o in bps["orgs"].items():
        if not (o.get("sector") or "").startswith("Municipal") or o.get("subsector") != "Municipality" or UPPER.search(name):
            continue
        hits = csd.get(("ON", core(name)), [])
        if len(hits) != 1 or hits[0]["pop"] <= 0:
            continue
        kwh = sum(g["kwh"] for g in o["groups"].values())
        pts.append({"name": name, "csd": hits[0]["code"], "csd_name": hits[0]["name"], "pop": hits[0]["pop"], "kwh": kwh, "per_resident": round(kwh / hits[0]["pop"], 1)})
    classes = []
    for lo, hi in CLASSES:
        v = sorted(p["per_resident"] for p in pts if lo <= p["pop"] < hi)
        q = statistics.quantiles(v, n=4) if len(v) >= 4 else None
        classes.append({"lo": lo, "hi": hi, "n": len(v), "p25": round(q[0], 1) if q else None, "median": round(q[1], 1) if q else None})
    prices = hq_city_prices()
    meta = dict(bps["meta"])
    out = {"built": __import__("datetime").date.today().isoformat(), "classes": classes, "points": sorted(pts, key=lambda p: p["pop"]),
           "prices": {k: {"line": v[0], "c_per_kwh": v[1], "city": CITY[k][0], "distributor": CITY[k][1]} for k, v in prices.items()},
           "hq_pdf": meta.get("hq_pdf"), "hq_title": meta.get("hq_title"), "bps_year": 2024, "bps_page": meta.get("dataset_page"), "bps_quote": meta.get("regulation_quote"),
           "census_url": CENSUS_URL, "census_file": CENSUS_FILE}
    with gzip.open(OUT, "wt", encoding="utf-8") as f:
        json.dump(out, f, ensure_ascii=False)
    print("%d Ontario municipalities matched to their census subdivision; classes: %s" % (len(pts), classes))
    print("prices:", {k: v["c_per_kwh"] for k, v in out["prices"].items()})


_D, _C = None, None


def load():
    global _D, _C
    if _D is None:
        try:
            _D = json.load(gzip.open(OUT, "rt", encoding="utf-8"))
            _C = _csd()
        except OSError:
            _D, _C = {}, {}
    return _D


def match(name, province, website=""):
    """(the census subdivision, population) of a municipality named on a row — a name with a word of its kind ("Ville de Mirabel", "City of Victoria",
    "Municipalité de Lambton"), or its bare name when its own site's domain spells it and nothing else (fredericton.ca); one subdivision of that
    name in its province, or nothing"""
    load()
    if not _D or province not in CITY:
        return None
    n = (name or "").strip()
    if not n or UPPER.search(fold(n)):
        return None
    c = core(n)
    if len(c) < 3:
        return None
    if not KIND.search(fold(n)):
        dom = re.sub(r"^https?://(?:www\.)?", "", (website or "").lower()).split("/")[0]
        lab = re.sub(r"[^a-z0-9]", "", fold(dom.split(".")[0]).replace(" ", "")) if dom else ""
        lab = re.sub(r"^(?:cityof|townof|villageof|townshipof|municipalityof|villede|ville|municipalite|rmof|rm)", "", lab)
        lab = re.sub(r"(?:township|municipality|village|town|city)$", "", lab)
        if lab != c:
            return None  # a bare place name is a municipality only on the municipality's own site
    hits = _C.get((province, c), [])
    if len(hits) != 1:
        return None
    return hits[0]


def estimate(pop, province):
    """{p25, median: $ a month; kwh_p25, kwh_median: kWh a month; class; price} for a municipality of pop residents in the province, or None"""
    d = load()
    if not d or province not in d.get("prices", {}) or not pop:
        return None
    cl = next((c for c in d["classes"] if c["lo"] <= pop < c["hi"]), None)
    if not cl or not cl.get("p25"):
        return None
    pr = d["prices"][province]
    cents = min(pr["c_per_kwh"])
    k25, kmed = pop * cl["p25"] / 12.0, pop * cl["median"] / 12.0
    return {"kwh_p25": k25, "kwh_median": kmed, "p25": k25 * cents / 100.0, "median": kmed * cents / 100.0, "class": cl, "cents": cents, "price": pr}


def _r(v):
    return format(int(round(v, -3 if v >= 100000 else -2 if v >= 10000 else -1)), ",")


def sentence(m, e, province):
    """the row's bill_amount_calculated: the amount at the lower quartile, the median beside it, and every figure it rests on"""
    d = load()
    cl, pr = e["class"], e["price"]
    hi = "or more" if cl["hi"] >= 10 ** 9 else "to %s" % format(cl["hi"] - 1, ",")
    return ("estimated — about $%s a month before tax for the electricity of the municipality's own facilities (about $%s at the median), each billed on its "
            "account by this distributor: %s had %s residents (Statistics Canada, 2021 Census, table 98-10-0002-01, census subdivision %s: %s); the %d Ontario "
            "municipalities of %s %s residents that report their facilities' grid electricity under O. Reg. 25/23 (%s data: %s) bought %s kWh a resident a year at "
            "their lower quartile and %s at their median — about %s and %s kWh a month here; priced at %.2f ¢ a kWh, the lower of Hydro-Québec's average prices for "
            "%s at 10,000 and 100,000 kWh a month (%s: “%s”; excluding taxes; %s). What a municipality reports is what Table 1 of the regulation lists (its "
            "offices, libraries, recreation and community centres, ambulance, fire and police stations, garages, water and sewage facilities and parking garages): its "
            "street lighting is not among them, so the use is a floor. Whose name is on each account is not published"
            % (_r(e["p25"]), _r(e["median"]), m["name"], format(m["pop"], ","), m["code"], d["census_url"], cl["n"], format(cl["lo"], ","), hi, d["bps_year"],
               d["bps_page"], format(cl["p25"], ",.0f"), format(cl["median"], ",.0f"), format(int(round(e["kwh_p25"])), ","), format(int(round(e["kwh_median"])), ","),
               e["cents"], pr["city"], d["hq_title"], pr["line"], d["hq_pdf"]))


if __name__ == "__main__":
    a = sys.argv[1:]
    if a[:1] == ["build"]:
        build()
    elif a[:1] == ["show"] and len(a) >= 3:
        m = match(a[1], a[2], a[3] if len(a) > 3 else "")
        print(m)
        if m:
            e = estimate(m["pop"], a[2])
            print(e and sentence(m, e, a[2]))
    else:
        print(__doc__)
