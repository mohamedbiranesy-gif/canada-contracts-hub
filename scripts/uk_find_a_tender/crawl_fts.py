#!/usr/bin/env python3
"""Crawl UK Find a Tender OCDS release packages (stages=award) in weekly windows of
updated date, cursor-paginated; checkpoint each page to disk; resumable.

Usage: python3 -I crawl_fts.py <out_dir> <from YYYY-MM-DD> <to YYYY-MM-DD> [stages] [window_days]
"""
import json, os, sys, time, logging, datetime as dt
import requests

UA = ('Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
      '(KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36')
BASE = ('https://www.find-tender.service.gov.uk/api/1.0/ocdsReleasePackages'
        '?updatedFrom={frm}&updatedTo={to}&stages={stages}&limit=100')
PACE = float(os.environ.get('FTS_PACE', '1.0'))

def windows(a, b, days):
    d = dt.date.fromisoformat(a); end = dt.date.fromisoformat(b)
    while d <= end:
        e = min(d + dt.timedelta(days=days), end + dt.timedelta(days=1))
        yield d.isoformat(), f'{d.isoformat()}T00:00:00', f'{e.isoformat()}T00:00:00'
        d = e

def fetch(s, url, log):
    for attempt in range(14):
        try:
            r = s.get(url, timeout=180, headers={'Accept': 'application/json'})
            if r.status_code == 200:
                return r.json()
            if r.status_code in (403, 429):
                wait = min(300, 15 * (attempt + 1))
                log.warning('%s throttled; sleeping %ds', r.status_code, wait); time.sleep(wait); continue
            log.warning('HTTP %s attempt %d %s', r.status_code, attempt, url[:150])
        except Exception as e:
            log.warning('error %s attempt %d', e, attempt)
        time.sleep(min(120, 3 * 2 ** attempt))
    raise RuntimeError('giving up on ' + url)

def main():
    out_dir, a, b = sys.argv[1], sys.argv[2], sys.argv[3]
    stages = sys.argv[4] if len(sys.argv) > 4 else 'award'
    days = int(sys.argv[5]) if len(sys.argv) > 5 else 7
    pages_dir = os.path.join(out_dir, 'pages'); os.makedirs(pages_dir, exist_ok=True)
    logging.basicConfig(level=logging.INFO, format='%(asctime)s %(message)s',
                        handlers=[logging.FileHandler(os.path.join(out_dir, 'crawl.log')), logging.StreamHandler()])
    log = logging.getLogger()
    state_path = os.path.join(out_dir, 'state.json')
    state = json.load(open(state_path)) if os.path.exists(state_path) else {'done': {}, 'partial': {}}
    s = requests.Session(); s.headers['User-Agent'] = UA
    total = sum(state['done'].values())
    for key, frm, to in windows(a, b, days):
        if key in state['done']:
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
        state['done'][key] = part['n']; state['partial'].pop(key, None)
        total += part['n']
        json.dump(state, open(state_path, 'w'))
        log.info('window %s pages=%d releases=%d total=%d', key, part['page'], part['n'], total)
    log.info('DONE total releases %d', total)

if __name__ == '__main__':
    main()
