import json, collections
path='normalized/seao_quebec.jsonl'
TODAY='2026-10-25'
viol=collections.Counter(); n=0; checked=0
raw_keys=collections.Counter()
for line in open(path, encoding='utf-8'):
    n+=1
    if n%25: continue
    r=json.loads(line); checked+=1
    d=r['contract']['dates']
    if r['status']=='ongoing':
        if not (d['end'] and d['end']>=TODAY): viol['ongoing_end_bad']+=1
        if d['signed'] and d['signed']>TODAY: viol['ongoing_signed_future']+=1
        cs=r['raw']['ocds_supplier_contracts'] or []
        if not any((c.get('period') or {}).get('endDate','')[:10]==d['end'] and c.get('status') not in ('terminated','cancelled') for c in cs): viol['ongoing_end_not_in_raw']+=1
    else:
        if d['end']: viol['inferred_has_end']+=1
        if r['raw']['information_finale'] is not None: viol['inferred_has_closure']+=1
        cs=r['raw']['ocds_supplier_contracts'] or []
        if cs and all(c.get('status') in ('terminated','cancelled') for c in cs): viol['inferred_but_all_terminated']+=1
    if r['vendor']['country']!='CA': viol['vendor_not_CA']+=1
    if not r['source']['record_url'].startswith('https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId='): viol['url_pattern']+=1
    for k,v in r['raw'].items(): raw_keys[(k, v is not None)]+=1
    # schema shape
    for k in ('record_id','source','status','status_basis','contract','buyer','vendor','raw'):
        if k not in r: viol['missing_'+k]+=1
print('checked', checked, 'violations', dict(viol))
print('raw key presence', sorted(raw_keys.items()))
