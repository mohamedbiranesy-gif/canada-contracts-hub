#!/usr/bin/env python3
"""Builds the search-worker queue (tools/api_search_worker.py) from the ranked file: the pages an invoice still needs, best packages first.
  af: buyer–vendor pairs (packages P01–P05, P09) whose proof record lacks value, dates or numbers → the buyer's own award page
  pc: delivered buyers (tiers A,B,T,M,L,C,D,E,F) with a website but no published payment terms or PO rule → AP / PO-terms pages
  vw: vendors (named, not inferred) without a website → candidate site
  pb: public-body buyers of P01–P05 still lacking payment terms or a PO rule after the pc pass → purchasing bylaw / procurement policy / PO terms, on the
      buyer's host or its council / board document portal (eSCRIBE, CivicWeb, Legistar, BoardDocs, Granicus, iCompass …) — the buyer's own documents
  python3 tools/api_queue.py --ranked ~/cch-tasks/ranked_latest.csv.gz --out ~/cch-tasks/apiq/queue.tsv [--max-af 3000 --max-pc 6000 --max-vw 4000]
"""
import argparse, csv, gzip, re, urllib.parse

csv.field_size_limit(1 << 30)
EMPTY = re.compile(r"^(?:$|not_published$|not_found_yet$|no |none\b|not |0 in the|only system|n/a\b|not applicable|unknown\b|aucun|no dataset|no record|no identifier)", re.I)
PRIO = {"GOLD": 0, "GOLD-T": 1, "GOLD-M": 1, "A1": 2, "B1": 2, "A2": 3, "B2": 3, "A3": 4, "B3": 4, "L1": 5, "T1": 5, "M1": 5}


def filled(v):
    return not EMPTY.match((v or "").strip())


def host(u):
    h = (urllib.parse.urlparse(u if "//" in (u or "") else "https://" + (u or "")).hostname or "").lower()
    return h[4:] if h.startswith("www.") else h


def main():
    a = argparse.ArgumentParser()
    a.add_argument("--ranked", required=True)
    a.add_argument("--out", required=True)
    a.add_argument("--max-af", type=int, default=4000)
    a.add_argument("--max-pc", type=int, default=6000)
    a.add_argument("--max-vw", type=int, default=4000)
    a.add_argument("--max-pb", type=int, default=3000)
    a = a.parse_args()
    af, pc, vw, pb, seen = [], [], [], [], set()
    PUBLIC = re.compile(r"municipal|city|town|village|county|region|district|township|school|scolaire|college|c[ée]gep|universit|hospital|health|sant[ée]|ciusss|cisss|government|ministry|agency|authority|commission|board|library|transit|police|fire|first nation|band|conseil|ville|municipalit", re.I)
    op = gzip.open if a.ranked.endswith(".gz") else open
    with op(a.ranked, "rt", encoding="utf-8", newline="") as f:
        for r in csv.DictReader(f):
            if not r.get("email"):
                continue
            rg, tier = r.get("rank_group") or "", r.get("tier") or ""
            pr = PRIO.get(rg, 6 if tier in ("A", "B", "L", "T", "M") else 8 if tier in ("C", "D", "E", "F") else 9)
            bk = (r.get("keys") or "").split("|")[0]
            h = host(r.get("buyer_website") or "")
            v = (r.get("vendor") or "").strip()
            if h and bk:
                lacking = (not filled(r.get("contract_value")) or (not filled(r.get("start_date")) and not filled(r.get("end_date"))) or (not filled(r.get("po_number_as_published")) and not filled(r.get("contract_or_agreement_number"))))
                if v and not v.startswith("inferred") and lacking and (tier in ("A", "B", "L") or rg in ("GOLD-T", "GOLD-M") or tier in ("T", "M", "C")):
                    k = ("af", bk, v)
                    if k not in seen:  # client-listing / older-record pairs (P06, P07, P09) get the award-page search too — a buyer's own award report is the only place their contract facts can come from
                        seen.add(k); af.append((pr if tier in ("A", "B", "L") else pr + 3, {"task_id": "af:%s||%s" % (bk, v), "kind": "af", "key": "%s||%s" % (bk, v), "name": v, "host": h, "extra": bk}))
                if tier in ("A", "B", "T", "M", "L", "C", "D", "E", "F") and (not filled(r.get("payment_terms_as_published")) or not filled(r.get("po_required_as_published"))) and ("pc", bk) not in seen:
                    seen.add(("pc", bk)); pc.append((pr, {"task_id": "pc:" + bk, "kind": "pc", "key": bk, "name": r.get("buyer") or "", "host": h, "extra": r.get("buyer_type") or ""}))
                if tier in ("A", "B", "L") and (not filled(r.get("payment_terms_as_published")) or not filled(r.get("po_required_as_published"))) and ("pb", bk) not in seen and PUBLIC.search((r.get("buyer_type") or "") + " " + (r.get("buyer") or "")):
                    seen.add(("pb", bk)); pb.append((pr, {"task_id": "pb:" + bk, "kind": "pb", "key": bk, "name": r.get("buyer") or "", "host": h, "extra": r.get("buyer_type") or ""}))
            if v and not v.startswith("inferred") and not filled(r.get("vendor_website")) and ("vw", v.lower()) not in seen:
                seen.add(("vw", v.lower())); vw.append((pr, {"task_id": "vw:" + v.lower()[:80], "kind": "vw", "key": v, "name": v, "host": "", "extra": (r.get("vendor_address") or "")[:80]}))
    rows = []
    for lst, mx in ((af, a.max_af), (pc, a.max_pc), (vw, a.max_vw), (pb, a.max_pb)):
        lst.sort(key=lambda t: t[0])
        rows += [((t[0] + 10) if t[1]["kind"] == "af" else t[0], {"af": 3, "pc": 0, "pb": 1, "vw": 2}[t[1]["kind"]], t[1]) for t in lst[:mx]]
    rows.sort(key=lambda t: (t[0], t[1]))  # AP / PO-terms pages and vendor sites of every package first; award pages (contract value, PO number: ~7 % yield) last — owner 2026-11-08 14:50 EST: don't burn the credits on PO numbers
    rows = [t[2] for t in rows]
    clean = lambda v: re.sub(r"[\t\r\n]+", " ", str(v or ""))[:200]
    with open(a.out, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=["task_id", "kind", "key", "name", "host", "extra"], delimiter="\t"); w.writeheader()
        for t in rows:
            w.writerow({k: clean(v) for k, v in t.items()})
    print("queue: af %d, pc %d, pb %d, vw %d → %s" % (min(len(af), a.max_af), min(len(pc), a.max_pc), min(len(pb), a.max_pb), min(len(vw), a.max_vw), a.out))


if __name__ == "__main__":
    main()
