import sys, json, collections, ijson
cn=collections.Counter(); idfmt=collections.Counter(); cstat=collections.Counter(); astat=collections.Counter()
nosupplier=0; n=0; multi_same_supplier=0
with open(sys.argv[1],'rb') as f:
    for rel in ijson.items(f,'releases.item', use_float=True):
        n+=1
        sup_ids={}
        for p in rel.get('parties',[]):
            if 'supplier' in p.get('roles',[]):
                cn[(p.get('address') or {}).get('countryName')]+=1
                pid=p.get('id','')
                import re
                idfmt[re.sub(r'\d','9',pid)[:12]]+=1
        seen=collections.Counter()
        for a in rel.get('awards') or []:
            astat[a.get('status')]+=1
            for s in a.get('suppliers') or []: seen[s.get('id')]+=1
            if not a.get('suppliers'): nosupplier+=1
        if any(v>1 for v in seen.values()): multi_same_supplier+=1
        for c in rel.get('contracts') or []: cstat[c.get('status')]+=1
print('releases',n); print('countryName',cn.most_common(40)); print('supplier id formats',idfmt.most_common(10)); print('award status',astat); print('contract status',cstat); print('awards without suppliers',nosupplier, 'releases with same supplier multiple awards', multi_same_supplier)
