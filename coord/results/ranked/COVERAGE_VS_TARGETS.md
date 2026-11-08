# Coverage vs the downstream team's targets — 2026-11-08

Benchmarks (field × package with a numeric target): **93 of 438 met** (21.2%); 63 within 10 points; 282 further away.
A cell counts as filled only when it carries a value: blank, `not_published`, `not_found_yet` and label-only cells ("no identifier published …", "no dataset record …", "0 in the contract dataset …") do not count; the DNS checks count when checked. `any` = share of non-blank cells incl. such labels. Δ = change since the previous build in `coord/results/coverage_history.csv`.
Rows per package: P01M 19, P01T 92, P01_GOLD 593, P02 395, P03 228, P04 1583, P05 379, P06M 168, P06T 2440, P06 165, P07 252, P08 3038, P09 373, P10 2597, P11 488, P12 21, P13 50793

## Invoice-grade readiness (the row as an invoice header: bill-to, submit-to, references, terms, tax, vendor identity, follow-up)

| package | rows | all 11 elements | ≥ 9 of 11 | median elements | most-missing element |
|---|---|---|---|---|---|
| P01M | 19 | 0.0% | 26.3% | 7 | reference to quote (PO / contract / vendor id) (19 rows) |
| P01T | 92 | 0.0% | 27.2% | 8 | reference to quote (PO / contract / vendor id) (87 rows) |
| P01_GOLD | 593 | 12.8% | 60.2% | 9 | buyer tax status (285 rows) |
| P02 | 395 | 1.3% | 41.3% | 8 | PO rule (365 rows) |
| P03 | 228 | 1.8% | 29.8% | 8 | payment terms (177 rows) |
| P04 | 1583 | 1.3% | 25.1% | 8 | PO rule (1474 rows) |
| P05 | 379 | 0.3% | 6.3% | 6 | payment terms (339 rows) |
| P06M | 168 | 0.0% | 0.0% | 6 | reference to quote (PO / contract / vendor id) (168 rows) |
| P06T | 2440 | 0.0% | 0.5% | 5 | reference to quote (PO / contract / vendor id) (2436 rows) |
| P06 | 165 | 0.0% | 3.6% | 5 | reference to quote (PO / contract / vendor id) (165 rows) |
| P07 | 252 | 0.0% | 0.0% | 5 | reference to quote (PO / contract / vendor id) (252 rows) |
| P08 | 3038 | 0.0% | 0.0% | 5 | reference to quote (PO / contract / vendor id) (3038 rows) |
| P09 | 373 | 0.0% | 35.4% | 8 | payment terms (355 rows) |
| P10 | 2597 | 0.0% | 0.2% | 4 | reference to quote (PO / contract / vendor id) (2595 rows) |
| P11 | 488 | 0.6% | 8.8% | 4 | PO rule (469 rows) |
| P12 | 21 | 0.0% | 33.3% | 8 | PO rule (20 rows) |
| P13 | 50793 | 0.0% | 0.0% | 5 | reference to quote (PO / contract / vendor id) (50793 rows) |

## AP grade (how stringently the row's accounts-payable data meets what an invoice needs; A = invoicing mailbox referee-confirmed on the buyer's own domain with MX, legal name, address, PO rule and terms all published, no penalties)

| package | rows | A | B | C | D | E | median ap_score |
|---|---|---|---|---|---|---|---|
| P01M | 19 | 5 | 2 | 12 | 0 | 0 | 75 |
| P01T | 92 | 16 | 48 | 28 | 0 | 0 | 79 |
| P01_GOLD | 593 | 128 | 253 | 212 | 0 | 0 | 79 |
| P02 | 395 | 0 | 52 | 343 | 0 | 0 | 63 |
| P03 | 228 | 0 | 0 | 219 | 9 | 0 | 51 |
| P04 | 1583 | 0 | 0 | 1521 | 62 | 0 | 50 |
| P05 | 379 | 9 | 27 | 324 | 19 | 0 | 48 |
| P06M | 168 | 0 | 1 | 158 | 9 | 0 | 48 |
| P06T | 2440 | 0 | 16 | 2138 | 286 | 0 | 48 |
| P06 | 165 | 14 | 31 | 120 | 0 | 0 | 69 |
| P07 | 252 | 0 | 12 | 215 | 25 | 0 | 50 |
| P08 | 3038 | 0 | 0 | 2252 | 786 | 0 | 40 |
| P09 | 373 | 4 | 9 | 359 | 1 | 0 | 50 |
| P10 | 2597 | 3 | 9 | 1853 | 732 | 0 | 40 |
| P11 | 488 | 0 | 0 | 0 | 0 | 488 | 25 |
| P12 | 21 | 0 | 0 | 21 | 0 | 0 | 53 |
| P13 | 50793 | 5 | 26 | 40945 | 9817 | 0 | 43 |

### What still blocks grade A (rows per missing element; a row counts under every element it lacks)

| package | rows not A | referee confirmation of the mailbox | an invoicing / AP mailbox (not finance / procurement / general) | a mailbox on the buyer's own domain | MX record for the mailbox domain | published bill-to legal name | invoice / billing address | published PO rule | published payment terms | clear the penalty |
|---|---|---|---|---|---|---|---|---|---|---|
| P01M | 14 | 0 | 0 | 0 | 0 | 1 | 1 | 11 | 12 | 5 |
| P01T | 76 | 0 | 0 | 0 | 1 | 4 | 4 | 29 | 42 | 59 |
| P01_GOLD | 465 | 0 | 0 | 0 | 7 | 84 | 42 | 198 | 253 | 268 |
| P02 | 395 | 0 | 395 | 0 | 2 | 36 | 13 | 365 | 353 | 231 |
| P03 | 228 | 0 | 228 | 0 | 1 | 40 | 13 | 165 | 190 | 90 |
| P04 | 1583 | 0 | 1583 | 0 | 6 | 336 | 127 | 1474 | 1368 | 960 |
| P05 | 370 | 0 | 316 | 0 | 4 | 92 | 55 | 319 | 342 | 238 |
| P06M | 168 | 0 | 168 | 0 | 0 | 19 | 47 | 166 | 167 | 95 |
| P06T | 2440 | 0 | 2440 | 0 | 23 | 870 | 490 | 2401 | 2364 | 1916 |
| P06 | 151 | 0 | 0 | 0 | 5 | 73 | 49 | 91 | 123 | 41 |
| P07 | 252 | 0 | 252 | 0 | 8 | 119 | 74 | 223 | 237 | 120 |
| P08 | 3038 | 0 | 3038 | 0 | 20 | 1917 | 1041 | 3030 | 3024 | 2067 |
| P09 | 369 | 0 | 349 | 0 | 2 | 67 | 1 | 353 | 359 | 280 |
| P10 | 2594 | 0 | 2539 | 0 | 26 | 1758 | 917 | 2573 | 2580 | 1867 |
| P11 | 488 | 488 | 449 | 0 | 9 | 357 | 236 | 469 | 470 | 311 |
| P12 | 21 | 0 | 16 | 0 | 0 | 4 | 0 | 20 | 19 | 16 |
| P13 | 50788 | 0 | 50482 | 0 | 460 | 26012 | 12652 | 50716 | 50664 | 40188 |

## Where the work is (largest gaps in rows still needed)

| field | package | now | target | rows needed |
|---|---|---|---|---|
| buyer_address | P13 | 75.0% | 95% | 10156 |
| buyer_ap_cycle_published | P13 | 0.0% | 20% | 10151 |
| ap_system_hint | P13 | 0.5% | 20% | 9919 |
| buyer_phone | P13 | 79.0% | 95% | 8123 |
| buyer_esignature_preference | P13 | 0.1% | 15% | 7580 |
| buyer_tax_exempt_status | P13 | 0.1% | 15% | 7548 |
| buyer_payment_method_preference | P13 | 0.9% | 15% | 7155 |
| buyer_legal_name_as_published | P13 | 48.8% | 60% | 5695 |
| buyer_logo_url | P13 | 83.9% | 95% | 5651 |
| buyer_bn_as_published | P13 | 21.6% | 30% | 4255 |
| buyer_legal_name_as_published | P08 | 36.9% | 75% | 1158 |
| buyer_legal_name_as_published | P10 | 32.3% | 70% | 979 |
| buyer_address | P08 | 65.6% | 95% | 893 |
| vendor_emails | P08 | 47.0% | 75% | 852 |
| buyer_address | P10 | 64.4% | 95% | 796 |
| vendor_emails | P10 | 50.6% | 80% | 763 |
| invoice_reference_hint | P08 | 0.3% | 25% | 752 |
| buyer_bn_as_published | P08 | 10.5% | 35% | 745 |
| vendor_registered_address | P10 | 42.4% | 70% | 718 |
| average_contract_duration_days | P04 | 44.8% | 90% | 716 |
| vendor_logo_url | P04 | 42.6% | 85% | 671 |
| invoice_reference_hint | P10 | 1.0% | 25% | 624 |
| buyer_phone | P08 | 74.6% | 95% | 622 |
| buyer_phone | P10 | 71.3% | 95% | 616 |
| vendor_phone | P08 | 64.8% | 85% | 613 |
| buyer_ap_cycle_published | P08 | 0.1% | 20% | 606 |
| vendor_emails | P04 | 32.3% | 70% | 598 |
| ap_system_hint | P08 | 0.9% | 20% | 580 |
| end_date | P04 | 53.8% | 90% | 573 |
| buyer_vendor_id | P04 | 4.3% | 40% | 566 |
| currency | P04 | 59.9% | 95% | 555 |
| vendor_neq | P04 | 60.1% | 95% | 553 |
| ap_phone | P04 | 50.2% | 85% | 551 |
| buyer_bn_as_published | P10 | 8.9% | 30% | 549 |
| vendor_registered_address | P08 | 52.2% | 70% | 542 |
| commodity_codes | P04 | 51.2% | 85% | 536 |
| po_required_as_published | P04 | 6.9% | 40% | 525 |
| vendor_phone | P10 | 65.0% | 85% | 519 |
| buyer_ap_cycle_published | P10 | 0.1% | 20% | 518 |
| award_or_notice_id | P04 | 52.6% | 85% | 514 |

## 1. identifiers

### `invoice_reference_hint`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 19 | 42.1% | 42.1% |  | 50% | 🟡 8 pts to go |
| P01T | 92 | 70.7% | 70.7% |  | 50% | ✅ met |
| P01_GOLD | 593 | 92.6% | 94.8% |  | 95% | 🟡 2 pts to go |
| P02 | 395 | 78.7% | 81.0% |  | 95% | ❌ 16 pts to go |
| P03 | 228 | 85.5% | 91.2% |  | 95% | 🟡 10 pts to go |
| P04 | 1583 | 67.8% | 70.6% |  | 90% | ❌ 22 pts to go |
| P05 | 379 | 38.3% | 41.4% |  | 70% | ❌ 32 pts to go |
| P06M | 168 | 1.2% | 1.2% |  | n/a | no target |
| P06T | 2440 | 1.8% | 1.8% |  | n/a | no target |
| P06 | 165 | 44.8% | 44.8% |  | 30% | ✅ met |
| P07 | 252 | 11.5% | 11.5% |  | 30% | ❌ 18 pts to go |
| P08 | 3038 | 0.3% | 0.3% |  | 25% | ❌ 25 pts to go |
| P09 | 373 | 98.7% | 99.5% |  | 100% | 🟡 1 pts to go |
| P10 | 2597 | 1.0% | 1.9% |  | 25% | ❌ 24 pts to go |
| P11 | 488 | 24.6% | 27.7% |  | 60% | ❌ 35 pts to go |
| P12 | 21 | 100.0% | 100.0% |  | 100% | ✅ met |
| P13 | 50793 | 0.2% | 0.3% |  | 0% by design | — leave (by design) |

### `po_number_as_published`

> ceiling: a purchase-order number exists only where the buyer publishes PO-level data (Montréal, Laval, Toronto open data so far) or the record itself carries one; most sources publish awards, not POs — the target cannot be reached from public data for most buyers

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 19 | 0.0% | 0.0% |  | n/a | no target |
| P01T | 92 | 0.0% | 0.0% |  | 10% | 🟡 10 pts to go |
| P01_GOLD | 593 | 6.4% | 6.4% |  | 50% | ❌ 44 pts to go |
| P02 | 395 | 7.6% | 7.6% |  | 50% | ❌ 42 pts to go |
| P03 | 228 | 1.8% | 1.8% |  | 40% | ❌ 38 pts to go |
| P04 | 1583 | 1.1% | 1.1% |  | 30% | ❌ 29 pts to go |
| P05 | 379 | 0.3% | 0.3% |  | 20% | ❌ 20 pts to go |
| P06M | 168 | 0.0% | 0.0% |  | n/a | no target |
| P06T | 2440 | 0.0% | 0.0% |  | n/a | no target |
| P06 | 165 | 0.0% | 0.0% |  | n/a | no target |
| P07 | 252 | 0.0% | 0.0% |  | n/a | no target |
| P08 | 3038 | 0.0% | 0.0% |  | n/a | no target |
| P09 | 373 | 0.5% | 0.5% |  | 50% | ❌ 50 pts to go |
| P10 | 2597 | 0.1% | 0.1% |  | n/a | no target |
| P11 | 488 | 1.2% | 1.2% |  | n/a | no target |
| P12 | 21 | 0.0% | 0.0% |  | n/a | no target |
| P13 | 50793 | 0.0% | 0.0% |  | n/a | no target |

### `contract_or_agreement_number`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 19 | 0.0% | 0.0% |  | n/a | no target |
| P01T | 92 | 5.4% | 5.4% |  | 50% | ❌ 45 pts to go |
| P01_GOLD | 593 | 69.6% | 69.6% |  | 85% | ❌ 15 pts to go |
| P02 | 395 | 73.7% | 73.7% |  | 90% | ❌ 16 pts to go |
| P03 | 228 | 71.5% | 71.5% |  | 85% | ❌ 14 pts to go |
| P04 | 1583 | 65.5% | 65.5% |  | 85% | ❌ 20 pts to go |
| P05 | 379 | 30.1% | 30.1% |  | 60% | ❌ 30 pts to go |
| P06M | 168 | 0.0% | 0.0% |  | n/a | no target |
| P06T | 2440 | 0.2% | 0.2% |  | n/a | no target |
| P06 | 165 | 0.0% | 0.0% |  | n/a | no target |
| P07 | 252 | 0.0% | 0.0% |  | n/a | no target |
| P08 | 3038 | 0.0% | 0.0% |  | n/a | no target |
| P09 | 373 | 96.5% | 96.5% |  | 100% | 🟡 4 pts to go |
| P10 | 2597 | 0.0% | 0.0% |  | n/a | no target |
| P11 | 488 | 22.3% | 22.3% |  | 60% | ❌ 38 pts to go |
| P12 | 21 | 100.0% | 100.0% |  | n/a | no target |
| P13 | 50793 | 0.0% | 0.0% |  | n/a | no target |

### `solicitation_or_tender_number`

> ceiling: SEAO's 'numero' is the organisation's own reference for the notice (SEAO data dictionary) and is reported here; sources that publish awards under a tender number only (bids&tenders, SaskTenders, BC) also carry it as the contract reference, labelled

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 19 | 0.0% | 0.0% |  | n/a | no target |
| P01T | 92 | 2.2% | 2.2% |  | 30% | ❌ 28 pts to go |
| P01_GOLD | 593 | 53.3% | 53.3% |  | 80% | ❌ 27 pts to go |
| P02 | 395 | 64.8% | 64.8% |  | 60% | ✅ met |
| P03 | 228 | 58.8% | 58.8% |  | 80% | ❌ 21 pts to go |
| P04 | 1583 | 54.4% | 54.4% |  | 50% | ✅ met |
| P05 | 379 | 12.4% | 12.4% |  | 40% | ❌ 28 pts to go |
| P06M | 168 | 0.0% | 0.0% |  | n/a | no target |
| P06T | 2440 | 0.2% | 0.2% |  | n/a | no target |
| P06 | 165 | 0.0% | 0.0% |  | n/a | no target |
| P07 | 252 | 0.0% | 0.0% |  | n/a | no target |
| P08 | 3038 | 0.0% | 0.0% |  | n/a | no target |
| P09 | 373 | 87.4% | 87.4% |  | 50% | ✅ met |
| P10 | 2597 | 0.0% | 0.0% |  | n/a | no target |
| P11 | 488 | 18.6% | 18.6% |  | 40% | ❌ 21 pts to go |
| P12 | 21 | 100.0% | 100.0% |  | 100% | ✅ met |
| P13 | 50793 | 0.0% | 0.0% |  | n/a | no target |

### `award_or_notice_id`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 19 | 0.0% | 0.0% |  | n/a | no target |
| P01T | 92 | 3.3% | 3.3% |  | n/a | no target |
| P01_GOLD | 593 | 44.4% | 44.4% |  | 85% | ❌ 41 pts to go |
| P02 | 395 | 54.2% | 54.2% |  | 90% | ❌ 36 pts to go |
| P03 | 228 | 50.9% | 50.9% |  | 85% | ❌ 34 pts to go |
| P04 | 1583 | 52.6% | 52.6% |  | 85% | ❌ 32 pts to go |
| P05 | 379 | 15.3% | 15.3% |  | 50% | ❌ 35 pts to go |
| P06M | 168 | 0.0% | 0.0% |  | n/a | no target |
| P06T | 2440 | 0.1% | 0.1% |  | n/a | no target |
| P06 | 165 | 0.0% | 0.0% |  | n/a | no target |
| P07 | 252 | 0.0% | 0.0% |  | n/a | no target |
| P08 | 3038 | 0.0% | 0.0% |  | n/a | no target |
| P09 | 373 | 90.6% | 90.6% |  | 100% | 🟡 9 pts to go |
| P10 | 2597 | 0.0% | 0.0% |  | n/a | no target |
| P11 | 488 | 17.4% | 17.4% |  | 60% | ❌ 43 pts to go |
| P12 | 21 | 0.0% | 0.0% |  | n/a | no target |
| P13 | 50793 | 0.0% | 0.0% |  | n/a | no target |

### `buyer_vendor_id`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 19 | 0.0% | 0.0% |  | n/a | no target |
| P01T | 92 | 2.2% | 2.2% |  | n/a | no target |
| P01_GOLD | 593 | 13.2% | 13.2% |  | 60% | ❌ 47 pts to go |
| P02 | 395 | 7.8% | 7.8% |  | 50% | ❌ 42 pts to go |
| P03 | 228 | 10.1% | 10.1% |  | 50% | ❌ 40 pts to go |
| P04 | 1583 | 4.3% | 4.3% |  | 40% | ❌ 36 pts to go |
| P05 | 379 | 1.3% | 1.3% |  | 20% | ❌ 19 pts to go |
| P06M | 168 | 0.0% | 0.0% |  | n/a | no target |
| P06T | 2440 | 0.1% | 0.1% |  | n/a | no target |
| P06 | 165 | 0.0% | 0.0% |  | n/a | no target |
| P07 | 252 | 0.0% | 0.0% |  | n/a | no target |
| P08 | 3038 | 0.0% | 0.0% |  | n/a | no target |
| P09 | 373 | 2.4% | 2.4% |  | 50% | ❌ 48 pts to go |
| P10 | 2597 | 0.0% | 0.0% |  | n/a | no target |
| P11 | 488 | 4.5% | 4.5% |  | n/a | no target |
| P12 | 21 | 0.0% | 0.0% |  | n/a | no target |
| P13 | 50793 | 0.0% | 0.0% |  | n/a | no target |

### `commodity_codes`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 19 | 0.0% | 0.0% |  | n/a | no target |
| P01T | 92 | 0.0% | 0.0% |  | n/a | no target |
| P01_GOLD | 593 | 36.8% | 36.8% |  | 80% | ❌ 43 pts to go |
| P02 | 395 | 58.7% | 58.7% |  | 90% | ❌ 31 pts to go |
| P03 | 228 | 36.8% | 36.8% |  | 80% | ❌ 43 pts to go |
| P04 | 1583 | 51.2% | 51.2% |  | 85% | ❌ 34 pts to go |
| P05 | 379 | 5.0% | 5.0% |  | 50% | ❌ 45 pts to go |
| P06M | 168 | 0.0% | 0.0% |  | n/a | no target |
| P06T | 2440 | 0.0% | 0.0% |  | n/a | no target |
| P06 | 165 | 0.0% | 0.0% |  | n/a | no target |
| P07 | 252 | 0.0% | 0.0% |  | n/a | no target |
| P08 | 3038 | 0.0% | 0.0% |  | n/a | no target |
| P09 | 373 | 75.6% | 75.6% |  | 95% | ❌ 19 pts to go |
| P10 | 2597 | 0.0% | 0.0% |  | n/a | no target |
| P11 | 488 | 15.0% | 15.0% |  | 50% | ❌ 35 pts to go |
| P12 | 21 | 0.0% | 0.0% |  | n/a | no target |
| P13 | 50793 | 0.0% | 0.0% |  | n/a | no target |

### `buyer_org_codes`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 19 | 0.0% | 0.0% |  | n/a | no target |
| P01T | 92 | 1.1% | 1.1% |  | n/a | no target |
| P01_GOLD | 593 | 8.6% | 8.6% |  | 50% | ❌ 41 pts to go |
| P02 | 395 | 7.6% | 7.6% |  | 50% | ❌ 42 pts to go |
| P03 | 228 | 2.6% | 2.6% |  | 30% | ❌ 27 pts to go |
| P04 | 1583 | 1.1% | 1.1% |  | 30% | ❌ 29 pts to go |
| P05 | 379 | 0.0% | 0.0% |  | n/a | no target |
| P06M | 168 | 0.0% | 0.0% |  | n/a | no target |
| P06T | 2440 | 0.0% | 0.0% |  | n/a | no target |
| P06 | 165 | 0.0% | 0.0% |  | n/a | no target |
| P07 | 252 | 0.0% | 0.0% |  | n/a | no target |
| P08 | 3038 | 0.0% | 0.0% |  | n/a | no target |
| P09 | 373 | 0.3% | 0.3% |  | n/a | no target |
| P10 | 2597 | 0.0% | 0.0% |  | n/a | no target |
| P11 | 488 | 1.2% | 1.2% |  | n/a | no target |
| P12 | 21 | 0.0% | 0.0% |  | n/a | no target |
| P13 | 50793 | 0.0% | 0.0% |  | n/a | no target |

### `records_with_this_vendor`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 19 | 100.0% | 100.0% |  | n/a | no target |
| P01T | 92 | 100.0% | 100.0% |  | 60% | ✅ met |
| P01_GOLD | 593 | 100.0% | 100.0% |  | 100% | ✅ met |
| P02 | 395 | 100.0% | 100.0% |  | 100% | ✅ met |
| P03 | 228 | 100.0% | 100.0% |  | 100% | ✅ met |
| P04 | 1583 | 100.0% | 100.0% |  | 95% | ✅ met |
| P05 | 379 | 100.0% | 100.0% |  | 70% | ✅ met |
| P06M | 168 | 100.0% | 100.0% |  | n/a | no target |
| P06T | 2440 | 100.0% | 100.0% |  | n/a | no target |
| P06 | 165 | 100.0% | 100.0% |  | 50% | ✅ met |
| P07 | 252 | 100.0% | 100.0% |  | n/a | no target |
| P08 | 3038 | 100.0% | 100.0% |  | n/a | no target |
| P09 | 373 | 100.0% | 100.0% |  | 100% | ✅ met |
| P10 | 2597 | 100.0% | 100.0% |  | n/a | no target |
| P11 | 488 | 100.0% | 100.0% |  | 70% | ✅ met |
| P12 | 21 | 100.0% | 100.0% |  | n/a | no target |
| P13 | 50793 | 0.0% | 0.0% |  | n/a | no target |

## 2. vendor

### `vendor_bn9`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 19 | 100.0% | 100.0% |  | 70% | ✅ met |
| P01T | 92 | 80.4% | 80.4% |  | 60% | ✅ met |
| P01_GOLD | 593 | 78.4% | 78.4% |  | 90% | ❌ 12 pts to go |
| P02 | 395 | 65.6% | 65.6% |  | 85% | ❌ 19 pts to go |
| P03 | 228 | 81.1% | 81.1% |  | 90% | 🟡 9 pts to go |
| P04 | 1583 | 53.8% | 53.8% |  | 75% | ❌ 21 pts to go |
| P05 | 379 | 52.8% | 52.8% |  | 50% | ✅ met |
| P06M | 168 | 74.4% | 74.4% |  | n/a | no target |
| P06T | 2440 | 60.7% | 60.7% |  | n/a | no target |
| P06 | 165 | 46.7% | 46.7% |  | 40% | ✅ met |
| P07 | 252 | 40.1% | 40.1% |  | 50% | 🟡 10 pts to go |
| P08 | 3038 | 41.8% | 41.8% |  | 50% | 🟡 8 pts to go |
| P09 | 373 | 54.7% | 54.7% |  | 80% | ❌ 25 pts to go |
| P10 | 2597 | 36.6% | 36.6% |  | 40% | 🟡 3 pts to go |
| P11 | 488 | 45.9% | 45.9% |  | 60% | ❌ 14 pts to go |
| P12 | 21 | 52.4% | 52.4% |  | 85% | ❌ 33 pts to go |
| P13 | 50793 | 91.7% | 91.7% |  | 0% by design | — leave (by design) |

### `vendor_registered_address`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 19 | 63.2% | 63.2% |  | n/a | no target |
| P01T | 92 | 63.0% | 63.0% |  | n/a | no target |
| P01_GOLD | 593 | 75.5% | 75.5% |  | 95% | ❌ 20 pts to go |
| P02 | 395 | 81.5% | 81.5% |  | 95% | ❌ 14 pts to go |
| P03 | 228 | 77.2% | 77.2% |  | 95% | ❌ 18 pts to go |
| P04 | 1583 | 78.7% | 78.7% |  | 95% | ❌ 16 pts to go |
| P05 | 379 | 55.7% | 55.7% |  | 70% | ❌ 14 pts to go |
| P06M | 168 | 20.8% | 20.8% |  | n/a | no target |
| P06T | 2440 | 78.3% | 78.3% |  | n/a | no target |
| P06 | 165 | 55.2% | 55.2% |  | 80% | ❌ 25 pts to go |
| P07 | 252 | 52.0% | 52.0% |  | 70% | ❌ 18 pts to go |
| P08 | 3038 | 52.2% | 52.2% |  | 70% | ❌ 18 pts to go |
| P09 | 373 | 89.5% | 89.5% |  | 100% | ❌ 10 pts to go |
| P10 | 2597 | 42.4% | 42.4% |  | 70% | ❌ 28 pts to go |
| P11 | 488 | 54.5% | 54.5% |  | 75% | ❌ 20 pts to go |
| P12 | 21 | 100.0% | 100.0% |  | n/a | no target |
| P13 | 50793 | 0.0% | 0.0% |  | n/a | no target |

### `vendor_trading_name`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 19 | 52.6% | 52.6% |  | n/a | no target |
| P01T | 92 | 19.6% | 19.6% |  | n/a | no target |
| P01_GOLD | 593 | 50.1% | 50.1% |  | 60% | 🟡 10 pts to go |
| P02 | 395 | 62.5% | 62.5% |  | 60% | ✅ met |
| P03 | 228 | 57.5% | 57.5% |  | 60% | 🟡 2 pts to go |
| P04 | 1583 | 53.3% | 53.3% |  | 55% | 🟡 2 pts to go |
| P05 | 379 | 23.5% | 23.5% |  | 50% | ❌ 26 pts to go |
| P06M | 168 | 17.3% | 17.3% |  | n/a | no target |
| P06T | 2440 | 53.6% | 53.6% |  | n/a | no target |
| P06 | 165 | 48.5% | 48.5% |  | n/a | no target |
| P07 | 252 | 44.4% | 44.4% |  | 55% | ❌ 11 pts to go |
| P08 | 3038 | 44.3% | 44.3% |  | 50% | 🟡 6 pts to go |
| P09 | 373 | 71.6% | 71.6% |  | 70% | ✅ met |
| P10 | 2597 | 50.4% | 50.4% |  | 55% | 🟡 5 pts to go |
| P11 | 488 | 41.4% | 41.4% |  | 50% | 🟡 9 pts to go |
| P12 | 21 | 85.7% | 85.7% |  | n/a | no target |
| P13 | 50793 | 0.0% | 0.0% |  | n/a | no target |

### `vendor_phone`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 19 | 36.8% | 36.8% |  | n/a | no target |
| P01T | 92 | 0.0% | 0.0% |  | n/a | no target |
| P01_GOLD | 593 | 33.1% | 33.1% |  | 70% | ❌ 37 pts to go |
| P02 | 395 | 41.3% | 41.3% |  | 70% | ❌ 29 pts to go |
| P03 | 228 | 39.5% | 39.5% |  | 70% | ❌ 30 pts to go |
| P04 | 1583 | 32.9% | 32.9% |  | 65% | ❌ 32 pts to go |
| P05 | 379 | 16.4% | 16.4% |  | 60% | ❌ 44 pts to go |
| P06M | 168 | 6.5% | 6.5% |  | n/a | no target |
| P06T | 2440 | 0.0% | 0.0% |  | n/a | no target |
| P06 | 165 | 58.2% | 58.2% |  | 40% | ✅ met |
| P07 | 252 | 64.7% | 64.7% |  | 85% | ❌ 20 pts to go |
| P08 | 3038 | 64.8% | 64.8% |  | 85% | ❌ 20 pts to go |
| P09 | 373 | 51.7% | 51.7% |  | 85% | ❌ 33 pts to go |
| P10 | 2597 | 65.0% | 65.0% |  | 85% | ❌ 20 pts to go |
| P11 | 488 | 48.8% | 48.8% |  | 75% | ❌ 26 pts to go |
| P12 | 21 | 4.8% | 4.8% |  | n/a | no target |
| P13 | 50793 | 100.0% | 100.0% |  | 60% | ✅ met |

### `vendor_website`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 19 | 94.7% | 94.7% |  | n/a | no target |
| P01T | 92 | 90.2% | 90.2% |  | n/a | no target |
| P01_GOLD | 593 | 89.0% | 89.0% |  | 90% | 🟡 1 pts to go |
| P02 | 395 | 81.8% | 81.8% |  | 90% | 🟡 8 pts to go |
| P03 | 228 | 84.6% | 84.6% |  | 90% | 🟡 5 pts to go |
| P04 | 1583 | 63.4% | 63.4% |  | 85% | ❌ 22 pts to go |
| P05 | 379 | 43.8% | 43.8% |  | 70% | ❌ 26 pts to go |
| P06M | 168 | 67.9% | 67.9% |  | n/a | no target |
| P06T | 2440 | 77.9% | 77.9% |  | n/a | no target |
| P06 | 165 | 97.0% | 97.0% |  | 50% | ✅ met |
| P07 | 252 | 96.8% | 96.8% |  | 100% | 🟡 3 pts to go |
| P08 | 3038 | 96.1% | 96.1% |  | 100% | 🟡 4 pts to go |
| P09 | 373 | 81.2% | 81.2% |  | 100% | ❌ 19 pts to go |
| P10 | 2597 | 100.0% | 100.0% |  | 100% | ✅ met |
| P11 | 488 | 90.0% | 90.0% |  | 100% | 🟡 10 pts to go |
| P12 | 21 | 42.9% | 42.9% |  | n/a | no target |
| P13 | 50793 | 100.0% | 100.0% |  | n/a | no target |

### `vendor_emails`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 19 | 36.8% | 36.8% |  | n/a | no target |
| P01T | 92 | 0.0% | 0.0% |  | n/a | no target |
| P01_GOLD | 593 | 36.6% | 36.6% |  | 70% | ❌ 33 pts to go |
| P02 | 395 | 43.8% | 43.8% |  | 75% | ❌ 31 pts to go |
| P03 | 228 | 43.0% | 43.0% |  | 75% | ❌ 32 pts to go |
| P04 | 1583 | 32.3% | 32.3% |  | 70% | ❌ 38 pts to go |
| P05 | 379 | 13.7% | 13.7% |  | 55% | ❌ 41 pts to go |
| P06M | 168 | 6.5% | 6.5% |  | n/a | no target |
| P06T | 2440 | 0.0% | 0.0% |  | n/a | no target |
| P06 | 165 | 40.0% | 40.0% |  | n/a | no target |
| P07 | 252 | 35.7% | 35.7% |  | 70% | ❌ 34 pts to go |
| P08 | 3038 | 47.0% | 47.0% |  | 75% | ❌ 28 pts to go |
| P09 | 373 | 52.5% | 52.5% |  | 85% | ❌ 32 pts to go |
| P10 | 2597 | 50.6% | 50.6% |  | 80% | ❌ 29 pts to go |
| P11 | 488 | 36.5% | 36.5% |  | 70% | ❌ 34 pts to go |
| P12 | 21 | 19.0% | 19.0% |  | n/a | no target |
| P13 | 50793 | 0.0% | 0.0% |  | n/a | no target |

### `vendor_logo_url`

> ceiling: needs the vendor's website first; sites that block automated readers (robots.txt / 403) are never read

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 19 | 36.8% | 36.8% |  | n/a | no target |
| P01T | 92 | 0.0% | 0.0% |  | n/a | no target |
| P01_GOLD | 593 | 48.9% | 48.9% |  | 90% | ❌ 41 pts to go |
| P02 | 395 | 56.2% | 56.2% |  | 90% | ❌ 34 pts to go |
| P03 | 228 | 55.7% | 55.7% |  | 90% | ❌ 34 pts to go |
| P04 | 1583 | 42.6% | 42.6% |  | 85% | ❌ 42 pts to go |
| P05 | 379 | 22.2% | 22.2% |  | 75% | ❌ 53 pts to go |
| P06M | 168 | 6.5% | 6.5% |  | n/a | no target |
| P06T | 2440 | 0.0% | 0.0% |  | n/a | no target |
| P06 | 165 | 87.3% | 87.3% |  | n/a | no target |
| P07 | 252 | 88.1% | 88.1% |  | 100% | ❌ 12 pts to go |
| P08 | 3038 | 85.4% | 85.4% |  | 100% | ❌ 15 pts to go |
| P09 | 373 | 58.2% | 58.2% |  | n/a | no target |
| P10 | 2597 | 87.6% | 87.6% |  | 100% | ❌ 12 pts to go |
| P11 | 488 | 64.3% | 64.3% |  | n/a | no target |
| P12 | 21 | 14.3% | 14.3% |  | n/a | no target |
| P13 | 50793 | 0.0% | 0.0% |  | n/a | no target |

### `vendor_neq`

> ceiling: only Québec-registered vendors have an NEQ; the share of QC vendors is reported next to the rate

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 19 | 0.0% | 0.0% |  | n/a | no target |
| P01T | 92 | 21.7% | 21.7% |  | n/a | no target · QC vendors: 2 rows, 100.0% filled |
| P01_GOLD | 593 | 49.1% | 49.1% |  | 95% | ❌ 46 pts to go · QC vendors: 51 rows, 98.0% filled |
| P02 | 395 | 66.8% | 66.8% |  | 95% | ❌ 28 pts to go · QC vendors: 98 rows, 100.0% filled |
| P03 | 228 | 54.8% | 54.8% |  | 95% | ❌ 40 pts to go · QC vendors: 16 rows, 100.0% filled |
| P04 | 1583 | 60.1% | 60.1% |  | 95% | ❌ 35 pts to go · QC vendors: 441 rows, 98.6% filled |
| P05 | 379 | 13.7% | 13.7% |  | n/a | no target · QC vendors: 26 rows, 92.3% filled |
| P06M | 168 | 0.0% | 0.0% |  | n/a | no target |
| P06T | 2440 | 55.9% | 55.9% |  | n/a | no target · QC vendors: 56 rows, 100.0% filled |
| P06 | 165 | 24.2% | 24.2% |  | n/a | no target · QC vendors: 16 rows, 100.0% filled |
| P07 | 252 | 19.4% | 19.4% |  | n/a | no target · QC vendors: 26 rows, 96.2% filled |
| P08 | 3038 | 26.9% | 26.9% |  | n/a | no target · QC vendors: 544 rows, 98.5% filled |
| P09 | 373 | 81.8% | 81.8% |  | 95% | ❌ 13 pts to go · QC vendors: 156 rows, 99.4% filled |
| P10 | 2597 | 22.8% | 22.8% |  | n/a | no target · QC vendors: 444 rows, 94.6% filled |
| P11 | 488 | 28.9% | 28.9% |  | n/a | no target · QC vendors: 79 rows, 98.7% filled |
| P12 | 21 | 76.2% | 76.2% |  | n/a | no target · QC vendors: 4 rows, 100.0% filled |
| P13 | 50793 | 0.0% | 0.0% |  | n/a | no target |

### `vendor_years_in_business`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 19 | 63.2% | 63.2% |  | n/a | no target · vendors with a registry record: 12 rows, 100.0% filled |
| P01T | 92 | 63.0% | 63.0% |  | n/a | no target · vendors with a registry record: 58 rows, 100.0% filled |
| P01_GOLD | 593 | 85.2% | 85.2% |  | 100% | ❌ 15 pts to go · vendors with a registry record: 505 rows, 100.0% filled |
| P02 | 395 | 87.8% | 87.8% |  | 100% | ❌ 12 pts to go · vendors with a registry record: 347 rows, 100.0% filled |
| P03 | 228 | 87.7% | 87.7% |  | 100% | ❌ 12 pts to go · vendors with a registry record: 200 rows, 100.0% filled |
| P04 | 1583 | 81.4% | 81.4% |  | 100% | ❌ 19 pts to go · vendors with a registry record: 1289 rows, 100.0% filled |
| P05 | 379 | 61.2% | 61.2% |  | n/a | no target · vendors with a registry record: 232 rows, 100.0% filled |
| P06M | 168 | 20.8% | 20.8% |  | n/a | no target · vendors with a registry record: 35 rows, 100.0% filled |
| P06T | 2440 | 78.3% | 78.3% |  | n/a | no target · vendors with a registry record: 1910 rows, 100.0% filled |
| P06 | 165 | 58.2% | 58.2% |  | n/a | no target · vendors with a registry record: 96 rows, 100.0% filled |
| P07 | 252 | 54.4% | 54.4% |  | n/a | no target · vendors with a registry record: 137 rows, 100.0% filled |
| P08 | 3038 | 54.3% | 54.3% |  | n/a | no target · vendors with a registry record: 1651 rows, 100.0% filled |
| P09 | 373 | 92.8% | 92.8% |  | n/a | no target · vendors with a registry record: 346 rows, 100.0% filled |
| P10 | 2597 | 43.6% | 43.6% |  | n/a | no target · vendors with a registry record: 1133 rows, 100.0% filled |
| P11 | 488 | 58.4% | 58.4% |  | n/a | no target · vendors with a registry record: 285 rows, 100.0% filled |
| P12 | 21 | 100.0% | 100.0% |  | n/a | no target · vendors with a registry record: 21 rows, 100.0% filled |
| P13 | 50793 | 0.0% | 0.0% |  | n/a | no target |

## 3. buyer

### `buyer_legal_name_as_published`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 19 | 94.7% | 94.7% |  | 90% | ✅ met |
| P01T | 92 | 95.7% | 95.7% |  | 90% | ✅ met |
| P01_GOLD | 593 | 85.8% | 85.8% |  | 95% | 🟡 9 pts to go |
| P02 | 395 | 90.9% | 90.9% |  | 95% | 🟡 4 pts to go |
| P03 | 228 | 82.5% | 82.5% |  | 85% | 🟡 2 pts to go |
| P04 | 1583 | 78.8% | 78.8% |  | 90% | ❌ 11 pts to go |
| P05 | 379 | 75.7% | 75.7% |  | 75% | ✅ met |
| P06M | 168 | 88.7% | 88.7% |  | n/a | no target |
| P06T | 2440 | 64.3% | 64.3% |  | n/a | no target |
| P06 | 165 | 55.8% | 55.8% |  | 80% | ❌ 24 pts to go |
| P07 | 252 | 52.8% | 52.8% |  | 80% | ❌ 27 pts to go |
| P08 | 3038 | 36.9% | 36.9% |  | 75% | ❌ 38 pts to go |
| P09 | 373 | 82.0% | 82.0% |  | 95% | ❌ 13 pts to go |
| P10 | 2597 | 32.3% | 32.3% |  | 70% | ❌ 38 pts to go |
| P11 | 488 | 26.8% | 26.8% |  | 65% | ❌ 38 pts to go |
| P12 | 21 | 81.0% | 81.0% |  | 80% | ✅ met |
| P13 | 50793 | 48.8% | 48.8% |  | 60% | ❌ 11 pts to go |

### `buyer_bn_as_published`

> ceiling: a buyer's BN is public only where the buyer prints it or a public dataset carries it (CRA charities, federal grants & contributions recipients, business registries for corporations); municipalities rarely publish theirs

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 19 | 36.8% | 36.8% |  | 50% | ❌ 13 pts to go |
| P01T | 92 | 20.7% | 20.7% |  | n/a | no target |
| P01_GOLD | 593 | 20.7% | 20.7% |  | 40% | ❌ 19 pts to go |
| P02 | 395 | 22.5% | 22.5% |  | 40% | ❌ 18 pts to go |
| P03 | 228 | 25.9% | 25.9% |  | 40% | ❌ 14 pts to go |
| P04 | 1583 | 27.4% | 27.4% |  | 40% | ❌ 13 pts to go |
| P05 | 379 | 23.5% | 23.5% |  | 25% | 🟡 2 pts to go |
| P06M | 168 | 25.0% | 25.0% |  | n/a | no target |
| P06T | 2440 | 30.8% | 30.8% |  | n/a | no target |
| P06 | 165 | 9.7% | 9.7% |  | 35% | ❌ 25 pts to go |
| P07 | 252 | 9.9% | 9.9% |  | 35% | ❌ 25 pts to go |
| P08 | 3038 | 10.5% | 10.5% |  | 35% | ❌ 24 pts to go |
| P09 | 373 | 18.0% | 18.0% |  | n/a | no target |
| P10 | 2597 | 8.9% | 8.9% |  | 30% | ❌ 21 pts to go |
| P11 | 488 | 8.8% | 8.8% |  | n/a | no target |
| P12 | 21 | 19.0% | 19.0% |  | n/a | no target |
| P13 | 50793 | 21.6% | 21.6% |  | 30% | 🟡 8 pts to go |

### `buyer_address`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 19 | 94.7% | 94.7% |  | 100% | 🟡 5 pts to go |
| P01T | 92 | 93.5% | 93.5% |  | 100% | 🟡 6 pts to go |
| P01_GOLD | 593 | 89.0% | 89.0% |  | 100% | ❌ 11 pts to go |
| P02 | 395 | 95.9% | 95.9% |  | 100% | 🟡 4 pts to go |
| P03 | 228 | 94.3% | 94.3% |  | 100% | 🟡 6 pts to go |
| P04 | 1583 | 90.8% | 90.8% |  | 100% | 🟡 9 pts to go |
| P05 | 379 | 84.4% | 84.4% |  | 100% | ❌ 16 pts to go |
| P06M | 168 | 71.4% | 71.4% |  | n/a | no target |
| P06T | 2440 | 79.8% | 79.8% |  | n/a | no target |
| P06 | 165 | 66.7% | 66.7% |  | 95% | ❌ 28 pts to go |
| P07 | 252 | 69.4% | 69.4% |  | 95% | ❌ 26 pts to go |
| P08 | 3038 | 65.6% | 65.6% |  | 95% | ❌ 29 pts to go |
| P09 | 373 | 98.4% | 98.4% |  | 100% | 🟡 2 pts to go |
| P10 | 2597 | 64.4% | 64.4% |  | 95% | ❌ 31 pts to go |
| P11 | 488 | 36.7% | 36.7% |  | 80% | ❌ 43 pts to go |
| P12 | 21 | 100.0% | 100.0% |  | 100% | ✅ met |
| P13 | 50793 | 75.0% | 75.0% |  | 95% | ❌ 20 pts to go |

### `buyer_phone`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 19 | 89.5% | 89.5% |  | n/a | no target |
| P01T | 92 | 80.4% | 80.4% |  | n/a | no target |
| P01_GOLD | 593 | 69.5% | 69.5% |  | 90% | ❌ 20 pts to go |
| P02 | 395 | 77.7% | 77.7% |  | 95% | ❌ 17 pts to go |
| P03 | 228 | 73.7% | 73.7% |  | 95% | ❌ 21 pts to go |
| P04 | 1583 | 84.7% | 84.7% |  | 95% | ❌ 10 pts to go |
| P05 | 379 | 74.9% | 74.9% |  | 90% | ❌ 15 pts to go |
| P06M | 168 | 83.9% | 83.9% |  | n/a | no target |
| P06T | 2440 | 77.1% | 77.1% |  | n/a | no target |
| P06 | 165 | 63.6% | 63.6% |  | 95% | ❌ 31 pts to go |
| P07 | 252 | 65.1% | 65.1% |  | 90% | ❌ 25 pts to go |
| P08 | 3038 | 74.6% | 74.6% |  | 95% | ❌ 20 pts to go |
| P09 | 373 | 89.5% | 89.5% |  | 100% | ❌ 10 pts to go |
| P10 | 2597 | 71.3% | 71.3% |  | 95% | ❌ 24 pts to go |
| P11 | 488 | 27.3% | 27.3% |  | 75% | ❌ 48 pts to go |
| P12 | 21 | 85.7% | 85.7% |  | n/a | no target |
| P13 | 50793 | 79.0% | 79.0% |  | 95% | ❌ 16 pts to go |

### `buyer_logo_url`

> ceiling: sites that block automated readers (robots.txt / 403) are never read; an og:image that looks like a photo is labelled

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 19 | 78.9% | 78.9% |  | n/a | no target |
| P01T | 92 | 91.3% | 91.3% |  | 95% | 🟡 4 pts to go |
| P01_GOLD | 593 | 68.1% | 68.1% |  | 90% | ❌ 22 pts to go |
| P02 | 395 | 77.2% | 77.2% |  | 95% | ❌ 18 pts to go |
| P03 | 228 | 70.2% | 70.2% |  | 95% | ❌ 25 pts to go |
| P04 | 1583 | 63.2% | 63.2% |  | 90% | ❌ 27 pts to go |
| P05 | 379 | 78.6% | 78.6% |  | 95% | ❌ 16 pts to go |
| P06M | 168 | 84.5% | 84.5% |  | n/a | no target |
| P06T | 2440 | 93.4% | 93.4% |  | n/a | no target |
| P06 | 165 | 88.5% | 88.5% |  | 100% | ❌ 12 pts to go |
| P07 | 252 | 86.5% | 86.5% |  | 100% | ❌ 14 pts to go |
| P08 | 3038 | 90.2% | 90.2% |  | 100% | 🟡 10 pts to go |
| P09 | 373 | 52.5% | 52.5% |  | n/a | no target |
| P10 | 2597 | 89.3% | 89.3% |  | 100% | ❌ 11 pts to go |
| P11 | 488 | 32.4% | 32.4% |  | 80% | ❌ 48 pts to go |
| P12 | 21 | 61.9% | 61.9% |  | n/a | no target |
| P13 | 50793 | 83.9% | 83.9% |  | 95% | ❌ 11 pts to go |

## 4. AP

### `ap_contact_name_as_published`

> ceiling: owner 2026-11-08: the AP contact person the organisation itself names on its AP / finance page is allowed (name + role phrase, quoted); mailboxes stay organisational; many bodies publish no AP person

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 19 | 15.8% | 15.8% |  | n/a | no target |
| P01T | 92 | 23.9% | 23.9% |  | n/a | no target |
| P01_GOLD | 593 | 13.5% | 13.5% |  | 25% | ❌ 12 pts to go |
| P02 | 395 | 19.7% | 19.7% |  | 40% | ❌ 20 pts to go |
| P03 | 228 | 3.1% | 3.1% |  | 20% | ❌ 17 pts to go |
| P04 | 1583 | 3.5% | 3.5% |  | 20% | ❌ 16 pts to go |
| P05 | 379 | 1.6% | 1.6% |  | 15% | ❌ 13 pts to go |
| P06M | 168 | 1.8% | 1.8% |  | n/a | no target |
| P06T | 2440 | 1.1% | 1.1% |  | n/a | no target |
| P06 | 165 | 4.8% | 4.8% |  | n/a | no target |
| P07 | 252 | 5.2% | 5.2% |  | n/a | no target |
| P08 | 3038 | 0.0% | 0.0% |  | n/a | no target |
| P09 | 373 | 5.6% | 5.6% |  | n/a | no target |
| P10 | 2597 | 0.3% | 0.3% |  | n/a | no target |
| P11 | 488 | 1.0% | 1.0% |  | n/a | no target |
| P12 | 21 | 0.0% | 0.0% |  | n/a | no target |
| P13 | 50793 | 0.2% | 0.2% |  | n/a | no target |

### `ap_phone`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 19 | 36.8% | 36.8% |  | n/a | no target |
| P01T | 92 | 34.8% | 34.8% |  | 70% | ❌ 35 pts to go |
| P01_GOLD | 593 | 43.7% | 43.7% |  | 80% | ❌ 36 pts to go |
| P02 | 395 | 64.8% | 64.8% |  | 90% | ❌ 25 pts to go |
| P03 | 228 | 21.9% | 21.9% |  | 60% | ❌ 38 pts to go |
| P04 | 1583 | 50.2% | 50.2% |  | 85% | ❌ 35 pts to go |
| P05 | 379 | 12.9% | 12.9% |  | 50% | ❌ 37 pts to go |
| P06M | 168 | 6.0% | 6.0% |  | n/a | no target |
| P06T | 2440 | 2.3% | 2.3% |  | n/a | no target |
| P06 | 165 | 18.2% | 18.2% |  | n/a | no target |
| P07 | 252 | 19.0% | 19.0% |  | n/a | no target |
| P08 | 3038 | 0.5% | 0.5% |  | n/a | no target |
| P09 | 373 | 81.0% | 81.0% |  | 95% | ❌ 14 pts to go |
| P10 | 2597 | 3.1% | 3.1% |  | n/a | no target |
| P11 | 488 | 31.6% | 31.6% |  | n/a | no target |
| P12 | 21 | 33.3% | 33.3% |  | n/a | no target |
| P13 | 50793 | 1.0% | 1.0% |  | n/a | no target |

### `invoice_mailing_address`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 19 | 0.0% | 0.0% |  | n/a | no target |
| P01T | 92 | 16.3% | 16.3% |  | n/a | no target |
| P01_GOLD | 593 | 33.9% | 33.9% |  | 70% | ❌ 36 pts to go |
| P02 | 395 | 43.0% | 43.0% |  | 75% | ❌ 32 pts to go |
| P03 | 228 | 21.5% | 21.5% |  | 55% | ❌ 34 pts to go |
| P04 | 1583 | 49.8% | 49.8% |  | 75% | ❌ 25 pts to go |
| P05 | 379 | 11.1% | 11.1% |  | 50% | ❌ 39 pts to go |
| P06M | 168 | 1.8% | 1.8% |  | n/a | no target |
| P06T | 2440 | 1.1% | 1.1% |  | n/a | no target |
| P06 | 165 | 10.3% | 10.3% |  | n/a | no target |
| P07 | 252 | 10.3% | 10.3% |  | n/a | no target |
| P08 | 3038 | 0.5% | 0.5% |  | n/a | no target |
| P09 | 373 | 77.5% | 77.5% |  | 95% | ❌ 18 pts to go |
| P10 | 2597 | 1.8% | 1.8% |  | n/a | no target |
| P11 | 488 | 30.5% | 30.5% |  | n/a | no target |
| P12 | 21 | 19.0% | 19.0% |  | n/a | no target |
| P13 | 50793 | 0.6% | 0.6% |  | n/a | no target |

### `invoicing_requirements`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 19 | 21.1% | 21.1% |  | n/a | no target |
| P01T | 92 | 18.5% | 18.5% |  | n/a | no target |
| P01_GOLD | 593 | 55.1% | 55.3% |  | 80% | ❌ 25 pts to go |
| P02 | 395 | 45.3% | 45.3% |  | 75% | ❌ 30 pts to go |
| P03 | 228 | 32.9% | 32.9% |  | 70% | ❌ 37 pts to go |
| P04 | 1583 | 39.0% | 39.0% |  | 70% | ❌ 31 pts to go |
| P05 | 379 | 14.5% | 14.5% |  | 50% | ❌ 36 pts to go |
| P06M | 168 | 0.6% | 0.6% |  | n/a | no target |
| P06T | 2440 | 1.0% | 1.0% |  | n/a | no target |
| P06 | 165 | 21.2% | 21.2% |  | n/a | no target |
| P07 | 252 | 2.4% | 2.4% |  | n/a | no target |
| P08 | 3038 | 0.4% | 0.4% |  | n/a | no target |
| P09 | 373 | 41.8% | 41.8% |  | 80% | ❌ 38 pts to go |
| P10 | 2597 | 1.2% | 1.2% |  | n/a | no target |
| P11 | 488 | 17.0% | 17.0% |  | n/a | no target |
| P12 | 21 | 33.3% | 33.3% |  | n/a | no target |
| P13 | 50793 | 0.3% | 0.3% |  | n/a | no target |

### `payment_terms_as_published`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 19 | 36.8% | 36.8% |  | n/a | no target |
| P01T | 92 | 54.3% | 54.3% |  | 60% | 🟡 6 pts to go |
| P01_GOLD | 593 | 57.3% | 57.3% |  | 70% | ❌ 13 pts to go |
| P02 | 395 | 10.6% | 10.6% |  | 50% | ❌ 39 pts to go |
| P03 | 228 | 16.7% | 16.7% |  | 55% | ❌ 38 pts to go |
| P04 | 1583 | 13.6% | 13.6% |  | 40% | ❌ 26 pts to go |
| P05 | 379 | 9.8% | 9.8% |  | 40% | ❌ 30 pts to go |
| P06M | 168 | 0.6% | 0.6% |  | n/a | no target |
| P06T | 2440 | 3.1% | 3.1% |  | n/a | no target |
| P06 | 165 | 25.5% | 25.5% |  | n/a | no target |
| P07 | 252 | 6.0% | 6.0% |  | n/a | no target |
| P08 | 3038 | 0.5% | 0.5% |  | n/a | no target |
| P09 | 373 | 3.8% | 3.8% |  | n/a | no target |
| P10 | 2597 | 0.7% | 0.7% |  | n/a | no target |
| P11 | 488 | 3.7% | 3.7% |  | n/a | no target |
| P12 | 21 | 9.5% | 9.5% |  | n/a | no target |
| P13 | 50793 | 0.3% | 0.3% |  | n/a | no target |

### `po_required_as_published`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 19 | 42.1% | 42.1% |  | n/a | no target |
| P01T | 92 | 68.5% | 68.5% |  | 65% | ✅ met |
| P01_GOLD | 593 | 66.6% | 66.6% |  | 70% | 🟡 3 pts to go |
| P02 | 395 | 7.6% | 7.6% |  | 50% | ❌ 42 pts to go |
| P03 | 228 | 27.6% | 27.6% |  | 60% | ❌ 32 pts to go |
| P04 | 1583 | 6.9% | 6.9% |  | 40% | ❌ 33 pts to go |
| P05 | 379 | 15.8% | 15.8% |  | 45% | ❌ 29 pts to go |
| P06M | 168 | 1.2% | 1.2% |  | n/a | no target |
| P06T | 2440 | 1.6% | 1.6% |  | n/a | no target |
| P06 | 165 | 44.8% | 44.8% |  | n/a | no target |
| P07 | 252 | 11.5% | 11.5% |  | n/a | no target |
| P08 | 3038 | 0.3% | 0.3% |  | n/a | no target |
| P09 | 373 | 5.4% | 5.4% |  | n/a | no target |
| P10 | 2597 | 0.9% | 0.9% |  | n/a | no target |
| P11 | 488 | 3.9% | 3.9% |  | n/a | no target |
| P12 | 21 | 4.8% | 4.8% |  | n/a | no target |
| P13 | 50793 | 0.2% | 0.2% |  | n/a | no target |

### `invoice_portal_url`

> ceiling: only portals the buyer names on its own pages; informational tax-authority links are not portals

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 19 | 15.8% | 15.8% |  | n/a | no target |
| P01T | 92 | 42.4% | 42.4% |  | n/a | no target |
| P01_GOLD | 593 | 46.7% | 46.7% |  | 50% | 🟡 3 pts to go |
| P02 | 395 | 25.3% | 25.3% |  | n/a | no target |
| P03 | 228 | 50.0% | 50.0% |  | 60% | 🟡 10 pts to go |
| P04 | 1583 | 19.6% | 19.6% |  | n/a | no target |
| P05 | 379 | 14.8% | 14.8% |  | n/a | no target |
| P06M | 168 | 2.4% | 2.4% |  | n/a | no target |
| P06T | 2440 | 2.3% | 2.3% |  | n/a | no target |
| P06 | 165 | 32.1% | 32.1% |  | n/a | no target |
| P07 | 252 | 13.1% | 13.1% |  | n/a | no target |
| P08 | 3038 | 0.5% | 0.5% |  | n/a | no target |
| P09 | 373 | 12.1% | 12.1% |  | n/a | no target |
| P10 | 2597 | 1.5% | 1.5% |  | n/a | no target |
| P11 | 488 | 5.1% | 5.1% |  | n/a | no target |
| P12 | 21 | 4.8% | 4.8% |  | n/a | no target |
| P13 | 50793 | 0.4% | 0.4% |  | n/a | no target |

### `buyer_payment_method_preference`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 19 | 31.6% | 31.6% |  | 15% | ✅ met |
| P01T | 92 | 29.3% | 29.3% |  | 15% | ✅ met |
| P01_GOLD | 593 | 34.9% | 34.9% |  | 40% | 🟡 5 pts to go |
| P02 | 395 | 8.6% | 8.9% |  | 25% | ❌ 16 pts to go |
| P03 | 228 | 12.7% | 12.7% |  | 25% | ❌ 12 pts to go |
| P04 | 1583 | 4.0% | 4.0% |  | 15% | ❌ 11 pts to go |
| P05 | 379 | 6.3% | 6.3% |  | 15% | 🟡 9 pts to go |
| P06M | 168 | 3.0% | 3.0% |  | 15% | ❌ 12 pts to go |
| P06T | 2440 | 1.2% | 1.2% |  | 15% | ❌ 14 pts to go |
| P06 | 165 | 9.1% | 9.1% |  | 15% | 🟡 6 pts to go |
| P07 | 252 | 4.0% | 4.0% |  | 15% | ❌ 11 pts to go |
| P08 | 3038 | 0.8% | 0.8% |  | 15% | ❌ 14 pts to go |
| P09 | 373 | 0.8% | 0.8% |  | 15% | ❌ 14 pts to go |
| P10 | 2597 | 1.0% | 1.0% |  | 15% | ❌ 14 pts to go |
| P11 | 488 | 1.2% | 1.2% |  | 15% | ❌ 14 pts to go |
| P12 | 21 | 0.0% | 0.0% |  | 15% | ❌ 15 pts to go |
| P13 | 50793 | 0.9% | 0.9% |  | 15% | ❌ 14 pts to go |

### `buyer_tax_exempt_status`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 19 | 10.5% | 10.5% |  | 15% | 🟡 4 pts to go |
| P01T | 92 | 31.5% | 31.5% |  | 25% | ✅ met |
| P01_GOLD | 593 | 25.5% | 25.5% |  | 25% | ✅ met |
| P02 | 395 | 7.1% | 7.1% |  | 15% | 🟡 8 pts to go |
| P03 | 228 | 3.5% | 3.5% |  | 15% | ❌ 12 pts to go |
| P04 | 1583 | 5.4% | 5.4% |  | 15% | 🟡 10 pts to go |
| P05 | 379 | 9.8% | 9.8% |  | 15% | 🟡 5 pts to go |
| P06M | 168 | 0.6% | 0.6% |  | 15% | ❌ 14 pts to go |
| P06T | 2440 | 0.9% | 0.9% |  | 15% | ❌ 14 pts to go |
| P06 | 165 | 9.1% | 9.1% |  | 15% | 🟡 6 pts to go |
| P07 | 252 | 4.8% | 4.8% |  | 15% | ❌ 10 pts to go |
| P08 | 3038 | 0.2% | 0.2% |  | 15% | ❌ 15 pts to go |
| P09 | 373 | 0.5% | 0.5% |  | 15% | ❌ 14 pts to go |
| P10 | 2597 | 0.3% | 0.3% |  | 15% | ❌ 15 pts to go |
| P11 | 488 | 3.1% | 3.1% |  | 15% | ❌ 12 pts to go |
| P12 | 21 | 9.5% | 9.5% |  | 15% | 🟡 6 pts to go |
| P13 | 50793 | 0.1% | 0.1% |  | 15% | ❌ 15 pts to go |

### `buyer_ap_cycle_published`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 19 | 5.3% | 5.3% |  | 20% | ❌ 15 pts to go |
| P01T | 92 | 9.8% | 9.8% |  | 20% | ❌ 10 pts to go |
| P01_GOLD | 593 | 4.2% | 4.2% |  | 20% | ❌ 16 pts to go |
| P02 | 395 | 0.3% | 0.3% |  | 20% | ❌ 20 pts to go |
| P03 | 228 | 0.0% | 0.0% |  | 20% | ❌ 20 pts to go |
| P04 | 1583 | 0.5% | 0.5% |  | 20% | ❌ 20 pts to go |
| P05 | 379 | 0.8% | 0.8% |  | 20% | ❌ 19 pts to go |
| P06M | 168 | 0.0% | 0.0% |  | 20% | ❌ 20 pts to go |
| P06T | 2440 | 0.2% | 0.2% |  | 20% | ❌ 20 pts to go |
| P06 | 165 | 3.6% | 3.6% |  | 20% | ❌ 16 pts to go |
| P07 | 252 | 0.4% | 0.4% |  | 20% | ❌ 20 pts to go |
| P08 | 3038 | 0.1% | 0.1% |  | 20% | ❌ 20 pts to go |
| P09 | 373 | 0.0% | 0.0% |  | 20% | ❌ 20 pts to go |
| P10 | 2597 | 0.1% | 0.1% |  | 20% | ❌ 20 pts to go |
| P11 | 488 | 0.6% | 0.6% |  | 20% | ❌ 19 pts to go |
| P12 | 21 | 0.0% | 0.0% |  | 20% | ❌ 20 pts to go |
| P13 | 50793 | 0.0% | 0.0% |  | 20% | ❌ 20 pts to go |

### `buyer_esignature_preference`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 19 | 5.3% | 5.3% |  | 15% | 🟡 10 pts to go |
| P01T | 92 | 7.6% | 7.6% |  | 15% | 🟡 7 pts to go |
| P01_GOLD | 593 | 8.8% | 8.8% |  | 15% | 🟡 6 pts to go |
| P02 | 395 | 3.0% | 3.0% |  | 15% | ❌ 12 pts to go |
| P03 | 228 | 5.7% | 5.7% |  | 15% | 🟡 9 pts to go |
| P04 | 1583 | 3.3% | 3.3% |  | 15% | ❌ 12 pts to go |
| P05 | 379 | 1.8% | 1.8% |  | 15% | ❌ 13 pts to go |
| P06M | 168 | 0.0% | 0.0% |  | 15% | ❌ 15 pts to go |
| P06T | 2440 | 0.3% | 0.3% |  | 15% | ❌ 15 pts to go |
| P06 | 165 | 4.2% | 4.2% |  | 15% | ❌ 11 pts to go |
| P07 | 252 | 0.4% | 0.4% |  | 15% | ❌ 15 pts to go |
| P08 | 3038 | 0.2% | 0.2% |  | 15% | ❌ 15 pts to go |
| P09 | 373 | 0.3% | 0.3% |  | 15% | ❌ 15 pts to go |
| P10 | 2597 | 0.2% | 0.2% |  | 15% | ❌ 15 pts to go |
| P11 | 488 | 0.8% | 0.8% |  | 15% | ❌ 14 pts to go |
| P12 | 21 | 0.0% | 0.0% |  | 15% | ❌ 15 pts to go |
| P13 | 50793 | 0.1% | 0.1% |  | 15% | ❌ 15 pts to go |

### `ap_system_hint`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 19 | 15.8% | 15.8% |  | 20% | 🟡 4 pts to go |
| P01T | 92 | 39.1% | 39.1% |  | 40% | 🟡 1 pts to go |
| P01_GOLD | 593 | 41.7% | 41.7% |  | 40% | ✅ met |
| P02 | 395 | 28.1% | 28.1% |  | 20% | ✅ met |
| P03 | 228 | 39.5% | 39.5% |  | 35% | ✅ met |
| P04 | 1583 | 22.8% | 22.8% |  | 20% | ✅ met |
| P05 | 379 | 13.5% | 13.5% |  | 20% | 🟡 6 pts to go |
| P06M | 168 | 2.4% | 2.4% |  | 20% | ❌ 18 pts to go |
| P06T | 2440 | 2.4% | 2.4% |  | 20% | ❌ 18 pts to go |
| P06 | 165 | 29.7% | 29.7% |  | 20% | ✅ met |
| P07 | 252 | 11.1% | 11.1% |  | 20% | 🟡 9 pts to go |
| P08 | 3038 | 0.9% | 0.9% |  | 20% | ❌ 19 pts to go |
| P09 | 373 | 16.9% | 16.9% |  | 20% | 🟡 3 pts to go |
| P10 | 2597 | 1.7% | 1.7% |  | 20% | ❌ 18 pts to go |
| P11 | 488 | 6.6% | 6.6% |  | 20% | ❌ 13 pts to go |
| P12 | 21 | 0.0% | 0.0% |  | 20% | ❌ 20 pts to go |
| P13 | 50793 | 0.5% | 0.5% |  | 20% | ❌ 20 pts to go |

## 5. contract

### `contract_value`

> ceiling: rows proven by a lobbying filing, a news release, an auditor appointment, a customer story or a vendor's client list have no contract value by nature (≈17 % of P01 Gold); bids&tenders awards now carry the awarded bidder's submitted price when no award value was published

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 19 | 0.0% | 0.0% |  | n/a | no target |
| P01T | 92 | 1.1% | 1.1% |  | n/a | no target |
| P01_GOLD | 593 | 70.7% | 70.7% |  | 95% | ❌ 24 pts to go |
| P02 | 395 | 73.2% | 73.2% |  | 95% | ❌ 22 pts to go |
| P03 | 228 | 63.6% | 63.6% |  | 90% | ❌ 26 pts to go |
| P04 | 1583 | 58.6% | 58.6% |  | 85% | ❌ 26 pts to go |
| P05 | 379 | 34.3% | 34.3% |  | 75% | ❌ 41 pts to go |
| P06M | 168 | 0.0% | 0.0% |  | n/a | no target |
| P06T | 2440 | 0.0% | 0.0% |  | n/a | no target |
| P06 | 165 | 0.0% | 0.0% |  | n/a | no target |
| P07 | 252 | 0.0% | 0.0% |  | n/a | no target |
| P08 | 3038 | 0.0% | 0.0% |  | n/a | no target |
| P09 | 373 | 90.9% | 90.9% |  | 100% | 🟡 9 pts to go |
| P10 | 2597 | 0.0% | 0.0% |  | n/a | no target |
| P11 | 488 | 20.7% | 20.7% |  | 60% | ❌ 39 pts to go |
| P12 | 21 | 100.0% | 100.0% |  | n/a | no target |
| P13 | 50793 | 0.0% | 0.0% |  | n/a | no target |

### `currency`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 19 | 0.0% | 0.0% |  | n/a | no target |
| P01T | 92 | 0.0% | 0.0% |  | n/a | no target |
| P01_GOLD | 593 | 74.2% | 74.2% |  | 100% | ❌ 26 pts to go |
| P02 | 395 | 76.7% | 76.7% |  | 100% | ❌ 23 pts to go |
| P03 | 228 | 71.1% | 71.1% |  | n/a | no target |
| P04 | 1583 | 59.9% | 59.9% |  | 95% | ❌ 35 pts to go |
| P05 | 379 | 30.6% | 30.6% |  | 80% | ❌ 49 pts to go |
| P06M | 168 | 0.0% | 0.0% |  | n/a | no target |
| P06T | 2440 | 0.0% | 0.0% |  | n/a | no target |
| P06 | 165 | 0.0% | 0.0% |  | n/a | no target |
| P07 | 252 | 0.0% | 0.0% |  | n/a | no target |
| P08 | 3038 | 0.0% | 0.0% |  | n/a | no target |
| P09 | 373 | 93.6% | 93.6% |  | 100% | 🟡 6 pts to go |
| P10 | 2597 | 0.0% | 0.0% |  | n/a | no target |
| P11 | 488 | 21.9% | 21.9% |  | n/a | no target |
| P12 | 21 | 100.0% | 100.0% |  | n/a | no target |
| P13 | 50793 | 0.0% | 0.0% |  | n/a | no target |

### `start_date`

> ceiling: most award notices publish an award date, not a start date; start_date carries the signature date when the source gives one, labelled

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 19 | 0.0% | 0.0% |  | n/a | no target |
| P01T | 92 | 1.1% | 1.1% |  | n/a | no target |
| P01_GOLD | 593 | 53.5% | 53.5% |  | 85% | ❌ 32 pts to go |
| P02 | 395 | 64.8% | 64.8% |  | 90% | ❌ 25 pts to go |
| P03 | 228 | 52.2% | 52.2% |  | 85% | ❌ 33 pts to go |
| P04 | 1583 | 63.9% | 63.9% |  | 90% | ❌ 26 pts to go |
| P05 | 379 | 35.1% | 35.1% |  | 75% | ❌ 40 pts to go |
| P06M | 168 | 0.0% | 0.0% |  | n/a | no target |
| P06T | 2440 | 0.0% | 0.0% |  | n/a | no target |
| P06 | 165 | 0.0% | 0.0% |  | n/a | no target |
| P07 | 252 | 0.0% | 0.0% |  | n/a | no target |
| P08 | 3038 | 0.0% | 0.0% |  | n/a | no target |
| P09 | 373 | 85.0% | 85.0% |  | 95% | 🟡 10 pts to go |
| P10 | 2597 | 0.0% | 0.0% |  | n/a | no target |
| P11 | 488 | 19.9% | 19.9% |  | n/a | no target |
| P12 | 21 | 0.0% | 0.0% |  | n/a | no target |
| P13 | 50793 | 0.0% | 0.0% |  | n/a | no target |

### `end_date`

> ceiling: an inferred end (award date + published duration) is labelled as such; sources without a duration leave end_date empty — the honest ceiling. P09 is BY DEFINITION the rows whose end date is not published (older SEAO contracts with no closing notice): its end_date / duration targets cannot be met without inventing a date

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 19 | 0.0% | 0.0% |  | n/a | no target |
| P01T | 92 | 1.1% | 1.1% |  | n/a | no target |
| P01_GOLD | 593 | 54.1% | 54.1% |  | 85% | ❌ 31 pts to go |
| P02 | 395 | 60.0% | 60.0% |  | 90% | ❌ 30 pts to go |
| P03 | 228 | 53.1% | 53.1% |  | 85% | ❌ 32 pts to go |
| P04 | 1583 | 53.8% | 53.8% |  | 90% | ❌ 36 pts to go |
| P05 | 379 | 42.2% | 42.2% |  | 75% | ❌ 33 pts to go |
| P06M | 168 | 0.0% | 0.0% |  | n/a | no target |
| P06T | 2440 | 0.0% | 0.0% |  | n/a | no target |
| P06 | 165 | 0.0% | 0.0% |  | n/a | no target |
| P07 | 252 | 0.0% | 0.0% |  | n/a | no target |
| P08 | 3038 | 0.0% | 0.0% |  | n/a | no target |
| P09 | 373 | 0.3% | 0.3% |  | 95% | ❌ 95 pts to go |
| P10 | 2597 | 0.0% | 0.0% |  | n/a | no target |
| P11 | 488 | 16.0% | 16.0% |  | n/a | no target |
| P12 | 21 | 0.0% | 0.0% |  | n/a | no target |
| P13 | 50793 | 0.0% | 0.0% |  | n/a | no target |

### `contract_title`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 19 | 0.0% | 0.0% |  | n/a | no target |
| P01T | 92 | 81.5% | 81.5% |  | n/a | no target |
| P01_GOLD | 593 | 86.5% | 86.5% |  | 100% | ❌ 14 pts to go |
| P02 | 395 | 80.3% | 80.3% |  | 100% | ❌ 20 pts to go |
| P03 | 228 | 91.2% | 91.2% |  | n/a | no target |
| P04 | 1583 | 72.6% | 72.6% |  | 95% | ❌ 22 pts to go |
| P05 | 379 | 75.2% | 75.2% |  | 95% | ❌ 20 pts to go |
| P06M | 168 | 0.6% | 0.6% |  | n/a | no target |
| P06T | 2440 | 83.4% | 83.4% |  | n/a | no target |
| P06 | 165 | 75.8% | 75.8% |  | n/a | no target |
| P07 | 252 | 77.0% | 77.0% |  | n/a | no target |
| P08 | 3038 | 84.9% | 85.0% |  | n/a | no target |
| P09 | 373 | 98.9% | 98.9% |  | 100% | 🟡 1 pts to go |
| P10 | 2597 | 98.4% | 98.4% |  | n/a | no target |
| P11 | 488 | 90.2% | 90.2% |  | n/a | no target |
| P12 | 21 | 100.0% | 100.0% |  | n/a | no target |
| P13 | 50793 | 0.0% | 0.0% |  | n/a | no target |

### `contract_description`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 19 | 0.0% | 0.0% |  | n/a | no target |
| P01T | 92 | 81.5% | 81.5% |  | n/a | no target |
| P01_GOLD | 593 | 89.9% | 89.9% |  | 100% | ❌ 10 pts to go |
| P02 | 395 | 81.5% | 81.8% |  | 100% | ❌ 18 pts to go |
| P03 | 228 | 92.1% | 92.1% |  | n/a | no target |
| P04 | 1583 | 79.0% | 79.0% |  | 95% | ❌ 16 pts to go |
| P05 | 379 | 90.0% | 90.0% |  | 70% | ✅ met |
| P06M | 168 | 0.6% | 0.6% |  | n/a | no target |
| P06T | 2440 | 83.4% | 83.4% |  | n/a | no target |
| P06 | 165 | 75.8% | 75.8% |  | n/a | no target |
| P07 | 252 | 77.0% | 77.0% |  | n/a | no target |
| P08 | 3038 | 84.9% | 85.0% |  | n/a | no target |
| P09 | 373 | 98.9% | 98.9% |  | 100% | 🟡 1 pts to go |
| P10 | 2597 | 98.4% | 98.4% |  | n/a | no target |
| P11 | 488 | 90.6% | 90.6% |  | n/a | no target |
| P12 | 21 | 100.0% | 100.0% |  | n/a | no target |
| P13 | 50793 | 0.0% | 0.0% |  | n/a | no target |

### `number_of_bids`

> ceiling: published by some portals only (bids&tenders submission lists, Biddingo bidder lists); federal proactive disclosure does not publish bid counts

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 19 | 0.0% | 0.0% |  | n/a | no target |
| P01T | 92 | 1.1% | 1.1% |  | n/a | no target · rows from a source that publishes bids: 3 rows, 33.3% filled |
| P01_GOLD | 593 | 17.9% | 17.9% |  | 60% | ❌ 42 pts to go · rows from a source that publishes bids: 360 rows, 29.4% filled |
| P02 | 395 | 13.4% | 13.4% |  | n/a | no target · rows from a source that publishes bids: 282 rows, 18.8% filled |
| P03 | 228 | 15.4% | 15.4% |  | n/a | no target · rows from a source that publishes bids: 142 rows, 24.6% filled |
| P04 | 1583 | 3.7% | 3.7% |  | n/a | no target · rows from a source that publishes bids: 882 rows, 6.6% filled |
| P05 | 379 | 3.4% | 3.4% |  | n/a | no target · rows from a source that publishes bids: 48 rows, 27.1% filled |
| P06M | 168 | 0.0% | 0.0% |  | n/a | no target |
| P06T | 2440 | 0.1% | 0.1% |  | n/a | no target · rows from a source that publishes bids: 4 rows, 50.0% filled |
| P06 | 165 | 0.0% | 0.0% |  | n/a | no target |
| P07 | 252 | 0.0% | 0.0% |  | n/a | no target |
| P08 | 3038 | 0.0% | 0.0% |  | n/a | no target |
| P09 | 373 | 3.2% | 3.2% |  | n/a | no target · rows from a source that publishes bids: 359 rows, 3.3% filled |
| P10 | 2597 | 0.0% | 0.0% |  | n/a | no target |
| P11 | 488 | 2.9% | 2.9% |  | n/a | no target · rows from a source that publishes bids: 104 rows, 13.5% filled |
| P12 | 21 | 0.0% | 0.0% |  | n/a | no target · rows from a source that publishes bids: 21 rows, 0.0% filled |
| P13 | 50793 | 0.0% | 0.0% |  | n/a | no target |

## 6. history

### `average_contract_duration_days`

> ceiling: needs two dates (or a published term) on the buyer's records; P09 rows (end date unpublished by definition) and buyers whose sources publish award dates only have no honest duration

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 19 | 0.0% | 100.0% |  | n/a | no target |
| P01T | 92 | 0.0% | 96.7% |  | n/a | no target |
| P01_GOLD | 593 | 55.1% | 82.5% |  | 90% | ❌ 35 pts to go |
| P02 | 395 | 60.0% | 86.1% |  | 90% | ❌ 30 pts to go |
| P03 | 228 | 53.1% | 77.6% |  | 90% | ❌ 37 pts to go |
| P04 | 1583 | 44.8% | 85.1% |  | 90% | ❌ 45 pts to go |
| P05 | 379 | 0.0% | 82.1% |  | 90% | ❌ 90 pts to go |
| P06M | 168 | 0.0% | 100.0% |  | n/a | no target |
| P06T | 2440 | 0.0% | 99.8% |  | n/a | no target |
| P06 | 165 | 0.0% | 100.0% |  | n/a | no target |
| P07 | 252 | 0.0% | 100.0% |  | n/a | no target |
| P08 | 3038 | 0.0% | 100.0% |  | n/a | no target |
| P09 | 373 | 1.3% | 2.7% |  | 90% | ❌ 89 pts to go |
| P10 | 2597 | 0.0% | 100.0% |  | n/a | no target |
| P11 | 488 | 15.0% | 90.6% |  | n/a | no target |
| P12 | 21 | 0.0% | 100.0% |  | n/a | no target |
| P13 | 50793 | 0.0% | 100.0% |  | n/a | no target |

### `commodity_distribution_top3`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 19 | 0.0% | 100.0% |  | n/a | no target |
| P01T | 92 | 0.0% | 96.7% |  | n/a | no target |
| P01_GOLD | 593 | 27.3% | 54.6% |  | 90% | ❌ 63 pts to go |
| P02 | 395 | 58.0% | 84.1% |  | n/a | no target |
| P03 | 228 | 28.5% | 53.1% |  | n/a | no target |
| P04 | 1583 | 49.6% | 89.9% |  | n/a | no target |
| P05 | 379 | 0.3% | 82.3% |  | n/a | no target |
| P06M | 168 | 0.0% | 100.0% |  | n/a | no target |
| P06T | 2440 | 0.0% | 99.8% |  | n/a | no target |
| P06 | 165 | 0.0% | 100.0% |  | n/a | no target |
| P07 | 252 | 0.0% | 100.0% |  | n/a | no target |
| P08 | 3038 | 0.0% | 100.0% |  | n/a | no target |
| P09 | 373 | 45.3% | 46.6% |  | n/a | no target |
| P10 | 2597 | 0.0% | 100.0% |  | n/a | no target |
| P11 | 488 | 12.5% | 88.1% |  | n/a | no target |
| P12 | 21 | 0.0% | 100.0% |  | n/a | no target |
| P13 | 50793 | 0.0% | 100.0% |  | n/a | no target |

### `year_over_year_spend_trend`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 19 | 0.0% | 100.0% |  | n/a | no target |
| P01T | 92 | 2.2% | 98.9% |  | n/a | no target |
| P01_GOLD | 593 | 53.6% | 80.9% |  | 95% | ❌ 41 pts to go |
| P02 | 395 | 64.1% | 90.1% |  | n/a | no target |
| P03 | 228 | 57.9% | 82.5% |  | n/a | no target |
| P04 | 1583 | 50.2% | 90.5% |  | n/a | no target |
| P05 | 379 | 4.5% | 86.5% |  | n/a | no target |
| P06M | 168 | 0.0% | 100.0% |  | n/a | no target |
| P06T | 2440 | 0.0% | 99.8% |  | n/a | no target |
| P06 | 165 | 0.0% | 100.0% |  | n/a | no target |
| P07 | 252 | 0.0% | 100.0% |  | n/a | no target |
| P08 | 3038 | 0.0% | 100.0% |  | n/a | no target |
| P09 | 373 | 68.9% | 70.2% |  | n/a | no target |
| P10 | 2597 | 0.0% | 100.0% |  | n/a | no target |
| P11 | 488 | 13.5% | 89.1% |  | n/a | no target |
| P12 | 21 | 0.0% | 100.0% |  | n/a | no target |
| P13 | 50793 | 0.0% | 100.0% |  | n/a | no target |

## 7. mail security

### `mta_sts`

> ceiling: DNS-only check; 'no record' counts as checked

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 19 | 100.0% | 100.0% |  | 100% | ✅ met |
| P01T | 92 | 100.0% | 100.0% |  | 100% | ✅ met |
| P01_GOLD | 593 | 100.0% | 100.0% |  | 100% | ✅ met |
| P02 | 395 | 100.0% | 100.0% |  | 100% | ✅ met |
| P03 | 228 | 100.0% | 100.0% |  | 100% | ✅ met |
| P04 | 1583 | 100.0% | 100.0% |  | 100% | ✅ met |
| P05 | 379 | 100.0% | 100.0% |  | 100% | ✅ met |
| P06M | 168 | 100.0% | 100.0% |  | 100% | ✅ met |
| P06T | 2440 | 100.0% | 100.0% |  | 100% | ✅ met |
| P06 | 165 | 100.0% | 100.0% |  | 100% | ✅ met |
| P07 | 252 | 100.0% | 100.0% |  | 100% | ✅ met |
| P08 | 3038 | 100.0% | 100.0% |  | 100% | ✅ met |
| P09 | 373 | 100.0% | 100.0% |  | 100% | ✅ met |
| P10 | 2597 | 100.0% | 100.0% |  | 100% | ✅ met |
| P11 | 488 | 100.0% | 100.0% |  | 100% | ✅ met |
| P12 | 21 | 100.0% | 100.0% |  | 100% | ✅ met |
| P13 | 50793 | 100.0% | 100.0% |  | 100% | ✅ met |

### `tls_rpt`

> ceiling: DNS-only check; 'no record' counts as checked

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 19 | 100.0% | 100.0% |  | 100% | ✅ met |
| P01T | 92 | 100.0% | 100.0% |  | 100% | ✅ met |
| P01_GOLD | 593 | 100.0% | 100.0% |  | 100% | ✅ met |
| P02 | 395 | 100.0% | 100.0% |  | 100% | ✅ met |
| P03 | 228 | 100.0% | 100.0% |  | 100% | ✅ met |
| P04 | 1583 | 100.0% | 100.0% |  | 100% | ✅ met |
| P05 | 379 | 100.0% | 100.0% |  | 100% | ✅ met |
| P06M | 168 | 100.0% | 100.0% |  | 100% | ✅ met |
| P06T | 2440 | 100.0% | 100.0% |  | 100% | ✅ met |
| P06 | 165 | 100.0% | 100.0% |  | 100% | ✅ met |
| P07 | 252 | 100.0% | 100.0% |  | 100% | ✅ met |
| P08 | 3038 | 100.0% | 100.0% |  | 100% | ✅ met |
| P09 | 373 | 100.0% | 100.0% |  | 100% | ✅ met |
| P10 | 2597 | 100.0% | 100.0% |  | 100% | ✅ met |
| P11 | 488 | 100.0% | 100.0% |  | 100% | ✅ met |
| P12 | 21 | 100.0% | 100.0% |  | 100% | ✅ met |
| P13 | 50793 | 100.0% | 100.0% |  | 100% | ✅ met |

### `bimi`

> ceiling: DNS-only check; 'no record' counts as checked

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 19 | 100.0% | 100.0% |  | 100% | ✅ met |
| P01T | 92 | 100.0% | 100.0% |  | 100% | ✅ met |
| P01_GOLD | 593 | 100.0% | 100.0% |  | 100% | ✅ met |
| P02 | 395 | 100.0% | 100.0% |  | 100% | ✅ met |
| P03 | 228 | 100.0% | 100.0% |  | 100% | ✅ met |
| P04 | 1583 | 100.0% | 100.0% |  | 100% | ✅ met |
| P05 | 379 | 100.0% | 100.0% |  | 100% | ✅ met |
| P06M | 168 | 100.0% | 100.0% |  | 100% | ✅ met |
| P06T | 2440 | 100.0% | 100.0% |  | 100% | ✅ met |
| P06 | 165 | 100.0% | 100.0% |  | 100% | ✅ met |
| P07 | 252 | 100.0% | 100.0% |  | 100% | ✅ met |
| P08 | 3038 | 100.0% | 100.0% |  | 100% | ✅ met |
| P09 | 373 | 100.0% | 100.0% |  | 100% | ✅ met |
| P10 | 2597 | 100.0% | 100.0% |  | 100% | ✅ met |
| P11 | 488 | 100.0% | 100.0% |  | 100% | ✅ met |
| P12 | 21 | 100.0% | 100.0% |  | 100% | ✅ met |
| P13 | 50793 | 100.0% | 100.0% |  | 100% | ✅ met |

