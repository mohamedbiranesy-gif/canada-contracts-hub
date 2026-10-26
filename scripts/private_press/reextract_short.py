"""Re-extract text for fetched rows whose body text was truncated by the gallery-parsing bug,
using the saved HTML copies. Rewrites the fetched_*.jsonl files in place (backup kept as .bak)."""
import json, sys, os, re, shutil
from bs4 import BeautifulSoup

# load body_soup()/extract() from fetch_releases.py without running its CLI section
_src = open("scripts/private_press/fetch_releases.py", encoding="utf-8").read()
_start = _src.find("def body_soup")
_end = _src.find("\nfor r in rows:")
ns = {"BeautifulSoup": BeautifulSoup, "re": re}
exec(compile(_src[_start:_end], "fetch_releases_defs", "exec"), ns)
extract = ns["extract"]

OUT = "downloads/private_press"
files = sys.argv[1:] or ["fetched_newswire.jsonl", "fetched_prnewswire.jsonl", "fetched_search.jsonl", "fetched_adhoc.jsonl"]
for fn in files:
    p = f"{OUT}/{fn}"
    if not os.path.exists(p):
        continue
    rows = [json.loads(l) for l in open(p, encoding="utf-8")]
    changed = 0
    for r in rows:
        hp = f"{OUT}/html/{r['sha1']}.html"
        if not os.path.exists(hp):
            continue
        html = open(hp, encoding="utf-8", errors="ignore").read()
        ex = extract(r["url"], html)
        if len(ex["text"]) > len(r.get("text") or "") + 50:
            r["text"] = ex["text"]
            r["tickers"] = ex["tickers"]
            r["dateline"] = ex["dateline"] or r.get("dateline")
            r["reextracted"] = True
            changed += 1
    shutil.copy(p, p + ".bak")
    with open(p, "w", encoding="utf-8") as f:
        for r in rows:
            f.write(json.dumps(r, ensure_ascii=False) + "\n")
    print(fn, "rows", len(rows), "re-extracted", changed)
