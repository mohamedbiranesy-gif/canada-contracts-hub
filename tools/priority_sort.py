#!/usr/bin/env python3
"""The table in the owner's order of priority (2026-11-11 20:36 EST: "we will also include those of lower value but mark them, mark everything,
prioritise over 5000 … no buyer twice is hard rule so it should be 1 million buyers").

Every row carries its amount mark (tools/relationship_rows.py: amount_mark — 1 published $5,000 or more, 2 estimated $5,000 or more,
3 published under $5,000, 4 estimated under $5,000, 5 no amount) and its test (ship_ready). This tool rewrites the built table so that the
rows stand in that order: the rows that meet the test first, by amount mark 1 to 5, then the rows that do not, by the same marks. Inside a
class the ranker's own order is kept. The JSON-lines copy is rewritten in step with it. Constant memory: rows go to one working file per class
and the classes are put back together (the table is meant to hold a million rows).

  python3 tools/priority_sort.py out/ranked        (run by tools/rank_tail.sh before anything reads the table)
"""
import collections, csv, gzip, os, shutil, sys, time

csv.field_size_limit(1 << 30)


def cls(ship_ready, mark):
    m = (mark or "5")[:1]
    return (0 if (ship_ready or "").startswith("yes") else 1, int(m) if m in "12345" else 5)


def main(d):
    t0 = time.time()
    table, lines = os.path.join(d, "ranked_buyers.csv.gz"), os.path.join(d, "ranked_buyers.jsonl.gz")
    if not os.path.exists(table):
        raise SystemExit("no table in %s" % d)
    work = os.path.join(d, "_priority")
    shutil.rmtree(work, ignore_errors=True)
    os.makedirs(work)
    has_json = os.path.exists(lines)
    fj = gzip.open(lines, "rt", encoding="utf-8") if has_json else None
    n, bc, bj = collections.Counter(), {}, {}
    with gzip.open(table, "rt", encoding="utf-8", newline="") as f:
        rd = csv.reader(f)
        head = next(rd)
        if "ship_ready" not in head or "amount_mark" not in head:
            print("priority order: the table has no amount_mark column (built by an earlier ranker) — left as it is")
            shutil.rmtree(work, ignore_errors=True)
            return
        i_s, i_m = head.index("ship_ready"), head.index("amount_mark")
        for row in rd:
            k = cls(row[i_s], row[i_m])
            if k not in bc:
                fo = gzip.open(os.path.join(work, "c_%d_%d.csv.gz" % k), "wt", encoding="utf-8", newline="", compresslevel=1)
                bc[k] = (fo, csv.writer(fo))
                if has_json:
                    bj[k] = gzip.open(os.path.join(work, "j_%d_%d.jsonl.gz" % k), "wt", encoding="utf-8", compresslevel=1)
            bc[k][1].writerow(row)
            if has_json:
                l = fj.readline()
                if not l:
                    raise SystemExit("priority order: the JSON-lines copy has fewer rows than the table — nothing changed")
                bj[k].write(l)
            n[k] += 1
    if has_json:
        if fj.readline():
            raise SystemExit("priority order: the JSON-lines copy has more rows than the table — nothing changed")
        fj.close()
    for fo, _ in bc.values():
        fo.close()
    for fo in bj.values():
        fo.close()
    order = sorted(bc)
    tmp = table + ".sorted"
    with gzip.open(tmp, "wt", encoding="utf-8", newline="", compresslevel=6) as fo:
        csv.writer(fo).writerow(head)
        for k in order:
            with gzip.open(os.path.join(work, "c_%d_%d.csv.gz" % k), "rt", encoding="utf-8", newline="") as fi:
                shutil.copyfileobj(fi, fo, 1 << 20)
    if has_json:
        tmpj = lines + ".sorted"
        with gzip.open(tmpj, "wt", encoding="utf-8", compresslevel=6) as fo:
            for k in order:
                with gzip.open(os.path.join(work, "j_%d_%d.jsonl.gz" % k), "rt", encoding="utf-8") as fi:
                    shutil.copyfileobj(fi, fo, 1 << 20)
        os.replace(tmpj, lines)
    os.replace(tmp, table)
    shutil.rmtree(work, ignore_errors=True)
    name = {1: "published, $5,000 or more", 2: "estimated, $5,000 or more", 3: "published, under $5,000", 4: "estimated, under $5,000", 5: "no amount"}
    print("priority order (rows that meet the test first, then by amount): %s — %d rows in %d s" % (
        " · ".join("%s, %s: %d" % ("ready" if k[0] == 0 else "not ready", name[k[1]], n[k]) for k in order), sum(n.values()), time.time() - t0))


if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else "out/ranked")
