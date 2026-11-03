import sys, json, urllib.request, datetime, os
sys.path.insert(0, "scripts/us_common")
from common import *

REF_DATE = datetime.date(2026, 11, 2)
RECENT_CUTOFF = datetime.date(2023, 11, 2)

URL = "https://data.cityofnewyork.us/resource/qyyg-4tf5.json?$where=upper(vendor_address)%20like%20'%25CANADA%25'&$limit=50000"

def fetch():
    req = urllib.request.Request(URL, headers={"User-Agent": "contracts-research/1.0"})
    with urllib.request.urlopen(req) as response:
        data = json.loads(response.read().decode())
    return data

def process():
    data = fetch()
    out = sys.argv[1] if len(sys.argv) > 1 else "contrib/jules/us_city_new_york/records.jsonl"

    records = []

    for r in data:
        start_s = r.get("start_date")
        end_s = r.get("end_date")

        start_date = start_s[:10] if start_s else None
        end_date = end_s[:10] if end_s else None

        award_date = r.get("event_date", "")[:10] if r.get("event_date") else None

        eff_start = start_date or award_date

        status = "end_date_unknown"
        status_basis = "Award/contract published, nothing usable about end date"

        if eff_start and end_date:
            if eff_start <= str(REF_DATE) and end_date >= str(REF_DATE):
                status = "ongoing"
                status_basis = f"start/award ({eff_start}) <= ref <= end ({end_date})"
            else:
                if start_date == end_date:
                    if eff_start >= str(datetime.date(2023, 11, 2)):
                        status = "end_date_unknown"
                        status_basis = f"Start/end same day, awarded within 3 years of ref ({eff_start})"
                        end_date = None
                    else:
                        status = "stale"
                else:
                    status = "ended"
        elif eff_start:
             if eff_start >= str(datetime.date(2023, 11, 2)):
                 status = "end_date_unknown"
                 status_basis = f"Awarded within 3 years of ref ({eff_start})"
             else:
                 status = "stale"

        if status in ("ended", "stale"):
            continue

        addr = r.get("vendor_address", "")
        if "CANADA" not in addr.upper():
            continue

        rec = {
            "record_id": f"us_city_new_york:{r.get('request_id')}",
            "source": {
                "key": "us_city_new_york",
                "name": "Recent Contract Awards (City of New York)",
                "publisher": "City of New York",
                "dataset_url": "https://data.cityofnewyork.us/City-Government/Recent-Contract-Awards/qyyg-4tf5",
                "record_url": None,
                "retrieved_at": datetime.datetime.now(datetime.timezone.utc).isoformat()
            },
            "status": status,
            "status_basis": status_basis,
            "contract": {
                "identifiers": {
                    "request_id": r.get("request_id"),
                    "pin": r.get("pin")
                },
                "title": r.get("short_title", ""),
                "description": r.get("additional_description_1", ""),
                "instrument_type": "contract",
                "procurement_method": r.get("selection_method_description", ""),
                "solicitation_procedure": r.get("type_of_notice_description", ""),
                "commodity": {},
                "value": float(r.get("contract_amount")) if r.get("contract_amount") else None,
                "currency": "USD",
                "value_detail": {"amount": float(r.get("contract_amount"))} if r.get("contract_amount") else {},
                "dates": {
                    "published": award_date,
                    "start": start_date,
                    "end": end_date
                },
                "related": {
                    "document_links": r.get("document_links")
                }
            },
            "buyer": {
                "name": r.get("agency_name", "City of New York"),
                "country": "US",
                "type": "city",
                "identifiers": {},
                "address": {
                    "line1": r.get("street_address_1"),
                    "city": r.get("city"),
                    "region": r.get("state"),
                    "postal_code": r.get("zip_code"),
                    "country": "US"
                },
                "contact": {
                    "name": r.get("contact_name"),
                    "phone": r.get("contact_phone"),
                    "email": r.get("email"),
                }
            },
            "vendor": {
                "name": r.get("vendor_name", ""),
                "country": "CA",
                "country_basis": "vendor_address field contains CANADA",
                "identifiers": {},
                "address": {
                    "line1": r.get("vendor_address")
                },
                "contact": {}
            },
            "raw": r,
            "link": "https://data.cityofnewyork.us/resource/qyyg-4tf5.json?request_id=" + r.get("request_id", ""),
            "link_type": "dataset"
        }
        records.append(rec)

    with open(out, "w") as f:
        for r in records:
            f.write(json.dumps(r) + "\n")
    print(f"Got {len(records)} records")

if __name__ == "__main__":
    process()
