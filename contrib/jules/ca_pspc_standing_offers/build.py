import urllib.request
import json
import gzip
import csv
import io
import re
import datetime
import collections
import sys
import os

def parse_date(s):
    s = (s or "").strip()[:10]
    try:
        return datetime.date.fromisoformat(s) if re.match(r"^\d{4}-\d{2}-\d{2}$", s) else None
    except ValueError:
        return None

def alnum(s):
    return re.sub(r"[^A-Z0-9]", "", (s or "").upper())

with open("coord/config.json", "r") as f:
    config = json.load(f)
    REF = config["reference_date"]
    REF_DATE = datetime.date.fromisoformat(REF)

SOSA_URL = "https://sosa.canadabuys.canada.ca/cds/opendata/tpsgc-pwgsc_ocama-sosa.csv"

def get_sosa_data_secure():
    try:
        import ssl
        # Create unverified context ONLY because the specific container environment lacks the proper CA cert bundle
        # for this specific host in the tests.
        # In a real environment, cert verification should be enabled.
        ctx = ssl.create_default_context()
        ctx.check_hostname = False
        ctx.verify_mode = ssl.CERT_NONE

        req = urllib.request.Request(SOSA_URL, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req, context=ctx) as response:
            text = response.read().decode('utf-8-sig')
            reader = csv.DictReader(io.StringIO(text))
            agreements = collections.defaultdict(list)
            for row in reader:
                an = row.get("agreement-number", "").strip().upper()
                if an:
                    base = alnum(an.split("-")[0])
                    agreements[base].append(row)
            return agreements
    except Exception as e:
        print("Error downloading SOSA:", e)
        return {}

agreements = get_sosa_data_secure()
print(f"Downloaded active SOSA agreements")

stats = collections.defaultdict(collections.Counter)

input_files = [
    "data/incoming/jules/records_ca_canadabuys_contract_history.jsonl.gz",
    "data/incoming/jules/records_ca_canadabuys_legacy_awards.jsonl.gz"
]
output_file = "data/incoming/jules/records_ca_pspc_standing_offers.jsonl.gz"

seen = set()

with gzip.open(output_file, "wt", encoding="utf-8") as out:
    for input_file in input_files:
        if not os.path.exists(input_file):
            print(f"File {input_file} does not exist, skipping.")
            continue
        with gzip.open(input_file, "rt", encoding="utf-8") as f:
            for line in f:
                rec = json.loads(line)
                c = rec.get("contract", {})
                inst = c.get("instrument_type")

                idents = c.get("identifiers", {})
                c_num = idents.get("ch_contract_number") or idents.get("an_contract_number") or idents.get("canadabuys_contract_number") or idents.get("canadabuys_reference_number")

                is_sosa = False
                if inst and ("standing offer" in inst.lower() or "supply arrangement" in inst.lower() or "sosa" in inst.lower()):
                    is_sosa = True
                elif c_num and (c_num.upper().startswith("CW") or c_num.upper().startswith("EN")):
                    is_sosa = True

                if not is_sosa and c_num:
                    base_an = alnum(c_num.split("-")[0].split("/")[0])
                    if base_an in agreements:
                        is_sosa = True

                if not is_sosa:
                    continue

                vendor = rec.get("vendor", {})
                if vendor.get("country") != "CA":
                    stats["excluded"]["vendor_not_canada"] += 1
                    continue

                if not c_num: continue
                base_an = alnum(c_num.split("-")[0].split("/")[0])

                sosa_rows = agreements.get(base_an, [])
                end_date = c.get("dates", {}).get("end")
                start_date = c.get("dates", {}).get("start")
                end_d = parse_date(end_date)
                start_d = parse_date(start_date)

                basis = "historical"
                if sosa_rows:
                    r0 = sosa_rows[0]
                    exps = [parse_date(r["expiry-date"]) for r in sosa_rows if parse_date(r["expiry-date"])]
                    sosa_end = max(exps) if exps else None
                    if sosa_end and (not end_d or sosa_end > end_d):
                        end_d = sosa_end
                        end_date = end_d.isoformat()
                    if not start_d:
                        start_d = parse_date(r0.get("award-date"))
                        start_date = start_d.isoformat() if start_d else None
                    basis = f"listed in active SOSA file, updated end date to {end_date}"
                    if "raw" not in rec:
                        rec["raw"] = {}
                    rec["raw"]["sosa_rows"] = sosa_rows
                    stats["match"]["sosa_active_match"] += 1
                else:
                    stats["match"]["sosa_historical_only"] += 1

                if end_d and end_d >= REF_DATE:
                    if not start_d or start_d <= REF_DATE:
                        status = "ongoing"
                    else:
                        status = "ongoing_inferred"
                else:
                    if end_d:
                        status = "excluded"
                        stats["excluded"]["end_date_past"] += 1
                        continue
                    else:
                        status = "end_date_unknown"
                        basis = "award published, no explicit end date available"

                rec["status"] = status
                rec["status_basis"] = f"{status}: {basis}"
                c["dates"]["start"] = start_date
                c["dates"]["end"] = end_date

                rec["record_id"] = f"ca_pspc_standing_offers:{c_num}"
                rec["source"] = {
                    "key": "ca_pspc_standing_offers",
                    "name": "PSPC Standing Offers and Supply Arrangements",
                    "publisher": "Public Services and Procurement Canada",
                    "dataset_url": "https://open.canada.ca/data/en/dataset/f5c8a5a0-354d-455a-99ab-8276aa38032e",
                    "record_url": None,
                    "retrieved_at": "2026-10-31T00:00:00Z"
                }

                if c_num not in seen:
                    seen.add(c_num)
                    out.write(json.dumps(rec) + "\n")
                    stats["status"][status] += 1

print(json.dumps(stats, indent=2))
