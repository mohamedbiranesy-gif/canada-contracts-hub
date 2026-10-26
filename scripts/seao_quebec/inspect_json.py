"""Inspect a weekly/monthly OCDS-like JSON: distinct key paths, tags, statuses, sample releases."""
import sys, json, collections, ijson, decimal
class E(json.JSONEncoder):
    def default(self,o):
        if isinstance(o, decimal.Decimal): return float(o)
        return super().default(o)
path = sys.argv[1]
paths = collections.Counter()
tags = collections.Counter()
cstat = collections.Counter(); astat = collections.Counter(); tstat=collections.Counter()
enddate_present = collections.Counter()
samples = {}
n=0
def walk(o, prefix):
    if isinstance(o, dict):
        for k,v in o.items():
            walk(v, prefix+'/'+k)
    elif isinstance(o, list):
        paths[prefix+'[]'] += 1
        for v in o: walk(v, prefix+'[]')
    else:
        paths[prefix] += 1
with open(path,'rb') as f:
    for rel in ijson.items(f, 'releases.item'):
        n+=1
        walk(rel, '')
        for t in rel.get('tag',[]): tags[t]+=1
        for c in rel.get('contracts',[]) or []:
            cstat[c.get('status')]+=1
            per = c.get('period') or {}
            enddate_present[('endDate' in per, 'startDate' in per, c.get('status'))]+=1
        for a in rel.get('awards',[]) or []:
            astat[a.get('status')]+=1
        tstat[(rel.get('tender') or {}).get('status')]+=1
        key = tuple(sorted(rel.get('tag',[])))
        if key not in samples: samples[key]=rel
print('releases', n)
print('tags', tags)
print('tender status', tstat)
print('award status', astat)
print('contract status', cstat)
print('contract period endDate/startDate presence by status', enddate_present)
print('--- paths ---')
for p,c in sorted(paths.items()): print(c, p)
print('--- samples ---')
for k,v in samples.items():
    print('=== tag', k)
    print(json.dumps(v, ensure_ascii=False, indent=1, cls=E)[:7000])
