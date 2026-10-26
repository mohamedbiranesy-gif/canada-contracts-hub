"""Fetch given URLs, save raw HTML, print emails with context and invoice-related sentences. Appends to WORK/probe_log.jsonl."""
import sys, os, json, re, hashlib
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from common import *
import requests
from bs4 import BeautifulSoup
os.makedirs(DL2 + '/pages', exist_ok=True)
import urllib.robotparser, urllib.parse
_rob = {}


def robots_ok(u):
    h = urllib.parse.urlsplit(u)
    base = h.scheme + '://' + h.netloc
    if base not in _rob:
        rp = None
        try:
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
KW = re.compile(r'(factur|invoice|payable|comptes à payer|comptes fournisseurs|paiement|IPP|WAWF|PIEE|portail|portal|e-invoic|Peppol|mailing address|adresse postale)', re.I)
log = open(WORK + '/probe_log.jsonl', 'a')
for u in sys.argv[1:]:
    t = now()
    if not robots_ok(u):
        print('##', u, 'ROBOTS_DISALLOW'); log.write(json.dumps({'url': u, 'final_url': u, 'status': 'robots_disallow', 'retrieved_at': t, 'emails': {}}) + '\n'); continue
    try:
        r = requests.get(u, headers={'User-Agent': UA, 'Accept-Language': 'fr-CA,fr;q=0.9,en;q=0.8'}, timeout=30)
    except Exception as e:
        print('##', u, 'ERROR', e); continue
    h = hashlib.md5(u.encode()).hexdigest()[:12]
    open(DL2 + '/pages/%s.html' % h, 'wb').write(r.content)
    low = r.text[:30000].lower() if r.content[:4] != b'%PDF' else ''
    if r.status_code in (403, 429, 503) or 'cf-chl' in low or '<title>just a moment' in low or '_incapsula_resource' in low or 'radware bot manager' in low or 'you have been blocked' in low:
        print('##', u, r.status_code, 'BLOCKED_OR_CHALLENGED (skipped, not retried)'); log.write(json.dumps({'url': u, 'final_url': r.url, 'status': r.status_code, 'blocked': True, 'retrieved_at': t, 'emails': {}}) + '\n'); continue
    print('##', u, r.status_code, r.url, len(r.content), t)
    if r.content[:4] == b'%PDF':
        import subprocess
        p = DL2 + '/pages/%s.pdf' % h
        open(p, 'wb').write(r.content)
        txt = subprocess.run(['pdftotext', '-layout', p, '-'], capture_output=True, text=True).stdout
        r._content = ('<html><title>PDF</title><body><main>' + txt.replace('<', ' ') + '</main></body></html>').encode()
        r.encoding = 'utf-8'
    soup = BeautifulSoup(r.text, 'lxml')
    for x in soup(['script', 'style', 'noscript']):
        x.decompose()
    mn = soup.find('main') or soup
    text = re.sub(r'\s+', ' ', mn.get_text(' ', strip=True))
    ems = {}
    for a in soup.find_all('a', href=True):
        if a['href'].lower().startswith('mailto:'):
            e = a['href'][7:].split('?')[0].strip()
            ems.setdefault(e.lower(), '')
    for m in EM.finditer(text):
        ems[m.group(0).lower().strip('.')] = text[max(0, m.start() - 250): m.end() + 150]
    title = soup.title.get_text(strip=True) if soup.title else ''
    print('TITLE', title)
    for e, c in ems.items():
        print('  EMAIL', e, '|', c)
    hits = []
    for m in KW.finditer(text):
        hits.append(text[max(0, m.start() - 150): m.end() + 250])
        if len(hits) >= int(os.environ.get('NHITS', '6')):
            break
    for hh in hits:
        print('  KW', hh)
    log.write(json.dumps({'url': u, 'final_url': r.url, 'status': r.status_code, 'retrieved_at': t, 'saved': 'downloads/enrichment_buyers_v2/pages/%s.html' % h, 'title': title,
                          'emails': ems}, ensure_ascii=False) + '\n')
