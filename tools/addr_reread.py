#!/usr/bin/env python3
"""Where an organisation is, read again on its own pages: the organisations with a confirmed role mailbox whose address names no distributor (no AI).

The rows that stand on where the organisation is (tools/by_location.py: the electricity distributor of its address bills it by law, every month,
on an invoice, paid through a bank) need the organisation's own address. The mailbox reader keeps the first postal address it sees in the VISIBLE
text of the pages it reads (tools/lead_crawl.py install_hooks). The rank build of 2026-11-13 04:08Z left 185,837 organisations with a confirmed
mailbox out for that reason alone ("no biller can be named for where it is"), 136,177 of them under a .ca name. A sample of 60 of those read again
(home page and up to three contact / about / location pages): 2 print a postal code in their text, 6 show their address only on the map their own
contact page embeds (“maps.google.com/maps?q=1131 Gainsborough Rd, London, Ontario”), 4 state it only in the page's structured data (schema.org
PostalAddress) — the organisation's own statements of where it is, in its own page's source, which the reader did not look at.

This reads those organisations' home page and up to three pages its own menu names as contact / about / location / hours, and keeps the first of:
  text    a Canadian postal address in the visible text (the same pattern as the mailbox reader: province, then postal code);
  jsonld  a schema.org PostalAddress of the organisation itself (an Organization / LocalBusiness / … object of the page's JSON-LD — never an
          event's venue, a person, a job posting or a product), in Canada (addressCountry CA / Canada, or a Canadian postal code);
  map     the address of the Google map its own page embeds (the place asked for in the map's address: q= / query=, or the place name of an
          embed's pb= string), when it carries a Canadian postal code or a city with its province.
A key the map's address carries (an API key) is never kept: only the address asked for. robots.txt obeyed, the project's user agent, the
project's reader (tools/ap_crawler.py: one request a second per host). A site that refuses the reader is left.

  pick   [--out F]                         the keys to read: confirmed mailbox (claude_buyer_ap_results_cccrawl*.csv, status found), no postal
                                           code in the site's facts or the mailbox's page, no city that names a distributor, not done before
  read   --shard K/N --minutes M --workers W  -> out/addr_reread_K.jsonl (one line per site: what was found, or why nothing)
  merge  DIR --stamp S                     -> data/incoming/claude/site_facts/facts_<S>a.gz (site facts lines with the address, the earlier
                                              line's name kept) + data/incoming/claude/site_facts/addr_reread_done.tsv (append-only)
"""
import argparse, csv, glob, gzip, html, json, os, re, sys, time, urllib.parse
import concurrent.futures as cf

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import ap_crawler as C  # noqa: E402
import by_location as BL  # noqa: E402

csv.field_size_limit(1 << 30)
INC = os.path.join(ROOT, "data/incoming/claude")
FACTS_DIR = os.path.join(INC, "site_facts")
DONE = os.path.join(FACTS_DIR, "addr_reread_done.tsv")
TARGETS = os.path.join(ROOT, "out/addr_targets.csv")
TODAY = time.strftime("%Y-%m-%d")
CONTACT = re.compile(r"contact|joindre|about|propos|location|find-us|visit|coordonn|nous-trouver|directions|hours|heures|adresse|address|bureau|office", re.I)
LD = re.compile(r"""<script[^>]+type\s*=\s*["']application/ld\+json["'][^>]*>(.*?)</script>""", re.I | re.S)
IFRAME = re.compile(r"""<iframe\b[^>]*?\bsrc\s*=\s*["']([^"']+)["']""", re.I)
MAPHOST = re.compile(r"^https?://(?:www\.|maps\.)?google\.[a-z.]+/maps|^https?://maps\.google\.[a-z.]+/", re.I)
# the objects of a page's JSON-LD whose address is NOT the organisation's own
NOT_ORG = {"event", "person", "jobposting", "offer", "aggregateoffer", "product", "review", "course", "courseinstance", "musicevent", "sportsevent",
           "businessevent", "educationevent", "socialevent", "theaterevent", "festival", "exhibitionevent", "screeningevent", "foodevent", "creativework",
           "article", "blogposting", "newsarticle", "webpage", "website", "breadcrumblist", "residence", "apartment", "house", "singlefamilyresidence",
           "accommodation", "realestatelisting", "lodgingreservation", "reservation", "trip"}
PROV = {"ab", "bc", "mb", "nb", "nl", "ns", "nt", "nu", "on", "pe", "qc", "sk", "yt", "alberta", "british columbia", "colombie-britannique", "manitoba",
        "new brunswick", "nouveau-brunswick", "newfoundland and labrador", "terre-neuve-et-labrador", "nova scotia", "nouvelle-écosse", "northwest territories",
        "nunavut", "ontario", "prince edward island", "île-du-prince-édouard", "quebec", "québec", "saskatchewan", "yukon", "pq", "nfld", "pei"}


def _norm_space(s):
    return re.sub(r"\s+", " ", re.sub(r"[\u200b-\u200f\u2060\ufeff]", "", html.unescape(str(s or "")))).strip()


def _types(o):
    t = o.get("@type")
    if isinstance(t, str):
        return {t.lower()}
    if isinstance(t, list):
        return {str(x).lower() for x in t}
    return set()


def jsonld_address(raw):
    """(address text, quote) of the page's own organisation, or None"""
    for m in LD.finditer(raw[:3_000_000]):
        body = m.group(1).strip()
        body = re.sub(r"^\s*<!--|-->\s*$", "", body)
        try:
            data = json.loads(body)
        except ValueError:
            try:
                data = json.loads(re.sub(r"[\x00-\x1f]", " ", body))
            except ValueError:
                continue
        stack = [(data, set())]
        while stack:
            o, parent = stack.pop()
            if isinstance(o, list):
                stack.extend((x, parent) for x in o)
                continue
            if not isinstance(o, dict):
                continue
            ty = _types(o)
            for k_, v_ in o.items():
                if k_ in ("@graph", "mainEntity", "publisher", "provider", "author", "brand", "parentOrganization", "department", "subOrganization", "member", "itemListElement"):
                    stack.append((v_, ty if k_ in ("@graph", "mainEntity", "itemListElement") else ty | {"_nested_" + k_.lower()}))
            if ty & NOT_ORG or any(t_.startswith("_nested_author") for t_ in parent) or (not ty and parent & NOT_ORG):
                continue
            adr = o.get("address")
            if isinstance(adr, list):
                adr = next((a for a in adr if isinstance(a, dict)), None)
            if not isinstance(adr, dict):
                continue
            parts = [_norm_space(adr.get(k_)) for k_ in ("streetAddress", "addressLocality", "addressRegion", "postalCode")]
            ctry = adr.get("addressCountry")
            if isinstance(ctry, dict):
                ctry = ctry.get("name") or ctry.get("@id") or ""
            ctry = _norm_space(ctry)
            pcs = list(BL.codes(parts[3] or "")) if parts[3] else []
            in_ca = ctry.lower() in ("ca", "can", "canada") or bool(pcs) or (parts[2] or "").lower() in PROV
            if not in_ca or not (parts[3] or (parts[1] and parts[2])):
                continue
            if ctry and ctry.lower() not in ("ca", "can", "canada"):
                continue
            txt = ", ".join(p for p in (parts[0], parts[1]) if p)
            tail = " ".join(p for p in (parts[2], parts[3]) if p)
            addr = (txt + (", " if txt and tail else "") + tail).strip(", ")
            quote = ", ".join("%s: %s" % (k_, v_) for k_, v_ in zip(("streetAddress", "addressLocality", "addressRegion", "postalCode"), parts) if v_)
            if ctry:
                quote += ", addressCountry: %s" % ctry
            name = _norm_space(o.get("name"))[:80]
            return addr[:200], ("%s (schema.org PostalAddress%s in the page source)" % (quote, (" of “%s”" % name) if name else ""))[:300]
    return None


def map_address(raw):
    """(address text, quote) of the Google map the page embeds, or None — the address asked for, never the map's key"""
    for m in IFRAME.finditer(raw[:3_000_000]):
        src = html.unescape(m.group(1).strip())
        if src.startswith("//"):
            src = "https:" + src
        if not MAPHOST.search(src):
            continue
        u = urllib.parse.urlparse(src)
        q = urllib.parse.parse_qs(u.query)
        cands = q.get("q", []) + q.get("query", []) + q.get("daddr", [])
        for pb in q.get("pb", []):
            cands += [urllib.parse.unquote_plus(x) for x in re.findall(r"!2s([^!]+)", pb)]
        for c_ in cands:
            c_ = _norm_space(urllib.parse.unquote_plus(c_))
            if not c_ or len(c_) > 200 or re.fullmatch(r"[-\d.,\s]+", c_) or "0x" in c_[:4]:
                continue
            if next(BL.codes(c_), None) or BL.CITY_RX.search(c_):
                return c_[:200], ("the map its own page embeds is of “%s” (Google Maps embed in the page source)" % c_)[:300]
    return None


def text_address(raw):
    import cc_clients as CCL
    t = C.visible(raw)
    m = CCL.ADDR.search(t)
    if not m:
        return None
    q = re.sub(r"^\S*\s", "", t[max(0, m.start() - 110):m.end()].strip())[-200:]
    return (CCL.address_from(q) or q)[:200], q[:300]


def get(url):
    try:
        if not C.allowed(url):
            return None, url, "robots"
        st, ct, data, final = C.fetch(url)
        if st != 200 or not data:
            return None, final or url, "http_%s" % st
        if "html" not in (ct or "text/html").lower() and "xml" not in (ct or "").lower():
            return None, final or url, "not_html"
        return data.decode("utf-8", "replace"), final or url, "ok"
    except Exception as e:  # noqa: BLE001
        return None, url, "error:%s" % type(e).__name__


# 2026-11-13: the organisation's own telephone number, printed on its pages (a tel: link first, else the number its pages print most often) —
# tools/phone_places.py looks for the Overture Maps place that lists it when no address was found
PHONE = os.path.join(FACTS_DIR, "phones.tsv")
_PH = re.compile(r"(?<!\d)(?:\+?1[\s.\-]?)?\(?([2-9]\d{2})\)?[\s.\-]?([2-9]\d{2})[\s.\-]?(\d{4})(?!\d)")
_CA_AC = set("204 226 236 249 250 257 263 289 306 343 354 365 367 368 382 403 416 418 428 431 437 438 450 468 474 506 514 519 548 579 581 584 587 604 613 "
             "639 647 672 683 705 709 742 753 778 780 782 807 819 825 867 873 879 902 905".split())


def own_phone(pages):
    import collections as _c
    for u, r in pages:
        for m in re.finditer(r"""href\s*=\s*["']tel:([^"']{7,40})["']""", r[:3_000_000], re.I):
            d = re.sub(r"\D", "", m.group(1))[-10:]
            if len(d) == 10 and d[:3] in _CA_AC:
                return d, u
    cnt, where = _c.Counter(), {}
    for u, r in pages:
        for m in _PH.finditer(C.visible(r)):
            if m.group(1) in _CA_AC:
                d = m.group(1) + m.group(2) + m.group(3)
                cnt[d] += 1; where.setdefault(d, u)
    if cnt:
        d, _ = cnt.most_common(1)[0]
        return d, where[d]
    return "", ""


def read_one(t):
    key, site = t["key"], t["site"]
    raw, final, st = get(site)
    out = {"key": key, "site": site, "date": TODAY, "status": st}
    if raw is None:
        return out
    base = final if str(final).startswith("http") else site
    home_dom = C.registrable(urllib.parse.urlparse(base).hostname or "")
    pages = [(base, raw)]
    seen = {base.rstrip("/")}
    for u, lab in C.links(raw, base):
        if len(pages) >= 4:
            break
        p = urllib.parse.urlparse(u)
        if p.scheme not in ("http", "https") or C.registrable(p.hostname or "") != home_dom or u.rstrip("/") in seen:
            continue
        if not (CONTACT.search(p.path or "") or CONTACT.search(lab or "")) or re.search(r"\.(?:pdf|jpe?g|png|gif|zip|docx?)$", p.path or "", re.I):
            continue
        seen.add(u.rstrip("/"))
        r2, f2, s2 = get(u)
        if r2 is not None:
            pages.append((f2 if str(f2).startswith("http") else u, r2))
    try:
        ph, phu = own_phone(pages)
    except Exception:  # noqa: BLE001
        ph, phu = "", ""
    if ph:
        out.update(phone=ph, phone_url=phu)
    for how, fn in (("text", text_address), ("jsonld", jsonld_address), ("map", map_address)):
        for u, r in pages:
            try:
                got = fn(r)
            except Exception:  # noqa: BLE001
                got = None
            if got:
                addr, quote = got
                out.update(status="found", address=addr, address_quote=quote, address_url=u, address_how=how, address_country="CA")
                return out
    out["status"] = "nothing"
    out["pages"] = len(pages)
    return out


def pick_phones(a):
    """the sites read before that gave no address, whose telephone number is not on file: read again for the number (and the address)"""
    have = set()
    if os.path.exists(PHONE):
        with open(PHONE, encoding="utf-8") as f:
            have = {l.split("\t", 1)[0] for l in f if l.strip()}
    last = {}
    if os.path.exists(DONE):
        with open(DONE, encoding="utf-8") as f:
            for l in f:
                p_ = l.rstrip("\n").split("\t")
                if len(p_) >= 2:
                    last[p_[0]] = p_[1]
    site = {}
    for p in sorted(glob.glob(os.path.join(FACTS_DIR, "facts_*.gz"))):
        with gzip.open(p, "rt", encoding="utf-8", errors="replace") as f:
            for l in f:
                try:
                    d = json.loads(l)
                except ValueError:
                    continue
                if d.get("key") and d.get("site") and d["key"] not in site:
                    site[d["key"]] = d["site"]
    need = {k for k, st in last.items() if st == "nothing" and k not in have and not site.get(k)}
    if need:  # no site facts: the mailbox's own domain (the organisation's site, as cmd_pick took it)
        for p in sorted(glob.glob(os.path.join(INC, "claude_buyer_ap_results_cccrawl*.csv"))):
            with open(p, encoding="utf-8", errors="replace", newline="") as f:
                for r in csv.DictReader(f):
                    k = r.get("buyer_key")
                    if k in need and r.get("status") == "found" and "@" in (r.get("ap_email") or "") and k not in site:
                        site[k] = "https://%s/" % r["ap_email"].strip().lower().partition("@")[2]
    os.makedirs(os.path.dirname(a.out) or ".", exist_ok=True)
    n = 0
    with open(a.out, "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["key", "site"])
        for k, st in sorted(last.items()):
            if st == "nothing" and k not in have and site.get(k):
                w.writerow([k, site[k]]); n += 1
    print("addr-reread pick --phones: %d sites read before with no address and no telephone number on file -> %s" % (n, a.out))


def cmd_pick(a):
    if getattr(a, "phones", False):
        return pick_phones(a)
    done = set()
    if os.path.exists(DONE):
        with open(DONE, encoding="utf-8") as f:
            done = {l.split("\t", 1)[0] for l in f if l.strip()}
    found = {}
    for p in sorted(glob.glob(os.path.join(INC, "claude_buyer_ap_results_cccrawl*.csv"))):
        with open(p, encoding="utf-8", errors="replace", newline="") as f:
            for r in csv.DictReader(f):
                if r.get("status") == "found" and r.get("ap_email") and "@" in r["ap_email"]:
                    found[r["buyer_key"]] = (r["ap_email"].strip().lower(), r.get("evidence_url") or "", r.get("evidence_quote") or "")
    facts = {}
    for p in sorted(glob.glob(os.path.join(FACTS_DIR, "facts_*.gz"))):
        with gzip.open(p, "rt", encoding="utf-8", errors="replace") as f:
            for l in f:
                try:
                    d = json.loads(l)
                except ValueError:
                    continue
                k = d.get("key")
                if not k:
                    continue
                o = facts.setdefault(k, {})
                for c_ in ("site", "address", "address_quote", "address_country", "city_quote"):
                    if d.get(c_) and not o.get(c_):
                        o[c_] = d[c_]
    n = {"found": len(found), "located": 0, "city": 0, "abroad": 0, "done": 0, "webmail": 0, "picked": 0}
    os.makedirs(os.path.dirname(a.out), exist_ok=True)
    with open(a.out, "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["key", "site"])
        for k, (e, url, q) in sorted(found.items()):
            if k in done and not getattr(a, "include_done", False):  # (tools/phone_places.py: every organisation still unlocated, read again or not)
                n["done"] += 1; continue
            fa = facts.get(k, {})
            txt = " ".join([fa.get("address") or "", fa.get("address_quote") or "", q])
            if BL.fsa_of(txt):
                n["located"] += 1; continue
            if fa.get("address_country") and fa["address_country"] != "CA":
                n["abroad"] += 1; continue
            if BL.biller_for_city(" ".join([fa.get("address_quote") or "", fa.get("city_quote") or "", q])):
                n["city"] += 1; continue
            dom = e.partition("@")[2]
            site = fa.get("site") or ""
            if not site:
                if re.match(r"(?:gmail|hotmail|outlook|yahoo|live|icloud|me|msn|aol|videotron|sympatico|shaw|telus|rogers|bell|cogeco|eastlink|sasktel)\.", dom):
                    n["webmail"] += 1; continue
                site = "https://%s/" % dom
            w.writerow([k, site])
            n["picked"] += 1
    print("addr-reread pick: %s -> %s" % (n, a.out))


def cmd_read(a):
    k_, n_ = (int(x) for x in a.shard.split("/"))
    with open(a.targets, encoding="utf-8", newline="") as f:
        rows = [r for i, r in enumerate(csv.DictReader(f)) if i % n_ == k_]
    if a.limit:
        rows = rows[:a.limit]
    os.makedirs("out", exist_ok=True)
    path = "out/addr_reread_%d.jsonl" % k_
    deadline = time.time() + a.minutes * 60
    cnt = {}
    with open(path, "a", encoding="utf-8") as f, cf.ThreadPoolExecutor(a.workers) as ex:
        it = iter(rows)
        futs = set()
        def feed():
            while len(futs) < a.workers * 2 and time.time() < deadline:
                try:
                    futs.add(ex.submit(read_one, next(it)))
                except StopIteration:
                    return False
            return True
        more = feed()
        while futs:
            done, _ = cf.wait(futs, timeout=60, return_when=cf.FIRST_COMPLETED)
            for fu in done:
                futs.discard(fu)
                try:
                    o = fu.result()
                except Exception:  # noqa: BLE001
                    continue
                f.write(json.dumps(o, ensure_ascii=False) + "\n")
                st = o["status"] if o["status"] in ("found", "nothing", "robots") else o["status"].split(":")[0]
                cnt[st] = cnt.get(st, 0) + 1
                if o["status"] == "found":
                    cnt["by_" + o["address_how"]] = cnt.get("by_" + o["address_how"], 0) + 1
            f.flush()
            if more:
                more = feed()
            if time.time() > deadline + 300:
                break
    print("addr-reread shard %s: %d sites asked; %s" % (a.shard, sum(v for k2, v in cnt.items() if not k2.startswith("by_")), cnt))


def cmd_merge(a):
    recs = {}
    for p in sorted(glob.glob(os.path.join(a.dir, "**", "addr_reread_*.jsonl"), recursive=True)):
        with open(p, encoding="utf-8") as f:
            for l in f:
                try:
                    o = json.loads(l)
                except ValueError:
                    continue
                if o.get("key") and (o["key"] not in recs or o.get("status") == "found"):
                    recs[o["key"]] = o
    if not recs:
        print("addr-reread merge: nothing to merge"); return
    prev = {}
    need = {k for k, o in recs.items() if o.get("status") == "found"}
    for p in sorted(glob.glob(os.path.join(FACTS_DIR, "facts_*.gz"))):
        with gzip.open(p, "rt", encoding="utf-8", errors="replace") as f:
            for l in f:
                try:
                    d = json.loads(l)
                except ValueError:
                    continue
                if d.get("key") in need:
                    o = prev.setdefault(d["key"], {})
                    for c_, v_ in d.items():
                        if v_ and not o.get(c_):
                            o[c_] = v_
    os.makedirs(FACTS_DIR, exist_ok=True)
    out = os.path.join(FACTS_DIR, "facts_%sa.gz" % a.stamp)
    n = {"found": 0, "text": 0, "jsonld": 0, "map": 0}
    with gzip.open(out, "wt", encoding="utf-8") as f:
        for k in sorted(need):
            o = recs[k]
            line = {c_: v_ for c_, v_ in (prev.get(k) or {}).items() if c_ in ("key", "site", "site_name", "title", "asked", "moved", "ids")}
            line.update(key=k, site=line.get("site") or o.get("site"), date=o.get("date") or TODAY, address_country="CA", address=o["address"],
                        address_quote=o["address_quote"], address_url=o["address_url"], address_how=o["address_how"])
            f.write(json.dumps(line, ensure_ascii=False) + "\n")
            n["found"] += 1; n[o["address_how"]] += 1
    with open(DONE, "a", encoding="utf-8") as f:
        for k, o in sorted(recs.items()):
            f.write("%s\t%s\t%s\n" % (k, o.get("status") or "", o.get("date") or TODAY))
    have_ph = set()
    if os.path.exists(PHONE):
        with open(PHONE, encoding="utf-8") as f:
            have_ph = {l.split("\t", 1)[0] for l in f if l.strip()}
    n_ph = 0
    with open(PHONE, "a", encoding="utf-8") as f:
        for k, o in sorted(recs.items()):
            if o.get("phone") and k not in have_ph:
                f.write("%s\t%s\t%s\t%s\n" % (k, o["phone"], o.get("phone_url") or "", o.get("date") or TODAY)); n_ph += 1
    print("addr-reread: %d telephone numbers of the organisations' own pages -> %s" % (n_ph, os.path.relpath(PHONE, ROOT)))
    tot = sum(1 for _ in open(DONE, encoding="utf-8"))
    print("addr-reread: %d sites read this run, %d addresses found (%s) -> %s; sites done so far: %d" % (len(recs), n["found"], n, os.path.relpath(out, ROOT), tot))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("cmd", choices=["pick", "read", "merge"])
    ap.add_argument("dir", nargs="?")
    ap.add_argument("--out", default=TARGETS)
    ap.add_argument("--targets", default=TARGETS)
    ap.add_argument("--shard", default="0/1")
    ap.add_argument("--minutes", type=float, default=150)
    ap.add_argument("--workers", type=int, default=40)
    ap.add_argument("--limit", type=int, default=0)
    ap.add_argument("--stamp", default=time.strftime("%Y%m%dT%H%M%S"))
    ap.add_argument("--phones", action="store_true", help="pick: the sites read before with no address and no telephone number on file")
    a = ap.parse_args()
    {"pick": cmd_pick, "read": cmd_read, "merge": cmd_merge}[a.cmd](a)


if __name__ == "__main__":
    main()
