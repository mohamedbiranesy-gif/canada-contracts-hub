import urllib.request
import urllib.parse
import json
import gzip
import datetime
from datetime import datetime as dt, timezone
import time
import os

def load_config():
    with open('coord/config.json') as f:
        return json.load(f)

config = load_config()
ref_date_str = config['reference_date']
ref_date = dt.strptime(ref_date_str, '%Y-%m-%d').date()

def is_ongoing(start, end, ref_date):
    if not start and not end:
        return 'end_date_unknown', 'No start or end date provided.'

    start_d = None
    if start:
        start_d = dt.strptime(start[:10], '%Y-%m-%d').date()

    end_d = None
    if end:
        end_d = dt.strptime(end[:10], '%Y-%m-%d').date()

    if not end_d:
        if start_d and start_d <= ref_date:
            return 'end_date_unknown', 'No end date provided, but started on or before reference date.'
        else:
            return 'end_date_unknown', 'No end date provided, and started after reference date.'

    if start_d:
        if start_d <= ref_date and end_d >= ref_date:
            return 'ongoing', f'Start date ({start_d}) <= reference date and end date ({end_d}) >= reference date.'
    else:
        if end_d >= ref_date:
            return 'ongoing', f'End date ({end_d}) >= reference date.'

    return None, None

def fetch_page(page, limit=100):
    url = "https://api.usaspending.gov/api/v2/search/spending_by_award/"
    payload = {
        "filters": {
            "award_type_codes": ["A", "B", "C", "D"], # prime contract types, subawards will be matched with subawards=True
            "recipient_locations": [{"country": "CAN"}],
            "time_period": [{"start_date": "2007-10-01", "end_date": ref_date_str}]
        },
        "fields": [
            "Sub-Award ID",
            "Sub-Awardee Name",
            "Sub-Award Date",
            "Sub-Award Amount",
            "Awarding Agency",
            "Awarding Sub Agency",
            "Prime Award ID",
            "Prime Recipient Name",
            "Sub-Award Description",
            "generated_internal_id",
            "prime_award_internal_id"
        ],
        "page": page,
        "limit": limit,
        "sort": "Sub-Award ID",
        "order": "desc",
        "subawards": True
    }

    req = urllib.request.Request(url, data=json.dumps(payload).encode('utf-8'), headers={'User-Agent': 'contracts-research/1.0', 'Content-Type': 'application/json'})
    print(f"Fetching page {page}")
    try:
        with urllib.request.urlopen(req) as response:
            return json.loads(response.read().decode('utf-8'))
    except urllib.error.HTTPError as e:
        print(f"Error fetching page {page}: HTTP {e.code}")
        print(e.read().decode('utf-8'))
        return None
    except Exception as e:
        print(f"Error fetching page {page}: {e}")
        return None

records = []
page = 1
limit = 100
seen_ids = set()

while True:
    data = fetch_page(page, limit)
    if not data or not data.get('results'):
        break

    results = data['results']
    print(f"Found {len(results)} records on page {page}")

    for row in results:
        start = row.get('Sub-Award Date')
        end = None # subawards usually only have an action date. Let's see.

        status, status_basis = is_ongoing(start, end, ref_date)
        if not status:
            continue

        award_id = row.get('Sub-Award ID') or row.get('internal_id')
        if not award_id:
            continue

        record_id = f"us_usaspending_subawards:{award_id}".replace(' ', '_').lower()
        if record_id in seen_ids:
            continue
        seen_ids.add(record_id)

        record = {
            "record_id": record_id,
            "source": {
                "key": "us_usaspending_subawards",
                "name": "USAspending sub-awards",
                "publisher": "US Federal Government",
                "dataset_url": "https://www.usaspending.gov/search",
                "record_url": f"https://www.usaspending.gov/award/{row.get('prime_award_internal_id')}" if row.get('prime_award_internal_id') else None,
                "retrieved_at": dt.now(timezone.utc).isoformat().replace('+00:00', 'Z')
            },
            "status": status,
            "status_basis": status_basis,
            "contract": {
                "identifiers": {"Sub-Award ID": award_id, "Prime Award ID": row.get('Prime Award ID', '')},
                "title": row.get('Sub-Award Description', ''),
                "description": row.get('Sub-Award Description', ''),
                "instrument_type": "subcontract",
                "procurement_method": "",
                "solicitation_procedure": "",
                "commodity": {},
                "value": row.get('Sub-Award Amount'),
                "currency": "USD",
                "value_detail": {},
                "dates": {
                    "published": "",
                    "signed": "",
                    "start": start[:10] if start else "",
                    "end": end[:10] if end else "",
                    "amended_last": ""
                },
                "related": {}
            },
            "buyer": {
                "name": row.get('Awarding Agency', '') + (" - " + row.get('Awarding Sub Agency') if row.get('Awarding Sub Agency') else ""),
                "country": "US",
                "type": "federal dept",
                "identifiers": {},
                "address": {},
                "contact": {}
            },
            "vendor": {
                "name": row.get('Sub-Awardee Name', ''),
                "country": "CA",
                "country_basis": "recipient_locations=CAN API filter",
                "identifiers": {},
                "address": {
                    "line1": "",
                    "city": "",
                    "region": "",
                    "postal_code": "",
                    "country": "CA"
                },
                "contact": {}
            },
            "raw": row,
            "link": f"https://www.usaspending.gov/award/{row.get('prime_award_internal_id')}" if row.get('prime_award_internal_id') else "https://www.usaspending.gov",
            "link_type": "notice"
        }
        records.append(record)

    if len(results) < limit:
        break

    page += 1
    time.sleep(1)

out_file = "data/incoming/jules/records_us_usaspending_subawards.jsonl.gz"
os.makedirs(os.path.dirname(out_file), exist_ok=True)
with gzip.open(out_file, "wt", encoding="utf-8") as f:
    for record in records:
        f.write(json.dumps(record, ensure_ascii=False) + '\n')

print(f"Wrote {len(records)} records to {out_file}")
