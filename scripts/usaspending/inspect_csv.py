#!/usr/bin/env python3
"""Quick inspection of a downloaded USAspending CSV: columns, row count, value counts for key columns."""
import sys
from collections import Counter

import pandas as pd

path = sys.argv[1]
cols_of_interest = sys.argv[2:]

n = 0
counters = {c: Counter() for c in cols_of_interest}
header = None
for chunk in pd.read_csv(path, dtype=str, keep_default_na=False, chunksize=100000, encoding="utf-8"):
    if header is None:
        header = list(chunk.columns)
    n += len(chunk)
    for c in cols_of_interest:
        if c in chunk.columns:
            counters[c].update(chunk[c].tolist())

print(f"file: {path}")
print(f"rows: {n}")
print(f"columns ({len(header)}):")
for i, c in enumerate(header):
    print(f"  {i:3d} {c}")
for c in cols_of_interest:
    print(f"--- {c}: {len(counters[c])} distinct")
    for v, k in counters[c].most_common(25):
        print(f"    {k:8d}  {v!r}")
