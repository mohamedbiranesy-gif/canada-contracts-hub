#!/usr/bin/env python3
"""The package files of a rank build (out/ranked/batches/): <package>.csv.gz, or <package>_partK_of_N.csv.gz for a big package.

Written compressed since 2026-11-10: a row is 15 KB of plain text, so the packages of a million rows would be 15 GB on a runner with ~14 GB
free. The release's ranked_batches.zip still holds plain .csv members under the same names (tools/ranked_publish.py streams each file into it).
Builds made before that day and local runs may hold plain .csv files: both are read.

    import batch_files as BF
    for p in BF.files("out/ranked/batches"):      # in the order of their plain names, as sorted(glob("*.csv")) gave before
        BF.member(p)                               # "P08_client_listing_general_email_part2_of_3.csv"
        BF.package(p)                              # "P08_client_listing_general_email"
        with BF.open_text(p) as fh: ...            # text, as open(p, encoding="utf-8") gave before
"""
import glob, gzip, os, re


def member(p):
    """the file's name as a plain CSV (the name of its member in ranked_batches.zip)"""
    b = os.path.basename(p)
    return b[:-3] if b.endswith(".gz") else b


def package(p):
    return re.sub(r"_part\d+_of_\d+$", "", member(p)[:-4])


def files(d):
    seen, out = set(), []
    for p in sorted(glob.glob(os.path.join(d, "*.csv.gz")) + glob.glob(os.path.join(d, "*.csv")), key=lambda p: (member(p), not p.endswith(".gz"))):
        if member(p) not in seen:  # a compressed and a plain copy of one file: the compressed one is the build's
            seen.add(member(p))
            out.append(p)
    return out


def open_text(p, newline=None):
    if p.endswith(".gz"):
        return gzip.open(p, "rt", encoding="utf-8", newline=newline)
    return open(p, encoding="utf-8", newline=newline)


def open_bytes(p):
    return gzip.open(p, "rb") if p.endswith(".gz") else open(p, "rb")


def plain_bytes(p):
    """size of the file as plain text (a compressed file is read through once)"""
    if not p.endswith(".gz"):
        return os.path.getsize(p)
    n = 0
    with gzip.open(p, "rb") as f:
        for b in iter(lambda: f.read(1 << 22), b""):
            n += len(b)
    return n
