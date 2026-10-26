#!/usr/bin/env python3
"""Second profiling pass on proactive-disclosure contracts.csv.
Usage: python3 -I profile_pd2.py /path/to/contracts.csv
"""
import sys, re, collections, json
import pandas as pd

path = sys.argv[1]
REF = "2026-10-25"
raw_country_nonstd = collections.Counter()
blank_dd_year_ca = collections.Counter()
blank_dd_country = collections.Counter()
future_start = 0
future_start_examples = []
proc_ids = collections.Counter()
groups_vendors = collections.defaultdict(set)   # (owner_org, procurement_id) -> vendor names (ongoing CA)
group_rows = collections.Counter()
inst_by_group = collections.defaultdict(list)
pc_vals = collections.Counter()
pc_pattern = re.compile(r"^[A-Za-z]\d[A-Za-z]")
far_future = collections.Counter()
end_before_start = 0
value_formats = collections.Counter()

for chunk in pd.read_csv(path, chunksize=100000, dtype=str, keep_default_na=False, encoding="utf-8-sig"):
    c_raw = chunk["country_of_vendor"]
    raw_country_nonstd.update(c_raw[~c_raw.str.fullmatch(r"[A-Z]{2}|")].value_counts().to_dict())
    c = c_raw.str.strip().str.upper()
    dd = chunk["delivery_date"].str.strip()
    cd = chunk["contract_date"].str.strip()
    ps = chunk["contract_period_start"].str.strip()
    blank_dd = dd == ""
    blank_dd_country.update(c[blank_dd].value_counts().to_dict())
    blank_dd_year_ca.update(cd[blank_dd & (c == "CA")].str[:4].value_counts().to_dict())
    ok_dd = dd.str.match(r"^\d{4}-\d{2}-\d{2}$")
    live = ok_dd & (dd >= REF) & (c == "CA")
    start = ps.where(ps != "", cd)
    fs = live & (start > REF)
    future_start += fs.sum()
    if len(future_start_examples) < 5:
        for _, r in chunk[fs].head(5 - len(future_start_examples)).iterrows():
            future_start_examples.append({k: r[k] for k in ["owner_org", "reference_number", "procurement_id", "vendor_name", "contract_date", "contract_period_start", "delivery_date", "instrument_type", "reporting_period"]})
    far_future.update(dd[live].str[:4].map(lambda y: y if y >= "2031" else "<=2030").value_counts().to_dict())
    end_before_start += (live & (dd < start)).sum()
    sel = chunk[live]
    proc_ids.update(sel["procurement_id"].str.strip().str.upper().value_counts().to_dict())
    for o, p, r, v, it in zip(sel["owner_org"], sel["procurement_id"], sel["reference_number"], sel["vendor_name"], sel["instrument_type"]):
        key = (o, p.strip().upper()) if p.strip() else (o, "REF:" + r)
        groups_vendors[key].add(v.strip().upper())
        group_rows[key] += 1
        inst_by_group[key].append(it)
    pc_vals.update(sel["vendor_postal_code"].str.strip().map(lambda s: "blank" if s == "" else ("NA" if s.upper() == "NA" else ("CA-pattern" if pc_pattern.match(s) else "other:" + s[:6]))).value_counts().to_dict())
    value_formats.update(chunk["contract_value"].map(lambda s: "blank" if s == "" else ("num" if re.fullmatch(r"-?\d+(\.\d+)?", s) else "other:" + s[:10])).value_counts().to_dict())

multi_vendor = {k: v for k, v in groups_vendors.items() if len(v) > 1}
out = {
    "raw_country_values_not_ISO2_uppercase": raw_country_nonstd.most_common(50),
    "blank_delivery_date_by_country_top10": blank_dd_country.most_common(10),
    "blank_delivery_date_CA_by_contract_year": sorted(blank_dd_year_ca.items()),
    "live_CA_rows_with_future_start": int(future_start),
    "future_start_examples": future_start_examples,
    "live_CA_delivery_year_buckets": far_future.most_common(),
    "live_CA_rows_end_before_start": int(end_before_start),
    "live_CA_procurement_id_top30": proc_ids.most_common(30),
    "live_CA_groups": len(groups_vendors),
    "live_CA_groups_with_multiple_vendor_names": len(multi_vendor),
    "multi_vendor_examples": [(list(k), sorted(v)[:5], group_rows[k]) for k, v in list(multi_vendor.items())[:15]],
    "live_CA_groups_rowcount_dist": collections.Counter(group_rows.values()).most_common(10),
    "live_CA_vendor_postal_code_kinds": pc_vals.most_common(15),
    "contract_value_formats": value_formats.most_common(10),
}
print(json.dumps(out, indent=1, ensure_ascii=False, default=str))
