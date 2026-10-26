import sqlite3, json, collections
con = sqlite3.connect('downloads/seao_quebec/staging/seao_json.sqlite')
print('files', con.execute('SELECT COUNT(*), SUM(n_releases) FROM json_files').fetchone())
print('distinct ocid', con.execute('SELECT COUNT(DISTINCT ocid) FROM json_releases').fetchone())
print('releases per ocid', con.execute('SELECT n, COUNT(*) FROM (SELECT ocid, COUNT(*) n FROM json_releases GROUP BY ocid) GROUP BY n ORDER BY n LIMIT 10').fetchall())
# latest release per ocid: file_order desc, then release_date desc, then release_id desc
con.execute('DROP TABLE IF EXISTS latest')
con.execute('''CREATE TABLE latest AS SELECT ocid, numeroseao, release_id, release_date, file_order, src, tags, json FROM (
  SELECT *, ROW_NUMBER() OVER (PARTITION BY ocid ORDER BY file_order DESC, release_id DESC, release_date DESC) rn FROM json_releases) WHERE rn=1''')
con.execute('CREATE INDEX ix_latest ON latest(numeroseao)')
con.commit()
print('latest rows', con.execute('SELECT COUNT(*) FROM latest').fetchone())
st=collections.Counter(); yrs=collections.Counter(); cn=collections.Counter(); has_contract=0; n=0
for (js,) in con.execute('SELECT json FROM latest'):
    r=json.loads(js); n+=1
    cs=r.get('contracts') or []
    if cs: has_contract+=1
    for c in cs:
        ed=(c.get('period') or {}).get('endDate')
        s=c.get('status')
        key=(s, 'end>=today' if ed and ed[:10]>='2026-10-25' else ('end<today' if ed else 'noEnd'))
        st[key]+=1
        if s=='active':
            yrs[((c.get('dateSigned') or '')[:4], 'end>=today' if ed and ed[:10]>='2026-10-25' else ('end<today' if ed else 'noEnd'))]+=1
print('latest ocids with contracts', has_contract)
for k,v in sorted(st.items()): print(v,k)
print('active contracts by signed year / end class:')
for k,v in sorted(yrs.items()): print(' ',k,v)
