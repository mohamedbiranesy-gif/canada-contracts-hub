# Coverage vs the downstream team's targets — 2026-11-11

Benchmarks (field × package with a numeric target): **95 of 446 met** (21.3%); 68 within 10 points; 283 further away.
A cell counts as filled only when it carries a value: blank, `not_published`, `not_found_yet` and label-only cells ("no identifier published …", "no dataset record …", "0 in the contract dataset …") do not count; the DNS checks count when checked. `any` = share of non-blank cells incl. such labels. Δ = change since the previous build in `coord/results/coverage_history.csv`.
Rows per package: P01M 126, P01T 398, P01_GOLD 625, P02 471, P03 257, P04 3823, P05 422, P06M 13201, P06T 75065, P06 295, P07 793, P08 25303, P09 295, P10R 99941, P10 2633, P11 17455, P12 7, P13 17623

## Invoice-grade readiness (the row as an invoice header: bill-to, submit-to, references, terms, tax, vendor identity, follow-up)

| package | rows | all 11 elements | ≥ 9 of 11 | median elements | most-missing element |
|---|---|---|---|---|---|
| P01M | 126 | 0.0% | 14.3% | 8 | vendor GST/HST number (115 rows) |
| P01T | 398 | 0.5% | 20.1% | 7 | payment terms (326 rows) |
| P01_GOLD | 625 | 24.8% | 70.9% | 10 | payment terms (214 rows) |
| P02 | 471 | 7.2% | 54.4% | 9 | PO rule (360 rows) |
| P03 | 257 | 14.8% | 58.4% | 9 | PO rule (123 rows) |
| P04 | 3823 | 1.2% | 16.1% | 6 | PO rule (3632 rows) |
| P05 | 422 | 1.2% | 17.5% | 7 | payment terms (347 rows) |
| P06M | 13201 | 0.0% | 1.3% | 7 | PO rule (13168 rows) |
| P06T | 75065 | 0.0% | 3.7% | 7 | PO rule (74722 rows) |
| P06 | 295 | 0.0% | 8.5% | 6 | reference to quote (PO / contract / vendor id) (295 rows) |
| P07 | 793 | 0.0% | 2.0% | 6 | reference to quote (PO / contract / vendor id) (793 rows) |
| P08 | 25303 | 0.0% | 0.3% | 6 | reference to quote (PO / contract / vendor id) (25303 rows) |
| P09 | 295 | 1.0% | 45.1% | 8 | payment terms (276 rows) |
| P10R | 99941 | 0.0% | 23.4% | 8 | PO rule (99905 rows) |
| P10 | 2633 | 0.0% | 1.1% | 5 | reference to quote (PO / contract / vendor id) (2633 rows) |
| P11 | 17455 | 0.0% | 1.8% | 7 | PO rule (17350 rows) |
| P12 | 7 | 0.0% | 28.6% | 8 | PO rule (7 rows) |
| P13 | 17623 | 0.0% | 0.2% | 7 | reference to quote (PO / contract / vendor id) (17623 rows) |

## AP grade (how stringently the row's accounts-payable data meets what an invoice needs; A = invoicing mailbox referee-confirmed on the buyer's own domain with MX, legal name, address, PO rule and terms all published, no penalties)

| package | rows | A | B | C | D | E | median ap_score |
|---|---|---|---|---|---|---|---|
| P01M | 126 | 9 | 12 | 105 | 0 | 0 | 71 |
| P01T | 398 | 30 | 62 | 306 | 0 | 0 | 68 |
| P01_GOLD | 625 | 229 | 197 | 199 | 0 | 0 | 82 |
| P02 | 471 | 0 | 194 | 277 | 0 | 0 | 66 |
| P03 | 257 | 0 | 0 | 247 | 10 | 0 | 57 |
| P04 | 3823 | 0 | 0 | 3275 | 548 | 0 | 46 |
| P05 | 422 | 16 | 30 | 364 | 12 | 0 | 51 |
| P06M | 13201 | 0 | 4 | 13137 | 60 | 0 | 46 |
| P06T | 75065 | 0 | 40 | 62543 | 12482 | 0 | 40 |
| P06 | 295 | 20 | 49 | 226 | 0 | 0 | 71 |
| P07 | 793 | 0 | 28 | 744 | 21 | 0 | 54 |
| P08 | 25303 | 0 | 0 | 22030 | 3273 | 0 | 43 |
| P09 | 295 | 3 | 12 | 278 | 2 | 0 | 53 |
| P10R | 99941 | 2 | 13 | 71564 | 28362 | 0 | 38 |
| P10 | 2633 | 2 | 15 | 2022 | 594 | 0 | 43 |
| P11 | 17455 | 7 | 14 | 39 | 0 | 17395 | 31 |
| P12 | 7 | 0 | 0 | 7 | 0 | 0 | 54 |
| P13 | 17623 | 0 | 16 | 14643 | 2964 | 0 | 43 |

### AP payability (confirmed channel + bill-to legal name and address + the buyer's reference rule + tax treatment known)

| package | rows | payable today | % | most common gap |
|---|---|---|---|---|
| P01M | 126 | 103 | 81.7% | the buyer's PO / reference rule (13) |
| P01T | 398 | 218 | 54.8% | bill-to legal name and address (130) |
| P01_GOLD | 625 | 472 | 75.5% | bill-to legal name and address (97) |
| P02 | 471 | 314 | 66.7% | the buyer's PO / reference rule (92) |
| P03 | 257 | 0 | 0.0% | a confirmed invoicing / AP or finance channel (257) |
| P04 | 3823 | 0 | 0.0% | a confirmed invoicing / AP or finance channel (3823) |
| P05 | 422 | 48 | 11.4% | a confirmed invoicing / AP or finance channel (335) |
| P06M | 13201 | 131 | 1.0% | a confirmed invoicing / AP or finance channel (13024) |
| P06T | 75065 | 480 | 0.6% | a confirmed invoicing / AP or finance channel (73965) |
| P06 | 295 | 43 | 14.6% | the buyer's PO / reference rule (141) |
| P07 | 793 | 10 | 1.3% | the buyer's PO / reference rule (316) |
| P08 | 25303 | 0 | 0.0% | a confirmed invoicing / AP or finance channel (25303) |
| P09 | 295 | 41 | 13.9% | a confirmed invoicing / AP or finance channel (245) |
| P10R | 99941 | 572 | 0.6% | a confirmed invoicing / AP or finance channel (98779) |
| P10 | 2633 | 5 | 0.2% | a confirmed invoicing / AP or finance channel (2537) |
| P11 | 17455 | 13 | 0.1% | a confirmed invoicing / AP or finance channel (17395) |
| P12 | 7 | 3 | 42.9% | a confirmed invoicing / AP or finance channel (4) |
| P13 | 17623 | 7 | 0.0% | a confirmed invoicing / AP or finance channel (17282) |

### Pay on sight (an invoice generated from the row would clear AP: confirmed invoicing / AP or finance channel, bill-to legal name + address, vendor legal name + GST/HST number + remit-to address, tax treatment and currency known — published or labelled-derived; the buyer's reference rule is reported separately)

| package | rows | pay on sight | % | + reference rule not published | routed (general inbox only) | most common gap |
|---|---|---|---|---|---|---|
| P01M | 126 | 5 | 4.0% | 5 | 0 | the vendor's GST/HST number (BN9) (115) |
| P01T | 398 | 71 | 17.8% | 26 | 0 | the vendor's GST/HST number (BN9) (229) |
| P01_GOLD | 625 | 396 | 63.4% | 12 | 0 | the vendor's GST/HST number (BN9) (156) |
| P02 | 471 | 211 | 44.8% | 23 | 0 | the vendor's GST/HST number (BN9) (207) |
| P03 | 257 | 16 | 6.2% | 0 | 132 | an invoicing / AP or finance mailbox (only a purchasing / general inbo (88) |
| P04 | 3823 | 42 | 1.1% | 8 | 811 | an invoicing / AP or finance mailbox (only a purchasing / general inbo (2906) |
| P05 | 422 | 20 | 4.7% | 7 | 110 | an invoicing / AP or finance mailbox (only a purchasing / general inbo (218) |
| P06M | 13201 | 1 | 0.0% | 10 | 149 | an invoicing / AP or finance mailbox (only a purchasing / general inbo (12854) |
| P06T | 75065 | 112 | 0.1% | 105 | 15282 | an invoicing / AP or finance mailbox (only a purchasing / general inbo (58525) |
| P06 | 295 | 16 | 5.4% | 35 | 0 | the vendor's GST/HST number (BN9) (174) |
| P07 | 793 | 5 | 0.6% | 75 | 29 | the vendor's GST/HST number (BN9) (429) |
| P08 | 25303 | 1 | 0.0% | 8 | 2969 | an invoicing / AP or finance mailbox (only a purchasing / general inbo (22271) |
| P09 | 295 | 38 | 12.9% | 1 | 120 | an invoicing / AP or finance mailbox (only a purchasing / general inbo (116) |
| P10R | 99941 | 884 | 0.9% | 0 | 54782 | an invoicing / AP or finance mailbox (only a purchasing / general inbo (43938) |
| P10 | 2633 | 4 | 0.2% | 21 | 389 | an invoicing / AP or finance mailbox (only a purchasing / general inbo (2118) |
| P11 | 17455 | 11 | 0.1% | 13 | 0 | a confirmed invoicing / AP or finance channel (17361) |
| P12 | 7 | 1 | 14.3% | 0 | 2 | the vendor's GST/HST number (BN9) (2) |
| P13 | 17623 | 9 | 0.1% | 249 | 10542 | an invoicing / AP or finance mailbox (only a purchasing / general inbo (6701) |
| **all** | 258733 | 1843 | 0.7% | 598 | 85317 | |

### What still blocks grade A (rows per missing element; a row counts under every element it lacks)

| package | rows not A | referee confirmation of the mailbox | an invoicing / AP mailbox (not finance / procurement / general) | a mailbox on the buyer's own domain | MX record for the mailbox domain | published bill-to legal name | invoice / billing address | published PO rule | published payment terms | clear the penalty |
|---|---|---|---|---|---|---|---|---|---|---|
| P01M | 117 | 0 | 0 | 0 | 62 | 7 | 0 | 108 | 112 | 1 |
| P01T | 368 | 0 | 0 | 0 | 177 | 116 | 36 | 313 | 328 | 27 |
| P01_GOLD | 396 | 0 | 0 | 0 | 11 | 78 | 31 | 194 | 228 | 57 |
| P02 | 471 | 0 | 471 | 0 | 47 | 53 | 18 | 360 | 290 | 22 |
| P03 | 257 | 0 | 257 | 0 | 15 | 40 | 23 | 123 | 129 | 25 |
| P04 | 3823 | 0 | 3823 | 0 | 1798 | 1338 | 904 | 3632 | 3374 | 131 |
| P05 | 406 | 0 | 355 | 0 | 74 | 84 | 43 | 338 | 349 | 50 |
| P06M | 13201 | 0 | 13201 | 0 | 8349 | 1072 | 111 | 13168 | 13132 | 77 |
| P06T | 75065 | 0 | 75065 | 0 | 59269 | 40754 | 16752 | 74722 | 73620 | 428 |
| P06 | 275 | 0 | 0 | 0 | 117 | 71 | 49 | 208 | 238 | 4 |
| P07 | 793 | 0 | 793 | 0 | 469 | 307 | 127 | 744 | 745 | 13 |
| P08 | 25303 | 0 | 25303 | 0 | 18551 | 11398 | 4952 | 25069 | 24762 | 224 |
| P09 | 292 | 0 | 271 | 0 | 9 | 67 | 2 | 266 | 278 | 44 |
| P10R | 99939 | 0 | 99765 | 0 | 78072 | 60175 | 38707 | 99905 | 99763 | 25 |
| P10 | 2631 | 0 | 2594 | 0 | 1262 | 1247 | 883 | 2566 | 2517 | 115 |
| P11 | 17448 | 17395 | 17331 | 0 | 15965 | 8517 | 1004 | 17350 | 16900 | 38 |
| P12 | 7 | 0 | 6 | 0 | 0 | 2 | 0 | 7 | 7 | 0 |
| P13 | 17623 | 0 | 17523 | 0 | 8855 | 8425 | 3928 | 17588 | 17581 | 19 |

## Where the work is (largest gaps in rows still needed)

| field | package | now | target | rows needed |
|---|---|---|---|---|
| buyer_ap_cycle_published | P10R | 0.0% | 20% | 19960 |
| ap_system_hint | P10R | 0.2% | 20% | 19786 |
| buyer_ap_cycle_published | P06T | 0.0% | 20% | 14987 |
| buyer_tax_exempt_status | P10R | 0.0% | 15% | 14964 |
| buyer_esignature_preference | P10R | 0.0% | 15% | 14944 |
| ap_system_hint | P06T | 0.6% | 20% | 14552 |
| buyer_payment_method_preference | P10R | 0.7% | 15% | 14323 |
| vendor_registered_address | P08 | 13.7% | 70% | 14259 |
| vendor_phone | P11 | 4.4% | 75% | 12319 |
| vendor_emails | P11 | 3.4% | 70% | 11618 |
| buyer_esignature_preference | P06T | 0.2% | 15% | 11120 |
| buyer_tax_exempt_status | P06T | 0.3% | 15% | 11070 |
| buyer_payment_method_preference | P06T | 0.6% | 15% | 10783 |
| contract_value | P11 | 0.5% | 60% | 10388 |
| award_or_notice_id | P11 | 0.5% | 60% | 10387 |
| contract_or_agreement_number | P11 | 7.8% | 60% | 9105 |
| invoice_reference_hint | P11 | 8.3% | 60% | 9016 |
| commodity_codes | P11 | 0.3% | 50% | 8667 |
| vendor_bn9 | P08 | 15.7% | 50% | 8667 |
| buyer_phone | P11 | 30.9% | 75% | 7704 |
| solicitation_or_tender_number | P11 | 0.5% | 40% | 6903 |
| buyer_phone | P08 | 70.0% | 95% | 6318 |
| invoice_reference_hint | P08 | 0.9% | 25% | 6092 |
| buyer_phone | P13 | 63.8% | 95% | 5501 |
| buyer_bn_as_published | P08 | 14.0% | 35% | 5320 |
| vendor_emails | P08 | 54.2% | 75% | 5270 |
| buyer_legal_name_as_published | P08 | 55.0% | 75% | 5073 |
| buyer_ap_cycle_published | P08 | 0.0% | 20% | 5051 |
| ap_system_hint | P08 | 0.9% | 20% | 4838 |
| vendor_phone | P08 | 66.2% | 85% | 4763 |
| buyer_esignature_preference | P08 | 0.4% | 15% | 3705 |
| buyer_tax_exempt_status | P08 | 0.4% | 15% | 3697 |
| buyer_address | P08 | 80.4% | 95% | 3692 |
| buyer_payment_method_preference | P08 | 0.6% | 15% | 3633 |
| buyer_ap_cycle_published | P13 | 0.0% | 20% | 3523 |
| buyer_ap_cycle_published | P11 | 0.0% | 20% | 3483 |
| buyer_logo_url | P13 | 75.3% | 95% | 3479 |
| ap_system_hint | P13 | 0.6% | 20% | 3418 |
| ap_system_hint | P11 | 0.6% | 20% | 3380 |
| vendor_trading_name | P08 | 36.7% | 50% | 3367 |

## 1. identifiers

### `invoice_reference_hint`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 126 | 88.1% | 88.1% | -0.6 | 50% | ✅ met |
| P01T | 398 | 89.4% | 89.4% | -0.1 | 50% | ✅ met |
| P01_GOLD | 625 | 92.2% | 94.4% | +0.0 | 95% | 🟡 3 pts to go |
| P02 | 471 | 72.8% | 74.3% | -1.0 | 95% | ❌ 22 pts to go |
| P03 | 257 | 81.7% | 84.8% | -0.3 | 95% | ❌ 13 pts to go |
| P04 | 3823 | 29.1% | 30.5% | -3.7 | 90% | ❌ 61 pts to go |
| P05 | 422 | 38.9% | 41.7% | +0.3 | 70% | ❌ 31 pts to go |
| P06M | 13201 | 91.4% | 91.4% | -1.2 | n/a | no target |
| P06T | 75065 | 77.7% | 77.7% | -2.6 | n/a | no target |
| P06 | 295 | 29.5% | 29.5% | -2.2 | 30% | 🟡 0 pts to go |
| P07 | 793 | 6.2% | 6.2% | -0.7 | 30% | ❌ 24 pts to go |
| P08 | 25303 | 0.9% | 0.9% | -0.2 | 25% | ❌ 24 pts to go |
| P09 | 295 | 99.0% | 99.7% | +0.0 | 100% | 🟡 1 pts to go |
| P10R | 99941 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P10 | 2633 | 2.5% | 2.6% | -0.1 | 25% | ❌ 22 pts to go |
| P11 | 17455 | 8.3% | 8.4% | -5.3 | 60% | ❌ 52 pts to go |
| P12 | 7 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P13 | 17623 | 0.2% | 0.2% | +0.0 | 0% by design | — leave (by design) |

### `po_number_as_published`

> ceiling: a purchase-order number exists only where the buyer publishes PO-level data (Montréal, Laval, Toronto open data so far) or the record itself carries one; most sources publish awards, not POs — the target cannot be reached from public data for most buyers

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 126 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P01T | 398 | 0.0% | 0.0% | +0.0 | 10% | 🟡 10 pts to go |
| P01_GOLD | 625 | 6.1% | 6.1% | +0.0 | 50% | ❌ 44 pts to go |
| P02 | 471 | 6.2% | 6.2% | +0.0 | 50% | ❌ 44 pts to go |
| P03 | 257 | 1.6% | 1.6% | +0.0 | 40% | ❌ 38 pts to go |
| P04 | 3823 | 0.5% | 0.5% | +0.0 | 30% | ❌ 30 pts to go |
| P05 | 422 | 0.2% | 0.2% | +0.0 | 20% | ❌ 20 pts to go |
| P06M | 13201 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06T | 75065 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06 | 295 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P07 | 793 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P08 | 25303 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P09 | 295 | 0.7% | 0.7% | +0.0 | 50% | ❌ 49 pts to go |
| P10R | 99941 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P10 | 2633 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P11 | 17455 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P12 | 7 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P13 | 17623 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `contract_or_agreement_number`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 126 | 83.3% | 83.3% | +1.9 | n/a | no target |
| P01T | 398 | 73.9% | 73.9% | +3.4 | 50% | ✅ met |
| P01_GOLD | 625 | 66.9% | 66.9% | +0.0 | 85% | ❌ 18 pts to go |
| P02 | 471 | 64.1% | 64.1% | -0.8 | 90% | ❌ 26 pts to go |
| P03 | 257 | 61.1% | 61.1% | -0.2 | 85% | ❌ 24 pts to go |
| P04 | 3823 | 26.9% | 26.9% | -3.2 | 85% | ❌ 58 pts to go |
| P05 | 422 | 29.1% | 29.1% | +0.1 | 60% | ❌ 31 pts to go |
| P06M | 13201 | 91.3% | 91.3% | -1.1 | n/a | no target |
| P06T | 75065 | 77.5% | 77.5% | -2.5 | n/a | no target |
| P06 | 295 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P07 | 793 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P08 | 25303 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P09 | 295 | 95.9% | 95.9% | -0.1 | 100% | 🟡 4 pts to go |
| P10R | 99941 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P10 | 2633 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P11 | 17455 | 7.8% | 7.8% | -4.9 | 60% | ❌ 52 pts to go |
| P12 | 7 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P13 | 17623 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `solicitation_or_tender_number`

> ceiling: SEAO's 'numero' is the organisation's own reference for the notice (SEAO data dictionary) and is reported here; sources that publish awards under a tender number only (bids&tenders, SaskTenders, BC) also carry it as the contract reference, labelled

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 126 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P01T | 398 | 0.0% | 0.0% | +0.0 | 30% | ❌ 30 pts to go |
| P01_GOLD | 625 | 50.7% | 50.7% | +0.1 | 80% | ❌ 29 pts to go |
| P02 | 471 | 56.3% | 56.3% | -0.7 | 60% | 🟡 4 pts to go |
| P03 | 257 | 51.4% | 51.4% | -0.2 | 80% | ❌ 29 pts to go |
| P04 | 3823 | 22.3% | 22.3% | -2.7 | 50% | ❌ 28 pts to go |
| P05 | 422 | 11.6% | 11.6% | -0.3 | 40% | ❌ 28 pts to go |
| P06M | 13201 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06T | 75065 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06 | 295 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P07 | 793 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P08 | 25303 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P09 | 295 | 83.1% | 83.1% | -0.4 | 50% | ✅ met |
| P10R | 99941 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P10 | 2633 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P11 | 17455 | 0.5% | 0.5% | -0.3 | 40% | ❌ 40 pts to go |
| P12 | 7 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P13 | 17623 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `award_or_notice_id`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 126 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P01T | 398 | 0.3% | 0.3% | +0.0 | n/a | no target |
| P01_GOLD | 625 | 60.5% | 60.5% | +0.1 | 85% | ❌ 24 pts to go |
| P02 | 471 | 55.6% | 55.6% | -0.7 | 90% | ❌ 34 pts to go |
| P03 | 257 | 59.9% | 59.9% | -0.3 | 85% | ❌ 25 pts to go |
| P04 | 3823 | 23.0% | 23.0% | -2.8 | 85% | ❌ 62 pts to go |
| P05 | 422 | 19.9% | 19.9% | +0.0 | 50% | ❌ 30 pts to go |
| P06M | 13201 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06T | 75065 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06 | 295 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P07 | 793 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P08 | 25303 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P09 | 295 | 96.9% | 96.9% | -0.1 | 100% | 🟡 3 pts to go |
| P10R | 99941 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P10 | 2633 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P11 | 17455 | 0.5% | 0.5% | -0.4 | 60% | ❌ 60 pts to go |
| P12 | 7 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P13 | 17623 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `buyer_vendor_id`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 126 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P01T | 398 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P01_GOLD | 625 | 13.0% | 13.0% | +0.1 | 60% | ❌ 47 pts to go |
| P02 | 471 | 5.9% | 5.9% | -0.1 | 50% | ❌ 44 pts to go |
| P03 | 257 | 8.6% | 8.6% | +0.0 | 50% | ❌ 41 pts to go |
| P04 | 3823 | 1.8% | 1.8% | -0.2 | 40% | ❌ 38 pts to go |
| P05 | 422 | 0.7% | 0.7% | -0.2 | 20% | ❌ 19 pts to go |
| P06M | 13201 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06T | 75065 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06 | 295 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P07 | 793 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P08 | 25303 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P09 | 295 | 2.4% | 2.4% | +0.1 | 50% | ❌ 48 pts to go |
| P10R | 99941 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P10 | 2633 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P11 | 17455 | 0.1% | 0.1% | +0.0 | n/a | no target |
| P12 | 7 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P13 | 17623 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `commodity_codes`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 126 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P01T | 398 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P01_GOLD | 625 | 34.9% | 34.9% | +0.1 | 80% | ❌ 45 pts to go |
| P02 | 471 | 51.4% | 51.4% | -0.6 | 90% | ❌ 39 pts to go |
| P03 | 257 | 33.5% | 33.5% | -0.1 | 80% | ❌ 46 pts to go |
| P04 | 3823 | 21.0% | 21.0% | -2.6 | 85% | ❌ 64 pts to go |
| P05 | 422 | 5.5% | 5.5% | +0.1 | 50% | ❌ 44 pts to go |
| P06M | 13201 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06T | 75065 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06 | 295 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P07 | 793 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P08 | 25303 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P09 | 295 | 75.6% | 75.6% | -0.3 | 95% | ❌ 19 pts to go |
| P10R | 99941 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P10 | 2633 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P11 | 17455 | 0.3% | 0.3% | -0.3 | 50% | ❌ 50 pts to go |
| P12 | 7 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P13 | 17623 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `buyer_org_codes`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 126 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P01T | 398 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P01_GOLD | 625 | 8.5% | 8.5% | +0.0 | 50% | ❌ 42 pts to go |
| P02 | 471 | 6.2% | 6.2% | +0.0 | 50% | ❌ 44 pts to go |
| P03 | 257 | 1.9% | 1.9% | -0.1 | 30% | ❌ 28 pts to go |
| P04 | 3823 | 0.4% | 0.4% | -0.1 | 30% | ❌ 30 pts to go |
| P05 | 422 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06M | 13201 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06T | 75065 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06 | 295 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P07 | 793 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P08 | 25303 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P09 | 295 | 0.3% | 0.3% | +0.0 | n/a | no target |
| P10R | 99941 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P10 | 2633 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P11 | 17455 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P12 | 7 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P13 | 17623 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `records_with_this_vendor`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 126 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P01T | 398 | 100.0% | 100.0% | +0.0 | 60% | ✅ met |
| P01_GOLD | 625 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P02 | 471 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P03 | 257 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P04 | 3823 | 100.0% | 100.0% | +0.0 | 95% | ✅ met |
| P05 | 422 | 100.0% | 100.0% | +0.0 | 70% | ✅ met |
| P06M | 13201 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P06T | 75065 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P06 | 295 | 100.0% | 100.0% | +0.0 | 50% | ✅ met |
| P07 | 793 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P08 | 25303 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P09 | 295 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P10R | 99941 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P10 | 2633 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P11 | 17455 | 100.0% | 100.0% | +0.0 | 70% | ✅ met |
| P12 | 7 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P13 | 17623 | 0.0% | 0.0% | +0.0 | n/a | no target |

## 2. vendor

### `vendor_bn9`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 126 | 8.7% | 8.7% | -5.7 | 70% | ❌ 61 pts to go |
| P01T | 398 | 31.2% | 31.2% | -2.5 | 60% | ❌ 29 pts to go |
| P01_GOLD | 625 | 72.6% | 72.6% | -0.4 | 90% | ❌ 17 pts to go |
| P02 | 471 | 53.5% | 53.5% | -1.6 | 85% | ❌ 32 pts to go |
| P03 | 257 | 68.1% | 68.1% | -1.8 | 90% | ❌ 22 pts to go |
| P04 | 3823 | 31.5% | 31.5% | -1.0 | 75% | ❌ 44 pts to go |
| P05 | 422 | 50.2% | 50.2% | +0.3 | 50% | ✅ met |
| P06M | 13201 | 1.6% | 1.6% | -0.2 | n/a | no target |
| P06T | 75065 | 24.0% | 24.0% | +6.7 | n/a | no target |
| P06 | 295 | 26.1% | 26.1% | +3.3 | 40% | ❌ 14 pts to go |
| P07 | 793 | 19.4% | 19.4% | +3.0 | 50% | ❌ 31 pts to go |
| P08 | 25303 | 15.7% | 15.7% | +4.8 | 50% | ❌ 34 pts to go |
| P09 | 295 | 58.3% | 58.3% | +0.5 | 80% | ❌ 22 pts to go |
| P10R | 99941 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P10 | 2633 | 31.2% | 31.2% | +2.5 | 40% | 🟡 9 pts to go |
| P11 | 17455 | 94.6% | 94.6% | +3.5 | 60% | ✅ met |
| P12 | 7 | 42.9% | 42.9% | -19.6 | 85% | ❌ 42 pts to go |
| P13 | 17623 | 90.6% | 90.6% | -0.4 | 0% by design | — leave (by design) |

### `vendor_registered_address`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 126 | 54.8% | 54.8% | -12.2 | n/a | no target |
| P01T | 398 | 39.7% | 39.7% | +1.7 | n/a | no target |
| P01_GOLD | 625 | 70.6% | 70.6% | +0.2 | 95% | ❌ 24 pts to go |
| P02 | 471 | 73.0% | 73.0% | -0.8 | 95% | ❌ 22 pts to go |
| P03 | 257 | 71.2% | 71.2% | -0.7 | 95% | ❌ 24 pts to go |
| P04 | 3823 | 43.7% | 43.7% | -1.9 | 95% | ❌ 51 pts to go |
| P05 | 422 | 53.1% | 53.1% | -0.3 | 70% | ❌ 17 pts to go |
| P06M | 13201 | 42.5% | 42.5% | -12.1 | n/a | no target |
| P06T | 75065 | 33.0% | 33.0% | +2.7 | n/a | no target |
| P06 | 295 | 25.8% | 25.8% | +1.0 | 80% | ❌ 54 pts to go |
| P07 | 793 | 18.0% | 18.0% | +0.0 | 70% | ❌ 52 pts to go |
| P08 | 25303 | 13.7% | 13.7% | -0.4 | 70% | ❌ 56 pts to go |
| P09 | 295 | 87.1% | 87.1% | -0.4 | 100% | ❌ 13 pts to go |
| P10R | 99941 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P10 | 2633 | 32.6% | 32.6% | +0.1 | 70% | ❌ 37 pts to go |
| P11 | 17455 | 95.1% | 95.1% | +2.9 | 75% | ✅ met |
| P12 | 7 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P13 | 17623 | 16.1% | 16.1% | +16.1 | n/a | no target |

### `vendor_trading_name`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 126 | 18.3% | 18.3% | +1.8 | n/a | no target |
| P01T | 398 | 58.5% | 58.5% | +32.6 | n/a | no target |
| P01_GOLD | 625 | 50.4% | 50.4% | +2.5 | 60% | 🟡 10 pts to go |
| P02 | 471 | 55.4% | 55.4% | +0.1 | 60% | 🟡 5 pts to go |
| P03 | 257 | 55.3% | 55.3% | +0.2 | 60% | 🟡 5 pts to go |
| P04 | 3823 | 40.0% | 40.0% | +3.3 | 55% | ❌ 15 pts to go |
| P05 | 422 | 24.4% | 24.4% | +2.2 | 50% | ❌ 26 pts to go |
| P06M | 13201 | 7.0% | 7.0% | +3.4 | n/a | no target |
| P06T | 75065 | 65.8% | 65.8% | +38.8 | n/a | no target |
| P06 | 295 | 47.5% | 47.5% | +12.3 | n/a | no target |
| P07 | 793 | 42.7% | 42.7% | +9.5 | 55% | ❌ 12 pts to go |
| P08 | 25303 | 36.7% | 36.7% | +9.8 | 50% | ❌ 13 pts to go |
| P09 | 295 | 73.2% | 73.2% | +2.2 | 70% | ✅ met |
| P10R | 99941 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P10 | 2633 | 48.8% | 48.8% | +9.3 | 55% | 🟡 6 pts to go |
| P11 | 17455 | 96.5% | 96.5% | +4.5 | 50% | ✅ met |
| P12 | 7 | 100.0% | 100.0% | +12.5 | n/a | no target |
| P13 | 17623 | 74.0% | 74.0% | +74.0 | n/a | no target |

### `vendor_phone`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 126 | 49.2% | 49.2% | +34.8 | n/a | no target |
| P01T | 398 | 77.9% | 77.9% | +21.6 | n/a | no target |
| P01_GOLD | 625 | 49.9% | 49.9% | +2.0 | 70% | ❌ 20 pts to go |
| P02 | 471 | 58.0% | 58.0% | +4.0 | 70% | ❌ 12 pts to go |
| P03 | 257 | 50.6% | 50.6% | +1.0 | 70% | ❌ 19 pts to go |
| P04 | 3823 | 54.1% | 54.1% | +7.0 | 65% | ❌ 11 pts to go |
| P05 | 422 | 28.0% | 28.0% | -2.7 | 60% | ❌ 32 pts to go |
| P06M | 13201 | 36.3% | 36.3% | +32.8 | n/a | no target |
| P06T | 75065 | 73.0% | 73.0% | +9.2 | n/a | no target |
| P06 | 295 | 68.5% | 68.5% | +10.9 | 40% | ✅ met |
| P07 | 793 | 64.9% | 64.9% | +7.9 | 85% | ❌ 20 pts to go |
| P08 | 25303 | 66.2% | 66.2% | +9.3 | 85% | ❌ 19 pts to go |
| P09 | 295 | 60.7% | 60.7% | +7.2 | 85% | ❌ 24 pts to go |
| P10R | 99941 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P10 | 2633 | 64.7% | 64.7% | +3.7 | 85% | ❌ 20 pts to go |
| P11 | 17455 | 4.4% | 4.4% | -2.0 | 75% | ❌ 71 pts to go |
| P12 | 7 | 28.6% | 28.6% | +3.6 | n/a | no target |
| P13 | 17623 | 100.0% | 100.0% | +0.0 | 60% | ✅ met |

### `vendor_website`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 126 | 54.0% | 54.0% | +34.4 | n/a | no target |
| P01T | 398 | 98.2% | 98.2% | +1.8 | n/a | no target |
| P01_GOLD | 625 | 79.5% | 79.5% | -9.8 | 90% | ❌ 10 pts to go |
| P02 | 471 | 84.3% | 84.3% | -4.9 | 90% | 🟡 6 pts to go |
| P03 | 257 | 87.5% | 87.5% | -3.5 | 90% | 🟡 2 pts to go |
| P04 | 3823 | 85.2% | 85.2% | -5.0 | 85% | ✅ met |
| P05 | 422 | 44.1% | 44.1% | -8.1 | 70% | ❌ 26 pts to go |
| P06M | 13201 | 42.6% | 42.6% | +36.4 | n/a | no target |
| P06T | 75065 | 100.0% | 100.0% | +8.0 | n/a | no target |
| P06 | 295 | 98.3% | 98.3% | +0.0 | 50% | ✅ met |
| P07 | 793 | 99.1% | 99.1% | +0.0 | 100% | 🟡 1 pts to go |
| P08 | 25303 | 99.5% | 99.5% | +0.1 | 100% | 🟡 0 pts to go |
| P09 | 295 | 80.3% | 80.3% | +0.1 | 100% | ❌ 20 pts to go |
| P10R | 99941 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P10 | 2633 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P11 | 17455 | 99.8% | 99.8% | +0.1 | 100% | 🟡 0 pts to go |
| P12 | 7 | 28.6% | 28.6% | -8.9 | n/a | no target |
| P13 | 17623 | 100.0% | 100.0% | +0.0 | n/a | no target |

### `vendor_emails`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 126 | 15.1% | 15.1% | +0.7 | n/a | no target |
| P01T | 398 | 54.0% | 54.0% | +4.9 | n/a | no target |
| P01_GOLD | 625 | 43.5% | 43.5% | -1.7 | 70% | ❌ 26 pts to go |
| P02 | 471 | 49.3% | 49.3% | -0.2 | 75% | ❌ 26 pts to go |
| P03 | 257 | 44.0% | 44.0% | -0.5 | 75% | ❌ 31 pts to go |
| P04 | 3823 | 39.2% | 39.2% | +1.8 | 70% | ❌ 31 pts to go |
| P05 | 422 | 21.6% | 21.6% | -3.9 | 55% | ❌ 33 pts to go |
| P06M | 13201 | 4.5% | 4.5% | +1.2 | n/a | no target |
| P06T | 75065 | 40.3% | 40.3% | +0.7 | n/a | no target |
| P06 | 295 | 47.5% | 47.5% | +4.7 | n/a | no target |
| P07 | 793 | 50.1% | 50.1% | +4.2 | 70% | ❌ 20 pts to go |
| P08 | 25303 | 54.2% | 54.2% | +4.3 | 75% | ❌ 21 pts to go |
| P09 | 295 | 50.2% | 50.2% | +0.4 | 85% | ❌ 35 pts to go |
| P10R | 99941 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P10 | 2633 | 45.5% | 45.5% | +2.0 | 80% | ❌ 34 pts to go |
| P11 | 17455 | 3.4% | 3.4% | -1.6 | 70% | ❌ 67 pts to go |
| P12 | 7 | 14.3% | 14.3% | -10.7 | n/a | no target |
| P13 | 17623 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `vendor_logo_url`

> ceiling: needs the vendor's website first; sites that block automated readers (robots.txt / 403) are never read

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 126 | 54.0% | 54.0% | +40.6 | n/a | no target |
| P01T | 398 | 96.7% | 96.7% | +6.9 | n/a | no target |
| P01_GOLD | 625 | 73.8% | 73.8% | -3.7 | 90% | ❌ 16 pts to go |
| P02 | 471 | 79.4% | 79.4% | +1.8 | 90% | ❌ 11 pts to go |
| P03 | 257 | 82.9% | 82.9% | -0.3 | 90% | 🟡 7 pts to go |
| P04 | 3823 | 79.0% | 79.0% | +3.4 | 85% | 🟡 6 pts to go |
| P05 | 422 | 42.4% | 42.4% | -6.3 | 75% | ❌ 33 pts to go |
| P06M | 13201 | 42.3% | 42.3% | +38.2 | n/a | no target |
| P06T | 75065 | 97.6% | 97.6% | +14.4 | n/a | no target |
| P06 | 295 | 90.5% | 90.5% | +11.2 | n/a | no target |
| P07 | 793 | 92.2% | 92.2% | +10.6 | 100% | 🟡 8 pts to go |
| P08 | 25303 | 90.9% | 90.9% | +12.0 | 100% | 🟡 9 pts to go |
| P09 | 295 | 66.8% | 66.8% | +5.4 | n/a | no target |
| P10R | 99941 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P10 | 2633 | 88.7% | 88.7% | +4.5 | 100% | ❌ 11 pts to go |
| P11 | 17455 | 94.1% | 94.1% | +5.7 | n/a | no target |
| P12 | 7 | 28.6% | 28.6% | -8.9 | n/a | no target |
| P13 | 17623 | 83.9% | 83.9% | +0.7 | n/a | no target |

### `vendor_neq`

> ceiling: only Québec-registered vendors have an NEQ; the share of QC vendors is reported next to the rate

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 126 | 46.0% | 46.0% | -7.6 | n/a | no target · QC vendors: 45 rows, 100.0% filled |
| P01T | 398 | 21.9% | 21.9% | +4.1 | n/a | no target · QC vendors: 22 rows, 100.0% filled |
| P01_GOLD | 625 | 43.7% | 43.7% | +0.1 | 95% | ❌ 51 pts to go · QC vendors: 53 rows, 98.1% filled |
| P02 | 471 | 54.4% | 54.4% | -0.7 | 95% | ❌ 41 pts to go · QC vendors: 110 rows, 100.0% filled |
| P03 | 257 | 45.9% | 45.9% | -0.6 | 95% | ❌ 49 pts to go · QC vendors: 18 rows, 100.0% filled |
| P04 | 3823 | 28.3% | 28.3% | -3.6 | 95% | ❌ 67 pts to go · QC vendors: 496 rows, 98.8% filled |
| P05 | 422 | 14.0% | 14.0% | -0.8 | n/a | no target · QC vendors: 34 rows, 94.1% filled |
| P06M | 13201 | 41.5% | 41.5% | -11.8 | n/a | no target · QC vendors: 4809 rows, 100.0% filled |
| P06T | 75065 | 21.3% | 21.3% | +3.8 | n/a | no target · QC vendors: 3445 rows, 100.0% filled |
| P06 | 295 | 8.1% | 8.1% | -0.2 | n/a | no target · QC vendors: 17 rows, 76.5% filled |
| P07 | 793 | 5.9% | 5.9% | -0.9 | n/a | no target · QC vendors: 39 rows, 79.5% filled |
| P08 | 25303 | 6.1% | 6.1% | -0.4 | n/a | no target · QC vendors: 1235 rows, 97.9% filled |
| P09 | 295 | 78.0% | 78.0% | -0.2 | 95% | ❌ 17 pts to go · QC vendors: 106 rows, 100.0% filled |
| P10R | 99941 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P10 | 2633 | 17.6% | 17.6% | +0.0 | n/a | no target · QC vendors: 304 rows, 94.7% filled |
| P11 | 17455 | 89.0% | 89.0% | +7.5 | n/a | no target · QC vendors: 114 rows, 98.2% filled |
| P12 | 7 | 71.4% | 71.4% | +8.9 | n/a | no target · QC vendors: 1 rows, 100.0% filled |
| P13 | 17623 | 16.1% | 16.1% | +16.1 | n/a | no target · QC vendors: 2841 rows, 100.0% filled |

### `vendor_years_in_business`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 126 | 54.0% | 54.0% | -10.9 | n/a | no target · vendors with a registry record: 68 rows, 100.0% filled |
| P01T | 398 | 39.7% | 39.7% | +1.4 | n/a | no target · vendors with a registry record: 158 rows, 100.0% filled |
| P01_GOLD | 625 | 79.5% | 79.5% | +0.1 | 100% | ❌ 20 pts to go · vendors with a registry record: 497 rows, 100.0% filled |
| P02 | 471 | 76.6% | 76.6% | -0.8 | 100% | ❌ 23 pts to go · vendors with a registry record: 361 rows, 100.0% filled |
| P03 | 257 | 80.5% | 80.5% | -0.7 | 100% | ❌ 20 pts to go · vendors with a registry record: 207 rows, 100.0% filled |
| P04 | 3823 | 44.1% | 44.1% | -2.0 | 100% | ❌ 56 pts to go · vendors with a registry record: 1685 rows, 100.0% filled |
| P05 | 422 | 58.1% | 58.1% | -0.2 | n/a | no target · vendors with a registry record: 245 rows, 100.0% filled |
| P06M | 13201 | 42.4% | 42.4% | -11.9 | n/a | no target · vendors with a registry record: 5592 rows, 100.0% filled |
| P06T | 75065 | 33.0% | 33.0% | +2.6 | n/a | no target · vendors with a registry record: 24780 rows, 100.0% filled |
| P06 | 295 | 26.1% | 26.1% | +0.6 | n/a | no target · vendors with a registry record: 77 rows, 100.0% filled |
| P07 | 793 | 18.4% | 18.4% | +0.0 | n/a | no target · vendors with a registry record: 146 rows, 100.0% filled |
| P08 | 25303 | 13.8% | 13.8% | -0.5 | n/a | no target · vendors with a registry record: 3504 rows, 100.0% filled |
| P09 | 295 | 90.8% | 90.8% | -0.3 | n/a | no target · vendors with a registry record: 268 rows, 100.0% filled |
| P10R | 99941 | 100.0% | 100.0% | +0.0 | n/a | no target · vendors with a registry record: 99941 rows, 100.0% filled |
| P10 | 2633 | 33.3% | 33.3% | +0.1 | n/a | no target · vendors with a registry record: 876 rows, 100.0% filled |
| P11 | 17455 | 95.2% | 95.2% | +2.9 | n/a | no target · vendors with a registry record: 16613 rows, 100.0% filled |
| P12 | 7 | 100.0% | 100.0% | +0.0 | n/a | no target · vendors with a registry record: 7 rows, 100.0% filled |
| P13 | 17623 | 16.1% | 16.1% | +16.1 | n/a | no target · vendors with a registry record: 2841 rows, 100.0% filled |

## 3. buyer

### `buyer_legal_name_as_published`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 126 | 94.4% | 94.4% | +5.7 | 90% | ✅ met |
| P01T | 398 | 70.9% | 70.9% | +14.6 | 90% | ❌ 19 pts to go |
| P01_GOLD | 625 | 87.5% | 87.5% | +3.8 | 95% | 🟡 8 pts to go |
| P02 | 471 | 88.7% | 88.7% | +3.5 | 95% | 🟡 6 pts to go |
| P03 | 257 | 84.4% | 84.4% | +5.5 | 85% | 🟡 1 pts to go |
| P04 | 3823 | 65.0% | 65.0% | +8.6 | 90% | ❌ 25 pts to go |
| P05 | 422 | 80.1% | 80.1% | +12.4 | 75% | ✅ met |
| P06M | 13201 | 91.9% | 91.9% | +4.8 | n/a | no target |
| P06T | 75065 | 45.7% | 45.7% | +16.7 | n/a | no target |
| P06 | 295 | 75.9% | 75.9% | +19.0 | 80% | 🟡 4 pts to go |
| P07 | 793 | 61.3% | 61.4% | +15.1 | 80% | ❌ 19 pts to go |
| P08 | 25303 | 55.0% | 55.0% | +16.5 | 75% | ❌ 20 pts to go |
| P09 | 295 | 77.3% | 77.3% | +0.1 | 95% | ❌ 18 pts to go |
| P10R | 99941 | 39.8% | 39.8% | +14.8 | n/a | no target |
| P10 | 2633 | 52.6% | 52.7% | +13.6 | 70% | ❌ 17 pts to go |
| P11 | 17455 | 51.2% | 51.2% | +41.6 | 65% | ❌ 14 pts to go |
| P12 | 7 | 71.4% | 71.4% | -3.6 | 80% | 🟡 9 pts to go |
| P13 | 17623 | 52.2% | 52.2% | +13.0 | 60% | 🟡 8 pts to go |

### `buyer_bn_as_published`

> ceiling: a buyer's BN is public only where the buyer prints it or a public dataset carries it (CRA charities, federal grants & contributions recipients, business registries for corporations); municipalities rarely publish theirs

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 126 | 19.0% | 19.0% | -0.6 | 50% | ❌ 31 pts to go |
| P01T | 398 | 13.6% | 13.6% | +0.3 | n/a | no target |
| P01_GOLD | 625 | 19.8% | 19.8% | -0.8 | 40% | ❌ 20 pts to go |
| P02 | 471 | 19.3% | 19.3% | +0.4 | 40% | ❌ 21 pts to go |
| P03 | 257 | 23.0% | 23.0% | +0.7 | 40% | ❌ 17 pts to go |
| P04 | 3823 | 15.3% | 15.3% | -1.0 | 40% | ❌ 25 pts to go |
| P05 | 422 | 19.9% | 19.9% | +0.2 | 25% | 🟡 5 pts to go |
| P06M | 13201 | 10.5% | 10.5% | +1.7 | n/a | no target |
| P06T | 75065 | 8.4% | 8.4% | +0.9 | n/a | no target |
| P06 | 295 | 16.3% | 16.3% | +3.5 | 35% | ❌ 19 pts to go |
| P07 | 793 | 14.9% | 14.9% | +3.4 | 35% | ❌ 20 pts to go |
| P08 | 25303 | 14.0% | 14.0% | +3.6 | 35% | ❌ 21 pts to go |
| P09 | 295 | 16.3% | 16.3% | +0.1 | n/a | no target |
| P10R | 99941 | 8.7% | 8.7% | +1.6 | n/a | no target |
| P10 | 2633 | 11.1% | 11.1% | +4.6 | 30% | ❌ 19 pts to go |
| P11 | 17455 | 1.6% | 1.6% | +0.4 | n/a | no target |
| P12 | 7 | 14.3% | 14.3% | +1.8 | n/a | no target |
| P13 | 17623 | 21.0% | 21.0% | +0.0 | 30% | 🟡 9 pts to go |

### `buyer_address`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 126 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P01T | 398 | 90.2% | 90.2% | -1.7 | 100% | 🟡 10 pts to go |
| P01_GOLD | 625 | 90.7% | 90.7% | +1.2 | 100% | 🟡 9 pts to go |
| P02 | 471 | 95.8% | 95.8% | +0.5 | 100% | 🟡 4 pts to go |
| P03 | 257 | 89.9% | 89.9% | +0.4 | 100% | ❌ 10 pts to go |
| P04 | 3823 | 75.9% | 75.9% | +0.0 | 100% | ❌ 24 pts to go |
| P05 | 422 | 89.1% | 89.1% | +1.7 | 100% | ❌ 11 pts to go |
| P06M | 13201 | 99.2% | 99.2% | +0.4 | n/a | no target |
| P06T | 75065 | 77.7% | 77.7% | +0.3 | n/a | no target |
| P06 | 295 | 82.0% | 82.0% | +1.0 | 95% | ❌ 13 pts to go |
| P07 | 793 | 83.9% | 83.9% | +0.3 | 95% | ❌ 11 pts to go |
| P08 | 25303 | 80.4% | 80.4% | +0.2 | 95% | ❌ 15 pts to go |
| P09 | 295 | 95.9% | 95.9% | +0.2 | 100% | 🟡 4 pts to go |
| P10R | 99941 | 61.3% | 61.3% | +2.5 | n/a | no target |
| P10 | 2633 | 66.3% | 66.4% | +1.2 | 95% | ❌ 29 pts to go |
| P11 | 17455 | 93.0% | 93.0% | +5.8 | 80% | ✅ met |
| P12 | 7 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P13 | 17623 | 77.7% | 77.7% | +2.5 | 95% | ❌ 17 pts to go |

### `buyer_phone`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 126 | 87.3% | 87.3% | +1.7 | n/a | no target |
| P01T | 398 | 75.1% | 75.1% | +11.5 | n/a | no target |
| P01_GOLD | 625 | 72.8% | 72.8% | +3.3 | 90% | ❌ 17 pts to go |
| P02 | 471 | 77.7% | 77.7% | +2.0 | 95% | ❌ 17 pts to go |
| P03 | 257 | 74.3% | 74.3% | +0.5 | 95% | ❌ 21 pts to go |
| P04 | 3823 | 70.4% | 70.4% | +3.8 | 95% | ❌ 25 pts to go |
| P05 | 422 | 73.5% | 73.5% | +3.0 | 90% | ❌ 16 pts to go |
| P06M | 13201 | 87.7% | 87.7% | +1.3 | n/a | no target |
| P06T | 75065 | 63.9% | 63.9% | +16.0 | n/a | no target |
| P06 | 295 | 72.2% | 72.2% | +9.1 | 95% | ❌ 23 pts to go |
| P07 | 793 | 67.1% | 67.1% | +12.1 | 90% | ❌ 23 pts to go |
| P08 | 25303 | 70.0% | 70.0% | +11.2 | 95% | ❌ 25 pts to go |
| P09 | 295 | 86.4% | 86.4% | +0.3 | 100% | ❌ 14 pts to go |
| P10R | 99941 | 60.8% | 60.8% | +15.7 | n/a | no target |
| P10 | 2633 | 61.1% | 61.1% | +4.6 | 95% | ❌ 34 pts to go |
| P11 | 17455 | 30.9% | 30.9% | +19.7 | 75% | ❌ 44 pts to go |
| P12 | 7 | 71.4% | 71.4% | -3.6 | n/a | no target |
| P13 | 17623 | 63.8% | 63.8% | +16.2 | 95% | ❌ 31 pts to go |

### `buyer_logo_url`

> ceiling: sites that block automated readers (robots.txt / 403) are never read; an og:image that looks like a photo is labelled

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 126 | 90.5% | 90.5% | +19.4 | n/a | no target |
| P01T | 398 | 88.4% | 88.4% | +14.3 | 95% | 🟡 7 pts to go |
| P01_GOLD | 625 | 84.8% | 84.8% | +4.1 | 90% | 🟡 5 pts to go |
| P02 | 471 | 90.7% | 90.7% | +4.9 | 95% | 🟡 4 pts to go |
| P03 | 257 | 85.6% | 85.6% | +1.6 | 95% | 🟡 9 pts to go |
| P04 | 3823 | 90.6% | 90.6% | +7.3 | 90% | ✅ met |
| P05 | 422 | 93.1% | 93.1% | +4.6 | 95% | 🟡 2 pts to go |
| P06M | 13201 | 95.7% | 95.7% | +29.0 | n/a | no target |
| P06T | 75065 | 85.7% | 85.7% | +24.2 | n/a | no target |
| P06 | 295 | 94.2% | 94.2% | +12.1 | 100% | 🟡 6 pts to go |
| P07 | 793 | 93.7% | 93.7% | +16.5 | 100% | 🟡 6 pts to go |
| P08 | 25303 | 94.1% | 94.1% | +17.0 | 100% | 🟡 6 pts to go |
| P09 | 295 | 72.5% | 72.5% | +3.9 | n/a | no target |
| P10R | 99941 | 84.9% | 84.9% | +24.9 | n/a | no target |
| P10 | 2633 | 93.2% | 93.2% | +6.4 | 100% | 🟡 7 pts to go |
| P11 | 17455 | 79.0% | 79.0% | +60.2 | 80% | 🟡 1 pts to go |
| P12 | 7 | 71.4% | 71.4% | -3.6 | n/a | no target |
| P13 | 17623 | 75.3% | 75.3% | +24.3 | 95% | ❌ 20 pts to go |

## 4. AP

### `ap_contact_name_as_published`

> ceiling: owner 2026-11-08: the AP contact person the organisation itself names on its AP / finance page is allowed (name + role phrase, quoted); mailboxes stay organisational; many bodies publish no AP person

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 126 | 2.4% | 2.4% | -1.7 | n/a | no target |
| P01T | 398 | 7.5% | 7.5% | -0.9 | n/a | no target |
| P01_GOLD | 625 | 14.2% | 14.2% | +0.0 | 25% | ❌ 11 pts to go |
| P02 | 471 | 24.2% | 24.2% | -0.3 | 40% | ❌ 16 pts to go |
| P03 | 257 | 8.9% | 8.9% | -0.1 | 20% | ❌ 11 pts to go |
| P04 | 3823 | 3.2% | 3.2% | -0.4 | 20% | ❌ 17 pts to go |
| P05 | 422 | 3.1% | 3.1% | -0.2 | 15% | ❌ 12 pts to go |
| P06M | 13201 | 0.2% | 0.2% | -0.1 | n/a | no target |
| P06T | 75065 | 0.3% | 0.3% | -0.1 | n/a | no target |
| P06 | 295 | 5.4% | 5.4% | -0.8 | n/a | no target |
| P07 | 793 | 7.3% | 7.3% | +0.0 | n/a | no target |
| P08 | 25303 | 0.2% | 0.2% | -0.1 | n/a | no target |
| P09 | 295 | 7.8% | 7.8% | +0.2 | n/a | no target |
| P10R | 99941 | 0.2% | 0.2% | +0.0 | n/a | no target |
| P10 | 2633 | 0.9% | 0.9% | -0.1 | n/a | no target |
| P11 | 17455 | 0.1% | 0.1% | -0.1 | n/a | no target |
| P12 | 7 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P13 | 17623 | 0.4% | 0.4% | +0.0 | n/a | no target |

### `ap_phone`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 126 | 19.0% | 19.0% | -7.8 | n/a | no target |
| P01T | 398 | 21.9% | 21.9% | -2.2 | 70% | ❌ 48 pts to go |
| P01_GOLD | 625 | 43.4% | 43.4% | +0.1 | 80% | ❌ 37 pts to go |
| P02 | 471 | 56.1% | 56.1% | -0.7 | 90% | ❌ 34 pts to go |
| P03 | 257 | 19.1% | 19.1% | +0.0 | 60% | ❌ 41 pts to go |
| P04 | 3823 | 21.1% | 21.1% | -2.6 | 85% | ❌ 64 pts to go |
| P05 | 422 | 11.8% | 11.8% | -0.1 | 50% | ❌ 38 pts to go |
| P06M | 13201 | 0.3% | 0.3% | -0.1 | n/a | no target |
| P06T | 75065 | 0.5% | 0.5% | -0.1 | n/a | no target |
| P06 | 295 | 14.9% | 14.9% | -1.3 | n/a | no target |
| P07 | 793 | 11.6% | 11.6% | -1.4 | n/a | no target |
| P08 | 25303 | 0.4% | 0.4% | -0.1 | n/a | no target |
| P09 | 295 | 77.3% | 77.3% | -0.3 | 95% | ❌ 18 pts to go |
| P10R | 99941 | 0.2% | 0.2% | +0.0 | n/a | no target |
| P10 | 2633 | 1.7% | 1.7% | +0.0 | n/a | no target |
| P11 | 17455 | 2.0% | 2.0% | -1.6 | n/a | no target |
| P12 | 7 | 28.6% | 28.6% | +3.6 | n/a | no target |
| P13 | 17623 | 0.7% | 0.7% | +0.0 | n/a | no target |

### `invoice_mailing_address`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 126 | 5.6% | 5.6% | -1.6 | n/a | no target |
| P01T | 398 | 11.3% | 11.3% | -0.7 | n/a | no target |
| P01_GOLD | 625 | 33.9% | 33.9% | +0.0 | 70% | ❌ 36 pts to go |
| P02 | 471 | 38.4% | 38.4% | -0.5 | 75% | ❌ 37 pts to go |
| P03 | 257 | 19.1% | 19.1% | +0.0 | 55% | ❌ 36 pts to go |
| P04 | 3823 | 21.0% | 21.0% | -2.6 | 75% | ❌ 54 pts to go |
| P05 | 422 | 10.9% | 10.9% | +0.1 | 50% | ❌ 39 pts to go |
| P06M | 13201 | 0.1% | 0.1% | -0.1 | n/a | no target |
| P06T | 75065 | 0.3% | 0.3% | -0.1 | n/a | no target |
| P06 | 295 | 7.5% | 7.5% | -0.8 | n/a | no target |
| P07 | 793 | 5.4% | 5.4% | -1.0 | n/a | no target |
| P08 | 25303 | 0.2% | 0.2% | +0.0 | n/a | no target |
| P09 | 295 | 74.9% | 74.9% | -0.3 | 95% | ❌ 20 pts to go |
| P10R | 99941 | 0.1% | 0.1% | -0.1 | n/a | no target |
| P10 | 2633 | 1.0% | 1.0% | +0.0 | n/a | no target |
| P11 | 17455 | 2.0% | 2.0% | -1.6 | n/a | no target |
| P12 | 7 | 14.3% | 14.3% | +1.8 | n/a | no target |
| P13 | 17623 | 0.4% | 0.4% | +0.0 | n/a | no target |

### `invoicing_requirements`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 126 | 5.6% | 5.6% | -0.6 | n/a | no target |
| P01T | 398 | 7.5% | 7.5% | -1.8 | n/a | no target |
| P01_GOLD | 625 | 57.9% | 58.1% | -0.1 | 80% | ❌ 22 pts to go |
| P02 | 471 | 45.2% | 45.4% | -0.6 | 75% | ❌ 30 pts to go |
| P03 | 257 | 37.7% | 37.7% | -0.2 | 70% | ❌ 32 pts to go |
| P04 | 3823 | 20.6% | 21.0% | -2.5 | 70% | ❌ 49 pts to go |
| P05 | 422 | 14.2% | 14.2% | -0.1 | 50% | ❌ 36 pts to go |
| P06M | 13201 | 0.3% | 0.3% | -0.1 | n/a | no target |
| P06T | 75065 | 0.2% | 0.3% | -0.1 | n/a | no target |
| P06 | 295 | 13.2% | 13.2% | -0.2 | n/a | no target |
| P07 | 793 | 1.9% | 1.9% | -0.1 | n/a | no target |
| P08 | 25303 | 0.3% | 0.3% | -0.1 | n/a | no target |
| P09 | 295 | 46.1% | 46.4% | +0.2 | 80% | ❌ 34 pts to go |
| P10R | 99941 | 0.1% | 0.1% | +0.0 | n/a | no target |
| P10 | 2633 | 1.2% | 1.2% | +0.0 | n/a | no target |
| P11 | 17455 | 0.6% | 0.6% | -0.5 | n/a | no target |
| P12 | 7 | 42.9% | 42.9% | +5.4 | n/a | no target |
| P13 | 17623 | 0.3% | 0.3% | +0.0 | n/a | no target |

### `payment_terms_as_published`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 126 | 11.1% | 11.1% | -0.2 | n/a | no target |
| P01T | 398 | 17.6% | 17.6% | -4.4 | 60% | ❌ 42 pts to go |
| P01_GOLD | 625 | 63.5% | 63.5% | -0.1 | 70% | 🟡 6 pts to go |
| P02 | 471 | 38.4% | 38.4% | -0.5 | 50% | ❌ 12 pts to go |
| P03 | 257 | 49.8% | 49.8% | -0.2 | 55% | 🟡 5 pts to go |
| P04 | 3823 | 11.7% | 11.7% | -1.6 | 40% | ❌ 28 pts to go |
| P05 | 422 | 17.3% | 17.3% | +0.0 | 40% | ❌ 23 pts to go |
| P06M | 13201 | 0.5% | 0.5% | -0.2 | n/a | no target |
| P06T | 75065 | 1.9% | 1.9% | -0.5 | n/a | no target |
| P06 | 295 | 19.3% | 19.3% | -0.4 | n/a | no target |
| P07 | 793 | 6.1% | 6.1% | -0.6 | n/a | no target |
| P08 | 25303 | 2.1% | 2.1% | -0.5 | n/a | no target |
| P09 | 295 | 5.8% | 5.8% | -0.1 | n/a | no target |
| P10R | 99941 | 0.2% | 0.2% | +0.0 | n/a | no target |
| P10 | 2633 | 4.4% | 4.4% | -0.1 | n/a | no target |
| P11 | 17455 | 3.2% | 3.2% | -1.1 | n/a | no target |
| P12 | 7 | 0.0% | 0.0% | -12.5 | n/a | no target |
| P13 | 17623 | 0.2% | 0.2% | +0.0 | n/a | no target |

### `po_required_as_published`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 126 | 14.3% | 14.3% | -2.2 | n/a | no target |
| P01T | 398 | 21.4% | 21.4% | -3.9 | 65% | ❌ 44 pts to go |
| P01_GOLD | 625 | 69.0% | 69.0% | +0.0 | 70% | 🟡 1 pts to go |
| P02 | 471 | 23.6% | 23.6% | -0.3 | 50% | ❌ 26 pts to go |
| P03 | 257 | 52.1% | 52.1% | -0.2 | 60% | 🟡 8 pts to go |
| P04 | 3823 | 5.0% | 5.0% | -0.8 | 40% | ❌ 35 pts to go |
| P05 | 422 | 19.9% | 19.9% | +0.2 | 45% | ❌ 25 pts to go |
| P06M | 13201 | 0.2% | 0.2% | -0.1 | n/a | no target |
| P06T | 75065 | 0.5% | 0.5% | -0.1 | n/a | no target |
| P06 | 295 | 29.5% | 29.5% | -2.2 | n/a | no target |
| P07 | 793 | 6.2% | 6.2% | -0.7 | n/a | no target |
| P08 | 25303 | 0.9% | 0.9% | -0.2 | n/a | no target |
| P09 | 295 | 9.8% | 9.8% | -0.1 | n/a | no target |
| P10R | 99941 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P10 | 2633 | 2.5% | 2.5% | -0.1 | n/a | no target |
| P11 | 17455 | 0.6% | 0.6% | -0.4 | n/a | no target |
| P12 | 7 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P13 | 17623 | 0.2% | 0.2% | +0.0 | n/a | no target |

### `invoice_portal_url`

> ceiling: only portals the buyer names on its own pages; informational tax-authority links are not portals

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 126 | 4.8% | 4.8% | -1.4 | n/a | no target |
| P01T | 398 | 12.1% | 12.1% | -2.4 | n/a | no target |
| P01_GOLD | 625 | 49.8% | 49.8% | +0.0 | 50% | 🟡 0 pts to go |
| P02 | 471 | 36.9% | 36.9% | -0.5 | n/a | no target |
| P03 | 257 | 52.5% | 52.5% | -0.6 | 60% | 🟡 8 pts to go |
| P04 | 3823 | 11.5% | 11.5% | -1.4 | n/a | no target |
| P05 | 422 | 14.9% | 14.9% | -0.3 | n/a | no target |
| P06M | 13201 | 0.2% | 0.2% | -0.1 | n/a | no target |
| P06T | 75065 | 0.4% | 0.4% | -0.1 | n/a | no target |
| P06 | 295 | 21.4% | 21.4% | -0.3 | n/a | no target |
| P07 | 793 | 6.8% | 6.8% | -0.4 | n/a | no target |
| P08 | 25303 | 0.5% | 0.5% | +0.0 | n/a | no target |
| P09 | 295 | 18.3% | 18.3% | +0.1 | n/a | no target |
| P10R | 99941 | 0.1% | 0.1% | +0.0 | n/a | no target |
| P10 | 2633 | 2.3% | 2.3% | +0.0 | n/a | no target |
| P11 | 17455 | 0.5% | 0.5% | -0.3 | n/a | no target |
| P12 | 7 | 14.3% | 14.3% | +14.3 | n/a | no target |
| P13 | 17623 | 0.4% | 0.4% | +0.0 | n/a | no target |

### `buyer_payment_method_preference`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 126 | 10.3% | 10.3% | -1.0 | 15% | 🟡 5 pts to go |
| P01T | 398 | 10.3% | 10.3% | -0.8 | 15% | 🟡 5 pts to go |
| P01_GOLD | 625 | 35.4% | 35.4% | +0.1 | 40% | 🟡 5 pts to go |
| P02 | 471 | 13.0% | 13.2% | +0.5 | 25% | ❌ 12 pts to go |
| P03 | 257 | 17.9% | 17.9% | -0.1 | 25% | 🟡 7 pts to go |
| P04 | 3823 | 2.7% | 2.7% | -0.1 | 15% | ❌ 12 pts to go |
| P05 | 422 | 6.6% | 6.6% | -0.2 | 15% | 🟡 8 pts to go |
| P06M | 13201 | 0.8% | 0.8% | +0.2 | 15% | ❌ 14 pts to go |
| P06T | 75065 | 0.6% | 0.6% | +0.2 | 15% | ❌ 14 pts to go |
| P06 | 295 | 9.5% | 9.5% | +0.2 | 15% | 🟡 6 pts to go |
| P07 | 793 | 3.9% | 3.9% | +0.7 | 15% | ❌ 11 pts to go |
| P08 | 25303 | 0.6% | 0.6% | +0.2 | 15% | ❌ 14 pts to go |
| P09 | 295 | 1.0% | 1.0% | +0.0 | 15% | ❌ 14 pts to go |
| P10R | 99941 | 0.7% | 0.7% | +0.3 | 15% | ❌ 14 pts to go |
| P10 | 2633 | 1.3% | 1.3% | +0.3 | 15% | ❌ 14 pts to go |
| P11 | 17455 | 0.4% | 0.4% | +0.2 | 15% | ❌ 15 pts to go |
| P12 | 7 | 14.3% | 14.3% | +1.8 | 15% | 🟡 1 pts to go |
| P13 | 17623 | 0.6% | 0.6% | +0.2 | 15% | ❌ 14 pts to go |

### `buyer_tax_exempt_status`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 126 | 3.2% | 3.2% | -3.0 | 15% | ❌ 12 pts to go |
| P01T | 398 | 9.3% | 9.3% | -2.7 | 25% | ❌ 16 pts to go |
| P01_GOLD | 625 | 29.1% | 29.1% | -0.1 | 25% | ✅ met |
| P02 | 471 | 25.1% | 25.1% | -0.3 | 15% | ✅ met |
| P03 | 257 | 21.4% | 21.4% | -0.1 | 15% | ✅ met |
| P04 | 3823 | 3.7% | 3.7% | -0.4 | 15% | ❌ 11 pts to go |
| P05 | 422 | 10.9% | 10.9% | +0.1 | 15% | 🟡 4 pts to go |
| P06M | 13201 | 0.2% | 0.2% | +0.0 | 15% | ❌ 15 pts to go |
| P06T | 75065 | 0.3% | 0.3% | +0.0 | 15% | ❌ 15 pts to go |
| P06 | 295 | 7.5% | 7.5% | -0.1 | 15% | 🟡 8 pts to go |
| P07 | 793 | 2.8% | 2.8% | -0.3 | 15% | ❌ 12 pts to go |
| P08 | 25303 | 0.4% | 0.4% | +0.0 | 15% | ❌ 15 pts to go |
| P09 | 295 | 1.0% | 1.0% | +0.0 | 15% | ❌ 14 pts to go |
| P10R | 99941 | 0.0% | 0.0% | +0.0 | 15% | ❌ 15 pts to go |
| P10 | 2633 | 1.6% | 1.6% | +0.0 | 15% | ❌ 13 pts to go |
| P11 | 17455 | 0.4% | 0.4% | -0.1 | 15% | ❌ 15 pts to go |
| P12 | 7 | 28.6% | 28.6% | +3.6 | 15% | ✅ met |
| P13 | 17623 | 0.1% | 0.1% | +0.1 | 15% | ❌ 15 pts to go |

### `buyer_ap_cycle_published`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 126 | 0.0% | 0.0% | +0.0 | 20% | ❌ 20 pts to go |
| P01T | 398 | 3.3% | 3.3% | -0.6 | 20% | ❌ 17 pts to go |
| P01_GOLD | 625 | 4.5% | 4.5% | +0.2 | 20% | ❌ 16 pts to go |
| P02 | 471 | 1.3% | 1.3% | +0.0 | 20% | ❌ 19 pts to go |
| P03 | 257 | 1.6% | 1.6% | +0.0 | 20% | ❌ 18 pts to go |
| P04 | 3823 | 0.6% | 0.6% | +0.0 | 20% | ❌ 19 pts to go |
| P05 | 422 | 1.2% | 1.2% | +0.0 | 20% | ❌ 19 pts to go |
| P06M | 13201 | 0.1% | 0.1% | +0.1 | 20% | ❌ 20 pts to go |
| P06T | 75065 | 0.0% | 0.0% | +0.0 | 20% | ❌ 20 pts to go |
| P06 | 295 | 1.4% | 1.4% | +0.0 | 20% | ❌ 19 pts to go |
| P07 | 793 | 0.4% | 0.4% | +0.0 | 20% | ❌ 20 pts to go |
| P08 | 25303 | 0.0% | 0.0% | +0.0 | 20% | ❌ 20 pts to go |
| P09 | 295 | 0.0% | 0.0% | +0.0 | 20% | ❌ 20 pts to go |
| P10R | 99941 | 0.0% | 0.0% | +0.0 | 20% | ❌ 20 pts to go |
| P10 | 2633 | 0.3% | 0.3% | +0.0 | 20% | ❌ 20 pts to go |
| P11 | 17455 | 0.0% | 0.0% | +0.0 | 20% | ❌ 20 pts to go |
| P12 | 7 | 0.0% | 0.0% | +0.0 | 20% | ❌ 20 pts to go |
| P13 | 17623 | 0.0% | 0.0% | +0.0 | 20% | ❌ 20 pts to go |

### `buyer_esignature_preference`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 126 | 0.8% | 0.8% | -0.2 | 15% | ❌ 14 pts to go |
| P01T | 398 | 2.3% | 2.3% | -0.1 | 15% | ❌ 13 pts to go |
| P01_GOLD | 625 | 10.4% | 10.4% | -0.1 | 15% | 🟡 5 pts to go |
| P02 | 471 | 11.9% | 11.9% | -0.1 | 15% | 🟡 3 pts to go |
| P03 | 257 | 20.6% | 20.6% | -0.1 | 15% | ✅ met |
| P04 | 3823 | 2.2% | 2.2% | -0.2 | 15% | ❌ 13 pts to go |
| P05 | 422 | 2.8% | 2.8% | -0.2 | 15% | ❌ 12 pts to go |
| P06M | 13201 | 0.1% | 0.1% | -0.1 | 15% | ❌ 15 pts to go |
| P06T | 75065 | 0.2% | 0.2% | +0.0 | 15% | ❌ 15 pts to go |
| P06 | 295 | 5.1% | 5.1% | -0.1 | 15% | 🟡 10 pts to go |
| P07 | 793 | 1.8% | 1.8% | +0.1 | 15% | ❌ 13 pts to go |
| P08 | 25303 | 0.4% | 0.4% | +0.0 | 15% | ❌ 15 pts to go |
| P09 | 295 | 0.7% | 0.7% | +0.0 | 15% | ❌ 14 pts to go |
| P10R | 99941 | 0.0% | 0.0% | +0.0 | 15% | ❌ 15 pts to go |
| P10 | 2633 | 0.9% | 0.9% | +0.0 | 15% | ❌ 14 pts to go |
| P11 | 17455 | 0.2% | 0.2% | -0.1 | 15% | ❌ 15 pts to go |
| P12 | 7 | 0.0% | 0.0% | +0.0 | 15% | ❌ 15 pts to go |
| P13 | 17623 | 0.1% | 0.1% | +0.0 | 15% | ❌ 15 pts to go |

### `ap_system_hint`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 126 | 7.9% | 7.9% | +0.7 | 20% | ❌ 12 pts to go |
| P01T | 398 | 12.6% | 12.6% | -2.5 | 40% | ❌ 27 pts to go |
| P01_GOLD | 625 | 46.1% | 46.1% | +0.3 | 40% | ✅ met |
| P02 | 471 | 42.5% | 42.5% | -0.3 | 20% | ✅ met |
| P03 | 257 | 49.0% | 49.0% | +0.2 | 35% | ✅ met |
| P04 | 3823 | 13.8% | 13.8% | -1.6 | 20% | 🟡 6 pts to go |
| P05 | 422 | 14.9% | 14.9% | +0.1 | 20% | 🟡 5 pts to go |
| P06M | 13201 | 0.5% | 0.5% | +0.0 | 20% | ❌ 20 pts to go |
| P06T | 75065 | 0.6% | 0.6% | -0.1 | 20% | ❌ 19 pts to go |
| P06 | 295 | 22.0% | 22.0% | -0.1 | 20% | ✅ met |
| P07 | 793 | 7.3% | 7.3% | +0.2 | 20% | ❌ 13 pts to go |
| P08 | 25303 | 0.9% | 0.9% | +0.0 | 20% | ❌ 19 pts to go |
| P09 | 295 | 19.0% | 19.0% | +0.8 | 20% | 🟡 1 pts to go |
| P10R | 99941 | 0.2% | 0.2% | +0.0 | 20% | ❌ 20 pts to go |
| P10 | 2633 | 3.5% | 3.5% | +0.1 | 20% | ❌ 16 pts to go |
| P11 | 17455 | 0.6% | 0.6% | -0.4 | 20% | ❌ 19 pts to go |
| P12 | 7 | 0.0% | 0.0% | +0.0 | 20% | ❌ 20 pts to go |
| P13 | 17623 | 0.6% | 0.6% | +0.1 | 20% | ❌ 19 pts to go |

## 5. contract

### `contract_value`

> ceiling: rows proven by a lobbying filing, a news release, an auditor appointment, a customer story or a vendor's client list have no contract value by nature (≈17 % of P01 Gold); bids&tenders awards now carry the awarded bidder's submitted price when no award value was published

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 126 | 32.5% | 32.5% | -11.8 | n/a | no target |
| P01T | 398 | 0.3% | 0.3% | +0.0 | n/a | no target |
| P01_GOLD | 625 | 69.4% | 69.4% | -0.1 | 95% | ❌ 26 pts to go |
| P02 | 471 | 62.2% | 62.2% | -0.8 | 95% | ❌ 33 pts to go |
| P03 | 257 | 54.5% | 54.5% | -0.2 | 90% | ❌ 36 pts to go |
| P04 | 3823 | 24.2% | 24.2% | -2.9 | 85% | ❌ 61 pts to go |
| P05 | 422 | 37.2% | 37.2% | +0.7 | 75% | ❌ 38 pts to go |
| P06M | 13201 | 35.4% | 35.4% | -14.7 | n/a | no target |
| P06T | 75065 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06 | 295 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P07 | 793 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P08 | 25303 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P09 | 295 | 89.5% | 89.5% | +0.1 | 100% | ❌ 10 pts to go |
| P10R | 99941 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P10 | 2633 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P11 | 17455 | 0.5% | 0.5% | -0.4 | 60% | ❌ 60 pts to go |
| P12 | 7 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P13 | 17623 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `currency`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 126 | 32.5% | 32.5% | -11.8 | n/a | no target |
| P01T | 398 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P01_GOLD | 625 | 72.8% | 72.8% | +0.0 | 100% | ❌ 27 pts to go |
| P02 | 471 | 65.6% | 65.6% | -0.9 | 100% | ❌ 34 pts to go |
| P03 | 257 | 60.3% | 60.3% | -0.2 | n/a | no target |
| P04 | 3823 | 24.8% | 24.8% | -3.0 | 95% | ❌ 70 pts to go |
| P05 | 422 | 33.2% | 33.2% | +0.2 | 80% | ❌ 47 pts to go |
| P06M | 13201 | 35.4% | 35.4% | -14.7 | n/a | no target |
| P06T | 75065 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06 | 295 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P07 | 793 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P08 | 25303 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P09 | 295 | 92.5% | 92.5% | -0.2 | 100% | 🟡 8 pts to go |
| P10R | 99941 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P10 | 2633 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P11 | 17455 | 0.5% | 0.5% | -0.5 | n/a | no target |
| P12 | 7 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P13 | 17623 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `start_date`

> ceiling: most award notices publish an award date, not a start date; start_date carries the signature date when the source gives one, labelled

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 126 | 81.7% | 81.7% | +3.3 | n/a | no target |
| P01T | 398 | 0.3% | 0.3% | +0.0 | n/a | no target |
| P01_GOLD | 625 | 51.7% | 51.7% | +0.1 | 85% | ❌ 33 pts to go |
| P02 | 471 | 56.9% | 56.9% | -0.7 | 90% | ❌ 33 pts to go |
| P03 | 257 | 43.6% | 43.6% | -0.5 | 85% | ❌ 41 pts to go |
| P04 | 3823 | 27.2% | 27.2% | -3.2 | 90% | ❌ 63 pts to go |
| P05 | 422 | 33.4% | 33.4% | +0.6 | 75% | ❌ 42 pts to go |
| P06M | 13201 | 89.7% | 89.7% | -0.7 | n/a | no target |
| P06T | 75065 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06 | 295 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P07 | 793 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P08 | 25303 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P09 | 295 | 85.1% | 85.1% | +0.0 | 95% | 🟡 10 pts to go |
| P10R | 99941 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P10 | 2633 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P11 | 17455 | 0.4% | 0.4% | -0.4 | n/a | no target |
| P12 | 7 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P13 | 17623 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `end_date`

> ceiling: an inferred end (award date + published duration) is labelled as such; sources without a duration leave end_date empty — the honest ceiling. P09 is BY DEFINITION the rows whose end date is not published (older SEAO contracts with no closing notice): its end_date / duration targets cannot be met without inventing a date

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 126 | 81.0% | 81.0% | +1.6 | n/a | no target |
| P01T | 398 | 0.3% | 0.3% | +0.0 | n/a | no target |
| P01_GOLD | 625 | 51.8% | 51.8% | +0.0 | 85% | ❌ 33 pts to go |
| P02 | 471 | 52.0% | 52.0% | -0.7 | 90% | ❌ 38 pts to go |
| P03 | 257 | 44.7% | 44.7% | -0.6 | 85% | ❌ 40 pts to go |
| P04 | 3823 | 23.2% | 23.2% | -2.8 | 90% | ❌ 67 pts to go |
| P05 | 422 | 43.6% | 43.6% | +0.7 | 75% | ❌ 31 pts to go |
| P06M | 13201 | 80.5% | 80.5% | -3.2 | n/a | no target |
| P06T | 75065 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06 | 295 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P07 | 793 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P08 | 25303 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P09 | 295 | 0.3% | 0.3% | +0.0 | 95% | ❌ 95 pts to go |
| P10R | 99941 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P10 | 2633 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P11 | 17455 | 0.4% | 0.4% | -0.3 | n/a | no target |
| P12 | 7 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P13 | 17623 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `contract_title`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 126 | 90.5% | 90.5% | +4.9 | n/a | no target |
| P01T | 398 | 91.5% | 91.5% | -0.7 | n/a | no target |
| P01_GOLD | 625 | 85.4% | 85.4% | -0.1 | 100% | ❌ 15 pts to go |
| P02 | 471 | 74.7% | 74.7% | -1.0 | 100% | ❌ 25 pts to go |
| P03 | 257 | 91.4% | 91.4% | -0.8 | n/a | no target |
| P04 | 3823 | 45.8% | 45.8% | -5.7 | 95% | ❌ 49 pts to go |
| P05 | 422 | 77.3% | 77.3% | -0.5 | 95% | ❌ 18 pts to go |
| P06M | 13201 | 98.9% | 98.9% | +0.6 | n/a | no target |
| P06T | 75065 | 80.4% | 80.4% | -3.3 | n/a | no target |
| P06 | 295 | 25.8% | 25.8% | -0.4 | n/a | no target |
| P07 | 793 | 16.9% | 16.9% | -2.2 | n/a | no target |
| P08 | 25303 | 9.9% | 9.9% | -1.1 | n/a | no target |
| P09 | 295 | 98.6% | 98.6% | -0.1 | 100% | 🟡 1 pts to go |
| P10R | 99941 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P10 | 2633 | 71.3% | 71.3% | -0.4 | n/a | no target |
| P11 | 17455 | 9.7% | 9.7% | -6.4 | n/a | no target |
| P12 | 7 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P13 | 17623 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `contract_description`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 126 | 90.5% | 90.5% | +4.9 | n/a | no target |
| P01T | 398 | 91.5% | 91.5% | -0.7 | n/a | no target |
| P01_GOLD | 625 | 88.6% | 88.6% | -0.1 | 100% | ❌ 11 pts to go |
| P02 | 471 | 75.8% | 76.0% | -1.0 | 100% | ❌ 24 pts to go |
| P03 | 257 | 92.2% | 92.2% | -0.8 | n/a | no target |
| P04 | 3823 | 49.0% | 49.0% | -6.1 | 95% | ❌ 46 pts to go |
| P05 | 422 | 89.8% | 89.8% | -0.4 | 70% | ✅ met |
| P06M | 13201 | 98.9% | 98.9% | +0.6 | n/a | no target |
| P06T | 75065 | 80.4% | 80.4% | -3.3 | n/a | no target |
| P06 | 295 | 25.8% | 25.8% | -0.4 | n/a | no target |
| P07 | 793 | 16.9% | 16.9% | -2.2 | n/a | no target |
| P08 | 25303 | 9.9% | 9.9% | -1.1 | n/a | no target |
| P09 | 295 | 98.6% | 98.6% | -0.1 | 100% | 🟡 1 pts to go |
| P10R | 99941 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P10 | 2633 | 71.3% | 71.3% | -0.4 | n/a | no target |
| P11 | 17455 | 9.7% | 9.7% | -6.4 | n/a | no target |
| P12 | 7 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P13 | 17623 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `number_of_bids`

> ceiling: published by some portals only (bids&tenders submission lists, Biddingo bidder lists); federal proactive disclosure does not publish bid counts

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 126 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P01T | 398 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P01_GOLD | 625 | 16.8% | 16.8% | +0.0 | 60% | ❌ 43 pts to go · rows from a source that publishes bids: 363 rows, 28.9% filled |
| P02 | 471 | 11.0% | 11.0% | -0.2 | n/a | no target · rows from a source that publishes bids: 290 rows, 17.9% filled |
| P03 | 257 | 13.2% | 13.2% | -0.1 | n/a | no target · rows from a source that publishes bids: 139 rows, 24.5% filled |
| P04 | 3823 | 1.4% | 1.4% | -0.2 | n/a | no target · rows from a source that publishes bids: 872 rows, 6.3% filled |
| P05 | 422 | 2.8% | 2.8% | -0.2 | n/a | no target · rows from a source that publishes bids: 51 rows, 23.5% filled |
| P06M | 13201 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06T | 75065 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06 | 295 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P07 | 793 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P08 | 25303 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P09 | 295 | 3.1% | 3.1% | +0.1 | n/a | no target · rows from a source that publishes bids: 282 rows, 3.2% filled |
| P10R | 99941 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P10 | 2633 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P11 | 17455 | 0.1% | 0.1% | +0.0 | n/a | no target · rows from a source that publishes bids: 88 rows, 13.6% filled |
| P12 | 7 | 0.0% | 0.0% | +0.0 | n/a | no target · rows from a source that publishes bids: 7 rows, 0.0% filled |
| P13 | 17623 | 0.0% | 0.0% | +0.0 | n/a | no target |

## 6. history

### `average_contract_duration_days`

> ceiling: needs two dates (or a published term) on the buyer's records; P09 rows (end date unpublished by definition) and buyers whose sources publish award dates only have no honest duration

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 126 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P01T | 398 | 0.3% | 98.5% | +0.0 | n/a | no target |
| P01_GOLD | 625 | 53.3% | 82.4% | +0.1 | 90% | ❌ 37 pts to go |
| P02 | 471 | 51.8% | 87.7% | -0.7 | 90% | ❌ 38 pts to go |
| P03 | 257 | 45.5% | 80.2% | -0.2 | 90% | ❌ 44 pts to go |
| P04 | 3823 | 18.7% | 94.1% | -2.2 | 90% | ❌ 71 pts to go |
| P05 | 422 | 0.0% | 83.2% | +0.0 | 90% | ❌ 90 pts to go |
| P06M | 13201 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P06T | 75065 | 0.0% | 99.9% | +0.0 | n/a | no target |
| P06 | 295 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P07 | 793 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P08 | 25303 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P09 | 295 | 2.4% | 4.1% | +0.1 | 90% | ❌ 88 pts to go |
| P10R | 99941 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P10 | 2633 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P11 | 17455 | 0.3% | 99.8% | -0.3 | n/a | no target |
| P12 | 7 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P13 | 17623 | 0.0% | 100.0% | +0.0 | n/a | no target |

### `commodity_distribution_top3`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 126 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P01T | 398 | 0.5% | 98.7% | -0.1 | n/a | no target |
| P01_GOLD | 625 | 25.9% | 55.0% | +0.0 | 90% | ❌ 64 pts to go |
| P02 | 471 | 51.0% | 86.8% | -0.6 | n/a | no target |
| P03 | 257 | 24.9% | 59.5% | -0.1 | n/a | no target |
| P04 | 3823 | 20.4% | 95.8% | -2.5 | n/a | no target |
| P05 | 422 | 0.5% | 83.6% | +0.0 | n/a | no target |
| P06M | 13201 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P06T | 75065 | 0.1% | 100.0% | +0.0 | n/a | no target |
| P06 | 295 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P07 | 793 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P08 | 25303 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P09 | 295 | 41.4% | 43.1% | -0.5 | n/a | no target |
| P10R | 99941 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P10 | 2633 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P11 | 17455 | 0.3% | 99.7% | -0.3 | n/a | no target |
| P12 | 7 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P13 | 17623 | 0.0% | 100.0% | +0.0 | n/a | no target |

### `year_over_year_spend_trend`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 126 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P01T | 398 | 1.5% | 99.7% | +0.0 | n/a | no target |
| P01_GOLD | 625 | 51.8% | 81.0% | +0.0 | 95% | ❌ 43 pts to go |
| P02 | 471 | 55.8% | 91.7% | -0.8 | n/a | no target |
| P03 | 257 | 47.9% | 82.5% | -0.1 | n/a | no target |
| P04 | 3823 | 20.6% | 96.1% | -2.5 | n/a | no target |
| P05 | 422 | 4.5% | 87.7% | -0.2 | n/a | no target |
| P06M | 13201 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P06T | 75065 | 0.1% | 100.0% | +0.0 | n/a | no target |
| P06 | 295 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P07 | 793 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P08 | 25303 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P09 | 295 | 63.7% | 65.4% | -0.3 | n/a | no target |
| P10R | 99941 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P10 | 2633 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P11 | 17455 | 0.3% | 99.8% | -0.3 | n/a | no target |
| P12 | 7 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P13 | 17623 | 0.0% | 100.0% | +0.0 | n/a | no target |

## 7. mail security

### `mta_sts`

> ceiling: DNS-only check; 'no record' counts as checked

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 126 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P01T | 398 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P01_GOLD | 625 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P02 | 471 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P03 | 257 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P04 | 3823 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P05 | 422 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P06M | 13201 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P06T | 75065 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P06 | 295 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P07 | 793 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P08 | 25303 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P09 | 295 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P10R | 99941 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P10 | 2633 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P11 | 17455 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P12 | 7 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P13 | 17623 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |

### `tls_rpt`

> ceiling: DNS-only check; 'no record' counts as checked

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 126 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P01T | 398 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P01_GOLD | 625 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P02 | 471 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P03 | 257 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P04 | 3823 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P05 | 422 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P06M | 13201 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P06T | 75065 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P06 | 295 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P07 | 793 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P08 | 25303 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P09 | 295 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P10R | 99941 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P10 | 2633 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P11 | 17455 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P12 | 7 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P13 | 17623 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |

### `bimi`

> ceiling: DNS-only check; 'no record' counts as checked

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 126 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P01T | 398 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P01_GOLD | 625 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P02 | 471 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P03 | 257 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P04 | 3823 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P05 | 422 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P06M | 13201 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P06T | 75065 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P06 | 295 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P07 | 793 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P08 | 25303 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P09 | 295 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P10R | 99941 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P10 | 2633 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P11 | 17455 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P12 | 7 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P13 | 17623 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |

