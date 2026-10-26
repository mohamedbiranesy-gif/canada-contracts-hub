import sys, collections, re
from lxml import etree
# blank pays awarded suppliers: what do province / postal code / ville look like?
prov=collections.Counter(); pc=collections.Counter(); ville=collections.Counter(); yrs=collections.Counter(); n=0
ex=[]
for f in sys.argv[1:]:
    for ev, el in etree.iterparse(f, events=('end',), tag='avis', recover=True, huge_tree=True):
        for fo in el.iterfind('fournisseurs/fournisseur'):
            if fo.findtext('adjudicataire')=='1' and (fo.findtext('pays') or '')=='':
                n+=1
                prov[fo.findtext('province')]+=1
                p=(fo.findtext('codepostal') or '').strip().upper()
                pc['CA-pattern' if re.match(r'^[A-Z]\d[A-Z] ?\d[A-Z]\d$', p) else ('empty' if not p else 'other')]+=1
                ville[(fo.findtext('ville') or '').strip().lower()]+=1
                yrs[(el.findtext('dateadjudication') or '')[:4]]+=1
                if len(ex)<8: ex.append((fo.findtext('nomorganisation'), fo.findtext('adresse1'), fo.findtext('ville'), fo.findtext('province'), fo.findtext('codepostal'), fo.findtext('neq')))
        el.clear()
        while el.getprevious() is not None: del el.getparent()[0]
print('blank pays awarded rows', n); print('province', prov.most_common(10)); print('postal', pc); print('ville', ville.most_common(15)); print('years', sorted(yrs.items()))
for e in ex: print(e)
