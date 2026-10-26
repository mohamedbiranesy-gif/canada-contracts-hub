#!/usr/bin/env python3
"""Normalize UK Contracts Finder OCDS compiled releases (candidate file produced by
scan_candidates.py) into the shared record shape; one record per award whose supplier is
located in Canada and whose contract is ongoing / end date unknown on the reference date.

Usage: python3 -I normalize_cf.py <candidates.jsonl> <out.jsonl> <review.tsv>
"""
import json, re, sys, collections, datetime as dt

TODAY = dt.date(2026, 10, 25)
RETRIEVED_AT = '2026-10-25T12:25:00Z'   # bulk file download time (UTC)
SOURCE = {
    'key': 'uk_contracts_finder',
    'name': 'Contracts Finder (UK) - OCDS award notices',
    'publisher': 'Cabinet Office / Crown Commercial Service (UK); bulk compiled releases via Open Contracting Partnership Data Registry',
    'dataset_url': 'https://www.contractsfinder.service.gov.uk/apidocumentation/Notices/1/GET-Published-Notice-OCDS-Search',
}
BULK_URL = 'https://data.open-contracting.org/en/publication/128/download?name=full.jsonl.gz'

CA_POSTAL = re.compile(r'\b[ABCEGHJ-NPRSTVXY]\d[ABCEGHJ-NPRSTV-Z][ ]?\d[ABCEGHJ-NPRSTV-Z]\d\b', re.I)
UK_POSTCODE = re.compile(r'\b[A-Z]{1,2}\d[A-Z\d]? ?\d[A-Z]{2}\b')
PROV_FULL = re.compile(r'\b(ontario|quebec|qu[ée]bec|british columbia|alberta|manitoba|saskatchewan|nova scotia|'
                       r'new brunswick|newfoundland|prince edward island|yukon|nunavut|northwest territories)\b', re.I)
PROV_ABBR = re.compile(r'\b(ON|QC|PQ|BC|B\.C\.|AB|MB|SK|NS|NB|NL|PE|PEI|YT|NU|NT)\b')
CANADA_WORD = re.compile(r'\bcanada\b', re.I)
# "Canada" as part of a UK street/building name
UK_CANADA_PLACE = re.compile(r'canada\W{0,3}(sq|square|water|house|place|wharf|street|st|road|rd|gate|life|court|lane|'
                             r'way|close|avenue|ave|dock|tower|yard|row|drive|walk|building|wood|quay|hill|works|farm)\b', re.I)

def addr_text(a):
    return ' '.join(str(v) for v in (a or {}).values() if v)

def is_canadian(party):
    """Return (bool, basis string) using only address fields (never the name)."""
    a = party.get('address') or {}
    txt = addr_text(a)
    cfield = ' '.join(str(a.get(k) or '') for k in ('country', 'countryName'))
    if re.search(r'\bcanada\b|^ca$', cfield.strip(), re.I):
        return True, 'address.country/countryName = Canada'
    structured = ' '.join(str(a.get(k) or '') for k in ('locality', 'region', 'postalCode'))
    if cfield.strip():
        # a non-Canadian country was stated; only override when structured fields are clearly Canadian
        if CA_POSTAL.search(structured) or PROV_FULL.search(structured) or CANADA_WORD.search(structured):
            return True, (f'address.locality/region/postalCode indicate Canada (postal code/province); '
                          f'NOTE source country field says {cfield.strip()!r} (conflict)')
        return False, ''
    # no country field (typical Contracts Finder record): free-text address only
    stripped = UK_CANADA_PLACE.sub('', txt)
    mentions_canada = bool(CANADA_WORD.search(stripped))
    has_ca_postal = bool(CA_POSTAL.search(txt))
    has_prov = bool(PROV_FULL.search(txt) or PROV_ABBR.search(txt))
    has_uk_pc = bool(UK_POSTCODE.search(txt)) and not has_ca_postal
    if has_uk_pc and not (mentions_canada and has_prov):
        return False, ''
    if mentions_canada:
        return True, 'address.streetAddress text contains country "Canada"'
    if has_ca_postal and has_prov:
        return True, 'address.streetAddress has Canadian postal code pattern + province'
    if has_ca_postal:
        # Canadian inward code is digit-letter-digit; UK inward codes are digit-letter-letter, so no UK collision
        return True, 'address.streetAddress has Canadian postal code pattern (A1A 1A1) and no other country stated'
    return False, ''

def iso_date(s):
    if not s or not isinstance(s, str):
        return None
    m = re.match(r'(\d{4}-\d{2}-\d{2})', s)
    return m.group(1) if m else None

def to_date(s):
    d = iso_date(s)
    try:
        return dt.date.fromisoformat(d) if d else None
    except ValueError:
        return None

def num(v):
    try:
        return float(v) if v is not None and v != '' else None
    except (TypeError, ValueError):
        return None

def notice_guid(url):
    m = re.search(r'contractsfinder\.service\.gov\.uk/Notice/([0-9a-f-]{36})', url or '', re.I)
    return m.group(1) if m else None

def main():
    src, out, review = sys.argv[1], sys.argv[2], sys.argv[3]
    counts = collections.Counter()
    seen = set()
    with open(src, encoding='utf-8') as f, open(out, 'w', encoding='utf-8') as o, open(review, 'w', encoding='utf-8') as rv:
        rv.write('decision\tstatus\tocid\taward_id\tsupplier\tbasis\taddress\tstart\tend\tnotice_url\n')
        for line in f:
            d = json.loads(line)
            d.pop('_match', None)
            counts['candidate_releases'] += 1
            parties = {p.get('id'): p for p in d.get('parties', []) or []}
            ca_parties = {}
            for p in d.get('parties', []) or []:
                if 'supplier' in (p.get('roles') or []):
                    ok, basis = is_canadian(p)
                    if ok:
                        ca_parties[p.get('id')] = basis
            if not ca_parties:
                counts['release_no_canadian_supplier_after_strict_check'] += 1
                for p in d.get('parties', []) or []:
                    if 'supplier' in (p.get('roles') or []):
                        rv.write('\t'.join(['EXCLUDED_not_canadian', '', d.get('ocid', ''), '', p.get('name', ''), '',
                                            addr_text(p.get('address')).replace('\n', ' ').replace('\t', ' '), '', '', '']) + '\n')
                continue
            tender = d.get('tender') or {}
            buyer = d.get('buyer') or {}
            buyer_party = parties.get(buyer.get('id')) or next((p for p in d.get('parties', []) if 'buyer' in (p.get('roles') or [])), {})
            awards = d.get('awards') or []
            if not awards:
                counts['release_without_awards'] += 1
                continue
            for aw in awards:
                sup_ids = [s.get('id') for s in (aw.get('suppliers') or [])]
                ca_sup = [sid for sid in sup_ids if sid in ca_parties]
                if not ca_sup:
                    continue
                counts['awards_to_canadian_supplier'] += 1
                vendor_party = parties.get(ca_sup[0]) or {}
                basis = ca_parties[ca_sup[0]]
                cp = aw.get('contractPeriod') or {}
                tcp = tender.get('contractPeriod') or {}
                start = to_date(cp.get('startDate')) or to_date(tcp.get('startDate'))
                end = to_date(cp.get('endDate')) or to_date(tcp.get('endDate'))
                start_src = 'awards[].contractPeriod' if cp.get('startDate') else ('tender.contractPeriod' if tcp.get('startDate') else None)
                end_src = 'awards[].contractPeriod' if cp.get('endDate') else ('tender.contractPeriod' if tcp.get('endDate') else None)
                award_date = to_date(aw.get('date'))
                effective_start = start or award_date
                if (aw.get('status') or 'active') not in ('active', 'pending'):
                    counts[f'excluded_award_status_{aw.get("status")}'] += 1
                    continue
                if tender.get('status') in ('cancelled', 'withdrawn', 'unsuccessful'):
                    counts[f'excluded_tender_status_{tender.get("status")}'] += 1
                    continue
                docs = [x for x in (aw.get('documents') or []) if notice_guid(x.get('url'))]
                notice_url = docs[0]['url'] if docs else None
                if not notice_url:
                    for x in (tender.get('documents') or []):
                        if notice_guid(x.get('url')):
                            notice_url = x['url']; break
                if end is None:
                    status = 'end_date_unknown'
                    status_basis = ('No awards[].contractPeriod.endDate or tender.contractPeriod.endDate in the notice; '
                                    f'award date {aw.get("date")}')
                    if effective_start and effective_start > TODAY:
                        counts['excluded_future_start_no_end'] += 1
                        continue
                else:
                    if end < TODAY:
                        counts['excluded_end_before_today'] += 1
                        rv.write('\t'.join(['EXCLUDED_ended', '', d.get('ocid', ''), aw.get('id', ''), vendor_party.get('name', ''), basis,
                                            addr_text(vendor_party.get('address')).replace('\n', ' ').replace('\t', ' '),
                                            str(start), str(end), notice_url or '']) + '\n')
                        continue
                    if effective_start and effective_start > TODAY:
                        counts['excluded_start_after_today'] += 1
                        continue
                    status = 'ongoing'
                    status_basis = (f'{start_src}.startDate {start} <= 2026-10-25 <= {end_src}.endDate {end}'
                                    if start else f'no start date; award date {award_date} <= 2026-10-25 <= {end_src}.endDate {end}')
                rid = f"uk_contracts_finder:{aw.get('id')}"
                if rid in seen:
                    rid = f"{rid}:{ca_sup[0]}"
                seen.add(rid)
                vaddr = vendor_party.get('address') or {}
                vid = vendor_party.get('identifier') or {}
                vendor_ids = {}
                if vid.get('scheme') and vid.get('id'):
                    vendor_ids[vid['scheme']] = vid['id']
                for ai in vendor_party.get('additionalIdentifiers') or []:
                    if ai.get('scheme') and ai.get('id'):
                        vendor_ids[ai['scheme']] = ai['id']
                vendor_ids['contracts_finder_party_id'] = vendor_party.get('id')
                bid = buyer_party.get('identifier') or {}
                buyer_ids = {'contracts_finder_party_id': buyer_party.get('id')}
                if bid.get('scheme') and bid.get('id'):
                    buyer_ids[bid['scheme']] = bid['id']
                cls = tender.get('classification') or {}
                commodity = {}
                if cls.get('id'):
                    commodity['cpv'] = cls.get('id'); commodity['cpv_description'] = cls.get('description')
                addl = [c.get('id') for c in (tender.get('additionalClassifications') or []) if c.get('id')]
                if addl:
                    commodity['cpv_additional'] = addl
                value = (aw.get('value') or {})
                n_sup = len(aw.get('suppliers') or [])
                instrument = 'contract'
                if (tender.get('techniques') or {}).get('hasFrameworkAgreement') or n_sup > 1 or re.search(r'\bframework\b', (tender.get('title') or '') + ' ' + (tender.get('description') or ''), re.I):
                    instrument = 'framework agreement / multi-supplier award' if n_sup > 1 else 'framework agreement'
                identifiers = {
                    'ocid': d.get('ocid'), 'award_id': aw.get('id'), 'notice_guid': notice_guid(notice_url),
                    'tender_id': tender.get('id'), 'compiled_release_id': d.get('id'),
                }
                record = {
                    'record_id': rid,
                    'source': dict(SOURCE, record_url=notice_url, retrieved_at=RETRIEVED_AT),
                    'status': status,
                    'status_basis': status_basis,
                    'contract': {
                        'identifiers': identifiers,
                        'title': tender.get('title'), 'description': tender.get('description') or aw.get('description'),
                        'instrument_type': instrument,
                        'procurement_method': tender.get('procurementMethod'),
                        'solicitation_procedure': tender.get('procurementMethodDetails'),
                        'commodity': commodity,
                        'value': num(value.get('amount')), 'currency': value.get('currency'),
                        'value_detail': dict({k: num(v) for k, v in {
                            'award_value': value.get('amount'),
                            'tender_value': (tender.get('value') or {}).get('amount'),
                            'tender_min_value': (tender.get('minValue') or {}).get('amount')}.items() if num(v) is not None},
                            **({'value_note': f'award value is the total for all {n_sup} suppliers on this award (Contracts Finder does not split per supplier)'} if n_sup > 1 else {})),
                        'dates': {'published': iso_date(aw.get('datePublished') or d.get('date')),
                                  'signed': iso_date(aw.get('date')), 'start': iso_date(start.isoformat() if start else None),
                                  'end': iso_date(end.isoformat() if end else None), 'amended_last': iso_date(d.get('date'))},
                        'related': {'award_notice_url': notice_url,
                                    'tender_notice_url': next((x.get('url') for x in (tender.get('documents') or []) if notice_guid(x.get('url'))), None),
                                    'ocds_record_url': f"https://www.contractsfinder.service.gov.uk/Published/OCDS/Record/{d.get('ocid')}",
                                    'all_suppliers_on_award': [s.get('name') for s in (aw.get('suppliers') or [])],
                                    'main_procurement_category': tender.get('mainProcurementCategory')},
                    },
                    'buyer': {
                        'name': buyer_party.get('name') or buyer.get('name'), 'country': 'GB',
                        'type': None, 'identifiers': buyer_ids,
                        'address': buyer_party.get('address') or {}, 'contact': buyer_party.get('contactPoint') or {},
                    },
                    'vendor': {
                        'name': vendor_party.get('name'), 'country': 'CA', 'country_basis': basis,
                        'identifiers': vendor_ids,
                        'address': {'line1': vaddr.get('streetAddress'), 'city': vaddr.get('locality'), 'region': vaddr.get('region'),
                                    'postal_code': vaddr.get('postalCode'), 'country': vaddr.get('countryName') or vaddr.get('country')},
                        'contact': vendor_party.get('contactPoint') or {},
                    },
                    'raw': {'compiled_release': d, 'bulk_source': BULK_URL},
                }
                o.write(json.dumps(record, ensure_ascii=False) + '\n')
                counts[f'emitted_{status}'] += 1
                rv.write('\t'.join(['INCLUDED', status, d.get('ocid', ''), aw.get('id', ''), vendor_party.get('name', ''), basis,
                                    addr_text(vaddr).replace('\n', ' ').replace('\t', ' '), str(start), str(end), notice_url or '']) + '\n')
    print(json.dumps(counts, indent=1))

if __name__ == '__main__':
    main()
