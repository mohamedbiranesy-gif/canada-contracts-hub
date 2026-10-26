# SOURCE INTELLIGENCE BRIEF

**Goal:** find every public source of *awarded* contracts that names the supplier **with its location** (country, address, province or postal code) and is **not** already in `04_SOURCES_COVERED.md`. Claude builds the pipelines. Your job is finding them and saying exactly how to pull them.

## Gemini — Canada (priority order)
1. Federal Crown corporations' own contract disclosures (quarterly "contracts over $10,000"): CBC/Radio-Canada, Canada Post, VIA Rail, BDC, EDC, FCC, CMHC, Canada Lands, NCC, museums, House of Commons, Senate…
2. Provincial Crown corporations and agencies: Hydro-Québec, Loto-Québec, SAQ, Investissement Québec, OPG, Hydro One, Metrolinx, Infrastructure Ontario, LCBO, BC Hydro, ICBC, BC Transit, SaskPower, SaskTel, Manitoba Hydro, MPI, NB Power, Nova Scotia Power (private), NL Hydro, ATCO (private)…
3. Provincial contract disclosures and sole-source registers: Ontario, Alberta, BC, Nova Scotia, PEI, New Brunswick, Manitoba, Saskatchewan, the territories.
4. Health authorities, universities, colleges and school boards that publish award lists (e.g. Ontario BPS award notices; Alberta Health Services; BC health authorities; Ontario Health).
5. Municipalities with their own award or council-report lists outside bids&tenders, MERX and Biddingo.

## ChatGPT — outside Canada
1. National e-procurement portals and open-data feeds that record **supplier country** (OCDS publishers, EU national portals below the TED thresholds, Latin America, Asia-Pacific, Africa, the Middle East).
2. US state and city contract datasets that record **vendor country or province**.
3. International organisations' own award lists: UN agencies, development banks, NATO agencies, ESA, CERN, ITER…

## For each source, report (06_RETURN_FORMATS.md §4)
- name, publisher, URL;
- coverage;
- access type (bulk file / API / HTML list / PDF);
- the supplier-location field;
- date / term fields;
- volume estimate;
- login or bot protection;
- exact `how_to_pull` (endpoint, parameters, file URL).
Skip anything already covered, login-only or CAPTCHA-protected.
