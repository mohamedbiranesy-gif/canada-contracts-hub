#!/usr/bin/env python3
"""The owner's test of a row — and, as an analysis only, the table with one row per (buyer, vendor) pair.

THE TEST (owner_test, used by contrib/claude/rank_buyers/rank.py on every row of the ranked table). Owner, 2026-11-11:
  13:00 EST  "There's an established relationship … a Canadian vendor or some type of entity that would be like … whatever month, year thing,
             okay, now you owe us so and so amount of money. And the buyer does not matter at all … the general email is where they take in …
             that is fine … the invoice fields … as populated as that relationship could expect it to be"
  13:09 EST  "it needs to be bank transfers relationship not credit card"        13:58 EST  "if it's not on invoice, by bank transfer then it's no"
  14:20 EST  asked whether an invoice that can be paid by bank transfer or cheque counts when the biller also takes a card: "In"; asked who the
             Canadian party may be: "Any Canadian entity" (a company, a regulator, a public body, an association)
A row is ship ready only when all five hold: (1) the relationship is established — a fact, or stated by the buyer itself — and current;
(2) the organisation's role mailbox was re-read by the referee; (3) the bill comes on invoice and bank transfer / cheque is a published or
inherent way to pay it (a card on file, or a registrar in between, is not a row at all: rank.py does not write such rows); (4) the fields of
its KIND of relationship are filled; (5) nothing flags it. ship_ready_missing names every one that does not hold.

THE PAIR TABLE (main(), an analysis — NOT published). Asked on 2026-11-11 13:40 EST whether a city that pays forty Canadian vendors is one row
or forty, the owner answered: "only 1 buyer so no buyer should be repeated". The ranked table therefore stays one row per buyer. What follows
describes the analysis that led to the question; it still measures how many relationships stand behind the buyers' rows.

One row per relationship: a Canada-located vendor that bills one organisation (owner, 2026-11-11, 13:00 and 13:09 EST).

Why. The ranked table (ranked_buyers.csv.gz) has one row per buyer. A city that pays forty Canada-located vendors under contract is one row
there, carrying its best vendor; the other thirty-nine relationships sit in a count (distinct_canadian_vendors). The owner's unit is the
relationship — "a Canadian vendor … that would send out an invoice … to whatever other entity out there in the world … the buyer does not
matter at all" — and his requirement for it is an invoice paid by bank transfer, not a card on file ("it needs to be bank transfers
relationship not credit card", "Shopify is over saturated in this way"). A contract award by a public body is exactly that relationship: the
vendor invoices under the contract number and the body's accounts payable pays the invoice.

What. ranked_relationships.csv.gz = every row of the ranked table, plus one row for each further (buyer, Canada-located vendor) pair of the
contract dataset whose buyer has a row with a mailbox. A pair row is the buyer's side of its row (name, address, mailbox, invoicing rules,
with their evidence — copied) and the vendor and the contract of that pair, built with the ranker's own rules: its functions are read out of
contrib/claude/rank_buyers/rank.py and run here (tier_of, classify_ids, rec_extra, vend_fill, the vendor-table loader …), not rewritten.

Every row then gets the owner's test, one function for all rows:
  payment_route, payment_route_basis        how the bill is paid: on invoice by the buyer's accounts payable (bank transfer / cheque), by a card
                                            on file, through a registrar, or not published — and where that is said
  invoice_fields_for_kind, _missing_for_kind the fields this KIND of relationship can carry (owner: "as populated as that relationship could
                                            expect it to be … Shopify … won't have a purchase order … maybe some other thing will") and the ones
                                            that are still empty
  ship_ready, ship_ready_missing            "yes" only when all five hold: (1) the relationship is established — a fact, or stated by the buyer
                                            itself — and current; (2) the organisation's role mailbox was re-read by the referee; (3) the bill
                                            is paid on invoice by bank transfer / cheque, not by a card on file; (4) the fields of its kind are
                                            filled; (5) nothing flags the row. ship_ready_missing names every one that does not hold.

  python3 tools/relationship_rows.py out/ranked/ranked_buyers.csv.gz [--out out/ranked] [--sample N]
      -> <out>/ranked_relationships.csv.gz   the table, one row per relationship
      -> <out>/RELATIONSHIPS.md              the counts: by kind, by payment route, ship ready, what is missing, the work lists
      -> <out>/relationships.json            the same counts for BUILD.json and the reports
      -> <out>/relationship_buyers_without_mailbox.csv   buyers of the contract dataset that have no mailbox yet, by the pairs that wait on them
"""
import argparse, ast, collections, csv, datetime, gzip, json, os, re, sys, time, unicodedata, zlib

csv.field_size_limit(1 << 30)
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
RANK = os.path.join(ROOT, "contrib/claude/rank_buyers/rank.py")
REL = ROOT + "/data/release/"

# ---- the ranker's own rules, read out of its script (it runs on import, so it cannot be imported) ---------------------------------------
WANT = ["today", "TIER", "TS", "CUTOFF", "CUTOFF3", "CUR", "JUR_SRC", "award_date", "tier_of", "jur_of_record", "contract_score", "classify_plus", "rec_extra", "KIND",
        "HOW_FOUND", "vend_fill", "form_conflict", "addr_text", "region_code", "norm", "parent", "host_of", "site_is_a_host", "clean_ve", "HOST_DOMS", "_VE_REG_KEYS", "jl",
        "VEN", "VEN_NAME", "VEN_DOM", "n_ve_form"]


def ranker_rules():
    src = open(RANK, encoding="utf-8").read()
    tree = ast.parse(src)
    top = {}
    for node in tree.body:
        if isinstance(node, ast.FunctionDef):
            top.setdefault(node.name, node)
        elif isinstance(node, ast.Assign):
            for tg in node.targets:
                for el in ([tg] if isinstance(tg, ast.Name) else tg.elts if isinstance(tg, ast.Tuple) else []):
                    if isinstance(el, ast.Name):
                        top.setdefault(el.id, node)
    closure, todo = {}, [w for w in WANT if w in top]
    while todo:
        n = todo.pop()
        if n in closure:
            continue
        closure[n] = top[n]
        for f in {x.id for x in ast.walk(top[n]) if isinstance(x, ast.Name)}:
            if f in top and f not in closure:
                todo.append(f)
    sys.path.insert(0, ROOT + "/tools")
    ns = {"__name__": "ranker_rules", "ROOT": ROOT, "REL": REL}
    exec("import csv, gzip, json, re, io, collections, unicodedata, datetime, sys, os, zlib\nimport urllib.parse\nfrom ap_crawler import same_org, registrable\nfrom lead_crawl import name_fit as _name_fit\n", ns)
    done = set()
    for name, node in sorted(closure.items(), key=lambda kv: kv[1].lineno):
        if id(node) in done or name in ("ROOT", "REL"):
            continue
        done.add(id(node))
        exec(compile(ast.get_source_segment(src, node), "rank.py:%d" % node.lineno, "exec"), ns)
    ns.setdefault("n_ve_form", 0)
    # the vendor table (vendors_enriched.jsonl.gz): the ranker's own loop, with its confidence rules (registry facts from an exact / strong match only …)
    loop = next(n for n in tree.body if isinstance(n, ast.For) and "vendors_enriched.jsonl.gz" in (ast.get_source_segment(src, n.iter) or ""))
    ns.update(n_form=0, n_dom_unfit=0, n_dom_host=0)
    exec(compile(ast.get_source_segment(src, loop), "rank.py:%d" % loop.lineno, "exec"), ns)
    return ns


# ---- which columns of a buyer's row describe the buyer (copied to its pair rows); everything else is the vendor's or the contract's -----
BUYER_SIDE = """jurisdiction buyer buyer_website buyer_address buyer_phone buyer_contact_evidence_url buyer_legal_name_as_published buyer_bn_as_published buyer_bn_program
buyer_trade_name_as_published buyer_gst_hst_derived buyer_logo_url buyer_website_status buyer_linkedin_url buyer_supplier_portals_linked buyer_registry_id buyer_bn_note buyer_type
sensitivity_tag sensitivity_flag buyer_sector peppol_participant_id peppol_registered statutory_payees_inferred buyer_municipal_tier buyer_population directory_general_email
municipal_directory_source buyer_fiscal_year_end buyer_charity_status buyer_charity_designation buyer_wikidata buyer_founded buyer_budget_or_revenue buyer_employees buyer_legal_form
buyer_facts_provenance email email_type email_check mailbox_confidence evidence_age_days reverify_due email_evidence_url email_evidence_quote email_evidence_context
mailbox_recheck_note mailbox_provenance email_deliverability email_security_posture dmarc_policy dmarc_record dmarc_record_domain spf_policy spf_record mail_provider dns_checked_date
mta_sts tls_rpt bimi ap_contact_name_as_published ap_phone invoice_mailing_address invoicing_requirements payment_terms_as_published payment_terms_default_policy
po_required_as_published invoice_portal_url invoice_portal_kind invoice_portal_note ap_system_hint invoicing_requirements_structured buyer_payment_method_preference
buyer_ap_cycle_published buyer_tax_exempt_status buyer_tax_status_derived tax_rate_indicative_derived invoice_currency_derived buyer_esignature_preference channel_tier ap_grade
ap_score ap_grade_basis ap_gap_to_A supplier_setup_url language_hint template_language method_notes contracts_with_canadian_suppliers buyer_keys keys grade acc
distinct_canadian_vendors records_last_12_months latest_award_date_any_vendor total_known_value_canadian_suppliers record_sources records_in_contract_dataset
typical_contract_value_p50 typical_contract_value_p75 typical_contract_value_p90 average_contract_duration_days commodity_distribution_top3 year_over_year_spend_trend
typical_cadence_days vendor_concentration_top_share most_recent_record_reference_any_vendor org_group_key ap_mailbox_ready""".split()

NEW_COLS = ["row_unit", "relationship_id", "payment_route", "payment_route_basis", "invoice_fields_for_kind", "invoice_fields_missing_for_kind", "vendor_tax_or_registration_number",
            "ship_ready", "ship_ready_missing"]

_has = lambda x, c: str(x.get(c) or "").strip() not in ("", "not_published", "{}")
_CARD = re.compile(r"credit card|carte de cr[ée]dit|\bvisa\b|mastercard|\bamex\b|american express|card on file|payment method (?:on file|that you authorize)|\bpaypal\b|\bstripe\b|debit card|charged? (?:to )?(?:your|the) (?:card|payment method)", re.I)
_BANK = re.compile(r"bank transfer|wire transfer|\bwire\b|virement|e-?transfer|interac|\beft\b|electronic funds|direct deposit|d[ée]p[oô]t direct|\bcheques?\b|\bchecks?\b|ch[èe]ques?|pre-?authori[sz]ed (?:debit|payment)|"
                   r"pr[ée]l[èe]vement|\bACH\b|bill payment|money order|mandat|at (?:a|your) (?:bank|financial institution)|institution financi|"
                   # 2026-11-11: the words of a bank's own bill-payment service, as utilities and public bodies print them ("Add NB Power as a payee",
                   # "through your bank", "automatic payments from your bank account") — NB Power's page read as card only without them
                   r"through (?:a|your|the|most) (?:banks?|financial institutions?|credit unions?)|from (?:a|your) bank account|online banking|telephone banking|as a payee|"
                   r"automatic(?:ally)? (?:withdraw\w*|payments?) from|withdrawn from your bank", re.I)
_DEAD = re.compile(r"dissol|inactive|radi[ée]|cancel|revoked|struck|annul|liquidat|discontinued|amalgamated|historical", re.I)
_LIVE = re.compile(r"\bactive\b|immatricul|en vigueur|in good standing|registered\b|existing|current", re.I)

# The fields a kind of relationship can carry (owner 2026-11-11, 13:00 EST: "as populated as that relationship could expect it to be"; 14:20 EST:
# "obviously can't be strict layout we have followed thus far, that was more so for contract, but tailor to each"). What a kind does not have is
# not asked of it: a contract award has a reference and no billing period in its record; a licence has a number, a yearly fee from a public
# tariff, and no tax number on its fee notice (a public body's licence fee is not a taxable sale); a member pays dues by the year and has no
# contract number; what a dealer buys and what a tenant pays are not public, so no amount is asked there; nobody but a buyer that says so
# needs a purchase-order number. The buyer's name and the biller's name are on every row by construction.
FIELDS = {
    "public contract": ["buyer address", "vendor address", "vendor tax or registration number", "what is billed", "amount", "reference"],
    "licence or registration": ["buyer address", "vendor address", "what is billed", "amount", "billing period", "reference"],
    "membership": ["buyer address", "vendor address", "vendor tax or registration number", "amount", "billing period"],
    "dealership": ["buyer address", "vendor address", "vendor tax or registration number"],
    "tenancy": ["buyer address", "vendor address", "vendor tax or registration number", "billing period"],
    "sponsorship": ["buyer address", "vendor address", "vendor tax or registration number"],
    "agent of record": ["buyer address", "vendor address", "vendor tax or registration number", "what is billed", "reference"],
    "service seen on the buyer's side": ["buyer address", "vendor legal name", "vendor address", "vendor tax or registration number", "what is billed", "amount", "billing period"],
    "utility account by location": ["buyer address", "vendor address", "what is billed", "amount", "billing period"],
    ".ca registration": ["buyer address", "vendor legal name", "vendor address", "vendor tax or registration number", "what is billed", "amount", "billing period"],
    "not established": ["buyer address", "vendor legal name", "vendor address", "vendor tax or registration number", "what is billed", "amount", "billing period"],
}
WHAT_IS_BILLED = {"membership": "membership dues", "dealership": "goods bought for resale, on the supplier's invoices", "tenancy": "rent and the charges of the lease",
                  "sponsorship": "the sponsorship or exhibitor fee"}  # the kind itself says what the bill is for


# test set of 2026-11-12: a contract a company announces in its own press release (a newswire, its newsroom) was labelled "fact, public
# record". It is the vendor's own dated announcement of a signed agreement — for a listed company a disclosure it answers for — and the
# row says so; it stays a public contract.
_PRESS = re.compile(r"press releases?|newswire|business wire|globenewswire|newsroom|communiqu[ée]s? de presse", re.I)


def record_basis(x):
    src, link = (x.get("source") or "the public source")[:120], (x.get("contract_link") or "")[:160]
    if _PRESS.search(src):
        return "fact, the vendor's own dated announcement of the agreement (not a public register): %s names the vendor and the contract (%s)" % (src, link)
    return "fact, public record: %s names the vendor and the contract (%s)" % (src, link)


def kind_of(x):
    t, fb, cs = x.get("tier") or "", x.get("relationship_fact_basis") or "", x.get("contract_status") or ""
    if "names the vendor and the contract" in fb or (t in ("A", "B", "L", "F") and fb.startswith("fact, public record")):
        return "public contract"
    if fb.startswith("by where it is"):
        return "utility account by location"  # tools/by_location.py: the exclusive electricity distributor of the organisation's own address
    if not (fb.startswith("fact") or fb.startswith("stated by the buyer")):
        return "not established"
    if "member named in the member directory" in cs or cs.startswith(("member of a Canadian body", "member / regulated payer", "accredited business")):
        return "membership"
    if "dealer / retailer named by" in cs:
        return "dealership"
    if "tenant / merchant named by" in cs:
        return "tenancy"
    if "sponsor / exhibitor named by" in cs:
        return "sponsorship"
    if cs.startswith(("client of a Canadian trademark agent", "client of a Canadian patent agent")):
        return "agent of record"
    return {"T": "service seen on the buyer's side", "R": ".ca registration", "M": "licence or registration"}.get(t, "public contract" if t == "C" and x.get("records_in_contract_dataset") else "not established")


def tax_or_registration(x):
    """the vendor's GST/HST number when a register or the vendor publishes its Business Number; otherwise its number in its home register (the
    Québec register gives the NEQ and no Business Number), said in so many words — never a number that is not printed somewhere"""
    if _has(x, "vendor_bn9"):
        return "%s — Business Number %s" % ((x.get("vendor_gst_hst_derived") or "").strip() or "GST/HST account not derived", str(x["vendor_bn9"]).strip()[:160])
    if _has(x, "vendor_neq"):
        return "NEQ %s — the Québec register publishes the enterprise number, not the Business Number" % str(x["vendor_neq"]).strip()[:140]
    if _has(x, "vendor_registry_id"):
        return "%s — this register entry carries no Business Number" % str(x["vendor_registry_id"]).strip()[:140]
    return ""


# A sentence about money going the other way says nothing of how the bill is paid: a refund clause ("refunds will be made by cheque"), or a
# body that pays its own suppliers ("will be processed via e-Transfer by … to the service provider"). Read on the owner's second test set,
# 2026-11-11: a college's refund policy, a host's refund clause and a charity's rule for paying its providers had each made a row "payable by bank".
_NOT_HOW_PAID = re.compile(r"\brefunds?\b|\brefunded\b|rembours|reimburs|\bpayouts?\b|to the service provider|to (?:our|its) (?:suppliers|vendors|providers)|we pay (?:you|our)|paid (?:out )?to you\b|vers[ée]s? (?:au|aux) fournisseur", re.I)


# a biller that says it refuses cards does not "take a card" because the word is in its sentence (Hydro-Québec: “Modes de paiement refusés* :
# Carte de crédit”; Manitoba Hydro: “we don’t accept e-transfers, credit card, cash”)
_CARD_REFUSED = re.compile(r"refus[ée]s?\*?\s*:?[^.]{0,40}carte de cr[ée]dit|credit cards? (?:is|are) (?:not accepted|refused)|(?:don.t|do not|doesn.t|does not|n.accepte pas)\s+accept[^.]{0,60}credit card|"
                           r"(?:don.t|do not|doesn.t|does not) accept[^.]{0,60}credit card|no credit card|credit card is refused|n.accepte(?:nt)? pas[^.]{0,40}carte", re.I)
_takes_card = lambda v: bool(_CARD.search(v)) and not _CARD_REFUSED.search(v)


def payment_route(x, kind):
    v = (x.get("bill_payment_method_as_published") or "").strip()
    if v and _NOT_HOW_PAID.search(v) and not re.search(r"we accept|nous acceptons|payment (?:methods|options) include|modes? de paiement accept|pay (?:your|the|an) invoice|payer (?:votre|la|une) facture", v, re.I):
        v = ""  # the sentence read is a refund or a payout clause: how the bill is paid is not published
    b = " ".join((x.get(c) or "") for c in ("buyer_payment_method_preference", "payment_terms_as_published")).strip()
    d = (x.get("bill_delivery_as_published") or "").strip()
    if d.startswith("no invoice is sent"):
        return "noinvoice", d[:300]
    if kind == "public contract":
        if _has(x, "buyer_payment_method_preference"):
            return "bank", "invoice paid by the buyer's accounts payable — as the buyer publishes: %s" % x["buyer_payment_method_preference"].strip()[:220]
        if _has(x, "payment_terms_as_published"):
            return "bank", "invoice paid by the buyer's accounts payable under its published payment terms: %s" % x["payment_terms_as_published"].strip()[:220]
        if _has(x, "payment_terms_default_policy"):
            return "bank", "invoice paid by the buyer's accounts payable; its government's payment policy: %s" % x["payment_terms_default_policy"].strip()[:220]
        return "bank", "invoice under a public contract award, paid by the buyer's accounts payable (by the kind of relationship: the buyer publishes no payment method)"
    by_kind = BY_KIND.get(kind) if not any(n in (x.get("vendor") or "").lower() for n in NOT_BY_KIND) else None
    if kind in INVOICE_SAID and _BANK.search(v) and not _INVOICE.search(d + " " + v):
        # a licence, a membership, a dealership …: how it can be paid is published, that the body sends an invoice, a bill or a notice for it is not.
        # The bank payment is in the biller's words; that the bill comes on an invoice is by the kind — except where a body's page was read for
        # it and names none (the Canadian Intellectual Property Office: cheques and wire transfers, no word of a notice).
        if by_kind and not _takes_card(v):
            return "kind", "bank payment in the biller's own words (%s); that the bill comes on an invoice or a notice is by the kind of relationship: %s" % (v[:160], by_kind)
        if by_kind:
            return "kind", "bank payment or card in the biller's own words (%s); that the bill comes on an invoice or a notice is by the kind of relationship: %s" % (v[:160], by_kind)
        return "nobill", "bank payment is accepted (%s), but nothing read says the body sends an invoice, a bill or a notice" % v[:200]
    if (x.get("vendor") or "").startswith("Shopify") or (_takes_card(v) and not _BANK.search(v)):
        return "card", "card or other method on file, charged by the vendor: %s" % v[:220]
    if "registrar of record" in v:
        return "registrar", "paid to the registrar of record, by the registrar's own methods; the Canadian registry bills the registrar: %s" % v[:160]
    if _BANK.search(v) and _takes_card(v):
        return "either", "the biller takes a bank payment or a card: %s" % v[:220]
    if _BANK.search(v):
        return "bank", "bank payment as the vendor publishes: %s" % v[:220]
    if by_kind:
        return "kind", "by the kind of relationship, not in this biller's own words: %s" % by_kind
    if _BANK.search(b) and kind != "not established":
        return "unknown", "the buyer pays its suppliers by bank payment (%s); how this vendor is paid is not published" % b[:160]
    return "unknown", "not published%s" % ((": " + v[:160]) if v else "")


# Owner, 2026-11-11 16:01 EST: "just populate those fields as best as you can, don't just go empty". When a biller's own sentence on how its bill
# is sent and paid has not been found, the row says how a bill of that kind is sent and paid — and says that it is by the kind, not in the
# biller's words. A sentence of the biller always wins: a card-only page still takes the row out, "we send no invoice" still fails it. Not for
# a service seen on the buyer's side (hosting, software): the common way there is a card on file.
BY_KIND = {
    "licence or registration": "a public body's fee for a licence or a registration: a notice or an invoice by mail, paid by cheque or through a financial institution",
    "membership": "an association's dues: an invoice for each membership year, paid by cheque or bank transfer",
    "dealership": "a supplier's sales to its dealer: an invoice with each delivery, on terms, paid by cheque or bank transfer",
    "tenancy": "rent under a commercial lease: due each month, paid by cheque or pre-authorised debit",
    "sponsorship": "a sponsorship or an exhibitor's fee: an invoice from the organiser, paid by cheque or bank transfer",
    "agent of record": "an agent's professional fees and the official fees it advances: an invoice for each step, paid by cheque or wire transfer",
    "utility account by location": "an electricity bill: issued every month or every two months, paid through a financial institution, by pre-authorised debit or by cheque",
}
NOT_BY_KIND = ("canadian intellectual property office",)  # its page names the ways of paying and no notice or invoice: nothing is said in its place
ROUTE_LABEL = {"kind": "on invoice, by bank transfer / cheque — by the kind of relationship (the biller's own words were not found)",
               "bank": "on invoice, by bank transfer / cheque", "card": "card on file, charged by the vendor", "registrar": "through the registrar of record",
               "either": "on invoice; bank payment or card (the biller takes both)", "unknown": "not published",
               "noinvoice": "no invoice is sent (the payer remits on its own, in the body's own words)",
               "nobill": "payable by bank, but no invoice or notice is published"}
INVOICE_SAID = ("licence or registration", "membership", "dealership", "tenancy", "sponsorship", "agent of record")
_INVOICE = re.compile(r"invoices?|factur|\bbills?\b|\bbilled\b|notices?\b|avis de (?:cotisation|renouvellement|paiement)|statements?\b|relev[ée]s?\b", re.I)
# a buyer's purchase-order rule is about what it orders from a supplier: a regulator's fee notice, a chamber's dues, a landlord's rent, an agent's
# account and a sponsorship are not ordered with a purchase order (owner 13:00 EST: "Shopify … won't have a purchase order … maybe some other thing will")
PO_KINDS = ("public contract", "service seen on the buyer's side", "dealership", ".ca registration", "not established")
# What reading the hundred of 2026-11-11 23:14Z found, each made a rule here so that a build and a re-test of a published table judge alike:
# - a mailbox that is only the hidden recipient of a web form (<input type="hidden" … value="info@…">) is in the page's source and not printed
#   on the page: the organisation does not publish it (§2.5), and a reader who opens the page does not find it;
_HIDDEN_FIELD = re.compile(r"<input\b[^<>]*\btype\s*=\s*[\"']?hidden\b[^<>]*$", re.I)
def mailbox_only_in_a_hidden_field(x):
    e, q = (x.get("email") or "").strip().lower(), x.get("email_evidence_quote") or ""
    if not e or not q:
        return False
    ql = q.lower()
    hits = [m.start() for m in re.finditer(re.escape(e[:12]), ql)]  # the quote is cut to 300 characters: the address may be cut too
    return bool(hits) and all(_HIDDEN_FIELD.search(q[max(0, i - 400):i]) for i in hits)
# - a sponsor or exhibitor list of a past year is not a current relationship (an exhibitor of a 2021 convention), a list of in-kind sponsors or
#   donors names nobody who is billed, and an event's own site prints the address of the hall it is held in, not the organiser's;
_IN_KIND = re.compile(r"in[-_ ]?kind|en[-_ ]nature|donor|donat(?:eur|ion|e)|media[-_ ]partner|partenaires?[-_ ]m[ée]dia", re.I)
_VENUE = re.compile(r"palais des congr|centre des congr|convention cent|congress cent|conference cent|exhibition (?:place|park|cent)|enercare|place jean-paul-riopelle|255 front st(?:reet|\.)? w|"
                    r"1055 canada pl|55 colonel by|375 york ave|1650 argyle|9797 jasper|20 roundup way|6900 airport r|650 dixon r|800,? (?:rue )?de la gaucheti|\bh[oô]tel\b|\bresort\b|fairmont|"
                    r"sheraton|marriott|hilton|hyatt|westin|delta hotels", re.I)
def sponsorship_faults(x, year=None):
    year = year or __import__("datetime").date.today().year
    out, link = [], (x.get("contract_link") or "") + " " + (x.get("vendor") or "")
    ys = [int(y) for y in re.findall(r"(?<!\d)(20[0-3]\d)(?!\d)", link)]
    if (ys and max(ys) < year - 1) or re.search(r"\bpast[-_ ]?(?:convention|conference|event|sponsors|exhibitors)", link, re.I):
        out.append("relationship not shown to be current (the sponsor or exhibitor list is of %s)" % (max(ys) if ys else "a past event"))
    if _IN_KIND.search(x.get("contract_link") or ""):
        out.append("relationship not established (a list of in-kind sponsors or donors: nobody on it is billed)")
    if _VENUE.search((x.get("vendor_address") or "").split(" (as printed")[0]):
        out.append("field: vendor address (the address printed is the hall or hotel of the event, not the organiser's)")
    return out
# - an agent of record that is a named person: the register names the agent, the firm that sends the account stands in brackets in its address,
#   and a natural person is not a row's biller (natural persons are left out of the register lanes).
_FIRM = re.compile(r"\b(?:llp|l\.l\.p|lp|inc|corp|corporation|ltd|limited|lt[ée]e|s\.?e\.?n\.?c|s\.?r\.?l|s\.?e\.?c|pllc|p\.?c\.?|plc|gmbh|ip|law|legal|avocats?|agents?|agency|agence|associates|associ[ée]s|"
                   r"partners|group|groupe|services?|office|bureau|trademarks?|marques|patents?|brevets|intellectual|propri[ée]t[ée]|consult\w*|company|cie|firm|cabinet|solicitors|barristers|&|and|et)\b|&", re.I)
_GIVEN = None
def agent_is_a_person(x):
    """two to four words, no word of a firm, and either an initial ("LLOYD W. AMENT") or a given name in front — "ANDREWS ROBICHAUD" and
    "Fasken Martineau DuMoulin" are firms named after their founders"""
    global _GIVEN
    v = (x.get("vendor") or "").strip()
    if re.match(r"(?:mr|mrs|ms|dr|me|ma[iî]tre)\.?\s+[A-Za-zÀ-ÿ]", v, re.I):
        return True  # "MR. CHRISTOPHER TAN", "ME DANIEL ROUSSIN", "MAÎTRE …" (test set of 2026-11-12)
    w = re.findall(r"[A-Za-zÀ-ÿ'’.-]+", v)
    if not (2 <= len(w) <= 4) or _FIRM.search(v) or "+" in v or re.search(r"\d", v):
        return False
    if any(re.fullmatch(r"(?:[A-Za-z]\.){1,3}|[A-Za-z]\.?", t) for t in w[:-1]):
        return True  # an initial: "D. MICHAEL BEAN", "MAY M.M. CHENG", "R.GRANT CANSFIELD"
    if re.fullmatch(r"[A-Za-z]\.[A-Za-z]{2,}", w[0]):
        return True
    if _GIVEN is None:
        try:
            sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
            from buyer_pages import FIRST_NAMES as _fn
            _GIVEN = set(_fn)
        except Exception:
            _GIVEN = set()
    return re.sub(r"[^a-z]", "", w[0].lower()) in _GIVEN or re.sub(r"[^a-z]", "", w[0].lower()) in _MORE_GIVEN


# given names of agents of record read on the test set of 2026-11-12 that the list of tools/buyer_pages.py did not hold
_MORE_GIVEN = set("""anita lei chad selena kimberley theo cory danyel jay xin rupinder kirsten jessie julien adrienne katharine yuri del stephanie
corey ardeshir bruno zak doreen tessa clare karol yue hubert emmet lyanne lonnie esmaeil sorel ahmed dirk yunwei dario russel yadvinder sampson
angeliki""".split())
# - a row by where the organisation is, at a postal code that fifty or more organisations print (tools/by_location.py: SHARED_FAIL): a tower,
#   a campus, a business centre or a mail service — the electricity account there is the landlord's
_SHARED = re.compile(r"(\d[\d,]*) organisations print this same postal code")
def shared_address(x):
    m = _SHARED.search(x.get("relationship_fact_basis") or "")
    return int(m.group(1).replace(",", "")) if m else 0
ROUTE_OK = ("bank", "either", "kind")  # owner 2026-11-11 14:20 EST: an invoice that can be paid by bank transfer is in, also when the biller would take a card

# Owner, 2026-11-11 evening. 20:22 EST: "the relationship billed amount per cadence should be 5000 plus". Shown that 1,510 of 136,513 rows carry
# a published amount that high, he first chose a hard floor and one row per buyer-vendor pair, then at 20:36 EST settled it: "we will also
# include those of lower value but mark them, mark everything, prioritise over 5000 … no buyer twice is hard rule so it should be 1 million
# buyers, vendor can be repeated … that's why I was willing to lift 5000 cap, make it soft". So $5,000 is a MARK and an order, not a test:
# every row says which of five classes its amount is in (amount_mark) and the table is written in that order (tools/priority_sort.py).
#   1 published, $5,000 or more    the value of the contract as the public record gives it, or the biller's own published fee or price
#   2 estimated, $5,000 or more    no published amount that high, and an amount calculated from published figures that is (labelled on the row)
#   3 published, under $5,000      a price "from $15.43 a month" is $15.43
#   4 estimated, under $5,000
#   5 no amount
# The figure is taken in the currency of the record (a contract in US dollars or euros is not converted). For a contract the public record
# gives the value of the contract and its dates, not each invoice: the row also carries the value by the year of its term, calculated and
# labelled (value_by_year).
FLOOR = 5000.0
_NUM = r"\d{1,3}(?:[ ,\u00a0]\d{3})+(?:\.\d+)?|\d+(?:\.\d+)?"
_AMT1 = re.compile(r"(?:C|CA|US|CAD|USD)?\$\s?(" + _NUM + r")")
_AMT2 = re.compile(r"(?<![\w.])(" + _NUM + r")\s?(?:\$|CAD\b|USD\b|EUR\b|€|dollars\b)")
def _f(t):
    try:
        return float(re.sub(r"[ ,\u00a0]", "", t))
    except ValueError:
        return None


def published_amount(x):
    """(the published amount of the row, the column it stands in) or (None, "") — never the calculated one"""
    # (a zero is no amount: test set of 2026-11-12, an import declaration whose "value" was the duty paid, 0)
    cv = str(x.get("contract_value") or x.get("contract_value_from_pair") or "").strip()
    m = re.match(r"\s*(?:C|CA|US|CAD|USD)?\$?\s?(" + _NUM + r")", cv)
    if m and (_f(m.group(1)) or 0) > 0:
        return _f(m.group(1)), "contract_value"
    b = str(x.get("bill_amount_indicative") or "").strip()
    m = _AMT1.search(b) or _AMT2.search(b)
    if m and (_f(m.group(1)) or 0) > 0:
        return _f(m.group(1)), "bill_amount_indicative"
    m = re.search(r"(" + _NUM + r")\s?(?:¢|cents?\b)", b)   # "40.89 ¢ a day"
    if m and (_f(m.group(1)) or 0) > 0:
        return _f(m.group(1)) / 100.0, "bill_amount_indicative"
    return None, ""


def estimated_amount(x):
    """the first figure of the row's calculated / estimated amount, or None (a contract's value by the year is the published value, spread: not an estimate of its own)"""
    b = str(x.get("bill_amount_calculated") or "").strip()
    if not b or published_amount(x)[1] == "contract_value":
        return None
    m = _AMT1.search(b) or _AMT2.search(b) or re.search(r"(?:—|about)\s+(" + _NUM + r")", b)
    return _f(m.group(1)) if m else None


def amount_mark(x):
    """the class of the row's amount (see FLOOR), with the figure it rests on"""
    amt, col = published_amount(x)
    est = estimated_amount(x)
    n = lambda v: format(v, ",.2f").rstrip("0").rstrip(".")
    if amt is not None and amt >= FLOOR:
        return "1 published, $5,000 or more (%s: %s)" % ("the contract's value" if col == "contract_value" else "the biller's published amount", n(amt))
    if est is not None and est >= FLOOR:
        return "2 estimated, $5,000 or more (%s, calculated — see bill_amount_calculated%s)" % (n(est), ("; published: %s" % n(amt)) if amt is not None else "")
    if amt is not None:
        return "3 published, under $5,000 (%s: %s%s)" % ("the contract's value" if col == "contract_value" else "the biller's published amount", n(amt), ("; estimated %s" % n(est)) if est is not None else "")
    if est is not None:
        return "4 estimated, under $5,000 (%s, calculated — see bill_amount_calculated)" % n(est)
    return "5 no amount"


def value_by_year(x):
    """'' or the contract's published value divided by the years of its published term — calculated, and said to be"""
    amt, col = published_amount(x)
    if col != "contract_value" or not amt:
        return ""
    try:
        d0 = datetime.date.fromisoformat(str(x.get("start_date") or x.get("award_date") or "")[:10])
        d1 = datetime.date.fromisoformat(str(x.get("end_date") or "")[:10])
    except ValueError:
        return ""
    days = (d1 - d0).days
    if days < 28:
        return ""
    if days <= 366:
        return "calculated — the whole value falls within one year (about %s a month): the contract runs %s to %s (%d days)" % (format(amt / max(1.0, days / 30.44), ",.0f"), d0, d1, days)
    return ("calculated — %s a year (about %s a month) over the term: the published value %s divided by the %.1f years from %s to %s; when the vendor bills, and how "
            "much each time, is not published" % (format(amt / (days / 365.25), ",.0f"), format(amt / (days / 30.44), ",.0f"), format(amt, ",.0f"), days / 365.25, d0, d1))


def owner_test(x):
    """payment route, fields of the kind, ship ready — on any row of the table (a buyer's row or a pair row)"""
    kind = kind_of(x)
    route, basis = payment_route(x, kind)
    x["payment_route"], x["payment_route_basis"] = ROUTE_LABEL[route], basis
    x["vendor_tax_or_registration_number"] = tax_or_registration(x)
    have = {"buyer address": _has(x, "buyer_address") or _has(x, "invoice_mailing_address"),
            "vendor legal name": _has(x, "vendor_legal_name") and "on that line alone" not in (x.get("vendor_legal_name") or ""),
            "vendor address": _has(x, "vendor_address") or _has(x, "vendor_registered_address"),
            "vendor tax or registration number": bool(x["vendor_tax_or_registration_number"]),
            "what is billed": _has(x, "contract_title") or _has(x, "bill_items_as_published") or (kind in ("public contract", "licence or registration", "agent of record") and _has(x, "contract_description")),
            "amount": _has(x, "contract_value") or _has(x, "bill_amount_indicative") or _has(x, "bill_amount_calculated"),
            "billing period": (x.get("recurring_billing") or "")[:1] in ("1", "2", "3", "4"),
            "reference": _has(x, "contract_reference") or _has(x, "invoice_reference_hint")}
    fields = FIELDS[kind]
    miss = [f for f in fields if not have[f]]
    x["invoice_fields_for_kind"] = "%s: %s" % (kind, ", ".join(fields))
    x["invoice_fields_missing_for_kind"] = "; ".join(miss) or "none"
    out = []
    fb = x.get("relationship_fact_basis") or ""
    if kind == "not established":
        out.append("relationship not established (%s)" % (fb.split(":")[0].strip()[:40] or "no basis on the row"))
    elif kind == "public contract" and (x.get("tier") or "") not in ("A", "B", "L"):
        out.append("relationship not shown to be current (%s)" % ((x.get("contract_status") or "older award, no end date published")[:60]))
    ec = x.get("email_check") or ""
    if not _has(x, "email"):
        out.append("no mailbox")
    elif not ec.startswith(("confirmed", "cross")):
        out.append("mailbox not re-read by the referee (%s)" % (ec or "not checked")[:40])
    if route not in ROUTE_OK:
        out.append("payment: %s" % ROUTE_LABEL[route])
    if kind == "public contract" and not _has(x, "bill_amount_calculated"):
        vy = value_by_year(x)
        if vy:
            x["bill_amount_calculated"] = vy
    x["amount_mark"] = amount_mark(x)
    # Owner, 2026-11-11 16:01 EST: "populate those fields as best as you can, don't just go empty … there's clear goal and it is 1 million". A row
    # stands on four things — a Canadian biller with a relationship, a bill on invoice, a bank payment, the organisation's mailbox. A field of
    # its kind that nothing published fills does not take the row out any more: it is said on the row (invoice_fields_missing_for_kind, and in
    # ship_ready itself), and the row sorts below the complete ones. Two things still must be there: the biller's own printed address (it is
    # what puts the biller in Canada), and, for a row that stands on where the organisation is, the organisation's own address.
    must = [f for f in miss if f == "vendor address" or (kind == "utility account by location" and f == "buyer address")]
    out += ["field: " + f for f in must]
    if mailbox_only_in_a_hidden_field(x):
        out.append("mailbox not printed on the page (it is the hidden recipient of a web form in the page's source)")
    if kind == "sponsorship":
        out += sponsorship_faults(x)
    if kind == "agent of record" and agent_is_a_person(x):
        out.append("relationship: the agent of record is a named person, not a firm")
    n_shared = shared_address(x) if kind == "utility account by location" else 0
    if n_shared >= 50:
        out.append("relationship: %d organisations print this postal code — a tower, a campus, a business centre or a mail service, where an account of its own is unlikely" % n_shared)
    if (x.get("sensitivity_flag") or "") == "yes":
        out.append("flag: " + ((x.get("sensitivity_tag") or "sensitive buyer").split(":")[0][:70]))
    if _has(x, "vendor_registry_warning"):
        out.append("flag: vendor registry warning")
    # 2026-11-12 (rule 13: a field nothing published fills is named on the row and no longer takes it out): the purchase-order number a buyer
    # asks for on invoices is in the vendor's own papers, not in the public record. It was a flag that failed the row (231 rows with a published
    # contract value of $5,000 or more, sample build of 02:00Z); it is said on the row now.
    po_missing = kind in PO_KINDS and (x.get("po_required_as_published") or "").startswith("yes") and not (_has(x, "po_number_as_published") or _has(x, "po_number_as_published_from_pair"))
    soft = [f for f in miss if f not in must]
    said = []
    if kind == "utility account by location":
        said.append("by where the organisation is: the biller is certain for the address, the account holder is not published")
        if "the address an Overture Maps place lists for its website" in (x.get("buyer_address") or ""):  # tools/by_location.py: DIRECTORY_MARK
            said.append("the organisation's address is the one a public places dataset (Overture Maps) lists for its website, not read on its own pages")
        if n_shared:
            said.append("a shared address: %d organisations print this postal code" % n_shared)
    if route == "kind":
        said.append("how it is billed and paid is by the kind of relationship, not yet in the biller's own words")
    if po_missing:
        said.append("not published: the purchase-order number the buyer requires on invoices (the vendor holds it)")
    if soft:
        said.append("not published: " + ", ".join(soft))
    elif "amount" in fields and not (_has(x, "contract_value") or _has(x, "bill_amount_indicative")):
        said.append("the amount is calculated and labelled so")
    x["ship_ready"] = "no" if out else ("yes (%s)" % "; ".join(said) if said else "yes")
    x["ship_ready_missing"] = "; ".join(out)
    return kind, route, out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("table")
    ap.add_argument("--out", default="out/ranked")
    ap.add_argument("--contracts", default=REL + "canadian_vendor_contracts.jsonl.gz")
    ap.add_argument("--sample", type=int, default=0, help="a local look: only every Nth buyer's pairs are built")
    ap.add_argument("--no-table", action="store_true", help="counts only")
    a = ap.parse_args()
    t0 = time.time()
    R = ranker_rules()
    norm, tier_of, award_date, contract_score, clean_ve, jur_of_record = R["norm"], R["tier_of"], R["award_date"], R["contract_score"], R["clean_ve"], R["jur_of_record"]
    print("ranker rules loaded (vendor table: %d vendors) in %d s" % (len(R["VEN"]), time.time() - t0), flush=True)

    # pass 1 — the table: which buyer keys belong to which row
    key_rows, row_info, cols = collections.defaultdict(list), {}, None
    with gzip.open(a.table, "rt", encoding="utf-8", newline="") as f:
        rd = csv.DictReader(f)
        cols = rd.fieldnames
        for i, x in enumerate(rd):
            ks = [k for k in (x.get("keys") or "").split("|") if k.startswith("b:")]
            if ks:
                row_info[i] = (bool((x.get("email") or "").strip()), norm(x.get("vendor") or ""), norm(x.get("vendor_legal_name") or ""))
                for k in ks:
                    key_rows[k].append((i, x.get("jurisdiction") or ""))
    print("pass 1: %d rows carry keys of the contract dataset (%d keys) — %d s" % (len(row_info), len(key_rows), time.time() - t0), flush=True)

    # pass 2 — the contract dataset: every (row, vendor) pair, its best record by the ranker's score, its references
    pairs, n_rec, n_amb, n_norow = {}, 0, 0, 0
    with gzip.open(a.contracts, "rt", encoding="utf-8") as f:
        for l in f:
            n_rec += 1
            r = clean_ve(json.loads(l))
            cands = key_rows.get((r.get("buyer_enrichment") or {}).get("buyer_key") or "")
            if not cands:
                n_norow += 1
                continue
            if len(cands) > 1:
                j = jur_of_record(r)
                cands = [c for c in cands if c[1] == j]
                if len(cands) != 1:
                    n_amb += 1
                    continue
            i = cands[0][0]
            if a.sample and i % a.sample:
                continue
            vname = ((r.get("vendor") or {}).get("name") or "").strip()
            if not vname:
                continue
            vid = (r.get("vendor_enrichment") or {}).get("vendor_key") or ("n:" + norm(vname))
            p = pairs.get((i, vid))
            if p is None:
                p = pairs[(i, vid)] = {"n": 0, "bs": (-1.0, ""), "key": (-1, (-1.0, "")), "best": b"", "refs": [], "name": vname}
            p["n"] += 1
            c = r.get("contract") or {}
            ad = award_date(r)
            ids = c.get("identifiers") or {}
            ref = next((str(ids[k]) for k in ("po_number", "purchase_order_number", "contract_number", "reference_number", "cn_id", "numero", "award_id") if ids.get(k)), "") or next((str(v) for v in ids.values() if v), "")
            if len(p["refs"]) < 40:
                p["refs"].append((ad, ref[:60], str(c.get("value") or ""), str(c.get("currency") or "")[:3]))
            sc = (float(contract_score(r)[0]), ad)
            # the record that stands for the pair: a current contract whose published value meets the floor first (owner 2026-11-11 20:35 EST),
            # then the ranker's own score. Before, the best-scored record stood for the pair also when a larger current one existed.
            try:
                _val = float(c.get("value")) if c.get("value") not in (None, "") else None
            except (TypeError, ValueError):
                _val = None
            key = (1 if (_val is not None and _val >= FLOOR and tier_of(r) in ("A", "B", "L")) else 0, sc)
            if key > p["key"]:
                p["key"], p["bs"], p["best"] = key, sc, zlib.compress(l.encode("utf-8"), 1)
    by_row = collections.defaultdict(list)
    for (i, vid), p in pairs.items():
        by_row[i].append((vid, p))
    print("pass 2: %d contract records, %d (row, vendor) pairs on %d rows (records of buyers without a row: %d; of a key shared by several governments, not assigned: %d) — %d s"
          % (n_rec, len(pairs), len(by_row), n_norow, n_amb, time.time() - t0), flush=True)

    # pass 3 — write: each row of the table, then the further pairs of its buyer
    os.makedirs(a.out, exist_ok=True)
    out_cols = [c for c in cols if c != "ship_ready"]
    j = out_cols.index("data_quality_score") + 1 if "data_quality_score" in out_cols else 4
    out_cols = out_cols[:j] + ["ship_ready", "ship_ready_missing", "amount_mark", "payment_route", "payment_route_basis", "invoice_fields_for_kind", "invoice_fields_missing_for_kind", "vendor_tax_or_registration_number", "row_unit", "relationship_id"] + \
        [c for c in out_cols[j:] if c not in ("ship_ready_missing",)] + (["ap_mailbox_ready"] if "ap_mailbox_ready" not in out_cols else [])
    out_cols = list(dict.fromkeys(out_cols))
    w = None
    if not a.no_table:
        fo = gzip.open(os.path.join(a.out, "ranked_relationships.csv.gz"), "wt", encoding="utf-8", newline="", compresslevel=6)
        w = csv.DictWriter(fo, fieldnames=out_cols, extrasaction="ignore")
        w.writeheader()
    n = collections.Counter(); by_kind = collections.Counter(); by_route = collections.Counter(); miss = collections.Counter(); one = collections.Counter(); two = collections.Counter()
    ready_kind = collections.Counter(); ready_mail = collections.Counter(); gap = collections.Counter(); wait_mail = collections.Counter(); wait_name = {}
    vend_short = collections.Counter()

    def count(x, unit):
        kind, route, out = owner_test(x)
        n["rows"] += 1; n[unit] += 1
        by_kind[kind] += 1; by_route[(kind, ROUTE_LABEL[route])] += 1
        if not out:
            n["ship_ready"] += 1; ready_kind[kind] += 1; ready_mail[x.get("email_type") or "?"] += 1
            n["ship_ready, amount calculated"] += x["ship_ready"] != "yes"
        else:
            gap[min(len(out), 4)] += 1
            for o in out:
                miss[o.split(" (")[0]] += 1
            if len(out) == 1:
                one[(kind, out[0].split(" (")[0])] += 1
            elif len(out) == 2:
                two[" + ".join(sorted(o.split(" (")[0] for o in out))] += 1
            if "field: vendor tax or registration number" in out and len(out) <= 2:
                vend_short[(x.get("vendor") or "")[:70]] += 1

    with gzip.open(a.table, "rt", encoding="utf-8", newline="") as f:
        for i, x in enumerate(csv.DictReader(f)):
            if "ap_mailbox_ready" not in x:
                x["ap_mailbox_ready"] = x.get("ship_ready") or ""   # a table built before 2026-11-11 18Z: the old label under its own name
            x["row_unit"] = "relationship: this buyer and the vendor named on the row"
            x["relationship_id"] = "%s|%s" % ((x.get("keys") or "").split("|")[0], norm(x.get("vendor") or "")[:60])
            prs = by_row.get(i)
            swapped = False
            if prs and row_info[i][0] and owner_test(x)[2]:
                # the buyer's own row carries one record of its best vendor. When that record fails the test and another record of the same pair
                # passes it (a larger, current contract with the same vendor), the pair's record stands for the relationship.
                for vid, p in prs:
                    if norm(p["name"]) and norm(p["name"]) in row_info[i][1:]:
                        y = pair_row(R, x, clean_ve(json.loads(zlib.decompress(p["best"]).decode("utf-8"))), p, int(x.get("grade") or 0), (x.get("acc") or "") == "True")
                        if not owner_test(y)[2]:
                            y["row_unit"] = "relationship: this buyer and its vendor of the ranked table, by the pair's record that meets the test"
                            count(y, "pair rows from the contract dataset")
                            n["… of which the buyer's own vendor, by another record of the pair"] += 1
                            if w:
                                w.writerow(y)
                            swapped = True
                        break
            if not swapped:
                count(x, "rows of the ranked table")
                if w:
                    w.writerow(x)
            if not prs:
                continue
            has_mail, own_v, own_l = row_info[i]
            if not has_mail:
                wait_mail[i] = len(prs)
                wait_name[i] = (x.get("buyer") or "", x.get("buyer_website") or "", x.get("jurisdiction") or "", x.get("buyer_type") or "", (x.get("keys") or "").split("|")[0])
                n["pairs waiting for a mailbox of their buyer"] += len(prs)
                continue
            g, acc = int(x.get("grade") or 0), (x.get("acc") or "") == "True"
            for vid, p in sorted(prs, key=lambda kv: (-kv[1]["bs"][0], kv[1]["name"])):
                vn = norm(p["name"])
                if vn and vn in (own_v, own_l):
                    n["pairs already the buyer's own row (its best vendor)"] += 1
                    continue
                r = clean_ve(json.loads(zlib.decompress(p["best"]).decode("utf-8")))
                y = pair_row(R, x, r, p, g, acc)
                count(y, "pair rows from the contract dataset")
                if w:
                    w.writerow(y)
            if i % 20000 == 0:
                print("  … row %d, %d written — %d s" % (i, n["rows"], time.time() - t0), flush=True)
    if w:
        fo.close()

    # the reports
    with open(os.path.join(a.out, "relationship_buyers_without_mailbox.csv"), "w", encoding="utf-8", newline="") as f:
        cw = csv.writer(f)
        cw.writerow(["pairs_waiting", "buyer", "buyer_website", "jurisdiction", "buyer_type", "buyer_key"])
        for i, c in wait_mail.most_common():
            cw.writerow([c] + list(wait_name[i]))
    rep = {"built": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()), "rows": n["rows"], "rows_of_the_ranked_table": n["rows of the ranked table"], "pair_rows": n["pair rows from the contract dataset"],
           "ship_ready": n["ship_ready"], "ship_ready_amount_calculated": n["ship_ready, amount calculated"], "ship_ready_by_kind": dict(ready_kind.most_common()),
           "ship_ready_by_mailbox": dict(ready_mail.most_common()), "by_kind": dict(by_kind.most_common()),
           "by_payment_route": {"%s | %s" % k: v for k, v in sorted(by_route.items(), key=lambda kv: -kv[1])},
           "fail_by_things_missing": {("4 or more" if k == 4 else str(k)): v for k, v in sorted(gap.items())}, "missing": dict(miss.most_common(30)),
           "one_thing_away": {"%s | %s" % k: v for k, v in one.most_common(30)}, "two_things_away": dict(two.most_common(20)),
           "pairs_waiting_for_a_mailbox": n["pairs waiting for a mailbox of their buyer"], "buyers_without_mailbox": len(wait_mail),
           "vendors_whose_number_is_the_last_gap": dict(vend_short.most_common(40)),
           "test": "established and current + the organisation's role mailbox re-read by the referee + paid on invoice by bank transfer (not a card) + the fields of its kind + no flag (owner 2026-11-11 13:00 and 13:09 EST)"}
    json.dump(rep, open(os.path.join(a.out, "relationships.json"), "w", encoding="utf-8"), indent=1, ensure_ascii=False)
    L = ["# Relationship rows — %s" % rep["built"], "",
         "One row per relationship: a Canada-located vendor that bills one organisation. Test of a row (owner 2026-11-11): the relationship is established and current, the organisation's role mailbox was re-read by the referee, the bill is paid on invoice by bank transfer (not a card on file), the fields of its kind are filled, nothing flags it.",
         "", "| | rows |", "|---|---|", "| rows in the table | %d |" % n["rows"], "| — rows of the ranked table (one per buyer) | %d |" % n["rows of the ranked table"],
         "| — further pairs from the contract dataset (same buyer, another Canada-located vendor) | %d |" % n["pair rows from the contract dataset"],
         "| **ship ready** | **%d** |" % n["ship_ready"], "| pairs that wait for a mailbox of their buyer (%d buyers) | %d |" % (len(wait_mail), n["pairs waiting for a mailbox of their buyer"]), "",
         "## Ship ready, by kind", ""] + ["- %s: %d" % kv for kv in ready_kind.most_common()] + ["", "by mailbox kind: " + " · ".join("%s %d" % kv for kv in ready_mail.most_common()), "",
         "## Rows by kind and by how the bill is paid", ""] + ["- %s — %s: %d" % (k[0], k[1], v) for k, v in sorted(by_route.items(), key=lambda kv: -kv[1])] + ["",
         "## Rows that fail", "", "by the number of things missing: " + " · ".join("%s: %d" % (("4 or more" if k == 4 else k), v) for k, v in sorted(gap.items())), "",
         "what is missing, over all rows that fail:", ""] + ["- %s: %d" % kv for kv in miss.most_common(24)] + ["", "## One thing away from ship ready (the work list)", ""] + \
        ["- %s — %s: %d" % (k[0], k[1], v) for k, v in one.most_common(24)] + ["", "## Two things away", ""] + ["- %s: %d" % kv for kv in two.most_common(14)] + ["",
         "## Vendors whose tax or registration number is the last gap (rows)", ""] + ["- %s: %d" % kv for kv in vend_short.most_common(30)] + [""]
    open(os.path.join(a.out, "RELATIONSHIPS.md"), "w", encoding="utf-8").write("\n".join(L))
    print("\n".join(L[:60]))
    print("done in %d s" % (time.time() - t0))


def pair_row(R, x, r, p, g, acc):
    """the row of one further (buyer, vendor) pair: the buyer's side of row x, the vendor and the contract of record r (the pair's best record)"""
    tier_of, award_date, jur_of_record, CUTOFF3, CUR = R["tier_of"], R["award_date"], R["jur_of_record"], R["CUTOFF3"], R["CUR"]
    y = {c: x.get(c, "") for c in BUYER_SIDE}
    c, v, ve, src = r.get("contract") or {}, r.get("vendor") or {}, r.get("vendor_enrichment") or {}, r.get("source") or {}
    d = c.get("dates") or {}
    tier = tier_of(r)
    a = v.get("address") or {}
    status = {"A": "active (published end date today or later)",
              "B": "likely active (" + (("Québec, awarded in the last 3 years, no closing notice" if jur_of_record(r) == "QC" else "source marks it as continuing; awarded in the last 3 years, no end date published")
                                        if r.get("status") == "ongoing_inferred" and award_date(r) >= CUTOFF3 else "awarded in the last 12 months, no end date published") + ")",
              "L": "likely active (awarded 12-36 months ago, no end date published; multi-year contracts often still run)", "C": "end date unknown, awarded over 3 years ago"}.get(tier, "older contract or payment")
    y.update({"rank_group": ("GOLD" if tier in "AB" and g == 4 and acc else "%s%d" % (tier, g)), "tier": tier, "contract_status": status,
              "contract_reference": json.dumps(c.get("identifiers") or {}, ensure_ascii=False)[:3000], "contract_title": (c.get("title") or "")[:200], **R["rec_extra"](c), **R["classify_plus"](c, src.get("key") or ""),
              "contract_value": c.get("value") or "", "currency": c.get("currency") or "", "award_date": award_date(r), "start_date": d.get("start") or "", "end_date": d.get("end") or "",
              "contract_link": r.get("link") or "", "source": src.get("name", ""), "vendor": v.get("name") or "", "vendor_legal_name": ve.get("legal_name") or "",
              "vendor_address": ", ".join(str(t) for t in (a.get("line1"), a.get("city"), a.get("region"), a.get("postal_code")) if t), "vendor_country_basis": v.get("country_basis") or "",
              "vendor_bn9": ve.get("business_number_bn9") or "", "vendor_gst_hst_derived": ve.get("gst_hst_account_derived") or "", "vendor_website": ve.get("website") or "",
              "vendor_emails": "; ".join((t.get("email") or t.get("value") or "") if isinstance(t, dict) else str(t) for t in (ve.get("contact_emails_published") or []))})
    vd = c.get("value_detail") or {}
    if y["contract_value"] and vd.get("value_basis") and "(" not in str(y["contract_value"]):
        y["contract_value"] = "%s (%s)" % (y["contract_value"], str(vd["value_basis"])[:200])
    if y["currency"] == "CAD" and c.get("currency_basis"):
        y["currency"] = "CAD (%s)" % c["currency_basis"]
    for col, val in R["vend_fill"](ve.get("vendor_key") or "", v.get("name") or "").items():
        if not y.get(col) and val:
            y[col] = val
    if y["vendor_bn9"] and not y["vendor_gst_hst_derived"]:
        y["vendor_gst_hst_derived"] = str(y["vendor_bn9"]) + "RT0001"
    if y["contract_value"] and not y["currency"] and CUR.get(jur_of_record(r)):
        y["currency"] = CUR[jur_of_record(r)] + " (derived from the source's government)"
    if not y["contract_link"]:
        y["contract_link"] = src.get("record_url") or src.get("dataset_url") or ""
    if y["contract_reference"] in ("{}", "") and r.get("record_id"):
        y["contract_reference"] = json.dumps({"record_id": r["record_id"]}, ensure_ascii=False)
    if not y.get("end_date") and d.get("end_inferred"):
        y["end_date"] = "%s (inferred: award date + the duration the source publishes; see contract_status)" % str(d["end_inferred"])[:10]
    if not y.get("start_date") and d.get("signed"):
        y["start_date"] = "%s (contract signature date as published)" % str(d["signed"])[:10]
    if not y.get("contract_title") and (y.get("contract_description") or "").strip():
        y["contract_title"] = re.split(r"(?<=[.!?])\s", y["contract_description"].strip(), maxsplit=1)[0][:150] + " (first sentence of the record's description; the source publishes no separate title)"
    vs = y.get("vendor_registry_status") or ""
    segs = [t.strip() for t in vs.split(";") if t.strip()]
    if segs and (_DEAD.search(segs[0]) and not _LIVE.search(segs[0]) or (not any(_LIVE.search(t) for t in segs) and any(_DEAD.search(t) for t in segs))):
        y["vendor_registry_warning"] = "WARNING: registry status '%s' — the match may be a namesake or the vendor may no longer exist; verify before use" % vs[:60]
    kind_label = R["KIND"].get(tier) or ""
    if tier == "C" or "client" in kind_label:
        kind_label = "public contract / purchase award, awarded over 3 years ago, no end date published (dated record)"
    y["relationship_kind"] = kind_label
    y["inference_confidence"] = "n/a (the relationship is a record, not an inference)"
    y["how_relationship_was_found"] = R["HOW_FOUND"].get("A") or ""
    y["relationship_fact_basis"] = record_basis(y)
    y["relationship_detail"] = ("%s (%s, %s) — %s: %s | %s" % (x.get("buyer") or "", x.get("buyer_type") or "", x.get("jurisdiction") or "", kind_label, y["vendor"], y.get("contract_title") or ""))[:400]
    y["recurring_billing"] = "5 not published"
    y["recurring_billing_basis"] = "the public record gives the parties, the subject, the value and the dates of the contract, not when the vendor bills"
    refs = sorted(p["refs"], reverse=True)
    y["records_with_this_vendor"] = str(p["n"])
    y["all_references_with_this_vendor"] = "; ".join("%s [%s] %s %s" % (rf or "(no number)", ad or "undated", val, cur) for ad, rf, val, cur in refs[:12])[:900]
    y["pair_prior_records"] = str(p["n"])
    y["pair_first_or_repeat"] = "single record of this pair in the dataset" if p["n"] == 1 else "%d records of this pair in the dataset (%s to %s)" % (p["n"], min((t[0] for t in refs if t[0]), default="?"), max((t[0] for t in refs if t[0]), default="?"))
    y["pair_dates_and_values"] = "; ".join("%s %s" % (ad, val) for ad, rf, val, cur in refs[:12] if ad or val)[:400]
    ref = (y.get("po_number_as_published") or y.get("contract_or_agreement_number") or y.get("solicitation_or_tender_number") or y.get("award_or_notice_id") or "").strip()
    y["invoice_reference_hint"] = (("purchase-order number: %s" % y["po_number_as_published"]) if y.get("po_number_as_published") else ("contract or agreement number: %s" % y["contract_or_agreement_number"]) if y.get("contract_or_agreement_number")
                                   else ("solicitation / tender number: %s" % y["solicitation_or_tender_number"]) if y.get("solicitation_or_tender_number") else ("award or notice id: %s" % ref) if ref else "")[:300] + ((" — source %s" % src.get("key")) if ref and src.get("key") else "")
    if (not y["invoice_reference_hint"]) and (y.get("po_required_as_published") or "").startswith("yes"):
        y["invoice_reference_hint"] = "the buyer's purchase-order number: the buyer publishes that invoices must quote a PO number (%s)" % y["po_required_as_published"][:200]
    y["other_relationship_sources"] = ""
    y["row_unit"] = "relationship: the same buyer as its row in the ranked table, with another Canada-located vendor of the contract dataset"
    y["relationship_id"] = "%s|%s" % ((x.get("keys") or "").split("|")[0], R["norm"](y["vendor"])[:60])
    y["method_notes"] = (x.get("method_notes") or "") + " | pair row: the buyer's side is copied from its row of the ranked table; the vendor and the contract come from the pair's best record in the contract dataset (tools/relationship_rows.py)"
    return y


if __name__ == "__main__":
    main()
