import json, collections, sys
path='normalized/seao_quebec.jsonl'
ids=collections.Counter(); st=collections.Counter(); basis=collections.Counter(); url=collections.Counter(); n=0; bad=0
val_none=0; signed_none=0; title_none=0; neq_none=0; buyer_none=0; end_set=0; sizes=[]
year_status=collections.defaultdict(collections.Counter)
for line in open(path, encoding='utf-8'):
    n+=1
    try: r=json.loads(line)
    except Exception as e: bad+=1; continue
    ids[r['record_id']]+=1; st[r['status']]+=1
    basis[r['vendor']['country_basis'].split(':')[0] + ' / ' + ('CAN/CA code' if 'country field = "C' in r['vendor']['country_basis'] else ('province fallback' if 'province field' in r['vendor']['country_basis'] else ('postal fallback' if 'postal code' in r['vendor']['country_basis'] else 'other')))]+=1
    url[bool(r['source']['record_url'])]+=1
    if r['contract']['value'] is None: val_none+=1
    if r['contract']['dates']['signed'] is None: signed_none+=1
    if not r['contract']['title']: title_none+=1
    if not r['vendor']['identifiers'].get('neq'): neq_none+=1
    if not r['buyer']['name']: buyer_none+=1
    if r['contract']['dates']['end']: end_set+=1
    sizes.append(len(line))
print('lines', n, 'bad json', bad, 'unique ids', len(ids), 'dup ids', sum(1 for v in ids.values() if v>1))
print('status', st)
print('vendor basis', basis)
print('has record_url', url)
print('value None', val_none, 'signed None', signed_none, 'title None', title_none, 'neq None', neq_none, 'buyer None', buyer_none, 'end set', end_set)
sizes.sort(); print('line size median', sizes[len(sizes)//2], 'p99', sizes[int(len(sizes)*0.99)], 'max', sizes[-1])
dups=[k for k,v in ids.items() if v>1][:10]; print('dup examples', dups)
