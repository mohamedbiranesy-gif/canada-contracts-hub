#!/bin/bash
cd scripts/private_press
while pgrep -f "fetch_releases.py downloads/private_press/candidates_prnewswire_ca.jsonl" > /dev/null; do sleep 15; done
python3 -I fetch_releases.py downloads/private_press/candidates_search.jsonl fetched_search.jsonl > downloads/private_press/fetch_search.out 2>&1
