#!/usr/bin/env python3
"""Rosters harvested by any lane -> listing leads (2026-11-11).

Owner, 2026-11-11: the lanes are the members of Canadian chambers and associations, the dealers, franchisees and commercial tenants of
Canadian companies, the exhibitors and sponsors of Canadian events — "and more, don't limit yourself". A roster is the list of who pays a
Canadian body, published by that body and current by construction: the body's own roster establishes the relationship
(coord/DECISIONS.md, 2026-11-11 19:24Z). The archive readers and the member-directory reader of this lane find rosters on their own; this
tool takes the ones another lane harvested, so that a lane that "only builds" can add a lane of relationships without touching the ranker.

A lane delivers a roster as two files (data/incoming/** and contrib/** merge without review):

  data/incoming/<lane>/roster_<key>.csv or .csv.gz      one line per listed organisation
      listed_name      the organisation as the roster names it
      listed_website   its own site, as the roster links it (required: the mailbox is read on that site, never taken from the roster)
      listed_address   its address as the roster prints it (optional)
      list_url         the roster page that names it (the page a reader can open to see the name)
      ref              the number the roster gives it — member number, booth, dealer or unit number (optional)

  contrib/<lane>/rosters/<key>.json                      the body, and the proof that it is in Canada and is paid
      kind                   member | dealer | tenant | exhibitor | sponsor
      biller                 the body's name
      biller_site            its own site
      biller_address         its own printed postal address in Canada (with the postal code)
      biller_address_url     the page of its site that prints that address;  biller_address_quote: the sentence, at most 300 characters
      read                   the day those pages were read (YYYY-MM-DD)
      pays_quote, pays_url   the body's own sentence saying the listed party pays it or how it bills (dues, booth fee, rent, invoices), <= 300 chars
      list_hosts, list_host_link_url   (optional) the platforms that keep the body's list (a show's exhibitor list on Map Your Show, a2z …) and
                             the body's own page that links the list there; list_url may then be a page of those hosts
      list_name              how to name the roster in a sentence ("the member directory of the X Chamber of Commerce")

Rules applied here, not left to the harvester: the body's address must carry a Canadian postal code and the quote must contain it; a listed
site must be the organisation's own domain (not a social network, a marketplace, a link shortener, nor the body's own domain); a domain that
more than 15 different bodies list is nobody's particular relationship and is left out; a roster of people is not a roster (the five kinds
only, and a listed name without a site is skipped). A roster's e-mail column, if it has one, is never read.

  python3 tools/roster_ingest.py check            every roster on file: what would be taken, what is left out and why (nothing is written)
  python3 tools/roster_ingest.py merge --stamp S   -> data/incoming/claude/lead_shards/leads_roster_<S>.gz + details_roster_<S>.gz
"""
import argparse, collections, csv, glob, gzip, json, os, re, sys, time

csv.field_size_limit(1 << 30)
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
KINDS = ("member", "dealer", "tenant", "exhibitor", "sponsor")
PC = re.compile(r"(?<![A-Za-z0-9])[ABCEGHJ-NPRSTVXY]\d[ABCEGHJ-NPRSTV-Z][ -]?\d[ABCEGHJ-NPRSTV-Z]\d(?![A-Za-z0-9])")
NOT_OWN = re.compile(r"(?:^|\.)(?:facebook|fb|instagram|linkedin|twitter|x|youtube|youtu|tiktok|pinterest|google|goo|bit|linktr|yelp|tripadvisor|amazon|ebay|etsy|kijiji|"
                     r"wixsite|wordpress|blogspot|weebly|godaddysites|square|shopify|myshopify|canada411|yellowpages|pagesjaunes|eventbrite|zoom|apple|microsoft)\.[a-z.]{2,7}$")
NEED = ("kind", "biller", "biller_site", "biller_address", "biller_address_url", "biller_address_quote", "read", "pays_quote", "pays_url", "list_name")
WHAT = {"member": "members pay it dues", "dealer": "the listed party buys from it", "tenant": "the listed party pays it rent, fees or a levy",
        "exhibitor": "the listed party pays it for its stand", "sponsor": "the listed party pays it a sponsorship"}


def host(u):
    h = re.sub(r"^https?://", "", (u or "").strip().lower()).split("/")[0].split(":")[0].split("?")[0]
    return h[4:] if h.startswith("www.") else h


def _fold(t):
    import unicodedata
    t = re.sub(r"['’`´]", " ", t or "")  # l’Or-et-des-Bois: the article is a word of its own
    return re.sub(r"[^a-z0-9 ]+", " ", unicodedata.normalize("NFKD", t).encode("ascii", "ignore").decode().lower())


_GENERIC_TOK = set("""the and les des inc ltd ltee limited corp corporation company group groupe centre center services service solutions canada quebec ontario
international construction contracting contractors entreprises enterprises de du la le et""".split())


def name_fits_domain(name, dom):
    """the member's own site carries its name: a distinctive word of the listed name (four letters or more) is in the domain's label, or the
    label starts with the name's first word (AGT Robotique at agtrobotics.com), or the label is the initials of the name"""
    label = re.sub(r"[^a-z0-9]", "", dom.split(".")[0].lower())
    name = re.sub(r"(?i)\bs\.?\s?e\.?\s?n\.?\s?c\.?(?:\s?r\.?\s?l\.?)?|\bs\.?\s?r\.?\s?l\.?|\bl\.?\s?l\.?\s?p\.?", " ", name or "")
    toks = [t for t in _fold(name).split() if t]
    if not label or not toks:
        return False
    if any(len(t) >= 4 and t not in _GENERIC_TOK and t in label for t in toks):
        return True
    if len(toks[0]) >= 3 and label.startswith(toks[0]):
        return True
    joined = "".join(toks)
    if len(label) >= 4 and label in joined:  # Ti-Coq at ti-coq.com, S&J Construction at sjconstruction.ca
        return True
    acr = [re.sub(r"[^a-z0-9]", "", m.lower()) for m in re.findall(r"\(([A-Za-z0-9&]{2,8})\)", name or "")]
    if any(len(a_) >= 3 and label.startswith(a_) for a_ in acr):  # Triple Crown Enterprises Ltd. (TCE) at tceont.com
        return True
    small = ("de", "du", "la", "le", "et", "and", "the", "of", "des", "les", "inc", "ltd", "ltee", "l", "d")
    ini = "".join(t[0] for t in toks if t not in small)
    return len(ini) >= 3 and len(label) >= 3 and (label.startswith(ini) or ini.startswith(label))


def rosters():
    """[(descriptor, rows, why not)]"""
    import ap_crawler as C
    out = []
    for jf in sorted(glob.glob(os.path.join(ROOT, "contrib/*/rosters/*.json")) + glob.glob(os.path.join(ROOT, "tools/data/rosters/*.json"))):
        lane = jf.split(os.sep)[-3] if "/contrib/" in jf else "claude"
        try:
            D = json.load(open(jf, encoding="utf-8"))
        except ValueError as e:
            out.append(({"key": os.path.basename(jf)[:-5], "_file": jf}, [], "descriptor not read: %s" % e))
            continue
        D["key"] = D.get("key") or os.path.basename(jf)[:-5]
        D["_file"], D["_lane"] = jf, lane
        miss = [k for k in NEED if not str(D.get(k) or "").strip()]
        why = ""
        if miss:
            why = "descriptor lacks " + ", ".join(miss)
        elif D["kind"] not in KINDS:
            why = "kind must be one of %s" % ", ".join(KINDS)
        elif not PC.search(D["biller_address"].upper()) or not PC.search(D["biller_address_quote"].upper()):
            why = "the body's address and its quote must carry a Canadian postal code"
        elif len(D["biller_address_quote"]) > 300 or len(D["pays_quote"]) > 300:
            why = "a quote of more than 300 characters"
        elif C.registrable(host(D["biller_address_url"])) != C.registrable(host(D["biller_site"])):
            why = "the address must be quoted from the body's own site"
        elif D.get("list_hosts") and C.registrable(host(D.get("list_host_link_url") or "")) != C.registrable(host(D["biller_site"])):
            why = "list_hosts needs list_host_link_url: the body's own page that links its list on that platform"
        rows = []
        if not why:
            files = sorted(glob.glob(os.path.join(ROOT, "data/incoming/*/roster_%s.csv" % D["key"])) + glob.glob(os.path.join(ROOT, "data/incoming/*/roster_%s.csv.gz" % D["key"])))
            if not files:
                why = "no data/incoming/<lane>/roster_%s.csv(.gz)" % D["key"]
            for f in files:
                op = gzip.open if f.endswith(".gz") else open
                with op(f, "rt", encoding="utf-8-sig", errors="replace", newline="") as fh:
                    rows += list(csv.DictReader(fh))
        out.append((D, rows, why))
    return out


def take(a):
    import ap_crawler as C
    import cc_clients as CCL
    listed_by = collections.defaultdict(set)
    kept, report = [], []
    for D, rows, why in rosters():
        st = collections.Counter()
        if why:
            report.append((D["key"], 0, {"left out: " + why: 1}))
            continue
        bdom = C.registrable(host(D["biller_site"]))
        # 2026-11-12: a trade show's exhibitor list is often kept on its organiser's platform (Map Your Show, a2z, the show's own second domain): the
        # descriptor names those hosts in list_hosts, with list_host_link_url, the body's own page that links the list there
        hosts_ok = {bdom} | {C.registrable(host(x)) or x for x in (D.get("list_hosts") or [])}
        for r in rows:
            name, site, url = (r.get("listed_name") or "").strip(), (r.get("listed_website") or "").strip(), (r.get("list_url") or "").strip()
            h = host(site)
            dom = C.registrable(h) if h and "." in h else ""
            if not name or not dom:
                st["no name or no site of its own"] += 1
            elif NOT_OWN.search(h) or dom in hosts_ok:
                st["the link is a social network, a marketplace or the body's own site"] += 1
            elif not url.startswith("http") or C.registrable(host(url)) not in hosts_ok:
                st["list_url is not a page of the body's own site (nor of a list host it names)"] += 1
            elif re.search(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}", name):
                st["the listed name is an e-mail address (no e-mail from a roster is kept)"] += 1
            elif re.search(r"#\s*\d", name):
                st["a numbered store or unit of a chain (its link goes to the chain's site, not the member's own)"] += 1
            elif not name_fits_domain(name, dom):
                st["the linked site's name shares nothing with the listed name (a web host, a parent's or a chain's site)"] += 1
            else:
                st["taken"] += 1
                listed_by[dom].add(D["key"])
                kept.append((D, dom, h, name, url, (r.get("listed_address") or "").strip()[:200], (r.get("ref") or "").strip()[:60]))
        report.append((D["key"], len(rows), dict(st)))
    many = {d for d, s in listed_by.items() if len(s) > 15}
    return [k for k in kept if k[1] not in many], report, len(many)


def check(a):
    kept, report, many = take(a)
    for key, n, st in report:
        print("%-28s %6d lines  %s" % (key, n, st))
    print("listed organisations that would become leads: %d (domains on more than 15 rosters, left out: %d)" % (len({k[1] for k in kept}), many))


def merge(a):
    import cc_clients as CCL
    import lead_store as LS
    stamp = a.stamp or time.strftime("%Y%m%dT%H%M%S", time.gmtime())
    kept, report, many = take(a)
    leads, det = LS.load(exclude=("roster", stamp))
    snap = LS.snapshot(leads, det)
    new, refreshed, withdrawn = collections.Counter(), collections.Counter(), collections.Counter()
    takers = collections.defaultdict(list)
    for k in kept:
        takers[CCL.lead_key(k[1])].append(k)
    # the roster lane's leads are what today's rules and descriptors take: a lead whose roster was withdrawn, or that a stricter rule no longer
    # takes, is withdrawn; a lead whose descriptor was corrected (a better sentence of the body, its address) is written again
    for key in [k for k, d in det.items() if d.get("platform") == "roster_file" and k not in takers]:
        withdrawn[det[key].get("roster_key") or "?"] += 1
        leads.pop(key, None)
        det.pop(key, None)
    for key, ks in takers.items():
        if key in leads and det.get(key, {}).get("platform") != "roster_file":
            continue  # the organisation is already a lead of another lane (one row per organisation): its first relationship keeps the key
        was = det.get(key, {}).get("roster_key")
        D, dom, h, name, url, addr, ref = next((k for k in ks if k[0]["key"] == was), ks[0])
        kind = D["kind"]
        leads[key] = {"buyer_key": key, "buyer_name": name, "website": "https://%s/" % h, "canadian_vendor_rows": 1, "example_vendor": D["biller"],
                      "canada_field_value": "vendor located in Canada (roster: %s)=%s; “%s” (as printed on %s, read %s); %s: “%s” (%s)"
                                            % (kind, host(D["biller_site"]), D["biller_address_quote"], D["biller_address_url"], D["read"], WHAT[kind], D["pays_quote"], D["pays_url"]),
                      "evidence_dataset": url, "latest_record_date": D["read"]}
        det[key] = {"key": key, "platform": "roster_file", "roster": kind, "page_class": "sponsor" if kind == "exhibitor" else kind, "record_url": url, "vendor": D["biller"],
                    "record_date": D["read"], "title": "", "reference": ref, "vendor_address": "%s (as printed on %s, read %s)" % (D["biller_address"], D["biller_address_url"], D["read"]),
                    "vendor_address_quote": D["biller_address_quote"], "vendor_address_url": D["biller_address_url"], "vendor_site": D["biller_site"], "member_address_quote": addr,
                    "pays_quote": D["pays_quote"], "pays_url": D["pays_url"], "list_name": D["list_name"], "harvested_by": D["_lane"], "roster_key": D["key"]}
        (refreshed if was else new)[D["key"]] += 1
    w = LS.save("roster", stamp, leads, det, snap)
    for key, n, st in report:
        print("%-28s %6d lines  %s" % (key, n, st))
    print("roster leads withdrawn (roster withdrawn or no longer taken): %d %s" % (sum(withdrawn.values()), dict(withdrawn)))
    print("roster leads: +%d this run (%s); on file again: %d; shards written (rows, details, withdrawn; a row whose text did not change is not written): %s; "
          "domains on more than 15 rosters, left out: %d" % (sum(new.values()), dict(new), sum(refreshed.values()), w, many))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("cmd", choices=["check", "merge"])
    ap.add_argument("--stamp", default="")
    a = ap.parse_args()
    {"check": check, "merge": merge}[a.cmd](a)


if __name__ == "__main__":
    main()
