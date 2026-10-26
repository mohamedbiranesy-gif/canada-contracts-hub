import sqlite3, json, collections, re, unicodedata
xc = sqlite3.connect('downloads/seao_quebec/staging/seao_xml.sqlite')
jc = sqlite3.connect('downloads/seao_quebec/staging/seao_json.sqlite')
LEGAL={'inc','ltee','ltd','limitee','limited','enr','senc','sencrl','llp','corp','corporation','co','cie','compagnie','lp','sec','llc','plc','ulc','gp'}
def sa(s): return ''.join(c for c in unicodedata.normalize('NFKD', s) if not unicodedata.combining(c))
def nn(s):
    s=re.sub(r'[^a-z0-9]+',' ',sa((s or '').lower())); return ' '.join(t for t in s.split() if t not in LEGAL)
def neq(s):
    d=re.sub(r'\D','',s or ''); return d if len(d)==10 else ''
k=0; cnt=collections.Counter()
for (ns,) in xc.execute("SELECT DISTINCT numeroseao FROM avis_rows WHERE numeroseao BETWEEN '1000000' AND '1003000'"):
    a=xc.execute('SELECT json FROM avis_rows WHERE numeroseao=? ORDER BY ord DESC LIMIT 1',(ns,)).fetchone()
    o=json.loads(a[0]); aw=[f for f in o.get('fournisseurs',[]) if f.get('adjudicataire')=='1']
    r=jc.execute('SELECT json FROM latest WHERE numeroseao=?',(ns,)).fetchone()
    if not r: continue
    rel=json.loads(r[0]); awards=rel.get('awards') or []
    if not awards: continue
    parties={p.get('id'):p for p in rel.get('parties') or []}
    jsup=[]
    for a_ in awards:
        for s in a_.get('suppliers') or []:
            p=parties.get(s.get('id')) or {}
            jsup.append((neq((p.get('details') or {}).get('neq') or (p.get('details') or {}).get('NEQ') or ''), nn(s.get('name')), s.get('name'), s.get('id')))
    for f in aw:
        fn=neq(f.get('neq')); fnm=nn(f.get('nomorganisation'))
        match = any((fn and fn==j[0]) or (fnm and fnm==j[1]) for j in jsup)
        cnt[match]+=1
        if not match and k<15:
            k+=1; print(ns, '| XML:', f.get('nomorganisation'), f.get('neq'), '| JSON:', [(j[2], j[0], j[3]) for j in jsup][:4], rel['tag'], rel.get('_source_file'))
print(cnt)
