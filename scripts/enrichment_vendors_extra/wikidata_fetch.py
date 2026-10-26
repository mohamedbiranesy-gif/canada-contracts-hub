#!/usr/bin/env python3
"""Fetch Canadian organisations from the Wikidata Query Service (polite: >= 1.5 s between queries, back-off on 429/5xx).

usage: python3 -I wikidata_fetch.py <outdir>
Step 1 collects item IDs: headquartered in Canada (P159 -> P17=Q16); country=Canada (P17=Q16) with any organisational property
(LEI, stock exchange, parent org, industry, employees, Canada Business Number, NEQ, Canadian corporation number, legal form,
revenue, CEO) or instance-of one of a list of organisation classes.
Step 2 fetches, in batches of 250 items, labels/aliases (en, fr), and the values of the properties of interest.
Raw SPARQL JSON responses are kept (gzip) in <outdir>/raw/.
"""
import sys, os, json, gzip, time, urllib.request, urllib.parse, urllib.error

OUT = sys.argv[1]
RAW = os.path.join(OUT, "raw")
os.makedirs(RAW, exist_ok=True)
EP = "https://query.wikidata.org/sparql"
UA = "contracts-research/1.0 (public-sector contract vendor enrichment; batch queries <= 1/s)"
LOG = open(os.path.join(OUT, "fetch.log"), "a")
last = [0.0]


def log(*a):
    LOG.write(time.strftime("%Y-%m-%dT%H:%M:%SZ ", time.gmtime()) + " ".join(str(x) for x in a) + "\n")
    LOG.flush()


def sparql(q, tag):
    fn = os.path.join(RAW, tag + ".json.gz")
    if os.path.exists(fn):
        return json.load(gzip.open(fn, "rt"))
    for attempt in range(6):
        wait = 1.5 - (time.time() - last[0])
        if wait > 0:
            time.sleep(wait)
        last[0] = time.time()
        try:
            req = urllib.request.Request(EP, data=urllib.parse.urlencode({"query": q}).encode(), headers={
                "User-Agent": UA, "Accept": "application/sparql-results+json", "Content-Type": "application/x-www-form-urlencoded"})
            body = urllib.request.urlopen(req, timeout=90).read()
            j = json.loads(body)
            with gzip.open(fn, "wt") as f:
                json.dump(j, f)
            log("ok", tag, len(j["results"]["bindings"]))
            return j
        except urllib.error.HTTPError as e:
            ra = e.headers.get("Retry-After") if e.headers else None
            log("http", e.code, tag, "retry-after", ra)
            time.sleep(min(int(ra) if ra and ra.isdigit() else 30 * (attempt + 1), 180))
        except Exception as e:
            log("err", tag, repr(e)[:200])
            time.sleep(20 * (attempt + 1))
    log("GAVE UP", tag)
    return None


def qid(uri):
    return uri.rsplit("/", 1)[1]


items = set()
seeds = {"hq_canada": "SELECT DISTINCT ?item WHERE { ?item wdt:P159 ?hq . ?hq wdt:P17 wd:Q16 . }"}
for p in ["P1278", "P414", "P749", "P452", "P1128", "P8860", "P10503", "P13850", "P1454", "P2139", "P169", "P355", "P1037"]:
    seeds["prop_" + p] = "SELECT DISTINCT ?item WHERE { ?item wdt:P17 wd:Q16 ; wdt:%s [] . }" % p
for c in ["Q4830453", "Q783794", "Q891723", "Q6881511", "Q163740", "Q708676", "Q658255", "Q43229", "Q2085381", "Q1058914", "Q210167",
          "Q46970", "Q22687", "Q4539", "Q178790", "Q48204", "Q157031", "Q31855", "Q3918", "Q189004", "Q16917", "Q613142", "Q1331793",
          "Q18388277", "Q1616075", "Q11032", "Q1137109", "Q15911314", "Q167037", "Q2659904", "Q327333", "Q484652", "Q7278", "Q1110684"]:
    seeds["class_" + c] = "SELECT DISTINCT ?item WHERE { ?item wdt:P17 wd:Q16 ; wdt:P31 wd:%s . }" % c
for tag, q in seeds.items():
    j = sparql(q, "seed_" + tag)
    if j:
        for b in j["results"]["bindings"]:
            items.add(qid(b["item"]["value"]))
    log("seed", tag, "items so far", len(items))
items = sorted(items, key=lambda x: int(x[1:]))
json.dump(items, open(os.path.join(OUT, "items.json"), "w"))
log("TOTAL ITEMS", len(items))

PROPS = ["P856", "P1278", "P749", "P452", "P571", "P1128", "P159", "P17", "P31", "P8860", "P10503", "P13850", "P1454", "P1329", "P968",
         "P6375", "P281", "P355", "P127", "P2139", "P576", "P1448", "P1813", "P2002", "P4264", "P3500"]
B = 250
for k in range(0, len(items), B):
    batch = items[k:k + B]
    vals = " ".join("wd:" + x for x in batch)
    qlab = """SELECT ?item ?l ?a WHERE { VALUES ?item { %s }
      { ?item rdfs:label ?l FILTER(LANG(?l) IN ("en","fr")) } UNION { ?item skos:altLabel ?a FILTER(LANG(?a) IN ("en","fr")) } }""" % vals
    sparql(qlab, "labels_%06d" % k)
    qp = """SELECT ?item ?p ?v ?vl WHERE { VALUES ?item { %s } VALUES ?p { %s } ?item ?p ?v .
      OPTIONAL { ?v rdfs:label ?vl FILTER(LANG(?vl)="en") } }""" % (vals, " ".join("wdt:" + p for p in PROPS))
    sparql(qp, "props_%06d" % k)
    qt = """SELECT ?item ?exch ?exchl ?ticker ?hq ?hql ?hqc WHERE { VALUES ?item { %s }
      { ?item p:P414 ?st . ?st ps:P414 ?exch . OPTIONAL { ?st pq:P249 ?ticker } OPTIONAL { ?exch rdfs:label ?exchl FILTER(LANG(?exchl)="en") } }
      UNION { ?item wdt:P159 ?hq . OPTIONAL { ?hq rdfs:label ?hql FILTER(LANG(?hql)="en") } OPTIONAL { ?hq wdt:P17 ?hqc } } }""" % vals
    sparql(qt, "ticker_hq_%06d" % k)
    log("batch", k, "of", len(items))
log("DONE")
