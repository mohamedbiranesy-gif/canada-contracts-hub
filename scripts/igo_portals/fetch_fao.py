#!/usr/bin/env python3 -I
"""Download the FAO quarterly 'POs above USD 100k' PDFs (vendor-actions 502 and service-provider-actions 507,
excluding the EU-only and PAGODA subsets which duplicate rows) and grep them for Canada.
Usage: python3 -I fetch_fao.py <pdf_links.json> <outdir>
"""
import sys, os, json, re, time, datetime, subprocess, hashlib
import requests

links = json.load(open(sys.argv[1]))
out = sys.argv[2]
os.makedirs(out, exist_ok=True)
H = {"User-Agent": "contracts-research/1.0"}
log = []
seen = set()
for l in links:
    href = l['href']
    if not href.startswith('http'):
        href = 'https://www.fao.org' + href
    low = href.lower()
    if 'eu_project' in low or 'eu-project' in low or 'pagoda' in low or '_eu_' in low or 'eu_above' in low or 'eu-above' in low or '_eu-' in low or 'q1_eu_' in low or '/eu_' in low or 'ec_regulations' in low or 'q1_507_eu' in low:
        continue
    key = href.split('?')[0]
    if key in seen:
        continue
    seen.add(key)
    m = re.search(r'statistics/(\d{4})(?:q1)?/(?:(q\d)/)?', href)
    year = m.group(1) if m else 'x'
    q = m.group(2) if m and m.group(2) else ('q1' if '2025q1/vendor' in href or '2025q1/service' in href else 'qx')
    kind = '502_vendor' if '502' in os.path.basename(key) or 'vendor-actions' in href else '507_service_provider'
    fn = os.path.join(out, f"fao_{year}_{q}_{kind}_{hashlib.md5(key.encode()).hexdigest()[:6]}.pdf")
    t = datetime.datetime.now(datetime.timezone.utc).isoformat(timespec='seconds')
    try:
        r = requests.get(href, headers=H, timeout=120)
        open(fn, 'wb').write(r.content)
        txt = subprocess.run(['pdftotext', '-layout', fn, '-'], capture_output=True, text=True).stdout
        ncan = len(re.findall(r'\bCanada\b', txt))
        log.append({'url': href, 'file': fn, 'status': r.status_code, 'bytes': len(r.content), 'retrieved_at': t, 'canada_mentions': ncan, 'year': year, 'quarter': q, 'kind': kind})
        print(year, q, kind, r.status_code, len(r.content), 'canada', ncan, flush=True)
    except Exception as e:
        log.append({'url': href, 'file': fn, 'status': 'ERR', 'error': str(e)[:200], 'retrieved_at': t})
        print('ERR', href, e)
    time.sleep(0.5)
json.dump(log, open(os.path.join(out, 'fetch_log.json'), 'w'), indent=1)
