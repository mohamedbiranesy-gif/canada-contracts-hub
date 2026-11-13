#!/usr/bin/env python3
"""The table in the owner's order of priority (2026-11-11 20:36 EST: "we will also include those of lower value but mark them, mark everything,
prioritise over 5000 … no buyer twice is hard rule so it should be 1 million buyers").

Every row carries its amount mark (tools/relationship_rows.py: amount_mark — 1 published $5,000 or more, 2 estimated $5,000 or more,
3 published under $5,000, 4 estimated under $5,000, 5 no amount) and its test (ship_ready). This tool rewrites the built table so that the
rows stand in that order: the rows that meet the test first, by amount mark 1 to 5, then the rows that do not, by the same marks. Inside a
class the ranker's own order is kept. The JSON-lines copy is rewritten in step with it. Constant memory: rows go to one working file per class
and the classes are put back together (the table is meant to hold a million rows).

  python3 tools/priority_sort.py out/ranked        (run by tools/rank_tail.sh before anything reads the table)
"""
import collections, csv, gzip, os, re, shutil, sys, time, unicodedata

csv.field_size_limit(1 << 30)
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from ap_crawler import registrable  # noqa: E402

# 2026-11-12 (owner: "the buyer is not repeated twice"; AGENTS.md §1 rule 14, "no buyer twice is hard rule"): the ranker keeps one row per
# organisation key, but one organisation can come in under two keys — two websites (rockyview.ca and mdrockyview.ab.ca), a contract record and
# a site reading, a name a register later gave the row. In the table of 10:45Z, 915 names stood on two rows and more; most were different
# organisations with the same name (two "Lakeview Dental", two "Camp Massad"), some were one organisation twice. Here, in the order of
# priority, an organisation already written is not written again. Same organisation means: the same name (legal form aside) and the same
# postal code, mail domain or website domain; or the same mail domain and the same postal code (a domain no other body shares).
_NORM = lambda s: re.sub(r"[^a-z0-9]+", " ", unicodedata.normalize("NFKD", s or "").encode("ascii", "ignore").decode().lower()).strip()
_FORMS = re.compile(r"\b(?:inc|incorporated|ltd|ltee|limited|limitee|corp|corporation|co|company|compagnie|cie|llc|llp|lp|plc|sa|sas|senc|the|la|le|les|l|de|du|des|d|et|and|of)\b")
_PC = re.compile(r"\b([A-Z]\d[A-Z])\s?(\d[A-Z]\d)\b")
_SHARED_MAIL = re.compile(r"^(?:gmail|googlemail|hotmail|outlook|live|msn|yahoo|ymail|aol|icloud|me|mac|protonmail|proton|gmx|mail|videotron|sympatico|bell|bellnet|"
                          r"rogers|shaw|telus|cogeco|eastlink|globetrotter|xplornet|sasktel|mts|tbaytel|execulink|cgocable|derytele|axion|sogetel|tlb|cooptel|"
                          r"netrevolution|b2b2c|wightman|persona|personainternet|xittel|maskatel|telupton|ccapcable|tellambton|netcom|qc\.aira|aira|nbnet\.nb|nb\.aibn)\.|"
                          r"(?:^|\.)(?:gov\.[a-z]{2}\.ca|gouv\.qc\.ca|ssss\.gouv\.qc\.ca|canada\.ca|gc\.ca|alberta\.ca|ontario\.ca|gnb\.ca|novascotia\.ca|saskatchewan\.ca|"
                          r"yukon\.ca|gov\.uk|nhs\.net|basware\.com|coupahost\.com|tungsten-network\.com|esker\.com|ariba\.com)$|^mrc", re.I)
_SHARED_SITE = re.compile(r"(?:^|\.)(?:canada\.ca|gc\.ca|quebec\.ca|gouv\.qc\.ca|gov\.[a-z]{2}\.ca|alberta\.ca|ontario\.ca|gnb\.ca|novascotia\.ca|saskatchewan\.ca|"
                          r"yukon\.ca|gov\.uk|wixsite\.com|squarespace\.com|wordpress\.com|myshopify\.com|facebook\.com|linkedin\.com|google\.com)$", re.I)


def _host(u):
    h = re.sub(r"^https?://", "", (u or "").strip().lower()).split("/")[0].split(":")[0].split("?")[0]
    return h[4:] if h.startswith("www.") else h


def identity_keys(buyer, email, website, address):
    nm = re.sub(r"\s+", " ", _FORMS.sub(" ", _NORM(buyer))).strip()
    md = registrable((email or "").partition("@")[2].lower()) if "@" in (email or "") else ""
    sd = registrable(_host(website)) if _host(website) else ""
    m = _PC.search((address or "").upper())
    pc = (m.group(1) + m.group(2)) if m else ""
    keys = []
    if len(nm) >= 3:
        if pc:
            keys.append(("name+postal", nm, pc))
        if md and not _SHARED_MAIL.search(md):
            keys.append(("name+mail domain", nm, md))
        elif md:
            keys.append(("name+mailbox", nm, (email or "").lower()))
        if sd and not _SHARED_SITE.search(sd):
            keys.append(("name+site", nm, sd))
    if md and pc and not _SHARED_MAIL.search(md):
        keys.append(("mail domain+postal", md, pc))
    return keys


_GRADE = {"invoicing/AP": 4, "finance/accounting dept or supplier-payment office": 3, "purchasing": 2, "general": 1}
# rule 13: a record (a contract, a licence, a roster) or a service seen on the buyer's side comes before the distributor of its address
_KIND = {"public contract": 6, "licence or registration": 5, "agent of record": 5, "promotional agency": 5, "exchange listing": 5, "export sale": 6, "benefit plan contract": 6, "membership": 4, "sponsorship": 4, "dealership": 4, "tenancy": 4,
         "service seen on the buyer's side": 3, "utility account by location": 2}
_DOMAIN_ONLY = re.compile(r"^(?:www\.)?[a-z0-9-]+(?:\.[a-z0-9-]+)*\.[a-z]{2,}$", re.I)


def row_score(email_type, kind_cell, buyer):
    """inside one class of priority, the row an organisation keeps: the stronger relationship, then the better mailbox, then a real name"""
    return (_KIND.get((kind_cell or "").split(":")[0], 0) * 10 + _GRADE.get(email_type or "", 0) + (0 if _DOMAIN_ONLY.match((buyer or "").strip()) else 0.5))


def cls(ship_ready, mark):
    m = (mark or "5")[:1]
    return (0 if (ship_ready or "").startswith("yes") else 1, int(m) if m in "12345" else 5)


def main(d):
    t0 = time.time()
    table, lines = os.path.join(d, "ranked_buyers.csv.gz"), os.path.join(d, "ranked_buyers.jsonl.gz")
    if not os.path.exists(table):
        raise SystemExit("no table in %s" % d)
    work = os.path.join(d, "_priority")
    shutil.rmtree(work, ignore_errors=True)
    os.makedirs(work)
    has_json = os.path.exists(lines)
    fj = gzip.open(lines, "rt", encoding="utf-8") if has_json else None
    n, bc, bj = collections.Counter(), {}, {}
    parent, owner_of_key, info = {}, {}, {}  # one organisation = the rows its identity keys join (union-find over (class, row number in class))

    def find(a):
        while parent[a] != a:
            parent[a] = parent[parent[a]]
            a = parent[a]
        return a
    with gzip.open(table, "rt", encoding="utf-8", newline="") as f:
        rd = csv.reader(f)
        head = next(rd)
        if "ship_ready" not in head or "amount_mark" not in head:
            print("priority order: the table has no amount_mark column (built by an earlier ranker) — left as it is")
            shutil.rmtree(work, ignore_errors=True)
            return
        i_s, i_m = head.index("ship_ready"), head.index("amount_mark")
        ix = {c: head.index(c) for c in ("buyer", "email", "buyer_website", "buyer_address", "keys", "relationship_kind", "email_type", "invoice_fields_for_kind") if c in head}
        g = lambda row, c: row[ix[c]] if c in ix and ix[c] < len(row) else ""
        for row in rd:
            k = cls(row[i_s], row[i_m])
            rid = (k, n[k])
            parent[rid] = rid
            info[rid] = (row_score(g(row, "email_type"), g(row, "invoice_fields_for_kind"), g(row, "buyer")), g(row, "buyer"), g(row, "email"), g(row, "keys"))
            for kk in identity_keys(g(row, "buyer"), g(row, "email"), g(row, "buyer_website"), g(row, "buyer_address")):
                o = owner_of_key.get(kk)
                if o is None:
                    owner_of_key[kk] = rid
                else:
                    ra, rb = find(o), find(rid)
                    if ra != rb:
                        parent[rb] = ra
                    info[rid] = info[rid] + (kk[0],) if len(info[rid]) == 4 else info[rid]
            if k not in bc:
                fo = gzip.open(os.path.join(work, "c_%d_%d.csv.gz" % k), "wt", encoding="utf-8", newline="", compresslevel=1)
                bc[k] = (fo, csv.writer(fo))
                if has_json:
                    bj[k] = gzip.open(os.path.join(work, "j_%d_%d.jsonl.gz" % k), "wt", encoding="utf-8", compresslevel=1)
            bc[k][1].writerow(row)
            if has_json:
                l = fj.readline()
                if not l:
                    raise SystemExit("priority order: the JSON-lines copy has fewer rows than the table — nothing changed")
                bj[k].write(l)
            n[k] += 1
    if has_json:
        if fj.readline():
            raise SystemExit("priority order: the JSON-lines copy has more rows than the table — nothing changed")
        fj.close()
    for fo, _ in bc.values():
        fo.close()
    for fo in bj.values():
        fo.close()
    order = sorted(bc)
    tmp = table + ".sorted"
    # the row each organisation keeps: the best class of priority (ready first, then by amount), then the stronger relationship and the
    # better mailbox, then the ranker's own order
    best = {}
    for rid in parent:
        r = find(rid)
        key = (rid[0], -info[rid][0], rid[1])
        if r not in best or key < best[r][0]:
            best[r] = (key, rid)
    keep = {v[1] for v in best.values()}
    dropped = collections.Counter()
    fd = open(os.path.join(d, "duplicate_buyers_dropped.csv"), "w", encoding="utf-8", newline="")
    wd = csv.writer(fd)
    wd.writerow(["matched_by", "kept_buyer", "kept_email", "kept_keys", "dropped_buyer", "dropped_email", "dropped_website", "dropped_address", "dropped_keys", "dropped_relationship"])
    tmpj = lines + ".sorted"
    fjo = gzip.open(tmpj, "wt", encoding="utf-8", compresslevel=6) if has_json else None
    with gzip.open(tmp, "wt", encoding="utf-8", newline="", compresslevel=6) as fo:
        wr = csv.writer(fo)
        wr.writerow(head)
        for k in order:
            fj2 = gzip.open(os.path.join(work, "j_%d_%d.jsonl.gz" % k), "rt", encoding="utf-8") if has_json else None
            with gzip.open(os.path.join(work, "c_%d_%d.csv.gz" % k), "rt", encoding="utf-8", newline="") as fi:
                for i, row in enumerate(csv.reader(fi)):
                    jl = fj2.readline() if fj2 else ""
                    rid = (k, i)
                    if rid not in keep:
                        w = best[find(rid)][1]
                        kept = info[w]
                        dropped[(info[rid][4] if len(info[rid]) > 4 else "joined through another row", "ready" if k[0] == 0 else "not ready")] += 1
                        wd.writerow([info[rid][4] if len(info[rid]) > 4 else "joined through another row", kept[1], kept[2], kept[3], g(row, "buyer"), g(row, "email"),
                                     g(row, "buyer_website"), g(row, "buyer_address")[:200], g(row, "keys"), g(row, "relationship_kind")[:120]])
                        continue
                    wr.writerow(row)
                    if fjo:
                        fjo.write(jl)
            if fj2:
                fj2.close()
    fd.close()
    if fjo:
        fjo.close()
        os.replace(tmpj, lines)
    os.replace(tmp, table)
    for rid in parent:
        if rid not in keep:
            n[rid[0]] -= 1
    print("one row per organisation: rows of an organisation that has a better row, left out (it keeps the best class, then the stronger relationship and the better mailbox): %d — %s "
          "(out/ranked/duplicate_buyers_dropped.csv lists each)" % (sum(dropped.values()), dict(sorted(dropped.items()))))
    shutil.rmtree(work, ignore_errors=True)
    name = {1: "published, $5,000 or more", 2: "estimated, $5,000 or more", 3: "published, under $5,000", 4: "estimated, under $5,000", 5: "no amount"}
    print("priority order (rows that meet the test first, then by amount): %s — %d rows in %d s" % (
        " · ".join("%s, %s: %d" % ("ready" if k[0] == 0 else "not ready", name[k[1]], n[k]) for k in order), sum(n.values()), time.time() - t0))


if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else "out/ranked")
