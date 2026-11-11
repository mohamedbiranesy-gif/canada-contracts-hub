# Coverage vs the downstream team's targets — 2026-11-11

Benchmarks (field × package with a numeric target): **94 of 446 met** (21.1%); 54 within 10 points; 298 further away.
A cell counts as filled only when it carries a value: blank, `not_published`, `not_found_yet` and label-only cells ("no identifier published …", "no dataset record …", "0 in the contract dataset …") do not count; the DNS checks count when checked. `any` = share of non-blank cells incl. such labels. Δ = change since the previous build in `coord/results/coverage_history.csv`.
Rows per package: P01M 126, P01T 370, P01_GOLD 625, P02 470, P03 257, P04 3821, P05 424, P06M 13001, P06T 67038, P06 298, P07 801, P08 25648, P09 295, P10R 98583, P10 2685, P11 14978, P12 7, P13 18028

## Invoice-grade readiness (the row as an invoice header: bill-to, submit-to, references, terms, tax, vendor identity, follow-up)

| package | rows | all 11 elements | ≥ 9 of 11 | median elements | most-missing element |
|---|---|---|---|---|---|
| P01M | 126 | 0.0% | 13.5% | 8 | vendor GST/HST number (114 rows) |
| P01T | 370 | 0.8% | 20.3% | 7 | payment terms (296 rows) |
| P01_GOLD | 625 | 24.0% | 70.7% | 9 | payment terms (214 rows) |
| P02 | 470 | 7.2% | 54.3% | 9 | PO rule (359 rows) |
| P03 | 257 | 14.8% | 58.0% | 9 | PO rule (123 rows) |
| P04 | 3821 | 1.2% | 15.9% | 6 | PO rule (3629 rows) |
| P05 | 424 | 1.2% | 17.0% | 7 | payment terms (349 rows) |
| P06M | 13001 | 0.0% | 1.2% | 7 | PO rule (12968 rows) |
| P06T | 67038 | 0.0% | 3.4% | 7 | PO rule (66690 rows) |
| P06 | 298 | 0.0% | 8.1% | 6 | reference to quote (PO / contract / vendor id) (298 rows) |
| P07 | 801 | 0.0% | 1.7% | 6 | reference to quote (PO / contract / vendor id) (801 rows) |
| P08 | 25648 | 0.0% | 0.3% | 5 | reference to quote (PO / contract / vendor id) (25648 rows) |
| P09 | 295 | 1.0% | 44.4% | 8 | payment terms (276 rows) |
| P10R | 98583 | 0.0% | 20.1% | 7 | PO rule (98546 rows) |
| P10 | 2685 | 0.0% | 0.9% | 5 | reference to quote (PO / contract / vendor id) (2685 rows) |
| P11 | 14978 | 0.0% | 1.7% | 6 | PO rule (14874 rows) |
| P12 | 7 | 0.0% | 28.6% | 8 | PO rule (7 rows) |
| P13 | 18028 | 0.0% | 0.2% | 7 | reference to quote (PO / contract / vendor id) (18028 rows) |

## AP grade (how stringently the row's accounts-payable data meets what an invoice needs; A = invoicing mailbox referee-confirmed on the buyer's own domain with MX, legal name, address, PO rule and terms all published, no penalties)

| package | rows | A | B | C | D | E | median ap_score |
|---|---|---|---|---|---|---|---|
| P01M | 126 | 10 | 12 | 104 | 0 | 0 | 71 |
| P01T | 370 | 30 | 60 | 280 | 0 | 0 | 69 |
| P01_GOLD | 625 | 226 | 191 | 208 | 0 | 0 | 82 |
| P02 | 470 | 0 | 192 | 278 | 0 | 0 | 66 |
| P03 | 257 | 0 | 0 | 245 | 12 | 0 | 57 |
| P04 | 3821 | 0 | 0 | 3128 | 693 | 0 | 46 |
| P05 | 424 | 15 | 29 | 366 | 14 | 0 | 51 |
| P06M | 13001 | 0 | 3 | 12941 | 57 | 0 | 46 |
| P06T | 67038 | 0 | 41 | 55618 | 11379 | 0 | 38 |
| P06 | 298 | 20 | 45 | 233 | 0 | 0 | 68 |
| P07 | 801 | 0 | 25 | 749 | 27 | 0 | 52 |
| P08 | 25648 | 0 | 0 | 21461 | 4187 | 0 | 38 |
| P09 | 295 | 3 | 12 | 278 | 2 | 0 | 53 |
| P10R | 98583 | 2 | 11 | 68301 | 30269 | 0 | 38 |
| P10 | 2685 | 2 | 14 | 2005 | 664 | 0 | 43 |
| P11 | 14978 | 6 | 10 | 43 | 0 | 14919 | 23 |
| P12 | 7 | 0 | 0 | 7 | 0 | 0 | 54 |
| P13 | 18028 | 0 | 15 | 14598 | 3415 | 0 | 43 |

### AP payability (confirmed channel + bill-to legal name and address + the buyer's reference rule + tax treatment known)

| package | rows | payable today | % | most common gap |
|---|---|---|---|---|
| P01M | 126 | 101 | 80.2% | the buyer's PO / reference rule (13) |
| P01T | 370 | 191 | 51.6% | bill-to legal name and address (134) |
| P01_GOLD | 625 | 464 | 74.2% | bill-to legal name and address (107) |
| P02 | 470 | 312 | 66.4% | the buyer's PO / reference rule (85) |
| P03 | 257 | 0 | 0.0% | a confirmed invoicing / AP or finance channel (257) |
| P04 | 3821 | 0 | 0.0% | a confirmed invoicing / AP or finance channel (3821) |
| P05 | 424 | 46 | 10.8% | a confirmed invoicing / AP or finance channel (337) |
| P06M | 13001 | 123 | 0.9% | a confirmed invoicing / AP or finance channel (12826) |
| P06T | 67038 | 396 | 0.6% | a confirmed invoicing / AP or finance channel (66052) |
| P06 | 298 | 43 | 14.4% | bill-to legal name and address (126) |
| P07 | 801 | 10 | 1.2% | bill-to legal name and address (369) |
| P08 | 25648 | 0 | 0.0% | a confirmed invoicing / AP or finance channel (25648) |
| P09 | 295 | 41 | 13.9% | a confirmed invoicing / AP or finance channel (245) |
| P10R | 98583 | 482 | 0.5% | a confirmed invoicing / AP or finance channel (97438) |
| P10 | 2685 | 4 | 0.1% | a confirmed invoicing / AP or finance channel (2588) |
| P11 | 14978 | 11 | 0.1% | a confirmed invoicing / AP or finance channel (14919) |
| P12 | 7 | 3 | 42.9% | a confirmed invoicing / AP or finance channel (4) |
| P13 | 18028 | 7 | 0.0% | a confirmed invoicing / AP or finance channel (17686) |

### Pay on sight (an invoice generated from the row would clear AP: confirmed invoicing / AP or finance channel, bill-to legal name + address, vendor legal name + GST/HST number + remit-to address, tax treatment and currency known — published or labelled-derived; the buyer's reference rule is reported separately)

| package | rows | pay on sight | % | + reference rule not published | routed (general inbox only) | most common gap |
|---|---|---|---|---|---|---|
| P01M | 126 | 6 | 4.8% | 5 | 0 | the vendor's GST/HST number (BN9) (113) |
| P01T | 370 | 66 | 17.8% | 26 | 0 | the vendor's GST/HST number (BN9) (205) |
| P01_GOLD | 625 | 396 | 63.4% | 12 | 0 | the vendor's GST/HST number (BN9) (154) |
| P02 | 470 | 211 | 44.9% | 23 | 0 | the vendor's GST/HST number (BN9) (205) |
| P03 | 257 | 16 | 6.2% | 0 | 132 | an invoicing / AP or finance mailbox (only a purchasing / general inbo (88) |
| P04 | 3821 | 42 | 1.1% | 8 | 809 | an invoicing / AP or finance mailbox (only a purchasing / general inbo (2905) |
| P05 | 424 | 20 | 4.7% | 7 | 110 | an invoicing / AP or finance mailbox (only a purchasing / general inbo (220) |
| P06M | 13001 | 1 | 0.0% | 10 | 147 | an invoicing / AP or finance mailbox (only a purchasing / general inbo (12659) |
| P06T | 67038 | 95 | 0.1% | 97 | 12206 | an invoicing / AP or finance mailbox (only a purchasing / general inbo (53689) |
| P06 | 298 | 16 | 5.4% | 29 | 0 | the vendor's GST/HST number (BN9) (176) |
| P07 | 801 | 5 | 0.6% | 68 | 28 | the vendor's GST/HST number (BN9) (430) |
| P08 | 25648 | 1 | 0.0% | 8 | 2673 | an invoicing / AP or finance mailbox (only a purchasing / general inbo (22912) |
| P09 | 295 | 38 | 12.9% | 1 | 119 | an invoicing / AP or finance mailbox (only a purchasing / general inbo (117) |
| P10R | 98583 | 844 | 0.9% | 0 | 53007 | an invoicing / AP or finance mailbox (only a purchasing / general inbo (44369) |
| P10 | 2685 | 4 | 0.1% | 20 | 393 | an invoicing / AP or finance mailbox (only a purchasing / general inbo (2165) |
| P11 | 14978 | 11 | 0.1% | 12 | 0 | a confirmed invoicing / AP or finance channel (14886) |
| P12 | 7 | 1 | 14.3% | 0 | 2 | the vendor's GST/HST number (BN9) (2) |
| P13 | 18028 | 9 | 0.0% | 247 | 10556 | an invoicing / AP or finance mailbox (only a purchasing / general inbo (7090) |
| **all** | 247455 | 1782 | 0.7% | 573 | 80182 | |

### What still blocks grade A (rows per missing element; a row counts under every element it lacks)

| package | rows not A | referee confirmation of the mailbox | an invoicing / AP mailbox (not finance / procurement / general) | a mailbox on the buyer's own domain | MX record for the mailbox domain | published bill-to legal name | invoice / billing address | published PO rule | published payment terms | clear the penalty |
|---|---|---|---|---|---|---|---|---|---|---|
| P01M | 116 | 0 | 0 | 0 | 60 | 9 | 0 | 107 | 111 | 1 |
| P01T | 340 | 0 | 0 | 0 | 153 | 120 | 32 | 285 | 298 | 31 |
| P01_GOLD | 399 | 0 | 0 | 0 | 11 | 90 | 33 | 194 | 228 | 57 |
| P02 | 470 | 0 | 470 | 0 | 46 | 63 | 19 | 359 | 289 | 22 |
| P03 | 257 | 0 | 257 | 0 | 14 | 43 | 25 | 123 | 129 | 25 |
| P04 | 3821 | 0 | 3821 | 0 | 1790 | 1658 | 953 | 3629 | 3369 | 131 |
| P05 | 409 | 0 | 357 | 0 | 74 | 98 | 48 | 340 | 351 | 50 |
| P06M | 13001 | 0 | 13001 | 0 | 8203 | 1456 | 106 | 12968 | 12930 | 78 |
| P06T | 67038 | 0 | 67038 | 0 | 51816 | 39090 | 14779 | 66690 | 65576 | 403 |
| P06 | 278 | 0 | 0 | 0 | 120 | 111 | 51 | 211 | 241 | 4 |
| P07 | 801 | 0 | 801 | 0 | 472 | 411 | 137 | 752 | 753 | 14 |
| P08 | 25648 | 0 | 25648 | 0 | 18833 | 14554 | 5387 | 25409 | 25076 | 228 |
| P09 | 292 | 0 | 271 | 0 | 9 | 68 | 2 | 266 | 278 | 44 |
| P10R | 98581 | 0 | 98410 | 0 | 76388 | 64605 | 38907 | 98546 | 98398 | 24 |
| P10 | 2683 | 0 | 2646 | 0 | 1282 | 1430 | 928 | 2616 | 2567 | 115 |
| P11 | 14972 | 14919 | 14858 | 0 | 13539 | 10954 | 952 | 14874 | 14477 | 39 |
| P12 | 7 | 0 | 6 | 0 | 0 | 2 | 0 | 7 | 7 | 0 |
| P13 | 18028 | 0 | 17925 | 0 | 9069 | 9917 | 4179 | 17992 | 17985 | 20 |

## Where the work is (largest gaps in rows still needed)

| field | package | now | target | rows needed |
|---|---|---|---|---|
| buyer_ap_cycle_published | P10R | 0.0% | 20% | 19691 |
| ap_system_hint | P10R | 0.2% | 20% | 19517 |
| buyer_tax_exempt_status | P10R | 0.0% | 15% | 14758 |
| buyer_esignature_preference | P10R | 0.0% | 15% | 14741 |
| vendor_registered_address | P08 | 13.2% | 70% | 14580 |
| buyer_payment_method_preference | P10R | 0.6% | 15% | 14157 |
| buyer_ap_cycle_published | P06T | 0.0% | 20% | 13385 |
| ap_system_hint | P06T | 0.7% | 20% | 12947 |
| vendor_phone | P11 | 4.8% | 75% | 10511 |
| vendor_emails | P11 | 3.5% | 70% | 9961 |
| buyer_esignature_preference | P06T | 0.2% | 15% | 9913 |
| buyer_tax_exempt_status | P06T | 0.3% | 15% | 9869 |
| buyer_phone | P08 | 56.8% | 95% | 9791 |
| buyer_payment_method_preference | P06T | 0.7% | 15% | 9619 |
| vendor_bn9 | P08 | 14.5% | 50% | 9106 |
| contract_value | P11 | 0.6% | 60% | 8902 |
| award_or_notice_id | P11 | 0.6% | 60% | 8901 |
| buyer_legal_name_as_published | P08 | 43.3% | 75% | 8142 |
| contract_or_agreement_number | P11 | 8.7% | 60% | 7682 |
| invoice_reference_hint | P11 | 9.3% | 60% | 7595 |
| buyer_phone | P11 | 24.9% | 75% | 7511 |
| commodity_codes | P11 | 0.4% | 50% | 7428 |
| buyer_phone | P13 | 57.1% | 95% | 6839 |
| buyer_logo_url | P08 | 74.1% | 100% | 6642 |
| vendor_phone | P08 | 60.2% | 85% | 6370 |
| invoice_reference_hint | P08 | 0.9% | 25% | 6173 |
| vendor_emails | P08 | 51.0% | 75% | 6153 |
| solicitation_or_tender_number | P11 | 0.5% | 40% | 5913 |
| buyer_legal_name_as_published | P11 | 26.9% | 65% | 5712 |
| buyer_logo_url | P13 | 64.1% | 95% | 5565 |
| buyer_bn_as_published | P08 | 13.8% | 35% | 5443 |
| buyer_ap_cycle_published | P08 | 0.0% | 20% | 5122 |
| vendor_trading_name | P08 | 30.3% | 50% | 5052 |
| ap_system_hint | P08 | 0.8% | 20% | 4921 |
| vendor_logo_url | P08 | 83.0% | 100% | 4370 |
| buyer_address | P08 | 79.0% | 95% | 4110 |
| buyer_esignature_preference | P08 | 0.4% | 15% | 3757 |
| buyer_tax_exempt_status | P08 | 0.4% | 15% | 3754 |
| buyer_payment_method_preference | P08 | 0.5% | 15% | 3710 |
| buyer_logo_url | P11 | 55.5% | 80% | 3674 |

## 1. identifiers

### `invoice_reference_hint`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 126 | 88.1% | 88.1% | -0.6 | 50% | ✅ met |
| P01T | 370 | 88.6% | 88.6% | -0.9 | 50% | ✅ met |
| P01_GOLD | 625 | 92.2% | 94.4% | +0.0 | 95% | 🟡 3 pts to go |
| P02 | 470 | 73.0% | 74.5% | -0.8 | 95% | ❌ 22 pts to go |
| P03 | 257 | 81.7% | 84.8% | -0.3 | 95% | ❌ 13 pts to go |
| P04 | 3821 | 29.2% | 30.6% | -3.6 | 90% | ❌ 61 pts to go |
| P05 | 424 | 38.7% | 41.5% | +0.1 | 70% | ❌ 31 pts to go |
| P06M | 13001 | 91.2% | 91.2% | -1.4 | n/a | no target |
| P06T | 67038 | 79.3% | 79.3% | -1.0 | n/a | no target |
| P06 | 298 | 29.2% | 29.2% | -2.5 | 30% | 🟡 1 pts to go |
| P07 | 801 | 6.1% | 6.1% | -0.8 | 30% | ❌ 24 pts to go |
| P08 | 25648 | 0.9% | 0.9% | -0.2 | 25% | ❌ 24 pts to go |
| P09 | 295 | 99.0% | 99.7% | +0.0 | 100% | 🟡 1 pts to go |
| P10R | 98583 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P10 | 2685 | 2.6% | 2.6% | +0.0 | 25% | ❌ 22 pts to go |
| P11 | 14978 | 9.3% | 9.4% | -4.3 | 60% | ❌ 51 pts to go |
| P12 | 7 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P13 | 18028 | 0.2% | 0.2% | +0.0 | 0% by design | — leave (by design) |

### `po_number_as_published`

> ceiling: a purchase-order number exists only where the buyer publishes PO-level data (Montréal, Laval, Toronto open data so far) or the record itself carries one; most sources publish awards, not POs — the target cannot be reached from public data for most buyers

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 126 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P01T | 370 | 0.0% | 0.0% | +0.0 | 10% | 🟡 10 pts to go |
| P01_GOLD | 625 | 6.1% | 6.1% | +0.0 | 50% | ❌ 44 pts to go |
| P02 | 470 | 6.2% | 6.2% | +0.0 | 50% | ❌ 44 pts to go |
| P03 | 257 | 1.6% | 1.6% | +0.0 | 40% | ❌ 38 pts to go |
| P04 | 3821 | 0.5% | 0.5% | +0.0 | 30% | ❌ 30 pts to go |
| P05 | 424 | 0.2% | 0.2% | +0.0 | 20% | ❌ 20 pts to go |
| P06M | 13001 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06T | 67038 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06 | 298 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P07 | 801 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P08 | 25648 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P09 | 295 | 0.7% | 0.7% | +0.0 | 50% | ❌ 49 pts to go |
| P10R | 98583 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P10 | 2685 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P11 | 14978 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P12 | 7 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P13 | 18028 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `contract_or_agreement_number`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 126 | 82.5% | 82.5% | +1.1 | n/a | no target |
| P01T | 370 | 71.6% | 71.6% | +1.1 | 50% | ✅ met |
| P01_GOLD | 625 | 66.9% | 66.9% | +0.0 | 85% | ❌ 18 pts to go |
| P02 | 470 | 64.3% | 64.3% | -0.6 | 90% | ❌ 26 pts to go |
| P03 | 257 | 61.1% | 61.1% | -0.2 | 85% | ❌ 24 pts to go |
| P04 | 3821 | 26.9% | 26.9% | -3.2 | 85% | ❌ 58 pts to go |
| P05 | 424 | 29.0% | 29.0% | +0.0 | 60% | ❌ 31 pts to go |
| P06M | 13001 | 91.1% | 91.1% | -1.3 | n/a | no target |
| P06T | 67038 | 79.0% | 79.0% | -1.0 | n/a | no target |
| P06 | 298 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P07 | 801 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P08 | 25648 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P09 | 295 | 95.9% | 95.9% | -0.1 | 100% | 🟡 4 pts to go |
| P10R | 98583 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P10 | 2685 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P11 | 14978 | 8.7% | 8.7% | -4.0 | 60% | ❌ 51 pts to go |
| P12 | 7 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P13 | 18028 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `solicitation_or_tender_number`

> ceiling: SEAO's 'numero' is the organisation's own reference for the notice (SEAO data dictionary) and is reported here; sources that publish awards under a tender number only (bids&tenders, SaskTenders, BC) also carry it as the contract reference, labelled

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 126 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P01T | 370 | 0.0% | 0.0% | +0.0 | 30% | ❌ 30 pts to go |
| P01_GOLD | 625 | 50.7% | 50.7% | +0.1 | 80% | ❌ 29 pts to go |
| P02 | 470 | 56.4% | 56.4% | -0.6 | 60% | 🟡 4 pts to go |
| P03 | 257 | 51.4% | 51.4% | -0.2 | 80% | ❌ 29 pts to go |
| P04 | 3821 | 22.3% | 22.3% | -2.7 | 50% | ❌ 28 pts to go |
| P05 | 424 | 11.6% | 11.6% | -0.3 | 40% | ❌ 28 pts to go |
| P06M | 13001 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06T | 67038 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06 | 298 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P07 | 801 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P08 | 25648 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P09 | 295 | 83.1% | 83.1% | -0.4 | 50% | ✅ met |
| P10R | 98583 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P10 | 2685 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P11 | 14978 | 0.5% | 0.5% | -0.3 | 40% | ❌ 40 pts to go |
| P12 | 7 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P13 | 18028 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `award_or_notice_id`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 126 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P01T | 370 | 0.3% | 0.3% | +0.0 | n/a | no target |
| P01_GOLD | 625 | 60.5% | 60.5% | +0.1 | 85% | ❌ 24 pts to go |
| P02 | 470 | 55.7% | 55.7% | -0.6 | 90% | ❌ 34 pts to go |
| P03 | 257 | 59.9% | 59.9% | -0.3 | 85% | ❌ 25 pts to go |
| P04 | 3821 | 23.0% | 23.0% | -2.8 | 85% | ❌ 62 pts to go |
| P05 | 424 | 19.8% | 19.8% | -0.1 | 50% | ❌ 30 pts to go |
| P06M | 13001 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06T | 67038 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06 | 298 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P07 | 801 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P08 | 25648 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P09 | 295 | 96.9% | 96.9% | -0.1 | 100% | 🟡 3 pts to go |
| P10R | 98583 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P10 | 2685 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P11 | 14978 | 0.6% | 0.6% | -0.3 | 60% | ❌ 59 pts to go |
| P12 | 7 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P13 | 18028 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `buyer_vendor_id`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 126 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P01T | 370 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P01_GOLD | 625 | 13.0% | 13.0% | +0.1 | 60% | ❌ 47 pts to go |
| P02 | 470 | 6.0% | 6.0% | +0.0 | 50% | ❌ 44 pts to go |
| P03 | 257 | 8.6% | 8.6% | +0.0 | 50% | ❌ 41 pts to go |
| P04 | 3821 | 1.8% | 1.8% | -0.2 | 40% | ❌ 38 pts to go |
| P05 | 424 | 0.7% | 0.7% | -0.2 | 20% | ❌ 19 pts to go |
| P06M | 13001 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06T | 67038 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06 | 298 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P07 | 801 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P08 | 25648 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P09 | 295 | 2.4% | 2.4% | +0.1 | 50% | ❌ 48 pts to go |
| P10R | 98583 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P10 | 2685 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P11 | 14978 | 0.1% | 0.1% | +0.0 | n/a | no target |
| P12 | 7 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P13 | 18028 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `commodity_codes`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 126 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P01T | 370 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P01_GOLD | 625 | 34.9% | 34.9% | +0.1 | 80% | ❌ 45 pts to go |
| P02 | 470 | 51.5% | 51.5% | -0.5 | 90% | ❌ 38 pts to go |
| P03 | 257 | 33.5% | 33.5% | -0.1 | 80% | ❌ 46 pts to go |
| P04 | 3821 | 21.0% | 21.0% | -2.6 | 85% | ❌ 64 pts to go |
| P05 | 424 | 5.4% | 5.4% | +0.0 | 50% | ❌ 45 pts to go |
| P06M | 13001 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06T | 67038 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06 | 298 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P07 | 801 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P08 | 25648 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P09 | 295 | 75.6% | 75.6% | -0.3 | 95% | ❌ 19 pts to go |
| P10R | 98583 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P10 | 2685 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P11 | 14978 | 0.4% | 0.4% | -0.2 | 50% | ❌ 50 pts to go |
| P12 | 7 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P13 | 18028 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `buyer_org_codes`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 126 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P01T | 370 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P01_GOLD | 625 | 8.5% | 8.5% | +0.0 | 50% | ❌ 42 pts to go |
| P02 | 470 | 6.2% | 6.2% | +0.0 | 50% | ❌ 44 pts to go |
| P03 | 257 | 1.9% | 1.9% | -0.1 | 30% | ❌ 28 pts to go |
| P04 | 3821 | 0.4% | 0.4% | -0.1 | 30% | ❌ 30 pts to go |
| P05 | 424 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06M | 13001 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06T | 67038 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06 | 298 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P07 | 801 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P08 | 25648 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P09 | 295 | 0.3% | 0.3% | +0.0 | n/a | no target |
| P10R | 98583 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P10 | 2685 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P11 | 14978 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P12 | 7 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P13 | 18028 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `records_with_this_vendor`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 126 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P01T | 370 | 100.0% | 100.0% | +0.0 | 60% | ✅ met |
| P01_GOLD | 625 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P02 | 470 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P03 | 257 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P04 | 3821 | 100.0% | 100.0% | +0.0 | 95% | ✅ met |
| P05 | 424 | 100.0% | 100.0% | +0.0 | 70% | ✅ met |
| P06M | 13001 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P06T | 67038 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P06 | 298 | 100.0% | 100.0% | +0.0 | 50% | ✅ met |
| P07 | 801 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P08 | 25648 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P09 | 295 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P10R | 98583 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P10 | 2685 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P11 | 14978 | 100.0% | 100.0% | +0.0 | 70% | ✅ met |
| P12 | 7 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P13 | 18028 | 0.0% | 0.0% | +0.0 | n/a | no target |

## 2. vendor

### `vendor_bn9`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 126 | 9.5% | 9.5% | -4.9 | 70% | ❌ 60 pts to go |
| P01T | 370 | 31.9% | 31.9% | -1.8 | 60% | ❌ 28 pts to go |
| P01_GOLD | 625 | 72.6% | 72.6% | -0.4 | 90% | ❌ 17 pts to go |
| P02 | 470 | 53.6% | 53.6% | -1.5 | 85% | ❌ 31 pts to go |
| P03 | 257 | 68.5% | 68.5% | -1.4 | 90% | ❌ 22 pts to go |
| P04 | 3821 | 31.6% | 31.6% | -0.9 | 75% | ❌ 43 pts to go |
| P05 | 424 | 50.5% | 50.5% | +0.6 | 50% | ✅ met |
| P06M | 13001 | 1.6% | 1.6% | -0.2 | n/a | no target |
| P06T | 67038 | 22.1% | 22.1% | +4.8 | n/a | no target |
| P06 | 298 | 25.2% | 25.2% | +2.4 | 40% | ❌ 15 pts to go |
| P07 | 801 | 18.4% | 18.4% | +2.0 | 50% | ❌ 32 pts to go |
| P08 | 25648 | 14.5% | 14.5% | +3.6 | 50% | ❌ 36 pts to go |
| P09 | 295 | 58.3% | 58.3% | +0.5 | 80% | ❌ 22 pts to go |
| P10R | 98583 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P10 | 2685 | 31.1% | 31.1% | +2.4 | 40% | 🟡 9 pts to go |
| P11 | 14978 | 93.9% | 93.9% | +2.8 | 60% | ✅ met |
| P12 | 7 | 42.9% | 42.9% | -19.6 | 85% | ❌ 42 pts to go |
| P13 | 18028 | 90.8% | 90.8% | -0.2 | 0% by design | — leave (by design) |

### `vendor_registered_address`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 126 | 56.3% | 56.3% | -10.7 | n/a | no target |
| P01T | 370 | 39.7% | 39.7% | +1.7 | n/a | no target |
| P01_GOLD | 625 | 70.6% | 70.6% | +0.2 | 95% | ❌ 24 pts to go |
| P02 | 470 | 73.2% | 73.2% | -0.6 | 95% | ❌ 22 pts to go |
| P03 | 257 | 71.6% | 71.6% | -0.3 | 95% | ❌ 23 pts to go |
| P04 | 3821 | 43.7% | 43.7% | -1.9 | 95% | ❌ 51 pts to go |
| P05 | 424 | 53.1% | 53.1% | -0.3 | 70% | ❌ 17 pts to go |
| P06M | 13001 | 43.4% | 43.4% | -11.2 | n/a | no target |
| P06T | 67038 | 31.4% | 31.4% | +1.1 | n/a | no target |
| P06 | 298 | 25.5% | 25.5% | +0.7 | 80% | ❌ 54 pts to go |
| P07 | 801 | 17.6% | 17.6% | -0.4 | 70% | ❌ 52 pts to go |
| P08 | 25648 | 13.2% | 13.2% | -0.9 | 70% | ❌ 57 pts to go |
| P09 | 295 | 87.1% | 87.1% | -0.4 | 100% | ❌ 13 pts to go |
| P10R | 98583 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P10 | 2685 | 32.5% | 32.5% | +0.0 | 70% | ❌ 38 pts to go |
| P11 | 14978 | 94.6% | 94.6% | +2.4 | 75% | ✅ met |
| P12 | 7 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P13 | 18028 | 16.3% | 16.3% | +16.3 | n/a | no target |

### `vendor_trading_name`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 126 | 19.0% | 19.0% | +2.5 | n/a | no target |
| P01T | 370 | 45.1% | 45.1% | +19.2 | n/a | no target |
| P01_GOLD | 625 | 48.8% | 48.8% | +0.9 | 60% | ❌ 11 pts to go |
| P02 | 470 | 54.7% | 54.7% | -0.6 | 60% | 🟡 5 pts to go |
| P03 | 257 | 53.7% | 53.7% | -1.4 | 60% | 🟡 6 pts to go |
| P04 | 3821 | 35.5% | 35.5% | -1.2 | 55% | ❌ 20 pts to go |
| P05 | 424 | 21.9% | 21.9% | -0.3 | 50% | ❌ 28 pts to go |
| P06M | 13001 | 7.2% | 7.2% | +3.6 | n/a | no target |
| P06T | 67038 | 56.0% | 56.0% | +29.0 | n/a | no target |
| P06 | 298 | 40.9% | 40.9% | +5.7 | n/a | no target |
| P07 | 801 | 35.5% | 35.5% | +2.3 | 55% | ❌ 20 pts to go |
| P08 | 25648 | 30.3% | 30.3% | +3.4 | 50% | ❌ 20 pts to go |
| P09 | 295 | 71.5% | 71.5% | +0.5 | 70% | ✅ met |
| P10R | 98583 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P10 | 2685 | 42.6% | 42.6% | +3.1 | 55% | ❌ 12 pts to go |
| P11 | 14978 | 95.6% | 95.6% | +3.6 | 50% | ✅ met |
| P12 | 7 | 100.0% | 100.0% | +12.5 | n/a | no target |
| P13 | 18028 | 74.0% | 74.0% | +74.0 | n/a | no target |

### `vendor_phone`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 126 | 50.0% | 50.0% | +35.6 | n/a | no target |
| P01T | 370 | 69.7% | 69.7% | +13.4 | n/a | no target |
| P01_GOLD | 625 | 45.9% | 45.9% | -2.0 | 70% | ❌ 24 pts to go |
| P02 | 470 | 51.9% | 51.9% | -2.1 | 70% | ❌ 18 pts to go |
| P03 | 257 | 47.9% | 47.9% | -1.7 | 70% | ❌ 22 pts to go |
| P04 | 3821 | 47.2% | 47.2% | +0.1 | 65% | ❌ 18 pts to go |
| P05 | 424 | 26.7% | 26.7% | -4.0 | 60% | ❌ 33 pts to go |
| P06M | 13001 | 37.1% | 37.1% | +33.6 | n/a | no target |
| P06T | 67038 | 73.0% | 73.0% | +9.2 | n/a | no target |
| P06 | 298 | 63.1% | 63.1% | +5.5 | 40% | ✅ met |
| P07 | 801 | 61.2% | 61.2% | +4.2 | 85% | ❌ 24 pts to go |
| P08 | 25648 | 60.2% | 60.2% | +3.3 | 85% | ❌ 25 pts to go |
| P09 | 295 | 54.6% | 54.6% | +1.1 | 85% | ❌ 30 pts to go |
| P10R | 98583 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P10 | 2685 | 61.5% | 61.5% | +0.5 | 85% | ❌ 24 pts to go |
| P11 | 14978 | 4.8% | 4.8% | -1.6 | 75% | ❌ 70 pts to go |
| P12 | 7 | 28.6% | 28.6% | +3.6 | n/a | no target |
| P13 | 18028 | 100.0% | 100.0% | +0.0 | 60% | ✅ met |

### `vendor_website`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 126 | 54.0% | 54.0% | +34.4 | n/a | no target |
| P01T | 370 | 98.1% | 98.1% | +1.7 | n/a | no target |
| P01_GOLD | 625 | 79.5% | 79.5% | -9.8 | 90% | ❌ 10 pts to go |
| P02 | 470 | 84.3% | 84.3% | -4.9 | 90% | 🟡 6 pts to go |
| P03 | 257 | 87.2% | 87.2% | -3.8 | 90% | 🟡 3 pts to go |
| P04 | 3821 | 85.3% | 85.3% | -4.9 | 85% | ✅ met |
| P05 | 424 | 44.1% | 44.1% | -8.1 | 70% | ❌ 26 pts to go |
| P06M | 13001 | 42.9% | 42.9% | +36.7 | n/a | no target |
| P06T | 67038 | 99.9% | 99.9% | +7.9 | n/a | no target |
| P06 | 298 | 98.3% | 98.3% | +0.0 | 50% | ✅ met |
| P07 | 801 | 99.1% | 99.1% | +0.0 | 100% | 🟡 1 pts to go |
| P08 | 25648 | 99.5% | 99.5% | +0.1 | 100% | 🟡 0 pts to go |
| P09 | 295 | 80.3% | 80.3% | +0.1 | 100% | ❌ 20 pts to go |
| P10R | 98583 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P10 | 2685 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P11 | 14978 | 99.8% | 99.8% | +0.1 | 100% | 🟡 0 pts to go |
| P12 | 7 | 28.6% | 28.6% | -8.9 | n/a | no target |
| P13 | 18028 | 100.0% | 100.0% | +0.0 | n/a | no target |

### `vendor_emails`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 126 | 15.1% | 15.1% | +0.7 | n/a | no target |
| P01T | 370 | 48.1% | 48.1% | -1.0 | n/a | no target |
| P01_GOLD | 625 | 43.0% | 43.0% | -2.2 | 70% | ❌ 27 pts to go |
| P02 | 470 | 48.5% | 48.5% | -1.0 | 75% | ❌ 26 pts to go |
| P03 | 257 | 44.0% | 44.0% | -0.5 | 75% | ❌ 31 pts to go |
| P04 | 3821 | 37.0% | 37.0% | -0.4 | 70% | ❌ 33 pts to go |
| P05 | 424 | 20.5% | 20.5% | -5.0 | 55% | ❌ 34 pts to go |
| P06M | 13001 | 4.6% | 4.6% | +1.3 | n/a | no target |
| P06T | 67038 | 40.1% | 40.1% | +0.5 | n/a | no target |
| P06 | 298 | 45.0% | 45.0% | +2.2 | n/a | no target |
| P07 | 801 | 47.7% | 47.7% | +1.8 | 70% | ❌ 22 pts to go |
| P08 | 25648 | 51.0% | 51.0% | +1.1 | 75% | ❌ 24 pts to go |
| P09 | 295 | 49.8% | 49.8% | +0.0 | 85% | ❌ 35 pts to go |
| P10R | 98583 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P10 | 2685 | 43.5% | 43.5% | +0.0 | 80% | ❌ 36 pts to go |
| P11 | 14978 | 3.5% | 3.5% | -1.5 | 70% | ❌ 66 pts to go |
| P12 | 7 | 14.3% | 14.3% | -10.7 | n/a | no target |
| P13 | 18028 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `vendor_logo_url`

> ceiling: needs the vendor's website first; sites that block automated readers (robots.txt / 403) are never read

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 126 | 54.0% | 54.0% | +40.6 | n/a | no target |
| P01T | 370 | 86.2% | 86.2% | -3.6 | n/a | no target |
| P01_GOLD | 625 | 69.4% | 69.4% | -8.1 | 90% | ❌ 21 pts to go |
| P02 | 470 | 73.0% | 73.0% | -4.6 | 90% | ❌ 17 pts to go |
| P03 | 257 | 79.4% | 79.4% | -3.8 | 90% | ❌ 11 pts to go |
| P04 | 3821 | 71.2% | 71.2% | -4.4 | 85% | ❌ 14 pts to go |
| P05 | 424 | 41.3% | 41.3% | -7.4 | 75% | ❌ 34 pts to go |
| P06M | 13001 | 42.6% | 42.6% | +38.5 | n/a | no target |
| P06T | 67038 | 94.0% | 94.0% | +10.8 | n/a | no target |
| P06 | 298 | 82.9% | 82.9% | +3.6 | n/a | no target |
| P07 | 801 | 86.1% | 86.1% | +4.5 | 100% | ❌ 14 pts to go |
| P08 | 25648 | 83.0% | 83.0% | +4.1 | 100% | ❌ 17 pts to go |
| P09 | 295 | 62.0% | 62.0% | +0.6 | n/a | no target |
| P10R | 98583 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P10 | 2685 | 84.2% | 84.2% | +0.0 | 100% | ❌ 16 pts to go |
| P11 | 14978 | 93.0% | 93.0% | +4.6 | n/a | no target |
| P12 | 7 | 28.6% | 28.6% | -8.9 | n/a | no target |
| P13 | 18028 | 83.6% | 83.6% | +0.4 | n/a | no target |

### `vendor_neq`

> ceiling: only Québec-registered vendors have an NEQ; the share of QC vendors is reported next to the rate

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 126 | 46.8% | 46.8% | -6.8 | n/a | no target · QC vendors: 46 rows, 100.0% filled |
| P01T | 370 | 20.8% | 20.8% | +3.0 | n/a | no target · QC vendors: 20 rows, 100.0% filled |
| P01_GOLD | 625 | 43.7% | 43.7% | +0.1 | 95% | ❌ 51 pts to go · QC vendors: 53 rows, 98.1% filled |
| P02 | 470 | 54.5% | 54.5% | -0.6 | 95% | ❌ 40 pts to go · QC vendors: 110 rows, 100.0% filled |
| P03 | 257 | 45.9% | 45.9% | -0.6 | 95% | ❌ 49 pts to go · QC vendors: 18 rows, 100.0% filled |
| P04 | 3821 | 28.3% | 28.3% | -3.6 | 95% | ❌ 67 pts to go · QC vendors: 493 rows, 98.8% filled |
| P05 | 424 | 14.2% | 14.2% | -0.6 | n/a | no target · QC vendors: 34 rows, 94.1% filled |
| P06M | 13001 | 42.4% | 42.4% | -10.9 | n/a | no target · QC vendors: 4809 rows, 100.0% filled |
| P06T | 67038 | 19.4% | 19.4% | +1.9 | n/a | no target · QC vendors: 3490 rows, 100.0% filled |
| P06 | 298 | 8.1% | 8.1% | -0.2 | n/a | no target · QC vendors: 17 rows, 76.5% filled |
| P07 | 801 | 5.9% | 5.9% | -0.9 | n/a | no target · QC vendors: 39 rows, 79.5% filled |
| P08 | 25648 | 6.0% | 6.0% | -0.5 | n/a | no target · QC vendors: 1246 rows, 97.9% filled |
| P09 | 295 | 78.0% | 78.0% | -0.2 | 95% | ❌ 17 pts to go · QC vendors: 106 rows, 100.0% filled |
| P10R | 98583 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P10 | 2685 | 17.5% | 17.5% | -0.1 | n/a | no target · QC vendors: 310 rows, 94.8% filled |
| P11 | 14978 | 87.7% | 87.7% | +6.2 | n/a | no target · QC vendors: 114 rows, 98.2% filled |
| P12 | 7 | 71.4% | 71.4% | +8.9 | n/a | no target · QC vendors: 1 rows, 100.0% filled |
| P13 | 18028 | 16.3% | 16.3% | +16.3 | n/a | no target · QC vendors: 2945 rows, 100.0% filled |

### `vendor_years_in_business`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 126 | 55.6% | 55.6% | -9.3 | n/a | no target · vendors with a registry record: 70 rows, 100.0% filled |
| P01T | 370 | 40.0% | 40.0% | +1.7 | n/a | no target · vendors with a registry record: 148 rows, 100.0% filled |
| P01_GOLD | 625 | 79.5% | 79.5% | +0.1 | 100% | ❌ 20 pts to go · vendors with a registry record: 497 rows, 100.0% filled |
| P02 | 470 | 76.8% | 76.8% | -0.6 | 100% | ❌ 23 pts to go · vendors with a registry record: 361 rows, 100.0% filled |
| P03 | 257 | 80.9% | 80.9% | -0.3 | 100% | ❌ 19 pts to go · vendors with a registry record: 208 rows, 100.0% filled |
| P04 | 3821 | 44.1% | 44.1% | -2.0 | 100% | ❌ 56 pts to go · vendors with a registry record: 1685 rows, 100.0% filled |
| P05 | 424 | 58.0% | 58.0% | -0.3 | n/a | no target · vendors with a registry record: 246 rows, 100.0% filled |
| P06M | 13001 | 43.2% | 43.2% | -11.1 | n/a | no target · vendors with a registry record: 5620 rows, 100.0% filled |
| P06T | 67038 | 31.4% | 31.4% | +1.0 | n/a | no target · vendors with a registry record: 21072 rows, 100.0% filled |
| P06 | 298 | 25.8% | 25.8% | +0.3 | n/a | no target · vendors with a registry record: 77 rows, 100.0% filled |
| P07 | 801 | 18.0% | 18.0% | -0.4 | n/a | no target · vendors with a registry record: 144 rows, 100.0% filled |
| P08 | 25648 | 13.3% | 13.3% | -1.0 | n/a | no target · vendors with a registry record: 3422 rows, 100.0% filled |
| P09 | 295 | 90.8% | 90.8% | -0.3 | n/a | no target · vendors with a registry record: 268 rows, 100.0% filled |
| P10R | 98583 | 100.0% | 100.0% | +0.0 | n/a | no target · vendors with a registry record: 98583 rows, 100.0% filled |
| P10 | 2685 | 33.1% | 33.1% | -0.1 | n/a | no target · vendors with a registry record: 889 rows, 100.0% filled |
| P11 | 14978 | 94.6% | 94.6% | +2.3 | n/a | no target · vendors with a registry record: 14176 rows, 100.0% filled |
| P12 | 7 | 100.0% | 100.0% | +0.0 | n/a | no target · vendors with a registry record: 7 rows, 100.0% filled |
| P13 | 18028 | 16.3% | 16.3% | +16.3 | n/a | no target · vendors with a registry record: 2945 rows, 100.0% filled |

## 3. buyer

### `buyer_legal_name_as_published`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 126 | 92.9% | 92.9% | +4.2 | 90% | ✅ met |
| P01T | 370 | 67.6% | 67.6% | +11.3 | 90% | ❌ 22 pts to go |
| P01_GOLD | 625 | 85.6% | 85.6% | +1.9 | 95% | 🟡 9 pts to go |
| P02 | 470 | 86.6% | 86.6% | +1.4 | 95% | 🟡 8 pts to go |
| P03 | 257 | 83.3% | 83.3% | +4.4 | 85% | 🟡 2 pts to go |
| P04 | 3821 | 56.6% | 56.6% | +0.2 | 90% | ❌ 33 pts to go |
| P05 | 424 | 76.9% | 76.9% | +9.2 | 75% | ✅ met |
| P06M | 13001 | 88.8% | 88.8% | +1.7 | n/a | no target |
| P06T | 67038 | 41.7% | 41.7% | +12.7 | n/a | no target |
| P06 | 298 | 62.8% | 62.8% | +5.9 | 80% | ❌ 17 pts to go |
| P07 | 801 | 48.7% | 48.8% | +2.5 | 80% | ❌ 31 pts to go |
| P08 | 25648 | 43.3% | 43.3% | +4.8 | 75% | ❌ 32 pts to go |
| P09 | 295 | 76.9% | 76.9% | -0.3 | 95% | ❌ 18 pts to go |
| P10R | 98583 | 34.5% | 34.5% | +9.5 | n/a | no target |
| P10 | 2685 | 46.7% | 46.8% | +7.7 | 70% | ❌ 23 pts to go |
| P11 | 14978 | 26.9% | 26.9% | +17.3 | 65% | ❌ 38 pts to go |
| P12 | 7 | 71.4% | 71.4% | -3.6 | 80% | 🟡 9 pts to go |
| P13 | 18028 | 45.0% | 45.0% | +5.8 | 60% | ❌ 15 pts to go |

### `buyer_bn_as_published`

> ceiling: a buyer's BN is public only where the buyer prints it or a public dataset carries it (CRA charities, federal grants & contributions recipients, business registries for corporations); municipalities rarely publish theirs

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 126 | 19.0% | 19.0% | -0.6 | 50% | ❌ 31 pts to go |
| P01T | 370 | 15.7% | 15.7% | +2.4 | n/a | no target |
| P01_GOLD | 625 | 19.8% | 19.8% | -0.8 | 40% | ❌ 20 pts to go |
| P02 | 470 | 19.4% | 19.4% | +0.5 | 40% | ❌ 21 pts to go |
| P03 | 257 | 23.0% | 23.0% | +0.7 | 40% | ❌ 17 pts to go |
| P04 | 3821 | 15.5% | 15.5% | -0.8 | 40% | ❌ 24 pts to go |
| P05 | 424 | 19.8% | 19.8% | +0.1 | 25% | 🟡 5 pts to go |
| P06M | 13001 | 10.5% | 10.5% | +1.7 | n/a | no target |
| P06T | 67038 | 9.7% | 9.7% | +2.2 | n/a | no target |
| P06 | 298 | 15.8% | 15.8% | +3.0 | 35% | ❌ 19 pts to go |
| P07 | 801 | 14.1% | 14.1% | +2.6 | 35% | ❌ 21 pts to go |
| P08 | 25648 | 13.8% | 13.8% | +3.4 | 35% | ❌ 21 pts to go |
| P09 | 295 | 16.3% | 16.3% | +0.1 | n/a | no target |
| P10R | 98583 | 8.9% | 8.9% | +1.8 | n/a | no target |
| P10 | 2685 | 11.3% | 11.3% | +4.8 | 30% | ❌ 19 pts to go |
| P11 | 14978 | 1.6% | 1.6% | +0.4 | n/a | no target |
| P12 | 7 | 14.3% | 14.3% | +1.8 | n/a | no target |
| P13 | 18028 | 20.8% | 20.8% | -0.2 | 30% | 🟡 9 pts to go |

### `buyer_address`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 126 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P01T | 370 | 90.5% | 90.5% | -1.4 | 100% | 🟡 10 pts to go |
| P01_GOLD | 625 | 90.1% | 90.1% | +0.6 | 100% | 🟡 10 pts to go |
| P02 | 470 | 95.5% | 95.5% | +0.2 | 100% | 🟡 4 pts to go |
| P03 | 257 | 89.1% | 89.1% | -0.4 | 100% | ❌ 11 pts to go |
| P04 | 3821 | 74.6% | 74.6% | -1.3 | 100% | ❌ 25 pts to go |
| P05 | 424 | 88.0% | 88.0% | +0.6 | 100% | ❌ 12 pts to go |
| P06M | 13001 | 99.2% | 99.2% | +0.4 | n/a | no target |
| P06T | 67038 | 77.9% | 77.9% | +0.5 | n/a | no target |
| P06 | 298 | 81.5% | 81.5% | +0.5 | 95% | ❌ 14 pts to go |
| P07 | 801 | 82.8% | 82.8% | -0.8 | 95% | ❌ 12 pts to go |
| P08 | 25648 | 79.0% | 79.0% | -1.2 | 95% | ❌ 16 pts to go |
| P09 | 295 | 95.9% | 95.9% | +0.2 | 100% | 🟡 4 pts to go |
| P10R | 98583 | 60.5% | 60.5% | +1.7 | n/a | no target |
| P10 | 2685 | 65.3% | 65.3% | +0.2 | 95% | ❌ 30 pts to go |
| P11 | 14978 | 92.1% | 92.1% | +4.9 | 80% | ✅ met |
| P12 | 7 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P13 | 18028 | 76.8% | 76.8% | +1.6 | 95% | ❌ 18 pts to go |

### `buyer_phone`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 126 | 68.3% | 68.3% | -17.3 | n/a | no target |
| P01T | 370 | 75.4% | 75.4% | +11.8 | n/a | no target |
| P01_GOLD | 625 | 70.4% | 70.4% | +0.9 | 90% | ❌ 20 pts to go |
| P02 | 470 | 75.5% | 75.5% | -0.2 | 95% | ❌ 20 pts to go |
| P03 | 257 | 73.5% | 73.5% | -0.3 | 95% | ❌ 22 pts to go |
| P04 | 3821 | 61.4% | 61.4% | -5.2 | 95% | ❌ 34 pts to go |
| P05 | 424 | 71.2% | 71.2% | +0.7 | 90% | ❌ 19 pts to go |
| P06M | 13001 | 68.6% | 68.6% | -17.8 | n/a | no target |
| P06T | 67038 | 66.3% | 66.3% | +18.4 | n/a | no target |
| P06 | 298 | 64.4% | 64.4% | +1.3 | 95% | ❌ 31 pts to go |
| P07 | 801 | 55.7% | 55.7% | +0.7 | 90% | ❌ 34 pts to go |
| P08 | 25648 | 56.8% | 56.8% | -2.0 | 95% | ❌ 38 pts to go |
| P09 | 295 | 85.8% | 85.8% | -0.3 | 100% | ❌ 14 pts to go |
| P10R | 98583 | 56.3% | 56.3% | +11.2 | n/a | no target |
| P10 | 2685 | 57.3% | 57.3% | +0.8 | 95% | ❌ 38 pts to go |
| P11 | 14978 | 24.9% | 24.9% | +13.7 | 75% | ❌ 50 pts to go |
| P12 | 7 | 71.4% | 71.4% | -3.6 | n/a | no target |
| P13 | 18028 | 57.1% | 57.1% | +9.5 | 95% | ❌ 38 pts to go |

### `buyer_logo_url`

> ceiling: sites that block automated readers (robots.txt / 403) are never read; an og:image that looks like a photo is labelled

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 126 | 62.7% | 62.7% | -8.4 | n/a | no target |
| P01T | 370 | 88.6% | 88.6% | +14.5 | 95% | 🟡 6 pts to go |
| P01_GOLD | 625 | 81.1% | 81.1% | +0.4 | 90% | 🟡 9 pts to go |
| P02 | 470 | 85.1% | 85.1% | -0.7 | 95% | 🟡 10 pts to go |
| P03 | 257 | 84.0% | 84.0% | +0.0 | 95% | ❌ 11 pts to go |
| P04 | 3821 | 76.3% | 76.3% | -7.0 | 90% | ❌ 14 pts to go |
| P05 | 424 | 89.4% | 89.4% | +0.9 | 95% | 🟡 6 pts to go |
| P06M | 13001 | 63.9% | 63.9% | -2.8 | n/a | no target |
| P06T | 67038 | 87.1% | 87.1% | +25.6 | n/a | no target |
| P06 | 298 | 81.2% | 81.2% | -0.9 | 100% | ❌ 19 pts to go |
| P07 | 801 | 74.5% | 74.5% | -2.7 | 100% | ❌ 26 pts to go |
| P08 | 25648 | 74.1% | 74.1% | -3.0 | 100% | ❌ 26 pts to go |
| P09 | 295 | 68.8% | 68.8% | +0.2 | n/a | no target |
| P10R | 98583 | 78.3% | 78.3% | +18.3 | n/a | no target |
| P10 | 2685 | 87.4% | 87.4% | +0.6 | 100% | ❌ 13 pts to go |
| P11 | 14978 | 55.5% | 55.5% | +36.7 | 80% | ❌ 24 pts to go |
| P12 | 7 | 71.4% | 71.4% | -3.6 | n/a | no target |
| P13 | 18028 | 64.1% | 64.1% | +13.1 | 95% | ❌ 31 pts to go |

## 4. AP

### `ap_contact_name_as_published`

> ceiling: owner 2026-11-08: the AP contact person the organisation itself names on its AP / finance page is allowed (name + role phrase, quoted); mailboxes stay organisational; many bodies publish no AP person

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 126 | 2.4% | 2.4% | -1.7 | n/a | no target |
| P01T | 370 | 8.1% | 8.1% | -0.3 | n/a | no target |
| P01_GOLD | 625 | 14.2% | 14.2% | +0.0 | 25% | ❌ 11 pts to go |
| P02 | 470 | 24.3% | 24.3% | -0.2 | 40% | ❌ 16 pts to go |
| P03 | 257 | 8.9% | 8.9% | -0.1 | 20% | ❌ 11 pts to go |
| P04 | 3821 | 3.2% | 3.2% | -0.4 | 20% | ❌ 17 pts to go |
| P05 | 424 | 3.1% | 3.1% | -0.2 | 15% | ❌ 12 pts to go |
| P06M | 13001 | 0.2% | 0.2% | -0.1 | n/a | no target |
| P06T | 67038 | 0.4% | 0.4% | +0.0 | n/a | no target |
| P06 | 298 | 5.4% | 5.4% | -0.8 | n/a | no target |
| P07 | 801 | 7.4% | 7.4% | +0.1 | n/a | no target |
| P08 | 25648 | 0.2% | 0.2% | -0.1 | n/a | no target |
| P09 | 295 | 7.8% | 7.8% | +0.2 | n/a | no target |
| P10R | 98583 | 0.2% | 0.2% | +0.0 | n/a | no target |
| P10 | 2685 | 0.9% | 0.9% | -0.1 | n/a | no target |
| P11 | 14978 | 0.1% | 0.1% | -0.1 | n/a | no target |
| P12 | 7 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P13 | 18028 | 0.4% | 0.4% | +0.0 | n/a | no target |

### `ap_phone`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 126 | 19.0% | 19.0% | -7.8 | n/a | no target |
| P01T | 370 | 23.8% | 23.8% | -0.3 | 70% | ❌ 46 pts to go |
| P01_GOLD | 625 | 43.4% | 43.4% | +0.1 | 80% | ❌ 37 pts to go |
| P02 | 470 | 56.2% | 56.2% | -0.6 | 90% | ❌ 34 pts to go |
| P03 | 257 | 19.1% | 19.1% | +0.0 | 60% | ❌ 41 pts to go |
| P04 | 3821 | 21.1% | 21.1% | -2.6 | 85% | ❌ 64 pts to go |
| P05 | 424 | 11.8% | 11.8% | -0.1 | 50% | ❌ 38 pts to go |
| P06M | 13001 | 0.3% | 0.3% | -0.1 | n/a | no target |
| P06T | 67038 | 0.6% | 0.6% | +0.0 | n/a | no target |
| P06 | 298 | 14.8% | 14.8% | -1.4 | n/a | no target |
| P07 | 801 | 11.7% | 11.7% | -1.3 | n/a | no target |
| P08 | 25648 | 0.4% | 0.4% | -0.1 | n/a | no target |
| P09 | 295 | 77.3% | 77.3% | -0.3 | 95% | ❌ 18 pts to go |
| P10R | 98583 | 0.2% | 0.2% | +0.0 | n/a | no target |
| P10 | 2685 | 1.7% | 1.7% | +0.0 | n/a | no target |
| P11 | 14978 | 2.3% | 2.3% | -1.3 | n/a | no target |
| P12 | 7 | 28.6% | 28.6% | +3.6 | n/a | no target |
| P13 | 18028 | 0.7% | 0.7% | +0.0 | n/a | no target |

### `invoice_mailing_address`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 126 | 5.6% | 5.6% | -1.6 | n/a | no target |
| P01T | 370 | 12.2% | 12.2% | +0.2 | n/a | no target |
| P01_GOLD | 625 | 33.9% | 33.9% | +0.0 | 70% | ❌ 36 pts to go |
| P02 | 470 | 38.5% | 38.5% | -0.4 | 75% | ❌ 36 pts to go |
| P03 | 257 | 19.1% | 19.1% | +0.0 | 55% | ❌ 36 pts to go |
| P04 | 3821 | 21.0% | 21.0% | -2.6 | 75% | ❌ 54 pts to go |
| P05 | 424 | 10.8% | 10.8% | +0.0 | 50% | ❌ 39 pts to go |
| P06M | 13001 | 0.1% | 0.1% | -0.1 | n/a | no target |
| P06T | 67038 | 0.3% | 0.3% | -0.1 | n/a | no target |
| P06 | 298 | 7.4% | 7.4% | -0.9 | n/a | no target |
| P07 | 801 | 5.6% | 5.6% | -0.8 | n/a | no target |
| P08 | 25648 | 0.2% | 0.2% | +0.0 | n/a | no target |
| P09 | 295 | 74.9% | 74.9% | -0.3 | 95% | ❌ 20 pts to go |
| P10R | 98583 | 0.1% | 0.1% | -0.1 | n/a | no target |
| P10 | 2685 | 1.0% | 1.0% | +0.0 | n/a | no target |
| P11 | 14978 | 2.3% | 2.3% | -1.3 | n/a | no target |
| P12 | 7 | 14.3% | 14.3% | +1.8 | n/a | no target |
| P13 | 18028 | 0.4% | 0.4% | +0.0 | n/a | no target |

### `invoicing_requirements`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 126 | 6.3% | 6.3% | +0.1 | n/a | no target |
| P01T | 370 | 8.4% | 8.4% | -0.9 | n/a | no target |
| P01_GOLD | 625 | 57.9% | 58.1% | -0.1 | 80% | ❌ 22 pts to go |
| P02 | 470 | 45.3% | 45.5% | -0.5 | 75% | ❌ 30 pts to go |
| P03 | 257 | 37.7% | 37.7% | -0.2 | 70% | ❌ 32 pts to go |
| P04 | 3821 | 20.6% | 21.0% | -2.5 | 70% | ❌ 49 pts to go |
| P05 | 424 | 14.2% | 14.2% | -0.1 | 50% | ❌ 36 pts to go |
| P06M | 13001 | 0.3% | 0.3% | -0.1 | n/a | no target |
| P06T | 67038 | 0.3% | 0.3% | +0.0 | n/a | no target |
| P06 | 298 | 13.1% | 13.1% | -0.3 | n/a | no target |
| P07 | 801 | 1.9% | 1.9% | -0.1 | n/a | no target |
| P08 | 25648 | 0.3% | 0.3% | -0.1 | n/a | no target |
| P09 | 295 | 46.1% | 46.4% | +0.2 | 80% | ❌ 34 pts to go |
| P10R | 98583 | 0.1% | 0.1% | +0.0 | n/a | no target |
| P10 | 2685 | 1.2% | 1.2% | +0.0 | n/a | no target |
| P11 | 14978 | 0.7% | 0.7% | -0.4 | n/a | no target |
| P12 | 7 | 42.9% | 42.9% | +5.4 | n/a | no target |
| P13 | 18028 | 0.3% | 0.3% | +0.0 | n/a | no target |

### `payment_terms_as_published`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 126 | 11.9% | 11.9% | +0.6 | n/a | no target |
| P01T | 370 | 19.5% | 19.5% | -2.5 | 60% | ❌ 40 pts to go |
| P01_GOLD | 625 | 63.5% | 63.5% | -0.1 | 70% | 🟡 6 pts to go |
| P02 | 470 | 38.5% | 38.5% | -0.4 | 50% | ❌ 12 pts to go |
| P03 | 257 | 49.8% | 49.8% | -0.2 | 55% | 🟡 5 pts to go |
| P04 | 3821 | 11.8% | 11.8% | -1.5 | 40% | ❌ 28 pts to go |
| P05 | 424 | 17.2% | 17.2% | -0.1 | 40% | ❌ 23 pts to go |
| P06M | 13001 | 0.5% | 0.5% | -0.2 | n/a | no target |
| P06T | 67038 | 2.2% | 2.2% | -0.2 | n/a | no target |
| P06 | 298 | 19.1% | 19.1% | -0.6 | n/a | no target |
| P07 | 801 | 6.0% | 6.0% | -0.7 | n/a | no target |
| P08 | 25648 | 2.2% | 2.2% | -0.4 | n/a | no target |
| P09 | 295 | 5.8% | 5.8% | -0.1 | n/a | no target |
| P10R | 98583 | 0.2% | 0.2% | +0.0 | n/a | no target |
| P10 | 2685 | 4.4% | 4.4% | -0.1 | n/a | no target |
| P11 | 14978 | 3.3% | 3.3% | -1.0 | n/a | no target |
| P12 | 7 | 0.0% | 0.0% | -12.5 | n/a | no target |
| P13 | 18028 | 0.2% | 0.2% | +0.0 | n/a | no target |

### `po_required_as_published`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 126 | 15.1% | 15.1% | -1.4 | n/a | no target |
| P01T | 370 | 23.0% | 23.0% | -2.3 | 65% | ❌ 42 pts to go |
| P01_GOLD | 625 | 69.0% | 69.0% | +0.0 | 70% | 🟡 1 pts to go |
| P02 | 470 | 23.6% | 23.6% | -0.3 | 50% | ❌ 26 pts to go |
| P03 | 257 | 52.1% | 52.1% | -0.2 | 60% | 🟡 8 pts to go |
| P04 | 3821 | 5.0% | 5.0% | -0.8 | 40% | ❌ 35 pts to go |
| P05 | 424 | 19.8% | 19.8% | +0.1 | 45% | ❌ 25 pts to go |
| P06M | 13001 | 0.3% | 0.3% | +0.0 | n/a | no target |
| P06T | 67038 | 0.5% | 0.5% | -0.1 | n/a | no target |
| P06 | 298 | 29.2% | 29.2% | -2.5 | n/a | no target |
| P07 | 801 | 6.1% | 6.1% | -0.8 | n/a | no target |
| P08 | 25648 | 0.9% | 0.9% | -0.2 | n/a | no target |
| P09 | 295 | 9.8% | 9.8% | -0.1 | n/a | no target |
| P10R | 98583 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P10 | 2685 | 2.6% | 2.6% | +0.0 | n/a | no target |
| P11 | 14978 | 0.7% | 0.7% | -0.3 | n/a | no target |
| P12 | 7 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P13 | 18028 | 0.2% | 0.2% | +0.0 | n/a | no target |

### `invoice_portal_url`

> ceiling: only portals the buyer names on its own pages; informational tax-authority links are not portals

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 126 | 4.8% | 4.8% | -1.4 | n/a | no target |
| P01T | 370 | 13.5% | 13.5% | -1.0 | n/a | no target |
| P01_GOLD | 625 | 49.8% | 49.8% | +0.0 | 50% | 🟡 0 pts to go |
| P02 | 470 | 37.0% | 37.0% | -0.4 | n/a | no target |
| P03 | 257 | 52.5% | 52.5% | -0.6 | 60% | 🟡 8 pts to go |
| P04 | 3821 | 11.5% | 11.5% | -1.4 | n/a | no target |
| P05 | 424 | 14.9% | 14.9% | -0.3 | n/a | no target |
| P06M | 13001 | 0.2% | 0.2% | -0.1 | n/a | no target |
| P06T | 67038 | 0.4% | 0.4% | -0.1 | n/a | no target |
| P06 | 298 | 21.1% | 21.1% | -0.6 | n/a | no target |
| P07 | 801 | 6.6% | 6.6% | -0.6 | n/a | no target |
| P08 | 25648 | 0.4% | 0.4% | -0.1 | n/a | no target |
| P09 | 295 | 18.3% | 18.3% | +0.1 | n/a | no target |
| P10R | 98583 | 0.1% | 0.1% | +0.0 | n/a | no target |
| P10 | 2685 | 2.3% | 2.3% | +0.0 | n/a | no target |
| P11 | 14978 | 0.5% | 0.5% | -0.3 | n/a | no target |
| P12 | 7 | 14.3% | 14.3% | +14.3 | n/a | no target |
| P13 | 18028 | 0.4% | 0.4% | +0.0 | n/a | no target |

### `buyer_payment_method_preference`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 126 | 10.3% | 10.3% | -1.0 | 15% | 🟡 5 pts to go |
| P01T | 370 | 11.1% | 11.1% | +0.0 | 15% | 🟡 4 pts to go |
| P01_GOLD | 625 | 35.4% | 35.4% | +0.1 | 40% | 🟡 5 pts to go |
| P02 | 470 | 12.6% | 12.8% | +0.1 | 25% | ❌ 12 pts to go |
| P03 | 257 | 17.9% | 17.9% | -0.1 | 25% | 🟡 7 pts to go |
| P04 | 3821 | 2.7% | 2.7% | -0.1 | 15% | ❌ 12 pts to go |
| P05 | 424 | 6.8% | 6.8% | +0.0 | 15% | 🟡 8 pts to go |
| P06M | 13001 | 0.6% | 0.6% | +0.0 | 15% | ❌ 14 pts to go |
| P06T | 67038 | 0.7% | 0.7% | +0.3 | 15% | ❌ 14 pts to go |
| P06 | 298 | 9.1% | 9.1% | -0.2 | 15% | 🟡 6 pts to go |
| P07 | 801 | 3.5% | 3.5% | +0.3 | 15% | ❌ 12 pts to go |
| P08 | 25648 | 0.5% | 0.5% | +0.1 | 15% | ❌ 14 pts to go |
| P09 | 295 | 1.0% | 1.0% | +0.0 | 15% | ❌ 14 pts to go |
| P10R | 98583 | 0.6% | 0.6% | +0.2 | 15% | ❌ 14 pts to go |
| P10 | 2685 | 1.3% | 1.3% | +0.3 | 15% | ❌ 14 pts to go |
| P11 | 14978 | 0.3% | 0.3% | +0.1 | 15% | ❌ 15 pts to go |
| P12 | 7 | 14.3% | 14.3% | +1.8 | 15% | 🟡 1 pts to go |
| P13 | 18028 | 0.5% | 0.5% | +0.1 | 15% | ❌ 14 pts to go |

### `buyer_tax_exempt_status`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 126 | 4.0% | 4.0% | -2.2 | 15% | ❌ 11 pts to go |
| P01T | 370 | 10.5% | 10.5% | -1.5 | 25% | ❌ 14 pts to go |
| P01_GOLD | 625 | 29.1% | 29.1% | -0.1 | 25% | ✅ met |
| P02 | 470 | 25.1% | 25.1% | -0.3 | 15% | ✅ met |
| P03 | 257 | 21.4% | 21.4% | -0.1 | 15% | ✅ met |
| P04 | 3821 | 3.6% | 3.6% | -0.5 | 15% | ❌ 11 pts to go |
| P05 | 424 | 10.8% | 10.8% | +0.0 | 15% | 🟡 4 pts to go |
| P06M | 13001 | 0.2% | 0.2% | +0.0 | 15% | ❌ 15 pts to go |
| P06T | 67038 | 0.3% | 0.3% | +0.0 | 15% | ❌ 15 pts to go |
| P06 | 298 | 7.7% | 7.7% | +0.1 | 15% | 🟡 7 pts to go |
| P07 | 801 | 2.7% | 2.7% | -0.4 | 15% | ❌ 12 pts to go |
| P08 | 25648 | 0.4% | 0.4% | +0.0 | 15% | ❌ 15 pts to go |
| P09 | 295 | 1.0% | 1.0% | +0.0 | 15% | ❌ 14 pts to go |
| P10R | 98583 | 0.0% | 0.0% | +0.0 | 15% | ❌ 15 pts to go |
| P10 | 2685 | 1.5% | 1.5% | -0.1 | 15% | ❌ 14 pts to go |
| P11 | 14978 | 0.4% | 0.4% | -0.1 | 15% | ❌ 15 pts to go |
| P12 | 7 | 28.6% | 28.6% | +3.6 | 15% | ✅ met |
| P13 | 18028 | 0.1% | 0.1% | +0.1 | 15% | ❌ 15 pts to go |

### `buyer_ap_cycle_published`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 126 | 0.0% | 0.0% | +0.0 | 20% | ❌ 20 pts to go |
| P01T | 370 | 3.8% | 3.8% | -0.1 | 20% | ❌ 16 pts to go |
| P01_GOLD | 625 | 4.5% | 4.5% | +0.2 | 20% | ❌ 16 pts to go |
| P02 | 470 | 1.3% | 1.3% | +0.0 | 20% | ❌ 19 pts to go |
| P03 | 257 | 1.6% | 1.6% | +0.0 | 20% | ❌ 18 pts to go |
| P04 | 3821 | 0.6% | 0.6% | +0.0 | 20% | ❌ 19 pts to go |
| P05 | 424 | 1.2% | 1.2% | +0.0 | 20% | ❌ 19 pts to go |
| P06M | 13001 | 0.0% | 0.0% | +0.0 | 20% | ❌ 20 pts to go |
| P06T | 67038 | 0.0% | 0.0% | +0.0 | 20% | ❌ 20 pts to go |
| P06 | 298 | 1.3% | 1.3% | -0.1 | 20% | ❌ 19 pts to go |
| P07 | 801 | 0.4% | 0.4% | +0.0 | 20% | ❌ 20 pts to go |
| P08 | 25648 | 0.0% | 0.0% | +0.0 | 20% | ❌ 20 pts to go |
| P09 | 295 | 0.0% | 0.0% | +0.0 | 20% | ❌ 20 pts to go |
| P10R | 98583 | 0.0% | 0.0% | +0.0 | 20% | ❌ 20 pts to go |
| P10 | 2685 | 0.3% | 0.3% | +0.0 | 20% | ❌ 20 pts to go |
| P11 | 14978 | 0.0% | 0.0% | +0.0 | 20% | ❌ 20 pts to go |
| P12 | 7 | 0.0% | 0.0% | +0.0 | 20% | ❌ 20 pts to go |
| P13 | 18028 | 0.0% | 0.0% | +0.0 | 20% | ❌ 20 pts to go |

### `buyer_esignature_preference`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 126 | 0.8% | 0.8% | -0.2 | 15% | ❌ 14 pts to go |
| P01T | 370 | 2.4% | 2.4% | +0.0 | 15% | ❌ 13 pts to go |
| P01_GOLD | 625 | 10.4% | 10.4% | -0.1 | 15% | 🟡 5 pts to go |
| P02 | 470 | 11.9% | 11.9% | -0.1 | 15% | 🟡 3 pts to go |
| P03 | 257 | 20.6% | 20.6% | -0.1 | 15% | ✅ met |
| P04 | 3821 | 2.1% | 2.1% | -0.3 | 15% | ❌ 13 pts to go |
| P05 | 424 | 2.8% | 2.8% | -0.2 | 15% | ❌ 12 pts to go |
| P06M | 13001 | 0.1% | 0.1% | -0.1 | 15% | ❌ 15 pts to go |
| P06T | 67038 | 0.2% | 0.2% | +0.0 | 15% | ❌ 15 pts to go |
| P06 | 298 | 5.0% | 5.0% | -0.2 | 15% | 🟡 10 pts to go |
| P07 | 801 | 1.6% | 1.6% | -0.1 | 15% | ❌ 13 pts to go |
| P08 | 25648 | 0.4% | 0.4% | +0.0 | 15% | ❌ 15 pts to go |
| P09 | 295 | 0.7% | 0.7% | +0.0 | 15% | ❌ 14 pts to go |
| P10R | 98583 | 0.0% | 0.0% | +0.0 | 15% | ❌ 15 pts to go |
| P10 | 2685 | 0.9% | 0.9% | +0.0 | 15% | ❌ 14 pts to go |
| P11 | 14978 | 0.2% | 0.2% | -0.1 | 15% | ❌ 15 pts to go |
| P12 | 7 | 0.0% | 0.0% | +0.0 | 15% | ❌ 15 pts to go |
| P13 | 18028 | 0.1% | 0.1% | +0.0 | 15% | ❌ 15 pts to go |

### `ap_system_hint`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 126 | 7.1% | 7.1% | -0.1 | 20% | ❌ 13 pts to go |
| P01T | 370 | 14.1% | 14.1% | -1.0 | 40% | ❌ 26 pts to go |
| P01_GOLD | 625 | 45.9% | 45.9% | +0.1 | 40% | ✅ met |
| P02 | 470 | 42.3% | 42.3% | -0.5 | 20% | ✅ met |
| P03 | 257 | 48.6% | 48.6% | -0.2 | 35% | ✅ met |
| P04 | 3821 | 13.7% | 13.7% | -1.7 | 20% | 🟡 6 pts to go |
| P05 | 424 | 14.9% | 14.9% | +0.1 | 20% | 🟡 5 pts to go |
| P06M | 13001 | 0.4% | 0.4% | -0.1 | 20% | ❌ 20 pts to go |
| P06T | 67038 | 0.7% | 0.7% | +0.0 | 20% | ❌ 19 pts to go |
| P06 | 298 | 21.8% | 21.8% | -0.3 | 20% | ✅ met |
| P07 | 801 | 6.9% | 6.9% | -0.2 | 20% | ❌ 13 pts to go |
| P08 | 25648 | 0.8% | 0.8% | -0.1 | 20% | ❌ 19 pts to go |
| P09 | 295 | 18.3% | 18.3% | +0.1 | 20% | 🟡 2 pts to go |
| P10R | 98583 | 0.2% | 0.2% | +0.0 | 20% | ❌ 20 pts to go |
| P10 | 2685 | 3.4% | 3.4% | +0.0 | 20% | ❌ 17 pts to go |
| P11 | 14978 | 0.7% | 0.7% | -0.3 | 20% | ❌ 19 pts to go |
| P12 | 7 | 0.0% | 0.0% | +0.0 | 20% | ❌ 20 pts to go |
| P13 | 18028 | 0.6% | 0.6% | +0.1 | 20% | ❌ 19 pts to go |

## 5. contract

### `contract_value`

> ceiling: rows proven by a lobbying filing, a news release, an auditor appointment, a customer story or a vendor's client list have no contract value by nature (≈17 % of P01 Gold); bids&tenders awards now carry the awarded bidder's submitted price when no award value was published

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 126 | 33.3% | 33.3% | -11.0 | n/a | no target |
| P01T | 370 | 0.3% | 0.3% | +0.0 | n/a | no target |
| P01_GOLD | 625 | 69.4% | 69.4% | -0.1 | 95% | ❌ 26 pts to go |
| P02 | 470 | 62.3% | 62.3% | -0.7 | 95% | ❌ 33 pts to go |
| P03 | 257 | 54.5% | 54.5% | -0.2 | 90% | ❌ 36 pts to go |
| P04 | 3821 | 24.2% | 24.2% | -2.9 | 85% | ❌ 61 pts to go |
| P05 | 424 | 37.3% | 37.3% | +0.8 | 75% | ❌ 38 pts to go |
| P06M | 13001 | 35.6% | 35.6% | -14.5 | n/a | no target |
| P06T | 67038 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06 | 298 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P07 | 801 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P08 | 25648 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P09 | 295 | 89.5% | 89.5% | +0.1 | 100% | ❌ 10 pts to go |
| P10R | 98583 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P10 | 2685 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P11 | 14978 | 0.6% | 0.6% | -0.3 | 60% | ❌ 59 pts to go |
| P12 | 7 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P13 | 18028 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `currency`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 126 | 33.3% | 33.3% | -11.0 | n/a | no target |
| P01T | 370 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P01_GOLD | 625 | 72.8% | 72.8% | +0.0 | 100% | ❌ 27 pts to go |
| P02 | 470 | 65.7% | 65.7% | -0.8 | 100% | ❌ 34 pts to go |
| P03 | 257 | 60.3% | 60.3% | -0.2 | n/a | no target |
| P04 | 3821 | 24.8% | 24.8% | -3.0 | 95% | ❌ 70 pts to go |
| P05 | 424 | 33.3% | 33.3% | +0.3 | 80% | ❌ 47 pts to go |
| P06M | 13001 | 35.6% | 35.6% | -14.5 | n/a | no target |
| P06T | 67038 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06 | 298 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P07 | 801 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P08 | 25648 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P09 | 295 | 92.5% | 92.5% | -0.2 | 100% | 🟡 8 pts to go |
| P10R | 98583 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P10 | 2685 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P11 | 14978 | 0.6% | 0.6% | -0.4 | n/a | no target |
| P12 | 7 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P13 | 18028 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `start_date`

> ceiling: most award notices publish an award date, not a start date; start_date carries the signature date when the source gives one, labelled

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 126 | 81.0% | 81.0% | +2.6 | n/a | no target |
| P01T | 370 | 0.3% | 0.3% | +0.0 | n/a | no target |
| P01_GOLD | 625 | 51.7% | 51.7% | +0.1 | 85% | ❌ 33 pts to go |
| P02 | 470 | 57.0% | 57.0% | -0.6 | 90% | ❌ 33 pts to go |
| P03 | 257 | 44.0% | 44.0% | -0.1 | 85% | ❌ 41 pts to go |
| P04 | 3821 | 27.2% | 27.2% | -3.2 | 90% | ❌ 63 pts to go |
| P05 | 424 | 33.3% | 33.3% | +0.5 | 75% | ❌ 42 pts to go |
| P06M | 13001 | 89.7% | 89.7% | -0.7 | n/a | no target |
| P06T | 67038 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06 | 298 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P07 | 801 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P08 | 25648 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P09 | 295 | 85.1% | 85.1% | +0.0 | 95% | 🟡 10 pts to go |
| P10R | 98583 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P10 | 2685 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P11 | 14978 | 0.5% | 0.5% | -0.3 | n/a | no target |
| P12 | 7 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P13 | 18028 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `end_date`

> ceiling: an inferred end (award date + published duration) is labelled as such; sources without a duration leave end_date empty — the honest ceiling. P09 is BY DEFINITION the rows whose end date is not published (older SEAO contracts with no closing notice): its end_date / duration targets cannot be met without inventing a date

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 126 | 80.2% | 80.2% | +0.8 | n/a | no target |
| P01T | 370 | 0.3% | 0.3% | +0.0 | n/a | no target |
| P01_GOLD | 625 | 51.8% | 51.8% | +0.0 | 85% | ❌ 33 pts to go |
| P02 | 470 | 52.1% | 52.1% | -0.6 | 90% | ❌ 38 pts to go |
| P03 | 257 | 45.1% | 45.1% | -0.2 | 85% | ❌ 40 pts to go |
| P04 | 3821 | 23.2% | 23.2% | -2.8 | 90% | ❌ 67 pts to go |
| P05 | 424 | 43.6% | 43.6% | +0.7 | 75% | ❌ 31 pts to go |
| P06M | 13001 | 80.4% | 80.4% | -3.3 | n/a | no target |
| P06T | 67038 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06 | 298 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P07 | 801 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P08 | 25648 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P09 | 295 | 0.3% | 0.3% | +0.0 | 95% | ❌ 95 pts to go |
| P10R | 98583 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P10 | 2685 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P11 | 14978 | 0.4% | 0.4% | -0.3 | n/a | no target |
| P12 | 7 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P13 | 18028 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `contract_title`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 126 | 89.7% | 89.7% | +4.1 | n/a | no target |
| P01T | 370 | 91.4% | 91.4% | -0.8 | n/a | no target |
| P01_GOLD | 625 | 85.4% | 85.4% | -0.1 | 100% | ❌ 15 pts to go |
| P02 | 470 | 74.9% | 74.9% | -0.8 | 100% | ❌ 25 pts to go |
| P03 | 257 | 91.4% | 91.4% | -0.8 | n/a | no target |
| P04 | 3821 | 45.8% | 45.8% | -5.7 | 95% | ❌ 49 pts to go |
| P05 | 424 | 77.4% | 77.4% | -0.4 | 95% | ❌ 18 pts to go |
| P06M | 13001 | 98.8% | 98.8% | +0.5 | n/a | no target |
| P06T | 67038 | 82.3% | 82.3% | -1.4 | n/a | no target |
| P06 | 298 | 25.5% | 25.5% | -0.7 | n/a | no target |
| P07 | 801 | 17.1% | 17.1% | -2.0 | n/a | no target |
| P08 | 25648 | 9.8% | 9.8% | -1.2 | n/a | no target |
| P09 | 295 | 98.6% | 98.6% | -0.1 | 100% | 🟡 1 pts to go |
| P10R | 98583 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P10 | 2685 | 71.5% | 71.5% | -0.2 | n/a | no target |
| P11 | 14978 | 10.8% | 10.8% | -5.3 | n/a | no target |
| P12 | 7 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P13 | 18028 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `contract_description`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 126 | 89.7% | 89.7% | +4.1 | n/a | no target |
| P01T | 370 | 91.4% | 91.4% | -0.8 | n/a | no target |
| P01_GOLD | 625 | 88.6% | 88.6% | -0.1 | 100% | ❌ 11 pts to go |
| P02 | 470 | 76.0% | 76.2% | -0.8 | 100% | ❌ 24 pts to go |
| P03 | 257 | 92.2% | 92.2% | -0.8 | n/a | no target |
| P04 | 3821 | 49.0% | 49.0% | -6.1 | 95% | ❌ 46 pts to go |
| P05 | 424 | 89.9% | 89.9% | -0.3 | 70% | ✅ met |
| P06M | 13001 | 98.8% | 98.8% | +0.5 | n/a | no target |
| P06T | 67038 | 82.3% | 82.3% | -1.4 | n/a | no target |
| P06 | 298 | 25.5% | 25.5% | -0.7 | n/a | no target |
| P07 | 801 | 17.1% | 17.1% | -2.0 | n/a | no target |
| P08 | 25648 | 9.8% | 9.8% | -1.2 | n/a | no target |
| P09 | 295 | 98.6% | 98.6% | -0.1 | 100% | 🟡 1 pts to go |
| P10R | 98583 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P10 | 2685 | 71.5% | 71.5% | -0.2 | n/a | no target |
| P11 | 14978 | 10.8% | 10.8% | -5.3 | n/a | no target |
| P12 | 7 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P13 | 18028 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `number_of_bids`

> ceiling: published by some portals only (bids&tenders submission lists, Biddingo bidder lists); federal proactive disclosure does not publish bid counts

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 126 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P01T | 370 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P01_GOLD | 625 | 16.8% | 16.8% | +0.0 | 60% | ❌ 43 pts to go · rows from a source that publishes bids: 363 rows, 28.9% filled |
| P02 | 470 | 11.1% | 11.1% | -0.1 | n/a | no target · rows from a source that publishes bids: 290 rows, 17.9% filled |
| P03 | 257 | 13.2% | 13.2% | -0.1 | n/a | no target · rows from a source that publishes bids: 139 rows, 24.5% filled |
| P04 | 3821 | 1.4% | 1.4% | -0.2 | n/a | no target · rows from a source that publishes bids: 872 rows, 6.3% filled |
| P05 | 424 | 2.8% | 2.8% | -0.2 | n/a | no target · rows from a source that publishes bids: 51 rows, 23.5% filled |
| P06M | 13001 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06T | 67038 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06 | 298 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P07 | 801 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P08 | 25648 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P09 | 295 | 3.1% | 3.1% | +0.1 | n/a | no target · rows from a source that publishes bids: 282 rows, 3.2% filled |
| P10R | 98583 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P10 | 2685 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P11 | 14978 | 0.1% | 0.1% | +0.0 | n/a | no target · rows from a source that publishes bids: 88 rows, 13.6% filled |
| P12 | 7 | 0.0% | 0.0% | +0.0 | n/a | no target · rows from a source that publishes bids: 7 rows, 0.0% filled |
| P13 | 18028 | 0.0% | 0.0% | +0.0 | n/a | no target |

## 6. history

### `average_contract_duration_days`

> ceiling: needs two dates (or a published term) on the buyer's records; P09 rows (end date unpublished by definition) and buyers whose sources publish award dates only have no honest duration

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 126 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P01T | 370 | 0.3% | 98.4% | +0.0 | n/a | no target |
| P01_GOLD | 625 | 53.3% | 82.4% | +0.1 | 90% | ❌ 37 pts to go |
| P02 | 470 | 51.9% | 87.7% | -0.6 | 90% | ❌ 38 pts to go |
| P03 | 257 | 45.5% | 80.2% | -0.2 | 90% | ❌ 44 pts to go |
| P04 | 3821 | 18.7% | 94.1% | -2.2 | 90% | ❌ 71 pts to go |
| P05 | 424 | 0.0% | 83.3% | +0.0 | 90% | ❌ 90 pts to go |
| P06M | 13001 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P06T | 67038 | 0.0% | 99.9% | +0.0 | n/a | no target |
| P06 | 298 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P07 | 801 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P08 | 25648 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P09 | 295 | 2.4% | 4.1% | +0.1 | 90% | ❌ 88 pts to go |
| P10R | 98583 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P10 | 2685 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P11 | 14978 | 0.4% | 99.7% | -0.2 | n/a | no target |
| P12 | 7 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P13 | 18028 | 0.0% | 100.0% | +0.0 | n/a | no target |

### `commodity_distribution_top3`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 126 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P01T | 370 | 0.5% | 98.6% | -0.1 | n/a | no target |
| P01_GOLD | 625 | 25.9% | 55.0% | +0.0 | 90% | ❌ 64 pts to go |
| P02 | 470 | 51.1% | 86.8% | -0.5 | n/a | no target |
| P03 | 257 | 24.9% | 59.5% | -0.1 | n/a | no target |
| P04 | 3821 | 20.4% | 95.8% | -2.5 | n/a | no target |
| P05 | 424 | 0.5% | 83.7% | +0.0 | n/a | no target |
| P06M | 13001 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P06T | 67038 | 0.1% | 99.9% | +0.0 | n/a | no target |
| P06 | 298 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P07 | 801 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P08 | 25648 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P09 | 295 | 41.4% | 43.1% | -0.5 | n/a | no target |
| P10R | 98583 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P10 | 2685 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P11 | 14978 | 0.4% | 99.7% | -0.2 | n/a | no target |
| P12 | 7 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P13 | 18028 | 0.0% | 100.0% | +0.0 | n/a | no target |

### `year_over_year_spend_trend`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 126 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P01T | 370 | 1.6% | 99.7% | +0.1 | n/a | no target |
| P01_GOLD | 625 | 51.8% | 81.0% | +0.0 | 95% | ❌ 43 pts to go |
| P02 | 470 | 56.0% | 91.7% | -0.6 | n/a | no target |
| P03 | 257 | 47.9% | 82.5% | -0.1 | n/a | no target |
| P04 | 3821 | 20.6% | 96.0% | -2.5 | n/a | no target |
| P05 | 424 | 4.5% | 87.7% | -0.2 | n/a | no target |
| P06M | 13001 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P06T | 67038 | 0.1% | 100.0% | +0.0 | n/a | no target |
| P06 | 298 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P07 | 801 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P08 | 25648 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P09 | 295 | 63.7% | 65.4% | -0.3 | n/a | no target |
| P10R | 98583 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P10 | 2685 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P11 | 14978 | 0.4% | 99.7% | -0.2 | n/a | no target |
| P12 | 7 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P13 | 18028 | 0.0% | 100.0% | +0.0 | n/a | no target |

## 7. mail security

### `mta_sts`

> ceiling: DNS-only check; 'no record' counts as checked

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 126 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P01T | 370 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P01_GOLD | 625 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P02 | 470 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P03 | 257 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P04 | 3821 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P05 | 424 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P06M | 13001 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P06T | 67038 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P06 | 298 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P07 | 801 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P08 | 25648 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P09 | 295 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P10R | 98583 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P10 | 2685 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P11 | 14978 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P12 | 7 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P13 | 18028 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |

### `tls_rpt`

> ceiling: DNS-only check; 'no record' counts as checked

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 126 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P01T | 370 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P01_GOLD | 625 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P02 | 470 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P03 | 257 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P04 | 3821 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P05 | 424 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P06M | 13001 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P06T | 67038 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P06 | 298 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P07 | 801 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P08 | 25648 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P09 | 295 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P10R | 98583 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P10 | 2685 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P11 | 14978 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P12 | 7 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P13 | 18028 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |

### `bimi`

> ceiling: DNS-only check; 'no record' counts as checked

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 126 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P01T | 370 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P01_GOLD | 625 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P02 | 470 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P03 | 257 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P04 | 3821 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P05 | 424 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P06M | 13001 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P06T | 67038 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P06 | 298 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P07 | 801 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P08 | 25648 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P09 | 295 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P10R | 98583 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P10 | 2685 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P11 | 14978 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P12 | 7 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P13 | 18028 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |

