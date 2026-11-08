#!/usr/bin/env python3
"""Purchase-order / contract-award open data of Canadian public bodies, found through the portals' own catalogue APIs (CKAN, Socrata,
Opendatasoft, ArcGIS Hub), downloaded, and joined to the buyer–vendor pairs already in the ranked file (downstream §1.1: PO numbers).

Mode `discover`: query each portal's catalogue for purchase-order / contract datasets and print dataset ids, titles, formats and
columns (Socrata and CKAN datastores expose column names). Mode `harvest`: download the datasets listed in po_sources.json (written by
hand from the discovery output — only datasets whose columns really carry a PO / order number), normalise (buyer, vendor name, PO
number, date, amount, description, source URL) and write <repo>/data/incoming/claude/claude_po_records.csv.gz. rank.py joins by buyer
organisation + exact vendor name and fills po_number_as_published / most recent PO for pairs it already has — never new rows, because
these files carry no vendor-location field (rule 1).
  python3 tools/po_opendata.py discover [--out ~/cch-tasks/po_discovery.json]
  python3 tools/po_opendata.py harvest --sources contrib/claude/po_sources.json [--repo ~/cch-crawler]
"""
import argparse, gzip, csv, datetime, io, json, os, re, sys, time, urllib.parse, urllib.request

UA = "canada-contracts-hub-crawler/1.0 (+https://github.com/mohamedbiranesy-gif/canada-contracts-hub)"
TODAY = datetime.date.today().isoformat()
KW = ["purchase order", "purchase orders", "contract award", "awarded contracts", "contracts awarded", "procurement", "bons de commande", "contrats", "contrats octroyés", "vendor payments", "payments to suppliers", "accounts payable"]
PORTALS = [
    ("City of Toronto", "ckan", "https://ckan0.cf.opendata.inter.prod-toronto.ca"),
    ("Ville de Montréal", "ckan", "https://donnees.montreal.ca"),
    ("Government of British Columbia", "ckan", "https://catalogue.data.gov.bc.ca"),
    ("Government of Alberta", "ckan", "https://open.alberta.ca"),
    ("Données Québec (all Québec bodies)", "ckan", "https://www.donneesquebec.ca/recherche"),
    ("Government of Canada", "ckan", "https://open.canada.ca/data"),
    ("City of Calgary", "socrata", "https://data.calgary.ca"),
    ("City of Edmonton", "socrata", "https://data.edmonton.ca"),
    ("City of Winnipeg", "socrata", "https://data.winnipeg.ca"),
    ("Region of Peel", "socrata", "https://data.peelregion.ca"),
    ("City of Vancouver", "ods", "https://opendata.vancouver.ca"),
    ("City of Ottawa", "hub", "https://open.ottawa.ca"),
    ("Halifax Regional Municipality", "hub", "https://catalogue-hrm.opendata.arcgis.com"),
    ("City of Hamilton", "hub", "https://open.hamilton.ca"),
    ("City of Mississauga", "hub", "https://data.mississauga.ca"),
    ("City of Regina", "hub", "https://open.regina.ca"),
    ("City of Saskatoon", "hub", "https://opendata-saskatoon.opendata.arcgis.com"),
    ("City of Surrey", "ckan", "https://data.surrey.ca"),
    ("City of Kitchener", "hub", "https://open-kitchenergis.opendata.arcgis.com"),
    ("City of London (ON)", "hub", "https://opendata.london.ca"),
]
PO_COL = re.compile(r"^(po|p\.o\.|purchase[_ ]?order|order[_ ]?(no|number|num|id)|po[_ ]?(no|number|num|id)|bon[_ ]?de[_ ]?commande|no[_ ]?(bc|commande)|commande|document[_ ]?(no|number|id)|reference[_ ]?(no|number)?|no[-_ ]?reference|contract[_ ]?(no|number|id)|numero)", re.I)
_last = [0.0]


def get(url, timeout=120):
    now = time.time()
    if now - _last[0] < 1.0:
        time.sleep(1.0 - (now - _last[0]))
    _last[0] = time.time()
    req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept": "application/json, text/csv, */*"})
    with urllib.request.urlopen(req, timeout=timeout) as r:
        return r.read()


def discover():
    found = []
    for buyer, kind, base in PORTALS:
        for kw in KW:
            try:
                if kind == "ckan":
                    d = json.loads(get("%s/api/3/action/package_search?q=%s&rows=8" % (base, urllib.parse.quote(kw))))
                    for p in (d.get("result") or {}).get("results") or []:
                        t = p.get("title") or ""
                        if not re.search(r"purchase|contract|contrat|procure|award|octroy|bon|payment|paiement|supplier|fournisseur|vendor", t, re.I):
                            continue
                        res = [{"url": r.get("url"), "format": r.get("format"), "name": r.get("name"), "id": r.get("id"), "datastore": r.get("datastore_active")} for r in p.get("resources") or []]
                        cols = []
                        for r in res:
                            if r.get("datastore"):
                                try:
                                    dd = json.loads(get("%s/api/3/action/datastore_search?resource_id=%s&limit=0" % (base, r["id"])))
                                    cols = [f["id"] for f in (dd.get("result") or {}).get("fields") or []]
                                    break
                                except Exception:
                                    pass
                        found.append({"buyer": buyer, "portal": base, "kind": kind, "id": p.get("name") or p.get("id"), "title": t, "resources": res[:6], "columns": cols, "keyword": kw})
                elif kind == "socrata":
                    hostn = urllib.parse.urlparse(base).hostname
                    d = json.loads(get("%s/api/catalog/v1?q=%s&limit=10&only=datasets&domains=%s&search_context=%s" % (base, urllib.parse.quote(kw), hostn, hostn)))
                    for it in d.get("results") or []:
                        r = it.get("resource") or {}
                        if (it.get("metadata") or {}).get("domain") not in (None, hostn):
                            continue  # federated result from another city
                        t = r.get("name") or ""
                        if not re.search(r"purchase|contract|procure|award|payment|supplier|vendor|cheque|check", t, re.I):
                            continue
                        found.append({"buyer": buyer, "portal": base, "kind": kind, "id": r.get("id"), "title": t, "resources": [{"url": "%s/api/views/%s/rows.csv?accessType=DOWNLOAD" % (base, r.get("id")), "format": "CSV"}],
                                      "columns": r.get("columns_name") or [], "keyword": kw})
                elif kind == "ods":
                    d = json.loads(get("%s/api/explore/v2.1/catalog/datasets?where=%s&limit=8" % (base, urllib.parse.quote('search("%s")' % kw))))
                    for it in d.get("results") or []:
                        t = (it.get("metas") or {}).get("default", {}).get("title") or it.get("dataset_id") or ""
                        if not re.search(r"purchase|contract|procure|award|payment|supplier|vendor", t, re.I):
                            continue
                        found.append({"buyer": buyer, "portal": base, "kind": kind, "id": it.get("dataset_id"), "title": t, "resources": [{"url": "%s/api/explore/v2.1/catalog/datasets/%s/exports/csv" % (base, it.get("dataset_id")), "format": "CSV"}],
                                      "columns": [f.get("name") for f in it.get("fields") or []], "keyword": kw})
                elif kind == "hub":
                    d = json.loads(get("%s/api/feed/dcat-us/1.1.json" % base, timeout=300)) if kw == KW[0] else {"dataset": []}
                    for it in d.get("dataset") or []:
                        t = it.get("title") or ""
                        if not re.search(r"purchase|contract|procure|award|payment|supplier|vendor|cheque", t, re.I):
                            continue
                        dist = [{"url": x.get("downloadURL") or x.get("accessURL"), "format": x.get("format") or x.get("mediaType")} for x in it.get("distribution") or []]
                        found.append({"buyer": buyer, "portal": base, "kind": kind, "id": it.get("identifier"), "title": t, "resources": dist[:6], "columns": [], "keyword": "dcat feed"})
            except Exception as e:
                print("  %s %s [%s]: %s" % (buyer, kind, kw, type(e).__name__), flush=True)
        print(buyer, "→", sum(1 for f in found if f["buyer"] == buyer), "candidates", flush=True)
    uniq = {}
    for f in found:
        uniq.setdefault((f["portal"], f["id"]), f)
    out = list(uniq.values())
    for f in out:
        f["po_like_columns"] = [c for c in f.get("columns") or [] if PO_COL.search(str(c))]
    return out


def harvest(sources, repo):
    """sources: [{buyer, url, format, po_col, vendor_col, date_col, amount_col, desc_col, delimiter?, encoding?}]"""
    out_rows = []
    for s in sources:
        try:
            data = get(s["url"], timeout=600)
        except Exception as e:
            print("download failed:", s["buyer"], s["url"][:90], type(e).__name__, flush=True); continue
        text = data.decode(s.get("encoding") or "utf-8-sig", "replace").replace("\0", "")
        if s.get("json_path"):
            recs = json.loads(text)
            for k in s["json_path"].split("."):
                recs = recs[k] if k else recs
            rows = recs
        else:
            rows = list(csv.DictReader(io.StringIO(text), delimiter=s.get("delimiter") or ","))
        n = 0
        if rows and not isinstance(rows, list):
            rows = list(rows)
        if rows and isinstance(rows[0], dict):
            import unicodedata
            def _k(k): return unicodedata.normalize("NFKD", str(k or "")).encode("ascii", "ignore").decode().strip().lower()
            keymap = {_k(k): k for k in rows[0].keys()}
            for ck in ("po_col", "vendor_col", "date_col", "amount_col", "desc_col"):
                if s.get(ck) and s[ck] not in rows[0] and _k(s[ck]) in keymap:
                    s[ck] = keymap[_k(s[ck])]
        for r in rows:
            po = str(r.get(s["po_col"]) or "").strip()
            vendor = str(r.get(s["vendor_col"]) or "").strip()
            if not po or not vendor or po.lower() in ("nan", "none", "null"):
                continue
            out_rows.append({"buyer": s["buyer"], "kind": s.get("kind", "po"), "id_label": s.get("id_label", ""), "vendor_name": vendor[:200], "po_number": po[:80], "date": str(r.get(s.get("date_col")) or "")[:10] if s.get("date_col") else "",
                             "amount": str(r.get(s.get("amount_col")) or "")[:30] if s.get("amount_col") else "", "description": str(r.get(s.get("desc_col")) or "")[:200] if s.get("desc_col") else "",
                             "source_url": s["url"], "source_title": s.get("title", ""), "retrieved_date": TODAY,
                             "source_quote": ("%s; %s; %s; %s" % (po, vendor, r.get(s.get("date_col")) if s.get("date_col") else "", r.get(s.get("amount_col")) if s.get("amount_col") else ""))[:300]})
            n += 1
        print(s["buyer"], "→", n, "PO rows", flush=True)
    out = os.path.join(repo, "data/incoming/claude/claude_po_records.csv.gz")  # gzipped: the plain CSV passed 170 MB, over GitHub's 100 MB file limit
    with gzip.open(out, "wt", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=["buyer", "kind", "id_label", "vendor_name", "po_number", "date", "amount", "description", "source_url", "source_title", "retrieved_date", "source_quote"])
        w.writeheader(); w.writerows(out_rows)
    print("wrote", out, len(out_rows), flush=True)


def main():
    a = argparse.ArgumentParser()
    a.add_argument("mode", choices=["discover", "harvest"])
    a.add_argument("--out", default=os.path.expanduser("~/cch-tasks/po_discovery.json"))
    a.add_argument("--sources", default="")
    a.add_argument("--repo", default=os.path.expanduser("~/cch-crawler"))
    a.add_argument("--only", default="", help="discover: only portals of this kind (ckan|socrata|ods|hub) or whose name contains this text")
    a = a.parse_args()
    if a.mode == "discover":
        if a.only:
            PORTALS[:] = [p for p in PORTALS if a.only in (p[1], p[0].lower()) or a.only.lower() in p[0].lower()]
        found = discover()
        json.dump(found, open(a.out, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
        for f in found:
            if f["po_like_columns"] or f["kind"] == "hub":
                print("*", f["buyer"], "|", f["title"][:60], "|", f["po_like_columns"][:4], "|", (f["resources"][0]["url"] if f["resources"] else "")[:90])
        print("wrote", a.out, len(found), "candidate datasets")
    else:
        harvest(json.load(open(a.sources, encoding="utf-8")), a.repo)


if __name__ == "__main__":
    main()
