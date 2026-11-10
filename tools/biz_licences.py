#!/usr/bin/env python3
"""Municipal business licences (open data) joined to the organisations we hold (cloud, bulk downloads only).

A business licence is a dated payment to a Canadian municipality: the city's own open data gives the licence number, the trade and legal
names, the address, the issue and EXPIRY dates, the status and — in some cities — the fee paid. For an organisation delivered with only a
registry contract (tier R) or an inferred relationship, that is a recorded, current, dated relationship with a published end date.
Matching is strict: same postal code (or same street number and street) AND the names agree; ambiguous matches are dropped.

  probe                 search each portal's catalogue for business-licence datasets; print ids, row counts, fields, two sample rows
                        (run first: the adapters below were written from the portals' documentation and are checked against the log)
  pull                  download each configured dataset (current licences only) -> out/licences_<city>.csv.gz
  match                 join to the organisations of the ranked table and the site facts -> out/licence_matches.csv
  merge DIR             -> data/incoming/claude/claude_licence_matches.csv (rank.py reads it)
No site is crawled: only the open-data portals' bulk / API endpoints, a few requests each.
"""
import argparse, collections, csv, glob, gzip, io, json, os, re, sys, time, unicodedata, urllib.parse, urllib.request

csv.field_size_limit(1 << 30)
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
INC = os.path.join(ROOT, "data/incoming/claude")
OUT = os.path.join(INC, "claude_licence_matches.csv")
UA = "canada-contracts-hub-crawler/1.0 (+https://github.com/mohamedbiranesy-gif/canada-contracts-hub)"
TODAY = time.strftime("%Y-%m-%d")

# portal catalogues to search (probe). kind: ods = Opendatasoft, socrata, ckan, arcgis (ArcGIS Hub search, one call for all of Canada)
PORTALS = [
    ("vancouver", "ods", "https://opendata.vancouver.ca"), ("calgary", "socrata", "https://data.calgary.ca"), ("edmonton", "socrata", "https://data.edmonton.ca"),
    ("toronto", "ckan", "https://ckan0.cf.opendata.inter.prod-toronto.ca"), ("winnipeg", "socrata", "https://data.winnipeg.ca"), ("surrey", "ckan", "https://data.surrey.ca"),
    ("regina", "ckan", "https://open.regina.ca"), ("montreal", "ckan", "https://donnees.montreal.ca"), ("quebec", "ckan", "https://www.donneesquebec.ca/recherche"),
    ("strathcona", "socrata", "https://data.strathcona.ca"), ("novascotia", "socrata", "https://data.novascotia.ca"), ("arcgis-hub", "arcgis", "https://hub.arcgis.com"),
]
QUERIES = ["business licence", "business licences", "business license", "permis d'affaires", "certificats d'occupation", "licences commerciales"]

# datasets to pull (filled / corrected after the probe). fields: logical name -> list of candidate column names (first one present wins)
SOURCES = {
    "vancouver": dict(kind="ods", base="https://opendata.vancouver.ca", dataset="business-licences", payee="City of Vancouver",
                      payee_address="453 West 12th Avenue, Vancouver, BC V5Y 1V4", payee_site="https://vancouver.ca/",
                      page="https://opendata.vancouver.ca/explore/dataset/business-licences/information/",
                      where="status='Issued'", fields=dict(number=["licencenumber"], rsn=["licencersn"], name=["businessname"], trade=["businesstradename"], status=["status"],
                                                             issued=["issueddate"], expires=["expireddate"], kind=["businesstype"], unit=["unit"], house=["house"], street=["street"],
                                                             city=["city"], prov=["province"], postal=["postalcode"], fee=["feepaid"], year=["folderyear"])),
}


def get(url, tries=4, timeout=120):
    err = None
    for i in range(tries):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept": "application/json, text/csv, */*"})
            with urllib.request.urlopen(req, timeout=timeout) as r:
                return r.read()
        except Exception as e:
            err = e
            time.sleep(3 * (i + 1))
    raise err


def jget(url, **kw):
    return json.loads(get(url, **kw).decode("utf-8", "replace"))


def probe(a):
    for name, kind, base in PORTALS:
        print("\n===== %s (%s) %s" % (name, kind, base), flush=True)
        seen = set()
        for q in QUERIES:
            try:
                if kind == "ods":
                    d = jget("%s/api/explore/v2.1/catalog/datasets?limit=20&where=%s" % (base, urllib.parse.quote('search("%s")' % q)))
                    for ds in d.get("results") or []:
                        did = ds.get("dataset_id")
                        if did in seen:
                            continue
                        seen.add(did)
                        meta = (ds.get("metas") or {}).get("default") or {}
                        print("  [%s] %s | records %s | modified %s | licence %s" % (did, meta.get("title"), meta.get("records_count"), meta.get("modified"), meta.get("license")), flush=True)
                        print("     fields: " + ", ".join("%s(%s)" % (f.get("name"), f.get("type")) for f in ds.get("fields") or []))
                        try:
                            rec = jget("%s/api/explore/v2.1/catalog/datasets/%s/records?limit=2" % (base, did))
                            for r in rec.get("results") or []:
                                print("     sample: " + json.dumps(r, ensure_ascii=False)[:700])
                        except Exception as e:
                            print("     (no sample: %s)" % e)
                elif kind == "socrata":
                    dom = urllib.parse.urlparse(base).netloc
                    d = jget("https://api.us.socrata.com/api/catalog/v1?domains=%s&search_context=%s&q=%s&limit=10" % (dom, dom, urllib.parse.quote(q)))
                    for res in d.get("results") or []:
                        r0 = res.get("resource") or {}
                        did = r0.get("id")
                        if did in seen or r0.get("type") not in ("dataset", "filter"):
                            continue
                        seen.add(did)
                        print("  [%s] %s | type %s | updated %s | rows? | page views %s" % (did, r0.get("name"), r0.get("type"), r0.get("updatedAt"), (r0.get("page_views") or {}).get("page_views_total")), flush=True)
                        print("     fields: " + ", ".join("%s(%s)" % (n, t) for n, t in zip(r0.get("columns_field_name") or [], r0.get("columns_datatype") or [])))
                        try:
                            cnt = jget("%s/resource/%s.json?$select=count(*)" % (base, did))
                            print("     rows: %s" % json.dumps(cnt)[:80])
                            for r in jget("%s/resource/%s.json?$limit=2" % (base, did)):
                                print("     sample: " + json.dumps(r, ensure_ascii=False)[:700])
                        except Exception as e:
                            print("     (no sample: %s)" % e)
                elif kind == "ckan":
                    d = jget("%s/api/3/action/package_search?q=%s&rows=8" % (base, urllib.parse.quote(q)))
                    for p in (d.get("result") or {}).get("results") or []:
                        if p.get("name") in seen:
                            continue
                        seen.add(p.get("name"))
                        print("  [%s] %s | org %s | modified %s" % (p.get("name"), p.get("title"), (p.get("organization") or {}).get("title"), p.get("metadata_modified")), flush=True)
                        for r in (p.get("resources") or [])[:8]:
                            print("     resource %s | %s | %s | datastore %s | %s" % (r.get("id"), r.get("name"), r.get("format"), r.get("datastore_active"), (r.get("url") or "")[:140]))
                            if r.get("datastore_active"):
                                try:
                                    ds = jget("%s/api/3/action/datastore_search?resource_id=%s&limit=2" % (base, r.get("id")))["result"]
                                    print("       total %s | fields: %s" % (ds.get("total"), ", ".join("%s(%s)" % (f.get("id"), f.get("type")) for f in ds.get("fields") or [])))
                                    for rec in ds.get("records") or []:
                                        print("       sample: " + json.dumps(rec, ensure_ascii=False)[:700])
                                except Exception as e:
                                    print("       (no sample: %s)" % e)
                elif kind == "arcgis":
                    d = jget("https://hub.arcgis.com/api/v3/datasets?q=%s&filter%%5Bcountry%%5D=CA&page%%5Bsize%%5D=25" % urllib.parse.quote(q))
                    for ds in d.get("data") or []:
                        at = ds.get("attributes") or {}
                        if ds.get("id") in seen:
                            continue
                        seen.add(ds.get("id"))
                        print("  [%s] %s | %s | records %s | %s | %s" % (ds.get("id"), at.get("name"), at.get("source") or at.get("owner"), at.get("recordCount"), at.get("modified"), (at.get("url") or "")[:150]), flush=True)
                        print("     fields: " + ", ".join(f.get("name") or "" for f in (at.get("fields") or [])[:40]))
            except Exception as e:
                print("  query %r failed: %s" % (q, str(e)[:160]), flush=True)


def norm(s):
    return re.sub(r"[^a-z0-9]+", " ", unicodedata.normalize("NFKD", s or "").encode("ascii", "ignore").decode().lower()).strip()


def pick(row, names):
    for n in names:
        if n in row and row[n] not in (None, ""):
            return str(row[n]).strip()
    return ""


def pull(a):
    os.makedirs("out", exist_ok=True)
    for city, S in SOURCES.items():
        if a.only and city not in a.only.split(","):
            continue
        t0 = time.time()
        rows = []
        try:
            if S["kind"] == "ods":
                url = "%s/api/explore/v2.1/catalog/datasets/%s/exports/csv?delimiter=%%2C&lang=en%s" % (S["base"], S["dataset"], ("&where=" + urllib.parse.quote(S["where"])) if S.get("where") else "")
                data = get(url, timeout=600)
                rd = csv.DictReader(io.StringIO(data.decode("utf-8-sig", "replace")))
                print("%s: columns %s" % (city, rd.fieldnames), flush=True)
                rows = list(rd)
            elif S["kind"] == "socrata":
                off = 0
                while True:
                    part = jget("%s/resource/%s.json?$limit=50000&$offset=%d%s" % (S["base"], S["dataset"], off, ("&$where=" + urllib.parse.quote(S["where"])) if S.get("where") else ""), timeout=300)
                    rows += part
                    if len(part) < 50000:
                        break
                    off += 50000
            elif S["kind"] == "ckan":
                off = 0
                while True:
                    res = jget("%s/api/3/action/datastore_search?resource_id=%s&limit=32000&offset=%d" % (S["base"], S["dataset"], off), timeout=300)["result"]
                    rows += res.get("records") or []
                    if len(res.get("records") or []) < 32000:
                        break
                    off += 32000
        except Exception as e:
            print("%s: download failed: %s" % (city, str(e)[:200]), flush=True)
            continue
        F = S["fields"]
        out = []
        for r in rows:
            o = {k: pick(r, v) for k, v in F.items()}
            if not (o.get("name") or o.get("trade")):
                continue
            o["city_source"] = city
            out.append(o)
        cols = ["city_source"] + list(F)
        with gzip.open("out/licences_%s.csv.gz" % city, "wt", encoding="utf-8", newline="") as f:
            w = csv.DictWriter(f, fieldnames=cols, extrasaction="ignore")
            w.writeheader()
            w.writerows(out)
        st = collections.Counter(o.get("status") for o in out)
        print("%s: %d records downloaded, %d kept (%.0f s); status %s; with postal code %d; sample %s" % (
            city, len(rows), len(out), time.time() - t0, dict(st.most_common(5)), sum(1 for o in out if o.get("postal")), json.dumps(out[:1], ensure_ascii=False)[:600]), flush=True)


PC = re.compile(r"\b([ABCEGHJ-NPRSTVXY]\d[ABCEGHJ-NPRSTV-Z])\s?(\d[ABCEGHJ-NPRSTV-Z]\d)\b")
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
first new old best royal golden green blue red black white big little one two""".split())


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


def match(a):
    import ranked_io
    os.makedirs("out", exist_ok=True)
    by_pc = collections.defaultdict(list)
    n_lic = 0
    for f in sorted(glob.glob(os.path.join(a.dir, "licences_*.csv.gz"))):
        with gzip.open(f, "rt", encoding="utf-8", newline="") as fh:
            for r in csv.DictReader(fh):
                m = PC.search((r.get("postal") or "").upper())
                if m:
                    by_pc[m.group(1) + m.group(2)].append(r)
                    n_lic += 1
    orgs = {}
    for r in ranked_io.rows():
        m = PC.search((r.get("buyer_address") or "").upper())
        if m and (r.get("email") or "").strip():
            dom = urllib.parse.urlparse(r.get("buyer_website") or "").hostname or ""
            orgs[(r.get("keys") or "").split("|")[0]] = (r.get("buyer") or "", m.group(1) + m.group(2), r.get("buyer_address") or "", dom, r.get("buyer_legal_name_as_published") or "", r.get("tier") or "")
    fp = os.path.join(INC, "claude_lead_site_facts.jsonl.gz")
    if os.path.exists(fp):
        for l in gzip.open(fp, "rt", encoding="utf-8"):
            try:
                o = json.loads(l)
            except ValueError:
                continue
            m = PC.search((o.get("address_quote") or "").upper())
            if m and o.get("key") and o["key"] not in orgs and o.get("site_name"):
                orgs[o["key"]] = (o["site_name"], m.group(1) + m.group(2), o.get("address_quote") or "", urllib.parse.urlparse(o.get("site") or "").hostname or "", "", "")
    out, stats = [], collections.Counter()
    for key, (name, pc, addr, dom, legal, tier) in orgs.items():
        cands = by_pc.get(pc) or []
        if not cands:
            continue
        stats["organisations in a postal code that has licences"] += 1
        hits = [r for r in cands if names_agree(name, r.get("trade") or "") or names_agree(name, r.get("name") or "") or (legal and (names_agree(legal, r.get("name") or "") or names_agree(legal, r.get("trade") or "")))]
        if not hits:
            continue
        payers = {(norm(r.get("name") or ""), norm(r.get("trade") or "")) for r in hits}
        if len(payers) > 1:
            stats["ambiguous (several licensees fit): dropped"] += 1
            continue
        best = sorted(hits, key=lambda r: (r.get("expires") or "", r.get("issued") or ""), reverse=True)[0]
        stats["matched"] += 1
        stats["matched, tier %s" % (tier or "none yet")] += 1
        out.append(dict(org_key=key, org_name=name, org_domain=dom, org_postal=pc, city_source=best["city_source"], licence_number=best.get("number") or best.get("rsn") or "",
                        licensee_legal_name=best.get("name") or "", licensee_trade_name=best.get("trade") or "", licence_type=best.get("kind") or "", status=best.get("status") or "",
                        issued=(best.get("issued") or "")[:10], expires=(best.get("expires") or "")[:10], fee_paid=best.get("fee") or "", licences_of_this_licensee=len(hits),
                        licence_address=" ".join(x for x in (best.get("unit"), best.get("house"), best.get("street"), best.get("city"), best.get("prov"), best.get("postal")) if x),
                        payee=SOURCES[best["city_source"]]["payee"], payee_address=SOURCES[best["city_source"]]["payee_address"], payee_site=SOURCES[best["city_source"]]["payee_site"],
                        dataset_page=SOURCES[best["city_source"]]["page"], read=TODAY,
                        match_basis="same postal code %s and the names agree (%r ~ %r)" % (pc, name, best.get("trade") or best.get("name"))))
    cols = list(out[0].keys()) if out else ["org_key"]
    with open("out/licence_matches.csv", "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=cols)
        w.writeheader()
        w.writerows(out)
    print("licences with a postal code: %d; organisations with a postal code: %d; %s" % (n_lic, len(orgs), dict(stats)), flush=True)
    for o in out[:12]:
        print("  ", json.dumps({k: o[k] for k in ("org_name", "licensee_trade_name", "licensee_legal_name", "licence_number", "issued", "expires", "fee_paid", "city_source")}, ensure_ascii=False))


def merge(a):
    rows = {}
    if os.path.exists(OUT):
        rows = {r["org_key"]: r for r in csv.DictReader(open(OUT, encoding="utf-8"))}
    n0 = len(rows)
    for f in sorted(glob.glob(os.path.join(a.dir, "licence_matches.csv"))):
        for r in csv.DictReader(open(f, encoding="utf-8")):
            if r.get("org_key"):
                rows[r["org_key"]] = r
    if rows:
        cols = list(next(iter(rows.values())).keys())
        with open(OUT, "w", newline="", encoding="utf-8") as f:
            w = csv.DictWriter(f, fieldnames=cols, extrasaction="ignore")
            w.writeheader()
            for k in sorted(rows):
                w.writerow(rows[k])
    print("business licences matched to organisations: %d (+%d this run): %s" % (len(rows), len(rows) - n0, dict(collections.Counter(r.get("city_source") for r in rows.values()))))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("cmd", choices=["probe", "pull", "match", "merge"])
    ap.add_argument("dir", nargs="?", default="out")
    ap.add_argument("--only", default="")
    a = ap.parse_args()
    {"probe": probe, "pull": pull, "match": match, "merge": merge}[a.cmd](a)


if __name__ == "__main__":
    main()
