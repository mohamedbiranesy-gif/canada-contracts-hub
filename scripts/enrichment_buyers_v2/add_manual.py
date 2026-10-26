"""Record a targeted finding. Emails must appear in probe_log.jsonl for the given URL (evidence check); snippet+retrieved_at copied from it.
usage: add_manual.py '<json>'  json: {"match": {"owner_org"|"website_host"|"canonical_name"|"buyer_key_regex": ...}, "url": ..., "ap_emails": [...],
       "proc_emails": [...], "general_emails": [...], "invoice_portal": "", "invoicing_requirements": "", "mailing_address": "", "phone": "", "notes": ""}"""
import sys, os, json
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from common import *
d = json.loads(sys.argv[1])
probes = [json.loads(l) for l in open(WORK + '/probe_log.jsonl')]
pr = [p for p in probes if p['url'] == d['url'] or p['final_url'] == d['url']]
if d.get('url') and not pr and not d.get('evidence_external'):
    sys.exit('URL not probed: ' + d['url'])
p = pr[-1] if pr else {}
d['retrieved_at'] = p.get('retrieved_at') or d.get('retrieved_at')
snips = []
for e in d.get('ap_emails', []) + d.get('proc_emails', []) + d.get('general_emails', []):
    if not any(e.lower() == k for pp in pr for k in pp['emails']):
        sys.exit('EMAIL NOT ON PAGE: ' + e)
    s = next((pp['emails'][e.lower()] for pp in pr if pp['emails'].get(e.lower())), '')
    snips.append(s)
d['evidence_snippet'] = d.get('evidence_snippet') or ' … '.join(dict.fromkeys(x for x in snips if x))[:900]
open(WORK + '/manual_ap.jsonl', 'a').write(json.dumps(d, ensure_ascii=False) + '\n')
print('ok', d['match'], d.get('ap_emails'), d['retrieved_at'])
