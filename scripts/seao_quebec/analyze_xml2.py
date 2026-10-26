import sqlite3, json, collections
con = sqlite3.connect('downloads/seao_quebec/staging/seao_xml.sqlite')
# How do contrat rows (closures) match suppliers? by neq? by name? multi-supplier avis
# Take avis with 2+ awarded suppliers and closure rows
k=0
for (ns,) in con.execute("SELECT numeroseao FROM contrat_rows GROUP BY numeroseao HAVING COUNT(*)>=2 LIMIT 400"):
    rows = con.execute('SELECT json FROM avis_rows WHERE numeroseao=? ORDER BY ord DESC LIMIT 1', (ns,)).fetchall()
    if not rows: continue
    o=json.loads(rows[0][0]); aw=[f for f in o.get('fournisseurs',[]) if f.get('adjudicataire')=='1']
    if len(aw)>=2:
        k+=1
        if k>4: break
        print('=== avis', ns, o.get('numero'), o.get('organisme')[:40], o.get('dateadjudication'))
        for f in aw: print('   AW', f.get('nomorganisation')[:40], f.get('neq'), f.get('montantcontrat'))
        for ordv, kind, neq, nom, js in con.execute('SELECT ord, kind, neq, nom, json FROM contrat_rows WHERE numeroseao=? ORDER BY ord', (ns,)):
            c=json.loads(js); print('   CL', kind, nom[:40], neq, c.get('datefinale'), c.get('datepublicationfinale'), c.get('montantfinal'))
# neq blank rate among awarded suppliers (recent years) and among closures
blank_aw=0; tot_aw=0
for (js,) in con.execute("SELECT json FROM avis_rows WHERE kind='Avis' AND ord >= 202201010"):
    o=json.loads(js)
    for f in o.get('fournisseurs',[]):
        if f.get('adjudicataire')=='1':
            tot_aw+=1; blank_aw += (not (f.get('neq') or '').strip())
print('awarded 2022+: ', tot_aw, 'blank neq', blank_aw)
print('closures blank neq', con.execute("SELECT COUNT(*) FROM contrat_rows WHERE TRIM(IFNULL(neq,''))=''").fetchone(), 'of', con.execute('SELECT COUNT(*) FROM contrat_rows').fetchone())
# closure with datefinale empty?
print('closures with empty datefinale', con.execute("SELECT COUNT(*) FROM contrat_rows WHERE json LIKE '%\"datefinale\": \"\"%'").fetchone())
# ContratsRevisions: do they revise an existing closure (same numeroseao in Contrats)?
print('ContratsRevisions rows', con.execute("SELECT COUNT(*) FROM contrat_rows WHERE kind='ContratsRevisions'").fetchone(), 'whose numeroseao has a Contrats row', con.execute("SELECT COUNT(*) FROM contrat_rows r WHERE kind='ContratsRevisions' AND EXISTS (SELECT 1 FROM contrat_rows c WHERE c.numeroseao=r.numeroseao AND c.kind='Contrats')").fetchone())
