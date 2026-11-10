# Coverage vs the downstream team's targets — 2026-11-10

Benchmarks (field × package with a numeric target): **48 of 446 met** (10.8%); 87 within 10 points; 311 further away.
A cell counts as filled only when it carries a value: blank, `not_published`, `not_found_yet` and label-only cells ("no identifier published …", "no dataset record …", "0 in the contract dataset …") do not count; the DNS checks count when checked. `any` = share of non-blank cells incl. such labels. Δ = change since the previous build in `coord/results/coverage_history.csv`.
Rows per package: P01M 61, P01T 269, P01_GOLD 625, P02 462, P03 255, P04 3204, P05 413, P06M 5017, P06T 37441, P06 276, P07 653, P08 19441, P09 305, P10R 74764, P10 2591, P11 5230, P12 8, P13 14237

## Invoice-grade readiness (the row as an invoice header: bill-to, submit-to, references, terms, tax, vendor identity, follow-up)

| package | rows | all 11 elements | ≥ 9 of 11 | median elements | most-missing element |
|---|---|---|---|---|---|
| P01M | 61 | 0.0% | 24.6% | 8 | PO rule (49 rows) |
| P01T | 269 | 0.7% | 18.2% | 7 | payment terms (200 rows) |
| P01_GOLD | 625 | 24.3% | 68.0% | 9 | payment terms (214 rows) |
| P02 | 462 | 7.6% | 52.4% | 9 | PO rule (351 rows) |
| P03 | 255 | 13.7% | 57.3% | 9 | PO rule (121 rows) |
| P04 | 3204 | 1.4% | 18.3% | 6 | PO rule (3013 rows) |
| P05 | 413 | 1.0% | 16.9% | 7 | payment terms (338 rows) |
| P06M | 5017 | 0.0% | 1.7% | 8 | PO rule (4992 rows) |
| P06T | 37441 | 0.0% | 0.5% | 5 | PO rule (37209 rows) |
| P06 | 276 | 0.0% | 5.4% | 5 | reference to quote (PO / contract / vendor id) (276 rows) |
| P07 | 653 | 0.0% | 1.4% | 5 | reference to quote (PO / contract / vendor id) (653 rows) |
| P08 | 19441 | 0.0% | 0.1% | 4 | reference to quote (PO / contract / vendor id) (19441 rows) |
| P09 | 305 | 1.0% | 43.3% | 8 | payment terms (285 rows) |
| P10R | 74764 | 0.0% | 9.6% | 7 | PO rule (74731 rows) |
| P10 | 2591 | 0.0% | 0.6% | 4 | reference to quote (PO / contract / vendor id) (2591 rows) |
| P11 | 5230 | 0.1% | 1.3% | 6 | PO rule (5132 rows) |
| P12 | 8 | 0.0% | 50.0% | 9 | PO rule (8 rows) |
| P13 | 14237 | 0.0% | 0.0% | 6 | reference to quote (PO / contract / vendor id) (14237 rows) |

## AP grade (how stringently the row's accounts-payable data meets what an invoice needs; A = invoicing mailbox referee-confirmed on the buyer's own domain with MX, legal name, address, PO rule and terms all published, no penalties)

| package | rows | A | B | C | D | E | median ap_score |
|---|---|---|---|---|---|---|---|
| P01M | 61 | 6 | 6 | 49 | 0 | 0 | 71 |
| P01T | 269 | 31 | 47 | 191 | 0 | 0 | 71 |
| P01_GOLD | 625 | 229 | 185 | 211 | 0 | 0 | 81 |
| P02 | 462 | 0 | 187 | 275 | 0 | 0 | 66 |
| P03 | 255 | 0 | 0 | 241 | 14 | 0 | 57 |
| P04 | 3204 | 0 | 0 | 2548 | 656 | 0 | 45 |
| P05 | 413 | 14 | 30 | 345 | 24 | 0 | 51 |
| P06M | 5017 | 0 | 1 | 4935 | 81 | 0 | 51 |
| P06T | 37441 | 0 | 30 | 29191 | 8220 | 0 | 38 |
| P06 | 276 | 19 | 27 | 230 | 0 | 0 | 67 |
| P07 | 653 | 0 | 15 | 604 | 34 | 0 | 48 |
| P08 | 19441 | 0 | 0 | 15209 | 4232 | 0 | 38 |
| P09 | 305 | 3 | 12 | 287 | 3 | 0 | 53 |
| P10R | 74764 | 1 | 8 | 46199 | 28556 | 0 | 38 |
| P10 | 2591 | 2 | 9 | 1763 | 817 | 0 | 38 |
| P11 | 5230 | 6 | 8 | 43 | 0 | 5173 | 23 |
| P12 | 8 | 0 | 1 | 7 | 0 | 0 | 54 |
| P13 | 14237 | 2 | 12 | 11527 | 2696 | 0 | 43 |

### AP payability (confirmed channel + bill-to legal name and address + the buyer's reference rule + tax treatment known)

| package | rows | payable today | % | most common gap |
|---|---|---|---|---|
| P01M | 61 | 47 | 77.0% | the buyer's PO / reference rule (7) |
| P01T | 269 | 115 | 42.8% | bill-to legal name and address (117) |
| P01_GOLD | 625 | 461 | 73.8% | bill-to legal name and address (111) |
| P02 | 462 | 308 | 66.7% | bill-to legal name and address (85) |
| P03 | 255 | 0 | 0.0% | a confirmed invoicing / AP or finance channel (255) |
| P04 | 3204 | 0 | 0.0% | a confirmed invoicing / AP or finance channel (3204) |
| P05 | 413 | 47 | 11.4% | a confirmed invoicing / AP or finance channel (326) |
| P06M | 5017 | 34 | 0.7% | a confirmed invoicing / AP or finance channel (4954) |
| P06T | 37441 | 167 | 0.4% | a confirmed invoicing / AP or finance channel (36784) |
| P06 | 276 | 29 | 10.5% | bill-to legal name and address (172) |
| P07 | 653 | 8 | 1.2% | bill-to legal name and address (385) |
| P08 | 19441 | 0 | 0.0% | a confirmed invoicing / AP or finance channel (19441) |
| P09 | 305 | 40 | 13.1% | a confirmed invoicing / AP or finance channel (255) |
| P10R | 74764 | 268 | 0.4% | a confirmed invoicing / AP or finance channel (73731) |
| P10 | 2591 | 3 | 0.1% | a confirmed invoicing / AP or finance channel (2494) |
| P11 | 5230 | 9 | 0.2% | a confirmed invoicing / AP or finance channel (5173) |
| P12 | 8 | 3 | 37.5% | a confirmed invoicing / AP or finance channel (5) |
| P13 | 14237 | 6 | 0.0% | a confirmed invoicing / AP or finance channel (13910) |

### Pay on sight (an invoice generated from the row would clear AP: confirmed invoicing / AP or finance channel, bill-to legal name + address, vendor legal name + GST/HST number + remit-to address, tax treatment and currency known — published or labelled-derived; the buyer's reference rule is reported separately)

| package | rows | pay on sight | % | + reference rule not published | routed (general inbox only) | most common gap |
|---|---|---|---|---|---|---|
| P01M | 61 | 6 | 9.8% | 6 | 0 | the vendor's GST/HST number (BN9) (47) |
| P01T | 269 | 45 | 16.7% | 18 | 0 | the vendor's GST/HST number (BN9) (145) |
| P01_GOLD | 625 | 395 | 63.2% | 13 | 0 | the vendor's GST/HST number (BN9) (150) |
| P02 | 462 | 212 | 45.9% | 20 | 0 | the vendor's GST/HST number (BN9) (189) |
| P03 | 255 | 18 | 7.1% | 0 | 129 | an invoicing / AP or finance mailbox (only a purchasing / general inbo (89) |
| P04 | 3204 | 42 | 1.3% | 7 | 711 | an invoicing / AP or finance mailbox (only a purchasing / general inbo (2385) |
| P05 | 413 | 22 | 5.3% | 8 | 98 | an invoicing / AP or finance mailbox (only a purchasing / general inbo (221) |
| P06M | 5017 | 1 | 0.0% | 10 | 77 | an invoicing / AP or finance mailbox (only a purchasing / general inbo (4864) |
| P06T | 37441 | 19 | 0.1% | 77 | 3362 | an invoicing / AP or finance mailbox (only a purchasing / general inbo (33308) |
| P06 | 276 | 13 | 4.7% | 16 | 0 | the vendor's GST/HST number (BN9) (164) |
| P07 | 653 | 6 | 0.9% | 30 | 14 | the vendor's GST/HST number (BN9) (353) |
| P08 | 19441 | 2 | 0.0% | 3 | 932 | an invoicing / AP or finance mailbox (only a purchasing / general inbo (18448) |
| P09 | 305 | 39 | 12.8% | 1 | 122 | an invoicing / AP or finance mailbox (only a purchasing / general inbo (124) |
| P10R | 74764 | 741 | 1.0% | 0 | 38812 | an invoicing / AP or finance mailbox (only a purchasing / general inbo (34867) |
| P10 | 2591 | 4 | 0.2% | 17 | 319 | an invoicing / AP or finance mailbox (only a purchasing / general inbo (2146) |
| P11 | 5230 | 9 | 0.2% | 18 | 0 | a confirmed invoicing / AP or finance channel (5137) |
| P12 | 8 | 2 | 25.0% | 0 | 3 | an invoicing / AP or finance mailbox (only a purchasing / general inbo (2) |
| P13 | 14237 | 8 | 0.1% | 239 | 8679 | an invoicing / AP or finance mailbox (only a purchasing / general inbo (5194) |
| **all** | 165252 | 1584 | 1.0% | 483 | 53258 | |

### What still blocks grade A (rows per missing element; a row counts under every element it lacks)

| package | rows not A | referee confirmation of the mailbox | an invoicing / AP mailbox (not finance / procurement / general) | a mailbox on the buyer's own domain | MX record for the mailbox domain | published bill-to legal name | invoice / billing address | published PO rule | published payment terms | clear the penalty |
|---|---|---|---|---|---|---|---|---|---|---|
| P01M | 55 | 0 | 0 | 0 | 12 | 6 | 0 | 49 | 52 | 0 |
| P01T | 238 | 0 | 0 | 0 | 70 | 113 | 17 | 186 | 202 | 30 |
| P01_GOLD | 396 | 0 | 0 | 0 | 11 | 96 | 34 | 193 | 228 | 59 |
| P02 | 462 | 0 | 462 | 0 | 36 | 79 | 20 | 351 | 283 | 22 |
| P03 | 255 | 0 | 255 | 0 | 12 | 54 | 23 | 121 | 127 | 27 |
| P04 | 3204 | 0 | 3204 | 0 | 1197 | 1678 | 757 | 3013 | 2763 | 136 |
| P05 | 399 | 0 | 345 | 0 | 64 | 138 | 49 | 330 | 340 | 52 |
| P06M | 5017 | 0 | 5017 | 0 | 1081 | 637 | 111 | 4992 | 4963 | 3 |
| P06T | 37441 | 0 | 37441 | 0 | 23657 | 30066 | 8805 | 37209 | 36748 | 205 |
| P06 | 257 | 0 | 0 | 0 | 90 | 166 | 55 | 183 | 219 | 5 |
| P07 | 653 | 0 | 653 | 0 | 341 | 470 | 125 | 601 | 606 | 15 |
| P08 | 19441 | 0 | 19441 | 0 | 13450 | 16223 | 4523 | 19194 | 18861 | 189 |
| P09 | 302 | 0 | 281 | 0 | 10 | 72 | 3 | 275 | 287 | 44 |
| P10R | 74763 | 0 | 74606 | 0 | 50608 | 64992 | 30086 | 74731 | 74620 | 22 |
| P10 | 2589 | 0 | 2553 | 0 | 1152 | 2000 | 958 | 2528 | 2480 | 112 |
| P11 | 5224 | 5173 | 5116 | 0 | 3787 | 5028 | 1093 | 5132 | 4851 | 35 |
| P12 | 8 | 0 | 7 | 0 | 0 | 2 | 0 | 8 | 7 | 0 |
| P13 | 14235 | 0 | 14135 | 0 | 4379 | 7255 | 3142 | 14202 | 14205 | 22 |

## Where the work is (largest gaps in rows still needed)

| field | package | now | target | rows needed |
|---|---|---|---|---|
| mta_sts | P10R | 75.5% | 100% | 18315 |
| tls_rpt | P10R | 75.5% | 100% | 18315 |
| bimi | P10R | 75.5% | 100% | 18315 |
| buyer_ap_cycle_published | P10R | 0.0% | 20% | 14949 |
| ap_system_hint | P10R | 0.2% | 20% | 14816 |
| buyer_logo_url | P08 | 30.9% | 100% | 13426 |
| buyer_phone | P08 | 26.7% | 95% | 13276 |
| vendor_registered_address | P08 | 9.1% | 70% | 11834 |
| buyer_legal_name_as_published | P08 | 16.6% | 75% | 11363 |
| buyer_esignature_preference | P10R | 0.0% | 15% | 11199 |
| buyer_tax_exempt_status | P10R | 0.0% | 15% | 11198 |
| buyer_payment_method_preference | P10R | 0.2% | 15% | 11070 |
| vendor_logo_url | P08 | 45.5% | 100% | 10598 |
| vendor_phone | P08 | 33.5% | 85% | 10004 |
| vendor_bn9 | P08 | 8.0% | 50% | 8171 |
| vendor_emails | P08 | 34.7% | 75% | 7843 |
| buyer_ap_cycle_published | P06T | 0.0% | 20% | 7478 |
| ap_system_hint | P06T | 0.8% | 20% | 7183 |
| vendor_trading_name | P08 | 15.8% | 50% | 6648 |
| buyer_phone | P13 | 53.2% | 95% | 5945 |
| buyer_logo_url | P13 | 53.4% | 95% | 5918 |
| buyer_esignature_preference | P06T | 0.2% | 15% | 5534 |
| buyer_tax_exempt_status | P06T | 0.3% | 15% | 5504 |
| buyer_payment_method_preference | P06T | 0.3% | 15% | 5499 |
| buyer_bn_as_published | P08 | 7.3% | 35% | 5388 |
| mta_sts | P06T | 86.7% | 100% | 4992 |
| tls_rpt | P06T | 86.7% | 100% | 4992 |
| bimi | P06T | 86.7% | 100% | 4992 |
| invoice_reference_hint | P08 | 1.3% | 25% | 4614 |
| buyer_ap_cycle_published | P08 | 0.0% | 20% | 3884 |
| buyer_logo_url | P11 | 8.8% | 80% | 3722 |
| ap_system_hint | P08 | 0.9% | 20% | 3718 |
| buyer_phone | P11 | 6.5% | 75% | 3582 |
| buyer_address | P08 | 76.7% | 95% | 3557 |
| vendor_phone | P11 | 8.0% | 75% | 3502 |
| vendor_emails | P11 | 7.1% | 70% | 3290 |
| buyer_legal_name_as_published | P11 | 3.9% | 65% | 3198 |
| award_or_notice_id | P11 | 1.6% | 60% | 3052 |
| contract_value | P11 | 1.6% | 60% | 3052 |
| buyer_payment_method_preference | P08 | 0.2% | 15% | 2877 |

## 1. identifiers

### `invoice_reference_hint`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 61 | 85.2% | 85.2% | +40.8 | 50% | ✅ met |
| P01T | 269 | 88.1% | 88.1% | +16.4 | 50% | ✅ met |
| P01_GOLD | 625 | 92.2% | 94.4% | -0.3 | 95% | 🟡 3 pts to go |
| P02 | 462 | 74.7% | 76.2% | -9.2 | 95% | ❌ 20 pts to go |
| P03 | 255 | 82.4% | 85.5% | -10.4 | 95% | ❌ 13 pts to go |
| P04 | 3204 | 34.7% | 36.3% | -33.9 | 90% | ❌ 55 pts to go |
| P05 | 413 | 39.5% | 42.4% | -1.6 | 70% | ❌ 30 pts to go |
| P06M | 5017 | 91.5% | 91.5% | +84.4 | n/a | no target |
| P06T | 37441 | 84.2% | 84.2% | +79.8 | n/a | no target |
| P06 | 276 | 33.7% | 33.7% | -14.5 | 30% | ✅ met |
| P07 | 653 | 8.0% | 8.0% | -15.8 | 30% | ❌ 22 pts to go |
| P08 | 19441 | 1.3% | 1.3% | -1.1 | 25% | ❌ 24 pts to go |
| P09 | 305 | 99.0% | 99.7% | +0.0 | 100% | 🟡 1 pts to go |
| P10R | 74764 | 100.0% | 100.0% |  | n/a | no target |
| P10 | 2591 | 2.4% | 2.5% | +0.2 | 25% | ❌ 23 pts to go |
| P11 | 5230 | 30.2% | 30.5% | +6.1 | 60% | ❌ 30 pts to go |
| P12 | 8 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P13 | 14237 | 0.2% | 0.3% | +0.0 | 0% by design | — leave (by design) |

### `po_number_as_published`

> ceiling: a purchase-order number exists only where the buyer publishes PO-level data (Montréal, Laval, Toronto open data so far) or the record itself carries one; most sources publish awards, not POs — the target cannot be reached from public data for most buyers

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 61 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P01T | 269 | 0.0% | 0.0% | +0.0 | 10% | 🟡 10 pts to go |
| P01_GOLD | 625 | 6.1% | 6.1% | -0.1 | 50% | ❌ 44 pts to go |
| P02 | 462 | 6.3% | 6.3% | -0.9 | 50% | ❌ 44 pts to go |
| P03 | 255 | 1.6% | 1.6% | -0.3 | 40% | ❌ 38 pts to go |
| P04 | 3204 | 0.6% | 0.6% | -0.5 | 30% | ❌ 29 pts to go |
| P05 | 413 | 0.2% | 0.2% | -0.1 | 20% | ❌ 20 pts to go |
| P06M | 5017 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06T | 37441 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06 | 276 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P07 | 653 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P08 | 19441 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P09 | 305 | 0.7% | 0.7% | +0.2 | 50% | ❌ 49 pts to go |
| P10R | 74764 | 0.0% | 0.0% |  | n/a | no target |
| P10 | 2591 | 0.0% | 0.0% | -0.1 | n/a | no target |
| P11 | 5230 | 0.1% | 0.1% | -0.7 | n/a | no target |
| P12 | 8 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P13 | 14237 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `contract_or_agreement_number`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 61 | 73.8% | 73.8% | +73.8 | n/a | no target |
| P01T | 269 | 64.7% | 64.7% | +59.3 | 50% | ✅ met |
| P01_GOLD | 625 | 66.9% | 66.9% | -0.7 | 85% | ❌ 18 pts to go |
| P02 | 462 | 65.8% | 65.8% | -9.7 | 90% | ❌ 24 pts to go |
| P03 | 255 | 61.6% | 61.6% | -13.9 | 85% | ❌ 23 pts to go |
| P04 | 3204 | 32.1% | 32.1% | -33.4 | 85% | ❌ 53 pts to go |
| P05 | 413 | 29.5% | 29.5% | -1.5 | 60% | ❌ 30 pts to go |
| P06M | 5017 | 91.3% | 91.3% | +91.3 | n/a | no target |
| P06T | 37441 | 83.8% | 83.8% | +83.6 | n/a | no target |
| P06 | 276 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P07 | 653 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P08 | 19441 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P09 | 305 | 96.1% | 96.1% | -0.5 | 100% | 🟡 4 pts to go |
| P10R | 74764 | 100.0% | 100.0% |  | n/a | no target |
| P10 | 2591 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P11 | 5230 | 28.6% | 28.6% | +8.6 | 60% | ❌ 31 pts to go |
| P12 | 8 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P13 | 14237 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `solicitation_or_tender_number`

> ceiling: SEAO's 'numero' is the organisation's own reference for the notice (SEAO data dictionary) and is reported here; sources that publish awards under a tender number only (bids&tenders, SaskTenders, BC) also carry it as the contract reference, labelled

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 61 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P01T | 269 | 0.0% | 0.0% | -2.2 | 30% | ❌ 30 pts to go |
| P01_GOLD | 625 | 50.6% | 50.6% | -0.7 | 80% | ❌ 29 pts to go |
| P02 | 462 | 57.8% | 57.8% | -9.0 | 60% | 🟡 2 pts to go |
| P03 | 255 | 51.8% | 51.8% | -12.1 | 80% | ❌ 28 pts to go |
| P04 | 3204 | 26.6% | 26.6% | -27.9 | 50% | ❌ 23 pts to go |
| P05 | 413 | 12.3% | 12.3% | -1.0 | 40% | ❌ 28 pts to go |
| P06M | 5017 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06T | 37441 | 0.0% | 0.0% | -0.2 | n/a | no target |
| P06 | 276 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P07 | 653 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P08 | 19441 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P09 | 305 | 83.6% | 83.6% | -2.5 | 50% | ✅ met |
| P10R | 74764 | 0.0% | 0.0% |  | n/a | no target |
| P10 | 2591 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P11 | 5230 | 1.5% | 1.5% | -16.0 | 40% | ❌ 38 pts to go |
| P12 | 8 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P13 | 14237 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `award_or_notice_id`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 61 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P01T | 269 | 0.4% | 0.4% | -2.9 | n/a | no target |
| P01_GOLD | 625 | 60.3% | 60.3% | -0.8 | 85% | ❌ 25 pts to go |
| P02 | 462 | 57.1% | 57.1% | -8.7 | 90% | ❌ 33 pts to go |
| P03 | 255 | 60.4% | 60.4% | -14.1 | 85% | ❌ 25 pts to go |
| P04 | 3204 | 27.5% | 27.5% | -28.8 | 85% | ❌ 58 pts to go |
| P05 | 413 | 20.3% | 20.3% | -0.8 | 50% | ❌ 30 pts to go |
| P06M | 5017 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06T | 37441 | 0.0% | 0.0% | -0.2 | n/a | no target |
| P06 | 276 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P07 | 653 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P08 | 19441 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P09 | 305 | 97.0% | 97.0% | -0.1 | 100% | 🟡 3 pts to go |
| P10R | 74764 | 0.0% | 0.0% |  | n/a | no target |
| P10 | 2591 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P11 | 5230 | 1.6% | 1.6% | -17.4 | 60% | ❌ 58 pts to go |
| P12 | 8 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P13 | 14237 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `buyer_vendor_id`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 61 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P01T | 269 | 0.0% | 0.0% | -2.2 | n/a | no target |
| P01_GOLD | 625 | 13.0% | 13.0% | +0.0 | 60% | ❌ 47 pts to go |
| P02 | 462 | 6.1% | 6.1% | -1.1 | 50% | ❌ 44 pts to go |
| P03 | 255 | 8.6% | 8.6% | -2.0 | 50% | ❌ 41 pts to go |
| P04 | 3204 | 2.1% | 2.1% | -2.2 | 40% | ❌ 38 pts to go |
| P05 | 413 | 1.0% | 1.0% | -0.3 | 20% | ❌ 19 pts to go |
| P06M | 5017 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06T | 37441 | 0.0% | 0.0% | -0.1 | n/a | no target |
| P06 | 276 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P07 | 653 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P08 | 19441 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P09 | 305 | 2.3% | 2.3% | -0.3 | 50% | ❌ 48 pts to go |
| P10R | 74764 | 0.0% | 0.0% |  | n/a | no target |
| P10 | 2591 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P11 | 5230 | 0.3% | 0.3% | -2.7 | n/a | no target |
| P12 | 8 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P13 | 14237 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `commodity_codes`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 61 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P01T | 269 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P01_GOLD | 625 | 34.9% | 34.9% | -0.2 | 80% | ❌ 45 pts to go |
| P02 | 462 | 52.8% | 52.8% | -7.8 | 90% | ❌ 37 pts to go |
| P03 | 255 | 33.7% | 33.7% | -7.6 | 80% | ❌ 46 pts to go |
| P04 | 3204 | 25.1% | 25.1% | -26.2 | 85% | ❌ 60 pts to go |
| P05 | 413 | 5.6% | 5.6% | -0.4 | 50% | ❌ 44 pts to go |
| P06M | 5017 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06T | 37441 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06 | 276 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P07 | 653 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P08 | 19441 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P09 | 305 | 76.1% | 76.1% | +0.2 | 95% | ❌ 19 pts to go |
| P10R | 74764 | 0.0% | 0.0% |  | n/a | no target |
| P10 | 2591 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P11 | 5230 | 1.2% | 1.2% | -11.9 | 50% | ❌ 49 pts to go |
| P12 | 8 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P13 | 14237 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `buyer_org_codes`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 61 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P01T | 269 | 0.0% | 0.0% | -1.1 | n/a | no target |
| P01_GOLD | 625 | 8.5% | 8.5% | +0.0 | 50% | ❌ 42 pts to go |
| P02 | 462 | 6.3% | 6.3% | -0.9 | 50% | ❌ 44 pts to go |
| P03 | 255 | 2.0% | 2.0% | -0.4 | 30% | ❌ 28 pts to go |
| P04 | 3204 | 0.5% | 0.5% | -0.6 | 30% | ❌ 30 pts to go |
| P05 | 413 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06M | 5017 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06T | 37441 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06 | 276 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P07 | 653 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P08 | 19441 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P09 | 305 | 0.3% | 0.3% | +0.0 | n/a | no target |
| P10R | 74764 | 0.0% | 0.0% |  | n/a | no target |
| P10 | 2591 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P11 | 5230 | 0.1% | 0.1% | -0.7 | n/a | no target |
| P12 | 8 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P13 | 14237 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `records_with_this_vendor`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 61 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P01T | 269 | 100.0% | 100.0% | +0.0 | 60% | ✅ met |
| P01_GOLD | 625 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P02 | 462 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P03 | 255 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P04 | 3204 | 100.0% | 100.0% | +0.0 | 95% | ✅ met |
| P05 | 413 | 100.0% | 100.0% | +0.0 | 70% | ✅ met |
| P06M | 5017 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P06T | 37441 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P06 | 276 | 100.0% | 100.0% | +0.0 | 50% | ✅ met |
| P07 | 653 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P08 | 19441 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P09 | 305 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P10R | 74764 | 100.0% | 100.0% |  | n/a | no target |
| P10 | 2591 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P11 | 5230 | 100.0% | 100.0% | +0.0 | 70% | ✅ met |
| P12 | 8 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P13 | 14237 | 0.0% | 0.0% | +0.0 | n/a | no target |

## 2. vendor

### `vendor_bn9`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 61 | 23.0% | 23.0% | -77.0 | 70% | ❌ 47 pts to go |
| P01T | 269 | 30.5% | 30.5% | -49.9 | 60% | ❌ 30 pts to go |
| P01_GOLD | 625 | 73.1% | 73.1% | -4.8 | 90% | ❌ 17 pts to go |
| P02 | 462 | 54.8% | 54.8% | -12.5 | 85% | ❌ 30 pts to go |
| P03 | 255 | 68.6% | 68.6% | -13.6 | 90% | ❌ 21 pts to go |
| P04 | 3204 | 31.0% | 31.0% | -24.4 | 75% | ❌ 44 pts to go |
| P05 | 413 | 50.1% | 50.1% | -2.5 | 50% | ✅ met |
| P06M | 5017 | 2.3% | 2.3% | -72.1 | n/a | no target |
| P06T | 37441 | 10.5% | 10.5% | -50.2 | n/a | no target |
| P06 | 276 | 19.6% | 19.6% | -24.4 | 40% | ❌ 20 pts to go |
| P07 | 653 | 13.3% | 13.3% | -24.8 | 50% | ❌ 37 pts to go |
| P08 | 19441 | 8.0% | 8.0% | -32.2 | 50% | ❌ 42 pts to go |
| P09 | 305 | 57.7% | 57.7% | +3.4 | 80% | ❌ 22 pts to go |
| P10R | 74764 | 100.0% | 100.0% |  | n/a | no target |
| P10 | 2591 | 28.1% | 28.1% | -8.5 | 40% | ❌ 12 pts to go |
| P11 | 5230 | 80.2% | 80.2% | +35.5 | 60% | ✅ met |
| P12 | 8 | 62.5% | 62.5% | +9.9 | 85% | ❌ 22 pts to go |
| P13 | 14237 | 90.4% | 90.4% | -1.3 | 0% by design | — leave (by design) |

### `vendor_registered_address`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 61 | 72.1% | 72.1% | +11.0 | n/a | no target |
| P01T | 269 | 30.1% | 30.1% | -32.9 | n/a | no target |
| P01_GOLD | 625 | 70.6% | 70.6% | -4.2 | 95% | ❌ 24 pts to go |
| P02 | 462 | 72.5% | 72.5% | -12.4 | 95% | ❌ 22 pts to go |
| P03 | 255 | 70.2% | 70.2% | -7.7 | 95% | ❌ 25 pts to go |
| P04 | 3204 | 44.4% | 44.4% | -36.3 | 95% | ❌ 51 pts to go |
| P05 | 413 | 53.0% | 53.0% | -3.2 | 70% | ❌ 17 pts to go |
| P06M | 5017 | 56.9% | 56.9% | +36.1 | n/a | no target |
| P06T | 37441 | 17.2% | 17.2% | -61.0 | n/a | no target |
| P06 | 276 | 21.0% | 21.0% | -34.4 | 80% | ❌ 59 pts to go |
| P07 | 653 | 14.4% | 14.4% | -37.6 | 70% | ❌ 56 pts to go |
| P08 | 19441 | 9.1% | 9.1% | -43.3 | 70% | ❌ 61 pts to go |
| P09 | 305 | 87.2% | 87.2% | -1.3 | 100% | ❌ 13 pts to go |
| P10R | 74764 | 100.0% | 100.0% |  | n/a | no target |
| P10 | 2591 | 30.7% | 30.7% | -11.7 | 70% | ❌ 39 pts to go |
| P11 | 5230 | 81.5% | 81.5% | +26.2 | 75% | ✅ met |
| P12 | 8 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P13 | 14237 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `vendor_trading_name`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 61 | 16.4% | 16.4% | -33.6 | n/a | no target |
| P01T | 269 | 19.0% | 19.0% | -0.6 | n/a | no target |
| P01_GOLD | 625 | 48.2% | 48.2% | -4.2 | 60% | ❌ 12 pts to go |
| P02 | 462 | 55.4% | 55.4% | -11.9 | 60% | 🟡 5 pts to go |
| P03 | 255 | 54.5% | 54.5% | -10.4 | 60% | 🟡 6 pts to go |
| P04 | 3204 | 33.5% | 33.5% | -22.0 | 55% | ❌ 22 pts to go |
| P05 | 413 | 23.0% | 23.0% | -2.3 | 50% | ❌ 27 pts to go |
| P06M | 5017 | 1.7% | 1.7% | -15.6 | n/a | no target |
| P06T | 37441 | 15.1% | 15.1% | -38.5 | n/a | no target |
| P06 | 276 | 26.8% | 26.8% | -26.2 | n/a | no target |
| P07 | 653 | 23.7% | 23.7% | -22.3 | 55% | ❌ 31 pts to go |
| P08 | 19441 | 15.8% | 15.8% | -31.7 | 50% | ❌ 34 pts to go |
| P09 | 305 | 70.8% | 70.8% | -0.6 | 70% | ✅ met |
| P10R | 74764 | 100.0% | 100.0% |  | n/a | no target |
| P10 | 2591 | 37.2% | 37.2% | -14.7 | 55% | ❌ 18 pts to go |
| P11 | 5230 | 81.1% | 81.1% | +38.1 | 50% | ✅ met |
| P12 | 8 | 87.5% | 87.5% | +3.3 | n/a | no target |
| P13 | 14237 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `vendor_phone`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 61 | 19.7% | 19.7% | -41.4 | n/a | no target |
| P01T | 269 | 30.1% | 30.1% | -0.3 | n/a | no target |
| P01_GOLD | 625 | 49.6% | 49.6% | -2.2 | 70% | ❌ 20 pts to go |
| P02 | 462 | 52.2% | 52.2% | -5.0 | 70% | ❌ 18 pts to go |
| P03 | 255 | 49.4% | 49.4% | -7.8 | 70% | ❌ 21 pts to go |
| P04 | 3204 | 35.0% | 35.0% | -17.0 | 65% | ❌ 30 pts to go |
| P05 | 413 | 31.2% | 31.2% | -3.4 | 60% | ❌ 29 pts to go |
| P06M | 5017 | 3.0% | 3.0% | -27.4 | n/a | no target |
| P06T | 37441 | 22.7% | 22.7% | +19.2 | n/a | no target |
| P06 | 276 | 45.7% | 45.7% | -13.9 | 40% | ✅ met |
| P07 | 653 | 41.8% | 41.8% | -26.1 | 85% | ❌ 43 pts to go |
| P08 | 19441 | 33.5% | 33.5% | -34.6 | 85% | ❌ 52 pts to go |
| P09 | 305 | 52.8% | 52.8% | -2.6 | 85% | ❌ 32 pts to go |
| P10R | 74764 | 0.0% | 0.0% |  | n/a | no target |
| P10 | 2591 | 51.4% | 51.4% | -14.9 | 85% | ❌ 34 pts to go |
| P11 | 5230 | 8.0% | 8.0% | -46.9 | 75% | ❌ 67 pts to go |
| P12 | 8 | 25.0% | 25.0% | +9.2 | n/a | no target |
| P13 | 14237 | 100.0% | 100.0% | +0.0 | 60% | ✅ met |

### `vendor_website`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 61 | 24.6% | 24.6% | -69.8 | n/a | no target |
| P01T | 269 | 95.9% | 95.9% | +5.7 | n/a | no target |
| P01_GOLD | 625 | 89.4% | 89.4% | +0.0 | 90% | 🟡 1 pts to go |
| P02 | 462 | 89.2% | 89.2% | +1.6 | 90% | 🟡 1 pts to go |
| P03 | 255 | 91.0% | 91.0% | +1.1 | 90% | ✅ met |
| P04 | 3204 | 89.8% | 89.8% | +8.5 | 85% | ✅ met |
| P05 | 413 | 51.3% | 51.3% | +0.3 | 70% | ❌ 19 pts to go |
| P06M | 5017 | 7.5% | 7.5% | -60.4 | n/a | no target |
| P06T | 37441 | 95.0% | 95.0% | +17.1 | n/a | no target |
| P06 | 276 | 98.2% | 98.2% | +1.2 | 50% | ✅ met |
| P07 | 653 | 98.8% | 98.8% | +2.0 | 100% | 🟡 1 pts to go |
| P08 | 19441 | 99.4% | 99.4% | +3.3 | 100% | 🟡 1 pts to go |
| P09 | 305 | 80.0% | 80.0% | +0.2 | 100% | ❌ 20 pts to go |
| P10R | 74764 | 100.0% | 100.0% |  | n/a | no target |
| P10 | 2591 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P11 | 5230 | 99.3% | 99.3% | +6.3 | 100% | 🟡 1 pts to go |
| P12 | 8 | 37.5% | 37.5% | -4.6 | n/a | no target |
| P13 | 14237 | 100.0% | 100.0% | +0.0 | n/a | no target |

### `vendor_emails`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 61 | 16.4% | 16.4% | -33.6 | n/a | no target |
| P01T | 269 | 38.7% | 38.7% | -7.0 | n/a | no target |
| P01_GOLD | 625 | 46.2% | 46.2% | +0.5 | 70% | ❌ 24 pts to go |
| P02 | 462 | 48.5% | 48.5% | -3.0 | 75% | ❌ 26 pts to go |
| P03 | 255 | 43.9% | 43.9% | -7.5 | 75% | ❌ 31 pts to go |
| P04 | 3204 | 30.7% | 30.7% | -12.2 | 70% | ❌ 39 pts to go |
| P05 | 413 | 25.4% | 25.4% | +0.9 | 55% | ❌ 30 pts to go |
| P06M | 5017 | 2.0% | 2.0% | -14.1 | n/a | no target |
| P06T | 37441 | 18.8% | 18.8% | +15.9 | n/a | no target |
| P06 | 276 | 37.0% | 37.0% | -4.0 | n/a | no target |
| P07 | 653 | 36.9% | 36.9% | +0.0 | 70% | ❌ 33 pts to go |
| P08 | 19441 | 34.7% | 34.7% | -14.0 | 75% | ❌ 40 pts to go |
| P09 | 305 | 49.5% | 49.5% | -2.5 | 85% | ❌ 36 pts to go |
| P10R | 74764 | 0.0% | 0.0% |  | n/a | no target |
| P10 | 2591 | 38.9% | 38.9% | -12.4 | 80% | ❌ 41 pts to go |
| P11 | 5230 | 7.1% | 7.1% | -33.4 | 70% | ❌ 63 pts to go |
| P12 | 8 | 25.0% | 25.0% | -6.6 | n/a | no target |
| P13 | 14237 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `vendor_logo_url`

> ceiling: needs the vendor's website first; sites that block automated readers (robots.txt / 403) are never read

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 61 | 23.0% | 23.0% | -71.4 | n/a | no target |
| P01T | 269 | 64.7% | 64.7% | -24.4 | n/a | no target |
| P01_GOLD | 625 | 79.8% | 79.8% | +0.0 | 90% | ❌ 10 pts to go |
| P02 | 462 | 75.8% | 75.8% | -1.4 | 90% | ❌ 14 pts to go |
| P03 | 255 | 82.7% | 82.7% | +1.0 | 90% | 🟡 7 pts to go |
| P04 | 3204 | 60.0% | 60.0% | -10.9 | 85% | ❌ 25 pts to go |
| P05 | 413 | 48.4% | 48.4% | +0.0 | 75% | ❌ 27 pts to go |
| P06M | 5017 | 4.7% | 4.7% | -63.2 | n/a | no target |
| P06T | 37441 | 39.2% | 39.2% | -37.9 | n/a | no target |
| P06 | 276 | 60.5% | 60.5% | -28.1 | n/a | no target |
| P07 | 653 | 55.4% | 55.4% | -35.1 | 100% | ❌ 45 pts to go |
| P08 | 19441 | 45.5% | 45.5% | -43.5 | 100% | ❌ 54 pts to go |
| P09 | 305 | 61.0% | 61.0% | -1.5 | n/a | no target |
| P10R | 74764 | 0.0% | 0.0% |  | n/a | no target |
| P10 | 2591 | 70.6% | 70.6% | -18.4 | 100% | ❌ 29 pts to go |
| P11 | 5230 | 69.3% | 69.3% | -5.2 | n/a | no target |
| P12 | 8 | 37.5% | 37.5% | +0.7 | n/a | no target |
| P13 | 14237 | 80.6% | 80.6% | -2.1 | n/a | no target |

### `vendor_neq`

> ceiling: only Québec-registered vendors have an NEQ; the share of QC vendors is reported next to the rate

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 61 | 50.8% | 50.8% | +50.8 | n/a | no target · QC vendors: 31 rows, 100.0% filled |
| P01T | 269 | 14.9% | 14.9% | -6.8 | n/a | no target · QC vendors: 5 rows, 100.0% filled |
| P01_GOLD | 625 | 43.8% | 43.8% | -4.1 | 95% | ❌ 51 pts to go · QC vendors: 53 rows, 98.1% filled |
| P02 | 462 | 55.0% | 55.0% | -13.6 | 95% | ❌ 40 pts to go · QC vendors: 107 rows, 100.0% filled |
| P03 | 255 | 46.3% | 46.3% | -9.5 | 95% | ❌ 49 pts to go · QC vendors: 17 rows, 100.0% filled |
| P04 | 3204 | 32.5% | 32.5% | -27.7 | 95% | ❌ 62 pts to go · QC vendors: 460 rows, 98.7% filled |
| P05 | 413 | 14.5% | 14.5% | -0.3 | n/a | no target · QC vendors: 34 rows, 94.1% filled |
| P06M | 5017 | 55.5% | 55.5% | +55.5 | n/a | no target · QC vendors: 2782 rows, 100.0% filled |
| P06T | 37441 | 12.2% | 12.2% | -43.7 | n/a | no target · QC vendors: 548 rows, 100.0% filled |
| P06 | 276 | 8.7% | 8.7% | -17.8 | n/a | no target · QC vendors: 13 rows, 100.0% filled |
| P07 | 653 | 6.0% | 6.0% | -15.4 | n/a | no target · QC vendors: 24 rows, 95.8% filled |
| P08 | 19441 | 4.8% | 4.8% | -24.1 | n/a | no target · QC vendors: 620 rows, 99.4% filled |
| P09 | 305 | 78.0% | 78.0% | -2.1 | 95% | ❌ 17 pts to go · QC vendors: 111 rows, 100.0% filled |
| P10R | 74764 | 0.0% | 0.0% |  | n/a | no target |
| P10 | 2591 | 16.8% | 16.8% | -6.6 | n/a | no target · QC vendors: 259 rows, 95.4% filled |
| P11 | 5230 | 60.6% | 60.6% | +31.3 | n/a | no target · QC vendors: 75 rows, 98.7% filled |
| P12 | 8 | 62.5% | 62.5% | -11.2 | n/a | no target · QC vendors: 1 rows, 100.0% filled |
| P13 | 14237 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `vendor_years_in_business`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 61 | 68.9% | 68.9% | +7.8 | n/a | no target · vendors with a registry record: 42 rows, 100.0% filled |
| P01T | 269 | 30.1% | 30.1% | -32.9 | n/a | no target · vendors with a registry record: 81 rows, 100.0% filled |
| P01_GOLD | 625 | 79.4% | 79.4% | -4.1 | 100% | ❌ 21 pts to go · vendors with a registry record: 496 rows, 100.0% filled |
| P02 | 462 | 76.2% | 76.2% | -12.9 | 100% | ❌ 24 pts to go · vendors with a registry record: 352 rows, 100.0% filled |
| P03 | 255 | 79.6% | 79.6% | -9.3 | 100% | ❌ 20 pts to go · vendors with a registry record: 203 rows, 100.0% filled |
| P04 | 3204 | 44.8% | 44.8% | -36.6 | 100% | ❌ 55 pts to go · vendors with a registry record: 1434 rows, 100.0% filled |
| P05 | 413 | 57.9% | 57.9% | -3.8 | n/a | no target · vendors with a registry record: 239 rows, 100.0% filled |
| P06M | 5017 | 56.1% | 56.1% | +35.3 | n/a | no target · vendors with a registry record: 2817 rows, 100.0% filled |
| P06T | 37441 | 17.2% | 17.2% | -61.0 | n/a | no target · vendors with a registry record: 6436 rows, 100.0% filled |
| P06 | 276 | 21.7% | 21.7% | -36.1 | n/a | no target · vendors with a registry record: 60 rows, 100.0% filled |
| P07 | 653 | 14.7% | 14.7% | -39.7 | n/a | no target · vendors with a registry record: 96 rows, 100.0% filled |
| P08 | 19441 | 9.1% | 9.1% | -45.2 | n/a | no target · vendors with a registry record: 1778 rows, 100.0% filled |
| P09 | 305 | 90.8% | 90.8% | -0.8 | n/a | no target · vendors with a registry record: 277 rows, 100.0% filled |
| P10R | 74764 | 100.0% | 100.0% |  | n/a | no target · vendors with a registry record: 74764 rows, 100.0% filled |
| P10 | 2591 | 31.6% | 31.6% | -12.1 | n/a | no target · vendors with a registry record: 820 rows, 100.0% filled |
| P11 | 5230 | 81.8% | 81.8% | +23.6 | n/a | no target · vendors with a registry record: 4278 rows, 100.0% filled |
| P12 | 8 | 100.0% | 100.0% | +0.0 | n/a | no target · vendors with a registry record: 8 rows, 100.0% filled |
| P13 | 14237 | 0.0% | 0.0% | +0.0 | n/a | no target |

## 3. buyer

### `buyer_legal_name_as_published`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 61 | 90.2% | 90.2% | -4.2 | 90% | ✅ met |
| P01T | 269 | 58.0% | 58.0% | -36.6 | 90% | ❌ 32 pts to go |
| P01_GOLD | 625 | 84.6% | 84.6% | +0.0 | 95% | ❌ 10 pts to go |
| P02 | 462 | 82.9% | 82.9% | -7.7 | 95% | ❌ 12 pts to go |
| P03 | 255 | 78.8% | 78.8% | -4.4 | 85% | 🟡 6 pts to go |
| P04 | 3204 | 47.6% | 47.6% | -31.2 | 90% | ❌ 42 pts to go |
| P05 | 413 | 66.6% | 66.6% | -9.2 | 75% | 🟡 8 pts to go |
| P06M | 5017 | 87.3% | 87.3% | -1.4 | n/a | no target |
| P06T | 37441 | 19.7% | 19.7% | -44.7 | n/a | no target |
| P06 | 276 | 39.9% | 39.9% | -16.7 | 80% | ❌ 40 pts to go |
| P07 | 653 | 28.0% | 28.0% | -25.6 | 80% | ❌ 52 pts to go |
| P08 | 19441 | 16.6% | 16.6% | -20.2 | 75% | ❌ 58 pts to go |
| P09 | 305 | 76.4% | 76.4% | -4.4 | 95% | ❌ 19 pts to go |
| P10R | 74764 | 13.1% | 13.1% |  | n/a | no target |
| P10 | 2591 | 22.8% | 22.8% | -9.2 | 70% | ❌ 47 pts to go |
| P11 | 5230 | 3.9% | 3.9% | -21.0 | 65% | ❌ 61 pts to go |
| P12 | 8 | 75.0% | 75.0% | +1.3 | 80% | 🟡 5 pts to go |
| P13 | 14237 | 49.0% | 49.1% | -3.5 | 60% | ❌ 11 pts to go |

### `buyer_bn_as_published`

> ceiling: a buyer's BN is public only where the buyer prints it or a public dataset carries it (CRA charities, federal grants & contributions recipients, business registries for corporations); municipalities rarely publish theirs

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 61 | 19.7% | 19.7% | -19.2 | 50% | ❌ 30 pts to go |
| P01T | 269 | 14.9% | 14.9% | -5.8 | n/a | no target |
| P01_GOLD | 625 | 20.5% | 20.5% | +0.1 | 40% | ❌ 20 pts to go |
| P02 | 462 | 19.3% | 19.3% | -2.5 | 40% | ❌ 21 pts to go |
| P03 | 255 | 22.4% | 22.4% | -4.5 | 40% | ❌ 18 pts to go |
| P04 | 3204 | 15.2% | 15.2% | -12.4 | 40% | ❌ 25 pts to go |
| P05 | 413 | 19.4% | 19.4% | -3.5 | 25% | 🟡 6 pts to go |
| P06M | 5017 | 10.6% | 10.6% | -15.0 | n/a | no target |
| P06T | 37441 | 9.0% | 9.0% | -21.9 | n/a | no target |
| P06 | 276 | 12.7% | 12.7% | +1.9 | 35% | ❌ 22 pts to go |
| P07 | 653 | 9.0% | 9.0% | -1.3 | 35% | ❌ 26 pts to go |
| P08 | 19441 | 7.3% | 7.3% | -3.8 | 35% | ❌ 28 pts to go |
| P09 | 305 | 16.1% | 16.1% | -1.0 | n/a | no target |
| P10R | 74764 | 6.1% | 6.1% |  | n/a | no target |
| P10 | 2591 | 4.9% | 4.9% | -4.7 | 30% | ❌ 25 pts to go |
| P11 | 5230 | 1.0% | 1.0% | -7.4 | n/a | no target |
| P12 | 8 | 12.5% | 12.5% | +2.0 | n/a | no target |
| P13 | 14237 | 28.9% | 28.9% | +3.0 | 30% | 🟡 1 pts to go |

### `buyer_address`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 61 | 100.0% | 100.0% | +5.6 | 100% | ✅ met |
| P01T | 269 | 92.9% | 92.9% | -0.6 | 100% | 🟡 7 pts to go |
| P01_GOLD | 625 | 90.2% | 90.2% | +2.5 | 100% | 🟡 10 pts to go |
| P02 | 462 | 95.2% | 95.2% | -1.6 | 100% | 🟡 5 pts to go |
| P03 | 255 | 89.4% | 89.4% | -2.4 | 100% | ❌ 11 pts to go |
| P04 | 3204 | 75.8% | 75.8% | -15.2 | 100% | ❌ 24 pts to go |
| P05 | 413 | 87.2% | 87.2% | +2.3 | 100% | ❌ 13 pts to go |
| P06M | 5017 | 97.8% | 97.8% | +25.8 | n/a | no target |
| P06T | 37441 | 76.4% | 76.4% | -3.8 | n/a | no target |
| P06 | 276 | 78.3% | 78.3% | +9.6 | 95% | ❌ 17 pts to go |
| P07 | 653 | 80.6% | 80.6% | +10.0 | 95% | ❌ 14 pts to go |
| P08 | 19441 | 76.7% | 76.7% | +10.5 | 95% | ❌ 18 pts to go |
| P09 | 305 | 95.7% | 95.7% | +0.2 | 100% | 🟡 4 pts to go |
| P10R | 74764 | 59.7% | 59.8% |  | n/a | no target |
| P10 | 2591 | 62.9% | 62.9% | -2.3 | 95% | ❌ 32 pts to go |
| P11 | 5230 | 74.2% | 74.2% | +39.8 | 80% | 🟡 6 pts to go |
| P12 | 8 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P13 | 14237 | 77.9% | 77.9% | +1.8 | 95% | ❌ 17 pts to go |

### `buyer_phone`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 61 | 91.8% | 91.8% | +2.9 | n/a | no target |
| P01T | 269 | 59.9% | 59.9% | -20.5 | n/a | no target |
| P01_GOLD | 625 | 70.4% | 70.4% | +0.2 | 90% | ❌ 20 pts to go |
| P02 | 462 | 73.8% | 73.8% | -5.9 | 95% | ❌ 21 pts to go |
| P03 | 255 | 72.9% | 72.9% | -0.7 | 95% | ❌ 22 pts to go |
| P04 | 3204 | 54.9% | 54.9% | -30.0 | 95% | ❌ 40 pts to go |
| P05 | 413 | 69.7% | 69.7% | -5.3 | 90% | ❌ 20 pts to go |
| P06M | 5017 | 90.4% | 90.4% | +6.5 | n/a | no target |
| P06T | 37441 | 30.9% | 30.9% | -46.4 | n/a | no target |
| P06 | 276 | 43.1% | 43.1% | -21.4 | 95% | ❌ 52 pts to go |
| P07 | 653 | 34.5% | 34.5% | -31.8 | 90% | ❌ 56 pts to go |
| P08 | 19441 | 26.7% | 26.7% | -48.0 | 95% | ❌ 68 pts to go |
| P09 | 305 | 86.6% | 86.6% | -2.4 | 100% | ❌ 13 pts to go |
| P10R | 74764 | 25.2% | 25.2% |  | n/a | no target |
| P10 | 2591 | 43.9% | 43.9% | -27.6 | 95% | ❌ 51 pts to go |
| P11 | 5230 | 6.5% | 6.5% | -22.4 | 75% | ❌ 68 pts to go |
| P12 | 8 | 75.0% | 75.0% | -14.5 | n/a | no target |
| P13 | 14237 | 53.2% | 53.2% | -26.1 | 95% | ❌ 42 pts to go |

### `buyer_logo_url`

> ceiling: sites that block automated readers (robots.txt / 403) are never read; an og:image that looks like a photo is labelled

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 61 | 68.9% | 68.9% | -8.9 | n/a | no target |
| P01T | 269 | 69.1% | 69.1% | -22.2 | 95% | ❌ 26 pts to go |
| P01_GOLD | 625 | 82.2% | 82.2% | +0.0 | 90% | 🟡 8 pts to go |
| P02 | 462 | 83.1% | 83.1% | -5.3 | 95% | ❌ 12 pts to go |
| P03 | 255 | 83.5% | 83.5% | -1.1 | 95% | ❌ 12 pts to go |
| P04 | 3204 | 61.2% | 61.2% | -23.0 | 90% | ❌ 29 pts to go |
| P05 | 413 | 86.2% | 86.2% | -3.4 | 95% | 🟡 9 pts to go |
| P06M | 5017 | 58.4% | 58.4% | -26.7 | n/a | no target |
| P06T | 37441 | 34.7% | 34.7% | -59.4 | n/a | no target |
| P06 | 276 | 56.9% | 56.9% | -33.5 | 100% | ❌ 43 pts to go |
| P07 | 653 | 45.9% | 45.9% | -42.2 | 100% | ❌ 54 pts to go |
| P08 | 19441 | 30.9% | 30.9% | -59.8 | 100% | ❌ 69 pts to go |
| P09 | 305 | 69.2% | 69.2% | -4.8 | n/a | no target |
| P10R | 74764 | 27.8% | 27.8% |  | n/a | no target |
| P10 | 2591 | 63.2% | 63.2% | -26.9 | 100% | ❌ 37 pts to go |
| P11 | 5230 | 8.8% | 8.8% | -27.7 | 80% | ❌ 71 pts to go |
| P12 | 8 | 100.0% | 100.0% | +15.8 | n/a | no target |
| P13 | 14237 | 53.4% | 53.4% | -30.8 | 95% | ❌ 42 pts to go |

## 4. AP

### `ap_contact_name_as_published`

> ceiling: owner 2026-11-08: the AP contact person the organisation itself names on its AP / finance page is allowed (name + role phrase, quoted); mailboxes stay organisational; many bodies publish no AP person

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 61 | 6.6% | 6.6% | -10.1 | n/a | no target |
| P01T | 269 | 10.4% | 10.4% | -13.5 | n/a | no target |
| P01_GOLD | 625 | 14.2% | 14.2% | -0.1 | 25% | ❌ 11 pts to go |
| P02 | 462 | 24.7% | 24.7% | -3.0 | 40% | ❌ 15 pts to go |
| P03 | 255 | 9.0% | 9.0% | -1.6 | 20% | ❌ 11 pts to go |
| P04 | 3204 | 3.8% | 3.8% | -3.6 | 20% | ❌ 16 pts to go |
| P05 | 413 | 3.4% | 3.4% | -0.5 | 15% | ❌ 12 pts to go |
| P06M | 5017 | 0.4% | 0.4% | -4.4 | n/a | no target |
| P06T | 37441 | 0.5% | 0.5% | -2.7 | n/a | no target |
| P06 | 276 | 5.4% | 5.4% | +0.0 | n/a | no target |
| P07 | 653 | 7.2% | 7.2% | +0.9 | n/a | no target |
| P08 | 19441 | 0.3% | 0.3% | -0.7 | n/a | no target |
| P09 | 305 | 7.5% | 7.5% | -0.4 | n/a | no target |
| P10R | 74764 | 0.2% | 0.2% |  | n/a | no target |
| P10 | 2591 | 1.0% | 1.0% | -0.3 | n/a | no target |
| P11 | 5230 | 0.3% | 0.3% | -2.2 | n/a | no target |
| P12 | 8 | 0.0% | 0.0% | -10.5 | n/a | no target |
| P13 | 14237 | 0.6% | 0.6% | +0.0 | n/a | no target |

### `ap_phone`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 61 | 29.5% | 29.5% | -9.4 | n/a | no target |
| P01T | 269 | 30.5% | 30.5% | -4.3 | 70% | ❌ 40 pts to go |
| P01_GOLD | 625 | 43.2% | 43.2% | -0.1 | 80% | ❌ 37 pts to go |
| P02 | 462 | 57.4% | 57.4% | -6.7 | 90% | ❌ 33 pts to go |
| P03 | 255 | 19.2% | 19.2% | -3.9 | 60% | ❌ 41 pts to go |
| P04 | 3204 | 25.0% | 25.0% | -25.5 | 85% | ❌ 60 pts to go |
| P05 | 413 | 12.1% | 12.1% | -0.9 | 50% | ❌ 38 pts to go |
| P06M | 5017 | 0.7% | 0.7% | -5.8 | n/a | no target |
| P06T | 37441 | 0.8% | 0.8% | -1.9 | n/a | no target |
| P06 | 276 | 17.8% | 17.8% | -0.3 | n/a | no target |
| P07 | 653 | 12.9% | 12.9% | -6.1 | n/a | no target |
| P08 | 19441 | 0.5% | 0.5% | -0.1 | n/a | no target |
| P09 | 305 | 77.4% | 77.4% | -3.2 | 95% | ❌ 18 pts to go |
| P10R | 74764 | 0.3% | 0.3% |  | n/a | no target |
| P10 | 2591 | 1.8% | 1.8% | -1.3 | n/a | no target |
| P11 | 5230 | 6.6% | 6.6% | -22.7 | n/a | no target |
| P12 | 8 | 25.0% | 25.0% | -6.6 | n/a | no target |
| P13 | 14237 | 0.9% | 0.9% | -0.1 | n/a | no target |

### `invoice_mailing_address`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 61 | 4.9% | 4.9% | +4.9 | n/a | no target |
| P01T | 269 | 14.9% | 14.9% | -1.4 | n/a | no target |
| P01_GOLD | 625 | 33.8% | 33.8% | -0.2 | 70% | ❌ 36 pts to go |
| P02 | 462 | 39.2% | 39.2% | -5.1 | 75% | ❌ 36 pts to go |
| P03 | 255 | 19.2% | 19.2% | -3.9 | 55% | ❌ 36 pts to go |
| P04 | 3204 | 24.9% | 24.9% | -25.6 | 75% | ❌ 50 pts to go |
| P05 | 413 | 11.1% | 11.1% | -0.6 | 50% | ❌ 39 pts to go |
| P06M | 5017 | 0.2% | 0.2% | -1.6 | n/a | no target |
| P06T | 37441 | 0.5% | 0.5% | -1.0 | n/a | no target |
| P06 | 276 | 9.4% | 9.4% | -0.8 | n/a | no target |
| P07 | 653 | 6.0% | 6.0% | -4.3 | n/a | no target |
| P08 | 19441 | 0.2% | 0.2% | -0.3 | n/a | no target |
| P09 | 305 | 75.1% | 75.1% | -2.6 | 95% | ❌ 20 pts to go |
| P10R | 74764 | 0.2% | 0.2% |  | n/a | no target |
| P10 | 2591 | 1.1% | 1.1% | -0.7 | n/a | no target |
| P11 | 5230 | 6.5% | 6.5% | -22.4 | n/a | no target |
| P12 | 8 | 12.5% | 12.5% | -3.3 | n/a | no target |
| P13 | 14237 | 0.6% | 0.6% | +0.0 | n/a | no target |

### `invoicing_requirements`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 61 | 6.6% | 6.6% | -10.1 | n/a | no target |
| P01T | 269 | 11.5% | 11.5% | -8.1 | n/a | no target |
| P01_GOLD | 625 | 57.9% | 58.1% | +0.0 | 80% | ❌ 22 pts to go |
| P02 | 462 | 46.1% | 46.3% | -6.1 | 75% | ❌ 29 pts to go |
| P03 | 255 | 37.6% | 37.6% | -7.6 | 70% | ❌ 32 pts to go |
| P04 | 3204 | 24.5% | 25.0% | -24.2 | 70% | ❌ 46 pts to go |
| P05 | 413 | 14.8% | 14.8% | -1.6 | 50% | ❌ 35 pts to go |
| P06M | 5017 | 0.7% | 0.7% | -3.5 | n/a | no target |
| P06T | 37441 | 0.4% | 0.4% | -1.2 | n/a | no target |
| P06 | 276 | 14.5% | 14.5% | -9.6 | n/a | no target |
| P07 | 653 | 2.6% | 2.6% | -2.6 | n/a | no target |
| P08 | 19441 | 0.4% | 0.4% | -0.6 | n/a | no target |
| P09 | 305 | 45.6% | 45.9% | +1.5 | 80% | ❌ 34 pts to go |
| P10R | 74764 | 0.1% | 0.1% |  | n/a | no target |
| P10 | 2591 | 1.2% | 1.3% | -0.3 | n/a | no target |
| P11 | 5230 | 2.1% | 2.1% | -14.6 | n/a | no target |
| P12 | 8 | 25.0% | 25.0% | -6.6 | n/a | no target |
| P13 | 14237 | 0.4% | 0.4% | +0.1 | n/a | no target |

### `payment_terms_as_published`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 61 | 14.8% | 14.8% | -24.1 | n/a | no target |
| P01T | 269 | 24.9% | 24.9% | -31.6 | 60% | ❌ 35 pts to go |
| P01_GOLD | 625 | 63.5% | 63.5% | +0.0 | 70% | 🟡 6 pts to go |
| P02 | 462 | 38.7% | 38.7% | -5.1 | 50% | ❌ 11 pts to go |
| P03 | 255 | 50.2% | 50.2% | -5.1 | 55% | 🟡 5 pts to go |
| P04 | 3204 | 13.8% | 13.8% | -9.1 | 40% | ❌ 26 pts to go |
| P05 | 413 | 17.7% | 17.7% | +0.3 | 40% | ❌ 22 pts to go |
| P06M | 5017 | 1.1% | 1.1% | -15.6 | n/a | no target |
| P06T | 37441 | 1.9% | 1.9% | -10.6 | n/a | no target |
| P06 | 276 | 20.7% | 20.7% | -10.0 | n/a | no target |
| P07 | 653 | 7.2% | 7.2% | -9.1 | n/a | no target |
| P08 | 19441 | 3.0% | 3.0% | -1.7 | n/a | no target |
| P09 | 305 | 5.9% | 5.9% | +0.1 | n/a | no target |
| P10R | 74764 | 0.2% | 0.2% |  | n/a | no target |
| P10 | 2591 | 4.3% | 4.3% | +0.4 | n/a | no target |
| P11 | 5230 | 7.2% | 7.2% | -0.4 | n/a | no target |
| P12 | 8 | 12.5% | 12.5% | -3.3 | n/a | no target |
| P13 | 14237 | 0.2% | 0.2% | -0.1 | n/a | no target |

### `po_required_as_published`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 61 | 19.7% | 19.7% | -24.7 | n/a | no target |
| P01T | 269 | 30.9% | 30.9% | -38.7 | 65% | ❌ 34 pts to go |
| P01_GOLD | 625 | 69.1% | 69.1% | -0.1 | 70% | 🟡 1 pts to go |
| P02 | 462 | 24.0% | 24.0% | -2.2 | 50% | ❌ 26 pts to go |
| P03 | 255 | 52.5% | 52.5% | -3.7 | 60% | 🟡 8 pts to go |
| P04 | 3204 | 6.0% | 6.0% | -3.9 | 40% | ❌ 34 pts to go |
| P05 | 413 | 20.1% | 20.1% | -1.3 | 45% | ❌ 25 pts to go |
| P06M | 5017 | 0.5% | 0.5% | -6.6 | n/a | no target |
| P06T | 37441 | 0.6% | 0.6% | -3.7 | n/a | no target |
| P06 | 276 | 33.7% | 33.7% | -14.5 | n/a | no target |
| P07 | 653 | 8.0% | 8.0% | -15.8 | n/a | no target |
| P08 | 19441 | 1.3% | 1.3% | -1.1 | n/a | no target |
| P09 | 305 | 9.8% | 9.8% | +1.1 | n/a | no target |
| P10R | 74764 | 0.0% | 0.0% |  | n/a | no target |
| P10 | 2591 | 2.4% | 2.4% | +0.3 | n/a | no target |
| P11 | 5230 | 1.9% | 1.9% | -4.9 | n/a | no target |
| P12 | 8 | 0.0% | 0.0% | -10.5 | n/a | no target |
| P13 | 14237 | 0.2% | 0.2% | +0.0 | n/a | no target |

### `invoice_portal_url`

> ceiling: only portals the buyer names on its own pages; informational tax-authority links are not portals

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 61 | 4.9% | 4.9% | -6.2 | n/a | no target |
| P01T | 269 | 17.5% | 17.5% | -27.1 | n/a | no target |
| P01_GOLD | 625 | 49.8% | 49.8% | +0.0 | 50% | 🟡 0 pts to go |
| P02 | 462 | 37.9% | 37.9% | -4.7 | n/a | no target |
| P03 | 255 | 53.3% | 53.3% | -5.4 | 60% | 🟡 7 pts to go |
| P04 | 3204 | 13.7% | 13.7% | -12.7 | n/a | no target |
| P05 | 413 | 15.5% | 15.5% | -1.2 | n/a | no target |
| P06M | 5017 | 0.4% | 0.4% | -3.8 | n/a | no target |
| P06T | 37441 | 0.6% | 0.6% | -3.4 | n/a | no target |
| P06 | 276 | 22.5% | 22.5% | -13.0 | n/a | no target |
| P07 | 653 | 8.1% | 8.1% | -10.6 | n/a | no target |
| P08 | 19441 | 0.6% | 0.6% | -0.9 | n/a | no target |
| P09 | 305 | 18.0% | 18.0% | -0.9 | n/a | no target |
| P10R | 74764 | 0.1% | 0.1% |  | n/a | no target |
| P10 | 2591 | 2.4% | 2.4% | +0.0 | n/a | no target |
| P11 | 5230 | 1.6% | 1.6% | -6.2 | n/a | no target |
| P12 | 8 | 0.0% | 0.0% | -21.1 | n/a | no target |
| P13 | 14237 | 0.5% | 0.5% | +0.1 | n/a | no target |

### `buyer_payment_method_preference`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 61 | 13.1% | 13.1% | -14.7 | 15% | 🟡 2 pts to go |
| P01T | 269 | 12.3% | 12.3% | -17.0 | 15% | 🟡 3 pts to go |
| P01_GOLD | 625 | 35.4% | 35.4% | +0.3 | 40% | 🟡 5 pts to go |
| P02 | 462 | 12.6% | 12.8% | -1.3 | 25% | ❌ 12 pts to go |
| P03 | 255 | 18.0% | 18.0% | -3.6 | 25% | 🟡 7 pts to go |
| P04 | 3204 | 2.8% | 2.8% | -2.4 | 15% | ❌ 12 pts to go |
| P05 | 413 | 6.8% | 6.8% | -1.3 | 15% | 🟡 8 pts to go |
| P06M | 5017 | 0.6% | 0.6% | -5.4 | 15% | ❌ 14 pts to go |
| P06T | 37441 | 0.3% | 0.3% | -1.2 | 15% | ❌ 15 pts to go |
| P06 | 276 | 9.4% | 9.4% | -0.8 | 15% | 🟡 6 pts to go |
| P07 | 653 | 3.2% | 3.2% | -3.5 | 15% | ❌ 12 pts to go |
| P08 | 19441 | 0.2% | 0.2% | -0.7 | 15% | ❌ 15 pts to go |
| P09 | 305 | 1.0% | 1.0% | +0.2 | 15% | ❌ 14 pts to go |
| P10R | 74764 | 0.2% | 0.2% |  | 15% | ❌ 15 pts to go |
| P10 | 2591 | 0.7% | 0.7% | -0.7 | 15% | ❌ 14 pts to go |
| P11 | 5230 | 0.3% | 0.3% | -1.0 | 15% | ❌ 15 pts to go |
| P12 | 8 | 0.0% | 0.0% | +0.0 | 15% | ❌ 15 pts to go |
| P13 | 14237 | 0.4% | 0.4% | -0.1 | 15% | ❌ 15 pts to go |

### `buyer_tax_exempt_status`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 61 | 6.6% | 6.6% | -4.5 | 15% | 🟡 8 pts to go |
| P01T | 269 | 13.8% | 13.8% | -18.8 | 25% | ❌ 11 pts to go |
| P01_GOLD | 625 | 29.1% | 29.1% | -0.1 | 25% | ✅ met |
| P02 | 462 | 25.3% | 25.3% | -2.7 | 15% | ✅ met |
| P03 | 255 | 21.6% | 21.6% | -4.4 | 15% | ✅ met |
| P04 | 3204 | 4.4% | 4.4% | -3.8 | 15% | ❌ 11 pts to go |
| P05 | 413 | 11.1% | 11.1% | -0.9 | 15% | 🟡 4 pts to go |
| P06M | 5017 | 0.3% | 0.3% | -2.1 | 15% | ❌ 15 pts to go |
| P06T | 37441 | 0.3% | 0.3% | -2.4 | 15% | ❌ 15 pts to go |
| P06 | 276 | 7.6% | 7.6% | -4.4 | 15% | 🟡 7 pts to go |
| P07 | 653 | 3.4% | 3.4% | -4.1 | 15% | ❌ 12 pts to go |
| P08 | 19441 | 0.5% | 0.5% | -0.5 | 15% | ❌ 14 pts to go |
| P09 | 305 | 1.0% | 1.0% | +0.2 | 15% | ❌ 14 pts to go |
| P10R | 74764 | 0.0% | 0.0% |  | 15% | ❌ 15 pts to go |
| P10 | 2591 | 1.4% | 1.4% | +0.0 | 15% | ❌ 14 pts to go |
| P11 | 5230 | 1.0% | 1.0% | -4.1 | 15% | ❌ 14 pts to go |
| P12 | 8 | 12.5% | 12.5% | -13.8 | 15% | 🟡 2 pts to go |
| P13 | 14237 | 0.1% | 0.1% | +0.0 | 15% | ❌ 15 pts to go |

### `buyer_ap_cycle_published`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 61 | 0.0% | 0.0% | -5.6 | 20% | ❌ 20 pts to go |
| P01T | 269 | 4.8% | 4.8% | -5.0 | 20% | ❌ 15 pts to go |
| P01_GOLD | 625 | 4.3% | 4.3% | +0.0 | 20% | ❌ 16 pts to go |
| P02 | 462 | 1.3% | 1.3% | -0.2 | 20% | ❌ 19 pts to go |
| P03 | 255 | 1.6% | 1.6% | -0.3 | 20% | ❌ 18 pts to go |
| P04 | 3204 | 0.6% | 0.6% | -0.4 | 20% | ❌ 19 pts to go |
| P05 | 413 | 1.2% | 1.2% | +0.2 | 20% | ❌ 19 pts to go |
| P06M | 5017 | 0.0% | 0.0% | +0.0 | 20% | ❌ 20 pts to go |
| P06T | 37441 | 0.0% | 0.0% | -0.2 | 20% | ❌ 20 pts to go |
| P06 | 276 | 1.4% | 1.4% | -2.2 | 20% | ❌ 19 pts to go |
| P07 | 653 | 0.6% | 0.6% | -0.2 | 20% | ❌ 19 pts to go |
| P08 | 19441 | 0.0% | 0.0% | -0.2 | 20% | ❌ 20 pts to go |
| P09 | 305 | 0.0% | 0.0% | +0.0 | 20% | ❌ 20 pts to go |
| P10R | 74764 | 0.0% | 0.0% |  | 20% | ❌ 20 pts to go |
| P10 | 2591 | 0.2% | 0.2% | -0.1 | 20% | ❌ 20 pts to go |
| P11 | 5230 | 0.1% | 0.1% | -0.5 | 20% | ❌ 20 pts to go |
| P12 | 8 | 0.0% | 0.0% | +0.0 | 20% | ❌ 20 pts to go |
| P13 | 14237 | 0.0% | 0.0% | +0.0 | 20% | ❌ 20 pts to go |

### `buyer_esignature_preference`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 61 | 1.6% | 1.6% | -4.0 | 15% | ❌ 13 pts to go |
| P01T | 269 | 3.0% | 3.0% | -4.6 | 15% | ❌ 12 pts to go |
| P01_GOLD | 625 | 10.6% | 10.6% | +0.0 | 15% | 🟡 4 pts to go |
| P02 | 462 | 11.9% | 11.9% | -1.5 | 15% | 🟡 3 pts to go |
| P03 | 255 | 20.8% | 20.8% | -3.2 | 15% | ✅ met |
| P04 | 3204 | 2.5% | 2.5% | -2.1 | 15% | ❌ 12 pts to go |
| P05 | 413 | 2.9% | 2.9% | +0.0 | 15% | ❌ 12 pts to go |
| P06M | 5017 | 0.2% | 0.2% | -2.2 | 15% | ❌ 15 pts to go |
| P06T | 37441 | 0.2% | 0.2% | -1.2 | 15% | ❌ 15 pts to go |
| P06 | 276 | 5.8% | 5.8% | +0.4 | 15% | 🟡 9 pts to go |
| P07 | 653 | 2.0% | 2.0% | -1.6 | 15% | ❌ 13 pts to go |
| P08 | 19441 | 0.4% | 0.4% | -0.3 | 15% | ❌ 15 pts to go |
| P09 | 305 | 0.7% | 0.7% | +0.2 | 15% | ❌ 14 pts to go |
| P10R | 74764 | 0.0% | 0.0% |  | 15% | ❌ 15 pts to go |
| P10 | 2591 | 0.9% | 0.9% | +0.1 | 15% | ❌ 14 pts to go |
| P11 | 5230 | 0.6% | 0.6% | -1.5 | 15% | ❌ 14 pts to go |
| P12 | 8 | 0.0% | 0.0% | -5.3 | 15% | ❌ 15 pts to go |
| P13 | 14237 | 0.1% | 0.1% | +0.0 | 15% | ❌ 15 pts to go |

### `ap_system_hint`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 61 | 6.6% | 6.6% | -4.5 | 20% | ❌ 13 pts to go |
| P01T | 269 | 17.8% | 17.8% | -23.5 | 40% | ❌ 22 pts to go |
| P01_GOLD | 625 | 45.8% | 45.8% | +0.0 | 40% | ✅ met |
| P02 | 462 | 43.1% | 43.1% | -5.4 | 20% | ✅ met |
| P03 | 255 | 49.0% | 49.0% | -6.8 | 35% | ✅ met |
| P04 | 3204 | 16.3% | 16.3% | -14.0 | 20% | 🟡 4 pts to go |
| P05 | 413 | 14.8% | 14.8% | -1.9 | 20% | 🟡 5 pts to go |
| P06M | 5017 | 0.6% | 0.6% | -3.6 | 20% | ❌ 19 pts to go |
| P06T | 37441 | 0.8% | 0.8% | -3.7 | 20% | ❌ 19 pts to go |
| P06 | 276 | 22.5% | 22.5% | -13.0 | 20% | ✅ met |
| P07 | 653 | 8.0% | 8.0% | -6.7 | 20% | ❌ 12 pts to go |
| P08 | 19441 | 0.9% | 0.9% | -1.4 | 20% | ❌ 19 pts to go |
| P09 | 305 | 18.0% | 18.0% | -4.0 | 20% | 🟡 2 pts to go |
| P10R | 74764 | 0.2% | 0.2% |  | 20% | ❌ 20 pts to go |
| P10 | 2591 | 3.2% | 3.2% | +0.6 | 20% | ❌ 17 pts to go |
| P11 | 5230 | 1.6% | 1.6% | -6.4 | 20% | ❌ 18 pts to go |
| P12 | 8 | 0.0% | 0.0% | -15.8 | 20% | ❌ 20 pts to go |
| P13 | 14237 | 0.7% | 0.7% | +0.1 | 20% | ❌ 19 pts to go |

## 5. contract

### `contract_value`

> ceiling: rows proven by a lobbying filing, a news release, an auditor appointment, a customer story or a vendor's client list have no contract value by nature (≈17 % of P01 Gold); bids&tenders awards now carry the awarded bidder's submitted price when no award value was published

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 61 | 52.5% | 52.5% | +52.5 | n/a | no target |
| P01T | 269 | 0.4% | 0.4% | -0.7 | n/a | no target |
| P01_GOLD | 625 | 69.4% | 69.4% | -0.3 | 95% | ❌ 26 pts to go |
| P02 | 462 | 63.9% | 63.9% | -9.4 | 95% | ❌ 31 pts to go |
| P03 | 255 | 54.9% | 54.9% | -12.4 | 90% | ❌ 35 pts to go |
| P04 | 3204 | 28.9% | 28.9% | -29.5 | 85% | ❌ 56 pts to go |
| P05 | 413 | 36.8% | 36.8% | +1.9 | 75% | ❌ 38 pts to go |
| P06M | 5017 | 60.8% | 60.8% | +60.8 | n/a | no target |
| P06T | 37441 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06 | 276 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P07 | 653 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P08 | 19441 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P09 | 305 | 89.2% | 89.2% | -1.6 | 100% | ❌ 11 pts to go |
| P10R | 74764 | 0.0% | 0.0% |  | n/a | no target |
| P10 | 2591 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P11 | 5230 | 1.6% | 1.6% | -17.2 | 60% | ❌ 58 pts to go |
| P12 | 8 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P13 | 14237 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `currency`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 61 | 52.5% | 52.5% | +52.5 | n/a | no target |
| P01T | 269 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P01_GOLD | 625 | 72.8% | 72.8% | -0.1 | 100% | ❌ 27 pts to go |
| P02 | 462 | 67.3% | 67.3% | -9.9 | 100% | ❌ 33 pts to go |
| P03 | 255 | 60.8% | 60.8% | -13.7 | n/a | no target |
| P04 | 3204 | 29.6% | 29.6% | -30.4 | 95% | ❌ 65 pts to go |
| P05 | 413 | 33.4% | 33.4% | +2.2 | 80% | ❌ 47 pts to go |
| P06M | 5017 | 60.8% | 60.8% | +60.8 | n/a | no target |
| P06T | 37441 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06 | 276 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P07 | 653 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P08 | 19441 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P09 | 305 | 92.5% | 92.5% | -0.9 | 100% | 🟡 8 pts to go |
| P10R | 74764 | 0.0% | 0.0% |  | n/a | no target |
| P10 | 2591 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P11 | 5230 | 1.8% | 1.8% | -18.2 | n/a | no target |
| P12 | 8 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P13 | 14237 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `start_date`

> ceiling: most award notices publish an award date, not a start date; start_date carries the signature date when the source gives one, labelled

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 61 | 70.5% | 70.5% | +70.5 | n/a | no target |
| P01T | 269 | 0.4% | 0.4% | -0.7 | n/a | no target |
| P01_GOLD | 625 | 51.7% | 51.7% | -0.2 | 85% | ❌ 33 pts to go |
| P02 | 462 | 58.4% | 58.4% | -8.4 | 90% | ❌ 32 pts to go |
| P03 | 255 | 44.3% | 44.3% | -10.5 | 85% | ❌ 41 pts to go |
| P04 | 3204 | 32.1% | 32.1% | -32.0 | 90% | ❌ 58 pts to go |
| P05 | 413 | 32.4% | 32.4% | -2.8 | 75% | ❌ 43 pts to go |
| P06M | 5017 | 89.5% | 89.5% | +89.5 | n/a | no target |
| P06T | 37441 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06 | 276 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P07 | 653 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P08 | 19441 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P09 | 305 | 84.9% | 84.9% | -0.7 | 95% | ❌ 10 pts to go |
| P10R | 74764 | 0.0% | 0.0% |  | n/a | no target |
| P10 | 2591 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P11 | 5230 | 1.5% | 1.5% | -15.8 | n/a | no target |
| P12 | 8 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P13 | 14237 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `end_date`

> ceiling: an inferred end (award date + published duration) is labelled as such; sources without a duration leave end_date empty — the honest ceiling. P09 is BY DEFINITION the rows whose end date is not published (older SEAO contracts with no closing notice): its end_date / duration targets cannot be met without inventing a date

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 61 | 70.5% | 70.5% | +70.5 | n/a | no target |
| P01T | 269 | 0.4% | 0.4% | -0.7 | n/a | no target |
| P01_GOLD | 625 | 51.7% | 51.7% | -0.4 | 85% | ❌ 33 pts to go |
| P02 | 462 | 53.5% | 53.5% | -7.6 | 90% | ❌ 36 pts to go |
| P03 | 255 | 45.5% | 45.5% | -10.7 | 85% | ❌ 40 pts to go |
| P04 | 3204 | 27.4% | 27.4% | -26.9 | 90% | ❌ 63 pts to go |
| P05 | 413 | 42.4% | 42.4% | +0.7 | 75% | ❌ 33 pts to go |
| P06M | 5017 | 82.5% | 82.5% | +82.5 | n/a | no target |
| P06T | 37441 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06 | 276 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P07 | 653 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P08 | 19441 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P09 | 305 | 0.3% | 0.3% | +0.0 | 95% | ❌ 95 pts to go |
| P10R | 74764 | 0.0% | 0.0% |  | n/a | no target |
| P10 | 2591 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P11 | 5230 | 1.3% | 1.3% | -12.8 | n/a | no target |
| P12 | 8 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P13 | 14237 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `contract_title`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 61 | 77.0% | 77.0% | +77.0 | n/a | no target |
| P01T | 269 | 91.1% | 91.1% | +9.6 | n/a | no target |
| P01_GOLD | 625 | 85.4% | 85.4% | -0.3 | 100% | ❌ 15 pts to go |
| P02 | 462 | 76.4% | 76.4% | -5.3 | 100% | ❌ 24 pts to go |
| P03 | 255 | 92.2% | 92.2% | -0.1 | n/a | no target |
| P04 | 3204 | 53.4% | 53.4% | -19.2 | 95% | ❌ 42 pts to go |
| P05 | 413 | 77.7% | 77.7% | +2.2 | 95% | ❌ 17 pts to go |
| P06M | 5017 | 96.9% | 96.9% | +96.3 | n/a | no target |
| P06T | 37441 | 89.6% | 89.6% | +6.2 | n/a | no target |
| P06 | 276 | 28.3% | 28.3% | -47.6 | n/a | no target |
| P07 | 653 | 21.6% | 21.6% | -55.4 | n/a | no target |
| P08 | 19441 | 13.0% | 13.0% | -71.9 | n/a | no target |
| P09 | 305 | 98.7% | 98.7% | -0.3 | 100% | 🟡 1 pts to go |
| P10R | 74764 | 100.0% | 100.0% |  | n/a | no target |
| P10 | 2591 | 72.9% | 72.9% | -25.5 | n/a | no target |
| P11 | 5230 | 34.6% | 34.6% | -55.3 | n/a | no target |
| P12 | 8 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P13 | 14237 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `contract_description`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 61 | 77.0% | 77.0% | +77.0 | n/a | no target |
| P01T | 269 | 91.1% | 91.1% | +9.6 | n/a | no target |
| P01_GOLD | 625 | 88.6% | 88.6% | -0.3 | 100% | ❌ 11 pts to go |
| P02 | 462 | 77.5% | 77.7% | -5.4 | 100% | ❌ 22 pts to go |
| P03 | 255 | 92.9% | 92.9% | -0.9 | n/a | no target |
| P04 | 3204 | 57.1% | 57.1% | -21.9 | 95% | ❌ 38 pts to go |
| P05 | 413 | 90.3% | 90.3% | +0.2 | 70% | ✅ met |
| P06M | 5017 | 96.9% | 96.9% | +96.3 | n/a | no target |
| P06T | 37441 | 89.6% | 89.6% | +6.2 | n/a | no target |
| P06 | 276 | 28.3% | 28.3% | -47.6 | n/a | no target |
| P07 | 653 | 21.6% | 21.6% | -55.4 | n/a | no target |
| P08 | 19441 | 13.0% | 13.0% | -71.9 | n/a | no target |
| P09 | 305 | 98.7% | 98.7% | -0.3 | 100% | 🟡 1 pts to go |
| P10R | 74764 | 100.0% | 100.0% |  | n/a | no target |
| P10 | 2591 | 72.9% | 72.9% | -25.5 | n/a | no target |
| P11 | 5230 | 34.7% | 34.7% | -55.6 | n/a | no target |
| P12 | 8 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P13 | 14237 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `number_of_bids`

> ceiling: published by some portals only (bids&tenders submission lists, Biddingo bidder lists); federal proactive disclosure does not publish bid counts

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 61 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P01T | 269 | 0.0% | 0.0% | -1.1 | n/a | no target |
| P01_GOLD | 625 | 16.8% | 16.8% | -0.5 | 60% | ❌ 43 pts to go · rows from a source that publishes bids: 362 rows, 29.0% filled |
| P02 | 462 | 11.3% | 11.3% | -1.8 | n/a | no target · rows from a source that publishes bids: 292 rows, 17.8% filled |
| P03 | 255 | 13.3% | 13.3% | -3.0 | n/a | no target · rows from a source that publishes bids: 139 rows, 24.5% filled |
| P04 | 3204 | 1.7% | 1.7% | -2.0 | n/a | no target · rows from a source that publishes bids: 872 rows, 6.3% filled |
| P05 | 413 | 3.1% | 3.1% | -0.3 | n/a | no target · rows from a source that publishes bids: 53 rows, 24.5% filled |
| P06M | 5017 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06T | 37441 | 0.0% | 0.0% | -0.1 | n/a | no target |
| P06 | 276 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P07 | 653 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P08 | 19441 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P09 | 305 | 3.0% | 3.0% | -0.1 | n/a | no target · rows from a source that publishes bids: 292 rows, 3.1% filled |
| P10R | 74764 | 0.0% | 0.0% |  | n/a | no target |
| P10 | 2591 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P11 | 5230 | 0.2% | 0.2% | -2.5 | n/a | no target · rows from a source that publishes bids: 88 rows, 12.5% filled |
| P12 | 8 | 0.0% | 0.0% | +0.0 | n/a | no target · rows from a source that publishes bids: 8 rows, 0.0% filled |
| P13 | 14237 | 0.0% | 0.0% | +0.0 | n/a | no target |

## 6. history

### `average_contract_duration_days`

> ceiling: needs two dates (or a published term) on the buyer's records; P09 rows (end date unpublished by definition) and buyers whose sources publish award dates only have no honest duration

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 61 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P01T | 269 | 0.4% | 98.1% | +0.4 | n/a | no target |
| P01_GOLD | 625 | 53.1% | 82.4% | -0.1 | 90% | ❌ 37 pts to go |
| P02 | 462 | 53.2% | 87.4% | -7.9 | 90% | ❌ 37 pts to go |
| P03 | 255 | 45.9% | 80.0% | -10.3 | 90% | ❌ 44 pts to go |
| P04 | 3204 | 22.3% | 92.9% | -23.0 | 90% | ❌ 68 pts to go |
| P05 | 413 | 0.0% | 82.3% | +0.0 | 90% | ❌ 90 pts to go |
| P06M | 5017 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P06T | 37441 | 0.0% | 99.8% | +0.0 | n/a | no target |
| P06 | 276 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P07 | 653 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P08 | 19441 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P09 | 305 | 2.3% | 3.9% | +0.2 | 90% | ❌ 88 pts to go |
| P10R | 74764 | 0.0% | 100.0% |  | n/a | no target |
| P10 | 2591 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P11 | 5230 | 1.1% | 99.2% | -11.6 | n/a | no target |
| P12 | 8 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P13 | 14237 | 0.0% | 100.0% | +0.0 | n/a | no target |

### `commodity_distribution_top3`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 61 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P01T | 269 | 0.7% | 98.5% | +0.7 | n/a | no target |
| P01_GOLD | 625 | 25.9% | 55.2% | -0.1 | 90% | ❌ 64 pts to go |
| P02 | 462 | 52.4% | 86.6% | -7.5 | n/a | no target |
| P03 | 255 | 25.1% | 59.2% | -5.7 | n/a | no target |
| P04 | 3204 | 24.4% | 95.1% | -25.3 | n/a | no target |
| P05 | 413 | 0.5% | 82.8% | +0.0 | n/a | no target |
| P06M | 5017 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P06T | 37441 | 0.1% | 99.9% | +0.1 | n/a | no target |
| P06 | 276 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P07 | 653 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P08 | 19441 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P09 | 305 | 41.6% | 43.3% | -2.8 | n/a | no target |
| P10R | 74764 | 0.0% | 100.0% |  | n/a | no target |
| P10 | 2591 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P11 | 5230 | 1.1% | 99.1% | -10.5 | n/a | no target |
| P12 | 8 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P13 | 14237 | 0.0% | 100.0% | +0.0 | n/a | no target |

### `year_over_year_spend_trend`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 61 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P01T | 269 | 1.9% | 99.6% | -0.3 | n/a | no target |
| P01_GOLD | 625 | 51.7% | 81.0% | +0.1 | 95% | ❌ 43 pts to go |
| P02 | 462 | 57.4% | 91.6% | -8.2 | n/a | no target |
| P03 | 255 | 48.2% | 82.4% | -10.9 | n/a | no target |
| P04 | 3204 | 24.7% | 95.3% | -25.6 | n/a | no target |
| P05 | 413 | 4.8% | 87.2% | -0.4 | n/a | no target |
| P06M | 5017 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P06T | 37441 | 0.1% | 100.0% | +0.1 | n/a | no target |
| P06 | 276 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P07 | 653 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P08 | 19441 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P09 | 305 | 63.9% | 65.6% | -3.6 | n/a | no target |
| P10R | 74764 | 0.0% | 100.0% |  | n/a | no target |
| P10 | 2591 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P11 | 5230 | 1.1% | 99.2% | -11.6 | n/a | no target |
| P12 | 8 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P13 | 14237 | 0.0% | 100.0% | +0.0 | n/a | no target |

## 7. mail security

### `mta_sts`

> ceiling: DNS-only check; 'no record' counts as checked

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 61 | 98.4% | 98.4% | -1.6 | 100% | 🟡 2 pts to go |
| P01T | 269 | 95.9% | 95.9% | -4.1 | 100% | 🟡 4 pts to go |
| P01_GOLD | 625 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P02 | 462 | 99.1% | 99.1% | -0.9 | 100% | 🟡 1 pts to go |
| P03 | 255 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P04 | 3204 | 97.9% | 97.9% | -2.1 | 100% | 🟡 2 pts to go |
| P05 | 413 | 98.8% | 98.8% | -1.2 | 100% | 🟡 1 pts to go |
| P06M | 5017 | 93.9% | 93.9% | -6.1 | 100% | 🟡 6 pts to go |
| P06T | 37441 | 86.7% | 86.7% | -13.3 | 100% | ❌ 13 pts to go |
| P06 | 276 | 98.9% | 98.9% | -1.1 | 100% | 🟡 1 pts to go |
| P07 | 653 | 96.8% | 96.8% | -3.2 | 100% | 🟡 3 pts to go |
| P08 | 19441 | 96.4% | 96.4% | -3.6 | 100% | 🟡 4 pts to go |
| P09 | 305 | 99.7% | 99.7% | -0.3 | 100% | 🟡 0 pts to go |
| P10R | 74764 | 75.5% | 75.5% |  | 100% | ❌ 24 pts to go |
| P10 | 2591 | 96.5% | 96.5% | -3.5 | 100% | 🟡 4 pts to go |
| P11 | 5230 | 95.2% | 95.2% | -4.8 | 100% | 🟡 5 pts to go |
| P12 | 8 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P13 | 14237 | 89.3% | 89.3% | -10.7 | 100% | ❌ 11 pts to go |

### `tls_rpt`

> ceiling: DNS-only check; 'no record' counts as checked

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 61 | 98.4% | 98.4% | -1.6 | 100% | 🟡 2 pts to go |
| P01T | 269 | 95.9% | 95.9% | -4.1 | 100% | 🟡 4 pts to go |
| P01_GOLD | 625 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P02 | 462 | 99.1% | 99.1% | -0.9 | 100% | 🟡 1 pts to go |
| P03 | 255 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P04 | 3204 | 97.9% | 97.9% | -2.1 | 100% | 🟡 2 pts to go |
| P05 | 413 | 98.8% | 98.8% | -1.2 | 100% | 🟡 1 pts to go |
| P06M | 5017 | 93.9% | 93.9% | -6.1 | 100% | 🟡 6 pts to go |
| P06T | 37441 | 86.7% | 86.7% | -13.3 | 100% | ❌ 13 pts to go |
| P06 | 276 | 98.9% | 98.9% | -1.1 | 100% | 🟡 1 pts to go |
| P07 | 653 | 96.8% | 96.8% | -3.2 | 100% | 🟡 3 pts to go |
| P08 | 19441 | 96.4% | 96.4% | -3.6 | 100% | 🟡 4 pts to go |
| P09 | 305 | 99.7% | 99.7% | -0.3 | 100% | 🟡 0 pts to go |
| P10R | 74764 | 75.5% | 75.5% |  | 100% | ❌ 24 pts to go |
| P10 | 2591 | 96.5% | 96.5% | -3.5 | 100% | 🟡 4 pts to go |
| P11 | 5230 | 95.2% | 95.2% | -4.8 | 100% | 🟡 5 pts to go |
| P12 | 8 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P13 | 14237 | 89.3% | 89.3% | -10.7 | 100% | ❌ 11 pts to go |

### `bimi`

> ceiling: DNS-only check; 'no record' counts as checked

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 61 | 98.4% | 98.4% | -1.6 | 100% | 🟡 2 pts to go |
| P01T | 269 | 95.9% | 95.9% | -4.1 | 100% | 🟡 4 pts to go |
| P01_GOLD | 625 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P02 | 462 | 99.1% | 99.1% | -0.9 | 100% | 🟡 1 pts to go |
| P03 | 255 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P04 | 3204 | 97.9% | 97.9% | -2.1 | 100% | 🟡 2 pts to go |
| P05 | 413 | 98.8% | 98.8% | -1.2 | 100% | 🟡 1 pts to go |
| P06M | 5017 | 93.9% | 93.9% | -6.1 | 100% | 🟡 6 pts to go |
| P06T | 37441 | 86.7% | 86.7% | -13.3 | 100% | ❌ 13 pts to go |
| P06 | 276 | 98.9% | 98.9% | -1.1 | 100% | 🟡 1 pts to go |
| P07 | 653 | 96.8% | 96.8% | -3.2 | 100% | 🟡 3 pts to go |
| P08 | 19441 | 96.4% | 96.4% | -3.6 | 100% | 🟡 4 pts to go |
| P09 | 305 | 99.7% | 99.7% | -0.3 | 100% | 🟡 0 pts to go |
| P10R | 74764 | 75.5% | 75.5% |  | 100% | ❌ 24 pts to go |
| P10 | 2591 | 96.5% | 96.5% | -3.5 | 100% | 🟡 4 pts to go |
| P11 | 5230 | 95.2% | 95.2% | -4.8 | 100% | 🟡 5 pts to go |
| P12 | 8 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P13 | 14237 | 89.3% | 89.3% | -10.7 | 100% | ❌ 11 pts to go |

