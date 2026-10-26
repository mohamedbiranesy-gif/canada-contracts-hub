#!/usr/bin/env python3
"""Write README.md and source_notes.md into the output folder from the run statistics.
Usage: python3 -I make_readme.py <contracts_dir> <out_dir>
"""
import sys, os, json, collections, datetime, re

BASE, OUT = sys.argv[1], sys.argv[2]
ms = json.load(open(os.path.join(BASE, "work/merge_stats.json")))
es = json.load(open(os.path.join(OUT, "enrichment_summary.json")))
cov = es["record_enrichment_coverage"]

def agg(bucket):
    st, cf, bc = collections.Counter(), collections.Counter(), collections.Counter()
    for s, d in ms["buckets"].get(bucket, {}).items():
        st.update(d["status"]); cf.update(d["confidence"]); bc.update(d["buyer_country"])
    return st, cf, bc

st_ca, cf_ca, bc_ca = agg("ca")
st_un, cf_un, bc_un = agg("unv")
n_ca_pre, n_un_pre = sum(st_ca.values()), sum(st_un.values())
n_ca = cov.get("ca_records", n_ca_pre)
n_un = cov.get("unverified_records", n_un_pre)
n_moved = cov.get("ca_moved_not_identifiable", 0) + cov.get("unverified_moved_not_identifiable", 0)
pct = lambda a, b: "%.0f%%" % (100.0 * a / b) if b else "-"

rows = []
for bucket, srcs in ms["buckets"].items():
    for s, d in srcs.items():
        c = d["confidence"]
        rows.append((s, "verified CA" if bucket == "ca" else "vendor location not published", sum(d["status"].values()),
                     c.get("high", 0) + c.get("high_flagged_date", 0), c.get("medium", 0), c.get("low", 0) + c.get("very_low", 0), c.get("unknown", 0)))
rows.sort(key=lambda r: (r[1] != "verified CA", -r[2]))
src_files = {r[0] for r in rows}
notes = sorted(f[:-3] for f in os.listdir(os.path.join(BASE, "notes")) if f.endswith(".md"))
pulled_keys = {re.sub(r"_unverified_country$", "", s) for s in src_files}
checked_only = [n for n in notes if n not in pulled_keys and not n.startswith("enrichment") and n not in ("_probe",)]

def heading(n):
    try:
        with open(os.path.join(BASE, "notes", n + ".md"), encoding="utf-8") as f:
            h = f.readline().strip().lstrip("# ").strip()
        return h
    except Exception:
        return n

L = []
L.append("# Ongoing contracts with Canada-based vendors — dataset README")
L.append("")
L.append("Reference date **2026-10-25**. Generated %s." % datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%d %H:%M UTC"))
L.append("")
L.append("Every contract found in published sources worldwide where (1) the **vendor is located in Canada** according to the source's own vendor country/address field (never guessed from the name), (2) the **buyer is a named organisation**, and (3) the contract is **ongoing on 2026-10-25** — or the source publishes the award without any end date (kept and flagged, never dropped).")
L.append("")
L.append("## Files")
L.append("")
L.append("| File | Contents |")
L.append("|---|---|")
L.append("| `canadian_vendor_contracts.jsonl.gz` | **%s records** with a verified Canada-located vendor. One JSON object per line: normalized fields + status/confidence + best link + vendor and buyer enrichment. The bulky verbatim source block (`raw`) is left out here — it is in `full/`. |" % f"{n_ca:,}")
L.append("| `vendor_country_unverified_contracts.jsonl.gz` | **%s records** from sources that do not publish where the vendor is (Nova Scotia, City of Toronto, City of Ottawa, Ontario Vendor of Record, a few others). Probably mostly Canadian vendors, but not verified — kept separate. |" % f"{n_un:,}")
L.append("| `parties_not_identified_contracts.jsonl.gz` | **%s records** kept out of the two files above because one party is not identifiable in the source — e.g. CCC (Canadian Commercial Corporation) transactions whose foreign-government buyer is not disclosed, WHO contracts with the supplier name withheld, placeholder vendor names (\"INDIVIDUAL CONSULTANT\", \"SEE SUPPLIER NOTES\", \"REDACTED\", \"Various\"…). Each has `parties_identifiable_reason`. In `full/` they stay, flagged `parties_identifiable: false`. |" % f"{n_moved:,}")
L.append("| `full/<source>.jsonl.gz` | The same records per source **with `raw`**: every field the source publishes, verbatim — all identifiers, PO / contract / solicitation / reference / procurement numbers, amendment and transaction rows, codes, amounts, dates, addresses, contacts — plus the same enrichment blocks. |")
L.append("| `vendors_enriched.jsonl.gz` | One line per vendor (%s): every registry candidate with its full registry row, match confidence and evidence; Business Number and derived GST/HST account; names, addresses and identifiers seen across all contract sources. Join on `vendor_enrichment.vendor_key`. |" % f"{es['vendor_table']['vendors']:,}")
L.append("| `buyers_enriched.jsonl.gz` | One line per buyer (%s): official website, accounts-payable / supplier-invoicing mailboxes with evidence URL, invoice portal, invoicing instructions, procurement and general contacts, identifiers, address. Join on `buyer_enrichment.buyer_key`. |" % f"{len(open(os.path.join(BASE,'enrichment/v2/buyer_master_input.jsonl')).readlines()):,}")
L.append("| `summary.json`, `merge_stats.json`, `enrichment_summary.json` | Counts by source, status, confidence, buyer country, value sums; enrichment coverage. |")
L.append("| `source_notes.md` | The coverage note of every source checked — what was downloaded (URLs, times, row counts), how vendor country and status were decided, how links are built, known gaps — including sources checked and rejected. |")
L.append("")
L.append("## How sure is \"ongoing\"? (`status` and `status_confidence`)")
L.append("")
L.append("_Counts in this section and in the per-source table include the %s records later moved to the not-identified file._" % f"{n_moved:,}")
L.append("")
L.append("| status_confidence | meaning | verified-CA records |")
L.append("|---|---|---|")
L.append("| `high` | explicit published end date ≥ 2026-10-25 and start/award ≤ 2026-10-25 | %s |" % f"{cf_ca.get('high', 0):,}")
L.append("| `high_flagged_date` | as high, but the end date looks like a placeholder (e.g. 9999-12-31) | %s |" % f"{cf_ca.get('high_flagged_date', 0):,}")
L.append("| `medium` | end computed from a stated duration/term, framework or project period, or the parent award's period (arithmetic in `status_basis`) | %s |" % f"{cf_ca.get('medium', 0):,}")
L.append("| `low` | Quebec SEAO convention: no closure record published, contract concluded 2023 or later | %s |" % f"{cf_ca.get('low', 0):,}")
L.append("| `very_low` | Quebec SEAO convention, contract concluded before 2023 — closure publication is incomplete and late, so many of these have ended | %s |" % f"{cf_ca.get('very_low', 0):,}")
L.append("| `unknown` | award/contract published, nothing about the end date | %s |" % f"{cf_ca.get('unknown', 0):,}")
L.append("")
L.append("For \"definitely running\" use `high` + `medium` (%s records). `status_basis` on every record states the exact fields and comparison used." % f"{cf_ca.get('high',0)+cf_ca.get('high_flagged_date',0)+cf_ca.get('medium',0):,}")
L.append("")
L.append("Buyer countries (verified-CA records): %s distinct; top: %s." % (len(bc_ca), ", ".join(f"{k} {v:,}" for k, v in bc_ca.most_common(12))))
L.append("")
L.append("## Record layout (every line)")
L.append("")
L.append("- `record_id`, `source` (key, name, publisher, dataset_url, record_url, retrieved_at), `source_file`")
L.append("- `status`, `status_basis`, `status_confidence`, `status_confidence_basis`")
L.append("- `link` + `link_type`: the record's own page when the portal has one, otherwise the closest notice/project page, otherwise the dataset page (then use the identifiers to find it)")
L.append("- `contract`: identifiers (every id type the source has), title, description, instrument_type, procurement_method, solicitation_procedure, commodity codes (GSIN/UNSPSC/NAICS/PSC/CPV…), value, currency, value_detail, dates (published, signed, start, end, amended_last…), related (notice URLs, parent awards…)")
L.append("- `buyer` and `vendor` as published (name, country, country_basis, identifiers, address, contact)")
L.append("- `cross_source_matches`: other records that are probably the same contract in another source (same vendor and buyer plus same value, same dates or a shared identifier) — records are not merged")
L.append("- `vendor_enrichment`: registry match level, legal name, status, federal corporation number, Quebec NEQ, BC registration number, **Business Number (BN9)** and its source, **derived GST/HST account (BN9+RT0001)**, registered address, incorporation/registration date, governing law, Quebec legal form / employee band / activity, the matches with evidence and source URL")
L.append("- `buyer_enrichment`: canonical name, official website, identifiers, address, **`ap_contact`** (emails, invoice portal, invoicing requirements, instructions URL, evidence with page URL + retrieval time), procurement contact, general contact")
L.append("")
L.append("## Enrichment: what it covers and how far to trust it")
L.append("")
L.append("Coverage on the %s verified-CA records: vendor matched to a business registry (exact/strong) %s; vendor Business Number %s; vendor website verified %s; vendor contact (published in the contract data or on its own site) %s; buyer official website %s; buyer accounts-payable mailbox %s; buyer invoice portal %s." % (
    f"{n_ca:,}", pct(cov.get("ca_vendor_registry_match", 0), n_ca), pct(cov.get("ca_vendor_bn9", 0), n_ca), pct(cov.get("ca_vendor_website", 0), n_ca),
    pct(cov.get("ca_vendor_contact_any", 0), n_ca), pct(cov.get("ca_buyer_website", 0), n_ca),
    pct(cov.get("ca_buyer_ap_email", 0), n_ca), pct(cov.get("ca_buyer_invoice_portal", 0), n_ca)))
vt = es.get("vendor_table", {})
L.append("")
L.append("Vendor table (%s vendors): registry match exact %s, strong %s; Business Number %s; website looked up %s, verified website %s, published role mailbox %s." % (
    f"{vt.get('vendors', 0):,}", f"{vt.get('level_exact', 0):,}", f"{vt.get('level_strong', 0):,}", f"{vt.get('with_bn9', 0):,}",
    f"{vt.get('website_looked_up', 0):,}", f"{vt.get('with_website', 0):,}", f"{vt.get('with_contact_email', 0):,}"))
L.append("")
L.append("**Vendors.** Matched by normalised legal name, using the vendor's city, postal code (or 3-character postal prefix) and province to tell same-named companies apart; NEQs already published in Quebec contract data were matched directly. Registries: Corporations Canada federal corporations open data (corporation number, Business Number, status, registered office; 2026-10-25 extract), Registraire des entreprises du Québec open data (NEQ, legal form, status, names history, domicile address, establishments, activity, employee band; 2026-10-15 extract), BC OrgBook public API (registration number, Business Number, status) for every vendor with a BC address, and for vendors elsewhere still lacking a Business Number, OrgBook's extraprovincial registrations (companies from other provinces registered to do business in BC) — a match counts only when the registration's home jurisdiction equals the vendor's province (this lookup is slow and was still running at assembly time; `vendors_enriched.jsonl.gz` shows which vendors were queried). One-word vendor names are never matched with more than `weak` confidence. Hand check of random samples: federal 30/30 correct; Quebec 25/30 before tightening — name-only matches without any city/postal agreement were then downgraded to `weak` (kept as candidates, never used for identifiers). Most Canadian companies are provincially incorporated outside Quebec/BC (e.g. Ontario, Alberta) and those registries publish no bulk data, which is why many vendors have no Business Number.")
L.append("")
L.append("**Vendor websites and contacts.** Few sources publish vendor websites, so candidate domains were derived from each vendor's distinctive name words (.ca/.com) and a site was accepted only when its pages show the company name and a location from the contract data or registry (postal code, city or province); robots.txt was honoured. Sites reached only through a redirect to another domain (often a parent or brand) are marked `verified_via_redirect`. From the verified site's homepage and contact pages, organisational role mailboxes on the site's own domain (info@, sales@, accounting@, billing@ …) and main phone numbers were recorded with the page URL; personal-looking addresses were dropped, and protected/obfuscated emails and bot-checked pages were skipped. Vendors were processed in order of contract count; `website_lookup_status` tells whether a vendor was reached before assembly. Contacts that the contract sources themselves publish (e.g. supplier contact e-mail and phone in CanadaBuys or bids&tenders) are in `vendor.contact`.")
L.append("")
L.append("**GST/HST.** No public source lists GST/HST numbers by company. `gst_hst_account_derived` = BN9 + `RT0001` is the usual first GST/HST account of a registered business, but it is **derived, not published**, and exists only if the business is registered. The CRA GST/HST Registry, which confirms a number, sits behind a CAPTCHA, so nothing was confirmed automatically — confirm there before relying on one.")
L.append("")
L.append("**Buyers / AP emails.** Only role mailboxes that the organisation itself publishes for suppliers (invoicing, accounts payable, procurement), each copied from a page whose URL and retrieval time are recorded; personal mailboxes were excluded and no address was ever constructed from a pattern. Some federal entries come from PSPC's table of departmental supplier-payment contacts — these handle payment/direct-deposit questions and are labelled as such; contract-specific invoicing instructions in the contract itself take precedence. Divisions inherit their parent organisation's invoicing contact (e.g. City of Toronto divisions, provincial ministries). Hand checks: websites 30/30, AP mailboxes 35/35 in the final samples. About 260 buyer websites refused automated access (403/bot checks) and were skipped.")
L.append("")
L.append("## Records by source")
L.append("")
L.append("| source | bucket | records | high | medium | low+very low | unknown |")
L.append("|---|---|---|---|---|---|---|")
for r in rows:
    L.append("| %s | %s | %s | %s | %s | %s | %s |" % (r[0], r[1], f"{r[2]:,}", f"{r[3]:,}", f"{r[4]:,}", f"{r[5]:,}", f"{r[6]:,}"))
L.append("")
L.append("Sources checked that produced no records (no supplier location, no award data, blocked, or nothing ongoing) — details in `source_notes.md`: " + "; ".join(heading(n) for n in checked_only) + ".")
L.append("")
L.append("## Known limits")
L.append("")
L.append("- **Private-sector contracts** are only those publicly announced (press releases, SEC filings): a few hundred, a sample rather than a census. Most business-to-business contracts are never published.")
L.append("- **Blocked or unavailable** (not bypassed): SEDAR+ (bot check), BC Bid contract awards tab (reCAPTCHA; BC's open-data ministry awards were used instead), Yukon contract registry and Nunavut (Cloudflare), PEI (403), New Brunswick NBON and Manitoba open data (not reachable from this environment), New Zealand MBIE GETS files (bot check), Ontario Tenders Portal awards (no public award listing), CRA GST/HST Registry (CAPTCHA).")
L.append("- **Quebec SEAO `low`/`very_low` records** rest only on the absence of a published closure record; treat them as candidates.")
L.append("- **Values** are as published — often ceilings, framework maxima or IDV ceilings, not spend. Don't sum across records without care.")
L.append("- **Duplicates across sources** (e.g. UK Contracts Finder vs Find a Tender, federal proactive disclosure vs CanadaBuys) are flagged in `cross_source_matches`, not merged.")
L.append("- **\"Located in Canada\"** follows the address in the contract: Canadian subsidiaries of foreign groups count; foreign subsidiaries of Canadian firms don't.")
L.append("- bids&tenders and MERX award pages were crawled newest first; very old awards (mostly finished) may not all be included — see their notes.")
L.append("")
with open(os.path.join(OUT, "README.md"), "w", encoding="utf-8") as f:
    f.write("\n".join(L) + "\n")

with open(os.path.join(OUT, "source_notes.md"), "w", encoding="utf-8") as f:
    f.write("# Source coverage notes (one section per source checked)\n\n")
    for n in notes:
        with open(os.path.join(BASE, "notes", n + ".md"), encoding="utf-8") as g:
            txt = g.read().strip()
        if not txt:
            continue
        f.write("\n\n---\n\n<!-- notes/%s.md -->\n\n" % n)
        f.write(re.sub(r"^# ", "## ", txt, count=1) + "\n")
summary = {"reference_date": "2026-10-25", "verified_ca_records": n_ca, "unverified_records": n_un,
           "status_verified_ca": dict(st_ca), "confidence_verified_ca": dict(cf_ca), "confidence_unverified": dict(cf_un),
           "buyer_countries_verified_ca": dict(bc_ca.most_common()), "sources_with_records": len(src_files),
           "sources_checked_without_records": len(checked_only), "enrichment": es}
with open(os.path.join(OUT, "summary.json"), "w", encoding="utf-8") as f:
    json.dump(summary, f, indent=1, ensure_ascii=False)
os.system("cp '%s' '%s'" % (os.path.join(BASE, "work/merge_stats.json"), os.path.join(OUT, "merge_stats.json")))
print("README lines", len(L), "checked-only sources", len(checked_only), "sources with records", len(src_files))
