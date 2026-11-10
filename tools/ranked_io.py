#!/usr/bin/env python3
"""The ranked table in parts (2026-11-10): coord/results/ranked/ranked_buyers.csv.gz was 70 MB at 68,910 rows; GitHub refuses any file over
100 MB, so the push of a build with ~98,000 rows would have failed — and the target is a million rows.

Committed: ranked_buyers.csv.gz.part01, .part02 … — each one a complete gzip member under 45 MB that holds a slice of the rows (the header is
in part 01 only). Concatenated in order they are one valid gzip file with one valid CSV inside, so
    python3 tools/ranked_io.py assemble        # parts -> coord/results/ranked/ranked_buyers.csv.gz (untracked, see .gitignore)
gives every existing reader the file it has always opened. Workflows run it right after checkout.

  split FILE [MB]   FILE -> FILE.part01 … (FILE itself is removed)
  assemble [DIR]    parts in DIR (default coord/results/ranked) -> the single file, when it is missing or older than the parts
  cat [DIR]         the CSV text on stdout (single file or parts)
Python: rows(path) yields dict rows from the single file or from its parts; lines(path) yields the text lines.
"""
import csv, glob, gzip, io, os, shutil, sys

csv.field_size_limit(1 << 30)
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
DEFAULT = os.path.join(ROOT, "coord/results/ranked/ranked_buyers.csv.gz")


def parts_of(path):
    return sorted(glob.glob(path + ".part[0-9][0-9]")) + sorted(glob.glob(path + ".part[0-9][0-9][0-9]"))


def lines(path=DEFAULT):
    """text lines of the table: its parts when there are any (they are what git holds), else the single file"""
    ps = parts_of(path)
    for p in (ps or ([path] if os.path.exists(path) else [])):
        with gzip.open(p, "rt", encoding="utf-8", newline="") as f:
            for l in f:
                yield l


def rows(path=DEFAULT):
    return csv.DictReader(lines(path))


def split(path, mb=40):
    limit = int(mb * 1024 * 1024)
    for p in parts_of(path):
        os.remove(p)
    n, k, out, raw = 0, 0, None, None

    def start():
        nonlocal k, out, raw
        k += 1
        raw = open("%s.part%02d" % (path, k), "wb")
        out = gzip.GzipFile(fileobj=raw, mode="wb", compresslevel=6, mtime=0)
    start()
    with gzip.open(path, "rb") as f:
        buf, in_quote = [], False
        for l in f:  # a CSV record may span several lines (quoted newlines): cut only between records
            buf.append(l)
            if l.count(b'"') % 2:
                in_quote = not in_quote
            if in_quote:
                continue
            out.write(b"".join(buf))
            buf, n = [], n + 1
            if n % 500 == 0:
                out.flush()
                if raw.tell() > limit:
                    out.close(); raw.close()
                    start()
        if buf:
            out.write(b"".join(buf))
    out.close(); raw.close()
    os.remove(path)
    print("%s: %d records in %d parts (%s MB)" % (os.path.basename(path), n - 1, k, ", ".join("%.0f" % (os.path.getsize(p) / 2 ** 20) for p in parts_of(path))))


def assemble(path=DEFAULT):
    ps = parts_of(path)
    if not ps:
        return os.path.exists(path)
    if os.path.exists(path) and os.path.getmtime(path) >= max(os.path.getmtime(p) for p in ps) and os.path.getsize(path) == sum(os.path.getsize(p) for p in ps):
        return True
    with open(path + ".tmp", "wb") as o:
        for p in ps:
            with open(p, "rb") as f:
                shutil.copyfileobj(f, o, 1 << 22)
    os.replace(path + ".tmp", path)
    return True


if __name__ == "__main__":
    cmd = sys.argv[1] if len(sys.argv) > 1 else "assemble"
    if cmd == "split":
        split(sys.argv[2], float(sys.argv[3]) if len(sys.argv) > 3 else 40)
    elif cmd == "cat":
        d = sys.argv[2] if len(sys.argv) > 2 else os.path.dirname(DEFAULT)
        for l in lines(os.path.join(d, "ranked_buyers.csv.gz")):
            sys.stdout.write(l)
    else:
        d = sys.argv[2] if len(sys.argv) > 2 else os.path.dirname(DEFAULT)
        ok = assemble(os.path.join(d, "ranked_buyers.csv.gz"))
        print("ranked table: %s" % ("ready" if ok else "not found"))
