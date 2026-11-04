# USAspending Sub-awards (Canadian Sub-recipients)

- **URL:** `https://api.usaspending.gov/api/v2/search/spending_by_award/`
- **Method:** `POST` with JSON payload filtering for `recipient_locations` CAN, `subawards` True, `time_period` 2007-10-01 to present.
- **Yield:** 1,869 sub-award records.
- **Ongoing Logic:** Uses 'Sub-Award Date' as start date, no end date provided. So it defaults to `end_date_unknown`.
- **Link:** Uses `https://www.usaspending.gov/award/{prime_award_internal_id}` as record_url since sub-awards don't have individual pages, they appear under the prime award page.
- **Missing Data:** Subawards do not have end dates in the general search endpoint. (Requires joining with prime award end date for true ongoing calculation, as mentioned in pipeline knowledge/docs, which Codex may implement in a later merge).
