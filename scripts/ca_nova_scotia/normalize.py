#!/usr/bin/env python3
"""Nova Scotia open data 'Awarded Public Tenders' (Socrata m6ps-8j6u) -> unverified-country records.
No vendor address/country column -> every record goes to normalized/ca_nova_scotia_unverified_country.jsonl
(vendor.country null, basis 'not published'). Status from TENDER_DESCRIPTION term/period (shared parser) anchored on
AWARDED_DATE, else end_date_unknown.
Usage: python3 -I normalize.py <downloads_dir> <normalized_dir>
"""
import sys, os, csv, json, hashlib, html, collections, urllib.parse
from datetime import date
sys.path.insert(0, "scripts/_muni")
import terms

dl, outdir = sys.argv[1], sys.argv[2]
RET = open(os.path.join(dl, "retrieved_at.txt")).read().strip()
out = open(os.path.join(outdir, "ca_nova_scotia_unverified_country.jsonl"), "w")
stats = collections.Counter()


def d(s):
    try:
        y, m, dd = (s or "").strip()[:10].split("/")
        return date(int(y), int(m), int(dd))
    except Exception:
        return None


for row in csv.DictReader(open(os.path.join(dl, "m6ps-8j6u.csv"), encoding="utf-8")):
    stats["rows"] += 1
    vendor = html.unescape((row.get("VENDOR") or "").strip())
    buyer = html.unescape((row.get("ENTITY") or "").strip())
    if not vendor or vendor.strip(" .").upper() in ("N/A", "NA", "VARIOUS", "NONE", "TBD", "CANCELLED", "CANCELED", "NO AWARD", "NOT AWARDED", "-", "MULTIPLE", "SEE ATTACHED"):
        stats["no_vendor_or_placeholder"] += 1
        continue
    if not buyer:
        stats["no_buyer"] += 1
        continue
    desc = html.unescape(row.get("TENDER_DESCRIPTION") or "")
    aw = d(row.get("AWARDED_DATE"))
    status, basis, st, en, kind = terms.decide(aw, desc, "AWARDED_DATE")
    if status is None:
        stats["excluded_" + basis] += 1
        continue
    try:
        val = float(row.get("AWARDED_AMOUNT"))
    except Exception:
        val = None
    h = hashlib.sha1(json.dumps(row, sort_keys=True).encode()).hexdigest()[:10]
    tid = row.get("TENDER_ID")
    kinds = [k for k in ("GOODS", "SERVICE", "CONSTRUCTION") if (row.get(k) or "").upper() == "Y"]
    rec = {
        "record_id": f"ca_nova_scotia:{tid}:{h}",
        "source": {"key": "ca_nova_scotia", "name": "Awarded Public Tenders (Nova Scotia open data, m6ps-8j6u)",
                   "publisher": "Province of Nova Scotia - Procurement Services (data.novascotia.ca)",
                   "dataset_url": "https://data.novascotia.ca/Government-Administration/Awarded-Public-Tenders/m6ps-8j6u",
                   "record_url": "https://data.novascotia.ca/resource/m6ps-8j6u.json?tender_id=" + urllib.parse.quote(tid or ""),
                   "retrieved_at": RET},
        "status": status, "status_basis": basis,
        "contract": {
            "identifiers": {"tender_id": tid},
            "title": desc or None, "description": desc or None, "instrument_type": "contract",
            "procurement_method": "public tender", "solicitation_procedure": None,
            "commodity": {"ns_type": "/".join(kinds) or None},
            "value": val, "currency": "CAD" if val is not None else None, "value_detail": {"awarded_amount": row.get("AWARDED_AMOUNT")},
            "dates": {"published": d(row.get("TENDER_START_DATE")).isoformat() if d(row.get("TENDER_START_DATE")) else None,
                      "tender_close": d(row.get("TENDER_CLOSE_DATE")).isoformat() if d(row.get("TENDER_CLOSE_DATE")) else None,
                      "signed": None, "awarded": aw.isoformat() if aw else None,
                      "start": st.isoformat() if (st and kind) else None, "end": en.isoformat() if en else None, "amended_last": None},
            "related": {},
        },
        "buyer": {"name": buyer, "country": "CA", "type": "Nova Scotia public sector entity (department, agency, health, education, municipality as named)",
                  "identifiers": {}, "address": {"region": "NS"}, "contact": {}},
        "vendor": {"name": vendor, "country": None, "country_basis": "not published (dataset has no vendor address/country column)",
                   "identifiers": {}, "address": {"line1": None, "city": None, "region": None, "postal_code": None, "country": None}, "contact": {}},
        "raw": dict(row),
    }
    out.write(json.dumps(rec, ensure_ascii=False) + "\n")
    stats["emitted_" + status] += 1

out.close()
json.dump(dict(stats), open(os.path.join(dl, "normalize_stats.json"), "w"), indent=1)
print(json.dumps(dict(stats), indent=1))
