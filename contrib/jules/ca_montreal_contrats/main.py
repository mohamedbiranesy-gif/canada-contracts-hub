import urllib.request
import ssl
import json
import csv
import gzip
import re
import datetime
from io import StringIO
from collections import defaultdict

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

def clean_name(n):
    return (n or "").strip().upper()

def get_fournisseurs():
    url = "https://donnees.montreal.ca/dataset/3bda8899-279a-46fc-9ad9-8dee68d05def/resource/ceee5da3-56ba-40f4-9008-8678bf4c14fe/download/listefournisseurs.csv"
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    fournisseurs = {}
    with urllib.request.urlopen(req, context=ctx) as response:
        content = response.read().decode('utf-8', errors='replace')
        reader = csv.DictReader(StringIO(content))
        for row in reader:
            nom = clean_name(row.get("Nom_Fournisseur"))
            autre = clean_name(row.get("Autre_Nom"))
            pays = (row.get("Lieu_Pays") or "").strip()
            if nom and pays:
                fournisseurs[nom] = pays
            if autre and pays:
                fournisseurs[autre] = pays
    return fournisseurs

fournisseurs = get_fournisseurs()
print(f"Loaded {len(fournisseurs)} suppliers")

urls = {
    "fonctionnaires": "https://donnees.montreal.ca/dataset/0b7955a7-8523-4254-8f95-81a59684866d/resource/e4b758ab-3edb-4b6a-8764-2a443b6b9404/download/contratsfonctionnaires.csv",
    "comite_executif": "https://donnees.montreal.ca/dataset/72083af8-83f8-41c1-823b-1cae5e76ff9a/resource/4b2d8744-a257-4102-8897-95a30a20de34/download/contrats_comite_executif.csv",
    "arrondissement": "https://donnees.montreal.ca/dataset/60b9662a-17c3-42f0-9ff1-c39bc9026df2/resource/941c7e36-a831-4228-b737-21174c6a1864/download/contratsconseilsarrondissements.csv",
    "agglomeration": "https://donnees.montreal.ca/dataset/5cf0220b-c149-43c4-ac23-758c55648584/resource/7cf955d0-a3e6-4e94-8c24-9b0a4f7c0408/download/contrats_conseil_agglomeration.csv",
    "municipal": "https://donnees.montreal.ca/dataset/5cf0220b-c149-43c4-ac23-758c55648584/resource/1e5ab066-f560-4b4f-8f12-991de39df134/download/contrats_conseil_municipal.csv"
}

out_path = "data/incoming/jules/records_ca_montreal_contrats.jsonl.gz"
stats = defaultdict(int)

DATE_RE = re.compile(r'^\d{4}-\d{2}-\d{2}$')

def parse_date(dstr):
    if not dstr:
        return None
    dstr = dstr.strip()
    if DATE_RE.match(dstr):
        return dstr
    try:
        if "/" in dstr:
            parts = dstr.split("/")
            if len(parts) == 3:
                m, d, y = parts
                return f"{int(y):04d}-{int(m):02d}-{int(d):02d}"
    except Exception:
        pass
    return None

with gzip.open(out_path, "wt", encoding="utf-8") as outf:
    for name, url in urls.items():
        print(f"Processing {name}...")
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req, context=ctx) as response:
            content = response.read().decode('utf-8-sig', errors='replace')
            reader = csv.DictReader(StringIO(content))
            for i, row in enumerate(reader):
                stats['rows_seen'] += 1

                vname = row.get("NOM DU FOURNISSEUR") or row.get("FOURNISSEUR") or ""
                vname_clean = clean_name(vname)

                if not vname_clean:
                    stats['rows_missing_vendor'] += 1
                    continue

                pays = fournisseurs.get(vname_clean)
                if not pays:
                    stats['rows_vendor_not_in_registry'] += 1
                    continue

                if pays != "CA":
                    stats['rows_vendor_not_ca'] += 1
                    continue

                stats['rows_canadian'] += 1

                raw_date = row.get("DATE D'APPROBATION") or row.get("DATE SIGNATURE") or ""
                iso_date = parse_date(raw_date)

                raw_amt = row.get("MONTANT") or ""
                amt = None
                try:
                    raw_amt_clean = raw_amt.replace(" ", "").replace(",", ".").replace("$", "")
                    amt = float(raw_amt_clean)
                except ValueError:
                    pass

                num = row.get("NUMÉRO") or ""
                dossier = row.get("NO DE DOSSIER") or ""
                decision = row.get("NO DÉCISION") or ""

                # Make rid guaranteed unique
                rid = f"{name}-{i}"
                if num:
                    rid += f"-{num}"
                if dossier:
                    rid += f"-{dossier}"
                if decision:
                    rid += f"-{decision}"

                # URL max size is OK

                record_id = f"ca_montreal_contrats:{rid}"

                desc = row.get("DESCRIPTION") or row.get("OBJET") or None
                service = row.get("SERVICE") or ""

                rec = {
                    "record_id": record_id,
                    "source": {
                        "key": "ca_montreal_contrats",
                        "name": "Ville de Montréal contracts (open data)",
                        "publisher": "Ville de Montréal",
                        "dataset_url": "https://donnees.montreal.ca/search?q=contrats",
                        "record_url": None,
                        "retrieved_at": datetime.datetime.now(datetime.timezone.utc).isoformat()
                    },
                    "link": url,
                    "status": "end_date_unknown",
                    "status_basis": "end_date_unknown: dataset publishes award/signature date but no contract term or end date",
                    "contract": {
                        "identifiers": {
                            "numero": num if num else None,
                            "no_dossier": dossier if dossier else None,
                            "no_decision": decision if decision else None
                        },
                        "title": desc,
                        "description": f"Service: {service}" if service else None,
                        "instrument_type": None,
                        "procurement_method": None,
                        "solicitation_procedure": None,
                        "commodity": {},
                        "value": amt,
                        "currency": "CAD" if amt is not None else None,
                        "value_detail": {"amount": amt} if amt is not None else {},
                        "dates": {
                            "published": None,
                            "signed": iso_date,
                            "start": iso_date,
                            "end": None,
                            "amended_last": None
                        },
                        "related": {}
                    },
                    "buyer": {
                        "name": "Ville de Montréal",
                        "country": "CA",
                        "type": "city",
                        "identifiers": {},
                        "address": {
                            "city": "Montréal",
                            "region": "QC",
                            "country": "CA"
                        },
                        "contact": {}
                    },
                    "vendor": {
                        "name": vname,
                        "country": "CA",
                        "country_basis": "Montreal fournisseurs dataset Lieu_Pays field",
                        "identifiers": {},
                        "address": {},
                        "contact": {}
                    },
                    "raw": dict(row)
                }

                rec["contract"]["identifiers"] = {k: v for k, v in rec["contract"]["identifiers"].items() if v}

                outf.write(json.dumps(rec, ensure_ascii=False) + "\n")
                stats['rows_output'] += 1

print("\nStats:")
for k, v in stats.items():
    print(f"  {k}: {v}")
