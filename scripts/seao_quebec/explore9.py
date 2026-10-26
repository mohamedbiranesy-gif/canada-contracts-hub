import sys, json, collections, ijson, re
path=sys.argv[1]
by=collections.Counter(); reldates=collections.Counter(); first=None; last=None
awy=collections.Counter()
with open(path,'rb') as f:
    for rel in ijson.items(f,'releases.item', use_float=True):
        n=int(rel['ocid'].rsplit('-',1)[1]); old = n<19000000
        rd=rel['date'][:7]; reldates[rd]+=1
        tags=tuple(rel['tag'])
        for c in rel.get('contracts') or []:
            by[(old, tags, c.get('status'), 'endDate' in (c.get('period') or {}))]+=1
            if c.get('status')=='active':
                awy[(old, (c.get('dateSigned') or '')[:4])]+=1
print('release date months', sorted(reldates.items())[:5], '...', sorted(reldates.items())[-5:])
for k,v in sorted(by.items(), key=lambda x:-x[1])[:25]: print(v,k)
print('active contracts by (old, signed year):', sorted(awy.items()))
