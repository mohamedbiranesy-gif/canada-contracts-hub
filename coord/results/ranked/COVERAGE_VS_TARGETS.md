# Coverage vs the downstream team's targets — 2026-11-12

Benchmarks (field × package with a numeric target): **92 of 438 met** (21.0%); 63 within 10 points; 283 further away.
A cell counts as filled only when it carries a value: blank, `not_published`, `not_found_yet` and label-only cells ("no identifier published …", "no dataset record …", "0 in the contract dataset …") do not count; the DNS checks count when checked. `any` = share of non-blank cells incl. such labels. Δ = change since the previous build in `coord/results/coverage_history.csv`.
Rows per package: P01M 250, P01T 225, P01_GOLD 626, P02 467, P03 265, P04 3572, P05 424, P06M 22195, P06T 59830, P06 276, P07 820, P08 30285, P09 275, P10R 0, P10 2126, P11 1807, P12 11, P13 152246

## Invoice-grade readiness (the row as an invoice header: bill-to, submit-to, references, terms, tax, vendor identity, follow-up)

| package | rows | all 11 elements | ≥ 9 of 11 | median elements | most-missing element |
|---|---|---|---|---|---|
| P01M | 250 | 0.0% | 14.4% | 7 | vendor GST/HST number (234 rows) |
| P01T | 225 | 1.3% | 37.8% | 8 | payment terms (180 rows) |
| P01_GOLD | 626 | 24.1% | 71.4% | 10 | payment terms (222 rows) |
| P02 | 467 | 7.5% | 55.2% | 9 | PO rule (355 rows) |
| P03 | 265 | 14.7% | 55.8% | 9 | PO rule (132 rows) |
| P04 | 3572 | 1.3% | 17.0% | 6 | PO rule (3372 rows) |
| P05 | 424 | 0.9% | 17.2% | 7 | payment terms (352 rows) |
| P06M | 22195 | 0.0% | 2.8% | 7 | PO rule (21816 rows) |
| P06T | 59830 | 0.1% | 13.0% | 7 | PO rule (59447 rows) |
| P06 | 276 | 0.0% | 10.1% | 6 | reference to quote (PO / contract / vendor id) (258 rows) |
| P07 | 820 | 0.0% | 2.4% | 6 | payment terms (779 rows) |
| P08 | 30285 | 0.0% | 0.9% | 6 | PO rule (30016 rows) |
| P09 | 275 | 1.5% | 42.2% | 8 | payment terms (257 rows) |
| P10 | 2126 | 0.0% | 1.3% | 5 | reference to quote (PO / contract / vendor id) (2126 rows) |
| P11 | 1807 | 0.1% | 7.9% | 6 | PO rule (1741 rows) |
| P12 | 11 | 0.0% | 36.4% | 8 | PO rule (11 rows) |
| P13 | 152246 | 0.0% | 0.3% | 7 | reference to quote (PO / contract / vendor id) (152246 rows) |

## AP grade (how stringently the row's accounts-payable data meets what an invoice needs; A = invoicing mailbox referee-confirmed on the buyer's own domain with MX, legal name, address, PO rule and terms all published, no penalties)

| package | rows | A | B | C | D | E | median ap_score |
|---|---|---|---|---|---|---|---|
| P01M | 250 | 9 | 57 | 184 | 0 | 0 | 70 |
| P01T | 225 | 27 | 35 | 163 | 0 | 0 | 66 |
| P01_GOLD | 626 | 255 | 166 | 205 | 0 | 0 | 82 |
| P02 | 467 | 0 | 191 | 276 | 0 | 0 | 66 |
| P03 | 265 | 0 | 0 | 253 | 12 | 0 | 57 |
| P04 | 3572 | 0 | 0 | 2945 | 627 | 0 | 46 |
| P05 | 424 | 13 | 29 | 369 | 13 | 0 | 51 |
| P06M | 22195 | 0 | 18 | 22122 | 55 | 0 | 46 |
| P06T | 59830 | 0 | 28 | 40257 | 19545 | 0 | 38 |
| P06 | 276 | 18 | 39 | 219 | 0 | 0 | 67 |
| P07 | 820 | 0 | 21 | 778 | 21 | 0 | 54 |
| P08 | 30285 | 0 | 0 | 27102 | 3183 | 0 | 43 |
| P09 | 275 | 5 | 10 | 259 | 1 | 0 | 53 |
| P10 | 2126 | 3 | 13 | 1445 | 665 | 0 | 41 |
| P11 | 1807 | 7 | 12 | 34 | 0 | 1754 | 23 |
| P12 | 11 | 0 | 0 | 11 | 0 | 0 | 51 |
| P13 | 152246 | 14 | 64 | 152156 | 12 | 0 | 43 |

### AP payability (confirmed channel + bill-to legal name and address + the buyer's reference rule + tax treatment known)

| package | rows | payable today | % | most common gap |
|---|---|---|---|---|
| P01M | 250 | 191 | 76.4% | tax treatment (35) |
| P01T | 225 | 137 | 60.9% | bill-to legal name and address (74) |
| P01_GOLD | 626 | 475 | 75.9% | bill-to legal name and address (94) |
| P02 | 467 | 316 | 67.7% | the buyer's PO / reference rule (86) |
| P03 | 265 | 0 | 0.0% | a confirmed invoicing / AP or finance channel (265) |
| P04 | 3572 | 0 | 0.0% | a confirmed invoicing / AP or finance channel (3572) |
| P05 | 424 | 44 | 10.4% | a confirmed invoicing / AP or finance channel (337) |
| P06M | 22195 | 238 | 1.1% | a confirmed invoicing / AP or finance channel (21893) |
| P06T | 59830 | 332 | 0.6% | a confirmed invoicing / AP or finance channel (59024) |
| P06 | 276 | 49 | 17.8% | the buyer's PO / reference rule (116) |
| P07 | 820 | 39 | 4.8% | bill-to legal name and address (331) |
| P08 | 30285 | 0 | 0.0% | a confirmed invoicing / AP or finance channel (30285) |
| P09 | 275 | 40 | 14.5% | a confirmed invoicing / AP or finance channel (224) |
| P10 | 2126 | 7 | 0.3% | a confirmed invoicing / AP or finance channel (2048) |
| P11 | 1807 | 14 | 0.8% | a confirmed invoicing / AP or finance channel (1754) |
| P12 | 11 | 2 | 18.2% | a confirmed invoicing / AP or finance channel (9) |
| P13 | 152246 | 43 | 0.0% | a confirmed invoicing / AP or finance channel (150121) |

### Pay on sight (an invoice generated from the row would clear AP: confirmed invoicing / AP or finance channel, bill-to legal name + address, vendor legal name + GST/HST number + remit-to address, tax treatment and currency known — published or labelled-derived; the buyer's reference rule is reported separately)

| package | rows | pay on sight | % | + reference rule not published | routed (general inbox only) | most common gap |
|---|---|---|---|---|---|---|
| P01M | 250 | 6 | 2.4% | 7 | 0 | the vendor's GST/HST number (BN9) (234) |
| P01T | 225 | 99 | 44.0% | 3 | 0 | the vendor's GST/HST number (BN9) (72) |
| P01_GOLD | 626 | 406 | 64.9% | 11 | 0 | the vendor's GST/HST number (BN9) (143) |
| P02 | 467 | 215 | 46.0% | 22 | 0 | the vendor's GST/HST number (BN9) (203) |
| P03 | 265 | 17 | 6.4% | 0 | 132 | an invoicing / AP or finance mailbox (only a purchasing / general inbo (96) |
| P04 | 3572 | 43 | 1.2% | 7 | 905 | an invoicing / AP or finance mailbox (only a purchasing / general inbo (2557) |
| P05 | 424 | 21 | 5.0% | 8 | 125 | an invoicing / AP or finance mailbox (only a purchasing / general inbo (203) |
| P06M | 22195 | 8 | 0.0% | 12 | 541 | an invoicing / AP or finance mailbox (only a purchasing / general inbo (21258) |
| P06T | 59830 | 385 | 0.6% | 14 | 18667 | an invoicing / AP or finance mailbox (only a purchasing / general inbo (40273) |
| P06 | 276 | 24 | 8.7% | 55 | 0 | the vendor's GST/HST number (BN9) (130) |
| P07 | 820 | 14 | 1.7% | 135 | 36 | the vendor's GST/HST number (BN9) (390) |
| P08 | 30285 | 5 | 0.0% | 13 | 7131 | an invoicing / AP or finance mailbox (only a purchasing / general inbo (23090) |
| P09 | 275 | 37 | 13.5% | 0 | 107 | an invoicing / AP or finance mailbox (only a purchasing / general inbo (105) |
| P10 | 2126 | 7 | 0.3% | 15 | 304 | an invoicing / AP or finance mailbox (only a purchasing / general inbo (1720) |
| P11 | 1807 | 7 | 0.4% | 2 | 0 | a confirmed invoicing / AP or finance channel (1738) |
| P12 | 11 | 1 | 9.1% | 0 | 4 | an invoicing / AP or finance mailbox (only a purchasing / general inbo (5) |
| P13 | 152246 | 21 | 0.0% | 1041 | 60815 | an invoicing / AP or finance mailbox (only a purchasing / general inbo (89123) |
| **all** | 275700 | 1316 | 0.5% | 1345 | 88767 | |

### What still blocks grade A (rows per missing element; a row counts under every element it lacks)

| package | rows not A | referee confirmation of the mailbox | an invoicing / AP mailbox (not finance / procurement / general) | a mailbox on the buyer's own domain | MX record for the mailbox domain | published bill-to legal name | invoice / billing address | published PO rule | published payment terms | clear the penalty |
|---|---|---|---|---|---|---|---|---|---|---|
| P01M | 241 | 0 | 0 | 0 | 164 | 9 | 0 | 196 | 212 | 0 |
| P01T | 198 | 0 | 0 | 0 | 123 | 66 | 31 | 164 | 182 | 4 |
| P01_GOLD | 371 | 0 | 0 | 0 | 13 | 77 | 29 | 202 | 237 | 2 |
| P02 | 467 | 0 | 467 | 0 | 36 | 56 | 14 | 355 | 283 | 2 |
| P03 | 265 | 0 | 265 | 0 | 17 | 45 | 27 | 132 | 139 | 2 |
| P04 | 3572 | 0 | 3572 | 0 | 1524 | 1268 | 959 | 3372 | 3129 | 34 |
| P05 | 411 | 0 | 358 | 0 | 83 | 94 | 39 | 340 | 354 | 7 |
| P06M | 22195 | 0 | 22195 | 0 | 16498 | 1376 | 146 | 21816 | 21569 | 20 |
| P06T | 59830 | 0 | 59830 | 0 | 53646 | 37774 | 24726 | 59447 | 58924 | 375 |
| P06 | 258 | 0 | 0 | 0 | 141 | 78 | 45 | 197 | 225 | 4 |
| P07 | 820 | 0 | 820 | 0 | 558 | 344 | 119 | 778 | 779 | 5 |
| P08 | 30285 | 0 | 30285 | 0 | 23947 | 14591 | 4733 | 30016 | 29659 | 159 |
| P09 | 270 | 0 | 251 | 0 | 12 | 68 | 1 | 245 | 259 | 7 |
| P10 | 2123 | 0 | 2090 | 0 | 1102 | 1131 | 963 | 2055 | 2017 | 16 |
| P11 | 1800 | 1754 | 1707 | 0 | 911 | 1235 | 554 | 1741 | 1734 | 20 |
| P12 | 11 | 0 | 10 | 0 | 0 | 3 | 0 | 11 | 11 | 2 |
| P13 | 152232 | 0 | 151840 | 0 | 122317 | 82871 | 18 | 151910 | 151128 | 60 |

## Where the work is (largest gaps in rows still needed)

| field | package | now | target | rows needed |
|---|---|---|---|---|
| buyer_phone | P13 | 67.9% | 95% | 41299 |
| buyer_ap_cycle_published | P13 | 0.0% | 20% | 30401 |
| ap_system_hint | P13 | 0.4% | 20% | 29858 |
| buyer_bn_as_published | P13 | 12.5% | 30% | 26639 |
| buyer_esignature_preference | P13 | 0.1% | 15% | 22696 |
| buyer_tax_exempt_status | P13 | 0.1% | 15% | 22653 |
| buyer_legal_name_as_published | P13 | 45.6% | 60% | 21973 |
| buyer_payment_method_preference | P13 | 0.6% | 15% | 21866 |
| buyer_logo_url | P13 | 80.8% | 95% | 21631 |
| vendor_registered_address | P08 | 30.1% | 70% | 12086 |
| buyer_ap_cycle_published | P06T | 0.0% | 20% | 11950 |
| ap_system_hint | P06T | 0.6% | 20% | 11619 |
| buyer_phone | P08 | 58.9% | 95% | 10941 |
| buyer_esignature_preference | P06T | 0.2% | 15% | 8868 |
| buyer_tax_exempt_status | P06T | 0.2% | 15% | 8856 |
| buyer_payment_method_preference | P06T | 0.7% | 15% | 8575 |
| buyer_legal_name_as_published | P08 | 51.8% | 75% | 7020 |
| buyer_logo_url | P08 | 78.2% | 100% | 6600 |
| vendor_phone | P08 | 63.8% | 85% | 6410 |
| vendor_emails | P08 | 54.7% | 75% | 6149 |
| buyer_ap_cycle_published | P08 | 0.0% | 20% | 6045 |
| ap_system_hint | P08 | 0.8% | 20% | 5824 |
| vendor_bn9 | P08 | 31.0% | 50% | 5765 |
| vendor_trading_name | P08 | 32.6% | 50% | 5275 |
| buyer_bn_as_published | P08 | 17.9% | 35% | 5184 |
| buyer_esignature_preference | P08 | 0.3% | 15% | 4442 |
| buyer_tax_exempt_status | P08 | 0.3% | 15% | 4441 |
| buyer_ap_cycle_published | P06M | 0.1% | 20% | 4427 |
| buyer_payment_method_preference | P08 | 0.5% | 15% | 4385 |
| ap_system_hint | P06M | 1.0% | 20% | 4210 |
| invoice_reference_hint | P08 | 12.3% | 25% | 3857 |
| vendor_logo_url | P08 | 87.3% | 100% | 3844 |
| buyer_esignature_preference | P06M | 0.4% | 15% | 3233 |
| buyer_address | P08 | 84.3% | 95% | 3227 |
| buyer_tax_exempt_status | P06M | 0.6% | 15% | 3188 |
| buyer_payment_method_preference | P06M | 0.8% | 15% | 3157 |
| average_contract_duration_days | P04 | 19.7% | 90% | 2512 |
| currency | P04 | 27.0% | 95% | 2428 |
| end_date | P04 | 24.6% | 90% | 2335 |
| ap_phone | P04 | 20.3% | 85% | 2311 |

## 1. identifiers

### `invoice_reference_hint`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 250 | 93.2% | 93.2% | +4.1 | 50% | ✅ met |
| P01T | 225 | 95.6% | 95.6% | +1.8 | 50% | ✅ met |
| P01_GOLD | 626 | 92.0% | 94.6% | -0.2 | 95% | 🟡 3 pts to go |
| P02 | 467 | 74.9% | 76.4% | +0.9 | 95% | ❌ 20 pts to go |
| P03 | 265 | 81.5% | 84.9% | +0.1 | 95% | ❌ 14 pts to go |
| P04 | 3572 | 31.9% | 33.6% | +1.7 | 90% | ❌ 58 pts to go |
| P05 | 424 | 39.6% | 42.5% | +1.0 | 70% | ❌ 30 pts to go |
| P06M | 22195 | 93.2% | 93.2% | +1.4 | n/a | no target |
| P06T | 59830 | 99.3% | 99.3% | +0.7 | n/a | no target |
| P06 | 276 | 34.8% | 34.8% | +0.4 | 30% | ✅ met |
| P07 | 820 | 14.3% | 14.3% | +7.4 | 30% | ❌ 16 pts to go |
| P08 | 30285 | 12.3% | 12.3% | +11.0 | 25% | ❌ 13 pts to go |
| P09 | 275 | 98.9% | 99.6% | -0.1 | 100% | 🟡 1 pts to go |
| P10 | 2126 | 3.3% | 3.3% | +0.2 | 25% | ❌ 22 pts to go |
| P11 | 1807 | 54.5% | 55.2% | +7.6 | 60% | 🟡 6 pts to go |
| P12 | 11 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P13 | 152246 | 99.6% | 99.6% | -0.1 | 0% by design | — leave (by design) |

### `po_number_as_published`

> ceiling: a purchase-order number exists only where the buyer publishes PO-level data (Montréal, Laval, Toronto open data so far) or the record itself carries one; most sources publish awards, not POs — the target cannot be reached from public data for most buyers

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 250 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P01T | 225 | 0.0% | 0.0% | +0.0 | 10% | 🟡 10 pts to go |
| P01_GOLD | 626 | 5.9% | 5.9% | -0.2 | 50% | ❌ 44 pts to go |
| P02 | 467 | 5.8% | 5.8% | -0.4 | 50% | ❌ 44 pts to go |
| P03 | 265 | 1.9% | 1.9% | +0.4 | 40% | ❌ 38 pts to go |
| P04 | 3572 | 0.6% | 0.6% | +0.1 | 30% | ❌ 29 pts to go |
| P05 | 424 | 0.2% | 0.2% | +0.0 | 20% | ❌ 20 pts to go |
| P06M | 22195 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06T | 59830 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06 | 276 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P07 | 820 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P08 | 30285 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P09 | 275 | 0.7% | 0.7% | +0.0 | 50% | ❌ 49 pts to go |
| P10 | 2126 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P11 | 1807 | 0.2% | 0.2% | -0.1 | n/a | no target |
| P12 | 11 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P13 | 152246 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `contract_or_agreement_number`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 250 | 89.6% | 89.6% | +7.4 | n/a | no target |
| P01T | 225 | 80.0% | 80.0% | +5.5 | 50% | ✅ met |
| P01_GOLD | 626 | 67.7% | 67.7% | +0.9 | 85% | ❌ 17 pts to go |
| P02 | 467 | 65.7% | 65.7% | +0.9 | 90% | ❌ 24 pts to go |
| P03 | 265 | 60.4% | 60.4% | +0.7 | 85% | ❌ 25 pts to go |
| P04 | 3572 | 29.1% | 29.1% | +1.5 | 85% | ❌ 56 pts to go |
| P05 | 424 | 30.0% | 30.0% | +1.1 | 60% | ❌ 30 pts to go |
| P06M | 22195 | 92.9% | 92.9% | +1.4 | n/a | no target |
| P06T | 59830 | 99.2% | 99.2% | +0.8 | n/a | no target |
| P06 | 276 | 6.5% | 6.5% | +6.5 | n/a | no target |
| P07 | 820 | 9.1% | 9.1% | +9.1 | n/a | no target |
| P08 | 30285 | 11.4% | 11.4% | +11.4 | n/a | no target |
| P09 | 275 | 95.6% | 95.6% | -0.5 | 100% | 🟡 4 pts to go |
| P10 | 2126 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P11 | 1807 | 51.7% | 51.7% | +8.4 | 60% | 🟡 8 pts to go |
| P12 | 11 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P13 | 152246 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `solicitation_or_tender_number`

> ceiling: SEAO's 'numero' is the organisation's own reference for the notice (SEAO data dictionary) and is reported here; sources that publish awards under a tender number only (bids&tenders, SaskTenders, BC) also carry it as the contract reference, labelled

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 250 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P01T | 225 | 0.0% | 0.0% | +0.0 | 30% | ❌ 30 pts to go |
| P01_GOLD | 626 | 51.4% | 51.4% | +0.6 | 80% | ❌ 29 pts to go |
| P02 | 467 | 57.8% | 57.8% | +0.9 | 60% | 🟡 2 pts to go |
| P03 | 265 | 50.6% | 50.6% | +0.4 | 80% | ❌ 29 pts to go |
| P04 | 3572 | 24.0% | 24.0% | +1.1 | 50% | ❌ 26 pts to go |
| P05 | 424 | 12.7% | 12.7% | +1.3 | 40% | ❌ 27 pts to go |
| P06M | 22195 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06T | 59830 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06 | 276 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P07 | 820 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P08 | 30285 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P09 | 275 | 81.1% | 81.1% | -2.3 | 50% | ✅ met |
| P10 | 2126 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P11 | 1807 | 3.3% | 3.3% | -2.3 | 40% | ❌ 37 pts to go |
| P12 | 11 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P13 | 152246 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `award_or_notice_id`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 250 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P01T | 225 | 0.4% | 0.4% | -0.1 | n/a | no target |
| P01_GOLD | 626 | 61.0% | 61.0% | +0.6 | 85% | ❌ 24 pts to go |
| P02 | 467 | 58.0% | 58.0% | +1.8 | 90% | ❌ 32 pts to go |
| P03 | 265 | 59.2% | 59.2% | +0.6 | 85% | ❌ 26 pts to go |
| P04 | 3572 | 25.0% | 25.0% | +1.4 | 85% | ❌ 60 pts to go |
| P05 | 424 | 20.5% | 20.5% | +0.8 | 50% | ❌ 30 pts to go |
| P06M | 22195 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06T | 59830 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06 | 276 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P07 | 820 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P08 | 30285 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P09 | 275 | 97.1% | 97.1% | +0.0 | 100% | 🟡 3 pts to go |
| P10 | 2126 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P11 | 1807 | 3.7% | 3.7% | -2.3 | 60% | ❌ 56 pts to go |
| P12 | 11 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P13 | 152246 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `buyer_vendor_id`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 250 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P01T | 225 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P01_GOLD | 626 | 12.8% | 12.8% | -0.1 | 60% | ❌ 47 pts to go |
| P02 | 467 | 6.9% | 6.9% | +0.9 | 50% | ❌ 43 pts to go |
| P03 | 265 | 8.7% | 8.7% | +0.3 | 50% | ❌ 41 pts to go |
| P04 | 3572 | 2.0% | 2.0% | +0.2 | 40% | ❌ 38 pts to go |
| P05 | 424 | 0.7% | 0.7% | +0.0 | 20% | ❌ 19 pts to go |
| P06M | 22195 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06T | 59830 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06 | 276 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P07 | 820 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P08 | 30285 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P09 | 275 | 3.6% | 3.6% | +0.3 | 50% | ❌ 46 pts to go |
| P10 | 2126 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P11 | 1807 | 0.4% | 0.4% | -0.5 | n/a | no target |
| P12 | 11 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P13 | 152246 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `commodity_codes`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 250 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P01T | 225 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P01_GOLD | 626 | 35.8% | 35.8% | +1.0 | 80% | ❌ 44 pts to go |
| P02 | 467 | 52.5% | 52.5% | +0.6 | 90% | ❌ 38 pts to go |
| P03 | 265 | 34.0% | 34.0% | +1.3 | 80% | ❌ 46 pts to go |
| P04 | 3572 | 22.3% | 22.3% | +0.7 | 85% | ❌ 63 pts to go |
| P05 | 424 | 6.6% | 6.6% | +1.1 | 50% | ❌ 43 pts to go |
| P06M | 22195 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06T | 59830 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06 | 276 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P07 | 820 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P08 | 30285 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P09 | 275 | 73.1% | 73.1% | -1.2 | 95% | ❌ 22 pts to go |
| P10 | 2126 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P11 | 1807 | 2.7% | 2.7% | -1.6 | 50% | ❌ 47 pts to go |
| P12 | 11 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P13 | 152246 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `buyer_org_codes`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 250 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P01T | 225 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P01_GOLD | 626 | 8.3% | 8.3% | -0.2 | 50% | ❌ 42 pts to go |
| P02 | 467 | 5.6% | 5.6% | -0.6 | 50% | ❌ 44 pts to go |
| P03 | 265 | 2.6% | 2.6% | +0.7 | 30% | ❌ 27 pts to go |
| P04 | 3572 | 0.6% | 0.6% | +0.1 | 30% | ❌ 29 pts to go |
| P05 | 424 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06M | 22195 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06T | 59830 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06 | 276 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P07 | 820 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P08 | 30285 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P09 | 275 | 0.4% | 0.4% | +0.1 | n/a | no target |
| P10 | 2126 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P11 | 1807 | 0.2% | 0.2% | -0.1 | n/a | no target |
| P12 | 11 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P13 | 152246 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `records_with_this_vendor`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 250 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P01T | 225 | 100.0% | 100.0% | +0.0 | 60% | ✅ met |
| P01_GOLD | 626 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P02 | 467 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P03 | 265 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P04 | 3572 | 100.0% | 100.0% | +0.0 | 95% | ✅ met |
| P05 | 424 | 100.0% | 100.0% | +0.0 | 70% | ✅ met |
| P06M | 22195 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P06T | 59830 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P06 | 276 | 100.0% | 100.0% | +0.0 | 50% | ✅ met |
| P07 | 820 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P08 | 30285 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P09 | 275 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P10 | 2126 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P11 | 1807 | 100.0% | 100.0% | +0.0 | 70% | ✅ met |
| P12 | 11 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P13 | 152246 | 0.0% | 0.0% | +0.0 | n/a | no target |

## 2. vendor

### `vendor_bn9`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 250 | 6.4% | 6.4% | -5.2 | 70% | ❌ 64 pts to go |
| P01T | 225 | 60.4% | 60.4% | +9.9 | 60% | ✅ met |
| P01_GOLD | 626 | 74.9% | 74.9% | +0.1 | 90% | ❌ 15 pts to go |
| P02 | 467 | 54.0% | 54.0% | +0.4 | 85% | ❌ 31 pts to go |
| P03 | 265 | 66.8% | 66.8% | -2.8 | 90% | ❌ 23 pts to go |
| P04 | 3572 | 38.3% | 38.3% | +3.3 | 75% | ❌ 37 pts to go |
| P05 | 424 | 54.7% | 54.7% | +0.0 | 50% | ✅ met |
| P06M | 22195 | 2.9% | 2.9% | -0.3 | n/a | no target |
| P06T | 59830 | 64.5% | 64.5% | +17.2 | n/a | no target |
| P06 | 276 | 42.4% | 42.4% | -1.6 | 40% | ✅ met |
| P07 | 820 | 32.6% | 32.6% | -0.4 | 50% | ❌ 17 pts to go |
| P08 | 30285 | 31.0% | 31.0% | +0.5 | 50% | ❌ 19 pts to go |
| P09 | 275 | 57.1% | 57.1% | -1.2 | 80% | ❌ 23 pts to go |
| P10 | 2126 | 38.8% | 38.8% | +4.3 | 40% | 🟡 1 pts to go |
| P11 | 1807 | 54.8% | 54.8% | +7.9 | 60% | 🟡 5 pts to go |
| P12 | 11 | 45.5% | 45.5% | -14.5 | 85% | ❌ 40 pts to go |
| P13 | 152246 | 44.8% | 44.8% | +13.1 | 0% by design | — leave (by design) |

### `vendor_registered_address`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 250 | 46.8% | 46.8% | -12.9 | n/a | no target |
| P01T | 225 | 60.0% | 60.0% | +9.0 | n/a | no target |
| P01_GOLD | 626 | 73.0% | 73.0% | +0.3 | 95% | ❌ 22 pts to go |
| P02 | 467 | 74.1% | 74.1% | +0.3 | 95% | ❌ 21 pts to go |
| P03 | 265 | 69.4% | 69.4% | -2.5 | 95% | ❌ 26 pts to go |
| P04 | 3572 | 53.1% | 53.1% | +3.9 | 95% | ❌ 42 pts to go |
| P05 | 424 | 58.3% | 58.3% | +0.0 | 70% | ❌ 12 pts to go |
| P06M | 22195 | 41.3% | 41.3% | -4.7 | n/a | no target |
| P06T | 59830 | 67.5% | 67.5% | +11.3 | n/a | no target |
| P06 | 276 | 38.0% | 38.0% | -3.0 | 80% | ❌ 42 pts to go |
| P07 | 820 | 31.5% | 31.5% | -0.4 | 70% | ❌ 38 pts to go |
| P08 | 30285 | 30.1% | 30.1% | -0.2 | 70% | ❌ 40 pts to go |
| P09 | 275 | 86.2% | 86.2% | -0.4 | 100% | ❌ 14 pts to go |
| P10 | 2126 | 39.2% | 39.2% | +3.7 | 70% | ❌ 31 pts to go |
| P11 | 1807 | 58.9% | 58.9% | +6.4 | 75% | ❌ 16 pts to go |
| P12 | 11 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P13 | 152246 | 40.2% | 40.2% | +13.3 | n/a | no target |

### `vendor_trading_name`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 250 | 21.6% | 21.6% | +4.5 | n/a | no target |
| P01T | 225 | 65.8% | 65.8% | +12.2 | n/a | no target |
| P01_GOLD | 626 | 48.9% | 48.9% | -0.9 | 60% | ❌ 11 pts to go |
| P02 | 467 | 55.7% | 55.7% | -0.5 | 60% | 🟡 4 pts to go |
| P03 | 265 | 51.7% | 51.7% | -3.4 | 60% | 🟡 8 pts to go |
| P04 | 3572 | 42.7% | 42.7% | +0.6 | 55% | ❌ 12 pts to go |
| P05 | 424 | 22.9% | 22.9% | -1.7 | 50% | ❌ 27 pts to go |
| P06M | 22195 | 9.6% | 9.6% | +2.8 | n/a | no target |
| P06T | 59830 | 67.9% | 67.9% | +17.0 | n/a | no target |
| P06 | 276 | 47.8% | 47.8% | +0.2 | n/a | no target |
| P07 | 820 | 39.1% | 39.1% | -1.8 | 55% | ❌ 16 pts to go |
| P08 | 30285 | 32.6% | 32.6% | -3.6 | 50% | ❌ 17 pts to go |
| P09 | 275 | 72.0% | 72.0% | -0.3 | 70% | ✅ met |
| P10 | 2126 | 48.1% | 48.1% | +1.3 | 55% | 🟡 7 pts to go |
| P11 | 1807 | 58.9% | 58.9% | +6.7 | 50% | ✅ met |
| P12 | 11 | 90.9% | 90.9% | +4.2 | n/a | no target |
| P13 | 152246 | 3.2% | 3.2% | -0.2 | n/a | no target |

### `vendor_phone`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 250 | 33.2% | 33.2% | -17.2 | n/a | no target |
| P01T | 225 | 79.6% | 79.6% | +5.1 | n/a | no target |
| P01_GOLD | 626 | 50.6% | 50.6% | +0.1 | 70% | ❌ 19 pts to go |
| P02 | 467 | 56.7% | 56.7% | -1.5 | 70% | ❌ 13 pts to go |
| P03 | 265 | 50.2% | 50.2% | -1.1 | 70% | ❌ 20 pts to go |
| P04 | 3572 | 54.9% | 54.9% | +0.8 | 65% | ❌ 10 pts to go |
| P05 | 424 | 29.0% | 29.0% | +0.6 | 60% | ❌ 31 pts to go |
| P06M | 22195 | 27.5% | 27.5% | -9.1 | n/a | no target |
| P06T | 59830 | 82.7% | 82.7% | +2.7 | n/a | no target |
| P06 | 276 | 69.2% | 69.2% | +0.3 | 40% | ✅ met |
| P07 | 820 | 64.5% | 64.5% | -0.4 | 85% | ❌ 20 pts to go |
| P08 | 30285 | 63.8% | 63.8% | -1.5 | 85% | ❌ 21 pts to go |
| P09 | 275 | 56.4% | 56.4% | -2.9 | 85% | ❌ 29 pts to go |
| P10 | 2126 | 66.1% | 66.1% | +2.6 | 85% | ❌ 19 pts to go |
| P11 | 1807 | 68.0% | 68.0% | +6.1 | 75% | 🟡 7 pts to go |
| P12 | 11 | 36.4% | 36.4% | +9.7 | n/a | no target |
| P13 | 152246 | 91.8% | 91.8% | +0.6 | 60% | ✅ met |

### `vendor_website`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 250 | 37.6% | 37.6% | -19.0 | n/a | no target |
| P01T | 225 | 98.2% | 98.2% | +0.8 | n/a | no target |
| P01_GOLD | 626 | 78.6% | 78.6% | -1.0 | 90% | ❌ 11 pts to go |
| P02 | 467 | 82.0% | 82.0% | -1.9 | 90% | 🟡 8 pts to go |
| P03 | 265 | 85.3% | 85.3% | -2.5 | 90% | 🟡 5 pts to go |
| P04 | 3572 | 82.9% | 82.9% | -1.5 | 85% | 🟡 2 pts to go |
| P05 | 424 | 44.6% | 44.6% | -0.2 | 70% | ❌ 25 pts to go |
| P06M | 22195 | 33.1% | 33.1% | -10.5 | n/a | no target |
| P06T | 59830 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P06 | 276 | 99.3% | 99.3% | +0.0 | 50% | ✅ met |
| P07 | 820 | 99.9% | 99.9% | +0.0 | 100% | 🟡 0 pts to go |
| P08 | 30285 | 99.9% | 99.9% | +0.1 | 100% | 🟡 0 pts to go |
| P09 | 275 | 77.8% | 77.8% | -2.0 | 100% | ❌ 22 pts to go |
| P10 | 2126 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P11 | 1807 | 98.0% | 98.0% | +0.7 | 100% | 🟡 2 pts to go |
| P12 | 11 | 54.5% | 54.5% | +1.2 | n/a | no target |
| P13 | 152246 | 100.0% | 100.0% | +0.0 | n/a | no target |

### `vendor_emails`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 250 | 15.6% | 15.6% | +0.1 | n/a | no target |
| P01T | 225 | 59.6% | 59.6% | -5.5 | n/a | no target |
| P01_GOLD | 626 | 43.8% | 43.8% | +0.3 | 70% | ❌ 26 pts to go |
| P02 | 467 | 46.9% | 46.9% | -1.8 | 75% | ❌ 28 pts to go |
| P03 | 265 | 44.5% | 44.5% | +1.2 | 75% | ❌ 30 pts to go |
| P04 | 3572 | 38.7% | 38.7% | +0.0 | 70% | ❌ 31 pts to go |
| P05 | 424 | 21.5% | 21.5% | -0.5 | 55% | ❌ 34 pts to go |
| P06M | 22195 | 6.0% | 6.0% | +1.2 | n/a | no target |
| P06T | 59830 | 47.4% | 47.4% | -14.7 | n/a | no target |
| P06 | 276 | 51.8% | 51.8% | +4.9 | n/a | no target |
| P07 | 820 | 52.8% | 52.8% | +2.8 | 70% | ❌ 17 pts to go |
| P08 | 30285 | 54.7% | 54.7% | -0.1 | 75% | ❌ 20 pts to go |
| P09 | 275 | 46.9% | 46.9% | -2.3 | 85% | ❌ 38 pts to go |
| P10 | 2126 | 44.4% | 44.4% | +0.8 | 80% | ❌ 36 pts to go |
| P11 | 1807 | 53.3% | 53.3% | -1.0 | 70% | ❌ 17 pts to go |
| P12 | 11 | 27.3% | 27.3% | -12.7 | n/a | no target |
| P13 | 152246 | 5.5% | 5.5% | +0.3 | n/a | no target |

### `vendor_logo_url`

> ceiling: needs the vendor's website first; sites that block automated readers (robots.txt / 403) are never read

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 250 | 37.6% | 37.6% | -19.0 | n/a | no target |
| P01T | 225 | 96.4% | 96.4% | +1.6 | n/a | no target |
| P01_GOLD | 626 | 72.8% | 72.8% | -1.0 | 90% | ❌ 17 pts to go |
| P02 | 467 | 76.9% | 76.9% | -2.1 | 90% | ❌ 13 pts to go |
| P03 | 265 | 81.9% | 81.9% | -1.4 | 90% | 🟡 8 pts to go |
| P04 | 3572 | 77.7% | 77.7% | +1.3 | 85% | 🟡 7 pts to go |
| P05 | 424 | 42.9% | 42.9% | -0.2 | 75% | ❌ 32 pts to go |
| P06M | 22195 | 33.0% | 33.0% | -10.3 | n/a | no target |
| P06T | 59830 | 98.3% | 98.3% | +1.6 | n/a | no target |
| P06 | 276 | 89.9% | 89.9% | -0.6 | n/a | no target |
| P07 | 820 | 91.7% | 91.7% | -0.8 | 100% | 🟡 8 pts to go |
| P08 | 30285 | 87.3% | 87.3% | -3.5 | 100% | ❌ 13 pts to go |
| P09 | 275 | 66.5% | 66.5% | +0.4 | n/a | no target |
| P10 | 2126 | 90.3% | 90.3% | +3.5 | 100% | 🟡 10 pts to go |
| P11 | 1807 | 90.1% | 90.1% | +2.4 | n/a | no target |
| P12 | 11 | 54.5% | 54.5% | +7.8 | n/a | no target |
| P13 | 152246 | 69.8% | 69.8% | +4.6 | n/a | no target |

### `vendor_neq`

> ceiling: only Québec-registered vendors have an NEQ; the share of QC vendors is reported next to the rate

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 250 | 37.2% | 37.2% | -9.3 | n/a | no target · QC vendors: 49 rows, 100.0% filled |
| P01T | 225 | 19.6% | 19.6% | +10.2 | n/a | no target · QC vendors: 33 rows, 87.9% filled |
| P01_GOLD | 626 | 43.5% | 43.5% | -0.3 | 95% | ❌ 52 pts to go · QC vendors: 50 rows, 98.0% filled |
| P02 | 467 | 55.9% | 55.9% | +0.3 | 95% | ❌ 39 pts to go · QC vendors: 111 rows, 100.0% filled |
| P03 | 265 | 42.6% | 42.6% | -3.4 | 95% | ❌ 52 pts to go · QC vendors: 19 rows, 100.0% filled |
| P04 | 3572 | 32.5% | 32.5% | +0.3 | 95% | ❌ 62 pts to go · QC vendors: 598 rows, 98.0% filled |
| P05 | 424 | 14.4% | 14.4% | +0.4 | n/a | no target · QC vendors: 36 rows, 100.0% filled |
| P06M | 22195 | 37.5% | 37.5% | -5.3 | n/a | no target · QC vendors: 6584 rows, 99.9% filled |
| P06T | 59830 | 30.6% | 30.6% | +25.3 | n/a | no target · QC vendors: 18604 rows, 95.7% filled |
| P06 | 276 | 6.9% | 6.9% | -1.5 | n/a | no target · QC vendors: 12 rows, 66.7% filled |
| P07 | 820 | 7.0% | 7.0% | +0.7 | n/a | no target · QC vendors: 47 rows, 78.7% filled |
| P08 | 30285 | 7.1% | 7.1% | +0.5 | n/a | no target · QC vendors: 1796 rows, 95.0% filled |
| P09 | 275 | 73.5% | 73.5% | -3.4 | 95% | ❌ 22 pts to go · QC vendors: 98 rows, 100.0% filled |
| P10 | 2126 | 15.7% | 15.7% | +0.1 | n/a | no target · QC vendors: 202 rows, 92.6% filled |
| P11 | 1807 | 19.6% | 19.6% | +4.8 | n/a | no target · QC vendors: 299 rows, 94.6% filled |
| P12 | 11 | 81.8% | 81.8% | +8.5 | n/a | no target · QC vendors: 2 rows, 100.0% filled |
| P13 | 152246 | 22.2% | 22.2% | -4.0 | n/a | no target · QC vendors: 33803 rows, 100.0% filled |

### `vendor_years_in_business`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 250 | 46.0% | 46.0% | -12.9 | n/a | no target · vendors with a registry record: 115 rows, 100.0% filled |
| P01T | 225 | 60.0% | 60.0% | +9.0 | n/a | no target · vendors with a registry record: 135 rows, 100.0% filled |
| P01_GOLD | 626 | 81.0% | 81.0% | -0.5 | 100% | ❌ 19 pts to go · vendors with a registry record: 507 rows, 100.0% filled |
| P02 | 467 | 77.9% | 77.9% | +0.4 | 100% | ❌ 22 pts to go · vendors with a registry record: 364 rows, 100.0% filled |
| P03 | 265 | 78.1% | 78.1% | -2.9 | 100% | ❌ 22 pts to go · vendors with a registry record: 207 rows, 100.0% filled |
| P04 | 3572 | 54.0% | 54.0% | +4.3 | 100% | ❌ 46 pts to go · vendors with a registry record: 1930 rows, 100.0% filled |
| P05 | 424 | 63.0% | 63.0% | -0.3 | n/a | no target · vendors with a registry record: 267 rows, 100.0% filled |
| P06M | 22195 | 41.2% | 41.2% | -4.7 | n/a | no target · vendors with a registry record: 9153 rows, 100.0% filled |
| P06T | 59830 | 67.6% | 67.6% | +11.4 | n/a | no target · vendors with a registry record: 40422 rows, 100.0% filled |
| P06 | 276 | 39.1% | 39.1% | -2.3 | n/a | no target · vendors with a registry record: 108 rows, 100.0% filled |
| P07 | 820 | 32.2% | 32.2% | -0.1 | n/a | no target · vendors with a registry record: 264 rows, 100.0% filled |
| P08 | 30285 | 30.3% | 30.3% | -0.1 | n/a | no target · vendors with a registry record: 9187 rows, 100.0% filled |
| P09 | 275 | 89.5% | 89.5% | -1.1 | n/a | no target · vendors with a registry record: 246 rows, 100.0% filled |
| P10 | 2126 | 40.1% | 40.1% | +3.9 | n/a | no target · vendors with a registry record: 853 rows, 100.0% filled |
| P11 | 1807 | 59.7% | 59.7% | +6.1 | n/a | no target · vendors with a registry record: 1078 rows, 100.0% filled |
| P12 | 11 | 100.0% | 100.0% | +0.0 | n/a | no target · vendors with a registry record: 11 rows, 100.0% filled |
| P13 | 152246 | 40.2% | 40.2% | +13.3 | n/a | no target · vendors with a registry record: 61221 rows, 100.0% filled |

## 3. buyer

### `buyer_legal_name_as_published`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 250 | 96.4% | 96.4% | +2.6 | 90% | ✅ met |
| P01T | 225 | 70.7% | 70.7% | -1.7 | 90% | ❌ 19 pts to go |
| P01_GOLD | 626 | 87.7% | 87.7% | +0.0 | 95% | 🟡 7 pts to go |
| P02 | 467 | 88.0% | 88.0% | +0.2 | 95% | 🟡 7 pts to go |
| P03 | 265 | 83.0% | 83.0% | -1.4 | 85% | 🟡 2 pts to go |
| P04 | 3572 | 64.5% | 64.5% | +1.5 | 90% | ❌ 26 pts to go |
| P05 | 424 | 77.8% | 77.8% | -1.3 | 75% | ✅ met |
| P06M | 22195 | 93.8% | 93.8% | +2.2 | n/a | no target |
| P06T | 59830 | 36.9% | 36.9% | -0.4 | n/a | no target |
| P06 | 276 | 71.7% | 71.7% | -1.9 | 80% | 🟡 8 pts to go |
| P07 | 820 | 58.0% | 58.2% | -1.8 | 80% | ❌ 22 pts to go |
| P08 | 30285 | 51.8% | 51.8% | -2.6 | 75% | ❌ 23 pts to go |
| P09 | 275 | 75.3% | 75.3% | -1.6 | 95% | ❌ 20 pts to go |
| P10 | 2126 | 46.8% | 46.8% | +0.1 | 70% | ❌ 23 pts to go |
| P11 | 1807 | 31.7% | 31.7% | +0.4 | 65% | ❌ 33 pts to go |
| P12 | 11 | 72.7% | 72.7% | -7.3 | 80% | 🟡 7 pts to go |
| P13 | 152246 | 45.6% | 45.6% | -1.9 | 60% | ❌ 14 pts to go |

### `buyer_bn_as_published`

> ceiling: a buyer's BN is public only where the buyer prints it or a public dataset carries it (CRA charities, federal grants & contributions recipients, business registries for corporations); municipalities rarely publish theirs

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 250 | 18.0% | 18.0% | -2.2 | 50% | ❌ 32 pts to go |
| P01T | 225 | 15.1% | 15.1% | -1.0 | n/a | no target |
| P01_GOLD | 626 | 19.6% | 19.6% | +0.1 | 40% | ❌ 20 pts to go |
| P02 | 467 | 19.9% | 19.9% | +0.8 | 40% | ❌ 20 pts to go |
| P03 | 265 | 20.4% | 20.4% | -0.9 | 40% | ❌ 20 pts to go |
| P04 | 3572 | 16.2% | 16.2% | +1.0 | 40% | ❌ 24 pts to go |
| P05 | 424 | 20.8% | 20.8% | +3.3 | 25% | 🟡 4 pts to go |
| P06M | 22195 | 20.5% | 20.5% | +8.9 | n/a | no target |
| P06T | 59830 | 7.5% | 7.5% | +0.6 | n/a | no target |
| P06 | 276 | 17.8% | 17.8% | +5.0 | 35% | ❌ 17 pts to go |
| P07 | 820 | 19.4% | 19.4% | +5.3 | 35% | ❌ 16 pts to go |
| P08 | 30285 | 17.9% | 17.9% | +2.5 | 35% | ❌ 17 pts to go |
| P09 | 275 | 16.7% | 16.7% | +0.4 | n/a | no target |
| P10 | 2126 | 7.1% | 7.1% | +0.4 | 30% | ❌ 23 pts to go |
| P11 | 1807 | 6.5% | 6.5% | -0.9 | n/a | no target |
| P12 | 11 | 18.2% | 18.2% | +11.5 | n/a | no target |
| P13 | 152246 | 12.5% | 12.5% | +0.2 | 30% | ❌ 18 pts to go |

### `buyer_address`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 250 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P01T | 225 | 84.9% | 84.9% | +0.5 | 100% | ❌ 15 pts to go |
| P01_GOLD | 626 | 91.1% | 91.1% | +0.4 | 100% | 🟡 9 pts to go |
| P02 | 467 | 96.6% | 96.6% | +1.1 | 100% | 🟡 3 pts to go |
| P03 | 265 | 89.1% | 89.1% | -0.3 | 100% | ❌ 11 pts to go |
| P04 | 3572 | 72.6% | 72.6% | +1.2 | 100% | ❌ 27 pts to go |
| P05 | 424 | 90.1% | 90.1% | +0.8 | 100% | 🟡 10 pts to go |
| P06M | 22195 | 99.3% | 99.3% | +0.1 | n/a | no target |
| P06T | 59830 | 58.7% | 58.7% | -0.6 | n/a | no target |
| P06 | 276 | 82.2% | 82.2% | +3.4 | 95% | ❌ 13 pts to go |
| P07 | 820 | 85.2% | 85.2% | +4.0 | 95% | 🟡 10 pts to go |
| P08 | 30285 | 84.3% | 84.3% | +6.0 | 95% | ❌ 11 pts to go |
| P09 | 275 | 96.4% | 96.4% | +0.3 | 100% | 🟡 4 pts to go |
| P10 | 2126 | 54.6% | 54.7% | +0.2 | 95% | ❌ 40 pts to go |
| P11 | 1807 | 60.9% | 60.9% | +11.5 | 80% | ❌ 19 pts to go |
| P12 | 11 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P13 | 152246 | 100.0% | 100.0% | +0.0 | 95% | ✅ met |

### `buyer_phone`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 250 | 71.2% | 71.2% | -14.8 | n/a | no target |
| P01T | 225 | 74.2% | 74.2% | +6.0 | n/a | no target |
| P01_GOLD | 626 | 73.0% | 73.0% | +0.0 | 90% | ❌ 17 pts to go |
| P02 | 467 | 79.0% | 79.0% | +1.1 | 95% | ❌ 16 pts to go |
| P03 | 265 | 73.6% | 73.6% | -1.3 | 95% | ❌ 21 pts to go |
| P04 | 3572 | 69.7% | 69.7% | +0.8 | 95% | ❌ 25 pts to go |
| P05 | 424 | 72.6% | 72.6% | -0.9 | 90% | ❌ 17 pts to go |
| P06M | 22195 | 76.9% | 76.9% | -10.0 | n/a | no target |
| P06T | 59830 | 58.6% | 58.6% | +1.4 | n/a | no target |
| P06 | 276 | 65.9% | 65.9% | -2.6 | 95% | ❌ 29 pts to go |
| P07 | 820 | 60.0% | 60.0% | -4.8 | 90% | ❌ 30 pts to go |
| P08 | 30285 | 58.9% | 58.9% | -8.9 | 95% | ❌ 36 pts to go |
| P09 | 275 | 85.5% | 85.5% | -1.5 | 100% | ❌ 14 pts to go |
| P10 | 2126 | 53.8% | 53.8% | -1.5 | 95% | ❌ 41 pts to go |
| P11 | 1807 | 30.6% | 30.6% | +1.7 | 75% | ❌ 44 pts to go |
| P12 | 11 | 81.8% | 81.8% | -11.5 | n/a | no target |
| P13 | 152246 | 67.9% | 67.9% | -2.9 | 95% | ❌ 27 pts to go |

### `buyer_logo_url`

> ceiling: sites that block automated readers (robots.txt / 403) are never read; an og:image that looks like a photo is labelled

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 250 | 83.6% | 83.6% | -4.0 | n/a | no target |
| P01T | 225 | 91.1% | 91.1% | +7.8 | 95% | 🟡 4 pts to go |
| P01_GOLD | 626 | 84.8% | 84.8% | +0.0 | 90% | 🟡 5 pts to go |
| P02 | 467 | 91.2% | 91.2% | +0.6 | 95% | 🟡 4 pts to go |
| P03 | 265 | 83.4% | 83.4% | -2.2 | 95% | ❌ 12 pts to go |
| P04 | 3572 | 91.7% | 91.7% | +2.5 | 90% | ✅ met |
| P05 | 424 | 92.5% | 92.5% | -0.6 | 95% | 🟡 2 pts to go |
| P06M | 22195 | 85.5% | 85.5% | -7.7 | n/a | no target |
| P06T | 59830 | 84.6% | 84.6% | +9.7 | n/a | no target |
| P06 | 276 | 85.9% | 85.9% | -6.4 | 100% | ❌ 14 pts to go |
| P07 | 820 | 84.1% | 84.1% | -8.1 | 100% | ❌ 16 pts to go |
| P08 | 30285 | 78.2% | 78.2% | -14.1 | 100% | ❌ 22 pts to go |
| P09 | 275 | 73.8% | 73.8% | +0.8 | n/a | no target |
| P10 | 2126 | 94.4% | 94.4% | +3.1 | 100% | 🟡 6 pts to go |
| P11 | 1807 | 50.9% | 50.9% | +9.0 | 80% | ❌ 29 pts to go |
| P12 | 11 | 90.9% | 90.9% | -9.1 | n/a | no target |
| P13 | 152246 | 80.8% | 80.8% | -2.9 | 95% | ❌ 14 pts to go |

## 4. AP

### `ap_contact_name_as_published`

> ceiling: owner 2026-11-08: the AP contact person the organisation itself names on its AP / finance page is allowed (name + role phrase, quoted); mailboxes stay organisational; many bodies publish no AP person

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 250 | 3.2% | 3.2% | +0.1 | n/a | no target |
| P01T | 225 | 8.9% | 8.9% | -0.5 | n/a | no target |
| P01_GOLD | 626 | 14.2% | 14.2% | +0.0 | 25% | ❌ 11 pts to go |
| P02 | 467 | 24.8% | 24.8% | -0.5 | 40% | ❌ 15 pts to go |
| P03 | 265 | 9.1% | 9.1% | +0.0 | 20% | ❌ 11 pts to go |
| P04 | 3572 | 3.3% | 3.3% | -0.2 | 20% | ❌ 17 pts to go |
| P05 | 424 | 3.1% | 3.1% | -0.2 | 15% | ❌ 12 pts to go |
| P06M | 22195 | 0.3% | 0.3% | +0.0 | n/a | no target |
| P06T | 59830 | 0.2% | 0.2% | -0.1 | n/a | no target |
| P06 | 276 | 5.1% | 5.1% | +0.0 | n/a | no target |
| P07 | 820 | 8.0% | 8.0% | -0.5 | n/a | no target |
| P08 | 30285 | 0.2% | 0.2% | -0.1 | n/a | no target |
| P09 | 275 | 7.6% | 7.6% | -0.2 | n/a | no target |
| P10 | 2126 | 0.8% | 0.8% | +0.0 | n/a | no target |
| P11 | 1807 | 0.7% | 0.7% | -0.3 | n/a | no target |
| P12 | 11 | 0.0% | 0.0% | -6.7 | n/a | no target |
| P13 | 152246 | 0.2% | 0.2% | -0.1 | n/a | no target |

### `ap_phone`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 250 | 15.6% | 15.6% | -3.0 | n/a | no target |
| P01T | 225 | 19.1% | 19.1% | -3.3 | 70% | ❌ 51 pts to go |
| P01_GOLD | 626 | 42.5% | 42.5% | -1.0 | 80% | ❌ 38 pts to go |
| P02 | 467 | 57.4% | 57.4% | +0.1 | 90% | ❌ 33 pts to go |
| P03 | 265 | 18.9% | 18.9% | +0.3 | 60% | ❌ 41 pts to go |
| P04 | 3572 | 20.3% | 20.3% | -1.3 | 85% | ❌ 65 pts to go |
| P05 | 424 | 10.8% | 10.8% | -0.8 | 50% | ❌ 39 pts to go |
| P06M | 22195 | 0.6% | 0.6% | +0.0 | n/a | no target |
| P06T | 59830 | 0.5% | 0.5% | -0.2 | n/a | no target |
| P06 | 276 | 13.4% | 13.4% | -2.0 | n/a | no target |
| P07 | 820 | 9.1% | 9.1% | -1.4 | n/a | no target |
| P08 | 30285 | 0.5% | 0.5% | -0.1 | n/a | no target |
| P09 | 275 | 72.4% | 72.4% | -5.5 | 95% | ❌ 23 pts to go |
| P10 | 2126 | 1.6% | 1.6% | -0.1 | n/a | no target |
| P11 | 1807 | 13.0% | 13.0% | -3.7 | n/a | no target |
| P12 | 11 | 27.3% | 27.3% | +0.6 | n/a | no target |
| P13 | 152246 | 0.3% | 0.3% | -0.2 | n/a | no target |

### `invoice_mailing_address`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 250 | 6.0% | 6.0% | -0.2 | n/a | no target |
| P01T | 225 | 9.8% | 9.8% | -0.6 | n/a | no target |
| P01_GOLD | 626 | 33.9% | 33.9% | -0.1 | 70% | ❌ 36 pts to go |
| P02 | 467 | 39.2% | 39.2% | +0.1 | 75% | ❌ 36 pts to go |
| P03 | 265 | 18.9% | 18.9% | +0.3 | 55% | ❌ 36 pts to go |
| P04 | 3572 | 20.4% | 20.4% | -1.2 | 75% | ❌ 55 pts to go |
| P05 | 424 | 10.1% | 10.1% | -0.6 | 50% | ❌ 40 pts to go |
| P06M | 22195 | 0.2% | 0.2% | +0.0 | n/a | no target |
| P06T | 59830 | 0.3% | 0.3% | -0.1 | n/a | no target |
| P06 | 276 | 5.8% | 5.8% | -0.1 | n/a | no target |
| P07 | 820 | 4.5% | 4.5% | -0.7 | n/a | no target |
| P08 | 30285 | 0.2% | 0.2% | +0.0 | n/a | no target |
| P09 | 275 | 69.1% | 69.1% | -6.1 | 95% | ❌ 26 pts to go |
| P10 | 2126 | 0.8% | 0.8% | -0.1 | n/a | no target |
| P11 | 1807 | 12.7% | 12.7% | -3.7 | n/a | no target |
| P12 | 11 | 18.2% | 18.2% | -1.8 | n/a | no target |
| P13 | 152246 | 0.2% | 0.2% | -0.1 | n/a | no target |

### `invoicing_requirements`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 250 | 7.6% | 7.6% | -0.2 | n/a | no target |
| P01T | 225 | 8.0% | 8.0% | -0.3 | n/a | no target |
| P01_GOLD | 626 | 57.0% | 57.2% | -1.0 | 80% | ❌ 23 pts to go |
| P02 | 467 | 45.4% | 45.6% | -0.3 | 75% | ❌ 30 pts to go |
| P03 | 265 | 35.5% | 35.5% | -1.8 | 70% | ❌ 34 pts to go |
| P04 | 3572 | 20.0% | 20.4% | -1.1 | 70% | ❌ 50 pts to go |
| P05 | 424 | 13.9% | 13.9% | -0.3 | 50% | ❌ 36 pts to go |
| P06M | 22195 | 0.3% | 0.3% | +0.0 | n/a | no target |
| P06T | 59830 | 0.2% | 0.2% | -0.1 | n/a | no target |
| P06 | 276 | 12.7% | 12.7% | -3.8 | n/a | no target |
| P07 | 820 | 1.1% | 1.1% | -0.9 | n/a | no target |
| P08 | 30285 | 0.3% | 0.3% | -0.1 | n/a | no target |
| P09 | 275 | 47.3% | 47.3% | +0.7 | 80% | ❌ 33 pts to go |
| P10 | 2126 | 1.1% | 1.2% | -0.1 | n/a | no target |
| P11 | 1807 | 4.5% | 4.5% | -2.3 | n/a | no target |
| P12 | 11 | 36.4% | 36.4% | -3.6 | n/a | no target |
| P13 | 152246 | 0.1% | 0.1% | -0.1 | n/a | no target |

### `payment_terms_as_published`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 250 | 15.2% | 15.2% | -3.4 | n/a | no target |
| P01T | 225 | 19.1% | 19.1% | -2.3 | 60% | ❌ 41 pts to go |
| P01_GOLD | 626 | 62.1% | 62.1% | -1.3 | 70% | 🟡 8 pts to go |
| P02 | 467 | 39.4% | 39.4% | -0.3 | 50% | ❌ 11 pts to go |
| P03 | 265 | 47.5% | 47.5% | -0.8 | 55% | 🟡 8 pts to go |
| P04 | 3572 | 12.4% | 12.4% | +0.2 | 40% | ❌ 28 pts to go |
| P05 | 424 | 16.5% | 16.5% | -0.6 | 40% | ❌ 24 pts to go |
| P06M | 22195 | 2.8% | 2.8% | +0.6 | n/a | no target |
| P06T | 59830 | 1.5% | 1.5% | -0.2 | n/a | no target |
| P06 | 276 | 18.5% | 18.5% | -3.5 | n/a | no target |
| P07 | 820 | 5.0% | 5.0% | -1.6 | n/a | no target |
| P08 | 30285 | 2.1% | 2.1% | -0.8 | n/a | no target |
| P09 | 275 | 5.8% | 5.8% | -0.1 | n/a | no target |
| P10 | 2126 | 5.1% | 5.1% | +0.5 | n/a | no target |
| P11 | 1807 | 4.0% | 4.0% | -1.2 | n/a | no target |
| P12 | 11 | 0.0% | 0.0% | -6.7 | n/a | no target |
| P13 | 152246 | 0.7% | 0.7% | -0.3 | n/a | no target |

### `po_required_as_published`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 250 | 21.6% | 21.6% | -0.1 | n/a | no target |
| P01T | 225 | 27.1% | 27.1% | -1.5 | 65% | ❌ 38 pts to go |
| P01_GOLD | 626 | 67.7% | 67.7% | -1.3 | 70% | 🟡 2 pts to go |
| P02 | 467 | 24.0% | 24.0% | -0.2 | 50% | ❌ 26 pts to go |
| P03 | 265 | 50.2% | 50.2% | -2.3 | 60% | 🟡 10 pts to go |
| P04 | 3572 | 5.6% | 5.6% | +0.2 | 40% | ❌ 34 pts to go |
| P05 | 424 | 19.8% | 19.8% | +0.1 | 45% | ❌ 25 pts to go |
| P06M | 22195 | 1.7% | 1.7% | +0.3 | n/a | no target |
| P06T | 59830 | 0.6% | 0.6% | -0.1 | n/a | no target |
| P06 | 276 | 28.6% | 28.6% | -5.8 | n/a | no target |
| P07 | 820 | 5.1% | 5.1% | -1.8 | n/a | no target |
| P08 | 30285 | 0.9% | 0.9% | -0.4 | n/a | no target |
| P09 | 275 | 10.9% | 10.9% | +1.1 | n/a | no target |
| P10 | 2126 | 3.3% | 3.3% | +0.2 | n/a | no target |
| P11 | 1807 | 3.7% | 3.7% | -1.4 | n/a | no target |
| P12 | 11 | 0.0% | 0.0% | -6.7 | n/a | no target |
| P13 | 152246 | 0.2% | 0.2% | -0.1 | n/a | no target |

### `invoice_portal_url`

> ceiling: only portals the buyer names on its own pages; informational tax-authority links are not portals

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 250 | 12.0% | 12.0% | -0.4 | n/a | no target |
| P01T | 225 | 12.0% | 12.0% | -1.5 | n/a | no target |
| P01_GOLD | 626 | 49.8% | 49.8% | +0.0 | 50% | 🟡 0 pts to go |
| P02 | 467 | 37.7% | 37.7% | +0.4 | n/a | no target |
| P03 | 265 | 50.6% | 50.6% | -1.5 | 60% | 🟡 9 pts to go |
| P04 | 3572 | 12.8% | 12.8% | +0.9 | n/a | no target |
| P05 | 424 | 15.1% | 15.1% | -0.1 | n/a | no target |
| P06M | 22195 | 0.8% | 0.8% | +0.3 | n/a | no target |
| P06T | 59830 | 0.3% | 0.3% | -0.1 | n/a | no target |
| P06 | 276 | 20.3% | 20.3% | -5.3 | n/a | no target |
| P07 | 820 | 5.7% | 5.7% | -2.6 | n/a | no target |
| P08 | 30285 | 0.4% | 0.4% | -0.2 | n/a | no target |
| P09 | 275 | 20.7% | 20.7% | +3.1 | n/a | no target |
| P10 | 2126 | 2.5% | 2.5% | +0.1 | n/a | no target |
| P11 | 1807 | 2.6% | 2.6% | -2.1 | n/a | no target |
| P12 | 11 | 18.2% | 18.2% | +4.9 | n/a | no target |
| P13 | 152246 | 0.2% | 0.2% | -0.1 | n/a | no target |

### `buyer_payment_method_preference`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 250 | 8.8% | 8.8% | -2.8 | 15% | 🟡 6 pts to go |
| P01T | 225 | 12.0% | 12.0% | -0.5 | 15% | 🟡 3 pts to go |
| P01_GOLD | 626 | 34.8% | 34.8% | -0.5 | 40% | 🟡 5 pts to go |
| P02 | 467 | 12.2% | 12.4% | -0.7 | 25% | ❌ 13 pts to go |
| P03 | 265 | 16.2% | 16.2% | -1.3 | 25% | 🟡 9 pts to go |
| P04 | 3572 | 2.7% | 2.7% | +0.0 | 15% | ❌ 12 pts to go |
| P05 | 424 | 6.6% | 6.6% | +0.0 | 15% | 🟡 8 pts to go |
| P06M | 22195 | 0.8% | 0.8% | -0.1 | 15% | ❌ 14 pts to go |
| P06T | 59830 | 0.7% | 0.7% | +0.2 | 15% | ❌ 14 pts to go |
| P06 | 276 | 9.1% | 9.1% | -1.5 | 15% | 🟡 6 pts to go |
| P07 | 820 | 3.4% | 3.4% | -0.9 | 15% | ❌ 12 pts to go |
| P08 | 30285 | 0.5% | 0.5% | -0.1 | 15% | ❌ 14 pts to go |
| P09 | 275 | 1.1% | 1.1% | +0.1 | 15% | ❌ 14 pts to go |
| P10 | 2126 | 1.4% | 1.4% | +0.1 | 15% | ❌ 14 pts to go |
| P11 | 1807 | 1.3% | 1.3% | -0.2 | 15% | ❌ 14 pts to go |
| P12 | 11 | 0.0% | 0.0% | +0.0 | 15% | ❌ 15 pts to go |
| P13 | 152246 | 0.6% | 0.6% | -0.1 | 15% | ❌ 14 pts to go |

### `buyer_tax_exempt_status`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 250 | 6.0% | 6.0% | +0.6 | 15% | 🟡 9 pts to go |
| P01T | 225 | 11.1% | 11.1% | -0.4 | 25% | ❌ 14 pts to go |
| P01_GOLD | 626 | 29.2% | 29.2% | +0.0 | 25% | ✅ met |
| P02 | 467 | 25.3% | 25.3% | +0.0 | 15% | ✅ met |
| P03 | 265 | 21.5% | 21.5% | -0.6 | 15% | ✅ met |
| P04 | 3572 | 4.0% | 4.0% | +0.0 | 15% | ❌ 11 pts to go |
| P05 | 424 | 11.3% | 11.3% | +0.2 | 15% | 🟡 4 pts to go |
| P06M | 22195 | 0.6% | 0.6% | +0.1 | 15% | ❌ 14 pts to go |
| P06T | 59830 | 0.2% | 0.2% | +0.0 | 15% | ❌ 15 pts to go |
| P06 | 276 | 7.6% | 7.6% | -0.8 | 15% | 🟡 7 pts to go |
| P07 | 820 | 1.8% | 1.8% | -1.1 | 15% | ❌ 13 pts to go |
| P08 | 30285 | 0.3% | 0.3% | -0.2 | 15% | ❌ 15 pts to go |
| P09 | 275 | 1.5% | 1.5% | +0.5 | 15% | ❌ 14 pts to go |
| P10 | 2126 | 1.6% | 1.6% | +0.0 | 15% | ❌ 13 pts to go |
| P11 | 1807 | 1.8% | 1.8% | -0.9 | 15% | ❌ 13 pts to go |
| P12 | 11 | 0.0% | 0.0% | -20.0 | 15% | ❌ 15 pts to go |
| P13 | 152246 | 0.1% | 0.1% | -0.1 | 15% | ❌ 15 pts to go |

### `buyer_ap_cycle_published`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 250 | 1.2% | 1.2% | -1.1 | 20% | ❌ 19 pts to go |
| P01T | 225 | 3.1% | 3.1% | -1.1 | 20% | ❌ 17 pts to go |
| P01_GOLD | 626 | 4.3% | 4.3% | -0.2 | 20% | ❌ 16 pts to go |
| P02 | 467 | 1.7% | 1.7% | +0.2 | 20% | ❌ 18 pts to go |
| P03 | 265 | 1.5% | 1.5% | +0.0 | 20% | ❌ 18 pts to go |
| P04 | 3572 | 0.7% | 0.7% | +0.1 | 20% | ❌ 19 pts to go |
| P05 | 424 | 0.9% | 0.9% | -0.3 | 20% | ❌ 19 pts to go |
| P06M | 22195 | 0.1% | 0.1% | +0.1 | 20% | ❌ 20 pts to go |
| P06T | 59830 | 0.0% | 0.0% | +0.0 | 20% | ❌ 20 pts to go |
| P06 | 276 | 1.1% | 1.1% | -0.4 | 20% | ❌ 19 pts to go |
| P07 | 820 | 0.2% | 0.2% | -0.2 | 20% | ❌ 20 pts to go |
| P08 | 30285 | 0.0% | 0.0% | +0.0 | 20% | ❌ 20 pts to go |
| P09 | 275 | 0.0% | 0.0% | +0.0 | 20% | ❌ 20 pts to go |
| P10 | 2126 | 0.3% | 0.3% | +0.0 | 20% | ❌ 20 pts to go |
| P11 | 1807 | 0.1% | 0.1% | -0.2 | 20% | ❌ 20 pts to go |
| P12 | 11 | 0.0% | 0.0% | +0.0 | 20% | ❌ 20 pts to go |
| P13 | 152246 | 0.0% | 0.0% | +0.0 | 20% | ❌ 20 pts to go |

### `buyer_esignature_preference`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 250 | 1.6% | 1.6% | +0.0 | 15% | ❌ 13 pts to go |
| P01T | 225 | 3.1% | 3.1% | +0.0 | 15% | ❌ 12 pts to go |
| P01_GOLD | 626 | 10.7% | 10.7% | +0.3 | 15% | 🟡 4 pts to go |
| P02 | 467 | 10.9% | 10.9% | -1.1 | 15% | 🟡 4 pts to go |
| P03 | 265 | 20.8% | 20.8% | +0.6 | 15% | ✅ met |
| P04 | 3572 | 2.4% | 2.4% | +0.1 | 15% | ❌ 13 pts to go |
| P05 | 424 | 2.8% | 2.8% | +0.0 | 15% | ❌ 12 pts to go |
| P06M | 22195 | 0.4% | 0.4% | +0.1 | 15% | ❌ 15 pts to go |
| P06T | 59830 | 0.2% | 0.2% | +0.0 | 15% | ❌ 15 pts to go |
| P06 | 276 | 4.0% | 4.0% | -1.1 | 15% | ❌ 11 pts to go |
| P07 | 820 | 1.2% | 1.2% | -0.4 | 15% | ❌ 14 pts to go |
| P08 | 30285 | 0.3% | 0.3% | -0.2 | 15% | ❌ 15 pts to go |
| P09 | 275 | 0.7% | 0.7% | +0.0 | 15% | ❌ 14 pts to go |
| P10 | 2126 | 1.1% | 1.1% | +0.1 | 15% | ❌ 14 pts to go |
| P11 | 1807 | 0.8% | 0.8% | -0.4 | 15% | ❌ 14 pts to go |
| P12 | 11 | 0.0% | 0.0% | -6.7 | 15% | ❌ 15 pts to go |
| P13 | 152246 | 0.1% | 0.1% | +0.0 | 15% | ❌ 15 pts to go |

### `ap_system_hint`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 250 | 12.4% | 12.4% | -1.6 | 20% | 🟡 8 pts to go |
| P01T | 225 | 12.9% | 12.9% | -1.2 | 40% | ❌ 27 pts to go |
| P01_GOLD | 626 | 46.5% | 46.5% | +0.3 | 40% | ✅ met |
| P02 | 467 | 43.3% | 43.3% | +0.4 | 20% | ✅ met |
| P03 | 265 | 48.3% | 48.3% | -0.7 | 35% | ✅ met |
| P04 | 3572 | 15.0% | 15.0% | +0.8 | 20% | 🟡 5 pts to go |
| P05 | 424 | 15.6% | 15.6% | +0.2 | 20% | 🟡 4 pts to go |
| P06M | 22195 | 1.0% | 1.0% | +0.2 | 20% | ❌ 19 pts to go |
| P06T | 59830 | 0.6% | 0.6% | -0.1 | 20% | ❌ 19 pts to go |
| P06 | 276 | 21.4% | 21.4% | -3.9 | 20% | ✅ met |
| P07 | 820 | 6.2% | 6.2% | -2.4 | 20% | ❌ 14 pts to go |
| P08 | 30285 | 0.8% | 0.8% | -0.2 | 20% | ❌ 19 pts to go |
| P09 | 275 | 20.7% | 20.7% | +2.5 | 20% | ✅ met |
| P10 | 2126 | 3.8% | 3.8% | +0.1 | 20% | ❌ 16 pts to go |
| P11 | 1807 | 3.1% | 3.1% | -1.7 | 20% | ❌ 17 pts to go |
| P12 | 11 | 9.1% | 9.1% | +2.4 | 20% | ❌ 11 pts to go |
| P13 | 152246 | 0.4% | 0.4% | -0.1 | 20% | ❌ 20 pts to go |

## 5. contract

### `contract_value`

> ceiling: rows proven by a lobbying filing, a news release, an auditor appointment, a customer story or a vendor's client list have no contract value by nature (≈17 % of P01 Gold); bids&tenders awards now carry the awarded bidder's submitted price when no award value was published

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 250 | 18.4% | 18.4% | -14.9 | n/a | no target |
| P01T | 225 | 0.4% | 0.4% | -0.1 | n/a | no target |
| P01_GOLD | 626 | 71.9% | 71.9% | +2.4 | 95% | ❌ 23 pts to go |
| P02 | 467 | 66.0% | 66.0% | +3.1 | 95% | ❌ 29 pts to go |
| P03 | 265 | 57.7% | 57.7% | +4.5 | 90% | ❌ 32 pts to go |
| P04 | 3572 | 26.6% | 26.6% | +1.8 | 85% | ❌ 58 pts to go |
| P05 | 424 | 38.9% | 38.9% | +1.2 | 75% | ❌ 36 pts to go |
| P06M | 22195 | 28.2% | 28.2% | -7.9 | n/a | no target |
| P06T | 59830 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06 | 276 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P07 | 820 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P08 | 30285 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P09 | 275 | 89.1% | 89.1% | +0.8 | 100% | ❌ 11 pts to go |
| P10 | 2126 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P11 | 1807 | 3.9% | 3.9% | -2.1 | 60% | ❌ 56 pts to go |
| P12 | 11 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P13 | 152246 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `currency`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 250 | 18.4% | 18.4% | -14.9 | n/a | no target |
| P01T | 225 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P01_GOLD | 626 | 73.8% | 73.8% | +1.0 | 100% | ❌ 26 pts to go |
| P02 | 467 | 67.9% | 67.9% | +1.6 | 100% | ❌ 32 pts to go |
| P03 | 265 | 60.4% | 60.4% | +1.5 | n/a | no target |
| P04 | 3572 | 27.0% | 27.0% | +1.5 | 95% | ❌ 68 pts to go |
| P05 | 424 | 34.7% | 34.7% | +1.3 | 80% | ❌ 45 pts to go |
| P06M | 22195 | 28.2% | 28.2% | -7.9 | n/a | no target |
| P06T | 59830 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06 | 276 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P07 | 820 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P08 | 30285 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P09 | 275 | 91.6% | 91.6% | +0.1 | 100% | 🟡 8 pts to go |
| P10 | 2126 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P11 | 1807 | 4.0% | 4.0% | -2.4 | n/a | no target |
| P12 | 11 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P13 | 152246 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `start_date`

> ceiling: most award notices publish an award date, not a start date; start_date carries the signature date when the source gives one, labelled

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 250 | 84.4% | 84.4% | +4.6 | n/a | no target |
| P01T | 225 | 0.4% | 0.4% | -0.1 | n/a | no target |
| P01_GOLD | 626 | 52.1% | 52.1% | +0.5 | 85% | ❌ 33 pts to go |
| P02 | 467 | 58.9% | 58.9% | +1.4 | 90% | ❌ 31 pts to go |
| P03 | 265 | 44.2% | 44.2% | +1.6 | 85% | ❌ 41 pts to go |
| P04 | 3572 | 29.1% | 29.1% | +1.2 | 90% | ❌ 61 pts to go |
| P05 | 424 | 33.0% | 33.0% | +0.3 | 75% | ❌ 42 pts to go |
| P06M | 22195 | 84.5% | 84.5% | -2.6 | n/a | no target |
| P06T | 59830 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06 | 276 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P07 | 820 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P08 | 30285 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P09 | 275 | 81.8% | 81.8% | -1.6 | 95% | ❌ 13 pts to go |
| P10 | 2126 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P11 | 1807 | 3.3% | 3.3% | -2.1 | n/a | no target |
| P12 | 11 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P13 | 152246 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `end_date`

> ceiling: an inferred end (award date + published duration) is labelled as such; sources without a duration leave end_date empty — the honest ceiling. P09 is BY DEFINITION the rows whose end date is not published (older SEAO contracts with no closing notice): its end_date / duration targets cannot be met without inventing a date

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 250 | 66.0% | 66.0% | -12.3 | n/a | no target |
| P01T | 225 | 0.4% | 0.4% | -0.1 | n/a | no target |
| P01_GOLD | 626 | 51.9% | 51.9% | +0.1 | 85% | ❌ 33 pts to go |
| P02 | 467 | 53.3% | 53.3% | +0.7 | 90% | ❌ 37 pts to go |
| P03 | 265 | 44.5% | 44.5% | +0.8 | 85% | ❌ 40 pts to go |
| P04 | 3572 | 24.6% | 24.6% | +0.8 | 90% | ❌ 65 pts to go |
| P05 | 424 | 42.5% | 42.5% | -0.9 | 75% | ❌ 32 pts to go |
| P06M | 22195 | 69.4% | 69.4% | -8.4 | n/a | no target |
| P06T | 59830 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06 | 276 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P07 | 820 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P08 | 30285 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P09 | 275 | 0.4% | 0.4% | +0.1 | 95% | ❌ 95 pts to go |
| P10 | 2126 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P11 | 1807 | 2.5% | 2.5% | -2.0 | n/a | no target |
| P12 | 11 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P13 | 152246 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `contract_title`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 250 | 95.2% | 95.2% | +5.3 | n/a | no target |
| P01T | 225 | 96.0% | 96.0% | +1.7 | n/a | no target |
| P01_GOLD | 626 | 85.6% | 85.8% | +0.3 | 100% | ❌ 14 pts to go |
| P02 | 467 | 77.3% | 77.3% | +0.9 | 100% | ❌ 23 pts to go |
| P03 | 265 | 92.5% | 92.5% | +1.2 | n/a | no target |
| P04 | 3572 | 50.6% | 50.6% | +1.8 | 95% | ❌ 44 pts to go |
| P05 | 424 | 77.4% | 77.4% | -0.1 | 95% | ❌ 18 pts to go |
| P06M | 22195 | 99.3% | 99.3% | +0.4 | n/a | no target |
| P06T | 59830 | 94.5% | 94.5% | +3.9 | n/a | no target |
| P06 | 276 | 20.3% | 20.3% | -2.8 | n/a | no target |
| P07 | 820 | 10.4% | 10.4% | -3.4 | n/a | no target |
| P08 | 30285 | 4.6% | 4.6% | -2.5 | n/a | no target |
| P09 | 275 | 98.2% | 98.2% | -0.5 | 100% | 🟡 2 pts to go |
| P10 | 2126 | 70.6% | 70.6% | -0.4 | n/a | no target |
| P11 | 1807 | 70.0% | 70.0% | +1.9 | n/a | no target |
| P12 | 11 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P13 | 152246 | 99.6% | 99.6% | -0.1 | n/a | no target |

### `contract_description`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 250 | 95.2% | 95.2% | +5.3 | n/a | no target |
| P01T | 225 | 96.0% | 96.0% | +1.7 | n/a | no target |
| P01_GOLD | 626 | 88.8% | 89.0% | +0.3 | 100% | ❌ 11 pts to go |
| P02 | 467 | 78.6% | 78.6% | +1.1 | 100% | ❌ 21 pts to go |
| P03 | 265 | 93.2% | 93.2% | +1.2 | n/a | no target |
| P04 | 3572 | 54.0% | 54.0% | +2.1 | 95% | ❌ 41 pts to go |
| P05 | 424 | 89.4% | 89.4% | -0.2 | 70% | ✅ met |
| P06M | 22195 | 99.3% | 99.3% | +0.4 | n/a | no target |
| P06T | 59830 | 94.5% | 94.5% | +3.9 | n/a | no target |
| P06 | 276 | 20.3% | 20.3% | -2.8 | n/a | no target |
| P07 | 820 | 10.4% | 10.4% | -3.4 | n/a | no target |
| P08 | 30285 | 4.6% | 4.6% | -2.5 | n/a | no target |
| P09 | 275 | 98.2% | 98.2% | -0.5 | 100% | 🟡 2 pts to go |
| P10 | 2126 | 70.6% | 70.6% | -0.4 | n/a | no target |
| P11 | 1807 | 70.1% | 70.1% | +1.9 | n/a | no target |
| P12 | 11 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P13 | 152246 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `number_of_bids`

> ceiling: published by some portals only (bids&tenders submission lists, Biddingo bidder lists); federal proactive disclosure does not publish bid counts

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 250 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P01T | 225 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P01_GOLD | 626 | 17.1% | 17.1% | +0.3 | 60% | ❌ 43 pts to go · rows from a source that publishes bids: 368 rows, 29.1% filled |
| P02 | 467 | 10.1% | 10.1% | -1.1 | n/a | no target · rows from a source that publishes bids: 294 rows, 16.0% filled |
| P03 | 265 | 14.0% | 14.0% | +1.1 | n/a | no target · rows from a source that publishes bids: 143 rows, 25.9% filled |
| P04 | 3572 | 1.7% | 1.7% | +0.2 | n/a | no target · rows from a source that publishes bids: 882 rows, 6.9% filled |
| P05 | 424 | 2.6% | 2.6% | +0.0 | n/a | no target · rows from a source that publishes bids: 56 rows, 19.6% filled |
| P06M | 22195 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06T | 59830 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06 | 276 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P07 | 820 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P08 | 30285 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P09 | 275 | 4.4% | 4.4% | +0.2 | n/a | no target · rows from a source that publishes bids: 262 rows, 4.6% filled |
| P10 | 2126 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P11 | 1807 | 0.4% | 0.4% | -0.5 | n/a | no target · rows from a source that publishes bids: 68 rows, 11.8% filled |
| P12 | 11 | 0.0% | 0.0% | +0.0 | n/a | no target · rows from a source that publishes bids: 11 rows, 0.0% filled |
| P13 | 152246 | 0.0% | 0.0% | +0.0 | n/a | no target |

## 6. history

### `average_contract_duration_days`

> ceiling: needs two dates (or a published term) on the buyer's records; P09 rows (end date unpublished by definition) and buyers whose sources publish award dates only have no honest duration

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 250 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P01T | 225 | 0.0% | 97.8% | +0.0 | n/a | no target |
| P01_GOLD | 626 | 53.4% | 81.9% | +0.2 | 90% | ❌ 37 pts to go |
| P02 | 467 | 53.3% | 87.2% | +0.9 | 90% | ❌ 37 pts to go |
| P03 | 265 | 46.0% | 80.0% | +1.5 | 90% | ❌ 44 pts to go |
| P04 | 3572 | 19.7% | 92.9% | +0.6 | 90% | ❌ 70 pts to go |
| P05 | 424 | 0.0% | 82.3% | +0.0 | 90% | ❌ 90 pts to go |
| P06M | 22195 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P06T | 59830 | 0.0% | 99.9% | +0.0 | n/a | no target |
| P06 | 276 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P07 | 820 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P08 | 30285 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P09 | 275 | 2.9% | 4.7% | +0.6 | 90% | ❌ 87 pts to go |
| P10 | 2126 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P11 | 1807 | 2.2% | 97.6% | -1.9 | n/a | no target |
| P12 | 11 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P13 | 152246 | 0.0% | 100.0% | +0.0 | n/a | no target |

### `commodity_distribution_top3`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 250 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P01T | 225 | 0.9% | 98.7% | +0.4 | n/a | no target |
| P01_GOLD | 626 | 26.2% | 54.8% | +0.3 | 90% | ❌ 64 pts to go |
| P02 | 467 | 52.0% | 85.9% | +0.5 | n/a | no target |
| P03 | 265 | 25.3% | 59.2% | +1.0 | n/a | no target |
| P04 | 3572 | 21.4% | 94.6% | +0.4 | n/a | no target |
| P05 | 424 | 0.5% | 82.8% | +0.0 | n/a | no target |
| P06M | 22195 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P06T | 59830 | 0.1% | 99.9% | +0.0 | n/a | no target |
| P06 | 276 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P07 | 820 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P08 | 30285 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P09 | 275 | 40.0% | 41.8% | -1.0 | n/a | no target |
| P10 | 2126 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P11 | 1807 | 2.3% | 97.7% | -1.4 | n/a | no target |
| P12 | 11 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P13 | 152246 | 0.0% | 100.0% | +0.0 | n/a | no target |

### `year_over_year_spend_trend`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 250 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P01T | 225 | 2.2% | 100.0% | +0.1 | n/a | no target |
| P01_GOLD | 626 | 52.2% | 80.8% | +0.4 | 95% | ❌ 43 pts to go |
| P02 | 467 | 58.0% | 91.9% | +1.6 | n/a | no target |
| P03 | 265 | 50.2% | 84.2% | +3.4 | n/a | no target |
| P04 | 3572 | 22.2% | 95.4% | +1.0 | n/a | no target |
| P05 | 424 | 5.0% | 87.3% | +0.5 | n/a | no target |
| P06M | 22195 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P06T | 59830 | 0.1% | 100.0% | +0.0 | n/a | no target |
| P06 | 276 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P07 | 820 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P08 | 30285 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P09 | 275 | 60.4% | 62.2% | -2.1 | n/a | no target |
| P10 | 2126 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P11 | 1807 | 2.3% | 97.8% | -1.8 | n/a | no target |
| P12 | 11 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P13 | 152246 | 0.0% | 100.0% | +0.0 | n/a | no target |

## 7. mail security

### `mta_sts`

> ceiling: DNS-only check; 'no record' counts as checked

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 250 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P01T | 225 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P01_GOLD | 626 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P02 | 467 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P03 | 265 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P04 | 3572 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P05 | 424 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P06M | 22195 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P06T | 59830 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P06 | 276 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P07 | 820 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P08 | 30285 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P09 | 275 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P10 | 2126 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P11 | 1807 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P12 | 11 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P13 | 152246 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |

### `tls_rpt`

> ceiling: DNS-only check; 'no record' counts as checked

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 250 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P01T | 225 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P01_GOLD | 626 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P02 | 467 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P03 | 265 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P04 | 3572 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P05 | 424 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P06M | 22195 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P06T | 59830 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P06 | 276 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P07 | 820 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P08 | 30285 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P09 | 275 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P10 | 2126 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P11 | 1807 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P12 | 11 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P13 | 152246 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |

### `bimi`

> ceiling: DNS-only check; 'no record' counts as checked

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 250 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P01T | 225 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P01_GOLD | 626 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P02 | 467 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P03 | 265 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P04 | 3572 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P05 | 424 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P06M | 22195 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P06T | 59830 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P06 | 276 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P07 | 820 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P08 | 30285 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P09 | 275 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P10 | 2126 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P11 | 1807 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P12 | 11 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P13 | 152246 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |

