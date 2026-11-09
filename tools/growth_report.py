#!/usr/bin/env python3
"""Growth vs the ship-now baseline (owner 2026-11-09 10:45 EST: "show me that I should wait").

The baseline is the pack the owner could have shipped on 2026-11-09 (build 89b4386, 14:29Z). Every later build is measured against it on the
numbers the owner cares about, and the report says in one line whether waiting is paying. Nothing here changes the pack.
  python3 tools/growth_report.py --ranked out/ranked/ranked_buyers.csv.gz --baseline coord/BASELINE_SHIP_NOW_2026-11-09.json \
                                 --write coord/GROWTH_VS_BASELINE.md [--history coord/growth_history.csv] [--snapshot path.json]
  python3 tools/growth_report.py --ranked ... --snapshot coord/BASELINE_SHIP_NOW_2026-11-09.json     # (re)write the baseline itself
Metrics (delivered rows = rows with a mailbox):
  rows, buyers_total (distinct buyer keys), buyers_ap_confirmed (referee-confirmed invoicing / AP mailbox), buyers_fin_confirmed (finance),
  pay_on_sight_yes / _ref / _routed, gold_rows, gold_pay_on_sight, grade_A (all) / gold_A, benchmarks_met (from coverage_vs_targets.json when present),
  rows_by_package, inferred_policy_cells (rows carrying a *_inferred value at p >= 0.8, once the inference layer exists), new_sources (source keys
  seen in how_relationship_was_found / keys that the baseline did not have).
"""
import argparse, collections, csv, datetime, gzip, json, os, re, sys

csv.field_size_limit(1 << 30)
TODAY = datetime.date.today().isoformat()


def load(path):
    op = gzip.open if path.endswith(".gz") else open
    with op(path, "rt", encoding="utf-8", newline="") as fh:
        return [r for r in csv.DictReader(fh) if r.get("email")]


def source_of(r):
    k = (r.get("keys") or "").split("|")[0]
    m = re.match(r"^([a-z0-9_]+):", k)
    return m.group(1) if m else (k.split(":")[0] if ":" in k else "")


def metrics(rows, cov_json=None):
    m = collections.OrderedDict()
    m["rows"] = len(rows)
    m["buyers_total"] = len({(r.get("keys") or r.get("buyer") or "").split("|")[0] for r in rows})
    conf = lambda r: (r.get("email_check") or "").startswith(("confirmed", "cross"))
    m["buyers_ap_confirmed"] = sum(1 for r in rows if conf(r) and (r.get("email_type") or "").startswith(("invoic", "accounts_payable", "supplier_payment", "ap")))
    m["buyers_fin_confirmed"] = sum(1 for r in rows if conf(r) and (r.get("email_type") or "").startswith("finance"))
    m["buyers_any_confirmed"] = sum(1 for r in rows if conf(r))
    pos = collections.Counter(("yes" if (r.get("pay_on_sight") or "") == "yes" else "ref" if (r.get("pay_on_sight") or "").startswith("yes") else "routed" if (r.get("pay_on_sight") or "").startswith("routed") else "no") for r in rows)
    m["pay_on_sight_yes"], m["pay_on_sight_ref"], m["pay_on_sight_routed"] = pos["yes"], pos["ref"], pos["routed"]
    gold = [r for r in rows if (r.get("rank_group") or "") == "GOLD"]
    m["gold_rows"] = len(gold)
    m["gold_pay_on_sight"] = sum(1 for r in gold if (r.get("pay_on_sight") or "") == "yes")
    m["grade_A"] = sum(1 for r in rows if (r.get("ap_grade") or "") == "A")
    m["gold_A"] = sum(1 for r in gold if (r.get("ap_grade") or "") == "A")
    m["grade_A_or_B"] = sum(1 for r in rows if (r.get("ap_grade") or "") in ("A", "B"))
    inf_cols = [c for c in (rows[0].keys() if rows else []) if c.endswith("_inferred")]
    m["inferred_policy_cells_p80"] = sum(1 for r in rows for c in inf_cols if re.search(r"\(p=0\.([89]\d|[89])", r.get(c) or "") or re.search(r"\b(0\.[89]\d?|1\.00?)\b", (r.get(c) or "")[:60]))
    pub = [r for r in rows if (r.get("tier") or "") != "I"]  # public bodies / strong tiers: where AP policies are published
    m["public_rows"] = len(pub)
    m["terms_published_public"] = sum(1 for r in pub if (r.get("payment_terms_as_published") or "").strip() not in ("", "not_published"))
    m["po_rule_published_public"] = sum(1 for r in pub if (r.get("po_required_as_published") or "").strip() not in ("", "not_published"))
    m["billto_legal_name_published"] = sum(1 for r in rows if (r.get("buyer_legal_name_as_published") or "").strip())
    m["vendor_bn9_known"] = sum(1 for r in rows if (r.get("vendor_bn9") or "").strip())
    m["benchmarks_met"] = (cov_json or {}).get("met")
    m["rows_by_package"] = dict(sorted(collections.Counter(r.get("tier") or "?" for r in rows).items()))
    m["sources"] = dict(sorted(collections.Counter(source_of(r) for r in rows if source_of(r)).items()))
    return m


def main():
    a = argparse.ArgumentParser()
    a.add_argument("--ranked", required=True)
    a.add_argument("--baseline", default="coord/BASELINE_SHIP_NOW_2026-11-09.json")
    a.add_argument("--coverage-json", default="")
    a.add_argument("--write", default="")
    a.add_argument("--history", default="")
    a.add_argument("--snapshot", default="", help="write this build's metrics to the given json (used once to create the baseline)")
    a.add_argument("--label", default="")
    a = a.parse_args()
    rows = load(a.ranked)
    cov = None
    if a.coverage_json and os.path.exists(a.coverage_json):
        try:
            cov = json.load(open(a.coverage_json, encoding="utf-8"))
        except Exception:
            cov = None
    cur = metrics(rows, cov)
    cur["date"] = TODAY
    cur["label"] = a.label
    if a.snapshot:
        json.dump(cur, open(a.snapshot, "w", encoding="utf-8"), indent=1, ensure_ascii=False)
        print("snapshot written", a.snapshot, {k: v for k, v in cur.items() if not isinstance(v, dict)})
        if not a.write:
            return
    if not os.path.exists(a.baseline):
        sys.exit("no baseline at %s" % a.baseline)
    base = json.load(open(a.baseline, encoding="utf-8"))
    keys = ["rows", "buyers_total", "buyers_ap_confirmed", "buyers_fin_confirmed", "buyers_any_confirmed", "pay_on_sight_yes", "pay_on_sight_ref",
            "pay_on_sight_routed", "gold_rows", "gold_pay_on_sight", "grade_A", "gold_A", "grade_A_or_B", "public_rows", "terms_published_public", "po_rule_published_public",
            "billto_legal_name_published", "vendor_bn9_known", "inferred_policy_cells_p80", "benchmarks_met"]
    L = ["# Growth vs the ship-now baseline (%s, build %s) — measured %s" % (base.get("date"), base.get("label") or "?", TODAY), "",
         "The baseline is what could have been shipped on 2026-11-09. Waiting pays only if the right-hand columns keep moving; the owner reads this file, not the scoreboard.", "",
         "| metric | baseline | now | change |", "|---|---|---|---|"]
    for k in keys:
        b, c = base.get(k), cur.get(k)
        if b is None and c is None:
            continue
        d = (c or 0) - (b or 0)
        L.append("| %s | %s | %s | %s |" % (k, "—" if b is None else b, "—" if c is None else c, ("%+d" % d) if (b is not None and c is not None) else "—"))
    newsrc = sorted(set(cur["sources"]) - set(base.get("sources", {})))
    L += ["", "New source keys since the baseline: %s" % (", ".join(newsrc) if newsrc else "none"), ""]
    bp, cp = base.get("rows_by_package", {}), cur.get("rows_by_package", {})
    L += ["| package tier | baseline rows | now | change |", "|---|---|---|---|"]
    for t in sorted(set(bp) | set(cp)):
        L.append("| %s | %d | %d | %+d |" % (t, bp.get(t, 0), cp.get(t, 0), cp.get(t, 0) - bp.get(t, 0)))
    L.append("")
    if a.history:
        new = not os.path.exists(a.history)
        with open(a.history, "a", newline="", encoding="utf-8") as fh:
            w = csv.writer(fh)
            if new:
                w.writerow(["date", "label"] + keys)
            w.writerow([TODAY, a.label] + [cur.get(k) for k in keys])
    out = "\n".join(L) + "\n"
    if a.write:
        open(a.write, "w", encoding="utf-8").write(out)
    print(out)


if __name__ == "__main__":
    main()
