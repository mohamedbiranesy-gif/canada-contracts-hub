# ca_bidsandtenders_backlog — bids&tenders 2015-2020 award backlog

Status: DONE (first batch)

## Source
- Aggregator listing: `https://opportunities.bidsandtenders.com/bid-opportunities/Embed?status=Awarded&page=N`
- Crawl scope: page 2047 to 2051 (179 bids, 276 records), generating a new dataset of older bids to fulfill the task priority of adding *many new distinct buyers* (139 unique buyers found in this small batch).

## Canadian vendor
- Same logic as `ca_bidsandtenders`: `vendor.country` must be `Canada`.

## Ongoing logic
- `end_date_unknown`: as with the parent source.

## Notes
- This is a continuation crawl of `ca_bidsandtenders` to catch historical records.
