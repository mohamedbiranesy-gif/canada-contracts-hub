"""Fetch given URLs (robots.txt honoured, <=~1.6 req/s per host, bot-check/403 pages logged and skipped), save the raw copy under
downloads/enrichment_buyers_intl/pages/, print e-mails with context and invoice-related sentences. Appends to WORK/probe_log.jsonl.
usage: python3 -I probe.py URL [URL ...]    env: NHITS (keyword snippets per page, default 4), GREP (extra regex to show context for)"""
import sys, os, json, re, hashlib, time, subprocess, urllib.parse, urllib.robotparser
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from common import *
import requests
from bs4 import BeautifulSoup
import warnings
warnings.filterwarnings('ignore')
_rob = {}
_last = {}


def wait_host(u):
    h = urllib.parse.urlsplit(u).netloc.lower()
    d = _last.get(h, 0) + 0.6 - time.time()
    if d > 0:
        time.sleep(d)
    _last[h] = time.time()


def robots_ok(u):
    h = urllib.parse.urlsplit(u)
    base = h.scheme + '://' + h.netloc
    if base not in _rob:
        rp = None
        try:
            wait_host(base)
            rr = requests.get(base + '/robots.txt', headers={'User-Agent': UA}, timeout=15)
            if rr.status_code == 200 and 'html' not in rr.headers.get('content-type', ''):
                rp = urllib.robotparser.RobotFileParser(); rp.parse(rr.text.splitlines())
        except Exception:
            rp = None
        _rob[base] = rp
    rp = _rob[base]
    try:
        return rp is None or rp.can_fetch(UA, u)
    except Exception:
        return True


EM = re.compile(r'[A-Za-z0-9._%+\-]+@[A-Za-z0-9.\-]+\.[A-Za-z]{2,}')
KW = re.compile(r'(factur|invoice|payable|comptes à payer|comptes fournisseurs|paiement des fournisseurs|e-invoic|einvoic|Peppol|Ariba|Coupa|Basware|Tungsten|Tradeshift|'
                r'Rechnung|XRechnung|Leitweg|ZRE|OZG-RE|Chorus|factuur|facturen|crediteuren|fattur|SdI|codice univoco|faktur|EAN|NemHandel|EHF|Svefaktura|lasku|verkkolasku|'
                r'e-arve|e-račun|eRačun|FACe|DIR3|e-faktur|KSeF|accounts payable|supplier portal|vendor portal)', re.I)
GREP = re.compile(os.environ['GREP'], re.I) if os.environ.get('GREP') else None
log = open(WORK + '/probe_log.jsonl', 'a')
for u in sys.argv[1:]:
    t = now()
    if not robots_ok(u):
        print('##', u, 'ROBOTS_DISALLOW (skipped)'); log.write(json.dumps({'url': u, 'final_url': u, 'status': 'robots_disallow', 'retrieved_at': t, 'emails': {}}) + '\n'); continue
    try:
        wait_host(u)
        r = requests.get(u, headers={'User-Agent': UA, 'Accept-Language': 'en;q=1.0,fr;q=0.8,de;q=0.7,es;q=0.6,*;q=0.5'}, timeout=30)
    except Exception as e:
        print('##', u, 'ERROR', type(e).__name__, str(e)[:150]); log.write(json.dumps({'url': u, 'final_url': u, 'status': 'error:' + type(e).__name__, 'retrieved_at': t, 'emails': {}}) + '\n'); continue
    h = hashlib.md5(u.encode()).hexdigest()[:12]
    ispdf = r.content[:5].startswith(b'%PDF')
    open(DL2 + '/pages/%s.%s' % (h, 'pdf' if ispdf else 'html'), 'wb').write(r.content)
    low = r.text[:30000].lower() if not ispdf else ''
    chal = ('cf-chl' in low or '<title>just a moment' in low or '_incapsula_resource' in low or 'radware bot manager' in low or 'you have been blocked' in low
            or 'validate.perfdrive.com' in low or 'px-captcha' in low or 'challenge-platform' in low)
    if r.status_code in (500, 502, 503, 504) and not chal:
        print('##', u, r.status_code, 'SERVER_ERROR (not a challenge; may retry later)'); log.write(json.dumps({'url': u, 'final_url': r.url, 'status': 'error:http%d' % r.status_code, 'retrieved_at': t, 'emails': {}}) + '\n'); continue
    if r.status_code in (401, 403, 429, 503) or 'cf-chl' in low or '<title>just a moment' in low or '_incapsula_resource' in low or 'radware bot manager' in low \
            or 'you have been blocked' in low or 'validate.perfdrive.com' in low or 'px-captcha' in low or 'challenge-platform' in low:
        print('##', u, r.status_code, 'BLOCKED_OR_CHALLENGED (skipped, not retried)'); log.write(json.dumps({'url': u, 'final_url': r.url, 'status': r.status_code, 'blocked': True, 'retrieved_at': t, 'emails': {}}) + '\n'); continue
    print('##', u, r.status_code, r.url if r.url != u else '', len(r.content), t, 'PDF' if ispdf else '')
    if ispdf:
        p = DL2 + '/pages/%s.pdf' % h
        txt = subprocess.run(['pdftotext', '-layout', p, '-'], capture_output=True, text=True).stdout
        html = '<html><title>PDF</title><body><main>' + txt.replace('<', ' ').replace('&', '&amp;') + '</main></body></html>'
    else:
        html = r.text
    soup = BeautifulSoup(html, 'lxml')
    for x in soup(['script', 'style', 'noscript']):
        x.decompose()
    mn = soup.find('main') or soup
    text = re.sub(r'\s+', ' ', mn.get_text(' ', strip=True))
    full = re.sub(r'\s+', ' ', soup.get_text(' ', strip=True))
    ems = {}
    for a in soup.find_all('a', href=True):
        if a['href'].lower().startswith('mailto:'):
            e = urllib.parse.unquote(a['href'][7:].split('?')[0]).strip()
            if EM.fullmatch(e):
                ems.setdefault(e.lower(), '')
    for m in EM.finditer(full):
        e = m.group(0).lower().strip('.')
        if not ems.get(e):
            ems[e] = full[max(0, m.start() - 250): m.end() + 150]
    title = soup.title.get_text(strip=True) if soup.title else ''
    print('TITLE', title[:150])
    for e, c in ems.items():
        print('  EMAIL', e, '|', c[-330:])
    hits = []
    for m in KW.finditer(text):
        hits.append(text[max(0, m.start() - 150): m.end() + 250])
        if len(hits) >= int(os.environ.get('NHITS', '4')):
            break
    for hh in hits:
        print('  KW', hh)
    if os.environ.get('LINKS'):
        LK = re.compile(os.environ['LINKS'], re.I)
        seenl = set()
        for a in soup.find_all('a', href=True):
            hu = urllib.parse.urljoin(r.url, a['href'].strip()).split('#')[0]
            at = a.get_text(' ', strip=True)
            if hu in seenl or hu.lower().startswith(('mailto:', 'javascript:', 'tel:')):
                continue
            if LK.search(at) or LK.search(urllib.parse.unquote(hu)):
                seenl.add(hu)
                print('  LINK', at[:80], '|', hu[:200])
    if GREP:
        for i, m in enumerate(GREP.finditer(full)):
            print('  GREP', full[max(0, m.start() - 200): m.end() + 300])
            if i >= 5:
                break
    log.write(json.dumps({'url': u, 'final_url': r.url, 'status': r.status_code, 'retrieved_at': t, 'saved': 'downloads/enrichment_buyers_intl/pages/%s.%s' % (h, 'pdf' if ispdf else 'html'),
                          'title': title, 'emails': ems}, ensure_ascii=False) + '\n')
    log.flush()
