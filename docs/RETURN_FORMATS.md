# Return formats (CSV, UTF-8, comma-separated, header row exactly as below)

File names: `<ai>_<task>_results_batchNN.csv`, matching the task batch you worked on, e.g. `gemini_buyer_ap_results_batch01.csv`, `chatgpt_vendor_contacts_results_batch03.csv`, `chatgpt_qa_results_batch01.csv`, `gemini_source_scouting_01.csv`. Save every result file into the team room's `RESULTS/` folder (or your Downloads folder). One row per task row you worked on, including rows you could not resolve: give them a `status` so they are not re-assigned.

## 1. Buyer AP / invoicing — `*_buyer_ap_results_*.csv`
```
task_id,buyer_key,org_name_as_found,ap_email,ap_email_type,invoice_portal_url,ap_phone,invoice_mailing_address,invoicing_requirements_summary,applies_to,evidence_url,evidence_quote,retrieved_date,status,queries_tried,notes
```
- `ap_email_type`: `invoice_submission` | `accounts_payable` | `supplier_payment` | `procurement` | `general`. Use the most specific type the page supports.
- `applies_to`: `whole_organisation` | `this_unit_only` | `parent_central_ap` (the parent's page says it covers this unit).
- `evidence_quote`: ≤ 300 characters copied from the page, containing the e-mail or portal.
- `retrieved_date`: YYYY-MM-DD.
- `status`: `found` | `portal_only` | `not_published` | `blocked` | `unclear`.
- Several mailboxes for one organisation: one row per mailbox, same `task_id`.

## 2. Vendor contact — `*_vendor_contact_results_*.csv`
```
task_id,vendor_key,official_website,website_verification,general_email,billing_or_ar_email,main_phone,address_on_site,business_number_if_published,other_identifiers,evidence_url,evidence_quote,retrieved_date,status,notes
```
- `website_verification`: what on the site proves it is this vendor — e.g. "legal name + 123 Main St, Laval QC H7L 5A7 on Contact page".
- `general_email` / `billing_or_ar_email`: role mailboxes on the vendor's own domain only.
- `main_phone`: the organisation's main line.
- `status`: `found` | `website_only` | `not_found` | `blocked` | `ambiguous` (several companies share the name — explain in notes).

## 3. QA verification — `chatgpt_qa_results_*.csv`
```
qa_id,record_id,link_opened,buyer_match,vendor_match,title_match,value_match,dates_match,status_supported,correct_values_if_mismatch,notes
```
- `*_match`: `yes` | `no` | `not_shown`.
- `status_supported`: `yes` | `no` | `unclear` — does the page support the contract being ongoing on 2026-10-25, given `status_basis`?
- `link_opened`: `yes` | `no_404` | `blocked` | `login_required`.

## 4. Source scouting — `*_source_scouting_*.csv`
```
source_name,publisher,url,coverage,data_access,supplier_location_field,award_or_start_date_field,end_date_or_term_field,approx_volume,login_required,bot_protection,already_in_covered_sources,how_to_pull,notes
```
- `data_access`: `bulk_file` | `api` | `html_list` | `pdf_reports`.
- `supplier_location_field`: field name, or `none` (rows without one are of little use).
- `how_to_pull`: concrete URL/endpoint/parameters.
