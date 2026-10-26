#!/usr/bin/env python3
"""Normalize USAspending bulk-download CSVs (Canadian recipient location) into the shared record shape.

Pass 1: read key columns of every FY prime-transaction CSV; pick the latest transaction per award and
        decide status (ongoing / end_date_unknown / excluded).
Pass 2: stream the CSVs again, collect ALL columns of ALL rows for the awards to emit; write records
        progressively to normalized/usaspending.jsonl.
Pass 3: subawards (subcontracts to Canadian sub-recipients): group reports per subcontract, infer status
        from the prime award's current end date (own prime index, then awards API for blanks).

Usage: python3 -I normalize.py
"""
import glob
import json
import os
import sys
import time
from collections import defaultdict
from datetime import datetime, timezone

import pandas as pd
import requests

REF = "2026-10-25"
BASE = "downloads/usaspending"
EXT = os.path.join(BASE, "extracted")
REQ_DIR = os.path.join(BASE, "requests")
OUT = "normalized/usaspending.jsonl"
STATS = "scripts/usaspending/logs/normalize_stats.json"
LOG = "scripts/usaspending/logs/normalize.log"
API = "https://api.usaspending.gov"
UA = "contracts-research/1.0"
DATASET_URL = "https://www.usaspending.gov/download_center/custom_award_data"

SOURCE_BASE = {
    "key": "usaspending",
    "name": "USAspending.gov Custom Award Data Download (FPDS prime contract transactions + SAM.gov/FSRS subaward reports)",
    "publisher": "U.S. Department of the Treasury, Bureau of the Fiscal Service (USAspending.gov)",
    "dataset_url": DATASET_URL,
}

AWARD_TYPE_INSTRUMENT = {"A": "BPA call", "B": "purchase order", "C": "delivery order", "D": "definitive contract"}
IDV_TYPE_INSTRUMENT = {"A": "IDV (GWAC)", "B": "IDV (IDC)", "C": "IDV (FSS)", "D": "IDV (BOA)", "E": "IDV (BPA)"}
ISO3_TO_ISO2 = {"USA": "US", "CAN": "CA", "GBR": "GB", "FRA": "FR", "DEU": "DE", "AUS": "AU", "NLD": "NL", "ITA": "IT",
                "JPN": "JP", "KOR": "KR", "ISR": "IL", "CHE": "CH", "SWE": "SE", "NOR": "NO", "DNK": "DK", "BEL": "BE",
                "ESP": "ES", "MEX": "MX", "IRL": "IE", "FIN": "FI", "AUT": "AT", "POL": "PL", "SGP": "SG", "IND": "IN"}

PASS1_COLS = ["contract_award_unique_key", "action_date", "modification_number", "last_modified_date", "initial_report_date",
              "period_of_performance_start_date", "period_of_performance_current_end_date", "ordering_period_end_date",
              "award_or_idv_flag", "action_type_code", "current_total_value_of_award", "recipient_country_code"]


def log(msg):
    line = f"{datetime.now(timezone.utc).isoformat()} {msg}"
    print(line, flush=True)
    with open(LOG, "a") as f:
        f.write(line + "\n")


def num(s):
    if s is None:
        return None
    s = str(s).strip()
    if s == "":
        return None
    try:
        return float(s)
    except ValueError:
        return None


def date_only(s):
    s = (s or "").strip()
    return s[:10] if len(s) >= 10 else (s or None)


def blank_to_none(s):
    s = (s or "").strip()
    return s if s else None


def load_states():
    states = {}
    for p in glob.glob(os.path.join(REQ_DIR, "FY*.json")):
        with open(p) as f:
            st = json.load(f)
        if st.get("status") == "done":
            states[f"FY{st['fy']}"] = st
    return states


def file_inventory(states):
    """Return list of (fy_label, path, kind, retrieved_at)."""
    inv = []
    for fy, st in sorted(states.items()):
        for f in st["files"]:
            kind = "prime" if "PrimeTransactions" in f["name"] else ("sub" if "Subawards" in f["name"] else "other")
            inv.append((fy, os.path.join(EXT, fy, f["name"]), kind, st["downloaded_at"]))
    return inv


# ----------------------------------------------------------------------------------------------
# PASS 1
# ----------------------------------------------------------------------------------------------
def pass1(prime_files):
    frames = []
    for fy, path, _, _ in prime_files:
        for chunk in pd.read_csv(path, dtype=str, keep_default_na=False, chunksize=100000, usecols=PASS1_COLS):
            chunk["_file"] = os.path.basename(path)
            frames.append(chunk)
    df = pd.concat(frames, ignore_index=True)
    log(f"pass1: {len(df)} transaction rows, {df.contract_award_unique_key.nunique()} distinct awards")
    non_can = int((df.recipient_country_code != "CAN").sum())
    if non_can:
        log(f"pass1: WARNING {non_can} rows with recipient_country_code != CAN (will be dropped)")
        df = df[df.recipient_country_code == "CAN"]
    df["_sort"] = df.action_date + "|" + df.last_modified_date + "|" + df.modification_number
    grp = df.groupby("contract_award_unique_key")
    latest = df.loc[grp["_sort"].idxmax()].set_index("contract_award_unique_key")
    latest["_min_action"] = grp["action_date"].min()
    latest["_max_action"] = grp["action_date"].max()
    latest["_n_rows"] = grp.size()
    # earliest initial_report_date (publication of base transaction)
    ird = df[df.initial_report_date != ""].groupby("contract_award_unique_key")["initial_report_date"].min()
    latest["_min_initial_report"] = ird
    latest["_min_initial_report"] = latest["_min_initial_report"].fillna("")
    return latest


def decide_status(r):
    """Return (status or None, basis, exclusion_reason or None)."""
    is_idv = r.award_or_idv_flag == "IDV"
    start = r.period_of_performance_start_date or ""
    start_field = "period_of_performance_start_date"
    if not start:
        start = r._min_action
        start_field = "earliest action_date (base transaction; period_of_performance_start_date blank)"
    if is_idv:
        end = r.ordering_period_end_date or ""
        end_field = "ordering_period_end_date"
        if not end and r.period_of_performance_current_end_date:
            end = r.period_of_performance_current_end_date
            end_field = "period_of_performance_current_end_date (ordering_period_end_date blank)"
    else:
        end = r.period_of_performance_current_end_date or ""
        end_field = "period_of_performance_current_end_date"
    at = r.action_type_code
    cur_val = num(r.current_total_value_of_award)
    # 1) date tests
    if end and end < REF:
        return None, "", f"{end_field} < {REF}"
    if start and start > REF:
        return None, "", f"{start_field} > {REF} (not yet started)"
    # 2) latest action is a cancellation / close-out / complete termination -> not ongoing even if dates say so
    if at == "N":
        return None, "", "dates ongoing but latest transaction action_type N (LEGAL CONTRACT CANCELLATION)"
    if at == "K":
        return None, "", "dates ongoing but latest transaction action_type K (CLOSE OUT)"
    if at == "F" and (cur_val is None or cur_val <= 0):
        return None, "", "dates ongoing but latest transaction action_type F (TERMINATE FOR CONVENIENCE) with current_total_value_of_award <= 0"
    cancel_note = ""
    if at == "F":
        cancel_note = " Note: latest transaction action_type F (TERMINATE FOR CONVENIENCE, COMPLETE OR PARTIAL) but current_total_value_of_award > 0, treated as partial termination."
    if not end:
        return "end_date_unknown", (f"Latest transaction (action_date {r.action_date}, mod {r.modification_number}) has blank {end_field}; "
                                    f"{start_field} = {start} <= {REF}.{cancel_note}"), None
    placeholder_note = ""
    if end >= "2050":
        placeholder_note = (f" Caution: end date {end} (latest action {r.action_date}) looks like a legacy placeholder value "
                            f"(e.g. 9999-09-09 / 2060-12-25) rather than a real completion date; kept because the published end date is >= {REF}.")
    basis = (f"Latest transaction (action_date {r.action_date}, mod {r.modification_number}) {end_field} = {end} >= {REF} "
             f"and {start_field} = {start} <= {REF}.{cancel_note}{placeholder_note}")
    return "ongoing", basis, None


# ----------------------------------------------------------------------------------------------
# PASS 2: collect full rows for selected awards
# ----------------------------------------------------------------------------------------------
def pass2_collect(prime_files, wanted_keys):
    rows = defaultdict(list)
    for fy, path, _, retrieved in prime_files:
        fname = os.path.basename(path)
        for chunk in pd.read_csv(path, dtype=str, keep_default_na=False, chunksize=100000):
            sel = chunk[chunk.contract_award_unique_key.isin(wanted_keys)]
            if sel.empty:
                continue
            for rec in sel.to_dict(orient="records"):
                rows[rec["contract_award_unique_key"]].append((rec, fname, retrieved))
    return rows


def pick_latest(rowlist):
    def k(t):
        r = t[0]
        return (r.get("action_date", ""), r.get("last_modified_date", ""), r.get("modification_number", ""))
    return max(rowlist, key=k)


def instrument_type(r):
    if r.get("award_or_idv_flag") == "IDV":
        code = r.get("idv_type_code", "")
        base = IDV_TYPE_INSTRUMENT.get(code, f"IDV ({r.get('idv_type') or code or 'unknown type'})")
        idc = r.get("type_of_idc", "")
        if code == "B" and idc:
            base = f"IDV (IDC: {idc})"
        if r.get("multiple_or_single_award_idv"):
            base += f", {r['multiple_or_single_award_idv'].lower()}"
        return base
    code = r.get("award_type_code", "")
    return AWARD_TYPE_INSTRUMENT.get(code, (r.get("award_type") or code or "contract").lower())


def build_prime_record(key, rowlist, status, basis, meta):
    latest_t = pick_latest(rowlist)
    r, latest_file, retrieved = latest_t
    is_idv = r.get("award_or_idv_flag") == "IDV"
    rows_sorted = sorted(rowlist, key=lambda t: (t[0].get("action_date", ""), t[0].get("last_modified_date", ""), t[0].get("modification_number", "")))
    base_row = rows_sorted[0][0]
    end = r.get("ordering_period_end_date") if is_idv else r.get("period_of_performance_current_end_date")
    if is_idv and not end:
        end = r.get("period_of_performance_current_end_date")
    cur = num(r.get("current_total_value_of_award"))
    pot = num(r.get("potential_total_value_of_award"))
    value = cur if cur is not None else pot
    parent_piid = blank_to_none(r.get("parent_award_id_piid"))
    parent_agency = blank_to_none(r.get("parent_award_agency_id"))
    parent_key = f"CONT_IDV_{parent_piid}_{parent_agency}" if parent_piid and parent_agency else None
    identifiers = {
        "contract_award_unique_key": key,
        "piid": blank_to_none(r.get("award_id_piid")),
        "awarding_agency_code": blank_to_none(r.get("awarding_agency_code")),
        "awarding_sub_agency_code": blank_to_none(r.get("awarding_sub_agency_code")),
        "parent_award_id_piid": parent_piid,
        "parent_award_agency_id": parent_agency,
        "solicitation_identifier": blank_to_none(r.get("solicitation_identifier")),
        "latest_contract_transaction_unique_key": blank_to_none(r.get("contract_transaction_unique_key")),
        "latest_modification_number": blank_to_none(r.get("modification_number")),
        "transaction_unique_keys": [t[0].get("contract_transaction_unique_key") for t in rows_sorted],
        "modification_numbers": [t[0].get("modification_number") for t in rows_sorted],
    }
    desc = blank_to_none(r.get("prime_award_base_transaction_description")) or blank_to_none(r.get("transaction_description"))
    rec = {
        "record_id": f"usaspending:{key}",
        "source": {**SOURCE_BASE, "record_url": blank_to_none(r.get("usaspending_permalink")), "retrieved_at": retrieved},
        "status": status,
        "status_basis": basis,
        "contract": {
            "identifiers": identifiers,
            "title": None,
            "description": desc,
            "latest_transaction_description": blank_to_none(r.get("transaction_description")),
            "instrument_type": instrument_type(r),
            "award_or_idv_flag": r.get("award_or_idv_flag"),
            "award_type_code": blank_to_none(r.get("award_type_code")),
            "award_type": blank_to_none(r.get("award_type")),
            "idv_type_code": blank_to_none(r.get("idv_type_code")),
            "idv_type": blank_to_none(r.get("idv_type")),
            "procurement_method": blank_to_none(r.get("extent_competed")),
            "solicitation_procedure": blank_to_none(r.get("solicitation_procedures")),
            "type_of_set_aside": blank_to_none(r.get("type_of_set_aside")),
            "type_of_contract_pricing": blank_to_none(r.get("type_of_contract_pricing")),
            "commodity": {
                "naics": blank_to_none(r.get("naics_code")),
                "naics_description": blank_to_none(r.get("naics_description")),
                "psc": blank_to_none(r.get("product_or_service_code")),
                "psc_description": blank_to_none(r.get("product_or_service_code_description")),
            },
            "value": value,
            "currency": "USD",
            "value_detail": {
                "current_total_value_of_award": cur,
                "potential_total_value_of_award": pot,
                "total_dollars_obligated": num(r.get("total_dollars_obligated")),
                "total_outlayed_amount_for_overall_award": num(r.get("total_outlayed_amount_for_overall_award")),
                "base_and_exercised_options_value_latest_mod": num(r.get("base_and_exercised_options_value")),
                "base_and_all_options_value_latest_mod": num(r.get("base_and_all_options_value")),
                "federal_action_obligation_latest_mod": num(r.get("federal_action_obligation")),
                "federal_action_obligation_sum_of_rows": round(sum((num(t[0].get("federal_action_obligation")) or 0.0) for t in rowlist), 2),
                "number_of_actions_latest_mod": num(r.get("number_of_actions")),
            },
            "dates": {
                "published": date_only(meta.get("min_initial_report")) or date_only(base_row.get("initial_report_date")),
                "signed": base_row.get("action_date") or None,
                "start": blank_to_none(r.get("period_of_performance_start_date")),
                "end": blank_to_none(end),
                "amended_last": r.get("action_date") or None,
                "potential_end": blank_to_none(r.get("period_of_performance_potential_end_date")),
                "ordering_period_end": blank_to_none(r.get("ordering_period_end_date")),
                "last_modified": blank_to_none(r.get("last_modified_date")),
                "solicitation_date": blank_to_none(r.get("solicitation_date")),
            },
            "related": {
                "parent_idv_id": parent_piid,
                "parent_idv_agency_id": parent_agency,
                "parent_idv_unique_key": parent_key,
                "parent_idv_url": f"https://www.usaspending.gov/award/{parent_key}/" if parent_key else None,
                "parent_award_type": blank_to_none(r.get("parent_award_type")),
                "parent_award_single_or_multiple": blank_to_none(r.get("parent_award_single_or_multiple")),
                "api_url": f"{API}/api/v2/awards/{key}/",
                "funding_agency_code": blank_to_none(r.get("funding_agency_code")),
                "funding_agency_name": blank_to_none(r.get("funding_agency_name")),
                "funding_sub_agency_code": blank_to_none(r.get("funding_sub_agency_code")),
                "funding_sub_agency_name": blank_to_none(r.get("funding_sub_agency_name")),
                "funding_office_code": blank_to_none(r.get("funding_office_code")),
                "funding_office_name": blank_to_none(r.get("funding_office_name")),
                "place_of_performance_country_code": blank_to_none(r.get("primary_place_of_performance_country_code")),
                "place_of_performance_city": blank_to_none(r.get("primary_place_of_performance_city_name")),
                "place_of_performance_state": blank_to_none(r.get("primary_place_of_performance_state_code")),
                "latest_action_type_code": blank_to_none(r.get("action_type_code")),
                "latest_action_type": blank_to_none(r.get("action_type")),
                "transaction_count_in_download": len(rowlist),
            },
        },
        "buyer": {
            "name": blank_to_none(r.get("awarding_agency_name")),
            "country": "US",
            "type": "US federal department/agency",
            "sub_agency_name": blank_to_none(r.get("awarding_sub_agency_name")),
            "office_name": blank_to_none(r.get("awarding_office_name")),
            "identifiers": {
                "awarding_agency_code": blank_to_none(r.get("awarding_agency_code")),
                "awarding_sub_agency_code": blank_to_none(r.get("awarding_sub_agency_code")),
                "awarding_office_code": blank_to_none(r.get("awarding_office_code")),
            },
            "address": {},
            "contact": {},
        },
        "vendor": {
            "name": blank_to_none(r.get("recipient_name")),
            "name_raw": blank_to_none(r.get("recipient_name_raw")),
            "doing_business_as": blank_to_none(r.get("recipient_doing_business_as_name")),
            "country": "CA",
            "country_basis": "recipient_country_code == 'CAN' (FPDS LegalEntityCountryCode of the latest transaction; bulk download filtered on recipient_locations country=CAN)",
            "identifiers": {
                "uei": blank_to_none(r.get("recipient_uei")),
                "duns": blank_to_none(r.get("recipient_duns")),
                "cage": blank_to_none(r.get("cage_code")),
                "parent_uei": blank_to_none(r.get("recipient_parent_uei")),
                "parent_duns": blank_to_none(r.get("recipient_parent_duns")),
                "parent_name": blank_to_none(r.get("recipient_parent_name")),
            },
            "address": {
                "line1": blank_to_none(r.get("recipient_address_line_1")),
                "line2": blank_to_none(r.get("recipient_address_line_2")),
                "city": blank_to_none(r.get("recipient_city_name")),
                "region": blank_to_none(r.get("recipient_state_name")) or blank_to_none(r.get("recipient_state_code")),
                "postal_code": blank_to_none(r.get("recipient_zip_4_code")),
                "country": blank_to_none(r.get("recipient_country_code")),
            },
            "contact": {
                "phone": blank_to_none(r.get("recipient_phone_number")),
                "fax": blank_to_none(r.get("recipient_fax_number")),
            },
        },
        "raw": {
            **r,  # latest transaction row, every column verbatim
            "rows": [t[0] for t in rows_sorted],
            "row_source_files": [t[1] for t in rows_sorted],
            "source_files": sorted({t[1] for t in rows_sorted}),
        },
    }
    return rec


# ----------------------------------------------------------------------------------------------
# PASS 3: subawards
# ----------------------------------------------------------------------------------------------
def api_award(session, key, cache):
    if key in cache:
        return cache[key]
    for attempt in range(1, 5):
        try:
            resp = session.get(f"{API}/api/v2/awards/{key}/", timeout=60)
            if resp.status_code == 200:
                cache[key] = resp.json()
                return cache[key]
            if resp.status_code == 404:
                cache[key] = {"_error": "404"}
                return cache[key]
            log(f"api_award {key}: HTTP {resp.status_code}")
        except requests.RequestException as e:
            log(f"api_award {key}: {e}")
        time.sleep(5 * attempt)
    cache[key] = {"_error": "unavailable"}
    return cache[key]


def build_sub_record(gkey, rowlist, prime_index, session, api_cache, stats):
    prime_key, subnum, uei = gkey
    rows_sorted = sorted(rowlist, key=lambda t: (t[0].get("subaward_action_date", ""), t[0].get("subaward_sam_report_last_modified_date", "")))
    r, latest_file, retrieved = rows_sorted[-1]
    prime_end = blank_to_none(r.get("prime_award_period_of_performance_current_end_date"))
    end_source = "subaward file column prime_award_period_of_performance_current_end_date"
    api_payload = None
    if not prime_end:
        pi = prime_index.get(prime_key)
        if pi is not None:
            cand = pi.get("ordering_period_end_date") or pi.get("period_of_performance_current_end_date") or ""
            if cand:
                prime_end = cand
                end_source = "prime IDV's ordering_period_end_date from this source's own prime-transaction download (latest transaction)"
        if not prime_end:
            api_payload = api_award(session, prime_key, api_cache)
            pop = (api_payload or {}).get("period_of_performance") or {}
            if pop.get("end_date"):
                prime_end = pop["end_date"]
                end_source = f"USAspending awards API {API}/api/v2/awards/{prime_key}/ period_of_performance.end_date (ordering period end for IDVs)"
    if not prime_end:
        status = "end_date_unknown"
        basis = ("Subcontract report carries no end date of its own; prime award's current end date is blank in the subaward file, "
                 "not in this source's prime download, and not returned by the awards API.")
        stats["sub_end_unknown"] += 1
    elif prime_end < REF:
        stats["sub_excluded_prime_ended"] += 1
        return None
    else:
        status = "ongoing_inferred"
        basis = (f"Subcontract reports have no end date of their own; inferred ongoing because the prime award's current end date "
                 f"{prime_end} >= {REF} ({end_source}) and the subaward action date {r.get('subaward_action_date')} <= {REF}.")
        stats["sub_ongoing_inferred"] += 1
        stats[f"sub_end_source::{end_source[:40]}"] += 1
    amounts = [num(t[0].get("subaward_amount")) for t in rows_sorted]
    amounts_clean = [a for a in amounts if a is not None]
    total = round(sum(amounts_clean), 2) if amounts_clean else None
    prime_country = blank_to_none(r.get("prime_awardee_country_code"))
    rec = {
        "record_id": f"usaspending:sub:{prime_key}:{subnum}:{uei}",
        "source": {**SOURCE_BASE, "record_url": blank_to_none(r.get("usaspending_permalink")), "retrieved_at": retrieved},
        "status": status,
        "status_basis": basis,
        "contract": {
            "identifiers": {
                "subaward_number": subnum,
                "prime_award_unique_key": prime_key,
                "prime_award_piid": blank_to_none(r.get("prime_award_piid")),
                "prime_award_parent_piid": blank_to_none(r.get("prime_award_parent_piid")),
                "subaward_sam_report_ids": [t[0].get("subaward_sam_report_id") for t in rows_sorted],
                "subaward_sam_report_periods": [f"{t[0].get('subaward_sam_report_year')}-{t[0].get('subaward_sam_report_month')}" for t in rows_sorted],
            },
            "title": None,
            "description": blank_to_none(r.get("subaward_description")),
            "prime_award_description": blank_to_none(r.get("prime_award_base_transaction_description")),
            "instrument_type": "subcontract",
            "subaward_type": blank_to_none(r.get("subaward_type")),
            "procurement_method": None,
            "solicitation_procedure": None,
            "commodity": {
                "naics": blank_to_none(r.get("prime_award_naics_code")),
                "naics_description": blank_to_none(r.get("prime_award_naics_description")),
                "naics_scope": "NAICS of the prime award (subaward reports carry no commodity code of their own)",
            },
            "value": total,
            "currency": "USD",
            "value_detail": {
                "subaward_amount_latest_report": amounts[-1],
                "subaward_amount_sum_all_reports": total,
                "subaward_amounts_by_report": amounts,
                "report_count": len(rows_sorted),
                "prime_award_amount": num(r.get("prime_award_amount")),
            },
            "dates": {
                "published": date_only(rows_sorted[0][0].get("subaward_sam_report_last_modified_date")),
                "signed": rows_sorted[0][0].get("subaward_action_date") or None,
                "start": None,
                "end": None,
                "amended_last": r.get("subaward_action_date") or None,
                "latest_report_last_modified": blank_to_none(r.get("subaward_sam_report_last_modified_date")),
            },
            "related": {
                "prime_award_url": blank_to_none(r.get("usaspending_permalink")),
                "prime_award_api_url": f"{API}/api/v2/awards/{prime_key}/",
                "prime_award_period_of_performance_start_date": blank_to_none(r.get("prime_award_period_of_performance_start_date")),
                "prime_award_period_of_performance_current_end_date": blank_to_none(r.get("prime_award_period_of_performance_current_end_date")),
                "prime_award_end_date_used_for_status": prime_end,
                "prime_award_end_date_source": end_source if prime_end else None,
                "awarding_agency_code": blank_to_none(r.get("prime_award_awarding_agency_code")),
                "awarding_agency_name": blank_to_none(r.get("prime_award_awarding_agency_name")),
                "awarding_sub_agency_code": blank_to_none(r.get("prime_award_awarding_sub_agency_code")),
                "awarding_sub_agency_name": blank_to_none(r.get("prime_award_awarding_sub_agency_name")),
                "awarding_office_code": blank_to_none(r.get("prime_award_awarding_office_code")),
                "awarding_office_name": blank_to_none(r.get("prime_award_awarding_office_name")),
                "funding_agency_name": blank_to_none(r.get("prime_award_funding_agency_name")),
                "funding_sub_agency_name": blank_to_none(r.get("prime_award_funding_sub_agency_name")),
                "funding_office_name": blank_to_none(r.get("prime_award_funding_office_name")),
                "subaward_place_of_performance_country_code": blank_to_none(r.get("subaward_primary_place_of_performance_country_code")),
                "subaward_place_of_performance_city": blank_to_none(r.get("subaward_primary_place_of_performance_city_name")),
            },
        },
        "buyer": {
            "name": blank_to_none(r.get("prime_awardee_name")),
            "country": ISO3_TO_ISO2.get(prime_country or "", prime_country),
            "type": "company (prime contractor to the US federal government)",
            "identifiers": {
                "uei": blank_to_none(r.get("prime_awardee_uei")),
                "duns": blank_to_none(r.get("prime_awardee_duns")),
                "parent_uei": blank_to_none(r.get("prime_awardee_parent_uei")),
                "parent_duns": blank_to_none(r.get("prime_awardee_parent_duns")),
                "parent_name": blank_to_none(r.get("prime_awardee_parent_name")),
                "dba_name": blank_to_none(r.get("prime_awardee_dba_name")),
            },
            "address": {
                "line1": blank_to_none(r.get("prime_awardee_address_line_1")),
                "city": blank_to_none(r.get("prime_awardee_city_name")),
                "region": blank_to_none(r.get("prime_awardee_state_code")),
                "postal_code": blank_to_none(r.get("prime_awardee_zip_code")) or blank_to_none(r.get("prime_awardee_foreign_postal_code")),
                "country": prime_country,
            },
            "contact": {},
        },
        "vendor": {
            "name": blank_to_none(r.get("subawardee_name")),
            "doing_business_as": blank_to_none(r.get("subawardee_dba_name")),
            "country": "CA",
            "country_basis": "subawardee_country_code == 'CAN' (SAM.gov/FSRS SubAwardeeLegalEntityCountryCode; bulk download filtered on recipient_locations country=CAN, applied to sub_recipient_location_country_code for subawards)",
            "identifiers": {
                "uei": blank_to_none(r.get("subawardee_uei")),
                "duns": blank_to_none(r.get("subawardee_duns")),
                "parent_uei": blank_to_none(r.get("subawardee_parent_uei")),
                "parent_duns": blank_to_none(r.get("subawardee_parent_duns")),
                "parent_name": blank_to_none(r.get("subawardee_parent_name")),
            },
            "address": {
                "line1": blank_to_none(r.get("subawardee_address_line_1")),
                "city": blank_to_none(r.get("subawardee_city_name")),
                "region": blank_to_none(r.get("subawardee_state_code")) or blank_to_none(r.get("subawardee_state_name")),
                "postal_code": blank_to_none(r.get("subawardee_foreign_postal_code")) or blank_to_none(r.get("subawardee_zip_code")),
                "country": blank_to_none(r.get("subawardee_country_code")),
            },
            "contact": {},
        },
        "raw": {
            **r,
            "rows": [t[0] for t in rows_sorted],
            "row_source_files": [t[1] for t in rows_sorted],
            "source_files": sorted({t[1] for t in rows_sorted}),
        },
    }
    if api_payload is not None:
        rec["raw"]["prime_award_api_response"] = api_payload
    return rec


def main():
    t0 = time.time()
    states = load_states()
    inv = file_inventory(states)
    prime_files = [x for x in inv if x[2] == "prime"]
    sub_files = [x for x in inv if x[2] == "sub"]
    log(f"files: {len(prime_files)} prime, {len(sub_files)} subaward")
    stats = defaultdict(int)

    latest = pass1(prime_files)
    stats["prime_transaction_rows"] = int(latest._n_rows.sum())
    stats["prime_distinct_awards"] = int(len(latest))
    decisions = {}
    excl = defaultdict(int)
    for key, r in latest.iterrows():
        status, basis, reason = decide_status(r)
        if status is None:
            excl[reason] += 1
            continue
        decisions[key] = (status, basis, {"min_initial_report": r._min_initial_report})
    stats["prime_excluded"] = dict(excl)
    stats["prime_selected"] = len(decisions)
    log(f"pass1: selected {len(decisions)} awards; exclusions: {json.dumps(dict(excl))}")

    # prime index for subaward end-date resolution (all awards, incl. ended)
    prime_index = {k: {"ordering_period_end_date": v.ordering_period_end_date, "period_of_performance_current_end_date": v.period_of_performance_current_end_date,
                       "award_or_idv_flag": v.award_or_idv_flag} for k, v in latest.iterrows()}

    rows = pass2_collect(prime_files, set(decisions.keys()))
    log(f"pass2: collected rows for {len(rows)} awards ({sum(len(v) for v in rows.values())} rows)")

    written = 0
    by_status = defaultdict(int)
    by_instrument = defaultdict(int)
    by_type = defaultdict(int)
    with open(OUT, "w", encoding="utf-8") as out:
        for key in sorted(decisions):
            status, basis, meta = decisions[key]
            try:
                rec = build_prime_record(key, rows[key], status, basis, meta)
            except Exception as e:  # keep going on bad rows
                log(f"ERROR building prime record {key}: {e!r}")
                stats["prime_build_errors"] += 1
                continue
            out.write(json.dumps(rec, ensure_ascii=False) + "\n")
            out.flush()
            written += 1
            by_status[status] += 1
            by_instrument[rec["contract"]["instrument_type"]] += 1
            flag = rec["contract"]["award_or_idv_flag"]
            code = rec["contract"]["idv_type_code"] if flag == "IDV" else rec["contract"]["award_type_code"]
            by_type[f"{flag}:{code}"] += 1
        log(f"primes written: {written}")
        stats["prime_written"] = written
        stats["prime_by_status"] = dict(by_status)
        stats["prime_by_instrument"] = dict(by_instrument)
        stats["prime_by_type"] = dict(by_type)

        # ---- subawards ----
        groups = defaultdict(list)
        n_sub_rows = 0
        for fy, path, _, retrieved in sub_files:
            fname = os.path.basename(path)
            df = pd.read_csv(path, dtype=str, keep_default_na=False)
            n_sub_rows += len(df)
            non_can = int((df.subawardee_country_code != "CAN").sum())
            if non_can:
                log(f"WARNING {fname}: {non_can} rows with subawardee_country_code != CAN dropped")
                df = df[df.subawardee_country_code == "CAN"]
            for rec in df.to_dict(orient="records"):
                if rec.get("subaward_action_date", "") > REF:
                    stats["sub_excluded_future_action_date"] += 1
                    continue
                g = (rec["prime_award_unique_key"], rec["subaward_number"], rec["subawardee_uei"])
                groups[g].append((rec, fname, retrieved))
        stats["sub_report_rows"] = n_sub_rows
        stats["sub_groups"] = len(groups)
        log(f"subawards: {n_sub_rows} report rows -> {len(groups)} subcontract groups")
        session = requests.Session()
        session.headers.update({"User-Agent": UA, "Accept": "application/json"})
        api_cache = {}
        sub_written = 0
        sub_by_status = defaultdict(int)
        for g in sorted(groups):
            try:
                rec = build_sub_record(g, groups[g], prime_index, session, api_cache, stats)
            except Exception as e:
                log(f"ERROR building sub record {g}: {e!r}")
                stats["sub_build_errors"] += 1
                continue
            if rec is None:
                continue
            out.write(json.dumps(rec, ensure_ascii=False) + "\n")
            out.flush()
            sub_written += 1
            sub_by_status[rec["status"]] += 1
        stats["sub_written"] = sub_written
        stats["sub_by_status"] = dict(sub_by_status)
        stats["sub_api_lookups"] = len(api_cache)
        stats["sub_api_lookup_failures"] = sum(1 for v in api_cache.values() if "_error" in v)
        log(f"subcontracts written: {sub_written}; api lookups {len(api_cache)}")

    stats["total_written"] = written + sub_written
    stats["elapsed_sec"] = round(time.time() - t0, 1)
    with open(STATS, "w") as f:
        json.dump(stats, f, indent=2, default=int)
    log(f"done: {json.dumps(stats, default=int)}")


if __name__ == "__main__":
    main()
