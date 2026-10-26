#!/usr/bin/env python3
"""Stream the TED open-data CAN CSV archives (data.europa.eu 'ted-csv' dataset) and
extract every award row whose WIN_COUNTRY_CODE contains CA (Canada).

Usage: python3 -I extract_csv_canada.py <out_dir> <zip1> [<zip2> ...]
Writes <out_dir>/<zipbasename>.canada.csv (header + matching rows) and a summary JSON.
"""
import csv, io, json, os, subprocess, sys, time, zipfile

csv.field_size_limit(1 << 30)


def main():
    out_dir = sys.argv[1]
    zips = sys.argv[2:]
    os.makedirs(out_dir, exist_ok=True)
    summary = {}
    for zp in zips:
        t0 = time.time()
        base = os.path.basename(zp).replace('.zip', '')
        out_path = os.path.join(out_dir, base + '.canada.csv')
        n_rows = 0
        n_hits = 0
        with zipfile.ZipFile(zp) as zf:
            names = zf.namelist()
            name = names[0]
            with zf.open(name) as fh:
                txt = io.TextIOWrapper(fh, encoding='utf-8', errors='replace', newline='')
                reader = csv.reader(txt)
                header = next(reader)
                header = [h.strip().strip('"') for h in header]
                try:
                    wi = header.index('WIN_COUNTRY_CODE')
                except ValueError:
                    print('no WIN_COUNTRY_CODE in', zp, header[:5], file=sys.stderr)
                    continue
                with open(out_path, 'w', newline='', encoding='utf-8') as out:
                    w = csv.writer(out)
                    w.writerow(header)
                    for row in reader:
                        n_rows += 1
                        if len(row) <= wi:
                            continue
                        v = row[wi]
                        if not v:
                            continue
                        parts = [p.strip().upper() for p in v.split('---')]
                        if 'CA' in parts:
                            w.writerow(row)
                            n_hits += 1
                        if n_rows % 1000000 == 0:
                            print(f'{base}: {n_rows} rows, {n_hits} hits, {time.time()-t0:.0f}s', file=sys.stderr, flush=True)
        summary[base] = {'csv_member': name, 'rows': n_rows, 'canada_rows': n_hits, 'seconds': round(time.time() - t0, 1), 'out': out_path}
        print(json.dumps(summary[base]), flush=True)
    with open(os.path.join(out_dir, 'extract_summary.json'), 'w') as f:
        json.dump(summary, f, indent=1)


if __name__ == '__main__':
    main()
