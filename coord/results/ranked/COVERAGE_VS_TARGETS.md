# Coverage vs the downstream team's targets — 2026-11-08

Benchmarks (field × package with a numeric target): **87 of 438 met** (19.9%); 41 within 10 points; 310 further away.
A cell is filled unless blank / `not_published` / `not_found_yet`. Δ = change since the previous build in `coord/results/coverage_history.csv`.
Rows per package: P01M 20, P01T 91, P01_GOLD 585, P02 366, P03 224, P04 1615, P05 378, P06M 167, P06T 2429, P06 160, P07 246, P08 3038, P09 369, P10 2587, P11 497, P12 21, P13 50786

## Where the work is (largest gaps in rows still needed)

| field | package | now | target | rows needed |
|---|---|---|---|---|
| buyer_legal_name_as_published | P13 | 26.4% | 60% | 17087 |
| buyer_logo_url | P13 | 73.4% | 95% | 10951 |
| buyer_address | P13 | 74.3% | 95% | 10526 |
| buyer_ap_cycle_published | P13 | 0.0% | 20% | 10157 |
| ap_system_hint | P13 | 0.3% | 20% | 9999 |
| buyer_phone | P13 | 76.2% | 95% | 9561 |
| buyer_esignature_preference | P13 | 0.1% | 15% | 7591 |
| buyer_tax_exempt_status | P13 | 0.1% | 15% | 7566 |
| buyer_payment_method_preference | P13 | 0.7% | 15% | 7275 |
| buyer_bn_as_published | P13 | 17.6% | 30% | 6309 |
| vendor_registered_address | P10 | 16.0% | 70% | 1398 |
| buyer_legal_name_as_published | P10 | 18.1% | 70% | 1344 |
| vendor_registered_address | P08 | 28.6% | 70% | 1257 |
| buyer_address | P08 | 64.5% | 95% | 929 |
| buyer_bn_as_published | P08 | 6.5% | 35% | 868 |
| vendor_emails | P08 | 47.0% | 75% | 851 |
| vendor_phone | P08 | 57.9% | 85% | 824 |
| buyer_address | P10 | 63.7% | 95% | 811 |
| invoice_reference_hint | P08 | 0.0% | 25% | 759 |
| vendor_emails | P10 | 50.8% | 80% | 756 |
| vendor_logo_url | P04 | 42.7% | 85% | 684 |
| vendor_bn9 | P08 | 27.5% | 50% | 683 |
| buyer_phone | P10 | 69.5% | 95% | 660 |
| buyer_bn_as_published | P10 | 5.0% | 30% | 647 |
| solicitation_or_tender_number | P04 | 10.0% | 50% | 646 |
| po_required_as_published | P04 | 0.4% | 40% | 639 |
| invoice_reference_hint | P10 | 0.4% | 25% | 637 |
| payment_terms_as_published | P04 | 0.6% | 40% | 636 |
| vendor_phone | P10 | 60.6% | 85% | 632 |
| buyer_phone | P08 | 74.4% | 95% | 628 |
| vendor_emails | P04 | 32.4% | 70% | 607 |
| buyer_ap_cycle_published | P08 | 0.1% | 20% | 605 |
| contract_description | P04 | 58.0% | 95% | 599 |
| end_date | P04 | 53.1% | 90% | 596 |
| currency | P04 | 58.5% | 95% | 590 |
| ap_system_hint | P08 | 0.8% | 20% | 583 |
| ap_phone | P04 | 49.2% | 85% | 578 |
| buyer_vendor_id | P04 | 4.3% | 40% | 576 |
| vendor_neq | P04 | 59.7% | 95% | 571 |
| invoicing_requirements | P04 | 35.4% | 70% | 560 |

## 1. identifiers

### `invoice_reference_hint`

| package | rows | now | Δ | target | status |
|---|---|---|---|---|---|
| P01M | 20 | 0.0% |  | 50% | ❌ 50 pts to go |
| P01T | 91 | 6.6% |  | 50% | ❌ 43 pts to go |
| P01_GOLD | 585 | 85.5% |  | 95% | 🟡 10 pts to go |
| P02 | 366 | 79.0% |  | 95% | ❌ 16 pts to go |
| P03 | 224 | 87.5% |  | 95% | 🟡 8 pts to go |
| P04 | 1615 | 69.2% |  | 90% | ❌ 21 pts to go |
| P05 | 378 | 36.2% |  | 70% | ❌ 34 pts to go |
| P06M | 167 | 0.0% |  | n/a | no target |
| P06T | 2429 | 0.5% |  | n/a | no target |
| P06 | 160 | 0.6% |  | 30% | ❌ 29 pts to go |
| P07 | 246 | 0.0% |  | 30% | ❌ 30 pts to go |
| P08 | 3038 | 0.0% |  | 25% | ❌ 25 pts to go |
| P09 | 369 | 99.2% |  | 100% | 🟡 1 pts to go |
| P10 | 2587 | 0.4% |  | 25% | ❌ 25 pts to go |
| P11 | 497 | 28.4% |  | 60% | ❌ 32 pts to go |
| P12 | 21 | 100.0% |  | 100% | ✅ met |
| P13 | 50786 | 0.0% |  | 0% by design | — leave (by design) |

### `po_number_as_published`

> ceiling: a purchase-order number exists only where the buyer publishes PO-level data (Montréal, Laval, Toronto open data so far) or the record itself carries one; most sources publish awards, not POs — the target cannot be reached from public data for most buyers

| package | rows | now | Δ | target | status |
|---|---|---|---|---|---|
| P01M | 20 | 0.0% |  | n/a | no target |
| P01T | 91 | 0.0% |  | 10% | 🟡 10 pts to go |
| P01_GOLD | 585 | 6.5% |  | 50% | ❌ 44 pts to go |
| P02 | 366 | 8.2% |  | 50% | ❌ 42 pts to go |
| P03 | 224 | 1.3% |  | 40% | ❌ 39 pts to go |
| P04 | 1615 | 1.1% |  | 30% | ❌ 29 pts to go |
| P05 | 378 | 0.3% |  | 20% | ❌ 20 pts to go |
| P06M | 167 | 0.0% |  | n/a | no target |
| P06T | 2429 | 0.0% |  | n/a | no target |
| P06 | 160 | 0.6% |  | n/a | no target |
| P07 | 246 | 0.0% |  | n/a | no target |
| P08 | 3038 | 0.0% |  | n/a | no target |
| P09 | 369 | 0.5% |  | 50% | ❌ 50 pts to go |
| P10 | 2587 | 0.0% |  | n/a | no target |
| P11 | 497 | 1.4% |  | n/a | no target |
| P12 | 21 | 0.0% |  | n/a | no target |
| P13 | 50786 | 0.0% |  | n/a | no target |

### `contract_or_agreement_number`

| package | rows | now | Δ | target | status |
|---|---|---|---|---|---|
| P01M | 20 | 0.0% |  | n/a | no target |
| P01T | 91 | 4.4% |  | 50% | ❌ 46 pts to go |
| P01_GOLD | 585 | 45.8% |  | 85% | ❌ 39 pts to go |
| P02 | 366 | 63.4% |  | 90% | ❌ 27 pts to go |
| P03 | 224 | 46.0% |  | 85% | ❌ 39 pts to go |
| P04 | 1615 | 61.3% |  | 85% | ❌ 24 pts to go |
| P05 | 378 | 22.0% |  | 60% | ❌ 38 pts to go |
| P06M | 167 | 0.0% |  | n/a | no target |
| P06T | 2429 | 0.0% |  | n/a | no target |
| P06 | 160 | 0.0% |  | n/a | no target |
| P07 | 246 | 0.0% |  | n/a | no target |
| P08 | 3038 | 0.0% |  | n/a | no target |
| P09 | 369 | 87.0% |  | 100% | ❌ 13 pts to go |
| P10 | 2587 | 0.0% |  | n/a | no target |
| P11 | 497 | 18.7% |  | 60% | ❌ 41 pts to go |
| P12 | 21 | 0.0% |  | n/a | no target |
| P13 | 50786 | 0.0% |  | n/a | no target |

### `solicitation_or_tender_number`

| package | rows | now | Δ | target | status |
|---|---|---|---|---|---|
| P01M | 20 | 0.0% |  | n/a | no target |
| P01T | 91 | 2.2% |  | 30% | ❌ 28 pts to go |
| P01_GOLD | 585 | 38.3% |  | 80% | ❌ 42 pts to go |
| P02 | 366 | 23.2% |  | 60% | ❌ 37 pts to go |
| P03 | 224 | 42.0% |  | 80% | ❌ 38 pts to go |
| P04 | 1615 | 10.0% |  | 50% | ❌ 40 pts to go |
| P05 | 378 | 12.4% |  | 40% | ❌ 28 pts to go |
| P06M | 167 | 0.0% |  | n/a | no target |
| P06T | 2429 | 0.2% |  | n/a | no target |
| P06 | 160 | 0.0% |  | n/a | no target |
| P07 | 246 | 0.0% |  | n/a | no target |
| P08 | 3038 | 0.0% |  | n/a | no target |
| P09 | 369 | 11.1% |  | 50% | ❌ 39 pts to go |
| P10 | 2587 | 0.0% |  | n/a | no target |
| P11 | 497 | 11.7% |  | 40% | ❌ 28 pts to go |
| P12 | 21 | 100.0% |  | 100% | ✅ met |
| P13 | 50786 | 0.0% |  | n/a | no target |

### `award_or_notice_id`

| package | rows | now | Δ | target | status |
|---|---|---|---|---|---|
| P01M | 20 | 0.0% |  | n/a | no target |
| P01T | 91 | 3.3% |  | n/a | no target |
| P01_GOLD | 585 | 44.3% |  | 85% | ❌ 41 pts to go |
| P02 | 366 | 54.6% |  | 90% | ❌ 35 pts to go |
| P03 | 224 | 50.9% |  | 85% | ❌ 34 pts to go |
| P04 | 1615 | 52.6% |  | 85% | ❌ 32 pts to go |
| P05 | 378 | 14.8% |  | 50% | ❌ 35 pts to go |
| P06M | 167 | 0.0% |  | n/a | no target |
| P06T | 2429 | 0.1% |  | n/a | no target |
| P06 | 160 | 0.0% |  | n/a | no target |
| P07 | 246 | 0.0% |  | n/a | no target |
| P08 | 3038 | 0.0% |  | n/a | no target |
| P09 | 369 | 90.8% |  | 100% | 🟡 9 pts to go |
| P10 | 2587 | 0.0% |  | n/a | no target |
| P11 | 497 | 18.5% |  | 60% | ❌ 42 pts to go |
| P12 | 21 | 0.0% |  | n/a | no target |
| P13 | 50786 | 0.0% |  | n/a | no target |

### `buyer_vendor_id`

| package | rows | now | Δ | target | status |
|---|---|---|---|---|---|
| P01M | 20 | 0.0% |  | n/a | no target |
| P01T | 91 | 2.2% |  | n/a | no target |
| P01_GOLD | 585 | 13.7% |  | 60% | ❌ 46 pts to go |
| P02 | 366 | 7.4% |  | 50% | ❌ 43 pts to go |
| P03 | 224 | 10.3% |  | 50% | ❌ 40 pts to go |
| P04 | 1615 | 4.3% |  | 40% | ❌ 36 pts to go |
| P05 | 378 | 1.3% |  | 20% | ❌ 19 pts to go |
| P06M | 167 | 0.0% |  | n/a | no target |
| P06T | 2429 | 0.1% |  | n/a | no target |
| P06 | 160 | 0.0% |  | n/a | no target |
| P07 | 246 | 0.0% |  | n/a | no target |
| P08 | 3038 | 0.0% |  | n/a | no target |
| P09 | 369 | 2.4% |  | 50% | ❌ 48 pts to go |
| P10 | 2587 | 0.0% |  | n/a | no target |
| P11 | 497 | 4.8% |  | n/a | no target |
| P12 | 21 | 0.0% |  | n/a | no target |
| P13 | 50786 | 0.0% |  | n/a | no target |

### `commodity_codes`

| package | rows | now | Δ | target | status |
|---|---|---|---|---|---|
| P01M | 20 | 0.0% |  | n/a | no target |
| P01T | 91 | 0.0% |  | n/a | no target |
| P01_GOLD | 585 | 36.2% |  | 80% | ❌ 44 pts to go |
| P02 | 366 | 60.1% |  | 90% | ❌ 30 pts to go |
| P03 | 224 | 37.1% |  | 80% | ❌ 43 pts to go |
| P04 | 1615 | 51.2% |  | 85% | ❌ 34 pts to go |
| P05 | 378 | 5.3% |  | 50% | ❌ 45 pts to go |
| P06M | 167 | 0.0% |  | n/a | no target |
| P06T | 2429 | 0.0% |  | n/a | no target |
| P06 | 160 | 0.0% |  | n/a | no target |
| P07 | 246 | 0.0% |  | n/a | no target |
| P08 | 3038 | 0.0% |  | n/a | no target |
| P09 | 369 | 76.2% |  | 95% | ❌ 19 pts to go |
| P10 | 2587 | 0.0% |  | n/a | no target |
| P11 | 497 | 15.9% |  | 50% | ❌ 34 pts to go |
| P12 | 21 | 0.0% |  | n/a | no target |
| P13 | 50786 | 0.0% |  | n/a | no target |

### `buyer_org_codes`

| package | rows | now | Δ | target | status |
|---|---|---|---|---|---|
| P01M | 20 | 0.0% |  | n/a | no target |
| P01T | 91 | 1.1% |  | n/a | no target |
| P01_GOLD | 585 | 8.7% |  | 50% | ❌ 41 pts to go |
| P02 | 366 | 8.2% |  | 50% | ❌ 42 pts to go |
| P03 | 224 | 2.2% |  | 30% | ❌ 28 pts to go |
| P04 | 1615 | 1.1% |  | 30% | ❌ 29 pts to go |
| P05 | 378 | 0.0% |  | n/a | no target |
| P06M | 167 | 0.0% |  | n/a | no target |
| P06T | 2429 | 0.0% |  | n/a | no target |
| P06 | 160 | 0.0% |  | n/a | no target |
| P07 | 246 | 0.0% |  | n/a | no target |
| P08 | 3038 | 0.0% |  | n/a | no target |
| P09 | 369 | 0.3% |  | n/a | no target |
| P10 | 2587 | 0.0% |  | n/a | no target |
| P11 | 497 | 1.4% |  | n/a | no target |
| P12 | 21 | 0.0% |  | n/a | no target |
| P13 | 50786 | 0.0% |  | n/a | no target |

### `records_with_this_vendor`

| package | rows | now | Δ | target | status |
|---|---|---|---|---|---|
| P01M | 20 | 100.0% |  | n/a | no target |
| P01T | 91 | 100.0% |  | 60% | ✅ met |
| P01_GOLD | 585 | 100.0% |  | 100% | ✅ met |
| P02 | 366 | 100.0% |  | 100% | ✅ met |
| P03 | 224 | 100.0% |  | 100% | ✅ met |
| P04 | 1615 | 100.0% |  | 95% | ✅ met |
| P05 | 378 | 100.0% |  | 70% | ✅ met |
| P06M | 167 | 100.0% |  | n/a | no target |
| P06T | 2429 | 100.0% |  | n/a | no target |
| P06 | 160 | 100.0% |  | 50% | ✅ met |
| P07 | 246 | 100.0% |  | n/a | no target |
| P08 | 3038 | 100.0% |  | n/a | no target |
| P09 | 369 | 100.0% |  | 100% | ✅ met |
| P10 | 2587 | 100.0% |  | n/a | no target |
| P11 | 497 | 100.0% |  | 70% | ✅ met |
| P12 | 21 | 100.0% |  | n/a | no target |
| P13 | 50786 | 0.0% |  | n/a | no target |

## 2. vendor

### `vendor_bn9`

| package | rows | now | Δ | target | status |
|---|---|---|---|---|---|
| P01M | 20 | 85.0% |  | 70% | ✅ met |
| P01T | 91 | 80.2% |  | 60% | ✅ met |
| P01_GOLD | 585 | 79.0% |  | 90% | ❌ 11 pts to go |
| P02 | 366 | 68.3% |  | 85% | ❌ 17 pts to go |
| P03 | 224 | 81.7% |  | 90% | 🟡 8 pts to go |
| P04 | 1615 | 56.9% |  | 75% | ❌ 18 pts to go |
| P05 | 378 | 53.7% |  | 50% | ✅ met |
| P06M | 167 | 70.1% |  | n/a | no target |
| P06T | 2429 | 60.4% |  | n/a | no target |
| P06 | 160 | 47.5% |  | 40% | ✅ met |
| P07 | 246 | 27.6% |  | 50% | ❌ 22 pts to go |
| P08 | 3038 | 27.5% |  | 50% | ❌ 22 pts to go |
| P09 | 369 | 52.6% |  | 80% | ❌ 27 pts to go |
| P10 | 2587 | 23.4% |  | 40% | ❌ 17 pts to go |
| P11 | 497 | 35.6% |  | 60% | ❌ 24 pts to go |
| P12 | 21 | 47.6% |  | 85% | ❌ 37 pts to go |
| P13 | 50786 | 91.7% |  | 0% by design | — leave (by design) |

### `vendor_registered_address`

| package | rows | now | Δ | target | status |
|---|---|---|---|---|---|
| P01M | 20 | 35.0% |  | n/a | no target |
| P01T | 91 | 62.6% |  | n/a | no target |
| P01_GOLD | 585 | 75.4% |  | 95% | ❌ 20 pts to go |
| P02 | 366 | 83.6% |  | 95% | ❌ 11 pts to go |
| P03 | 224 | 77.7% |  | 95% | ❌ 17 pts to go |
| P04 | 1615 | 81.4% |  | 95% | ❌ 14 pts to go |
| P05 | 378 | 54.0% |  | 70% | ❌ 16 pts to go |
| P06M | 167 | 6.6% |  | n/a | no target |
| P06T | 2429 | 74.7% |  | n/a | no target |
| P06 | 160 | 52.5% |  | 80% | ❌ 28 pts to go |
| P07 | 246 | 32.1% |  | 70% | ❌ 38 pts to go |
| P08 | 3038 | 28.6% |  | 70% | ❌ 41 pts to go |
| P09 | 369 | 85.1% |  | 100% | ❌ 15 pts to go |
| P10 | 2587 | 16.0% |  | 70% | ❌ 54 pts to go |
| P11 | 497 | 36.4% |  | 75% | ❌ 39 pts to go |
| P12 | 21 | 85.7% |  | n/a | no target |
| P13 | 50786 | 0.0% |  | n/a | no target |

### `vendor_trading_name`

| package | rows | now | Δ | target | status |
|---|---|---|---|---|---|
| P01M | 20 | 35.0% |  | n/a | no target |
| P01T | 91 | 19.8% |  | n/a | no target |
| P01_GOLD | 585 | 52.5% |  | 60% | 🟡 8 pts to go |
| P02 | 366 | 66.1% |  | 60% | ✅ met |
| P03 | 224 | 58.9% |  | 60% | 🟡 1 pts to go |
| P04 | 1615 | 56.5% |  | 55% | ✅ met |
| P05 | 378 | 24.3% |  | 50% | ❌ 26 pts to go |
| P06M | 167 | 13.2% |  | n/a | no target |
| P06T | 2429 | 53.4% |  | n/a | no target |
| P06 | 160 | 40.0% |  | n/a | no target |
| P07 | 246 | 36.6% |  | 55% | ❌ 18 pts to go |
| P08 | 3038 | 34.3% |  | 50% | ❌ 16 pts to go |
| P09 | 369 | 70.7% |  | 70% | ✅ met |
| P10 | 2587 | 37.6% |  | 55% | ❌ 17 pts to go |
| P11 | 497 | 35.6% |  | 50% | ❌ 14 pts to go |
| P12 | 21 | 85.7% |  | n/a | no target |
| P13 | 50786 | 0.0% |  | n/a | no target |

### `vendor_phone`

| package | rows | now | Δ | target | status |
|---|---|---|---|---|---|
| P01M | 20 | 35.0% |  | n/a | no target |
| P01T | 91 | 0.0% |  | n/a | no target |
| P01_GOLD | 585 | 33.0% |  | 70% | ❌ 37 pts to go |
| P02 | 366 | 42.3% |  | 70% | ❌ 28 pts to go |
| P03 | 224 | 38.8% |  | 70% | ❌ 31 pts to go |
| P04 | 1615 | 33.2% |  | 65% | ❌ 32 pts to go |
| P05 | 378 | 16.7% |  | 60% | ❌ 43 pts to go |
| P06M | 167 | 6.6% |  | n/a | no target |
| P06T | 2429 | 0.0% |  | n/a | no target |
| P06 | 160 | 53.8% |  | 40% | ✅ met |
| P07 | 246 | 60.2% |  | 85% | ❌ 25 pts to go |
| P08 | 3038 | 57.9% |  | 85% | ❌ 27 pts to go |
| P09 | 369 | 50.1% |  | 85% | ❌ 35 pts to go |
| P10 | 2587 | 60.6% |  | 85% | ❌ 24 pts to go |
| P11 | 497 | 44.3% |  | 75% | ❌ 31 pts to go |
| P12 | 21 | 4.8% |  | n/a | no target |
| P13 | 50786 | 100.0% |  | 60% | ✅ met |

### `vendor_website`

| package | rows | now | Δ | target | status |
|---|---|---|---|---|---|
| P01M | 20 | 45.0% |  | n/a | no target |
| P01T | 91 | 11.0% |  | n/a | no target |
| P01_GOLD | 585 | 70.1% |  | 90% | ❌ 20 pts to go |
| P02 | 366 | 73.5% |  | 90% | ❌ 16 pts to go |
| P03 | 224 | 67.4% |  | 90% | ❌ 23 pts to go |
| P04 | 1615 | 56.8% |  | 85% | ❌ 28 pts to go |
| P05 | 378 | 27.8% |  | 70% | ❌ 42 pts to go |
| P06M | 167 | 10.2% |  | n/a | no target |
| P06T | 2429 | 2.6% |  | n/a | no target |
| P06 | 160 | 97.5% |  | 50% | ✅ met |
| P07 | 246 | 94.3% |  | 100% | 🟡 6 pts to go |
| P08 | 3038 | 92.7% |  | 100% | 🟡 7 pts to go |
| P09 | 369 | 78.6% |  | 100% | ❌ 21 pts to go |
| P10 | 2587 | 100.0% |  | 100% | ✅ met |
| P11 | 497 | 84.1% |  | 100% | ❌ 16 pts to go |
| P12 | 21 | 23.8% |  | n/a | no target |
| P13 | 50786 | 100.0% |  | n/a | no target |

### `vendor_emails`

| package | rows | now | Δ | target | status |
|---|---|---|---|---|---|
| P01M | 20 | 35.0% |  | n/a | no target |
| P01T | 91 | 0.0% |  | n/a | no target |
| P01_GOLD | 585 | 36.6% |  | 70% | ❌ 33 pts to go |
| P02 | 366 | 45.4% |  | 75% | ❌ 30 pts to go |
| P03 | 224 | 42.0% |  | 75% | ❌ 33 pts to go |
| P04 | 1615 | 32.4% |  | 70% | ❌ 38 pts to go |
| P05 | 378 | 14.0% |  | 55% | ❌ 41 pts to go |
| P06M | 167 | 6.6% |  | n/a | no target |
| P06T | 2429 | 0.0% |  | n/a | no target |
| P06 | 160 | 40.6% |  | n/a | no target |
| P07 | 246 | 36.2% |  | 70% | ❌ 34 pts to go |
| P08 | 3038 | 47.0% |  | 75% | ❌ 28 pts to go |
| P09 | 369 | 52.8% |  | 85% | ❌ 32 pts to go |
| P10 | 2587 | 50.8% |  | 80% | ❌ 29 pts to go |
| P11 | 497 | 36.4% |  | 70% | ❌ 34 pts to go |
| P12 | 21 | 19.0% |  | n/a | no target |
| P13 | 50786 | 0.0% |  | n/a | no target |

### `vendor_logo_url`

> ceiling: needs the vendor's website first; sites that block automated readers (robots.txt / 403) are never read

| package | rows | now | Δ | target | status |
|---|---|---|---|---|---|
| P01M | 20 | 35.0% |  | n/a | no target |
| P01T | 91 | 0.0% |  | n/a | no target |
| P01_GOLD | 585 | 48.7% |  | 90% | ❌ 41 pts to go |
| P02 | 366 | 58.2% |  | 90% | ❌ 32 pts to go |
| P03 | 224 | 54.9% |  | 90% | ❌ 35 pts to go |
| P04 | 1615 | 42.7% |  | 85% | ❌ 42 pts to go |
| P05 | 378 | 22.8% |  | 75% | ❌ 52 pts to go |
| P06M | 167 | 6.6% |  | n/a | no target |
| P06T | 2429 | 0.0% |  | n/a | no target |
| P06 | 160 | 85.6% |  | n/a | no target |
| P07 | 246 | 84.6% |  | 100% | ❌ 15 pts to go |
| P08 | 3038 | 82.8% |  | 100% | ❌ 17 pts to go |
| P09 | 369 | 57.7% |  | n/a | no target |
| P10 | 2587 | 84.1% |  | 100% | ❌ 16 pts to go |
| P11 | 497 | 62.0% |  | n/a | no target |
| P12 | 21 | 14.3% |  | n/a | no target |
| P13 | 50786 | 0.0% |  | n/a | no target |

### `vendor_neq`

> ceiling: only Québec-registered vendors have an NEQ; the share of QC vendors is reported next to the rate

| package | rows | now | Δ | target | status |
|---|---|---|---|---|---|
| P01M | 20 | 0.0% |  | n/a | no target |
| P01T | 91 | 19.8% |  | n/a | no target · QC vendors: 1 rows, 0.0% filled |
| P01_GOLD | 585 | 46.5% |  | 95% | ❌ 48 pts to go · QC vendors: 46 rows, 87.0% filled |
| P02 | 366 | 66.9% |  | 95% | ❌ 28 pts to go · QC vendors: 91 rows, 100.0% filled |
| P03 | 224 | 54.0% |  | 95% | ❌ 41 pts to go · QC vendors: 16 rows, 87.5% filled |
| P04 | 1615 | 59.7% |  | 95% | ❌ 35 pts to go · QC vendors: 447 rows, 97.1% filled |
| P05 | 378 | 11.1% |  | n/a | no target · QC vendors: 20 rows, 80.0% filled |
| P06M | 167 | 0.0% |  | n/a | no target |
| P06T | 2429 | 53.4% |  | n/a | no target · QC vendors: 4 rows, 0.0% filled |
| P06 | 160 | 21.9% |  | n/a | no target · QC vendors: 14 rows, 92.9% filled |
| P07 | 246 | 17.1% |  | n/a | no target · QC vendors: 21 rows, 100.0% filled |
| P08 | 3038 | 23.4% |  | n/a | no target · QC vendors: 437 rows, 100.0% filled |
| P09 | 369 | 81.8% |  | 95% | ❌ 13 pts to go · QC vendors: 153 rows, 100.0% filled |
| P10 | 2587 | 15.5% |  | n/a | no target · QC vendors: 218 rows, 100.0% filled |
| P11 | 497 | 26.2% |  | n/a | no target · QC vendors: 64 rows, 96.9% filled |
| P12 | 21 | 71.4% |  | n/a | no target · QC vendors: 3 rows, 100.0% filled |
| P13 | 50786 | 0.0% |  | n/a | no target |

### `vendor_years_in_business`

| package | rows | now | Δ | target | status |
|---|---|---|---|---|---|
| P01M | 20 | 0.0% |  | n/a | no target |
| P01T | 91 | 46.2% |  | n/a | no target · vendors with a registry record: 42 rows, 100.0% filled |
| P01_GOLD | 585 | 85.0% |  | 100% | ❌ 15 pts to go · vendors with a registry record: 497 rows, 100.0% filled |
| P02 | 366 | 90.7% |  | 100% | 🟡 9 pts to go · vendors with a registry record: 332 rows, 100.0% filled |
| P03 | 224 | 87.9% |  | 100% | ❌ 12 pts to go · vendors with a registry record: 197 rows, 100.0% filled |
| P04 | 1615 | 83.9% |  | 100% | ❌ 16 pts to go · vendors with a registry record: 1355 rows, 100.0% filled |
| P05 | 378 | 59.0% |  | n/a | no target · vendors with a registry record: 223 rows, 100.0% filled |
| P06M | 167 | 0.0% |  | n/a | no target |
| P06T | 2429 | 73.4% |  | n/a | no target · vendors with a registry record: 1784 rows, 100.0% filled |
| P06 | 160 | 53.8% |  | n/a | no target · vendors with a registry record: 86 rows, 100.0% filled |
| P07 | 246 | 32.5% |  | n/a | no target · vendors with a registry record: 80 rows, 100.0% filled |
| P08 | 3038 | 29.4% |  | n/a | no target · vendors with a registry record: 894 rows, 100.0% filled |
| P09 | 369 | 88.3% |  | n/a | no target · vendors with a registry record: 326 rows, 100.0% filled |
| P10 | 2587 | 16.5% |  | n/a | no target · vendors with a registry record: 426 rows, 100.0% filled |
| P11 | 497 | 40.0% |  | n/a | no target · vendors with a registry record: 199 rows, 100.0% filled |
| P12 | 21 | 71.4% |  | n/a | no target · vendors with a registry record: 15 rows, 100.0% filled |
| P13 | 50786 | 0.0% |  | n/a | no target |

## 3. buyer

### `buyer_legal_name_as_published`

| package | rows | now | Δ | target | status |
|---|---|---|---|---|---|
| P01M | 20 | 95.0% |  | 90% | ✅ met |
| P01T | 91 | 96.7% |  | 90% | ✅ met |
| P01_GOLD | 585 | 87.5% |  | 95% | 🟡 8 pts to go |
| P02 | 366 | 93.7% |  | 95% | 🟡 1 pts to go |
| P03 | 224 | 84.8% |  | 85% | 🟡 0 pts to go |
| P04 | 1615 | 77.4% |  | 90% | ❌ 13 pts to go |
| P05 | 378 | 74.3% |  | 75% | 🟡 1 pts to go |
| P06M | 167 | 83.2% |  | n/a | no target |
| P06T | 2429 | 70.3% |  | n/a | no target |
| P06 | 160 | 73.8% |  | 80% | 🟡 6 pts to go |
| P07 | 246 | 75.2% |  | 80% | 🟡 5 pts to go |
| P08 | 3038 | 58.3% |  | 75% | ❌ 17 pts to go |
| P09 | 369 | 75.9% |  | 95% | ❌ 19 pts to go |
| P10 | 2587 | 18.1% |  | 70% | ❌ 52 pts to go |
| P11 | 497 | 28.6% |  | 65% | ❌ 36 pts to go |
| P12 | 21 | 57.1% |  | 80% | ❌ 23 pts to go |
| P13 | 50786 | 26.4% |  | 60% | ❌ 34 pts to go |

### `buyer_bn_as_published`

> ceiling: a buyer's BN is public only where the buyer prints it or a public dataset carries it (CRA charities, federal grants & contributions recipients, business registries for corporations); municipalities rarely publish theirs

| package | rows | now | Δ | target | status |
|---|---|---|---|---|---|
| P01M | 20 | 40.0% |  | 50% | 🟡 10 pts to go |
| P01T | 91 | 18.7% |  | n/a | no target |
| P01_GOLD | 585 | 18.8% |  | 40% | ❌ 21 pts to go |
| P02 | 366 | 19.1% |  | 40% | ❌ 21 pts to go |
| P03 | 224 | 23.2% |  | 40% | ❌ 17 pts to go |
| P04 | 1615 | 22.8% |  | 40% | ❌ 17 pts to go |
| P05 | 378 | 13.2% |  | 25% | ❌ 12 pts to go |
| P06M | 167 | 13.2% |  | n/a | no target |
| P06T | 2429 | 11.1% |  | n/a | no target |
| P06 | 160 | 7.5% |  | 35% | ❌ 28 pts to go |
| P07 | 246 | 6.5% |  | 35% | ❌ 28 pts to go |
| P08 | 3038 | 6.5% |  | 35% | ❌ 28 pts to go |
| P09 | 369 | 17.6% |  | n/a | no target |
| P10 | 2587 | 5.0% |  | 30% | ❌ 25 pts to go |
| P11 | 497 | 9.1% |  | n/a | no target |
| P12 | 21 | 23.8% |  | n/a | no target |
| P13 | 50786 | 17.6% |  | 30% | ❌ 12 pts to go |

### `buyer_address`

| package | rows | now | Δ | target | status |
|---|---|---|---|---|---|
| P01M | 20 | 95.0% |  | 100% | 🟡 5 pts to go |
| P01T | 91 | 93.4% |  | 100% | 🟡 7 pts to go |
| P01_GOLD | 585 | 89.1% |  | 100% | ❌ 11 pts to go |
| P02 | 366 | 95.4% |  | 100% | 🟡 5 pts to go |
| P03 | 224 | 94.2% |  | 100% | 🟡 6 pts to go |
| P04 | 1615 | 90.8% |  | 100% | 🟡 9 pts to go |
| P05 | 378 | 79.9% |  | 100% | ❌ 20 pts to go |
| P06M | 167 | 69.5% |  | n/a | no target |
| P06T | 2429 | 77.8% |  | n/a | no target |
| P06 | 160 | 62.5% |  | 95% | ❌ 32 pts to go |
| P07 | 246 | 64.6% |  | 95% | ❌ 30 pts to go |
| P08 | 3038 | 64.5% |  | 95% | ❌ 30 pts to go |
| P09 | 369 | 97.6% |  | 100% | 🟡 2 pts to go |
| P10 | 2587 | 63.7% |  | 95% | ❌ 31 pts to go |
| P11 | 497 | 37.8% |  | 80% | ❌ 42 pts to go |
| P12 | 21 | 100.0% |  | 100% | ✅ met |
| P13 | 50786 | 74.3% |  | 95% | ❌ 21 pts to go |

### `buyer_phone`

| package | rows | now | Δ | target | status |
|---|---|---|---|---|---|
| P01M | 20 | 90.0% |  | n/a | no target |
| P01T | 91 | 80.2% |  | n/a | no target |
| P01_GOLD | 585 | 69.9% |  | 90% | ❌ 20 pts to go |
| P02 | 366 | 78.1% |  | 95% | ❌ 17 pts to go |
| P03 | 224 | 74.1% |  | 95% | ❌ 21 pts to go |
| P04 | 1615 | 85.4% |  | 95% | 🟡 10 pts to go |
| P05 | 378 | 74.6% |  | 90% | ❌ 15 pts to go |
| P06M | 167 | 83.8% |  | n/a | no target |
| P06T | 2429 | 77.2% |  | n/a | no target |
| P06 | 160 | 65.0% |  | 95% | ❌ 30 pts to go |
| P07 | 246 | 65.0% |  | 90% | ❌ 25 pts to go |
| P08 | 3038 | 74.4% |  | 95% | ❌ 21 pts to go |
| P09 | 369 | 89.7% |  | 100% | ❌ 10 pts to go |
| P10 | 2587 | 69.5% |  | 95% | ❌ 26 pts to go |
| P11 | 497 | 27.4% |  | 75% | ❌ 48 pts to go |
| P12 | 21 | 81.0% |  | n/a | no target |
| P13 | 50786 | 76.2% |  | 95% | ❌ 19 pts to go |

### `buyer_logo_url`

> ceiling: sites that block automated readers (robots.txt / 403) are never read; an og:image that looks like a photo is labelled

| package | rows | now | Δ | target | status |
|---|---|---|---|---|---|
| P01M | 20 | 80.0% |  | n/a | no target |
| P01T | 91 | 91.2% |  | 95% | 🟡 4 pts to go |
| P01_GOLD | 585 | 68.9% |  | 90% | ❌ 21 pts to go |
| P02 | 366 | 77.6% |  | 95% | ❌ 17 pts to go |
| P03 | 224 | 70.1% |  | 95% | ❌ 25 pts to go |
| P04 | 1615 | 63.3% |  | 90% | ❌ 27 pts to go |
| P05 | 378 | 78.6% |  | 95% | ❌ 16 pts to go |
| P06M | 167 | 84.4% |  | n/a | no target |
| P06T | 2429 | 93.8% |  | n/a | no target |
| P06 | 160 | 89.4% |  | 100% | ❌ 11 pts to go |
| P07 | 246 | 87.0% |  | 100% | ❌ 13 pts to go |
| P08 | 3038 | 89.8% |  | 100% | ❌ 10 pts to go |
| P09 | 369 | 53.1% |  | n/a | no target |
| P10 | 2587 | 84.7% |  | 100% | ❌ 15 pts to go |
| P11 | 497 | 30.0% |  | 80% | ❌ 50 pts to go |
| P12 | 21 | 52.4% |  | n/a | no target |
| P13 | 50786 | 73.4% |  | 95% | ❌ 22 pts to go |

## 4. AP

### `ap_contact_name_as_published`

> ceiling: role titles only (Supervisor, Accounts Payable) — the owner's rule 'never a named person' overrides the 25 % target; a person's name is never collected

| package | rows | now | Δ | target | status |
|---|---|---|---|---|---|
| P01M | 20 | 5.0% |  | n/a | no target |
| P01T | 91 | 1.1% |  | n/a | no target |
| P01_GOLD | 585 | 1.9% |  | 25% | ❌ 23 pts to go |
| P02 | 366 | 11.2% |  | 40% | ❌ 29 pts to go |
| P03 | 224 | 0.0% |  | 20% | ❌ 20 pts to go |
| P04 | 1615 | 0.8% |  | 20% | ❌ 19 pts to go |
| P05 | 378 | 0.3% |  | 15% | ❌ 15 pts to go |
| P06M | 167 | 0.0% |  | n/a | no target |
| P06T | 2429 | 0.0% |  | n/a | no target |
| P06 | 160 | 0.6% |  | n/a | no target |
| P07 | 246 | 2.8% |  | n/a | no target |
| P08 | 3038 | 0.0% |  | n/a | no target |
| P09 | 369 | 3.8% |  | n/a | no target |
| P10 | 2587 | 0.2% |  | n/a | no target |
| P11 | 497 | 0.4% |  | n/a | no target |
| P12 | 21 | 0.0% |  | n/a | no target |
| P13 | 50786 | 0.1% |  | n/a | no target |

### `ap_phone`

| package | rows | now | Δ | target | status |
|---|---|---|---|---|---|
| P01M | 20 | 35.0% |  | n/a | no target |
| P01T | 91 | 36.3% |  | 70% | ❌ 34 pts to go |
| P01_GOLD | 585 | 42.4% |  | 80% | ❌ 38 pts to go |
| P02 | 366 | 66.4% |  | 90% | ❌ 24 pts to go |
| P03 | 224 | 20.1% |  | 60% | ❌ 40 pts to go |
| P04 | 1615 | 49.2% |  | 85% | ❌ 36 pts to go |
| P05 | 378 | 12.2% |  | 50% | ❌ 38 pts to go |
| P06M | 167 | 5.4% |  | n/a | no target |
| P06T | 2429 | 2.1% |  | n/a | no target |
| P06 | 160 | 18.1% |  | n/a | no target |
| P07 | 246 | 19.1% |  | n/a | no target |
| P08 | 3038 | 0.5% |  | n/a | no target |
| P09 | 369 | 81.6% |  | 95% | ❌ 13 pts to go |
| P10 | 2587 | 3.1% |  | n/a | no target |
| P11 | 497 | 33.2% |  | n/a | no target |
| P12 | 21 | 33.3% |  | n/a | no target |
| P13 | 50786 | 0.9% |  | n/a | no target |

### `invoice_mailing_address`

| package | rows | now | Δ | target | status |
|---|---|---|---|---|---|
| P01M | 20 | 5.0% |  | n/a | no target |
| P01T | 91 | 17.6% |  | n/a | no target |
| P01_GOLD | 585 | 31.6% |  | 70% | ❌ 38 pts to go |
| P02 | 366 | 39.9% |  | 75% | ❌ 35 pts to go |
| P03 | 224 | 20.1% |  | 55% | ❌ 35 pts to go |
| P04 | 1615 | 48.5% |  | 75% | ❌ 26 pts to go |
| P05 | 378 | 10.6% |  | 50% | ❌ 39 pts to go |
| P06M | 167 | 1.8% |  | n/a | no target |
| P06T | 2429 | 0.9% |  | n/a | no target |
| P06 | 160 | 10.0% |  | n/a | no target |
| P07 | 246 | 10.2% |  | n/a | no target |
| P08 | 3038 | 0.5% |  | n/a | no target |
| P09 | 369 | 77.5% |  | 95% | ❌ 18 pts to go |
| P10 | 2587 | 1.7% |  | n/a | no target |
| P11 | 497 | 32.8% |  | n/a | no target |
| P12 | 21 | 19.0% |  | n/a | no target |
| P13 | 50786 | 0.6% |  | n/a | no target |

### `invoicing_requirements`

| package | rows | now | Δ | target | status |
|---|---|---|---|---|---|
| P01M | 20 | 15.0% |  | n/a | no target |
| P01T | 91 | 5.5% |  | n/a | no target |
| P01_GOLD | 585 | 46.8% |  | 80% | ❌ 33 pts to go |
| P02 | 366 | 41.5% |  | 75% | ❌ 34 pts to go |
| P03 | 224 | 25.4% |  | 70% | ❌ 45 pts to go |
| P04 | 1615 | 35.4% |  | 70% | ❌ 35 pts to go |
| P05 | 378 | 10.8% |  | 50% | ❌ 39 pts to go |
| P06M | 167 | 0.6% |  | n/a | no target |
| P06T | 2429 | 0.6% |  | n/a | no target |
| P06 | 160 | 14.4% |  | n/a | no target |
| P07 | 246 | 1.6% |  | n/a | no target |
| P08 | 3038 | 0.4% |  | n/a | no target |
| P09 | 369 | 41.2% |  | 80% | ❌ 39 pts to go |
| P10 | 2587 | 1.0% |  | n/a | no target |
| P11 | 497 | 16.9% |  | n/a | no target |
| P12 | 21 | 33.3% |  | n/a | no target |
| P13 | 50786 | 0.3% |  | n/a | no target |

### `payment_terms_as_published`

| package | rows | now | Δ | target | status |
|---|---|---|---|---|---|
| P01M | 20 | 20.0% |  | n/a | no target |
| P01T | 91 | 16.5% |  | 60% | ❌ 44 pts to go |
| P01_GOLD | 585 | 18.8% |  | 70% | ❌ 51 pts to go |
| P02 | 366 | 2.7% |  | 50% | ❌ 47 pts to go |
| P03 | 224 | 5.8% |  | 55% | ❌ 49 pts to go |
| P04 | 1615 | 0.6% |  | 40% | ❌ 39 pts to go |
| P05 | 378 | 2.9% |  | 40% | ❌ 37 pts to go |
| P06M | 167 | 0.6% |  | n/a | no target |
| P06T | 2429 | 0.5% |  | n/a | no target |
| P06 | 160 | 13.1% |  | n/a | no target |
| P07 | 246 | 3.3% |  | n/a | no target |
| P08 | 3038 | 0.5% |  | n/a | no target |
| P09 | 369 | 2.4% |  | n/a | no target |
| P10 | 2587 | 0.5% |  | n/a | no target |
| P11 | 497 | 0.4% |  | n/a | no target |
| P12 | 21 | 9.5% |  | n/a | no target |
| P13 | 50786 | 0.2% |  | n/a | no target |

### `po_required_as_published`

| package | rows | now | Δ | target | status |
|---|---|---|---|---|---|
| P01M | 20 | 20.0% |  | n/a | no target |
| P01T | 91 | 28.6% |  | 65% | ❌ 36 pts to go |
| P01_GOLD | 585 | 30.1% |  | 70% | ❌ 40 pts to go |
| P02 | 366 | 0.5% |  | 50% | ❌ 50 pts to go |
| P03 | 224 | 11.6% |  | 60% | ❌ 48 pts to go |
| P04 | 1615 | 0.4% |  | 40% | ❌ 40 pts to go |
| P05 | 378 | 7.7% |  | 45% | ❌ 37 pts to go |
| P06M | 167 | 1.2% |  | n/a | no target |
| P06T | 2429 | 0.2% |  | n/a | no target |
| P06 | 160 | 31.9% |  | n/a | no target |
| P07 | 246 | 6.5% |  | n/a | no target |
| P08 | 3038 | 0.3% |  | n/a | no target |
| P09 | 369 | 3.3% |  | n/a | no target |
| P10 | 2587 | 0.8% |  | n/a | no target |
| P11 | 497 | 1.6% |  | n/a | no target |
| P12 | 21 | 4.8% |  | n/a | no target |
| P13 | 50786 | 0.1% |  | n/a | no target |

### `invoice_portal_url`

> ceiling: only portals the buyer names on its own pages; informational tax-authority links are not portals

| package | rows | now | Δ | target | status |
|---|---|---|---|---|---|
| P01M | 20 | 10.0% |  | n/a | no target |
| P01T | 91 | 19.8% |  | n/a | no target |
| P01_GOLD | 585 | 15.0% |  | 50% | ❌ 35 pts to go |
| P02 | 366 | 5.5% |  | n/a | no target |
| P03 | 224 | 33.9% |  | 60% | ❌ 26 pts to go |
| P04 | 1615 | 4.6% |  | n/a | no target |
| P05 | 378 | 7.9% |  | n/a | no target |
| P06M | 167 | 2.4% |  | n/a | no target |
| P06T | 2429 | 0.8% |  | n/a | no target |
| P06 | 160 | 15.0% |  | n/a | no target |
| P07 | 246 | 10.2% |  | n/a | no target |
| P08 | 3038 | 0.5% |  | n/a | no target |
| P09 | 369 | 6.2% |  | n/a | no target |
| P10 | 2587 | 1.4% |  | n/a | no target |
| P11 | 497 | 1.6% |  | n/a | no target |
| P12 | 21 | 4.8% |  | n/a | no target |
| P13 | 50786 | 0.4% |  | n/a | no target |

### `buyer_payment_method_preference`

| package | rows | now | Δ | target | status |
|---|---|---|---|---|---|
| P01M | 20 | 15.0% |  | 15% | ✅ met |
| P01T | 91 | 40.7% |  | 15% | ✅ met |
| P01_GOLD | 585 | 37.3% |  | 40% | 🟡 3 pts to go |
| P02 | 366 | 33.3% |  | 25% | ✅ met |
| P03 | 224 | 33.0% |  | 25% | ✅ met |
| P04 | 1615 | 22.7% |  | 15% | ✅ met |
| P05 | 378 | 29.6% |  | 15% | ✅ met |
| P06M | 167 | 37.1% |  | 15% | ✅ met |
| P06T | 2429 | 36.1% |  | 15% | ✅ met |
| P06 | 160 | 38.1% |  | 15% | ✅ met |
| P07 | 246 | 37.4% |  | 15% | ✅ met |
| P08 | 3038 | 31.1% |  | 15% | ✅ met |
| P09 | 369 | 10.8% |  | 15% | 🟡 4 pts to go |
| P10 | 2587 | 3.2% |  | 15% | ❌ 12 pts to go |
| P11 | 497 | 7.0% |  | 15% | 🟡 8 pts to go |
| P12 | 21 | 0.0% |  | 15% | ❌ 15 pts to go |
| P13 | 50786 | 0.7% |  | 15% | ❌ 14 pts to go |

### `buyer_tax_exempt_status`

| package | rows | now | Δ | target | status |
|---|---|---|---|---|---|
| P01M | 20 | 0.0% |  | 15% | ❌ 15 pts to go |
| P01T | 91 | 8.8% |  | 25% | ❌ 16 pts to go |
| P01_GOLD | 585 | 8.2% |  | 25% | ❌ 17 pts to go |
| P02 | 366 | 3.3% |  | 15% | ❌ 12 pts to go |
| P03 | 224 | 2.2% |  | 15% | ❌ 13 pts to go |
| P04 | 1615 | 0.6% |  | 15% | ❌ 14 pts to go |
| P05 | 378 | 4.2% |  | 15% | ❌ 11 pts to go |
| P06M | 167 | 0.6% |  | 15% | ❌ 14 pts to go |
| P06T | 2429 | 0.7% |  | 15% | ❌ 14 pts to go |
| P06 | 160 | 6.2% |  | 15% | 🟡 9 pts to go |
| P07 | 246 | 2.8% |  | 15% | ❌ 12 pts to go |
| P08 | 3038 | 0.7% |  | 15% | ❌ 14 pts to go |
| P09 | 369 | 0.3% |  | 15% | ❌ 15 pts to go |
| P10 | 2587 | 0.2% |  | 15% | ❌ 15 pts to go |
| P11 | 497 | 1.0% |  | 15% | ❌ 14 pts to go |
| P12 | 21 | 9.5% |  | 15% | 🟡 6 pts to go |
| P13 | 50786 | 0.1% |  | 15% | ❌ 15 pts to go |

### `buyer_ap_cycle_published`

| package | rows | now | Δ | target | status |
|---|---|---|---|---|---|
| P01M | 20 | 0.0% |  | 20% | ❌ 20 pts to go |
| P01T | 91 | 3.3% |  | 20% | ❌ 17 pts to go |
| P01_GOLD | 585 | 1.2% |  | 20% | ❌ 19 pts to go |
| P02 | 366 | 0.3% |  | 20% | ❌ 20 pts to go |
| P03 | 224 | 0.0% |  | 20% | ❌ 20 pts to go |
| P04 | 1615 | 0.1% |  | 20% | ❌ 20 pts to go |
| P05 | 378 | 0.5% |  | 20% | ❌ 20 pts to go |
| P06M | 167 | 0.6% |  | 20% | ❌ 19 pts to go |
| P06T | 2429 | 0.0% |  | 20% | ❌ 20 pts to go |
| P06 | 160 | 1.9% |  | 20% | ❌ 18 pts to go |
| P07 | 246 | 0.4% |  | 20% | ❌ 20 pts to go |
| P08 | 3038 | 0.1% |  | 20% | ❌ 20 pts to go |
| P09 | 369 | 0.0% |  | 20% | ❌ 20 pts to go |
| P10 | 2587 | 0.0% |  | 20% | ❌ 20 pts to go |
| P11 | 497 | 0.2% |  | 20% | ❌ 20 pts to go |
| P12 | 21 | 0.0% |  | 20% | ❌ 20 pts to go |
| P13 | 50786 | 0.0% |  | 20% | ❌ 20 pts to go |

### `buyer_esignature_preference`

| package | rows | now | Δ | target | status |
|---|---|---|---|---|---|
| P01M | 20 | 0.0% |  | 15% | ❌ 15 pts to go |
| P01T | 91 | 3.3% |  | 15% | ❌ 12 pts to go |
| P01_GOLD | 585 | 1.9% |  | 15% | ❌ 13 pts to go |
| P02 | 366 | 0.3% |  | 15% | ❌ 15 pts to go |
| P03 | 224 | 1.8% |  | 15% | ❌ 13 pts to go |
| P04 | 1615 | 0.6% |  | 15% | ❌ 14 pts to go |
| P05 | 378 | 0.3% |  | 15% | ❌ 15 pts to go |
| P06M | 167 | 1.8% |  | 15% | ❌ 13 pts to go |
| P06T | 2429 | 1.4% |  | 15% | ❌ 14 pts to go |
| P06 | 160 | 3.1% |  | 15% | ❌ 12 pts to go |
| P07 | 246 | 2.4% |  | 15% | ❌ 13 pts to go |
| P08 | 3038 | 1.5% |  | 15% | ❌ 14 pts to go |
| P09 | 369 | 0.3% |  | 15% | ❌ 15 pts to go |
| P10 | 2587 | 0.2% |  | 15% | ❌ 15 pts to go |
| P11 | 497 | 0.2% |  | 15% | ❌ 15 pts to go |
| P12 | 21 | 0.0% |  | 15% | ❌ 15 pts to go |
| P13 | 50786 | 0.1% |  | 15% | ❌ 15 pts to go |

### `ap_system_hint`

| package | rows | now | Δ | target | status |
|---|---|---|---|---|---|
| P01M | 20 | 10.0% |  | 20% | 🟡 10 pts to go |
| P01T | 91 | 16.5% |  | 40% | ❌ 24 pts to go |
| P01_GOLD | 585 | 11.1% |  | 40% | ❌ 29 pts to go |
| P02 | 366 | 4.9% |  | 20% | ❌ 15 pts to go |
| P03 | 224 | 9.4% |  | 35% | ❌ 26 pts to go |
| P04 | 1615 | 4.3% |  | 20% | ❌ 16 pts to go |
| P05 | 378 | 5.0% |  | 20% | ❌ 15 pts to go |
| P06M | 167 | 2.4% |  | 20% | ❌ 18 pts to go |
| P06T | 2429 | 1.1% |  | 20% | ❌ 19 pts to go |
| P06 | 160 | 16.2% |  | 20% | 🟡 4 pts to go |
| P07 | 246 | 9.8% |  | 20% | ❌ 10 pts to go |
| P08 | 3038 | 0.8% |  | 20% | ❌ 19 pts to go |
| P09 | 369 | 9.5% |  | 20% | ❌ 10 pts to go |
| P10 | 2587 | 1.0% |  | 20% | ❌ 19 pts to go |
| P11 | 497 | 2.0% |  | 20% | ❌ 18 pts to go |
| P12 | 21 | 0.0% |  | 20% | ❌ 20 pts to go |
| P13 | 50786 | 0.3% |  | 20% | ❌ 20 pts to go |

## 5. contract

### `contract_value`

> ceiling: rows proven by a lobbying filing, a news release, an auditor appointment, a customer story or a vendor's client list have no contract value by nature (≈17 % of P01 Gold); bids&tenders awards now carry the awarded bidder's submitted price when no award value was published

| package | rows | now | Δ | target | status |
|---|---|---|---|---|---|
| P01M | 20 | 0.0% |  | n/a | no target |
| P01T | 91 | 1.1% |  | n/a | no target |
| P01_GOLD | 585 | 68.7% |  | 95% | ❌ 26 pts to go |
| P02 | 366 | 74.3% |  | 95% | ❌ 21 pts to go |
| P03 | 224 | 64.3% |  | 90% | ❌ 26 pts to go |
| P04 | 1615 | 57.0% |  | 85% | ❌ 28 pts to go |
| P05 | 378 | 34.4% |  | 75% | ❌ 41 pts to go |
| P06M | 167 | 0.0% |  | n/a | no target |
| P06T | 2429 | 0.0% |  | n/a | no target |
| P06 | 160 | 0.0% |  | n/a | no target |
| P07 | 246 | 0.0% |  | n/a | no target |
| P08 | 3038 | 0.0% |  | n/a | no target |
| P09 | 369 | 90.8% |  | 100% | 🟡 9 pts to go |
| P10 | 2587 | 0.0% |  | n/a | no target |
| P11 | 497 | 21.9% |  | 60% | ❌ 38 pts to go |
| P12 | 21 | 100.0% |  | n/a | no target |
| P13 | 50786 | 0.0% |  | n/a | no target |

### `currency`

| package | rows | now | Δ | target | status |
|---|---|---|---|---|---|
| P01M | 20 | 0.0% |  | n/a | no target |
| P01T | 91 | 0.0% |  | n/a | no target |
| P01_GOLD | 585 | 72.5% |  | 100% | ❌ 28 pts to go |
| P02 | 366 | 77.9% |  | 100% | ❌ 22 pts to go |
| P03 | 224 | 71.4% |  | n/a | no target |
| P04 | 1615 | 58.5% |  | 95% | ❌ 36 pts to go |
| P05 | 378 | 30.7% |  | 80% | ❌ 49 pts to go |
| P06M | 167 | 0.0% |  | n/a | no target |
| P06T | 2429 | 0.0% |  | n/a | no target |
| P06 | 160 | 0.0% |  | n/a | no target |
| P07 | 246 | 0.0% |  | n/a | no target |
| P08 | 3038 | 0.0% |  | n/a | no target |
| P09 | 369 | 93.5% |  | 100% | 🟡 6 pts to go |
| P10 | 2587 | 0.0% |  | n/a | no target |
| P11 | 497 | 23.3% |  | n/a | no target |
| P12 | 21 | 100.0% |  | n/a | no target |
| P13 | 50786 | 0.0% |  | n/a | no target |

### `start_date`

> ceiling: most award notices publish an award date, not a start date; start_date carries the signature date when the source gives one, labelled

| package | rows | now | Δ | target | status |
|---|---|---|---|---|---|
| P01M | 20 | 0.0% |  | n/a | no target |
| P01T | 91 | 1.1% |  | n/a | no target |
| P01_GOLD | 585 | 52.3% |  | 85% | ❌ 33 pts to go |
| P02 | 366 | 65.8% |  | 90% | ❌ 24 pts to go |
| P03 | 224 | 52.2% |  | 85% | ❌ 33 pts to go |
| P04 | 1615 | 63.5% |  | 90% | ❌ 26 pts to go |
| P05 | 378 | 35.4% |  | 75% | ❌ 40 pts to go |
| P06M | 167 | 0.0% |  | n/a | no target |
| P06T | 2429 | 0.0% |  | n/a | no target |
| P06 | 160 | 0.0% |  | n/a | no target |
| P07 | 246 | 0.0% |  | n/a | no target |
| P08 | 3038 | 0.0% |  | n/a | no target |
| P09 | 369 | 85.4% |  | 95% | 🟡 10 pts to go |
| P10 | 2587 | 0.0% |  | n/a | no target |
| P11 | 497 | 21.1% |  | n/a | no target |
| P12 | 21 | 0.0% |  | n/a | no target |
| P13 | 50786 | 0.0% |  | n/a | no target |

### `end_date`

> ceiling: an inferred end (award date + published duration) is labelled as such; sources without a duration leave end_date empty — the honest ceiling

| package | rows | now | Δ | target | status |
|---|---|---|---|---|---|
| P01M | 20 | 0.0% |  | n/a | no target |
| P01T | 91 | 1.1% |  | n/a | no target |
| P01_GOLD | 585 | 52.8% |  | 85% | ❌ 32 pts to go |
| P02 | 366 | 61.2% |  | 90% | ❌ 29 pts to go |
| P03 | 224 | 52.7% |  | 85% | ❌ 32 pts to go |
| P04 | 1615 | 53.1% |  | 90% | ❌ 37 pts to go |
| P05 | 378 | 42.3% |  | 75% | ❌ 33 pts to go |
| P06M | 167 | 0.0% |  | n/a | no target |
| P06T | 2429 | 0.0% |  | n/a | no target |
| P06 | 160 | 0.0% |  | n/a | no target |
| P07 | 246 | 0.0% |  | n/a | no target |
| P08 | 3038 | 0.0% |  | n/a | no target |
| P09 | 369 | 0.3% |  | 95% | ❌ 95 pts to go |
| P10 | 2587 | 0.0% |  | n/a | no target |
| P11 | 497 | 17.3% |  | n/a | no target |
| P12 | 21 | 0.0% |  | n/a | no target |
| P13 | 50786 | 0.0% |  | n/a | no target |

### `contract_title`

| package | rows | now | Δ | target | status |
|---|---|---|---|---|---|
| P01M | 20 | 0.0% |  | n/a | no target |
| P01T | 91 | 76.9% |  | n/a | no target |
| P01_GOLD | 585 | 81.9% |  | 100% | ❌ 18 pts to go |
| P02 | 366 | 80.9% |  | 100% | ❌ 19 pts to go |
| P03 | 224 | 86.2% |  | n/a | no target |
| P04 | 1615 | 71.6% |  | 95% | ❌ 23 pts to go |
| P05 | 378 | 75.4% |  | 95% | ❌ 20 pts to go |
| P06M | 167 | 0.6% |  | n/a | no target |
| P06T | 2429 | 83.3% |  | n/a | no target |
| P06 | 160 | 75.6% |  | n/a | no target |
| P07 | 246 | 76.8% |  | n/a | no target |
| P08 | 3038 | 85.0% |  | n/a | no target |
| P09 | 369 | 98.9% |  | 100% | 🟡 1 pts to go |
| P10 | 2587 | 98.4% |  | n/a | no target |
| P11 | 497 | 89.5% |  | n/a | no target |
| P12 | 21 | 100.0% |  | n/a | no target |
| P13 | 50786 | 0.0% |  | n/a | no target |

### `contract_description`

| package | rows | now | Δ | target | status |
|---|---|---|---|---|---|
| P01M | 20 | 0.0% |  | n/a | no target |
| P01T | 91 | 3.3% |  | n/a | no target |
| P01_GOLD | 585 | 69.2% |  | 100% | ❌ 31 pts to go |
| P02 | 366 | 72.4% |  | 100% | ❌ 28 pts to go |
| P03 | 224 | 68.3% |  | n/a | no target |
| P04 | 1615 | 58.0% |  | 95% | ❌ 37 pts to go |
| P05 | 378 | 14.0% |  | 70% | ❌ 56 pts to go |
| P06M | 167 | 0.0% |  | n/a | no target |
| P06T | 2429 | 0.2% |  | n/a | no target |
| P06 | 160 | 0.0% |  | n/a | no target |
| P07 | 246 | 0.0% |  | n/a | no target |
| P08 | 3038 | 0.0% |  | n/a | no target |
| P09 | 369 | 95.7% |  | 100% | 🟡 4 pts to go |
| P10 | 2587 | 0.0% |  | n/a | no target |
| P11 | 497 | 24.1% |  | n/a | no target |
| P12 | 21 | 100.0% |  | n/a | no target |
| P13 | 50786 | 0.0% |  | n/a | no target |

### `number_of_bids`

> ceiling: published by some portals only (bids&tenders submission lists, Biddingo bidder lists); federal proactive disclosure does not publish bid counts

| package | rows | now | Δ | target | status |
|---|---|---|---|---|---|
| P01M | 20 | 0.0% |  | n/a | no target |
| P01T | 91 | 1.1% |  | n/a | no target · rows from a source that publishes bids: 3 rows, 33.3% filled |
| P01_GOLD | 585 | 19.0% |  | 60% | ❌ 41 pts to go · rows from a source that publishes bids: 356 rows, 31.2% filled |
| P02 | 366 | 14.8% |  | n/a | no target · rows from a source that publishes bids: 268 rows, 20.1% filled |
| P03 | 224 | 16.5% |  | n/a | no target · rows from a source that publishes bids: 141 rows, 26.2% filled |
| P04 | 1615 | 3.5% |  | n/a | no target · rows from a source that publishes bids: 900 rows, 6.3% filled |
| P05 | 378 | 3.4% |  | n/a | no target · rows from a source that publishes bids: 48 rows, 27.1% filled |
| P06M | 167 | 0.0% |  | n/a | no target |
| P06T | 2429 | 0.1% |  | n/a | no target · rows from a source that publishes bids: 4 rows, 50.0% filled |
| P06 | 160 | 0.0% |  | n/a | no target |
| P07 | 246 | 0.0% |  | n/a | no target |
| P08 | 3038 | 0.0% |  | n/a | no target |
| P09 | 369 | 3.3% |  | n/a | no target · rows from a source that publishes bids: 355 rows, 3.4% filled |
| P10 | 2587 | 0.0% |  | n/a | no target |
| P11 | 497 | 3.0% |  | n/a | no target · rows from a source that publishes bids: 111 rows, 13.5% filled |
| P12 | 21 | 0.0% |  | n/a | no target · rows from a source that publishes bids: 21 rows, 0.0% filled |
| P13 | 50786 | 0.0% |  | n/a | no target |

## 6. history

### `average_contract_duration_days`

| package | rows | now | Δ | target | status |
|---|---|---|---|---|---|
| P01M | 20 | 100.0% |  | n/a | no target |
| P01T | 91 | 96.7% |  | n/a | no target |
| P01_GOLD | 585 | 67.9% |  | 90% | ❌ 22 pts to go |
| P02 | 366 | 80.3% |  | 90% | 🟡 10 pts to go |
| P03 | 224 | 64.3% |  | 90% | ❌ 26 pts to go |
| P04 | 1615 | 82.9% |  | 90% | 🟡 7 pts to go |
| P05 | 378 | 82.0% |  | 90% | 🟡 8 pts to go |
| P06M | 167 | 100.0% |  | n/a | no target |
| P06T | 2429 | 99.8% |  | n/a | no target |
| P06 | 160 | 100.0% |  | n/a | no target |
| P07 | 246 | 100.0% |  | n/a | no target |
| P08 | 3038 | 100.0% |  | n/a | no target |
| P09 | 369 | 1.4% |  | 90% | ❌ 89 pts to go |
| P10 | 2587 | 100.0% |  | n/a | no target |
| P11 | 497 | 88.3% |  | n/a | no target |
| P12 | 21 | 100.0% |  | n/a | no target |
| P13 | 50786 | 100.0% |  | n/a | no target |

### `commodity_distribution_top3`

| package | rows | now | Δ | target | status |
|---|---|---|---|---|---|
| P01M | 20 | 100.0% |  | n/a | no target |
| P01T | 91 | 96.7% |  | n/a | no target |
| P01_GOLD | 585 | 54.5% |  | 90% | ❌ 36 pts to go |
| P02 | 366 | 83.6% |  | n/a | no target |
| P03 | 224 | 53.1% |  | n/a | no target |
| P04 | 1615 | 89.8% |  | n/a | no target |
| P05 | 378 | 82.3% |  | n/a | no target |
| P06M | 167 | 100.0% |  | n/a | no target |
| P06T | 2429 | 99.8% |  | n/a | no target |
| P06 | 160 | 100.0% |  | n/a | no target |
| P07 | 246 | 100.0% |  | n/a | no target |
| P08 | 3038 | 100.0% |  | n/a | no target |
| P09 | 369 | 47.2% |  | n/a | no target |
| P10 | 2587 | 100.0% |  | n/a | no target |
| P11 | 497 | 87.5% |  | n/a | no target |
| P12 | 21 | 100.0% |  | n/a | no target |
| P13 | 50786 | 100.0% |  | n/a | no target |

### `year_over_year_spend_trend`

| package | rows | now | Δ | target | status |
|---|---|---|---|---|---|
| P01M | 20 | 100.0% |  | n/a | no target |
| P01T | 91 | 98.9% |  | n/a | no target |
| P01_GOLD | 585 | 81.4% |  | 95% | ❌ 14 pts to go |
| P02 | 366 | 91.0% |  | n/a | no target |
| P03 | 224 | 83.0% |  | n/a | no target |
| P04 | 1615 | 90.5% |  | n/a | no target |
| P05 | 378 | 86.8% |  | n/a | no target |
| P06M | 167 | 100.0% |  | n/a | no target |
| P06T | 2429 | 99.8% |  | n/a | no target |
| P06 | 160 | 100.0% |  | n/a | no target |
| P07 | 246 | 100.0% |  | n/a | no target |
| P08 | 3038 | 100.0% |  | n/a | no target |
| P09 | 369 | 70.5% |  | n/a | no target |
| P10 | 2587 | 100.0% |  | n/a | no target |
| P11 | 497 | 87.9% |  | n/a | no target |
| P12 | 21 | 100.0% |  | n/a | no target |
| P13 | 50786 | 100.0% |  | n/a | no target |

## 7. mail security

### `mta_sts`

> ceiling: DNS-only check; 'no record' counts as checked

| package | rows | now | Δ | target | status |
|---|---|---|---|---|---|
| P01M | 20 | 100.0% |  | 100% | ✅ met |
| P01T | 91 | 100.0% |  | 100% | ✅ met |
| P01_GOLD | 585 | 100.0% |  | 100% | ✅ met |
| P02 | 366 | 100.0% |  | 100% | ✅ met |
| P03 | 224 | 100.0% |  | 100% | ✅ met |
| P04 | 1615 | 100.0% |  | 100% | ✅ met |
| P05 | 378 | 100.0% |  | 100% | ✅ met |
| P06M | 167 | 100.0% |  | 100% | ✅ met |
| P06T | 2429 | 100.0% |  | 100% | ✅ met |
| P06 | 160 | 100.0% |  | 100% | ✅ met |
| P07 | 246 | 100.0% |  | 100% | ✅ met |
| P08 | 3038 | 100.0% |  | 100% | ✅ met |
| P09 | 369 | 100.0% |  | 100% | ✅ met |
| P10 | 2587 | 100.0% |  | 100% | ✅ met |
| P11 | 497 | 100.0% |  | 100% | ✅ met |
| P12 | 21 | 100.0% |  | 100% | ✅ met |
| P13 | 50786 | 100.0% |  | 100% | ✅ met |

### `tls_rpt`

> ceiling: DNS-only check; 'no record' counts as checked

| package | rows | now | Δ | target | status |
|---|---|---|---|---|---|
| P01M | 20 | 100.0% |  | 100% | ✅ met |
| P01T | 91 | 100.0% |  | 100% | ✅ met |
| P01_GOLD | 585 | 100.0% |  | 100% | ✅ met |
| P02 | 366 | 100.0% |  | 100% | ✅ met |
| P03 | 224 | 100.0% |  | 100% | ✅ met |
| P04 | 1615 | 100.0% |  | 100% | ✅ met |
| P05 | 378 | 100.0% |  | 100% | ✅ met |
| P06M | 167 | 100.0% |  | 100% | ✅ met |
| P06T | 2429 | 100.0% |  | 100% | ✅ met |
| P06 | 160 | 100.0% |  | 100% | ✅ met |
| P07 | 246 | 100.0% |  | 100% | ✅ met |
| P08 | 3038 | 100.0% |  | 100% | ✅ met |
| P09 | 369 | 100.0% |  | 100% | ✅ met |
| P10 | 2587 | 100.0% |  | 100% | ✅ met |
| P11 | 497 | 100.0% |  | 100% | ✅ met |
| P12 | 21 | 100.0% |  | 100% | ✅ met |
| P13 | 50786 | 100.0% |  | 100% | ✅ met |

### `bimi`

> ceiling: DNS-only check; 'no record' counts as checked

| package | rows | now | Δ | target | status |
|---|---|---|---|---|---|
| P01M | 20 | 100.0% |  | 100% | ✅ met |
| P01T | 91 | 100.0% |  | 100% | ✅ met |
| P01_GOLD | 585 | 100.0% |  | 100% | ✅ met |
| P02 | 366 | 100.0% |  | 100% | ✅ met |
| P03 | 224 | 100.0% |  | 100% | ✅ met |
| P04 | 1615 | 100.0% |  | 100% | ✅ met |
| P05 | 378 | 100.0% |  | 100% | ✅ met |
| P06M | 167 | 100.0% |  | 100% | ✅ met |
| P06T | 2429 | 100.0% |  | 100% | ✅ met |
| P06 | 160 | 100.0% |  | 100% | ✅ met |
| P07 | 246 | 100.0% |  | 100% | ✅ met |
| P08 | 3038 | 100.0% |  | 100% | ✅ met |
| P09 | 369 | 100.0% |  | 100% | ✅ met |
| P10 | 2587 | 100.0% |  | 100% | ✅ met |
| P11 | 497 | 100.0% |  | 100% | ✅ met |
| P12 | 21 | 100.0% |  | 100% | ✅ met |
| P13 | 50786 | 100.0% |  | 100% | ✅ met |

