#!/usr/bin/env python3
"""CMHC (Canada Mortgage and Housing Corporation) "Disclosure of contracts over $10,000" monthly/quarterly XLSX files ->
normalized/ca_crown_cmhc_unverified_country.jsonl (CMHC publishes no supplier address/country, so every record is
vendor-location-unverified) and an (empty) normalized/ca_crown_cmhc.jsonl.
Usage: python3 -I build_cmhc.py <xlsx_dir> <links.txt> <download.log> <out_main.jsonl> <out_unverified.jsonl> <stats.json>
"""
import sys, os, re, json, glob, hashlib, datetime, collections
import openpyxl

D, LINKS, DLOG, OUT, OUTU, STATS = sys.argv[1:7]
REF = datetime.date(2026, 10, 25)
PAGE = "https://www.cmhc-schl.gc.ca/about-us/corporate-reporting/transparency/procurement/disclosure-of-contracts-over-10000"
MON = {m: i for i, m in enumerate(["jan", "feb", "mar", "apr", "may", "jun", "jul", "aug", "sep", "oct", "nov", "dec"], 1)}
url_of, ret_of = {}, {}
for u in open(LINKS).read().split():
    url_of[os.path.basename(u.split("?")[0])] = u
for l in open(DLOG):
    p = l.split()
    if len(p) >= 4 and p[1] == "200":
        ret_of[os.path.basename(p[3].split("?")[0])] = p[0]
stats = collections.Counter()


def period(fn):
    f = fn.lower()
    m = re.search(r"(jan|feb|mar|apr|may|jun|jul|aug|sep|oct|nov|dec)[a-z]*-(\d{4})", f) or None
    if m:
        return f"{m.group(2)}-{MON[m.group(1)]:02d}"
    m = re.search(r"(\d{4})-contracts-over-10k-(jan|feb|mar|apr|may|jun|jul|aug|sep|oct|nov|dec)", f)
    if m:
        return f"{m.group(1)}-{MON[m.group(2)]:02d}"
    m = re.search(r"q([1-4])-(\d{4})", f)
    if m:
        return f"{m.group(2)}-Q{m.group(1)}"
    m = re.search(r"(\d{4})", f)
    return m.group(1) if m else "0000"


def pdate(v):
    if isinstance(v, datetime.datetime):
        return v.date()
    if isinstance(v, datetime.date):
        return v
    s = str(v or "").strip()
    for fmt in ("%Y-%m-%d", "%Y/%m/%d", "%d/%m/%Y", "%m/%d/%Y", "%m/%d/%y", "%B %d, %Y", "%b %d, %Y", "%Y-%m-%d %H:%M:%S"):
        try:
            return datetime.datetime.strptime(s, fmt).date()
        except ValueError:
            pass
    return None


def pmoney(v):
    if isinstance(v, (int, float)):
        return float(v), "CAD"
    s = str(v or "").strip()
    cur = "USD" if "USD" in s.upper() else ("EUR" if "EUR" in s.upper() else "CAD")
    s2 = re.sub(r"[^0-9.\-]", "", s.replace(",", ""))
    try:
        return float(s2), cur
    except ValueError:
        return None, None


def colrole(h):
    h = re.sub(r"\s+", " ", str(h or "").replace("_x000D_", " ")).strip().lower()
    if h.startswith(("supplier", "vendor")):
        return "supplier"
    if "scope" in h:
        return "scope"
    if "before amendment" in h:
        return "value_before"
    if h.startswith("amendment amount"):
        return "amendment_amount"
    if "incl. amendment" in h:
        return "value_total"
    if "value" in h:
        return "value"
    if "start" in h or "effective" in h:
        return "start"
    if "end date" in h or "expir" in h or h.startswith("end") or "completion" in h:
        return "end"
    if "contract number" in h or "contract no" in h or h.startswith("number"):
        return "contract_number"
    return None


def kind_of(title):
    t = title.lower()
    if "amend" in t:
        return "amendment"
    if "call" in t:
        return "call-up"
    if "correction" in t:
        return "correction"
    return "contract"


def nk(s):
    return re.sub(r"[^A-Z0-9]", "", str(s or "").upper())


groups = collections.defaultdict(list)
for f in sorted(glob.glob(os.path.join(D, "*.xlsx"))):
    fn = os.path.basename(f)
    try:
        wb = openpyxl.load_workbook(f, read_only=True, data_only=True)
    except Exception as e:
        stats["bad_file"] += 1
        continue
    per = period(fn)
    for si, ws in enumerate(wb.worksheets):
        hdr = None; roles = None
        for ri, row in enumerate(ws.iter_rows(values_only=True), 1):
            if hdr is None:
                vals = [str(v).strip() if v is not None else "" for v in row]
                if vals and vals[0].lower().startswith(("supplier", "vendor")):
                    hdr = vals; roles = [colrole(h) for h in vals]
                    title_lines = []
                continue
            vals = list(row)
            if not any(v not in (None, "") for v in vals):
                continue
            v0 = str(vals[0] or "").strip().lower()
            if v0.startswith(("supplier", "vendor")):
                hdr = [str(v).strip() if v is not None else "" for v in vals]; roles = [colrole(h) for h in hdr]
                continue
            rec = {}
            for r, v in zip(roles, vals):
                if r and r not in rec:
                    rec[r] = v
            sup = str(rec.get("supplier") or "").strip()
            if not sup or sup.lower().startswith(("total", "note", "*")):
                continue
            rawrow = {hdr[i] if i < len(hdr) and hdr[i] else f"col{i + 1}": (v.isoformat() if isinstance(v, (datetime.date, datetime.datetime)) else v) for i, v in enumerate(vals) if v not in (None, "")}
            start, end = pdate(rec.get("start")), pdate(rec.get("end"))
            cn = str(rec.get("contract_number") or "").strip()
            key = ("CN", nk(cn), nk(sup)[:30]) if len(nk(cn)) >= 5 else (nk(sup)[:60], nk(rec.get("scope"))[:50], start.isoformat() if start else "")
            groups[key].append({"file": fn, "period": per, "sheet": ws.title, "sheet_index": si, "row": ri, "kind": kind_of(ws.title),
                                "supplier": sup, "scope": str(rec.get("scope") or "").strip() or None, "start": start, "end": end, "contract_number": cn or None,
                                "value": rec.get("value"), "value_before": rec.get("value_before"), "amendment_amount": rec.get("amendment_amount"),
                                "value_total": rec.get("value_total"), "raw_row": rawrow})
            stats["rows"] += 1
stats["groups"] = len(groups)

fo = open(OUT, "w"); fu = open(OUTU, "w"); by_status = collections.Counter()
order = {"contract": 0, "call-up": 1, "correction": 2, "amendment": 3}
for key, rows in groups.items():
    rows.sort(key=lambda r: (r["period"], order.get(r["kind"], 9), r["row"]))
    last = rows[-1]
    ends = [r["end"] for r in rows if r["end"]]
    end = last["end"] or (ends[-1] if ends else None)
    start = last["start"] or next((r["start"] for r in rows if r["start"]), None)
    if end and end < REF:
        stats["excluded_ended"] += 1; continue
    if start and start > REF:
        stats["excluded_future_start"] += 1; continue
    if end:
        status = "ongoing"
        basis = f"ongoing: CMHC disclosure latest row ({last['file']}, sheet '{last['sheet']}') End Date {end.isoformat()} >= 2026-10-25 and Start Date {start.isoformat() if start else 'n/a'} <= 2026-10-25"
    else:
        status = "end_date_unknown"
        basis = f"end_date_unknown: CMHC disclosure rows give no end date (latest {last['file']}, sheet '{last['sheet']}')"
    # value: latest total incl. amendments, else latest contract/call-up value
    val, cur = None, None
    for r in reversed(rows):
        for fld in ("value_total", "value"):
            if r.get(fld) not in (None, ""):
                val, cur = pmoney(r[fld]); break
        if val is not None:
            break
    orig = next((pmoney(r["value"])[0] for r in rows if r["kind"] in ("contract", "call-up") and r.get("value") not in (None, "")), None)
    kinds = sorted({r["kind"] for r in rows})
    inst = "call-up" if "call-up" in kinds and "contract" not in kinds else "contract"
    h = hashlib.sha1("|".join(key).encode()).hexdigest()[:16]
    rec = {"record_id": f"ca_crown_cmhc:{h}",
           "source": {"key": "ca_crown_cmhc", "name": "CMHC - Disclosure of contracts over $10,000 (monthly XLSX)",
                      "publisher": "Canada Mortgage and Housing Corporation", "dataset_url": PAGE, "record_url": None,
                      "retrieved_at": ret_of.get(last["file"])},
           "status": status, "status_basis": basis,
           "contract": {"identifiers": {"cmhc_group_key": "|".join(key), "cmhc_contract_numbers": sorted({r["contract_number"] for r in rows if r.get("contract_number")}) or None, "cmhc_files": sorted({r["file"] for r in rows})},
                        "title": last["scope"], "description": last["scope"], "instrument_type": inst,
                        "procurement_method": None, "solicitation_procedure": None, "commodity": {},
                        "value": val, "currency": cur,
                        "value_detail": {"original_value": orig, "latest_total_incl_amendments": pmoney(last["value_total"])[0] if last.get("value_total") not in (None, "") else None,
                                         "amendment_rows": sum(1 for r in rows if r["kind"] == "amendment"), "value_note": "values include taxes"},
                        "dates": {"published": None, "signed": None, "start": start.isoformat() if start else None, "end": end.isoformat() if end else None,
                                  "amended_last": None, "last_reported_period": last["period"], "first_reported_period": rows[0]["period"]},
                        "related": {"source_file_urls": sorted({url_of.get(r["file"]) for r in rows if url_of.get(r["file"])})}},
           "buyer": {"name": "Canada Mortgage and Housing Corporation", "country": "CA", "type": "crown corporation",
                     "identifiers": {"abbreviation": "CMHC"}, "address": {}, "contact": {}},
           "vendor": {"name": last["supplier"], "country": None,
                      "country_basis": "not published: CMHC's disclosure lists supplier name only (no address or country)",
                      "identifiers": {"supplier_name_variants": sorted({r["supplier"] for r in rows})}, "address": {}, "contact": {}},
           "raw": {"rows": [{k: (v.isoformat() if isinstance(v, datetime.date) else v) for k, v in r.items()} for r in rows]}}
    fu.write(json.dumps(rec, ensure_ascii=False, default=str) + "\n"); by_status[status] += 1
fo.close(); fu.close()
json.dump({"stats": stats, "by_status_unverified": by_status}, open(STATS, "w"), indent=1)
print(dict(stats), dict(by_status))
