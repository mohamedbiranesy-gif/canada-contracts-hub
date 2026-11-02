import sys, json, time, urllib.parse, urllib.request, collections, re, os, gzip

# Hardcoded list of domains and datasets found in the probe
DATASETS = [
    {"domain": "corstat.coronaca.gov", "id": "mdmf-aswt", "cols": [{"col": "vendor_st", "kind": "state", "vendorish": True}, {"col": "vendor_city", "kind": "city", "vendorish": True}]},
    {"domain": "citydata.mesaaz.gov", "id": "u5x3-dvhs", "cols": [{"col": "vendor_state", "kind": "state", "vendorish": True}]},
    {"domain": "controllerdata.lacity.org", "id": "4bdv-srep", "cols": [{"col": "supplier_country", "kind": "country", "vendorish": True}, {"col": "supplier_city", "kind": "city", "vendorish": True}]},
    {"domain": "data.brla.gov", "id": "54bn-2sqf", "cols": [{"col": "vendor_state", "kind": "state", "vendorish": True}, {"col": "vendor_city", "kind": "city", "vendorish": True}]},
    {"domain": "data.brla.gov", "id": "eyp8-c7wc", "cols": [{"col": "vendor_state", "kind": "state", "vendorish": True}, {"col": "vendor_city", "kind": "city", "vendorish": True}]},
    {"domain": "cthru.data.socrata.com", "id": "2bxs-ytms", "cols": [{"col": "vendor_state", "kind": "state", "vendorish": True}, {"col": "vendor_city", "kind": "city", "vendorish": True}]},
    {"domain": "data.brla.gov", "id": "2ung-w7t4", "cols": [{"col": "vendor_state", "kind": "state", "vendorish": True}, {"col": "vendor_city", "kind": "city", "vendorish": True}]},
    {"domain": "controllerdata.lacity.org", "id": "pggv-e4fn", "cols": [{"col": "supplier_country", "kind": "country", "vendorish": True}, {"col": "supplier_city", "kind": "city", "vendorish": True}]},
    {"domain": "data.cincinnati-oh.gov", "id": "vmk6-gy84", "cols": [{"col": "vendor_state", "kind": "state", "vendorish": True}, {"col": "vendor_city", "kind": "city", "vendorish": True}]},
    {"domain": "data.cityofchicago.org", "id": "5wd9-d675", "cols": [{"col": "state", "kind": "state", "vendorish": True}, {"col": "city", "kind": "city", "vendorish": True}]},
    {"domain": "data.brla.gov", "id": "vwa8-ps2a", "cols": [{"col": "vendor_state", "kind": "state", "vendorish": True}, {"col": "vendor_city", "kind": "city", "vendorish": True}]},
    {"domain": "data.brla.gov", "id": "6w2f-pxr9", "cols": [{"col": "vendor_state", "kind": "state", "vendorish": True}, {"col": "vendor_city", "kind": "city", "vendorish": True}]},
    {"domain": "data.cityofchicago.org", "id": "rsxa-ify5", "cols": [{"col": "state", "kind": "state", "vendorish": True}, {"col": "city", "kind": "city", "vendorish": True}]},
    {"domain": "data.brla.gov", "id": "7fq7-8j7r", "cols": [{"col": "contractor_state", "kind": "state", "vendorish": True}, {"col": "contractor_city", "kind": "city", "vendorish": True}]},
    {"domain": "data.cityofnewyork.us", "id": "szkz-syh6", "cols": [{"col": "vendor_state", "kind": "state", "vendorish": True}, {"col": "vendor_city", "kind": "city", "vendorish": True}]},
    {"domain": "data.colorado.gov", "id": "66zf-qjdd", "cols": [{"col": "vendor_state", "kind": "state", "vendorish": True}, {"col": "vendor_city", "kind": "city", "vendorish": True}]},
    {"domain": "data.colorado.gov", "id": "wnau-xrqi", "cols": [{"col": "vendor_state", "kind": "state", "vendorish": True}, {"col": "vendor_city", "kind": "city", "vendorish": True}]},
    {"domain": "data.fultoncountyga.gov", "id": "2jx8-2ffx", "cols": [{"col": "state", "kind": "state", "vendorish": True}, {"col": "zip", "kind": "zip", "vendorish": True}, {"col": "city", "kind": "city", "vendorish": True}]},
    {"domain": "data.delaware.gov", "id": "h9bb-iyu6", "cols": [{"col": "state", "kind": "state", "vendorish": True}, {"col": "city", "kind": "city", "vendorish": True}]},
    {"domain": "data.lacity.org", "id": "3f9m-afei", "cols": [{"col": "contractor_state", "kind": "state", "vendorish": True}, {"col": "contractor_city", "kind": "city", "vendorish": True}]},
    {"domain": "data.mo.gov", "id": "kf27-upwz", "cols": [{"col": "state", "kind": "state", "vendorish": True}, {"col": "city", "kind": "city", "vendorish": True}]},
    {"domain": "data.marincounty.gov", "id": "mkbn-caye", "cols": [{"col": "contractor_state", "kind": "state", "vendorish": True}, {"col": "contractor_city", "kind": "city", "vendorish": True}]},
    {"domain": "data.nj.gov", "id": "tfhb-8beb", "cols": [{"col": "vendor_state", "kind": "state", "vendorish": True}, {"col": "vendor_city", "kind": "city", "vendorish": True}]},
    {"domain": "data.ny.gov", "id": "26ei-n4eb", "cols": [{"col": "state", "kind": "state", "vendorish": True}, {"col": "city", "kind": "city", "vendorish": True}]},
    {"domain": "data.ny.gov", "id": "3pjx-bgty", "cols": [{"col": "state", "kind": "state", "vendorish": True}, {"col": "city", "kind": "city", "vendorish": True}]},
    {"domain": "data.ny.gov", "id": "3x8r-34rs", "cols": [{"col": "contractor_state", "kind": "state", "vendorish": True}, {"col": "contractor_city", "kind": "city", "vendorish": True}]},
    {"domain": "data.ny.gov", "id": "7xzk-zyk5", "cols": [{"col": "contractor_state", "kind": "state", "vendorish": True}, {"col": "contractor_city", "kind": "city", "vendorish": True}]},
    {"domain": "data.ny.gov", "id": "8bmh-tuz3", "cols": [{"col": "state", "kind": "state", "vendorish": True}, {"col": "city", "kind": "city", "vendorish": True}]},
    {"domain": "data.ny.gov", "id": "9wxk-hakb", "cols": [{"col": "contractor_state", "kind": "state", "vendorish": True}, {"col": "contractor_city", "kind": "city", "vendorish": True}]},
    {"domain": "data.ny.gov", "id": "c6c2-n3if", "cols": [{"col": "state", "kind": "state", "vendorish": True}, {"col": "city", "kind": "city", "vendorish": True}]},
    {"domain": "data.ny.gov", "id": "8w5p-k45m", "cols": [{"col": "vendor_state", "kind": "state", "vendorish": True}, {"col": "vendor_city", "kind": "city", "vendorish": True}, {"col": "vendor_country", "kind": "country", "vendorish": True}]},
    {"domain": "data.ny.gov", "id": "dprp-55ye", "cols": [{"col": "contractor_state", "kind": "state", "vendorish": True}, {"col": "contractor_city", "kind": "city", "vendorish": True}]},
    {"domain": "data.ny.gov", "id": "d84c-dk28", "cols": [{"col": "vendor_state", "kind": "state", "vendorish": True}, {"col": "vendor_city", "kind": "city", "vendorish": True}, {"col": "vendor_country", "kind": "country", "vendorish": True}]},
    {"domain": "data.ny.gov", "id": "djsm-9cw7", "cols": [{"col": "state", "kind": "state", "vendorish": True}, {"col": "city", "kind": "city", "vendorish": True}]},
    {"domain": "data.ny.gov", "id": "ehig-g5x3", "cols": [{"col": "vendor_state", "kind": "state", "vendorish": True}, {"col": "vendor_city", "kind": "city", "vendorish": True}, {"col": "vendor_country", "kind": "country", "vendorish": True}]},
    {"domain": "data.ny.gov", "id": "i4jv-zkey", "cols": [{"col": "state", "kind": "state", "vendorish": True}, {"col": "city", "kind": "city", "vendorish": True}]},
    {"domain": "data.ny.gov", "id": "kbn3-a3jv", "cols": [{"col": "state", "kind": "state", "vendorish": True}, {"col": "city", "kind": "city", "vendorish": True}]},
    {"domain": "data.ny.gov", "id": "p3p6-xqr5", "cols": [{"col": "vendor_state", "kind": "state", "vendorish": True}, {"col": "vendor_city", "kind": "city", "vendorish": True}, {"col": "vendor_country", "kind": "country", "vendorish": True}]}
]

sys.path.insert(0, "scripts/us_discovery_sweep")
from sweeplib import *

out = Out(sys.argv[1])
seen = set()

for j in DATASETS:
    dom = j['domain']
    if 'controllerdata.lacity.org' in dom or 'data.colorado.gov' in dom or 'cthru.data.socrata.com' in dom or 'data.brla.gov' in dom or 'data.cityofchicago.org' in dom or 'data.cityofnewyork.us' in dom: continue
    if 'corstat.coronaca.gov' in dom or 'data.montgomerycountymd.gov' in dom: continue
    if 'data.texas.gov' in dom: continue

    id = j['id']
    if id in seen: continue
    seen.add(id)

    print(f"Scraping {dom} {id}")

    meta = None
    try:
        with urllib.request.urlopen(f"https://{dom}/api/views/{id}.json", timeout=60) as r:
            meta = json.loads(r.read())
    except:
        pass

    buyer_name = "Unknown"
    buyer_website = None
    if meta:
        buyer_name = meta.get('attribution') or dom
        buyer_website = meta.get('metadata', {}).get('custom_fields', {}).get('Publisher', {}).get('Publisher Website', None)
        if not buyer_website:
            buyer_website = meta.get('metadata', {}).get('custom_fields', {}).get('Dataset Information', {}).get('Agency Website', None)

    offset = 0
    limit = 10000

    def q(s): return "'" + s.replace("'", "''") + "'"
    PROVS = ["ON", "ONT", "ONTARIO", "QC", "PQ", "QUE", "QUEBEC", "QUÉBEC", "BC", "B.C.", "BRITISH COLUMBIA", "AB", "ALTA",
             "ALBERTA", "MB", "MAN", "MANITOBA", "SK", "SASK", "SASKATCHEWAN", "NS", "N.S.", "NOVA SCOTIA", "NB", "N.B.",
             "NEW BRUNSWICK", "NL", "NF", "NFLD", "NEWFOUNDLAND", "NEWFOUNDLAND AND LABRADOR", "PE", "PEI", "P.E.I.",
             "PRINCE EDWARD ISLAND", "YT", "YUKON", "NT", "NWT", "NORTHWEST TERRITORIES", "NU", "NUNAVUT", "CANADA", "CAN", "CDN"]

    where_clauses = []
    for c in j['cols']:
        col = c['col']
        kind = c['kind']
        c_name = f"upper(`{col}`)"
        if kind == "country":
            where_clauses.append(f"({c_name} in ('CA','CAN','CANADA','CDN') OR {c_name} like '%CANADA%')")
        elif kind == "state":
            where_clauses.append(f"({c_name} in ({','.join(q(p) for p in PROVS)}) OR {c_name} like '%CANADA%')")
        elif kind == "zip":
            where_clauses.append(f"({c_name} >= 'A' AND {c_name} < '[')")
        elif kind in ("address", "city"):
            where_clauses.append(f"({c_name} like '%CANADA%')")

    where_query = " OR ".join(where_clauses)
    where_query_encoded = urllib.parse.quote(where_query)

    while True:
        u = f"https://{dom}/resource/{id}.json?$limit={limit}&$offset={offset}&$where={where_query_encoded}"
        try:
            req = urllib.request.Request(u, headers={'User-Agent': 'contracts-research/1.0'})
            with urllib.request.urlopen(req, timeout=120) as r:
                data = json.loads(r.read())
        except Exception as e:
            print(f"Error {dom} {id} {e}")
            break

        if not data: break

        for row in data:
            canadian_basis = None
            region_val = None
            postal_val = None
            country_val = None
            text_val = None

            for c in j['cols']:
                col = c['col']
                kind = c['kind']
                if kind == 'state':
                    ok, basis = canadian(region=row.get(col), region_field=col)
                    if ok: canadian_basis = basis; region_val = row.get(col)
                elif kind == 'country':
                    ok, basis = canadian(country=row.get(col), country_field=col)
                    if ok: canadian_basis = basis; country_val = row.get(col)
                elif kind == 'zip':
                    ok, basis = canadian(postal=row.get(col), postal_field=col)
                    if ok: canadian_basis = basis; postal_val = row.get(col)
                elif kind in ('address', 'city'):
                    ok, basis = canadian(text=row.get(col))
                    if ok: canadian_basis = basis; text_val = row.get(col)

            if not canadian_basis:
                out.exclude("not_canadian no_match")
                continue

            title = None
            val = None
            date_col = None
            for k in row.keys():
                kl = k.lower()
                if 'title' in kl or 'desc' in kl:
                    if not title: title = str(row[k])
                if 'amount' in kl or 'total' in kl or 'price' in kl or 'value' in kl:
                    if not val: val = amt(row[k])
                if 'date' in kl and not date_col:
                    date_col = k

            st = "end_date_unknown"
            sb = "Extracted from Socrata sweep; end date not definitively known."

            start_date = None
            end_date = None
            award_date = None
            for k, v in row.items():
                kl = k.lower()
                if 'start' in kl and 'date' in kl: start_date = d(v)
                elif 'end' in kl and 'date' in kl: end_date = d(v)
                elif 'award' in kl and 'date' in kl: award_date = d(v)

            if start_date or end_date or award_date:
                calc_st, calc_sb = status_contract(start_date, end_date, award_date)
                if calc_st:
                    st = calc_st
                    sb = calc_sb
                else:
                    out.exclude(calc_sb)
                    continue

            vid = row.get('vendor_name') or row.get('vendor') or row.get('company') or row.get('company_name') or row.get('business_name') or row.get('contractor_name') or row.get('payee_name') or row.get('vendor_id') or row.get('organization') or row.get('entity_name') or "Missing"
            if vid.lower() in ("missing", "unknown", "n/a", "none", "null"):
                out.exclude("vendor.name_missing")
                continue

            link = f"https://{dom}/d/{id}"

            rec_id = sid(dom, id, json.dumps(row))

            src = {
                "key": "us_socrata_sweep_continue",
                "name": meta.get('name') if meta else id,
                "publisher": meta.get('attribution') if meta else dom,
                "dataset_url": link,
                "record_url": link,
                "retrieved_at": now_iso()
            }

            b = buyer(buyer_name, "public body", address={"country": "US"}, contact={"website": buyer_website})
            c = contract(identifiers={"socrata_id": id}, title=title, value=val, related={})
            v = vendor(name=vid, basis=canadian_basis, region=region_val, postal=postal_val, country=country_val, contact={})

            record = rec(src, rec_id, st, sb, c, b, v, raw=row)
            record["link"] = link
            record["link_type"] = "dataset_url"
            out.write(record)

        offset += limit

print(json.dumps(out.close()))
