# ChatGPT agent mode — buyers' invoicing contacts (lane `chatgpt`)

Paste into ChatGPT with Agent mode on. Replace NN with your batch number from coord/NEXT.md.

You are ChatGPT, lead of lane `chatgpt` on a three-AI team.
- Repo: https://github.com/REPO_OWNER/canada-contracts-hub
- Read `AGENTS.md` there first; it is binding.
- Then open `coord/tasks/chatgpt/chatgpt_buyer_ap_batchNN.csv`.

For each buyer in the batch:
1. **Find the official page that gives its accounts-payable / invoicing e-mail or invoice portal.** Good places to look:
   - supplier guides;
   - "doing business with us" pages;
   - purchase-order terms PDFs;
   - finance department pages;
   - the parent government's central AP page.
2. **Copy the evidence.** Take the exact value, the page URL, today's date, and a quote of at most 300 characters
   containing the value.
3. **Never** give a named person's address, guess an address, or get around a CAPTCHA or login. Record `blocked` or
   `not_published` (with the queries you tried) instead.

Output one CSV file named `chatgpt_buyer_ap_results_batchNN.csv` with exactly this header:
```
task_id,buyer_key,org_name_as_found,ap_email,ap_email_type,invoice_portal_url,ap_phone,invoice_mailing_address,invoicing_requirements_summary,applies_to,evidence_url,evidence_quote,retrieved_date,status,queries_tried,notes
```
Allowed values:
- `ap_email_type`: invoice_submission | accounts_payable | supplier_payment | procurement | general.
- `applies_to`: whole_organisation | this_unit_only | parent_central_ap.
- `status`: found | portal_only | not_published | blocked | unclear.

Delivery: upload the CSV to the repo folder `data/incoming/chatgpt/` (GitHub → Add file → Upload files → Commit).
The verifier checks every row automatically.
