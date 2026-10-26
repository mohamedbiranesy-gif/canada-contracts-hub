import sqlite3, json
jc = sqlite3.connect('downloads/seao_quebec/staging/seao_json.sqlite')
for ocid in ('ocds-ec9k95-20000032','ocds-ec9k95-20000116','ocds-ec9k95-20000177'):
    print('=====', ocid)
    for fo, src, rid, rd, tags, js in jc.execute('SELECT file_order, src, release_id, release_date, tags, json FROM json_releases WHERE ocid=? ORDER BY file_order, release_date', (ocid,)):
        r=json.loads(js)
        print(' ', src, rid, rd[:10], tags, 'tender.status', r['tender'].get('status'), 'awards', [(a['id'], a['status'], (a.get('suppliers') or [{}])[0].get('name','')[:18], a.get('value',{}).get('amount')) for a in r.get('awards') or []], 'contracts', [(c['id'], c['status'], (c.get('period') or {}).get('endDate','')[:10]) for c in r.get('contracts') or []])
