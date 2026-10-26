#!/usr/bin/env python3
"""Scan an OCDS compiled-release JSONL(.gz) file and dump every release whose supplier
party address looks Canadian (any address field mentions Canada / a Canadian province +
postal code pattern). Writes candidates to <out>.jsonl with a `_match` annotation; also
prints summary counts. Broad on purpose - a second pass reviews/filters.

Usage: python3 -I scan_candidates.py <in.jsonl.gz> <out.jsonl>
"""
import gzip, json, re, sys, collections

CA_POSTAL = re.compile(r'\b[ABCEGHJ-NPRSTVXY]\d[ABCEGHJ-NPRSTV-Z][ ]?\d[ABCEGHJ-NPRSTV-Z]\d\b', re.I)
CANADA = re.compile(r'\bcanada\b', re.I)
PROVINCES = re.compile(r'\b(ontario|quebec|québec|british columbia|alberta|manitoba|saskatchewan|nova scotia|'
                       r'new brunswick|newfoundland|prince edward island|yukon|nunavut|northwest territories|'
                       r'ON|QC|BC|AB|MB|SK|NS|NB|NL|PE|PEI|YT|NU|NT)\b', re.I)
CA_CITIES = re.compile(r'\b(Toronto|Ottawa|Montr[ée]al|Vancouver|Calgary|Edmonton|Winnipeg|Mississauga|Kanata|Kitchener|Fredericton|'
                       r'Saskatoon|Regina|Burnaby|Markham|Gatineau|Laval|Oakville|Guelph|Halifax|Victoria|Waterloo|Hamilton|London|'
                       r'Brampton|Surrey|Richmond|Moncton|St\.? John\'?s|Saanichton|Repentigny|Boisbriand|Westmount|Coquitlam|Nanaimo)\b', re.I)
# UK-style false positives we must not count as a country mention
UK_CANADA_PLACES = re.compile(r'canada (square|water|house|place|wharf|street|road|gate|life|court|lane|way|close|'
                              r'avenue|dock|tower|yard|row|drive|walk|building|wood|quay|hill)', re.I)

def addr_text(a):
    if not isinstance(a, dict):
        return ''
    return ' | '.join(str(v) for v in a.values() if v)

def classify(party):
    a = party.get('address') or {}
    txt = addr_text(a)
    cn = (a.get('countryName') or '') + ' ' + (a.get('country') or '')
    reasons = []
    if re.search(r'\b(canada|ca)\b', cn, re.I):
        reasons.append('countryName/country field = Canada')
    stripped = UK_CANADA_PLACES.sub('', txt)
    if CANADA.search(stripped):
        reasons.append('address text mentions Canada')
    if CA_POSTAL.search(txt) and PROVINCES.search(txt):
        reasons.append('Canadian postal code pattern + province token')
    elif CA_POSTAL.search(txt) and CA_CITIES.search(txt):
        reasons.append('Canadian postal code pattern + Canadian city name')
    return reasons, txt

def main():
    src, out = sys.argv[1], sys.argv[2]
    n = nsup = 0; hits = 0
    reason_counts = collections.Counter()
    opener = gzip.open if src.endswith('.gz') else open
    with opener(src, 'rt', encoding='utf-8') as f, open(out, 'w', encoding='utf-8') as o:
        for line in f:
            n += 1
            try:
                d = json.loads(line)
            except Exception as e:
                print('bad line', n, e, file=sys.stderr); continue
            matches = []
            for p in d.get('parties', []) or []:
                roles = p.get('roles') or []
                if 'supplier' not in roles and 'tenderer' not in roles:
                    continue
                nsup += 1
                reasons, txt = classify(p)
                if reasons:
                    matches.append({'party_id': p.get('id'), 'name': p.get('name'), 'roles': roles,
                                    'address_text': txt, 'reasons': reasons})
            if matches:
                hits += 1
                for m in matches:
                    for r in m['reasons']:
                        reason_counts[r] += 1
                d['_match'] = matches
                o.write(json.dumps(d, ensure_ascii=False) + '\n')
            if n % 100000 == 0:
                print(f'{n} releases scanned, {hits} candidate releases', file=sys.stderr)
    print(json.dumps({'releases': n, 'supplier_parties': nsup, 'candidate_releases': hits,
                      'reasons': reason_counts}, indent=1))

if __name__ == '__main__':
    main()
