#!/usr/bin/env python3
"""Recon: fetch candidate disclosure URLs (one thread per host, 1 req/s per host), save HTML, print status/title/contract links.
Usage: python3 -I recon.py <outdir> <urls.txt>   (urls.txt lines: key url)"""
import sys, os, re, time, html, threading, collections, hashlib
import requests
out, lst = sys.argv[1], sys.argv[2]
os.makedirs(out, exist_ok=True)
jobs = collections.defaultdict(list)
for line in open(lst):
    line = line.strip()
    if not line or line.startswith("#"):
        continue
    k, u = line.split(None, 1)
    jobs[re.sub(r"^https?://([^/]+).*", r"\1", u)].append((k, u))
lock = threading.Lock()
res = []
def work(host, items):
    s = requests.Session(); s.headers["User-Agent"] = "contracts-research/1.0"
    for k, u in items:
        try:
            r = s.get(u, timeout=40, allow_redirects=True)
            t = r.text
            title = re.search(r"<title[^>]*>(.*?)</title>", t, re.S | re.I)
            title = html.unescape(re.sub(r"\s+", " ", title.group(1))).strip()[:90] if title else ""
            links = sorted(set(re.findall(r'href="([^"]*(?:contract|contrat|disclosure|divulgation|procurement|approvisionnement)[^"]*)"', t, re.I)))[:12]
            fn = os.path.join(out, k + "_" + hashlib.md5(u.encode()).hexdigest()[:8] + ".html")
            open(fn, "w").write(t)
            line = f"{k} {r.status_code} {len(t)} {r.url} | {title} | {links}"
        except Exception as e:
            line = f"{k} ERR {e!r} {u}"
        with lock:
            print(line, flush=True)
        time.sleep(1.0)
ths = [threading.Thread(target=work, args=(h, it)) for h, it in jobs.items()]
[t.start() for t in ths]; [t.join() for t in ths]
