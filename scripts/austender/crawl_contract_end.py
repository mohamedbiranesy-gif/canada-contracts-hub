#!/usr/bin/env python3
"""Crawl AusTender OCDS API: all contract releases whose contract END date is on/after
the reference date, page by page (cursor pagination), checkpointing to disk.

Usage: python3 -I crawl_contract_end.py <out_dir> [from_iso] [to_iso]
Writes <out_dir>/pages/page_NNNNN.json, <out_dir>/state.json (resume), <out_dir>/crawl.log
"""
import json, os, sys, time, logging
import requests

UA = ('Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
      '(KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36')
BASE = 'https://api.tenders.gov.au/ocds/findByDates/contractEnd/{frm}/{to}'

def main():
    out_dir = sys.argv[1]
    frm = sys.argv[2] if len(sys.argv) > 2 else '2026-10-24T00:00:00Z'
    to = sys.argv[3] if len(sys.argv) > 3 else '2999-12-31T00:00:00Z'
    pages_dir = os.path.join(out_dir, 'pages')
    os.makedirs(pages_dir, exist_ok=True)
    logging.basicConfig(level=logging.INFO, format='%(asctime)s %(message)s',
                        handlers=[logging.FileHandler(os.path.join(out_dir, 'crawl.log')),
                                  logging.StreamHandler()])
    state_path = os.path.join(out_dir, 'state.json')
    state = {'next': BASE.format(frm=frm, to=to), 'page': 0, 'releases': 0, 'done': False}
    if os.path.exists(state_path):
        state = json.load(open(state_path))
        logging.info('resuming at page %s', state['page'])
    if state.get('done'):
        logging.info('already done'); return
    s = requests.Session(); s.headers['User-Agent'] = UA
    url = state['next']
    while url:
        for attempt in range(8):
            try:
                t0 = time.time()
                r = s.get(url, timeout=120)
                if r.status_code == 200:
                    break
                logging.warning('HTTP %s on %s (attempt %d)', r.status_code, url[:120], attempt)
            except Exception as e:
                logging.warning('error %s (attempt %d)', e, attempt)
            time.sleep(min(60, 2 ** attempt))
        else:
            logging.error('giving up at page %s url %s', state['page'], url); sys.exit(1)
        d = r.json()
        rels = d.get('releases', [])
        with open(os.path.join(pages_dir, f'page_{state["page"]:05d}.json'), 'w') as f:
            json.dump(d, f)
        state['page'] += 1
        state['releases'] += len(rels)
        nxt = d.get('links', {}).get('next')
        state['next'] = nxt
        if not nxt or not rels:
            state['done'] = True
        json.dump(state, open(state_path, 'w'))
        if state['page'] % 10 == 0 or state['done']:
            ids = [c.get('id') for rr in rels for c in rr.get('contracts', [])]
            logging.info('page %d releases so far %d last ids %s (%.1fs)', state['page'],
                         state['releases'], ids[:2], time.time() - t0)
        url = nxt if not state['done'] else None
        time.sleep(0.35)  # <= ~3 req/s
    logging.info('DONE pages=%d releases=%d', state['page'], state['releases'])

if __name__ == '__main__':
    main()
