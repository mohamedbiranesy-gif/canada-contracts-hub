#!/usr/bin/env python3
"""Private buyers from the customer stories of Canada-headquartered companies. No AI.

Canadian software and service companies publish one page per customer ("How <Customer> ... with <Vendor>",
"<Customer> case study"). Each page names a buyer of a Canada-located vendor and usually links to the buyer's site.
For each vendor: the sitemap gives the story pages (paths like /customers/<slug>, /case-studies/<slug>,
/customer-stories/<slug>, /success-stories/<slug>, /clients/<slug>); each page is read once (robots.txt, one request per
second per site) and gives: the customer's name (page title / h1), the customer's website (the external link that the
page's main content points to most), the page date when shown. Output, picked up by tools/lead_scanner.py --bridge:
~/cch-leads/socrata_stories.jsonl (customer with a website) and ~/cch-leads/logo_names_9stories.jsonl (name only,
for tools/logo_sites.py to find the website in Wikidata).
  python3 tools/customer_stories.py [--per-vendor 600] [--workers 8]
"""
import argparse, collections, html, json, os, re, sys, threading, urllib.parse
from concurrent.futures import ThreadPoolExecutor
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import client_lists as CL

VENDORS = """shopify.com lightspeedhq.com opentext.com kinaxis.com coveo.com docebo.com clio.com hootsuite.com getjobber.com
descartes.com cgi.com thinkific.com vendasta.com mitel.com absolute.com nuvei.com d2l.com geotab.com tecsys.com nulogy.com
visier.com procurify.com ada.cx 1password.com unbounce.com later.com trulioo.com absorblms.com benevity.com plooto.com
softchoice.com calian.com alithya.com enghouse.com magnetforensics.com dialogue.co league.com cohere.com symend.com
mdfcommerce.com jonassoftware.com harriscomputer.com coconutsoftware.com sylogist.com points.com pivotree.com
freshbooks.com wave.com dyedurham.com bench.co clearco.com wealthsimple.com telus.com bell.ca rogers.com colliers.com
firstservice.com stantec.com wsp.com atkinsrealis.com hatch.com aecon.com pcl.com ellisdon.com pomerleau.ca bird.ca
cae.com mda.space bombardier.com magna.com linamar.com ats-automation.com celestica.com nfigroup.com novabus.com
prevostcar.com bluewater.ca ritchiebros.com sierrawireless.com kinaxis.com ecobee.com farmersedge.ca dialogue.co
miovision.com faire.com wattpad.com ecoation.com ceridian.com dayforce.com uken.com hopper.com borrowell.com
igloosoftware.com acquisio.com lumenpulse.com element.ai stackadapt.com northstarclean.ca fullscript.com eventmobi.com
achievers.com vidyard.com rewind.com wealthica.com float.com fintech.ca ritual.co hubdoc.com ecopia.ai 360insights.com
p2pi.com clearpath.ai avidbots.com attabotics.com kepler.space ssa.ca sigma.software""".split()
STORY = re.compile(r"/(customers?|customer-stories|customer-story|case-studies|case-study|casestudies|success-stories|"
                   r"success-story|clients?|client-stories|stories|etudes-de-cas|temoignages|references)/[^/?#]{3,}", re.I)
NOT_STORY = re.compile(r"/(tag|category|page|author|feed|search|login|support|help|careers?|jobs?)/|\.(pdf|jpg|png|xml)$", re.I)
TITLE_PATTERNS = [r"^how\s+(.{2,60}?)\s+(uses?|used|scaled?|grew|increased|reduced|built|transformed|boosted|saved|cut|drove|"
                  r"achieved|improved|streamlined|automated|leverages?|gets?|got|turned|went|moved|made|keeps?|runs?)\b",
                  r"^(.{2,60}?)\s+(case study|customer story|success story|étude de cas)\b",
                  r"^(case study|customer story|success story|étude de cas)\s*[:|\-–]\s*(.{2,60})$",
                  r"^(.{2,50}?)\s*[|\-–:]\s"]
lock = threading.Lock()
LEADS = CL.LEADS


def fetch_xml(url, limit=8_000_000):
    """Like client_lists.fetch, but for sitemaps (XML, possibly gzipped)."""
    import gzip, time, urllib.request
    host = urllib.parse.urlparse(url).hostname or ""
    wait = CL.last.get(host, 0) + 1.0 - time.time()
    if wait > 0:
        time.sleep(wait)
    CL.last[host] = time.time()
    try:
        with urllib.request.urlopen(urllib.request.Request(url, headers={"User-Agent": CL.UA}), timeout=30) as r:
            data = r.read(limit)
        if data[:2] == b"\x1f\x8b":
            data = gzip.decompress(data)
        return data.decode("utf-8", "replace")
    except Exception:
        return None


def sitemap_urls(site, cap):
    out, seen = [], set()
    robots = fetch_xml(urllib.parse.urljoin(site, "/robots.txt"), 300_000) or ""
    queue = re.findall(r"(?im)^\s*sitemap:\s*(\S+)", robots) + [urllib.parse.urljoin(site, p) for p in ("/sitemap.xml", "/sitemap_index.xml", "/en/sitemap.xml")]
    while queue and len(seen) < 60 and len(out) < cap * 8:
        sm = queue.pop(0)
        if sm in seen:
            continue
        seen.add(sm)
        if not CL.allowed(sm):
            continue
        txt = fetch_xml(sm)
        if not txt:
            continue
        index = "<sitemapindex" in txt[:3000].lower()
        for loc in re.findall(r"<loc>\s*([^<\s]+)\s*</loc>", txt):
            loc = html.unescape(loc)
            if index or loc.endswith(".xml") or ".xml?" in loc or loc.endswith(".xml.gz"):
                if re.search(r"custom|case|stor|client|success|temoign|etude", loc, re.I):
                    queue.insert(0, loc)  # the sitemap of the customer stories first
                elif len(queue) < 80:
                    queue.append(loc)
            elif STORY.search(urllib.parse.urlparse(loc).path) and not NOT_STORY.search(loc):
                out.append(loc.split("#")[0])
    best = {}
    for u in out:  # one URL per story: the same story in other languages (/fr/, /zh/, /en-gb/ ...) counts once, English first
        p = urllib.parse.urlparse(u).path
        m = re.match(r"^/([a-z]{2}(?:[-_][a-zA-Z]{2})?)(/.*)$", p)
        loc, rest = (m.group(1).lower(), m.group(2)) if m else ("", p)
        k = rest.rstrip("/").lower()
        rank = 0 if loc in ("", "en", "en-us", "en-ca") else 1
        if k not in best or rank < best[k][0]:
            best[k] = (rank, u)
    return [u for r, u in sorted(best.values())][:cap]


def name_from(title, h1, vendor_words):
    for t in [h1, title]:
        t = re.sub(r"\s+", " ", html.unescape(t or "")).strip()
        if not t:
            continue
        for rx in TITLE_PATTERNS:
            m = re.search(rx, t, re.I)
            if m:
                cand = (m.group(2) if m.lastindex and m.lastindex >= 2 and re.match(r"(case study|customer story|success story|étude de cas)", m.group(1), re.I) else m.group(1)).strip(" .,:;|-–")
                if 2 <= len(cand) <= 60 and not any(w in cand.lower() for w in vendor_words) and not re.search(r"^(the|our|why|what|customer|case)", cand, re.I):
                    return cand
    return ""


def one(vendor, cap, meta=None):
    """vendor: a host (HQ list) or, with meta, a crawler-list row (buyer_key v:/wd:/osm:, buyer_name, known_website)"""
    meta = meta or {}
    site = meta.get("known_website") or ("https://www." + vendor if vendor.count(".") == 1 else "https://" + vendor)
    vhost = CL.base(urllib.parse.urlparse(site).hostname)
    basis = (meta.get("buyer_key") or "hq:").split(":")[0]
    vname = meta.get("buyer_name") or vhost
    proof = ""  # the vendor's Canadian address on its own site (needed before a dated story counts as a dated record)
    if basis not in ("v", "hq"):
        try:
            from small_sources import canada_address_on_site
            proof, _ = canada_address_on_site(site, max_pages=4)
        except Exception:
            proof = ""
    vwords = [w for w in re.split(r"[^a-z]+", vhost.split(".")[0]) if len(w) >= 4]
    urls = sitemap_urls(site, cap)
    n_site = n_name = 0
    for u in urls:
        if not CL.allowed(u):
            continue
        page, final = CL.fetch(u)
        if not page:
            continue
        title = re.search(r"(?is)<title>(.*?)</title>", page)
        h1 = re.search(r"(?is)<h1[^>]*>(.*?)</h1>", page)
        title = re.sub(r"(?s)<[^>]+>", " ", title.group(1)) if title else ""
        h1 = re.sub(r"(?s)<[^>]+>", " ", h1.group(1)) if h1 else ""
        body = re.sub(r"(?is)<(header|nav|footer|aside)\b.*?</\1>", " ", page)
        doms = collections.Counter()
        labels = {}
        for href, label in CL.anchors(body, final):
            h = CL.base(urllib.parse.urlparse(href).hostname)
            if not h or h == vhost or h.endswith("." + vhost) or CL.SKIP.search(h) or "." not in h:
                continue
            doms[h] += 1
            labels.setdefault(h, label)
        name = name_from(title, h1, vwords)
        date = re.search(r'"datePublished"\s*:\s*"(\d{4}-\d{2}-\d{2})', page) or re.search(r'article:published_time"\s+content="(\d{4}-\d{2}-\d{2})', page)
        date = date.group(1) if date else ""
        # the customer's site: an external domain the story links to that echoes the customer's name, else the only one
        cust = ""
        nw = [w for w in re.split(r"[^a-z0-9]+", CL.base(name).lower() if name else "") if len(w) >= 3]
        for h, c in doms.most_common():
            if nw and any(w in h for w in nw):
                cust = h
                break
        if not cust and len(doms) == 1:
            cust = next(iter(doms))
        row = {"relationship_page": final, "page_title": re.sub(r"\s+", " ", title).strip()[:160], "client_label": name[:120],
               "story_date": date, "vendor_site": site, "pass": "customer_story", "vendor_basis": basis, "vendor_canada_address": proof}
        with lock:
            if cust:
                n_site += 1
                with open(os.path.join(LEADS, "socrata_stories.jsonl"), "a", encoding="utf-8") as f:
                    f.write(json.dumps({"platform": "vendor_site", "domain": cust, "dataset_id": final, "dataset": "customer story of a Canada-located vendor",
                                        "dataset_url": final, "publisher": name[:120] or cust, "buyer_unit": "", "website": "https://%s/" % cust, "vendor": vname,
                                        "canada_field": "vendor located in Canada (stories; %s)" % {"v": "contract data vendor country", "hq": "Canada-HQ list",
                                                                                                     "wd": "Wikidata country + address on its site", "osm": "OpenStreetMap + address on its site"}.get(basis, basis),
                                        "canada_value": proof or vhost, "row": row}, ensure_ascii=False) + "\n")
            elif name:
                n_name += 1
                with open(os.path.join(LEADS, "logo_names_9stories.jsonl"), "a", encoding="utf-8") as f:
                    f.write(json.dumps({"name": name, "vendor": vhost, "vendor_key": "stories:" + vhost, "vendor_site": site, "page": final}, ensure_ascii=False) + "\n")
                with open(os.path.join(LEADS, "socrata_stories_named.jsonl"), "a", encoding="utf-8") as f:  # website found later by site_finder_names
                    f.write(json.dumps({"platform": "vendor_site_story", "domain": "", "dataset_id": final, "dataset": "customer story of a Canada-located vendor",
                                        "dataset_url": final, "publisher": name[:120], "buyer_unit": "", "website": "", "vendor": vname,
                                        "canada_field": "vendor located in Canada (stories; %s)" % basis, "canada_value": proof or vhost, "row": row}, ensure_ascii=False) + "\n")
    with lock:
        with open(os.path.join(LEADS, "stories.done"), "a") as f:
            f.write("%s\t%d\t%d\t%d\n" % (vendor, len(urls), n_site, n_name))
    print(vendor, len(urls), "story pages,", n_site, "with a customer site,", n_name, "name only", flush=True)


def main():
    a = argparse.ArgumentParser()
    a.add_argument("--per-vendor", type=int, default=600)
    a.add_argument("--workers", type=int, default=8)
    a.add_argument("--vendors", default="")
    a.add_argument("--vendors-file", nargs="*", default=[], help="crawler lists (buyer_key, buyer_name, known_website): every vendor site in them")
    a.add_argument("--shard", type=int, default=0)
    a.add_argument("--of", type=int, default=1)
    a = a.parse_args()
    done = set(l.split("\t")[0] for l in open(os.path.join(LEADS, "stories.done"))) if os.path.exists(os.path.join(LEADS, "stories.done")) else set()
    if a.vendors_file:
        import csv, hashlib
        vendors, seen = [], set()
        for f in a.vendors_file:
            for r in csv.DictReader(open(os.path.expanduser(f), encoding="utf-8-sig", errors="replace")):
                h = CL.base(urllib.parse.urlparse(r.get("known_website") or "").hostname)
                if h and h not in seen and h not in done and int(hashlib.sha1(h.encode()).hexdigest(), 16) % a.of == a.shard:
                    seen.add(h); vendors.append((h, r))
        print("shard %d: %d vendor sites" % (a.shard, len(vendors)), flush=True)
        with ThreadPoolExecutor(a.workers) as ex:
            list(ex.map(lambda hv: one(hv[0], a.per_vendor, hv[1]), vendors))
        return
    vendors = [v for v in dict.fromkeys((a.vendors.split(",") if a.vendors else VENDORS)) if v and v not in done]
    with ThreadPoolExecutor(a.workers) as ex:
        list(ex.map(lambda v: one(v, a.per_vendor), vendors))


if __name__ == "__main__":
    main()
