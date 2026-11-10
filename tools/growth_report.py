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
    """the delivered rows, each kept as the cells this tool reads (every column named in an r.get("…") of this file, plus the *_inferred
    columns), each string stored once. 2026-11-10, measured: whole rows cost 30 KB each in memory — 2.3 GB at 73,600 delivered rows."""
    src = open(os.path.abspath(__file__), encoding="utf-8").read()
    need = set(re.findall(r"""\br\.get\("([A-Za-z0-9_]+)"\)""", src))
    op = gzip.open if path.endswith(".gz") else open
    with op(path, "rt", encoding="utf-8", newline="") as fh:
        rd = csv.DictReader(fh)
        keep = [k for k in (rd.fieldnames or []) if k in need or k.endswith("_inferred")]
        return [{k: sys.intern(r[k] or "") for k in keep} for r in rd if r.get("email")]


def source_of(r):
    k = (r.get("keys") or "").split("|")[0]
    m = re.match(r"^([a-z0-9_]+):", k)
    return m.group(1) if m else (k.split(":")[0] if ":" in k else "")


def split_rows(by_tier):
    """the headline, split by what the relationship is (2026-11-10: tier R — the .ca registration contract — is recorded and certain but generic,
    so it is never added to the named-vendor count): a named Canada-located vendor / a registry contract / no record (inferred) or weak"""
    named = sum(c for t, c in by_tier.items() if t in ("A", "B", "T", "M", "C", "D", "L", "E"))
    return {"rows_named_vendor_relationship": named, "rows_registry_contract_R": by_tier.get("R", 0), "rows_inferred_or_weak": by_tier.get("I", 0) + by_tier.get("F", 0)}


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
    m.update(split_rows(m["rows_by_package"]))
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
    for _k, _v in split_rows(base.get("rows_by_package", {})).items():
        base.setdefault(_k, _v)
    keys = ["rows", "rows_named_vendor_relationship", "rows_registry_contract_R", "rows_inferred_or_weak", "buyers_total", "buyers_ap_confirmed", "buyers_fin_confirmed", "buyers_any_confirmed", "pay_on_sight_yes", "pay_on_sight_ref",
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
        # the list of metrics has grown since the first builds: the file is rewritten with one header that holds every column ever used, so a
        # value always sits under its own name (rows written before a metric existed leave it blank)
        old_rows, head = [], ["date", "label"]
        if os.path.exists(a.history):
            with open(a.history, encoding="utf-8", newline="") as fh:
                rd = csv.reader(fh)
                h0 = next(rd, None) or []
                for row in rd:
                    old_rows.append({h0[i]: v for i, v in enumerate(row) if i < len(h0)})
                head = h0 or head
        head = head + [k for k in keys if k not in head]
        old_rows.append(dict({"date": TODAY, "label": a.label}, **{k: cur.get(k) for k in keys}))
        with open(a.history, "w", newline="", encoding="utf-8") as fh:
            w = csv.DictWriter(fh, fieldnames=head, extrasaction="ignore")
            w.writeheader()
            w.writerows(old_rows)
    out = "\n".join(L) + "\n"
    if a.write:
        open(a.write, "w", encoding="utf-8").write(out)
    print(out)


if __name__ == "__main__":
    main()
