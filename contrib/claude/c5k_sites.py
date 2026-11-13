#!/usr/bin/env python3
"""The $5,000+ rows held back for want of a mailbox and with no website on file: the organisation's own site, found the way the register lanes
find a holder's (tools/hc_registers.py): the company-name autocomplete (Clearbit) proposes a domain under the organisation's very name (legal forms
and accents aside), the domain fits the name and the country, and the site's own home page carries the name. Nothing else is taken.

  python3 contrib/claude/c5k_sites.py ranked_buyers.csv.gz [--minutes 30] [--threads 6]  -> data/incoming/claude/cb_sites_cb.csv (key, name, site, tied_by)

rank.py loads the file beside cb_sites_wd.csv; contrib/claude/c5k_mailboxes.py --sites reads the sites for a role mailbox.
"""
import argparse, csv, gzip, os, queue, re, sys, threading, time

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "../.."))
sys.path.insert(0, os.path.join(ROOT, "tools"))
import hc_registers as HR  # noqa: E402

csv.field_size_limit(1 << 30)
OUT = os.path.join(ROOT, "data/incoming/claude/cb_sites_cb.csv")
COUNTRY = {"US": "united states", "UK": "united kingdom", "EU": ""}


_CA_MARK = re.compile(r"\b(?:canada|qu[ée]bec|ontario|british columbia|alberta|manitoba|saskatchewan|nova scotia|new brunswick|newfoundland|prince edward island|"
                      r"yukon|nunavut|northwest territories)\b|\b[ABCEGHJ-NPRSTVXY]\d[A-Z]\s?\d[A-Z]\d\b", re.I)


def canadian_page(d):
    import client_lists as CL
    u = "https://%s/" % d
    if not CL.allowed(u):
        return False
    page, _ = CL.fetch(u)
    return bool(page and _CA_MARK.search(re.sub(r"<[^>]+>", " ", page)))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("ranked")
    ap.add_argument("--minutes", type=float, default=30)
    ap.add_argument("--threads", type=int, default=6)
    a = ap.parse_args()
    have = {}
    if os.path.exists(OUT):
        have = {r["key"]: r for r in csv.DictReader(open(OUT, encoding="utf-8"))}
    todo, seen = [], set()
    with gzip.open(a.ranked, "rt", encoding="utf-8", errors="replace") as fh:
        for x in csv.DictReader(fh):
            if (x.get("amount_mark") or "5")[:1] not in "12" or (x.get("ship_ready") or "").startswith("yes"):
                continue
            if "no mailbox" not in (x.get("ship_ready_missing") or "") or (x.get("buyer_website") or "").strip():
                continue
            key = next((k for k in (x.get("keys") or "").split("|") if k.startswith("b:")), "")
            name = re.sub(r"\s*\((?:[^()]*)\)\s*$", "", (x.get("buyer") or "").strip()).strip(" .")
            if not key or key in have or name.lower() in seen:
                continue
            seen.add(name.lower())
            j = (x.get("jurisdiction") or "")[:2]
            todo.append((key, name, "canada" if j not in COUNTRY else COUNTRY[j]))
    print("%d organisations with no website on file" % len(todo), flush=True)
    t_end = time.time() + 60 * a.minutes
    q, lock, cnt = queue.Queue(maxsize=32), threading.Lock(), {"looked up": 0, "found": 0}
    new = not os.path.exists(OUT)
    f = open(OUT, "a", newline="", encoding="utf-8")
    w = csv.DictWriter(f, fieldnames=["key", "name", "site", "tied_by"])
    if new:
        w.writeheader()

    def producer():
        for key, name, country in todo:
            if time.time() > t_end:
                break
            n = HR.core(name)
            if len(n) < 3 or (len(n.split()) == 1 and len(n) < 5):
                continue
            cands = [((s.get("domain") or "").lower().strip(), HR.core(s.get("name") or "")) for s in (HR.suggest(n) or [])[:5]]
            doms = [d for d, sn in cands if d and not HR.BAD.search(d) and sn == n and (not country or HR.domain_fits(d, n, country))]
            with lock:
                cnt["looked up"] += 1
            if doms:
                q.put((key, name, n, doms))
        for _ in range(a.threads):
            q.put(None)

    def worker():
        while True:
            it = q.get()
            if it is None:
                return
            key, name, n, doms = it
            for d in doms:
                try:
                    said = HR.home_says(d, n)
                except Exception:
                    said = ""
                if said and country == "canada" and not d.endswith(".ca") and not canadian_page(d):
                    said = ""  # 2026-11-13: "Valoris" took a Belgrade employment agency's valoris.org, "NL Housing" a Dutch room-rental site: a site that is not
                    # a .ca must print a Canadian province or postal code on its home page
                    with lock:
                        w.writerow({"key": key, "name": name, "site": "https://%s/" % d,
                                    "tied_by": "the company-name autocomplete (Clearbit) proposes %s under the organisation's very name (%s, legal forms aside), and the site's own home page carries it: “%s”" % (d, n, said[:200])})
                        f.flush()
                        cnt["found"] += 1
                    break

    ts = [threading.Thread(target=worker, daemon=True) for _ in range(a.threads)]
    for t in ts:
        t.start()
    producer()
    for t in ts:
        t.join()
    f.close()
    print("done:", cnt, "->", OUT, flush=True)


if __name__ == "__main__":
    main()
