#!/bin/bash
cd scripts/private_press
while pgrep -f "fetch_releases.py downloads/private_press/candidates_search.jsonl" > /dev/null; do sleep 20; done
python3 -I crawl_search.py companies company_slugs.txt > downloads/private_press/crawl_companies.out 2>&1
python3 -I fetch_releases.py downloads/private_press/candidates_search.jsonl fetched_search.jsonl > downloads/private_press/fetch_search2.out 2>&1
