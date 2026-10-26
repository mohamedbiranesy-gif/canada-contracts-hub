#!/usr/bin/env python3
"""Socrata Discovery API term sweep -> compact dataset metadata (gzip JSONL), deduped by (domain,id).
usage: python3 -I socrata_terms.py <out.jsonl.gz> [mode=terms|domains] [domains_file]
"""
import sys, json, time, gzip, urllib.parse, urllib.request, os
UA = "contracts-research/1.0"
API = "https://api.us.socrata.com/api/catalog/v1"
TERMS = ["contract", "contracts", "contractor", "contractors", "contract awards", "awarded contracts", "award", "awards",
         "agreement", "agreements", "purchase order", "purchase orders", "purchasing", "procurement", "purchases",
         "vendor", "vendors", "supplier", "suppliers", "payee", "payees", "encumbrance", "encumbrances", "checkbook",
         "check register", "ledger", "expenditure", "expenditures", "spending", "spend", "payment", "payments",
         "disbursement", "disbursements", "accounts payable", "invoice", "invoices", "warrant", "warrants",
         "obligation", "obligations", "bid", "bids", "solicitation", "sole source", "professional services",
         "transparency", "open book", "purchasing card", "p-card", "blanket", "master agreement", "cooperative contract",
         "statewide contract", "consultant", "consulting", "expense", "expenses", "transactions", "general ledger",
         "commitments", "requisition", "goods and services", "services agreement", "lease", "concession", "PO",
         "open checkbook", "vendor payments", "spending data", "financial transactions", "supplier payments"]

def get(url, tries=5):
    last = None
    for i in range(tries):
        try:
            with urllib.request.urlopen(urllib.request.Request(url, headers={"User-Agent": UA}), timeout=180) as r:
                return json.loads(r.read().decode("utf-8"))
        except Exception as e:
            last = e; time.sleep(3 * (i + 1))
    raise last

def compact(x):
    r = x["resource"]; c = x.get("classification", {}); m = x.get("metadata", {})
    return {"domain": m.get("domain"), "id": r.get("id"), "name": r.get("name"), "type": r.get("type"),
            "description": (r.get("description") or "")[:600], "attribution": r.get("attribution"),
            "updatedAt": r.get("updatedAt"), "data_updated_at": r.get("data_updated_at"), "createdAt": r.get("createdAt"),
            "cols_field": r.get("columns_field_name") or [], "cols_name": r.get("columns_name") or [],
            "cols_type": r.get("columns_datatype") or [], "cols_desc": [(d or "")[:120] for d in (r.get("columns_description") or [])],
            "category": c.get("domain_category"), "tags": c.get("domain_tags") or [], "link": x.get("link"),
            "permalink": x.get("permalink"), "provenance": r.get("provenance"), "lens_view_type": r.get("lens_view_type"),
            "download_count": r.get("download_count"), "page_views_total": (r.get("page_views") or {}).get("page_views_total")}

def main():
    out = sys.argv[1]; mode = sys.argv[2] if len(sys.argv) > 2 else "terms"
    seen = set()
    if os.path.exists(out):
        with gzip.open(out, "rt", encoding="utf-8") as f:
            for l in f:
                j = json.loads(l); seen.add((j["domain"], j["id"]))
    log = open(out + ".log", "a")
    fo = gzip.open(out, "at", encoding="utf-8")
    if mode == "terms":
        jobs = [{"q": t} for t in TERMS]
    else:
        doms = [l.strip() for l in open(sys.argv[3]) if l.strip()]
        jobs = [{"domains": d} for d in doms]
    done_f = out + f".{mode}.done"
    done = set(l.strip() for l in open(done_f)) if os.path.exists(done_f) else set()
    df = open(done_f, "a")
    for jb in jobs:
        key = json.dumps(jb, sort_keys=True)
        if key in done:
            continue
        p = dict(jb); p.update({"only": "dataset", "limit": 10000})
        if "domains" in jb:
            p["search_context"] = jb["domains"]
        try:
            j = get(API + "?" + urllib.parse.urlencode(p))
        except Exception as e:
            log.write(f"ERR {key} {e}\n"); log.flush(); continue
        res = j.get("results", []); new = 0
        for x in res:
            c = compact(x)
            k = (c["domain"], c["id"])
            if k in seen:
                continue
            seen.add(k); new += 1
            fo.write(json.dumps(c, ensure_ascii=False) + "\n")
        fo.flush()
        log.write(f"{time.strftime('%H:%M:%S')} {key} total={j.get('resultSetSize')} got={len(res)} new={new} seen={len(seen)}\n"); log.flush()
        df.write(key + "\n"); df.flush()
        time.sleep(0.5)
    fo.close()
    print("seen", len(seen))

if __name__ == "__main__":
    main()
