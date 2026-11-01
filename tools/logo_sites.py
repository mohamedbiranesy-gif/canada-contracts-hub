#!/usr/bin/env python3
"""Websites for client names shown as logos (no link) on Canada-located vendors' client pages. No AI.

tools/client_lists2.py records the alt text of client logos that carry no link (~/cch-leads/logo_names_*.jsonl). This
looks each distinct name up in Wikidata (tools/site_finder_quick.py: exact label or alias of an item in Canada or the US
that has an official website) and writes a relationship lead with that website, so the crawler and the page readers can
find the client's invoicing mailbox. Loops: new names are picked up every 20 minutes.
  python3 tools/logo_sites.py
Output: ~/cch-leads/socrata_rel3_logos.jsonl ; cache of looked-up names: ~/cch-leads/logo_names_done.tsv
"""
import glob, json, os, re, sys, time, urllib.parse
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import site_finder_quick as SF

LEADS = os.path.expanduser("~/cch-leads")
OUT = os.path.join(LEADS, "socrata_rel3_logos.jsonl")
DONE = os.path.join(LEADS, "logo_names_done.tsv")
JUNK = re.compile(r"case study|award|partner|certif|member|winner|people|person|team|photo|participants|logo|image|"
                  r"video|play|icon|banner|background|slide|thumbnail", re.I)


def main():
    while True:
        done = {}
        if os.path.exists(DONE):
            for line in open(DONE, encoding="utf-8"):
                p = line.rstrip("\n").split("\t")
                if len(p) >= 2:
                    done[p[0]] = p[1]
        seen = {}
        for f in glob.glob(os.path.join(LEADS, "logo_names_[0-9]*.jsonl")):
            for line in open(f, encoding="utf-8", errors="replace"):
                try:
                    r = json.loads(line)
                except ValueError:
                    continue
                n = SF.norm(r["name"])
                if n and n not in seen and not JUNK.search(r["name"]) and 2 <= len(n.split()) <= 8:
                    seen[n] = r
        todo = [(n, r) for n, r in seen.items() if n not in done]
        print(time.strftime("%H:%M"), "logo names: %d distinct, %d to look up" % (len(seen), len(todo)), flush=True)
        for n, r in todo:
            hit = SF.find(r["name"])
            with open(DONE, "a", encoding="utf-8") as f:
                f.write("%s\t%s\n" % (n, hit[0] if hit else ""))
            if not hit:
                continue
            h = (urllib.parse.urlparse(hit[0]).hostname or "").lower()
            h = h[4:] if h.startswith("www.") else h
            vh = (urllib.parse.urlparse(r["vendor_site"]).hostname or "").lower().removeprefix("www.")
            if not h or h == vh:
                continue
            with open(OUT, "a", encoding="utf-8") as f:
                f.write(json.dumps({"platform": "vendor_site", "domain": h, "dataset_id": r["page"], "dataset": "relationship page of a Canada-located vendor",
                                    "dataset_url": r["page"], "publisher": h, "buyer_unit": "", "website": hit[0], "vendor": r["vendor"],
                                    "canada_field": "vendor located in Canada (%s)" % r["vendor_key"].split(":")[0], "canada_value": vh,
                                    "row": {"relationship_page": r["page"], "client_label": r["name"][:120], "vendor_key": r["vendor_key"],
                                            "vendor_site": r["vendor_site"], "wikidata": hit[1], "pass": "logo"}}, ensure_ascii=False) + "\n")
        time.sleep(1200)


if __name__ == "__main__":
    main()
