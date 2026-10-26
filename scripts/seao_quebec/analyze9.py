import sqlite3, json, collections
jc = sqlite3.connect('downloads/seao_quebec/staging/seao_json.sqlite')
for ocid in ('ocds-ec9k95-1002051','ocds-ec9k95-1267506','ocds-ec9k95-1012017'):
    print('=====', ocid)
    for fo, src, rid, rd, tags, js in jc.execute('SELECT file_order, src, release_id, release_date, tags, json FROM json_releases WHERE ocid=? ORDER BY file_order, release_id', (ocid,)):
        r=json.loads(js)
        print(' ', src, rid, rd[:10], tags, 'keys', [k for k in r.keys() if k in ('awards','contracts','bids')], 'awards', [(a.get('id'), a.get('status'), (a.get('suppliers') or [{}])[0].get('name','')[:18], (a.get('value') or {}).get('amount'), (a.get('date') or '')[:10]) for a in r.get('awards') or []], 'contracts', [(c.get('id'), c.get('status'), (c.get('period') or {}).get('endDate','')[:10]) for c in r.get('contracts') or []])
