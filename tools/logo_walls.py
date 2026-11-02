#!/usr/bin/env python3
"""Clients shown in the "trusted by / our clients / ils nous font confiance" logo wall of Canadian vendors' home pages. No AI.

Business-to-business vendors show their best-known customers as a row of logos on the home page. Each logo is a buyer
of a Canada-located vendor, published by the vendor itself. This reads each vendor's home page once (robots.txt, one
request per second per site), finds the section introduced by a client phrase, and keeps the logos in it: linked logos
become relationship leads directly (~/cch-leads/socrata_walls.jsonl), unlinked logos become names for tools/logo_sites.py
to find in Wikidata (~/cch-leads/logo_names_8walls.jsonl).
  python3 tools/logo_walls.py --shard I --of N
"""
import argparse, csv, glob, hashlib, html, json, os, re, sys, threading, urllib.parse
from concurrent.futures import ThreadPoolExecutor
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import client_lists as CL

PHRASE = re.compile(r"trusted by|our clients|our customers|clients include|customers include|who we work with|who we serve|"
                    r"brands we|companies we|some of our clients|selected clients|our valued clients|join (?:the )?(?:\d|thousands)|"
                    r"leading (?:companies|brands|organizations) (?:trust|rely|choose)|nos clients|ils nous font confiance|"
                    r"elles nous font confiance|ils nous ont fait confiance|nos clientèles?|quelques[- ]uns de nos clients|"
                    r"nos partenaires d'affaires|client list|clientele", re.I)
NOT_PHRASE = re.compile(r"partner|partenaire|certified|certifié|accredit|award|prix|member of|membre de|as seen|featured in|"
                        r"vu dans|press|media|funded by|financé|supported by|soutenu par|investor", re.I)
LOGO_BAD = re.compile(r"^logo$|image|img|icon|banner|photo|picture|arrow|menu|search|close|facebook|linkedin|twitter|"
                      r"instagram|youtube|\.png|\.jpe?g|\.svg|\.webp|^\W*$|^\d+$|placeholder|slide|background", re.I)
lock = threading.Lock()


def sections(page):
    """Chunks of the home page that follow a client phrase (up to the next heading block)."""
    body = re.sub(r"(?is)<(header|nav|footer|script|style)\b.*?</\1>", " ", page)
    for m in PHRASE.finditer(body):
        before = body[max(0, m.start() - 300):m.start()]
        heading = re.sub(r"(?s)<[^>]+>", " ", body[m.start():m.start() + 200])
        if NOT_PHRASE.search(heading[:120]):
            continue
        yield body[m.start():m.start() + 12000]


def one(v, out_leads, out_names, done):
    site = v["known_website"].strip()
    if not site.startswith("http") or site in done:
        return
    vhost = CL.base(urllib.parse.urlparse(site).hostname)
    links, names = {}, {}
    if CL.allowed(site):
        page, final = CL.fetch(site)
        if page:
            for sec in sections(page):
                for href, label in CL.anchors(sec, final):
                    h = CL.base(urllib.parse.urlparse(href).hostname)
                    if h and h != vhost and not h.endswith("." + vhost) and not CL.SKIP.search(h) and "." in h:
                        links.setdefault(h, label)
                for alt in re.findall(r"(?is)<img\b[^>]*?\balt\s*=\s*[\"']([^\"']{2,80})[\"']", sec):
                    a = re.sub(r"\s+", " ", html.unescape(alt)).strip()
                    a = re.sub(r"(?i)\s*(logo|logotype|logotipo|client logo|customer logo)\s*$", "", a).strip(" -|")
                    a = re.sub(r"(?i)^(logo|client|customer)\s*[-:|]?\s*", "", a).strip()
                    if len(a) >= 2 and not LOGO_BAD.search(a) and a.lower() != (v.get("buyer_name") or "").lower():
                        names.setdefault(a.lower(), a)
    with lock:
        if 0 < len(links) <= 80:
            with open(out_leads, "a", encoding="utf-8") as f:
                for h, label in links.items():
                    f.write(json.dumps({"platform": "vendor_site", "domain": h, "dataset_id": site, "dataset": "client logo wall on a Canada-located vendor's home page",
                                        "dataset_url": site, "publisher": h, "buyer_unit": "", "website": "https://%s/" % h,
                                        "vendor": v.get("buyer_name") or vhost, "canada_field": "vendor located in Canada (wall)", "canada_value": vhost,
                                        "row": {"relationship_page": site, "client_label": label[:120], "vendor_key": v["buyer_key"], "pass": "logo_wall"}}, ensure_ascii=False) + "\n")
        if 0 < len(names) <= 80:
            with open(out_names, "a", encoding="utf-8") as f:
                for a in names.values():
                    f.write(json.dumps({"name": a, "vendor": v.get("buyer_name") or vhost, "vendor_key": "wall:" + v["buyer_key"], "vendor_site": site, "page": site}, ensure_ascii=False) + "\n")
        with open(out_leads + ".done", "a", encoding="utf-8") as f:
            f.write("%s\t%d\t%d\n" % (site, len(links), len(names)))


def main():
    a = argparse.ArgumentParser()
    a.add_argument("--shard", type=int, default=0)
    a.add_argument("--of", type=int, default=1)
    a.add_argument("--workers", type=int, default=32)
    a = a.parse_args()
    out_leads = os.path.join(CL.LEADS, "socrata_walls_%02d.jsonl" % a.shard)
    out_names = os.path.join(CL.LEADS, "logo_names_8walls_%02d.jsonl" % a.shard)
    done = set(l.split("\t")[0] for l in open(out_leads + ".done", encoding="utf-8")) if os.path.exists(out_leads + ".done") else set()
    vendors = []
    for n in (3, 4, 2):
        f = os.path.expanduser("~/cch-crawler/coord/tasks/claude/claude_buyer_ap_batch90%d.csv" % n)
        if not os.path.exists(f):
            continue
        for r in csv.DictReader(open(f, encoding="utf-8-sig")):
            h = CL.base(urllib.parse.urlparse(r.get("known_website") or "").hostname)
            if h and int(hashlib.sha1(h.encode()).hexdigest(), 16) % a.of == a.shard:
                vendors.append(r)
    print("shard %d: %d vendor home pages" % (a.shard, len(vendors)), flush=True)
    with ThreadPoolExecutor(a.workers) as ex:
        list(ex.map(lambda v: one(v, out_leads, out_names, done), vendors))
    print("shard %d finished" % a.shard, flush=True)


if __name__ == "__main__":
    main()
