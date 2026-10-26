#!/usr/bin/env python3
"""Crawl UK Contracts Finder OCDS Search for award-stage releases, month by month,
cursor-paginated, checkpointing each page to disk so it can resume.

Usage: python3 -I crawl_ocds_search.py <out_dir> <from YYYY-MM> <to YYYY-MM> [stages]
"""
import json, os, sys, time, logging, datetime as dt
import requests

UA = ('Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
      '(KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36')
BASE = ('https://www.contractsfinder.service.gov.uk/Published/Notices/OCDS/Search'
        '?publishedFrom={frm}&publishedTo={to}&stages={stages}&limit=100')
PACE = float(os.environ.get('CF_PACE', '1.5'))  # seconds per request (site throttles ~1 req/s)

def months(a, b):
    y, m = map(int, a.split('-')); y2, m2 = map(int, b.split('-'))
    while (y, m) <= (y2, m2):
        nm = (y + (m // 12), (m % 12) + 1)
        yield f'{y:04d}-{m:02d}', f'{y:04d}-{m:02d}-01T00:00:00', f'{nm[0]:04d}-{nm[1]:02d}-01T00:00:00'
        y, m = nm

def fetch(s, url, log):
    for attempt in range(14):
        try:
            r = s.get(url, timeout=180, headers={'Accept': 'application/json'})
            if r.status_code == 200:
                return r.json()
            if r.status_code == 403:
                log.warning('403 rate limit; sleeping 310s'); time.sleep(310); continue
            if r.status_code == 429:
                wait = min(120, 10 * (attempt + 1))
                log.warning('429 throttled; sleeping %ds', wait); time.sleep(wait); continue
            log.warning('HTTP %s attempt %d %s', r.status_code, attempt, url[:150])
        except Exception as e:
            log.warning('error %s attempt %d', e, attempt)
        time.sleep(min(120, 3 * 2 ** attempt))
    raise RuntimeError('giving up on ' + url)

def main():
    out_dir, a, b = sys.argv[1], sys.argv[2], sys.argv[3]
    stages = sys.argv[4] if len(sys.argv) > 4 else 'award'
    pages_dir = os.path.join(out_dir, 'pages'); os.makedirs(pages_dir, exist_ok=True)
    logging.basicConfig(level=logging.INFO, format='%(asctime)s %(message)s',
                        handlers=[logging.FileHandler(os.path.join(out_dir, 'crawl.log')), logging.StreamHandler()])
    log = logging.getLogger()
    state_path = os.path.join(out_dir, 'state.json')
    state = json.load(open(state_path)) if os.path.exists(state_path) else {'done_months': {}, 'partial': {}}
    s = requests.Session(); s.headers['User-Agent'] = UA
    total = sum(v for v in state['done_months'].values())
    for key, frm, to in months(a, b):
        if key in state['done_months']:
            continue
        part = state['partial'].get(key, {'page': 0, 'next': BASE.format(frm=frm, to=to, stages=stages), 'n': 0})
        url = part['next']
        while url:
            t0 = time.time()
            d = fetch(s, url, log)
            rels = d.get('releases', [])
            with open(os.path.join(pages_dir, f'{key}_p{part["page"]:04d}.json'), 'w') as f:
                json.dump(d, f)
            part['page'] += 1; part['n'] += len(rels)
            url = d.get('links', {}).get('next') if rels else None
            part['next'] = url
            state['partial'][key] = part
            json.dump(state, open(state_path, 'w'))
            time.sleep(max(0.0, PACE - (time.time() - t0)))
        state['done_months'][key] = part['n']; state['partial'].pop(key, None)
        total += part['n']
        json.dump(state, open(state_path, 'w'))
        log.info('month %s pages=%d releases=%d total=%d', key, part['page'], part['n'], total)
    log.info('DONE total releases %d', total)

if __name__ == '__main__':
    main()
