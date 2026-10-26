"""Profile SEAO XML: element inventory per file type, distinct pays values, counts. Streams with iterparse.
Usage: python3 -I profile_xml.py <xml_extracted_root> <out_report>"""
import sys, os, collections, re
from lxml import etree
root, out = sys.argv[1:3]
files = []
for dp, dn, fns in os.walk(root):
    for fn in fns:
        if fn.lower().endswith('.xml'): files.append(os.path.join(dp, fn))
files.sort()
def kind(fn):
    b = os.path.basename(fn)
    return re.sub(r'_\d{8}_\d{8}\.xml$', '', b, flags=re.I)
tags_by_kind = collections.defaultdict(collections.Counter)
pays_avis = collections.Counter(); pays_four = collections.Counter(); prov_four=collections.Counter()
adj_vals = collections.Counter(); type_vals=collections.Counter(); nature_vals=collections.Counter()
n_by_kind = collections.Counter(); n_four=0; n_adj=0
hyper = collections.Counter()
years_adj = collections.Counter()
for i, f in enumerate(files):
    k = kind(f)
    top = 'avis' if k.startswith('Avis') or k.startswith('Depenses') else 'contrat'
    try:
        for ev, el in etree.iterparse(f, events=('end',), tag=top, recover=True, huge_tree=True):
            n_by_kind[k] += 1
            for sub in el.iter():
                tags_by_kind[k][sub.tag] += 1
            if k.startswith('Avis'):
                p = el.findtext('pays'); pays_avis[p] += 1
                type_vals[el.findtext('type')] += 1; nature_vals[el.findtext('nature')] += 1
                h = el.findtext('hyperlienseao') or ''
                hyper[re.sub(r'ItemId=.*', 'ItemId=...', h)] += 1
                for fo in el.iterfind('fournisseurs/fournisseur'):
                    n_four += 1
                    a = fo.findtext('adjudicataire'); adj_vals[a] += 1
                    if a == '1':
                        n_adj += 1
                        pays_four[fo.findtext('pays')] += 1
                        prov_four[(fo.findtext('pays'), fo.findtext('province'))] += 1
                        years_adj[(el.findtext('dateadjudication') or '')[:4]] += 1
            el.clear()
            while el.getprevious() is not None:
                del el.getparent()[0]
    except Exception as e:
        print('ERR', f, repr(e), flush=True)
    if i % 20 == 0: print(i, f, flush=True)
with open(out, 'w', encoding='utf-8') as o:
    o.write(f'files {len(files)}\n')
    o.write(f'records by kind {dict(n_by_kind)}\n')
    o.write(f'fournisseur rows {n_four}, adjudicataire=1 rows {n_adj}\n')
    o.write(f'adjudicataire values {dict(adj_vals)}\n')
    o.write(f'type values {dict(type_vals)}\n')
    o.write(f'nature values {dict(nature_vals)}\n')
    o.write(f'hyperlien patterns {dict(hyper)}\n')
    o.write(f'avis pays {pays_avis.most_common()}\n')
    o.write(f'awarded supplier pays {pays_four.most_common()}\n')
    o.write(f'awarded supplier (pays,province) {prov_four.most_common(60)}\n')
    o.write(f'adjudication years (awarded rows) {sorted(years_adj.items())}\n')
    for k, c in sorted(tags_by_kind.items()):
        o.write(f'--- {k}\n')
        for t, n in c.most_common(): o.write(f'  {n}\t{t}\n')
print('done')
