#!/usr/bin/env python3
"""Every delivered buyer that still lacks a confirmed invoicing / AP mailbox, as search batches (owner, 2026-11-01: an
AP mailbox for every buyer of every package, private buyers first). Reads out/ranked/ranked_buyers.csv or
coord/results/ranked/ranked_buyers.csv; skips buyers already searched (keys in claude_search_urls_p*.csv and in
--skip files). Order: active relationships first (an AP mailbox makes them Gold), then likely active, client listings, other links,
older records. Writes B_NNN.tsv (buyers with a website: 10 sites per search) and D_NNN.tsv (no website: one
search per buyer) into <dir>.
  python3 contrib/claude/private_buyers/ap_upgrade_targets.py <dir> --b-start 402 --d-start 201 [--skip f ...] [--exclude-out x.csv N]
"""
import argparse, csv, glob, os, urllib.parse

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../.."))
a = argparse.ArgumentParser()
a.add_argument("dir")
a.add_argument("--b-start", type=int, required=True)
a.add_argument("--d-start", type=int, required=True)
a.add_argument("--skip", nargs="*", default=[], help="CSV or TSV files whose buyer_key column lists buyers already searched")
a = a.parse_args()
src = ROOT + "/out/ranked/ranked_buyers.csv"
src = src if os.path.exists(src) else ROOT + "/coord/results/ranked/ranked_buyers.csv"
rows = list(csv.DictReader(open(src, encoding="utf-8")))
done = set()
for f in glob.glob(ROOT + "/coord/tasks/claude/claude_search_urls_p*.csv") + a.skip:
    for r in csv.DictReader(open(f, encoding="utf-8", errors="replace"), delimiter="\t" if f.endswith(".tsv") else ","):
        done.add(r.get("buyer_key") or "")
OK = ("confirmed", "from dataset enrichment")


def rel(r):
    st = r["contract_status"]
    return ("inferred" if st.startswith("inferred relationship") else "weak" if st.startswith("weaker relationship") else  # P13 / P12: last
            "member" if st.startswith("member / regulated payer") else
            "client" if st.startswith("client listing") else "other_link" if st.startswith("linked from") else
            "older" if st.startswith(("end date unknown", "payment / subaward")) else "likely" if st.startswith("likely active (awarded 12-36") else "active")


def prio(r):
    g, private = int(r["grade"] or 0), r["keys"].startswith("lead:")
    order = {"active": 0, "likely": 1, "client": 2, "other_link": 3, "member": 3, "older": 4, "weak": 5, "inferred": 6}[rel(r)]  # an AP mailbox turns an active one into Gold
    return (order, -g)


todo = [r for r in rows if r["rank_group"] != "GOLD" and not (r["grade"] == "4" and r["email_check"] in OK)
        and not any(k in done for k in r["keys"].split("|"))]
todo.sort(key=prio)
bs, ds = [], []
for r in todo:
    h = (urllib.parse.urlparse(r["buyer_website"]).hostname or "").lower().removeprefix("www.")
    (bs if h else ds).append((r, h))
os.makedirs(a.dir, exist_ok=True)
for i in range(0, len(bs), 330):
    with open(os.path.join(a.dir, "B_%03d.tsv" % (a.b_start + i // 330)), "w", encoding="utf-8") as f:
        f.write("buyer_key\tbuyer\tjurisdiction\twebsite_host\ttier\tknown_email\n")
        for r, h in bs[i:i + 330]:
            f.write("\t".join([r["keys"].split("|")[0], r["buyer"].replace("\t", " ")[:100], r["jurisdiction"], h, r["tier"], r["email"]]) + "\n")
for i in range(0, len(ds), 45):
    with open(os.path.join(a.dir, "D_%03d.tsv" % (a.d_start + i // 45)), "w", encoding="utf-8") as f:
        f.write("buyer_key\tbuyer\tvendor\n")
        for r, h in ds[i:i + 45]:
            f.write("\t".join([r["keys"].split("|")[0], r["buyer"].replace("\t", " ")[:100], r["vendor"].replace("\t", " ")[:60]]) + "\n")
print("buyers without a confirmed AP mailbox, not yet searched: %d with a website (%d B files), %d without (%d D files)"
      % (len(bs), (len(bs) + 329) // 330, len(ds), (len(ds) + 44) // 45))
