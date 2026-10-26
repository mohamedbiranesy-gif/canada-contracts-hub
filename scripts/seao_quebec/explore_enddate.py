import sys, json, collections, ijson, decimal
path = sys.argv[1]
n=0; shown=0
future = collections.Counter(); byrel=collections.Counter()
multi = collections.defaultdict(list)
with open(path,'rb') as f:
    for rel in ijson.items(f, 'releases.item'):
        multi[rel['ocid']].append((rel['date'], tuple(rel.get('tag',[])), bool(rel.get('contracts')), bool(rel.get('awards')), rel.get('tender',{}).get('status')))
        for c in rel.get('contracts',[]) or []:
            per = c.get('period') or {}
            if c.get('status')=='active' and 'endDate' in per:
                n+=1
                ed = per['endDate'][:10]
                future[(ed >= '2026-10-25', tuple(rel.get('tag',[])))]+=1
                if shown < 12:
                    shown+=1
                    print(rel['ocid'], rel['date'][:10], rel.get('tag'), 'signed', c.get('dateSigned','')[:10], 'end', ed, 'award', [a.get('date','')[:10] for a in rel.get('awards',[])], 'tender', rel['tender'].get('id'), rel['tender'].get('title')[:50], 'amend', len(c.get('amendments',[]) or []))
print('active with endDate:', n)
print('future/past by tag', future)
# multi-release ocids
k=0
for ocid, lst in multi.items():
    if len(lst)>1:
        k+=1
        if k<=8: print(ocid, lst)
print('ocids with multiple releases', k, 'of', len(multi))
