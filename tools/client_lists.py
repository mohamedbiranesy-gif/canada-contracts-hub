#!/usr/bin/env python3
"""New buyers from the relationship pages of Canada-located vendors' own websites. No AI, no search engine.

A Canadian company's "our clients", "case studies", "references", "projects", "testimonials" or "dealers / where to
buy" page names the organisations it sells to, and usually links to their websites (logo links). Each linked
organisation is a buyer of a Canada-located vendor, published by the vendor itself (page URL + quote kept as proof).
"Partners" pages are skipped: those are usually the vendor's own suppliers (the wrong direction).

Vendors read: our verified vendor sites (batch903), Wikidata organisations located in Canada (batch902) and
OpenStreetMap offices/industry in Canada (batch904), from the crawler's local work lists.
  python3 tools/client_lists.py --shard I --of N
Leads: ~/cch-leads/socrata_rel_<I>.jsonl (picked up by tools/lead_scanner.py --bridge -> tools/ap_crawler.py, which then
finds each buyer's invoicing / AP mailbox on its own site). Polite: robots.txt, one request per second per site.
"""
import argparse, csv, glob, hashlib, html, json, os, re, sys, time, urllib.error, urllib.parse, urllib.request, urllib.robotparser
from concurrent.futures import ThreadPoolExecutor

LEADS = os.path.expanduser("~/cch-leads")
UA = "canada-contracts-hub-crawler/1.0 (+https://github.com/mohamedbiranesy-gif/canada-contracts-hub)"
REL = re.compile(r"client|customer|case-stud|case_stud|casestud|reference|portfolio|our-work|projects?\b|projets?|"
                 r"realisation|réalisation|testimonial|temoignage|témoignage|trusted|success-stor|dealer|distributor|"
                 r"where-to-buy|ou-acheter|où-acheter|revendeur|distributeur|detaillant|détaillant|retailer|stockist", re.I)
NOT_REL = re.compile(r"partner|partenaire|supplier|fournisseur|career|carriere|job|emploi|login|account|cart|privacy", re.I)
SKIP = re.compile(r"facebook|linkedin|twitter|x\.com|instagram|youtube|youtu\.be|tiktok|pinterest|google|goo\.gl|apple\.com|"
                  r"microsoft|wordpress|wix|squarespace|shopify|godaddy|w3\.org|bbb\.org|iso\.org|adobe|mailchimp|hubspot|"
                  r"vimeo|flickr|yelp|tripadvisor|amazon\.|gstatic|cloudflare|jquery|bootstrap|fontawesome|gravatar|"
                  r"canada\.ca$|gc\.ca$|gouv\.qc\.ca$|wikipedia|creativecommons|github|zoom\.us|calendly|bit\.ly|addthis|sharethis", re.I)
robots, last = {}, {}


def fetch(url, limit=3_000_000):
    host = urllib.parse.urlparse(url).hostname or ""
    wait = last.get(host, 0) + 1.0 - time.time()
    if wait > 0:
        time.sleep(wait)
    last[host] = time.time()
    try:
        with urllib.request.urlopen(urllib.request.Request(url, headers={"User-Agent": UA}), timeout=20) as r:
            if "html" not in (r.headers.get("content-type") or "html"):
                return None, url
            return html.unescape(r.read(limit).decode("utf-8", "replace")), r.geturl()
    except Exception:
        return None, url


def fetch_text(url, limit=300_000):
    """Any text reply (robots.txt). None when missing or unreachable, False when refused (401/403)."""
    host = urllib.parse.urlparse(url).hostname or ""
    wait = last.get(host, 0) + 1.0 - time.time()
    if wait > 0:
        time.sleep(wait)
    last[host] = time.time()
    try:
        with urllib.request.urlopen(urllib.request.Request(url, headers={"User-Agent": UA}), timeout=20) as r:
            return r.read(limit).decode("utf-8", "replace")
    except urllib.error.HTTPError as e:
        return False if e.code in (401, 403) else None
    except Exception:
        return None


def allowed(url):
    p = urllib.parse.urlparse(url)
    key = "%s://%s" % (p.scheme, p.netloc)
    if key not in robots:
        rp = urllib.robotparser.RobotFileParser()
        txt = fetch_text(key + "/robots.txt", 300_000)  # robots.txt is text/plain: fetch() keeps only HTML
        if txt is False:
            rp.disallow_all = True  # robots.txt refused (401/403): stay out, as urllib.robotparser does
        rp.parse((txt or "").lstrip("\ufeff").splitlines())  # a robots.txt that starts with a byte-order mark keeps its first group
        robots[key] = rp
    try:
        return robots[key].can_fetch(UA, url)
    except Exception:
        return True


def base(host):
    host = (host or "").lower()
    return host[4:] if host.startswith("www.") else host


def anchors(page, pageurl):
    for m in re.finditer(r"(?is)<a\s[^>]*?href\s*=\s*[\"']([^\"'#>]+)[\"'][^>]*>(.*?)</a>", page[:2_000_000]):
        href, inner = urllib.parse.urljoin(pageurl, m.group(1).strip()), m.group(2)
        alt = re.search(r"(?is)(?:alt|title)\s*=\s*[\"']([^\"']{2,120})[\"']", m.group(0) + inner)
        text = re.sub(r"(?s)<[^>]+>", " ", inner)
        label = re.sub(r"\s+", " ", (alt.group(1) if alt else "") or text).strip()
        yield href, label


def one(v, out, done):
    site = v["known_website"].strip()
    if not site.startswith("http") or site in done:
        return
    vhost = base(urllib.parse.urlparse(site).hostname)
    hits, pages = [], []
    if allowed(site):
        home, final = fetch(site)
        if home:
            for href, label in anchors(home, final):
                p = urllib.parse.urlparse(href)
                if base(p.hostname) == vhost and REL.search(p.path + " " + label) and not NOT_REL.search(p.path + " " + label):
                    pages.append(href.split("#")[0])
    for pu in list(dict.fromkeys(pages))[:4]:
        if not allowed(pu):
            continue
        page, final = fetch(pu)
        if not page:
            continue
        title = re.search(r"(?is)<title>(.*?)</title>", page)
        title = re.sub(r"\s+", " ", title.group(1)).strip()[:120] if title else ""
        for href, label in anchors(page, final):
            h = base(urllib.parse.urlparse(href).hostname)
            if not h or h == vhost or h.endswith("." + vhost) or SKIP.search(h) or "." not in h:
                continue
            hits.append({"platform": "vendor_site", "domain": h, "dataset_id": final, "dataset": "relationship page of a Canada-located vendor",
                         "dataset_url": final, "publisher": h, "buyer_unit": "", "website": "https://%s/" % h,
                         "vendor": v.get("buyer_name") or vhost, "canada_field": "vendor located in Canada (%s)" % v["buyer_key"].split(":")[0],
                         "canada_value": vhost, "row": {"relationship_page": final, "page_title": title, "client_label": label[:120],
                                                        "vendor_key": v["buyer_key"], "vendor_site": site}})
    uniq = {h["domain"]: h for h in hits}
    if 0 < len(uniq) <= 300:  # a page linking hundreds of sites is a directory, not a client list
        with open(out, "a", encoding="utf-8") as f:
            for h in uniq.values():
                f.write(json.dumps(h, ensure_ascii=False) + "\n")
    with open(out + ".done", "a", encoding="utf-8") as f:
        f.write("%s\t%d\n" % (site, len(uniq)))


def main():
    a = argparse.ArgumentParser()
    a.add_argument("--shard", type=int, default=0)
    a.add_argument("--of", type=int, default=1)
    a.add_argument("--workers", type=int, default=24)
    a = a.parse_args()
    os.makedirs(LEADS, exist_ok=True)
    out = os.path.join(LEADS, "socrata_rel_%02d.jsonl" % a.shard)
    done = set(l.split("\t")[0] for l in open(out + ".done", encoding="utf-8")) if os.path.exists(out + ".done") else set()
    vendors = []
    for f in sorted(glob.glob(os.path.expanduser("~/cch-crawler/coord/tasks/claude/claude_buyer_ap_batch90[2-4].csv"))):
        for r in csv.DictReader(open(f, encoding="utf-8-sig")):
            h = base(urllib.parse.urlparse(r.get("known_website") or "").hostname)
            if h and int(hashlib.sha1(h.encode()).hexdigest(), 16) % a.of == a.shard:
                vendors.append(r)
    print("shard %d: %d vendor sites" % (a.shard, len(vendors)), flush=True)
    with ThreadPoolExecutor(a.workers) as ex:
        list(ex.map(lambda v: one(v, out, done), vendors))
    print("shard %d finished" % a.shard, flush=True)


if __name__ == "__main__":
    main()
