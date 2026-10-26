#!/usr/bin/env python3
"""Cross-year analysis of the per-FY prime transaction CSVs: how many distinct awards, how many
appear in multiple FY files, status distribution under the planned rules. Read-only; prints a report."""
import glob
import os
import sys
from collections import Counter, defaultdict

import pandas as pd

EXT = "downloads/usaspending/extracted"
REF = "2026-10-25"

KEEP = ["contract_award_unique_key", "action_date", "modification_number", "transaction_number", "action_date_fiscal_year",
        "period_of_performance_start_date", "period_of_performance_current_end_date", "ordering_period_end_date",
        "award_or_idv_flag", "award_type_code", "idv_type_code", "recipient_country_code", "last_modified_date", "action_type_code"]

frames = []
for fy_dir in sorted(glob.glob(os.path.join(EXT, "FY*"))):
    for p in glob.glob(os.path.join(fy_dir, "All_Contracts_PrimeTransactions_*.csv")):
        for chunk in pd.read_csv(p, dtype=str, keep_default_na=False, chunksize=100000, usecols=KEEP):
            chunk["src_fy"] = os.path.basename(fy_dir)
            frames.append(chunk)
df = pd.concat(frames, ignore_index=True)
print("total transaction rows:", len(df))
print("recipient_country_code:", df.recipient_country_code.value_counts().to_dict())
print("distinct awards:", df.contract_award_unique_key.nunique())
per_award_fys = df.groupby("contract_award_unique_key")["src_fy"].nunique()
print("awards spanning >1 FY file:", (per_award_fys > 1).sum(), "max FY files:", per_award_fys.max())

# latest transaction per award = max(action_date, then last_modified_date)
df["_k"] = df.action_date + "|" + df.last_modified_date + "|" + df.modification_number
idx = df.groupby("contract_award_unique_key")["_k"].idxmax()
latest = df.loc[idx].set_index("contract_award_unique_key")
print("latest rows:", len(latest))
print("award_or_idv_flag:", latest.award_or_idv_flag.value_counts().to_dict())
print("award_type_code (AWARD rows):", latest[latest.award_or_idv_flag == "AWARD"].award_type_code.value_counts().to_dict())
print("idv_type_code (IDV rows):", latest[latest.award_or_idv_flag == "IDV"].idv_type_code.value_counts().to_dict())

# status under planned rules
def status(r):
    is_idv = r.award_or_idv_flag == "IDV"
    start = r.period_of_performance_start_date or None
    if not start:
        # fallback: earliest action_date for this award (base action date) - approximated here with min action_date
        start = r["_min_action"]
    end = r.ordering_period_end_date if is_idv else r.period_of_performance_current_end_date
    if is_idv and not end:
        end = r.period_of_performance_current_end_date
    if not end:
        return "end_date_unknown" if (start and start <= REF) else "end_date_unknown_future_start"
    if end < REF:
        return "ended"
    if start and start > REF:
        return "future_start"
    return "ongoing"

min_action = df.groupby("contract_award_unique_key")["action_date"].min()
latest["_min_action"] = min_action
latest["_status"] = latest.apply(status, axis=1)
print("status (latest row):", latest._status.value_counts().to_dict())
print("status by flag:")
print(latest.groupby(["award_or_idv_flag", "_status"]).size().to_string())
# blank start rate
print("blank pop start:", (latest.period_of_performance_start_date == "").sum())
print("blank pop current end (AWARD):", ((latest.award_or_idv_flag == "AWARD") & (latest.period_of_performance_current_end_date == "")).sum())
print("blank ordering end (IDV):", ((latest.award_or_idv_flag == "IDV") & (latest.ordering_period_end_date == "")).sum())
print("IDV with ordering blank but pop end present:", ((latest.award_or_idv_flag == "IDV") & (latest.ordering_period_end_date == "") & (latest.period_of_performance_current_end_date != "")).sum())
# how many "ongoing" awards have latest action_date in old years
on = latest[latest._status == "ongoing"]
print("ongoing by latest action FY:", on.action_date_fiscal_year.value_counts().sort_index().to_dict())
print("ongoing with end date > 2040:", (on.apply(lambda r: (r.ordering_period_end_date if r.award_or_idv_flag == 'IDV' else r.period_of_performance_current_end_date), axis=1) > "2040").sum())
# any closeout/termination action types among ongoing
print("ongoing latest action_type_code:", on.action_type_code.value_counts().to_dict())
# how often does latest-row end date differ from max end date among all rows
maxend = df.groupby("contract_award_unique_key")["period_of_performance_current_end_date"].max()
latest["_maxend"] = maxend
aw = latest[latest.award_or_idv_flag == "AWARD"]
print("AWARD: latest end != max end:", (aw.period_of_performance_current_end_date != aw._maxend).sum(), "of", len(aw))
diff = aw[(aw.period_of_performance_current_end_date != aw._maxend)]
print("  of which latest end < REF <= max end (would flip status):", ((diff.period_of_performance_current_end_date < REF) & (diff._maxend >= REF)).sum())
print(diff[["action_date", "modification_number", "period_of_performance_current_end_date", "_maxend", "action_type_code"]].head(10).to_string())
