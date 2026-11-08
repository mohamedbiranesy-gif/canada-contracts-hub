#!/usr/bin/env python3
"""Scoreboard: per-package fill rate of every field the downstream team set a target for (their 2026-11-08 "Dataset coverage asks")
against that target, so every build says which benchmarks are met and how many rows each gap still needs. No AI, no network.

  python3 tools/coverage_targets.py [--batches-dir out/ranked/batches] [--ranked ranked_buyers.csv(.gz)]
                                    [--write out/ranked] [--history coord/results/coverage_history.csv]

Reads the package CSVs (one per package, as batches.py writes them); without them, reads the ranked CSV and assigns packages with
batches.py's own rules. A cell counts as filled unless it is blank or the literal not_published / not_found_yet / {} / [].
Writes COVERAGE_VS_TARGETS.md (+ .json) and appends today's numbers to the history file so progress between builds is visible.
"""
import argparse, collections, csv, datetime, glob, gzip, json, os, re, sys

csv.field_size_limit(1 << 30)
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
TODAY = datetime.date.today().isoformat()
EMPTY = {"", "not_published", "not_found_yet", "{}", "[]", "null", "None"}
DELIVERED = ["P01_GOLD", "P01T", "P01M", "P02", "P03", "P04", "P05", "P06", "P06T", "P06M", "P07", "P08", "P09", "P10", "P11", "P12", "P13"]

# field -> {package: target %}; "*" = every other delivered package the downstream team listed as "rest / all / most packages".
# None = the team's instruction is "leave at 0% / not applicable" (reported, never counted as a benchmark).
T = {
 # 1. identifiers
 "invoice_reference_hint": {"P01_GOLD": 95, "P01T": 50, "P01M": 50, "P02": 95, "P03": 95, "P04": 90, "P05": 70, "P06": 30, "P07": 30, "P08": 25, "P09": 100, "P10": 25, "P11": 60, "P12": 100, "P13": None},
 "po_number_as_published": {"P01_GOLD": 50, "P01T": 10, "P02": 50, "P03": 40, "P04": 30, "P05": 20, "P09": 50},
 "contract_or_agreement_number": {"P01_GOLD": 85, "P01T": 50, "P02": 90, "P03": 85, "P04": 85, "P05": 60, "P09": 100, "P11": 60},
 "solicitation_or_tender_number": {"P01_GOLD": 80, "P01T": 30, "P02": 60, "P03": 80, "P04": 50, "P05": 40, "P09": 50, "P11": 40, "P12": 100},
 "award_or_notice_id": {"P01_GOLD": 85, "P02": 90, "P03": 85, "P04": 85, "P05": 50, "P09": 100, "P11": 60},
 "buyer_vendor_id": {"P01_GOLD": 60, "P02": 50, "P03": 50, "P04": 40, "P05": 20, "P09": 50},
 "commodity_codes": {"P01_GOLD": 80, "P02": 90, "P03": 80, "P04": 85, "P05": 50, "P09": 95, "P11": 50},
 "buyer_org_codes": {"P01_GOLD": 50, "P02": 50, "P03": 30, "P04": 30},
 "records_with_this_vendor": {"P01_GOLD": 100, "P01T": 60, "P02": 100, "P03": 100, "P04": 95, "P05": 70, "P06": 50, "P09": 100, "P11": 70},
 # 2. vendor
 "vendor_bn9": {"P01_GOLD": 90, "P01T": 60, "P01M": 70, "P02": 85, "P03": 90, "P04": 75, "P05": 50, "P06": 40, "P07": 50, "P08": 50, "P09": 80, "P10": 40, "P11": 60, "P12": 85, "P13": None},
 "vendor_registered_address": {"P01_GOLD": 95, "P02": 95, "P03": 95, "P04": 95, "P05": 70, "P06": 80, "P07": 70, "P08": 70, "P09": 100, "P10": 70, "P11": 75},
 "vendor_trading_name": {"P01_GOLD": 60, "P02": 60, "P03": 60, "P04": 55, "P05": 50, "P07": 55, "P08": 50, "P09": 70, "P10": 55, "P11": 50},
 "vendor_phone": {"P01_GOLD": 70, "P02": 70, "P03": 70, "P04": 65, "P05": 60, "P06": 40, "P07": 85, "P08": 85, "P09": 85, "P10": 85, "P11": 75, "P13": 60},
 "vendor_website": {"P01_GOLD": 90, "P02": 90, "P03": 90, "P04": 85, "P05": 70, "P06": 50, "P07": 100, "P08": 100, "P09": 100, "P10": 100, "P11": 100},
 "vendor_emails": {"P01_GOLD": 70, "P02": 75, "P03": 75, "P04": 70, "P05": 55, "P07": 70, "P08": 75, "P09": 85, "P10": 80, "P11": 70},
 "vendor_logo_url": {"P01_GOLD": 90, "P02": 90, "P03": 90, "P04": 85, "P05": 75, "P07": 100, "P08": 100, "P10": 100},
 # 3. buyer
 "buyer_legal_name_as_published": {"P01_GOLD": 95, "P01T": 90, "P01M": 90, "P02": 95, "P03": 85, "P04": 90, "P05": 75, "P06": 80, "P07": 80, "P08": 75, "P09": 95, "P10": 70, "P11": 65, "P12": 80, "P13": 60},
 "buyer_bn_as_published": {"P01_GOLD": 40, "P01M": 50, "P02": 40, "P03": 40, "P04": 40, "P05": 25, "P06": 35, "P07": 35, "P08": 35, "P10": 30, "P13": 30},
 "buyer_address": {"P01_GOLD": 100, "P01T": 100, "P01M": 100, "P02": 100, "P03": 100, "P04": 100, "P05": 100, "P06": 95, "P07": 95, "P08": 95, "P09": 100, "P10": 95, "P11": 80, "P12": 100, "P13": 95},
 "buyer_phone": {"P01_GOLD": 90, "P02": 95, "P03": 95, "P04": 95, "P05": 90, "P06": 95, "P07": 90, "P08": 95, "P09": 100, "P10": 95, "P11": 75, "P13": 95},
 "buyer_logo_url": {"P01_GOLD": 90, "P01T": 95, "P02": 95, "P03": 95, "P04": 90, "P05": 95, "P06": 100, "P07": 100, "P08": 100, "P10": 100, "P11": 80, "P13": 95},
 # 4. AP
 "ap_contact_name_as_published": {"P01_GOLD": 25, "P02": 40, "P03": 20, "P04": 20, "P05": 15},
 "ap_phone": {"P01_GOLD": 80, "P01T": 70, "P02": 90, "P03": 60, "P04": 85, "P05": 50, "P09": 95},
 "invoice_mailing_address": {"P01_GOLD": 70, "P02": 75, "P03": 55, "P04": 75, "P05": 50, "P09": 95},
 "invoicing_requirements": {"P01_GOLD": 80, "P02": 75, "P03": 70, "P04": 70, "P05": 50, "P09": 80},
 "payment_terms_as_published": {"P01_GOLD": 70, "P01T": 60, "P02": 50, "P03": 55, "P04": 40, "P05": 40},
 "po_required_as_published": {"P01_GOLD": 70, "P01T": 65, "P02": 50, "P03": 60, "P04": 40, "P05": 45},
 "invoice_portal_url": {"P01_GOLD": 50, "P03": 60},
 "buyer_payment_method_preference": {"P01_GOLD": 40, "P02": 25, "P03": 25, "*": 15},
 "buyer_tax_exempt_status": {"P01_GOLD": 25, "P01T": 25, "*": 15},
 "buyer_ap_cycle_published": {"*": 20},
 "buyer_esignature_preference": {"*": 15},
 "ap_system_hint": {"P01_GOLD": 40, "P01T": 40, "P03": 35, "*": 20},
 # 5. contract metadata
 "contract_value": {"P01_GOLD": 95, "P02": 95, "P03": 90, "P04": 85, "P05": 75, "P09": 100, "P11": 60},
 "currency": {"P01_GOLD": 100, "P02": 100, "P04": 95, "P05": 80, "P09": 100},
 "start_date": {"P01_GOLD": 85, "P02": 90, "P03": 85, "P04": 90, "P05": 75, "P09": 95},
 "end_date": {"P01_GOLD": 85, "P02": 90, "P03": 85, "P04": 90, "P05": 75, "P09": 95},
 "contract_title": {"P01_GOLD": 100, "P02": 100, "P04": 95, "P05": 95, "P09": 100},
 "contract_description": {"P01_GOLD": 100, "P02": 100, "P04": 95, "P05": 70, "P09": 100},
 "number_of_bids": {"P01_GOLD": 60},
 # 6. history aggregates
 "average_contract_duration_days": {"P01_GOLD": 90, "P02": 90, "P03": 90, "P04": 90, "P05": 90, "P09": 90},
 "commodity_distribution_top3": {"P01_GOLD": 90},
 "year_over_year_spend_trend": {"P01_GOLD": 95},
 # 7. mail / domain security
 "mta_sts": {"*": 100}, "tls_rpt": {"*": 100}, "bimi": {"*": 100},
 # 2.8 / 2.10 vendor registry extras (QC vendors: measured on every row, the QC share is reported separately)
 "vendor_neq": {"P01_GOLD": 95, "P02": 95, "P03": 95, "P04": 95, "P09": 95},
 "vendor_years_in_business": {"P01_GOLD": 100, "P02": 100, "P03": 100, "P04": 100},
}
# honest ceilings: why some targets cannot be met under the rules (printed under the field so the number is read with its reason)
CEILING = {
 "po_number_as_published": "a purchase-order number exists only where the buyer publishes PO-level data (Montréal, Laval, Toronto open data so far) or the record itself carries one; most sources publish awards, not POs — the target cannot be reached from public data for most buyers",
 "contract_value": "rows proven by a lobbying filing, a news release, an auditor appointment, a customer story or a vendor's client list have no contract value by nature (≈17 % of P01 Gold); bids&tenders awards now carry the awarded bidder's submitted price when no award value was published",
 "start_date": "most award notices publish an award date, not a start date; start_date carries the signature date when the source gives one, labelled",
 "end_date": "an inferred end (award date + published duration) is labelled as such; sources without a duration leave end_date empty — the honest ceiling",
 "ap_contact_name_as_published": "role titles only (Supervisor, Accounts Payable) — the owner's rule 'never a named person' overrides the 25 % target; a person's name is never collected",
 "vendor_neq": "only Québec-registered vendors have an NEQ; the share of QC vendors is reported next to the rate",
 "number_of_bids": "published by some portals only (bids&tenders submission lists, Biddingo bidder lists); federal proactive disclosure does not publish bid counts",
 "buyer_bn_as_published": "a buyer's BN is public only where the buyer prints it or a public dataset carries it (CRA charities, federal grants & contributions recipients, business registries for corporations); municipalities rarely publish theirs",
 "vendor_logo_url": "needs the vendor's website first; sites that block automated readers (robots.txt / 403) are never read",
 "buyer_logo_url": "sites that block automated readers (robots.txt / 403) are never read; an og:image that looks like a photo is labelled",
 "invoice_portal_url": "only portals the buyer names on its own pages; informational tax-authority links are not portals",
 "mta_sts": "DNS-only check; 'no record' counts as checked", "tls_rpt": "DNS-only check; 'no record' counts as checked", "bimi": "DNS-only check; 'no record' counts as checked",
}
GROUP = {"1. identifiers": ["invoice_reference_hint", "po_number_as_published", "contract_or_agreement_number", "solicitation_or_tender_number", "award_or_notice_id", "buyer_vendor_id", "commodity_codes", "buyer_org_codes", "records_with_this_vendor"],
         "2. vendor": ["vendor_bn9", "vendor_registered_address", "vendor_trading_name", "vendor_phone", "vendor_website", "vendor_emails", "vendor_logo_url", "vendor_neq", "vendor_years_in_business"],
         "3. buyer": ["buyer_legal_name_as_published", "buyer_bn_as_published", "buyer_address", "buyer_phone", "buyer_logo_url"],
         "4. AP": ["ap_contact_name_as_published", "ap_phone", "invoice_mailing_address", "invoicing_requirements", "payment_terms_as_published", "po_required_as_published", "invoice_portal_url", "buyer_payment_method_preference", "buyer_tax_exempt_status", "buyer_ap_cycle_published", "buyer_esignature_preference", "ap_system_hint"],
         "5. contract": ["contract_value", "currency", "start_date", "end_date", "contract_title", "contract_description", "number_of_bids"],
         "6. history": ["average_contract_duration_days", "commodity_distribution_top3", "year_over_year_spend_trend"],
         "7. mail security": ["mta_sts", "tls_rpt", "bimi"]}
# a few fields only make sense on a subset of rows; the share is reported next to the rate so the ceiling is visible
SUBSET = {"vendor_neq": ("QC vendors", lambda r: (r.get("vendor_province") or r.get("vendor_jurisdiction") or "").upper().startswith("QC") or "quebec" in (r.get("vendor_registered_address") or "").lower() or "québec" in (r.get("vendor_registered_address") or "").lower()),
          "vendor_years_in_business": ("vendors with a registry record", lambda r: (r.get("vendor_incorporation_date") or "") not in EMPTY or (r.get("vendor_registry_ids") or "") not in EMPTY),
          "number_of_bids": ("rows from a source that publishes bids", lambda r: (r.get("number_of_bids") or "") not in EMPTY or (r.get("procurement_method") or "") not in EMPTY)}


def code_of(name):
    p = name.split("_")
    return p[0] + ("_GOLD" if len(p) > 1 and p[1] == "GOLD" else "")


def filled(v):
    return (v or "").strip() not in EMPTY


def load_batches(d):
    pk = collections.OrderedDict()
    for f in sorted(glob.glob(os.path.join(d, "*.csv"))):
        c = code_of(os.path.basename(f))
        if c.startswith("Z"):
            continue
        with open(f, encoding="utf-8", newline="") as fh:
            pk.setdefault(c, []).extend(csv.DictReader(fh))
    return pk


def load_ranked(path):
    cands = [os.path.join(ROOT, "contrib/claude/rank_buyers/batches.py"), os.path.expanduser("~/cch-crawler/contrib/claude/rank_buyers/batches.py")]
    src = open([c for c in cands if os.path.exists(c)][0], encoding="utf-8").read()
    ns = {"collections": collections}
    exec(src[src.index("OK = ("):src.index("# owner 2026-11-03 \"make sure all the fields")], ns)  # OK, rel(), B: the package rules themselves
    op = gzip.open if path.endswith(".gz") else open
    pk, used = collections.OrderedDict(), set()
    with op(path, "rt", encoding="utf-8", newline="") as fh:
        rows = list(csv.DictReader(fh))
    for name, f in ns["B"].items():
        c = code_of(name)
        for i, r in enumerate(rows):
            if i not in used and f(r):
                used.add(i)
                if not c.startswith("Z"):
                    pk.setdefault(c, []).append(r)
    return pk


def main():
    a = argparse.ArgumentParser()
    a.add_argument("--batches-dir", default=os.path.join(ROOT, "out/ranked/batches"))
    a.add_argument("--ranked", default="")
    a.add_argument("--write", default=os.path.join(ROOT, "out/ranked"))
    a.add_argument("--history", default=os.path.join(ROOT, "coord/results/coverage_history.csv"))
    a.add_argument("--date", default=TODAY)
    a = a.parse_args()
    pk = load_ranked(a.ranked) if a.ranked else load_batches(a.batches_dir)
    if not pk:
        sys.exit("no package rows found")
    cols = set()
    for rows in pk.values():
        if rows:
            cols |= set(rows[0].keys())
    # measure
    res = {}  # (field, pkg) -> dict
    for field, tg in T.items():
        for pkg, rows in pk.items():
            if not rows:
                continue
            target = tg.get(pkg, tg.get("*", "n/a")) if pkg in tg or "*" in tg else "n/a"
            n = len(rows)
            present = field in cols
            k = sum(1 for r in rows if filled(r.get(field))) if present else 0
            sub = ""
            if field in SUBSET and present:
                label, fn = SUBSET[field]
                m = [r for r in rows if fn(r)]
                if m:
                    sub = "%s: %d rows, %.1f%% filled" % (label, len(m), 100.0 * sum(1 for r in m if filled(r.get(field))) / len(m))
            res[(field, pkg)] = {"rows": n, "filled": k, "pct": round(100.0 * k / n, 1), "target": target, "present": present, "subset": sub}
    # history (previous build's value per field/pkg)
    prev = {}
    hist = []
    if os.path.exists(a.history):
        with open(a.history, encoding="utf-8", newline="") as fh:
            hist = [h for h in csv.DictReader(fh) if h.get("date") != a.date]
        last = {}
        for h in hist:
            key = (h["field"], h["package"])
            if key not in last or h["date"] > last[key][0]:
                last[key] = (h["date"], float(h["pct"] or 0))
        prev = {k: v for k, (d, v) in last.items()}
    for (field, pkg), v in res.items():
        hist.append({"date": a.date, "field": field, "package": pkg, "rows": v["rows"], "filled": v["filled"], "pct": v["pct"], "target": v["target"]})
    os.makedirs(os.path.dirname(a.history) or ".", exist_ok=True)
    with open(a.history, "w", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, fieldnames=["date", "field", "package", "rows", "filled", "pct", "target"]); w.writeheader(); w.writerows(hist)
    # score
    bench = [(f, p, v) for (f, p), v in res.items() if isinstance(v["target"], (int, float))]
    met = [b for b in bench if b[2]["pct"] >= b[2]["target"]]
    near = [b for b in bench if b[2]["pct"] < b[2]["target"] and b[2]["pct"] >= b[2]["target"] - 10]
    gaps = sorted(((f, p, v, int(-(-v["target"] * v["rows"] // 100) - v["filled"])) for f, p, v in bench if v["pct"] < v["target"]), key=lambda t: -t[3])
    L = ["# Coverage vs the downstream team's targets — %s" % a.date, "",
         "Benchmarks (field × package with a numeric target): **%d of %d met** (%.1f%%); %d within 10 points; %d further away." % (len(met), len(bench), 100.0 * len(met) / max(1, len(bench)), len(near), len(bench) - len(met) - len(near)),
         "A cell is filled unless blank / `not_published` / `not_found_yet`. Δ = change since the previous build in `coord/results/coverage_history.csv`.",
         "Rows per package: " + ", ".join("%s %d" % (p, len(r)) for p, r in pk.items()), ""]
    L += ["## Where the work is (largest gaps in rows still needed)", "", "| field | package | now | target | rows needed |", "|---|---|---|---|---|"]
    for f, p, v, need in gaps[:40]:
        L.append("| %s | %s | %.1f%% | %d%% | %d |" % (f, p, v["pct"], v["target"], need))
    L.append("")
    for g, fields in GROUP.items():
        L += ["## %s" % g, ""]
        for f in fields:
            if not any((f, p) in res for p in pk):
                continue
            if f not in cols:
                L += ["### `%s` — column missing from this build" % f, ""]
                continue
            L += ["### `%s`" % f, ""] + (["> ceiling: " + CEILING[f], ""] if f in CEILING else []) + ["| package | rows | now | Δ | target | status |", "|---|---|---|---|---|---|"]
            for p in pk:
                v = res.get((f, p))
                if not v:
                    continue
                d = ("%+.1f" % (v["pct"] - prev[(f, p)])) if (f, p) in prev else ""
                t = v["target"]
                st = ("✅ met" if v["pct"] >= t else "🟡 %.0f pts to go" % (t - v["pct"]) if v["pct"] >= t - 10 else "❌ %.0f pts to go" % (t - v["pct"])) if isinstance(t, (int, float)) else ("— leave (by design)" if t is None else "no target")
                L.append("| %s | %d | %.1f%% | %s | %s | %s%s |" % (p, v["rows"], v["pct"], d, ("%d%%" % t) if isinstance(t, (int, float)) else ("0% by design" if t is None else "n/a"), st, (" · " + v["subset"]) if v["subset"] else ""))
            L.append("")
    os.makedirs(a.write, exist_ok=True)
    open(os.path.join(a.write, "COVERAGE_VS_TARGETS.md"), "w", encoding="utf-8").write("\n".join(L) + "\n")
    json.dump({"date": a.date, "benchmarks": len(bench), "met": len(met), "near": len(near),
               "cells": {"%s|%s" % k: v for k, v in res.items()}}, open(os.path.join(a.write, "coverage_vs_targets.json"), "w"), indent=0)
    print("benchmarks met %d / %d (%.1f%%); near %d; written %s" % (len(met), len(bench), 100.0 * len(met) / max(1, len(bench)), len(near), os.path.join(a.write, "COVERAGE_VS_TARGETS.md")))
    for f, p, v, need in gaps[:15]:
        print("  gap %-34s %-8s %5.1f%% -> %3d%%  rows needed %d" % (f, p, v["pct"], v["target"], need))


if __name__ == "__main__":
    main()
