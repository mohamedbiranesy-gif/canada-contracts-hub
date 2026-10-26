p='scripts/seao_quebec/download.py'
s=open(p).read()
a="""        if r.returncode == 0 and (want is None or got == want):
            L(f'OK {local} {got} bytes in {time.time()-t0:.1f}s <- {url}')
            break"""
b="""        # CKAN 'size' metadata is sometimes stale by a few bytes; trust curl's success
        # (it validates Content-Length itself) and, for JSON, a well-formed tail.
        ok_tail = True
        if local.endswith('.json') and got:
            with open(dest, 'rb') as fh:
                fh.seek(max(0, got - 64)); ok_tail = fh.read().rstrip().endswith(b'}')
        if r.returncode == 0 and got > 0 and ok_tail and (want is None or abs(got - want) <= 4096):
            L(f'OK {local} {got} bytes (ckan says {want}) in {time.time()-t0:.1f}s <- {url}')
            break"""
assert a in s; s=s.replace(a,b)
a2="""        if r.returncode == 0 and want is not None and got > want:
            os.remove(dest)  # corrupted/resume mismatch, start over"""
b2="""        if os.path.exists(dest) and ((r.returncode != 0 and '416' in r.stderr) or (want is not None and got > want + 4096)):
            os.remove(dest)  # resume mismatch, start over"""
assert a2 in s; s=s.replace(a2,b2)
a3="""    if os.path.exists(dest) and want and os.path.getsize(dest) == want:
        L(f'SKIP {local} already complete {want}')
        continue"""
b3="""    if os.path.exists(dest) and want and abs(os.path.getsize(dest) - want) <= 4096:
        L(f'SKIP {local} already complete {os.path.getsize(dest)} (ckan {want})')
        continue"""
assert a3 in s; s=s.replace(a3,b3)
open(p,'w').write(s); print('patched')
