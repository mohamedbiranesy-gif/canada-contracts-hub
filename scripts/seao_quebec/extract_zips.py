"""Extract all SEAO zip archives (incl. nested zips) into <outdir>/<zipstem>/ . Usage: python3 -I extract_zips.py <zipdir> <outdir> <log>"""
import sys, os, zipfile, io, datetime
zipdir, outdir, logf = sys.argv[1:4]
log = open(logf, 'a', encoding='utf-8')
def L(m):
    log.write(datetime.datetime.now(datetime.timezone.utc).isoformat()+'\t'+m+'\n'); log.flush(); print(m, flush=True)
def safe_join(base, name):
    name = name.replace('\\', '/')
    p = os.path.normpath(os.path.join(base, name))
    if not p.startswith(os.path.abspath(base) + os.sep): raise ValueError('zip slip: '+name)
    return p
def extract(zf, base, depth=0):
    for info in zf.infolist():
        if info.is_dir(): continue
        if info.filename.lower().endswith('.zip'):
            data = zf.read(info)
            sub = os.path.join(base, os.path.splitext(os.path.basename(info.filename))[0])
            os.makedirs(sub, exist_ok=True)
            with zipfile.ZipFile(io.BytesIO(data)) as z2:
                extract(z2, sub, depth+1)
            L(f'  nested {info.filename} -> {sub}')
        else:
            dest = safe_join(base, os.path.basename(info.filename))
            if os.path.exists(dest) and os.path.getsize(dest) == info.file_size:
                continue
            with zf.open(info) as src, open(dest, 'wb') as dst:
                while True:
                    chunk = src.read(1<<20)
                    if not chunk: break
                    dst.write(chunk)
            L(f'  {info.filename} {info.file_size}')
for fn in sorted(os.listdir(zipdir)):
    if not fn.lower().endswith('.zip'): continue
    if fn.startswith('json_'): 
        L(f'skip {fn} (json archive handled separately)'); continue
    stem = os.path.splitext(fn)[0]
    base = os.path.abspath(os.path.join(outdir, stem))
    os.makedirs(base, exist_ok=True)
    L(f'ZIP {fn}')
    try:
        with zipfile.ZipFile(os.path.join(zipdir, fn)) as zf:
            extract(zf, base)
    except Exception as e:
        L(f'ERROR {fn}: {e!r}')
L('DONE')
