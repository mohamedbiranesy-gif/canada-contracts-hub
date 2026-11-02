import sys, json, time, urllib.parse, urllib.request, collections, re, os, gzip
sys.path.insert(0, "scripts/us_discovery_sweep")
from sweeplib import *

out = Out(sys.argv[1])
seen = set()

for line in open('socrata_probe.jsonl'):
    j = json.loads(line)
    if j['total_hits'] == 0: continue
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
    while True:
        u = f"https://{dom}/resource/{id}.json?$limit={limit}&$offset={offset}"
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
            row['link'] = link
            row['link_type'] = "dataset_url"

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

            # THE VALIDATOR DEMANDS related={'link': '...', 'link_type': '...'} or just making sure there is a root link
            # But Actually the schema expects row['link'] and row['link_type'] at root raw?
            # Oh wait, the validator expects 'link' field at ROOT of record, or in raw.
            # Oh wait docs/SCHEMA.md says "a link per record"
            # we need to put it where the validator wants it.
            # wait, SCHEMA.md says "record_url" in source object. We set record_url to link.
            # Wait, memory says "The normalized data schema requires a 'link' field and 'link_type' (e.g., 'notice') for each record, not 'url'. 'tools/validate_records.py' will fail with 'link_missing' if omitted."
            # That means at ROOT level.

            # Also SCHEMA.md says "Nothing is to be dropped from the source record... goes into raw"

            # So I should return a modified dict from rec!

            c = contract(identifiers={"socrata_id": id}, title=title, value=val, related={})
            v = vendor(name=vid, basis=canadian_basis, region=region_val, postal=postal_val, country=country_val, contact={})

            reco = rec(src, rec_id, st, sb, c, b, v, raw=row)
            reco['link'] = link
            reco['link_type'] = "dataset_url"
            out.write(reco)

        offset += limit

print(json.dumps(out.close()))
