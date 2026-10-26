#!/usr/bin/env python3
"""Stream PLACSP atom zip archives; keep every <entry> whose TenderResult/WinningParty address
country code is CA (Canada). Writes one JSON line per kept entry {zip, member, id, updated, xml}.
usage: extract.py <zip> ... --out matches.jsonl --log log.txt"""
import sys, zipfile, re, json, argparse, time, os

ENTRY = re.compile(r"<entry>.*?</entry>", re.S)
WIN = re.compile(r"<cac:WinningParty>.*?</cac:WinningParty>", re.S)
CA = re.compile(r"<cac:Country>\s*<cbc:IdentificationCode[^>]*>CA</cbc:IdentificationCode>", re.S)

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("zips", nargs="+"); ap.add_argument("--out", required=True); ap.add_argument("--log", required=True)
    a = ap.parse_args()
    for zp in a.zips:
        t0 = time.time(); n_ent = n_keep = n_mem = 0
        try:
            z = zipfile.ZipFile(zp)
        except Exception as e:
            open(a.log, "a").write(f"{time.strftime('%FT%TZ', time.gmtime())} BADZIP {zp} {e}\n"); continue
        with open(a.out, "a", encoding="utf-8") as fo:
            for m in z.namelist():
                if not m.endswith(".atom"):
                    continue
                n_mem += 1
                try:
                    s = z.read(m).decode("utf-8", "replace")
                except Exception as e:
                    open(a.log, "a").write(f"{time.strftime('%FT%TZ', time.gmtime())} BADMEMBER {zp} {m} {e}\n"); continue
                for e in ENTRY.findall(s):
                    n_ent += 1
                    if "WinningParty" not in e:
                        continue
                    if not any(CA.search(w) for w in WIN.findall(e)):
                        continue
                    n_keep += 1
                    idm = re.search(r"<id>([^<]*)</id>", e); up = re.search(r"<updated>([^<]*)</updated>", e)
                    fo.write(json.dumps({"zip": os.path.basename(zp), "member": m, "id": idm.group(1) if idm else None,
                                         "updated": up.group(1) if up else None, "xml": e}, ensure_ascii=False) + "\n")
                    fo.flush()
        open(a.log, "a").write(f"{time.strftime('%FT%TZ', time.gmtime())} DONE {zp} members={n_mem} entries={n_ent} kept={n_keep} secs={time.time()-t0:.0f} zipbytes={os.path.getsize(zp)}\n")
        print(zp, n_mem, n_ent, n_keep, file=sys.stderr)

if __name__ == "__main__":
    main()
