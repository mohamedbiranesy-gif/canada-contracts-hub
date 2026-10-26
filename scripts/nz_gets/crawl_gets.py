#!/usr/bin/env python3
"""Crawl NZ GETS (www.gets.govt.nz) awarded tenders.

Phase 1 (list): POST the public Advanced Search with Status=Awarded and an awarded-date window
(month by month) and collect every result row (RFx ID, reference, title, type, open date, org, URL).
Phase 2 (detail): GET each ExternalTenderDetails page, save raw HTML, parse the field table,
Overview and "RFx Outcome" block (awarded supplier name + address lines, award date).

Everything is checkpointed under <out_dir>; re-running resumes.
Usage: python3 -I crawl_gets.py <out_dir> <from YYYY-MM> <to YYYY-MM> [list|detail|both]
"""
import json, os, re, sys, time, html, logging, datetime as dt
import requests

UA = ('Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36')
BASE = 'https://www.gets.govt.nz/'
PACE = float(os.environ.get('GETS_PACE', '1.0'))

def months(a, b):
    y, m = map(int, a.split('-')); y2, m2 = map(int, b.split('-'))
    while (y, m) <= (y2, m2):
        last = (dt.date(y + (m // 12), (m % 12) + 1, 1) - dt.timedelta(days=1)).day
        yield f'{y:04d}-{m:02d}', f'{y:04d}-{m:02d}-01', f'{y:04d}-{m:02d}-{last:02d}'
        y, m = (y + (m // 12), (m % 12) + 1)

def req(s, log, method, url, **kw):
    for attempt in range(10):
        try:
            r = s.request(method, url, timeout=120, **kw)
            if r.status_code == 200:
                return r
            log.warning('HTTP %s %s attempt %d', r.status_code, url[:100], attempt)
        except Exception as e:
            log.warning('error %s attempt %d', e, attempt)
        time.sleep(min(120, 5 * 2 ** attempt))
    raise RuntimeError('giving up ' + url)

def clean(x):
    return html.unescape(re.sub(r'\s+', ' ', re.sub(r'<[^>]+>', ' ', x))).strip()

def parse_rows(page):
    out = []
    for r in re.findall(r'<tr[^>]*>(.*?)</tr>', page, flags=re.S):
        m = re.search(r'href="([^"]*ExternalTenderDetails\.htm\?id=(\d+))"', r)
        if not m:
            continue
        cells = [clean(c) for c in re.findall(r'<td[^>]*>(.*?)</td>', r, flags=re.S)]
        out.append({'rfx_id': m.group(2), 'url': BASE + m.group(1).lstrip('/'), 'cells': cells})
    return out

def phase_list(s, log, out_dir, a, b):
    lst_path = os.path.join(out_dir, 'list.json')
    lst = json.load(open(lst_path)) if os.path.exists(lst_path) else {'months': {}, 'rows': {}}
    for key, d1, d2 in months(a, b):
        if key in lst['months']:
            continue
        data = {'srchTenderNameKeywords': '', 'srchRefNumSubStr': '', 'rfxID': '', 'srchClientOrgId': '0', 'srchPMNameKeywords': '',
                'srchOverviewKeywords': '', 'srchPublishedStartDate': '', 'srchPublishedEndDate': '', 'srchClosedStartDate': '',
                'srchClosedEndDate': '', 'srchAwardedStartDate': d1, 'srchAwardedEndDate': d2, 'srchStatus': 'Awarded',
                'submitBtn': 'Search', 'searchSubmitted': 'true', 'browserTimeZone': 'Pacific/Auckland'}
        t0 = time.time()
        r = req(s, log, 'POST', BASE + 'ExternalAdvancedSearching.htm', data=data)
        rows = parse_rows(r.text)
        with open(os.path.join(out_dir, 'list_pages', f'{key}.html'), 'w', encoding='utf-8') as f:
            f.write(r.text)
        for row in rows:
            row['award_window'] = key
            lst['rows'].setdefault(row['rfx_id'], row)
        lst['months'][key] = len(rows)
        json.dump(lst, open(lst_path, 'w'))
        log.info('list %s rows=%d total_distinct=%d (cap hit=%s)', key, len(rows), len(lst['rows']), len(rows) >= 2000)
        time.sleep(max(0, PACE - (time.time() - t0)))
    return lst

def parse_detail(page):
    d = {}
    # field table: <td class="label-cell">Label&nbsp;:</td><td>value</td>
    for m in re.finditer(r'<td class="label-cell">(.*?)</td>\s*<td[^>]*>(.*?)</td>', page, flags=re.S):
        label = clean(m.group(1)).replace('\xa0', ' ').rstrip(':').strip()
        val = clean(m.group(2)).replace('\xa0', ' ').strip()
        if label == 'Categories':
            cats = [clean(li) for li in re.findall(r'<li>(.*?)</li>', m.group(2), flags=re.S)]
            d['Categories_list'] = cats
        if label and val and label not in d:
            d[label] = val
    st = re.search(r'<div[^>]*class="notice[^"]*"[^>]*>(.*?)</div>', page, flags=re.S)
    if st: d['status_banner'] = clean(st.group(1))
    ov = re.search(r'<span class="legend">\s*Overview\s*</span>\s*</div>(.*?)(?:<div class="detail-divider">|<div class="rfx-outcome|</div>\s*</div>\s*</div>)', page, flags=re.S)
    if ov:
        d['Overview'] = clean(ov.group(1))
    oc = re.search(r'RFx Outcome\s*</span>\s*</div>(.*?)</p>', page, flags=re.S)
    outcome = {}
    if oc:
        block = oc.group(1)
        outcome['text'] = clean(block)
        outcome['awarded_to'] = [clean(li) for li in re.findall(r'<li>(.*?)</li>', block, flags=re.S)]
        ad = re.search(r'Award Date:\s*(.*?)\s*<br', block, flags=re.S)
        if ad: outcome['award_date'] = clean(ad.group(1))
        cd = re.search(r'Date RFx was completed/updated:\s*(.*?)\s*<br', block, flags=re.S)
        if cd: outcome['completed_updated'] = clean(cd.group(1))
    d['RFx Outcome'] = outcome
    title = re.search(r'<h1[^>]*>(.*?)</h1>', page, flags=re.S)
    if title: d['page_title'] = clean(title.group(1))
    return d

def phase_detail(s, log, out_dir, lst, shard=0, nshards=1, min_window='0000-00'):
    det_dir = os.path.join(out_dir, 'detail'); os.makedirs(det_dir, exist_ok=True)
    parsed_path = os.path.join(out_dir, f'details_{shard}.jsonl' if nshards > 1 else 'details.jsonl')
    done = set()
    import glob
    for p in glob.glob(os.path.join(out_dir, 'details*.jsonl')):
        for line in open(p, encoding='utf-8'):
            try: done.add(json.loads(line)['rfx_id'])
            except Exception: pass
    rows = sorted(lst['rows'].values(), key=lambda r: (r['award_window'], r['rfx_id']), reverse=True)
    todo = [r for i, r in enumerate(rows) if i % nshards == shard and r['rfx_id'] not in done and r['award_window'] >= min_window]
    log.info('detail phase: %d to fetch (%d done)', len(todo), len(done))
    with open(parsed_path, 'a', encoding='utf-8') as out:
        for i, row in enumerate(todo):
            t0 = time.time()
            try:
                r = req(s, log, 'GET', row['url'])
            except Exception as e:
                log.error('skip %s: %s', row['rfx_id'], e); continue
            with open(os.path.join(det_dir, f"{row['rfx_id']}.html"), 'w', encoding='utf-8') as f:
                f.write(r.text)
            rec = {'rfx_id': row['rfx_id'], 'url': row['url'], 'list_row': row, 'fetched_at': dt.datetime.now(dt.timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ'),
                   'detail': parse_detail(r.text)}
            out.write(json.dumps(rec, ensure_ascii=False) + '\n'); out.flush()
            if (i + 1) % 50 == 0:
                log.info('detail %d/%d', i + 1, len(todo))
            time.sleep(max(0, PACE - (time.time() - t0)))
    log.info('detail phase DONE')

def main():
    out_dir, a, b = sys.argv[1], sys.argv[2], sys.argv[3]
    mode = sys.argv[4] if len(sys.argv) > 4 else 'both'
    shard = int(sys.argv[5]) if len(sys.argv) > 5 else 0
    nshards = int(sys.argv[6]) if len(sys.argv) > 6 else 1
    min_window = sys.argv[7] if len(sys.argv) > 7 else '0000-00'
    os.makedirs(os.path.join(out_dir, 'list_pages'), exist_ok=True)
    logging.basicConfig(level=logging.INFO, format='%(asctime)s %(message)s',
                        handlers=[logging.FileHandler(os.path.join(out_dir, f'crawl_{mode}_{shard}.log')), logging.StreamHandler()])
    log = logging.getLogger()
    s = requests.Session(); s.headers['User-Agent'] = UA
    req(s, log, 'GET', BASE + 'ExternalAdvancedSearching.htm')  # cookie
    lst = phase_list(s, log, out_dir, a, b) if mode in ('list', 'both') else json.load(open(os.path.join(out_dir, 'list.json')))
    if mode in ('detail', 'both'):
        phase_detail(s, log, out_dir, lst, shard, nshards, min_window)

if __name__ == '__main__':
    main()
