#!/usr/bin/env python3
"""Pass 1: for each distinct Vendor ID whose prefix is in PREFIXES (Comptroller-assigned TINs: foreign vendors, state
agencies, etc.), fetch ONE contract detail page to learn the vendor's address/state. Pass 2: for vendor IDs whose State is a
Canadian province, fetch ALL their active contracts' detail pages.
usage: python3 -I fetch_by_vendor.py <lbb_download_csv> <out_dir>
"""
import sys, csv, re, os, json, time, urllib.request, urllib.parse, http.cookiejar
sys.path.insert(0, "scripts/us_state_texas_lbb")
from fetch_details import parse_vendor, UA

PREFIXES = tuple(os.environ.get("LBB_PREFIXES", "3,5,9,6,8,4,2,U,0,u").split(","))  # "u" = "ue-" unverified-entity IDs (added on resume)
PROV = {"ON", "QC", "BC", "AB", "MB", "SK", "NS", "NB", "NL", "PE", "NT", "YT", "NU", "PQ"}


def is_canadian_block(v):
    """Structured State is a province code, OR (State is '--'/blank and City/address lines name CANADA or a province + Canadian postal code)."""
    st = (v.get("State") or "").strip().upper()
    if st in PROV:
        return True
    txt = " ".join((v.get(k) or "") for k in ("Address Line 1", "Address Line 2", "Address Line 3", "Address Line 4", "City")).upper()
    if st in ("--", "", "ZZ", "XX"):
        if re.search(r"\bCANADA\b", txt):
            return True
        if re.search(r"\b(ON|QC|BC|AB|MB|SK|NS|NB|NL|PE|ONTARIO|QUEBEC|BRITISH COLUMBIA|ALBERTA|MANITOBA|SASKATCHEWAN|NOVA SCOTIA|NEW BRUNSWICK)\b", txt) and re.search(r"\b[A-Z]\d[A-Z] ?\d[A-Z]\d\b", txt):
            return True
    return False


def fetch(opener, url, log):
    for attempt in range(5):
        try:
            with opener.open(url, timeout=120) as resp:
                return resp.read().decode("utf-8", errors="replace"), resp.geturl()
        except Exception as e:
            log.write(f"retry {attempt} {url} {e}\n"); log.flush()
            time.sleep(2 * (attempt + 1))
    return None, None


def main():
    path, out_dir = sys.argv[1], sys.argv[2]
    os.makedirs(os.path.join(out_dir, "html"), exist_ok=True)
    log = open(os.path.join(out_dir, "fetch_by_vendor.log"), "a")
    cj = http.cookiejar.CookieJar()
    opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj))
    opener.addheaders = [("User-Agent", UA)]
    rows = list(csv.DictReader(open(path, newline="", encoding="utf-8")))
    byvid = {}
    for r in rows:
        vid = r["Vendor ID"].strip('"')
        if vid[:1] in PREFIXES:
            byvid.setdefault(vid, []).append(r)
    vendors_path = os.path.join(out_dir, "vendor_probe.jsonl")
    probed = {}
    if os.path.exists(vendors_path):
        for line in open(vendors_path, encoding="utf-8"):
            j = json.loads(line); probed[j["vid"]] = j
    log.write(f"{time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())} PASS1 vendors={len(byvid)} probed={len(probed)}\n"); log.flush()
    with open(vendors_path, "a", encoding="utf-8") as fo:
        for i, (vid, rs) in enumerate(byvid.items()):
            if vid in probed:
                continue
            m = re.search(r"href='([^']+)'", rs[0]["Contract-ID"])
            url = m.group(1).replace(" ", "%20")
            htm, final = fetch(opener, url, log)
            if htm is None:
                continue
            v = parse_vendor(htm)
            j = {"vid": vid, "probe_url": url, "final_url": final, "fetched_at": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
                 "vendor_block": v, "n_contracts": len(rs), "vendor_name_csv": rs[0]["Vendor"]}
            fo.write(json.dumps(j, ensure_ascii=False) + "\n"); fo.flush()
            probed[vid] = j
            if (i + 1) % 20 == 0:
                log.write(f"{time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())} pass1 {i+1}/{len(byvid)}\n"); log.flush()
            time.sleep(0.3)
    ca_vids = [vid for vid, j in probed.items() if is_canadian_block(j["vendor_block"])]
    log.write(f"{time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())} PASS2 canadian vendors={len(ca_vids)} {ca_vids}\n"); log.flush()
    details_path = os.path.join(out_dir, "details_canadian.jsonl")
    done = set()
    if os.path.exists(details_path):
        for line in open(details_path, encoding="utf-8"):
            done.add(json.loads(line)["cid"])
    with open(details_path, "a", encoding="utf-8") as fo:
        for vid in ca_vids:
            for r in byvid[vid]:
                m = re.search(r"href='([^']+)'", r["Contract-ID"])
                url = m.group(1).replace(" ", "%20")
                q = urllib.parse.parse_qs(urllib.parse.urlparse(url).query)
                aid, cid = q.get("aid", [""])[0], q.get("cid", [""])[0]
                if cid in done:
                    continue
                htm, final = fetch(opener, url, log)
                if htm is None:
                    continue
                fn = os.path.join(out_dir, "html", re.sub(r"[^A-Za-z0-9_.-]", "_", f"{aid}_{cid}") + ".html")
                open(fn, "w", encoding="utf-8").write(htm)
                v = parse_vendor(htm)
                rec = {"aid": aid, "cid": cid, "url": url, "final_url": final, "fetched_at": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
                       "vendor_block": v, "csv_row": r, "html_file": fn}
                fo.write(json.dumps(rec, ensure_ascii=False) + "\n"); fo.flush()
                done.add(cid)
                time.sleep(0.3)
    log.write(f"{time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())} DONE\n"); log.close()


if __name__ == "__main__":
    main()
