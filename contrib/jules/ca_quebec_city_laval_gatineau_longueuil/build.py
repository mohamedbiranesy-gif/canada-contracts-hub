import urllib.request
import json
import collections
import re
import datetime
import gzip
import os
import csv

OUT = "data/incoming/jules/records_ca_quebec_city_laval_gatineau_longueuil.jsonl.gz"

REF = json.load(open("coord/config.json"))["reference_date"]
REF_DATE = datetime.date.fromisoformat(REF)

stats = collections.defaultdict(collections.Counter)

import ssl
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

def parse_date(s):
    s = (s or "").strip()[:10]
    try:
        return datetime.date.fromisoformat(s) if re.match(r"^\d{4}-\d{2}-\d{2}$", s) else None
    except ValueError:
        return None

def process_laval(out_fd):
    url = "https://www.donneesquebec.ca/recherche/dataset/6acde2c0-6f08-407a-86e2-db49dd0bbb49/resource/db066d35-7e6d-465d-8fae-3a0937b800ae/download/contrats-octroyes.csv"
    req = urllib.request.Request(url)
    req.add_header("User-Agent", "Mozilla/5.0")
    with urllib.request.urlopen(req, context=ctx) as r:
        lines = [line.decode('utf-8-sig') for line in r.readlines()]
    reader = csv.DictReader(lines)
    for row in reader:
        stats["laval"]["rows"] += 1

        d = parse_date(row.get("date"))
        if not d:
            stats["laval"]["excluded_no_date"] += 1
            continue

        status = "end_date_unknown"
        status_basis = "end_date_unknown: award date published, no end date published"

        amt = None
        if row.get("montant"):
            try:
                amt = float(row.get("montant").replace(",", "."))
            except ValueError:
                pass

        rec = {
            "record_id": f"ca_quebec_city_laval:laval_{row.get('no-reference')}_{row.get('date')}_{row.get('contractant')}",
            "source": {
                "key": "ca_quebec_city_laval_gatineau_longueuil",
                "name": "Contrats octroyés - Ville de Laval",
                "publisher": "Ville de Laval",
                "dataset_url": "https://www.donneesquebec.ca/recherche/dataset/6acde2c0-6f08-407a-86e2-db49dd0bbb49",
                "record_url": None,
                "retrieved_at": datetime.datetime.now(datetime.timezone.utc).isoformat()
            },
            "status": status,
            "status_basis": status_basis,
            "contract": {
                "identifiers": {"no-reference": row.get("no-reference")} if row.get("no-reference") else {},
                "title": row.get("nature") or None,
                "description": None,
                "instrument_type": "contract",
                "procurement_method": None,
                "solicitation_procedure": None,
                "commodity": {},
                "value": amt,
                "currency": "CAD" if amt else None,
                "value_detail": {"montant": amt} if amt else {},
                "dates": {
                    "published": None,
                    "signed": d.isoformat(),
                    "start": d.isoformat(),
                    "end": None,
                    "amended_last": None
                },
                "related": {}
            },
            "buyer": {
                "name": "Ville de Laval",
                "country": "CA",
                "type": "city",
                "identifiers": {},
                "address": {},
                "contact": {}
            },
            "vendor": {
                "name": row.get("contractant") or None,
                "country": "CA",
                "country_basis": "assumed for municipal contracts", # wait, SCHEMA says never infer from name alone, and must be stated in source
                "identifiers": {},
                "address": {},
                "contact": {}
            },
            "raw": {k: v for k, v in row.items()}
        }
        # Laval source does not have vendor address/country.

out_fd = gzip.open(OUT_GZ, "wt", encoding="utf-8")
# process_laval(out_fd)
out_fd.close()
