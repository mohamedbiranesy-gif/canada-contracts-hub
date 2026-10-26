#!/usr/bin/env python3
"""Vendor-contact batches, QA sample (record pages only), verified examples. Usage: <contracts_dir> <teamroom_dir>"""
import sys, os, json, csv, glob, gzip, random, collections

C, T = sys.argv[1], sys.argv[2]


def write_batches(prefix, header, rows, size):
    for i in range(0, len(rows), size):
        with open("%s_batch%02d.csv" % (prefix, i // size + 1), "w", newline="", encoding="utf-8") as f:
            w = csv.writer(f)
            w.writerow(header)
            w.writerows(rows[i:i + size])


# vendor contact tasks: copy from hub task files (already prioritised), re-batched by 100
for who in ("gemini", "chatgpt"):
    src = os.path.join(C, "hub/tasks/%s_vendor_contact_tasks.csv" % who)
    rd = list(csv.reader(open(src, encoding="utf-8")))
    write_batches(os.path.join(T, "TASKS", who, "%s_vendor_contacts" % who), rd[0], rd[1:], 100)
    print(who, "vendor rows", len(rd) - 1)

# QA sample: only records that have their own page
want = {"high": 70, "medium": 40, "low": 30, "very_low": 20, "unknown": 40}
pools = collections.defaultdict(list)
random.seed(77)
with gzip.open(os.path.join(C, "out_final/canadian_vendor_contracts.jsonl.gz"), "rt", encoding="utf-8") as f:
    for line in f:
        if '"link_type": "record_page"' not in line or random.random() > 0.03:
            continue
        r = json.loads(line)
        if r["status_confidence"] in want:
            pools[r["status_confidence"]].append(r)
qa = []
for c, n in want.items():
    qa += random.sample(pools[c], min(n, len(pools[c])))
hdr = ["qa_id", "record_id", "source", "link", "buyer_name", "vendor_name", "vendor_city_province", "contract_title",
       "value", "currency", "start", "end", "status", "status_confidence", "status_basis"]
rows = []
for i, r in enumerate(qa, 1):
    a = r["vendor"].get("address") or {}
    d = r["contract"].get("dates") or {}
    rows.append(["QA-%03d" % i, r["record_id"], r["source"]["name"], r["link"], r["buyer"].get("name"), r["vendor"].get("name"),
                 " ".join(x for x in [a.get("city") or "", a.get("region") or ""] if x), (r["contract"].get("title") or "")[:200],
                 r["contract"].get("value"), r["contract"].get("currency"), d.get("start"), d.get("end"), r["status"],
                 r["status_confidence"], (r.get("status_basis") or "")[:300]])
write_batches(os.path.join(T, "TASKS/chatgpt/chatgpt_qa_audit"), hdr, rows, 100)
print("qa rows", len(rows))

# verified AP examples (evidence standard) from our buyer tables
ex = []
for p in (os.path.join(C, "enrichment/buyers_enriched.jsonl"), os.path.join(C, "enrichment/v2/buyers_enriched_v2.jsonl")):
    for l in open(p, encoding="utf-8"):
        d = json.loads(l)
        ap = d.get("ap_contact") or {}
        for e in ap.get("evidence") or []:
            if e.get("page_url") and e.get("email") and len(e.get("snippet") or "") > 20:
                ex.append([d.get("canonical_name") or d.get("name"), e["email"], e["page_url"], (e.get("snippet") or "")[:220], (e.get("retrieved_at") or "")[:10]])
                break
random.seed(3)
pick = random.sample(ex, min(25, len(ex)))
with open(os.path.join(T, "DATA/verified_ap_examples.csv"), "w", newline="", encoding="utf-8") as f:
    w = csv.writer(f)
    w.writerow(["organisation", "ap_email", "evidence_url", "evidence_quote", "retrieved_date"])
    w.writerows(pick)
print("ap examples", len(pick), "of", len(ex))

# sample full records (schema + richness)
samp = []
with gzip.open(os.path.join(C, "out_final/canadian_vendor_contracts.jsonl.gz"), "rt", encoding="utf-8") as f:
    for line in f:
        if '"business_number_bn9": "' in line and '"ap_contact": {"emails": ["' in line and '"status_confidence": "high"' in line:
            samp.append(json.loads(line))
            if len(samp) >= 3:
                break
json.dump(samp, open(os.path.join(T, "DATA/sample_enriched_records.json"), "w"), indent=1, ensure_ascii=False)
print("sample records", len(samp))
