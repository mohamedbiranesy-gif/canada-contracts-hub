import sqlite3, json, collections, sys
con = sqlite3.connect('downloads/seao_quebec/staging/seao_xml.sqlite')
print('distinct numeroseao in avis_rows', con.execute('SELECT COUNT(DISTINCT numeroseao) FROM avis_rows').fetchone())
print('appearances per numeroseao', con.execute('SELECT n, COUNT(*) FROM (SELECT numeroseao, COUNT(*) n FROM avis_rows GROUP BY numeroseao) GROUP BY n ORDER BY n LIMIT 8').fetchall())
print('appearances in Avis (non-revision) per numeroseao', con.execute("SELECT n, COUNT(*) FROM (SELECT numeroseao, COUNT(*) n FROM avis_rows WHERE kind='Avis' GROUP BY numeroseao) GROUP BY n ORDER BY n LIMIT 6").fetchall())
print('numeroseao only in AvisRevisions (never in Avis)', con.execute("SELECT COUNT(*) FROM (SELECT numeroseao FROM avis_rows GROUP BY numeroseao HAVING SUM(kind='Avis')=0)").fetchone())
print('contrat rows per numeroseao', con.execute('SELECT n, COUNT(*) FROM (SELECT numeroseao, COUNT(*) n FROM contrat_rows GROUP BY numeroseao) GROUP BY n ORDER BY n LIMIT 8').fetchall())
print('contrat numeroseao without any avis row', con.execute('SELECT COUNT(DISTINCT c.numeroseao) FROM contrat_rows c LEFT JOIN avis_rows a ON a.numeroseao=c.numeroseao WHERE a.numeroseao IS NULL').fetchone())
print('depense numeroseao without any avis row', con.execute('SELECT COUNT(DISTINCT c.numeroseao) FROM depense_rows c LEFT JOIN avis_rows a ON a.numeroseao=c.numeroseao WHERE a.numeroseao IS NULL').fetchone())
# sample: an avis appearing 3+ times in Avis non-revision
rows = con.execute("SELECT numeroseao FROM avis_rows WHERE kind='Avis' GROUP BY numeroseao HAVING COUNT(*)>=3 LIMIT 3").fetchall()
for (ns,) in rows:
    print('=== numeroseao', ns)
    for ordv, src, kind, js in con.execute('SELECT ord, src, kind, json FROM avis_rows WHERE numeroseao=? ORDER BY ord', (ns,)):
        o = json.loads(js)
        print(' ', ordv, kind, src.split('/')[-1], o.get('dateadjudication'), o.get('datesaisieadjudication'), len(o.get('fournisseurs',[])), [(f.get('nomorganisation')[:25], f.get('adjudicataire'), f.get('montantcontrat')) for f in o.get('fournisseurs',[]) if f.get('adjudicataire')=='1'])
# multiple awarded suppliers for same avis; same supplier twice
multi=collections.Counter(); dup=0; tot=0
for (js,) in con.execute("SELECT json FROM avis_rows WHERE kind='Avis' AND ord >= 202301010"):
    o=json.loads(js); tot+=1
    aw=[f for f in o.get('fournisseurs',[]) if f.get('adjudicataire')=='1']
    multi[len(aw)]+=1
    names=collections.Counter((f.get('nomorganisation') or '').strip().lower() for f in aw)
    if any(v>1 for v in names.values()): dup+=1
print('2023+ Avis rows', tot, 'awarded suppliers per avis', sorted(multi.items())[:10], 'rows with same supplier awarded twice', dup)
