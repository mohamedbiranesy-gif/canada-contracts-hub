import sys, json, collections, ijson, re
# compare the same ocid across two files; look at pending contracts; ocid numeric ranges
f1, f2 = sys.argv[1], sys.argv[2]
def load(path):
    d={}
    with open(path,'rb') as f:
        for rel in ijson.items(f,'releases.item', use_float=True):
            d.setdefault(rel['ocid'],[]).append(rel)
    return d
a=load(f1); b=load(f2)
common=[o for o in a if o in b]
print('ocids', len(a), len(b), 'common', len(common))
diff_contracts=0; shown=0
for o in common:
    ra=a[o][-1]; rb=b[o][-1]
    ca=ra.get('contracts') or []; cb=rb.get('contracts') or []
    if len(ca)!=len(cb) and shown<3:
        shown+=1; diff_contracts+=1
        print('DIFF', o, ra['date'][:10], ra['tag'], len(ra.get('awards') or []), len(ca), '->', rb['date'][:10], rb['tag'], len(rb.get('awards') or []), len(cb))
    elif len(ca)!=len(cb): diff_contracts+=1
print('common with different contract counts', diff_contracts)
# within-file multiple releases for same ocid
mult=sum(1 for v in b.values() if len(v)>1); print('ocids with >1 release in file2', mult)
# pending
k=0
for o,rels in b.items():
    for r in rels:
        for c in r.get('contracts') or []:
            if c.get('status')=='pending' and k<3:
                k+=1; print('PENDING', json.dumps({x:r[x] for x in ('ocid','date','tag','awards','contracts')}, ensure_ascii=False)[:1200])
nums=[int(o.rsplit('-',1)[1]) for o in b]
print('ocid numeric min/max', min(nums), max(nums))
old=[o for o in b if int(o.rsplit('-',1)[1])<1900000]
print('ocids with numeroseao<1.9M (XML-era style) in file2:', len(old), old[:5])
# what tags do old ones have
print(collections.Counter(tuple(b[o][-1]['tag']) for o in old).most_common(10))
