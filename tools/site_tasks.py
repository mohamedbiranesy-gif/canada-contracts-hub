#!/usr/bin/env python3
"""Task list for the site readers (tools/org_contacts.py, tools/org_extras.py): every delivered buyer's and vendor's website from the
ranked deliverable, one line per registrable domain, strongest packages first, so the readers fill the rows that matter most first.

  python3 tools/site_tasks.py --ranked ~/cch-tasks/ranked_latest.csv.gz --out ~/cch-tasks/site_tasks.csv [--kind buyer|vendor|both]
Prints how many domains the two readers have not read yet (their resume files in ~/cch-crawler-state).
"""
import argparse, csv, gzip, json, os, sys, urllib.parse

csv.field_size_limit(1 << 30)
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import ap_crawler as C  # registrable()

STATE = os.path.expanduser("~/cch-crawler-state")


def prio(r):
    rg, t, g = r.get("rank_group") or "", r.get("tier") or "", r.get("grade") or ""
    if rg == "GOLD":
        return 0
    if rg in ("GOLD-T", "GOLD-M"):
        return 2
    if t in ("A", "B"):
        return 1 if g in ("3", "2") else 3
    if t == "L":
        return 3
    if t in ("T", "M", "C", "D", "E"):
        return 4
    if t == "I":
        return 6
    return 5


def host_of(w):
    w = (w or "").strip()
    if not w:
        return ""
    h = (urllib.parse.urlparse(w if "//" in w else "https://" + w).hostname or "").lower()
    return h[4:] if h.startswith("www.") else h


def main():
    a = argparse.ArgumentParser()
    a.add_argument("--ranked", default=os.path.expanduser("~/cch-tasks/ranked_latest.csv.gz"))
    a.add_argument("--out", default=os.path.expanduser("~/cch-tasks/site_tasks.csv"))
    a.add_argument("--kind", default="both")
    a = a.parse_args()
    op = gzip.open if a.ranked.endswith(".gz") else open
    seen, tasks = {}, []
    with op(a.ranked, "rt", encoding="utf-8", newline="") as fh:
        for r in csv.DictReader(fh):
            if not r.get("email"):
                continue  # Z rows are not delivered
            p = prio(r)
            cands = []
            if a.kind in ("both", "buyer"):
                cands.append(("buyer", r.get("buyer_website"), (r.get("keys") or "").split("|")[0], r.get("buyer")))
            if a.kind in ("both", "vendor") and not (r.get("vendor") or "").startswith("inferred"):
                cands.append(("vendor", r.get("vendor_website"), "vendor:" + (r.get("vendor") or "")[:80], r.get("vendor")))
            for kind, w, key, name in cands:
                h = host_of(w)
                if not h or "." not in h:
                    continue
                dom = C.registrable(h)
                if dom in seen:
                    continue
                seen[dom] = p + (0.5 if kind == "vendor" else 0)
                tasks.append((seen[dom], dom, {"website": "https://%s/" % h, "key": key, "name": name, "kind": kind}))
    tasks.sort(key=lambda t: t[0])
    with open(a.out, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=["website", "key", "name", "kind"]); w.writeheader()
        for _, _, t in tasks:
            w.writerow(t)
    done = {}
    for fn in ("org_contacts.jsonl", "org_extras.jsonl"):
        s = set()
        pth = os.path.join(STATE, fn)
        if os.path.exists(pth):
            for l in open(pth, encoding="utf-8"):
                try:
                    s.add(json.loads(l).get("domain"))
                except Exception:
                    pass
        done[fn] = s
    print("domains:", len(tasks), "| by priority:", {p: sum(1 for t in tasks if int(t[0]) == p) for p in range(7)})
    for fn, s in done.items():
        new = [t for t in tasks if t[1] not in s]
        print("%s: %d read before; %d not read yet (priority 0-1: %d)" % (fn, len(s), len(new), sum(1 for t in new if t[0] < 2)))
    print("wrote", a.out)


if __name__ == "__main__":
    main()
