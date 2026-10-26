"""Directory source (v2): Wikidata SPARQL lookup of candidate labels (exact label/alias, en+fr) -> items with an official website (P856),
country (P17), class (P31) and the province/territory/US state they are located in (P131*). Raw results saved verbatim (one JSON per batch)
under downloads/enrichment_buyers_v2/dir/wikidata/. Sequential requests, descriptive UA.
usage: python3 -I wikidata_fetch.py"""
import sys, os, json, time
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from common import *
import requests

OUTD = DL2 + '/dir/wikidata'
os.makedirs(OUTD, exist_ok=True)
EP = 'https://query.wikidata.org/sparql'
C = json.load(open(WORK + '/classify.json'))
labels = []
seen = set()
for k, c in C.items():  # classify.json keeps input order (priority first)
    for l in c['labels']:
        if l not in seen and '"' not in l and '\\' not in l:
            seen.add(l); labels.append(l)
print('labels', len(labels), flush=True)
B = 90
sess = requests.Session(); sess.headers.update({'User-Agent': UA + ' contact: dataset enrichment worker', 'Accept': 'application/sparql-results+json'})


def q(batch):
    vals = ' '.join('"%s"@en "%s"@fr' % (l, l) for l in batch)
    return """SELECT ?item ?lab ?web ?country ?cls ?prov WHERE {
  VALUES ?lab { %s }
  ?item rdfs:label|skos:altLabel ?lab .
  ?item wdt:P856 ?web .
  OPTIONAL { ?item wdt:P17 ?country . }
  OPTIONAL { ?item wdt:P31 ?cls . }
  OPTIONAL { ?item wdt:P131* ?prov . ?prov wdt:P31 ?ptype . VALUES ?ptype { wd:Q11828004 wd:Q9357527 wd:Q35657 } }
}""" % vals


done = {f for f in os.listdir(OUTD)}
for i in range(0, len(labels), B):
    fn = 'batch_%04d.json' % (i // B)
    if fn in done:
        continue
    batch = labels[i:i + B]
    for attempt in range(3):
        try:
            t = now()
            r = sess.post(EP, data={'query': q(batch)}, timeout=90)
            if r.status_code == 200:
                d = r.json(); d['_retrieved_at'] = t; d['_labels'] = batch; d['_endpoint'] = EP
                json.dump(d, open(OUTD + '/' + fn, 'w'), ensure_ascii=False)
                print(t, fn, len(d['results']['bindings']), flush=True)
                break
            print('HTTP', r.status_code, fn, r.text[:200], flush=True)
            if r.status_code in (403, 429):
                time.sleep(30)
        except Exception as e:
            print('ERR', fn, type(e).__name__, flush=True)
        time.sleep(5)
    time.sleep(1.5)
# labels for classes and provinces
qids = set()
for f in os.listdir(OUTD):
    if not f.startswith('batch_'):
        continue
    for b in json.load(open(OUTD + '/' + f))['results']['bindings']:
        for v in ('cls', 'prov', 'country'):
            if v in b:
                qids.add(b[v]['value'].rsplit('/', 1)[1])
qids = sorted(qids)
lab = {}
for i in range(0, len(qids), 300):
    vals = ' '.join('wd:' + x for x in qids[i:i + 300])
    qq = 'SELECT ?x ?l WHERE { VALUES ?x { %s } ?x rdfs:label ?l . FILTER(lang(?l)="en") }' % vals
    r = sess.post(EP, data={'query': qq}, timeout=90)
    if r.status_code == 200:
        for b in r.json()['results']['bindings']:
            lab[b['x']['value'].rsplit('/', 1)[1]] = b['l']['value']
    time.sleep(1.5)
json.dump({'retrieved_at': now(), 'labels': lab}, open(OUTD + '/qid_labels.json', 'w'), ensure_ascii=False)
print('qid labels', len(lab))
