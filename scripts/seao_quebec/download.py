"""Download SEAO resources listed in resources.tsv. Usage:
python3 -I download.py <resources.tsv> <outdir> <logfile> <pattern-regex-on-filename> [--check]
Uses curl -C - -L for resume; skips files whose size already matches CKAN size.
"""
import sys, re, subprocess, os, time, datetime
tsv, outdir, logfile, pattern = sys.argv[1:5]
check = '--check' in sys.argv
os.makedirs(outdir, exist_ok=True)
rx = re.compile(pattern, re.I)
rows = []
for line in open(tsv, encoding='utf-8'):
    parts = line.rstrip('\n').split('\t')
    if len(parts) < 5: continue
    fmt, name, size, mod, url = parts
    fn = url.rsplit('/', 1)[-1]
    if rx.search(fn):
        rows.append((fmt, name, size, mod, url, fn))
log = open(logfile, 'a', encoding='utf-8')
def L(msg):
    ts = datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')
    log.write(f'{ts}\t{msg}\n'); log.flush(); print(msg, flush=True)
L(f'START {len(rows)} files matching {pattern}')
seen = {}
for fmt, name, size, mod, url, fn in rows:
    # resource ids are unique; filenames may collide (duplicate monthly resources) -> prefix resource id when collision
    rid = url.split('/resource/')[1].split('/')[0]
    local = fn
    if fn in seen and seen[fn] != rid:
        local = rid[:8] + '_' + fn
    seen.setdefault(fn, rid)
    dest = os.path.join(outdir, local)
    want = int(size) if size not in ('None', '', None) else None
    if os.path.exists(dest) and want and abs(os.path.getsize(dest) - want) <= 4096:
        L(f'SKIP {local} already complete {os.path.getsize(dest)} (ckan {want})')
        continue
    if check:
        L(f'WOULD {local} <- {url} ({size})'); continue
    for attempt in range(1, 6):
        t0 = time.time()
        cmd = ['curl', '-sS', '-L', '-C', '-', '--retry', '3', '--retry-delay', '5', '-A', 'contracts-research/1.0', '-o', dest, url]
        r = subprocess.run(cmd, capture_output=True, text=True)
        got = os.path.getsize(dest) if os.path.exists(dest) else 0
        # CKAN 'size' metadata is sometimes stale by a few bytes; trust curl's success
        # (it validates Content-Length itself) and, for JSON, a well-formed tail.
        ok_tail = True
        if local.endswith('.json') and got:
            with open(dest, 'rb') as fh:
                fh.seek(max(0, got - 64)); ok_tail = fh.read().rstrip().endswith(b'}')
        if r.returncode == 0 and got > 0 and ok_tail and (want is None or abs(got - want) <= 4096):
            L(f'OK {local} {got} bytes (ckan says {want}) in {time.time()-t0:.1f}s <- {url}')
            break
        L(f'RETRY{attempt} {local} rc={r.returncode} got={got} want={want} err={r.stderr.strip()[:200]}')
        if os.path.exists(dest) and ((r.returncode != 0 and '416' in r.stderr) or (want is not None and got > want + 4096)):
            os.remove(dest)  # resume mismatch, start over
        time.sleep(5 * attempt)
    else:
        L(f'FAIL {local} <- {url}')
L('DONE')
