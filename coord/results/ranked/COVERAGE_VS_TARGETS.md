# Coverage vs the downstream team's targets — 2026-11-13

Benchmarks (field × package with a numeric target): **89 of 438 met** (20.3%); 64 within 10 points; 285 further away.
A cell counts as filled only when it carries a value: blank, `not_published`, `not_found_yet` and label-only cells ("no identifier published …", "no dataset record …", "0 in the contract dataset …") do not count; the DNS checks count when checked. `any` = share of non-blank cells incl. such labels. Δ = change since the previous build in `coord/results/coverage_history.csv`.
Rows per package: P01M 377, P01T 211, P01_GOLD 653, P02 491, P03 279, P04 4868, P05 429, P06M 28835, P06T 55504, P06 259, P07 791, P08 29605, P09 276, P10R 0, P10 2080, P11 1799, P12 11, P13 193993

## Invoice-grade readiness (the row as an invoice header: bill-to, submit-to, references, terms, tax, vendor identity, follow-up)

| package | rows | all 11 elements | ≥ 9 of 11 | median elements | most-missing element |
|---|---|---|---|---|---|
| P01M | 377 | 0.0% | 9.8% | 7 | vendor GST/HST number (356 rows) |
| P01T | 211 | 0.9% | 33.6% | 8 | payment terms (167 rows) |
| P01_GOLD | 653 | 23.3% | 68.5% | 9 | payment terms (249 rows) |
| P02 | 491 | 7.1% | 52.7% | 9 | PO rule (379 rows) |
| P03 | 279 | 14.0% | 53.8% | 9 | PO rule (145 rows) |
| P04 | 4868 | 1.0% | 12.6% | 7 | PO rule (4669 rows) |
| P05 | 429 | 0.9% | 17.0% | 7 | payment terms (358 rows) |
| P06M | 28835 | 0.0% | 2.4% | 7 | PO rule (28452 rows) |
| P06T | 55504 | 0.1% | 13.4% | 7 | PO rule (55173 rows) |
| P06 | 259 | 0.0% | 10.0% | 6 | reference to quote (PO / contract / vendor id) (242 rows) |
| P07 | 791 | 0.0% | 2.9% | 6 | PO rule (752 rows) |
| P08 | 29605 | 0.0% | 1.5% | 6 | PO rule (29352 rows) |
| P09 | 276 | 1.4% | 42.0% | 8 | payment terms (257 rows) |
| P10 | 2080 | 0.0% | 1.2% | 5 | reference to quote (PO / contract / vendor id) (2080 rows) |
| P11 | 1799 | 0.1% | 7.7% | 6 | PO rule (1734 rows) |
| P12 | 11 | 0.0% | 36.4% | 8 | PO rule (11 rows) |
| P13 | 193993 | 0.0% | 0.3% | 6 | reference to quote (PO / contract / vendor id) (193993 rows) |

## AP grade (how stringently the row's accounts-payable data meets what an invoice needs; A = invoicing mailbox referee-confirmed on the buyer's own domain with MX, legal name, address, PO rule and terms all published, no penalties)

| package | rows | A | B | C | D | E | median ap_score |
|---|---|---|---|---|---|---|---|
| P01M | 377 | 11 | 68 | 298 | 0 | 0 | 66 |
| P01T | 211 | 26 | 32 | 153 | 0 | 0 | 66 |
| P01_GOLD | 653 | 254 | 169 | 230 | 0 | 0 | 81 |
| P02 | 491 | 0 | 193 | 298 | 0 | 0 | 66 |
| P03 | 279 | 0 | 0 | 267 | 12 | 0 | 57 |
| P04 | 4868 | 0 | 0 | 4199 | 669 | 0 | 46 |
| P05 | 429 | 14 | 29 | 373 | 13 | 0 | 51 |
| P06M | 28835 | 0 | 19 | 28766 | 50 | 0 | 46 |
| P06T | 55504 | 0 | 27 | 38139 | 17338 | 0 | 38 |
| P06 | 259 | 16 | 32 | 211 | 0 | 0 | 66 |
| P07 | 791 | 0 | 20 | 752 | 19 | 0 | 55 |
| P08 | 29605 | 0 | 0 | 26803 | 2802 | 0 | 46 |
| P09 | 276 | 5 | 10 | 260 | 1 | 0 | 53 |
| P10 | 2080 | 2 | 10 | 1412 | 656 | 0 | 41 |
| P11 | 1799 | 7 | 13 | 37 | 0 | 1742 | 23 |
| P12 | 11 | 0 | 0 | 11 | 0 | 0 | 51 |
| P13 | 193993 | 12 | 64 | 193904 | 13 | 0 | 38 |

### AP payability (confirmed channel + bill-to legal name and address + the buyer's reference rule + tax treatment known)

| package | rows | payable today | % | most common gap |
|---|---|---|---|---|
| P01M | 377 | 280 | 74.3% | tax treatment (69) |
| P01T | 211 | 126 | 59.7% | bill-to legal name and address (69) |
| P01_GOLD | 653 | 490 | 75.0% | bill-to legal name and address (95) |
| P02 | 491 | 334 | 68.0% | the buyer's PO / reference rule (85) |
| P03 | 279 | 0 | 0.0% | a confirmed invoicing / AP or finance channel (279) |
| P04 | 4868 | 0 | 0.0% | a confirmed invoicing / AP or finance channel (4868) |
| P05 | 429 | 45 | 10.5% | a confirmed invoicing / AP or finance channel (341) |
| P06M | 28835 | 314 | 1.1% | a confirmed invoicing / AP or finance channel (28441) |
| P06T | 55504 | 330 | 0.6% | a confirmed invoicing / AP or finance channel (54736) |
| P06 | 259 | 45 | 17.4% | the buyer's PO / reference rule (115) |
| P07 | 791 | 48 | 6.1% | the buyer's PO / reference rule (322) |
| P08 | 29605 | 0 | 0.0% | a confirmed invoicing / AP or finance channel (29605) |
| P09 | 276 | 39 | 14.1% | a confirmed invoicing / AP or finance channel (226) |
| P10 | 2080 | 5 | 0.2% | a confirmed invoicing / AP or finance channel (2007) |
| P11 | 1799 | 19 | 1.1% | a confirmed invoicing / AP or finance channel (1742) |
| P12 | 11 | 2 | 18.2% | a confirmed invoicing / AP or finance channel (9) |
| P13 | 193993 | 43 | 0.0% | a confirmed invoicing / AP or finance channel (191582) |

### Pay on sight (an invoice generated from the row would clear AP: confirmed invoicing / AP or finance channel, bill-to legal name + address, vendor legal name + GST/HST number + remit-to address, tax treatment and currency known — published or labelled-derived; the buyer's reference rule is reported separately)

| package | rows | pay on sight | % | + reference rule not published | routed (general inbox only) | most common gap |
|---|---|---|---|---|---|---|
| P01M | 377 | 9 | 2.4% | 7 | 0 | the vendor's GST/HST number (BN9) (356) |
| P01T | 211 | 84 | 39.8% | 3 | 0 | the vendor's GST/HST number (BN9) (76) |
| P01_GOLD | 653 | 409 | 62.6% | 11 | 0 | the vendor's GST/HST number (BN9) (167) |
| P02 | 491 | 215 | 43.8% | 22 | 0 | the vendor's GST/HST number (BN9) (226) |
| P03 | 279 | 18 | 6.5% | 0 | 133 | an invoicing / AP or finance mailbox (only a purchasing / general inbo (108) |
| P04 | 4868 | 42 | 0.9% | 7 | 920 | an invoicing / AP or finance mailbox (only a purchasing / general inbo (3842) |
| P05 | 429 | 21 | 4.9% | 8 | 128 | an invoicing / AP or finance mailbox (only a purchasing / general inbo (204) |
| P06M | 28835 | 8 | 0.0% | 14 | 702 | an invoicing / AP or finance mailbox (only a purchasing / general inbo (27638) |
| P06T | 55504 | 362 | 0.7% | 15 | 18138 | an invoicing / AP or finance mailbox (only a purchasing / general inbo (36518) |
| P06 | 259 | 21 | 8.1% | 51 | 0 | the vendor's GST/HST number (BN9) (118) |
| P07 | 791 | 16 | 2.0% | 137 | 37 | the vendor's GST/HST number (BN9) (385) |
| P08 | 29605 | 4 | 0.0% | 13 | 7299 | an invoicing / AP or finance mailbox (only a purchasing / general inbo (22246) |
| P09 | 276 | 36 | 13.0% | 0 | 107 | an invoicing / AP or finance mailbox (only a purchasing / general inbo (107) |
| P10 | 2080 | 5 | 0.2% | 14 | 298 | an invoicing / AP or finance mailbox (only a purchasing / general inbo (1688) |
| P11 | 1799 | 7 | 0.4% | 2 | 0 | a confirmed invoicing / AP or finance channel (1726) |
| P12 | 11 | 1 | 9.1% | 0 | 5 | an invoicing / AP or finance mailbox (only a purchasing / general inbo (4) |
| P13 | 193993 | 22 | 0.0% | 1148 | 76447 | an invoicing / AP or finance mailbox (only a purchasing / general inbo (114955) |
| **all** | 320461 | 1280 | 0.4% | 1452 | 104214 | |

### What still blocks grade A (rows per missing element; a row counts under every element it lacks)

| package | rows not A | referee confirmation of the mailbox | an invoicing / AP mailbox (not finance / procurement / general) | a mailbox on the buyer's own domain | MX record for the mailbox domain | published bill-to legal name | invoice / billing address | published PO rule | published payment terms | clear the penalty |
|---|---|---|---|---|---|---|---|---|---|---|
| P01M | 366 | 0 | 0 | 0 | 273 | 9 | 0 | 314 | 333 | 0 |
| P01T | 185 | 0 | 0 | 0 | 119 | 63 | 28 | 156 | 168 | 4 |
| P01_GOLD | 399 | 0 | 0 | 0 | 39 | 77 | 30 | 227 | 264 | 2 |
| P02 | 491 | 0 | 491 | 0 | 59 | 57 | 14 | 379 | 306 | 2 |
| P03 | 279 | 0 | 279 | 0 | 28 | 46 | 27 | 145 | 153 | 2 |
| P04 | 4868 | 0 | 4868 | 0 | 2705 | 1539 | 1016 | 4669 | 4428 | 33 |
| P05 | 415 | 0 | 362 | 0 | 87 | 100 | 40 | 345 | 360 | 7 |
| P06M | 28835 | 0 | 28835 | 0 | 22605 | 1456 | 128 | 28452 | 28192 | 20 |
| P06T | 55504 | 0 | 55504 | 0 | 49826 | 34673 | 22304 | 55173 | 54708 | 419 |
| P06 | 243 | 0 | 0 | 0 | 132 | 71 | 42 | 191 | 214 | 4 |
| P07 | 791 | 0 | 791 | 0 | 537 | 307 | 103 | 752 | 752 | 5 |
| P08 | 29605 | 0 | 29605 | 0 | 23416 | 12783 | 4319 | 29352 | 28996 | 188 |
| P09 | 271 | 0 | 252 | 0 | 12 | 68 | 1 | 246 | 259 | 7 |
| P10 | 2078 | 0 | 2049 | 0 | 1080 | 1123 | 949 | 2017 | 1979 | 16 |
| P11 | 1792 | 1742 | 1697 | 0 | 920 | 1221 | 544 | 1734 | 1729 | 21 |
| P12 | 11 | 0 | 10 | 0 | 0 | 3 | 0 | 11 | 11 | 2 |
| P13 | 193981 | 0 | 193542 | 0 | 164219 | 118725 | 19 | 193650 | 192788 | 70 |

## Where the work is (largest gaps in rows still needed)

| field | package | now | target | rows needed |
|---|---|---|---|---|
| buyer_phone | P13 | 57.5% | 95% | 72692 |
| buyer_logo_url | P13 | 69.9% | 95% | 48624 |
| buyer_legal_name_as_published | P13 | 38.8% | 60% | 41128 |
| buyer_ap_cycle_published | P13 | 0.0% | 20% | 38745 |
| ap_system_hint | P13 | 0.3% | 20% | 38181 |
| buyer_bn_as_published | P13 | 10.7% | 30% | 37505 |
| buyer_esignature_preference | P13 | 0.1% | 15% | 28947 |
| buyer_tax_exempt_status | P13 | 0.1% | 15% | 28902 |
| buyer_payment_method_preference | P13 | 0.6% | 15% | 28019 |
| vendor_registered_address | P08 | 31.8% | 70% | 11304 |
| buyer_ap_cycle_published | P06T | 0.0% | 20% | 11086 |
| ap_system_hint | P06T | 0.6% | 20% | 10767 |
| buyer_esignature_preference | P06T | 0.2% | 15% | 8230 |
| buyer_tax_exempt_status | P06T | 0.2% | 15% | 8219 |
| buyer_payment_method_preference | P06T | 0.6% | 15% | 7971 |
| buyer_phone | P08 | 70.9% | 95% | 7141 |
| buyer_ap_cycle_published | P08 | 0.0% | 20% | 5909 |
| buyer_ap_cycle_published | P06M | 0.0% | 20% | 5753 |
| ap_system_hint | P08 | 0.8% | 20% | 5697 |
| vendor_emails | P08 | 55.9% | 75% | 5657 |
| ap_system_hint | P06M | 0.9% | 20% | 5511 |
| buyer_legal_name_as_published | P08 | 56.8% | 75% | 5382 |
| vendor_bn9 | P08 | 32.2% | 50% | 5256 |
| vendor_phone | P08 | 67.5% | 85% | 5173 |
| vendor_trading_name | P08 | 33.9% | 50% | 4781 |
| buyer_esignature_preference | P08 | 0.3% | 15% | 4343 |
| buyer_tax_exempt_status | P08 | 0.3% | 15% | 4338 |
| buyer_payment_method_preference | P08 | 0.6% | 15% | 4262 |
| buyer_esignature_preference | P06M | 0.3% | 15% | 4230 |
| buyer_tax_exempt_status | P06M | 0.5% | 15% | 4174 |
| buyer_payment_method_preference | P06M | 0.7% | 15% | 4122 |
| invoice_reference_hint | P08 | 12.1% | 25% | 3813 |
| buyer_bn_as_published | P08 | 22.6% | 35% | 3677 |
| average_contract_duration_days | P04 | 14.5% | 90% | 3675 |
| currency | P04 | 20.9% | 95% | 3609 |
| ap_phone | P04 | 14.9% | 85% | 3412 |
| commodity_codes | P04 | 16.4% | 85% | 3339 |
| award_or_notice_id | P04 | 18.4% | 85% | 3243 |
| contract_value | P04 | 20.5% | 85% | 3139 |
| invoice_mailing_address | P04 | 14.9% | 75% | 2924 |

## 1. identifiers

### `invoice_reference_hint`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 377 | 94.4% | 94.4% | +1.2 | 50% | ✅ met |
| P01T | 211 | 94.8% | 94.8% | -0.8 | 50% | ✅ met |
| P01_GOLD | 653 | 92.2% | 94.6% | +0.0 | 95% | 🟡 3 pts to go |
| P02 | 491 | 75.8% | 77.2% | +0.8 | 95% | ❌ 19 pts to go |
| P03 | 279 | 82.1% | 85.3% | +0.5 | 95% | ❌ 13 pts to go |
| P04 | 4868 | 43.3% | 44.6% | +11.5 | 90% | ❌ 47 pts to go |
| P05 | 429 | 40.3% | 43.4% | +0.7 | 70% | ❌ 30 pts to go |
| P06M | 28835 | 93.8% | 93.8% | +0.6 | n/a | no target |
| P06T | 55504 | 99.5% | 99.5% | +0.2 | n/a | no target |
| P06 | 259 | 32.4% | 32.4% | -3.0 | 30% | ✅ met |
| P07 | 791 | 13.9% | 13.9% | -0.3 | 30% | ❌ 16 pts to go |
| P08 | 29605 | 12.1% | 12.1% | -0.1 | 25% | ❌ 13 pts to go |
| P09 | 276 | 98.9% | 99.6% | +0.0 | 100% | 🟡 1 pts to go |
| P10 | 2080 | 3.0% | 3.0% | -0.3 | 25% | ❌ 22 pts to go |
| P11 | 1799 | 54.6% | 55.3% | +0.3 | 60% | 🟡 5 pts to go |
| P12 | 11 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P13 | 193993 | 99.6% | 99.6% | +0.0 | 0% by design | — leave (by design) |

### `po_number_as_published`

> ceiling: a purchase-order number exists only where the buyer publishes PO-level data (Montréal, Laval, Toronto open data so far) or the record itself carries one; most sources publish awards, not POs — the target cannot be reached from public data for most buyers

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 377 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P01T | 211 | 0.0% | 0.0% | +0.0 | 10% | 🟡 10 pts to go |
| P01_GOLD | 653 | 5.7% | 5.7% | +0.0 | 50% | ❌ 44 pts to go |
| P02 | 491 | 5.7% | 5.7% | -0.5 | 50% | ❌ 44 pts to go |
| P03 | 279 | 1.8% | 1.8% | -0.1 | 40% | ❌ 38 pts to go |
| P04 | 4868 | 0.5% | 0.5% | -0.1 | 30% | ❌ 30 pts to go |
| P05 | 429 | 0.2% | 0.2% | +0.0 | 20% | ❌ 20 pts to go |
| P06M | 28835 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06T | 55504 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06 | 259 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P07 | 791 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P08 | 29605 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P09 | 276 | 0.7% | 0.7% | +0.0 | 50% | ❌ 49 pts to go |
| P10 | 2080 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P11 | 1799 | 0.2% | 0.2% | +0.0 | n/a | no target |
| P12 | 11 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P13 | 193993 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `contract_or_agreement_number`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 377 | 92.0% | 92.0% | +2.4 | n/a | no target |
| P01T | 211 | 78.2% | 78.2% | -1.7 | 50% | ✅ met |
| P01_GOLD | 653 | 68.9% | 68.9% | +1.6 | 85% | ❌ 16 pts to go |
| P02 | 491 | 67.2% | 67.2% | +1.0 | 90% | ❌ 23 pts to go |
| P03 | 279 | 62.0% | 62.0% | +1.5 | 85% | ❌ 23 pts to go |
| P04 | 4868 | 41.3% | 41.3% | +12.2 | 85% | ❌ 44 pts to go |
| P05 | 429 | 31.0% | 31.0% | +1.1 | 60% | ❌ 29 pts to go |
| P06M | 28835 | 93.5% | 93.5% | +0.5 | n/a | no target |
| P06T | 55504 | 99.4% | 99.4% | +0.2 | n/a | no target |
| P06 | 259 | 6.6% | 6.6% | +0.2 | n/a | no target |
| P07 | 791 | 9.0% | 9.0% | -0.1 | n/a | no target |
| P08 | 29605 | 11.3% | 11.3% | +0.0 | n/a | no target |
| P09 | 276 | 95.7% | 95.7% | +0.1 | 100% | 🟡 4 pts to go |
| P10 | 2080 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P11 | 1799 | 51.8% | 51.8% | +0.3 | 60% | 🟡 8 pts to go |
| P12 | 11 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P13 | 193993 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `solicitation_or_tender_number`

> ceiling: SEAO's 'numero' is the organisation's own reference for the notice (SEAO data dictionary) and is reported here; sources that publish awards under a tender number only (bids&tenders, SaskTenders, BC) also carry it as the contract reference, labelled

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 377 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P01T | 211 | 0.0% | 0.0% | +0.0 | 30% | ❌ 30 pts to go |
| P01_GOLD | 653 | 49.3% | 49.3% | -2.4 | 80% | ❌ 31 pts to go |
| P02 | 491 | 55.2% | 55.2% | -2.9 | 60% | 🟡 5 pts to go |
| P03 | 279 | 48.0% | 48.0% | -2.4 | 80% | ❌ 32 pts to go |
| P04 | 4868 | 17.7% | 17.7% | -6.3 | 50% | ❌ 32 pts to go |
| P05 | 429 | 13.8% | 13.8% | +1.2 | 40% | ❌ 26 pts to go |
| P06M | 28835 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06T | 55504 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06 | 259 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P07 | 791 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P08 | 29605 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P09 | 276 | 81.2% | 81.2% | +0.1 | 50% | ✅ met |
| P10 | 2080 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P11 | 1799 | 3.3% | 3.3% | +0.0 | 40% | ❌ 37 pts to go |
| P12 | 11 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P13 | 193993 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `award_or_notice_id`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 377 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P01T | 211 | 0.5% | 0.5% | +0.1 | n/a | no target |
| P01_GOLD | 653 | 58.5% | 58.5% | -2.4 | 85% | ❌ 26 pts to go |
| P02 | 491 | 55.0% | 55.0% | -3.1 | 90% | ❌ 35 pts to go |
| P03 | 279 | 56.3% | 56.3% | -3.1 | 85% | ❌ 29 pts to go |
| P04 | 4868 | 18.4% | 18.4% | -6.5 | 85% | ❌ 67 pts to go |
| P05 | 429 | 21.4% | 21.4% | +1.0 | 50% | ❌ 29 pts to go |
| P06M | 28835 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06T | 55504 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06 | 259 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P07 | 791 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P08 | 29605 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P09 | 276 | 97.1% | 97.1% | +0.0 | 100% | 🟡 3 pts to go |
| P10 | 2080 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P11 | 1799 | 3.7% | 3.7% | +0.1 | 60% | ❌ 56 pts to go |
| P12 | 11 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P13 | 193993 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `buyer_vendor_id`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 377 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P01T | 211 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P01_GOLD | 653 | 12.3% | 12.3% | -0.3 | 60% | ❌ 48 pts to go |
| P02 | 491 | 6.5% | 6.5% | -0.8 | 50% | ❌ 44 pts to go |
| P03 | 279 | 8.2% | 8.2% | -0.4 | 50% | ❌ 42 pts to go |
| P04 | 4868 | 1.4% | 1.4% | -0.5 | 40% | ❌ 39 pts to go |
| P05 | 429 | 0.7% | 0.7% | +0.0 | 20% | ❌ 19 pts to go |
| P06M | 28835 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06T | 55504 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06 | 259 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P07 | 791 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P08 | 29605 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P09 | 276 | 3.6% | 3.6% | +0.0 | 50% | ❌ 46 pts to go |
| P10 | 2080 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P11 | 1799 | 0.4% | 0.4% | +0.0 | n/a | no target |
| P12 | 11 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P13 | 193993 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `commodity_codes`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 377 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P01T | 211 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P01_GOLD | 653 | 34.3% | 34.3% | -1.6 | 80% | ❌ 46 pts to go |
| P02 | 491 | 50.1% | 50.1% | -2.9 | 90% | ❌ 40 pts to go |
| P03 | 279 | 32.3% | 32.3% | -1.5 | 80% | ❌ 48 pts to go |
| P04 | 4868 | 16.4% | 16.4% | -5.8 | 85% | ❌ 69 pts to go |
| P05 | 429 | 7.7% | 7.7% | +1.3 | 50% | ❌ 42 pts to go |
| P06M | 28835 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06T | 55504 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06 | 259 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P07 | 791 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P08 | 29605 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P09 | 276 | 73.2% | 73.2% | +0.1 | 95% | ❌ 22 pts to go |
| P10 | 2080 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P11 | 1799 | 2.6% | 2.6% | +0.0 | 50% | ❌ 47 pts to go |
| P12 | 11 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P13 | 193993 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `buyer_org_codes`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 377 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P01T | 211 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P01_GOLD | 653 | 8.0% | 8.0% | -0.1 | 50% | ❌ 42 pts to go |
| P02 | 491 | 5.5% | 5.5% | -0.7 | 50% | ❌ 44 pts to go |
| P03 | 279 | 2.5% | 2.5% | -0.1 | 30% | ❌ 28 pts to go |
| P04 | 4868 | 0.4% | 0.4% | -0.2 | 30% | ❌ 30 pts to go |
| P05 | 429 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06M | 28835 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06T | 55504 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06 | 259 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P07 | 791 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P08 | 29605 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P09 | 276 | 0.4% | 0.4% | +0.0 | n/a | no target |
| P10 | 2080 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P11 | 1799 | 0.2% | 0.2% | +0.0 | n/a | no target |
| P12 | 11 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P13 | 193993 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `records_with_this_vendor`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 377 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P01T | 211 | 100.0% | 100.0% | +0.0 | 60% | ✅ met |
| P01_GOLD | 653 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P02 | 491 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P03 | 279 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P04 | 4868 | 100.0% | 100.0% | +0.0 | 95% | ✅ met |
| P05 | 429 | 100.0% | 100.0% | +0.0 | 70% | ✅ met |
| P06M | 28835 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P06T | 55504 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P06 | 259 | 100.0% | 100.0% | +0.0 | 50% | ✅ met |
| P07 | 791 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P08 | 29605 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P09 | 276 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P10 | 2080 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P11 | 1799 | 100.0% | 100.0% | +0.0 | 70% | ✅ met |
| P12 | 11 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P13 | 193993 | 0.0% | 0.0% | +0.0 | n/a | no target |

## 2. vendor

### `vendor_bn9`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 377 | 5.6% | 5.6% | -0.8 | 70% | ❌ 64 pts to go |
| P01T | 211 | 56.4% | 56.4% | -3.9 | 60% | 🟡 4 pts to go |
| P01_GOLD | 653 | 72.1% | 72.1% | -2.7 | 90% | ❌ 18 pts to go |
| P02 | 491 | 51.5% | 51.5% | -2.8 | 85% | ❌ 34 pts to go |
| P03 | 279 | 63.8% | 63.8% | -3.1 | 90% | ❌ 26 pts to go |
| P04 | 4868 | 28.4% | 28.4% | -9.8 | 75% | ❌ 47 pts to go |
| P05 | 429 | 54.8% | 54.8% | +0.1 | 50% | ✅ met |
| P06M | 28835 | 3.0% | 3.0% | +0.1 | n/a | no target |
| P06T | 55504 | 64.8% | 64.8% | +0.3 | n/a | no target |
| P06 | 259 | 42.5% | 42.5% | +0.4 | 40% | ✅ met |
| P07 | 791 | 32.4% | 32.4% | +0.3 | 50% | ❌ 18 pts to go |
| P08 | 29605 | 32.2% | 32.2% | +1.6 | 50% | ❌ 18 pts to go |
| P09 | 276 | 56.5% | 56.5% | -0.2 | 80% | ❌ 24 pts to go |
| P10 | 2080 | 38.9% | 38.9% | +0.1 | 40% | 🟡 1 pts to go |
| P11 | 1799 | 53.7% | 53.7% | -0.9 | 60% | 🟡 6 pts to go |
| P12 | 11 | 54.5% | 54.5% | +9.0 | 85% | ❌ 30 pts to go |
| P13 | 193993 | 44.7% | 44.7% | -0.1 | 0% by design | — leave (by design) |

### `vendor_registered_address`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 377 | 43.2% | 43.2% | -3.4 | n/a | no target |
| P01T | 211 | 56.9% | 56.9% | -2.9 | n/a | no target |
| P01_GOLD | 653 | 74.1% | 74.1% | +1.2 | 95% | ❌ 21 pts to go |
| P02 | 491 | 74.5% | 74.5% | -0.1 | 95% | ❌ 20 pts to go |
| P03 | 279 | 70.6% | 70.6% | +1.1 | 95% | ❌ 24 pts to go |
| P04 | 4868 | 54.0% | 54.0% | +0.9 | 95% | ❌ 41 pts to go |
| P05 | 429 | 58.7% | 58.7% | +0.6 | 70% | ❌ 11 pts to go |
| P06M | 28835 | 39.7% | 39.7% | -1.6 | n/a | no target |
| P06T | 55504 | 68.3% | 68.3% | +0.8 | n/a | no target |
| P06 | 259 | 38.2% | 38.2% | +0.0 | 80% | ❌ 42 pts to go |
| P07 | 791 | 31.5% | 31.5% | +0.5 | 70% | ❌ 38 pts to go |
| P08 | 29605 | 31.8% | 31.8% | +2.1 | 70% | ❌ 38 pts to go |
| P09 | 276 | 86.2% | 86.2% | +0.0 | 100% | ❌ 14 pts to go |
| P10 | 2080 | 39.4% | 39.4% | +0.2 | 70% | ❌ 31 pts to go |
| P11 | 1799 | 58.6% | 58.6% | +0.0 | 75% | ❌ 16 pts to go |
| P12 | 11 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P13 | 193993 | 40.3% | 40.3% | +0.1 | n/a | no target |

### `vendor_trading_name`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 377 | 21.8% | 21.8% | -0.3 | n/a | no target |
| P01T | 211 | 59.7% | 59.7% | -5.8 | n/a | no target |
| P01_GOLD | 653 | 50.8% | 50.8% | +2.0 | 60% | 🟡 9 pts to go |
| P02 | 491 | 57.8% | 57.8% | +2.0 | 60% | 🟡 2 pts to go |
| P03 | 279 | 53.8% | 53.8% | +1.5 | 60% | 🟡 6 pts to go |
| P04 | 4868 | 53.9% | 53.9% | +11.3 | 55% | 🟡 1 pts to go |
| P05 | 429 | 23.5% | 23.5% | +0.8 | 50% | ❌ 26 pts to go |
| P06M | 28835 | 11.1% | 11.1% | +1.6 | n/a | no target |
| P06T | 55504 | 69.9% | 69.9% | +2.0 | n/a | no target |
| P06 | 259 | 49.4% | 49.4% | +0.8 | n/a | no target |
| P07 | 791 | 39.4% | 39.4% | -0.2 | 55% | ❌ 16 pts to go |
| P08 | 29605 | 33.9% | 33.9% | +0.9 | 50% | ❌ 16 pts to go |
| P09 | 276 | 72.1% | 72.1% | +0.1 | 70% | ✅ met |
| P10 | 2080 | 47.5% | 47.5% | -0.6 | 55% | 🟡 8 pts to go |
| P11 | 1799 | 59.2% | 59.2% | +0.0 | 50% | ✅ met |
| P12 | 11 | 90.9% | 90.9% | +0.0 | n/a | no target |
| P13 | 193993 | 3.0% | 3.0% | -0.2 | n/a | no target |

### `vendor_phone`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 377 | 25.7% | 25.7% | -7.6 | n/a | no target |
| P01T | 211 | 77.7% | 77.7% | -1.8 | n/a | no target |
| P01_GOLD | 653 | 48.4% | 48.4% | -2.0 | 70% | ❌ 22 pts to go |
| P02 | 491 | 54.8% | 54.8% | -2.0 | 70% | ❌ 15 pts to go |
| P03 | 279 | 48.0% | 48.0% | -2.4 | 70% | ❌ 22 pts to go |
| P04 | 4868 | 47.3% | 47.3% | -7.6 | 65% | ❌ 18 pts to go |
| P05 | 429 | 29.6% | 29.6% | +0.5 | 60% | ❌ 30 pts to go |
| P06M | 28835 | 24.4% | 24.4% | -3.0 | n/a | no target |
| P06T | 55504 | 87.0% | 87.0% | +4.3 | n/a | no target |
| P06 | 259 | 71.8% | 71.8% | +2.5 | 40% | ✅ met |
| P07 | 791 | 66.8% | 66.8% | +1.8 | 85% | ❌ 18 pts to go |
| P08 | 29605 | 67.5% | 67.5% | +3.5 | 85% | ❌ 18 pts to go |
| P09 | 276 | 56.2% | 56.2% | -0.2 | 85% | ❌ 29 pts to go |
| P10 | 2080 | 65.4% | 65.4% | -0.7 | 85% | ❌ 20 pts to go |
| P11 | 1799 | 68.5% | 68.5% | +0.4 | 75% | 🟡 6 pts to go |
| P12 | 11 | 36.4% | 36.4% | +0.0 | n/a | no target |
| P13 | 193993 | 91.8% | 91.8% | +0.0 | 60% | ✅ met |

### `vendor_website`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 377 | 30.2% | 30.2% | -7.6 | n/a | no target |
| P01T | 211 | 98.1% | 98.1% | -0.2 | n/a | no target |
| P01_GOLD | 653 | 75.3% | 75.3% | -3.3 | 90% | ❌ 15 pts to go |
| P02 | 491 | 78.6% | 78.6% | -3.2 | 90% | ❌ 11 pts to go |
| P03 | 279 | 81.0% | 81.0% | -4.3 | 90% | 🟡 9 pts to go |
| P04 | 4868 | 71.3% | 71.3% | -11.5 | 85% | ❌ 14 pts to go |
| P05 | 429 | 44.8% | 44.8% | +0.3 | 70% | ❌ 25 pts to go |
| P06M | 28835 | 30.0% | 30.0% | -3.0 | n/a | no target |
| P06T | 55504 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P06 | 259 | 99.2% | 99.2% | -0.1 | 50% | ✅ met |
| P07 | 791 | 99.9% | 99.9% | +0.0 | 100% | 🟡 0 pts to go |
| P08 | 29605 | 99.9% | 99.9% | +0.0 | 100% | 🟡 0 pts to go |
| P09 | 276 | 77.5% | 77.5% | -0.3 | 100% | ❌ 22 pts to go |
| P10 | 2080 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P11 | 1799 | 97.4% | 97.4% | -0.6 | 100% | 🟡 3 pts to go |
| P12 | 11 | 54.5% | 54.5% | +0.0 | n/a | no target |
| P13 | 193993 | 100.0% | 100.0% | +0.0 | n/a | no target |

### `vendor_emails`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 377 | 13.8% | 13.8% | -2.3 | n/a | no target |
| P01T | 211 | 54.5% | 54.5% | -5.3 | n/a | no target |
| P01_GOLD | 653 | 41.8% | 41.8% | -1.6 | 70% | ❌ 28 pts to go |
| P02 | 491 | 45.2% | 45.2% | -2.0 | 75% | ❌ 30 pts to go |
| P03 | 279 | 43.0% | 43.0% | -1.7 | 75% | ❌ 32 pts to go |
| P04 | 4868 | 35.5% | 35.5% | -3.2 | 70% | ❌ 34 pts to go |
| P05 | 429 | 21.9% | 21.9% | +0.6 | 55% | ❌ 33 pts to go |
| P06M | 28835 | 6.6% | 6.6% | +0.7 | n/a | no target |
| P06T | 55504 | 42.6% | 42.6% | -4.8 | n/a | no target |
| P06 | 259 | 51.7% | 51.7% | +0.6 | n/a | no target |
| P07 | 791 | 53.6% | 53.6% | +0.9 | 70% | ❌ 16 pts to go |
| P08 | 29605 | 55.9% | 55.9% | +1.1 | 75% | ❌ 19 pts to go |
| P09 | 276 | 46.7% | 46.7% | -0.2 | 85% | ❌ 38 pts to go |
| P10 | 2080 | 44.6% | 44.6% | +0.2 | 80% | ❌ 35 pts to go |
| P11 | 1799 | 51.6% | 51.6% | -1.7 | 70% | ❌ 18 pts to go |
| P12 | 11 | 27.3% | 27.3% | +0.0 | n/a | no target |
| P13 | 193993 | 5.5% | 5.5% | +0.0 | n/a | no target |

### `vendor_logo_url`

> ceiling: needs the vendor's website first; sites that block automated readers (robots.txt / 403) are never read

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 377 | 29.2% | 29.2% | -8.6 | n/a | no target |
| P01T | 211 | 96.2% | 96.2% | -0.3 | n/a | no target |
| P01_GOLD | 653 | 69.8% | 69.8% | -3.1 | 90% | ❌ 20 pts to go |
| P02 | 491 | 73.5% | 73.5% | -3.2 | 90% | ❌ 16 pts to go |
| P03 | 279 | 77.8% | 77.8% | -4.2 | 90% | ❌ 12 pts to go |
| P04 | 4868 | 64.6% | 64.6% | -13.1 | 85% | ❌ 20 pts to go |
| P05 | 429 | 43.4% | 43.4% | +0.5 | 75% | ❌ 32 pts to go |
| P06M | 28835 | 29.1% | 29.1% | -3.8 | n/a | no target |
| P06T | 55504 | 97.8% | 97.8% | -0.5 | n/a | no target |
| P06 | 259 | 91.9% | 91.9% | +1.9 | n/a | no target |
| P07 | 791 | 94.2% | 94.2% | +2.5 | 100% | 🟡 6 pts to go |
| P08 | 29605 | 92.6% | 92.6% | +5.3 | 100% | 🟡 7 pts to go |
| P09 | 276 | 66.3% | 66.3% | -0.2 | n/a | no target |
| P10 | 2080 | 90.0% | 90.0% | -0.3 | 100% | 🟡 10 pts to go |
| P11 | 1799 | 90.3% | 90.3% | +0.1 | n/a | no target |
| P12 | 11 | 54.5% | 54.5% | +0.0 | n/a | no target |
| P13 | 193993 | 69.5% | 69.5% | -0.3 | n/a | no target |

### `vendor_neq`

> ceiling: only Québec-registered vendors have an NEQ; the share of QC vendors is reported next to the rate

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 377 | 33.4% | 33.4% | -3.5 | n/a | no target · QC vendors: 57 rows, 100.0% filled |
| P01T | 211 | 21.8% | 21.8% | +2.1 | n/a | no target · QC vendors: 34 rows, 88.2% filled |
| P01_GOLD | 653 | 45.5% | 45.5% | +2.0 | 95% | ❌ 50 pts to go · QC vendors: 49 rows, 98.0% filled |
| P02 | 491 | 57.6% | 57.6% | +1.6 | 95% | ❌ 37 pts to go · QC vendors: 111 rows, 100.0% filled |
| P03 | 279 | 44.4% | 44.4% | +1.5 | 95% | ❌ 51 pts to go · QC vendors: 19 rows, 100.0% filled |
| P04 | 4868 | 38.9% | 38.9% | +6.5 | 95% | ❌ 56 pts to go · QC vendors: 600 rows, 97.8% filled |
| P05 | 429 | 14.9% | 14.9% | +0.9 | n/a | no target · QC vendors: 38 rows, 100.0% filled |
| P06M | 28835 | 35.4% | 35.4% | -2.1 | n/a | no target · QC vendors: 7503 rows, 99.9% filled |
| P06T | 55504 | 37.5% | 37.5% | +6.9 | n/a | no target · QC vendors: 21174 rows, 96.1% filled |
| P06 | 259 | 6.9% | 6.9% | -0.2 | n/a | no target · QC vendors: 12 rows, 66.7% filled |
| P07 | 791 | 6.7% | 6.7% | -0.2 | n/a | no target · QC vendors: 45 rows, 77.8% filled |
| P08 | 29605 | 7.1% | 7.1% | +0.1 | n/a | no target · QC vendors: 1804 rows, 92.7% filled |
| P09 | 276 | 73.6% | 73.6% | +0.1 | 95% | ❌ 21 pts to go · QC vendors: 100 rows, 100.0% filled |
| P10 | 2080 | 15.8% | 15.8% | +0.1 | n/a | no target · QC vendors: 201 rows, 92.5% filled |
| P11 | 1799 | 20.7% | 20.7% | +1.1 | n/a | no target · QC vendors: 321 rows, 94.1% filled |
| P12 | 11 | 81.8% | 81.8% | +0.0 | n/a | no target · QC vendors: 2 rows, 100.0% filled |
| P13 | 193993 | 22.5% | 22.5% | +0.3 | n/a | no target · QC vendors: 43620 rows, 100.0% filled |

### `vendor_years_in_business`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 377 | 42.7% | 42.7% | -3.5 | n/a | no target · vendors with a registry record: 161 rows, 100.0% filled |
| P01T | 211 | 56.9% | 56.9% | -2.9 | n/a | no target · vendors with a registry record: 120 rows, 100.0% filled |
| P01_GOLD | 653 | 81.8% | 81.8% | +0.9 | 100% | ❌ 18 pts to go · vendors with a registry record: 534 rows, 100.0% filled |
| P02 | 491 | 78.4% | 78.4% | +0.0 | 100% | ❌ 22 pts to go · vendors with a registry record: 385 rows, 100.0% filled |
| P03 | 279 | 78.9% | 78.9% | +0.7 | 100% | ❌ 21 pts to go · vendors with a registry record: 220 rows, 100.0% filled |
| P04 | 4868 | 54.7% | 54.7% | +0.7 | 100% | ❌ 45 pts to go · vendors with a registry record: 2662 rows, 100.0% filled |
| P05 | 429 | 63.2% | 63.2% | +0.4 | n/a | no target · vendors with a registry record: 271 rows, 100.0% filled |
| P06M | 28835 | 39.7% | 39.7% | -1.5 | n/a | no target · vendors with a registry record: 11453 rows, 100.0% filled |
| P06T | 55504 | 68.3% | 68.3% | +0.7 | n/a | no target · vendors with a registry record: 37936 rows, 100.0% filled |
| P06 | 259 | 39.0% | 39.0% | -0.3 | n/a | no target · vendors with a registry record: 101 rows, 100.0% filled |
| P07 | 791 | 32.1% | 32.1% | +0.3 | n/a | no target · vendors with a registry record: 254 rows, 100.0% filled |
| P08 | 29605 | 31.9% | 31.9% | +1.9 | n/a | no target · vendors with a registry record: 9438 rows, 100.0% filled |
| P09 | 276 | 89.5% | 89.5% | +0.0 | n/a | no target · vendors with a registry record: 247 rows, 100.0% filled |
| P10 | 2080 | 40.3% | 40.3% | +0.2 | n/a | no target · vendors with a registry record: 838 rows, 100.0% filled |
| P11 | 1799 | 59.4% | 59.4% | +0.1 | n/a | no target · vendors with a registry record: 1068 rows, 100.0% filled |
| P12 | 11 | 100.0% | 100.0% | +0.0 | n/a | no target · vendors with a registry record: 11 rows, 100.0% filled |
| P13 | 193993 | 40.3% | 40.3% | +0.1 | n/a | no target · vendors with a registry record: 78232 rows, 100.0% filled |

## 3. buyer

### `buyer_legal_name_as_published`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 377 | 97.6% | 97.6% | +1.2 | 90% | ✅ met |
| P01T | 211 | 70.1% | 70.1% | -0.6 | 90% | ❌ 20 pts to go |
| P01_GOLD | 653 | 88.2% | 88.2% | +0.8 | 95% | 🟡 7 pts to go |
| P02 | 491 | 88.4% | 88.4% | +0.2 | 95% | 🟡 7 pts to go |
| P03 | 279 | 83.5% | 83.5% | +0.4 | 85% | 🟡 2 pts to go |
| P04 | 4868 | 68.4% | 68.4% | +3.9 | 90% | ❌ 22 pts to go |
| P05 | 429 | 76.7% | 76.7% | -1.3 | 75% | ✅ met |
| P06M | 28835 | 95.0% | 95.0% | +1.2 | n/a | no target |
| P06T | 55504 | 37.5% | 37.5% | +0.6 | n/a | no target |
| P06 | 259 | 72.6% | 72.6% | +1.5 | 80% | 🟡 7 pts to go |
| P07 | 791 | 61.2% | 61.3% | +3.0 | 80% | ❌ 19 pts to go |
| P08 | 29605 | 56.8% | 56.8% | +4.9 | 75% | ❌ 18 pts to go |
| P09 | 276 | 75.4% | 75.4% | -0.2 | 95% | ❌ 20 pts to go |
| P10 | 2080 | 46.0% | 46.1% | -0.8 | 70% | ❌ 24 pts to go |
| P11 | 1799 | 32.1% | 32.1% | +0.3 | 65% | ❌ 33 pts to go |
| P12 | 11 | 72.7% | 72.7% | +0.0 | 80% | 🟡 7 pts to go |
| P13 | 193993 | 38.8% | 38.8% | -6.8 | 60% | ❌ 21 pts to go |

### `buyer_bn_as_published`

> ceiling: a buyer's BN is public only where the buyer prints it or a public dataset carries it (CRA charities, federal grants & contributions recipients, business registries for corporations); municipalities rarely publish theirs

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 377 | 14.3% | 14.3% | -4.2 | 50% | ❌ 36 pts to go |
| P01T | 211 | 16.1% | 16.1% | -0.1 | n/a | no target |
| P01_GOLD | 653 | 19.1% | 19.1% | -0.7 | 40% | ❌ 21 pts to go |
| P02 | 491 | 19.1% | 19.1% | -0.8 | 40% | ❌ 21 pts to go |
| P03 | 279 | 19.4% | 19.4% | -0.9 | 40% | ❌ 21 pts to go |
| P04 | 4868 | 14.0% | 14.0% | -2.3 | 40% | ❌ 26 pts to go |
| P05 | 429 | 21.0% | 21.0% | +0.1 | 25% | 🟡 4 pts to go |
| P06M | 28835 | 20.1% | 20.1% | -0.3 | n/a | no target |
| P06T | 55504 | 10.2% | 10.2% | +2.7 | n/a | no target |
| P06 | 259 | 21.2% | 21.2% | +3.7 | 35% | ❌ 14 pts to go |
| P07 | 791 | 22.9% | 22.9% | +3.8 | 35% | ❌ 12 pts to go |
| P08 | 29605 | 22.6% | 22.6% | +4.9 | 35% | ❌ 12 pts to go |
| P09 | 276 | 16.7% | 16.7% | +0.0 | n/a | no target |
| P10 | 2080 | 9.3% | 9.3% | +2.2 | 30% | ❌ 21 pts to go |
| P11 | 1799 | 9.6% | 9.6% | +3.1 | n/a | no target |
| P12 | 11 | 18.2% | 18.2% | +0.0 | n/a | no target |
| P13 | 193993 | 10.7% | 10.7% | -1.8 | 30% | ❌ 19 pts to go |

### `buyer_address`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 377 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P01T | 211 | 85.3% | 85.3% | +0.1 | 100% | ❌ 15 pts to go |
| P01_GOLD | 653 | 91.7% | 91.7% | +0.6 | 100% | 🟡 8 pts to go |
| P02 | 491 | 96.7% | 96.7% | +0.1 | 100% | 🟡 3 pts to go |
| P03 | 279 | 89.6% | 89.6% | +0.1 | 100% | ❌ 10 pts to go |
| P04 | 4868 | 78.7% | 78.7% | +6.2 | 100% | ❌ 21 pts to go |
| P05 | 429 | 90.0% | 90.0% | +0.0 | 100% | 🟡 10 pts to go |
| P06M | 28835 | 99.6% | 99.6% | +0.2 | n/a | no target |
| P06T | 55504 | 59.8% | 59.8% | +1.1 | n/a | no target |
| P06 | 259 | 82.2% | 82.2% | +0.1 | 95% | ❌ 13 pts to go |
| P07 | 791 | 86.7% | 86.7% | +1.3 | 95% | 🟡 8 pts to go |
| P08 | 29605 | 85.4% | 85.4% | +0.9 | 95% | 🟡 10 pts to go |
| P09 | 276 | 96.4% | 96.4% | +0.0 | 100% | 🟡 4 pts to go |
| P10 | 2080 | 54.3% | 54.3% | -0.3 | 95% | ❌ 41 pts to go |
| P11 | 1799 | 61.6% | 61.6% | +0.7 | 80% | ❌ 18 pts to go |
| P12 | 11 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P13 | 193993 | 100.0% | 100.0% | +0.0 | 95% | ✅ met |

### `buyer_phone`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 377 | 61.0% | 61.0% | -10.1 | n/a | no target |
| P01T | 211 | 72.5% | 72.5% | -1.7 | n/a | no target |
| P01_GOLD | 653 | 71.4% | 71.4% | -1.8 | 90% | ❌ 19 pts to go |
| P02 | 491 | 75.6% | 75.6% | -2.8 | 95% | ❌ 19 pts to go |
| P03 | 279 | 71.3% | 71.3% | -2.8 | 95% | ❌ 24 pts to go |
| P04 | 4868 | 59.9% | 59.9% | -9.6 | 95% | ❌ 35 pts to go |
| P05 | 429 | 71.6% | 71.6% | -0.9 | 90% | ❌ 18 pts to go |
| P06M | 28835 | 69.8% | 69.8% | -6.9 | n/a | no target |
| P06T | 55504 | 58.1% | 58.1% | -0.5 | n/a | no target |
| P06 | 259 | 70.3% | 70.3% | +4.9 | 95% | ❌ 25 pts to go |
| P07 | 791 | 67.9% | 67.9% | +8.2 | 90% | ❌ 22 pts to go |
| P08 | 29605 | 70.9% | 70.9% | +12.3 | 95% | ❌ 24 pts to go |
| P09 | 276 | 85.5% | 85.5% | -0.3 | 100% | ❌ 14 pts to go |
| P10 | 2080 | 53.4% | 53.4% | -0.4 | 95% | ❌ 42 pts to go |
| P11 | 1799 | 32.7% | 32.7% | +2.0 | 75% | ❌ 42 pts to go |
| P12 | 11 | 81.8% | 81.8% | +0.0 | n/a | no target |
| P13 | 193993 | 57.5% | 57.5% | -10.4 | 95% | ❌ 38 pts to go |

### `buyer_logo_url`

> ceiling: sites that block automated readers (robots.txt / 403) are never read; an og:image that looks like a photo is labelled

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 377 | 70.6% | 70.6% | -12.9 | n/a | no target |
| P01T | 211 | 90.5% | 90.5% | -1.2 | 95% | 🟡 4 pts to go |
| P01_GOLD | 653 | 82.4% | 82.4% | -2.6 | 90% | 🟡 8 pts to go |
| P02 | 491 | 88.2% | 88.2% | -2.8 | 95% | 🟡 7 pts to go |
| P03 | 279 | 81.4% | 81.4% | -2.4 | 95% | ❌ 14 pts to go |
| P04 | 4868 | 78.1% | 78.1% | -13.5 | 90% | ❌ 12 pts to go |
| P05 | 429 | 92.5% | 92.5% | +0.1 | 95% | 🟡 2 pts to go |
| P06M | 28835 | 79.4% | 79.4% | -5.9 | n/a | no target |
| P06T | 55504 | 85.8% | 85.8% | +1.2 | n/a | no target |
| P06 | 259 | 93.1% | 93.1% | +7.7 | 100% | 🟡 7 pts to go |
| P07 | 791 | 94.4% | 94.4% | +10.8 | 100% | 🟡 6 pts to go |
| P08 | 29605 | 94.9% | 94.9% | +17.1 | 100% | 🟡 5 pts to go |
| P09 | 276 | 73.6% | 73.6% | -0.6 | n/a | no target |
| P10 | 2080 | 94.2% | 94.2% | -0.2 | 100% | 🟡 6 pts to go |
| P11 | 1799 | 53.9% | 53.9% | +2.8 | 80% | ❌ 26 pts to go |
| P12 | 11 | 90.9% | 90.9% | +0.0 | n/a | no target |
| P13 | 193993 | 69.9% | 69.9% | -10.9 | 95% | ❌ 25 pts to go |

## 4. AP

### `ap_contact_name_as_published`

> ceiling: owner 2026-11-08: the AP contact person the organisation itself names on its AP / finance page is allowed (name + role phrase, quoted); mailboxes stay organisational; many bodies publish no AP person

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 377 | 2.4% | 2.4% | -0.8 | n/a | no target |
| P01T | 211 | 9.5% | 9.5% | +0.8 | n/a | no target |
| P01_GOLD | 653 | 13.6% | 13.6% | -0.4 | 25% | ❌ 11 pts to go |
| P02 | 491 | 23.8% | 23.8% | -1.0 | 40% | ❌ 16 pts to go |
| P03 | 279 | 8.6% | 8.6% | -0.4 | 20% | ❌ 11 pts to go |
| P04 | 4868 | 2.4% | 2.4% | -0.9 | 20% | ❌ 18 pts to go |
| P05 | 429 | 3.0% | 3.0% | -0.3 | 15% | ❌ 12 pts to go |
| P06M | 28835 | 0.2% | 0.2% | -0.1 | n/a | no target |
| P06T | 55504 | 0.3% | 0.3% | +0.1 | n/a | no target |
| P06 | 259 | 5.4% | 5.4% | +0.0 | n/a | no target |
| P07 | 791 | 8.0% | 8.0% | +0.1 | n/a | no target |
| P08 | 29605 | 0.2% | 0.2% | +0.0 | n/a | no target |
| P09 | 276 | 7.2% | 7.2% | -0.4 | n/a | no target |
| P10 | 2080 | 0.8% | 0.8% | +0.0 | n/a | no target |
| P11 | 1799 | 0.7% | 0.7% | +0.0 | n/a | no target |
| P12 | 11 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P13 | 193993 | 0.2% | 0.2% | +0.0 | n/a | no target |

### `ap_phone`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 377 | 11.9% | 11.9% | -4.2 | n/a | no target |
| P01T | 211 | 18.0% | 18.0% | -1.2 | 70% | ❌ 52 pts to go |
| P01_GOLD | 653 | 40.7% | 40.7% | -1.4 | 80% | ❌ 39 pts to go |
| P02 | 491 | 54.6% | 54.6% | -2.7 | 90% | ❌ 35 pts to go |
| P03 | 279 | 17.9% | 17.9% | -1.3 | 60% | ❌ 42 pts to go |
| P04 | 4868 | 14.9% | 14.9% | -5.3 | 85% | ❌ 70 pts to go |
| P05 | 429 | 11.0% | 11.0% | -0.1 | 50% | ❌ 39 pts to go |
| P06M | 28835 | 0.5% | 0.5% | -0.1 | n/a | no target |
| P06T | 55504 | 0.5% | 0.5% | +0.0 | n/a | no target |
| P06 | 259 | 13.5% | 13.5% | +0.3 | n/a | no target |
| P07 | 791 | 9.5% | 9.5% | +0.4 | n/a | no target |
| P08 | 29605 | 0.5% | 0.5% | +0.0 | n/a | no target |
| P09 | 276 | 72.1% | 72.1% | +0.1 | 95% | ❌ 23 pts to go |
| P10 | 2080 | 1.4% | 1.4% | -0.2 | n/a | no target |
| P11 | 1799 | 12.7% | 12.7% | -0.3 | n/a | no target |
| P12 | 11 | 27.3% | 27.3% | +0.0 | n/a | no target |
| P13 | 193993 | 0.3% | 0.3% | +0.0 | n/a | no target |

### `invoice_mailing_address`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 377 | 4.5% | 4.5% | -1.1 | n/a | no target |
| P01T | 211 | 10.9% | 10.9% | +1.7 | n/a | no target |
| P01_GOLD | 653 | 32.5% | 32.5% | -1.3 | 70% | ❌ 38 pts to go |
| P02 | 491 | 37.1% | 37.1% | -1.6 | 75% | ❌ 38 pts to go |
| P03 | 279 | 17.9% | 17.9% | -1.3 | 55% | ❌ 37 pts to go |
| P04 | 4868 | 14.9% | 14.9% | -5.3 | 75% | ❌ 60 pts to go |
| P05 | 429 | 10.3% | 10.3% | +0.1 | 50% | ❌ 40 pts to go |
| P06M | 28835 | 0.2% | 0.2% | +0.0 | n/a | no target |
| P06T | 55504 | 0.3% | 0.3% | +0.0 | n/a | no target |
| P06 | 259 | 5.4% | 5.4% | -0.3 | n/a | no target |
| P07 | 791 | 4.8% | 4.8% | +0.2 | n/a | no target |
| P08 | 29605 | 0.2% | 0.2% | +0.0 | n/a | no target |
| P09 | 276 | 68.8% | 68.8% | +0.1 | 95% | ❌ 26 pts to go |
| P10 | 2080 | 0.7% | 0.7% | -0.1 | n/a | no target |
| P11 | 1799 | 12.5% | 12.5% | -0.3 | n/a | no target |
| P12 | 11 | 18.2% | 18.2% | +0.0 | n/a | no target |
| P13 | 193993 | 0.1% | 0.1% | -0.1 | n/a | no target |

### `invoicing_requirements`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 377 | 5.3% | 5.3% | -2.3 | n/a | no target |
| P01T | 211 | 8.5% | 8.5% | -0.2 | n/a | no target |
| P01_GOLD | 653 | 54.8% | 55.0% | -2.3 | 80% | ❌ 25 pts to go |
| P02 | 491 | 43.4% | 43.6% | -1.9 | 75% | ❌ 32 pts to go |
| P03 | 279 | 34.1% | 34.1% | -2.0 | 70% | ❌ 36 pts to go |
| P04 | 4868 | 14.7% | 15.0% | -5.2 | 70% | ❌ 55 pts to go |
| P05 | 429 | 13.8% | 13.8% | -0.2 | 50% | ❌ 36 pts to go |
| P06M | 28835 | 0.2% | 0.2% | -0.1 | n/a | no target |
| P06T | 55504 | 0.2% | 0.2% | +0.0 | n/a | no target |
| P06 | 259 | 12.7% | 12.7% | -0.5 | n/a | no target |
| P07 | 791 | 1.0% | 1.0% | -0.1 | n/a | no target |
| P08 | 29605 | 0.3% | 0.3% | +0.0 | n/a | no target |
| P09 | 276 | 46.7% | 47.1% | -0.2 | 80% | ❌ 33 pts to go |
| P10 | 2080 | 1.1% | 1.1% | +0.0 | n/a | no target |
| P11 | 1799 | 4.3% | 4.4% | -0.2 | n/a | no target |
| P12 | 11 | 36.4% | 36.4% | +0.0 | n/a | no target |
| P13 | 193993 | 0.1% | 0.1% | +0.0 | n/a | no target |

### `payment_terms_as_published`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 377 | 11.7% | 11.7% | -3.2 | n/a | no target |
| P01T | 211 | 20.4% | 20.4% | +1.2 | 60% | ❌ 40 pts to go |
| P01_GOLD | 653 | 59.6% | 59.6% | -2.6 | 70% | ❌ 10 pts to go |
| P02 | 491 | 37.7% | 37.7% | -1.8 | 50% | ❌ 12 pts to go |
| P03 | 279 | 45.2% | 45.2% | -2.5 | 55% | 🟡 10 pts to go |
| P04 | 4868 | 9.0% | 9.0% | -3.5 | 40% | ❌ 31 pts to go |
| P05 | 429 | 16.1% | 16.1% | -0.5 | 40% | ❌ 24 pts to go |
| P06M | 28835 | 2.2% | 2.2% | -0.6 | n/a | no target |
| P06T | 55504 | 1.4% | 1.4% | -0.1 | n/a | no target |
| P06 | 259 | 17.4% | 17.4% | -0.8 | n/a | no target |
| P07 | 791 | 4.9% | 4.9% | +0.0 | n/a | no target |
| P08 | 29605 | 2.1% | 2.1% | +0.0 | n/a | no target |
| P09 | 276 | 6.2% | 6.2% | +0.4 | n/a | no target |
| P10 | 2080 | 4.9% | 4.9% | -0.2 | n/a | no target |
| P11 | 1799 | 3.9% | 3.9% | -0.1 | n/a | no target |
| P12 | 11 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P13 | 193993 | 0.6% | 0.6% | -0.1 | n/a | no target |

### `po_required_as_published`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 377 | 16.7% | 16.7% | -5.0 | n/a | no target |
| P01T | 211 | 26.1% | 26.1% | -1.8 | 65% | ❌ 39 pts to go |
| P01_GOLD | 653 | 65.2% | 65.2% | -3.4 | 70% | 🟡 5 pts to go |
| P02 | 491 | 22.8% | 22.8% | -0.9 | 50% | ❌ 27 pts to go |
| P03 | 279 | 48.0% | 48.0% | -2.4 | 60% | ❌ 12 pts to go |
| P04 | 4868 | 4.1% | 4.1% | -1.5 | 40% | ❌ 36 pts to go |
| P05 | 429 | 19.6% | 19.6% | -0.3 | 45% | ❌ 25 pts to go |
| P06M | 28835 | 1.3% | 1.3% | -0.4 | n/a | no target |
| P06T | 55504 | 0.6% | 0.6% | +0.0 | n/a | no target |
| P06 | 259 | 26.3% | 26.3% | -3.0 | n/a | no target |
| P07 | 791 | 4.9% | 4.9% | -0.2 | n/a | no target |
| P08 | 29605 | 0.9% | 0.9% | +0.0 | n/a | no target |
| P09 | 276 | 10.9% | 10.9% | +0.0 | n/a | no target |
| P10 | 2080 | 3.0% | 3.0% | -0.3 | n/a | no target |
| P11 | 1799 | 3.6% | 3.6% | +0.0 | n/a | no target |
| P12 | 11 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P13 | 193993 | 0.2% | 0.2% | +0.0 | n/a | no target |

### `invoice_portal_url`

> ceiling: only portals the buyer names on its own pages; informational tax-authority links are not portals

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 377 | 9.5% | 9.5% | -2.5 | n/a | no target |
| P01T | 211 | 13.3% | 13.3% | +0.6 | n/a | no target |
| P01_GOLD | 653 | 47.8% | 47.8% | -2.4 | 50% | 🟡 2 pts to go |
| P02 | 491 | 35.6% | 35.6% | -2.0 | n/a | no target |
| P03 | 279 | 48.4% | 48.4% | -2.4 | 60% | ❌ 12 pts to go |
| P04 | 4868 | 9.3% | 9.3% | -3.5 | n/a | no target |
| P05 | 429 | 15.2% | 15.2% | +0.0 | n/a | no target |
| P06M | 28835 | 0.6% | 0.6% | -0.2 | n/a | no target |
| P06T | 55504 | 0.3% | 0.3% | +0.0 | n/a | no target |
| P06 | 259 | 18.5% | 18.5% | -1.9 | n/a | no target |
| P07 | 791 | 5.1% | 5.1% | -0.6 | n/a | no target |
| P08 | 29605 | 0.4% | 0.4% | +0.0 | n/a | no target |
| P09 | 276 | 20.7% | 20.7% | +0.0 | n/a | no target |
| P10 | 2080 | 2.2% | 2.2% | -0.3 | n/a | no target |
| P11 | 1799 | 2.5% | 2.5% | -0.2 | n/a | no target |
| P12 | 11 | 18.2% | 18.2% | +0.0 | n/a | no target |
| P13 | 193993 | 0.1% | 0.1% | -0.1 | n/a | no target |

### `buyer_payment_method_preference`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 377 | 6.4% | 6.4% | -2.4 | 15% | 🟡 9 pts to go |
| P01T | 211 | 12.8% | 12.8% | +0.1 | 15% | 🟡 2 pts to go |
| P01_GOLD | 653 | 33.4% | 33.4% | -1.7 | 40% | 🟡 7 pts to go |
| P02 | 491 | 11.8% | 12.0% | -0.4 | 25% | ❌ 13 pts to go |
| P03 | 279 | 15.4% | 15.4% | -1.1 | 25% | 🟡 10 pts to go |
| P04 | 4868 | 2.0% | 2.0% | -0.7 | 15% | ❌ 13 pts to go |
| P05 | 429 | 6.3% | 6.3% | -0.3 | 15% | 🟡 9 pts to go |
| P06M | 28835 | 0.7% | 0.7% | -0.1 | 15% | ❌ 14 pts to go |
| P06T | 55504 | 0.6% | 0.6% | -0.1 | 15% | ❌ 14 pts to go |
| P06 | 259 | 8.5% | 8.5% | -0.8 | 15% | 🟡 6 pts to go |
| P07 | 791 | 3.4% | 3.4% | +0.0 | 15% | ❌ 12 pts to go |
| P08 | 29605 | 0.6% | 0.6% | +0.1 | 15% | ❌ 14 pts to go |
| P09 | 276 | 1.1% | 1.1% | +0.0 | 15% | ❌ 14 pts to go |
| P10 | 2080 | 1.3% | 1.3% | -0.1 | 15% | ❌ 14 pts to go |
| P11 | 1799 | 1.1% | 1.1% | -0.1 | 15% | ❌ 14 pts to go |
| P12 | 11 | 0.0% | 0.0% | +0.0 | 15% | ❌ 15 pts to go |
| P13 | 193993 | 0.6% | 0.6% | +0.0 | 15% | ❌ 14 pts to go |

### `buyer_tax_exempt_status`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 377 | 4.8% | 4.8% | -0.8 | 15% | ❌ 10 pts to go |
| P01T | 211 | 11.4% | 11.4% | +0.5 | 25% | ❌ 14 pts to go |
| P01_GOLD | 653 | 27.9% | 27.9% | -1.0 | 25% | ✅ met |
| P02 | 491 | 23.8% | 23.8% | -1.6 | 15% | ✅ met |
| P03 | 279 | 20.8% | 20.8% | -1.0 | 15% | ✅ met |
| P04 | 4868 | 2.9% | 2.9% | -1.1 | 15% | ❌ 12 pts to go |
| P05 | 429 | 11.4% | 11.4% | +0.0 | 15% | 🟡 4 pts to go |
| P06M | 28835 | 0.5% | 0.5% | -0.1 | 15% | ❌ 14 pts to go |
| P06T | 55504 | 0.2% | 0.2% | +0.0 | 15% | ❌ 15 pts to go |
| P06 | 259 | 6.9% | 6.9% | -0.2 | 15% | 🟡 8 pts to go |
| P07 | 791 | 1.6% | 1.6% | -0.2 | 15% | ❌ 13 pts to go |
| P08 | 29605 | 0.3% | 0.3% | +0.0 | 15% | ❌ 15 pts to go |
| P09 | 276 | 1.4% | 1.4% | -0.1 | 15% | ❌ 14 pts to go |
| P10 | 2080 | 1.5% | 1.5% | -0.1 | 15% | ❌ 14 pts to go |
| P11 | 1799 | 1.8% | 1.8% | +0.0 | 15% | ❌ 13 pts to go |
| P12 | 11 | 0.0% | 0.0% | +0.0 | 15% | ❌ 15 pts to go |
| P13 | 193993 | 0.1% | 0.1% | +0.0 | 15% | ❌ 15 pts to go |

### `buyer_ap_cycle_published`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 377 | 1.1% | 1.1% | -0.5 | 20% | ❌ 19 pts to go |
| P01T | 211 | 3.3% | 3.3% | +0.2 | 20% | ❌ 17 pts to go |
| P01_GOLD | 653 | 4.1% | 4.1% | -0.2 | 20% | ❌ 16 pts to go |
| P02 | 491 | 1.4% | 1.4% | -0.1 | 20% | ❌ 19 pts to go |
| P03 | 279 | 1.4% | 1.4% | -0.5 | 20% | ❌ 19 pts to go |
| P04 | 4868 | 0.6% | 0.6% | -0.1 | 20% | ❌ 19 pts to go |
| P05 | 429 | 0.9% | 0.9% | +0.0 | 20% | ❌ 19 pts to go |
| P06M | 28835 | 0.0% | 0.0% | +0.0 | 20% | ❌ 20 pts to go |
| P06T | 55504 | 0.0% | 0.0% | +0.0 | 20% | ❌ 20 pts to go |
| P06 | 259 | 1.2% | 1.2% | -0.2 | 20% | ❌ 19 pts to go |
| P07 | 791 | 0.3% | 0.3% | +0.1 | 20% | ❌ 20 pts to go |
| P08 | 29605 | 0.0% | 0.0% | +0.0 | 20% | ❌ 20 pts to go |
| P09 | 276 | 0.0% | 0.0% | +0.0 | 20% | ❌ 20 pts to go |
| P10 | 2080 | 0.3% | 0.3% | +0.0 | 20% | ❌ 20 pts to go |
| P11 | 1799 | 0.1% | 0.1% | +0.0 | 20% | ❌ 20 pts to go |
| P12 | 11 | 0.0% | 0.0% | +0.0 | 20% | ❌ 20 pts to go |
| P13 | 193993 | 0.0% | 0.0% | +0.0 | 20% | ❌ 20 pts to go |

### `buyer_esignature_preference`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 377 | 1.1% | 1.1% | -0.5 | 15% | ❌ 14 pts to go |
| P01T | 211 | 2.4% | 2.4% | -0.7 | 15% | ❌ 13 pts to go |
| P01_GOLD | 653 | 10.4% | 10.4% | -0.1 | 15% | 🟡 5 pts to go |
| P02 | 491 | 10.6% | 10.6% | -0.9 | 15% | 🟡 4 pts to go |
| P03 | 279 | 20.1% | 20.1% | -0.6 | 15% | ✅ met |
| P04 | 4868 | 1.7% | 1.7% | -0.7 | 15% | ❌ 13 pts to go |
| P05 | 429 | 2.8% | 2.8% | +0.0 | 15% | ❌ 12 pts to go |
| P06M | 28835 | 0.3% | 0.3% | -0.1 | 15% | ❌ 15 pts to go |
| P06T | 55504 | 0.2% | 0.2% | +0.0 | 15% | ❌ 15 pts to go |
| P06 | 259 | 3.9% | 3.9% | +0.0 | 15% | ❌ 11 pts to go |
| P07 | 791 | 1.3% | 1.3% | +0.1 | 15% | ❌ 14 pts to go |
| P08 | 29605 | 0.3% | 0.3% | +0.0 | 15% | ❌ 15 pts to go |
| P09 | 276 | 0.7% | 0.7% | +0.0 | 15% | ❌ 14 pts to go |
| P10 | 2080 | 1.1% | 1.1% | +0.0 | 15% | ❌ 14 pts to go |
| P11 | 1799 | 0.7% | 0.7% | -0.1 | 15% | ❌ 14 pts to go |
| P12 | 11 | 0.0% | 0.0% | +0.0 | 15% | ❌ 15 pts to go |
| P13 | 193993 | 0.1% | 0.1% | +0.0 | 15% | ❌ 15 pts to go |

### `ap_system_hint`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 377 | 10.6% | 10.6% | -1.8 | 20% | 🟡 9 pts to go |
| P01T | 211 | 14.2% | 14.2% | +0.7 | 40% | ❌ 26 pts to go |
| P01_GOLD | 653 | 44.6% | 44.6% | -2.0 | 40% | ✅ met |
| P02 | 491 | 41.1% | 41.1% | -2.1 | 20% | ✅ met |
| P03 | 279 | 46.2% | 46.2% | -2.3 | 35% | ✅ met |
| P04 | 4868 | 10.9% | 10.9% | -4.0 | 20% | 🟡 9 pts to go |
| P05 | 429 | 15.6% | 15.6% | +0.0 | 20% | 🟡 4 pts to go |
| P06M | 28835 | 0.9% | 0.9% | -0.1 | 20% | ❌ 19 pts to go |
| P06T | 55504 | 0.6% | 0.6% | +0.0 | 20% | ❌ 19 pts to go |
| P06 | 259 | 19.3% | 19.3% | -1.8 | 20% | 🟡 1 pts to go |
| P07 | 791 | 5.7% | 5.7% | -0.4 | 20% | ❌ 14 pts to go |
| P08 | 29605 | 0.8% | 0.8% | +0.0 | 20% | ❌ 19 pts to go |
| P09 | 276 | 21.0% | 21.0% | -0.1 | 20% | ✅ met |
| P10 | 2080 | 3.5% | 3.5% | -0.3 | 20% | ❌ 16 pts to go |
| P11 | 1799 | 3.1% | 3.1% | -0.1 | 20% | ❌ 17 pts to go |
| P12 | 11 | 9.1% | 9.1% | +0.0 | 20% | ❌ 11 pts to go |
| P13 | 193993 | 0.3% | 0.3% | -0.1 | 20% | ❌ 20 pts to go |

## 5. contract

### `contract_value`

> ceiling: rows proven by a lobbying filing, a news release, an auditor appointment, a customer story or a vendor's client list have no contract value by nature (≈17 % of P01 Gold); bids&tenders awards now carry the awarded bidder's submitted price when no award value was published

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 377 | 12.7% | 12.7% | -5.4 | n/a | no target |
| P01T | 211 | 0.5% | 0.5% | +0.1 | n/a | no target |
| P01_GOLD | 653 | 68.9% | 68.9% | -2.7 | 95% | ❌ 26 pts to go |
| P02 | 491 | 62.9% | 62.9% | -3.3 | 95% | ❌ 32 pts to go |
| P03 | 279 | 54.8% | 54.8% | -3.1 | 90% | ❌ 35 pts to go |
| P04 | 4868 | 20.5% | 20.5% | -6.0 | 85% | ❌ 64 pts to go |
| P05 | 429 | 39.4% | 39.4% | +0.5 | 75% | ❌ 36 pts to go |
| P06M | 28835 | 23.9% | 23.9% | -4.2 | n/a | no target |
| P06T | 55504 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06 | 259 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P07 | 791 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P08 | 29605 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P09 | 276 | 89.1% | 89.1% | +0.0 | 100% | ❌ 11 pts to go |
| P10 | 2080 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P11 | 1799 | 3.9% | 3.9% | +0.1 | 60% | ❌ 56 pts to go |
| P12 | 11 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P13 | 193993 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `currency`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 377 | 12.7% | 12.7% | -5.4 | n/a | no target |
| P01T | 211 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P01_GOLD | 653 | 70.8% | 70.8% | -2.7 | 100% | ❌ 29 pts to go |
| P02 | 491 | 64.8% | 64.8% | -3.4 | 100% | ❌ 35 pts to go |
| P03 | 279 | 57.3% | 57.3% | -3.2 | n/a | no target |
| P04 | 4868 | 20.9% | 20.9% | -6.1 | 95% | ❌ 74 pts to go |
| P05 | 429 | 35.2% | 35.2% | +0.6 | 80% | ❌ 45 pts to go |
| P06M | 28835 | 23.9% | 23.9% | -4.2 | n/a | no target |
| P06T | 55504 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06 | 259 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P07 | 791 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P08 | 29605 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P09 | 276 | 91.7% | 91.7% | +0.1 | 100% | 🟡 8 pts to go |
| P10 | 2080 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P11 | 1799 | 4.1% | 4.1% | +0.1 | n/a | no target |
| P12 | 11 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P13 | 193993 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `start_date`

> ceiling: most award notices publish an award date, not a start date; start_date carries the signature date when the source gives one, labelled

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 377 | 82.0% | 82.0% | -2.3 | n/a | no target |
| P01T | 211 | 0.5% | 0.5% | +0.1 | n/a | no target |
| P01_GOLD | 653 | 54.1% | 54.1% | +1.8 | 85% | ❌ 31 pts to go |
| P02 | 491 | 60.5% | 60.5% | +1.3 | 90% | ❌ 30 pts to go |
| P03 | 279 | 46.6% | 46.6% | +2.6 | 85% | ❌ 38 pts to go |
| P04 | 4868 | 37.4% | 37.4% | +8.3 | 90% | ❌ 53 pts to go |
| P05 | 429 | 33.1% | 33.1% | +0.2 | 75% | ❌ 42 pts to go |
| P06M | 28835 | 81.9% | 81.9% | -2.4 | n/a | no target |
| P06T | 55504 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06 | 259 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P07 | 791 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P08 | 29605 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P09 | 276 | 81.9% | 81.9% | +0.1 | 95% | ❌ 13 pts to go |
| P10 | 2080 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P11 | 1799 | 3.8% | 3.8% | +0.5 | n/a | no target |
| P12 | 11 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P13 | 193993 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `end_date`

> ceiling: an inferred end (award date + published duration) is labelled as such; sources without a duration leave end_date empty — the honest ceiling. P09 is BY DEFINITION the rows whose end date is not published (older SEAO contracts with no closing notice): its end_date / duration targets cannot be met without inventing a date

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 377 | 54.4% | 54.4% | -11.5 | n/a | no target |
| P01T | 211 | 0.5% | 0.5% | +0.1 | n/a | no target |
| P01_GOLD | 653 | 53.8% | 53.8% | +1.8 | 85% | ❌ 31 pts to go |
| P02 | 491 | 55.2% | 55.2% | +1.8 | 90% | ❌ 35 pts to go |
| P03 | 279 | 47.0% | 47.0% | +2.6 | 85% | ❌ 38 pts to go |
| P04 | 4868 | 33.1% | 33.1% | +8.5 | 90% | ❌ 57 pts to go |
| P05 | 429 | 42.0% | 42.0% | -0.7 | 75% | ❌ 33 pts to go |
| P06M | 28835 | 63.3% | 63.3% | -5.9 | n/a | no target |
| P06T | 55504 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06 | 259 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P07 | 791 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P08 | 29605 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P09 | 276 | 0.4% | 0.4% | +0.0 | 95% | ❌ 95 pts to go |
| P10 | 2080 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P11 | 1799 | 2.9% | 2.9% | +0.4 | n/a | no target |
| P12 | 11 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P13 | 193993 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `contract_title`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 377 | 96.8% | 96.8% | +1.6 | n/a | no target |
| P01T | 211 | 95.7% | 95.7% | -0.4 | n/a | no target |
| P01_GOLD | 653 | 86.1% | 86.2% | +0.6 | 100% | ❌ 14 pts to go |
| P02 | 491 | 78.0% | 78.0% | +0.4 | 100% | ❌ 22 pts to go |
| P03 | 279 | 92.1% | 92.1% | -0.4 | n/a | no target |
| P04 | 4868 | 53.2% | 53.2% | +2.6 | 95% | ❌ 42 pts to go |
| P05 | 429 | 77.6% | 77.6% | +0.3 | 95% | ❌ 17 pts to go |
| P06M | 28835 | 99.4% | 99.4% | +0.1 | n/a | no target |
| P06T | 55504 | 97.8% | 97.8% | +3.3 | n/a | no target |
| P06 | 259 | 21.2% | 21.2% | +0.8 | n/a | no target |
| P07 | 791 | 10.4% | 10.4% | +0.2 | n/a | no target |
| P08 | 29605 | 4.6% | 4.6% | +0.1 | n/a | no target |
| P09 | 276 | 98.2% | 98.2% | +0.0 | 100% | 🟡 2 pts to go |
| P10 | 2080 | 70.8% | 70.8% | +0.2 | n/a | no target |
| P11 | 1799 | 69.9% | 69.9% | +0.1 | n/a | no target |
| P12 | 11 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P13 | 193993 | 99.6% | 99.6% | +0.0 | n/a | no target |

### `contract_description`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 377 | 96.8% | 96.8% | +1.6 | n/a | no target |
| P01T | 211 | 95.7% | 95.7% | -0.4 | n/a | no target |
| P01_GOLD | 653 | 89.1% | 89.3% | +0.4 | 100% | ❌ 11 pts to go |
| P02 | 491 | 79.2% | 79.2% | +0.4 | 100% | ❌ 21 pts to go |
| P03 | 279 | 92.8% | 92.8% | -0.4 | n/a | no target |
| P04 | 4868 | 55.7% | 55.7% | +1.7 | 95% | ❌ 39 pts to go |
| P05 | 429 | 89.7% | 89.7% | +0.4 | 70% | ✅ met |
| P06M | 28835 | 99.4% | 99.4% | +0.1 | n/a | no target |
| P06T | 55504 | 97.8% | 97.8% | +3.3 | n/a | no target |
| P06 | 259 | 21.2% | 21.2% | +0.8 | n/a | no target |
| P07 | 791 | 10.4% | 10.4% | +0.2 | n/a | no target |
| P08 | 29605 | 4.6% | 4.6% | +0.1 | n/a | no target |
| P09 | 276 | 98.2% | 98.2% | +0.0 | 100% | 🟡 2 pts to go |
| P10 | 2080 | 70.8% | 70.8% | +0.2 | n/a | no target |
| P11 | 1799 | 69.9% | 69.9% | +0.0 | n/a | no target |
| P12 | 11 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P13 | 193993 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `number_of_bids`

> ceiling: published by some portals only (bids&tenders submission lists, Biddingo bidder lists); federal proactive disclosure does not publish bid counts

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 377 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P01T | 211 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P01_GOLD | 653 | 16.4% | 16.4% | -0.5 | 60% | ❌ 44 pts to go · rows from a source that publishes bids: 368 rows, 29.1% filled |
| P02 | 491 | 10.0% | 10.0% | -0.7 | n/a | no target · rows from a source that publishes bids: 295 rows, 16.6% filled |
| P03 | 279 | 13.3% | 13.3% | -0.6 | n/a | no target · rows from a source that publishes bids: 143 rows, 25.9% filled |
| P04 | 4868 | 1.3% | 1.3% | -0.4 | n/a | no target · rows from a source that publishes bids: 885 rows, 6.9% filled |
| P05 | 429 | 2.6% | 2.6% | +0.0 | n/a | no target · rows from a source that publishes bids: 60 rows, 18.3% filled |
| P06M | 28835 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06T | 55504 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06 | 259 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P07 | 791 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P08 | 29605 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P09 | 276 | 4.3% | 4.3% | -0.1 | n/a | no target · rows from a source that publishes bids: 263 rows, 4.6% filled |
| P10 | 2080 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P11 | 1799 | 0.4% | 0.4% | +0.0 | n/a | no target · rows from a source that publishes bids: 67 rows, 10.4% filled |
| P12 | 11 | 0.0% | 0.0% | +0.0 | n/a | no target · rows from a source that publishes bids: 11 rows, 0.0% filled |
| P13 | 193993 | 0.0% | 0.0% | +0.0 | n/a | no target |

## 6. history

### `average_contract_duration_days`

> ceiling: needs two dates (or a published term) on the buyer's records; P09 rows (end date unpublished by definition) and buyers whose sources publish award dates only have no honest duration

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 377 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P01T | 211 | 0.0% | 97.6% | +0.0 | n/a | no target |
| P01_GOLD | 653 | 51.1% | 82.7% | -2.3 | 90% | ❌ 39 pts to go |
| P02 | 491 | 50.9% | 87.8% | -2.5 | 90% | ❌ 39 pts to go |
| P03 | 279 | 43.7% | 81.0% | -2.2 | 90% | ❌ 46 pts to go |
| P04 | 4868 | 14.5% | 94.8% | -5.1 | 90% | ❌ 76 pts to go |
| P05 | 429 | 0.0% | 81.1% | +0.0 | 90% | ❌ 90 pts to go |
| P06M | 28835 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P06T | 55504 | 0.0% | 99.9% | +0.0 | n/a | no target |
| P06 | 259 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P07 | 791 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P08 | 29605 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P09 | 276 | 2.9% | 4.7% | +0.0 | 90% | ❌ 87 pts to go |
| P10 | 2080 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P11 | 1799 | 2.1% | 97.6% | +0.0 | n/a | no target |
| P12 | 11 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P13 | 193993 | 0.0% | 100.0% | +0.0 | n/a | no target |

### `commodity_distribution_top3`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 377 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P01T | 211 | 0.9% | 98.6% | +0.0 | n/a | no target |
| P01_GOLD | 653 | 25.1% | 56.7% | -1.4 | 90% | ❌ 65 pts to go |
| P02 | 491 | 49.7% | 86.6% | -2.7 | n/a | no target |
| P03 | 279 | 24.0% | 61.3% | -1.2 | n/a | no target |
| P04 | 4868 | 15.7% | 96.0% | -5.7 | n/a | no target |
| P05 | 429 | 0.5% | 81.6% | +0.0 | n/a | no target |
| P06M | 28835 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P06T | 55504 | 0.1% | 99.9% | +0.0 | n/a | no target |
| P06 | 259 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P07 | 791 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P08 | 29605 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P09 | 276 | 40.6% | 42.4% | +0.2 | n/a | no target |
| P10 | 2080 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P11 | 1799 | 2.2% | 97.7% | +0.0 | n/a | no target |
| P12 | 11 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P13 | 193993 | 0.0% | 100.0% | +0.0 | n/a | no target |

### `year_over_year_spend_trend`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 377 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P01T | 211 | 2.4% | 100.0% | +0.2 | n/a | no target |
| P01_GOLD | 653 | 50.1% | 81.6% | -1.9 | 95% | ❌ 45 pts to go |
| P02 | 491 | 55.4% | 92.3% | -2.7 | n/a | no target |
| P03 | 279 | 47.7% | 84.9% | -2.7 | n/a | no target |
| P04 | 4868 | 16.3% | 96.5% | -5.9 | n/a | no target |
| P05 | 429 | 5.1% | 86.2% | +0.1 | n/a | no target |
| P06M | 28835 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P06T | 55504 | 0.1% | 100.0% | +0.0 | n/a | no target |
| P06 | 259 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P07 | 791 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P08 | 29605 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P09 | 276 | 59.8% | 61.6% | -0.6 | n/a | no target |
| P10 | 2080 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P11 | 1799 | 2.3% | 97.8% | -0.1 | n/a | no target |
| P12 | 11 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P13 | 193993 | 0.0% | 100.0% | +0.0 | n/a | no target |

## 7. mail security

### `mta_sts`

> ceiling: DNS-only check; 'no record' counts as checked

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 377 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P01T | 211 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P01_GOLD | 653 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P02 | 491 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P03 | 279 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P04 | 4868 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P05 | 429 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P06M | 28835 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P06T | 55504 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P06 | 259 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P07 | 791 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P08 | 29605 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P09 | 276 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P10 | 2080 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P11 | 1799 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P12 | 11 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P13 | 193993 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |

### `tls_rpt`

> ceiling: DNS-only check; 'no record' counts as checked

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 377 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P01T | 211 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P01_GOLD | 653 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P02 | 491 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P03 | 279 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P04 | 4868 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P05 | 429 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P06M | 28835 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P06T | 55504 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P06 | 259 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P07 | 791 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P08 | 29605 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P09 | 276 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P10 | 2080 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P11 | 1799 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P12 | 11 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P13 | 193993 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |

### `bimi`

> ceiling: DNS-only check; 'no record' counts as checked

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 377 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P01T | 211 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P01_GOLD | 653 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P02 | 491 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P03 | 279 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P04 | 4868 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P05 | 429 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P06M | 28835 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P06T | 55504 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P06 | 259 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P07 | 791 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P08 | 29605 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P09 | 276 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P10 | 2080 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P11 | 1799 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P12 | 11 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P13 | 193993 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |

