#!/usr/bin/env python3
"""For notices that are NOT in the TED Search API index (2015 / early 2016) we only know the
publication number (from the CSV), not the OJS issue. Notice numbers are sequential within a
year across daily packages, so binary-search the issue number for each wanted notice by
downloading packages and reading their min/max notice numbers; cache ranges.

Usage: python3 -I scan_packages_by_number.py <ids_json> <xml_dir> <tmp_dir> <year> <max_issue>
"""
import json, os, sys, tarfile, time
import requests

H = {"User-Agent": "contracts-research/1.0"}


class Packages:
    def __init__(self, year, tmp_dir, xml_dir, wanted):
        self.year = year
        self.tmp = tmp_dir
        self.xml_dir = xml_dir
        self.wanted = wanted  # basename -> pubno
        self.ranges = {}  # issue -> (lo, hi) or None if unavailable
        self.found = set()

    def load(self, issue):
        if issue in self.ranges:
            return self.ranges[issue]
        pid = f"{self.year}{issue:05d}"
        url = f"https://ted.europa.eu/packages/daily/{pid}"
        tgz = os.path.join(self.tmp, pid + ".tar.gz")
        data_ok = False
        for attempt in range(3):
            try:
                with requests.get(url, headers=H, stream=True, timeout=300) as r:
                    if r.status_code != 200:
                        self.ranges[issue] = None
                        print(pid, "HTTP", r.status_code, flush=True)
                        return None
                    with open(tgz, "wb") as f:
                        for chunk in r.iter_content(1 << 20):
                            f.write(chunk)
                data_ok = True
                break
            except requests.RequestException:
                time.sleep(3 * (attempt + 1))
        if not data_ok:
            self.ranges[issue] = None
            return None
        lo = hi = None
        try:
            with tarfile.open(tgz, "r:gz") as tf:
                for m in tf:
                    base = os.path.basename(m.name)
                    if not m.isfile() or not base.endswith(".xml"):
                        continue
                    try:
                        n = int(base.split("_")[0])
                        lo = n if lo is None else min(lo, n)
                        hi = n if hi is None else max(hi, n)
                    except ValueError:
                        pass
                    key = None
                    try:
                        key = f"{int(base.split('_')[0])}_{base.split('_', 1)[1]}"
                    except (ValueError, IndexError):
                        pass
                    if key in self.wanted:
                        pn = self.wanted[key]
                        with open(os.path.join(self.xml_dir, pn + ".xml"), "wb") as f:
                            f.write(tf.extractfile(m).read())
                        self.found.add(pn)
        except Exception as e:
            print(pid, "tar error", e, flush=True)
        os.remove(tgz)
        self.ranges[issue] = (lo, hi)
        print(f"{pid}: {lo}-{hi}", flush=True)
        time.sleep(0.3)
        return self.ranges[issue]

    def locate(self, num, max_issue):
        lo_i, hi_i = 1, max_issue
        while lo_i <= hi_i:
            mid = (lo_i + hi_i) // 2
            rng = self.load(mid)
            if rng is None or rng[0] is None:
                # unavailable issue: probe neighbours
                rng2 = self.load(mid + 1) if mid + 1 <= hi_i else None
                if rng2 and rng2[0] is not None:
                    if num < rng2[0]:
                        hi_i = mid - 1
                        continue
                    lo_i = mid + 1
                    continue
                hi_i = mid - 1
                continue
            if num < rng[0]:
                hi_i = mid - 1
            elif num > rng[1]:
                lo_i = mid + 1
            else:
                return mid
        return None


def main():
    ids_json, xml_dir, tmp_dir, year, max_issue = sys.argv[1:6]
    max_issue = int(max_issue)
    os.makedirs(xml_dir, exist_ok=True)
    os.makedirs(tmp_dir, exist_ok=True)
    wanted = {}
    nums = {}
    for pn in json.load(open(ids_json)):
        num, yr = pn.split("-")
        if yr != year or os.path.exists(os.path.join(xml_dir, pn + ".xml")):
            continue
        wanted[f"{int(num)}_{yr}.xml"] = pn
        nums[pn] = int(num)
    print(f"{len(nums)} wanted notices for {year}", flush=True)
    # the found set is keyed by pubno; wanted keys are "<num>_<year>.xml" without zero padding
    pk = Packages(year, tmp_dir, xml_dir, wanted)
    for pn, num in sorted(nums.items(), key=lambda kv: kv[1]):
        if pn in pk.found:
            continue
        issue = pk.locate(num, max_issue)
        print(pn, "-> issue", issue, "found" if pn in pk.found else "NOT FOUND", flush=True)
    with open(os.path.join(xml_dir, f"_scan_log_{year}.json"), "w") as f:
        json.dump({"ranges": pk.ranges, "found": sorted(pk.found)}, f)
    print("done; still missing:", sorted(set(nums) - pk.found))


if __name__ == "__main__":
    main()
