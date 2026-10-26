"""Regenerate notes/enrichment_buyers_v2.md from current v2 outputs (re-run after each assemble)."""
import sys, os, json, collections, glob
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from common import *

L = [json.loads(l) for l in open(OUT_ENRICHED)]
B = {json.loads(l)['buyer_key']: json.loads(l) for l in open(INPUT)}
CL = json.load(open(WORK + '/classify.json'))
st = json.load(open(WORK + '/assemble_stats.json'))
crawl_status = collections.Counter(); pages = 0; blocked = []; okset = set(); nsites = collections.Counter()
for f in sorted(glob.glob(WORK + '/crawl*.jsonl')) + sorted(glob.glob(WORK + '/deep*.jsonl')) + sorted(glob.glob(WORK + '/pdf*.jsonl')):
    tag = os.path.basename(f).split('.')[0]
    for l in open(f):
        r = json.loads(l)
        crawl_status[(tag, r['status'])] += 1; nsites[tag] += 1
        pages += len(r.get('pages', []))
        if r['status'] in ('blocked_or_challenged', 'partially_blocked'):
            blocked.append(r['site'])
        if r['status'] == 'ok' and r.get('pages'):
            okset.add(r['site'])
reused = json.load(open(WORK + '/sites_reused_v1.json')) if os.path.exists(WORK + '/sites_reused_v1.json') else []
manual = [json.loads(l) for l in open(WORK + '/manual_ap.jsonl')] if os.path.exists(WORK + '/manual_ap.jsonl') else []
probes = [json.loads(l) for l in open(WORK + '/probe_log.jsonl')] if os.path.exists(WORK + '/probe_log.jsonl') else []
probe_blocked = sorted({p['url'] for p in probes if p.get('blocked') or p.get('status') == 'robots_disallow'})
blocked_u = sorted(set(blocked) - okset)
hm = [x for x in L if B[x['buyer_key']]['record_count_high_or_medium'] > 0]


def has_ap(x):
    return bool(x['ap_contact']['emails'] or x['ap_contact']['invoice_portal'] or x['ap_contact']['invoicing_requirements'])


grp = collections.defaultdict(lambda: [0, 0, 0, 0, 0])  # n, website, ap email, ap any, hm
for x in L:
    b = B[x['buyer_key']]
    g = b['sources'][0]['value']
    a = grp[g]; a[0] += 1; a[1] += bool(x['official_website']); a[2] += bool(x['ap_contact']['emails']); a[3] += has_ap(x); a[4] += b['record_count_high_or_medium'] > 0
grp_rows = '\n'.join('| %s | %d | %d | %d | %d | %d |' % (g, a[0], a[4], a[1], a[2], a[3]) for g, a in sorted(grp.items(), key=lambda t: -t[1][0]))
# organisations (parents joined)
agg = collections.defaultdict(lambda: {'hm': 0, 'web': False, 'ap': False, 'apany': False, 'proc': False, 'keys': 0})
for x in L:
    po = x['extras'].get('parent_organisation')
    k = po['name'] if po else (x['canonical_name'] or x['name'])
    a = agg[k]; a['hm'] += B[x['buyer_key']]['record_count_high_or_medium']; a['keys'] += 1
    a['web'] |= bool(x['official_website']); a['ap'] |= bool(x['ap_contact']['emails']); a['apany'] |= has_ap(x)
    a['proc'] |= bool(x['procurement_contact']['emails'] or x['procurement_contact']['url'])
top = sorted(agg.items(), key=lambda t: -t[1]['hm'])[:150]
top_line = 'Of the 150 distinct organisations with the most high/medium contract records (divisions/ministries joined to their parent): website %d, AP mailbox %d, AP mailbox or invoice portal or invoicing instructions %d, procurement mailbox or page %d.' % (
    sum(a['web'] for k, a in top), sum(a['ap'] for k, a in top), sum(a['apany'] for k, a in top), sum(a['proc'] for k, a in top))
top_rows = '\n'.join('| %d | %s | %d | %s | %s |' % (i + 1, k[:70], a['hm'], 'yes' if a['web'] else '', 'e-mail' if a['ap'] else ('portal/instructions' if a['apany'] else '')) for i, (k, a) in enumerate(top[:60]))
man_rows = []
for m in manual:
    mt = m['match']; who = mt.get('parent_key') or mt.get('name_regex') or mt.get('website_host') or str(mt)
    man_rows.append('- `%s` — %s (retrieved %s): AP %s%s%s' % (who, m['url'], m.get('retrieved_at', ''), ', '.join(m.get('ap_emails', [])) or '—',
                                                         ('; portal: ' + m['invoice_portal']) if m.get('invoice_portal') else '',
                                                         ('; procurement: ' + ', '.join(m['proc_emails'])) if m.get('proc_emails') else ''))
wd_files = sorted(glob.glob(DL2 + '/dir/wikidata/batch_*.json'))
wd_t = [json.load(open(f))['_retrieved_at'] for f in wd_files[:1] + wd_files[-1:]] if wd_files else ['', '']
src_counts = collections.Counter()
for x in L:
    for s in x['extras'].get('directory_sources', []):
        src_counts[(s['source'].split(' (')[0][:60], s.get('match_confidence', ''))] += 1
src_rows = '\n'.join('| %s | %s | %d |' % (k[0], k[1], v) for k, v in src_counts.most_common())
par_counts = collections.Counter((x['extras'].get('parent_organisation') or {}).get('name') for x in L if x['extras'].get('parent_organisation'))
amb = [x for x in L if x['extras'].get('jurisdiction_candidates')]
prec = json.load(open(WORK + '/precision.json')) if os.path.exists(WORK + '/precision.json') else {}
cs = ', '.join('%s %s: %d' % (k[0], k[1], v) for k, v in sorted(crawl_status.items()))
ts = now()

md = f"""# Buyer enrichment v2 (buyers_enriched_v2.jsonl) — 2,055 buyers added later

Generated {ts} by `scripts/enrichment_buyers_v2/notes.py` (re-run after each assemble). Output: `enrichment/v2/buyers_enriched_v2.jsonl`, one line for **every** one of the {len(L)} buyers in `enrichment/v2/buyers_new_input.jsonl` (input order; the {len(hm)} buyers with high/medium-confidence contracts come first), keyed by `buyer_key`, same record layout as `enrichment/buyers_enriched.jsonl` (see `notes/enrichment_buyers.md`). Buyers with nothing found still get a line whose `notes` says so. Pipeline = copy of `scripts/enrichment_buyers/` adapted in `scripts/enrichment_buyers_v2/` (originals and `enrichment/buyers_enriched.jsonl` untouched); work files in `enrichment/work_buyers_v2/`, new downloads in `downloads/enrichment_buyers_v2/`.

## Coverage (all {len(L)} buyers / {len(hm)} high-medium buyers)

| field | all buyers | high/medium buyers |
|---|---|---|
| official_website (directory, parent organisation's site, or known official domain; `extras.website_check` = crawl status) | {st.get('website',0)} | {st.get('hm_website',0)} |
| directory identifiers (Wikidata QID, Ontario board number, …; dataset identifiers are in `identifiers.from_dataset`) | {st.get('identifiers_directory',0)} | {st.get('hm_identifiers_directory',0)} |
| address (directory, else buyer address as published in the notices, some partial) | {st.get('address',0)} | {st.get('hm_address',0)} |
| ap_contact.emails (supplier-invoicing / accounts-payable role mailboxes, own or parent organisation's) | {st.get('ap_email',0)} | {st.get('hm_ap_email',0)} |
| ap_contact.invoice_portal (SAP Business Network/1GX, Ontario Vendor Portal, Ariba …) | {st.get('invoice_portal',0)} | {st.get('hm_invoice_portal',0)} |
| ap_contact.invoicing_requirements (curated text or page excerpt) | {st.get('invoicing_requirements',0)} | {st.get('hm_invoicing_requirements',0)} |
| procurement_contact.emails (role mailboxes) | {st.get('procurement_email',0)} | {st.get('hm_procurement_email',0)} |
| procurement_contact.url | {st.get('procurement_url',0)} | {st.get('hm_procurement_url',0)} |
| general_contact.emails | {st.get('general_email',0)} | {st.get('hm_general_email',0)} |

{top_line}

By source group of the buyer (first source; n / high-medium / website / AP e-mail / AP e-mail-or-portal-or-instructions):

| source | buyers | h/m | website | AP e-mail | AP any |
|---|---|---|---|---|---|
{grp_rows}

Record additions vs v1 layout: `extras.parent_organisation` (name, key, jurisdiction, basis, website) for divisions and provincial/state government units — the AP/invoicing facts of the parent apply to them (e.g. every "City of Toronto – <division>" gets the City's accounts-payable requirements; every GNL department gets the central GNL invoice mailbox); `extras.jurisdiction_candidates` for {len(amb)} buyer keys whose bare name ("Infrastructure", "Finance", "Justice", "Education", "Municipal Affairs", "Executive Council", "Public Service Commission", "Legislative Assembly", "Advanced Education", "Agriculture"…) is used by departments of several governments in the merged data — no single organisation is asserted, instead one entry per government with that government's central AP facts (pick by the record's source); `identifiers.wikidata_qid`; `extras.website_check.reused_from_v1`.

Parent organisations assigned ({sum(par_counts.values())} buyer keys): """ + ', '.join('%s %d' % kv for kv in par_counts.most_common()) + f"""

## Sources (fetched {ts[:10]} unless stated)

Directory / website sources:
| source | match confidence | buyers |
|---|---|---|
{src_rows}

- Parent-organisation rules (`classify.py`): name patterns for divisions ("City of Toronto - …", "City of Ottawa - …", "Commonwealth of Massachusetts - …", "State of Vermont — …", "UNDP - …", "NL Health Services - …", …) and provincial/territorial government units: buyers published by a provincial government's own award source (BC ministry awards, Alberta sole-source disclosure, Alberta APC ministries list, Nova Scotia / Saskatchewan / Newfoundland / NWT sources) whose names are department-like (no municipal designation, no university/board/authority/corporation/… words) → that government. Official sites of the parents are listed in `bulk_v2.py` (PARENT_SITE); government portals were not crawled (their central AP pages were researched directly).
- Wikidata SPARQL (https://query.wikidata.org/sparql, {len(wd_files)} batches {wd_t[0]} – {wd_t[-1]}, raw JSON in `downloads/enrichment_buyers_v2/dir/wikidata/`): exact label/alias (en, fr) lookup of name variants (full name, designation-stripped core, "X County"/"County of X"/"Regional Municipality of X" …) → items with official website P856, country P17, class P31 and the province/state reached through P131*. Accepted only when the item is in the buyer's country and province/state (province from the source, notice address, MERX location, or the bids&tenders portal time zone), with municipal class preferred for designated names and full-name labels preferred over core labels; ties with different websites are left unresolved (noted). 'strong' = province verified; 'weak' = unique match without province evidence.
- Ontario Ministry of Education "School board and school authority contact information" (data.ontario.ca, September 2026 CSV, `dir/on_school_board_contact_list_september2026_en.csv`, 85 boards: board number, address, phone, fax, website) — exact normalized board name.
- Alias table (`bulk_v2.py` ALIAS): official domains of well-known organisations (universities, colleges, crowns, utilities, police services, school divisions, Texas/Virginia institutions, EU agencies) — every such site was fetched by the crawler (status in `extras.website_check`).
- Website fields published in the notice's buyer contact block (e.g. PROMPERU, Peruvian/Chilean/EU notices).
- Checked and not usable: CivicInfo BC directory (https://www.civicinfo.bc.ca/directories → Cloudflare "Just a moment" challenge, 403; skipped), Alberta "Find a municipal official" (https://www.alberta.ca/find-a-municipal-official, interactive page behind reCAPTCHA; skipped), Ontario "List of Ontario municipalities" page (no website links). Saskatchewan / Nova Scotia / Newfoundland municipal directories were not reached in the time budget — Wikidata covered most of those municipalities.

Crawler (`crawl.py`, unchanged politeness: UA `{UA}`, robots.txt honoured, 0.7 s spacing per host ≈ 1.4 req/s, homepage + ≤ 13 same-site pages chosen by invoice/supplier/procurement/contact keywords); sitemap pass (`deep.py`) for high-priority sites still lacking an AP mailbox; PDF pass (`pdfpass.py`, now honouring robots.txt) over linked supplier/direct-deposit/invoice PDFs. Sites already crawled by the v1 run were reused from `enrichment/work_buyers/` instead of re-fetched ({len(reused)} sites: {', '.join(x['site'] for x in reused[:12])}). Run statistics (pass status: sites): {cs}; HTML/PDF pages fetched in v2: {pages}.

Targeted research (WebSearch to locate candidate pages, then the page itself fetched with `probe.py` — robots.txt checked, bot-challenge/403 pages logged and skipped, raw copy under `downloads/enrichment_buyers_v2/pages/`, {len(probes)} fetches logged in `enrichment/work_buyers_v2/probe_log.jsonl`). `add_manual.py` refuses an e-mail unless it appears in the fetched copy of the cited URL. {len(manual)} curated findings in `enrichment/work_buyers_v2/manual_ap.jsonl`:
""" + '\n'.join(man_rows) + f"""

## Matching / e-mail rules
- Same e-mail rules as v1 (precision over recall): only addresses copied from the organisation's own pages/documents (or the notice's own contact field for procurement role boxes), each with page URL + retrieval time + snippet in `*.evidence`; personal-looking local parts dropped (first.last, initial+surname, name+digits without role word — e.g. the bids&tenders "purchasing representatives" and APC contact persons in the input are never copied); no address constructed from a pattern; a Cloudflare-obfuscated address (TDSB invoice box) was NOT decoded.
- v2 classifier fix: receivable/customer-billing boxes (water billing, utility billing, tax, AR tokens) are no longer classed as accounts payable (found in the first crawl results: waterbilling…@peelregion.ca, finance-ar@ornge.ca).
- Parent facts are attached to units: the City of Toronto AP requirements apply to all Toronto divisions; GNL's central gnlinvoices@gov.nl.ca applies to provincial departments only (the GNL page says it does not apply to NL Health Services or crown corporations — those keep their own facts); GNWT FESS mailbox applies to GNWT departments, Housing NWT and NTHSSA (stated on the GNWT page).

## Precision checks
""" + ('\n'.join('- ' + v for v in prec.get('lines', [])) or '- (pending)') + f"""

## Top organisations (by high/medium contract records, parents joined)

| # | organisation | h/m records | website | AP |
|---|---|---|---|---|
{top_rows}

## Known gaps / blockers
- Sites answering 403/503 or a bot challenge were skipped and never retried around the block ({len(blocked_u)} crawl sites): {', '.join(blocked_u[:90])}{' …' if len(blocked_u) > 90 else ''}.
- Targeted pages that were blocked / disallowed (skipped): {', '.join(probe_blocked)}.
- Provincial governments without a central supplier-invoice mailbox on their own pages: Government of Alberta (1GX / SAP Business Network only), Government of Ontario (invoice to the ministry client; OPS Service Centre for vendor assistance), Manitoba (paying department), BC, Nova Scotia and Saskatchewan (no central AP page found in the time budget — BC's invoice.pss.gov.bc.ca mailbox is for PSS customers' receivables and was not used). Yukon's invoice pages (yukon.ca/en/invoice-government, Departmental Accounts Payable contact list) answered 403 and were skipped.
- City of Ottawa's AP page (ottawa.ca) answered with a bot challenge; the Accounts Payable vendor-master mailbox from the City's EFT form (documents.ottawa.ca) is recorded instead.
- Multi-government buyer keys (`extras.jurisdiction_candidates`) are not resolved to one organisation by design.
- Non-North-American buyers (UNDP offices, EU institutions, Nordic/Dutch/Spanish/Latin American bodies) received websites from the notice/alias/Wikidata and crawler results only.
- Text excerpts in `invoicing_requirements` that start with "[page excerpt]" are raw page text around the first invoice mention; curated entries are written summaries of the cited page.
"""
open(NOTE, 'w').write(md)
print('note written', NOTE, len(md))
