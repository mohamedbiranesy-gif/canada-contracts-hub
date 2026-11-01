import urllib.request
import ssl
import json
import csv
import gzip
import datetime
import re
from io import StringIO
from collections import defaultdict
import os

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = "https://sosa.canadabuys.canada.ca/cds/opendata/tpsgc-pwgsc_ocama-sosa.csv"
url_cb = "https://canadabuys.canada.ca/opendata/pub/2009-2023-contractHistoryHistorical-contratsOctroyesHistorique.csv"
url_an = "https://canadabuys.canada.ca/opendata/pub/2012-2022-awardNoticeHistorical-avisAttributionHistorique.csv"

out_dir = "data/incoming/jules"
os.makedirs(out_dir, exist_ok=True)
out_path = os.path.join(out_dir, "records_ca_pspc_standing_offers.jsonl.gz")

stats = defaultdict(int)

REF_DATE = datetime.date(2026, 10, 31)
REF = "2026-10-31"

def parse_date(dstr):
    if not dstr:
        return None
    dstr = dstr.strip()[:10]
    if re.match(r"^\d{4}-\d{2}-\d{2}$", dstr):
        try:
            return datetime.date.fromisoformat(dstr)
        except ValueError:
            return None
    return None

CANADA_VALUES = {"CA", "CAN", "CANADA", "CANADA(CA)", "CANADÁ", "CANDA", "CANANDA", "CANANA", "CANAD"}

def is_canada_label(s):
    return re.sub(r"[\s`'\".]", "", (s or "")).upper() in CANADA_VALUES

PC_RE = re.compile(r"^[A-Za-z]\d[A-Za-z](?:\s?\d[A-Za-z]\d)?$")

def main():
    print(f"Downloading from {url}...")
    req = urllib.request.Request(url, headers={'User-Agent': 'contracts-research/1.0'})
    with urllib.request.urlopen(req, context=ctx) as response:
        raw_data = response.read()
        try:
            content = raw_data.decode('utf-8-sig')
        except UnicodeDecodeError:
            content = raw_data.decode('latin-1')

    reader = csv.DictReader(StringIO(content))

    agreements = defaultdict(list)
    for row in reader:
        stats['sosa_rows_seen'] += 1
        a = row.get("agreement-number", "").strip()
        if not a:
            continue
        agreements[a].append(row)

    print(f"Parsed {len(agreements)} agreements")

    cw_numbers = set()
    for a in agreements:
        match = re.match(r"^(CW\d{7})", a.upper())
        if match:
            cw_numbers.add(match.group(1))

    print(f"Downloading CanadaBuys legacy award notices to find addresses...")
    req_an = urllib.request.Request(url_an, headers={'User-Agent': 'contracts-research/1.0'})
    try:
        with urllib.request.urlopen(req_an, context=ctx) as response:
            raw_data_an = response.read()
            try:
                content_an = raw_data_an.decode('utf-8-sig')
            except UnicodeDecodeError:
                content_an = raw_data_an.decode('latin-1')
    except Exception as e:
        print(f"Error downloading {url_an}: {e}")
        content_an = ""

    cb_addresses = {}
    if content_an:
        reader_an = csv.DictReader(StringIO(content_an))
        for row in reader_an:
            a = row.get("contractNumber-numeroContrat", "").strip().upper()
            ref = row.get("referenceNumber-numeroReference", "").strip().upper()
            cw = None
            if re.match(r"^(CW\d{7})", a):
                cw = re.match(r"^(CW\d{7})", a).group(1)
            elif re.match(r"^(CW\d{7})", ref):
                cw = re.match(r"^(CW\d{7})", ref).group(1)

            if cw and cw in cw_numbers:
                c = row.get("supplierAddressCountry-fournisseurAdressePays-eng", "").strip()
                pc = row.get("supplierAddressPostalCode-fournisseurAdresseCodePostal", "").strip()
                if is_canada_label(c) or (not c and PC_RE.match(pc)):
                    cb_addresses[cw] = {
                        "country": "CA",
                        "country_basis": (f"supplierAddressCountry {c!r}" if c else f"supplierAddressPostalCode pattern {pc!r}") + f" from legacy award notices ({ref})",
                        "address": {
                            "line1": row.get("supplierAddressLine-ligneAdresseFournisseur-eng", "").replace("<br>", ", ").strip() or None,
                            "city": row.get("supplierAddressCity-fournisseurAdresseVille-eng", "").strip() or None,
                            "region": row.get("supplierAddressProvince-fournisseurAdresseProvince-eng", "").strip() or None,
                            "postal_code": pc or None,
                            "country": c or None
                        },
                        "source_row": row
                    }

    print(f"Downloading CanadaBuys legacy contract history to find addresses...")
    req_cb = urllib.request.Request(url_cb, headers={'User-Agent': 'contracts-research/1.0'})
    try:
        with urllib.request.urlopen(req_cb, context=ctx) as response:
            raw_data_cb = response.read()
            try:
                content_cb = raw_data_cb.decode('utf-8-sig')
            except UnicodeDecodeError:
                content_cb = raw_data_cb.decode('latin-1')
    except Exception as e:
        print(f"Error downloading {url_cb}: {e}")
        content_cb = ""

    if content_cb:
        reader_cb = csv.DictReader(StringIO(content_cb))
        for row in reader_cb:
            a = row.get("contractNumber-numeroContrat", "").strip().upper()
            ref = row.get("referenceNumber-numeroReference", "").strip().upper()
            cw = None
            if re.match(r"^(CW\d{7})", a):
                cw = re.match(r"^(CW\d{7})", a).group(1)
            elif re.match(r"^(CW\d{7})", ref):
                cw = re.match(r"^(CW\d{7})", ref).group(1)

            if cw and cw in cw_numbers and cw not in cb_addresses:
                c = row.get("supplierAddressCountry-fournisseurAdressePays-eng", "").strip()
                pc = row.get("supplierAddressPostalCode-fournisseurAdresseCodePostal", "").strip()
                if is_canada_label(c) or (not c and PC_RE.match(pc)):
                    cb_addresses[cw] = {
                        "country": "CA",
                        "country_basis": (f"supplierAddressCountry {c!r}" if c else f"supplierAddressPostalCode pattern {pc!r}") + f" from legacy contract history ({ref})",
                        "address": {
                            "line1": row.get("supplierAddressLine-ligneAdresseFournisseur-eng", "").replace("<br>", ", ").strip() or None,
                            "city": row.get("supplierAddressCity-fournisseurAdresseVille-eng", "").strip() or None,
                            "region": row.get("supplierAddressProvince-fournisseurAdresseProvince-eng", "").strip() or None,
                            "postal_code": pc or None,
                            "country": c or None
                        },
                        "source_row": row
                    }

    print(f"Found addresses for {len(cb_addresses)} CW numbers.")

    with gzip.open(out_path, "wt", encoding="utf-8") as outf:
        for a, rows in agreements.items():
            r0 = rows[0]
            start = parse_date(r0.get("sosa-start-date"))
            end = parse_date(r0.get("sosa-expiry-date"))

            status = "end_date_unknown"
            basis = "end_date_unknown: SOSA file has no expiry date"
            dates_end = None
            if end:
                dates_end = end.isoformat()
                if end.year >= 2100:
                    status = "end_date_unknown"
                    dates_end = None
                    basis = f"end_date_unknown: SOSA expiry-date {end.isoformat()} is a placeholder value (year >= 2100)"
                elif start and start > REF_DATE:
                    status = "ongoing"
                    basis = f"ongoing: SOSA award-date {start.isoformat()} > {REF} and expiry-date {end.isoformat()} >= {REF}"
                elif end < REF_DATE:
                    stats['excluded_end_past'] += 1
                    continue
                else:
                    status = "ongoing"
                    basis = f"ongoing: SOSA award-date {start.isoformat()} <= {REF} and expiry-date {end.isoformat()} >= {REF}"

            exps = set()
            for r in rows:
                e = parse_date(r.get("sosa-expiry-date"))
                if e and e.year < 2100:
                    exps.add(e)
            if len(exps) > 1:
                basis += f"; rows carry several expiry dates {[d.isoformat() for d in exps]}, latest used"

            cw = None
            match = re.match(r"^(CW\d{7})", a.upper())
            if match:
                cw = match.group(1)

            addr_info = cb_addresses.get(cw)
            if not addr_info:
                stats['excluded_no_canadian_address'] += 1
                continue

            vname = r0.get("supplier-legal-name", "").strip() or r0.get("supplier-standardized-name", "").strip() or r0.get("supplier-operating-name", "").strip() or None
            if not vname:
                stats['excluded_no_vendor_name'] += 1
                continue

            vendor = {
                "name": vname,
                "country": "CA",
                "country_basis": addr_info["country_basis"],
                "identifiers": {
                    "sosa_supplier_legal_name": r0.get("supplier-legal-name", "").strip() or None,
                    "sosa_supplier_standardized_name": r0.get("supplier-standardized-name", "").strip() or None,
                    "sosa_supplier_operating_name": r0.get("supplier-operating-name", "").strip() or None
                },
                "address": addr_info["address"],
                "contact": {}
            }

            commodities = []
            for r in rows:
                cd = r.get("commodity", "").strip().strip('"')
                if cd and cd not in [x["code"] for x in commodities]:
                    commodities.append({
                        "code": cd,
                        "description_en": r.get("commodity-description_en", "").strip().strip('"'),
                        "description_fr": r.get("commodity-description_fr", "").strip().strip('"')
                    })

            regions = []
            for r in rows:
                x = (r.get("delivery-point-code", "").strip(), r.get("delivery-point_en", "").strip())
                if x not in regions:
                    regions.append(x)

            at = r0.get("agreement-type_en", "").strip()

            contract = {
                "identifiers": {
                    "sosa_agreement_number": a,
                    "cw_number": cw
                },
                "title": r0.get("sosa-description_en", "").strip() or None,
                "description": "; ".join(f"{c['code']} - {c['description_en']}" for c in commodities) or None,
                "instrument_type": "supply arrangement" if at == "SA" else ("standing offer" if at else None),
                "procurement_method": None,
                "solicitation_procedure": None,
                "commodity": {
                    "unspsc": " | ".join(c["code"] for c in commodities) or None,
                    "unspsc_description": " | ".join(c["description_en"] for c in commodities) or None
                },
                "value": None,
                "currency": None,
                "value_detail": {},
                "dates": {
                    "published": (r0.get("date-file-published") or "")[:10] or None,
                    "signed": start.isoformat() if start else None,
                    "start": start.isoformat() if start else None,
                    "end": dates_end,
                    "amended_last": None
                },
                "related": {
                    "regions_of_delivery": [f"{c} {n}".strip() for c, n in regions]
                }
            }

            if end and end.year >= 2100:
                contract["dates"]["end_as_published"] = end.isoformat()

            eu = r0.get("end-user-entity_en", "").strip()

            # buyer must have a name
            if not eu:
                eu = "Public Works and Government Services Canada"

            buyer = {
                "name": eu or None,
                "country": "CA",
                "type": "federal department or agency",
                "identifiers": {
                    "sosa_end_user_entity_en": eu or None,
                    "sosa_end_user_entity_fr": r0.get("end-user-entity_fr", "").strip() or None,
                    "issuing_authority": "Public Services and Procurement Canada"
                },
                "address": {},
                "contact": {}
            }
            if eu == "Public Works and Government Services Canada":
                buyer["name_note"] = "PSPC/PWGSC as end user = government-wide instrument put in place by PSPC for use by federal organizations"

            raw = {
                "sosa_rows": rows,
                "supplier_address_source_row": addr_info["source_row"],
                "resource_url": url,
                "retrieved_at": datetime.datetime.now(datetime.timezone.utc).isoformat()
            }

            # Remove None values from dicts where appropriate
            contract["identifiers"] = {k: v for k, v in contract["identifiers"].items() if v}
            vendor["identifiers"] = {k: v for k, v in vendor["identifiers"].items() if v}
            buyer["identifiers"] = {k: v for k, v in buyer["identifiers"].items() if v}

            rec = {
                "record_id": f"ca_pspc_standing_offers:{a}",
                "source": {
                    "key": "ca_pspc_standing_offers",
                    "name": "PSPC standing offers and supply arrangements",
                    "publisher": "Public Services and Procurement Canada",
                    "dataset_url": "https://open.canada.ca/data/en/dataset/f5c8a5a0-354d-455a-99ab-8276aa38032e",
                    "record_url": None,
                    "retrieved_at": raw["retrieved_at"]
                },
                "status": status,
                "status_basis": basis,
                "contract": contract,
                "buyer": buyer,
                "vendor": vendor,
                "raw": raw,
                "link": "https://open.canada.ca/data/en/dataset/f5c8a5a0-354d-455a-99ab-8276aa38032e"
            }

            outf.write(json.dumps(rec, ensure_ascii=False) + "\n")
            stats['rows_output'] += 1

    print("\nStats:")
    for k, v in stats.items():
        print(f"  {k}: {v}")

if __name__ == "__main__":
    main()
