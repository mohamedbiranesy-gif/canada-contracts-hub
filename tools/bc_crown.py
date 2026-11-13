#!/usr/bin/env python3
"""The Province of British Columbia's own bills to organisations, read from its own open data -> relationship leads (cloud; no AI, no search engine).

water     Every holder of a current water licence is billed a yearly water rental by the Province. Its own words: "When a water licence is issued,
          annual water rentals are assessed." "Depending on the amount of annual rental payable, clients are billed in the following manner: Twice a
          year if the annual rental is over $100,000.00 / Once a year for all other annual rentals less than $100,000.00." "Our statements are sent to
          the client(s) we currently have registered on record as the water licence holder." (its FAQ about water billing). Paid by "Online banking for
          water rental fees" or by cheque "made out to "Minister of Finance"" (FrontCounter BC payment guidelines). The Province publishes every point
          of diversion of every water licence — the licence number, its status, its purpose, the licensed quantity, the primary licensee's name (with
          its client number), address and postal code (BC Data Catalogue, Water Rights Licences – Public, Open Government Licence – British Columbia).
          "Application fees and annual rentals are not required from Provincial or federal ministries / First Nations using water on reserve land"
          (the Province's page on fees and rentals): those holders are left out, and so are domestic groundwater licences ("Domestic groundwater users
          are not required to pay water rentals"). The yearly rental of each licence is calculated from its published quantity and purpose with the
          published rates (Water Sustainability Fees, Rentals and Charges Tariff Regulation, B.C. Reg. 37/2016, Schedule 2, Table 1: the greater of the
          minimum annual rental and the quantity-based rental) and labelled "calculated"; the purposes the regulation rates another way (waterworks and
          irrigation of a local provider, pulp mills, power) are not calculated and the row says so.
stumpage  Every client the Harvest Billing System bills stumpage: its public "Billing Summary" report (by date of invoice, for each area of the province
          and each scale type, at most 12 months a request) lists every invoice — its number, the client it is billed to, the timber mark, the volume,
          the value, the billing date — and the harvesting authorities layer (WHSE_FOREST_TENURE.FTEN_HARVEST_AUTH_POLY_SVW) names each client number.
          The Province's own words: "Billing Notices are issued one day after invoices are sent and show details about the items on your invoices.
          Notices are mailed to your main location address." "Statements of Account are issued on the 23rd of each month and mailed to your main
          location address." "Your stumpage and export fees are due upon receipt of your invoice." Payable "Through your bank or financial institution"
          ("EFTs and wire transfers can take up to three days to get from your bank to us"), online with eTaxBC, or by cheque to the Minister of
          Finance; "Credit card payments are not accepted." A client whose latest invoice is at most 183 days old is a current relationship.

Natural persons are left out (organisations only). No e-mail is read from either register (they have none). A row needs the organisation's own
site, tied the way the other register lanes tie one (tools/hc_registers.py): a site on file printing the holder's postal code under a name that
agrees, a website an Overture place at that postal code lists (kept on the site's own pages), or the company-name autocomplete under the holder's
very name (kept when the site's own home page carries it); then the mailbox crawl reads its role mailbox (lead_shards/).

  pull-water --work W        the water licences layer (WFS pages of 10,000, no geometry) -> W/wls_*.json
  build-water --work W       -> data/incoming/claude/bcgov/bc_water_licensees.csv.gz (one line per licensee that is an organisation)
  pull-stumpage --work W     the Billing Summary reports (a100.gov.bc.ca asks a 10-second crawl delay) and the harvesting authorities' client names
  build-stumpage --work W    -> data/incoming/claude/bcgov/bc_stumpage_clients.csv.gz (+ bc_stumpage_invoices.csv.gz, the invoices of those clients)
  pull-aer --work W          the AER's ST37 Excel package, when newer than the last build's
  build-aer --work W         -> data/incoming/claude/bcgov/ab_aer_licensees.csv.gz (one line per licensee of a drilled well in force; Alberta)
  pull-pmra / build-pmra     the PMRA's product extract -> data/incoming/claude/bcgov/hc_pmra_registrants.csv.gz (registrants of current products)
  sites --minutes M          each holder's own site -> bcgov/bc_sites.csv (+ bc_sites_done.tsv: names the autocomplete was asked)
  leads --stamp S            -> lead_shards/leads_bcgov_S.gz + details_bcgov_S.gz (new leads only)
"""
import argparse, collections, csv, datetime, glob, gzip, hashlib, json, os, re, subprocess, sys, threading, time, urllib.parse, urllib.request

csv.field_size_limit(1 << 30)
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import hc_registers as HR  # noqa: E402  (the site finder)
import radio_licences as RL  # noqa: E402  (is_org, FEDERAL)

INC = os.path.join(ROOT, "data/incoming/claude")
DIR = os.path.join(INC, "bcgov")
SHARDS = os.path.join(INC, "lead_shards")
UA = HR.UA
TODAY = time.strftime("%Y-%m-%d")
READ = "2026-11-13"
WFS = "https://openmaps.gov.bc.ca/geo/pub/wfs"
WLS = "WHSE_WATER_MANAGEMENT.WLS_WATER_RIGHTS_LICENCES_SV"
FTA = "WHSE_FOREST_TENURE.FTEN_HARVEST_AUTH_POLY_SVW"
WLS_PAGE = "https://catalogue.data.gov.bc.ca/dataset/water-rights-licences-public"
FTA_PAGE = "https://catalogue.data.gov.bc.ca/dataset/harvest-authorities-all"
HBS = "https://a100.gov.bc.ca/pub/hbs/"
HBS_FORM = "https://a100.gov.bc.ca/pub/hbs/opq/P421.jsp?actionType=New"
WATER_BODY = "Province of British Columbia — Water Management Branch (water rentals)"
STUMP_BODY = "Province of British Columbia — Ministry of Forests (stumpage)"
# the Province's own sentences, as its pages print them (read 2026-11-13 with the project's reader)
FAQ = ("https://www2.gov.bc.ca/gov/content/environment/air-land-water/water/water-licensing-rights/water-licences-approvals/water-application-fees-rental-rates/"
       "frequently-asked-questions-about-water-billing")
FEES = "https://www2.gov.bc.ca/gov/content/environment/air-land-water/water/water-licensing-rights/water-licences-approvals/water-application-fees-rental-rates"
FCBC_PAY = "https://www2.gov.bc.ca/gov/content/industry/natural-resource-use/natural-resource-permits/fcbc-locations/fcbc-payment-guidelines"
FCBC_LOC = "https://www2.gov.bc.ca/gov/content/industry/natural-resource-use/natural-resource-permits/fcbc-locations"
TARIFF = "https://free.bcpublications.ca/civix/document/id/complete/statreg/37_2016"
ST_PAY = "https://www2.gov.bc.ca/gov/content/taxes/natural-resource-taxes/forestry/stumpage/pay"
ST_MAIN = "https://www2.gov.bc.ca/gov/content/taxes/natural-resource-taxes/forestry/stumpage"
ST_OVERDUE = "https://www2.gov.bc.ca/gov/content/taxes/natural-resource-taxes/forestry/stumpage/pay/overdue"
W_ASSESSED = "When a water licence is issued, annual water rentals are assessed."
W_STATEMENT = "Your statement reflects your annual rental charge for the right to use the water allocated to you under your water licence."
W_ONCE = "Once a year for all other annual rentals less than $100,000.00."
W_TWICE = "Twice a year if the annual rental is over $100,000.00"
W_TO = "Our statements are sent to the client(s) we currently have registered on record as the water licence holder."
W_MIN = "However, the water rental will be the same – that is, default to the minimum of $50.00."
W_OVERDUE = "If an overdue account is not settled within a reasonable amount of time, it runs the risk of being forwarded to a collection agency."
W_BANK = "Online banking for water rental fees"
W_CHEQUE = "Must be made out to \"Minister of Finance\""
W_MAIL = "Mail to a FrontCounter BC location"
S_NOTICE = "Billing Notices are issued one day after invoices are sent and show details about the items on your invoices. Notices are mailed to your main location address."
S_STATEMENT = "Statements of Account are issued on the 23rd of each month and mailed to your main location address."
S_DUE = "Your stumpage and export fees are due upon receipt of your invoice."
S_BANK = "EFTs and wire transfers can take up to three days to get from your bank to us."
S_NOCARD = "Credit card payments are not accepted."
S_INTEREST = "Interest applies to all overdue accounts at a rate of prime plus 3%."
S_REMIT = "Collection Loan Management Group Ministry of Finance PO Box 9990 Stn Prov Govt Victoria BC V8W 9R7"
# FrontCounter BC's regional offices, as its locations page prints them; a water rental paid by mail goes to a FrontCounter BC location
OFFICES = {"Cariboo": "Williams Lake - regional office 120 - 640 Borland Street Williams Lake, BC V2G 4T1",
           "Kootenay-Boundary": "Cranbrook - regional office 1902 Theatre Road Cranbrook, BC V1C 7G1",
           "Northeast": "Fort St. John - regional office 100 - 10003 110 Avenue Fort St. John, BC V1J 6M7",
           "Omineca": "Prince George - regional office 5th Floor - 499 George Street Prince George, BC V2L 1R5",
           "Thompson-Okanagan": "Kamloops - regional office 441 Columbia Street Kamloops, BC V2C 2T3",
           "Skeena": "Smithers - regional office 1st Floor - 3726 Alfred Avenue, PO Box 3969 Smithers, BC V0J 2N0",
           "South Coast": "Surrey - regional office 200 - 10428 153rd Street Surrey, BC V3R 1E1",
           "West Coast": "Nanaimo - regional office 142 - 2080 Labieux Road Nanaimo, BC V9T 6J9"}
# the water district of a licence (its DISTRICT_PRECINCT_NAME) -> the natural resource region of FrontCounter BC's locations page
REGION = {"Nelson": "Kootenay-Boundary", "Kaslo": "Kootenay-Boundary", "Grand Forks": "Kootenay-Boundary", "Golden": "Kootenay-Boundary",
          "Fernie": "Kootenay-Boundary", "Cranbrook": "Kootenay-Boundary", "Revelstoke": "Thompson-Okanagan", "Kamloops": "Thompson-Okanagan",
          "Vernon": "Thompson-Okanagan", "Ashcroft": "Thompson-Okanagan", "Penticton": "Thompson-Okanagan", "Princeton": "Thompson-Okanagan",
          "Nicola": "Thompson-Okanagan", "Cariboo": "Cariboo", "Quesnel": "Cariboo", "New Westminster": "South Coast", "Vancouver": "South Coast",
          "Victoria": "West Coast", "Nanaimo": "West Coast", "Alberni": "West Coast", "Prince George": "Omineca", "Peace River": "Northeast",
          "Liard": "Northeast", "Hazelton": "Skeena", "Prince Rupert": "Skeena", "Atlin": "Skeena"}
# B.C. Reg. 37/2016, Schedule 2, Table 1 (min annual rental $, $ per 1 000 m3; "flat" = a flat rate), by the licence's purpose code. None = rated
# another way by the regulation (s. 4 (2): irrigation and waterworks of a local provider, pulp mills; Table 2: power by capacity and output).
RATE = {"01A": ("domestic use", 50, 2.25), "01A01": ("domestic use", 50, 2.25), "WSA01": ("domestic groundwater: no rental", 0, 0.0),
        "03B": ("private irrigation", 50, 0.85), "03A": None, "00A": None, "00B": ("water conveyed and used for waterworks purpose by a person other than a local provider", 200, 2.25),
        "00C": ("water sales", 200, 2.25), "02I35": ("water delivery", 200, 2.25),
        "08A": ("storage", 25, 0.02), "08B": ("storage", 25, 0.02), "12A": ("storage", 25, 0.02),
        "02I31": ("livestock and animal", 50, 0.85), "WSA08": ("livestock and animal", 50, 0.85), "02I15": ("livestock and animal", 50, 0.85),
        "WSA03": ("commercial enterprise", 200, 2.25), "02D": ("commercial enterprise", 200, 2.25), "02I40": ("commercial enterprise", 200, 2.25),
        "WSA02": ("camp and public facility", 50, 2.25), "02I37": ("camp and public facility", 50, 2.25), "02I02": ("camp and public facility", 50, 2.25),
        "02I25": ("camp and public facility", 50, 2.25), "02I21": ("camp and public facility", 50, 2.25), "02I03": ("camp and public facility", 50, 2.25),
        "02I09": ("camp and public facility", 50, 2.25),
        "WSA07": ("miscellaneous industrial", 200, "flat"), "02I12": ("miscellaneous industrial", 200, "flat"), "02I27": ("miscellaneous industrial", 200, "flat"),
        "02I06": ("miscellaneous industrial", 200, "flat"), "02I24": ("miscellaneous industrial", 200, "flat"),
        "04A": ("land improvement — general", 50, "flat"), "04B": ("land improvement for rehabilitation or remediation purposes", 50, "flat"),
        "02I08": ("water well drilling, transportation and utility corridor management", 200, 2.25), "WSA10": ("water well drilling, transportation and utility corridor management", 200, 2.25),
        "02I46": ("water well drilling, transportation and utility corridor management", 200, 2.25),
        "11A": ("storage associated with conservation use", 25, "flat"), "11B": ("conservation use", 25, 0.02), "11C": ("construction of works in and about a stream — associated with conservation purpose", 25, "flat"),
        "07A": ("power — residential (Table 2: licensed quantity)", 200, 0.02), "07B": None, "07C": None,
        "02F": ("lawn, fairway and garden", 50, 0.85), "WSA11": ("lawn, fairway and garden", 50, 0.85), "02I42": ("lawn, fairway and garden", 50, 0.85),
        "WSA09": ("processing and manufacturing", 200, 2.25), "02B": ("processing and manufacturing", 200, 2.25), "02I36": ("processing and manufacturing", 200, 2.25),
        "02I11": ("processing and manufacturing", 200, 2.25),
        "05C": ("processing ore", 200, 2.25), "05D": ("placer mining", 200, 1.30), "05B": ("washing coal", 200, 2.25), "05A": ("hydraulic mining", 200, 1.30),
        "WSA12": ("vehicle and equipment", 200, 2.25), "02I01": ("vehicle and equipment", 200, 2.25), "02I39": ("vehicle and equipment", 200, 2.25), "02I33": ("vehicle and equipment", 200, 2.25),
        "02E": ("pond and aquaculture", 50, "flat"), "02I38": ("fish hatcheries", 200, 0.11),
        "02I14": ("crop harvesting and processing", 50, 0.85), "02I13": ("crop harvesting and processing", 50, 0.85), "WSA04": ("crop harvesting and processing", 50, 0.85),
        "02I05": ("crop harvesting and processing", 50, 0.85),
        "WSA05": ("greenhouse and nursery", 50, 0.85), "02I22": ("greenhouse and nursery", 50, 0.85), "02I17": ("greenhouse and nursery", 50, 0.85),
        "02C": ("cooling", 200, 1.30), "05E": ("hydraulic fracturing — other than deep groundwater", 200, 2.25), "05F": ("hydraulic fracturing — deep groundwater", 0, 0.0),
        "05H": ("drilling", 200, 2.25), "02I23": ("oil field injection — other than deep groundwater", 200, 2.25), "02A": None,
        "02G": ("fresh water bottling", 200, 2.25), "09A": ("bottling and commercial distribution", 200, 2.25), "09B": ("commercial bathing pool", 200, 2.25),
        "WSA13": ("waste management", 200, 2.25), "02I28": ("waste management", 200, 2.25), "02I16": ("waste management", 200, 2.25), "02I07": ("waste management", 200, 2.25),
        "02I30": ("ice and snow making", 200, 2.25), "WSA06": ("ice and snow making", 200, 2.25), "02I20": ("ice and snow making", 200, 2.25),
        "02I18": ("heat exchange", 200, 2.25), "02I47": ("residential heat exchange", 50, 2.25), "02I32": ("swimming pool", 50, "flat"),
        "02H": ("bulk shipment for marine transport", 200, 2.25)}
TO_YEAR = {"m3/year": 1.0, "m3/day": 365.0, "m3/sec": 365.0 * 86400}
PROVINCIAL = re.compile(r"\b(?:ministry|minister|province of british columbia|government of british columbia|her majesty|his majesty|the crown|"
                        r"provincial government|bc parks|b\.c\. parks)\b", re.I)
# "First Nations using water on reserve land" and an entity "exempt under a First Nations treaty final agreement" (Nisga'a villages, the Maa-nulth
# nations, Tsawwassen, Tla'amin) pay no rental, and the layer does not say where the water is used: every First Nation, band or treaty nation is left out
FIRST_NATION = re.compile(r"\b(?:first nations?|nations?|indian|bands?|band council|tribal council|nisga.?a|tsawwassen|tla.?amin|maa-nulth|huu-ay-aht|toquaht|"
                          r"uchucklesaht|yuu.?u.?ich|ka.?yu.?k.?t.?h)\b", re.I)
WCOLS = ["key", "client_no", "name", "address", "postal_code", "country", "licences", "licence_examples", "purposes", "rental_calc", "rental_parts",
         "rental_uncalculated", "first_priority", "district", "region", "sources", "pods", "extract_date"]
SCOLS = ["key", "client", "name", "invoices", "value_12m", "months_billed", "first_billed", "last_billed", "last_invoice", "last_value", "last_mark",
         "last_category", "marks", "max_month", "max_month_value", "areas", "report_from", "report_to", "extract_date"]
# ---- one Alberta body of the same kind (2026-11-13): the Alberta Energy Regulator's yearly administration fee (industry levy) on every operator of
# wells. Its words: "Invoices for administration fees are sent to and payable by the party that was the operator on record (as defined in section
# 29 of REDA) as of December 31, 2025."; "Invoices to operators detailing the fee calculations will be emailed on April 1, 2026, with payment due
# by May 1, 2026." (Bulletin 2026-14); "If the operator fails to pay the fee, then the licensee is responsible for paying the invoiced amount and
# any assessed penalty."; "No. Cheques and Electronic Fund Transfer (EFT) are the only methods of payment accepted." (its FAQ, Bulletin 2024-07).
# The wells and their licensees: ST37, List of Wells in Alberta (free, monthly). A licensee with a drilled well whose licence is in force
# (issued, amended, suspended, re-entered) is billed for it — as the operator, or when the operator does not pay.
AER_BODY = "Alberta Energy Regulator (administration fee — industry levy)"
AER_ST37 = "https://www.aer.ca/data-and-performance-reports/statistical-reports/st37"
AER_ZIP = "https://static.aer.ca/prd/documents/sts/st37/ST_37_Excel.zip"
AER_BULLETIN = "https://static.aer.ca/prd/documents/bulletins/Bulletin-2026-14.pdf"
AER_FAQ = "https://static.aer.ca/prd/documents/bulletins/Bulletin-2024-07-FAQ.pdf"
AER_CONTACT = "https://www.aer.ca/about-aer/contact-us"
AER_ADDRESS = "Calgary (Head Office) Suite 1000, 250 – 5th Street SW Calgary, Alberta T2P 0R4"
A_TO = ("Invoices for administration fees are sent to and payable by the party that was the operator on record (as defined in section 29 of REDA) as of "
        "December 31, 2025.")
A_EMAIL = "The invoices are sent by email to ensure secure delivery and create efficiencies in approval and payment processing."
A_WHEN = "Invoices to operators detailing the fee calculations will be emailed on April 1, 2026, with payment due by May 1, 2026."
A_LICENSEE = "If the operator fails to pay the fee, then the licensee is responsible for paying the invoiced amount and any assessed penalty."
A_PAY = "No. Cheques and Electronic Fund Transfer (EFT) are the only methods of payment accepted."
A_PENALTY = "impose a late-payment penalty, which is 20 per cent on any portion of the fee that remains unpaid after the due date."
A_BASE, A_FACTOR = 42.00, 4.359006  # the base fee of an inactive well (fee class 0) and the 2026/27 adjustment factor (Bulletin 2026-14)
A_LIVE = {"Issued", "Amended", "Suspension", "Re-Entered", "Re-entered"}
ACOLS = ["key", "name", "wells", "suspended", "licences", "licence_examples", "first_spud", "last_status_date", "fee_floor", "extract_date"]
AER = os.path.join(DIR, "ab_aer_licensees.csv.gz")
AER_INFO = os.path.join(DIR, "ab_aer_info.json")
# ---- a federal body of the same kind (2026-11-13): Health Canada's Pest Management Regulatory Agency bills every registrant an annual charge for
# each pest control product registered in its name on April 1, in four invoices a year. Its words (guidance on the Fees and Charges Regulations):
# "four (4) invoices will be issued by the PMRA and sent in one mailing to each registrant for products registered in that registrant's name on
# April 1 of each year." "Upon receipt of the invoices, annual charges can be paid in full or in four equal instalments due on May 30, August 28,
# November 26, and February 24." The registrants: the Pesticide Product Information Database's own extract (products, their status, registrant).
# Paid as any Health Canada invoice (its page on paying fees: bill payment through a Canadian financial institution, direct deposit, wire, cheque).
PMRA_GUIDE = ("https://www.canada.ca/en/health-canada/services/consumer-product-safety/reports-publications/pesticides-pest-management/policies-guidelines/"
              "fees-charges-regulations.html")
PMRA_API = "https://pest-control.canada.ca/pesticide-registry-api/api/extract/product/?lang=en"
PMRA_DB = "https://pest-control.canada.ca/pesticide-registry/en/index.html"
HC_PAY = "https://www.canada.ca/en/health-canada/services/funding/cost-recovery-service-fees/how-pay-fees.html"
HC_ADDRESS = "Health Canada Accounts Receivable, Address Locator: 1918B 18th Floor, Room 1804B, Jeanne-Mance Building 161 Goldenrod Driveway, Tunney's Pasture Ottawa, Ontario K1A 0K9"
P_INVOICES = ("Under paragraph 9(2)(b) of the Fees and Charges Regulations four (4) invoices will be issued by the PMRA and sent in one mailing to each registrant "
              "for products registered in that registrant's name on April 1 of each year.")
P_INSTAL = "Upon receipt of the invoices, annual charges can be paid in full or in four equal instalments due on May 30, August 28, November 26, and February 24."
P_CHARGE = ("A registrant must pay each year, in respect of every pest control product that is registered in their name on April 1 of the year, an annual charge "
            "that is the lesser of the Annual Charge amount for that year and 4% of the actual gross revenue during the registrant's preceding fiscal year, but not "
            "less than the minimum charge.")
P_BASE = "The base amount of the Annual Charge, as stated in the Pest Control Products Fees and Charges Regulations, is $3,600 and the minimum charge is $100."
P_INTEREST = "interest calculated and compounded monthly at the average bank rate plus 3% is payable on that amount"
PCOLS = ["key", "name", "products", "product_examples", "first_registered", "extract_date", "fee_floor"]
PMRA = os.path.join(DIR, "hc_pmra_registrants.csv.gz")
# ---- the Canadian Nuclear Safety Commission (2026-11-13): every holder of a nuclear substance / radiation device licence pays a yearly fee, invoiced
# before each licence anniversary — "Every year before the licence anniversary date, the Commission shall issue to the licensee an invoice for the
# annual fee payable." (Cost Recovery Fees Regulations, s. 17(1)); "Clients may remit their fee payment by cheque, credit card or electronically"
# (its "Paying your fees": cheque to the Receiver General, direct deposit or wire to the Receiver General's account). Its licence database lists
# every active licence: number, purpose, organisation, expiry date, city, province. The regulations do not apply to schools, universities and colleges,
# research bodies they own, and publicly funded not-for-profit medical institutions (s. 2): those holders are left out.
CNSC_DB = "https://www.cnsc-ccsn.gc.ca/eng/nuclear-substances/licensing-nuclear-substances-and-radiation-devices/licence-search/"
CNSC_REG = "https://laws-lois.justice.gc.ca/eng/regulations/sor-2003-212/FullText.html"
CNSC_PAY = "https://api.cnsc-ccsn.gc.ca/dms/digital-medias/Cost-Recovery-Program-Paying-your-Fees.pdf/object"
CNSC_ADDRESS = "Canadian Nuclear Safety Commission 280 Slater Street P.O. Box 1046, STN B Ottawa ON K1P 5S9 Canada"
C_INVOICE = "Every year before the licence anniversary date, the Commission shall issue to the licensee an invoice for the annual fee payable."
C_TERMS = "The licensee shall pay the fee to the Commission by the later of 30 days after the date of the invoice and the licence anniversary date."
C_PAY = "Clients may remit their fee payment by cheque, credit card or electronically"
CNSC_EXEMPT = re.compile(r"universit|college|coll[èe]ge|c[ée]gep|school|[ée]cole|hospital|h[ôo]pital|sant[ée]|ciusss|cisss|\bchu\b|centre hospitalier|"
                         r"health (?:authority|services|sciences|region|pei|nl)|health$|alberta health|horizon health|vitalit|nova scotia health|interior health|"
                         r"fraser health|vancouver coastal|island health|northern health|provincial health|shared health|eastern health|central health|"
                         r"western health|labrador-grenfell|regional health|research council|polytechnique|institut national|cancer (?:agency|care|centre)|"
                         r"cancercare|bc cancer|health network|health centre|healthcare|soins de sant", re.I)
NCOLS = ["key", "name", "licences", "licence_examples", "purposes", "places", "first_expiry", "last_expiry", "extract_date"]
CNSC = os.path.join(DIR, "cnsc_licensees.csv.gz")
WATER = os.path.join(DIR, "bc_water_licensees.csv.gz")
STUMP = os.path.join(DIR, "bc_stumpage_clients.csv.gz")
STUMP_INV = os.path.join(DIR, "bc_stumpage_invoices.csv.gz")
SITES = os.path.join(DIR, "bc_sites.csv")
SDONE = os.path.join(DIR, "bc_sites_done.tsv")
OVT_ADDR = os.path.join(INC, "overture", "bcw_addr_candidates.csv")  # places at the licensee's own postal code (tools/overture_names.py addr --lanes bcw)
ADONE = os.path.join(DIR, "bc_addr_done.tsv")


def get(url, path=None, data=None, timeout=300, jar=None):
    req = urllib.request.Request(url, data=data, headers={"User-Agent": UA})
    op = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(jar)) if jar is not None else urllib.request.build_opener()
    with op.open(req, timeout=timeout) as r:
        b = r.read()
        ct = r.headers.get("Content-Type") or ""
    if path:
        with open(path, "wb") as f:
            f.write(b)
    return b, ct


def wfs_url(layer, props, start=0, count=10000, cql=""):
    q = {"service": "WFS", "version": "2.0.0", "request": "GetFeature", "typeName": layer, "outputFormat": "json", "count": str(count),
         "startIndex": str(start), "propertyName": ",".join(props)}
    if cql:
        q["CQL_FILTER"] = cql
    else:
        q["sortBy"] = props[0]
    return WFS + "?" + urllib.parse.urlencode(q)


def record_url(layer, field, value):
    """the Province's own record of one licence / one client (a GetFeature request filtered on it): what the row cites"""
    return WFS + "?" + urllib.parse.urlencode({"service": "WFS", "version": "2.0.0", "request": "GetFeature", "typeName": layer, "outputFormat": "json",
                                               "CQL_FILTER": "%s='%s'" % (field, value)})


def pull_pages(layer, props, work, prefix, sort_key):
    os.makedirs(work, exist_ok=True)
    start, n = 0, 0
    while True:
        p = os.path.join(work, "%s_%06d.json" % (prefix, start))
        b, _ = get(wfs_url(layer, [sort_key] + [x for x in props if x != sort_key], start), p, timeout=300)
        k = len(json.loads(b).get("features") or [])
        n += k
        print("%s: %d features from %d" % (layer, k, start), flush=True)
        if k < 10000:
            break
        start += 10000
        time.sleep(2)
    return n


def cmd_pull_water(a):
    props = ["WLS_WRL_SYSID", "POD_NUMBER", "POD_STATUS", "FILE_NUMBER", "LICENCE_NUMBER", "LICENCE_STATUS", "LICENCE_STATUS_DATE", "PRIORITY_DATE", "EXPIRY_DATE",
             "PURPOSE_USE_CODE", "PURPOSE_USE", "SOURCE_NAME", "QUANTITY", "QUANTITY_UNITS", "QUANTITY_FLAG", "PRIMARY_LICENSEE_NAME", "ADDRESS_LINE_1",
             "ADDRESS_LINE_2", "ADDRESS_LINE_3", "ADDRESS_LINE_4", "COUNTRY", "POSTAL_CODE", "DISTRICT_PRECINCT_NAME"]
    for p in glob.glob(os.path.join(a.work, "wls_*.json")):
        os.remove(p)
    print("water licence points of diversion: %d" % pull_pages(WLS, props, a.work, "wls", "WLS_WRL_SYSID"), flush=True)


def clean_name(n):
    """a name as the layer gives it, without a character the layer lost (a bilingual name keeps its first half then)"""
    n = re.sub(r"\s+", " ", n or "").strip()
    if "\ufffd" in n:
        n = n.split(" /")[0].strip() if " /" in n and "\ufffd" not in n.split(" /")[0] else n.replace("\ufffd", "")
    return n


def strip_no(name):
    m = re.search(r"\s*\((\d{3,9})\)\s*$", name or "")
    return (re.sub(r"\s+", " ", (name or "")[:m.start()] if m else (name or "")).strip(), m.group(1) if m else "")


def holder_ok(name):
    """an organisation that pays the rental (not a person, not a ministry, not a First Nation on reserve land)"""
    if not name or not RL.is_org(name) or RL.FEDERAL.search(name.replace("&", "and")) or PROVINCIAL.search(name):
        return False
    if FIRST_NATION.search(name):
        return False  # "First Nations using water on reserve land" pay no rental, and the layer does not say where the water is used
    return True


def pc_of(s):
    m = re.search(r"\b([A-Z]\d[A-Z])\s?(\d[A-Z]\d)\b", (s or "").upper())
    return (m.group(1) + " " + m.group(2)) if m else ""


def rental(purpose_code, qty, units):
    """(the yearly rental of one licence's purpose by the published rates, its words) — or (None, why)"""
    r = RATE.get(purpose_code, "unknown")
    if r is None:
        return None, "rated another way by the regulation (a local provider's waterworks or irrigation, a pulp mill, or power)"
    if r == "unknown":
        return None, "purpose not in the rate table read here"
    what, mn, rate = r
    if mn == 0 and rate == 0:
        return 0.0, "%s: no rental" % what
    if rate == "flat":
        return float(mn), "%s: $%d flat rate" % (what, mn)
    if units not in TO_YEAR or qty is None:
        return float(mn), "%s: the minimum annual rental, $%d (the licensed quantity is given as %s)" % (what, mn, units or "no unit")
    m3 = qty * TO_YEAR[units]
    v = max(float(mn), rate * m3 / 1000.0)
    return v, "%s: %s m3 a year × $%s per 1 000 m3 = $%s (minimum $%d)" % (what, format(round(m3), ","), ("%.2f" % rate).rstrip("0").rstrip("."), format(rate * m3 / 1000.0, ",.2f"), mn)


def cmd_build_water(a):
    os.makedirs(DIR, exist_ok=True)
    rows = []
    for p in sorted(glob.glob(os.path.join(a.work, "wls_*.json"))):
        rows += [f["properties"] for f in json.load(open(p, encoding="utf-8"))["features"]]
    by, why = collections.defaultdict(list), collections.Counter()
    for r in rows:
        if (r.get("LICENCE_STATUS") or "") != "Current":
            why["licence not current"] += 1
            continue
        name, no = strip_no(clean_name(r.get("PRIMARY_LICENSEE_NAME")))
        if not holder_ok(name):
            why["a person, a ministry, a federal body or a First Nation"] += 1
            continue
        key = "bcw:" + (no or hashlib.sha1(("%s|%s" % (HR.norm(name), pc_of(r.get("POSTAL_CODE")))).encode()).hexdigest()[:12])
        by[key].append((name, no, r))
    out = []
    for key, lst in by.items():
        name, no = lst[0][0], lst[0][1]
        r0 = lst[0][2]
        addr = ", ".join(x.strip() for x in (r0.get("ADDRESS_LINE_1"), r0.get("ADDRESS_LINE_2"), r0.get("ADDRESS_LINE_3"), r0.get("ADDRESS_LINE_4")) if x and x.strip())
        # one quantity per licence and purpose: points of diversion that each repeat the licence's maximum ("M", "P", "T") are counted once;
        # "D" (multiple points, quantity at each known) are added up
        lp = collections.defaultdict(list)
        for _, _, r in lst:
            lp[(r.get("LICENCE_NUMBER"), (r.get("PURPOSE_USE_CODE") or (r.get("PURPOSE_USE") or "").split(" - ")[0]).strip(), (r.get("QUANTITY_UNITS") or "").strip())].append(r)
        total, parts, unc, purposes = 0.0, [], [], collections.Counter()
        for (lic, code, units), rs in lp.items():
            qs = [float(r["QUANTITY"]) for r in rs if r.get("QUANTITY") not in (None, "")]
            q = (sum(qs) if any((r.get("QUANTITY_FLAG") or "") == "D" for r in rs) else max(qs)) if qs else None
            purposes[(rs[0].get("PURPOSE_USE") or code).strip()] += 1
            v, words = rental(code, q, units)
            if v is None:
                unc.append("licence %s, %s: %s" % (lic, (rs[0].get("PURPOSE_USE") or code).strip(), words))
            else:
                total += v
                parts.append("licence %s — %s" % (lic, words))
        if not parts and not unc:
            continue
        if total == 0 and not unc:
            why["only purposes that pay no rental (domestic groundwater)"] += 1
            continue
        lics = sorted({r.get("LICENCE_NUMBER") for _, _, r in lst if r.get("LICENCE_NUMBER")})
        prio = sorted((r.get("PRIORITY_DATE") or "")[:10] for _, _, r in lst if r.get("PRIORITY_DATE"))
        dist = collections.Counter((r.get("DISTRICT_PRECINCT_NAME") or "").split("/")[0].strip() for _, _, r in lst).most_common(1)[0][0]
        out.append({"key": key, "client_no": no, "name": name, "address": addr, "postal_code": pc_of(r0.get("POSTAL_CODE")), "country": r0.get("COUNTRY") or "",
                    "licences": len(lics), "licence_examples": " ".join(lics[:8]), "purposes": json.dumps(dict(purposes.most_common(8)), ensure_ascii=False),
                    "rental_calc": "%.2f" % total if parts else "", "rental_parts": json.dumps(parts[:12], ensure_ascii=False), "rental_uncalculated": json.dumps(unc[:6], ensure_ascii=False),
                    "first_priority": prio[0] if prio else "", "district": dist, "region": REGION.get(dist, ""),
                    "sources": "; ".join(sorted({(r.get("SOURCE_NAME") or "").strip() for _, _, r in lst if r.get("SOURCE_NAME")})[:5]), "pods": len(lst), "extract_date": TODAY})
        why["licensee kept"] += 1
    out.sort(key=lambda o: o["key"])
    with gzip.open(WATER, "wt", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=WCOLS)
        w.writeheader()
        w.writerows(out)
    big = sum(1 for o in out if o["rental_calc"] and float(o["rental_calc"]) >= 5000)
    print("water licensees: %d organisations (%d points of diversion read; calculated rental $5,000 a year or more: %d); %s" % (len(out), len(rows), big, dict(why)), flush=True)


# ---------------------------------------------------------------------------------------------------- stumpage
AREAS = {"10001": "Coast Area", "10002": "North Area", "10003": "South Area"}
INV = re.compile(r"^[A-Z]{1,2}\d{5,7}$")
C8, C2 = re.compile(r"^\d{8}$"), re.compile(r"^\d{2}$")
DT = re.compile(r"^\d{4}-[A-Z][a-z]{2}-\d{2}$")
V2, V3 = re.compile(r"^-?[\d,]+\.\d{2}$"), re.compile(r"^-?[\d,]+\.\d{3}$")
MON = {m: i + 1 for i, m in enumerate("Jan Feb Mar Apr May Jun Jul Aug Sep Oct Nov Dec".split())}


def iso(d):
    y, m, dd = d.split("-")
    return "%s-%02d-%s" % (y, MON[m], dd)


def parse_report(txt, area, scale):
    """the invoice lines of one Billing Summary report (pdftotext -layout)"""
    out, mark, cat = [], "", ""
    for l in open(txt, encoding="utf-8", errors="replace"):
        t = l.split()
        if len(t) < 8 or not (DT.match(t[-1]) and DT.match(t[-2])):
            continue
        i = next((j for j in range(min(6, len(t) - 3)) if INV.match(t[j]) and C8.match(t[j + 1]) and C2.match(t[j + 2])), None)
        if i is None:
            continue
        head = t[:i]
        if head and not re.match(r"^[A-Z][a-z]+$", head[0]):
            mark, head = head[0], head[1:]
        if head:
            cat = " ".join(head)
        j, copied = i + 3, ""
        if j + 2 < len(t) and C8.match(t[j]) and C2.match(t[j + 1]) and C8.match(t[j + 2]):
            copied, j = t[j] + " " + t[j + 1], j + 2
        doc = t[j] if C8.match(t[j]) else ""
        k, val = len(t) - 3, ""
        if V2.match(t[k]):
            val, k = t[k], k - 1
        vol = t[k] if V3.match(t[k]) else ""
        out.append({"mark": mark, "category": cat, "invoice": t[i], "billed_to": t[i + 1] + t[i + 2], "copied_to": copied.replace(" ", ""), "doc": doc,
                    "volume": vol.replace(",", ""), "value": val.replace(",", ""), "scale_date": iso(t[-2]), "bill_date": iso(t[-1]), "area": area, "scale": scale})
    return out


def cmd_pull_stumpage(a):
    import http.cookiejar
    os.makedirs(a.work, exist_ok=True)
    to = datetime.date.today() - datetime.timedelta(days=1)
    fr = to - datetime.timedelta(days=364)
    json.dump({"from": fr.isoformat(), "to": to.isoformat()}, open(os.path.join(a.work, "hbs_range.json"), "w"))
    for area in AREAS:
        for scale in ("P", "W"):
            jar = http.cookiejar.CookieJar()
            form, _ = get(HBS_FORM, jar=jar, timeout=120)
            time.sleep(11)  # robots.txt: Crawl-Delay: 10
            s = form.decode("latin-1")
            act = re.search(r'action="([^"]*BillingSummaryReport[^"]*)"', s)
            hid = re.search(r'name="helperid" value="([^"]*)"', s)
            if not act:
                print("HBS: the form did not come back (%s %s)" % (area, scale), flush=True)
                continue
            data = urllib.parse.urlencode({"radScaleType": scale, "chcBillingDateFromDate": fr.strftime("%Y%m%d"), "chcBillingDateToDate": to.strftime("%Y%m%d"),
                                           "chcScaleDateFromDate": "", "chcScaleDateToDate": "", "radLicenceMark": "district", "chcDistrictHarv": area,
                                           "radScaleSite": "district", "chcDistrictScale": "", "chcReturnCategory": "", "chcClientType": "Both", "txtClientNo": "",
                                           "txtClientLoc": "", "actionType": "View PDF Report", "helperid": hid.group(1) if hid else ""}).encode()
            pdf = os.path.join(a.work, "hbs_%s_%s.pdf" % (area, scale))
            try:
                b, ct = get("https://a100.gov.bc.ca" + act.group(1), pdf, data=data, timeout=900, jar=jar)
            except Exception as e:
                print("HBS %s %s: %s" % (AREAS[area], scale, str(e)[:120]), flush=True)
                time.sleep(11)
                continue
            if b[:5] != b"%PDF-":
                print("HBS %s %s: not a PDF (%s, %d bytes)" % (AREAS[area], scale, ct, len(b)), flush=True)
                os.remove(pdf)
            else:
                subprocess.run(["pdftotext", "-layout", pdf, pdf[:-4] + ".txt"], check=True)
                print("HBS %s %s: %d bytes" % (AREAS[area], scale, len(b)), flush=True)
            time.sleep(11)
    for p in glob.glob(os.path.join(a.work, "fta_*.json")):
        os.remove(p)
    props = ["HARVEST_AUTH_SKEY", "FOREST_FILE_ID", "CUTTING_PERMIT_ID", "TIMBER_MARK_PRIME", "CLIENT_NUMBER", "CLIENT_LOCATION_CODE", "CLIENT_NAME",
             "FILE_TYPE_DESCRIPTION", "HARVEST_AUTH_STATUS_CODE", "LIFE_CYCLE_STATUS_CODE", "ISSUE_DATE", "EXPIRY_DATE", "ADMIN_DISTRICT_NAME"]
    print("harvesting authorities: %d" % pull_pages(FTA, props, a.work, "fta", "HARVEST_AUTH_SKEY"), flush=True)


def cmd_build_stumpage(a):
    os.makedirs(DIR, exist_ok=True)
    rng = json.load(open(os.path.join(a.work, "hbs_range.json")))
    names, files = {}, collections.defaultdict(set)
    for p in sorted(glob.glob(os.path.join(a.work, "fta_*.json"))):
        for f in json.load(open(p, encoding="utf-8"))["features"]:
            r = f["properties"]
            c, loc = (r.get("CLIENT_NUMBER") or ""), (r.get("CLIENT_LOCATION_CODE") or "")
            if len(c) == 8 and r.get("CLIENT_NAME") and (c not in names or loc == "00"):
                names[c] = clean_name(r["CLIENT_NAME"])
            if len(c) == 8 and r.get("FOREST_FILE_ID"):
                files[c].add(r["FOREST_FILE_ID"])
    inv = []
    for p in sorted(glob.glob(os.path.join(a.work, "hbs_*_*.txt"))):
        area, scale = os.path.basename(p)[4:-4].split("_")
        inv += parse_report(p, AREAS.get(area, area), {"P": "piece scale", "W": "weight scale"}.get(scale, scale))
    seen, uniq = set(), []
    for r in inv:  # an invoice is listed once per report; the same invoice number never stands for two bills
        k = (r["invoice"], r["billed_to"], r["mark"], r["value"])
        if k not in seen:
            seen.add(k)
            uniq.append(r)
    by, why = collections.defaultdict(list), collections.Counter()
    for r in uniq:  # one client number is one organisation, whatever its location codes (its offices) on the invoices
        if r["value"] and float(r["value"]) > 0:
            by[r["billed_to"][:8]].append(r)
    cutoff = (datetime.date.today() - datetime.timedelta(days=183)).isoformat()
    out, keep = [], []
    for c, rs in by.items():
        nm = names.get(c, "")
        if not nm:
            why["client number not named in the harvesting authorities layer"] += 1
            continue
        if not org_any(nm):
            why["a person, a ministry or a federal body"] += 1
            continue
        rs.sort(key=lambda r: (r["bill_date"], r["invoice"]))
        last = rs[-1]
        if last["bill_date"] < cutoff:
            why["latest invoice more than 183 days old"] += 1
            continue
        months = collections.defaultdict(float)
        for r in rs:
            months[r["bill_date"][:7]] += float(r["value"])
        mx = max(months.items(), key=lambda kv: kv[1])
        out.append({"key": "bcs:" + c, "client": c + " (location%s %s)" % ("s" if len({r["billed_to"][8:] for r in rs}) > 1 else "", ", ".join(sorted({r["billed_to"][8:] for r in rs}))), "name": nm, "invoices": len(rs), "value_12m": "%.2f" % sum(float(r["value"]) for r in rs),
                    "months_billed": len(months), "first_billed": rs[0]["bill_date"], "last_billed": last["bill_date"], "last_invoice": last["invoice"],
                    "last_value": last["value"], "last_mark": last["mark"], "last_category": last["category"], "marks": " ".join(sorted({r["mark"] for r in rs if r["mark"]})[:10]),
                    "max_month": mx[0], "max_month_value": "%.2f" % mx[1], "areas": ", ".join(sorted({r["area"] for r in rs})), "report_from": rng["from"],
                    "report_to": rng["to"], "extract_date": TODAY})
        keep += rs
        why["client kept"] += 1
    out.sort(key=lambda o: o["key"])
    with gzip.open(STUMP, "wt", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=SCOLS)
        w.writeheader()
        w.writerows(out)
    with gzip.open(STUMP_INV, "wt", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(keep[0].keys()) if keep else ["invoice"])
        w.writeheader()
        w.writerows(keep)
    big = sum(1 for o in out if float(o["max_month_value"]) >= 5000)
    print("stumpage clients: %d organisations billed in the 183 days to %s (%d invoice lines read, %d with a value; a month of $5,000 or more: %d); %s"
          % (len(out), rng["to"], len(inv), sum(len(v) for v in by.values()), big, dict(why)), flush=True)


# ---------------------------------------------------------------------------------------------------- the AER's administration fee
def cmd_pull_aer(a):
    """ST37's free Excel package (about 180 MB), only when the AER has published a newer one than the last build's"""
    import zipfile
    os.makedirs(a.work, exist_ok=True)
    req = urllib.request.Request(AER_ZIP, method="HEAD", headers={"User-Agent": UA})
    with urllib.request.urlopen(req, timeout=120) as r:
        lm = r.headers.get("Last-Modified") or r.headers.get("ETag") or ""
    info = json.load(open(AER_INFO)) if os.path.exists(AER_INFO) else {}
    if lm and info.get("last_modified") == lm and os.path.exists(AER) and not getattr(a, "force", False):
        print("ST37: not newer than the last build (%s)" % lm, flush=True)
        return
    z = os.path.join(a.work, "ST_37_Excel.zip")
    get(AER_ZIP, z, timeout=900)
    with zipfile.ZipFile(z) as zf:
        n = next(i.filename for i in zf.infolist() if i.filename.endswith("ST37_BH.xlsx"))
        with zf.open(n) as src, open(os.path.join(a.work, "ST37_BH.xlsx"), "wb") as dst:
            dst.write(src.read())
    os.remove(z)
    json.dump({"last_modified": lm, "pulled": TODAY}, open(os.path.join(a.work, "ab_aer_info.json"), "w"))
    print("ST37: pulled (%s)" % lm, flush=True)


def cmd_build_aer(a):
    import openpyxl
    src = os.path.join(a.work, "ST37_BH.xlsx")
    if not os.path.exists(src):
        print("ST37: nothing new to build", flush=True)
        return
    os.makedirs(DIR, exist_ok=True)
    ws = openpyxl.load_workbook(src, read_only=True).worksheets[0]
    by, n = collections.defaultdict(lambda: {"wells": 0, "suspended": 0, "lic": [], "spud": [], "sdate": []}), 0
    head = None
    for row in ws.iter_rows(values_only=True):
        if head is None:
            head = {c: i for i, c in enumerate(row)}
            continue
        n += 1
        st = (row[head["Licence_Status"]] or "").strip()
        spud = str(row[head["Spud_Date"]] or "").strip()
        if st not in A_LIVE or not spud:
            continue  # a well not drilled, abandoned, reclaimed or cancelled is not billed
        nm = clean_name(row[head["Licensee"]] or "")
        o = by[nm]
        o["wells"] += 1
        o["suspended"] += st == "Suspension"
        if len(o["lic"]) < 8:
            o["lic"].append(str(row[head["Well_Licence_Number"]] or "").strip())
        m = re.match(r"(\d{2})/(\d{2})/(\d{4})", spud)
        if m:
            o["spud"].append("%s-%s-%s" % (m.group(3), m.group(1), m.group(2)))
        m = re.match(r"(\d{2})/(\d{2})/(\d{4})", str(row[head["Licence_Status_Date"]] or ""))
        if m:
            o["sdate"].append("%s-%s-%s" % (m.group(3), m.group(1), m.group(2)))
    out, why = [], collections.Counter()
    for nm, o in by.items():
        if not nm or not org_any(nm) or re.search(r"orphan well association", nm, re.I):
            why["a person, a public body or the orphan well association"] += 1
            continue
        out.append({"key": "aer:" + hashlib.sha1(HR.norm(nm).encode()).hexdigest()[:12], "name": nm, "wells": o["wells"], "suspended": o["suspended"],
                    "licences": o["wells"], "licence_examples": " ".join(o["lic"]), "first_spud": min(o["spud"]) if o["spud"] else "",
                    "last_status_date": max(o["sdate"]) if o["sdate"] else "", "fee_floor": "%.2f" % (o["wells"] * A_BASE * A_FACTOR), "extract_date": TODAY})
        why["licensee kept"] += 1
    out.sort(key=lambda o: o["key"])
    with gzip.open(AER, "wt", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=ACOLS)
        w.writeheader()
        w.writerows(out)
    if os.path.exists(os.path.join(a.work, "ab_aer_info.json")):
        json.dump(json.load(open(os.path.join(a.work, "ab_aer_info.json"))), open(AER_INFO, "w"))
    big = sum(1 for o in out if float(o["fee_floor"]) >= 5000)
    print("AER: %d licensees with a drilled well in force (%d wells read; a fee floor of $5,000 a year or more: %d); %s" % (len(out), n, big, dict(why)), flush=True)


# ---------------------------------------------------------------------------------------------------- the PMRA's annual charges
def cmd_pull_pmra(a):
    os.makedirs(a.work, exist_ok=True)
    b, _ = get(PMRA_API, os.path.join(a.work, "pmra_products.csv"), timeout=600)
    print("PMRA product extract: %d bytes" % len(b), flush=True)


INTL_FORM = re.compile(r"\b(?:llc|l\.l\.c\.?|gmbh|ag|kg|sas|sa|s\.a\.?|sau|spa|s\.p\.a\.?|srl|s\.r\.l\.?|bv|b\.v\.?|nv|n\.v\.?|ab|as|a/s|a s|oy|plc|ltda\.?|kft|"
                       r"sp\.? ?z ?o\.? ?o\.?|pty|bhd|co|corp|llp|lp|i/s|kk|k\.k\.|sarl|s\.a\.r\.l\.?|eftf|d\.b\.a\.?|dba)\b", re.I)
GOVT = re.compile(r"\b(?:environment and parks|government|department|ministry|minist[eè]re|city of|county of|province of|state of)\b", re.I)


LEGAL_FORM = re.compile(r"\b(?:ltd|ltée|ltee|inc|incorporated|corp|corporation|limited|limitée|company|compagnie|cie|ulc|gp|lp|l\.p|s\.e\.n\.c)\b\.?", re.I)
TRADE2 = re.compile(r"\b(?:products?|international|spas?|nurser(?:y|ies)|chemicals?|devices?|robotics|laborato\w*|pest|control|eco\w*|specialty|health|home|"
                    r"quality|aero|fillers?|benelux|australia|canada|wizard)\b", re.I)


def org_any(nm):
    """a registrant that is an organisation: a legal form (of Canada or another country), a word of the trade, or a name not shaped like a
    person's; a government body (a federal department, a provincial ministry) is not one, unless the name carries a company's legal form"""
    if re.match(r"(?:dr|mr|mrs|ms|me|prof|docteur|dre)\.?\s", nm, re.I):
        return False  # "Dr. David Lautner": a person
    form = bool(LEGAL_FORM.search(nm) or INTL_FORM.search(nm))
    if not form and (RL.FEDERAL.search(nm.replace("&", "and")) or PROVINCIAL.search(nm) or GOVT.search(nm)):
        return False
    return form or bool(RL.is_org(nm) or TRADE2.search(nm)) or not RL.PERSON.match(nm.title())


def cmd_build_pmra(a):
    import io
    os.makedirs(DIR, exist_ok=True)
    raw = open(os.path.join(a.work, "pmra_products.csv"), "rb").read()
    try:
        txt = raw.decode("utf-8")
    except UnicodeDecodeError:
        txt = raw.decode("cp1252", "replace")
    by = collections.defaultdict(list)
    n = 0
    for r in csv.DictReader(io.StringIO(txt)):
        n += 1
        if (r.get("Current / Historical") or "") != "Current" or (r.get("Registration Status") or "") in ("", "Cancelled"):
            continue
        nm = clean_name(re.sub(r"\*+\s*$", "", r.get("Registrant name") or "")).strip()
        if nm:
            by[nm].append(r)
    out, why = [], collections.Counter()
    for nm, rs in by.items():
        if not org_any(nm):
            why["a person or a public body"] += 1
            continue
        rs.sort(key=lambda r: r.get("Registration number") or "")
        first = min((r.get("Date first registered") or "9999") for r in rs)
        out.append({"key": "pmra:" + hashlib.sha1(HR.norm(nm).encode()).hexdigest()[:12], "name": nm, "products": len(rs),
                    "product_examples": " | ".join("%s %s" % (r.get("Registration number"), (r.get("Product name - English") or "").strip()) for r in rs[:5])[:400],
                    "first_registered": "" if first == "9999" else first, "extract_date": TODAY, "fee_floor": "%.2f" % (len(rs) * 100.0)})
        why["registrant kept"] += 1
    out.sort(key=lambda o: o["key"])
    with gzip.open(PMRA, "wt", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=PCOLS)
        w.writeheader()
        w.writerows(out)
    print("PMRA: %d registrants with a current registered product (%d product lines read; 50 products or more: %d); %s"
          % (len(out), n, sum(1 for o in out if int(o["products"]) >= 50), dict(why)), flush=True)


# ---------------------------------------------------------------------------------------------------- the CNSC's yearly licence fees
def cmd_pull_cnsc(a):
    os.makedirs(a.work, exist_ok=True)
    b, _ = get(CNSC_DB, os.path.join(a.work, "cnsc.html"), timeout=300)
    print("CNSC licence database: %d bytes" % len(b), flush=True)


def cmd_build_cnsc(a):
    import html as H
    os.makedirs(DIR, exist_ok=True)
    s_ = open(os.path.join(a.work, "cnsc.html"), encoding="utf-8", errors="replace").read()
    by, why, n = collections.defaultdict(list), collections.Counter(), 0
    for r in re.findall(r"(?s)<tr[^>]*>(.*?)</tr>", s_):
        c = [H.unescape(re.sub(r"<[^>]+>", "", x)).strip() for x in re.findall(r"(?s)<t[dh][^>]*>(.*?)</t[dh]>", r)]
        if len(c) < 7 or c[0].lower().startswith("licence number"):
            continue
        n += 1
        by[clean_name(c[2])].append(c)
    out = []
    for nm, cs in by.items():
        if (not nm or not org_any(nm) or CNSC_EXEMPT.search(nm)
                or (re.search(r"\bhealth\b|sant[ée]|m[ée]dical centre|medical center", nm, re.I) and not LEGAL_FORM.search(nm) and not INTL_FORM.search(nm))):
            why["exempt (school, university, college, publicly funded medical institution), a person or a government body"] += 1
            continue
        cs.sort(key=lambda c: c[3])
        out.append({"key": "cnsc:" + hashlib.sha1(HR.norm(nm).encode()).hexdigest()[:12], "name": nm, "licences": len(cs),
                    "licence_examples": " ".join(c[0] for c in cs[:5]), "purposes": json.dumps(collections.Counter(c[1] for c in cs).most_common(5), ensure_ascii=False),
                    "places": "; ".join(sorted({"%s, %s" % (c[4], c[5]) for c in cs})[:4]), "first_expiry": cs[0][3], "last_expiry": cs[-1][3], "extract_date": TODAY})
        why["licensee kept"] += 1
    out.sort(key=lambda o: o["key"])
    with gzip.open(CNSC, "wt", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=NCOLS)
        w.writeheader()
        w.writerows(out)
    print("CNSC: %d licensees that pay the yearly fee (%d active licences read); %s" % (len(out), n, dict(why)), flush=True)


# ---------------------------------------------------------------------------------------------------- sites and leads
def holders():
    out = []
    for p, lane in ((WATER, "water"), (STUMP, "stumpage"), (AER, "aer"), (PMRA, "pmra"), (CNSC, "cnsc")):
        if os.path.exists(p):
            with gzip.open(p, "rt", encoding="utf-8", newline="") as f:
                for r in csv.DictReader(f):
                    r["lane"] = lane
                    r.setdefault("postal_code", "")
                    out.append(r)
    return out


def sites_on_file():
    out = {}
    if os.path.exists(SITES):
        for r in csv.DictReader(open(SITES, encoding="utf-8", newline="")):
            out[r["key"]] = r
    return out


def wd_pass(cos, have, w, f, threads):
    import tm_register as TM
    import wikidata_sites as WDS
    from concurrent.futures import ThreadPoolExecutor
    todo = [o for o in cos if o["key"] not in have]
    if not todo:
        return 0
    idx = WDS.build_index(os.path.join(os.environ.get("RUNNER_TEMP") or "/tmp", "wikidata_parts"), only={"CA", "US"})  # 18 queries, 12 s apart
    used = {urllib.parse.urlparse(s_["site"]).hostname for s_ in have.values() if s_.get("site")}
    cands = []
    for o in todo:
        k = TM.nkey_x(o["name"])
        ccs = ["CA"] if o["lane"] != "pmra" else ["CA", "US"]
        hits = {}
        for cc in ccs:
            hits.update({h: (it, nm, cc) for h, (it, nm) in (idx.get((cc, k)) or {}).items()})
        if len(hits) == 1:
            h, (it, nm, cc) = next(iter(hits.items()))
            if h not in used and "www." + h not in used:
                cands.append((o, h, it, nm, cc))
    lock, n = threading.Lock(), [0]

    def one(c):
        o, h, it, nm, cc = c
        core_ = HR.core(o["name"])
        try:
            said = HR.home_says(h, core_)
        except Exception:
            said = ""
        if said:
            with lock:
                w.writerow({"key": o["key"], "site": "https://%s/" % h, "read": TODAY, "quote": said,
                            "tied_by": "Wikidata gives %s as the official website of the organisation of that very name (%s, https://www.wikidata.org/wiki/%s; %s), and the site's own home page carries it: “%s”"
                                       % (h, nm, it, cc, said)})
                f.flush(); have[o["key"]] = {"site": "https://%s/" % h}; n[0] += 1
    with ThreadPoolExecutor(max(4, threads)) as ex:
        list(ex.map(one, cands))
    print("wikidata pass: %d holders with one candidate, %d sites tied" % (len(cands), n[0]), flush=True)
    return n[0]


def cmd_sites(a):
    import queue
    os.makedirs(DIR, exist_ok=True)
    cos = holders()
    have = sites_on_file()
    new = not os.path.exists(SITES)
    f = open(SITES, "a", encoding="utf-8", newline="")
    w = csv.DictWriter(f, fieldnames=HR.SITE_COLS)
    if new:
        w.writeheader()
    n_file = 0
    for k, r in HR.tie_on_file([o for o in cos if o["key"] not in have and o.get("postal_code")]).items():
        w.writerow(r); have[k] = r; n_file += 1
    f.flush()
    HR.addr_pass([o for o in cos if o.get("postal_code")], have, w, f, a.addr_minutes, a.threads, ovt_addr=OVT_ADDR, adone=ADONE)
    # 2026-11-13: Wikidata's official website (P856) of an item of the holder's very name in Canada (or, for a pesticide registrant, in the country the
    # site tests know), kept when the site's own home page carries the name — before the autocomplete
    try:
        n_wd = wd_pass(cos, have, w, f, a.threads)
    except Exception as e:
        n_wd = 0
        print("wikidata pass: %s" % str(e)[:160], flush=True)
    done = set()
    if os.path.exists(SDONE):
        done = {l.split("\t")[0] for l in open(SDONE, encoding="utf-8")}
    todo = [o for o in cos if o["key"] not in have and o["key"] not in done]
    t_end = time.time() + 60 * a.minutes
    lock, q, cnt = threading.Lock(), queue.Queue(maxsize=64), collections.Counter()
    dn = open(SDONE, "a", encoding="utf-8")

    def producer():  # the autocomplete, one request a second
        for o in todo:
            if time.time() > t_end:
                break
            n = HR.core(o["name"])
            if len(n) < 3 or (len(n.split()) == 1 and len(n) < 5) or re.fullmatch(r"[\d ]+(?:b ?c|bc)?", n):
                with lock:
                    dn.write("%s\t\n" % o["key"]); dn.flush()
                continue
            cands = [((s_.get("domain") or "").lower().strip(), HR.core(s_.get("name") or "")) for s_ in (HR.suggest(n) or [])[:5]]
            q.put((o, n, [d for d, sn in cands if d and not HR.BAD.search(d) and sn == n and HR.domain_fits(d, n, "canada")]))
            cnt["looked up"] += 1
        for _ in range(a.threads):
            q.put(None)

    def worker():
        while True:
            it = q.get()
            if it is None:
                return
            o, n, doms = it
            hit, said = "", ""
            for d in doms:
                try:
                    said = HR.home_says(d, n)
                except Exception:
                    said = ""
                if said:
                    hit = d
                    break
            with lock:
                dn.write("%s\t%s\n" % (o["key"], hit)); dn.flush()
                if hit:
                    w.writerow({"key": o["key"], "site": "https://%s/" % hit, "read": TODAY, "quote": said,
                                "tied_by": "the company-name autocomplete (Clearbit) proposes %s under the holder's very name (%s, legal forms aside), and the site's own home page carries it: “%s”" % (hit, n, said)})
                    f.flush(); cnt["found"] += 1

    ts = [threading.Thread(target=worker, daemon=True) for _ in range(a.threads)]
    for t in ts:
        t.start()
    producer()
    for t in ts:
        t.join()
    dn.close(); f.close()
    print("sites: %d on file before the autocomplete (+%d from sites on file); the autocomplete: %d names looked up, %d sites tied"
          % (len(have), n_file, cnt["looked up"], cnt["found"]), flush=True)


def money(v):
    return "C$" + format(float(v), ",.2f")


def lead_water(o, s):
    key = "lead:" + hashlib.sha1(("bcwater|%s" % o["key"]).encode()).hexdigest()[:16]
    lics = o["licence_examples"].split()
    office = OFFICES.get(o.get("region") or "", "")
    parts, unc = json.loads(o["rental_parts"] or "[]"), json.loads(o["rental_uncalculated"] or "[]")
    purposes = json.loads(o["purposes"] or "{}")
    rec = record_url(WLS, "LICENCE_NUMBER", lics[0]) if lics else WLS_PAGE
    calc = ""
    if o.get("rental_calc"):
        calc = ("calculated — %s a year: %s — the Province's rates (B.C. Reg. 37/2016, Schedule 2, Table 1: the greater of the minimum annual rental and the "
                "quantity-based rental; %s) applied to the licensed quantities and purposes of this holder's current licences in the Province's water licences layer "
                "(read %s)%s; the statement itself is not published"
                % (money(o["rental_calc"]), "; ".join(parts[:6]) + (" …" if len(parts) > 6 else ""), TARIFF, o["extract_date"],
                   ("; not calculated: %s" % "; ".join(unc[:3])) if unc else ""))
    elif unc:
        calc = "not calculated: %s (B.C. Reg. 37/2016 rates them another way)" % "; ".join(unc[:3])
    s = dict(s, tied_by=HR.no_mail(s.get("tied_by")), quote=HR.no_mail(s.get("quote")))
    what = "%d current water licence%s (%s)" % (int(o["licences"]), "" if o["licences"] == "1" else "s", ", ".join(list(purposes)[:4]))
    row = {"buyer_key": key, "buyer_name": o["name"], "website": s["site"], "canadian_vendor_rows": 1, "example_vendor": WATER_BODY,
           "canada_field_value": "membership / statutory fee relationship: licence holder of the Canadian body (%s)=%s (as printed on %s, read %s); the Province: “%s” “%s” (%s)"
                                 % (WATER_BODY, office or "FrontCounter BC locations", FCBC_LOC, READ, W_ASSESSED, W_TO, FAQ),
           "evidence_dataset": WLS_PAGE, "latest_record_date": o["extract_date"]}
    det = {"key": key, "platform": "bc_water", "record_url": rec, "vendor": WATER_BODY, "record_date": o["extract_date"],
           "start": o.get("first_priority") or "", "end": "", "reference": " ".join(lics[:3]),
           "title": "Water licence(s): %s — %s" % (what, o.get("sources") or ""),
           "vendor_address": "%s (FrontCounter BC's regional office for the licence's region, as printed on %s, read %s; “%s”, %s)" % (office, FCBC_LOC, READ, W_MAIL, FCBC_PAY) if office else "",
           "vendor_site": "https://www2.gov.bc.ca/", "member_address_quote": o["address"] if HR.pc(o["postal_code"]) and HR.pc(o["postal_code"]) in HR.pc(o["address"].replace(" ", "")) or o["postal_code"] in o["address"] else ("%s %s" % (o["address"], o["postal_code"])).strip(),
           "register_label": "the Province's water licences layer (Water Rights Licences – Public: each point of diversion, the licence, its purpose and quantity, the primary licensee's name and address)",
           "buyer_register": {"legal_name": o["name"], "trade_names": [], "registry_id": ("water licensee client no. %s (printed beside the name in the layer)" % o["client_no"]) if o["client_no"] else "",
                              "label": "the Province's water licences layer, read %s" % o["extract_date"]},
           "bc_licences": lics, "bc_purposes": purposes,
           "fee_unit": "at least C$50.00 a year for each licence (the minimum water rental for most purposes; C$200 for industrial ones)",
           "fee_unit_basis": "the Province's FAQ: “%s” (%s, read %s); the minimum annual rentals of B.C. Reg. 37/2016, Schedule 2, Table 1 (%s)" % (W_MIN, FAQ, READ, TARIFF),
           "fee_calculated": calc,
           "bill_delivery": "a statement every year (twice a year above $100,000): “%s” “%s” “%s” “%s” (%s, read %s)" % (W_STATEMENT, W_ONCE, W_TWICE, W_TO, FAQ, READ),
           "bill_terms": "",
           "bill_items": "the yearly rental for the water allocated under %s" % what,
           "fee_basis": "%s (%s)" % (W_ASSESSED, FAQ), "site_named_by": s["tied_by"], "site_tied_to_holder_by": s["tied_by"], "site_quote": s.get("quote") or ""}
    return row, det


def lead_stumpage(o, s):
    key = "lead:" + hashlib.sha1(("bcstump|%s" % o["key"]).encode()).hexdigest()[:16]
    s = dict(s, tied_by=HR.no_mail(s.get("tied_by")), quote=HR.no_mail(s.get("quote")))
    rec = record_url(FTA, "CLIENT_NUMBER", o["client"].split()[0])
    avg = float(o["value_12m"]) / max(1, int(o["months_billed"]))
    row = {"buyer_key": key, "buyer_name": o["name"], "website": s["site"], "canadian_vendor_rows": 1, "example_vendor": STUMP_BODY,
           "canada_field_value": "membership / statutory fee relationship: stumpage invoice of the Canadian body (%s)=%s (as printed on %s, read %s); the Province: “%s” (%s)"
                                 % (STUMP_BODY, S_REMIT, ST_PAY, READ, S_DUE, ST_OVERDUE),
           "evidence_dataset": HBS, "latest_record_date": o["last_billed"]}
    det = {"key": key, "platform": "bc_stumpage", "record_url": HBS, "vendor": STUMP_BODY, "record_date": o["last_billed"],
           "start": o["first_billed"], "end": "", "reference": o["last_invoice"],
           "title": "Stumpage: %s invoices in the 12 months to %s (timber marks %s) — latest invoice no. %s of %s, %s" % (o["invoices"], o["report_to"], o["marks"], o["last_invoice"], o["last_billed"], money(o["last_value"])),
           "vendor_address": "%s (as printed on %s, read %s)" % (S_REMIT, ST_PAY, READ), "vendor_site": ST_MAIN, "member_address_quote": "",
           "register_label": "the Harvest Billing System's public Billing Summary report (by date of invoice, %s to %s; %s) and the harvesting authorities layer (client names)" % (o["report_from"], o["report_to"], o["areas"]),
           "buyer_register": {"legal_name": o["name"], "trade_names": [], "registry_id": "forest client no. %s (the Harvest Billing System's billed-to client)" % o["client"],
                              "label": "the harvesting authorities layer (%s), read %s" % (rec, o["extract_date"])},
           "bc_client": o["client"], "bc_invoices": int(o["invoices"]), "bc_value_12m": o["value_12m"], "bc_last_invoice": o["last_invoice"],
           "fee_unit": "%s — invoice no. %s of %s (timber mark %s; the Billing Summary's value)" % (money(o["last_value"]), o["last_invoice"], o["last_billed"], o["last_mark"]),
           "fee_unit_basis": "the Harvest Billing System's public Billing Summary report (%s, form %s), read %s: the invoice's own line" % (HBS, HBS_FORM, o["extract_date"]),
           "fee_calculated": ("calculated — %s a month on average: the %s invoices of the 12 months to %s add up to %s over %s months with an invoice (the highest month, %s: %s)"
                              % (money(avg), o["invoices"], o["report_to"], money(o["value_12m"]), o["months_billed"], o["max_month"], money(o["max_month_value"]))),
           "bill_delivery": "an invoice for each scale return, a Billing Notice the next day and a Statement of Account every month: “%s” “%s” (%s, read %s)" % (S_NOTICE, S_STATEMENT, ST_MAIN, READ),
           "bill_terms": "“%s” “%s” (%s, read %s)" % (S_DUE, S_INTEREST, ST_OVERDUE, READ),
           "bill_items": "stumpage for the Crown timber scaled under timber mark%s %s" % ("s" if " " in o["marks"] else "", o["marks"]),
           "fee_basis": "%s (%s)" % (S_DUE, ST_OVERDUE), "site_named_by": s["tied_by"], "site_tied_to_holder_by": s["tied_by"], "site_quote": s.get("quote") or ""}
    return row, det


def lead_aer(o, s):
    key = "lead:" + hashlib.sha1(("aerlevy|%s" % o["key"]).encode()).hexdigest()[:16]
    s = dict(s, tied_by=HR.no_mail(s.get("tied_by")), quote=HR.no_mail(s.get("quote")))
    n = int(o["wells"])
    unit = A_BASE * A_FACTOR
    row = {"buyer_key": key, "buyer_name": o["name"], "website": s["site"], "canadian_vendor_rows": 1, "example_vendor": AER_BODY,
           "canada_field_value": "membership / statutory fee relationship: licence holder of the Canadian body (%s)=%s (as printed on %s, read %s); the AER: “%s” “%s” (%s; %s)"
                                 % (AER_BODY, AER_ADDRESS, AER_CONTACT, READ, A_TO, A_LICENSEE, AER_BULLETIN, AER_FAQ),
           "evidence_dataset": AER_ST37, "latest_record_date": o["extract_date"]}
    det = {"key": key, "platform": "ab_aer", "record_url": AER_ST37, "vendor": AER_BODY, "record_date": o["extract_date"],
           "start": o.get("first_spud") or "", "end": "", "reference": "well licence %s" % " ".join(o["licence_examples"].split()[:3]),
           "title": "Licensee of %d drilled well%s in force in Alberta (%d suspended) — ST37, List of Wells in Alberta" % (n, "" if n == 1 else "s", int(o["suspended"])),
           "vendor_address": "%s (as printed on %s, read %s)" % (AER_ADDRESS, AER_CONTACT, READ), "vendor_site": "https://www.aer.ca/", "member_address_quote": "",
           "register_label": "the AER's ST37, List of Wells in Alberta (each well, its licence, its licensee and its status)",
           "buyer_register": {"legal_name": o["name"], "trade_names": [], "registry_id": "", "label": "the AER's ST37, List of Wells in Alberta, read %s" % o["extract_date"]},
           "aer_wells": n, "aer_suspended": int(o["suspended"]),
           "fee_unit": "C$%.2f base fee a year for each inactive well, times the adjustment factor %s (a producing well pays more, by its production class)" % (A_BASE, A_FACTOR),
           "fee_unit_basis": "the AER's Bulletin 2026-14 (2026/27 administration fees): fee class 0 “Inactive wells … $42.00”; “The adjustment factor is set at 4.359006 of the base fee specified for wells in all classes in the AFR.” (%s, read %s)" % (AER_BULLETIN, READ),
           "fee_calculated": ("calculated — at least C$%s a year: %d well%s × C$%.2f (the base fee of an inactive well, $42.00, × the adjustment factor 4.359006); a producing well "
                              "is billed by its production class (up to $3,800.00 × 4.359006), not published by well here" % (format(n * unit, ",.2f"), n, "" if n == 1 else "s", unit)),
           "bill_delivery": "an invoice every year, by e-mail: “%s” “%s” (%s, read %s)" % (A_EMAIL, A_WHEN, AER_BULLETIN, READ),
           "bill_terms": "due by May 1, 2026; the AER may “%s” (%s, read %s)" % (A_PENALTY, AER_BULLETIN, READ),
           "bill_items": "the yearly administration fee (industry levy) on its %d well%s" % (n, "" if n == 1 else "s"),
           "fee_basis": "%s (%s)" % (A_TO, AER_BULLETIN), "site_named_by": s["tied_by"], "site_tied_to_holder_by": s["tied_by"], "site_quote": s.get("quote") or ""}
    return row, det


def lead_pmra(o, s):
    key = "lead:" + hashlib.sha1(("pmra|%s" % o["key"]).encode()).hexdigest()[:16]
    s = dict(s, tied_by=HR.no_mail(s.get("tied_by")), quote=HR.no_mail(s.get("quote")))
    n = int(o["products"])
    what = "%d registered pest control product%s" % (n, "" if n == 1 else "s")
    row = {"buyer_key": key, "buyer_name": o["name"], "website": s["site"], "canadian_vendor_rows": 1, "example_vendor": "Health Canada",
           "canada_field_value": "membership / statutory fee relationship: right-to-sell holder of the Canadian body (Health Canada — Pest Management Regulatory Agency)=%s (as printed on %s, read %s); the PMRA: “%s” (%s)"
                                 % (HC_ADDRESS, HC_PAY, READ, P_INVOICES, PMRA_GUIDE),
           "evidence_dataset": PMRA_DB, "latest_record_date": o["extract_date"]}
    det = {"key": key, "platform": "hc_pmra", "record_url": PMRA_DB, "vendor": "Health Canada", "record_date": o["extract_date"],
           "start": o.get("first_registered") or "", "end": "", "reference": "registration no. %s" % (o["product_examples"].split(" ")[0] if o["product_examples"] else "?"),
           "title": "Registrant of %s — e.g. %s" % (what, o["product_examples"][:200]),
           "vendor_address": "%s (as printed on %s, read %s)" % (HC_ADDRESS, HC_PAY, READ), "vendor_site": "https://www.canada.ca/en/health-canada.html", "member_address_quote": "",
           "register_label": "the Pest Management Regulatory Agency's Pesticide Product Information Database (each product, its status, its registrant)",
           "hc_what": what,
           "buyer_register": {"legal_name": o["name"], "trade_names": [], "registry_id": "", "label": "the Pesticide Product Information Database's extract, read %s" % o["extract_date"]},
           "fee_unit": "C$3,600 a year for each registered product at most (the base amount, adjusted every April by the consumer price index), C$100 at least",
           "fee_unit_basis": "the PMRA's guidance on the Fees and Charges Regulations: “%s” “%s” (%s, read %s)" % (P_CHARGE, P_BASE, PMRA_GUIDE, READ),
           "fee_calculated": ("calculated — at least C$%s a year: %s × the minimum charge of $100 (at most %s × the base amount of $3,600, both adjusted by the CPI every April); "
                              "the charge of each product is the lesser of the year's Annual Charge and 4 %% of its gross revenue, which is not published" % (format(n * 100.0, ",.2f"), what, what)),
           "bill_delivery": "four invoices a year, sent together: “%s” “%s” (%s, read %s)" % (P_INVOICES, P_INSTAL, PMRA_GUIDE, READ),
           "bill_terms": "instalments due May 30, August 28, November 26 and February 24; on a late payment, “%s” (%s, read %s)" % (P_INTEREST, PMRA_GUIDE, READ),
           "bill_items": "the annual charge for the right to sell its %s" % what,
           "fee_basis": "%s (%s)" % (P_CHARGE, PMRA_GUIDE), "site_named_by": s["tied_by"], "site_tied_to_holder_by": s["tied_by"], "site_quote": s.get("quote") or ""}
    return row, det


def lead_cnsc(o, s):
    key = "lead:" + hashlib.sha1(("cnsc|%s" % o["key"]).encode()).hexdigest()[:16]
    s = dict(s, tied_by=HR.no_mail(s.get("tied_by")), quote=HR.no_mail(s.get("quote")))
    n = int(o["licences"])
    purposes = json.loads(o["purposes"] or "[]")
    what = "%d licence%s (%s)" % (n, "" if n == 1 else "s", "; ".join(p_ for p_, _ in purposes[:3]))
    row = {"buyer_key": key, "buyer_name": o["name"], "website": s["site"], "canadian_vendor_rows": 1, "example_vendor": "Canadian Nuclear Safety Commission",
           "canada_field_value": "membership / statutory fee relationship: licence holder of the Canadian body (Canadian Nuclear Safety Commission)=%s (as printed on %s, read %s); the regulations: “%s” (%s)"
                                 % (CNSC_ADDRESS, CNSC_PAY, READ, C_INVOICE, CNSC_REG),
           "evidence_dataset": CNSC_DB, "latest_record_date": o["extract_date"]}
    det = {"key": key, "platform": "cnsc_licence", "record_url": CNSC_DB, "vendor": "Canadian Nuclear Safety Commission", "record_date": o["extract_date"],
           "start": "", "end": o.get("last_expiry") or "", "reference": o["licence_examples"].split(" ")[0] if o["licence_examples"] else "",
           "title": "Nuclear substance / radiation device %s — %s" % (what, o.get("places") or ""),
           "vendor_address": "%s (as printed on %s, read %s)" % (CNSC_ADDRESS, CNSC_PAY, READ), "vendor_site": "https://www.cnsc-ccsn.gc.ca/", "member_address_quote": o.get("places") or "",
           "register_label": "the CNSC's licence database of nuclear substances, radiation devices and Class II facilities (all active licences: number, purpose, organisation, expiry, city, province)",
           "buyer_register": {"legal_name": o["name"], "trade_names": [], "registry_id": "", "label": "the CNSC's licence database, read %s" % o["extract_date"]},
           "fee_unit": "", "fee_unit_basis": "the fee of each licence is calculated by the CNSC's formulas (its 2026-27 Cost Recovery Fees Schedule) from the licensee's locations and devices: not published by licence",
           "fee_calculated": "",
           "bill_delivery": "an invoice every year before the licence anniversary: “%s” (%s, read %s)" % (C_INVOICE, CNSC_REG, READ),
           "bill_terms": "“%s” (%s, read %s)" % (C_TERMS, CNSC_REG, READ),
           "bill_items": "the yearly fee for its %s" % what,
           "fee_basis": "%s (%s)" % (C_INVOICE, CNSC_REG), "site_named_by": s["tied_by"], "site_tied_to_holder_by": s["tied_by"], "site_quote": s.get("quote") or ""}
    return row, det


def cmd_leads(a):
    os.makedirs(SHARDS, exist_ok=True)
    stamp = a.stamp or time.strftime("%Y%m%dT%H%M%S", time.gmtime())
    cos, sites = holders(), sites_on_file()
    have = set()
    for p in glob.glob(os.path.join(SHARDS, "leads_bcgov_*.gz")):
        with gzip.open(p, "rt", encoding="utf-8", newline="") as fh:
            have |= {r["buyer_key"] for r in csv.DictReader(fh)}
    for p in glob.glob(os.path.join(SHARDS, "gone_bcgov_*.gz")):
        with gzip.open(p, "rt", encoding="utf-8") as fh:
            have -= {l.split("\t", 1)[1].strip() for l in fh if l.startswith("D\t")}
    hosts = collections.Counter(urllib.parse.urlparse(s["site"]).hostname for s in sites.values() if s.get("site"))
    rows, dets, by = [], [], collections.Counter()
    for o in cos:
        s = sites.get(o["key"])
        if not s or not s.get("site"):
            continue
        if hosts[urllib.parse.urlparse(s["site"]).hostname] > 3:
            by["site shared by more than three holders (a group's or a host's site): left out"] += 1
            continue
        row, det = {"water": lead_water, "stumpage": lead_stumpage, "aer": lead_aer, "pmra": lead_pmra, "cnsc": lead_cnsc}[o["lane"]](o, s)
        if row["buyer_key"] in have:
            continue
        have.add(row["buyer_key"]); rows.append(row); dets.append(det); by["new lead (%s)" % o["lane"]] += 1
    if rows:
        cols = sorted({k for r in rows for k in r}, key=list(rows[0].keys()).index)
        with gzip.open(os.path.join(SHARDS, "leads_bcgov_%s.gz" % stamp), "wt", encoding="utf-8", newline="") as f:
            w = csv.DictWriter(f, fieldnames=cols); w.writeheader(); w.writerows(rows)
        with gzip.open(os.path.join(SHARDS, "details_bcgov_%s.gz" % stamp), "wt", encoding="utf-8") as f:
            for d in dets:
                f.write(json.dumps(d, ensure_ascii=False) + "\n")
    print("B.C. water licensee / stumpage client / AER licensee leads on file: %d (+%d this run: %s)" % (len(have), len(rows), dict(by)), flush=True)


def main():
    ap = argparse.ArgumentParser()
    sub = ap.add_subparsers(dest="cmd", required=True)
    for c in ("pull-water", "build-water", "pull-stumpage", "build-stumpage", "pull-aer", "build-aer", "pull-pmra", "build-pmra", "pull-cnsc", "build-cnsc"):
        p = sub.add_parser(c); p.add_argument("--work", required=True); p.add_argument("--force", action="store_true")
    p = sub.add_parser("sites"); p.add_argument("--minutes", type=float, default=60); p.add_argument("--threads", type=int, default=12); p.add_argument("--addr-minutes", type=float, default=30)
    p = sub.add_parser("leads"); p.add_argument("--stamp", default="")
    a = ap.parse_args()
    {"pull-water": cmd_pull_water, "build-water": cmd_build_water, "pull-stumpage": cmd_pull_stumpage, "build-stumpage": cmd_build_stumpage,
     "pull-aer": cmd_pull_aer, "build-aer": cmd_build_aer, "pull-pmra": cmd_pull_pmra, "build-pmra": cmd_build_pmra,
     "pull-cnsc": cmd_pull_cnsc, "build-cnsc": cmd_build_cnsc, "sites": cmd_sites, "leads": cmd_leads}[a.cmd](a)


if __name__ == "__main__":
    main()
