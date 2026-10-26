#!/usr/bin/env python3
"""Enumerate Socrata datasets (api.us.socrata.com Discovery API) by keyword and by exact column name.
usage: python3 -I socrata_enum.py <out.jsonl>
Writes one JSON line per unique dataset (condensed metadata + which queries hit it)."""
import json, sys, time, urllib.parse, urllib.request
UA = "contracts-research/1.0"
API = "https://api.us.socrata.com/api/catalog/v1"
KW = ["contract", "contracts", "purchase order", "purchase orders", "procurement", "vendor", "vendors", "award",
      "awards", "agreement", "agreements", "encumbrance", "encumbrances", "checkbook", "check register", "payments",
      "vendor payments", "expenditure", "expenditures", "spending", "supplier", "suppliers", "accounts payable",
      "purchasing", "purchases", "bid", "bids", "solicitation", "disbursement", "disbursements", "ledger", "invoice",
      "invoices", "payee", "contractor", "contractors", "open checkbook", "warrant register", "check detail",
      "payment register", "claims paid", "p-card", "purchasing card", "blanket", "master agreement", "spend",
      "expense", "expenses", "transparency", "open expenditures", "open finance", "vendor list", "vendor master"]
COLS = ["vendor_state", "vendor_country", "vendor_province", "vendor_zip", "vendor_zip_code", "vendor_zipcode",
        "vendor_postal_code", "vendor_postal", "vendorstate", "vendorcountry", "vendorzip", "vendor_st", "vendor_ctry",
        "vendor_address_state", "vendor_address_country", "vendor_address_postal", "vendor_city", "vendor_address",
        "vendor_address_1", "vendor_address1", "vendor_state_code", "vendor_country_code", "vend_state", "vend_country",
        "ven_state", "ven_country", "supplier_state", "supplier_country", "supplier_zip", "supplier_postal_code",
        "supplier_city", "supplier_address", "supplier_province", "payee_state", "payee_country", "payee_zip",
        "payee_city", "payee_address", "contractor_state", "contractor_country", "contractor_zip", "contractor_city",
        "contractor_state_province", "contractor_address", "merchant_state", "merchant_country", "merchant_zip",
        "remit_state", "remit_to_state", "remit_country", "remittance_state", "company_state", "company_country",
        "business_state", "business_country", "recipient_state", "recipient_country", "vendor_state_province",
        "state_province", "province", "ctry", "country", "country_code", "vendor_region", "vendor_location",
        "payee_state_code", "vendor_mailing_state", "mailing_country", "vendor_address_line_1", "zip_code_vendor",
        "st", "vendor_zip5", "vendor_postalcode", "postal_code", "vendor_state_abbr", "vendorstatecode"]

def get(params):
    u = API + "?" + urllib.parse.urlencode(params)
    for a in range(5):
        try:
            with urllib.request.urlopen(urllib.request.Request(u, headers={"User-Agent": UA}), timeout=90) as r:
                return json.loads(r.read().decode("utf-8"))
        except Exception as e:
            print("retry", a, params, e, file=sys.stderr); time.sleep(3 * (a + 1))
    return {"results": [], "resultSetSize": 0}

seen = {}
def add(x, tag):
    r = x["resource"]; m = x["metadata"]; c = x.get("classification", {})
    k = m.get("domain", "") + "/" + r["id"]
    if k not in seen:
        seen[k] = {"domain": m.get("domain"), "id": r["id"], "name": r.get("name"), "type": r.get("type"),
                   "description": (r.get("description") or "")[:600], "updatedAt": r.get("updatedAt"),
                   "data_updated_at": r.get("data_updated_at"), "createdAt": r.get("createdAt"),
                   "cols": r.get("columns_field_name", []), "col_names": r.get("columns_name", []),
                   "col_types": r.get("columns_datatype", []), "category": c.get("domain_category"),
                   "tags": c.get("domain_tags", [])[:15], "link": x.get("link"), "permalink": x.get("permalink"),
                   "attribution": r.get("attribution"), "download_count": r.get("download_count"),
                   "provenance": r.get("provenance"), "parent_fxf": r.get("parent_fxf"), "hits": []}
    seen[k]["hits"].append(tag)

def sweep(params, tag):
    off = 0; total = None
    while True:
        p = dict(params); p.update({"only": "dataset", "limit": 100, "offset": off})
        j = get(p)
        res = j.get("results", [])
        total = j.get("resultSetSize", 0)
        for x in res:
            add(x, tag)
        off += len(res)
        time.sleep(0.5)
        if not res or off >= total or off >= 9900:
            break
    print(f"{tag}\t{total}\t{off}", file=sys.stderr, flush=True)

for q in KW:
    sweep({"q": q}, "q:" + q)
for c in COLS:
    sweep({"column_names": c}, "col:" + c)
with open(sys.argv[1], "w") as fo:
    for k, v in seen.items():
        fo.write(json.dumps(v, ensure_ascii=False) + "\n")
print("unique", len(seen), file=sys.stderr)
