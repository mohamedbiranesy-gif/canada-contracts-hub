# Coverage vs the downstream team's targets — 2026-11-08

Benchmarks (field × package with a numeric target): **94 of 438 met** (21.5%); 65 within 10 points; 279 further away.
A cell counts as filled only when it carries a value: blank, `not_published`, `not_found_yet` and label-only cells ("no identifier published …", "no dataset record …", "0 in the contract dataset …") do not count; the DNS checks count when checked. `any` = share of non-blank cells incl. such labels. Δ = change since the previous build in `coord/results/coverage_history.csv`.
Rows per package: P01M 19, P01T 92, P01_GOLD 596, P02 399, P03 223, P04 1580, P05 379, P06M 168, P06T 2440, P06 165, P07 252, P08 3038, P09 374, P10 2597, P11 478, P12 21, P13 50793

## Invoice-grade readiness (the row as an invoice header: bill-to, submit-to, references, terms, tax, vendor identity, follow-up)

| package | rows | all 11 elements | ≥ 9 of 11 | median elements | most-missing element |
|---|---|---|---|---|---|
| P01M | 19 | 0.0% | 26.3% | 7 | reference to quote (PO / contract / vendor id) (19 rows) |
| P01T | 92 | 0.0% | 27.2% | 8 | reference to quote (PO / contract / vendor id) (87 rows) |
| P01_GOLD | 596 | 12.8% | 60.2% | 9 | buyer tax status (287 rows) |
| P02 | 399 | 1.3% | 41.4% | 8 | PO rule (368 rows) |
| P03 | 223 | 3.1% | 35.0% | 8 | buyer tax status (162 rows) |
| P04 | 1580 | 1.3% | 25.5% | 8 | PO rule (1458 rows) |
| P05 | 379 | 0.3% | 6.3% | 6 | payment terms (339 rows) |
| P06M | 168 | 0.0% | 0.0% | 6 | reference to quote (PO / contract / vendor id) (168 rows) |
| P06T | 2440 | 0.0% | 0.5% | 5 | reference to quote (PO / contract / vendor id) (2436 rows) |
| P06 | 165 | 0.0% | 3.6% | 5 | reference to quote (PO / contract / vendor id) (165 rows) |
| P07 | 252 | 0.0% | 0.0% | 5 | reference to quote (PO / contract / vendor id) (252 rows) |
| P08 | 3038 | 0.0% | 0.0% | 5 | reference to quote (PO / contract / vendor id) (3038 rows) |
| P09 | 374 | 0.0% | 35.3% | 8 | payment terms (356 rows) |
| P10 | 2597 | 0.0% | 0.2% | 4 | reference to quote (PO / contract / vendor id) (2595 rows) |
| P11 | 478 | 0.4% | 8.4% | 3 | PO rule (461 rows) |
| P12 | 21 | 0.0% | 33.3% | 8 | PO rule (20 rows) |
| P13 | 50793 | 0.0% | 0.0% | 5 | reference to quote (PO / contract / vendor id) (50793 rows) |

## AP grade (how stringently the row's accounts-payable data meets what an invoice needs; A = invoicing mailbox referee-confirmed on the buyer's own domain with MX, legal name, address, PO rule and terms all published, no penalties)

| package | rows | A | B | C | D | E | median ap_score |
|---|---|---|---|---|---|---|---|
| P01M | 19 | 5 | 2 | 12 | 0 | 0 | 75 |
| P01T | 92 | 16 | 49 | 27 | 0 | 0 | 79 |
| P01_GOLD | 596 | 129 | 255 | 212 | 0 | 0 | 79 |
| P02 | 399 | 0 | 57 | 342 | 0 | 0 | 63 |
| P03 | 223 | 0 | 0 | 214 | 9 | 0 | 53 |
| P04 | 1580 | 0 | 0 | 1518 | 62 | 0 | 51 |
| P05 | 379 | 9 | 27 | 324 | 19 | 0 | 48 |
| P06M | 168 | 0 | 1 | 158 | 9 | 0 | 48 |
| P06T | 2440 | 0 | 16 | 2140 | 284 | 0 | 48 |
| P06 | 165 | 15 | 31 | 119 | 0 | 0 | 69 |
| P07 | 252 | 0 | 12 | 215 | 25 | 0 | 50 |
| P08 | 3038 | 0 | 0 | 2253 | 785 | 0 | 40 |
| P09 | 374 | 4 | 9 | 360 | 1 | 0 | 50 |
| P10 | 2597 | 3 | 9 | 1855 | 730 | 0 | 40 |
| P11 | 478 | 0 | 0 | 0 | 0 | 478 | 25 |
| P12 | 21 | 0 | 0 | 21 | 0 | 0 | 53 |
| P13 | 50793 | 5 | 26 | 41037 | 9725 | 0 | 43 |

### What still blocks grade A (rows per missing element; a row counts under every element it lacks)

| package | rows not A | referee confirmation of the mailbox | an invoicing / AP mailbox (not finance / procurement / general) | a mailbox on the buyer's own domain | MX record for the mailbox domain | published bill-to legal name | invoice / billing address | published PO rule | published payment terms | clear the penalty |
|---|---|---|---|---|---|---|---|---|---|---|
| P01M | 14 | 0 | 0 | 0 | 0 | 1 | 1 | 11 | 12 | 5 |
| P01T | 76 | 0 | 0 | 0 | 1 | 4 | 4 | 28 | 42 | 59 |
| P01_GOLD | 467 | 0 | 0 | 0 | 9 | 86 | 42 | 198 | 252 | 269 |
| P02 | 399 | 0 | 399 | 0 | 2 | 37 | 13 | 368 | 351 | 232 |
| P03 | 223 | 0 | 223 | 0 | 1 | 39 | 13 | 149 | 169 | 88 |
| P04 | 1580 | 0 | 1580 | 0 | 6 | 334 | 127 | 1458 | 1330 | 959 |
| P05 | 370 | 0 | 316 | 0 | 4 | 91 | 55 | 319 | 342 | 238 |
| P06M | 168 | 0 | 168 | 0 | 0 | 19 | 47 | 166 | 167 | 95 |
| P06T | 2440 | 0 | 2440 | 0 | 23 | 869 | 489 | 2401 | 2364 | 1916 |
| P06 | 150 | 0 | 0 | 0 | 5 | 71 | 49 | 91 | 123 | 41 |
| P07 | 252 | 0 | 252 | 0 | 8 | 117 | 74 | 223 | 237 | 120 |
| P08 | 3038 | 0 | 3038 | 0 | 20 | 1916 | 1041 | 3030 | 3024 | 2067 |
| P09 | 370 | 0 | 350 | 0 | 2 | 68 | 1 | 354 | 360 | 280 |
| P10 | 2594 | 0 | 2539 | 0 | 26 | 1756 | 917 | 2573 | 2580 | 1867 |
| P11 | 478 | 478 | 441 | 0 | 9 | 357 | 236 | 461 | 461 | 306 |
| P12 | 21 | 0 | 16 | 0 | 0 | 4 | 0 | 20 | 19 | 16 |
| P13 | 50788 | 0 | 50482 | 0 | 460 | 25782 | 12591 | 50716 | 50664 | 40189 |

## Where the work is (largest gaps in rows still needed)

| field | package | now | target | rows needed |
|---|---|---|---|---|
| buyer_ap_cycle_published | P13 | 0.0% | 20% | 10151 |
| buyer_address | P13 | 75.1% | 95% | 10095 |
| ap_system_hint | P13 | 0.5% | 20% | 9919 |
| buyer_phone | P13 | 79.1% | 95% | 8100 |
| buyer_esignature_preference | P13 | 0.1% | 15% | 7580 |
| buyer_tax_exempt_status | P13 | 0.1% | 15% | 7548 |
| buyer_payment_method_preference | P13 | 0.9% | 15% | 7154 |
| buyer_logo_url | P13 | 83.9% | 95% | 5625 |
| buyer_legal_name_as_published | P13 | 49.2% | 60% | 5465 |
| buyer_bn_as_published | P13 | 21.6% | 30% | 4244 |
| buyer_legal_name_as_published | P08 | 36.9% | 75% | 1157 |
| buyer_legal_name_as_published | P10 | 32.4% | 70% | 977 |
| buyer_address | P08 | 65.6% | 95% | 893 |
| vendor_emails | P08 | 47.0% | 75% | 852 |
| buyer_address | P10 | 64.4% | 95% | 796 |
| vendor_emails | P10 | 50.6% | 80% | 763 |
| invoice_reference_hint | P08 | 0.3% | 25% | 752 |
| buyer_bn_as_published | P08 | 10.5% | 35% | 745 |
| vendor_registered_address | P10 | 42.4% | 70% | 718 |
| average_contract_duration_days | P04 | 44.8% | 90% | 714 |
| vendor_logo_url | P04 | 43.1% | 85% | 662 |
| invoice_reference_hint | P10 | 1.0% | 25% | 624 |
| buyer_phone | P08 | 74.6% | 95% | 622 |
| buyer_phone | P10 | 71.4% | 95% | 615 |
| vendor_phone | P08 | 64.9% | 85% | 612 |
| buyer_ap_cycle_published | P08 | 0.1% | 20% | 606 |
| vendor_emails | P04 | 32.3% | 70% | 595 |
| ap_system_hint | P08 | 0.9% | 20% | 580 |
| end_date | P04 | 53.9% | 90% | 571 |
| buyer_vendor_id | P04 | 4.2% | 40% | 565 |
| currency | P04 | 59.9% | 95% | 554 |
| vendor_neq | P04 | 60.1% | 95% | 552 |
| ap_phone | P04 | 50.3% | 85% | 549 |
| buyer_bn_as_published | P10 | 8.9% | 30% | 548 |
| vendor_registered_address | P08 | 52.2% | 70% | 542 |
| commodity_codes | P04 | 51.1% | 85% | 535 |
| vendor_phone | P10 | 65.0% | 85% | 519 |
| buyer_ap_cycle_published | P10 | 0.1% | 20% | 518 |
| po_required_as_published | P04 | 7.7% | 40% | 510 |
| vendor_phone | P04 | 33.0% | 65% | 506 |

## 1. identifiers

### `invoice_reference_hint`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 19 | 42.1% | 42.1% |  | 50% | 🟡 8 pts to go |
| P01T | 92 | 71.7% | 71.7% |  | 50% | ✅ met |
| P01_GOLD | 596 | 92.6% | 94.8% |  | 95% | 🟡 2 pts to go |
| P02 | 399 | 78.7% | 81.0% |  | 95% | ❌ 16 pts to go |
| P03 | 223 | 85.2% | 91.0% |  | 95% | 🟡 10 pts to go |
| P04 | 1580 | 68.4% | 71.0% |  | 90% | ❌ 22 pts to go |
| P05 | 379 | 38.3% | 41.4% |  | 70% | ❌ 32 pts to go |
| P06M | 168 | 1.2% | 1.2% |  | n/a | no target |
| P06T | 2440 | 1.8% | 1.8% |  | n/a | no target |
| P06 | 165 | 44.8% | 44.8% |  | 30% | ✅ met |
| P07 | 252 | 11.5% | 11.5% |  | 30% | ❌ 18 pts to go |
| P08 | 3038 | 0.3% | 0.3% |  | 25% | ❌ 25 pts to go |
| P09 | 374 | 98.7% | 99.5% |  | 100% | 🟡 1 pts to go |
| P10 | 2597 | 1.0% | 1.9% |  | 25% | ❌ 24 pts to go |
| P11 | 478 | 23.4% | 26.4% |  | 60% | ❌ 37 pts to go |
| P12 | 21 | 100.0% | 100.0% |  | 100% | ✅ met |
| P13 | 50793 | 0.2% | 0.3% |  | 0% by design | — leave (by design) |

### `po_number_as_published`

> ceiling: a purchase-order number exists only where the buyer publishes PO-level data (Montréal, Laval, Toronto open data so far) or the record itself carries one; most sources publish awards, not POs — the target cannot be reached from public data for most buyers

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 19 | 0.0% | 0.0% |  | n/a | no target |
| P01T | 92 | 0.0% | 0.0% |  | 10% | 🟡 10 pts to go |
| P01_GOLD | 596 | 6.4% | 6.4% |  | 50% | ❌ 44 pts to go |
| P02 | 399 | 7.5% | 7.5% |  | 50% | ❌ 42 pts to go |
| P03 | 223 | 1.8% | 1.8% |  | 40% | ❌ 38 pts to go |
| P04 | 1580 | 1.1% | 1.1% |  | 30% | ❌ 29 pts to go |
| P05 | 379 | 0.3% | 0.3% |  | 20% | ❌ 20 pts to go |
| P06M | 168 | 0.0% | 0.0% |  | n/a | no target |
| P06T | 2440 | 0.0% | 0.0% |  | n/a | no target |
| P06 | 165 | 0.0% | 0.0% |  | n/a | no target |
| P07 | 252 | 0.0% | 0.0% |  | n/a | no target |
| P08 | 3038 | 0.0% | 0.0% |  | n/a | no target |
| P09 | 374 | 0.5% | 0.5% |  | 50% | ❌ 50 pts to go |
| P10 | 2597 | 0.1% | 0.1% |  | n/a | no target |
| P11 | 478 | 0.8% | 0.8% |  | n/a | no target |
| P12 | 21 | 0.0% | 0.0% |  | n/a | no target |
| P13 | 50793 | 0.0% | 0.0% |  | n/a | no target |

### `contract_or_agreement_number`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 19 | 0.0% | 0.0% |  | n/a | no target |
| P01T | 92 | 5.4% | 5.4% |  | 50% | ❌ 45 pts to go |
| P01_GOLD | 596 | 69.6% | 69.6% |  | 85% | ❌ 15 pts to go |
| P02 | 399 | 73.7% | 73.7% |  | 90% | ❌ 16 pts to go |
| P03 | 223 | 70.9% | 70.9% |  | 85% | ❌ 14 pts to go |
| P04 | 1580 | 65.5% | 65.5% |  | 85% | ❌ 20 pts to go |
| P05 | 379 | 30.1% | 30.1% |  | 60% | ❌ 30 pts to go |
| P06M | 168 | 0.0% | 0.0% |  | n/a | no target |
| P06T | 2440 | 0.2% | 0.2% |  | n/a | no target |
| P06 | 165 | 0.0% | 0.0% |  | n/a | no target |
| P07 | 252 | 0.0% | 0.0% |  | n/a | no target |
| P08 | 3038 | 0.0% | 0.0% |  | n/a | no target |
| P09 | 374 | 96.5% | 96.5% |  | 100% | 🟡 4 pts to go |
| P10 | 2597 | 0.0% | 0.0% |  | n/a | no target |
| P11 | 478 | 21.3% | 21.3% |  | 60% | ❌ 39 pts to go |
| P12 | 21 | 100.0% | 100.0% |  | n/a | no target |
| P13 | 50793 | 0.0% | 0.0% |  | n/a | no target |

### `solicitation_or_tender_number`

> ceiling: SEAO's 'numero' is the organisation's own reference for the notice (SEAO data dictionary) and is reported here; sources that publish awards under a tender number only (bids&tenders, SaskTenders, BC) also carry it as the contract reference, labelled

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 19 | 0.0% | 0.0% |  | n/a | no target |
| P01T | 92 | 2.2% | 2.2% |  | 30% | ❌ 28 pts to go |
| P01_GOLD | 596 | 53.4% | 53.4% |  | 80% | ❌ 27 pts to go |
| P02 | 399 | 64.9% | 64.9% |  | 60% | ✅ met |
| P03 | 223 | 58.3% | 58.3% |  | 80% | ❌ 22 pts to go |
| P04 | 1580 | 54.4% | 54.4% |  | 50% | ✅ met |
| P05 | 379 | 12.4% | 12.4% |  | 40% | ❌ 28 pts to go |
| P06M | 168 | 0.0% | 0.0% |  | n/a | no target |
| P06T | 2440 | 0.2% | 0.2% |  | n/a | no target |
| P06 | 165 | 0.0% | 0.0% |  | n/a | no target |
| P07 | 252 | 0.0% | 0.0% |  | n/a | no target |
| P08 | 3038 | 0.0% | 0.0% |  | n/a | no target |
| P09 | 374 | 87.4% | 87.4% |  | 50% | ✅ met |
| P10 | 2597 | 0.0% | 0.0% |  | n/a | no target |
| P11 | 478 | 18.2% | 18.2% |  | 40% | ❌ 22 pts to go |
| P12 | 21 | 100.0% | 100.0% |  | 100% | ✅ met |
| P13 | 50793 | 0.0% | 0.0% |  | n/a | no target |

### `award_or_notice_id`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 19 | 0.0% | 0.0% |  | n/a | no target |
| P01T | 92 | 3.3% | 3.3% |  | n/a | no target |
| P01_GOLD | 596 | 63.1% | 63.1% |  | 85% | ❌ 22 pts to go |
| P02 | 399 | 64.2% | 64.2% |  | 90% | ❌ 26 pts to go |
| P03 | 223 | 69.1% | 69.1% |  | 85% | ❌ 16 pts to go |
| P04 | 1580 | 56.2% | 56.2% |  | 85% | ❌ 29 pts to go |
| P05 | 379 | 20.3% | 20.3% |  | 50% | ❌ 30 pts to go |
| P06M | 168 | 0.0% | 0.0% |  | n/a | no target |
| P06T | 2440 | 0.2% | 0.2% |  | n/a | no target |
| P06 | 165 | 0.0% | 0.0% |  | n/a | no target |
| P07 | 252 | 0.0% | 0.0% |  | n/a | no target |
| P08 | 3038 | 0.0% | 0.0% |  | n/a | no target |
| P09 | 374 | 97.1% | 97.1% |  | 100% | 🟡 3 pts to go |
| P10 | 2597 | 0.0% | 0.0% |  | n/a | no target |
| P11 | 478 | 20.1% | 20.1% |  | 60% | ❌ 40 pts to go |
| P12 | 21 | 100.0% | 100.0% |  | n/a | no target |
| P13 | 50793 | 0.0% | 0.0% |  | n/a | no target |

### `buyer_vendor_id`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 19 | 0.0% | 0.0% |  | n/a | no target |
| P01T | 92 | 2.2% | 2.2% |  | n/a | no target |
| P01_GOLD | 596 | 13.1% | 13.1% |  | 60% | ❌ 47 pts to go |
| P02 | 399 | 7.8% | 7.8% |  | 50% | ❌ 42 pts to go |
| P03 | 223 | 10.3% | 10.3% |  | 50% | ❌ 40 pts to go |
| P04 | 1580 | 4.2% | 4.2% |  | 40% | ❌ 36 pts to go |
| P05 | 379 | 1.3% | 1.3% |  | 20% | ❌ 19 pts to go |
| P06M | 168 | 0.0% | 0.0% |  | n/a | no target |
| P06T | 2440 | 0.1% | 0.1% |  | n/a | no target |
| P06 | 165 | 0.0% | 0.0% |  | n/a | no target |
| P07 | 252 | 0.0% | 0.0% |  | n/a | no target |
| P08 | 3038 | 0.0% | 0.0% |  | n/a | no target |
| P09 | 374 | 2.4% | 2.4% |  | 50% | ❌ 48 pts to go |
| P10 | 2597 | 0.0% | 0.0% |  | n/a | no target |
| P11 | 478 | 4.2% | 4.2% |  | n/a | no target |
| P12 | 21 | 0.0% | 0.0% |  | n/a | no target |
| P13 | 50793 | 0.0% | 0.0% |  | n/a | no target |

### `commodity_codes`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 19 | 0.0% | 0.0% |  | n/a | no target |
| P01T | 92 | 0.0% | 0.0% |  | n/a | no target |
| P01_GOLD | 596 | 36.6% | 36.6% |  | 80% | ❌ 43 pts to go |
| P02 | 399 | 58.9% | 58.9% |  | 90% | ❌ 31 pts to go |
| P03 | 223 | 36.3% | 36.3% |  | 80% | ❌ 44 pts to go |
| P04 | 1580 | 51.1% | 51.1% |  | 85% | ❌ 34 pts to go |
| P05 | 379 | 5.0% | 5.0% |  | 50% | ❌ 45 pts to go |
| P06M | 168 | 0.0% | 0.0% |  | n/a | no target |
| P06T | 2440 | 0.0% | 0.0% |  | n/a | no target |
| P06 | 165 | 0.0% | 0.0% |  | n/a | no target |
| P07 | 252 | 0.0% | 0.0% |  | n/a | no target |
| P08 | 3038 | 0.0% | 0.0% |  | n/a | no target |
| P09 | 374 | 75.7% | 75.7% |  | 95% | ❌ 19 pts to go |
| P10 | 2597 | 0.0% | 0.0% |  | n/a | no target |
| P11 | 478 | 14.0% | 14.0% |  | 50% | ❌ 36 pts to go |
| P12 | 21 | 0.0% | 0.0% |  | n/a | no target |
| P13 | 50793 | 0.0% | 0.0% |  | n/a | no target |

### `buyer_org_codes`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 19 | 0.0% | 0.0% |  | n/a | no target |
| P01T | 92 | 1.1% | 1.1% |  | n/a | no target |
| P01_GOLD | 596 | 8.6% | 8.6% |  | 50% | ❌ 41 pts to go |
| P02 | 399 | 7.5% | 7.5% |  | 50% | ❌ 42 pts to go |
| P03 | 223 | 2.7% | 2.7% |  | 30% | ❌ 27 pts to go |
| P04 | 1580 | 1.1% | 1.1% |  | 30% | ❌ 29 pts to go |
| P05 | 379 | 0.0% | 0.0% |  | n/a | no target |
| P06M | 168 | 0.0% | 0.0% |  | n/a | no target |
| P06T | 2440 | 0.0% | 0.0% |  | n/a | no target |
| P06 | 165 | 0.0% | 0.0% |  | n/a | no target |
| P07 | 252 | 0.0% | 0.0% |  | n/a | no target |
| P08 | 3038 | 0.0% | 0.0% |  | n/a | no target |
| P09 | 374 | 0.3% | 0.3% |  | n/a | no target |
| P10 | 2597 | 0.0% | 0.0% |  | n/a | no target |
| P11 | 478 | 0.8% | 0.8% |  | n/a | no target |
| P12 | 21 | 0.0% | 0.0% |  | n/a | no target |
| P13 | 50793 | 0.0% | 0.0% |  | n/a | no target |

### `records_with_this_vendor`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 19 | 100.0% | 100.0% |  | n/a | no target |
| P01T | 92 | 100.0% | 100.0% |  | 60% | ✅ met |
| P01_GOLD | 596 | 100.0% | 100.0% |  | 100% | ✅ met |
| P02 | 399 | 100.0% | 100.0% |  | 100% | ✅ met |
| P03 | 223 | 100.0% | 100.0% |  | 100% | ✅ met |
| P04 | 1580 | 100.0% | 100.0% |  | 95% | ✅ met |
| P05 | 379 | 100.0% | 100.0% |  | 70% | ✅ met |
| P06M | 168 | 100.0% | 100.0% |  | n/a | no target |
| P06T | 2440 | 100.0% | 100.0% |  | n/a | no target |
| P06 | 165 | 100.0% | 100.0% |  | 50% | ✅ met |
| P07 | 252 | 100.0% | 100.0% |  | n/a | no target |
| P08 | 3038 | 100.0% | 100.0% |  | n/a | no target |
| P09 | 374 | 100.0% | 100.0% |  | 100% | ✅ met |
| P10 | 2597 | 100.0% | 100.0% |  | n/a | no target |
| P11 | 478 | 100.0% | 100.0% |  | 70% | ✅ met |
| P12 | 21 | 100.0% | 100.0% |  | n/a | no target |
| P13 | 50793 | 0.0% | 0.0% |  | n/a | no target |

## 2. vendor

### `vendor_bn9`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 19 | 100.0% | 100.0% |  | 70% | ✅ met |
| P01T | 92 | 80.4% | 80.4% |  | 60% | ✅ met |
| P01_GOLD | 596 | 78.5% | 78.5% |  | 90% | ❌ 12 pts to go |
| P02 | 399 | 65.9% | 65.9% |  | 85% | ❌ 19 pts to go |
| P03 | 223 | 80.7% | 80.7% |  | 90% | 🟡 9 pts to go |
| P04 | 1580 | 53.7% | 53.7% |  | 75% | ❌ 21 pts to go |
| P05 | 379 | 52.8% | 52.8% |  | 50% | ✅ met |
| P06M | 168 | 74.4% | 74.4% |  | n/a | no target |
| P06T | 2440 | 60.7% | 60.7% |  | n/a | no target |
| P06 | 165 | 46.7% | 46.7% |  | 40% | ✅ met |
| P07 | 252 | 40.1% | 40.1% |  | 50% | 🟡 10 pts to go |
| P08 | 3038 | 41.8% | 41.8% |  | 50% | 🟡 8 pts to go |
| P09 | 374 | 54.8% | 54.8% |  | 80% | ❌ 25 pts to go |
| P10 | 2597 | 36.6% | 36.6% |  | 40% | 🟡 3 pts to go |
| P11 | 478 | 45.0% | 45.0% |  | 60% | ❌ 15 pts to go |
| P12 | 21 | 52.4% | 52.4% |  | 85% | ❌ 33 pts to go |
| P13 | 50793 | 91.7% | 91.7% |  | 0% by design | — leave (by design) |

### `vendor_registered_address`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 19 | 63.2% | 63.2% |  | n/a | no target |
| P01T | 92 | 63.0% | 63.0% |  | n/a | no target |
| P01_GOLD | 596 | 75.5% | 75.5% |  | 95% | ❌ 20 pts to go |
| P02 | 399 | 81.7% | 81.7% |  | 95% | ❌ 13 pts to go |
| P03 | 223 | 76.7% | 76.7% |  | 95% | ❌ 18 pts to go |
| P04 | 1580 | 78.7% | 78.7% |  | 95% | ❌ 16 pts to go |
| P05 | 379 | 55.7% | 55.7% |  | 70% | ❌ 14 pts to go |
| P06M | 168 | 20.8% | 20.8% |  | n/a | no target |
| P06T | 2440 | 78.3% | 78.3% |  | n/a | no target |
| P06 | 165 | 55.2% | 55.2% |  | 80% | ❌ 25 pts to go |
| P07 | 252 | 52.0% | 52.0% |  | 70% | ❌ 18 pts to go |
| P08 | 3038 | 52.2% | 52.2% |  | 70% | ❌ 18 pts to go |
| P09 | 374 | 89.6% | 89.6% |  | 100% | ❌ 10 pts to go |
| P10 | 2597 | 42.4% | 42.4% |  | 70% | ❌ 28 pts to go |
| P11 | 478 | 54.0% | 54.0% |  | 75% | ❌ 21 pts to go |
| P12 | 21 | 100.0% | 100.0% |  | n/a | no target |
| P13 | 50793 | 0.0% | 0.0% |  | n/a | no target |

### `vendor_trading_name`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 19 | 52.6% | 52.6% |  | n/a | no target |
| P01T | 92 | 19.6% | 19.6% |  | n/a | no target |
| P01_GOLD | 596 | 50.0% | 50.0% |  | 60% | 🟡 10 pts to go |
| P02 | 399 | 62.7% | 62.7% |  | 60% | ✅ met |
| P03 | 223 | 57.0% | 57.0% |  | 60% | 🟡 3 pts to go |
| P04 | 1580 | 53.4% | 53.4% |  | 55% | 🟡 2 pts to go |
| P05 | 379 | 23.5% | 23.5% |  | 50% | ❌ 26 pts to go |
| P06M | 168 | 17.3% | 17.3% |  | n/a | no target |
| P06T | 2440 | 53.6% | 53.6% |  | n/a | no target |
| P06 | 165 | 48.5% | 48.5% |  | n/a | no target |
| P07 | 252 | 44.4% | 44.4% |  | 55% | ❌ 11 pts to go |
| P08 | 3038 | 44.3% | 44.3% |  | 50% | 🟡 6 pts to go |
| P09 | 374 | 71.4% | 71.4% |  | 70% | ✅ met |
| P10 | 2597 | 50.4% | 50.4% |  | 55% | 🟡 5 pts to go |
| P11 | 478 | 41.2% | 41.2% |  | 50% | 🟡 9 pts to go |
| P12 | 21 | 85.7% | 85.7% |  | n/a | no target |
| P13 | 50793 | 0.0% | 0.0% |  | n/a | no target |

### `vendor_phone`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 19 | 36.8% | 36.8% |  | n/a | no target |
| P01T | 92 | 0.0% | 0.0% |  | n/a | no target |
| P01_GOLD | 596 | 33.1% | 33.1% |  | 70% | ❌ 37 pts to go |
| P02 | 399 | 41.4% | 41.4% |  | 70% | ❌ 29 pts to go |
| P03 | 223 | 39.0% | 39.0% |  | 70% | ❌ 31 pts to go |
| P04 | 1580 | 33.0% | 33.0% |  | 65% | ❌ 32 pts to go |
| P05 | 379 | 16.9% | 16.9% |  | 60% | ❌ 43 pts to go |
| P06M | 168 | 6.5% | 6.5% |  | n/a | no target |
| P06T | 2440 | 0.0% | 0.0% |  | n/a | no target |
| P06 | 165 | 58.2% | 58.2% |  | 40% | ✅ met |
| P07 | 252 | 64.7% | 64.7% |  | 85% | ❌ 20 pts to go |
| P08 | 3038 | 64.9% | 64.9% |  | 85% | ❌ 20 pts to go |
| P09 | 374 | 51.6% | 51.6% |  | 85% | ❌ 33 pts to go |
| P10 | 2597 | 65.0% | 65.0% |  | 85% | ❌ 20 pts to go |
| P11 | 478 | 49.0% | 49.0% |  | 75% | ❌ 26 pts to go |
| P12 | 21 | 4.8% | 4.8% |  | n/a | no target |
| P13 | 50793 | 100.0% | 100.0% |  | 60% | ✅ met |

### `vendor_website`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 19 | 94.7% | 94.7% |  | n/a | no target |
| P01T | 92 | 90.2% | 90.2% |  | n/a | no target |
| P01_GOLD | 596 | 90.1% | 90.1% |  | 90% | ✅ met |
| P02 | 399 | 82.5% | 82.5% |  | 90% | 🟡 8 pts to go |
| P03 | 223 | 84.3% | 84.3% |  | 90% | 🟡 6 pts to go |
| P04 | 1580 | 80.1% | 80.1% |  | 85% | 🟡 5 pts to go |
| P05 | 379 | 50.1% | 50.1% |  | 70% | ❌ 20 pts to go |
| P06M | 168 | 67.9% | 67.9% |  | n/a | no target |
| P06T | 2440 | 77.9% | 77.9% |  | n/a | no target |
| P06 | 165 | 97.0% | 97.0% |  | 50% | ✅ met |
| P07 | 252 | 96.8% | 96.8% |  | 100% | 🟡 3 pts to go |
| P08 | 3038 | 96.1% | 96.1% |  | 100% | 🟡 4 pts to go |
| P09 | 374 | 81.0% | 81.0% |  | 100% | ❌ 19 pts to go |
| P10 | 2597 | 100.0% | 100.0% |  | 100% | ✅ met |
| P11 | 478 | 92.5% | 92.5% |  | 100% | 🟡 8 pts to go |
| P12 | 21 | 42.9% | 42.9% |  | n/a | no target |
| P13 | 50793 | 100.0% | 100.0% |  | n/a | no target |

### `vendor_emails`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 19 | 36.8% | 36.8% |  | n/a | no target |
| P01T | 92 | 0.0% | 0.0% |  | n/a | no target |
| P01_GOLD | 596 | 36.7% | 36.7% |  | 70% | ❌ 33 pts to go |
| P02 | 399 | 44.1% | 44.1% |  | 75% | ❌ 31 pts to go |
| P03 | 223 | 42.2% | 42.2% |  | 75% | ❌ 33 pts to go |
| P04 | 1580 | 32.3% | 32.3% |  | 70% | ❌ 38 pts to go |
| P05 | 379 | 13.7% | 13.7% |  | 55% | ❌ 41 pts to go |
| P06M | 168 | 6.5% | 6.5% |  | n/a | no target |
| P06T | 2440 | 0.0% | 0.0% |  | n/a | no target |
| P06 | 165 | 40.0% | 40.0% |  | n/a | no target |
| P07 | 252 | 35.7% | 35.7% |  | 70% | ❌ 34 pts to go |
| P08 | 3038 | 47.0% | 47.0% |  | 75% | ❌ 28 pts to go |
| P09 | 374 | 52.4% | 52.4% |  | 85% | ❌ 33 pts to go |
| P10 | 2597 | 50.6% | 50.6% |  | 80% | ❌ 29 pts to go |
| P11 | 478 | 36.4% | 36.4% |  | 70% | ❌ 34 pts to go |
| P12 | 21 | 19.0% | 19.0% |  | n/a | no target |
| P13 | 50793 | 0.0% | 0.0% |  | n/a | no target |

### `vendor_logo_url`

> ceiling: needs the vendor's website first; sites that block automated readers (robots.txt / 403) are never read

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 19 | 36.8% | 36.8% |  | n/a | no target |
| P01T | 92 | 0.0% | 0.0% |  | n/a | no target |
| P01_GOLD | 596 | 49.0% | 49.0% |  | 90% | ❌ 41 pts to go |
| P02 | 399 | 56.9% | 56.9% |  | 90% | ❌ 33 pts to go |
| P03 | 223 | 54.7% | 54.7% |  | 90% | ❌ 35 pts to go |
| P04 | 1580 | 43.1% | 43.1% |  | 85% | ❌ 42 pts to go |
| P05 | 379 | 22.2% | 22.2% |  | 75% | ❌ 53 pts to go |
| P06M | 168 | 6.5% | 6.5% |  | n/a | no target |
| P06T | 2440 | 0.0% | 0.0% |  | n/a | no target |
| P06 | 165 | 87.3% | 87.3% |  | n/a | no target |
| P07 | 252 | 88.1% | 88.1% |  | 100% | ❌ 12 pts to go |
| P08 | 3038 | 85.4% | 85.4% |  | 100% | ❌ 15 pts to go |
| P09 | 374 | 58.0% | 58.0% |  | n/a | no target |
| P10 | 2597 | 87.6% | 87.6% |  | 100% | ❌ 12 pts to go |
| P11 | 478 | 64.6% | 64.6% |  | n/a | no target |
| P12 | 21 | 14.3% | 14.3% |  | n/a | no target |
| P13 | 50793 | 0.0% | 0.0% |  | n/a | no target |

### `vendor_neq`

> ceiling: only Québec-registered vendors have an NEQ; the share of QC vendors is reported next to the rate

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 19 | 0.0% | 0.0% |  | n/a | no target |
| P01T | 92 | 21.7% | 21.7% |  | n/a | no target · QC vendors: 2 rows, 100.0% filled |
| P01_GOLD | 596 | 49.2% | 49.2% |  | 95% | ❌ 46 pts to go · QC vendors: 52 rows, 98.1% filled |
| P02 | 399 | 67.2% | 67.2% |  | 95% | ❌ 28 pts to go · QC vendors: 98 rows, 100.0% filled |
| P03 | 223 | 53.8% | 53.8% |  | 95% | ❌ 41 pts to go · QC vendors: 16 rows, 100.0% filled |
| P04 | 1580 | 60.1% | 60.1% |  | 95% | ❌ 35 pts to go · QC vendors: 440 rows, 98.6% filled |
| P05 | 379 | 13.7% | 13.7% |  | n/a | no target · QC vendors: 26 rows, 92.3% filled |
| P06M | 168 | 0.0% | 0.0% |  | n/a | no target |
| P06T | 2440 | 55.9% | 55.9% |  | n/a | no target · QC vendors: 56 rows, 100.0% filled |
| P06 | 165 | 24.2% | 24.2% |  | n/a | no target · QC vendors: 16 rows, 100.0% filled |
| P07 | 252 | 19.4% | 19.4% |  | n/a | no target · QC vendors: 26 rows, 96.2% filled |
| P08 | 3038 | 26.9% | 26.9% |  | n/a | no target · QC vendors: 544 rows, 98.5% filled |
| P09 | 374 | 81.8% | 81.8% |  | 95% | ❌ 13 pts to go · QC vendors: 156 rows, 99.4% filled |
| P10 | 2597 | 22.8% | 22.8% |  | n/a | no target · QC vendors: 444 rows, 94.6% filled |
| P11 | 478 | 28.2% | 28.2% |  | n/a | no target · QC vendors: 78 rows, 98.7% filled |
| P12 | 21 | 76.2% | 76.2% |  | n/a | no target · QC vendors: 4 rows, 100.0% filled |
| P13 | 50793 | 0.0% | 0.0% |  | n/a | no target |

### `vendor_years_in_business`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 19 | 63.2% | 63.2% |  | n/a | no target · vendors with a registry record: 12 rows, 100.0% filled |
| P01T | 92 | 63.0% | 63.0% |  | n/a | no target · vendors with a registry record: 58 rows, 100.0% filled |
| P01_GOLD | 596 | 85.2% | 85.2% |  | 100% | ❌ 15 pts to go · vendors with a registry record: 508 rows, 100.0% filled |
| P02 | 399 | 88.0% | 88.0% |  | 100% | ❌ 12 pts to go · vendors with a registry record: 351 rows, 100.0% filled |
| P03 | 223 | 87.4% | 87.4% |  | 100% | ❌ 13 pts to go · vendors with a registry record: 195 rows, 100.0% filled |
| P04 | 1580 | 81.4% | 81.4% |  | 100% | ❌ 19 pts to go · vendors with a registry record: 1286 rows, 100.0% filled |
| P05 | 379 | 61.2% | 61.2% |  | n/a | no target · vendors with a registry record: 232 rows, 100.0% filled |
| P06M | 168 | 20.8% | 20.8% |  | n/a | no target · vendors with a registry record: 35 rows, 100.0% filled |
| P06T | 2440 | 78.3% | 78.3% |  | n/a | no target · vendors with a registry record: 1910 rows, 100.0% filled |
| P06 | 165 | 58.2% | 58.2% |  | n/a | no target · vendors with a registry record: 96 rows, 100.0% filled |
| P07 | 252 | 54.4% | 54.4% |  | n/a | no target · vendors with a registry record: 137 rows, 100.0% filled |
| P08 | 3038 | 54.3% | 54.3% |  | n/a | no target · vendors with a registry record: 1651 rows, 100.0% filled |
| P09 | 374 | 92.8% | 92.8% |  | n/a | no target · vendors with a registry record: 347 rows, 100.0% filled |
| P10 | 2597 | 43.6% | 43.6% |  | n/a | no target · vendors with a registry record: 1133 rows, 100.0% filled |
| P11 | 478 | 57.5% | 57.5% |  | n/a | no target · vendors with a registry record: 275 rows, 100.0% filled |
| P12 | 21 | 100.0% | 100.0% |  | n/a | no target · vendors with a registry record: 21 rows, 100.0% filled |
| P13 | 50793 | 0.0% | 0.0% |  | n/a | no target |

## 3. buyer

### `buyer_legal_name_as_published`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 19 | 94.7% | 94.7% |  | 90% | ✅ met |
| P01T | 92 | 95.7% | 95.7% |  | 90% | ✅ met |
| P01_GOLD | 596 | 85.6% | 85.6% |  | 95% | 🟡 9 pts to go |
| P02 | 399 | 90.7% | 90.7% |  | 95% | 🟡 4 pts to go |
| P03 | 223 | 82.5% | 82.5% |  | 85% | 🟡 2 pts to go |
| P04 | 1580 | 78.9% | 78.9% |  | 90% | ❌ 11 pts to go |
| P05 | 379 | 76.0% | 76.0% |  | 75% | ✅ met |
| P06M | 168 | 88.7% | 88.7% |  | n/a | no target |
| P06T | 2440 | 64.4% | 64.4% |  | n/a | no target |
| P06 | 165 | 57.0% | 57.0% |  | 80% | ❌ 23 pts to go |
| P07 | 252 | 53.6% | 53.6% |  | 80% | ❌ 26 pts to go |
| P08 | 3038 | 36.9% | 36.9% |  | 75% | ❌ 38 pts to go |
| P09 | 374 | 81.8% | 81.8% |  | 95% | ❌ 13 pts to go |
| P10 | 2597 | 32.4% | 32.4% |  | 70% | ❌ 38 pts to go |
| P11 | 478 | 25.3% | 25.3% |  | 65% | ❌ 40 pts to go |
| P12 | 21 | 81.0% | 81.0% |  | 80% | ✅ met |
| P13 | 50793 | 49.2% | 49.3% |  | 60% | ❌ 11 pts to go |

### `buyer_bn_as_published`

> ceiling: a buyer's BN is public only where the buyer prints it or a public dataset carries it (CRA charities, federal grants & contributions recipients, business registries for corporations); municipalities rarely publish theirs

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 19 | 36.8% | 36.8% |  | 50% | ❌ 13 pts to go |
| P01T | 92 | 20.7% | 20.7% |  | n/a | no target |
| P01_GOLD | 596 | 20.6% | 20.6% |  | 40% | ❌ 19 pts to go |
| P02 | 399 | 22.3% | 22.3% |  | 40% | ❌ 18 pts to go |
| P03 | 223 | 26.5% | 26.5% |  | 40% | ❌ 14 pts to go |
| P04 | 1580 | 27.5% | 27.5% |  | 40% | ❌ 12 pts to go |
| P05 | 379 | 23.5% | 23.5% |  | 25% | 🟡 2 pts to go |
| P06M | 168 | 25.0% | 25.0% |  | n/a | no target |
| P06T | 2440 | 30.8% | 30.8% |  | n/a | no target |
| P06 | 165 | 9.7% | 9.7% |  | 35% | ❌ 25 pts to go |
| P07 | 252 | 9.9% | 9.9% |  | 35% | ❌ 25 pts to go |
| P08 | 3038 | 10.5% | 10.5% |  | 35% | ❌ 24 pts to go |
| P09 | 374 | 17.9% | 17.9% |  | n/a | no target |
| P10 | 2597 | 8.9% | 8.9% |  | 30% | ❌ 21 pts to go |
| P11 | 478 | 8.4% | 8.4% |  | n/a | no target |
| P12 | 21 | 19.0% | 19.0% |  | n/a | no target |
| P13 | 50793 | 21.6% | 21.6% |  | 30% | 🟡 8 pts to go |

### `buyer_address`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 19 | 94.7% | 94.7% |  | 100% | 🟡 5 pts to go |
| P01T | 92 | 93.5% | 93.5% |  | 100% | 🟡 6 pts to go |
| P01_GOLD | 596 | 89.1% | 89.1% |  | 100% | ❌ 11 pts to go |
| P02 | 399 | 96.0% | 96.0% |  | 100% | 🟡 4 pts to go |
| P03 | 223 | 94.2% | 94.2% |  | 100% | 🟡 6 pts to go |
| P04 | 1580 | 90.8% | 90.8% |  | 100% | 🟡 9 pts to go |
| P05 | 379 | 84.4% | 84.4% |  | 100% | ❌ 16 pts to go |
| P06M | 168 | 71.4% | 71.4% |  | n/a | no target |
| P06T | 2440 | 79.8% | 79.8% |  | n/a | no target |
| P06 | 165 | 66.7% | 66.7% |  | 95% | ❌ 28 pts to go |
| P07 | 252 | 69.4% | 69.4% |  | 95% | ❌ 26 pts to go |
| P08 | 3038 | 65.6% | 65.6% |  | 95% | ❌ 29 pts to go |
| P09 | 374 | 98.4% | 98.4% |  | 100% | 🟡 2 pts to go |
| P10 | 2597 | 64.4% | 64.4% |  | 95% | ❌ 31 pts to go |
| P11 | 478 | 35.4% | 35.4% |  | 80% | ❌ 45 pts to go |
| P12 | 21 | 100.0% | 100.0% |  | 100% | ✅ met |
| P13 | 50793 | 75.1% | 75.1% |  | 95% | ❌ 20 pts to go |

### `buyer_phone`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 19 | 89.5% | 89.5% |  | n/a | no target |
| P01T | 92 | 80.4% | 80.4% |  | n/a | no target |
| P01_GOLD | 596 | 69.5% | 69.5% |  | 90% | ❌ 20 pts to go |
| P02 | 399 | 77.7% | 77.7% |  | 95% | ❌ 17 pts to go |
| P03 | 223 | 74.9% | 74.9% |  | 95% | ❌ 20 pts to go |
| P04 | 1580 | 84.7% | 84.7% |  | 95% | ❌ 10 pts to go |
| P05 | 379 | 74.9% | 74.9% |  | 90% | ❌ 15 pts to go |
| P06M | 168 | 83.9% | 83.9% |  | n/a | no target |
| P06T | 2440 | 77.1% | 77.1% |  | n/a | no target |
| P06 | 165 | 63.6% | 63.6% |  | 95% | ❌ 31 pts to go |
| P07 | 252 | 65.1% | 65.1% |  | 90% | ❌ 25 pts to go |
| P08 | 3038 | 74.6% | 74.6% |  | 95% | ❌ 20 pts to go |
| P09 | 374 | 89.3% | 89.3% |  | 100% | ❌ 11 pts to go |
| P10 | 2597 | 71.4% | 71.4% |  | 95% | ❌ 24 pts to go |
| P11 | 478 | 28.0% | 28.0% |  | 75% | ❌ 47 pts to go |
| P12 | 21 | 85.7% | 85.7% |  | n/a | no target |
| P13 | 50793 | 79.1% | 79.1% |  | 95% | ❌ 16 pts to go |

### `buyer_logo_url`

> ceiling: sites that block automated readers (robots.txt / 403) are never read; an og:image that looks like a photo is labelled

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 19 | 78.9% | 78.9% |  | n/a | no target |
| P01T | 92 | 91.3% | 91.3% |  | 95% | 🟡 4 pts to go |
| P01_GOLD | 596 | 68.1% | 68.1% |  | 90% | ❌ 22 pts to go |
| P02 | 399 | 77.2% | 77.2% |  | 95% | ❌ 18 pts to go |
| P03 | 223 | 71.3% | 71.3% |  | 95% | ❌ 24 pts to go |
| P04 | 1580 | 63.4% | 63.4% |  | 90% | ❌ 27 pts to go |
| P05 | 379 | 78.6% | 78.6% |  | 95% | ❌ 16 pts to go |
| P06M | 168 | 84.5% | 84.5% |  | n/a | no target |
| P06T | 2440 | 93.6% | 93.6% |  | n/a | no target |
| P06 | 165 | 89.7% | 89.7% |  | 100% | ❌ 10 pts to go |
| P07 | 252 | 86.9% | 86.9% |  | 100% | ❌ 13 pts to go |
| P08 | 3038 | 90.2% | 90.2% |  | 100% | 🟡 10 pts to go |
| P09 | 374 | 52.4% | 52.4% |  | n/a | no target |
| P10 | 2597 | 89.4% | 89.4% |  | 100% | ❌ 11 pts to go |
| P11 | 478 | 32.6% | 32.6% |  | 80% | ❌ 47 pts to go |
| P12 | 21 | 61.9% | 61.9% |  | n/a | no target |
| P13 | 50793 | 83.9% | 83.9% |  | 95% | ❌ 11 pts to go |

## 4. AP

### `ap_contact_name_as_published`

> ceiling: owner 2026-11-08: the AP contact person the organisation itself names on its AP / finance page is allowed (name + role phrase, quoted); mailboxes stay organisational; many bodies publish no AP person

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 19 | 15.8% | 15.8% |  | n/a | no target |
| P01T | 92 | 23.9% | 23.9% |  | n/a | no target |
| P01_GOLD | 596 | 13.4% | 13.4% |  | 25% | ❌ 12 pts to go |
| P02 | 399 | 19.8% | 19.8% |  | 40% | ❌ 20 pts to go |
| P03 | 223 | 4.5% | 4.5% |  | 20% | ❌ 16 pts to go |
| P04 | 1580 | 4.1% | 4.1% |  | 20% | ❌ 16 pts to go |
| P05 | 379 | 1.6% | 1.6% |  | 15% | ❌ 13 pts to go |
| P06M | 168 | 1.8% | 1.8% |  | n/a | no target |
| P06T | 2440 | 1.1% | 1.1% |  | n/a | no target |
| P06 | 165 | 4.8% | 4.8% |  | n/a | no target |
| P07 | 252 | 5.2% | 5.2% |  | n/a | no target |
| P08 | 3038 | 0.0% | 0.0% |  | n/a | no target |
| P09 | 374 | 5.6% | 5.6% |  | n/a | no target |
| P10 | 2597 | 0.3% | 0.3% |  | n/a | no target |
| P11 | 478 | 1.0% | 1.0% |  | n/a | no target |
| P12 | 21 | 0.0% | 0.0% |  | n/a | no target |
| P13 | 50793 | 0.2% | 0.2% |  | n/a | no target |

### `ap_phone`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 19 | 36.8% | 36.8% |  | n/a | no target |
| P01T | 92 | 34.8% | 34.8% |  | 70% | ❌ 35 pts to go |
| P01_GOLD | 596 | 43.5% | 43.5% |  | 80% | ❌ 36 pts to go |
| P02 | 399 | 64.2% | 64.2% |  | 90% | ❌ 26 pts to go |
| P03 | 223 | 21.5% | 21.5% |  | 60% | ❌ 38 pts to go |
| P04 | 1580 | 50.3% | 50.3% |  | 85% | ❌ 35 pts to go |
| P05 | 379 | 12.9% | 12.9% |  | 50% | ❌ 37 pts to go |
| P06M | 168 | 6.0% | 6.0% |  | n/a | no target |
| P06T | 2440 | 2.3% | 2.3% |  | n/a | no target |
| P06 | 165 | 18.2% | 18.2% |  | n/a | no target |
| P07 | 252 | 19.0% | 19.0% |  | n/a | no target |
| P08 | 3038 | 0.5% | 0.5% |  | n/a | no target |
| P09 | 374 | 81.0% | 81.0% |  | 95% | ❌ 14 pts to go |
| P10 | 2597 | 3.1% | 3.1% |  | n/a | no target |
| P11 | 478 | 30.8% | 30.8% |  | n/a | no target |
| P12 | 21 | 33.3% | 33.3% |  | n/a | no target |
| P13 | 50793 | 1.0% | 1.0% |  | n/a | no target |

### `invoice_mailing_address`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 19 | 0.0% | 0.0% |  | n/a | no target |
| P01T | 92 | 16.3% | 16.3% |  | n/a | no target |
| P01_GOLD | 596 | 33.6% | 33.6% |  | 70% | ❌ 36 pts to go |
| P02 | 399 | 42.6% | 42.6% |  | 75% | ❌ 32 pts to go |
| P03 | 223 | 21.1% | 21.1% |  | 55% | ❌ 34 pts to go |
| P04 | 1580 | 49.9% | 49.9% |  | 75% | ❌ 25 pts to go |
| P05 | 379 | 11.1% | 11.1% |  | 50% | ❌ 39 pts to go |
| P06M | 168 | 1.8% | 1.8% |  | n/a | no target |
| P06T | 2440 | 1.1% | 1.1% |  | n/a | no target |
| P06 | 165 | 10.3% | 10.3% |  | n/a | no target |
| P07 | 252 | 10.3% | 10.3% |  | n/a | no target |
| P08 | 3038 | 0.5% | 0.5% |  | n/a | no target |
| P09 | 374 | 77.5% | 77.5% |  | 95% | ❌ 18 pts to go |
| P10 | 2597 | 1.8% | 1.8% |  | n/a | no target |
| P11 | 478 | 29.7% | 29.7% |  | n/a | no target |
| P12 | 21 | 19.0% | 19.0% |  | n/a | no target |
| P13 | 50793 | 0.6% | 0.6% |  | n/a | no target |

### `invoicing_requirements`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 19 | 21.1% | 21.1% |  | n/a | no target |
| P01T | 92 | 18.5% | 18.5% |  | n/a | no target |
| P01_GOLD | 596 | 54.7% | 54.9% |  | 80% | ❌ 25 pts to go |
| P02 | 399 | 44.9% | 44.9% |  | 75% | ❌ 30 pts to go |
| P03 | 223 | 32.7% | 32.7% |  | 70% | ❌ 37 pts to go |
| P04 | 1580 | 39.6% | 39.6% |  | 70% | ❌ 30 pts to go |
| P05 | 379 | 14.5% | 14.5% |  | 50% | ❌ 36 pts to go |
| P06M | 168 | 0.6% | 0.6% |  | n/a | no target |
| P06T | 2440 | 1.0% | 1.0% |  | n/a | no target |
| P06 | 165 | 21.2% | 21.2% |  | n/a | no target |
| P07 | 252 | 2.4% | 2.4% |  | n/a | no target |
| P08 | 3038 | 0.4% | 0.4% |  | n/a | no target |
| P09 | 374 | 42.0% | 42.0% |  | 80% | ❌ 38 pts to go |
| P10 | 2597 | 1.2% | 1.2% |  | n/a | no target |
| P11 | 478 | 16.7% | 16.7% |  | n/a | no target |
| P12 | 21 | 33.3% | 33.3% |  | n/a | no target |
| P13 | 50793 | 0.3% | 0.3% |  | n/a | no target |

### `payment_terms_as_published`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 19 | 36.8% | 36.8% |  | n/a | no target |
| P01T | 92 | 54.3% | 54.3% |  | 60% | 🟡 6 pts to go |
| P01_GOLD | 596 | 57.7% | 57.7% |  | 70% | ❌ 12 pts to go |
| P02 | 399 | 12.0% | 12.0% |  | 50% | ❌ 38 pts to go |
| P03 | 223 | 24.2% | 24.2% |  | 55% | ❌ 31 pts to go |
| P04 | 1580 | 15.8% | 15.8% |  | 40% | ❌ 24 pts to go |
| P05 | 379 | 9.8% | 9.8% |  | 40% | ❌ 30 pts to go |
| P06M | 168 | 0.6% | 0.6% |  | n/a | no target |
| P06T | 2440 | 3.1% | 3.1% |  | n/a | no target |
| P06 | 165 | 25.5% | 25.5% |  | n/a | no target |
| P07 | 252 | 6.0% | 6.0% |  | n/a | no target |
| P08 | 3038 | 0.5% | 0.5% |  | n/a | no target |
| P09 | 374 | 3.7% | 3.7% |  | n/a | no target |
| P10 | 2597 | 0.7% | 0.7% |  | n/a | no target |
| P11 | 478 | 3.6% | 3.6% |  | n/a | no target |
| P12 | 21 | 9.5% | 9.5% |  | n/a | no target |
| P13 | 50793 | 0.3% | 0.3% |  | n/a | no target |

### `po_required_as_published`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 19 | 42.1% | 42.1% |  | n/a | no target |
| P01T | 92 | 69.6% | 69.6% |  | 65% | ✅ met |
| P01_GOLD | 596 | 66.8% | 66.8% |  | 70% | 🟡 3 pts to go |
| P02 | 399 | 7.8% | 7.8% |  | 50% | ❌ 42 pts to go |
| P03 | 223 | 33.2% | 33.2% |  | 60% | ❌ 27 pts to go |
| P04 | 1580 | 7.7% | 7.7% |  | 40% | ❌ 32 pts to go |
| P05 | 379 | 15.8% | 15.8% |  | 45% | ❌ 29 pts to go |
| P06M | 168 | 1.2% | 1.2% |  | n/a | no target |
| P06T | 2440 | 1.6% | 1.6% |  | n/a | no target |
| P06 | 165 | 44.8% | 44.8% |  | n/a | no target |
| P07 | 252 | 11.5% | 11.5% |  | n/a | no target |
| P08 | 3038 | 0.3% | 0.3% |  | n/a | no target |
| P09 | 374 | 5.3% | 5.3% |  | n/a | no target |
| P10 | 2597 | 0.9% | 0.9% |  | n/a | no target |
| P11 | 478 | 3.6% | 3.6% |  | n/a | no target |
| P12 | 21 | 4.8% | 4.8% |  | n/a | no target |
| P13 | 50793 | 0.2% | 0.2% |  | n/a | no target |

### `invoice_portal_url`

> ceiling: only portals the buyer names on its own pages; informational tax-authority links are not portals

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 19 | 15.8% | 15.8% |  | n/a | no target |
| P01T | 92 | 42.4% | 42.4% |  | n/a | no target |
| P01_GOLD | 596 | 46.5% | 46.5% |  | 50% | 🟡 4 pts to go |
| P02 | 399 | 25.6% | 25.6% |  | n/a | no target |
| P03 | 223 | 52.0% | 52.0% |  | 60% | 🟡 8 pts to go |
| P04 | 1580 | 20.6% | 20.6% |  | n/a | no target |
| P05 | 379 | 14.8% | 14.8% |  | n/a | no target |
| P06M | 168 | 2.4% | 2.4% |  | n/a | no target |
| P06T | 2440 | 2.3% | 2.3% |  | n/a | no target |
| P06 | 165 | 32.1% | 32.1% |  | n/a | no target |
| P07 | 252 | 13.1% | 13.1% |  | n/a | no target |
| P08 | 3038 | 0.5% | 0.5% |  | n/a | no target |
| P09 | 374 | 12.0% | 12.0% |  | n/a | no target |
| P10 | 2597 | 1.5% | 1.5% |  | n/a | no target |
| P11 | 478 | 5.0% | 5.0% |  | n/a | no target |
| P12 | 21 | 4.8% | 4.8% |  | n/a | no target |
| P13 | 50793 | 0.4% | 0.4% |  | n/a | no target |

### `buyer_payment_method_preference`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 19 | 31.6% | 31.6% |  | 15% | ✅ met |
| P01T | 92 | 29.3% | 29.3% |  | 15% | ✅ met |
| P01_GOLD | 596 | 35.1% | 35.1% |  | 40% | 🟡 5 pts to go |
| P02 | 399 | 8.8% | 9.0% |  | 25% | ❌ 16 pts to go |
| P03 | 223 | 15.2% | 15.2% |  | 25% | 🟡 10 pts to go |
| P04 | 1580 | 4.9% | 4.9% |  | 15% | ❌ 10 pts to go |
| P05 | 379 | 6.3% | 6.3% |  | 15% | 🟡 9 pts to go |
| P06M | 168 | 3.0% | 3.0% |  | 15% | ❌ 12 pts to go |
| P06T | 2440 | 1.2% | 1.2% |  | 15% | ❌ 14 pts to go |
| P06 | 165 | 9.1% | 9.1% |  | 15% | 🟡 6 pts to go |
| P07 | 252 | 4.0% | 4.0% |  | 15% | ❌ 11 pts to go |
| P08 | 3038 | 0.8% | 0.8% |  | 15% | ❌ 14 pts to go |
| P09 | 374 | 0.8% | 0.8% |  | 15% | ❌ 14 pts to go |
| P10 | 2597 | 1.0% | 1.0% |  | 15% | ❌ 14 pts to go |
| P11 | 478 | 1.3% | 1.3% |  | 15% | ❌ 14 pts to go |
| P12 | 21 | 0.0% | 0.0% |  | 15% | ❌ 15 pts to go |
| P13 | 50793 | 0.9% | 0.9% |  | 15% | ❌ 14 pts to go |

### `buyer_tax_exempt_status`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 19 | 10.5% | 10.5% |  | 15% | 🟡 4 pts to go |
| P01T | 92 | 32.6% | 32.6% |  | 25% | ✅ met |
| P01_GOLD | 596 | 25.5% | 25.5% |  | 25% | ✅ met |
| P02 | 399 | 7.3% | 7.3% |  | 15% | 🟡 8 pts to go |
| P03 | 223 | 6.7% | 6.7% |  | 15% | 🟡 8 pts to go |
| P04 | 1580 | 6.4% | 6.4% |  | 15% | 🟡 9 pts to go |
| P05 | 379 | 9.8% | 9.8% |  | 15% | 🟡 5 pts to go |
| P06M | 168 | 0.6% | 0.6% |  | 15% | ❌ 14 pts to go |
| P06T | 2440 | 0.9% | 0.9% |  | 15% | ❌ 14 pts to go |
| P06 | 165 | 9.1% | 9.1% |  | 15% | 🟡 6 pts to go |
| P07 | 252 | 4.8% | 4.8% |  | 15% | ❌ 10 pts to go |
| P08 | 3038 | 0.2% | 0.2% |  | 15% | ❌ 15 pts to go |
| P09 | 374 | 0.5% | 0.5% |  | 15% | ❌ 14 pts to go |
| P10 | 2597 | 0.3% | 0.3% |  | 15% | ❌ 15 pts to go |
| P11 | 478 | 2.9% | 2.9% |  | 15% | ❌ 12 pts to go |
| P12 | 21 | 9.5% | 9.5% |  | 15% | 🟡 6 pts to go |
| P13 | 50793 | 0.1% | 0.1% |  | 15% | ❌ 15 pts to go |

### `buyer_ap_cycle_published`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 19 | 5.3% | 5.3% |  | 20% | ❌ 15 pts to go |
| P01T | 92 | 9.8% | 9.8% |  | 20% | ❌ 10 pts to go |
| P01_GOLD | 596 | 4.4% | 4.4% |  | 20% | ❌ 16 pts to go |
| P02 | 399 | 0.3% | 0.3% |  | 20% | ❌ 20 pts to go |
| P03 | 223 | 0.4% | 0.4% |  | 20% | ❌ 20 pts to go |
| P04 | 1580 | 0.7% | 0.7% |  | 20% | ❌ 19 pts to go |
| P05 | 379 | 0.8% | 0.8% |  | 20% | ❌ 19 pts to go |
| P06M | 168 | 0.0% | 0.0% |  | 20% | ❌ 20 pts to go |
| P06T | 2440 | 0.2% | 0.2% |  | 20% | ❌ 20 pts to go |
| P06 | 165 | 3.6% | 3.6% |  | 20% | ❌ 16 pts to go |
| P07 | 252 | 0.4% | 0.4% |  | 20% | ❌ 20 pts to go |
| P08 | 3038 | 0.1% | 0.1% |  | 20% | ❌ 20 pts to go |
| P09 | 374 | 0.0% | 0.0% |  | 20% | ❌ 20 pts to go |
| P10 | 2597 | 0.1% | 0.1% |  | 20% | ❌ 20 pts to go |
| P11 | 478 | 0.4% | 0.4% |  | 20% | ❌ 20 pts to go |
| P12 | 21 | 0.0% | 0.0% |  | 20% | ❌ 20 pts to go |
| P13 | 50793 | 0.0% | 0.0% |  | 20% | ❌ 20 pts to go |

### `buyer_esignature_preference`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 19 | 5.3% | 5.3% |  | 15% | 🟡 10 pts to go |
| P01T | 92 | 7.6% | 7.6% |  | 15% | 🟡 7 pts to go |
| P01_GOLD | 596 | 8.9% | 8.9% |  | 15% | 🟡 6 pts to go |
| P02 | 399 | 3.8% | 3.8% |  | 15% | ❌ 11 pts to go |
| P03 | 223 | 7.6% | 7.6% |  | 15% | 🟡 7 pts to go |
| P04 | 1580 | 4.1% | 4.1% |  | 15% | ❌ 11 pts to go |
| P05 | 379 | 1.8% | 1.8% |  | 15% | ❌ 13 pts to go |
| P06M | 168 | 0.0% | 0.0% |  | 15% | ❌ 15 pts to go |
| P06T | 2440 | 0.3% | 0.3% |  | 15% | ❌ 15 pts to go |
| P06 | 165 | 4.2% | 4.2% |  | 15% | ❌ 11 pts to go |
| P07 | 252 | 0.4% | 0.4% |  | 15% | ❌ 15 pts to go |
| P08 | 3038 | 0.2% | 0.2% |  | 15% | ❌ 15 pts to go |
| P09 | 374 | 0.3% | 0.3% |  | 15% | ❌ 15 pts to go |
| P10 | 2597 | 0.2% | 0.2% |  | 15% | ❌ 15 pts to go |
| P11 | 478 | 0.6% | 0.6% |  | 15% | ❌ 14 pts to go |
| P12 | 21 | 0.0% | 0.0% |  | 15% | ❌ 15 pts to go |
| P13 | 50793 | 0.1% | 0.1% |  | 15% | ❌ 15 pts to go |

### `ap_system_hint`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 19 | 15.8% | 15.8% |  | 20% | 🟡 4 pts to go |
| P01T | 92 | 39.1% | 39.1% |  | 40% | 🟡 1 pts to go |
| P01_GOLD | 596 | 41.4% | 41.4% |  | 40% | ✅ met |
| P02 | 399 | 28.3% | 28.3% |  | 20% | ✅ met |
| P03 | 223 | 43.5% | 43.5% |  | 35% | ✅ met |
| P04 | 1580 | 24.6% | 24.6% |  | 20% | ✅ met |
| P05 | 379 | 13.5% | 13.5% |  | 20% | 🟡 6 pts to go |
| P06M | 168 | 2.4% | 2.4% |  | 20% | ❌ 18 pts to go |
| P06T | 2440 | 2.4% | 2.4% |  | 20% | ❌ 18 pts to go |
| P06 | 165 | 30.3% | 30.3% |  | 20% | ✅ met |
| P07 | 252 | 11.1% | 11.1% |  | 20% | 🟡 9 pts to go |
| P08 | 3038 | 0.9% | 0.9% |  | 20% | ❌ 19 pts to go |
| P09 | 374 | 16.8% | 16.8% |  | 20% | 🟡 3 pts to go |
| P10 | 2597 | 1.7% | 1.7% |  | 20% | ❌ 18 pts to go |
| P11 | 478 | 6.1% | 6.1% |  | 20% | ❌ 14 pts to go |
| P12 | 21 | 0.0% | 0.0% |  | 20% | ❌ 20 pts to go |
| P13 | 50793 | 0.5% | 0.5% |  | 20% | ❌ 20 pts to go |

## 5. contract

### `contract_value`

> ceiling: rows proven by a lobbying filing, a news release, an auditor appointment, a customer story or a vendor's client list have no contract value by nature (≈17 % of P01 Gold); bids&tenders awards now carry the awarded bidder's submitted price when no award value was published

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 19 | 0.0% | 0.0% |  | n/a | no target |
| P01T | 92 | 1.1% | 1.1% |  | n/a | no target |
| P01_GOLD | 596 | 70.6% | 70.6% |  | 95% | ❌ 24 pts to go |
| P02 | 399 | 72.9% | 72.9% |  | 95% | ❌ 22 pts to go |
| P03 | 223 | 63.2% | 63.2% |  | 90% | ❌ 27 pts to go |
| P04 | 1580 | 58.5% | 58.5% |  | 85% | ❌ 26 pts to go |
| P05 | 379 | 34.3% | 34.3% |  | 75% | ❌ 41 pts to go |
| P06M | 168 | 0.0% | 0.0% |  | n/a | no target |
| P06T | 2440 | 0.0% | 0.0% |  | n/a | no target |
| P06 | 165 | 0.0% | 0.0% |  | n/a | no target |
| P07 | 252 | 0.0% | 0.0% |  | n/a | no target |
| P08 | 3038 | 0.0% | 0.0% |  | n/a | no target |
| P09 | 374 | 90.9% | 90.9% |  | 100% | 🟡 9 pts to go |
| P10 | 2597 | 0.0% | 0.0% |  | n/a | no target |
| P11 | 478 | 19.5% | 19.5% |  | 60% | ❌ 40 pts to go |
| P12 | 21 | 100.0% | 100.0% |  | n/a | no target |
| P13 | 50793 | 0.0% | 0.0% |  | n/a | no target |

### `currency`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 19 | 0.0% | 0.0% |  | n/a | no target |
| P01T | 92 | 0.0% | 0.0% |  | n/a | no target |
| P01_GOLD | 596 | 74.2% | 74.2% |  | 100% | ❌ 26 pts to go |
| P02 | 399 | 76.7% | 76.7% |  | 100% | ❌ 23 pts to go |
| P03 | 223 | 70.4% | 70.4% |  | n/a | no target |
| P04 | 1580 | 59.9% | 59.9% |  | 95% | ❌ 35 pts to go |
| P05 | 379 | 30.6% | 30.6% |  | 80% | ❌ 49 pts to go |
| P06M | 168 | 0.0% | 0.0% |  | n/a | no target |
| P06T | 2440 | 0.0% | 0.0% |  | n/a | no target |
| P06 | 165 | 0.0% | 0.0% |  | n/a | no target |
| P07 | 252 | 0.0% | 0.0% |  | n/a | no target |
| P08 | 3038 | 0.0% | 0.0% |  | n/a | no target |
| P09 | 374 | 93.6% | 93.6% |  | 100% | 🟡 6 pts to go |
| P10 | 2597 | 0.0% | 0.0% |  | n/a | no target |
| P11 | 478 | 20.7% | 20.7% |  | n/a | no target |
| P12 | 21 | 100.0% | 100.0% |  | n/a | no target |
| P13 | 50793 | 0.0% | 0.0% |  | n/a | no target |

### `start_date`

> ceiling: most award notices publish an award date, not a start date; start_date carries the signature date when the source gives one, labelled

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 19 | 0.0% | 0.0% |  | n/a | no target |
| P01T | 92 | 1.1% | 1.1% |  | n/a | no target |
| P01_GOLD | 596 | 53.2% | 53.2% |  | 85% | ❌ 32 pts to go |
| P02 | 399 | 64.9% | 64.9% |  | 90% | ❌ 25 pts to go |
| P03 | 223 | 51.1% | 51.1% |  | 85% | ❌ 34 pts to go |
| P04 | 1580 | 64.0% | 64.0% |  | 90% | ❌ 26 pts to go |
| P05 | 379 | 35.1% | 35.1% |  | 75% | ❌ 40 pts to go |
| P06M | 168 | 0.0% | 0.0% |  | n/a | no target |
| P06T | 2440 | 0.0% | 0.0% |  | n/a | no target |
| P06 | 165 | 0.0% | 0.0% |  | n/a | no target |
| P07 | 252 | 0.0% | 0.0% |  | n/a | no target |
| P08 | 3038 | 0.0% | 0.0% |  | n/a | no target |
| P09 | 374 | 85.0% | 85.0% |  | 95% | 🟡 10 pts to go |
| P10 | 2597 | 0.0% | 0.0% |  | n/a | no target |
| P11 | 478 | 18.8% | 18.8% |  | n/a | no target |
| P12 | 21 | 0.0% | 0.0% |  | n/a | no target |
| P13 | 50793 | 0.0% | 0.0% |  | n/a | no target |

### `end_date`

> ceiling: an inferred end (award date + published duration) is labelled as such; sources without a duration leave end_date empty — the honest ceiling. P09 is BY DEFINITION the rows whose end date is not published (older SEAO contracts with no closing notice): its end_date / duration targets cannot be met without inventing a date

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 19 | 0.0% | 0.0% |  | n/a | no target |
| P01T | 92 | 1.1% | 1.1% |  | n/a | no target |
| P01_GOLD | 596 | 53.9% | 53.9% |  | 85% | ❌ 31 pts to go |
| P02 | 399 | 60.2% | 60.2% |  | 90% | ❌ 30 pts to go |
| P03 | 223 | 52.0% | 52.0% |  | 85% | ❌ 33 pts to go |
| P04 | 1580 | 53.9% | 53.9% |  | 90% | ❌ 36 pts to go |
| P05 | 379 | 42.2% | 42.2% |  | 75% | ❌ 33 pts to go |
| P06M | 168 | 0.0% | 0.0% |  | n/a | no target |
| P06T | 2440 | 0.0% | 0.0% |  | n/a | no target |
| P06 | 165 | 0.0% | 0.0% |  | n/a | no target |
| P07 | 252 | 0.0% | 0.0% |  | n/a | no target |
| P08 | 3038 | 0.0% | 0.0% |  | n/a | no target |
| P09 | 374 | 0.3% | 0.3% |  | 95% | ❌ 95 pts to go |
| P10 | 2597 | 0.0% | 0.0% |  | n/a | no target |
| P11 | 478 | 15.3% | 15.3% |  | n/a | no target |
| P12 | 21 | 0.0% | 0.0% |  | n/a | no target |
| P13 | 50793 | 0.0% | 0.0% |  | n/a | no target |

### `contract_title`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 19 | 0.0% | 0.0% |  | n/a | no target |
| P01T | 92 | 81.5% | 81.5% |  | n/a | no target |
| P01_GOLD | 596 | 86.6% | 86.6% |  | 100% | ❌ 13 pts to go |
| P02 | 399 | 80.5% | 80.5% |  | 100% | ❌ 20 pts to go |
| P03 | 223 | 91.0% | 91.0% |  | n/a | no target |
| P04 | 1580 | 72.6% | 72.6% |  | 95% | ❌ 22 pts to go |
| P05 | 379 | 75.2% | 75.2% |  | 95% | ❌ 20 pts to go |
| P06M | 168 | 0.6% | 0.6% |  | n/a | no target |
| P06T | 2440 | 83.4% | 83.4% |  | n/a | no target |
| P06 | 165 | 75.8% | 75.8% |  | n/a | no target |
| P07 | 252 | 77.0% | 77.0% |  | n/a | no target |
| P08 | 3038 | 84.9% | 85.0% |  | n/a | no target |
| P09 | 374 | 98.9% | 98.9% |  | 100% | 🟡 1 pts to go |
| P10 | 2597 | 98.4% | 98.4% |  | n/a | no target |
| P11 | 478 | 90.0% | 90.0% |  | n/a | no target |
| P12 | 21 | 100.0% | 100.0% |  | n/a | no target |
| P13 | 50793 | 0.0% | 0.0% |  | n/a | no target |

### `contract_description`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 19 | 0.0% | 0.0% |  | n/a | no target |
| P01T | 92 | 81.5% | 81.5% |  | n/a | no target |
| P01_GOLD | 596 | 89.9% | 89.9% |  | 100% | ❌ 10 pts to go |
| P02 | 399 | 81.7% | 82.0% |  | 100% | ❌ 18 pts to go |
| P03 | 223 | 91.9% | 91.9% |  | n/a | no target |
| P04 | 1580 | 79.0% | 79.0% |  | 95% | ❌ 16 pts to go |
| P05 | 379 | 90.0% | 90.0% |  | 70% | ✅ met |
| P06M | 168 | 0.6% | 0.6% |  | n/a | no target |
| P06T | 2440 | 83.4% | 83.4% |  | n/a | no target |
| P06 | 165 | 75.8% | 75.8% |  | n/a | no target |
| P07 | 252 | 77.0% | 77.0% |  | n/a | no target |
| P08 | 3038 | 84.9% | 85.0% |  | n/a | no target |
| P09 | 374 | 98.9% | 98.9% |  | 100% | 🟡 1 pts to go |
| P10 | 2597 | 98.4% | 98.4% |  | n/a | no target |
| P11 | 478 | 90.4% | 90.4% |  | n/a | no target |
| P12 | 21 | 100.0% | 100.0% |  | n/a | no target |
| P13 | 50793 | 0.0% | 0.0% |  | n/a | no target |

### `number_of_bids`

> ceiling: published by some portals only (bids&tenders submission lists, Biddingo bidder lists); federal proactive disclosure does not publish bid counts

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 19 | 0.0% | 0.0% |  | n/a | no target |
| P01T | 92 | 1.1% | 1.1% |  | n/a | no target · rows from a source that publishes bids: 3 rows, 33.3% filled |
| P01_GOLD | 596 | 18.0% | 18.0% |  | 60% | ❌ 42 pts to go · rows from a source that publishes bids: 362 rows, 29.6% filled |
| P02 | 399 | 13.3% | 13.3% |  | n/a | no target · rows from a source that publishes bids: 285 rows, 18.6% filled |
| P03 | 223 | 15.7% | 15.7% |  | n/a | no target · rows from a source that publishes bids: 138 rows, 25.4% filled |
| P04 | 1580 | 3.7% | 3.7% |  | n/a | no target · rows from a source that publishes bids: 880 rows, 6.6% filled |
| P05 | 379 | 3.4% | 3.4% |  | n/a | no target · rows from a source that publishes bids: 48 rows, 27.1% filled |
| P06M | 168 | 0.0% | 0.0% |  | n/a | no target |
| P06T | 2440 | 0.1% | 0.1% |  | n/a | no target · rows from a source that publishes bids: 4 rows, 50.0% filled |
| P06 | 165 | 0.0% | 0.0% |  | n/a | no target |
| P07 | 252 | 0.0% | 0.0% |  | n/a | no target |
| P08 | 3038 | 0.0% | 0.0% |  | n/a | no target |
| P09 | 374 | 3.2% | 3.2% |  | n/a | no target · rows from a source that publishes bids: 360 rows, 3.3% filled |
| P10 | 2597 | 0.0% | 0.0% |  | n/a | no target |
| P11 | 478 | 2.7% | 2.7% |  | n/a | no target · rows from a source that publishes bids: 98 rows, 13.3% filled |
| P12 | 21 | 0.0% | 0.0% |  | n/a | no target · rows from a source that publishes bids: 21 rows, 0.0% filled |
| P13 | 50793 | 0.0% | 0.0% |  | n/a | no target |

## 6. history

### `average_contract_duration_days`

> ceiling: needs two dates (or a published term) on the buyer's records; P09 rows (end date unpublished by definition) and buyers whose sources publish award dates only have no honest duration

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 19 | 0.0% | 100.0% |  | n/a | no target |
| P01T | 92 | 0.0% | 96.7% |  | n/a | no target |
| P01_GOLD | 596 | 55.0% | 82.4% |  | 90% | ❌ 35 pts to go |
| P02 | 399 | 60.2% | 86.2% |  | 90% | ❌ 30 pts to go |
| P03 | 223 | 52.0% | 77.1% |  | 90% | ❌ 38 pts to go |
| P04 | 1580 | 44.8% | 85.1% |  | 90% | ❌ 45 pts to go |
| P05 | 379 | 0.0% | 82.1% |  | 90% | ❌ 90 pts to go |
| P06M | 168 | 0.0% | 100.0% |  | n/a | no target |
| P06T | 2440 | 0.0% | 99.8% |  | n/a | no target |
| P06 | 165 | 0.0% | 100.0% |  | n/a | no target |
| P07 | 252 | 0.0% | 100.0% |  | n/a | no target |
| P08 | 3038 | 0.0% | 100.0% |  | n/a | no target |
| P09 | 374 | 1.3% | 2.7% |  | 90% | ❌ 89 pts to go |
| P10 | 2597 | 0.0% | 100.0% |  | n/a | no target |
| P11 | 478 | 14.0% | 90.8% |  | n/a | no target |
| P12 | 21 | 0.0% | 100.0% |  | n/a | no target |
| P13 | 50793 | 0.0% | 100.0% |  | n/a | no target |

### `commodity_distribution_top3`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 19 | 0.0% | 100.0% |  | n/a | no target |
| P01T | 92 | 0.0% | 96.7% |  | n/a | no target |
| P01_GOLD | 596 | 27.2% | 54.5% |  | 90% | ❌ 63 pts to go |
| P02 | 399 | 58.1% | 84.2% |  | n/a | no target |
| P03 | 223 | 27.4% | 52.5% |  | n/a | no target |
| P04 | 1580 | 49.6% | 89.9% |  | n/a | no target |
| P05 | 379 | 0.3% | 82.3% |  | n/a | no target |
| P06M | 168 | 0.0% | 100.0% |  | n/a | no target |
| P06T | 2440 | 0.0% | 99.8% |  | n/a | no target |
| P06 | 165 | 0.0% | 100.0% |  | n/a | no target |
| P07 | 252 | 0.0% | 100.0% |  | n/a | no target |
| P08 | 3038 | 0.0% | 100.0% |  | n/a | no target |
| P09 | 374 | 45.2% | 46.5% |  | n/a | no target |
| P10 | 2597 | 0.0% | 100.0% |  | n/a | no target |
| P11 | 478 | 12.3% | 89.1% |  | n/a | no target |
| P12 | 21 | 0.0% | 100.0% |  | n/a | no target |
| P13 | 50793 | 0.0% | 100.0% |  | n/a | no target |

### `year_over_year_spend_trend`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 19 | 0.0% | 100.0% |  | n/a | no target |
| P01T | 92 | 2.2% | 98.9% |  | n/a | no target |
| P01_GOLD | 596 | 53.5% | 80.9% |  | 95% | ❌ 42 pts to go |
| P02 | 399 | 64.2% | 90.2% |  | n/a | no target |
| P03 | 223 | 57.0% | 82.1% |  | n/a | no target |
| P04 | 1580 | 50.2% | 90.5% |  | n/a | no target |
| P05 | 379 | 4.5% | 86.5% |  | n/a | no target |
| P06M | 168 | 0.0% | 100.0% |  | n/a | no target |
| P06T | 2440 | 0.0% | 99.8% |  | n/a | no target |
| P06 | 165 | 0.0% | 100.0% |  | n/a | no target |
| P07 | 252 | 0.0% | 100.0% |  | n/a | no target |
| P08 | 3038 | 0.0% | 100.0% |  | n/a | no target |
| P09 | 374 | 69.0% | 70.3% |  | n/a | no target |
| P10 | 2597 | 0.0% | 100.0% |  | n/a | no target |
| P11 | 478 | 12.8% | 89.5% |  | n/a | no target |
| P12 | 21 | 0.0% | 100.0% |  | n/a | no target |
| P13 | 50793 | 0.0% | 100.0% |  | n/a | no target |

## 7. mail security

### `mta_sts`

> ceiling: DNS-only check; 'no record' counts as checked

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 19 | 100.0% | 100.0% |  | 100% | ✅ met |
| P01T | 92 | 100.0% | 100.0% |  | 100% | ✅ met |
| P01_GOLD | 596 | 100.0% | 100.0% |  | 100% | ✅ met |
| P02 | 399 | 100.0% | 100.0% |  | 100% | ✅ met |
| P03 | 223 | 100.0% | 100.0% |  | 100% | ✅ met |
| P04 | 1580 | 100.0% | 100.0% |  | 100% | ✅ met |
| P05 | 379 | 100.0% | 100.0% |  | 100% | ✅ met |
| P06M | 168 | 100.0% | 100.0% |  | 100% | ✅ met |
| P06T | 2440 | 100.0% | 100.0% |  | 100% | ✅ met |
| P06 | 165 | 100.0% | 100.0% |  | 100% | ✅ met |
| P07 | 252 | 100.0% | 100.0% |  | 100% | ✅ met |
| P08 | 3038 | 100.0% | 100.0% |  | 100% | ✅ met |
| P09 | 374 | 100.0% | 100.0% |  | 100% | ✅ met |
| P10 | 2597 | 100.0% | 100.0% |  | 100% | ✅ met |
| P11 | 478 | 100.0% | 100.0% |  | 100% | ✅ met |
| P12 | 21 | 100.0% | 100.0% |  | 100% | ✅ met |
| P13 | 50793 | 100.0% | 100.0% |  | 100% | ✅ met |

### `tls_rpt`

> ceiling: DNS-only check; 'no record' counts as checked

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 19 | 100.0% | 100.0% |  | 100% | ✅ met |
| P01T | 92 | 100.0% | 100.0% |  | 100% | ✅ met |
| P01_GOLD | 596 | 100.0% | 100.0% |  | 100% | ✅ met |
| P02 | 399 | 100.0% | 100.0% |  | 100% | ✅ met |
| P03 | 223 | 100.0% | 100.0% |  | 100% | ✅ met |
| P04 | 1580 | 100.0% | 100.0% |  | 100% | ✅ met |
| P05 | 379 | 100.0% | 100.0% |  | 100% | ✅ met |
| P06M | 168 | 100.0% | 100.0% |  | 100% | ✅ met |
| P06T | 2440 | 100.0% | 100.0% |  | 100% | ✅ met |
| P06 | 165 | 100.0% | 100.0% |  | 100% | ✅ met |
| P07 | 252 | 100.0% | 100.0% |  | 100% | ✅ met |
| P08 | 3038 | 100.0% | 100.0% |  | 100% | ✅ met |
| P09 | 374 | 100.0% | 100.0% |  | 100% | ✅ met |
| P10 | 2597 | 100.0% | 100.0% |  | 100% | ✅ met |
| P11 | 478 | 100.0% | 100.0% |  | 100% | ✅ met |
| P12 | 21 | 100.0% | 100.0% |  | 100% | ✅ met |
| P13 | 50793 | 100.0% | 100.0% |  | 100% | ✅ met |

### `bimi`

> ceiling: DNS-only check; 'no record' counts as checked

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 19 | 100.0% | 100.0% |  | 100% | ✅ met |
| P01T | 92 | 100.0% | 100.0% |  | 100% | ✅ met |
| P01_GOLD | 596 | 100.0% | 100.0% |  | 100% | ✅ met |
| P02 | 399 | 100.0% | 100.0% |  | 100% | ✅ met |
| P03 | 223 | 100.0% | 100.0% |  | 100% | ✅ met |
| P04 | 1580 | 100.0% | 100.0% |  | 100% | ✅ met |
| P05 | 379 | 100.0% | 100.0% |  | 100% | ✅ met |
| P06M | 168 | 100.0% | 100.0% |  | 100% | ✅ met |
| P06T | 2440 | 100.0% | 100.0% |  | 100% | ✅ met |
| P06 | 165 | 100.0% | 100.0% |  | 100% | ✅ met |
| P07 | 252 | 100.0% | 100.0% |  | 100% | ✅ met |
| P08 | 3038 | 100.0% | 100.0% |  | 100% | ✅ met |
| P09 | 374 | 100.0% | 100.0% |  | 100% | ✅ met |
| P10 | 2597 | 100.0% | 100.0% |  | 100% | ✅ met |
| P11 | 478 | 100.0% | 100.0% |  | 100% | ✅ met |
| P12 | 21 | 100.0% | 100.0% |  | 100% | ✅ met |
| P13 | 50793 | 100.0% | 100.0% |  | 100% | ✅ met |

