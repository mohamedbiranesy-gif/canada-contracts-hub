# Coverage vs the downstream team's targets — 2026-11-11

Benchmarks (field × package with a numeric target): **97 of 446 met** (21.7%); 67 within 10 points; 282 further away.
A cell counts as filled only when it carries a value: blank, `not_published`, `not_found_yet` and label-only cells ("no identifier published …", "no dataset record …", "0 in the contract dataset …") do not count; the DNS checks count when checked. `any` = share of non-blank cells incl. such labels. Δ = change since the previous build in `coord/results/coverage_history.csv`.
Rows per package: P01M 126, P01T 427, P01_GOLD 625, P02 471, P03 257, P04 3859, P05 421, P06M 13192, P06T 84475, P06 298, P07 803, P08 25629, P09 295, P10R 102647, P10 2648, P11 20964, P12 7, P13 17390

## Invoice-grade readiness (the row as an invoice header: bill-to, submit-to, references, terms, tax, vendor identity, follow-up)

| package | rows | all 11 elements | ≥ 9 of 11 | median elements | most-missing element |
|---|---|---|---|---|---|
| P01M | 126 | 0.0% | 19.8% | 8 | vendor GST/HST number (115 rows) |
| P01T | 427 | 0.5% | 21.5% | 7 | payment terms (350 rows) |
| P01_GOLD | 625 | 24.8% | 70.9% | 10 | payment terms (214 rows) |
| P02 | 471 | 7.2% | 54.4% | 9 | PO rule (359 rows) |
| P03 | 257 | 14.8% | 58.4% | 9 | payment terms (123 rows) |
| P04 | 3859 | 1.2% | 16.0% | 6 | PO rule (3654 rows) |
| P05 | 421 | 1.2% | 17.8% | 7 | payment terms (346 rows) |
| P06M | 13192 | 0.0% | 2.3% | 8 | PO rule (12992 rows) |
| P06T | 84475 | 0.0% | 7.2% | 7 | PO rule (83983 rows) |
| P06 | 298 | 0.0% | 9.1% | 7 | reference to quote (PO / contract / vendor id) (298 rows) |
| P07 | 803 | 0.0% | 2.1% | 6 | reference to quote (PO / contract / vendor id) (803 rows) |
| P08 | 25629 | 0.0% | 0.4% | 6 | reference to quote (PO / contract / vendor id) (25629 rows) |
| P09 | 295 | 1.0% | 45.1% | 8 | payment terms (276 rows) |
| P10R | 102647 | 0.0% | 22.7% | 8 | PO rule (102610 rows) |
| P10 | 2648 | 0.0% | 1.1% | 5 | reference to quote (PO / contract / vendor id) (2648 rows) |
| P11 | 20964 | 0.2% | 21.0% | 8 | PO rule (20762 rows) |
| P12 | 7 | 0.0% | 28.6% | 8 | PO rule (7 rows) |
| P13 | 17390 | 0.0% | 0.2% | 7 | reference to quote (PO / contract / vendor id) (17390 rows) |

## AP grade (how stringently the row's accounts-payable data meets what an invoice needs; A = invoicing mailbox referee-confirmed on the buyer's own domain with MX, legal name, address, PO rule and terms all published, no penalties)

| package | rows | A | B | C | D | E | median ap_score |
|---|---|---|---|---|---|---|---|
| P01M | 126 | 9 | 26 | 91 | 0 | 0 | 71 |
| P01T | 427 | 30 | 71 | 326 | 0 | 0 | 68 |
| P01_GOLD | 625 | 229 | 197 | 199 | 0 | 0 | 82 |
| P02 | 471 | 0 | 196 | 275 | 0 | 0 | 66 |
| P03 | 257 | 0 | 0 | 247 | 10 | 0 | 57 |
| P04 | 3859 | 0 | 0 | 3289 | 570 | 0 | 46 |
| P05 | 421 | 16 | 29 | 364 | 12 | 0 | 51 |
| P06M | 13192 | 0 | 9 | 13121 | 62 | 0 | 46 |
| P06T | 84475 | 0 | 45 | 68073 | 16357 | 0 | 38 |
| P06 | 298 | 21 | 57 | 220 | 0 | 0 | 71 |
| P07 | 803 | 0 | 33 | 750 | 20 | 0 | 54 |
| P08 | 25629 | 0 | 0 | 22254 | 3375 | 0 | 43 |
| P09 | 295 | 3 | 12 | 278 | 2 | 0 | 53 |
| P10R | 102647 | 2 | 14 | 73055 | 29576 | 0 | 38 |
| P10 | 2648 | 2 | 14 | 2028 | 604 | 0 | 43 |
| P11 | 20964 | 7 | 15 | 38 | 0 | 20904 | 23 |
| P12 | 7 | 0 | 0 | 7 | 0 | 0 | 54 |
| P13 | 17390 | 0 | 16 | 14389 | 2985 | 0 | 43 |

### AP payability (confirmed channel + bill-to legal name and address + the buyer's reference rule + tax treatment known)

| package | rows | payable today | % | most common gap |
|---|---|---|---|---|
| P01M | 126 | 107 | 84.9% | the buyer's PO / reference rule (9) |
| P01T | 427 | 236 | 55.3% | bill-to legal name and address (155) |
| P01_GOLD | 625 | 472 | 75.5% | bill-to legal name and address (97) |
| P02 | 471 | 314 | 66.7% | the buyer's PO / reference rule (92) |
| P03 | 257 | 0 | 0.0% | a confirmed invoicing / AP or finance channel (257) |
| P04 | 3859 | 0 | 0.0% | a confirmed invoicing / AP or finance channel (3859) |
| P05 | 421 | 47 | 11.2% | a confirmed invoicing / AP or finance channel (335) |
| P06M | 13192 | 131 | 1.0% | a confirmed invoicing / AP or finance channel (13016) |
| P06T | 84475 | 526 | 0.6% | a confirmed invoicing / AP or finance channel (83279) |
| P06 | 298 | 52 | 17.4% | the buyer's PO / reference rule (133) |
| P07 | 803 | 13 | 1.6% | the buyer's PO / reference rule (311) |
| P08 | 25629 | 0 | 0.0% | a confirmed invoicing / AP or finance channel (25629) |
| P09 | 295 | 41 | 13.9% | a confirmed invoicing / AP or finance channel (245) |
| P10R | 102647 | 575 | 0.6% | a confirmed invoicing / AP or finance channel (101458) |
| P10 | 2648 | 5 | 0.2% | a confirmed invoicing / AP or finance channel (2555) |
| P11 | 20964 | 14 | 0.1% | a confirmed invoicing / AP or finance channel (20904) |
| P12 | 7 | 3 | 42.9% | a confirmed invoicing / AP or finance channel (4) |
| P13 | 17390 | 7 | 0.0% | a confirmed invoicing / AP or finance channel (17050) |

### Pay on sight (an invoice generated from the row would clear AP: confirmed invoicing / AP or finance channel, bill-to legal name + address, vendor legal name + GST/HST number + remit-to address, tax treatment and currency known — published or labelled-derived; the buyer's reference rule is reported separately)

| package | rows | pay on sight | % | + reference rule not published | routed (general inbox only) | most common gap |
|---|---|---|---|---|---|---|
| P01M | 126 | 5 | 4.0% | 5 | 0 | the vendor's GST/HST number (BN9) (115) |
| P01T | 427 | 83 | 19.4% | 14 | 0 | the vendor's GST/HST number (BN9) (246) |
| P01_GOLD | 625 | 396 | 63.4% | 12 | 0 | the vendor's GST/HST number (BN9) (156) |
| P02 | 471 | 211 | 44.8% | 23 | 0 | the vendor's GST/HST number (BN9) (207) |
| P03 | 257 | 16 | 6.2% | 0 | 132 | an invoicing / AP or finance mailbox (only a purchasing / general inbo (88) |
| P04 | 3859 | 42 | 1.1% | 7 | 813 | an invoicing / AP or finance mailbox (only a purchasing / general inbo (2940) |
| P05 | 421 | 20 | 4.8% | 7 | 110 | an invoicing / AP or finance mailbox (only a purchasing / general inbo (217) |
| P06M | 13192 | 1 | 0.0% | 10 | 149 | an invoicing / AP or finance mailbox (only a purchasing / general inbo (12822) |
| P06T | 84475 | 186 | 0.2% | 48 | 15980 | an invoicing / AP or finance mailbox (only a purchasing / general inbo (67112) |
| P06 | 298 | 16 | 5.4% | 35 | 0 | the vendor's GST/HST number (BN9) (175) |
| P07 | 803 | 6 | 0.7% | 75 | 30 | the vendor's GST/HST number (BN9) (436) |
| P08 | 25629 | 1 | 0.0% | 9 | 2996 | an invoicing / AP or finance mailbox (only a purchasing / general inbo (22554) |
| P09 | 295 | 38 | 12.9% | 1 | 120 | an invoicing / AP or finance mailbox (only a purchasing / general inbo (116) |
| P10R | 102647 | 906 | 0.9% | 0 | 55954 | an invoicing / AP or finance mailbox (only a purchasing / general inbo (45444) |
| P10 | 2648 | 4 | 0.2% | 21 | 382 | an invoicing / AP or finance mailbox (only a purchasing / general inbo (2142) |
| P11 | 20964 | 65 | 0.3% | 0 | 0 | a confirmed invoicing / AP or finance channel (20829) |
| P12 | 7 | 1 | 14.3% | 0 | 2 | the vendor's GST/HST number (BN9) (2) |
| P13 | 17390 | 9 | 0.1% | 250 | 10374 | an invoicing / AP or finance mailbox (only a purchasing / general inbo (6637) |
| **all** | 274534 | 2006 | 0.7% | 517 | 87042 | |

### What still blocks grade A (rows per missing element; a row counts under every element it lacks)

| package | rows not A | referee confirmation of the mailbox | an invoicing / AP mailbox (not finance / procurement / general) | a mailbox on the buyer's own domain | MX record for the mailbox domain | published bill-to legal name | invoice / billing address | published PO rule | published payment terms | clear the penalty |
|---|---|---|---|---|---|---|---|---|---|---|
| P01M | 117 | 0 | 0 | 0 | 62 | 7 | 0 | 97 | 102 | 1 |
| P01T | 397 | 0 | 0 | 0 | 201 | 139 | 44 | 331 | 352 | 26 |
| P01_GOLD | 396 | 0 | 0 | 0 | 11 | 78 | 31 | 194 | 228 | 57 |
| P02 | 471 | 0 | 471 | 0 | 47 | 53 | 18 | 359 | 287 | 22 |
| P03 | 257 | 0 | 257 | 0 | 15 | 40 | 23 | 122 | 129 | 25 |
| P04 | 3859 | 0 | 3859 | 0 | 1835 | 1379 | 927 | 3654 | 3379 | 131 |
| P05 | 405 | 0 | 355 | 0 | 75 | 85 | 43 | 337 | 348 | 50 |
| P06M | 13192 | 0 | 13192 | 0 | 8365 | 1079 | 113 | 12992 | 12873 | 77 |
| P06T | 84475 | 0 | 84475 | 0 | 68454 | 49535 | 20769 | 83983 | 82256 | 433 |
| P06 | 277 | 0 | 0 | 0 | 121 | 74 | 51 | 201 | 235 | 4 |
| P07 | 803 | 0 | 803 | 0 | 478 | 318 | 127 | 745 | 748 | 13 |
| P08 | 25629 | 0 | 25629 | 0 | 18897 | 11745 | 5056 | 25314 | 24882 | 225 |
| P09 | 292 | 0 | 271 | 0 | 9 | 67 | 2 | 266 | 278 | 44 |
| P10R | 102645 | 0 | 102471 | 0 | 80845 | 62761 | 39996 | 102610 | 102459 | 25 |
| P10 | 2646 | 0 | 2610 | 0 | 1291 | 1274 | 893 | 2576 | 2526 | 115 |
| P11 | 20957 | 20904 | 20839 | 0 | 19429 | 11864 | 1090 | 20762 | 19002 | 38 |
| P12 | 7 | 0 | 6 | 0 | 0 | 2 | 0 | 7 | 7 | 0 |
| P13 | 17390 | 0 | 17290 | 0 | 8752 | 8366 | 3935 | 17355 | 17349 | 19 |

## Where the work is (largest gaps in rows still needed)

| field | package | now | target | rows needed |
|---|---|---|---|---|
| buyer_ap_cycle_published | P10R | 0.0% | 20% | 20501 |
| ap_system_hint | P10R | 0.2% | 20% | 20326 |
| buyer_ap_cycle_published | P06T | 0.0% | 20% | 16869 |
| ap_system_hint | P06T | 0.7% | 20% | 16338 |
| buyer_tax_exempt_status | P10R | 0.0% | 15% | 15370 |
| buyer_esignature_preference | P10R | 0.0% | 15% | 15349 |
| vendor_phone | P11 | 4.0% | 75% | 14882 |
| buyer_payment_method_preference | P10R | 0.6% | 15% | 14733 |
| vendor_registered_address | P08 | 13.6% | 70% | 14451 |
| vendor_emails | P11 | 3.3% | 70% | 13986 |
| contract_value | P11 | 0.4% | 60% | 12494 |
| award_or_notice_id | P11 | 0.4% | 60% | 12493 |
| buyer_esignature_preference | P06T | 0.2% | 15% | 12493 |
| buyer_tax_exempt_status | P06T | 0.3% | 15% | 12423 |
| buyer_payment_method_preference | P06T | 0.6% | 15% | 12172 |
| commodity_codes | P11 | 0.3% | 50% | 10421 |
| buyer_phone | P11 | 25.9% | 75% | 10289 |
| vendor_bn9 | P08 | 15.7% | 50% | 8784 |
| solicitation_or_tender_number | P11 | 0.4% | 40% | 8307 |
| buyer_phone | P08 | 68.9% | 95% | 6699 |
| invoice_reference_hint | P08 | 1.2% | 25% | 6093 |
| buyer_phone | P13 | 63.2% | 95% | 5525 |
| buyer_bn_as_published | P08 | 13.6% | 35% | 5481 |
| vendor_emails | P08 | 54.1% | 75% | 5347 |
| buyer_legal_name_as_published | P08 | 54.2% | 75% | 5338 |
| buyer_ap_cycle_published | P08 | 0.0% | 20% | 5114 |
| vendor_phone | P08 | 66.0% | 85% | 4865 |
| ap_system_hint | P08 | 1.1% | 20% | 4849 |
| buyer_legal_name_as_published | P11 | 43.4% | 65% | 4527 |
| buyer_ap_cycle_published | P11 | 0.0% | 20% | 4185 |
| ap_system_hint | P11 | 0.8% | 20% | 4027 |
| buyer_address | P08 | 80.3% | 95% | 3780 |
| buyer_esignature_preference | P08 | 0.5% | 15% | 3729 |
| buyer_tax_exempt_status | P08 | 0.5% | 15% | 3710 |
| buyer_payment_method_preference | P08 | 0.7% | 15% | 3676 |
| buyer_logo_url | P13 | 74.6% | 95% | 3543 |
| buyer_ap_cycle_published | P13 | 0.0% | 20% | 3476 |
| vendor_trading_name | P08 | 36.8% | 50% | 3391 |
| ap_system_hint | P13 | 0.6% | 20% | 3372 |
| buyer_address | P13 | 77.3% | 95% | 3072 |

## 1. identifiers

### `invoice_reference_hint`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 126 | 91.3% | 91.3% | +2.6 | 50% | ✅ met |
| P01T | 427 | 93.9% | 93.9% | +4.4 | 50% | ✅ met |
| P01_GOLD | 625 | 92.2% | 94.4% | +0.0 | 95% | 🟡 3 pts to go |
| P02 | 471 | 73.0% | 74.5% | -0.8 | 95% | ❌ 22 pts to go |
| P03 | 257 | 82.1% | 85.2% | +0.1 | 95% | ❌ 13 pts to go |
| P04 | 3859 | 29.2% | 30.7% | -3.6 | 90% | ❌ 61 pts to go |
| P05 | 421 | 39.0% | 41.8% | +0.4 | 70% | ❌ 31 pts to go |
| P06M | 13192 | 91.5% | 91.5% | -1.1 | n/a | no target |
| P06T | 84475 | 97.1% | 97.1% | +16.8 | n/a | no target |
| P06 | 298 | 32.6% | 32.6% | +0.9 | 30% | ✅ met |
| P07 | 803 | 7.2% | 7.2% | +0.3 | 30% | ❌ 23 pts to go |
| P08 | 25629 | 1.2% | 1.2% | +0.1 | 25% | ❌ 24 pts to go |
| P09 | 295 | 99.0% | 99.7% | +0.0 | 100% | 🟡 1 pts to go |
| P10R | 102647 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P10 | 2648 | 2.7% | 2.8% | +0.1 | 25% | ❌ 22 pts to go |
| P11 | 20964 | 96.6% | 96.7% | +83.0 | 60% | ✅ met |
| P12 | 7 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P13 | 17390 | 0.2% | 0.2% | +0.0 | 0% by design | — leave (by design) |

### `po_number_as_published`

> ceiling: a purchase-order number exists only where the buyer publishes PO-level data (Montréal, Laval, Toronto open data so far) or the record itself carries one; most sources publish awards, not POs — the target cannot be reached from public data for most buyers

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 126 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P01T | 427 | 0.0% | 0.0% | +0.0 | 10% | 🟡 10 pts to go |
| P01_GOLD | 625 | 6.1% | 6.1% | +0.0 | 50% | ❌ 44 pts to go |
| P02 | 471 | 6.2% | 6.2% | +0.0 | 50% | ❌ 44 pts to go |
| P03 | 257 | 1.6% | 1.6% | +0.0 | 40% | ❌ 38 pts to go |
| P04 | 3859 | 0.5% | 0.5% | +0.0 | 30% | ❌ 30 pts to go |
| P05 | 421 | 0.2% | 0.2% | +0.0 | 20% | ❌ 20 pts to go |
| P06M | 13192 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06T | 84475 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06 | 298 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P07 | 803 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P08 | 25629 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P09 | 295 | 0.7% | 0.7% | +0.0 | 50% | ❌ 49 pts to go |
| P10R | 102647 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P10 | 2648 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P11 | 20964 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P12 | 7 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P13 | 17390 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `contract_or_agreement_number`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 126 | 84.1% | 84.1% | +2.7 | n/a | no target |
| P01T | 427 | 79.6% | 79.6% | +9.1 | 50% | ✅ met |
| P01_GOLD | 625 | 66.9% | 66.9% | +0.0 | 85% | ❌ 18 pts to go |
| P02 | 471 | 64.1% | 64.1% | -0.8 | 90% | ❌ 26 pts to go |
| P03 | 257 | 61.1% | 61.1% | -0.2 | 85% | ❌ 24 pts to go |
| P04 | 3859 | 26.6% | 26.6% | -3.5 | 85% | ❌ 58 pts to go |
| P05 | 421 | 29.0% | 29.0% | +0.0 | 60% | ❌ 31 pts to go |
| P06M | 13192 | 91.3% | 91.3% | -1.1 | n/a | no target |
| P06T | 84475 | 97.0% | 97.0% | +17.0 | n/a | no target |
| P06 | 298 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P07 | 803 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P08 | 25629 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P09 | 295 | 95.9% | 95.9% | -0.1 | 100% | 🟡 4 pts to go |
| P10R | 102647 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P10 | 2648 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P11 | 20964 | 96.4% | 96.4% | +83.7 | 60% | ✅ met |
| P12 | 7 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P13 | 17390 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `solicitation_or_tender_number`

> ceiling: SEAO's 'numero' is the organisation's own reference for the notice (SEAO data dictionary) and is reported here; sources that publish awards under a tender number only (bids&tenders, SaskTenders, BC) also carry it as the contract reference, labelled

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 126 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P01T | 427 | 0.0% | 0.0% | +0.0 | 30% | ❌ 30 pts to go |
| P01_GOLD | 625 | 50.7% | 50.7% | +0.1 | 80% | ❌ 29 pts to go |
| P02 | 471 | 56.3% | 56.3% | -0.7 | 60% | 🟡 4 pts to go |
| P03 | 257 | 51.4% | 51.4% | -0.2 | 80% | ❌ 29 pts to go |
| P04 | 3859 | 22.1% | 22.1% | -2.9 | 50% | ❌ 28 pts to go |
| P05 | 421 | 11.6% | 11.6% | -0.3 | 40% | ❌ 28 pts to go |
| P06M | 13192 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06T | 84475 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06 | 298 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P07 | 803 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P08 | 25629 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P09 | 295 | 83.1% | 83.1% | -0.4 | 50% | ✅ met |
| P10R | 102647 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P10 | 2648 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P11 | 20964 | 0.4% | 0.4% | -0.4 | 40% | ❌ 40 pts to go |
| P12 | 7 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P13 | 17390 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `award_or_notice_id`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 126 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P01T | 427 | 0.2% | 0.2% | -0.1 | n/a | no target |
| P01_GOLD | 625 | 60.5% | 60.5% | +0.1 | 85% | ❌ 24 pts to go |
| P02 | 471 | 55.6% | 55.6% | -0.7 | 90% | ❌ 34 pts to go |
| P03 | 257 | 59.9% | 59.9% | -0.3 | 85% | ❌ 25 pts to go |
| P04 | 3859 | 22.8% | 22.8% | -3.0 | 85% | ❌ 62 pts to go |
| P05 | 421 | 20.0% | 20.0% | +0.1 | 50% | ❌ 30 pts to go |
| P06M | 13192 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06T | 84475 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06 | 298 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P07 | 803 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P08 | 25629 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P09 | 295 | 96.9% | 96.9% | -0.1 | 100% | 🟡 3 pts to go |
| P10R | 102647 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P10 | 2648 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P11 | 20964 | 0.4% | 0.4% | -0.5 | 60% | ❌ 60 pts to go |
| P12 | 7 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P13 | 17390 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `buyer_vendor_id`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 126 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P01T | 427 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P01_GOLD | 625 | 13.0% | 13.0% | +0.1 | 60% | ❌ 47 pts to go |
| P02 | 471 | 5.9% | 5.9% | -0.1 | 50% | ❌ 44 pts to go |
| P03 | 257 | 8.6% | 8.6% | +0.0 | 50% | ❌ 41 pts to go |
| P04 | 3859 | 1.8% | 1.8% | -0.2 | 40% | ❌ 38 pts to go |
| P05 | 421 | 0.7% | 0.7% | -0.2 | 20% | ❌ 19 pts to go |
| P06M | 13192 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06T | 84475 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06 | 298 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P07 | 803 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P08 | 25629 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P09 | 295 | 2.4% | 2.4% | +0.1 | 50% | ❌ 48 pts to go |
| P10R | 102647 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P10 | 2648 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P11 | 20964 | 0.1% | 0.1% | +0.0 | n/a | no target |
| P12 | 7 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P13 | 17390 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `commodity_codes`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 126 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P01T | 427 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P01_GOLD | 625 | 34.9% | 34.9% | +0.1 | 80% | ❌ 45 pts to go |
| P02 | 471 | 51.4% | 51.4% | -0.6 | 90% | ❌ 39 pts to go |
| P03 | 257 | 33.5% | 33.5% | -0.1 | 80% | ❌ 46 pts to go |
| P04 | 3859 | 20.8% | 20.8% | -2.8 | 85% | ❌ 64 pts to go |
| P05 | 421 | 5.5% | 5.5% | +0.1 | 50% | ❌ 44 pts to go |
| P06M | 13192 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06T | 84475 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06 | 298 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P07 | 803 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P08 | 25629 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P09 | 295 | 75.6% | 75.6% | -0.3 | 95% | ❌ 19 pts to go |
| P10R | 102647 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P10 | 2648 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P11 | 20964 | 0.3% | 0.3% | -0.3 | 50% | ❌ 50 pts to go |
| P12 | 7 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P13 | 17390 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `buyer_org_codes`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 126 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P01T | 427 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P01_GOLD | 625 | 8.5% | 8.5% | +0.0 | 50% | ❌ 42 pts to go |
| P02 | 471 | 6.2% | 6.2% | +0.0 | 50% | ❌ 44 pts to go |
| P03 | 257 | 1.9% | 1.9% | -0.1 | 30% | ❌ 28 pts to go |
| P04 | 3859 | 0.4% | 0.4% | -0.1 | 30% | ❌ 30 pts to go |
| P05 | 421 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06M | 13192 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06T | 84475 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06 | 298 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P07 | 803 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P08 | 25629 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P09 | 295 | 0.3% | 0.3% | +0.0 | n/a | no target |
| P10R | 102647 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P10 | 2648 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P11 | 20964 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P12 | 7 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P13 | 17390 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `records_with_this_vendor`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 126 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P01T | 427 | 100.0% | 100.0% | +0.0 | 60% | ✅ met |
| P01_GOLD | 625 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P02 | 471 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P03 | 257 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P04 | 3859 | 100.0% | 100.0% | +0.0 | 95% | ✅ met |
| P05 | 421 | 100.0% | 100.0% | +0.0 | 70% | ✅ met |
| P06M | 13192 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P06T | 84475 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P06 | 298 | 100.0% | 100.0% | +0.0 | 50% | ✅ met |
| P07 | 803 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P08 | 25629 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P09 | 295 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P10R | 102647 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P10 | 2648 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P11 | 20964 | 100.0% | 100.0% | +0.0 | 70% | ✅ met |
| P12 | 7 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P13 | 17390 | 0.0% | 0.0% | +0.0 | n/a | no target |

## 2. vendor

### `vendor_bn9`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 126 | 8.7% | 8.7% | -5.7 | 70% | ❌ 61 pts to go |
| P01T | 427 | 29.3% | 29.3% | -4.4 | 60% | ❌ 31 pts to go |
| P01_GOLD | 625 | 72.6% | 72.6% | -0.4 | 90% | ❌ 17 pts to go |
| P02 | 471 | 53.5% | 53.5% | -1.6 | 85% | ❌ 32 pts to go |
| P03 | 257 | 68.1% | 68.1% | -1.8 | 90% | ❌ 22 pts to go |
| P04 | 3859 | 31.4% | 31.4% | -1.1 | 75% | ❌ 44 pts to go |
| P05 | 421 | 50.4% | 50.4% | +0.5 | 50% | ✅ met |
| P06M | 13192 | 1.6% | 1.6% | -0.2 | n/a | no target |
| P06T | 84475 | 22.5% | 22.5% | +5.2 | n/a | no target |
| P06 | 298 | 25.8% | 25.8% | +3.0 | 40% | ❌ 14 pts to go |
| P07 | 803 | 19.4% | 19.4% | +3.0 | 50% | ❌ 31 pts to go |
| P08 | 25629 | 15.7% | 15.7% | +4.8 | 50% | ❌ 34 pts to go |
| P09 | 295 | 58.3% | 58.3% | +0.5 | 80% | ❌ 22 pts to go |
| P10R | 102647 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P10 | 2648 | 30.8% | 30.8% | +2.1 | 40% | 🟡 9 pts to go |
| P11 | 20964 | 94.7% | 94.7% | +3.6 | 60% | ✅ met |
| P12 | 7 | 42.9% | 42.9% | -19.6 | 85% | ❌ 42 pts to go |
| P13 | 17390 | 90.9% | 90.9% | -0.1 | 0% by design | — leave (by design) |

### `vendor_registered_address`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 126 | 54.8% | 54.8% | -12.2 | n/a | no target |
| P01T | 427 | 38.2% | 38.2% | +0.2 | n/a | no target |
| P01_GOLD | 625 | 70.6% | 70.6% | +0.2 | 95% | ❌ 24 pts to go |
| P02 | 471 | 73.0% | 73.0% | -0.8 | 95% | ❌ 22 pts to go |
| P03 | 257 | 71.2% | 71.2% | -0.7 | 95% | ❌ 24 pts to go |
| P04 | 3859 | 43.4% | 43.4% | -2.2 | 95% | ❌ 52 pts to go |
| P05 | 421 | 53.2% | 53.2% | -0.2 | 70% | ❌ 17 pts to go |
| P06M | 13192 | 42.7% | 42.7% | -11.9 | n/a | no target |
| P06T | 84475 | 30.7% | 30.7% | +0.4 | n/a | no target |
| P06 | 298 | 25.2% | 25.2% | +0.4 | 80% | ❌ 55 pts to go |
| P07 | 803 | 17.9% | 17.9% | -0.1 | 70% | ❌ 52 pts to go |
| P08 | 25629 | 13.6% | 13.6% | -0.5 | 70% | ❌ 56 pts to go |
| P09 | 295 | 87.1% | 87.1% | -0.4 | 100% | ❌ 13 pts to go |
| P10R | 102647 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P10 | 2648 | 32.4% | 32.4% | -0.1 | 70% | ❌ 38 pts to go |
| P11 | 20964 | 95.1% | 95.1% | +2.9 | 75% | ✅ met |
| P12 | 7 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P13 | 17390 | 16.1% | 16.1% | +16.1 | n/a | no target |

### `vendor_trading_name`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 126 | 18.3% | 18.3% | +1.8 | n/a | no target |
| P01T | 427 | 60.9% | 60.9% | +35.0 | n/a | no target |
| P01_GOLD | 625 | 50.4% | 50.4% | +2.5 | 60% | 🟡 10 pts to go |
| P02 | 471 | 55.6% | 55.6% | +0.3 | 60% | 🟡 4 pts to go |
| P03 | 257 | 55.3% | 55.3% | +0.2 | 60% | 🟡 5 pts to go |
| P04 | 3859 | 40.0% | 40.0% | +3.3 | 55% | ❌ 15 pts to go |
| P05 | 421 | 24.5% | 24.5% | +2.3 | 50% | ❌ 26 pts to go |
| P06M | 13192 | 7.0% | 7.0% | +3.4 | n/a | no target |
| P06T | 84475 | 66.8% | 66.8% | +39.8 | n/a | no target |
| P06 | 298 | 47.7% | 47.7% | +12.5 | n/a | no target |
| P07 | 803 | 42.5% | 42.5% | +9.3 | 55% | ❌ 12 pts to go |
| P08 | 25629 | 36.8% | 36.8% | +9.9 | 50% | ❌ 13 pts to go |
| P09 | 295 | 73.2% | 73.2% | +2.2 | 70% | ✅ met |
| P10R | 102647 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P10 | 2648 | 48.8% | 48.8% | +9.3 | 55% | 🟡 6 pts to go |
| P11 | 20964 | 97.0% | 97.0% | +5.0 | 50% | ✅ met |
| P12 | 7 | 100.0% | 100.0% | +12.5 | n/a | no target |
| P13 | 17390 | 74.4% | 74.4% | +74.4 | n/a | no target |

### `vendor_phone`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 126 | 49.2% | 49.2% | +34.8 | n/a | no target |
| P01T | 427 | 77.0% | 77.0% | +20.7 | n/a | no target |
| P01_GOLD | 625 | 49.9% | 49.9% | +2.0 | 70% | ❌ 20 pts to go |
| P02 | 471 | 58.0% | 58.0% | +4.0 | 70% | ❌ 12 pts to go |
| P03 | 257 | 50.6% | 50.6% | +1.0 | 70% | ❌ 19 pts to go |
| P04 | 3859 | 54.0% | 54.0% | +6.9 | 65% | ❌ 11 pts to go |
| P05 | 421 | 27.8% | 27.8% | -2.9 | 60% | ❌ 32 pts to go |
| P06M | 13192 | 36.6% | 36.6% | +33.1 | n/a | no target |
| P06T | 84475 | 70.6% | 70.6% | +6.8 | n/a | no target |
| P06 | 298 | 68.8% | 68.8% | +11.2 | 40% | ✅ met |
| P07 | 803 | 64.8% | 64.8% | +7.8 | 85% | ❌ 20 pts to go |
| P08 | 25629 | 66.0% | 66.0% | +9.1 | 85% | ❌ 19 pts to go |
| P09 | 295 | 60.7% | 60.7% | +7.2 | 85% | ❌ 24 pts to go |
| P10R | 102647 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P10 | 2648 | 64.4% | 64.4% | +3.4 | 85% | ❌ 21 pts to go |
| P11 | 20964 | 4.0% | 4.0% | -2.4 | 75% | ❌ 71 pts to go |
| P12 | 7 | 28.6% | 28.6% | +3.6 | n/a | no target |
| P13 | 17390 | 100.0% | 100.0% | +0.0 | 60% | ✅ met |

### `vendor_website`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 126 | 54.0% | 54.0% | +34.4 | n/a | no target |
| P01T | 427 | 98.4% | 98.4% | +2.0 | n/a | no target |
| P01_GOLD | 625 | 79.5% | 79.5% | -9.8 | 90% | ❌ 10 pts to go |
| P02 | 471 | 84.3% | 84.3% | -4.9 | 90% | 🟡 6 pts to go |
| P03 | 257 | 87.5% | 87.5% | -3.5 | 90% | 🟡 2 pts to go |
| P04 | 3859 | 85.3% | 85.3% | -4.9 | 85% | ✅ met |
| P05 | 421 | 43.9% | 43.9% | -8.3 | 70% | ❌ 26 pts to go |
| P06M | 13192 | 42.8% | 42.8% | +36.6 | n/a | no target |
| P06T | 84475 | 100.0% | 100.0% | +8.0 | n/a | no target |
| P06 | 298 | 98.3% | 98.3% | +0.0 | 50% | ✅ met |
| P07 | 803 | 99.1% | 99.1% | +0.0 | 100% | 🟡 1 pts to go |
| P08 | 25629 | 99.5% | 99.5% | +0.1 | 100% | 🟡 0 pts to go |
| P09 | 295 | 80.3% | 80.3% | +0.1 | 100% | ❌ 20 pts to go |
| P10R | 102647 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P10 | 2648 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P11 | 20964 | 99.8% | 99.8% | +0.1 | 100% | 🟡 0 pts to go |
| P12 | 7 | 28.6% | 28.6% | -8.9 | n/a | no target |
| P13 | 17390 | 100.0% | 100.0% | +0.0 | n/a | no target |

### `vendor_emails`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 126 | 15.1% | 15.1% | +0.7 | n/a | no target |
| P01T | 427 | 54.6% | 54.6% | +5.5 | n/a | no target |
| P01_GOLD | 625 | 43.5% | 43.5% | -1.7 | 70% | ❌ 26 pts to go |
| P02 | 471 | 49.3% | 49.3% | -0.2 | 75% | ❌ 26 pts to go |
| P03 | 257 | 44.0% | 44.0% | -0.5 | 75% | ❌ 31 pts to go |
| P04 | 3859 | 39.1% | 39.1% | +1.7 | 70% | ❌ 31 pts to go |
| P05 | 421 | 21.4% | 21.4% | -4.1 | 55% | ❌ 34 pts to go |
| P06M | 13192 | 4.6% | 4.6% | +1.3 | n/a | no target |
| P06T | 84475 | 40.1% | 40.1% | +0.5 | n/a | no target |
| P06 | 298 | 47.7% | 47.7% | +4.9 | n/a | no target |
| P07 | 803 | 49.6% | 49.6% | +3.7 | 70% | ❌ 20 pts to go |
| P08 | 25629 | 54.1% | 54.1% | +4.2 | 75% | ❌ 21 pts to go |
| P09 | 295 | 50.2% | 50.2% | +0.4 | 85% | ❌ 35 pts to go |
| P10R | 102647 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P10 | 2648 | 45.6% | 45.6% | +2.1 | 80% | ❌ 34 pts to go |
| P11 | 20964 | 3.3% | 3.3% | -1.7 | 70% | ❌ 67 pts to go |
| P12 | 7 | 14.3% | 14.3% | -10.7 | n/a | no target |
| P13 | 17390 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `vendor_logo_url`

> ceiling: needs the vendor's website first; sites that block automated readers (robots.txt / 403) are never read

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 126 | 54.0% | 54.0% | +40.6 | n/a | no target |
| P01T | 427 | 96.7% | 96.7% | +6.9 | n/a | no target |
| P01_GOLD | 625 | 73.8% | 73.8% | -3.7 | 90% | ❌ 16 pts to go |
| P02 | 471 | 79.4% | 79.4% | +1.8 | 90% | ❌ 11 pts to go |
| P03 | 257 | 82.9% | 82.9% | -0.3 | 90% | 🟡 7 pts to go |
| P04 | 3859 | 78.9% | 78.9% | +3.3 | 85% | 🟡 6 pts to go |
| P05 | 421 | 42.3% | 42.3% | -6.4 | 75% | ❌ 33 pts to go |
| P06M | 13192 | 42.5% | 42.5% | +38.4 | n/a | no target |
| P06T | 84475 | 97.6% | 97.6% | +14.4 | n/a | no target |
| P06 | 298 | 90.6% | 90.6% | +11.3 | n/a | no target |
| P07 | 803 | 91.8% | 91.8% | +10.2 | 100% | 🟡 8 pts to go |
| P08 | 25629 | 90.8% | 90.8% | +11.9 | 100% | 🟡 9 pts to go |
| P09 | 295 | 66.8% | 66.8% | +5.4 | n/a | no target |
| P10R | 102647 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P10 | 2648 | 88.4% | 88.4% | +4.2 | 100% | ❌ 12 pts to go |
| P11 | 20964 | 94.9% | 94.9% | +6.5 | n/a | no target |
| P12 | 7 | 28.6% | 28.6% | -8.9 | n/a | no target |
| P13 | 17390 | 83.9% | 83.9% | +0.7 | n/a | no target |

### `vendor_neq`

> ceiling: only Québec-registered vendors have an NEQ; the share of QC vendors is reported next to the rate

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 126 | 46.0% | 46.0% | -7.6 | n/a | no target · QC vendors: 45 rows, 100.0% filled |
| P01T | 427 | 21.8% | 21.8% | +4.0 | n/a | no target · QC vendors: 22 rows, 100.0% filled |
| P01_GOLD | 625 | 43.7% | 43.7% | +0.1 | 95% | ❌ 51 pts to go · QC vendors: 53 rows, 98.1% filled |
| P02 | 471 | 54.4% | 54.4% | -0.7 | 95% | ❌ 41 pts to go · QC vendors: 110 rows, 100.0% filled |
| P03 | 257 | 45.9% | 45.9% | -0.6 | 95% | ❌ 49 pts to go · QC vendors: 18 rows, 100.0% filled |
| P04 | 3859 | 28.1% | 28.1% | -3.8 | 95% | ❌ 67 pts to go · QC vendors: 497 rows, 98.8% filled |
| P05 | 421 | 14.0% | 14.0% | -0.8 | n/a | no target · QC vendors: 34 rows, 94.1% filled |
| P06M | 13192 | 41.8% | 41.8% | -11.5 | n/a | no target · QC vendors: 4833 rows, 100.0% filled |
| P06T | 84475 | 19.7% | 19.7% | +2.2 | n/a | no target · QC vendors: 3549 rows, 100.0% filled |
| P06 | 298 | 8.1% | 8.1% | -0.2 | n/a | no target · QC vendors: 17 rows, 76.5% filled |
| P07 | 803 | 6.0% | 6.0% | -0.8 | n/a | no target · QC vendors: 40 rows, 80.0% filled |
| P08 | 25629 | 6.1% | 6.1% | -0.4 | n/a | no target · QC vendors: 1253 rows, 97.9% filled |
| P09 | 295 | 78.0% | 78.0% | -0.2 | 95% | ❌ 17 pts to go · QC vendors: 106 rows, 100.0% filled |
| P10R | 102647 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P10 | 2648 | 17.5% | 17.5% | -0.1 | n/a | no target · QC vendors: 305 rows, 94.8% filled |
| P11 | 20964 | 89.9% | 89.9% | +8.4 | n/a | no target · QC vendors: 115 rows, 98.3% filled |
| P12 | 7 | 71.4% | 71.4% | +8.9 | n/a | no target · QC vendors: 1 rows, 100.0% filled |
| P13 | 17390 | 16.1% | 16.1% | +16.1 | n/a | no target · QC vendors: 2798 rows, 100.0% filled |

### `vendor_years_in_business`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 126 | 54.0% | 54.0% | -10.9 | n/a | no target · vendors with a registry record: 68 rows, 100.0% filled |
| P01T | 427 | 38.2% | 38.2% | -0.1 | n/a | no target · vendors with a registry record: 163 rows, 100.0% filled |
| P01_GOLD | 625 | 79.5% | 79.5% | +0.1 | 100% | ❌ 20 pts to go · vendors with a registry record: 497 rows, 100.0% filled |
| P02 | 471 | 76.6% | 76.6% | -0.8 | 100% | ❌ 23 pts to go · vendors with a registry record: 361 rows, 100.0% filled |
| P03 | 257 | 80.5% | 80.5% | -0.7 | 100% | ❌ 20 pts to go · vendors with a registry record: 207 rows, 100.0% filled |
| P04 | 3859 | 43.8% | 43.8% | -2.3 | 100% | ❌ 56 pts to go · vendors with a registry record: 1691 rows, 100.0% filled |
| P05 | 421 | 58.2% | 58.2% | -0.1 | n/a | no target · vendors with a registry record: 245 rows, 100.0% filled |
| P06M | 13192 | 42.6% | 42.6% | -11.7 | n/a | no target · vendors with a registry record: 5617 rows, 100.0% filled |
| P06T | 84475 | 30.7% | 30.7% | +0.3 | n/a | no target · vendors with a registry record: 25925 rows, 100.0% filled |
| P06 | 298 | 25.5% | 25.5% | +0.0 | n/a | no target · vendors with a registry record: 76 rows, 100.0% filled |
| P07 | 803 | 18.3% | 18.3% | -0.1 | n/a | no target · vendors with a registry record: 147 rows, 100.0% filled |
| P08 | 25629 | 13.8% | 13.8% | -0.5 | n/a | no target · vendors with a registry record: 3540 rows, 100.0% filled |
| P09 | 295 | 90.8% | 90.8% | -0.3 | n/a | no target · vendors with a registry record: 268 rows, 100.0% filled |
| P10R | 102647 | 100.0% | 100.0% | +0.0 | n/a | no target · vendors with a registry record: 102647 rows, 100.0% filled |
| P10 | 2648 | 33.0% | 33.0% | -0.2 | n/a | no target · vendors with a registry record: 875 rows, 100.0% filled |
| P11 | 20964 | 95.2% | 95.2% | +2.9 | n/a | no target · vendors with a registry record: 19959 rows, 100.0% filled |
| P12 | 7 | 100.0% | 100.0% | +0.0 | n/a | no target · vendors with a registry record: 7 rows, 100.0% filled |
| P13 | 17390 | 16.1% | 16.1% | +16.1 | n/a | no target · vendors with a registry record: 2798 rows, 100.0% filled |

## 3. buyer

### `buyer_legal_name_as_published`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 126 | 94.4% | 94.4% | +5.7 | 90% | ✅ met |
| P01T | 427 | 67.4% | 67.4% | +11.1 | 90% | ❌ 23 pts to go |
| P01_GOLD | 625 | 87.5% | 87.5% | +3.8 | 95% | 🟡 8 pts to go |
| P02 | 471 | 88.7% | 88.7% | +3.5 | 95% | 🟡 6 pts to go |
| P03 | 257 | 84.4% | 84.4% | +5.5 | 85% | 🟡 1 pts to go |
| P04 | 3859 | 64.3% | 64.3% | +7.9 | 90% | ❌ 26 pts to go |
| P05 | 421 | 79.8% | 79.8% | +12.1 | 75% | ✅ met |
| P06M | 13192 | 91.8% | 91.8% | +4.7 | n/a | no target |
| P06T | 84475 | 41.4% | 41.4% | +12.4 | n/a | no target |
| P06 | 298 | 75.2% | 75.2% | +18.3 | 80% | 🟡 5 pts to go |
| P07 | 803 | 60.4% | 60.5% | +14.2 | 80% | ❌ 20 pts to go |
| P08 | 25629 | 54.2% | 54.2% | +15.7 | 75% | ❌ 21 pts to go |
| P09 | 295 | 77.3% | 77.3% | +0.1 | 95% | ❌ 18 pts to go |
| P10R | 102647 | 38.9% | 38.9% | +13.9 | n/a | no target |
| P10 | 2648 | 51.9% | 51.9% | +12.9 | 70% | ❌ 18 pts to go |
| P11 | 20964 | 43.4% | 43.4% | +33.8 | 65% | ❌ 22 pts to go |
| P12 | 7 | 71.4% | 71.4% | -3.6 | 80% | 🟡 9 pts to go |
| P13 | 17390 | 51.9% | 51.9% | +12.7 | 60% | 🟡 8 pts to go |

### `buyer_bn_as_published`

> ceiling: a buyer's BN is public only where the buyer prints it or a public dataset carries it (CRA charities, federal grants & contributions recipients, business registries for corporations); municipalities rarely publish theirs

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 126 | 19.0% | 19.0% | -0.6 | 50% | ❌ 31 pts to go |
| P01T | 427 | 12.4% | 12.4% | -0.9 | n/a | no target |
| P01_GOLD | 625 | 19.0% | 19.0% | -1.6 | 40% | ❌ 21 pts to go |
| P02 | 471 | 19.1% | 19.1% | +0.2 | 40% | ❌ 21 pts to go |
| P03 | 257 | 21.8% | 21.8% | -0.5 | 40% | ❌ 18 pts to go |
| P04 | 3859 | 14.4% | 14.4% | -1.9 | 40% | ❌ 26 pts to go |
| P05 | 421 | 15.7% | 15.7% | -4.0 | 25% | 🟡 9 pts to go |
| P06M | 13192 | 10.4% | 10.4% | +1.6 | n/a | no target |
| P06T | 84475 | 7.3% | 7.3% | -0.2 | n/a | no target |
| P06 | 298 | 15.8% | 15.8% | +3.0 | 35% | ❌ 19 pts to go |
| P07 | 803 | 14.2% | 14.2% | +2.7 | 35% | ❌ 21 pts to go |
| P08 | 25629 | 13.6% | 13.6% | +3.2 | 35% | ❌ 21 pts to go |
| P09 | 295 | 16.3% | 16.3% | +0.1 | n/a | no target |
| P10R | 102647 | 8.5% | 8.5% | +1.4 | n/a | no target |
| P10 | 2648 | 10.8% | 10.8% | +4.3 | 30% | ❌ 19 pts to go |
| P11 | 20964 | 1.4% | 1.4% | +0.2 | n/a | no target |
| P12 | 7 | 14.3% | 14.3% | +1.8 | n/a | no target |
| P13 | 17390 | 21.0% | 21.0% | +0.0 | 30% | 🟡 9 pts to go |

### `buyer_address`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 126 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P01T | 427 | 89.0% | 89.0% | -2.9 | 100% | ❌ 11 pts to go |
| P01_GOLD | 625 | 90.7% | 90.7% | +1.2 | 100% | 🟡 9 pts to go |
| P02 | 471 | 95.8% | 95.8% | +0.5 | 100% | 🟡 4 pts to go |
| P03 | 257 | 89.9% | 89.9% | +0.4 | 100% | ❌ 10 pts to go |
| P04 | 3859 | 75.5% | 75.5% | -0.4 | 100% | ❌ 24 pts to go |
| P05 | 421 | 89.1% | 89.1% | +1.7 | 100% | ❌ 11 pts to go |
| P06M | 13192 | 99.1% | 99.1% | +0.3 | n/a | no target |
| P06T | 84475 | 75.4% | 75.4% | -2.0 | n/a | no target |
| P06 | 298 | 81.5% | 81.5% | +0.5 | 95% | ❌ 14 pts to go |
| P07 | 803 | 83.9% | 83.9% | +0.3 | 95% | ❌ 11 pts to go |
| P08 | 25629 | 80.3% | 80.3% | +0.1 | 95% | ❌ 15 pts to go |
| P09 | 295 | 95.9% | 95.9% | +0.2 | 100% | 🟡 4 pts to go |
| P10R | 102647 | 61.0% | 61.0% | +2.2 | n/a | no target |
| P10 | 2648 | 66.1% | 66.2% | +1.0 | 95% | ❌ 29 pts to go |
| P11 | 20964 | 93.7% | 93.7% | +6.5 | 80% | ✅ met |
| P12 | 7 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P13 | 17390 | 77.3% | 77.3% | +2.1 | 95% | ❌ 18 pts to go |

### `buyer_phone`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 126 | 86.5% | 86.5% | +0.9 | n/a | no target |
| P01T | 427 | 71.4% | 71.4% | +7.8 | n/a | no target |
| P01_GOLD | 625 | 72.8% | 72.8% | +3.3 | 90% | ❌ 17 pts to go |
| P02 | 471 | 77.7% | 77.7% | +2.0 | 95% | ❌ 17 pts to go |
| P03 | 257 | 74.3% | 74.3% | +0.5 | 95% | ❌ 21 pts to go |
| P04 | 3859 | 69.5% | 69.5% | +2.9 | 95% | ❌ 26 pts to go |
| P05 | 421 | 73.2% | 73.2% | +2.7 | 90% | ❌ 17 pts to go |
| P06M | 13192 | 87.4% | 87.4% | +1.0 | n/a | no target |
| P06T | 84475 | 57.6% | 57.6% | +9.7 | n/a | no target |
| P06 | 298 | 71.1% | 71.1% | +8.0 | 95% | ❌ 24 pts to go |
| P07 | 803 | 66.3% | 66.3% | +11.3 | 90% | ❌ 24 pts to go |
| P08 | 25629 | 68.9% | 68.9% | +10.1 | 95% | ❌ 26 pts to go |
| P09 | 295 | 86.4% | 86.4% | +0.3 | 100% | ❌ 14 pts to go |
| P10R | 102647 | 59.0% | 59.0% | +13.9 | n/a | no target |
| P10 | 2648 | 60.3% | 60.3% | +3.8 | 95% | ❌ 35 pts to go |
| P11 | 20964 | 25.9% | 25.9% | +14.7 | 75% | ❌ 49 pts to go |
| P12 | 7 | 71.4% | 71.4% | -3.6 | n/a | no target |
| P13 | 17390 | 63.2% | 63.2% | +15.6 | 95% | ❌ 32 pts to go |

### `buyer_logo_url`

> ceiling: sites that block automated readers (robots.txt / 403) are never read; an og:image that looks like a photo is labelled

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 126 | 89.7% | 89.7% | +18.6 | n/a | no target |
| P01T | 427 | 83.8% | 83.8% | +9.7 | 95% | ❌ 11 pts to go |
| P01_GOLD | 625 | 84.8% | 84.8% | +4.1 | 90% | 🟡 5 pts to go |
| P02 | 471 | 90.7% | 90.7% | +4.9 | 95% | 🟡 4 pts to go |
| P03 | 257 | 85.6% | 85.6% | +1.6 | 95% | 🟡 9 pts to go |
| P04 | 3859 | 89.3% | 89.3% | +6.0 | 90% | 🟡 1 pts to go |
| P05 | 421 | 93.1% | 93.1% | +4.6 | 95% | 🟡 2 pts to go |
| P06M | 13192 | 95.2% | 95.2% | +28.5 | n/a | no target |
| P06T | 84475 | 77.0% | 77.0% | +15.5 | n/a | no target |
| P06 | 298 | 93.3% | 93.3% | +11.2 | 100% | 🟡 7 pts to go |
| P07 | 803 | 92.4% | 92.4% | +15.2 | 100% | 🟡 8 pts to go |
| P08 | 25629 | 92.6% | 92.6% | +15.5 | 100% | 🟡 7 pts to go |
| P09 | 295 | 72.5% | 72.5% | +3.9 | n/a | no target |
| P10R | 102647 | 82.5% | 82.5% | +22.5 | n/a | no target |
| P10 | 2648 | 92.0% | 92.0% | +5.2 | 100% | 🟡 8 pts to go |
| P11 | 20964 | 66.3% | 66.3% | +47.5 | 80% | ❌ 14 pts to go |
| P12 | 7 | 71.4% | 71.4% | -3.6 | n/a | no target |
| P13 | 17390 | 74.6% | 74.6% | +23.6 | 95% | ❌ 20 pts to go |

## 4. AP

### `ap_contact_name_as_published`

> ceiling: owner 2026-11-08: the AP contact person the organisation itself names on its AP / finance page is allowed (name + role phrase, quoted); mailboxes stay organisational; many bodies publish no AP person

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 126 | 2.4% | 2.4% | -1.7 | n/a | no target |
| P01T | 427 | 7.0% | 7.0% | -1.4 | n/a | no target |
| P01_GOLD | 625 | 14.2% | 14.2% | +0.0 | 25% | ❌ 11 pts to go |
| P02 | 471 | 24.2% | 24.2% | -0.3 | 40% | ❌ 16 pts to go |
| P03 | 257 | 8.9% | 8.9% | -0.1 | 20% | ❌ 11 pts to go |
| P04 | 3859 | 3.2% | 3.2% | -0.4 | 20% | ❌ 17 pts to go |
| P05 | 421 | 3.3% | 3.3% | +0.0 | 15% | ❌ 12 pts to go |
| P06M | 13192 | 0.3% | 0.3% | +0.0 | n/a | no target |
| P06T | 84475 | 0.3% | 0.3% | -0.1 | n/a | no target |
| P06 | 298 | 5.7% | 5.7% | -0.5 | n/a | no target |
| P07 | 803 | 7.6% | 7.6% | +0.3 | n/a | no target |
| P08 | 25629 | 0.3% | 0.3% | +0.0 | n/a | no target |
| P09 | 295 | 7.8% | 7.8% | +0.2 | n/a | no target |
| P10R | 102647 | 0.2% | 0.2% | +0.0 | n/a | no target |
| P10 | 2648 | 0.9% | 0.9% | -0.1 | n/a | no target |
| P11 | 20964 | 0.1% | 0.1% | -0.1 | n/a | no target |
| P12 | 7 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P13 | 17390 | 0.4% | 0.4% | +0.0 | n/a | no target |

### `ap_phone`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 126 | 21.4% | 21.4% | -5.4 | n/a | no target |
| P01T | 427 | 21.3% | 21.3% | -2.8 | 70% | ❌ 49 pts to go |
| P01_GOLD | 625 | 43.4% | 43.4% | +0.1 | 80% | ❌ 37 pts to go |
| P02 | 471 | 56.5% | 56.5% | -0.3 | 90% | ❌ 34 pts to go |
| P03 | 257 | 19.1% | 19.1% | +0.0 | 60% | ❌ 41 pts to go |
| P04 | 3859 | 21.0% | 21.0% | -2.7 | 85% | ❌ 64 pts to go |
| P05 | 421 | 11.9% | 11.9% | +0.0 | 50% | ❌ 38 pts to go |
| P06M | 13192 | 0.7% | 0.7% | +0.3 | n/a | no target |
| P06T | 84475 | 0.6% | 0.6% | +0.0 | n/a | no target |
| P06 | 298 | 15.4% | 15.4% | -0.8 | n/a | no target |
| P07 | 803 | 11.3% | 11.3% | -1.7 | n/a | no target |
| P08 | 25629 | 0.6% | 0.6% | +0.1 | n/a | no target |
| P09 | 295 | 77.3% | 77.3% | -0.3 | 95% | ❌ 18 pts to go |
| P10R | 102647 | 0.2% | 0.2% | +0.0 | n/a | no target |
| P10 | 2648 | 1.7% | 1.7% | +0.0 | n/a | no target |
| P11 | 20964 | 2.0% | 2.0% | -1.6 | n/a | no target |
| P12 | 7 | 28.6% | 28.6% | +3.6 | n/a | no target |
| P13 | 17390 | 0.7% | 0.7% | +0.0 | n/a | no target |

### `invoice_mailing_address`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 126 | 8.7% | 8.7% | +1.5 | n/a | no target |
| P01T | 427 | 11.5% | 11.5% | -0.5 | n/a | no target |
| P01_GOLD | 625 | 33.9% | 33.9% | +0.0 | 70% | ❌ 36 pts to go |
| P02 | 471 | 38.4% | 38.4% | -0.5 | 75% | ❌ 37 pts to go |
| P03 | 257 | 19.1% | 19.1% | +0.0 | 55% | ❌ 36 pts to go |
| P04 | 3859 | 20.9% | 20.9% | -2.7 | 75% | ❌ 54 pts to go |
| P05 | 421 | 10.7% | 10.7% | -0.1 | 50% | ❌ 39 pts to go |
| P06M | 13192 | 0.2% | 0.2% | +0.0 | n/a | no target |
| P06T | 84475 | 0.3% | 0.3% | -0.1 | n/a | no target |
| P06 | 298 | 7.4% | 7.4% | -0.9 | n/a | no target |
| P07 | 803 | 5.5% | 5.5% | -0.9 | n/a | no target |
| P08 | 25629 | 0.2% | 0.2% | +0.0 | n/a | no target |
| P09 | 295 | 74.9% | 74.9% | -0.3 | 95% | ❌ 20 pts to go |
| P10R | 102647 | 0.1% | 0.1% | -0.1 | n/a | no target |
| P10 | 2648 | 1.0% | 1.0% | +0.0 | n/a | no target |
| P11 | 20964 | 1.9% | 1.9% | -1.7 | n/a | no target |
| P12 | 7 | 14.3% | 14.3% | +1.8 | n/a | no target |
| P13 | 17390 | 0.4% | 0.4% | +0.0 | n/a | no target |

### `invoicing_requirements`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 126 | 8.7% | 8.7% | +2.5 | n/a | no target |
| P01T | 427 | 8.0% | 8.0% | -1.3 | n/a | no target |
| P01_GOLD | 625 | 57.9% | 58.1% | -0.1 | 80% | ❌ 22 pts to go |
| P02 | 471 | 45.2% | 45.4% | -0.6 | 75% | ❌ 30 pts to go |
| P03 | 257 | 37.7% | 37.7% | -0.2 | 70% | ❌ 32 pts to go |
| P04 | 3859 | 20.5% | 20.9% | -2.6 | 70% | ❌ 50 pts to go |
| P05 | 421 | 14.5% | 14.5% | +0.2 | 50% | ❌ 36 pts to go |
| P06M | 13192 | 0.4% | 0.4% | +0.0 | n/a | no target |
| P06T | 84475 | 0.2% | 0.2% | -0.1 | n/a | no target |
| P06 | 298 | 14.4% | 14.4% | +1.0 | n/a | no target |
| P07 | 803 | 2.0% | 2.0% | +0.0 | n/a | no target |
| P08 | 25629 | 0.4% | 0.4% | +0.0 | n/a | no target |
| P09 | 295 | 46.1% | 46.4% | +0.2 | 80% | ❌ 34 pts to go |
| P10R | 102647 | 0.1% | 0.1% | +0.0 | n/a | no target |
| P10 | 2648 | 1.2% | 1.2% | +0.0 | n/a | no target |
| P11 | 20964 | 0.6% | 0.6% | -0.5 | n/a | no target |
| P12 | 7 | 42.9% | 42.9% | +5.4 | n/a | no target |
| P13 | 17390 | 0.3% | 0.3% | +0.0 | n/a | no target |

### `payment_terms_as_published`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 126 | 19.0% | 19.0% | +7.7 | n/a | no target |
| P01T | 427 | 17.6% | 17.6% | -4.4 | 60% | ❌ 42 pts to go |
| P01_GOLD | 625 | 63.5% | 63.5% | -0.1 | 70% | 🟡 6 pts to go |
| P02 | 471 | 39.1% | 39.1% | +0.2 | 50% | ❌ 11 pts to go |
| P03 | 257 | 49.8% | 49.8% | -0.2 | 55% | 🟡 5 pts to go |
| P04 | 3859 | 12.4% | 12.4% | -0.9 | 40% | ❌ 28 pts to go |
| P05 | 421 | 17.3% | 17.3% | +0.0 | 40% | ❌ 23 pts to go |
| P06M | 13192 | 2.4% | 2.4% | +1.7 | n/a | no target |
| P06T | 84475 | 2.6% | 2.6% | +0.2 | n/a | no target |
| P06 | 298 | 21.1% | 21.1% | +1.4 | n/a | no target |
| P07 | 803 | 6.8% | 6.8% | +0.1 | n/a | no target |
| P08 | 25629 | 2.9% | 2.9% | +0.3 | n/a | no target |
| P09 | 295 | 5.8% | 5.8% | -0.1 | n/a | no target |
| P10R | 102647 | 0.2% | 0.2% | +0.0 | n/a | no target |
| P10 | 2648 | 4.6% | 4.6% | +0.1 | n/a | no target |
| P11 | 20964 | 9.4% | 9.4% | +5.1 | n/a | no target |
| P12 | 7 | 0.0% | 0.0% | -12.5 | n/a | no target |
| P13 | 17390 | 0.2% | 0.2% | +0.0 | n/a | no target |

### `po_required_as_published`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 126 | 23.0% | 23.0% | +6.5 | n/a | no target |
| P01T | 427 | 22.5% | 22.5% | -2.8 | 65% | ❌ 42 pts to go |
| P01_GOLD | 625 | 69.0% | 69.0% | +0.0 | 70% | 🟡 1 pts to go |
| P02 | 471 | 23.8% | 23.8% | -0.1 | 50% | ❌ 26 pts to go |
| P03 | 257 | 52.5% | 52.5% | +0.2 | 60% | 🟡 8 pts to go |
| P04 | 3859 | 5.3% | 5.3% | -0.5 | 40% | ❌ 35 pts to go |
| P05 | 421 | 20.0% | 20.0% | +0.3 | 45% | ❌ 25 pts to go |
| P06M | 13192 | 1.5% | 1.5% | +1.2 | n/a | no target |
| P06T | 84475 | 0.6% | 0.6% | +0.0 | n/a | no target |
| P06 | 298 | 32.6% | 32.6% | +0.9 | n/a | no target |
| P07 | 803 | 7.2% | 7.2% | +0.3 | n/a | no target |
| P08 | 25629 | 1.2% | 1.2% | +0.1 | n/a | no target |
| P09 | 295 | 9.8% | 9.8% | -0.1 | n/a | no target |
| P10R | 102647 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P10 | 2648 | 2.7% | 2.7% | +0.1 | n/a | no target |
| P11 | 20964 | 1.0% | 1.0% | +0.0 | n/a | no target |
| P12 | 7 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P13 | 17390 | 0.2% | 0.2% | +0.0 | n/a | no target |

### `invoice_portal_url`

> ceiling: only portals the buyer names on its own pages; informational tax-authority links are not portals

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 126 | 13.5% | 13.5% | +7.3 | n/a | no target |
| P01T | 427 | 12.2% | 12.2% | -2.3 | n/a | no target |
| P01_GOLD | 625 | 49.8% | 49.8% | +0.0 | 50% | 🟡 0 pts to go |
| P02 | 471 | 36.9% | 36.9% | -0.5 | n/a | no target |
| P03 | 257 | 52.9% | 52.9% | -0.2 | 60% | 🟡 7 pts to go |
| P04 | 3859 | 11.4% | 11.4% | -1.5 | n/a | no target |
| P05 | 421 | 15.0% | 15.0% | -0.2 | n/a | no target |
| P06M | 13192 | 0.6% | 0.6% | +0.3 | n/a | no target |
| P06T | 84475 | 0.4% | 0.4% | -0.1 | n/a | no target |
| P06 | 298 | 23.8% | 23.8% | +2.1 | n/a | no target |
| P07 | 803 | 7.5% | 7.5% | +0.3 | n/a | no target |
| P08 | 25629 | 0.6% | 0.6% | +0.1 | n/a | no target |
| P09 | 295 | 18.3% | 18.3% | +0.1 | n/a | no target |
| P10R | 102647 | 0.1% | 0.1% | +0.0 | n/a | no target |
| P10 | 2648 | 2.4% | 2.4% | +0.1 | n/a | no target |
| P11 | 20964 | 0.7% | 0.7% | -0.1 | n/a | no target |
| P12 | 7 | 14.3% | 14.3% | +14.3 | n/a | no target |
| P13 | 17390 | 0.4% | 0.4% | +0.0 | n/a | no target |

### `buyer_payment_method_preference`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 126 | 11.9% | 11.9% | +0.6 | 15% | 🟡 3 pts to go |
| P01T | 427 | 9.8% | 9.8% | -1.3 | 15% | 🟡 5 pts to go |
| P01_GOLD | 625 | 35.4% | 35.4% | +0.1 | 40% | 🟡 5 pts to go |
| P02 | 471 | 13.0% | 13.2% | +0.5 | 25% | ❌ 12 pts to go |
| P03 | 257 | 17.9% | 17.9% | -0.1 | 25% | 🟡 7 pts to go |
| P04 | 3859 | 2.7% | 2.7% | -0.1 | 15% | ❌ 12 pts to go |
| P05 | 421 | 6.7% | 6.7% | -0.1 | 15% | 🟡 8 pts to go |
| P06M | 13192 | 0.9% | 0.9% | +0.3 | 15% | ❌ 14 pts to go |
| P06T | 84475 | 0.6% | 0.6% | +0.2 | 15% | ❌ 14 pts to go |
| P06 | 298 | 10.4% | 10.4% | +1.1 | 15% | 🟡 5 pts to go |
| P07 | 803 | 4.0% | 4.0% | +0.8 | 15% | ❌ 11 pts to go |
| P08 | 25629 | 0.7% | 0.7% | +0.3 | 15% | ❌ 14 pts to go |
| P09 | 295 | 1.0% | 1.0% | +0.0 | 15% | ❌ 14 pts to go |
| P10R | 102647 | 0.6% | 0.6% | +0.2 | 15% | ❌ 14 pts to go |
| P10 | 2648 | 1.2% | 1.2% | +0.2 | 15% | ❌ 14 pts to go |
| P11 | 20964 | 0.4% | 0.4% | +0.2 | 15% | ❌ 15 pts to go |
| P12 | 7 | 14.3% | 14.3% | +1.8 | 15% | 🟡 1 pts to go |
| P13 | 17390 | 0.6% | 0.6% | +0.2 | 15% | ❌ 14 pts to go |

### `buyer_tax_exempt_status`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 126 | 6.3% | 6.3% | +0.1 | 15% | 🟡 9 pts to go |
| P01T | 427 | 9.4% | 9.4% | -2.6 | 25% | ❌ 16 pts to go |
| P01_GOLD | 625 | 29.1% | 29.1% | -0.1 | 25% | ✅ met |
| P02 | 471 | 25.1% | 25.1% | -0.3 | 15% | ✅ met |
| P03 | 257 | 21.4% | 21.4% | -0.1 | 15% | ✅ met |
| P04 | 3859 | 3.9% | 3.9% | -0.2 | 15% | ❌ 11 pts to go |
| P05 | 421 | 11.2% | 11.2% | +0.4 | 15% | 🟡 4 pts to go |
| P06M | 13192 | 0.6% | 0.6% | +0.4 | 15% | ❌ 14 pts to go |
| P06T | 84475 | 0.3% | 0.3% | +0.0 | 15% | ❌ 15 pts to go |
| P06 | 298 | 8.4% | 8.4% | +0.8 | 15% | 🟡 7 pts to go |
| P07 | 803 | 3.0% | 3.0% | -0.1 | 15% | ❌ 12 pts to go |
| P08 | 25629 | 0.5% | 0.5% | +0.1 | 15% | ❌ 14 pts to go |
| P09 | 295 | 1.0% | 1.0% | +0.0 | 15% | ❌ 14 pts to go |
| P10R | 102647 | 0.0% | 0.0% | +0.0 | 15% | ❌ 15 pts to go |
| P10 | 2648 | 1.5% | 1.5% | -0.1 | 15% | ❌ 14 pts to go |
| P11 | 20964 | 0.5% | 0.5% | +0.0 | 15% | ❌ 14 pts to go |
| P12 | 7 | 28.6% | 28.6% | +3.6 | 15% | ✅ met |
| P13 | 17390 | 0.1% | 0.1% | +0.1 | 15% | ❌ 15 pts to go |

### `buyer_ap_cycle_published`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 126 | 1.6% | 1.6% | +1.6 | 20% | ❌ 18 pts to go |
| P01T | 427 | 3.0% | 3.0% | -0.9 | 20% | ❌ 17 pts to go |
| P01_GOLD | 625 | 4.5% | 4.5% | +0.2 | 20% | ❌ 16 pts to go |
| P02 | 471 | 1.5% | 1.5% | +0.2 | 20% | ❌ 18 pts to go |
| P03 | 257 | 1.6% | 1.6% | +0.0 | 20% | ❌ 18 pts to go |
| P04 | 3859 | 0.5% | 0.5% | -0.1 | 20% | ❌ 20 pts to go |
| P05 | 421 | 1.2% | 1.2% | +0.0 | 20% | ❌ 19 pts to go |
| P06M | 13192 | 0.1% | 0.1% | +0.1 | 20% | ❌ 20 pts to go |
| P06T | 84475 | 0.0% | 0.0% | +0.0 | 20% | ❌ 20 pts to go |
| P06 | 298 | 1.3% | 1.3% | -0.1 | 20% | ❌ 19 pts to go |
| P07 | 803 | 0.4% | 0.4% | +0.0 | 20% | ❌ 20 pts to go |
| P08 | 25629 | 0.0% | 0.0% | +0.0 | 20% | ❌ 20 pts to go |
| P09 | 295 | 0.0% | 0.0% | +0.0 | 20% | ❌ 20 pts to go |
| P10R | 102647 | 0.0% | 0.0% | +0.0 | 20% | ❌ 20 pts to go |
| P10 | 2648 | 0.3% | 0.3% | +0.0 | 20% | ❌ 20 pts to go |
| P11 | 20964 | 0.0% | 0.0% | +0.0 | 20% | ❌ 20 pts to go |
| P12 | 7 | 0.0% | 0.0% | +0.0 | 20% | ❌ 20 pts to go |
| P13 | 17390 | 0.0% | 0.0% | +0.0 | 20% | ❌ 20 pts to go |

### `buyer_esignature_preference`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 126 | 1.6% | 1.6% | +0.6 | 15% | ❌ 13 pts to go |
| P01T | 427 | 2.3% | 2.3% | -0.1 | 15% | ❌ 13 pts to go |
| P01_GOLD | 625 | 10.4% | 10.4% | -0.1 | 15% | 🟡 5 pts to go |
| P02 | 471 | 11.9% | 11.9% | -0.1 | 15% | 🟡 3 pts to go |
| P03 | 257 | 20.6% | 20.6% | -0.1 | 15% | ✅ met |
| P04 | 3859 | 2.3% | 2.3% | -0.1 | 15% | ❌ 13 pts to go |
| P05 | 421 | 2.9% | 2.9% | -0.1 | 15% | ❌ 12 pts to go |
| P06M | 13192 | 0.4% | 0.4% | +0.2 | 15% | ❌ 15 pts to go |
| P06T | 84475 | 0.2% | 0.2% | +0.0 | 15% | ❌ 15 pts to go |
| P06 | 298 | 5.4% | 5.4% | +0.2 | 15% | 🟡 10 pts to go |
| P07 | 803 | 1.7% | 1.7% | +0.0 | 15% | ❌ 13 pts to go |
| P08 | 25629 | 0.5% | 0.5% | +0.1 | 15% | ❌ 14 pts to go |
| P09 | 295 | 0.7% | 0.7% | +0.0 | 15% | ❌ 14 pts to go |
| P10R | 102647 | 0.0% | 0.0% | +0.0 | 15% | ❌ 15 pts to go |
| P10 | 2648 | 1.0% | 1.0% | +0.1 | 15% | ❌ 14 pts to go |
| P11 | 20964 | 0.4% | 0.4% | +0.1 | 15% | ❌ 15 pts to go |
| P12 | 7 | 0.0% | 0.0% | +0.0 | 15% | ❌ 15 pts to go |
| P13 | 17390 | 0.1% | 0.1% | +0.0 | 15% | ❌ 15 pts to go |

### `ap_system_hint`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 126 | 15.1% | 15.1% | +7.9 | 20% | 🟡 5 pts to go |
| P01T | 427 | 12.9% | 12.9% | -2.2 | 40% | ❌ 27 pts to go |
| P01_GOLD | 625 | 46.1% | 46.1% | +0.3 | 40% | ✅ met |
| P02 | 471 | 42.5% | 42.5% | -0.3 | 20% | ✅ met |
| P03 | 257 | 49.0% | 49.0% | +0.2 | 35% | ✅ met |
| P04 | 3859 | 13.8% | 13.8% | -1.6 | 20% | 🟡 6 pts to go |
| P05 | 421 | 15.2% | 15.2% | +0.4 | 20% | 🟡 5 pts to go |
| P06M | 13192 | 0.9% | 0.9% | +0.4 | 20% | ❌ 19 pts to go |
| P06T | 84475 | 0.7% | 0.7% | +0.0 | 20% | ❌ 19 pts to go |
| P06 | 298 | 23.8% | 23.8% | +1.7 | 20% | ✅ met |
| P07 | 803 | 8.0% | 8.0% | +0.9 | 20% | ❌ 12 pts to go |
| P08 | 25629 | 1.1% | 1.1% | +0.2 | 20% | ❌ 19 pts to go |
| P09 | 295 | 19.0% | 19.0% | +0.8 | 20% | 🟡 1 pts to go |
| P10R | 102647 | 0.2% | 0.2% | +0.0 | 20% | ❌ 20 pts to go |
| P10 | 2648 | 3.5% | 3.5% | +0.1 | 20% | ❌ 16 pts to go |
| P11 | 20964 | 0.8% | 0.8% | -0.2 | 20% | ❌ 19 pts to go |
| P12 | 7 | 0.0% | 0.0% | +0.0 | 20% | ❌ 20 pts to go |
| P13 | 17390 | 0.6% | 0.6% | +0.1 | 20% | ❌ 19 pts to go |

## 5. contract

### `contract_value`

> ceiling: rows proven by a lobbying filing, a news release, an auditor appointment, a customer story or a vendor's client list have no contract value by nature (≈17 % of P01 Gold); bids&tenders awards now carry the awarded bidder's submitted price when no award value was published

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 126 | 32.5% | 32.5% | -11.8 | n/a | no target |
| P01T | 427 | 0.2% | 0.2% | -0.1 | n/a | no target |
| P01_GOLD | 625 | 69.4% | 69.4% | -0.1 | 95% | ❌ 26 pts to go |
| P02 | 471 | 62.2% | 62.2% | -0.8 | 95% | ❌ 33 pts to go |
| P03 | 257 | 54.5% | 54.5% | -0.2 | 90% | ❌ 36 pts to go |
| P04 | 3859 | 24.0% | 24.0% | -3.1 | 85% | ❌ 61 pts to go |
| P05 | 421 | 37.3% | 37.3% | +0.8 | 75% | ❌ 38 pts to go |
| P06M | 13192 | 35.5% | 35.5% | -14.6 | n/a | no target |
| P06T | 84475 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06 | 298 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P07 | 803 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P08 | 25629 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P09 | 295 | 89.5% | 89.5% | +0.1 | 100% | ❌ 10 pts to go |
| P10R | 102647 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P10 | 2648 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P11 | 20964 | 0.4% | 0.4% | -0.5 | 60% | ❌ 60 pts to go |
| P12 | 7 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P13 | 17390 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `currency`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 126 | 32.5% | 32.5% | -11.8 | n/a | no target |
| P01T | 427 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P01_GOLD | 625 | 72.8% | 72.8% | +0.0 | 100% | ❌ 27 pts to go |
| P02 | 471 | 65.6% | 65.6% | -0.9 | 100% | ❌ 34 pts to go |
| P03 | 257 | 60.3% | 60.3% | -0.2 | n/a | no target |
| P04 | 3859 | 24.6% | 24.6% | -3.2 | 95% | ❌ 70 pts to go |
| P05 | 421 | 33.3% | 33.3% | +0.3 | 80% | ❌ 47 pts to go |
| P06M | 13192 | 35.5% | 35.5% | -14.6 | n/a | no target |
| P06T | 84475 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06 | 298 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P07 | 803 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P08 | 25629 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P09 | 295 | 92.5% | 92.5% | -0.2 | 100% | 🟡 8 pts to go |
| P10R | 102647 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P10 | 2648 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P11 | 20964 | 0.4% | 0.4% | -0.6 | n/a | no target |
| P12 | 7 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P13 | 17390 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `start_date`

> ceiling: most award notices publish an award date, not a start date; start_date carries the signature date when the source gives one, labelled

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 126 | 82.5% | 82.5% | +4.1 | n/a | no target |
| P01T | 427 | 0.2% | 0.2% | -0.1 | n/a | no target |
| P01_GOLD | 625 | 51.7% | 51.7% | +0.1 | 85% | ❌ 33 pts to go |
| P02 | 471 | 56.9% | 56.9% | -0.7 | 90% | ❌ 33 pts to go |
| P03 | 257 | 43.6% | 43.6% | -0.5 | 85% | ❌ 41 pts to go |
| P04 | 3859 | 27.0% | 27.0% | -3.4 | 90% | ❌ 63 pts to go |
| P05 | 421 | 33.3% | 33.3% | +0.5 | 75% | ❌ 42 pts to go |
| P06M | 13192 | 89.7% | 89.7% | -0.7 | n/a | no target |
| P06T | 84475 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06 | 298 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P07 | 803 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P08 | 25629 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P09 | 295 | 85.1% | 85.1% | +0.0 | 95% | 🟡 10 pts to go |
| P10R | 102647 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P10 | 2648 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P11 | 20964 | 0.4% | 0.4% | -0.4 | n/a | no target |
| P12 | 7 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P13 | 17390 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `end_date`

> ceiling: an inferred end (award date + published duration) is labelled as such; sources without a duration leave end_date empty — the honest ceiling. P09 is BY DEFINITION the rows whose end date is not published (older SEAO contracts with no closing notice): its end_date / duration targets cannot be met without inventing a date

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 126 | 81.7% | 81.7% | +2.3 | n/a | no target |
| P01T | 427 | 0.2% | 0.2% | -0.1 | n/a | no target |
| P01_GOLD | 625 | 51.8% | 51.8% | +0.0 | 85% | ❌ 33 pts to go |
| P02 | 471 | 52.0% | 52.0% | -0.7 | 90% | ❌ 38 pts to go |
| P03 | 257 | 44.7% | 44.7% | -0.6 | 85% | ❌ 40 pts to go |
| P04 | 3859 | 23.0% | 23.0% | -3.0 | 90% | ❌ 67 pts to go |
| P05 | 421 | 43.7% | 43.7% | +0.8 | 75% | ❌ 31 pts to go |
| P06M | 13192 | 80.5% | 80.5% | -3.2 | n/a | no target |
| P06T | 84475 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06 | 298 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P07 | 803 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P08 | 25629 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P09 | 295 | 0.3% | 0.3% | +0.0 | 95% | ❌ 95 pts to go |
| P10R | 102647 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P10 | 2648 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P11 | 20964 | 0.3% | 0.3% | -0.4 | n/a | no target |
| P12 | 7 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P13 | 17390 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `contract_title`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 126 | 90.5% | 90.5% | +4.9 | n/a | no target |
| P01T | 427 | 91.8% | 91.8% | -0.4 | n/a | no target |
| P01_GOLD | 625 | 85.4% | 85.4% | -0.1 | 100% | ❌ 15 pts to go |
| P02 | 471 | 74.7% | 74.7% | -1.0 | 100% | ❌ 25 pts to go |
| P03 | 257 | 91.4% | 91.4% | -0.8 | n/a | no target |
| P04 | 3859 | 45.5% | 45.5% | -6.0 | 95% | ❌ 50 pts to go |
| P05 | 421 | 77.4% | 77.4% | -0.4 | 95% | ❌ 18 pts to go |
| P06M | 13192 | 98.8% | 98.8% | +0.5 | n/a | no target |
| P06T | 84475 | 81.3% | 81.3% | -2.4 | n/a | no target |
| P06 | 298 | 25.5% | 25.5% | -0.7 | n/a | no target |
| P07 | 803 | 16.8% | 16.8% | -2.3 | n/a | no target |
| P08 | 25629 | 9.8% | 9.8% | -1.2 | n/a | no target |
| P09 | 295 | 98.6% | 98.6% | -0.1 | 100% | 🟡 1 pts to go |
| P10R | 102647 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P10 | 2648 | 71.0% | 71.0% | -0.7 | n/a | no target |
| P11 | 20964 | 9.0% | 9.0% | -7.1 | n/a | no target |
| P12 | 7 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P13 | 17390 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `contract_description`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 126 | 90.5% | 90.5% | +4.9 | n/a | no target |
| P01T | 427 | 91.8% | 91.8% | -0.4 | n/a | no target |
| P01_GOLD | 625 | 88.6% | 88.6% | -0.1 | 100% | ❌ 11 pts to go |
| P02 | 471 | 75.8% | 76.0% | -1.0 | 100% | ❌ 24 pts to go |
| P03 | 257 | 92.2% | 92.2% | -0.8 | n/a | no target |
| P04 | 3859 | 48.7% | 48.7% | -6.4 | 95% | ❌ 46 pts to go |
| P05 | 421 | 90.0% | 90.0% | -0.2 | 70% | ✅ met |
| P06M | 13192 | 98.8% | 98.8% | +0.5 | n/a | no target |
| P06T | 84475 | 81.3% | 81.3% | -2.4 | n/a | no target |
| P06 | 298 | 25.5% | 25.5% | -0.7 | n/a | no target |
| P07 | 803 | 16.8% | 16.8% | -2.3 | n/a | no target |
| P08 | 25629 | 9.8% | 9.8% | -1.2 | n/a | no target |
| P09 | 295 | 98.6% | 98.6% | -0.1 | 100% | 🟡 1 pts to go |
| P10R | 102647 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P10 | 2648 | 71.0% | 71.0% | -0.7 | n/a | no target |
| P11 | 20964 | 9.0% | 9.0% | -7.1 | n/a | no target |
| P12 | 7 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P13 | 17390 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `number_of_bids`

> ceiling: published by some portals only (bids&tenders submission lists, Biddingo bidder lists); federal proactive disclosure does not publish bid counts

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 126 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P01T | 427 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P01_GOLD | 625 | 16.8% | 16.8% | +0.0 | 60% | ❌ 43 pts to go · rows from a source that publishes bids: 363 rows, 28.9% filled |
| P02 | 471 | 11.0% | 11.0% | -0.2 | n/a | no target · rows from a source that publishes bids: 290 rows, 17.9% filled |
| P03 | 257 | 13.2% | 13.2% | -0.1 | n/a | no target · rows from a source that publishes bids: 139 rows, 24.5% filled |
| P04 | 3859 | 1.4% | 1.4% | -0.2 | n/a | no target · rows from a source that publishes bids: 872 rows, 6.3% filled |
| P05 | 421 | 2.9% | 2.9% | -0.1 | n/a | no target · rows from a source that publishes bids: 51 rows, 23.5% filled |
| P06M | 13192 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06T | 84475 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06 | 298 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P07 | 803 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P08 | 25629 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P09 | 295 | 3.1% | 3.1% | +0.1 | n/a | no target · rows from a source that publishes bids: 282 rows, 3.2% filled |
| P10R | 102647 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P10 | 2648 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P11 | 20964 | 0.1% | 0.1% | +0.0 | n/a | no target · rows from a source that publishes bids: 88 rows, 13.6% filled |
| P12 | 7 | 0.0% | 0.0% | +0.0 | n/a | no target · rows from a source that publishes bids: 7 rows, 0.0% filled |
| P13 | 17390 | 0.0% | 0.0% | +0.0 | n/a | no target |

## 6. history

### `average_contract_duration_days`

> ceiling: needs two dates (or a published term) on the buyer's records; P09 rows (end date unpublished by definition) and buyers whose sources publish award dates only have no honest duration

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 126 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P01T | 427 | 0.2% | 98.6% | -0.1 | n/a | no target |
| P01_GOLD | 625 | 53.3% | 82.4% | +0.1 | 90% | ❌ 37 pts to go |
| P02 | 471 | 51.8% | 87.7% | -0.7 | 90% | ❌ 38 pts to go |
| P03 | 257 | 45.5% | 80.2% | -0.2 | 90% | ❌ 44 pts to go |
| P04 | 3859 | 18.5% | 94.1% | -2.4 | 90% | ❌ 72 pts to go |
| P05 | 421 | 0.0% | 83.1% | +0.0 | 90% | ❌ 90 pts to go |
| P06M | 13192 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P06T | 84475 | 0.0% | 99.9% | +0.0 | n/a | no target |
| P06 | 298 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P07 | 803 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P08 | 25629 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P09 | 295 | 2.4% | 4.1% | +0.1 | 90% | ❌ 88 pts to go |
| P10R | 102647 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P10 | 2648 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P11 | 20964 | 0.3% | 99.8% | -0.3 | n/a | no target |
| P12 | 7 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P13 | 17390 | 0.0% | 100.0% | +0.0 | n/a | no target |

### `commodity_distribution_top3`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 126 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P01T | 427 | 0.5% | 98.8% | -0.1 | n/a | no target |
| P01_GOLD | 625 | 25.9% | 55.0% | +0.0 | 90% | ❌ 64 pts to go |
| P02 | 471 | 51.0% | 86.8% | -0.6 | n/a | no target |
| P03 | 257 | 24.9% | 59.5% | -0.1 | n/a | no target |
| P04 | 3859 | 20.2% | 95.9% | -2.7 | n/a | no target |
| P05 | 421 | 0.5% | 83.6% | +0.0 | n/a | no target |
| P06M | 13192 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P06T | 84475 | 0.0% | 100.0% | -0.1 | n/a | no target |
| P06 | 298 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P07 | 803 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P08 | 25629 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P09 | 295 | 41.4% | 43.1% | -0.5 | n/a | no target |
| P10R | 102647 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P10 | 2648 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P11 | 20964 | 0.3% | 99.8% | -0.3 | n/a | no target |
| P12 | 7 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P13 | 17390 | 0.0% | 100.0% | +0.0 | n/a | no target |

### `year_over_year_spend_trend`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 126 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P01T | 427 | 1.4% | 99.8% | -0.1 | n/a | no target |
| P01_GOLD | 625 | 51.8% | 81.0% | +0.0 | 95% | ❌ 43 pts to go |
| P02 | 471 | 55.8% | 91.7% | -0.8 | n/a | no target |
| P03 | 257 | 47.9% | 82.5% | -0.1 | n/a | no target |
| P04 | 3859 | 20.4% | 96.1% | -2.7 | n/a | no target |
| P05 | 421 | 4.5% | 87.6% | -0.2 | n/a | no target |
| P06M | 13192 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P06T | 84475 | 0.1% | 100.0% | +0.0 | n/a | no target |
| P06 | 298 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P07 | 803 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P08 | 25629 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P09 | 295 | 63.7% | 65.4% | -0.3 | n/a | no target |
| P10R | 102647 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P10 | 2648 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P11 | 20964 | 0.3% | 99.8% | -0.3 | n/a | no target |
| P12 | 7 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P13 | 17390 | 0.0% | 100.0% | +0.0 | n/a | no target |

## 7. mail security

### `mta_sts`

> ceiling: DNS-only check; 'no record' counts as checked

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 126 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P01T | 427 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P01_GOLD | 625 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P02 | 471 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P03 | 257 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P04 | 3859 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P05 | 421 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P06M | 13192 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P06T | 84475 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P06 | 298 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P07 | 803 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P08 | 25629 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P09 | 295 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P10R | 102647 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P10 | 2648 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P11 | 20964 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P12 | 7 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P13 | 17390 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |

### `tls_rpt`

> ceiling: DNS-only check; 'no record' counts as checked

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 126 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P01T | 427 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P01_GOLD | 625 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P02 | 471 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P03 | 257 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P04 | 3859 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P05 | 421 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P06M | 13192 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P06T | 84475 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P06 | 298 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P07 | 803 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P08 | 25629 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P09 | 295 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P10R | 102647 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P10 | 2648 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P11 | 20964 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P12 | 7 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P13 | 17390 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |

### `bimi`

> ceiling: DNS-only check; 'no record' counts as checked

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 126 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P01T | 427 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P01_GOLD | 625 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P02 | 471 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P03 | 257 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P04 | 3859 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P05 | 421 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P06M | 13192 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P06T | 84475 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P06 | 298 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P07 | 803 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P08 | 25629 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P09 | 295 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P10R | 102647 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P10 | 2648 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P11 | 20964 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P12 | 7 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P13 | 17390 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |

