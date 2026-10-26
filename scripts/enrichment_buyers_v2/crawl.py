"""Stage 2: polite crawler over buyer websites looking for supplier-invoicing / AP / procurement role mailboxes.
usage: python3 -I crawl.py <sites.json> <out.jsonl>
sites.json: list of {"site": url, "buyer_keys": [...]} in priority order. Already-crawled sites in out.jsonl are skipped.
"""
import sys, os, json, re, time, threading, queue, urllib.parse, urllib.robotparser
from concurrent.futures import ThreadPoolExecutor
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from common import *
import requests
from bs4 import BeautifulSoup
import warnings
warnings.filterwarnings('ignore')

SITES, OUT = sys.argv[1], sys.argv[2]
MAXPAGES = int(os.environ.get('MAXPAGES', '14'))
DELAY = 0.7  # seconds between requests to the same host (<= ~1.4 req/s)
lock = threading.Lock()

KW_STRONG = ['factur', 'invoice', 'payable', 'comptes-fournisseurs', 'comptes-a-payer', 'paiement-des-fournisseurs', 'paiement-fournisseur',
             'accounts-payable', 'billing', 'supplier', 'fournisseur', 'vendor', 'doing-business', 'faire-affaire', 'faire-des-affaires', 'affaires-avec']
KW_MED = ['approvisionnement', 'procurement', 'purchasing', 'achats', 'acquisition', 'appels-d-offres', 'appel-d-offres', 'appels-doffres', 'soumission',
          'contrats', 'contracts', 'tender', 'bids', 'finance', 'tresorerie', 'comptabilite', 'nous-joindre', 'contact', 'joindre', 'coordonnees',
          'services-administratifs', 'administration', 'business', 'affaires']
TXT_STRONG = ['factur', 'invoice', 'payable', 'fournisseur', 'supplier', 'vendor', 'faire affaire', 'doing business', 'comptes a payer', 'paiement']
TXT_MED = ['approvisionnement', 'procurement', 'purchasing', 'achat', 'acquisition', 'appel d offres', 'appels d offres', 'contrat', 'contract', 'tender',
           'finance', 'tresorerie', 'comptabilite', 'nous joindre', 'contact', 'coordonnees']
EMAIL_RE = re.compile(r'[A-Za-z0-9._%+\-]+@[A-Za-z0-9.\-]+\.[A-Za-z]{2,}')
BAD_EXT = re.compile(r'\.(jpg|jpeg|png|gif|svg|zip|docx?|xlsx?|pptx?|mp4|mp3|webp|ico|css|js)(\?|$)', re.I)

ROLE_SUB = ['info', 'reception', 'accueil', 'admin', 'contact', 'communication', 'mairie', 'hoteldeville', 'municipal', 'ville', 'greff', 'secretariat',
            'tresor', 'financ', 'compta', 'factur', 'invoice', 'payable', 'fournisseur', 'supplier', 'vendor', 'approvision', 'achat', 'purchas', 'procure',
            'acquisition', 'contrat', 'contract', 'tender', 'soumission', 'appeldoffre', 'appelsdoffres', 'bid', 'paie', 'payment', 'paiement', 'urbanism',
            'travaux', 'loisir', 'taxe', 'perception', 'revenu', 'recette', 'service', 'client', 'support', 'help', 'media', 'plainte', 'ombuds',
            'emploi', 'career', 'job', 'inspect', 'permis', 'bureau', 'office', 'general', 'courrier', 'webmaster', 'receivable', 'billing', 'account',
            'compte', 'direction', 'question', 'demande', 'requete', 'citoyen', 'public', 'enquiries', 'enquiry', 'inquir', 'mrc', 'cp.', 'secretary', 'clerk',
            'treasur', 'records', 'privacy', 'atip', 'aiprp', 'foi', 'cour', 'admission', 'registra', 'library', 'biblio', 'immeuble', 'ressources',
            'materiel', 'logistique', 'magasin', 'stores', 'mailroom', 'reclamation', 'claims', 'audit', 'portail', 'portal', 'urgence', 'securite', 'police',
            'incendie', 'transport', 'habitation', 'environnement', 'eau', 'water', 'parcs', 'culture', 'sport', 'evaluation', 'cour', 'municipale']
ROLE_TOK = {'dg', 'ap', 'cp', 'rh', 'hr', 'ti', 'it', 'sg', 'ar', 'ca', 'ops', 'fin', 'dga', 'cs', 'po', 'pa', 'ss', 'ville', 'mun', 'adm', 'appro', 'sti'}
AP_SUB = ['factur', 'invoice', 'payable', 'comptesapayer', 'comptes.a.payer', 'accountspayable', 'apinvoice', 'ap.invoice', 'cptespayables', 'comptespay',
          'cpayables', 'apdept', 'fournisseurs.paiement', 'paiementfournisseur', 'paiement.fournisseur', 'paiements', 'payment', 'billing']
AP_TOK = {'ap', 'cp', 'cap', 'apm'}
PROC_SUB = ['approvision', 'appro', 'achat', 'purchas', 'procure', 'acquisition', 'contrat', 'contract', 'tender', 'soumission', 'appeldoffre',
            'appelsdoffres', 'bid', 'fournisseur', 'supplier', 'vendor', 'sourcing', 'gestioncontractuelle', 'commercial']
AP_CTX = ['factur', 'invoice', 'payable', 'comptes a payer', 'paiement des fournisseurs', 'payment to supplier', 'supplier payment', 'paiement aux fournisseurs']
PORTAL_CTX = ['portail fournisseur', 'portail des fournisseurs', 'supplier portal', 'vendor portal', 'invoice portal', 'facturation electronique',
              'facture electronique', 'e-invoic', 'einvoic', 'electronic invoic', 'ariba', 'coupa', 'jaggaer', 'basware', 'tungsten', 'ipp.gov', 'invoice processing platform',
              'portail de facturation', 'depot de facture', 'plateforme de facturation']


LONG_STEMS = [x for x in ROLE_SUB + AP_SUB + PROC_SUB if len(x) >= 5]


def looks_personal(lp):
    toks = [t for t in re.split(r'[._\-+]', lp) if t]
    if len(toks) >= 2 and all(t.isalpha() for t in toks):
        for t in toks:
            if t in ROLE_TOK or t in AP_TOK or t in ('info', 'ville', 'mrc', 'dg', 'media', 'atip', 'aiprp', 'foi', 'achat', 'achats', 'appro', 'paie'):
                return False
            if any(st in t for st in LONG_STEMS):
                return False
        return True
    if re.fullmatch(r'[a-z]+[._-][a-z]+\d+', lp):
        return True
    return False


STRONG_END = ('invoices', 'invoice', 'payable', 'payables', 'factures', 'facture', 'facturation', 'procurement', 'purchasing',
              'approvisionnement', 'approvisionnements', 'achats', 'contracts', 'tenders', 'soumissions', 'fournisseurs', 'suppliers', 'vendors',
              'finance', 'comptabilite', 'accounting', 'info', 'reception', 'commercial')
STEMS = sorted({x for x in ROLE_SUB + AP_SUB + PROC_SUB if len(x) >= 4 and '.' not in x}, key=len)


def token_gate(lp):
    for t in [t for t in re.split(r'[._\-+]', lp) if t]:
        t2 = re.sub(r'\d+$', '', t)
        if t2 in ROLE_TOK or t2 in AP_TOK or t2 in ('dg', 'mrc', 'cp', 'ap'):
            return True
        if any(t2.startswith(st) for st in STEMS) or t2.endswith(STRONG_END):
            return True
    return lp in SHORT_OK


SHORT_OK = {'srf', 'drf', 'dse', 'sic', 'dst', 'adm', 'mun', 'urb', 'env', 'sec', 'dir', 'rh', 'ti', 'dg', 'cp', 'ap', 'tp', 'foi', 'cse',
            'sas', 'ssf', 'uta', 'dpo', 'ogc', 'bao', 'mcu', 'pfp', 'sg', 'dga', 'ca', 'cs', 'it', 'hr', 'fin', 'cap', 'cfp'}


def localpart_class(email, ctx):
    lp = email.split('@')[0].lower()
    if looks_personal(lp) or not token_gate(lp):
        return None
    toks = set(re.split(r'[._\-+]', lp))
    is_ap = any(s in lp for s in AP_SUB if s != 'factur') or bool(re.search(r'(?<!manu)factur', lp)) or bool(toks & AP_TOK)
    is_proc = any(s in lp for s in PROC_SUB) or 'appro' in toks
    is_role = is_ap or is_proc or any(s in lp for s in ROLE_SUB if len(s) >= 4) or bool(toks & ROLE_TOK) or lp in SHORT_OK
    if not is_role:
        return None
    c = norm(ctx)
    if any(x in lp for x in ('receivable', 'recevable', 'client', 'debiteur', 'taxation', 'perception', 'customer', 'waterbill', 'utilitybill',
                                'billing', 'propertytax', 'taxes', 'collections', 'parking', 'ticket')) or (toks & {'ar', 'tax', 'water', 'utility', 'utilities'}):
        is_ap = False
        return 'general'
    if is_ap:
        return 'ap'
    if any(w in c for w in [norm(x) for x in AP_CTX]) and any(s in lp for s in ['financ', 'compta', 'tresor', 'fournisseur', 'supplier', 'vendor', 'account', 'compte']):
        return 'ap_context'
    if is_proc:
        return 'procurement'
    return 'general'


class Host:
    def __init__(self):
        self.last = 0
        self.lk = threading.Lock()

    def wait(self):
        with self.lk:
            d = self.last + DELAY - time.time()
            if d > 0:
                time.sleep(d)
            self.last = time.time()


hosts = {}


def host_of(u):
    return urllib.parse.urlsplit(u).netloc.lower()


def get(sess, u, robots):
    h = host_of(u)
    with lock:
        H = hosts.setdefault(h, Host())
    if robots is not None:
        try:
            if not robots.can_fetch(UA, u):
                return None, 'robots_disallow'
        except Exception:
            pass
    H.wait()
    try:
        r = sess.get(u, timeout=(10, 20), allow_redirects=True, stream=True)
        ct = r.headers.get('content-type', '')
        if 'html' not in ct and 'text' not in ct:
            r.close()
            return None, 'non_html:%s' % ct[:40]
        body = r.raw.read(3_000_000, decode_content=True)
        enc = r.encoding or 'utf-8'
        if not r.encoding or r.encoding.lower() in ('iso-8859-1', 'latin-1', 'ascii'):
            try:
                body.decode('utf-8'); enc = 'utf-8'
            except UnicodeDecodeError:
                enc = r.encoding or 'cp1252'
        txt = body.decode(enc, errors='replace')
        return (r.status_code, r.url, txt, dict(r.headers)), None
    except Exception as e:
        return None, 'error:%s' % type(e).__name__


def challenged(status, txt, headers):
    t = txt[:30000].lower()
    strong = ('cf-chl' in t or 'challenge-platform' in t or '_incapsula_resource' in t or '<title>just a moment' in t
              or 'validate.perfdrive.com' in t or 'radware bot manager' in t or 'px-captcha' in t)
    return status in (403, 429, 503) or strong


def score_link(href, text):
    h = norm(urllib.parse.unquote(href)).replace(' ', '-')
    t = norm(text)
    s = 0
    if any(k in h for k in KW_STRONG) or any(k in t for k in TXT_STRONG):
        s += 10
    if any(k in h for k in KW_MED) or any(k in t for k in TXT_MED):
        s += 3
    if any(k in h for k in ['factur', 'invoice', 'payable']) or any(k in t for k in ['factur', 'invoice', 'payable']):
        s += 10
    if any(k in h for k in ['emploi', 'career', 'job', 'news', 'nouvelles', 'actualit', 'evenement', 'event', 'calendrier', 'blog', 'facebook', 'twitter',
                             'linkedin', 'youtube', 'instagram', 'proces-verba', 'minutes', 'seance']):
        s -= 8
    return s


def extract(url, html):
    soup = BeautifulSoup(html, 'lxml')
    for t in soup(['script', 'style', 'noscript']):
        t.decompose()
    title = (soup.title.string or '').strip() if soup.title and soup.title.string else ''
    text = soup.get_text(' ', strip=True)
    mn = soup.find('main') or soup.find(attrs={'role': 'main'}) or soup.find(id=re.compile('content|main', re.I))
    maintext = mn.get_text(' ', strip=True) if mn else text
    links = []
    emails = {}
    for a in soup.find_all('a', href=True):
        href = a['href'].strip()
        at = a.get_text(' ', strip=True)
        if href.lower().startswith('mailto:'):
            e = urllib.parse.unquote(href[7:].split('?')[0]).strip()
            if EMAIL_RE.fullmatch(e):
                par = a.find_parent(['p', 'li', 'td', 'div', 'section'])
                ctx = par.get_text(' ', strip=True)[:400] if par else at
                emails.setdefault(e.lower(), ctx)
            continue
        if href.startswith('#') or href.lower().startswith(('javascript:', 'tel:')):
            continue
        links.append((urllib.parse.urljoin(url, href).split('#')[0], at))
    for m in EMAIL_RE.finditer(text):
        e = m.group(0).strip('.').lower()
        if e not in emails:
            emails[e] = text[max(0, m.start() - 220): m.end() + 180]
    return title, text, links, emails, maintext


def same_site(u, root_host):
    h = host_of(u)
    rh = root_host[4:] if root_host.startswith('www.') else root_host
    return h == root_host or h.endswith('.' + rh) or rh.endswith('.' + h.replace('www.', ''))


def crawl_site(site):
    sess = requests.Session()
    sess.headers.update({'User-Agent': UA, 'Accept-Language': 'fr-CA,fr;q=0.9,en;q=0.8'})
    res = {'site': site, 'started_at': now(), 'pages': [], 'emails': [], 'portal_links': [], 'invoice_snippets': [], 'status': 'ok', 'errors': []}
    home = site if site.startswith('http') else 'https://' + site
    robots = None
    try:
        rp = urllib.robotparser.RobotFileParser()
        rr = sess.get(urllib.parse.urljoin(home, '/robots.txt'), timeout=(10, 15))
        if rr.status_code == 200 and 'html' not in rr.headers.get('content-type', ''):
            rp.parse(rr.text.splitlines()); robots = rp
    except Exception:
        pass
    r, err = get(sess, home, robots)
    if r is None and home.startswith('https://'):
        r, err = get(sess, 'http://' + home[8:], robots)
    if r is None:
        res['status'] = 'unreachable'; res['errors'].append(err); return res
    st, final, html, hdr = r
    if challenged(st, html, hdr):
        res['status'] = 'blocked_or_challenged'; res['errors'].append('HTTP %s at home page; challenge markers' % st); return res
    if st >= 400:
        res['status'] = 'http_%s' % st; return res
    res['final_url'] = final
    root_host = host_of(final)
    seen = {home, final}
    frontier = []

    def process(u, st, html):
        title, text, links, emails, mt = extract(u, html)
        res['pages'].append({'url': u, 'status': st, 'title': title[:200], 'retrieved_at': now()})
        for e, ctx in emails.items():
            cl = localpart_class(e, ctx + ' ' + title + ' ' + u)
            if cl is None:
                res.setdefault('dropped_nonrole', 0)
                res['dropped_nonrole'] = res.get('dropped_nonrole', 0) + 1
                continue
            res['emails'].append({'email': e, 'class': cl, 'page_url': u, 'page_title': title[:150], 'snippet': re.sub(r'\s+', ' ', ctx)[:400], 'retrieved_at': now()})
        nt = unaccent(mt.lower())
        for kw in ['factur', 'invoice']:
            i = nt.find(kw)
            if i >= 0 and (any(k in norm(u) for k in ['factur', 'invoice', 'fournisseur', 'supplier', 'vendor', 'payable', 'affaire', 'business']) or any(k in norm(title) for k in ['factur', 'invoice', 'fournisseur', 'supplier', 'vendor'])):
                # take original-text window around first invoice mention
                ot = text
                j = norm(ot[:]).find(kw)
                res['invoice_snippets'].append({'page_url': u, 'title': title[:150], 'snippet': re.sub(r'\s+', ' ', mt[max(0, i - 300): i + 900])})
                break
        for lu, lt in links:
            ln = norm(lt + ' ' + lu)
            if any(norm(p) in ln for p in PORTAL_CTX):
                res['portal_links'].append({'url': lu, 'anchor': lt[:150], 'page_url': u})
        return links

    links = process(final, st, html)
    for lu, lt in links:
        if lu in seen or not same_site(lu, root_host) or BAD_EXT.search(lu) or lu.lower().endswith('.pdf'):
            continue
        s = score_link(lu, lt)
        if s > 0:
            frontier.append((s, lu, lt)); seen.add(lu)
    n = 1
    level2 = []
    frontier.sort(key=lambda x: -x[0])
    for s, lu, lt in frontier[:9]:
        if n >= MAXPAGES:
            break
        r, err = get(sess, lu, robots); n += 1
        if r is None:
            res['errors'].append('%s %s' % (err, lu)); continue
        st, fu, html, hdr = r
        if challenged(st, html, hdr):
            res['errors'].append('challenge at %s' % lu); res['status'] = 'partially_blocked'; break
        if st >= 400:
            continue
        for lu2, lt2 in process(fu, st, html):
            if lu2 in seen or not same_site(lu2, root_host) or BAD_EXT.search(lu2) or lu2.lower().endswith('.pdf'):
                continue
            s2 = score_link(lu2, lt2)
            if s2 >= 10:
                level2.append((s2, lu2, lt2)); seen.add(lu2)
    level2.sort(key=lambda x: -x[0])
    for s, lu, lt in level2:
        if n >= MAXPAGES:
            break
        r, err = get(sess, lu, robots); n += 1
        if r is None:
            continue
        st, fu, html, hdr = r
        if challenged(st, html, hdr) or st >= 400:
            continue
        process(fu, st, html)
    res['finished_at'] = now()
    # dedupe emails keep first evidence
    d = {}
    for e in res['emails']:
        d.setdefault((e['email'], e['class']), e)
    res['emails'] = list(d.values())
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
    todo = [s for s in sites if s['site'] not in done]
    print('todo', len(todo), 'done', len(done), flush=True)
    f = open(OUT, 'a')

    def work(s):
        try:
            r = crawl_site(s['site'])
        except Exception as e:
            r = {'site': s['site'], 'status': 'crash', 'errors': [repr(e)[:300]], 'pages': [], 'emails': []}
        r['buyer_keys'] = s['buyer_keys']
        with lock:
            f.write(json.dumps(r, ensure_ascii=False) + '\n'); f.flush()
        return r['status']
    with ThreadPoolExecutor(int(os.environ.get('THREADS', '20'))) as ex:
        for i, st in enumerate(ex.map(work, todo)):
            if i % 25 == 0:
                print(now(), i, st, flush=True)


if __name__ == '__main__':
    main()
