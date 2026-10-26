import sqlite3, json, collections, re
xc = sqlite3.connect('downloads/seao_quebec/staging/seao_xml.sqlite')
jc = sqlite3.connect('downloads/seao_quebec/staging/seao_json.sqlite')
# overlap of numeroseao sets
xs = {r[0] for r in xc.execute('SELECT DISTINCT numeroseao FROM avis_rows')}
js = {r[0] for r in jc.execute('SELECT DISTINCT numeroseao FROM latest')}
print('xml numeroseao', len(xs), 'json', len(js), 'both', len(xs & js), 'json only', len(js - xs), 'xml only', len(xs - js))
# json-only: by max file order / contract presence
only = js - xs
cnt = collections.Counter(); yr=collections.Counter()
for ns in list(only)[:200000]:
    pass
rows = jc.execute('SELECT numeroseao, tags, json FROM latest').fetchall()
k=0
for ns, tags, j in rows:
    if ns in only:
        r=json.loads(j)
        cs=r.get('contracts') or []
        cnt[('has_contract' if cs else 'no_contract', int(ns)>=19000000)]+=1
        for c in cs:
            yr[(c.get('dateSigned') or '')[:4]]+=1
print('json-only numeroseao:', cnt.most_common()); print('json-only contract signed years', sorted(yr.items()))
# For numeroseao in both: compare xml awarded suppliers vs json contracts count for a sample of 2023 ones
mism=0; tot=0; ex=[]
for ns, tags, j in rows[:400000]:
    if ns in xs and tot<3000:
        r=json.loads(j); cs=r.get('contracts') or []
        if not cs: continue
        a=xc.execute('SELECT json FROM avis_rows WHERE numeroseao=? ORDER BY ord DESC LIMIT 1',(ns,)).fetchone()
        o=json.loads(a[0]); aw=[f for f in o.get('fournisseurs',[]) if f.get('adjudicataire')=='1']
        tot+=1
        if len(aw)!=len(cs):
            mism+=1
            if len(ex)<5: ex.append((ns, len(aw), len(cs), [f.get('nomorganisation')[:20] for f in aw], [(c.get('status'), c.get('value',{}).get('amount')) for c in cs], r['tag']))
print('both: sample', tot, 'count mismatch xml awarded vs json contracts', mism); 
for e in ex: print(e)
