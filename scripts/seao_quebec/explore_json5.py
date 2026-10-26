import sys, json, collections, ijson, re
path=sys.argv[1]
k=0; idpat=collections.Counter(); id_vs_date=collections.Counter()
old_end=collections.Counter()
with open(path,'rb') as f:
    for rel in ijson.items(f,'releases.item', use_float=True):
        rid=rel['id']; idpat[re.sub(r'\d','9',rid)]+=1
        d=rel['date'].replace('-','').replace('T','').replace(':','')[:14]
        id_vs_date[('id>=date' if rid>=d[:len(rid)] else 'id<date')]+=1
        n=int(rel['ocid'].rsplit('-',1)[1])
        if n<1900000:
            for c in rel.get('contracts') or []:
                old_end[(c.get('status'), 'endDate' in (c.get('period') or {}))]+=1
            if k<2 and rel.get('contracts') and any(c.get('status')=='active' for c in rel['contracts']):
                k+=1; print(json.dumps(rel, ensure_ascii=False)[:3500]); print()
print('release id patterns', idpat.most_common(5))
print('id vs date', id_vs_date)
print('old-ocid contracts (status, has endDate)', old_end)
