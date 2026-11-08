# Coverage vs the downstream team's targets — 2026-11-08

Benchmarks (field × package with a numeric target): **99 of 438 met** (22.6%); 72 within 10 points; 267 further away.
A cell counts as filled only when it carries a value: blank, `not_published`, `not_found_yet` and label-only cells ("no identifier published …", "no dataset record …", "0 in the contract dataset …") do not count; the DNS checks count when checked. `any` = share of non-blank cells incl. such labels. Δ = change since the previous build in `coord/results/coverage_history.csv`.
Rows per package: P01M 18, P01T 92, P01_GOLD 597, P02 399, P03 223, P04 1575, P05 379, P06M 168, P06T 2440, P06 165, P07 252, P08 3038, P09 374, P10 2597, P11 475, P12 21, P13 50796

## Invoice-grade readiness (the row as an invoice header: bill-to, submit-to, references, terms, tax, vendor identity, follow-up)

| package | rows | all 11 elements | ≥ 9 of 11 | median elements | most-missing element |
|---|---|---|---|---|---|
| P01M | 18 | 0.0% | 22.2% | 7 | reference to quote (PO / contract / vendor id) (18 rows) |
| P01T | 92 | 0.0% | 27.2% | 8 | reference to quote (PO / contract / vendor id) (87 rows) |
| P01_GOLD | 597 | 13.2% | 61.0% | 9 | buyer tax status (287 rows) |
| P02 | 399 | 2.8% | 44.1% | 8 | PO rule (353 rows) |
| P03 | 223 | 4.5% | 39.5% | 8 | buyer tax status (158 rows) |
| P04 | 1575 | 1.5% | 27.7% | 8 | PO rule (1418 rows) |
| P05 | 379 | 0.3% | 8.7% | 6 | payment terms (322 rows) |
| P06M | 168 | 0.0% | 1.8% | 6 | reference to quote (PO / contract / vendor id) (168 rows) |
| P06T | 2440 | 0.0% | 1.1% | 6 | reference to quote (PO / contract / vendor id) (2436 rows) |
| P06 | 165 | 0.0% | 4.2% | 5 | reference to quote (PO / contract / vendor id) (165 rows) |
| P07 | 252 | 0.0% | 0.8% | 5 | reference to quote (PO / contract / vendor id) (252 rows) |
| P08 | 3038 | 0.0% | 0.1% | 5 | reference to quote (PO / contract / vendor id) (3038 rows) |
| P09 | 374 | 0.0% | 36.6% | 8 | payment terms (351 rows) |
| P10 | 2597 | 0.0% | 0.4% | 5 | reference to quote (PO / contract / vendor id) (2595 rows) |
| P11 | 475 | 0.4% | 9.5% | 4 | PO rule (447 rows) |
| P12 | 21 | 0.0% | 38.1% | 8 | PO rule (18 rows) |
| P13 | 50796 | 0.0% | 0.0% | 5 | reference to quote (PO / contract / vendor id) (50796 rows) |

## AP grade (how stringently the row's accounts-payable data meets what an invoice needs; A = invoicing mailbox referee-confirmed on the buyer's own domain with MX, legal name, address, PO rule and terms all published, no penalties)

| package | rows | A | B | C | D | E | median ap_score |
|---|---|---|---|---|---|---|---|
| P01M | 18 | 4 | 4 | 10 | 0 | 0 | 76 |
| P01T | 92 | 16 | 49 | 27 | 0 | 0 | 79 |
| P01_GOLD | 597 | 134 | 259 | 204 | 0 | 0 | 79 |
| P02 | 399 | 0 | 84 | 315 | 0 | 0 | 63 |
| P03 | 223 | 0 | 0 | 214 | 9 | 0 | 54 |
| P04 | 1575 | 0 | 0 | 1514 | 61 | 0 | 51 |
| P05 | 379 | 10 | 32 | 320 | 17 | 0 | 49 |
| P06M | 168 | 0 | 5 | 155 | 8 | 0 | 48 |
| P06T | 2440 | 0 | 20 | 2139 | 281 | 0 | 48 |
| P06 | 165 | 15 | 34 | 116 | 0 | 0 | 70 |
| P07 | 252 | 0 | 15 | 212 | 25 | 0 | 52 |
| P08 | 3038 | 0 | 0 | 2265 | 773 | 0 | 40 |
| P09 | 374 | 4 | 11 | 358 | 1 | 0 | 51 |
| P10 | 2597 | 3 | 13 | 1864 | 717 | 0 | 40 |
| P11 | 475 | 0 | 0 | 0 | 0 | 475 | 25 |
| P12 | 21 | 1 | 1 | 19 | 0 | 0 | 53 |
| P13 | 50796 | 5 | 26 | 41193 | 9572 | 0 | 43 |

### What still blocks grade A (rows per missing element; a row counts under every element it lacks)

| package | rows not A | referee confirmation of the mailbox | an invoicing / AP mailbox (not finance / procurement / general) | a mailbox on the buyer's own domain | MX record for the mailbox domain | published bill-to legal name | invoice / billing address | published PO rule | published payment terms | clear the penalty |
|---|---|---|---|---|---|---|---|---|---|---|
| P01M | 14 | 0 | 0 | 0 | 0 | 1 | 1 | 10 | 11 | 5 |
| P01T | 76 | 0 | 0 | 0 | 1 | 4 | 4 | 28 | 40 | 59 |
| P01_GOLD | 463 | 0 | 0 | 0 | 9 | 87 | 40 | 194 | 240 | 269 |
| P02 | 399 | 0 | 399 | 0 | 2 | 37 | 11 | 353 | 326 | 232 |
| P03 | 223 | 0 | 223 | 0 | 1 | 39 | 13 | 138 | 158 | 88 |
| P04 | 1575 | 0 | 1575 | 0 | 6 | 332 | 124 | 1418 | 1284 | 958 |
| P05 | 369 | 0 | 316 | 0 | 4 | 91 | 52 | 306 | 324 | 238 |
| P06M | 168 | 0 | 168 | 0 | 0 | 19 | 46 | 156 | 141 | 95 |
| P06T | 2440 | 0 | 2440 | 0 | 23 | 868 | 484 | 2358 | 2218 | 1916 |
| P06 | 150 | 0 | 0 | 0 | 5 | 70 | 47 | 86 | 115 | 41 |
| P07 | 252 | 0 | 252 | 0 | 8 | 115 | 72 | 194 | 212 | 120 |
| P08 | 3038 | 0 | 3038 | 0 | 20 | 1912 | 1027 | 2967 | 2898 | 2067 |
| P09 | 370 | 0 | 350 | 0 | 2 | 67 | 1 | 345 | 355 | 280 |
| P10 | 2594 | 0 | 2539 | 0 | 26 | 1751 | 898 | 2544 | 2507 | 1867 |
| P11 | 475 | 475 | 439 | 0 | 9 | 355 | 230 | 447 | 447 | 306 |
| P12 | 20 | 0 | 16 | 0 | 0 | 4 | 0 | 18 | 17 | 16 |
| P13 | 50791 | 0 | 50485 | 0 | 460 | 25757 | 12378 | 50719 | 50667 | 40189 |

## Where the work is (largest gaps in rows still needed)

| field | package | now | target | rows needed |
|---|---|---|---|---|
| buyer_ap_cycle_published | P13 | 0.0% | 20% | 10152 |
| ap_system_hint | P13 | 0.5% | 20% | 9920 |
| buyer_address | P13 | 75.5% | 95% | 9881 |
| buyer_phone | P13 | 79.2% | 95% | 8021 |
| buyer_esignature_preference | P13 | 0.1% | 15% | 7581 |
| buyer_tax_exempt_status | P13 | 0.1% | 15% | 7549 |
| buyer_payment_method_preference | P13 | 0.9% | 15% | 7155 |
| buyer_logo_url | P13 | 84.2% | 95% | 5495 |
| buyer_legal_name_as_published | P13 | 49.3% | 60% | 5439 |
| buyer_bn_as_published | P13 | 21.7% | 30% | 4240 |
| buyer_legal_name_as_published | P08 | 37.1% | 75% | 1153 |
| buyer_legal_name_as_published | P10 | 32.6% | 70% | 972 |
| buyer_address | P08 | 66.1% | 95% | 879 |
| vendor_emails | P08 | 47.2% | 75% | 846 |
| buyer_address | P10 | 65.1% | 95% | 777 |
| vendor_emails | P10 | 51.3% | 80% | 745 |
| buyer_bn_as_published | P08 | 10.5% | 35% | 745 |
| vendor_registered_address | P10 | 42.4% | 70% | 718 |
| average_contract_duration_days | P04 | 44.9% | 90% | 711 |
| invoice_reference_hint | P08 | 2.3% | 25% | 689 |
| vendor_logo_url | P04 | 43.9% | 85% | 647 |
| buyer_phone | P08 | 74.8% | 95% | 616 |
| buyer_phone | P10 | 71.5% | 95% | 611 |
| buyer_ap_cycle_published | P08 | 0.2% | 20% | 603 |
| vendor_phone | P08 | 65.4% | 85% | 596 |
| invoice_reference_hint | P10 | 2.1% | 25% | 595 |
| vendor_emails | P04 | 32.6% | 70% | 590 |
| end_date | P04 | 54.0% | 90% | 568 |
| buyer_vendor_id | P04 | 4.3% | 40% | 563 |
| ap_system_hint | P08 | 1.7% | 20% | 555 |
| currency | P04 | 60.1% | 95% | 551 |
| vendor_neq | P04 | 60.1% | 95% | 550 |
| ap_phone | P04 | 50.2% | 85% | 549 |
| buyer_bn_as_published | P10 | 8.9% | 30% | 548 |
| vendor_registered_address | P08 | 52.2% | 70% | 542 |
| commodity_codes | P04 | 51.2% | 85% | 532 |
| buyer_ap_cycle_published | P10 | 0.3% | 20% | 513 |
| vendor_phone | P10 | 66.1% | 85% | 492 |
| vendor_phone | P04 | 33.9% | 65% | 490 |
| buyer_ap_cycle_published | P06T | 0.2% | 20% | 483 |

## 1. identifiers

### `invoice_reference_hint`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 18 | 44.4% | 44.4% |  | 50% | 🟡 6 pts to go |
| P01T | 92 | 71.7% | 71.7% |  | 50% | ✅ met |
| P01_GOLD | 597 | 92.5% | 94.8% |  | 95% | 🟡 2 pts to go |
| P02 | 399 | 79.4% | 81.5% |  | 95% | ❌ 16 pts to go |
| P03 | 223 | 86.5% | 92.4% |  | 95% | 🟡 8 pts to go |
| P04 | 1575 | 68.8% | 71.4% |  | 90% | ❌ 21 pts to go |
| P05 | 379 | 40.4% | 43.3% |  | 70% | ❌ 30 pts to go |
| P06M | 168 | 7.1% | 7.1% |  | n/a | no target |
| P06T | 2440 | 3.5% | 3.6% |  | n/a | no target |
| P06 | 165 | 47.9% | 47.9% |  | 30% | ✅ met |
| P07 | 252 | 23.0% | 23.0% |  | 30% | 🟡 7 pts to go |
| P08 | 3038 | 2.3% | 2.3% |  | 25% | ❌ 23 pts to go |
| P09 | 374 | 98.9% | 99.7% |  | 100% | 🟡 1 pts to go |
| P10 | 2597 | 2.1% | 3.0% |  | 25% | ❌ 23 pts to go |
| P11 | 475 | 24.6% | 27.6% |  | 60% | ❌ 35 pts to go |
| P12 | 21 | 100.0% | 100.0% |  | 100% | ✅ met |
| P13 | 50796 | 0.2% | 0.3% |  | 0% by design | — leave (by design) |

### `po_number_as_published`

> ceiling: a purchase-order number exists only where the buyer publishes PO-level data (Montréal, Laval, Toronto open data so far) or the record itself carries one; most sources publish awards, not POs — the target cannot be reached from public data for most buyers

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 18 | 0.0% | 0.0% |  | n/a | no target |
| P01T | 92 | 0.0% | 0.0% |  | 10% | 🟡 10 pts to go |
| P01_GOLD | 597 | 6.4% | 6.4% |  | 50% | ❌ 44 pts to go |
| P02 | 399 | 7.5% | 7.5% |  | 50% | ❌ 42 pts to go |
| P03 | 223 | 1.8% | 1.8% |  | 40% | ❌ 38 pts to go |
| P04 | 1575 | 1.1% | 1.1% |  | 30% | ❌ 29 pts to go |
| P05 | 379 | 0.3% | 0.3% |  | 20% | ❌ 20 pts to go |
| P06M | 168 | 0.0% | 0.0% |  | n/a | no target |
| P06T | 2440 | 0.0% | 0.0% |  | n/a | no target |
| P06 | 165 | 0.0% | 0.0% |  | n/a | no target |
| P07 | 252 | 0.0% | 0.0% |  | n/a | no target |
| P08 | 3038 | 0.0% | 0.0% |  | n/a | no target |
| P09 | 374 | 0.5% | 0.5% |  | 50% | ❌ 50 pts to go |
| P10 | 2597 | 0.1% | 0.1% |  | n/a | no target |
| P11 | 475 | 0.8% | 0.8% |  | n/a | no target |
| P12 | 21 | 0.0% | 0.0% |  | n/a | no target |
| P13 | 50796 | 0.0% | 0.0% |  | n/a | no target |

### `contract_or_agreement_number`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 18 | 0.0% | 0.0% |  | n/a | no target |
| P01T | 92 | 5.4% | 5.4% |  | 50% | ❌ 45 pts to go |
| P01_GOLD | 597 | 69.7% | 69.7% |  | 85% | ❌ 15 pts to go |
| P02 | 399 | 73.7% | 73.7% |  | 90% | ❌ 16 pts to go |
| P03 | 223 | 70.9% | 70.9% |  | 85% | ❌ 14 pts to go |
| P04 | 1575 | 65.6% | 65.6% |  | 85% | ❌ 19 pts to go |
| P05 | 379 | 30.1% | 30.1% |  | 60% | ❌ 30 pts to go |
| P06M | 168 | 0.0% | 0.0% |  | n/a | no target |
| P06T | 2440 | 0.2% | 0.2% |  | n/a | no target |
| P06 | 165 | 0.0% | 0.0% |  | n/a | no target |
| P07 | 252 | 0.0% | 0.0% |  | n/a | no target |
| P08 | 3038 | 0.0% | 0.0% |  | n/a | no target |
| P09 | 374 | 96.5% | 96.5% |  | 100% | 🟡 4 pts to go |
| P10 | 2597 | 0.0% | 0.0% |  | n/a | no target |
| P11 | 475 | 20.8% | 20.8% |  | 60% | ❌ 39 pts to go |
| P12 | 21 | 100.0% | 100.0% |  | n/a | no target |
| P13 | 50796 | 0.0% | 0.0% |  | n/a | no target |

### `solicitation_or_tender_number`

> ceiling: SEAO's 'numero' is the organisation's own reference for the notice (SEAO data dictionary) and is reported here; sources that publish awards under a tender number only (bids&tenders, SaskTenders, BC) also carry it as the contract reference, labelled

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 18 | 0.0% | 0.0% |  | n/a | no target |
| P01T | 92 | 2.2% | 2.2% |  | 30% | ❌ 28 pts to go |
| P01_GOLD | 597 | 53.3% | 53.3% |  | 80% | ❌ 27 pts to go |
| P02 | 399 | 64.9% | 64.9% |  | 60% | ✅ met |
| P03 | 223 | 58.3% | 58.3% |  | 80% | ❌ 22 pts to go |
| P04 | 1575 | 54.5% | 54.5% |  | 50% | ✅ met |
| P05 | 379 | 12.4% | 12.4% |  | 40% | ❌ 28 pts to go |
| P06M | 168 | 0.0% | 0.0% |  | n/a | no target |
| P06T | 2440 | 0.2% | 0.2% |  | n/a | no target |
| P06 | 165 | 0.0% | 0.0% |  | n/a | no target |
| P07 | 252 | 0.0% | 0.0% |  | n/a | no target |
| P08 | 3038 | 0.0% | 0.0% |  | n/a | no target |
| P09 | 374 | 87.4% | 87.4% |  | 50% | ✅ met |
| P10 | 2597 | 0.0% | 0.0% |  | n/a | no target |
| P11 | 475 | 17.9% | 17.9% |  | 40% | ❌ 22 pts to go |
| P12 | 21 | 100.0% | 100.0% |  | 100% | ✅ met |
| P13 | 50796 | 0.0% | 0.0% |  | n/a | no target |

### `award_or_notice_id`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 18 | 0.0% | 0.0% |  | n/a | no target |
| P01T | 92 | 3.3% | 3.3% |  | n/a | no target |
| P01_GOLD | 597 | 63.0% | 63.0% |  | 85% | ❌ 22 pts to go |
| P02 | 399 | 64.2% | 64.2% |  | 90% | ❌ 26 pts to go |
| P03 | 223 | 69.1% | 69.1% |  | 85% | ❌ 16 pts to go |
| P04 | 1575 | 56.3% | 56.3% |  | 85% | ❌ 29 pts to go |
| P05 | 379 | 20.3% | 20.3% |  | 50% | ❌ 30 pts to go |
| P06M | 168 | 0.0% | 0.0% |  | n/a | no target |
| P06T | 2440 | 0.2% | 0.2% |  | n/a | no target |
| P06 | 165 | 0.0% | 0.0% |  | n/a | no target |
| P07 | 252 | 0.0% | 0.0% |  | n/a | no target |
| P08 | 3038 | 0.0% | 0.0% |  | n/a | no target |
| P09 | 374 | 97.1% | 97.1% |  | 100% | 🟡 3 pts to go |
| P10 | 2597 | 0.0% | 0.0% |  | n/a | no target |
| P11 | 475 | 19.8% | 19.8% |  | 60% | ❌ 40 pts to go |
| P12 | 21 | 100.0% | 100.0% |  | n/a | no target |
| P13 | 50796 | 0.0% | 0.0% |  | n/a | no target |

### `buyer_vendor_id`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 18 | 0.0% | 0.0% |  | n/a | no target |
| P01T | 92 | 2.2% | 2.2% |  | n/a | no target |
| P01_GOLD | 597 | 13.1% | 13.1% |  | 60% | ❌ 47 pts to go |
| P02 | 399 | 7.8% | 7.8% |  | 50% | ❌ 42 pts to go |
| P03 | 223 | 10.3% | 10.3% |  | 50% | ❌ 40 pts to go |
| P04 | 1575 | 4.3% | 4.3% |  | 40% | ❌ 36 pts to go |
| P05 | 379 | 1.3% | 1.3% |  | 20% | ❌ 19 pts to go |
| P06M | 168 | 0.0% | 0.0% |  | n/a | no target |
| P06T | 2440 | 0.1% | 0.1% |  | n/a | no target |
| P06 | 165 | 0.0% | 0.0% |  | n/a | no target |
| P07 | 252 | 0.0% | 0.0% |  | n/a | no target |
| P08 | 3038 | 0.0% | 0.0% |  | n/a | no target |
| P09 | 374 | 2.4% | 2.4% |  | 50% | ❌ 48 pts to go |
| P10 | 2597 | 0.0% | 0.0% |  | n/a | no target |
| P11 | 475 | 4.2% | 4.2% |  | n/a | no target |
| P12 | 21 | 0.0% | 0.0% |  | n/a | no target |
| P13 | 50796 | 0.0% | 0.0% |  | n/a | no target |

### `commodity_codes`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 18 | 0.0% | 0.0% |  | n/a | no target |
| P01T | 92 | 0.0% | 0.0% |  | n/a | no target |
| P01_GOLD | 597 | 36.5% | 36.5% |  | 80% | ❌ 44 pts to go |
| P02 | 399 | 58.9% | 58.9% |  | 90% | ❌ 31 pts to go |
| P03 | 223 | 36.3% | 36.3% |  | 80% | ❌ 44 pts to go |
| P04 | 1575 | 51.2% | 51.2% |  | 85% | ❌ 34 pts to go |
| P05 | 379 | 5.0% | 5.0% |  | 50% | ❌ 45 pts to go |
| P06M | 168 | 0.0% | 0.0% |  | n/a | no target |
| P06T | 2440 | 0.0% | 0.0% |  | n/a | no target |
| P06 | 165 | 0.0% | 0.0% |  | n/a | no target |
| P07 | 252 | 0.0% | 0.0% |  | n/a | no target |
| P08 | 3038 | 0.0% | 0.0% |  | n/a | no target |
| P09 | 374 | 75.7% | 75.7% |  | 95% | ❌ 19 pts to go |
| P10 | 2597 | 0.0% | 0.0% |  | n/a | no target |
| P11 | 475 | 13.7% | 13.7% |  | 50% | ❌ 36 pts to go |
| P12 | 21 | 0.0% | 0.0% |  | n/a | no target |
| P13 | 50796 | 0.0% | 0.0% |  | n/a | no target |

### `buyer_org_codes`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 18 | 0.0% | 0.0% |  | n/a | no target |
| P01T | 92 | 1.1% | 1.1% |  | n/a | no target |
| P01_GOLD | 597 | 8.5% | 8.5% |  | 50% | ❌ 42 pts to go |
| P02 | 399 | 7.5% | 7.5% |  | 50% | ❌ 42 pts to go |
| P03 | 223 | 2.7% | 2.7% |  | 30% | ❌ 27 pts to go |
| P04 | 1575 | 1.1% | 1.1% |  | 30% | ❌ 29 pts to go |
| P05 | 379 | 0.0% | 0.0% |  | n/a | no target |
| P06M | 168 | 0.0% | 0.0% |  | n/a | no target |
| P06T | 2440 | 0.0% | 0.0% |  | n/a | no target |
| P06 | 165 | 0.0% | 0.0% |  | n/a | no target |
| P07 | 252 | 0.0% | 0.0% |  | n/a | no target |
| P08 | 3038 | 0.0% | 0.0% |  | n/a | no target |
| P09 | 374 | 0.3% | 0.3% |  | n/a | no target |
| P10 | 2597 | 0.0% | 0.0% |  | n/a | no target |
| P11 | 475 | 0.8% | 0.8% |  | n/a | no target |
| P12 | 21 | 0.0% | 0.0% |  | n/a | no target |
| P13 | 50796 | 0.0% | 0.0% |  | n/a | no target |

### `records_with_this_vendor`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 18 | 100.0% | 100.0% |  | n/a | no target |
| P01T | 92 | 100.0% | 100.0% |  | 60% | ✅ met |
| P01_GOLD | 597 | 100.0% | 100.0% |  | 100% | ✅ met |
| P02 | 399 | 100.0% | 100.0% |  | 100% | ✅ met |
| P03 | 223 | 100.0% | 100.0% |  | 100% | ✅ met |
| P04 | 1575 | 100.0% | 100.0% |  | 95% | ✅ met |
| P05 | 379 | 100.0% | 100.0% |  | 70% | ✅ met |
| P06M | 168 | 100.0% | 100.0% |  | n/a | no target |
| P06T | 2440 | 100.0% | 100.0% |  | n/a | no target |
| P06 | 165 | 100.0% | 100.0% |  | 50% | ✅ met |
| P07 | 252 | 100.0% | 100.0% |  | n/a | no target |
| P08 | 3038 | 100.0% | 100.0% |  | n/a | no target |
| P09 | 374 | 100.0% | 100.0% |  | 100% | ✅ met |
| P10 | 2597 | 100.0% | 100.0% |  | n/a | no target |
| P11 | 475 | 100.0% | 100.0% |  | 70% | ✅ met |
| P12 | 21 | 100.0% | 100.0% |  | n/a | no target |
| P13 | 50796 | 0.0% | 0.0% |  | n/a | no target |

## 2. vendor

### `vendor_bn9`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 18 | 100.0% | 100.0% |  | 70% | ✅ met |
| P01T | 92 | 80.4% | 80.4% |  | 60% | ✅ met |
| P01_GOLD | 597 | 78.2% | 78.2% |  | 90% | ❌ 12 pts to go |
| P02 | 399 | 65.9% | 65.9% |  | 85% | ❌ 19 pts to go |
| P03 | 223 | 80.7% | 80.7% |  | 90% | 🟡 9 pts to go |
| P04 | 1575 | 53.6% | 53.6% |  | 75% | ❌ 21 pts to go |
| P05 | 379 | 52.8% | 52.8% |  | 50% | ✅ met |
| P06M | 168 | 74.4% | 74.4% |  | n/a | no target |
| P06T | 2440 | 60.7% | 60.7% |  | n/a | no target |
| P06 | 165 | 46.7% | 46.7% |  | 40% | ✅ met |
| P07 | 252 | 40.1% | 40.1% |  | 50% | 🟡 10 pts to go |
| P08 | 3038 | 41.8% | 41.8% |  | 50% | 🟡 8 pts to go |
| P09 | 374 | 54.8% | 54.8% |  | 80% | ❌ 25 pts to go |
| P10 | 2597 | 36.6% | 36.6% |  | 40% | 🟡 3 pts to go |
| P11 | 475 | 44.6% | 44.6% |  | 60% | ❌ 15 pts to go |
| P12 | 21 | 52.4% | 52.4% |  | 85% | ❌ 33 pts to go |
| P13 | 50796 | 91.7% | 91.7% |  | 0% by design | — leave (by design) |

### `vendor_registered_address`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 18 | 61.1% | 61.1% |  | n/a | no target |
| P01T | 92 | 63.0% | 63.0% |  | n/a | no target |
| P01_GOLD | 597 | 75.2% | 75.2% |  | 95% | ❌ 20 pts to go |
| P02 | 399 | 81.7% | 81.7% |  | 95% | ❌ 13 pts to go |
| P03 | 223 | 76.7% | 76.7% |  | 95% | ❌ 18 pts to go |
| P04 | 1575 | 78.6% | 78.6% |  | 95% | ❌ 16 pts to go |
| P05 | 379 | 55.7% | 55.7% |  | 70% | ❌ 14 pts to go |
| P06M | 168 | 20.8% | 20.8% |  | n/a | no target |
| P06T | 2440 | 78.3% | 78.3% |  | n/a | no target |
| P06 | 165 | 55.2% | 55.2% |  | 80% | ❌ 25 pts to go |
| P07 | 252 | 52.0% | 52.0% |  | 70% | ❌ 18 pts to go |
| P08 | 3038 | 52.2% | 52.2% |  | 70% | ❌ 18 pts to go |
| P09 | 374 | 89.6% | 89.6% |  | 100% | ❌ 10 pts to go |
| P10 | 2597 | 42.4% | 42.4% |  | 70% | ❌ 28 pts to go |
| P11 | 475 | 53.9% | 53.9% |  | 75% | ❌ 21 pts to go |
| P12 | 21 | 100.0% | 100.0% |  | n/a | no target |
| P13 | 50796 | 0.0% | 0.0% |  | n/a | no target |

### `vendor_trading_name`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 18 | 50.0% | 50.0% |  | n/a | no target |
| P01T | 92 | 19.6% | 19.6% |  | n/a | no target |
| P01_GOLD | 597 | 53.8% | 53.8% |  | 60% | 🟡 6 pts to go |
| P02 | 399 | 66.2% | 66.2% |  | 60% | ✅ met |
| P03 | 223 | 62.3% | 62.3% |  | 60% | ✅ met |
| P04 | 1575 | 55.6% | 55.6% |  | 55% | ✅ met |
| P05 | 379 | 25.3% | 25.3% |  | 50% | ❌ 25 pts to go |
| P06M | 168 | 17.3% | 17.3% |  | n/a | no target |
| P06T | 2440 | 53.6% | 53.6% |  | n/a | no target |
| P06 | 165 | 52.7% | 52.7% |  | n/a | no target |
| P07 | 252 | 46.8% | 46.8% |  | 55% | 🟡 8 pts to go |
| P08 | 3038 | 49.2% | 49.2% |  | 50% | 🟡 1 pts to go |
| P09 | 374 | 73.0% | 73.0% |  | 70% | ✅ met |
| P10 | 2597 | 52.7% | 52.7% |  | 55% | 🟡 2 pts to go |
| P11 | 475 | 43.4% | 43.4% |  | 50% | 🟡 7 pts to go |
| P12 | 21 | 85.7% | 85.7% |  | n/a | no target |
| P13 | 50796 | 0.0% | 0.0% |  | n/a | no target |

### `vendor_phone`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 18 | 38.9% | 38.9% |  | n/a | no target |
| P01T | 92 | 0.0% | 0.0% |  | n/a | no target |
| P01_GOLD | 597 | 33.7% | 33.7% |  | 70% | ❌ 36 pts to go |
| P02 | 399 | 41.9% | 41.9% |  | 70% | ❌ 28 pts to go |
| P03 | 223 | 40.8% | 40.8% |  | 70% | ❌ 29 pts to go |
| P04 | 1575 | 33.9% | 33.9% |  | 65% | ❌ 31 pts to go |
| P05 | 379 | 17.2% | 17.2% |  | 60% | ❌ 43 pts to go |
| P06M | 168 | 6.5% | 6.5% |  | n/a | no target |
| P06T | 2440 | 0.0% | 0.0% |  | n/a | no target |
| P06 | 165 | 59.4% | 59.4% |  | 40% | ✅ met |
| P07 | 252 | 65.9% | 65.9% |  | 85% | ❌ 19 pts to go |
| P08 | 3038 | 65.4% | 65.4% |  | 85% | ❌ 20 pts to go |
| P09 | 374 | 54.0% | 54.0% |  | 85% | ❌ 31 pts to go |
| P10 | 2597 | 66.1% | 66.1% |  | 85% | ❌ 19 pts to go |
| P11 | 475 | 50.7% | 50.7% |  | 75% | ❌ 24 pts to go |
| P12 | 21 | 9.5% | 9.5% |  | n/a | no target |
| P13 | 50796 | 100.0% | 100.0% |  | 60% | ✅ met |

### `vendor_website`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 18 | 94.4% | 94.4% |  | n/a | no target |
| P01T | 92 | 90.2% | 90.2% |  | n/a | no target |
| P01_GOLD | 597 | 90.1% | 90.1% |  | 90% | ✅ met |
| P02 | 399 | 82.5% | 82.5% |  | 90% | 🟡 8 pts to go |
| P03 | 223 | 84.3% | 84.3% |  | 90% | 🟡 6 pts to go |
| P04 | 1575 | 80.1% | 80.1% |  | 85% | 🟡 5 pts to go |
| P05 | 379 | 50.1% | 50.1% |  | 70% | ❌ 20 pts to go |
| P06M | 168 | 67.9% | 67.9% |  | n/a | no target |
| P06T | 2440 | 77.9% | 77.9% |  | n/a | no target |
| P06 | 165 | 97.0% | 97.0% |  | 50% | ✅ met |
| P07 | 252 | 96.8% | 96.8% |  | 100% | 🟡 3 pts to go |
| P08 | 3038 | 96.1% | 96.1% |  | 100% | 🟡 4 pts to go |
| P09 | 374 | 81.0% | 81.0% |  | 100% | ❌ 19 pts to go |
| P10 | 2597 | 100.0% | 100.0% |  | 100% | ✅ met |
| P11 | 475 | 92.6% | 92.6% |  | 100% | 🟡 7 pts to go |
| P12 | 21 | 42.9% | 42.9% |  | n/a | no target |
| P13 | 50796 | 100.0% | 100.0% |  | n/a | no target |

### `vendor_emails`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 18 | 38.9% | 38.9% |  | n/a | no target |
| P01T | 92 | 0.0% | 0.0% |  | n/a | no target |
| P01_GOLD | 597 | 36.7% | 36.7% |  | 70% | ❌ 33 pts to go |
| P02 | 399 | 44.1% | 44.1% |  | 75% | ❌ 31 pts to go |
| P03 | 223 | 42.2% | 42.2% |  | 75% | ❌ 33 pts to go |
| P04 | 1575 | 32.6% | 32.6% |  | 70% | ❌ 37 pts to go |
| P05 | 379 | 13.7% | 13.7% |  | 55% | ❌ 41 pts to go |
| P06M | 168 | 6.5% | 6.5% |  | n/a | no target |
| P06T | 2440 | 0.0% | 0.0% |  | n/a | no target |
| P06 | 165 | 40.0% | 40.0% |  | n/a | no target |
| P07 | 252 | 35.7% | 35.7% |  | 70% | ❌ 34 pts to go |
| P08 | 3038 | 47.2% | 47.2% |  | 75% | ❌ 28 pts to go |
| P09 | 374 | 52.4% | 52.4% |  | 85% | ❌ 33 pts to go |
| P10 | 2597 | 51.3% | 51.3% |  | 80% | ❌ 29 pts to go |
| P11 | 475 | 36.8% | 36.8% |  | 70% | ❌ 33 pts to go |
| P12 | 21 | 19.0% | 19.0% |  | n/a | no target |
| P13 | 50796 | 0.0% | 0.0% |  | n/a | no target |

### `vendor_logo_url`

> ceiling: needs the vendor's website first; sites that block automated readers (robots.txt / 403) are never read

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 18 | 38.9% | 38.9% |  | n/a | no target |
| P01T | 92 | 0.0% | 0.0% |  | n/a | no target |
| P01_GOLD | 597 | 49.2% | 49.2% |  | 90% | ❌ 41 pts to go |
| P02 | 399 | 57.6% | 57.6% |  | 90% | ❌ 32 pts to go |
| P03 | 223 | 56.5% | 56.5% |  | 90% | ❌ 34 pts to go |
| P04 | 1575 | 43.9% | 43.9% |  | 85% | ❌ 41 pts to go |
| P05 | 379 | 22.4% | 22.4% |  | 75% | ❌ 53 pts to go |
| P06M | 168 | 6.5% | 6.5% |  | n/a | no target |
| P06T | 2440 | 0.0% | 0.0% |  | n/a | no target |
| P06 | 165 | 87.9% | 87.9% |  | n/a | no target |
| P07 | 252 | 88.1% | 88.1% |  | 100% | ❌ 12 pts to go |
| P08 | 3038 | 85.7% | 85.7% |  | 100% | ❌ 14 pts to go |
| P09 | 374 | 60.4% | 60.4% |  | n/a | no target |
| P10 | 2597 | 88.7% | 88.7% |  | 100% | ❌ 11 pts to go |
| P11 | 475 | 66.1% | 66.1% |  | n/a | no target |
| P12 | 21 | 19.0% | 19.0% |  | n/a | no target |
| P13 | 50796 | 0.0% | 0.0% |  | n/a | no target |

### `vendor_neq`

> ceiling: only Québec-registered vendors have an NEQ; the share of QC vendors is reported next to the rate

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 18 | 0.0% | 0.0% |  | n/a | no target |
| P01T | 92 | 21.7% | 21.7% |  | n/a | no target · QC vendors: 2 rows, 100.0% filled |
| P01_GOLD | 597 | 49.1% | 49.1% |  | 95% | ❌ 46 pts to go · QC vendors: 52 rows, 98.1% filled |
| P02 | 399 | 67.2% | 67.2% |  | 95% | ❌ 28 pts to go · QC vendors: 98 rows, 100.0% filled |
| P03 | 223 | 53.8% | 53.8% |  | 95% | ❌ 41 pts to go · QC vendors: 16 rows, 100.0% filled |
| P04 | 1575 | 60.1% | 60.1% |  | 95% | ❌ 35 pts to go · QC vendors: 439 rows, 98.6% filled |
| P05 | 379 | 13.7% | 13.7% |  | n/a | no target · QC vendors: 26 rows, 92.3% filled |
| P06M | 168 | 0.0% | 0.0% |  | n/a | no target |
| P06T | 2440 | 55.9% | 55.9% |  | n/a | no target · QC vendors: 56 rows, 100.0% filled |
| P06 | 165 | 24.2% | 24.2% |  | n/a | no target · QC vendors: 16 rows, 100.0% filled |
| P07 | 252 | 19.4% | 19.4% |  | n/a | no target · QC vendors: 26 rows, 96.2% filled |
| P08 | 3038 | 26.9% | 26.9% |  | n/a | no target · QC vendors: 544 rows, 98.5% filled |
| P09 | 374 | 81.8% | 81.8% |  | 95% | ❌ 13 pts to go · QC vendors: 156 rows, 99.4% filled |
| P10 | 2597 | 22.8% | 22.8% |  | n/a | no target · QC vendors: 444 rows, 94.6% filled |
| P11 | 475 | 28.0% | 28.0% |  | n/a | no target · QC vendors: 77 rows, 98.7% filled |
| P12 | 21 | 76.2% | 76.2% |  | n/a | no target · QC vendors: 4 rows, 100.0% filled |
| P13 | 50796 | 0.0% | 0.0% |  | n/a | no target |

### `vendor_years_in_business`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 18 | 61.1% | 61.1% |  | n/a | no target · vendors with a registry record: 11 rows, 100.0% filled |
| P01T | 92 | 63.0% | 63.0% |  | n/a | no target · vendors with a registry record: 58 rows, 100.0% filled |
| P01_GOLD | 597 | 84.9% | 84.9% |  | 100% | ❌ 15 pts to go · vendors with a registry record: 507 rows, 100.0% filled |
| P02 | 399 | 88.0% | 88.0% |  | 100% | ❌ 12 pts to go · vendors with a registry record: 351 rows, 100.0% filled |
| P03 | 223 | 87.4% | 87.4% |  | 100% | ❌ 13 pts to go · vendors with a registry record: 195 rows, 100.0% filled |
| P04 | 1575 | 81.3% | 81.3% |  | 100% | ❌ 19 pts to go · vendors with a registry record: 1281 rows, 100.0% filled |
| P05 | 379 | 61.2% | 61.2% |  | n/a | no target · vendors with a registry record: 232 rows, 100.0% filled |
| P06M | 168 | 20.8% | 20.8% |  | n/a | no target · vendors with a registry record: 35 rows, 100.0% filled |
| P06T | 2440 | 78.3% | 78.3% |  | n/a | no target · vendors with a registry record: 1910 rows, 100.0% filled |
| P06 | 165 | 58.2% | 58.2% |  | n/a | no target · vendors with a registry record: 96 rows, 100.0% filled |
| P07 | 252 | 54.4% | 54.4% |  | n/a | no target · vendors with a registry record: 137 rows, 100.0% filled |
| P08 | 3038 | 54.3% | 54.3% |  | n/a | no target · vendors with a registry record: 1651 rows, 100.0% filled |
| P09 | 374 | 92.8% | 92.8% |  | n/a | no target · vendors with a registry record: 347 rows, 100.0% filled |
| P10 | 2597 | 43.6% | 43.6% |  | n/a | no target · vendors with a registry record: 1133 rows, 100.0% filled |
| P11 | 475 | 57.3% | 57.3% |  | n/a | no target · vendors with a registry record: 272 rows, 100.0% filled |
| P12 | 21 | 100.0% | 100.0% |  | n/a | no target · vendors with a registry record: 21 rows, 100.0% filled |
| P13 | 50796 | 0.0% | 0.0% |  | n/a | no target |

## 3. buyer

### `buyer_legal_name_as_published`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 18 | 94.4% | 94.4% |  | 90% | ✅ met |
| P01T | 92 | 95.7% | 95.7% |  | 90% | ✅ met |
| P01_GOLD | 597 | 85.4% | 85.4% |  | 95% | 🟡 10 pts to go |
| P02 | 399 | 90.7% | 90.7% |  | 95% | 🟡 4 pts to go |
| P03 | 223 | 82.5% | 82.5% |  | 85% | 🟡 2 pts to go |
| P04 | 1575 | 78.9% | 78.9% |  | 90% | ❌ 11 pts to go |
| P05 | 379 | 76.0% | 76.0% |  | 75% | ✅ met |
| P06M | 168 | 88.7% | 88.7% |  | n/a | no target |
| P06T | 2440 | 64.4% | 64.4% |  | n/a | no target |
| P06 | 165 | 57.6% | 57.6% |  | 80% | ❌ 22 pts to go |
| P07 | 252 | 54.4% | 54.4% |  | 80% | ❌ 26 pts to go |
| P08 | 3038 | 37.1% | 37.1% |  | 75% | ❌ 38 pts to go |
| P09 | 374 | 82.1% | 82.1% |  | 95% | ❌ 13 pts to go |
| P10 | 2597 | 32.6% | 32.6% |  | 70% | ❌ 37 pts to go |
| P11 | 475 | 25.3% | 25.3% |  | 65% | ❌ 40 pts to go |
| P12 | 21 | 81.0% | 81.0% |  | 80% | ✅ met |
| P13 | 50796 | 49.3% | 49.3% |  | 60% | ❌ 11 pts to go |

### `buyer_bn_as_published`

> ceiling: a buyer's BN is public only where the buyer prints it or a public dataset carries it (CRA charities, federal grants & contributions recipients, business registries for corporations); municipalities rarely publish theirs

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 18 | 38.9% | 38.9% |  | 50% | ❌ 11 pts to go |
| P01T | 92 | 20.7% | 20.7% |  | n/a | no target |
| P01_GOLD | 597 | 20.6% | 20.6% |  | 40% | ❌ 19 pts to go |
| P02 | 399 | 22.3% | 22.3% |  | 40% | ❌ 18 pts to go |
| P03 | 223 | 26.5% | 26.5% |  | 40% | ❌ 14 pts to go |
| P04 | 1575 | 27.5% | 27.5% |  | 40% | ❌ 12 pts to go |
| P05 | 379 | 23.5% | 23.5% |  | 25% | 🟡 2 pts to go |
| P06M | 168 | 25.6% | 25.6% |  | n/a | no target |
| P06T | 2440 | 30.9% | 30.9% |  | n/a | no target |
| P06 | 165 | 9.7% | 9.7% |  | 35% | ❌ 25 pts to go |
| P07 | 252 | 9.9% | 9.9% |  | 35% | ❌ 25 pts to go |
| P08 | 3038 | 10.5% | 10.5% |  | 35% | ❌ 24 pts to go |
| P09 | 374 | 17.9% | 17.9% |  | n/a | no target |
| P10 | 2597 | 8.9% | 8.9% |  | 30% | ❌ 21 pts to go |
| P11 | 475 | 8.4% | 8.4% |  | n/a | no target |
| P12 | 21 | 19.0% | 19.0% |  | n/a | no target |
| P13 | 50796 | 21.7% | 21.7% |  | 30% | 🟡 8 pts to go |

### `buyer_address`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 18 | 94.4% | 94.4% |  | 100% | 🟡 6 pts to go |
| P01T | 92 | 93.5% | 93.5% |  | 100% | 🟡 6 pts to go |
| P01_GOLD | 597 | 89.4% | 89.4% |  | 100% | ❌ 11 pts to go |
| P02 | 399 | 96.5% | 96.5% |  | 100% | 🟡 4 pts to go |
| P03 | 223 | 94.2% | 94.2% |  | 100% | 🟡 6 pts to go |
| P04 | 1575 | 90.9% | 90.9% |  | 100% | 🟡 9 pts to go |
| P05 | 379 | 85.2% | 85.2% |  | 100% | ❌ 15 pts to go |
| P06M | 168 | 72.0% | 72.0% |  | n/a | no target |
| P06T | 2440 | 80.0% | 80.0% |  | n/a | no target |
| P06 | 165 | 68.5% | 68.5% |  | 95% | ❌ 26 pts to go |
| P07 | 252 | 70.2% | 70.2% |  | 95% | ❌ 25 pts to go |
| P08 | 3038 | 66.1% | 66.1% |  | 95% | ❌ 29 pts to go |
| P09 | 374 | 98.4% | 98.4% |  | 100% | 🟡 2 pts to go |
| P10 | 2597 | 65.1% | 65.1% |  | 95% | ❌ 30 pts to go |
| P11 | 475 | 36.2% | 36.2% |  | 80% | ❌ 44 pts to go |
| P12 | 21 | 100.0% | 100.0% |  | 100% | ✅ met |
| P13 | 50796 | 75.5% | 75.6% |  | 95% | ❌ 20 pts to go |

### `buyer_phone`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 18 | 88.9% | 88.9% |  | n/a | no target |
| P01T | 92 | 80.4% | 80.4% |  | n/a | no target |
| P01_GOLD | 597 | 70.4% | 70.4% |  | 90% | ❌ 20 pts to go |
| P02 | 399 | 78.2% | 78.2% |  | 95% | ❌ 17 pts to go |
| P03 | 223 | 74.9% | 74.9% |  | 95% | ❌ 20 pts to go |
| P04 | 1575 | 85.0% | 85.0% |  | 95% | 🟡 10 pts to go |
| P05 | 379 | 75.7% | 75.7% |  | 90% | ❌ 14 pts to go |
| P06M | 168 | 83.9% | 83.9% |  | n/a | no target |
| P06T | 2440 | 77.2% | 77.2% |  | n/a | no target |
| P06 | 165 | 64.2% | 64.2% |  | 95% | ❌ 31 pts to go |
| P07 | 252 | 66.3% | 66.3% |  | 90% | ❌ 24 pts to go |
| P08 | 3038 | 74.8% | 74.8% |  | 95% | ❌ 20 pts to go |
| P09 | 374 | 89.6% | 89.6% |  | 100% | ❌ 10 pts to go |
| P10 | 2597 | 71.5% | 71.5% |  | 95% | ❌ 24 pts to go |
| P11 | 475 | 29.1% | 29.1% |  | 75% | ❌ 46 pts to go |
| P12 | 21 | 85.7% | 85.7% |  | n/a | no target |
| P13 | 50796 | 79.2% | 79.2% |  | 95% | ❌ 16 pts to go |

### `buyer_logo_url`

> ceiling: sites that block automated readers (robots.txt / 403) are never read; an og:image that looks like a photo is labelled

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 18 | 77.8% | 77.8% |  | n/a | no target |
| P01T | 92 | 91.3% | 91.3% |  | 95% | 🟡 4 pts to go |
| P01_GOLD | 597 | 70.2% | 70.2% |  | 90% | ❌ 20 pts to go |
| P02 | 399 | 81.5% | 81.5% |  | 95% | ❌ 14 pts to go |
| P03 | 223 | 72.6% | 72.6% |  | 95% | ❌ 22 pts to go |
| P04 | 1575 | 65.7% | 65.7% |  | 90% | ❌ 24 pts to go |
| P05 | 379 | 79.2% | 79.2% |  | 95% | ❌ 16 pts to go |
| P06M | 168 | 85.1% | 85.1% |  | n/a | no target |
| P06T | 2440 | 93.8% | 93.8% |  | n/a | no target |
| P06 | 165 | 90.3% | 90.3% |  | 100% | 🟡 10 pts to go |
| P07 | 252 | 87.7% | 87.7% |  | 100% | ❌ 12 pts to go |
| P08 | 3038 | 90.6% | 90.6% |  | 100% | 🟡 9 pts to go |
| P09 | 374 | 54.8% | 54.8% |  | n/a | no target |
| P10 | 2597 | 90.0% | 90.0% |  | 100% | 🟡 10 pts to go |
| P11 | 475 | 33.9% | 33.9% |  | 80% | ❌ 46 pts to go |
| P12 | 21 | 61.9% | 61.9% |  | n/a | no target |
| P13 | 50796 | 84.2% | 84.2% |  | 95% | ❌ 11 pts to go |

## 4. AP

### `ap_contact_name_as_published`

> ceiling: owner 2026-11-08: the AP contact person the organisation itself names on its AP / finance page is allowed (name + role phrase, quoted); mailboxes stay organisational; many bodies publish no AP person

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 18 | 16.7% | 16.7% |  | n/a | no target |
| P01T | 92 | 23.9% | 23.9% |  | n/a | no target |
| P01_GOLD | 597 | 13.7% | 13.7% |  | 25% | ❌ 11 pts to go |
| P02 | 399 | 19.8% | 19.8% |  | 40% | ❌ 20 pts to go |
| P03 | 223 | 4.5% | 4.5% |  | 20% | ❌ 16 pts to go |
| P04 | 1575 | 3.8% | 3.8% |  | 20% | ❌ 16 pts to go |
| P05 | 379 | 2.1% | 2.1% |  | 15% | ❌ 13 pts to go |
| P06M | 168 | 1.8% | 1.8% |  | n/a | no target |
| P06T | 2440 | 1.2% | 1.2% |  | n/a | no target |
| P06 | 165 | 5.5% | 5.5% |  | n/a | no target |
| P07 | 252 | 6.3% | 6.3% |  | n/a | no target |
| P08 | 3038 | 0.3% | 0.3% |  | n/a | no target |
| P09 | 374 | 5.6% | 5.6% |  | n/a | no target |
| P10 | 2597 | 0.5% | 0.5% |  | n/a | no target |
| P11 | 475 | 1.9% | 1.9% |  | n/a | no target |
| P12 | 21 | 9.5% | 9.5% |  | n/a | no target |
| P13 | 50796 | 0.2% | 0.2% |  | n/a | no target |

### `ap_phone`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 18 | 38.9% | 38.9% |  | n/a | no target |
| P01T | 92 | 34.8% | 34.8% |  | 70% | ❌ 35 pts to go |
| P01_GOLD | 597 | 43.4% | 43.4% |  | 80% | ❌ 37 pts to go |
| P02 | 399 | 64.2% | 64.2% |  | 90% | ❌ 26 pts to go |
| P03 | 223 | 21.5% | 21.5% |  | 60% | ❌ 38 pts to go |
| P04 | 1575 | 50.2% | 50.2% |  | 85% | ❌ 35 pts to go |
| P05 | 379 | 12.9% | 12.9% |  | 50% | ❌ 37 pts to go |
| P06M | 168 | 6.0% | 6.0% |  | n/a | no target |
| P06T | 2440 | 2.3% | 2.3% |  | n/a | no target |
| P06 | 165 | 18.2% | 18.2% |  | n/a | no target |
| P07 | 252 | 19.0% | 19.0% |  | n/a | no target |
| P08 | 3038 | 0.5% | 0.5% |  | n/a | no target |
| P09 | 374 | 81.0% | 81.0% |  | 95% | ❌ 14 pts to go |
| P10 | 2597 | 3.1% | 3.1% |  | n/a | no target |
| P11 | 475 | 30.5% | 30.5% |  | n/a | no target |
| P12 | 21 | 33.3% | 33.3% |  | n/a | no target |
| P13 | 50796 | 1.0% | 1.0% |  | n/a | no target |

### `invoice_mailing_address`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 18 | 0.0% | 0.0% |  | n/a | no target |
| P01T | 92 | 16.3% | 16.3% |  | n/a | no target |
| P01_GOLD | 597 | 33.5% | 33.5% |  | 70% | ❌ 36 pts to go |
| P02 | 399 | 42.6% | 42.6% |  | 75% | ❌ 32 pts to go |
| P03 | 223 | 21.1% | 21.1% |  | 55% | ❌ 34 pts to go |
| P04 | 1575 | 49.8% | 49.8% |  | 75% | ❌ 25 pts to go |
| P05 | 379 | 11.1% | 11.1% |  | 50% | ❌ 39 pts to go |
| P06M | 168 | 1.8% | 1.8% |  | n/a | no target |
| P06T | 2440 | 1.1% | 1.1% |  | n/a | no target |
| P06 | 165 | 10.3% | 10.3% |  | n/a | no target |
| P07 | 252 | 10.3% | 10.3% |  | n/a | no target |
| P08 | 3038 | 0.5% | 0.5% |  | n/a | no target |
| P09 | 374 | 77.5% | 77.5% |  | 95% | ❌ 18 pts to go |
| P10 | 2597 | 1.8% | 1.8% |  | n/a | no target |
| P11 | 475 | 29.5% | 29.5% |  | n/a | no target |
| P12 | 21 | 19.0% | 19.0% |  | n/a | no target |
| P13 | 50796 | 0.6% | 0.6% |  | n/a | no target |

### `invoicing_requirements`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 18 | 16.7% | 16.7% |  | n/a | no target |
| P01T | 92 | 19.6% | 19.6% |  | n/a | no target |
| P01_GOLD | 597 | 55.9% | 56.1% |  | 80% | ❌ 24 pts to go |
| P02 | 399 | 45.4% | 45.4% |  | 75% | ❌ 30 pts to go |
| P03 | 223 | 33.6% | 33.6% |  | 70% | ❌ 36 pts to go |
| P04 | 1575 | 39.8% | 39.8% |  | 70% | ❌ 30 pts to go |
| P05 | 379 | 15.0% | 15.0% |  | 50% | ❌ 35 pts to go |
| P06M | 168 | 4.2% | 4.2% |  | n/a | no target |
| P06T | 2440 | 1.4% | 1.4% |  | n/a | no target |
| P06 | 165 | 23.6% | 23.6% |  | n/a | no target |
| P07 | 252 | 5.2% | 5.2% |  | n/a | no target |
| P08 | 3038 | 1.0% | 1.0% |  | n/a | no target |
| P09 | 374 | 42.2% | 42.2% |  | 80% | ❌ 38 pts to go |
| P10 | 2597 | 1.5% | 1.6% |  | n/a | no target |
| P11 | 475 | 17.3% | 17.3% |  | n/a | no target |
| P12 | 21 | 38.1% | 38.1% |  | n/a | no target |
| P13 | 50796 | 0.3% | 0.3% |  | n/a | no target |

### `payment_terms_as_published`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 18 | 38.9% | 38.9% |  | n/a | no target |
| P01T | 92 | 56.5% | 56.5% |  | 60% | 🟡 4 pts to go |
| P01_GOLD | 597 | 59.8% | 59.8% |  | 70% | ❌ 10 pts to go |
| P02 | 399 | 18.3% | 18.3% |  | 50% | ❌ 32 pts to go |
| P03 | 223 | 29.1% | 29.1% |  | 55% | ❌ 26 pts to go |
| P04 | 1575 | 18.5% | 18.5% |  | 40% | ❌ 22 pts to go |
| P05 | 379 | 14.5% | 14.5% |  | 40% | ❌ 26 pts to go |
| P06M | 168 | 16.1% | 16.1% |  | n/a | no target |
| P06T | 2440 | 9.1% | 9.1% |  | n/a | no target |
| P06 | 165 | 30.3% | 30.3% |  | n/a | no target |
| P07 | 252 | 15.9% | 15.9% |  | n/a | no target |
| P08 | 3038 | 4.6% | 4.6% |  | n/a | no target |
| P09 | 374 | 5.1% | 5.1% |  | n/a | no target |
| P10 | 2597 | 3.5% | 3.5% |  | n/a | no target |
| P11 | 475 | 5.9% | 5.9% |  | n/a | no target |
| P12 | 21 | 19.0% | 19.0% |  | n/a | no target |
| P13 | 50796 | 0.3% | 0.3% |  | n/a | no target |

### `po_required_as_published`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 18 | 44.4% | 44.4% |  | n/a | no target |
| P01T | 92 | 69.6% | 69.6% |  | 65% | ✅ met |
| P01_GOLD | 597 | 67.5% | 67.5% |  | 70% | 🟡 2 pts to go |
| P02 | 399 | 11.5% | 11.5% |  | 50% | ❌ 38 pts to go |
| P03 | 223 | 38.1% | 38.1% |  | 60% | ❌ 22 pts to go |
| P04 | 1575 | 10.0% | 10.0% |  | 40% | ❌ 30 pts to go |
| P05 | 379 | 19.3% | 19.3% |  | 45% | ❌ 26 pts to go |
| P06M | 168 | 7.1% | 7.1% |  | n/a | no target |
| P06T | 2440 | 3.4% | 3.4% |  | n/a | no target |
| P06 | 165 | 47.9% | 47.9% |  | n/a | no target |
| P07 | 252 | 23.0% | 23.0% |  | n/a | no target |
| P08 | 3038 | 2.3% | 2.3% |  | n/a | no target |
| P09 | 374 | 7.8% | 7.8% |  | n/a | no target |
| P10 | 2597 | 2.0% | 2.0% |  | n/a | no target |
| P11 | 475 | 5.9% | 5.9% |  | n/a | no target |
| P12 | 21 | 14.3% | 14.3% |  | n/a | no target |
| P13 | 50796 | 0.2% | 0.2% |  | n/a | no target |

### `invoice_portal_url`

> ceiling: only portals the buyer names on its own pages; informational tax-authority links are not portals

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 18 | 11.1% | 11.1% |  | n/a | no target |
| P01T | 92 | 44.6% | 44.6% |  | n/a | no target |
| P01_GOLD | 597 | 49.4% | 49.4% |  | 50% | 🟡 1 pts to go |
| P02 | 399 | 30.8% | 30.8% |  | n/a | no target |
| P03 | 223 | 54.7% | 54.7% |  | 60% | 🟡 5 pts to go |
| P04 | 1575 | 24.1% | 24.1% |  | n/a | no target |
| P05 | 379 | 15.6% | 15.6% |  | n/a | no target |
| P06M | 168 | 4.2% | 4.2% |  | n/a | no target |
| P06T | 2440 | 2.7% | 2.7% |  | n/a | no target |
| P06 | 165 | 35.2% | 35.2% |  | n/a | no target |
| P07 | 252 | 17.9% | 17.9% |  | n/a | no target |
| P08 | 3038 | 1.5% | 1.5% |  | n/a | no target |
| P09 | 374 | 19.3% | 19.3% |  | n/a | no target |
| P10 | 2597 | 2.3% | 2.3% |  | n/a | no target |
| P11 | 475 | 6.9% | 6.9% |  | n/a | no target |
| P12 | 21 | 19.0% | 19.0% |  | n/a | no target |
| P13 | 50796 | 0.4% | 0.4% |  | n/a | no target |

### `buyer_payment_method_preference`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 18 | 27.8% | 27.8% |  | 15% | ✅ met |
| P01T | 92 | 29.3% | 29.3% |  | 15% | ✅ met |
| P01_GOLD | 597 | 35.3% | 35.3% |  | 40% | 🟡 5 pts to go |
| P02 | 399 | 9.0% | 9.3% |  | 25% | ❌ 16 pts to go |
| P03 | 223 | 15.7% | 15.7% |  | 25% | 🟡 9 pts to go |
| P04 | 1575 | 5.1% | 5.1% |  | 15% | 🟡 10 pts to go |
| P05 | 379 | 6.9% | 6.9% |  | 15% | 🟡 8 pts to go |
| P06M | 168 | 6.0% | 6.0% |  | 15% | 🟡 9 pts to go |
| P06T | 2440 | 1.4% | 1.4% |  | 15% | ❌ 14 pts to go |
| P06 | 165 | 11.5% | 11.5% |  | 15% | 🟡 4 pts to go |
| P07 | 252 | 7.1% | 7.1% |  | 15% | 🟡 8 pts to go |
| P08 | 3038 | 1.2% | 1.2% |  | 15% | ❌ 14 pts to go |
| P09 | 374 | 0.8% | 0.8% |  | 15% | ❌ 14 pts to go |
| P10 | 2597 | 1.5% | 1.5% |  | 15% | ❌ 14 pts to go |
| P11 | 475 | 1.3% | 1.3% |  | 15% | ❌ 14 pts to go |
| P12 | 21 | 4.8% | 4.8% |  | 15% | ❌ 10 pts to go |
| P13 | 50796 | 0.9% | 0.9% |  | 15% | ❌ 14 pts to go |

### `buyer_tax_exempt_status`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 18 | 11.1% | 11.1% |  | 15% | 🟡 4 pts to go |
| P01T | 92 | 32.6% | 32.6% |  | 25% | ✅ met |
| P01_GOLD | 597 | 26.3% | 26.3% |  | 25% | ✅ met |
| P02 | 399 | 9.3% | 9.3% |  | 15% | 🟡 6 pts to go |
| P03 | 223 | 9.0% | 9.0% |  | 15% | 🟡 6 pts to go |
| P04 | 1575 | 6.8% | 6.8% |  | 15% | 🟡 8 pts to go |
| P05 | 379 | 11.3% | 11.3% |  | 15% | 🟡 4 pts to go |
| P06M | 168 | 2.4% | 2.4% |  | 15% | ❌ 13 pts to go |
| P06T | 2440 | 2.0% | 2.0% |  | 15% | ❌ 13 pts to go |
| P06 | 165 | 12.1% | 12.1% |  | 15% | 🟡 3 pts to go |
| P07 | 252 | 7.5% | 7.5% |  | 15% | 🟡 8 pts to go |
| P08 | 3038 | 0.9% | 0.9% |  | 15% | ❌ 14 pts to go |
| P09 | 374 | 0.5% | 0.5% |  | 15% | ❌ 14 pts to go |
| P10 | 2597 | 1.3% | 1.3% |  | 15% | ❌ 14 pts to go |
| P11 | 475 | 3.8% | 3.8% |  | 15% | ❌ 11 pts to go |
| P12 | 21 | 23.8% | 23.8% |  | 15% | ✅ met |
| P13 | 50796 | 0.1% | 0.1% |  | 15% | ❌ 15 pts to go |

### `buyer_ap_cycle_published`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 18 | 5.6% | 5.6% |  | 20% | ❌ 14 pts to go |
| P01T | 92 | 9.8% | 9.8% |  | 20% | ❌ 10 pts to go |
| P01_GOLD | 597 | 4.4% | 4.4% |  | 20% | ❌ 16 pts to go |
| P02 | 399 | 0.3% | 0.3% |  | 20% | ❌ 20 pts to go |
| P03 | 223 | 0.4% | 0.4% |  | 20% | ❌ 20 pts to go |
| P04 | 1575 | 1.0% | 1.0% |  | 20% | ❌ 19 pts to go |
| P05 | 379 | 1.1% | 1.1% |  | 20% | ❌ 19 pts to go |
| P06M | 168 | 0.0% | 0.0% |  | 20% | ❌ 20 pts to go |
| P06T | 2440 | 0.2% | 0.2% |  | 20% | ❌ 20 pts to go |
| P06 | 165 | 3.6% | 3.6% |  | 20% | ❌ 16 pts to go |
| P07 | 252 | 0.8% | 0.8% |  | 20% | ❌ 19 pts to go |
| P08 | 3038 | 0.2% | 0.2% |  | 20% | ❌ 20 pts to go |
| P09 | 374 | 0.0% | 0.0% |  | 20% | ❌ 20 pts to go |
| P10 | 2597 | 0.3% | 0.3% |  | 20% | ❌ 20 pts to go |
| P11 | 475 | 0.4% | 0.4% |  | 20% | ❌ 20 pts to go |
| P12 | 21 | 0.0% | 0.0% |  | 20% | ❌ 20 pts to go |
| P13 | 50796 | 0.0% | 0.0% |  | 20% | ❌ 20 pts to go |

### `buyer_esignature_preference`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 18 | 5.6% | 5.6% |  | 15% | 🟡 9 pts to go |
| P01T | 92 | 7.6% | 7.6% |  | 15% | 🟡 7 pts to go |
| P01_GOLD | 597 | 9.2% | 9.2% |  | 15% | 🟡 6 pts to go |
| P02 | 399 | 5.3% | 5.3% |  | 15% | 🟡 10 pts to go |
| P03 | 223 | 9.4% | 9.4% |  | 15% | 🟡 6 pts to go |
| P04 | 1575 | 4.4% | 4.4% |  | 15% | ❌ 11 pts to go |
| P05 | 379 | 2.4% | 2.4% |  | 15% | ❌ 13 pts to go |
| P06M | 168 | 2.4% | 2.4% |  | 15% | ❌ 13 pts to go |
| P06T | 2440 | 0.8% | 0.8% |  | 15% | ❌ 14 pts to go |
| P06 | 165 | 5.5% | 5.5% |  | 15% | 🟡 10 pts to go |
| P07 | 252 | 2.4% | 2.4% |  | 15% | ❌ 13 pts to go |
| P08 | 3038 | 0.7% | 0.7% |  | 15% | ❌ 14 pts to go |
| P09 | 374 | 0.5% | 0.5% |  | 15% | ❌ 14 pts to go |
| P10 | 2597 | 0.7% | 0.7% |  | 15% | ❌ 14 pts to go |
| P11 | 475 | 1.1% | 1.1% |  | 15% | ❌ 14 pts to go |
| P12 | 21 | 4.8% | 4.8% |  | 15% | ❌ 10 pts to go |
| P13 | 50796 | 0.1% | 0.1% |  | 15% | ❌ 15 pts to go |

### `ap_system_hint`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 18 | 11.1% | 11.1% |  | 20% | 🟡 9 pts to go |
| P01T | 92 | 41.3% | 41.3% |  | 40% | ✅ met |
| P01_GOLD | 597 | 44.4% | 44.4% |  | 40% | ✅ met |
| P02 | 399 | 34.1% | 34.1% |  | 20% | ✅ met |
| P03 | 223 | 46.2% | 46.2% |  | 35% | ✅ met |
| P04 | 1575 | 27.9% | 27.9% |  | 20% | ✅ met |
| P05 | 379 | 14.5% | 14.5% |  | 20% | 🟡 6 pts to go |
| P06M | 168 | 4.2% | 4.2% |  | 20% | ❌ 16 pts to go |
| P06T | 2440 | 3.0% | 3.0% |  | 20% | ❌ 17 pts to go |
| P06 | 165 | 33.9% | 33.9% |  | 20% | ✅ met |
| P07 | 252 | 13.9% | 13.9% |  | 20% | 🟡 6 pts to go |
| P08 | 3038 | 1.7% | 1.7% |  | 20% | ❌ 18 pts to go |
| P09 | 374 | 22.5% | 22.5% |  | 20% | ✅ met |
| P10 | 2597 | 2.3% | 2.3% |  | 20% | ❌ 18 pts to go |
| P11 | 475 | 7.4% | 7.4% |  | 20% | ❌ 13 pts to go |
| P12 | 21 | 14.3% | 14.3% |  | 20% | 🟡 6 pts to go |
| P13 | 50796 | 0.5% | 0.5% |  | 20% | ❌ 20 pts to go |

## 5. contract

### `contract_value`

> ceiling: rows proven by a lobbying filing, a news release, an auditor appointment, a customer story or a vendor's client list have no contract value by nature (≈17 % of P01 Gold); bids&tenders awards now carry the awarded bidder's submitted price when no award value was published

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 18 | 0.0% | 0.0% |  | n/a | no target |
| P01T | 92 | 1.1% | 1.1% |  | n/a | no target |
| P01_GOLD | 597 | 70.5% | 70.5% |  | 95% | ❌ 24 pts to go |
| P02 | 399 | 72.9% | 72.9% |  | 95% | ❌ 22 pts to go |
| P03 | 223 | 63.2% | 63.2% |  | 90% | ❌ 27 pts to go |
| P04 | 1575 | 58.7% | 58.7% |  | 85% | ❌ 26 pts to go |
| P05 | 379 | 34.3% | 34.3% |  | 75% | ❌ 41 pts to go |
| P06M | 168 | 0.0% | 0.0% |  | n/a | no target |
| P06T | 2440 | 0.0% | 0.0% |  | n/a | no target |
| P06 | 165 | 0.0% | 0.0% |  | n/a | no target |
| P07 | 252 | 0.0% | 0.0% |  | n/a | no target |
| P08 | 3038 | 0.0% | 0.0% |  | n/a | no target |
| P09 | 374 | 90.9% | 90.9% |  | 100% | 🟡 9 pts to go |
| P10 | 2597 | 0.0% | 0.0% |  | n/a | no target |
| P11 | 475 | 18.9% | 18.9% |  | 60% | ❌ 41 pts to go |
| P12 | 21 | 100.0% | 100.0% |  | n/a | no target |
| P13 | 50796 | 0.0% | 0.0% |  | n/a | no target |

### `currency`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 18 | 0.0% | 0.0% |  | n/a | no target |
| P01T | 92 | 0.0% | 0.0% |  | n/a | no target |
| P01_GOLD | 597 | 74.0% | 74.0% |  | 100% | ❌ 26 pts to go |
| P02 | 399 | 76.7% | 76.7% |  | 100% | ❌ 23 pts to go |
| P03 | 223 | 70.4% | 70.4% |  | n/a | no target |
| P04 | 1575 | 60.1% | 60.1% |  | 95% | ❌ 35 pts to go |
| P05 | 379 | 30.6% | 30.6% |  | 80% | ❌ 49 pts to go |
| P06M | 168 | 0.0% | 0.0% |  | n/a | no target |
| P06T | 2440 | 0.0% | 0.0% |  | n/a | no target |
| P06 | 165 | 0.0% | 0.0% |  | n/a | no target |
| P07 | 252 | 0.0% | 0.0% |  | n/a | no target |
| P08 | 3038 | 0.0% | 0.0% |  | n/a | no target |
| P09 | 374 | 93.6% | 93.6% |  | 100% | 🟡 6 pts to go |
| P10 | 2597 | 0.0% | 0.0% |  | n/a | no target |
| P11 | 475 | 20.2% | 20.2% |  | n/a | no target |
| P12 | 21 | 100.0% | 100.0% |  | n/a | no target |
| P13 | 50796 | 0.0% | 0.0% |  | n/a | no target |

### `start_date`

> ceiling: most award notices publish an award date, not a start date; start_date carries the signature date when the source gives one, labelled

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 18 | 0.0% | 0.0% |  | n/a | no target |
| P01T | 92 | 1.1% | 1.1% |  | n/a | no target |
| P01_GOLD | 597 | 53.1% | 53.1% |  | 85% | ❌ 32 pts to go |
| P02 | 399 | 64.9% | 64.9% |  | 90% | ❌ 25 pts to go |
| P03 | 223 | 51.1% | 51.1% |  | 85% | ❌ 34 pts to go |
| P04 | 1575 | 64.1% | 64.1% |  | 90% | ❌ 26 pts to go |
| P05 | 379 | 35.1% | 35.1% |  | 75% | ❌ 40 pts to go |
| P06M | 168 | 0.0% | 0.0% |  | n/a | no target |
| P06T | 2440 | 0.0% | 0.0% |  | n/a | no target |
| P06 | 165 | 0.0% | 0.0% |  | n/a | no target |
| P07 | 252 | 0.0% | 0.0% |  | n/a | no target |
| P08 | 3038 | 0.0% | 0.0% |  | n/a | no target |
| P09 | 374 | 85.0% | 85.0% |  | 95% | 🟡 10 pts to go |
| P10 | 2597 | 0.0% | 0.0% |  | n/a | no target |
| P11 | 475 | 18.3% | 18.3% |  | n/a | no target |
| P12 | 21 | 0.0% | 0.0% |  | n/a | no target |
| P13 | 50796 | 0.0% | 0.0% |  | n/a | no target |

### `end_date`

> ceiling: an inferred end (award date + published duration) is labelled as such; sources without a duration leave end_date empty — the honest ceiling. P09 is BY DEFINITION the rows whose end date is not published (older SEAO contracts with no closing notice): its end_date / duration targets cannot be met without inventing a date

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 18 | 0.0% | 0.0% |  | n/a | no target |
| P01T | 92 | 1.1% | 1.1% |  | n/a | no target |
| P01_GOLD | 597 | 53.8% | 53.8% |  | 85% | ❌ 31 pts to go |
| P02 | 399 | 60.2% | 60.2% |  | 90% | ❌ 30 pts to go |
| P03 | 223 | 52.0% | 52.0% |  | 85% | ❌ 33 pts to go |
| P04 | 1575 | 54.0% | 54.0% |  | 90% | ❌ 36 pts to go |
| P05 | 379 | 42.2% | 42.2% |  | 75% | ❌ 33 pts to go |
| P06M | 168 | 0.0% | 0.0% |  | n/a | no target |
| P06T | 2440 | 0.0% | 0.0% |  | n/a | no target |
| P06 | 165 | 0.0% | 0.0% |  | n/a | no target |
| P07 | 252 | 0.0% | 0.0% |  | n/a | no target |
| P08 | 3038 | 0.0% | 0.0% |  | n/a | no target |
| P09 | 374 | 0.3% | 0.3% |  | 95% | ❌ 95 pts to go |
| P10 | 2597 | 0.0% | 0.0% |  | n/a | no target |
| P11 | 475 | 14.7% | 14.7% |  | n/a | no target |
| P12 | 21 | 0.0% | 0.0% |  | n/a | no target |
| P13 | 50796 | 0.0% | 0.0% |  | n/a | no target |

### `contract_title`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 18 | 0.0% | 0.0% |  | n/a | no target |
| P01T | 92 | 81.5% | 81.5% |  | n/a | no target |
| P01_GOLD | 597 | 86.4% | 86.4% |  | 100% | ❌ 14 pts to go |
| P02 | 399 | 80.5% | 80.5% |  | 100% | ❌ 20 pts to go |
| P03 | 223 | 91.0% | 91.0% |  | n/a | no target |
| P04 | 1575 | 72.6% | 72.6% |  | 95% | ❌ 22 pts to go |
| P05 | 379 | 75.2% | 75.2% |  | 95% | ❌ 20 pts to go |
| P06M | 168 | 0.6% | 0.6% |  | n/a | no target |
| P06T | 2440 | 83.4% | 83.4% |  | n/a | no target |
| P06 | 165 | 75.8% | 75.8% |  | n/a | no target |
| P07 | 252 | 77.0% | 77.0% |  | n/a | no target |
| P08 | 3038 | 84.9% | 85.0% |  | n/a | no target |
| P09 | 374 | 98.9% | 98.9% |  | 100% | 🟡 1 pts to go |
| P10 | 2597 | 98.4% | 98.4% |  | n/a | no target |
| P11 | 475 | 89.9% | 89.9% |  | n/a | no target |
| P12 | 21 | 100.0% | 100.0% |  | n/a | no target |
| P13 | 50796 | 0.0% | 0.0% |  | n/a | no target |

### `contract_description`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 18 | 0.0% | 0.0% |  | n/a | no target |
| P01T | 92 | 81.5% | 81.5% |  | n/a | no target |
| P01_GOLD | 597 | 89.8% | 89.8% |  | 100% | ❌ 10 pts to go |
| P02 | 399 | 81.7% | 82.0% |  | 100% | ❌ 18 pts to go |
| P03 | 223 | 91.9% | 91.9% |  | n/a | no target |
| P04 | 1575 | 79.0% | 79.0% |  | 95% | ❌ 16 pts to go |
| P05 | 379 | 90.0% | 90.0% |  | 70% | ✅ met |
| P06M | 168 | 0.6% | 0.6% |  | n/a | no target |
| P06T | 2440 | 83.4% | 83.4% |  | n/a | no target |
| P06 | 165 | 75.8% | 75.8% |  | n/a | no target |
| P07 | 252 | 77.0% | 77.0% |  | n/a | no target |
| P08 | 3038 | 84.9% | 85.0% |  | n/a | no target |
| P09 | 374 | 98.9% | 98.9% |  | 100% | 🟡 1 pts to go |
| P10 | 2597 | 98.4% | 98.4% |  | n/a | no target |
| P11 | 475 | 90.3% | 90.3% |  | n/a | no target |
| P12 | 21 | 100.0% | 100.0% |  | n/a | no target |
| P13 | 50796 | 0.0% | 0.0% |  | n/a | no target |

### `number_of_bids`

> ceiling: published by some portals only (bids&tenders submission lists, Biddingo bidder lists); federal proactive disclosure does not publish bid counts

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 18 | 0.0% | 0.0% |  | n/a | no target |
| P01T | 92 | 1.1% | 1.1% |  | n/a | no target · rows from a source that publishes bids: 3 rows, 33.3% filled |
| P01_GOLD | 597 | 17.9% | 17.9% |  | 60% | ❌ 42 pts to go · rows from a source that publishes bids: 362 rows, 29.6% filled |
| P02 | 399 | 13.3% | 13.3% |  | n/a | no target · rows from a source that publishes bids: 285 rows, 18.6% filled |
| P03 | 223 | 15.7% | 15.7% |  | n/a | no target · rows from a source that publishes bids: 138 rows, 25.4% filled |
| P04 | 1575 | 3.7% | 3.7% |  | n/a | no target · rows from a source that publishes bids: 879 rows, 6.6% filled |
| P05 | 379 | 3.4% | 3.4% |  | n/a | no target · rows from a source that publishes bids: 48 rows, 27.1% filled |
| P06M | 168 | 0.0% | 0.0% |  | n/a | no target |
| P06T | 2440 | 0.1% | 0.1% |  | n/a | no target · rows from a source that publishes bids: 4 rows, 50.0% filled |
| P06 | 165 | 0.0% | 0.0% |  | n/a | no target |
| P07 | 252 | 0.0% | 0.0% |  | n/a | no target |
| P08 | 3038 | 0.0% | 0.0% |  | n/a | no target |
| P09 | 374 | 3.2% | 3.2% |  | n/a | no target · rows from a source that publishes bids: 360 rows, 3.3% filled |
| P10 | 2597 | 0.0% | 0.0% |  | n/a | no target |
| P11 | 475 | 2.7% | 2.7% |  | n/a | no target · rows from a source that publishes bids: 95 rows, 13.7% filled |
| P12 | 21 | 0.0% | 0.0% |  | n/a | no target · rows from a source that publishes bids: 21 rows, 0.0% filled |
| P13 | 50796 | 0.0% | 0.0% |  | n/a | no target |

## 6. history

### `average_contract_duration_days`

> ceiling: needs two dates (or a published term) on the buyer's records; P09 rows (end date unpublished by definition) and buyers whose sources publish award dates only have no honest duration

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 18 | 0.0% | 100.0% |  | n/a | no target |
| P01T | 92 | 0.0% | 96.7% |  | n/a | no target |
| P01_GOLD | 597 | 54.9% | 82.4% |  | 90% | ❌ 35 pts to go |
| P02 | 399 | 60.2% | 86.2% |  | 90% | ❌ 30 pts to go |
| P03 | 223 | 52.0% | 77.1% |  | 90% | ❌ 38 pts to go |
| P04 | 1575 | 44.9% | 85.1% |  | 90% | ❌ 45 pts to go |
| P05 | 379 | 0.0% | 82.1% |  | 90% | ❌ 90 pts to go |
| P06M | 168 | 0.0% | 100.0% |  | n/a | no target |
| P06T | 2440 | 0.0% | 99.8% |  | n/a | no target |
| P06 | 165 | 0.0% | 100.0% |  | n/a | no target |
| P07 | 252 | 0.0% | 100.0% |  | n/a | no target |
| P08 | 3038 | 0.0% | 100.0% |  | n/a | no target |
| P09 | 374 | 1.3% | 2.7% |  | 90% | ❌ 89 pts to go |
| P10 | 2597 | 0.0% | 100.0% |  | n/a | no target |
| P11 | 475 | 13.5% | 90.7% |  | n/a | no target |
| P12 | 21 | 0.0% | 100.0% |  | n/a | no target |
| P13 | 50796 | 0.0% | 100.0% |  | n/a | no target |

### `commodity_distribution_top3`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 18 | 0.0% | 100.0% |  | n/a | no target |
| P01T | 92 | 0.0% | 96.7% |  | n/a | no target |
| P01_GOLD | 597 | 27.1% | 54.6% |  | 90% | ❌ 63 pts to go |
| P02 | 399 | 58.1% | 84.2% |  | n/a | no target |
| P03 | 223 | 27.4% | 52.5% |  | n/a | no target |
| P04 | 1575 | 49.7% | 89.9% |  | n/a | no target |
| P05 | 379 | 0.3% | 82.3% |  | n/a | no target |
| P06M | 168 | 0.0% | 100.0% |  | n/a | no target |
| P06T | 2440 | 0.0% | 99.8% |  | n/a | no target |
| P06 | 165 | 0.0% | 100.0% |  | n/a | no target |
| P07 | 252 | 0.0% | 100.0% |  | n/a | no target |
| P08 | 3038 | 0.0% | 100.0% |  | n/a | no target |
| P09 | 374 | 45.2% | 46.5% |  | n/a | no target |
| P10 | 2597 | 0.0% | 100.0% |  | n/a | no target |
| P11 | 475 | 12.2% | 89.5% |  | n/a | no target |
| P12 | 21 | 0.0% | 100.0% |  | n/a | no target |
| P13 | 50796 | 0.0% | 100.0% |  | n/a | no target |

### `year_over_year_spend_trend`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 18 | 0.0% | 100.0% |  | n/a | no target |
| P01T | 92 | 2.2% | 98.9% |  | n/a | no target |
| P01_GOLD | 597 | 53.4% | 80.9% |  | 95% | ❌ 42 pts to go |
| P02 | 399 | 64.2% | 90.2% |  | n/a | no target |
| P03 | 223 | 57.0% | 82.1% |  | n/a | no target |
| P04 | 1575 | 50.3% | 90.5% |  | n/a | no target |
| P05 | 379 | 4.5% | 86.5% |  | n/a | no target |
| P06M | 168 | 0.0% | 100.0% |  | n/a | no target |
| P06T | 2440 | 0.0% | 99.8% |  | n/a | no target |
| P06 | 165 | 0.0% | 100.0% |  | n/a | no target |
| P07 | 252 | 0.0% | 100.0% |  | n/a | no target |
| P08 | 3038 | 0.0% | 100.0% |  | n/a | no target |
| P09 | 374 | 69.0% | 70.3% |  | n/a | no target |
| P10 | 2597 | 0.0% | 100.0% |  | n/a | no target |
| P11 | 475 | 12.4% | 89.7% |  | n/a | no target |
| P12 | 21 | 0.0% | 100.0% |  | n/a | no target |
| P13 | 50796 | 0.0% | 100.0% |  | n/a | no target |

## 7. mail security

### `mta_sts`

> ceiling: DNS-only check; 'no record' counts as checked

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 18 | 100.0% | 100.0% |  | 100% | ✅ met |
| P01T | 92 | 100.0% | 100.0% |  | 100% | ✅ met |
| P01_GOLD | 597 | 100.0% | 100.0% |  | 100% | ✅ met |
| P02 | 399 | 100.0% | 100.0% |  | 100% | ✅ met |
| P03 | 223 | 100.0% | 100.0% |  | 100% | ✅ met |
| P04 | 1575 | 100.0% | 100.0% |  | 100% | ✅ met |
| P05 | 379 | 100.0% | 100.0% |  | 100% | ✅ met |
| P06M | 168 | 100.0% | 100.0% |  | 100% | ✅ met |
| P06T | 2440 | 100.0% | 100.0% |  | 100% | ✅ met |
| P06 | 165 | 100.0% | 100.0% |  | 100% | ✅ met |
| P07 | 252 | 100.0% | 100.0% |  | 100% | ✅ met |
| P08 | 3038 | 100.0% | 100.0% |  | 100% | ✅ met |
| P09 | 374 | 100.0% | 100.0% |  | 100% | ✅ met |
| P10 | 2597 | 100.0% | 100.0% |  | 100% | ✅ met |
| P11 | 475 | 100.0% | 100.0% |  | 100% | ✅ met |
| P12 | 21 | 100.0% | 100.0% |  | 100% | ✅ met |
| P13 | 50796 | 100.0% | 100.0% |  | 100% | ✅ met |

### `tls_rpt`

> ceiling: DNS-only check; 'no record' counts as checked

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 18 | 100.0% | 100.0% |  | 100% | ✅ met |
| P01T | 92 | 100.0% | 100.0% |  | 100% | ✅ met |
| P01_GOLD | 597 | 100.0% | 100.0% |  | 100% | ✅ met |
| P02 | 399 | 100.0% | 100.0% |  | 100% | ✅ met |
| P03 | 223 | 100.0% | 100.0% |  | 100% | ✅ met |
| P04 | 1575 | 100.0% | 100.0% |  | 100% | ✅ met |
| P05 | 379 | 100.0% | 100.0% |  | 100% | ✅ met |
| P06M | 168 | 100.0% | 100.0% |  | 100% | ✅ met |
| P06T | 2440 | 100.0% | 100.0% |  | 100% | ✅ met |
| P06 | 165 | 100.0% | 100.0% |  | 100% | ✅ met |
| P07 | 252 | 100.0% | 100.0% |  | 100% | ✅ met |
| P08 | 3038 | 100.0% | 100.0% |  | 100% | ✅ met |
| P09 | 374 | 100.0% | 100.0% |  | 100% | ✅ met |
| P10 | 2597 | 100.0% | 100.0% |  | 100% | ✅ met |
| P11 | 475 | 100.0% | 100.0% |  | 100% | ✅ met |
| P12 | 21 | 100.0% | 100.0% |  | 100% | ✅ met |
| P13 | 50796 | 100.0% | 100.0% |  | 100% | ✅ met |

### `bimi`

> ceiling: DNS-only check; 'no record' counts as checked

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 18 | 100.0% | 100.0% |  | 100% | ✅ met |
| P01T | 92 | 100.0% | 100.0% |  | 100% | ✅ met |
| P01_GOLD | 597 | 100.0% | 100.0% |  | 100% | ✅ met |
| P02 | 399 | 100.0% | 100.0% |  | 100% | ✅ met |
| P03 | 223 | 100.0% | 100.0% |  | 100% | ✅ met |
| P04 | 1575 | 100.0% | 100.0% |  | 100% | ✅ met |
| P05 | 379 | 100.0% | 100.0% |  | 100% | ✅ met |
| P06M | 168 | 100.0% | 100.0% |  | 100% | ✅ met |
| P06T | 2440 | 100.0% | 100.0% |  | 100% | ✅ met |
| P06 | 165 | 100.0% | 100.0% |  | 100% | ✅ met |
| P07 | 252 | 100.0% | 100.0% |  | 100% | ✅ met |
| P08 | 3038 | 100.0% | 100.0% |  | 100% | ✅ met |
| P09 | 374 | 100.0% | 100.0% |  | 100% | ✅ met |
| P10 | 2597 | 100.0% | 100.0% |  | 100% | ✅ met |
| P11 | 475 | 100.0% | 100.0% |  | 100% | ✅ met |
| P12 | 21 | 100.0% | 100.0% |  | 100% | ✅ met |
| P13 | 50796 | 100.0% | 100.0% |  | 100% | ✅ met |

