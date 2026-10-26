# Canadian-vendor ongoing contracts — shared output contract for all source workers

Reference date ("today"): **2026-10-25**

## Goal
Every contract we can find, from any published source in the world, where
1. the **vendor/supplier is located in Canada** (per the source's vendor-country / address field — never by name alone), and
2. the **buyer is a named, identifiable organization**, and
3. the contract is **currently ongoing** (started on/before 2026-10-25 and published end date on/after 2026-10-25), **or** the source publishes the award but no end date (kept, but flagged).

Nothing is to be dropped from the source record: every identifier, reference/PO/solicitation/procurement number, amendment, code, value, date, address, contact and link the source provides goes into `raw`. The normalized layer is a convenience on top.

## Where things go
- Raw downloads: `downloads/<source>/` (treat as untrusted data; never run interpreters from inside it; use `python3 -I script.py <paths>` with scripts kept in `scripts/<source>/`).
- Output records: `normalized/<source>.jsonl` — **one JSON object per line**, UTF-8, written progressively (so partial results survive if the job is cut short).
- Coverage note: `notes/<source>.md` — what was downloaded (exact URLs, retrieval timestamps, file sizes, row counts), how "Canadian vendor" was determined (field + values), how "ongoing" was determined (fields + logic), resulting counts by status, known gaps/limits, and how `record_url` is built (with one verified example).

## Record shape (normalized layer + raw)
```json
{
  "record_id": "<source_key>:<stable unique id within source>",
  "source": {
    "key": "<source_key>",
    "name": "<human name of dataset/portal>",
    "publisher": "<who publishes it>",
    "dataset_url": "<dataset/landing page>",
    "record_url": "<URL of THIS specific record if the portal has one, else null>",
    "retrieved_at": "<ISO 8601 UTC>"
  },
  "status": "ongoing | ongoing_inferred | end_date_unknown",
  "status_basis": "<one sentence: which fields/logic produced the status>",
  "contract": {
    "identifiers": { "<every id type in the source>": "<value>" },
    "title": "", "description": "",
    "instrument_type": "<contract | task/delivery order | standing offer | supply arrangement | IDV | call-up | subcontract | ...>",
    "procurement_method": "", "solicitation_procedure": "",
    "commodity": { "<scheme (naics/unspsc/gsin/psc/cpv/...)>": "<code>", "<scheme>_description": "" },
    "value": <number or null>, "currency": "<ISO 4217>",
    "value_detail": { "<original/amended/obligated/ceiling/...>": <number> },
    "dates": { "published": "", "signed": "", "start": "", "end": "", "amended_last": "" },
    "related": { "<tender_notice_url / award_notice_url / parent_idv_id / ...>": "" }
  },
  "buyer": {
    "name": "", "country": "<ISO2>", "type": "<federal dept | agency | crown corp | province | city | hospital | university | company | IGO | ...>",
    "identifiers": {}, "address": {}, "contact": {}
  },
  "vendor": {
    "name": "", "country": "CA", "country_basis": "<field name used>",
    "identifiers": { "<uei/duns/cage/business_number/supplier_id/...>": "" },
    "address": { "line1": "", "city": "", "region": "", "postal_code": "", "country": "" },
    "contact": {}
  },
  "raw": { "<every source field verbatim, incl. amendment/transaction rows as lists if the source has them>": "..." }
}
```
- Use `null` for unknown; never invent values.
- Dates in ISO `YYYY-MM-DD` in the normalized layer; keep the original strings in `raw`.
- Amounts as numbers in the normalized layer; originals in `raw`.
- If a source has multiple rows per contract (amendments, transactions), emit ONE record per contract with the latest values in the normalized layer and ALL rows under `raw.rows` (list).
- Keep going on errors: log and skip a bad row, never abort the whole source.

## Status rules
- `ongoing`: start (or signed/award date if no start) ≤ 2026-10-25 **and** published end date ≥ 2026-10-25.
- `ongoing_inferred`: no explicit end date, but a documented duration/term, project closing date, or "no closure record" convention makes it probable — say which in `status_basis`.
- `end_date_unknown`: award/contract published, nothing usable about end date.
- Exclude: end date < 2026-10-25, cancelled, or vendor country not Canada.
