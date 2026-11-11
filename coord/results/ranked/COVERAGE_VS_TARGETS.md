# Coverage vs the downstream team's targets — 2026-11-11

Benchmarks (field × package with a numeric target): **96 of 446 met** (21.5%); 69 within 10 points; 281 further away.
A cell counts as filled only when it carries a value: blank, `not_published`, `not_found_yet` and label-only cells ("no identifier published …", "no dataset record …", "0 in the contract dataset …") do not count; the DNS checks count when checked. `any` = share of non-blank cells incl. such labels. Δ = change since the previous build in `coord/results/coverage_history.csv`.
Rows per package: P01M 122, P01T 431, P01_GOLD 625, P02 485, P03 264, P04 4104, P05 420, P06M 13022, P06T 86551, P06 296, P07 786, P08 25380, P09 295, P10R 102400, P10 2648, P11 20970, P12 7, P13 17402

## Invoice-grade readiness (the row as an invoice header: bill-to, submit-to, references, terms, tax, vendor identity, follow-up)

| package | rows | all 11 elements | ≥ 9 of 11 | median elements | most-missing element |
|---|---|---|---|---|---|
| P01M | 122 | 0.0% | 19.7% | 8 | vendor GST/HST number (111 rows) |
| P01T | 431 | 0.5% | 21.6% | 7 | payment terms (354 rows) |
| P01_GOLD | 625 | 25.1% | 71.4% | 10 | payment terms (214 rows) |
| P02 | 485 | 7.0% | 52.6% | 9 | PO rule (372 rows) |
| P03 | 264 | 14.8% | 56.8% | 9 | payment terms (130 rows) |
| P04 | 4104 | 1.1% | 15.1% | 6 | PO rule (3896 rows) |
| P05 | 420 | 1.2% | 17.9% | 7 | payment terms (345 rows) |
| P06M | 13022 | 0.0% | 2.3% | 8 | PO rule (12832 rows) |
| P06T | 86551 | 0.0% | 7.1% | 7 | PO rule (86059 rows) |
| P06 | 296 | 0.0% | 8.8% | 6 | reference to quote (PO / contract / vendor id) (296 rows) |
| P07 | 786 | 0.0% | 2.0% | 6 | reference to quote (PO / contract / vendor id) (786 rows) |
| P08 | 25380 | 0.0% | 0.3% | 6 | reference to quote (PO / contract / vendor id) (25380 rows) |
| P09 | 295 | 1.0% | 45.1% | 8 | payment terms (276 rows) |
| P10R | 102400 | 0.0% | 22.4% | 8 | PO rule (102363 rows) |
| P10 | 2648 | 0.0% | 1.1% | 5 | reference to quote (PO / contract / vendor id) (2648 rows) |
| P11 | 20970 | 0.2% | 20.7% | 8 | PO rule (20768 rows) |
| P12 | 7 | 0.0% | 28.6% | 8 | PO rule (7 rows) |
| P13 | 17402 | 0.0% | 0.2% | 7 | reference to quote (PO / contract / vendor id) (17402 rows) |

## AP grade (how stringently the row's accounts-payable data meets what an invoice needs; A = invoicing mailbox referee-confirmed on the buyer's own domain with MX, legal name, address, PO rule and terms all published, no penalties)

| package | rows | A | B | C | D | E | median ap_score |
|---|---|---|---|---|---|---|---|
| P01M | 122 | 8 | 26 | 88 | 0 | 0 | 71 |
| P01T | 431 | 30 | 70 | 331 | 0 | 0 | 66 |
| P01_GOLD | 625 | 229 | 197 | 199 | 0 | 0 | 82 |
| P02 | 485 | 0 | 196 | 289 | 0 | 0 | 66 |
| P03 | 264 | 0 | 0 | 252 | 12 | 0 | 57 |
| P04 | 4104 | 0 | 0 | 3462 | 642 | 0 | 46 |
| P05 | 420 | 16 | 29 | 363 | 12 | 0 | 51 |
| P06M | 13022 | 0 | 9 | 12951 | 62 | 0 | 46 |
| P06T | 86551 | 0 | 44 | 69556 | 16951 | 0 | 38 |
| P06 | 296 | 22 | 55 | 219 | 0 | 0 | 71 |
| P07 | 786 | 0 | 31 | 736 | 19 | 0 | 53 |
| P08 | 25380 | 0 | 0 | 22016 | 3364 | 0 | 43 |
| P09 | 295 | 3 | 12 | 278 | 2 | 0 | 53 |
| P10R | 102400 | 1 | 14 | 72574 | 29811 | 0 | 38 |
| P10 | 2648 | 2 | 14 | 2014 | 618 | 0 | 43 |
| P11 | 20970 | 7 | 16 | 41 | 0 | 20906 | 23 |
| P12 | 7 | 0 | 0 | 7 | 0 | 0 | 54 |
| P13 | 17402 | 0 | 17 | 14372 | 3013 | 0 | 43 |

### AP payability (confirmed channel + bill-to legal name and address + the buyer's reference rule + tax treatment known)

| package | rows | payable today | % | most common gap |
|---|---|---|---|---|
| P01M | 122 | 103 | 84.4% | the buyer's PO / reference rule (8) |
| P01T | 431 | 234 | 54.3% | bill-to legal name and address (161) |
| P01_GOLD | 625 | 472 | 75.5% | bill-to legal name and address (97) |
| P02 | 485 | 313 | 64.5% | the buyer's PO / reference rule (99) |
| P03 | 264 | 0 | 0.0% | a confirmed invoicing / AP or finance channel (264) |
| P04 | 4104 | 0 | 0.0% | a confirmed invoicing / AP or finance channel (4104) |
| P05 | 420 | 47 | 11.2% | a confirmed invoicing / AP or finance channel (334) |
| P06M | 13022 | 123 | 0.9% | a confirmed invoicing / AP or finance channel (12856) |
| P06T | 86551 | 518 | 0.6% | a confirmed invoicing / AP or finance channel (85338) |
| P06 | 296 | 53 | 17.9% | the buyer's PO / reference rule (131) |
| P07 | 786 | 13 | 1.7% | bill-to legal name and address (314) |
| P08 | 25380 | 0 | 0.0% | a confirmed invoicing / AP or finance channel (25380) |
| P09 | 295 | 41 | 13.9% | a confirmed invoicing / AP or finance channel (245) |
| P10R | 102400 | 570 | 0.6% | a confirmed invoicing / AP or finance channel (101209) |
| P10 | 2648 | 5 | 0.2% | a confirmed invoicing / AP or finance channel (2555) |
| P11 | 20970 | 14 | 0.1% | a confirmed invoicing / AP or finance channel (20906) |
| P12 | 7 | 3 | 42.9% | a confirmed invoicing / AP or finance channel (4) |
| P13 | 17402 | 8 | 0.0% | a confirmed invoicing / AP or finance channel (17060) |

### Pay on sight (an invoice generated from the row would clear AP: confirmed invoicing / AP or finance channel, bill-to legal name + address, vendor legal name + GST/HST number + remit-to address, tax treatment and currency known — published or labelled-derived; the buyer's reference rule is reported separately)

| package | rows | pay on sight | % | + reference rule not published | routed (general inbox only) | most common gap |
|---|---|---|---|---|---|---|
| P01M | 122 | 5 | 4.1% | 5 | 0 | the vendor's GST/HST number (BN9) (111) |
| P01T | 431 | 84 | 19.5% | 14 | 0 | the vendor's GST/HST number (BN9) (245) |
| P01_GOLD | 625 | 404 | 64.6% | 11 | 0 | the vendor's GST/HST number (BN9) (148) |
| P02 | 485 | 211 | 43.5% | 26 | 0 | the vendor's GST/HST number (BN9) (211) |
| P03 | 264 | 16 | 6.1% | 0 | 135 | an invoicing / AP or finance mailbox (only a purchasing / general inbo (91) |
| P04 | 4104 | 41 | 1.0% | 7 | 881 | an invoicing / AP or finance mailbox (only a purchasing / general inbo (3116) |
| P05 | 420 | 20 | 4.8% | 7 | 110 | an invoicing / AP or finance mailbox (only a purchasing / general inbo (216) |
| P06M | 13022 | 1 | 0.0% | 10 | 148 | an invoicing / AP or finance mailbox (only a purchasing / general inbo (12665) |
| P06T | 86551 | 193 | 0.2% | 48 | 16521 | an invoicing / AP or finance mailbox (only a purchasing / general inbo (68631) |
| P06 | 296 | 15 | 5.1% | 34 | 0 | the vendor's GST/HST number (BN9) (175) |
| P07 | 786 | 7 | 0.9% | 69 | 27 | the vendor's GST/HST number (BN9) (423) |
| P08 | 25380 | 1 | 0.0% | 9 | 2899 | an invoicing / AP or finance mailbox (only a purchasing / general inbo (22404) |
| P09 | 295 | 38 | 12.9% | 1 | 120 | an invoicing / AP or finance mailbox (only a purchasing / general inbo (116) |
| P10R | 102400 | 898 | 0.9% | 0 | 55529 | an invoicing / AP or finance mailbox (only a purchasing / general inbo (45620) |
| P10 | 2648 | 4 | 0.2% | 20 | 380 | an invoicing / AP or finance mailbox (only a purchasing / general inbo (2144) |
| P11 | 20970 | 66 | 0.3% | 1 | 0 | a confirmed invoicing / AP or finance channel (20831) |
| P12 | 7 | 1 | 14.3% | 0 | 2 | the vendor's GST/HST number (BN9) (2) |
| P13 | 17402 | 9 | 0.1% | 253 | 10339 | an invoicing / AP or finance mailbox (only a purchasing / general inbo (6682) |
| **all** | 276208 | 2014 | 0.7% | 515 | 87091 | |

### What still blocks grade A (rows per missing element; a row counts under every element it lacks)

| package | rows not A | referee confirmation of the mailbox | an invoicing / AP mailbox (not finance / procurement / general) | a mailbox on the buyer's own domain | MX record for the mailbox domain | published bill-to legal name | invoice / billing address | published PO rule | published payment terms | clear the penalty |
|---|---|---|---|---|---|---|---|---|---|---|
| P01M | 114 | 0 | 0 | 0 | 62 | 8 | 0 | 94 | 99 | 1 |
| P01T | 401 | 0 | 0 | 0 | 205 | 145 | 46 | 335 | 356 | 26 |
| P01_GOLD | 396 | 0 | 0 | 0 | 11 | 78 | 31 | 194 | 228 | 57 |
| P02 | 485 | 0 | 485 | 0 | 48 | 61 | 18 | 372 | 299 | 22 |
| P03 | 264 | 0 | 264 | 0 | 15 | 43 | 25 | 126 | 136 | 25 |
| P04 | 4104 | 0 | 4104 | 0 | 1889 | 1538 | 995 | 3896 | 3615 | 138 |
| P05 | 404 | 0 | 354 | 0 | 75 | 87 | 43 | 337 | 347 | 50 |
| P06M | 13022 | 0 | 13022 | 0 | 8388 | 1082 | 113 | 12832 | 12722 | 77 |
| P06T | 86551 | 0 | 86551 | 0 | 70392 | 51780 | 21256 | 86059 | 84325 | 433 |
| P06 | 274 | 0 | 0 | 0 | 120 | 73 | 50 | 199 | 233 | 4 |
| P07 | 786 | 0 | 786 | 0 | 478 | 325 | 125 | 730 | 733 | 13 |
| P08 | 25380 | 0 | 25380 | 0 | 18803 | 11814 | 4964 | 25068 | 24648 | 216 |
| P09 | 292 | 0 | 271 | 0 | 9 | 68 | 2 | 266 | 278 | 44 |
| P10R | 102399 | 0 | 102225 | 0 | 80636 | 63408 | 39876 | 102363 | 102216 | 24 |
| P10 | 2646 | 0 | 2610 | 0 | 1288 | 1317 | 893 | 2576 | 2526 | 115 |
| P11 | 20963 | 20906 | 20841 | 0 | 19433 | 11911 | 1086 | 20768 | 19006 | 38 |
| P12 | 7 | 0 | 6 | 0 | 0 | 2 | 0 | 7 | 7 | 0 |
| P13 | 17402 | 0 | 17300 | 0 | 8708 | 8501 | 3932 | 17366 | 17361 | 19 |

## Where the work is (largest gaps in rows still needed)

| field | package | now | target | rows needed |
|---|---|---|---|---|
| buyer_ap_cycle_published | P10R | 0.0% | 20% | 20451 |
| ap_system_hint | P10R | 0.2% | 20% | 20276 |
| buyer_ap_cycle_published | P06T | 0.0% | 20% | 17285 |
| ap_system_hint | P06T | 0.6% | 20% | 16755 |
| buyer_tax_exempt_status | P10R | 0.0% | 15% | 15332 |
| buyer_esignature_preference | P10R | 0.0% | 15% | 15312 |
| vendor_phone | P11 | 4.0% | 75% | 14879 |
| buyer_payment_method_preference | P10R | 0.7% | 15% | 14694 |
| vendor_registered_address | P08 | 13.3% | 70% | 14380 |
| vendor_emails | P11 | 3.3% | 70% | 13986 |
| buyer_esignature_preference | P06T | 0.2% | 15% | 12803 |
| buyer_tax_exempt_status | P06T | 0.3% | 15% | 12735 |
| contract_value | P11 | 0.4% | 60% | 12497 |
| award_or_notice_id | P11 | 0.4% | 60% | 12496 |
| buyer_payment_method_preference | P06T | 0.6% | 15% | 12482 |
| commodity_codes | P11 | 0.3% | 50% | 10424 |
| buyer_phone | P11 | 25.9% | 75% | 10292 |
| vendor_bn9 | P08 | 15.4% | 50% | 8771 |
| solicitation_or_tender_number | P11 | 0.4% | 40% | 8309 |
| buyer_phone | P08 | 69.0% | 95% | 6604 |
| invoice_reference_hint | P08 | 1.2% | 25% | 6033 |
| buyer_phone | P13 | 63.4% | 95% | 5505 |
| buyer_legal_name_as_published | P08 | 53.5% | 75% | 5469 |
| buyer_bn_as_published | P08 | 13.6% | 35% | 5430 |
| vendor_emails | P08 | 54.4% | 75% | 5233 |
| buyer_ap_cycle_published | P08 | 0.0% | 20% | 5064 |
| vendor_phone | P08 | 66.0% | 85% | 4810 |
| ap_system_hint | P08 | 1.1% | 20% | 4803 |
| buyer_legal_name_as_published | P11 | 43.2% | 65% | 4572 |
| buyer_ap_cycle_published | P11 | 0.0% | 20% | 4186 |
| ap_system_hint | P11 | 0.8% | 20% | 4028 |
| buyer_address | P08 | 80.4% | 95% | 3700 |
| buyer_esignature_preference | P08 | 0.5% | 15% | 3691 |
| buyer_tax_exempt_status | P08 | 0.5% | 15% | 3676 |
| buyer_payment_method_preference | P08 | 0.7% | 15% | 3637 |
| buyer_logo_url | P13 | 74.7% | 95% | 3534 |
| buyer_ap_cycle_published | P13 | 0.0% | 20% | 3479 |
| vendor_trading_name | P08 | 36.5% | 50% | 3419 |
| ap_system_hint | P13 | 0.6% | 20% | 3374 |
| buyer_address | P13 | 77.4% | 95% | 3068 |

## 1. identifiers

### `invoice_reference_hint`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 122 | 91.0% | 91.0% | +2.3 | 50% | ✅ met |
| P01T | 431 | 94.0% | 94.0% | +4.5 | 50% | ✅ met |
| P01_GOLD | 625 | 92.2% | 94.4% | +0.0 | 95% | 🟡 3 pts to go |
| P02 | 485 | 71.1% | 72.6% | -2.7 | 95% | ❌ 24 pts to go |
| P03 | 264 | 81.1% | 84.1% | -0.9 | 95% | ❌ 14 pts to go |
| P04 | 4104 | 27.5% | 28.9% | -5.3 | 90% | ❌ 62 pts to go |
| P05 | 420 | 38.8% | 41.7% | +0.2 | 70% | ❌ 31 pts to go |
| P06M | 13022 | 91.6% | 91.6% | -1.0 | n/a | no target |
| P06T | 86551 | 97.2% | 97.2% | +16.9 | n/a | no target |
| P06 | 296 | 32.8% | 32.8% | +1.1 | 30% | ✅ met |
| P07 | 786 | 7.1% | 7.1% | +0.2 | 30% | ❌ 23 pts to go |
| P08 | 25380 | 1.2% | 1.2% | +0.1 | 25% | ❌ 24 pts to go |
| P09 | 295 | 99.0% | 99.7% | +0.0 | 100% | 🟡 1 pts to go |
| P10R | 102400 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P10 | 2648 | 2.7% | 2.8% | +0.1 | 25% | ❌ 22 pts to go |
| P11 | 20970 | 96.6% | 96.7% | +83.0 | 60% | ✅ met |
| P12 | 7 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P13 | 17402 | 0.2% | 0.2% | +0.0 | 0% by design | — leave (by design) |

### `po_number_as_published`

> ceiling: a purchase-order number exists only where the buyer publishes PO-level data (Montréal, Laval, Toronto open data so far) or the record itself carries one; most sources publish awards, not POs — the target cannot be reached from public data for most buyers

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 122 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P01T | 431 | 0.0% | 0.0% | +0.0 | 10% | 🟡 10 pts to go |
| P01_GOLD | 625 | 6.1% | 6.1% | +0.0 | 50% | ❌ 44 pts to go |
| P02 | 485 | 6.0% | 6.0% | -0.2 | 50% | ❌ 44 pts to go |
| P03 | 264 | 1.5% | 1.5% | -0.1 | 40% | ❌ 38 pts to go |
| P04 | 4104 | 0.4% | 0.4% | -0.1 | 30% | ❌ 30 pts to go |
| P05 | 420 | 0.2% | 0.2% | +0.0 | 20% | ❌ 20 pts to go |
| P06M | 13022 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06T | 86551 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06 | 296 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P07 | 786 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P08 | 25380 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P09 | 295 | 0.7% | 0.7% | +0.0 | 50% | ❌ 49 pts to go |
| P10R | 102400 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P10 | 2648 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P11 | 20970 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P12 | 7 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P13 | 17402 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `contract_or_agreement_number`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 122 | 83.6% | 83.6% | +2.2 | n/a | no target |
| P01T | 431 | 79.8% | 79.8% | +9.3 | 50% | ✅ met |
| P01_GOLD | 625 | 66.9% | 66.9% | +0.0 | 85% | ❌ 18 pts to go |
| P02 | 485 | 62.3% | 62.3% | -2.6 | 90% | ❌ 28 pts to go |
| P03 | 264 | 59.5% | 59.5% | -1.8 | 85% | ❌ 26 pts to go |
| P04 | 4104 | 25.0% | 25.0% | -5.1 | 85% | ❌ 60 pts to go |
| P05 | 420 | 29.0% | 29.0% | +0.0 | 60% | ❌ 31 pts to go |
| P06M | 13022 | 91.3% | 91.3% | -1.1 | n/a | no target |
| P06T | 86551 | 97.1% | 97.1% | +17.1 | n/a | no target |
| P06 | 296 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P07 | 786 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P08 | 25380 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P09 | 295 | 95.9% | 95.9% | -0.1 | 100% | 🟡 4 pts to go |
| P10R | 102400 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P10 | 2648 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P11 | 20970 | 96.4% | 96.4% | +83.7 | 60% | ✅ met |
| P12 | 7 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P13 | 17402 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `solicitation_or_tender_number`

> ceiling: SEAO's 'numero' is the organisation's own reference for the notice (SEAO data dictionary) and is reported here; sources that publish awards under a tender number only (bids&tenders, SaskTenders, BC) also carry it as the contract reference, labelled

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 122 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P01T | 431 | 0.0% | 0.0% | +0.0 | 30% | ❌ 30 pts to go |
| P01_GOLD | 625 | 50.7% | 50.7% | +0.1 | 80% | ❌ 29 pts to go |
| P02 | 485 | 54.6% | 54.6% | -2.4 | 60% | 🟡 5 pts to go |
| P03 | 264 | 50.0% | 50.0% | -1.6 | 80% | ❌ 30 pts to go |
| P04 | 4104 | 20.8% | 20.8% | -4.2 | 50% | ❌ 29 pts to go |
| P05 | 420 | 11.7% | 11.7% | -0.2 | 40% | ❌ 28 pts to go |
| P06M | 13022 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06T | 86551 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06 | 296 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P07 | 786 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P08 | 25380 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P09 | 295 | 83.1% | 83.1% | -0.4 | 50% | ✅ met |
| P10R | 102400 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P10 | 2648 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P11 | 20970 | 0.4% | 0.4% | -0.4 | 40% | ❌ 40 pts to go |
| P12 | 7 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P13 | 17402 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `award_or_notice_id`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 122 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P01T | 431 | 0.2% | 0.2% | -0.1 | n/a | no target |
| P01_GOLD | 625 | 60.5% | 60.5% | +0.1 | 85% | ❌ 24 pts to go |
| P02 | 485 | 54.0% | 54.0% | -2.3 | 90% | ❌ 36 pts to go |
| P03 | 264 | 58.3% | 58.3% | -1.9 | 85% | ❌ 27 pts to go |
| P04 | 4104 | 21.4% | 21.4% | -4.4 | 85% | ❌ 64 pts to go |
| P05 | 420 | 20.0% | 20.0% | +0.1 | 50% | ❌ 30 pts to go |
| P06M | 13022 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06T | 86551 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06 | 296 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P07 | 786 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P08 | 25380 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P09 | 295 | 96.9% | 96.9% | -0.1 | 100% | 🟡 3 pts to go |
| P10R | 102400 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P10 | 2648 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P11 | 20970 | 0.4% | 0.4% | -0.5 | 60% | ❌ 60 pts to go |
| P12 | 7 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P13 | 17402 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `buyer_vendor_id`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 122 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P01T | 431 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P01_GOLD | 625 | 13.0% | 13.0% | +0.1 | 60% | ❌ 47 pts to go |
| P02 | 485 | 5.8% | 5.8% | -0.2 | 50% | ❌ 44 pts to go |
| P03 | 264 | 8.3% | 8.3% | -0.3 | 50% | ❌ 42 pts to go |
| P04 | 4104 | 1.7% | 1.7% | -0.3 | 40% | ❌ 38 pts to go |
| P05 | 420 | 0.7% | 0.7% | -0.2 | 20% | ❌ 19 pts to go |
| P06M | 13022 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06T | 86551 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06 | 296 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P07 | 786 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P08 | 25380 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P09 | 295 | 2.4% | 2.4% | +0.1 | 50% | ❌ 48 pts to go |
| P10R | 102400 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P10 | 2648 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P11 | 20970 | 0.1% | 0.1% | +0.0 | n/a | no target |
| P12 | 7 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P13 | 17402 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `commodity_codes`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 122 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P01T | 431 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P01_GOLD | 625 | 34.9% | 34.9% | +0.1 | 80% | ❌ 45 pts to go |
| P02 | 485 | 49.9% | 49.9% | -2.1 | 90% | ❌ 40 pts to go |
| P03 | 264 | 32.6% | 32.6% | -1.0 | 80% | ❌ 47 pts to go |
| P04 | 4104 | 19.6% | 19.6% | -4.0 | 85% | ❌ 65 pts to go |
| P05 | 420 | 5.5% | 5.5% | +0.1 | 50% | ❌ 44 pts to go |
| P06M | 13022 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06T | 86551 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06 | 296 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P07 | 786 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P08 | 25380 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P09 | 295 | 75.6% | 75.6% | -0.3 | 95% | ❌ 19 pts to go |
| P10R | 102400 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P10 | 2648 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P11 | 20970 | 0.3% | 0.3% | -0.3 | 50% | ❌ 50 pts to go |
| P12 | 7 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P13 | 17402 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `buyer_org_codes`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 122 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P01T | 431 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P01_GOLD | 625 | 8.5% | 8.5% | +0.0 | 50% | ❌ 42 pts to go |
| P02 | 485 | 6.0% | 6.0% | -0.2 | 50% | ❌ 44 pts to go |
| P03 | 264 | 1.9% | 1.9% | -0.1 | 30% | ❌ 28 pts to go |
| P04 | 4104 | 0.4% | 0.4% | -0.1 | 30% | ❌ 30 pts to go |
| P05 | 420 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06M | 13022 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06T | 86551 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06 | 296 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P07 | 786 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P08 | 25380 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P09 | 295 | 0.3% | 0.3% | +0.0 | n/a | no target |
| P10R | 102400 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P10 | 2648 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P11 | 20970 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P12 | 7 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P13 | 17402 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `records_with_this_vendor`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 122 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P01T | 431 | 100.0% | 100.0% | +0.0 | 60% | ✅ met |
| P01_GOLD | 625 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P02 | 485 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P03 | 264 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P04 | 4104 | 100.0% | 100.0% | +0.0 | 95% | ✅ met |
| P05 | 420 | 100.0% | 100.0% | +0.0 | 70% | ✅ met |
| P06M | 13022 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P06T | 86551 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P06 | 296 | 100.0% | 100.0% | +0.0 | 50% | ✅ met |
| P07 | 786 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P08 | 25380 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P09 | 295 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P10R | 102400 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P10 | 2648 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P11 | 20970 | 100.0% | 100.0% | +0.0 | 70% | ✅ met |
| P12 | 7 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P13 | 17402 | 0.0% | 0.0% | +0.0 | n/a | no target |

## 2. vendor

### `vendor_bn9`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 122 | 9.0% | 9.0% | -5.4 | 70% | ❌ 61 pts to go |
| P01T | 431 | 29.2% | 29.2% | -4.5 | 60% | ❌ 31 pts to go |
| P01_GOLD | 625 | 73.9% | 73.9% | +0.9 | 90% | ❌ 16 pts to go |
| P02 | 485 | 53.0% | 53.0% | -2.1 | 85% | ❌ 32 pts to go |
| P03 | 264 | 68.2% | 68.2% | -1.7 | 90% | ❌ 22 pts to go |
| P04 | 4104 | 32.4% | 32.4% | -0.1 | 75% | ❌ 43 pts to go |
| P05 | 420 | 50.5% | 50.5% | +0.6 | 50% | ✅ met |
| P06M | 13022 | 1.6% | 1.6% | -0.2 | n/a | no target |
| P06T | 86551 | 22.7% | 22.7% | +5.4 | n/a | no target |
| P06 | 296 | 25.0% | 25.0% | +2.2 | 40% | ❌ 15 pts to go |
| P07 | 786 | 19.0% | 19.0% | +2.6 | 50% | ❌ 31 pts to go |
| P08 | 25380 | 15.4% | 15.4% | +4.5 | 50% | ❌ 35 pts to go |
| P09 | 295 | 58.3% | 58.3% | +0.5 | 80% | ❌ 22 pts to go |
| P10R | 102400 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P10 | 2648 | 30.9% | 30.9% | +2.2 | 40% | 🟡 9 pts to go |
| P11 | 20970 | 94.7% | 94.7% | +3.6 | 60% | ✅ met |
| P12 | 7 | 42.9% | 42.9% | -19.6 | 85% | ❌ 42 pts to go |
| P13 | 17402 | 90.9% | 90.9% | -0.1 | 0% by design | — leave (by design) |

### `vendor_registered_address`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 122 | 53.3% | 53.3% | -13.7 | n/a | no target |
| P01T | 431 | 38.1% | 38.1% | +0.1 | n/a | no target |
| P01_GOLD | 625 | 72.0% | 72.0% | +1.6 | 95% | ❌ 23 pts to go |
| P02 | 485 | 71.8% | 71.8% | -2.0 | 95% | ❌ 23 pts to go |
| P03 | 264 | 70.5% | 70.5% | -1.4 | 95% | ❌ 24 pts to go |
| P04 | 4104 | 43.5% | 43.5% | -2.1 | 95% | ❌ 52 pts to go |
| P05 | 420 | 53.3% | 53.3% | -0.1 | 70% | ❌ 17 pts to go |
| P06M | 13022 | 43.1% | 43.1% | -11.5 | n/a | no target |
| P06T | 86551 | 30.9% | 30.9% | +0.6 | n/a | no target |
| P06 | 296 | 24.3% | 24.3% | -0.5 | 80% | ❌ 56 pts to go |
| P07 | 786 | 17.8% | 17.8% | -0.2 | 70% | ❌ 52 pts to go |
| P08 | 25380 | 13.3% | 13.3% | -0.8 | 70% | ❌ 57 pts to go |
| P09 | 295 | 87.1% | 87.1% | -0.4 | 100% | ❌ 13 pts to go |
| P10R | 102400 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P10 | 2648 | 32.5% | 32.5% | +0.0 | 70% | ❌ 38 pts to go |
| P11 | 20970 | 95.1% | 95.1% | +2.9 | 75% | ✅ met |
| P12 | 7 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P13 | 17402 | 16.2% | 16.2% | +16.2 | n/a | no target |

### `vendor_trading_name`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 122 | 15.6% | 15.6% | -0.9 | n/a | no target |
| P01T | 431 | 61.3% | 61.3% | +35.4 | n/a | no target |
| P01_GOLD | 625 | 50.1% | 50.1% | +2.2 | 60% | 🟡 10 pts to go |
| P02 | 485 | 55.1% | 55.1% | -0.2 | 60% | 🟡 5 pts to go |
| P03 | 264 | 55.3% | 55.3% | +0.2 | 60% | 🟡 5 pts to go |
| P04 | 4104 | 41.0% | 41.0% | +4.3 | 55% | ❌ 14 pts to go |
| P05 | 420 | 24.5% | 24.5% | +2.3 | 50% | ❌ 26 pts to go |
| P06M | 13022 | 7.0% | 7.0% | +3.4 | n/a | no target |
| P06T | 86551 | 66.2% | 66.2% | +39.2 | n/a | no target |
| P06 | 296 | 47.0% | 47.0% | +11.8 | n/a | no target |
| P07 | 786 | 41.1% | 41.1% | +7.9 | 55% | ❌ 14 pts to go |
| P08 | 25380 | 36.5% | 36.5% | +9.6 | 50% | ❌ 14 pts to go |
| P09 | 295 | 73.2% | 73.2% | +2.2 | 70% | ✅ met |
| P10R | 102400 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P10 | 2648 | 47.7% | 47.7% | +8.2 | 55% | 🟡 7 pts to go |
| P11 | 20970 | 97.0% | 97.0% | +5.0 | 50% | ✅ met |
| P12 | 7 | 100.0% | 100.0% | +12.5 | n/a | no target |
| P13 | 17402 | 74.3% | 74.3% | +74.3 | n/a | no target |

### `vendor_phone`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 122 | 49.2% | 49.2% | +34.8 | n/a | no target |
| P01T | 431 | 77.0% | 77.0% | +20.7 | n/a | no target |
| P01_GOLD | 625 | 49.9% | 49.9% | +2.0 | 70% | ❌ 20 pts to go |
| P02 | 485 | 58.1% | 58.1% | +4.1 | 70% | ❌ 12 pts to go |
| P03 | 264 | 51.1% | 51.1% | +1.5 | 70% | ❌ 19 pts to go |
| P04 | 4104 | 55.0% | 55.0% | +7.9 | 65% | 🟡 10 pts to go |
| P05 | 420 | 27.9% | 27.9% | -2.8 | 60% | ❌ 32 pts to go |
| P06M | 13022 | 37.0% | 37.0% | +33.5 | n/a | no target |
| P06T | 86551 | 70.5% | 70.5% | +6.7 | n/a | no target |
| P06 | 296 | 69.3% | 69.3% | +11.7 | 40% | ✅ met |
| P07 | 786 | 64.9% | 64.9% | +7.9 | 85% | ❌ 20 pts to go |
| P08 | 25380 | 66.0% | 66.0% | +9.1 | 85% | ❌ 19 pts to go |
| P09 | 295 | 60.7% | 60.7% | +7.2 | 85% | ❌ 24 pts to go |
| P10R | 102400 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P10 | 2648 | 64.2% | 64.2% | +3.2 | 85% | ❌ 21 pts to go |
| P11 | 20970 | 4.0% | 4.0% | -2.4 | 75% | ❌ 71 pts to go |
| P12 | 7 | 28.6% | 28.6% | +3.6 | n/a | no target |
| P13 | 17402 | 100.0% | 100.0% | +0.0 | 60% | ✅ met |

### `vendor_website`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 122 | 54.9% | 54.9% | +35.3 | n/a | no target |
| P01T | 431 | 98.4% | 98.4% | +2.0 | n/a | no target |
| P01_GOLD | 625 | 79.5% | 79.5% | -9.8 | 90% | ❌ 10 pts to go |
| P02 | 485 | 83.7% | 83.7% | -5.5 | 90% | 🟡 6 pts to go |
| P03 | 264 | 87.9% | 87.9% | -3.1 | 90% | 🟡 2 pts to go |
| P04 | 4104 | 84.9% | 84.9% | -5.3 | 85% | 🟡 0 pts to go |
| P05 | 420 | 44.0% | 44.0% | -8.2 | 70% | ❌ 26 pts to go |
| P06M | 13022 | 43.2% | 43.2% | +37.0 | n/a | no target |
| P06T | 86551 | 100.0% | 100.0% | +8.0 | n/a | no target |
| P06 | 296 | 99.3% | 99.3% | +1.0 | 50% | ✅ met |
| P07 | 786 | 99.7% | 99.7% | +0.6 | 100% | 🟡 0 pts to go |
| P08 | 25380 | 99.8% | 99.8% | +0.4 | 100% | 🟡 0 pts to go |
| P09 | 295 | 80.3% | 80.3% | +0.1 | 100% | ❌ 20 pts to go |
| P10R | 102400 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P10 | 2648 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P11 | 20970 | 99.8% | 99.8% | +0.1 | 100% | 🟡 0 pts to go |
| P12 | 7 | 28.6% | 28.6% | -8.9 | n/a | no target |
| P13 | 17402 | 100.0% | 100.0% | +0.0 | n/a | no target |

### `vendor_emails`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 122 | 13.9% | 13.9% | -0.5 | n/a | no target |
| P01T | 431 | 54.1% | 54.1% | +5.0 | n/a | no target |
| P01_GOLD | 625 | 43.5% | 43.5% | -1.7 | 70% | ❌ 26 pts to go |
| P02 | 485 | 48.7% | 48.7% | -0.8 | 75% | ❌ 26 pts to go |
| P03 | 264 | 43.2% | 43.2% | -1.3 | 75% | ❌ 32 pts to go |
| P04 | 4104 | 38.8% | 38.8% | +1.4 | 70% | ❌ 31 pts to go |
| P05 | 420 | 21.4% | 21.4% | -4.1 | 55% | ❌ 34 pts to go |
| P06M | 13022 | 4.6% | 4.6% | +1.3 | n/a | no target |
| P06T | 86551 | 39.6% | 39.6% | +0.0 | n/a | no target |
| P06 | 296 | 48.0% | 48.0% | +5.2 | n/a | no target |
| P07 | 786 | 50.3% | 50.3% | +4.4 | 70% | ❌ 20 pts to go |
| P08 | 25380 | 54.4% | 54.4% | +4.5 | 75% | ❌ 21 pts to go |
| P09 | 295 | 50.2% | 50.2% | +0.4 | 85% | ❌ 35 pts to go |
| P10R | 102400 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P10 | 2648 | 45.5% | 45.5% | +2.0 | 80% | ❌ 34 pts to go |
| P11 | 20970 | 3.3% | 3.3% | -1.7 | 70% | ❌ 67 pts to go |
| P12 | 7 | 14.3% | 14.3% | -10.7 | n/a | no target |
| P13 | 17402 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `vendor_logo_url`

> ceiling: needs the vendor's website first; sites that block automated readers (robots.txt / 403) are never read

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 122 | 54.9% | 54.9% | +41.5 | n/a | no target |
| P01T | 431 | 96.8% | 96.8% | +7.0 | n/a | no target |
| P01_GOLD | 625 | 73.8% | 73.8% | -3.7 | 90% | ❌ 16 pts to go |
| P02 | 485 | 79.0% | 79.0% | +1.4 | 90% | ❌ 11 pts to go |
| P03 | 264 | 83.3% | 83.3% | +0.1 | 90% | 🟡 7 pts to go |
| P04 | 4104 | 79.2% | 79.2% | +3.6 | 85% | 🟡 6 pts to go |
| P05 | 420 | 42.4% | 42.4% | -6.3 | 75% | ❌ 33 pts to go |
| P06M | 13022 | 42.9% | 42.9% | +38.8 | n/a | no target |
| P06T | 86551 | 97.4% | 97.4% | +14.2 | n/a | no target |
| P06 | 296 | 91.2% | 91.2% | +11.9 | n/a | no target |
| P07 | 786 | 92.0% | 92.0% | +10.4 | 100% | 🟡 8 pts to go |
| P08 | 25380 | 90.9% | 90.9% | +12.0 | 100% | 🟡 9 pts to go |
| P09 | 295 | 66.8% | 66.8% | +5.4 | n/a | no target |
| P10R | 102400 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P10 | 2648 | 88.2% | 88.2% | +4.0 | 100% | ❌ 12 pts to go |
| P11 | 20970 | 95.0% | 95.0% | +6.6 | n/a | no target |
| P12 | 7 | 28.6% | 28.6% | -8.9 | n/a | no target |
| P13 | 17402 | 83.8% | 83.8% | +0.6 | n/a | no target |

### `vendor_neq`

> ceiling: only Québec-registered vendors have an NEQ; the share of QC vendors is reported next to the rate

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 122 | 44.3% | 44.3% | -9.3 | n/a | no target · QC vendors: 45 rows, 100.0% filled |
| P01T | 431 | 21.8% | 21.8% | +4.0 | n/a | no target · QC vendors: 22 rows, 100.0% filled |
| P01_GOLD | 625 | 43.7% | 43.7% | +0.1 | 95% | ❌ 51 pts to go · QC vendors: 53 rows, 98.1% filled |
| P02 | 485 | 53.2% | 53.2% | -1.9 | 95% | ❌ 42 pts to go · QC vendors: 111 rows, 100.0% filled |
| P03 | 264 | 44.7% | 44.7% | -1.8 | 95% | ❌ 50 pts to go · QC vendors: 18 rows, 100.0% filled |
| P04 | 4104 | 27.1% | 27.1% | -4.8 | 95% | ❌ 68 pts to go · QC vendors: 519 rows, 98.8% filled |
| P05 | 420 | 14.0% | 14.0% | -0.8 | n/a | no target · QC vendors: 34 rows, 94.1% filled |
| P06M | 13022 | 42.2% | 42.2% | -11.1 | n/a | no target · QC vendors: 4828 rows, 100.0% filled |
| P06T | 86551 | 20.0% | 20.0% | +2.5 | n/a | no target · QC vendors: 3548 rows, 100.0% filled |
| P06 | 296 | 8.1% | 8.1% | -0.2 | n/a | no target · QC vendors: 17 rows, 76.5% filled |
| P07 | 786 | 5.9% | 5.9% | -0.9 | n/a | no target · QC vendors: 39 rows, 79.5% filled |
| P08 | 25380 | 6.0% | 6.0% | -0.5 | n/a | no target · QC vendors: 1235 rows, 97.9% filled |
| P09 | 295 | 78.0% | 78.0% | -0.2 | 95% | ❌ 17 pts to go · QC vendors: 106 rows, 100.0% filled |
| P10R | 102400 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P10 | 2648 | 17.6% | 17.6% | +0.0 | n/a | no target · QC vendors: 304 rows, 94.7% filled |
| P11 | 20970 | 89.9% | 89.9% | +8.4 | n/a | no target · QC vendors: 115 rows, 98.3% filled |
| P12 | 7 | 71.4% | 71.4% | +8.9 | n/a | no target · QC vendors: 1 rows, 100.0% filled |
| P13 | 17402 | 16.2% | 16.2% | +16.2 | n/a | no target · QC vendors: 2812 rows, 100.0% filled |

### `vendor_years_in_business`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 122 | 52.5% | 52.5% | -12.4 | n/a | no target · vendors with a registry record: 64 rows, 100.0% filled |
| P01T | 431 | 38.1% | 38.1% | -0.2 | n/a | no target · vendors with a registry record: 164 rows, 100.0% filled |
| P01_GOLD | 625 | 81.0% | 81.0% | +1.6 | 100% | ❌ 19 pts to go · vendors with a registry record: 506 rows, 100.0% filled |
| P02 | 485 | 75.5% | 75.5% | -1.9 | 100% | ❌ 24 pts to go · vendors with a registry record: 366 rows, 100.0% filled |
| P03 | 264 | 79.2% | 79.2% | -2.0 | 100% | ❌ 21 pts to go · vendors with a registry record: 209 rows, 100.0% filled |
| P04 | 4104 | 43.8% | 43.8% | -2.3 | 100% | ❌ 56 pts to go · vendors with a registry record: 1799 rows, 100.0% filled |
| P05 | 420 | 58.3% | 58.3% | +0.0 | n/a | no target · vendors with a registry record: 245 rows, 100.0% filled |
| P06M | 13022 | 43.0% | 43.0% | -11.3 | n/a | no target · vendors with a registry record: 5595 rows, 100.0% filled |
| P06T | 86551 | 30.9% | 30.9% | +0.5 | n/a | no target · vendors with a registry record: 26742 rows, 100.0% filled |
| P06 | 296 | 25.3% | 25.3% | -0.2 | n/a | no target · vendors with a registry record: 75 rows, 100.0% filled |
| P07 | 786 | 18.2% | 18.2% | -0.2 | n/a | no target · vendors with a registry record: 143 rows, 100.0% filled |
| P08 | 25380 | 13.5% | 13.5% | -0.8 | n/a | no target · vendors with a registry record: 3438 rows, 100.0% filled |
| P09 | 295 | 90.8% | 90.8% | -0.3 | n/a | no target · vendors with a registry record: 268 rows, 100.0% filled |
| P10R | 102400 | 100.0% | 100.0% | +0.0 | n/a | no target · vendors with a registry record: 102400 rows, 100.0% filled |
| P10 | 2648 | 33.1% | 33.1% | -0.1 | n/a | no target · vendors with a registry record: 877 rows, 100.0% filled |
| P11 | 20970 | 95.2% | 95.2% | +2.9 | n/a | no target · vendors with a registry record: 19957 rows, 100.0% filled |
| P12 | 7 | 100.0% | 100.0% | +0.0 | n/a | no target · vendors with a registry record: 7 rows, 100.0% filled |
| P13 | 17402 | 16.2% | 16.2% | +16.2 | n/a | no target · vendors with a registry record: 2812 rows, 100.0% filled |

## 3. buyer

### `buyer_legal_name_as_published`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 122 | 93.4% | 93.4% | +4.7 | 90% | ✅ met |
| P01T | 431 | 66.4% | 66.4% | +10.1 | 90% | ❌ 24 pts to go |
| P01_GOLD | 625 | 87.5% | 87.5% | +3.8 | 95% | 🟡 8 pts to go |
| P02 | 485 | 87.4% | 87.4% | +2.2 | 95% | 🟡 8 pts to go |
| P03 | 264 | 83.7% | 83.7% | +4.8 | 85% | 🟡 1 pts to go |
| P04 | 4104 | 62.5% | 62.5% | +6.1 | 90% | ❌ 28 pts to go |
| P05 | 420 | 79.3% | 79.3% | +11.6 | 75% | ✅ met |
| P06M | 13022 | 91.7% | 91.7% | +4.6 | n/a | no target |
| P06T | 86551 | 40.2% | 40.2% | +11.2 | n/a | no target |
| P06 | 296 | 75.3% | 75.3% | +18.4 | 80% | 🟡 5 pts to go |
| P07 | 786 | 58.7% | 58.8% | +12.5 | 80% | ❌ 21 pts to go |
| P08 | 25380 | 53.5% | 53.5% | +15.0 | 75% | ❌ 22 pts to go |
| P09 | 295 | 76.9% | 76.9% | -0.3 | 95% | ❌ 18 pts to go |
| P10R | 102400 | 38.1% | 38.1% | +13.1 | n/a | no target |
| P10 | 2648 | 50.3% | 50.3% | +11.3 | 70% | ❌ 20 pts to go |
| P11 | 20970 | 43.2% | 43.2% | +33.6 | 65% | ❌ 22 pts to go |
| P12 | 7 | 71.4% | 71.4% | -3.6 | 80% | 🟡 9 pts to go |
| P13 | 17402 | 51.1% | 51.2% | +11.9 | 60% | 🟡 9 pts to go |

### `buyer_bn_as_published`

> ceiling: a buyer's BN is public only where the buyer prints it or a public dataset carries it (CRA charities, federal grants & contributions recipients, business registries for corporations); municipalities rarely publish theirs

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 122 | 18.9% | 18.9% | -0.7 | 50% | ❌ 31 pts to go |
| P01T | 431 | 12.3% | 12.3% | -1.0 | n/a | no target |
| P01_GOLD | 625 | 19.0% | 19.0% | -1.6 | 40% | ❌ 21 pts to go |
| P02 | 485 | 20.2% | 20.2% | +1.3 | 40% | ❌ 20 pts to go |
| P03 | 264 | 21.2% | 21.2% | -1.1 | 40% | ❌ 19 pts to go |
| P04 | 4104 | 14.8% | 14.8% | -1.5 | 40% | ❌ 25 pts to go |
| P05 | 420 | 15.7% | 15.7% | -4.0 | 25% | 🟡 9 pts to go |
| P06M | 13022 | 9.3% | 9.3% | +0.5 | n/a | no target |
| P06T | 86551 | 7.1% | 7.1% | -0.4 | n/a | no target |
| P06 | 296 | 15.5% | 15.5% | +2.7 | 35% | ❌ 20 pts to go |
| P07 | 786 | 13.5% | 13.5% | +2.0 | 35% | ❌ 22 pts to go |
| P08 | 25380 | 13.6% | 13.6% | +3.2 | 35% | ❌ 21 pts to go |
| P09 | 295 | 16.3% | 16.3% | +0.1 | n/a | no target |
| P10R | 102400 | 8.5% | 8.5% | +1.4 | n/a | no target |
| P10 | 2648 | 10.8% | 10.8% | +4.3 | 30% | ❌ 19 pts to go |
| P11 | 20970 | 1.4% | 1.4% | +0.2 | n/a | no target |
| P12 | 7 | 14.3% | 14.3% | +1.8 | n/a | no target |
| P13 | 17402 | 21.2% | 21.2% | +0.2 | 30% | 🟡 9 pts to go |

### `buyer_address`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 122 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P01T | 431 | 88.6% | 88.6% | -3.3 | 100% | ❌ 11 pts to go |
| P01_GOLD | 625 | 90.7% | 90.7% | +1.2 | 100% | 🟡 9 pts to go |
| P02 | 485 | 95.9% | 95.9% | +0.6 | 100% | 🟡 4 pts to go |
| P03 | 264 | 89.4% | 89.4% | -0.1 | 100% | ❌ 11 pts to go |
| P04 | 4104 | 75.3% | 75.3% | -0.6 | 100% | ❌ 25 pts to go |
| P05 | 420 | 89.0% | 89.0% | +1.6 | 100% | ❌ 11 pts to go |
| P06M | 13022 | 99.1% | 99.1% | +0.3 | n/a | no target |
| P06T | 86551 | 75.4% | 75.4% | -2.0 | n/a | no target |
| P06 | 296 | 81.8% | 81.8% | +0.8 | 95% | ❌ 13 pts to go |
| P07 | 786 | 83.8% | 83.8% | +0.2 | 95% | ❌ 11 pts to go |
| P08 | 25380 | 80.4% | 80.4% | +0.2 | 95% | ❌ 15 pts to go |
| P09 | 295 | 95.9% | 95.9% | +0.2 | 100% | 🟡 4 pts to go |
| P10R | 102400 | 61.1% | 61.1% | +2.3 | n/a | no target |
| P10 | 2648 | 66.1% | 66.2% | +1.0 | 95% | ❌ 29 pts to go |
| P11 | 20970 | 93.7% | 93.7% | +6.5 | 80% | ✅ met |
| P12 | 7 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P13 | 17402 | 77.4% | 77.4% | +2.2 | 95% | ❌ 18 pts to go |

### `buyer_phone`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 122 | 86.9% | 86.9% | +1.3 | n/a | no target |
| P01T | 431 | 71.0% | 71.0% | +7.4 | n/a | no target |
| P01_GOLD | 625 | 72.8% | 72.8% | +3.3 | 90% | ❌ 17 pts to go |
| P02 | 485 | 77.5% | 77.5% | +1.8 | 95% | ❌ 18 pts to go |
| P03 | 264 | 74.2% | 74.2% | +0.4 | 95% | ❌ 21 pts to go |
| P04 | 4104 | 68.9% | 68.9% | +2.3 | 95% | ❌ 26 pts to go |
| P05 | 420 | 73.3% | 73.3% | +2.8 | 90% | ❌ 17 pts to go |
| P06M | 13022 | 87.4% | 87.4% | +1.0 | n/a | no target |
| P06T | 86551 | 56.4% | 56.4% | +8.5 | n/a | no target |
| P06 | 296 | 70.9% | 70.9% | +7.8 | 95% | ❌ 24 pts to go |
| P07 | 786 | 66.2% | 66.2% | +11.2 | 90% | ❌ 24 pts to go |
| P08 | 25380 | 69.0% | 69.0% | +10.2 | 95% | ❌ 26 pts to go |
| P09 | 295 | 86.4% | 86.4% | +0.3 | 100% | ❌ 14 pts to go |
| P10R | 102400 | 59.1% | 59.1% | +14.0 | n/a | no target |
| P10 | 2648 | 60.2% | 60.2% | +3.7 | 95% | ❌ 35 pts to go |
| P11 | 20970 | 25.9% | 25.9% | +14.7 | 75% | ❌ 49 pts to go |
| P12 | 7 | 71.4% | 71.4% | -3.6 | n/a | no target |
| P13 | 17402 | 63.4% | 63.4% | +15.8 | 95% | ❌ 32 pts to go |

### `buyer_logo_url`

> ceiling: sites that block automated readers (robots.txt / 403) are never read; an og:image that looks like a photo is labelled

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 122 | 89.3% | 89.3% | +18.2 | n/a | no target |
| P01T | 431 | 83.3% | 83.3% | +9.2 | 95% | ❌ 12 pts to go |
| P01_GOLD | 625 | 84.8% | 84.8% | +4.1 | 90% | 🟡 5 pts to go |
| P02 | 485 | 90.9% | 90.9% | +5.1 | 95% | 🟡 4 pts to go |
| P03 | 264 | 85.2% | 85.2% | +1.2 | 95% | 🟡 10 pts to go |
| P04 | 4104 | 89.4% | 89.4% | +6.1 | 90% | 🟡 1 pts to go |
| P05 | 420 | 93.1% | 93.1% | +4.6 | 95% | 🟡 2 pts to go |
| P06M | 13022 | 95.0% | 95.0% | +28.3 | n/a | no target |
| P06T | 86551 | 75.6% | 75.6% | +14.1 | n/a | no target |
| P06 | 296 | 93.6% | 93.6% | +11.5 | 100% | 🟡 6 pts to go |
| P07 | 786 | 92.5% | 92.5% | +15.3 | 100% | 🟡 8 pts to go |
| P08 | 25380 | 92.6% | 92.6% | +15.5 | 100% | 🟡 7 pts to go |
| P09 | 295 | 72.5% | 72.5% | +3.9 | n/a | no target |
| P10R | 102400 | 82.5% | 82.5% | +22.5 | n/a | no target |
| P10 | 2648 | 92.0% | 92.0% | +5.2 | 100% | 🟡 8 pts to go |
| P11 | 20970 | 66.3% | 66.3% | +47.5 | 80% | ❌ 14 pts to go |
| P12 | 7 | 71.4% | 71.4% | -3.6 | n/a | no target |
| P13 | 17402 | 74.7% | 74.7% | +23.7 | 95% | ❌ 20 pts to go |

## 4. AP

### `ap_contact_name_as_published`

> ceiling: owner 2026-11-08: the AP contact person the organisation itself names on its AP / finance page is allowed (name + role phrase, quoted); mailboxes stay organisational; many bodies publish no AP person

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 122 | 2.5% | 2.5% | -1.6 | n/a | no target |
| P01T | 431 | 7.0% | 7.0% | -1.4 | n/a | no target |
| P01_GOLD | 625 | 14.2% | 14.2% | +0.0 | 25% | ❌ 11 pts to go |
| P02 | 485 | 23.5% | 23.5% | -1.0 | 40% | ❌ 16 pts to go |
| P03 | 264 | 9.1% | 9.1% | +0.1 | 20% | ❌ 11 pts to go |
| P04 | 4104 | 3.0% | 3.0% | -0.6 | 20% | ❌ 17 pts to go |
| P05 | 420 | 3.3% | 3.3% | +0.0 | 15% | ❌ 12 pts to go |
| P06M | 13022 | 0.3% | 0.3% | +0.0 | n/a | no target |
| P06T | 86551 | 0.3% | 0.3% | -0.1 | n/a | no target |
| P06 | 296 | 5.7% | 5.7% | -0.5 | n/a | no target |
| P07 | 786 | 7.6% | 7.6% | +0.3 | n/a | no target |
| P08 | 25380 | 0.2% | 0.2% | -0.1 | n/a | no target |
| P09 | 295 | 7.8% | 7.8% | +0.2 | n/a | no target |
| P10R | 102400 | 0.2% | 0.2% | +0.0 | n/a | no target |
| P10 | 2648 | 0.9% | 0.9% | -0.1 | n/a | no target |
| P11 | 20970 | 0.1% | 0.1% | -0.1 | n/a | no target |
| P12 | 7 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P13 | 17402 | 0.4% | 0.4% | +0.0 | n/a | no target |

### `ap_phone`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 122 | 19.7% | 19.7% | -7.1 | n/a | no target |
| P01T | 431 | 21.1% | 21.1% | -3.0 | 70% | ❌ 49 pts to go |
| P01_GOLD | 625 | 43.4% | 43.4% | +0.1 | 80% | ❌ 37 pts to go |
| P02 | 485 | 56.1% | 56.1% | -0.7 | 90% | ❌ 34 pts to go |
| P03 | 264 | 18.6% | 18.6% | -0.5 | 60% | ❌ 41 pts to go |
| P04 | 4104 | 19.8% | 19.8% | -3.9 | 85% | ❌ 65 pts to go |
| P05 | 420 | 11.9% | 11.9% | +0.0 | 50% | ❌ 38 pts to go |
| P06M | 13022 | 0.7% | 0.7% | +0.3 | n/a | no target |
| P06T | 86551 | 0.5% | 0.5% | -0.1 | n/a | no target |
| P06 | 296 | 16.2% | 16.2% | +0.0 | n/a | no target |
| P07 | 786 | 10.9% | 10.9% | -2.1 | n/a | no target |
| P08 | 25380 | 0.6% | 0.6% | +0.1 | n/a | no target |
| P09 | 295 | 77.3% | 77.3% | -0.3 | 95% | ❌ 18 pts to go |
| P10R | 102400 | 0.2% | 0.2% | +0.0 | n/a | no target |
| P10 | 2648 | 1.7% | 1.7% | +0.0 | n/a | no target |
| P11 | 20970 | 2.0% | 2.0% | -1.6 | n/a | no target |
| P12 | 7 | 28.6% | 28.6% | +3.6 | n/a | no target |
| P13 | 17402 | 0.7% | 0.7% | +0.0 | n/a | no target |

### `invoice_mailing_address`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 122 | 7.4% | 7.4% | +0.2 | n/a | no target |
| P01T | 431 | 11.4% | 11.4% | -0.6 | n/a | no target |
| P01_GOLD | 625 | 33.9% | 33.9% | +0.0 | 70% | ❌ 36 pts to go |
| P02 | 485 | 37.9% | 37.9% | -1.0 | 75% | ❌ 37 pts to go |
| P03 | 264 | 18.6% | 18.6% | -0.5 | 55% | ❌ 36 pts to go |
| P04 | 4104 | 19.6% | 19.6% | -4.0 | 75% | ❌ 55 pts to go |
| P05 | 420 | 10.7% | 10.7% | -0.1 | 50% | ❌ 39 pts to go |
| P06M | 13022 | 0.2% | 0.2% | +0.0 | n/a | no target |
| P06T | 86551 | 0.3% | 0.3% | -0.1 | n/a | no target |
| P06 | 296 | 7.8% | 7.8% | -0.5 | n/a | no target |
| P07 | 786 | 5.2% | 5.2% | -1.2 | n/a | no target |
| P08 | 25380 | 0.2% | 0.2% | +0.0 | n/a | no target |
| P09 | 295 | 74.9% | 74.9% | -0.3 | 95% | ❌ 20 pts to go |
| P10R | 102400 | 0.1% | 0.1% | -0.1 | n/a | no target |
| P10 | 2648 | 1.0% | 1.0% | +0.0 | n/a | no target |
| P11 | 20970 | 1.9% | 1.9% | -1.7 | n/a | no target |
| P12 | 7 | 14.3% | 14.3% | +1.8 | n/a | no target |
| P13 | 17402 | 0.4% | 0.4% | +0.0 | n/a | no target |

### `invoicing_requirements`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 122 | 9.0% | 9.0% | +2.8 | n/a | no target |
| P01T | 431 | 7.9% | 7.9% | -1.4 | n/a | no target |
| P01_GOLD | 625 | 57.9% | 58.1% | -0.1 | 80% | ❌ 22 pts to go |
| P02 | 485 | 43.9% | 44.1% | -1.9 | 75% | ❌ 31 pts to go |
| P03 | 264 | 37.1% | 37.1% | -0.8 | 70% | ❌ 33 pts to go |
| P04 | 4104 | 19.3% | 19.7% | -3.8 | 70% | ❌ 51 pts to go |
| P05 | 420 | 14.5% | 14.5% | +0.2 | 50% | ❌ 36 pts to go |
| P06M | 13022 | 0.4% | 0.4% | +0.0 | n/a | no target |
| P06T | 86551 | 0.2% | 0.2% | -0.1 | n/a | no target |
| P06 | 296 | 14.5% | 14.5% | +1.1 | n/a | no target |
| P07 | 786 | 1.9% | 1.9% | -0.1 | n/a | no target |
| P08 | 25380 | 0.4% | 0.4% | +0.0 | n/a | no target |
| P09 | 295 | 46.1% | 46.4% | +0.2 | 80% | ❌ 34 pts to go |
| P10R | 102400 | 0.1% | 0.1% | +0.0 | n/a | no target |
| P10 | 2648 | 1.2% | 1.2% | +0.0 | n/a | no target |
| P11 | 20970 | 0.6% | 0.6% | -0.5 | n/a | no target |
| P12 | 7 | 42.9% | 42.9% | +5.4 | n/a | no target |
| P13 | 17402 | 0.3% | 0.3% | +0.0 | n/a | no target |

### `payment_terms_as_published`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 122 | 18.9% | 18.9% | +7.6 | n/a | no target |
| P01T | 431 | 17.4% | 17.4% | -4.6 | 60% | ❌ 43 pts to go |
| P01_GOLD | 625 | 63.5% | 63.5% | -0.1 | 70% | 🟡 6 pts to go |
| P02 | 485 | 38.4% | 38.4% | -0.5 | 50% | ❌ 12 pts to go |
| P03 | 264 | 48.5% | 48.5% | -1.5 | 55% | 🟡 6 pts to go |
| P04 | 4104 | 11.9% | 11.9% | -1.4 | 40% | ❌ 28 pts to go |
| P05 | 420 | 17.4% | 17.4% | +0.1 | 40% | ❌ 23 pts to go |
| P06M | 13022 | 2.3% | 2.3% | +1.6 | n/a | no target |
| P06T | 86551 | 2.6% | 2.6% | +0.2 | n/a | no target |
| P06 | 296 | 21.3% | 21.3% | +1.6 | n/a | no target |
| P07 | 786 | 6.7% | 6.7% | +0.0 | n/a | no target |
| P08 | 25380 | 2.9% | 2.9% | +0.3 | n/a | no target |
| P09 | 295 | 5.8% | 5.8% | -0.1 | n/a | no target |
| P10R | 102400 | 0.2% | 0.2% | +0.0 | n/a | no target |
| P10 | 2648 | 4.6% | 4.6% | +0.1 | n/a | no target |
| P11 | 20970 | 9.4% | 9.4% | +5.1 | n/a | no target |
| P12 | 7 | 0.0% | 0.0% | -12.5 | n/a | no target |
| P13 | 17402 | 0.2% | 0.2% | +0.0 | n/a | no target |

### `po_required_as_published`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 122 | 23.0% | 23.0% | +6.5 | n/a | no target |
| P01T | 431 | 22.3% | 22.3% | -3.0 | 65% | ❌ 43 pts to go |
| P01_GOLD | 625 | 69.0% | 69.0% | +0.0 | 70% | 🟡 1 pts to go |
| P02 | 485 | 23.3% | 23.3% | -0.6 | 50% | ❌ 27 pts to go |
| P03 | 264 | 52.3% | 52.3% | +0.0 | 60% | 🟡 8 pts to go |
| P04 | 4104 | 5.1% | 5.1% | -0.7 | 40% | ❌ 35 pts to go |
| P05 | 420 | 19.8% | 19.8% | +0.1 | 45% | ❌ 25 pts to go |
| P06M | 13022 | 1.5% | 1.5% | +1.2 | n/a | no target |
| P06T | 86551 | 0.6% | 0.6% | +0.0 | n/a | no target |
| P06 | 296 | 32.8% | 32.8% | +1.1 | n/a | no target |
| P07 | 786 | 7.1% | 7.1% | +0.2 | n/a | no target |
| P08 | 25380 | 1.2% | 1.2% | +0.1 | n/a | no target |
| P09 | 295 | 9.8% | 9.8% | -0.1 | n/a | no target |
| P10R | 102400 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P10 | 2648 | 2.7% | 2.7% | +0.1 | n/a | no target |
| P11 | 20970 | 1.0% | 1.0% | +0.0 | n/a | no target |
| P12 | 7 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P13 | 17402 | 0.2% | 0.2% | +0.0 | n/a | no target |

### `invoice_portal_url`

> ceiling: only portals the buyer names on its own pages; informational tax-authority links are not portals

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 122 | 13.9% | 13.9% | +7.7 | n/a | no target |
| P01T | 431 | 12.1% | 12.1% | -2.4 | n/a | no target |
| P01_GOLD | 625 | 49.8% | 49.8% | +0.0 | 50% | 🟡 0 pts to go |
| P02 | 485 | 36.1% | 36.1% | -1.3 | n/a | no target |
| P03 | 264 | 51.9% | 51.9% | -1.2 | 60% | 🟡 8 pts to go |
| P04 | 4104 | 10.7% | 10.7% | -2.2 | n/a | no target |
| P05 | 420 | 15.0% | 15.0% | -0.2 | n/a | no target |
| P06M | 13022 | 0.6% | 0.6% | +0.3 | n/a | no target |
| P06T | 86551 | 0.4% | 0.4% | -0.1 | n/a | no target |
| P06 | 296 | 24.0% | 24.0% | +2.3 | n/a | no target |
| P07 | 786 | 7.5% | 7.5% | +0.3 | n/a | no target |
| P08 | 25380 | 0.6% | 0.6% | +0.1 | n/a | no target |
| P09 | 295 | 18.3% | 18.3% | +0.1 | n/a | no target |
| P10R | 102400 | 0.1% | 0.1% | +0.0 | n/a | no target |
| P10 | 2648 | 2.4% | 2.4% | +0.1 | n/a | no target |
| P11 | 20970 | 0.7% | 0.7% | -0.1 | n/a | no target |
| P12 | 7 | 14.3% | 14.3% | +14.3 | n/a | no target |
| P13 | 17402 | 0.4% | 0.4% | +0.0 | n/a | no target |

### `buyer_payment_method_preference`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 122 | 12.3% | 12.3% | +1.0 | 15% | 🟡 3 pts to go |
| P01T | 431 | 9.7% | 9.7% | -1.4 | 15% | 🟡 5 pts to go |
| P01_GOLD | 625 | 35.4% | 35.4% | +0.1 | 40% | 🟡 5 pts to go |
| P02 | 485 | 12.6% | 12.8% | +0.1 | 25% | ❌ 12 pts to go |
| P03 | 264 | 17.4% | 17.4% | -0.6 | 25% | 🟡 8 pts to go |
| P04 | 4104 | 2.5% | 2.5% | -0.3 | 15% | ❌ 12 pts to go |
| P05 | 420 | 6.7% | 6.7% | -0.1 | 15% | 🟡 8 pts to go |
| P06M | 13022 | 0.9% | 0.9% | +0.3 | 15% | ❌ 14 pts to go |
| P06T | 86551 | 0.6% | 0.6% | +0.2 | 15% | ❌ 14 pts to go |
| P06 | 296 | 10.5% | 10.5% | +1.2 | 15% | 🟡 4 pts to go |
| P07 | 786 | 4.2% | 4.2% | +1.0 | 15% | ❌ 11 pts to go |
| P08 | 25380 | 0.7% | 0.7% | +0.3 | 15% | ❌ 14 pts to go |
| P09 | 295 | 1.0% | 1.0% | +0.0 | 15% | ❌ 14 pts to go |
| P10R | 102400 | 0.7% | 0.7% | +0.3 | 15% | ❌ 14 pts to go |
| P10 | 2648 | 1.2% | 1.2% | +0.2 | 15% | ❌ 14 pts to go |
| P11 | 20970 | 0.4% | 0.4% | +0.2 | 15% | ❌ 15 pts to go |
| P12 | 7 | 14.3% | 14.3% | +1.8 | 15% | 🟡 1 pts to go |
| P13 | 17402 | 0.6% | 0.6% | +0.2 | 15% | ❌ 14 pts to go |

### `buyer_tax_exempt_status`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 122 | 5.7% | 5.7% | -0.5 | 15% | 🟡 9 pts to go |
| P01T | 431 | 9.3% | 9.3% | -2.7 | 25% | ❌ 16 pts to go |
| P01_GOLD | 625 | 29.1% | 29.1% | -0.1 | 25% | ✅ met |
| P02 | 485 | 24.3% | 24.3% | -1.1 | 15% | ✅ met |
| P03 | 264 | 22.0% | 22.0% | +0.5 | 15% | ✅ met |
| P04 | 4104 | 3.8% | 3.8% | -0.3 | 15% | ❌ 11 pts to go |
| P05 | 420 | 11.2% | 11.2% | +0.4 | 15% | 🟡 4 pts to go |
| P06M | 13022 | 0.5% | 0.5% | +0.3 | 15% | ❌ 14 pts to go |
| P06T | 86551 | 0.3% | 0.3% | +0.0 | 15% | ❌ 15 pts to go |
| P06 | 296 | 8.4% | 8.4% | +0.8 | 15% | 🟡 7 pts to go |
| P07 | 786 | 2.7% | 2.7% | -0.4 | 15% | ❌ 12 pts to go |
| P08 | 25380 | 0.5% | 0.5% | +0.1 | 15% | ❌ 14 pts to go |
| P09 | 295 | 1.0% | 1.0% | +0.0 | 15% | ❌ 14 pts to go |
| P10R | 102400 | 0.0% | 0.0% | +0.0 | 15% | ❌ 15 pts to go |
| P10 | 2648 | 1.5% | 1.5% | -0.1 | 15% | ❌ 14 pts to go |
| P11 | 20970 | 0.5% | 0.5% | +0.0 | 15% | ❌ 14 pts to go |
| P12 | 7 | 28.6% | 28.6% | +3.6 | 15% | ✅ met |
| P13 | 17402 | 0.1% | 0.1% | +0.1 | 15% | ❌ 15 pts to go |

### `buyer_ap_cycle_published`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 122 | 1.6% | 1.6% | +1.6 | 20% | ❌ 18 pts to go |
| P01T | 431 | 3.0% | 3.0% | -0.9 | 20% | ❌ 17 pts to go |
| P01_GOLD | 625 | 4.5% | 4.5% | +0.2 | 20% | ❌ 16 pts to go |
| P02 | 485 | 1.4% | 1.4% | +0.1 | 20% | ❌ 19 pts to go |
| P03 | 264 | 1.5% | 1.5% | -0.1 | 20% | ❌ 18 pts to go |
| P04 | 4104 | 0.5% | 0.5% | -0.1 | 20% | ❌ 20 pts to go |
| P05 | 420 | 1.2% | 1.2% | +0.0 | 20% | ❌ 19 pts to go |
| P06M | 13022 | 0.1% | 0.1% | +0.1 | 20% | ❌ 20 pts to go |
| P06T | 86551 | 0.0% | 0.0% | +0.0 | 20% | ❌ 20 pts to go |
| P06 | 296 | 1.4% | 1.4% | +0.0 | 20% | ❌ 19 pts to go |
| P07 | 786 | 0.4% | 0.4% | +0.0 | 20% | ❌ 20 pts to go |
| P08 | 25380 | 0.0% | 0.0% | +0.0 | 20% | ❌ 20 pts to go |
| P09 | 295 | 0.0% | 0.0% | +0.0 | 20% | ❌ 20 pts to go |
| P10R | 102400 | 0.0% | 0.0% | +0.0 | 20% | ❌ 20 pts to go |
| P10 | 2648 | 0.3% | 0.3% | +0.0 | 20% | ❌ 20 pts to go |
| P11 | 20970 | 0.0% | 0.0% | +0.0 | 20% | ❌ 20 pts to go |
| P12 | 7 | 0.0% | 0.0% | +0.0 | 20% | ❌ 20 pts to go |
| P13 | 17402 | 0.0% | 0.0% | +0.0 | 20% | ❌ 20 pts to go |

### `buyer_esignature_preference`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 122 | 1.6% | 1.6% | +0.6 | 15% | ❌ 13 pts to go |
| P01T | 431 | 2.3% | 2.3% | -0.1 | 15% | ❌ 13 pts to go |
| P01_GOLD | 625 | 10.4% | 10.4% | -0.1 | 15% | 🟡 5 pts to go |
| P02 | 485 | 11.5% | 11.5% | -0.5 | 15% | 🟡 4 pts to go |
| P03 | 264 | 20.1% | 20.1% | -0.6 | 15% | ✅ met |
| P04 | 4104 | 2.2% | 2.2% | -0.2 | 15% | ❌ 13 pts to go |
| P05 | 420 | 2.9% | 2.9% | -0.1 | 15% | ❌ 12 pts to go |
| P06M | 13022 | 0.4% | 0.4% | +0.2 | 15% | ❌ 15 pts to go |
| P06T | 86551 | 0.2% | 0.2% | +0.0 | 15% | ❌ 15 pts to go |
| P06 | 296 | 5.4% | 5.4% | +0.2 | 15% | 🟡 10 pts to go |
| P07 | 786 | 1.8% | 1.8% | +0.1 | 15% | ❌ 13 pts to go |
| P08 | 25380 | 0.5% | 0.5% | +0.1 | 15% | ❌ 14 pts to go |
| P09 | 295 | 0.7% | 0.7% | +0.0 | 15% | ❌ 14 pts to go |
| P10R | 102400 | 0.0% | 0.0% | +0.0 | 15% | ❌ 15 pts to go |
| P10 | 2648 | 1.0% | 1.0% | +0.1 | 15% | ❌ 14 pts to go |
| P11 | 20970 | 0.4% | 0.4% | +0.1 | 15% | ❌ 15 pts to go |
| P12 | 7 | 0.0% | 0.0% | +0.0 | 15% | ❌ 15 pts to go |
| P13 | 17402 | 0.1% | 0.1% | +0.0 | 15% | ❌ 15 pts to go |

### `ap_system_hint`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 122 | 15.6% | 15.6% | +8.4 | 20% | 🟡 4 pts to go |
| P01T | 431 | 12.8% | 12.8% | -2.3 | 40% | ❌ 27 pts to go |
| P01_GOLD | 625 | 46.1% | 46.1% | +0.3 | 40% | ✅ met |
| P02 | 485 | 41.4% | 41.4% | -1.4 | 20% | ✅ met |
| P03 | 264 | 48.9% | 48.9% | +0.1 | 35% | ✅ met |
| P04 | 4104 | 13.0% | 13.0% | -2.4 | 20% | 🟡 7 pts to go |
| P05 | 420 | 15.2% | 15.2% | +0.4 | 20% | 🟡 5 pts to go |
| P06M | 13022 | 0.9% | 0.9% | +0.4 | 20% | ❌ 19 pts to go |
| P06T | 86551 | 0.6% | 0.6% | -0.1 | 20% | ❌ 19 pts to go |
| P06 | 296 | 24.0% | 24.0% | +1.9 | 20% | ✅ met |
| P07 | 786 | 7.8% | 7.8% | +0.7 | 20% | ❌ 12 pts to go |
| P08 | 25380 | 1.1% | 1.1% | +0.2 | 20% | ❌ 19 pts to go |
| P09 | 295 | 19.0% | 19.0% | +0.8 | 20% | 🟡 1 pts to go |
| P10R | 102400 | 0.2% | 0.2% | +0.0 | 20% | ❌ 20 pts to go |
| P10 | 2648 | 3.5% | 3.5% | +0.1 | 20% | ❌ 16 pts to go |
| P11 | 20970 | 0.8% | 0.8% | -0.2 | 20% | ❌ 19 pts to go |
| P12 | 7 | 0.0% | 0.0% | +0.0 | 20% | ❌ 20 pts to go |
| P13 | 17402 | 0.6% | 0.6% | +0.1 | 20% | ❌ 19 pts to go |

## 5. contract

### `contract_value`

> ceiling: rows proven by a lobbying filing, a news release, an auditor appointment, a customer story or a vendor's client list have no contract value by nature (≈17 % of P01 Gold); bids&tenders awards now carry the awarded bidder's submitted price when no award value was published

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 122 | 33.6% | 33.6% | -10.7 | n/a | no target |
| P01T | 431 | 0.2% | 0.2% | -0.1 | n/a | no target |
| P01_GOLD | 625 | 69.4% | 69.4% | -0.1 | 95% | ❌ 26 pts to go |
| P02 | 485 | 60.4% | 60.4% | -2.6 | 95% | ❌ 35 pts to go |
| P03 | 264 | 53.0% | 53.0% | -1.7 | 90% | ❌ 37 pts to go |
| P04 | 4104 | 22.5% | 22.5% | -4.6 | 85% | ❌ 62 pts to go |
| P05 | 420 | 37.4% | 37.4% | +0.9 | 75% | ❌ 38 pts to go |
| P06M | 13022 | 36.0% | 36.0% | -14.1 | n/a | no target |
| P06T | 86551 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06 | 296 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P07 | 786 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P08 | 25380 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P09 | 295 | 89.5% | 89.5% | +0.1 | 100% | ❌ 10 pts to go |
| P10R | 102400 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P10 | 2648 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P11 | 20970 | 0.4% | 0.4% | -0.5 | 60% | ❌ 60 pts to go |
| P12 | 7 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P13 | 17402 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `currency`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 122 | 33.6% | 33.6% | -10.7 | n/a | no target |
| P01T | 431 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P01_GOLD | 625 | 72.8% | 72.8% | +0.0 | 100% | ❌ 27 pts to go |
| P02 | 485 | 63.7% | 63.7% | -2.8 | 100% | ❌ 36 pts to go |
| P03 | 264 | 58.7% | 58.7% | -1.8 | n/a | no target |
| P04 | 4104 | 23.1% | 23.1% | -4.7 | 95% | ❌ 72 pts to go |
| P05 | 420 | 33.3% | 33.3% | +0.3 | 80% | ❌ 47 pts to go |
| P06M | 13022 | 36.0% | 36.0% | -14.1 | n/a | no target |
| P06T | 86551 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06 | 296 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P07 | 786 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P08 | 25380 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P09 | 295 | 92.5% | 92.5% | -0.2 | 100% | 🟡 8 pts to go |
| P10R | 102400 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P10 | 2648 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P11 | 20970 | 0.4% | 0.4% | -0.6 | n/a | no target |
| P12 | 7 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P13 | 17402 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `start_date`

> ceiling: most award notices publish an award date, not a start date; start_date carries the signature date when the source gives one, labelled

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 122 | 82.0% | 82.0% | +3.6 | n/a | no target |
| P01T | 431 | 0.2% | 0.2% | -0.1 | n/a | no target |
| P01_GOLD | 625 | 51.7% | 51.7% | +0.1 | 85% | ❌ 33 pts to go |
| P02 | 485 | 55.3% | 55.3% | -2.3 | 90% | ❌ 35 pts to go |
| P03 | 264 | 42.4% | 42.4% | -1.7 | 85% | ❌ 43 pts to go |
| P04 | 4104 | 25.2% | 25.2% | -5.2 | 90% | ❌ 65 pts to go |
| P05 | 420 | 33.1% | 33.1% | +0.3 | 75% | ❌ 42 pts to go |
| P06M | 13022 | 89.8% | 89.8% | -0.6 | n/a | no target |
| P06T | 86551 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06 | 296 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P07 | 786 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P08 | 25380 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P09 | 295 | 85.1% | 85.1% | +0.0 | 95% | 🟡 10 pts to go |
| P10R | 102400 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P10 | 2648 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P11 | 20970 | 0.4% | 0.4% | -0.4 | n/a | no target |
| P12 | 7 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P13 | 17402 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `end_date`

> ceiling: an inferred end (award date + published duration) is labelled as such; sources without a duration leave end_date empty — the honest ceiling. P09 is BY DEFINITION the rows whose end date is not published (older SEAO contracts with no closing notice): its end_date / duration targets cannot be met without inventing a date

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 122 | 81.1% | 81.1% | +1.7 | n/a | no target |
| P01T | 431 | 0.2% | 0.2% | -0.1 | n/a | no target |
| P01_GOLD | 625 | 51.8% | 51.8% | +0.0 | 85% | ❌ 33 pts to go |
| P02 | 485 | 50.5% | 50.5% | -2.2 | 90% | ❌ 40 pts to go |
| P03 | 264 | 43.6% | 43.6% | -1.7 | 85% | ❌ 41 pts to go |
| P04 | 4104 | 21.6% | 21.6% | -4.4 | 90% | ❌ 68 pts to go |
| P05 | 420 | 43.6% | 43.6% | +0.7 | 75% | ❌ 31 pts to go |
| P06M | 13022 | 80.4% | 80.4% | -3.3 | n/a | no target |
| P06T | 86551 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06 | 296 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P07 | 786 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P08 | 25380 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P09 | 295 | 0.3% | 0.3% | +0.0 | 95% | ❌ 95 pts to go |
| P10R | 102400 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P10 | 2648 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P11 | 20970 | 0.3% | 0.3% | -0.4 | n/a | no target |
| P12 | 7 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P13 | 17402 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `contract_title`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 122 | 90.2% | 90.2% | +4.6 | n/a | no target |
| P01T | 431 | 91.6% | 91.6% | -0.6 | n/a | no target |
| P01_GOLD | 625 | 85.4% | 85.4% | -0.1 | 100% | ❌ 15 pts to go |
| P02 | 485 | 75.3% | 75.3% | -0.4 | 100% | ❌ 25 pts to go |
| P03 | 264 | 91.3% | 91.3% | -0.9 | n/a | no target |
| P04 | 4104 | 48.7% | 48.7% | -2.8 | 95% | ❌ 46 pts to go |
| P05 | 420 | 77.6% | 77.6% | -0.2 | 95% | ❌ 17 pts to go |
| P06M | 13022 | 98.8% | 98.8% | +0.5 | n/a | no target |
| P06T | 86551 | 79.8% | 79.8% | -3.9 | n/a | no target |
| P06 | 296 | 24.3% | 24.3% | -1.9 | n/a | no target |
| P07 | 786 | 15.1% | 15.1% | -4.0 | n/a | no target |
| P08 | 25380 | 8.9% | 9.0% | -2.1 | n/a | no target |
| P09 | 295 | 98.6% | 98.6% | -0.1 | 100% | 🟡 1 pts to go |
| P10R | 102400 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P10 | 2648 | 71.0% | 71.0% | -0.7 | n/a | no target |
| P11 | 20970 | 9.0% | 9.0% | -7.1 | n/a | no target |
| P12 | 7 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P13 | 17402 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `contract_description`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 122 | 90.2% | 90.2% | +4.6 | n/a | no target |
| P01T | 431 | 91.6% | 91.6% | -0.6 | n/a | no target |
| P01_GOLD | 625 | 88.6% | 88.6% | -0.1 | 100% | ❌ 11 pts to go |
| P02 | 485 | 76.3% | 76.5% | -0.5 | 100% | ❌ 24 pts to go |
| P03 | 264 | 92.0% | 92.0% | -1.0 | n/a | no target |
| P04 | 4104 | 51.7% | 51.7% | -3.4 | 95% | ❌ 43 pts to go |
| P05 | 420 | 90.0% | 90.0% | -0.2 | 70% | ✅ met |
| P06M | 13022 | 98.8% | 98.8% | +0.5 | n/a | no target |
| P06T | 86551 | 79.8% | 79.8% | -3.9 | n/a | no target |
| P06 | 296 | 24.3% | 24.3% | -1.9 | n/a | no target |
| P07 | 786 | 15.1% | 15.1% | -4.0 | n/a | no target |
| P08 | 25380 | 8.9% | 9.0% | -2.1 | n/a | no target |
| P09 | 295 | 98.6% | 98.6% | -0.1 | 100% | 🟡 1 pts to go |
| P10R | 102400 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P10 | 2648 | 71.0% | 71.0% | -0.7 | n/a | no target |
| P11 | 20970 | 9.0% | 9.0% | -7.1 | n/a | no target |
| P12 | 7 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P13 | 17402 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `number_of_bids`

> ceiling: published by some portals only (bids&tenders submission lists, Biddingo bidder lists); federal proactive disclosure does not publish bid counts

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 122 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P01T | 431 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P01_GOLD | 625 | 16.8% | 16.8% | +0.0 | 60% | ❌ 43 pts to go · rows from a source that publishes bids: 363 rows, 28.9% filled |
| P02 | 485 | 10.7% | 10.7% | -0.5 | n/a | no target · rows from a source that publishes bids: 290 rows, 17.9% filled |
| P03 | 264 | 12.9% | 12.9% | -0.4 | n/a | no target · rows from a source that publishes bids: 139 rows, 24.5% filled |
| P04 | 4104 | 1.3% | 1.3% | -0.3 | n/a | no target · rows from a source that publishes bids: 872 rows, 6.3% filled |
| P05 | 420 | 2.9% | 2.9% | -0.1 | n/a | no target · rows from a source that publishes bids: 51 rows, 23.5% filled |
| P06M | 13022 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06T | 86551 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06 | 296 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P07 | 786 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P08 | 25380 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P09 | 295 | 3.1% | 3.1% | +0.1 | n/a | no target · rows from a source that publishes bids: 282 rows, 3.2% filled |
| P10R | 102400 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P10 | 2648 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P11 | 20970 | 0.1% | 0.1% | +0.0 | n/a | no target · rows from a source that publishes bids: 88 rows, 13.6% filled |
| P12 | 7 | 0.0% | 0.0% | +0.0 | n/a | no target · rows from a source that publishes bids: 7 rows, 0.0% filled |
| P13 | 17402 | 0.0% | 0.0% | +0.0 | n/a | no target |

## 6. history

### `average_contract_duration_days`

> ceiling: needs two dates (or a published term) on the buyer's records; P09 rows (end date unpublished by definition) and buyers whose sources publish award dates only have no honest duration

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 122 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P01T | 431 | 0.2% | 98.6% | -0.1 | n/a | no target |
| P01_GOLD | 625 | 53.3% | 82.4% | +0.1 | 90% | ❌ 37 pts to go |
| P02 | 485 | 50.3% | 88.0% | -2.2 | 90% | ❌ 40 pts to go |
| P03 | 264 | 44.3% | 80.7% | -1.4 | 90% | ❌ 46 pts to go |
| P04 | 4104 | 17.3% | 94.4% | -3.6 | 90% | ❌ 73 pts to go |
| P05 | 420 | 0.0% | 83.1% | +0.0 | 90% | ❌ 90 pts to go |
| P06M | 13022 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P06T | 86551 | 0.0% | 99.9% | +0.0 | n/a | no target |
| P06 | 296 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P07 | 786 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P08 | 25380 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P09 | 295 | 2.4% | 4.1% | +0.1 | 90% | ❌ 88 pts to go |
| P10R | 102400 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P10 | 2648 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P11 | 20970 | 0.3% | 99.8% | -0.3 | n/a | no target |
| P12 | 7 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P13 | 17402 | 0.0% | 100.0% | +0.0 | n/a | no target |

### `commodity_distribution_top3`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 122 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P01T | 431 | 0.5% | 98.8% | -0.1 | n/a | no target |
| P01_GOLD | 625 | 25.9% | 55.0% | +0.0 | 90% | ❌ 64 pts to go |
| P02 | 485 | 49.5% | 87.2% | -2.1 | n/a | no target |
| P03 | 264 | 24.2% | 60.6% | -0.8 | n/a | no target |
| P04 | 4104 | 19.0% | 96.1% | -3.9 | n/a | no target |
| P05 | 420 | 0.5% | 83.6% | +0.0 | n/a | no target |
| P06M | 13022 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P06T | 86551 | 0.0% | 100.0% | -0.1 | n/a | no target |
| P06 | 296 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P07 | 786 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P08 | 25380 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P09 | 295 | 41.4% | 43.1% | -0.5 | n/a | no target |
| P10R | 102400 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P10 | 2648 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P11 | 20970 | 0.3% | 99.8% | -0.3 | n/a | no target |
| P12 | 7 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P13 | 17402 | 0.0% | 100.0% | +0.0 | n/a | no target |

### `year_over_year_spend_trend`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 122 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P01T | 431 | 1.4% | 99.8% | -0.1 | n/a | no target |
| P01_GOLD | 625 | 51.8% | 81.0% | +0.0 | 95% | ❌ 43 pts to go |
| P02 | 485 | 54.2% | 92.0% | -2.4 | n/a | no target |
| P03 | 264 | 46.6% | 83.0% | -1.4 | n/a | no target |
| P04 | 4104 | 19.2% | 96.3% | -3.9 | n/a | no target |
| P05 | 420 | 4.5% | 87.6% | -0.2 | n/a | no target |
| P06M | 13022 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P06T | 86551 | 0.1% | 100.0% | +0.0 | n/a | no target |
| P06 | 296 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P07 | 786 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P08 | 25380 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P09 | 295 | 63.7% | 65.4% | -0.3 | n/a | no target |
| P10R | 102400 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P10 | 2648 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P11 | 20970 | 0.3% | 99.8% | -0.3 | n/a | no target |
| P12 | 7 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P13 | 17402 | 0.0% | 100.0% | +0.0 | n/a | no target |

## 7. mail security

### `mta_sts`

> ceiling: DNS-only check; 'no record' counts as checked

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 122 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P01T | 431 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P01_GOLD | 625 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P02 | 485 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P03 | 264 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P04 | 4104 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P05 | 420 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P06M | 13022 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P06T | 86551 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P06 | 296 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P07 | 786 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P08 | 25380 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P09 | 295 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P10R | 102400 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P10 | 2648 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P11 | 20970 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P12 | 7 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P13 | 17402 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |

### `tls_rpt`

> ceiling: DNS-only check; 'no record' counts as checked

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 122 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P01T | 431 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P01_GOLD | 625 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P02 | 485 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P03 | 264 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P04 | 4104 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P05 | 420 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P06M | 13022 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P06T | 86551 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P06 | 296 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P07 | 786 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P08 | 25380 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P09 | 295 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P10R | 102400 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P10 | 2648 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P11 | 20970 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P12 | 7 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P13 | 17402 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |

### `bimi`

> ceiling: DNS-only check; 'no record' counts as checked

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 122 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P01T | 431 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P01_GOLD | 625 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P02 | 485 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P03 | 264 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P04 | 4104 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P05 | 420 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P06M | 13022 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P06T | 86551 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P06 | 296 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P07 | 786 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P08 | 25380 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P09 | 295 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P10R | 102400 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P10 | 2648 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P11 | 20970 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P12 | 7 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P13 | 17402 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |

