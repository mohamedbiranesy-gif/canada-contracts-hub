"""Deep-search pass 4 (W3): sitemap scan for (a) Canada Post labour-disruption notices (2024-2025) — municipalities and public bodies published
the e-mail addresses suppliers should use for invoices while mail was suspended — and (b) invoicing / accounts-payable / direct-deposit pages and
forms that earlier passes did not open. Reads the robots-declared sitemaps (or /sitemap.xml), keeps same-site URLs matching POSTAL or AP patterns,
skips URLs already fetched by any earlier pass, fetches <= MAXF of them (HTML or PDF).
Politeness unchanged: robots.txt honoured, one queue per host, 0.7 s spacing (<= ~1.4 req/s), bot-check/403/429/503 stops the site.
usage: python3 -I deep4.py <sites.json> <out.jsonl>"""
import sys, os, json, re, gzip, glob, urllib.parse, urllib.robotparser, threading
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
SITES, OUT = sys.argv[1], sys.argv[2]
_argv = sys.argv
sys.argv = [_argv[0], '/dev/null', '/dev/null']
import importlib.util
here = os.path.dirname(os.path.abspath(__file__))
spec = importlib.util.spec_from_file_location('crawlmod', os.path.join(here, 'crawl.py'))
C = importlib.util.module_from_spec(spec); spec.loader.exec_module(C)
import requests
from concurrent.futures import ThreadPoolExecutor
from common import *

# reuse deep3's fetch/scan helpers without running its main()
src = open(os.path.join(here, 'deep3.py')).read().split('\ndef main():')[0]
src = src.replace("SITES, OUT = sys.argv[1], sys.argv[2]\n", '').replace("sys.argv = [sys.argv[0], '/dev/null', '/dev/null']\n", '')
D3 = {'__file__': os.path.join(here, 'deep3.py'), '__name__': 'deep3mod'}
exec(compile(src, 'deep3.py', 'exec'), D3)
fetch = D3['fetch']; get_raw = D3['get_raw']

POSTAL = re.compile(r'(postes?[-_ ]canada|canada[-_ ]post|postal|greve|grève|courrier|strike|arret[-_]de[-_]travail|arrêt[-_]de[-_]travail|interruption[-_]de[-_]service|'
                    r'interruption[-_]du[-_]service|perturbation|labour[-_]disruption|work[-_]stoppage|mail[-_]delivery|livraison[-_]du[-_]courrier)', re.I)
APU = re.compile(r'(factur|invoice|payable|comptes?[-_]?(a|à)[-_]?payer|comptes?[-_]payables?|comptes?[-_]fournisseurs?|depot[-_]direct|dépôt[-_]direct|direct[-_]deposit|'
                 r'paiement[s]?[-_](des[-_]|aux[-_])?fournisseurs?|vendor[-_]payment|supplier[-_]payment|eft[-_]|[-_]eft|virement|guide[-_](du[-_]|des[-_])?fournisseur|'
                 r'supplier[-_]guide|vendor[-_]guide|conditions[-_]generales[-_]d[-_]?achat|purchase[-_]order[-_]terms|terms[-_]and[-_]conditions[-_]of[-_]purchase|'
                 r'po[-_]terms|bon[-_]de[-_]commande)', re.I)
MAXF = int(os.environ.get('MAXF', '8'))
lk = threading.Lock()

SEEN_PAGES = set()
for f in sorted(glob.glob(OLD_WORK + '/crawl*.jsonl')) + sorted(glob.glob(OLD_WORK + '/deep*.jsonl')) + sorted(glob.glob(V2_WORK + '/*.jsonl')) + \
        sorted(glob.glob(WORK + '/deep*.jsonl')):
    if f.endswith(os.path.basename(OUT)):
        continue
    for l in open(f):
        try:
            r = json.loads(l)
        except Exception:
            continue
        for p in r.get('pages', []) or []:
            SEEN_PAGES.add(p.get('url', '').split('#')[0])


def sitemap_urls(sess, home, robots_txt, robots):
    sm = re.findall(r'(?im)^\s*sitemap:\s*(\S+)', robots_txt or '')
    if not sm:
        sm = [urllib.parse.urljoin(home, '/sitemap.xml'), urllib.parse.urljoin(home, '/sitemap_index.xml')]
    seen = set(); urls = []; queue = list(dict.fromkeys(sm))[:8]; n = 0
    while queue and n < 40:
        u = queue.pop(0)
        if u in seen:
            continue
        seen.add(u); n += 1
        body, err = get_raw(sess, u, robots, 30_000_000)
        if body is None:
            continue
        if u.endswith('.gz') or body[:2] == b'\x1f\x8b':
            try:
                body = gzip.decompress(body)
            except Exception:
                continue
        txt = body.decode('utf-8', 'replace')
        locs = re.findall(r'<loc>\s*(?:<!\[CDATA\[)?\s*([^<\s\]]+)', txt)
        if '<sitemapindex' in txt[:3000]:
            locs.sort(key=lambda x: (not re.search(r'(page|post|nouvelle|actualit|news|communiq|media|document|file|attachment)', x, re.I), len(x)))
            queue.extend([l for l in locs if not re.search(r'(image|video|product|produit|event|evenement)', l, re.I)][:30])
        else:
            urls.extend(locs)
        if len(urls) > 400000:
            break
    return urls


def scan(s):
    site = s['site']
    sess = requests.Session(); sess.headers.update({'User-Agent': UA, 'Accept-Language': 'fr-CA,fr;q=0.9,en;q=0.8'})
    home = site if site.startswith('http') else 'https://' + site
    res = {'site': site, 'mode': 'deep4', 'started_at': now(), 'pages': [], 'emails': [], 'portal_links': [], 'invoice_snippets': [], 'ap_phone_snippets': [],
           'status': 'ok', 'errors': []}
    robots = None; rtxt = ''
    try:
        rr = sess.get(urllib.parse.urljoin(home, '/robots.txt'), timeout=(10, 15))
        if rr.status_code == 200 and 'html' not in rr.headers.get('content-type', ''):
            rtxt = rr.text; rp = urllib.robotparser.RobotFileParser(); rp.parse(rtxt.splitlines()); robots = rp
        elif rr.status_code in (403, 429):
            res['status'] = 'blocked_or_challenged'; res['errors'].append('robots.txt HTTP %s' % rr.status_code); return res
    except Exception as e:
        res['errors'].append('robots %s' % type(e).__name__)
    urls = sitemap_urls(sess, home, rtxt, robots)
    res['sitemap_urls'] = len(urls)
    root = C.host_of(home)
    cand = []
    for u in set(urls):
        if not C.same_site(u, root) or u.split('#')[0] in SEEN_PAGES or C.BAD_EXT.search(u):
            continue
        p = unaccent(urllib.parse.unquote(urllib.parse.urlsplit(u).path).lower())
        sc = 0
        if POSTAL.search(p) and re.search(r'(postes?[-_ ]canada|canada[-_ ]post|postal|courrier|mail)', p):
            sc += 20
        if APU.search(p):
            sc += 15
        if sc and re.search(r'(fournisseur|supplier|vendor|factur|invoice|payable|paiement|payment)', p):
            sc += 5
        if sc:
            cand.append((sc - p.count('/') * 0.2, u))
    cand.sort(key=lambda t: -t[0])
    res['candidates'] = [u for _, u in cand[:20]]
    for _, u in cand[:MAXF]:
        x = fetch(sess, res, u, robots)
        if x == 'STOP':
            break
    d = {}
    for e in res['emails']:
        d.setdefault((e['email'], e['class']), e)
    res['emails'] = list(d.values())
    res['finished_at'] = now()
    return res


def main():
    sites = json.load(open(SITES))
    done = set()
    if os.path.exists(OUT):
        for l in open(OUT):
            try:
                done.add(json.loads(l)['site'])
            except Exception:
                pass
    f = open(OUT, 'a')

    def work(s):
        try:
            r = scan(s)
        except Exception as e:
            r = {'site': s['site'], 'mode': 'deep4', 'status': 'crash', 'errors': [repr(e)[:200]], 'pages': [], 'emails': []}
        r['buyer_keys'] = s['buyer_keys']; r['gid'] = s.get('gid')
        with lk:
            f.write(json.dumps(r, ensure_ascii=False) + '\n'); f.flush()
        print(now(), s['site'], r['status'], r.get('sitemap_urls'), len(r.get('pages', [])), [e['email'] for e in r.get('emails', []) if e['class'].startswith('ap')][:3], flush=True)
    with ThreadPoolExecutor(int(os.environ.get('THREADS', '6'))) as ex:
        list(ex.map(work, [s for s in sites if s['site'] not in done]))


main()
