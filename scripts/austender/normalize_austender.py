#!/usr/bin/env python3
"""Normalize AusTender OCDS releases (crawled pages from crawl_contract_end.py) into the shared
record shape: one record per Contract Notice (CN) whose supplier address countryName is Canada
and whose contract period covers the reference date. All releases for the CN (original +
amendments) are kept under raw.rows; normalized values come from the latest release.

Usage: python3 -I normalize_austender.py <pages_dir> <out.jsonl> <review.tsv> [unspsc.xlsx]
"""
import json, glob, os, re, sys, collections, datetime as dt
from zoneinfo import ZoneInfo

TODAY = dt.date(2026, 10, 25)
AEST = ZoneInfo('Australia/Sydney')
SOURCE = {
    'key': 'austender',
    'name': 'AusTender Contract Notices (OCDS API)',
    'publisher': 'Department of Finance (Australian Government)',
    'dataset_url': 'https://api.tenders.gov.au/ocds/findByDates/contractEnd/{from}/{to} (docs: https://github.com/austender/austender-ocds-api)',
}

def local_date(iso):
    """AusTender stores dates as UTC instants of local midnight (e.g. 2026-10-25T13:00:00Z = 26 Oct 00:00 AEDT).
    Convert to the Australian local calendar date."""
    if not iso:
        return None
    try:
        t = dt.datetime.fromisoformat(iso.replace('Z', '+00:00'))
    except ValueError:
        return None
    return t.astimezone(AEST).date()

def num(v):
    try:
        return float(v) if v not in (None, '') else None
    except (TypeError, ValueError):
        return None

def uuid_from_award(award_id):
    m = re.search(r'-([0-9a-f]{32})$', award_id or '')
    if not m:
        return None
    h = m.group(1)
    return f'{h[0:8]}-{h[8:12]}-{h[12:16]}-{h[16:20]}-{h[20:32]}'

def load_unspsc(path):
    out = {}
    if not path or not os.path.exists(path):
        return out
    try:
        import pandas as pd
        x = pd.read_excel(path, sheet_name=None, dtype=str, header=None)
        for sheet in x.values():
            for _, row in sheet.iterrows():
                code, title = str(row.iloc[0]).strip(), str(row.iloc[1]).strip()
                if re.fullmatch(r'\d{8}', code):
                    out[code] = title
    except Exception as e:
        print('unspsc load failed', e, file=sys.stderr)
    return out

def main():
    pages_dir, out, review = sys.argv[1], sys.argv[2], sys.argv[3]
    unspsc = load_unspsc(sys.argv[4] if len(sys.argv) > 4 else None)
    retrieved_at = None
    by_cn = collections.defaultdict(list)
    counts = collections.Counter()
    for fn in sorted(glob.glob(os.path.join(pages_dir, '*.json'))):
        try:
            d = json.load(open(fn))
        except Exception as e:
            print('bad page', fn, e, file=sys.stderr); continue
        for r in d.get('releases', []):
            counts['releases'] += 1
            cn = (r.get('contracts') or [{}])[0].get('id')
            if not cn:
                counts['release_without_contract_id'] += 1; continue
            by_cn[cn].append(r)
    retrieved_at = dt.datetime.fromtimestamp(os.path.getmtime(sorted(glob.glob(os.path.join(pages_dir, '*.json')))[-1]), dt.timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')
    counts['distinct_cns'] = len(by_cn)
    with open(out, 'w', encoding='utf-8') as o, open(review, 'w', encoding='utf-8') as rv:
        rv.write('decision\tstatus\tcn\tsupplier\tcountry\tcity\tstart\tend\tvalue\trecord_url\n')
        for cn, rels in sorted(by_cn.items()):
            # order: original contract release first, then amendments by their sequence number (A1, A2, ...);
            # release dates are unreliable for ordering (re-published amendments share one timestamp)
            def amend_no(r):
                ams = (r.get('contracts') or [{}])[0].get('amendments') or []
                nums = [int(m.group(1)) for a in ams for m in [re.search(r'-A(\d+)$', a.get('id') or '')] if m]
                return max(nums) if nums else (0 if 'contractAmendment' not in (r.get('tag') or []) else 999)
            rels.sort(key=lambda r: (amend_no(r), r.get('date') or ''))
            latest = rels[-1]
            sup = [p for p in latest.get('parties', []) if 'supplier' in (p.get('roles') or [])]
            if not sup:
                counts['cn_without_supplier_party'] += 1; continue
            country = (sup[0].get('address') or {}).get('countryName') or ''
            countries_all = {((p.get('address') or {}).get('countryName') or '').strip().upper()
                             for r in rels for p in r.get('parties', []) if 'supplier' in (p.get('roles') or [])}
            country_basis = 'parties[role=supplier].address.countryName (latest release)'
            if country.strip().upper() != 'CANADA':
                if 'CANADA' in countries_all:
                    # supplier country differs between the original CN release and an amendment release; the
                    # original/parent CN record says Canada -> keep, flag the conflict
                    orig_sup = next((p for p in rels[0].get('parties', []) if 'supplier' in (p.get('roles') or [])), sup[0])
                    country_basis = (f'CONFLICT: original CN release parties[role=supplier].address.countryName = '
                                     f'{(orig_sup.get("address") or {}).get("countryName")!r} (address {orig_sup.get("address")}), but the latest '
                                     f'amendment release says {country!r}; kept because the parent CN record states Canada')
                    sup = [orig_sup]
                    counts['cn_canadian_with_country_conflict'] += 1
                else:
                    counts['cn_non_canadian'] += 1; continue
            counts['cn_canadian'] += 1
            con = latest['contracts'][0]
            per = con.get('period') or {}
            start = local_date(per.get('startDate')); end = local_date(per.get('endDate'))
            signed = local_date(con.get('dateSigned'))
            if end is None:
                status, basis = 'end_date_unknown', 'contracts[0].period.endDate missing in latest release'
            elif end < TODAY:
                counts['excluded_end_before_today'] += 1
                rv.write('\t'.join(['EXCLUDED_ended', '', cn, sup[0].get('name', ''), country, str((sup[0].get('address') or {}).get('locality')), str(start), str(end), str(con.get('value', {}).get('amount')), '']) + '\n')
                continue
            elif start and start > TODAY:
                counts['excluded_start_after_today'] += 1
                rv.write('\t'.join(['EXCLUDED_future_start', '', cn, sup[0].get('name', ''), country, str((sup[0].get('address') or {}).get('locality')), str(start), str(end), str(con.get('value', {}).get('amount')), '']) + '\n')
                continue
            else:
                status = 'ongoing'
                basis = (f'contracts[0].period.startDate {per.get("startDate")} (= {start} Australia/Sydney) <= 2026-10-25 <= '
                         f'contracts[0].period.endDate {per.get("endDate")} (= {end} Australia/Sydney); latest release tag {latest.get("tag")}')
            if con.get('status') and con.get('status') != 'active':
                basis += f'; NOTE contract status = {con.get("status")}'
            uuid = uuid_from_award((latest.get('awards') or [{}])[0].get('id'))
            record_url = f'https://www.tenders.gov.au/Cn/Show/{uuid}' if uuid else None
            proc = latest.get('parties', [])
            buyer = next((p for p in proc if 'procuringEntity' in (p.get('roles') or []) or 'buyer' in (p.get('roles') or [])), {})
            tender = latest.get('tender') or {}
            saddr = sup[0].get('address') or {}
            sup_ids = {}
            for ai in sup[0].get('additionalIdentifiers') or []:
                if ai.get('scheme') and ai.get('id'): sup_ids[ai['scheme']] = ai['id']
            sup_ids['austender_party_id'] = sup[0].get('id')
            buyer_ids = {'austender_party_id': buyer.get('id')}
            for ai in buyer.get('additionalIdentifiers') or []:
                if ai.get('scheme') and ai.get('id'): buyer_ids[ai['scheme']] = ai['id']
            codes = [(it.get('classification') or {}).get('id') for it in con.get('items') or [] if (it.get('classification') or {}).get('id')]
            commodity = {}
            if codes:
                commodity['unspsc'] = codes[0]; commodity['unspsc_description'] = unspsc.get(codes[0])
                if len(codes) > 1: commodity['unspsc_additional'] = codes[1:]
            amendments = []
            for r in rels:
                c0 = r['contracts'][0]
                for a in c0.get('amendments') or []:
                    amendments.append({'id': a.get('id'), 'release_id': a.get('releaseID'), 'release_date': r.get('date'),
                                       'value_after': num((c0.get('value') or {}).get('amount')),
                                       'end_after': local_date((c0.get('period') or {}).get('endDate')).isoformat() if (c0.get('period') or {}).get('endDate') else None})
            original = rels[0]['contracts'][0]
            value_detail = {'latest_value': num((con.get('value') or {}).get('amount')),
                            'original_value': num((original.get('value') or {}).get('amount'))}
            ids = {'cn_id': cn, 'ocid': latest.get('ocid'), 'release_id': latest.get('id'), 'award_id': (latest.get('awards') or [{}])[0].get('id'),
                   'agency_reference_id': con.get('title'), 'tender_id': tender.get('id'), 'austender_cn_uuid': uuid,
                   'amendment_ids': [a['id'] for a in amendments] or None}
            for k in ('atmId', 'sonId', 'ATM ID', 'SON ID'):
                if tender.get(k): ids[k] = tender[k]
            rec = {
                'record_id': f'austender:{cn}',
                'source': dict(SOURCE, record_url=record_url, retrieved_at=retrieved_at),
                'status': status, 'status_basis': basis,
                'contract': {
                    'identifiers': ids,
                    'title': con.get('description'), 'description': con.get('description'),
                    'instrument_type': 'contract notice (contract)',
                    'procurement_method': tender.get('procurementMethodDetails') or tender.get('procurementMethod'),
                    'solicitation_procedure': tender.get('procurementMethod'),
                    'commodity': commodity,
                    'value': num((con.get('value') or {}).get('amount')), 'currency': (con.get('value') or {}).get('currency') or 'AUD',
                    'value_detail': value_detail,
                    'dates': {'published': local_date(rels[0].get('date')).isoformat() if rels[0].get('date') else None,
                              'signed': signed.isoformat() if signed else None,
                              'start': start.isoformat() if start else None, 'end': end.isoformat() if end else None,
                              'amended_last': local_date(latest.get('date')).isoformat() if len(rels) > 1 and latest.get('date') else None},
                    'related': {'ocds_record_url': f'https://api.tenders.gov.au/ocds/findById/{cn}',
                                'limited_tender_exempt': tender.get('limitedTenderExempt'),
                                'limited_tender_reason': tender.get('limitedTenderReason'), 'exemption': tender.get('exemption'),
                                'amendments': amendments or None},
                },
                'buyer': {'name': buyer.get('name'), 'country': 'AU', 'type': 'Australian Government entity (AusTender reporting agency)',
                          'identifiers': buyer_ids, 'address': buyer.get('address') or {}, 'contact': buyer.get('contactPoint') or {}},
                'vendor': {'name': sup[0].get('name'), 'country': 'CA', 'country_basis': country_basis,
                           'identifiers': sup_ids,
                           'address': {'line1': saddr.get('streetAddress'), 'city': saddr.get('locality'), 'region': saddr.get('region'),
                                       'postal_code': saddr.get('postalCode'), 'country': saddr.get('countryName')},
                           'contact': sup[0].get('contactPoint') or {}},
                'raw': {'rows': rels, 'row_count': len(rels), 'note': 'rows = every OCDS release for this CN returned by the contractEnd index (original contract release first, then contractAmendment releases in amendment-number order A1, A2, ...)'},
            }
            o.write(json.dumps(rec, ensure_ascii=False) + '\n')
            counts[f'emitted_{status}'] += 1
            rv.write('\t'.join(['INCLUDED', status, cn, sup[0].get('name', ''), country, str(saddr.get('locality')), str(start), str(end), str((con.get('value') or {}).get('amount')), record_url or '']) + '\n')
    print(json.dumps(counts, indent=1))

if __name__ == '__main__':
    main()
