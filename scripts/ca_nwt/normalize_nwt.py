#!/usr/bin/env python3
"""Normalize GNWT 'Contract Report' spreadsheets (Department of Finance, Contracts Reporting).
Handles the standard 'Contract Data' layout (reports from FY2021-22 onward). One record per
Contract ID Number, taking the row from the most recent report; all rows kept under raw.rows.
Usage: python3 -I normalize_nwt.py <download_dir> <out_jsonl> <stats_json>
"""
import glob, json, os, re, sys, datetime as dt, collections, warnings
import openpyxl
warnings.filterwarnings("ignore")

DL, OUT, STATS = sys.argv[1:4]
REF = dt.date(2026, 10, 25)
RETRIEVED = open(os.path.join(DL, "retrieved_at.txt")).read().split()[0]
CA_PROV = {"AB", "BC", "SK", "MB", "ON", "QC", "NB", "NS", "PE", "PEI", "NL", "YT", "NT", "NU", "NWT"}
PROV_NAMES = {"alberta": "AB", "british columbia": "BC", "saskatchewan": "SK", "manitoba": "MB", "ontario": "ON",
              "quebec": "QC", "new brunswick": "NB", "nova scotia": "NS", "prince edward island": "PE",
              "newfoundland and labrador": "NL", "yukon": "YT", "northwest territories": "NT", "nunavut": "NU"}
NODE_URL = {}  # filename -> fin.gov.nt.ca node url


def norm_hdr(h):
    return re.sub(r"\s+", " ", str(h or "")).strip()


def to_date(v):
    if v is None or v == "":
        return None
    if isinstance(v, (dt.datetime, dt.date)):
        return v.strftime("%Y-%m-%d")
    s = str(v).strip()
    m = re.match(r"^(\d{4})-(\d{2})-(\d{2})", s)
    if m:
        return m.group(0)
    for fmt in ("%m/%d/%Y", "%d/%m/%Y", "%Y/%m/%d", "%b %d, %Y", "%d-%b-%y"):
        try:
            return dt.datetime.strptime(s, fmt).strftime("%Y-%m-%d")
        except ValueError:
            pass
    return None


def num(v):
    if v is None or v == "":
        return None
    if isinstance(v, (int, float)):
        return float(v)
    s = str(v).strip()
    if s.startswith("="):
        return None
    try:
        return float(s.replace(",", "").replace("$", ""))
    except ValueError:
        return None


def period_of(fname):
    m = re.search(r"apr(?:il)?_1_(\d{4})_to_([a-z]+)_(\d{1,2})_(\d{4})", fname)
    return m.group(0).replace("_", " ") if m else fname


def load_rows():
    allrows = []
    for path in sorted(glob.glob(os.path.join(DL, "node*.xlsx"))):
        fname = os.path.basename(path)
        wb = openpyxl.load_workbook(path, read_only=True)
        for ws in wb.worksheets:
            hdr = None
            for i, row in enumerate(ws.iter_rows(values_only=True)):
                vals = list(row)
                nv = [norm_hdr(v) for v in vals]
                if hdr is None:
                    if "Contract ID Number" in nv and "Contractor Name" in nv:
                        hdr = nv
                    continue
                if not any(v not in (None, "") for v in vals):
                    continue
                rec = {}
                for h, v in zip(hdr, vals):
                    if not h:
                        continue
                    if isinstance(v, (dt.datetime, dt.date)):
                        v = v.strftime("%Y-%m-%d")
                    rec[h] = v
                rec["_file"] = fname
                rec["_sheet"] = ws.title
                rec["_row"] = i + 1
                allrows.append(rec)
    return allrows


def main():
    stats = collections.Counter()
    rows = load_rows()
    stats["rows_total_standard_layout"] = len(rows)
    by_id = collections.defaultdict(list)
    for r in rows:
        cid = str(r.get("Contract ID Number") or "").strip()
        if not cid:
            stats["rows_no_contract_id"] += 1
            continue
        by_id[cid].append(r)
    stats["distinct_contract_ids"] = len(by_id)
    out = open(OUT, "w")
    for cid, rs in by_id.items():
        # latest report = max file node number (node ids increase with time), then max row
        rs.sort(key=lambda r: (int(re.search(r"node(\d+)", r["_file"]).group(1)), r["_row"]))
        latest = rs[-1]
        prov_raw = str(latest.get("Contractor Prov./Terr.") or "").strip()
        prov = PROV_NAMES.get(prov_raw.lower(), prov_raw.upper())
        if prov == "PEI":
            prov = "PE"
        if prov == "NWT":
            prov = "NT"
        if prov not in CA_PROV:
            stats["skip_prov_not_canadian:" + (prov_raw or "<blank>")] += 1
            continue
        start = to_date(latest.get("Contract Original Start Date"))
        end = to_date(latest.get("Expiry Date"))
        if not start:
            stats["skip_no_start"] += 1
            continue
        if start > REF.isoformat():
            stats["skip_not_started"] += 1
            continue
        if end and end < REF.isoformat():
            stats["skip_ended"] += 1
            continue
        status = "ongoing" if end else "end_date_unknown"
        basis = ("Contract Original Start Date %s <= 2026-10-25 <= Expiry Date %s (latest report %s)" % (start, end, period_of(latest["_file"]))
                 if end else "Expiry Date blank in the latest report (%s); start %s" % (period_of(latest["_file"]), start))
        amt_latest = num(latest.get("Revised Amount (for fiscal reporting period)"))
        if amt_latest is None:
            amt_latest = num(latest.get("Contract Amount (for fiscal reporting period)"))
        # sum of revised amounts across distinct reporting files is not additive (overlapping periods); keep per-row in raw
        buyer = str(latest.get("Contracting Department") or "").strip()
        vendor = str(latest.get("Contractor Name") or "").strip()
        if not buyer or not vendor:
            stats["skip_blank_party"] += 1
            continue
        rec = {
            "record_id": "ca_nwt:" + cid,
            "source": {
                "key": "ca_nwt",
                "name": "Government of the Northwest Territories Contract Report (contracts over $5,000, Contracts Reporting)",
                "publisher": "Government of the Northwest Territories, Department of Finance (Procurement Shared Services)",
                "dataset_url": "https://www.fin.gov.nt.ca/en/resources/contracts-over-5000-report?f%5B0%5D=field_resource_category_legacy%3A582",
                "record_url": None,
                "retrieved_at": RETRIEVED,
            },
            "status": status,
            "status_basis": basis,
            "contract": {
                "identifiers": {"contract_id_number": cid, "competition_id_number": (str(latest.get("Competition ID number") or "").strip() or None),
                                "set_id": (str(latest.get("SetID") or latest.get("Set ID") or "").strip() or None)},
                "title": str(latest.get("Contract Title") or "").strip() or None,
                "description": None,
                "instrument_type": str(latest.get("Contract Sub-type") or "").strip() or None,
                "procurement_method": str(latest.get("Contract Method") or "").strip() or None,
                "solicitation_procedure": str(latest.get("Contract Request Format") or "").strip() or None,
                "commodity": {"gnwt_bip_category": str(latest.get("Contract BIP Category") or "").strip() or None,
                              "gnwt_contract_type": str(latest.get("Contract Type") or "").strip() or None},
                "value": amt_latest, "currency": "CAD" if amt_latest is not None else None,
                "value_detail": {"latest_period_revised_amount": amt_latest,
                                 "latest_period_contract_amount": num(latest.get("Contract Amount (for fiscal reporting period)")),
                                 "latest_period_change_order_amount": num(latest.get("Change Order Amount (for fiscal reporting period)")),
                                 "latest_period_change_orders": num(latest.get("Change Orders (for fiscal reporting period)")),
                                 "note": "amounts are per fiscal reporting period, not cumulative contract value"},
                "dates": {"published": None, "signed": None, "start": start, "end": end, "amended_last": None},
                "related": {"contract_region": str(latest.get("Contract Region") or "").strip() or None,
                            "contract_bip_community": str(latest.get("Contract BIP Community") or "").strip() or None,
                            "reports_containing_contract": sorted(set(period_of(r["_file"]) for r in rs))},
            },
            "buyer": {"name": buyer, "country": "CA", "type": "GNWT department / territorial agency", "identifiers": {}, "address": {}, "contact": {}},
            "vendor": {
                "name": vendor, "country": "CA",
                "country_basis": "Contractor Prov./Terr. == %r (Canadian province/territory code) + Contractor City" % prov_raw,
                "identifiers": {},
                "address": {"line1": None, "city": str(latest.get("Contractor City") or "").strip() or None, "region": prov, "postal_code": None, "country": "Canada (inferred from province/territory code)"},
                "contact": {},
                "nwt_business_status": (lambda v, b: ("NWT Business" if b in ("BIP Registered", "NWT Non-BIP") else "Not in the NWT" if b == "Not in NWT" else None) if v.startswith("=") else (v or None))(str(latest.get("NWT Business Status") or "").strip(), str(latest.get("Contractor BIP Status") or "").strip()),
                "contractor_bip_status": str(latest.get("Contractor BIP Status") or "").strip() or None,
            },
            "raw": {"latest": latest, "rows": rs},
        }
        out.write(json.dumps(rec, ensure_ascii=False, default=str) + "\n")
        stats["emitted_" + status] += 1
    out.close()
    json.dump(dict(stats), open(STATS, "w"), indent=1)
    print(json.dumps(dict(stats), indent=1))


if __name__ == "__main__":
    main()
