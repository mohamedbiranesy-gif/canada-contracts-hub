# Coverage vs the downstream team's targets — 2026-11-11

Benchmarks (field × package with a numeric target): **94 of 446 met** (21.1%); 57 within 10 points; 295 further away.
A cell counts as filled only when it carries a value: blank, `not_published`, `not_found_yet` and label-only cells ("no identifier published …", "no dataset record …", "0 in the contract dataset …") do not count; the DNS checks count when checked. `any` = share of non-blank cells incl. such labels. Δ = change since the previous build in `coord/results/coverage_history.csv`.
Rows per package: P01M 125, P01T 398, P01_GOLD 625, P02 471, P03 257, P04 3833, P05 422, P06M 13084, P06T 74208, P06 295, P07 800, P08 25539, P09 295, P10R 100545, P10 2642, P11 17418, P12 7, P13 17697

## Invoice-grade readiness (the row as an invoice header: bill-to, submit-to, references, terms, tax, vendor identity, follow-up)

| package | rows | all 11 elements | ≥ 9 of 11 | median elements | most-missing element |
|---|---|---|---|---|---|
| P01M | 125 | 0.0% | 14.4% | 8 | vendor GST/HST number (114 rows) |
| P01T | 398 | 0.8% | 20.6% | 7 | payment terms (324 rows) |
| P01_GOLD | 625 | 24.2% | 70.7% | 9 | payment terms (214 rows) |
| P02 | 471 | 7.2% | 54.1% | 9 | PO rule (360 rows) |
| P03 | 257 | 14.8% | 58.0% | 9 | PO rule (123 rows) |
| P04 | 3833 | 1.2% | 16.0% | 6 | PO rule (3642 rows) |
| P05 | 422 | 1.2% | 17.3% | 7 | payment terms (347 rows) |
| P06M | 13084 | 0.0% | 1.3% | 7 | PO rule (13051 rows) |
| P06T | 74208 | 0.0% | 3.5% | 7 | PO rule (73859 rows) |
| P06 | 295 | 0.0% | 8.5% | 6 | reference to quote (PO / contract / vendor id) (295 rows) |
| P07 | 800 | 0.0% | 1.9% | 6 | reference to quote (PO / contract / vendor id) (800 rows) |
| P08 | 25539 | 0.0% | 0.3% | 5 | reference to quote (PO / contract / vendor id) (25539 rows) |
| P09 | 295 | 1.0% | 44.4% | 8 | payment terms (276 rows) |
| P10R | 100545 | 0.0% | 21.6% | 7 | PO rule (100508 rows) |
| P10 | 2642 | 0.0% | 1.0% | 5 | reference to quote (PO / contract / vendor id) (2642 rows) |
| P11 | 17418 | 0.0% | 1.7% | 7 | PO rule (17311 rows) |
| P12 | 7 | 0.0% | 28.6% | 8 | PO rule (7 rows) |
| P13 | 17697 | 0.0% | 0.2% | 7 | reference to quote (PO / contract / vendor id) (17697 rows) |

## AP grade (how stringently the row's accounts-payable data meets what an invoice needs; A = invoicing mailbox referee-confirmed on the buyer's own domain with MX, legal name, address, PO rule and terms all published, no penalties)

| package | rows | A | B | C | D | E | median ap_score |
|---|---|---|---|---|---|---|---|
| P01M | 125 | 9 | 12 | 104 | 0 | 0 | 71 |
| P01T | 398 | 31 | 63 | 304 | 0 | 0 | 68 |
| P01_GOLD | 625 | 227 | 194 | 204 | 0 | 0 | 82 |
| P02 | 471 | 0 | 193 | 278 | 0 | 0 | 66 |
| P03 | 257 | 0 | 0 | 246 | 11 | 0 | 57 |
| P04 | 3833 | 0 | 0 | 3220 | 613 | 0 | 46 |
| P05 | 422 | 15 | 30 | 363 | 14 | 0 | 51 |
| P06M | 13084 | 0 | 3 | 13018 | 63 | 0 | 46 |
| P06T | 74208 | 0 | 41 | 61260 | 12907 | 0 | 38 |
| P06 | 295 | 20 | 49 | 226 | 0 | 0 | 69 |
| P07 | 800 | 0 | 28 | 749 | 23 | 0 | 53 |
| P08 | 25539 | 0 | 0 | 21796 | 3743 | 0 | 43 |
| P09 | 295 | 3 | 12 | 278 | 2 | 0 | 53 |
| P10R | 100545 | 2 | 12 | 70725 | 29806 | 0 | 38 |
| P10 | 2642 | 2 | 15 | 1996 | 629 | 0 | 43 |
| P11 | 17418 | 6 | 12 | 42 | 0 | 17358 | 23 |
| P12 | 7 | 0 | 0 | 7 | 0 | 0 | 54 |
| P13 | 17697 | 0 | 16 | 14491 | 3190 | 0 | 43 |

### AP payability (confirmed channel + bill-to legal name and address + the buyer's reference rule + tax treatment known)

| package | rows | payable today | % | most common gap |
|---|---|---|---|---|
| P01M | 125 | 102 | 81.6% | the buyer's PO / reference rule (13) |
| P01T | 398 | 217 | 54.5% | bill-to legal name and address (134) |
| P01_GOLD | 625 | 467 | 74.7% | bill-to legal name and address (103) |
| P02 | 471 | 313 | 66.5% | the buyer's PO / reference rule (89) |
| P03 | 257 | 0 | 0.0% | a confirmed invoicing / AP or finance channel (257) |
| P04 | 3833 | 0 | 0.0% | a confirmed invoicing / AP or finance channel (3833) |
| P05 | 422 | 46 | 10.9% | a confirmed invoicing / AP or finance channel (335) |
| P06M | 13084 | 127 | 1.0% | a confirmed invoicing / AP or finance channel (12909) |
| P06T | 74208 | 451 | 0.6% | a confirmed invoicing / AP or finance channel (73113) |
| P06 | 295 | 44 | 14.9% | the buyer's PO / reference rule (132) |
| P07 | 800 | 10 | 1.2% | bill-to legal name and address (336) |
| P08 | 25539 | 0 | 0.0% | a confirmed invoicing / AP or finance channel (25539) |
| P09 | 295 | 41 | 13.9% | a confirmed invoicing / AP or finance channel (245) |
| P10R | 100545 | 529 | 0.5% | a confirmed invoicing / AP or finance channel (99382) |
| P10 | 2642 | 5 | 0.2% | a confirmed invoicing / AP or finance channel (2546) |
| P11 | 17418 | 12 | 0.1% | a confirmed invoicing / AP or finance channel (17358) |
| P12 | 7 | 3 | 42.9% | a confirmed invoicing / AP or finance channel (4) |
| P13 | 17697 | 7 | 0.0% | a confirmed invoicing / AP or finance channel (17354) |

### Pay on sight (an invoice generated from the row would clear AP: confirmed invoicing / AP or finance channel, bill-to legal name + address, vendor legal name + GST/HST number + remit-to address, tax treatment and currency known — published or labelled-derived; the buyer's reference rule is reported separately)

| package | rows | pay on sight | % | + reference rule not published | routed (general inbox only) | most common gap |
|---|---|---|---|---|---|---|
| P01M | 125 | 5 | 4.0% | 5 | 0 | the vendor's GST/HST number (BN9) (114) |
| P01T | 398 | 72 | 18.1% | 26 | 0 | the vendor's GST/HST number (BN9) (223) |
| P01_GOLD | 625 | 396 | 63.4% | 12 | 0 | the vendor's GST/HST number (BN9) (154) |
| P02 | 471 | 211 | 44.8% | 23 | 0 | the vendor's GST/HST number (BN9) (206) |
| P03 | 257 | 16 | 6.2% | 0 | 132 | an invoicing / AP or finance mailbox (only a purchasing / general inbo (88) |
| P04 | 3833 | 42 | 1.1% | 8 | 810 | an invoicing / AP or finance mailbox (only a purchasing / general inbo (2917) |
| P05 | 422 | 20 | 4.7% | 7 | 109 | an invoicing / AP or finance mailbox (only a purchasing / general inbo (219) |
| P06M | 13084 | 1 | 0.0% | 10 | 147 | an invoicing / AP or finance mailbox (only a purchasing / general inbo (12742) |
| P06T | 74208 | 102 | 0.1% | 103 | 13688 | an invoicing / AP or finance mailbox (only a purchasing / general inbo (59264) |
| P06 | 295 | 16 | 5.4% | 30 | 0 | the vendor's GST/HST number (BN9) (174) |
| P07 | 800 | 5 | 0.6% | 75 | 29 | the vendor's GST/HST number (BN9) (422) |
| P08 | 25539 | 1 | 0.0% | 8 | 2930 | an invoicing / AP or finance mailbox (only a purchasing / general inbo (22546) |
| P09 | 295 | 38 | 12.9% | 1 | 119 | an invoicing / AP or finance mailbox (only a purchasing / general inbo (117) |
| P10R | 100545 | 865 | 0.9% | 0 | 54071 | an invoicing / AP or finance mailbox (only a purchasing / general inbo (45252) |
| P10 | 2642 | 4 | 0.2% | 21 | 387 | an invoicing / AP or finance mailbox (only a purchasing / general inbo (2129) |
| P11 | 17418 | 11 | 0.1% | 12 | 0 | a confirmed invoicing / AP or finance channel (17325) |
| P12 | 7 | 1 | 14.3% | 0 | 2 | the vendor's GST/HST number (BN9) (2) |
| P13 | 17697 | 9 | 0.1% | 246 | 10391 | an invoicing / AP or finance mailbox (only a purchasing / general inbo (6924) |
| **all** | 258661 | 1815 | 0.7% | 587 | 82815 | |

### What still blocks grade A (rows per missing element; a row counts under every element it lacks)

| package | rows not A | referee confirmation of the mailbox | an invoicing / AP mailbox (not finance / procurement / general) | a mailbox on the buyer's own domain | MX record for the mailbox domain | published bill-to legal name | invoice / billing address | published PO rule | published payment terms | clear the penalty |
|---|---|---|---|---|---|---|---|---|---|---|
| P01M | 116 | 0 | 0 | 0 | 61 | 7 | 0 | 107 | 111 | 1 |
| P01T | 367 | 0 | 0 | 0 | 177 | 118 | 36 | 310 | 326 | 30 |
| P01_GOLD | 398 | 0 | 0 | 0 | 11 | 84 | 33 | 194 | 228 | 57 |
| P02 | 471 | 0 | 471 | 0 | 47 | 59 | 19 | 360 | 290 | 22 |
| P03 | 257 | 0 | 257 | 0 | 15 | 43 | 24 | 123 | 129 | 25 |
| P04 | 3833 | 0 | 3833 | 0 | 1807 | 1484 | 924 | 3642 | 3383 | 131 |
| P05 | 407 | 0 | 355 | 0 | 74 | 91 | 47 | 338 | 349 | 50 |
| P06M | 13084 | 0 | 13084 | 0 | 8245 | 1344 | 111 | 13051 | 13013 | 78 |
| P06T | 74208 | 0 | 74208 | 0 | 58662 | 41755 | 17105 | 73859 | 72718 | 445 |
| P06 | 275 | 0 | 0 | 0 | 117 | 82 | 51 | 208 | 238 | 4 |
| P07 | 800 | 0 | 800 | 0 | 473 | 360 | 135 | 751 | 752 | 14 |
| P08 | 25539 | 0 | 25539 | 0 | 18753 | 12893 | 5221 | 25303 | 24979 | 225 |
| P09 | 292 | 0 | 271 | 0 | 9 | 68 | 2 | 266 | 278 | 44 |
| P10R | 100543 | 0 | 100369 | 0 | 78464 | 62872 | 39731 | 100508 | 100364 | 24 |
| P10 | 2640 | 0 | 2603 | 0 | 1270 | 1304 | 910 | 2575 | 2525 | 115 |
| P11 | 17412 | 17358 | 17294 | 0 | 15932 | 10299 | 1030 | 17311 | 16863 | 39 |
| P12 | 7 | 0 | 6 | 0 | 0 | 2 | 0 | 7 | 7 | 0 |
| P13 | 17697 | 0 | 17596 | 0 | 8913 | 9111 | 4065 | 17662 | 17655 | 19 |

## Where the work is (largest gaps in rows still needed)

| field | package | now | target | rows needed |
|---|---|---|---|---|
| buyer_ap_cycle_published | P10R | 0.0% | 20% | 20082 |
| ap_system_hint | P10R | 0.2% | 20% | 19909 |
| buyer_tax_exempt_status | P10R | 0.0% | 15% | 15055 |
| buyer_esignature_preference | P10R | 0.0% | 15% | 15035 |
| buyer_ap_cycle_published | P06T | 0.0% | 20% | 14816 |
| buyer_payment_method_preference | P10R | 0.6% | 15% | 14445 |
| vendor_registered_address | P08 | 13.6% | 70% | 14401 |
| ap_system_hint | P06T | 0.6% | 20% | 14371 |
| vendor_phone | P11 | 4.5% | 75% | 12273 |
| vendor_emails | P11 | 3.4% | 70% | 11601 |
| buyer_esignature_preference | P06T | 0.2% | 15% | 10990 |
| buyer_tax_exempt_status | P06T | 0.3% | 15% | 10939 |
| buyer_payment_method_preference | P06T | 0.6% | 15% | 10674 |
| contract_value | P11 | 0.5% | 60% | 10366 |
| award_or_notice_id | P11 | 0.5% | 60% | 10365 |
| contract_or_agreement_number | P11 | 8.5% | 60% | 8972 |
| invoice_reference_hint | P11 | 9.0% | 60% | 8883 |
| vendor_bn9 | P08 | 15.6% | 50% | 8794 |
| commodity_codes | P11 | 0.4% | 50% | 8648 |
| buyer_phone | P11 | 27.9% | 75% | 8205 |
| buyer_phone | P08 | 63.7% | 95% | 7990 |
| solicitation_or_tender_number | P11 | 0.5% | 40% | 6889 |
| buyer_legal_name_as_published | P08 | 49.5% | 75% | 6509 |
| buyer_phone | P13 | 60.0% | 95% | 6192 |
| invoice_reference_hint | P08 | 0.9% | 25% | 6149 |
| vendor_phone | P08 | 61.7% | 85% | 5953 |
| vendor_emails | P08 | 51.8% | 75% | 5927 |
| buyer_bn_as_published | P08 | 13.8% | 35% | 5418 |
| buyer_logo_url | P13 | 65.2% | 95% | 5266 |
| buyer_ap_cycle_published | P08 | 0.0% | 20% | 5100 |
| buyer_logo_url | P08 | 80.2% | 100% | 5049 |
| ap_system_hint | P08 | 0.8% | 20% | 4892 |
| buyer_legal_name_as_published | P11 | 40.9% | 65% | 4203 |
| vendor_trading_name | P08 | 33.9% | 50% | 4119 |
| vendor_logo_url | P08 | 84.3% | 100% | 4008 |
| buyer_address | P08 | 79.5% | 95% | 3950 |
| buyer_esignature_preference | P08 | 0.4% | 15% | 3741 |
| buyer_tax_exempt_status | P08 | 0.4% | 15% | 3734 |
| buyer_payment_method_preference | P08 | 0.6% | 15% | 3686 |
| buyer_ap_cycle_published | P13 | 0.0% | 20% | 3538 |

## 1. identifiers

### `invoice_reference_hint`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 125 | 88.0% | 88.0% | -0.7 | 50% | ✅ met |
| P01T | 398 | 89.4% | 89.4% | -0.1 | 50% | ✅ met |
| P01_GOLD | 625 | 92.2% | 94.4% | +0.0 | 95% | 🟡 3 pts to go |
| P02 | 471 | 72.8% | 74.3% | -1.0 | 95% | ❌ 22 pts to go |
| P03 | 257 | 81.7% | 84.8% | -0.3 | 95% | ❌ 13 pts to go |
| P04 | 3833 | 29.0% | 30.4% | -3.8 | 90% | ❌ 61 pts to go |
| P05 | 422 | 38.9% | 41.7% | +0.3 | 70% | ❌ 31 pts to go |
| P06M | 13084 | 91.1% | 91.1% | -1.5 | n/a | no target |
| P06T | 74208 | 79.8% | 79.8% | -0.5 | n/a | no target |
| P06 | 295 | 29.5% | 29.5% | -2.2 | 30% | 🟡 0 pts to go |
| P07 | 800 | 6.1% | 6.1% | -0.8 | 30% | ❌ 24 pts to go |
| P08 | 25539 | 0.9% | 0.9% | -0.2 | 25% | ❌ 24 pts to go |
| P09 | 295 | 99.0% | 99.7% | +0.0 | 100% | 🟡 1 pts to go |
| P10R | 100545 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P10 | 2642 | 2.5% | 2.6% | -0.1 | 25% | ❌ 22 pts to go |
| P11 | 17418 | 9.0% | 9.1% | -4.6 | 60% | ❌ 51 pts to go |
| P12 | 7 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P13 | 17697 | 0.2% | 0.2% | +0.0 | 0% by design | — leave (by design) |

### `po_number_as_published`

> ceiling: a purchase-order number exists only where the buyer publishes PO-level data (Montréal, Laval, Toronto open data so far) or the record itself carries one; most sources publish awards, not POs — the target cannot be reached from public data for most buyers

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 125 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P01T | 398 | 0.0% | 0.0% | +0.0 | 10% | 🟡 10 pts to go |
| P01_GOLD | 625 | 6.1% | 6.1% | +0.0 | 50% | ❌ 44 pts to go |
| P02 | 471 | 6.2% | 6.2% | +0.0 | 50% | ❌ 44 pts to go |
| P03 | 257 | 1.6% | 1.6% | +0.0 | 40% | ❌ 38 pts to go |
| P04 | 3833 | 0.5% | 0.5% | +0.0 | 30% | ❌ 30 pts to go |
| P05 | 422 | 0.2% | 0.2% | +0.0 | 20% | ❌ 20 pts to go |
| P06M | 13084 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06T | 74208 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06 | 295 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P07 | 800 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P08 | 25539 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P09 | 295 | 0.7% | 0.7% | +0.0 | 50% | ❌ 49 pts to go |
| P10R | 100545 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P10 | 2642 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P11 | 17418 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P12 | 7 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P13 | 17697 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `contract_or_agreement_number`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 125 | 83.2% | 83.2% | +1.8 | n/a | no target |
| P01T | 398 | 73.6% | 73.6% | +3.1 | 50% | ✅ met |
| P01_GOLD | 625 | 66.9% | 66.9% | +0.0 | 85% | ❌ 18 pts to go |
| P02 | 471 | 64.1% | 64.1% | -0.8 | 90% | ❌ 26 pts to go |
| P03 | 257 | 61.1% | 61.1% | -0.2 | 85% | ❌ 24 pts to go |
| P04 | 3833 | 26.8% | 26.8% | -3.3 | 85% | ❌ 58 pts to go |
| P05 | 422 | 29.1% | 29.1% | +0.1 | 60% | ❌ 31 pts to go |
| P06M | 13084 | 91.0% | 91.0% | -1.4 | n/a | no target |
| P06T | 74208 | 79.6% | 79.6% | -0.4 | n/a | no target |
| P06 | 295 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P07 | 800 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P08 | 25539 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P09 | 295 | 95.9% | 95.9% | -0.1 | 100% | 🟡 4 pts to go |
| P10R | 100545 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P10 | 2642 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P11 | 17418 | 8.5% | 8.5% | -4.2 | 60% | ❌ 52 pts to go |
| P12 | 7 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P13 | 17697 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `solicitation_or_tender_number`

> ceiling: SEAO's 'numero' is the organisation's own reference for the notice (SEAO data dictionary) and is reported here; sources that publish awards under a tender number only (bids&tenders, SaskTenders, BC) also carry it as the contract reference, labelled

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 125 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P01T | 398 | 0.0% | 0.0% | +0.0 | 30% | ❌ 30 pts to go |
| P01_GOLD | 625 | 50.7% | 50.7% | +0.1 | 80% | ❌ 29 pts to go |
| P02 | 471 | 56.3% | 56.3% | -0.7 | 60% | 🟡 4 pts to go |
| P03 | 257 | 51.4% | 51.4% | -0.2 | 80% | ❌ 29 pts to go |
| P04 | 3833 | 22.2% | 22.2% | -2.8 | 50% | ❌ 28 pts to go |
| P05 | 422 | 11.6% | 11.6% | -0.3 | 40% | ❌ 28 pts to go |
| P06M | 13084 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06T | 74208 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06 | 295 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P07 | 800 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P08 | 25539 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P09 | 295 | 83.1% | 83.1% | -0.4 | 50% | ✅ met |
| P10R | 100545 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P10 | 2642 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P11 | 17418 | 0.5% | 0.5% | -0.3 | 40% | ❌ 40 pts to go |
| P12 | 7 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P13 | 17697 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `award_or_notice_id`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 125 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P01T | 398 | 0.3% | 0.3% | +0.0 | n/a | no target |
| P01_GOLD | 625 | 60.5% | 60.5% | +0.1 | 85% | ❌ 24 pts to go |
| P02 | 471 | 55.6% | 55.6% | -0.7 | 90% | ❌ 34 pts to go |
| P03 | 257 | 59.9% | 59.9% | -0.3 | 85% | ❌ 25 pts to go |
| P04 | 3833 | 23.0% | 23.0% | -2.8 | 85% | ❌ 62 pts to go |
| P05 | 422 | 19.9% | 19.9% | +0.0 | 50% | ❌ 30 pts to go |
| P06M | 13084 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06T | 74208 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06 | 295 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P07 | 800 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P08 | 25539 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P09 | 295 | 96.9% | 96.9% | -0.1 | 100% | 🟡 3 pts to go |
| P10R | 100545 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P10 | 2642 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P11 | 17418 | 0.5% | 0.5% | -0.4 | 60% | ❌ 60 pts to go |
| P12 | 7 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P13 | 17697 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `buyer_vendor_id`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 125 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P01T | 398 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P01_GOLD | 625 | 13.0% | 13.0% | +0.1 | 60% | ❌ 47 pts to go |
| P02 | 471 | 5.9% | 5.9% | -0.1 | 50% | ❌ 44 pts to go |
| P03 | 257 | 8.6% | 8.6% | +0.0 | 50% | ❌ 41 pts to go |
| P04 | 3833 | 1.8% | 1.8% | -0.2 | 40% | ❌ 38 pts to go |
| P05 | 422 | 0.7% | 0.7% | -0.2 | 20% | ❌ 19 pts to go |
| P06M | 13084 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06T | 74208 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06 | 295 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P07 | 800 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P08 | 25539 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P09 | 295 | 2.4% | 2.4% | +0.1 | 50% | ❌ 48 pts to go |
| P10R | 100545 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P10 | 2642 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P11 | 17418 | 0.1% | 0.1% | +0.0 | n/a | no target |
| P12 | 7 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P13 | 17697 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `commodity_codes`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 125 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P01T | 398 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P01_GOLD | 625 | 34.9% | 34.9% | +0.1 | 80% | ❌ 45 pts to go |
| P02 | 471 | 51.4% | 51.4% | -0.6 | 90% | ❌ 39 pts to go |
| P03 | 257 | 33.5% | 33.5% | -0.1 | 80% | ❌ 46 pts to go |
| P04 | 3833 | 21.0% | 21.0% | -2.6 | 85% | ❌ 64 pts to go |
| P05 | 422 | 5.5% | 5.5% | +0.1 | 50% | ❌ 44 pts to go |
| P06M | 13084 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06T | 74208 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06 | 295 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P07 | 800 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P08 | 25539 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P09 | 295 | 75.6% | 75.6% | -0.3 | 95% | ❌ 19 pts to go |
| P10R | 100545 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P10 | 2642 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P11 | 17418 | 0.4% | 0.4% | -0.2 | 50% | ❌ 50 pts to go |
| P12 | 7 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P13 | 17697 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `buyer_org_codes`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 125 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P01T | 398 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P01_GOLD | 625 | 8.5% | 8.5% | +0.0 | 50% | ❌ 42 pts to go |
| P02 | 471 | 6.2% | 6.2% | +0.0 | 50% | ❌ 44 pts to go |
| P03 | 257 | 1.9% | 1.9% | -0.1 | 30% | ❌ 28 pts to go |
| P04 | 3833 | 0.4% | 0.4% | -0.1 | 30% | ❌ 30 pts to go |
| P05 | 422 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06M | 13084 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06T | 74208 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06 | 295 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P07 | 800 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P08 | 25539 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P09 | 295 | 0.3% | 0.3% | +0.0 | n/a | no target |
| P10R | 100545 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P10 | 2642 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P11 | 17418 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P12 | 7 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P13 | 17697 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `records_with_this_vendor`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 125 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P01T | 398 | 100.0% | 100.0% | +0.0 | 60% | ✅ met |
| P01_GOLD | 625 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P02 | 471 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P03 | 257 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P04 | 3833 | 100.0% | 100.0% | +0.0 | 95% | ✅ met |
| P05 | 422 | 100.0% | 100.0% | +0.0 | 70% | ✅ met |
| P06M | 13084 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P06T | 74208 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P06 | 295 | 100.0% | 100.0% | +0.0 | 50% | ✅ met |
| P07 | 800 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P08 | 25539 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P09 | 295 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P10R | 100545 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P10 | 2642 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P11 | 17418 | 100.0% | 100.0% | +0.0 | 70% | ✅ met |
| P12 | 7 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P13 | 17697 | 0.0% | 0.0% | +0.0 | n/a | no target |

## 2. vendor

### `vendor_bn9`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 125 | 8.8% | 8.8% | -5.6 | 70% | ❌ 61 pts to go |
| P01T | 398 | 31.4% | 31.4% | -2.3 | 60% | ❌ 29 pts to go |
| P01_GOLD | 625 | 72.6% | 72.6% | -0.4 | 90% | ❌ 17 pts to go |
| P02 | 471 | 53.5% | 53.5% | -1.6 | 85% | ❌ 32 pts to go |
| P03 | 257 | 68.1% | 68.1% | -1.8 | 90% | ❌ 22 pts to go |
| P04 | 3833 | 31.4% | 31.4% | -1.1 | 75% | ❌ 44 pts to go |
| P05 | 422 | 50.2% | 50.2% | +0.3 | 50% | ✅ met |
| P06M | 13084 | 1.6% | 1.6% | -0.2 | n/a | no target |
| P06T | 74208 | 22.3% | 22.3% | +5.0 | n/a | no target |
| P06 | 295 | 25.4% | 25.4% | +2.6 | 40% | ❌ 15 pts to go |
| P07 | 800 | 19.5% | 19.5% | +3.1 | 50% | ❌ 30 pts to go |
| P08 | 25539 | 15.6% | 15.6% | +4.7 | 50% | ❌ 34 pts to go |
| P09 | 295 | 58.3% | 58.3% | +0.5 | 80% | ❌ 22 pts to go |
| P10R | 100545 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P10 | 2642 | 31.2% | 31.2% | +2.5 | 40% | 🟡 9 pts to go |
| P11 | 17418 | 94.1% | 94.1% | +3.0 | 60% | ✅ met |
| P12 | 7 | 42.9% | 42.9% | -19.6 | 85% | ❌ 42 pts to go |
| P13 | 17697 | 90.6% | 90.6% | -0.4 | 0% by design | — leave (by design) |

### `vendor_registered_address`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 125 | 55.2% | 55.2% | -11.8 | n/a | no target |
| P01T | 398 | 39.4% | 39.4% | +1.4 | n/a | no target |
| P01_GOLD | 625 | 70.6% | 70.6% | +0.2 | 95% | ❌ 24 pts to go |
| P02 | 471 | 73.0% | 73.0% | -0.8 | 95% | ❌ 22 pts to go |
| P03 | 257 | 71.2% | 71.2% | -0.7 | 95% | ❌ 24 pts to go |
| P04 | 3833 | 43.6% | 43.6% | -2.0 | 95% | ❌ 51 pts to go |
| P05 | 422 | 53.1% | 53.1% | -0.3 | 70% | ❌ 17 pts to go |
| P06M | 13084 | 42.9% | 42.9% | -11.7 | n/a | no target |
| P06T | 74208 | 31.2% | 31.2% | +0.9 | n/a | no target |
| P06 | 295 | 25.8% | 25.8% | +1.0 | 80% | ❌ 54 pts to go |
| P07 | 800 | 18.2% | 18.2% | +0.2 | 70% | ❌ 52 pts to go |
| P08 | 25539 | 13.6% | 13.6% | -0.5 | 70% | ❌ 56 pts to go |
| P09 | 295 | 87.1% | 87.1% | -0.4 | 100% | ❌ 13 pts to go |
| P10R | 100545 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P10 | 2642 | 32.6% | 32.6% | +0.1 | 70% | ❌ 37 pts to go |
| P11 | 17418 | 94.6% | 94.6% | +2.4 | 75% | ✅ met |
| P12 | 7 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P13 | 17697 | 16.1% | 16.1% | +16.1 | n/a | no target |

### `vendor_trading_name`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 125 | 18.4% | 18.4% | +1.9 | n/a | no target |
| P01T | 398 | 53.3% | 53.3% | +27.4 | n/a | no target |
| P01_GOLD | 625 | 49.9% | 49.9% | +2.0 | 60% | ❌ 10 pts to go |
| P02 | 471 | 55.0% | 55.0% | -0.3 | 60% | 🟡 5 pts to go |
| P03 | 257 | 54.9% | 54.9% | -0.2 | 60% | 🟡 5 pts to go |
| P04 | 3833 | 38.6% | 38.6% | +1.9 | 55% | ❌ 16 pts to go |
| P05 | 422 | 23.9% | 23.9% | +1.7 | 50% | ❌ 26 pts to go |
| P06M | 13084 | 7.2% | 7.2% | +3.6 | n/a | no target |
| P06T | 74208 | 62.6% | 62.6% | +35.6 | n/a | no target |
| P06 | 295 | 44.4% | 44.4% | +9.2 | n/a | no target |
| P07 | 800 | 40.5% | 40.5% | +7.3 | 55% | ❌ 14 pts to go |
| P08 | 25539 | 33.9% | 33.9% | +7.0 | 50% | ❌ 16 pts to go |
| P09 | 295 | 72.2% | 72.2% | +1.2 | 70% | ✅ met |
| P10R | 100545 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P10 | 2642 | 47.0% | 47.0% | +7.5 | 55% | 🟡 8 pts to go |
| P11 | 17418 | 96.1% | 96.1% | +4.1 | 50% | ✅ met |
| P12 | 7 | 100.0% | 100.0% | +12.5 | n/a | no target |
| P13 | 17697 | 74.0% | 74.0% | +74.0 | n/a | no target |

### `vendor_phone`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 125 | 49.6% | 49.6% | +35.2 | n/a | no target |
| P01T | 398 | 74.9% | 74.9% | +18.6 | n/a | no target |
| P01_GOLD | 625 | 46.1% | 46.1% | -1.8 | 70% | ❌ 24 pts to go |
| P02 | 471 | 52.2% | 52.2% | -1.8 | 70% | ❌ 18 pts to go |
| P03 | 257 | 47.9% | 47.9% | -1.7 | 70% | ❌ 22 pts to go |
| P04 | 3833 | 49.6% | 49.6% | +2.5 | 65% | ❌ 15 pts to go |
| P05 | 422 | 26.8% | 26.8% | -3.9 | 60% | ❌ 33 pts to go |
| P06M | 13084 | 36.8% | 36.8% | +33.3 | n/a | no target |
| P06T | 74208 | 72.6% | 72.6% | +8.8 | n/a | no target |
| P06 | 295 | 64.7% | 64.7% | +7.1 | 40% | ✅ met |
| P07 | 800 | 62.2% | 62.2% | +5.2 | 85% | ❌ 23 pts to go |
| P08 | 25539 | 61.7% | 61.7% | +4.8 | 85% | ❌ 23 pts to go |
| P09 | 295 | 54.6% | 54.6% | +1.1 | 85% | ❌ 30 pts to go |
| P10R | 100545 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P10 | 2642 | 62.0% | 62.0% | +1.0 | 85% | ❌ 23 pts to go |
| P11 | 17418 | 4.5% | 4.5% | -1.9 | 75% | ❌ 70 pts to go |
| P12 | 7 | 28.6% | 28.6% | +3.6 | n/a | no target |
| P13 | 17697 | 100.0% | 100.0% | +0.0 | 60% | ✅ met |

### `vendor_website`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 125 | 53.6% | 53.6% | +34.0 | n/a | no target |
| P01T | 398 | 98.2% | 98.2% | +1.8 | n/a | no target |
| P01_GOLD | 625 | 79.5% | 79.5% | -9.8 | 90% | ❌ 10 pts to go |
| P02 | 471 | 84.3% | 84.3% | -4.9 | 90% | 🟡 6 pts to go |
| P03 | 257 | 87.5% | 87.5% | -3.5 | 90% | 🟡 2 pts to go |
| P04 | 3833 | 85.3% | 85.3% | -4.9 | 85% | ✅ met |
| P05 | 422 | 44.1% | 44.1% | -8.1 | 70% | ❌ 26 pts to go |
| P06M | 13084 | 42.6% | 42.6% | +36.4 | n/a | no target |
| P06T | 74208 | 99.9% | 99.9% | +7.9 | n/a | no target |
| P06 | 295 | 98.3% | 98.3% | +0.0 | 50% | ✅ met |
| P07 | 800 | 99.1% | 99.1% | +0.0 | 100% | 🟡 1 pts to go |
| P08 | 25539 | 99.5% | 99.5% | +0.1 | 100% | 🟡 0 pts to go |
| P09 | 295 | 80.3% | 80.3% | +0.1 | 100% | ❌ 20 pts to go |
| P10R | 100545 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P10 | 2642 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P11 | 17418 | 99.8% | 99.8% | +0.1 | 100% | 🟡 0 pts to go |
| P12 | 7 | 28.6% | 28.6% | -8.9 | n/a | no target |
| P13 | 17697 | 100.0% | 100.0% | +0.0 | n/a | no target |

### `vendor_emails`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 125 | 15.2% | 15.2% | +0.8 | n/a | no target |
| P01T | 398 | 51.5% | 51.5% | +2.4 | n/a | no target |
| P01_GOLD | 625 | 43.0% | 43.0% | -2.2 | 70% | ❌ 27 pts to go |
| P02 | 471 | 48.8% | 48.8% | -0.7 | 75% | ❌ 26 pts to go |
| P03 | 257 | 44.0% | 44.0% | -0.5 | 75% | ❌ 31 pts to go |
| P04 | 3833 | 38.5% | 38.5% | +1.1 | 70% | ❌ 32 pts to go |
| P05 | 422 | 20.6% | 20.6% | -4.9 | 55% | ❌ 34 pts to go |
| P06M | 13084 | 4.6% | 4.6% | +1.3 | n/a | no target |
| P06T | 74208 | 39.5% | 39.5% | -0.1 | n/a | no target |
| P06 | 295 | 46.1% | 46.1% | +3.3 | n/a | no target |
| P07 | 800 | 48.4% | 48.4% | +2.5 | 70% | ❌ 22 pts to go |
| P08 | 25539 | 51.8% | 51.8% | +1.9 | 75% | ❌ 23 pts to go |
| P09 | 295 | 49.8% | 49.8% | +0.0 | 85% | ❌ 35 pts to go |
| P10R | 100545 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P10 | 2642 | 43.8% | 43.8% | +0.3 | 80% | ❌ 36 pts to go |
| P11 | 17418 | 3.4% | 3.4% | -1.6 | 70% | ❌ 67 pts to go |
| P12 | 7 | 14.3% | 14.3% | -10.7 | n/a | no target |
| P13 | 17697 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `vendor_logo_url`

> ceiling: needs the vendor's website first; sites that block automated readers (robots.txt / 403) are never read

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 125 | 53.6% | 53.6% | +40.2 | n/a | no target |
| P01T | 398 | 88.4% | 88.4% | -1.4 | n/a | no target |
| P01_GOLD | 625 | 69.4% | 69.4% | -8.1 | 90% | ❌ 21 pts to go |
| P02 | 471 | 73.2% | 73.2% | -4.4 | 90% | ❌ 17 pts to go |
| P03 | 257 | 80.2% | 80.2% | -3.0 | 90% | 🟡 10 pts to go |
| P04 | 3833 | 72.3% | 72.3% | -3.3 | 85% | ❌ 13 pts to go |
| P05 | 422 | 41.0% | 41.0% | -7.7 | 75% | ❌ 34 pts to go |
| P06M | 13084 | 42.2% | 42.2% | +38.1 | n/a | no target |
| P06T | 74208 | 94.1% | 94.1% | +10.9 | n/a | no target |
| P06 | 295 | 84.1% | 84.1% | +4.8 | n/a | no target |
| P07 | 800 | 87.8% | 87.8% | +6.2 | 100% | ❌ 12 pts to go |
| P08 | 25539 | 84.3% | 84.3% | +5.4 | 100% | ❌ 16 pts to go |
| P09 | 295 | 62.0% | 62.0% | +0.6 | n/a | no target |
| P10R | 100545 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P10 | 2642 | 84.7% | 84.7% | +0.5 | 100% | ❌ 15 pts to go |
| P11 | 17418 | 93.5% | 93.5% | +5.1 | n/a | no target |
| P12 | 7 | 28.6% | 28.6% | -8.9 | n/a | no target |
| P13 | 17697 | 83.9% | 83.9% | +0.7 | n/a | no target |

### `vendor_neq`

> ceiling: only Québec-registered vendors have an NEQ; the share of QC vendors is reported next to the rate

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 125 | 46.4% | 46.4% | -7.2 | n/a | no target · QC vendors: 45 rows, 100.0% filled |
| P01T | 398 | 21.4% | 21.4% | +3.6 | n/a | no target · QC vendors: 20 rows, 100.0% filled |
| P01_GOLD | 625 | 43.7% | 43.7% | +0.1 | 95% | ❌ 51 pts to go · QC vendors: 53 rows, 98.1% filled |
| P02 | 471 | 54.4% | 54.4% | -0.7 | 95% | ❌ 41 pts to go · QC vendors: 110 rows, 100.0% filled |
| P03 | 257 | 45.9% | 45.9% | -0.6 | 95% | ❌ 49 pts to go · QC vendors: 18 rows, 100.0% filled |
| P04 | 3833 | 28.3% | 28.3% | -3.6 | 95% | ❌ 67 pts to go · QC vendors: 496 rows, 98.8% filled |
| P05 | 422 | 14.0% | 14.0% | -0.8 | n/a | no target · QC vendors: 34 rows, 94.1% filled |
| P06M | 13084 | 41.9% | 41.9% | -11.4 | n/a | no target · QC vendors: 4791 rows, 100.0% filled |
| P06T | 74208 | 19.8% | 19.8% | +2.3 | n/a | no target · QC vendors: 3646 rows, 100.0% filled |
| P06 | 295 | 8.1% | 8.1% | -0.2 | n/a | no target · QC vendors: 17 rows, 76.5% filled |
| P07 | 800 | 5.9% | 5.9% | -0.9 | n/a | no target · QC vendors: 39 rows, 79.5% filled |
| P08 | 25539 | 6.0% | 6.0% | -0.5 | n/a | no target · QC vendors: 1239 rows, 97.9% filled |
| P09 | 295 | 78.0% | 78.0% | -0.2 | 95% | ❌ 17 pts to go · QC vendors: 106 rows, 100.0% filled |
| P10R | 100545 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P10 | 2642 | 17.6% | 17.6% | +0.0 | n/a | no target · QC vendors: 304 rows, 94.7% filled |
| P11 | 17418 | 88.4% | 88.4% | +6.9 | n/a | no target · QC vendors: 116 rows, 98.3% filled |
| P12 | 7 | 71.4% | 71.4% | +8.9 | n/a | no target · QC vendors: 1 rows, 100.0% filled |
| P13 | 17697 | 16.1% | 16.1% | +16.1 | n/a | no target · QC vendors: 2851 rows, 100.0% filled |

### `vendor_years_in_business`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 125 | 54.4% | 54.4% | -10.5 | n/a | no target · vendors with a registry record: 68 rows, 100.0% filled |
| P01T | 398 | 39.7% | 39.7% | +1.4 | n/a | no target · vendors with a registry record: 158 rows, 100.0% filled |
| P01_GOLD | 625 | 79.5% | 79.5% | +0.1 | 100% | ❌ 20 pts to go · vendors with a registry record: 497 rows, 100.0% filled |
| P02 | 471 | 76.6% | 76.6% | -0.8 | 100% | ❌ 23 pts to go · vendors with a registry record: 361 rows, 100.0% filled |
| P03 | 257 | 80.5% | 80.5% | -0.7 | 100% | ❌ 20 pts to go · vendors with a registry record: 207 rows, 100.0% filled |
| P04 | 3833 | 44.0% | 44.0% | -2.1 | 100% | ❌ 56 pts to go · vendors with a registry record: 1688 rows, 100.0% filled |
| P05 | 422 | 58.1% | 58.1% | -0.2 | n/a | no target · vendors with a registry record: 245 rows, 100.0% filled |
| P06M | 13084 | 42.8% | 42.8% | -11.5 | n/a | no target · vendors with a registry record: 5596 rows, 100.0% filled |
| P06T | 74208 | 31.2% | 31.2% | +0.8 | n/a | no target · vendors with a registry record: 23181 rows, 100.0% filled |
| P06 | 295 | 26.1% | 26.1% | +0.6 | n/a | no target · vendors with a registry record: 77 rows, 100.0% filled |
| P07 | 800 | 18.6% | 18.6% | +0.2 | n/a | no target · vendors with a registry record: 149 rows, 100.0% filled |
| P08 | 25539 | 13.8% | 13.8% | -0.5 | n/a | no target · vendors with a registry record: 3527 rows, 100.0% filled |
| P09 | 295 | 90.8% | 90.8% | -0.3 | n/a | no target · vendors with a registry record: 268 rows, 100.0% filled |
| P10R | 100545 | 100.0% | 100.0% | +0.0 | n/a | no target · vendors with a registry record: 100545 rows, 100.0% filled |
| P10 | 2642 | 33.2% | 33.2% | +0.0 | n/a | no target · vendors with a registry record: 878 rows, 100.0% filled |
| P11 | 17418 | 94.7% | 94.7% | +2.4 | n/a | no target · vendors with a registry record: 16496 rows, 100.0% filled |
| P12 | 7 | 100.0% | 100.0% | +0.0 | n/a | no target · vendors with a registry record: 7 rows, 100.0% filled |
| P13 | 17697 | 16.1% | 16.1% | +16.1 | n/a | no target · vendors with a registry record: 2851 rows, 100.0% filled |

## 3. buyer

### `buyer_legal_name_as_published`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 125 | 94.4% | 94.4% | +5.7 | 90% | ✅ met |
| P01T | 398 | 70.4% | 70.4% | +14.1 | 90% | ❌ 20 pts to go |
| P01_GOLD | 625 | 86.6% | 86.6% | +2.9 | 95% | 🟡 8 pts to go |
| P02 | 471 | 87.5% | 87.5% | +2.3 | 95% | 🟡 8 pts to go |
| P03 | 257 | 83.3% | 83.3% | +4.4 | 85% | 🟡 2 pts to go |
| P04 | 3833 | 61.3% | 61.3% | +4.9 | 90% | ❌ 29 pts to go |
| P05 | 422 | 78.4% | 78.4% | +10.7 | 75% | ✅ met |
| P06M | 13084 | 89.7% | 89.7% | +2.6 | n/a | no target |
| P06T | 74208 | 43.7% | 43.7% | +14.7 | n/a | no target |
| P06 | 295 | 72.2% | 72.2% | +15.3 | 80% | 🟡 8 pts to go |
| P07 | 800 | 55.0% | 55.1% | +8.8 | 80% | ❌ 25 pts to go |
| P08 | 25539 | 49.5% | 49.5% | +11.0 | 75% | ❌ 26 pts to go |
| P09 | 295 | 76.9% | 76.9% | -0.3 | 95% | ❌ 18 pts to go |
| P10R | 100545 | 37.5% | 37.5% | +12.5 | n/a | no target |
| P10 | 2642 | 50.6% | 50.7% | +11.6 | 70% | ❌ 19 pts to go |
| P11 | 17418 | 40.9% | 40.9% | +31.3 | 65% | ❌ 24 pts to go |
| P12 | 7 | 71.4% | 71.4% | -3.6 | 80% | 🟡 9 pts to go |
| P13 | 17697 | 48.5% | 48.5% | +9.3 | 60% | ❌ 12 pts to go |

### `buyer_bn_as_published`

> ceiling: a buyer's BN is public only where the buyer prints it or a public dataset carries it (CRA charities, federal grants & contributions recipients, business registries for corporations); municipalities rarely publish theirs

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 125 | 19.2% | 19.2% | -0.4 | 50% | ❌ 31 pts to go |
| P01T | 398 | 14.3% | 14.3% | +1.0 | n/a | no target |
| P01_GOLD | 625 | 19.8% | 19.8% | -0.8 | 40% | ❌ 20 pts to go |
| P02 | 471 | 19.3% | 19.3% | +0.4 | 40% | ❌ 21 pts to go |
| P03 | 257 | 23.0% | 23.0% | +0.7 | 40% | ❌ 17 pts to go |
| P04 | 3833 | 15.3% | 15.3% | -1.0 | 40% | ❌ 25 pts to go |
| P05 | 422 | 19.9% | 19.9% | +0.2 | 25% | 🟡 5 pts to go |
| P06M | 13084 | 10.5% | 10.5% | +1.7 | n/a | no target |
| P06T | 74208 | 8.8% | 8.8% | +1.3 | n/a | no target |
| P06 | 295 | 15.9% | 15.9% | +3.1 | 35% | ❌ 19 pts to go |
| P07 | 800 | 14.2% | 14.2% | +2.7 | 35% | ❌ 21 pts to go |
| P08 | 25539 | 13.8% | 13.8% | +3.4 | 35% | ❌ 21 pts to go |
| P09 | 295 | 16.3% | 16.3% | +0.1 | n/a | no target |
| P10R | 100545 | 8.7% | 8.7% | +1.6 | n/a | no target |
| P10 | 2642 | 11.2% | 11.2% | +4.7 | 30% | ❌ 19 pts to go |
| P11 | 17418 | 1.5% | 1.5% | +0.3 | n/a | no target |
| P12 | 7 | 14.3% | 14.3% | +1.8 | n/a | no target |
| P13 | 17697 | 20.8% | 20.8% | -0.2 | 30% | 🟡 9 pts to go |

### `buyer_address`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 125 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P01T | 398 | 90.2% | 90.2% | -1.7 | 100% | 🟡 10 pts to go |
| P01_GOLD | 625 | 90.1% | 90.1% | +0.6 | 100% | 🟡 10 pts to go |
| P02 | 471 | 95.5% | 95.5% | +0.2 | 100% | 🟡 4 pts to go |
| P03 | 257 | 89.5% | 89.5% | +0.0 | 100% | ❌ 10 pts to go |
| P04 | 3833 | 75.4% | 75.4% | -0.5 | 100% | ❌ 25 pts to go |
| P05 | 422 | 88.2% | 88.2% | +0.8 | 100% | ❌ 12 pts to go |
| P06M | 13084 | 99.2% | 99.2% | +0.4 | n/a | no target |
| P06T | 74208 | 76.9% | 76.9% | -0.5 | n/a | no target |
| P06 | 295 | 81.4% | 81.4% | +0.4 | 95% | ❌ 14 pts to go |
| P07 | 800 | 83.0% | 83.0% | -0.6 | 95% | ❌ 12 pts to go |
| P08 | 25539 | 79.5% | 79.5% | -0.7 | 95% | ❌ 16 pts to go |
| P09 | 295 | 95.9% | 95.9% | +0.2 | 100% | 🟡 4 pts to go |
| P10R | 100545 | 60.5% | 60.5% | +1.7 | n/a | no target |
| P10 | 2642 | 65.4% | 65.4% | +0.3 | 95% | ❌ 30 pts to go |
| P11 | 17418 | 92.8% | 92.8% | +5.6 | 80% | ✅ met |
| P12 | 7 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P13 | 17697 | 77.0% | 77.0% | +1.8 | 95% | ❌ 18 pts to go |

### `buyer_phone`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 125 | 85.6% | 85.6% | +0.0 | n/a | no target |
| P01T | 398 | 72.4% | 72.4% | +8.8 | n/a | no target |
| P01_GOLD | 625 | 70.4% | 70.4% | +0.9 | 90% | ❌ 20 pts to go |
| P02 | 471 | 76.6% | 76.6% | +0.9 | 95% | ❌ 18 pts to go |
| P03 | 257 | 73.5% | 73.5% | -0.3 | 95% | ❌ 22 pts to go |
| P04 | 3833 | 67.8% | 67.8% | +1.2 | 95% | ❌ 27 pts to go |
| P05 | 422 | 71.6% | 71.6% | +1.1 | 90% | ❌ 18 pts to go |
| P06M | 13084 | 82.4% | 82.4% | -4.0 | n/a | no target |
| P06T | 74208 | 61.7% | 61.7% | +13.8 | n/a | no target |
| P06 | 295 | 68.1% | 68.1% | +5.0 | 95% | ❌ 27 pts to go |
| P07 | 800 | 59.9% | 59.9% | +4.9 | 90% | ❌ 30 pts to go |
| P08 | 25539 | 63.7% | 63.7% | +4.9 | 95% | ❌ 31 pts to go |
| P09 | 295 | 85.8% | 85.8% | -0.3 | 100% | ❌ 14 pts to go |
| P10R | 100545 | 56.8% | 56.8% | +11.7 | n/a | no target |
| P10 | 2642 | 58.1% | 58.1% | +1.6 | 95% | ❌ 37 pts to go |
| P11 | 17418 | 27.9% | 27.9% | +16.7 | 75% | ❌ 47 pts to go |
| P12 | 7 | 71.4% | 71.4% | -3.6 | n/a | no target |
| P13 | 17697 | 60.0% | 60.0% | +12.4 | 95% | ❌ 35 pts to go |

### `buyer_logo_url`

> ceiling: sites that block automated readers (robots.txt / 403) are never read; an og:image that looks like a photo is labelled

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 125 | 65.6% | 65.6% | -5.5 | n/a | no target |
| P01T | 398 | 83.4% | 83.4% | +9.3 | 95% | ❌ 12 pts to go |
| P01_GOLD | 625 | 81.1% | 81.1% | +0.4 | 90% | 🟡 9 pts to go |
| P02 | 471 | 85.6% | 85.6% | -0.2 | 95% | 🟡 9 pts to go |
| P03 | 257 | 83.7% | 83.7% | -0.3 | 95% | ❌ 11 pts to go |
| P04 | 3833 | 81.0% | 81.0% | -2.3 | 90% | 🟡 9 pts to go |
| P05 | 422 | 89.3% | 89.3% | +0.8 | 95% | 🟡 6 pts to go |
| P06M | 13084 | 68.6% | 68.6% | +1.9 | n/a | no target |
| P06T | 74208 | 80.8% | 80.8% | +19.3 | n/a | no target |
| P06 | 295 | 86.4% | 86.4% | +4.3 | 100% | ❌ 14 pts to go |
| P07 | 800 | 79.6% | 79.6% | +2.4 | 100% | ❌ 20 pts to go |
| P08 | 25539 | 80.2% | 80.2% | +3.1 | 100% | ❌ 20 pts to go |
| P09 | 295 | 68.8% | 68.8% | +0.2 | n/a | no target |
| P10R | 100545 | 77.7% | 77.7% | +17.7 | n/a | no target |
| P10 | 2642 | 87.6% | 87.6% | +0.8 | 100% | ❌ 12 pts to go |
| P11 | 17418 | 62.0% | 62.0% | +43.2 | 80% | ❌ 18 pts to go |
| P12 | 7 | 71.4% | 71.4% | -3.6 | n/a | no target |
| P13 | 17697 | 65.2% | 65.2% | +14.2 | 95% | ❌ 30 pts to go |

## 4. AP

### `ap_contact_name_as_published`

> ceiling: owner 2026-11-08: the AP contact person the organisation itself names on its AP / finance page is allowed (name + role phrase, quoted); mailboxes stay organisational; many bodies publish no AP person

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 125 | 2.4% | 2.4% | -1.7 | n/a | no target |
| P01T | 398 | 7.8% | 7.8% | -0.6 | n/a | no target |
| P01_GOLD | 625 | 14.2% | 14.2% | +0.0 | 25% | ❌ 11 pts to go |
| P02 | 471 | 24.2% | 24.2% | -0.3 | 40% | ❌ 16 pts to go |
| P03 | 257 | 8.9% | 8.9% | -0.1 | 20% | ❌ 11 pts to go |
| P04 | 3833 | 3.2% | 3.2% | -0.4 | 20% | ❌ 17 pts to go |
| P05 | 422 | 3.1% | 3.1% | -0.2 | 15% | ❌ 12 pts to go |
| P06M | 13084 | 0.2% | 0.2% | -0.1 | n/a | no target |
| P06T | 74208 | 0.3% | 0.3% | -0.1 | n/a | no target |
| P06 | 295 | 5.4% | 5.4% | -0.8 | n/a | no target |
| P07 | 800 | 7.4% | 7.4% | +0.1 | n/a | no target |
| P08 | 25539 | 0.2% | 0.2% | -0.1 | n/a | no target |
| P09 | 295 | 7.8% | 7.8% | +0.2 | n/a | no target |
| P10R | 100545 | 0.2% | 0.2% | +0.0 | n/a | no target |
| P10 | 2642 | 0.9% | 0.9% | -0.1 | n/a | no target |
| P11 | 17418 | 0.1% | 0.1% | -0.1 | n/a | no target |
| P12 | 7 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P13 | 17697 | 0.4% | 0.4% | +0.0 | n/a | no target |

### `ap_phone`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 125 | 19.2% | 19.2% | -7.6 | n/a | no target |
| P01T | 398 | 21.9% | 21.9% | -2.2 | 70% | ❌ 48 pts to go |
| P01_GOLD | 625 | 43.4% | 43.4% | +0.1 | 80% | ❌ 37 pts to go |
| P02 | 471 | 56.1% | 56.1% | -0.7 | 90% | ❌ 34 pts to go |
| P03 | 257 | 19.1% | 19.1% | +0.0 | 60% | ❌ 41 pts to go |
| P04 | 3833 | 21.1% | 21.1% | -2.6 | 85% | ❌ 64 pts to go |
| P05 | 422 | 11.8% | 11.8% | -0.1 | 50% | ❌ 38 pts to go |
| P06M | 13084 | 0.3% | 0.3% | -0.1 | n/a | no target |
| P06T | 74208 | 0.5% | 0.5% | -0.1 | n/a | no target |
| P06 | 295 | 14.9% | 14.9% | -1.3 | n/a | no target |
| P07 | 800 | 11.6% | 11.6% | -1.4 | n/a | no target |
| P08 | 25539 | 0.4% | 0.4% | -0.1 | n/a | no target |
| P09 | 295 | 77.3% | 77.3% | -0.3 | 95% | ❌ 18 pts to go |
| P10R | 100545 | 0.2% | 0.2% | +0.0 | n/a | no target |
| P10 | 2642 | 1.7% | 1.7% | +0.0 | n/a | no target |
| P11 | 17418 | 2.0% | 2.0% | -1.6 | n/a | no target |
| P12 | 7 | 28.6% | 28.6% | +3.6 | n/a | no target |
| P13 | 17697 | 0.7% | 0.7% | +0.0 | n/a | no target |

### `invoice_mailing_address`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 125 | 5.6% | 5.6% | -1.6 | n/a | no target |
| P01T | 398 | 11.3% | 11.3% | -0.7 | n/a | no target |
| P01_GOLD | 625 | 33.9% | 33.9% | +0.0 | 70% | ❌ 36 pts to go |
| P02 | 471 | 38.4% | 38.4% | -0.5 | 75% | ❌ 37 pts to go |
| P03 | 257 | 19.1% | 19.1% | +0.0 | 55% | ❌ 36 pts to go |
| P04 | 3833 | 21.0% | 21.0% | -2.6 | 75% | ❌ 54 pts to go |
| P05 | 422 | 10.9% | 10.9% | +0.1 | 50% | ❌ 39 pts to go |
| P06M | 13084 | 0.1% | 0.1% | -0.1 | n/a | no target |
| P06T | 74208 | 0.3% | 0.3% | -0.1 | n/a | no target |
| P06 | 295 | 7.5% | 7.5% | -0.8 | n/a | no target |
| P07 | 800 | 5.4% | 5.4% | -1.0 | n/a | no target |
| P08 | 25539 | 0.2% | 0.2% | +0.0 | n/a | no target |
| P09 | 295 | 74.9% | 74.9% | -0.3 | 95% | ❌ 20 pts to go |
| P10R | 100545 | 0.1% | 0.1% | -0.1 | n/a | no target |
| P10 | 2642 | 1.0% | 1.0% | +0.0 | n/a | no target |
| P11 | 17418 | 2.0% | 2.0% | -1.6 | n/a | no target |
| P12 | 7 | 14.3% | 14.3% | +1.8 | n/a | no target |
| P13 | 17697 | 0.4% | 0.4% | +0.0 | n/a | no target |

### `invoicing_requirements`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 125 | 5.6% | 5.6% | -0.6 | n/a | no target |
| P01T | 398 | 8.0% | 8.0% | -1.3 | n/a | no target |
| P01_GOLD | 625 | 57.9% | 58.1% | -0.1 | 80% | ❌ 22 pts to go |
| P02 | 471 | 45.2% | 45.4% | -0.6 | 75% | ❌ 30 pts to go |
| P03 | 257 | 37.7% | 37.7% | -0.2 | 70% | ❌ 32 pts to go |
| P04 | 3833 | 20.5% | 21.0% | -2.6 | 70% | ❌ 50 pts to go |
| P05 | 422 | 14.2% | 14.2% | -0.1 | 50% | ❌ 36 pts to go |
| P06M | 13084 | 0.3% | 0.3% | -0.1 | n/a | no target |
| P06T | 74208 | 0.3% | 0.3% | +0.0 | n/a | no target |
| P06 | 295 | 13.2% | 13.2% | -0.2 | n/a | no target |
| P07 | 800 | 1.9% | 1.9% | -0.1 | n/a | no target |
| P08 | 25539 | 0.3% | 0.3% | -0.1 | n/a | no target |
| P09 | 295 | 46.1% | 46.4% | +0.2 | 80% | ❌ 34 pts to go |
| P10R | 100545 | 0.1% | 0.1% | +0.0 | n/a | no target |
| P10 | 2642 | 1.2% | 1.2% | +0.0 | n/a | no target |
| P11 | 17418 | 0.6% | 0.6% | -0.5 | n/a | no target |
| P12 | 7 | 42.9% | 42.9% | +5.4 | n/a | no target |
| P13 | 17697 | 0.3% | 0.3% | +0.0 | n/a | no target |

### `payment_terms_as_published`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 125 | 11.2% | 11.2% | -0.1 | n/a | no target |
| P01T | 398 | 18.1% | 18.1% | -3.9 | 60% | ❌ 42 pts to go |
| P01_GOLD | 625 | 63.5% | 63.5% | -0.1 | 70% | 🟡 6 pts to go |
| P02 | 471 | 38.4% | 38.4% | -0.5 | 50% | ❌ 12 pts to go |
| P03 | 257 | 49.8% | 49.8% | -0.2 | 55% | 🟡 5 pts to go |
| P04 | 3833 | 11.7% | 11.7% | -1.6 | 40% | ❌ 28 pts to go |
| P05 | 422 | 17.3% | 17.3% | +0.0 | 40% | ❌ 23 pts to go |
| P06M | 13084 | 0.5% | 0.5% | -0.2 | n/a | no target |
| P06T | 74208 | 2.0% | 2.0% | -0.4 | n/a | no target |
| P06 | 295 | 19.3% | 19.3% | -0.4 | n/a | no target |
| P07 | 800 | 6.0% | 6.0% | -0.7 | n/a | no target |
| P08 | 25539 | 2.2% | 2.2% | -0.4 | n/a | no target |
| P09 | 295 | 5.8% | 5.8% | -0.1 | n/a | no target |
| P10R | 100545 | 0.2% | 0.2% | +0.0 | n/a | no target |
| P10 | 2642 | 4.4% | 4.4% | -0.1 | n/a | no target |
| P11 | 17418 | 3.2% | 3.2% | -1.1 | n/a | no target |
| P12 | 7 | 0.0% | 0.0% | -12.5 | n/a | no target |
| P13 | 17697 | 0.2% | 0.2% | +0.0 | n/a | no target |

### `po_required_as_published`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 125 | 14.4% | 14.4% | -2.1 | n/a | no target |
| P01T | 398 | 22.1% | 22.1% | -3.2 | 65% | ❌ 43 pts to go |
| P01_GOLD | 625 | 69.0% | 69.0% | +0.0 | 70% | 🟡 1 pts to go |
| P02 | 471 | 23.6% | 23.6% | -0.3 | 50% | ❌ 26 pts to go |
| P03 | 257 | 52.1% | 52.1% | -0.2 | 60% | 🟡 8 pts to go |
| P04 | 3833 | 5.0% | 5.0% | -0.8 | 40% | ❌ 35 pts to go |
| P05 | 422 | 19.9% | 19.9% | +0.2 | 45% | ❌ 25 pts to go |
| P06M | 13084 | 0.3% | 0.3% | +0.0 | n/a | no target |
| P06T | 74208 | 0.5% | 0.5% | -0.1 | n/a | no target |
| P06 | 295 | 29.5% | 29.5% | -2.2 | n/a | no target |
| P07 | 800 | 6.1% | 6.1% | -0.8 | n/a | no target |
| P08 | 25539 | 0.9% | 0.9% | -0.2 | n/a | no target |
| P09 | 295 | 9.8% | 9.8% | -0.1 | n/a | no target |
| P10R | 100545 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P10 | 2642 | 2.5% | 2.5% | -0.1 | n/a | no target |
| P11 | 17418 | 0.6% | 0.6% | -0.4 | n/a | no target |
| P12 | 7 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P13 | 17697 | 0.2% | 0.2% | +0.0 | n/a | no target |

### `invoice_portal_url`

> ceiling: only portals the buyer names on its own pages; informational tax-authority links are not portals

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 125 | 4.8% | 4.8% | -1.4 | n/a | no target |
| P01T | 398 | 12.6% | 12.6% | -1.9 | n/a | no target |
| P01_GOLD | 625 | 49.8% | 49.8% | +0.0 | 50% | 🟡 0 pts to go |
| P02 | 471 | 36.9% | 36.9% | -0.5 | n/a | no target |
| P03 | 257 | 52.5% | 52.5% | -0.6 | 60% | 🟡 8 pts to go |
| P04 | 3833 | 11.4% | 11.4% | -1.5 | n/a | no target |
| P05 | 422 | 14.9% | 14.9% | -0.3 | n/a | no target |
| P06M | 13084 | 0.2% | 0.2% | -0.1 | n/a | no target |
| P06T | 74208 | 0.4% | 0.4% | -0.1 | n/a | no target |
| P06 | 295 | 21.4% | 21.4% | -0.3 | n/a | no target |
| P07 | 800 | 6.8% | 6.8% | -0.4 | n/a | no target |
| P08 | 25539 | 0.4% | 0.4% | -0.1 | n/a | no target |
| P09 | 295 | 18.3% | 18.3% | +0.1 | n/a | no target |
| P10R | 100545 | 0.1% | 0.1% | +0.0 | n/a | no target |
| P10 | 2642 | 2.3% | 2.3% | +0.0 | n/a | no target |
| P11 | 17418 | 0.5% | 0.5% | -0.3 | n/a | no target |
| P12 | 7 | 14.3% | 14.3% | +14.3 | n/a | no target |
| P13 | 17697 | 0.4% | 0.4% | +0.0 | n/a | no target |

### `buyer_payment_method_preference`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 125 | 9.6% | 9.6% | -1.7 | 15% | 🟡 5 pts to go |
| P01T | 398 | 10.6% | 10.6% | -0.5 | 15% | 🟡 4 pts to go |
| P01_GOLD | 625 | 35.4% | 35.4% | +0.1 | 40% | 🟡 5 pts to go |
| P02 | 471 | 12.5% | 12.7% | +0.0 | 25% | ❌ 12 pts to go |
| P03 | 257 | 17.9% | 17.9% | -0.1 | 25% | 🟡 7 pts to go |
| P04 | 3833 | 2.7% | 2.7% | -0.1 | 15% | ❌ 12 pts to go |
| P05 | 422 | 6.6% | 6.6% | -0.2 | 15% | 🟡 8 pts to go |
| P06M | 13084 | 0.6% | 0.6% | +0.0 | 15% | ❌ 14 pts to go |
| P06T | 74208 | 0.6% | 0.6% | +0.2 | 15% | ❌ 14 pts to go |
| P06 | 295 | 9.2% | 9.2% | -0.1 | 15% | 🟡 6 pts to go |
| P07 | 800 | 3.6% | 3.6% | +0.4 | 15% | ❌ 11 pts to go |
| P08 | 25539 | 0.6% | 0.6% | +0.2 | 15% | ❌ 14 pts to go |
| P09 | 295 | 1.0% | 1.0% | +0.0 | 15% | ❌ 14 pts to go |
| P10R | 100545 | 0.6% | 0.6% | +0.2 | 15% | ❌ 14 pts to go |
| P10 | 2642 | 1.2% | 1.2% | +0.2 | 15% | ❌ 14 pts to go |
| P11 | 17418 | 0.3% | 0.3% | +0.1 | 15% | ❌ 15 pts to go |
| P12 | 7 | 14.3% | 14.3% | +1.8 | 15% | 🟡 1 pts to go |
| P13 | 17697 | 0.5% | 0.5% | +0.1 | 15% | ❌ 14 pts to go |

### `buyer_tax_exempt_status`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 125 | 3.2% | 3.2% | -3.0 | 15% | ❌ 12 pts to go |
| P01T | 398 | 9.8% | 9.8% | -2.2 | 25% | ❌ 15 pts to go |
| P01_GOLD | 625 | 29.1% | 29.1% | -0.1 | 25% | ✅ met |
| P02 | 471 | 25.1% | 25.1% | -0.3 | 15% | ✅ met |
| P03 | 257 | 21.4% | 21.4% | -0.1 | 15% | ✅ met |
| P04 | 3833 | 3.7% | 3.7% | -0.4 | 15% | ❌ 11 pts to go |
| P05 | 422 | 10.9% | 10.9% | +0.1 | 15% | 🟡 4 pts to go |
| P06M | 13084 | 0.2% | 0.2% | +0.0 | 15% | ❌ 15 pts to go |
| P06T | 74208 | 0.3% | 0.3% | +0.0 | 15% | ❌ 15 pts to go |
| P06 | 295 | 7.8% | 7.8% | +0.2 | 15% | 🟡 7 pts to go |
| P07 | 800 | 2.8% | 2.8% | -0.3 | 15% | ❌ 12 pts to go |
| P08 | 25539 | 0.4% | 0.4% | +0.0 | 15% | ❌ 15 pts to go |
| P09 | 295 | 1.0% | 1.0% | +0.0 | 15% | ❌ 14 pts to go |
| P10R | 100545 | 0.0% | 0.0% | +0.0 | 15% | ❌ 15 pts to go |
| P10 | 2642 | 1.6% | 1.6% | +0.0 | 15% | ❌ 13 pts to go |
| P11 | 17418 | 0.4% | 0.4% | -0.1 | 15% | ❌ 15 pts to go |
| P12 | 7 | 28.6% | 28.6% | +3.6 | 15% | ✅ met |
| P13 | 17697 | 0.1% | 0.1% | +0.1 | 15% | ❌ 15 pts to go |

### `buyer_ap_cycle_published`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 125 | 0.0% | 0.0% | +0.0 | 20% | ❌ 20 pts to go |
| P01T | 398 | 3.5% | 3.5% | -0.4 | 20% | ❌ 16 pts to go |
| P01_GOLD | 625 | 4.5% | 4.5% | +0.2 | 20% | ❌ 16 pts to go |
| P02 | 471 | 1.3% | 1.3% | +0.0 | 20% | ❌ 19 pts to go |
| P03 | 257 | 1.6% | 1.6% | +0.0 | 20% | ❌ 18 pts to go |
| P04 | 3833 | 0.6% | 0.6% | +0.0 | 20% | ❌ 19 pts to go |
| P05 | 422 | 1.2% | 1.2% | +0.0 | 20% | ❌ 19 pts to go |
| P06M | 13084 | 0.0% | 0.0% | +0.0 | 20% | ❌ 20 pts to go |
| P06T | 74208 | 0.0% | 0.0% | +0.0 | 20% | ❌ 20 pts to go |
| P06 | 295 | 1.4% | 1.4% | +0.0 | 20% | ❌ 19 pts to go |
| P07 | 800 | 0.4% | 0.4% | +0.0 | 20% | ❌ 20 pts to go |
| P08 | 25539 | 0.0% | 0.0% | +0.0 | 20% | ❌ 20 pts to go |
| P09 | 295 | 0.0% | 0.0% | +0.0 | 20% | ❌ 20 pts to go |
| P10R | 100545 | 0.0% | 0.0% | +0.0 | 20% | ❌ 20 pts to go |
| P10 | 2642 | 0.3% | 0.3% | +0.0 | 20% | ❌ 20 pts to go |
| P11 | 17418 | 0.0% | 0.0% | +0.0 | 20% | ❌ 20 pts to go |
| P12 | 7 | 0.0% | 0.0% | +0.0 | 20% | ❌ 20 pts to go |
| P13 | 17697 | 0.0% | 0.0% | +0.0 | 20% | ❌ 20 pts to go |

### `buyer_esignature_preference`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 125 | 0.8% | 0.8% | -0.2 | 15% | ❌ 14 pts to go |
| P01T | 398 | 2.3% | 2.3% | -0.1 | 15% | ❌ 13 pts to go |
| P01_GOLD | 625 | 10.4% | 10.4% | -0.1 | 15% | 🟡 5 pts to go |
| P02 | 471 | 11.9% | 11.9% | -0.1 | 15% | 🟡 3 pts to go |
| P03 | 257 | 20.6% | 20.6% | -0.1 | 15% | ✅ met |
| P04 | 3833 | 2.2% | 2.2% | -0.2 | 15% | ❌ 13 pts to go |
| P05 | 422 | 2.8% | 2.8% | -0.2 | 15% | ❌ 12 pts to go |
| P06M | 13084 | 0.1% | 0.1% | -0.1 | 15% | ❌ 15 pts to go |
| P06T | 74208 | 0.2% | 0.2% | +0.0 | 15% | ❌ 15 pts to go |
| P06 | 295 | 5.1% | 5.1% | -0.1 | 15% | 🟡 10 pts to go |
| P07 | 800 | 1.6% | 1.6% | -0.1 | 15% | ❌ 13 pts to go |
| P08 | 25539 | 0.4% | 0.4% | +0.0 | 15% | ❌ 15 pts to go |
| P09 | 295 | 0.7% | 0.7% | +0.0 | 15% | ❌ 14 pts to go |
| P10R | 100545 | 0.0% | 0.0% | +0.0 | 15% | ❌ 15 pts to go |
| P10 | 2642 | 0.9% | 0.9% | +0.0 | 15% | ❌ 14 pts to go |
| P11 | 17418 | 0.2% | 0.2% | -0.1 | 15% | ❌ 15 pts to go |
| P12 | 7 | 0.0% | 0.0% | +0.0 | 15% | ❌ 15 pts to go |
| P13 | 17697 | 0.1% | 0.1% | +0.0 | 15% | ❌ 15 pts to go |

### `ap_system_hint`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 125 | 7.2% | 7.2% | +0.0 | 20% | ❌ 13 pts to go |
| P01T | 398 | 13.3% | 13.3% | -1.8 | 40% | ❌ 27 pts to go |
| P01_GOLD | 625 | 45.9% | 45.9% | +0.1 | 40% | ✅ met |
| P02 | 471 | 42.3% | 42.3% | -0.5 | 20% | ✅ met |
| P03 | 257 | 48.6% | 48.6% | -0.2 | 35% | ✅ met |
| P04 | 3833 | 13.7% | 13.7% | -1.7 | 20% | 🟡 6 pts to go |
| P05 | 422 | 14.9% | 14.9% | +0.1 | 20% | 🟡 5 pts to go |
| P06M | 13084 | 0.5% | 0.5% | +0.0 | 20% | ❌ 20 pts to go |
| P06T | 74208 | 0.6% | 0.6% | -0.1 | 20% | ❌ 19 pts to go |
| P06 | 295 | 22.0% | 22.0% | -0.1 | 20% | ✅ met |
| P07 | 800 | 7.0% | 7.0% | -0.1 | 20% | ❌ 13 pts to go |
| P08 | 25539 | 0.8% | 0.8% | -0.1 | 20% | ❌ 19 pts to go |
| P09 | 295 | 18.3% | 18.3% | +0.1 | 20% | 🟡 2 pts to go |
| P10R | 100545 | 0.2% | 0.2% | +0.0 | 20% | ❌ 20 pts to go |
| P10 | 2642 | 3.4% | 3.4% | +0.0 | 20% | ❌ 17 pts to go |
| P11 | 17418 | 0.6% | 0.6% | -0.4 | 20% | ❌ 19 pts to go |
| P12 | 7 | 0.0% | 0.0% | +0.0 | 20% | ❌ 20 pts to go |
| P13 | 17697 | 0.6% | 0.6% | +0.1 | 20% | ❌ 19 pts to go |

## 5. contract

### `contract_value`

> ceiling: rows proven by a lobbying filing, a news release, an auditor appointment, a customer story or a vendor's client list have no contract value by nature (≈17 % of P01 Gold); bids&tenders awards now carry the awarded bidder's submitted price when no award value was published

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 125 | 32.8% | 32.8% | -11.5 | n/a | no target |
| P01T | 398 | 0.3% | 0.3% | +0.0 | n/a | no target |
| P01_GOLD | 625 | 69.4% | 69.4% | -0.1 | 95% | ❌ 26 pts to go |
| P02 | 471 | 62.2% | 62.2% | -0.8 | 95% | ❌ 33 pts to go |
| P03 | 257 | 54.5% | 54.5% | -0.2 | 90% | ❌ 36 pts to go |
| P04 | 3833 | 24.1% | 24.1% | -3.0 | 85% | ❌ 61 pts to go |
| P05 | 422 | 37.2% | 37.2% | +0.7 | 75% | ❌ 38 pts to go |
| P06M | 13084 | 35.2% | 35.2% | -14.9 | n/a | no target |
| P06T | 74208 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06 | 295 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P07 | 800 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P08 | 25539 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P09 | 295 | 89.5% | 89.5% | +0.1 | 100% | ❌ 10 pts to go |
| P10R | 100545 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P10 | 2642 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P11 | 17418 | 0.5% | 0.5% | -0.4 | 60% | ❌ 60 pts to go |
| P12 | 7 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P13 | 17697 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `currency`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 125 | 32.8% | 32.8% | -11.5 | n/a | no target |
| P01T | 398 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P01_GOLD | 625 | 72.8% | 72.8% | +0.0 | 100% | ❌ 27 pts to go |
| P02 | 471 | 65.6% | 65.6% | -0.9 | 100% | ❌ 34 pts to go |
| P03 | 257 | 60.3% | 60.3% | -0.2 | n/a | no target |
| P04 | 3833 | 24.8% | 24.8% | -3.0 | 95% | ❌ 70 pts to go |
| P05 | 422 | 33.2% | 33.2% | +0.2 | 80% | ❌ 47 pts to go |
| P06M | 13084 | 35.2% | 35.2% | -14.9 | n/a | no target |
| P06T | 74208 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06 | 295 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P07 | 800 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P08 | 25539 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P09 | 295 | 92.5% | 92.5% | -0.2 | 100% | 🟡 8 pts to go |
| P10R | 100545 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P10 | 2642 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P11 | 17418 | 0.5% | 0.5% | -0.5 | n/a | no target |
| P12 | 7 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P13 | 17697 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `start_date`

> ceiling: most award notices publish an award date, not a start date; start_date carries the signature date when the source gives one, labelled

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 125 | 81.6% | 81.6% | +3.2 | n/a | no target |
| P01T | 398 | 0.3% | 0.3% | +0.0 | n/a | no target |
| P01_GOLD | 625 | 51.7% | 51.7% | +0.1 | 85% | ❌ 33 pts to go |
| P02 | 471 | 56.9% | 56.9% | -0.7 | 90% | ❌ 33 pts to go |
| P03 | 257 | 43.6% | 43.6% | -0.5 | 85% | ❌ 41 pts to go |
| P04 | 3833 | 27.1% | 27.1% | -3.3 | 90% | ❌ 63 pts to go |
| P05 | 422 | 33.4% | 33.4% | +0.6 | 75% | ❌ 42 pts to go |
| P06M | 13084 | 89.7% | 89.7% | -0.7 | n/a | no target |
| P06T | 74208 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06 | 295 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P07 | 800 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P08 | 25539 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P09 | 295 | 85.1% | 85.1% | +0.0 | 95% | 🟡 10 pts to go |
| P10R | 100545 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P10 | 2642 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P11 | 17418 | 0.4% | 0.4% | -0.4 | n/a | no target |
| P12 | 7 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P13 | 17697 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `end_date`

> ceiling: an inferred end (award date + published duration) is labelled as such; sources without a duration leave end_date empty — the honest ceiling. P09 is BY DEFINITION the rows whose end date is not published (older SEAO contracts with no closing notice): its end_date / duration targets cannot be met without inventing a date

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 125 | 80.8% | 80.8% | +1.4 | n/a | no target |
| P01T | 398 | 0.3% | 0.3% | +0.0 | n/a | no target |
| P01_GOLD | 625 | 51.8% | 51.8% | +0.0 | 85% | ❌ 33 pts to go |
| P02 | 471 | 52.0% | 52.0% | -0.7 | 90% | ❌ 38 pts to go |
| P03 | 257 | 44.7% | 44.7% | -0.6 | 85% | ❌ 40 pts to go |
| P04 | 3833 | 23.1% | 23.1% | -2.9 | 90% | ❌ 67 pts to go |
| P05 | 422 | 43.6% | 43.6% | +0.7 | 75% | ❌ 31 pts to go |
| P06M | 13084 | 80.4% | 80.4% | -3.3 | n/a | no target |
| P06T | 74208 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06 | 295 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P07 | 800 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P08 | 25539 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P09 | 295 | 0.3% | 0.3% | +0.0 | 95% | ❌ 95 pts to go |
| P10R | 100545 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P10 | 2642 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P11 | 17418 | 0.4% | 0.4% | -0.3 | n/a | no target |
| P12 | 7 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P13 | 17697 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `contract_title`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 125 | 90.4% | 90.4% | +4.8 | n/a | no target |
| P01T | 398 | 92.0% | 92.0% | -0.2 | n/a | no target |
| P01_GOLD | 625 | 85.4% | 85.4% | -0.1 | 100% | ❌ 15 pts to go |
| P02 | 471 | 74.7% | 74.7% | -1.0 | 100% | ❌ 25 pts to go |
| P03 | 257 | 91.4% | 91.4% | -0.8 | n/a | no target |
| P04 | 3833 | 45.7% | 45.7% | -5.8 | 95% | ❌ 49 pts to go |
| P05 | 422 | 77.3% | 77.3% | -0.5 | 95% | ❌ 18 pts to go |
| P06M | 13084 | 98.9% | 98.9% | +0.6 | n/a | no target |
| P06T | 74208 | 82.6% | 82.6% | -1.1 | n/a | no target |
| P06 | 295 | 25.8% | 25.8% | -0.4 | n/a | no target |
| P07 | 800 | 16.9% | 16.9% | -2.2 | n/a | no target |
| P08 | 25539 | 9.9% | 9.9% | -1.1 | n/a | no target |
| P09 | 295 | 98.6% | 98.6% | -0.1 | 100% | 🟡 1 pts to go |
| P10R | 100545 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P10 | 2642 | 71.2% | 71.2% | -0.5 | n/a | no target |
| P11 | 17418 | 10.3% | 10.3% | -5.8 | n/a | no target |
| P12 | 7 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P13 | 17697 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `contract_description`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 125 | 90.4% | 90.4% | +4.8 | n/a | no target |
| P01T | 398 | 92.0% | 92.0% | -0.2 | n/a | no target |
| P01_GOLD | 625 | 88.6% | 88.6% | -0.1 | 100% | ❌ 11 pts to go |
| P02 | 471 | 75.8% | 76.0% | -1.0 | 100% | ❌ 24 pts to go |
| P03 | 257 | 92.2% | 92.2% | -0.8 | n/a | no target |
| P04 | 3833 | 49.0% | 49.0% | -6.1 | 95% | ❌ 46 pts to go |
| P05 | 422 | 89.8% | 89.8% | -0.4 | 70% | ✅ met |
| P06M | 13084 | 98.9% | 98.9% | +0.6 | n/a | no target |
| P06T | 74208 | 82.6% | 82.6% | -1.1 | n/a | no target |
| P06 | 295 | 25.8% | 25.8% | -0.4 | n/a | no target |
| P07 | 800 | 16.9% | 16.9% | -2.2 | n/a | no target |
| P08 | 25539 | 9.9% | 9.9% | -1.1 | n/a | no target |
| P09 | 295 | 98.6% | 98.6% | -0.1 | 100% | 🟡 1 pts to go |
| P10R | 100545 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P10 | 2642 | 71.2% | 71.2% | -0.5 | n/a | no target |
| P11 | 17418 | 10.3% | 10.3% | -5.8 | n/a | no target |
| P12 | 7 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P13 | 17697 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `number_of_bids`

> ceiling: published by some portals only (bids&tenders submission lists, Biddingo bidder lists); federal proactive disclosure does not publish bid counts

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 125 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P01T | 398 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P01_GOLD | 625 | 16.8% | 16.8% | +0.0 | 60% | ❌ 43 pts to go · rows from a source that publishes bids: 363 rows, 28.9% filled |
| P02 | 471 | 11.0% | 11.0% | -0.2 | n/a | no target · rows from a source that publishes bids: 290 rows, 17.9% filled |
| P03 | 257 | 13.2% | 13.2% | -0.1 | n/a | no target · rows from a source that publishes bids: 139 rows, 24.5% filled |
| P04 | 3833 | 1.4% | 1.4% | -0.2 | n/a | no target · rows from a source that publishes bids: 872 rows, 6.3% filled |
| P05 | 422 | 2.8% | 2.8% | -0.2 | n/a | no target · rows from a source that publishes bids: 51 rows, 23.5% filled |
| P06M | 13084 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06T | 74208 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06 | 295 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P07 | 800 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P08 | 25539 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P09 | 295 | 3.1% | 3.1% | +0.1 | n/a | no target · rows from a source that publishes bids: 282 rows, 3.2% filled |
| P10R | 100545 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P10 | 2642 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P11 | 17418 | 0.1% | 0.1% | +0.0 | n/a | no target · rows from a source that publishes bids: 88 rows, 13.6% filled |
| P12 | 7 | 0.0% | 0.0% | +0.0 | n/a | no target · rows from a source that publishes bids: 7 rows, 0.0% filled |
| P13 | 17697 | 0.0% | 0.0% | +0.0 | n/a | no target |

## 6. history

### `average_contract_duration_days`

> ceiling: needs two dates (or a published term) on the buyer's records; P09 rows (end date unpublished by definition) and buyers whose sources publish award dates only have no honest duration

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 125 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P01T | 398 | 0.3% | 98.5% | +0.0 | n/a | no target |
| P01_GOLD | 625 | 53.3% | 82.4% | +0.1 | 90% | ❌ 37 pts to go |
| P02 | 471 | 51.8% | 87.7% | -0.7 | 90% | ❌ 38 pts to go |
| P03 | 257 | 45.5% | 80.2% | -0.2 | 90% | ❌ 44 pts to go |
| P04 | 3833 | 18.6% | 94.1% | -2.3 | 90% | ❌ 71 pts to go |
| P05 | 422 | 0.0% | 83.2% | +0.0 | 90% | ❌ 90 pts to go |
| P06M | 13084 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P06T | 74208 | 0.0% | 99.9% | +0.0 | n/a | no target |
| P06 | 295 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P07 | 800 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P08 | 25539 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P09 | 295 | 2.4% | 4.1% | +0.1 | 90% | ❌ 88 pts to go |
| P10R | 100545 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P10 | 2642 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P11 | 17418 | 0.3% | 99.8% | -0.3 | n/a | no target |
| P12 | 7 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P13 | 17697 | 0.0% | 100.0% | +0.0 | n/a | no target |

### `commodity_distribution_top3`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 125 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P01T | 398 | 0.5% | 98.7% | -0.1 | n/a | no target |
| P01_GOLD | 625 | 25.9% | 55.0% | +0.0 | 90% | ❌ 64 pts to go |
| P02 | 471 | 51.0% | 86.8% | -0.6 | n/a | no target |
| P03 | 257 | 24.9% | 59.5% | -0.1 | n/a | no target |
| P04 | 3833 | 20.4% | 95.9% | -2.5 | n/a | no target |
| P05 | 422 | 0.5% | 83.6% | +0.0 | n/a | no target |
| P06M | 13084 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P06T | 74208 | 0.1% | 100.0% | +0.0 | n/a | no target |
| P06 | 295 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P07 | 800 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P08 | 25539 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P09 | 295 | 41.4% | 43.1% | -0.5 | n/a | no target |
| P10R | 100545 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P10 | 2642 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P11 | 17418 | 0.3% | 99.7% | -0.3 | n/a | no target |
| P12 | 7 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P13 | 17697 | 0.0% | 100.0% | +0.0 | n/a | no target |

### `year_over_year_spend_trend`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 125 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P01T | 398 | 1.5% | 99.7% | +0.0 | n/a | no target |
| P01_GOLD | 625 | 51.8% | 81.0% | +0.0 | 95% | ❌ 43 pts to go |
| P02 | 471 | 55.8% | 91.7% | -0.8 | n/a | no target |
| P03 | 257 | 47.9% | 82.5% | -0.1 | n/a | no target |
| P04 | 3833 | 20.6% | 96.1% | -2.5 | n/a | no target |
| P05 | 422 | 4.5% | 87.7% | -0.2 | n/a | no target |
| P06M | 13084 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P06T | 74208 | 0.1% | 100.0% | +0.0 | n/a | no target |
| P06 | 295 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P07 | 800 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P08 | 25539 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P09 | 295 | 63.7% | 65.4% | -0.3 | n/a | no target |
| P10R | 100545 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P10 | 2642 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P11 | 17418 | 0.3% | 99.8% | -0.3 | n/a | no target |
| P12 | 7 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P13 | 17697 | 0.0% | 100.0% | +0.0 | n/a | no target |

## 7. mail security

### `mta_sts`

> ceiling: DNS-only check; 'no record' counts as checked

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 125 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P01T | 398 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P01_GOLD | 625 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P02 | 471 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P03 | 257 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P04 | 3833 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P05 | 422 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P06M | 13084 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P06T | 74208 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P06 | 295 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P07 | 800 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P08 | 25539 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P09 | 295 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P10R | 100545 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P10 | 2642 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P11 | 17418 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P12 | 7 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P13 | 17697 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |

### `tls_rpt`

> ceiling: DNS-only check; 'no record' counts as checked

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 125 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P01T | 398 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P01_GOLD | 625 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P02 | 471 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P03 | 257 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P04 | 3833 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P05 | 422 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P06M | 13084 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P06T | 74208 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P06 | 295 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P07 | 800 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P08 | 25539 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P09 | 295 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P10R | 100545 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P10 | 2642 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P11 | 17418 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P12 | 7 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P13 | 17697 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |

### `bimi`

> ceiling: DNS-only check; 'no record' counts as checked

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 125 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P01T | 398 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P01_GOLD | 625 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P02 | 471 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P03 | 257 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P04 | 3833 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P05 | 422 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P06M | 13084 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P06T | 74208 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P06 | 295 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P07 | 800 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P08 | 25539 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P09 | 295 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P10R | 100545 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P10 | 2642 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P11 | 17418 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P12 | 7 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P13 | 17697 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |

