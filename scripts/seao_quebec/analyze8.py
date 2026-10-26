import sqlite3, json, collections
xc = sqlite3.connect('downloads/seao_quebec/staging/seao_xml.sqlite')
jc = sqlite3.connect('downloads/seao_quebec/staging/seao_json.sqlite')
cnt=collections.Counter(); ex=collections.defaultdict(list)
closed=set(r[0] for r in xc.execute('SELECT DISTINCT numeroseao FROM contrat_rows'))
n=0
for ns, tags, js in jc.execute("SELECT numeroseao, tags, json FROM latest WHERE numeroseao < '19000000'"):
    r=json.loads(js)
    if r.get('contracts'): continue
    a=xc.execute("SELECT json FROM avis_rows WHERE numeroseao=? ORDER BY ord DESC LIMIT 1",(ns,)).fetchone()
    if not a: continue
    o=json.loads(a[0]); aw=[f for f in o.get('fournisseurs',[]) if f.get('adjudicataire')=='1']
    if not aw: continue
    n+=1
    hist=jc.execute('SELECT COUNT(*), SUM(json LIKE \'%"contracts"%\') FROM json_releases WHERE ocid=?',(r['ocid'],)).fetchone()
    key=(tags, 'xml_closed' if ns in closed else 'xml_open', 'had_contracts_before' if hist[1] else 'never_had_contracts', (r.get('tender') or {}).get('status'))
    cnt[key]+=1
    if len(ex[key])<2: ex[key].append((ns, r['id'], r.get('_source_file'), [f['nomorganisation'][:25] for f in aw], [ (p['name'][:20], p['roles']) for p in r.get('parties',[]) if 'buyer' not in p['roles']][:3], ((r.get('tender') or {}).get('documents') or [{}])[0].get('url','')[-40:]))
print('XML-awarded notices whose latest JSON release has no contracts:', n)
for k,v in cnt.most_common(): print(v,k)
print()
for k,v in ex.items():
    print(k); 
    for e in v: print('   ',e)
