#!/usr/bin/env python3
"""Colombian importers (buyers) that bought from an exporter located in Canada, from DIAN import declarations. No AI.

Source: DIAN (Dirección de Impuestos y Aduanas Nacionales de Colombia), "Bases estadísticas de comercio exterior -
Importaciones": declaration-level (tariff-line) microdata, one zip per month holding one xlsx (163-166 columns,
inline strings), ~250-300 MB per zip.
  Landing page: https://www.dian.gov.co/dian/cifras/Paginas/Bases-Estadisticas-de-Comercio-Exterior-Importaciones-y-Exportaciones.aspx
  Files:        https://www.dian.gov.co/dian/cifras/Basesestadisticasimportaciones/{MM}_Importaciones_{YYYY}_{Mes}.zip
  Listing:      https://www.dian.gov.co/dian/cifras/_api/web/GetFolderByServerRelativeUrl('/dian/cifras/Basesestadisticasimportaciones')/Files
Legal-person importer names, NIT, address and phone are published under a court order (Tribunal Administrativo de
Cundinamarca, exp. 25000-23-41-000-2022-00994-00); natural persons are anonymised as "PERSONA NATURAL" (dropped here).

Fields used (exact column names, same in 2023 and 2026 files):
  buyer   NOMBRE_IMPORTADOR (razón social), NIT_IMPORTADOR (+ DIGITO_VERIFI_NIT_IMPORTA), DIRECCION_IMPORTADOR,
          TELEFONO_IMPORTADOR, DEPARTAMENTO_IMPORTADOR, CLASE IMPORTADOR
  vendor  NOMBRE_EXPORTADOR, DIRECCION_EXPORTADOR (truncated by DIAN at ~35 chars), CIUDAD_PAIS_EXPORTADOR,
          CODIGO_PAIS_EXPORTADOR, PAIS_EXPORTADOR, EMAIL_EXPORTADOR
  record  NUMERO_FORMULARIO (= NUM_ACEPTACION_DECLARACION), FECHA_ACEPTACION_DECLARACION (fallback FECHA_PRESENTACION),
          YYYYMMDD; VALOR_FOB_USD
Canada filter: the exporter's own country field. PAIS_EXPORTADOR, accents/case removed, == "CANADA". Checked in the
data: files up to 2024 code Canada as CODIGO_PAIS_EXPORTADOR "149" / PAIS_EXPORTADOR "CANADÁ"; from 2025 on DIAN uses
M49 "124" / "Canadá". PAIS_ORIGEN / PAIS_PROCEDENCIA / PAIS_COMPRA are origin, shipping and purchase countries and
are NOT used. A row whose code is 124/149 but whose name is not Canada (or the reverse) is counted, not kept.
Kept: importer named (not "PERSONA NATURAL", not a natural person), NIT present, record date >= 2023-11-02.
One output line per (importer NIT, normalised exporter name), the most recent declaration kept; row carries all source
columns of that declaration plus record_date and agg_* totals over every declaration of the pair.
Importer website: Wikidata only, exact: (1) an item whose Colombian NIT (P13465) equals NIT_IMPORTADOR, else (2) a
Colombian item (P17 Q739) whose label/alias equals the importer name exactly (case/accent/punctuation-insensitive),
unambiguous, with an official website (P856). One SPARQL request, cached. Otherwise website is left empty.

Run on the Mac (each zip is downloaded once, newest first, into ~/cch-sources/dian/; a monthly rerun fetches 1 file):
  python3 tools/dian_imports.py download  # listing + missing zips from 2023-11 on (~250-300 MB each, one at a time)
  python3 tools/dian_imports.py extract   # parse every cached zip not parsed yet -> ~/cch-sources/dian/extract/
  python3 tools/dian_imports.py build     # aggregate + Wikidata -> ~/cch-leads/socrata_dian.jsonl
  python3 tools/dian_imports.py all       # all three
Counts seen (run of 2026-11-02, 10 monthly files 2025-11 .. 2026-08): 3,295,622 declaration rows, 13,676 with a Canada
exporter (code 124 in every one), 167 dropped as PERSONA NATURAL, 13,509 kept -> 1,740 (importer, exporter) lines,
1,210 distinct importer NITs (1,205 dated 2025-11-02 or later), 18 with a Wikidata website. ~1,400 Canada rows/month.
2023-11 .. 2025-10 files were still downloading; `build` prints the COUNTS line for whatever is cached.
"""
import collections, glob, gzip, html, json, os, re, shutil, sys, time, unicodedata, urllib.parse, urllib.request, zipfile

UA = "canada-contracts-hub-crawler/1.0 (+https://github.com/mohamedbiranesy-gif/canada-contracts-hub)"
BASE = "https://www.dian.gov.co/dian/cifras/Basesestadisticasimportaciones/"
LISTING = ("https://www.dian.gov.co/dian/cifras/_api/web/GetFolderByServerRelativeUrl('/dian/cifras/Basesestadisticasimportaciones')"
           "/Files?$select=Name,Length,TimeLastModified&$top=5000")
SRC = os.path.expanduser("~/cch-sources/dian")
EXTRACT = os.path.join(SRC, "extract")
OUT = os.path.expanduser("~/cch-leads/socrata_dian.jsonl")
WD_CACHE = os.path.join(SRC, "wikidata_co.json")
MIN_DATE = "2023-11-02"
LAST12 = "2025-11-02"
DATASET = "Colombia DIAN - Bases estadísticas de comercio exterior, Importaciones (declaration-level microdata)"
CANADA_FIELD = "PAIS_EXPORTADOR (DIAN Bases estadísticas de comercio exterior - Importaciones)"
CELL = re.compile(rb'<c r="([A-Z]+)\d+"[^>]*?(?:/>|>(.*?)</c>)', re.S)
TAG = re.compile(rb"<[^>]+>")


def norm(s):
    s = unicodedata.normalize("NFKD", s or "").encode("ascii", "ignore").decode().upper()
    return re.sub(r"[^A-Z0-9]+", " ", s).strip()


def cells(row):
    out = {}
    for m in CELL.finditer(row):
        out[m.group(1).decode()] = html.unescape(TAG.sub(b"", m.group(2) or b"").decode("utf-8", "replace"))
    return out


def extract_one(zpath):
    """Stream the sheet of one monthly zip; return (stats, [Canada-exporter rows as dicts of every column])."""
    name = os.path.basename(zpath)
    tmp = os.path.join(SRC, "tmp_" + name[:-4] + ".xlsx")
    with zipfile.ZipFile(zpath) as z:
        member = [m for m in z.namelist() if m.lower().endswith(".xlsx")][0]
        with z.open(member) as src, open(tmp, "wb") as dst:
            shutil.copyfileobj(src, dst, 8 << 20)
    hdr, rows, stats = None, [], collections.Counter()
    try:
        with zipfile.ZipFile(tmp) as x:
            sheet = [m for m in x.namelist() if m.startswith("xl/worksheets/") and m.endswith(".xml")][0]
            with x.open(sheet) as f:
                buf = b""
                while True:
                    chunk = f.read(16 << 20)
                    buf += chunk
                    parts = buf.split(b"</row>")
                    buf = parts.pop() if chunk else b""
                    for p in parts:
                        if b"<row" not in p:
                            continue
                        if hdr is None:
                            c = cells(p[p.find(b"<row"):])
                            if b't="s"' in p:
                                raise SystemExit("shared strings not supported: " + name)
                            hdr = c
                            continue
                        stats["rows"] += 1
                        if b"anad" not in p and b"ANAD" not in p and b">124<" not in p and b">149<" not in p:
                            continue
                        rec = {hdr[k]: v for k, v in cells(p).items() if k in hdr}
                        code, pais = rec.get("CODIGO_PAIS_EXPORTADOR", "").strip(), rec.get("PAIS_EXPORTADOR", "")
                        is_ca = norm(pais) == "CANADA"
                        code_ca = code.split(".")[0] in ("124", "149")
                        if is_ca and not code_ca:
                            stats["name_canada_code_other"] += 1
                        if code_ca and not is_ca:
                            stats["code_124_149_name_other"] += 1
                            stats["code_other_name:" + pais] += 1
                            continue
                        if is_ca:
                            stats["canada_rows"] += 1
                            stats["canada_code:" + code] += 1
                            rec = {v: rec.get(v, "") for v in hdr.values()}
                            rows.append(rec)
                    if not chunk:
                        break
    finally:
        os.remove(tmp)
    stats["columns"] = len(hdr or {})
    return stats, rows


def download():
    """Fetch the folder listing, then every monthly zip from MIN_DATE's month on, newest first, one at a time.
    A zip already cached with the listed size is skipped; a .part is resumed; a .lock dir marks a file in progress."""
    os.makedirs(SRC, exist_ok=True)
    req = urllib.request.Request(LISTING, headers={"User-Agent": UA, "Accept": "application/json;odata=nometadata"})
    data = urllib.request.urlopen(req, timeout=60).read()
    open(os.path.join(SRC, "listing.json"), "wb").write(data)
    files = []
    for x in json.loads(data)["value"]:
        m = re.fullmatch(r"(\d\d)_Importaciones_(\d{4})_\w+\.zip", x["Name"])
        if m and "%s-%s" % (m.group(2), m.group(1)) >= MIN_DATE[:7]:
            files.append(("%s-%s" % (m.group(2), m.group(1)), x["Name"], int(x["Length"])))
    for _, name, size in sorted(files, reverse=True):
        path = os.path.join(SRC, name)
        if os.path.exists(path) and os.path.getsize(path) == size:
            continue
        try:
            os.mkdir(path + ".lock")
        except FileExistsError:
            continue
        try:
            part = path + ".part"
            have = os.path.getsize(part) if os.path.exists(part) else 0
            hdrs = {"User-Agent": UA, "Range": "bytes=%d-" % have} if have else {"User-Agent": UA}
            with urllib.request.urlopen(urllib.request.Request(BASE + urllib.parse.quote(name), headers=hdrs), timeout=120) as r:
                with open(part, "ab" if have and r.status == 206 else "wb") as f:
                    shutil.copyfileobj(r, f, 1 << 20)
            if os.path.getsize(part) == size:
                os.replace(part, path)
            print(time.strftime("%H:%M:%S"), "downloaded", name, os.path.getsize(path if os.path.exists(path) else part), "/", size, flush=True)
        finally:
            os.rmdir(path + ".lock")
        time.sleep(1)


def listing_sizes():
    try:
        return {x["Name"]: int(x["Length"]) for x in json.load(open(os.path.join(SRC, "listing.json")))["value"]}
    except (OSError, ValueError, KeyError):
        return {}


def extract_all():
    os.makedirs(EXTRACT, exist_ok=True)
    sizes = listing_sizes()
    for zpath in sorted(glob.glob(os.path.join(SRC, "*_Importaciones_*.zip")), reverse=True):
        name = os.path.basename(zpath)
        out = os.path.join(EXTRACT, name[:-4] + ".canada.jsonl.gz")
        if os.path.exists(out) or os.path.isdir(zpath + ".lock") or (sizes.get(name) and os.path.getsize(zpath) != sizes[name]):
            continue
        t = time.time()
        stats, rows = extract_one(zpath)
        with gzip.open(out + ".tmp", "wt", encoding="utf-8") as f:
            f.write(json.dumps({"_stats": dict(stats), "_file": name}, ensure_ascii=False) + "\n")
            for r in rows:
                f.write(json.dumps(r, ensure_ascii=False) + "\n")
        os.replace(out + ".tmp", out)
        print(time.strftime("%H:%M:%S"), name, "rows", stats["rows"], "canada", stats["canada_rows"],
              "codes", {k: v for k, v in stats.items() if k.startswith("canada_code:")}, "%.0fs" % (time.time() - t), flush=True)


def ymd(v):
    v = (v or "").strip().split(".")[0]
    return "%s-%s-%s" % (v[:4], v[4:6], v[6:8]) if re.fullmatch(r"20\d{6}", v) else ""


def num(v):
    try:
        return float(v)
    except (TypeError, ValueError):
        return 0.0


def wikidata():
    if not os.path.exists(WD_CACHE):
        q = """SELECT ?item ?nit ?label ?website WHERE {
  { ?item wdt:P13465 ?nit . ?item wdt:P856 ?website . OPTIONAL { ?item rdfs:label ?label FILTER(LANG(?label)="es") } }
  UNION
  { ?item wdt:P17 wd:Q739 ; wdt:P856 ?website . { ?item rdfs:label ?label } UNION { ?item skos:altLabel ?label }
    FILTER(LANG(?label) IN ("es","en","mul")) }
}"""
        url = "https://query.wikidata.org/sparql?" + urllib.parse.urlencode({"query": q, "format": "json"})
        req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept": "application/sparql-results+json"})
        data = json.loads(urllib.request.urlopen(req, timeout=300).read())
        rows = [{k: v["value"] for k, v in b.items()} for b in data["results"]["bindings"]]
        json.dump(rows, open(WD_CACHE, "w"), ensure_ascii=False)
    by_nit, by_name, labels = collections.defaultdict(set), collections.defaultdict(set), collections.defaultdict(set)
    for r in json.load(open(WD_CACHE)):
        item, site = r["item"].rsplit("/", 1)[-1], r["website"]
        if r.get("nit"):
            n = re.sub(r"\D", "", r["nit"].split("-")[0])
            if n:
                by_nit[n].add((item, site))
        if r.get("label"):
            by_name[norm(r["label"])].add((item, site))
            labels[item].add(norm(r["label"]))
    return by_nit, by_name, labels


def host(url):
    h = urllib.parse.urlparse(url).netloc.lower().split(":")[0]
    return h[4:] if h.startswith("www.") else h


def build():
    pairs, files, totals = {}, [], collections.Counter()
    for path in sorted(glob.glob(os.path.join(EXTRACT, "*.canada.jsonl.gz")), reverse=True):
        with gzip.open(path, "rt", encoding="utf-8") as f:
            meta = json.loads(f.readline())
            fname = meta["_file"]
            files.append(fname)
            totals["declaration_rows_seen"] += meta["_stats"].get("rows", 0)
            for line in f:
                r = json.loads(line)
                totals["canada_rows"] += 1
                buyer, nit = (r.get("NOMBRE_IMPORTADOR") or "").strip(), (r.get("NIT_IMPORTADOR") or "").strip().split(".")[0]
                cls = norm(r.get("CLASE IMPORTADOR"))
                if not buyer or norm(buyer).startswith("PERSONA NATURAL") or "PERSONA NATURAL" in cls or norm(buyer) in ("N A", "NA", "NO APLICA", "ANONIMO"):
                    totals["dropped_person_or_unnamed"] += 1
                    continue
                if not re.fullmatch(r"\d{5,12}", nit) or int(nit) == 0:
                    totals["dropped_no_nit"] += 1
                    continue
                d = ymd(r.get("FECHA_ACEPTACION_DECLARACION")) or ymd(r.get("FECHA_PRESENTACION"))
                if not d or d < MIN_DATE:
                    totals["dropped_before_window"] += 1
                    continue
                vendor = (r.get("NOMBRE_EXPORTADOR") or "").strip()
                if not norm(vendor):
                    totals["dropped_no_vendor"] += 1
                    continue
                totals["kept_rows"] += 1
                key = (nit, norm(vendor))
                form = (r.get("NUMERO_FORMULARIO") or r.get("NUM_ACEPTACION_DECLARACION") or "").strip()
                p = pairs.get(key)
                if p is None:
                    p = pairs[key] = {"best": None, "best_k": None, "forms": set(), "first": d, "fob": 0.0, "files": set()}
                p["forms"].add(form)
                p["files"].add(fname)
                p["first"] = min(p["first"], d)
                p["fob"] += num(r.get("VALOR_FOB_USD"))
                k = (d, form)
                if p["best_k"] is None or k > p["best_k"]:
                    p["best_k"], p["best"], p["best_file"] = k, r, fname
    by_nit, by_name, labels = wikidata()
    site_for = {}
    for nit, vname in pairs:
        if nit in site_for:
            continue
        name = norm(pairs[(nit, vname)]["best"]["NOMBRE_IMPORTADOR"])
        # NIT match counts only when one of the item's labels is contained in the importer name (drops brand items
        # such as "Ktronix" carrying its operator's NIT); else an exact label/alias match on the full name.
        nit_hit = {(i, s) for i, s in by_nit.get(nit, ()) if any(l and set(l.split()) <= set(name.split()) for l in labels[i])}
        hit = nit_hit or by_name.get(name) or set()
        hosts = {host(s) for _, s in hit} - {""}
        site_for[nit] = (sorted(hosts)[0], "P13465" if nit_hit else "label", sorted({i for i, _ in hit})) if len(hosts) == 1 else None
    n, buyers, recent, with_site = 0, set(), set(), set()
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    with open(OUT + ".tmp", "w", encoding="utf-8") as f:
        for (nit, vname), p in sorted(pairs.items(), key=lambda kv: (kv[0][0], kv[0][1])):
            r, d = p["best"], p["best_k"][0]
            ws = site_for.get(nit)
            website = ("https://%s/" % ws[0]) if ws else ""
            row = dict(r)
            row.update(record_date=d, source_file=p["best_file"], agg_declarations=len(p["forms"]),
                       agg_first_record_date=p["first"], agg_fob_usd_total=round(p["fob"], 2),
                       agg_forms=sorted(p["forms"])[-25:], agg_source_files=sorted(p["files"]))
            if ws:
                row.update(website_source="Wikidata %s (%s)" % (",".join(ws[2]), ws[1]))
            canada_value = "DIRECCION_EXPORTADOR=%s; CIUDAD_PAIS_EXPORTADOR=%s; PAIS_EXPORTADOR=%s; CODIGO_PAIS_EXPORTADOR=%s" % (
                r.get("DIRECCION_EXPORTADOR", ""), r.get("CIUDAD_PAIS_EXPORTADOR", ""), r.get("PAIS_EXPORTADOR", ""), r.get("CODIGO_PAIS_EXPORTADOR", ""))
            out = {"platform": "dian", "domain": host(website) if website else "", "dataset_id": p["best_k"][1],
                   "dataset": "%s, %s" % (DATASET, p["best_file"][:-4]), "dataset_url": BASE + p["best_file"],
                   "publisher": r["NOMBRE_IMPORTADOR"].strip(), "buyer_unit": "", "website": website,
                   "vendor": r["NOMBRE_EXPORTADOR"].strip(), "canada_field": CANADA_FIELD, "canada_value": canada_value,
                   "row": row}
            f.write(json.dumps(out, ensure_ascii=False) + "\n")
            n += 1
            buyers.add(nit)
            if d >= LAST12:
                recent.add(nit)
            if website:
                with_site.add(nit)
    os.replace(OUT + ".tmp", OUT)
    print("COUNTS files=%d (%s .. %s) %s" % (len(files), files[-1] if files else "", files[0] if files else "", dict(totals)))
    print("dian_imports: %d rows, %d distinct buyers, %d buyers dated in last 12 months, %d with website" % (n, len(buyers), len(recent), len(with_site)))


if __name__ == "__main__":
    cmd = sys.argv[1] if len(sys.argv) > 1 else "all"
    if cmd in ("download", "all"):
        download()
    if cmd in ("extract", "all"):
        extract_all()
    if cmd in ("build", "all"):
        build()
