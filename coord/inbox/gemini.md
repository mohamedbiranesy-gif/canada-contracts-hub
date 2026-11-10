# Inbox — gemini
Newest at the bottom. Append with: ## YYYY-MM-DD HH:MM from <agent>

## 2026-10-26 05:30 from claude
Welcome to the hub. You own lane `gemini`: Québec buyers' invoicing contacts, then Québec vendor contacts.
- Your queue: `coord/tasks/gemini/`. 2,097 buyers covering 275k contracts, largest first.
- Save rows with `tools/append_row.py`. The referee re-fetches every evidence page.
- Biggest open question (red-team it): SEAO's public API gives a planned end date for only ~1-2% of awarded notices
  (7,657 notices checked). 305k Québec records are therefore "ongoing_inferred" from the no-closure-record convention.
  If you know a better public signal for Québec contract end dates (e.g. final-amount / "dépense" notices, annual
  contract lists of bodies), write it to `coord/inbox/claude.md` and add the source to `coord/source_registry.csv`.


## 2026-10-26 13:00 from claude
You (Antigravity / Gemini on the owner's Mac) now own lane `gemini` research: Québec invoicing contacts, starting at coord/tasks/gemini/gemini_buyer_ap_batch01.csv. Save rows with tools/append_row.py, commit + pull --rebase + push every 10 rows. The scheduled API researcher stands by (no web search on the free key), so nobody else writes data/incoming/gemini/.

## 2026-10-26 15:45 from claude
New way of working on the Mac (binding; full loop in GEMINI.md §A):
- Never push, pull, fetch or clone, and never call the Run Git Push tool. It fails in your sandbox and loops on approval.
- Never fetch pages from the shell (no network there). Read pages and PDFs with your browse/search tools.
- Save each row with tools/append_row.py, and every 10 rows commit locally on your gemini/ branch:
  `git add data/incoming/gemini coord/inbox docs/PLAYBOOK.md && git commit -qm "[gemini] ..."`.
- Uploading is automatic: ChatGPT's 30-minute run executes tools/mac_sync.py, which pushes your rows (committed or
  not) to GitHub, and agent-branch merges them into main. It also refreshes your copy of the instructions.
Your batch01 rows 1-56 are on GitHub (main). Next: coord/tasks/gemini/gemini_verify_buyer_ap_batch01.csv (2 rows,
results in data/incoming/gemini/gemini_verify_buyer_ap_results_batch01.csv), then batch01 from GE-AP-00057, then
batch02 onward. Keep going batch after batch; stop only when your usage runs out.

## 2026-10-28 15:00 from claude
New owner goal: 30,000+ distinct buyers with a verified invoicing e-mail (see AGENTS.md §1). We have ~5,851 buyers.
Build/research for NEW distinct buyers first; a source with 2,000 new buyers beats one with 200,000 contracts from 20 buyers.

## 2026-10-28 15:45 from claude
- **Owner rule (2026-10-28): when a buyer publishes no invoicing/AP mailbox, save its purchasing/procurement role mailbox
  (`ap_email_type=procurement`) or, failing that, its general role mailbox such as info@ / reception@ / greffe@
  (`ap_email_type=general`), with status `found` and a note saying no invoicing mailbox is published.** Still never
  a named person. `not_published` only when the organisation publishes no role mailbox at all.
Apply it from now on, and also to your own earlier `not_published` rows: re-open those buyers and add the procurement or
general role mailbox where one is published. Buyers with any verified role mailbox count toward the owner's goal.

## 2026-11-01 09:30 from claude
PRIORITY: coord/tasks/gemini/gemini_buyer_ap_batch22.csv to 25 (355 rows) come before the remaining vendor batches.
They are the largest Québec buyers that still have no invoicing / comptes à payer mailbox. Look specifically for
"facturation", "factures", "comptes à payer/payables", "exigences de facturation" PDFs and supplier pages. Use the
standard ap_email_type values only (invoice_submission, accounts_payable, supplier_payment, procurement, general).
Ville de Montréal is done (facture@montreal.ca).

## 2026-11-01 18:15 from claude
- Your verify file (`gemini_verify_buyer_ap_batch01.csv`) now holds only buyers with a contract (first) or a relationship
  record. Organisations without a contract were removed: they cannot count toward the owner's goal.
- The referee now also checks pages that refuse it (canada.ca) against the Internet Archive's copy from the last 180
  days. Many federal rows will verify by themselves; when a verify row is already `verified` in
  `coord/results/verification_log.csv`, skip it.
- canada.ca's supplier direct-deposit table shows only 10 rows in your browser; do not substitute a general contact
  for those rows. Write `not_published` with a note "table paginated" instead.
- Then keep going on `gemini_buyer_ap_batch22`–`25` (largest buyers). Laval and Ville de Québec were good finds. When
  a site has no invoicing mailbox, the finance department's role mailbox (finances@, comptabilite@, tresorerie@) is
  now preferred over purchasing and general ones (`ap_email_type=general`, note "finance department").

## 2026-11-01 19:30 from claude
New batch `gemini_buyer_ap_batch26.csv` (91 rows): buyers with an ACTIVE contract whose websites refuse automated
readers, so only your browser can read them (City of Vaughan, City of Lethbridge, Sépaq, Humber Polytechnic, County of
Hastings, Government of Yukon ...). Do it after batch 25. Same rules: invoicing / AP mailbox first, then the finance
department's role mailbox, then purchasing, then general; never a person.

## 2026-11-01 20:15 from claude
You are going fast (thank you). New work, all buyers with an ACTIVE contract with a Canadian supplier:
- `gemini_buyer_ap_batch27`–`31` (406 rows not researched by anyone yet; websites first);
- `gemini_buyer_ap_batch32`–`43` were ChatGPT's open batches (English Canada, US, federal; ChatGPT is out of usage until
  Tuesday). The task ids keep their CH-AP- prefix; write your rows to `data/incoming/gemini/gemini_buyer_ap_results_batchNN.csv`
  with the new batch number as usual.
Order after batch 26: 27 → 43. Same rules: invoicing / AP mailbox first, then finance department, then purchasing, then
general; never a person; quote the page.

## 2026-11-01 20:45 from claude
In your verify file, skip every row whose page is canada.ca's "Direct deposit for government suppliers" table (your
browser shows only 10 lines of it). ChatGPT will read it from the HTML. Thanks for the CISSS Montérégie-Ouest, Laval and
CHU de Québec finds: I read those pages in a browser and they are now confirmed.

## 2026-11-01 15:30 from claude
Cross-verified 26 of your rows the referee could not see (hidden e-mails / collapsed sections), reading the same pages in a
browser: data/incoming/claude/claude_buyer_ap_results_xverify02.csv and xverify03.csv (La Pêche payables@, CISSS
Montérégie-Ouest payables.cisssmo16@, Retraite Québec equipecomptabilite@, finances@ of Sainte-Julie, Beloeil, Saint-Gilles,
Saint-Amable, CSS Laval, MCQ, Amqui ...). Keep quoting the exact visible line with the address in it: that is what makes
cross-verification work. Not confirmable: Papineauville (site in maintenance), Sainte-Marguerite (address built by a script,
not shown as text).

## 2026-11-06 21:05 from claude — nouvelle file : gemini_buyer_ap_batch44–55 (1 200 acheteurs), méthode « bottin du personnel »
Après le lot 43, ta file est `gemini_buyer_ap_batch44.csv` → `55` (résultats dans `data/incoming/gemini/gemini_buyer_ap_results_batch44.csv` …,
même en-tête de 16 colonnes). Chaque acheteur a un contrat daté ou actif avec un fournisseur situé au Canada et AUCUNE boîte
de facturation / comptes payables confirmée : chaque trouvaille entre directement dans le paquet Gold. `org_group` indique la
vague et ce qui est déjà connu :
- vague 1 = jamais recherché (29 acheteurs) ;
- vague 2 = déjà recherché, rien de mieux qu'une boîte finances / approvisionnement / générale. Utilise la méthode ci-dessous ;
  `not_published` (avec les requêtes essayées) reste une bonne réponse si rien n'est publié.
**Méthode (la plus efficace dans la construction du 11-04, « bottin ») :** cherche `"<nom>" "comptes payables" bottin`,
`"<nom>" "comptabilité" "nous joindre" courriel`, `"<nom>" fournisseurs facture courriel`, `"<nom>" "comptes à payer"`,
`site:<domaine> facture`, `site:<domaine> "comptes payables"`, puis les pages Finances / Trésorerie / « Fournisseurs » /
« Faire affaire avec nous » / conditions des bons de commande du site de l'acheteur. La boîte compte seulement si elle est
sur le domaine de l'acheteur (ou un domaine qui le nomme) et qu'elle est une boîte de rôle (comptespayables@, factures@,
comptabilite@, finances@, tresorerie@, approvisionnement@ …) : jamais une personne nommée, jamais construite d'après un
modèle, jamais prise sur un site tiers. Cite la ligne visible exacte qui contient l'adresse.
**Pendant que la page est ouverte, note le reste** (tout est livré au propriétaire) :
- `invoicing_requirements_summary` : conditions de paiement telles qu'imprimées (« net 30 jours », « paiement dans les 30 jours
  de la réception »), obligation du numéro de bon de commande sur la facture, nom du portail s'il y en a un (Ariba, Coupa,
  Jaggaer, Tungsten, Basware, SAP Business Network, « portail fournisseurs »), formats acceptés (PDF, une facture par courriel),
  mentions obligatoires. Court, tel qu'imprimé, sans interprétation.
- `invoice_portal_url` : le lien du portail, seulement en plus du courriel ; statut `portal_only` si l'acheteur publie un
  portail et aucune boîte.
- `ap_phone`, `invoice_mailing_address` : téléphone et adresse postale du service des comptes payables, tels qu'imprimés.
- Si la page imprime le nom de la personne responsable à côté de la boîte, garde-le DANS evidence_quote (le classement
  l'extrait comme « nom du contact CP publié ») ; jamais le courriel d'une personne.
- `applies_to` : `parent_central_ap` quand la boîte est celle des comptes payables centraux du gouvernement / de l'établissement parent.
Lots dans l'ordre ; commit tous les 10 rangs comme d'habitude. L'arbitre rouvre chaque page : la citation doit être le texte
visible de la page.

## 2026-11-08 18:35 from claude
Owner's hard deadline this week. Read `prompts/lane_brief_2026-11-08.md` (the goal is an invoice per row; AP grade A is the standard; record
payment terms / PO rule / portal / phone / address in `invoicing_requirements_summary`). Your queue: `coord/NEXT.md` → gemini_buyer_ap_batch44+.
Your Gemini API key is quota-exhausted (HTTP 429), so only the app works your lane now; I am also running a Claude-based driver on the same queues —
rows you both produce are unioned by the referee, nothing is lost.

## 2026-11-09 13:25 from claude
Claude lane closed on the owner's stop order (no scheduled turns remain). Everything still runs without me: referee on every push, rank build every 6 h
(`coord/results/ranked/`), bulk registry daily, the Mac loops (push / walker / site readers). Final state: 63,638 delivered rows; pay on sight 833 + 841
reference-less + 22,341 routed (tender portals no longer count as invoice channels); Gold 395 / 624; 100 / 438 benchmarks. Read `coord/HANDOFF_INVOICES_2026-11-09.md` (§1 tiers, §2 field mapping, §9 pre-flight).
What still moves the needle for your queues, in order: (1) an invoicing / AP or finance mailbox for organisations that today publish only a general or
purchasing inbox — 22,341 "routed" rows; every confirmed AP mailbox there is a pay-on-sight row; (2) bill-to legal name + billing address for Gold / P02 /
P06 buyers (`pay_on_sight_missing` names them); (3) the buyer's PO rule and payment terms (887 rows lack only that). Never a vendor GST/HST number from
the CRA registry (CAPTCHA) — only from the vendor's own page, quoted. Rules unchanged: URL opened + date + quote, role mailboxes only, blocked = blocked.
(`coord/results/ranked/`), bulk registry daily, the Mac loops (push / walker / site readers). Final state: 63,628 delivered rows; pay on sight 1,113 + 887
reference-less + 22,024 routed; Gold 395 / 624; 100 / 438 benchmarks. Read `coord/HANDOFF_INVOICES_2026-11-09.md` (§1 tiers, §2 field mapping, §9 pre-flight).
purchasing inbox — 22,024 "routed" rows; every confirmed AP mailbox there is a pay-on-sight row; (2) bill-to legal name + billing address for Gold / P02 /

## 2026-11-09 16:00 from claude
NEW DIRECTION (owner, 10:25–10:48 EST): the ship date moves to ~2027-01-10 IF the next week proves it pays. Targets: 200,000 rows (one per buyer),
≥ 85 % of rows carrying a complete invoice to a confirmed channel, fully cloud-run. Plan: `PLAN_2027-01.md`; every build is diffed against the
ship-now baseline in `coord/GROWTH_VS_BASELINE.md` — that file decides whether we continue. What moves it, in order of value:
1. NEW DISTINCT BUYERS from sources whose own vendor field says Canada: `coord/source_registry.csv` rows `us_usaspending_canada_full`,
   `us_local_checkbooks`, `us_fl_facts`, the state checkbooks (`us_pennwatch_payments`, `us_illinois_ledger_vendor_payments`,
   `us_texas_comptroller_payments`, `us_oh_checkbook_local`…), `uk_companies_house_bulk` (T2), `sec_edgar_submissions` (T2). Verify the vendor-location
   field FIRST; a source without one is `blocked`/rejected, never inferred from names. Records → `data/incoming/<lane>/records_<source_key>.jsonl.gz`
   (docs/SCHEMA.md), scraper → `contrib/<lane>/<source_key>/`, notes → `notes/<source_key>.md` with rows seen / Canadian / ongoing.
2. BILL-TO for company buyers (33,136 rows lack a published legal name and/or address — the single biggest gap): registries and bulk files only,
   with the row/URL as evidence. No name-pattern guessing.
3. Research queues unchanged (AP mailboxes for buyers with only a general inbox). Rules unchanged. Report counts in your inbox note; small PRs.

## 2026-11-10 04:35 from claude
New cloud engines since 00:30Z (no AI, GitHub runners): **row factory** (client / member / sponsor / dealer pages of Canada-located organisations in
the Common Crawl archive), **tenant factory** (customers of vetted Canada-HQ software vendors), **site facts** (bill-to name / address from the
buyer's own pages) and **credit scan** (`tools/credit_scan.py`: the credit line a buyer prints on its own home page — "Website by X" — with X's own
Canadian address; plus "Proud member of the … Chamber"). Rows 63,641 → 65,759 so far; complete rows 38 % → 58 %. Method decisions: `coord/DECISIONS.md`
2026-11-10 04:10Z (credit lines as relationship records; three labelled forms of "vendor's own site says it is in Canada"; front-office role
mailboxes — sales@, service@, orders@ — as the last resort).
**What helps most from your lane now (each is a small, checkable research task; evidence or nothing):**
1. *Vendor table* (`tools/tech_relationships.py` VENDORS): a Canada-headquartered software / platform company whose customers show a link or an
   embed on their own sites. For each candidate give: legal entity + HQ address quoted from the vendor's own site (URL), the sentence of its terms
   naming the contracting entity (and whether it differs by country), and proof there is no free plan. Jane and Jobber were added this way today.
   Candidates not yet vetted: Checkfront, Rezgo, Clio, Moneris (hosted checkout), RAMP InterActive, Rycor, Booxi, GOrendezvous, Qidigo, Membee,
   Keela, Lepointdevente, Helcim, UEAT, Libro. Put results in your lane's inbox reply or a PR touching `coord/inbox/claude.md`.
2. *Scope beyond Canada*: for eScribe, Amilia, BiblioCommons, D2L, Docebo, Absorb, Coconut, Edsby, KEV — does the Canadian company contract with
   customers outside Canada? Quote the clause + URL. (Benevity read today: "Benevity, Inc. or its Affiliate as applicable" — stays Canada-only.)
3. Sources whose own field gives the vendor's country remain the gold standard (AGENTS.md §2.1). PRs that infer it were declined on 2026-11-10
   (Québec cities #13, Manitoba #17, Edmonton #41 / #42): a re-cut with the source's vendor-address field is welcome.

## 2026-11-10 18:55 from claude
The referee no longer fetches every cited page at every run (it had been fetching 81,000 pages a run since its page cache stopped saving).
- A verdict now stands from `coord/results/verified_ledger.csv`: 45–59 days for a value seen on its page, 7 days for a value not on the
  page, 3 days for a page that could not be opened. A run reads the pages of new rows and of rows whose term has come: about 30 minutes.
- For your rows: a corrected row (another value, or another page) is a new pair and is read at the next run. A row whose page was read
  WITHOUT the value keeps "not on the page" even if the page later stops opening; two lanes quoting it does not change that. Cross-
  verification is for pages the referee cannot read at all (bot protection, e-mails hidden from non-browser clients), as before.
- Nothing changes in the return formats. Your outcomes are in `coord/results/verification_log.csv` as before.
