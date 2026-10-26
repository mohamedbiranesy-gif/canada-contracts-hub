#!/usr/bin/env python3
"""Normalize NBON award rows (downloads/ca_new_brunswick/nbon/awards.jsonl) into
normalized/ca_new_brunswick.jsonl (+ ca_new_brunswick_unverified_country.jsonl).
Usage: python3 -I normalize.py <awards.jsonl> <out.jsonl> <out_unverified.jsonl> <stats.json>
"""
import sys, re, json, collections, datetime

src, out_p, outu_p, stats_p = sys.argv[1:5]
REF = datetime.date(2026, 10, 25)
PROV = {"NB": "NB", "N.B.": "NB", "N.B": "NB", "NEW BRUNSWICK": "NB", "NS": "NS", "N.S.": "NS", "NOVA SCOTIA": "NS", "PE": "PE", "P.E.I.": "PE", "PEI": "PE",
        "PRINCE EDWARD ISLAND": "PE", "NL": "NL", "NFLD": "NL", "NFLD.": "NL", "NEWFOUNDLAND": "NL", "QC": "QC", "QUE": "QC", "QUE.": "QC", "QUEBEC": "QC", "QUÉBEC": "QC",
        "PQ": "QC", "ON": "ON", "ONT": "ON", "ONT.": "ON", "ONTARIO": "ON", "MB": "MB", "MAN.": "MB", "MANITOBA": "MB", "SK": "SK", "SASK.": "SK", "SASKATCHEWAN": "SK",
        "AB": "AB", "ALTA.": "AB", "ALBERTA": "AB", "BC": "BC", "B.C.": "BC", "BRITISH COLUMBIA": "BC", "YT": "YT", "YUKON": "YT", "NT": "NT", "NWT": "NT", "NU": "NU", "NUNAVUT": "NU"}
US = {"AL", "AK", "AZ", "AR", "CO", "CT", "DE", "FL", "GA", "HI", "ID", "IL", "IN", "IA", "KS", "KY", "LA", "ME", "MD", "MA", "MI", "MN", "MS", "MO", "MT", "NE", "NV",
      "NH", "NJ", "NM", "NY", "NC", "ND", "OH", "OK", "OR", "PA", "RI", "SC", "SD", "TN", "TX", "UT", "VT", "VA", "WA", "WV", "WI", "WY", "DC"}
stats = collections.Counter(); by_status = collections.Counter(); by_status_u = collections.Counter()


def money(s):
    s = (s or "").replace("$", "").replace(",", "").strip()
    try:
        return float(s)
    except ValueError:
        return None


def d(s):
    try:
        return datetime.datetime.strptime((s or "").strip(), "%Y/%m/%d").date().isoformat()
    except ValueError:
        return None


fo = open(out_p, "w", encoding="utf-8"); fu = open(outu_p, "w", encoding="utf-8")
for line in open(src, encoding="utf-8"):
    t = json.loads(line)
    stats["tenders"] += 1
    if not t.get("awards"):
        stats["tenders_without_award_rows"] += 1
        continue
    for i, a in enumerate(t["awards"], 1):
        stats["award_rows"] += 1
        L = a.get("vendor_block_lines") or []
        vnum = L[0] if len(L) >= 3 else None
        vname = L[1] if len(L) >= 3 else (L[0] if L else None)
        vloc = L[2] if len(L) >= 3 else (L[1] if len(L) == 2 else None)
        extra = L[3:] if len(L) > 3 else []
        city, region_tok = None, None
        if vloc:
            parts = [p.strip() for p in vloc.split(",")]
            region_tok = parts[-1].upper() if len(parts) >= 2 else None
            city = ", ".join(parts[:-1]) if len(parts) >= 2 else vloc
        prov = PROV.get(region_tok or "")
        if region_tok in US:
            stats["excluded_vendor_us_state"] += 1
            stats["vendor_region_excluded:" + region_tok] += 1
            continue
        da = d(a.get("date_awarded"))
        if da and da > REF.isoformat():
            stats["excluded_future_award"] += 1
            continue
        status = "end_date_unknown"
        basis = (f"end_date_unknown: NBON bid result publishes award total and Date Awarded {a.get('date_awarded') or 'n/a'} (tender closing {t.get('closing_date') or 'n/a'}) "
                 "but no contract end date, term or duration")
        rec = {"record_id": f"ca_new_brunswick:{t.get('tender_number')}:{t.get('disID')}:{i}",
               "source": {"key": "ca_new_brunswick", "name": "New Brunswick Opportunities Network (NBON) - Browse Bid Results (Awards Only)",
                          "publisher": "Service New Brunswick (Strategic Procurement) / Government of New Brunswick",
                          "dataset_url": "https://nbon-rpanb.gnb.ca/", "record_url": None, "retrieved_at": t.get("retrieved_at")},
               "status": status, "status_basis": basis,
               "contract": {"identifiers": {"nbon_tender_number": t.get("tender_number"), "nbon_document_id": t.get("disID"), "award_row": i},
                            "title": t.get("title"), "description": None, "instrument_type": "contract",
                            "procurement_method": "Competitive - public tender (NBON)", "solicitation_procedure": None,
                            "commodity": {}, "value": money(a.get("award_total_incl_hst")), "currency": "CAD",
                            "value_detail": {"award_total_incl_hst": money(a.get("award_total_incl_hst")), "value_basis": "NBON 'Award Total (Includes HST)'"},
                            "dates": {"published": None, "signed": da, "start": None, "end": None, "amended_last": None,
                                      "tender_closing": d(t.get("closing_date"))},
                            "related": {}},
               "buyer": {"name": t.get("issuing_organization"), "country": "CA", "type": "province (central procurement agency)" if "Strategic Procurement" in (t.get("issuing_organization") or "") else "provincial body",
                         "identifiers": {"nbon_issuing_organization": t.get("issuing_organization"),
                                         "parent": "Service New Brunswick / Government of New Brunswick" if "Strategic Procurement" in (t.get("issuing_organization") or "") else None},
                         "address": {"region": "NB", "country": "CA"},
                         "contact": {"purchasing_agent_lines": t.get("purchasing_agent_lines")}},
               "vendor": {"name": vname, "country": "CA" if prov else None,
                          "country_basis": (f"NBON Successful Vendor location line {vloc!r} ends with Canadian province '{region_tok}'" if prov else
                                            f"not determinable: vendor location line {vloc!r} has no Canadian province or US state token"),
                          "identifiers": {"nbon_vendor_number": vnum},
                          "address": {"city": city, "region": prov or region_tok, "country": "CA" if prov else None, "location_line": vloc,
                                      "extra_lines": extra or None},
                          "contact": {}},
               "raw": {"nbon_tender": {k: v for k, v in t.items() if k != "awards"}, "nbon_award_row": a, "nbon_award_rows_all": t.get("awards")}}
        if prov:
            fo.write(json.dumps(rec, ensure_ascii=False) + "\n"); by_status[status] += 1; stats["records_main"] += 1
        else:
            fu.write(json.dumps(rec, ensure_ascii=False) + "\n"); by_status_u[status] += 1; stats["records_unverified"] += 1
            stats["unverified_region:" + str(region_tok)] += 1
fo.close(); fu.close()
json.dump({"stats": stats, "by_status": by_status, "by_status_unverified": by_status_u}, open(stats_p, "w"), indent=1)
print(json.dumps({"stats": stats, "by_status": by_status, "by_status_unverified": by_status_u}))
