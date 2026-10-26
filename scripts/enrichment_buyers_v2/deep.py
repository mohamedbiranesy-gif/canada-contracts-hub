"""Stage 2b: sitemap-driven deep pass for high-priority sites. Reads robots.txt Sitemap: lines (or /sitemap.xml), collects same-site URLs whose
path mentions invoicing/supplier keywords, fetches the best ~15 (same politeness as crawl.py) and extracts role mailboxes / invoicing text.
usage: python3 -I deep.py <sites.json> <out.jsonl>"""
import sys, os, json, re, gzip, urllib.parse, urllib.robotparser
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
SITES, OUT = sys.argv[1], sys.argv[2]
sys.argv = [sys.argv[0], '/dev/null', '/dev/null']
import importlib.util
spec = importlib.util.spec_from_file_location('crawlmod', os.path.join(os.path.dirname(os.path.abspath(__file__)), 'crawl.py'))
C = importlib.util.module_from_spec(spec); spec.loader.exec_module(C)
import requests
from concurrent.futures import ThreadPoolExecutor
from common import *

PAT = re.compile(r'(factur|invoice|payable|comptes-a-payer|comptes-fournisseurs|paiement-des-fournisseurs|fournisseur|supplier|vendor|doing-business|faire-affaire|approvisionnement|procurement|purchasing|achats)', re.I)
STRONG = re.compile(r'(factur|invoice|payable|comptes-a-payer|paiement)', re.I)
BAD = re.compile(r'(emploi|career|job|nouvelle|news|communique|actualit|evenement|event|/\d{4}/\d{2}/|avis-public|proces-verbal|seance|reglement)', re.I)


def sitemap_urls(sess, home, robots_txt, robots):
    sm = re.findall(r'(?im)^\s*sitemap:\s*(\S+)', robots_txt or '')
    if not sm:
        sm = [urllib.parse.urljoin(home, '/sitemap.xml'), urllib.parse.urljoin(home, '/sitemap_index.xml')]
    seen = set(); urls = []; queue = list(sm)[:6]; n = 0
    while queue and n < 25:
        u = queue.pop(0)
        if u in seen:
            continue
        seen.add(u); n += 1
        r, err = C.get_raw(sess, u, robots)
        if r is None:
            continue
        body = r
        if u.endswith('.gz') or body[:2] == b'\x1f\x8b':
            try:
                body = gzip.decompress(body)
            except Exception:
                continue
        txt = body.decode('utf-8', 'replace')
        locs = re.findall(r'<loc>\s*([^<\s]+)\s*</loc>', txt)
        if '<sitemapindex' in txt[:2000]:
            # prioritise sub-sitemaps likely to hold pages (fr/en pages, not images/news)
            locs.sort(key=lambda x: (('page' not in x and 'fr' not in x), len(x)))
            queue.extend([l for l in locs if not re.search(r'(image|video|news|post|event|product)', l, re.I)][:15])
        else:
            urls.extend(locs)
        if len(urls) > 200000:
            break
    return urls


def get_raw(sess, u, robots):
    h = C.host_of(u)
    with C.lock:
        H = C.hosts.setdefault(h, C.Host())
    if robots is not None:
        try:
            if not robots.can_fetch(UA, u):
                return None, 'robots'
        except Exception:
            pass
    H.wait()
    try:
        r = sess.get(u, timeout=(10, 30), stream=True)
        if r.status_code != 200:
            return None, 'http %s' % r.status_code
        return r.raw.read(15_000_000, decode_content=True), None
    except Exception as e:
        return None, type(e).__name__


C.get_raw = get_raw


def deep(site):
    sess = requests.Session(); sess.headers.update({'User-Agent': UA, 'Accept-Language': 'fr-CA,fr;q=0.9,en;q=0.8'})
    home = site
    res = {'site': site, 'mode': 'deep_sitemap', 'started_at': now(), 'pages': [], 'emails': [], 'portal_links': [], 'invoice_snippets': [], 'status': 'ok', 'errors': []}
    robots = None; rtxt = ''
    try:
        rr = sess.get(urllib.parse.urljoin(home, '/robots.txt'), timeout=(10, 15))
        if rr.status_code == 200 and 'html' not in rr.headers.get('content-type', ''):
            rtxt = rr.text; rp = urllib.robotparser.RobotFileParser(); rp.parse(rtxt.splitlines()); robots = rp
        elif rr.status_code in (403, 429, 503):
            res['status'] = 'blocked_or_challenged'; res['errors'].append('robots.txt HTTP %s' % rr.status_code); return res
    except Exception as e:
        res['errors'].append('robots %s' % type(e).__name__)
    urls = sitemap_urls(sess, home, rtxt, robots)
    res['sitemap_urls'] = len(urls)
    root = C.host_of(home)
    cand = []
    for u in set(urls):
        p = urllib.parse.unquote(urllib.parse.urlsplit(u).path)
        pn = unaccent(p.lower())
        if not C.same_site(u, root) or not PAT.search(pn) or BAD.search(pn) or C.BAD_EXT.search(u) or pn.endswith('.pdf'):
            continue
        sc = (10 if STRONG.search(pn) else 0) + (3 if re.search('fournisseur|supplier|vendor', pn) else 0) - pn.count('/') * 0.3
        cand.append((sc, u))
    cand.sort(key=lambda x: -x[0])
    res['candidates'] = [u for s, u in cand[:25]]
    for s, u in cand[:int(os.environ.get('DEEPMAX', '14'))]:
        r, err = C.get(sess, u, robots)
        if r is None:
            res['errors'].append('%s %s' % (err, u)); continue
        st, fu, html, hdr = r
        if C.challenged(st, html, hdr):
            res['status'] = 'partially_blocked'; res['errors'].append('challenge at %s' % u); break
        if st >= 400:
            continue
        title, text, links, emails, mt = C.extract(fu, html)
        res['pages'].append({'url': fu, 'status': st, 'title': title[:200], 'retrieved_at': now()})
        for e, ctx in emails.items():
            cl = C.localpart_class(e, ctx + ' ' + title + ' ' + fu)
            if cl:
                res['emails'].append({'email': e, 'class': cl, 'page_url': fu, 'page_title': title[:150], 'snippet': re.sub(r'\s+', ' ', ctx)[:400], 'retrieved_at': now()})
        nt = unaccent(mt.lower())
        for kw in ['factur', 'invoice']:
            i = nt.find(kw)
            if i >= 0:
                res['invoice_snippets'].append({'page_url': fu, 'title': title[:150], 'snippet': re.sub(r'\s+', ' ', mt[max(0, i - 300): i + 900])})
                break
        for lu, lt in links:
            ln = norm(lt + ' ' + lu)
            if any(norm(p) in ln for p in C.PORTAL_CTX):
                res['portal_links'].append({'url': lu, 'anchor': lt[:150], 'page_url': fu})
    if not urls:
        res['status'] = 'no_sitemap'
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
        done = {json.loads(l)['site'] for l in open(OUT)}
    f = open(OUT, 'a')
    import threading
    lk = threading.Lock()

    def work(s):
        try:
            r = deep(s['site'])
        except Exception as e:
            r = {'site': s['site'], 'mode': 'deep_sitemap', 'status': 'crash', 'errors': [repr(e)[:200]], 'pages': [], 'emails': []}
        r['fetched_site'] = s['site']
        r['site'] = s.get('orig_site', s['site'])  # key = official website as in bulk.json (crawl key)
        r['buyer_keys'] = s['buyer_keys']
        with lk:
            f.write(json.dumps(r, ensure_ascii=False) + '\n'); f.flush()
        print(now(), s['site'], r['status'], r.get('sitemap_urls'), len(r.get('pages', [])), [e['email'] for e in r.get('emails', []) if e['class'].startswith('ap')][:3], flush=True)
    with ThreadPoolExecutor(int(os.environ.get('THREADS', '10'))) as ex:
        list(ex.map(work, [s for s in sites if s.get('orig_site', s['site']) not in done]))


main()
