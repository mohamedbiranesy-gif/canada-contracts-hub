# Coverage vs the downstream team's targets — 2026-11-11

Benchmarks (field × package with a numeric target): **94 of 446 met** (21.1%); 54 within 10 points; 298 further away.
A cell counts as filled only when it carries a value: blank, `not_published`, `not_found_yet` and label-only cells ("no identifier published …", "no dataset record …", "0 in the contract dataset …") do not count; the DNS checks count when checked. `any` = share of non-blank cells incl. such labels. Δ = change since the previous build in `coord/results/coverage_history.csv`.
Rows per package: P01M 126, P01T 370, P01_GOLD 625, P02 471, P03 257, P04 3839, P05 424, P06M 13001, P06T 67038, P06 297, P07 800, P08 25630, P09 295, P10R 98583, P10 2685, P11 14979, P12 7, P13 18028

## Invoice-grade readiness (the row as an invoice header: bill-to, submit-to, references, terms, tax, vendor identity, follow-up)

| package | rows | all 11 elements | ≥ 9 of 11 | median elements | most-missing element |
|---|---|---|---|---|---|
| P01M | 126 | 0.0% | 13.5% | 8 | vendor GST/HST number (114 rows) |
| P01T | 370 | 0.8% | 21.6% | 7 | payment terms (296 rows) |
| P01_GOLD | 625 | 24.0% | 70.7% | 9 | payment terms (214 rows) |
| P02 | 471 | 7.2% | 54.1% | 9 | PO rule (360 rows) |
| P03 | 257 | 14.8% | 58.0% | 9 | PO rule (123 rows) |
| P04 | 3839 | 1.2% | 16.0% | 6 | PO rule (3647 rows) |
| P05 | 424 | 1.2% | 17.5% | 7 | payment terms (349 rows) |
| P06M | 13001 | 0.0% | 1.2% | 7 | PO rule (12968 rows) |
| P06T | 67038 | 0.0% | 3.7% | 7 | PO rule (66690 rows) |
| P06 | 297 | 0.0% | 8.4% | 6 | reference to quote (PO / contract / vendor id) (297 rows) |
| P07 | 800 | 0.0% | 1.8% | 6 | reference to quote (PO / contract / vendor id) (800 rows) |
| P08 | 25630 | 0.0% | 0.3% | 5 | reference to quote (PO / contract / vendor id) (25630 rows) |
| P09 | 295 | 1.0% | 44.4% | 8 | payment terms (276 rows) |
| P10R | 98583 | 0.0% | 21.4% | 7 | PO rule (98546 rows) |
| P10 | 2685 | 0.0% | 0.9% | 5 | reference to quote (PO / contract / vendor id) (2685 rows) |
| P11 | 14979 | 0.0% | 1.8% | 6 | PO rule (14875 rows) |
| P12 | 7 | 0.0% | 28.6% | 8 | PO rule (7 rows) |
| P13 | 18028 | 0.0% | 0.2% | 7 | reference to quote (PO / contract / vendor id) (18028 rows) |

## AP grade (how stringently the row's accounts-payable data meets what an invoice needs; A = invoicing mailbox referee-confirmed on the buyer's own domain with MX, legal name, address, PO rule and terms all published, no penalties)

| package | rows | A | B | C | D | E | median ap_score |
|---|---|---|---|---|---|---|---|
| P01M | 126 | 10 | 12 | 104 | 0 | 0 | 71 |
| P01T | 370 | 30 | 61 | 279 | 0 | 0 | 71 |
| P01_GOLD | 625 | 226 | 191 | 208 | 0 | 0 | 82 |
| P02 | 471 | 0 | 192 | 279 | 0 | 0 | 66 |
| P03 | 257 | 0 | 0 | 246 | 11 | 0 | 57 |
| P04 | 3839 | 0 | 0 | 3194 | 645 | 0 | 46 |
| P05 | 424 | 15 | 30 | 365 | 14 | 0 | 51 |
| P06M | 13001 | 0 | 3 | 12941 | 57 | 0 | 46 |
| P06T | 67038 | 0 | 41 | 56159 | 10838 | 0 | 40 |
| P06 | 297 | 20 | 47 | 230 | 0 | 0 | 69 |
| P07 | 800 | 0 | 27 | 748 | 25 | 0 | 53 |
| P08 | 25630 | 0 | 0 | 21720 | 3910 | 0 | 43 |
| P09 | 295 | 3 | 12 | 278 | 2 | 0 | 53 |
| P10R | 98583 | 2 | 12 | 69264 | 29305 | 0 | 38 |
| P10 | 2685 | 2 | 15 | 2025 | 643 | 0 | 43 |
| P11 | 14979 | 6 | 11 | 43 | 0 | 14919 | 23 |
| P12 | 7 | 0 | 0 | 7 | 0 | 0 | 54 |
| P13 | 18028 | 0 | 15 | 14663 | 3350 | 0 | 43 |

### AP payability (confirmed channel + bill-to legal name and address + the buyer's reference rule + tax treatment known)

| package | rows | payable today | % | most common gap |
|---|---|---|---|---|
| P01M | 126 | 102 | 81.0% | the buyer's PO / reference rule (13) |
| P01T | 370 | 205 | 55.4% | bill-to legal name and address (118) |
| P01_GOLD | 625 | 464 | 74.2% | bill-to legal name and address (107) |
| P02 | 471 | 312 | 66.2% | the buyer's PO / reference rule (86) |
| P03 | 257 | 0 | 0.0% | a confirmed invoicing / AP or finance channel (257) |
| P04 | 3839 | 0 | 0.0% | a confirmed invoicing / AP or finance channel (3839) |
| P05 | 424 | 47 | 11.1% | a confirmed invoicing / AP or finance channel (337) |
| P06M | 13001 | 126 | 1.0% | a confirmed invoicing / AP or finance channel (12826) |
| P06T | 67038 | 425 | 0.6% | a confirmed invoicing / AP or finance channel (66052) |
| P06 | 297 | 43 | 14.5% | the buyer's PO / reference rule (124) |
| P07 | 800 | 10 | 1.2% | bill-to legal name and address (351) |
| P08 | 25630 | 0 | 0.0% | a confirmed invoicing / AP or finance channel (25630) |
| P09 | 295 | 41 | 13.9% | a confirmed invoicing / AP or finance channel (245) |
| P10R | 98583 | 510 | 0.5% | a confirmed invoicing / AP or finance channel (97438) |
| P10 | 2685 | 5 | 0.2% | a confirmed invoicing / AP or finance channel (2588) |
| P11 | 14979 | 11 | 0.1% | a confirmed invoicing / AP or finance channel (14919) |
| P12 | 7 | 3 | 42.9% | a confirmed invoicing / AP or finance channel (4) |
| P13 | 18028 | 7 | 0.0% | a confirmed invoicing / AP or finance channel (17686) |

### Pay on sight (an invoice generated from the row would clear AP: confirmed invoicing / AP or finance channel, bill-to legal name + address, vendor legal name + GST/HST number + remit-to address, tax treatment and currency known — published or labelled-derived; the buyer's reference rule is reported separately)

| package | rows | pay on sight | % | + reference rule not published | routed (general inbox only) | most common gap |
|---|---|---|---|---|---|---|
| P01M | 126 | 6 | 4.8% | 5 | 0 | the vendor's GST/HST number (BN9) (113) |
| P01T | 370 | 66 | 17.8% | 26 | 0 | the vendor's GST/HST number (BN9) (206) |
| P01_GOLD | 625 | 396 | 63.4% | 12 | 0 | the vendor's GST/HST number (BN9) (154) |
| P02 | 471 | 211 | 44.8% | 23 | 0 | the vendor's GST/HST number (BN9) (206) |
| P03 | 257 | 16 | 6.2% | 0 | 133 | an invoicing / AP or finance mailbox (only a purchasing / general inbo (87) |
| P04 | 3839 | 42 | 1.1% | 8 | 810 | an invoicing / AP or finance mailbox (only a purchasing / general inbo (2922) |
| P05 | 424 | 21 | 5.0% | 7 | 110 | an invoicing / AP or finance mailbox (only a purchasing / general inbo (220) |
| P06M | 13001 | 1 | 0.0% | 10 | 147 | an invoicing / AP or finance mailbox (only a purchasing / general inbo (12659) |
| P06T | 67038 | 95 | 0.1% | 97 | 12234 | an invoicing / AP or finance mailbox (only a purchasing / general inbo (53661) |
| P06 | 297 | 16 | 5.4% | 29 | 0 | the vendor's GST/HST number (BN9) (175) |
| P07 | 800 | 5 | 0.6% | 75 | 28 | the vendor's GST/HST number (BN9) (422) |
| P08 | 25630 | 1 | 0.0% | 8 | 2929 | an invoicing / AP or finance mailbox (only a purchasing / general inbo (22637) |
| P09 | 295 | 38 | 12.9% | 1 | 119 | an invoicing / AP or finance mailbox (only a purchasing / general inbo (117) |
| P10R | 98583 | 845 | 0.9% | 0 | 53246 | an invoicing / AP or finance mailbox (only a purchasing / general inbo (44130) |
| P10 | 2685 | 4 | 0.1% | 20 | 394 | an invoicing / AP or finance mailbox (only a purchasing / general inbo (2164) |
| P11 | 14979 | 11 | 0.1% | 12 | 0 | a confirmed invoicing / AP or finance channel (14886) |
| P12 | 7 | 1 | 14.3% | 0 | 2 | the vendor's GST/HST number (BN9) (2) |
| P13 | 18028 | 9 | 0.0% | 247 | 10568 | an invoicing / AP or finance mailbox (only a purchasing / general inbo (7078) |
| **all** | 247455 | 1784 | 0.7% | 580 | 80720 | |

### What still blocks grade A (rows per missing element; a row counts under every element it lacks)

| package | rows not A | referee confirmation of the mailbox | an invoicing / AP mailbox (not finance / procurement / general) | a mailbox on the buyer's own domain | MX record for the mailbox domain | published bill-to legal name | invoice / billing address | published PO rule | published payment terms | clear the penalty |
|---|---|---|---|---|---|---|---|---|---|---|
| P01M | 116 | 0 | 0 | 0 | 60 | 8 | 0 | 107 | 111 | 1 |
| P01T | 340 | 0 | 0 | 0 | 153 | 104 | 32 | 285 | 298 | 31 |
| P01_GOLD | 399 | 0 | 0 | 0 | 11 | 89 | 33 | 194 | 228 | 57 |
| P02 | 471 | 0 | 471 | 0 | 47 | 63 | 19 | 360 | 290 | 22 |
| P03 | 257 | 0 | 257 | 0 | 14 | 42 | 24 | 123 | 129 | 25 |
| P04 | 3839 | 0 | 3839 | 0 | 1808 | 1587 | 925 | 3647 | 3387 | 131 |
| P05 | 409 | 0 | 357 | 0 | 74 | 93 | 47 | 340 | 351 | 50 |
| P06M | 13001 | 0 | 13001 | 0 | 8203 | 1359 | 106 | 12968 | 12930 | 78 |
| P06T | 67038 | 0 | 67038 | 0 | 51816 | 36471 | 14758 | 66690 | 65576 | 404 |
| P06 | 277 | 0 | 0 | 0 | 119 | 97 | 51 | 210 | 240 | 4 |
| P07 | 800 | 0 | 800 | 0 | 471 | 385 | 136 | 751 | 752 | 14 |
| P08 | 25630 | 0 | 25630 | 0 | 18815 | 13781 | 5226 | 25391 | 25058 | 228 |
| P09 | 292 | 0 | 271 | 0 | 9 | 68 | 2 | 266 | 278 | 44 |
| P10R | 98581 | 0 | 98410 | 0 | 76388 | 62019 | 38886 | 98546 | 98398 | 24 |
| P10 | 2683 | 0 | 2646 | 0 | 1282 | 1348 | 928 | 2616 | 2567 | 115 |
| P11 | 14973 | 14919 | 14858 | 0 | 13540 | 9547 | 949 | 14875 | 14478 | 39 |
| P12 | 7 | 0 | 6 | 0 | 0 | 2 | 0 | 7 | 7 | 0 |
| P13 | 18028 | 0 | 17925 | 0 | 9069 | 9603 | 4175 | 17992 | 17985 | 20 |

## Where the work is (largest gaps in rows still needed)

| field | package | now | target | rows needed |
|---|---|---|---|---|
| buyer_ap_cycle_published | P10R | 0.0% | 20% | 19690 |
| ap_system_hint | P10R | 0.2% | 20% | 19517 |
| buyer_tax_exempt_status | P10R | 0.0% | 15% | 14758 |
| buyer_esignature_preference | P10R | 0.0% | 15% | 14741 |
| vendor_registered_address | P08 | 13.6% | 70% | 14450 |
| buyer_payment_method_preference | P10R | 0.6% | 15% | 14153 |
| buyer_ap_cycle_published | P06T | 0.0% | 20% | 13384 |
| ap_system_hint | P06T | 0.7% | 20% | 12946 |
| vendor_phone | P11 | 4.8% | 75% | 10511 |
| vendor_emails | P11 | 3.5% | 70% | 9961 |
| buyer_esignature_preference | P06T | 0.2% | 15% | 9913 |
| buyer_tax_exempt_status | P06T | 0.3% | 15% | 9869 |
| buyer_payment_method_preference | P06T | 0.7% | 15% | 9615 |
| contract_value | P11 | 0.6% | 60% | 8903 |
| award_or_notice_id | P11 | 0.6% | 60% | 8902 |
| vendor_bn9 | P08 | 15.5% | 50% | 8838 |
| buyer_phone | P08 | 62.8% | 95% | 8253 |
| contract_or_agreement_number | P11 | 8.7% | 60% | 7683 |
| invoice_reference_hint | P11 | 9.3% | 60% | 7596 |
| commodity_codes | P11 | 0.4% | 50% | 7429 |
| buyer_legal_name_as_published | P08 | 46.2% | 75% | 7374 |
| buyer_phone | P11 | 28.3% | 75% | 6998 |
| buyer_phone | P13 | 58.0% | 95% | 6666 |
| buyer_logo_url | P08 | 74.2% | 100% | 6624 |
| invoice_reference_hint | P08 | 0.9% | 25% | 6169 |
| vendor_phone | P08 | 61.6% | 85% | 6010 |
| vendor_emails | P08 | 51.6% | 75% | 5988 |
| solicitation_or_tender_number | P11 | 0.5% | 40% | 5913 |
| buyer_logo_url | P13 | 64.1% | 95% | 5564 |
| buyer_bn_as_published | P08 | 13.8% | 35% | 5435 |
| buyer_ap_cycle_published | P08 | 0.0% | 20% | 5119 |
| ap_system_hint | P08 | 0.8% | 20% | 4916 |
| vendor_trading_name | P08 | 32.5% | 50% | 4478 |
| vendor_logo_url | P08 | 83.0% | 100% | 4353 |
| buyer_legal_name_as_published | P11 | 36.3% | 65% | 4305 |
| buyer_address | P08 | 79.6% | 95% | 3950 |
| buyer_esignature_preference | P08 | 0.4% | 15% | 3755 |
| buyer_tax_exempt_status | P08 | 0.4% | 15% | 3751 |
| buyer_payment_method_preference | P08 | 0.5% | 15% | 3705 |
| buyer_logo_url | P11 | 55.5% | 80% | 3674 |

## 1. identifiers

### `invoice_reference_hint`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 126 | 88.1% | 88.1% | -0.6 | 50% | ✅ met |
| P01T | 370 | 88.6% | 88.6% | -0.9 | 50% | ✅ met |
| P01_GOLD | 625 | 92.2% | 94.4% | +0.0 | 95% | 🟡 3 pts to go |
| P02 | 471 | 72.8% | 74.3% | -1.0 | 95% | ❌ 22 pts to go |
| P03 | 257 | 81.7% | 84.8% | -0.3 | 95% | ❌ 13 pts to go |
| P04 | 3839 | 29.0% | 30.4% | -3.8 | 90% | ❌ 61 pts to go |
| P05 | 424 | 38.7% | 41.5% | +0.1 | 70% | ❌ 31 pts to go |
| P06M | 13001 | 91.2% | 91.2% | -1.4 | n/a | no target |
| P06T | 67038 | 79.3% | 79.3% | -1.0 | n/a | no target |
| P06 | 297 | 29.3% | 29.3% | -2.4 | 30% | 🟡 1 pts to go |
| P07 | 800 | 6.1% | 6.1% | -0.8 | 30% | ❌ 24 pts to go |
| P08 | 25630 | 0.9% | 0.9% | -0.2 | 25% | ❌ 24 pts to go |
| P09 | 295 | 99.0% | 99.7% | +0.0 | 100% | 🟡 1 pts to go |
| P10R | 98583 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P10 | 2685 | 2.6% | 2.6% | +0.0 | 25% | ❌ 22 pts to go |
| P11 | 14979 | 9.3% | 9.4% | -4.3 | 60% | ❌ 51 pts to go |
| P12 | 7 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P13 | 18028 | 0.2% | 0.2% | +0.0 | 0% by design | — leave (by design) |

### `po_number_as_published`

> ceiling: a purchase-order number exists only where the buyer publishes PO-level data (Montréal, Laval, Toronto open data so far) or the record itself carries one; most sources publish awards, not POs — the target cannot be reached from public data for most buyers

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 126 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P01T | 370 | 0.0% | 0.0% | +0.0 | 10% | 🟡 10 pts to go |
| P01_GOLD | 625 | 6.1% | 6.1% | +0.0 | 50% | ❌ 44 pts to go |
| P02 | 471 | 6.2% | 6.2% | +0.0 | 50% | ❌ 44 pts to go |
| P03 | 257 | 1.6% | 1.6% | +0.0 | 40% | ❌ 38 pts to go |
| P04 | 3839 | 0.5% | 0.5% | +0.0 | 30% | ❌ 30 pts to go |
| P05 | 424 | 0.2% | 0.2% | +0.0 | 20% | ❌ 20 pts to go |
| P06M | 13001 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06T | 67038 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06 | 297 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P07 | 800 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P08 | 25630 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P09 | 295 | 0.7% | 0.7% | +0.0 | 50% | ❌ 49 pts to go |
| P10R | 98583 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P10 | 2685 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P11 | 14979 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P12 | 7 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P13 | 18028 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `contract_or_agreement_number`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 126 | 82.5% | 82.5% | +1.1 | n/a | no target |
| P01T | 370 | 71.6% | 71.6% | +1.1 | 50% | ✅ met |
| P01_GOLD | 625 | 66.9% | 66.9% | +0.0 | 85% | ❌ 18 pts to go |
| P02 | 471 | 64.1% | 64.1% | -0.8 | 90% | ❌ 26 pts to go |
| P03 | 257 | 61.1% | 61.1% | -0.2 | 85% | ❌ 24 pts to go |
| P04 | 3839 | 26.8% | 26.8% | -3.3 | 85% | ❌ 58 pts to go |
| P05 | 424 | 29.0% | 29.0% | +0.0 | 60% | ❌ 31 pts to go |
| P06M | 13001 | 91.1% | 91.1% | -1.3 | n/a | no target |
| P06T | 67038 | 79.0% | 79.0% | -1.0 | n/a | no target |
| P06 | 297 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P07 | 800 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P08 | 25630 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P09 | 295 | 95.9% | 95.9% | -0.1 | 100% | 🟡 4 pts to go |
| P10R | 98583 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P10 | 2685 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P11 | 14979 | 8.7% | 8.7% | -4.0 | 60% | ❌ 51 pts to go |
| P12 | 7 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P13 | 18028 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `solicitation_or_tender_number`

> ceiling: SEAO's 'numero' is the organisation's own reference for the notice (SEAO data dictionary) and is reported here; sources that publish awards under a tender number only (bids&tenders, SaskTenders, BC) also carry it as the contract reference, labelled

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 126 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P01T | 370 | 0.0% | 0.0% | +0.0 | 30% | ❌ 30 pts to go |
| P01_GOLD | 625 | 50.7% | 50.7% | +0.1 | 80% | ❌ 29 pts to go |
| P02 | 471 | 56.3% | 56.3% | -0.7 | 60% | 🟡 4 pts to go |
| P03 | 257 | 51.4% | 51.4% | -0.2 | 80% | ❌ 29 pts to go |
| P04 | 3839 | 22.2% | 22.2% | -2.8 | 50% | ❌ 28 pts to go |
| P05 | 424 | 11.6% | 11.6% | -0.3 | 40% | ❌ 28 pts to go |
| P06M | 13001 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06T | 67038 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06 | 297 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P07 | 800 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P08 | 25630 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P09 | 295 | 83.1% | 83.1% | -0.4 | 50% | ✅ met |
| P10R | 98583 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P10 | 2685 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P11 | 14979 | 0.5% | 0.5% | -0.3 | 40% | ❌ 40 pts to go |
| P12 | 7 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P13 | 18028 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `award_or_notice_id`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 126 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P01T | 370 | 0.3% | 0.3% | +0.0 | n/a | no target |
| P01_GOLD | 625 | 60.5% | 60.5% | +0.1 | 85% | ❌ 24 pts to go |
| P02 | 471 | 55.6% | 55.6% | -0.7 | 90% | ❌ 34 pts to go |
| P03 | 257 | 59.9% | 59.9% | -0.3 | 85% | ❌ 25 pts to go |
| P04 | 3839 | 22.9% | 22.9% | -2.9 | 85% | ❌ 62 pts to go |
| P05 | 424 | 19.8% | 19.8% | -0.1 | 50% | ❌ 30 pts to go |
| P06M | 13001 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06T | 67038 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06 | 297 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P07 | 800 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P08 | 25630 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P09 | 295 | 96.9% | 96.9% | -0.1 | 100% | 🟡 3 pts to go |
| P10R | 98583 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P10 | 2685 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P11 | 14979 | 0.6% | 0.6% | -0.3 | 60% | ❌ 59 pts to go |
| P12 | 7 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P13 | 18028 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `buyer_vendor_id`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 126 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P01T | 370 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P01_GOLD | 625 | 13.0% | 13.0% | +0.1 | 60% | ❌ 47 pts to go |
| P02 | 471 | 5.9% | 5.9% | -0.1 | 50% | ❌ 44 pts to go |
| P03 | 257 | 8.6% | 8.6% | +0.0 | 50% | ❌ 41 pts to go |
| P04 | 3839 | 1.8% | 1.8% | -0.2 | 40% | ❌ 38 pts to go |
| P05 | 424 | 0.7% | 0.7% | -0.2 | 20% | ❌ 19 pts to go |
| P06M | 13001 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06T | 67038 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06 | 297 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P07 | 800 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P08 | 25630 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P09 | 295 | 2.4% | 2.4% | +0.1 | 50% | ❌ 48 pts to go |
| P10R | 98583 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P10 | 2685 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P11 | 14979 | 0.1% | 0.1% | +0.0 | n/a | no target |
| P12 | 7 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P13 | 18028 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `commodity_codes`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 126 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P01T | 370 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P01_GOLD | 625 | 34.9% | 34.9% | +0.1 | 80% | ❌ 45 pts to go |
| P02 | 471 | 51.4% | 51.4% | -0.6 | 90% | ❌ 39 pts to go |
| P03 | 257 | 33.5% | 33.5% | -0.1 | 80% | ❌ 46 pts to go |
| P04 | 3839 | 20.9% | 20.9% | -2.7 | 85% | ❌ 64 pts to go |
| P05 | 424 | 5.4% | 5.4% | +0.0 | 50% | ❌ 45 pts to go |
| P06M | 13001 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06T | 67038 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06 | 297 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P07 | 800 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P08 | 25630 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P09 | 295 | 75.6% | 75.6% | -0.3 | 95% | ❌ 19 pts to go |
| P10R | 98583 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P10 | 2685 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P11 | 14979 | 0.4% | 0.4% | -0.2 | 50% | ❌ 50 pts to go |
| P12 | 7 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P13 | 18028 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `buyer_org_codes`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 126 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P01T | 370 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P01_GOLD | 625 | 8.5% | 8.5% | +0.0 | 50% | ❌ 42 pts to go |
| P02 | 471 | 6.2% | 6.2% | +0.0 | 50% | ❌ 44 pts to go |
| P03 | 257 | 1.9% | 1.9% | -0.1 | 30% | ❌ 28 pts to go |
| P04 | 3839 | 0.4% | 0.4% | -0.1 | 30% | ❌ 30 pts to go |
| P05 | 424 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06M | 13001 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06T | 67038 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06 | 297 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P07 | 800 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P08 | 25630 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P09 | 295 | 0.3% | 0.3% | +0.0 | n/a | no target |
| P10R | 98583 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P10 | 2685 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P11 | 14979 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P12 | 7 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P13 | 18028 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `records_with_this_vendor`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 126 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P01T | 370 | 100.0% | 100.0% | +0.0 | 60% | ✅ met |
| P01_GOLD | 625 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P02 | 471 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P03 | 257 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P04 | 3839 | 100.0% | 100.0% | +0.0 | 95% | ✅ met |
| P05 | 424 | 100.0% | 100.0% | +0.0 | 70% | ✅ met |
| P06M | 13001 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P06T | 67038 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P06 | 297 | 100.0% | 100.0% | +0.0 | 50% | ✅ met |
| P07 | 800 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P08 | 25630 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P09 | 295 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P10R | 98583 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P10 | 2685 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P11 | 14979 | 100.0% | 100.0% | +0.0 | 70% | ✅ met |
| P12 | 7 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P13 | 18028 | 0.0% | 0.0% | +0.0 | n/a | no target |

## 2. vendor

### `vendor_bn9`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 126 | 9.5% | 9.5% | -4.9 | 70% | ❌ 60 pts to go |
| P01T | 370 | 31.9% | 31.9% | -1.8 | 60% | ❌ 28 pts to go |
| P01_GOLD | 625 | 72.6% | 72.6% | -0.4 | 90% | ❌ 17 pts to go |
| P02 | 471 | 53.5% | 53.5% | -1.6 | 85% | ❌ 32 pts to go |
| P03 | 257 | 68.5% | 68.5% | -1.4 | 90% | ❌ 22 pts to go |
| P04 | 3839 | 31.4% | 31.4% | -1.1 | 75% | ❌ 44 pts to go |
| P05 | 424 | 50.5% | 50.5% | +0.6 | 50% | ✅ met |
| P06M | 13001 | 1.6% | 1.6% | -0.2 | n/a | no target |
| P06T | 67038 | 22.1% | 22.1% | +4.8 | n/a | no target |
| P06 | 297 | 25.3% | 25.3% | +2.5 | 40% | ❌ 15 pts to go |
| P07 | 800 | 19.4% | 19.4% | +3.0 | 50% | ❌ 31 pts to go |
| P08 | 25630 | 15.5% | 15.5% | +4.6 | 50% | ❌ 34 pts to go |
| P09 | 295 | 58.3% | 58.3% | +0.5 | 80% | ❌ 22 pts to go |
| P10R | 98583 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P10 | 2685 | 31.1% | 31.1% | +2.4 | 40% | 🟡 9 pts to go |
| P11 | 14979 | 93.9% | 93.9% | +2.8 | 60% | ✅ met |
| P12 | 7 | 42.9% | 42.9% | -19.6 | 85% | ❌ 42 pts to go |
| P13 | 18028 | 90.8% | 90.8% | -0.2 | 0% by design | — leave (by design) |

### `vendor_registered_address`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 126 | 56.3% | 56.3% | -10.7 | n/a | no target |
| P01T | 370 | 39.7% | 39.7% | +1.7 | n/a | no target |
| P01_GOLD | 625 | 70.6% | 70.6% | +0.2 | 95% | ❌ 24 pts to go |
| P02 | 471 | 73.0% | 73.0% | -0.8 | 95% | ❌ 22 pts to go |
| P03 | 257 | 71.6% | 71.6% | -0.3 | 95% | ❌ 23 pts to go |
| P04 | 3839 | 43.5% | 43.5% | -2.1 | 95% | ❌ 52 pts to go |
| P05 | 424 | 53.1% | 53.1% | -0.3 | 70% | ❌ 17 pts to go |
| P06M | 13001 | 43.4% | 43.4% | -11.2 | n/a | no target |
| P06T | 67038 | 31.4% | 31.4% | +1.1 | n/a | no target |
| P06 | 297 | 25.6% | 25.6% | +0.8 | 80% | ❌ 54 pts to go |
| P07 | 800 | 18.2% | 18.2% | +0.2 | 70% | ❌ 52 pts to go |
| P08 | 25630 | 13.6% | 13.6% | -0.5 | 70% | ❌ 56 pts to go |
| P09 | 295 | 87.1% | 87.1% | -0.4 | 100% | ❌ 13 pts to go |
| P10R | 98583 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P10 | 2685 | 32.5% | 32.5% | +0.0 | 70% | ❌ 38 pts to go |
| P11 | 14979 | 94.6% | 94.6% | +2.4 | 75% | ✅ met |
| P12 | 7 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P13 | 18028 | 16.3% | 16.3% | +16.3 | n/a | no target |

### `vendor_trading_name`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 126 | 19.0% | 19.0% | +2.5 | n/a | no target |
| P01T | 370 | 49.7% | 49.7% | +23.8 | n/a | no target |
| P01_GOLD | 625 | 49.6% | 49.6% | +1.7 | 60% | ❌ 10 pts to go |
| P02 | 471 | 54.8% | 54.8% | -0.5 | 60% | 🟡 5 pts to go |
| P03 | 257 | 54.5% | 54.5% | -0.6 | 60% | 🟡 6 pts to go |
| P04 | 3839 | 37.3% | 37.3% | +0.6 | 55% | ❌ 18 pts to go |
| P05 | 424 | 23.3% | 23.3% | +1.1 | 50% | ❌ 27 pts to go |
| P06M | 13001 | 7.3% | 7.3% | +3.7 | n/a | no target |
| P06T | 67038 | 60.7% | 60.7% | +33.7 | n/a | no target |
| P06 | 297 | 44.1% | 44.1% | +8.9 | n/a | no target |
| P07 | 800 | 38.2% | 38.2% | +5.0 | 55% | ❌ 17 pts to go |
| P08 | 25630 | 32.5% | 32.5% | +5.6 | 50% | ❌ 18 pts to go |
| P09 | 295 | 72.2% | 72.2% | +1.2 | 70% | ✅ met |
| P10R | 98583 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P10 | 2685 | 46.2% | 46.2% | +6.7 | 55% | 🟡 9 pts to go |
| P11 | 14979 | 95.8% | 95.8% | +3.8 | 50% | ✅ met |
| P12 | 7 | 100.0% | 100.0% | +12.5 | n/a | no target |
| P13 | 18028 | 74.0% | 74.0% | +74.0 | n/a | no target |

### `vendor_phone`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 126 | 50.0% | 50.0% | +35.6 | n/a | no target |
| P01T | 370 | 69.7% | 69.7% | +13.4 | n/a | no target |
| P01_GOLD | 625 | 46.1% | 46.1% | -1.8 | 70% | ❌ 24 pts to go |
| P02 | 471 | 51.8% | 51.8% | -2.2 | 70% | ❌ 18 pts to go |
| P03 | 257 | 47.9% | 47.9% | -1.7 | 70% | ❌ 22 pts to go |
| P04 | 3839 | 49.1% | 49.1% | +2.0 | 65% | ❌ 16 pts to go |
| P05 | 424 | 26.7% | 26.7% | -4.0 | 60% | ❌ 33 pts to go |
| P06M | 13001 | 37.1% | 37.1% | +33.6 | n/a | no target |
| P06T | 67038 | 73.1% | 73.1% | +9.3 | n/a | no target |
| P06 | 297 | 65.0% | 65.0% | +7.4 | 40% | ✅ met |
| P07 | 800 | 62.2% | 62.2% | +5.2 | 85% | ❌ 23 pts to go |
| P08 | 25630 | 61.6% | 61.6% | +4.7 | 85% | ❌ 23 pts to go |
| P09 | 295 | 54.6% | 54.6% | +1.1 | 85% | ❌ 30 pts to go |
| P10R | 98583 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P10 | 2685 | 62.2% | 62.2% | +1.2 | 85% | ❌ 23 pts to go |
| P11 | 14979 | 4.8% | 4.8% | -1.6 | 75% | ❌ 70 pts to go |
| P12 | 7 | 28.6% | 28.6% | +3.6 | n/a | no target |
| P13 | 18028 | 100.0% | 100.0% | +0.0 | 60% | ✅ met |

### `vendor_website`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 126 | 54.0% | 54.0% | +34.4 | n/a | no target |
| P01T | 370 | 98.1% | 98.1% | +1.7 | n/a | no target |
| P01_GOLD | 625 | 79.5% | 79.5% | -9.8 | 90% | ❌ 10 pts to go |
| P02 | 471 | 84.3% | 84.3% | -4.9 | 90% | 🟡 6 pts to go |
| P03 | 257 | 87.2% | 87.2% | -3.8 | 90% | 🟡 3 pts to go |
| P04 | 3839 | 85.3% | 85.3% | -4.9 | 85% | ✅ met |
| P05 | 424 | 44.1% | 44.1% | -8.1 | 70% | ❌ 26 pts to go |
| P06M | 13001 | 42.9% | 42.9% | +36.7 | n/a | no target |
| P06T | 67038 | 99.9% | 99.9% | +7.9 | n/a | no target |
| P06 | 297 | 98.3% | 98.3% | +0.0 | 50% | ✅ met |
| P07 | 800 | 99.1% | 99.1% | +0.0 | 100% | 🟡 1 pts to go |
| P08 | 25630 | 99.5% | 99.5% | +0.1 | 100% | 🟡 0 pts to go |
| P09 | 295 | 80.3% | 80.3% | +0.1 | 100% | ❌ 20 pts to go |
| P10R | 98583 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P10 | 2685 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P11 | 14979 | 99.8% | 99.8% | +0.1 | 100% | 🟡 0 pts to go |
| P12 | 7 | 28.6% | 28.6% | -8.9 | n/a | no target |
| P13 | 18028 | 100.0% | 100.0% | +0.0 | n/a | no target |

### `vendor_emails`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 126 | 15.1% | 15.1% | +0.7 | n/a | no target |
| P01T | 370 | 48.1% | 48.1% | -1.0 | n/a | no target |
| P01_GOLD | 625 | 43.0% | 43.0% | -2.2 | 70% | ❌ 27 pts to go |
| P02 | 471 | 48.8% | 48.8% | -0.7 | 75% | ❌ 26 pts to go |
| P03 | 257 | 44.0% | 44.0% | -0.5 | 75% | ❌ 31 pts to go |
| P04 | 3839 | 38.5% | 38.5% | +1.1 | 70% | ❌ 32 pts to go |
| P05 | 424 | 20.5% | 20.5% | -5.0 | 55% | ❌ 34 pts to go |
| P06M | 13001 | 4.6% | 4.6% | +1.3 | n/a | no target |
| P06T | 67038 | 40.1% | 40.1% | +0.5 | n/a | no target |
| P06 | 297 | 46.5% | 46.5% | +3.7 | n/a | no target |
| P07 | 800 | 48.1% | 48.1% | +2.2 | 70% | ❌ 22 pts to go |
| P08 | 25630 | 51.6% | 51.6% | +1.7 | 75% | ❌ 23 pts to go |
| P09 | 295 | 49.8% | 49.8% | +0.0 | 85% | ❌ 35 pts to go |
| P10R | 98583 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P10 | 2685 | 43.9% | 43.9% | +0.4 | 80% | ❌ 36 pts to go |
| P11 | 14979 | 3.5% | 3.5% | -1.5 | 70% | ❌ 66 pts to go |
| P12 | 7 | 14.3% | 14.3% | -10.7 | n/a | no target |
| P13 | 18028 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `vendor_logo_url`

> ceiling: needs the vendor's website first; sites that block automated readers (robots.txt / 403) are never read

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 126 | 54.0% | 54.0% | +40.6 | n/a | no target |
| P01T | 370 | 86.2% | 86.2% | -3.6 | n/a | no target |
| P01_GOLD | 625 | 69.4% | 69.4% | -8.1 | 90% | ❌ 21 pts to go |
| P02 | 471 | 72.8% | 72.8% | -4.8 | 90% | ❌ 17 pts to go |
| P03 | 257 | 79.4% | 79.4% | -3.8 | 90% | ❌ 11 pts to go |
| P04 | 3839 | 70.9% | 70.9% | -4.7 | 85% | ❌ 14 pts to go |
| P05 | 424 | 41.3% | 41.3% | -7.4 | 75% | ❌ 34 pts to go |
| P06M | 13001 | 42.6% | 42.6% | +38.5 | n/a | no target |
| P06T | 67038 | 94.0% | 94.0% | +10.8 | n/a | no target |
| P06 | 297 | 83.2% | 83.2% | +3.9 | n/a | no target |
| P07 | 800 | 86.2% | 86.2% | +4.6 | 100% | ❌ 14 pts to go |
| P08 | 25630 | 83.0% | 83.0% | +4.1 | 100% | ❌ 17 pts to go |
| P09 | 295 | 62.0% | 62.0% | +0.6 | n/a | no target |
| P10R | 98583 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P10 | 2685 | 84.2% | 84.2% | +0.0 | 100% | ❌ 16 pts to go |
| P11 | 14979 | 93.0% | 93.0% | +4.6 | n/a | no target |
| P12 | 7 | 28.6% | 28.6% | -8.9 | n/a | no target |
| P13 | 18028 | 83.6% | 83.6% | +0.4 | n/a | no target |

### `vendor_neq`

> ceiling: only Québec-registered vendors have an NEQ; the share of QC vendors is reported next to the rate

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 126 | 46.8% | 46.8% | -6.8 | n/a | no target · QC vendors: 46 rows, 100.0% filled |
| P01T | 370 | 20.8% | 20.8% | +3.0 | n/a | no target · QC vendors: 20 rows, 100.0% filled |
| P01_GOLD | 625 | 43.7% | 43.7% | +0.1 | 95% | ❌ 51 pts to go · QC vendors: 53 rows, 98.1% filled |
| P02 | 471 | 54.4% | 54.4% | -0.7 | 95% | ❌ 41 pts to go · QC vendors: 110 rows, 100.0% filled |
| P03 | 257 | 45.9% | 45.9% | -0.6 | 95% | ❌ 49 pts to go · QC vendors: 18 rows, 100.0% filled |
| P04 | 3839 | 28.2% | 28.2% | -3.7 | 95% | ❌ 67 pts to go · QC vendors: 493 rows, 98.8% filled |
| P05 | 424 | 14.2% | 14.2% | -0.6 | n/a | no target · QC vendors: 34 rows, 94.1% filled |
| P06M | 13001 | 42.4% | 42.4% | -10.9 | n/a | no target · QC vendors: 4809 rows, 100.0% filled |
| P06T | 67038 | 19.4% | 19.4% | +1.9 | n/a | no target · QC vendors: 3490 rows, 100.0% filled |
| P06 | 297 | 8.1% | 8.1% | -0.2 | n/a | no target · QC vendors: 17 rows, 76.5% filled |
| P07 | 800 | 5.9% | 5.9% | -0.9 | n/a | no target · QC vendors: 39 rows, 79.5% filled |
| P08 | 25630 | 6.0% | 6.0% | -0.5 | n/a | no target · QC vendors: 1246 rows, 97.9% filled |
| P09 | 295 | 78.0% | 78.0% | -0.2 | 95% | ❌ 17 pts to go · QC vendors: 106 rows, 100.0% filled |
| P10R | 98583 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P10 | 2685 | 17.5% | 17.5% | -0.1 | n/a | no target · QC vendors: 310 rows, 94.8% filled |
| P11 | 14979 | 87.7% | 87.7% | +6.2 | n/a | no target · QC vendors: 114 rows, 98.2% filled |
| P12 | 7 | 71.4% | 71.4% | +8.9 | n/a | no target · QC vendors: 1 rows, 100.0% filled |
| P13 | 18028 | 16.3% | 16.3% | +16.3 | n/a | no target · QC vendors: 2945 rows, 100.0% filled |

### `vendor_years_in_business`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 126 | 55.6% | 55.6% | -9.3 | n/a | no target · vendors with a registry record: 70 rows, 100.0% filled |
| P01T | 370 | 40.0% | 40.0% | +1.7 | n/a | no target · vendors with a registry record: 148 rows, 100.0% filled |
| P01_GOLD | 625 | 79.5% | 79.5% | +0.1 | 100% | ❌ 20 pts to go · vendors with a registry record: 497 rows, 100.0% filled |
| P02 | 471 | 76.6% | 76.6% | -0.8 | 100% | ❌ 23 pts to go · vendors with a registry record: 361 rows, 100.0% filled |
| P03 | 257 | 80.9% | 80.9% | -0.3 | 100% | ❌ 19 pts to go · vendors with a registry record: 208 rows, 100.0% filled |
| P04 | 3839 | 43.9% | 43.9% | -2.2 | 100% | ❌ 56 pts to go · vendors with a registry record: 1685 rows, 100.0% filled |
| P05 | 424 | 58.0% | 58.0% | -0.3 | n/a | no target · vendors with a registry record: 246 rows, 100.0% filled |
| P06M | 13001 | 43.2% | 43.2% | -11.1 | n/a | no target · vendors with a registry record: 5620 rows, 100.0% filled |
| P06T | 67038 | 31.4% | 31.4% | +1.0 | n/a | no target · vendors with a registry record: 21072 rows, 100.0% filled |
| P06 | 297 | 25.9% | 25.9% | +0.4 | n/a | no target · vendors with a registry record: 77 rows, 100.0% filled |
| P07 | 800 | 18.6% | 18.6% | +0.2 | n/a | no target · vendors with a registry record: 149 rows, 100.0% filled |
| P08 | 25630 | 13.8% | 13.8% | -0.5 | n/a | no target · vendors with a registry record: 3539 rows, 100.0% filled |
| P09 | 295 | 90.8% | 90.8% | -0.3 | n/a | no target · vendors with a registry record: 268 rows, 100.0% filled |
| P10R | 98583 | 100.0% | 100.0% | +0.0 | n/a | no target · vendors with a registry record: 98583 rows, 100.0% filled |
| P10 | 2685 | 33.1% | 33.1% | -0.1 | n/a | no target · vendors with a registry record: 889 rows, 100.0% filled |
| P11 | 14979 | 94.6% | 94.6% | +2.3 | n/a | no target · vendors with a registry record: 14176 rows, 100.0% filled |
| P12 | 7 | 100.0% | 100.0% | +0.0 | n/a | no target · vendors with a registry record: 7 rows, 100.0% filled |
| P13 | 18028 | 16.3% | 16.3% | +16.3 | n/a | no target · vendors with a registry record: 2945 rows, 100.0% filled |

## 3. buyer

### `buyer_legal_name_as_published`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 126 | 93.7% | 93.7% | +5.0 | 90% | ✅ met |
| P01T | 370 | 71.9% | 71.9% | +15.6 | 90% | ❌ 18 pts to go |
| P01_GOLD | 625 | 85.8% | 85.8% | +2.1 | 95% | 🟡 9 pts to go |
| P02 | 471 | 86.6% | 86.6% | +1.4 | 95% | 🟡 8 pts to go |
| P03 | 257 | 83.7% | 83.7% | +4.8 | 85% | 🟡 1 pts to go |
| P04 | 3839 | 58.7% | 58.7% | +2.3 | 90% | ❌ 31 pts to go |
| P05 | 424 | 78.1% | 78.1% | +10.4 | 75% | ✅ met |
| P06M | 13001 | 89.5% | 89.6% | +2.4 | n/a | no target |
| P06T | 67038 | 45.6% | 45.6% | +16.6 | n/a | no target |
| P06 | 297 | 67.3% | 67.3% | +10.4 | 80% | ❌ 13 pts to go |
| P07 | 800 | 51.9% | 52.0% | +5.7 | 80% | ❌ 28 pts to go |
| P08 | 25630 | 46.2% | 46.2% | +7.7 | 75% | ❌ 29 pts to go |
| P09 | 295 | 76.9% | 76.9% | -0.3 | 95% | ❌ 18 pts to go |
| P10R | 98583 | 37.1% | 37.1% | +12.1 | n/a | no target |
| P10 | 2685 | 49.8% | 49.8% | +10.8 | 70% | ❌ 20 pts to go |
| P11 | 14979 | 36.3% | 36.3% | +26.7 | 65% | ❌ 29 pts to go |
| P12 | 7 | 71.4% | 71.4% | -3.6 | 80% | 🟡 9 pts to go |
| P13 | 18028 | 46.7% | 46.7% | +7.5 | 60% | ❌ 13 pts to go |

### `buyer_bn_as_published`

> ceiling: a buyer's BN is public only where the buyer prints it or a public dataset carries it (CRA charities, federal grants & contributions recipients, business registries for corporations); municipalities rarely publish theirs

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 126 | 19.0% | 19.0% | -0.6 | 50% | ❌ 31 pts to go |
| P01T | 370 | 15.7% | 15.7% | +2.4 | n/a | no target |
| P01_GOLD | 625 | 19.8% | 19.8% | -0.8 | 40% | ❌ 20 pts to go |
| P02 | 471 | 19.3% | 19.3% | +0.4 | 40% | ❌ 21 pts to go |
| P03 | 257 | 23.0% | 23.0% | +0.7 | 40% | ❌ 17 pts to go |
| P04 | 3839 | 15.4% | 15.4% | -0.9 | 40% | ❌ 25 pts to go |
| P05 | 424 | 20.0% | 20.0% | +0.3 | 25% | 🟡 5 pts to go |
| P06M | 13001 | 10.5% | 10.5% | +1.7 | n/a | no target |
| P06T | 67038 | 9.7% | 9.7% | +2.2 | n/a | no target |
| P06 | 297 | 15.8% | 15.8% | +3.0 | 35% | ❌ 19 pts to go |
| P07 | 800 | 14.1% | 14.1% | +2.6 | 35% | ❌ 21 pts to go |
| P08 | 25630 | 13.8% | 13.8% | +3.4 | 35% | ❌ 21 pts to go |
| P09 | 295 | 16.3% | 16.3% | +0.1 | n/a | no target |
| P10R | 98583 | 8.9% | 8.9% | +1.8 | n/a | no target |
| P10 | 2685 | 11.3% | 11.3% | +4.8 | 30% | ❌ 19 pts to go |
| P11 | 14979 | 1.7% | 1.7% | +0.5 | n/a | no target |
| P12 | 7 | 14.3% | 14.3% | +1.8 | n/a | no target |
| P13 | 18028 | 20.8% | 20.8% | -0.2 | 30% | 🟡 9 pts to go |

### `buyer_address`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 126 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P01T | 370 | 90.5% | 90.5% | -1.4 | 100% | 🟡 10 pts to go |
| P01_GOLD | 625 | 90.1% | 90.1% | +0.6 | 100% | 🟡 10 pts to go |
| P02 | 471 | 95.5% | 95.5% | +0.2 | 100% | 🟡 4 pts to go |
| P03 | 257 | 89.5% | 89.5% | +0.0 | 100% | ❌ 10 pts to go |
| P04 | 3839 | 75.4% | 75.4% | -0.5 | 100% | ❌ 25 pts to go |
| P05 | 424 | 88.2% | 88.2% | +0.8 | 100% | ❌ 12 pts to go |
| P06M | 13001 | 99.2% | 99.2% | +0.4 | n/a | no target |
| P06T | 67038 | 78.0% | 78.0% | +0.6 | n/a | no target |
| P06 | 297 | 81.5% | 81.5% | +0.5 | 95% | ❌ 14 pts to go |
| P07 | 800 | 82.9% | 82.9% | -0.7 | 95% | ❌ 12 pts to go |
| P08 | 25630 | 79.6% | 79.6% | -0.6 | 95% | ❌ 15 pts to go |
| P09 | 295 | 95.9% | 95.9% | +0.2 | 100% | 🟡 4 pts to go |
| P10R | 98583 | 60.5% | 60.6% | +1.7 | n/a | no target |
| P10 | 2685 | 65.3% | 65.3% | +0.2 | 95% | ❌ 30 pts to go |
| P11 | 14979 | 92.2% | 92.2% | +5.0 | 80% | ✅ met |
| P12 | 7 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P13 | 18028 | 76.8% | 76.8% | +1.6 | 95% | ❌ 18 pts to go |

### `buyer_phone`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 126 | 70.6% | 70.6% | -15.0 | n/a | no target |
| P01T | 370 | 75.4% | 75.4% | +11.8 | n/a | no target |
| P01_GOLD | 625 | 70.4% | 70.4% | +0.9 | 90% | ❌ 20 pts to go |
| P02 | 471 | 76.4% | 76.4% | +0.7 | 95% | ❌ 19 pts to go |
| P03 | 257 | 73.9% | 73.9% | +0.1 | 95% | ❌ 21 pts to go |
| P04 | 3839 | 67.3% | 67.3% | +0.7 | 95% | ❌ 28 pts to go |
| P05 | 424 | 71.5% | 71.5% | +1.0 | 90% | ❌ 18 pts to go |
| P06M | 13001 | 69.6% | 69.6% | -16.8 | n/a | no target |
| P06T | 67038 | 66.9% | 66.9% | +19.0 | n/a | no target |
| P06 | 297 | 67.0% | 67.0% | +3.9 | 95% | ❌ 28 pts to go |
| P07 | 800 | 58.9% | 58.9% | +3.9 | 90% | ❌ 31 pts to go |
| P08 | 25630 | 62.8% | 62.8% | +4.0 | 95% | ❌ 32 pts to go |
| P09 | 295 | 85.8% | 85.8% | -0.3 | 100% | ❌ 14 pts to go |
| P10R | 98583 | 56.9% | 56.9% | +11.8 | n/a | no target |
| P10 | 2685 | 58.3% | 58.3% | +1.8 | 95% | ❌ 37 pts to go |
| P11 | 14979 | 28.3% | 28.3% | +17.1 | 75% | ❌ 47 pts to go |
| P12 | 7 | 71.4% | 71.4% | -3.6 | n/a | no target |
| P13 | 18028 | 58.0% | 58.0% | +10.4 | 95% | ❌ 37 pts to go |

### `buyer_logo_url`

> ceiling: sites that block automated readers (robots.txt / 403) are never read; an og:image that looks like a photo is labelled

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 126 | 62.7% | 62.7% | -8.4 | n/a | no target |
| P01T | 370 | 88.6% | 88.6% | +14.5 | 95% | 🟡 6 pts to go |
| P01_GOLD | 625 | 81.1% | 81.1% | +0.4 | 90% | 🟡 9 pts to go |
| P02 | 471 | 84.9% | 84.9% | -0.9 | 95% | ❌ 10 pts to go |
| P03 | 257 | 84.0% | 84.0% | +0.0 | 95% | ❌ 11 pts to go |
| P04 | 3839 | 76.0% | 76.0% | -7.3 | 90% | ❌ 14 pts to go |
| P05 | 424 | 89.4% | 89.4% | +0.9 | 95% | 🟡 6 pts to go |
| P06M | 13001 | 64.0% | 64.0% | -2.7 | n/a | no target |
| P06T | 67038 | 87.1% | 87.1% | +25.6 | n/a | no target |
| P06 | 297 | 81.5% | 81.5% | -0.6 | 100% | ❌ 18 pts to go |
| P07 | 800 | 74.6% | 74.6% | -2.6 | 100% | ❌ 25 pts to go |
| P08 | 25630 | 74.2% | 74.2% | -2.9 | 100% | ❌ 26 pts to go |
| P09 | 295 | 68.8% | 68.8% | +0.2 | n/a | no target |
| P10R | 98583 | 78.3% | 78.3% | +18.3 | n/a | no target |
| P10 | 2685 | 87.4% | 87.4% | +0.6 | 100% | ❌ 13 pts to go |
| P11 | 14979 | 55.5% | 55.5% | +36.7 | 80% | ❌ 24 pts to go |
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
| P02 | 471 | 24.2% | 24.2% | -0.3 | 40% | ❌ 16 pts to go |
| P03 | 257 | 8.9% | 8.9% | -0.1 | 20% | ❌ 11 pts to go |
| P04 | 3839 | 3.2% | 3.2% | -0.4 | 20% | ❌ 17 pts to go |
| P05 | 424 | 3.1% | 3.1% | -0.2 | 15% | ❌ 12 pts to go |
| P06M | 13001 | 0.2% | 0.2% | -0.1 | n/a | no target |
| P06T | 67038 | 0.4% | 0.4% | +0.0 | n/a | no target |
| P06 | 297 | 5.4% | 5.4% | -0.8 | n/a | no target |
| P07 | 800 | 7.4% | 7.4% | +0.1 | n/a | no target |
| P08 | 25630 | 0.2% | 0.2% | -0.1 | n/a | no target |
| P09 | 295 | 7.8% | 7.8% | +0.2 | n/a | no target |
| P10R | 98583 | 0.2% | 0.2% | +0.0 | n/a | no target |
| P10 | 2685 | 0.9% | 0.9% | -0.1 | n/a | no target |
| P11 | 14979 | 0.1% | 0.1% | -0.1 | n/a | no target |
| P12 | 7 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P13 | 18028 | 0.4% | 0.4% | +0.0 | n/a | no target |

### `ap_phone`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 126 | 19.0% | 19.0% | -7.8 | n/a | no target |
| P01T | 370 | 23.8% | 23.8% | -0.3 | 70% | ❌ 46 pts to go |
| P01_GOLD | 625 | 43.4% | 43.4% | +0.1 | 80% | ❌ 37 pts to go |
| P02 | 471 | 56.1% | 56.1% | -0.7 | 90% | ❌ 34 pts to go |
| P03 | 257 | 19.1% | 19.1% | +0.0 | 60% | ❌ 41 pts to go |
| P04 | 3839 | 21.0% | 21.0% | -2.7 | 85% | ❌ 64 pts to go |
| P05 | 424 | 11.8% | 11.8% | -0.1 | 50% | ❌ 38 pts to go |
| P06M | 13001 | 0.3% | 0.3% | -0.1 | n/a | no target |
| P06T | 67038 | 0.6% | 0.6% | +0.0 | n/a | no target |
| P06 | 297 | 14.8% | 14.8% | -1.4 | n/a | no target |
| P07 | 800 | 11.8% | 11.8% | -1.2 | n/a | no target |
| P08 | 25630 | 0.4% | 0.4% | -0.1 | n/a | no target |
| P09 | 295 | 77.3% | 77.3% | -0.3 | 95% | ❌ 18 pts to go |
| P10R | 98583 | 0.2% | 0.2% | +0.0 | n/a | no target |
| P10 | 2685 | 1.7% | 1.7% | +0.0 | n/a | no target |
| P11 | 14979 | 2.3% | 2.3% | -1.3 | n/a | no target |
| P12 | 7 | 28.6% | 28.6% | +3.6 | n/a | no target |
| P13 | 18028 | 0.7% | 0.7% | +0.0 | n/a | no target |

### `invoice_mailing_address`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 126 | 5.6% | 5.6% | -1.6 | n/a | no target |
| P01T | 370 | 12.2% | 12.2% | +0.2 | n/a | no target |
| P01_GOLD | 625 | 33.9% | 33.9% | +0.0 | 70% | ❌ 36 pts to go |
| P02 | 471 | 38.4% | 38.4% | -0.5 | 75% | ❌ 37 pts to go |
| P03 | 257 | 19.1% | 19.1% | +0.0 | 55% | ❌ 36 pts to go |
| P04 | 3839 | 20.9% | 20.9% | -2.7 | 75% | ❌ 54 pts to go |
| P05 | 424 | 10.8% | 10.8% | +0.0 | 50% | ❌ 39 pts to go |
| P06M | 13001 | 0.1% | 0.1% | -0.1 | n/a | no target |
| P06T | 67038 | 0.3% | 0.3% | -0.1 | n/a | no target |
| P06 | 297 | 7.4% | 7.4% | -0.9 | n/a | no target |
| P07 | 800 | 5.6% | 5.6% | -0.8 | n/a | no target |
| P08 | 25630 | 0.2% | 0.2% | +0.0 | n/a | no target |
| P09 | 295 | 74.9% | 74.9% | -0.3 | 95% | ❌ 20 pts to go |
| P10R | 98583 | 0.1% | 0.1% | -0.1 | n/a | no target |
| P10 | 2685 | 1.0% | 1.0% | +0.0 | n/a | no target |
| P11 | 14979 | 2.3% | 2.3% | -1.3 | n/a | no target |
| P12 | 7 | 14.3% | 14.3% | +1.8 | n/a | no target |
| P13 | 18028 | 0.4% | 0.4% | +0.0 | n/a | no target |

### `invoicing_requirements`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 126 | 6.3% | 6.3% | +0.1 | n/a | no target |
| P01T | 370 | 8.4% | 8.4% | -0.9 | n/a | no target |
| P01_GOLD | 625 | 57.9% | 58.1% | -0.1 | 80% | ❌ 22 pts to go |
| P02 | 471 | 45.2% | 45.4% | -0.6 | 75% | ❌ 30 pts to go |
| P03 | 257 | 37.7% | 37.7% | -0.2 | 70% | ❌ 32 pts to go |
| P04 | 3839 | 20.5% | 20.9% | -2.6 | 70% | ❌ 50 pts to go |
| P05 | 424 | 14.2% | 14.2% | -0.1 | 50% | ❌ 36 pts to go |
| P06M | 13001 | 0.3% | 0.3% | -0.1 | n/a | no target |
| P06T | 67038 | 0.3% | 0.3% | +0.0 | n/a | no target |
| P06 | 297 | 13.1% | 13.1% | -0.3 | n/a | no target |
| P07 | 800 | 1.9% | 1.9% | -0.1 | n/a | no target |
| P08 | 25630 | 0.3% | 0.3% | -0.1 | n/a | no target |
| P09 | 295 | 46.1% | 46.4% | +0.2 | 80% | ❌ 34 pts to go |
| P10R | 98583 | 0.1% | 0.1% | +0.0 | n/a | no target |
| P10 | 2685 | 1.2% | 1.2% | +0.0 | n/a | no target |
| P11 | 14979 | 0.7% | 0.7% | -0.4 | n/a | no target |
| P12 | 7 | 42.9% | 42.9% | +5.4 | n/a | no target |
| P13 | 18028 | 0.3% | 0.3% | +0.0 | n/a | no target |

### `payment_terms_as_published`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 126 | 11.9% | 11.9% | +0.6 | n/a | no target |
| P01T | 370 | 19.5% | 19.5% | -2.5 | 60% | ❌ 40 pts to go |
| P01_GOLD | 625 | 63.5% | 63.5% | -0.1 | 70% | 🟡 6 pts to go |
| P02 | 471 | 38.4% | 38.4% | -0.5 | 50% | ❌ 12 pts to go |
| P03 | 257 | 49.8% | 49.8% | -0.2 | 55% | 🟡 5 pts to go |
| P04 | 3839 | 11.8% | 11.8% | -1.5 | 40% | ❌ 28 pts to go |
| P05 | 424 | 17.2% | 17.2% | -0.1 | 40% | ❌ 23 pts to go |
| P06M | 13001 | 0.5% | 0.5% | -0.2 | n/a | no target |
| P06T | 67038 | 2.2% | 2.2% | -0.2 | n/a | no target |
| P06 | 297 | 19.2% | 19.2% | -0.5 | n/a | no target |
| P07 | 800 | 6.0% | 6.0% | -0.7 | n/a | no target |
| P08 | 25630 | 2.2% | 2.2% | -0.4 | n/a | no target |
| P09 | 295 | 5.8% | 5.8% | -0.1 | n/a | no target |
| P10R | 98583 | 0.2% | 0.2% | +0.0 | n/a | no target |
| P10 | 2685 | 4.4% | 4.4% | -0.1 | n/a | no target |
| P11 | 14979 | 3.3% | 3.3% | -1.0 | n/a | no target |
| P12 | 7 | 0.0% | 0.0% | -12.5 | n/a | no target |
| P13 | 18028 | 0.2% | 0.2% | +0.0 | n/a | no target |

### `po_required_as_published`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 126 | 15.1% | 15.1% | -1.4 | n/a | no target |
| P01T | 370 | 23.0% | 23.0% | -2.3 | 65% | ❌ 42 pts to go |
| P01_GOLD | 625 | 69.0% | 69.0% | +0.0 | 70% | 🟡 1 pts to go |
| P02 | 471 | 23.6% | 23.6% | -0.3 | 50% | ❌ 26 pts to go |
| P03 | 257 | 52.1% | 52.1% | -0.2 | 60% | 🟡 8 pts to go |
| P04 | 3839 | 5.0% | 5.0% | -0.8 | 40% | ❌ 35 pts to go |
| P05 | 424 | 19.8% | 19.8% | +0.1 | 45% | ❌ 25 pts to go |
| P06M | 13001 | 0.3% | 0.3% | +0.0 | n/a | no target |
| P06T | 67038 | 0.5% | 0.5% | -0.1 | n/a | no target |
| P06 | 297 | 29.3% | 29.3% | -2.4 | n/a | no target |
| P07 | 800 | 6.1% | 6.1% | -0.8 | n/a | no target |
| P08 | 25630 | 0.9% | 0.9% | -0.2 | n/a | no target |
| P09 | 295 | 9.8% | 9.8% | -0.1 | n/a | no target |
| P10R | 98583 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P10 | 2685 | 2.6% | 2.6% | +0.0 | n/a | no target |
| P11 | 14979 | 0.7% | 0.7% | -0.3 | n/a | no target |
| P12 | 7 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P13 | 18028 | 0.2% | 0.2% | +0.0 | n/a | no target |

### `invoice_portal_url`

> ceiling: only portals the buyer names on its own pages; informational tax-authority links are not portals

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 126 | 4.8% | 4.8% | -1.4 | n/a | no target |
| P01T | 370 | 13.5% | 13.5% | -1.0 | n/a | no target |
| P01_GOLD | 625 | 49.8% | 49.8% | +0.0 | 50% | 🟡 0 pts to go |
| P02 | 471 | 36.9% | 36.9% | -0.5 | n/a | no target |
| P03 | 257 | 52.5% | 52.5% | -0.6 | 60% | 🟡 8 pts to go |
| P04 | 3839 | 11.4% | 11.4% | -1.5 | n/a | no target |
| P05 | 424 | 14.9% | 14.9% | -0.3 | n/a | no target |
| P06M | 13001 | 0.2% | 0.2% | -0.1 | n/a | no target |
| P06T | 67038 | 0.4% | 0.4% | -0.1 | n/a | no target |
| P06 | 297 | 21.2% | 21.2% | -0.5 | n/a | no target |
| P07 | 800 | 6.6% | 6.6% | -0.6 | n/a | no target |
| P08 | 25630 | 0.5% | 0.5% | +0.0 | n/a | no target |
| P09 | 295 | 18.3% | 18.3% | +0.1 | n/a | no target |
| P10R | 98583 | 0.1% | 0.1% | +0.0 | n/a | no target |
| P10 | 2685 | 2.3% | 2.3% | +0.0 | n/a | no target |
| P11 | 14979 | 0.5% | 0.5% | -0.3 | n/a | no target |
| P12 | 7 | 14.3% | 14.3% | +14.3 | n/a | no target |
| P13 | 18028 | 0.4% | 0.4% | +0.0 | n/a | no target |

### `buyer_payment_method_preference`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 126 | 10.3% | 10.3% | -1.0 | 15% | 🟡 5 pts to go |
| P01T | 370 | 11.1% | 11.1% | +0.0 | 15% | 🟡 4 pts to go |
| P01_GOLD | 625 | 35.4% | 35.4% | +0.1 | 40% | 🟡 5 pts to go |
| P02 | 471 | 12.5% | 12.7% | +0.0 | 25% | ❌ 12 pts to go |
| P03 | 257 | 17.9% | 17.9% | -0.1 | 25% | 🟡 7 pts to go |
| P04 | 3839 | 2.7% | 2.7% | -0.1 | 15% | ❌ 12 pts to go |
| P05 | 424 | 6.8% | 6.8% | +0.0 | 15% | 🟡 8 pts to go |
| P06M | 13001 | 0.6% | 0.6% | +0.0 | 15% | ❌ 14 pts to go |
| P06T | 67038 | 0.7% | 0.7% | +0.3 | 15% | ❌ 14 pts to go |
| P06 | 297 | 9.1% | 9.1% | -0.2 | 15% | 🟡 6 pts to go |
| P07 | 800 | 3.5% | 3.5% | +0.3 | 15% | ❌ 12 pts to go |
| P08 | 25630 | 0.5% | 0.5% | +0.1 | 15% | ❌ 14 pts to go |
| P09 | 295 | 1.0% | 1.0% | +0.0 | 15% | ❌ 14 pts to go |
| P10R | 98583 | 0.6% | 0.6% | +0.2 | 15% | ❌ 14 pts to go |
| P10 | 2685 | 1.3% | 1.3% | +0.3 | 15% | ❌ 14 pts to go |
| P11 | 14979 | 0.4% | 0.4% | +0.2 | 15% | ❌ 15 pts to go |
| P12 | 7 | 14.3% | 14.3% | +1.8 | 15% | 🟡 1 pts to go |
| P13 | 18028 | 0.5% | 0.5% | +0.1 | 15% | ❌ 14 pts to go |

### `buyer_tax_exempt_status`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 126 | 4.0% | 4.0% | -2.2 | 15% | ❌ 11 pts to go |
| P01T | 370 | 10.5% | 10.5% | -1.5 | 25% | ❌ 14 pts to go |
| P01_GOLD | 625 | 29.1% | 29.1% | -0.1 | 25% | ✅ met |
| P02 | 471 | 25.1% | 25.1% | -0.3 | 15% | ✅ met |
| P03 | 257 | 21.4% | 21.4% | -0.1 | 15% | ✅ met |
| P04 | 3839 | 3.6% | 3.6% | -0.5 | 15% | ❌ 11 pts to go |
| P05 | 424 | 10.8% | 10.8% | +0.0 | 15% | 🟡 4 pts to go |
| P06M | 13001 | 0.2% | 0.2% | +0.0 | 15% | ❌ 15 pts to go |
| P06T | 67038 | 0.3% | 0.3% | +0.0 | 15% | ❌ 15 pts to go |
| P06 | 297 | 7.7% | 7.7% | +0.1 | 15% | 🟡 7 pts to go |
| P07 | 800 | 2.8% | 2.8% | -0.3 | 15% | ❌ 12 pts to go |
| P08 | 25630 | 0.4% | 0.4% | +0.0 | 15% | ❌ 15 pts to go |
| P09 | 295 | 1.0% | 1.0% | +0.0 | 15% | ❌ 14 pts to go |
| P10R | 98583 | 0.0% | 0.0% | +0.0 | 15% | ❌ 15 pts to go |
| P10 | 2685 | 1.5% | 1.5% | -0.1 | 15% | ❌ 14 pts to go |
| P11 | 14979 | 0.4% | 0.4% | -0.1 | 15% | ❌ 15 pts to go |
| P12 | 7 | 28.6% | 28.6% | +3.6 | 15% | ✅ met |
| P13 | 18028 | 0.1% | 0.1% | +0.1 | 15% | ❌ 15 pts to go |

### `buyer_ap_cycle_published`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 126 | 0.0% | 0.0% | +0.0 | 20% | ❌ 20 pts to go |
| P01T | 370 | 3.8% | 3.8% | -0.1 | 20% | ❌ 16 pts to go |
| P01_GOLD | 625 | 4.5% | 4.5% | +0.2 | 20% | ❌ 16 pts to go |
| P02 | 471 | 1.3% | 1.3% | +0.0 | 20% | ❌ 19 pts to go |
| P03 | 257 | 1.6% | 1.6% | +0.0 | 20% | ❌ 18 pts to go |
| P04 | 3839 | 0.6% | 0.6% | +0.0 | 20% | ❌ 19 pts to go |
| P05 | 424 | 1.2% | 1.2% | +0.0 | 20% | ❌ 19 pts to go |
| P06M | 13001 | 0.0% | 0.0% | +0.0 | 20% | ❌ 20 pts to go |
| P06T | 67038 | 0.0% | 0.0% | +0.0 | 20% | ❌ 20 pts to go |
| P06 | 297 | 1.3% | 1.3% | -0.1 | 20% | ❌ 19 pts to go |
| P07 | 800 | 0.4% | 0.4% | +0.0 | 20% | ❌ 20 pts to go |
| P08 | 25630 | 0.0% | 0.0% | +0.0 | 20% | ❌ 20 pts to go |
| P09 | 295 | 0.0% | 0.0% | +0.0 | 20% | ❌ 20 pts to go |
| P10R | 98583 | 0.0% | 0.0% | +0.0 | 20% | ❌ 20 pts to go |
| P10 | 2685 | 0.3% | 0.3% | +0.0 | 20% | ❌ 20 pts to go |
| P11 | 14979 | 0.0% | 0.0% | +0.0 | 20% | ❌ 20 pts to go |
| P12 | 7 | 0.0% | 0.0% | +0.0 | 20% | ❌ 20 pts to go |
| P13 | 18028 | 0.0% | 0.0% | +0.0 | 20% | ❌ 20 pts to go |

### `buyer_esignature_preference`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 126 | 0.8% | 0.8% | -0.2 | 15% | ❌ 14 pts to go |
| P01T | 370 | 2.4% | 2.4% | +0.0 | 15% | ❌ 13 pts to go |
| P01_GOLD | 625 | 10.4% | 10.4% | -0.1 | 15% | 🟡 5 pts to go |
| P02 | 471 | 11.9% | 11.9% | -0.1 | 15% | 🟡 3 pts to go |
| P03 | 257 | 20.6% | 20.6% | -0.1 | 15% | ✅ met |
| P04 | 3839 | 2.1% | 2.1% | -0.3 | 15% | ❌ 13 pts to go |
| P05 | 424 | 2.8% | 2.8% | -0.2 | 15% | ❌ 12 pts to go |
| P06M | 13001 | 0.1% | 0.1% | -0.1 | 15% | ❌ 15 pts to go |
| P06T | 67038 | 0.2% | 0.2% | +0.0 | 15% | ❌ 15 pts to go |
| P06 | 297 | 5.1% | 5.1% | -0.1 | 15% | 🟡 10 pts to go |
| P07 | 800 | 1.6% | 1.6% | -0.1 | 15% | ❌ 13 pts to go |
| P08 | 25630 | 0.4% | 0.4% | +0.0 | 15% | ❌ 15 pts to go |
| P09 | 295 | 0.7% | 0.7% | +0.0 | 15% | ❌ 14 pts to go |
| P10R | 98583 | 0.0% | 0.0% | +0.0 | 15% | ❌ 15 pts to go |
| P10 | 2685 | 0.9% | 0.9% | +0.0 | 15% | ❌ 14 pts to go |
| P11 | 14979 | 0.2% | 0.2% | -0.1 | 15% | ❌ 15 pts to go |
| P12 | 7 | 0.0% | 0.0% | +0.0 | 15% | ❌ 15 pts to go |
| P13 | 18028 | 0.1% | 0.1% | +0.0 | 15% | ❌ 15 pts to go |

### `ap_system_hint`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 126 | 7.1% | 7.1% | -0.1 | 20% | ❌ 13 pts to go |
| P01T | 370 | 14.1% | 14.1% | -1.0 | 40% | ❌ 26 pts to go |
| P01_GOLD | 625 | 45.9% | 45.9% | +0.1 | 40% | ✅ met |
| P02 | 471 | 42.3% | 42.3% | -0.5 | 20% | ✅ met |
| P03 | 257 | 48.6% | 48.6% | -0.2 | 35% | ✅ met |
| P04 | 3839 | 13.6% | 13.6% | -1.8 | 20% | 🟡 6 pts to go |
| P05 | 424 | 14.9% | 14.9% | +0.1 | 20% | 🟡 5 pts to go |
| P06M | 13001 | 0.4% | 0.4% | -0.1 | 20% | ❌ 20 pts to go |
| P06T | 67038 | 0.7% | 0.7% | +0.0 | 20% | ❌ 19 pts to go |
| P06 | 297 | 21.9% | 21.9% | -0.2 | 20% | ✅ met |
| P07 | 800 | 6.9% | 6.9% | -0.2 | 20% | ❌ 13 pts to go |
| P08 | 25630 | 0.8% | 0.8% | -0.1 | 20% | ❌ 19 pts to go |
| P09 | 295 | 18.3% | 18.3% | +0.1 | 20% | 🟡 2 pts to go |
| P10R | 98583 | 0.2% | 0.2% | +0.0 | 20% | ❌ 20 pts to go |
| P10 | 2685 | 3.4% | 3.4% | +0.0 | 20% | ❌ 17 pts to go |
| P11 | 14979 | 0.7% | 0.7% | -0.3 | 20% | ❌ 19 pts to go |
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
| P02 | 471 | 62.2% | 62.2% | -0.8 | 95% | ❌ 33 pts to go |
| P03 | 257 | 54.5% | 54.5% | -0.2 | 90% | ❌ 36 pts to go |
| P04 | 3839 | 24.1% | 24.1% | -3.0 | 85% | ❌ 61 pts to go |
| P05 | 424 | 37.3% | 37.3% | +0.8 | 75% | ❌ 38 pts to go |
| P06M | 13001 | 35.6% | 35.6% | -14.5 | n/a | no target |
| P06T | 67038 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06 | 297 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P07 | 800 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P08 | 25630 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P09 | 295 | 89.5% | 89.5% | +0.1 | 100% | ❌ 10 pts to go |
| P10R | 98583 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P10 | 2685 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P11 | 14979 | 0.6% | 0.6% | -0.3 | 60% | ❌ 59 pts to go |
| P12 | 7 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P13 | 18028 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `currency`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 126 | 33.3% | 33.3% | -11.0 | n/a | no target |
| P01T | 370 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P01_GOLD | 625 | 72.8% | 72.8% | +0.0 | 100% | ❌ 27 pts to go |
| P02 | 471 | 65.6% | 65.6% | -0.9 | 100% | ❌ 34 pts to go |
| P03 | 257 | 60.3% | 60.3% | -0.2 | n/a | no target |
| P04 | 3839 | 24.7% | 24.7% | -3.1 | 95% | ❌ 70 pts to go |
| P05 | 424 | 33.3% | 33.3% | +0.3 | 80% | ❌ 47 pts to go |
| P06M | 13001 | 35.6% | 35.6% | -14.5 | n/a | no target |
| P06T | 67038 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06 | 297 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P07 | 800 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P08 | 25630 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P09 | 295 | 92.5% | 92.5% | -0.2 | 100% | 🟡 8 pts to go |
| P10R | 98583 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P10 | 2685 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P11 | 14979 | 0.6% | 0.6% | -0.4 | n/a | no target |
| P12 | 7 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P13 | 18028 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `start_date`

> ceiling: most award notices publish an award date, not a start date; start_date carries the signature date when the source gives one, labelled

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 126 | 81.0% | 81.0% | +2.6 | n/a | no target |
| P01T | 370 | 0.3% | 0.3% | +0.0 | n/a | no target |
| P01_GOLD | 625 | 51.7% | 51.7% | +0.1 | 85% | ❌ 33 pts to go |
| P02 | 471 | 56.9% | 56.9% | -0.7 | 90% | ❌ 33 pts to go |
| P03 | 257 | 44.0% | 44.0% | -0.1 | 85% | ❌ 41 pts to go |
| P04 | 3839 | 27.1% | 27.1% | -3.3 | 90% | ❌ 63 pts to go |
| P05 | 424 | 33.3% | 33.3% | +0.5 | 75% | ❌ 42 pts to go |
| P06M | 13001 | 89.7% | 89.7% | -0.7 | n/a | no target |
| P06T | 67038 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06 | 297 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P07 | 800 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P08 | 25630 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P09 | 295 | 85.1% | 85.1% | +0.0 | 95% | 🟡 10 pts to go |
| P10R | 98583 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P10 | 2685 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P11 | 14979 | 0.5% | 0.5% | -0.3 | n/a | no target |
| P12 | 7 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P13 | 18028 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `end_date`

> ceiling: an inferred end (award date + published duration) is labelled as such; sources without a duration leave end_date empty — the honest ceiling. P09 is BY DEFINITION the rows whose end date is not published (older SEAO contracts with no closing notice): its end_date / duration targets cannot be met without inventing a date

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 126 | 80.2% | 80.2% | +0.8 | n/a | no target |
| P01T | 370 | 0.3% | 0.3% | +0.0 | n/a | no target |
| P01_GOLD | 625 | 51.8% | 51.8% | +0.0 | 85% | ❌ 33 pts to go |
| P02 | 471 | 52.0% | 52.0% | -0.7 | 90% | ❌ 38 pts to go |
| P03 | 257 | 45.1% | 45.1% | -0.2 | 85% | ❌ 40 pts to go |
| P04 | 3839 | 23.1% | 23.1% | -2.9 | 90% | ❌ 67 pts to go |
| P05 | 424 | 43.6% | 43.6% | +0.7 | 75% | ❌ 31 pts to go |
| P06M | 13001 | 80.4% | 80.4% | -3.3 | n/a | no target |
| P06T | 67038 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06 | 297 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P07 | 800 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P08 | 25630 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P09 | 295 | 0.3% | 0.3% | +0.0 | 95% | ❌ 95 pts to go |
| P10R | 98583 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P10 | 2685 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P11 | 14979 | 0.4% | 0.4% | -0.3 | n/a | no target |
| P12 | 7 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P13 | 18028 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `contract_title`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 126 | 89.7% | 89.7% | +4.1 | n/a | no target |
| P01T | 370 | 91.4% | 91.4% | -0.8 | n/a | no target |
| P01_GOLD | 625 | 85.4% | 85.4% | -0.1 | 100% | ❌ 15 pts to go |
| P02 | 471 | 74.7% | 74.7% | -1.0 | 100% | ❌ 25 pts to go |
| P03 | 257 | 91.4% | 91.4% | -0.8 | n/a | no target |
| P04 | 3839 | 45.6% | 45.6% | -5.9 | 95% | ❌ 49 pts to go |
| P05 | 424 | 77.4% | 77.4% | -0.4 | 95% | ❌ 18 pts to go |
| P06M | 13001 | 98.8% | 98.8% | +0.5 | n/a | no target |
| P06T | 67038 | 82.3% | 82.3% | -1.4 | n/a | no target |
| P06 | 297 | 25.6% | 25.6% | -0.6 | n/a | no target |
| P07 | 800 | 17.1% | 17.1% | -2.0 | n/a | no target |
| P08 | 25630 | 9.8% | 9.8% | -1.2 | n/a | no target |
| P09 | 295 | 98.6% | 98.6% | -0.1 | 100% | 🟡 1 pts to go |
| P10R | 98583 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P10 | 2685 | 71.5% | 71.5% | -0.2 | n/a | no target |
| P11 | 14979 | 10.8% | 10.8% | -5.3 | n/a | no target |
| P12 | 7 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P13 | 18028 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `contract_description`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 126 | 89.7% | 89.7% | +4.1 | n/a | no target |
| P01T | 370 | 91.4% | 91.4% | -0.8 | n/a | no target |
| P01_GOLD | 625 | 88.6% | 88.6% | -0.1 | 100% | ❌ 11 pts to go |
| P02 | 471 | 75.8% | 76.0% | -1.0 | 100% | ❌ 24 pts to go |
| P03 | 257 | 92.2% | 92.2% | -0.8 | n/a | no target |
| P04 | 3839 | 48.8% | 48.8% | -6.3 | 95% | ❌ 46 pts to go |
| P05 | 424 | 89.9% | 89.9% | -0.3 | 70% | ✅ met |
| P06M | 13001 | 98.8% | 98.8% | +0.5 | n/a | no target |
| P06T | 67038 | 82.3% | 82.3% | -1.4 | n/a | no target |
| P06 | 297 | 25.6% | 25.6% | -0.6 | n/a | no target |
| P07 | 800 | 17.1% | 17.1% | -2.0 | n/a | no target |
| P08 | 25630 | 9.8% | 9.8% | -1.2 | n/a | no target |
| P09 | 295 | 98.6% | 98.6% | -0.1 | 100% | 🟡 1 pts to go |
| P10R | 98583 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P10 | 2685 | 71.5% | 71.5% | -0.2 | n/a | no target |
| P11 | 14979 | 10.8% | 10.8% | -5.3 | n/a | no target |
| P12 | 7 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P13 | 18028 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `number_of_bids`

> ceiling: published by some portals only (bids&tenders submission lists, Biddingo bidder lists); federal proactive disclosure does not publish bid counts

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 126 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P01T | 370 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P01_GOLD | 625 | 16.8% | 16.8% | +0.0 | 60% | ❌ 43 pts to go · rows from a source that publishes bids: 363 rows, 28.9% filled |
| P02 | 471 | 11.0% | 11.0% | -0.2 | n/a | no target · rows from a source that publishes bids: 290 rows, 17.9% filled |
| P03 | 257 | 13.2% | 13.2% | -0.1 | n/a | no target · rows from a source that publishes bids: 139 rows, 24.5% filled |
| P04 | 3839 | 1.4% | 1.4% | -0.2 | n/a | no target · rows from a source that publishes bids: 872 rows, 6.3% filled |
| P05 | 424 | 2.8% | 2.8% | -0.2 | n/a | no target · rows from a source that publishes bids: 51 rows, 23.5% filled |
| P06M | 13001 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06T | 67038 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06 | 297 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P07 | 800 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P08 | 25630 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P09 | 295 | 3.1% | 3.1% | +0.1 | n/a | no target · rows from a source that publishes bids: 282 rows, 3.2% filled |
| P10R | 98583 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P10 | 2685 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P11 | 14979 | 0.1% | 0.1% | +0.0 | n/a | no target · rows from a source that publishes bids: 88 rows, 13.6% filled |
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
| P02 | 471 | 51.8% | 87.7% | -0.7 | 90% | ❌ 38 pts to go |
| P03 | 257 | 45.5% | 80.2% | -0.2 | 90% | ❌ 44 pts to go |
| P04 | 3839 | 18.6% | 94.1% | -2.3 | 90% | ❌ 71 pts to go |
| P05 | 424 | 0.0% | 83.3% | +0.0 | 90% | ❌ 90 pts to go |
| P06M | 13001 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P06T | 67038 | 0.0% | 99.9% | +0.0 | n/a | no target |
| P06 | 297 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P07 | 800 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P08 | 25630 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P09 | 295 | 2.4% | 4.1% | +0.1 | 90% | ❌ 88 pts to go |
| P10R | 98583 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P10 | 2685 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P11 | 14979 | 0.4% | 99.7% | -0.2 | n/a | no target |
| P12 | 7 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P13 | 18028 | 0.0% | 100.0% | +0.0 | n/a | no target |

### `commodity_distribution_top3`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 126 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P01T | 370 | 0.5% | 98.6% | -0.1 | n/a | no target |
| P01_GOLD | 625 | 25.9% | 55.0% | +0.0 | 90% | ❌ 64 pts to go |
| P02 | 471 | 51.0% | 86.8% | -0.6 | n/a | no target |
| P03 | 257 | 24.9% | 59.5% | -0.1 | n/a | no target |
| P04 | 3839 | 20.3% | 95.9% | -2.6 | n/a | no target |
| P05 | 424 | 0.5% | 83.7% | +0.0 | n/a | no target |
| P06M | 13001 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P06T | 67038 | 0.1% | 99.9% | +0.0 | n/a | no target |
| P06 | 297 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P07 | 800 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P08 | 25630 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P09 | 295 | 41.4% | 43.1% | -0.5 | n/a | no target |
| P10R | 98583 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P10 | 2685 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P11 | 14979 | 0.4% | 99.7% | -0.2 | n/a | no target |
| P12 | 7 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P13 | 18028 | 0.0% | 100.0% | +0.0 | n/a | no target |

### `year_over_year_spend_trend`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 126 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P01T | 370 | 1.6% | 99.7% | +0.1 | n/a | no target |
| P01_GOLD | 625 | 51.8% | 81.0% | +0.0 | 95% | ❌ 43 pts to go |
| P02 | 471 | 55.8% | 91.7% | -0.8 | n/a | no target |
| P03 | 257 | 47.9% | 82.5% | -0.1 | n/a | no target |
| P04 | 3839 | 20.6% | 96.1% | -2.5 | n/a | no target |
| P05 | 424 | 4.5% | 87.7% | -0.2 | n/a | no target |
| P06M | 13001 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P06T | 67038 | 0.1% | 100.0% | +0.0 | n/a | no target |
| P06 | 297 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P07 | 800 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P08 | 25630 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P09 | 295 | 63.7% | 65.4% | -0.3 | n/a | no target |
| P10R | 98583 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P10 | 2685 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P11 | 14979 | 0.4% | 99.7% | -0.2 | n/a | no target |
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
| P02 | 471 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P03 | 257 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P04 | 3839 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P05 | 424 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P06M | 13001 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P06T | 67038 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P06 | 297 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P07 | 800 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P08 | 25630 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P09 | 295 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P10R | 98583 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P10 | 2685 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P11 | 14979 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P12 | 7 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P13 | 18028 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |

### `tls_rpt`

> ceiling: DNS-only check; 'no record' counts as checked

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 126 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P01T | 370 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P01_GOLD | 625 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P02 | 471 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P03 | 257 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P04 | 3839 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P05 | 424 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P06M | 13001 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P06T | 67038 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P06 | 297 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P07 | 800 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P08 | 25630 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P09 | 295 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P10R | 98583 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P10 | 2685 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P11 | 14979 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P12 | 7 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P13 | 18028 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |

### `bimi`

> ceiling: DNS-only check; 'no record' counts as checked

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 126 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P01T | 370 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P01_GOLD | 625 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P02 | 471 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P03 | 257 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P04 | 3839 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P05 | 424 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P06M | 13001 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P06T | 67038 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P06 | 297 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P07 | 800 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P08 | 25630 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P09 | 295 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P10R | 98583 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P10 | 2685 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P11 | 14979 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P12 | 7 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P13 | 18028 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |

