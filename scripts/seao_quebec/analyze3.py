import sqlite3, json, collections, re
xc = sqlite3.connect('downloads/seao_quebec/staging/seao_xml.sqlite')
# 'CA' pays rows: province distribution
prov=collections.Counter(); pc=collections.Counter()
CAPROV={'AB','BC','PE','MB','NB','NS','ON','QC','SK','NF','NL','NT','YT','NU','PQ'}
for (js,) in xc.execute("""SELECT json FROM avis_rows WHERE ord >= 201801010 AND json LIKE '%"pays": "CA"%'"""):
    o=json.loads(js)
    for f in o.get('fournisseurs',[]):
        if f.get('adjudicataire')=='1' and f.get('pays')=='CA':
            p=(f.get('province') or '').strip().upper(); prov[p]+=1
            cp=(f.get('codepostal') or '').strip().upper().replace(' ','')
            pc[('CAprov' if p in CAPROV else 'other', bool(re.match(r'^[A-Z]\d[A-Z]\d[A-Z]\d$', cp)))]+=1
print("pays=CA awarded: province", prov.most_common(12)); print(pc)
jc = sqlite3.connect('downloads/seao_quebec/staging/seao_json.sqlite')
# release redundancy: for a sample of ocids with >=4 releases, how many distinct versions (ignoring id/date/tag/_source_file)?
dist=collections.Counter(); drop=0; n=0
for (ocid,) in jc.execute("SELECT ocid FROM json_releases GROUP BY ocid HAVING COUNT(*)>=3 LIMIT 600"):
    rels=[json.loads(js) for (js,) in jc.execute('SELECT json FROM json_releases WHERE ocid=? ORDER BY file_order, release_date', (ocid,))]
    vers=set(); prev_ids=None
    for r in rels:
        rr={k:v for k,v in r.items() if k not in ('id','date','tag','_source_file')}
        vers.add(json.dumps(rr, sort_keys=True, ensure_ascii=False))
        ids={c.get('id') for c in r.get('contracts') or []}
        if prev_ids is not None and not ids.issuperset(prev_ids): drop+=1
        prev_ids=ids
    dist[(len(rels), len(vers))]+=1; n+=1
print('sample ocids', n, '(n_releases, n_distinct_versions):', sorted(dist.items())[:25]); print('later release dropped a contract id:', drop)
