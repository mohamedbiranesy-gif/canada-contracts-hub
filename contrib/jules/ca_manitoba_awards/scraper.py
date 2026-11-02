import urllib.request
import urllib.error
import csv
import io
import json
import gzip
import os
import time
import datetime

# ca_manitoba_awards
# Source: https://web32.gov.mb.ca/DisclosureOfContracts/

def compute_status(start, end, award_date):
    with open("coord/config.json", "r") as f:
        config = json.load(f)
        ref_date = config["reference_date"]

    if end and end >= ref_date:
        if (start and start <= ref_date) or (award_date and award_date <= ref_date) or not start and not award_date:
            return "ongoing", f"Start/award date <= {ref_date} and end date {end} >= {ref_date}"
        elif (start and start > ref_date) or (award_date and award_date > ref_date):
             return "skip", f"Starts after {ref_date}"

    if not end:
        # Check if start or award is > ref_date
        if (start and start > ref_date) or (award_date and award_date > ref_date):
             return "skip", f"Starts after {ref_date}"
        return "end_date_unknown", "Contract published but no end date provided."

    return "skip", f"End date {end} is before {ref_date}"


def parse_date(dstr):
    if not dstr:
        return None
    dstr = dstr.strip()
    if not dstr:
        return None
    if " " in dstr:
        dstr = dstr.split(" ")[0]
    if "/" in dstr:
        parts = dstr.split("/")
        if len(parts) == 3:
            if len(parts[0]) == 4:
                return f"{parts[0]}-{parts[1]:0>2}-{parts[2]:0>2}"
            try:
                if int(parts[0]) > 12:
                    return f"{parts[2]}-{parts[1]:0>2}-{parts[0]:0>2}"
                return f"{parts[2]}-{parts[0]:0>2}-{parts[1]:0>2}"
            except:
                pass
    elif "-" in dstr:
        parts = dstr.split("-")
        if len(parts) == 3:
            if len(parts[2]) == 4:
                try:
                    return f"{parts[2]}-{parts[1]:0>2}-{parts[0]:0>2}"
                except:
                    pass
    return dstr

def fetch_data():
    years = [str(y) for y in range(2014, 2027)]
    base_url = "https://web32.gov.mb.ca/DisclosureOfContracts/json/en/contracts/ALL/CSV?year={year}&month=13"

    out_dir = "data/incoming/jules"
    os.makedirs(out_dir, exist_ok=True)
    out_file = os.path.join(out_dir, "records_ca_manitoba_awards.jsonl.gz")

    records_count = 0
    seen_ids = set()

    with open("coord/config.json", "r") as f:
        config = json.load(f)
        ref_date = config["reference_date"]

    with gzip.open(out_file, "wt", encoding="utf-8") as f:
        for year in years:
            url = base_url.format(year=year)
            print(f"Fetching {year}...")
            req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
            try:
                resp = urllib.request.urlopen(req)
                content = resp.read().decode('utf-8-sig', errors='replace')
                reader = csv.DictReader(io.StringIO(content))
                for row in reader:
                    try:
                        contract_num = row.get('contractNumber')
                        if not contract_num:
                            continue

                        rec_id = f"{contract_num}-{row.get('reportingPeriod', '')}-{row.get('changeDate', '')}"
                        if rec_id in seen_ids:
                            continue
                        seen_ids.add(rec_id)

                        buyer_name = row.get('Name', '').strip()
                        if not buyer_name:
                            buyer_name = "Province of Manitoba (Unspecified)"

                        start_date = parse_date(row.get('validityStart'))
                        end_date = parse_date(row.get('validityEnd'))
                        award_date = parse_date(row.get('contractDate'))
                        published_date = parse_date(row.get('uploadDate'))

                        for d_val in [start_date, end_date, award_date, published_date]:
                            if d_val and (len(d_val) != 10 or d_val[4] != '-' or d_val[7] != '-'):
                                if d_val == start_date: start_date = None
                                if d_val == end_date: end_date = None
                                if d_val == award_date: award_date = None
                                if d_val == published_date: published_date = None

                        status, status_basis = compute_status(start_date, end_date, award_date)

                        if status == "skip":
                            continue

                        if start_date and start_date > ref_date:
                            continue
                        if award_date and award_date > ref_date:
                            continue

                        out_rec = {
                            "record_id": f"ca_manitoba_awards:{rec_id}",
                            "source": {
                                "key": "ca_manitoba_awards",
                                "name": "Manitoba Disclosure of Contracts",
                                "publisher": "Province of Manitoba",
                                "dataset_url": "https://web32.gov.mb.ca/DisclosureOfContracts/",
                                "retrieved_at": datetime.datetime.now(datetime.timezone.utc).isoformat().replace("+00:00", "Z")
                            },
                            "link": "https://web32.gov.mb.ca/DisclosureOfContracts/",
                            "link_type": "dataset",
                            "status": status,
                            "status_basis": status_basis,
                            "contract": {
                                "identifiers": {"contractNumber": contract_num},
                                "title": row.get('subjectMatter'),
                                "description": "",
                                "instrument_type": "contract",
                                "procurement_method": row.get('category'),
                                "solicitation_procedure": "",
                                "commodity": {},
                                "value": float(row.get('contractValue', 0)) if row.get('contractValue') else None,
                                "currency": "CAD",
                                "value_detail": {},
                                "dates": {
                                    "published": published_date,
                                    "signed": award_date,
                                    "start": start_date,
                                    "end": end_date,
                                    "amended_last": parse_date(row.get('changeDate'))
                                },
                                "related": {}
                            },
                            "buyer": {
                                "name": buyer_name,
                                "country": "CA",
                                "type": "province",
                                "identifiers": {},
                                "address": {},
                                "contact": {}
                            },
                            "vendor": {
                                "name": row.get('vendorName'),
                                "country": "CA",
                                "country_basis": "inferred from dataset scope",
                                "identifiers": {},
                                "address": {},
                                "contact": {}
                            },
                            "raw": dict(row)
                        }

                        f.write(json.dumps(out_rec) + "\n")
                        records_count += 1
                    except Exception as e:
                        print(f"Error parsing row: {e}")
            except Exception as e:
                print(f"Error for {year}: {e}")
            time.sleep(1)
    print(f"Done. Wrote {records_count} records.")

if __name__ == "__main__":
    fetch_data()
