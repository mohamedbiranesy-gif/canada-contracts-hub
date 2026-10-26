#!/bin/bash
cd scripts/private_press
while pgrep -f "fetch_releases.py downloads/private_press/candidates_newswire.jsonl" > /dev/null; do sleep 15; done
python3 -I fetch_releases.py downloads/private_press/candidates_prnewswire_ca.jsonl fetched_prnewswire.jsonl > downloads/private_press/fetch_prnewswire.out 2>&1
