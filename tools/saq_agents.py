#!/usr/bin/env python3
"""Producers abroad (and in Canada) represented in Québec by a Canadian promotional agent: the Société des alcools du Québec's own product pages
(no AI).

Every wine, beer or spirit the SAQ (a Québec Crown corporation) sells has a public product page that names its producer ("Producteur") and the
promotional agent that represents it in Québec ("Agent promotionnel": a Québec agency — Breakthru Canada, Univins, Sélections François Fréchette,
Charton Hobbs …), with the country and region of the product. The agent is the producer's representative in Québec and is paid by it: a
relationship between a Canadian vendor and an organisation anywhere, published by a public body, current for as long as the product is listed.
Measured on 300 product pages (2026-11-13): 269 name a producer, 249 an agent; 254 different producers in 269 products; France 129, Italy 33,
United States 19, Canada 18, Spain 14 …; 78 different agents.

  pull  --shard K/N --minutes M   the product pages of the SAQ's own product sitemap (robots.txt obeyed, the project's reader: one request a second
                                  a runner) not read before -> out/saq_K.jsonl (code, name, country, region, producer, agent, format, colour, url, read)
  merge DIR                       -> data/incoming/claude/saq/saq_products.csv.gz (one line per product, the newest read wins) + saq_done.tsv
  producers                       -> data/incoming/claude/saq/saq_producers.csv (producer, country, the agents that represent it, products, a sample)
"""
import argparse, collections, csv, glob, gzip, html, json, os, re, sys, time

csv.field_size_limit(1 << 30)
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import ap_crawler as C  # noqa: E402

INC = os.path.join(ROOT, "data/incoming/claude")
DIR = os.path.join(INC, "saq")
PRODUCTS = os.path.join(DIR, "saq_products.csv.gz")
DONE = os.path.join(DIR, "saq_done.tsv")
PRODUCERS = os.path.join(DIR, "saq_producers.csv")
SITEMAP = "https://www.saq.com/media/sitemaps/fr/sitemap_product.xml"
TODAY = time.strftime("%Y-%m-%d")
FIELDS = ["Pays", "Région", "Appellation d'origine", "Désignation réglementée", "Classification", "Cépage", "Cépages", "Producteur", "Agent promotionnel",
          "Code SAQ", "Code CUP", "Format", "Couleur", "Degré d'alcool", "Taux de sucre", "Produit du Québec", "Producteur-transformateur", "Particularité"]
COLS = ["code", "name", "country", "region", "producer", "agent", "format", "colour", "url", "read"]


def product_urls():
    st, ct, data, final = C.fetch(SITEMAP)
    if st != 200 or not data:
        sys.exit("SAQ product sitemap not read (%s)" % st)
    urls = []
    for sm in re.findall(r"<loc>\s*([^<\s]+)\s*</loc>", data.decode("utf-8", "replace")):
        if not C.allowed(sm):
            continue
        st2, ct2, d2, f2 = C.fetch(sm, 30_000_000)
        if st2 == 200 and d2:
            urls += re.findall(r"<loc>\s*(https://www\.saq\.com/fr/\d+)\s*</loc>", d2.decode("utf-8", "replace"))
    return list(dict.fromkeys(urls))


def parse(raw, url):
    t = re.sub(r"\s+", " ", C.visible(raw))
    rec = {"url": url, "code": url.rstrip("/").rsplit("/", 1)[-1], "read": TODAY}
    m = re.search(r"<h1[^>]*>(.*?)</h1>", raw, re.S)
    rec["name"] = re.sub(r"<[^>]+>|\s+", " ", m.group(1)).strip()[:160] if m else ""
    got = {}
    for f in FIELDS:
        j = t.find(" " + f + " ")
        if j < 0:
            continue
        rest = t[j + len(f) + 2:]
        nxt = min([rest.find(" " + g + " ") for g in FIELDS if rest.find(" " + g + " ") >= 0] + [140])
        got[f] = rest[:nxt].strip()[:140]
    rec.update(country=got.get("Pays", ""), region=got.get("Région", ""), producer=got.get("Producteur", ""), agent=got.get("Agent promotionnel", ""),
               format=got.get("Format", ""), colour=got.get("Couleur", ""))
    return rec


def cmd_pull(a):
    k, n = (int(x) for x in a.shard.split("/"))
    done = set()
    if os.path.exists(DONE):
        done = {l.split("\t", 1)[0] for l in open(DONE, encoding="utf-8") if l.strip()}
    urls = [u for u in product_urls() if u.rstrip("/").rsplit("/", 1)[-1] not in done]
    mine = [u for i, u in enumerate(sorted(urls)) if i % n == k]
    print("SAQ: %d product pages in the sitemap not read before; %d for shard %s" % (len(urls), len(mine), a.shard), flush=True)
    os.makedirs("out", exist_ok=True)
    deadline = time.time() + a.minutes * 60
    cnt = collections.Counter()
    with open("out/saq_%d.jsonl" % k, "a", encoding="utf-8") as f:
        for u in mine:
            if time.time() > deadline:
                break
            if not C.allowed(u):
                cnt["robots"] += 1
                continue
            st, ct, data, final = C.fetch(u)
            if st != 200 or not data:
                f.write(json.dumps({"url": u, "code": u.rstrip("/").rsplit("/", 1)[-1], "status": "http_%s" % st, "read": TODAY}) + "\n")
                cnt["http_%s" % st] += 1
                continue
            rec = parse(html.unescape(data.decode("utf-8", "replace")), u)
            rec["status"] = "ok"
            f.write(json.dumps(rec, ensure_ascii=False) + "\n")
            cnt["with a producer" if rec.get("producer") else "no producer named"] += 1
            cnt["with an agent"] += bool(rec.get("agent"))
            time.sleep(max(0.0, a.pause))
    print("SAQ shard %s: %s" % (a.shard, dict(cnt)), flush=True)


def cmd_merge(a):
    recs = {}
    for p in sorted(glob.glob(os.path.join(a.dir, "**", "saq_*.jsonl"), recursive=True)):
        for l in open(p, encoding="utf-8"):
            try:
                o = json.loads(l)
            except ValueError:
                continue
            if o.get("code"):
                recs[o["code"]] = o
    os.makedirs(DIR, exist_ok=True)
    old = {}
    if os.path.exists(PRODUCTS):
        with gzip.open(PRODUCTS, "rt", encoding="utf-8", newline="") as f:
            old = {r["code"]: r for r in csv.DictReader(f)}
    n_new = 0
    for c, o in recs.items():
        if o.get("status") == "ok":
            old[c] = {k: o.get(k, "") for k in COLS}
            n_new += 1
    with gzip.open(PRODUCTS, "wt", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=COLS)
        w.writeheader()
        for c in sorted(old):
            w.writerow(old[c])
    with open(DONE, "a", encoding="utf-8") as f:
        for c, o in sorted(recs.items()):
            f.write("%s\t%s\t%s\n" % (c, o.get("status", ""), o.get("read", TODAY)))
    print("SAQ merge: %d product pages read this run, %d products on file -> %s" % (len(recs), len(old), os.path.relpath(PRODUCTS, ROOT)), flush=True)
    cmd_producers(a)


def cmd_producers(a):
    if not os.path.exists(PRODUCTS):
        print("no products on file"); return
    by = collections.defaultdict(lambda: {"agents": collections.Counter(), "n": 0, "sample": None, "regions": collections.Counter()})
    with gzip.open(PRODUCTS, "rt", encoding="utf-8", newline="") as f:
        for r in csv.DictReader(f):
            p, cc = (r.get("producer") or "").strip(), (r.get("country") or "").strip()
            if not p or not r.get("agent"):
                continue
            g = by[(p, cc)]
            g["agents"][r["agent"].strip()] += 1
            g["n"] += 1
            g["regions"][r.get("region") or ""] += 1
            if g["sample"] is None or r["read"] > g["sample"]["read"]:
                g["sample"] = r
    with open(PRODUCERS, "w", encoding="utf-8", newline="") as f:
        w = csv.writer(f)
        w.writerow(["producer", "country", "region", "agent", "agents", "products", "sample_code", "sample_name", "sample_url", "read"])
        for (p, cc), g in sorted(by.items()):
            ag = g["agents"].most_common()
            s = g["sample"]
            w.writerow([p, cc, g["regions"].most_common(1)[0][0], ag[0][0], " | ".join("%s (%d)" % x for x in ag), g["n"], s["code"], s["name"], s["url"], s["read"]])
    print("SAQ producers with an agent: %d (%d abroad) -> %s" % (len(by), sum(1 for (p, cc) in by if cc and cc != "Canada"), os.path.relpath(PRODUCERS, ROOT)), flush=True)


def cmd_left(a):
    """the number of product pages of the sitemap not read yet (the workflow starts again while some are left)"""
    done = set()
    if os.path.exists(DONE):
        done = {l.split("\t", 1)[0] for l in open(DONE, encoding="utf-8") if l.strip()}
    print(sum(1 for u in product_urls() if u.rstrip("/").rsplit("/", 1)[-1] not in done))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("cmd", choices=["pull", "merge", "producers", "left"])
    ap.add_argument("dir", nargs="?", default="shards")
    ap.add_argument("--shard", default="0/1")
    ap.add_argument("--minutes", type=float, default=330)
    ap.add_argument("--pause", type=float, default=0.0, help="seconds to wait between pages, beyond the reader's own pace")
    a = ap.parse_args()
    {"pull": cmd_pull, "merge": cmd_merge, "producers": cmd_producers, "left": cmd_left}[a.cmd](a)


if __name__ == "__main__":
    main()
