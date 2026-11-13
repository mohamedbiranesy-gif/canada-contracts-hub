#!/usr/bin/env python3
"""Buyers seen using the PAID service of a Canada-headquartered tech vendor, on their own website. No AI.

Source key: tech. An organisation's own website often shows that it currently pays a Canadian software company: its
council meetings are on pub-<org>.escribemeetings.com (eSCRIBE), its library catalogue is <lib>.bibliocommons.com
(BiblioCommons), its LMS is <org>.brightspace.com (D2L), its school portal is <board>.edsby.com (Edsby), its
registration store is app.amilia.com/store/... (Amilia), its clinic booking is <clinic>.janeapp.com (Jane), its
training portal is <org>.docebosaas.com (Docebo) or <org>.myabsorb.com (Absorb), its own pages load Shopify, Coveo,
Unbounce or Lightspeed assets. That is buyer-published evidence of an ACTIVE service relationship with a vendor whose
Canada location is the vendor's own published headquarters address (VENDORS below; verified 2026-11-02 on each
vendor's own site; dropped: Bonfire and Questica (Euna Solutions, US headquarters), eSolutions/Govstack, Municipal
Websites (Catalis), PerfectMind (Xplor), Vidyard and Thinkific (free plans), Ada (403), Moneris (no HQ address on its
site), bids&tenders (agencies do not visibly pay)).

Modes
  --reverse            organisations that already have a role mailbox found by tools/ap_crawler.py
                       (~/cch-crawler/data/incoming/claude/claude_buyer_ap_results_{crawl01,search01,deep01}.csv: buyer_key,
                       org_name_as_found, evidence_url, ap_email): fetch the home page of the evidence_url host plus at
                       most 3 internal pages about meetings / library / payments-registration / learning / careers / bids,
                       and match the signatures. robots.txt honoured, <= 1 request/second per site.
                       Output ~/cch-leads/socrata_tech_reverse.jsonl
  --forward <vendor>   enumerate the vendor's customer portals from the public Common Crawl URL index (newest 2 crawls,
                       https://index.commoncrawl.org/collinfo.json -> CC-MAIN-*-index?url=*.<portal-domain>&output=json&fl=url),
                       read each portal's title / og:site_name / logo link to get the organisation and its own website.
                       Output ~/cch-leads/socrata_tech_<vendor>.jsonl   (vendor: escribe bibliocommons d2l edsby amilia jane
                       docebo absorb, or 'all')
Canada filter: the vendor's own HQ address (canada_value = quote from the vendor's site, row.vendor_hq_url).
Record date: the day the signature was observed (row.observed_date = row.record_date = today).
Rules kept: no login, no CAPTCHA/Cloudflare bypass (401/403/429/challenge = blocked, skipped), UA below, caches raw
Common Crawl index pages under ~/cch-sources/tech/cc/.
Counts (2026-11-02 test runs) are in the .stats file written next to each output.
"""
import argparse, csv, glob, html, json, os, re, subprocess, sys, threading, time
import urllib.error, urllib.parse, urllib.request, urllib.robotparser
from concurrent.futures import ThreadPoolExecutor

UA = "canada-contracts-hub-crawler/1.0 (+https://github.com/mohamedbiranesy-gif/canada-contracts-hub)"
LEADS = os.path.expanduser("~/cch-leads")
CACHE = os.path.expanduser("~/cch-sources/tech")
INPUTS = [os.path.expanduser("~/cch-crawler/data/incoming/claude/claude_buyer_ap_results_%s.csv" % s)
          for s in ("crawl01", "search01", "deep01")]
TODAY = time.strftime("%Y-%m-%d")
CANADA_FIELD = "service of a Canada-HQ vendor seen on the buyer's own site (tech)"

VENDORS = {
    "escribe": dict(name="eSCRIBE", legal="eScribe Software Ltd.", kind="portal",
                    hq_url="https://www.escribemeetings.com/terms-of-use/",
                    hq="eScribe Software Ltd. 204-60 Centurian Drive Markham, ON L3R 9R2",
                    host_re=r"^(?:pub-)?([a-z0-9-]+)\.escribemeetings\.com$", cc=["*.escribemeetings.com"],
                    excl={"www", "help", "support", "status", "cdn", "api"}),
    "bibliocommons": dict(name="BiblioCommons", legal="BiblioCommons Corp.", kind="portal",
                          hq_url="https://www.bibliocommons.com/contact-us",
                          hq="BiblioCommons Corp. 5060 Spectrum Way, Suite 100 Mississauga, ON L4W 5N5",
                          host_re=r"^([a-z0-9-]+)\.biblio(?:commons|cms)\.com$", cc=["*.bibliocommons.com", "*.bibliocms.com"],
                          excl={"www", "help", "support", "status", "community", "developer", "developers", "api", "gateway",
                                "cdn", "static", "assets", "secure", "accounts", "my", "partners", "s3", "media", "sandbox",
                                "demo", "staging", "test", "qa", "dev", "local", "images", "img", "files"}),
    "d2l": dict(name="D2L (Brightspace)", legal="D2L Corporation", kind="portal",
                hq_url="https://www.d2l.com/about/",
                hq="You can find us at our headquarters in Kitchener, Ontario and in satellite offices across the globe.",
                host_re=r"^([a-z0-9-]+)\.(?:brightspace|desire2learn)\.com$", path_re=r"^/d2l/(?:login|home|lp/)",
                cc=["*.brightspace.com"],
                excl={"www", "community", "documentation", "status", "support", "help", "s", "cdn", "api", "partners",
                      "developers", "brightspace", "d2l", "lor", "assets", "static", "templates", "content", "ca1", "us1",
                      "eu1", "ap1", "demo", "sandbox", "trial", "test", "dev", "staging", "learn", "login", "auth",
                      "accounts", "creatorplus", "media", "video"}),
    "edsby": dict(name="Edsby", legal="CoreFour Inc.", kind="portal",
                  hq_url="https://www.edsby.com/about-edsby/contact-us/",
                  hq="Richmond Hill 68B Leek Crescent Suite 200 Richmond Hill, Ontario L4B 1H1 Canada",
                  host_re=r"^([a-z0-9-]+)\.edsby\.com$", cc=["*.edsby.com"],
                  excl={"www", "help", "community", "status", "support", "demo", "blog", "cdn", "static", "assets", "api",
                        "app", "test", "dev", "staging", "sandbox", "trial", "info"}),
    "amilia": dict(name="Amilia", legal="Amilia Enterprises Inc.", kind="portal",
                   hq_url="https://www.amilia.com/contact",
                   hq="Address 1751 #3.105 Richardson St Montréal QC H3K 1G6",
                   link_re=r"^(?:app|www)\.amilia\.com/store/(?:en|fr|es)/([a-z0-9-]+)", cc=["app.amilia.com/store/"],
                   excl={"amilia", "shop", "login"}),
    "jane": dict(name="Jane App", legal="Jane Software Inc.", kind="portal",
                 hq_url="https://jane.app/ca/legal/terms-of-use",
                 hq="Jane Software Inc. 500 - 138 13th St E. North Vancouver, BC V7L 0E5 Canada",
                 host_re=r"^([a-z0-9-]+)\.janeapp\.(?:com|co\.uk|com\.au)$", cc=["*.janeapp.com"],
                 excl={"www", "help", "status", "community", "api", "app", "secure", "cdn", "assets", "jane", "blog",
                       "developers", "demo", "test", "staging", "sandbox", "support", "practitioner", "my"},
                 # read 2026-11-10 (https://jane.app/terms, "Updated: July 2026"): one contracting entity for every country
                 scope="\"These Terms are a legal contract between Jane Software Inc.\" — one entity for customers in every country; governed by the laws of British Columbia (https://jane.app/terms, read 2026-11-10)"),
    # vetted 2026-11-10 (https://getjobber.com/terms-of-service/, "Last Updated Date: September 22, 2026"): the customer's contract is with Octopusapp Inc.
    # dba Jobber, Edmonton, in every country (Alberta law outside the United States, New York law inside; the notice address names Octopusapp Inc. in
    # both). Subscription service: "we may offer a free trial" — no free plan. A site that links or embeds its own Client Hub is a subscriber.
    "jobber": dict(name="Jobber", legal="Octopusapp Inc. dba Jobber", kind="portal",
                   hq_url="https://getjobber.com/terms-of-service/",
                   hq="Octopusapp Inc. dba Jobber at Suite 300, 10130 103 Street NW, Edmonton, AB, Canada, T5J 3N9",
                   link_re=r"^clienthub\.getjobber\.com/(?:client_hubs|booking)/([0-9a-f][0-9a-f-]{15,})", cc=["clienthub.getjobber.com/client_hubs/"],
                   portal_fmt="https://clienthub.getjobber.com/client_hubs/%s/login/new", excl=set(),
                   scope="\"GOVERNED BY AND MADE UNDER CANADIAN LAW BETWEEN YOU AND JOBBER\" — Octopusapp Inc. dba Jobber is the contracting entity in every country (https://getjobber.com/terms-of-service/, read 2026-11-10)"),
    # ---- vetted 2026-11-10 from each vendor's own pages (opened that day from the cloud session, robots.txt obeyed): who the customer contracts
    # with, where that company is, and that there is no free plan. `scope` quotes the pages; tools/cc_tenants.py SCOPE lists the countries.
    "checkfront": dict(name="Checkfront", legal="Checkfront Inc.", kind="portal",
                       hq_url="https://www.checkfront.com/company/contact/",
                       hq="Billing accounts@checkfront.com 777 Broughton Street, 3rd floor Victoria, BC, Canada, V8W 1E3",
                       host_re=r"^([a-z0-9-]+)\.checkfront\.com$", cc=["*.checkfront.com"],
                       excl={"www", "support", "help", "status", "blog", "app", "api", "cdn", "static", "assets", "demo", "developers", "docs", "partners", "mobile", "my", "secure",
                             "login", "accounts", "ideas", "community", "sandbox", "test", "staging", "dev", "marketing", "go", "info", "email", "mail", "links", "learn", "media",
                             "images", "img", "files", "get", "try", "start", "checkfront", "booking", "bookings", "reserve"},
                       scope="\"you will be in a legal agreement with Checkfront Inc. and/or its Affiliates\" … \"governed by and construed in accordance with the laws of the Province of "
                             "British Columbia\", lawsuits \"in Victoria, British Columbia, Canada\" (https://www.checkfront.com/terms/master/, read 2026-11-10); billing office in Victoria; "
                             "\"$99 per month + 3% online booking fee\", no free plan (https://www.checkfront.com/pricing/). Kept for customers in Canada and the United States: the affiliates "
                             "(Rezdy, Regiondo) serve other regions under their own names"),
    "touchbistro": dict(name="TouchBistro (reservations / online ordering)", legal="TouchBistro Inc.", kind="portal",
                        hq_url="https://www.touchbistro.com/privacy-notice/",
                        hq="TouchBistro Inc., 1100 – 85 Richmond St W, Toronto, ON M5H 2C9 Canada",
                        link_re=r"^(?:www\.)?tbdine\.com/(?:book/)?restaurant/([a-z0-9][a-z0-9-]{2,})", cc=["www.tbdine.com/restaurant/"],
                        portal_fmt="https://www.tbdine.com/restaurant/%s", excl=set(),
                        scope="\"TouchBistro Inc. and its affiliates (collectively, “TouchBistro”) provide the TouchBistro restaurant point of sale software\" … \"exclusively governed by the "
                              "laws of the Province of Ontario … and the courts sitting at Toronto\" (https://www.touchbistro.com/terms-of-service/, effective March 31, 2026, read 2026-11-10); "
                              "\"our Essentials Bundle starts at $99 per month\" (https://www.touchbistro.com/): a restaurant bookable on TouchBistro's guest site is a subscriber"),
    "wellnessliving": dict(name="WellnessLiving", legal="WellnessLiving Inc.", kind="portal",
                           hq_url="https://www.wellnessliving.com/privacy-policy/",
                           hq="WellnessLiving Inc., 175 Commerce Valley Drive West, Suite 320, Thornhill, Ontario, L3T 7P6, Canada",
                           link_re=r"^(?:www\.)?wellnessliving\.com/(?:rs/)?(?:login|schedule|catalog|event|appointment|book|store|review|explore/locations)/([a-z0-9][a-z0-9_-]{2,})(?:[/?#]|$)",
                           cc=["www.wellnessliving.com/schedule/", "www.wellnessliving.com/login/"],
                           portal_fmt="https://www.wellnessliving.com/schedule/%s", excl={"index", "home", "default"},
                           scope="\"the terms on which WellnessLiving Inc. (“WellnessLiving,” “we,” or “us”) provides the WellnessLiving website\" — one company for every customer "
                                 "(https://www.wellnessliving.com/terms-of-use/, read 2026-11-10); plans Starter $69, Business $199, BusinessPro $349 a month, no free plan "
                                 "(https://www.wellnessliving.com/pricing/)"),
    "wellnessliving_widget": dict(name="WellnessLiving", legal="WellnessLiving Inc.", kind="asset",
                                  hq_url="https://www.wellnessliving.com/privacy-policy/",
                                  hq="WellnessLiving Inc., 175 Commerce Valley Drive West, Suite 320, Thornhill, Ontario, L3T 7P6, Canada",
                                  asset_re=r"wellnessliving\.com/rs/(?:skin-widget|widget|skin)",
                                  scope="\"the terms on which WellnessLiving Inc. (“WellnessLiving,” “we,” or “us”) provides the WellnessLiving website\" — one company for every customer "
                                        "(https://www.wellnessliving.com/terms-of-use/, read 2026-11-10); plans from $69 a month, no free plan (https://www.wellnessliving.com/pricing/)"),
    "clubrunner": dict(name="ClubRunner", legal="Infotech Business Centre Inc. dba ClubRunner", kind="asset",
                       hq_url="https://site.clubrunner.ca/Page/terms-and-conditions",
                       hq="Infotech Business Centre Inc. doing business as ClubRunner, headquartered at 2010 Winston Park Drive, Suite 200, Oakville, Ontario, L6H 5R7",
                       graph=["clubrunner.ca"], asset_re=r"clubrunner\.blob\.core\.windows\.net/\d{8,}/|globalassets\.clubrunner\.ca/",
                       scope="\"ClubRunner Subscription Agreement represents the complete Agreement and understanding between Infotech Business Centre Inc. doing business as ClubRunner … "
                             "and the customer requesting a subscription\" … \"governed by the laws of the Province of Ontario\" (https://site.clubrunner.ca/Page/terms-and-conditions, "
                             "read 2026-11-10); priced in US dollars \"for customers outside of Canada and Canadian Dollars (CAD) for customers in Canada\" "
                             "(https://site.clubrunner.ca/page/pricing): one company for every country; the site's own pages are served from its ClubRunner account"),
    "crowdriff": dict(name="CrowdRiff", legal="CrowdRiff Inc.", kind="asset",
                      hq_url="https://crowdriff.com/contact/",
                      hq="hello@crowdriff.com 240 Richmond St. W. 5th floor, Unit 5-101 Toronto, ON M5V 1V6",
                      graph=["crowdriff.com"], asset_re=r"starling\.crowdriff\.com/js/|embed\.crowdriff\.com/",
                      scope="\"the services made available by CrowdRiff Inc. (“CrowdRiff”, “we”, “us”) to subscribers (“Customer”, “you”) who have entered into one or more "
                            "software-as-a-service order forms\" … \"governed by and construed in accordance with the laws of Ontario, Canada\" whatever \"Customer’s current state or "
                            "country of residence\" (https://crowdriff.com/terms-of-service/, read 2026-11-10): one company for every country, subscribers only"),
    "nicejob": dict(name="NiceJob", legal="Paystone Inc. (NiceJob)", kind="asset",
                    hq_url="https://get.nicejob.com/terms",
                    hq="NiceJob (Paystone Inc.) 509 Commissioners Rd. W., Unit 434 London, ON, N6J 1Y5",
                    graph=["nicejob.com", "nicejob.co"], asset_re=r"cdn\.nicejob\.(?:co|com)/",
                    scope="\"NiceJob is a tradename owned and operated by Paystone Inc.\" … \"the laws of the Province of British Columbia, Canada … will govern these Terms of Service\" "
                          "(https://get.nicejob.com/terms, last updated August 27, 2023, read 2026-11-10): one company for every country; Starter $95, Pro $135 a month, no free plan "
                          "(https://get.nicejob.com/pricing)"),
    # Thinkific (read 2026-11-10). A school on its thinkific.com address may be a school of the old free plan, and a link to it proves nothing:
    # counted ONLY when the organisation's own address is an alias (CNAME) of its school — "As part of any of our paid plans, you can set up
    # a custom domain for your Thinkific site" … "Your CNAME record will need to point to your current Thinkific URL"
    # (https://support.thinkific.com/hc/en-us/articles/360030360074). The contract is with the Vancouver company everywhere except the
    # United States. alias_only: tools/tech_relationships.py portal_hits() ignores it; tools/lead_crawl.py makes the candidates from DNS.
    "thinkific": dict(name="Thinkific", legal="Thinkific Labs Inc.", kind="portal", alias_only=True,
                      hq_url="https://www.thinkific.com/terms-of-service/",
                      hq="Business Name Canada : Thinkific Labs Inc. US : Thinkific.com Inc. Address 400-369 Terminal Ave, Vancouver, BC V6A 4C4",
                      host_re=r"^([a-z0-9-]+)\.thinkific\.com$", cc=[], excl={"www", "support", "help", "status", "app", "api", "cdn", "blog", "community", "developers", "partners"},
                      scope="\"Your contract and Account is with Thinkific Labs Inc. (if you register from within Canada and the rest of the world), or with its subsidiary, "
                            "Thinkific.com Inc. (if you register from within the United States)\" (https://www.thinkific.com/terms-of-service/, read 2026-11-10): customers in "
                            "the United States are left out; a custom domain comes with paid plans only (https://support.thinkific.com/hc/en-us/articles/360030360074)"),
    "docebo": dict(name="Docebo", legal="Docebo Inc.", kind="portal",
                   hq_url="https://www.docebo.com/contact/",
                   hq="Our offices Docebo Inc. 55 York Street – 12th floor, Toronto, ON M5J 1R7, Canada",
                   host_re=r"^([a-z0-9-]+)\.docebosaas\.com$", cc=["*.docebosaas.com"],
                   excl={"www", "help", "status", "demo", "trial", "sandbox", "cdn", "api", "test", "staging", "dev"}),
    "absorb": dict(name="Absorb LMS", legal="Absorb Software Inc.", kind="portal",
                   hq_url="https://www.absorbai.com/support/privacy-policy",
                   hq="Absorb Software Inc., Centennial Place - East Tower, Suite 308, 520 - 3rd Avenue SW Calgary, AB, Canada T2P 0R3",
                   host_re=r"^([a-z0-9-]+)\.myabsorb\.(?:com|ca|eu|com\.au)$",
                   cc=["*.myabsorb.com", "*.myabsorb.ca", "*.myabsorb.eu"],
                   excl={"www", "help", "support", "status", "api", "cdn", "demo", "sandbox", "test", "staging", "dev"}),
    "benevity": dict(name="Benevity", legal="Benevity, Inc.", kind="portal",
                     hq_url="https://benevity.com/contact-us",
                     hq="Calgary Head Office #700, 611 Meredith Road NE Calgary, AB T2E 2W5 CA",
                     host_re=r"^([a-z0-9-]+)\.benevity\.org$", cc=["*.benevity.org"],
                     excl={"www", "help", "support", "status", "api", "cdn", "static", "assets", "demo", "sandbox", "test", "staging",
                           "dev", "causes", "cause", "community", "login", "app", "my", "secure", "accounts", "mail", "email", "go",
                           "info", "blog", "docs", "developer", "developers", "partners", "benevity", "spark", "goodness", "giving",
                           "volunteer", "grants", "admin", "portal", "events", "impact", "affinity", "missions", "fund", "funds"}),
    "coconut": dict(name="Coconut Software", legal="Coconut Software Corporation", kind="portal",
                    hq_url="https://www.coconutsoftware.com/privacy-policy/",
                    hq="Privacy Officer Coconut Software 201-111 Research Drive Saskatoon, SK S7N 3R2",
                    host_re=r"^([a-z0-9-]+)\.coconutcalendar\.com$", cc=["*.coconutcalendar.com"],
                    excl={"www", "help", "support", "status", "api", "cdn", "static", "assets", "demo", "sandbox", "test", "staging",
                          "dev", "app", "my", "secure", "accounts", "login", "admin", "widget", "widgets", "book", "booking"}),
    "mobius": dict(name="Möbius (DigitalEd)", legal="DigitalEd", kind="portal",
                   hq_url="https://www.digitaled.com/contact",
                   hq="Corporate Headquarters 180 Northfield Drive West, Unit 4, Waterloo, Ontario, Canada, N2L 0C7",
                   host_re=r"^([a-z0-9-]+)\.mobius\.cloud$", cc=["*.mobius.cloud"],
                   excl={"www", "help", "support", "status", "api", "cdn", "static", "assets", "demo", "sandbox", "test", "staging",
                         "dev", "app", "my", "secure", "accounts", "login", "admin", "docs", "mobius", "digitaled", "trial", "learn"}),
    "kev": dict(name="SchoolCash Online (KEV Group)", legal="KEV Group Inc.", kind="portal",
                hq_url="https://kevgroup.com/general-inquiries/",
                hq="Toronto, Canada 90 Eglinton Avenue East, Suite 502 Toronto, ON, M4P 2Y3",
                host_re=r"^([a-z0-9-]+)\.schoolcashonline\.com$", cc=["*.schoolcashonline.com"],
                excl={"www", "help", "support", "status", "api", "cdn", "static", "assets", "demo", "sandbox", "test", "staging", "dev",
                      "app", "my", "secure", "accounts", "login", "admin", "docs", "kev", "parent", "parents", "school", "schools", "district"}),
    "shopify": dict(name="Shopify", legal="Shopify Inc.", kind="asset",
                    hq_url="https://www.shopify.com/legal/terms",
                    hq="United States or Canada Shopify Inc., a Canadian corporation 151 O'Connor Street, Ground floor, Ottawa, Ontario, K2P 2L8, Canada",
                    asset_re=r"cdn\.shopify\.com/s/files/|//[a-z0-9-]+\.myshopify\.com|Shopify\.theme\s*=",
                    # 2026-11-11, terms last updated October 20, 2026, read with the project's reader: section 13 names TWO contracting parties for the
                    # region (Shopify Inc., a Canadian corporation; Shopify Technology (USA) Inc., a Nevada corporation) and does not say which
                    # of them provides which service; Shopify Payment Activities Inc. (Canadian) only for regulated payment services.
                    scope=("Shopify's terms, section 13: “You are contracting with the Shopify Contracting Party or Parties below, based on the billing address of your Store.” — for "
                           "“United States or Canada” the parties listed are “Shopify Inc., a Canadian corporation” (Ottawa) and “Shopify Technology (USA) Inc., a Nevada corporation”; "
                           "“Shopify Inc. may act as the billing agent for Shopify Technology (USA) Inc.” The terms do not say which of the two provides which service to a store. "
                           "Stores with a billing address elsewhere contract with Shopify's Irish or Singaporean company and are left out"), scope_countries=("US", "CA")),
    "coveo": dict(name="Coveo", legal="Coveo Solutions Inc.", kind="asset",
                  hq_url="https://ir.coveo.com/en",
                  hq="Coveo Solutions Inc. 1100 Av. Des Canadiens-de-Montréal Suite 401 Montréal, Québec H3B 2S2 Canada",
                  asset_re=r"static\.cloud\.coveo\.com|platform(?:-[a-z]+)?\.cloud\.coveo\.com|coveo-search-ui|CoveoSearch|atomic-search-interface"),
    "unbounce": dict(name="Unbounce", legal="Unbounce Marketing Solutions Inc.", kind="asset",
                     hq_url="https://unbounce.com/contact-us/",
                     hq="drop into our headquarters to say hi in person. Vancouver 603-401 West Georgia St. Vancouver, BC, Canada, V6B 5A1",
                     asset_re=r"assets\.ubembed\.com|//[a-z0-9-]+\.ubembed\.com",
                     scope="\"a legally binding contract between the Customer (“you” or “your”) and Unbounce Marketing Solutions Incorporated\" — one company for every customer "
                           "(https://unbounce.com/terms-of-service/, read 2026-11-10)"),
    "lightspeed": dict(name="Lightspeed", legal="Lightspeed Commerce Inc.", kind="asset",
                       hq_url="https://www.lightspeedhq.com/about/",
                       hq="Proudly headquartered in Montreal, Canada (700 St-Antoine Est, Montreal, Quebec, Canada, H2Y 1A6)",
                       asset_re=r"cdn\.shoplightspeed\.com|cdn\.webshopapp\.com",
                       scope="Lightspeed's own table of contracting entities: \"Lightspeed eCom (C-Series) Europe Lightspeed Netherlands B.V. … Rest of World Lightspeed Commerce Inc. "
                             "Quebec, Canada\" (https://www.lightspeedhq.com/legal/lightspeed-service-agreement/, section III, read 2026-11-10): customers in Europe are left out"),
    # Lightspeed Golf (Chronogolf): a club's own booking page on chronogolf.com. Same table: "Lightspeed Golf Europe Lightspeed Netherlands B.V. … Rest of World
    # Lightspeed Commerce Inc. Quebec, Canada". A golf-course management subscription; the club links its tee-time booking page from its own site.
    "lightspeed_golf": dict(name="Lightspeed Golf (Chronogolf)", legal="Lightspeed Commerce Inc.", kind="portal",
                            hq_url="https://www.lightspeedhq.com/legal/lightspeed-service-agreement/",
                            hq="If you’re located elsewhere in the world: Lightspeed Commerce Inc. 700 Saint-Antoine Street East, Suite 300 Montréal (Quebec) H2Y 1A6, Canada",
                            link_re=r"^(?:www\.)?chronogolf\.(?:com|ca)/(?:[a-z]{2}/)?club/([a-z0-9][a-z0-9-]{2,})", cc=["www.chronogolf.com/club/", "www.chronogolf.ca/club/"],
                            portal_fmt="https://www.chronogolf.com/club/%s", excl=set(),
                            scope="Lightspeed's own table of contracting entities: \"Lightspeed Golf Europe Lightspeed Netherlands B.V. … Rest of World Lightspeed Commerce Inc. "
                                  "Quebec, Canada\" (https://www.lightspeedhq.com/legal/lightspeed-service-agreement/, section III, read 2026-11-10): clubs in Europe are left out"),
    # ---- vetted 2026-11-11 from each vendor's own pages (opened that day from the cloud session, robots.txt obeyed). Found, not guessed: the scan's
    # link detector (tools/credit_scan.py, detector 5) counted the home pages that link their own account at each service (445,303 pages in its
    # first cycle: Rezgo 367, Owl Practice 353, GOrendezvous 472, WebRezPro 200, Juvonno 137). Read and NOT taken: RAMP InterActive, Clio, Spordle
    # (their sites refuse the reader), SkipTheDishes, CARFAX Canada, Moneris, Libro (robots.txt), Noterro, Medeo (terms behind scripts), Keela (its
    # pages print no address), Ocean (sending referrals "is always free"; the price of the patient forms not read yet).
    "owlpractice": dict(name="Owl Practice", legal="Owl Practice Inc.", kind="portal",
                        hq_url="https://owlpractice.ca/privacy-policy/",
                        hq="by mail at: Owl Practice Inc 345-150 King Street West Toronto, ON M5H 1J9 Canada",
                        link_re=r"^((?:aws-portal|portal|oab)\.owlpractice\.ca(?:/(?:portal/|booking/)?[a-z0-9][a-z0-9_-]{2,})?)", cc=[],
                        portal_fmt="https://%s", excl=set(),
                        scope="\"Owl Practice Inc. Subscriber Terms of Use\" … \"If you are located in Canada or any other jurisdiction, you agree that the laws of the Province of Ontario … "
                              "will govern these Terms\" (in the United States the laws of Delaware; the same company) (https://owlpractice.ca/terms-and-conditions/, read 2026-11-11); "
                              "\"a fourteen (14) day free trial\", then a subscription — no free plan. A practice that links its client portal or its online booking page is a subscriber"),
    "juvonno": dict(name="Juvonno", legal="Global Office Software Inc.", kind="portal",
                    hq_url="https://www.juvonno.com/legal/privacy-policy",
                    hq="Global Office Software Inc. Mailing Address: 200-135 Innovation Dr, Winnipeg, Manitoba, R3T 6A8, Canada",
                    host_re=r"^([a-z0-9-]+)(?:\.[a-z]{2}\d)?\.juvonno\.com$", cc=["*.juvonno.com"],
                    excl={"www", "app", "help", "support", "status", "api", "cdn", "blog", "demo", "sandbox", "test", "staging", "dev", "docs", "learn", "go", "info", "get", "login",
                          "secure", "accounts", "mail", "email", "my", "portal", "static", "assets", "training", "university", "partners"},
                    scope="\"these Terms of Service will serve as a legal and written agreement between you, the Subscriber, and Global Office Software\" … \"interpreted and governed by the "
                          "laws of the Province of Manitoba\" (https://www.juvonno.com/legal/terms-of-service, read 2026-11-11); \"flexible subscription plans starting at $55 per month\" "
                          "(https://www.juvonno.com/) — no free plan. A clinic that links its own booking site <clinic>.juvonno.com is a subscriber"),
    "gorendezvous": dict(name="GOrendezvous", legal="GOrendezvous", kind="portal",
                         hq_url="https://www.gorendezvous.com/conditions-utilisation",
                         hq="GOrendezvous est une entreprise enregistrée, avec un siège social situé au 500-1275 Av. des Canadiens-de-Montréal, Montréal, QC CANADA H3B 0G4",
                         link_re=r"^(?:www\.)?gorendezvous\.com/(?:(?:fr|en)/)?((?:homepage/)?(?!(?:homepage|conditions-utilisation|terms|tarifs|pricing|apropos|about|avis-de-confidentialite|privacy|"
                                 r"blog|blogue|aide|help|login|connexion|signup|inscription|recherche|search|partenaires|partners|temoignages|decouvrir|discover|professionnels|fonctionnalites|"
                                 r"features|contact|cms|bookingwidget|demo|fr|en)(?:[/?#]|$))[a-z0-9À-ÿ][a-z0-9À-ÿ_.%-]{2,})",
                         cc=[], portal_fmt="https://www.gorendezvous.com/%s", excl=set(),
                         scope="\"le présent contrat soit régi et interprété conformément aux lois de la Province du Québec, au Canada\" (https://www.gorendezvous.com/conditions-utilisation, "
                               "read 2026-11-11); \"ESSENTIEL 59$ par mois … PREMIUM 69$ par mois\", a free trial and no free plan (https://www.gorendezvous.com/tarifs). A practice that "
                               "links its own booking page gorendezvous.com/<name> is a subscriber"),
    "rezgo": dict(name="Rezgo", legal="Sentias Software Corp. dba Rezgo", kind="portal",
                  hq_url="https://www.rezgo.com/privacy-policy/",
                  hq="owned and provided by Sentias Software Corp. DBA Rezgo, a company incorporated in the province of British Columbia, Canada",
                  host_re=r"^([a-z0-9-]+)\.rezgo\.com$", cc=["*.rezgo.com"],
                  excl={"www", "support", "help", "status", "api", "cdn", "blog", "demo", "sandbox", "test", "staging", "dev", "docs", "app", "secure", "login", "accounts", "my", "go",
                        "info", "get", "mail", "email", "static", "assets", "white", "whitelabel", "partners", "developers", "activityhub", "marketplace"},
                  scope="\"This Agreement between Rezgo (A Division of Sentias Software Corp), a British Columbia Corporation (hereinafter “Rezgo”) and You\" … \"governed by and construed in "
                        "accordance with the laws of the British Columbia\" (https://www.rezgo.com/rezgo-terms-of-service/, read 2026-11-11); \"You pay a consistent transaction rate per "
                        "booking\" (https://www.rezgo.com/pricing/): no monthly fee, a fee to Rezgo on every booking taken on the operator's own Rezgo site"),
    "webrezpro": dict(name="WebRezPro", legal="World Web Technologies Inc.", kind="portal",
                      hq_url="https://webrezpro.com/about-us/",
                      hq="SAAS (software as a service) property management system created by World Web Technologies Inc. … a privately held company headquartered in Calgary, Alberta",
                      link_re=r"^secure\.webrez\.com/+hotel/(\d{2,6})(?:[/?#]|$)", cc=["secure.webrez.com/hotel/"],
                      portal_fmt="https://secure.webrez.com/hotel/%s", excl=set(),
                      scope="\"created by World Web Technologies Inc.\" … \"Incorporated in 1994, World Web Technologies is a privately held company headquartered in Calgary, Alberta\" "
                            "(https://webrezpro.com/about-us/, read 2026-11-11); a property management subscription (\"WebRezPro doesn’t charge any commission or transaction fees for "
                            "reservations generated from its website booking engine\", https://webrezpro.com/price/). The master services agreement is a PDF its robots.txt keeps from "
                            "the reader: kept for properties in Canada and the United States. A property that links its own booking engine secure.webrez.com/hotel/<id> is a subscriber"),
    # vetted 2026-11-11 07:15Z from the scan's own counts of EMBEDDED services (445,303 home pages; vetting sheets of the probe workflow, run 42972522675).
    # Each is seen as a script or image the organisation's own page loads from the vendor's servers.
    "commerce7": dict(name="Commerce7", legal="FS Operations Canada Ltd. (DBA Commerce7)", kind="asset",
                      hq_url="https://www.commerce7.com/contact-us/",
                      hq="Mailing Address: Commerce7 Platform Inc 199 Bay Street, Suite 4000 Toronto, ON M5L 1A9 CA",
                      graph=["commerce7.com"], asset_re=r"cdn\.commerce7\.com",
                      scope="\"“Company” means Fullsteam Software Holdings LLC (DBA Commerce 7, a subsidiary of Fullsteam Operations LLC, if Client is located in the United States), and FS "
                            "Operations Canada Ltd. (DBA Commerce 7, if Client is located outside the Unit[ed States]\" … \"a legal agreement between you (“Client”) and Company … to purchase "
                            "access to the Company Platforms … and the related subscription services\" (https://www.commerce7.com/terms-of-service/, read 2026-11-11): the Canadian company "
                            "contracts with wineries OUTSIDE the United States only; a subscription"),
    "myrealpage": dict(name="myRealPage", legal="MRP Ventures Inc.", kind="asset",
                       hq_url="https://myrealpage.com/terms-and-conditions/",
                       hq="© Copyright 2026 MRP Ventures Inc. All rights reserved. 1899 St Matthews Ave Unit 1, Winnipeg, MB Canada R3H 0J1",
                       graph=["myrealpage.com"], asset_re=r"(?:iss-cdn|res|idx|common-static)\.myrealpage\.com",
                       scope="\"The agreement between myRealPage.com (“MRP”) and the client named in this order form and Contract Agreement (the “Client”) is comprised of these terms and the "
                             "selected products and features for the length of the term\" (https://myrealpage.com/terms-and-conditions/, read 2026-11-11): an order form and a term, one "
                             "company; its clients are real-estate agents and brokerages (\"trusted by over 15,000 REALTORS\")"),
    "socast": dict(name="SoCast", legal="SoCast Inc.", kind="asset",
                   hq_url="https://www.socastdigital.com/terms/",
                   hq="SoCast Inc. (“SoCast”), an Ontario corporation with offices at 292 Sheppard Ave West, 2nd Floor, North York, Ontario M2N 1N5, Canada",
                   graph=["socastsrm.com", "socastdigital.com"], asset_re=r"(?:cdn-js|media-cdn|media)\.socastsrm\.com",
                   scope="\"License Agreement entered into between SoCast Inc. (“SoCast”), an Ontario corporation with offices at 292 Sheppard Ave West … and the Licensee\" … \"In "
                         "consideration for us providing the Services, you must pay all fees, charges and costs set out in the SOW\" … \"governed by and construed in accordance with the "
                         "laws of the Province of Ontario\" (https://www.socastdigital.com/terms/, read 2026-11-11): one company; licence fees. Its licensees are radio stations"),
    "jumptools": dict(name="Jumptools", legal="Jumptools Inc.", kind="asset",
                      hq_url="https://app.jumptools.com/termsAndConditions.faces",
                      hq="Manager, Customer Care, Jumptools Inc., 171 East Liberty Street, Suite 250, Toronto, Ontario, M6K 3P6",
                      graph=["jumptools.com"], asset_re=r"ws\.jumptools\.com",
                      scope="\"This Agreement is governed exclusively by the laws of the province of Ontario\" … \"Jumptools® is a registered trademark of Jumptools Inc.\" "
                            "(https://app.jumptools.com/termsAndConditions.faces, read 2026-11-11): one company; a pricing page and no free plan on it (https://jumptools.com/pricing/). "
                            "A real-estate marketing platform: its clients are agents and brokerages"),
}

# ---- how each vetted vendor bills, in its own words (owner's bar of 2026-11-11: "billed for something monthly … or every 3 months …
# systematically by the vendor"). Every quote is from the vendor's own page, opened with the project's reader on the date given, and read by
# hand afterwards. cls: monthly — the vendor's terms say it bills by the month (every 30 days); monthly_or_yearly — its terms / price list are by
# the month and it also sells a yearly period (or does not say which period is billed); yearly; per_transaction. Vendors that publish no
# price and no billing period (enterprise contracts: D2L, Docebo, Absorb, Benevity, Coveo, eScribe, BiblioCommons, Coconut, KEV, SoCast,
# DigitalEd, WellnessLiving) have no entry: "not published" is the answer. getjobber.com answered 403 to the reader on 2026-11-11: not read.
BILLING = {
    "shopify": dict(cls="monthly", read="2026-11-11", url="https://www.shopify.com/legal/terms",
                    quote="You will be billed for your Subscription Fees every 30 days. Any Transaction Fees or Additional Fees will be charged to your payment method.",
                    more="“Subscription Fees are paid in advance and will be billed in 30 day intervals” … “Fees will appear on an invoice, which will be sent to the Store Owner via the Primary Email Address provided.”"),
    "jane": dict(cls="monthly", read="2026-11-11", url="https://jane.app/ca/legal/terms-of-use",
                 quote="Subscriptions run on a monthly basis. Fees are charged monthly in advance in accordance with the billing information provided by you to us"),
    "rezgo": dict(cls="monthly", read="2026-11-11", url="https://www.rezgo.com/rezgo-terms-of-service/",
                  quote="The service will be billed on a monthly basis. On the first business day of the calendar month you will be sent a payment notice via email."),
    "myrealpage": dict(cls="monthly", read="2026-11-11", url="https://myrealpage.com/terms-and-conditions/",
                       quote="Billing for services provided are billed monthly in advance."),
    "nicejob": dict(cls="monthly", read="2026-11-11", url="https://get.nicejob.com/terms",
                    quote="By requesting NiceJob Services or Sites Services through your User Account, you agree to pay the following fees as invoiced on a monthly basis:"),
    "checkfront": dict(cls="monthly", read="2026-11-11", url="https://www.checkfront.com/pricing/",
                       quote="a monthly subscription fee*, plus a 3% online booking fee charged at the time of booking."),
    "webrezpro": dict(cls="monthly", read="2026-11-11", url="https://webrezpro.com/price/",
                      quote="WebRezPro is a feature-packed property management system that is available for a monthly subscription fee and with no system setup costs",
                      more="“While WebRezPro signs and renews contracts on a yearly basis, properties can cancel with 30-days written notice (without penalty).”"),
    "lightspeed": dict(cls="monthly_or_yearly", read="2026-11-11", url="https://www.lightspeedhq.com/legal/lightspeed-service-agreement/",
                       quote="Fees attributable to recurring subscription services are paid in advance on a monthly basis",
                       more="the same agreement speaks of “Customers with an annual subscription”"),
    "unbounce": dict(cls="monthly_or_yearly", read="2026-11-11", url="https://unbounce.com/terms-of-service/",
                     quote="5.1. Your paid Subscription is valid for either a monthly or an annual Subscription Period.",
                     more="“4.2. Unless otherwise specified in a Subscription, such fees will be billed in advance for each month and are strictly non-refundable.”"),
    "thinkific": dict(cls="monthly_or_yearly", read="2026-11-11", url="https://www.thinkific.com/terms-of-service/",
                      quote="8.2. For our paid plans, Services will be billed in advance on a monthly, annual or such other agreed-upon periodic basis."),
    "gorendezvous": dict(cls="monthly_or_yearly", read="2026-11-11", url="https://www.gorendezvous.com/conditions-utilisation",
                         quote="Pour les professionnels abonnés aux plans payants, GOrendezvous facture un frais mensuel ou annuel en fonction du forfait que vous aurez choisi."),
    "owlpractice": dict(cls="monthly_or_yearly", read="2026-11-11", url="https://owlpractice.ca/terms-and-conditions/",
                        quote="In the case of Monthly Subscriptions and Annual Subscriptions, your Initial Term shall automatically renew for additional thirty (30) day or 365 day terms"),
    "juvonno": dict(cls="monthly_or_yearly", read="2026-11-11", url="https://www.juvonno.com/",
                    quote="We offer flexible subscription plans starting at $55 per month, with scalable options for multi-location practices.",
                    more="its price page: “per month, billed yearly” (https://www.juvonno.com/pricing)"),
    "touchbistro": dict(cls="monthly_or_yearly", read="2026-11-11", url="https://www.touchbistro.com/",
                        quote="TouchBistro’s POS software starts at $69 per month for all our restaurant POS features"),
    "amilia": dict(cls="monthly_or_yearly", read="2026-11-11", url="https://www.amilia.com/pricing",
                   quote="$99 /mo", more="the plan “Best for small and growing recreation businesses and nonprofits.”"),
    "commerce7": dict(cls="monthly_or_yearly", read="2026-11-11", url="https://www.commerce7.com/pricing/", quote="USD $59/month"),
    "clubrunner": dict(cls="yearly", read="2026-11-11", url="https://site.clubrunner.ca/page/pricing",
                       quote="*Subscriptions are payable annually in advance and are subject to the setup fee and the Terms and Conditions in the ClubRunner Subscription Agreement."),
    "crowdriff": dict(cls="yearly", read="2026-11-11", url="https://crowdriff.com/terms-of-service/",
                      quote="Fees for the Services will be invoiced annually in advance unless otherwise provided on the applicable Order Form."),
    "edsby": dict(cls="yearly", read="2026-11-11", url="https://www.edsby.com/faqs/",
                  quote="Certain other features and advanced functionality are also charged for annually and at per student per year rates."),
    "jumptools": dict(cls="yearly", read="2026-11-11", url="https://jumptools.com/", quote="Get online for as little as $35/month (paid annually)."),
    # WellnessLiving's terms for businesses, read with the project's reader on 2026-11-12: a monthly bill, debited from a card or a bank account,
    # or sent as an invoice
    "wellnessliving": dict(cls="monthly", read="2026-11-12", url="https://www.wellnessliving.com/text/terms-of-use-business.html",
                           quote=("WellnessLiving will automatically renew as per Section 8, and bill your credit card/bank account or other form of payment or issue an invoice "
                                  "to you every month for monthly fees."),
                           bill=dict(payment=("“WellnessLiving will automatically renew as per Section 8, and bill your credit card/bank account or other form of payment or issue "
                                              "an invoice to you every month for monthly fees.” (terms of use for businesses)"),
                                     delivery="an invoice every month, or a debit: “… or issue an invoice to you every month for monthly fees.” (terms of use for businesses)")),
}
# what the vendor's bill carries and how much it is, in the vendor's own words (owner 2026-11-11 07:15 EST: "there's some Shopify invoice
# somewhere online, so we can know the fields that the Shopify invoice would have … How much does it cost?"). Pages opened with the project's
# reader on 2026-11-11: https://www.shopify.com/legal/terms (section 5), https://www.shopify.com/charge, https://www.shopify.com/pricing.
# help.shopify.com answered 403 to the reader: not read, not quoted.
BILLING["shopify"].update(
    addr="151 O'Connor Street, Ground floor, Ottawa, Ontario, K2P 2L8, Canada (the registered office Shopify's terms give for Shopify Inc., section 13: https://www.shopify.com/legal/terms, read 2026-11-11)",
    amount="from US$29 a month",
    amount_basis=("Shopify's price page: “Basic $29 /mo”, “Grow $79 /mo”, “Advanced $299 /mo”, “Plus from $2,300 /mo” (https://www.shopify.com/pricing, read 2026-11-11; "
                  "the page offers a “Pay yearly” choice); the store's own plan is not published, so US$29 is the least a store with an online storefront is billed for its subscription"),
    bill=dict(
        items=("“Subscription Fees” (the plan), “Transaction Fees” (“fees relating to the value of sales made through your Store when using all payment providers other than Shopify "
               "Payments”) and “Additional Fees” (“Shopify Payments, POS Equipment, shipping, apps, Themes, domain names, Shopify App Store, or Third Party Services”) — terms, section 5"),
        currency="“Unless otherwise indicated, all Fees and other charges are in U.S. dollars, and all payments will be in U.S. currency.” (terms, section 5)",
        delivery=("“Fees will appear on an invoice, which will be sent to the Store Owner via the Primary Email Address provided. As well, an invoice will appear on the Account page of "
                  "your Store's administrative console.” (terms, section 5); “You can also download PDF versions of the bills” (https://www.shopify.com/charge)"),
        payment=("card or other method on file, charged by Shopify: “Shopify will charge applicable Fees to any valid payment method that you authorize” … “You will be charged on each "
                 "Billing Date for all outstanding Fees that have not previously been charged.” (terms, section 5)"),
        tax=("“All Fees are exclusive of applicable federal, provincial, state, local or other governmental sales, goods and services … harmonized or other taxes” … “To the extent that "
             "Shopify charges these Taxes, they are calculated using the tax rates that apply based on the billing address you provide to us.” (terms, section 5)"),
        identifier=("a nine-digit bill number: “Shopify billing charges show up on bank statements as SHOPIFY* 123456789 and the nine digit bill number is different for each bill.” "
                    "(https://www.shopify.com/charge)"),
        unpaid=("“If we are unable to successfully process payment of Fees using an Authorized Payment Method within 28 days of our initial attempt, we may suspend and revoke access to "
                "your Account and the Services.” … “You may not be able to access your Account or your storefront during any period of suspension.” (terms, section 5)")))
BILLING["jane"]["bill"] = dict(BILLING["jane"].get("bill") or {}, payment=("by card only: “You’ll want to make sure you have a valid credit card on file for your monthly subscription.” … "
    "“No, we’re not able to accept payment by cheque or EFT.” (https://jane.app/guide/managing-your-jane-subscription, read 2026-11-13)"))
BILLING["jane"].update(amount="from US$59 a month", amount_basis="Jane's price page, plan “Balance”: “USD $59 / month”; plan “Practice”: “USD $79 / month”; plan “Thrive”: “USD $99 / month” (https://jane.app/pricing, read 2026-11-11, prices as shown to the reader); the clinic's own plan is not published")
BILLING["checkfront"].update(amount="$99 a month + 3 % of online bookings", amount_basis="“$99 monthly subscription fee to the operator, plus a 3% online booking fee” (https://www.checkfront.com/support/faq/, read 2026-11-11)")
BILLING["touchbistro"].update(amount="from $69 a month", amount_basis="“TouchBistro’s POS software starts at $69 per month” (https://www.touchbistro.com/, read 2026-11-11)")
BILLING["commerce7"].update(amount="from US$59 a month", amount_basis="“USD $59/month” (https://www.commerce7.com/pricing/, read 2026-11-11)")
BILLING["juvonno"].update(amount="from $55 a month", amount_basis="“Plans Start at $55/month” (https://www.juvonno.com/pricing, read 2026-11-11)")
BILLING["myrealpage"].update(amount="$69.99 a month", amount_basis="“Only $69.99 a month” (https://myrealpage.com/real-estate-website-pricing/, read 2026-11-11)")
BILLING["thinkific"].update(amount="from $109 a month", amount_basis="“Our Start plan ($109/month) includes our core feature set” (https://www.thinkific.com/faq/, read 2026-11-11)")
BILLING["amilia"].update(amount="from $99 a month", amount_basis="“$99 /mo” (https://www.amilia.com/pricing, read 2026-11-11)")
BILLING["jumptools"].update(amount="from $35 a month, paid by the year", amount_basis="“Get online for as little as $35/month (paid annually).” (https://jumptools.com/, read 2026-11-11)")
# vendors found through DNS records or credits, not in VENDORS: their terms read by hand, keyed by the vendor's own domain
# 2026-11-13 (owner 13:23 EST: "go through every row populate as much as can be max"): when the bill is due, in the host's own terms. 44,084 ready rows of
# services and licences had every main invoice field but the due terms (build 18:26Z: Web Hosting Canada alone 19,386). Each host's terms page opened with
# the project's reader on 2026-11-13; the sentence is the host's own, at most 300 characters each. rank.py writes it to bill_due_terms_as_published.
DUE_TERMS_BY_DOMAIN = {
    "whc.ca": ("each invoice is due on the service's expiration date, the renewal invoice issued at least 15 days before: “A first payment is required prior to the activation of a "
               "service, and all following invoices must be paid in full prior to their due date.” … “WHC will generate renewal invoices automatically for all your active services "
               "at least 15 days prior to their expiration date.” (https://whc.ca/legal/terms-of-service, read 2026-11-13)"),
    "doteasy.com": ("by the due date the invoice gives, the invoice sent ahead of it: “Invoices will be sent in advance of payment due.” … “If you do not make any payment to us by the due "
                    "date we may charge interest to you on the overdue amount” (https://terms.doteasy.com/, read 2026-11-13)"),
    "aplus.net": ("in advance, before the registration or renewal date: “All fees are due prior to the registration or renewal date.” … “Your activation fee and monthly service fees are "
                  "payable in advance” … “If you fail to pay the fees within 30 days after due your services will be disabled.” (https://www.aplus.net/sites/aplus/files/Terms_and_Conditions.pdf, read 2026-11-13)"),
    "canadianwebhosting.com": ("in advance, by the time the invoice states: “Pre-payment of recurring fees is due by the time stated on CWH's invoice.” … “All CLIENT fees are due in advance of the "
                               "first day of the relevant term.” (https://canadianwebhosting.com/company/terms-of-service, read 2026-11-13)"),
    # 2026-11-13 21Z: the ten business days of its terms are for a cheque at sign-up only (the one-time design fee), not for the monthly fees
    "linknowmedia.com": ("on the billing date: “All amounts billed on your account on a given date are due and payable on that date.” (https://linknow.com/terms/, read 2026-11-13)"),
    "linknow.com": ("on the billing date: “All amounts billed on your account on a given date are due and payable on that date.” (https://linknow.com/terms/, read 2026-11-13)"),
    "astralinternet.com": ("by the service's due date, printed on the invoice, the renewal invoice issued 30 days before: “Cette date d’expiration est la « date d’échéance du Service » et constitue "
                           "la date limite de paiement de son renouvellement ; elle est indiquée sur la facture.” … “Astral Internet émet la facture de renouvellement trente (30) jours avant la "
                           "date d’échéance du Service” (https://www.astralinternet.com/conditions/, read 2026-11-13)"),
    "webware.ai": ("by the due date the invoice sets out: “In the event a payment is not received by the due date set forth on an invoice, a late fee of one and a half percent” "
                   "(https://www.webware.ai/?fuseaction=store.privacy, read 2026-11-13)"),
    "websites.ca": "in advance: “All fees are billed in advance and are non-refundable.” (https://websites.ca/terms/, read 2026-11-13)",
    "coolcom.com": ("on or before the due date, after notices 30 and 15 days ahead: “30 and 15 days notice for payment due (allowing time for checks to be mailed in) are sent out and payment "
                    "is due on or before due date.” (https://coolcom.com/index.php/policies, read 2026-11-13)"),
    "varialhosting.com": ("by the date the account is due for renewal, the invoice issued 15 days before: “Hosting renewal invoices are automatically generated 15 days before the account is due for.” "
                          "(https://my.varialhosting.com/knowledgebase/33/Billing, read 2026-11-12)"),
}
BILLING_BY_DOMAIN = {
    "1password.com": dict(cls="monthly_or_yearly", read="2026-11-11", url="https://1password.com/legal/terms-of-service",
                          quote="You will be billed in advance on a recurring and periodic basis (“Billing Cycle”). Billing cycles are set on a regular basis, typically monthly or yearly.",
                          bill=dict(payment="“A valid payment method, including credit card, is required to process the payment for your Subscription.” (terms of service)")),
    # Web Hosting Canada: 11,551 rows on 2026-11-11 (the organisation's zone on ns1 / ns2.whc.ca), the largest vendor seen in DNS. Its terms and its hosting page
    # were opened with the project's reader on 2026-11-11; the daily reader had kept an e-mail plan's price for every row.
    "whc.ca": dict(cls="monthly_or_yearly", read="2026-11-11", url="https://whc.ca/legal/terms-of-service",
                   quote="WHC will generate renewal invoices automatically for all your active services at least 15 days prior to their expiration date.",
                   more=("its price list is by the month — “As low as C$2.79 /mo” — and a plan can be “prepaid for a minimum of 1 year” (https://whc.ca/canadian-web-hosting): "
                         "which term this organisation chose is not published"),
                   amount="from C$2.79 a month",
                   amount_basis=("Web Hosting Canada's hosting page: “Affordable plan, great for personal projects. As low as C$2.79 /mo C$9.99 Save 72%” (https://whc.ca/canadian-web-hosting, "
                                 "read 2026-11-11): C$2.79 is the reduced price of its smallest plan and C$9.99 the price printed beside it; the organisation's own plan is not published"),
                   bill=dict(
                       items="the services active on the account, each renewed at the end of its term: “renewal invoices … for all your active services” (terms of service)",
                       currency="“All payments must be made in Canadian dollars, unless stated otherwise.” (terms of service)",
                       delivery=("“When we generate a new invoice, we'll send you an email with a copy of the invoice and will also make the invoice available in your Client Area” "
                                 "(terms of service)"),
                       # 2026-11-12: its payment page (https://whc.ca/pay) offers the invoice paid by wire transfer, Interac e-mail transfer or a deposit at the bank:
                       # an invoice that can be paid by bank transfer is in, also when the biller would take a card (owner 2026-11-11 14:20 EST)
                       payment=("on its payment page: “Complete our online order form to generate an invoice and select Wire Transfer / Interac / Deposit as the payment method.” "
                                "“North American Wire transfers or direct deposits at a CIBC branch (in North America) Please note: we do not accept wire transfers or direct deposits "
                                "for amounts less than 30$.” (https://whc.ca/pay, read 2026-11-12) — and in its terms: “WHC accepts payments by Visa, Mastercard and Paypal (which "
                                "includes American Express).” … “Unless otherwise requested, WHC will attempt to charge the payment method on file 5 days prior to your invoice's due "
                                "date.” (terms of service)"),
                       unpaid=("“Services not paid on their due date risk being suspended, and may be terminated permanently shortly after, at WHC’s sole discretion.” "
                               "(https://whc.ca/legal/terms-of-service, read 2026-11-11)"))),
    # Varial Hosting: its billing questions, read with the project's reader on 2026-11-12 (knowledge base of its client area)
    "varialhosting.com": dict(cls="monthly_or_yearly", read="2026-11-12", url="https://my.varialhosting.com/knowledgebase/33/Billing",
                              quote="How do I renew my hosting plan? Hosting renewal invoices are automatically generated 15 days before the account is due for.",
                              more="its price list is by the month and by terms of one to three years (https://varialhosting.com/): which term this organisation chose is not published",
                              bill=dict(
                                  delivery="an invoice before each renewal: “Hosting renewal invoices are automatically generated 15 days before the account is due for.” (knowledge base: Billing)",
                                  payment=("“We accept payment by credit card, PayPal, Interac e-Transfer, electronic funds transfer (EFT) and...” (https://my.varialhosting.com/knowledgebase/33/Billing) — "
                                           "“If you wish to send payment for an invoice by cheque or money order, please make the payment payable to Varial Technologies, Inc” "
                                           "(https://my.varialhosting.com/knowledgebase/41/How-do-I-mail-in-a-payment.html, read 2026-11-12)"))),
    # 2026-11-13: the hosts behind the most rows held as "payment: not published" (build 04:08Z: 34,575 rows with a mailbox) — each host's own terms read with the
    # project's reader; a sentence is kept only where the host itself names an invoice and a bank payment (bank transfer, cheque, direct debit, Interac, ACH).
    # Card only (no row): Jane (“No, we’re not able to accept payment by cheque or EFT.”), Hawk Host (its billing articles name cards, PayPal, crypto and wallets only),
    # Ex2 (automatic charge to the card or PayPal account on file), Internic.ca (“Billing for the Subscription Service will be by valid credit card”).
    "doteasy.com": dict(cls="yearly", read="2026-11-13", url="https://doteasy.com/web-hosting",
                        quote="Kickstart your online journey with a FREE domain name for the first year with all annual shared hosting plans.",
                        more="its shared hosting is sold by the year (“any annual plan”); a longer term can be chosen (“depending on the term length you choose”): which term this organisation chose is not published",
                        bill=dict(
                            delivery=("“Invoices will be sent in advance of payment due. Invoices will be sent to the email address provided by you to us when registering your account.” "
                                      "(https://terms.doteasy.com/, read 2026-11-13)"),
                            payment="“We accept payment by most major credit and debit cards, direct debit, PayPal, bank transfer and cheque.” (https://terms.doteasy.com/, read 2026-11-13)",
                            unpaid=("“If you do not pay us for the services when you are supposed to (see Clause 11.1), we may suspend the supply of the services until you have paid us the "
                                    "outstanding amounts.” (https://terms.doteasy.com/, read 2026-11-13)"))),
    "aplus.net": dict(cls="monthly_or_yearly", read="2026-11-13", url="https://www.aplus.net/",
                      quote="Sign up for a monthly hosting plan, and the first month is on us!",
                      more="it sells monthly plans and annual ones (“Save 10% on any annual hosting plan”, same page): which term this organisation chose is not published",
                      bill=dict(
                          delivery=("a charge each billing cycle, extra fees “to be invoiced to you in the following billing cycle” (terms and conditions, "
                                    "https://www.aplus.net/sites/aplus/files/Terms_and_Conditions.pdf, read 2026-11-13)"),
                          payment=("“Unless otherwise stated, you may pay for Products and Services by providing a valid credit card or ACH if available.” "
                                   "(https://www.aplus.net/sites/aplus/files/Terms_and_Conditions.pdf, read 2026-11-13)"))),
    "canadianwebhosting.com": dict(cls="monthly_or_yearly", read="2026-11-13", url="https://canadianwebhosting.com/hosting/shared-hosting",
                                   quote="Canadian shared web hosting · From $5.95 CAD/mo",
                                   more="its terms speak of monthly plans and annual ones (“the discounted price that the customer may have paid for an annual plan”): which term this organisation chose is not published",
                                   bill=dict(
                                       delivery=("“CLIENT shall pay CWH recurring fees (hereinafter \"Recurring Fees\"), plus bandwidth charges as outlined on invoice. Pre-payment of recurring fees is "
                                                 "due by the time stated on CWH's invoice.” (https://canadianwebhosting.com/company/terms-of-service, read 2026-11-13)"),
                                       payment=("the methods of payment its terms name where they say which are non-refundable: “The following methods of payments are non-refundable, and "
                                                "refunds will be posted as credit to the hosting account: bank wire transfers, Interac Email Transfers, cheques, and money orders.” "
                                                "(https://canadianwebhosting.com/company/terms-of-service, read 2026-11-13)"),
                                       unpaid="“Amounts past due may result in the termination of CLIENT's account.” (terms of service)",
                                       currency="“All prices are in Canadian dollars.” (https://canadianwebhosting.com/hosting/shared-hosting)")),
    "hostedincanada.com": dict(cls="yearly", read="2026-11-13", url="https://hostedincanada.com/",
                               quote="Free Domain transfer on one year 1-year packages",
                               more="its hosting is sold in packages of a year or more: which term this organisation chose is not published",
                               bill=dict(
                                   delivery=("“8.1 The Host shall issue invoices for the Charges to the Customer from time to time during the Term OR on or after the invoicing dates set out "
                                             "in Section 4 of the Services Order Form OR dates for invoicing .” (https://hostedincanada.com/terms/, read 2026-11-13)"),
                                   terms=("“8.2 The Customer must pay the Charges to the Host within the period of 30 days following the issue of an invoice in accordance with this Clause 8 "
                                          "OR the receipt of an invoice issued in accordance with this Clause 8.” (terms)"),
                                   payment=("“8.3 The Customer must pay the Charges by debit card, credit card, direct debit, bank transfer or cheque (using such payment details as are "
                                            "notified by the Host to the Customer from time to time).” (https://hostedincanada.com/terms/, read 2026-11-13)"))),
    "websites.ca": dict(cls="monthly_or_yearly", read="2026-11-13", url="https://websites.ca/terms/",
                        quote="All fees are billed in advance and are non-refundable. You can prepay for 12 months of service at a discount of 15%.",
                        bill=dict(
                            delivery="an invoice with a link to pay it: “or you can click the link in your invoice to pay online.” (https://customers.websites.ca/, read 2026-11-13)",
                            payment=("by cheque, by card or online through the invoice: “Pay an invoice, update billing information, or send a cheque You can call us with a credit card "
                                     "number or new expiry date 1-877-517-7867 (9am – 5pm central time Monday to Friday) or you can click the link in your invoice to pay online.” "
                                     "(https://customers.websites.ca/, read 2026-11-13)"),
                            remit_to="“Our mailing address is: Websites.ca Web Design 300-245 McDermot Ave Winnipeg, MB R3B 0S6” (https://customers.websites.ca/)")),
    "coolcom.com": dict(cls="yearly", read="2026-11-13", url="https://coolcom.com/index.php/policies",
                        quote="All domain renewal notices, hosting renewal notices, order confirmations, invoice copies and failed billing notices will go to your Client Centre contact email.",
                        more="hosting and domains are renewed term by term (its renewal notices): the length of this organisation's term is not published",
                        bill=dict(
                            delivery="renewal notices and invoice copies by e-mail: “All domain renewal notices, hosting renewal notices, order confirmations, invoice copies and failed billing notices will go to your Client Centre contact email.” (policies)",
                            payment=("by card, or by Interac, cheque or online banking: “If you order a Service and choose to pay for your order using a method other than credit card "
                                     "(e.g. Interac, cheque or online banking) then you acknowledge and agree that: (a) we are not obligated to fully process your order or provide the "
                                     "Service unless and until we have received full payment for the Service;” (https://coolcom.com/index.php/policies, read 2026-11-13)"))),
    "vianet.ca": dict(cls="monthly", read="2026-11-13", url="https://www.vianet.ca/legal/billing-policy/",
                      quote=("Statements are sent by mail or email within the 1st week of each month and cover: Service from the first to the last day of the current month and all "
                             "related charges."),
                      bill=dict(
                          delivery="a monthly statement: “Statements are sent by mail or email within the 1st week of each month” … “Statements are dated the 1st of the month. The due date for the balance owing is the 10th of the month.” (billing policy)",
                          payment=("“Payment Options Subject to some restrictions, payment options include: Automatic bank withdrawal Automatic credit card debit (Visa, Visa Debit, "
                                   "Mastercard, Mastercard Debit and American Express)” (https://www.vianet.ca/legal/billing-policy/, read 2026-11-13)"),
                          terms="“Statements are dated the 1st of the month. The due date for the balance owing is the 10th of the month.” (billing policy)")),
    # PowerStores (webware.ai): its policy page, read with the project's reader on 2026-11-13
    "webware.ai": dict(cls="monthly", read="2026-11-13", url="https://www.webware.ai/?fuseaction=store.privacy",
                       quote="If you cancel the Services in the middle of the month, you will receive a closing invoice via email.",
                       bill=dict(
                           delivery=("“When you subscribe for the Services, Company shall send an invoice via email. An invoice will also appear on the account page of your "
                                     "administration console (account page).” (https://www.webware.ai/?fuseaction=store.privacy, read 2026-11-13)"),
                           payment="“Our Payment Service requires Users to pay with a credit card, wire transfer, debit card or cheque.” (https://www.webware.ai/?fuseaction=store.privacy, read 2026-11-13)",
                           unpaid=("“In the event a payment is not received by the due date set forth on an invoice, a late fee of one and a half percent (1.5%) shall be assessed "
                                   "against overdue amounts.” (same page)"))),
    # card only: the row says so instead of "not published"
    "hawkhost.com": dict(cls="monthly_or_yearly", read="2026-11-13", url="https://www.hawkhost.com/kb/billing/",
                         quote="How do I pay my invoice with a credit card?",
                         bill=dict(payment=("its billing articles name cards, PayPal, cryptocurrency and regional wallets only (“How do I pay my invoice with a credit card?”, “How do I pay my "
                                            "invoice with PayPal”, “How do I pay my invoice with cryptocurrency?” — https://www.hawkhost.com/kb/billing/, read 2026-11-13): "
                                            "a card or a wallet, no bank payment"))),
    "ex2.com": dict(cls="monthly_or_yearly", read="2026-11-13", url="https://www.ex2.com/ca/terms-and-conditions",
                    quote="10.4 - Les factures sont payables d’avance pour la période à venir.",
                    bill=dict(payment=("“10.5 - Paiement automatique. Lorsque Ex2 est autorisée à procéder ainsi conformément au présent contrat, les frais et taxes applicables seront "
                                       "automatiquement imputés à la carte de crédit ou au compte PayPal enregistré dans votre compte Ex2.” (https://www.ex2.com/ca/terms-and-conditions, "
                                       "read 2026-11-13): charged to the card or PayPal account on file"))),
    "linknow.com": dict(cls="monthly", read="2026-11-13", url="https://linknow.com/terms/",
                    quote=("further monthly recurring fees will be billed on the calendar day of the initial purchase date each subsequent month until cancelled. All amounts "
                           "billed on your account on a given date are due and payable on that date."),
                    bill=dict(
                        # its terms read whole on 2026-11-13 (21Z): the cheque and money-order sentence the reader had kept is for the one-time design fee at sign-up
                        # (with a year of monthly fees prepaid); the monthly fees are charged to the card, which it retries when refused — no bank payment, no row
                        payment=("by credit card: “Payment(s) for your Package or any Services can normally be made via credit card.” … “You irrevocably authorize us to "
                                 "attempt to process your credit card payment again if initially rejected” (https://linknow.com/terms/, read 2026-11-13); its other forms "
                                 "of payment are accepted only at sign-up, for the one-time design fee"),
                        terms="on the billing date: “All amounts billed on your account on a given date are due and payable on that date.” (https://linknow.com/terms/, read 2026-11-13)",
                        unpaid=("“If your account is suspended, you will need to contact Customer Support to reactivate it and pay any outstanding balance in full.” "
                                "(https://linknow.com/terms/, read 2026-11-13)"))),
    "linknowmedia.com": dict(cls="monthly", read="2026-11-13", url="https://linknow.com/terms/",
                    quote=("further monthly recurring fees will be billed on the calendar day of the initial purchase date each subsequent month until cancelled. All amounts "
                           "billed on your account on a given date are due and payable on that date."),
                    bill=dict(
                        # its terms read whole on 2026-11-13 (21Z): the cheque and money-order sentence the reader had kept is for the one-time design fee at sign-up
                        # (with a year of monthly fees prepaid); the monthly fees are charged to the card, which it retries when refused — no bank payment, no row
                        payment=("by credit card: “Payment(s) for your Package or any Services can normally be made via credit card.” … “You irrevocably authorize us to "
                                 "attempt to process your credit card payment again if initially rejected” (https://linknow.com/terms/, read 2026-11-13); its other forms "
                                 "of payment are accepted only at sign-up, for the one-time design fee"),
                        terms="on the billing date: “All amounts billed on your account on a given date are due and payable on that date.” (https://linknow.com/terms/, read 2026-11-13)",
                        unpaid=("“If your account is suspended, you will need to contact Customer Support to reactivate it and pay any outstanding balance in full.” "
                                "(https://linknow.com/terms/, read 2026-11-13)"))),
    "mnsi.net": dict(cls="monthly_or_yearly", read="2026-11-13", url="https://mnsi.net/support/billing",
                 quote="Invoicing is available to approved companies for six-month and twelve-month term plans.",
                 more=("a subscription paid by pre-authorised debit or by card is charged each month (“Pre-Authorized Payment plan (PAP) accounts are debited on your renewal "
                       "date each month.”): which way this organisation pays is not published"),
                 bill=dict(
                     # 2026-11-13 (21Z): the reader had kept its residential page (“We never invoice residential accounts.”), which is not about an organisation's account
                     delivery=("an invoice for an approved company on a term plan: “Invoicing is available to approved companies for six-month and twelve-month term plans.” … "
                               "“Invoices, for approved accounts, are processed on the anniversary day of sign-up.” (https://mnsi.net/support/billing, read 2026-11-13)"),
                     payment=("by pre-authorised debit of the organisation's bank account, by payment sent to its billing department, or by card: “Direct Payment from "
                              "Account, or Pre-Authorized Payment plan (PAP), allows quick, easy payment of your subscription automatically from your checking account.” … "
                              "“Where can I send my payments? MNSi Telecom Attention: Billing Department 3363 Tecumseh Rd E Windsor ON N8W 1H4 Canada” … “Credit Card "
                              "subscriptions will be charged automatically monthly.” (https://mnsi.net/support/billing, read 2026-11-13)"),
                     tax="“The amount including HST will appear on your account statement.” (https://mnsi.net/support/billing, read 2026-11-13)")),
}
BILLING["lightspeed_golf"] = BILLING["lightspeed"]
BILLING["wellnessliving_widget"] = BILLING.get("wellnessliving")
for _k, _b in BILLING.items():
    if _b and _k in VENDORS:
        VENDORS[_k]["billing"] = _b
for _k, _v in VENDORS.items():
    _v["key"] = _k
    for _f in ("host_re", "link_re", "path_re", "asset_re"):
        if _v.get(_f):
            _v[_f + "_c"] = re.compile(_v[_f], re.I)
# The platform domains an organisation's own address may be an alias (CNAME) of -> vendor key. An organisation that points
# learn.example.org at its account on one of these platforms names the vendor in its own DNS: the host sweep keeps such hosts
# (tools/dns_services.py) and tools/lead_crawl.py reads the organisation's site as a candidate of that vendor.
ALIAS_DOMAINS = {"thinkific.com": "thinkific", "docebosaas.com": "docebo", "brightspace.com": "d2l", "desire2learn.com": "d2l", "myabsorb.com": "absorb", "myabsorb.ca": "absorb",
                 "myabsorb.eu": "absorb", "checkfront.com": "checkfront", "edsby.com": "edsby", "escribemeetings.com": "escribe", "bibliocommons.com": "bibliocommons",
                 "coconutcalendar.com": "coconut", "benevity.org": "benevity", "mobius.cloud": "mobius", "unbouncepages.com": "unbounce", "jobbersites.com": "jobber",
                 "shoplightspeed.com": "lightspeed", "janeapp.com": "jane"}
VENDOR_BASES = {"commerce7.com", "myrealpage.com", "socastsrm.com", "socastdigital.com", "jumptools.com", "owlpractice.ca", "juvonno.com", "gorendezvous.com", "rezgo.com", "webrez.com", "webrezpro.com", "thinkific.com", "chronogolf.com", "chronogolf.ca", "checkfront.com", "tbdine.com", "touchbistro.com", "wellnessliving.com", "clubrunner.ca", "crowdriff.com", "nicejob.co", "nicejob.com", "paystone.com", "getjobber.com", "schoolcashonline.com", "kevgroup.com", "benevity.org", "benevity.com", "coconutcalendar.com", "coconutsoftware.com", "mobius.cloud", "digitaled.com",
                "escribemeetings.com", "bibliocommons.com", "bibliocms.com", "brightspace.com", "desire2learn.com",
                "d2l.com", "edsby.com", "amilia.com", "janeapp.com", "jane.app", "docebosaas.com", "docebo.com",
                "myabsorb.com", "myabsorb.ca", "myabsorb.eu", "absorbai.com", "absorblms.com", "shopify.com",
                "myshopify.com", "coveo.com", "unbounce.com", "ubembed.com", "lightspeedhq.com", "shoplightspeed.com"}
SKIP_BASES = {"facebook.com", "fb.com", "linkedin.com", "twitter.com", "x.com", "instagram.com", "youtube.com", "youtu.be",
              "tiktok.com", "pinterest.com", "google.com", "google.ca", "googleapis.com", "gstatic.com", "goo.gl",
              "apple.com", "microsoft.com", "w3.org", "cloudflare.com", "jquery.com", "bootstrapcdn.com", "jsdelivr.net",
              "unpkg.com", "fontawesome.com", "gravatar.com", "wikipedia.org", "creativecommons.org", "github.com",
              "addthis.com", "sharethis.com", "doubleclick.net", "googletagmanager.com", "datadoghq.com",
              "datadoghq-browser-agent.com", "syncfusion.com", "icons8.com", "datatables.net", "vimeo.com", "flickr.com",
              "yelp.com", "yelp.ca", "bit.ly", "cloudfront.net", "amazonaws.com", "hotjar.com", "typekit.net", "adobe.com",
              "zendesk.com", "stackoverflow.com", "stackpath.com", "recaptcha.net", "youtube-nocookie.com",
              "itunes.apple.com", "play.google.com", "wordpress.org", "wordpress.com", "wix.com", "squarespace.com",
              "mailchimp.com", "list-manage.com", "hubspot.com", "zoom.us", "eventbrite.com", "eventbrite.ca",
              "tripadvisor.com", "tripadvisor.ca", "issuu.com", "canada.ca", "gc.ca", "readspeaker.com", "userway.org",
              "accessibe.com", "overdrive.com", "libbyapp.com", "hoopladigital.com", "kanopy.com", "cloudlibrary.com",
              "trustpilot.com", "bbb.org", "paypal.com", "stripe.com", "whatsapp.com", "t.me", "threads.net",
              "bsky.app", "maps.app.goo.gl", "openstreetmap.org", "osm.org", "cdn-cgi", "polyfill.io", "akamaihd.net",
              "msecnd.net", "azureedge.net", "office.com", "sharepoint.com", "live.com", "outlook.com"}
TWO_LEVEL = {"co.uk", "org.uk", "ac.uk", "gov.uk", "com.au", "org.au", "gov.au", "edu.au", "co.nz", "govt.nz",
             "gc.ca", "qc.ca", "on.ca", "bc.ca", "ab.ca", "mb.ca", "sk.ca", "ns.ca", "nb.ca", "nl.ca", "pe.ca",
             "nt.ca", "nu.ca", "yk.ca", "k12.ca.us"}
BAD_TITLE = re.compile(
    r"escribe|published meetings|meeting portal|board manager|meeting manager|^meetings?$|agendas? (?:and|&) minutes|"
    r"^council meetings?$|^public portal$|bibliocommons|biblio ?cms|brightspace|desire2learn|\bd2l\b|edsby|"
    r"amilia|\bjane\b|book online|online booking|booking|select a location|docebo|absorb|^lms$|learning portal|"
    r"^home$|^accueil$|^welcome$|^bienvenue$|\blog ?in\b|\bsign ?in\b|connexion|se connecter|recent activity|catalog(ue)?|"
    r"^search|recherche|^shop$|^store$|^boutique$|page not found|not found|error|erreur|access denied|just a moment|"
    r"trial expired|maintenance|^index$|^untitled|^default$|^portal$|^portail$|^online store$|^my account",
    re.I)
ORG_WORD = re.compile(r"universit|college|coll[eè]ge|c[ée]gep|school|[ée]cole|board|district|city|town|ville|county|"
                      r"municipal|village|township|regional|r[ée]gion|library|biblioth|institute|institut|council|hospital|"
                      r"h[oô]pital|health|sant[ée]|ministry|minist[eè]re|government|gouvernement|association|society|"
                      r"soci[ée]t[ée]|\binc\b|\bltd\b|corporation|foundation|fondation|academy|acad[ée]mie|clinic|clinique|"
                      r"centre|center|church|[ée]glise|club|federation|f[ée]d[ée]ration|authority|agency|agence|commission|"
                      r"department|service", re.I)
CATS = [("meetings", r"agenda|minutes|meeting|council|conseil|s[ée]ances?|ordre[-_ ]du[-_ ]jour|proc[eè]s[-_ ]verba"),
        ("library", r"library|librar|biblioth|catalog"),
        ("pay", r"registration|register|inscription|recreation|loisirs|programs?\b|activit|payment|paiement|pay[-_ ]?online|"
                r"shop|store|boutique|donat|tickets|billet"),
        ("learn", r"brightspace|d2l|\blms\b|e-?learning|online learning|student|[ée]l[eè]ves?|parents?\b|portal|portail|"
                  r"training|formation"),
        ("careers", r"career|\bjobs?\b|employment|emploi|carri[eè]re|work[-_ ]with[-_ ]us|join[-_ ]our[-_ ]team|recrutement"),
        ("bids", r"\bbids?\b|tender|procure|purchas|rfp|rfq|solicitation|appels?[-_ ]d|approvisionnement|soumission")]
CATS = [(n, re.compile(p, re.I)) for n, p in CATS]
NOT_PAGE = re.compile(r"\.(?:pdf|docx?|xlsx?|pptx?|zip|jpe?g|png|gif|svg|mp4|mp3|ics|csv|xml|rss)(?:$|\?)|^mailto:|^tel:|"
                      r"^javascript:|login|logout|signin|/cart", re.I)

A_RE = re.compile(r"(?is)<a\b([^>]*)>(.*?)</a>")
HREF_RE = re.compile(r"""(?is)\bhref\s*=\s*["']([^"'>]+)["']""")
SRC_RE = re.compile(r"""(?is)<(?:script|iframe|img|embed|source|frame)\b[^>]*?\bsrc\s*=\s*["']([^"'>]+)["']""")
LINKTAG_RE = re.compile(r"""(?is)<link\b[^>]*?\bhref\s*=\s*["']([^"'>]+)["']""")
FORM_RE = re.compile(r"""(?is)<form\b[^>]*?\baction\s*=\s*["']([^"'>]+)["']""")
INLINE_RE = re.compile(r"(?is)<script\b[^>]*>(.*?)</script>")
TITLE_RE = re.compile(r"(?is)<title[^>]*>(.*?)</title>")
META_RE = re.compile(r"""(?is)<meta\b[^>]*>""")
IMG_ALT_RE = re.compile(r"""(?is)<img\b[^>]*?\balt\s*=\s*["']([^"']{3,120})["']""")

_glock, _locks, _last = threading.Lock(), {}, {}
_robots, _rlock = {}, threading.Lock()
_out_lock = threading.Lock()


def host_of(u):
    try:
        return (urllib.parse.urlparse(u).hostname or "").lower().rstrip(".")
    except ValueError:
        return ""


def base_domain(h):
    parts = (h or "").lower().split(".")
    if len(parts) >= 3 and ".".join(parts[-2:]) in TWO_LEVEL:
        return ".".join(parts[-3:])
    return ".".join(parts[-2:])


def nowww(h):
    return h[4:] if h.startswith("www.") else h


def _wait(key, gap):
    with _glock:
        lk = _locks.setdefault(key, threading.Lock())
    with lk:
        w = _last.get(key, 0) + gap - time.time()
        if w > 0:
            time.sleep(w)
        _last[key] = time.time()


def _curl(url, limit):
    try:
        p = subprocess.run(["curl", "-sL", "--max-redirs", "6", "-m", "25", "-A", UA, "-w",
                            "\n__ST__%{http_code} %{content_type} %{url_effective}", url], capture_output=True, timeout=40)
    except Exception:
        return 0, url, "", ""
    out = p.stdout.decode("utf-8", "replace")
    body, _, tail = out.rpartition("\n__ST__")
    bits = tail.split(" ")
    try:
        st = int(bits[0])
    except ValueError:
        st = 0
    return st, bits[-1] if len(bits) > 1 else url, body[:limit], " ".join(bits[1:-1])


def fetch(url, gap=1.0, limit=2_000_000, _hops=0):
    """(status, final_url, text, content_type). Polite: <= 1 request per `gap` seconds per registered domain."""
    _wait(base_domain(host_of(url)), gap)
    try:
        req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept": "text/html,application/xhtml+xml,*/*;q=0.5"})
        with urllib.request.urlopen(req, timeout=20) as r:
            ct = r.headers.get("content-type") or ""
            return r.status, r.geturl(), r.read(limit).decode("utf-8", "replace"), ct
    except urllib.error.HTTPError as e:
        loc = e.headers.get("Location") if e.headers else None
        if e.code in (307, 308) and loc and _hops < 3:  # urllib in Python 3.9 does not follow 308
            return fetch(urllib.parse.urljoin(url, loc), gap, limit, _hops + 1)
        return e.code, url, "", ""
    except Exception as e:  # old LibreSSL on macOS python3.9 cannot talk TLS 1.3-only hosts: let curl try
        s = str(e)
        if "SSL" in s and "CERTIFICATE_VERIFY_FAILED" not in s:
            return _curl(url, limit)
        return 0, url, "", ""


def blocked(st, body):
    if st in (401, 403, 429):
        return True
    head = body[:4000].lower()
    return ("<title>just a moment" in head or "cf-chl" in head or "attention required! | cloudflare" in head
            or "captcha-delivery" in head or "/_incapsula_resource" in head)


def allowed(url):
    p = urllib.parse.urlparse(url)
    key = "%s://%s" % (p.scheme, p.netloc)
    with _rlock:
        rp = _robots.get(key)
    if rp is None:
        st, _, body, _ = fetch(key + "/robots.txt", limit=300_000)
        rp = urllib.robotparser.RobotFileParser()
        if st in (401, 403):
            rp.disallow_all = True
        elif st == 200 and "<html" not in body[:600].lower():
            rp.parse(body.splitlines())
        else:
            rp.parse([])
        with _rlock:
            _robots[key] = rp
    try:
        return rp.can_fetch(UA, url)
    except Exception:
        return True


def anchors_of(body, page_url):
    out = []
    for m in A_RE.finditer(body):
        h = HREF_RE.search(m.group(1))
        if not h:
            continue
        href = html.unescape(h.group(1)).strip()
        if href.startswith("#") or "{{" in href:
            continue
        inner = m.group(2)
        txt = re.sub(r"\s+", " ", html.unescape(re.sub(r"<[^>]+>", " ", inner))).strip()
        alt = IMG_ALT_RE.search(inner)
        try:
            out.append((urllib.parse.urljoin(page_url, href), txt[:150], "<img" in inner.lower() or "<svg" in inner.lower(),
                        html.unescape(alt.group(1)).strip() if alt else ""))
        except ValueError:
            continue
    return out


def all_urls(body, page_url):
    urls = [a[0] for a in anchors_of(body, page_url)]
    for rx in (SRC_RE, FORM_RE, LINKTAG_RE):
        for x in rx.findall(body):
            try:
                urls.append(urllib.parse.urljoin(page_url, html.unescape(x).strip()))
            except ValueError:
                pass
    return urls


def portal_hits(u):
    """[(vendor_key, slug, portal_url)] for a URL that points into a kept vendor's customer portal."""
    p = urllib.parse.urlparse(u)
    h = (p.hostname or "").lower()
    res = []
    for k, v in VENDORS.items():
        if v["kind"] != "portal" or v.get("alias_only"):
            continue
        if v.get("link_re_c"):
            m = v["link_re_c"].match(h + p.path)
            if m and m.group(1).lower() not in v["excl"]:
                res.append((k, m.group(1).lower(), v.get("portal_fmt", "https://app.amilia.com/store/en/%s/shop") % m.group(1).lower()))
        if v.get("host_re_c"):
            m = v["host_re_c"].match(h)
            if m and m.group(1).lower() not in v["excl"]:
                res.append((k, h, "https://%s/" % h))
        if v.get("path_re_c") and v["path_re_c"].match(p.path or "") and base_domain(h) not in VENDOR_BASES:
            res.append((k, h, "https://%s/d2l/login" % h))
    return res


def page_meta(body):
    t = TITLE_RE.search(body)
    title = re.sub(r"\s+", " ", html.unescape(t.group(1))).strip() if t else ""
    meta = {}
    for m in META_RE.finditer(body[:200_000]):
        tag = m.group(0)
        pm = re.search(r"""(?:property|name)\s*=\s*["']([^"']+)["']""", tag, re.I)
        cm = re.search(r"""content\s*=\s*(?:"([^"]*)"|'([^']*)')""", tag, re.I)  # the value ends at ITS quote: content="Uncle Bob's Self Storage"
        if pm and cm:
            meta.setdefault(pm.group(1).lower(), html.unescape(cm.group(1) if cm.group(1) is not None else cm.group(2)).strip())
    return title, meta


def clean_name(s):
    if not s:
        return ""
    parts = [p.strip(" -–—|:·•") for p in re.split(r"\s+[|–—:·•]\s+|\s+-\s+|\s*\|\s*", s)]
    good = []
    for p in parts:
        p = re.sub(r"^(?:welcome to|bienvenue (?:à|au|aux|chez)|book (?:online|an appointment) (?:at|with))\s+", "", p, flags=re.I).strip()
        if 3 <= len(p) <= 120 and not BAD_TITLE.search(p) and re.search(r"[A-Za-zÀ-ÿ]{3}", p):
            good.append(p)
    if not good:
        return ""
    org = [p for p in good if ORG_WORD.search(p)]
    return max(org or good, key=len)


def name_tokens(*ss):
    stop = {"the", "and", "of", "de", "du", "des", "la", "le", "les", "city", "town", "county", "public", "library",
            "school", "district", "board", "university", "college", "www", "pub", "com", "org", "net"}
    toks = set()
    for s in ss:
        for t in re.split(r"[^a-z0-9]+", (s or "").lower()):
            if len(t) >= 4 and t not in stop:
                toks.add(t)
    return toks


def pick_website(anchors, page_host, toks):
    cands = {}
    for u, txt, img, alt in anchors:
        h = host_of(u)
        if not h or not u.lower().startswith("http"):
            continue
        b = base_domain(h)
        if b in SKIP_BASES or b in VENDOR_BASES or b == base_domain(page_host) or h in SKIP_BASES:
            continue
        c = cands.setdefault(b, {"score": 0.0, "host": h, "basis": []})
        if img:
            c["score"] += 3
            c["basis"].append("logo link")
        if re.search(r"website|home ?page|^home$|return|back to|visit|main site|site web|site internet|accueil|retour", txt, re.I):
            c["score"] += 2
            c["basis"].append("link text '%s'" % txt[:40])
        if any(t in b.replace("-", "") for t in toks):
            c["score"] += 3
            c["basis"].append("domain matches name")
        c["score"] += 0.5
        if len(h) < len(c["host"]):
            c["host"] = h
    if not cands:
        return "", ""
    b, c = max(cands.items(), key=lambda kv: kv[1]["score"])
    if c["score"] < 3:
        return "", ""
    return "https://%s/" % c["host"], "; ".join(sorted(set(c["basis"])))[:200]


def write_line(f, rec):
    with _out_lock:
        f.write(json.dumps(rec, ensure_ascii=False) + "\n")
        f.flush()


def lead(vkey, publisher, website, dataset_url, row):
    v = VENDORS[vkey]
    dom = nowww(host_of(website)) if website else ""
    row = dict(row)
    row.update(vendor_key=vkey, vendor_trade_name=v["name"], vendor_hq_url=v["hq_url"], vendor_hq_quote=v["hq"],
               observed_date=TODAY, record_date=TODAY)
    if v.get("scope"):
        row["contracting_scope"] = v["scope"]
    return {"platform": "tech", "domain": dom,
            "dataset_id": "tech:%s:%s" % (vkey, dom or row.get("portal_slug") or publisher.lower()),
            "dataset": "organisation uses the paid service of a Canada-HQ vendor (%s), seen on its own site or its customer portal" % v["name"],
            "dataset_url": dataset_url, "publisher": publisher, "buyer_unit": "", "website": website,
            "vendor": v["legal"], "canada_field": CANADA_FIELD, "canada_value": v["hq"], "row": row}


# ----------------------------------------------------------------------------------------------- reverse mode
def load_orgs(paths):
    by_host = {}
    for p in paths:
        if not os.path.exists(p):
            continue
        with open(p, newline="", encoding="utf-8", errors="replace") as f:
            for r in csv.DictReader(line.replace("\0", "") for line in f):
                if not (r.get("ap_email") or "").strip() or not (r.get("evidence_url") or "").startswith("http"):
                    continue
                h = host_of(r["evidence_url"])
                if not h or base_domain(h) in SKIP_BASES or base_domain(h) in VENDOR_BASES:
                    continue
                d = by_host.setdefault(h, {"scheme": urllib.parse.urlparse(r["evidence_url"]).scheme or "https", "orgs": {}})
                d["orgs"].setdefault(r.get("buyer_key") or r.get("org_name_as_found"),
                                     {"name": (r.get("org_name_as_found") or "").strip(), "src": os.path.basename(p)})
    return by_host


def scan_host(h, info):
    """Fetch the home page + <= 3 relevant internal pages of one organisation's site; return (hits, pages, status)."""
    home = "%s://%s/" % (info["scheme"], h)
    if not allowed(home):
        return {}, 0, "robots"
    st, fu, body, ct = fetch(home)
    if blocked(st, body):
        return {}, 1, "blocked"
    if st != 200 or not body:
        return {}, 1, "http_%s" % st
    org_base = base_domain(host_of(fu) or h)
    pages = [(home, fu, body)]
    chosen, used = [], set()
    anchors = anchors_of(body, fu)
    for cat, rx in CATS:
        if len(chosen) >= 3:
            break
        for u, txt, img, alt in anchors:
            hu = host_of(u)
            if base_domain(hu) != org_base or NOT_PAGE.search(u) or u.split("#")[0] in used or u.rstrip("/") == fu.rstrip("/"):
                continue
            if rx.search(txt) or rx.search(urllib.parse.urlparse(u).path):
                chosen.append((cat, u.split("#")[0]))
                used.add(u.split("#")[0])
                break
    for cat, u in chosen:
        if not allowed(u):
            continue
        st2, fu2, b2, ct2 = fetch(u)
        if st2 == 200 and b2 and not blocked(st2, b2):
            pages.append((u, fu2, b2))
        elif st2 == 200 and portal_hits(fu2):  # redirected straight into a portal (body may be JS)
            pages.append((u, fu2, ""))
    hits = {}
    for req_url, final, b in pages:
        for k, slug, purl in portal_hits(final):
            hits.setdefault(k, {}).setdefault(slug, (req_url, final, purl, "redirect to the vendor portal"))
        if not b:
            continue
        for u in all_urls(b, final):
            for k, slug, purl in portal_hits(u):
                hits.setdefault(k, {}).setdefault(slug, (final, u, purl, "link/embed on the organisation's page"))
        if base_domain(host_of(final)) != org_base:
            continue
        assets = " ".join(SRC_RE.findall(b) + LINKTAG_RE.findall(b) + INLINE_RE.findall(b)[:40])
        for k, v in VENDORS.items():
            if v["kind"] == "asset" and v.get("asset_re_c"):
                m = v["asset_re_c"].search(assets)
                if m:
                    kind = "asset loaded by the organisation's own page"
                    if k == "shopify":  # Shopify Inc. contracts only with US/Canada billing addresses: keep stores set to CA/US
                        mc = re.search(r'Shopify\.country\s*=\s*"([A-Z]{2})"', b)
                        if mc and mc.group(1) not in ("CA", "US"):
                            continue
                        kind += " (Shopify.country=%s)" % (mc.group(1) if mc else "?")
                    ctx = assets[max(0, m.start() - 60):m.end() + 60].replace("\n", " ")
                    hits.setdefault(k, {}).setdefault("asset", (final, ctx.strip(), "", kind))
    if "jane" in hits:  # the free Jane plan allows one practitioner: keep clinics whose portal lists 2+
        for slug, t in list(hits["jane"].items()):
            info, _ = portal_info("jane", t[2])
            if not info:
                del hits["jane"][slug]
        if not hits["jane"]:
            del hits["jane"]
    return hits, len(pages), "ok"


def reverse(args):
    by_host = load_orgs(args.inputs)
    hosts = sorted(h for h, d in by_host.items() if len(d["orgs"]) <= 3)  # shared portals (many orgs) cannot be attributed
    if args.limit:
        hosts = hosts[:args.limit]
    os.makedirs(LEADS, exist_ok=True)
    out_path = args.out or os.path.join(LEADS, "socrata_tech_reverse.jsonl")
    stats = {"hosts": len(hosts), "orgs": sum(len(by_host[h]["orgs"]) for h in hosts), "status": {}, "hosts_with_hit": 0,
             "orgs_with_hit": 0, "per_vendor": {}, "directory_skipped": 0, "leads": 0}
    t0 = time.time()
    with open(out_path, "w", encoding="utf-8") as f:
        def work(h):
            try:
                return h, scan_host(h, by_host[h])
            except Exception as e:
                return h, ({}, 0, "error %s" % type(e).__name__)
        done = 0
        with ThreadPoolExecutor(args.workers) as ex:
            for h, (hits, npages, status) in ex.map(work, hosts):
                done += 1
                stats["status"][status.split(" ")[0]] = stats["status"].get(status.split(" ")[0], 0) + 1
                orgs = by_host[h]["orgs"]
                got = False
                for k, slugs in hits.items():
                    if len(slugs) > 2:  # a page linking 3+ different tenants is a directory, not the org's own service
                        stats["directory_skipped"] += 1
                        continue
                    slug, (page, sig, purl, kind) = sorted(slugs.items())[0]
                    for bk, o in orgs.items():
                        if not o["name"]:
                            continue
                        toks = name_tokens(o["name"], h)
                        row = {"buyer_key": bk, "org_name_as_found": o["name"], "source_list": o["src"],
                               "signature": sig[:300], "signature_kind": kind, "page_seen": page,
                               "portal_url": purl, "portal_slug": slug if slug != "asset" else "",
                               "slug_matches_org": bool(slug != "asset" and any(t in slug.replace("-", "") for t in toks)),
                               "other_tenants_linked": len(slugs) - 1}
                        write_line(f, lead(k, o["name"], "https://%s/" % h, page, row))
                        stats["leads"] += 1
                    stats["per_vendor"][k] = stats["per_vendor"].get(k, 0) + 1
                    got = True
                if got:
                    stats["hosts_with_hit"] += 1
                    stats["orgs_with_hit"] += len(orgs)
                if done % 100 == 0:
                    print(time.strftime("%H:%M:%S"), "reverse %d/%d hosts, %d with a hit, %s" %
                          (done, len(hosts), stats["hosts_with_hit"], json.dumps(stats["per_vendor"])), flush=True)
    stats["seconds"] = int(time.time() - t0)
    ok = stats["status"].get("ok", 0)
    stats["hit_rate_of_fetched_sites"] = round(stats["hosts_with_hit"] / ok, 4) if ok else 0
    json.dump(stats, open(out_path + ".stats", "w"), indent=1)
    print("DONE reverse", json.dumps(stats), flush=True)


# ----------------------------------------------------------------------------------------------- forward mode
def cc_get(url, tries=4):
    for i in range(tries):
        st, fu, body, ct = fetch(url, gap=2.0, limit=60_000_000)
        if st == 200:
            return body
        if st in (400, 404):
            return ""
        time.sleep((10, 30, 60, 90)[i])
    return None


def cc_urls(pattern, crawls, max_pages):
    os.makedirs(os.path.join(CACHE, "cc"), exist_ok=True)
    prefix = not pattern.startswith("*.")
    for cid, api in crawls:
        q = {"url": pattern, "output": "json", "fl": "url"}
        if prefix:
            q["matchType"] = "prefix"
        base = api + "?" + urllib.parse.urlencode(q)
        tag = re.sub(r"[^a-z0-9]+", "_", pattern.lower()).strip("_")
        info = cc_get(base + "&showNumPages=true")
        try:
            n = int(json.loads(info)["pages"]) if info else 0
        except (ValueError, KeyError, TypeError):
            n = 0
        print(time.strftime("%H:%M:%S"), "cc %s %s: %d index pages" % (cid, pattern, n), flush=True)
        for page in range(min(n, max_pages)):
            cf = os.path.join(CACHE, "cc", "%s_%s_%d.jsonl" % (cid, tag, page))
            if os.path.exists(cf) and os.path.getsize(cf) > 0:
                body = open(cf, encoding="utf-8", errors="replace").read()
            else:
                body = cc_get(base + "&page=%d" % page)
                if body is None:
                    print("  cc page %d failed (503/504 after retries)" % page, flush=True)
                    continue
                open(cf, "w", encoding="utf-8").write(body)
            for line in body.splitlines():
                try:
                    yield cid, json.loads(line)["url"]
                except (ValueError, KeyError):
                    continue


def portal_info(vkey, purl):
    if not allowed(purl):
        return None, "robots"
    st, fu, body, ct = fetch(purl, gap=1.0)
    if blocked(st, body):
        return None, "blocked"
    if st != 200 or not body:
        return None, "http_%s" % st
    if "trialexpired" in fu.lower().replace("-", "").replace("_", ""):
        return None, "trial_expired"
    title, meta = page_meta(body)
    anchors = anchors_of(body, fu)
    staff = set(re.findall(r"#/staff_member/(\d+)", body))
    if vkey == "jane" and len(staff) < 2:
        return None, "jane_lt2_practitioners"  # the free Jane plan allows one practitioner
    name, basis = "", ""
    for label, s in (("og:site_name", meta.get("og:site_name")), ("title", title), ("og:title", meta.get("og:title")),
                     ("application-name", meta.get("application-name"))):
        name = clean_name(s)
        if name:
            basis = label
            break
    if not name:
        for u, txt, img, alt in anchors:
            if img and alt and ORG_WORD.search(alt) and not BAD_TITLE.search(alt):
                name, basis = alt.strip(), "logo alt text"
                break
    slug = host_of(fu).split(".")[0].replace("pub-", "")
    if vkey == "benevity":  # the page shows the programme's brand ("My Impact Hub"); the employer is in the text or the slug
        txt = re.sub(r"\s+", " ", html.unescape(re.sub(r"(?is)<(script|style)[^>]*>.*?</\1>|<[^>]+>", " ", body[:400_000])))
        m = re.search(r"(?:Welcome to|Welcome,?|for|of)\s+(?:the\s+)?([A-Z][\w&.,'’ -]{2,60}?)\s+(?:Employees|employees|Team Members|team members|Associates|Colleagues|Staff)\b", txt) or \
            re.search(r"\b([A-Z][\w&.,'’ -]{2,60}?)\s+(?:Employee|Team Member|Associate|Colleague)\s+(?:Giving|Volunteering|Impact|Community|Engagement)\b", txt)
        if m and not BAD_TITLE.search(m.group(1)):
            name, basis = m.group(1).strip(" ,.-"), "programme text (employer named)"
        elif name and re.search(r"benevity|login|sign in", name, re.I):
            name = ""
    if vkey == "amilia":
        m = re.search(r"/store/(?:en|fr|es)/([a-z0-9-]+)", fu, re.I)
        slug = m.group(1) if m else slug
    elif VENDORS.get(vkey, {}).get("link_re_c"):  # a portal named by its path (tbdine.com/restaurant/<slug>): the slug is in the path, not the host
        pu = urllib.parse.urlparse(fu)
        m = VENDORS[vkey]["link_re_c"].match((pu.hostname or "").lower() + pu.path) or VENDORS[vkey]["link_re_c"].match(urllib.parse.urlparse(purl).hostname.lower() + urllib.parse.urlparse(purl).path)
        slug = m.group(1).lower() if m else slug
    website, wbasis = pick_website(anchors, host_of(fu), name_tokens(name, slug))
    if website and not name:  # the portal names no organisation: read the organisation's own home page title
        if allowed(website):
            st2, fu2, b2, _ = fetch(website)
            if st2 == 200 and b2 and not blocked(st2, b2):
                t2, m2 = page_meta(b2)
                name = clean_name(m2.get("og:site_name")) or clean_name(t2)
                basis = "title of the linked organisation website" if name else ""
    if not name:
        return None, "no_name"
    if vkey == "benevity" and website and re.search(r"g2\.com|benevity\.|linkedin|facebook|twitter|instagram|youtube|apple\.com|google\.com", website):
        website, wbasis = "", ""
    return {"name": name, "name_basis": basis, "website": website, "website_basis": wbasis, "final_url": fu,
            "page_title": title[:200], "og_site_name": meta.get("og:site_name", "")[:200], "slug": slug,
            "practitioners_listed": len(staff) if vkey == "jane" else None}, "ok"


def cdx_urls(pattern, limit=60000):
    """URLs of the vendor's customer portals listed by the Internet Archive's CDX index (captured since 2022); the
    LIVE portal page is what gets read. Large domains are read page by page (the index's own pagination), 3 s apart,
    one host of each URL kept; cached for a week (never an empty answer)."""
    os.makedirs(os.path.join(CACHE, "cdx"), exist_ok=True)
    dom = pattern.replace("*.", "").split("/")[0]
    cf = os.path.join(CACHE, "cdx", re.sub(r"[^a-z0-9.]+", "_", pattern) + ".jsonl")
    if os.path.exists(cf) and os.path.getsize(cf) > 0 and time.time() - os.path.getmtime(cf) < 7 * 86400:
        return [l.strip() for l in open(cf, encoding="utf-8") if l.strip()]
    base = [("url", dom if pattern.startswith("*.") else pattern), ("matchType", "domain" if pattern.startswith("*.") else "prefix"),
            ("output", "json"), ("fl", "original"), ("filter", "statuscode:200"), ("filter", "mimetype:text/html"), ("from", "2022"),
            ("collapse", "urlkey")]
    def get(params, timeout=120):
        time.sleep(3)
        req = urllib.request.Request("https://web.archive.org/cdx/search/cdx?" + urllib.parse.urlencode(params), headers={"User-Agent": UA})
        with urllib.request.urlopen(req, timeout=timeout) as r:
            return r.read(80_000_000).decode("utf-8", "replace")
    hosts, out = set(), []
    def take(rows):
        for row in rows:
            u = row[0] if isinstance(row, list) else row
            h = (urllib.parse.urlparse(u).hostname or "").lower()
            if h and h not in hosts:
                hosts.add(h); out.append(u)
    try:  # how many index pages (blocks) the query spans
        n = int((get(base[:2] + [("showNumPages", "true")], 60) or "1").strip() or 1)
    except Exception as e:
        print("cdx %s pages: %s" % (pattern, e), flush=True)
        n = 1
    pages_read = 0
    for pg in range(min(n, 400)):
        for attempt in range(4):  # the index answers 503 / 504 under load: wait and ask again
            try:
                txt = get(base + [("page", str(pg))])
                rows = json.loads(txt or "[]")
                take(rows[1:] if rows and rows[0] == ["original"] else rows)
                pages_read += 1
                break
            except Exception as e:
                print("cdx %s page %d/%d try %d: %s" % (pattern, pg, n, attempt + 1, e), flush=True)
                time.sleep(30 * (attempt + 1))
        if len(out) >= limit:
            break
    print(time.strftime("%H:%M:%S"), "cdx %s: %d pages (%d read), %d hosts" % (pattern, n, pages_read, len(out)), flush=True)
    if out:
        with open(cf, "w", encoding="utf-8") as f:
            f.write("\n".join(out))
    return out


def forward(vkey, args):
    v = VENDORS[vkey]
    portals = {}
    if getattr(args, "source", "cc") == "cdx":
        crawls = [("wayback-cdx", "")]
        for pat in v["cc"]:
            for u in cdx_urls(pat):
                for k, slug, purl in portal_hits(u):
                    if k == vkey and slug not in portals:
                        portals[slug] = (purl, "wayback-cdx", u)
    else:
        coll = json.loads(cc_get("https://index.commoncrawl.org/collinfo.json") or "[]")
        crawls = [(c["id"], c["cdx-api"]) for c in coll[:args.crawls]]
        for pat in v["cc"]:
            for cid, u in cc_urls(pat, crawls, args.max_pages):
                for k, slug, purl in portal_hits(u):
                    if k == vkey and slug not in portals:
                        portals[slug] = (purl, cid, u)
    slugs = sorted(portals)
    print(time.strftime("%H:%M:%S"), "%s: %d distinct portals in Common Crawl" % (vkey, len(slugs)), flush=True)
    if args.limit:
        slugs = slugs[:args.limit]
    os.makedirs(LEADS, exist_ok=True)
    out_path = args.out or os.path.join(LEADS, "socrata_tech_%s%s.jsonl" % (vkey, "_cdx" if getattr(args, "source", "cc") == "cdx" else ""))
    stats = {"vendor": vkey, "crawls": [c[0] for c in crawls], "portals_in_cc": len(portals), "portals_read": len(slugs),
             "status": {}, "leads": 0, "with_website": 0}
    seen = set()
    t0 = time.time()
    with open(out_path, "w", encoding="utf-8") as f:
        for i, slug in enumerate(slugs, 1):
            purl, cid, ccu = portals[slug]
            try:
                info, status = portal_info(vkey, purl)
            except Exception as e:
                info, status = None, "error_%s" % type(e).__name__
            stats["status"][status] = stats["status"].get(status, 0) + 1
            if info:
                key = (info["name"].lower(), nowww(host_of(info["website"])) if info["website"] else slug)
                if key not in seen:
                    seen.add(key)
                    row = {"portal_url": info["final_url"], "portal_slug": info["slug"], "page_title": info["page_title"],
                           "og_site_name": info["og_site_name"], "name_basis": info["name_basis"],
                           "website_basis": info["website_basis"], "signature": host_of(purl) + urllib.parse.urlparse(purl).path,
                           "signature_kind": "vendor-hosted customer portal (%s)" % ("listed by the Internet Archive CDX index, live page read" if cid == "wayback-cdx" else "Common Crawl %s" % cid),
                           "common_crawl_url": ccu}
                    if info["practitioners_listed"] is not None:
                        row["practitioners_listed"] = info["practitioners_listed"]
                    write_line(f, lead(vkey, info["name"], info["website"], info["final_url"], row))
                    stats["leads"] += 1
                    stats["with_website"] += bool(info["website"])
            if i % 50 == 0:
                print(time.strftime("%H:%M:%S"), "%s %d/%d portals, %d leads, %s" % (vkey, i, len(slugs), stats["leads"],
                                                                                       json.dumps(stats["status"])), flush=True)
    stats["seconds"] = int(time.time() - t0)
    json.dump(stats, open(out_path + ".stats", "w"), indent=1)
    print("DONE forward", json.dumps(stats), flush=True)


def main():
    a = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    a.add_argument("--reverse", action="store_true")
    a.add_argument("--forward", metavar="VENDOR")
    a.add_argument("--inputs", nargs="*", default=INPUTS)
    a.add_argument("--limit", type=int, default=0, help="test: first N organisations / portals")
    a.add_argument("--workers", type=int, default=12)
    a.add_argument("--crawls", type=int, default=2)
    a.add_argument("--max-pages", type=int, default=300, help="Common Crawl index pages per pattern per crawl")
    a.add_argument("--out", default="")
    a.add_argument("--source", default="cc", choices=["cc", "cdx"], help="portal list: Common Crawl index or Internet Archive CDX")
    args = a.parse_args()
    if args.reverse:
        reverse(args)
    elif args.forward:
        keys = [k for k, v in VENDORS.items() if v["kind"] == "portal"] if args.forward == "all" else [args.forward]
        for k in keys:
            if k not in VENDORS or VENDORS[k]["kind"] != "portal":
                sys.exit("unknown portal vendor %s (choose from %s)" % (k, ", ".join(x for x in VENDORS if VENDORS[x]["kind"] == "portal")))
            forward(k, args)
    else:
        a.print_help()


if __name__ == "__main__":
    main()
