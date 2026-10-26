#!/usr/bin/env python3
"""Parse NL Public Procurement Agency 'Contract Awards Report' PDFs (semi-monthly) into rows, then normalize.
Usage: python3 -I parse_nl.py <download_dir> <rows_jsonl> <out_jsonl> <stats_json>
"""
import glob, json, os, re, sys, datetime as dt, collections, hashlib
import pdfplumber

DL, ROWS_OUT, OUT, STATS = sys.argv[1:5]
REF = dt.date(2026, 10, 25)
RETRIEVED = open(os.path.join(DL, "retrieved_at.txt")).read().split()[0]
CA_PROV = {"NL", "NS", "NB", "PE", "PEI", "QC", "ON", "MB", "SK", "AB", "BC", "YT", "NT", "NU", "NFLD", "NF", "PQ"}
PROV_NAMES = {"newfoundland and labrador": "NL", "newfoundland": "NL", "nova scotia": "NS", "new brunswick": "NB",
              "prince edward island": "PE", "quebec": "QC", "québec": "QC", "ontario": "ON", "manitoba": "MB",
              "saskatchewan": "SK", "alberta": "AB", "british columbia": "BC", "yukon": "YT", "northwest territories": "NT", "nunavut": "NU"}
HEADER_KEYS = ["public body", "type of", "description", "supplier name", "supplier location", "contract price", "contract #", "date of", "term of", "renewal"]


def norm(s):
    if s is None:
        return None
    return re.sub(r"\s+", " ", str(s).replace("\n", " ")).strip()


def is_header(row):
    j = " ".join(norm(c) or "" for c in row).lower()
    return "public body" in j and "supplier" in j


def map_header(row):
    cols = []
    for c in row:
        t = (norm(c) or "").lower()
        if "public body" in t: cols.append("public_body")
        elif t.startswith("type of"): cols.append("type_of_procurement")
        elif "relevant clause" in t: cols.append("relevant_clause_if_other")
        elif t == "description": cols.append("description")
        elif "commodity" in t: cols.append("commodity_type")
        elif "supplier name" in t: cols.append("supplier_name")
        elif "city" in t or "town" in t: cols.append("supplier_city")
        elif "province" in t or "prov" in t or "state" in t: cols.append("supplier_province_state")
        elif "contract price" in t or "price" in t: cols.append("contract_price_excl_hst")
        elif "contract #" in t or t.startswith("contract#") or t == "contract": cols.append("contract_number")
        elif "date of" in t or t.startswith("award date") or t == "date": cols.append("date_of_award")
        elif "term" in t: cols.append("term_of_contract")
        elif "renewal" in t: cols.append("renewal_options")
        else: cols.append("col_" + re.sub(r"[^a-z0-9]+", "_", t)[:30])
    return cols


def parse_pdf(path):
    rows = []
    fname = os.path.basename(path)
    period = None
    cols = None
    with pdfplumber.open(path) as pdf:
        for pno, page in enumerate(pdf.pages):
            try:
                tables = page.extract_tables()
            except Exception:
                tables = []
            text = page.extract_text() or ""
            m = re.search(r"REPORTING PERIOD:\s*(.+)", text)
            if m and not period:
                period = norm(m.group(1))
            for t in tables:
                for row in t:
                    if row is None or all(c in (None, "") for c in row):
                        continue
                    if is_header(row):
                        cols = map_header(row)
                        continue
                    if cols is None:
                        continue
                    if len(row) < 5:
                        continue
                    first = norm(row[0]) or ""
                    if first.startswith("Government of Newfoundland") or first.startswith("CONTRACT AWARDS") or first.startswith("Page ") or first.startswith("EXCEPTIONS"):
                        continue
                    rec = {}
                    for i, c in enumerate(row):
                        key = cols[i] if i < len(cols) else f"col_{i}"
                        rec[key] = norm(c)
                    if not rec.get("supplier_name") and not rec.get("public_body"):
                        continue
                    rec["_file"] = fname; rec["_page"] = pno + 1; rec["_reporting_period"] = period
                    rows.append(rec)
    return rows


def pdate(s):
    if not s:
        return None
    s = s.strip().replace("\u2010", "-").replace("\u2011", "-").replace("\u2013", "-")
    for fmt in ("%m/%d/%Y", "%m/%d/%y", "%B %d, %Y", "%b %d, %Y", "%Y-%m-%d", "%d-%b-%y", "%d-%b-%Y"):
        try:
            return dt.datetime.strptime(s, fmt).date()
        except ValueError:
            pass
    m = re.match(r"^(\d{1,2})/(\d{1,2})/(\d{4})", s)
    if m:
        try:
            return dt.date(int(m.group(3)), int(m.group(1)), int(m.group(2)))
        except ValueError:
            return None
    return None


def term_to_end(term, award):
    """Map 'Term of Contract' to an end date when it is a duration (N Years/Months) or an explicit date."""
    if not term or not award:
        return None, None
    t = term.strip()
    d = pdate(t)
    if d:
        return d, "Term of Contract column holds an explicit date %s" % d.isoformat()
    m = re.match(r"^<?\s*(\d+(?:\.\d+)?)\s*(year|yr|month|mo|week|day)s?\b", t, re.I)
    if m:
        n = float(m.group(1)); unit = m.group(2).lower()
        days = {"year": 365.25, "yr": 365.25, "month": 30.44, "mo": 30.44, "week": 7, "day": 1}[unit]
        end = award + dt.timedelta(days=round(n * days))
        return end, "Term of Contract %r: end = award date %s + %g %s(s) = %s" % (t, award.isoformat(), n, unit, end.isoformat())
    return None, None


def money(s):
    if not s:
        return None
    t = re.sub(r"[^\d.\-]", "", s)
    try:
        return float(t) if t not in ("", "-", ".") else None
    except ValueError:
        return None


def main():
    stats = collections.Counter()
    allrows = []
    for path in sorted(glob.glob(os.path.join(DL, "pdf", "*.pdf"))):
        try:
            rows = parse_pdf(path)
        except Exception as e:
            stats["pdf_failed"] += 1; print("FAIL", path, e); continue
        stats["pdf_parsed"] += 1
        allrows.extend(rows)
    with open(ROWS_OUT, "w") as f:
        for r in allrows:
            f.write(json.dumps(r, ensure_ascii=False) + "\n")
    stats["rows_total"] = len(allrows)
    out = open(OUT, "w")
    seen = set()
    for r in allrows:
        prov_raw = (r.get("supplier_province_state") or "").strip()
        city = (r.get("supplier_city") or "").strip()
        supplier = (r.get("supplier_name") or "").strip()
        buyer = (r.get("public_body") or "").strip()
        if not supplier or not buyer:
            stats["skip_missing_party"] += 1; continue
        pr = prov_raw.upper().replace(".", "")
        prov = None
        if pr in CA_PROV:
            prov = {"PEI": "PE", "NFLD": "NL", "NF": "NL", "PQ": "QC"}.get(pr, pr)
            basis = "Supplier Location (Province/State) == %r (Canadian province/territory)" % prov_raw
        elif prov_raw.lower() in PROV_NAMES:
            prov = PROV_NAMES[prov_raw.lower()]; basis = "Supplier Location (Province/State) == %r" % prov_raw
        elif re.search(r"\b(usa|us|united states)\b", prov_raw.lower()) or re.match(r"^[A-Z]{2},?\s*USA", pr):
            stats["skip_foreign"] += 1; continue
        elif prov_raw:
            stats["skip_other_location:" + prov_raw[:20]] += 1; continue
        else:
            stats["skip_blank_province"] += 1; continue
        award = pdate(r.get("date_of_award"))
        if award and award > REF:
            stats["skip_future_award"] += 1; continue
        end, how = term_to_end(r.get("term_of_contract"), award)
        if end:
            if end < REF:
                stats["skip_ended_by_term"] += 1; continue
            status = "ongoing_inferred" if "+" in how else "ongoing"
            basis_status = how + "; award date %s <= 2026-10-25 <= %s" % (award.isoformat(), end.isoformat())
        else:
            status = "end_date_unknown"
            basis_status = "Term of Contract is %r (not a usable duration/date); award date %s" % (r.get("term_of_contract"), award.isoformat() if award else None)
        key = "|".join([r["_file"], buyer, supplier, r.get("contract_number") or "", r.get("date_of_award") or "", r.get("contract_price_excl_hst") or "", r.get("description") or ""])
        rid = "ca_newfoundland:" + hashlib.sha1(key.encode()).hexdigest()[:16]
        if rid in seen:
            stats["dup"] += 1; continue
        seen.add(rid)
        amount = money(r.get("contract_price_excl_hst"))
        rec = {
            "record_id": rid,
            "source": {
                "key": "ca_newfoundland",
                "name": "NL Public Procurement Agency - Contract Awards Reports (semi-monthly PDF reports to the Chief Procurement Officer, s.31 Public Procurement Regulations)",
                "publisher": "Government of Newfoundland and Labrador, Public Procurement Agency",
                "dataset_url": "https://www.gov.nl.ca/ppa/tenders/awarded/",
                "record_url": None,
                "retrieved_at": RETRIEVED,
            },
            "status": status, "status_basis": basis_status,
            "contract": {
                "identifiers": {"contract_number": r.get("contract_number") or None},
                "title": r.get("description"), "description": r.get("description"),
                "instrument_type": "contract award (%s)" % (r.get("type_of_procurement") or "unspecified"),
                "procurement_method": r.get("type_of_procurement"),
                "solicitation_procedure": r.get("relevant_clause_if_other") or None,
                "commodity": {"nl_commodity_type": r.get("commodity_type")},
                "value": amount, "currency": "CAD" if amount is not None else None,
                "value_detail": {"contract_price_excl_hst": amount} if amount is not None else {},
                "dates": {"published": None, "signed": None, "start": None, "end": end.isoformat() if end else None, "amended_last": None,
                          "awarded": award.isoformat() if award else None},
                "related": {"term_of_contract": r.get("term_of_contract"), "renewal_options": r.get("renewal_options"),
                            "report_file": r["_file"], "report_url": "https://www.gov.nl.ca/ppa/files/" + r["_file"],
                            "reporting_period": r.get("_reporting_period"), "report_page": r.get("_page")},
            },
            "buyer": {"name": buyer, "country": "CA", "type": "NL public body (department, agency, Crown corporation, health authority, municipality, post-secondary) as named",
                      "identifiers": {}, "address": {}, "contact": {}},
            "vendor": {"name": supplier, "country": "CA", "country_basis": basis, "identifiers": {},
                       "address": {"line1": None, "city": city or None, "region": prov, "postal_code": None, "country": None},
                       "contact": {}},
            "raw": r,
        }
        out.write(json.dumps(rec, ensure_ascii=False) + "\n")
        stats["emitted_" + status] += 1
    out.close()
    json.dump(dict(stats), open(STATS, "w"), indent=1)
    print(json.dumps(dict(stats), indent=1))


if __name__ == "__main__":
    main()
