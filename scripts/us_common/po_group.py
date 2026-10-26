"""Group Canadian-vendor PO/payment rows into one record per key; keep as end_date_unknown iff the latest date is within
the 12 months before the reference date (convention shared with us_state_virginia / us_city_la / us_state_massachusetts)."""
import sys, json, collections
sys.path.insert(0, "scripts/us_common")
from common import *

WIN = "2025-10-25"


def load_jsonl(p):
    return [json.loads(l) for l in open(p, encoding="utf-8") if l.strip()]


def run(rows, keyf, datef, build, out, kind="purchase order"):
    """build(key, rows, first, last) -> (contract, buyer, vendor, record_url, rid) or None (excluded)."""
    g = collections.OrderedDict()
    for r in rows:
        g.setdefault(keyf(r), []).append(r)
    w = Writer(out); st = collections.Counter()
    for k, rs in g.items():
        st["groups"] += 1
        ds = sorted(filter(None, (parse_date(datef(r)) for r in rs)))
        first, last = (ds[0], ds[-1]) if ds else (None, None)
        if not last or last < WIN or last > REF_S:
            st["excl_outside_12m"] += 1; continue
        res = build(k, rs, first, last)
        if res is None:
            st["excl_build"] += 1; continue
        rec, = (res,)
        w.write(rec); st[rec["status"]] += 1
    print(w.close(), dict(st))
    return st
