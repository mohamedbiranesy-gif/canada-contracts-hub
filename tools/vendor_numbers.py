#!/usr/bin/env python3
"""Billers first: the register number of the vendors that carry the most rows without one (owner 2026-11-13 13:23 EST: "go through every row
populate as much as can be max"; AGENTS.md rule 11: when the GST/HST number is not public, the number in its home register, labelled).

tools/registry_lookup.py looks each vendor up under the name the rows carry. A vendor the lane names by its brand ("doteasy") or by a
bilingual pair ("ROBIC AGENCE PI S.E.C./ ROBIC IP AGENCY LP") is never found that way. Here the vendors of the ready rows that lack a number
are taken by the rows they carry, and looked up in Canada's Business Registries under:
  - the legal name the vendor's own site prints (the row's vendor_legal_name, "World Host Group Ca Corp (stated on https://terms.doteasy.com/…)");
  - each half of a name written in two languages, and a legal name in brackets ("Alstom Canada (Alstom Transport Canada Inc.)").
A register entry counts only when its name equals the name looked up (tools/registry_lookup.pick: accents, punctuation and legal-form words
aside; the same legal form; the vendor's own province when several), and only while it is active. Answers go to
data/incoming/claude/claude_registry_alias.csv, the same columns as claude_registry_lookup.csv, keyed by the vendor's name as the rows carry
it; rank.py fills the vendor's number from them where no other register record was found. One request a second, identified user agent.

  python3 tools/vendor_numbers.py --ranked ranked_buyers.csv.gz [--top 300]
"""
import argparse, collections, csv, datetime, gzip, json, os, re, sys, time, urllib.parse

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, ".."))
sys.path.insert(0, HERE)
import registry_lookup as RL  # noqa: E402

csv.field_size_limit(1 << 30)
OUT = os.path.join(ROOT, "data/incoming/claude/claude_registry_alias.csv")
TODAY = datetime.date.today().isoformat()
_CUT = re.compile(r"\s*\((?:as printed|stated on|schema\.org|printed with its legal form|the copyright line|as registered|the vendor's name as the source).*$", re.I)
_FORM = re.compile(r"\b(inc|incorporated|ltd|limited|lt[ée]e|corp|corporation|llp|lp|s\.?e\.?n\.?c\.?r?\.?l?\.?|s\.?e\.?c\.?|ulc|co\.)\b\.?", re.I)
_PROV = {"A": "NL", "B": "NS", "C": "PE", "E": "NB", "G": "QC", "H": "QC", "J": "QC", "K": "ON", "L": "ON", "M": "ON", "N": "ON", "P": "ON", "R": "MB", "S": "SK",
         "T": "AB", "V": "BC", "X": "NT", "Y": "YT"}


def candidates(vendor, legal):
    out = []
    lg = _CUT.sub("", legal or "").strip(" -—–")
    if lg and len(lg) >= 4:
        out.append(lg)
    v = (vendor or "").strip()
    if re.fullmatch(r"(?:https?://)?[a-z0-9.-]+\.[a-z]{2,}/?", v.lower()):
        return list(dict.fromkeys(out))  # a vendor named by its domain: only a printed legal name is looked up
    m = re.search(r"\(([^()]{3,90})\)", v)
    if m and _FORM.search(m.group(1)):
        out.append(m.group(1).strip())
    base = re.sub(r"\([^()]*\)", " ", v).strip()
    parts = [p.strip(" ,") for p in re.split(r"\s*/\s*", base) if len(p.strip(" ,")) >= 4]
    out += parts if len(parts) > 1 else [base]
    return [c for c in dict.fromkeys(out) if c]


def province_of(addr):
    m = re.search(r"\b([ABCEGHJ-NPRSTVXY])\d[A-Z]\s?\d[A-Z]\d\b", (addr or "").upper())
    if m:
        return _PROV.get(m.group(1), "")
    m = re.search(r"\b(QC|ON|BC|AB|MB|SK|NS|NB|NL|PE|YT|NT|NU)\b", addr or "")
    return m.group(1) if m else ""


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--ranked", required=True)
    ap.add_argument("--top", type=int, default=300)
    ap.add_argument("--rate", type=float, default=1.0)
    ap.add_argument("--redo", action="store_true")
    a = ap.parse_args()
    cnt, info = collections.Counter(), {}
    with gzip.open(a.ranked, "rt", encoding="utf-8", errors="replace") as fh:
        for x in csv.DictReader(fh):
            if not (x.get("ship_ready") or "").startswith("yes") or "vendor tax" not in (x.get("invoice_fields_missing_for_kind") or ""):
                continue
            v = (x.get("vendor") or "").strip()
            if not v or v.startswith("inferred"):
                continue
            cnt[v] += 1
            info.setdefault(v, (x.get("vendor_legal_name") or "", x.get("vendor_address") or x.get("vendor_registered_address") or ""))
    have = {}
    if os.path.exists(OUT):
        with open(OUT, encoding="utf-8") as fh:
            have = {(r["kind"], r["key"]): r for r in csv.DictReader(fh)}
    stats = collections.Counter()
    for v, n in cnt.most_common(a.top):
        if ("vendor", v) in have and have[("vendor", v)].get("status") == "found":
            stats["already found"] += 1
            continue
        if ("vendor", v) in have and have[("vendor", v)].get("retrieved_date") == TODAY and not a.redo:
            stats["looked up today already"] += 1
            continue
        legal, addr = info[v]
        prov = province_of(addr)
        row = {"kind": "vendor", "key": v, "name": v, "status": "not_found", "retrieved_date": TODAY, "match_basis": "no registered name equals a name the vendor goes by"}
        for c in candidates(v, legal)[:4]:
            t0 = time.time()
            st, data, url = RL.search(c[:170])
            if st in (401, 403, 429):
                print("the service refused (HTTP %s): stopping as the rules require" % st, flush=True)
                stats["blocked"] += 1
                break
            docs = [d for d in ((data or {}).get("docs") or []) if re.match(r"\s*(?:active|good standing|en vigueur|immatricul)", d.get("Status_State") or "", re.I)]  # never "Inactive"
            d, basis, cands = RL.pick(c, docs, prov)
            time.sleep(max(0.0, 1.0 / a.rate - (time.time() - t0)))
            if d:
                how = ("the legal name the vendor's own site prints (%s)" % legal[:160]) if c == _CUT.sub("", legal or "").strip(" -—–") else ("a name the vendor goes by on the rows: %s" % c)
                row.update({"name": c, "status": "found", "matched_name": d.get("Company_Name") or "", "bn9": re.sub(r"\D", "", d.get("BN") or "")[:9], "juri_id": d.get("Juri_ID") or "",
                            "registry_source": d.get("Registry_Source") or "", "mras_id": d.get("MRAS_ID") or "", "entity_type": d.get("Entity_Type") or "",
                            "status_state": d.get("Status_State") or "", "status_notes": d.get("Status_Notes") or "",
                            "date_incorporated": (d.get("Date_Incorporated") or d.get("Date_Registered") or d.get("Display_Date") or "")[:10],
                            "reg_office_city": d.get("Reg_office_city") or "", "reg_office_province": d.get("Reg_office_province") or "",
                            "alternate_names": "; ".join(x for x in (d.get("Alternate_Name") or []) if x)[:200],
                            "match_basis": "%s; looked up under %s" % (basis, how), "api_url": url, "ui_url": RL.UI + urllib.parse.quote(c[:170], safe=""),
                            "source_quote": json.dumps({k: d.get(k) for k in ("Company_Name", "BN", "Juri_ID", "Registry_Source", "Entity_Type", "Status_State", "Reg_office_city", "Reg_office_province") if d.get(k)}, ensure_ascii=False)[:300]})
                break
        stats[row["status"]] += 1
        stats["rows of found vendors" if row["status"] == "found" else "rows of vendors not found"] += n
        have[("vendor", v)] = row
        if stats["blocked"]:
            break
    with open(OUT, "w", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, fieldnames=RL.COLS, extrasaction="ignore")
        w.writeheader()
        for k in sorted(have):
            w.writerow(have[k])
    print(json.dumps(dict(stats), indent=1), "->", OUT)


if __name__ == "__main__":
    main()
