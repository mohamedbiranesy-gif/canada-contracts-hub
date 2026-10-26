"""Load SEAO OCDS-like JSON files (weekly/monthly) into the SQLite staging DB (streaming with ijson).

Usage: python3 -I load_json.py <sqlite_db> <logfile> <json_file_or_dir> [...]

Table json_releases(ocid, numeroseao, release_id, release_date, file_order, src, tags, json)
  file_order = int(period_start YYYYMMDD) from the filename, so that later files win on conflicts.
Only the latest release per ocid is needed for status, but all releases are stored (small enough) so that
emit.py can keep the whole release history under raw.
"""
import sys, os, re, json, sqlite3, datetime, decimal, ijson

dbpath, logpath = sys.argv[1:3]
inputs = sys.argv[3:]
log = open(logpath, 'a', encoding='utf-8')


def L(msg):
    ts = datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')
    log.write(f'{ts}\t{msg}\n'); log.flush(); print(msg, flush=True)


files = []
for inp in inputs:
    if os.path.isdir(inp):
        for fn in sorted(os.listdir(inp)):
            if fn.lower().endswith('.json'):
                files.append(os.path.join(inp, fn))
    else:
        files.append(inp)


def file_order(path):
    m = re.search(r'(hebdo|mensuel)_(\d{8})_(\d{8})', os.path.basename(path))
    if not m:
        return 0
    # monthly files are published after the weekly files of the same month and are the consolidated view -> +1
    return int(m.group(2)) * 10 + (1 if m.group(1) == 'mensuel' else 0)


con = sqlite3.connect(dbpath)
con.execute('PRAGMA journal_mode=OFF'); con.execute('PRAGMA synchronous=OFF'); con.execute('PRAGMA cache_size=-200000')
con.execute('CREATE TABLE IF NOT EXISTS json_releases (ocid TEXT, numeroseao TEXT, release_id TEXT, release_date TEXT, file_order INTEGER, src TEXT, tags TEXT, json TEXT)')
con.execute('CREATE TABLE IF NOT EXISTS json_files (src TEXT PRIMARY KEY, file_order INTEGER, n_releases INTEGER, bytes INTEGER, published_date TEXT, uri TEXT)')
done = {r[0] for r in con.execute('SELECT src FROM json_files')}

for path in sorted(files, key=file_order):
    src = os.path.basename(path)
    if src in done:
        L(f'SKIP {src}'); continue
    fo = file_order(path)
    n = 0
    batch = []
    meta = {}
    try:
        with open(path, 'rb') as f:
            # header metadata (uri, publishedDate) -- small prefix parse
            head = f.read(4000).decode('utf-8', 'replace')
            m = re.search(r'"uri"\s*:\s*"([^"]+)"', head); meta['uri'] = m.group(1) if m else None
            m = re.search(r'"publishedDate"\s*:\s*"([^"]+)"', head); meta['publishedDate'] = m.group(1) if m else None
            f.seek(0)
            for rel in ijson.items(f, 'releases.item', use_float=True):
                ocid = rel.get('ocid') or ''
                ns = ocid.rsplit('-', 1)[-1] if ocid else ''
                rel['_source_file'] = src
                batch.append((ocid, ns, rel.get('id'), rel.get('date'), fo, src, ','.join(rel.get('tag') or []), json.dumps(rel, ensure_ascii=False)))
                n += 1
                if len(batch) >= 1000:
                    con.executemany('INSERT INTO json_releases VALUES (?,?,?,?,?,?,?,?)', batch); batch = []
        con.executemany('INSERT INTO json_releases VALUES (?,?,?,?,?,?,?,?)', batch)
        con.execute('INSERT OR REPLACE INTO json_files VALUES (?,?,?,?,?,?)', (src, fo, n, os.path.getsize(path), meta.get('publishedDate'), meta.get('uri')))
        con.commit()
        L(f'OK {src} {n} releases')
    except Exception as e:
        L(f'ERROR {src}: {e!r}')
        con.rollback()

L('indexing')
con.execute('CREATE INDEX IF NOT EXISTS ix_jr ON json_releases(numeroseao, file_order, release_date)')
con.commit()
L(f'json_releases: {con.execute("SELECT COUNT(*) FROM json_releases").fetchone()[0]} rows')
L('DONE')
