#!/usr/bin/env python3
"""One legal person, two Canadian registers: a site the patent lane tied to an owner is that owner's site in the trademark lane too, and the reverse.

The Canadian patents register and the Canadian trademarks register name the same companies (3D Systems, Inc.; ADC Therapeutics SA …), each with
its address, and each lane looks for the owner's site by itself (tools/tm_register.py sites, tools/pt_register.py). When one lane has tied a site
to an owner by its own tests (the site's own pages state the owner's name with the register's postal code, or its full legal name with its legal
form), an owner of the other register with the SAME legal name (legal form included, compared without case, accents or punctuation), in the
SAME country and at the SAME postal code (U.S.: the ZIP code; where neither register gives a postal code: the same address) is the same legal
person, and the site is its site. Kept only when that name, country and postal code lead to one site, when the owner has no site of its own in
its lane yet, and when no other owner of its lane holds that site. Nothing is fetched.

  python3 tools/cross_sites.py        appends the ties to data/incoming/claude/tm/tm_sites_found.csv and data/incoming/claude/pt/pt_sites_found.csv
"""
import collections, csv, gzip, os, re, sys, time, unicodedata

csv.field_size_limit(1 << 30)
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
INC = os.path.join(ROOT, "data/incoming/claude")
LANES = {"tm": ("trademark", [os.path.join(INC, "tm/tm_owners_abroad.csv.gz"), os.path.join(INC, "tm/tm_owners_ca.csv.gz")], os.path.join(INC, "tm/tm_sites_found.csv")),
         "pt": ("patent", [os.path.join(INC, "pt/pt_owners_abroad.csv.gz"), os.path.join(INC, "pt/pt_owners_ca.csv.gz")], os.path.join(INC, "pt/pt_sites_found.csv"))}
TODAY = time.strftime("%Y-%m-%d")


def norm(s):
    s = unicodedata.normalize("NFKD", s or "").encode("ascii", "ignore").decode().lower().replace("&", " and ")
    return re.sub(r"[^a-z0-9]+", " ", s).strip()


def place_key(r):
    c = (r.get("country") or "CA").strip().upper()
    pc = re.sub(r"[^A-Z0-9]", "", (r.get("postal_code") or "").upper())
    if not pc and c == "US":
        m = re.search(r"\b(\d{5})(?:-\d{4})?\s*$", r.get("address") or "")
        pc = m.group(1) if m else ""
    if c == "US":
        pc = pc[:5]
    return c, (pc or ("addr:" + norm(r.get("address") or "")))


def owners(paths):
    out = {}
    for p in paths:
        if not os.path.exists(p):
            continue
        with gzip.open(p, "rt", encoding="utf-8", errors="replace") as f:
            for r in csv.DictReader(f):
                n = norm(r.get("owner_name"))
                if n and len(n) >= 4:
                    c, pk = place_key(r)
                    out[r["owner_key"]] = (n, c, pk, r.get("owner_name") or "", r.get("postal_code") or "")
    return out


def read_found(path):
    with open(path, encoding="utf-8", newline="") as f:
        rd = csv.DictReader(f)
        return rd.fieldnames, list(rd)


def main():
    own = {k: owners(v[1]) for k, v in LANES.items()}
    found = {}
    for k, v in LANES.items():
        found[k] = read_found(v[2])
    by_owner = {k: {r["owner_key"]: r for r in found[k][1] if r.get("owner_key")} for k in LANES}
    sites_held = {k: {r["site"] for r in found[k][1]} for k in LANES}
    for tgt, src in (("tm", "pt"), ("pt", "tm")):
        ix = collections.defaultdict(dict)
        for ok, r in by_owner[src].items():
            o = own[src].get(ok)
            if o:
                ix[o[:3]][r["site"]] = r
        cols, rows = found[tgt]
        add, used = [], set()
        for ok, o in own[tgt].items():
            if ok in by_owner[tgt]:
                continue
            hits = ix.get(o[:3]) or {}
            if len(hits) != 1:
                continue
            site, r = next(iter(hits.items()))
            if site in sites_held[tgt] or site in used:
                continue
            used.add(site)
            where = ("postal code %s" % o[4]) if o[4] else ("ZIP code %s" % o[2]) if o[1] == "US" and not o[2].startswith("addr:") else "the same address"
            tied = ("the same legal person on both Canadian registers (“%s”, %s, %s): the %s lane tied this site to it — %s"
                    % (o[3], o[1], where, LANES[src][0], r.get("tied_by") or ""))[:600]
            line = {c: "" for c in cols}
            line.update(site=site, owner_key=ok, owner_name=o[3], postal_code=o[4], tied_by=tied, site_facts_from=r.get("site_facts_from") or "",
                        site_states=r.get("site_states") or "", read=r.get("read") or TODAY)
            add.append(line)
        if add:
            with open(LANES[tgt][2], "a", encoding="utf-8", newline="") as f:
                w = csv.DictWriter(f, fieldnames=cols)
                for line in add:
                    w.writerow(line)
        print("cross-sites: %d %s owners tied to the site the %s lane tied to the same legal person" % (len(add), LANES[tgt][0], LANES[src][0]))


# ---------------------------------------------------------------------------------------------------- sites already read -> owners abroad
# 2026-11-13: the mailbox reader has read some 56,000 sites that print an address abroad (U.S., U.K., Australia). A trademark or patent owner abroad
# with no site in its lane whose register ZIP / postcode is printed in an address on such a site, under the owner's own name (the site's own name
# states the owner's name, legal form aside, or is two words or more of it), is tied by the lane's own test ("the same name and the same ZIP code
# printed in an address on the site"). Only one owner a site and one site an owner; a site another owner of the lane holds is left.
def _zipk(c, text):
    text = text or ""
    if c == "US":
        m = re.findall(r"\b(\d{5})(?:-\d{4})?\b", text)
        return m[-1] if m else ""
    if c == "GB":
        m = re.findall(r"\b([A-Z]{1,2}\d[A-Z\d]?\s?\d[A-Z]{2})\b", text.upper())
        return re.sub(r"\s", "", m[-1]) if m else ""
    if c == "AU":
        m = re.findall(r"\b(\d{4})\b", text)
        return m[-1] if m else ""
    return ""


def read_sites():
    import glob, json
    sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
    import biz_licences as BL
    import tm_register as T
    found = set()
    for p in sorted(glob.glob(os.path.join(INC, "claude_buyer_ap_results_cccrawl*.csv"))):
        with open(p, encoding="utf-8", errors="replace", newline="") as f:
            for r in csv.DictReader(f):
                if r.get("status") == "found" and r.get("ap_email"):
                    found.add(r["buyer_key"])
    facts = {}
    for p in glob.glob(os.path.join(INC, "site_facts", "facts_*.gz")):
        with gzip.open(p, "rt", encoding="utf-8", errors="replace") as f:
            for l in f:
                try:
                    d = json.loads(l)
                except ValueError:
                    continue
                k = d.get("key")
                if k in found:
                    o = facts.setdefault(k, {})
                    for c_, v_ in d.items():
                        if v_ and not o.get(c_):
                            o[c_] = v_
    toks = lambda s: set(T.nkey_x(s or "").split()) - {"a", "an", "the", "and", "of", "dba", "d", "b"}
    for lane, (word, paths, fpath) in LANES.items():
        cols, rows = read_found(fpath)
        held_site, held_owner = {r["site"] for r in rows}, {r["owner_key"] for r in rows}
        own = collections.defaultdict(list)
        for p in paths:
            if not os.path.exists(p):
                continue
            with gzip.open(p, "rt", encoding="utf-8", errors="replace") as f:
                for r in csv.DictReader(f):
                    c = r.get("country") or ""
                    z = _zipk(c, (r.get("postal_code") or "") + " " + (r.get("address") or "")) if c in ("US", "GB", "AU") else ""
                    if z and r["owner_key"] not in held_owner:
                        own[(c, z)].append(r)
        cand = collections.defaultdict(set)
        info = {}
        for k, o in facts.items():
            c = o.get("address_country") or ""
            if c not in ("US", "GB", "AU"):
                continue
            z = _zipk(c, o.get("address") or o.get("address_quote"))
            nm = o.get("site_name") or ""
            if not z or not nm:
                continue
            dom = re.sub(r"^https?://(www\.)?", "", o.get("site") or "").split("/")[0].lower()
            if not dom or dom in held_site:
                continue
            ts = toks(nm)
            for r in own.get((c, z), []):
                to = toks(r["owner_name"])
                if to and ts and BL.names_agree(nm, r["owner_name"]) and (to <= ts or (len(ts) >= 2 and ts <= to)):
                    cand[("s", dom)].add(r["owner_key"]); cand[("o", r["owner_key"])].add(dom)
                    info[(r["owner_key"], dom)] = (r, o, nm)
        add = []
        for (ok, dom), (r, o, nm) in sorted(info.items()):
            if len(cand[("s", dom)]) != 1 or len(cand[("o", ok)]) != 1 or dom in held_site or ok in held_owner:
                continue
            zw = "ZIP code" if r.get("country") == "US" else "postcode"
            line = {c: "" for c in cols}
            line.update(site=dom, owner_key=ok, owner_name=r["owner_name"], postal_code=r.get("postal_code") or "",
                        tied_by=("the same name (the site's own name “%s”) and the owner's %s printed in an address on the site's own page (%s: “%s”) — a site the mailbox "
                                 "reader had read for its role mailbox; one owner of the register at that %s with that name" % (nm, zw, o.get("address_url") or o.get("site") or "",
                                 (o.get("address_quote") or o.get("address") or "")[:200], zw))[:700],
                        site_facts_from="its own pages (%s), read by the mailbox reader (tools/lead_crawl.py)" % (o.get("site") or dom),
                        site_states="site name: %s" % nm, read=o.get("date") or TODAY)
            add.append(line); held_site.add(dom); held_owner.add(ok)
        if add:
            with open(fpath, "a", encoding="utf-8", newline="") as f:
                w = csv.DictWriter(f, fieldnames=cols)
                for line in add:
                    w.writerow(line)
        print("cross-sites: %d %s owners abroad tied to a site the mailbox reader had read (same name + the register's ZIP / postcode printed)" % (len(add), word))


if __name__ == "__main__":
    main()
    if "--no-read" not in sys.argv:
        read_sites()
