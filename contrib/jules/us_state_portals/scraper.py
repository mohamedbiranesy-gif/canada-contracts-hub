import urllib.request
import urllib.parse
import json
import os
import gzip
import re
from datetime import datetime, timezone
import collections

REF_DATE = "2026-11-02"
USER_AGENT = "contracts-research/1.0"
PROVS = ["ON", "ONT", "ONTARIO", "QC", "PQ", "QUE", "QUEBEC", "QUÉBEC", "BC", "B.C.", "BRITISH COLUMBIA", "AB", "ALTA",
         "ALBERTA", "MB", "MAN", "MANITOBA", "SK", "SASK", "SASKATCHEWAN", "NS", "N.S.", "NOVA SCOTIA", "NB", "N.B.",
         "NEW BRUNSWICK", "NL", "NF", "NFLD", "NEWFOUNDLAND", "NEWFOUNDLAND AND LABRADOR", "PE", "PEI", "P.E.I.",
         "PRINCE EDWARD ISLAND", "YT", "YUKON", "NT", "NWT", "NORTHWEST TERRITORIES", "NU", "NUNAVUT", "CANADA", "CAN"]

PC_FULL = re.compile(r"\b([ABCEGHJ-NPRSTVXY]\d[ABCEGHJ-NPRSTV-Z])[ -]?(\d[ABCEGHJ-NPRSTV-Z]\d)\b", re.I)

def fetch_socrata(domain, dataset_id):
    url = f"https://{domain}/api/views/{dataset_id}/rows.json?accessType=DOWNLOAD"
    try:
        req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
        res = urllib.request.urlopen(req)
        return json.loads(res.read())
    except Exception as e:
        print(f"Error fetching {url}: {e}")
        return None

def is_canada(country, state, zip_code):
    c = str(country).strip().upper() if country else ""
    s = str(state).strip().upper() if state else ""
    if c in ("US", "USA", "UNITED STATES"):
        return False, ""

    if c:
        if c in ("CA", "CAN", "CANADA", "CDN") or "CANADA" in c:
            return True, f"country='{country}'"
    if s:
        if s in PROVS:
            return True, f"state='{state}'"
    if zip_code:
        z = str(zip_code).strip()
        if PC_FULL.search(z):
            return True, f"zip='{zip_code}'"
    return False, ""

def process():
    datasets = [
        ('data.ny.gov', 'ehig-g5x3', 'Procurement Report for State Authorities'),
        ('data.ny.gov', '8w5p-k45m', 'Procurement Report for Local Authorities'),
        ('data.ny.gov', 'd84c-dk28', 'Procurement Report for Local Development Corporations'),
        ('data.ny.gov', 'p3p6-xqr5', 'Procurement Report for Industrial Development Agencies'),
    ]

    records = []

    for domain, ds_id, name in datasets:
        j = fetch_socrata(domain, ds_id)
        if not j or 'data' not in j:
            continue

        cols = j['meta']['view']['columns']
        col_names = [c['name'].lower() for c in cols]

        try:
            auth_idx = col_names.index('authority name')
            vend_idx = col_names.index('vendor name')
            ctry_idx = col_names.index('vendor country')
            state_idx = col_names.index('vendor state')
            zip_idx = col_names.index('vendor postal code')
            start_idx = col_names.index('begin date') if 'begin date' in col_names else None
            end_idx = col_names.index('end date')
            award_idx = col_names.index('award date')
            amt_idx = col_names.index('contract amount')
            desc_idx = col_names.index('procurement description')
        except ValueError as e:
            print(f"Missing column in {ds_id}:", e)
            continue

        for row in j['data']:
            country = row[ctry_idx]
            state = row[state_idx]
            zip_code = row[zip_idx]

            is_can, basis = is_canada(country, state, zip_code)
            if not is_can: continue

            start = (row[start_idx] or "")[:10] if start_idx is not None else None
            end = (row[end_idx] or "")[:10]
            award = (row[award_idx] or "")[:10]

            status = "end_date_unknown"
            sbasis = "No end date"

            ref = REF_DATE
            if end:
                if (start or award or "1900-01-01") <= ref <= end:
                    status = "ongoing"
                    sbasis = f"start/award <= {ref} <= end ({end})"
                elif end < ref:
                    continue # ended
                elif (start or award or "") > ref:
                    continue # future
            elif (start or award):
                try:
                    yr = int((start or award)[:4])
                    if yr >= 2023:
                        status = "end_date_unknown"
                        sbasis = "Recent award, no end date"
                    else:
                        continue
                except:
                    continue
            else:
                status = "end_date_unknown"
                sbasis = "No dates"

            raw = {cols[i]['name']: row[i] for i in range(len(cols))}

            try:
                amt = float(row[amt_idx]) if row[amt_idx] else None
            except:
                amt = None

            record = {
                "record_id": f"us_state_portals:ny_{ds_id}:{row[0]}",
                "source": {
                    "key": "us_state_portals",
                    "name": name,
                    "publisher": domain,
                    "dataset_url": f"https://{domain}/d/{ds_id}",
                    "record_url": None,
                    "retrieved_at": datetime.now(timezone.utc).isoformat().replace("+00:00", "Z")
                },
                "status": status,
                "status_basis": sbasis,
                "link": f"https://{domain}/d/{ds_id}",
                "link_type": "dataset",
                "contract": {
                    "identifiers": {},
                    "title": row[desc_idx] or "",
                    "description": row[desc_idx] or "",
                    "value": amt,
                    "currency": "USD",
                    "dates": {
                        "start": start,
                        "end": end,
                        "signed": award,
                    }
                },
                "buyer": {
                    "name": row[auth_idx] or "",
                    "country": "US",
                    "type": "authority"
                },
                "vendor": {
                    "name": row[vend_idx] or "",
                    "country": "CA",
                    "country_basis": basis
                },
                "raw": raw
            }
            records.append(record)

    print(f"Total CA ongoing/unknown records: {len(records)}")
    with gzip.open("data/incoming/jules/records_us_state_portals.jsonl.gz", "wt") as f:
        for r in records:
            f.write(json.dumps(r, ensure_ascii=False) + "\n")

    with open("notes/us_state_portals.md", "w") as f:
        f.write(f"# US State Portals\n\n")
        f.write(f"- Built scraper for NY OpenBook datasets from data.ny.gov using Socrata API\n")
        f.write(f"- Datasets included:\n")
        f.write(f"  - Procurement Report for State Authorities: ehig-g5x3\n")
        f.write(f"  - Procurement Report for Local Authorities: 8w5p-k45m\n")
        f.write(f"  - Procurement Report for Local Development Corporations: d84c-dk28\n")
        f.write(f"  - Procurement Report for Industrial Development Agencies: p3p6-xqr5\n")
        f.write(f"- CA filter based on vendor country, state, zip. CA is no longer used for state, and US/USA is filtered out for country\n")
        f.write(f"- Total records retrieved matching criteria: {len(records)}\n")

if __name__ == '__main__':
    process()
