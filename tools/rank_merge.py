#!/usr/bin/env python3
"""Put the parts of a ranking together (2026-11-10).

contrib/claude/rank_buyers/rank.py ranks part i of N when RANK_PART="i/N" is set (a million rows do not fit one runner's memory). Each part
writes out/ranked/ranked_buyers.csv.gz and .jsonl.gz: part 0 every row that exists before the leads plus its own organisations' rows,
the other parts only their own organisations' rows. An organisation's part is decided so that everything the ranker joins — a website
domain, a mailbox — is in one part; this tool therefore only has to

  1. merge the parts in the table's order (older / inferred rows last, Gold first, then by score — the ranker's own sort key; rows that tie
     keep the order of their part, part 0 first);
  2. check what must not happen: one mailbox held by rows of two parts (reported; the later row is left out so that the table keeps one
     row per mailbox).

Not done here, and measured: the ranker skips an inferred row (tier I) when a row already carries the same organisation NAME; across parts
it cannot see the other parts' names. Two parts of 76,706 rows gave one inferred row more than a single run. A rule on the final names in
this tool would do worse (it removed two rows the single run keeps: their names only became equal after the ranker renamed them).

    python3 tools/rank_merge.py --out out/ranked part0/out/ranked part1/out/ranked …
Two passes over the parts' CSV files; memory: one short string a row.
"""
import argparse, csv, gzip, heapq, json, os, sys

csv.field_size_limit(1 << 30)


def table(d):
    """a part's table as text lines: ranked_buyers.csv, or ranked_buyers.csv.gz when only the compressed copy was passed on"""
    p = os.path.join(d, "ranked_buyers.csv")
    return open(p, encoding="utf-8", newline="") if os.path.exists(p) else gzip.open(p + ".gz", "rt", encoding="utf-8", newline="")


def main():
    a = argparse.ArgumentParser()
    a.add_argument("parts", nargs="+", help="the parts' out/ranked directories, part 0 first")
    a.add_argument("--out", required=True)
    a = a.parse_args()
    # pass 1: a mailbox must not sit in two parts
    box, drop, n_rows, two_parts = {}, set(), [], 0
    for p, d in enumerate(a.parts):
        n = 0
        with table(d) as fh:
            for i, r in enumerate(csv.DictReader(fh)):
                n += 1
                e = (r.get("email") or "").strip().lower()
                if e:
                    if e in box and box[e] != p:
                        two_parts += 1
                        drop.add((p, i))
                        if two_parts <= 5:
                            print("mailbox in two parts: %s (parts %d and %d; %s)" % (e, box[e], p, (r.get("buyer") or "")[:60]))
                    box.setdefault(e, p)
        n_rows.append(n)
    del box
    # pass 2: merge in the table's order
    os.makedirs(a.out, exist_ok=True)

    def stream(p, d):
        with table(d) as fc, gzip.open(os.path.join(d, "ranked_buyers.jsonl.gz"), "rt", encoding="utf-8") as fj:
            rd = csv.reader(fc)
            header = next(rd)
            it, ig, isc = header.index("tier"), header.index("rank_group"), header.index("completeness_score")
            yield header
            for i, row in enumerate(rd):
                jl = fj.readline()
                if (p, i) in drop:
                    continue
                try:
                    sc = float(row[isc] or 0)
                except ValueError:
                    sc = 0.0
                yield ((row[it] in ("F", "I"), row[it] == "I", row[ig] != "GOLD", -sc), p, i, row, jl)

    streams = [stream(p, d) for p, d in enumerate(a.parts)]
    headers = [next(s) for s in streams]
    if any(h != headers[0] for h in headers):
        sys.exit("the parts do not have the same columns: %s" % [len(h) for h in headers])
    n_out = 0
    for old in ("ranked_buyers.csv", "ranked_buyers.csv.gz", "ranked_buyers.jsonl.gz"):
        # only the compressed table is written (15 KB a row as plain text; batches.py reads a plain file first when one is there). Removed, not
        # overwritten: the publisher hard-links the table into coord/results/ranked/, and writing through the old name would empty that copy too
        if os.path.exists(os.path.join(a.out, old)):
            os.remove(os.path.join(a.out, old))
    with gzip.open(os.path.join(a.out, "ranked_buyers.csv.gz"), "wt", encoding="utf-8", newline="", compresslevel=6) as f2, \
            gzip.open(os.path.join(a.out, "ranked_buyers.jsonl.gz"), "wt", encoding="utf-8", compresslevel=6) as f3:
        w2 = csv.writer(f2)
        w2.writerow(headers[0])
        for key, p, i, row, jl in heapq.merge(*streams):
            w2.writerow(row)
            f3.write(jl if jl.endswith("\n") else jl + "\n")
            n_out += 1
    print("ranking put together: %d parts, rows per part %s -> %d rows; mailboxes held by rows of two parts (must be 0): %d" % (len(a.parts), n_rows, n_out, two_parts))
    json.dump({"parts": len(a.parts), "rows_per_part": n_rows, "rows": n_out, "mailbox_in_two_parts": two_parts}, open(os.path.join(a.out, "merge_report.json"), "w"))


if __name__ == "__main__":
    main()
