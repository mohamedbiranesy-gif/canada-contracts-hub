import sqlite3, json, collections
xc = sqlite3.connect('downloads/seao_quebec/staging/seao_xml.sqlite')
jc = sqlite3.connect('downloads/seao_quebec/staging/seao_json.sqlite')
xs = {r[0] for r in xc.execute('SELECT DISTINCT numeroseao FROM avis_rows')}
cnt=collections.Counter(); ex=[]
for ns, tags, js in jc.execute('SELECT numeroseao, tags, json FROM latest'):
    if ns in xs: continue
    r=json.loads(js)
    aw=r.get('awards') or []; cs=r.get('contracts') or []
    if aw and not cs:
        new = int(ns)>=19000000
        cnt[(new, tags, tuple(sorted({a.get('status') for a in aw})))]+=1
        if len(ex)<5 and new: ex.append((ns, r['id'], r.get('_source_file'), tags, [(a.get('id'), a.get('status'), (a.get('date') or '')[:10], (a.get('suppliers') or [{}])[0].get('name','')[:20]) for a in aw]))
print('JSON-only notices with awards but no contracts:', sum(cnt.values()))
for k,v in cnt.most_common(15): print(v,k)
for e in ex: print(e)
