#!/bin/bash
# Round 2: crawl verified company slugs, prefilter to likely contract titles, fetch releases.
cd scripts/private_press
python3 -I crawl_search.py companies company_slugs_round2.txt > downloads/private_press/crawl_companies2.out 2>&1
python3 -I prefilter_candidates.py downloads/private_press/candidates_search.jsonl downloads/private_press/candidates_company_filtered.jsonl > downloads/private_press/prefilter.out 2>&1
python3 -I fetch_releases.py downloads/private_press/candidates_company_filtered.jsonl fetched_search.jsonl > downloads/private_press/fetch_company.out 2>&1
echo ROUND2_DONE >> downloads/private_press/fetch_company.out
