import sys, json, collections, ijson, re
from lxml import etree
# 1. pending contracts in new-system data
path='downloads/seao_quebec/json/mensuel_20250301_20250331.json'
k=0; pend=collections.Counter()
with open(path,'rb') as f:
    for rel in ijson.items(f,'releases.item', use_float=True):
        for c in rel.get('contracts') or []:
            if c.get('status')=='pending':
                old=int(rel['ocid'].rsplit('-',1)[1])<19000000
                pend[(old, tuple(rel['tag']), 'endDate' in (c.get('period') or {}), (c.get('dateSigned') or '')[:4])]+=1
                if k<2 and not old:
                    k+=1; print('PENDING-NEW', json.dumps({x:rel.get(x) for x in ('ocid','date','tag','awards','contracts')}, ensure_ascii=False)[:1200]); print()
print('pending breakdown', pend.most_common(12))
# 2. old-system JSON (2022) documents url & neq presence
path='downloads/seao_quebec/json/mensuel_20220301_20220331.json'
urls=collections.Counter(); neq=collections.Counter(); n=0
with open(path,'rb') as f:
    for rel in ijson.items(f,'releases.item', use_float=True):
        n+=1
        for d in (rel.get('tender') or {}).get('documents') or []:
            urls[re.sub(r'ItemId=.*','ItemId=...', d.get('url',''))]+=1
        for p in rel.get('parties') or []:
            if 'supplier' in p.get('roles',[]):
                neq[('neq' in (p.get('details') or {}), re.sub(r'\d','9',p.get('id',''))[:6])]+=1
        if n==1: print('OLD-SYSTEM sample parties:', json.dumps(rel['parties'][:3], ensure_ascii=False)[:800])
print('2022 urls', urls.most_common(5)); print('2022 supplier neq/id', neq.most_common(6))
