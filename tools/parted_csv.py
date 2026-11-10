#!/usr/bin/env python3
"""A CSV written in parts (2026-11-10): GitHub refuses a file over 100 MB and warns from 50 MB.

    X.csv            the header and the first rows
    X.part02.csv     more rows, no header        (X.part03.csv, …)

    import parted_csv as PC
    PC.write("coord/results/verification_log_claude.csv", header, rows)     # rows: lists in the order of the header; stale parts are removed
    for r in PC.rows("coord/results/verification_log_claude.csv"): …        # dicts, all parts in order (nothing when the file is absent)

The parts hold plain text in a stable order, so git stores a new version as a difference; a compressed file would be stored whole every time
(tools/state_io.py is for those).
"""
import csv, glob, os

csv.field_size_limit(1 << 30)
PART_BYTES = 40 * 1024 * 1024


def _parts(path):
    stem = path[:-4] if path.endswith(".csv") else path
    return sorted(glob.glob(glob.escape(stem) + ".part[0-9][0-9]*.csv"))


def files(path):
    """the first file and its parts, in reading order (only those that exist)"""
    return ([path] if os.path.exists(path) else []) + _parts(path)


def write(path, header, rows, part_bytes=PART_BYTES):
    """returns (rows written, files written)"""
    stem = path[:-4] if path.endswith(".csv") else path
    os.makedirs(os.path.dirname(os.path.abspath(path)), exist_ok=True)
    for old in _parts(path):
        os.remove(old)
    n, part = 0, 1
    f = open(path, "w", newline="", encoding="utf-8")
    w = csv.writer(f)
    w.writerow(header)
    try:
        for r in rows:
            if f.tell() >= part_bytes:
                f.close()
                part += 1
                f = open("%s.part%02d.csv" % (stem, part), "w", newline="", encoding="utf-8")
                w = csv.writer(f)
            w.writerow(r)
            n += 1
    finally:
        f.close()
    return n, part


def rows(path):
    """every row of the file and its parts as a dict (keys: the first file's header)"""
    fs = files(path)
    if not fs or fs[0] != path:
        return
    header = None
    for i, p in enumerate(fs):
        with open(p, encoding="utf-8", errors="replace", newline="") as fh:
            rd = csv.reader(line.replace("\0", "") for line in fh)
            if i == 0:
                header = next(rd, None)
                if not header:
                    return
            for r in rd:
                if r:
                    yield dict(zip(header, r + [""] * (len(header) - len(r))))
