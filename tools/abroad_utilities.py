#!/usr/bin/env python3
"""Electric utilities abroad that Canadian companies own, as billers by where the organisation is (owner, 2026-11-13 09:46 EST: "The U.S. power
company owned by Canadian company counts as Canadian vendor"; AGENTS.md rule 18). No AI.

The rule is Canada's (rule 13, tools/by_location.py): electricity at an address is distributed and billed by one body, every month, on an
invoice, paid through a bank; the biller is certain for the address, whose name is on the account is not published. Abroad the biller is a
utility a Canadian company owns (the parent's own page is quoted on the row). Households are never rows; an organisation needs its own site,
its own role mailbox and its own printed address.

Territories. The retail service territories of U.S. electric utilities, as Homeland Infrastructure Foundation-Level Data published them (EIA-861,
FERC-714, the utilities' own maps; public domain), served by the Pacific Northwest National Laboratory's ArcGIS server (the HIFLD Open portal
closed in 2025). A ZIP code area (U.S. Census Bureau ZCTA, cartographic boundaries 2020) counts as one utility's when at least 98 % of its area
lies in that utility's territory and no other retail territory covers more than 2 % of it — a ZIP shared with a cooperative, a municipal utility
or another company names nobody (as a postal area shared by two distributors does in Ontario). Caribbean utilities serve whole islands.

  territories            the target utilities' polygons and every other retail territory that touches them -> DIR/territories.geojson.gz
  zips --zcta ZIP        -> tools/data/us_zip_billers.csv (zip, biller, share, other_share, other)
  places --release R     Overture Maps places with a website whose ZIP code is in the table, and the Caribbean islands' places
                         -> DIR/places_sites.csv.gz (dom, name, zip, biller, objects)
  leads --stamp S        each site not on file yet -> data/incoming/claude/lead_shards/leads_usb_<S>.gz (no vendor on the lead: the mailbox
                         crawl reads the site; the ranker's rows by where the organisation is make the row once its own pages give a
                         mailbox and an address)
"""
import argparse, collections, csv, glob, gzip, hashlib, io, json, os, re, sys, time, urllib.parse, urllib.request, zipfile

csv.field_size_limit(1 << 30)
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
INC = os.path.join(ROOT, "data/incoming/claude")
DIR = os.path.join(INC, "abroad")
SHARDS = os.path.join(INC, "lead_shards")
ZIPS = os.path.join(ROOT, "tools", "data", "us_zip_billers.csv")
BILLERS = os.path.join(ROOT, "tools", "data", "billers_abroad.json")
TERR = os.path.join(DIR, "territories.geojson.gz")
SITES = os.path.join(DIR, "places_sites.csv.gz")
UA = "canada-contracts-hub-crawler/1.0 (+https://github.com/mohamedbiranesy-gif/canada-contracts-hub)"
TODAY = time.strftime("%Y-%m-%d")
LAYER = "https://eedgis.pnnl.gov/arcgis/rest/services/Hosted/Electric_Service_Territories/FeatureServer/0"
# the territory layer's id of each target utility (EIA utility id), checked 2026-11-13 against the layer's own records
TARGETS = {"18454": "us_tampa_electric", "24211": "us_tep", "19728": "us_uns_electric", "3249": "us_central_hudson", "7601": "us_green_mountain_power",
           "1179": "us_versant", "5860": "us_empire_district", "26510": "us_granite_state", "57483": "us_calpeco"}
SHARE, OTHER = 0.98, 0.02
# A state's own map of franchise areas replaces the HIFLD polygons where one is published: then the target and every neighbour come from it alone
# (Vermont's Public Service Department: "VT Data - Electric Utility Franchise Areas", the seventeen franchise holders of the state)
STATE_LAYERS = {"us_green_mountain_power": dict(state="VT", url="https://maps.vcgi.vermont.gov/arcgis/rest/services/PSD_services/OPENDATA_PSD_LAYERS_SP_NOCACHE_v1/MapServer/40",
                                                 target_field="COMPANY", target_value="GMP", name_field="COMPANYNAM",
                                                 source="the Vermont Public Service Department's electric utility franchise areas")}
# The layer's polygons are of two qualities. A target drawn from the utility's own service map (its source says so: TECO's outage map, TEP's
# UniSource maps, Central Hudson's storm map, Green Mountain Power's service-area map, the California Energy Almanac) is precise; so is any address inside it. Several NEIGHBOURS are county fills (Duke Energy Florida's polygon covers 91 % of Tampa
# Electric's territory, Ajo Improvement Co's 97 % of Tucson Electric Power's): a neighbour that covers a quarter or more of a precise target's
# territory is such a fill and is not a real enclave; federal power marketers (WAPA, the Bureau of Indian Affairs' irrigation projects) sell no
# retail service inside these territories. A target drawn from county or town fills (Versant, Granite State, UNS Electric) keeps every
# cooperative and municipal neighbour as an exclusion (the safe side); only federal marketers and investor-owned fills over half of it are set aside.
# (Empire District's one feature in the layer is a county fill of Benton County, Arkansas — the City of Bentonville's municipal polygon is the very
# same area — and its Missouri, Kansas and Oklahoma territory is not in the layer: treated as a fill, so its neighbours stay exclusions)
# 2026-11-13 16:30Z: a utility's own list of the towns it serves replaces a coarse HIFLD polygon (tools/data/utility_town_lists.json: Versant's
# "Towns in our Service Districts", Liberty's NHPUC No. 23 tariff "Service Area"). Only the towns the list gives as served whole are taken — a town
# marked as served in part is left out — and their Census Bureau county subdivision polygons (cartographic boundaries 2020) make the target. A target
# made so is drawn from the utility's own words: it is treated as PRECISE (a neighbour over a quarter of it is a county fill; every other neighbour
# stays an exclusion — a municipal utility inside a listed town, Houlton Water Company in Houlton, still keeps its ZIP areas out).
TOWN_LISTS_FILE = os.path.join(ROOT, "tools", "data", "utility_town_lists.json")
COUSUB_URL = "https://www2.census.gov/geo/tiger/GENZ2020/shp/cb_2020_%s_cousub_500k.zip"
PLACE_URL = "https://www2.census.gov/geo/tiger/GENZ2020/shp/cb_2020_%s_place_500k.zip"  # a list that names cities ("layer": "place"): the incorporated places
PRECISE = {"us_tampa_electric", "us_tep", "us_central_hudson", "us_green_mountain_power", "us_calpeco"}  # (Green Mountain Power: from Vermont's own map)
NOT_RETAIL = re.compile(r"WAPA|WESTERN AREA POWER|IRR(?:IGATION)? PROJ|USBIA|BUREAU OF INDIAN|POWER MARKETER|BONNEVILLE", re.I)


def get(url, timeout=120):
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    for i in range(4):
        try:
            with urllib.request.urlopen(req, timeout=timeout) as r:
                return r.read()
        except Exception as e:
            print("  %s (attempt %d): %s" % (url[:120], i + 1, e), flush=True)
            time.sleep(5 * (i + 1))
    raise SystemExit("the territory layer could not be read")


def query(where, geometry=True, extra=""):
    """every feature of the layer matching `where`, in WGS84, paged (the server returns at most 2,000 a request)"""
    out, off = [], 0
    while True:
        q = {"where": where, "outFields": "objectid,id,name,state,type,holding_co,customers,source,year", "returnGeometry": "true" if geometry else "false",
             "outSR": "4326", "f": "geojson" if geometry else "json", "resultOffset": str(off), "resultRecordCount": "200"}
        if extra:
            q.update(dict(urllib.parse.parse_qsl(extra)))
        d = json.loads(get(LAYER + "/query?" + urllib.parse.urlencode(q)))
        feats = d.get("features") or []
        out += feats
        if len(feats) < 200:
            return out
        off += len(feats)


def cmd_territories(a):
    os.makedirs(DIR, exist_ok=True)
    ids = ",".join("'%s'" % i for i in TARGETS)
    tg = query("id in (%s)" % ids)
    print("target utilities: %d features — %s" % (len(tg), sorted({(f["properties"]["name"], f["properties"]["state"]) for f in tg})), flush=True)
    # every other retail territory that touches a target's bounding box (cooperatives, municipal utilities, other companies)
    from shapely.geometry import shape
    others, seen = [], set()
    for f in tg:
        x0, y0, x1, y1 = shape(f["geometry"]).bounds
        env = json.dumps({"xmin": x0, "ymin": y0, "xmax": x1, "ymax": y1, "spatialReference": {"wkid": 4326}})
        for g in query("1=1", extra=urllib.parse.urlencode({"geometry": env, "geometryType": "esriGeometryEnvelope", "inSR": "4326",
                                                          "spatialRel": "esriSpatialRelIntersects"})):
            oid = g["properties"].get("objectid")
            if oid in seen or str(g["properties"].get("id")) in TARGETS:
                continue
            seen.add(oid)
            others.append(g)
    for f in tg:
        f["properties"]["_target"] = TARGETS[str(f["properties"]["id"])]
    # a state's own franchise map: the target's polygon and its neighbours from it (the HIFLD target feature is replaced)
    for key, L in STATE_LAYERS.items():
        q = {"where": "1=1", "outFields": "*", "returnGeometry": "true", "outSR": "4326", "f": "geojson"}
        sl = json.loads(get(L["url"] + "/query?" + urllib.parse.urlencode(q))).get("features") or []
        if not any(str(x["properties"].get(L["target_field"])) == L["target_value"] for x in sl):
            print("state layer %s: no feature of the target — the HIFLD polygon stays" % L["state"], flush=True)
            continue
        tg = [f for f in tg if f["properties"].get("_target") != key]
        for x in sl:
            p0 = x.get("properties") or {}
            is_t = str(p0.get(L["target_field"])) == L["target_value"]
            x["properties"] = {"name": p0.get(L["name_field"]) or "", "type": "STATE FRANCHISE AREA", "state": L["state"], "_state_layer": L["state"], "source": L["source"]}
            if is_t:
                x["properties"]["_target"] = key
        others += [x for x in sl if not x["properties"].get("_target")]
        tg += [x for x in sl if x["properties"].get("_target")]
        print("state layer %s: %d franchise areas (target %s from it)" % (L["state"], len(sl), key), flush=True)
    try:
        town_lists = json.load(open(TOWN_LISTS_FILE, encoding="utf-8"))
    except (OSError, ValueError):
        town_lists = {}
    if town_lists:
        import shapefile
        from shapely.geometry import shape as _shape, mapping as _mapping
        from shapely.ops import unary_union as _union
        for key, T in town_lists.items():
            is_place = T.get("layer") == "place"
            want = {(n.lower(), "" if is_place else c.lower()) for n, c in T["whole"]}
            z = zipfile.ZipFile(io.BytesIO(get((PLACE_URL if is_place else COUSUB_URL) % T["state_fips"], timeout=300)))
            base = [n for n in z.namelist() if n.endswith(".shp")][0][:-4]
            r = shapefile.Reader(shp=io.BytesIO(z.read(base + ".shp")), shx=io.BytesIO(z.read(base + ".shx")), dbf=io.BytesIO(z.read(base + ".dbf")))
            fl = [f_[0] for f_ in r.fields[1:]]
            ni, ci = fl.index("NAME"), (None if is_place else fl.index("NAMELSADCO"))
            polys, got = [], set()
            for sr in r.iterShapeRecords():
                nm, co = sr.record[ni], ("" if is_place else re.sub(r"\s+County$", "", sr.record[ci]))
                if (nm.lower(), co.lower()) in want:
                    polys.append(_shape(sr.shape.__geo_interface__).buffer(0)); got.add((nm.lower(), co.lower()))
            if not polys:
                print("town list %s: no town matched — the HIFLD polygon stays" % key, flush=True)
                continue
            tg = [f for f in tg if f["properties"].get("_target") != key]
            tg.append({"type": "Feature", "geometry": _mapping(_union(polys)),
                       "properties": {"name": key, "type": "UTILITY'S OWN TOWN LIST", "state": T["state"], "_target": key, "_town_list": True,
                                      "source": "%s (%s, read %s); Census Bureau county subdivisions 2020" % (T["source"], T["url"], T["read"])}})
            print("town list %s: %d of %d towns served whole matched (%s)" % (key, len(got), len(want), ", ".join(sorted(n for n, c in want - got))[:300] or "all"), flush=True)
    with gzip.open(TERR, "wt", encoding="utf-8") as fh:
        json.dump({"type": "FeatureCollection", "read": TODAY, "source": LAYER, "features": tg + others}, fh)
    print("territories: %d target features, %d other retail territories touching them -> %s" % (len(tg), len(others), TERR), flush=True)


def cmd_zips(a):
    import shapefile
    from shapely.geometry import shape
    from shapely.strtree import STRtree
    from shapely.ops import unary_union
    with gzip.open(TERR, "rt", encoding="utf-8") as fh:
        fc = json.load(fh)
    tgt = collections.defaultdict(list)
    oth = []
    state_tg, state_oth = set(), collections.defaultdict(set)
    town_tg = set()
    for f in fc["features"]:
        g = shape(f["geometry"]).buffer(0)
        if f["properties"].get("_target"):
            tgt[f["properties"]["_target"]].append(g)
            if f["properties"].get("_town_list"):
                town_tg.add(f["properties"]["_target"])
            if f["properties"].get("_state_layer"):
                state_tg.add(f["properties"]["_target"])
        else:
            if f["properties"].get("_state_layer"):
                state_oth[f["properties"]["_state_layer"]].add(len(oth))
            oth.append((g, "%s (%s, %s)" % (f["properties"].get("name"), f["properties"].get("type"), f["properties"].get("state"))))
    tgt = {k: unary_union(v) for k, v in tgt.items()}
    # a neighbour that is a county fill for a target is no exclusion for that target (see PRECISE above); counted per target
    fills = collections.defaultdict(set)
    for i, (g, nm) in enumerate(oth):
        for k, t in tgt.items():
            if not g.intersects(t):
                continue
            if k in STATE_LAYERS and k in state_tg:
                if i not in state_oth.get(STATE_LAYERS[k]["state"], set()):
                    fills[k].add(i)  # the state's own map decides: the HIFLD polygons around this target are not used
                continue
            ov = g.intersection(t).area / t.area
            if NOT_RETAIL.search(nm) or "FEDERAL" in nm:
                fills[k].add(i)
            elif (k in PRECISE or k in town_tg) and ov >= 0.25:
                fills[k].add(i)
            # (2026-11-13 16:15Z: an investor-owned neighbour over half of a target NOT drawn from its own maps is no longer set aside. Liberty's
            # Granite State polygon is itself a county fill — it covers Nashua, Manchester and Keene, which Eversource's PSNH serves — and
            # setting PSNH aside gave Liberty 54 ZIP areas it does not serve. A coarse target keeps every neighbour as an exclusion.)
    for k in sorted(tgt):
        print("%-26s neighbours set aside as county fills or non-retail: %s" % (k, sorted({oth[i][1] for i in fills[k]})[:8]), flush=True)
    tree = STRtree([g for g, _ in oth])
    z = zipfile.ZipFile(a.zcta)
    base = [n for n in z.namelist() if n.endswith(".shp")][0][:-4]
    r = shapefile.Reader(shp=io.BytesIO(z.read(base + ".shp")), shx=io.BytesIO(z.read(base + ".shx")), dbf=io.BytesIO(z.read(base + ".dbf")))
    fields = [f[0] for f in r.fields[1:]]
    zi = fields.index("ZCTA5CE20")
    allb = unary_union(list(tgt.values()))
    x0, y0, x1, y1 = allb.bounds
    rows, n = [], collections.Counter()
    for sr in r.iterShapeRecords():
        bx = sr.shape.bbox
        if bx[2] < x0 or bx[0] > x1 or bx[3] < y0 or bx[1] > y1:
            continue
        zg = shape(sr.shape.__geo_interface__).buffer(0)
        if zg.is_empty or not zg.intersects(allb):
            continue
        za = zg.area
        best, share = None, 0.0
        for k, g in tgt.items():
            if zg.intersects(g):
                s = zg.intersection(g).area / za
                if s > share:
                    best, share = k, s
        if not best or share < 0.5:
            continue
        osh, oname = 0.0, ""
        for i in tree.query(zg):
            if int(i) in fills[best]:
                continue
            g, nm = oth[int(i)]
            if zg.intersects(g):
                s = zg.intersection(g).area / za
                if s > osh:
                    osh, oname = s, nm
        for k, g in tgt.items():  # another target utility in the same ZIP area is "another" too
            if k != best and zg.intersects(g):
                s = zg.intersection(g).area / za
                if s > osh:
                    osh, oname = s, k
        ok = share >= SHARE and osh <= OTHER
        n[(best, "kept" if ok else "shared or edge")] += 1
        rows.append((sr.record[zi], best, round(share, 4), round(osh, 4), oname, ok))
    os.makedirs(os.path.dirname(ZIPS), exist_ok=True)
    with open(ZIPS, "w", encoding="utf-8", newline="") as f:
        w = csv.writer(f)
        w.writerow(["zip", "biller", "share", "other_share", "other", "kept"])
        for x in sorted(rows):
            w.writerow(x[:5] + ("yes" if x[5] else "no",))
    for k in sorted(tgt):
        print("%-26s ZIP areas kept %5d, shared or at the edge %5d" % (k, n[(k, "kept")], n[(k, "shared or edge")]), flush=True)
    print("ZIP table -> %s (%d kept of %d)" % (ZIPS, sum(1 for x in rows if x[5]), len(rows)), flush=True)


OVERTURE_BUCKET = "https://overturemaps-us-west-2.s3.amazonaws.com"
# the Caribbean utilities serve whole islands; a place's country (Overture's address) and, where one country has two utilities, its island
#   KY Grand Cayman only (Cayman Brac and Little Cayman: Cayman Brac Power & Light) — Caribbean Utilities Company (Fortis)
#   TC the Turks and Caicos Islands served by FortisTCI (Providenciales, the Caicos islands, Grand Turk, Salt Cay)
#   BB Barbados — The Barbados Light & Power Company (Emera)          BM Bermuda — Bermuda Electric Light Company (Algonquin)
#   BS Grand Bahama only (New Providence and the Family Islands: Bahamas Power and Light) — Grand Bahama Power Company (Emera)
CARIB = {"KY": "ky_caribbean_utilities", "TC": "tc_fortistci", "BB": "bb_blpc", "BM": "bm_belco", "BS": "bs_grand_bahama_power"}
CARIB_NOT = {"KY": re.compile(r"cayman brac|little cayman", re.I)}
CARIB_ONLY = {"BS": re.compile(r"freeport|grand bahama|lucaya|eight mile rock|west end|holmes rock|pinder|high rock|mcleans? town|sweeting", re.I)}
# the boxes of the targets' states and the islands (Overture's release is sorted in space: only the files that touch them are read)
BOXES = [(-83.5, 24.4, -79.8, 31.0), (-114.9, 31.3, -109.0, 37.0), (-79.8, 40.5, -71.8, 45.0), (-73.5, 42.7, -66.9, 47.5), (-124.5, 36.5, -119.0, 42.0),
         (-81.5, 19.2, -79.7, 19.8), (-72.5, 21.0, -71.0, 22.1), (-59.7, 13.0, -59.4, 13.4), (-65.0, 32.2, -64.6, 32.45), (-79.2, 26.4, -77.8, 26.9)]


def cmd_places(a):
    import duckdb
    import ap_crawler as C
    zips = {}
    for r in csv.DictReader(open(ZIPS, encoding="utf-8", newline="")):
        if r["kept"] == "yes":
            zips[r["zip"]] = r["biller"]
    ls = lambda prefix: urllib.request.urlopen(urllib.request.Request("%s/?list-type=2&prefix=%s&delimiter=/" % (OVERTURE_BUCKET, urllib.parse.quote(prefix, safe="/=")),
                                                                      headers={"User-Agent": UA}), timeout=120).read().decode("utf-8", "replace")
    rel = sorted(re.findall(r"<Prefix>(release/[0-9]{4}-[0-9]{2}-[0-9]{2}\.[0-9]+/)</Prefix>", ls("release/")))
    release = a.release or rel[-1]
    keys = re.findall(r"<Key>([^<]+\.parquet)</Key>", ls(release + "theme=places/type=place/"))
    con = duckdb.connect()
    con.execute("INSTALL httpfs; LOAD httpfs; SET enable_progress_bar=false;")
    box = " OR ".join("(bbox.xmin < %s AND bbox.xmax > %s AND bbox.ymin < %s AND bbox.ymax > %s)" % (x1, x0, y1, y0) for x0, y0, x1, y1 in BOXES)
    files = []
    for k in keys:
        f = "%s/%s" % (OVERTURE_BUCKET, k)
        if con.execute("SELECT count(*) FROM read_parquet('%s') WHERE %s" % (f, box)).fetchone()[0]:
            files.append(f)
    print("Overture %s: %d place files, %d touch the territories' boxes" % (release, len(keys), len(files)), flush=True)
    con.execute("CREATE TEMP TABLE z(zip VARCHAR)")
    con.executemany("INSERT INTO z VALUES (?)", [(z_,) for z_ in zips])
    rows = con.execute("""SELECT names."primary", websites[1], addresses[1].country, left(coalesce(addresses[1].postcode, ''), 5), coalesce(addresses[1].locality, ''),
                                 coalesce(addresses[1].freeform, ''), coalesce(operating_status, '')
                          FROM read_parquet([%s]) WHERE (%s) AND websites IS NOT NULL AND len(websites) > 0
                            AND ((addresses[1].country = 'US' AND left(coalesce(addresses[1].postcode, ''), 5) IN (SELECT zip FROM z))
                                 OR addresses[1].country IN ('KY', 'TC', 'BB', 'BM', 'BS'))""" % (", ".join("'%s'" % f for f in files), box)).fetchall()
    best, n = {}, collections.Counter()
    if not getattr(a, "no_fsq", False):
        # 2026-11-13: and Foursquare Open Source Places (Apache 2.0; tools/fsq_places.py reads the same release) — its places of the same ZIP areas
        # and islands, each with the closing date the dataset keeps (a place closed is left out); the e-mail column is never read
        try:
            import fsq_places as FSQ
            frel, ffiles = FSQ.release_files("")
            fcon = FSQ._con()
            fcon.execute("CREATE TEMP TABLE z(zip VARCHAR)")
            fcon.executemany("INSERT INTO z VALUES (?)", [(z_,) for z_ in zips])
            frows = fcon.execute("""SELECT name, website, country, left(coalesce(postcode, ''), 5), coalesce(locality, ''), coalesce(address, '') || ' ' || coalesce(region, ''), ''
                                    FROM read_parquet([%s]) WHERE website IS NOT NULL AND website <> '' AND date_closed IS NULL
                                      AND ((country = 'US' AND left(coalesce(postcode, ''), 5) IN (SELECT zip FROM z)) OR country IN ('KY', 'TC', 'BB', 'BM', 'BS'))"""
                                 % ", ".join("'%s'" % f for f in ffiles)).fetchall()
            print("Foursquare %s: %d places with a website in the ZIP areas and islands" % (frel, len(frows)), flush=True)
            rows = list(rows) + list(frows)
        except Exception as e:
            print("Foursquare places not read: %s" % e, flush=True)
    for name, site, cc, z_, loc, free, st in rows:
        if st and st != "open":
            n["closed"] += 1
            continue
        if cc == "US":
            b = zips.get(z_)
        else:
            if (CARIB_NOT.get(cc) and CARIB_NOT[cc].search(loc + " " + free)) or (CARIB_ONLY.get(cc) and not CARIB_ONLY[cc].search(loc + " " + free)):
                n["island of another utility (%s)" % cc] += 1
                continue
            b = CARIB[cc]
        h = (urllib.parse.urlparse(site if "://" in site else "http://" + site).hostname or "").lower()
        h = h[4:] if h.startswith("www.") else h
        if not h or "." not in h:
            continue
        d = C.registrable(h)
        o = best.setdefault(d, {"dom": d, "name": name or "", "zip": z_ if cc == "US" else cc, "biller": b, "objects": 0, "billers": set()})
        o["objects"] += 1
        o["billers"].add(b)
        n[b] += 1
    os.makedirs(DIR, exist_ok=True)
    kept = 0
    with gzip.open(SITES, "wt", encoding="utf-8", newline="") as f:
        w = csv.writer(f)
        w.writerow(["dom", "name", "zip", "biller", "objects"])
        for d, o in sorted(best.items()):
            if len(o["billers"]) > 1 or o["objects"] > 50:
                continue  # a chain across territories, or a brand's site listed by many places: no one place is the organisation
            w.writerow([d, o["name"], o["zip"], o["biller"], o["objects"]])
            kept += 1
    print("places with a website in the territories: %d rows -> %d registrable domains, %d kept (single territory, at most 50 places) -> %s; %s"
          % (len(rows), len(best), kept, SITES, dict(n)), flush=True)


def cmd_leads(a):
    """each place site of the territories that no lead, no delivered row and no mailbox row has -> a lead with no vendor: the mailbox crawl reads
    the site; the ranker makes the row by where the organisation is once its own pages give a mailbox and an address in the territory"""
    import lead_store as LS
    import ap_crawler as C
    billers = {b["key"]: b for b in json.load(open(BILLERS, encoding="utf-8"))}
    leads, det = LS.load(details=False)
    have = set()
    for r in leads.values():
        h = (urllib.parse.urlparse(r.get("website") or "").hostname or "").lower()
        if h:
            have.add(C.registrable(h[4:] if h.startswith("www.") else h))
    for pth in glob.glob(os.path.join(ROOT, "data/incoming/*/*buyer_ap_results*.csv")):
        try:
            for r in csv.DictReader(open(pth, encoding="utf-8", errors="replace", newline="")):
                if (r.get("ap_email") or "").strip():
                    h = (urllib.parse.urlparse(r.get("evidence_url") or "").hostname or "").lower()
                    if h:
                        have.add(C.registrable(h[4:] if h.startswith("www.") else h))
        except Exception:
            pass
    snap = LS.snapshot(leads, {})
    new_leads, new_det, n = {}, {}, collections.Counter()
    with gzip.open(SITES, "rt", encoding="utf-8", newline="") as fh:
        for r in csv.DictReader(fh):
            d, b = r["dom"], r["biller"]
            if b not in billers:
                n["utility not in the billers file (ownership not read on the parent's own page)"] += 1
                continue
            if d in have:
                n["site already on file"] += 1
                continue
            k = "lead:" + hashlib.sha1(("%s|place:abroad" % d).encode()).hexdigest()[:16]
            new_leads[k] = {"buyer_key": k, "buyer_name": r["name"] or d, "website": "https://%s/" % d, "canadian_vendor_rows": "1", "example_vendor": "",
                            "canada_field_value": "", "evidence_dataset": "Overture Maps places (%s)" % (r.get("zip") or ""), "latest_record_date": TODAY}
            new_det[k] = {"key": k, "platform": "places_abroad", "biller": b, "zip": r.get("zip") or "", "places": r.get("objects") or ""}
            n["lead (%s)" % b] += 1
    leads.update(new_leads)
    nu, nd, ng = LS.save("usb", a.stamp, leads, new_det, snap)
    print("abroad leads: %s; shards written: %d leads, %d details" % (dict(n), nu, nd), flush=True)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("cmd", choices=["territories", "zips", "places", "leads"])
    ap.add_argument("--stamp", default=time.strftime("%Y%m%dT%H%M%S", time.gmtime()))
    ap.add_argument("--zcta", default="")
    ap.add_argument("--release", default="")
    ap.add_argument("--no-fsq", dest="no_fsq", action="store_true")
    a = ap.parse_args()
    {"territories": cmd_territories, "zips": cmd_zips, "places": cmd_places, "leads": cmd_leads}[a.cmd](a)


if __name__ == "__main__":
    main()
