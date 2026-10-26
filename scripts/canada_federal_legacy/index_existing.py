#!/usr/bin/env python3
"""Build a compact identifier index of normalized/canada_federal.jsonl (streamed) for de-duplication.

Contract-level identifiers only (NOT solicitation numbers, NOT pd_standing_offer_number, which is the parent SO/SA of a
call-up): pd_procurement_id, pd_reference_numbers, pd_additional_groups[].procurement_id, ch_reference_number,
ch_contract_number, ch_additional_reference_numbers, an_reference_number_latest, an_reference_numbers, an_contract_number.
Also keeps every proactive-disclosure row's procurement_id / reference_number from raw.

Usage: python3 -I index_existing.py <canada_federal.jsonl> <out.jsonl.gz>
Output lines: {"record_id", "status", "ids": [alnum ids], "ids_orig": {alnum: original}, "vendors": [names],
               "buyer": name, "end": date, "instrument": str}
"""
import sys, json, gzip, re

src, out = sys.argv[1], sys.argv[2]


def alnum(s):
    return re.sub(r"[^A-Z0-9]", "", (s or "").upper())


DEGEN = {"", "NULL", "NA", "NONE", "0", "TBD", "UNKNOWN", "ACQUISITIONCARD", "ACQUISITIONCARDS", "VARIOUS", "MULTIPLE"}
n = 0
with open(src, encoding="utf-8") as f, gzip.open(out, "wt", encoding="utf-8") as fo:
    for line in f:
        try:
            r = json.loads(line)
        except Exception:
            continue
        n += 1
        ci = r.get("contract", {}).get("identifiers", {}) or {}
        vals = []
        for k in ["pd_procurement_id", "ch_reference_number", "ch_contract_number", "an_reference_number_latest", "an_contract_number"]:
            if ci.get(k):
                vals.append((k, ci[k]))
        for k in ["pd_reference_numbers", "ch_additional_reference_numbers", "an_reference_numbers"]:
            for v in ci.get(k) or []:
                if isinstance(v, str) and not v.startswith("... ("):
                    vals.append((k, v))
        for g in ci.get("pd_additional_groups") or []:
            if g.get("procurement_id"):
                vals.append(("pd_additional_groups.procurement_id", g["procurement_id"]))
        raw = r.get("raw", {}) or {}
        pdr = raw.get("proactive_disclosure") or {}
        rows = pdr.get("rows") if isinstance(pdr, dict) else (pdr if isinstance(pdr, list) else [])
        for row in rows or []:
            if isinstance(row, dict):
                if row.get("procurement_id"):
                    vals.append(("raw.pd.procurement_id", row["procurement_id"]))
                if row.get("reference_number"):
                    vals.append(("raw.pd.reference_number", row["reference_number"]))
        for key in ["canadabuys_contract_history", "canadabuys_award_notice"]:
            x = raw.get(key)
            rows = x.get("rows") if isinstance(x, dict) else (x if isinstance(x, list) else [])
            for row in rows or []:
                if isinstance(row, dict):
                    for fld in ["contractNumber-numeroContrat", "referenceNumber-numeroReference"]:
                        if row.get(fld):
                            vals.append((f"raw.{key}.{fld}", row[fld]))
        ids = {}
        for k, v in vals:
            a = alnum(v)
            if a in DEGEN or len(a) < 4:
                continue
            ids.setdefault(a, v)
        v = r.get("vendor", {}) or {}
        vi = v.get("identifiers", {}) or {}
        names = {v.get("name")}
        for k in ["pd_vendor_name_latest", "canadabuys_legal_name", "canadabuys_operating_name", "canadabuys_standardized_name"]:
            names.add(vi.get(k))
        for nm in vi.get("pd_vendor_name_variants") or []:
            names.add(nm)
        names = sorted(x for x in names if x)
        fo.write(json.dumps({"record_id": r.get("record_id"), "status": r.get("status"), "ids": sorted(ids), "ids_orig": ids,
                             "vendors": names, "buyer": (r.get("buyer") or {}).get("name"),
                             "end": (r.get("contract", {}).get("dates") or {}).get("end"),
                             "instrument": r.get("contract", {}).get("instrument_type")}, ensure_ascii=False) + "\n")
print("records", n)
