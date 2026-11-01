# ca_bidsandtenders_backlog

- **Publisher**: bids&tenders (eSolutions) public procurement portals
- **Dataset Name**: Awarded Bids
- **URL**: https://opportunities.bidsandtenders.com/bid-opportunities/Embed?status=Awarded
- **Endpoint**: `https://opportunities.bidsandtenders.com/bid-opportunities/Embed?status=Awarded` (and portal details pages)

## Processing Notes
This is a continuation of the `ca_bidsandtenders` source to fetch the backlog of older awarded bids.
The pipeline extracts the details page for awarded bids listed in `listing.jsonl`, keeping vendors located in Canada.
The reference date is read dynamically from `coord/config.json`.

## Statistics from sample run
- details pages crawled: 250
- records output: 294

## Quirks
- The data includes multiple individual portals hosted by bids&tenders.
- A single bid can be awarded to multiple vendors.
