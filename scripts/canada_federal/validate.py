#!/usr/bin/env python3
"""Validate the canada_federal.jsonl output against SCHEMA.md rules.
Usage: python3 -I validate.py <jsonl> <report_json>
"""
import sys, json, collections, datetime, re
REF = datetime.date(2026, 10, 25)
path, report = sys.argv[1], sys.argv[2]
c = collections.Counter()
ids = set()
issues = collections.defaultdict(list)
status_basis_samples = collections.defaultdict(list)
by_buyer = collections.Counter()
by_buyer_type = collections.Counter()
by_vendor_basis = collections.Counter()
by_instrument = collections.Counter()
end_year = collections.Counter()
value_missing = 0
line_no = 0
raw_sizes = []
pd_rows_total = 0
per_combo_status = collections.Counter()
samples_by_combo = {}
with open(path, encoding="utf-8") as f:
    for line in f:
        line_no += 1
        try:
            r = json.loads(line)
        except Exception as e:
            issues["bad_json"].append(line_no); continue
        c["records"] += 1
        rid = r["record_id"]
        if rid in ids:
            issues["dup_record_id"].append(rid)
        ids.add(rid)
        for k in ["record_id", "source", "status", "status_basis", "contract", "buyer", "vendor", "raw"]:
            if k not in r:
                issues["missing_top_" + k].append(rid)
        if r["status"] not in ("ongoing", "ongoing_inferred", "end_date_unknown"):
            issues["bad_status"].append(rid)
        if r["vendor"].get("country") != "CA":
            issues["vendor_country_not_CA"].append(rid)
        if not r["vendor"].get("country_basis"):
            issues["no_country_basis"].append(rid)
        if not r["vendor"].get("name"):
            issues["no_vendor_name"].append(rid)
        if not r["buyer"].get("name"):
            issues["no_buyer_name"].append(rid)
        d = r["contract"].get("dates", {})
        end = d.get("end"); start = d.get("start")
        if r["status"] == "ongoing":
            if not end:
                issues["ongoing_without_end"].append(rid)
            else:
                e = datetime.date.fromisoformat(end)
                if e < REF:
                    issues["ongoing_end_before_ref"].append(rid)
                end_year[e.year if e.year <= 2035 else ("2036-2100" if e.year <= 2100 else ">2100")] += 1
            if start and datetime.date.fromisoformat(start) > REF:
                issues["ongoing_start_after_ref"].append(rid)
        if r["status"] == "end_date_unknown" and end:
            issues["unknown_with_end"].append(rid)
        if r["contract"].get("value") is None:
            value_missing += 1
        combo = "+".join(k for k in ["proactive_disclosure", "canadabuys_contract_history", "canadabuys_award_notice", "related_tender_notice"] if k in r["raw"])
        per_combo_status[(combo, r["status"])] += 1
        if combo not in samples_by_combo:
            samples_by_combo[combo] = rid
        if "proactive_disclosure" in r["raw"]:
            pd_rows_total += r["raw"]["proactive_disclosure"]["n_rows"]
            if not r["source"]["record_url"] or "search.open.canada.ca/contracts/record/" not in r["source"]["record_url"]:
                issues["pd_record_url_missing"].append(rid)
            rows = r["raw"]["proactive_disclosure"]["rows"]
            if len(rows) != len(set(x["reference_number"] for x in rows)):
                issues["pd_duplicate_rows"].append(rid)
            if not rid.startswith(f"canada_federal:{rows[-1]['owner_org']}:"):
                issues["pd_record_id_org_mismatch"].append(rid)
        if "related_tender_notice" in r["raw"] and not r["contract"]["related"].get("tender_notice_url"):
            c["tn_without_cb_url"] += 1
        if r["contract"]["related"].get("tender_notice_url") and not re.match(r"^https://canadabuys\.canada\.ca/en/tender-opportunities/tender-notice/[a-z0-9_.-]+$", r["contract"]["related"]["tender_notice_url"]):
            issues["bad_tn_url"].append(rid)
        by_buyer[r["buyer"]["name"]] += 1
        by_buyer_type[r["buyer"].get("type")] += 1
        by_vendor_basis[re.sub(r"'.*", "", r["vendor"]["country_basis"].split(";")[0]).strip()] += 1
        by_instrument[r["contract"].get("instrument_type")] += 1
        raw_sizes.append(len(line))
        if len(status_basis_samples[r["status"]]) < 3:
            status_basis_samples[r["status"]].append(r["status_basis"])
out = {
    "records": c["records"], "issues": {k: (len(v), v[:5]) for k, v in issues.items()},
    "per_combo_status": sorted(((k[0], k[1], v) for k, v in per_combo_status.items()), key=lambda x: -x[2]),
    "pd_rows_in_output": pd_rows_total, "value_missing": value_missing,
    "end_year_dist": sorted(end_year.items(), key=lambda x: str(x[0])),
    "buyers_distinct": len(by_buyer), "top_buyers": by_buyer.most_common(25), "buyer_types": dict(by_buyer_type),
    "vendor_country_basis": dict(by_vendor_basis), "instrument_types": by_instrument.most_common(),
    "line_size_bytes": {"max": max(raw_sizes), "mean": sum(raw_sizes) // len(raw_sizes), "p50": sorted(raw_sizes)[len(raw_sizes) // 2]},
    "status_basis_samples": status_basis_samples, "tn_without_cb_url": c["tn_without_cb_url"], "samples_by_combo": samples_by_combo,
}
json.dump(out, open(report, "w"), indent=1, ensure_ascii=False, default=str)
print(json.dumps(out, indent=1, ensure_ascii=False, default=str))
