import urllib.parse
import urllib.request
import json
import gzip
import os
import sys

def fetch_dataset(resource_id):
    base_url = f"https://data.ny.gov/resource/{resource_id}.json"

    # Filter for Canadian vendors
    where_clause = "upper(vendor_country) = 'CAN' OR upper(vendor_country) = 'CANADA' OR upper(vendor_country) = 'CA' OR upper(vendor_country) = 'ONTARIO, CANADA'"

    query_params = {
        "$where": where_clause,
        "$limit": 50000,
    }

    url = f"{base_url}?{urllib.parse.urlencode(query_params)}"
    print(f"Fetching from: {url}")

    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    with urllib.request.urlopen(req) as response:
        data = json.loads(response.read())

    print(f"Fetched {len(data)} records")
    return data

def main():
    datasets = {
        "state_authorities": "ehig-g5x3",
        "local_authorities": "8w5p-k45m",
        "local_development_corps": "d84c-dk28",
        "industrial_development_agencies": "p3p6-xqr5"
    }

    all_data = []
    for key, resource_id in datasets.items():
        print(f"Fetching {key}...")
        data = fetch_dataset(resource_id)
        for row in data:
            row["_source_dataset"] = key
        all_data.extend(data)

    print(f"Total fetched: {len(all_data)}")
    with open("raw.json", "w") as f:
        json.dump(all_data, f)

if __name__ == "__main__":
    main()
