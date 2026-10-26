"""Write notes/enrichment_buyers_deep.md from the assembled output + work files (re-run after each assembly)."""
import sys, os, json, glob, collections, urllib.parse
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from common import *

buyers = {b['buyer_key']: b for b in load_buyers()}
out = [json.loads(l) for l in open(OUT_ENRICHED)]
st = json.load(open(WORK + '/assemble_stats.json'))
manual = [json.loads(l) for l in open(WORK + '/manual_ap.jsonl')] if os.path.exists(WORK + '/manual_ap.jsonl') else []
probes = [json.loads(l) for l in open(WORK + '/probe_log.jsonl')]
G = json.load(open(WORK + '/groups.json'))
prec = json.load(open(WORK + '/precision_check.json')) if os.path.exists(WORK + '/precision_check.json') else None

ap_deep_total = sum(1 for b in buyers.values() if b['_task'] == 'ap_deep')
ap_deep_records = sum(b['record_count'] for b in buyers.values() if b['_task'] == 'ap_deep')
cnt = collections.Counter(); rec = collections.Counter()
orgs_ap = set(); orgs_any = set()
for r in out:
    b = buyers[r['buyer_key']]; nf = set(r['extras']['deep_pass']['new_fields']); task = b['_task']
    ap = r['ap_contact']
    for f in sorted(nf):
        cnt[(task, f)] += 1; rec[(task, f)] += b['record_count']
    if task == 'ap_deep':
        if 'ap_contact.emails' in nf or 'ap_contact.invoice_portal' in nf:
            cnt['ap_deep_gain_ap'] += 1; rec['ap_deep_gain_ap'] += b['record_count']; orgs_ap.add(r['extras']['deep_pass']['group'])
        if 'ap_contact.emails' in nf or 'ap_contact.invoice_portal' in nf or 'ap_contact.invoicing_requirements' in nf or 'ap_contact.phone' in nf or 'ap_contact.mailing_address' in nf:
            cnt['ap_deep_gain_ap_any'] += 1; rec['ap_deep_gain_ap_any'] += b['record_count']
        orgs_any.add(r['extras']['deep_pass']['group'])
    else:
        for f, c in [('website', r['official_website']), ('ap_email', ap['emails']), ('invoice_portal', ap['invoice_portal']), ('invoicing_requirements', ap['invoicing_requirements']),
                     ('procurement_email', r['procurement_contact']['emails']), ('procurement_url', r['procurement_contact'].get('url')), ('general_email', r['general_contact']['emails']),
                     ('general_phone', r['general_contact'].get('phone')), ('address_line1', (r['address'] or {}).get('line1')), ('address_any', (r['address'] or {}).get('city') or (r['address'] or {}).get('region')),
                     ('identifiers_directory', any(x != 'from_dataset' for x in r['identifiers']))]:
            if c:
                cnt[('new', f)] += 1; rec[('new', f)] += b['record_count']

L = []
L.append('# Buyer deep AP / invoicing search (W3) — buyers_deep.jsonl\n')
L.append('Generated %s by `scripts/enrichment_buyers_deep/notes_deep.py` after `assemble_deep.py` (assembled %s). Output: `enrichment/v2/buyers_deep.jsonl` — one line per buyer_key with something new: '
         'for `ap_deep` buyers the FULL merged record (the previous record from `enrichment/buyers_enriched.jsonl` / `enrichment/v2/buyers_enriched_v2.jsonl`, which holds the `_known` facts, plus this pass\'s findings), '
         'for the 104 `full_enrichment_new_buyer` keys a full record (always written). Same layout as `buyers_enriched.jsonl`; `extras.deep_pass` lists `new_fields` and `sources` for every line, '
         '`extras.ap_inherited_from` marks facts taken from a parent organisation. Pipeline: `scripts/enrichment_buyers_deep/` (copies of the v2 scripts + new `groups.py`, `deep3.py`, `deep4.py`, `newbuyers.py`, `assemble_deep.py`, `notes_deep.py`); earlier scripts and outputs untouched. Work files: `enrichment/work_buyers_deep/`; raw copies of targeted pages: `downloads/enrichment_buyers_deep/pages/`.\n' % (now(), st.get('assembled_at')))
L.append('## Coverage\n')
L.append('Input: %d `ap_deep` buyers (%d contract records) with no AP mailbox and no invoice portal, %d new buyers (%d records). Grouped into %d organisations (`groups.py`: canonical name from the previous enrichment, explicit merge rules for historical CSSS/CISSS names, union of keys sharing the same official website URL when the names are compatible, e.g. "Halifax Transit (Halifax Regional Municipality)" → HRM, "Newfoundland Labrador Hydro" → NL Hydro); every finding is applied to all keys of its organisation.\n'
         % (ap_deep_total, ap_deep_records, len(buyers) - ap_deep_total, sum(b['record_count'] for b in buyers.values() if b['_task'] != 'ap_deep'), len(G)))
L.append('| result (ap_deep buyers) | buyer keys | contract records |\n|---|---|---|')
L.append('| gained an AP mailbox or invoice portal | %d | %d |' % (cnt['ap_deep_gain_ap'], rec['ap_deep_gain_ap']))
L.append('| gained any AP fact (mailbox, portal, AP phone, invoice mailing address or invoicing requirements) | %d | %d |' % (cnt['ap_deep_gain_ap_any'], rec['ap_deep_gain_ap_any']))
L.append('| lines written (any new fact) | %d | %d |\n' % (sum(1 for r in out if buyers[r['buyer_key']]['_task'] == 'ap_deep'), sum(buyers[r['buyer_key']]['record_count'] for r in out if buyers[r['buyer_key']]['_task'] == 'ap_deep')))
L.append('Organisations (groups) gaining an AP mailbox/portal: %d.\n' % len(orgs_ap))
L.append('New facts per field, ap_deep buyers (buyer keys / contract records):\n')
L.append('| field | keys | records |\n|---|---|---|')
for k in sorted([k for k in cnt if isinstance(k, tuple) and k[0] == 'ap_deep'], key=lambda k: -cnt[k]):
    L.append('| %s | %d | %d |' % (k[1], cnt[k], rec[k]))
L.append('\nNew buyers (104, full enrichment) — fill counts (buyer keys / records):\n')
L.append('| field | keys | records |\n|---|---|---|')
for k in sorted([k for k in cnt if isinstance(k, tuple) and k[0] == 'new'], key=lambda k: -cnt[k]):
    L.append('| %s | %d | %d |' % (k[1], cnt[k], rec[k]))
L.append('')
# sources
L.append('## Methods and sources\n')
crawl_files = sorted(glob.glob(WORK + '/deep*.jsonl'))
cs = collections.Counter(); pages = 0
for f in crawl_files:
    for l in open(f):
        r = json.loads(l); cs[(os.path.basename(f), r.get('status'))] += 1; pages += len(r.get('pages', []))
L.append('1. **Automated crawler passes** (UA `contracts-research/1.0 (public-procurement dataset enrichment; polite crawler)`, robots.txt honoured, one queue per host, 0.7 s spacing ≈ 1.4 req/s, a 403/429/503 or bot-challenge page stops the site and is never retried around):')
L.append('   - `deep2.py` (sitemap-ranked French/English invoicing keywords, ≤16 pages + linked PDFs) over the own websites of all groups with ≥15 records (1,066 sites);')
L.append('   - `deep3.py` (best-first walk through supplier / finance / procurement / contact sections, depth ≤3, ≤45 HTML + ≤14 PDFs, also records phone numbers printed next to an accounts-payable heading) over the 550 largest sites (`deep3.jsonl`), over 89 websites newly mapped for groups that had none (`deep3b.jsonl`, CEGEPs, museums, agencies, NS/ON/SK bodies; a website is asserted only when its homepage loaded and the title/domain carries a distinctive token of the name) and over 88 candidate websites of the new buyers (`deep3c.jsonl`);')
L.append('   - `deep4.py` (sitemap scan for Canada Post labour-disruption notices 2024–2025 — municipalities listed the e-mail suppliers should use for invoices while mail was suspended — and invoicing / direct-deposit / PO-terms URLs not opened before).')
L.append('   Run statistics (file, status: sites): ' + ', '.join('%s %s: %d' % (f, s, n) for (f, s), n in sorted(cs.items())) + '; pages/PDFs fetched by these passes: %d.' % pages)
L.append('2. **Targeted research** (WebSearch in French/English to locate candidate pages — mostly ineffective for French-language Quebec pages, as noted in v1 — then the page itself fetched with `probe.py`, raw copy saved; `add_manual.py` refuses an e-mail that is not in the fetched copy of the cited URL). %d fetches logged in `enrichment/work_buyers_deep/probe_log.jsonl`; %d curated findings in `enrichment/work_buyers_deep/manual_ap.jsonl`:' % (len(probes), len(manual)))
for m in manual:
    mt = m['match']
    who = mt.get('group') or ','.join(mt.get('groups', [])) or mt.get('parent_key') or mt.get('name_regex') or ','.join(mt.get('buyer_keys', []))
    L.append('   - `%s` — %s (retrieved %s): AP %s%s%s%s' % (who, m['url'], m.get('retrieved_at'), ', '.join(m.get('ap_emails', [])) or '—',
                                                     ('; portal: ' + m['invoice_portal']) if m.get('invoice_portal') else '',
                                                     ('; procurement: ' + ', '.join(m.get('proc_emails', []))) if m.get('proc_emails') else '',
                                                     ('; basis: ' + m.get('basis', 'own') + (' (' + m.get('parent_name', '') + ')' if m.get('parent_name') else '')) if m.get('basis', 'own') != 'own' else ''))
L.append('3. **Parent-organisation inheritance**: central supplier-payment facts of a government apply to its departments only where the government publishes them for all ministries — Government of Saskatchewan (Provincial Comptroller direct-deposit form M221: applies to all ministries; `mhd@gov.sk.ca` is the remittance/direct-deposit box, invoices go to the ordering ministry) → 33 SK ministry keys; Province of Nova Scotia (Service Nova Scotia vendor master, EFT form) → 27 NS department keys. Multi-government bare names ("Infrastructure", "Education", …) get the facts inside their `extras.jurisdiction_candidates` entries only.')
L.append('4. **New buyers** (`newbuyers.py`): same organisation already enriched under another key (normalized name) → facts copied with `extras.same_organisation_as`; CRA registered-charity list (downloads/cra_charities/ident_2024.csv + weburl_2024.csv, T3010 open data 2024, downloaded by the vendor worker 2026-10-26T02:46Z) → BN (RR account), registered address (exact normalized operating/legal name, province must agree; a charity whose operating name differs from the legal name — e.g. "CITY OF SURREY" operating as Surrey Public Library — is NOT used); candidate official websites crawled and asserted only when verified; locations as published in the notices.\n')
L.append('## E-mail rules (unchanged from v1/v2, precision over recall)')
L.append('- Only role mailboxes copied from the organisation\'s own pages/documents, each with page URL + retrieval time + snippet in `*.evidence` (`source` says crawler or targeted). No personal mailboxes (first.last, initial+surname, names; personal contacts listed next to role boxes on finance pages were ignored), no pattern-constructed addresses, no decoding of Cloudflare-protected addresses (TDSB, NS Public Works contact page).')
L.append('- Crawler e-mails must be on the organisation\'s own domain (or the page\'s domain / a jurisdiction-consistent government domain); receivable/billing/tax/customer boxes are never AP (new in this pass: `recevoir`, `cashmgmt`, `revenue` tokens); a mailbox whose AP signal comes only from "payment/paiement" needs supplier/invoice context; an `ap_context` box (finance/comptabilité/fournisseurs) is AP only on an invoice/payables/direct-deposit page or next to "send invoices to" wording.')
L.append('- Supplier-payment boxes that are not invoice-submission addresses (vendor master / EFT / direct-deposit / remittance boxes: Halifax hrmaplink, Winnipeg FIN-EFT-Advice, Saskatchewan mhd, Nova Scotia GAAccountingServices) are kept in `ap_contact.emails` with the wording of the source in `invoicing_requirements`/`notes`, as in v2.\n')
if prec:
    L.append('## Precision check (AP findings re-read on the evidence page)\n')
    L.append(prec.get('summary', ''))
    for x in prec.get('items', []):
        L.append('- %s | %s | %s | %s' % (x.get('verdict'), x.get('email'), x.get('org'), x.get('url')))
    L.append('')
L.append('## Blockers and gaps\n')
blocked = sorted({p['url'] for p in probes if p.get('blocked')})
L.append('- Targeted pages that answered 403 / bot challenge (skipped, never retried around): ' + ', '.join(blocked[:60]) + ('' if len(blocked) <= 60 else ' …'))
bl = sorted({json.loads(l)['site'] for f in crawl_files for l in open(f) if json.loads(l).get('status') in ('blocked_or_challenged', 'partially_blocked')})
L.append('- Crawler sites that answered with a block/challenge (%d): %s' % (len(bl), ', '.join(bl[:80]) + (' …' if len(bl) > 80 else '')))
L.append('- Sites blocked in earlier passes were not crawled again (e.g. transports.gouv.qc.ca, revenuquebec.ca, saaq.gouv.qc.ca, laval.ca, terrebonne.ca, justice.gouv.qc.ca, santequebec.ca, yukon.ca, princeedwardisland.ca, vaughan.ca, guelph.ca, burlington.ca).')
L.append('- bids&tenders / MERX / SEAO tender documents require supplier registration or a paid account: not downloaded (registration-gated, not "publicly downloadable"), even where a direct document link exists.')
L.append('- Most Quebec public bodies (ministries, CIUSSS/CISSS, cities, school service centres) publish no supplier-invoicing mailbox on their public sites; invoicing instructions are in contract/PO documents distributed through SEAO. Santé Québec has no central supplier-invoicing page reachable (santequebec.ca answers 403). The Quebec government supplier direct-deposit form formerly at cdn-contenu.quebec.ca (FO_adhesion_depotdirect.pdf) now answers 404.')
L.append('- Government of British Columbia: no central supplier-invoice or vendor-master mailbox found (FIN 312 direct-deposit form has none; the forests invoice page is disallowed by robots.txt); BC ministry keys keep their previous facts.')
L.append('- WebSearch returned mostly job ads / unrelated pages for French queries; English queries worked better for English-language organisations.')
open(NOTE, 'w').write('\n'.join(L) + '\n')
print('wrote', NOTE, len(L), 'lines')
