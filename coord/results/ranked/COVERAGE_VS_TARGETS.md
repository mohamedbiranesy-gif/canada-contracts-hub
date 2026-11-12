# Coverage vs the downstream team's targets — 2026-11-12

Benchmarks (field × package with a numeric target): **47 of 438 met** (10.7%); 108 within 10 points; 283 further away.
A cell counts as filled only when it carries a value: blank, `not_published`, `not_found_yet` and label-only cells ("no identifier published …", "no dataset record …", "0 in the contract dataset …") do not count; the DNS checks count when checked. `any` = share of non-blank cells incl. such labels. Δ = change since the previous build in `coord/results/coverage_history.csv`.
Rows per package: P01M 131, P01T 194, P01_GOLD 636, P02 466, P03 265, P04 3733, P05 424, P06M 15579, P06T 40065, P06 272, P07 697, P08 22233, P09 307, P10R 0, P10 2391, P11 1525, P12 15, P13 118052

## Invoice-grade readiness (the row as an invoice header: bill-to, submit-to, references, terms, tax, vendor identity, follow-up)

| package | rows | all 11 elements | ≥ 9 of 11 | median elements | most-missing element |
|---|---|---|---|---|---|
| P01M | 131 | 0.0% | 19.8% | 8 | vendor GST/HST number (116 rows) |
| P01T | 194 | 1.0% | 34.5% | 8 | payment terms (153 rows) |
| P01_GOLD | 636 | 24.4% | 70.8% | 9 | payment terms (221 rows) |
| P02 | 466 | 7.5% | 54.7% | 9 | PO rule (353 rows) |
| P03 | 265 | 14.3% | 56.6% | 9 | payment terms (130 rows) |
| P04 | 3733 | 1.2% | 16.6% | 6 | PO rule (3534 rows) |
| P05 | 424 | 1.2% | 17.5% | 7 | payment terms (350 rows) |
| P06M | 15579 | 0.0% | 3.0% | 7 | PO rule (15373 rows) |
| P06T | 40065 | 0.0% | 11.0% | 6 | PO rule (39819 rows) |
| P06 | 272 | 0.0% | 11.4% | 6 | reference to quote (PO / contract / vendor id) (272 rows) |
| P07 | 697 | 0.0% | 2.4% | 6 | reference to quote (PO / contract / vendor id) (697 rows) |
| P08 | 22233 | 0.0% | 0.6% | 6 | reference to quote (PO / contract / vendor id) (22233 rows) |
| P09 | 307 | 1.3% | 44.6% | 8 | payment terms (286 rows) |
| P10 | 2391 | 0.0% | 1.0% | 5 | reference to quote (PO / contract / vendor id) (2391 rows) |
| P11 | 1525 | 0.3% | 8.1% | 6 | PO rule (1452 rows) |
| P12 | 15 | 0.0% | 53.3% | 9 | PO rule (14 rows) |
| P13 | 118052 | 0.0% | 0.3% | 6 | reference to quote (PO / contract / vendor id) (118052 rows) |

## AP grade (how stringently the row's accounts-payable data meets what an invoice needs; A = invoicing mailbox referee-confirmed on the buyer's own domain with MX, legal name, address, PO rule and terms all published, no penalties)

| package | rows | A | B | C | D | E | median ap_score |
|---|---|---|---|---|---|---|---|
| P01M | 131 | 8 | 26 | 97 | 0 | 0 | 71 |
| P01T | 194 | 24 | 34 | 136 | 0 | 0 | 70 |
| P01_GOLD | 636 | 229 | 206 | 201 | 0 | 0 | 82 |
| P02 | 466 | 0 | 196 | 270 | 0 | 0 | 66 |
| P03 | 265 | 0 | 0 | 251 | 14 | 0 | 57 |
| P04 | 3733 | 0 | 0 | 3037 | 696 | 0 | 46 |
| P05 | 424 | 15 | 30 | 366 | 13 | 0 | 51 |
| P06M | 15579 | 0 | 10 | 15493 | 76 | 0 | 46 |
| P06T | 40065 | 0 | 24 | 26729 | 13312 | 0 | 38 |
| P06 | 272 | 16 | 50 | 206 | 0 | 0 | 70 |
| P07 | 697 | 0 | 21 | 652 | 24 | 0 | 54 |
| P08 | 22233 | 0 | 0 | 18951 | 3282 | 0 | 43 |
| P09 | 307 | 4 | 12 | 290 | 1 | 0 | 53 |
| P10 | 2391 | 3 | 13 | 1620 | 755 | 0 | 41 |
| P11 | 1525 | 7 | 15 | 43 | 0 | 1460 | 23 |
| P12 | 15 | 0 | 0 | 15 | 0 | 0 | 54 |
| P13 | 118052 | 9 | 61 | 117966 | 16 | 0 | 43 |

### AP payability (confirmed channel + bill-to legal name and address + the buyer's reference rule + tax treatment known)

| package | rows | payable today | % | most common gap |
|---|---|---|---|---|
| P01M | 131 | 108 | 82.4% | the buyer's PO / reference rule (12) |
| P01T | 194 | 118 | 60.8% | bill-to legal name and address (60) |
| P01_GOLD | 636 | 483 | 75.9% | bill-to legal name and address (96) |
| P02 | 466 | 315 | 67.6% | the buyer's PO / reference rule (83) |
| P03 | 265 | 0 | 0.0% | a confirmed invoicing / AP or finance channel (265) |
| P04 | 3733 | 0 | 0.0% | a confirmed invoicing / AP or finance channel (3733) |
| P05 | 424 | 47 | 11.1% | a confirmed invoicing / AP or finance channel (337) |
| P06M | 15579 | 164 | 1.1% | a confirmed invoicing / AP or finance channel (15371) |
| P06T | 40065 | 249 | 0.6% | a confirmed invoicing / AP or finance channel (39478) |
| P06 | 272 | 46 | 16.9% | the buyer's PO / reference rule (117) |
| P07 | 697 | 6 | 0.9% | the buyer's PO / reference rule (273) |
| P08 | 22233 | 0 | 0.0% | a confirmed invoicing / AP or finance channel (22233) |
| P09 | 307 | 42 | 13.7% | a confirmed invoicing / AP or finance channel (255) |
| P10 | 2391 | 7 | 0.3% | a confirmed invoicing / AP or finance channel (2303) |
| P11 | 1525 | 14 | 0.9% | a confirmed invoicing / AP or finance channel (1460) |
| P12 | 15 | 4 | 26.7% | a confirmed invoicing / AP or finance channel (10) |
| P13 | 118052 | 40 | 0.0% | a confirmed invoicing / AP or finance channel (116114) |

### Pay on sight (an invoice generated from the row would clear AP: confirmed invoicing / AP or finance channel, bill-to legal name + address, vendor legal name + GST/HST number + remit-to address, tax treatment and currency known — published or labelled-derived; the buyer's reference rule is reported separately)

| package | rows | pay on sight | % | + reference rule not published | routed (general inbox only) | most common gap |
|---|---|---|---|---|---|---|
| P01M | 131 | 6 | 4.6% | 7 | 0 | the vendor's GST/HST number (BN9) (114) |
| P01T | 194 | 70 | 36.1% | 4 | 0 | the vendor's GST/HST number (BN9) (72) |
| P01_GOLD | 636 | 401 | 63.1% | 11 | 0 | the vendor's GST/HST number (BN9) (159) |
| P02 | 466 | 208 | 44.6% | 21 | 0 | the vendor's GST/HST number (BN9) (201) |
| P03 | 265 | 17 | 6.4% | 0 | 129 | an invoicing / AP or finance mailbox (only a purchasing / general inbo (98) |
| P04 | 3733 | 42 | 1.1% | 7 | 853 | an invoicing / AP or finance mailbox (only a purchasing / general inbo (2773) |
| P05 | 424 | 20 | 4.7% | 8 | 119 | an invoicing / AP or finance mailbox (only a purchasing / general inbo (210) |
| P06M | 15579 | 6 | 0.0% | 11 | 403 | an invoicing / AP or finance mailbox (only a purchasing / general inbo (14922) |
| P06T | 40065 | 234 | 0.6% | 16 | 9521 | an invoicing / AP or finance mailbox (only a purchasing / general inbo (29894) |
| P06 | 272 | 28 | 10.3% | 51 | 0 | the vendor's GST/HST number (BN9) (117) |
| P07 | 697 | 6 | 0.9% | 111 | 35 | the vendor's GST/HST number (BN9) (308) |
| P08 | 22233 | 3 | 0.0% | 14 | 4944 | an invoicing / AP or finance mailbox (only a purchasing / general inbo (17226) |
| P09 | 307 | 38 | 12.4% | 1 | 123 | an invoicing / AP or finance mailbox (only a purchasing / general inbo (123) |
| P10 | 2391 | 7 | 0.3% | 15 | 304 | an invoicing / AP or finance mailbox (only a purchasing / general inbo (1973) |
| P11 | 1525 | 9 | 0.6% | 3 | 0 | a confirmed invoicing / AP or finance channel (1443) |
| P12 | 15 | 3 | 20.0% | 0 | 6 | an invoicing / AP or finance mailbox (only a purchasing / general inbo (4) |
| P13 | 118052 | 11 | 0.0% | 616 | 31414 | an invoicing / AP or finance mailbox (only a purchasing / general inbo (84533) |
| **all** | 206985 | 1109 | 0.5% | 896 | 47851 | |

### What still blocks grade A (rows per missing element; a row counts under every element it lacks)

| package | rows not A | referee confirmation of the mailbox | an invoicing / AP mailbox (not finance / procurement / general) | a mailbox on the buyer's own domain | MX record for the mailbox domain | published bill-to legal name | invoice / billing address | published PO rule | published payment terms | clear the penalty |
|---|---|---|---|---|---|---|---|---|---|---|
| P01M | 123 | 0 | 0 | 0 | 69 | 8 | 0 | 103 | 107 | 4 |
| P01T | 170 | 0 | 0 | 0 | 93 | 51 | 28 | 139 | 154 | 7 |
| P01_GOLD | 407 | 0 | 0 | 0 | 13 | 77 | 31 | 201 | 236 | 61 |
| P02 | 466 | 0 | 466 | 0 | 40 | 53 | 21 | 353 | 281 | 23 |
| P03 | 265 | 0 | 265 | 0 | 17 | 43 | 27 | 127 | 138 | 25 |
| P04 | 3733 | 0 | 3733 | 0 | 1626 | 1355 | 1062 | 3534 | 3279 | 166 |
| P05 | 409 | 0 | 357 | 0 | 79 | 88 | 43 | 341 | 352 | 52 |
| P06M | 15579 | 0 | 15579 | 0 | 10200 | 1224 | 127 | 15373 | 15252 | 219 |
| P06T | 40065 | 0 | 40065 | 0 | 35019 | 24600 | 17185 | 39819 | 39459 | 932 |
| P06 | 256 | 0 | 0 | 0 | 117 | 71 | 52 | 179 | 214 | 9 |
| P07 | 697 | 0 | 697 | 0 | 442 | 276 | 133 | 651 | 652 | 13 |
| P08 | 22233 | 0 | 22233 | 0 | 16863 | 10039 | 4809 | 21949 | 21597 | 431 |
| P09 | 303 | 0 | 282 | 0 | 9 | 71 | 2 | 277 | 289 | 47 |
| P10 | 2388 | 0 | 2354 | 0 | 1196 | 1272 | 1102 | 2321 | 2282 | 123 |
| P11 | 1518 | 1460 | 1413 | 0 | 659 | 1036 | 601 | 1452 | 1451 | 61 |
| P12 | 15 | 0 | 13 | 0 | 1 | 3 | 0 | 14 | 14 | 1 |
| P13 | 118043 | 0 | 117657 | 0 | 90125 | 67125 | 24 | 117737 | 117007 | 34 |

## Where the work is (largest gaps in rows still needed)

| field | package | now | target | rows needed |
|---|---|---|---|---|
| buyer_phone | P13 | 64.5% | 95% | 35957 |
| buyer_ap_cycle_published | P13 | 0.0% | 20% | 23578 |
| buyer_bn_as_published | P13 | 10.1% | 30% | 23512 |
| ap_system_hint | P13 | 0.4% | 20% | 23099 |
| buyer_logo_url | P13 | 77.9% | 95% | 20206 |
| buyer_legal_name_as_published | P13 | 43.1% | 60% | 19905 |
| mta_sts | P13 | 84.0% | 100% | 18881 |
| tls_rpt | P13 | 84.0% | 100% | 18881 |
| bimi | P13 | 84.0% | 100% | 18881 |
| buyer_esignature_preference | P13 | 0.1% | 15% | 17592 |
| buyer_tax_exempt_status | P13 | 0.1% | 15% | 17547 |
| buyer_payment_method_preference | P13 | 0.7% | 15% | 16938 |
| vendor_registered_address | P08 | 30.3% | 70% | 8820 |
| buyer_ap_cycle_published | P06T | 0.0% | 20% | 8003 |
| ap_system_hint | P06T | 0.6% | 20% | 7760 |
| buyer_esignature_preference | P06T | 0.2% | 15% | 5938 |
| buyer_tax_exempt_status | P06T | 0.2% | 15% | 5927 |
| buyer_phone | P08 | 68.7% | 95% | 5856 |
| buyer_payment_method_preference | P06T | 0.6% | 15% | 5786 |
| invoice_reference_hint | P08 | 1.3% | 25% | 5275 |
| buyer_legal_name_as_published | P08 | 54.8% | 75% | 4481 |
| buyer_ap_cycle_published | P08 | 0.0% | 20% | 4436 |
| buyer_bn_as_published | P08 | 15.2% | 35% | 4401 |
| vendor_bn9 | P08 | 30.6% | 50% | 4323 |
| ap_system_hint | P08 | 1.0% | 20% | 4219 |
| vendor_phone | P08 | 66.1% | 85% | 4194 |
| vendor_emails | P08 | 56.3% | 75% | 4157 |
| mta_sts | P06T | 90.3% | 100% | 3901 |
| tls_rpt | P06T | 90.3% | 100% | 3901 |
| bimi | P06T | 90.3% | 100% | 3901 |
| buyer_address | P08 | 78.4% | 95% | 3702 |
| buyer_esignature_preference | P08 | 0.5% | 15% | 3231 |
| buyer_tax_exempt_status | P08 | 0.5% | 15% | 3221 |
| buyer_payment_method_preference | P08 | 0.6% | 15% | 3193 |
| buyer_ap_cycle_published | P06M | 0.0% | 20% | 3110 |
| ap_system_hint | P06M | 0.8% | 20% | 2991 |
| vendor_trading_name | P08 | 36.6% | 50% | 2989 |
| average_contract_duration_days | P04 | 19.0% | 90% | 2649 |
| currency | P04 | 25.5% | 95% | 2596 |
| end_date | P04 | 23.8% | 90% | 2471 |

## 1. identifiers

### `invoice_reference_hint`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 131 | 89.3% | 89.3% | +0.2 | 50% | ✅ met |
| P01T | 194 | 93.8% | 93.8% | +0.0 | 50% | ✅ met |
| P01_GOLD | 636 | 92.3% | 94.5% | +0.1 | 95% | 🟡 3 pts to go |
| P02 | 466 | 74.0% | 75.8% | +0.0 | 95% | ❌ 21 pts to go |
| P03 | 265 | 80.8% | 83.8% | -0.6 | 95% | ❌ 14 pts to go |
| P04 | 3733 | 30.0% | 31.7% | -0.2 | 90% | ❌ 60 pts to go |
| P05 | 424 | 38.4% | 41.3% | -0.2 | 70% | ❌ 32 pts to go |
| P06M | 15579 | 91.9% | 91.9% | +0.1 | n/a | no target |
| P06T | 40065 | 98.7% | 98.7% | +0.1 | n/a | no target |
| P06 | 272 | 34.2% | 34.2% | -0.2 | 30% | ✅ met |
| P07 | 697 | 6.6% | 6.6% | -0.3 | 30% | ❌ 23 pts to go |
| P08 | 22233 | 1.3% | 1.3% | +0.0 | 25% | ❌ 24 pts to go |
| P09 | 307 | 99.0% | 99.7% | +0.0 | 100% | 🟡 1 pts to go |
| P10 | 2391 | 2.9% | 3.0% | -0.2 | 25% | ❌ 22 pts to go |
| P11 | 1525 | 48.5% | 49.4% | +1.6 | 60% | ❌ 12 pts to go |
| P12 | 15 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P13 | 118052 | 99.8% | 99.8% | +0.1 | 0% by design | — leave (by design) |

### `po_number_as_published`

> ceiling: a purchase-order number exists only where the buyer publishes PO-level data (Montréal, Laval, Toronto open data so far) or the record itself carries one; most sources publish awards, not POs — the target cannot be reached from public data for most buyers

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 131 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P01T | 194 | 0.0% | 0.0% | +0.0 | 10% | 🟡 10 pts to go |
| P01_GOLD | 636 | 6.0% | 6.0% | -0.1 | 50% | ❌ 44 pts to go |
| P02 | 466 | 6.2% | 6.2% | +0.0 | 50% | ❌ 44 pts to go |
| P03 | 265 | 1.5% | 1.5% | +0.0 | 40% | ❌ 38 pts to go |
| P04 | 3733 | 0.5% | 0.5% | +0.0 | 30% | ❌ 30 pts to go |
| P05 | 424 | 0.2% | 0.2% | +0.0 | 20% | ❌ 20 pts to go |
| P06M | 15579 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06T | 40065 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06 | 272 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P07 | 697 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P08 | 22233 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P09 | 307 | 0.7% | 0.7% | +0.0 | 50% | ❌ 49 pts to go |
| P10 | 2391 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P11 | 1525 | 0.3% | 0.3% | +0.0 | n/a | no target |
| P12 | 15 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P13 | 118052 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `contract_or_agreement_number`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 131 | 82.4% | 82.4% | +0.2 | n/a | no target |
| P01T | 194 | 74.7% | 74.7% | +0.2 | 50% | ✅ met |
| P01_GOLD | 636 | 67.1% | 67.1% | +0.3 | 85% | ❌ 18 pts to go |
| P02 | 466 | 64.8% | 64.8% | +0.0 | 90% | ❌ 25 pts to go |
| P03 | 265 | 59.2% | 59.2% | -0.5 | 85% | ❌ 26 pts to go |
| P04 | 3733 | 27.5% | 27.5% | -0.1 | 85% | ❌ 58 pts to go |
| P05 | 424 | 28.8% | 28.8% | -0.1 | 60% | ❌ 31 pts to go |
| P06M | 15579 | 91.7% | 91.7% | +0.2 | n/a | no target |
| P06T | 40065 | 98.6% | 98.6% | +0.2 | n/a | no target |
| P06 | 272 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P07 | 697 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P08 | 22233 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P09 | 307 | 96.1% | 96.1% | +0.0 | 100% | 🟡 4 pts to go |
| P10 | 2391 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P11 | 1525 | 45.0% | 45.0% | +1.7 | 60% | ❌ 15 pts to go |
| P12 | 15 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P13 | 118052 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `solicitation_or_tender_number`

> ceiling: SEAO's 'numero' is the organisation's own reference for the notice (SEAO data dictionary) and is reported here; sources that publish awards under a tender number only (bids&tenders, SaskTenders, BC) also carry it as the contract reference, labelled

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 131 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P01T | 194 | 0.0% | 0.0% | +0.0 | 30% | ❌ 30 pts to go |
| P01_GOLD | 636 | 51.1% | 51.1% | +0.3 | 80% | ❌ 29 pts to go |
| P02 | 466 | 56.9% | 56.9% | +0.0 | 60% | 🟡 3 pts to go |
| P03 | 265 | 49.8% | 49.8% | -0.4 | 80% | ❌ 30 pts to go |
| P04 | 3733 | 22.8% | 22.8% | -0.1 | 50% | ❌ 27 pts to go |
| P05 | 424 | 11.3% | 11.3% | -0.1 | 40% | ❌ 29 pts to go |
| P06M | 15579 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06T | 40065 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06 | 272 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P07 | 697 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P08 | 22233 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P09 | 307 | 83.1% | 83.1% | -0.3 | 50% | ✅ met |
| P10 | 2391 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P11 | 1525 | 5.2% | 5.2% | -0.4 | 40% | ❌ 35 pts to go |
| P12 | 15 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P13 | 118052 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `award_or_notice_id`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 131 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P01T | 194 | 0.5% | 0.5% | +0.0 | n/a | no target |
| P01_GOLD | 636 | 61.0% | 61.0% | +0.6 | 85% | ❌ 24 pts to go |
| P02 | 466 | 56.2% | 56.2% | +0.0 | 90% | ❌ 34 pts to go |
| P03 | 265 | 58.1% | 58.1% | -0.5 | 85% | ❌ 27 pts to go |
| P04 | 3733 | 23.5% | 23.5% | -0.1 | 85% | ❌ 62 pts to go |
| P05 | 424 | 19.6% | 19.6% | -0.1 | 50% | ❌ 30 pts to go |
| P06M | 15579 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06T | 40065 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06 | 272 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P07 | 697 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P08 | 22233 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P09 | 307 | 97.1% | 97.1% | +0.0 | 100% | 🟡 3 pts to go |
| P10 | 2391 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P11 | 1525 | 5.6% | 5.6% | -0.4 | 60% | ❌ 54 pts to go |
| P12 | 15 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P13 | 118052 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `buyer_vendor_id`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 131 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P01T | 194 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P01_GOLD | 636 | 13.4% | 13.4% | +0.5 | 60% | ❌ 47 pts to go |
| P02 | 466 | 6.0% | 6.0% | +0.0 | 50% | ❌ 44 pts to go |
| P03 | 265 | 7.9% | 7.9% | -0.5 | 50% | ❌ 42 pts to go |
| P04 | 3733 | 1.8% | 1.8% | +0.0 | 40% | ❌ 38 pts to go |
| P05 | 424 | 0.7% | 0.7% | +0.0 | 20% | ❌ 19 pts to go |
| P06M | 15579 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06T | 40065 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06 | 272 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P07 | 697 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P08 | 22233 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P09 | 307 | 3.3% | 3.3% | +0.0 | 50% | ❌ 47 pts to go |
| P10 | 2391 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P11 | 1525 | 0.7% | 0.7% | -0.2 | n/a | no target |
| P12 | 15 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P13 | 118052 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `commodity_codes`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 131 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P01T | 194 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P01_GOLD | 636 | 35.5% | 35.5% | +0.7 | 80% | ❌ 44 pts to go |
| P02 | 466 | 51.9% | 51.9% | +0.0 | 90% | ❌ 38 pts to go |
| P03 | 265 | 32.5% | 32.5% | -0.2 | 80% | ❌ 48 pts to go |
| P04 | 3733 | 21.5% | 21.5% | -0.1 | 85% | ❌ 64 pts to go |
| P05 | 424 | 5.4% | 5.4% | -0.1 | 50% | ❌ 45 pts to go |
| P06M | 15579 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06T | 40065 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06 | 272 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P07 | 697 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P08 | 22233 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P09 | 307 | 74.9% | 74.9% | +0.6 | 95% | ❌ 20 pts to go |
| P10 | 2391 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P11 | 1525 | 3.9% | 3.9% | -0.4 | 50% | ❌ 46 pts to go |
| P12 | 15 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P13 | 118052 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `buyer_org_codes`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 131 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P01T | 194 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P01_GOLD | 636 | 8.5% | 8.5% | +0.0 | 50% | ❌ 42 pts to go |
| P02 | 466 | 6.2% | 6.2% | +0.0 | 50% | ❌ 44 pts to go |
| P03 | 265 | 1.9% | 1.9% | +0.0 | 30% | ❌ 28 pts to go |
| P04 | 3733 | 0.5% | 0.5% | +0.0 | 30% | ❌ 30 pts to go |
| P05 | 424 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06M | 15579 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06T | 40065 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06 | 272 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P07 | 697 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P08 | 22233 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P09 | 307 | 0.3% | 0.3% | +0.0 | n/a | no target |
| P10 | 2391 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P11 | 1525 | 0.3% | 0.3% | +0.0 | n/a | no target |
| P12 | 15 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P13 | 118052 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `records_with_this_vendor`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 131 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P01T | 194 | 100.0% | 100.0% | +0.0 | 60% | ✅ met |
| P01_GOLD | 636 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P02 | 466 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P03 | 265 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P04 | 3733 | 100.0% | 100.0% | +0.0 | 95% | ✅ met |
| P05 | 424 | 100.0% | 100.0% | +0.0 | 70% | ✅ met |
| P06M | 15579 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P06T | 40065 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P06 | 272 | 100.0% | 100.0% | +0.0 | 50% | ✅ met |
| P07 | 697 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P08 | 22233 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P09 | 307 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P10 | 2391 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P11 | 1525 | 100.0% | 100.0% | +0.0 | 70% | ✅ met |
| P12 | 15 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P13 | 118052 | 0.0% | 0.0% | +0.0 | n/a | no target |

## 2. vendor

### `vendor_bn9`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 131 | 11.5% | 11.5% | -0.1 | 70% | ❌ 58 pts to go |
| P01T | 194 | 52.1% | 52.1% | +1.6 | 60% | 🟡 8 pts to go |
| P01_GOLD | 636 | 72.6% | 72.6% | -2.2 | 90% | ❌ 17 pts to go |
| P02 | 466 | 53.2% | 53.2% | -0.4 | 85% | ❌ 32 pts to go |
| P03 | 265 | 66.4% | 66.4% | -3.2 | 90% | ❌ 24 pts to go |
| P04 | 3733 | 34.5% | 34.5% | -0.5 | 75% | ❌ 40 pts to go |
| P05 | 424 | 53.3% | 53.3% | -1.4 | 50% | ✅ met |
| P06M | 15579 | 3.1% | 3.1% | -0.1 | n/a | no target |
| P06T | 40065 | 48.5% | 48.5% | +1.2 | n/a | no target |
| P06 | 272 | 43.8% | 43.8% | -0.2 | 40% | ✅ met |
| P07 | 697 | 32.7% | 32.7% | -0.3 | 50% | ❌ 17 pts to go |
| P08 | 22233 | 30.6% | 30.6% | +0.1 | 50% | ❌ 19 pts to go |
| P09 | 307 | 57.0% | 57.0% | -1.3 | 80% | ❌ 23 pts to go |
| P10 | 2391 | 34.2% | 34.2% | -0.3 | 40% | 🟡 6 pts to go |
| P11 | 1525 | 47.6% | 47.6% | +0.7 | 60% | ❌ 12 pts to go |
| P12 | 15 | 60.0% | 60.0% | +0.0 | 85% | ❌ 25 pts to go |
| P13 | 118052 | 30.1% | 30.1% | -1.6 | 0% by design | — leave (by design) |

### `vendor_registered_address`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 131 | 58.8% | 58.8% | -0.9 | n/a | no target |
| P01T | 194 | 53.1% | 53.1% | +2.1 | n/a | no target |
| P01_GOLD | 636 | 71.4% | 71.4% | -1.3 | 95% | ❌ 24 pts to go |
| P02 | 466 | 74.2% | 74.2% | +0.4 | 95% | ❌ 21 pts to go |
| P03 | 265 | 69.1% | 69.1% | -2.8 | 95% | ❌ 26 pts to go |
| P04 | 3733 | 49.2% | 49.2% | +0.0 | 95% | ❌ 46 pts to go |
| P05 | 424 | 57.5% | 57.5% | -0.8 | 70% | ❌ 12 pts to go |
| P06M | 15579 | 45.4% | 45.4% | -0.6 | n/a | no target |
| P06T | 40065 | 57.5% | 57.5% | +1.3 | n/a | no target |
| P06 | 272 | 41.2% | 41.2% | +0.2 | 80% | ❌ 39 pts to go |
| P07 | 697 | 32.1% | 32.1% | +0.2 | 70% | ❌ 38 pts to go |
| P08 | 22233 | 30.3% | 30.3% | +0.0 | 70% | ❌ 40 pts to go |
| P09 | 307 | 86.6% | 86.6% | +0.0 | 100% | ❌ 13 pts to go |
| P10 | 2391 | 35.5% | 35.5% | +0.0 | 70% | ❌ 34 pts to go |
| P11 | 1525 | 53.4% | 53.4% | +0.9 | 75% | ❌ 22 pts to go |
| P12 | 15 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P13 | 118052 | 25.5% | 25.5% | -1.4 | n/a | no target |

### `vendor_trading_name`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 131 | 16.8% | 16.8% | -0.3 | n/a | no target |
| P01T | 194 | 55.2% | 55.2% | +1.6 | n/a | no target |
| P01_GOLD | 636 | 48.4% | 48.4% | -1.4 | 60% | ❌ 12 pts to go |
| P02 | 466 | 56.2% | 56.2% | +0.0 | 60% | 🟡 4 pts to go |
| P03 | 265 | 54.3% | 54.3% | -0.8 | 60% | 🟡 6 pts to go |
| P04 | 3733 | 42.5% | 42.5% | +0.4 | 55% | ❌ 12 pts to go |
| P05 | 424 | 24.3% | 24.3% | -0.3 | 50% | ❌ 26 pts to go |
| P06M | 15579 | 6.8% | 6.8% | +0.0 | n/a | no target |
| P06T | 40065 | 51.0% | 51.0% | +0.1 | n/a | no target |
| P06 | 272 | 48.5% | 48.5% | +0.9 | n/a | no target |
| P07 | 697 | 41.9% | 41.9% | +1.0 | 55% | ❌ 13 pts to go |
| P08 | 22233 | 36.6% | 36.6% | +0.4 | 50% | ❌ 13 pts to go |
| P09 | 307 | 72.0% | 72.0% | -0.3 | 70% | ✅ met |
| P10 | 2391 | 47.7% | 47.7% | +0.9 | 55% | 🟡 7 pts to go |
| P11 | 1525 | 54.2% | 54.2% | +2.0 | 50% | ✅ met |
| P12 | 15 | 86.7% | 86.7% | +0.0 | n/a | no target |
| P13 | 118052 | 3.2% | 3.2% | -0.2 | n/a | no target |

### `vendor_phone`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 131 | 49.6% | 49.6% | -0.8 | n/a | no target |
| P01T | 194 | 75.8% | 75.8% | +1.3 | n/a | no target |
| P01_GOLD | 636 | 49.4% | 49.4% | -1.1 | 70% | ❌ 21 pts to go |
| P02 | 466 | 57.3% | 57.3% | -0.9 | 70% | ❌ 13 pts to go |
| P03 | 265 | 50.6% | 50.6% | -0.7 | 70% | ❌ 19 pts to go |
| P04 | 3733 | 56.0% | 56.0% | +1.9 | 65% | 🟡 9 pts to go |
| P05 | 424 | 28.3% | 28.3% | -0.1 | 60% | ❌ 32 pts to go |
| P06M | 15579 | 35.8% | 35.8% | -0.8 | n/a | no target |
| P06T | 40065 | 78.1% | 78.1% | -1.9 | n/a | no target |
| P06 | 272 | 69.1% | 69.1% | +0.2 | 40% | ✅ met |
| P07 | 697 | 65.6% | 65.6% | +0.7 | 85% | ❌ 19 pts to go |
| P08 | 22233 | 66.1% | 66.1% | +0.8 | 85% | ❌ 19 pts to go |
| P09 | 307 | 57.7% | 57.7% | -1.6 | 85% | ❌ 27 pts to go |
| P10 | 2391 | 66.1% | 66.1% | +2.6 | 85% | ❌ 19 pts to go |
| P11 | 1525 | 63.1% | 63.1% | +1.2 | 75% | ❌ 12 pts to go |
| P12 | 15 | 33.3% | 33.3% | +6.6 | n/a | no target |
| P13 | 118052 | 91.8% | 91.8% | +0.6 | 60% | ✅ met |

### `vendor_website`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 131 | 55.7% | 55.7% | -0.9 | n/a | no target |
| P01T | 194 | 97.4% | 97.4% | +0.0 | n/a | no target |
| P01_GOLD | 636 | 78.5% | 78.5% | -1.1 | 90% | ❌ 12 pts to go |
| P02 | 466 | 82.6% | 82.6% | -1.3 | 90% | 🟡 7 pts to go |
| P03 | 265 | 87.2% | 87.2% | -0.6 | 90% | 🟡 3 pts to go |
| P04 | 3733 | 84.1% | 84.1% | -0.3 | 85% | 🟡 1 pts to go |
| P05 | 424 | 44.8% | 44.8% | +0.0 | 70% | ❌ 25 pts to go |
| P06M | 15579 | 42.3% | 42.3% | -1.3 | n/a | no target |
| P06T | 40065 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P06 | 272 | 99.3% | 99.3% | +0.0 | 50% | ✅ met |
| P07 | 697 | 99.9% | 99.9% | +0.0 | 100% | 🟡 0 pts to go |
| P08 | 22233 | 99.8% | 99.8% | +0.0 | 100% | 🟡 0 pts to go |
| P09 | 307 | 78.2% | 78.2% | -1.6 | 100% | ❌ 22 pts to go |
| P10 | 2391 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P11 | 1525 | 97.4% | 97.4% | +0.1 | 100% | 🟡 3 pts to go |
| P12 | 15 | 53.3% | 53.3% | +0.0 | n/a | no target |
| P13 | 118052 | 100.0% | 100.0% | +0.0 | n/a | no target |

### `vendor_emails`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 131 | 15.3% | 15.3% | -0.2 | n/a | no target |
| P01T | 194 | 66.5% | 66.5% | +1.4 | n/a | no target |
| P01_GOLD | 636 | 42.3% | 42.3% | -1.2 | 70% | ❌ 28 pts to go |
| P02 | 466 | 48.1% | 48.1% | -0.6 | 75% | ❌ 27 pts to go |
| P03 | 265 | 43.4% | 43.4% | +0.1 | 75% | ❌ 32 pts to go |
| P04 | 3733 | 39.5% | 39.5% | +0.8 | 70% | ❌ 30 pts to go |
| P05 | 424 | 22.2% | 22.2% | +0.2 | 55% | ❌ 33 pts to go |
| P06M | 15579 | 4.7% | 4.7% | -0.1 | n/a | no target |
| P06T | 40065 | 64.2% | 64.2% | +2.1 | n/a | no target |
| P06 | 272 | 49.3% | 49.3% | +2.4 | n/a | no target |
| P07 | 697 | 50.8% | 50.8% | +0.8 | 70% | ❌ 19 pts to go |
| P08 | 22233 | 56.3% | 56.3% | +1.5 | 75% | ❌ 19 pts to go |
| P09 | 307 | 48.5% | 48.5% | -0.7 | 85% | ❌ 36 pts to go |
| P10 | 2391 | 44.8% | 44.8% | +1.2 | 80% | ❌ 35 pts to go |
| P11 | 1525 | 56.2% | 56.2% | +1.9 | 70% | ❌ 14 pts to go |
| P12 | 15 | 40.0% | 40.0% | +0.0 | n/a | no target |
| P13 | 118052 | 5.3% | 5.3% | +0.1 | n/a | no target |

### `vendor_logo_url`

> ceiling: needs the vendor's website first; sites that block automated readers (robots.txt / 403) are never read

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 131 | 55.7% | 55.7% | -0.9 | n/a | no target |
| P01T | 194 | 95.4% | 95.4% | +0.6 | n/a | no target |
| P01_GOLD | 636 | 72.0% | 72.0% | -1.8 | 90% | ❌ 18 pts to go |
| P02 | 466 | 77.7% | 77.7% | -1.3 | 90% | ❌ 12 pts to go |
| P03 | 265 | 83.4% | 83.4% | +0.1 | 90% | 🟡 7 pts to go |
| P04 | 3733 | 78.9% | 78.9% | +2.5 | 85% | 🟡 6 pts to go |
| P05 | 424 | 43.4% | 43.4% | +0.3 | 75% | ❌ 32 pts to go |
| P06M | 15579 | 42.1% | 42.1% | -1.2 | n/a | no target |
| P06T | 40065 | 97.1% | 97.1% | +0.4 | n/a | no target |
| P06 | 272 | 92.3% | 92.3% | +1.8 | n/a | no target |
| P07 | 697 | 93.7% | 93.7% | +1.2 | 100% | 🟡 6 pts to go |
| P08 | 22233 | 92.8% | 92.8% | +2.0 | 100% | 🟡 7 pts to go |
| P09 | 307 | 67.1% | 67.1% | +1.0 | n/a | no target |
| P10 | 2391 | 90.0% | 90.0% | +3.2 | 100% | 🟡 10 pts to go |
| P11 | 1525 | 89.4% | 89.4% | +1.7 | n/a | no target |
| P12 | 15 | 53.3% | 53.3% | +6.6 | n/a | no target |
| P13 | 118052 | 67.0% | 67.0% | +1.8 | n/a | no target |

### `vendor_neq`

> ceiling: only Québec-registered vendors have an NEQ; the share of QC vendors is reported next to the rate

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 131 | 45.8% | 45.8% | -0.7 | n/a | no target · QC vendors: 49 rows, 100.0% filled |
| P01T | 194 | 8.8% | 8.8% | -0.6 | n/a | no target · QC vendors: 4 rows, 75.0% filled |
| P01_GOLD | 636 | 42.9% | 42.9% | -0.9 | 95% | ❌ 52 pts to go · QC vendors: 51 rows, 98.0% filled |
| P02 | 466 | 56.2% | 56.2% | +0.6 | 95% | ❌ 39 pts to go · QC vendors: 112 rows, 100.0% filled |
| P03 | 265 | 45.3% | 45.3% | -0.7 | 95% | ❌ 50 pts to go · QC vendors: 21 rows, 100.0% filled |
| P04 | 3733 | 32.0% | 32.0% | -0.2 | 95% | ❌ 63 pts to go · QC vendors: 618 rows, 97.9% filled |
| P05 | 424 | 13.7% | 13.7% | -0.3 | n/a | no target · QC vendors: 35 rows, 94.3% filled |
| P06M | 15579 | 42.3% | 42.3% | -0.5 | n/a | no target · QC vendors: 5832 rows, 99.8% filled |
| P06T | 40065 | 5.1% | 5.1% | -0.2 | n/a | no target · QC vendors: 2080 rows, 76.9% filled |
| P06 | 272 | 8.5% | 8.5% | +0.1 | n/a | no target · QC vendors: 16 rows, 68.8% filled |
| P07 | 697 | 6.6% | 6.6% | +0.3 | n/a | no target · QC vendors: 40 rows, 77.5% filled |
| P08 | 22233 | 6.6% | 6.6% | +0.0 | n/a | no target · QC vendors: 1295 rows, 92.7% filled |
| P09 | 307 | 76.5% | 76.5% | -0.4 | 95% | ❌ 18 pts to go · QC vendors: 115 rows, 100.0% filled |
| P10 | 2391 | 15.6% | 15.6% | +0.0 | n/a | no target · QC vendors: 231 rows, 90.0% filled |
| P11 | 1525 | 14.5% | 14.5% | -0.3 | n/a | no target · QC vendors: 156 rows, 91.0% filled |
| P12 | 15 | 73.3% | 73.3% | +0.0 | n/a | no target · QC vendors: 3 rows, 100.0% filled |
| P13 | 118052 | 25.0% | 25.0% | -1.2 | n/a | no target · QC vendors: 29498 rows, 100.0% filled |

### `vendor_years_in_business`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 131 | 58.0% | 58.0% | -0.9 | n/a | no target · vendors with a registry record: 76 rows, 100.0% filled |
| P01T | 194 | 53.1% | 53.1% | +2.1 | n/a | no target · vendors with a registry record: 103 rows, 100.0% filled |
| P01_GOLD | 636 | 79.7% | 79.7% | -1.8 | 100% | ❌ 20 pts to go · vendors with a registry record: 507 rows, 100.0% filled |
| P02 | 466 | 77.3% | 77.3% | -0.2 | 100% | ❌ 23 pts to go · vendors with a registry record: 360 rows, 100.0% filled |
| P03 | 265 | 77.7% | 77.7% | -3.3 | 100% | ❌ 22 pts to go · vendors with a registry record: 206 rows, 100.0% filled |
| P04 | 3733 | 49.5% | 49.5% | -0.2 | 100% | ❌ 50 pts to go · vendors with a registry record: 1848 rows, 100.0% filled |
| P05 | 424 | 62.3% | 62.3% | -1.0 | n/a | no target · vendors with a registry record: 264 rows, 100.0% filled |
| P06M | 15579 | 45.2% | 45.2% | -0.7 | n/a | no target · vendors with a registry record: 7049 rows, 100.0% filled |
| P06T | 40065 | 57.6% | 57.6% | +1.4 | n/a | no target · vendors with a registry record: 23072 rows, 100.0% filled |
| P06 | 272 | 41.5% | 41.5% | +0.1 | n/a | no target · vendors with a registry record: 113 rows, 100.0% filled |
| P07 | 697 | 32.7% | 32.7% | +0.4 | n/a | no target · vendors with a registry record: 228 rows, 100.0% filled |
| P08 | 22233 | 30.5% | 30.5% | +0.1 | n/a | no target · vendors with a registry record: 6777 rows, 100.0% filled |
| P09 | 307 | 90.2% | 90.2% | -0.4 | n/a | no target · vendors with a registry record: 277 rows, 100.0% filled |
| P10 | 2391 | 36.2% | 36.2% | +0.0 | n/a | no target · vendors with a registry record: 866 rows, 100.0% filled |
| P11 | 1525 | 54.4% | 54.4% | +0.8 | n/a | no target · vendors with a registry record: 829 rows, 100.0% filled |
| P12 | 15 | 100.0% | 100.0% | +0.0 | n/a | no target · vendors with a registry record: 15 rows, 100.0% filled |
| P13 | 118052 | 25.5% | 25.5% | -1.4 | n/a | no target · vendors with a registry record: 30158 rows, 100.0% filled |

## 3. buyer

### `buyer_legal_name_as_published`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 131 | 93.9% | 93.9% | +0.1 | 90% | ✅ met |
| P01T | 194 | 73.7% | 73.7% | +1.3 | 90% | ❌ 16 pts to go |
| P01_GOLD | 636 | 87.9% | 87.9% | +0.2 | 95% | 🟡 7 pts to go |
| P02 | 466 | 88.6% | 88.6% | +0.8 | 95% | 🟡 6 pts to go |
| P03 | 265 | 83.8% | 83.8% | -0.6 | 85% | 🟡 1 pts to go |
| P04 | 3733 | 63.7% | 63.7% | +0.7 | 90% | ❌ 26 pts to go |
| P05 | 424 | 79.2% | 79.2% | +0.1 | 75% | ✅ met |
| P06M | 15579 | 92.1% | 92.2% | +0.5 | n/a | no target |
| P06T | 40065 | 38.6% | 38.6% | +1.3 | n/a | no target |
| P06 | 272 | 73.9% | 73.9% | +0.3 | 80% | 🟡 6 pts to go |
| P07 | 697 | 60.4% | 60.5% | +0.6 | 80% | ❌ 20 pts to go |
| P08 | 22233 | 54.8% | 54.9% | +0.4 | 75% | ❌ 20 pts to go |
| P09 | 307 | 76.9% | 76.9% | +0.0 | 95% | ❌ 18 pts to go |
| P10 | 2391 | 46.8% | 46.8% | +0.1 | 70% | ❌ 23 pts to go |
| P11 | 1525 | 32.1% | 32.1% | +0.8 | 65% | ❌ 33 pts to go |
| P12 | 15 | 80.0% | 80.0% | +0.0 | 80% | ✅ met |
| P13 | 118052 | 43.1% | 43.1% | -4.4 | 60% | ❌ 17 pts to go |

### `buyer_bn_as_published`

> ceiling: a buyer's BN is public only where the buyer prints it or a public dataset carries it (CRA charities, federal grants & contributions recipients, business registries for corporations); municipalities rarely publish theirs

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 131 | 19.8% | 19.8% | -0.4 | 50% | ❌ 30 pts to go |
| P01T | 194 | 15.5% | 15.5% | -0.6 | n/a | no target |
| P01_GOLD | 636 | 19.2% | 19.2% | -0.3 | 40% | ❌ 21 pts to go |
| P02 | 466 | 18.9% | 18.9% | -0.2 | 40% | ❌ 21 pts to go |
| P03 | 265 | 21.1% | 21.1% | -0.2 | 40% | ❌ 19 pts to go |
| P04 | 3733 | 14.9% | 14.9% | -0.3 | 40% | ❌ 25 pts to go |
| P05 | 424 | 17.5% | 17.5% | +0.0 | 25% | 🟡 8 pts to go |
| P06M | 15579 | 10.9% | 10.9% | -0.7 | n/a | no target |
| P06T | 40065 | 6.1% | 6.1% | -0.8 | n/a | no target |
| P06 | 272 | 12.5% | 12.5% | -0.3 | 35% | ❌ 22 pts to go |
| P07 | 697 | 13.9% | 13.9% | -0.2 | 35% | ❌ 21 pts to go |
| P08 | 22233 | 15.2% | 15.2% | -0.2 | 35% | ❌ 20 pts to go |
| P09 | 307 | 16.3% | 16.3% | +0.0 | n/a | no target |
| P10 | 2391 | 6.4% | 6.4% | -0.3 | 30% | ❌ 24 pts to go |
| P11 | 1525 | 7.1% | 7.1% | -0.3 | n/a | no target |
| P12 | 15 | 6.7% | 6.7% | +0.0 | n/a | no target |
| P13 | 118052 | 10.1% | 10.1% | -2.2 | 30% | ❌ 20 pts to go |

### `buyer_address`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 131 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P01T | 194 | 84.5% | 84.5% | +0.1 | 100% | ❌ 16 pts to go |
| P01_GOLD | 636 | 90.9% | 90.9% | +0.2 | 100% | 🟡 9 pts to go |
| P02 | 466 | 95.1% | 95.1% | -0.4 | 100% | 🟡 5 pts to go |
| P03 | 265 | 88.7% | 88.7% | -0.7 | 100% | ❌ 11 pts to go |
| P04 | 3733 | 71.0% | 71.0% | -0.4 | 100% | ❌ 29 pts to go |
| P05 | 424 | 89.2% | 89.2% | -0.1 | 100% | ❌ 11 pts to go |
| P06M | 15579 | 99.2% | 99.2% | +0.0 | n/a | no target |
| P06T | 40065 | 57.1% | 57.1% | -2.2 | n/a | no target |
| P06 | 272 | 79.4% | 79.4% | +0.6 | 95% | ❌ 16 pts to go |
| P07 | 697 | 80.6% | 80.6% | -0.6 | 95% | ❌ 14 pts to go |
| P08 | 22233 | 78.4% | 78.4% | +0.1 | 95% | ❌ 17 pts to go |
| P09 | 307 | 96.1% | 96.1% | +0.0 | 100% | 🟡 4 pts to go |
| P10 | 2391 | 53.8% | 53.9% | -0.6 | 95% | ❌ 41 pts to go |
| P11 | 1525 | 50.6% | 50.6% | +1.2 | 80% | ❌ 29 pts to go |
| P12 | 15 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P13 | 118052 | 100.0% | 100.0% | +0.0 | 95% | ✅ met |

### `buyer_phone`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 131 | 87.0% | 87.0% | +1.0 | n/a | no target |
| P01T | 194 | 75.3% | 75.3% | +7.1 | n/a | no target |
| P01_GOLD | 636 | 73.0% | 73.0% | +0.0 | 90% | ❌ 17 pts to go |
| P02 | 466 | 78.1% | 78.1% | +0.2 | 95% | ❌ 17 pts to go |
| P03 | 265 | 74.0% | 74.0% | -0.9 | 95% | ❌ 21 pts to go |
| P04 | 3733 | 69.0% | 69.0% | +0.1 | 95% | ❌ 26 pts to go |
| P05 | 424 | 72.9% | 72.9% | -0.6 | 90% | ❌ 17 pts to go |
| P06M | 15579 | 85.3% | 85.3% | -1.6 | n/a | no target |
| P06T | 40065 | 60.8% | 60.8% | +3.6 | n/a | no target |
| P06 | 272 | 69.5% | 69.5% | +1.0 | 95% | ❌ 26 pts to go |
| P07 | 697 | 66.0% | 66.0% | +1.2 | 90% | ❌ 24 pts to go |
| P08 | 22233 | 68.7% | 68.7% | +0.9 | 95% | ❌ 26 pts to go |
| P09 | 307 | 87.0% | 87.0% | +0.0 | 100% | ❌ 13 pts to go |
| P10 | 2391 | 54.8% | 54.8% | -0.5 | 95% | ❌ 40 pts to go |
| P11 | 1525 | 31.5% | 31.5% | +2.6 | 75% | ❌ 44 pts to go |
| P12 | 15 | 93.3% | 93.3% | +0.0 | n/a | no target |
| P13 | 118052 | 64.5% | 64.5% | -6.3 | 95% | ❌ 30 pts to go |

### `buyer_logo_url`

> ceiling: sites that block automated readers (robots.txt / 403) are never read; an og:image that looks like a photo is labelled

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 131 | 88.5% | 88.5% | +0.9 | n/a | no target |
| P01T | 194 | 90.2% | 90.2% | +6.9 | 95% | 🟡 5 pts to go |
| P01_GOLD | 636 | 84.6% | 84.6% | -0.2 | 90% | 🟡 5 pts to go |
| P02 | 466 | 90.6% | 90.6% | +0.0 | 95% | 🟡 4 pts to go |
| P03 | 265 | 84.9% | 84.9% | -0.7 | 95% | ❌ 10 pts to go |
| P04 | 3733 | 90.7% | 90.7% | +1.5 | 90% | ✅ met |
| P05 | 424 | 92.5% | 92.5% | -0.6 | 95% | 🟡 2 pts to go |
| P06M | 15579 | 90.8% | 90.8% | -2.4 | n/a | no target |
| P06T | 40065 | 82.4% | 82.4% | +7.5 | n/a | no target |
| P06 | 272 | 93.0% | 93.0% | +0.7 | 100% | 🟡 7 pts to go |
| P07 | 697 | 92.8% | 92.8% | +0.6 | 100% | 🟡 7 pts to go |
| P08 | 22233 | 94.2% | 94.2% | +1.9 | 100% | 🟡 6 pts to go |
| P09 | 307 | 73.3% | 73.3% | +0.3 | n/a | no target |
| P10 | 2391 | 93.2% | 93.2% | +1.9 | 100% | 🟡 7 pts to go |
| P11 | 1525 | 50.0% | 50.0% | +8.1 | 80% | ❌ 30 pts to go |
| P12 | 15 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P13 | 118052 | 77.9% | 77.9% | -5.8 | 95% | ❌ 17 pts to go |

## 4. AP

### `ap_contact_name_as_published`

> ceiling: owner 2026-11-08: the AP contact person the organisation itself names on its AP / finance page is allowed (name + role phrase, quoted); mailboxes stay organisational; many bodies publish no AP person

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 131 | 3.1% | 3.1% | +0.0 | n/a | no target |
| P01T | 194 | 9.3% | 9.3% | -0.1 | n/a | no target |
| P01_GOLD | 636 | 14.0% | 14.0% | -0.2 | 25% | ❌ 11 pts to go |
| P02 | 466 | 25.1% | 25.1% | -0.2 | 40% | ❌ 15 pts to go |
| P03 | 265 | 9.1% | 9.1% | +0.0 | 20% | ❌ 11 pts to go |
| P04 | 3733 | 3.5% | 3.5% | +0.0 | 20% | ❌ 16 pts to go |
| P05 | 424 | 3.3% | 3.3% | +0.0 | 15% | ❌ 12 pts to go |
| P06M | 15579 | 0.3% | 0.3% | +0.0 | n/a | no target |
| P06T | 40065 | 0.3% | 0.3% | +0.0 | n/a | no target |
| P06 | 272 | 5.1% | 5.1% | +0.0 | n/a | no target |
| P07 | 697 | 8.5% | 8.5% | +0.0 | n/a | no target |
| P08 | 22233 | 0.3% | 0.3% | +0.0 | n/a | no target |
| P09 | 307 | 7.8% | 7.8% | +0.0 | n/a | no target |
| P10 | 2391 | 0.8% | 0.8% | +0.0 | n/a | no target |
| P11 | 1525 | 0.9% | 0.9% | -0.1 | n/a | no target |
| P12 | 15 | 6.7% | 6.7% | +0.0 | n/a | no target |
| P13 | 118052 | 0.3% | 0.3% | +0.0 | n/a | no target |

### `ap_phone`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 131 | 18.3% | 18.3% | -0.3 | n/a | no target |
| P01T | 194 | 22.2% | 22.2% | -0.2 | 70% | ❌ 48 pts to go |
| P01_GOLD | 636 | 43.1% | 43.1% | -0.4 | 80% | ❌ 37 pts to go |
| P02 | 466 | 57.3% | 57.3% | +0.0 | 90% | ❌ 33 pts to go |
| P03 | 265 | 18.5% | 18.5% | -0.1 | 60% | ❌ 42 pts to go |
| P04 | 3733 | 21.6% | 21.6% | +0.0 | 85% | ❌ 63 pts to go |
| P05 | 424 | 11.6% | 11.6% | +0.0 | 50% | ❌ 38 pts to go |
| P06M | 15579 | 0.6% | 0.6% | +0.0 | n/a | no target |
| P06T | 40065 | 0.6% | 0.6% | -0.1 | n/a | no target |
| P06 | 272 | 15.4% | 15.4% | +0.0 | n/a | no target |
| P07 | 697 | 10.0% | 10.0% | -0.5 | n/a | no target |
| P08 | 22233 | 0.6% | 0.6% | +0.0 | n/a | no target |
| P09 | 307 | 77.9% | 77.9% | +0.0 | 95% | ❌ 17 pts to go |
| P10 | 2391 | 1.5% | 1.5% | -0.2 | n/a | no target |
| P11 | 1525 | 15.9% | 15.9% | -0.8 | n/a | no target |
| P12 | 15 | 26.7% | 26.7% | +0.0 | n/a | no target |
| P13 | 118052 | 0.4% | 0.4% | -0.1 | n/a | no target |

### `invoice_mailing_address`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 131 | 6.1% | 6.1% | -0.1 | n/a | no target |
| P01T | 194 | 9.8% | 9.8% | -0.6 | n/a | no target |
| P01_GOLD | 636 | 34.1% | 34.1% | +0.1 | 70% | ❌ 36 pts to go |
| P02 | 466 | 39.1% | 39.1% | +0.0 | 75% | ❌ 36 pts to go |
| P03 | 265 | 18.5% | 18.5% | -0.1 | 55% | ❌ 36 pts to go |
| P04 | 3733 | 21.5% | 21.5% | -0.1 | 75% | ❌ 54 pts to go |
| P05 | 424 | 10.6% | 10.6% | -0.1 | 50% | ❌ 39 pts to go |
| P06M | 15579 | 0.2% | 0.2% | +0.0 | n/a | no target |
| P06T | 40065 | 0.3% | 0.3% | -0.1 | n/a | no target |
| P06 | 272 | 6.2% | 6.2% | +0.3 | n/a | no target |
| P07 | 697 | 4.9% | 4.9% | -0.3 | n/a | no target |
| P08 | 22233 | 0.2% | 0.2% | +0.0 | n/a | no target |
| P09 | 307 | 75.2% | 75.2% | +0.0 | 95% | ❌ 20 pts to go |
| P10 | 2391 | 0.7% | 0.7% | -0.2 | n/a | no target |
| P11 | 1525 | 15.5% | 15.5% | -0.9 | n/a | no target |
| P12 | 15 | 20.0% | 20.0% | +0.0 | n/a | no target |
| P13 | 118052 | 0.3% | 0.3% | +0.0 | n/a | no target |

### `invoicing_requirements`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 131 | 7.6% | 7.6% | -0.2 | n/a | no target |
| P01T | 194 | 8.2% | 8.2% | -0.1 | n/a | no target |
| P01_GOLD | 636 | 57.9% | 58.0% | -0.1 | 80% | ❌ 22 pts to go |
| P02 | 466 | 45.7% | 45.9% | +0.0 | 75% | ❌ 29 pts to go |
| P03 | 265 | 37.0% | 37.0% | -0.3 | 70% | ❌ 33 pts to go |
| P04 | 3733 | 21.1% | 21.5% | +0.0 | 70% | ❌ 49 pts to go |
| P05 | 424 | 14.2% | 14.2% | +0.0 | 50% | ❌ 36 pts to go |
| P06M | 15579 | 0.3% | 0.3% | +0.0 | n/a | no target |
| P06T | 40065 | 0.2% | 0.2% | -0.1 | n/a | no target |
| P06 | 272 | 15.8% | 15.8% | -0.7 | n/a | no target |
| P07 | 697 | 1.9% | 1.9% | -0.1 | n/a | no target |
| P08 | 22233 | 0.4% | 0.4% | +0.0 | n/a | no target |
| P09 | 307 | 46.6% | 46.9% | +0.0 | 80% | ❌ 33 pts to go |
| P10 | 2391 | 1.0% | 1.1% | -0.2 | n/a | no target |
| P11 | 1525 | 6.4% | 6.4% | -0.4 | n/a | no target |
| P12 | 15 | 40.0% | 40.0% | +0.0 | n/a | no target |
| P13 | 118052 | 0.2% | 0.2% | +0.0 | n/a | no target |

### `payment_terms_as_published`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 131 | 18.3% | 18.3% | -0.3 | n/a | no target |
| P01T | 194 | 20.6% | 20.6% | -0.8 | 60% | ❌ 39 pts to go |
| P01_GOLD | 636 | 62.9% | 62.9% | -0.5 | 70% | 🟡 7 pts to go |
| P02 | 466 | 39.7% | 39.7% | +0.0 | 50% | ❌ 10 pts to go |
| P03 | 265 | 47.9% | 47.9% | -0.4 | 55% | 🟡 7 pts to go |
| P04 | 3733 | 12.2% | 12.2% | +0.0 | 40% | ❌ 28 pts to go |
| P05 | 424 | 17.0% | 17.0% | -0.1 | 40% | ❌ 23 pts to go |
| P06M | 15579 | 2.1% | 2.1% | -0.1 | n/a | no target |
| P06T | 40065 | 1.5% | 1.5% | -0.2 | n/a | no target |
| P06 | 272 | 21.3% | 21.3% | -0.7 | n/a | no target |
| P07 | 697 | 6.5% | 6.5% | -0.1 | n/a | no target |
| P08 | 22233 | 2.9% | 2.9% | +0.0 | n/a | no target |
| P09 | 307 | 5.9% | 5.9% | +0.0 | n/a | no target |
| P10 | 2391 | 4.6% | 4.6% | +0.0 | n/a | no target |
| P11 | 1525 | 4.9% | 4.9% | -0.3 | n/a | no target |
| P12 | 15 | 6.7% | 6.7% | +0.0 | n/a | no target |
| P13 | 118052 | 0.9% | 0.9% | -0.1 | n/a | no target |

### `po_required_as_published`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 131 | 21.4% | 21.4% | -0.3 | n/a | no target |
| P01T | 194 | 28.4% | 28.4% | -0.2 | 65% | ❌ 37 pts to go |
| P01_GOLD | 636 | 68.4% | 68.4% | -0.6 | 70% | 🟡 2 pts to go |
| P02 | 466 | 24.2% | 24.2% | +0.0 | 50% | ❌ 26 pts to go |
| P03 | 265 | 52.1% | 52.1% | -0.4 | 60% | 🟡 8 pts to go |
| P04 | 3733 | 5.3% | 5.3% | -0.1 | 40% | ❌ 35 pts to go |
| P05 | 424 | 19.6% | 19.6% | -0.1 | 45% | ❌ 25 pts to go |
| P06M | 15579 | 1.3% | 1.3% | -0.1 | n/a | no target |
| P06T | 40065 | 0.6% | 0.6% | -0.1 | n/a | no target |
| P06 | 272 | 34.2% | 34.2% | -0.2 | n/a | no target |
| P07 | 697 | 6.6% | 6.6% | -0.3 | n/a | no target |
| P08 | 22233 | 1.3% | 1.3% | +0.0 | n/a | no target |
| P09 | 307 | 9.8% | 9.8% | +0.0 | n/a | no target |
| P10 | 2391 | 2.9% | 2.9% | -0.2 | n/a | no target |
| P11 | 1525 | 4.8% | 4.8% | -0.3 | n/a | no target |
| P12 | 15 | 6.7% | 6.7% | +0.0 | n/a | no target |
| P13 | 118052 | 0.3% | 0.3% | +0.0 | n/a | no target |

### `invoice_portal_url`

> ceiling: only portals the buyer names on its own pages; informational tax-authority links are not portals

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 131 | 12.2% | 12.2% | -0.2 | n/a | no target |
| P01T | 194 | 13.4% | 13.4% | -0.1 | n/a | no target |
| P01_GOLD | 636 | 49.2% | 49.2% | -0.6 | 50% | 🟡 1 pts to go |
| P02 | 466 | 37.3% | 37.3% | +0.0 | n/a | no target |
| P03 | 265 | 51.7% | 51.7% | -0.4 | 60% | 🟡 8 pts to go |
| P04 | 3733 | 11.8% | 11.8% | -0.1 | n/a | no target |
| P05 | 424 | 15.1% | 15.1% | -0.1 | n/a | no target |
| P06M | 15579 | 0.5% | 0.5% | +0.0 | n/a | no target |
| P06T | 40065 | 0.3% | 0.3% | -0.1 | n/a | no target |
| P06 | 272 | 25.4% | 25.4% | -0.2 | n/a | no target |
| P07 | 697 | 8.2% | 8.2% | -0.1 | n/a | no target |
| P08 | 22233 | 0.6% | 0.6% | +0.0 | n/a | no target |
| P09 | 307 | 17.6% | 17.6% | +0.0 | n/a | no target |
| P10 | 2391 | 2.4% | 2.4% | +0.0 | n/a | no target |
| P11 | 1525 | 4.3% | 4.3% | -0.4 | n/a | no target |
| P12 | 15 | 13.3% | 13.3% | +0.0 | n/a | no target |
| P13 | 118052 | 0.2% | 0.2% | -0.1 | n/a | no target |

### `buyer_payment_method_preference`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 131 | 11.5% | 11.5% | -0.1 | 15% | 🟡 4 pts to go |
| P01T | 194 | 12.4% | 12.4% | -0.1 | 15% | 🟡 3 pts to go |
| P01_GOLD | 636 | 34.9% | 34.9% | -0.4 | 40% | 🟡 5 pts to go |
| P02 | 466 | 12.9% | 13.1% | +0.0 | 25% | ❌ 12 pts to go |
| P03 | 265 | 17.4% | 17.4% | -0.1 | 25% | 🟡 8 pts to go |
| P04 | 3733 | 2.7% | 2.7% | +0.0 | 15% | ❌ 12 pts to go |
| P05 | 424 | 6.6% | 6.6% | +0.0 | 15% | 🟡 8 pts to go |
| P06M | 15579 | 0.8% | 0.8% | -0.1 | 15% | ❌ 14 pts to go |
| P06T | 40065 | 0.6% | 0.6% | +0.1 | 15% | ❌ 14 pts to go |
| P06 | 272 | 10.7% | 10.7% | +0.1 | 15% | 🟡 4 pts to go |
| P07 | 697 | 4.2% | 4.2% | -0.1 | 15% | ❌ 11 pts to go |
| P08 | 22233 | 0.6% | 0.6% | +0.0 | 15% | ❌ 14 pts to go |
| P09 | 307 | 1.0% | 1.0% | +0.0 | 15% | ❌ 14 pts to go |
| P10 | 2391 | 1.3% | 1.3% | +0.0 | 15% | ❌ 14 pts to go |
| P11 | 1525 | 1.6% | 1.6% | +0.1 | 15% | ❌ 13 pts to go |
| P12 | 15 | 0.0% | 0.0% | +0.0 | 15% | ❌ 15 pts to go |
| P13 | 118052 | 0.7% | 0.7% | +0.0 | 15% | ❌ 14 pts to go |

### `buyer_tax_exempt_status`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 131 | 5.3% | 5.3% | -0.1 | 15% | 🟡 10 pts to go |
| P01T | 194 | 11.3% | 11.3% | -0.2 | 25% | ❌ 14 pts to go |
| P01_GOLD | 636 | 28.8% | 28.8% | -0.4 | 25% | ✅ met |
| P02 | 466 | 25.3% | 25.3% | +0.0 | 15% | ✅ met |
| P03 | 265 | 21.9% | 21.9% | -0.2 | 15% | ✅ met |
| P04 | 3733 | 4.0% | 4.0% | +0.0 | 15% | ❌ 11 pts to go |
| P05 | 424 | 11.1% | 11.1% | +0.0 | 15% | 🟡 4 pts to go |
| P06M | 15579 | 0.5% | 0.5% | +0.0 | 15% | ❌ 14 pts to go |
| P06T | 40065 | 0.2% | 0.2% | +0.0 | 15% | ❌ 15 pts to go |
| P06 | 272 | 8.5% | 8.5% | +0.1 | 15% | 🟡 6 pts to go |
| P07 | 697 | 2.9% | 2.9% | +0.0 | 15% | ❌ 12 pts to go |
| P08 | 22233 | 0.5% | 0.5% | +0.0 | 15% | ❌ 14 pts to go |
| P09 | 307 | 1.0% | 1.0% | +0.0 | 15% | ❌ 14 pts to go |
| P10 | 2391 | 1.5% | 1.5% | -0.1 | 15% | ❌ 14 pts to go |
| P11 | 1525 | 2.5% | 2.5% | -0.2 | 15% | ❌ 12 pts to go |
| P12 | 15 | 20.0% | 20.0% | +0.0 | 15% | ✅ met |
| P13 | 118052 | 0.1% | 0.1% | -0.1 | 15% | ❌ 15 pts to go |

### `buyer_ap_cycle_published`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 131 | 2.3% | 2.3% | +0.0 | 20% | ❌ 18 pts to go |
| P01T | 194 | 4.1% | 4.1% | -0.1 | 20% | ❌ 16 pts to go |
| P01_GOLD | 636 | 4.4% | 4.4% | -0.1 | 20% | ❌ 16 pts to go |
| P02 | 466 | 1.5% | 1.5% | +0.0 | 20% | ❌ 18 pts to go |
| P03 | 265 | 1.5% | 1.5% | +0.0 | 20% | ❌ 18 pts to go |
| P04 | 3733 | 0.6% | 0.6% | +0.0 | 20% | ❌ 19 pts to go |
| P05 | 424 | 1.2% | 1.2% | +0.0 | 20% | ❌ 19 pts to go |
| P06M | 15579 | 0.0% | 0.0% | +0.0 | 20% | ❌ 20 pts to go |
| P06T | 40065 | 0.0% | 0.0% | +0.0 | 20% | ❌ 20 pts to go |
| P06 | 272 | 1.5% | 1.5% | +0.0 | 20% | ❌ 18 pts to go |
| P07 | 697 | 0.4% | 0.4% | +0.0 | 20% | ❌ 20 pts to go |
| P08 | 22233 | 0.0% | 0.0% | +0.0 | 20% | ❌ 20 pts to go |
| P09 | 307 | 0.0% | 0.0% | +0.0 | 20% | ❌ 20 pts to go |
| P10 | 2391 | 0.3% | 0.3% | +0.0 | 20% | ❌ 20 pts to go |
| P11 | 1525 | 0.3% | 0.3% | +0.0 | 20% | ❌ 20 pts to go |
| P12 | 15 | 0.0% | 0.0% | +0.0 | 20% | ❌ 20 pts to go |
| P13 | 118052 | 0.0% | 0.0% | +0.0 | 20% | ❌ 20 pts to go |

### `buyer_esignature_preference`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 131 | 1.5% | 1.5% | -0.1 | 15% | ❌ 14 pts to go |
| P01T | 194 | 3.1% | 3.1% | +0.0 | 15% | ❌ 12 pts to go |
| P01_GOLD | 636 | 10.2% | 10.2% | -0.2 | 15% | 🟡 5 pts to go |
| P02 | 466 | 12.0% | 12.0% | +0.0 | 15% | 🟡 3 pts to go |
| P03 | 265 | 20.0% | 20.0% | -0.2 | 15% | ✅ met |
| P04 | 3733 | 2.3% | 2.3% | +0.0 | 15% | ❌ 13 pts to go |
| P05 | 424 | 2.8% | 2.8% | +0.0 | 15% | ❌ 12 pts to go |
| P06M | 15579 | 0.3% | 0.3% | +0.0 | 15% | ❌ 15 pts to go |
| P06T | 40065 | 0.2% | 0.2% | +0.0 | 15% | ❌ 15 pts to go |
| P06 | 272 | 5.1% | 5.1% | +0.0 | 15% | 🟡 10 pts to go |
| P07 | 697 | 1.6% | 1.6% | +0.0 | 15% | ❌ 13 pts to go |
| P08 | 22233 | 0.5% | 0.5% | +0.0 | 15% | ❌ 14 pts to go |
| P09 | 307 | 0.7% | 0.7% | +0.0 | 15% | ❌ 14 pts to go |
| P10 | 2391 | 1.0% | 1.0% | +0.0 | 15% | ❌ 14 pts to go |
| P11 | 1525 | 1.2% | 1.2% | +0.0 | 15% | ❌ 14 pts to go |
| P12 | 15 | 6.7% | 6.7% | +0.0 | 15% | 🟡 8 pts to go |
| P13 | 118052 | 0.1% | 0.1% | +0.0 | 15% | ❌ 15 pts to go |

### `ap_system_hint`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 131 | 13.7% | 13.7% | -0.3 | 20% | 🟡 6 pts to go |
| P01T | 194 | 13.9% | 13.9% | -0.2 | 40% | ❌ 26 pts to go |
| P01_GOLD | 636 | 45.6% | 45.6% | -0.6 | 40% | ✅ met |
| P02 | 466 | 42.9% | 42.9% | +0.0 | 20% | ✅ met |
| P03 | 265 | 48.7% | 48.7% | -0.3 | 35% | ✅ met |
| P04 | 3733 | 14.1% | 14.1% | -0.1 | 20% | 🟡 6 pts to go |
| P05 | 424 | 15.3% | 15.3% | -0.1 | 20% | 🟡 5 pts to go |
| P06M | 15579 | 0.8% | 0.8% | +0.0 | 20% | ❌ 19 pts to go |
| P06T | 40065 | 0.6% | 0.6% | -0.1 | 20% | ❌ 19 pts to go |
| P06 | 272 | 25.0% | 25.0% | -0.3 | 20% | ✅ met |
| P07 | 697 | 8.6% | 8.6% | +0.0 | 20% | ❌ 11 pts to go |
| P08 | 22233 | 1.0% | 1.0% | +0.0 | 20% | ❌ 19 pts to go |
| P09 | 307 | 18.2% | 18.2% | +0.0 | 20% | 🟡 2 pts to go |
| P10 | 2391 | 3.6% | 3.6% | -0.1 | 20% | ❌ 16 pts to go |
| P11 | 1525 | 4.6% | 4.6% | -0.2 | 20% | ❌ 15 pts to go |
| P12 | 15 | 6.7% | 6.7% | +0.0 | 20% | ❌ 13 pts to go |
| P13 | 118052 | 0.4% | 0.4% | -0.1 | 20% | ❌ 20 pts to go |

## 5. contract

### `contract_value`

> ceiling: rows proven by a lobbying filing, a news release, an auditor appointment, a customer story or a vendor's client list have no contract value by nature (≈17 % of P01 Gold); bids&tenders awards now carry the awarded bidder's submitted price when no award value was published

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 131 | 33.6% | 33.6% | +0.3 | n/a | no target |
| P01T | 194 | 0.5% | 0.5% | +0.0 | n/a | no target |
| P01_GOLD | 636 | 71.7% | 71.7% | +2.2 | 95% | ❌ 23 pts to go |
| P02 | 466 | 64.2% | 64.2% | +1.3 | 95% | ❌ 31 pts to go |
| P03 | 265 | 55.8% | 55.8% | +2.6 | 90% | ❌ 34 pts to go |
| P04 | 3733 | 25.1% | 25.1% | +0.3 | 85% | ❌ 60 pts to go |
| P05 | 424 | 38.2% | 38.2% | +0.5 | 75% | ❌ 37 pts to go |
| P06M | 15579 | 36.2% | 36.2% | +0.1 | n/a | no target |
| P06T | 40065 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06 | 272 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P07 | 697 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P08 | 22233 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P09 | 307 | 90.6% | 90.6% | +2.3 | 100% | 🟡 9 pts to go |
| P10 | 2391 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P11 | 1525 | 5.8% | 5.8% | -0.2 | 60% | ❌ 54 pts to go |
| P12 | 15 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P13 | 118052 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `currency`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 131 | 33.6% | 33.6% | +0.3 | n/a | no target |
| P01T | 194 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P01_GOLD | 636 | 73.4% | 73.4% | +0.6 | 100% | ❌ 27 pts to go |
| P02 | 466 | 66.3% | 66.3% | +0.0 | 100% | ❌ 34 pts to go |
| P03 | 265 | 58.5% | 58.5% | -0.4 | n/a | no target |
| P04 | 3733 | 25.5% | 25.5% | +0.0 | 95% | ❌ 70 pts to go |
| P05 | 424 | 33.7% | 33.7% | +0.3 | 80% | ❌ 46 pts to go |
| P06M | 15579 | 36.2% | 36.2% | +0.1 | n/a | no target |
| P06T | 40065 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06 | 272 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P07 | 697 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P08 | 22233 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P09 | 307 | 92.5% | 92.5% | +1.0 | 100% | 🟡 8 pts to go |
| P10 | 2391 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P11 | 1525 | 6.0% | 6.0% | -0.4 | n/a | no target |
| P12 | 15 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P13 | 118052 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `start_date`

> ceiling: most award notices publish an award date, not a start date; start_date carries the signature date when the source gives one, labelled

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 131 | 80.2% | 80.2% | +0.4 | n/a | no target |
| P01T | 194 | 0.5% | 0.5% | +0.0 | n/a | no target |
| P01_GOLD | 636 | 52.2% | 52.2% | +0.6 | 85% | ❌ 33 pts to go |
| P02 | 466 | 57.5% | 57.5% | +0.0 | 90% | ❌ 32 pts to go |
| P03 | 265 | 42.3% | 42.3% | -0.3 | 85% | ❌ 43 pts to go |
| P04 | 3733 | 27.8% | 27.8% | -0.1 | 90% | ❌ 62 pts to go |
| P05 | 424 | 32.3% | 32.3% | -0.4 | 75% | ❌ 43 pts to go |
| P06M | 15579 | 86.1% | 86.1% | -1.0 | n/a | no target |
| P06T | 40065 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06 | 272 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P07 | 697 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P08 | 22233 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P09 | 307 | 83.4% | 83.4% | +0.0 | 95% | ❌ 12 pts to go |
| P10 | 2391 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P11 | 1525 | 5.0% | 5.0% | -0.4 | n/a | no target |
| P12 | 15 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P13 | 118052 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `end_date`

> ceiling: an inferred end (award date + published duration) is labelled as such; sources without a duration leave end_date empty — the honest ceiling. P09 is BY DEFINITION the rows whose end date is not published (older SEAO contracts with no closing notice): its end_date / duration targets cannot be met without inventing a date

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 131 | 78.6% | 78.6% | +0.3 | n/a | no target |
| P01T | 194 | 0.5% | 0.5% | +0.0 | n/a | no target |
| P01_GOLD | 636 | 52.5% | 52.5% | +0.7 | 85% | ❌ 32 pts to go |
| P02 | 466 | 52.6% | 52.6% | +0.0 | 90% | ❌ 37 pts to go |
| P03 | 265 | 42.6% | 42.6% | -1.1 | 85% | ❌ 42 pts to go |
| P04 | 3733 | 23.8% | 23.8% | +0.0 | 90% | ❌ 66 pts to go |
| P05 | 424 | 42.9% | 42.9% | -0.5 | 75% | ❌ 32 pts to go |
| P06M | 15579 | 76.7% | 76.7% | -1.1 | n/a | no target |
| P06T | 40065 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06 | 272 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P07 | 697 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P08 | 22233 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P09 | 307 | 0.3% | 0.3% | +0.0 | 95% | ❌ 95 pts to go |
| P10 | 2391 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P11 | 1525 | 4.1% | 4.1% | -0.4 | n/a | no target |
| P12 | 15 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P13 | 118052 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `contract_title`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 131 | 90.1% | 90.1% | +0.2 | n/a | no target |
| P01T | 194 | 94.3% | 94.3% | +0.0 | n/a | no target |
| P01_GOLD | 636 | 85.4% | 85.4% | +0.1 | 100% | ❌ 15 pts to go |
| P02 | 466 | 76.6% | 76.6% | +0.2 | 100% | ❌ 23 pts to go |
| P03 | 265 | 91.3% | 91.3% | +0.0 | n/a | no target |
| P04 | 3733 | 49.0% | 49.0% | +0.2 | 95% | ❌ 46 pts to go |
| P05 | 424 | 77.4% | 77.4% | -0.1 | 95% | ❌ 18 pts to go |
| P06M | 15579 | 99.0% | 99.0% | +0.1 | n/a | no target |
| P06T | 40065 | 91.8% | 91.8% | +1.2 | n/a | no target |
| P06 | 272 | 22.8% | 22.8% | -0.3 | n/a | no target |
| P07 | 697 | 13.2% | 13.2% | -0.6 | n/a | no target |
| P08 | 22233 | 7.1% | 7.1% | +0.0 | n/a | no target |
| P09 | 307 | 98.7% | 98.7% | +0.0 | 100% | 🟡 1 pts to go |
| P10 | 2391 | 71.0% | 71.0% | +0.0 | n/a | no target |
| P11 | 1525 | 69.2% | 69.2% | +1.1 | n/a | no target |
| P12 | 15 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P13 | 118052 | 99.8% | 99.8% | +0.1 | n/a | no target |

### `contract_description`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 131 | 90.1% | 90.1% | +0.2 | n/a | no target |
| P01T | 194 | 94.3% | 94.3% | +0.0 | n/a | no target |
| P01_GOLD | 636 | 88.5% | 88.5% | +0.0 | 100% | ❌ 12 pts to go |
| P02 | 466 | 77.7% | 77.9% | +0.2 | 100% | ❌ 22 pts to go |
| P03 | 265 | 92.1% | 92.1% | +0.1 | n/a | no target |
| P04 | 3733 | 52.2% | 52.2% | +0.3 | 95% | ❌ 43 pts to go |
| P05 | 424 | 89.4% | 89.4% | -0.2 | 70% | ✅ met |
| P06M | 15579 | 99.0% | 99.0% | +0.1 | n/a | no target |
| P06T | 40065 | 91.8% | 91.8% | +1.2 | n/a | no target |
| P06 | 272 | 22.8% | 22.8% | -0.3 | n/a | no target |
| P07 | 697 | 13.2% | 13.2% | -0.6 | n/a | no target |
| P08 | 22233 | 7.1% | 7.1% | +0.0 | n/a | no target |
| P09 | 307 | 98.7% | 98.7% | +0.0 | 100% | 🟡 1 pts to go |
| P10 | 2391 | 71.0% | 71.0% | +0.0 | n/a | no target |
| P11 | 1525 | 69.3% | 69.3% | +1.1 | n/a | no target |
| P12 | 15 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P13 | 118052 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `number_of_bids`

> ceiling: published by some portals only (bids&tenders submission lists, Biddingo bidder lists); federal proactive disclosure does not publish bid counts

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 131 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P01T | 194 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P01_GOLD | 636 | 16.5% | 16.5% | -0.3 | 60% | ❌ 44 pts to go · rows from a source that publishes bids: 371 rows, 28.3% filled |
| P02 | 466 | 11.2% | 11.2% | +0.0 | n/a | no target · rows from a source that publishes bids: 290 rows, 17.9% filled |
| P03 | 265 | 14.0% | 14.0% | +1.1 | n/a | no target · rows from a source that publishes bids: 139 rows, 26.6% filled |
| P04 | 3733 | 1.5% | 1.5% | +0.0 | n/a | no target · rows from a source that publishes bids: 871 rows, 6.4% filled |
| P05 | 424 | 2.6% | 2.6% | +0.0 | n/a | no target · rows from a source that publishes bids: 50 rows, 22.0% filled |
| P06M | 15579 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06T | 40065 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06 | 272 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P07 | 697 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P08 | 22233 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P09 | 307 | 4.2% | 4.2% | +0.0 | n/a | no target · rows from a source that publishes bids: 293 rows, 4.4% filled |
| P10 | 2391 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P11 | 1525 | 0.9% | 0.9% | +0.0 | n/a | no target · rows from a source that publishes bids: 88 rows, 14.8% filled |
| P12 | 15 | 0.0% | 0.0% | +0.0 | n/a | no target · rows from a source that publishes bids: 15 rows, 0.0% filled |
| P13 | 118052 | 0.0% | 0.0% | +0.0 | n/a | no target |

## 6. history

### `average_contract_duration_days`

> ceiling: needs two dates (or a published term) on the buyer's records; P09 rows (end date unpublished by definition) and buyers whose sources publish award dates only have no honest duration

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 131 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P01T | 194 | 0.0% | 97.9% | +0.0 | n/a | no target |
| P01_GOLD | 636 | 53.5% | 82.4% | +0.3 | 90% | ❌ 36 pts to go |
| P02 | 466 | 52.4% | 87.6% | +0.0 | 90% | ❌ 38 pts to go |
| P03 | 265 | 44.2% | 80.8% | -0.3 | 90% | ❌ 46 pts to go |
| P04 | 3733 | 19.0% | 93.9% | -0.1 | 90% | ❌ 71 pts to go |
| P05 | 424 | 0.0% | 83.5% | +0.0 | 90% | ❌ 90 pts to go |
| P06M | 15579 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P06T | 40065 | 0.0% | 99.8% | +0.0 | n/a | no target |
| P06 | 272 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P07 | 697 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P08 | 22233 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P09 | 307 | 2.3% | 3.9% | +0.0 | 90% | ❌ 88 pts to go |
| P10 | 2391 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P11 | 1525 | 3.7% | 97.0% | -0.4 | n/a | no target |
| P12 | 15 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P13 | 118052 | 0.0% | 100.0% | +0.0 | n/a | no target |

### `commodity_distribution_top3`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 131 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P01T | 194 | 0.5% | 98.5% | +0.0 | n/a | no target |
| P01_GOLD | 636 | 26.3% | 55.2% | +0.4 | 90% | ❌ 64 pts to go |
| P02 | 466 | 51.5% | 86.7% | +0.0 | n/a | no target |
| P03 | 265 | 24.2% | 60.8% | -0.1 | n/a | no target |
| P04 | 3733 | 20.9% | 95.7% | -0.1 | n/a | no target |
| P05 | 424 | 0.5% | 84.0% | +0.0 | n/a | no target |
| P06M | 15579 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P06T | 40065 | 0.1% | 99.9% | +0.0 | n/a | no target |
| P06 | 272 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P07 | 697 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P08 | 22233 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P09 | 307 | 41.0% | 42.7% | +0.0 | n/a | no target |
| P10 | 2391 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P11 | 1525 | 3.5% | 96.8% | -0.2 | n/a | no target |
| P12 | 15 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P13 | 118052 | 0.0% | 100.0% | +0.0 | n/a | no target |

### `year_over_year_spend_trend`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 131 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P01T | 194 | 2.1% | 100.0% | +0.0 | n/a | no target |
| P01_GOLD | 636 | 51.9% | 80.8% | +0.1 | 95% | ❌ 43 pts to go |
| P02 | 466 | 56.4% | 91.6% | +0.0 | n/a | no target |
| P03 | 265 | 46.4% | 83.0% | -0.4 | n/a | no target |
| P04 | 3733 | 21.1% | 96.0% | -0.1 | n/a | no target |
| P05 | 424 | 4.5% | 88.0% | +0.0 | n/a | no target |
| P06M | 15579 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P06T | 40065 | 0.1% | 100.0% | +0.0 | n/a | no target |
| P06 | 272 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P07 | 697 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P08 | 22233 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P09 | 307 | 62.5% | 64.2% | +0.0 | n/a | no target |
| P10 | 2391 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P11 | 1525 | 3.9% | 97.2% | -0.2 | n/a | no target |
| P12 | 15 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P13 | 118052 | 0.0% | 100.0% | +0.0 | n/a | no target |

## 7. mail security

### `mta_sts`

> ceiling: DNS-only check; 'no record' counts as checked

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 131 | 98.5% | 98.5% | -1.5 | 100% | 🟡 2 pts to go |
| P01T | 194 | 98.5% | 98.5% | -1.5 | 100% | 🟡 2 pts to go |
| P01_GOLD | 636 | 99.8% | 99.8% | -0.2 | 100% | 🟡 0 pts to go |
| P02 | 466 | 99.8% | 99.8% | -0.2 | 100% | 🟡 0 pts to go |
| P03 | 265 | 99.2% | 99.2% | -0.8 | 100% | 🟡 1 pts to go |
| P04 | 3733 | 98.8% | 98.8% | -1.2 | 100% | 🟡 1 pts to go |
| P05 | 424 | 99.3% | 99.3% | -0.7 | 100% | 🟡 1 pts to go |
| P06M | 15579 | 95.0% | 95.0% | -5.0 | 100% | 🟡 5 pts to go |
| P06T | 40065 | 90.3% | 90.3% | -9.7 | 100% | 🟡 10 pts to go |
| P06 | 272 | 99.3% | 99.3% | -0.7 | 100% | 🟡 1 pts to go |
| P07 | 697 | 98.9% | 98.9% | -1.1 | 100% | 🟡 1 pts to go |
| P08 | 22233 | 98.5% | 98.5% | -1.5 | 100% | 🟡 2 pts to go |
| P09 | 307 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P10 | 2391 | 98.0% | 98.0% | -2.0 | 100% | 🟡 2 pts to go |
| P11 | 1525 | 95.6% | 95.6% | -4.4 | 100% | 🟡 4 pts to go |
| P12 | 15 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P13 | 118052 | 84.0% | 84.0% | -16.0 | 100% | ❌ 16 pts to go |

### `tls_rpt`

> ceiling: DNS-only check; 'no record' counts as checked

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 131 | 98.5% | 98.5% | -1.5 | 100% | 🟡 2 pts to go |
| P01T | 194 | 98.5% | 98.5% | -1.5 | 100% | 🟡 2 pts to go |
| P01_GOLD | 636 | 99.8% | 99.8% | -0.2 | 100% | 🟡 0 pts to go |
| P02 | 466 | 99.8% | 99.8% | -0.2 | 100% | 🟡 0 pts to go |
| P03 | 265 | 99.2% | 99.2% | -0.8 | 100% | 🟡 1 pts to go |
| P04 | 3733 | 98.8% | 98.8% | -1.2 | 100% | 🟡 1 pts to go |
| P05 | 424 | 99.3% | 99.3% | -0.7 | 100% | 🟡 1 pts to go |
| P06M | 15579 | 95.0% | 95.0% | -5.0 | 100% | 🟡 5 pts to go |
| P06T | 40065 | 90.3% | 90.3% | -9.7 | 100% | 🟡 10 pts to go |
| P06 | 272 | 99.3% | 99.3% | -0.7 | 100% | 🟡 1 pts to go |
| P07 | 697 | 98.9% | 98.9% | -1.1 | 100% | 🟡 1 pts to go |
| P08 | 22233 | 98.5% | 98.5% | -1.5 | 100% | 🟡 2 pts to go |
| P09 | 307 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P10 | 2391 | 98.0% | 98.0% | -2.0 | 100% | 🟡 2 pts to go |
| P11 | 1525 | 95.6% | 95.6% | -4.4 | 100% | 🟡 4 pts to go |
| P12 | 15 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P13 | 118052 | 84.0% | 84.0% | -16.0 | 100% | ❌ 16 pts to go |

### `bimi`

> ceiling: DNS-only check; 'no record' counts as checked

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 131 | 98.5% | 98.5% | -1.5 | 100% | 🟡 2 pts to go |
| P01T | 194 | 98.5% | 98.5% | -1.5 | 100% | 🟡 2 pts to go |
| P01_GOLD | 636 | 99.8% | 99.8% | -0.2 | 100% | 🟡 0 pts to go |
| P02 | 466 | 99.8% | 99.8% | -0.2 | 100% | 🟡 0 pts to go |
| P03 | 265 | 99.2% | 99.2% | -0.8 | 100% | 🟡 1 pts to go |
| P04 | 3733 | 98.8% | 98.8% | -1.2 | 100% | 🟡 1 pts to go |
| P05 | 424 | 99.3% | 99.3% | -0.7 | 100% | 🟡 1 pts to go |
| P06M | 15579 | 95.0% | 95.0% | -5.0 | 100% | 🟡 5 pts to go |
| P06T | 40065 | 90.3% | 90.3% | -9.7 | 100% | 🟡 10 pts to go |
| P06 | 272 | 99.3% | 99.3% | -0.7 | 100% | 🟡 1 pts to go |
| P07 | 697 | 98.9% | 98.9% | -1.1 | 100% | 🟡 1 pts to go |
| P08 | 22233 | 98.5% | 98.5% | -1.5 | 100% | 🟡 2 pts to go |
| P09 | 307 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P10 | 2391 | 98.0% | 98.0% | -2.0 | 100% | 🟡 2 pts to go |
| P11 | 1525 | 95.6% | 95.6% | -4.4 | 100% | 🟡 4 pts to go |
| P12 | 15 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P13 | 118052 | 84.0% | 84.0% | -16.0 | 100% | ❌ 16 pts to go |

