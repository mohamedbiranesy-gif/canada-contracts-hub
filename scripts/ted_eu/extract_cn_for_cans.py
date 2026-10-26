#!/usr/bin/env python3
"""From the TED open-data contract-notice (CN/CFC) CSV archives, pull the rows whose
FUTURE_CAN_ID is one of our Canadian-winner award notices (ID_NOTICE_CAN), to obtain
DURATION / CONTRACT_START / CONTRACT_COMPLETION for legacy awards.

Usage: python3 -I extract_cn_for_cans.py <canada_can_dir> <out_csv> <cn_zip1> [<cn_zip2> ...]
"""
import csv, glob, io, json, os, sys, time, zipfile

csv.field_size_limit(1 << 30)


def main():
    can_dir, out_csv = sys.argv[1], sys.argv[2]
    zips = sys.argv[3:]
    can_ids = set()
    for f in glob.glob(os.path.join(can_dir, '*.canada.csv')):
        with open(f, encoding='utf-8', newline='') as fh:
            for row in csv.DictReader(fh):
                can_ids.add(row['ID_NOTICE_CAN'].strip())
    print(len(can_ids), 'CAN ids', file=sys.stderr)
    header_out = None
    n_hits = 0
    with open(out_csv, 'w', newline='', encoding='utf-8') as out:
        w = None
        for zp in zips:
            t0 = time.time()
            n_rows = 0
            with zipfile.ZipFile(zp) as zf:
                name = zf.namelist()[0]
                with zf.open(name) as fh:
                    txt = io.TextIOWrapper(fh, encoding='utf-8', errors='replace', newline='')
                    reader = csv.reader(txt)
                    header = [h.strip().strip('"') for h in next(reader)]
                    fi = header.index('FUTURE_CAN_ID')
                    if w is None:
                        header_out = header
                        w = csv.writer(out)
                        w.writerow(header + ['_source_zip'])
                    for row in reader:
                        n_rows += 1
                        if len(row) > fi and row[fi].strip() in can_ids:
                            if header != header_out:
                                row = [dict(zip(header, row)).get(h, '') for h in header_out]
                            w.writerow(row + [os.path.basename(zp)])
                            n_hits += 1
            print(json.dumps({'zip': zp, 'rows': n_rows, 'hits_total': n_hits, 'seconds': round(time.time() - t0, 1)}), flush=True)


if __name__ == '__main__':
    main()
