#!/usr/bin/env python3
"""Build TeamRoom task batches. Usage: python3 -I build_teamroom_data.py <contracts_dir> <teamroom_dir>"""
import sys, os, json, re, csv, collections, unicodedata

C, T = sys.argv[1], sys.argv[2]
for d in ("TASKS/gemini", "TASKS/chatgpt", "DATA"):
    os.makedirs(os.path.join(T, d), exist_ok=True)


def fold(s):
    return unicodedata.normalize("NFKD", s or "").encode("ascii", "ignore").decode().lower()


def org_group(name):
    n = re.split(r"\s+[-–—/|]\s+|\s*\(", name or "")[0]
    return re.sub(r"\s+", " ", re.sub(r"[^a-z0-9 ]", " ", fold(n))).strip()


def write_batches(prefix, header, rows, size):
    for i in range(0, len(rows), size):
        p = "%s_batch%02d.csv" % (prefix, i // size + 1)
        with open(p, "w", newline="", encoding="utf-8") as f:
            w = csv.writer(f)
            w.writerow(header)
            w.writerows(rows[i:i + size])
    return (len(rows) + size - 1) // size


rows = [json.loads(l) for l in open(os.path.join(C, "enrichment/v2/buyers_deep_input.jsonl"))]
groups = collections.defaultdict(list)
for b in rows:
    groups[(org_group(b["name"]), b.get("country") or "")].append(b)
ordered = sorted(groups.items(), key=lambda kv: -sum(x["record_count"] for x in kv[1]))
share = {"gemini": [], "chatgpt": [], "claude": []}
for (g, c), bs in ordered:
    qc = any("seao_quebec" in {s["value"] for s in b.get("sources") or []} for b in bs)
    who = "gemini" if (c == "CA" and qc) else ("chatgpt" if c in ("CA", "US") else "claude")
    share[who].append((g, c, bs))
hdr = ["task_id", "org_group", "buyer_key", "buyer_name", "other_spellings", "country", "known_website",
       "known_general_email", "known_procurement_email", "contracts_in_dataset"]
for who in ("gemini", "chatgpt"):
    out, n = [], 0
    for g, c, bs in share[who]:
        for b in sorted(bs, key=lambda x: -x["record_count"]):
            k = b.get("_known") or {}
            n += 1
            out.append(["%s-AP-%05d" % (who[:2].upper(), n), g, b["buyer_key"], b["name"],
                        " | ".join((b.get("name_variants") or [])[1:4]), c, k.get("official_website") or "",
                        ", ".join(((k.get("general_contact") or {}).get("emails") or [])[:2]),
                        ", ".join(((k.get("procurement_contact") or {}).get("emails") or [])[:2]), b["record_count"]])
    nb = write_batches(os.path.join(T, "TASKS", who, "%s_buyer_ap" % who), hdr, out, 100)
    print(who, "buyer AP rows", len(out), "groups", len(share[who]), "batches", nb,
          "contracts", sum(sum(x["record_count"] for x in bs) for _, _, bs in share[who]))
json.dump([{"org_group": g, "country": c, "buyer_keys": [b["buyer_key"] for b in bs]} for g, c, bs in share["claude"]],
          open(os.path.join(C, "hub/claude_buyer_ap_scope.json"), "w"))
print("claude groups", len(share["claude"]))
