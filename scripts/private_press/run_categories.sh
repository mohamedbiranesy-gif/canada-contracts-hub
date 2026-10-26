#!/bin/bash
# Wait for round-2 company crawl to finish, then crawl sector category listings (back to 2024), prefilter and fetch.
cd scripts/private_press
while pgrep -f "crawl_search.py companies" > /dev/null; do sleep 30; done
python3 -I crawl_search.py categories categories.txt > downloads/private_press/crawl_categories.out 2>&1
while pgrep -f "fetch_releases.py downloads/private_press/candidates_company_filtered.jsonl" > /dev/null; do sleep 30; done
python3 -I prefilter_candidates.py downloads/private_press/candidates_search.jsonl downloads/private_press/candidates_cat_filtered.jsonl > downloads/private_press/prefilter_cat.out 2>&1
python3 -I fetch_releases.py downloads/private_press/candidates_cat_filtered.jsonl fetched_search.jsonl > downloads/private_press/fetch_cat.out 2>&1
echo CAT_DONE >> downloads/private_press/fetch_cat.out
