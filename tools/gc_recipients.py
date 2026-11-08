#!/usr/bin/env python3
"""Federal proactive disclosure of grants and contributions (open.canada.ca, dataset 432527ab-7aac-45b5-81d6-7597107a7013): every
agreement names the recipient and, for most, its Business Number (recipient_business_number), legal name, city, province, postal
code. Municipalities, universities, hospitals, school boards, non-profits and companies all receive federal grants, so this is a
public source of BNs for buyers (downstream §3.2) and vendors (§2.1) that no registry match covered.

Match rule: the recipient's legal / operating name equals the organisation's name after normalisation (accents, punctuation,
legal-form words) and the province agrees when both are known; a name carried by several different BNs is `ambiguous` and skipped.
Output <repo>/data/incoming/claude/claude_gc_recipients.csv with the resource URL as evidence and the matched row as the quote.
  python3 tools/gc_recipients.py --ranked ~/cch-tasks/ranked_latest.csv.gz [--workdir ~/cch-tasks/gc] [--repo ~/cch-crawler]
"""
import argparse, collections, csv, datetime, gzip, io, json, os, re, sys, unicodedata, urllib.parse, urllib.request, zipfile

csv.field_size_limit(1 << 30)
UA = "canada-contracts-hub-crawler/1.0 (+https://github.com/mohamedbiranesy-gif/canada-contracts-hub)"
PKG = "https://open.canada.ca/data/api/3/action/package_show?id=432527ab-7aac-45b5-81d6-7597107a7013"
TODAY = datetime.date.today().isoformat()
COLS = ["kind", "key", "name", "matched_name", "bn_as_published", "bn9", "province", "city", "postal_code", "recipient_type", "agreements", "last_agreement_date", "last_agreement_title", "match_basis",
        "source_url", "retrieved_date", "source_quote"]
LEGAL = {"inc", "incorporated", "incorporee", "incorporée", "ltd", "limited", "ltee", "ltée", "limitee", "limitée", "corp", "corporation", "co", "company", "cie", "compagnie", "llc", "llp", "lp",
         "enr", "enrg", "senc", "sencrl", "ulc", "plc", "the", "la", "le", "les", "l", "d", "de", "du", "des", "and", "et", "&", "of", "a"}
PROV = {"alberta": "AB", "british columbia": "BC", "colombie-britannique": "BC", "manitoba": "MB", "new brunswick": "NB", "nouveau-brunswick": "NB", "newfoundland and labrador": "NL", "terre-neuve-et-labrador": "NL",
        "nova scotia": "NS", "nouvelle-ecosse": "NS", "northwest territories": "NT", "territoires du nord-ouest": "NT", "nunavut": "NU", "ontario": "ON", "prince edward island": "PE", "ile-du-prince-edouard": "PE",
        "quebec": "QC", "saskatchewan": "SK", "yukon": "YT"}
PROV_RX = re.compile(r"\b(AB|BC|MB|NB|NL|NS|NT|NU|ON|PE|QC|SK|YT|Alberta|British Columbia|Colombie-Britannique|Manitoba|New Brunswick|Nouveau-Brunswick|Newfoundland(?: and Labrador)?|Nova Scotia|Nouvelle-[EÉ]cosse|Ontario|Prince Edward Island|Qu[eé]bec|Saskatchewan|Yukon)\b")


def norm(s):
    s = unicodedata.normalize("NFKD", s or "").encode("ascii", "ignore").decode().lower().replace("&", " and ")
    return " ".join(t for t in re.findall(r"[a-z0-9]+", s) if t not in LEGAL)


def pcode(s):
    s = (s or "").strip()
    if len(s) == 2:
        return s.upper()
    return PROV.get(unicodedata.normalize("NFKD", s).encode("ascii", "ignore").decode().lower(), "")


def prov_of(*texts):
    for t in texts:
        m = PROV_RX.search(t or "")
        if m:
            return pcode(m.group(1))
    return ""


def fetch(url, dest):
    if os.path.exists(dest) and os.path.getsize(dest) > 1000:
        return dest
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    with urllib.request.urlopen(req, timeout=600) as r, open(dest + ".part", "wb") as f:
        while True:
            b = r.read(1 << 20)
            if not b:
                break
            f.write(b)
    os.replace(dest + ".part", dest)
    return dest


def main():
    a = argparse.ArgumentParser()
    a.add_argument("--ranked", default=os.path.expanduser("~/cch-tasks/ranked_latest.csv.gz"))
    a.add_argument("--workdir", default=os.path.expanduser("~/cch-tasks/gc"))
    a.add_argument("--repo", default=os.path.expanduser("~/cch-crawler"))
    a = a.parse_args()
    os.makedirs(a.workdir, exist_ok=True)
    pkg = json.loads(urllib.request.urlopen(urllib.request.Request(PKG, headers={"User-Agent": UA}), timeout=60).read())
    res = [r for r in pkg["result"]["resources"] if (r.get("format") or "").upper() in ("CSV", "ZIP") and re.search(r"grants", (r.get("name") or "") + (r.get("url") or ""), re.I) and not re.search(r"nil|dictionary|schema", (r.get("name") or "") + (r.get("url") or ""), re.I)]
    res.sort(key=lambda r: (not (r.get("url") or "").endswith(".csv"), -(r.get("size") or 0)))
    if not res:
        sys.exit("no grants CSV resource found: " + "; ".join((r.get("name") or "") + " " + (r.get("url") or "") for r in pkg["result"]["resources"]))
    url = res[0]["url"]
    dest = fetch(url, os.path.join(a.workdir, os.path.basename(urllib.parse.urlparse(url).path)))
    print("resource:", url, os.path.getsize(dest), "bytes", flush=True)
    fh = zipfile.ZipFile(dest).open([n for n in zipfile.ZipFile(dest).namelist() if n.lower().endswith(".csv")][0]) if dest.endswith(".zip") else open(dest, "rb")
    rd = csv.DictReader(io.TextIOWrapper(fh, encoding="utf-8-sig", errors="replace", newline=""))
    # index: normalised recipient name -> {bn: stats}
    idx = collections.defaultdict(lambda: collections.defaultdict(lambda: {"n": 0, "last": "", "title": "", "row": None, "prov": collections.Counter()}))
    cols = None
    n = 0
    for r in rd:
        if cols is None:
            cols = list(r.keys()); print("columns:", cols[:40], flush=True)
        n += 1
        bn = (r.get("recipient_business_number") or "").strip()
        bn9 = re.sub(r"\D", "", bn)[:9]
        if not bn or len(bn9) < 9 or bn9 in ("999999999", "000000000", "123456789") or re.fullmatch(r"(\d)\1{8}", bn9):
            continue  # placeholder numbers departments key when the recipient has no BN (reviewer 2026-11-08: 999999999 on 22 rows)
        rtype = (r.get("recipient_type") or "").strip().upper()
        legal = (r.get("recipient_legal_name") or "").strip()
        if rtype in ("P", "I") or re.match(r"^[A-Z][A-Za-zÀ-ÿ'’\- ]{1,40},\s*[A-Z][A-Za-zÀ-ÿ'’\-]{1,30}(?:\s+[A-Z]\.?)?$", legal):
            continue  # individuals (recipient_type P = person; "Surname, Given"): never a buyer or vendor organisation
        names = {legal, r.get("recipient_operating_name")}
        for nm in names:
            k = norm(nm)
            if len(k) < 4:
                continue
            e = idx[k][re.sub(r"\s", "", bn)]
            e["n"] += 1
            d = (r.get("agreement_start_date") or r.get("agreement_date") or "")[:10]
            if d >= e["last"]:
                e["last"], e["title"], e["row"] = d, (r.get("agreement_title_en") or "")[:120], r
            e["prov"][pcode(r.get("recipient_province"))] += 1
        if n % 200000 == 0:
            print(n, "rows read;", len(idx), "names", flush=True)
    print("rows:", n, "| recipient names with a BN:", len(idx), flush=True)
    op = gzip.open if a.ranked.endswith(".gz") else open
    out_rows, seen = [], set()
    with op(a.ranked, "rt", encoding="utf-8", newline="") as f:
        for x in csv.DictReader(f):
            if not x.get("email"):
                continue
            key = (x.get("keys") or "").split("|")[0]
            cands = []
            if not (x.get("buyer_bn_as_published") or "").strip() and key and ("buyer", key) not in seen:
                bl = x.get("buyer_legal_name_as_published") or ""
                bl = bl.split(" (")[0] if bl and not re.search(r"\((?:stated on|schema\.org|recipient legal name|as registered)", bl) else ""  # never match on a name that was itself inferred from a page or another dataset
                cands.append(("buyer", key, [x.get("buyer"), bl], prov_of(x.get("jurisdiction") or "", x.get("buyer_address") or "")))
            v = (x.get("vendor") or "").strip()
            if v and not v.startswith("inferred") and not (x.get("vendor_bn9") or "").strip() and ("vendor", v) not in seen:
                cands.append(("vendor", v, [v, (x.get("vendor_legal_name") or "").split(" (")[0]], prov_of(x.get("vendor_address") or "", x.get("vendor_registered_address") or "", x.get("vendor_country_basis") or "")))
            for kind, k, names, prov in cands:
                seen.add((kind, k))
                hit = None
                for nm in names:
                    kn = norm(nm)
                    if len(kn) < 4 or kn not in idx:
                        continue
                    bns = idx[kn]
                    if len(bns) > 1:
                        agree = [b for b, e in bns.items() if prov and e["prov"].most_common(1)[0][0] == prov]
                        if len(agree) != 1:
                            hit = ("ambiguous", kn, None); break
                        bn = agree[0]
                    else:
                        bn = next(iter(bns))
                    e = bns[bn]
                    bp = e["prov"].most_common(1)[0][0]
                    if prov and bp and bp != prov:
                        continue
                    hit = ("found", kn, (bn, e)); break
                if not hit or hit[0] != "found":
                    continue
                bn, e = hit[2]
                r = e["row"]
                out_rows.append({"kind": kind, "key": k, "name": names[0], "matched_name": r.get("recipient_legal_name") or r.get("recipient_operating_name") or "", "bn_as_published": bn, "bn9": re.sub(r"\D", "", bn)[:9],
                                 "province": r.get("recipient_province") or "", "city": r.get("recipient_city") or "", "postal_code": r.get("recipient_postal_code") or "", "recipient_type": r.get("recipient_type") or "",
                                 "agreements": e["n"], "last_agreement_date": e["last"], "last_agreement_title": e["title"],
                                 "match_basis": "recipient name equals the organisation's name" + ("; province agrees" if prov and bp else ("; recipient province blank, not checked" if prov else "; no province known for the organisation, not checked")), "source_url": url, "retrieved_date": TODAY,
                                 "source_quote": ("%s; %s; %s %s; %s %s" % (r.get("recipient_legal_name") or "", bn, r.get("recipient_city") or "", r.get("recipient_province") or "", e["last"], e["title"]))[:300]})
    out = os.path.join(a.repo, "data/incoming/claude/claude_gc_recipients.csv")
    with open(out, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=COLS); w.writeheader(); w.writerows(out_rows)
    print("wrote", out, len(out_rows), "organisations matched (%d buyers, %d vendors)" % (sum(1 for r in out_rows if r["kind"] == "buyer"), sum(1 for r in out_rows if r["kind"] == "vendor")), flush=True)


if __name__ == "__main__":
    main()
