#!/usr/bin/env python3
"""Second pass over Canada-located vendors' sites for their client / case-study / reference pages. No AI.

tools/client_lists.py only follows relationship links found on each vendor's home page. Many vendors keep their client
list deeper: in the sitemap, or at a conventional address (/clients, /customers, /case-studies, /nos-clients ...). This
pass reads the sitemap and tries those addresses, then (like client_lists.py) keeps every outbound link of a real
relationship page as a lead, and also the client names shown as logos without a link (img alt text) in a separate file
for website look-up. Pages already read by client_lists.py are skipped. Polite: robots.txt, one request per second per site.
  python3 tools/client_lists2.py --shard I --of N
Leads: ~/cch-leads/socrata_rel2_<I>.jsonl (picked up by tools/lead_scanner.py --bridge); logo names:
~/cch-leads/logo_names_<I>.jsonl.
"""
import argparse, csv, glob, hashlib, json, os, re, sys, urllib.parse
from concurrent.futures import ThreadPoolExecutor

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import client_lists as CL

PATHS = ["clients", "our-clients", "customers", "our-customers", "case-studies", "casestudies", "success-stories",
         "testimonials", "references", "clientele", "nos-clients", "clients/", "fr/clients", "en/clients",
         "nos-realisations", "realisations", "temoignages", "fr/nos-clients", "en/our-clients", "portfolio"]
LOGO_BAD = re.compile(r"logo$|^logo|image|img|icon|banner|photo|picture|arrow|menu|search|close|facebook|linkedin|twitter|"
                      r"instagram|youtube|\.png|\.jpe?g|\.svg|\.webp|^\W*$|^\d+$", re.I)


def sitemap_rel(site):
    """Relationship-page addresses listed in the site's sitemap (first two sitemap files)."""
    out, seen = [], set()
    queue = [urllib.parse.urljoin(site, "/sitemap.xml"), urllib.parse.urljoin(site, "/sitemap_index.xml")]
    while queue and len(seen) < 4:
        sm = queue.pop(0)
        if sm in seen:
            continue
        seen.add(sm)
        txt, _ = CL.fetch(sm, 2_000_000) if CL.allowed(sm) else (None, sm)
        if not txt:
            continue
        for loc in re.findall(r"<loc>\s*([^<\s]+)\s*</loc>", txt):
            if loc.endswith(".xml") and len(queue) < 4:
                queue.append(loc)
            elif CL.REL.search(urllib.parse.urlparse(loc).path) and not CL.NOT_REL.search(loc):
                out.append(loc)
    return out[:20]


def one(v, out, logos, done, read_before):
    site = v["known_website"].strip()
    if not site.startswith("http") or site in done:
        return
    vhost = CL.base(urllib.parse.urlparse(site).hostname)
    cands = sitemap_rel(site)
    for p in PATHS:
        cands.append(urllib.parse.urljoin(site.rstrip("/") + "/", p))
    hits, names, read = [], [], 0
    for pu in list(dict.fromkeys(cands)):
        if read >= 5 or pu in read_before or not CL.allowed(pu):
            continue
        page, final = CL.fetch(pu)
        if not page or CL.base(urllib.parse.urlparse(final).hostname) != vhost:
            continue
        path = urllib.parse.urlparse(final).path
        if not CL.REL.search(path) or CL.NOT_REL.search(path) or final in read_before:
            continue  # redirected to the home page or elsewhere: not a relationship page
        read += 1
        read_before.add(final)
        title = re.search(r"(?is)<title>(.*?)</title>", page)
        title = re.sub(r"\s+", " ", title.group(1)).strip()[:120] if title else ""
        for href, label in CL.anchors(page, final):
            h = CL.base(urllib.parse.urlparse(href).hostname)
            if not h or h == vhost or h.endswith("." + vhost) or CL.SKIP.search(h) or "." not in h:
                continue
            hits.append({"platform": "vendor_site", "domain": h, "dataset_id": final, "dataset": "relationship page of a Canada-located vendor",
                         "dataset_url": final, "publisher": h, "buyer_unit": "", "website": "https://%s/" % h,
                         "vendor": v.get("buyer_name") or vhost, "canada_field": "vendor located in Canada (%s)" % v["buyer_key"].split(":")[0],
                         "canada_value": vhost, "row": {"relationship_page": final, "page_title": title, "client_label": label[:120],
                                                        "vendor_key": v["buyer_key"], "vendor_site": site, "pass": 2}})
        body = re.sub(r"(?is)<(header|nav|footer)\b.*?</\1>", " ", page)  # logos in the page body, not the menus
        for alt in re.findall(r"(?is)<img\b[^>]*?\balt\s*=\s*[\"']([^\"']{3,80})[\"']", body):
            a = re.sub(r"\s+", " ", alt).strip()
            a = re.sub(r"(?i)\s*(logo|logotype|logotipo)\s*$", "", a).strip(" -|")
            if len(a) >= 3 and not LOGO_BAD.search(a) and a.lower() not in (v.get("buyer_name") or "").lower():
                names.append({"name": a, "vendor": v.get("buyer_name") or vhost, "vendor_key": v["buyer_key"], "vendor_site": site, "page": final})
    uniq = {h["domain"]: h for h in hits}
    with CL_LOCK:
        if 0 < len(uniq) <= 300:
            with open(out, "a", encoding="utf-8") as f:
                for h in uniq.values():
                    f.write(json.dumps(h, ensure_ascii=False) + "\n")
        if 0 < len(names) <= 300:
            with open(logos, "a", encoding="utf-8") as f:
                for n in {x["name"].lower(): x for x in names}.values():
                    f.write(json.dumps(n, ensure_ascii=False) + "\n")
        with open(out + ".done", "a", encoding="utf-8") as f:
            f.write("%s\t%d\t%d\n" % (site, len(uniq), len(names)))


import threading
CL_LOCK = threading.Lock()


def main():
    a = argparse.ArgumentParser()
    a.add_argument("--shard", type=int, default=0)
    a.add_argument("--of", type=int, default=1)
    a.add_argument("--workers", type=int, default=24)
    a = a.parse_args()
    os.makedirs(CL.LEADS, exist_ok=True)
    out = os.path.join(CL.LEADS, "socrata_rel2_%02d.jsonl" % a.shard)
    logos = os.path.join(CL.LEADS, "logo_names_%02d.jsonl" % a.shard)
    done = set(l.split("\t")[0] for l in open(out + ".done", encoding="utf-8")) if os.path.exists(out + ".done") else set()
    read_before = set()
    for f in glob.glob(os.path.join(CL.LEADS, "socrata_rel_*.jsonl")):
        for line in open(f, encoding="utf-8", errors="replace"):
            try:
                read_before.add((json.loads(line).get("row") or {}).get("relationship_page", ""))
            except ValueError:
                pass
    vendors = []
    for f in sorted(glob.glob(os.path.expanduser("~/cch-crawler/coord/tasks/claude/claude_buyer_ap_batch90[2-4].csv"))):
        for r in csv.DictReader(open(f, encoding="utf-8-sig")):
            h = CL.base(urllib.parse.urlparse(r.get("known_website") or "").hostname)
            if h and int(hashlib.sha1(h.encode()).hexdigest(), 16) % a.of == a.shard:
                vendors.append(r)
    print("shard %d: %d vendor sites" % (a.shard, len(vendors)), flush=True)
    with ThreadPoolExecutor(a.workers) as ex:
        list(ex.map(lambda v: one(v, out, logos, done, read_before), vendors))
    print("shard %d finished" % a.shard, flush=True)


if __name__ == "__main__":
    main()
