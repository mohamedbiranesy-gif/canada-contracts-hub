#!/usr/bin/env python3
"""Official websites for lead buyers that have none, from the Clearbit company-name autocomplete, verified. No AI.

For each dated lead buyer without a website (~/cch-leads/socrata_*.jsonl, record dated in the last 36 months), the free
public endpoint https://autocomplete.clearbit.com/v1/companies/suggest?query=<name> (no key, one request per second)
proposes companies with their domain. A domain is kept only when (1) the suggestion's name equals the buyer's name
once legal suffixes, accents, case and punctuation are ignored, and (2) the domain's home page answers (robots.txt
respected) and its <title> or og:site_name contains the buyer's distinctive words. Domains of directories and shared
platforms are never kept. Results go to ~/cch-crawler-state/websites.tsv (buyer_key, website, "clearbit:<name>"), the
file tools/ap_crawler.py and tools/crawl_some.py already read, and to ~/cch-crawl-some/sited_leads.csv (a task list for
tools/crawl_some.py). Progress: ~/cch-crawler-state/site_names_done.tsv.
  python3 tools/site_finder_names.py [--sources dian lobby ...]
"""
import argparse, csv, glob, hashlib, html, json, os, re, sys, time, unicodedata, urllib.parse, urllib.request

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import client_lists as CL

LEADS = os.path.expanduser("~/cch-leads")
STATE = os.path.expanduser("~/cch-crawler-state")
OUT = os.path.join(STATE, "websites.tsv")
DONE = os.path.join(STATE, "site_names_done.tsv")
TASKS = os.path.expanduser("~/cch-crawl-some/sited_leads.csv")
UA = "canada-contracts-hub-sitefinder/1.0 (+https://github.com/mohamedbiranesy-gif/canada-contracts-hub)"
LEGAL = re.compile(r"\b(inc|incorporated|ltd|limited|llc|l l c|lp|llp|plc|corp|corporation|co|company|sa|s a|sas|s a s|"
                   r"ltda|gmbh|ag|bv|nv|spa|srl|oy|ab|as|pty|ulc|ltee|the|de|del|la|el|y|and|et|group|holdings?)\b")
BAD = re.compile(r"linkedin|facebook|wikipedia|crunchbase|bloomberg|zoominfo|dnb\.com|yelp|indeed|glassdoor|"
                 r"opencorporates|wix|squarespace|godaddy|shopify|wordpress|google|apple|amazon", re.I)
CUTOFF = time.strftime("%Y-%m-%d", time.localtime(time.time() - 3 * 365 * 86400))
_last = [0.0]


def norm(s):
    s = unicodedata.normalize("NFKD", s or "").encode("ascii", "ignore").decode().lower()
    s = re.sub(r"[^a-z0-9]+", " ", s)
    return re.sub(r"\s+", " ", LEGAL.sub(" ", s)).strip()


def suggest(name):
    wait = _last[0] + 1.0 - time.time()
    if wait > 0:
        time.sleep(wait)
    _last[0] = time.time()
    url = "https://autocomplete.clearbit.com/v1/companies/suggest?query=" + urllib.parse.quote(name[:80])
    try:
        with urllib.request.urlopen(urllib.request.Request(url, headers={"User-Agent": UA}), timeout=15) as r:
            return json.loads(r.read().decode("utf-8", "replace"))
    except Exception:
        return []


def verified(domain, n):
    site = "https://%s/" % domain
    if not CL.allowed(site):
        return False
    page, final = CL.fetch(site)
    if not page:
        return False
    head = page[:200_000]
    bits = re.findall(r"(?is)<title[^>]*>(.*?)</title>", head)[:1] + \
        re.findall(r"(?is)<meta[^>]+property\s*=\s*[\"']og:site_name[\"'][^>]+content\s*=\s*[\"']([^\"']+)", head)[:1]
    text = norm(html.unescape(" ".join(bits)))
    words = [w for w in n.split() if len(w) >= 3] or n.split()
    return bool(words) and all(w in text.split() or w in text.replace(" ", "") for w in words[:3])


def main():
    a = argparse.ArgumentParser()
    a.add_argument("--sources", nargs="*", default=[])
    a = a.parse_args()
    have = set()
    if os.path.exists(OUT):
        have = {l.split("\t")[0] for l in open(OUT, encoding="utf-8")}
    done = set()
    if os.path.exists(DONE):
        done = {l.split("\t")[0] for l in open(DONE, encoding="utf-8")}
    todo = {}
    files = [os.path.join(LEADS, "socrata_%s.jsonl" % s) for s in a.sources] if a.sources else glob.glob(os.path.join(LEADS, "socrata_*.jsonl"))
    for f in files:
        if not os.path.exists(f):
            continue
        for line in open(f, encoding="utf-8", errors="replace"):
            try:
                r = json.loads(line)
            except ValueError:
                continue
            if r.get("website") or r.get("platform") in ("vendor_site", "socrata", "ckan"):
                continue
            d = max([str(v)[:10] for k, v in (r.get("row") or {}).items() if "date" in k.lower() and isinstance(v, str)] or [""])
            if d < CUTOFF:
                continue
            name = (r["publisher"] if not r.get("buyer_unit") else "%s - %s" % (r["publisher"], r["buyer_unit"])).strip()
            key = "lead:" + hashlib.sha1(("%s|%s" % (r["domain"], name.lower())).encode()).hexdigest()[:16]
            if key not in have and key not in done and len(norm(name)) >= 3:
                todo.setdefault(key, name)
    print(time.strftime("%H:%M"), "names to look up:", len(todo), flush=True)
    found = 0
    new = not os.path.exists(TASKS)
    with open(OUT, "a", encoding="utf-8") as out, open(DONE, "a", encoding="utf-8") as dn, open(TASKS, "a", newline="", encoding="utf-8") as tf:
        w = csv.writer(tf)
        if new:
            w.writerow(["task_id", "org_group", "buyer_key", "buyer_name", "other_spellings", "country", "known_website",
                        "known_general_email", "known_procurement_email", "contracts_in_dataset"])
        for i, (key, name) in enumerate(todo.items(), 1):
            n, hit = norm(name), ""
            for s in suggest(name)[:5]:
                dom = (s.get("domain") or "").lower().strip()
                if dom and not BAD.search(dom) and norm(s.get("name")) == n and verified(dom, n):
                    hit = dom
                    break
            dn.write("%s\t%s\n" % (key, hit))
            if hit:
                found += 1
                out.write("%s\thttps://%s/\tclearbit:%s\n" % (key, hit, name.replace("\t", " ")[:80]))
                w.writerow(["CL-SN-%05d" % i, "", key, name, "", "", "https://%s/" % hit, "", "", 1])
                out.flush(); tf.flush()
            dn.flush()
            if i % 200 == 0:
                print(time.strftime("%H:%M"), i, "looked up,", found, "websites", flush=True)
    print(time.strftime("%H:%M"), "finished:", len(todo), "looked up,", found, "websites", flush=True)


if __name__ == "__main__":
    main()
