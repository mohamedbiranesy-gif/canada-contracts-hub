#!/usr/bin/env python3
"""Ontario: which licensed electricity distributor serves a postal code (2026-11-11).

Ontario has about sixty distributors, each licensed by the Ontario Energy Board for a service area of its own; a customer in that area is
billed by that distributor (also one that buys its energy from a retailer). A postal area (first three characters) is often shared by two of
them — Hydro One's rural lines run between the towns that kept a utility of their own — so the rule "postal area -> distributor" that serves
the provinces with one utility is wrong here (it had K1E, 97 % Hydro One, as Hydro Ottawa). This tool builds the table by geometry, from three
public files:

  1. the Board's own map of the service areas, open data of the Government of Ontario ("Ontario's Local Distribution Companies (LDCs)
     Boundaries Map", refresh of 2024-09-30, Open Government Licence - Ontario): one polygon per distributor, with its licence number;
  2. the location of every Canadian postal code (GeoNames, postal code dump CA_full, Creative Commons Attribution);
  3. the boundaries of the postal areas (Statistics Canada, 2021 Census forward sortation area boundary file, Statistics Canada Open Licence).

A postal code is given to a distributor when its location lies inside that distributor's area and inside no other, and
  - at least 300 m from the edge of the area (5 km for a rural code — second character 0 — whose location is the post office of a district), or
  - its whole postal area lies in that one service area (99.5 % of the part of it that any distributor serves).
Everything else — a code near an edge, a code the dump does not know in a shared postal area — gets no distributor: no row is made on it.

And from the Board's own page on each distributor (utility performance scorecard, "Contact this Utility"): its address and its site.

  python3 tools/on_ldc_table.py build     writes tools/data/on_postal_ldc.tsv.gz and tools/data/billers_by_location_on.json
  python3 tools/on_ldc_table.py check     the table's counts, and a few postal codes whose distributor is known
  python3 tools/on_ldc_table.py rates     every distributor's bill from the regulator: the Code's rules, the fixed charge and the calculated bill (monthly)
  python3 tools/on_ldc_table.py cities    every place name of the postal-code dump and the one distributor of all its postal codes (tools/data/city_biller.tsv.gz)

Needs: pip install pyshp shapely pyproj. Run by hand or by a workflow when the Board refreshes its map (once a year so far).
"""
import collections, gzip, hashlib, html, io, json, os, re, sys, time, urllib.parse, zipfile

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
TABLE = os.path.join(ROOT, "tools/data/on_postal_ldc.tsv.gz")
BILLERS = os.path.join(ROOT, "tools/data/billers_by_location_on.json")
ABCE = os.path.join(ROOT, "tools/data/pc_abce.txt.gz")
CACHE = os.path.join(ROOT, "out/geo")
LDC_PAGE = "https://data.ontario.ca/dataset/ontario-ldc-boundaries-map"
LDC_ZIP = "https://data.ontario.ca/dataset/ca5c6df5-ca15-4005-be33-c75fcf9bc7e8/resource/42cb3659-8d6a-4a77-b0e5-a9c32736169f/download/energy_ldc_service_boundaries_20240930.zip"
LDC_DATE = "2024-09-30"
GEONAMES = "https://www.geonames.org/export/zip/CA_full.csv.zip"
FSA_LAYER = "https://geo.statcan.gc.ca/geo_wa/rest/services/2021/Cartographic_boundary_files/MapServer/14"
OEB_FIRST = "https://www.oeb.ca/utility-performance-and-monitoring/scorecard/543/view"
OEB_PAGE = "https://www.oeb.ca/utility-performance-and-monitoring/scorecard/%s/view"
URBAN_M, RURAL_M, PURE = 300.0, 5000.0, 0.995
# the Board's page prints no site for these; the site is the one whose contact page was read (2026-11-11: "Mailing Address GrandBridge Energy 39 Glebe Street, P.O. Box 1060 Cambridge, Ontario N1R 5X6")
SITES = {"GrandBridge Energy Inc.": "https://grandbridgeenergy.com/"}
flat = lambda t: re.sub(r"\s+", " ", t).strip()
nkey = lambda s: re.sub(r"[^a-z0-9]+", " ", (s or "").lower()).strip()

# ---- what every Ontario distributor's bill is, from the regulator itself (2026-11-12) ---------------------------------------------------------
# Owner, 2026-11-11 20:04 EST: "what about estimated value per billing cadence and all other … invoice fields". 41 of the 53 distributors had
# nothing but an address. Two sources of the Ontario Energy Board fill every one of them at once:
#  (1) its Distribution System Code, binding on every licensed distributor: a bill every month to each small-business customer, at least
#      20 days to pay it, how a bill is issued and how a payment is made;
#  (2) its file of current rates behind its bill calculator (open data, refreshed monthly): for each distributor and rate zone the fixed
#      monthly charge of the General Service Less Than 50 kW class and every rate by the kilowatt-hour.
# The fixed charge is published: it is the least a bill is ("from $… a month"). What a bill comes to at a stated use is CALCULATED from
# those published rates and labelled so; the use is the one at which the Board's own small-business calculator opens (2,500 kWh a month).
# A distributor read by hand (tools/data/billers_by_location.json) keeps its own sentences: these fill only what it does not have.
DSC = "https://www.oeb.ca/sites/default/files/Distribution_System_Code_20250801_AODA.pdf"
DSC_NAME = "the Ontario Energy Board's Distribution System Code, which binds every licensed distributor"
DSC_Q = {"period": "A distributor shall issue a bill to each non-seasonal residential customer and each general service < 50kW customer on a monthly basis.",
         "terms": "the minimum payment period shall be 20 days from the date on which the bill was issued to the customer.",
         "delivery": "a bill will be deemed to have been issued to a customer: (a) if sent by mail, on the third day after the date on which the bill was printed by the distributor; (b) if made available over the internet",
         "payment": "(a) if paid by mail, three days prior to the date on which the distributor receives the payment; (b) if paid at a financial institution or electronically, on the date on which the payment is acknowledged or recorded by the customer’s financial institution; or (c) if paid by credit card"}
OEB_RATES = "https://www.oeb.ca/_html/calculator/data/BillData_GS.xml"
OEB_RATES_PAGE = "https://oeb.ca/open-data/current-electricity-rates-general-service-50-kw-rate-class"
OEB_CALC = "https://www.oeb.ca/_html/calculator/en/electricity/smallbusiness/"
REF_KWH = 2500


def _rate_rows():
    """[{field: value}] of the Board's file of current small-business rates, one per distributor and rate zone"""
    t = _get(OEB_RATES, "BillData_GS.xml").decode("utf-8", "replace")
    return [dict(re.findall(r"<(\w+)>([^<]*)</\1>", blk)) for blk in re.findall(r"<BillDataRow>(.*?)</BillDataRow>", t, re.S)]


def _estimate(r, kwh=REF_KWH):
    """(the bill before tax at `kwh` a month, the fixed part, the rate by the kilowatt-hour) from one row of the Board's file, or None: energy at
    the Time-of-Use prices in the row's own split of the day, adjusted for line losses, plus the distribution, transmission and regulatory rates"""
    try:
        f = lambda k: float(r[k])
        com = f("EOffP") * f("RPPOffP") + f("EMidP") * f("RPPMidP") + f("EOnP") * f("RPPOnP")
        per = com * f("LF") + f("DC") + f("LF") * (f("Net") + f("Conn") + f("WMSR") + f("RRRP"))
        fixed = f("SC") + f("SSS")
    except (KeyError, ValueError):
        return None
    return fixed + kwh * per, fixed, per


def enrich(ent, read_day=None):
    """adds to each distributor's entry: its licensed name and licence number, the Code's rules on its bill, the fixed charge and the calculated bill"""
    day = read_day or time.strftime("%Y-%m-%d")
    rows = _rate_rows()
    names = sorted((e["table_key"] for e in ent), key=lambda x: -len(nkey(x)))
    alias = {"hearst power distribution co ltd": "Hearst Power Distribution Company Limited"}
    by = collections.defaultdict(list)
    for r in rows:
        k = nkey(r.get("Dist"))
        m = alias.get(k) or next((n for n in names if k == nkey(n) or k.startswith(nkey(n) + " ")), None)
        if m:
            by[m].append(r)
    n = collections.Counter()
    for e in ent:
        nm = e["table_key"]
        lic = re.search(r"\(licence ([A-Z]{2}-\d{4}-\d{4})", e.get("territory") or "")
        e["legal_name"] = nm
        e["legal_name_basis"] = "the name under which the Ontario Energy Board licenses this distributor%s, as the Board prints it on its page for the distributor (%s, read %s)" % (
            (" (licence %s)" % lic.group(1)) if lic else "", e.get("address_url") or "", e.get("address_read") or day)
        if lic:
            e["registration"] = "Ontario Energy Board electricity distribution licence %s (its number in the regulator's public register of licensed distributors)" % lic.group(1)
        e["period"] = "1 monthly"
        e["period_basis"] = "%s: “%s” (s. 2.6.1A; %s)" % (DSC_NAME, DSC_Q["period"], DSC)
        e["delivery"] = "a bill, by mail or made available on line: %s says how — “%s” (s. 2.6.4; %s)" % (DSC_NAME, DSC_Q["delivery"], DSC)
        e["payment"] = ("by mail, at a financial institution or electronically; by credit card where the distributor takes one — the ways %s counts a payment: “%s” (s. 2.6.5; %s)"
                        % (DSC_NAME, DSC_Q["payment"], DSC))
        e["terms"] = "at least 20 days from the day the bill is issued: “%s” (s. 2.6.3 of %s; %s)" % (DSC_Q["terms"], DSC_NAME, DSC)
        e["tax"] = "HST of 13 %% is added: the Board's file of current rates carries it for every Ontario distributor (“<GST>0.13</GST>”, %s)" % OEB_RATES
        zs = [(r, _estimate(r)) for r in by.get(nm, [])]
        zs = [(r, x) for r, x in zs if x]
        if not zs:
            n["no row in the Board's rate file"] += 1
            continue
        zs.sort(key=lambda rx: float(rx[0]["SC"]))
        lo, hi = zs[0], zs[-1]
        zone = lambda r: (r["Dist"] + ((" : " + r["Class"]) if "GENERAL SERVICE LESS THAN 50" not in (r.get("Class") or "") else "")).strip()
        many = (" — the lowest of its %d rate zones or classes; the highest is $%s (%s)" % (len(zs), hi[0]["SC"], zone(hi[0]))) if len(zs) > 1 else ""
        e["amount"] = "from $%s a month" % lo[0]["SC"]
        e["amount_basis"] = ("the fixed monthly charge of its small-business class (service charge and fixed riders), year %s, in the Ontario Energy Board's file of current rates behind its bill "
                             "calculator: “<Dist>%s</Dist>” … “<SC>%s</SC>”%s (%s, described at %s; read %s); the rates by the kilowatt-hour come on top — the organisation's own "
                             "consumption is not published" % (lo[0].get("YEAR") or "", lo[0]["Dist"], lo[0]["SC"], many, OEB_RATES, OEB_RATES_PAGE, day))
        est = sorted(x[0] for r, x in zs)
        e["estimate"] = ("estimated — about $%s a month before tax for %s kWh a month%s: calculated from the Ontario Energy Board's file of current rates for this distributor (%s, read %s) — "
                         "fixed charges $%.2f + %s kWh × %.2f ¢ (energy at the Time-of-Use prices in the file's own split of the day, with line losses; distribution, transmission and "
                         "regulatory rates)%s; %s kWh a month is the use at which the Board's small-business bill calculator opens (%s); the Ontario Electricity Rebate and HST are not "
                         "counted; this organisation's own consumption is not published"
                         % (format(round(est[0]), ","), format(REF_KWH, ","), (" (about $%s in its dearest rate zone)" % format(round(est[-1]), ",")) if len(est) > 1 and round(est[-1]) != round(est[0]) else "",
                            OEB_RATES, day, lo[1][1], format(REF_KWH, ","), 100 * lo[1][2], (" for “%s”" % zone(lo[0])) if len(zs) > 1 else "", format(REF_KWH, ","), OEB_CALC))
        n["distributors with the fixed charge and the calculated bill"] += 1
    print("Ontario distributors' bills from the regulator: %s (of %d); rate rows of the file matched to no distributor on file: %s" % (
        dict(n), len(ent), sorted({r.get("Dist") for r in rows} - {r.get("Dist") for rs in by.values() for r in rs})))
    return ent


def cities():
    """tools/data/city_biller.tsv.gz — for every place name of the postal-code dump, province by province: the distributor of its postal codes when
    one distributor has 98 % of them and another at most 1 % (tools/by_location.py: biller_for_city); '-' for a place no single distributor serves
    (a city split between two, a pocket, Alberta) so that a text naming it is not given another city's distributor"""
    import importlib
    import by_location as BL
    importlib.reload(BL)  # the Ontario table just written
    z = zipfile.ZipFile(io.BytesIO(_get(GEONAMES, "CA_full.csv.zip", big=True)))
    per = collections.defaultdict(collections.Counter)
    with z.open("CA_full.txt") as fh:
        for line in io.TextIOWrapper(fh, encoding="utf-8", errors="replace"):
            q = line.rstrip("\n").split("\t")
            if len(q) < 5 or not q[2] or not q[4]:
                continue
            pc = q[1].replace(" ", "").upper()
            b = BL.biller_for(pc) if len(pc) == 6 and BL.usable(pc) else None
            per[(q[4], BL.norm_city(q[2]))][b["key"] if b else "-"] += 1
    n = collections.Counter()
    with gzip.open(BL.CITY_TABLE, "wt", encoding="utf-8") as f:
        f.write("# province\tplace (normalised)\tdistributor key or -\tshare of the place's postal codes\tpostal codes. Built by tools/on_ldc_table.py cities on %s from the GeoNames "
                "postal code dump CA_full (CC BY) and tools/by_location.py's rules for a postal code.\n" % time.strftime("%Y-%m-%d"))
        for (prov, city), c in sorted(per.items()):
            tot = sum(c.values())
            top, k = c.most_common(1)[0]
            other = sum(v for b, v in c.items() if b not in ("-", top))
            # one distributor has 98 % of the place's postal codes and another has at most 1 % (a code at the edge: Toronto's 14,802 codes
            # include one of Hydro One's and one of Alectra's); a place of one or two postal codes (a rural district) only when all are its
            ok = top != "-" and k / tot >= 0.98 and other <= 0.01 * tot and (tot >= 3 or k == tot)
            f.write("%s\t%s\t%s\t%.3f\t%d\n" % (prov, city, top if ok else "-", k / tot, tot))
            n["places with one distributor" if ok else "places with none, or split"] += 1
    print("places of the postal-code dump by distributor: %s" % dict(n))


def rates():
    """the monthly refresh: the regulator's rate file read again, every distributor's entry updated in place"""
    ent = json.load(open(BILLERS, encoding="utf-8"))
    json.dump(enrich(ent), open(BILLERS, "w", encoding="utf-8"), ensure_ascii=False, indent=1)


def _get(url, name, big=False):
    """a public file, fetched once (robots.txt respected, identified user agent), kept under out/geo/"""
    import ap_crawler as C
    os.makedirs(CACHE, exist_ok=True)
    f = os.path.join(CACHE, name)
    if os.path.exists(f) and os.path.getsize(f) > 0:
        return open(f, "rb").read()
    if not C.allowed(url):
        raise SystemExit("robots.txt refuses %s" % url)
    if big:  # the reader keeps 6 MB of a page; a data file is taken whole, with the same user agent
        import urllib.request
        with urllib.request.urlopen(urllib.request.Request(url, headers={"User-Agent": C.UA}), timeout=300) as r:
            data = r.read()
    else:
        st, ct, data, final = C.fetch(url)
        if st != 200 or not data:
            raise SystemExit("%s answered %s" % (url, st))
    time.sleep(1.0)
    open(f, "wb").write(data)
    return data


def _areas():
    """[(distributor as licensed, licence number, polygon in metres)] from the Board's map"""
    import shapefile, pyproj
    from shapely.geometry import shape
    from shapely.ops import transform
    from shapely import make_valid
    z = zipfile.ZipFile(io.BytesIO(_get(LDC_ZIP, "ldc.zip", big=True)))
    d = os.path.join(CACHE, "ldc")
    os.makedirs(d, exist_ok=True)
    for i in z.infolist():
        if re.fullmatch(r"[A-Za-z0-9_.-]+\.(?:shp|shx|dbf|prj|cpg)", i.filename):  # only the shapefile's own parts, flat names
            open(os.path.join(d, i.filename), "wb").write(z.read(i))
    shp = [f for f in os.listdir(d) if f.endswith(".shp")][0]
    tr = pyproj.Transformer.from_crs("EPSG:4326", "EPSG:3347", always_xy=True)
    out = []
    for sr in shapefile.Reader(os.path.join(d, shp), encoding="utf-8", encodingErrors="replace").shapeRecords():
        rec = sr.record.as_dict()
        out.append((flat(rec.get("EDName") or rec.get("LDC") or ""), flat(rec.get("EDNum") or ""), flat(rec.get("LDC") or ""), make_valid(transform(tr.transform, shape(sr.shape.__geo_interface__)))))
    return out, tr


def _fsas(tr):
    """{postal area: polygon in metres} for Ontario, from Statistics Canada's map service (pages of at most 40 areas)"""
    import ap_crawler as C
    from shapely.geometry import shape
    from shapely.ops import transform
    from shapely import make_valid
    f = os.path.join(CACHE, "on_fsa.geojson")
    if not os.path.exists(f):
        feats, off, n = [], 0, 40
        while True:
            q = {"where": "PRUID='35'", "outFields": "CFSAUID", "outSR": "4326", "f": "geojson", "geometryPrecision": "5", "maxAllowableOffset": "0.0002",
                 "resultOffset": str(off), "resultRecordCount": str(n), "orderByFields": "CFSAUID"}
            st, ct, data, final = C.fetch(FSA_LAYER + "/query?" + urllib.parse.urlencode(q))
            time.sleep(0.7)
            if st != 200 or not data:
                raise SystemExit("the postal-area layer answered %s" % st)
            if len(data) >= 5_999_000:
                n = max(5, n // 2)
                continue
            fs = json.loads(data.decode("utf-8", "replace")).get("features") or []
            feats += fs
            if len(fs) < n:
                break
            off += len(fs)
        os.makedirs(CACHE, exist_ok=True)
        json.dump({"type": "FeatureCollection", "features": feats}, open(f, "w"))
    return {x["properties"]["CFSAUID"]: make_valid(transform(tr.transform, shape(x["geometry"]))) for x in json.load(open(f))["features"]}


def _oeb_contacts():
    """{distributor name as the Board prints it: (address, site, page, quote)} from the Board's page on each distributor"""
    import ap_crawler as C
    def page(u, name):
        return _get(u, name).decode("utf-8", "replace")
    h = page(OEB_FIRST, "oeb_543.html")
    out = {}
    for m in re.finditer(r'<option[^>]*value="(\d+)"[^>]*>([^<]+)</option>', h):
        u = OEB_PAGE % m.group(1)
        t = flat(C.visible(C.quote_attrs(html.unescape(page(u, "oeb_%s.html" % m.group(1))))))
        c = re.search(r"Contact this Utility:\s*(.{5,160}?\b[A-Z]\d[A-Z]\s?\d[A-Z]\d)\b\s*(\S+)?", t)
        if c:
            site = c.group(2) or ""
            site = "" if "@" in site or "." not in site else ("https://" + re.sub(r"^https?://", "", site).rstrip("/") + "/")
            out[html.unescape(m.group(2)).strip()] = (flat(c.group(1)), site, u, "Contact this Utility: " + flat(c.group(1)))
    return out


def build():
    from shapely.geometry import Point
    from shapely.strtree import STRtree
    areas, tr = _areas()
    polys, bounds = [a[3] for a in areas], [a[3].boundary for a in areas]
    tree = STRtree(polys)
    pure = {}
    for code, g in _fsas(tr).items():
        sh = collections.Counter()
        for i in tree.query(g):
            a = g.intersection(polys[int(i)]).area
            if a > 0:
                sh[areas[int(i)][0]] += a
        if sh and sh.most_common(1)[0][1] / sum(sh.values()) >= PURE:
            pure[code] = sh.most_common(1)[0][0]
    z = zipfile.ZipFile(io.BytesIO(_get(GEONAMES, "CA_full.csv.zip", big=True)))
    out, n, abce = {}, collections.Counter(), set()
    with z.open("CA_full.txt") as fh:
        for line in io.TextIOWrapper(fh, encoding="utf-8", errors="replace"):
            q = line.rstrip("\n").split("\t")
            if len(q) > 1 and re.fullmatch(r"[ABCE]\d[ABCE] ?\d[ABCE]\d", q[1].strip().upper()):
                abce.add(q[1].replace(" ", "").upper())  # every province: the codes a colour code could spell (tools/by_location.py: usable)
            if len(q) < 11 or q[4] != "ON":
                continue
            pc = q[1].replace(" ", "").upper()
            if len(pc) != 6:
                continue
            n["postal codes"] += 1
            pt = Point(*tr.transform(float(q[10]), float(q[9])))
            hits = [int(i) for i in tree.query(pt) if polys[int(i)].covers(pt)]
            if len(hits) != 1:
                n["in no service area, or in two"] += 1
                continue  # its postal area decides, when that lies in one service area (the area's own line below)
            i = hits[0]
            if bounds[i].distance(pt) >= (RURAL_M if pc[1] == "0" else URBAN_M) or pure.get(pc[:3]) == areas[i][0]:
                out[pc] = areas[i][0]; n["given a distributor"] += 1
            else:
                n["too near the edge of its service area"] += 1
    if len(abce) > 5000:  # (a dump that lost them is not written over the list on file)
        with gzip.open(ABCE, "wt", encoding="utf-8") as f:
            f.write("# Canadian postal codes whose three letters are all among A, B, C and E — the letters a colour code can spell (#E6E6E6). Built by tools/on_ldc_table.py from the "
                    "GeoNames postal code dump CA_full (CC BY). A code of that shape printed on a page is taken as a postal code only when it is in this list.\n")
            f.write("\n".join(sorted(abce)) + "\n")
    names = sorted({a[0] for a in areas})
    idx = {nm: i for i, nm in enumerate(names)}
    os.makedirs(os.path.dirname(TABLE), exist_ok=True)
    with gzip.open(TABLE, "wt", encoding="utf-8", newline="") as f:
        f.write("# Ontario postal codes and postal areas -> licensed electricity distributor. Built by tools/on_ldc_table.py on %s from: the Ontario Energy Board's map of service areas "
                "(%s, refresh of %s, Open Government Licence - Ontario); postal code locations (GeoNames, %s, CC BY); postal areas (Statistics Canada, 2021 Census boundary file, %s).\n"
                % (time.strftime("%Y-%m-%d"), LDC_PAGE, LDC_DATE, GEONAMES, FSA_LAYER))
        for nm in names:
            f.write("=%d\t%s\n" % (idx[nm], nm))
        for code in sorted(pure):          # a postal area that lies in one service area: every code of it, also one the dump does not know
            f.write("%s\t%d\n" % (code, idx[pure[code]]))
        for pc in sorted(out):
            if pure.get(pc[:3]) != out[pc]:  # the codes of a shared postal area, one by one
                f.write("%s\t%d\n" % (pc, idx[out[pc]]))
    print("Ontario postal codes: %s; postal areas in one service area: %d of them" % (dict(n), len(pure)))
    # the distributors themselves: licence number from the map, address and site from the Board's page on each
    lic = {}
    for nm, num, area, _ in areas:
        lic.setdefault(nm, (num, []))[1].append(area)
    oeb = {nkey(k): (k, v) for k, v in _oeb_contacts().items()}
    ent, missing = [], []
    for nm in names:
        c = oeb.get(nkey(nm))
        if not c:
            missing.append(nm)
            continue
        printed, (addr, site, page, quote) = c
        site = site or SITES.get(nm, "")
        if not site:
            missing.append(nm + " (no site of its own on the Board's page)")
            continue
        num, parts = lic[nm]
        other = [a for a in parts if nkey(a) != nkey(nm)]
        ent.append({"key": "on_" + re.sub(r"[^a-z0-9]+", "_", nm.lower()).strip("_")[:40], "name": nm, "site": site, "table_key": nm, "prefixes": [],
                    "address": addr, "address_url": page, "address_quote": quote, "address_read": time.strftime("%Y-%m-%d"),
                    "address_source": "the Ontario Energy Board's page on this distributor",
                    "territory": ("%s is the electricity distributor licensed by the Ontario Energy Board (licence %s; Ontario Energy Board Act, 1998) for the service area the Board maps for it%s "
                                  "(open data “Ontario's Local Distribution Companies (LDCs) Boundaries Map”, refresh of %s): a customer in its area is billed by it, also one that buys its "
                                  "energy from a retailer; the organisation's postal code is located inside that area and inside no other distributor's (postal code location: GeoNames)"
                                  % (nm, num or "on the Board's register", (" — with the area mapped as “%s”" % "”, “".join(other)) if other else "", LDC_DATE)),
                    "what": "electricity delivered to the premises at the organisation's address", "read": time.strftime("%Y-%m-%d")})
    json.dump(enrich(ent), open(BILLERS, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print("distributors with the Board's page (address, site): %d; mapped but without such a page (no row is made on them): %s" % (len(ent), missing))
    cities()


def load():
    """({postal code or postal area: distributor name}) — empty when the table is not there"""
    out, names = {}, {}
    try:
        with gzip.open(TABLE, "rt", encoding="utf-8") as f:
            for l in f:
                if l.startswith("#"):
                    continue
                a, _, b = l.rstrip("\n").partition("\t")
                if a.startswith("="):
                    names[a[1:]] = b
                elif a:
                    out[a] = names.get(b, "")
    except OSError:
        pass
    return out


def check():
    t = load()
    n = collections.Counter(len(k) for k in t)
    print("postal areas wholly in one service area: %d; postal codes of shared areas, one by one: %d" % (n[3], n[6]))
    print(collections.Counter(t.values()).most_common(12))
    for pc, want in (("M5B1K5", "Toronto Hydro-Electric System Limited"), ("K1G3S4", "Hydro Ottawa Limited"), ("L5N7A6", "Alectra Utilities Corporation"), ("N6A4H6", "London Hydro Inc."),
                     ("K1E3V3", "")):
        got = t.get(pc) or t.get(pc[:3]) or ""
        print("%s -> %s%s" % (pc, got or "no distributor given", "" if got == want else "   (expected: %s)" % (want or "none")))


if __name__ == "__main__":
    {"build": build, "check": check, "rates": rates, "cities": cities}.get(sys.argv[1] if len(sys.argv) > 1 else "", lambda: print(__doc__))()
