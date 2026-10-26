#!/usr/bin/env python3
"""City of Toronto - Toronto Bids Awarded Contracts + Toronto Bids Non-Competitive Contracts (CKAN open data).
'Supplier Address' column exists but is empty in every row -> all records go to the unverified-country file.
Status: explicit period / term parsed from 'Solicitation Document Description' (awarded) anchored on
'Award Authority Obtained Date'; non-competitive: 'Contract Date' only -> end_date_unknown.
Multiple rows with the same Document Number + supplier are one award line each (kept separately: one record per row,
since each row is a distinct supplier/award amount).
Usage: python3 -I normalize.py <downloads_dir> <normalized_dir>
"""
import sys, os, json, collections, csv
from datetime import date
sys.path.insert(0, "scripts/_muni")
import terms

dl, outdir = sys.argv[1], sys.argv[2]
RET = "2026-10-25T17:19:07Z"
out = open(os.path.join(outdir, "ca_city_toronto_unverified_country.jsonl"), "w")
stats = collections.Counter()


def d(s):
    try:
        return date.fromisoformat((s or "")[:10])
    except Exception:
        return None


def money(s):
    try:
        return float(str(s).replace(",", "").replace("$", ""))
    except Exception:
        return None


def emit(rec, status):
    out.write(json.dumps(rec, ensure_ascii=False) + "\n")
    stats["emitted_" + status] += 1


# ---- awarded
for row in csv.DictReader(open(os.path.join(dl, "awarded-contracts-datastore.csv"), encoding="utf-8")):
    stats["awarded_rows"] += 1
    sup = (row.get("Successful Supplier") or "").strip()
    if not sup:
        stats["awarded_no_supplier"] += 1
        continue
    if (row.get("Supplier Address") or "").strip():
        stats["awarded_has_address"] += 1  # never seen; would need main-file routing
    anchor = d(row.get("Award Authority Obtained Date"))
    desc = row.get("Solicitation Document Description") or ""
    status, basis, st, en, kind = terms.decide(anchor, desc, "Award Authority Obtained Date")
    if status is None:
        stats["awarded_excluded_" + basis] += 1
        continue
    val = money(row.get("Award"))
    rid = f"ca_city_toronto:awarded:{row['_id']}"
    rec = {
        "record_id": rid,
        "source": {"key": "ca_city_toronto", "name": "Toronto Bids Awarded Contracts", "publisher": "City of Toronto (Purchasing & Materials Management Division), Open Data Toronto",
                   "dataset_url": "https://open.toronto.ca/dataset/tobids-awarded-contracts/",
                   "record_url": None, "retrieved_at": RET},
        "status": status, "status_basis": basis,
        "contract": {
            "identifiers": {"document_number": row.get("Document Number"), "open_data_row_id": row.get("_id")},
            "title": desc[:200] or None, "description": desc or None, "instrument_type": "contract",
            "procurement_method": "competitive", "solicitation_procedure": row.get("RFx (Solicitation) Type"),
            "commodity": {"toronto_high_level_category": row.get("High Level Category")},
            "value": val, "currency": "CAD" if val is not None else None, "value_detail": {"award": row.get("Award")},
            "dates": {"published": None, "signed": None, "awarded": anchor.isoformat() if anchor else None,
                      "start": st.isoformat() if st else None, "end": en.isoformat() if en else None, "end_kind": kind, "amended_last": None},
            "related": {"wards": row.get("Wards")},
        },
        "buyer": {"name": "City of Toronto - " + (row.get("Division") or "").strip() if row.get("Division") else "City of Toronto",
                  "country": "CA", "type": "city", "identifiers": {}, "address": {"city": "Toronto", "region": "ON"},
                  "contact": {"name": row.get("Buyer Name"), "email": row.get("Buyer Email"), "phone": row.get("Buyer Phone Number")}},
        "vendor": {"name": sup, "country": None, "country_basis": "not published (Supplier Address column empty)",
                   "identifiers": {}, "address": {"line1": None, "city": None, "region": None, "postal_code": None, "country": None}, "contact": {}},
        "raw": dict(row),
    }
    emit(rec, status)

# ---- non-competitive
for row in csv.DictReader(open(os.path.join(dl, "non-competitive-contracts.csv"), encoding="utf-8")):
    stats["noncomp_rows"] += 1
    sup = (row.get("Supplier Name") or "").strip()
    if not sup:
        stats["noncomp_no_supplier"] += 1
        continue
    anchor = d(row.get("Contract Date"))
    if anchor and anchor > terms.REF:
        stats["noncomp_excluded_future"] += 1
        continue
    status = "end_date_unknown"
    basis = f"Non-competitive contract published with 'Contract Date' {row.get('Contract Date')}; no end date or term published."
    val = money(row.get("Contract Amount"))
    rec = {
        "record_id": f"ca_city_toronto:noncompetitive:{row['_id']}",
        "source": {"key": "ca_city_toronto", "name": "Toronto Bids Non-Competitive Contracts", "publisher": "City of Toronto (Purchasing & Materials Management Division), Open Data Toronto",
                   "dataset_url": "https://open.toronto.ca/dataset/tobids-non-competitive-contracts/", "record_url": None, "retrieved_at": RET},
        "status": status, "status_basis": basis,
        "contract": {
            "identifiers": {"workspace_number": row.get("Workspace Number"), "open_data_row_id": row.get("_id")},
            "title": None, "description": None, "instrument_type": "contract", "procurement_method": "non-competitive",
            "solicitation_procedure": row.get("Reason"), "commodity": {},
            "value": val, "currency": "CAD" if val is not None else None, "value_detail": {"contract_amount": row.get("Contract Amount")},
            "dates": {"published": None, "signed": anchor.isoformat() if anchor else None, "start": anchor.isoformat() if anchor else None, "end": None, "amended_last": None},
            "related": {"wards": row.get("Wards")},
        },
        "buyer": {"name": "City of Toronto - " + (row.get("Division") or "").strip() if row.get("Division") else "City of Toronto",
                  "country": "CA", "type": "city", "identifiers": {}, "address": {"city": "Toronto", "region": "ON"}, "contact": {}},
        "vendor": {"name": sup, "country": None, "country_basis": "not published (Supplier Address column empty)",
                   "identifiers": {}, "address": {"line1": None, "city": None, "region": None, "postal_code": None, "country": None}, "contact": {}},
        "raw": dict(row),
    }
    emit(rec, status)

out.close()
json.dump(dict(stats), open(os.path.join(dl, "normalize_stats.json"), "w"), indent=1)
print(json.dumps(dict(stats), indent=1))
