#!/usr/bin/env python3 -I
"""Parse WHO annual 'Awarded Contracts' PDFs (goods & services) into row dicts.
Usage: python3 -I parse_who.py <pdf_dir> <out_rows_json>
Each PDF page is a fixed-column table (header row + one line per contract; cells may wrap; long
supplier names may physically run into the next column). Per page:
  1. header lines = lines above the first 9-digit contract reference that contain header keywords;
  2. column label x-positions are read from the header words;
  3. each label is snapped to the nearest white gap (low character coverage) at/left of the label,
     giving column boundaries robust to centred or right-aligned headers;
  4. every character below the header is assigned to a column by x and to the row of the
     vertically nearest 9-digit reference number (row anchor).
"""
import sys, os, re, json, glob, collections, bisect
import pdfplumber

pdf_dir, out_fn = sys.argv[1], sys.argv[2]
REF_RE = re.compile(r'^\d{9}$')
KEYWORDS = {'contract', 'supplier', 'who', 'date', 'purchase', 'service', 'number', 'amount', 'usd', 'approval',
            'signature', 'country', 'name', 'office', 'category', 'type', 'reference', 'ref', 'order', 'supply'}

def tok(w):
    return w['text'].strip().rstrip(':').rstrip('.').lower()

def header_lines(words, first_top):
    cand = [w for w in words if w['top'] < first_top - 2]
    lines = []
    for w in sorted(cand, key=lambda w: w['top']):
        if lines and abs(lines[-1]['top'] - w['top']) < 3.5:
            lines[-1]['words'].append(w)
        else:
            lines.append({'top': w['top'], 'words': [w]})
    hdr_idx = [i for i, l in enumerate(lines) if any(tok(w) in KEYWORDS for w in l['words'])]
    if not hdr_idx:
        return [], first_top - 2
    last = max(hdr_idx)
    hwords = [w for l in lines[:last + 1] for w in l['words']]
    bottom = max(w['bottom'] for w in lines[last]['words'])
    return hwords, bottom

def label_positions(hw, anchors):
    hw = sorted(hw, key=lambda w: (w['top'], w['x0']))
    def right_neighbor(w):
        c = [v for v in hw if abs(v['top'] - w['top']) < 4 and v['x0'] > w['x1'] - 1 and v['x0'] - w['x1'] < 12]
        return min(c, key=lambda v: v['x0']) if c else None
    def below(w):
        c = [v for v in hw if 0 < v['top'] - w['top'] < 16 and abs(v['x0'] - w['x0']) < 8]
        return min(c, key=lambda v: v['top']) if c else None
    cols = {'contract_reference_number': 0.0}
    service_x = []
    for w in hw:
        t = tok(w); rn = right_neighbor(w); rnt = tok(rn) if rn else ''
        if t == 'supplier':
            b = below(w); bt = tok(b) if b else ''
            if rnt.startswith('name') or bt.startswith('name'):
                cols['supplier_name'] = w['x0']
            elif rnt.startswith('country') or bt.startswith('country'):
                cols['supplier_country'] = w['x0']
        elif t == 'who':
            cols['who_office'] = w['x0']
        elif t == 'purchase':
            cols['purchase_order_for_the_supply_of'] = w['x0']
        elif t == 'service':
            service_x.append(w['x0'])
        elif t == 'date':
            cols['date_of_contract'] = w['x0']
        elif t == 'amount':
            left = [v for v in hw if abs(v['top'] - w['top']) < 4 and v['x1'] <= w['x0'] + 1 and w['x0'] - v['x1'] < 12 and tok(v) == 'contract']
            cols['contract_amount_usd'] = min([w['x0']] + [v['x0'] for v in left])
    if service_x:
        xs = sorted(set(round(x) for x in service_x)); clusters = []
        for x in xs:
            if clusters and x - clusters[-1][-1] < 8: clusters[-1].append(x)
            else: clusters.append([x])
        if len(clusters) >= 2:
            cols['service_contract_type'] = clusters[0][0]; cols['service_category'] = clusters[1][0]
        else:
            cols['service_category'] = clusters[0][0]
    return cols

def snap_to_gaps(cols, chars, width, n_rows):
    W = int(width) + 2
    cov = [0] * W
    for c in chars:
        for x in range(max(0, int(c['x0'])), min(W - 1, int(c['x1']) + 1)):
            cov[x] += 1
    thr = max(1, int(0.03 * n_rows))
    gaps = []; start = None
    for x in range(W):
        if cov[x] <= thr and start is None: start = x
        elif cov[x] > thr and start is not None:
            if x - start >= 2: gaps.append((start, x))
            start = None
    if start is not None: gaps.append((start, W))
    out = []
    prev_hx = 0.0
    for name, hx in sorted(cols.items(), key=lambda kv: kv[1]):
        if name == 'contract_reference_number':
            out.append((name, hx, 0.0)); continue
        # candidate gaps: start at/left of the label, end right of the previous column's label (so a gap
        # erased by long supplier names never makes us jump back over the previous column) and not
        # absurdly far left (headers may be centred ~110pt right of left-aligned data)
        cand = [g for g in gaps if g[0] <= hx + 2.5 and g[1] >= prev_hx + 3 and g[1] >= hx - 200]
        prev_hx = hx
        if cand:
            g = max(cand, key=lambda g: g[0])
            b = (g[0] + g[1]) / 2 if g[1] - g[0] < 60 else g[1] - 3   # wide gap: hug the right (data) side
            # never place the boundary right of the label start + 2.5
            b = min(b, hx + 2.5)
        else:
            b = hx - 3
        out.append((name, hx, b))
    # enforce monotonic boundaries
    for i in range(1, len(out)):
        if out[i][2] <= out[i - 1][2]:
            out[i] = (out[i][0], out[i][1], out[i - 1][2] + 1)
    return out, gaps

def page_rows(page, fn, pno):
    words = page.extract_words(x_tolerance=1.5, y_tolerance=2)
    if not words:
        return [], None
    anchors = [w for w in words if REF_RE.match(w['text']) and w['x0'] < page.width * 0.25]
    if not anchors:
        return [], None
    anchors.sort(key=lambda a: a['top'])
    first_top = anchors[0]['top']
    hw, hdr_bottom = header_lines(words, first_top)
    header_text = ' '.join(w['text'] for w in sorted(hw, key=lambda w: (round(w['top']), w['x0'])))
    chars = [c for c in page.chars if c['top'] >= hdr_bottom - 1 and c['text'].strip()]
    cols = label_positions(hw, anchors)
    colb, gaps = snap_to_gaps(cols, chars, page.width, len(anchors))
    bounds = [b for _, _, b in colb]; names = [n for n, _, _ in colb]
    def col_of(x):
        return names[max(bisect.bisect_right(bounds, x) - 1, 0)]
    tops = [a['top'] for a in anchors]
    rows = [collections.defaultdict(list) for _ in anchors]
    for c in chars:
        i = bisect.bisect_left(tops, c['top'])
        if i >= len(tops):
            j = len(tops) - 1
        elif i == 0:
            j = 0
        else:
            d_up = c['top'] - tops[i - 1]      # distance to the anchor above (wrapped continuation lines)
            d_down = tops[i] - c['top']        # distance to the anchor below
            j = i - 1 if d_up <= d_down + 1.0 else i   # ties go to the row above (text wraps downward)
        if abs(tops[j] - c['top']) > 26:
            continue
        rows[j][col_of(c['x0'])].append(c)
    out = []
    for r, a in zip(rows, anchors):
        cells = {}
        for name, cs in r.items():
            cs.sort(key=lambda c: (round(c['top'] / 4), c['x0']))
            s = ''; prev = None
            for c in cs:
                if prev is None: s = c['text']
                elif abs(c['top'] - prev['top']) > 3: s += ' ' + c['text']
                elif c['x0'] - prev['x1'] > 1.2: s += ' ' + c['text']
                else: s += c['text']
                prev = c
            cells[name] = re.sub(r'\s+', ' ', s).strip()
        out.append({'file': fn, 'page': pno + 1, 'anchor_top': round(a['top'], 1), 'anchor_ref': a['text'], 'cells': cells})
    meta = {'columns': [(n, round(hx, 1), round(b, 1)) for n, hx, b in colb], 'header_text': header_text}
    return out, meta

all_rows = []; summary = {}
for fn in sorted(glob.glob(os.path.join(pdf_dir, '*.pdf'))):
    base = os.path.basename(fn)
    nrows = 0; ncanada = 0; colsets = collections.Counter()
    with pdfplumber.open(fn) as pdf:
        for pno, page in enumerate(pdf.pages):
            rows, meta = page_rows(page, base, pno)
            if not rows: continue
            for r in rows:
                r['header_text'] = meta['header_text']; r['columns'] = meta['columns']
                colsets[tuple(n for n, _, _ in meta['columns'])] += 1
                all_rows.append(r); nrows += 1
                if (r['cells'].get('supplier_country') or '').strip().lower() == 'canada': ncanada += 1
    summary[base] = {'rows': nrows, 'canada_rows': ncanada, 'column_sets': {' | '.join(k): v for k, v in colsets.items()}}
    print(base, json.dumps(summary[base]), flush=True)
    json.dump({'rows': all_rows, 'summary': summary}, open(out_fn, 'w'), indent=0, ensure_ascii=False)
print('total rows', len(all_rows))
