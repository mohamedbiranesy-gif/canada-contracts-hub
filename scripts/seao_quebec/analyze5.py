import sqlite3, json, collections
jc = sqlite3.connect('downloads/seao_quebec/staging/seao_json.sqlite')
k=0; kinds=collections.Counter()
for (ocid,) in jc.execute("SELECT ocid FROM latest WHERE file_order>=202501010 AND numeroseao>='19000000' LIMIT 3000"):
    rels=[(fo, src, json.loads(js)) for (fo, src, js) in jc.execute('SELECT file_order, src, json FROM json_releases WHERE ocid=? ORDER BY file_order, release_date', (ocid,))]
    prev=None
    for fo, src, r in rels:
        ids={c.get('id') for c in r.get('contracts') or []}
        if prev is not None and not ids.issuperset(prev[0]):
            new_sys_prev = prev[1] >= 202406010; new_sys_cur = fo >= 202406010
            kinds[(new_sys_prev, new_sys_cur, len(prev[0]), len(ids), tuple(r['tag']))]+=1
            if k<6 and new_sys_prev and new_sys_cur:
                k+=1
                print('===', ocid, 'prev', prev[2], sorted(prev[0]), [ (c['id'], c['status']) for c in prev[3]], '-> cur', src, r['tag'], sorted(ids), [(c['id'], c['status'], c.get('value',{}).get('amount')) for c in r.get('contracts') or []])
                print('    awards cur', [(a['id'], a['status'], a.get('suppliers',[{}])[0].get('name','')[:20]) for a in r.get('awards') or []])
        prev=(ids, fo, src, r.get('contracts') or [])
print(kinds.most_common(15))
