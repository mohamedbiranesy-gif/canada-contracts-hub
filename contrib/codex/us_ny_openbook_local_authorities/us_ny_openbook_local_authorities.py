import urllib.request, json, time, sys, gzip, os, hashlib
from datetime import datetime, timezone

out_file = sys.argv[1] if len(sys.argv) > 1 else "data/incoming/codex/records_us_ny_openbook_local_authorities.jsonl.gz"
os.makedirs(os.path.dirname(out_file), exist_ok=True)

with open("coord/config.json") as f:
    REF_DATE = json.load(f)["reference_date"]

DATASETS = [
    ("8w5p-k45m", "Procurement Report for Local Authorities"),
    ("d84c-dk28", "Procurement Report for Local Development Corporations"),
    ("p3p6-xqr5", "Procurement Report for Industrial Development Agencies")
]

import urllib.parse
with gzip.open(out_file, "wt") as f:
    for ds_id, ds_name in DATASETS:
        limit = 1000
        offset = 0
        seen_ids = set()
        while True:
            p = urllib.parse.urlencode({
                "$where": "upper(`vendor_country`) in ('CAN', 'CANADA') OR upper(`vendor_country`) like '%CANADA%'",
                "$limit": limit,
                "$offset": offset
            })
            u = f'https://data.ny.gov/resource/{ds_id}.json?{p}'
            try:
                req = urllib.request.Request(u, headers={"User-Agent": "contracts-research/1.0"})
                data = json.loads(urllib.request.urlopen(req).read())
            except Exception as e:
                break

            if not data:
                break

            for row in data:
                start = row.get("begin_date") or row.get("award_date")
                end = row.get("end_date")

                status = "ongoing"
                status_basis = "start <= ref and end >= ref"
                if end and end[:10] < REF_DATE:
                    continue
                elif not end:
                    status = "end_date_unknown"
                    status_basis = "award published, no end date"

                val = row.get("contract_amount")
                if val:
                    val = val.replace("$", "").replace(",", "")
                    try:
                        val = float(val)
                    except:
                        val = None

                uid = hashlib.md5(f"{ds_id}:{row.get('authority_name')}:{row.get('vendor_name')}:{row.get('procurement_description')}:{val}".encode()).hexdigest()

                if uid in seen_ids:
                    continue
                seen_ids.add(uid)

                rec = {
                    "record_id": f"us_ny_openbook_local_authorities:{uid}",
                    "source": {
                        "key": "us_ny_openbook_local_authorities",
                        "name": ds_name,
                        "publisher": "New York State",
                        "dataset_url": f"https://data.ny.gov/d/{ds_id}",
                        "record_url": f"https://data.ny.gov/d/{ds_id}",
                        "retrieved_at": datetime.now(timezone.utc).isoformat()
                    },
                    "status": status,
                    "status_basis": status_basis,
                    "contract": {
                        "title": row.get("procurement_description") or "Unknown",
                        "description": row.get("procurement_description"),
                        "instrument_type": row.get("type_of_procurement"),
                        "procurement_method": row.get("award_process"),
                        "value": val,
                        "currency": "USD" if val else None,
                        "dates": {
                            "start": start[:10] if start else None,
                            "end": end[:10] if end else None,
                            "published": row.get("award_date")[:10] if row.get("award_date") else None,
                            "signed": row.get("award_date")[:10] if row.get("award_date") else None
                        }
                    },
                    "buyer": {
                        "name": row.get("authority_name") or "Unknown",
                        "country": "US",
                        "type": "authority"
                    },
                    "vendor": {
                        "name": row.get("vendor_name") or "Unknown",
                        "country": "CA",
                        "country_basis": "vendor_country",
                        "address": {
                            "line1": row.get("vendor_address_1"),
                            "city": row.get("vendor_city"),
                            "region": row.get("vendor_province_region") or row.get("vendor_state"),
                            "postal_code": row.get("vendor_postal_code"),
                            "country": "CA"
                        }
                    },
                    "raw": row,
                    "link": f"https://data.ny.gov/d/{ds_id}",
                    "link_type": "dataset"
                }
                f.write(json.dumps(rec) + "\n")

            offset += limit
