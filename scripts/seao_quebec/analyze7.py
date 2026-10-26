import sqlite3, json, collections
xc = sqlite3.connect('downloads/seao_quebec/staging/seao_xml.sqlite')
jc = sqlite3.connect('downloads/seao_quebec/staging/seao_json.sqlite')
# map XML type codes -> JSON procurementMethodDetails using notices present in both (recent)
m=collections.Counter(); k=0
for (ns, js) in xc.execute("SELECT numeroseao, json FROM avis_rows WHERE kind='Avis' AND ord>=202401010 LIMIT 40000"):
    o=json.loads(js)
    r=jc.execute('SELECT json FROM latest WHERE numeroseao=?',(ns,)).fetchone()
    if not r: continue
    t=json.loads(r[0]).get('tender',{})
    m[(o.get('type'), t.get('procurementMethod'), t.get('procurementMethodDetails'))]+=1
    k+=1
    if k>=6000: break
for key,v in m.most_common(25): print(v,key)
# nature/precision -> mainProcurementCategory/additionalProcurementCategories
m2=collections.Counter(); k=0
for (ns, js) in xc.execute("SELECT numeroseao, json FROM avis_rows WHERE kind='Avis' AND ord>=202401010 LIMIT 40000"):
    o=json.loads(js)
    r=jc.execute('SELECT json FROM latest WHERE numeroseao=?',(ns,)).fetchone()
    if not r: continue
    t=json.loads(r[0]).get('tender',{})
    m2[(o.get('nature'), o.get('precision'), t.get('mainProcurementCategory'), tuple(t.get('additionalProcurementCategories') or []))]+=1
    k+=1
    if k>=6000: break
for key,v in m2.most_common(20): print(v,key)
# precision values overall
print(xc.execute("SELECT COUNT(*) FROM avis_rows WHERE json LIKE '%\"montanttotalcontrat\"%'").fetchone(), 'rows with montanttotalcontrat; first ord with it:', xc.execute("SELECT MIN(ord) FROM avis_rows WHERE json LIKE '%\"montanttotalcontrat\"%'").fetchone())
