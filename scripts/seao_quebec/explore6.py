import sys, json, collections, ijson, re
from lxml import etree
# 1. pending contracts + procurementMethodDetails mapping in a monthly JSON
path='downloads/seao_quebec/json/mensuel_20250301_20250331.json'
pmd=collections.Counter(); k=0
with open(path,'rb') as f:
    for rel in ijson.items(f,'releases.item', use_float=True):
        t=rel.get('tender') or {}
        pmd[(t.get('procurementMethod'), t.get('procurementMethodDetails'))]+=1
        for c in rel.get('contracts') or []:
            if c.get('status')=='pending' and k<2:
                k+=1; print('PENDING', json.dumps({x:rel.get(x) for x in ('ocid','date','tag','awards','contracts')}, ensure_ascii=False)[:900]); print()
print('procurementMethod details', pmd.most_common(20))
# 5. check 304462 in mensuel_202405 json
path='downloads/seao_quebec/json/mensuel_20240501_20240531.json'
with open(path,'rb') as f:
    for rel in ijson.items(f,'releases.item', use_float=True):
        if rel['ocid'].endswith('-304462'):
            print('304462 JSON:', json.dumps({x:rel.get(x) for x in ('id','date','tag','awards','contracts')}, ensure_ascii=False)[:1500]); break
