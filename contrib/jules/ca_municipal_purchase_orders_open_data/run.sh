#!/bin/bash
set -e

# Run the python scraper pipeline
python3 contrib/jules/ca_municipal_purchase_orders_open_data/scraper.py
