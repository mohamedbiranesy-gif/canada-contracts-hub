#!/usr/bin/env python3
"""Profile the proactive-disclosure contracts.csv in chunks.
Usage: python3 -I profile_pd.py /path/to/contracts.csv
"""
import sys, re, collections, json
import pandas as pd

path = sys.argv[1]
REF = "2026-10-25"
country = collections.Counter()
instr = collections.Counter()
rp = collections.Counter()
ddate_fmt = collections.Counter()
sdate_fmt = collections.Counter()
cdate_fmt = collections.Counter()
pc_pattern = re.compile(r"^[A-Za-z]\d[A-Za-z]\s?\d[A-Za-z]\d$|^[A-Za-z]\d[A-Za-z]$")
blank_country_with_ca_pc = 0
blank_country_total = 0
blank_country_pc_vals = collections.Counter()
nrows = 0
ongoing_like = 0
ongoing_country = collections.Counter()
future_delivery_blank_start = 0
dup_ref = collections.Counter()
proc_blank = 0
ref_blank = 0
owner_orgs = collections.Counter()
max_delivery = ""
# Track CA rows with delivery >= REF: count distinct (owner_org, procurement_id)
ca_ongoing_keys = set()
ca_ongoing_rows = 0
ca_unknown_end_recent = 0  # blank delivery_date, contract_date >= 2024
rowlen_issue = 0

def fmt(s):
    if s == "":
        return "blank"
    if re.fullmatch(r"\d{4}-\d{2}-\d{2}", s):
        return "YYYY-MM-DD"
    if re.fullmatch(r"\d{4}-\d{2}-\d{2}[ T].*", s):
        return "YYYY-MM-DD+time"
    if re.fullmatch(r"\d{4}/\d{2}/\d{2}", s):
        return "YYYY/MM/DD"
    if re.fullmatch(r"\d{2}/\d{2}/\d{4}", s):
        return "DD/MM/YYYY-or-MM/DD/YYYY"
    return "other:" + s[:12]

for chunk in pd.read_csv(path, chunksize=100000, dtype=str, keep_default_na=False, encoding="utf-8-sig"):
    nrows += len(chunk)
    country.update(chunk["country_of_vendor"].str.strip().str.upper().value_counts().to_dict())
    instr.update(chunk["instrument_type"].value_counts().to_dict())
    rp.update(chunk["reporting_period"].value_counts().to_dict())
    owner_orgs.update(chunk["owner_org"].value_counts().to_dict())
    ddate_fmt.update(chunk["delivery_date"].map(fmt).value_counts().to_dict())
    sdate_fmt.update(chunk["contract_period_start"].map(fmt).value_counts().to_dict())
    cdate_fmt.update(chunk["contract_date"].map(fmt).value_counts().to_dict())
    proc_blank += (chunk["procurement_id"].str.strip() == "").sum()
    ref_blank += (chunk["reference_number"].str.strip() == "").sum()
    dup_ref.update((chunk["owner_org"] + "|" + chunk["reference_number"]).value_counts().to_dict())
    c = chunk["country_of_vendor"].str.strip()
    blank = c == ""
    blank_country_total += blank.sum()
    pcs = chunk.loc[blank, "vendor_postal_code"].str.strip()
    blank_country_with_ca_pc += pcs.map(lambda s: bool(pc_pattern.match(s))).sum()
    blank_country_pc_vals.update(pcs.map(lambda s: "CA-pattern" if pc_pattern.match(s) else ("blank" if s == "" else ("NA" if s.upper() == "NA" else "other"))).value_counts().to_dict())
    dd = chunk["delivery_date"].str.strip()
    ok_dd = dd.str.match(r"^\d{4}-\d{2}-\d{2}")
    m = ok_dd & (dd.str[:10] >= REF)
    ongoing_like += m.sum()
    ongoing_country.update(c[m].str.upper().value_counts().to_dict())
    mx = dd[ok_dd].str[:10].max() if ok_dd.any() else ""
    if mx and mx > max_delivery:
        max_delivery = mx
    ca = c.str.upper() == "CA"
    sel = chunk[m & ca]
    ca_ongoing_rows += len(sel)
    for o, p, r in zip(sel["owner_org"], sel["procurement_id"], sel["reference_number"]):
        ca_ongoing_keys.add((o, p.strip().upper() if p.strip() else "REF:" + r.strip().upper()))
    cd = chunk["contract_date"].str.strip()
    ca_unknown_end_recent += ((dd == "") & ca & (cd.str[:4] >= "2024")).sum()
    print(f"rows so far {nrows}", file=sys.stderr, flush=True)

out = {
    "nrows": nrows,
    "country_of_vendor_top60": country.most_common(60),
    "country_distinct_count": len(country),
    "instrument_type": instr.most_common(),
    "reporting_period_recent": sorted([(k, v) for k, v in rp.items() if k >= "2023"], key=lambda x: x[0]),
    "reporting_period_min": min(rp), "reporting_period_max": max(rp),
    "delivery_date_formats": ddate_fmt.most_common(20),
    "contract_period_start_formats": sdate_fmt.most_common(20),
    "contract_date_formats": cdate_fmt.most_common(20),
    "procurement_id_blank": int(proc_blank),
    "reference_number_blank": int(ref_blank),
    "owner_org|reference_number duplicates (count of keys with >1 rows)": sum(1 for k, v in dup_ref.items() if v > 1),
    "n_owner_orgs": len(owner_orgs),
    "blank_country_total": int(blank_country_total),
    "blank_country_with_CA_postal_pattern": int(blank_country_with_ca_pc),
    "blank_country_postal_breakdown": blank_country_pc_vals.most_common(),
    "rows_delivery_ge_ref": int(ongoing_like),
    "rows_delivery_ge_ref_by_country_top20": ongoing_country.most_common(20),
    "max_delivery_date": max_delivery,
    "CA_rows_delivery_ge_ref": ca_ongoing_rows,
    "CA_distinct_contract_keys_delivery_ge_ref": len(ca_ongoing_keys),
    "CA_blank_delivery_contract_date_ge_2024": int(ca_unknown_end_recent),
}
print(json.dumps(out, indent=1, ensure_ascii=False))
