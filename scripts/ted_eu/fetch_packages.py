#!/usr/bin/env python3
"""Download TED daily OJS packages (tar.gz of notice XMLs) for the OJS issues of the
notices found in <api_dir>, extract only the wanted notice XML files into <xml_dir>,
then delete the tarball. Checkpointed: skips notices whose XML already exists.

Usage: python3 -I fetch_packages.py <api_dir> <xml_dir> <tmp_dir>
"""
import json, os, re, sys, tarfile, time
import requests

H = {"User-Agent": "contracts-research/1.0"}


def pkg_id(ojs):
    # "177/2023" -> 202300177
    no, yr = ojs.split("/")
    return f"{yr}{int(no):05d}"


def main():
    api_dir, xml_dir, tmp_dir = sys.argv[1:4]
    os.makedirs(xml_dir, exist_ok=True)
    os.makedirs(tmp_dir, exist_ok=True)
    wanted = {}  # ojs -> set(pubno)
    for fn in os.listdir(api_dir):
        if not fn.endswith(".json") or fn.startswith("_"):
            continue
        n = json.load(open(os.path.join(api_dir, fn)))
        pn = n.get("publication-number")
        ojs = n.get("ojs-number") or n.get("OJ")
        if not pn or not ojs:
            continue
        if os.path.exists(os.path.join(xml_dir, pn + ".xml")):
            continue
        wanted.setdefault(ojs, set()).add(pn)
    print(f"{sum(len(v) for v in wanted.values())} notices across {len(wanted)} OJS issues", flush=True)
    log = {}
    for i, (ojs, pns) in enumerate(sorted(wanted.items(), key=lambda kv: pkg_id(kv[0]))):
        pid = pkg_id(ojs)
        url = f"https://ted.europa.eu/packages/daily/{pid}"
        tgz = os.path.join(tmp_dir, pid + ".tar.gz")
        ok = False
        for attempt in range(4):
            try:
                with requests.get(url, headers=H, stream=True, timeout=300) as r:
                    if r.status_code != 200:
                        print(pid, "HTTP", r.status_code, flush=True)
                        time.sleep(2 * (attempt + 1))
                        continue
                    with open(tgz, "wb") as f:
                        for chunk in r.iter_content(1 << 20):
                            f.write(chunk)
                ok = True
                break
            except requests.RequestException as e:
                print(pid, "error", e, flush=True)
                time.sleep(3 * (attempt + 1))
        if not ok:
            log[ojs] = {"package": url, "status": "download_failed"}
            continue
        found = set()
        # notice number variants: 553483-2023 -> 00553483_2023.xml or 553483_2023.xml
        want_names = {}
        for pn in pns:
            num, yr = pn.split("-")
            want_names[f"{int(num)}_{yr}.xml"] = pn  # padding-agnostic key
        try:
            with tarfile.open(tgz, "r:gz") as tf:
                for m in tf:
                    base = os.path.basename(m.name)
                    try:
                        key = f"{int(base.split('_')[0])}_{base.split('_', 1)[1]}"
                    except (ValueError, IndexError):
                        key = None
                    if key in want_names and m.isfile():
                        pn = want_names[key]
                        data = tf.extractfile(m).read()
                        with open(os.path.join(xml_dir, pn + ".xml"), "wb") as f:
                            f.write(data)
                        found.add(pn)
        except Exception as e:
            print(pid, "tar error", e, flush=True)
        size = os.path.getsize(tgz)
        os.remove(tgz)
        log[ojs] = {"package": url, "bytes": size, "wanted": sorted(pns), "found": sorted(found), "missing": sorted(pns - found)}
        if (i + 1) % 20 == 0:
            print(f"{i+1}/{len(wanted)} packages done", flush=True)
        time.sleep(0.4)
    with open(os.path.join(xml_dir, "_packages_log.json"), "w") as f:
        json.dump(log, f, indent=1)
    missing = [m for v in log.values() for m in v.get("missing", [])]
    print("done. missing XML:", len(missing), missing[:30])


if __name__ == "__main__":
    main()
