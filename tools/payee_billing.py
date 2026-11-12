#!/usr/bin/env python3
"""How the bodies behind the register, roster and licence lanes send their bill and take the money — each line a quote from the body's own page.

Owner, 2026-11-11 (13:09, 13:58, 14:20 EST): a row needs a bill that comes "on invoice" and can be paid "by bank transfer"; "any Canadian
entity" may be the one that sends it (a regulator, a city, an association); "don't forget all invoice details … tailor to each". A software
vendor's terms are read by tools/vendor_billing.py and the hand-read ones sit in tools/tech_relationships.py (BILLING_BY_DOMAIN). The bodies
here are not vendors with a price page: a regulator's "how to pay your licence" page, a city's "paying an invoice" page. A few bodies carry
thousands of rows each (the Régie du bâtiment du Québec: 4,179 on 2026-11-11), so they are read one by one, with the project's reader, and
every value below is a sentence of the page named beside it (at most 300 characters, as written on the page the day it was read).

Keys of an entry: names (the body's name as rows carry it, compared without accents, case or punctuation), hosts (the body's own site: a row's
vendor site that ends with one of them), url + read (the page and the day), and the published facts:
  period    how often the body bills                     delivery  how the bill reaches the payer
  payment   how it can be paid (the words the owner's test reads: a bank payment, a cheque, a card)
  terms     when it is due                               unpaid    what happens when it is not paid
  remit_to  where a payment by mail goes (the body's own printed address)
A fact read on another page of the body carries that page beside it (delivery_url, remit_to_url, …). rank.py (bill_profile) writes them to the
row's bill_* columns when the lane's own reading left them empty; the amount of one licence comes from tools/payee_fees.py (the body's own list
of open invoices, or its fee schedule).
"""
import collections, re, unicodedata

norm = lambda s: re.sub(r"[^a-z0-9]+", " ", unicodedata.normalize("NFKD", s or "").encode("ascii", "ignore").decode().lower()).strip()

PAYEES = [
    dict(names=["Régie du bâtiment du Québec", "Regie du batiment du Quebec (RBQ)", "RBQ"], hosts=["rbq.gouv.qc.ca"], read="2026-11-11",
         url="https://www.rbq.gouv.qc.ca/licence/repondre-a-ses-obligations/payer-le-maintien-de-sa-licence",
         period="“Chaque année, vous devez payer votre licence pour la maintenir.”",
         delivery="a notice of assessment by mail: “Un avis de cotisation vous sera envoyé par la poste 60 jours avant l’échéance de votre licence.”",
         payment=("through a financial institution's online banking, or by cheque / postal money order: “Vous pouvez effectuer le paiement de votre licence de deux façons : en ligne : pour ce faire, "
                  "consultez la page Paiement en ligne ou sur le site Internet des institutions financières suivantes : Caisses Desjardins, Banque Nationale et Banque Laurentienne.” … "
                  "“par la poste : en envoyant un chèque ou un mandat-poste à notre bureau de”"),
         unpaid="“Si vous n’avez pas acquitté les droits et frais de maintien de votre licence à son échéance, elle cessera d’avoir effet.”"),
    dict(names=["The City of Calgary", "City of Calgary"], hosts=["calgary.ca"], read="2026-11-11",
         url="https://www.calgary.ca/buy-sell/buy-from-city/invoices.html",
         delivery="an invoice of the City (its page on paying one): “For any inquiries about the invoice you’ve received, please refer to the contact details listed on the top of your invoice.”",
         payment=("through a bank (online banking, ATM, telephone, in person) or by cheque / money order: “Pay through your bank Payments can be made in person, via ATM, phone and online banking at most "
                  "chartered banks, trust companies, credit unions, and Alberta Treasury Branches.” … “Mail a cheque or money order payable to \"The City of Calgary.\" Write your customer number "
                  "and/or invoice number on the cheque and enclose the return portion of your invoice.”"),
         terms="“Payment is due 30 days from the date of the invoice.”",
         unpaid="“Interest of 1.5% per month will be charged on any unpaid balance.”",
         remit_to="“The City of Calgary Attn: Chief Cashier 8042 P.O. Box 2100, Station M Calgary, Alberta, Canada T2P 2M5”"),
    dict(names=["City of Edmonton", "The City of Edmonton"], hosts=["edmonton.ca"], read="2026-11-11",
         url="https://www.edmonton.ca/business_economy/pay-licence-and-permit-fees",
         payment=("cheque, bank debit, electronic funds transfer or a card: “We accept the following payment types: Cash, Personal and Company Cheques, Money Orders, Bank Debit Cards (Interac), Visa, "
                  "MasterCard, and American Express.” … “Electronic Funds Transfer (EFT) can be used to pay for City services such as permits, licences and land development applications. "
                  "It’s limited to payments of $10,000 and over.”"),
         delivery=("a renewal notice by mail, which states the fee: “A renewal notice will be sent to the mailing address on file approximately 45 days before your licence expires.” … "
                   "“Your new licensing fees will be displayed on your renewal notice that you receive by mail.”"),
         delivery_url="https://www.edmonton.ca/business_economy/licences_permits/renew-your-business-licence",
         remit_to=("“Urban Planning and Economy City of Edmonton PO Box 2670 Edmonton, Alberta T5J 2G4” — “Include the top portion of your renewal notice, and write your account number on your "
                   "cheque or money order.”"),
         remit_to_url="https://www.edmonton.ca/business_economy/licences_permits/renew-your-business-licence",
         unpaid="“Permits/Licences are not issued until all fees have been paid.”"),
    # the City of Toronto: every kind of licence has its own page with the same four sentences (the page read here is the one for building renovators);
    # the City also publishes, every night, its list of outstanding licence invoices (tools/payee_fees.py reads it and the fee of each kind of licence)
    dict(names=["City of Toronto", "The City of Toronto"], hosts=["toronto.ca"], read="2026-11-11",
         url="https://www.toronto.ca/services-payments/permits-licences-bylaws/building-renovators/",
         period="“Your licence will expire annually on the anniversary of the date that the licence was first issued.”",
         delivery=("a renewal notice by mail and a renewal invoice: “A courtesy notice will be mailed to your mailing address on file identifying any documents required to renew the licence.” … "
                   "“Find your outstanding business licence or permit renewal invoice”"),
         payment=("in person, online (by credit card, with the invoice number) or by cheque: “Licence renewal fees can be made in-person, paid online or by sending a cheque.” … "
                  "“Once you have your invoice number, you can pay online using a credit card.” (the second sentence is on the City's list of outstanding invoices, "
                  "https://www.toronto.ca/data/mls/invoices/index.html)"),
         unpaid="“If you fail to renew your licence according to the bylaw, your licence will be cancelled and you will have to reapply.”"),
    # the Canadian Intellectual Property Office: how its fees can be paid. Its page does not say that it sends an invoice or a notice for a fee,
    # so nothing is written about how the bill arrives, and the owner's test says so on the rows it bills directly.
    dict(names=["Canadian Intellectual Property Office", "Canadian Intellectual Property Office (CIPO)", "CIPO"], hosts=["opic-cipo.gc.ca", "cipo.ic.gc.ca"], read="2026-11-11",
         url="https://ised-isde.canada.ca/site/canadian-intellectual-property-office/en/payments-and-fees/methods-payment-accepted",
         payment=("a cheque, a wire transfer or direct deposit, a deposit account or a credit card: “All cheques and money orders must be in Canadian dollars and made payable to the Receiver General "
                  "for Canada.” … “All electronic funds transfers (wire transfers or direct deposits) must be made through the Bank of Nova Scotia in Canadian dollars and be made payable to the "
                  "Receiver General for Canada.”")),
    # a firm of patent and trademark agents: its own page on paying an invoice (the agent-of-record lane: the owner of a mark or a patent is its client)
    dict(names=["SMART & BIGGAR LP", "SMART & BIGGAR LLP", "SMART & BIGGAR", "Smart & Biggar"], hosts=["smartbiggar.ca"], read="2026-11-11",
         url="https://www.smartbiggar.ca/payment-options",
         delivery="the firm's invoice, quoted by its number when it is paid: “Please ensure to provide the invoice number(s), or the payment is subject to return.”",
         payment=("Interac e-Transfer, electronic funds transfer or cheque (a card through the firm's payment page as well): “You can pay your invoice using one of the following methods: "
                  "Interac e-Transfer: Send funds to remittance@smartbiggar.ca .” … “Electronic Fund Transfer: Send requests for banking details to ar@smartbiggar.ca . By cheque: Send to "
                  "PO Box 2999 Station D Ottawa, ON, K1P 5Y6 Canada.”"),
         remit_to="“By cheque: Send to PO Box 2999 Station D Ottawa, ON, K1P 5Y6 Canada.”"),
    # the Québec liquor regulator: an invoice with an 11-digit reference number, paid through a financial institution or by cheque; yearly fees by permit
    dict(names=["Régie des alcools, des courses et des jeux", "Regie des alcools, des courses et des jeux (RACJ)", "RACJ"], hosts=["racj.gouv.qc.ca"], read="2026-11-11",
         url="https://www.racj.gouv.qc.ca/alcool/vendre-ou-servir-des-boissons-alcooliques-pour-consommation-sur-place/boite-a-outils-consommation-sur-place/modes-de-paiement-pour-le-secteur-de-lalcool-detaillants",
         period=("yearly: “Ce mode de paiement est offert seulement pour le paiement des frais et droits payables annuels liés à certains permis d’alcool (bar, restaurant, accessoire, épicerie, "
                 "vendeur de cidre, centre de vinification et de brassage).”"),
         delivery="an invoice with its due date: “Le montant indiqué sur toute facture doit être acquitté avant la date d’échéance qui y est indiquée.”",
         payment=("cheque, postal money order or bank draft by mail, or through a participating financial institution with the invoice's reference number: “Le chèque, le mandat-poste ou la traite "
                  "bancaire, à transmettre par la poste, doivent être libellés à l’ordre du ministre des Finances et le numéro du permis ou de l’établissement doit y être inscrit.” … “Une fois le bon "
                  "fournisseur sélectionné, le numéro de référence de 11 chiffres se trouvant en haut à droite de la facture doit être utilisé.”"),
         unpaid=("“Le défaut d’avoir payé une facture à la date d’échéance qui y est indiquée pourrait entraîner un refus de la délivrance de permis et de licences et autorisations ou leur "
                 "révocation sans autre avis ni délai.”"),
         # the yearly fee by kind of permit, from the Régie's fee table (the second amount of each line is the column “Droits annuels exigés”)
         amounts_url="https://www.racj.gouv.qc.ca/alcool/boite-a-outils/frais-et-droits-payables-se-rattachant-au-secteur-de-lalcool",
         amounts=[(r"\brestaurant\b", "688 $ a year", "“Permis de restaurant Frais d'étude et droits à payer au moment de la transmission de la demande Droits annuels exigés* Nouvel établissement (où aucun permis n'est en vigueur) ou nouvelle demande 289 $** 688 $”"),
                  (r"\bbar\b", "688 $ a year", "“Permis de bar Frais d'étude et droits à payer au moment de la transmission de la demande Droits annuels exigés* Nouvel établissement (où aucun permis n'est en vigueur) ou nouvelle demande 289 $** 688 $”"),
                  (r"\baccessoire\b", "403 $ a year", "“Permis accessoire Frais d'étude et droits à payer au moment de la transmission de la demande Droits annuels exigés* Nouvel établissement (où aucun permis n'est en vigueur) ou nouvelle demande 289 $** 403 $”"),
                  (r"[ée]picerie", "202 $ a year", "“Permis d'épicerie Frais d'étude et droits à payer au moment de la transmission de la demande Droits annuels exigés Nouvel établissement (où aucun permis n'est en vigueur) ou nouvelle demande 169 $ 202 $”")]),
    # a body that says it sends no invoice: its registrants are not billed "on invoice" (owner 2026-11-11) and the row says so in the body's words
    dict(names=["Ontario Motor Vehicle Industry Council (OMVIC)", "Ontario Motor Vehicle Industry Council", "OMVIC"], hosts=["omvic.ca"], read="2026-11-11",
         url="https://www.omvic.ca/selling/fees/transaction-fees/",
         no_invoice="“OMVIC does not issue invoices. Dealers are expected to self-report and remit payment with their renewal application.”"),
    # Health Canada: the yearly right-to-sell fees of drugs and medical devices (tools/hc_registers.py); its page on paying its invoices, read 2026-11-12
    dict(names=["Health Canada", "Santé Canada", "Sante Canada"], hosts=[], read="2026-11-12",
         url="https://www.canada.ca/en/health-canada/services/funding/cost-recovery-service-fees/how-pay-fees.html",
         payment=("through a Canadian financial institution's bill payment, direct deposit, wire transfer, cheque, bank draft or money order, or a card: “Payments can be "
                  "made by applying an existing credit, payment through a Canadian Financial Institution (via Bill Payment Service - BPS), direct deposit, wire transfer, "
                  "cheque, bank draft, money order, or credit card.”"),
         remit_to=("“Health Canada Accounts Receivable, Address Locator: 1918B 18th Floor, Room 1804B, Jeanne-Mance Building 161 Goldenrod Driveway, Tunney's Pasture "
                   "Ottawa, Ontario K1A 0K9” — “Please include your Health Canada customer number or group account number on the Cheque, Money Order or Bank Draft”")),
    # ISED: the yearly radio licence invoice (tools/radio_licences.py); its page on paying a radio authorization invoice, read 2026-11-12
    dict(names=["Innovation, Science and Economic Development Canada", "Innovation, Sciences et Développement économique Canada", "ISED", "ISDE"], hosts=[], read="2026-11-12",
         url="https://ised-isde.canada.ca/site/spectrum-management-system/en/pay-online",
         payment=("by wire transfer or direct deposit to the Receiver General for Canada at The Bank of Nova Scotia, by cheque or money order, or online: “Other payment "
                  "options Wire transfer Use the following information to complete a wire transfer payment: Bank Name : The Bank of Nova Scotia 4715 Tahoe Blvd, Mississauga "
                  "ON L4W 0B4” — “For payment by cheque or money order made payable to the Receiver General for Canada, include your account number and the invoice number, "
                  "both available on your invoice or on your email notification”"),
         delivery="an invoice every year: “They are used to calculate licence renewal invoices and for any new or amended licences issued throughout the fiscal year.”",
         delivery_url=("https://ised-isde.canada.ca/site/spectrum-management-telecommunications/en/licences-and-certificates/radiocom-information-circulars-ric/"
                       "ric-42-guide-calculating-radio-licence-fees"),
         period="“The annual fee for the renewal of a radio licence is payable before the radio licence expires on March 31 of each year.”",
         period_url=("https://ised-isde.canada.ca/site/spectrum-management-telecommunications/en/licences-and-certificates/radiocom-information-circulars-ric/"
                     "ric-42-guide-calculating-radio-licence-fees"),
         remit_to="“By courier to the following address: ISED – Spectrum Revenue Centre 235 Queen Street, Room 643A Ottawa ON K1A 0H5”"),
]

# ---- entries added by any lane (2026-11-11): contrib/<lane>/payees/<key>.json, one body a file, the same keys as an entry above ------------------
# {"names": [...], "hosts": [...], "url": "...", "read": "YYYY-MM-DD", "payment": "…“quote”…", "delivery": "…", "period": "…", "terms": "…", "unpaid": "…",
#  "remit_to": "…", "no_invoice": "…“the body's own sentence that it sends no invoice”…"}
# An entry from a file is used only once `payee_billing.py verify` has opened its page with the project's reader and found every quoted sentence on
# it (data/incoming/claude/payee_verified.json); an entry whose page refuses the reader, or whose quote is not on the page, is not used.
import glob as _glob, hashlib as _hashlib, json as _json, os as _os
_ROOT = _os.path.abspath(_os.path.join(_os.path.dirname(__file__), ".."))
VERIFIED = _os.path.join(_ROOT, "data/incoming/claude/payee_verified.json")
FACTS = ("period", "delivery", "payment", "terms", "unpaid", "remit_to", "no_invoice")


def _sig(p):
    keys = ("url",) + FACTS + tuple(k + "_url" for k in FACTS if p.get(k + "_url")) + tuple(k for k in ("amounts", "amounts_url") if p.get(k))
    return _hashlib.sha1(_json.dumps({k: p.get(k) for k in keys}, sort_keys=True, ensure_ascii=False).encode()).hexdigest()[:16]


def file_entries():
    out = []
    for f in sorted(_glob.glob(_os.path.join(_ROOT, "contrib/*/payees/*.json")) + _glob.glob(_os.path.join(_ROOT, "tools/data/payees/*.json"))):
        try:
            p = _json.load(open(f, encoding="utf-8"))
        except ValueError:
            continue
        if isinstance(p, dict) and p.get("names") and p.get("url") and p.get("read") and any(p.get(k) for k in FACTS):
            p.setdefault("hosts", []); p["_file"] = _os.path.relpath(f, _ROOT)
            out.append(p)
    return out


def _load_verified():
    try:
        return _json.load(open(VERIFIED, encoding="utf-8"))
    except (OSError, ValueError):
        return {}


_ok = _load_verified()
PAYEES += [p for p in file_entries() if _ok.get(p["_file"], {}).get("sig") == _sig(p)]
_BY_NAME = {norm(n): p for p in PAYEES for n in p["names"]}


def payee_for(name="", site=""):
    """the entry of a body, by its name as the row carries it, or by its own site"""
    p = _BY_NAME.get(norm(name))
    if p:
        return p
    host = re.sub(r"^https?://", "", (site or "").strip().lower()).split("/")[0].split(":")[0]
    host = host[4:] if host.startswith("www.") else host
    if host:
        for p in PAYEES:
            if any(host == h or host.endswith("." + h) for h in p["hosts"]):
                return p
    return None


COLS = (("bill_delivery_as_published", "delivery"), ("bill_payment_method_as_published", "payment"), ("service_stops_if_unpaid", "unpaid"),
        ("bill_due_terms_as_published", "terms"), ("bill_remit_to_as_published", "remit_to"))


def verify():
    """open each file entry's page with the project's reader and look for every quoted sentence on it; write what holds to VERIFIED"""
    import html, sys, time
    sys.path.insert(0, _os.path.dirname(_os.path.abspath(__file__)))
    import ap_crawler as C
    flat = lambda t: re.sub(r"\s+", " ", t).strip()
    ok, n = _load_verified(), collections.Counter()
    for p in file_entries():
        f = p["_file"]
        if ok.get(f, {}).get("sig") == _sig(p):
            n["verified before"] += 1
            continue
        by_url = collections.defaultdict(list)
        for k in FACTS:
            by_url[p.get(k + "_url") or p["url"]] += re.findall(r"“([^”]+)”", p.get(k) or "")
        try:  # a fee table: [[a pattern of the licence kind, the amount in words, the “line of the table”], …] on the page amounts_url
            for rx, amount, quote in p.get("amounts") or ():
                re.compile(rx)
                by_url[p.get("amounts_url") or p["url"]] += re.findall(r"“([^”]+)”", quote)
        except (ValueError, TypeError, re.error):
            n["a fee table that is not [pattern, amount, quoted line] lines"] += 1
            continue
        quotes = [q for qs in by_url.values() for q in qs]
        if not quotes or any(len(q) > 300 for q in quotes):
            n["no quote, or a quote over 300 characters"] += 1
            continue
        miss, why = [], ""
        for url, qs in by_url.items():
            if not qs:
                continue
            if not C.allowed(url):
                why = "the page's robots.txt does not allow the reader"
                break
            st, ct, data, final = C.fetch(url)
            time.sleep(1.0)
            if st != 200 or not data:
                why = "page not read (%s)" % st
                break
            pdf = data[:5] == b"%PDF-" or "pdf" in (ct or "").lower()
            text = flat(C.pdf_text(data) or "") if pdf else flat(C.visible(C.quote_attrs(html.unescape(data.decode("utf-8", "replace")))))
            miss += [q for q in qs if flat(q) not in text]
        if why:
            n[why] += 1
            continue
        if miss:
            n["a quoted sentence is not on the page"] += 1
            print("not verified: %s — “%s”" % (f, miss[0][:120]))
            continue
        ok[f] = {"sig": _sig(p), "verified": time.strftime("%Y-%m-%d"), "url": p["url"], "quotes": len(quotes)}
        n["verified now"] += 1
    _os.makedirs(_os.path.dirname(VERIFIED), exist_ok=True)
    _json.dump(ok, open(VERIFIED, "w", encoding="utf-8"), indent=1, sort_keys=True)
    print("payee entries from files: %s" % dict(n))


def fill(out, x, name, site):
    """write the body's published facts to the row's empty bill_* cells; returns the entry used (or None)"""
    p = payee_for(name, site)
    if not p:
        return None
    for col, k in COLS:
        if p.get(k) and not out.get(col) and not str(x.get(col) or "").strip():
            out[col] = "%s (%s, read %s)" % (p[k], p.get(k + "_url") or p["url"], p["read"])
    if p.get("no_invoice"):
        out["bill_delivery_as_published"] = "no invoice is sent: %s (%s, read %s)" % (p["no_invoice"], p["url"], p["read"])
    if p.get("amounts") and not out.get("bill_amount_indicative") and not str(x.get("bill_amount_indicative") or "").strip() and not str(x.get("contract_value") or "").strip():
        title = " ".join(str(x.get(c) or "") for c in ("contract_title", "contract_description", "instrument_type"))
        for rx, amount, quote in p["amounts"]:
            if re.search(rx, title, re.I):
                out["bill_amount_indicative"] = amount
                out["bill_amount_basis"] = "the body's own fee table, for this kind of licence: %s (%s, read %s)" % (quote, p.get("amounts_url") or p["url"], p["read"])
                break
    if (str(x.get("contract_status") or "").startswith("holder of licence") and not out.get("bill_amount_indicative") and not out.get("bill_amount_calculated")
            and not str(x.get("bill_amount_indicative") or "").strip() and not str(x.get("contract_value") or "").strip()):
        import payee_fees
        r = payee_fees.amount(p["names"][0], x)
        if r and r["calculated"]:
            out["bill_amount_calculated"] = "calculated — %s: %s" % (r["amount"], r["basis"].split("calculated — ", 1)[-1])
        elif r:
            out["bill_amount_indicative"], out["bill_amount_basis"] = r["amount"], r["basis"]
        if r and r.get("bill_number") and not out.get("bill_identifier_format") and not str(x.get("bill_identifier_format") or "").strip():
            out["bill_identifier_format"] = "%s, as the body's own list of open invoices gives it for this licence" % r["bill_number"]
        if r and r.get("delivery"):
            out["bill_delivery_as_published"] = r["delivery"] + ("; " + out["bill_delivery_as_published"] if out.get("bill_delivery_as_published") else "")
    return p


if __name__ == "__main__" and len(__import__("sys").argv) > 1 and __import__("sys").argv[1] == "verify":
    verify()
elif __name__ == "__main__":
    for p in PAYEES:
        for k in ("period", "delivery", "payment", "terms", "unpaid", "remit_to"):
            if p.get(k):
                for q in re.findall(r"“([^”]+)”", p[k]):
                    assert len(q) <= 300, (p["names"][0], k, len(q))
        for rx, amount, quote in p.get("amounts") or ():
            assert len(quote) <= 302, (p["names"][0], rx, len(quote))
        print("%-34s %s" % (p["names"][0], ", ".join(k for k in ("period", "delivery", "payment", "terms", "unpaid", "remit_to") if p.get(k))))
