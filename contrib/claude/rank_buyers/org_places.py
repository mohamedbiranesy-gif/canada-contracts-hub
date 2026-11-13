#!/usr/bin/env python3
"""Registered addresses of organisations from public registries, for rank.py's P13 (location in Canada + province). No AI.

Writes org_places.csv.gz next to this file: buyer_key, name, address, city, province, postal_code, country, source
(the source file URLs are the constants below).
  cra:<BN9>        CRA "List of charities" Identification files 2022-2024 (open.canada.ca), latest year first; only charities
                   with a web address in that year's Charity Contact Web Addresses file
  onps:<number>    Ontario "Private school contact information" (data.ontario.ca)
  abed:s<code>     Alberta "Alberta schools and authorities" (open.alberta.ca), schools; abed:a<code> = school authorities
  lead:<hash>      2026-11-13: written by tools/bps_energy.py leads — the address of an Ontario public body (school board, municipality,
                   hospital, college, university) in Ontario's school board contact list or directory of institutions under FIPPA / MFIPPA,
                   under the key of its lead; kept as they are when this script rebuilds the file
The same keys are used by the crawler task lists built from these registries (claude_buyer_ap_batch910-914, local work
lists on the crawler Mac). Downloads are cached in ~/.cache/cch-org-places/ (one request per file, identified UA).
Usage: python3 contrib/claude/rank_buyers/org_places.py
"""
import csv, gzip, io, os, urllib.request

UA = "canada-contracts-hub-orgplaces/1.0 (+https://github.com/mohamedbiranesy-gif/canada-contracts-hub)"
CACHE = os.path.expanduser("~/.cache/cch-org-places")
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "org_places.csv.gz")
OC = "https://open.canada.ca/data/dataset/"
CRA = [("2024", OC + "80c00cdb-1358-415c-bb8b-0de7f12675b8/resource/694fdc72-eae4-4ee0-83eb-832ab7b230e3/download/ident_2024_updated.csv"),
       ("2023", OC + "05b3abd0-e70f-4b3b-a9c5-acc436bd15b6/resource/31a52caf-fa79-4ab3-bded-1ccc7b61c17f/download/ident_2023_updated.csv"),
       ("2022", OC + "b2acb3be-c720-4329-a8c0-d4d36c8db61e/resource/4284197f-73f9-4c28-8e4f-56aeaf9414cf/download/ident_2022_updated.csv")]
WEB = [OC + "80c00cdb-1358-415c-bb8b-0de7f12675b8/resource/e3567bb5-5d98-44d0-b0e8-9cdd3732c9e4/download/weburl_2024_updated.csv",
       OC + "05b3abd0-e70f-4b3b-a9c5-acc436bd15b6/resource/204222a0-eefc-4ccc-8c29-b6ecea0f6eb5/download/weburl_2023_updated.csv",
       OC + "b2acb3be-c720-4329-a8c0-d4d36c8db61e/resource/26a5ca19-77ed-4fad-a522-a3bf37c7956b/download/weburl_2022_updated.csv"]
ONPS = "https://data.ontario.ca/dataset/7a049187-cf29-4ffe-9028-235b95c61fa3/resource/d16de265-35e9-4277-9381-0c311e802e39/download/private_school_contact_information_eng.csv"
ABED = "https://education.alberta.ca/media/1626669/authority_and_school.xlsx"
PROV = {"ON", "QC", "BC", "AB", "MB", "SK", "NS", "NB", "NL", "PE", "YT", "NT", "NU"}


def get(url):
    os.makedirs(CACHE, exist_ok=True)
    p = os.path.join(CACHE, url.rsplit("/", 1)[-1])
    if not os.path.exists(p):
        with urllib.request.urlopen(urllib.request.Request(url, headers={"User-Agent": UA}), timeout=300) as r, open(p + ".part", "wb") as f:
            f.write(r.read())
        os.replace(p + ".part", p)
    return p


def main():
    out, has_web = {}, set()  # charities with a web address (Charity Contact Web Addresses): the ones the crawler reads
    for url in WEB:
        for r in csv.DictReader(open(get(url), encoding="utf-8-sig", errors="replace")):
            if (r.get("Contact URL") or "").strip().strip('"'):
                has_web.add("cra:" + (r.get("BN/NE") or "")[:9])
    for year, url in CRA:
        for r in csv.DictReader(open(get(url), encoding="utf-8-sig", errors="replace")):
            k = "cra:" + (r.get("BN") or "")[:9]
            if len(k) != 13 or k in out or k not in has_web:
                continue
            prov = (r.get("Province") or "").strip().upper()
            out[k] = {"buyer_key": k, "name": (r.get("Account Name") or r.get("Legal Name") or "").strip(),
                      "address": " ".join(x.strip() for x in (r.get("Address Line 1") or "", r.get("Address Line 2") or "") if x.strip()),
                      "city": (r.get("City") or "").strip().title(), "province": prov if prov in PROV else "",
                      "postal_code": (r.get("Postal Code") or "").strip(), "country": (r.get("Country") or "CA").strip().upper() or "CA",
                      "source": "the CRA List of charities %s (open.canada.ca)" % year}
    for r in csv.DictReader(open(get(ONPS), encoding="latin1")):
        k = "onps:" + r["School Number"].strip()
        out[k] = {"buyer_key": k, "name": r["School Name"].strip(), "address": r["Street Address"].strip(), "city": r["City"].strip(),
                  "province": "ON", "postal_code": r["Postal Code"].strip(), "country": "CA",
                  "source": "Ontario's Private school contact information (data.ontario.ca)"}
    try:
        import openpyxl
        rows = list(openpyxl.load_workbook(get(ABED), read_only=True).worksheets[0].iter_rows(values_only=True))
        hdr = rows[2]
        for row in rows[3:]:
            d = {h: ("" if v is None else str(v).strip()) for h, v in zip(hdr, row) if h}
            if not d.get("School Code"):
                continue
            src = "Alberta schools and authorities (open.alberta.ca)"
            out["abed:s" + d["School Code"]] = {"buyer_key": "abed:s" + d["School Code"], "name": d.get("School Name", ""),
                                               "address": d.get("School Address1", ""), "city": d.get("School City", ""), "province": "AB",
                                               "postal_code": d.get("School Postal Code", ""), "country": "CA", "source": src}
            if d.get("Authority Code"):
                out.setdefault("abed:a" + d["Authority Code"], {"buyer_key": "abed:a" + d["Authority Code"], "name": d.get("Authority Name", ""),
                               "address": d.get("Authority Address1", ""), "city": d.get("Authority City", ""), "province": "AB",
                               "postal_code": d.get("Authority Postal Code", ""), "country": "CA", "source": src})
    except ImportError:
        print("openpyxl missing: Alberta schools skipped")
    cols = ["buyer_key", "name", "address", "city", "province", "postal_code", "country", "source"]
    if os.path.exists(OUT):  # the rows tools/bps_energy.py adds (lead keys, Ontario's own directories) are not this script's to rebuild
        with gzip.open(OUT, "rt", encoding="utf-8") as f:
            for r in csv.DictReader(f):
                if r["buyer_key"].startswith("lead:") and r["buyer_key"] not in out:
                    out[r["buyer_key"]] = r
    with gzip.open(OUT, "wt", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=cols)
        w.writeheader()
        for k in sorted(out):
            w.writerow(out[k])
    print("org_places:", len(out), "rows ->", OUT)


if __name__ == "__main__":
    main()
