#!/usr/bin/env bash
set -euo pipefail

# This script fetches a slice of the MERX backlog using the existing ca_merx pipeline scripts.
# It is designed to be self-contained and reproducible.

echo "Running MERX backlog slice..."

# Create a temporary directory for the scrape
TMP_DIR=$(mktemp -d)
echo "Using temporary directory: $TMP_DIR"

# 1. Fetch a listing of recent awards (e.g. 2 pages deep)
echo "Crawling listing..."
python3 scripts/ca_merx/crawl_listing.py "$TMP_DIR" 2026-01-01 2 ""

# 2. Fetch detail pages for 20 records
echo "Crawling details..."
python3 scripts/ca_merx/crawl_details.py "$TMP_DIR" award,notice 20 1

# 3. Normalize the output
echo "Normalizing..."
python3 scripts/ca_merx/normalize.py "$TMP_DIR" "data/incoming/jules/"

# 4. Package and compress the output correctly
echo "Packaging..."
mv "data/incoming/jules/ca_merx.jsonl" "data/incoming/jules/records_ca_merx_backlog.jsonl"
gzip -f "data/incoming/jules/records_ca_merx_backlog.jsonl"

# Cleanup the remaining raw data if needed
rm -f data/incoming/jules/ca_merx_unverified_country.jsonl

echo "Backlog slice generated: data/incoming/jules/records_ca_merx_backlog.jsonl.gz"
