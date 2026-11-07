#!/usr/bin/env python3
"""Buyer-AP research batches for the human-like lanes (ChatGPT on the owner's Mac, Gemini app on the owner's Mac) from the
ranked file — owner 2026-11-06 (D1): "expand the P02/P03/P04 pool via additional search passes using the staff directory method".

Targets, in order of value for P01 Gold:
  1. tiers A/B (dated or active relationship with a Canada-located vendor) without a confirmed invoicing/AP mailbox,
     never researched by a searching lane (chatgpt / gemini / codex) first, then researched before but with no AP-grade
     result (finance-known first, then purchasing, then general, then no mailbox at all);
  2. tier T (active service seen on the buyer's own site) the same way — an AP mailbox there makes P01T;
  3. tier L (client listings) — an AP mailbox there makes P06.
Québec buyers go to Gemini (French sources), everything else to ChatGPT (US buyers are its lane; buyers outside
Canada/US sit at the end of its queue, the codex queue it takes when its own is done).

Task files use the exact 10-column format the lanes validate:
  task_id,org_group,buyer_key,buyer_name,other_spellings,country,known_website,known_general_email,known_procurement_email,contracts_in_dataset
`org_group` carries the priority wave and what is already known, so the researcher starts from the right place.
  python3 contrib/claude/lane_tasks/make_lane_batches.py [--chatgpt-from 50] [--gemini-from 44] [--max-batches 20]
"""
import argparse, collections, csv, glob, gzip, os, re, unicodedata

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
COLS = ["task_id", "org_group", "buyer_key", "buyer_name", "other_spellings", "country", "known_website", "known_general_email", "known_procurement_email", "contracts_in_dataset"]
QC_NAME = re.compile(r"\b(qu[ée]bec|montr[ée]al|laval|gatineau|sherbrooke|saguenay|l[ée]vis|trois-rivi[èe]res|longueuil|cisss|ciusss|c[ée]gep|mrc\b|municipalit[ée] (?:de|du|des|d')|"
                     r"ville de|centre de services scolaire|commission scolaire|soci[ée]t[ée] (?:de|du|des|d')|r[ée]gie|office municipal|minist[èe]re|f[ée]d[ée]ration|coop[ée]rative|"
                     r"universit[ée] (?:de|du|laval)|arrondissement|paroisse|canton de|secteur)\b", re.I)
QC_ADDR = re.compile(r"\b(QC|Qu[ée]bec|Quebec)\b|\b[GHJ]\d[A-Z] ?\d[A-Z]\d\b", re.I)  # G/H/J postal codes are Québec
AP_TYPES = ("invoice_submission", "accounts_payable", "supplier_payment")


def norm(s):
    s = unicodedata.normalize("NFKD", s or "").encode("ascii", "ignore").decode()
    return re.sub(r"[^a-z0-9]+", " ", s.lower()).strip()


def is_qc(x):
    j = x.get("jurisdiction") or ""
    if j == "QC":
        return True
    if j and j not in ("", "CA", "FED"):
        return False
    site = (x.get("buyer_website") or "").lower()
    if ".qc.ca" in site or site.endswith(".quebec") or ".quebec/" in site or site.endswith(".quebec/"):
        return True
    if QC_ADDR.search(x.get("buyer_address") or ""):
        return True
    return bool(QC_NAME.search(x.get("buyer") or ""))


def country(x):
    j = x.get("jurisdiction") or ""
    if j in ("QC", "ON", "BC", "AB", "SK", "MB", "NS", "NB", "PE", "NL", "YT", "NT", "NU", "CA", "FED"):
        return "CA"
    if j == "US":
        return "US"
    if j in ("UK", "GB"):
        return "UK"
    if j:
        return j[:3]
    a = (x.get("buyer_address") or "")
    if re.search(r"\b[A-Z]\d[A-Z] ?\d[A-Z]\d\b", a) or re.search(r"\bcanada\b", a, re.I):
        return "CA"
    if re.search(r"\b[A-Z]{2} \d{5}(?:-\d{4})?\b", a) or re.search(r"\bUSA\b|United States", a):
        return "US"
    site = (x.get("buyer_website") or "").lower()
    if re.search(r"\.(?:ca|qc\.ca|on\.ca|bc\.ca|ab\.ca|sk\.ca|mb\.ca|ns\.ca|nb\.ca|nl\.ca|pe\.ca)(?:/|$)", site) or site.endswith(".quebec"):
        return "CA"
    if re.search(r"\.(?:gov|us|edu|k12\.[a-z]{2}\.us)(?:/|$)", site):
        return "US"
    return ""


def main():
    a = argparse.ArgumentParser()
    a.add_argument("--ranked", default=os.path.join(ROOT, "coord/results/ranked/ranked_buyers.csv.gz"))
    a.add_argument("--chatgpt-from", type=int, default=50)
    a.add_argument("--gemini-from", type=int, default=44)
    a.add_argument("--max-batches", type=int, default=20, help="per lane")
    a.add_argument("--size", type=int, default=100)
    a = a.parse_args()
    rows = list(csv.DictReader(gzip.open(a.ranked, "rt", encoding="utf-8")))
    # what the lanes already did, per key: the best mailbox grade they returned
    tasked = collections.defaultdict(set)      # key -> lanes that had it in a task file
    used_ids = set()
    for f in glob.glob(os.path.join(ROOT, "coord/tasks/*/*.csv")):
        lane = f.split(os.sep)[-2]
        for r in csv.DictReader(open(f, encoding="utf-8")):
            if r.get("buyer_key"):
                tasked[r["buyer_key"].strip()].add(lane)
            if r.get("task_id"):
                used_ids.add(r["task_id"].strip())
    got_ap = set()
    for f in glob.glob(os.path.join(ROOT, "data/incoming/*/*buyer_ap*results*.csv")):
        for r in csv.DictReader(open(f, encoding="utf-8", errors="replace")):
            if (r.get("status") or "") == "found" and (r.get("ap_email_type") or "") in AP_TYPES and r.get("buyer_key"):
                got_ap.add(r["buyer_key"].strip())
    cand = []
    seen_org = set()
    for x in rows:
        t, g = x.get("tier") or "", x.get("rank_group") or ""
        if t not in ("A", "B", "T", "L") or g in ("GOLD", "GOLD-T", "GOLD-M"):
            continue
        if (x.get("email_type") or "").startswith("invoicing"):
            continue  # already an AP-grade mailbox (awaiting the referee)
        keys = [k for k in (x.get("keys") or "").split("|") if k]
        if any(k in got_ap for k in keys):
            continue
        bkey = next((k for k in keys if k.startswith("b:")), keys[0] if keys else "")
        if not bkey:
            continue
        okey = norm(x.get("buyer") or "")
        if okey in seen_org:
            continue
        seen_org.add(okey)
        lanes = set(l for k in keys for l in tasked.get(k, ()))
        researched = bool(lanes & {"chatgpt", "gemini", "codex"})
        grade = int(g[1]) if len(g) > 1 and g[1].isdigit() else 0
        tier_rank = {"A": 0, "B": 0, "T": 1, "L": 2}[t]
        # never-researched first; then by what is known (finance > purchasing > general > nothing); A/B before T before L
        prio = (tier_rank, 1 if researched else 0, {3: 0, 2: 1, 1: 2, 0: 3}.get(grade, 3), -int(float(x.get("contracts_with_canadian_suppliers") or 0)))
        wave = ("wave 1 (never researched by a lane)" if not researched else "wave 2 (researched before, no AP mailbox found: use the staff-directory method)")
        kind = {"A": "active contract with a Canadian supplier", "B": "contract with a Canadian supplier awarded in the last 12 months", "T": "Canadian supplier's service in use on the buyer's own site", "L": "listed as a client of a Canadian supplier"}[t]
        best = {3: "finance mailbox", 2: "purchasing mailbox", 1: "general mailbox", 0: "none"}.get(grade, "none")
        email = (x.get("email") or "").lower()
        et = x.get("email_type") or ""
        cand.append((prio, {
            "org_group": "%s; %s; current best: %s" % (wave, kind, best),
            "buyer_key": bkey, "buyer_name": x.get("buyer") or "",
            "other_spellings": (x.get("buyer_legal_name_as_published") or "") if norm(x.get("buyer_legal_name_as_published") or "") != okey else "",
            "country": country(x), "known_website": x.get("buyer_website") or "",
            "known_general_email": email if (et.startswith("general") or et.startswith("finance")) else "",
            "known_procurement_email": email if et.startswith("purchasing") or et.startswith("procurement") else "",
            "contracts_in_dataset": x.get("contracts_with_canadian_suppliers") or "0",
            "_qc": is_qc(x), "_outside": country(x) not in ("CA", "US", "")}))
    cand.sort(key=lambda p: (p[1]["_outside"], p[0]))
    gem = [r for _, r in cand if r["_qc"]]
    cha = [r for _, r in cand if not r["_qc"]]
    print("candidates: %d (gemini/QC %d, chatgpt %d)" % (len(cand), len(gem), len(cha)))
    stats = collections.Counter()
    for lane, lst, start, pre in (("gemini", gem, a.gemini_from, "GE-AP-"), ("chatgpt", cha, a.chatgpt_from, "CH-AP-")):
        n = 0
        for bi in range(a.max_batches):
            chunk = lst[bi * a.size:(bi + 1) * a.size]
            if not chunk:
                break
            bn = start + bi
            path = os.path.join(ROOT, "coord/tasks/%s/%s_buyer_ap_batch%02d.csv" % (lane, lane, bn))
            if os.path.exists(path):
                raise SystemExit("exists: " + path)
            with open(path, "w", newline="", encoding="utf-8") as fh:
                w = csv.DictWriter(fh, fieldnames=COLS)
                w.writeheader()
                for i, r in enumerate(chunk):
                    tid = "%s%02d%03d" % (pre, bn, i + 1)
                    assert tid not in used_ids, tid
                    w.writerow({"task_id": tid, **{k: r[k] for k in COLS if k != "task_id"}})
                    stats[(lane, r["org_group"].split(";")[0])] += 1
            n += len(chunk)
            print("wrote", path, len(chunk))
        print(lane, "tasks written:", n, "of", len(lst))
    for k, v in sorted(stats.items()):
        print(k, v)


if __name__ == "__main__":
    main()
