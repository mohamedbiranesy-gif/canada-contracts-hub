"""Load all SEAO XML open-data files into a SQLite staging DB (streaming, low memory).

Usage: python3 -I load_xml.py <xml_extracted_root> <sqlite_db> <logfile>

Tables (all appearances are kept; merge decisions are made later in emit.py):
  avis_rows(numeroseao, ord, src, kind, json)        -- Avis_* and AvisRevisions_* records (full record incl. all fournisseurs)
  contrat_rows(numeroseao, ord, src, kind, neq, nom, json) -- Contrats_* / ContratsRevisions_* (information finale)
  depense_rows(numeroseao, ord, src, kind, json)     -- Depenses_* / DepensesRevisions_* (one row per <avis> block, json = list of depense dicts)
ord = int(period_start YYYYMMDD) * 10 + (1 if revision file else 0)  -> chronological processing order.
"""
import sys, os, re, json, sqlite3, datetime
from lxml import etree

root, dbpath, logpath = sys.argv[1:4]
log = open(logpath, 'a', encoding='utf-8')


def L(msg):
    ts = datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')
    log.write(f'{ts}\t{msg}\n'); log.flush(); print(msg, flush=True)


def el_to_obj(el):
    """Convert an element to a dict; children with sub-elements become lists of dicts; leaves become text ('' if empty)."""
    out = {}
    for child in el:
        if not isinstance(child.tag, str):
            continue
        if len(child):
            # container element (e.g. fournisseurs, depenses): list of child dicts
            items = []
            for sub in child:
                if not isinstance(sub.tag, str):
                    continue
                items.append(el_to_obj(sub) if len(sub) else (sub.text or ''))
            out[child.tag] = items
        else:
            txt = child.text
            out[child.tag] = txt.strip() if txt is not None else ''
    return out


files = []
for dp, dn, fns in os.walk(root):
    for fn in fns:
        m = re.match(r'^(Avis|AvisRevisions|Contrats|ContratsRevisions|Depenses|DepensesRevisions)_(\d{8})_(\d{8})\.xml$', fn, re.I)
        if m:
            kind, start, end = m.group(1), m.group(2), m.group(3)
            kind_norm = {'avis': 'Avis', 'avisrevisions': 'AvisRevisions', 'contrats': 'Contrats', 'contratsrevisions': 'ContratsRevisions',
                         'depenses': 'Depenses', 'depensesrevisions': 'DepensesRevisions'}[kind.lower()]
            ordv = int(start) * 10 + (1 if 'Revisions' in kind_norm else 0)
            files.append((ordv, kind_norm, start, end, os.path.join(dp, fn)))
files.sort()
L(f'START {len(files)} xml files')

con = sqlite3.connect(dbpath)
con.execute('PRAGMA journal_mode=OFF'); con.execute('PRAGMA synchronous=OFF'); con.execute('PRAGMA cache_size=-200000')
con.execute('CREATE TABLE IF NOT EXISTS avis_rows (numeroseao TEXT, ord INTEGER, src TEXT, kind TEXT, json TEXT)')
con.execute('CREATE TABLE IF NOT EXISTS contrat_rows (numeroseao TEXT, ord INTEGER, src TEXT, kind TEXT, neq TEXT, nom TEXT, json TEXT)')
con.execute('CREATE TABLE IF NOT EXISTS depense_rows (numeroseao TEXT, ord INTEGER, src TEXT, kind TEXT, json TEXT)')
con.execute('CREATE TABLE IF NOT EXISTS xml_files (src TEXT PRIMARY KEY, kind TEXT, period_start TEXT, period_end TEXT, ord INTEGER, n_records INTEGER, bytes INTEGER)')
done = {r[0] for r in con.execute('SELECT src FROM xml_files')}

for ordv, kind, start, end, path in files:
    rel = os.path.relpath(path, root)
    if rel in done:
        L(f'SKIP {rel}'); continue
    n = 0
    top = 'contrat' if kind.startswith('Contrats') else 'avis'
    batch = []
    try:
        for ev, el in etree.iterparse(path, events=('end',), tag=top, recover=True, huge_tree=True):
            obj = el_to_obj(el)
            obj['_source_file'] = rel
            obj['_export_period'] = {'datedebut': start, 'datefin': end}
            ns = obj.get('numeroseao', '')
            js = json.dumps(obj, ensure_ascii=False)
            if kind.startswith('Avis'):
                batch.append(('avis', (ns, ordv, rel, kind, js)))
            elif kind.startswith('Contrats'):
                batch.append(('contrat', (ns, ordv, rel, kind, obj.get('neqcontractant', ''), obj.get('nomcontractant', ''), js)))
            else:
                batch.append(('depense', (ns, ordv, rel, kind, js)))
            n += 1
            el.clear()
            while el.getprevious() is not None:
                del el.getparent()[0]
            if len(batch) >= 2000:
                con.executemany('INSERT INTO avis_rows VALUES (?,?,?,?,?)', [b for k, b in batch if k == 'avis'])
                con.executemany('INSERT INTO contrat_rows VALUES (?,?,?,?,?,?,?)', [b for k, b in batch if k == 'contrat'])
                con.executemany('INSERT INTO depense_rows VALUES (?,?,?,?,?)', [b for k, b in batch if k == 'depense'])
                batch = []
        con.executemany('INSERT INTO avis_rows VALUES (?,?,?,?,?)', [b for k, b in batch if k == 'avis'])
        con.executemany('INSERT INTO contrat_rows VALUES (?,?,?,?,?,?,?)', [b for k, b in batch if k == 'contrat'])
        con.executemany('INSERT INTO depense_rows VALUES (?,?,?,?,?)', [b for k, b in batch if k == 'depense'])
        con.execute('INSERT OR REPLACE INTO xml_files VALUES (?,?,?,?,?,?,?)', (rel, kind, start, end, ordv, n, os.path.getsize(path)))
        con.commit()
        L(f'OK {rel} {n} records')
    except Exception as e:
        L(f'ERROR {rel}: {e!r}')
        con.rollback()

L('indexing')
con.execute('CREATE INDEX IF NOT EXISTS ix_avis ON avis_rows(numeroseao, ord)')
con.execute('CREATE INDEX IF NOT EXISTS ix_contrat ON contrat_rows(numeroseao)')
con.execute('CREATE INDEX IF NOT EXISTS ix_dep ON depense_rows(numeroseao, ord)')
con.commit()
for t in ('avis_rows', 'contrat_rows', 'depense_rows'):
    L(f'{t}: {con.execute(f"SELECT COUNT(*) FROM {t}").fetchone()[0]} rows')
L('DONE')
