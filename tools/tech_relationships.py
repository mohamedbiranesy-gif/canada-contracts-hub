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
                    scope="Shopify Inc. contracts only with merchants whose billing address is in the United States or Canada", scope_countries=("US", "CA")),
    "coveo": dict(name="Coveo", legal="Coveo Solutions Inc.", kind="asset",
                  hq_url="https://ir.coveo.com/en",
                  hq="Coveo Solutions Inc. 1100 Av. Des Canadiens-de-Montréal Suite 401 Montréal, Québec H3B 2S2 Canada",
                  asset_re=r"static\.cloud\.coveo\.com|platform(?:-[a-z]+)?\.cloud\.coveo\.com|coveo-search-ui|CoveoSearch|atomic-search-interface"),
    "unbounce": dict(name="Unbounce", legal="Unbounce Inc.", kind="asset",
                     hq_url="https://unbounce.com/contact-us/",
                     hq="drop into our headquarters to say hi in person. Vancouver 603-401 West Georgia St. Vancouver, BC, Canada, V6B 5A1",
                     asset_re=r"assets\.ubembed\.com|//[a-z0-9-]+\.ubembed\.com"),
    "lightspeed": dict(name="Lightspeed", legal="Lightspeed Commerce Inc.", kind="asset",
                       hq_url="https://www.lightspeedhq.com/about/",
                       hq="Proudly headquartered in Montreal, Canada (700 St-Antoine Est, Montreal, Quebec, Canada, H2Y 1A6)",
                       asset_re=r"cdn\.shoplightspeed\.com|cdn\.webshopapp\.com"),
}
for _k, _v in VENDORS.items():
    _v["key"] = _k
    for _f in ("host_re", "link_re", "path_re", "asset_re"):
        if _v.get(_f):
            _v[_f + "_c"] = re.compile(_v[_f], re.I)
VENDOR_BASES = {"checkfront.com", "tbdine.com", "touchbistro.com", "wellnessliving.com", "clubrunner.ca", "crowdriff.com", "nicejob.co", "nicejob.com", "paystone.com", "getjobber.com", "schoolcashonline.com", "kevgroup.com", "benevity.org", "benevity.com", "coconutcalendar.com", "coconutsoftware.com", "mobius.cloud", "digitaled.com",
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
        if v["kind"] != "portal":
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
