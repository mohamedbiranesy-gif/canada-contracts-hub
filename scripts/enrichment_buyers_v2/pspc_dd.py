"""Turn the PSPC 'Direct deposit for government suppliers' departmental contact table into targeted findings (manual_ap.jsonl)."""
import sys, os, json, re
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from common import *
import importlib.util
spec = importlib.util.spec_from_file_location('al', os.path.join(os.path.dirname(os.path.abspath(__file__)), 'alias.py'))
src = open(spec.origin).read().split('\ndef main():')[0]
ns = {'__file__': spec.origin}; exec(src, ns)
GC_ALIAS = ns['GC_ALIAS']
URL = 'https://www.canada.ca/en/public-services-procurement/services/payments-to-from-government/direct-deposit/businesses/suppliers.html'
probe = [json.loads(l) for l in open(WORK + '/probe_log.jsonl') if json.loads(l)['url'] == URL][-1]
gc = json.load(open(DL + '/gc/organization_list.json'))['result']
by = {}
for o in gc:
    for lang in ('en',):
        t = norm(re.sub(r'\(.*?\)', '', o['title_translated'][lang]))
        by[t] = o['name']
rows = json.load(open(WORK + '/pspc_dd_contacts.json'))[1:]
out = open(WORK + '/manual_ap.jsonl', 'a'); n = 0; unm = []
for inst, txt, emails in rows:
    if not emails:
        continue
    key = norm(re.sub(r'\(.*?\)', '', inst))
    code = by.get(key)
    if not code:
        for k, c in by.items():
            if key and (key == k or (len(key) > 12 and (key in k or k in key))):
                code = c; break
    if not code:
        for rx, c in GC_ALIAS:
            if re.search(rx, key):
                code = c; break
    if not code:
        unm.append(inst); continue
    ems = [e.strip().lower() for e in emails if EMAIL_OK.match(e.strip())] if False else [e.strip().lower() for e in emails if '@' in e and '/' not in e]
    ems = [e for e in ems if e in probe['emails']]
    if not ems:
        continue
    ph = re.findall(r'Telephone[^|]*\|\s*([0-9‑\-\s,ext\.]+)', txt)
    d = {'match': {'owner_org': code}, 'url': URL, 'ap_emails': ems, 'retrieved_at': probe['retrieved_at'],
         'phone': (ph[0].strip(' ,') if ph else ''),
         'notes': 'PSPC list "Direct deposit for government suppliers": departmental contact for supplier payments / direct deposit (%s: %s)' % (inst, txt.replace(' | ', ' ')[:200]),
         'evidence_snippet': '%s — %s' % (inst, txt.replace(' | ', ' ')[:300]), 'source_kind': 'pspc_direct_deposit_contacts'}
    out.write(json.dumps(d, ensure_ascii=False) + '\n'); n += 1
print('written', n, 'unmatched', unm)
