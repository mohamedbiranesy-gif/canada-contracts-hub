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
         unpaid="“Permits/Licences are not issued until all fees have been paid.”"),
    # a firm of patent and trademark agents: its own page on paying an invoice (the agent-of-record lane: the owner of a mark or a patent is its client)
    dict(names=["SMART & BIGGAR LP", "SMART & BIGGAR LLP", "SMART & BIGGAR", "Smart & Biggar"], hosts=["smartbiggar.ca"], read="2026-11-11",
         url="https://www.smartbiggar.ca/payment-options",
         delivery="the firm's invoice, quoted by its number when it is paid: “Please ensure to provide the invoice number(s), or the payment is subject to return.”",
         payment=("Interac e-Transfer, electronic funds transfer or cheque (a card through the firm's payment page as well): “You can pay your invoice using one of the following methods: "
                  "Interac e-Transfer: Send funds to remittance@smartbiggar.ca .” … “Electronic Fund Transfer: Send requests for banking details to ar@smartbiggar.ca . By cheque: Send to "
                  "PO Box 2999 Station D Ottawa, ON, K1P 5Y6 Canada.”"),
         remit_to="“By cheque: Send to PO Box 2999 Station D Ottawa, ON, K1P 5Y6 Canada.”"),
    # a body that says it sends no invoice: its registrants are not billed "on invoice" (owner 2026-11-11) and the row says so in the body's words
    dict(names=["Ontario Motor Vehicle Industry Council (OMVIC)", "Ontario Motor Vehicle Industry Council", "OMVIC"], hosts=["omvic.ca"], read="2026-11-11",
         url="https://www.omvic.ca/selling/fees/transaction-fees/",
         no_invoice="“OMVIC does not issue invoices. Dealers are expected to self-report and remit payment with their renewal application.”"),
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
    return _hashlib.sha1(_json.dumps({k: p.get(k) for k in ("url",) + FACTS}, sort_keys=True, ensure_ascii=False).encode()).hexdigest()[:16]


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


COLS = (("bill_delivery_as_published", "delivery"), ("bill_payment_method_as_published", "payment"), ("service_stops_if_unpaid", "unpaid"))


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
        quotes = [q for k in FACTS for q in re.findall(r"“([^”]+)”", p.get(k) or "")]
        if not quotes or any(len(q) > 300 for q in quotes):
            n["no quote, or a quote over 300 characters"] += 1
            continue
        if not C.allowed(p["url"]):
            n["the page's robots.txt does not allow the reader"] += 1
            continue
        st, ct, data, final = C.fetch(p["url"])
        time.sleep(1.0)
        if st != 200 or not data:
            n["page not read (%s)" % st] += 1
            continue
        text = flat(C.visible(C.quote_attrs(html.unescape(data.decode("utf-8", "replace")))))
        miss = [q for q in quotes if flat(q) not in text]
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
            out[col] = "%s (%s, read %s)" % (p[k], p["url"], p["read"])
    if p.get("no_invoice"):
        out["bill_delivery_as_published"] = "no invoice is sent: %s (%s, read %s)" % (p["no_invoice"], p["url"], p["read"])
    return p


if __name__ == "__main__" and len(__import__("sys").argv) > 1 and __import__("sys").argv[1] == "verify":
    verify()
elif __name__ == "__main__":
    for p in PAYEES:
        for k in ("period", "delivery", "payment", "terms", "unpaid", "remit_to"):
            if p.get(k):
                for q in re.findall(r"“([^”]+)”", p[k]):
                    assert len(q) <= 300, (p["names"][0], k, len(q))
        print("%-34s %s" % (p["names"][0], ", ".join(k for k in ("period", "delivery", "payment", "terms", "unpaid", "remit_to") if p.get(k))))
