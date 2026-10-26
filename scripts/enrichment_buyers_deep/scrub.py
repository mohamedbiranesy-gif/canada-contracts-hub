"""Remove non-role (possibly personal) e-mail addresses from intermediate work files (crawl*/deep*/probe_log). Raw downloaded pages are left as fetched."""
import sys, os, json, glob, importlib.util
sys.argv = [sys.argv[0], '/dev/null', '/dev/null']
spec = importlib.util.spec_from_file_location('crawlmod', os.path.join(os.path.dirname(os.path.abspath(__file__)), 'crawl.py'))
C = importlib.util.module_from_spec(spec); spec.loader.exec_module(C)
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from common import *
keep_manual = set()
for l in open(WORK + '/manual_ap.jsonl'):
    d = json.loads(l)
    for k in ('ap_emails', 'proc_emails', 'general_emails'):
        keep_manual.update(e.lower() for e in d.get(k, []))
dropped = 0
for f in glob.glob(WORK + '/crawl*.jsonl') + glob.glob(WORK + '/deep*.jsonl') + glob.glob(WORK + '/pdf*.jsonl'):
    out = []
    for l in open(f):
        r = json.loads(l)
        em = []
        for e in r.get('emails', []):
            if C.localpart_class(e['email'], e.get('snippet', '')) is None and e['email'] not in keep_manual:
                dropped += 1; continue
            em.append(e)
        r['emails'] = em
        out.append(json.dumps(r, ensure_ascii=False) + '\n')
    open(f + '.tmp', 'w').writelines(out); os.replace(f + '.tmp', f)
out = []
for l in open(WORK + '/probe_log.jsonl'):
    r = json.loads(l)
    em = {}
    for e, ctx in r['emails'].items():
        if e in keep_manual or C.localpart_class(e, ctx or '') is not None:
            em[e] = ctx
        else:
            dropped += 1
    r['emails'] = em
    out.append(json.dumps(r, ensure_ascii=False) + '\n')
open(WORK + '/probe_log.jsonl.tmp', 'w').writelines(out); os.replace(WORK + '/probe_log.jsonl.tmp', WORK + '/probe_log.jsonl')
print('dropped', dropped)
