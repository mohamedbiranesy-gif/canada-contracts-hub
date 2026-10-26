#!/usr/bin/env python3
"""Tenders WA Contract Award Details (data.wa.gov.au) -> Canadian-supplier records (Supplier_Address with Canadian postal code)."""
import csv, json, re, sys, datetime, os, collections
REF = datetime.date(2026, 10, 25)
PC = re.compile(r"\b([ABCEGHJ-NPRSTVXY]\d[ABCEGHJ-NPRSTV-Z]) ?(\d[ABCEGHJ-NPRSTV-Z]\d)\s*$", re.I)
PROV = re.compile(r"\b(Ontario|Quebec|Québec|British Columbia|Alberta|Manitoba|Saskatchewan|Nova Scotia|New Brunswick|Newfoundland|Canada)\b", re.I)
URLS = {"wa_2021_22.csv": "https://catalogue.data.wa.gov.au/dataset/cab2f08c-6776-4328-b4b3-776f1f88eb3a/resource/2f29a5b8-ad39-465a-8374-84cbe5a2afc9/download/tenders-wa-contract-award-details-2021-22-financial-year.csv",
        "wa_2022_23.csv": "https://catalogue.data.wa.gov.au/dataset/a66013f6-07db-433b-bc6a-984b249a1013/resource/063fa676-4ae3-48dd-ad0b-0e207182abf8/download/tenders-wa-contract-award-details-2022-23-financial-year.csv",
        "wa_2023_24.csv": "https://catalogue.data.wa.gov.au/dataset/90b272e8-9ae0-4995-8dc9-86f8249b51d1/resource/855378f8-0398-4a0a-a1c2-218816508ec9/download/tenders-wa-contract-award-details-2023-24-financial-year.csv"}
def dmy(s):
    m = re.match(r"\s*(\d{1,2})/(\d{1,2})/(\d{4})", s or "")
    if not m: return None
    try: return datetime.date(int(m.group(3)), int(m.group(2)), int(m.group(1)))
    except ValueError: return None
out = open(sys.argv[1], "w", encoding="utf-8"); st = collections.Counter(); ex = []
seen = set()
for f in sys.argv[2:]:
    fn = os.path.basename(f)
    retrieved = datetime.datetime.fromtimestamp(os.path.getmtime(f), datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    for row in csv.DictReader(open(f, encoding="utf-8-sig", errors="replace")):
        st["rows"] += 1
        addr = (row.get("Supplier_Address") or "").strip()
        m = PC.search(addr)
        if not m: continue
        st["canadian_postcode_rows"] += 1
        start = dmy(row["Commencement_Date"]) or dmy(row["Award_Date"])
        end = dmy(row["Final_Expiry_Date"]) or dmy(row["Initial_Expiry_Date"])
        if end and end < REF:
            st["excluded_ended"] += 1; ex.append((row["Reference_Number"], row["Supplier_Name"], str(end))); continue
        if start and start > REF:
            st["excluded_future"] += 1; continue
        if end:
            status = "ongoing"; basis = "Commencement_Date %s <= 2026-10-25 <= Final_Expiry_Date %s (Initial_Expiry_Date %s)" % (row["Commencement_Date"], row["Final_Expiry_Date"], row["Initial_Expiry_Date"])
        else:
            status = "end_date_unknown"; basis = "no expiry date published"
        st[status] += 1
        parts = [p.strip() for p in addr.split(",")]
        rid = "au_wa:%s:%s" % (row["Reference_Number"], re.sub(r"\W+", "_", row["Supplier_Name"])[:40])
        if rid in seen: rid += ":" + fn
        seen.add(rid)
        val = float(row["Original_Contract_Value"]) if re.match(r"^[\d.]+$", row["Original_Contract_Value"] or "") else None
        rec = {"record_id": rid,
          "source": {"key": "au_wa", "name": "Tenders WA Contract Award Details (Western Australia, per financial year)", "publisher": "Department of Finance, Government of Western Australia (via data.wa.gov.au)",
                     "dataset_url": "https://catalogue.data.wa.gov.au/dataset/?q=tenders+wa+contract+award+details", "record_url": None, "retrieved_at": retrieved},
          "status": status, "status_basis": basis,
          "contract": {"identifiers": {"reference_number": row["Reference_Number"], "cua_number": row["CUA_Number"] or None, "associated_with_tender": row["Associated_With_Tender"] or None},
            "title": row["Title"], "description": row["Description"], "instrument_type": "contract (%s%s)" % (row["Contract_Term"], ", panel" if row["Panel_Contract"] == "Yes" else ""),
            "procurement_method": row["Procurement_Method"], "solicitation_procedure": row["Procurement_Method"],
            "commodity": {"unspsc": row["UNSPSC_Code_1"], "unspsc_description": row["UNSPSC_Title_1"]},
            "value": val, "currency": "AUD", "value_detail": {"original_contract_value": val, "value_type": row["Original_Contract_Value_Type"]},
            "dates": {"published": None, "signed": None, "award": (dmy(row["Award_Date"]) or "") and dmy(row["Award_Date"]).isoformat(), "start": start.isoformat() if start else None, "end": end.isoformat() if end else None,
                      "initial_expiry": (dmy(row["Initial_Expiry_Date"]).isoformat() if dmy(row["Initial_Expiry_Date"]) else None), "tender_closing": (dmy(row["Closing_Date"]).isoformat() if dmy(row["Closing_Date"]) else None), "amended_last": None},
            "related": {"source_csv": URLS.get(fn)}},
          "buyer": {"name": row["Public_Authority"], "country": "AU", "type": "Western Australian state public authority", "identifiers": {}, "address": {"line1": row["Public_Authority_Address"]}, "contact": {}},
          "vendor": {"name": row["Supplier_Name"], "country": "CA", "country_basis": "Supplier_Address ends with a Canadian postal code (%s %s)%s" % (m.group(1).upper(), m.group(2).upper(), "; province/country token: " + PROV.search(addr).group(0) if PROV.search(addr) else ""),
                     "identifiers": {}, "address": {"line1": ", ".join(parts[:-2]) if len(parts) > 2 else parts[0], "city": parts[-2] if len(parts) >= 2 else None, "region": None, "postal_code": (m.group(1) + " " + m.group(2)).upper(), "country": None}, "contact": {}},
          "raw": {"source_file": fn, **row}}
        out.write(json.dumps(rec, ensure_ascii=False) + "\n")
st["excluded_examples"] = ex[:20]
json.dump(st, open("downloads/au_wa/normalize_stats.json", "w"), indent=1)
print(dict(st))
