# bids&tenders award backlog

- **Endpoint**: https://opportunities.bidsandtenders.com/bid-opportunities/Embed
- **Access**: Resumable crawler `scripts/ca_bidsandtenders/crawl_listing.py` followed by `crawl_details.py`.
- **Fields extracted**: Bid title, description, categories, vendor names, vendor addresses, trade agreements.
- **Rows seen**: 140 details pages retrieved.
- **Canadian-vendor rows**: 109 rows output (country="Canada").
- **Ongoing rows**: 39 inferred ongoing (based on duration in months), 70 end date unknown.
- **Quirks**: The normalization script (`scripts/ca_bidsandtenders/normalize.py`) was patched to add the `link` property matching `record_url` to satisfy the schema validation.
