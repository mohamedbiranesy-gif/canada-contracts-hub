#!/usr/bin/env python3
"""Supplementary crawl of Contracts Finder OCDS Search (stages=award) for the window after the
OCP bulk snapshot (published 2026-10-05T00:00:00 .. 2026-10-26T00:00:00), one request per page,
slow pace to respect the ~1 req/s throttle (429 -> sleep)."""
import json, os, sys, time, logging, requests
UA = ('Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36')
out_dir, frm, to = sys.argv[1], sys.argv[2], sys.argv[3]
os.makedirs(out_dir, exist_ok=True)
logging.basicConfig(level=logging.INFO, format='%(asctime)s %(message)s',
                    handlers=[logging.FileHandler(os.path.join(out_dir, 'crawl.log')), logging.StreamHandler()])
state_path = os.path.join(out_dir, 'state.json')
url = (f'https://www.contractsfinder.service.gov.uk/Published/Notices/OCDS/Search?publishedFrom={frm}&publishedTo={to}&stages=award&limit=100')
state = {'next': url, 'page': 0, 'n': 0, 'done': False}
if os.path.exists(state_path):
    state = json.load(open(state_path))
s = requests.Session(); s.headers['User-Agent'] = UA
while state['next'] and not state['done']:
    for attempt in range(20):
        try:
            r = s.get(state['next'], timeout=180, headers={'Accept': 'application/json'})
            if r.status_code == 200:
                break
            wait = min(300, 20 * (attempt + 1))
            logging.warning('HTTP %s; sleeping %ds', r.status_code, wait); time.sleep(wait)
        except Exception as e:
            logging.warning('error %s', e); time.sleep(30)
    else:
        sys.exit('giving up')
    d = r.json(); rels = d.get('releases', [])
    json.dump(d, open(os.path.join(out_dir, f'page_{state["page"]:04d}.json'), 'w'))
    state['page'] += 1; state['n'] += len(rels)
    state['next'] = d.get('links', {}).get('next') if rels else None
    state['done'] = not state['next']
    json.dump(state, open(state_path, 'w'))
    logging.info('page %d releases %d done=%s', state['page'], state['n'], state['done'])
    time.sleep(4.0)
logging.info('DONE releases=%d', state['n'])
