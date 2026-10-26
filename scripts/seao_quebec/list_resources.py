import json, sys, re, collections
d=json.load(open(sys.argv[1]))
r=d['result']
res=r['resources']
fmt=collections.Counter(x.get('format') for x in res)
print('formats',fmt)
# classify by name
pat=collections.Counter()
rows=[]
for x in res:
    n=x.get('name') or ''
    url=x.get('url')
    fn=url.rsplit('/',1)[-1]
    kind=re.sub(r'\d+','#',fn)
    pat[kind]+=1
    rows.append((x.get('format'),n,x.get('size'),x.get('last_modified') or x.get('created'),url,fn,x.get('description','')[:100]))
print('name patterns')
for k,v in pat.most_common(): print(' ',v,k)
print()
print('--- non-standard resources (docs etc) ---')
for row in rows:
    if not re.match(r'^(hebdo|mensuel)_\d+_\d+\.(json|xml)$', row[5], re.I):
        print(row)
print()
# totals by format
tot=collections.defaultdict(int)
for x in res:
    tot[x.get('format')]+= int(x.get('size') or 0)
print('total sizes', {k:f'{v/1e9:.2f} GB' for k,v in tot.items()})
# year range of xml
xmls=sorted(x['url'].rsplit('/',1)[-1] for x in res if x['url'].lower().endswith('.xml'))
print('xml count',len(xmls)); print('first',xmls[:3]); print('last',xmls[-3:])
jsons=sorted(x['url'].rsplit('/',1)[-1] for x in res if x['url'].lower().endswith('.json'))
print('json count',len(jsons)); print('first',jsons[:3]); print('last',jsons[-3:])
# dump a tsv of all resources
with open(sys.argv[2],'w') as f:
    for x in res:
        f.write('\t'.join(str(v) for v in [x.get('format'),x.get('name'),x.get('size'),x.get('last_modified') or x.get('created'),x.get('url')])+'\n')
