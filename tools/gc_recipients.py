#!/usr/bin/env python3
"""Federal proactive disclosure of grants and contributions (open.canada.ca, dataset 432527ab-7aac-45b5-81d6-7597107a7013): every
agreement names the recipient and, for most, its Business Number (recipient_business_number), legal name, city, province, postal
code. Municipalities, universities, hospitals, school boards, non-profits and companies all receive federal grants, so this is a
public source of BNs for buyers (downstream §3.2) and vendors (§2.1) that no registry match covered.

Match rule: the recipient's legal / operating name equals the organisation's name after normalisation (accents, punctuation,
legal-form words) and the province agrees when both are known; a name carried by several different BNs is `ambiguous` and skipped.
2026-11-10: the place must not disagree, and a name alone is not enough everywhere. When the organisation's address is on file, its
postal code (first three characters) or the recipient's city in it settles the match, and another postal code with another city
refuses it; without an address the organisation must be in Canada by its record or its .ca address, and its name must not be one
that many congregations and clubs carry ("Holy Trinity Armenian Church" of Pennsylvania had been given the record of the church of
that name in Scarborough). Runs daily in the cloud (claude-engines.yml, bulk_registry step); until this day the file was one made on
the owner's Mac on 2026-11-08 for a table of 65,000 rows.
Output <repo>/data/incoming/claude/claude_gc_recipients.csv with the resource URL as evidence and the matched row as the quote.
  python3 tools/gc_recipients.py [--ranked coord/results/ranked/ranked_buyers.csv.gz] [--workdir ~/cch-tasks/gc] [--repo .]
"""
import argparse, collections, csv, datetime, gzip, io, json, os, re, sys, unicodedata, urllib.parse, urllib.request, zipfile

csv.field_size_limit(1 << 30)
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import ranked_io as RIO  # noqa: E402
from charity_buyers import needs_place  # noqa: E402
ROOT = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
_PN = r"[A-Za-zÀ-ÿ][A-Za-zÀ-ÿ'’\-]{1,19}"
# natural persons as a recipient's legal name: "Surname, Given Given", "Given S Surname, Given D Surname", "Given Surname & Given Surname" — in any letter case
PERSONS = re.compile(r"^(?:" + _PN + r"(?: " + _PN + r")?,\s*" + _PN + r"(?:\s+(?:" + _PN + r"|[A-Za-z]\.?)){0,2}"
                     r"|" + _PN + r"(?: [A-Za-z]\.?)?(?: " + _PN + r"){1,2}(?:\s*(?:,|&|\band\b|\bet\b|/)\s*" + _PN + r"(?: [A-Za-z]\.?)?(?: " + _PN + r"){1,2})+)$")
ORG_WORD = re.compile(r"\b(?:inc|ltd|limited|lt[ée]e|corp|corporation|llp|company|co|cie|society|soci[ée]t[ée]|association|club|church|[ée]glise|farms?|fermes?|foundation|fondation|centre|center|group|groupe|services?|"
                      r"enterprises?|entreprises?|holdings|partners|partnership|council|conseil|nation|band|school|[ée]cole|college|university|universit[ée]|city|town|ville|village|municipalit\w*|district|hospital|"
                      r"h[ôo]pital|library|museum|mus[ée]e|institute|institut|studio|shop|store|restaurant|caf[ée]|hotel|inn|ranch|orchards?|gardens?|vineyards?|winery|brewery|bakery|market|construction|"
                      r"contracting|consulting|productions?|media|design|photography|trucking|transport|logging|fisheries|dairy|acres|estates?|parish|paroisse|place|house|maison|mission|ministr\w+|temple|"
                      r"mosque|academy|acad[ée]mie|camp|lodge|legion|branch|hall|theatre|th[ée][âa]tre|gallery|galerie|press|books|radio|network|r[ée]seau|alliance|coalition|federation|f[ée]d[ée]ration|"
                      r"union|guild|league|ligue|team|[ée]quipe|choir|ch[oœ]ur|orchestra|orchestre|ensemble|festival|fair|exhibition|project|projet|program\w*|initiative|fund|fonds|trust|agency|agence|"
                      r"authority|board|commission|committee|comit[ée]|office|bureau|department|government|gouvernement|systems?|syst[èe]mes?|solutions?|technolog\w+|industries|international|canada|"
                      r"communit\w+|communaut\w+|coop\w*|co-op\w*|caisse|bank|banque|clinic|clinique|pharmac\w+|dental|medical|health|sant[ée]|sports?|arts?|culture\w*|tourism\w*|development|"
                      r"d[ée]veloppement|management|gestion|logistics|energy|[ée]nergie|power|electric\w*|mechanical|plumbing|roofing|landscaping|homes?|properties|realty|investments?|capital|"
                      r"ventures?|labs?|laboratories|research|recherche|training|formation|learning|education|[ée]ducation|daycare|garderie|childcare|preschool|kids|youth|jeunesse|seniors?|a[îi]n[ée]s)\b", re.I)
CA_PC = re.compile(r"(?<![A-Z0-9])([ABCEGHJ-NPRSTVXY]\d[ABCEGHJ-NPRSTV-Z])\s?(\d[ABCEGHJ-NPRSTV-Z]\d)(?![A-Z0-9])")
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
    a.add_argument("--ranked", default=RIO.DEFAULT)
    a.add_argument("--workdir", default=os.path.expanduser("~/cch-tasks/gc"))
    a.add_argument("--repo", default=ROOT)
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
    n = persons = 0
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
        if PERSONS.match(legal) and not ORG_WORD.search(legal):
            persons += 1
            continue  # a business carried on by natural persons under their own names ("Janis Smith, Mark James Harris" for Harris Flower Farm): left out, as
                      # natural persons are in every register lane of this project
        if len(re.sub(r"\s", "", bn)) > 9 and not re.fullmatch(r"\d{9}\s?R[A-Z]\s?\d{4}", bn.upper()):
            continue  # "900086828XX9999": not a program account of a Business Number
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
    print("rows:", n, "| recipient names with a BN:", len(idx), "| agreements of businesses carried on by natural persons under their own names, left out:", persons, flush=True)
    out_rows, seen = [], set()
    stats = collections.Counter()

    def place(addr, r):
        """the recipient's place against the organisation's address: 'agrees' (same first three characters of the postal code, or the recipient's
        city written in the address), 'differs' (a Canadian postal code of another area and another city, or an address without the city nor any
        Canadian postal code where the recipient has both), '' (no address on file)"""
        addr = addr or ""
        if not addr.strip():
            return ""
        fsa = {m.group(1) for m in CA_PC.finditer(addr.upper())}
        rp = re.sub(r"[^A-Z0-9]", "", (r.get("recipient_postal_code") or "").upper())[:3]
        city = unicodedata.normalize("NFKD", (r.get("recipient_city") or "").strip()).encode("ascii", "ignore").decode().lower()
        al = unicodedata.normalize("NFKD", addr).encode("ascii", "ignore").decode().lower()
        in_city = len(city) >= 3 and re.search(r"(?<![a-z])" + re.escape(city) + r"(?![a-z])", al) is not None
        if rp and rp in fsa:
            return "postal"
        if in_city:
            return "city"
        return "differs" if (fsa and rp) or (city and not fsa) else ""

    if True:
        for x in RIO.rows(a.ranked):
            if not x.get("email"):
                continue
            key = (x.get("keys") or "").split("|")[0]
            _site = (urllib.parse.urlparse(x.get("buyer_website") or "").hostname or "").lower()
            cands = []
            # every organisation is matched, whether its row carries a number already or not: a daily run that skipped the rows it had itself given a
            # number to would drop them from its file, and the next build would lose the number (the ranker decides which source a cell shows)
            if key and ("buyer", key) not in seen:
                bl = x.get("buyer_legal_name_as_published") or ""
                bl = bl.split(" (")[0] if bl and not re.search(r"\((?:stated on|printed with its legal form|the name on the organisation's own home page|the organisation's name as the source|schema\.org|recipient legal name|as registered)", bl) else ""  # never match on a name that was itself inferred from a page or another dataset
                cands.append(("buyer", key, [x.get("buyer"), bl], prov_of(x.get("jurisdiction") or "", x.get("buyer_address") or ""), x.get("buyer_address") or "",
                              (x.get("jurisdiction") or "") in ("CA", "FED", "AB", "BC", "MB", "NB", "NL", "NS", "NT", "NU", "ON", "PE", "QC", "SK", "YT") or _site.endswith(".ca")))
            v = (x.get("vendor") or "").strip()
            if v and not v.startswith("inferred") and ("vendor", v) not in seen:
                cands.append(("vendor", v, [v, (x.get("vendor_legal_name") or "").split(" (")[0]], prov_of(x.get("vendor_address") or "", x.get("vendor_registered_address") or "", x.get("vendor_country_basis") or ""),
                              (x.get("vendor_address") or "") + " " + (x.get("vendor_registered_address") or ""), True))  # a vendor of this table is located in Canada by its source record
            for kind, k, names, prov, addr, in_canada in cands:
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
                    pl = place(addr, e["row"])
                    # the name that agreed: the recipient's legal name, or only the name it operates under
                    via = "legal" if norm(e["row"].get("recipient_legal_name")) == kn else "operating"
                    rtype = (e["row"].get("recipient_type") or "").strip().upper()
                    own_name = not needs_place(nm) and len(kn.split()) >= 2  # not a name many congregations and clubs carry, and more than one word
                    if pl == "differs" and prov and bp and via == "legal" and own_name:
                        pl = "prov"  # another city of the same province, under the same legal name: an organisation with several offices ("Water Security Agency")
                    if pl == "differs":
                        stats[kind + ": same name, another place — not taken"] += 1
                        continue
                    # A trade name is shared by the franchisees of a chain and by namesakes more than a legal name is ("Paramount Fine Foods" is SKIES
                    # ENTERPRISE INC. for one restaurant): for a business it needs the postal code area; for a public body, a First Nation, a school or
                    # a non-profit ("Region of Halton" for The Regional Municipality of Halton) the city is enough
                    if via == "operating" and not (pl == "postal" or (pl == "city" and rtype in ("G", "A", "S", "N")) or (pl in ("", "prov") and rtype in ("G", "A", "S") and in_canada and own_name)):
                        stats[kind + ": the recipient's operating name only, nothing to settle it — not taken"] += 1
                        continue
                    if not pl and not (in_canada and own_name):
                        stats[kind + ": same name, no address on file and no other sign it is this one — not taken"] += 1
                        continue
                    hit = ("found", kn, (bn, e, pl, via)); break
                if not hit or hit[0] != "found":
                    continue
                bn, e, pl, via = hit[2]
                r = e["row"]
                stats[kind + ": %s name%s" % (via, {"postal": " + postal code area", "city": " + city", "prov": " + province (another city)", "": ", in Canada, no address on file"}[pl])] += 1
                out_rows.append({"kind": kind, "key": k, "name": names[0], "matched_name": r.get("recipient_legal_name") or r.get("recipient_operating_name") or "", "bn_as_published": bn, "bn9": re.sub(r"\D", "", bn)[:9],
                                 "province": r.get("recipient_province") or "", "city": r.get("recipient_city") or "", "postal_code": r.get("recipient_postal_code") or "", "recipient_type": r.get("recipient_type") or "",
                                 "agreements": e["n"], "last_agreement_date": e["last"], "last_agreement_title": e["title"],
                                 "match_basis": ("recipient legal name equals the organisation's name" if via == "legal" else "recipient operating name equals the organisation's name") + {"postal": "; postal code area of the organisation's address agrees", "city": "; city of the organisation's address agrees", "prov": "; the organisation's address is in another city of the same province", "": "; the organisation's address is not on file"}[pl] + ("; province agrees" if prov and bp else ("; recipient province blank, not checked" if prov else "; no province known for the organisation, not checked")), "source_url": url, "retrieved_date": TODAY,
                                 "source_quote": ("%s; %s; %s %s; %s %s" % (r.get("recipient_legal_name") or "", bn, r.get("recipient_city") or "", r.get("recipient_province") or "", e["last"], e["title"]))[:300]})
    out = os.path.join(a.repo, "data/incoming/claude/claude_gc_recipients.csv")
    print("matches:", dict(stats), flush=True)
    if os.path.exists(out):  # a match that stands as it stood keeps its date: the file changes in git by its new and changed lines only
        try:
            prev = {(r["kind"], r["key"]): r for r in csv.DictReader(open(out, encoding="utf-8", errors="replace", newline=""))}
            for r in out_rows:
                o = prev.get((r["kind"], r["key"]))
                if o and o.get("retrieved_date") and all(str(o.get(c) or "") == str(r.get(c) or "") for c in COLS if c != "retrieved_date"):
                    r["retrieved_date"] = o["retrieved_date"]
        except Exception as e:
            print("the matches in the repo could not be read (%s): written anew" % e, flush=True)
    out_rows.sort(key=lambda r: (r["kind"], str(r["key"])))
    with open(out, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=COLS); w.writeheader(); w.writerows(out_rows)
    print("wrote", out, len(out_rows), "organisations matched (%d buyers, %d vendors)" % (sum(1 for r in out_rows if r["kind"] == "buyer"), sum(1 for r in out_rows if r["kind"] == "vendor")), flush=True)


if __name__ == "__main__":
    main()
