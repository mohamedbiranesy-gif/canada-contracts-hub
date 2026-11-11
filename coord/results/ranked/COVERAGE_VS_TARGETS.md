# Coverage vs the downstream team's targets — 2026-11-11

Benchmarks (field × package with a numeric target): **58 of 446 met** (13.0%); 90 within 10 points; 298 further away.
A cell counts as filled only when it carries a value: blank, `not_published`, `not_found_yet` and label-only cells ("no identifier published …", "no dataset record …", "0 in the contract dataset …") do not count; the DNS checks count when checked. `any` = share of non-blank cells incl. such labels. Δ = change since the previous build in `coord/results/coverage_history.csv`.
Rows per package: P01M 106, P01T 366, P01_GOLD 625, P02 470, P03 257, P04 3818, P05 423, P06M 11132, P06T 65815, P06 298, P07 800, P08 25619, P09 295, P10R 97211, P10 2658, P11 12828, P12 7, P13 17816

## Invoice-grade readiness (the row as an invoice header: bill-to, submit-to, references, terms, tax, vendor identity, follow-up)

| package | rows | all 11 elements | ≥ 9 of 11 | median elements | most-missing element |
|---|---|---|---|---|---|
| P01M | 106 | 0.0% | 15.1% | 8 | vendor GST/HST number (94 rows) |
| P01T | 366 | 0.8% | 20.5% | 7 | payment terms (292 rows) |
| P01_GOLD | 625 | 24.0% | 70.7% | 9 | payment terms (214 rows) |
| P02 | 470 | 7.2% | 54.3% | 9 | PO rule (359 rows) |
| P03 | 257 | 14.8% | 58.0% | 9 | PO rule (123 rows) |
| P04 | 3818 | 1.2% | 15.9% | 6 | PO rule (3624 rows) |
| P05 | 423 | 1.2% | 17.0% | 7 | payment terms (348 rows) |
| P06M | 11132 | 0.0% | 1.4% | 7 | PO rule (11101 rows) |
| P06T | 65815 | 0.0% | 3.5% | 7 | PO rule (65467 rows) |
| P06 | 298 | 0.0% | 8.1% | 6 | reference to quote (PO / contract / vendor id) (298 rows) |
| P07 | 800 | 0.0% | 1.6% | 5 | reference to quote (PO / contract / vendor id) (800 rows) |
| P08 | 25619 | 0.0% | 0.3% | 5 | reference to quote (PO / contract / vendor id) (25619 rows) |
| P09 | 295 | 1.0% | 44.4% | 8 | payment terms (276 rows) |
| P10R | 97211 | 0.0% | 20.4% | 7 | PO rule (97172 rows) |
| P10 | 2658 | 0.0% | 0.9% | 5 | reference to quote (PO / contract / vendor id) (2658 rows) |
| P11 | 12828 | 0.0% | 1.9% | 6 | PO rule (12728 rows) |
| P12 | 7 | 0.0% | 28.6% | 8 | PO rule (7 rows) |
| P13 | 17816 | 0.0% | 0.0% | 6 | reference to quote (PO / contract / vendor id) (17816 rows) |

## AP grade (how stringently the row's accounts-payable data meets what an invoice needs; A = invoicing mailbox referee-confirmed on the buyer's own domain with MX, legal name, address, PO rule and terms all published, no penalties)

| package | rows | A | B | C | D | E | median ap_score |
|---|---|---|---|---|---|---|---|
| P01M | 106 | 10 | 8 | 88 | 0 | 0 | 71 |
| P01T | 366 | 30 | 60 | 276 | 0 | 0 | 70 |
| P01_GOLD | 625 | 226 | 191 | 208 | 0 | 0 | 82 |
| P02 | 470 | 0 | 192 | 278 | 0 | 0 | 66 |
| P03 | 257 | 0 | 0 | 245 | 12 | 0 | 57 |
| P04 | 3818 | 0 | 0 | 3126 | 692 | 0 | 46 |
| P05 | 423 | 15 | 29 | 365 | 14 | 0 | 51 |
| P06M | 11132 | 0 | 3 | 11072 | 57 | 0 | 46 |
| P06T | 65815 | 0 | 41 | 54465 | 11309 | 0 | 38 |
| P06 | 298 | 20 | 45 | 233 | 0 | 0 | 68 |
| P07 | 800 | 0 | 25 | 748 | 27 | 0 | 52 |
| P08 | 25619 | 0 | 0 | 21437 | 4182 | 0 | 38 |
| P09 | 295 | 3 | 12 | 278 | 2 | 0 | 53 |
| P10R | 97211 | 2 | 11 | 67660 | 29538 | 0 | 38 |
| P10 | 2658 | 2 | 14 | 1984 | 658 | 0 | 43 |
| P11 | 12828 | 6 | 10 | 42 | 0 | 12770 | 23 |
| P12 | 7 | 0 | 0 | 7 | 0 | 0 | 54 |
| P13 | 17816 | 0 | 15 | 14494 | 3307 | 0 | 43 |

### AP payability (confirmed channel + bill-to legal name and address + the buyer's reference rule + tax treatment known)

| package | rows | payable today | % | most common gap |
|---|---|---|---|---|
| P01M | 106 | 85 | 80.2% | bill-to legal name and address (9) |
| P01T | 366 | 191 | 52.2% | bill-to legal name and address (131) |
| P01_GOLD | 625 | 464 | 74.2% | bill-to legal name and address (107) |
| P02 | 470 | 312 | 66.4% | the buyer's PO / reference rule (85) |
| P03 | 257 | 0 | 0.0% | a confirmed invoicing / AP or finance channel (257) |
| P04 | 3818 | 0 | 0.0% | a confirmed invoicing / AP or finance channel (3818) |
| P05 | 423 | 46 | 10.9% | a confirmed invoicing / AP or finance channel (337) |
| P06M | 11132 | 112 | 1.0% | a confirmed invoicing / AP or finance channel (10977) |
| P06T | 65815 | 395 | 0.6% | a confirmed invoicing / AP or finance channel (64837) |
| P06 | 298 | 43 | 14.4% | bill-to legal name and address (126) |
| P07 | 800 | 10 | 1.2% | bill-to legal name and address (369) |
| P08 | 25619 | 0 | 0.0% | a confirmed invoicing / AP or finance channel (25619) |
| P09 | 295 | 41 | 13.9% | a confirmed invoicing / AP or finance channel (245) |
| P10R | 97211 | 479 | 0.5% | a confirmed invoicing / AP or finance channel (96093) |
| P10 | 2658 | 4 | 0.2% | a confirmed invoicing / AP or finance channel (2563) |
| P11 | 12828 | 11 | 0.1% | a confirmed invoicing / AP or finance channel (12770) |
| P12 | 7 | 3 | 42.9% | a confirmed invoicing / AP or finance channel (4) |
| P13 | 17816 | 7 | 0.0% | a confirmed invoicing / AP or finance channel (17475) |

### Pay on sight (an invoice generated from the row would clear AP: confirmed invoicing / AP or finance channel, bill-to legal name + address, vendor legal name + GST/HST number + remit-to address, tax treatment and currency known — published or labelled-derived; the buyer's reference rule is reported separately)

| package | rows | pay on sight | % | + reference rule not published | routed (general inbox only) | most common gap |
|---|---|---|---|---|---|---|
| P01M | 106 | 6 | 5.7% | 5 | 0 | the vendor's GST/HST number (BN9) (93) |
| P01T | 366 | 66 | 18.0% | 23 | 0 | the vendor's GST/HST number (BN9) (205) |
| P01_GOLD | 625 | 396 | 63.4% | 12 | 0 | the vendor's GST/HST number (BN9) (154) |
| P02 | 470 | 211 | 44.9% | 23 | 0 | the vendor's GST/HST number (BN9) (206) |
| P03 | 257 | 16 | 6.2% | 0 | 132 | an invoicing / AP or finance mailbox (only a purchasing / general inbo (88) |
| P04 | 3818 | 42 | 1.1% | 8 | 783 | an invoicing / AP or finance mailbox (only a purchasing / general inbo (2927) |
| P05 | 423 | 20 | 4.7% | 8 | 111 | an invoicing / AP or finance mailbox (only a purchasing / general inbo (219) |
| P06M | 11132 | 1 | 0.0% | 10 | 145 | an invoicing / AP or finance mailbox (only a purchasing / general inbo (10812) |
| P06T | 65815 | 95 | 0.1% | 95 | 11242 | an invoicing / AP or finance mailbox (only a purchasing / general inbo (53438) |
| P06 | 298 | 16 | 5.4% | 31 | 0 | the vendor's GST/HST number (BN9) (173) |
| P07 | 800 | 4 | 0.5% | 67 | 27 | the vendor's GST/HST number (BN9) (432) |
| P08 | 25619 | 1 | 0.0% | 8 | 2647 | an invoicing / AP or finance mailbox (only a purchasing / general inbo (22909) |
| P09 | 295 | 38 | 12.9% | 1 | 119 | an invoicing / AP or finance mailbox (only a purchasing / general inbo (117) |
| P10R | 97211 | 827 | 0.9% | 0 | 52502 | an invoicing / AP or finance mailbox (only a purchasing / general inbo (43530) |
| P10 | 2658 | 4 | 0.2% | 20 | 389 | an invoicing / AP or finance mailbox (only a purchasing / general inbo (2144) |
| P11 | 12828 | 11 | 0.1% | 12 | 0 | a confirmed invoicing / AP or finance channel (12737) |
| P12 | 7 | 1 | 14.3% | 0 | 2 | the vendor's GST/HST number (BN9) (2) |
| P13 | 17816 | 9 | 0.1% | 246 | 10490 | an invoicing / AP or finance mailbox (only a purchasing / general inbo (6945) |
| **all** | 240544 | 1764 | 0.7% | 569 | 78589 | |

### What still blocks grade A (rows per missing element; a row counts under every element it lacks)

| package | rows not A | referee confirmation of the mailbox | an invoicing / AP mailbox (not finance / procurement / general) | a mailbox on the buyer's own domain | MX record for the mailbox domain | published bill-to legal name | invoice / billing address | published PO rule | published payment terms | clear the penalty |
|---|---|---|---|---|---|---|---|---|---|---|
| P01M | 96 | 0 | 0 | 0 | 39 | 9 | 0 | 89 | 93 | 0 |
| P01T | 336 | 0 | 0 | 0 | 151 | 117 | 32 | 281 | 294 | 31 |
| P01_GOLD | 399 | 0 | 0 | 0 | 11 | 90 | 33 | 194 | 228 | 57 |
| P02 | 470 | 0 | 470 | 0 | 46 | 63 | 19 | 359 | 289 | 22 |
| P03 | 257 | 0 | 257 | 0 | 14 | 43 | 25 | 123 | 129 | 25 |
| P04 | 3818 | 0 | 3818 | 0 | 1786 | 1653 | 953 | 3624 | 3364 | 130 |
| P05 | 408 | 0 | 356 | 0 | 72 | 96 | 48 | 339 | 350 | 50 |
| P06M | 11132 | 0 | 11132 | 0 | 6332 | 1133 | 106 | 11101 | 11065 | 35 |
| P06T | 65815 | 0 | 65815 | 0 | 50696 | 38048 | 14699 | 65467 | 64367 | 402 |
| P06 | 278 | 0 | 0 | 0 | 120 | 111 | 51 | 211 | 241 | 4 |
| P07 | 800 | 0 | 800 | 0 | 471 | 410 | 137 | 751 | 752 | 14 |
| P08 | 25619 | 0 | 25619 | 0 | 18799 | 14513 | 5385 | 25380 | 25046 | 226 |
| P09 | 292 | 0 | 271 | 0 | 9 | 68 | 2 | 266 | 278 | 44 |
| P10R | 97209 | 0 | 97039 | 0 | 74939 | 63210 | 38178 | 97172 | 97024 | 24 |
| P10 | 2656 | 0 | 2620 | 0 | 1257 | 1407 | 919 | 2589 | 2540 | 113 |
| P11 | 12822 | 12770 | 12711 | 0 | 11406 | 8865 | 946 | 12728 | 12369 | 39 |
| P12 | 7 | 0 | 6 | 0 | 0 | 2 | 0 | 7 | 7 | 0 |
| P13 | 17816 | 0 | 17713 | 0 | 8853 | 9690 | 4074 | 17780 | 17775 | 20 |

## Where the work is (largest gaps in rows still needed)

| field | package | now | target | rows needed |
|---|---|---|---|---|
| buyer_ap_cycle_published | P10R | 0.0% | 20% | 19417 |
| ap_system_hint | P10R | 0.2% | 20% | 19245 |
| vendor_registered_address | P08 | 12.6% | 70% | 14699 |
| buyer_tax_exempt_status | P10R | 0.0% | 15% | 14552 |
| buyer_esignature_preference | P10R | 0.0% | 15% | 14535 |
| buyer_payment_method_preference | P10R | 0.7% | 15% | 13948 |
| buyer_ap_cycle_published | P06T | 0.0% | 20% | 13140 |
| ap_system_hint | P06T | 0.7% | 20% | 12703 |
| buyer_phone | P08 | 56.9% | 95% | 9759 |
| buyer_esignature_preference | P06T | 0.2% | 15% | 9730 |
| buyer_tax_exempt_status | P06T | 0.3% | 15% | 9686 |
| buyer_payment_method_preference | P06T | 0.7% | 15% | 9439 |
| vendor_bn9 | P08 | 14.5% | 50% | 9105 |
| vendor_phone | P11 | 5.6% | 75% | 8907 |
| vendor_emails | P11 | 4.1% | 70% | 8459 |
| buyer_legal_name_as_published | P08 | 43.4% | 75% | 8109 |
| contract_value | P11 | 0.7% | 60% | 7613 |
| award_or_notice_id | P11 | 0.7% | 60% | 7612 |
| buyer_phone | P13 | 57.8% | 95% | 6623 |
| buyer_logo_url | P08 | 74.2% | 100% | 6605 |
| contract_or_agreement_number | P11 | 10.0% | 60% | 6410 |
| vendor_phone | P08 | 60.0% | 85% | 6393 |
| commodity_codes | P11 | 0.5% | 50% | 6353 |
| invoice_reference_hint | P11 | 10.7% | 60% | 6327 |
| invoice_reference_hint | P08 | 0.9% | 25% | 6166 |
| vendor_emails | P08 | 51.0% | 75% | 6161 |
| buyer_phone | P11 | 28.9% | 75% | 5920 |
| buyer_bn_as_published | P08 | 13.8% | 35% | 5425 |
| buyer_logo_url | P13 | 65.0% | 95% | 5338 |
| buyer_ap_cycle_published | P08 | 0.0% | 20% | 5116 |
| solicitation_or_tender_number | P11 | 0.6% | 40% | 5054 |
| ap_system_hint | P08 | 0.8% | 20% | 4915 |
| vendor_trading_name | P08 | 31.3% | 50% | 4797 |
| vendor_logo_url | P08 | 82.9% | 100% | 4384 |
| buyer_legal_name_as_published | P11 | 30.9% | 65% | 4376 |
| buyer_address | P08 | 79.0% | 95% | 4110 |
| buyer_esignature_preference | P08 | 0.4% | 15% | 3752 |
| buyer_tax_exempt_status | P08 | 0.4% | 15% | 3748 |
| buyer_payment_method_preference | P08 | 0.5% | 15% | 3705 |
| buyer_ap_cycle_published | P13 | 0.0% | 20% | 3562 |

## 1. identifiers

### `invoice_reference_hint`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 106 | 90.6% | 90.6% | +1.9 | 50% | ✅ met |
| P01T | 366 | 89.3% | 89.3% | -0.2 | 50% | ✅ met |
| P01_GOLD | 625 | 92.2% | 94.4% | +0.0 | 95% | 🟡 3 pts to go |
| P02 | 470 | 73.0% | 74.5% | -0.8 | 95% | ❌ 22 pts to go |
| P03 | 257 | 81.7% | 84.8% | -0.3 | 95% | ❌ 13 pts to go |
| P04 | 3818 | 29.2% | 30.6% | -3.6 | 90% | ❌ 61 pts to go |
| P05 | 423 | 38.5% | 41.6% | -0.1 | 70% | ❌ 32 pts to go |
| P06M | 11132 | 91.7% | 91.7% | -0.9 | n/a | no target |
| P06T | 65815 | 80.4% | 80.4% | +0.1 | n/a | no target |
| P06 | 298 | 29.2% | 29.2% | -2.5 | 30% | 🟡 1 pts to go |
| P07 | 800 | 6.1% | 6.1% | -0.8 | 30% | ❌ 24 pts to go |
| P08 | 25619 | 0.9% | 0.9% | -0.2 | 25% | ❌ 24 pts to go |
| P09 | 295 | 99.0% | 99.7% | +0.0 | 100% | 🟡 1 pts to go |
| P10R | 97211 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P10 | 2658 | 2.6% | 2.6% | +0.0 | 25% | ❌ 22 pts to go |
| P11 | 12828 | 10.7% | 10.8% | -2.9 | 60% | ❌ 49 pts to go |
| P12 | 7 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P13 | 17816 | 0.2% | 0.2% | +0.0 | 0% by design | — leave (by design) |

### `po_number_as_published`

> ceiling: a purchase-order number exists only where the buyer publishes PO-level data (Montréal, Laval, Toronto open data so far) or the record itself carries one; most sources publish awards, not POs — the target cannot be reached from public data for most buyers

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 106 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P01T | 366 | 0.0% | 0.0% | +0.0 | 10% | 🟡 10 pts to go |
| P01_GOLD | 625 | 6.1% | 6.1% | +0.0 | 50% | ❌ 44 pts to go |
| P02 | 470 | 6.2% | 6.2% | +0.0 | 50% | ❌ 44 pts to go |
| P03 | 257 | 1.6% | 1.6% | +0.0 | 40% | ❌ 38 pts to go |
| P04 | 3818 | 0.5% | 0.5% | +0.0 | 30% | ❌ 30 pts to go |
| P05 | 423 | 0.2% | 0.2% | +0.0 | 20% | ❌ 20 pts to go |
| P06M | 11132 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06T | 65815 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06 | 298 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P07 | 800 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P08 | 25619 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P09 | 295 | 0.7% | 0.7% | +0.0 | 50% | ❌ 49 pts to go |
| P10R | 97211 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P10 | 2658 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P11 | 12828 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P12 | 7 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P13 | 17816 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `contract_or_agreement_number`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 106 | 84.0% | 84.0% | +2.6 | n/a | no target |
| P01T | 366 | 72.1% | 72.1% | +1.6 | 50% | ✅ met |
| P01_GOLD | 625 | 66.9% | 66.9% | +0.0 | 85% | ❌ 18 pts to go |
| P02 | 470 | 64.3% | 64.3% | -0.6 | 90% | ❌ 26 pts to go |
| P03 | 257 | 61.1% | 61.1% | -0.2 | 85% | ❌ 24 pts to go |
| P04 | 3818 | 26.9% | 26.9% | -3.2 | 85% | ❌ 58 pts to go |
| P05 | 423 | 28.8% | 28.8% | -0.2 | 60% | ❌ 31 pts to go |
| P06M | 11132 | 91.6% | 91.6% | -0.8 | n/a | no target |
| P06T | 65815 | 80.1% | 80.1% | +0.1 | n/a | no target |
| P06 | 298 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P07 | 800 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P08 | 25619 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P09 | 295 | 95.9% | 95.9% | -0.1 | 100% | 🟡 4 pts to go |
| P10R | 97211 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P10 | 2658 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P11 | 12828 | 10.0% | 10.0% | -2.7 | 60% | ❌ 50 pts to go |
| P12 | 7 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P13 | 17816 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `solicitation_or_tender_number`

> ceiling: SEAO's 'numero' is the organisation's own reference for the notice (SEAO data dictionary) and is reported here; sources that publish awards under a tender number only (bids&tenders, SaskTenders, BC) also carry it as the contract reference, labelled

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 106 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P01T | 366 | 0.0% | 0.0% | +0.0 | 30% | ❌ 30 pts to go |
| P01_GOLD | 625 | 50.7% | 50.7% | +0.1 | 80% | ❌ 29 pts to go |
| P02 | 470 | 56.4% | 56.4% | -0.6 | 60% | 🟡 4 pts to go |
| P03 | 257 | 51.4% | 51.4% | -0.2 | 80% | ❌ 29 pts to go |
| P04 | 3818 | 22.3% | 22.3% | -2.7 | 50% | ❌ 28 pts to go |
| P05 | 423 | 11.6% | 11.6% | -0.3 | 40% | ❌ 28 pts to go |
| P06M | 11132 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06T | 65815 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06 | 298 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P07 | 800 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P08 | 25619 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P09 | 295 | 83.1% | 83.1% | -0.4 | 50% | ✅ met |
| P10R | 97211 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P10 | 2658 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P11 | 12828 | 0.6% | 0.6% | -0.2 | 40% | ❌ 39 pts to go |
| P12 | 7 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P13 | 17816 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `award_or_notice_id`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 106 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P01T | 366 | 0.3% | 0.3% | +0.0 | n/a | no target |
| P01_GOLD | 625 | 60.5% | 60.5% | +0.1 | 85% | ❌ 24 pts to go |
| P02 | 470 | 55.7% | 55.7% | -0.6 | 90% | ❌ 34 pts to go |
| P03 | 257 | 59.9% | 59.9% | -0.3 | 85% | ❌ 25 pts to go |
| P04 | 3818 | 23.0% | 23.0% | -2.8 | 85% | ❌ 62 pts to go |
| P05 | 423 | 19.6% | 19.6% | -0.3 | 50% | ❌ 30 pts to go |
| P06M | 11132 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06T | 65815 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06 | 298 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P07 | 800 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P08 | 25619 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P09 | 295 | 96.9% | 96.9% | -0.1 | 100% | 🟡 3 pts to go |
| P10R | 97211 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P10 | 2658 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P11 | 12828 | 0.7% | 0.7% | -0.2 | 60% | ❌ 59 pts to go |
| P12 | 7 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P13 | 17816 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `buyer_vendor_id`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 106 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P01T | 366 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P01_GOLD | 625 | 13.0% | 13.0% | +0.1 | 60% | ❌ 47 pts to go |
| P02 | 470 | 6.0% | 6.0% | +0.0 | 50% | ❌ 44 pts to go |
| P03 | 257 | 8.6% | 8.6% | +0.0 | 50% | ❌ 41 pts to go |
| P04 | 3818 | 1.8% | 1.8% | -0.2 | 40% | ❌ 38 pts to go |
| P05 | 423 | 0.7% | 0.7% | -0.2 | 20% | ❌ 19 pts to go |
| P06M | 11132 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06T | 65815 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06 | 298 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P07 | 800 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P08 | 25619 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P09 | 295 | 2.4% | 2.4% | +0.1 | 50% | ❌ 48 pts to go |
| P10R | 97211 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P10 | 2658 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P11 | 12828 | 0.1% | 0.1% | +0.0 | n/a | no target |
| P12 | 7 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P13 | 17816 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `commodity_codes`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 106 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P01T | 366 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P01_GOLD | 625 | 34.9% | 34.9% | +0.1 | 80% | ❌ 45 pts to go |
| P02 | 470 | 51.5% | 51.5% | -0.5 | 90% | ❌ 38 pts to go |
| P03 | 257 | 33.5% | 33.5% | -0.1 | 80% | ❌ 46 pts to go |
| P04 | 3818 | 21.1% | 21.1% | -2.5 | 85% | ❌ 64 pts to go |
| P05 | 423 | 5.4% | 5.4% | +0.0 | 50% | ❌ 45 pts to go |
| P06M | 11132 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06T | 65815 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06 | 298 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P07 | 800 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P08 | 25619 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P09 | 295 | 75.6% | 75.6% | -0.3 | 95% | ❌ 19 pts to go |
| P10R | 97211 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P10 | 2658 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P11 | 12828 | 0.5% | 0.5% | -0.1 | 50% | ❌ 50 pts to go |
| P12 | 7 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P13 | 17816 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `buyer_org_codes`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 106 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P01T | 366 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P01_GOLD | 625 | 8.5% | 8.5% | +0.0 | 50% | ❌ 42 pts to go |
| P02 | 470 | 6.2% | 6.2% | +0.0 | 50% | ❌ 44 pts to go |
| P03 | 257 | 1.9% | 1.9% | -0.1 | 30% | ❌ 28 pts to go |
| P04 | 3818 | 0.4% | 0.4% | -0.1 | 30% | ❌ 30 pts to go |
| P05 | 423 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06M | 11132 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06T | 65815 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06 | 298 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P07 | 800 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P08 | 25619 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P09 | 295 | 0.3% | 0.3% | +0.0 | n/a | no target |
| P10R | 97211 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P10 | 2658 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P11 | 12828 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P12 | 7 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P13 | 17816 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `records_with_this_vendor`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 106 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P01T | 366 | 100.0% | 100.0% | +0.0 | 60% | ✅ met |
| P01_GOLD | 625 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P02 | 470 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P03 | 257 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P04 | 3818 | 100.0% | 100.0% | +0.0 | 95% | ✅ met |
| P05 | 423 | 100.0% | 100.0% | +0.0 | 70% | ✅ met |
| P06M | 11132 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P06T | 65815 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P06 | 298 | 100.0% | 100.0% | +0.0 | 50% | ✅ met |
| P07 | 800 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P08 | 25619 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P09 | 295 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P10R | 97211 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P10 | 2658 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P11 | 12828 | 100.0% | 100.0% | +0.0 | 70% | ✅ met |
| P12 | 7 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P13 | 17816 | 0.0% | 0.0% | +0.0 | n/a | no target |

## 2. vendor

### `vendor_bn9`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 106 | 11.3% | 11.3% | -3.1 | 70% | ❌ 59 pts to go |
| P01T | 366 | 31.4% | 31.4% | -2.3 | 60% | ❌ 29 pts to go |
| P01_GOLD | 625 | 72.6% | 72.6% | -0.4 | 90% | ❌ 17 pts to go |
| P02 | 470 | 53.4% | 53.4% | -1.7 | 85% | ❌ 32 pts to go |
| P03 | 257 | 68.1% | 68.1% | -1.8 | 90% | ❌ 22 pts to go |
| P04 | 3818 | 28.8% | 28.8% | -3.7 | 75% | ❌ 46 pts to go |
| P05 | 423 | 51.3% | 51.3% | +1.4 | 50% | ✅ met |
| P06M | 11132 | 1.9% | 1.9% | +0.1 | n/a | no target |
| P06T | 65815 | 21.0% | 21.0% | +3.7 | n/a | no target |
| P06 | 298 | 26.5% | 26.5% | +3.7 | 40% | ❌ 14 pts to go |
| P07 | 800 | 18.2% | 18.2% | +1.8 | 50% | ❌ 32 pts to go |
| P08 | 25619 | 14.5% | 14.5% | +3.6 | 50% | ❌ 36 pts to go |
| P09 | 295 | 58.3% | 58.3% | +0.5 | 80% | ❌ 22 pts to go |
| P10R | 97211 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P10 | 2658 | 31.1% | 31.1% | +2.4 | 40% | 🟡 9 pts to go |
| P11 | 12828 | 93.0% | 93.0% | +1.9 | 60% | ✅ met |
| P12 | 7 | 42.9% | 42.9% | -19.6 | 85% | ❌ 42 pts to go |
| P13 | 17816 | 90.8% | 90.8% | -0.2 | 0% by design | — leave (by design) |

### `vendor_registered_address`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 106 | 60.4% | 60.4% | -6.6 | n/a | no target |
| P01T | 366 | 39.3% | 39.3% | +1.3 | n/a | no target |
| P01_GOLD | 625 | 70.6% | 70.6% | +0.2 | 95% | ❌ 24 pts to go |
| P02 | 470 | 73.0% | 73.0% | -0.8 | 95% | ❌ 22 pts to go |
| P03 | 257 | 71.2% | 71.2% | -0.7 | 95% | ❌ 24 pts to go |
| P04 | 3818 | 40.6% | 40.6% | -5.0 | 95% | ❌ 54 pts to go |
| P05 | 423 | 53.0% | 53.0% | -0.4 | 70% | ❌ 17 pts to go |
| P06M | 11132 | 47.1% | 47.1% | -7.5 | n/a | no target |
| P06T | 65815 | 30.5% | 30.5% | +0.2 | n/a | no target |
| P06 | 298 | 23.8% | 23.8% | -1.0 | 80% | ❌ 56 pts to go |
| P07 | 800 | 16.2% | 16.2% | -1.8 | 70% | ❌ 54 pts to go |
| P08 | 25619 | 12.6% | 12.6% | -1.5 | 70% | ❌ 57 pts to go |
| P09 | 295 | 87.1% | 87.1% | -0.4 | 100% | ❌ 13 pts to go |
| P10R | 97211 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P10 | 2658 | 32.1% | 32.1% | -0.4 | 70% | ❌ 38 pts to go |
| P11 | 12828 | 93.7% | 93.7% | +1.5 | 75% | ✅ met |
| P12 | 7 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P13 | 17816 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `vendor_trading_name`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 106 | 16.0% | 16.0% | -0.5 | n/a | no target |
| P01T | 366 | 44.8% | 44.8% | +18.9 | n/a | no target |
| P01_GOLD | 625 | 48.8% | 48.8% | +0.9 | 60% | ❌ 11 pts to go |
| P02 | 470 | 54.9% | 54.9% | -0.4 | 60% | 🟡 5 pts to go |
| P03 | 257 | 53.7% | 53.7% | -1.4 | 60% | 🟡 6 pts to go |
| P04 | 3818 | 36.0% | 36.0% | -0.7 | 55% | ❌ 19 pts to go |
| P05 | 423 | 22.0% | 22.0% | -0.2 | 50% | ❌ 28 pts to go |
| P06M | 11132 | 4.8% | 4.8% | +1.2 | n/a | no target |
| P06T | 65815 | 55.4% | 55.4% | +28.4 | n/a | no target |
| P06 | 298 | 41.3% | 41.3% | +6.1 | n/a | no target |
| P07 | 800 | 37.4% | 37.4% | +4.2 | 55% | ❌ 18 pts to go |
| P08 | 25619 | 31.3% | 31.3% | +4.4 | 50% | ❌ 19 pts to go |
| P09 | 295 | 71.5% | 71.5% | +0.5 | 70% | ✅ met |
| P10R | 97211 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P10 | 2658 | 42.9% | 42.9% | +3.4 | 55% | ❌ 12 pts to go |
| P11 | 12828 | 94.9% | 94.9% | +2.9 | 50% | ✅ met |
| P12 | 7 | 100.0% | 100.0% | +12.5 | n/a | no target |
| P13 | 17816 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `vendor_phone`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 106 | 17.0% | 17.0% | +2.6 | n/a | no target |
| P01T | 366 | 70.2% | 70.2% | +13.9 | n/a | no target |
| P01_GOLD | 625 | 45.3% | 45.3% | -2.6 | 70% | ❌ 25 pts to go |
| P02 | 470 | 51.5% | 51.5% | -2.5 | 70% | ❌ 18 pts to go |
| P03 | 257 | 47.5% | 47.5% | -2.1 | 70% | ❌ 22 pts to go |
| P04 | 3818 | 46.9% | 46.9% | -0.2 | 65% | ❌ 18 pts to go |
| P05 | 423 | 26.2% | 26.2% | -4.5 | 60% | ❌ 34 pts to go |
| P06M | 11132 | 4.5% | 4.5% | +1.0 | n/a | no target |
| P06T | 65815 | 74.0% | 74.0% | +10.2 | n/a | no target |
| P06 | 298 | 62.4% | 62.4% | +4.8 | 40% | ✅ met |
| P07 | 800 | 60.9% | 60.9% | +3.9 | 85% | ❌ 24 pts to go |
| P08 | 25619 | 60.0% | 60.0% | +3.1 | 85% | ❌ 25 pts to go |
| P09 | 295 | 54.2% | 54.2% | +0.7 | 85% | ❌ 31 pts to go |
| P10R | 97211 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P10 | 2658 | 61.4% | 61.4% | +0.4 | 85% | ❌ 24 pts to go |
| P11 | 12828 | 5.6% | 5.6% | -0.8 | 75% | ❌ 69 pts to go |
| P12 | 7 | 28.6% | 28.6% | +3.6 | n/a | no target |
| P13 | 17816 | 100.0% | 100.0% | +0.0 | 60% | ✅ met |

### `vendor_website`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 106 | 17.0% | 17.0% | -2.6 | n/a | no target |
| P01T | 366 | 98.1% | 98.1% | +1.7 | n/a | no target |
| P01_GOLD | 625 | 79.5% | 79.5% | -9.8 | 90% | ❌ 10 pts to go |
| P02 | 470 | 84.3% | 84.3% | -4.9 | 90% | 🟡 6 pts to go |
| P03 | 257 | 87.2% | 87.2% | -3.8 | 90% | 🟡 3 pts to go |
| P04 | 3818 | 85.2% | 85.2% | -5.0 | 85% | ✅ met |
| P05 | 423 | 44.2% | 44.2% | -8.0 | 70% | ❌ 26 pts to go |
| P06M | 11132 | 5.7% | 5.7% | -0.5 | n/a | no target |
| P06T | 65815 | 99.9% | 99.9% | +7.9 | n/a | no target |
| P06 | 298 | 98.3% | 98.3% | +0.0 | 50% | ✅ met |
| P07 | 800 | 99.1% | 99.1% | +0.0 | 100% | 🟡 1 pts to go |
| P08 | 25619 | 99.5% | 99.5% | +0.1 | 100% | 🟡 0 pts to go |
| P09 | 295 | 80.3% | 80.3% | +0.1 | 100% | ❌ 20 pts to go |
| P10R | 97211 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P10 | 2658 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P11 | 12828 | 99.7% | 99.7% | +0.0 | 100% | 🟡 0 pts to go |
| P12 | 7 | 28.6% | 28.6% | -8.9 | n/a | no target |
| P13 | 17816 | 100.0% | 100.0% | +0.0 | n/a | no target |

### `vendor_emails`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 106 | 14.2% | 14.2% | -0.2 | n/a | no target |
| P01T | 366 | 48.4% | 48.4% | -0.7 | n/a | no target |
| P01_GOLD | 625 | 43.0% | 43.0% | -2.2 | 70% | ❌ 27 pts to go |
| P02 | 470 | 48.5% | 48.5% | -1.0 | 75% | ❌ 26 pts to go |
| P03 | 257 | 44.0% | 44.0% | -0.5 | 75% | ❌ 31 pts to go |
| P04 | 3818 | 36.9% | 36.9% | -0.5 | 70% | ❌ 33 pts to go |
| P05 | 423 | 20.6% | 20.6% | -4.9 | 55% | ❌ 34 pts to go |
| P06M | 11132 | 3.4% | 3.4% | +0.1 | n/a | no target |
| P06T | 65815 | 40.6% | 40.6% | +1.0 | n/a | no target |
| P06 | 298 | 44.6% | 44.6% | +1.8 | n/a | no target |
| P07 | 800 | 47.6% | 47.6% | +1.7 | 70% | ❌ 22 pts to go |
| P08 | 25619 | 51.0% | 51.0% | +1.1 | 75% | ❌ 24 pts to go |
| P09 | 295 | 49.8% | 49.8% | +0.0 | 85% | ❌ 35 pts to go |
| P10R | 97211 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P10 | 2658 | 43.6% | 43.6% | +0.1 | 80% | ❌ 36 pts to go |
| P11 | 12828 | 4.1% | 4.1% | -0.9 | 70% | ❌ 66 pts to go |
| P12 | 7 | 14.3% | 14.3% | -10.7 | n/a | no target |
| P13 | 17816 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `vendor_logo_url`

> ceiling: needs the vendor's website first; sites that block automated readers (robots.txt / 403) are never read

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 106 | 17.0% | 17.0% | +3.6 | n/a | no target |
| P01T | 366 | 86.3% | 86.3% | -3.5 | n/a | no target |
| P01_GOLD | 625 | 69.4% | 69.4% | -8.1 | 90% | ❌ 21 pts to go |
| P02 | 470 | 73.0% | 73.0% | -4.6 | 90% | ❌ 17 pts to go |
| P03 | 257 | 79.4% | 79.4% | -3.8 | 90% | ❌ 11 pts to go |
| P04 | 3818 | 71.2% | 71.2% | -4.4 | 85% | ❌ 14 pts to go |
| P05 | 423 | 41.4% | 41.4% | -7.3 | 75% | ❌ 34 pts to go |
| P06M | 11132 | 5.3% | 5.3% | +1.2 | n/a | no target |
| P06T | 65815 | 93.9% | 93.9% | +10.7 | n/a | no target |
| P06 | 298 | 82.6% | 82.6% | +3.3 | n/a | no target |
| P07 | 800 | 86.1% | 86.1% | +4.5 | 100% | ❌ 14 pts to go |
| P08 | 25619 | 82.9% | 82.9% | +4.0 | 100% | ❌ 17 pts to go |
| P09 | 295 | 62.0% | 62.0% | +0.6 | n/a | no target |
| P10R | 97211 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P10 | 2658 | 84.5% | 84.5% | +0.3 | 100% | ❌ 16 pts to go |
| P11 | 12828 | 91.9% | 91.9% | +3.5 | n/a | no target |
| P12 | 7 | 28.6% | 28.6% | -8.9 | n/a | no target |
| P13 | 17816 | 83.6% | 83.6% | +0.4 | n/a | no target |

### `vendor_neq`

> ceiling: only Québec-registered vendors have an NEQ; the share of QC vendors is reported next to the rate

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 106 | 49.1% | 49.1% | -4.5 | n/a | no target · QC vendors: 46 rows, 100.0% filled |
| P01T | 366 | 20.2% | 20.2% | +2.4 | n/a | no target · QC vendors: 20 rows, 100.0% filled |
| P01_GOLD | 625 | 43.7% | 43.7% | +0.1 | 95% | ❌ 51 pts to go · QC vendors: 53 rows, 98.1% filled |
| P02 | 470 | 54.5% | 54.5% | -0.6 | 95% | ❌ 40 pts to go · QC vendors: 110 rows, 100.0% filled |
| P03 | 257 | 45.9% | 45.9% | -0.6 | 95% | ❌ 49 pts to go · QC vendors: 18 rows, 100.0% filled |
| P04 | 3818 | 28.3% | 28.3% | -3.6 | 95% | ❌ 67 pts to go · QC vendors: 492 rows, 98.8% filled |
| P05 | 423 | 14.2% | 14.2% | -0.6 | n/a | no target · QC vendors: 34 rows, 94.1% filled |
| P06M | 11132 | 45.9% | 45.9% | -7.4 | n/a | no target · QC vendors: 4799 rows, 100.0% filled |
| P06T | 65815 | 18.3% | 18.3% | +0.8 | n/a | no target · QC vendors: 3542 rows, 100.0% filled |
| P06 | 298 | 8.1% | 8.1% | -0.2 | n/a | no target · QC vendors: 13 rows, 100.0% filled |
| P07 | 800 | 5.9% | 5.9% | -0.9 | n/a | no target · QC vendors: 32 rows, 96.9% filled |
| P08 | 25619 | 6.0% | 6.0% | -0.5 | n/a | no target · QC vendors: 1218 rows, 99.7% filled |
| P09 | 295 | 78.0% | 78.0% | -0.2 | 95% | ❌ 17 pts to go · QC vendors: 106 rows, 100.0% filled |
| P10R | 97211 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P10 | 2658 | 17.3% | 17.3% | -0.3 | n/a | no target · QC vendors: 300 rows, 94.7% filled |
| P11 | 12828 | 85.8% | 85.8% | +4.3 | n/a | no target · QC vendors: 113 rows, 99.1% filled |
| P12 | 7 | 71.4% | 71.4% | +8.9 | n/a | no target · QC vendors: 1 rows, 100.0% filled |
| P13 | 17816 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `vendor_years_in_business`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 106 | 59.4% | 59.4% | -5.5 | n/a | no target · vendors with a registry record: 63 rows, 100.0% filled |
| P01T | 366 | 39.6% | 39.6% | +1.3 | n/a | no target · vendors with a registry record: 145 rows, 100.0% filled |
| P01_GOLD | 625 | 79.5% | 79.5% | +0.1 | 100% | ❌ 20 pts to go · vendors with a registry record: 497 rows, 100.0% filled |
| P02 | 470 | 76.6% | 76.6% | -0.8 | 100% | ❌ 23 pts to go · vendors with a registry record: 360 rows, 100.0% filled |
| P03 | 257 | 80.5% | 80.5% | -0.7 | 100% | ❌ 20 pts to go · vendors with a registry record: 207 rows, 100.0% filled |
| P04 | 3818 | 41.0% | 41.0% | -5.1 | 100% | ❌ 59 pts to go · vendors with a registry record: 1566 rows, 100.0% filled |
| P05 | 423 | 57.9% | 57.9% | -0.4 | n/a | no target · vendors with a registry record: 245 rows, 100.0% filled |
| P06M | 11132 | 46.9% | 46.9% | -7.4 | n/a | no target · vendors with a registry record: 5221 rows, 100.0% filled |
| P06T | 65815 | 30.5% | 30.5% | +0.1 | n/a | no target · vendors with a registry record: 20097 rows, 100.0% filled |
| P06 | 298 | 24.5% | 24.5% | -1.0 | n/a | no target · vendors with a registry record: 73 rows, 100.0% filled |
| P07 | 800 | 16.6% | 16.6% | -1.8 | n/a | no target · vendors with a registry record: 133 rows, 100.0% filled |
| P08 | 25619 | 12.8% | 12.8% | -1.5 | n/a | no target · vendors with a registry record: 3285 rows, 100.0% filled |
| P09 | 295 | 90.8% | 90.8% | -0.3 | n/a | no target · vendors with a registry record: 268 rows, 100.0% filled |
| P10R | 97211 | 100.0% | 100.0% | +0.0 | n/a | no target · vendors with a registry record: 97211 rows, 100.0% filled |
| P10 | 2658 | 32.8% | 32.8% | -0.4 | n/a | no target · vendors with a registry record: 871 rows, 100.0% filled |
| P11 | 12828 | 93.8% | 93.8% | +1.5 | n/a | no target · vendors with a registry record: 12036 rows, 100.0% filled |
| P12 | 7 | 100.0% | 100.0% | +0.0 | n/a | no target · vendors with a registry record: 7 rows, 100.0% filled |
| P13 | 17816 | 0.0% | 0.0% | +0.0 | n/a | no target |

## 3. buyer

### `buyer_legal_name_as_published`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 106 | 91.5% | 91.5% | +2.8 | 90% | ✅ met |
| P01T | 366 | 68.0% | 68.0% | +11.7 | 90% | ❌ 22 pts to go |
| P01_GOLD | 625 | 85.6% | 85.6% | +1.9 | 95% | 🟡 9 pts to go |
| P02 | 470 | 86.6% | 86.6% | +1.4 | 95% | 🟡 8 pts to go |
| P03 | 257 | 83.3% | 83.3% | +4.4 | 85% | 🟡 2 pts to go |
| P04 | 3818 | 56.7% | 56.7% | +0.3 | 90% | ❌ 33 pts to go |
| P05 | 423 | 77.3% | 77.3% | +9.6 | 75% | ✅ met |
| P06M | 11132 | 89.8% | 89.8% | +2.7 | n/a | no target |
| P06T | 65815 | 42.2% | 42.2% | +13.2 | n/a | no target |
| P06 | 298 | 62.8% | 62.8% | +5.9 | 80% | ❌ 17 pts to go |
| P07 | 800 | 48.8% | 48.9% | +2.6 | 80% | ❌ 31 pts to go |
| P08 | 25619 | 43.4% | 43.4% | +4.9 | 75% | ❌ 32 pts to go |
| P09 | 295 | 76.9% | 76.9% | -0.3 | 95% | ❌ 18 pts to go |
| P10R | 97211 | 35.0% | 35.0% | +10.0 | n/a | no target |
| P10 | 2658 | 47.1% | 47.1% | +8.1 | 70% | ❌ 23 pts to go |
| P11 | 12828 | 30.9% | 30.9% | +21.3 | 65% | ❌ 34 pts to go |
| P12 | 7 | 71.4% | 71.4% | -3.6 | 80% | 🟡 9 pts to go |
| P13 | 17816 | 45.6% | 45.6% | +6.4 | 60% | ❌ 14 pts to go |

### `buyer_bn_as_published`

> ceiling: a buyer's BN is public only where the buyer prints it or a public dataset carries it (CRA charities, federal grants & contributions recipients, business registries for corporations); municipalities rarely publish theirs

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 106 | 22.6% | 22.6% | +3.0 | 50% | ❌ 27 pts to go |
| P01T | 366 | 15.8% | 15.8% | +2.5 | n/a | no target |
| P01_GOLD | 625 | 19.8% | 19.8% | -0.8 | 40% | ❌ 20 pts to go |
| P02 | 470 | 19.4% | 19.4% | +0.5 | 40% | ❌ 21 pts to go |
| P03 | 257 | 23.0% | 23.0% | +0.7 | 40% | ❌ 17 pts to go |
| P04 | 3818 | 15.5% | 15.5% | -0.8 | 40% | ❌ 24 pts to go |
| P05 | 423 | 19.9% | 19.9% | +0.2 | 25% | 🟡 5 pts to go |
| P06M | 11132 | 12.3% | 12.3% | +3.5 | n/a | no target |
| P06T | 65815 | 9.8% | 9.8% | +2.3 | n/a | no target |
| P06 | 298 | 15.8% | 15.8% | +3.0 | 35% | ❌ 19 pts to go |
| P07 | 800 | 14.1% | 14.1% | +2.6 | 35% | ❌ 21 pts to go |
| P08 | 25619 | 13.8% | 13.8% | +3.4 | 35% | ❌ 21 pts to go |
| P09 | 295 | 16.3% | 16.3% | +0.1 | n/a | no target |
| P10R | 97211 | 9.0% | 9.0% | +1.9 | n/a | no target |
| P10 | 2658 | 11.5% | 11.5% | +5.0 | 30% | ❌ 18 pts to go |
| P11 | 12828 | 1.9% | 1.9% | +0.7 | n/a | no target |
| P12 | 7 | 14.3% | 14.3% | +1.8 | n/a | no target |
| P13 | 17816 | 21.0% | 21.0% | +0.0 | 30% | 🟡 9 pts to go |

### `buyer_address`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 106 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P01T | 366 | 90.4% | 90.4% | -1.5 | 100% | 🟡 10 pts to go |
| P01_GOLD | 625 | 90.1% | 90.1% | +0.6 | 100% | 🟡 10 pts to go |
| P02 | 470 | 95.5% | 95.5% | +0.2 | 100% | 🟡 4 pts to go |
| P03 | 257 | 89.1% | 89.1% | -0.4 | 100% | ❌ 11 pts to go |
| P04 | 3818 | 74.5% | 74.5% | -1.4 | 100% | ❌ 26 pts to go |
| P05 | 423 | 87.9% | 87.9% | +0.5 | 100% | ❌ 12 pts to go |
| P06M | 11132 | 99.0% | 99.0% | +0.2 | n/a | no target |
| P06T | 65815 | 77.6% | 77.6% | +0.2 | n/a | no target |
| P06 | 298 | 81.5% | 81.5% | +0.5 | 95% | ❌ 14 pts to go |
| P07 | 800 | 82.8% | 82.8% | -0.8 | 95% | ❌ 12 pts to go |
| P08 | 25619 | 79.0% | 79.0% | -1.2 | 95% | ❌ 16 pts to go |
| P09 | 295 | 95.9% | 95.9% | +0.2 | 100% | 🟡 4 pts to go |
| P10R | 97211 | 60.7% | 60.7% | +1.9 | n/a | no target |
| P10 | 2658 | 65.3% | 65.3% | +0.2 | 95% | ❌ 30 pts to go |
| P11 | 12828 | 90.9% | 90.9% | +3.7 | 80% | ✅ met |
| P12 | 7 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P13 | 17816 | 77.1% | 77.1% | +1.9 | 95% | ❌ 18 pts to go |

### `buyer_phone`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 106 | 82.1% | 82.1% | -3.5 | n/a | no target |
| P01T | 366 | 75.7% | 75.7% | +12.1 | n/a | no target |
| P01_GOLD | 625 | 70.4% | 70.4% | +0.9 | 90% | ❌ 20 pts to go |
| P02 | 470 | 75.5% | 75.5% | -0.2 | 95% | ❌ 20 pts to go |
| P03 | 257 | 73.5% | 73.5% | -0.3 | 95% | ❌ 22 pts to go |
| P04 | 3818 | 61.4% | 61.4% | -5.2 | 95% | ❌ 34 pts to go |
| P05 | 423 | 71.6% | 71.6% | +1.1 | 90% | ❌ 18 pts to go |
| P06M | 11132 | 80.2% | 80.2% | -6.2 | n/a | no target |
| P06T | 65815 | 67.3% | 67.3% | +19.4 | n/a | no target |
| P06 | 298 | 64.4% | 64.4% | +1.3 | 95% | ❌ 31 pts to go |
| P07 | 800 | 55.8% | 55.8% | +0.8 | 90% | ❌ 34 pts to go |
| P08 | 25619 | 56.9% | 56.9% | -1.9 | 95% | ❌ 38 pts to go |
| P09 | 295 | 85.8% | 85.8% | -0.3 | 100% | ❌ 14 pts to go |
| P10R | 97211 | 57.2% | 57.2% | +12.1 | n/a | no target |
| P10 | 2658 | 57.5% | 57.5% | +1.0 | 95% | ❌ 38 pts to go |
| P11 | 12828 | 28.9% | 28.9% | +17.7 | 75% | ❌ 46 pts to go |
| P12 | 7 | 71.4% | 71.4% | -3.6 | n/a | no target |
| P13 | 17816 | 57.8% | 57.8% | +10.2 | 95% | ❌ 37 pts to go |

### `buyer_logo_url`

> ceiling: sites that block automated readers (robots.txt / 403) are never read; an og:image that looks like a photo is labelled

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 106 | 75.5% | 75.5% | +4.4 | n/a | no target |
| P01T | 366 | 89.1% | 89.1% | +15.0 | 95% | 🟡 6 pts to go |
| P01_GOLD | 625 | 81.1% | 81.1% | +0.4 | 90% | 🟡 9 pts to go |
| P02 | 470 | 85.1% | 85.1% | -0.7 | 95% | 🟡 10 pts to go |
| P03 | 257 | 84.0% | 84.0% | +0.0 | 95% | ❌ 11 pts to go |
| P04 | 3818 | 76.3% | 76.3% | -7.0 | 90% | ❌ 14 pts to go |
| P05 | 423 | 89.6% | 89.6% | +1.1 | 95% | 🟡 5 pts to go |
| P06M | 11132 | 74.7% | 74.7% | +8.0 | n/a | no target |
| P06T | 65815 | 88.3% | 88.3% | +26.8 | n/a | no target |
| P06 | 298 | 81.2% | 81.2% | -0.9 | 100% | ❌ 19 pts to go |
| P07 | 800 | 74.6% | 74.6% | -2.6 | 100% | ❌ 25 pts to go |
| P08 | 25619 | 74.2% | 74.2% | -2.9 | 100% | ❌ 26 pts to go |
| P09 | 295 | 68.8% | 68.8% | +0.2 | n/a | no target |
| P10R | 97211 | 79.6% | 79.6% | +19.6 | n/a | no target |
| P10 | 2658 | 87.5% | 87.5% | +0.7 | 100% | ❌ 12 pts to go |
| P11 | 12828 | 64.5% | 64.5% | +45.7 | 80% | ❌ 16 pts to go |
| P12 | 7 | 71.4% | 71.4% | -3.6 | n/a | no target |
| P13 | 17816 | 65.0% | 65.0% | +14.0 | 95% | ❌ 30 pts to go |

## 4. AP

### `ap_contact_name_as_published`

> ceiling: owner 2026-11-08: the AP contact person the organisation itself names on its AP / finance page is allowed (name + role phrase, quoted); mailboxes stay organisational; many bodies publish no AP person

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 106 | 2.8% | 2.8% | -1.3 | n/a | no target |
| P01T | 366 | 8.2% | 8.2% | -0.2 | n/a | no target |
| P01_GOLD | 625 | 14.2% | 14.2% | +0.0 | 25% | ❌ 11 pts to go |
| P02 | 470 | 24.3% | 24.3% | -0.2 | 40% | ❌ 16 pts to go |
| P03 | 257 | 8.9% | 8.9% | -0.1 | 20% | ❌ 11 pts to go |
| P04 | 3818 | 3.2% | 3.2% | -0.4 | 20% | ❌ 17 pts to go |
| P05 | 423 | 3.1% | 3.1% | -0.2 | 15% | ❌ 12 pts to go |
| P06M | 11132 | 0.2% | 0.2% | -0.1 | n/a | no target |
| P06T | 65815 | 0.4% | 0.4% | +0.0 | n/a | no target |
| P06 | 298 | 5.4% | 5.4% | -0.8 | n/a | no target |
| P07 | 800 | 7.4% | 7.4% | +0.1 | n/a | no target |
| P08 | 25619 | 0.2% | 0.2% | -0.1 | n/a | no target |
| P09 | 295 | 7.8% | 7.8% | +0.2 | n/a | no target |
| P10R | 97211 | 0.2% | 0.2% | +0.0 | n/a | no target |
| P10 | 2658 | 0.9% | 0.9% | -0.1 | n/a | no target |
| P11 | 12828 | 0.1% | 0.1% | -0.1 | n/a | no target |
| P12 | 7 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P13 | 17816 | 0.4% | 0.4% | +0.0 | n/a | no target |

### `ap_phone`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 106 | 23.6% | 23.6% | -3.2 | n/a | no target |
| P01T | 366 | 24.0% | 24.0% | -0.1 | 70% | ❌ 46 pts to go |
| P01_GOLD | 625 | 43.4% | 43.4% | +0.1 | 80% | ❌ 37 pts to go |
| P02 | 470 | 56.2% | 56.2% | -0.6 | 90% | ❌ 34 pts to go |
| P03 | 257 | 19.1% | 19.1% | +0.0 | 60% | ❌ 41 pts to go |
| P04 | 3818 | 21.2% | 21.2% | -2.5 | 85% | ❌ 64 pts to go |
| P05 | 423 | 11.8% | 11.8% | -0.1 | 50% | ❌ 38 pts to go |
| P06M | 11132 | 0.4% | 0.4% | +0.0 | n/a | no target |
| P06T | 65815 | 0.6% | 0.6% | +0.0 | n/a | no target |
| P06 | 298 | 14.8% | 14.8% | -1.4 | n/a | no target |
| P07 | 800 | 11.8% | 11.8% | -1.2 | n/a | no target |
| P08 | 25619 | 0.4% | 0.4% | -0.1 | n/a | no target |
| P09 | 295 | 77.3% | 77.3% | -0.3 | 95% | ❌ 18 pts to go |
| P10R | 97211 | 0.2% | 0.2% | +0.0 | n/a | no target |
| P10 | 2658 | 1.7% | 1.7% | +0.0 | n/a | no target |
| P11 | 12828 | 2.7% | 2.7% | -0.9 | n/a | no target |
| P12 | 7 | 28.6% | 28.6% | +3.6 | n/a | no target |
| P13 | 17816 | 0.7% | 0.7% | +0.0 | n/a | no target |

### `invoice_mailing_address`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 106 | 6.6% | 6.6% | -0.6 | n/a | no target |
| P01T | 366 | 12.3% | 12.3% | +0.3 | n/a | no target |
| P01_GOLD | 625 | 33.9% | 33.9% | +0.0 | 70% | ❌ 36 pts to go |
| P02 | 470 | 38.5% | 38.5% | -0.4 | 75% | ❌ 36 pts to go |
| P03 | 257 | 19.1% | 19.1% | +0.0 | 55% | ❌ 36 pts to go |
| P04 | 3818 | 21.1% | 21.1% | -2.5 | 75% | ❌ 54 pts to go |
| P05 | 423 | 10.9% | 10.9% | +0.1 | 50% | ❌ 39 pts to go |
| P06M | 11132 | 0.1% | 0.1% | -0.1 | n/a | no target |
| P06T | 65815 | 0.3% | 0.3% | -0.1 | n/a | no target |
| P06 | 298 | 7.4% | 7.4% | -0.9 | n/a | no target |
| P07 | 800 | 5.6% | 5.6% | -0.8 | n/a | no target |
| P08 | 25619 | 0.2% | 0.2% | +0.0 | n/a | no target |
| P09 | 295 | 74.9% | 74.9% | -0.3 | 95% | ❌ 20 pts to go |
| P10R | 97211 | 0.2% | 0.2% | +0.0 | n/a | no target |
| P10 | 2658 | 1.0% | 1.0% | +0.0 | n/a | no target |
| P11 | 12828 | 2.7% | 2.7% | -0.9 | n/a | no target |
| P12 | 7 | 14.3% | 14.3% | +1.8 | n/a | no target |
| P13 | 17816 | 0.4% | 0.4% | +0.0 | n/a | no target |

### `invoicing_requirements`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 106 | 7.5% | 7.5% | +1.3 | n/a | no target |
| P01T | 366 | 8.5% | 8.5% | -0.8 | n/a | no target |
| P01_GOLD | 625 | 57.9% | 58.1% | -0.1 | 80% | ❌ 22 pts to go |
| P02 | 470 | 45.3% | 45.5% | -0.5 | 75% | ❌ 30 pts to go |
| P03 | 257 | 37.7% | 37.7% | -0.2 | 70% | ❌ 32 pts to go |
| P04 | 3818 | 20.6% | 21.1% | -2.5 | 70% | ❌ 49 pts to go |
| P05 | 423 | 14.2% | 14.2% | -0.1 | 50% | ❌ 36 pts to go |
| P06M | 11132 | 0.3% | 0.3% | -0.1 | n/a | no target |
| P06T | 65815 | 0.3% | 0.3% | +0.0 | n/a | no target |
| P06 | 298 | 13.1% | 13.1% | -0.3 | n/a | no target |
| P07 | 800 | 1.9% | 1.9% | -0.1 | n/a | no target |
| P08 | 25619 | 0.3% | 0.3% | -0.1 | n/a | no target |
| P09 | 295 | 46.1% | 46.4% | +0.2 | 80% | ❌ 34 pts to go |
| P10R | 97211 | 0.1% | 0.1% | +0.0 | n/a | no target |
| P10 | 2658 | 1.2% | 1.2% | +0.0 | n/a | no target |
| P11 | 12828 | 0.8% | 0.8% | -0.3 | n/a | no target |
| P12 | 7 | 42.9% | 42.9% | +5.4 | n/a | no target |
| P13 | 17816 | 0.3% | 0.3% | +0.0 | n/a | no target |

### `payment_terms_as_published`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 106 | 12.3% | 12.3% | +1.0 | n/a | no target |
| P01T | 366 | 19.7% | 19.7% | -2.3 | 60% | ❌ 40 pts to go |
| P01_GOLD | 625 | 63.5% | 63.5% | -0.1 | 70% | 🟡 6 pts to go |
| P02 | 470 | 38.5% | 38.5% | -0.4 | 50% | ❌ 12 pts to go |
| P03 | 257 | 49.8% | 49.8% | -0.2 | 55% | 🟡 5 pts to go |
| P04 | 3818 | 11.9% | 11.9% | -1.4 | 40% | ❌ 28 pts to go |
| P05 | 423 | 17.3% | 17.3% | +0.0 | 40% | ❌ 23 pts to go |
| P06M | 11132 | 0.6% | 0.6% | -0.1 | n/a | no target |
| P06T | 65815 | 2.2% | 2.2% | -0.2 | n/a | no target |
| P06 | 298 | 19.1% | 19.1% | -0.6 | n/a | no target |
| P07 | 800 | 6.0% | 6.0% | -0.7 | n/a | no target |
| P08 | 25619 | 2.2% | 2.2% | -0.4 | n/a | no target |
| P09 | 295 | 5.8% | 5.8% | -0.1 | n/a | no target |
| P10R | 97211 | 0.2% | 0.2% | +0.0 | n/a | no target |
| P10 | 2658 | 4.4% | 4.4% | -0.1 | n/a | no target |
| P11 | 12828 | 3.6% | 3.6% | -0.7 | n/a | no target |
| P12 | 7 | 0.0% | 0.0% | -12.5 | n/a | no target |
| P13 | 17816 | 0.2% | 0.2% | +0.0 | n/a | no target |

### `po_required_as_published`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 106 | 16.0% | 16.0% | -0.5 | n/a | no target |
| P01T | 366 | 23.2% | 23.2% | -2.1 | 65% | ❌ 42 pts to go |
| P01_GOLD | 625 | 69.0% | 69.0% | +0.0 | 70% | 🟡 1 pts to go |
| P02 | 470 | 23.6% | 23.6% | -0.3 | 50% | ❌ 26 pts to go |
| P03 | 257 | 52.1% | 52.1% | -0.2 | 60% | 🟡 8 pts to go |
| P04 | 3818 | 5.1% | 5.1% | -0.7 | 40% | ❌ 35 pts to go |
| P05 | 423 | 19.9% | 19.9% | +0.2 | 45% | ❌ 25 pts to go |
| P06M | 11132 | 0.3% | 0.3% | +0.0 | n/a | no target |
| P06T | 65815 | 0.5% | 0.5% | -0.1 | n/a | no target |
| P06 | 298 | 29.2% | 29.2% | -2.5 | n/a | no target |
| P07 | 800 | 6.1% | 6.1% | -0.8 | n/a | no target |
| P08 | 25619 | 0.9% | 0.9% | -0.2 | n/a | no target |
| P09 | 295 | 9.8% | 9.8% | -0.1 | n/a | no target |
| P10R | 97211 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P10 | 2658 | 2.6% | 2.6% | +0.0 | n/a | no target |
| P11 | 12828 | 0.8% | 0.8% | -0.2 | n/a | no target |
| P12 | 7 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P13 | 17816 | 0.2% | 0.2% | +0.0 | n/a | no target |

### `invoice_portal_url`

> ceiling: only portals the buyer names on its own pages; informational tax-authority links are not portals

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 106 | 5.7% | 5.7% | -0.5 | n/a | no target |
| P01T | 366 | 13.7% | 13.7% | -0.8 | n/a | no target |
| P01_GOLD | 625 | 49.8% | 49.8% | +0.0 | 50% | 🟡 0 pts to go |
| P02 | 470 | 37.0% | 37.0% | -0.4 | n/a | no target |
| P03 | 257 | 52.5% | 52.5% | -0.6 | 60% | 🟡 8 pts to go |
| P04 | 3818 | 11.5% | 11.5% | -1.4 | n/a | no target |
| P05 | 423 | 14.9% | 14.9% | -0.3 | n/a | no target |
| P06M | 11132 | 0.3% | 0.3% | +0.0 | n/a | no target |
| P06T | 65815 | 0.4% | 0.4% | -0.1 | n/a | no target |
| P06 | 298 | 21.1% | 21.1% | -0.6 | n/a | no target |
| P07 | 800 | 6.6% | 6.6% | -0.6 | n/a | no target |
| P08 | 25619 | 0.4% | 0.4% | -0.1 | n/a | no target |
| P09 | 295 | 18.3% | 18.3% | +0.1 | n/a | no target |
| P10R | 97211 | 0.1% | 0.1% | +0.0 | n/a | no target |
| P10 | 2658 | 2.3% | 2.3% | +0.0 | n/a | no target |
| P11 | 12828 | 0.6% | 0.6% | -0.2 | n/a | no target |
| P12 | 7 | 14.3% | 14.3% | +14.3 | n/a | no target |
| P13 | 17816 | 0.4% | 0.4% | +0.0 | n/a | no target |

### `buyer_payment_method_preference`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 106 | 12.3% | 12.3% | +1.0 | 15% | 🟡 3 pts to go |
| P01T | 366 | 11.2% | 11.2% | +0.1 | 15% | 🟡 4 pts to go |
| P01_GOLD | 625 | 35.4% | 35.4% | +0.1 | 40% | 🟡 5 pts to go |
| P02 | 470 | 12.6% | 12.8% | +0.1 | 25% | ❌ 12 pts to go |
| P03 | 257 | 17.9% | 17.9% | -0.1 | 25% | 🟡 7 pts to go |
| P04 | 3818 | 2.7% | 2.7% | -0.1 | 15% | ❌ 12 pts to go |
| P05 | 423 | 6.9% | 6.9% | +0.1 | 15% | 🟡 8 pts to go |
| P06M | 11132 | 0.7% | 0.7% | +0.1 | 15% | ❌ 14 pts to go |
| P06T | 65815 | 0.7% | 0.7% | +0.3 | 15% | ❌ 14 pts to go |
| P06 | 298 | 9.1% | 9.1% | -0.2 | 15% | 🟡 6 pts to go |
| P07 | 800 | 3.5% | 3.5% | +0.3 | 15% | ❌ 12 pts to go |
| P08 | 25619 | 0.5% | 0.5% | +0.1 | 15% | ❌ 14 pts to go |
| P09 | 295 | 1.0% | 1.0% | +0.0 | 15% | ❌ 14 pts to go |
| P10R | 97211 | 0.7% | 0.7% | +0.3 | 15% | ❌ 14 pts to go |
| P10 | 2658 | 1.2% | 1.2% | +0.2 | 15% | ❌ 14 pts to go |
| P11 | 12828 | 0.4% | 0.4% | +0.2 | 15% | ❌ 15 pts to go |
| P12 | 7 | 14.3% | 14.3% | +1.8 | 15% | 🟡 1 pts to go |
| P13 | 17816 | 0.5% | 0.5% | +0.1 | 15% | ❌ 14 pts to go |

### `buyer_tax_exempt_status`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 106 | 4.7% | 4.7% | -1.5 | 15% | ❌ 10 pts to go |
| P01T | 366 | 10.7% | 10.7% | -1.3 | 25% | ❌ 14 pts to go |
| P01_GOLD | 625 | 29.1% | 29.1% | -0.1 | 25% | ✅ met |
| P02 | 470 | 25.1% | 25.1% | -0.3 | 15% | ✅ met |
| P03 | 257 | 21.4% | 21.4% | -0.1 | 15% | ✅ met |
| P04 | 3818 | 3.7% | 3.7% | -0.4 | 15% | ❌ 11 pts to go |
| P05 | 423 | 10.9% | 10.9% | +0.1 | 15% | 🟡 4 pts to go |
| P06M | 11132 | 0.2% | 0.2% | +0.0 | 15% | ❌ 15 pts to go |
| P06T | 65815 | 0.3% | 0.3% | +0.0 | 15% | ❌ 15 pts to go |
| P06 | 298 | 7.7% | 7.7% | +0.1 | 15% | 🟡 7 pts to go |
| P07 | 800 | 2.8% | 2.8% | -0.3 | 15% | ❌ 12 pts to go |
| P08 | 25619 | 0.4% | 0.4% | +0.0 | 15% | ❌ 15 pts to go |
| P09 | 295 | 1.0% | 1.0% | +0.0 | 15% | ❌ 14 pts to go |
| P10R | 97211 | 0.0% | 0.0% | +0.0 | 15% | ❌ 15 pts to go |
| P10 | 2658 | 1.5% | 1.5% | -0.1 | 15% | ❌ 14 pts to go |
| P11 | 12828 | 0.5% | 0.5% | +0.0 | 15% | ❌ 14 pts to go |
| P12 | 7 | 28.6% | 28.6% | +3.6 | 15% | ✅ met |
| P13 | 17816 | 0.1% | 0.1% | +0.1 | 15% | ❌ 15 pts to go |

### `buyer_ap_cycle_published`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 106 | 0.0% | 0.0% | +0.0 | 20% | ❌ 20 pts to go |
| P01T | 366 | 3.8% | 3.8% | -0.1 | 20% | ❌ 16 pts to go |
| P01_GOLD | 625 | 4.5% | 4.5% | +0.2 | 20% | ❌ 16 pts to go |
| P02 | 470 | 1.3% | 1.3% | +0.0 | 20% | ❌ 19 pts to go |
| P03 | 257 | 1.6% | 1.6% | +0.0 | 20% | ❌ 18 pts to go |
| P04 | 3818 | 0.6% | 0.6% | +0.0 | 20% | ❌ 19 pts to go |
| P05 | 423 | 1.2% | 1.2% | +0.0 | 20% | ❌ 19 pts to go |
| P06M | 11132 | 0.0% | 0.0% | +0.0 | 20% | ❌ 20 pts to go |
| P06T | 65815 | 0.0% | 0.0% | +0.0 | 20% | ❌ 20 pts to go |
| P06 | 298 | 1.3% | 1.3% | -0.1 | 20% | ❌ 19 pts to go |
| P07 | 800 | 0.4% | 0.4% | +0.0 | 20% | ❌ 20 pts to go |
| P08 | 25619 | 0.0% | 0.0% | +0.0 | 20% | ❌ 20 pts to go |
| P09 | 295 | 0.0% | 0.0% | +0.0 | 20% | ❌ 20 pts to go |
| P10R | 97211 | 0.0% | 0.0% | +0.0 | 20% | ❌ 20 pts to go |
| P10 | 2658 | 0.3% | 0.3% | +0.0 | 20% | ❌ 20 pts to go |
| P11 | 12828 | 0.0% | 0.0% | +0.0 | 20% | ❌ 20 pts to go |
| P12 | 7 | 0.0% | 0.0% | +0.0 | 20% | ❌ 20 pts to go |
| P13 | 17816 | 0.0% | 0.0% | +0.0 | 20% | ❌ 20 pts to go |

### `buyer_esignature_preference`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 106 | 0.9% | 0.9% | -0.1 | 15% | ❌ 14 pts to go |
| P01T | 366 | 2.5% | 2.5% | +0.1 | 15% | ❌ 12 pts to go |
| P01_GOLD | 625 | 10.4% | 10.4% | -0.1 | 15% | 🟡 5 pts to go |
| P02 | 470 | 11.9% | 11.9% | -0.1 | 15% | 🟡 3 pts to go |
| P03 | 257 | 20.6% | 20.6% | -0.1 | 15% | ✅ met |
| P04 | 3818 | 2.2% | 2.2% | -0.2 | 15% | ❌ 13 pts to go |
| P05 | 423 | 2.8% | 2.8% | -0.2 | 15% | ❌ 12 pts to go |
| P06M | 11132 | 0.1% | 0.1% | -0.1 | 15% | ❌ 15 pts to go |
| P06T | 65815 | 0.2% | 0.2% | +0.0 | 15% | ❌ 15 pts to go |
| P06 | 298 | 5.0% | 5.0% | -0.2 | 15% | 🟡 10 pts to go |
| P07 | 800 | 1.6% | 1.6% | -0.1 | 15% | ❌ 13 pts to go |
| P08 | 25619 | 0.4% | 0.4% | +0.0 | 15% | ❌ 15 pts to go |
| P09 | 295 | 0.7% | 0.7% | +0.0 | 15% | ❌ 14 pts to go |
| P10R | 97211 | 0.0% | 0.0% | +0.0 | 15% | ❌ 15 pts to go |
| P10 | 2658 | 0.9% | 0.9% | +0.0 | 15% | ❌ 14 pts to go |
| P11 | 12828 | 0.2% | 0.2% | -0.1 | 15% | ❌ 15 pts to go |
| P12 | 7 | 0.0% | 0.0% | +0.0 | 15% | ❌ 15 pts to go |
| P13 | 17816 | 0.1% | 0.1% | +0.0 | 15% | ❌ 15 pts to go |

### `ap_system_hint`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 106 | 7.5% | 7.5% | +0.3 | 20% | ❌ 12 pts to go |
| P01T | 366 | 14.2% | 14.2% | -0.9 | 40% | ❌ 26 pts to go |
| P01_GOLD | 625 | 45.9% | 45.9% | +0.1 | 40% | ✅ met |
| P02 | 470 | 42.3% | 42.3% | -0.5 | 20% | ✅ met |
| P03 | 257 | 48.6% | 48.6% | -0.2 | 35% | ✅ met |
| P04 | 3818 | 13.8% | 13.8% | -1.6 | 20% | 🟡 6 pts to go |
| P05 | 423 | 14.9% | 14.9% | +0.1 | 20% | 🟡 5 pts to go |
| P06M | 11132 | 0.5% | 0.5% | +0.0 | 20% | ❌ 20 pts to go |
| P06T | 65815 | 0.7% | 0.7% | +0.0 | 20% | ❌ 19 pts to go |
| P06 | 298 | 21.8% | 21.8% | -0.3 | 20% | ✅ met |
| P07 | 800 | 6.9% | 6.9% | -0.2 | 20% | ❌ 13 pts to go |
| P08 | 25619 | 0.8% | 0.8% | -0.1 | 20% | ❌ 19 pts to go |
| P09 | 295 | 18.3% | 18.3% | +0.1 | 20% | 🟡 2 pts to go |
| P10R | 97211 | 0.2% | 0.2% | +0.0 | 20% | ❌ 20 pts to go |
| P10 | 2658 | 3.4% | 3.4% | +0.0 | 20% | ❌ 17 pts to go |
| P11 | 12828 | 0.8% | 0.8% | -0.2 | 20% | ❌ 19 pts to go |
| P12 | 7 | 0.0% | 0.0% | +0.0 | 20% | ❌ 20 pts to go |
| P13 | 17816 | 0.6% | 0.6% | +0.1 | 20% | ❌ 19 pts to go |

## 5. contract

### `contract_value`

> ceiling: rows proven by a lobbying filing, a news release, an auditor appointment, a customer story or a vendor's client list have no contract value by nature (≈17 % of P01 Gold); bids&tenders awards now carry the awarded bidder's submitted price when no award value was published

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 106 | 39.6% | 39.6% | -4.7 | n/a | no target |
| P01T | 366 | 0.3% | 0.3% | +0.0 | n/a | no target |
| P01_GOLD | 625 | 69.4% | 69.4% | -0.1 | 95% | ❌ 26 pts to go |
| P02 | 470 | 62.3% | 62.3% | -0.7 | 95% | ❌ 33 pts to go |
| P03 | 257 | 54.5% | 54.5% | -0.2 | 90% | ❌ 36 pts to go |
| P04 | 3818 | 24.2% | 24.2% | -2.9 | 85% | ❌ 61 pts to go |
| P05 | 423 | 36.9% | 36.9% | +0.4 | 75% | ❌ 38 pts to go |
| P06M | 11132 | 41.6% | 41.6% | -8.5 | n/a | no target |
| P06T | 65815 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06 | 298 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P07 | 800 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P08 | 25619 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P09 | 295 | 89.5% | 89.5% | +0.1 | 100% | ❌ 10 pts to go |
| P10R | 97211 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P10 | 2658 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P11 | 12828 | 0.7% | 0.7% | -0.2 | 60% | ❌ 59 pts to go |
| P12 | 7 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P13 | 17816 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `currency`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 106 | 39.6% | 39.6% | -4.7 | n/a | no target |
| P01T | 366 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P01_GOLD | 625 | 72.8% | 72.8% | +0.0 | 100% | ❌ 27 pts to go |
| P02 | 470 | 65.7% | 65.7% | -0.8 | 100% | ❌ 34 pts to go |
| P03 | 257 | 60.3% | 60.3% | -0.2 | n/a | no target |
| P04 | 3818 | 24.9% | 24.9% | -2.9 | 95% | ❌ 70 pts to go |
| P05 | 423 | 33.1% | 33.1% | +0.1 | 80% | ❌ 47 pts to go |
| P06M | 11132 | 41.6% | 41.6% | -8.5 | n/a | no target |
| P06T | 65815 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06 | 298 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P07 | 800 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P08 | 25619 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P09 | 295 | 92.5% | 92.5% | -0.2 | 100% | 🟡 8 pts to go |
| P10R | 97211 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P10 | 2658 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P11 | 12828 | 0.7% | 0.7% | -0.3 | n/a | no target |
| P12 | 7 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P13 | 17816 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `start_date`

> ceiling: most award notices publish an award date, not a start date; start_date carries the signature date when the source gives one, labelled

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 106 | 81.1% | 81.1% | +2.7 | n/a | no target |
| P01T | 366 | 0.3% | 0.3% | +0.0 | n/a | no target |
| P01_GOLD | 625 | 51.7% | 51.7% | +0.1 | 85% | ❌ 33 pts to go |
| P02 | 470 | 57.0% | 57.0% | -0.6 | 90% | ❌ 33 pts to go |
| P03 | 257 | 44.0% | 44.0% | -0.1 | 85% | ❌ 41 pts to go |
| P04 | 3818 | 27.2% | 27.2% | -3.2 | 90% | ❌ 63 pts to go |
| P05 | 423 | 33.1% | 33.1% | +0.3 | 75% | ❌ 42 pts to go |
| P06M | 11132 | 90.0% | 90.0% | -0.4 | n/a | no target |
| P06T | 65815 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06 | 298 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P07 | 800 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P08 | 25619 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P09 | 295 | 85.1% | 85.1% | +0.0 | 95% | 🟡 10 pts to go |
| P10R | 97211 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P10 | 2658 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P11 | 12828 | 0.6% | 0.6% | -0.2 | n/a | no target |
| P12 | 7 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P13 | 17816 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `end_date`

> ceiling: an inferred end (award date + published duration) is labelled as such; sources without a duration leave end_date empty — the honest ceiling. P09 is BY DEFINITION the rows whose end date is not published (older SEAO contracts with no closing notice): its end_date / duration targets cannot be met without inventing a date

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 106 | 81.1% | 81.1% | +1.7 | n/a | no target |
| P01T | 366 | 0.3% | 0.3% | +0.0 | n/a | no target |
| P01_GOLD | 625 | 51.8% | 51.8% | +0.0 | 85% | ❌ 33 pts to go |
| P02 | 470 | 52.1% | 52.1% | -0.6 | 90% | ❌ 38 pts to go |
| P03 | 257 | 45.1% | 45.1% | -0.2 | 85% | ❌ 40 pts to go |
| P04 | 3818 | 23.2% | 23.2% | -2.8 | 90% | ❌ 67 pts to go |
| P05 | 423 | 43.3% | 43.3% | +0.4 | 75% | ❌ 32 pts to go |
| P06M | 11132 | 82.0% | 82.0% | -1.7 | n/a | no target |
| P06T | 65815 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06 | 298 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P07 | 800 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P08 | 25619 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P09 | 295 | 0.3% | 0.3% | +0.0 | 95% | ❌ 95 pts to go |
| P10R | 97211 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P10 | 2658 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P11 | 12828 | 0.5% | 0.5% | -0.2 | n/a | no target |
| P12 | 7 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P13 | 17816 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `contract_title`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 106 | 87.7% | 87.7% | +2.1 | n/a | no target |
| P01T | 366 | 92.1% | 92.1% | -0.1 | n/a | no target |
| P01_GOLD | 625 | 85.4% | 85.4% | -0.1 | 100% | ❌ 15 pts to go |
| P02 | 470 | 74.9% | 74.9% | -0.8 | 100% | ❌ 25 pts to go |
| P03 | 257 | 91.4% | 91.4% | -0.8 | n/a | no target |
| P04 | 3818 | 45.8% | 45.8% | -5.7 | 95% | ❌ 49 pts to go |
| P05 | 423 | 77.5% | 77.5% | -0.3 | 95% | ❌ 18 pts to go |
| P06M | 11132 | 98.6% | 98.6% | +0.3 | n/a | no target |
| P06T | 65815 | 83.4% | 83.4% | -0.3 | n/a | no target |
| P06 | 298 | 25.5% | 25.5% | -0.7 | n/a | no target |
| P07 | 800 | 17.1% | 17.1% | -2.0 | n/a | no target |
| P08 | 25619 | 9.7% | 9.8% | -1.3 | n/a | no target |
| P09 | 295 | 98.6% | 98.6% | -0.1 | 100% | 🟡 1 pts to go |
| P10R | 97211 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P10 | 2658 | 71.2% | 71.2% | -0.5 | n/a | no target |
| P11 | 12828 | 12.5% | 12.5% | -3.6 | n/a | no target |
| P12 | 7 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P13 | 17816 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `contract_description`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 106 | 87.7% | 87.7% | +2.1 | n/a | no target |
| P01T | 366 | 92.1% | 92.1% | -0.1 | n/a | no target |
| P01_GOLD | 625 | 88.6% | 88.6% | -0.1 | 100% | ❌ 11 pts to go |
| P02 | 470 | 76.0% | 76.2% | -0.8 | 100% | ❌ 24 pts to go |
| P03 | 257 | 92.2% | 92.2% | -0.8 | n/a | no target |
| P04 | 3818 | 49.0% | 49.0% | -6.1 | 95% | ❌ 46 pts to go |
| P05 | 423 | 90.1% | 90.1% | -0.1 | 70% | ✅ met |
| P06M | 11132 | 98.6% | 98.6% | +0.3 | n/a | no target |
| P06T | 65815 | 83.4% | 83.4% | -0.3 | n/a | no target |
| P06 | 298 | 25.5% | 25.5% | -0.7 | n/a | no target |
| P07 | 800 | 17.1% | 17.1% | -2.0 | n/a | no target |
| P08 | 25619 | 9.7% | 9.8% | -1.3 | n/a | no target |
| P09 | 295 | 98.6% | 98.6% | -0.1 | 100% | 🟡 1 pts to go |
| P10R | 97211 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P10 | 2658 | 71.2% | 71.2% | -0.5 | n/a | no target |
| P11 | 12828 | 12.5% | 12.5% | -3.6 | n/a | no target |
| P12 | 7 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P13 | 17816 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `number_of_bids`

> ceiling: published by some portals only (bids&tenders submission lists, Biddingo bidder lists); federal proactive disclosure does not publish bid counts

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 106 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P01T | 366 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P01_GOLD | 625 | 16.8% | 16.8% | +0.0 | 60% | ❌ 43 pts to go · rows from a source that publishes bids: 363 rows, 28.9% filled |
| P02 | 470 | 11.1% | 11.1% | -0.1 | n/a | no target · rows from a source that publishes bids: 290 rows, 17.9% filled |
| P03 | 257 | 13.2% | 13.2% | -0.1 | n/a | no target · rows from a source that publishes bids: 139 rows, 24.5% filled |
| P04 | 3818 | 1.4% | 1.4% | -0.2 | n/a | no target · rows from a source that publishes bids: 872 rows, 6.3% filled |
| P05 | 423 | 2.8% | 2.8% | -0.2 | n/a | no target · rows from a source that publishes bids: 51 rows, 23.5% filled |
| P06M | 11132 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06T | 65815 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06 | 298 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P07 | 800 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P08 | 25619 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P09 | 295 | 3.1% | 3.1% | +0.1 | n/a | no target · rows from a source that publishes bids: 282 rows, 3.2% filled |
| P10R | 97211 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P10 | 2658 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P11 | 12828 | 0.1% | 0.1% | +0.0 | n/a | no target · rows from a source that publishes bids: 87 rows, 12.6% filled |
| P12 | 7 | 0.0% | 0.0% | +0.0 | n/a | no target · rows from a source that publishes bids: 7 rows, 0.0% filled |
| P13 | 17816 | 0.0% | 0.0% | +0.0 | n/a | no target |

## 6. history

### `average_contract_duration_days`

> ceiling: needs two dates (or a published term) on the buyer's records; P09 rows (end date unpublished by definition) and buyers whose sources publish award dates only have no honest duration

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 106 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P01T | 366 | 0.3% | 98.4% | +0.0 | n/a | no target |
| P01_GOLD | 625 | 53.3% | 82.4% | +0.1 | 90% | ❌ 37 pts to go |
| P02 | 470 | 51.9% | 87.7% | -0.6 | 90% | ❌ 38 pts to go |
| P03 | 257 | 45.5% | 80.2% | -0.2 | 90% | ❌ 44 pts to go |
| P04 | 3818 | 18.7% | 94.1% | -2.2 | 90% | ❌ 71 pts to go |
| P05 | 423 | 0.0% | 83.2% | +0.0 | 90% | ❌ 90 pts to go |
| P06M | 11132 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P06T | 65815 | 0.0% | 99.9% | +0.0 | n/a | no target |
| P06 | 298 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P07 | 800 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P08 | 25619 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P09 | 295 | 2.4% | 4.1% | +0.1 | 90% | ❌ 88 pts to go |
| P10R | 97211 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P10 | 2658 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P11 | 12828 | 0.5% | 99.7% | -0.1 | n/a | no target |
| P12 | 7 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P13 | 17816 | 0.0% | 100.0% | +0.0 | n/a | no target |

### `commodity_distribution_top3`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 106 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P01T | 366 | 0.5% | 98.6% | -0.1 | n/a | no target |
| P01_GOLD | 625 | 25.9% | 55.0% | +0.0 | 90% | ❌ 64 pts to go |
| P02 | 470 | 51.1% | 86.8% | -0.5 | n/a | no target |
| P03 | 257 | 24.9% | 59.5% | -0.1 | n/a | no target |
| P04 | 3818 | 20.5% | 95.8% | -2.4 | n/a | no target |
| P05 | 423 | 0.5% | 83.7% | +0.0 | n/a | no target |
| P06M | 11132 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P06T | 65815 | 0.1% | 99.9% | +0.0 | n/a | no target |
| P06 | 298 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P07 | 800 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P08 | 25619 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P09 | 295 | 41.4% | 43.1% | -0.5 | n/a | no target |
| P10R | 97211 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P10 | 2658 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P11 | 12828 | 0.4% | 99.6% | -0.2 | n/a | no target |
| P12 | 7 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P13 | 17816 | 0.0% | 100.0% | +0.0 | n/a | no target |

### `year_over_year_spend_trend`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 106 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P01T | 366 | 1.6% | 99.7% | +0.1 | n/a | no target |
| P01_GOLD | 625 | 51.8% | 81.0% | +0.0 | 95% | ❌ 43 pts to go |
| P02 | 470 | 56.0% | 91.7% | -0.6 | n/a | no target |
| P03 | 257 | 47.9% | 82.5% | -0.1 | n/a | no target |
| P04 | 3818 | 20.7% | 96.0% | -2.4 | n/a | no target |
| P05 | 423 | 4.5% | 87.7% | -0.2 | n/a | no target |
| P06M | 11132 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P06T | 65815 | 0.1% | 100.0% | +0.0 | n/a | no target |
| P06 | 298 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P07 | 800 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P08 | 25619 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P09 | 295 | 63.7% | 65.4% | -0.3 | n/a | no target |
| P10R | 97211 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P10 | 2658 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P11 | 12828 | 0.5% | 99.7% | -0.1 | n/a | no target |
| P12 | 7 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P13 | 17816 | 0.0% | 100.0% | +0.0 | n/a | no target |

## 7. mail security

### `mta_sts`

> ceiling: DNS-only check; 'no record' counts as checked

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 106 | 98.1% | 98.1% | -1.9 | 100% | 🟡 2 pts to go |
| P01T | 366 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P01_GOLD | 625 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P02 | 470 | 99.8% | 99.8% | -0.2 | 100% | 🟡 0 pts to go |
| P03 | 257 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P04 | 3818 | 99.2% | 99.2% | -0.8 | 100% | 🟡 1 pts to go |
| P05 | 423 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P06M | 11132 | 94.4% | 94.4% | -5.6 | 100% | 🟡 6 pts to go |
| P06T | 65815 | 99.8% | 99.8% | -0.2 | 100% | 🟡 0 pts to go |
| P06 | 298 | 99.7% | 99.7% | -0.3 | 100% | 🟡 0 pts to go |
| P07 | 800 | 99.4% | 99.4% | -0.6 | 100% | 🟡 1 pts to go |
| P08 | 25619 | 99.1% | 99.1% | -0.9 | 100% | 🟡 1 pts to go |
| P09 | 295 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P10R | 97211 | 99.5% | 99.5% | -0.5 | 100% | 🟡 0 pts to go |
| P10 | 2658 | 99.7% | 99.7% | -0.3 | 100% | 🟡 0 pts to go |
| P11 | 12828 | 99.8% | 99.8% | -0.2 | 100% | 🟡 0 pts to go |
| P12 | 7 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P13 | 17816 | 99.3% | 99.3% | -0.7 | 100% | 🟡 1 pts to go |

### `tls_rpt`

> ceiling: DNS-only check; 'no record' counts as checked

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 106 | 98.1% | 98.1% | -1.9 | 100% | 🟡 2 pts to go |
| P01T | 366 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P01_GOLD | 625 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P02 | 470 | 99.8% | 99.8% | -0.2 | 100% | 🟡 0 pts to go |
| P03 | 257 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P04 | 3818 | 99.2% | 99.2% | -0.8 | 100% | 🟡 1 pts to go |
| P05 | 423 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P06M | 11132 | 94.4% | 94.4% | -5.6 | 100% | 🟡 6 pts to go |
| P06T | 65815 | 99.8% | 99.8% | -0.2 | 100% | 🟡 0 pts to go |
| P06 | 298 | 99.7% | 99.7% | -0.3 | 100% | 🟡 0 pts to go |
| P07 | 800 | 99.4% | 99.4% | -0.6 | 100% | 🟡 1 pts to go |
| P08 | 25619 | 99.1% | 99.1% | -0.9 | 100% | 🟡 1 pts to go |
| P09 | 295 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P10R | 97211 | 99.5% | 99.5% | -0.5 | 100% | 🟡 0 pts to go |
| P10 | 2658 | 99.7% | 99.7% | -0.3 | 100% | 🟡 0 pts to go |
| P11 | 12828 | 99.8% | 99.8% | -0.2 | 100% | 🟡 0 pts to go |
| P12 | 7 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P13 | 17816 | 99.3% | 99.3% | -0.7 | 100% | 🟡 1 pts to go |

### `bimi`

> ceiling: DNS-only check; 'no record' counts as checked

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 106 | 98.1% | 98.1% | -1.9 | 100% | 🟡 2 pts to go |
| P01T | 366 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P01_GOLD | 625 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P02 | 470 | 99.8% | 99.8% | -0.2 | 100% | 🟡 0 pts to go |
| P03 | 257 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P04 | 3818 | 99.2% | 99.2% | -0.8 | 100% | 🟡 1 pts to go |
| P05 | 423 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P06M | 11132 | 94.4% | 94.4% | -5.6 | 100% | 🟡 6 pts to go |
| P06T | 65815 | 99.8% | 99.8% | -0.2 | 100% | 🟡 0 pts to go |
| P06 | 298 | 99.7% | 99.7% | -0.3 | 100% | 🟡 0 pts to go |
| P07 | 800 | 99.4% | 99.4% | -0.6 | 100% | 🟡 1 pts to go |
| P08 | 25619 | 99.1% | 99.1% | -0.9 | 100% | 🟡 1 pts to go |
| P09 | 295 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P10R | 97211 | 99.5% | 99.5% | -0.5 | 100% | 🟡 0 pts to go |
| P10 | 2658 | 99.7% | 99.7% | -0.3 | 100% | 🟡 0 pts to go |
| P11 | 12828 | 99.8% | 99.8% | -0.2 | 100% | 🟡 0 pts to go |
| P12 | 7 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P13 | 17816 | 99.3% | 99.3% | -0.7 | 100% | 🟡 1 pts to go |

