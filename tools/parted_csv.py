#!/usr/bin/env python3
"""A CSV written in parts (2026-11-10): GitHub refuses a file over 100 MB and warns from 50 MB.

    X.csv            the header and the first rows
    X.part02.csv     more rows, no header        (X.part03.csv, …)

    import parted_csv as PC
    PC.write("coord/results/verification_log_claude.csv", header, rows)     # rows: lists in the order of the header; stale parts are removed
    for r in PC.rows("coord/results/verification_log_claude.csv"): …        # dicts, all parts in order (nothing when the file is absent)

The parts hold plain text in a stable order, so git stores a new version as a difference; a compressed file would be stored whole every time
(tools/state_io.py is for those). A tab-separated file works the same way: X.tsv, X.part02.tsv … with delimiter="\t".
"""
import csv, glob, os

csv.field_size_limit(1 << 30)
PART_BYTES = 40 * 1024 * 1024


def _stem_ext(path):
    return (path[:-4], path[-4:]) if path.endswith((".csv", ".tsv")) else (path, ".csv")


def _parts(path):
    stem, ext = _stem_ext(path)
    return sorted(glob.glob(glob.escape(stem) + ".part[0-9][0-9]*" + ext))


def files(path):
    """the first file and its parts, in reading order (only those that exist)"""
    return ([path] if os.path.exists(path) else []) + _parts(path)


def write(path, header, rows, part_bytes=PART_BYTES, delimiter=","):
    """returns (rows written, files written). The first file is written under a temporary name and put in place at the end, so a reader (or a
    run that is killed) never sees a first file without its rows; parts no longer needed are removed last."""
    stem, ext = _stem_ext(path)
    os.makedirs(os.path.dirname(os.path.abspath(path)), exist_ok=True)
    before = set(_parts(path))
    n, part, made = 0, 1, []
    f = open(path + ".tmp", "w", newline="", encoding="utf-8")
    w = csv.writer(f, delimiter=delimiter)
    w.writerow(header)
    try:
        for r in rows:
            if f.tell() >= part_bytes:
                f.close()
                part += 1
                made.append("%s.part%02d%s" % (stem, part, ext))
                f = open(made[-1], "w", newline="", encoding="utf-8")
                w = csv.writer(f, delimiter=delimiter)
            w.writerow(r)
            n += 1
    finally:
        f.close()
    os.replace(path + ".tmp", path)
    for old in before - set(made):
        os.remove(old)
    return n, part


def rows(path, delimiter=","):
    """every row of the file and its parts as a dict (keys: the first file's header)"""
    fs = files(path)
    if not fs or fs[0] != path:
        return
    header = None
    for i, p in enumerate(fs):
        with open(p, encoding="utf-8", errors="replace", newline="") as fh:
            rd = csv.reader((line.replace("\0", "") for line in fh), delimiter=delimiter)
            if i == 0:
                header = next(rd, None)
                if not header:
                    return
            for r in rd:
                if r:
                    yield dict(zip(header, r + [""] * (len(header) - len(r))))
