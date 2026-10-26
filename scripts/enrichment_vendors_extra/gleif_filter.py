#!/usr/bin/env python3
"""Stream the GLEIF golden-copy zips (lei2 / rr / repex) and keep what concerns Canada.

Usage: python3 -I gleif_filter.py <gleif_download_dir>
Writes into the same dir:
  lei2_ca.jsonl.gz      one JSON object per LEI record whose legal/HQ/other address country is CA or legal jurisdiction is CA[-xx]
                        (non-empty columns only, verbatim column names)
  rr_ca.jsonl.gz        relationship records where start or end node is one of those LEIs
  repex_ca.jsonl.gz     reporting exceptions of those LEIs
  lei2_related.jsonl.gz minimal records (name, addresses, status, jurisdiction) of the non-Canadian LEIs at the other end of a relationship
"""
import sys, os, io, csv, gzip, json, zipfile

csv.field_size_limit(10 ** 9)
D = sys.argv[1]


def open_zip_csv(fn):
    z = zipfile.ZipFile(os.path.join(D, fn))
    f = io.TextIOWrapper(z.open(z.infolist()[0]), encoding="utf-8", newline="")
    return csv.reader(f)


def is_ca(h, row, idx):
    for i in idx["countries"]:
        if row[i] == "CA":
            return True
    j = row[idx["jur"]]
    return j == "CA" or j.startswith("CA-")


r = open_zip_csv("lei2.csv.zip")
h = next(r)
idx = {"countries": [i for i, c in enumerate(h) if c.endswith(".Country") and "Transliterated" not in c],
       "jur": h.index("Entity.LegalJurisdiction")}
ca = set()
n = 0
with gzip.open(os.path.join(D, "lei2_ca.jsonl.gz"), "wt", encoding="utf-8") as out:
    for row in r:
        n += 1
        if is_ca(h, row, idx):
            ca.add(row[0])
            out.write(json.dumps({h[i]: v for i, v in enumerate(row) if v != ""}, ensure_ascii=False) + "\n")
        if n % 500000 == 0:
            print("lei2 pass1", n, len(ca), file=sys.stderr, flush=True)
print("lei2 rows", n, "canada", len(ca), file=sys.stderr, flush=True)

other = set()
r = open_zip_csv("rr.csv.zip")
h = next(r)
nr = 0
with gzip.open(os.path.join(D, "rr_ca.jsonl.gz"), "wt", encoding="utf-8") as out:
    for row in r:
        s, e = row[0], row[2]
        if s in ca or e in ca:
            nr += 1
            out.write(json.dumps({h[i]: v for i, v in enumerate(row) if v != ""}, ensure_ascii=False) + "\n")
            for x in (s, e):
                if x not in ca:
                    other.add(x)
print("rr kept", nr, "other LEIs", len(other), file=sys.stderr, flush=True)

r = open_zip_csv("repex.csv.zip")
h = next(r)
nx = 0
with gzip.open(os.path.join(D, "repex_ca.jsonl.gz"), "wt", encoding="utf-8") as out:
    for row in r:
        if row[0] in ca:
            nx += 1
            out.write(json.dumps({h[i]: v for i, v in enumerate(row) if v != ""}, ensure_ascii=False) + "\n")
print("repex kept", nx, file=sys.stderr, flush=True)

keep_cols = None
r = open_zip_csv("lei2.csv.zip")
h = next(r)
keep_cols = [i for i, c in enumerate(h) if c in ("LEI", "Entity.LegalName", "Entity.LegalJurisdiction", "Entity.EntityStatus", "Entity.EntityCategory",
                                                  "Registration.RegistrationStatus", "Entity.RegistrationAuthority.RegistrationAuthorityID",
                                                  "Entity.RegistrationAuthority.RegistrationAuthorityEntityID")
             or c.startswith("Entity.LegalAddress.") or c.startswith("Entity.HeadquartersAddress.")]
no = 0
with gzip.open(os.path.join(D, "lei2_related.jsonl.gz"), "wt", encoding="utf-8") as out:
    for row in r:
        if row[0] in other:
            no += 1
            out.write(json.dumps({h[i]: row[i] for i in keep_cols if row[i] != ""}, ensure_ascii=False) + "\n")
print("related non-CA LEIs written", no, file=sys.stderr, flush=True)
print("DONE", file=sys.stderr, flush=True)
