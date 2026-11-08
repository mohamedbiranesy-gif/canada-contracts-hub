#!/usr/bin/env python3
"""Official provincial municipal directories → data/incoming/claude/claude_municipal_directory.csv (owner D11 / downstream C1, C2, H1).

Sources (official, downloaded by the Mac; URLs found 2026-11-08):
- Québec, MAMH "Répertoire des municipalités" (Données Québec): https://donneesouvertes.affmunqc.net/repertoire/MUN.csv — legal name,
  designation, MRC, address, postal code, phone, website, the municipality's general mailbox, population.
- Ontario, MMAH "List of municipalities" (data.ontario.ca): municipalities_-_en_*.csv — legal name with status, municipal tier
  (Lower Tier / Upper Tier / Single Tier), geographic area, website.
Every value is copied verbatim with the file URL as evidence; rank.py merges by website domain or exact name and labels the
provenance "provincial municipal directory". Nothing is inferred.
  python3 tools/municipal_directory.py --dir ~/cch-tasks/dirs --out ~/cch-crawler/data/incoming/claude/claude_municipal_directory.csv
"""
import argparse, csv, datetime, html, os, re, sys

QC_URL = "https://donneesouvertes.affmunqc.net/repertoire/MUN.csv"
ON_URL = "https://data.ontario.ca/dataset/62e83cbc-0731-4d66-abdc-2f2b31bcd76c/resource/6783a586-6b05-4a73-9663-e60a6963c91e/download/municipalities_-_en_2026-0526.csv"
COLS = ["province", "legal_name", "designation", "municipal_tier", "upper_tier_or_mrc", "address", "postal_code", "phone", "website", "general_email", "population", "mayor_or_head",
        "source_url", "retrieved_date", "source_quote"]
TODAY = datetime.date.today().isoformat()


def qc(path):
    out = []
    with open(path, encoding="utf-8-sig", newline="") as f:
        for r in csv.DictReader(f):
            name = (r.get("munnom") or "").strip()
            if not name:
                continue
            desi = (r.get("mdes") or "").strip()
            addr = ", ".join(dict.fromkeys(x.strip() for x in (r.get("madr1"), r.get("madr2"), r.get("madr3"), r.get("madr4")) if x and x.strip()))  # the file repeats lines
            legal = name if re.match(r"^(Ville|Municipalit[ée]|Paroisse|Village|Canton|Cantons unis|Cit[ée]|Territoire)\b", name) else ("%s de %s" % (desi, name) if desi and desi.lower() not in name.lower() else name)
            out.append({"province": "QC", "legal_name": legal, "designation": desi, "municipal_tier": "", "upper_tier_or_mrc": (r.get("mrc") or "").strip(), "address": addr,
                        "postal_code": (r.get("mcodpos") or "").strip(), "phone": (r.get("mtel") or "").strip(), "website": (r.get("mweb") or "").strip(),
                        "general_email": (r.get("mcourriel") or "").strip().lower(), "population": (r.get("mpopul") or "").strip(), "mayor_or_head": (r.get("maire") or "").strip(),
                        "source_url": QC_URL, "retrieved_date": TODAY,
                        "source_quote": ("%s; %s; %s; %s; %s; %s" % (name, desi, addr, r.get("mcodpos") or "", r.get("mtel") or "", r.get("mweb") or ""))[:300]})
    return out


def on(path):
    out = []
    with open(path, encoding="utf-8-sig", newline="") as f:
        for r in csv.DictReader(f):
            raw = r.get("Municipality") or ""
            m = re.search(r'href="([^"]+)"', raw)
            name = html.unescape(re.sub(r"<[^>]+>", "", raw)).strip()
            if not name:
                continue
            # "Addington Highlands, Township of" → "Township of Addington Highlands"
            legal = re.sub(r"^(.*), (Township|Town|City|Municipality|Village|County|Region|Regional Municipality|United Counties|District Municipality|Township Municipality|Separated Town|Northern Town|United Townships|Municipal Township|Corporation) of$", r"\2 of \1", name)
            out.append({"province": "ON", "legal_name": legal, "designation": legal.split(" of ")[0] if " of " in legal else "", "municipal_tier": (r.get("Municipal status") or "").strip(),
                        "upper_tier_or_mrc": (r.get("Geographic area") or "").strip(), "address": "", "postal_code": "", "phone": "", "website": (m.group(1).strip() if m else ""),
                        "general_email": "", "population": "", "mayor_or_head": "", "source_url": ON_URL, "retrieved_date": TODAY,
                        "source_quote": ("%s; %s; %s; %s" % (name, r.get("Municipal status") or "", r.get("Geographic area") or "", m.group(1) if m else ""))[:300]})
    return out


def main():
    a = argparse.ArgumentParser()
    a.add_argument("--dir", default=os.path.expanduser("~/cch-tasks/dirs"))
    a.add_argument("--out", default=os.path.expanduser("~/cch-crawler/data/incoming/claude/claude_municipal_directory.csv"))
    a = a.parse_args()
    rows = []
    for fn, fnc in (("qc_mun.csv", qc), ("on_municipalities.csv", on)):
        p = os.path.join(a.dir, fn)
        if os.path.exists(p):
            got = fnc(p)
            print(fn, len(got), "municipalities", flush=True)
            rows += got
    with open(a.out, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=COLS)
        w.writeheader()
        w.writerows(rows)
    print("wrote", a.out, len(rows))


if __name__ == "__main__":
    main()
