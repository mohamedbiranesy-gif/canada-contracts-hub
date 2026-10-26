"""Stage 2c: PDF pass. For sites still lacking an AP mailbox, re-open up to 3 already-crawled supplier/finance pages, collect linked PDFs whose
link text/URL mentions direct deposit / supplier / invoicing, fetch up to 3 PDFs (<= 6 MB) per site and extract role mailboxes with context.
usage: python3 -I pdfpass.py <sites.json> <out.jsonl>   (sites.json: [{site, buyer_keys, pages:[urls]}])"""
import sys, os, json, re, subprocess, tempfile, urllib.parse
SITES, OUT = sys.argv[1], sys.argv[2]
sys.argv = [sys.argv[0], '/dev/null', '/dev/null']
import importlib.util
spec = importlib.util.spec_from_file_location('crawlmod', os.path.join(os.path.dirname(os.path.abspath(__file__)), 'crawl.py'))
C = importlib.util.module_from_spec(spec); spec.loader.exec_module(C)
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from common import *
import requests
from concurrent.futures import ThreadPoolExecutor
import threading
PDFKW = re.compile(r'(depot|dépôt|direct|fournisseur|facturation|facture|paiement|vendor|supplier|invoice|payable|comptes)', re.I)
lk = threading.Lock()


def get_pdf(sess, u, robots):
    h = C.host_of(u)
    with C.lock:
        H = C.hosts.setdefault(h, C.Host())
    if robots is not None:
        try:
            if not robots.can_fetch(UA, u):
                return None
        except Exception:
            pass
    H.wait()
    try:
        r = sess.get(u, timeout=(10, 40), stream=True)
        if r.status_code != 200:
            return None
        b = r.raw.read(6_000_000, decode_content=True)
        if not b.startswith(b'%PDF'):
            return None
        with tempfile.NamedTemporaryFile(suffix='.pdf') as f:
            f.write(b); f.flush()
            return subprocess.run(['pdftotext', '-layout', f.name, '-'], capture_output=True, text=True, timeout=60).stdout
    except Exception:
        return None


def robots_for(sess, site):
    import urllib.robotparser
    try:
        rr = sess.get(urllib.parse.urljoin(site, '/robots.txt'), timeout=(10, 15))
        if rr.status_code == 200 and 'html' not in rr.headers.get('content-type', ''):
            rp = urllib.robotparser.RobotFileParser(); rp.parse(rr.text.splitlines()); return rp
    except Exception:
        pass
    return None


def work(s):
    sess = requests.Session(); sess.headers.update({'User-Agent': UA, 'Accept-Language': 'fr-CA,fr;q=0.9,en;q=0.8'})
    robots = robots_for(sess, s['site'])  # v2: robots.txt honoured in the PDF pass too
    res = {'site': s['site'], 'mode': 'pdf_pass', 'started_at': now(), 'pages': [], 'emails': [], 'invoice_snippets': [], 'portal_links': [], 'status': 'ok', 'errors': []}
    pdfs = []
    for pu in s['pages'][:3]:
        r, err = C.get(sess, pu, robots)
        if r is None:
            continue
        st, fu, html, hdr = r
        if C.challenged(st, html, hdr):
            res['status'] = 'partially_blocked'; break
        title, text, links, emails, mt = C.extract(fu, html)
        for lu, lt in links:
            if lu.lower().split('?')[0].endswith('.pdf') and (PDFKW.search(lt) or PDFKW.search(urllib.parse.unquote(lu))) and C.same_site(lu, C.host_of(s['site'])):
                if lu not in [p[0] for p in pdfs]:
                    pdfs.append((lu, lt, fu))
    for lu, lt, fu in pdfs[:3]:
        txt = get_pdf(sess, lu, robots)
        if not txt:
            continue
        t = re.sub(r'\s+', ' ', txt)
        res['pages'].append({'url': lu, 'status': 200, 'title': 'PDF: ' + lt[:150], 'retrieved_at': now(), 'linked_from': fu})
        for m in C.EMAIL_RE.finditer(t):
            e = m.group(0).strip('.').lower()
            ctx = t[max(0, m.start() - 250): m.end() + 150]
            cl = C.localpart_class(e, ctx + ' ' + lt + ' ' + lu)
            if cl:
                res['emails'].append({'email': e, 'class': cl, 'page_url': lu, 'page_title': 'PDF: ' + lt[:120], 'snippet': ctx[:400], 'retrieved_at': now()})
    d = {}
    for e in res['emails']:
        d.setdefault((e['email'], e['class']), e)
    res['emails'] = list(d.values()); res['buyer_keys'] = s['buyer_keys']; res['finished_at'] = now()
    with lk:
        out.write(json.dumps(res, ensure_ascii=False) + '\n'); out.flush()
    print(now(), s['site'], len(pdfs), [e['email'] for e in res['emails'] if e['class'].startswith('ap')][:3], flush=True)


sites = json.load(open(SITES))
done = {json.loads(l)['site'] for l in open(OUT)} if os.path.exists(OUT) else set()
out = open(OUT, 'a')
with ThreadPoolExecutor(8) as ex:
    list(ex.map(work, [s for s in sites if s['site'] not in done]))
