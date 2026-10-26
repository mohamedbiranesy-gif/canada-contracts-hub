#!/bin/bash
cd scripts/private_press
while pgrep -f "crawl_search.py companies" > /dev/null; do sleep 20; done
python3 -I prefilter_candidates.py downloads/private_press/candidates_search.jsonl downloads/private_press/candidates_company_filtered.jsonl > downloads/private_press/prefilter.out 2>&1
python3 -I fetch_releases.py downloads/private_press/candidates_company_filtered.jsonl fetched_search.jsonl > downloads/private_press/fetch_company.out 2>&1
