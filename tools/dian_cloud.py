#!/usr/bin/env python3
"""Colombian importers billed by an exporter located in Canada, from DIAN's declaration-level import microdata — in the cloud. No AI.

Every import into Colombia is declared to DIAN (Dirección de Impuestos y Aduanas Nacionales), which publishes each month every declaration
line ("Bases estadísticas de comercio exterior - Importaciones", one zip a month, ~280 MB; importer names published under a court order,
natural persons anonymised — tools/dian_imports.py holds the source notes). A declaration line names, in DIAN's own fields:
  the importer (NOMBRE_IMPORTADOR, NIT_IMPORTADOR + check digit, DIRECCION_IMPORTADOR, DEPARTAMENTO_IMPORTADOR),
  the exporter (NOMBRE_EXPORTADOR, DIRECCION_EXPORTADOR, CIUDAD_PAIS_EXPORTADOR, PAIS_EXPORTADOR — "Canadá": the vendor in Canada by the
    source's own field, AGENTS.md §2.1),
  the exporter's invoice (NUMERO_FACTURA, FECHA_FACTURA) and its value (VALOR_FOB_USD; freight, insurance, CIF),
  what was bought (DESCRIPCION_MERCANCIA, SUBPARTIDA_ARANCELARIA), and how the importer pays it (FORMA_PAGO: "Giro directo" — a direct transfer
    through the foreign-exchange market —, "Pagos anticipados", "Financiación directa del proveedor", ...; TIPO_IMPORTACION "Reembolsable").
Every invoice field is published, in a public record: the biller in Canada, the buyer, the bill's number, date and amount, what is billed and
how it is paid. A line with no payment abroad ("Importación que no genera pago en el exterior", "Otras no reembolsables", foreign direct
investment, samples) makes no row; neither does an importer that is a natural person, nor an exporter whose name is a person's.

  fetch  [--months 12]       the newest N monthly zips not read yet: download one at a time into $RUNNER_TEMP, keep the Canada lines (a
                             compact set of columns, no e-mail) in data/incoming/claude/dian/months/<YYYY-MM>.jsonl.gz, delete the zip
  pairs                      -> data/incoming/claude/dian/dian_pairs.csv.gz: one line per (importer NIT, exporter), its newest invoice and totals
  sites  [--minutes M]       the importers' own websites: Wikidata (the NIT, P13465), the Overture Maps place under the importer's very name
                             (tools/overture_names.py, lane dian), the company-name autocomplete, and the importer's name as a .com.co / .com
                             / .co domain — each kept ONLY when the site's own pages print the importer's NIT (its home page, or its contact /
                             privacy / legal page linked from it): a nine- or ten-digit tax number printed on the site is the tie
                             -> data/incoming/claude/dian/dian_sites.csv (append-only) and dian_sites_done.tsv
  leads  [--stamp S]         importers with a site -> data/incoming/claude/lead_shards/leads_dian_<S>.gz + details_dian_<S>.gz
"""
import argparse, collections, csv, glob, gzip, hashlib, html, json, os, re, shutil, socket, sys, time, urllib.parse, urllib.request

csv.field_size_limit(1 << 30)
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import dian_imports as DI

INC = os.path.join(ROOT, "data/incoming/claude")
DIR = os.path.join(INC, "dian")
MONTHS = os.path.join(DIR, "months")
PAIRS = os.path.join(DIR, "dian_pairs.csv.gz")
SITES = os.path.join(DIR, "dian_sites.csv")
SDONE = os.path.join(DIR, "dian_sites_done.tsv")
SHARDS = os.path.join(INC, "lead_shards")
OVT = os.path.join(INC, "overture", "dian_candidates.csv")
UA = DI.UA
TODAY = time.strftime("%Y-%m-%d")
KEEP = ["NOMBRE_IMPORTADOR", "NIT_IMPORTADOR", "DIGITO_VERIFI_NIT_IMPORTA", "CIUDAD_PAIS_IMPORTADOR", "DIRECCION_IMPORTADOR", "TELEFONO_IMPORTADOR",
        "CODIGO_DEPTO_IMPORTADOR", "DEPARTAMENTO_IMPORTADOR", "CODIGO_MUNICIPIO", "CLASE IMPORTADOR", "NOMBRE_EXPORTADOR", "DIRECCION_EXPORTADOR",
        "CIUDAD_PAIS_EXPORTADOR", "CODIGO_PAIS_EXPORTADOR", "PAIS_EXPORTADOR", "NUMERO_FACTURA", "FECHA_FACTURA", "VALOR_FOB_USD", "VALOR_FLETES_USD",
        "VALOR_SEGUROS_USD", "VALOR_CIF_USD", "DESCRIPCION_MERCANCIA", "SUBPARTIDA_ARANCELARIA", "CANTIDAD", "UNIDAD_COMERCIAL", "PESO_NETO", "COD_FORMA_PAGO",
        "FORMA_PAGO", "TIPO_IMPORTACION", "NUM_CUOTAS_O_MESES", "MODO_TRANSPORTE", "ADUANA_PRESENTADA", "NUMERO_FORMULARIO", "NUM_ACEPTACION_DECLARACION",
        "FECHA_ACEPTACION_DECLARACION", "FECHA_PRESENTACION", "PAIS_ORIGEN", "PAIS_PROCEDENCIA", "PAIS_COMPRA", "RAZON_SOCIAL_DECLARANTE"]
# the payment forms of a purchase paid abroad (DIAN's FORMA_PAGO words); what is not paid abroad makes no row
NO_PAYMENT = re.compile(r"no genera pago|no reembolsable|inversi[oó]n extranjera|muestra", re.I)
# Colombian law (Ley 1581 de 2012) has every site that collects personal data publish its data-processing policy, which names the company and
# its NIT; the contact page and the legal notice often print it too
LEGAL_LINK = re.compile(r"privacidad|datos[-_ ]?personales|tratamiento|habeas|aviso[-_ ]?legal|t[eé]rminos|terminos|politica|pol%C3%ADtica|contacto|contact|"
                        r"nosotros|quienes|qui%C3%A9nes|empresa|legal|facturaci", re.I)


def month_of(name):
    m = re.fullmatch(r"(\d\d)_Importaciones_(\d{4})_\w+\.zip", name)
    return "%s-%s" % (m.group(2), m.group(1)) if m else ""


def cmd_fetch(a):
    os.makedirs(MONTHS, exist_ok=True)
    req = urllib.request.Request(DI.LISTING, headers={"User-Agent": UA, "Accept": "application/json;odata=nometadata"})
    files = sorted(((month_of(x["Name"]), x["Name"], int(x["Length"])) for x in json.loads(urllib.request.urlopen(req, timeout=120).read())["value"]
                    if month_of(x["Name"])), reverse=True)[:a.months]
    tmp = os.path.join(os.environ.get("RUNNER_TEMP") or "/tmp", "dian_zips")
    os.makedirs(tmp, exist_ok=True)
    DI.SRC = tmp
    t_end = time.time() + 60 * a.minutes
    for ym, name, size in files:
        out = os.path.join(MONTHS, ym + ".jsonl.gz")
        if os.path.exists(out):
            continue
        if time.time() > t_end:
            print("fetch: time is up; %s left for the next run" % ym, flush=True)
            break
        path = os.path.join(tmp, name)
        t0 = time.time()
        with urllib.request.urlopen(urllib.request.Request(DI.BASE + urllib.parse.quote(name), headers={"User-Agent": UA}), timeout=300) as r, open(path, "wb") as f:
            shutil.copyfileobj(r, f, 4 << 20)
        if os.path.getsize(path) != size:
            print("fetch: %s came short (%d of %d bytes): left for the next run" % (name, os.path.getsize(path), size), flush=True)
            os.remove(path)
            continue
        stats, rows = DI.extract_one(path)
        os.remove(path)
        kept = 0
        with gzip.open(out + ".tmp", "wt", encoding="utf-8") as f:
            f.write(json.dumps({"_file": name, "_month": ym, "_stats": dict((k, v) for k, v in stats.items() if not k.startswith("code_other")), "_read": TODAY},
                               ensure_ascii=False) + "\n")
            for r in rows:
                rec = {k: (r.get(k) or "").strip() for k in KEEP}
                rec["DESCRIPCION_MERCANCIA"] = rec["DESCRIPCION_MERCANCIA"][:400]
                f.write(json.dumps(rec, ensure_ascii=False) + "\n")
                kept += 1
        os.replace(out + ".tmp", out)
        print(time.strftime("%H:%M:%S"), "%s: %d declaration lines, %d with an exporter in Canada (%.0f s)" % (name, stats.get("rows", 0), kept, time.time() - t0), flush=True)


BUSINESS = set("""transport transports trucking logistics foods food global international medical imaging distributors distribution metals metal parts drills
radiopharma pharma pharmaceutical pharmaceuticals export exports import measurement alliance trade trading impex containers technology technologies
networks motors systems packaging plants standards industries industry holding holdings automation electric electrical equipment equipt security
composites alarm division group solutions services service canada canadian north america american products produits marine seafood seafoods farms
farm agri seeds grain grains feeds supply supplies machinery manufacturing energy resources mining minerals labs laboratories sciences health
aerospace aviation airlines software studios media enterprises entreprises company compagnie co corp inc ltd ltee limited llc lp ulc""".split())


def is_person(name):
    """an exporter's name that reads as a natural person's ("TATIANA GOMEZ REY"): no legal form, no word of a trade, two to four words of letters
    only. A company named without its legal form ("AGT FOODS", "L.SIMARD TRANSPORT", "MARCH NETWORKS") is not a person."""
    import tm_register as TM
    if TM.is_org(name) or re.search(r"[&/\d.,()\-]", name):
        return False
    w = re.findall(r"[A-Za-zÀ-ÿ']+", name)
    if any(x.lower() in BUSINESS for x in w):
        return False
    return 2 <= len(w) <= 4


def nit_of(r):
    n = re.sub(r"\D", "", (r.get("NIT_IMPORTADOR") or "").split(".")[0])
    dv = re.sub(r"\D", "", (r.get("DIGITO_VERIFI_NIT_IMPORTA") or "").split(".")[0])
    return n, dv[:1]


def num(v):
    try:
        return float(v)
    except (TypeError, ValueError):
        return 0.0


PAIR_COLS = ["key", "nit", "dv", "importer", "importer_address", "importer_city", "importer_department", "importer_phone", "exporter", "exporter_address",
             "exporter_city", "exporter_country", "invoice", "invoice_date", "fob_usd", "freight_usd", "insurance_usd", "cif_usd", "goods", "hs_code", "payment_form",
             "import_type", "transport", "customs_office", "declaration", "declaration_date", "source_file", "declarations", "invoices", "first_date", "last_date",
             "fob_usd_total", "months"]


def cmd_pairs(a):
    pairs, cnt = {}, collections.Counter()
    for path in sorted(glob.glob(os.path.join(MONTHS, "*.jsonl.gz"))):
        with gzip.open(path, "rt", encoding="utf-8") as f:
            meta = json.loads(f.readline())
            for line in f:
                r = json.loads(line)
                cnt["lines"] += 1
                imp, exp = r["NOMBRE_IMPORTADOR"], r["NOMBRE_EXPORTADOR"]
                if DI.norm(r["PAIS_EXPORTADOR"]) != "CANADA":
                    cnt["exporter not in Canada"] += 1; continue
                if not imp or "PERSONA NATURAL" in DI.norm(imp) or "PERSONA NATURAL" in DI.norm(r["CLASE IMPORTADOR"]):
                    cnt["importer a natural person / unnamed"] += 1; continue
                nit, dv = nit_of(r)
                if not re.fullmatch(r"\d{6,12}", nit) or int(nit) == 0:
                    cnt["no NIT"] += 1; continue
                if not exp or is_person(exp):
                    cnt["exporter unnamed or a person's name"] += 1; continue
                if NO_PAYMENT.search(r["FORMA_PAGO"]) or NO_PAYMENT.search(r["TIPO_IMPORTACION"]):
                    cnt["no payment abroad"] += 1; continue
                fob = num(r["VALOR_FOB_USD"])
                if fob <= 0:
                    cnt["no value"] += 1; continue
                d = DI.ymd(r["FECHA_ACEPTACION_DECLARACION"]) or DI.ymd(r["FECHA_PRESENTACION"])
                if not d:
                    cnt["no date"] += 1; continue
                cnt["kept"] += 1
                k = (nit, DI.norm(exp))
                p = pairs.setdefault(k, {"best": None, "bk": None, "forms": set(), "inv": set(), "first": d, "last": d, "fob": 0.0, "months": set()})
                p["forms"].add(r["NUMERO_FORMULARIO"]); p["inv"].add(r["NUMERO_FACTURA"]); p["months"].add(meta["_month"])
                p["first"], p["last"] = min(p["first"], d), max(p["last"], d)
                p["fob"] += fob
                bk = (d, r["NUMERO_FORMULARIO"], fob)
                if p["bk"] is None or bk > p["bk"]:
                    p["bk"], p["best"], p["file"] = bk, r, meta["_file"]
    os.makedirs(DIR, exist_ok=True)
    with gzip.open(PAIRS + ".tmp", "wt", encoding="utf-8", newline="") as f:
        w = csv.writer(f)
        w.writerow(PAIR_COLS)
        for (nit, _), p in sorted(pairs.items()):
            r = p["best"]
            w.writerow(["dian:%s" % nit, nit, nit_of(r)[1], r["NOMBRE_IMPORTADOR"], r["DIRECCION_IMPORTADOR"], r["CIUDAD_PAIS_IMPORTADOR"], r["DEPARTAMENTO_IMPORTADOR"],
                        r["TELEFONO_IMPORTADOR"].split(".")[0], r["NOMBRE_EXPORTADOR"], r["DIRECCION_EXPORTADOR"], r["CIUDAD_PAIS_EXPORTADOR"], r["PAIS_EXPORTADOR"],
                        r["NUMERO_FACTURA"], DI.ymd(r["FECHA_FACTURA"]), r["VALOR_FOB_USD"], r["VALOR_FLETES_USD"], r["VALOR_SEGUROS_USD"], r["VALOR_CIF_USD"],
                        r["DESCRIPCION_MERCANCIA"], r["SUBPARTIDA_ARANCELARIA"].split(".")[0], r["FORMA_PAGO"], r["TIPO_IMPORTACION"], r["MODO_TRANSPORTE"],
                        r["ADUANA_PRESENTADA"], r["NUMERO_FORMULARIO"], p["bk"][0], p["file"], len(p["forms"]), len(p["inv"] - {""}), p["first"], p["last"],
                        "%.2f" % p["fob"], ";".join(sorted(p["months"]))])
    os.replace(PAIRS + ".tmp", PAIRS)
    nits = {k[0] for k in pairs}
    print("dian pairs: %d (importer, exporter) pairs, %d importers; lines %s" % (len(pairs), len(nits), dict(cnt)), flush=True)


def pairs_by_nit():
    out = collections.defaultdict(list)
    if os.path.exists(PAIRS):
        with gzip.open(PAIRS, "rt", encoding="utf-8", newline="") as f:
            for r in csv.DictReader(f):
                out[r["nit"]].append(r)
    return out


def sites_on_file():
    out = {}
    if os.path.exists(SITES):
        for r in csv.DictReader(open(SITES, encoding="utf-8", newline="")):
            out[r["key"]] = r
    return out


def visible(page):
    return re.sub(r"\s+", " ", html.unescape(re.sub(r"<[^>]+>", " ", re.sub(r"(?is)<(script|style|noscript).*?</\1>", " ", page[:600_000]))))


def nit_rx(nit):
    return re.compile(r"(?<![\d.])" + r"[.\s,]?".join(nit) + r"(?:\s?-\s?\d)?(?![\d])")


def nit_on_site(domain, nit):
    """the importer's NIT printed on the site's own home page, or on one of its contact / privacy / legal pages linked from it (at most four
    pages read) -> (url, the words around it), else None"""
    import client_lists as CL
    site = "https://%s/" % domain
    if not CL.allowed(site):
        return None
    page, final = CL.fetch(site)
    if not page:
        return None
    rx = nit_rx(nit)
    t = visible(page)
    m = rx.search(t)
    if m:
        return final or site, t[max(0, m.start() - 80): m.end() + 20].strip()
    base = final or site
    links = []
    for h, txt in re.findall(r"(?is)<a\b[^>]*href\s*=\s*[\"']([^\"'#]+)[\"'][^>]*>(.*?)</a>", page[:600_000]):
        u = urllib.parse.urljoin(base, html.unescape(h))
        if urllib.parse.urlparse(u).scheme not in ("http", "https") or urllib.parse.urlparse(u).hostname is None:
            continue
        if DI.host(u).split(".")[-2:] != DI.host(base).split(".")[-2:]:
            continue
        if LEGAL_LINK.search(u) or LEGAL_LINK.search(re.sub(r"<[^>]+>", " ", txt)):
            if u not in links and not re.search(r"\.(?:jpg|png|gif|zip|docx?|xlsx?)$", u, re.I):
                links.append(u)
    for u in links[:4]:
        if not CL.allowed(u):
            continue
        p2, f2 = CL.fetch(u)
        if not p2:
            continue
        if re.search(r"\.pdf(?:$|\?)", u, re.I):
            continue
        t2 = visible(p2)
        m = rx.search(t2)
        if m:
            return f2 or u, t2[max(0, m.start() - 80): m.end() + 20].strip()
    return None


GENERIC_ES = set("""comercializadora distribuidora importadora exportadora industrias industria inversiones sociedad compania compañia cia empresa empresas
grupo group internacional international colombia colombiana colombiano de del la las los el y e en para s a sas ltda limitada sucursal corporacion
corp servicios servicio soluciones productos productora andina andino comercial suministros agencia representaciones the and of aereo aerea
nacional nacionales territorios autos alimentos fabrica manufacturas organizacion trading global latam america americas caribe norte sur""".split())


def guesses(name):
    import tm_register as TM
    w = [x for x in TM.nkey_x(name).split() if x not in GENERIC_ES and not x.isdigit()]
    out = []
    if w:
        # the first distinctive word, the first two together, and the last one (a brand often ends the name: "Productora de Cables PROCABLES")
        stems = [w[0]] + ([w[-1]] if len(w) >= 2 else []) + (["".join(w[:2])] if len(w) >= 2 else [])
        for s in stems:
            if len(s) < 5:
                continue
            for tld in ("com.co", "com", "co"):
                d = "%s.%s" % (s, tld)
                if d not in out:
                    out.append(d)
    return out[:9]


def resolves(domain):
    try:
        socket.setdefaulttimeout(5)
        socket.getaddrinfo(domain, 443)
        return True
    except Exception:
        return False


def cmd_sites(a):
    import queue, threading
    import hc_registers as HR
    os.makedirs(DIR, exist_ok=True)
    tmp = os.path.join(os.environ.get("RUNNER_TEMP") or "/tmp", "dian_wd")
    os.makedirs(tmp, exist_ok=True)
    DI.WD_CACHE = os.path.join(tmp, "wikidata_co.json")
    by = pairs_by_nit()
    have = sites_on_file()
    done = {l.split("\t")[0] for l in open(SDONE, encoding="utf-8")} if os.path.exists(SDONE) else set()
    ovt = collections.defaultdict(list)
    if os.path.exists(OVT):
        for r in csv.DictReader(open(OVT, encoding="utf-8", newline="")):
            ovt[r["key"]].append(r["site"])
    try:
        wd_nit, wd_name, _labels = DI.wikidata()
    except Exception as e:
        print("wikidata: not read (%s)" % e, flush=True)
        wd_nit, wd_name = {}, {}
    todo = [n for n in by if "dian:%s" % n not in have and "dian:%s" % n not in done]
    # the largest buyers first: their invoices from Canada on file, in US dollars
    todo.sort(key=lambda n: -sum(num(p["fob_usd_total"]) for p in by[n]))
    new = not os.path.exists(SITES)
    f = open(SITES, "a", encoding="utf-8", newline="")
    w = csv.DictWriter(f, fieldnames=["key", "site", "tied_by", "quote", "read"])
    if new:
        w.writeheader()
    dn = open(SDONE, "a", encoding="utf-8")
    t_end, cnt = time.time() + 60 * a.minutes, collections.Counter()
    lock, cb_lock, q = threading.Lock(), threading.Lock(), queue.Queue()
    for n in todo:
        q.put(n)

    def one(nit):
        name = by[nit][0]["importer"]
        core = HR.core(name)
        cands = []
        for _i, s_ in sorted(wd_nit.get(nit, ())):
            cands.append((DI.host(s_), "Wikidata gives it as the official website of the item whose Colombian NIT is %s" % nit))
        for s_ in ovt.get("dian:%s" % nit, ()):
            cands.append((s_, "an Overture Maps place lists it under the importer's very name in Colombia"))
        if core and len(core) >= 4:
            with cb_lock:  # the autocomplete: one request a second for the whole run
                sug = HR.suggest(core) or []
            for x in sug[:5]:
                d = (x.get("domain") or "").lower().strip()
                if d and HR.core(x.get("name") or "") == core:
                    cands.append((d, "the company-name autocomplete (Clearbit) gives it under the importer's very name (%s)" % core))
        for d in guesses(name):
            if resolves(d):
                cands.append((d, "the importer's name as a domain (%s)" % d))
        seen, n_read = set(), 0
        for d, why in cands:
            d = d[4:] if d.startswith("www.") else d
            if not d or d in seen or HR.BAD.search(d):
                continue
            seen.add(d)
            n_read += 1
            try:
                got = nit_on_site(d, nit)
            except Exception:
                got = None
            if got:
                return (d, why, got), n_read
        return None, n_read

    def worker():
        while time.time() < t_end:
            try:
                nit = q.get_nowait()
            except queue.Empty:
                return
            hit, n_read = one(nit)
            with lock:
                dn.write("%s\t%s\n" % ("dian:%s" % nit, hit[0] if hit else "")); dn.flush()
                cnt["importers asked"] += 1; cnt["sites read"] += n_read
                if hit:
                    d, why, (u, qt) = hit
                    qt = re.sub(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}", "[e-mail]", qt)
                    w.writerow({"key": "dian:%s" % nit, "site": "https://%s/" % d, "read": TODAY, "quote": qt[:300],
                                "tied_by": "%s; the site's own page %s prints the importer's NIT %s: “%s”" % (why, u, nit, qt[:200])})
                    f.flush(); cnt["sites tied"] += 1

    ts = [threading.Thread(target=worker, daemon=True) for _ in range(a.threads)]
    for t in ts:
        t.start()
    for t in ts:
        t.join()
    dn.close(); f.close()
    print("dian sites: %d on file before, %d importers without one; %s" % (len(have), len(todo), dict(cnt)), flush=True)


def money(v):
    return "US$" + format(num(v), ",.2f")


def cmd_leads(a):
    os.makedirs(SHARDS, exist_ok=True)
    stamp = a.stamp or time.strftime("%Y%m%dT%H%M%S", time.gmtime())
    by, sites = pairs_by_nit(), sites_on_file()
    hosts = collections.Counter(DI.host(s["site"]) for s in sites.values() if s.get("site"))
    rows, dets, cnt = [], [], collections.Counter()
    for nit, ps in by.items():
        s = sites.get("dian:%s" % nit)
        if not s or not s.get("site"):
            continue
        if hosts[DI.host(s["site"])] > 2:
            cnt["site shared by more than two importers: left out"] += 1
            continue
        # the relationship shown: the exporter of the newest invoice, among the pairs of the importer
        p = max(ps, key=lambda r: (r["last_date"], num(r["fob_usd"])))
        key = "lead:" + hashlib.sha1(("dian|%s" % nit).encode()).hexdigest()[:16]
        url = DI.BASE + p["source_file"]
        exp_addr = ", ".join(x for x in (p["exporter_address"], p["exporter_city"], p["exporter_country"]) if x)
        cfv = ("importer of record of goods invoiced by an exporter located in Canada — Colombia's customs (DIAN), import declaration %s: "
               "PAIS_EXPORTADOR=%s; DIRECCION_EXPORTADOR=%s; CIUDAD_PAIS_EXPORTADOR=%s" % (p["declaration"], p["exporter_country"], p["exporter_address"], p["exporter_city"]))
        tot = sum(num(x["fob_usd_total"]) for x in ps)
        n_exp = len(ps)
        rows.append({"buyer_key": key, "buyer_name": p["importer"], "website": s["site"], "canadian_vendor_rows": sum(int(x["declarations"] or 0) for x in ps),
                     "example_vendor": p["exporter"], "canada_field_value": cfv, "evidence_dataset": url, "latest_record_date": p["last_date"]})
        dets.append({"key": key, "platform": "dian_import", "record_url": url, "record_date": p["last_date"], "vendor": p["exporter"],
                     "vendor_address": "%s (the exporter's address as the import declaration records it: DIRECCION_EXPORTADOR, CIUDAD_PAIS_EXPORTADOR, PAIS_EXPORTADOR)" % exp_addr,
                     "value": p["fob_usd"], "currency": "USD",
                     "value_basis": "VALOR_FOB_USD of the newest declaration: the exporter's invoice %s of %s" % (p["invoice"], p["invoice_date"] or "an unstated date"),
                     "reference": p["invoice"], "start": p["first_date"], "end": "", "title": p["goods"][:300],
                     "dian_nit": nit, "dian_dv": p["dv"], "dian_declaration": p["declaration"], "dian_declaration_date": p["declaration_date"],
                     "dian_invoice": p["invoice"], "dian_invoice_date": p["invoice_date"], "dian_fob": p["fob_usd"], "dian_cif": p["cif_usd"],
                     "dian_freight": p["freight_usd"], "dian_insurance": p["insurance_usd"], "dian_hs": p["hs_code"], "dian_payment_form": p["payment_form"],
                     "dian_import_type": p["import_type"], "dian_transport": p["transport"], "dian_customs_office": p["customs_office"],
                     "dian_declarations": p["declarations"], "dian_invoices": p["invoices"], "dian_first": p["first_date"], "dian_last": p["last_date"],
                     "dian_fob_total_pair": p["fob_usd_total"], "dian_fob_total_buyer": "%.2f" % tot, "dian_exporters": n_exp,
                     "dian_other_exporters": "; ".join(sorted({x["exporter"] for x in ps} - {p["exporter"]}))[:300], "dian_months": p["months"],
                     "dian_importer_address": ", ".join(x for x in (p["importer_address"], p["importer_city"], p["importer_department"], "Colombia") if x),
                     "register_label": "the import declaration published by Colombia's customs (DIAN)",
                     "buyer_register": {"legal_name": p["importer"], "trade_names": [], "registry_id": "NIT %s-%s (Colombia)" % (nit, p["dv"]) if p["dv"] else "NIT %s (Colombia)" % nit,
                                        "label": "the import declaration %s published by Colombia's customs (DIAN), %s" % (p["declaration"], p["source_file"])},
                     "site_named_by": s.get("tied_by") or "", "site_tied_to_holder_by": s.get("tied_by") or "", "site_quote": s.get("quote") or ""})
        cnt["leads"] += 1
    # only what is new or changed since the shards on file (a later shard replaces an earlier row of the key)
    old_r, old_d = {}, {}
    for pth in sorted(glob.glob(os.path.join(SHARDS, "leads_dian_*.gz"))):
        with gzip.open(pth, "rt", encoding="utf-8", newline="") as fh:
            for r in csv.DictReader(fh):
                old_r[r["buyer_key"]] = json.dumps(r, sort_keys=True, ensure_ascii=False)
    for pth in sorted(glob.glob(os.path.join(SHARDS, "details_dian_*.gz"))):
        with gzip.open(pth, "rt", encoding="utf-8") as fh:
            for l in fh:
                d_ = json.loads(l)
                old_d[d_["key"]] = json.dumps(d_, sort_keys=True, ensure_ascii=False)
    keep = [i for i, (r, d_) in enumerate(zip(rows, dets)) if old_r.get(r["buyer_key"]) != json.dumps({k: str(v) for k, v in r.items()}, sort_keys=True, ensure_ascii=False)
            or old_d.get(d_["key"]) != json.dumps(d_, sort_keys=True, ensure_ascii=False)]
    cnt["unchanged since the shards on file"] = len(rows) - len(keep)
    rows, dets = [rows[i] for i in keep], [dets[i] for i in keep]
    if rows:
        with gzip.open(os.path.join(SHARDS, "leads_dian_%s.gz" % stamp), "wt", encoding="utf-8", newline="") as f:
            w = csv.DictWriter(f, fieldnames=list(rows[0].keys())); w.writeheader(); w.writerows(rows)
        with gzip.open(os.path.join(SHARDS, "details_dian_%s.gz" % stamp), "wt", encoding="utf-8") as f:
            for d in dets:
                f.write(json.dumps(d, ensure_ascii=False) + "\n")
    print("dian leads written: %d (%s)" % (len(rows), dict(cnt)), flush=True)


def main():
    ap = argparse.ArgumentParser()
    sub = ap.add_subparsers(dest="cmd", required=True)
    p = sub.add_parser("fetch"); p.add_argument("--months", type=int, default=12); p.add_argument("--minutes", type=float, default=240)
    sub.add_parser("pairs")
    p = sub.add_parser("sites"); p.add_argument("--minutes", type=float, default=60); p.add_argument("--threads", type=int, default=8)
    p = sub.add_parser("leads"); p.add_argument("--stamp", default="")
    a = ap.parse_args()
    {"fetch": cmd_fetch, "pairs": cmd_pairs, "sites": cmd_sites, "leads": cmd_leads}[a.cmd](a)


if __name__ == "__main__":
    main()
