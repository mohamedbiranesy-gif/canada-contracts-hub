# Coverage vs the downstream team's targets — 2026-11-12

Benchmarks (field × package with a numeric target): **91 of 438 met** (20.8%); 64 within 10 points; 283 further away.
A cell counts as filled only when it carries a value: blank, `not_published`, `not_found_yet` and label-only cells ("no identifier published …", "no dataset record …", "0 in the contract dataset …") do not count; the DNS checks count when checked. `any` = share of non-blank cells incl. such labels. Δ = change since the previous build in `coord/results/coverage_history.csv`.
Rows per package: P01M 129, P01T 189, P01_GOLD 626, P02 464, P03 263, P04 3678, P05 422, P06M 14663, P06T 35923, P06 271, P07 691, P08 21900, P09 307, P10R 0, P10 2334, P11 1455, P12 15, P13 97406

## Invoice-grade readiness (the row as an invoice header: bill-to, submit-to, references, terms, tax, vendor identity, follow-up)

| package | rows | all 11 elements | ≥ 9 of 11 | median elements | most-missing element |
|---|---|---|---|---|---|
| P01M | 129 | 0.0% | 20.2% | 8 | vendor GST/HST number (114 rows) |
| P01T | 189 | 1.1% | 31.7% | 8 | payment terms (148 rows) |
| P01_GOLD | 626 | 25.1% | 71.9% | 10 | payment terms (214 rows) |
| P02 | 464 | 7.5% | 55.2% | 9 | PO rule (351 rows) |
| P03 | 263 | 14.8% | 57.4% | 9 | payment terms (130 rows) |
| P04 | 3678 | 1.3% | 16.9% | 6 | PO rule (3477 rows) |
| P05 | 422 | 1.2% | 17.8% | 7 | payment terms (348 rows) |
| P06M | 14663 | 0.0% | 3.2% | 8 | PO rule (14457 rows) |
| P06T | 35923 | 0.0% | 10.2% | 6 | PO rule (35680 rows) |
| P06 | 271 | 0.0% | 11.4% | 6 | reference to quote (PO / contract / vendor id) (271 rows) |
| P07 | 691 | 0.0% | 2.6% | 6 | reference to quote (PO / contract / vendor id) (691 rows) |
| P08 | 21900 | 0.0% | 0.6% | 6 | reference to quote (PO / contract / vendor id) (21900 rows) |
| P09 | 307 | 1.3% | 45.3% | 8 | payment terms (286 rows) |
| P10 | 2334 | 0.0% | 1.1% | 5 | reference to quote (PO / contract / vendor id) (2334 rows) |
| P11 | 1455 | 0.4% | 7.5% | 5 | PO rule (1381 rows) |
| P12 | 15 | 0.0% | 53.3% | 9 | PO rule (14 rows) |
| P13 | 97406 | 0.0% | 0.3% | 6 | reference to quote (PO / contract / vendor id) (97406 rows) |

## AP grade (how stringently the row's accounts-payable data meets what an invoice needs; A = invoicing mailbox referee-confirmed on the buyer's own domain with MX, legal name, address, PO rule and terms all published, no penalties)

| package | rows | A | B | C | D | E | median ap_score |
|---|---|---|---|---|---|---|---|
| P01M | 129 | 8 | 26 | 95 | 0 | 0 | 71 |
| P01T | 189 | 24 | 32 | 133 | 0 | 0 | 71 |
| P01_GOLD | 626 | 227 | 201 | 198 | 0 | 0 | 82 |
| P02 | 464 | 0 | 196 | 268 | 0 | 0 | 66 |
| P03 | 263 | 0 | 0 | 251 | 12 | 0 | 57 |
| P04 | 3678 | 0 | 0 | 2986 | 692 | 0 | 46 |
| P05 | 422 | 15 | 30 | 365 | 12 | 0 | 51 |
| P06M | 14663 | 0 | 10 | 14583 | 70 | 0 | 46 |
| P06T | 35923 | 0 | 24 | 24117 | 11782 | 0 | 38 |
| P06 | 271 | 17 | 50 | 204 | 0 | 0 | 70 |
| P07 | 691 | 0 | 22 | 646 | 23 | 0 | 54 |
| P08 | 21900 | 0 | 0 | 18622 | 3278 | 0 | 43 |
| P09 | 307 | 4 | 12 | 290 | 1 | 0 | 53 |
| P10 | 2334 | 3 | 13 | 1570 | 748 | 0 | 41 |
| P11 | 1455 | 7 | 16 | 41 | 0 | 1391 | 23 |
| P12 | 15 | 0 | 0 | 15 | 0 | 0 | 54 |
| P13 | 97406 | 8 | 62 | 97319 | 17 | 0 | 43 |

### AP payability (confirmed channel + bill-to legal name and address + the buyer's reference rule + tax treatment known)

| package | rows | payable today | % | most common gap |
|---|---|---|---|---|
| P01M | 129 | 106 | 82.2% | the buyer's PO / reference rule (12) |
| P01T | 189 | 113 | 59.8% | bill-to legal name and address (62) |
| P01_GOLD | 626 | 474 | 75.7% | bill-to legal name and address (96) |
| P02 | 464 | 314 | 67.7% | the buyer's PO / reference rule (82) |
| P03 | 263 | 0 | 0.0% | a confirmed invoicing / AP or finance channel (263) |
| P04 | 3678 | 0 | 0.0% | a confirmed invoicing / AP or finance channel (3678) |
| P05 | 422 | 47 | 11.1% | a confirmed invoicing / AP or finance channel (336) |
| P06M | 14663 | 152 | 1.0% | a confirmed invoicing / AP or finance channel (14467) |
| P06T | 35923 | 227 | 0.6% | a confirmed invoicing / AP or finance channel (35365) |
| P06 | 271 | 47 | 17.3% | the buyer's PO / reference rule (115) |
| P07 | 691 | 7 | 1.0% | the buyer's PO / reference rule (269) |
| P08 | 21900 | 0 | 0.0% | a confirmed invoicing / AP or finance channel (21900) |
| P09 | 307 | 42 | 13.7% | a confirmed invoicing / AP or finance channel (255) |
| P10 | 2334 | 7 | 0.3% | a confirmed invoicing / AP or finance channel (2246) |
| P11 | 1455 | 14 | 1.0% | a confirmed invoicing / AP or finance channel (1391) |
| P12 | 15 | 4 | 26.7% | a confirmed invoicing / AP or finance channel (10) |
| P13 | 97406 | 39 | 0.0% | a confirmed invoicing / AP or finance channel (95708) |

### Pay on sight (an invoice generated from the row would clear AP: confirmed invoicing / AP or finance channel, bill-to legal name + address, vendor legal name + GST/HST number + remit-to address, tax treatment and currency known — published or labelled-derived; the buyer's reference rule is reported separately)

| package | rows | pay on sight | % | + reference rule not published | routed (general inbox only) | most common gap |
|---|---|---|---|---|---|---|
| P01M | 129 | 6 | 4.7% | 7 | 0 | the vendor's GST/HST number (BN9) (112) |
| P01T | 189 | 67 | 35.4% | 4 | 0 | the vendor's GST/HST number (BN9) (68) |
| P01_GOLD | 626 | 409 | 65.3% | 11 | 0 | the vendor's GST/HST number (BN9) (143) |
| P02 | 464 | 211 | 45.5% | 21 | 0 | the vendor's GST/HST number (BN9) (198) |
| P03 | 263 | 16 | 6.1% | 0 | 137 | an invoicing / AP or finance mailbox (only a purchasing / general inbo (88) |
| P04 | 3678 | 43 | 1.2% | 7 | 864 | an invoicing / AP or finance mailbox (only a purchasing / general inbo (2707) |
| P05 | 422 | 20 | 4.7% | 8 | 123 | an invoicing / AP or finance mailbox (only a purchasing / general inbo (205) |
| P06M | 14663 | 6 | 0.0% | 11 | 385 | an invoicing / AP or finance mailbox (only a purchasing / general inbo (14037) |
| P06T | 35923 | 218 | 0.6% | 16 | 8620 | an invoicing / AP or finance mailbox (only a purchasing / general inbo (26684) |
| P06 | 271 | 28 | 10.3% | 50 | 0 | the vendor's GST/HST number (BN9) (115) |
| P07 | 691 | 7 | 1.0% | 111 | 35 | the vendor's GST/HST number (BN9) (305) |
| P08 | 21900 | 3 | 0.0% | 14 | 4858 | an invoicing / AP or finance mailbox (only a purchasing / general inbo (16979) |
| P09 | 307 | 40 | 13.0% | 1 | 125 | an invoicing / AP or finance mailbox (only a purchasing / general inbo (121) |
| P10 | 2334 | 7 | 0.3% | 15 | 296 | an invoicing / AP or finance mailbox (only a purchasing / general inbo (1924) |
| P11 | 1455 | 9 | 0.6% | 4 | 0 | a confirmed invoicing / AP or finance channel (1373) |
| P12 | 15 | 3 | 20.0% | 0 | 6 | an invoicing / AP or finance mailbox (only a purchasing / general inbo (4) |
| P13 | 97406 | 11 | 0.0% | 549 | 26384 | an invoicing / AP or finance mailbox (only a purchasing / general inbo (69159) |
| **all** | 180736 | 1104 | 0.6% | 829 | 41833 | |

### What still blocks grade A (rows per missing element; a row counts under every element it lacks)

| package | rows not A | referee confirmation of the mailbox | an invoicing / AP mailbox (not finance / procurement / general) | a mailbox on the buyer's own domain | MX record for the mailbox domain | published bill-to legal name | invoice / billing address | published PO rule | published payment terms | clear the penalty |
|---|---|---|---|---|---|---|---|---|---|---|
| P01M | 121 | 0 | 0 | 0 | 67 | 8 | 0 | 101 | 105 | 4 |
| P01T | 165 | 0 | 0 | 0 | 88 | 53 | 28 | 134 | 149 | 7 |
| P01_GOLD | 399 | 0 | 0 | 0 | 11 | 77 | 31 | 194 | 228 | 60 |
| P02 | 464 | 0 | 464 | 0 | 38 | 56 | 19 | 351 | 279 | 22 |
| P03 | 263 | 0 | 263 | 0 | 15 | 41 | 25 | 125 | 136 | 26 |
| P04 | 3678 | 0 | 3678 | 0 | 1574 | 1352 | 1045 | 3477 | 3224 | 168 |
| P05 | 407 | 0 | 356 | 0 | 76 | 88 | 42 | 339 | 350 | 53 |
| P06M | 14663 | 0 | 14663 | 0 | 9320 | 1235 | 122 | 14457 | 14334 | 216 |
| P06T | 35923 | 0 | 35923 | 0 | 30909 | 22606 | 14912 | 35680 | 35324 | 881 |
| P06 | 254 | 0 | 0 | 0 | 116 | 71 | 54 | 177 | 212 | 9 |
| P07 | 691 | 0 | 691 | 0 | 434 | 276 | 129 | 644 | 645 | 13 |
| P08 | 21900 | 0 | 21900 | 0 | 16512 | 9988 | 4767 | 21614 | 21260 | 426 |
| P09 | 303 | 0 | 282 | 0 | 9 | 71 | 2 | 277 | 289 | 46 |
| P10 | 2331 | 0 | 2296 | 0 | 1138 | 1248 | 1085 | 2264 | 2225 | 118 |
| P11 | 1448 | 1391 | 1345 | 0 | 583 | 999 | 584 | 1381 | 1380 | 59 |
| P12 | 15 | 0 | 13 | 0 | 1 | 3 | 0 | 14 | 14 | 1 |
| P13 | 97398 | 0 | 97053 | 0 | 69510 | 51307 | 24 | 97099 | 96388 | 35 |

## Where the work is (largest gaps in rows still needed)

| field | package | now | target | rows needed |
|---|---|---|---|---|
| buyer_phone | P13 | 70.7% | 95% | 23714 |
| buyer_ap_cycle_published | P13 | 0.0% | 20% | 19453 |
| ap_system_hint | P13 | 0.5% | 20% | 19000 |
| buyer_bn_as_published | P13 | 12.2% | 30% | 17307 |
| buyer_esignature_preference | P13 | 0.1% | 15% | 14497 |
| buyer_tax_exempt_status | P13 | 0.2% | 15% | 14456 |
| buyer_payment_method_preference | P13 | 0.7% | 15% | 13925 |
| buyer_legal_name_as_published | P13 | 47.3% | 60% | 12345 |
| buyer_logo_url | P13 | 83.7% | 95% | 11010 |
| vendor_registered_address | P08 | 30.3% | 70% | 8693 |
| buyer_ap_cycle_published | P06T | 0.0% | 20% | 7175 |
| ap_system_hint | P06T | 0.7% | 20% | 6949 |
| buyer_phone | P08 | 67.8% | 95% | 5961 |
| buyer_esignature_preference | P06T | 0.2% | 15% | 5317 |
| buyer_tax_exempt_status | P06T | 0.2% | 15% | 5306 |
| buyer_payment_method_preference | P06T | 0.5% | 15% | 5205 |
| invoice_reference_hint | P08 | 1.3% | 25% | 5189 |
| buyer_legal_name_as_published | P08 | 54.4% | 75% | 4513 |
| vendor_emails | P08 | 54.8% | 75% | 4426 |
| buyer_ap_cycle_published | P08 | 0.1% | 20% | 4369 |
| vendor_phone | P08 | 65.4% | 85% | 4302 |
| buyer_bn_as_published | P08 | 15.4% | 35% | 4283 |
| vendor_bn9 | P08 | 30.5% | 50% | 4274 |
| ap_system_hint | P08 | 1.0% | 20% | 4152 |
| buyer_address | P08 | 78.2% | 95% | 3676 |
| buyer_esignature_preference | P08 | 0.5% | 15% | 3181 |
| buyer_tax_exempt_status | P08 | 0.5% | 15% | 3171 |
| buyer_payment_method_preference | P08 | 0.6% | 15% | 3147 |
| vendor_trading_name | P08 | 36.2% | 50% | 3025 |
| buyer_ap_cycle_published | P06M | 0.0% | 20% | 2927 |
| ap_system_hint | P06M | 0.8% | 20% | 2810 |
| average_contract_duration_days | P04 | 19.3% | 90% | 2600 |
| currency | P04 | 25.8% | 95% | 2546 |
| end_date | P04 | 24.1% | 90% | 2424 |
| commodity_codes | P04 | 21.8% | 85% | 2324 |
| ap_phone | P04 | 21.9% | 85% | 2322 |
| vendor_neq | P04 | 32.6% | 95% | 2297 |
| start_date | P04 | 28.2% | 90% | 2274 |
| award_or_notice_id | P04 | 23.9% | 85% | 2248 |
| contract_value | P04 | 25.1% | 85% | 2202 |

## 1. identifiers

### `invoice_reference_hint`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 129 | 89.1% | 89.1% | +0.0 | 50% | ✅ met |
| P01T | 189 | 93.7% | 93.7% | -0.1 | 50% | ✅ met |
| P01_GOLD | 626 | 92.2% | 94.4% | +0.0 | 95% | 🟡 3 pts to go |
| P02 | 464 | 74.4% | 75.9% | +0.4 | 95% | ❌ 21 pts to go |
| P03 | 263 | 81.4% | 84.4% | +0.0 | 95% | ❌ 14 pts to go |
| P04 | 3678 | 30.5% | 32.1% | +0.3 | 90% | ❌ 60 pts to go |
| P05 | 422 | 38.6% | 41.5% | +0.0 | 70% | ❌ 31 pts to go |
| P06M | 14663 | 91.8% | 91.8% | +0.0 | n/a | no target |
| P06T | 35923 | 98.6% | 98.6% | +0.0 | n/a | no target |
| P06 | 271 | 34.7% | 34.7% | +0.3 | 30% | ✅ met |
| P07 | 691 | 6.8% | 6.8% | -0.1 | 30% | ❌ 23 pts to go |
| P08 | 21900 | 1.3% | 1.3% | +0.0 | 25% | ❌ 24 pts to go |
| P09 | 307 | 99.0% | 99.7% | +0.0 | 100% | 🟡 1 pts to go |
| P10 | 2334 | 3.0% | 3.1% | -0.1 | 25% | ❌ 22 pts to go |
| P11 | 1455 | 46.9% | 47.8% | +0.0 | 60% | ❌ 13 pts to go |
| P12 | 15 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P13 | 97406 | 99.7% | 99.7% | +0.0 | 0% by design | — leave (by design) |

### `po_number_as_published`

> ceiling: a purchase-order number exists only where the buyer publishes PO-level data (Montréal, Laval, Toronto open data so far) or the record itself carries one; most sources publish awards, not POs — the target cannot be reached from public data for most buyers

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 129 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P01T | 189 | 0.0% | 0.0% | +0.0 | 10% | 🟡 10 pts to go |
| P01_GOLD | 626 | 6.1% | 6.1% | +0.0 | 50% | ❌ 44 pts to go |
| P02 | 464 | 6.2% | 6.2% | +0.0 | 50% | ❌ 44 pts to go |
| P03 | 263 | 1.5% | 1.5% | +0.0 | 40% | ❌ 38 pts to go |
| P04 | 3678 | 0.5% | 0.5% | +0.0 | 30% | ❌ 30 pts to go |
| P05 | 422 | 0.2% | 0.2% | +0.0 | 20% | ❌ 20 pts to go |
| P06M | 14663 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06T | 35923 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06 | 271 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P07 | 691 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P08 | 21900 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P09 | 307 | 0.7% | 0.7% | +0.0 | 50% | ❌ 49 pts to go |
| P10 | 2334 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P11 | 1455 | 0.3% | 0.3% | +0.0 | n/a | no target |
| P12 | 15 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P13 | 97406 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `contract_or_agreement_number`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 129 | 82.2% | 82.2% | +0.0 | n/a | no target |
| P01T | 189 | 74.1% | 74.1% | -0.4 | 50% | ✅ met |
| P01_GOLD | 626 | 66.8% | 66.8% | +0.0 | 85% | ❌ 18 pts to go |
| P02 | 464 | 65.1% | 65.1% | +0.3 | 90% | ❌ 25 pts to go |
| P03 | 263 | 59.7% | 59.7% | +0.0 | 85% | ❌ 25 pts to go |
| P04 | 3678 | 27.9% | 27.9% | +0.3 | 85% | ❌ 57 pts to go |
| P05 | 422 | 28.9% | 28.9% | +0.0 | 60% | ❌ 31 pts to go |
| P06M | 14663 | 91.5% | 91.5% | +0.0 | n/a | no target |
| P06T | 35923 | 98.5% | 98.5% | +0.1 | n/a | no target |
| P06 | 271 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P07 | 691 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P08 | 21900 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P09 | 307 | 96.1% | 96.1% | +0.0 | 100% | 🟡 4 pts to go |
| P10 | 2334 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P11 | 1455 | 43.3% | 43.3% | +0.0 | 60% | ❌ 17 pts to go |
| P12 | 15 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P13 | 97406 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `solicitation_or_tender_number`

> ceiling: SEAO's 'numero' is the organisation's own reference for the notice (SEAO data dictionary) and is reported here; sources that publish awards under a tender number only (bids&tenders, SaskTenders, BC) also carry it as the contract reference, labelled

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 129 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P01T | 189 | 0.0% | 0.0% | +0.0 | 30% | ❌ 30 pts to go |
| P01_GOLD | 626 | 50.8% | 50.8% | +0.0 | 80% | ❌ 29 pts to go |
| P02 | 464 | 57.1% | 57.1% | +0.2 | 60% | 🟡 3 pts to go |
| P03 | 263 | 50.2% | 50.2% | +0.0 | 80% | ❌ 30 pts to go |
| P04 | 3678 | 23.1% | 23.1% | +0.2 | 50% | ❌ 27 pts to go |
| P05 | 422 | 11.4% | 11.4% | +0.0 | 40% | ❌ 29 pts to go |
| P06M | 14663 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06T | 35923 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06 | 271 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P07 | 691 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P08 | 21900 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P09 | 307 | 83.4% | 83.4% | +0.0 | 50% | ✅ met |
| P10 | 2334 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P11 | 1455 | 5.6% | 5.6% | +0.0 | 40% | ❌ 34 pts to go |
| P12 | 15 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P13 | 97406 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `award_or_notice_id`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 129 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P01T | 189 | 0.5% | 0.5% | +0.0 | n/a | no target |
| P01_GOLD | 626 | 60.4% | 60.4% | +0.0 | 85% | ❌ 25 pts to go |
| P02 | 464 | 56.5% | 56.5% | +0.3 | 90% | ❌ 34 pts to go |
| P03 | 263 | 58.6% | 58.6% | +0.0 | 85% | ❌ 26 pts to go |
| P04 | 3678 | 23.9% | 23.9% | +0.3 | 85% | ❌ 61 pts to go |
| P05 | 422 | 19.7% | 19.7% | +0.0 | 50% | ❌ 30 pts to go |
| P06M | 14663 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06T | 35923 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06 | 271 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P07 | 691 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P08 | 21900 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P09 | 307 | 97.1% | 97.1% | +0.0 | 100% | 🟡 3 pts to go |
| P10 | 2334 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P11 | 1455 | 6.0% | 6.0% | +0.0 | 60% | ❌ 54 pts to go |
| P12 | 15 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P13 | 97406 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `buyer_vendor_id`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 129 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P01T | 189 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P01_GOLD | 626 | 12.9% | 12.9% | +0.0 | 60% | ❌ 47 pts to go |
| P02 | 464 | 6.0% | 6.0% | +0.0 | 50% | ❌ 44 pts to go |
| P03 | 263 | 8.4% | 8.4% | +0.0 | 50% | ❌ 42 pts to go |
| P04 | 3678 | 1.8% | 1.8% | +0.0 | 40% | ❌ 38 pts to go |
| P05 | 422 | 0.7% | 0.7% | +0.0 | 20% | ❌ 19 pts to go |
| P06M | 14663 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06T | 35923 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06 | 271 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P07 | 691 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P08 | 21900 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P09 | 307 | 3.3% | 3.3% | +0.0 | 50% | ❌ 47 pts to go |
| P10 | 2334 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P11 | 1455 | 0.9% | 0.9% | +0.0 | n/a | no target |
| P12 | 15 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P13 | 97406 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `commodity_codes`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 129 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P01T | 189 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P01_GOLD | 626 | 34.8% | 34.8% | +0.0 | 80% | ❌ 45 pts to go |
| P02 | 464 | 52.2% | 52.2% | +0.3 | 90% | ❌ 38 pts to go |
| P03 | 263 | 32.7% | 32.7% | +0.0 | 80% | ❌ 47 pts to go |
| P04 | 3678 | 21.8% | 21.8% | +0.2 | 85% | ❌ 63 pts to go |
| P05 | 422 | 5.5% | 5.5% | +0.0 | 50% | ❌ 44 pts to go |
| P06M | 14663 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06T | 35923 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06 | 271 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P07 | 691 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P08 | 21900 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P09 | 307 | 74.3% | 74.3% | +0.0 | 95% | ❌ 21 pts to go |
| P10 | 2334 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P11 | 1455 | 4.3% | 4.3% | +0.0 | 50% | ❌ 46 pts to go |
| P12 | 15 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P13 | 97406 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `buyer_org_codes`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 129 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P01T | 189 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P01_GOLD | 626 | 8.5% | 8.5% | +0.0 | 50% | ❌ 42 pts to go |
| P02 | 464 | 6.2% | 6.2% | +0.0 | 50% | ❌ 44 pts to go |
| P03 | 263 | 1.9% | 1.9% | +0.0 | 30% | ❌ 28 pts to go |
| P04 | 3678 | 0.5% | 0.5% | +0.0 | 30% | ❌ 30 pts to go |
| P05 | 422 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06M | 14663 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06T | 35923 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06 | 271 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P07 | 691 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P08 | 21900 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P09 | 307 | 0.3% | 0.3% | +0.0 | n/a | no target |
| P10 | 2334 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P11 | 1455 | 0.3% | 0.3% | +0.0 | n/a | no target |
| P12 | 15 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P13 | 97406 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `records_with_this_vendor`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 129 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P01T | 189 | 100.0% | 100.0% | +0.0 | 60% | ✅ met |
| P01_GOLD | 626 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P02 | 464 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P03 | 263 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P04 | 3678 | 100.0% | 100.0% | +0.0 | 95% | ✅ met |
| P05 | 422 | 100.0% | 100.0% | +0.0 | 70% | ✅ met |
| P06M | 14663 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P06T | 35923 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P06 | 271 | 100.0% | 100.0% | +0.0 | 50% | ✅ met |
| P07 | 691 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P08 | 21900 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P09 | 307 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P10 | 2334 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P11 | 1455 | 100.0% | 100.0% | +0.0 | 70% | ✅ met |
| P12 | 15 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P13 | 97406 | 0.0% | 0.0% | +0.0 | n/a | no target |

## 2. vendor

### `vendor_bn9`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 129 | 11.6% | 11.6% | +0.0 | 70% | ❌ 58 pts to go |
| P01T | 189 | 51.3% | 51.3% | +0.8 | 60% | 🟡 9 pts to go |
| P01_GOLD | 626 | 74.8% | 74.8% | +0.0 | 90% | ❌ 15 pts to go |
| P02 | 464 | 53.9% | 53.9% | +0.3 | 85% | ❌ 31 pts to go |
| P03 | 263 | 69.6% | 69.6% | +0.0 | 90% | ❌ 20 pts to go |
| P04 | 3678 | 35.1% | 35.1% | +0.1 | 75% | ❌ 40 pts to go |
| P05 | 422 | 54.7% | 54.7% | +0.0 | 50% | ✅ met |
| P06M | 14663 | 3.2% | 3.2% | +0.0 | n/a | no target |
| P06T | 35923 | 47.6% | 47.6% | +0.3 | n/a | no target |
| P06 | 271 | 43.9% | 43.9% | -0.1 | 40% | ✅ met |
| P07 | 691 | 33.0% | 33.0% | +0.0 | 50% | ❌ 17 pts to go |
| P08 | 21900 | 30.5% | 30.5% | +0.0 | 50% | ❌ 20 pts to go |
| P09 | 307 | 58.3% | 58.3% | +0.0 | 80% | ❌ 22 pts to go |
| P10 | 2334 | 34.5% | 34.5% | +0.0 | 40% | 🟡 6 pts to go |
| P11 | 1455 | 46.9% | 46.9% | +0.0 | 60% | ❌ 13 pts to go |
| P12 | 15 | 60.0% | 60.0% | +0.0 | 85% | ❌ 25 pts to go |
| P13 | 97406 | 30.5% | 30.5% | -1.2 | 0% by design | — leave (by design) |

### `vendor_registered_address`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 129 | 59.7% | 59.7% | +0.0 | n/a | no target |
| P01T | 189 | 51.9% | 51.9% | +0.9 | n/a | no target |
| P01_GOLD | 626 | 72.7% | 72.7% | +0.0 | 95% | ❌ 22 pts to go |
| P02 | 464 | 74.1% | 74.1% | +0.3 | 95% | ❌ 21 pts to go |
| P03 | 263 | 71.9% | 71.9% | +0.0 | 95% | ❌ 23 pts to go |
| P04 | 3678 | 49.7% | 49.7% | +0.5 | 95% | ❌ 45 pts to go |
| P05 | 422 | 58.3% | 58.3% | +0.0 | 70% | ❌ 12 pts to go |
| P06M | 14663 | 46.0% | 46.0% | +0.0 | n/a | no target |
| P06T | 35923 | 56.3% | 56.3% | +0.1 | n/a | no target |
| P06 | 271 | 41.3% | 41.3% | +0.3 | 80% | ❌ 39 pts to go |
| P07 | 691 | 31.8% | 31.8% | -0.1 | 70% | ❌ 38 pts to go |
| P08 | 21900 | 30.3% | 30.3% | +0.0 | 70% | ❌ 40 pts to go |
| P09 | 307 | 86.6% | 86.6% | +0.0 | 100% | ❌ 13 pts to go |
| P10 | 2334 | 35.6% | 35.6% | +0.1 | 70% | ❌ 34 pts to go |
| P11 | 1455 | 52.5% | 52.5% | +0.0 | 75% | ❌ 22 pts to go |
| P12 | 15 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P13 | 97406 | 25.8% | 25.8% | -1.1 | n/a | no target |

### `vendor_trading_name`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 129 | 17.1% | 17.1% | +0.0 | n/a | no target |
| P01T | 189 | 54.5% | 54.5% | +0.9 | n/a | no target |
| P01_GOLD | 626 | 49.8% | 49.8% | +0.0 | 60% | ❌ 10 pts to go |
| P02 | 464 | 56.2% | 56.2% | +0.0 | 60% | 🟡 4 pts to go |
| P03 | 263 | 55.1% | 55.1% | +0.0 | 60% | 🟡 5 pts to go |
| P04 | 3678 | 42.3% | 42.3% | +0.2 | 55% | ❌ 13 pts to go |
| P05 | 422 | 24.6% | 24.6% | +0.0 | 50% | ❌ 25 pts to go |
| P06M | 14663 | 6.8% | 6.8% | +0.0 | n/a | no target |
| P06T | 35923 | 51.2% | 51.2% | +0.3 | n/a | no target |
| P06 | 271 | 47.6% | 47.6% | +0.0 | n/a | no target |
| P07 | 691 | 41.1% | 41.1% | +0.2 | 55% | ❌ 14 pts to go |
| P08 | 21900 | 36.2% | 36.2% | +0.0 | 50% | ❌ 14 pts to go |
| P09 | 307 | 72.3% | 72.3% | +0.0 | 70% | ✅ met |
| P10 | 2334 | 46.9% | 46.9% | +0.1 | 55% | 🟡 8 pts to go |
| P11 | 1455 | 52.2% | 52.2% | +0.0 | 50% | ✅ met |
| P12 | 15 | 86.7% | 86.7% | +0.0 | n/a | no target |
| P13 | 97406 | 3.3% | 3.3% | -0.1 | n/a | no target |

### `vendor_phone`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 129 | 50.4% | 50.4% | +0.0 | n/a | no target |
| P01T | 189 | 74.1% | 74.1% | -0.4 | n/a | no target |
| P01_GOLD | 626 | 50.5% | 50.5% | +0.0 | 70% | ❌ 20 pts to go |
| P02 | 464 | 58.2% | 58.2% | +0.0 | 70% | ❌ 12 pts to go |
| P03 | 263 | 51.3% | 51.3% | +0.0 | 70% | ❌ 19 pts to go |
| P04 | 3678 | 54.0% | 54.0% | -0.1 | 65% | ❌ 11 pts to go |
| P05 | 422 | 28.4% | 28.4% | +0.0 | 60% | ❌ 32 pts to go |
| P06M | 14663 | 36.6% | 36.6% | +0.0 | n/a | no target |
| P06T | 35923 | 79.9% | 79.9% | -0.1 | n/a | no target |
| P06 | 271 | 69.0% | 69.0% | +0.1 | 40% | ✅ met |
| P07 | 691 | 64.7% | 64.7% | -0.2 | 85% | ❌ 20 pts to go |
| P08 | 21900 | 65.4% | 65.4% | +0.1 | 85% | ❌ 20 pts to go |
| P09 | 307 | 59.3% | 59.3% | +0.0 | 85% | ❌ 26 pts to go |
| P10 | 2334 | 64.0% | 64.0% | +0.5 | 85% | ❌ 21 pts to go |
| P11 | 1455 | 61.9% | 61.9% | +0.0 | 75% | ❌ 13 pts to go |
| P12 | 15 | 26.7% | 26.7% | +0.0 | n/a | no target |
| P13 | 97406 | 91.4% | 91.4% | +0.2 | 60% | ✅ met |

### `vendor_website`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 129 | 56.6% | 56.6% | +0.0 | n/a | no target |
| P01T | 189 | 97.4% | 97.4% | +0.0 | n/a | no target |
| P01_GOLD | 626 | 79.6% | 79.6% | +0.0 | 90% | ❌ 10 pts to go |
| P02 | 464 | 83.8% | 83.8% | -0.1 | 90% | 🟡 6 pts to go |
| P03 | 263 | 87.8% | 87.8% | +0.0 | 90% | 🟡 2 pts to go |
| P04 | 3678 | 84.2% | 84.2% | -0.2 | 85% | 🟡 1 pts to go |
| P05 | 422 | 44.8% | 44.8% | +0.0 | 70% | ❌ 25 pts to go |
| P06M | 14663 | 43.5% | 43.5% | -0.1 | n/a | no target |
| P06T | 35923 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P06 | 271 | 99.3% | 99.3% | +0.0 | 50% | ✅ met |
| P07 | 691 | 99.9% | 99.9% | +0.0 | 100% | 🟡 0 pts to go |
| P08 | 21900 | 99.8% | 99.8% | +0.0 | 100% | 🟡 0 pts to go |
| P09 | 307 | 79.8% | 79.8% | +0.0 | 100% | ❌ 20 pts to go |
| P10 | 2334 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P11 | 1455 | 97.3% | 97.3% | +0.0 | 100% | 🟡 3 pts to go |
| P12 | 15 | 53.3% | 53.3% | +0.0 | n/a | no target |
| P13 | 97406 | 100.0% | 100.0% | +0.0 | n/a | no target |

### `vendor_emails`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 129 | 15.5% | 15.5% | +0.0 | n/a | no target |
| P01T | 189 | 65.1% | 65.1% | +0.0 | n/a | no target |
| P01_GOLD | 626 | 43.5% | 43.5% | +0.0 | 70% | ❌ 26 pts to go |
| P02 | 464 | 48.7% | 48.7% | +0.0 | 75% | ❌ 26 pts to go |
| P03 | 263 | 43.3% | 43.3% | +0.0 | 75% | ❌ 32 pts to go |
| P04 | 3678 | 38.7% | 38.7% | +0.0 | 70% | ❌ 31 pts to go |
| P05 | 422 | 22.0% | 22.0% | +0.0 | 55% | ❌ 33 pts to go |
| P06M | 14663 | 4.8% | 4.8% | +0.0 | n/a | no target |
| P06T | 35923 | 62.4% | 62.4% | +0.3 | n/a | no target |
| P06 | 271 | 47.2% | 47.2% | +0.3 | n/a | no target |
| P07 | 691 | 49.9% | 49.9% | -0.1 | 70% | ❌ 20 pts to go |
| P08 | 21900 | 54.8% | 54.8% | +0.0 | 75% | ❌ 20 pts to go |
| P09 | 307 | 49.2% | 49.2% | +0.0 | 85% | ❌ 36 pts to go |
| P10 | 2334 | 43.7% | 43.7% | +0.1 | 80% | ❌ 36 pts to go |
| P11 | 1455 | 54.3% | 54.3% | +0.0 | 70% | ❌ 16 pts to go |
| P12 | 15 | 40.0% | 40.0% | +0.0 | n/a | no target |
| P13 | 97406 | 5.0% | 5.0% | -0.2 | n/a | no target |

### `vendor_logo_url`

> ceiling: needs the vendor's website first; sites that block automated readers (robots.txt / 403) are never read

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 129 | 56.6% | 56.6% | +0.0 | n/a | no target |
| P01T | 189 | 94.7% | 94.7% | -0.1 | n/a | no target |
| P01_GOLD | 626 | 73.8% | 73.8% | +0.0 | 90% | ❌ 16 pts to go |
| P02 | 464 | 78.9% | 78.9% | -0.1 | 90% | ❌ 11 pts to go |
| P03 | 263 | 83.3% | 83.3% | +0.0 | 90% | 🟡 7 pts to go |
| P04 | 3678 | 76.4% | 76.4% | +0.0 | 85% | 🟡 9 pts to go |
| P05 | 422 | 43.1% | 43.1% | +0.0 | 75% | ❌ 32 pts to go |
| P06M | 14663 | 43.3% | 43.3% | +0.0 | n/a | no target |
| P06T | 35923 | 96.7% | 96.7% | +0.0 | n/a | no target |
| P06 | 271 | 90.4% | 90.4% | -0.1 | n/a | no target |
| P07 | 691 | 92.5% | 92.5% | +0.0 | 100% | 🟡 8 pts to go |
| P08 | 21900 | 90.8% | 90.8% | +0.0 | 100% | 🟡 9 pts to go |
| P09 | 307 | 66.1% | 66.1% | +0.0 | n/a | no target |
| P10 | 2334 | 86.9% | 86.9% | +0.1 | 100% | ❌ 13 pts to go |
| P11 | 1455 | 87.7% | 87.7% | +0.0 | n/a | no target |
| P12 | 15 | 46.7% | 46.7% | +0.0 | n/a | no target |
| P13 | 97406 | 66.4% | 66.4% | +1.2 | n/a | no target |

### `vendor_neq`

> ceiling: only Québec-registered vendors have an NEQ; the share of QC vendors is reported next to the rate

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 129 | 46.5% | 46.5% | +0.0 | n/a | no target · QC vendors: 49 rows, 100.0% filled |
| P01T | 189 | 9.5% | 9.5% | +0.1 | n/a | no target · QC vendors: 4 rows, 75.0% filled |
| P01_GOLD | 626 | 43.8% | 43.8% | +0.0 | 95% | ❌ 51 pts to go · QC vendors: 54 rows, 98.1% filled |
| P02 | 464 | 55.8% | 55.8% | +0.2 | 95% | ❌ 39 pts to go · QC vendors: 113 rows, 100.0% filled |
| P03 | 263 | 46.0% | 46.0% | +0.0 | 95% | ❌ 49 pts to go · QC vendors: 21 rows, 100.0% filled |
| P04 | 3678 | 32.6% | 32.6% | +0.4 | 95% | ❌ 62 pts to go · QC vendors: 617 rows, 98.1% filled |
| P05 | 422 | 14.0% | 14.0% | +0.0 | n/a | no target · QC vendors: 34 rows, 94.1% filled |
| P06M | 14663 | 42.8% | 42.8% | +0.0 | n/a | no target · QC vendors: 5559 rows, 99.8% filled |
| P06T | 35923 | 5.4% | 5.4% | +0.1 | n/a | no target · QC vendors: 1990 rows, 77.2% filled |
| P06 | 271 | 8.5% | 8.5% | +0.1 | n/a | no target · QC vendors: 16 rows, 68.8% filled |
| P07 | 691 | 6.4% | 6.4% | +0.1 | n/a | no target · QC vendors: 39 rows, 76.9% filled |
| P08 | 21900 | 6.6% | 6.6% | +0.0 | n/a | no target · QC vendors: 1280 rows, 92.9% filled |
| P09 | 307 | 76.9% | 76.9% | +0.0 | 95% | ❌ 18 pts to go · QC vendors: 112 rows, 100.0% filled |
| P10 | 2334 | 15.9% | 15.9% | +0.3 | n/a | no target · QC vendors: 228 rows, 89.9% filled |
| P11 | 1455 | 14.8% | 14.8% | +0.0 | n/a | no target · QC vendors: 153 rows, 91.5% filled |
| P12 | 15 | 73.3% | 73.3% | +0.0 | n/a | no target · QC vendors: 3 rows, 100.0% filled |
| P13 | 97406 | 25.2% | 25.2% | -1.0 | n/a | no target · QC vendors: 24574 rows, 100.0% filled |

### `vendor_years_in_business`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 129 | 58.9% | 58.9% | +0.0 | n/a | no target · vendors with a registry record: 76 rows, 100.0% filled |
| P01T | 189 | 51.9% | 51.9% | +0.9 | n/a | no target · vendors with a registry record: 98 rows, 100.0% filled |
| P01_GOLD | 626 | 81.5% | 81.5% | +0.0 | 100% | ❌ 18 pts to go · vendors with a registry record: 510 rows, 100.0% filled |
| P02 | 464 | 77.8% | 77.8% | +0.3 | 100% | ❌ 22 pts to go · vendors with a registry record: 361 rows, 100.0% filled |
| P03 | 263 | 81.0% | 81.0% | +0.0 | 100% | ❌ 19 pts to go · vendors with a registry record: 213 rows, 100.0% filled |
| P04 | 3678 | 50.2% | 50.2% | +0.5 | 100% | ❌ 50 pts to go · vendors with a registry record: 1845 rows, 100.0% filled |
| P05 | 422 | 63.3% | 63.3% | +0.0 | n/a | no target · vendors with a registry record: 267 rows, 100.0% filled |
| P06M | 14663 | 45.8% | 45.8% | -0.1 | n/a | no target · vendors with a registry record: 6722 rows, 100.0% filled |
| P06T | 35923 | 56.4% | 56.4% | +0.2 | n/a | no target · vendors with a registry record: 20263 rows, 100.0% filled |
| P06 | 271 | 41.7% | 41.7% | +0.3 | n/a | no target · vendors with a registry record: 113 rows, 100.0% filled |
| P07 | 691 | 32.4% | 32.4% | +0.1 | n/a | no target · vendors with a registry record: 224 rows, 100.0% filled |
| P08 | 21900 | 30.5% | 30.5% | +0.1 | n/a | no target · vendors with a registry record: 6671 rows, 100.0% filled |
| P09 | 307 | 90.6% | 90.6% | +0.0 | n/a | no target · vendors with a registry record: 278 rows, 100.0% filled |
| P10 | 2334 | 36.4% | 36.4% | +0.2 | n/a | no target · vendors with a registry record: 849 rows, 100.0% filled |
| P11 | 1455 | 53.6% | 53.6% | +0.0 | n/a | no target · vendors with a registry record: 780 rows, 100.0% filled |
| P12 | 15 | 100.0% | 100.0% | +0.0 | n/a | no target · vendors with a registry record: 15 rows, 100.0% filled |
| P13 | 97406 | 25.8% | 25.8% | -1.1 | n/a | no target · vendors with a registry record: 25121 rows, 100.0% filled |

## 3. buyer

### `buyer_legal_name_as_published`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 129 | 93.8% | 93.8% | +0.0 | 90% | ✅ met |
| P01T | 189 | 72.0% | 72.0% | -0.4 | 90% | ❌ 18 pts to go |
| P01_GOLD | 626 | 87.7% | 87.7% | +0.0 | 95% | 🟡 7 pts to go |
| P02 | 464 | 87.9% | 87.9% | +0.1 | 95% | 🟡 7 pts to go |
| P03 | 263 | 84.4% | 84.4% | +0.0 | 85% | 🟡 1 pts to go |
| P04 | 3678 | 63.2% | 63.2% | +0.2 | 90% | ❌ 27 pts to go |
| P05 | 422 | 79.1% | 79.1% | +0.0 | 75% | ✅ met |
| P06M | 14663 | 91.6% | 91.6% | +0.0 | n/a | no target |
| P06T | 35923 | 37.1% | 37.1% | -0.2 | n/a | no target |
| P06 | 271 | 73.8% | 73.8% | +0.2 | 80% | 🟡 6 pts to go |
| P07 | 691 | 60.1% | 60.2% | +0.3 | 80% | ❌ 20 pts to go |
| P08 | 21900 | 54.4% | 54.4% | +0.0 | 75% | ❌ 21 pts to go |
| P09 | 307 | 76.9% | 76.9% | +0.0 | 95% | ❌ 18 pts to go |
| P10 | 2334 | 46.5% | 46.6% | -0.2 | 70% | ❌ 24 pts to go |
| P11 | 1455 | 31.3% | 31.3% | +0.0 | 65% | ❌ 34 pts to go |
| P12 | 15 | 80.0% | 80.0% | +0.0 | 80% | ✅ met |
| P13 | 97406 | 47.3% | 47.3% | -0.2 | 60% | ❌ 13 pts to go |

### `buyer_bn_as_published`

> ceiling: a buyer's BN is public only where the buyer prints it or a public dataset carries it (CRA charities, federal grants & contributions recipients, business registries for corporations); municipalities rarely publish theirs

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 129 | 20.2% | 20.2% | +0.0 | 50% | ❌ 30 pts to go |
| P01T | 189 | 15.9% | 15.9% | -0.2 | n/a | no target |
| P01_GOLD | 626 | 19.5% | 19.5% | +0.0 | 40% | ❌ 20 pts to go |
| P02 | 464 | 19.0% | 19.0% | -0.1 | 40% | ❌ 21 pts to go |
| P03 | 263 | 21.3% | 21.3% | +0.0 | 40% | ❌ 19 pts to go |
| P04 | 3678 | 15.1% | 15.1% | -0.1 | 40% | ❌ 25 pts to go |
| P05 | 422 | 17.5% | 17.5% | +0.0 | 25% | 🟡 8 pts to go |
| P06M | 14663 | 11.6% | 11.6% | +0.0 | n/a | no target |
| P06T | 35923 | 6.8% | 6.8% | -0.1 | n/a | no target |
| P06 | 271 | 12.5% | 12.5% | -0.3 | 35% | ❌ 22 pts to go |
| P07 | 691 | 14.0% | 14.0% | -0.1 | 35% | ❌ 21 pts to go |
| P08 | 21900 | 15.4% | 15.4% | +0.0 | 35% | ❌ 20 pts to go |
| P09 | 307 | 16.3% | 16.3% | +0.0 | n/a | no target |
| P10 | 2334 | 6.6% | 6.6% | -0.1 | 30% | ❌ 23 pts to go |
| P11 | 1455 | 7.4% | 7.4% | +0.0 | n/a | no target |
| P12 | 15 | 6.7% | 6.7% | +0.0 | n/a | no target |
| P13 | 97406 | 12.2% | 12.2% | -0.1 | 30% | ❌ 18 pts to go |

### `buyer_address`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 129 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P01T | 189 | 84.1% | 84.1% | -0.3 | 100% | ❌ 16 pts to go |
| P01_GOLD | 626 | 90.7% | 90.7% | +0.0 | 100% | 🟡 9 pts to go |
| P02 | 464 | 95.5% | 95.5% | +0.0 | 100% | 🟡 4 pts to go |
| P03 | 263 | 89.4% | 89.4% | +0.0 | 100% | ❌ 11 pts to go |
| P04 | 3678 | 71.1% | 71.1% | -0.3 | 100% | ❌ 29 pts to go |
| P05 | 422 | 89.3% | 89.3% | +0.0 | 100% | ❌ 11 pts to go |
| P06M | 14663 | 99.2% | 99.2% | +0.0 | n/a | no target |
| P06T | 35923 | 58.5% | 58.5% | -0.8 | n/a | no target |
| P06 | 271 | 78.6% | 78.6% | -0.2 | 95% | ❌ 16 pts to go |
| P07 | 691 | 81.0% | 81.0% | -0.2 | 95% | ❌ 14 pts to go |
| P08 | 21900 | 78.2% | 78.2% | -0.1 | 95% | ❌ 17 pts to go |
| P09 | 307 | 96.1% | 96.1% | +0.0 | 100% | 🟡 4 pts to go |
| P10 | 2334 | 53.4% | 53.5% | -1.0 | 95% | ❌ 42 pts to go |
| P11 | 1455 | 49.4% | 49.4% | +0.0 | 80% | ❌ 31 pts to go |
| P12 | 15 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P13 | 97406 | 100.0% | 100.0% | +0.0 | 95% | ✅ met |

### `buyer_phone`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 129 | 86.0% | 86.0% | +0.0 | n/a | no target |
| P01T | 189 | 68.3% | 68.3% | +0.1 | n/a | no target |
| P01_GOLD | 626 | 73.0% | 73.0% | +0.0 | 90% | ❌ 17 pts to go |
| P02 | 464 | 78.2% | 78.2% | +0.3 | 95% | ❌ 17 pts to go |
| P03 | 263 | 74.9% | 74.9% | +0.0 | 95% | ❌ 20 pts to go |
| P04 | 3678 | 68.8% | 68.8% | -0.1 | 95% | ❌ 26 pts to go |
| P05 | 422 | 73.5% | 73.5% | +0.0 | 90% | ❌ 16 pts to go |
| P06M | 14663 | 86.8% | 86.8% | -0.1 | n/a | no target |
| P06T | 35923 | 56.8% | 56.8% | -0.4 | n/a | no target |
| P06 | 271 | 69.0% | 69.0% | +0.5 | 95% | ❌ 26 pts to go |
| P07 | 691 | 65.3% | 65.3% | +0.5 | 90% | ❌ 25 pts to go |
| P08 | 21900 | 67.8% | 67.8% | +0.0 | 95% | ❌ 27 pts to go |
| P09 | 307 | 87.0% | 87.0% | +0.0 | 100% | ❌ 13 pts to go |
| P10 | 2334 | 54.9% | 54.9% | -0.4 | 95% | ❌ 40 pts to go |
| P11 | 1455 | 28.9% | 28.9% | +0.0 | 75% | ❌ 46 pts to go |
| P12 | 15 | 93.3% | 93.3% | +0.0 | n/a | no target |
| P13 | 97406 | 70.7% | 70.7% | -0.1 | 95% | ❌ 24 pts to go |

### `buyer_logo_url`

> ceiling: sites that block automated readers (robots.txt / 403) are never read; an og:image that looks like a photo is labelled

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 129 | 87.6% | 87.6% | +0.0 | n/a | no target |
| P01T | 189 | 83.1% | 83.1% | -0.2 | 95% | ❌ 12 pts to go |
| P01_GOLD | 626 | 84.8% | 84.8% | +0.0 | 90% | 🟡 5 pts to go |
| P02 | 464 | 90.5% | 90.5% | -0.1 | 95% | 🟡 4 pts to go |
| P03 | 263 | 85.6% | 85.6% | +0.0 | 95% | 🟡 9 pts to go |
| P04 | 3678 | 89.1% | 89.1% | -0.1 | 90% | 🟡 1 pts to go |
| P05 | 422 | 93.1% | 93.1% | +0.0 | 95% | 🟡 2 pts to go |
| P06M | 14663 | 93.2% | 93.2% | +0.0 | n/a | no target |
| P06T | 35923 | 74.5% | 74.5% | -0.4 | n/a | no target |
| P06 | 271 | 92.6% | 92.6% | +0.3 | 100% | 🟡 7 pts to go |
| P07 | 691 | 92.2% | 92.2% | +0.0 | 100% | 🟡 8 pts to go |
| P08 | 21900 | 92.3% | 92.3% | +0.0 | 100% | 🟡 8 pts to go |
| P09 | 307 | 73.0% | 73.0% | +0.0 | n/a | no target |
| P10 | 2334 | 91.4% | 91.4% | +0.1 | 100% | 🟡 9 pts to go |
| P11 | 1455 | 41.9% | 41.9% | +0.0 | 80% | ❌ 38 pts to go |
| P12 | 15 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P13 | 97406 | 83.7% | 83.7% | +0.0 | 95% | ❌ 11 pts to go |

## 4. AP

### `ap_contact_name_as_published`

> ceiling: owner 2026-11-08: the AP contact person the organisation itself names on its AP / finance page is allowed (name + role phrase, quoted); mailboxes stay organisational; many bodies publish no AP person

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 129 | 3.1% | 3.1% | +0.0 | n/a | no target |
| P01T | 189 | 9.5% | 9.5% | +0.1 | n/a | no target |
| P01_GOLD | 626 | 14.2% | 14.2% | +0.0 | 25% | ❌ 11 pts to go |
| P02 | 464 | 25.2% | 25.2% | -0.1 | 40% | ❌ 15 pts to go |
| P03 | 263 | 9.1% | 9.1% | +0.0 | 20% | ❌ 11 pts to go |
| P04 | 3678 | 3.5% | 3.5% | +0.0 | 20% | ❌ 16 pts to go |
| P05 | 422 | 3.3% | 3.3% | +0.0 | 15% | ❌ 12 pts to go |
| P06M | 14663 | 0.3% | 0.3% | +0.0 | n/a | no target |
| P06T | 35923 | 0.3% | 0.3% | +0.0 | n/a | no target |
| P06 | 271 | 5.2% | 5.2% | +0.1 | n/a | no target |
| P07 | 691 | 8.5% | 8.5% | +0.0 | n/a | no target |
| P08 | 21900 | 0.3% | 0.3% | +0.0 | n/a | no target |
| P09 | 307 | 7.8% | 7.8% | +0.0 | n/a | no target |
| P10 | 2334 | 0.9% | 0.9% | +0.1 | n/a | no target |
| P11 | 1455 | 1.0% | 1.0% | +0.0 | n/a | no target |
| P12 | 15 | 6.7% | 6.7% | +0.0 | n/a | no target |
| P13 | 97406 | 0.3% | 0.3% | +0.0 | n/a | no target |

### `ap_phone`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 129 | 18.6% | 18.6% | +0.0 | n/a | no target |
| P01T | 189 | 22.8% | 22.8% | +0.4 | 70% | ❌ 47 pts to go |
| P01_GOLD | 626 | 43.5% | 43.5% | +0.0 | 80% | ❌ 36 pts to go |
| P02 | 464 | 57.5% | 57.5% | +0.2 | 90% | ❌ 32 pts to go |
| P03 | 263 | 18.6% | 18.6% | +0.0 | 60% | ❌ 41 pts to go |
| P04 | 3678 | 21.9% | 21.9% | +0.3 | 85% | ❌ 63 pts to go |
| P05 | 422 | 11.6% | 11.6% | +0.0 | 50% | ❌ 38 pts to go |
| P06M | 14663 | 0.6% | 0.6% | +0.0 | n/a | no target |
| P06T | 35923 | 0.7% | 0.7% | +0.0 | n/a | no target |
| P06 | 271 | 15.5% | 15.5% | +0.1 | n/a | no target |
| P07 | 691 | 10.3% | 10.3% | -0.2 | n/a | no target |
| P08 | 21900 | 0.6% | 0.6% | +0.0 | n/a | no target |
| P09 | 307 | 77.9% | 77.9% | +0.0 | 95% | ❌ 17 pts to go |
| P10 | 2334 | 1.5% | 1.5% | -0.2 | n/a | no target |
| P11 | 1455 | 16.7% | 16.7% | +0.0 | n/a | no target |
| P12 | 15 | 26.7% | 26.7% | +0.0 | n/a | no target |
| P13 | 97406 | 0.5% | 0.5% | +0.0 | n/a | no target |

### `invoice_mailing_address`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 129 | 6.2% | 6.2% | +0.0 | n/a | no target |
| P01T | 189 | 10.1% | 10.1% | -0.3 | n/a | no target |
| P01_GOLD | 626 | 34.0% | 34.0% | +0.0 | 70% | ❌ 36 pts to go |
| P02 | 464 | 39.2% | 39.2% | +0.1 | 75% | ❌ 36 pts to go |
| P03 | 263 | 18.6% | 18.6% | +0.0 | 55% | ❌ 36 pts to go |
| P04 | 3678 | 21.9% | 21.9% | +0.3 | 75% | ❌ 53 pts to go |
| P05 | 422 | 10.7% | 10.7% | +0.0 | 50% | ❌ 39 pts to go |
| P06M | 14663 | 0.2% | 0.2% | +0.0 | n/a | no target |
| P06T | 35923 | 0.4% | 0.4% | +0.0 | n/a | no target |
| P06 | 271 | 5.9% | 5.9% | +0.0 | n/a | no target |
| P07 | 691 | 5.1% | 5.1% | -0.1 | n/a | no target |
| P08 | 21900 | 0.2% | 0.2% | +0.0 | n/a | no target |
| P09 | 307 | 75.2% | 75.2% | +0.0 | 95% | ❌ 20 pts to go |
| P10 | 2334 | 0.7% | 0.7% | -0.2 | n/a | no target |
| P11 | 1455 | 16.4% | 16.4% | +0.0 | n/a | no target |
| P12 | 15 | 20.0% | 20.0% | +0.0 | n/a | no target |
| P13 | 97406 | 0.3% | 0.3% | +0.0 | n/a | no target |

### `invoicing_requirements`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 129 | 7.8% | 7.8% | +0.0 | n/a | no target |
| P01T | 189 | 8.5% | 8.5% | +0.2 | n/a | no target |
| P01_GOLD | 626 | 58.0% | 58.1% | +0.0 | 80% | ❌ 22 pts to go |
| P02 | 464 | 45.9% | 46.1% | +0.2 | 75% | ❌ 29 pts to go |
| P03 | 263 | 37.3% | 37.3% | +0.0 | 70% | ❌ 33 pts to go |
| P04 | 3678 | 21.4% | 21.8% | +0.3 | 70% | ❌ 49 pts to go |
| P05 | 422 | 14.2% | 14.2% | +0.0 | 50% | ❌ 36 pts to go |
| P06M | 14663 | 0.3% | 0.3% | +0.0 | n/a | no target |
| P06T | 35923 | 0.3% | 0.3% | +0.0 | n/a | no target |
| P06 | 271 | 16.6% | 16.6% | +0.1 | n/a | no target |
| P07 | 691 | 2.0% | 2.0% | +0.0 | n/a | no target |
| P08 | 21900 | 0.4% | 0.4% | +0.0 | n/a | no target |
| P09 | 307 | 46.6% | 46.9% | +0.0 | 80% | ❌ 33 pts to go |
| P10 | 2334 | 1.1% | 1.1% | -0.1 | n/a | no target |
| P11 | 1455 | 6.8% | 6.9% | +0.0 | n/a | no target |
| P12 | 15 | 40.0% | 40.0% | +0.0 | n/a | no target |
| P13 | 97406 | 0.2% | 0.2% | +0.0 | n/a | no target |

### `payment_terms_as_published`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 129 | 18.6% | 18.6% | +0.0 | n/a | no target |
| P01T | 189 | 21.2% | 21.2% | -0.2 | 60% | ❌ 39 pts to go |
| P01_GOLD | 626 | 63.6% | 63.6% | +0.2 | 70% | 🟡 6 pts to go |
| P02 | 464 | 39.9% | 39.9% | +0.2 | 50% | ❌ 10 pts to go |
| P03 | 263 | 48.3% | 48.3% | +0.0 | 55% | 🟡 7 pts to go |
| P04 | 3678 | 12.3% | 12.3% | +0.1 | 40% | ❌ 28 pts to go |
| P05 | 422 | 17.1% | 17.1% | +0.0 | 40% | ❌ 23 pts to go |
| P06M | 14663 | 2.2% | 2.2% | +0.0 | n/a | no target |
| P06T | 35923 | 1.7% | 1.7% | +0.0 | n/a | no target |
| P06 | 271 | 21.8% | 21.8% | -0.2 | n/a | no target |
| P07 | 691 | 6.7% | 6.7% | +0.1 | n/a | no target |
| P08 | 21900 | 2.9% | 2.9% | +0.0 | n/a | no target |
| P09 | 307 | 5.9% | 5.9% | +0.0 | n/a | no target |
| P10 | 2334 | 4.7% | 4.7% | +0.1 | n/a | no target |
| P11 | 1455 | 5.2% | 5.2% | +0.0 | n/a | no target |
| P12 | 15 | 6.7% | 6.7% | +0.0 | n/a | no target |
| P13 | 97406 | 1.0% | 1.0% | +0.0 | n/a | no target |

### `po_required_as_published`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 129 | 21.7% | 21.7% | +0.0 | n/a | no target |
| P01T | 189 | 29.1% | 29.1% | +0.5 | 65% | ❌ 36 pts to go |
| P01_GOLD | 626 | 69.0% | 69.0% | +0.0 | 70% | 🟡 1 pts to go |
| P02 | 464 | 24.4% | 24.4% | +0.2 | 50% | ❌ 26 pts to go |
| P03 | 263 | 52.5% | 52.5% | +0.0 | 60% | 🟡 8 pts to go |
| P04 | 3678 | 5.5% | 5.5% | +0.1 | 40% | ❌ 34 pts to go |
| P05 | 422 | 19.7% | 19.7% | +0.0 | 45% | ❌ 25 pts to go |
| P06M | 14663 | 1.4% | 1.4% | +0.0 | n/a | no target |
| P06T | 35923 | 0.7% | 0.7% | +0.0 | n/a | no target |
| P06 | 271 | 34.7% | 34.7% | +0.3 | n/a | no target |
| P07 | 691 | 6.8% | 6.8% | -0.1 | n/a | no target |
| P08 | 21900 | 1.3% | 1.3% | +0.0 | n/a | no target |
| P09 | 307 | 9.8% | 9.8% | +0.0 | n/a | no target |
| P10 | 2334 | 3.0% | 3.0% | -0.1 | n/a | no target |
| P11 | 1455 | 5.1% | 5.1% | +0.0 | n/a | no target |
| P12 | 15 | 6.7% | 6.7% | +0.0 | n/a | no target |
| P13 | 97406 | 0.3% | 0.3% | +0.0 | n/a | no target |

### `invoice_portal_url`

> ceiling: only portals the buyer names on its own pages; informational tax-authority links are not portals

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 129 | 12.4% | 12.4% | +0.0 | n/a | no target |
| P01T | 189 | 13.8% | 13.8% | +0.3 | n/a | no target |
| P01_GOLD | 626 | 49.8% | 49.8% | +0.0 | 50% | 🟡 0 pts to go |
| P02 | 464 | 37.5% | 37.5% | +0.2 | n/a | no target |
| P03 | 263 | 52.1% | 52.1% | +0.0 | 60% | 🟡 8 pts to go |
| P04 | 3678 | 12.0% | 12.0% | +0.1 | n/a | no target |
| P05 | 422 | 15.2% | 15.2% | +0.0 | n/a | no target |
| P06M | 14663 | 0.5% | 0.5% | +0.0 | n/a | no target |
| P06T | 35923 | 0.4% | 0.4% | +0.0 | n/a | no target |
| P06 | 271 | 25.8% | 25.8% | +0.2 | n/a | no target |
| P07 | 691 | 8.4% | 8.4% | +0.1 | n/a | no target |
| P08 | 21900 | 0.6% | 0.6% | +0.0 | n/a | no target |
| P09 | 307 | 17.6% | 17.6% | +0.0 | n/a | no target |
| P10 | 2334 | 2.4% | 2.4% | +0.0 | n/a | no target |
| P11 | 1455 | 4.7% | 4.7% | +0.0 | n/a | no target |
| P12 | 15 | 13.3% | 13.3% | +0.0 | n/a | no target |
| P13 | 97406 | 0.3% | 0.3% | +0.0 | n/a | no target |

### `buyer_payment_method_preference`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 129 | 11.6% | 11.6% | +0.0 | 15% | 🟡 3 pts to go |
| P01T | 189 | 12.2% | 12.2% | -0.3 | 15% | 🟡 3 pts to go |
| P01_GOLD | 626 | 35.5% | 35.5% | +0.2 | 40% | 🟡 4 pts to go |
| P02 | 464 | 12.9% | 13.1% | +0.0 | 25% | ❌ 12 pts to go |
| P03 | 263 | 17.5% | 17.5% | +0.0 | 25% | 🟡 8 pts to go |
| P04 | 3678 | 2.8% | 2.8% | +0.1 | 15% | ❌ 12 pts to go |
| P05 | 422 | 6.6% | 6.6% | +0.0 | 15% | 🟡 8 pts to go |
| P06M | 14663 | 0.9% | 0.9% | +0.0 | 15% | ❌ 14 pts to go |
| P06T | 35923 | 0.5% | 0.5% | +0.0 | 15% | ❌ 14 pts to go |
| P06 | 271 | 10.7% | 10.7% | +0.1 | 15% | 🟡 4 pts to go |
| P07 | 691 | 4.2% | 4.2% | -0.1 | 15% | ❌ 11 pts to go |
| P08 | 21900 | 0.6% | 0.6% | +0.0 | 15% | ❌ 14 pts to go |
| P09 | 307 | 1.0% | 1.0% | +0.0 | 15% | ❌ 14 pts to go |
| P10 | 2334 | 1.3% | 1.3% | +0.0 | 15% | ❌ 14 pts to go |
| P11 | 1455 | 1.5% | 1.5% | +0.0 | 15% | ❌ 14 pts to go |
| P12 | 15 | 0.0% | 0.0% | +0.0 | 15% | ❌ 15 pts to go |
| P13 | 97406 | 0.7% | 0.7% | +0.0 | 15% | ❌ 14 pts to go |

### `buyer_tax_exempt_status`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 129 | 5.4% | 5.4% | +0.0 | 15% | 🟡 10 pts to go |
| P01T | 189 | 11.6% | 11.6% | +0.1 | 25% | ❌ 13 pts to go |
| P01_GOLD | 626 | 29.2% | 29.2% | +0.0 | 25% | ✅ met |
| P02 | 464 | 25.4% | 25.4% | +0.1 | 15% | ✅ met |
| P03 | 263 | 22.1% | 22.1% | +0.0 | 15% | ✅ met |
| P04 | 3678 | 4.0% | 4.0% | +0.0 | 15% | ❌ 11 pts to go |
| P05 | 422 | 11.1% | 11.1% | +0.0 | 15% | 🟡 4 pts to go |
| P06M | 14663 | 0.5% | 0.5% | +0.0 | 15% | ❌ 14 pts to go |
| P06T | 35923 | 0.2% | 0.2% | +0.0 | 15% | ❌ 15 pts to go |
| P06 | 271 | 8.5% | 8.5% | +0.1 | 15% | 🟡 6 pts to go |
| P07 | 691 | 2.9% | 2.9% | +0.0 | 15% | ❌ 12 pts to go |
| P08 | 21900 | 0.5% | 0.5% | +0.0 | 15% | ❌ 14 pts to go |
| P09 | 307 | 1.0% | 1.0% | +0.0 | 15% | ❌ 14 pts to go |
| P10 | 2334 | 1.6% | 1.6% | +0.0 | 15% | ❌ 13 pts to go |
| P11 | 1455 | 2.7% | 2.7% | +0.0 | 15% | ❌ 12 pts to go |
| P12 | 15 | 20.0% | 20.0% | +0.0 | 15% | ✅ met |
| P13 | 97406 | 0.2% | 0.2% | +0.0 | 15% | ❌ 15 pts to go |

### `buyer_ap_cycle_published`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 129 | 2.3% | 2.3% | +0.0 | 20% | ❌ 18 pts to go |
| P01T | 189 | 4.2% | 4.2% | +0.0 | 20% | ❌ 16 pts to go |
| P01_GOLD | 626 | 4.5% | 4.5% | +0.0 | 20% | ❌ 16 pts to go |
| P02 | 464 | 1.5% | 1.5% | +0.0 | 20% | ❌ 18 pts to go |
| P03 | 263 | 1.5% | 1.5% | +0.0 | 20% | ❌ 18 pts to go |
| P04 | 3678 | 0.6% | 0.6% | +0.0 | 20% | ❌ 19 pts to go |
| P05 | 422 | 1.2% | 1.2% | +0.0 | 20% | ❌ 19 pts to go |
| P06M | 14663 | 0.0% | 0.0% | +0.0 | 20% | ❌ 20 pts to go |
| P06T | 35923 | 0.0% | 0.0% | +0.0 | 20% | ❌ 20 pts to go |
| P06 | 271 | 1.5% | 1.5% | +0.0 | 20% | ❌ 18 pts to go |
| P07 | 691 | 0.4% | 0.4% | +0.0 | 20% | ❌ 20 pts to go |
| P08 | 21900 | 0.1% | 0.1% | +0.1 | 20% | ❌ 20 pts to go |
| P09 | 307 | 0.0% | 0.0% | +0.0 | 20% | ❌ 20 pts to go |
| P10 | 2334 | 0.3% | 0.3% | +0.0 | 20% | ❌ 20 pts to go |
| P11 | 1455 | 0.3% | 0.3% | +0.0 | 20% | ❌ 20 pts to go |
| P12 | 15 | 0.0% | 0.0% | +0.0 | 20% | ❌ 20 pts to go |
| P13 | 97406 | 0.0% | 0.0% | +0.0 | 20% | ❌ 20 pts to go |

### `buyer_esignature_preference`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 129 | 1.6% | 1.6% | +0.0 | 15% | ❌ 13 pts to go |
| P01T | 189 | 3.2% | 3.2% | +0.1 | 15% | ❌ 12 pts to go |
| P01_GOLD | 626 | 10.4% | 10.4% | +0.0 | 15% | 🟡 5 pts to go |
| P02 | 464 | 12.1% | 12.1% | +0.1 | 15% | 🟡 3 pts to go |
| P03 | 263 | 20.2% | 20.2% | +0.0 | 15% | ✅ met |
| P04 | 3678 | 2.3% | 2.3% | +0.0 | 15% | ❌ 13 pts to go |
| P05 | 422 | 2.8% | 2.8% | +0.0 | 15% | ❌ 12 pts to go |
| P06M | 14663 | 0.3% | 0.3% | +0.0 | 15% | ❌ 15 pts to go |
| P06T | 35923 | 0.2% | 0.2% | +0.0 | 15% | ❌ 15 pts to go |
| P06 | 271 | 5.2% | 5.2% | +0.1 | 15% | 🟡 10 pts to go |
| P07 | 691 | 1.6% | 1.6% | +0.0 | 15% | ❌ 13 pts to go |
| P08 | 21900 | 0.5% | 0.5% | +0.0 | 15% | ❌ 14 pts to go |
| P09 | 307 | 0.7% | 0.7% | +0.0 | 15% | ❌ 14 pts to go |
| P10 | 2334 | 1.0% | 1.0% | +0.0 | 15% | ❌ 14 pts to go |
| P11 | 1455 | 1.2% | 1.2% | +0.0 | 15% | ❌ 14 pts to go |
| P12 | 15 | 6.7% | 6.7% | +0.0 | 15% | 🟡 8 pts to go |
| P13 | 97406 | 0.1% | 0.1% | +0.0 | 15% | ❌ 15 pts to go |

### `ap_system_hint`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 129 | 14.0% | 14.0% | +0.0 | 20% | 🟡 6 pts to go |
| P01T | 189 | 14.3% | 14.3% | +0.2 | 40% | ❌ 26 pts to go |
| P01_GOLD | 626 | 46.2% | 46.2% | +0.0 | 40% | ✅ met |
| P02 | 464 | 43.1% | 43.1% | +0.2 | 20% | ✅ met |
| P03 | 263 | 49.0% | 49.0% | +0.0 | 35% | ✅ met |
| P04 | 3678 | 14.3% | 14.3% | +0.1 | 20% | 🟡 6 pts to go |
| P05 | 422 | 15.4% | 15.4% | +0.0 | 20% | 🟡 5 pts to go |
| P06M | 14663 | 0.8% | 0.8% | +0.0 | 20% | ❌ 19 pts to go |
| P06T | 35923 | 0.7% | 0.7% | +0.0 | 20% | ❌ 19 pts to go |
| P06 | 271 | 25.5% | 25.5% | +0.2 | 20% | ✅ met |
| P07 | 691 | 8.7% | 8.7% | +0.1 | 20% | ❌ 11 pts to go |
| P08 | 21900 | 1.0% | 1.0% | +0.0 | 20% | ❌ 19 pts to go |
| P09 | 307 | 18.2% | 18.2% | +0.0 | 20% | 🟡 2 pts to go |
| P10 | 2334 | 3.6% | 3.6% | -0.1 | 20% | ❌ 16 pts to go |
| P11 | 1455 | 4.8% | 4.8% | +0.0 | 20% | ❌ 15 pts to go |
| P12 | 15 | 6.7% | 6.7% | +0.0 | 20% | ❌ 13 pts to go |
| P13 | 97406 | 0.5% | 0.5% | +0.0 | 20% | ❌ 20 pts to go |

## 5. contract

### `contract_value`

> ceiling: rows proven by a lobbying filing, a news release, an auditor appointment, a customer story or a vendor's client list have no contract value by nature (≈17 % of P01 Gold); bids&tenders awards now carry the awarded bidder's submitted price when no award value was published

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 129 | 33.3% | 33.3% | +0.0 | n/a | no target |
| P01T | 189 | 0.5% | 0.5% | +0.0 | n/a | no target |
| P01_GOLD | 626 | 69.5% | 69.5% | +0.0 | 95% | ❌ 26 pts to go |
| P02 | 464 | 63.1% | 63.1% | +0.2 | 95% | ❌ 32 pts to go |
| P03 | 263 | 53.2% | 53.2% | +0.0 | 90% | ❌ 37 pts to go |
| P04 | 3678 | 25.1% | 25.1% | +0.3 | 85% | ❌ 60 pts to go |
| P05 | 422 | 37.7% | 37.7% | +0.0 | 75% | ❌ 37 pts to go |
| P06M | 14663 | 36.2% | 36.2% | +0.1 | n/a | no target |
| P06T | 35923 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06 | 271 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P07 | 691 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P08 | 21900 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P09 | 307 | 88.3% | 88.3% | +0.0 | 100% | ❌ 12 pts to go |
| P10 | 2334 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P11 | 1455 | 6.0% | 6.0% | +0.0 | 60% | ❌ 54 pts to go |
| P12 | 15 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P13 | 97406 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `currency`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 129 | 33.3% | 33.3% | +0.0 | n/a | no target |
| P01T | 189 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P01_GOLD | 626 | 72.8% | 72.8% | +0.0 | 100% | ❌ 27 pts to go |
| P02 | 464 | 66.6% | 66.6% | +0.3 | 100% | ❌ 33 pts to go |
| P03 | 263 | 58.9% | 58.9% | +0.0 | n/a | no target |
| P04 | 3678 | 25.8% | 25.8% | +0.3 | 95% | ❌ 69 pts to go |
| P05 | 422 | 33.4% | 33.4% | +0.0 | 80% | ❌ 47 pts to go |
| P06M | 14663 | 36.2% | 36.2% | +0.1 | n/a | no target |
| P06T | 35923 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06 | 271 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P07 | 691 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P08 | 21900 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P09 | 307 | 91.5% | 91.5% | +0.0 | 100% | 🟡 8 pts to go |
| P10 | 2334 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P11 | 1455 | 6.4% | 6.4% | +0.0 | n/a | no target |
| P12 | 15 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P13 | 97406 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `start_date`

> ceiling: most award notices publish an award date, not a start date; start_date carries the signature date when the source gives one, labelled

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 129 | 79.8% | 79.8% | +0.0 | n/a | no target |
| P01T | 189 | 0.5% | 0.5% | +0.0 | n/a | no target |
| P01_GOLD | 626 | 51.6% | 51.6% | +0.0 | 85% | ❌ 33 pts to go |
| P02 | 464 | 57.8% | 57.8% | +0.3 | 90% | ❌ 32 pts to go |
| P03 | 263 | 42.6% | 42.6% | +0.0 | 85% | ❌ 42 pts to go |
| P04 | 3678 | 28.2% | 28.2% | +0.3 | 90% | ❌ 62 pts to go |
| P05 | 422 | 32.7% | 32.7% | +0.0 | 75% | ❌ 42 pts to go |
| P06M | 14663 | 86.9% | 86.9% | -0.2 | n/a | no target |
| P06T | 35923 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06 | 271 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P07 | 691 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P08 | 21900 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P09 | 307 | 83.4% | 83.4% | +0.0 | 95% | ❌ 12 pts to go |
| P10 | 2334 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P11 | 1455 | 5.4% | 5.4% | +0.0 | n/a | no target |
| P12 | 15 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P13 | 97406 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `end_date`

> ceiling: an inferred end (award date + published duration) is labelled as such; sources without a duration leave end_date empty — the honest ceiling. P09 is BY DEFINITION the rows whose end date is not published (older SEAO contracts with no closing notice): its end_date / duration targets cannot be met without inventing a date

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 129 | 78.3% | 78.3% | +0.0 | n/a | no target |
| P01T | 189 | 0.5% | 0.5% | +0.0 | n/a | no target |
| P01_GOLD | 626 | 51.8% | 51.8% | +0.0 | 85% | ❌ 33 pts to go |
| P02 | 464 | 52.8% | 52.8% | +0.2 | 90% | ❌ 37 pts to go |
| P03 | 263 | 43.7% | 43.7% | +0.0 | 85% | ❌ 41 pts to go |
| P04 | 3678 | 24.1% | 24.1% | +0.3 | 90% | ❌ 66 pts to go |
| P05 | 422 | 43.4% | 43.4% | +0.0 | 75% | ❌ 32 pts to go |
| P06M | 14663 | 77.7% | 77.7% | -0.1 | n/a | no target |
| P06T | 35923 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06 | 271 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P07 | 691 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P08 | 21900 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P09 | 307 | 0.3% | 0.3% | +0.0 | 95% | ❌ 95 pts to go |
| P10 | 2334 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P11 | 1455 | 4.5% | 4.5% | +0.0 | n/a | no target |
| P12 | 15 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P13 | 97406 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `contract_title`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 129 | 89.9% | 89.9% | +0.0 | n/a | no target |
| P01T | 189 | 94.2% | 94.2% | -0.1 | n/a | no target |
| P01_GOLD | 626 | 85.3% | 85.3% | +0.0 | 100% | ❌ 15 pts to go |
| P02 | 464 | 76.7% | 76.7% | +0.3 | 100% | ❌ 23 pts to go |
| P03 | 263 | 91.3% | 91.3% | +0.0 | n/a | no target |
| P04 | 3678 | 49.1% | 49.1% | +0.3 | 95% | ❌ 46 pts to go |
| P05 | 422 | 77.5% | 77.5% | +0.0 | 95% | ❌ 18 pts to go |
| P06M | 14663 | 98.9% | 98.9% | +0.0 | n/a | no target |
| P06T | 35923 | 90.8% | 90.8% | +0.2 | n/a | no target |
| P06 | 271 | 22.9% | 22.9% | -0.2 | n/a | no target |
| P07 | 691 | 13.3% | 13.3% | -0.5 | n/a | no target |
| P08 | 21900 | 7.0% | 7.0% | -0.1 | n/a | no target |
| P09 | 307 | 98.7% | 98.7% | +0.0 | 100% | 🟡 1 pts to go |
| P10 | 2334 | 70.8% | 70.8% | -0.2 | n/a | no target |
| P11 | 1455 | 68.1% | 68.1% | +0.0 | n/a | no target |
| P12 | 15 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P13 | 97406 | 99.7% | 99.7% | +0.0 | n/a | no target |

### `contract_description`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 129 | 89.9% | 89.9% | +0.0 | n/a | no target |
| P01T | 189 | 94.2% | 94.2% | -0.1 | n/a | no target |
| P01_GOLD | 626 | 88.5% | 88.5% | +0.0 | 100% | ❌ 12 pts to go |
| P02 | 464 | 77.8% | 78.0% | +0.3 | 100% | ❌ 22 pts to go |
| P03 | 263 | 92.0% | 92.0% | +0.0 | n/a | no target |
| P04 | 3678 | 52.4% | 52.4% | +0.5 | 95% | ❌ 43 pts to go |
| P05 | 422 | 89.6% | 89.6% | +0.0 | 70% | ✅ met |
| P06M | 14663 | 98.9% | 98.9% | +0.0 | n/a | no target |
| P06T | 35923 | 90.8% | 90.8% | +0.2 | n/a | no target |
| P06 | 271 | 22.9% | 22.9% | -0.2 | n/a | no target |
| P07 | 691 | 13.3% | 13.3% | -0.5 | n/a | no target |
| P08 | 21900 | 7.0% | 7.0% | -0.1 | n/a | no target |
| P09 | 307 | 98.7% | 98.7% | +0.0 | 100% | 🟡 1 pts to go |
| P10 | 2334 | 70.8% | 70.8% | -0.2 | n/a | no target |
| P11 | 1455 | 68.2% | 68.2% | +0.0 | n/a | no target |
| P12 | 15 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P13 | 97406 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `number_of_bids`

> ceiling: published by some portals only (bids&tenders submission lists, Biddingo bidder lists); federal proactive disclosure does not publish bid counts

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 129 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P01T | 189 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P01_GOLD | 626 | 16.8% | 16.8% | +0.0 | 60% | ❌ 43 pts to go · rows from a source that publishes bids: 363 rows, 28.9% filled |
| P02 | 464 | 11.2% | 11.2% | +0.0 | n/a | no target · rows from a source that publishes bids: 290 rows, 17.9% filled |
| P03 | 263 | 12.9% | 12.9% | +0.0 | n/a | no target · rows from a source that publishes bids: 139 rows, 24.5% filled |
| P04 | 3678 | 1.5% | 1.5% | +0.0 | n/a | no target · rows from a source that publishes bids: 871 rows, 6.3% filled |
| P05 | 422 | 2.6% | 2.6% | +0.0 | n/a | no target · rows from a source that publishes bids: 50 rows, 22.0% filled |
| P06M | 14663 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06T | 35923 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06 | 271 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P07 | 691 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P08 | 21900 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P09 | 307 | 4.2% | 4.2% | +0.0 | n/a | no target · rows from a source that publishes bids: 293 rows, 4.4% filled |
| P10 | 2334 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P11 | 1455 | 0.9% | 0.9% | +0.0 | n/a | no target · rows from a source that publishes bids: 90 rows, 14.4% filled |
| P12 | 15 | 0.0% | 0.0% | +0.0 | n/a | no target · rows from a source that publishes bids: 15 rows, 0.0% filled |
| P13 | 97406 | 0.0% | 0.0% | +0.0 | n/a | no target |

## 6. history

### `average_contract_duration_days`

> ceiling: needs two dates (or a published term) on the buyer's records; P09 rows (end date unpublished by definition) and buyers whose sources publish award dates only have no honest duration

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 129 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P01T | 189 | 0.0% | 97.9% | +0.0 | n/a | no target |
| P01_GOLD | 626 | 53.2% | 82.4% | +0.0 | 90% | ❌ 37 pts to go |
| P02 | 464 | 52.6% | 87.5% | +0.2 | 90% | ❌ 37 pts to go |
| P03 | 263 | 44.5% | 80.6% | +0.0 | 90% | ❌ 46 pts to go |
| P04 | 3678 | 19.3% | 93.8% | +0.2 | 90% | ❌ 71 pts to go |
| P05 | 422 | 0.0% | 83.4% | +0.0 | 90% | ❌ 90 pts to go |
| P06M | 14663 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P06T | 35923 | 0.0% | 99.8% | +0.0 | n/a | no target |
| P06 | 271 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P07 | 691 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P08 | 21900 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P09 | 307 | 2.3% | 3.9% | +0.0 | 90% | ❌ 88 pts to go |
| P10 | 2334 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P11 | 1455 | 4.1% | 96.9% | +0.0 | n/a | no target |
| P12 | 15 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P13 | 97406 | 0.0% | 100.0% | +0.0 | n/a | no target |

### `commodity_distribution_top3`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 129 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P01T | 189 | 0.5% | 98.4% | +0.0 | n/a | no target |
| P01_GOLD | 626 | 25.9% | 55.1% | +0.0 | 90% | ❌ 64 pts to go |
| P02 | 464 | 51.7% | 86.6% | +0.2 | n/a | no target |
| P03 | 263 | 24.3% | 60.5% | +0.0 | n/a | no target |
| P04 | 3678 | 21.2% | 95.7% | +0.2 | n/a | no target |
| P05 | 422 | 0.5% | 83.9% | +0.0 | n/a | no target |
| P06M | 14663 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P06T | 35923 | 0.1% | 99.9% | +0.0 | n/a | no target |
| P06 | 271 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P07 | 691 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P08 | 21900 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P09 | 307 | 41.0% | 42.7% | +0.0 | n/a | no target |
| P10 | 2334 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P11 | 1455 | 3.7% | 96.6% | +0.0 | n/a | no target |
| P12 | 15 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P13 | 97406 | 0.0% | 100.0% | +0.0 | n/a | no target |

### `year_over_year_spend_trend`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 129 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P01T | 189 | 2.1% | 100.0% | +0.0 | n/a | no target |
| P01_GOLD | 626 | 51.8% | 81.0% | +0.0 | 95% | ❌ 43 pts to go |
| P02 | 464 | 56.7% | 91.6% | +0.3 | n/a | no target |
| P03 | 263 | 46.8% | 82.9% | +0.0 | n/a | no target |
| P04 | 3678 | 21.4% | 95.9% | +0.2 | n/a | no target |
| P05 | 422 | 4.5% | 87.9% | +0.0 | n/a | no target |
| P06M | 14663 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P06T | 35923 | 0.1% | 100.0% | +0.0 | n/a | no target |
| P06 | 271 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P07 | 691 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P08 | 21900 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P09 | 307 | 62.5% | 64.2% | +0.0 | n/a | no target |
| P10 | 2334 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P11 | 1455 | 4.1% | 97.0% | +0.0 | n/a | no target |
| P12 | 15 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P13 | 97406 | 0.0% | 100.0% | +0.0 | n/a | no target |

## 7. mail security

### `mta_sts`

> ceiling: DNS-only check; 'no record' counts as checked

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 129 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P01T | 189 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P01_GOLD | 626 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P02 | 464 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P03 | 263 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P04 | 3678 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P05 | 422 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P06M | 14663 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P06T | 35923 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P06 | 271 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P07 | 691 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P08 | 21900 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P09 | 307 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P10 | 2334 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P11 | 1455 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P12 | 15 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P13 | 97406 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |

### `tls_rpt`

> ceiling: DNS-only check; 'no record' counts as checked

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 129 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P01T | 189 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P01_GOLD | 626 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P02 | 464 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P03 | 263 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P04 | 3678 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P05 | 422 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P06M | 14663 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P06T | 35923 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P06 | 271 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P07 | 691 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P08 | 21900 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P09 | 307 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P10 | 2334 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P11 | 1455 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P12 | 15 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P13 | 97406 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |

### `bimi`

> ceiling: DNS-only check; 'no record' counts as checked

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 129 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P01T | 189 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P01_GOLD | 626 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P02 | 464 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P03 | 263 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P04 | 3678 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P05 | 422 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P06M | 14663 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P06T | 35923 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P06 | 271 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P07 | 691 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P08 | 21900 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P09 | 307 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P10 | 2334 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P11 | 1455 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P12 | 15 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P13 | 97406 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |

