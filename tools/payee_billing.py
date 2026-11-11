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
rank.py (bill_profile) writes them to the row's bill_* columns when the lane's own reading left them empty.
"""
import re, unicodedata

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
         unpaid="“Permits/Licences are not issued until all fees have been paid.”"),
]

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


COLS = (("bill_delivery_as_published", "delivery"), ("bill_payment_method_as_published", "payment"), ("service_stops_if_unpaid", "unpaid"))


def fill(out, x, name, site):
    """write the body's published facts to the row's empty bill_* cells; returns the entry used (or None)"""
    p = payee_for(name, site)
    if not p:
        return None
    for col, k in COLS:
        if p.get(k) and not out.get(col) and not str(x.get(col) or "").strip():
            out[col] = "%s (%s, read %s)" % (p[k], p["url"], p["read"])
    return p


if __name__ == "__main__":
    for p in PAYEES:
        for k in ("period", "delivery", "payment", "terms", "unpaid", "remit_to"):
            if p.get(k):
                for q in re.findall(r"“([^”]+)”", p[k]):
                    assert len(q) <= 300, (p["names"][0], k, len(q))
        print("%-34s %s" % (p["names"][0], ", ".join(k for k in ("period", "delivery", "payment", "terms", "unpaid", "remit_to") if p.get(k))))
