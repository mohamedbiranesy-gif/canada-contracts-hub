#!/usr/bin/env python3
"""Normalize Alberta 'Sole-source service contracts' disclosure (CSV export of the OData service).
Usage: python3 -I normalize_ab_sole_source.py <csv_path> <retrieved_at> <out_jsonl> <stats_json>
"""
import csv, json, sys, re, hashlib, datetime as dt, collections

CSV, RETRIEVED, OUT, STATS = sys.argv[1:5]
REF = dt.date(2026, 10, 25)
PROV = {"alberta": "AB", "british columbia": "BC", "saskatchewan": "SK", "manitoba": "MB", "ontario": "ON",
        "quebec": "QC", "québec": "QC", "new brunswick": "NB", "nova scotia": "NS", "prince edward island": "PE",
        "newfoundland and labrador": "NL", "yukon": "YT", "northwest territories": "NT", "nunavut": "NU"}


def pdate(s):
    s = (s or "").strip()
    if not s:
        return None
    try:
        return dt.datetime.strptime(s.split()[0], "%m/%d/%Y").date().isoformat()
    except ValueError:
        return None


def money(s):
    try:
        return float(str(s).replace(",", "").replace("$", "").strip())
    except Exception:
        return None


def main():
    stats = collections.Counter()
    rows = list(csv.DictReader(open(CSV, encoding="utf-8-sig", newline="")))
    out = open(OUT, "w")
    seen = set()
    for r in rows:
        r = {k: v for k, v in r.items() if k is not None and k != ""}
        stats["rows_total"] += 1
        country = (r.get("vendorCountry") or "").strip()
        if country.lower() not in ("canada", "ca"):
            stats["skip_vendor_country_not_canada"] += 1
            continue
        start, end = pdate(r.get("startDate")), pdate(r.get("endDate"))
        if not start or not end:
            stats["skip_unparseable_dates"] += 1
            continue
        if end < REF.isoformat():
            stats["skip_ended"] += 1
            continue
        if start > REF.isoformat():
            stats["skip_not_started"] += 1
            continue
        key = "|".join([r.get("contractNumber", ""), r.get("department", ""), r.get("vendor", ""), start, end, r.get("contractAmount", ""), r.get("fiscalYear", ""), r.get("special", "")])
        rid = "ca_alberta_sole_source:" + hashlib.sha1(key.encode()).hexdigest()[:16]
        if rid in seen:
            stats["dup"] += 1
            continue
        seen.add(rid)
        prov_raw = (r.get("vendorProvince") or "").strip()
        prov = PROV.get(prov_raw.lower(), prov_raw.upper() if len(prov_raw) == 2 else prov_raw or None)
        amount = money(r.get("contractAmount"))
        special = (r.get("special") or "").strip().lower() == "true"
        rec = {
            "record_id": rid,
            "source": {
                "key": "ca_alberta_sole_source",
                "name": "Alberta Sole-source service contracts disclosure (contracts >= $10,000; %s)" % ("direct human services and supports" if special else "government business"),
                "publisher": "Government of Alberta (Treasury Board and Finance / Service Alberta) via open.alberta.ca",
                "dataset_url": "https://open.alberta.ca/opendata/sole-source-service-contracts",
                "record_url": None,
                "retrieved_at": RETRIEVED,
            },
            "status": "ongoing",
            "status_basis": "startDate %s <= 2026-10-25 <= endDate %s (both explicit fields in the disclosure)" % (start, end),
            "contract": {
                "identifiers": {"contract_number": (r.get("contractNumber") or "").strip() or None},
                "title": (r.get("contractServices") or "").strip()[:200] or None,
                "description": (r.get("contractServices") or "").strip() or None,
                "instrument_type": "sole-source service contract",
                "procurement_method": "sole source (non-competitive)",
                "solicitation_procedure": "permitted situation code '%s' (Alberta sole-source disclosure exception letter)" % (r.get("permittedSituations") or "").strip(),
                "commodity": {},
                "value": amount, "currency": "CAD" if amount is not None else None,
                "value_detail": {"contract_amount": amount} if amount is not None else {},
                "dates": {"published": None, "signed": None, "start": start, "end": end, "amended_last": None},
                "related": {"fiscal_year": r.get("fiscalYear"), "special_direct_human_services": special,
                            "odata_service": "http://sole-source.dataservices.alberta.ca/SoleSourceDataService.svc/" + ("DisplaySpecialContracts" if special else "DisplayContracts"),
                            "disclosure_table_url": "https://www.alberta.ca/sole-source-contracts-disclosure-table"},
            },
            "buyer": {
                "name": (r.get("department") or "").strip(), "country": "CA", "type": "Alberta provincial government department",
                "identifiers": {},
                "address": {"line1": (r.get("departmentStreet") or "").strip() or None, "line2": (r.get("departmentStreet2") or "").strip() or None,
                            "city": (r.get("departmentCity") or "").strip() or None, "region": (r.get("departmentProvince") or "").strip() or None,
                            "postal_code": (r.get("departmentPostalCode") or "").strip() or None, "country": (r.get("departmentCountry") or "").strip() or None},
                "contact": {},
            },
            "vendor": {
                "name": (r.get("vendor") or "").strip(), "country": "CA", "country_basis": "vendorCountry == %r" % country,
                "identifiers": {},
                "address": {"line1": (r.get("vendorStreet") or "").strip() or None, "line2": (r.get("vendorStreet2") or "").strip() or None,
                            "city": (r.get("vendorCity") or "").strip() or None, "region": prov,
                            "postal_code": (r.get("vendorPostalCode") or "").strip() or None, "country": country},
                "contact": {},
            },
            "raw": r,
        }
        if not rec["buyer"]["name"] or not rec["vendor"]["name"]:
            stats["skip_blank_party"] += 1
            continue
        out.write(json.dumps(rec, ensure_ascii=False) + "\n")
        stats["emitted_ongoing"] += 1
        stats["end_year_" + end[:4]] += 1
    out.close()
    json.dump(dict(stats), open(STATS, "w"), indent=1)
    print(json.dumps(dict(stats), indent=1))


if __name__ == "__main__":
    main()
