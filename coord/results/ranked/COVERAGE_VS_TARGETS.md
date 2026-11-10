# Coverage vs the downstream team's targets — 2026-11-10

Benchmarks (field × package with a numeric target): **102 of 446 met** (22.9%); 66 within 10 points; 278 further away.
A cell counts as filled only when it carries a value: blank, `not_published`, `not_found_yet` and label-only cells ("no identifier published …", "no dataset record …", "0 in the contract dataset …") do not count; the DNS checks count when checked. `any` = share of non-blank cells incl. such labels. Δ = change since the previous build in `coord/results/coverage_history.csv`.
Rows per package: P01M 44, P01T 139, P01_GOLD 626, P02 403, P03 209, P04 1570, P05 377, P06M 4314, P06T 9559, P06 276, P07 529, P08 11055, P09 348, P10R 27005, P10 2580, P11 3168, P12 8, P13 11305

## Invoice-grade readiness (the row as an invoice header: bill-to, submit-to, references, terms, tax, vendor identity, follow-up)

| package | rows | all 11 elements | ≥ 9 of 11 | median elements | most-missing element |
|---|---|---|---|---|---|
| P01M | 44 | 0.0% | 25.0% | 8 | PO rule (36 rows) |
| P01T | 139 | 0.7% | 31.7% | 8 | reference to quote (PO / contract / vendor id) (133 rows) |
| P01_GOLD | 626 | 24.3% | 71.1% | 10 | payment terms (215 rows) |
| P02 | 403 | 8.9% | 62.8% | 9 | PO rule (298 rows) |
| P03 | 209 | 17.7% | 69.9% | 9 | PO rule (92 rows) |
| P04 | 1570 | 2.9% | 38.4% | 8 | PO rule (1415 rows) |
| P05 | 377 | 1.3% | 18.8% | 7 | payment terms (308 rows) |
| P06M | 4314 | 0.0% | 1.1% | 8 | PO rule (4304 rows) |
| P06T | 9559 | 0.0% | 1.5% | 6 | reference to quote (PO / contract / vendor id) (9526 rows) |
| P06 | 276 | 0.0% | 7.2% | 6 | reference to quote (PO / contract / vendor id) (276 rows) |
| P07 | 529 | 0.0% | 2.5% | 5 | reference to quote (PO / contract / vendor id) (529 rows) |
| P08 | 11055 | 0.0% | 0.2% | 5 | reference to quote (PO / contract / vendor id) (11055 rows) |
| P09 | 348 | 1.1% | 44.3% | 8 | payment terms (325 rows) |
| P10R | 27005 | 0.0% | 0.0% | 6 | vendor GST/HST number (27005 rows) |
| P10 | 2580 | 0.0% | 0.9% | 5 | reference to quote (PO / contract / vendor id) (2577 rows) |
| P11 | 3168 | 0.2% | 1.8% | 6 | PO rule (3137 rows) |
| P12 | 8 | 0.0% | 62.5% | 9 | PO rule (7 rows) |
| P13 | 11305 | 0.0% | 0.0% | 6 | reference to quote (PO / contract / vendor id) (11305 rows) |

## AP grade (how stringently the row's accounts-payable data meets what an invoice needs; A = invoicing mailbox referee-confirmed on the buyer's own domain with MX, legal name, address, PO rule and terms all published, no penalties)

| package | rows | A | B | C | D | E | median ap_score |
|---|---|---|---|---|---|---|---|
| P01M | 44 | 6 | 1 | 37 | 0 | 0 | 73 |
| P01T | 139 | 27 | 44 | 68 | 0 | 0 | 76 |
| P01_GOLD | 626 | 231 | 186 | 209 | 0 | 0 | 82 |
| P02 | 403 | 0 | 183 | 220 | 0 | 0 | 66 |
| P03 | 209 | 0 | 0 | 202 | 7 | 0 | 58 |
| P04 | 1570 | 0 | 0 | 1520 | 50 | 0 | 53 |
| P05 | 377 | 15 | 28 | 317 | 17 | 0 | 51 |
| P06M | 4314 | 0 | 3 | 4307 | 4 | 0 | 51 |
| P06T | 9559 | 0 | 26 | 8505 | 1028 | 0 | 43 |
| P06 | 276 | 21 | 34 | 221 | 0 | 0 | 71 |
| P07 | 529 | 0 | 16 | 479 | 34 | 0 | 53 |
| P08 | 11055 | 0 | 0 | 8402 | 2653 | 0 | 43 |
| P09 | 348 | 5 | 13 | 327 | 3 | 0 | 53 |
| P10R | 27005 | 0 | 7 | 21984 | 5014 | 0 | 43 |
| P10 | 2580 | 4 | 14 | 1841 | 721 | 0 | 43 |
| P11 | 3168 | 0 | 0 | 0 | 0 | 3168 | 23 |
| P12 | 8 | 0 | 1 | 7 | 0 | 0 | 54 |
| P13 | 11305 | 2 | 8 | 10181 | 1114 | 0 | 51 |

### AP payability (confirmed channel + bill-to legal name and address + the buyer's reference rule + tax treatment known)

| package | rows | payable today | % | most common gap |
|---|---|---|---|---|
| P01M | 44 | 34 | 77.3% | the buyer's PO / reference rule (8) |
| P01T | 139 | 57 | 41.0% | the buyer's PO / reference rule (50) |
| P01_GOLD | 626 | 464 | 74.1% | bill-to legal name and address (109) |
| P02 | 403 | 305 | 75.7% | the buyer's PO / reference rule (54) |
| P03 | 209 | 0 | 0.0% | a confirmed invoicing / AP or finance channel (209) |
| P04 | 1570 | 0 | 0.0% | a confirmed invoicing / AP or finance channel (1570) |
| P05 | 377 | 46 | 12.2% | a confirmed invoicing / AP or finance channel (290) |
| P06M | 4314 | 32 | 0.7% | a confirmed invoicing / AP or finance channel (4255) |
| P06T | 9559 | 18 | 0.2% | a confirmed invoicing / AP or finance channel (9335) |
| P06 | 276 | 33 | 12.0% | bill-to legal name and address (144) |
| P07 | 529 | 9 | 1.7% | bill-to legal name and address (221) |
| P08 | 11055 | 0 | 0.0% | a confirmed invoicing / AP or finance channel (11055) |
| P09 | 348 | 48 | 13.8% | a confirmed invoicing / AP or finance channel (291) |
| P10R | 27005 | 294 | 1.1% | a confirmed invoicing / AP or finance channel (26385) |
| P10 | 2580 | 10 | 0.4% | a confirmed invoicing / AP or finance channel (2443) |
| P11 | 3168 | 0 | 0.0% | a confirmed invoicing / AP or finance channel (3168) |
| P12 | 8 | 2 | 25.0% | a confirmed invoicing / AP or finance channel (6) |
| P13 | 11305 | 3 | 0.0% | a confirmed invoicing / AP or finance channel (11024) |

### Pay on sight (an invoice generated from the row would clear AP: confirmed invoicing / AP or finance channel, bill-to legal name + address, vendor legal name + GST/HST number + remit-to address, tax treatment and currency known — published or labelled-derived; the buyer's reference rule is reported separately)

| package | rows | pay on sight | % | + reference rule not published | routed (general inbox only) | most common gap |
|---|---|---|---|---|---|---|
| P01M | 44 | 6 | 13.6% | 7 | 0 | the vendor's GST/HST number (BN9) (29) |
| P01T | 139 | 42 | 30.2% | 17 | 0 | the vendor's GST/HST number (BN9) (53) |
| P01_GOLD | 626 | 409 | 65.3% | 21 | 0 | the vendor's GST/HST number (BN9) (124) |
| P02 | 403 | 218 | 54.1% | 35 | 0 | the vendor's GST/HST number (BN9) (130) |
| P03 | 209 | 17 | 8.1% | 1 | 131 | an invoicing / AP or finance mailbox (only a purchasing / general inbo (49) |
| P04 | 1570 | 43 | 2.7% | 10 | 707 | an invoicing / AP or finance mailbox (only a purchasing / general inbo (772) |
| P05 | 377 | 22 | 5.8% | 10 | 93 | an invoicing / AP or finance mailbox (only a purchasing / general inbo (188) |
| P06M | 4314 | 2 | 0.0% | 14 | 66 | an invoicing / AP or finance mailbox (only a purchasing / general inbo (4179) |
| P06T | 9559 | 17 | 0.2% | 60 | 1880 | an invoicing / AP or finance mailbox (only a purchasing / general inbo (7381) |
| P06 | 276 | 14 | 5.1% | 19 | 0 | the vendor's GST/HST number (BN9) (143) |
| P07 | 529 | 7 | 1.3% | 28 | 16 | the vendor's GST/HST number (BN9) (226) |
| P08 | 11055 | 1 | 0.0% | 3 | 733 | an invoicing / AP or finance mailbox (only a purchasing / general inbo (10286) |
| P09 | 348 | 44 | 12.6% | 1 | 135 | an invoicing / AP or finance mailbox (only a purchasing / general inbo (146) |
| P10R | 27005 | 493 | 1.8% | 0 | 18388 | an invoicing / AP or finance mailbox (only a purchasing / general inbo (7938) |
| P10 | 2580 | 6 | 0.2% | 23 | 393 | an invoicing / AP or finance mailbox (only a purchasing / general inbo (2027) |
| P11 | 3168 | 5 | 0.2% | 0 | 0 | a confirmed invoicing / AP or finance channel (3152) |
| P12 | 8 | 2 | 25.0% | 0 | 3 | an invoicing / AP or finance mailbox (only a purchasing / general inbo (3) |
| P13 | 11305 | 3 | 0.0% | 217 | 7697 | an invoicing / AP or finance mailbox (only a purchasing / general inbo (3287) |
| **all** | 73515 | 1351 | 1.8% | 466 | 30242 | |

### What still blocks grade A (rows per missing element; a row counts under every element it lacks)

| package | rows not A | referee confirmation of the mailbox | an invoicing / AP mailbox (not finance / procurement / general) | a mailbox on the buyer's own domain | MX record for the mailbox domain | published bill-to legal name | invoice / billing address | published PO rule | published payment terms | clear the penalty |
|---|---|---|---|---|---|---|---|---|---|---|
| P01M | 38 | 0 | 0 | 0 | 1 | 2 | 0 | 36 | 37 | 1 |
| P01T | 112 | 0 | 0 | 0 | 6 | 21 | 4 | 71 | 82 | 30 |
| P01_GOLD | 395 | 0 | 0 | 0 | 11 | 94 | 34 | 193 | 228 | 60 |
| P02 | 403 | 0 | 403 | 0 | 4 | 38 | 8 | 298 | 227 | 22 |
| P03 | 209 | 0 | 209 | 0 | 2 | 34 | 11 | 92 | 94 | 25 |
| P04 | 1570 | 0 | 1570 | 0 | 12 | 327 | 93 | 1415 | 1210 | 106 |
| P05 | 362 | 0 | 312 | 0 | 8 | 91 | 44 | 296 | 310 | 55 |
| P06M | 4314 | 0 | 4314 | 0 | 80 | 299 | 31 | 4304 | 4294 | 3 |
| P06T | 9559 | 0 | 9559 | 0 | 1533 | 5199 | 1402 | 9445 | 9232 | 125 |
| P06 | 255 | 0 | 0 | 0 | 33 | 131 | 63 | 186 | 224 | 7 |
| P07 | 529 | 0 | 529 | 0 | 132 | 286 | 108 | 471 | 487 | 16 |
| P08 | 11055 | 0 | 11055 | 0 | 3882 | 7400 | 2982 | 10981 | 10894 | 166 |
| P09 | 343 | 0 | 322 | 0 | 9 | 73 | 4 | 316 | 329 | 50 |
| P10R | 27005 | 0 | 26917 | 0 | 451 | 15920 | 6607 | 26977 | 26928 | 24 |
| P10 | 2576 | 0 | 2521 | 0 | 212 | 1730 | 886 | 2529 | 2484 | 112 |
| P11 | 3168 | 3168 | 3120 | 0 | 1837 | 3020 | 796 | 3137 | 3106 | 31 |
| P12 | 8 | 0 | 7 | 0 | 0 | 2 | 0 | 7 | 6 | 0 |
| P13 | 11303 | 0 | 11209 | 0 | 324 | 3341 | 1604 | 11275 | 11281 | 26 |

## Where the work is (largest gaps in rows still needed)

| field | package | now | target | rows needed |
|---|---|---|---|---|
| vendor_registered_address | P08 | 14.6% | 70% | 6129 |
| buyer_ap_cycle_published | P10R | 0.0% | 20% | 5397 |
| vendor_logo_url | P08 | 51.6% | 100% | 5354 |
| ap_system_hint | P10R | 0.4% | 20% | 5290 |
| vendor_phone | P08 | 38.1% | 85% | 5182 |
| buyer_phone | P08 | 51.2% | 95% | 4841 |
| buyer_logo_url | P08 | 57.1% | 100% | 4746 |
| buyer_legal_name_as_published | P08 | 33.1% | 75% | 4637 |
| vendor_emails | P08 | 37.1% | 75% | 4194 |
| vendor_bn9 | P08 | 12.2% | 50% | 4184 |
| buyer_tax_exempt_status | P10R | 0.1% | 15% | 4035 |
| buyer_esignature_preference | P10R | 0.1% | 15% | 4034 |
| buyer_payment_method_preference | P10R | 0.6% | 15% | 3890 |
| vendor_trading_name | P08 | 21.7% | 50% | 3133 |
| invoice_reference_hint | P08 | 0.7% | 25% | 2690 |
| buyer_address | P08 | 73.0% | 95% | 2438 |
| buyer_ap_cycle_published | P13 | 0.0% | 20% | 2259 |
| buyer_phone | P13 | 75.3% | 95% | 2230 |
| buyer_ap_cycle_published | P08 | 0.0% | 20% | 2206 |
| buyer_logo_url | P11 | 10.8% | 80% | 2193 |
| buyer_bn_as_published | P08 | 15.4% | 35% | 2172 |
| ap_system_hint | P13 | 0.8% | 20% | 2165 |
| buyer_logo_url | P13 | 76.2% | 95% | 2129 |
| ap_system_hint | P08 | 0.8% | 20% | 2120 |
| buyer_phone | P11 | 8.2% | 75% | 2117 |
| vendor_phone | P11 | 11.8% | 75% | 2002 |
| vendor_emails | P11 | 9.6% | 70% | 1913 |
| buyer_legal_name_as_published | P11 | 4.7% | 65% | 1912 |
| buyer_ap_cycle_published | P06T | 0.1% | 20% | 1905 |
| contract_value | P11 | 2.8% | 60% | 1813 |
| award_or_notice_id | P11 | 2.8% | 60% | 1812 |
| ap_system_hint | P06T | 1.7% | 20% | 1752 |
| buyer_tax_exempt_status | P13 | 0.1% | 15% | 1688 |
| buyer_esignature_preference | P13 | 0.1% | 15% | 1686 |
| buyer_payment_method_preference | P13 | 0.5% | 15% | 1642 |
| buyer_esignature_preference | P08 | 0.2% | 15% | 1632 |
| buyer_payment_method_preference | P08 | 0.3% | 15% | 1626 |
| buyer_tax_exempt_status | P08 | 0.3% | 15% | 1625 |
| commodity_codes | P11 | 1.9% | 50% | 1523 |
| buyer_esignature_preference | P06T | 0.4% | 15% | 1396 |

## 1. identifiers

### `invoice_reference_hint`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 44 | 81.8% | 81.8% | +37.4 | 50% | ✅ met |
| P01T | 139 | 51.1% | 51.1% | -20.6 | 50% | ✅ met |
| P01_GOLD | 626 | 92.3% | 94.6% | -0.2 | 95% | 🟡 3 pts to go |
| P02 | 403 | 83.9% | 85.6% | +0.0 | 95% | ❌ 11 pts to go |
| P03 | 209 | 92.3% | 95.7% | -0.5 | 95% | 🟡 3 pts to go |
| P04 | 1570 | 68.7% | 71.3% | +0.1 | 90% | ❌ 21 pts to go |
| P05 | 377 | 41.6% | 44.6% | +0.5 | 70% | ❌ 28 pts to go |
| P06M | 4314 | 96.5% | 96.5% | +89.4 | n/a | no target |
| P06T | 9559 | 1.5% | 1.6% | -2.9 | n/a | no target |
| P06 | 276 | 32.6% | 32.6% | -15.6 | 30% | ✅ met |
| P07 | 529 | 11.0% | 11.0% | -12.8 | 30% | ❌ 19 pts to go |
| P08 | 11055 | 0.7% | 0.7% | -1.7 | 25% | ❌ 24 pts to go |
| P09 | 348 | 99.1% | 99.7% | +0.1 | 100% | 🟡 1 pts to go |
| P10R | 27005 | 100.0% | 100.0% |  | n/a | no target |
| P10 | 2580 | 2.1% | 2.9% | -0.1 | 25% | ❌ 23 pts to go |
| P11 | 3168 | 21.5% | 22.0% | -2.6 | 60% | ❌ 38 pts to go |
| P12 | 8 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P13 | 11305 | 0.3% | 0.3% | +0.1 | 0% by design | — leave (by design) |

### `po_number_as_published`

> ceiling: a purchase-order number exists only where the buyer publishes PO-level data (Montréal, Laval, Toronto open data so far) or the record itself carries one; most sources publish awards, not POs — the target cannot be reached from public data for most buyers

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 44 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P01T | 139 | 0.0% | 0.0% | +0.0 | 10% | 🟡 10 pts to go |
| P01_GOLD | 626 | 6.2% | 6.2% | +0.0 | 50% | ❌ 44 pts to go |
| P02 | 403 | 7.2% | 7.2% | +0.0 | 50% | ❌ 43 pts to go |
| P03 | 209 | 1.9% | 1.9% | +0.0 | 40% | ❌ 38 pts to go |
| P04 | 1570 | 1.1% | 1.1% | +0.0 | 30% | ❌ 29 pts to go |
| P05 | 377 | 0.3% | 0.3% | +0.0 | 20% | ❌ 20 pts to go |
| P06M | 4314 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06T | 9559 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06 | 276 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P07 | 529 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P08 | 11055 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P09 | 348 | 0.6% | 0.6% | +0.1 | 50% | ❌ 49 pts to go |
| P10R | 27005 | 0.0% | 0.0% |  | n/a | no target |
| P10 | 2580 | 0.1% | 0.1% | +0.0 | n/a | no target |
| P11 | 3168 | 0.1% | 0.1% | -0.7 | n/a | no target |
| P12 | 8 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P13 | 11305 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `contract_or_agreement_number`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 44 | 65.9% | 65.9% | +65.9 | n/a | no target |
| P01T | 139 | 4.3% | 4.3% | -1.1 | 50% | ❌ 46 pts to go |
| P01_GOLD | 626 | 67.6% | 67.6% | +0.0 | 85% | ❌ 17 pts to go |
| P02 | 403 | 75.4% | 75.4% | -0.1 | 90% | ❌ 15 pts to go |
| P03 | 209 | 75.1% | 75.1% | -0.4 | 85% | 🟡 10 pts to go |
| P04 | 1570 | 65.6% | 65.6% | +0.1 | 85% | ❌ 19 pts to go |
| P05 | 377 | 31.6% | 31.6% | +0.6 | 60% | ❌ 28 pts to go |
| P06M | 4314 | 96.2% | 96.2% | +96.2 | n/a | no target |
| P06T | 9559 | 0.3% | 0.3% | +0.1 | n/a | no target |
| P06 | 276 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P07 | 529 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P08 | 11055 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P09 | 348 | 96.6% | 96.6% | +0.0 | 100% | 🟡 3 pts to go |
| P10R | 27005 | 100.0% | 100.0% |  | n/a | no target |
| P10 | 2580 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P11 | 3168 | 20.9% | 20.9% | +0.9 | 60% | ❌ 39 pts to go |
| P12 | 8 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P13 | 11305 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `solicitation_or_tender_number`

> ceiling: SEAO's 'numero' is the organisation's own reference for the notice (SEAO data dictionary) and is reported here; sources that publish awards under a tender number only (bids&tenders, SaskTenders, BC) also carry it as the contract reference, labelled

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 44 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P01T | 139 | 2.2% | 2.2% | +0.0 | 30% | ❌ 28 pts to go |
| P01_GOLD | 626 | 51.3% | 51.3% | +0.0 | 80% | ❌ 29 pts to go |
| P02 | 403 | 66.7% | 66.7% | -0.1 | 60% | ✅ met |
| P03 | 209 | 63.6% | 63.6% | -0.3 | 80% | ❌ 16 pts to go |
| P04 | 1570 | 54.6% | 54.6% | +0.1 | 50% | ✅ met |
| P05 | 377 | 13.5% | 13.5% | +0.2 | 40% | ❌ 26 pts to go |
| P06M | 4314 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06T | 9559 | 0.3% | 0.3% | +0.1 | n/a | no target |
| P06 | 276 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P07 | 529 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P08 | 11055 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P09 | 348 | 85.6% | 85.6% | -0.5 | 50% | ✅ met |
| P10R | 27005 | 0.0% | 0.0% |  | n/a | no target |
| P10 | 2580 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P11 | 3168 | 2.6% | 2.6% | -14.9 | 40% | ❌ 37 pts to go |
| P12 | 8 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P13 | 11305 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `award_or_notice_id`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 44 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P01T | 139 | 2.9% | 2.9% | -0.4 | n/a | no target |
| P01_GOLD | 626 | 61.0% | 61.0% | -0.1 | 85% | ❌ 24 pts to go |
| P02 | 403 | 65.8% | 65.8% | +0.0 | 90% | ❌ 24 pts to go |
| P03 | 209 | 74.2% | 74.2% | -0.3 | 85% | ❌ 11 pts to go |
| P04 | 1570 | 56.4% | 56.4% | +0.1 | 85% | ❌ 29 pts to go |
| P05 | 377 | 21.5% | 21.5% | +0.4 | 50% | ❌ 28 pts to go |
| P06M | 4314 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06T | 9559 | 0.3% | 0.3% | +0.1 | n/a | no target |
| P06 | 276 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P07 | 529 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P08 | 11055 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P09 | 348 | 97.1% | 97.1% | +0.0 | 100% | 🟡 3 pts to go |
| P10R | 27005 | 0.0% | 0.0% |  | n/a | no target |
| P10 | 2580 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P11 | 3168 | 2.8% | 2.8% | -16.2 | 60% | ❌ 57 pts to go |
| P12 | 8 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P13 | 11305 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `buyer_vendor_id`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 44 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P01T | 139 | 1.4% | 1.4% | -0.8 | n/a | no target |
| P01_GOLD | 626 | 12.9% | 12.9% | -0.1 | 60% | ❌ 47 pts to go |
| P02 | 403 | 7.2% | 7.2% | +0.0 | 50% | ❌ 43 pts to go |
| P03 | 209 | 10.5% | 10.5% | -0.1 | 50% | ❌ 40 pts to go |
| P04 | 1570 | 4.3% | 4.3% | +0.0 | 40% | ❌ 36 pts to go |
| P05 | 377 | 1.3% | 1.3% | +0.0 | 20% | ❌ 19 pts to go |
| P06M | 4314 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06T | 9559 | 0.0% | 0.0% | -0.1 | n/a | no target |
| P06 | 276 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P07 | 529 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P08 | 11055 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P09 | 348 | 2.9% | 2.9% | +0.3 | 50% | ❌ 47 pts to go |
| P10R | 27005 | 0.0% | 0.0% |  | n/a | no target |
| P10 | 2580 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P11 | 3168 | 0.4% | 0.4% | -2.6 | n/a | no target |
| P12 | 8 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P13 | 11305 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `commodity_codes`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 44 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P01T | 139 | 0.7% | 0.7% | +0.7 | n/a | no target |
| P01_GOLD | 626 | 35.0% | 35.0% | -0.1 | 80% | ❌ 45 pts to go |
| P02 | 403 | 60.8% | 60.8% | +0.2 | 90% | ❌ 29 pts to go |
| P03 | 209 | 41.1% | 41.1% | -0.2 | 80% | ❌ 39 pts to go |
| P04 | 1570 | 51.3% | 51.3% | +0.0 | 85% | ❌ 34 pts to go |
| P05 | 377 | 6.1% | 6.1% | +0.1 | 50% | ❌ 44 pts to go |
| P06M | 4314 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06T | 9559 | 0.2% | 0.2% | +0.2 | n/a | no target |
| P06 | 276 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P07 | 529 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P08 | 11055 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P09 | 348 | 76.7% | 76.7% | +0.8 | 95% | ❌ 18 pts to go |
| P10R | 27005 | 0.0% | 0.0% |  | n/a | no target |
| P10 | 2580 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P11 | 3168 | 1.9% | 1.9% | -11.2 | 50% | ❌ 48 pts to go |
| P12 | 8 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P13 | 11305 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `buyer_org_codes`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 44 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P01T | 139 | 0.7% | 0.7% | -0.4 | n/a | no target |
| P01_GOLD | 626 | 8.5% | 8.5% | +0.0 | 50% | ❌ 42 pts to go |
| P02 | 403 | 7.2% | 7.2% | +0.0 | 50% | ❌ 43 pts to go |
| P03 | 209 | 2.4% | 2.4% | +0.0 | 30% | ❌ 28 pts to go |
| P04 | 1570 | 1.1% | 1.1% | +0.0 | 30% | ❌ 29 pts to go |
| P05 | 377 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06M | 4314 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06T | 9559 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06 | 276 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P07 | 529 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P08 | 11055 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P09 | 348 | 0.3% | 0.3% | +0.0 | n/a | no target |
| P10R | 27005 | 0.0% | 0.0% |  | n/a | no target |
| P10 | 2580 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P11 | 3168 | 0.1% | 0.1% | -0.7 | n/a | no target |
| P12 | 8 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P13 | 11305 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `records_with_this_vendor`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 44 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P01T | 139 | 100.0% | 100.0% | +0.0 | 60% | ✅ met |
| P01_GOLD | 626 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P02 | 403 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P03 | 209 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P04 | 1570 | 100.0% | 100.0% | +0.0 | 95% | ✅ met |
| P05 | 377 | 100.0% | 100.0% | +0.0 | 70% | ✅ met |
| P06M | 4314 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P06T | 9559 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P06 | 276 | 100.0% | 100.0% | +0.0 | 50% | ✅ met |
| P07 | 529 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P08 | 11055 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P09 | 348 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P10R | 27005 | 100.0% | 100.0% |  | n/a | no target |
| P10 | 2580 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P11 | 3168 | 100.0% | 100.0% | +0.0 | 70% | ✅ met |
| P12 | 8 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P13 | 11305 | 0.0% | 0.0% | +0.0 | n/a | no target |

## 2. vendor

### `vendor_bn9`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 44 | 34.1% | 34.1% | -65.9 | 70% | ❌ 36 pts to go |
| P01T | 139 | 56.1% | 56.1% | -24.3 | 60% | 🟡 4 pts to go |
| P01_GOLD | 626 | 77.8% | 77.8% | -0.1 | 90% | ❌ 12 pts to go |
| P02 | 403 | 67.2% | 67.2% | -0.1 | 85% | ❌ 18 pts to go |
| P03 | 209 | 82.3% | 82.3% | +0.1 | 90% | 🟡 8 pts to go |
| P04 | 1570 | 55.3% | 55.3% | -0.1 | 75% | ❌ 20 pts to go |
| P05 | 377 | 53.6% | 53.6% | +1.0 | 50% | ✅ met |
| P06M | 4314 | 2.4% | 2.4% | -72.0 | n/a | no target |
| P06T | 9559 | 25.0% | 25.0% | -35.7 | n/a | no target |
| P06 | 276 | 24.6% | 24.6% | -19.4 | 40% | ❌ 15 pts to go |
| P07 | 529 | 18.1% | 18.1% | -20.0 | 50% | ❌ 32 pts to go |
| P08 | 11055 | 12.2% | 12.2% | -28.0 | 50% | ❌ 38 pts to go |
| P09 | 348 | 55.7% | 55.7% | +1.4 | 80% | ❌ 24 pts to go |
| P10R | 27005 | 100.0% | 100.0% |  | n/a | no target |
| P10 | 2580 | 31.8% | 31.8% | -4.8 | 40% | 🟡 8 pts to go |
| P11 | 3168 | 81.3% | 81.3% | +36.6 | 60% | ✅ met |
| P12 | 8 | 62.5% | 62.5% | +9.9 | 85% | ❌ 22 pts to go |
| P13 | 11305 | 89.0% | 89.0% | -2.7 | 0% by design | — leave (by design) |

### `vendor_registered_address`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 44 | 70.5% | 70.5% | +9.4 | n/a | no target |
| P01T | 139 | 44.6% | 44.6% | -18.4 | n/a | no target |
| P01_GOLD | 626 | 74.9% | 74.9% | +0.1 | 95% | ❌ 20 pts to go |
| P02 | 403 | 84.9% | 84.9% | +0.0 | 95% | ❌ 10 pts to go |
| P03 | 209 | 78.0% | 78.0% | +0.1 | 95% | ❌ 17 pts to go |
| P04 | 1570 | 80.6% | 80.6% | -0.1 | 95% | ❌ 14 pts to go |
| P05 | 377 | 56.8% | 56.8% | +0.6 | 70% | ❌ 13 pts to go |
| P06M | 4314 | 56.4% | 56.4% | +35.6 | n/a | no target |
| P06T | 9559 | 43.2% | 43.2% | -35.0 | n/a | no target |
| P06 | 276 | 30.1% | 30.1% | -25.3 | 80% | ❌ 50 pts to go |
| P07 | 529 | 23.6% | 23.6% | -28.4 | 70% | ❌ 46 pts to go |
| P08 | 11055 | 14.6% | 14.6% | -37.8 | 70% | ❌ 55 pts to go |
| P09 | 348 | 88.5% | 88.5% | +0.0 | 100% | ❌ 12 pts to go |
| P10R | 27005 | 0.0% | 0.0% |  | n/a | no target |
| P10 | 2580 | 36.2% | 36.2% | -6.2 | 70% | ❌ 34 pts to go |
| P11 | 3168 | 65.3% | 65.3% | +10.0 | 75% | 🟡 10 pts to go |
| P12 | 8 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P13 | 11305 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `vendor_trading_name`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 44 | 20.5% | 20.5% | -29.5 | n/a | no target |
| P01T | 139 | 22.3% | 22.3% | +2.7 | n/a | no target |
| P01_GOLD | 626 | 52.4% | 52.4% | +0.0 | 60% | 🟡 8 pts to go |
| P02 | 403 | 67.2% | 67.2% | -0.1 | 60% | ✅ met |
| P03 | 209 | 64.6% | 64.6% | -0.3 | 60% | ✅ met |
| P04 | 1570 | 55.5% | 55.5% | +0.0 | 55% | ✅ met |
| P05 | 377 | 24.9% | 24.9% | -0.4 | 50% | ❌ 25 pts to go |
| P06M | 4314 | 0.7% | 0.7% | -16.6 | n/a | no target |
| P06T | 9559 | 39.6% | 39.6% | -14.0 | n/a | no target |
| P06 | 276 | 33.3% | 33.3% | -19.7 | n/a | no target |
| P07 | 529 | 27.8% | 27.8% | -18.2 | 55% | ❌ 27 pts to go |
| P08 | 11055 | 21.7% | 21.7% | -25.8 | 50% | ❌ 28 pts to go |
| P09 | 348 | 72.4% | 72.4% | +1.0 | 70% | ✅ met |
| P10R | 27005 | 0.0% | 0.0% |  | n/a | no target |
| P10 | 2580 | 47.4% | 47.4% | -4.5 | 55% | 🟡 8 pts to go |
| P11 | 3168 | 64.5% | 64.5% | +21.5 | 50% | ✅ met |
| P12 | 8 | 87.5% | 87.5% | +3.3 | n/a | no target |
| P13 | 11305 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `vendor_phone`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 44 | 25.0% | 25.0% | -36.1 | n/a | no target |
| P01T | 139 | 39.6% | 39.6% | +9.2 | n/a | no target |
| P01_GOLD | 626 | 51.8% | 51.8% | +0.0 | 70% | ❌ 18 pts to go |
| P02 | 403 | 57.1% | 57.1% | -0.1 | 70% | ❌ 13 pts to go |
| P03 | 209 | 57.4% | 57.4% | +0.2 | 70% | ❌ 13 pts to go |
| P04 | 1570 | 51.8% | 51.8% | -0.2 | 65% | ❌ 13 pts to go |
| P05 | 377 | 33.4% | 33.4% | -1.2 | 60% | ❌ 27 pts to go |
| P06M | 4314 | 1.2% | 1.2% | -29.2 | n/a | no target |
| P06T | 9559 | 25.2% | 25.2% | +21.7 | n/a | no target |
| P06 | 276 | 46.7% | 46.7% | -12.9 | 40% | ✅ met |
| P07 | 529 | 46.7% | 46.7% | -21.2 | 85% | ❌ 38 pts to go |
| P08 | 11055 | 38.1% | 38.1% | -30.0 | 85% | ❌ 47 pts to go |
| P09 | 348 | 53.7% | 53.7% | -1.7 | 85% | ❌ 31 pts to go |
| P10R | 27005 | 0.0% | 0.0% |  | n/a | no target |
| P10 | 2580 | 60.5% | 60.5% | -5.8 | 85% | ❌ 24 pts to go |
| P11 | 3168 | 11.8% | 11.8% | -43.1 | 75% | ❌ 63 pts to go |
| P12 | 8 | 12.5% | 12.5% | -3.3 | n/a | no target |
| P13 | 11305 | 100.0% | 100.0% | +0.0 | 60% | ✅ met |

### `vendor_website`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 44 | 31.8% | 31.8% | -62.6 | n/a | no target |
| P01T | 139 | 93.5% | 93.5% | +3.3 | n/a | no target |
| P01_GOLD | 626 | 89.5% | 89.5% | +0.1 | 90% | 🟡 0 pts to go |
| P02 | 403 | 87.8% | 87.8% | +0.2 | 90% | 🟡 2 pts to go |
| P03 | 209 | 90.0% | 90.0% | +0.1 | 90% | ✅ met |
| P04 | 1570 | 81.0% | 81.0% | -0.3 | 85% | 🟡 4 pts to go |
| P05 | 377 | 50.4% | 50.4% | -0.6 | 70% | ❌ 20 pts to go |
| P06M | 4314 | 2.6% | 2.6% | -65.3 | n/a | no target |
| P06T | 9559 | 91.9% | 91.9% | +14.0 | n/a | no target |
| P06 | 276 | 98.2% | 98.2% | +1.2 | 50% | ✅ met |
| P07 | 529 | 98.7% | 98.7% | +1.9 | 100% | 🟡 1 pts to go |
| P08 | 11055 | 99.0% | 99.0% | +2.9 | 100% | 🟡 1 pts to go |
| P09 | 348 | 79.6% | 79.6% | -0.2 | 100% | ❌ 20 pts to go |
| P10R | 27005 | 100.0% | 100.0% |  | n/a | no target |
| P10 | 2580 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P11 | 3168 | 99.0% | 99.0% | +6.0 | 100% | 🟡 1 pts to go |
| P12 | 8 | 25.0% | 25.0% | -17.1 | n/a | no target |
| P13 | 11305 | 100.0% | 100.0% | +0.0 | n/a | no target |

### `vendor_emails`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 44 | 20.5% | 20.5% | -29.5 | n/a | no target |
| P01T | 139 | 41.7% | 41.7% | -4.0 | n/a | no target |
| P01_GOLD | 626 | 45.7% | 45.7% | +0.0 | 70% | ❌ 24 pts to go |
| P02 | 403 | 51.6% | 51.6% | +0.1 | 75% | ❌ 23 pts to go |
| P03 | 209 | 51.7% | 51.7% | +0.3 | 75% | ❌ 23 pts to go |
| P04 | 1570 | 42.8% | 42.8% | -0.1 | 70% | ❌ 27 pts to go |
| P05 | 377 | 24.1% | 24.1% | -0.4 | 55% | ❌ 31 pts to go |
| P06M | 4314 | 0.8% | 0.8% | -15.3 | n/a | no target |
| P06T | 9559 | 18.3% | 18.3% | +15.4 | n/a | no target |
| P06 | 276 | 36.6% | 36.6% | -4.4 | n/a | no target |
| P07 | 529 | 35.5% | 35.5% | -1.4 | 70% | ❌ 34 pts to go |
| P08 | 11055 | 37.1% | 37.1% | -11.6 | 75% | ❌ 38 pts to go |
| P09 | 348 | 51.4% | 51.4% | -0.6 | 85% | ❌ 34 pts to go |
| P10R | 27005 | 0.0% | 0.0% |  | n/a | no target |
| P10 | 2580 | 46.4% | 46.4% | -4.9 | 80% | ❌ 34 pts to go |
| P11 | 3168 | 9.6% | 9.6% | -30.9 | 70% | ❌ 60 pts to go |
| P12 | 8 | 25.0% | 25.0% | -6.6 | n/a | no target |
| P13 | 11305 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `vendor_logo_url`

> ceiling: needs the vendor's website first; sites that block automated readers (robots.txt / 403) are never read

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 44 | 31.8% | 31.8% | -62.6 | n/a | no target |
| P01T | 139 | 82.0% | 82.0% | -7.1 | n/a | no target |
| P01_GOLD | 626 | 79.9% | 79.9% | +0.1 | 90% | ❌ 10 pts to go |
| P02 | 403 | 77.4% | 77.4% | +0.2 | 90% | ❌ 13 pts to go |
| P03 | 209 | 81.8% | 81.8% | +0.1 | 90% | 🟡 8 pts to go |
| P04 | 1570 | 70.6% | 70.6% | -0.3 | 85% | ❌ 14 pts to go |
| P05 | 377 | 47.7% | 47.7% | -0.7 | 75% | ❌ 27 pts to go |
| P06M | 4314 | 2.3% | 2.3% | -65.6 | n/a | no target |
| P06T | 9559 | 55.8% | 55.8% | -21.3 | n/a | no target |
| P06 | 276 | 66.7% | 66.7% | -21.9 | n/a | no target |
| P07 | 529 | 62.6% | 62.6% | -27.9 | 100% | ❌ 37 pts to go |
| P08 | 11055 | 51.6% | 51.6% | -37.4 | 100% | ❌ 48 pts to go |
| P09 | 348 | 61.2% | 61.2% | -1.3 | n/a | no target |
| P10R | 27005 | 0.0% | 0.0% |  | n/a | no target |
| P10 | 2580 | 81.6% | 81.6% | -7.4 | 100% | ❌ 18 pts to go |
| P11 | 3168 | 72.3% | 72.3% | -2.2 | n/a | no target |
| P12 | 8 | 25.0% | 25.0% | -11.8 | n/a | no target |
| P13 | 11305 | 74.5% | 74.5% | -8.2 | n/a | no target |

### `vendor_neq`

> ceiling: only Québec-registered vendors have an NEQ; the share of QC vendors is reported next to the rate

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 44 | 38.6% | 38.6% | +38.6 | n/a | no target · QC vendors: 17 rows, 100.0% filled |
| P01T | 139 | 16.5% | 16.5% | -5.2 | n/a | no target · QC vendors: 3 rows, 100.0% filled |
| P01_GOLD | 626 | 48.1% | 48.1% | +0.2 | 95% | ❌ 47 pts to go · QC vendors: 52 rows, 98.1% filled |
| P02 | 403 | 68.5% | 68.5% | -0.1 | 95% | ❌ 26 pts to go · QC vendors: 107 rows, 100.0% filled |
| P03 | 209 | 55.5% | 55.5% | -0.3 | 95% | ❌ 40 pts to go · QC vendors: 17 rows, 100.0% filled |
| P04 | 1570 | 60.1% | 60.1% | -0.1 | 95% | ❌ 35 pts to go · QC vendors: 435 rows, 98.6% filled |
| P05 | 377 | 15.1% | 15.1% | +0.3 | n/a | no target · QC vendors: 31 rows, 93.5% filled |
| P06M | 4314 | 54.5% | 54.5% | +54.5 | n/a | no target · QC vendors: 2353 rows, 100.0% filled |
| P06T | 9559 | 34.9% | 34.9% | -21.0 | n/a | no target · QC vendors: 1189 rows, 100.0% filled |
| P06 | 276 | 14.9% | 14.9% | -11.6 | n/a | no target · QC vendors: 19 rows, 100.0% filled |
| P07 | 529 | 10.4% | 10.4% | -11.0 | n/a | no target · QC vendors: 29 rows, 96.6% filled |
| P08 | 11055 | 8.4% | 8.4% | -20.5 | n/a | no target · QC vendors: 614 rows, 99.3% filled |
| P09 | 348 | 80.2% | 80.2% | +0.1 | 95% | ❌ 15 pts to go · QC vendors: 137 rows, 99.3% filled |
| P10R | 27005 | 0.0% | 0.0% |  | n/a | no target |
| P10 | 2580 | 20.0% | 20.0% | -3.4 | n/a | no target · QC vendors: 395 rows, 97.5% filled |
| P11 | 3168 | 61.3% | 61.3% | +32.0 | n/a | no target · QC vendors: 94 rows, 98.9% filled |
| P12 | 8 | 62.5% | 62.5% | -11.2 | n/a | no target · QC vendors: 1 rows, 100.0% filled |
| P13 | 11305 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `vendor_years_in_business`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 44 | 63.6% | 63.6% | +2.5 | n/a | no target · vendors with a registry record: 28 rows, 100.0% filled |
| P01T | 139 | 44.6% | 44.6% | -18.4 | n/a | no target · vendors with a registry record: 62 rows, 100.0% filled |
| P01_GOLD | 626 | 83.4% | 83.4% | -0.1 | 100% | ❌ 17 pts to go · vendors with a registry record: 522 rows, 100.0% filled |
| P02 | 403 | 89.1% | 89.1% | +0.0 | 100% | ❌ 11 pts to go · vendors with a registry record: 359 rows, 100.0% filled |
| P03 | 209 | 89.0% | 89.0% | +0.1 | 100% | ❌ 11 pts to go · vendors with a registry record: 186 rows, 100.0% filled |
| P04 | 1570 | 81.3% | 81.3% | -0.1 | 100% | ❌ 19 pts to go · vendors with a registry record: 1276 rows, 100.0% filled |
| P05 | 377 | 62.3% | 62.3% | +0.6 | n/a | no target · vendors with a registry record: 235 rows, 100.0% filled |
| P06M | 4314 | 55.3% | 55.3% | +34.5 | n/a | no target · vendors with a registry record: 2386 rows, 100.0% filled |
| P06T | 9559 | 43.2% | 43.2% | -35.0 | n/a | no target · vendors with a registry record: 4128 rows, 100.0% filled |
| P06 | 276 | 31.2% | 31.2% | -26.6 | n/a | no target · vendors with a registry record: 86 rows, 100.0% filled |
| P07 | 529 | 24.2% | 24.2% | -30.2 | n/a | no target · vendors with a registry record: 128 rows, 100.0% filled |
| P08 | 11055 | 14.9% | 14.9% | -39.4 | n/a | no target · vendors with a registry record: 1645 rows, 100.0% filled |
| P09 | 348 | 92.0% | 92.0% | +0.4 | n/a | no target · vendors with a registry record: 320 rows, 100.0% filled |
| P10R | 27005 | 0.0% | 0.0% |  | n/a | no target |
| P10 | 2580 | 37.3% | 37.3% | -6.4 | n/a | no target · vendors with a registry record: 962 rows, 100.0% filled |
| P11 | 3168 | 65.7% | 65.7% | +7.5 | n/a | no target · vendors with a registry record: 2082 rows, 100.0% filled |
| P12 | 8 | 100.0% | 100.0% | +0.0 | n/a | no target · vendors with a registry record: 8 rows, 100.0% filled |
| P13 | 11305 | 0.0% | 0.0% | +0.0 | n/a | no target |

## 3. buyer

### `buyer_legal_name_as_published`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 44 | 95.5% | 95.5% | +1.1 | 90% | ✅ met |
| P01T | 139 | 84.9% | 84.9% | -9.7 | 90% | 🟡 5 pts to go |
| P01_GOLD | 626 | 85.0% | 85.0% | +0.4 | 95% | 🟡 10 pts to go |
| P02 | 403 | 90.6% | 90.6% | +0.0 | 95% | 🟡 4 pts to go |
| P03 | 209 | 83.7% | 83.7% | +0.5 | 85% | 🟡 1 pts to go |
| P04 | 1570 | 79.2% | 79.2% | +0.4 | 90% | ❌ 11 pts to go |
| P05 | 377 | 75.9% | 75.9% | +0.1 | 75% | ✅ met |
| P06M | 4314 | 93.1% | 93.1% | +4.4 | n/a | no target |
| P06T | 9559 | 45.6% | 45.6% | -18.8 | n/a | no target |
| P06 | 276 | 52.5% | 52.5% | -4.1 | 80% | ❌ 28 pts to go |
| P07 | 529 | 45.9% | 45.9% | -7.7 | 80% | ❌ 34 pts to go |
| P08 | 11055 | 33.1% | 33.1% | -3.7 | 75% | ❌ 42 pts to go |
| P09 | 348 | 79.0% | 79.0% | -1.8 | 95% | ❌ 16 pts to go |
| P10R | 27005 | 41.0% | 41.1% |  | n/a | no target |
| P10 | 2580 | 32.9% | 32.9% | +0.9 | 70% | ❌ 37 pts to go |
| P11 | 3168 | 4.7% | 4.7% | -20.2 | 65% | ❌ 60 pts to go |
| P12 | 8 | 75.0% | 75.0% | +1.3 | 80% | 🟡 5 pts to go |
| P13 | 11305 | 70.4% | 70.5% | +17.9 | 60% | ✅ met |

### `buyer_bn_as_published`

> ceiling: a buyer's BN is public only where the buyer prints it or a public dataset carries it (CRA charities, federal grants & contributions recipients, business registries for corporations); municipalities rarely publish theirs

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 44 | 27.3% | 27.3% | -11.6 | 50% | ❌ 23 pts to go |
| P01T | 139 | 19.4% | 19.4% | -1.3 | n/a | no target |
| P01_GOLD | 626 | 20.6% | 20.6% | +0.2 | 40% | ❌ 19 pts to go |
| P02 | 403 | 21.6% | 21.6% | -0.2 | 40% | ❌ 18 pts to go |
| P03 | 209 | 26.8% | 26.8% | -0.1 | 40% | ❌ 13 pts to go |
| P04 | 1570 | 27.6% | 27.6% | +0.0 | 40% | ❌ 12 pts to go |
| P05 | 377 | 23.1% | 23.1% | +0.2 | 25% | 🟡 2 pts to go |
| P06M | 4314 | 13.6% | 13.6% | -12.0 | n/a | no target |
| P06T | 9559 | 21.0% | 21.0% | -9.9 | n/a | no target |
| P06 | 276 | 13.8% | 13.8% | +3.0 | 35% | ❌ 21 pts to go |
| P07 | 529 | 13.4% | 13.4% | +3.1 | 35% | ❌ 22 pts to go |
| P08 | 11055 | 15.4% | 15.4% | +4.3 | 35% | ❌ 20 pts to go |
| P09 | 348 | 17.0% | 17.0% | -0.1 | n/a | no target |
| P10R | 27005 | 18.8% | 18.8% |  | n/a | no target |
| P10 | 2580 | 10.0% | 10.0% | +0.4 | 30% | ❌ 20 pts to go |
| P11 | 3168 | 1.4% | 1.4% | -7.0 | n/a | no target |
| P12 | 8 | 12.5% | 12.5% | +2.0 | n/a | no target |
| P13 | 11305 | 41.0% | 41.0% | +15.1 | 30% | ✅ met |

### `buyer_address`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 44 | 100.0% | 100.0% | +5.6 | 100% | ✅ met |
| P01T | 139 | 97.1% | 97.1% | +3.6 | 100% | 🟡 3 pts to go |
| P01_GOLD | 626 | 90.3% | 90.3% | +2.6 | 100% | 🟡 10 pts to go |
| P02 | 403 | 97.5% | 97.5% | +0.7 | 100% | 🟡 2 pts to go |
| P03 | 209 | 92.8% | 92.8% | +1.0 | 100% | 🟡 7 pts to go |
| P04 | 1570 | 93.0% | 93.0% | +2.0 | 100% | 🟡 7 pts to go |
| P05 | 377 | 87.3% | 87.3% | +2.4 | 100% | ❌ 13 pts to go |
| P06M | 4314 | 99.3% | 99.3% | +27.3 | n/a | no target |
| P06T | 9559 | 85.2% | 85.2% | +5.0 | n/a | no target |
| P06 | 276 | 74.3% | 74.3% | +5.6 | 95% | ❌ 21 pts to go |
| P07 | 529 | 79.2% | 79.2% | +8.6 | 95% | ❌ 16 pts to go |
| P08 | 11055 | 73.0% | 73.0% | +6.8 | 95% | ❌ 22 pts to go |
| P09 | 348 | 96.3% | 96.3% | +0.8 | 100% | 🟡 4 pts to go |
| P10R | 27005 | 75.5% | 75.5% |  | n/a | no target |
| P10 | 2580 | 65.5% | 65.5% | +0.3 | 95% | ❌ 30 pts to go |
| P11 | 3168 | 67.0% | 67.0% | +32.6 | 80% | ❌ 13 pts to go |
| P12 | 8 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P13 | 11305 | 85.7% | 85.7% | +9.6 | 95% | 🟡 9 pts to go |

### `buyer_phone`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 44 | 95.5% | 95.5% | +6.6 | n/a | no target |
| P01T | 139 | 77.7% | 77.7% | -2.7 | n/a | no target |
| P01_GOLD | 626 | 70.4% | 70.4% | +0.2 | 90% | ❌ 20 pts to go |
| P02 | 403 | 79.7% | 79.7% | +0.0 | 95% | ❌ 15 pts to go |
| P03 | 209 | 73.2% | 73.2% | -0.4 | 95% | ❌ 22 pts to go |
| P04 | 1570 | 84.7% | 84.7% | -0.2 | 95% | ❌ 10 pts to go |
| P05 | 377 | 74.8% | 74.8% | -0.2 | 90% | ❌ 15 pts to go |
| P06M | 4314 | 95.9% | 95.9% | +12.0 | n/a | no target |
| P06T | 9559 | 70.2% | 70.2% | -7.1 | n/a | no target |
| P06 | 276 | 55.1% | 55.1% | -9.4 | 95% | ❌ 40 pts to go |
| P07 | 529 | 53.1% | 53.1% | -13.2 | 90% | ❌ 37 pts to go |
| P08 | 11055 | 51.2% | 51.2% | -23.5 | 95% | ❌ 44 pts to go |
| P09 | 348 | 87.9% | 87.9% | -1.1 | 100% | ❌ 12 pts to go |
| P10R | 27005 | 76.1% | 76.1% |  | n/a | no target |
| P10 | 2580 | 64.3% | 64.3% | -7.2 | 95% | ❌ 31 pts to go |
| P11 | 3168 | 8.2% | 8.2% | -20.7 | 75% | ❌ 67 pts to go |
| P12 | 8 | 87.5% | 87.5% | -2.0 | n/a | no target |
| P13 | 11305 | 75.3% | 75.3% | -4.0 | 95% | ❌ 20 pts to go |

### `buyer_logo_url`

> ceiling: sites that block automated readers (robots.txt / 403) are never read; an og:image that looks like a photo is labelled

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 44 | 84.1% | 84.1% | +6.3 | n/a | no target |
| P01T | 139 | 87.8% | 87.8% | -3.5 | 95% | 🟡 7 pts to go |
| P01_GOLD | 626 | 82.3% | 82.3% | +0.1 | 90% | 🟡 8 pts to go |
| P02 | 403 | 88.3% | 88.3% | -0.1 | 95% | 🟡 7 pts to go |
| P03 | 209 | 84.2% | 84.2% | -0.4 | 95% | ❌ 11 pts to go |
| P04 | 1570 | 84.3% | 84.3% | +0.1 | 90% | 🟡 6 pts to go |
| P05 | 377 | 89.7% | 89.7% | +0.1 | 95% | 🟡 5 pts to go |
| P06M | 4314 | 71.0% | 71.0% | -14.1 | n/a | no target |
| P06T | 9559 | 78.2% | 78.2% | -15.9 | n/a | no target |
| P06 | 276 | 75.7% | 75.7% | -14.7 | 100% | ❌ 24 pts to go |
| P07 | 529 | 68.1% | 68.1% | -20.0 | 100% | ❌ 32 pts to go |
| P08 | 11055 | 57.1% | 57.1% | -33.6 | 100% | ❌ 43 pts to go |
| P09 | 348 | 71.8% | 71.8% | -2.2 | n/a | no target |
| P10R | 27005 | 84.0% | 84.0% |  | n/a | no target |
| P10 | 2580 | 83.0% | 83.0% | -7.1 | 100% | ❌ 17 pts to go |
| P11 | 3168 | 10.8% | 10.8% | -25.7 | 80% | ❌ 69 pts to go |
| P12 | 8 | 87.5% | 87.5% | +3.3 | n/a | no target |
| P13 | 11305 | 76.2% | 76.2% | -8.0 | 95% | ❌ 19 pts to go |

## 4. AP

### `ap_contact_name_as_published`

> ceiling: owner 2026-11-08: the AP contact person the organisation itself names on its AP / finance page is allowed (name + role phrase, quoted); mailboxes stay organisational; many bodies publish no AP person

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 44 | 9.1% | 9.1% | -7.6 | n/a | no target |
| P01T | 139 | 18.0% | 18.0% | -5.9 | n/a | no target |
| P01_GOLD | 626 | 14.2% | 14.2% | -0.1 | 25% | ❌ 11 pts to go |
| P02 | 403 | 27.8% | 27.8% | +0.1 | 40% | ❌ 12 pts to go |
| P03 | 209 | 10.5% | 10.5% | -0.1 | 20% | 🟡 10 pts to go |
| P04 | 1570 | 7.4% | 7.4% | +0.0 | 20% | ❌ 13 pts to go |
| P05 | 377 | 4.0% | 4.0% | +0.1 | 15% | ❌ 11 pts to go |
| P06M | 4314 | 0.5% | 0.5% | -4.3 | n/a | no target |
| P06T | 9559 | 1.3% | 1.3% | -1.9 | n/a | no target |
| P06 | 276 | 5.8% | 5.8% | +0.4 | n/a | no target |
| P07 | 529 | 7.6% | 7.6% | +1.3 | n/a | no target |
| P08 | 11055 | 0.5% | 0.5% | -0.5 | n/a | no target |
| P09 | 348 | 7.5% | 7.5% | -0.4 | n/a | no target |
| P10R | 27005 | 0.6% | 0.6% |  | n/a | no target |
| P10 | 2580 | 1.1% | 1.1% | -0.2 | n/a | no target |
| P11 | 3168 | 0.4% | 0.4% | -2.1 | n/a | no target |
| P12 | 8 | 0.0% | 0.0% | -10.5 | n/a | no target |
| P13 | 11305 | 0.8% | 0.8% | +0.2 | n/a | no target |

### `ap_phone`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 44 | 45.5% | 45.5% | +6.6 | n/a | no target |
| P01T | 139 | 38.1% | 38.1% | +3.3 | 70% | ❌ 32 pts to go |
| P01_GOLD | 626 | 43.3% | 43.3% | +0.0 | 80% | ❌ 37 pts to go |
| P02 | 403 | 64.3% | 64.3% | +0.2 | 90% | ❌ 26 pts to go |
| P03 | 209 | 23.4% | 23.4% | +0.3 | 60% | ❌ 37 pts to go |
| P04 | 1570 | 50.5% | 50.5% | +0.0 | 85% | ❌ 34 pts to go |
| P05 | 377 | 13.3% | 13.3% | +0.3 | 50% | ❌ 37 pts to go |
| P06M | 4314 | 0.5% | 0.5% | -6.0 | n/a | no target |
| P06T | 9559 | 1.6% | 1.6% | -1.1 | n/a | no target |
| P06 | 276 | 21.4% | 21.4% | +3.3 | n/a | no target |
| P07 | 529 | 17.2% | 17.2% | -1.8 | n/a | no target |
| P08 | 11055 | 0.2% | 0.2% | -0.4 | n/a | no target |
| P09 | 348 | 78.7% | 78.7% | -1.9 | 95% | ❌ 16 pts to go |
| P10R | 27005 | 0.8% | 0.8% |  | n/a | no target |
| P10 | 2580 | 2.9% | 2.9% | -0.2 | n/a | no target |
| P11 | 3168 | 9.9% | 9.9% | -19.4 | n/a | no target |
| P12 | 8 | 25.0% | 25.0% | -6.6 | n/a | no target |
| P13 | 11305 | 1.1% | 1.1% | +0.1 | n/a | no target |

### `invoice_mailing_address`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 44 | 4.5% | 4.5% | +4.5 | n/a | no target |
| P01T | 139 | 16.5% | 16.5% | +0.2 | n/a | no target |
| P01_GOLD | 626 | 33.9% | 33.9% | -0.1 | 70% | ❌ 36 pts to go |
| P02 | 403 | 44.4% | 44.4% | +0.1 | 75% | ❌ 31 pts to go |
| P03 | 209 | 23.4% | 23.4% | +0.3 | 55% | ❌ 32 pts to go |
| P04 | 1570 | 50.5% | 50.5% | +0.0 | 75% | ❌ 24 pts to go |
| P05 | 377 | 11.9% | 11.9% | +0.2 | 50% | ❌ 38 pts to go |
| P06M | 4314 | 0.2% | 0.2% | -1.6 | n/a | no target |
| P06T | 9559 | 1.1% | 1.1% | -0.4 | n/a | no target |
| P06 | 276 | 12.7% | 12.7% | +2.5 | n/a | no target |
| P07 | 529 | 8.5% | 8.5% | -1.8 | n/a | no target |
| P08 | 11055 | 0.2% | 0.2% | -0.3 | n/a | no target |
| P09 | 348 | 75.9% | 75.9% | -1.8 | 95% | ❌ 19 pts to go |
| P10R | 27005 | 0.7% | 0.7% |  | n/a | no target |
| P10 | 2580 | 1.7% | 1.7% | -0.1 | n/a | no target |
| P11 | 3168 | 9.9% | 9.9% | -19.0 | n/a | no target |
| P12 | 8 | 12.5% | 12.5% | -3.3 | n/a | no target |
| P13 | 11305 | 0.7% | 0.7% | +0.1 | n/a | no target |

### `invoicing_requirements`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 44 | 9.1% | 9.1% | -7.6 | n/a | no target |
| P01T | 139 | 14.4% | 14.4% | -5.2 | n/a | no target |
| P01_GOLD | 626 | 57.8% | 58.0% | -0.1 | 80% | ❌ 22 pts to go |
| P02 | 403 | 52.4% | 52.6% | +0.2 | 75% | ❌ 23 pts to go |
| P03 | 209 | 45.5% | 45.5% | +0.3 | 70% | ❌ 24 pts to go |
| P04 | 1570 | 48.8% | 49.9% | +0.1 | 70% | ❌ 21 pts to go |
| P05 | 377 | 16.7% | 16.7% | +0.3 | 50% | ❌ 33 pts to go |
| P06M | 4314 | 0.6% | 0.6% | -3.6 | n/a | no target |
| P06T | 9559 | 0.9% | 0.9% | -0.7 | n/a | no target |
| P06 | 276 | 18.5% | 18.5% | -5.6 | n/a | no target |
| P07 | 529 | 3.2% | 3.2% | -2.0 | n/a | no target |
| P08 | 11055 | 0.4% | 0.4% | -0.6 | n/a | no target |
| P09 | 348 | 44.0% | 44.3% | -0.1 | 80% | ❌ 36 pts to go |
| P10R | 27005 | 0.2% | 0.2% |  | n/a | no target |
| P10 | 2580 | 1.4% | 1.5% | -0.1 | n/a | no target |
| P11 | 3168 | 2.8% | 2.8% | -13.9 | n/a | no target |
| P12 | 8 | 25.0% | 25.0% | -6.6 | n/a | no target |
| P13 | 11305 | 0.4% | 0.4% | +0.1 | n/a | no target |

### `payment_terms_as_published`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 44 | 15.9% | 15.9% | -23.0 | n/a | no target |
| P01T | 139 | 41.0% | 41.0% | -15.5 | 60% | ❌ 19 pts to go |
| P01_GOLD | 626 | 63.6% | 63.6% | +0.1 | 70% | 🟡 6 pts to go |
| P02 | 403 | 43.7% | 43.7% | -0.1 | 50% | 🟡 6 pts to go |
| P03 | 209 | 55.0% | 55.0% | -0.3 | 55% | ✅ met |
| P04 | 1570 | 22.9% | 22.9% | +0.0 | 40% | ❌ 17 pts to go |
| P05 | 377 | 17.8% | 17.8% | +0.4 | 40% | ❌ 22 pts to go |
| P06M | 4314 | 0.5% | 0.5% | -16.2 | n/a | no target |
| P06T | 9559 | 3.4% | 3.4% | -9.1 | n/a | no target |
| P06 | 276 | 18.8% | 18.8% | -11.9 | n/a | no target |
| P07 | 529 | 7.9% | 7.9% | -8.4 | n/a | no target |
| P08 | 11055 | 1.5% | 1.5% | -3.2 | n/a | no target |
| P09 | 348 | 5.5% | 5.5% | -0.3 | n/a | no target |
| P10R | 27005 | 0.3% | 0.3% |  | n/a | no target |
| P10 | 2580 | 3.7% | 3.7% | -0.2 | n/a | no target |
| P11 | 3168 | 2.0% | 2.0% | -5.6 | n/a | no target |
| P12 | 8 | 25.0% | 25.0% | +9.2 | n/a | no target |
| P13 | 11305 | 0.2% | 0.2% | -0.1 | n/a | no target |

### `po_required_as_published`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 44 | 18.2% | 18.2% | -26.2 | n/a | no target |
| P01T | 139 | 48.9% | 48.9% | -20.7 | 65% | ❌ 16 pts to go |
| P01_GOLD | 626 | 69.2% | 69.2% | +0.0 | 70% | 🟡 1 pts to go |
| P02 | 403 | 26.1% | 26.1% | -0.1 | 50% | ❌ 24 pts to go |
| P03 | 209 | 56.0% | 56.0% | -0.2 | 60% | 🟡 4 pts to go |
| P04 | 1570 | 9.9% | 9.9% | +0.0 | 40% | ❌ 30 pts to go |
| P05 | 377 | 21.5% | 21.5% | +0.1 | 45% | ❌ 24 pts to go |
| P06M | 4314 | 0.2% | 0.2% | -6.9 | n/a | no target |
| P06T | 9559 | 1.2% | 1.2% | -3.1 | n/a | no target |
| P06 | 276 | 32.6% | 32.6% | -15.6 | n/a | no target |
| P07 | 529 | 11.0% | 11.0% | -12.8 | n/a | no target |
| P08 | 11055 | 0.7% | 0.7% | -1.7 | n/a | no target |
| P09 | 348 | 9.2% | 9.2% | +0.5 | n/a | no target |
| P10R | 27005 | 0.1% | 0.1% |  | n/a | no target |
| P10 | 2580 | 2.0% | 2.0% | -0.1 | n/a | no target |
| P11 | 3168 | 1.0% | 1.0% | -5.8 | n/a | no target |
| P12 | 8 | 12.5% | 12.5% | +2.0 | n/a | no target |
| P13 | 11305 | 0.3% | 0.3% | +0.1 | n/a | no target |

### `invoice_portal_url`

> ceiling: only portals the buyer names on its own pages; informational tax-authority links are not portals

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 44 | 4.5% | 4.5% | -6.6 | n/a | no target |
| P01T | 139 | 30.2% | 30.2% | -14.4 | n/a | no target |
| P01_GOLD | 626 | 49.7% | 49.7% | -0.1 | 50% | 🟡 0 pts to go |
| P02 | 403 | 42.7% | 42.7% | +0.1 | n/a | no target |
| P03 | 209 | 58.4% | 58.4% | -0.3 | 60% | 🟡 2 pts to go |
| P04 | 1570 | 26.3% | 26.3% | -0.1 | n/a | no target |
| P05 | 377 | 16.4% | 16.4% | -0.3 | n/a | no target |
| P06M | 4314 | 0.4% | 0.4% | -3.8 | n/a | no target |
| P06T | 9559 | 1.3% | 1.3% | -2.7 | n/a | no target |
| P06 | 276 | 24.3% | 24.3% | -11.2 | n/a | no target |
| P07 | 529 | 10.0% | 10.0% | -8.7 | n/a | no target |
| P08 | 11055 | 0.5% | 0.5% | -1.0 | n/a | no target |
| P09 | 348 | 19.5% | 19.5% | +0.6 | n/a | no target |
| P10R | 27005 | 0.3% | 0.3% |  | n/a | no target |
| P10 | 2580 | 2.3% | 2.3% | -0.1 | n/a | no target |
| P11 | 3168 | 1.1% | 1.1% | -6.7 | n/a | no target |
| P12 | 8 | 12.5% | 12.5% | -8.6 | n/a | no target |
| P13 | 11305 | 0.6% | 0.6% | +0.2 | n/a | no target |

### `buyer_payment_method_preference`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 44 | 9.1% | 9.1% | -18.7 | 15% | 🟡 6 pts to go |
| P01T | 139 | 20.9% | 20.9% | -8.4 | 15% | ✅ met |
| P01_GOLD | 626 | 35.3% | 35.3% | +0.2 | 40% | 🟡 5 pts to go |
| P02 | 403 | 13.6% | 13.9% | -0.3 | 25% | ❌ 11 pts to go |
| P03 | 209 | 21.5% | 21.5% | -0.1 | 25% | 🟡 4 pts to go |
| P04 | 1570 | 5.2% | 5.2% | +0.0 | 15% | 🟡 10 pts to go |
| P05 | 377 | 7.7% | 7.7% | -0.4 | 15% | 🟡 7 pts to go |
| P06M | 4314 | 0.7% | 0.7% | -5.3 | 15% | ❌ 14 pts to go |
| P06T | 9559 | 0.6% | 0.6% | -0.9 | 15% | ❌ 14 pts to go |
| P06 | 276 | 8.0% | 8.0% | -2.2 | 15% | 🟡 7 pts to go |
| P07 | 529 | 3.6% | 3.6% | -3.1 | 15% | ❌ 11 pts to go |
| P08 | 11055 | 0.3% | 0.3% | -0.6 | 15% | ❌ 15 pts to go |
| P09 | 348 | 0.9% | 0.9% | +0.1 | 15% | ❌ 14 pts to go |
| P10R | 27005 | 0.6% | 0.6% |  | 15% | ❌ 14 pts to go |
| P10 | 2580 | 1.5% | 1.5% | +0.1 | 15% | ❌ 14 pts to go |
| P11 | 3168 | 0.2% | 0.2% | -1.1 | 15% | ❌ 15 pts to go |
| P12 | 8 | 0.0% | 0.0% | +0.0 | 15% | ❌ 15 pts to go |
| P13 | 11305 | 0.5% | 0.5% | +0.0 | 15% | ❌ 14 pts to go |

### `buyer_tax_exempt_status`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 44 | 4.5% | 4.5% | -6.6 | 15% | ❌ 10 pts to go |
| P01T | 139 | 23.0% | 23.0% | -9.6 | 25% | 🟡 2 pts to go |
| P01_GOLD | 626 | 29.1% | 29.1% | -0.1 | 25% | ✅ met |
| P02 | 403 | 28.0% | 28.0% | +0.0 | 15% | ✅ met |
| P03 | 209 | 25.8% | 25.8% | -0.2 | 15% | ✅ met |
| P04 | 1570 | 8.1% | 8.1% | -0.1 | 15% | 🟡 7 pts to go |
| P05 | 377 | 11.9% | 11.9% | -0.1 | 15% | 🟡 3 pts to go |
| P06M | 4314 | 0.1% | 0.1% | -2.3 | 15% | ❌ 15 pts to go |
| P06T | 9559 | 0.8% | 0.8% | -1.9 | 15% | ❌ 14 pts to go |
| P06 | 276 | 7.6% | 7.6% | -4.4 | 15% | 🟡 7 pts to go |
| P07 | 529 | 3.8% | 3.8% | -3.7 | 15% | ❌ 11 pts to go |
| P08 | 11055 | 0.3% | 0.3% | -0.7 | 15% | ❌ 15 pts to go |
| P09 | 348 | 0.9% | 0.9% | +0.1 | 15% | ❌ 14 pts to go |
| P10R | 27005 | 0.1% | 0.1% |  | 15% | ❌ 15 pts to go |
| P10 | 2580 | 1.3% | 1.3% | -0.1 | 15% | ❌ 14 pts to go |
| P11 | 3168 | 0.8% | 0.8% | -4.3 | 15% | ❌ 14 pts to go |
| P12 | 8 | 25.0% | 25.0% | -1.3 | 15% | ✅ met |
| P13 | 11305 | 0.1% | 0.1% | +0.0 | 15% | ❌ 15 pts to go |

### `buyer_ap_cycle_published`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 44 | 2.3% | 2.3% | -3.3 | 20% | ❌ 18 pts to go |
| P01T | 139 | 7.2% | 7.2% | -2.6 | 20% | ❌ 13 pts to go |
| P01_GOLD | 626 | 4.3% | 4.3% | +0.0 | 20% | ❌ 16 pts to go |
| P02 | 403 | 1.5% | 1.5% | +0.0 | 20% | ❌ 18 pts to go |
| P03 | 209 | 1.9% | 1.9% | +0.0 | 20% | ❌ 18 pts to go |
| P04 | 1570 | 1.0% | 1.0% | +0.0 | 20% | ❌ 19 pts to go |
| P05 | 377 | 1.1% | 1.1% | +0.1 | 20% | ❌ 19 pts to go |
| P06M | 4314 | 0.0% | 0.0% | +0.0 | 20% | ❌ 20 pts to go |
| P06T | 9559 | 0.1% | 0.1% | -0.1 | 20% | ❌ 20 pts to go |
| P06 | 276 | 1.8% | 1.8% | -1.8 | 20% | ❌ 18 pts to go |
| P07 | 529 | 0.6% | 0.6% | -0.2 | 20% | ❌ 19 pts to go |
| P08 | 11055 | 0.0% | 0.0% | -0.2 | 20% | ❌ 20 pts to go |
| P09 | 348 | 0.0% | 0.0% | +0.0 | 20% | ❌ 20 pts to go |
| P10R | 27005 | 0.0% | 0.0% |  | 20% | ❌ 20 pts to go |
| P10 | 2580 | 0.3% | 0.3% | +0.0 | 20% | ❌ 20 pts to go |
| P11 | 3168 | 0.1% | 0.1% | -0.5 | 20% | ❌ 20 pts to go |
| P12 | 8 | 0.0% | 0.0% | +0.0 | 20% | ❌ 20 pts to go |
| P13 | 11305 | 0.0% | 0.0% | +0.0 | 20% | ❌ 20 pts to go |

### `buyer_esignature_preference`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 44 | 2.3% | 2.3% | -3.3 | 15% | ❌ 13 pts to go |
| P01T | 139 | 5.0% | 5.0% | -2.6 | 15% | 🟡 10 pts to go |
| P01_GOLD | 626 | 10.5% | 10.5% | -0.1 | 15% | 🟡 4 pts to go |
| P02 | 403 | 13.4% | 13.4% | +0.0 | 15% | 🟡 2 pts to go |
| P03 | 209 | 23.9% | 23.9% | -0.1 | 15% | ✅ met |
| P04 | 1570 | 4.5% | 4.5% | -0.1 | 15% | ❌ 10 pts to go |
| P05 | 377 | 2.9% | 2.9% | +0.0 | 15% | ❌ 12 pts to go |
| P06M | 4314 | 0.2% | 0.2% | -2.2 | 15% | ❌ 15 pts to go |
| P06T | 9559 | 0.4% | 0.4% | -1.0 | 15% | ❌ 15 pts to go |
| P06 | 276 | 3.6% | 3.6% | -1.8 | 15% | ❌ 11 pts to go |
| P07 | 529 | 1.9% | 1.9% | -1.7 | 15% | ❌ 13 pts to go |
| P08 | 11055 | 0.2% | 0.2% | -0.5 | 15% | ❌ 15 pts to go |
| P09 | 348 | 0.6% | 0.6% | +0.1 | 15% | ❌ 14 pts to go |
| P10R | 27005 | 0.1% | 0.1% |  | 15% | ❌ 15 pts to go |
| P10 | 2580 | 0.7% | 0.7% | -0.1 | 15% | ❌ 14 pts to go |
| P11 | 3168 | 0.3% | 0.3% | -1.8 | 15% | ❌ 15 pts to go |
| P12 | 8 | 0.0% | 0.0% | -5.3 | 15% | ❌ 15 pts to go |
| P13 | 11305 | 0.1% | 0.1% | +0.0 | 15% | ❌ 15 pts to go |

### `ap_system_hint`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 44 | 6.8% | 6.8% | -4.3 | 20% | ❌ 13 pts to go |
| P01T | 139 | 28.1% | 28.1% | -13.2 | 40% | ❌ 12 pts to go |
| P01_GOLD | 626 | 45.7% | 45.7% | -0.1 | 40% | ✅ met |
| P02 | 403 | 48.6% | 48.6% | +0.1 | 20% | ✅ met |
| P03 | 209 | 55.5% | 55.5% | -0.3 | 35% | ✅ met |
| P04 | 1570 | 30.2% | 30.2% | -0.1 | 20% | ✅ met |
| P05 | 377 | 16.4% | 16.4% | -0.3 | 20% | 🟡 4 pts to go |
| P06M | 4314 | 0.5% | 0.5% | -3.7 | 20% | ❌ 20 pts to go |
| P06T | 9559 | 1.7% | 1.7% | -2.8 | 20% | ❌ 18 pts to go |
| P06 | 276 | 24.3% | 24.3% | -11.2 | 20% | ✅ met |
| P07 | 529 | 8.7% | 8.7% | -6.0 | 20% | ❌ 11 pts to go |
| P08 | 11055 | 0.8% | 0.8% | -1.5 | 20% | ❌ 19 pts to go |
| P09 | 348 | 19.8% | 19.8% | -2.2 | 20% | 🟡 0 pts to go |
| P10R | 27005 | 0.4% | 0.4% |  | 20% | ❌ 20 pts to go |
| P10 | 2580 | 2.4% | 2.4% | -0.2 | 20% | ❌ 18 pts to go |
| P11 | 3168 | 1.3% | 1.3% | -6.7 | 20% | ❌ 19 pts to go |
| P12 | 8 | 12.5% | 12.5% | -3.3 | 20% | 🟡 8 pts to go |
| P13 | 11305 | 0.8% | 0.8% | +0.2 | 20% | ❌ 19 pts to go |

## 5. contract

### `contract_value`

> ceiling: rows proven by a lobbying filing, a news release, an auditor appointment, a customer story or a vendor's client list have no contract value by nature (≈17 % of P01 Gold); bids&tenders awards now carry the awarded bidder's submitted price when no award value was published

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 44 | 4.5% | 4.5% | +4.5 | n/a | no target |
| P01T | 139 | 0.7% | 0.7% | -0.4 | n/a | no target |
| P01_GOLD | 626 | 69.6% | 69.6% | -0.1 | 95% | ❌ 25 pts to go |
| P02 | 403 | 73.2% | 73.2% | -0.1 | 95% | ❌ 22 pts to go |
| P03 | 209 | 67.0% | 67.0% | -0.3 | 90% | ❌ 23 pts to go |
| P04 | 1570 | 58.5% | 58.5% | +0.1 | 85% | ❌ 26 pts to go |
| P05 | 377 | 35.3% | 35.3% | +0.4 | 75% | ❌ 40 pts to go |
| P06M | 4314 | 8.0% | 8.0% | +8.0 | n/a | no target |
| P06T | 9559 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06 | 276 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P07 | 529 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P08 | 11055 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P09 | 348 | 90.2% | 90.2% | -0.6 | 100% | 🟡 10 pts to go |
| P10R | 27005 | 0.0% | 0.0% |  | n/a | no target |
| P10 | 2580 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P11 | 3168 | 2.8% | 2.8% | -16.0 | 60% | ❌ 57 pts to go |
| P12 | 8 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P13 | 11305 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `currency`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 44 | 4.5% | 4.5% | +4.5 | n/a | no target |
| P01T | 139 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P01_GOLD | 626 | 72.8% | 72.8% | -0.1 | 100% | ❌ 27 pts to go |
| P02 | 403 | 77.2% | 77.2% | +0.0 | 100% | ❌ 23 pts to go |
| P03 | 209 | 74.2% | 74.2% | -0.3 | n/a | no target |
| P04 | 1570 | 60.1% | 60.1% | +0.1 | 95% | ❌ 35 pts to go |
| P05 | 377 | 31.6% | 31.6% | +0.4 | 80% | ❌ 48 pts to go |
| P06M | 4314 | 8.0% | 8.0% | +8.0 | n/a | no target |
| P06T | 9559 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06 | 276 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P07 | 529 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P08 | 11055 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P09 | 348 | 93.1% | 93.1% | -0.3 | 100% | 🟡 7 pts to go |
| P10R | 27005 | 0.0% | 0.0% |  | n/a | no target |
| P10 | 2580 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P11 | 3168 | 3.0% | 3.0% | -17.0 | n/a | no target |
| P12 | 8 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P13 | 11305 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `start_date`

> ceiling: most award notices publish an award date, not a start date; start_date carries the signature date when the source gives one, labelled

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 44 | 61.4% | 61.4% | +61.4 | n/a | no target |
| P01T | 139 | 0.7% | 0.7% | -0.4 | n/a | no target |
| P01_GOLD | 626 | 51.8% | 51.8% | -0.1 | 85% | ❌ 33 pts to go |
| P02 | 403 | 66.7% | 66.7% | -0.1 | 90% | ❌ 23 pts to go |
| P03 | 209 | 54.5% | 54.5% | -0.3 | 85% | ❌ 30 pts to go |
| P04 | 1570 | 64.3% | 64.3% | +0.2 | 90% | ❌ 26 pts to go |
| P05 | 377 | 35.0% | 35.0% | -0.2 | 75% | ❌ 40 pts to go |
| P06M | 4314 | 93.1% | 93.1% | +93.1 | n/a | no target |
| P06T | 9559 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06 | 276 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P07 | 529 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P08 | 11055 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P09 | 348 | 86.2% | 86.2% | +0.6 | 95% | 🟡 9 pts to go |
| P10R | 27005 | 0.0% | 0.0% |  | n/a | no target |
| P10 | 2580 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P11 | 3168 | 2.6% | 2.6% | -14.7 | n/a | no target |
| P12 | 8 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P13 | 11305 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `end_date`

> ceiling: an inferred end (award date + published duration) is labelled as such; sources without a duration leave end_date empty — the honest ceiling. P09 is BY DEFINITION the rows whose end date is not published (older SEAO contracts with no closing notice): its end_date / duration targets cannot be met without inventing a date

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 44 | 65.9% | 65.9% | +65.9 | n/a | no target |
| P01T | 139 | 0.7% | 0.7% | -0.4 | n/a | no target |
| P01_GOLD | 626 | 51.9% | 51.9% | -0.2 | 85% | ❌ 33 pts to go |
| P02 | 403 | 61.0% | 61.0% | -0.1 | 90% | ❌ 29 pts to go |
| P03 | 209 | 56.0% | 56.0% | -0.2 | 85% | ❌ 29 pts to go |
| P04 | 1570 | 54.3% | 54.3% | +0.0 | 90% | ❌ 36 pts to go |
| P05 | 377 | 41.4% | 41.4% | -0.3 | 75% | ❌ 34 pts to go |
| P06M | 4314 | 87.6% | 87.6% | +87.6 | n/a | no target |
| P06T | 9559 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06 | 276 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P07 | 529 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P08 | 11055 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P09 | 348 | 0.3% | 0.3% | +0.0 | 95% | ❌ 95 pts to go |
| P10R | 27005 | 0.0% | 0.0% |  | n/a | no target |
| P10 | 2580 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P11 | 3168 | 2.1% | 2.1% | -12.0 | n/a | no target |
| P12 | 8 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P13 | 11305 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `contract_title`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 44 | 65.9% | 65.9% | +65.9 | n/a | no target |
| P01T | 139 | 86.3% | 86.3% | +4.8 | n/a | no target |
| P01_GOLD | 626 | 85.6% | 85.6% | -0.1 | 100% | ❌ 14 pts to go |
| P02 | 403 | 81.6% | 81.6% | -0.1 | 100% | ❌ 18 pts to go |
| P03 | 209 | 92.3% | 92.3% | +0.0 | n/a | no target |
| P04 | 1570 | 72.7% | 72.7% | +0.1 | 95% | ❌ 22 pts to go |
| P05 | 377 | 75.3% | 75.3% | -0.2 | 95% | ❌ 20 pts to go |
| P06M | 4314 | 96.7% | 96.7% | +96.1 | n/a | no target |
| P06T | 9559 | 84.6% | 84.6% | +1.2 | n/a | no target |
| P06 | 276 | 43.1% | 43.1% | -32.8 | n/a | no target |
| P07 | 529 | 34.0% | 34.0% | -43.0 | n/a | no target |
| P08 | 11055 | 21.5% | 21.6% | -63.4 | n/a | no target |
| P09 | 348 | 98.9% | 98.9% | -0.1 | 100% | 🟡 1 pts to go |
| P10R | 27005 | 100.0% | 100.0% |  | n/a | no target |
| P10 | 2580 | 86.4% | 86.4% | -12.0 | n/a | no target |
| P11 | 3168 | 32.8% | 32.8% | -57.1 | n/a | no target |
| P12 | 8 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P13 | 11305 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `contract_description`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 44 | 65.9% | 65.9% | +65.9 | n/a | no target |
| P01T | 139 | 86.3% | 86.3% | +4.8 | n/a | no target |
| P01_GOLD | 626 | 88.8% | 88.8% | -0.1 | 100% | ❌ 11 pts to go |
| P02 | 403 | 82.9% | 83.1% | +0.0 | 100% | ❌ 17 pts to go |
| P03 | 209 | 93.8% | 93.8% | +0.0 | n/a | no target |
| P04 | 1570 | 79.2% | 79.2% | +0.2 | 95% | ❌ 16 pts to go |
| P05 | 377 | 89.7% | 89.7% | -0.4 | 70% | ✅ met |
| P06M | 4314 | 96.7% | 96.7% | +96.1 | n/a | no target |
| P06T | 9559 | 84.6% | 84.6% | +1.2 | n/a | no target |
| P06 | 276 | 43.1% | 43.1% | -32.8 | n/a | no target |
| P07 | 529 | 34.0% | 34.0% | -43.0 | n/a | no target |
| P08 | 11055 | 21.5% | 21.6% | -63.4 | n/a | no target |
| P09 | 348 | 98.9% | 98.9% | -0.1 | 100% | 🟡 1 pts to go |
| P10R | 27005 | 100.0% | 100.0% |  | n/a | no target |
| P10 | 2580 | 86.4% | 86.4% | -12.0 | n/a | no target |
| P11 | 3168 | 32.9% | 32.9% | -57.4 | n/a | no target |
| P12 | 8 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P13 | 11305 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `number_of_bids`

> ceiling: published by some portals only (bids&tenders submission lists, Biddingo bidder lists); federal proactive disclosure does not publish bid counts

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 44 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P01T | 139 | 0.7% | 0.7% | -0.4 | n/a | no target · rows from a source that publishes bids: 4 rows, 25.0% filled |
| P01_GOLD | 626 | 17.3% | 17.3% | +0.0 | 60% | ❌ 43 pts to go · rows from a source that publishes bids: 367 rows, 29.4% filled |
| P02 | 403 | 13.2% | 13.2% | +0.1 | n/a | no target · rows from a source that publishes bids: 294 rows, 18.0% filled |
| P03 | 209 | 16.3% | 16.3% | +0.0 | n/a | no target · rows from a source that publishes bids: 140 rows, 24.3% filled |
| P04 | 1570 | 3.7% | 3.7% | +0.0 | n/a | no target · rows from a source that publishes bids: 878 rows, 6.6% filled |
| P05 | 377 | 3.4% | 3.4% | +0.0 | n/a | no target · rows from a source that publishes bids: 53 rows, 24.5% filled |
| P06M | 4314 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06T | 9559 | 0.0% | 0.0% | -0.1 | n/a | no target · rows from a source that publishes bids: 34 rows, 5.9% filled |
| P06 | 276 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P07 | 529 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P08 | 11055 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P09 | 348 | 3.4% | 3.4% | +0.3 | n/a | no target · rows from a source that publishes bids: 336 rows, 3.6% filled |
| P10R | 27005 | 0.0% | 0.0% |  | n/a | no target |
| P10 | 2580 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P11 | 3168 | 0.4% | 0.4% | -2.3 | n/a | no target · rows from a source that publishes bids: 91 rows, 14.3% filled |
| P12 | 8 | 0.0% | 0.0% | +0.0 | n/a | no target · rows from a source that publishes bids: 8 rows, 0.0% filled |
| P13 | 11305 | 0.0% | 0.0% | +0.0 | n/a | no target |

## 6. history

### `average_contract_duration_days`

> ceiling: needs two dates (or a published term) on the buyer's records; P09 rows (end date unpublished by definition) and buyers whose sources publish award dates only have no honest duration

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 44 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P01T | 139 | 0.0% | 97.1% | +0.0 | n/a | no target |
| P01_GOLD | 626 | 53.0% | 82.4% | -0.2 | 90% | ❌ 37 pts to go |
| P02 | 403 | 61.0% | 85.6% | -0.1 | 90% | ❌ 29 pts to go |
| P03 | 209 | 56.0% | 75.6% | -0.2 | 90% | ❌ 34 pts to go |
| P04 | 1570 | 45.4% | 85.6% | +0.1 | 90% | ❌ 45 pts to go |
| P05 | 377 | 0.0% | 80.6% | +0.0 | 90% | ❌ 90 pts to go |
| P06M | 4314 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P06T | 9559 | 0.0% | 99.6% | +0.0 | n/a | no target |
| P06 | 276 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P07 | 529 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P08 | 11055 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P09 | 348 | 2.3% | 3.7% | +0.2 | 90% | ❌ 88 pts to go |
| P10R | 27005 | 0.0% | 100.0% |  | n/a | no target |
| P10 | 2580 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P11 | 3168 | 1.9% | 98.6% | -10.8 | n/a | no target |
| P12 | 8 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P13 | 11305 | 0.0% | 100.0% | +0.0 | n/a | no target |

### `commodity_distribution_top3`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 44 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P01T | 139 | 0.7% | 97.8% | +0.7 | n/a | no target |
| P01_GOLD | 626 | 25.9% | 55.3% | -0.1 | 90% | ❌ 64 pts to go |
| P02 | 403 | 60.0% | 84.6% | +0.1 | n/a | no target |
| P03 | 209 | 30.6% | 50.2% | -0.2 | n/a | no target |
| P04 | 1570 | 49.7% | 89.9% | +0.0 | n/a | no target |
| P05 | 377 | 0.5% | 81.2% | +0.0 | n/a | no target |
| P06M | 4314 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P06T | 9559 | 0.2% | 99.8% | +0.2 | n/a | no target |
| P06 | 276 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P07 | 529 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P08 | 11055 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P09 | 348 | 43.7% | 45.1% | -0.7 | n/a | no target |
| P10R | 27005 | 0.0% | 100.0% |  | n/a | no target |
| P10 | 2580 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P11 | 3168 | 1.7% | 98.5% | -9.9 | n/a | no target |
| P12 | 8 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P13 | 11305 | 0.0% | 100.0% | +0.0 | n/a | no target |

### `year_over_year_spend_trend`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 44 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P01T | 139 | 2.2% | 99.3% | +0.0 | n/a | no target |
| P01_GOLD | 626 | 51.6% | 81.0% | +0.0 | 95% | ❌ 43 pts to go |
| P02 | 403 | 65.8% | 90.3% | +0.2 | n/a | no target |
| P03 | 209 | 58.9% | 78.5% | -0.2 | n/a | no target |
| P04 | 1570 | 50.3% | 90.5% | +0.0 | n/a | no target |
| P05 | 377 | 5.3% | 85.9% | +0.1 | n/a | no target |
| P06M | 4314 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P06T | 9559 | 0.2% | 99.9% | +0.2 | n/a | no target |
| P06 | 276 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P07 | 529 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P08 | 11055 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P09 | 348 | 66.4% | 67.8% | -1.1 | n/a | no target |
| P10R | 27005 | 0.0% | 100.0% |  | n/a | no target |
| P10 | 2580 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P11 | 3168 | 1.9% | 98.6% | -10.8 | n/a | no target |
| P12 | 8 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P13 | 11305 | 0.0% | 100.0% | +0.0 | n/a | no target |

## 7. mail security

### `mta_sts`

> ceiling: DNS-only check; 'no record' counts as checked

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 44 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P01T | 139 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P01_GOLD | 626 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P02 | 403 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P03 | 209 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P04 | 1570 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P05 | 377 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P06M | 4314 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P06T | 9559 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P06 | 276 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P07 | 529 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P08 | 11055 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P09 | 348 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P10R | 27005 | 100.0% | 100.0% |  | 100% | ✅ met |
| P10 | 2580 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P11 | 3168 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P12 | 8 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P13 | 11305 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |

### `tls_rpt`

> ceiling: DNS-only check; 'no record' counts as checked

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 44 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P01T | 139 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P01_GOLD | 626 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P02 | 403 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P03 | 209 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P04 | 1570 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P05 | 377 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P06M | 4314 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P06T | 9559 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P06 | 276 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P07 | 529 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P08 | 11055 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P09 | 348 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P10R | 27005 | 100.0% | 100.0% |  | 100% | ✅ met |
| P10 | 2580 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P11 | 3168 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P12 | 8 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P13 | 11305 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |

### `bimi`

> ceiling: DNS-only check; 'no record' counts as checked

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 44 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P01T | 139 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P01_GOLD | 626 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P02 | 403 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P03 | 209 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P04 | 1570 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P05 | 377 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P06M | 4314 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P06T | 9559 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P06 | 276 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P07 | 529 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P08 | 11055 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P09 | 348 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P10R | 27005 | 100.0% | 100.0% |  | 100% | ✅ met |
| P10 | 2580 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P11 | 3168 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P12 | 8 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P13 | 11305 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |

