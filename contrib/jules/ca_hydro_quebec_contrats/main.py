import urllib.request
import ssl
import json
import csv
import gzip
import datetime
from io import StringIO
from collections import defaultdict
import os

# Create default context that DOES verify certificates (more secure)
ctx = ssl.create_default_context()

url = "https://www.hydroquebec.com/soumissionnez/attribution/attribution.csv"

out_dir = "data/incoming/jules"
os.makedirs(out_dir, exist_ok=True)
out_path = os.path.join(out_dir, "records_ca_hydro_quebec_contrats.jsonl.gz")

stats = defaultdict(int)

def parse_date(dstr):
    if not dstr:
        return None
    dstr = dstr.strip()
    if len(dstr) == 8 and dstr.isdigit():
        return f"{dstr[:4]}-{dstr[4:6]}-{dstr[6:]}"
    return None

def main():
    print(f"Downloading from {url}...")
    req = urllib.request.Request(url, headers={'User-Agent': 'contracts-research/1.0'})
    with urllib.request.urlopen(req, context=ctx) as response:
        try:
            content = response.read().decode('utf-8-sig')
        except UnicodeDecodeError:
            content = response.read().decode('latin-1')

    reader = csv.DictReader(StringIO(content), delimiter=';')

    with gzip.open(out_path, "wt", encoding="utf-8") as outf:
        for i, row in enumerate(reader):
            stats['rows_seen'] += 1

            pays = (row.get("PAYS_FOURN") or "").strip()

            if pays.lower() != "canada":
                stats['excluded_non_canada'] += 1
                continue

            stats['rows_canadian'] += 1

            vname = (row.get("DV_CW_FOURN_NOM") or "").strip()
            if not vname:
                stats['excluded_no_vendor_name'] += 1
                continue

            raw_date = row.get("DATE_DE_CONCLUSION_DU_CONTRAT")
            iso_date = parse_date(raw_date)

            raw_amt = row.get("MONTANT")
            amt = None
            if raw_amt:
                try:
                    amt = float(raw_amt.strip())
                except ValueError:
                    pass

            record_id = f"ca_hydro_quebec_contrats:{row.get('APPEL_DE_PROPOSITION') or stats['rows_seen']}:{i}"

            rec = {
                "record_id": record_id,
                "source": {
                    "key": "ca_hydro_quebec_contrats",
                    "name": "Hydro-Québec contracts awarded",
                    "publisher": "Hydro-Québec",
                    "dataset_url": "https://www.hydroquebec.com/fournisseurs/soumissionner/attribution-des-contrats.html",
                    "record_url": None,
                    "retrieved_at": datetime.datetime.now(datetime.timezone.utc).isoformat()
                },
                "link": "https://www.hydroquebec.com/fournisseurs/soumissionner/attribution-des-contrats.html",
                "status": "end_date_unknown",
                "status_basis": "end_date_unknown: dataset publishes DATE_DE_CONCLUSION_DU_CONTRAT but no contract term or end date",
                "contract": {
                    "identifiers": {
                        "appel_de_proposition": row.get("APPEL_DE_PROPOSITION") or None
                    },
                    "title": (row.get("OBJET") or "").strip() or None,
                    "description": None,
                    "instrument_type": (row.get("TYPE_DE_CONTRAT") or "").strip() or None,
                    "procurement_method": None,
                    "solicitation_procedure": None,
                    "commodity": {},
                    "value": amt,
                    "currency": "CAD" if amt is not None else None,
                    "value_detail": {"MONTANT": amt} if amt is not None else {},
                    "dates": {
                        "published": None,
                        "signed": iso_date,
                        "start": None,
                        "end": None,
                        "amended_last": None
                    },
                    "related": {}
                },
                "buyer": {
                    "name": "Hydro-Québec",
                    "country": "CA",
                    "type": "provincial crown corporation",
                    "identifiers": {},
                    "address": {
                        "region": "QC",
                        "country": "CA"
                    },
                    "contact": {}
                },
                "vendor": {
                    "name": vname,
                    "country": "CA",
                    "country_basis": "PAYS_FOURN field",
                    "identifiers": {},
                    "address": {
                        "line1": (row.get("DI_CW_NOM_RUE") or "").strip() or None,
                        "city": (row.get("DI_CW_NOM_VILLE") or "").strip() or None,
                        "region": (row.get("PROVINCE") or "").strip() or None,
                        "postal_code": (row.get("DI_CW_CODE_POSTAL") or "").strip() or None,
                        "country": "CA"
                    },
                    "contact": {}
                },
                "raw": dict(row)
            }

            # Remove empty dict keys in identifiers
            rec["contract"]["identifiers"] = {k: v for k, v in rec["contract"]["identifiers"].items() if v}

            outf.write(json.dumps(rec, ensure_ascii=False) + "\n")
            stats['rows_output'] += 1

    print("\nStats:")
    for k, v in stats.items():
        print(f"  {k}: {v}")

if __name__ == "__main__":
    main()
