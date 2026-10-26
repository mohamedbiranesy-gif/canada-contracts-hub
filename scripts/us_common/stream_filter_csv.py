#!/usr/bin/env python3
"""Stream a large remote CSV and keep only rows whose <column> value is in a set.
usage: python3 -I stream_filter_csv.py <url> <out.csv> <column> <comma-separated-values>
Writes header + matching rows; writes <out>.log with total row count. Does not store the full file (disk constraint).
"""
import sys, csv, io, time, urllib.request

UA = "contracts-research/1.0"

def main():
    url, out, col, vals = sys.argv[1], sys.argv[2], sys.argv[3], set(sys.argv[4].split(","))
    log = open(out + ".log", "a")
    log.write(f"{time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())} START {url} col={col} vals={sorted(vals)}\n"); log.flush()
    total = kept = 0
    if url == "-":
        r = sys.stdin.buffer
    else:
        req = urllib.request.Request(url, headers={"User-Agent": UA})
        r = urllib.request.urlopen(req, timeout=600)
    with open(out, "w", newline="", encoding="utf-8") as fo:
        text = io.TextIOWrapper(r, encoding="utf-8", errors="replace", newline="")
        reader = csv.reader(text)
        header = next(reader)
        w = csv.writer(fo)
        w.writerow(header)
        try:
            idx = header.index(col)
        except ValueError:
            log.write(f"column {col} not in header {header}\n"); log.close(); sys.exit(2)
        for row in reader:
            total += 1
            if len(row) > idx and row[idx].strip().upper() in vals:
                w.writerow(row); kept += 1
            if total % 500000 == 0:
                log.write(f"{time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())} rows={total} kept={kept}\n"); log.flush()
    log.write(f"{time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())} DONE rows={total} kept={kept}\n"); log.close()

if __name__ == "__main__":
    main()
