#!/usr/bin/env python3
"""Build normalized/ca_quebec_city_laval_gatineau_longueuil.jsonl from Données Québec API:
Laval and Longueuil contract lists.

Usage: python3 build.py <out.jsonl.gz>
"""
import os
import sys
import json
import gzip
import httpx
import pandas as pd
from datetime import datetime, timezone
from io import StringIO

REF_DATE = json.load(open('coord/config.json'))['reference_date']
SOURCE_KEY = "ca_quebec_city_laval_gatineau_longueuil"
DATASET_URL_LAVAL = "https://www.donneesquebec.ca/recherche/dataset/6acde2c0-6f08-407a-86e2-db49dd0bbb49"
RESOURCE_URL_LAVAL = "https://www.donneesquebec.ca/recherche/dataset/6acde2c0-6f08-407a-86e2-db49dd0bbb49/resource/db066d35-7e6d-465d-8fae-3a0937b800ae/download/contrats-octroyes.csv"

DATASET_URL_LONGUEUIL = "https://www.donneesquebec.ca/recherche/dataset/96c41f45-6f76-4cc2-a6a8-98299fe26cd6"
RESOURCE_URL_LONGUEUIL = "https://www.donneesquebec.ca/recherche/dataset/96c41f45-6f76-4cc2-a6a8-98299fe26cd6/resource/121492e6-afa7-4e3c-afa0-aa8bacc33879/download/ententes25k.csv"

def parse_date(d):
    d = str(d or "").strip()[:10]
    if len(d) == 10 and d[4] == '-' and d[7] == '-':
        return d
    if len(d) == 10 and d[2] == '/' and d[5] == '/':
        return f"{d[6:10]}-{d[3:5]}-{d[0:2]}"
    d_clean = str(d or "").strip()
    if len(d_clean) >= 14 and d_clean.isdigit():
        return f"{d_clean[0:4]}-{d_clean[4:6]}-{d_clean[6:8]}"
    return ""

def to_num(s):
    try:
        return float((str(s) or "").replace(",", ".").replace("$", "").replace(" ", "").strip())
    except Exception:
        return None

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 build.py <out.jsonl.gz>")
        sys.exit(1)

    out_path = sys.argv[1]

    # We use a fixed date for the test to avoid deprecation warnings
    # retrieved_at = datetime.utcnow().isoformat() + "Z"
    retrieved_at = datetime.now(timezone.utc).isoformat().replace("+00:00", "Z")

    records = []

    # Process Laval
    try:
        r_laval = httpx.get(RESOURCE_URL_LAVAL, timeout=30.0)
        r_laval.raise_for_status()
        content_laval = r_laval.content.decode('utf-8-sig', errors='ignore')
        df_laval = pd.read_csv(StringIO(content_laval), sep=',', dtype=str)

        for idx, row in df_laval.iterrows():
            row_dict = row.to_dict()
            vendor_name = (row_dict.get('contractant') or "").strip()
            if not vendor_name:
                continue

            val = to_num(row_dict.get('montant'))

            rec = {
                "record_id": f"{SOURCE_KEY}:laval:{idx}",
                "source": {
                    "key": SOURCE_KEY,
                    "name": "Ville de Laval - Contrats octroyés",
                    "publisher": "Ville de Laval",
                    "dataset_url": DATASET_URL_LAVAL,
                    "record_url": DATASET_URL_LAVAL,
                    "retrieved_at": retrieved_at
                },
                "status": "end_date_unknown",
                "status_basis": "award/contract published without end date",
                "contract": {
                    "identifiers": {"no-reference": row_dict.get("no-reference")} if row_dict.get("no-reference") else {},
                    "title": row_dict.get("nature", ""),
                    "description": "",
                    "instrument_type": "contract",
                    "procurement_method": "",
                    "solicitation_procedure": "",
                    "commodity": {},
                    "value": val,
                    "currency": "CAD",
                    "value_detail": {},
                    "dates": {
                        "published": parse_date(row_dict.get("date", "")),
                        "signed": "",
                        "start": "",
                        "end": "",
                        "amended_last": ""
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
                    "name": vendor_name,
                    "country": "CA",
                    "country_basis": "not published",
                    "identifiers": {},
                    "address": {},
                    "contact": {}
                },
                "link": DATASET_URL_LAVAL,
                "raw": row_dict
            }
            records.append(rec)

    except Exception as e:
        print(f"Error fetching Laval: {e}")

    # Process Longueuil
    try:
        r_long = httpx.get(RESOURCE_URL_LONGUEUIL, timeout=30.0)
        r_long.raise_for_status()
        content_long = r_long.content.decode('utf-8-sig', errors='ignore')
        df_long = pd.read_csv(StringIO(content_long), sep=',', dtype=str, engine='python', on_bad_lines='skip')
        # Fix trailing column
        cols = list(df_long.columns)
        if cols and cols[-1].endswith(';;;'):
            df_long = df_long.rename(columns={cols[-1]: cols[-1].replace(';;;', '')})

        for idx, row in df_long.iterrows():
            row_dict = row.to_dict()
            # The last value might have ';;;' appended
            for k, v in row_dict.items():
                if isinstance(v, str) and v.endswith(';;;'):
                    row_dict[k] = v.replace(';;;', '')

            vendor_name = str(row_dict.get('NOM_FOURNISSEUR') or "").strip()
            if not vendor_name or vendor_name == "nan":
                continue

            val = to_num(row_dict.get('MONTANT_INITIAL'))

            rec = {
                "record_id": f"{SOURCE_KEY}:longueuil:{row_dict.get('NUMERO_ENTENTE', idx)}",
                "source": {
                    "key": SOURCE_KEY,
                    "name": "Ville de Longueuil - Ententes de 25 000 $ et plus",
                    "publisher": "Ville de Longueuil",
                    "dataset_url": DATASET_URL_LONGUEUIL,
                    "record_url": DATASET_URL_LONGUEUIL,
                    "retrieved_at": retrieved_at
                },
                "status": "end_date_unknown",
                "status_basis": "award/contract published without end date",
                "contract": {
                    "identifiers": {
                        "NUMERO_ENTENTE": row_dict.get("NUMERO_ENTENTE"),
                        "NUMERO_APPEL": row_dict.get("NUMERO_APPEL")
                    },
                    "title": row_dict.get("DESCRIPTION_ENTENTE", ""),
                    "description": "",
                    "instrument_type": row_dict.get("TYPE_ENTENTE", "contract"),
                    "procurement_method": "",
                    "solicitation_procedure": "",
                    "commodity": {},
                    "value": val,
                    "currency": "CAD",
                    "value_detail": {
                        "MONTANT_DEPENSE": to_num(row_dict.get("MONTANT_DEPENSE")),
                        "MONTANT_RESTANT": to_num(row_dict.get("MONTANT_RESTANT"))
                    },
                    "dates": {
                        "published": parse_date(row_dict.get("DATE_CREATION", "")),
                        "signed": "",
                        "start": parse_date(row_dict.get("DATE_DEBUT", "")),
                        "end": parse_date(row_dict.get("DATE_FERMETURE", "")),
                        "amended_last": ""
                    },
                    "related": {}
                },
                "buyer": {
                    "name": "Ville de Longueuil",
                    "country": "CA",
                    "type": "city",
                    "identifiers": {},
                    "address": {},
                    "contact": {}
                },
                "vendor": {
                    "name": vendor_name,
                    "country": "CA",
                    "country_basis": "not published",
                    "identifiers": {},
                    "address": {},
                    "contact": {}
                },
                "link": DATASET_URL_LONGUEUIL,
                "raw": row_dict
            }

            # Since Longueuil provides start and end dates, we can calculate status better!
            start = rec["contract"]["dates"]["start"]
            end = rec["contract"]["dates"]["end"]

            if start and end:
                try:
                    s_date = start[:10]
                    e_date = end[:10]
                    if s_date <= REF_DATE and e_date >= REF_DATE:
                        rec["status"] = "ongoing"
                        rec["status_basis"] = "start <= ref_date and end >= ref_date"
                    else:
                        if e_date < REF_DATE:
                            continue # skip
                        else:
                            rec["status"] = "ongoing"
                            rec["status_basis"] = "future end date"
                except Exception:
                    pass

            records.append(rec)

    except Exception as e:
        print(f"Error fetching Longueuil: {e}")

    # write to gzip jsonl
    with gzip.open(out_path, 'wt', encoding='utf-8') as f:
        for r in records:
            f.write(json.dumps(r, ensure_ascii=False) + '\n')

    print(f"Wrote {len(records)} records.")

if __name__ == '__main__':
    main()
