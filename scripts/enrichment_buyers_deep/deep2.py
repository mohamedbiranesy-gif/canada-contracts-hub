"""Deep-search automated pass (W3): for organisation websites of buyers still lacking an AP mailbox / invoice portal.
Sitemap-driven like deep.py but (a) French + English invoicing/supplier keyword set (facturation, comptes payables/à payer/fournisseurs,
dépôt direct, guide du fournisseur, conditions générales d'achat, purchase-order terms, vendor guide, EFT ...), (b) PDFs listed in sitemaps or linked
from the fetched pages ARE read (pdftotext), (c) sites without a sitemap: homepage + keyword links (2 levels) + linked PDFs.
Politeness unchanged: robots.txt honoured, one queue per host, 0.7 s spacing (<= ~1.4 req/s), bot-check/403 pages stop the site (never retried around).
usage: python3 -I deep2.py <sites.json> <out.jsonl>     sites.json: [{"site": url, "buyer_keys": [...], "gid": ...}]"""
import sys, os, json, re, gzip, subprocess, tempfile, urllib.parse, urllib.robotparser, threading
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
SITES, OUT = sys.argv[1], sys.argv[2]
sys.argv = [sys.argv[0], '/dev/null', '/dev/null']
import importlib.util
spec = importlib.util.spec_from_file_location('crawlmod', os.path.join(os.path.dirname(os.path.abspath(__file__)), 'crawl.py'))
C = importlib.util.module_from_spec(spec); spec.loader.exec_module(C)
import requests
from concurrent.futures import ThreadPoolExecutor
from common import *

PAT = re.compile(r'(factur|invoice|payable|comptes?-?a-?payer|comptes-fournisseurs|comptes-payables|paiement|payment|fournisseur|supplier|vendor|depot-direct|'
                 r'direct-deposit|virement|\beft\b|doing-business|faire-affaire|faire-des-affaires|conditions-generales|terms-and-conditions|bon-de-commande|'
                 r'purchase-order|approvisionnement|procurement|purchasing|achats|acquisitions|finances?|comptabilite|accounting)', re.I)
STRONG = re.compile(r'(factur|invoice|payable|comptes-?a-?payer|comptes-payables|comptes-fournisseurs|paiement-?(des-|aux-)?fournisseur|depot-direct|'
                    r'direct-deposit|supplier-payment|vendor-payment|guide-?(du-|des-|de-)?fournisseur|supplier-guide|vendor-guide|conditions-generales-d-?achat|'
                    r'purchase-order-terms|terms-and-conditions-of-purchase|formulaire-fournisseur|supplier-form|vendor-form|eft|virement)', re.I)
BAD = re.compile(r'(emploi|career|job|nouvelle|news|communique|actualit|evenement|event|/\d{4}/\d{2}/|avis-public|proces-verbal|seance|reglement|'
                 r'budget|rapport-annuel|annual-report|etats-financiers|financial-statement|ordre-du-jour|agenda|minutes|bylaw|by-law|taxe|tax-|permis|permit|'
                 r'water|eau-potable|stationnement|parking|loisir|recreation)', re.I)
PDFLINK = re.compile(r'(depot|dépôt|direct|fournisseur|factur|paiement|vendor|supplier|invoice|payable|comptes|eft|virement|conditions|terms|guide)', re.I)
DEEPMAX = int(os.environ.get('DEEPMAX', '16'))
PDFMAX = int(os.environ.get('PDFMAX', '6'))
lk = threading.Lock()


def get_raw(sess, u, robots, limit=15_000_000):
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
        r = sess.get(u, timeout=(10, 40), stream=True)
        if r.status_code != 200:
            return None, 'http %s' % r.status_code
        return r.raw.read(limit, decode_content=True), None
    except Exception as e:
        return None, type(e).__name__


def pdf_text(b):
    if not b or not b.startswith(b'%PDF'):
        return None
    with tempfile.NamedTemporaryFile(suffix='.pdf') as f:
        f.write(b); f.flush()
        try:
            return subprocess.run(['pdftotext', '-layout', f.name, '-'], capture_output=True, text=True, timeout=60).stdout
        except Exception:
            return None


def sitemap_urls(sess, home, robots_txt, robots):
    sm = re.findall(r'(?im)^\s*sitemap:\s*(\S+)', robots_txt or '')
    if not sm:
        sm = [urllib.parse.urljoin(home, '/sitemap.xml'), urllib.parse.urljoin(home, '/sitemap_index.xml')]
    seen = set(); urls = []; queue = list(dict.fromkeys(sm))[:8]; n = 0
    while queue and n < 30:
        u = queue.pop(0)
        if u in seen:
            continue
        seen.add(u); n += 1
        body, err = get_raw(sess, u, robots)
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
            locs.sort(key=lambda x: (('page' not in x and 'fr' not in x and 'attachment' not in x and 'media' not in x), len(x)))
            queue.extend([l for l in locs if not re.search(r'(image|video|news|post-sitemap|event|product|nouvelle|actualite)', l, re.I)][:20])
        else:
            urls.extend(locs)
        if len(urls) > 300000:
            break
    return urls


def handle_text(res, u, title, text, mt, links=()):
    for m in C.EMAIL_RE.finditer(text):
        e = m.group(0).strip('.').lower()
        ctx = text[max(0, m.start() - 250): m.end() + 150]
        cl = C.localpart_class(e, ctx + ' ' + title + ' ' + u)
        if cl:
            res['emails'].append({'email': e, 'class': cl, 'page_url': u, 'page_title': title[:150], 'snippet': re.sub(r'\s+', ' ', ctx)[:400], 'retrieved_at': now()})
    nt = unaccent(mt.lower())
    for kw in ['factur', 'invoice']:
        i = nt.find(kw)
        if i >= 0:
            res['invoice_snippets'].append({'page_url': u, 'title': title[:150], 'snippet': re.sub(r'\s+', ' ', mt[max(0, i - 300): i + 900])})
            break
    for lu, lt in links:
        ln = norm(lt + ' ' + lu)
        if any(norm(p) in ln for p in C.PORTAL_CTX):
            res['portal_links'].append({'url': lu, 'anchor': lt[:150], 'page_url': u})


def fetch_page(sess, res, u, robots, pdfq):
    if u.lower().split('?')[0].endswith('.pdf'):
        b, err = get_raw(sess, u, robots, 8_000_000)
        t = pdf_text(b)
        if not t:
            res['errors'].append('%s %s' % (err or 'not_pdf', u)); return None
        t = re.sub(r'\s+', ' ', t)
        res['pages'].append({'url': u, 'status': 200, 'title': 'PDF', 'retrieved_at': now()})
        handle_text(res, u, 'PDF ' + urllib.parse.unquote(u.rsplit('/', 1)[-1]), t, t)
        return []
    r, err = C.get(sess, u, robots)
    if r is None:
        res['errors'].append('%s %s' % (err, u)); return None
    st, fu, html, hdr = r
    if C.challenged(st, html, hdr):
        res['status'] = 'partially_blocked'; res['errors'].append('challenge at %s' % u); return 'STOP'
    if st >= 400:
        return None
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
        if lu.lower().split('?')[0].endswith('.pdf') and (PDFLINK.search(lt) or PDFLINK.search(urllib.parse.unquote(lu))):
            pdfq.append((lu, lt))
    return links


def deep(site):
    sess = requests.Session(); sess.headers.update({'User-Agent': UA, 'Accept-Language': 'fr-CA,fr;q=0.9,en;q=0.8'})
    home = site if site.startswith('http') else 'https://' + site
    res = {'site': site, 'mode': 'deep2', 'started_at': now(), 'pages': [], 'emails': [], 'portal_links': [], 'invoice_snippets': [], 'status': 'ok', 'errors': []}
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
        if not C.same_site(u, root) or not PAT.search(pn) or BAD.search(pn):
            continue
        if C.BAD_EXT.search(u):
            continue
        ispdf = pn.endswith('.pdf')
        sc = (10 if STRONG.search(pn) else 0) + (3 if re.search('fournisseur|supplier|vendor', pn) else 0) - pn.count('/') * 0.3 + (1 if ispdf and STRONG.search(pn) else 0)
        if ispdf and not STRONG.search(pn) and not re.search('fournisseur|supplier|vendor', pn):
            continue
        cand.append((sc, u))
    cand.sort(key=lambda x: -x[0])
    res['candidates'] = [u for s, u in cand[:30]]
    pdfq = []
    seen = set()
    stop = False
    for s, u in cand[:DEEPMAX]:
        seen.add(u)
        x = fetch_page(sess, res, u, robots, pdfq)
        if x == 'STOP':
            stop = True; break
    if not urls and not stop:
        # no sitemap: homepage + keyword links, two levels
        res['status'] = 'no_sitemap_fallback'
        x = fetch_page(sess, res, home, robots, pdfq)
        if x == 'STOP' or x is None:
            stop = True
            if x is None:
                res['status'] = 'unreachable'
        else:
            fr = []
            for lu, lt in x:
                if lu in seen or not C.same_site(lu, root) or C.BAD_EXT.search(lu) or lu.lower().endswith('.pdf'):
                    continue
                sc = C.score_link(lu, lt)
                if sc > 0:
                    fr.append((sc, lu)); seen.add(lu)
            fr.sort(key=lambda t: -t[0])
            lvl2 = []
            for sc, lu in fr[:8]:
                y = fetch_page(sess, res, lu, robots, pdfq)
                if y == 'STOP':
                    stop = True; break
                for lu2, lt2 in (y or []):
                    if lu2 in seen or not C.same_site(lu2, root) or C.BAD_EXT.search(lu2) or lu2.lower().endswith('.pdf'):
                        continue
                    s2 = C.score_link(lu2, lt2)
                    if s2 >= 10:
                        lvl2.append((s2, lu2)); seen.add(lu2)
            lvl2.sort(key=lambda t: -t[0])
            for s2, lu2 in lvl2[:6]:
                if stop:
                    break
                if fetch_page(sess, res, lu2, robots, pdfq) == 'STOP':
                    stop = True
    if not stop:
        k = 0
        for lu, lt in sorted(dict.fromkeys(pdfq), key=lambda t: -(10 if STRONG.search(unaccent(urllib.parse.unquote(t[0]).lower())) else 0)):
            if lu in seen or not C.same_site(lu, root):
                continue
            seen.add(lu)
            fetch_page(sess, res, lu, robots, [])
            k += 1
            if k >= PDFMAX:
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
            r = deep(s['site'])
        except Exception as e:
            r = {'site': s['site'], 'mode': 'deep2', 'status': 'crash', 'errors': [repr(e)[:200]], 'pages': [], 'emails': []}
        r['buyer_keys'] = s['buyer_keys']; r['gid'] = s.get('gid')
        with lk:
            f.write(json.dumps(r, ensure_ascii=False) + '\n'); f.flush()
        print(now(), s['site'], r['status'], r.get('sitemap_urls'), len(r.get('pages', [])), [e['email'] for e in r.get('emails', []) if e['class'].startswith('ap')][:3], flush=True)
    with ThreadPoolExecutor(int(os.environ.get('THREADS', '8'))) as ex:
        list(ex.map(work, [s for s in sites if s['site'] not in done]))


main()
