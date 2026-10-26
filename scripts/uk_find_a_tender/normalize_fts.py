#!/usr/bin/env python3
"""Normalize UK Find a Tender OCDS compiled releases (candidate file from scan_candidates.py)
into the shared record shape: one record per award whose supplier address is in Canada and whose
contract is ongoing / inferred ongoing / end date unknown on the reference date.

Usage: python3 -I normalize_fts.py <candidates.jsonl> <out.jsonl> <review.tsv>
"""
import json, re, sys, collections, datetime as dt

TODAY = dt.date(2026, 10, 25)
RETRIEVED_AT = '2026-10-25T12:25:00Z'
SOURCE = {
    'key': 'uk_find_a_tender',
    'name': 'Find a Tender Service (UK) - OCDS release packages',
    'publisher': 'Cabinet Office (UK); bulk compiled releases via Open Contracting Partnership Data Registry',
    'dataset_url': 'https://www.find-tender.service.gov.uk/apidocumentation/1.0/GET-ocdsReleasePackages',
}
BULK_URL = 'https://data.open-contracting.org/en/publication/41/download?name=full.jsonl.gz'

CA_POSTAL = re.compile(r'\b[ABCEGHJ-NPRSTVXY]\d[ABCEGHJ-NPRSTV-Z][ ]?\d[ABCEGHJ-NPRSTV-Z]\d\b', re.I)
UK_POSTCODE = re.compile(r'\b[A-Z]{1,2}\d[A-Z\d]? ?\d[A-Z]{2}\b')
PROV_FULL = re.compile(r'\b(ontario|quebec|qu[ée]bec|british columbia|alberta|manitoba|saskatchewan|nova scotia|'
                       r'new brunswick|newfoundland|prince edward island|yukon|nunavut|northwest territories)\b', re.I)
PROV_ABBR = re.compile(r'\b(ON|QC|PQ|BC|B\.C\.|AB|MB|SK|NS|NB|NL|PE|PEI|YT|NU|NT)\b')
CANADA_WORD = re.compile(r'\bcanada\b', re.I)
UK_CANADA_PLACE = re.compile(r'canada\W{0,3}(sq|square|water|house|place|wharf|street|st|road|rd|gate|life|court|lane|'
                             r'way|close|avenue|ave|dock|tower|yard|row|drive|walk|building|wood|quay|hill|works|farm|highway)\b', re.I)
NOTICE_RE = re.compile(r'find-tender\.service\.gov\.uk/Notice/(\d{6}-\d{4})', re.I)

def addr_text(a):
    return ' '.join(str(v) for v in (a or {}).values() if v)

def is_canadian(party):
    a = party.get('address') or {}
    txt = addr_text(a)
    country = str(a.get('country') or '').strip()
    cname = str(a.get('countryName') or '').strip()
    if country.upper() == 'CA' or re.search(r'\bcanada\b', cname, re.I):
        rest = ' '.join(str(a.get(k) or '') for k in ('streetAddress', 'locality', 'region', 'postalCode'))
        if re.search(r'\b\d{5}(-\d{4})?\b', rest) and not CA_POSTAL.search(rest) and re.search(
                r'\b(AL|AK|AZ|AR|CA|CO|CT|DE|FL|GA|HI|ID|IL|IN|IA|KS|KY|LA|ME|MD|MA|MI|MN|MS|MO|MT|NE|NV|NH|NJ|NM|NY|NC|ND|OH|OK|OR|PA|RI|SC|SD|TN|TX|UT|VT|VA|WA|WV|WI|WY)\b', rest):
            return True, (f'address.country={country!r} / address.countryName={cname!r} BUT street/locality/postal code look like a '
                          f'US address ({rest.strip()!r}) (CONFLICT, included because the source country field says Canada)'), True
        return True, f'address.country={country!r} / address.countryName={cname!r}', False
    structured = ' '.join(str(a.get(k) or '') for k in ('locality', 'region', 'postalCode'))
    if country or cname:
        # publisher stated another country; override only on hard evidence in structured address fields
        # (a Canadian postal code A1A 1A1 cannot be a UK/US/other postcode)
        if CA_POSTAL.search(structured) or CANADA_WORD.search(UK_CANADA_PLACE.sub('', structured)):
            return True, (f'address.locality/region/postalCode are Canadian ({structured.strip()!r}) but source country '
                          f'field says country={country!r} countryName={cname!r} (CONFLICT, included for review)'), True
        return False, '', False
    stripped = UK_CANADA_PLACE.sub('', txt)
    if UK_POSTCODE.search(txt) and not CA_POSTAL.search(txt) and not (CANADA_WORD.search(stripped) and (PROV_FULL.search(txt) or PROV_ABBR.search(txt))):
        return False, '', False
    if CANADA_WORD.search(stripped):
        return True, 'address text contains country "Canada" (no country field)', False
    if CA_POSTAL.search(txt) and (PROV_FULL.search(txt) or PROV_ABBR.search(txt)):
        return True, 'address has Canadian postal code pattern + province (no country field)', False
    return False, '', False

def iso_date(s):
    m = re.match(r'(\d{4}-\d{2}-\d{2})', s or '') if isinstance(s, str) else None
    return m.group(1) if m else None

def to_date(s):
    d = iso_date(s)
    try:
        return dt.date.fromisoformat(d) if d else None
    except ValueError:
        return None

def num(v):
    try:
        return float(v) if v not in (None, '') else None
    except (TypeError, ValueError):
        return None

def notice_ids(obj):
    acc = []
    def walk(o):
        if isinstance(o, dict):
            for v in o.values(): walk(v)
        elif isinstance(o, list):
            for v in o: walk(v)
        elif isinstance(o, str):
            for m in NOTICE_RE.finditer(o):
                if m.group(1) not in acc: acc.append(m.group(1))
    walk(obj)
    return acc

def main():
    src, out, review = sys.argv[1], sys.argv[2], sys.argv[3]
    counts = collections.Counter(); seen = set()
    with open(src, encoding='utf-8') as f, open(out, 'w', encoding='utf-8') as o, open(review, 'w', encoding='utf-8') as rv:
        rv.write('decision\tstatus\tocid\taward_id\tsupplier\tbasis\taddress\tstart\tend\tnotice_url\n')
        for line in f:
            d = json.loads(line); d.pop('_match', None)
            counts['candidate_releases'] += 1
            parties = {p.get('id'): p for p in d.get('parties', []) or []}
            ca = {}
            for p in d.get('parties', []) or []:
                if 'supplier' in (p.get('roles') or []):
                    ok, basis, conflict = is_canadian(p)
                    if ok: ca[p.get('id')] = (basis, conflict)
                    else:
                        rv.write('\t'.join(['NOT_CANADIAN', '', d.get('ocid', ''), '', p.get('name', ''), '',
                                            addr_text(p.get('address')).replace('\n', ' ').replace('\t', ' '), '', '', '']) + '\n')
            if not ca:
                counts['release_no_canadian_supplier_after_strict_check'] += 1; continue
            tender = d.get('tender') or {}
            buyer = d.get('buyer') or {}
            buyer_party = parties.get(buyer.get('id')) or next((p for p in d.get('parties', []) if 'buyer' in (p.get('roles') or [])), {})
            lots = {l.get('id'): l for l in (tender.get('lots') or [])}
            contracts_by_award = collections.defaultdict(list)
            for c in d.get('contracts') or []:
                contracts_by_award[c.get('awardID')].append(c)
            techniques = tender.get('techniques') or {}
            fw = techniques.get('frameworkAgreement') or {}
            is_dps = bool(techniques.get('hasDynamicPurchasingSystem') or techniques.get('dynamicPurchasingSystem'))
            # --- group awards: (a) Dynamic Market / open framework admissions -> one record per supplier
            #                   (b) identical awards re-published under several notice ids -> one record
            groups = collections.OrderedDict()
            for aw in d.get('awards') or []:
                sup_ids = [s.get('id') for s in (aw.get('suppliers') or [])]
                ca_sup = [sid for sid in sup_ids if sid in ca]
                if not ca_sup: continue
                counts['awards_to_canadian_supplier'] += 1
                if (aw.get('status') or 'active') in ('cancelled', 'unsuccessful'):
                    counts[f'excluded_award_status_{aw.get("status")}'] += 1; continue
                cons = contracts_by_award.get(aw.get('id'), [])
                if cons and all(c.get('status') in ('cancelled', 'terminated') for c in cons):
                    counts['excluded_contract_terminated_or_cancelled'] += 1; continue
                seen_names = set()
                for sid in ca_sup:
                    nm = re.sub(r'[^a-z0-9]', '', (parties.get(sid) or {}).get('name', '').lower())
                    if nm in seen_names:
                        counts['duplicate_supplier_party_within_award'] += 1; continue
                    seen_names.add(nm)
                    if is_dps and not cons and not (aw.get('contractPeriod') or {}).get('endDate'):
                        key = ('dps', nm)
                    else:
                        val = (cons[0].get('value') if cons else None) or aw.get('value') or {}
                        lots_key = tuple(aw.get('relatedLots') or [])
                        if lots_key or val.get('amount') is not None:
                            # same process + same supplier + same lot(s) + same value => same contract published in
                            # several notices (e.g. UK5 transparency notice followed by UK7 contract details notice)
                            sig = (lots_key, round(float(val.get('amount') or 0), 2), val.get('currency'))
                        else:
                            sig = (aw.get('title') or (cons[0].get('title') if cons else None), (cons[0].get('dateSigned') if cons else aw.get('date')))
                        key = ('award', nm, sig)
                    groups.setdefault(key, []).append((aw, cons, sid))
            for key, members in groups.items():
                # prefer the member that carries a contract (dateSigned / value / period), then the latest notice
                members = sorted(members, key=lambda m: (bool(m[1]), bool((m[1][0].get('period') if m[1] else None) or m[0].get('contractPeriod')),
                                                         bool(m[1] and m[1][0].get('dateSigned')), str(m[0].get('id'))), reverse=True)
                aw, cons, sid = members[0]
                dup_award_ids = [m[0].get('id') for m in members[1:]]
                dup_contract_ids = [c.get('id') for m in members[1:] for c in m[1]]
                if dup_award_ids:
                    counts['awards_collapsed_as_duplicates_or_dps_lots'] += len(dup_award_ids)
                vendor_party = parties.get(sid) or {}
                basis, conflict = ca[sid]
                # merge period info from collapsed members if the chosen one lacks it
                for m in members[1:]:
                    for c in m[1]:
                        if c.get('period') and not any(cc.get('period') for cc in cons):
                            cons = cons + [dict(c, _from_collapsed_award=m[0].get('id'))]
                # ---- period resolution ----
                start = end = None; start_src = end_src = None; duration_days = None; dur_src = None
                for c in cons:
                    per = c.get('period') or {}
                    if per.get('startDate') and not start: start, start_src = to_date(per['startDate']), 'contracts[].period.startDate'
                    if per.get('endDate') and not end: end, end_src = to_date(per['endDate']), 'contracts[].period.endDate'
                    if per.get('durationInDays') and not duration_days: duration_days, dur_src = per['durationInDays'], 'contracts[].period.durationInDays'
                acp = aw.get('contractPeriod') or {}
                if acp.get('startDate') and not start: start, start_src = to_date(acp['startDate']), 'awards[].contractPeriod.startDate'
                if acp.get('endDate') and not end: end, end_src = to_date(acp['endDate']), 'awards[].contractPeriod.endDate'
                if acp.get('durationInDays') and not duration_days: duration_days, dur_src = acp['durationInDays'], 'awards[].contractPeriod.durationInDays'
                for lid in aw.get('relatedLots') or []:
                    lcp = (lots.get(lid) or {}).get('contractPeriod') or {}
                    if lcp.get('startDate') and not start: start, start_src = to_date(lcp['startDate']), f'tender.lots[{lid}].contractPeriod.startDate'
                    if lcp.get('endDate') and not end: end, end_src = to_date(lcp['endDate']), f'tender.lots[{lid}].contractPeriod.endDate'
                    if lcp.get('durationInDays') and not duration_days: duration_days, dur_src = lcp['durationInDays'], f'tender.lots[{lid}].contractPeriod.durationInDays'
                tcp = tender.get('contractPeriod') or {}
                if tcp.get('startDate') and not start: start, start_src = to_date(tcp['startDate']), 'tender.contractPeriod.startDate'
                if tcp.get('endDate') and not end: end, end_src = to_date(tcp['endDate']), 'tender.contractPeriod.endDate'
                if tcp.get('durationInDays') and not duration_days: duration_days, dur_src = tcp['durationInDays'], 'tender.contractPeriod.durationInDays'
                fwp = fw.get('period') or {}
                dps_note = ''
                if key[0] == 'dps' and fwp.get('endDate'):
                    # admission to a dynamic market / open framework: the instrument's own period applies
                    if not end: end, end_src = to_date(fwp['endDate']), 'tender.techniques.frameworkAgreement.period.endDate'
                    if not start and fwp.get('startDate'): start, start_src = to_date(fwp['startDate']), 'tender.techniques.frameworkAgreement.period.startDate'
                    dps_note = (f' [dynamic market / open framework admission: supplier appears on {len(members)} lot award(s) of this '
                                f'process; no call-off contract value in notice]')
                signed = next((to_date(c.get('dateSigned')) for c in cons if c.get('dateSigned')), None)
                award_date = to_date(aw.get('date'))
                anchor = start or signed or award_date
                anchor_src = start_src if start else ('contracts[].dateSigned' if signed else ('awards[].date' if award_date else None))
                if end is not None:
                    if end < TODAY:
                        counts['excluded_end_before_today'] += 1
                        rv.write('\t'.join(['EXCLUDED_ended', '', d.get('ocid', ''), aw.get('id', ''), vendor_party.get('name', ''), basis,
                                            addr_text(vendor_party.get('address')).replace('\n', ' '), str(start), str(end), '']) + '\n')
                        continue
                    if anchor and anchor > TODAY:
                        counts['excluded_start_after_today'] += 1; continue
                    status = 'ongoing'
                    status_basis = (f'{anchor_src} {anchor} <= 2026-10-25 <= {end_src} {end}' if anchor else f'no start/signed date; {end_src} {end} >= 2026-10-25') + dps_note
                elif duration_days and anchor:
                    try:
                        inferred_end = anchor + dt.timedelta(days=int(float(duration_days)))
                    except (TypeError, ValueError):
                        inferred_end = None
                    if inferred_end and inferred_end < TODAY:
                        counts['excluded_inferred_end_before_today'] += 1
                        rv.write('\t'.join(['EXCLUDED_inferred_ended', '', d.get('ocid', ''), aw.get('id', ''), vendor_party.get('name', ''), basis,
                                            addr_text(vendor_party.get('address')).replace('\n', ' '), str(anchor), f'~{inferred_end}', '']) + '\n')
                        continue
                    if anchor > TODAY:
                        counts['excluded_start_after_today'] += 1; continue
                    status = 'ongoing_inferred'
                    status_basis = (f'No explicit end date; {dur_src}={duration_days} days from {anchor_src} {anchor} gives inferred end '
                                    f'~{inferred_end} >= 2026-10-25')
                    end = inferred_end
                else:
                    if anchor and anchor > TODAY:
                        counts['excluded_start_after_today'] += 1; continue
                    status = 'end_date_unknown'
                    status_basis = f'No contract/award/lot/tender period end date or duration in the notice data; signed/award date {anchor} ({anchor_src})'
                # ---- ids / urls ----
                m = re.match(r'^(\d{6}-\d{4})', aw.get('id') or '')
                nids = notice_ids({'a': aw, 'c': cons})
                notice_id = m.group(1) if m else (nids[0] if nids else None)
                if not notice_id:
                    allids = notice_ids(d); notice_id = allids[-1] if allids else None
                record_url = f'https://www.find-tender.service.gov.uk/Notice/{notice_id}' if notice_id else None
                rid = f"uk_find_a_tender:{d.get('ocid')}:{aw.get('id')}"
                if key[0] == 'dps' or len(aw.get('suppliers') or []) > 1:
                    # multi-supplier award (framework lot / DPS): one record per Canadian supplier -> supplier id in record_id
                    rid = f"uk_find_a_tender:{d.get('ocid')}:{aw.get('id')}:{sid}" if key[0] != 'dps' else f"uk_find_a_tender:{d.get('ocid')}:{sid}"
                if rid in seen: rid = f'{rid}:{sid}'
                seen.add(rid)
                vaddr = vendor_party.get('address') or {}
                vendor_ids = {'fts_party_id': vendor_party.get('id')}
                vid = vendor_party.get('identifier') or {}
                if vid.get('scheme') and vid.get('id'): vendor_ids[vid['scheme']] = vid['id']
                for ai in vendor_party.get('additionalIdentifiers') or []:
                    if ai.get('scheme') and ai.get('id'): vendor_ids[ai['scheme']] = ai['id']
                bid = buyer_party.get('identifier') or {}
                buyer_ids = {'fts_party_id': buyer_party.get('id')}
                if bid.get('scheme') and bid.get('id'): buyer_ids[bid['scheme']] = bid['id']
                btype = next((c.get('description') for c in ((buyer_party.get('details') or {}).get('classifications') or [])
                              if c.get('scheme') in ('UK_CA_TYPE', 'TED_CA_TYPE')), None)
                cls = tender.get('classification') or {}
                commodity = {}
                if cls.get('id'): commodity['cpv'] = cls['id']; commodity['cpv_description'] = cls.get('description')
                addl = [c.get('id') for c in (tender.get('additionalClassifications') or []) if c.get('id')]
                for it in aw.get('items') or []:
                    for c in it.get('additionalClassifications') or []:
                        if c.get('scheme') == 'CPV' and c.get('id') and c['id'] not in addl and c['id'] != cls.get('id'): addl.append(c['id'])
                if addl: commodity['cpv_additional'] = addl
                cval = next(((c.get('value') or {}) for c in cons if (c.get('value') or {}).get('amount') is not None), None)
                aval = aw.get('value') or {}
                value = cval or aval or {}
                vd = {}
                if cval: vd['contract_value'] = num(cval.get('amount'))
                if aval.get('amount') is not None: vd['award_value'] = num(aval.get('amount'))
                if (tender.get('value') or {}).get('amount') is not None: vd['tender_estimated_value'] = num(tender['value']['amount'])
                if cval and cval.get('amountGross') is not None: vd['contract_value_gross'] = num(cval.get('amountGross'))
                has_fw = bool(techniques.get('hasFrameworkAgreement') or fw)
                if key[0] == 'dps':
                    instrument = 'dynamic market / dynamic purchasing system admission'
                elif has_fw and len(aw.get('suppliers') or []) > 1:
                    instrument = 'framework agreement / multi-supplier award'
                elif has_fw:
                    instrument = 'framework agreement'
                else:
                    instrument = 'contract'
                if len(aw.get('suppliers') or []) > 1 and value.get('amount') is not None:
                    vd['value_note'] = f'value is the total for all {len(aw.get("suppliers") or [])} suppliers on this award'
                record = {
                    'record_id': rid,
                    'source': dict(SOURCE, record_url=record_url, retrieved_at=RETRIEVED_AT),
                    'status': status, 'status_basis': status_basis,
                    'contract': {
                        'identifiers': {'ocid': d.get('ocid'), 'award_id': aw.get('id'), 'contract_ids': [c.get('id') for c in cons],
                                        'notice_id': notice_id, 'all_notice_ids_in_process': notice_ids(d), 'tender_id': tender.get('id'),
                                        'related_lots': aw.get('relatedLots'), 'compiled_release_id': d.get('id'),
                                        'collapsed_duplicate_award_ids': dup_award_ids or None,
                                        'collapsed_duplicate_contract_ids': dup_contract_ids or None,
                                        'all_related_lots_for_supplier': sorted({l for m in members for l in (m[0].get('relatedLots') or [])}) if dup_award_ids else None},
                        'title': aw.get('title') or (cons[0].get('title') if cons else None) or tender.get('title'),
                        'description': tender.get('description') or aw.get('description'),
                        'instrument_type': instrument,
                        'procurement_method': tender.get('procurementMethod'), 'solicitation_procedure': tender.get('procurementMethodDetails'),
                        'commodity': commodity,
                        'value': num(value.get('amount')), 'currency': value.get('currency'),
                        'value_detail': vd,
                        'dates': {'published': iso_date(aw.get('datePublished') or next((x.get('datePublished') for c in cons for x in (c.get('documents') or [])), None) or d.get('date')),
                                  'signed': signed.isoformat() if signed else iso_date(aw.get('date')),
                                  'start': start.isoformat() if start else None, 'end': end.isoformat() if end else None,
                                  'amended_last': iso_date(d.get('date'))},
                        'related': {'award_notice_url': record_url,
                                    'ocds_release_package_url': f"https://www.find-tender.service.gov.uk/api/1.0/ocdsReleasePackages/{d.get('ocid')}",
                                    'all_suppliers_on_award': [s.get('name') for s in (aw.get('suppliers') or [])],
                                    'main_procurement_category': aw.get('mainProcurementCategory') or tender.get('mainProcurementCategory'),
                                    'legal_basis': (tender.get('legalBasis') or {}).get('id')},
                    },
                    'buyer': {'name': buyer_party.get('name') or buyer.get('name'), 'country': 'GB', 'type': btype,
                              'identifiers': buyer_ids, 'address': buyer_party.get('address') or {}, 'contact': buyer_party.get('contactPoint') or {}},
                    'vendor': {'name': vendor_party.get('name'), 'country': 'CA', 'country_basis': basis, 'country_conflict': conflict,
                               'identifiers': vendor_ids,
                               'address': {'line1': vaddr.get('streetAddress'), 'city': vaddr.get('locality'), 'region': vaddr.get('region'),
                                           'postal_code': vaddr.get('postalCode'), 'country': vaddr.get('countryName') or vaddr.get('country')},
                               'contact': vendor_party.get('contactPoint') or {}, 'details': vendor_party.get('details') or {}},
                    'raw': {'compiled_release': d, 'bulk_source': BULK_URL},
                }
                o.write(json.dumps(record, ensure_ascii=False) + '\n')
                counts[f'emitted_{status}'] += 1
                if conflict: counts['emitted_with_country_conflict'] += 1
                rv.write('\t'.join(['INCLUDED', status, d.get('ocid', ''), aw.get('id', ''), vendor_party.get('name', ''), basis,
                                    addr_text(vaddr).replace('\n', ' ').replace('\t', ' '), str(start or anchor), str(end), record_url or '']) + '\n')
    print(json.dumps(counts, indent=1))

if __name__ == '__main__':
    main()
