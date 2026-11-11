# Coverage vs the downstream team's targets — 2026-11-11

Benchmarks (field × package with a numeric target): **98 of 446 met** (22.0%); 67 within 10 points; 281 further away.
A cell counts as filled only when it carries a value: blank, `not_published`, `not_found_yet` and label-only cells ("no identifier published …", "no dataset record …", "0 in the contract dataset …") do not count; the DNS checks count when checked. `any` = share of non-blank cells incl. such labels. Δ = change since the previous build in `coord/results/coverage_history.csv`.
Rows per package: P01M 123, P01T 446, P01_GOLD 625, P02 486, P03 264, P04 4132, P05 420, P06M 13240, P06T 95584, P06 297, P07 788, P08 25442, P09 294, P10R 105619, P10 2652, P11 24579, P12 7, P13 17451

## Invoice-grade readiness (the row as an invoice header: bill-to, submit-to, references, terms, tax, vendor identity, follow-up)

| package | rows | all 11 elements | ≥ 9 of 11 | median elements | most-missing element |
|---|---|---|---|---|---|
| P01M | 123 | 0.0% | 21.1% | 8 | vendor GST/HST number (109 rows) |
| P01T | 446 | 0.4% | 30.3% | 8 | payment terms (365 rows) |
| P01_GOLD | 625 | 25.1% | 71.5% | 10 | payment terms (214 rows) |
| P02 | 486 | 7.0% | 52.9% | 9 | PO rule (373 rows) |
| P03 | 264 | 14.8% | 57.2% | 9 | payment terms (130 rows) |
| P04 | 4132 | 1.2% | 15.2% | 6 | PO rule (3924 rows) |
| P05 | 420 | 1.2% | 17.9% | 7 | payment terms (345 rows) |
| P06M | 13240 | 0.0% | 3.2% | 8 | PO rule (13048 rows) |
| P06T | 95584 | 0.1% | 14.1% | 7 | PO rule (94930 rows) |
| P06 | 297 | 0.0% | 11.8% | 7 | reference to quote (PO / contract / vendor id) (297 rows) |
| P07 | 788 | 0.0% | 2.7% | 6 | reference to quote (PO / contract / vendor id) (788 rows) |
| P08 | 25442 | 0.0% | 0.6% | 6 | reference to quote (PO / contract / vendor id) (25442 rows) |
| P09 | 294 | 1.0% | 46.3% | 8 | payment terms (275 rows) |
| P10R | 105619 | 0.0% | 23.0% | 8 | PO rule (105581 rows) |
| P10 | 2652 | 0.0% | 1.1% | 5 | reference to quote (PO / contract / vendor id) (2652 rows) |
| P11 | 24579 | 0.2% | 19.7% | 8 | PO rule (24342 rows) |
| P12 | 7 | 0.0% | 42.9% | 8 | PO rule (7 rows) |
| P13 | 17451 | 0.0% | 0.2% | 7 | reference to quote (PO / contract / vendor id) (17451 rows) |

## AP grade (how stringently the row's accounts-payable data meets what an invoice needs; A = invoicing mailbox referee-confirmed on the buyer's own domain with MX, legal name, address, PO rule and terms all published, no penalties)

| package | rows | A | B | C | D | E | median ap_score |
|---|---|---|---|---|---|---|---|
| P01M | 123 | 8 | 26 | 89 | 0 | 0 | 71 |
| P01T | 446 | 31 | 71 | 344 | 0 | 0 | 67 |
| P01_GOLD | 625 | 227 | 199 | 199 | 0 | 0 | 82 |
| P02 | 486 | 0 | 196 | 290 | 0 | 0 | 66 |
| P03 | 264 | 0 | 0 | 252 | 12 | 0 | 57 |
| P04 | 4132 | 0 | 0 | 3485 | 647 | 0 | 46 |
| P05 | 420 | 16 | 29 | 363 | 12 | 0 | 51 |
| P06M | 13240 | 0 | 9 | 13170 | 61 | 0 | 46 |
| P06T | 95584 | 0 | 49 | 74932 | 20603 | 0 | 38 |
| P06 | 297 | 22 | 56 | 219 | 0 | 0 | 71 |
| P07 | 788 | 0 | 31 | 737 | 20 | 0 | 54 |
| P08 | 25442 | 0 | 0 | 22119 | 3323 | 0 | 44 |
| P09 | 294 | 3 | 12 | 277 | 2 | 0 | 53 |
| P10R | 105619 | 1 | 14 | 74827 | 30777 | 0 | 38 |
| P10 | 2652 | 2 | 14 | 2016 | 620 | 0 | 43 |
| P11 | 24579 | 7 | 16 | 41 | 0 | 24515 | 23 |
| P12 | 7 | 0 | 0 | 7 | 0 | 0 | 54 |
| P13 | 17451 | 0 | 17 | 14354 | 3080 | 0 | 43 |

### AP payability (confirmed channel + bill-to legal name and address + the buyer's reference rule + tax treatment known)

| package | rows | payable today | % | most common gap |
|---|---|---|---|---|
| P01M | 123 | 103 | 83.7% | the buyer's PO / reference rule (10) |
| P01T | 446 | 253 | 56.7% | bill-to legal name and address (157) |
| P01_GOLD | 625 | 472 | 75.5% | bill-to legal name and address (97) |
| P02 | 486 | 313 | 64.4% | the buyer's PO / reference rule (99) |
| P03 | 264 | 0 | 0.0% | a confirmed invoicing / AP or finance channel (264) |
| P04 | 4132 | 0 | 0.0% | a confirmed invoicing / AP or finance channel (4132) |
| P05 | 420 | 47 | 11.2% | a confirmed invoicing / AP or finance channel (334) |
| P06M | 13240 | 127 | 1.0% | a confirmed invoicing / AP or finance channel (13070) |
| P06T | 95584 | 591 | 0.6% | a confirmed invoicing / AP or finance channel (94303) |
| P06 | 297 | 54 | 18.2% | the buyer's PO / reference rule (132) |
| P07 | 788 | 13 | 1.6% | the buyer's PO / reference rule (307) |
| P08 | 25442 | 0 | 0.0% | a confirmed invoicing / AP or finance channel (25442) |
| P09 | 294 | 41 | 13.9% | a confirmed invoicing / AP or finance channel (244) |
| P10R | 105619 | 596 | 0.6% | a confirmed invoicing / AP or finance channel (104393) |
| P10 | 2652 | 5 | 0.2% | a confirmed invoicing / AP or finance channel (2559) |
| P11 | 24579 | 14 | 0.1% | a confirmed invoicing / AP or finance channel (24515) |
| P12 | 7 | 3 | 42.9% | a confirmed invoicing / AP or finance channel (4) |
| P13 | 17451 | 8 | 0.0% | a confirmed invoicing / AP or finance channel (17104) |

### Pay on sight (an invoice generated from the row would clear AP: confirmed invoicing / AP or finance channel, bill-to legal name + address, vendor legal name + GST/HST number + remit-to address, tax treatment and currency known — published or labelled-derived; the buyer's reference rule is reported separately)

| package | rows | pay on sight | % | + reference rule not published | routed (general inbox only) | most common gap |
|---|---|---|---|---|---|---|
| P01M | 123 | 6 | 4.9% | 6 | 0 | the vendor's GST/HST number (BN9) (109) |
| P01T | 446 | 150 | 33.6% | 14 | 0 | the vendor's GST/HST number (BN9) (185) |
| P01_GOLD | 625 | 407 | 65.1% | 11 | 0 | the vendor's GST/HST number (BN9) (144) |
| P02 | 486 | 211 | 43.4% | 34 | 0 | the vendor's GST/HST number (BN9) (205) |
| P03 | 264 | 16 | 6.1% | 0 | 137 | an invoicing / AP or finance mailbox (only a purchasing / general inbo (89) |
| P04 | 4132 | 42 | 1.0% | 6 | 1020 | an invoicing / AP or finance mailbox (only a purchasing / general inbo (3004) |
| P05 | 420 | 20 | 4.8% | 8 | 121 | an invoicing / AP or finance mailbox (only a purchasing / general inbo (205) |
| P06M | 13240 | 3 | 0.0% | 11 | 359 | an invoicing / AP or finance mailbox (only a purchasing / general inbo (12667) |
| P06T | 95584 | 550 | 0.6% | 48 | 33086 | an invoicing / AP or finance mailbox (only a purchasing / general inbo (61007) |
| P06 | 297 | 32 | 10.8% | 51 | 0 | the vendor's GST/HST number (BN9) (139) |
| P07 | 788 | 10 | 1.3% | 115 | 38 | the vendor's GST/HST number (BN9) (372) |
| P08 | 25442 | 3 | 0.0% | 16 | 5329 | an invoicing / AP or finance mailbox (only a purchasing / general inbo (20035) |
| P09 | 294 | 39 | 13.3% | 1 | 122 | an invoicing / AP or finance mailbox (only a purchasing / general inbo (113) |
| P10R | 105619 | 917 | 0.9% | 0 | 58120 | an invoicing / AP or finance mailbox (only a purchasing / general inbo (46213) |
| P10 | 2652 | 5 | 0.2% | 24 | 447 | an invoicing / AP or finance mailbox (only a purchasing / general inbo (2081) |
| P11 | 24579 | 86 | 0.3% | 4 | 0 | a confirmed invoicing / AP or finance channel (24419) |
| P12 | 7 | 1 | 14.3% | 0 | 2 | the vendor's GST/HST number (BN9) (2) |
| P13 | 17451 | 9 | 0.1% | 260 | 10410 | an invoicing / AP or finance mailbox (only a purchasing / general inbo (6656) |
| **all** | 292449 | 2507 | 0.9% | 609 | 109191 | |

### What still blocks grade A (rows per missing element; a row counts under every element it lacks)

| package | rows not A | referee confirmation of the mailbox | an invoicing / AP mailbox (not finance / procurement / general) | a mailbox on the buyer's own domain | MX record for the mailbox domain | published bill-to legal name | invoice / billing address | published PO rule | published payment terms | clear the penalty |
|---|---|---|---|---|---|---|---|---|---|---|
| P01M | 115 | 0 | 0 | 0 | 63 | 7 | 0 | 95 | 100 | 4 |
| P01T | 415 | 0 | 0 | 0 | 221 | 139 | 49 | 342 | 367 | 45 |
| P01_GOLD | 398 | 0 | 0 | 0 | 11 | 78 | 31 | 194 | 228 | 59 |
| P02 | 486 | 0 | 486 | 0 | 49 | 62 | 19 | 373 | 300 | 23 |
| P03 | 264 | 0 | 264 | 0 | 15 | 42 | 25 | 126 | 136 | 26 |
| P04 | 4132 | 0 | 4132 | 0 | 1916 | 1520 | 995 | 3924 | 3638 | 181 |
| P05 | 404 | 0 | 354 | 0 | 76 | 87 | 42 | 337 | 347 | 53 |
| P06M | 13240 | 0 | 13240 | 0 | 8556 | 1053 | 111 | 13048 | 12935 | 198 |
| P06T | 95584 | 0 | 95584 | 0 | 79382 | 55208 | 25292 | 94930 | 92933 | 8966 |
| P06 | 275 | 0 | 0 | 0 | 121 | 72 | 50 | 198 | 234 | 11 |
| P07 | 788 | 0 | 788 | 0 | 481 | 313 | 127 | 732 | 733 | 19 |
| P08 | 25442 | 0 | 25442 | 0 | 18860 | 11343 | 4856 | 25123 | 24703 | 562 |
| P09 | 291 | 0 | 270 | 0 | 9 | 67 | 2 | 265 | 277 | 45 |
| P10R | 105618 | 0 | 105441 | 0 | 83871 | 64621 | 40264 | 105581 | 105428 | 27 |
| P10 | 2650 | 0 | 2613 | 0 | 1296 | 1311 | 892 | 2580 | 2530 | 134 |
| P11 | 24572 | 24515 | 24448 | 0 | 23021 | 14500 | 1181 | 24342 | 22094 | 165 |
| P12 | 7 | 0 | 6 | 0 | 0 | 1 | 0 | 7 | 7 | 0 |
| P13 | 17451 | 0 | 17348 | 0 | 8824 | 8567 | 3900 | 17415 | 17410 | 19 |

## Where the work is (largest gaps in rows still needed)

| field | package | now | target | rows needed |
|---|---|---|---|---|
| buyer_ap_cycle_published | P10R | 0.0% | 20% | 21095 |
| ap_system_hint | P10R | 0.2% | 20% | 20917 |
| buyer_ap_cycle_published | P06T | 0.0% | 20% | 19084 |
| ap_system_hint | P06T | 0.7% | 20% | 18478 |
| vendor_phone | P11 | 3.9% | 75% | 17480 |
| vendor_emails | P11 | 3.0% | 70% | 16470 |
| buyer_tax_exempt_status | P10R | 0.0% | 15% | 15813 |
| buyer_esignature_preference | P10R | 0.0% | 15% | 15793 |
| buyer_payment_method_preference | P10R | 0.6% | 15% | 15162 |
| contract_value | P11 | 0.3% | 60% | 14663 |
| award_or_notice_id | P11 | 0.3% | 60% | 14662 |
| buyer_esignature_preference | P06T | 0.2% | 15% | 14110 |
| buyer_tax_exempt_status | P06T | 0.3% | 15% | 14035 |
| buyer_payment_method_preference | P06T | 0.6% | 15% | 13768 |
| buyer_phone | P11 | 24.1% | 75% | 12514 |
| commodity_codes | P11 | 0.2% | 50% | 12229 |
| vendor_registered_address | P08 | 29.1% | 70% | 10401 |
| solicitation_or_tender_number | P11 | 0.3% | 40% | 9753 |
| buyer_phone | P08 | 69.1% | 95% | 6596 |
| invoice_reference_hint | P08 | 1.3% | 25% | 6042 |
| buyer_legal_name_as_published | P11 | 41.0% | 65% | 5898 |
| vendor_bn9 | P08 | 28.1% | 50% | 5582 |
| buyer_phone | P13 | 63.0% | 95% | 5578 |
| vendor_emails | P08 | 54.9% | 75% | 5121 |
| buyer_ap_cycle_published | P08 | 0.1% | 20% | 5076 |
| buyer_legal_name_as_published | P08 | 55.4% | 75% | 4983 |
| buyer_ap_cycle_published | P11 | 0.0% | 20% | 4907 |
| ap_system_hint | P08 | 1.1% | 20% | 4814 |
| vendor_phone | P08 | 66.1% | 85% | 4798 |
| buyer_bn_as_published | P08 | 16.2% | 35% | 4792 |
| ap_system_hint | P11 | 0.8% | 20% | 4726 |
| buyer_logo_url | P11 | 61.1% | 80% | 4645 |
| buyer_esignature_preference | P08 | 0.5% | 15% | 3700 |
| buyer_tax_exempt_status | P08 | 0.5% | 15% | 3684 |
| buyer_payment_method_preference | P08 | 0.7% | 15% | 3646 |
| buyer_payment_method_preference | P11 | 0.4% | 15% | 3599 |
| buyer_address | P08 | 80.9% | 95% | 3589 |
| buyer_esignature_preference | P11 | 0.4% | 15% | 3589 |
| buyer_tax_exempt_status | P11 | 0.5% | 15% | 3554 |
| buyer_logo_url | P13 | 74.6% | 95% | 3553 |

## 1. identifiers

### `invoice_reference_hint`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 123 | 90.2% | 90.2% | +1.5 | 50% | ✅ met |
| P01T | 446 | 94.2% | 94.2% | +4.7 | 50% | ✅ met |
| P01_GOLD | 625 | 92.2% | 94.4% | +0.0 | 95% | 🟡 3 pts to go |
| P02 | 486 | 71.0% | 72.4% | -2.8 | 95% | ❌ 24 pts to go |
| P03 | 264 | 81.1% | 84.1% | -0.9 | 95% | ❌ 14 pts to go |
| P04 | 4132 | 27.4% | 28.8% | -5.4 | 90% | ❌ 63 pts to go |
| P05 | 420 | 38.8% | 41.7% | +0.2 | 70% | ❌ 31 pts to go |
| P06M | 13240 | 91.7% | 91.7% | -0.9 | n/a | no target |
| P06T | 95584 | 97.5% | 97.5% | +17.2 | n/a | no target |
| P06 | 297 | 33.3% | 33.3% | +1.6 | 30% | ✅ met |
| P07 | 788 | 7.1% | 7.1% | +0.2 | 30% | ❌ 23 pts to go |
| P08 | 25442 | 1.3% | 1.3% | +0.2 | 25% | ❌ 24 pts to go |
| P09 | 294 | 99.0% | 99.7% | +0.0 | 100% | 🟡 1 pts to go |
| P10R | 105619 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P10 | 2652 | 2.7% | 2.8% | +0.1 | 25% | ❌ 22 pts to go |
| P11 | 24579 | 97.1% | 97.1% | +83.5 | 60% | ✅ met |
| P12 | 7 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P13 | 17451 | 0.2% | 0.2% | +0.0 | 0% by design | — leave (by design) |

### `po_number_as_published`

> ceiling: a purchase-order number exists only where the buyer publishes PO-level data (Montréal, Laval, Toronto open data so far) or the record itself carries one; most sources publish awards, not POs — the target cannot be reached from public data for most buyers

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 123 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P01T | 446 | 0.0% | 0.0% | +0.0 | 10% | 🟡 10 pts to go |
| P01_GOLD | 625 | 6.1% | 6.1% | +0.0 | 50% | ❌ 44 pts to go |
| P02 | 486 | 6.0% | 6.0% | -0.2 | 50% | ❌ 44 pts to go |
| P03 | 264 | 1.5% | 1.5% | -0.1 | 40% | ❌ 38 pts to go |
| P04 | 4132 | 0.4% | 0.4% | -0.1 | 30% | ❌ 30 pts to go |
| P05 | 420 | 0.2% | 0.2% | +0.0 | 20% | ❌ 20 pts to go |
| P06M | 13240 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06T | 95584 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06 | 297 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P07 | 788 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P08 | 25442 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P09 | 294 | 0.7% | 0.7% | +0.0 | 50% | ❌ 49 pts to go |
| P10R | 105619 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P10 | 2652 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P11 | 24579 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P12 | 7 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P13 | 17451 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `contract_or_agreement_number`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 123 | 82.9% | 82.9% | +1.5 | n/a | no target |
| P01T | 446 | 80.5% | 80.5% | +10.0 | 50% | ✅ met |
| P01_GOLD | 625 | 66.9% | 66.9% | +0.0 | 85% | ❌ 18 pts to go |
| P02 | 486 | 62.1% | 62.1% | -2.8 | 90% | ❌ 28 pts to go |
| P03 | 264 | 59.5% | 59.5% | -1.8 | 85% | ❌ 26 pts to go |
| P04 | 4132 | 24.9% | 24.9% | -5.2 | 85% | ❌ 60 pts to go |
| P05 | 420 | 29.0% | 29.0% | +0.0 | 60% | ❌ 31 pts to go |
| P06M | 13240 | 91.4% | 91.4% | -1.0 | n/a | no target |
| P06T | 95584 | 97.4% | 97.4% | +17.4 | n/a | no target |
| P06 | 297 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P07 | 788 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P08 | 25442 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P09 | 294 | 95.9% | 95.9% | -0.1 | 100% | 🟡 4 pts to go |
| P10R | 105619 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P10 | 2652 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P11 | 24579 | 96.9% | 96.9% | +84.2 | 60% | ✅ met |
| P12 | 7 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P13 | 17451 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `solicitation_or_tender_number`

> ceiling: SEAO's 'numero' is the organisation's own reference for the notice (SEAO data dictionary) and is reported here; sources that publish awards under a tender number only (bids&tenders, SaskTenders, BC) also carry it as the contract reference, labelled

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 123 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P01T | 446 | 0.0% | 0.0% | +0.0 | 30% | ❌ 30 pts to go |
| P01_GOLD | 625 | 50.7% | 50.7% | +0.1 | 80% | ❌ 29 pts to go |
| P02 | 486 | 54.5% | 54.5% | -2.5 | 60% | 🟡 6 pts to go |
| P03 | 264 | 50.0% | 50.0% | -1.6 | 80% | ❌ 30 pts to go |
| P04 | 4132 | 20.6% | 20.6% | -4.4 | 50% | ❌ 29 pts to go |
| P05 | 420 | 11.7% | 11.7% | -0.2 | 40% | ❌ 28 pts to go |
| P06M | 13240 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06T | 95584 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06 | 297 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P07 | 788 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P08 | 25442 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P09 | 294 | 83.0% | 83.0% | -0.5 | 50% | ✅ met |
| P10R | 105619 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P10 | 2652 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P11 | 24579 | 0.3% | 0.3% | -0.5 | 40% | ❌ 40 pts to go |
| P12 | 7 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P13 | 17451 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `award_or_notice_id`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 123 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P01T | 446 | 0.2% | 0.2% | -0.1 | n/a | no target |
| P01_GOLD | 625 | 60.5% | 60.5% | +0.1 | 85% | ❌ 24 pts to go |
| P02 | 486 | 53.9% | 53.9% | -2.4 | 90% | ❌ 36 pts to go |
| P03 | 264 | 58.3% | 58.3% | -1.9 | 85% | ❌ 27 pts to go |
| P04 | 4132 | 21.3% | 21.3% | -4.5 | 85% | ❌ 64 pts to go |
| P05 | 420 | 20.0% | 20.0% | +0.1 | 50% | ❌ 30 pts to go |
| P06M | 13240 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06T | 95584 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06 | 297 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P07 | 788 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P08 | 25442 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P09 | 294 | 96.9% | 96.9% | -0.1 | 100% | 🟡 3 pts to go |
| P10R | 105619 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P10 | 2652 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P11 | 24579 | 0.3% | 0.3% | -0.6 | 60% | ❌ 60 pts to go |
| P12 | 7 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P13 | 17451 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `buyer_vendor_id`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 123 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P01T | 446 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P01_GOLD | 625 | 13.0% | 13.0% | +0.1 | 60% | ❌ 47 pts to go |
| P02 | 486 | 5.8% | 5.8% | -0.2 | 50% | ❌ 44 pts to go |
| P03 | 264 | 8.3% | 8.3% | -0.3 | 50% | ❌ 42 pts to go |
| P04 | 4132 | 1.6% | 1.6% | -0.4 | 40% | ❌ 38 pts to go |
| P05 | 420 | 0.7% | 0.7% | -0.2 | 20% | ❌ 19 pts to go |
| P06M | 13240 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06T | 95584 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06 | 297 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P07 | 788 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P08 | 25442 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P09 | 294 | 2.4% | 2.4% | +0.1 | 50% | ❌ 48 pts to go |
| P10R | 105619 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P10 | 2652 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P11 | 24579 | 0.1% | 0.1% | +0.0 | n/a | no target |
| P12 | 7 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P13 | 17451 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `commodity_codes`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 123 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P01T | 446 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P01_GOLD | 625 | 34.9% | 34.9% | +0.1 | 80% | ❌ 45 pts to go |
| P02 | 486 | 49.8% | 49.8% | -2.2 | 90% | ❌ 40 pts to go |
| P03 | 264 | 32.6% | 32.6% | -1.0 | 80% | ❌ 47 pts to go |
| P04 | 4132 | 19.5% | 19.5% | -4.1 | 85% | ❌ 66 pts to go |
| P05 | 420 | 5.5% | 5.5% | +0.1 | 50% | ❌ 44 pts to go |
| P06M | 13240 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06T | 95584 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06 | 297 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P07 | 788 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P08 | 25442 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P09 | 294 | 75.5% | 75.5% | -0.4 | 95% | ❌ 20 pts to go |
| P10R | 105619 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P10 | 2652 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P11 | 24579 | 0.2% | 0.2% | -0.4 | 50% | ❌ 50 pts to go |
| P12 | 7 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P13 | 17451 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `buyer_org_codes`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 123 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P01T | 446 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P01_GOLD | 625 | 8.5% | 8.5% | +0.0 | 50% | ❌ 42 pts to go |
| P02 | 486 | 6.0% | 6.0% | -0.2 | 50% | ❌ 44 pts to go |
| P03 | 264 | 1.9% | 1.9% | -0.1 | 30% | ❌ 28 pts to go |
| P04 | 4132 | 0.4% | 0.4% | -0.1 | 30% | ❌ 30 pts to go |
| P05 | 420 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06M | 13240 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06T | 95584 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06 | 297 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P07 | 788 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P08 | 25442 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P09 | 294 | 0.3% | 0.3% | +0.0 | n/a | no target |
| P10R | 105619 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P10 | 2652 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P11 | 24579 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P12 | 7 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P13 | 17451 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `records_with_this_vendor`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 123 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P01T | 446 | 100.0% | 100.0% | +0.0 | 60% | ✅ met |
| P01_GOLD | 625 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P02 | 486 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P03 | 264 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P04 | 4132 | 100.0% | 100.0% | +0.0 | 95% | ✅ met |
| P05 | 420 | 100.0% | 100.0% | +0.0 | 70% | ✅ met |
| P06M | 13240 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P06T | 95584 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P06 | 297 | 100.0% | 100.0% | +0.0 | 50% | ✅ met |
| P07 | 788 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P08 | 25442 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P09 | 294 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P10R | 105619 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P10 | 2652 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P11 | 24579 | 100.0% | 100.0% | +0.0 | 70% | ✅ met |
| P12 | 7 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P13 | 17451 | 0.0% | 0.0% | +0.0 | n/a | no target |

## 2. vendor

### `vendor_bn9`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 123 | 11.4% | 11.4% | -3.0 | 70% | ❌ 59 pts to go |
| P01T | 446 | 49.8% | 49.8% | +16.1 | 60% | ❌ 10 pts to go |
| P01_GOLD | 625 | 74.6% | 74.6% | +1.6 | 90% | ❌ 15 pts to go |
| P02 | 486 | 54.1% | 54.1% | -1.0 | 85% | ❌ 31 pts to go |
| P03 | 264 | 69.7% | 69.7% | -0.2 | 90% | ❌ 20 pts to go |
| P04 | 4132 | 36.8% | 36.8% | +4.3 | 75% | ❌ 38 pts to go |
| P05 | 420 | 54.5% | 54.5% | +4.6 | 50% | ✅ met |
| P06M | 13240 | 3.3% | 3.3% | +1.5 | n/a | no target |
| P06T | 95584 | 51.3% | 51.3% | +34.0 | n/a | no target |
| P06 | 297 | 41.4% | 41.4% | +18.6 | 40% | ✅ met |
| P07 | 788 | 30.7% | 30.7% | +14.3 | 50% | ❌ 19 pts to go |
| P08 | 25442 | 28.1% | 28.1% | +17.2 | 50% | ❌ 22 pts to go |
| P09 | 294 | 59.5% | 59.5% | +1.7 | 80% | ❌ 20 pts to go |
| P10R | 105619 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P10 | 2652 | 35.5% | 35.5% | +6.8 | 40% | 🟡 4 pts to go |
| P11 | 24579 | 96.5% | 96.5% | +5.4 | 60% | ✅ met |
| P12 | 7 | 42.9% | 42.9% | -19.6 | 85% | ❌ 42 pts to go |
| P13 | 17451 | 90.9% | 90.9% | -0.1 | 0% by design | — leave (by design) |

### `vendor_registered_address`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 123 | 58.5% | 58.5% | -8.5 | n/a | no target |
| P01T | 446 | 56.3% | 56.3% | +18.3 | n/a | no target |
| P01_GOLD | 625 | 72.3% | 72.3% | +1.9 | 95% | ❌ 23 pts to go |
| P02 | 486 | 73.3% | 73.3% | -0.5 | 95% | ❌ 22 pts to go |
| P03 | 264 | 72.0% | 72.0% | +0.1 | 95% | ❌ 23 pts to go |
| P04 | 4132 | 49.8% | 49.8% | +4.2 | 95% | ❌ 45 pts to go |
| P05 | 420 | 58.3% | 58.3% | +4.9 | 70% | ❌ 12 pts to go |
| P06M | 13240 | 46.5% | 46.5% | -8.1 | n/a | no target |
| P06T | 95584 | 67.2% | 67.2% | +36.9 | n/a | no target |
| P06 | 297 | 39.4% | 39.4% | +14.6 | 80% | ❌ 41 pts to go |
| P07 | 788 | 31.2% | 31.2% | +13.2 | 70% | ❌ 39 pts to go |
| P08 | 25442 | 29.1% | 29.1% | +15.0 | 70% | ❌ 41 pts to go |
| P09 | 294 | 87.8% | 87.8% | +0.3 | 100% | ❌ 12 pts to go |
| P10R | 105619 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P10 | 2652 | 37.3% | 37.3% | +4.8 | 70% | ❌ 33 pts to go |
| P11 | 24579 | 97.3% | 97.3% | +5.1 | 75% | ✅ met |
| P12 | 7 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P13 | 17451 | 15.8% | 15.8% | +15.8 | n/a | no target |

### `vendor_trading_name`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 123 | 16.3% | 16.3% | -0.2 | n/a | no target |
| P01T | 446 | 61.9% | 61.9% | +36.0 | n/a | no target |
| P01_GOLD | 625 | 49.9% | 49.9% | +2.0 | 60% | ❌ 10 pts to go |
| P02 | 486 | 54.9% | 54.9% | -0.4 | 60% | 🟡 5 pts to go |
| P03 | 264 | 54.9% | 54.9% | -0.2 | 60% | 🟡 5 pts to go |
| P04 | 4132 | 41.2% | 41.2% | +4.5 | 55% | ❌ 14 pts to go |
| P05 | 420 | 24.5% | 24.5% | +2.3 | 50% | ❌ 26 pts to go |
| P06M | 13240 | 7.0% | 7.0% | +3.4 | n/a | no target |
| P06T | 95584 | 67.2% | 67.2% | +40.2 | n/a | no target |
| P06 | 297 | 47.8% | 47.8% | +12.6 | n/a | no target |
| P07 | 788 | 41.6% | 41.6% | +8.4 | 55% | ❌ 13 pts to go |
| P08 | 25442 | 37.1% | 37.1% | +10.2 | 50% | ❌ 13 pts to go |
| P09 | 294 | 73.1% | 73.1% | +2.1 | 70% | ✅ met |
| P10R | 105619 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P10 | 2652 | 47.8% | 47.8% | +8.3 | 55% | 🟡 7 pts to go |
| P11 | 24579 | 97.4% | 97.4% | +5.4 | 50% | ✅ met |
| P12 | 7 | 100.0% | 100.0% | +12.5 | n/a | no target |
| P13 | 17451 | 74.6% | 74.6% | +74.6 | n/a | no target |

### `vendor_phone`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 123 | 49.6% | 49.6% | +35.2 | n/a | no target |
| P01T | 446 | 77.1% | 77.1% | +20.8 | n/a | no target |
| P01_GOLD | 625 | 49.9% | 49.9% | +2.0 | 70% | ❌ 20 pts to go |
| P02 | 486 | 58.0% | 58.0% | +4.0 | 70% | ❌ 12 pts to go |
| P03 | 264 | 51.1% | 51.1% | +1.5 | 70% | ❌ 19 pts to go |
| P04 | 4132 | 54.9% | 54.9% | +7.8 | 65% | ❌ 10 pts to go |
| P05 | 420 | 27.9% | 27.9% | -2.8 | 60% | ❌ 32 pts to go |
| P06M | 13240 | 37.1% | 37.1% | +33.6 | n/a | no target |
| P06T | 95584 | 68.8% | 68.8% | +5.0 | n/a | no target |
| P06 | 297 | 69.4% | 69.4% | +11.8 | 40% | ✅ met |
| P07 | 788 | 65.1% | 65.1% | +8.1 | 85% | ❌ 20 pts to go |
| P08 | 25442 | 66.1% | 66.1% | +9.2 | 85% | ❌ 19 pts to go |
| P09 | 294 | 60.5% | 60.5% | +7.0 | 85% | ❌ 24 pts to go |
| P10R | 105619 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P10 | 2652 | 64.4% | 64.4% | +3.4 | 85% | ❌ 21 pts to go |
| P11 | 24579 | 3.9% | 3.9% | -2.5 | 75% | ❌ 71 pts to go |
| P12 | 7 | 28.6% | 28.6% | +3.6 | n/a | no target |
| P13 | 17451 | 100.0% | 100.0% | +0.0 | 60% | ✅ met |

### `vendor_website`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 123 | 55.3% | 55.3% | +35.7 | n/a | no target |
| P01T | 446 | 98.4% | 98.4% | +2.0 | n/a | no target |
| P01_GOLD | 625 | 79.5% | 79.5% | -9.8 | 90% | ❌ 10 pts to go |
| P02 | 486 | 83.7% | 83.7% | -5.5 | 90% | 🟡 6 pts to go |
| P03 | 264 | 87.9% | 87.9% | -3.1 | 90% | 🟡 2 pts to go |
| P04 | 4132 | 84.9% | 84.9% | -5.3 | 85% | 🟡 0 pts to go |
| P05 | 420 | 44.0% | 44.0% | -8.2 | 70% | ❌ 26 pts to go |
| P06M | 13240 | 43.2% | 43.2% | +37.0 | n/a | no target |
| P06T | 95584 | 100.0% | 100.0% | +8.0 | n/a | no target |
| P06 | 297 | 99.3% | 99.3% | +1.0 | 50% | ✅ met |
| P07 | 788 | 99.7% | 99.7% | +0.6 | 100% | 🟡 0 pts to go |
| P08 | 25442 | 99.8% | 99.8% | +0.4 | 100% | 🟡 0 pts to go |
| P09 | 294 | 80.3% | 80.3% | +0.1 | 100% | ❌ 20 pts to go |
| P10R | 105619 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P10 | 2652 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P11 | 24579 | 99.8% | 99.8% | +0.1 | 100% | 🟡 0 pts to go |
| P12 | 7 | 28.6% | 28.6% | -8.9 | n/a | no target |
| P13 | 17451 | 100.0% | 100.0% | +0.0 | n/a | no target |

### `vendor_emails`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 123 | 14.6% | 14.6% | +0.2 | n/a | no target |
| P01T | 446 | 53.6% | 53.6% | +4.5 | n/a | no target |
| P01_GOLD | 625 | 43.5% | 43.5% | -1.7 | 70% | ❌ 26 pts to go |
| P02 | 486 | 48.8% | 48.8% | -0.7 | 75% | ❌ 26 pts to go |
| P03 | 264 | 43.2% | 43.2% | -1.3 | 75% | ❌ 32 pts to go |
| P04 | 4132 | 38.6% | 38.6% | +1.2 | 70% | ❌ 31 pts to go |
| P05 | 420 | 21.4% | 21.4% | -4.1 | 55% | ❌ 34 pts to go |
| P06M | 13240 | 4.6% | 4.6% | +1.3 | n/a | no target |
| P06T | 95584 | 39.4% | 39.4% | -0.2 | n/a | no target |
| P06 | 297 | 47.8% | 47.8% | +5.0 | n/a | no target |
| P07 | 788 | 50.3% | 50.3% | +4.4 | 70% | ❌ 20 pts to go |
| P08 | 25442 | 54.9% | 54.9% | +5.0 | 75% | ❌ 20 pts to go |
| P09 | 294 | 50.0% | 50.0% | +0.2 | 85% | ❌ 35 pts to go |
| P10R | 105619 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P10 | 2652 | 45.4% | 45.4% | +1.9 | 80% | ❌ 35 pts to go |
| P11 | 24579 | 3.0% | 3.0% | -2.0 | 70% | ❌ 67 pts to go |
| P12 | 7 | 14.3% | 14.3% | -10.7 | n/a | no target |
| P13 | 17451 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `vendor_logo_url`

> ceiling: needs the vendor's website first; sites that block automated readers (robots.txt / 403) are never read

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 123 | 55.3% | 55.3% | +41.9 | n/a | no target |
| P01T | 446 | 96.9% | 96.9% | +7.1 | n/a | no target |
| P01_GOLD | 625 | 73.8% | 73.8% | -3.7 | 90% | ❌ 16 pts to go |
| P02 | 486 | 79.0% | 79.0% | +1.4 | 90% | ❌ 11 pts to go |
| P03 | 264 | 83.3% | 83.3% | +0.1 | 90% | 🟡 7 pts to go |
| P04 | 4132 | 79.1% | 79.1% | +3.5 | 85% | 🟡 6 pts to go |
| P05 | 420 | 42.4% | 42.4% | -6.3 | 75% | ❌ 33 pts to go |
| P06M | 13240 | 43.0% | 43.0% | +38.9 | n/a | no target |
| P06T | 95584 | 97.8% | 97.8% | +14.6 | n/a | no target |
| P06 | 297 | 91.2% | 91.2% | +11.9 | n/a | no target |
| P07 | 788 | 92.1% | 92.1% | +10.5 | 100% | 🟡 8 pts to go |
| P08 | 25442 | 91.1% | 91.1% | +12.2 | 100% | 🟡 9 pts to go |
| P09 | 294 | 66.7% | 66.7% | +5.3 | n/a | no target |
| P10R | 105619 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P10 | 2652 | 88.6% | 88.6% | +4.4 | 100% | ❌ 11 pts to go |
| P11 | 24579 | 95.5% | 95.5% | +7.1 | n/a | no target |
| P12 | 7 | 28.6% | 28.6% | -8.9 | n/a | no target |
| P13 | 17451 | 84.2% | 84.2% | +1.0 | n/a | no target |

### `vendor_neq`

> ceiling: only Québec-registered vendors have an NEQ; the share of QC vendors is reported next to the rate

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 123 | 45.5% | 45.5% | -8.1 | n/a | no target · QC vendors: 46 rows, 100.0% filled |
| P01T | 446 | 25.3% | 25.3% | +7.5 | n/a | no target · QC vendors: 47 rows, 89.4% filled |
| P01_GOLD | 625 | 43.7% | 43.7% | +0.1 | 95% | ❌ 51 pts to go · QC vendors: 53 rows, 98.1% filled |
| P02 | 486 | 54.1% | 54.1% | -1.0 | 95% | ❌ 41 pts to go · QC vendors: 116 rows, 100.0% filled |
| P03 | 264 | 45.8% | 45.8% | -0.7 | 95% | ❌ 49 pts to go · QC vendors: 21 rows, 100.0% filled |
| P04 | 4132 | 30.3% | 30.3% | -1.6 | 95% | ❌ 65 pts to go · QC vendors: 669 rows, 97.2% filled |
| P05 | 420 | 14.0% | 14.0% | -0.8 | n/a | no target · QC vendors: 34 rows, 94.1% filled |
| P06M | 13240 | 43.3% | 43.3% | -10.0 | n/a | no target · QC vendors: 5070 rows, 99.9% filled |
| P06T | 95584 | 32.7% | 32.7% | +15.2 | n/a | no target · QC vendors: 17986 rows, 94.3% filled |
| P06 | 297 | 8.8% | 8.8% | +0.5 | n/a | no target · QC vendors: 19 rows, 73.7% filled |
| P07 | 788 | 6.6% | 6.6% | -0.2 | n/a | no target · QC vendors: 48 rows, 77.1% filled |
| P08 | 25442 | 8.0% | 8.0% | +1.5 | n/a | no target · QC vendors: 1854 rows, 92.7% filled |
| P09 | 294 | 77.9% | 77.9% | -0.3 | 95% | ❌ 17 pts to go · QC vendors: 106 rows, 100.0% filled |
| P10R | 105619 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P10 | 2652 | 17.6% | 17.6% | +0.0 | n/a | no target · QC vendors: 316 rows, 90.8% filled |
| P11 | 24579 | 91.0% | 91.0% | +9.5 | n/a | no target · QC vendors: 241 rows, 94.6% filled |
| P12 | 7 | 71.4% | 71.4% | +8.9 | n/a | no target · QC vendors: 1 rows, 100.0% filled |
| P13 | 17451 | 15.8% | 15.8% | +15.8 | n/a | no target · QC vendors: 2765 rows, 100.0% filled |

### `vendor_years_in_business`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 123 | 57.7% | 57.7% | -7.2 | n/a | no target · vendors with a registry record: 71 rows, 100.0% filled |
| P01T | 446 | 56.3% | 56.3% | +18.0 | n/a | no target · vendors with a registry record: 251 rows, 100.0% filled |
| P01_GOLD | 625 | 81.3% | 81.3% | +1.9 | 100% | ❌ 19 pts to go · vendors with a registry record: 508 rows, 100.0% filled |
| P02 | 486 | 77.0% | 77.0% | -0.4 | 100% | ❌ 23 pts to go · vendors with a registry record: 374 rows, 100.0% filled |
| P03 | 264 | 80.7% | 80.7% | -0.5 | 100% | ❌ 19 pts to go · vendors with a registry record: 213 rows, 100.0% filled |
| P04 | 4132 | 50.2% | 50.2% | +4.1 | 100% | ❌ 50 pts to go · vendors with a registry record: 2073 rows, 100.0% filled |
| P05 | 420 | 63.1% | 63.1% | +4.8 | n/a | no target · vendors with a registry record: 265 rows, 100.0% filled |
| P06M | 13240 | 46.3% | 46.3% | -8.0 | n/a | no target · vendors with a registry record: 6133 rows, 100.0% filled |
| P06T | 95584 | 67.3% | 67.3% | +36.9 | n/a | no target · vendors with a registry record: 64287 rows, 100.0% filled |
| P06 | 297 | 40.4% | 40.4% | +14.9 | n/a | no target · vendors with a registry record: 120 rows, 100.0% filled |
| P07 | 788 | 31.6% | 31.6% | +13.2 | n/a | no target · vendors with a registry record: 249 rows, 100.0% filled |
| P08 | 25442 | 29.4% | 29.4% | +15.1 | n/a | no target · vendors with a registry record: 7471 rows, 100.0% filled |
| P09 | 294 | 91.5% | 91.5% | +0.4 | n/a | no target · vendors with a registry record: 269 rows, 100.0% filled |
| P10R | 105619 | 100.0% | 100.0% | +0.0 | n/a | no target · vendors with a registry record: 105619 rows, 100.0% filled |
| P10 | 2652 | 37.9% | 37.9% | +4.7 | n/a | no target · vendors with a registry record: 1006 rows, 100.0% filled |
| P11 | 24579 | 97.3% | 97.3% | +5.0 | n/a | no target · vendors with a registry record: 23918 rows, 100.0% filled |
| P12 | 7 | 100.0% | 100.0% | +0.0 | n/a | no target · vendors with a registry record: 7 rows, 100.0% filled |
| P13 | 17451 | 15.8% | 15.8% | +15.8 | n/a | no target · vendors with a registry record: 2765 rows, 100.0% filled |

## 3. buyer

### `buyer_legal_name_as_published`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 123 | 94.3% | 94.3% | +5.6 | 90% | ✅ met |
| P01T | 446 | 68.8% | 68.8% | +12.5 | 90% | ❌ 21 pts to go |
| P01_GOLD | 625 | 87.5% | 87.5% | +3.8 | 95% | 🟡 8 pts to go |
| P02 | 486 | 87.2% | 87.2% | +2.0 | 95% | 🟡 8 pts to go |
| P03 | 264 | 84.1% | 84.1% | +5.2 | 85% | 🟡 1 pts to go |
| P04 | 4132 | 63.2% | 63.2% | +6.8 | 90% | ❌ 27 pts to go |
| P05 | 420 | 79.3% | 79.3% | +11.6 | 75% | ✅ met |
| P06M | 13240 | 92.0% | 92.1% | +4.9 | n/a | no target |
| P06T | 95584 | 42.2% | 42.2% | +13.2 | n/a | no target |
| P06 | 297 | 75.8% | 75.8% | +18.9 | 80% | 🟡 4 pts to go |
| P07 | 788 | 60.3% | 60.4% | +14.1 | 80% | ❌ 20 pts to go |
| P08 | 25442 | 55.4% | 55.4% | +16.9 | 75% | ❌ 20 pts to go |
| P09 | 294 | 77.2% | 77.2% | +0.0 | 95% | ❌ 18 pts to go |
| P10R | 105619 | 38.8% | 38.8% | +13.8 | n/a | no target |
| P10 | 2652 | 50.6% | 50.6% | +11.6 | 70% | ❌ 19 pts to go |
| P11 | 24579 | 41.0% | 41.0% | +31.4 | 65% | ❌ 24 pts to go |
| P12 | 7 | 85.7% | 85.7% | +10.7 | 80% | ✅ met |
| P13 | 17451 | 50.9% | 50.9% | +11.7 | 60% | 🟡 9 pts to go |

### `buyer_bn_as_published`

> ceiling: a buyer's BN is public only where the buyer prints it or a public dataset carries it (CRA charities, federal grants & contributions recipients, business registries for corporations); municipalities rarely publish theirs

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 123 | 27.6% | 27.6% | +8.0 | 50% | ❌ 22 pts to go |
| P01T | 446 | 18.4% | 18.4% | +5.1 | n/a | no target |
| P01_GOLD | 625 | 19.5% | 19.5% | -1.1 | 40% | ❌ 20 pts to go |
| P02 | 486 | 20.2% | 20.2% | +1.3 | 40% | ❌ 20 pts to go |
| P03 | 264 | 21.2% | 21.2% | -1.1 | 40% | ❌ 19 pts to go |
| P04 | 4132 | 16.3% | 16.3% | +0.0 | 40% | ❌ 24 pts to go |
| P05 | 420 | 17.6% | 17.6% | -2.1 | 25% | 🟡 7 pts to go |
| P06M | 13240 | 14.4% | 14.4% | +5.6 | n/a | no target |
| P06T | 95584 | 8.9% | 8.9% | +1.4 | n/a | no target |
| P06 | 297 | 15.8% | 15.8% | +3.0 | 35% | ❌ 19 pts to go |
| P07 | 788 | 15.4% | 15.4% | +3.9 | 35% | ❌ 20 pts to go |
| P08 | 25442 | 16.2% | 16.2% | +5.8 | 35% | ❌ 19 pts to go |
| P09 | 294 | 16.0% | 16.0% | -0.2 | n/a | no target |
| P10R | 105619 | 10.8% | 10.8% | +3.7 | n/a | no target |
| P10 | 2652 | 11.9% | 11.9% | +5.4 | 30% | ❌ 18 pts to go |
| P11 | 24579 | 2.5% | 2.5% | +1.3 | n/a | no target |
| P12 | 7 | 14.3% | 14.3% | +1.8 | n/a | no target |
| P13 | 17451 | 23.4% | 23.4% | +2.4 | 30% | 🟡 7 pts to go |

### `buyer_address`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 123 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P01T | 446 | 88.3% | 88.3% | -3.6 | 100% | ❌ 12 pts to go |
| P01_GOLD | 625 | 90.7% | 90.7% | +1.2 | 100% | 🟡 9 pts to go |
| P02 | 486 | 95.7% | 95.7% | +0.4 | 100% | 🟡 4 pts to go |
| P03 | 264 | 89.4% | 89.4% | -0.1 | 100% | ❌ 11 pts to go |
| P04 | 4132 | 75.5% | 75.5% | -0.4 | 100% | ❌ 24 pts to go |
| P05 | 420 | 89.3% | 89.3% | +1.9 | 100% | ❌ 11 pts to go |
| P06M | 13240 | 99.2% | 99.2% | +0.4 | n/a | no target |
| P06T | 95584 | 73.5% | 73.5% | -3.9 | n/a | no target |
| P06 | 297 | 81.8% | 81.8% | +0.8 | 95% | ❌ 13 pts to go |
| P07 | 788 | 83.6% | 83.6% | +0.0 | 95% | ❌ 11 pts to go |
| P08 | 25442 | 80.9% | 80.9% | +0.7 | 95% | ❌ 14 pts to go |
| P09 | 294 | 96.3% | 96.3% | +0.6 | 100% | 🟡 4 pts to go |
| P10R | 105619 | 61.9% | 61.9% | +3.1 | n/a | no target |
| P10 | 2652 | 66.2% | 66.3% | +1.1 | 95% | ❌ 29 pts to go |
| P11 | 24579 | 94.3% | 94.3% | +7.1 | 80% | ✅ met |
| P12 | 7 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P13 | 17451 | 77.6% | 77.6% | +2.4 | 95% | ❌ 17 pts to go |

### `buyer_phone`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 123 | 86.2% | 86.2% | +0.6 | n/a | no target |
| P01T | 446 | 71.3% | 71.3% | +7.7 | n/a | no target |
| P01_GOLD | 625 | 73.0% | 73.0% | +3.5 | 90% | ❌ 17 pts to go |
| P02 | 486 | 77.6% | 77.6% | +1.9 | 95% | ❌ 17 pts to go |
| P03 | 264 | 74.6% | 74.6% | +0.8 | 95% | ❌ 20 pts to go |
| P04 | 4132 | 68.7% | 68.7% | +2.1 | 95% | ❌ 26 pts to go |
| P05 | 420 | 73.3% | 73.3% | +2.8 | 90% | ❌ 17 pts to go |
| P06M | 13240 | 87.6% | 87.6% | +1.2 | n/a | no target |
| P06T | 95584 | 56.3% | 56.3% | +8.4 | n/a | no target |
| P06 | 297 | 70.4% | 70.4% | +7.3 | 95% | ❌ 25 pts to go |
| P07 | 788 | 66.5% | 66.5% | +11.5 | 90% | ❌ 24 pts to go |
| P08 | 25442 | 69.1% | 69.1% | +10.3 | 95% | ❌ 26 pts to go |
| P09 | 294 | 86.7% | 86.7% | +0.6 | 100% | ❌ 13 pts to go |
| P10R | 105619 | 58.3% | 58.3% | +13.2 | n/a | no target |
| P10 | 2652 | 60.1% | 60.1% | +3.6 | 95% | ❌ 35 pts to go |
| P11 | 24579 | 24.1% | 24.1% | +12.9 | 75% | ❌ 51 pts to go |
| P12 | 7 | 85.7% | 85.7% | +10.7 | n/a | no target |
| P13 | 17451 | 63.0% | 63.0% | +15.4 | 95% | ❌ 32 pts to go |

### `buyer_logo_url`

> ceiling: sites that block automated readers (robots.txt / 403) are never read; an og:image that looks like a photo is labelled

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 123 | 88.6% | 88.6% | +17.5 | n/a | no target |
| P01T | 446 | 85.9% | 85.9% | +11.8 | 95% | 🟡 9 pts to go |
| P01_GOLD | 625 | 84.8% | 84.8% | +4.1 | 90% | 🟡 5 pts to go |
| P02 | 486 | 90.9% | 90.9% | +5.1 | 95% | 🟡 4 pts to go |
| P03 | 264 | 85.6% | 85.6% | +1.6 | 95% | 🟡 9 pts to go |
| P04 | 4132 | 89.6% | 89.6% | +6.3 | 90% | 🟡 0 pts to go |
| P05 | 420 | 93.1% | 93.1% | +4.6 | 95% | 🟡 2 pts to go |
| P06M | 13240 | 94.4% | 94.4% | +27.7 | n/a | no target |
| P06T | 95584 | 76.2% | 76.2% | +14.7 | n/a | no target |
| P06 | 297 | 92.9% | 92.9% | +10.8 | 100% | 🟡 7 pts to go |
| P07 | 788 | 92.6% | 92.6% | +15.4 | 100% | 🟡 7 pts to go |
| P08 | 25442 | 92.8% | 92.8% | +15.7 | 100% | 🟡 7 pts to go |
| P09 | 294 | 73.5% | 73.5% | +4.9 | n/a | no target |
| P10R | 105619 | 81.4% | 81.4% | +21.4 | n/a | no target |
| P10 | 2652 | 92.0% | 92.0% | +5.2 | 100% | 🟡 8 pts to go |
| P11 | 24579 | 61.1% | 61.1% | +42.3 | 80% | ❌ 19 pts to go |
| P12 | 7 | 100.0% | 100.0% | +25.0 | n/a | no target |
| P13 | 17451 | 74.6% | 74.6% | +23.6 | 95% | ❌ 20 pts to go |

## 4. AP

### `ap_contact_name_as_published`

> ceiling: owner 2026-11-08: the AP contact person the organisation itself names on its AP / finance page is allowed (name + role phrase, quoted); mailboxes stay organisational; many bodies publish no AP person

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 123 | 2.4% | 2.4% | -1.7 | n/a | no target |
| P01T | 446 | 7.4% | 7.4% | -1.0 | n/a | no target |
| P01_GOLD | 625 | 14.2% | 14.2% | +0.0 | 25% | ❌ 11 pts to go |
| P02 | 486 | 23.5% | 23.5% | -1.0 | 40% | ❌ 16 pts to go |
| P03 | 264 | 9.1% | 9.1% | +0.1 | 20% | ❌ 11 pts to go |
| P04 | 4132 | 3.0% | 3.0% | -0.6 | 20% | ❌ 17 pts to go |
| P05 | 420 | 3.3% | 3.3% | +0.0 | 15% | ❌ 12 pts to go |
| P06M | 13240 | 0.3% | 0.3% | +0.0 | n/a | no target |
| P06T | 95584 | 0.3% | 0.3% | -0.1 | n/a | no target |
| P06 | 297 | 5.7% | 5.7% | -0.5 | n/a | no target |
| P07 | 788 | 7.6% | 7.6% | +0.3 | n/a | no target |
| P08 | 25442 | 0.3% | 0.3% | +0.0 | n/a | no target |
| P09 | 294 | 7.8% | 7.8% | +0.2 | n/a | no target |
| P10R | 105619 | 0.2% | 0.2% | +0.0 | n/a | no target |
| P10 | 2652 | 0.9% | 0.9% | -0.1 | n/a | no target |
| P11 | 24579 | 0.1% | 0.1% | -0.1 | n/a | no target |
| P12 | 7 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P13 | 17451 | 0.4% | 0.4% | +0.0 | n/a | no target |

### `ap_phone`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 123 | 19.5% | 19.5% | -7.3 | n/a | no target |
| P01T | 446 | 21.1% | 21.1% | -3.0 | 70% | ❌ 49 pts to go |
| P01_GOLD | 625 | 43.4% | 43.4% | +0.1 | 80% | ❌ 37 pts to go |
| P02 | 486 | 56.0% | 56.0% | -0.8 | 90% | ❌ 34 pts to go |
| P03 | 264 | 18.6% | 18.6% | -0.5 | 60% | ❌ 41 pts to go |
| P04 | 4132 | 19.6% | 19.6% | -4.1 | 85% | ❌ 65 pts to go |
| P05 | 420 | 11.9% | 11.9% | +0.0 | 50% | ❌ 38 pts to go |
| P06M | 13240 | 0.7% | 0.7% | +0.3 | n/a | no target |
| P06T | 95584 | 0.6% | 0.6% | +0.0 | n/a | no target |
| P06 | 297 | 16.2% | 16.2% | +0.0 | n/a | no target |
| P07 | 788 | 10.9% | 10.9% | -2.1 | n/a | no target |
| P08 | 25442 | 0.6% | 0.6% | +0.1 | n/a | no target |
| P09 | 294 | 77.2% | 77.2% | -0.4 | 95% | ❌ 18 pts to go |
| P10R | 105619 | 0.2% | 0.2% | +0.0 | n/a | no target |
| P10 | 2652 | 1.7% | 1.7% | +0.0 | n/a | no target |
| P11 | 24579 | 1.8% | 1.8% | -1.8 | n/a | no target |
| P12 | 7 | 28.6% | 28.6% | +3.6 | n/a | no target |
| P13 | 17451 | 0.7% | 0.7% | +0.0 | n/a | no target |

### `invoice_mailing_address`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 123 | 7.3% | 7.3% | +0.1 | n/a | no target |
| P01T | 446 | 10.8% | 10.8% | -1.2 | n/a | no target |
| P01_GOLD | 625 | 33.9% | 33.9% | +0.0 | 70% | ❌ 36 pts to go |
| P02 | 486 | 37.9% | 37.9% | -1.0 | 75% | ❌ 37 pts to go |
| P03 | 264 | 18.6% | 18.6% | -0.5 | 55% | ❌ 36 pts to go |
| P04 | 4132 | 19.5% | 19.5% | -4.1 | 75% | ❌ 56 pts to go |
| P05 | 420 | 10.7% | 10.7% | -0.1 | 50% | ❌ 39 pts to go |
| P06M | 13240 | 0.2% | 0.2% | +0.0 | n/a | no target |
| P06T | 95584 | 0.3% | 0.3% | -0.1 | n/a | no target |
| P06 | 297 | 7.7% | 7.7% | -0.6 | n/a | no target |
| P07 | 788 | 5.2% | 5.2% | -1.2 | n/a | no target |
| P08 | 25442 | 0.2% | 0.2% | +0.0 | n/a | no target |
| P09 | 294 | 74.8% | 74.8% | -0.4 | 95% | ❌ 20 pts to go |
| P10R | 105619 | 0.1% | 0.1% | -0.1 | n/a | no target |
| P10 | 2652 | 1.0% | 1.0% | +0.0 | n/a | no target |
| P11 | 24579 | 1.6% | 1.6% | -2.0 | n/a | no target |
| P12 | 7 | 14.3% | 14.3% | +1.8 | n/a | no target |
| P13 | 17451 | 0.4% | 0.4% | +0.0 | n/a | no target |

### `invoicing_requirements`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 123 | 8.9% | 8.9% | +2.7 | n/a | no target |
| P01T | 446 | 7.8% | 7.8% | -1.5 | n/a | no target |
| P01_GOLD | 625 | 57.9% | 58.1% | -0.1 | 80% | ❌ 22 pts to go |
| P02 | 486 | 43.8% | 44.0% | -2.0 | 75% | ❌ 31 pts to go |
| P03 | 264 | 37.1% | 37.1% | -0.8 | 70% | ❌ 33 pts to go |
| P04 | 4132 | 19.2% | 19.6% | -3.9 | 70% | ❌ 51 pts to go |
| P05 | 420 | 14.5% | 14.5% | +0.2 | 50% | ❌ 36 pts to go |
| P06M | 13240 | 0.4% | 0.4% | +0.0 | n/a | no target |
| P06T | 95584 | 0.2% | 0.2% | -0.1 | n/a | no target |
| P06 | 297 | 15.2% | 15.2% | +1.8 | n/a | no target |
| P07 | 788 | 1.9% | 1.9% | -0.1 | n/a | no target |
| P08 | 25442 | 0.4% | 0.4% | +0.0 | n/a | no target |
| P09 | 294 | 45.9% | 46.3% | +0.0 | 80% | ❌ 34 pts to go |
| P10R | 105619 | 0.1% | 0.1% | +0.0 | n/a | no target |
| P10 | 2652 | 1.2% | 1.2% | +0.0 | n/a | no target |
| P11 | 24579 | 0.5% | 0.5% | -0.6 | n/a | no target |
| P12 | 7 | 42.9% | 42.9% | +5.4 | n/a | no target |
| P13 | 17451 | 0.3% | 0.3% | +0.0 | n/a | no target |

### `payment_terms_as_published`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 123 | 18.7% | 18.7% | +7.4 | n/a | no target |
| P01T | 446 | 17.7% | 17.7% | -4.3 | 60% | ❌ 42 pts to go |
| P01_GOLD | 625 | 63.5% | 63.5% | -0.1 | 70% | 🟡 6 pts to go |
| P02 | 486 | 38.3% | 38.3% | -0.6 | 50% | ❌ 12 pts to go |
| P03 | 264 | 48.5% | 48.5% | -1.5 | 55% | 🟡 6 pts to go |
| P04 | 4132 | 12.0% | 12.0% | -1.3 | 40% | ❌ 28 pts to go |
| P05 | 420 | 17.4% | 17.4% | +0.1 | 40% | ❌ 23 pts to go |
| P06M | 13240 | 2.3% | 2.3% | +1.6 | n/a | no target |
| P06T | 95584 | 2.8% | 2.8% | +0.4 | n/a | no target |
| P06 | 297 | 21.2% | 21.2% | +1.5 | n/a | no target |
| P07 | 788 | 7.0% | 7.0% | +0.3 | n/a | no target |
| P08 | 25442 | 2.9% | 2.9% | +0.3 | n/a | no target |
| P09 | 294 | 5.8% | 5.8% | -0.1 | n/a | no target |
| P10R | 105619 | 0.2% | 0.2% | +0.0 | n/a | no target |
| P10 | 2652 | 4.6% | 4.6% | +0.1 | n/a | no target |
| P11 | 24579 | 10.1% | 10.1% | +5.8 | n/a | no target |
| P12 | 7 | 0.0% | 0.0% | -12.5 | n/a | no target |
| P13 | 17451 | 0.2% | 0.2% | +0.0 | n/a | no target |

### `po_required_as_published`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 123 | 22.8% | 22.8% | +6.3 | n/a | no target |
| P01T | 446 | 23.3% | 23.3% | -2.0 | 65% | ❌ 42 pts to go |
| P01_GOLD | 625 | 69.0% | 69.0% | +0.0 | 70% | 🟡 1 pts to go |
| P02 | 486 | 23.3% | 23.3% | -0.6 | 50% | ❌ 27 pts to go |
| P03 | 264 | 52.3% | 52.3% | +0.0 | 60% | 🟡 8 pts to go |
| P04 | 4132 | 5.0% | 5.0% | -0.8 | 40% | ❌ 35 pts to go |
| P05 | 420 | 19.8% | 19.8% | +0.1 | 45% | ❌ 25 pts to go |
| P06M | 13240 | 1.5% | 1.5% | +1.2 | n/a | no target |
| P06T | 95584 | 0.7% | 0.7% | +0.1 | n/a | no target |
| P06 | 297 | 33.3% | 33.3% | +1.6 | n/a | no target |
| P07 | 788 | 7.1% | 7.1% | +0.2 | n/a | no target |
| P08 | 25442 | 1.3% | 1.3% | +0.2 | n/a | no target |
| P09 | 294 | 9.9% | 9.9% | +0.0 | n/a | no target |
| P10R | 105619 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P10 | 2652 | 2.7% | 2.7% | +0.1 | n/a | no target |
| P11 | 24579 | 1.0% | 1.0% | +0.0 | n/a | no target |
| P12 | 7 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P13 | 17451 | 0.2% | 0.2% | +0.0 | n/a | no target |

### `invoice_portal_url`

> ceiling: only portals the buyer names on its own pages; informational tax-authority links are not portals

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 123 | 13.8% | 13.8% | +7.6 | n/a | no target |
| P01T | 446 | 12.8% | 12.8% | -1.7 | n/a | no target |
| P01_GOLD | 625 | 49.8% | 49.8% | +0.0 | 50% | 🟡 0 pts to go |
| P02 | 486 | 36.0% | 36.0% | -1.4 | n/a | no target |
| P03 | 264 | 51.9% | 51.9% | -1.2 | 60% | 🟡 8 pts to go |
| P04 | 4132 | 10.7% | 10.7% | -2.2 | n/a | no target |
| P05 | 420 | 15.0% | 15.0% | -0.2 | n/a | no target |
| P06M | 13240 | 0.6% | 0.6% | +0.3 | n/a | no target |
| P06T | 95584 | 0.4% | 0.4% | -0.1 | n/a | no target |
| P06 | 297 | 24.2% | 24.2% | +2.5 | n/a | no target |
| P07 | 788 | 7.5% | 7.5% | +0.3 | n/a | no target |
| P08 | 25442 | 0.6% | 0.6% | +0.1 | n/a | no target |
| P09 | 294 | 18.4% | 18.4% | +0.2 | n/a | no target |
| P10R | 105619 | 0.1% | 0.1% | +0.0 | n/a | no target |
| P10 | 2652 | 2.4% | 2.4% | +0.1 | n/a | no target |
| P11 | 24579 | 0.7% | 0.7% | -0.1 | n/a | no target |
| P12 | 7 | 14.3% | 14.3% | +14.3 | n/a | no target |
| P13 | 17451 | 0.4% | 0.4% | +0.0 | n/a | no target |

### `buyer_payment_method_preference`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 123 | 12.2% | 12.2% | +0.9 | 15% | 🟡 3 pts to go |
| P01T | 446 | 9.6% | 9.6% | -1.5 | 15% | 🟡 5 pts to go |
| P01_GOLD | 625 | 35.4% | 35.4% | +0.1 | 40% | 🟡 5 pts to go |
| P02 | 486 | 12.8% | 13.0% | +0.3 | 25% | ❌ 12 pts to go |
| P03 | 264 | 17.4% | 17.4% | -0.6 | 25% | 🟡 8 pts to go |
| P04 | 4132 | 2.5% | 2.5% | -0.3 | 15% | ❌ 12 pts to go |
| P05 | 420 | 6.7% | 6.7% | -0.1 | 15% | 🟡 8 pts to go |
| P06M | 13240 | 0.9% | 0.9% | +0.3 | 15% | ❌ 14 pts to go |
| P06T | 95584 | 0.6% | 0.6% | +0.2 | 15% | ❌ 14 pts to go |
| P06 | 297 | 10.1% | 10.1% | +0.8 | 15% | 🟡 5 pts to go |
| P07 | 788 | 4.2% | 4.2% | +1.0 | 15% | ❌ 11 pts to go |
| P08 | 25442 | 0.7% | 0.7% | +0.3 | 15% | ❌ 14 pts to go |
| P09 | 294 | 1.0% | 1.0% | +0.0 | 15% | ❌ 14 pts to go |
| P10R | 105619 | 0.6% | 0.6% | +0.2 | 15% | ❌ 14 pts to go |
| P10 | 2652 | 1.2% | 1.2% | +0.2 | 15% | ❌ 14 pts to go |
| P11 | 24579 | 0.4% | 0.4% | +0.2 | 15% | ❌ 15 pts to go |
| P12 | 7 | 14.3% | 14.3% | +1.8 | 15% | 🟡 1 pts to go |
| P13 | 17451 | 0.6% | 0.6% | +0.2 | 15% | ❌ 14 pts to go |

### `buyer_tax_exempt_status`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 123 | 5.7% | 5.7% | -0.5 | 15% | 🟡 9 pts to go |
| P01T | 446 | 9.2% | 9.2% | -2.8 | 25% | ❌ 16 pts to go |
| P01_GOLD | 625 | 29.1% | 29.1% | -0.1 | 25% | ✅ met |
| P02 | 486 | 24.3% | 24.3% | -1.1 | 15% | ✅ met |
| P03 | 264 | 22.0% | 22.0% | +0.5 | 15% | ✅ met |
| P04 | 4132 | 3.7% | 3.7% | -0.4 | 15% | ❌ 11 pts to go |
| P05 | 420 | 11.2% | 11.2% | +0.4 | 15% | 🟡 4 pts to go |
| P06M | 13240 | 0.5% | 0.5% | +0.3 | 15% | ❌ 14 pts to go |
| P06T | 95584 | 0.3% | 0.3% | +0.0 | 15% | ❌ 15 pts to go |
| P06 | 297 | 8.1% | 8.1% | +0.5 | 15% | 🟡 7 pts to go |
| P07 | 788 | 2.7% | 2.7% | -0.4 | 15% | ❌ 12 pts to go |
| P08 | 25442 | 0.5% | 0.5% | +0.1 | 15% | ❌ 14 pts to go |
| P09 | 294 | 1.0% | 1.0% | +0.0 | 15% | ❌ 14 pts to go |
| P10R | 105619 | 0.0% | 0.0% | +0.0 | 15% | ❌ 15 pts to go |
| P10 | 2652 | 1.5% | 1.5% | -0.1 | 15% | ❌ 14 pts to go |
| P11 | 24579 | 0.5% | 0.5% | +0.0 | 15% | ❌ 14 pts to go |
| P12 | 7 | 28.6% | 28.6% | +3.6 | 15% | ✅ met |
| P13 | 17451 | 0.1% | 0.1% | +0.1 | 15% | ❌ 15 pts to go |

### `buyer_ap_cycle_published`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 123 | 1.6% | 1.6% | +1.6 | 20% | ❌ 18 pts to go |
| P01T | 446 | 2.9% | 2.9% | -1.0 | 20% | ❌ 17 pts to go |
| P01_GOLD | 625 | 4.5% | 4.5% | +0.2 | 20% | ❌ 16 pts to go |
| P02 | 486 | 1.4% | 1.4% | +0.1 | 20% | ❌ 19 pts to go |
| P03 | 264 | 1.5% | 1.5% | -0.1 | 20% | ❌ 18 pts to go |
| P04 | 4132 | 0.5% | 0.5% | -0.1 | 20% | ❌ 20 pts to go |
| P05 | 420 | 1.2% | 1.2% | +0.0 | 20% | ❌ 19 pts to go |
| P06M | 13240 | 0.1% | 0.1% | +0.1 | 20% | ❌ 20 pts to go |
| P06T | 95584 | 0.0% | 0.0% | +0.0 | 20% | ❌ 20 pts to go |
| P06 | 297 | 1.3% | 1.3% | -0.1 | 20% | ❌ 19 pts to go |
| P07 | 788 | 0.4% | 0.4% | +0.0 | 20% | ❌ 20 pts to go |
| P08 | 25442 | 0.1% | 0.1% | +0.1 | 20% | ❌ 20 pts to go |
| P09 | 294 | 0.0% | 0.0% | +0.0 | 20% | ❌ 20 pts to go |
| P10R | 105619 | 0.0% | 0.0% | +0.0 | 20% | ❌ 20 pts to go |
| P10 | 2652 | 0.3% | 0.3% | +0.0 | 20% | ❌ 20 pts to go |
| P11 | 24579 | 0.0% | 0.0% | +0.0 | 20% | ❌ 20 pts to go |
| P12 | 7 | 0.0% | 0.0% | +0.0 | 20% | ❌ 20 pts to go |
| P13 | 17451 | 0.0% | 0.0% | +0.0 | 20% | ❌ 20 pts to go |

### `buyer_esignature_preference`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 123 | 1.6% | 1.6% | +0.6 | 15% | ❌ 13 pts to go |
| P01T | 446 | 2.9% | 2.9% | +0.5 | 15% | ❌ 12 pts to go |
| P01_GOLD | 625 | 10.4% | 10.4% | -0.1 | 15% | 🟡 5 pts to go |
| P02 | 486 | 11.5% | 11.5% | -0.5 | 15% | 🟡 4 pts to go |
| P03 | 264 | 20.1% | 20.1% | -0.6 | 15% | ✅ met |
| P04 | 4132 | 2.2% | 2.2% | -0.2 | 15% | ❌ 13 pts to go |
| P05 | 420 | 2.9% | 2.9% | -0.1 | 15% | ❌ 12 pts to go |
| P06M | 13240 | 0.4% | 0.4% | +0.2 | 15% | ❌ 15 pts to go |
| P06T | 95584 | 0.2% | 0.2% | +0.0 | 15% | ❌ 15 pts to go |
| P06 | 297 | 5.4% | 5.4% | +0.2 | 15% | 🟡 10 pts to go |
| P07 | 788 | 1.8% | 1.8% | +0.1 | 15% | ❌ 13 pts to go |
| P08 | 25442 | 0.5% | 0.5% | +0.1 | 15% | ❌ 14 pts to go |
| P09 | 294 | 0.7% | 0.7% | +0.0 | 15% | ❌ 14 pts to go |
| P10R | 105619 | 0.0% | 0.0% | +0.0 | 15% | ❌ 15 pts to go |
| P10 | 2652 | 0.9% | 0.9% | +0.0 | 15% | ❌ 14 pts to go |
| P11 | 24579 | 0.4% | 0.4% | +0.1 | 15% | ❌ 15 pts to go |
| P12 | 7 | 0.0% | 0.0% | +0.0 | 15% | ❌ 15 pts to go |
| P13 | 17451 | 0.1% | 0.1% | +0.0 | 15% | ❌ 15 pts to go |

### `ap_system_hint`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 123 | 15.4% | 15.4% | +8.2 | 20% | 🟡 5 pts to go |
| P01T | 446 | 13.5% | 13.5% | -1.6 | 40% | ❌ 26 pts to go |
| P01_GOLD | 625 | 46.1% | 46.1% | +0.3 | 40% | ✅ met |
| P02 | 486 | 41.4% | 41.4% | -1.4 | 20% | ✅ met |
| P03 | 264 | 48.9% | 48.9% | +0.1 | 35% | ✅ met |
| P04 | 4132 | 12.9% | 12.9% | -2.5 | 20% | 🟡 7 pts to go |
| P05 | 420 | 15.2% | 15.2% | +0.4 | 20% | 🟡 5 pts to go |
| P06M | 13240 | 0.9% | 0.9% | +0.4 | 20% | ❌ 19 pts to go |
| P06T | 95584 | 0.7% | 0.7% | +0.0 | 20% | ❌ 19 pts to go |
| P06 | 297 | 24.2% | 24.2% | +2.1 | 20% | ✅ met |
| P07 | 788 | 7.9% | 7.9% | +0.8 | 20% | ❌ 12 pts to go |
| P08 | 25442 | 1.1% | 1.1% | +0.2 | 20% | ❌ 19 pts to go |
| P09 | 294 | 19.0% | 19.0% | +0.8 | 20% | 🟡 1 pts to go |
| P10R | 105619 | 0.2% | 0.2% | +0.0 | 20% | ❌ 20 pts to go |
| P10 | 2652 | 3.6% | 3.6% | +0.2 | 20% | ❌ 16 pts to go |
| P11 | 24579 | 0.8% | 0.8% | -0.2 | 20% | ❌ 19 pts to go |
| P12 | 7 | 0.0% | 0.0% | +0.0 | 20% | ❌ 20 pts to go |
| P13 | 17451 | 0.6% | 0.6% | +0.1 | 20% | ❌ 19 pts to go |

## 5. contract

### `contract_value`

> ceiling: rows proven by a lobbying filing, a news release, an auditor appointment, a customer story or a vendor's client list have no contract value by nature (≈17 % of P01 Gold); bids&tenders awards now carry the awarded bidder's submitted price when no award value was published

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 123 | 33.3% | 33.3% | -11.0 | n/a | no target |
| P01T | 446 | 0.2% | 0.2% | -0.1 | n/a | no target |
| P01_GOLD | 625 | 69.4% | 69.4% | -0.1 | 95% | ❌ 26 pts to go |
| P02 | 486 | 60.3% | 60.3% | -2.7 | 95% | ❌ 35 pts to go |
| P03 | 264 | 53.0% | 53.0% | -1.7 | 90% | ❌ 37 pts to go |
| P04 | 4132 | 22.4% | 22.4% | -4.7 | 85% | ❌ 63 pts to go |
| P05 | 420 | 37.6% | 37.6% | +1.1 | 75% | ❌ 37 pts to go |
| P06M | 13240 | 36.1% | 36.1% | -14.0 | n/a | no target |
| P06T | 95584 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06 | 297 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P07 | 788 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P08 | 25442 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P09 | 294 | 89.5% | 89.5% | +0.1 | 100% | ❌ 10 pts to go |
| P10R | 105619 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P10 | 2652 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P11 | 24579 | 0.3% | 0.3% | -0.6 | 60% | ❌ 60 pts to go |
| P12 | 7 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P13 | 17451 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `currency`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 123 | 33.3% | 33.3% | -11.0 | n/a | no target |
| P01T | 446 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P01_GOLD | 625 | 72.8% | 72.8% | +0.0 | 100% | ❌ 27 pts to go |
| P02 | 486 | 63.6% | 63.6% | -2.9 | 100% | ❌ 36 pts to go |
| P03 | 264 | 58.7% | 58.7% | -1.8 | n/a | no target |
| P04 | 4132 | 23.0% | 23.0% | -4.8 | 95% | ❌ 72 pts to go |
| P05 | 420 | 33.6% | 33.6% | +0.6 | 80% | ❌ 46 pts to go |
| P06M | 13240 | 36.1% | 36.1% | -14.0 | n/a | no target |
| P06T | 95584 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06 | 297 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P07 | 788 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P08 | 25442 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P09 | 294 | 92.5% | 92.5% | -0.2 | 100% | 🟡 8 pts to go |
| P10R | 105619 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P10 | 2652 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P11 | 24579 | 0.4% | 0.4% | -0.6 | n/a | no target |
| P12 | 7 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P13 | 17451 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `start_date`

> ceiling: most award notices publish an award date, not a start date; start_date carries the signature date when the source gives one, labelled

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 123 | 81.3% | 81.3% | +2.9 | n/a | no target |
| P01T | 446 | 0.2% | 0.2% | -0.1 | n/a | no target |
| P01_GOLD | 625 | 51.7% | 51.7% | +0.1 | 85% | ❌ 33 pts to go |
| P02 | 486 | 55.1% | 55.1% | -2.5 | 90% | ❌ 35 pts to go |
| P03 | 264 | 42.4% | 42.4% | -1.7 | 85% | ❌ 43 pts to go |
| P04 | 4132 | 25.1% | 25.1% | -5.3 | 90% | ❌ 65 pts to go |
| P05 | 420 | 32.9% | 32.9% | +0.1 | 75% | ❌ 42 pts to go |
| P06M | 13240 | 89.9% | 89.9% | -0.5 | n/a | no target |
| P06T | 95584 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06 | 297 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P07 | 788 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P08 | 25442 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P09 | 294 | 85.0% | 85.0% | -0.1 | 95% | 🟡 10 pts to go |
| P10R | 105619 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P10 | 2652 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P11 | 24579 | 0.3% | 0.3% | -0.5 | n/a | no target |
| P12 | 7 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P13 | 17451 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `end_date`

> ceiling: an inferred end (award date + published duration) is labelled as such; sources without a duration leave end_date empty — the honest ceiling. P09 is BY DEFINITION the rows whose end date is not published (older SEAO contracts with no closing notice): its end_date / duration targets cannot be met without inventing a date

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 123 | 80.5% | 80.5% | +1.1 | n/a | no target |
| P01T | 446 | 0.2% | 0.2% | -0.1 | n/a | no target |
| P01_GOLD | 625 | 51.8% | 51.8% | +0.0 | 85% | ❌ 33 pts to go |
| P02 | 486 | 50.4% | 50.4% | -2.3 | 90% | ❌ 40 pts to go |
| P03 | 264 | 43.6% | 43.6% | -1.7 | 85% | ❌ 41 pts to go |
| P04 | 4132 | 21.5% | 21.5% | -4.5 | 90% | ❌ 68 pts to go |
| P05 | 420 | 43.6% | 43.6% | +0.7 | 75% | ❌ 31 pts to go |
| P06M | 13240 | 80.7% | 80.7% | -3.0 | n/a | no target |
| P06T | 95584 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06 | 297 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P07 | 788 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P08 | 25442 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P09 | 294 | 0.3% | 0.3% | +0.0 | 95% | ❌ 95 pts to go |
| P10R | 105619 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P10 | 2652 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P11 | 24579 | 0.3% | 0.3% | -0.4 | n/a | no target |
| P12 | 7 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P13 | 17451 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `contract_title`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 123 | 90.2% | 90.2% | +4.6 | n/a | no target |
| P01T | 446 | 92.2% | 92.2% | +0.0 | n/a | no target |
| P01_GOLD | 625 | 85.4% | 85.4% | -0.1 | 100% | ❌ 15 pts to go |
| P02 | 486 | 75.3% | 75.3% | -0.4 | 100% | ❌ 25 pts to go |
| P03 | 264 | 91.3% | 91.3% | -0.9 | n/a | no target |
| P04 | 4132 | 48.8% | 48.8% | -2.7 | 95% | ❌ 46 pts to go |
| P05 | 420 | 77.9% | 77.9% | +0.1 | 95% | ❌ 17 pts to go |
| P06M | 13240 | 98.9% | 98.9% | +0.6 | n/a | no target |
| P06T | 95584 | 81.3% | 81.3% | -2.4 | n/a | no target |
| P06 | 297 | 24.6% | 24.6% | -1.6 | n/a | no target |
| P07 | 788 | 15.0% | 15.0% | -4.1 | n/a | no target |
| P08 | 25442 | 9.0% | 9.0% | -2.0 | n/a | no target |
| P09 | 294 | 98.6% | 98.6% | -0.1 | 100% | 🟡 1 pts to go |
| P10R | 105619 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P10 | 2652 | 71.3% | 71.3% | -0.4 | n/a | no target |
| P11 | 24579 | 8.5% | 8.5% | -7.6 | n/a | no target |
| P12 | 7 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P13 | 17451 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `contract_description`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 123 | 90.2% | 90.2% | +4.6 | n/a | no target |
| P01T | 446 | 92.2% | 92.2% | +0.0 | n/a | no target |
| P01_GOLD | 625 | 88.6% | 88.6% | -0.1 | 100% | ❌ 11 pts to go |
| P02 | 486 | 76.3% | 76.5% | -0.5 | 100% | ❌ 24 pts to go |
| P03 | 264 | 92.0% | 92.0% | -1.0 | n/a | no target |
| P04 | 4132 | 51.7% | 51.7% | -3.4 | 95% | ❌ 43 pts to go |
| P05 | 420 | 90.0% | 90.0% | -0.2 | 70% | ✅ met |
| P06M | 13240 | 98.9% | 98.9% | +0.6 | n/a | no target |
| P06T | 95584 | 81.3% | 81.3% | -2.4 | n/a | no target |
| P06 | 297 | 24.6% | 24.6% | -1.6 | n/a | no target |
| P07 | 788 | 15.0% | 15.0% | -4.1 | n/a | no target |
| P08 | 25442 | 9.0% | 9.0% | -2.0 | n/a | no target |
| P09 | 294 | 98.6% | 98.6% | -0.1 | 100% | 🟡 1 pts to go |
| P10R | 105619 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P10 | 2652 | 71.3% | 71.3% | -0.4 | n/a | no target |
| P11 | 24579 | 8.5% | 8.5% | -7.6 | n/a | no target |
| P12 | 7 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P13 | 17451 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `number_of_bids`

> ceiling: published by some portals only (bids&tenders submission lists, Biddingo bidder lists); federal proactive disclosure does not publish bid counts

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 123 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P01T | 446 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P01_GOLD | 625 | 16.8% | 16.8% | +0.0 | 60% | ❌ 43 pts to go · rows from a source that publishes bids: 363 rows, 28.9% filled |
| P02 | 486 | 10.7% | 10.7% | -0.5 | n/a | no target · rows from a source that publishes bids: 290 rows, 17.9% filled |
| P03 | 264 | 12.9% | 12.9% | -0.4 | n/a | no target · rows from a source that publishes bids: 139 rows, 24.5% filled |
| P04 | 4132 | 1.3% | 1.3% | -0.3 | n/a | no target · rows from a source that publishes bids: 872 rows, 6.3% filled |
| P05 | 420 | 2.9% | 2.9% | -0.1 | n/a | no target · rows from a source that publishes bids: 51 rows, 23.5% filled |
| P06M | 13240 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06T | 95584 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06 | 297 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P07 | 788 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P08 | 25442 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P09 | 294 | 3.1% | 3.1% | +0.1 | n/a | no target · rows from a source that publishes bids: 281 rows, 3.2% filled |
| P10R | 105619 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P10 | 2652 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P11 | 24579 | 0.0% | 0.0% | -0.1 | n/a | no target · rows from a source that publishes bids: 88 rows, 13.6% filled |
| P12 | 7 | 0.0% | 0.0% | +0.0 | n/a | no target · rows from a source that publishes bids: 7 rows, 0.0% filled |
| P13 | 17451 | 0.0% | 0.0% | +0.0 | n/a | no target |

## 6. history

### `average_contract_duration_days`

> ceiling: needs two dates (or a published term) on the buyer's records; P09 rows (end date unpublished by definition) and buyers whose sources publish award dates only have no honest duration

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 123 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P01T | 446 | 0.2% | 98.7% | -0.1 | n/a | no target |
| P01_GOLD | 625 | 53.3% | 82.4% | +0.1 | 90% | ❌ 37 pts to go |
| P02 | 486 | 50.2% | 88.1% | -2.3 | 90% | ❌ 40 pts to go |
| P03 | 264 | 44.3% | 80.7% | -1.4 | 90% | ❌ 46 pts to go |
| P04 | 4132 | 17.2% | 94.5% | -3.7 | 90% | ❌ 73 pts to go |
| P05 | 420 | 0.0% | 83.1% | +0.0 | 90% | ❌ 90 pts to go |
| P06M | 13240 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P06T | 95584 | 0.0% | 99.9% | +0.0 | n/a | no target |
| P06 | 297 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P07 | 788 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P08 | 25442 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P09 | 294 | 2.4% | 4.1% | +0.1 | 90% | ❌ 88 pts to go |
| P10R | 105619 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P10 | 2652 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P11 | 24579 | 0.2% | 99.8% | -0.4 | n/a | no target |
| P12 | 7 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P13 | 17451 | 0.0% | 100.0% | +0.0 | n/a | no target |

### `commodity_distribution_top3`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 123 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P01T | 446 | 0.4% | 98.9% | -0.2 | n/a | no target |
| P01_GOLD | 625 | 25.9% | 55.0% | +0.0 | 90% | ❌ 64 pts to go |
| P02 | 486 | 49.4% | 87.2% | -2.2 | n/a | no target |
| P03 | 264 | 24.2% | 60.6% | -0.8 | n/a | no target |
| P04 | 4132 | 18.9% | 96.2% | -4.0 | n/a | no target |
| P05 | 420 | 0.5% | 83.6% | +0.0 | n/a | no target |
| P06M | 13240 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P06T | 95584 | 0.0% | 100.0% | -0.1 | n/a | no target |
| P06 | 297 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P07 | 788 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P08 | 25442 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P09 | 294 | 41.2% | 42.9% | -0.7 | n/a | no target |
| P10R | 105619 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P10 | 2652 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P11 | 24579 | 0.2% | 99.8% | -0.4 | n/a | no target |
| P12 | 7 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P13 | 17451 | 0.0% | 100.0% | +0.0 | n/a | no target |

### `year_over_year_spend_trend`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 123 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P01T | 446 | 1.3% | 99.8% | -0.2 | n/a | no target |
| P01_GOLD | 625 | 51.8% | 81.0% | +0.0 | 95% | ❌ 43 pts to go |
| P02 | 486 | 54.1% | 92.0% | -2.5 | n/a | no target |
| P03 | 264 | 46.6% | 83.0% | -1.4 | n/a | no target |
| P04 | 4132 | 19.1% | 96.3% | -4.0 | n/a | no target |
| P05 | 420 | 4.5% | 87.6% | -0.2 | n/a | no target |
| P06M | 13240 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P06T | 95584 | 0.1% | 100.0% | +0.0 | n/a | no target |
| P06 | 297 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P07 | 788 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P08 | 25442 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P09 | 294 | 63.6% | 65.3% | -0.4 | n/a | no target |
| P10R | 105619 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P10 | 2652 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P11 | 24579 | 0.2% | 99.8% | -0.4 | n/a | no target |
| P12 | 7 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P13 | 17451 | 0.0% | 100.0% | +0.0 | n/a | no target |

## 7. mail security

### `mta_sts`

> ceiling: DNS-only check; 'no record' counts as checked

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 123 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P01T | 446 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P01_GOLD | 625 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P02 | 486 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P03 | 264 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P04 | 4132 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P05 | 420 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P06M | 13240 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P06T | 95584 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P06 | 297 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P07 | 788 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P08 | 25442 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P09 | 294 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P10R | 105619 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P10 | 2652 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P11 | 24579 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P12 | 7 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P13 | 17451 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |

### `tls_rpt`

> ceiling: DNS-only check; 'no record' counts as checked

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 123 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P01T | 446 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P01_GOLD | 625 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P02 | 486 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P03 | 264 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P04 | 4132 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P05 | 420 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P06M | 13240 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P06T | 95584 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P06 | 297 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P07 | 788 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P08 | 25442 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P09 | 294 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P10R | 105619 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P10 | 2652 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P11 | 24579 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P12 | 7 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P13 | 17451 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |

### `bimi`

> ceiling: DNS-only check; 'no record' counts as checked

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 123 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P01T | 446 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P01_GOLD | 625 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P02 | 486 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P03 | 264 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P04 | 4132 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P05 | 420 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P06M | 13240 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P06T | 95584 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P06 | 297 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P07 | 788 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P08 | 25442 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P09 | 294 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P10R | 105619 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P10 | 2652 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P11 | 24579 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P12 | 7 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P13 | 17451 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |

