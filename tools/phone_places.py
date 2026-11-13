#!/usr/bin/env python3
"""Where an organisation is, by its telephone number: the Overture Maps place that lists the number the organisation prints (no AI).

The rows that stand on where the organisation is (tools/by_location.py) need its address. 136,177 mailbox owners under a .ca name print no postal
code the reader saw (rank build 2026-11-13 04:08Z); 77,187 of the 207,671 organisations left unlocated print a Canadian telephone number beside
their mailbox or on their contact page. A business listing (Overture Maps: open data from Meta, Microsoft, Foursquare … places) carries the
telephone number of the place and its address. When the place that lists the organisation's own telephone number also bears the organisation's
name, the place's address is where the organisation is — a public places dataset's statement, said so on the row ("the address of the Overture
Maps place that lists its telephone number"), never mixed with an address the organisation printed itself.

Kept only when: the number is a Canadian geographic number (not toll-free), printed by at most three of our organisations, listed by places that
all print ONE postal code — or, among them, by places that bear the organisation's name and print one postal code; the place's name agrees with the
organisation's (every word of the shorter name in the longer one, or the very same name), or the place lists the organisation's own website.

  targets              -> out/phone_targets.csv (key, phone, site, name): unlocated organisations with a confirmed mailbox and a Canadian number
  query [--files N]    -> out/phone_places_raw.csv: the Overture places in Canada whose number is one of the targets'
  pick                 -> data/incoming/claude/overture/phone_places.csv (one line per organisation located)
"""
import argparse, collections, csv, glob, gzip, json, os, re, sys, time, urllib.request

csv.field_size_limit(1 << 30)
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
INC = os.path.join(ROOT, "data/incoming/claude")
OUT = os.path.join(INC, "overture", "phone_places.csv")
BUCKET = "https://overturemaps-us-west-2.s3.amazonaws.com"
UA = "canada-contracts-hub-crawler/1.0 (+https://github.com/mohamedbiranesy-gif/canada-contracts-hub)"
PH = re.compile(r"(?<!\d)(?:\+?1[\s.\-]?)?\(?([2-9]\d{2})\)?[\s.\-]?([2-9]\d{2})[\s.\-]?(\d{4})(?!\d)")
CA_AC = set("204 226 236 249 250 257 263 289 306 343 354 365 367 368 382 403 416 418 428 431 437 438 450 468 474 506 514 519 548 579 581 584 587 604 613 639 "
            "647 672 683 705 709 742 753 778 780 782 807 819 825 867 873 879 902 905".split())
COLS = ["key", "phone", "dom", "place_id", "names", "street", "city", "province", "postcode", "website", "release", "how"]


def host(u):
    h = re.sub(r"^https?://", "", (u or "").strip().lower()).split("/")[0].split(":")[0]
    return h[4:] if h.startswith("www.") else h


def cmd_targets(a):
    import addr_reread as AR
    # every organisation with a confirmed mailbox still unlocated — also the ones the address re-read has read without finding an address
    # (2026-11-13 06:48Z: without them the targets fell from 77,187 to 131 once the re-read had marked its sites done)
    AR.cmd_pick(argparse.Namespace(out="out/addr_targets_phone.csv", include_done=True))
    tg = {r["key"]: r["site"] for r in csv.DictReader(open("out/addr_targets_phone.csv", encoding="utf-8"))}
    ph, name = {}, {}
    for p in sorted(glob.glob(os.path.join(INC, "claude_buyer_ap_results_cccrawl*.csv"))):
        with open(p, encoding="utf-8", errors="replace", newline="") as f:
            for r in csv.DictReader(f):
                k = r["buyer_key"]
                if k in tg and k not in ph:
                    for m in PH.finditer((r.get("evidence_quote") or "") + " " + (r.get("ap_phone") or "")):
                        if m.group(1) in CA_AC:
                            ph[k] = m.group(1) + m.group(2) + m.group(3)
                            break
                    if r.get("org_name_as_found"):
                        name.setdefault(k, r["org_name_as_found"])
    dom_ph = {}
    p = os.path.join(INC, "claude_org_contacts.jsonl.gz")
    if os.path.exists(p):
        with gzip.open(p, "rt", encoding="utf-8", errors="replace") as f:
            for l in f:
                try:
                    d = json.loads(l)
                except ValueError:
                    continue
                dg = re.sub(r"\D", "", d.get("phone") or "")[-10:]
                if len(dg) == 10 and dg[:3] in CA_AC:
                    dom_ph.setdefault(host(d.get("website")), (dg, d.get("name") or ""))
    # the numbers the address re-read kept from the organisations' own pages (tools/addr_reread.py: a tel: link first)
    pp = os.path.join(INC, "site_facts", "phones.tsv")
    if os.path.exists(pp):
        with open(pp, encoding="utf-8") as f:
            for l in f:
                p_ = l.rstrip("\n").split("\t")
                if len(p_) >= 2 and p_[0] in tg and p_[0] not in ph and len(p_[1]) == 10:
                    ph[p_[0]] = p_[1]
    for k, s in tg.items():
        if k not in ph and host(s) in dom_ph:
            ph[k] = dom_ph[host(s)][0]
            name.setdefault(k, dom_ph[host(s)][1])
    for p in sorted(glob.glob(os.path.join(INC, "site_facts", "facts_*.gz"))):
        with gzip.open(p, "rt", encoding="utf-8", errors="replace") as f:
            for l in f:
                try:
                    d = json.loads(l)
                except ValueError:
                    continue
                if d.get("key") in tg and d.get("phone") and d["key"] not in ph and len(d["phone"]) == 10:
                    ph[d["key"]] = d["phone"]  # the tel: link the mailbox reader saw on the organisation's own page
                if d.get("key") in tg and d.get("site_name"):
                    name[d["key"]] = d["site_name"]
    cnt = collections.Counter(ph.values())
    os.makedirs("out", exist_ok=True)
    n = 0
    with open("out/phone_targets.csv", "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["key", "phone", "site", "name"])
        for k, v in sorted(ph.items()):
            if cnt[v] <= 3:
                w.writerow([k, v, tg[k], name.get(k, "")])
                n += 1
    print("phone targets: %d unlocated organisations with a Canadian number (%d numbers shared by more than three left out)" % (n, sum(1 for v in cnt.values() if v > 3)))


def cmd_query(a):
    import duckdb
    phones = sorted({r["phone"] for r in csv.DictReader(open("out/phone_targets.csv", encoding="utf-8"))})
    ls = lambda prefix: urllib.request.urlopen(urllib.request.Request("%s/?list-type=2&prefix=%s&delimiter=/" % (BUCKET, prefix), headers={"User-Agent": UA}), timeout=120).read().decode()
    rel = sorted(re.findall(r"<Prefix>(release/[0-9]{4}-[0-9]{2}-[0-9]{2}\.[0-9]+/)</Prefix>", ls("release/")))[-1]
    keys = re.findall(r"<Key>([^<]+\.parquet)</Key>", ls(rel + "theme=places/type=place/"))
    if a.files:
        keys = keys[:a.files]
    release = rel.rstrip("/").rsplit("/", 1)[-1]
    con = duckdb.connect()
    con.execute("SET enable_progress_bar=false; INSTALL httpfs; LOAD httpfs; SET memory_limit='3000MB'; SET threads=4;")
    con.execute("CREATE TABLE t (phone VARCHAR)")
    con.executemany("INSERT INTO t VALUES (?)", [(p,) for p in phones])
    src = "read_parquet([%s])" % ", ".join("'%s/%s'" % (BUCKET, k) for k in keys)
    t0 = time.time()
    cur = con.execute(r"""WITH p AS (SELECT id, names."primary" AS name, websites[1] AS website, addresses[1].freeform AS street, addresses[1].locality AS city,
                                            addresses[1].region AS region, addresses[1].postcode AS postcode, phones
                                     FROM %s WHERE bbox.xmin BETWEEN -141.1 AND -52.5 AND bbox.ymin BETWEEN 41.6 AND 84.0
                                       AND addresses[1].country = 'CA' AND phones IS NOT NULL AND len(phones) > 0),
                              q AS (SELECT id, name, website, street, city, region, postcode, right(regexp_replace(ph, '[^0-9]', '', 'g'), 10) AS phone
                                    FROM p, unnest(phones) AS u(ph))
                         SELECT q.* FROM q JOIN t ON t.phone = q.phone""" % src)
    n = 0
    with open("out/phone_places_raw.csv", "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["place_id", "name", "website", "street", "city", "region", "postcode", "phone", "release"])
        while True:
            b = cur.fetchmany(50000)
            if not b:
                break
            for r in b:
                w.writerow(list(r) + [release])
                n += 1
    print("Overture %s: %d place listings carry a target's number (%.0f s, %d files)" % (release, n, time.time() - t0, len(keys)))


def cmd_pick(a):
    import biz_licences as BL
    import by_location as BYL
    import tm_register as T
    tg = list(csv.DictReader(open("out/phone_targets.csv", encoding="utf-8")))
    by_ph = collections.defaultdict(list)
    for r in csv.DictReader(open("out/phone_places_raw.csv", encoding="utf-8")):
        by_ph[r["phone"]].append(r)
    prev = {}
    if os.path.exists(OUT):
        for r in csv.DictReader(open(OUT, encoding="utf-8")):
            prev[r["key"]] = r
    out, why = dict(prev), collections.Counter()
    for t in tg:
        pl = by_ph.get(t["phone"]) or []
        if not pl:
            why["no place lists the number"] += 1
            continue
        dom = host(t["site"])
        nm = t.get("name") or ""

        def agrees(p):
            if host(p.get("website")) and host(p.get("website")) == dom:
                return "website"
            pn = p.get("name") or ""
            if nm and pn and (T.nkey_x(nm) == T.nkey_x(pn) or BL.names_agree(nm, pn)):
                return "name"
            return ""
        good = [(p, agrees(p)) for p in pl]
        good = [(p, h) for p, h in good if h and not BYL.bare_person(p.get("name") or "")]  # (a place named like a person: a person's listing, never kept)
        if not good:
            why["no place with that number bears the organisation's name or lists its website"] += 1
            continue
        pcs = {re.sub(r"[^A-Z0-9]", "", (p.get("postcode") or "").upper()) for p, _ in good}
        pcs.discard("")
        if len(pcs) != 1 or len(next(iter(pcs))) != 6:
            why["places of that name print several postal codes, or none"] += 1
            continue
        pc = next(iter(pcs))
        if not BYL.usable(pc):
            why["not a usable postal code"] += 1
            continue
        p, h = good[0]
        out[t["key"]] = {"key": t["key"], "phone": t["phone"], "dom": dom, "place_id": p["place_id"], "names": p.get("name") or "", "street": p.get("street") or "",
                         "city": p.get("city") or "", "province": p.get("region") or "", "postcode": pc, "website": p.get("website") or "", "release": p.get("release") or "",
                         "how": h}
        why["located"] += 1
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    with open(OUT, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=COLS)
        w.writeheader()
        for k in sorted(out):
            w.writerow({c: out[k].get(c, "") for c in COLS})
    print("phone places: %d organisations located by the place that lists their telephone number (%d on file); %s" % (why["located"], len(out), dict(why)))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("cmd", choices=["targets", "query", "pick"])
    ap.add_argument("--files", type=int, default=0)
    a = ap.parse_args()
    {"targets": cmd_targets, "query": cmd_query, "pick": cmd_pick}[a.cmd](a)


if __name__ == "__main__":
    main()
