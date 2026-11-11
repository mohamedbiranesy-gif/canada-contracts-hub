# Coverage vs the downstream team's targets — 2026-11-11

Benchmarks (field × package with a numeric target): **93 of 446 met** (20.9%); 58 within 10 points; 295 further away.
A cell counts as filled only when it carries a value: blank, `not_published`, `not_found_yet` and label-only cells ("no identifier published …", "no dataset record …", "0 in the contract dataset …") do not count; the DNS checks count when checked. `any` = share of non-blank cells incl. such labels. Δ = change since the previous build in `coord/results/coverage_history.csv`.
Rows per package: P01M 105, P01T 334, P01_GOLD 625, P02 474, P03 257, P04 3887, P05 427, P06M 10630, P06T 60045, P06 312, P07 838, P08 26652, P09 303, P10R 98993, P10 2735, P11 11585, P12 7, P13 18053

## Invoice-grade readiness (the row as an invoice header: bill-to, submit-to, references, terms, tax, vendor identity, follow-up)

| package | rows | all 11 elements | ≥ 9 of 11 | median elements | most-missing element |
|---|---|---|---|---|---|
| P01M | 105 | 0.0% | 15.2% | 8 | vendor GST/HST number (92 rows) |
| P01T | 334 | 0.9% | 20.1% | 7 | payment terms (259 rows) |
| P01_GOLD | 625 | 23.7% | 67.7% | 9 | payment terms (214 rows) |
| P02 | 474 | 7.2% | 50.6% | 9 | PO rule (363 rows) |
| P03 | 257 | 13.6% | 57.2% | 9 | PO rule (123 rows) |
| P04 | 3887 | 1.2% | 15.2% | 6 | PO rule (3691 rows) |
| P05 | 427 | 0.9% | 16.9% | 7 | payment terms (351 rows) |
| P06M | 10630 | 0.0% | 1.4% | 8 | PO rule (10599 rows) |
| P06T | 60045 | 0.0% | 3.2% | 6 | PO rule (59695 rows) |
| P06 | 312 | 0.0% | 7.1% | 6 | reference to quote (PO / contract / vendor id) (312 rows) |
| P07 | 838 | 0.0% | 1.6% | 5 | reference to quote (PO / contract / vendor id) (838 rows) |
| P08 | 26652 | 0.0% | 0.2% | 5 | reference to quote (PO / contract / vendor id) (26652 rows) |
| P09 | 303 | 1.0% | 43.2% | 8 | payment terms (283 rows) |
| P10R | 98993 | 0.0% | 19.9% | 7 | PO rule (98951 rows) |
| P10 | 2735 | 0.0% | 0.7% | 5 | reference to quote (PO / contract / vendor id) (2735 rows) |
| P11 | 11585 | 0.1% | 2.0% | 6 | PO rule (11485 rows) |
| P12 | 7 | 0.0% | 42.9% | 8 | PO rule (7 rows) |
| P13 | 18053 | 0.0% | 0.0% | 6 | reference to quote (PO / contract / vendor id) (18053 rows) |

## AP grade (how stringently the row's accounts-payable data meets what an invoice needs; A = invoicing mailbox referee-confirmed on the buyer's own domain with MX, legal name, address, PO rule and terms all published, no penalties)

| package | rows | A | B | C | D | E | median ap_score |
|---|---|---|---|---|---|---|---|
| P01M | 105 | 9 | 9 | 87 | 0 | 0 | 71 |
| P01T | 334 | 31 | 58 | 245 | 0 | 0 | 71 |
| P01_GOLD | 625 | 226 | 189 | 210 | 0 | 0 | 81 |
| P02 | 474 | 0 | 190 | 284 | 0 | 0 | 66 |
| P03 | 257 | 0 | 0 | 244 | 13 | 0 | 57 |
| P04 | 3887 | 0 | 0 | 3137 | 750 | 0 | 45 |
| P05 | 427 | 15 | 29 | 365 | 18 | 0 | 51 |
| P06M | 10630 | 0 | 3 | 10565 | 62 | 0 | 46 |
| P06T | 60045 | 0 | 42 | 50247 | 9756 | 0 | 38 |
| P06 | 312 | 18 | 44 | 250 | 0 | 0 | 67 |
| P07 | 838 | 0 | 25 | 784 | 29 | 0 | 51 |
| P08 | 26652 | 0 | 0 | 22230 | 4422 | 0 | 38 |
| P09 | 303 | 3 | 12 | 285 | 3 | 0 | 53 |
| P10R | 98993 | 2 | 11 | 68312 | 30668 | 0 | 38 |
| P10 | 2735 | 2 | 13 | 2010 | 710 | 0 | 43 |
| P11 | 11585 | 6 | 9 | 44 | 0 | 11526 | 23 |
| P12 | 7 | 0 | 0 | 7 | 0 | 0 | 51 |
| P13 | 18053 | 0 | 14 | 14643 | 3396 | 0 | 43 |

### AP payability (confirmed channel + bill-to legal name and address + the buyer's reference rule + tax treatment known)

| package | rows | payable today | % | most common gap |
|---|---|---|---|---|
| P01M | 105 | 81 | 77.1% | bill-to legal name and address (11) |
| P01T | 334 | 177 | 53.0% | bill-to legal name and address (118) |
| P01_GOLD | 625 | 462 | 73.9% | bill-to legal name and address (109) |
| P02 | 474 | 308 | 65.0% | the buyer's PO / reference rule (86) |
| P03 | 257 | 0 | 0.0% | a confirmed invoicing / AP or finance channel (257) |
| P04 | 3887 | 0 | 0.0% | a confirmed invoicing / AP or finance channel (3887) |
| P05 | 427 | 46 | 10.8% | a confirmed invoicing / AP or finance channel (340) |
| P06M | 10630 | 102 | 1.0% | a confirmed invoicing / AP or finance channel (10486) |
| P06T | 60045 | 379 | 0.6% | a confirmed invoicing / AP or finance channel (59146) |
| P06 | 312 | 41 | 13.1% | bill-to legal name and address (144) |
| P07 | 838 | 11 | 1.3% | bill-to legal name and address (389) |
| P08 | 26652 | 0 | 0.0% | a confirmed invoicing / AP or finance channel (26652) |
| P09 | 303 | 41 | 13.5% | a confirmed invoicing / AP or finance channel (253) |
| P10R | 98993 | 477 | 0.5% | a confirmed invoicing / AP or finance channel (97860) |
| P10 | 2735 | 4 | 0.1% | a confirmed invoicing / AP or finance channel (2638) |
| P11 | 11585 | 10 | 0.1% | a confirmed invoicing / AP or finance channel (11526) |
| P12 | 7 | 2 | 28.6% | a confirmed invoicing / AP or finance channel (5) |
| P13 | 18053 | 6 | 0.0% | a confirmed invoicing / AP or finance channel (17705) |

### Pay on sight (an invoice generated from the row would clear AP: confirmed invoicing / AP or finance channel, bill-to legal name + address, vendor legal name + GST/HST number + remit-to address, tax treatment and currency known — published or labelled-derived; the buyer's reference rule is reported separately)

| package | rows | pay on sight | % | + reference rule not published | routed (general inbox only) | most common gap |
|---|---|---|---|---|---|---|
| P01M | 105 | 5 | 4.8% | 6 | 0 | the vendor's GST/HST number (BN9) (91) |
| P01T | 334 | 63 | 18.9% | 22 | 0 | the vendor's GST/HST number (BN9) (192) |
| P01_GOLD | 625 | 396 | 63.4% | 13 | 0 | the vendor's GST/HST number (BN9) (154) |
| P02 | 474 | 211 | 44.5% | 23 | 0 | the vendor's GST/HST number (BN9) (208) |
| P03 | 257 | 16 | 6.2% | 0 | 132 | an invoicing / AP or finance mailbox (only a purchasing / general inbo (88) |
| P04 | 3887 | 42 | 1.1% | 8 | 784 | an invoicing / AP or finance mailbox (only a purchasing / general inbo (2994) |
| P05 | 427 | 22 | 5.2% | 8 | 111 | an invoicing / AP or finance mailbox (only a purchasing / general inbo (222) |
| P06M | 10630 | 1 | 0.0% | 10 | 151 | an invoicing / AP or finance mailbox (only a purchasing / general inbo (10314) |
| P06T | 60045 | 93 | 0.2% | 92 | 10588 | an invoicing / AP or finance mailbox (only a purchasing / general inbo (48404) |
| P06 | 312 | 16 | 5.1% | 33 | 0 | the vendor's GST/HST number (BN9) (183) |
| P07 | 838 | 4 | 0.5% | 72 | 27 | the vendor's GST/HST number (BN9) (452) |
| P08 | 26652 | 1 | 0.0% | 7 | 2718 | an invoicing / AP or finance mailbox (only a purchasing / general inbo (23869) |
| P09 | 303 | 38 | 12.5% | 1 | 121 | an invoicing / AP or finance mailbox (only a purchasing / general inbo (123) |
| P10R | 98993 | 843 | 0.9% | 0 | 53367 | an invoicing / AP or finance mailbox (only a purchasing / general inbo (44431) |
| P10 | 2735 | 4 | 0.1% | 20 | 392 | an invoicing / AP or finance mailbox (only a purchasing / general inbo (2216) |
| P11 | 11585 | 11 | 0.1% | 11 | 0 | a confirmed invoicing / AP or finance channel (11494) |
| P12 | 7 | 1 | 14.3% | 0 | 3 | an invoicing / AP or finance mailbox (only a purchasing / general inbo (2) |
| P13 | 18053 | 9 | 0.0% | 250 | 10697 | an invoicing / AP or finance mailbox (only a purchasing / general inbo (6968) |
| **all** | 236262 | 1776 | 0.8% | 576 | 79091 | |

### What still blocks grade A (rows per missing element; a row counts under every element it lacks)

| package | rows not A | referee confirmation of the mailbox | an invoicing / AP mailbox (not finance / procurement / general) | a mailbox on the buyer's own domain | MX record for the mailbox domain | published bill-to legal name | invoice / billing address | published PO rule | published payment terms | clear the penalty |
|---|---|---|---|---|---|---|---|---|---|---|
| P01M | 96 | 0 | 0 | 0 | 36 | 11 | 0 | 87 | 92 | 0 |
| P01T | 303 | 0 | 0 | 0 | 134 | 106 | 25 | 250 | 261 | 31 |
| P01_GOLD | 399 | 0 | 0 | 0 | 11 | 93 | 33 | 194 | 228 | 57 |
| P02 | 474 | 0 | 474 | 0 | 50 | 71 | 21 | 363 | 293 | 22 |
| P03 | 257 | 0 | 257 | 0 | 14 | 48 | 25 | 123 | 129 | 25 |
| P04 | 3887 | 0 | 3887 | 0 | 1847 | 1829 | 974 | 3691 | 3432 | 131 |
| P05 | 412 | 0 | 359 | 0 | 73 | 112 | 49 | 343 | 353 | 52 |
| P06M | 10630 | 0 | 10630 | 0 | 5663 | 1173 | 108 | 10599 | 10558 | 27 |
| P06T | 60045 | 0 | 60045 | 0 | 45924 | 35154 | 12654 | 59695 | 58599 | 372 |
| P06 | 294 | 0 | 0 | 0 | 128 | 129 | 53 | 220 | 255 | 4 |
| P07 | 838 | 0 | 838 | 0 | 496 | 438 | 141 | 786 | 788 | 15 |
| P08 | 26652 | 0 | 26652 | 0 | 19647 | 15774 | 5539 | 26400 | 26050 | 230 |
| P09 | 300 | 0 | 279 | 0 | 9 | 69 | 3 | 273 | 285 | 44 |
| P10R | 98991 | 0 | 98818 | 0 | 76302 | 65461 | 39033 | 98951 | 98802 | 27 |
| P10 | 2733 | 0 | 2696 | 0 | 1315 | 1590 | 935 | 2665 | 2614 | 114 |
| P11 | 11579 | 11526 | 11467 | 0 | 10186 | 7892 | 929 | 11485 | 11136 | 39 |
| P12 | 7 | 0 | 6 | 0 | 0 | 2 | 0 | 7 | 7 | 0 |
| P13 | 18053 | 0 | 17947 | 0 | 8936 | 9956 | 4125 | 18019 | 18016 | 20 |

## Where the work is (largest gaps in rows still needed)

| field | package | now | target | rows needed |
|---|---|---|---|---|
| buyer_ap_cycle_published | P10R | 0.0% | 20% | 19778 |
| ap_system_hint | P10R | 0.2% | 20% | 19598 |
| vendor_registered_address | P08 | 12.6% | 70% | 15302 |
| buyer_tax_exempt_status | P10R | 0.0% | 15% | 14819 |
| buyer_esignature_preference | P10R | 0.0% | 15% | 14804 |
| buyer_payment_method_preference | P10R | 0.6% | 15% | 14247 |
| buyer_ap_cycle_published | P06T | 0.0% | 20% | 11988 |
| ap_system_hint | P06T | 0.7% | 20% | 11560 |
| buyer_phone | P08 | 56.5% | 95% | 10273 |
| vendor_bn9 | P08 | 14.3% | 50% | 9517 |
| buyer_legal_name_as_published | P08 | 40.8% | 75% | 9111 |
| buyer_esignature_preference | P06T | 0.2% | 15% | 8867 |
| buyer_tax_exempt_status | P06T | 0.3% | 15% | 8821 |
| buyer_payment_method_preference | P06T | 0.6% | 15% | 8659 |
| vendor_phone | P11 | 5.5% | 75% | 8051 |
| vendor_emails | P11 | 4.2% | 70% | 7619 |
| contract_value | P11 | 0.7% | 60% | 6867 |
| award_or_notice_id | P11 | 0.7% | 60% | 6866 |
| buyer_logo_url | P08 | 74.6% | 100% | 6762 |
| vendor_phone | P08 | 59.6% | 85% | 6759 |
| buyer_phone | P13 | 58.5% | 95% | 6591 |
| vendor_emails | P08 | 50.8% | 75% | 6448 |
| invoice_reference_hint | P08 | 0.9% | 25% | 6411 |
| vendor_trading_name | P08 | 27.8% | 50% | 5904 |
| contract_or_agreement_number | P11 | 10.5% | 60% | 5739 |
| commodity_codes | P11 | 0.5% | 50% | 5732 |
| invoice_reference_hint | P11 | 11.2% | 60% | 5656 |
| buyer_bn_as_published | P08 | 13.8% | 35% | 5651 |
| buyer_ap_cycle_published | P08 | 0.0% | 20% | 5322 |
| buyer_phone | P11 | 29.4% | 75% | 5287 |
| buyer_logo_url | P13 | 66.0% | 95% | 5237 |
| ap_system_hint | P08 | 0.8% | 20% | 5118 |
| vendor_logo_url | P08 | 82.8% | 100% | 4589 |
| solicitation_or_tender_number | P11 | 0.7% | 40% | 4556 |
| buyer_address | P08 | 79.2% | 95% | 4212 |
| buyer_esignature_preference | P08 | 0.4% | 15% | 3904 |
| buyer_tax_exempt_status | P08 | 0.4% | 15% | 3900 |
| buyer_payment_method_preference | P08 | 0.4% | 15% | 3880 |
| buyer_legal_name_as_published | P11 | 31.9% | 65% | 3838 |
| buyer_ap_cycle_published | P13 | 0.0% | 20% | 3609 |

## 1. identifiers

### `invoice_reference_hint`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 105 | 89.5% | 89.5% | +0.8 | 50% | ✅ met |
| P01T | 334 | 88.9% | 88.9% | -0.6 | 50% | ✅ met |
| P01_GOLD | 625 | 92.2% | 94.4% | +0.0 | 95% | 🟡 3 pts to go |
| P02 | 474 | 72.4% | 73.8% | -1.4 | 95% | ❌ 23 pts to go |
| P03 | 257 | 81.7% | 84.8% | -0.3 | 95% | ❌ 13 pts to go |
| P04 | 3887 | 28.8% | 30.2% | -4.0 | 90% | ❌ 61 pts to go |
| P05 | 427 | 38.6% | 41.7% | +0.0 | 70% | ❌ 31 pts to go |
| P06M | 10630 | 92.5% | 92.5% | -0.1 | n/a | no target |
| P06T | 60045 | 79.4% | 79.4% | -0.9 | n/a | no target |
| P06 | 312 | 29.5% | 29.5% | -2.2 | 30% | 🟡 0 pts to go |
| P07 | 838 | 6.2% | 6.2% | -0.7 | 30% | ❌ 24 pts to go |
| P08 | 26652 | 0.9% | 0.9% | -0.2 | 25% | ❌ 24 pts to go |
| P09 | 303 | 99.0% | 99.7% | +0.0 | 100% | 🟡 1 pts to go |
| P10R | 98993 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P10 | 2735 | 2.6% | 2.6% | +0.0 | 25% | ❌ 22 pts to go |
| P11 | 11585 | 11.2% | 11.3% | -2.4 | 60% | ❌ 49 pts to go |
| P12 | 7 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P13 | 18053 | 0.2% | 0.2% | +0.0 | 0% by design | — leave (by design) |

### `po_number_as_published`

> ceiling: a purchase-order number exists only where the buyer publishes PO-level data (Montréal, Laval, Toronto open data so far) or the record itself carries one; most sources publish awards, not POs — the target cannot be reached from public data for most buyers

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 105 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P01T | 334 | 0.0% | 0.0% | +0.0 | 10% | 🟡 10 pts to go |
| P01_GOLD | 625 | 6.1% | 6.1% | +0.0 | 50% | ❌ 44 pts to go |
| P02 | 474 | 6.1% | 6.1% | -0.1 | 50% | ❌ 44 pts to go |
| P03 | 257 | 1.6% | 1.6% | +0.0 | 40% | ❌ 38 pts to go |
| P04 | 3887 | 0.5% | 0.5% | +0.0 | 30% | ❌ 30 pts to go |
| P05 | 427 | 0.2% | 0.2% | +0.0 | 20% | ❌ 20 pts to go |
| P06M | 10630 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06T | 60045 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06 | 312 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P07 | 838 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P08 | 26652 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P09 | 303 | 0.7% | 0.7% | +0.0 | 50% | ❌ 49 pts to go |
| P10R | 98993 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P10 | 2735 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P11 | 11585 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P12 | 7 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P13 | 18053 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `contract_or_agreement_number`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 105 | 82.9% | 82.9% | +1.5 | n/a | no target |
| P01T | 334 | 70.1% | 70.1% | -0.4 | 50% | ✅ met |
| P01_GOLD | 625 | 66.9% | 66.9% | +0.0 | 85% | ❌ 18 pts to go |
| P02 | 474 | 63.7% | 63.7% | -1.2 | 90% | ❌ 26 pts to go |
| P03 | 257 | 61.1% | 61.1% | -0.2 | 85% | ❌ 24 pts to go |
| P04 | 3887 | 26.4% | 26.4% | -3.7 | 85% | ❌ 59 pts to go |
| P05 | 427 | 29.0% | 29.0% | +0.0 | 60% | ❌ 31 pts to go |
| P06M | 10630 | 92.4% | 92.4% | +0.0 | n/a | no target |
| P06T | 60045 | 79.1% | 79.1% | -0.9 | n/a | no target |
| P06 | 312 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P07 | 838 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P08 | 26652 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P09 | 303 | 96.0% | 96.0% | +0.0 | 100% | 🟡 4 pts to go |
| P10R | 98993 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P10 | 2735 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P11 | 11585 | 10.5% | 10.5% | -2.2 | 60% | ❌ 50 pts to go |
| P12 | 7 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P13 | 18053 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `solicitation_or_tender_number`

> ceiling: SEAO's 'numero' is the organisation's own reference for the notice (SEAO data dictionary) and is reported here; sources that publish awards under a tender number only (bids&tenders, SaskTenders, BC) also carry it as the contract reference, labelled

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 105 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P01T | 334 | 0.0% | 0.0% | +0.0 | 30% | ❌ 30 pts to go |
| P01_GOLD | 625 | 50.7% | 50.7% | +0.1 | 80% | ❌ 29 pts to go |
| P02 | 474 | 55.9% | 55.9% | -1.1 | 60% | 🟡 4 pts to go |
| P03 | 257 | 51.4% | 51.4% | -0.2 | 80% | ❌ 29 pts to go |
| P04 | 3887 | 21.9% | 21.9% | -3.1 | 50% | ❌ 28 pts to go |
| P05 | 427 | 11.9% | 11.9% | +0.0 | 40% | ❌ 28 pts to go |
| P06M | 10630 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06T | 60045 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06 | 312 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P07 | 838 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P08 | 26652 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P09 | 303 | 83.5% | 83.5% | +0.0 | 50% | ✅ met |
| P10R | 98993 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P10 | 2735 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P11 | 11585 | 0.7% | 0.7% | -0.1 | 40% | ❌ 39 pts to go |
| P12 | 7 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P13 | 18053 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `award_or_notice_id`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 105 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P01T | 334 | 0.3% | 0.3% | +0.0 | n/a | no target |
| P01_GOLD | 625 | 60.5% | 60.5% | +0.1 | 85% | ❌ 24 pts to go |
| P02 | 474 | 55.3% | 55.3% | -1.0 | 90% | ❌ 35 pts to go |
| P03 | 257 | 59.9% | 59.9% | -0.3 | 85% | ❌ 25 pts to go |
| P04 | 3887 | 22.6% | 22.6% | -3.2 | 85% | ❌ 62 pts to go |
| P05 | 427 | 19.9% | 19.9% | +0.0 | 50% | ❌ 30 pts to go |
| P06M | 10630 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06T | 60045 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06 | 312 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P07 | 838 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P08 | 26652 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P09 | 303 | 97.0% | 97.0% | +0.0 | 100% | 🟡 3 pts to go |
| P10R | 98993 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P10 | 2735 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P11 | 11585 | 0.7% | 0.7% | -0.2 | 60% | ❌ 59 pts to go |
| P12 | 7 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P13 | 18053 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `buyer_vendor_id`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 105 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P01T | 334 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P01_GOLD | 625 | 13.0% | 13.0% | +0.1 | 60% | ❌ 47 pts to go |
| P02 | 474 | 5.9% | 5.9% | -0.1 | 50% | ❌ 44 pts to go |
| P03 | 257 | 8.6% | 8.6% | +0.0 | 50% | ❌ 41 pts to go |
| P04 | 3887 | 1.7% | 1.7% | -0.3 | 40% | ❌ 38 pts to go |
| P05 | 427 | 0.9% | 0.9% | +0.0 | 20% | ❌ 19 pts to go |
| P06M | 10630 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06T | 60045 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06 | 312 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P07 | 838 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P08 | 26652 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P09 | 303 | 2.3% | 2.3% | +0.0 | 50% | ❌ 48 pts to go |
| P10R | 98993 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P10 | 2735 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P11 | 11585 | 0.1% | 0.1% | +0.0 | n/a | no target |
| P12 | 7 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P13 | 18053 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `commodity_codes`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 105 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P01T | 334 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P01_GOLD | 625 | 34.9% | 34.9% | +0.1 | 80% | ❌ 45 pts to go |
| P02 | 474 | 51.1% | 51.1% | -0.9 | 90% | ❌ 39 pts to go |
| P03 | 257 | 33.5% | 33.5% | -0.1 | 80% | ❌ 46 pts to go |
| P04 | 3887 | 20.7% | 20.7% | -2.9 | 85% | ❌ 64 pts to go |
| P05 | 427 | 5.4% | 5.4% | +0.0 | 50% | ❌ 45 pts to go |
| P06M | 10630 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06T | 60045 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06 | 312 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P07 | 838 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P08 | 26652 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P09 | 303 | 75.9% | 75.9% | +0.0 | 95% | ❌ 19 pts to go |
| P10R | 98993 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P10 | 2735 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P11 | 11585 | 0.5% | 0.5% | -0.1 | 50% | ❌ 50 pts to go |
| P12 | 7 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P13 | 18053 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `buyer_org_codes`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 105 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P01T | 334 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P01_GOLD | 625 | 8.5% | 8.5% | +0.0 | 50% | ❌ 42 pts to go |
| P02 | 474 | 6.1% | 6.1% | -0.1 | 50% | ❌ 44 pts to go |
| P03 | 257 | 1.9% | 1.9% | -0.1 | 30% | ❌ 28 pts to go |
| P04 | 3887 | 0.4% | 0.4% | -0.1 | 30% | ❌ 30 pts to go |
| P05 | 427 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06M | 10630 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06T | 60045 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06 | 312 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P07 | 838 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P08 | 26652 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P09 | 303 | 0.3% | 0.3% | +0.0 | n/a | no target |
| P10R | 98993 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P10 | 2735 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P11 | 11585 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P12 | 7 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P13 | 18053 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `records_with_this_vendor`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 105 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P01T | 334 | 100.0% | 100.0% | +0.0 | 60% | ✅ met |
| P01_GOLD | 625 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P02 | 474 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P03 | 257 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P04 | 3887 | 100.0% | 100.0% | +0.0 | 95% | ✅ met |
| P05 | 427 | 100.0% | 100.0% | +0.0 | 70% | ✅ met |
| P06M | 10630 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P06T | 60045 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P06 | 312 | 100.0% | 100.0% | +0.0 | 50% | ✅ met |
| P07 | 838 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P08 | 26652 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P09 | 303 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P10R | 98993 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P10 | 2735 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P11 | 11585 | 100.0% | 100.0% | +0.0 | 70% | ✅ met |
| P12 | 7 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P13 | 18053 | 0.0% | 0.0% | +0.0 | n/a | no target |

## 2. vendor

### `vendor_bn9`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 105 | 12.4% | 12.4% | -2.0 | 70% | ❌ 58 pts to go |
| P01T | 334 | 32.6% | 32.6% | -1.1 | 60% | ❌ 27 pts to go |
| P01_GOLD | 625 | 72.6% | 72.6% | -0.4 | 90% | ❌ 17 pts to go |
| P02 | 474 | 53.0% | 53.0% | -2.1 | 85% | ❌ 32 pts to go |
| P03 | 257 | 68.1% | 68.1% | -1.8 | 90% | ❌ 22 pts to go |
| P04 | 3887 | 28.4% | 28.4% | -4.1 | 75% | ❌ 47 pts to go |
| P05 | 427 | 51.8% | 51.8% | +1.9 | 50% | ✅ met |
| P06M | 10630 | 2.0% | 2.0% | +0.2 | n/a | no target |
| P06T | 60045 | 21.2% | 21.2% | +3.9 | n/a | no target |
| P06 | 312 | 25.3% | 25.3% | +2.5 | 40% | ❌ 15 pts to go |
| P07 | 838 | 18.3% | 18.3% | +1.9 | 50% | ❌ 32 pts to go |
| P08 | 26652 | 14.3% | 14.3% | +3.4 | 50% | ❌ 36 pts to go |
| P09 | 303 | 57.4% | 57.4% | -0.4 | 80% | ❌ 23 pts to go |
| P10R | 98993 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P10 | 2735 | 30.7% | 30.7% | +2.0 | 40% | 🟡 9 pts to go |
| P11 | 11585 | 92.8% | 92.8% | +1.7 | 60% | ✅ met |
| P12 | 7 | 57.1% | 57.1% | -5.4 | 85% | ❌ 28 pts to go |
| P13 | 18053 | 91.0% | 91.0% | +0.0 | 0% by design | — leave (by design) |

### `vendor_registered_address`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 105 | 63.8% | 63.8% | -3.2 | n/a | no target |
| P01T | 334 | 38.3% | 38.3% | +0.3 | n/a | no target |
| P01_GOLD | 625 | 70.6% | 70.6% | +0.2 | 95% | ❌ 24 pts to go |
| P02 | 474 | 72.4% | 72.4% | -1.4 | 95% | ❌ 23 pts to go |
| P03 | 257 | 71.2% | 71.2% | -0.7 | 95% | ❌ 24 pts to go |
| P04 | 3887 | 40.2% | 40.2% | -5.4 | 95% | ❌ 55 pts to go |
| P05 | 427 | 53.4% | 53.4% | +0.0 | 70% | ❌ 17 pts to go |
| P06M | 10630 | 51.6% | 51.6% | -3.0 | n/a | no target |
| P06T | 60045 | 31.1% | 31.1% | +0.8 | n/a | no target |
| P06 | 312 | 22.8% | 22.8% | -2.0 | 80% | ❌ 57 pts to go |
| P07 | 838 | 16.2% | 16.2% | -1.8 | 70% | ❌ 54 pts to go |
| P08 | 26652 | 12.6% | 12.6% | -1.5 | 70% | ❌ 57 pts to go |
| P09 | 303 | 87.5% | 87.5% | +0.0 | 100% | ❌ 12 pts to go |
| P10R | 98993 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P10 | 2735 | 31.9% | 31.9% | -0.6 | 70% | ❌ 38 pts to go |
| P11 | 11585 | 93.4% | 93.4% | +1.2 | 75% | ✅ met |
| P12 | 7 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P13 | 18053 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `vendor_trading_name`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 105 | 16.2% | 16.2% | -0.3 | n/a | no target |
| P01T | 334 | 26.3% | 26.3% | +0.4 | n/a | no target |
| P01_GOLD | 625 | 48.0% | 48.0% | +0.1 | 60% | ❌ 12 pts to go |
| P02 | 474 | 54.9% | 54.9% | -0.4 | 60% | 🟡 5 pts to go |
| P03 | 257 | 54.5% | 54.5% | -0.6 | 60% | 🟡 6 pts to go |
| P04 | 3887 | 35.1% | 35.1% | -1.6 | 55% | ❌ 20 pts to go |
| P05 | 427 | 22.2% | 22.2% | +0.0 | 50% | ❌ 28 pts to go |
| P06M | 10630 | 4.1% | 4.1% | +0.5 | n/a | no target |
| P06T | 60045 | 28.3% | 28.3% | +1.3 | n/a | no target |
| P06 | 312 | 34.9% | 34.9% | -0.3 | n/a | no target |
| P07 | 838 | 33.3% | 33.3% | +0.1 | 55% | ❌ 22 pts to go |
| P08 | 26652 | 27.8% | 27.8% | +0.9 | 50% | ❌ 22 pts to go |
| P09 | 303 | 71.0% | 71.0% | +0.0 | 70% | ✅ met |
| P10R | 98993 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P10 | 2735 | 38.9% | 38.9% | -0.6 | 55% | ❌ 16 pts to go |
| P11 | 11585 | 93.4% | 93.4% | +1.4 | 50% | ✅ met |
| P12 | 7 | 100.0% | 100.0% | +12.5 | n/a | no target |
| P13 | 18053 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `vendor_phone`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 105 | 17.1% | 17.1% | +2.7 | n/a | no target |
| P01T | 334 | 56.6% | 56.6% | +0.3 | n/a | no target |
| P01_GOLD | 625 | 49.4% | 49.4% | +1.5 | 70% | ❌ 21 pts to go |
| P02 | 474 | 54.0% | 54.0% | +0.0 | 70% | ❌ 16 pts to go |
| P03 | 257 | 49.8% | 49.8% | +0.2 | 70% | ❌ 20 pts to go |
| P04 | 3887 | 48.6% | 48.6% | +1.5 | 65% | ❌ 16 pts to go |
| P05 | 427 | 31.4% | 31.4% | +0.7 | 60% | ❌ 29 pts to go |
| P06M | 10630 | 4.3% | 4.3% | +0.8 | n/a | no target |
| P06T | 60045 | 64.0% | 64.0% | +0.2 | n/a | no target |
| P06 | 312 | 59.9% | 59.9% | +2.3 | 40% | ✅ met |
| P07 | 838 | 58.6% | 58.6% | +1.6 | 85% | ❌ 26 pts to go |
| P08 | 26652 | 59.6% | 59.6% | +2.7 | 85% | ❌ 25 pts to go |
| P09 | 303 | 53.5% | 53.5% | +0.0 | 85% | ❌ 32 pts to go |
| P10R | 98993 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P10 | 2735 | 60.7% | 60.7% | -0.3 | 85% | ❌ 24 pts to go |
| P11 | 11585 | 5.5% | 5.5% | -0.9 | 75% | ❌ 70 pts to go |
| P12 | 7 | 28.6% | 28.6% | +3.6 | n/a | no target |
| P13 | 18053 | 100.0% | 100.0% | +0.0 | 60% | ✅ met |

### `vendor_website`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 105 | 19.0% | 19.0% | -0.6 | n/a | no target |
| P01T | 334 | 96.4% | 96.4% | +0.0 | n/a | no target |
| P01_GOLD | 625 | 89.4% | 89.4% | +0.1 | 90% | 🟡 1 pts to go |
| P02 | 474 | 89.5% | 89.5% | +0.3 | 90% | 🟡 0 pts to go |
| P03 | 257 | 91.1% | 91.1% | +0.1 | 90% | ✅ met |
| P04 | 3887 | 91.4% | 91.4% | +1.2 | 85% | ✅ met |
| P05 | 427 | 52.2% | 52.2% | +0.0 | 70% | ❌ 18 pts to go |
| P06M | 10630 | 6.1% | 6.1% | -0.1 | n/a | no target |
| P06T | 60045 | 92.0% | 92.0% | +0.0 | n/a | no target |
| P06 | 312 | 98.4% | 98.4% | +0.1 | 50% | ✅ met |
| P07 | 838 | 99.2% | 99.2% | +0.1 | 100% | 🟡 1 pts to go |
| P08 | 26652 | 99.5% | 99.5% | +0.1 | 100% | 🟡 0 pts to go |
| P09 | 303 | 80.2% | 80.2% | +0.0 | 100% | ❌ 20 pts to go |
| P10R | 98993 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P10 | 2735 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P11 | 11585 | 99.7% | 99.7% | +0.0 | 100% | 🟡 0 pts to go |
| P12 | 7 | 42.9% | 42.9% | +5.4 | n/a | no target |
| P13 | 18053 | 100.0% | 100.0% | +0.0 | n/a | no target |

### `vendor_emails`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 105 | 14.3% | 14.3% | -0.1 | n/a | no target |
| P01T | 334 | 48.8% | 48.8% | -0.3 | n/a | no target |
| P01_GOLD | 625 | 45.6% | 45.6% | +0.4 | 70% | ❌ 24 pts to go |
| P02 | 474 | 49.6% | 49.6% | +0.1 | 75% | ❌ 25 pts to go |
| P03 | 257 | 44.7% | 44.7% | +0.2 | 75% | ❌ 30 pts to go |
| P04 | 3887 | 39.3% | 39.3% | +1.9 | 70% | ❌ 31 pts to go |
| P05 | 427 | 25.5% | 25.5% | +0.0 | 55% | ❌ 30 pts to go |
| P06M | 10630 | 3.3% | 3.3% | +0.0 | n/a | no target |
| P06T | 60045 | 39.8% | 39.8% | +0.2 | n/a | no target |
| P06 | 312 | 43.9% | 43.9% | +1.1 | n/a | no target |
| P07 | 838 | 46.4% | 46.4% | +0.5 | 70% | ❌ 24 pts to go |
| P08 | 26652 | 50.8% | 50.8% | +0.9 | 75% | ❌ 24 pts to go |
| P09 | 303 | 49.8% | 49.8% | +0.0 | 85% | ❌ 35 pts to go |
| P10R | 98993 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P10 | 2735 | 43.5% | 43.5% | +0.0 | 80% | ❌ 36 pts to go |
| P11 | 11585 | 4.2% | 4.2% | -0.8 | 70% | ❌ 66 pts to go |
| P12 | 7 | 28.6% | 28.6% | +3.6 | n/a | no target |
| P13 | 18053 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `vendor_logo_url`

> ceiling: needs the vendor's website first; sites that block automated readers (robots.txt / 403) are never read

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 105 | 17.1% | 17.1% | +3.7 | n/a | no target |
| P01T | 334 | 90.7% | 90.7% | +0.9 | n/a | no target |
| P01_GOLD | 625 | 78.6% | 78.6% | +1.1 | 90% | ❌ 11 pts to go |
| P02 | 474 | 77.6% | 77.6% | +0.0 | 90% | ❌ 12 pts to go |
| P03 | 257 | 82.9% | 82.9% | -0.3 | 90% | 🟡 7 pts to go |
| P04 | 3887 | 76.5% | 76.5% | +0.9 | 85% | 🟡 8 pts to go |
| P05 | 427 | 49.2% | 49.2% | +0.5 | 75% | ❌ 26 pts to go |
| P06M | 10630 | 5.3% | 5.3% | +1.2 | n/a | no target |
| P06T | 60045 | 87.2% | 87.2% | +4.0 | n/a | no target |
| P06 | 312 | 82.7% | 82.7% | +3.4 | n/a | no target |
| P07 | 838 | 85.0% | 85.0% | +3.4 | 100% | ❌ 15 pts to go |
| P08 | 26652 | 82.8% | 82.8% | +3.9 | 100% | ❌ 17 pts to go |
| P09 | 303 | 61.4% | 61.4% | +0.0 | n/a | no target |
| P10R | 98993 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P10 | 2735 | 84.5% | 84.5% | +0.3 | 100% | ❌ 16 pts to go |
| P11 | 11585 | 90.9% | 90.9% | +2.5 | n/a | no target |
| P12 | 7 | 42.9% | 42.9% | +5.4 | n/a | no target |
| P13 | 18053 | 83.3% | 83.3% | +0.1 | n/a | no target |

### `vendor_neq`

> ceiling: only Québec-registered vendors have an NEQ; the share of QC vendors is reported next to the rate

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 105 | 51.4% | 51.4% | -2.2 | n/a | no target · QC vendors: 48 rows, 100.0% filled |
| P01T | 334 | 18.3% | 18.3% | +0.5 | n/a | no target · QC vendors: 17 rows, 100.0% filled |
| P01_GOLD | 625 | 43.7% | 43.7% | +0.1 | 95% | ❌ 51 pts to go · QC vendors: 53 rows, 98.1% filled |
| P02 | 474 | 54.0% | 54.0% | -1.1 | 95% | ❌ 41 pts to go · QC vendors: 110 rows, 100.0% filled |
| P03 | 257 | 45.9% | 45.9% | -0.6 | 95% | ❌ 49 pts to go · QC vendors: 18 rows, 100.0% filled |
| P04 | 3887 | 28.0% | 28.0% | -3.9 | 95% | ❌ 67 pts to go · QC vendors: 498 rows, 98.8% filled |
| P05 | 427 | 14.8% | 14.8% | +0.0 | n/a | no target · QC vendors: 35 rows, 94.3% filled |
| P06M | 10630 | 50.4% | 50.4% | -2.9 | n/a | no target · QC vendors: 5114 rows, 100.0% filled |
| P06T | 60045 | 18.5% | 18.5% | +1.0 | n/a | no target · QC vendors: 3295 rows, 100.0% filled |
| P06 | 312 | 7.7% | 7.7% | -0.6 | n/a | no target · QC vendors: 13 rows, 100.0% filled |
| P07 | 838 | 6.2% | 6.2% | -0.6 | n/a | no target · QC vendors: 36 rows, 97.2% filled |
| P08 | 26652 | 6.0% | 6.0% | -0.5 | n/a | no target · QC vendors: 1283 rows, 99.7% filled |
| P09 | 303 | 78.2% | 78.2% | +0.0 | 95% | ❌ 17 pts to go · QC vendors: 111 rows, 100.0% filled |
| P10R | 98993 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P10 | 2735 | 17.2% | 17.2% | -0.4 | n/a | no target · QC vendors: 310 rows, 94.8% filled |
| P11 | 11585 | 84.6% | 84.6% | +3.1 | n/a | no target · QC vendors: 111 rows, 99.1% filled |
| P12 | 7 | 71.4% | 71.4% | +8.9 | n/a | no target · QC vendors: 1 rows, 100.0% filled |
| P13 | 18053 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `vendor_years_in_business`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 105 | 61.9% | 61.9% | -3.0 | n/a | no target · vendors with a registry record: 65 rows, 100.0% filled |
| P01T | 334 | 38.6% | 38.6% | +0.3 | n/a | no target · vendors with a registry record: 129 rows, 100.0% filled |
| P01_GOLD | 625 | 79.5% | 79.5% | +0.1 | 100% | ❌ 20 pts to go · vendors with a registry record: 497 rows, 100.0% filled |
| P02 | 474 | 75.9% | 75.9% | -1.5 | 100% | ❌ 24 pts to go · vendors with a registry record: 360 rows, 100.0% filled |
| P03 | 257 | 80.5% | 80.5% | -0.7 | 100% | ❌ 20 pts to go · vendors with a registry record: 207 rows, 100.0% filled |
| P04 | 3887 | 40.5% | 40.5% | -5.6 | 100% | ❌ 60 pts to go · vendors with a registry record: 1576 rows, 100.0% filled |
| P05 | 427 | 58.3% | 58.3% | +0.0 | n/a | no target · vendors with a registry record: 249 rows, 100.0% filled |
| P06M | 10630 | 51.3% | 51.3% | -3.0 | n/a | no target · vendors with a registry record: 5455 rows, 100.0% filled |
| P06T | 60045 | 31.2% | 31.2% | +0.8 | n/a | no target · vendors with a registry record: 18713 rows, 100.0% filled |
| P06 | 312 | 23.4% | 23.4% | -2.1 | n/a | no target · vendors with a registry record: 73 rows, 100.0% filled |
| P07 | 838 | 16.6% | 16.6% | -1.8 | n/a | no target · vendors with a registry record: 139 rows, 100.0% filled |
| P08 | 26652 | 12.8% | 12.8% | -1.5 | n/a | no target · vendors with a registry record: 3405 rows, 100.0% filled |
| P09 | 303 | 91.1% | 91.1% | +0.0 | n/a | no target · vendors with a registry record: 276 rows, 100.0% filled |
| P10R | 98993 | 100.0% | 100.0% | +0.0 | n/a | no target · vendors with a registry record: 98993 rows, 100.0% filled |
| P10 | 2735 | 32.5% | 32.5% | -0.7 | n/a | no target · vendors with a registry record: 890 rows, 100.0% filled |
| P11 | 11585 | 93.6% | 93.6% | +1.3 | n/a | no target · vendors with a registry record: 10838 rows, 100.0% filled |
| P12 | 7 | 100.0% | 100.0% | +0.0 | n/a | no target · vendors with a registry record: 7 rows, 100.0% filled |
| P13 | 18053 | 0.0% | 0.0% | +0.0 | n/a | no target |

## 3. buyer

### `buyer_legal_name_as_published`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 105 | 89.5% | 89.5% | +0.8 | 90% | 🟡 0 pts to go |
| P01T | 334 | 68.3% | 68.3% | +12.0 | 90% | ❌ 22 pts to go |
| P01_GOLD | 625 | 85.1% | 85.1% | +1.4 | 95% | 🟡 10 pts to go |
| P02 | 474 | 85.0% | 85.0% | -0.2 | 95% | 🟡 10 pts to go |
| P03 | 257 | 81.3% | 81.3% | +2.4 | 85% | 🟡 4 pts to go |
| P04 | 3887 | 52.9% | 52.9% | -3.5 | 90% | ❌ 37 pts to go |
| P05 | 427 | 73.8% | 73.8% | +6.1 | 75% | 🟡 1 pts to go |
| P06M | 10630 | 89.0% | 89.0% | +1.9 | n/a | no target |
| P06T | 60045 | 41.5% | 41.5% | +12.5 | n/a | no target |
| P06 | 312 | 58.7% | 58.7% | +1.8 | 80% | ❌ 21 pts to go |
| P07 | 838 | 47.7% | 47.9% | +1.5 | 80% | ❌ 32 pts to go |
| P08 | 26652 | 40.8% | 40.8% | +2.3 | 75% | ❌ 34 pts to go |
| P09 | 303 | 77.2% | 77.2% | +0.0 | 95% | ❌ 18 pts to go |
| P10R | 98993 | 33.9% | 33.9% | +8.9 | n/a | no target |
| P10 | 2735 | 41.9% | 41.9% | +2.9 | 70% | ❌ 28 pts to go |
| P11 | 11585 | 31.9% | 31.9% | +22.3 | 65% | ❌ 33 pts to go |
| P12 | 7 | 71.4% | 71.4% | -3.6 | 80% | 🟡 9 pts to go |
| P13 | 18053 | 44.9% | 44.9% | +5.7 | 60% | ❌ 15 pts to go |

### `buyer_bn_as_published`

> ceiling: a buyer's BN is public only where the buyer prints it or a public dataset carries it (CRA charities, federal grants & contributions recipients, business registries for corporations); municipalities rarely publish theirs

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 105 | 23.8% | 23.8% | +4.2 | 50% | ❌ 26 pts to go |
| P01T | 334 | 17.4% | 17.4% | +4.1 | n/a | no target |
| P01_GOLD | 625 | 19.8% | 19.8% | -0.8 | 40% | ❌ 20 pts to go |
| P02 | 474 | 19.4% | 19.4% | +0.5 | 40% | ❌ 21 pts to go |
| P03 | 257 | 23.0% | 23.0% | +0.7 | 40% | ❌ 17 pts to go |
| P04 | 3887 | 15.4% | 15.4% | -0.9 | 40% | ❌ 25 pts to go |
| P05 | 427 | 19.9% | 19.9% | +0.2 | 25% | 🟡 5 pts to go |
| P06M | 10630 | 13.4% | 13.4% | +4.6 | n/a | no target |
| P06T | 60045 | 10.6% | 10.6% | +3.1 | n/a | no target |
| P06 | 312 | 15.4% | 15.4% | +2.6 | 35% | ❌ 20 pts to go |
| P07 | 838 | 14.3% | 14.3% | +2.8 | 35% | ❌ 21 pts to go |
| P08 | 26652 | 13.8% | 13.8% | +3.4 | 35% | ❌ 21 pts to go |
| P09 | 303 | 16.5% | 16.5% | +0.3 | n/a | no target |
| P10R | 98993 | 9.1% | 9.1% | +2.0 | n/a | no target |
| P10 | 2735 | 11.2% | 11.2% | +4.7 | 30% | ❌ 19 pts to go |
| P11 | 11585 | 2.1% | 2.1% | +0.9 | n/a | no target |
| P12 | 7 | 14.3% | 14.3% | +1.8 | n/a | no target |
| P13 | 18053 | 21.0% | 21.0% | +0.0 | 30% | 🟡 9 pts to go |

### `buyer_address`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 105 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P01T | 334 | 91.9% | 91.9% | +0.0 | 100% | 🟡 8 pts to go |
| P01_GOLD | 625 | 90.1% | 90.1% | +0.6 | 100% | 🟡 10 pts to go |
| P02 | 474 | 95.1% | 95.1% | -0.2 | 100% | 🟡 5 pts to go |
| P03 | 257 | 89.1% | 89.1% | -0.4 | 100% | ❌ 11 pts to go |
| P04 | 3887 | 74.5% | 74.5% | -1.4 | 100% | ❌ 26 pts to go |
| P05 | 427 | 87.8% | 87.8% | +0.4 | 100% | ❌ 12 pts to go |
| P06M | 10630 | 99.0% | 99.0% | +0.2 | n/a | no target |
| P06T | 60045 | 78.9% | 78.9% | +1.5 | n/a | no target |
| P06 | 312 | 81.4% | 81.4% | +0.4 | 95% | ❌ 14 pts to go |
| P07 | 838 | 83.1% | 83.1% | -0.5 | 95% | ❌ 12 pts to go |
| P08 | 26652 | 79.2% | 79.2% | -1.0 | 95% | ❌ 16 pts to go |
| P09 | 303 | 95.7% | 95.7% | +0.0 | 100% | 🟡 4 pts to go |
| P10R | 98993 | 60.6% | 60.6% | +1.8 | n/a | no target |
| P10 | 2735 | 65.7% | 65.7% | +0.6 | 95% | ❌ 29 pts to go |
| P11 | 11585 | 90.0% | 90.0% | +2.8 | 80% | ✅ met |
| P12 | 7 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P13 | 18053 | 77.1% | 77.1% | +1.9 | 95% | ❌ 18 pts to go |

### `buyer_phone`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 105 | 85.7% | 85.7% | +0.1 | n/a | no target |
| P01T | 334 | 75.4% | 75.4% | +11.8 | n/a | no target |
| P01_GOLD | 625 | 69.6% | 69.6% | +0.1 | 90% | ❌ 20 pts to go |
| P02 | 474 | 74.7% | 74.7% | -1.0 | 95% | ❌ 20 pts to go |
| P03 | 257 | 73.2% | 73.2% | -0.6 | 95% | ❌ 22 pts to go |
| P04 | 3887 | 60.5% | 60.5% | -6.1 | 95% | ❌ 34 pts to go |
| P05 | 427 | 70.7% | 70.7% | +0.2 | 90% | ❌ 19 pts to go |
| P06M | 10630 | 87.6% | 87.6% | +1.2 | n/a | no target |
| P06T | 60045 | 68.8% | 68.8% | +20.9 | n/a | no target |
| P06 | 312 | 62.8% | 62.8% | -0.3 | 95% | ❌ 32 pts to go |
| P07 | 838 | 54.1% | 54.1% | -0.9 | 90% | ❌ 36 pts to go |
| P08 | 26652 | 56.5% | 56.5% | -2.3 | 95% | ❌ 38 pts to go |
| P09 | 303 | 86.1% | 86.1% | +0.0 | 100% | ❌ 14 pts to go |
| P10R | 98993 | 57.7% | 57.7% | +12.6 | n/a | no target |
| P10 | 2735 | 56.5% | 56.5% | +0.0 | 95% | ❌ 38 pts to go |
| P11 | 11585 | 29.4% | 29.4% | +18.2 | 75% | ❌ 46 pts to go |
| P12 | 7 | 71.4% | 71.4% | -3.6 | n/a | no target |
| P13 | 18053 | 58.5% | 58.5% | +10.9 | 95% | ❌ 36 pts to go |

### `buyer_logo_url`

> ceiling: sites that block automated readers (robots.txt / 403) are never read; an og:image that looks like a photo is labelled

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 105 | 78.1% | 78.1% | +7.0 | n/a | no target |
| P01T | 334 | 91.0% | 91.0% | +16.9 | 95% | 🟡 4 pts to go |
| P01_GOLD | 625 | 80.8% | 80.8% | +0.1 | 90% | 🟡 9 pts to go |
| P02 | 474 | 84.8% | 84.8% | -1.0 | 95% | ❌ 10 pts to go |
| P03 | 257 | 83.7% | 83.7% | -0.3 | 95% | ❌ 11 pts to go |
| P04 | 3887 | 76.1% | 76.1% | -7.2 | 90% | ❌ 14 pts to go |
| P05 | 427 | 89.0% | 89.0% | +0.5 | 95% | 🟡 6 pts to go |
| P06M | 10630 | 82.4% | 82.4% | +15.7 | n/a | no target |
| P06T | 60045 | 90.5% | 90.5% | +29.0 | n/a | no target |
| P06 | 312 | 81.1% | 81.1% | -1.0 | 100% | ❌ 19 pts to go |
| P07 | 838 | 75.7% | 75.7% | -1.5 | 100% | ❌ 24 pts to go |
| P08 | 26652 | 74.6% | 74.6% | -2.5 | 100% | ❌ 25 pts to go |
| P09 | 303 | 68.6% | 68.6% | +0.0 | n/a | no target |
| P10R | 98993 | 80.5% | 80.5% | +20.5 | n/a | no target |
| P10 | 2735 | 87.2% | 87.2% | +0.4 | 100% | ❌ 13 pts to go |
| P11 | 11585 | 71.2% | 71.2% | +52.4 | 80% | 🟡 9 pts to go |
| P12 | 7 | 71.4% | 71.4% | -3.6 | n/a | no target |
| P13 | 18053 | 66.0% | 66.0% | +15.0 | 95% | ❌ 29 pts to go |

## 4. AP

### `ap_contact_name_as_published`

> ceiling: owner 2026-11-08: the AP contact person the organisation itself names on its AP / finance page is allowed (name + role phrase, quoted); mailboxes stay organisational; many bodies publish no AP person

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 105 | 3.8% | 3.8% | -0.3 | n/a | no target |
| P01T | 334 | 8.4% | 8.4% | +0.0 | n/a | no target |
| P01_GOLD | 625 | 14.2% | 14.2% | +0.0 | 25% | ❌ 11 pts to go |
| P02 | 474 | 24.1% | 24.1% | -0.4 | 40% | ❌ 16 pts to go |
| P03 | 257 | 8.9% | 8.9% | -0.1 | 20% | ❌ 11 pts to go |
| P04 | 3887 | 3.1% | 3.1% | -0.5 | 20% | ❌ 17 pts to go |
| P05 | 427 | 3.3% | 3.3% | +0.0 | 15% | ❌ 12 pts to go |
| P06M | 10630 | 0.3% | 0.3% | +0.0 | n/a | no target |
| P06T | 60045 | 0.4% | 0.4% | +0.0 | n/a | no target |
| P06 | 312 | 5.4% | 5.4% | -0.8 | n/a | no target |
| P07 | 838 | 7.2% | 7.2% | -0.1 | n/a | no target |
| P08 | 26652 | 0.2% | 0.2% | -0.1 | n/a | no target |
| P09 | 303 | 7.6% | 7.6% | +0.0 | n/a | no target |
| P10R | 98993 | 0.2% | 0.2% | +0.0 | n/a | no target |
| P10 | 2735 | 1.0% | 1.0% | +0.0 | n/a | no target |
| P11 | 11585 | 0.1% | 0.1% | -0.1 | n/a | no target |
| P12 | 7 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P13 | 18053 | 0.4% | 0.4% | +0.0 | n/a | no target |

### `ap_phone`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 105 | 24.8% | 24.8% | -2.0 | n/a | no target |
| P01T | 334 | 24.0% | 24.0% | -0.1 | 70% | ❌ 46 pts to go |
| P01_GOLD | 625 | 43.4% | 43.4% | +0.1 | 80% | ❌ 37 pts to go |
| P02 | 474 | 55.7% | 55.7% | -1.1 | 90% | ❌ 34 pts to go |
| P03 | 257 | 19.1% | 19.1% | +0.0 | 60% | ❌ 41 pts to go |
| P04 | 3887 | 20.8% | 20.8% | -2.9 | 85% | ❌ 64 pts to go |
| P05 | 427 | 11.9% | 11.9% | +0.0 | 50% | ❌ 38 pts to go |
| P06M | 10630 | 0.4% | 0.4% | +0.0 | n/a | no target |
| P06T | 60045 | 0.6% | 0.6% | +0.0 | n/a | no target |
| P06 | 312 | 15.1% | 15.1% | -1.1 | n/a | no target |
| P07 | 838 | 11.6% | 11.6% | -1.4 | n/a | no target |
| P08 | 26652 | 0.4% | 0.4% | -0.1 | n/a | no target |
| P09 | 303 | 77.6% | 77.6% | +0.0 | 95% | ❌ 17 pts to go |
| P10R | 98993 | 0.2% | 0.2% | +0.0 | n/a | no target |
| P10 | 2735 | 1.7% | 1.7% | +0.0 | n/a | no target |
| P11 | 11585 | 3.0% | 3.0% | -0.6 | n/a | no target |
| P12 | 7 | 14.3% | 14.3% | -10.7 | n/a | no target |
| P13 | 18053 | 0.7% | 0.7% | +0.0 | n/a | no target |

### `invoice_mailing_address`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 105 | 6.7% | 6.7% | -0.5 | n/a | no target |
| P01T | 334 | 12.0% | 12.0% | +0.0 | n/a | no target |
| P01_GOLD | 625 | 33.9% | 33.9% | +0.0 | 70% | ❌ 36 pts to go |
| P02 | 474 | 38.2% | 38.2% | -0.7 | 75% | ❌ 37 pts to go |
| P03 | 257 | 19.1% | 19.1% | +0.0 | 55% | ❌ 36 pts to go |
| P04 | 3887 | 20.7% | 20.7% | -2.9 | 75% | ❌ 54 pts to go |
| P05 | 427 | 10.8% | 10.8% | +0.0 | 50% | ❌ 39 pts to go |
| P06M | 10630 | 0.2% | 0.2% | +0.0 | n/a | no target |
| P06T | 60045 | 0.4% | 0.4% | +0.0 | n/a | no target |
| P06 | 312 | 7.7% | 7.7% | -0.6 | n/a | no target |
| P07 | 838 | 5.7% | 5.7% | -0.7 | n/a | no target |
| P08 | 26652 | 0.2% | 0.2% | +0.0 | n/a | no target |
| P09 | 303 | 75.2% | 75.2% | +0.0 | 95% | ❌ 20 pts to go |
| P10R | 98993 | 0.2% | 0.2% | +0.0 | n/a | no target |
| P10 | 2735 | 1.0% | 1.0% | +0.0 | n/a | no target |
| P11 | 11585 | 2.9% | 2.9% | -0.7 | n/a | no target |
| P12 | 7 | 14.3% | 14.3% | +1.8 | n/a | no target |
| P13 | 18053 | 0.4% | 0.4% | +0.0 | n/a | no target |

### `invoicing_requirements`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 105 | 7.6% | 7.6% | +1.4 | n/a | no target |
| P01T | 334 | 9.3% | 9.3% | +0.0 | n/a | no target |
| P01_GOLD | 625 | 57.9% | 58.1% | -0.1 | 80% | ❌ 22 pts to go |
| P02 | 474 | 44.9% | 45.1% | -0.9 | 75% | ❌ 30 pts to go |
| P03 | 257 | 37.7% | 37.7% | -0.2 | 70% | ❌ 32 pts to go |
| P04 | 3887 | 20.3% | 20.7% | -2.8 | 70% | ❌ 50 pts to go |
| P05 | 427 | 14.3% | 14.3% | +0.0 | 50% | ❌ 36 pts to go |
| P06M | 10630 | 0.4% | 0.4% | +0.0 | n/a | no target |
| P06T | 60045 | 0.3% | 0.3% | +0.0 | n/a | no target |
| P06 | 312 | 12.5% | 12.5% | -0.9 | n/a | no target |
| P07 | 838 | 1.8% | 1.8% | -0.2 | n/a | no target |
| P08 | 26652 | 0.3% | 0.3% | -0.1 | n/a | no target |
| P09 | 303 | 45.9% | 46.2% | +0.0 | 80% | ❌ 34 pts to go |
| P10R | 98993 | 0.1% | 0.1% | +0.0 | n/a | no target |
| P10 | 2735 | 1.2% | 1.2% | +0.0 | n/a | no target |
| P11 | 11585 | 0.9% | 0.9% | -0.2 | n/a | no target |
| P12 | 7 | 42.9% | 42.9% | +5.4 | n/a | no target |
| P13 | 18053 | 0.3% | 0.3% | +0.0 | n/a | no target |

### `payment_terms_as_published`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 105 | 12.4% | 12.4% | +1.1 | n/a | no target |
| P01T | 334 | 21.9% | 21.9% | -0.1 | 60% | ❌ 38 pts to go |
| P01_GOLD | 625 | 63.5% | 63.5% | -0.1 | 70% | 🟡 6 pts to go |
| P02 | 474 | 38.2% | 38.2% | -0.7 | 50% | ❌ 12 pts to go |
| P03 | 257 | 49.8% | 49.8% | -0.2 | 55% | 🟡 5 pts to go |
| P04 | 3887 | 11.7% | 11.7% | -1.6 | 40% | ❌ 28 pts to go |
| P05 | 427 | 17.3% | 17.3% | +0.0 | 40% | ❌ 23 pts to go |
| P06M | 10630 | 0.7% | 0.7% | +0.0 | n/a | no target |
| P06T | 60045 | 2.4% | 2.4% | +0.0 | n/a | no target |
| P06 | 312 | 18.3% | 18.3% | -1.4 | n/a | no target |
| P07 | 838 | 6.0% | 6.0% | -0.7 | n/a | no target |
| P08 | 26652 | 2.3% | 2.3% | -0.3 | n/a | no target |
| P09 | 303 | 5.9% | 5.9% | +0.0 | n/a | no target |
| P10R | 98993 | 0.2% | 0.2% | +0.0 | n/a | no target |
| P10 | 2735 | 4.4% | 4.4% | -0.1 | n/a | no target |
| P11 | 11585 | 3.9% | 3.9% | -0.4 | n/a | no target |
| P12 | 7 | 0.0% | 0.0% | -12.5 | n/a | no target |
| P13 | 18053 | 0.2% | 0.2% | +0.0 | n/a | no target |

### `po_required_as_published`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 105 | 17.1% | 17.1% | +0.6 | n/a | no target |
| P01T | 334 | 25.1% | 25.1% | -0.2 | 65% | ❌ 40 pts to go |
| P01_GOLD | 625 | 69.0% | 69.0% | +0.0 | 70% | 🟡 1 pts to go |
| P02 | 474 | 23.4% | 23.4% | -0.5 | 50% | ❌ 27 pts to go |
| P03 | 257 | 52.1% | 52.1% | -0.2 | 60% | 🟡 8 pts to go |
| P04 | 3887 | 5.0% | 5.0% | -0.8 | 40% | ❌ 35 pts to go |
| P05 | 427 | 19.7% | 19.7% | +0.0 | 45% | ❌ 25 pts to go |
| P06M | 10630 | 0.3% | 0.3% | +0.0 | n/a | no target |
| P06T | 60045 | 0.6% | 0.6% | +0.0 | n/a | no target |
| P06 | 312 | 29.5% | 29.5% | -2.2 | n/a | no target |
| P07 | 838 | 6.2% | 6.2% | -0.7 | n/a | no target |
| P08 | 26652 | 0.9% | 0.9% | -0.2 | n/a | no target |
| P09 | 303 | 9.9% | 9.9% | +0.0 | n/a | no target |
| P10R | 98993 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P10 | 2735 | 2.6% | 2.6% | +0.0 | n/a | no target |
| P11 | 11585 | 0.9% | 0.9% | -0.1 | n/a | no target |
| P12 | 7 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P13 | 18053 | 0.2% | 0.2% | +0.0 | n/a | no target |

### `invoice_portal_url`

> ceiling: only portals the buyer names on its own pages; informational tax-authority links are not portals

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 105 | 5.7% | 5.7% | -0.5 | n/a | no target |
| P01T | 334 | 14.7% | 14.7% | +0.2 | n/a | no target |
| P01_GOLD | 625 | 49.8% | 49.8% | +0.0 | 50% | 🟡 0 pts to go |
| P02 | 474 | 36.7% | 36.7% | -0.7 | n/a | no target |
| P03 | 257 | 52.5% | 52.5% | -0.6 | 60% | 🟡 8 pts to go |
| P04 | 3887 | 11.3% | 11.3% | -1.6 | n/a | no target |
| P05 | 427 | 15.2% | 15.2% | +0.0 | n/a | no target |
| P06M | 10630 | 0.3% | 0.3% | +0.0 | n/a | no target |
| P06T | 60045 | 0.5% | 0.5% | +0.0 | n/a | no target |
| P06 | 312 | 20.2% | 20.2% | -1.5 | n/a | no target |
| P07 | 838 | 6.4% | 6.4% | -0.8 | n/a | no target |
| P08 | 26652 | 0.5% | 0.5% | +0.0 | n/a | no target |
| P09 | 303 | 18.2% | 18.2% | +0.0 | n/a | no target |
| P10R | 98993 | 0.1% | 0.1% | +0.0 | n/a | no target |
| P10 | 2735 | 2.3% | 2.3% | +0.0 | n/a | no target |
| P11 | 11585 | 0.7% | 0.7% | -0.1 | n/a | no target |
| P12 | 7 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P13 | 18053 | 0.4% | 0.4% | +0.0 | n/a | no target |

### `buyer_payment_method_preference`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 105 | 12.4% | 12.4% | +1.1 | 15% | 🟡 3 pts to go |
| P01T | 334 | 12.0% | 12.0% | +0.9 | 15% | 🟡 3 pts to go |
| P01_GOLD | 625 | 35.2% | 35.2% | -0.1 | 40% | 🟡 5 pts to go |
| P02 | 474 | 12.2% | 12.4% | -0.3 | 25% | ❌ 13 pts to go |
| P03 | 257 | 17.9% | 17.9% | -0.1 | 25% | 🟡 7 pts to go |
| P04 | 3887 | 2.5% | 2.5% | -0.3 | 15% | ❌ 12 pts to go |
| P05 | 427 | 6.8% | 6.8% | +0.0 | 15% | 🟡 8 pts to go |
| P06M | 10630 | 0.6% | 0.6% | +0.0 | 15% | ❌ 14 pts to go |
| P06T | 60045 | 0.6% | 0.6% | +0.2 | 15% | ❌ 14 pts to go |
| P06 | 312 | 8.7% | 8.7% | -0.6 | 15% | 🟡 6 pts to go |
| P07 | 838 | 3.1% | 3.1% | -0.1 | 15% | ❌ 12 pts to go |
| P08 | 26652 | 0.4% | 0.4% | +0.0 | 15% | ❌ 15 pts to go |
| P09 | 303 | 1.0% | 1.0% | +0.0 | 15% | ❌ 14 pts to go |
| P10R | 98993 | 0.6% | 0.6% | +0.2 | 15% | ❌ 14 pts to go |
| P10 | 2735 | 1.1% | 1.1% | +0.1 | 15% | ❌ 14 pts to go |
| P11 | 11585 | 0.4% | 0.4% | +0.2 | 15% | ❌ 15 pts to go |
| P12 | 7 | 14.3% | 14.3% | +1.8 | 15% | 🟡 1 pts to go |
| P13 | 18053 | 0.4% | 0.4% | +0.0 | 15% | ❌ 15 pts to go |

### `buyer_tax_exempt_status`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 105 | 5.7% | 5.7% | -0.5 | 15% | 🟡 9 pts to go |
| P01T | 334 | 12.0% | 12.0% | +0.0 | 25% | ❌ 13 pts to go |
| P01_GOLD | 625 | 29.1% | 29.1% | -0.1 | 25% | ✅ met |
| P02 | 474 | 24.9% | 24.9% | -0.5 | 15% | ✅ met |
| P03 | 257 | 21.4% | 21.4% | -0.1 | 15% | ✅ met |
| P04 | 3887 | 3.6% | 3.6% | -0.5 | 15% | ❌ 11 pts to go |
| P05 | 427 | 10.8% | 10.8% | +0.0 | 15% | 🟡 4 pts to go |
| P06M | 10630 | 0.2% | 0.2% | +0.0 | 15% | ❌ 15 pts to go |
| P06T | 60045 | 0.3% | 0.3% | +0.0 | 15% | ❌ 15 pts to go |
| P06 | 312 | 7.1% | 7.1% | -0.5 | 15% | 🟡 8 pts to go |
| P07 | 838 | 2.7% | 2.7% | -0.4 | 15% | ❌ 12 pts to go |
| P08 | 26652 | 0.4% | 0.4% | +0.0 | 15% | ❌ 15 pts to go |
| P09 | 303 | 1.0% | 1.0% | +0.0 | 15% | ❌ 14 pts to go |
| P10R | 98993 | 0.0% | 0.0% | +0.0 | 15% | ❌ 15 pts to go |
| P10 | 2735 | 1.6% | 1.6% | +0.0 | 15% | ❌ 13 pts to go |
| P11 | 11585 | 0.6% | 0.6% | +0.1 | 15% | ❌ 14 pts to go |
| P12 | 7 | 28.6% | 28.6% | +3.6 | 15% | ✅ met |
| P13 | 18053 | 0.0% | 0.0% | +0.0 | 15% | ❌ 15 pts to go |

### `buyer_ap_cycle_published`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 105 | 0.0% | 0.0% | +0.0 | 20% | ❌ 20 pts to go |
| P01T | 334 | 4.2% | 4.2% | +0.3 | 20% | ❌ 16 pts to go |
| P01_GOLD | 625 | 4.3% | 4.3% | +0.0 | 20% | ❌ 16 pts to go |
| P02 | 474 | 1.3% | 1.3% | +0.0 | 20% | ❌ 19 pts to go |
| P03 | 257 | 1.6% | 1.6% | +0.0 | 20% | ❌ 18 pts to go |
| P04 | 3887 | 0.5% | 0.5% | -0.1 | 20% | ❌ 20 pts to go |
| P05 | 427 | 1.2% | 1.2% | +0.0 | 20% | ❌ 19 pts to go |
| P06M | 10630 | 0.0% | 0.0% | +0.0 | 20% | ❌ 20 pts to go |
| P06T | 60045 | 0.0% | 0.0% | +0.0 | 20% | ❌ 20 pts to go |
| P06 | 312 | 1.3% | 1.3% | -0.1 | 20% | ❌ 19 pts to go |
| P07 | 838 | 0.4% | 0.4% | +0.0 | 20% | ❌ 20 pts to go |
| P08 | 26652 | 0.0% | 0.0% | +0.0 | 20% | ❌ 20 pts to go |
| P09 | 303 | 0.0% | 0.0% | +0.0 | 20% | ❌ 20 pts to go |
| P10R | 98993 | 0.0% | 0.0% | +0.0 | 20% | ❌ 20 pts to go |
| P10 | 2735 | 0.3% | 0.3% | +0.0 | 20% | ❌ 20 pts to go |
| P11 | 11585 | 0.0% | 0.0% | +0.0 | 20% | ❌ 20 pts to go |
| P12 | 7 | 0.0% | 0.0% | +0.0 | 20% | ❌ 20 pts to go |
| P13 | 18053 | 0.0% | 0.0% | +0.0 | 20% | ❌ 20 pts to go |

### `buyer_esignature_preference`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 105 | 1.0% | 1.0% | +0.0 | 15% | ❌ 14 pts to go |
| P01T | 334 | 2.4% | 2.4% | +0.0 | 15% | ❌ 13 pts to go |
| P01_GOLD | 625 | 10.4% | 10.4% | -0.1 | 15% | 🟡 5 pts to go |
| P02 | 474 | 11.8% | 11.8% | -0.2 | 15% | 🟡 3 pts to go |
| P03 | 257 | 20.6% | 20.6% | -0.1 | 15% | ✅ met |
| P04 | 3887 | 2.1% | 2.1% | -0.3 | 15% | ❌ 13 pts to go |
| P05 | 427 | 3.0% | 3.0% | +0.0 | 15% | ❌ 12 pts to go |
| P06M | 10630 | 0.1% | 0.1% | -0.1 | 15% | ❌ 15 pts to go |
| P06T | 60045 | 0.2% | 0.2% | +0.0 | 15% | ❌ 15 pts to go |
| P06 | 312 | 4.8% | 4.8% | -0.4 | 15% | ❌ 10 pts to go |
| P07 | 838 | 1.6% | 1.6% | -0.1 | 15% | ❌ 13 pts to go |
| P08 | 26652 | 0.4% | 0.4% | +0.0 | 15% | ❌ 15 pts to go |
| P09 | 303 | 0.7% | 0.7% | +0.0 | 15% | ❌ 14 pts to go |
| P10R | 98993 | 0.0% | 0.0% | +0.0 | 15% | ❌ 15 pts to go |
| P10 | 2735 | 0.9% | 0.9% | +0.0 | 15% | ❌ 14 pts to go |
| P11 | 11585 | 0.2% | 0.2% | -0.1 | 15% | ❌ 15 pts to go |
| P12 | 7 | 0.0% | 0.0% | +0.0 | 15% | ❌ 15 pts to go |
| P13 | 18053 | 0.1% | 0.1% | +0.0 | 15% | ❌ 15 pts to go |

### `ap_system_hint`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 105 | 7.6% | 7.6% | +0.4 | 20% | ❌ 12 pts to go |
| P01T | 334 | 15.3% | 15.3% | +0.2 | 40% | ❌ 25 pts to go |
| P01_GOLD | 625 | 45.8% | 45.8% | +0.0 | 40% | ✅ met |
| P02 | 474 | 42.0% | 42.0% | -0.8 | 20% | ✅ met |
| P03 | 257 | 48.6% | 48.6% | -0.2 | 35% | ✅ met |
| P04 | 3887 | 13.6% | 13.6% | -1.8 | 20% | 🟡 6 pts to go |
| P05 | 427 | 14.8% | 14.8% | +0.0 | 20% | 🟡 5 pts to go |
| P06M | 10630 | 0.5% | 0.5% | +0.0 | 20% | ❌ 20 pts to go |
| P06T | 60045 | 0.7% | 0.7% | +0.0 | 20% | ❌ 19 pts to go |
| P06 | 312 | 20.5% | 20.5% | -1.6 | 20% | ✅ met |
| P07 | 838 | 6.4% | 6.4% | -0.7 | 20% | ❌ 14 pts to go |
| P08 | 26652 | 0.8% | 0.8% | -0.1 | 20% | ❌ 19 pts to go |
| P09 | 303 | 18.2% | 18.2% | +0.0 | 20% | 🟡 2 pts to go |
| P10R | 98993 | 0.2% | 0.2% | +0.0 | 20% | ❌ 20 pts to go |
| P10 | 2735 | 3.4% | 3.4% | +0.0 | 20% | ❌ 17 pts to go |
| P11 | 11585 | 0.8% | 0.8% | -0.2 | 20% | ❌ 19 pts to go |
| P12 | 7 | 0.0% | 0.0% | +0.0 | 20% | ❌ 20 pts to go |
| P13 | 18053 | 0.6% | 0.6% | +0.1 | 20% | ❌ 19 pts to go |

## 5. contract

### `contract_value`

> ceiling: rows proven by a lobbying filing, a news release, an auditor appointment, a customer story or a vendor's client list have no contract value by nature (≈17 % of P01 Gold); bids&tenders awards now carry the awarded bidder's submitted price when no award value was published

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 105 | 41.9% | 41.9% | -2.4 | n/a | no target |
| P01T | 334 | 0.3% | 0.3% | +0.0 | n/a | no target |
| P01_GOLD | 625 | 69.4% | 69.4% | -0.1 | 95% | ❌ 26 pts to go |
| P02 | 474 | 61.8% | 61.8% | -1.2 | 95% | ❌ 33 pts to go |
| P03 | 257 | 54.5% | 54.5% | -0.2 | 90% | ❌ 36 pts to go |
| P04 | 3887 | 23.8% | 23.8% | -3.3 | 85% | ❌ 61 pts to go |
| P05 | 427 | 36.5% | 36.5% | +0.0 | 75% | ❌ 38 pts to go |
| P06M | 10630 | 46.3% | 46.3% | -3.8 | n/a | no target |
| P06T | 60045 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06 | 312 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P07 | 838 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P08 | 26652 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P09 | 303 | 89.4% | 89.4% | +0.0 | 100% | ❌ 11 pts to go |
| P10R | 98993 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P10 | 2735 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P11 | 11585 | 0.7% | 0.7% | -0.2 | 60% | ❌ 59 pts to go |
| P12 | 7 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P13 | 18053 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `currency`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 105 | 41.9% | 41.9% | -2.4 | n/a | no target |
| P01T | 334 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P01_GOLD | 625 | 72.8% | 72.8% | +0.0 | 100% | ❌ 27 pts to go |
| P02 | 474 | 65.2% | 65.2% | -1.3 | 100% | ❌ 35 pts to go |
| P03 | 257 | 60.3% | 60.3% | -0.2 | n/a | no target |
| P04 | 3887 | 24.4% | 24.4% | -3.4 | 95% | ❌ 71 pts to go |
| P05 | 427 | 33.0% | 33.0% | +0.0 | 80% | ❌ 47 pts to go |
| P06M | 10630 | 46.3% | 46.3% | -3.8 | n/a | no target |
| P06T | 60045 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06 | 312 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P07 | 838 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P08 | 26652 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P09 | 303 | 92.7% | 92.7% | +0.0 | 100% | 🟡 7 pts to go |
| P10R | 98993 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P10 | 2735 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P11 | 11585 | 0.8% | 0.8% | -0.2 | n/a | no target |
| P12 | 7 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P13 | 18053 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `start_date`

> ceiling: most award notices publish an award date, not a start date; start_date carries the signature date when the source gives one, labelled

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 105 | 80.0% | 80.0% | +1.6 | n/a | no target |
| P01T | 334 | 0.3% | 0.3% | +0.0 | n/a | no target |
| P01_GOLD | 625 | 51.7% | 51.7% | +0.1 | 85% | ❌ 33 pts to go |
| P02 | 474 | 56.5% | 56.5% | -1.1 | 90% | ❌ 34 pts to go |
| P03 | 257 | 44.0% | 44.0% | -0.1 | 85% | ❌ 41 pts to go |
| P04 | 3887 | 26.7% | 26.7% | -3.7 | 90% | ❌ 63 pts to go |
| P05 | 427 | 32.8% | 32.8% | +0.0 | 75% | ❌ 42 pts to go |
| P06M | 10630 | 90.7% | 90.7% | +0.3 | n/a | no target |
| P06T | 60045 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06 | 312 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P07 | 838 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P08 | 26652 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P09 | 303 | 85.1% | 85.1% | +0.0 | 95% | 🟡 10 pts to go |
| P10R | 98993 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P10 | 2735 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P11 | 11585 | 0.7% | 0.7% | -0.1 | n/a | no target |
| P12 | 7 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P13 | 18053 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `end_date`

> ceiling: an inferred end (award date + published duration) is labelled as such; sources without a duration leave end_date empty — the honest ceiling. P09 is BY DEFINITION the rows whose end date is not published (older SEAO contracts with no closing notice): its end_date / duration targets cannot be met without inventing a date

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 105 | 80.0% | 80.0% | +0.6 | n/a | no target |
| P01T | 334 | 0.3% | 0.3% | +0.0 | n/a | no target |
| P01_GOLD | 625 | 51.8% | 51.8% | +0.0 | 85% | ❌ 33 pts to go |
| P02 | 474 | 51.7% | 51.7% | -1.0 | 90% | ❌ 38 pts to go |
| P03 | 257 | 45.1% | 45.1% | -0.2 | 85% | ❌ 40 pts to go |
| P04 | 3887 | 22.8% | 22.8% | -3.2 | 90% | ❌ 67 pts to go |
| P05 | 427 | 42.9% | 42.9% | +0.0 | 75% | ❌ 32 pts to go |
| P06M | 10630 | 82.1% | 82.1% | -1.6 | n/a | no target |
| P06T | 60045 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06 | 312 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P07 | 838 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P08 | 26652 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P09 | 303 | 0.3% | 0.3% | +0.0 | 95% | ❌ 95 pts to go |
| P10R | 98993 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P10 | 2735 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P11 | 11585 | 0.6% | 0.6% | -0.1 | n/a | no target |
| P12 | 7 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P13 | 18053 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `contract_title`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 105 | 86.7% | 86.7% | +1.1 | n/a | no target |
| P01T | 334 | 91.9% | 91.9% | -0.3 | n/a | no target |
| P01_GOLD | 625 | 85.4% | 85.4% | -0.1 | 100% | ❌ 15 pts to go |
| P02 | 474 | 74.3% | 74.3% | -1.4 | 100% | ❌ 26 pts to go |
| P03 | 257 | 91.4% | 91.4% | -0.8 | n/a | no target |
| P04 | 3887 | 45.1% | 45.1% | -6.4 | 95% | ❌ 50 pts to go |
| P05 | 427 | 77.8% | 77.8% | +0.0 | 95% | ❌ 17 pts to go |
| P06M | 10630 | 98.5% | 98.5% | +0.2 | n/a | no target |
| P06T | 60045 | 82.7% | 82.7% | -1.0 | n/a | no target |
| P06 | 312 | 24.4% | 24.4% | -1.8 | n/a | no target |
| P07 | 838 | 16.9% | 16.9% | -2.2 | n/a | no target |
| P08 | 26652 | 9.5% | 9.5% | -1.5 | n/a | no target |
| P09 | 303 | 98.7% | 98.7% | +0.0 | 100% | 🟡 1 pts to go |
| P10R | 98993 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P10 | 2735 | 70.3% | 70.3% | -1.4 | n/a | no target |
| P11 | 11585 | 13.2% | 13.2% | -2.9 | n/a | no target |
| P12 | 7 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P13 | 18053 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `contract_description`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 105 | 86.7% | 86.7% | +1.1 | n/a | no target |
| P01T | 334 | 91.9% | 91.9% | -0.3 | n/a | no target |
| P01_GOLD | 625 | 88.6% | 88.6% | -0.1 | 100% | ❌ 11 pts to go |
| P02 | 474 | 75.3% | 75.5% | -1.5 | 100% | ❌ 25 pts to go |
| P03 | 257 | 92.2% | 92.2% | -0.8 | n/a | no target |
| P04 | 3887 | 48.3% | 48.3% | -6.8 | 95% | ❌ 47 pts to go |
| P05 | 427 | 90.2% | 90.2% | +0.0 | 70% | ✅ met |
| P06M | 10630 | 98.5% | 98.5% | +0.2 | n/a | no target |
| P06T | 60045 | 82.7% | 82.7% | -1.0 | n/a | no target |
| P06 | 312 | 24.4% | 24.4% | -1.8 | n/a | no target |
| P07 | 838 | 16.9% | 16.9% | -2.2 | n/a | no target |
| P08 | 26652 | 9.5% | 9.5% | -1.5 | n/a | no target |
| P09 | 303 | 98.7% | 98.7% | +0.0 | 100% | 🟡 1 pts to go |
| P10R | 98993 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P10 | 2735 | 70.3% | 70.3% | -1.4 | n/a | no target |
| P11 | 11585 | 13.2% | 13.2% | -2.9 | n/a | no target |
| P12 | 7 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P13 | 18053 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `number_of_bids`

> ceiling: published by some portals only (bids&tenders submission lists, Biddingo bidder lists); federal proactive disclosure does not publish bid counts

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 105 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P01T | 334 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P01_GOLD | 625 | 16.8% | 16.8% | +0.0 | 60% | ❌ 43 pts to go · rows from a source that publishes bids: 363 rows, 28.9% filled |
| P02 | 474 | 11.0% | 11.0% | -0.2 | n/a | no target · rows from a source that publishes bids: 290 rows, 17.9% filled |
| P03 | 257 | 13.2% | 13.2% | -0.1 | n/a | no target · rows from a source that publishes bids: 139 rows, 24.5% filled |
| P04 | 3887 | 1.4% | 1.4% | -0.2 | n/a | no target · rows from a source that publishes bids: 872 rows, 6.3% filled |
| P05 | 427 | 3.0% | 3.0% | +0.0 | n/a | no target · rows from a source that publishes bids: 53 rows, 24.5% filled |
| P06M | 10630 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06T | 60045 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06 | 312 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P07 | 838 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P08 | 26652 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P09 | 303 | 3.0% | 3.0% | +0.0 | n/a | no target · rows from a source that publishes bids: 290 rows, 3.1% filled |
| P10R | 98993 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P10 | 2735 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P11 | 11585 | 0.1% | 0.1% | +0.0 | n/a | no target · rows from a source that publishes bids: 87 rows, 12.6% filled |
| P12 | 7 | 0.0% | 0.0% | +0.0 | n/a | no target · rows from a source that publishes bids: 7 rows, 0.0% filled |
| P13 | 18053 | 0.0% | 0.0% | +0.0 | n/a | no target |

## 6. history

### `average_contract_duration_days`

> ceiling: needs two dates (or a published term) on the buyer's records; P09 rows (end date unpublished by definition) and buyers whose sources publish award dates only have no honest duration

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 105 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P01T | 334 | 0.3% | 98.5% | +0.0 | n/a | no target |
| P01_GOLD | 625 | 53.3% | 82.4% | +0.1 | 90% | ❌ 37 pts to go |
| P02 | 474 | 51.5% | 87.8% | -1.0 | 90% | ❌ 38 pts to go |
| P03 | 257 | 45.5% | 80.2% | -0.2 | 90% | ❌ 44 pts to go |
| P04 | 3887 | 18.3% | 94.2% | -2.6 | 90% | ❌ 72 pts to go |
| P05 | 427 | 0.0% | 82.9% | +0.0 | 90% | ❌ 90 pts to go |
| P06M | 10630 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P06T | 60045 | 0.0% | 99.9% | +0.0 | n/a | no target |
| P06 | 312 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P07 | 838 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P08 | 26652 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P09 | 303 | 2.3% | 4.0% | +0.0 | 90% | ❌ 88 pts to go |
| P10R | 98993 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P10 | 2735 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P11 | 11585 | 0.5% | 99.6% | -0.1 | n/a | no target |
| P12 | 7 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P13 | 18053 | 0.0% | 100.0% | +0.0 | n/a | no target |

### `commodity_distribution_top3`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 105 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P01T | 334 | 0.6% | 98.8% | +0.0 | n/a | no target |
| P01_GOLD | 625 | 25.9% | 55.0% | +0.0 | 90% | ❌ 64 pts to go |
| P02 | 474 | 50.6% | 86.9% | -1.0 | n/a | no target |
| P03 | 257 | 24.9% | 59.5% | -0.1 | n/a | no target |
| P04 | 3887 | 20.1% | 95.9% | -2.8 | n/a | no target |
| P05 | 427 | 0.5% | 83.4% | +0.0 | n/a | no target |
| P06M | 10630 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P06T | 60045 | 0.1% | 99.9% | +0.0 | n/a | no target |
| P06 | 312 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P07 | 838 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P08 | 26652 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P09 | 303 | 41.9% | 43.6% | +0.0 | n/a | no target |
| P10R | 98993 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P10 | 2735 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P11 | 11585 | 0.5% | 99.6% | -0.1 | n/a | no target |
| P12 | 7 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P13 | 18053 | 0.0% | 100.0% | +0.0 | n/a | no target |

### `year_over_year_spend_trend`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 105 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P01T | 334 | 1.5% | 99.7% | +0.0 | n/a | no target |
| P01_GOLD | 625 | 51.8% | 81.0% | +0.0 | 95% | ❌ 43 pts to go |
| P02 | 474 | 55.5% | 91.8% | -1.1 | n/a | no target |
| P03 | 257 | 47.9% | 82.5% | -0.1 | n/a | no target |
| P04 | 3887 | 20.3% | 96.1% | -2.8 | n/a | no target |
| P05 | 427 | 4.7% | 87.6% | +0.0 | n/a | no target |
| P06M | 10630 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P06T | 60045 | 0.1% | 100.0% | +0.0 | n/a | no target |
| P06 | 312 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P07 | 838 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P08 | 26652 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P09 | 303 | 64.0% | 65.7% | +0.0 | n/a | no target |
| P10R | 98993 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P10 | 2735 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P11 | 11585 | 0.5% | 99.6% | -0.1 | n/a | no target |
| P12 | 7 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P13 | 18053 | 0.0% | 100.0% | +0.0 | n/a | no target |

## 7. mail security

### `mta_sts`

> ceiling: DNS-only check; 'no record' counts as checked

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 105 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P01T | 334 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P01_GOLD | 625 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P02 | 474 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P03 | 257 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P04 | 3887 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P05 | 427 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P06M | 10630 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P06T | 60045 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P06 | 312 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P07 | 838 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P08 | 26652 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P09 | 303 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P10R | 98993 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P10 | 2735 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P11 | 11585 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P12 | 7 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P13 | 18053 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |

### `tls_rpt`

> ceiling: DNS-only check; 'no record' counts as checked

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 105 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P01T | 334 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P01_GOLD | 625 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P02 | 474 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P03 | 257 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P04 | 3887 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P05 | 427 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P06M | 10630 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P06T | 60045 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P06 | 312 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P07 | 838 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P08 | 26652 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P09 | 303 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P10R | 98993 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P10 | 2735 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P11 | 11585 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P12 | 7 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P13 | 18053 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |

### `bimi`

> ceiling: DNS-only check; 'no record' counts as checked

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 105 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P01T | 334 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P01_GOLD | 625 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P02 | 474 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P03 | 257 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P04 | 3887 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P05 | 427 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P06M | 10630 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P06T | 60045 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P06 | 312 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P07 | 838 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P08 | 26652 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P09 | 303 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P10R | 98993 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P10 | 2735 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P11 | 11585 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P12 | 7 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P13 | 18053 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |

