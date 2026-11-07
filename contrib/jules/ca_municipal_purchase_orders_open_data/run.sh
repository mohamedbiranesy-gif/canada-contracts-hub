#!/bin/bash
set -e
echo "Fetching data..."
python3 contrib/jules/ca_municipal_purchase_orders_open_data/fetch.py
echo "Parsing and normalizing data..."
python3 contrib/jules/ca_municipal_purchase_orders_open_data/ca_municipal_purchase_orders_open_data.py
echo "Validating records..."
python3 tools/validate_records.py data/incoming/jules/records_ca_municipal_purchase_orders_open_data.jsonl.gz
echo "Done."
