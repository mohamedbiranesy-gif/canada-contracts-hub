"""Deep-search pass 3 (W3): section-focused crawl of the websites of the LARGEST organisations still lacking an AP mailbox / invoice portal.
Unlike deep2 (sitemap ranking, <=16 pages), deep3 does a best-first walk through the supplier / finance / procurement / contact sections:
start = homepage + supplier-ish pages already seen by earlier passes + deep2 sitemap candidates; links scored by French/English keywords
(fournisseur, faire affaire, facturation, comptes payables/à payer/fournisseurs, dépôt direct, conditions générales, bon de commande,
supplier, vendor, invoice, accounts payable, purchase order terms, doing business, finance, nous joindre, contact ...), depth <= 3,
<= MAXHTML pages + <= MAXPDF linked PDFs (pdftotext). It also records phone numbers printed next to an accounts-payable heading.
Politeness unchanged: robots.txt honoured, one queue per host, 0.7 s spacing (<= ~1.4 req/s), bot-check/403/429/503 stops the site (never retried around).
usage: python3 -I deep3.py <sites.json> <out.jsonl>     sites.json: [{"site": url, "buyer_keys": [...], "gid": ..., "seeds": [...]}]"""
import sys, os, json, re, gzip, subprocess, tempfile, heapq, urllib.parse, urllib.robotparser, threading
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
SITES, OUT = sys.argv[1], sys.argv[2]
sys.argv = [sys.argv[0], '/dev/null', '/dev/null']
import importlib.util
spec = importlib.util.spec_from_file_location('crawlmod', os.path.join(os.path.dirname(os.path.abspath(__file__)), 'crawl.py'))
C = importlib.util.module_from_spec(spec); spec.loader.exec_module(C)
import requests
from concurrent.futures import ThreadPoolExecutor
from common import *

MAXHTML = int(os.environ.get('MAXHTML', '45'))
MAXPDF = int(os.environ.get('MAXPDF', '14'))
lk = threading.Lock()

S_TOP = re.compile(r'(factur|invoice|payable|comptes?[ -]?(a|à)[ -]?payer|comptes?[ -]payables?|comptes?[ -]fournisseurs?|paiement[s]? (des |aux )?fournisseurs?|'
                   r'supplier payment|vendor payment|depot direct|dépôt direct|direct deposit|virement|\beft\b|guide (du |des )?fournisseurs?|supplier guide|vendor guide|'
                   r'conditions g(e|é)n(e|é)rales|terms and conditions|purchase order|bon de commande|modalit(e|é)s de paiement|payment terms)', re.I)
S_MID = re.compile(r'(fournisseur|supplier|vendor|faire affaire|faire des affaires|doing business|business with|approvisionnement|procurement|purchasing|achats?\b|'
                   r'acquisitions?|appels? d.offres|contrats?|finances?|comptabilit|accounting|financial services|services financiers|ressources financi|'
                   r'tr(e|é)sorerie|treasury|partenaires|partners|entreprises)', re.I)
S_LOW = re.compile(r'(nous joindre|joindre|contact|coordonn(e|é)es|about|(a|à) propos|administration|gouvernance|directions?|services administratifs|organisation)', re.I)
S_BAD = re.compile(r'(emploi|carri(e|è)re|career|job|nouvelles?|news|communiqu|actualit|(e|é)v(e|é)nement|event|calendrier|calendar|blog|facebook|twitter|linkedin|'
                   r'youtube|instagram|proc(e|è)s.verba|minutes|s(e|é)ance|ordre du jour|agenda|r(e|è)glement|bylaw|budget|rapport annuel|annual report|'
                   r'(e|é)tats financiers|financial statement|taxe|tax bill|permis|permit|stationnement|parking|loisir|recreation|piscine|bibliot|library|'
                   r'collecte|garbage|recycl|patient|usager|visiteur|visitor|don |donate|fondation|foundation|bourse|scholar|admission|(e|é)tudiant|student|'
                   r'cours |course|programme d|program|recherche|research|login|connexion|panier|cart|/en/|/english/)', re.I)
PDF_OK = re.compile(r'(d(e|é)p(o|ô)t|direct|fournisseur|factur|paiement|payment|vendor|supplier|invoice|payable|comptes|eft|virement|conditions|terms|guide|'
                    r'bon de commande|purchase order|formulaire|form|achat|approvisionnement|procurement)', re.I)
PHONE = re.compile(r'(?:\+?1[ .-]?)?\(?\b[2-9]\d{2}\)?[ .-]?\d{3}[ .-]?\d{4}\b(?:\s*(?:poste|ext\.?|x)\s*\d{1,6})?')
APHEAD = re.compile(r'(comptes?\s+(?:à|a)\s+payer|comptes?\s+payables?|comptes?\s+fournisseurs?|accounts?\s+payable|paiement\s+des\s+fournisseurs)', re.I)


def lscore(u, t):
    s = urllib.parse.unquote(u).lower().replace('-', ' ').replace('_', ' ')
    tt = (t or '').lower()
    both = s + ' ' + tt
    if S_BAD.search(both) and not S_TOP.search(both):
        return -1
    sc = 0
    if S_TOP.search(both):
        sc += 20
    if S_MID.search(both):
        sc += 8
    if S_LOW.search(both):
        sc += 3
    return sc


def get_raw(sess, u, robots, limit=8_000_000):
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


def scan_text(res, u, title, text):
    for m in C.EMAIL_RE.finditer(text):
        e = m.group(0).strip('.').lower()
        ctx = text[max(0, m.start() - 250): m.end() + 150]
        cl = C.localpart_class(e, ctx + ' ' + title + ' ' + u)
        if cl:
            res['emails'].append({'email': e, 'class': cl, 'page_url': u, 'page_title': title[:150], 'snippet': re.sub(r'\s+', ' ', ctx)[:400], 'retrieved_at': now()})
    nt = unaccent(text.lower())
    for kw in ['factur', 'invoice']:
        i = nt.find(kw)
        if i >= 0:
            res['invoice_snippets'].append({'page_url': u, 'title': title[:150], 'snippet': re.sub(r'\s+', ' ', text[max(0, i - 300): i + 900])})
            break
    for m in APHEAD.finditer(text):
        win = text[m.start(): m.end() + 220]
        ph = PHONE.search(win)
        if ph:
            res['ap_phone_snippets'].append({'page_url': u, 'title': title[:150], 'phone': ph.group(0), 'snippet': re.sub(r'\s+', ' ', text[max(0, m.start() - 120): m.end() + 260])})
            break


def fetch(sess, res, u, robots):
    """returns list of (link, anchor) or None; 'STOP' on challenge"""
    if u.lower().split('?')[0].endswith('.pdf'):
        b, err = get_raw(sess, u, robots)
        t = pdf_text(b)
        if not t:
            res['errors'].append('%s %s' % (err or 'not_pdf', u)); return None
        t = re.sub(r'[ \t]+', ' ', t)
        res['pages'].append({'url': u, 'status': 200, 'title': 'PDF', 'retrieved_at': now()})
        scan_text(res, u, 'PDF ' + urllib.parse.unquote(u.rsplit('/', 1)[-1]), re.sub(r'\s+', ' ', t))
        return []
    r, err = C.get(sess, u, robots)
    if r is None:
        res['errors'].append('%s %s' % (err, u)); return None
    st, fu, html, hdr = r
    if C.challenged(st, html, hdr):
        res['status'] = 'partially_blocked'; res['errors'].append('challenge/HTTP %s at %s' % (st, u)); return 'STOP'
    if st >= 400:
        res['errors'].append('http %s %s' % (st, u)); return None
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
    for m in APHEAD.finditer(text):
        win = text[m.start(): m.end() + 220]
        ph = PHONE.search(win)
        if ph:
            res['ap_phone_snippets'].append({'page_url': fu, 'title': title[:150], 'phone': ph.group(0), 'snippet': re.sub(r'\s+', ' ', text[max(0, m.start() - 120): m.end() + 260])})
            break
    for lu, lt in links:
        ln = norm(lt + ' ' + lu)
        if any(norm(p) in ln for p in C.PORTAL_CTX):
            res['portal_links'].append({'url': lu, 'anchor': lt[:150], 'page_url': fu})
    return links


def deep(s):
    site = s['site']
    sess = requests.Session(); sess.headers.update({'User-Agent': UA, 'Accept-Language': 'fr-CA,fr;q=0.9,en;q=0.8'})
    home = site if site.startswith('http') else 'https://' + site
    res = {'site': site, 'mode': 'deep3', 'started_at': now(), 'pages': [], 'emails': [], 'portal_links': [], 'invoice_snippets': [], 'ap_phone_snippets': [],
           'status': 'ok', 'errors': []}
    robots = None
    try:
        rr = sess.get(urllib.parse.urljoin(home, '/robots.txt'), timeout=(10, 15))
        if rr.status_code == 200 and 'html' not in rr.headers.get('content-type', ''):
            rp = urllib.robotparser.RobotFileParser(); rp.parse(rr.text.splitlines()); robots = rp
        elif rr.status_code in (403, 429):
            res['status'] = 'blocked_or_challenged'; res['errors'].append('robots.txt HTTP %s' % rr.status_code); return res
    except Exception as e:
        res['errors'].append('robots %s' % type(e).__name__)
    roots = {C.host_of(home)}
    for x in s.get('extra_hosts', []):
        roots.add(x)
    def same(u):
        return any(C.same_site(u, r) for r in roots)
    heap = []
    seen = set()
    def push(u, sc, depth):
        u = u.split('#')[0]
        if u in seen or not same(u) or C.BAD_EXT.search(u):
            return
        seen.add(u)
        heapq.heappush(heap, (-sc, depth, u))
    push(home, 5, 0)
    for u in s.get('seeds', []):
        push(u, 30, 1)
    nh = npdf = 0
    while heap and (nh < MAXHTML or npdf < MAXPDF):
        negsc, depth, u = heapq.heappop(heap)
        ispdf = u.lower().split('?')[0].endswith('.pdf')
        if ispdf and npdf >= MAXPDF or (not ispdf and nh >= MAXHTML):
            continue
        links = fetch(sess, res, u, robots)
        if depth == 0 and res['pages']:
            nh0 = C.host_of(res['pages'][-1]['url'])
            if nh0 and not same(res['pages'][-1]['url']):
                roots.add(nh0); res['moved_to'] = nh0   # organisation site moved to a new hostname (redirect)
        if ispdf:
            npdf += 1
        else:
            nh += 1
        if links == 'STOP':
            break
        if not links or depth >= 3:
            continue
        for lu, lt in links:
            if lu.lower().split('?')[0].endswith('.pdf'):
                if PDF_OK.search(lt or '') or PDF_OK.search(urllib.parse.unquote(lu.rsplit('/', 1)[-1])):
                    sc = lscore(lu, lt)
                    if sc >= 0:
                        push(lu, sc + 4, depth + 1)
                continue
            sc = lscore(lu, lt)
            if sc >= 8 or (sc >= 3 and depth == 0):
                push(lu, sc - depth, depth + 1)
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
            r = deep(s)
        except Exception as e:
            r = {'site': s['site'], 'mode': 'deep3', 'status': 'crash', 'errors': [repr(e)[:200]], 'pages': [], 'emails': []}
        r['buyer_keys'] = s['buyer_keys']; r['gid'] = s.get('gid')
        with lk:
            f.write(json.dumps(r, ensure_ascii=False) + '\n'); f.flush()
        print(now(), s['site'], r['status'], len(r.get('pages', [])), [e['email'] for e in r.get('emails', []) if e['class'].startswith('ap')][:3],
              [p['phone'] for p in r.get('ap_phone_snippets', [])][:2], flush=True)
    with ThreadPoolExecutor(int(os.environ.get('THREADS', '8'))) as ex:
        list(ex.map(work, [s for s in sites if s['site'] not in done]))


main()
