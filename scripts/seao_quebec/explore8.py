import sys, json, collections, ijson, re
for path in sys.argv[1:]:
    st=collections.Counter(); ids=collections.Counter(); n=0; k=0; cn=collections.Counter(); amend=0
    with open(path,'rb') as f:
        for rel in ijson.items(f,'releases.item', use_float=True):
            n+=1
            ids[re.sub(r'\d','9',rel['id'])]+=1
            for c in rel.get('contracts') or []:
                st[(c.get('status'), 'endDate' in (c.get('period') or {}))]+=1
                if c.get('amendments'): amend+=1
            for p in rel.get('parties') or []:
                if 'supplier' in p.get('roles',[]): cn[(p.get('address') or {}).get('countryName')]+=1
            if k<1 and rel.get('contracts'):
                k+=1; print(path.rsplit('/',1)[1], json.dumps({x:rel.get(x) for x in ('ocid','id','date','tag','awards','contracts')}, ensure_ascii=False)[:700])
    print(path.rsplit('/',1)[1], 'releases', n, 'contract status/endDate', dict(st), 'id patterns', ids.most_common(3), 'amend', amend, 'supplier countries', cn.most_common(6))
