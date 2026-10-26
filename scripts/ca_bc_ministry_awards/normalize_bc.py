#!/usr/bin/env python3
"""Normalize BC 'Ministry Contract Awards - Province of British Columbia' (DataBC) files.
Usage: python3 -I normalize_bc.py <download_dir> <out_jsonl> <stats_json>
"""
import csv, io, glob, json, os, re, sys, hashlib, datetime as dt, collections
import openpyxl

csv.field_size_limit(10 ** 8)
DL, OUT, STATS = sys.argv[1], sys.argv[2], sys.argv[3]
REF = dt.date(2026, 10, 25)
RETRIEVED = open(os.path.join(DL, "retrieved_at.txt")).read().split()[0]
PKG = json.load(open(os.path.join(DL, "package_show.json")))["result"]
RES_BY_FILE = {os.path.basename(r["url"]): r for r in PKG["resources"]}

PROV_FULL = {"british columbia": "BC", "alberta": "AB", "saskatchewan": "SK", "manitoba": "MB", "ontario": "ON",
             "quebec": "QC", "québec": "QC", "new brunswick": "NB", "nova scotia": "NS", "prince edward island": "PE",
             "newfoundland and labrador": "NL", "newfoundland": "NL", "yukon": "YT", "northwest territories": "NT",
             "nunavut": "NU"}
PROV_ABBR = {"BC", "AB", "SK", "MB", "ON", "QC", "NB", "NS", "PE", "PEI", "NL", "YT", "NT", "NU"}
POSTAL_RE = re.compile(r"\b[ABCEGHJ-NPRSTVXY]\d[ABCEGHJ-NPRSTV-Z][ -]?\d[ABCEGHJ-NPRSTV-Z]\d\b", re.I)
CA_COUNTRY = {"canada", "ca", "can"}
DATE_RE = re.compile(r"^\d{4}[/-]\d{2}[/-]\d{2}$")


def norm_date(s):
    if s is None:
        return None
    if isinstance(s, (dt.datetime, dt.date)):
        return s.strftime("%Y-%m-%d")
    s = str(s).strip()
    s = re.sub(r"^entered\s+", "", s, flags=re.I)
    m = re.match(r"^(\d{4})[/-](\d{1,2})[/-](\d{1,2})", s)
    if m:
        try:
            return dt.date(int(m.group(1)), int(m.group(2)), int(m.group(3))).isoformat()
        except ValueError:
            return None
    return None


def money(s):
    if s is None:
        return None
    if isinstance(s, (int, float)):
        return float(s)
    t = re.sub(r"[^\d.\-]", "", str(s))
    try:
        return float(t) if t not in ("", "-", ".") else None
    except ValueError:
        return None


def read_rows(path):
    name = os.path.basename(path)
    if path.endswith(".xlsx"):
        wb = openpyxl.load_workbook(path, read_only=True)
        ws = wb.worksheets[0]
        it = ws.iter_rows(values_only=True)
        hdr = [str(x).strip() if x is not None else "" for x in next(it)]
        for r in it:
            vals = ["" if v is None else (v.strftime("%Y-%m-%d") if isinstance(v, (dt.datetime, dt.date)) else str(v)) for v in r]
            if any(v.strip() for v in vals):
                yield name, hdr, vals
    else:
        raw = open(path, "rb").read()
        for enc in ("utf-8-sig", "cp1252", "latin-1"):
            try:
                txt = raw.decode(enc); break
            except UnicodeDecodeError:
                continue
        rd = csv.reader(io.StringIO(txt, newline=""))
        hdr = [x.strip() for x in next(rd)]
        for r in rd:
            if any(x.strip() for x in r):
                yield name, hdr, r


def province_from_address(addr):
    """Return (prov_code, postal, basis) if a Canadian province token is found in the address."""
    if not addr:
        return None, None, None
    a = addr.strip()
    low = a.lower()
    postal = POSTAL_RE.search(a)
    # trailing ' CA' country token (2025+ format: '... Burnaby British Columbia CA')
    m = re.search(r"\b(CA|Canada)\s*$", a, flags=re.I)
    for full, code in PROV_FULL.items():
        if re.search(r"\b" + re.escape(full) + r"\b", low):
            return code, postal.group(0) if postal else None, ("province name '%s' in address" % full) + (" + postal code" if postal else "") + (" + country token 'CA'" if m else "")
    tok = re.findall(r"\b([A-Z]{2})\b", a)
    for t in reversed(tok):
        if t in PROV_ABBR and (postal or re.search(r",\s*" + t + r"\b|\s" + t + r"\s+[A-Z]\d[A-Z]", a)):
            return ("PE" if t == "PEI" else t), postal.group(0) if postal else None, ("province abbreviation '%s' in address" % t) + (" + postal code" if postal else "")
    return None, postal.group(0) if postal else None, None


def main():
    stats = collections.Counter()
    seen_ids = set()
    out = open(OUT, "w")
    files = sorted(glob.glob(os.path.join(DL, "*.csv")) + glob.glob(os.path.join(DL, "*.xlsx")))
    for path in files:
        for fname, hdr, vals in read_rows(path):
            stats["rows_total"] += 1
            row = {hdr[i] if i < len(hdr) and hdr[i] else f"col{i}": vals[i] for i in range(len(vals))}
            g = lambda *ks: next((row[k] for k in ks if k in row and str(row[k]).strip() != ""), None)
            country_field = g("Country", "Successful Vendor Country")
            province_field = g("Province", "Province / State")
            city = g("Successful Vendor City")
            addr = g("Successful Vendor Address")
            vendor = g("Successful Vendor")
            if not vendor or vendor.strip().upper() in ("N/A", "NA", "NONE", "NO AWARD", "CANCELLED"):
                stats["skip_no_vendor"] += 1
                continue
            # --- vendor country ---
            country = None; basis = None; prov = None; postal = None
            if country_field and DATE_RE.match(country_field.strip()):
                # shifted columns (2022 Q1 file): country cell holds a date -> no country info
                country_field = None
            if country_field:
                cf = country_field.strip().lower()
                if cf in CA_COUNTRY:
                    country = "CA"; basis = "'%s' column == %r" % ("Successful Vendor Country" if "Successful Vendor Country" in row else "Country", country_field.strip())
                elif cf in ("n/a", ""):
                    pass
                else:
                    stats["skip_foreign_country_field"] += 1
                    continue
            if country is None and province_field:
                pf = province_field.strip().lower()
                if pf in PROV_FULL:
                    country = "CA"; prov = PROV_FULL[pf]
                    basis = "Province column == %r (Canadian province; Country column %s)" % (province_field.strip(), "blank" if not country_field else repr(country_field))
                elif province_field.strip().upper() in PROV_ABBR:
                    country = "CA"; prov = province_field.strip().upper()
                    basis = "Province column == %r" % province_field.strip()
                else:
                    stats["skip_foreign_province_field"] += 1
                    continue
            if country is None and addr:
                p, postal, b = province_from_address(addr)
                if p:
                    country = "CA"; prov = p; basis = "Successful Vendor Address: " + b
            if country is None:
                stats["skip_no_country_info"] += 1
                continue
            if prov is None and province_field and province_field.strip().lower() in PROV_FULL:
                prov = PROV_FULL[province_field.strip().lower()]
            if prov is None and addr:
                p, postal2, _ = province_from_address(addr)
                prov = prov or p; postal = postal or postal2
            # --- dates ---
            awarded = norm_date(g("Date Awarded"))
            issued = norm_date(g("Issued Date"))
            closing = norm_date(g("Closing Date"))
            if awarded and awarded > REF.isoformat():
                stats["skip_future_award"] += 1
                continue
            tender_no = g("Tender No", "Opportunity ID")
            amount = money(g("Award Total"))
            key = "|".join([fname, str(tender_no), vendor, str(awarded), str(g("Award Total")), str(g("Title"))])
            rid = "ca_bc_ministry_awards:" + hashlib.sha1(key.encode("utf-8")).hexdigest()[:16]
            if rid in seen_ids:
                stats["dup_rows"] += 1
                continue
            seen_ids.add(rid)
            res = RES_BY_FILE.get(fname, {})
            buyer_for = g("Issued for Organization")
            buyer_by = g("Issued by Organization")
            buyer_name = (buyer_for or buyer_by or "").strip()
            if not buyer_name:
                stats["skip_no_buyer"] += 1
                continue
            rec = {
                "record_id": rid,
                "source": {
                    "key": "ca_bc_ministry_awards",
                    "name": "Ministry Contract Awards - Province of British Columbia (BC Bid contract award summaries)",
                    "publisher": "Province of British Columbia, Ministry of Citizens' Services (Procurement Services Branch) via BC Data Catalogue",
                    "dataset_url": "https://catalogue.data.gov.bc.ca/dataset/ministry-contract-awards-province-of-british-columbia",
                    "record_url": None,
                    "retrieved_at": RETRIEVED,
                },
                "status": "end_date_unknown",
                "status_basis": "Source publishes only Date Awarded (%s), Issued Date and Closing Date; no contract start/end/term field exists in any file version, so the end date is unknown." % awarded,
                "contract": {
                    "identifiers": {k: v for k, v in {
                        "tender_no": g("Tender No"), "opportunity_id": g("Opportunity ID"),
                        "bc_data_catalogue_resource_id": res.get("id")}.items() if v},
                    "title": (g("Title") or "").strip() or None,
                    "description": None,
                    "instrument_type": "contract award summary",
                    "procurement_method": (g("Procurement Method") or "").strip() or None,
                    "solicitation_procedure": None,
                    "commodity": {},
                    "value": amount, "currency": "CAD" if amount is not None else None,
                    "value_detail": {"award_total": amount} if amount is not None else {},
                    "dates": {"published": issued, "signed": None, "start": None, "end": None,
                              "amended_last": None, "awarded": awarded, "tender_closing": closing},
                    "related": {"amendments_count": g("Amendments"), "source_file": fname,
                                "source_file_url": res.get("url")},
                },
                "buyer": {
                    "name": buyer_name, "country": "CA",
                    "type": "BC provincial ministry/agency or BC public-sector organization (as named)",
                    "identifiers": {}, "address": {},
                    "contact": {},
                    "issued_by_organization": buyer_by,
                },
                "vendor": {
                    "name": vendor.strip(), "country": "CA", "country_basis": basis,
                    "identifiers": {},
                    "address": {"line1": addr.strip() if addr else None, "city": city.strip() if city else None,
                                "region": prov, "postal_code": postal, "country": country_field.strip() if country_field else None},
                    "contact": {},
                },
                "raw": dict(row, **{"_source_file": fname}),
            }
            out.write(json.dumps(rec, ensure_ascii=False) + "\n")
            stats["emitted"] += 1
            stats["emitted_year_" + (awarded or "unknown")[:4]] += 1
    out.close()
    json.dump(dict(stats), open(STATS, "w"), indent=1)
    print(json.dumps(dict(stats), indent=1))


if __name__ == "__main__":
    main()
