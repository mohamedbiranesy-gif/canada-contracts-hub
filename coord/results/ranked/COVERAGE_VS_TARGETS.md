# Coverage vs the downstream team's targets — 2026-11-13

Benchmarks (field × package with a numeric target): **92 of 438 met** (21.0%); 63 within 10 points; 283 further away.
A cell counts as filled only when it carries a value: blank, `not_published`, `not_found_yet` and label-only cells ("no identifier published …", "no dataset record …", "0 in the contract dataset …") do not count; the DNS checks count when checked. `any` = share of non-blank cells incl. such labels. Δ = change since the previous build in `coord/results/coverage_history.csv`.
Rows per package: P01M 313, P01T 228, P01_GOLD 650, P02 475, P03 272, P04 4187, P05 423, P06M 24573, P06T 61958, P06 268, P07 814, P08 30392, P09 279, P10R 0, P10 2094, P11 1830, P12 10, P13 151168

## Invoice-grade readiness (the row as an invoice header: bill-to, submit-to, references, terms, tax, vendor identity, follow-up)

| package | rows | all 11 elements | ≥ 9 of 11 | median elements | most-missing element |
|---|---|---|---|---|---|
| P01M | 313 | 0.0% | 12.5% | 7 | vendor GST/HST number (294 rows) |
| P01T | 228 | 1.3% | 37.3% | 8 | payment terms (181 rows) |
| P01_GOLD | 650 | 23.4% | 69.4% | 9 | payment terms (241 rows) |
| P02 | 475 | 7.4% | 54.1% | 9 | PO rule (367 rows) |
| P03 | 272 | 14.7% | 54.8% | 9 | PO rule (139 rows) |
| P04 | 4187 | 1.1% | 14.7% | 7 | PO rule (3988 rows) |
| P05 | 423 | 0.9% | 17.0% | 7 | payment terms (352 rows) |
| P06M | 24573 | 0.0% | 2.7% | 7 | PO rule (24195 rows) |
| P06T | 61958 | 0.1% | 13.1% | 7 | PO rule (61578 rows) |
| P06 | 268 | 0.0% | 10.4% | 7 | reference to quote (PO / contract / vendor id) (250 rows) |
| P07 | 814 | 0.0% | 2.5% | 6 | PO rule (775 rows) |
| P08 | 30392 | 0.0% | 1.3% | 6 | PO rule (30133 rows) |
| P09 | 279 | 1.4% | 42.3% | 8 | payment terms (259 rows) |
| P10 | 2094 | 0.0% | 1.1% | 5 | reference to quote (PO / contract / vendor id) (2094 rows) |
| P11 | 1830 | 0.1% | 8.4% | 6 | PO rule (1764 rows) |
| P12 | 10 | 0.0% | 40.0% | 8 | PO rule (10 rows) |
| P13 | 151168 | 0.0% | 0.3% | 7 | reference to quote (PO / contract / vendor id) (151168 rows) |

## AP grade (how stringently the row's accounts-payable data meets what an invoice needs; A = invoicing mailbox referee-confirmed on the buyer's own domain with MX, legal name, address, PO rule and terms all published, no penalties)

| package | rows | A | B | C | D | E | median ap_score |
|---|---|---|---|---|---|---|---|
| P01M | 313 | 11 | 65 | 237 | 0 | 0 | 68 |
| P01T | 228 | 27 | 39 | 162 | 0 | 0 | 68 |
| P01_GOLD | 650 | 256 | 171 | 223 | 0 | 0 | 82 |
| P02 | 475 | 0 | 188 | 287 | 0 | 0 | 66 |
| P03 | 272 | 0 | 0 | 260 | 12 | 0 | 57 |
| P04 | 4187 | 0 | 0 | 3563 | 624 | 0 | 46 |
| P05 | 423 | 16 | 28 | 366 | 13 | 0 | 51 |
| P06M | 24573 | 0 | 18 | 24499 | 56 | 0 | 46 |
| P06T | 61958 | 0 | 29 | 41596 | 20333 | 0 | 38 |
| P06 | 268 | 17 | 40 | 211 | 0 | 0 | 67 |
| P07 | 814 | 0 | 21 | 774 | 19 | 0 | 55 |
| P08 | 30392 | 0 | 0 | 27426 | 2966 | 0 | 46 |
| P09 | 279 | 5 | 10 | 263 | 1 | 0 | 53 |
| P10 | 2094 | 1 | 10 | 1424 | 659 | 0 | 41 |
| P11 | 1830 | 7 | 12 | 39 | 0 | 1772 | 24 |
| P12 | 10 | 0 | 0 | 10 | 0 | 0 | 54 |
| P13 | 151168 | 13 | 62 | 151081 | 12 | 0 | 43 |

### AP payability (confirmed channel + bill-to legal name and address + the buyer's reference rule + tax treatment known)

| package | rows | payable today | % | most common gap |
|---|---|---|---|---|
| P01M | 313 | 233 | 74.4% | tax treatment (56) |
| P01T | 228 | 140 | 61.4% | bill-to legal name and address (73) |
| P01_GOLD | 650 | 489 | 75.2% | bill-to legal name and address (98) |
| P02 | 475 | 324 | 68.2% | the buyer's PO / reference rule (84) |
| P03 | 272 | 0 | 0.0% | a confirmed invoicing / AP or finance channel (272) |
| P04 | 4187 | 0 | 0.0% | a confirmed invoicing / AP or finance channel (4187) |
| P05 | 423 | 45 | 10.6% | a confirmed invoicing / AP or finance channel (335) |
| P06M | 24573 | 263 | 1.1% | a confirmed invoicing / AP or finance channel (24237) |
| P06T | 61958 | 336 | 0.5% | a confirmed invoicing / AP or finance channel (61144) |
| P06 | 268 | 53 | 19.8% | the buyer's PO / reference rule (114) |
| P07 | 814 | 48 | 5.9% | the buyer's PO / reference rule (327) |
| P08 | 30392 | 0 | 0.0% | a confirmed invoicing / AP or finance channel (30392) |
| P09 | 279 | 40 | 14.3% | a confirmed invoicing / AP or finance channel (228) |
| P10 | 2094 | 4 | 0.2% | a confirmed invoicing / AP or finance channel (2022) |
| P11 | 1830 | 18 | 1.0% | a confirmed invoicing / AP or finance channel (1772) |
| P12 | 10 | 2 | 20.0% | a confirmed invoicing / AP or finance channel (8) |
| P13 | 151168 | 42 | 0.0% | a confirmed invoicing / AP or finance channel (149060) |

### Pay on sight (an invoice generated from the row would clear AP: confirmed invoicing / AP or finance channel, bill-to legal name + address, vendor legal name + GST/HST number + remit-to address, tax treatment and currency known — published or labelled-derived; the buyer's reference rule is reported separately)

| package | rows | pay on sight | % | + reference rule not published | routed (general inbox only) | most common gap |
|---|---|---|---|---|---|---|
| P01M | 313 | 8 | 2.6% | 7 | 0 | the vendor's GST/HST number (BN9) (294) |
| P01T | 228 | 101 | 44.3% | 3 | 0 | the vendor's GST/HST number (BN9) (73) |
| P01_GOLD | 650 | 409 | 62.9% | 11 | 0 | the vendor's GST/HST number (BN9) (164) |
| P02 | 475 | 214 | 45.1% | 21 | 0 | the vendor's GST/HST number (BN9) (212) |
| P03 | 272 | 17 | 6.2% | 0 | 134 | an invoicing / AP or finance mailbox (only a purchasing / general inbo (103) |
| P04 | 4187 | 43 | 1.0% | 7 | 897 | an invoicing / AP or finance mailbox (only a purchasing / general inbo (3184) |
| P05 | 423 | 20 | 4.7% | 8 | 125 | an invoicing / AP or finance mailbox (only a purchasing / general inbo (202) |
| P06M | 24573 | 8 | 0.0% | 12 | 595 | an invoicing / AP or finance mailbox (only a purchasing / general inbo (23544) |
| P06T | 61958 | 389 | 0.6% | 14 | 19317 | an invoicing / AP or finance mailbox (only a purchasing / general inbo (41742) |
| P06 | 268 | 24 | 9.0% | 53 | 0 | the vendor's GST/HST number (BN9) (127) |
| P07 | 814 | 13 | 1.6% | 140 | 36 | the vendor's GST/HST number (BN9) (407) |
| P08 | 30392 | 4 | 0.0% | 13 | 7308 | an invoicing / AP or finance mailbox (only a purchasing / general inbo (23023) |
| P09 | 279 | 37 | 13.3% | 0 | 108 | an invoicing / AP or finance mailbox (only a purchasing / general inbo (108) |
| P10 | 2094 | 5 | 0.2% | 13 | 302 | an invoicing / AP or finance mailbox (only a purchasing / general inbo (1698) |
| P11 | 1830 | 7 | 0.4% | 2 | 0 | a confirmed invoicing / AP or finance channel (1756) |
| P12 | 10 | 1 | 10.0% | 0 | 5 | an invoicing / AP or finance mailbox (only a purchasing / general inbo (3) |
| P13 | 151168 | 21 | 0.0% | 1034 | 60449 | an invoicing / AP or finance mailbox (only a purchasing / general inbo (88430) |
| **all** | 279934 | 1321 | 0.5% | 1338 | 89276 | |

### What still blocks grade A (rows per missing element; a row counts under every element it lacks)

| package | rows not A | referee confirmation of the mailbox | an invoicing / AP mailbox (not finance / procurement / general) | a mailbox on the buyer's own domain | MX record for the mailbox domain | published bill-to legal name | invoice / billing address | published PO rule | published payment terms | clear the penalty |
|---|---|---|---|---|---|---|---|---|---|---|
| P01M | 302 | 0 | 0 | 0 | 214 | 9 | 0 | 253 | 269 | 1 |
| P01T | 201 | 0 | 0 | 0 | 122 | 65 | 31 | 166 | 183 | 4 |
| P01_GOLD | 394 | 0 | 0 | 0 | 33 | 79 | 31 | 217 | 256 | 3 |
| P02 | 475 | 0 | 475 | 0 | 49 | 53 | 14 | 367 | 294 | 2 |
| P03 | 272 | 0 | 272 | 0 | 25 | 45 | 25 | 139 | 148 | 2 |
| P04 | 4187 | 0 | 4187 | 0 | 2141 | 1260 | 953 | 3988 | 3736 | 31 |
| P05 | 407 | 0 | 355 | 0 | 82 | 95 | 40 | 339 | 354 | 7 |
| P06M | 24573 | 0 | 24573 | 0 | 18673 | 1352 | 137 | 24195 | 23950 | 20 |
| P06T | 61958 | 0 | 61958 | 0 | 55783 | 38799 | 26219 | 61578 | 61050 | 412 |
| P06 | 251 | 0 | 0 | 0 | 137 | 70 | 42 | 191 | 219 | 4 |
| P07 | 814 | 0 | 814 | 0 | 554 | 318 | 113 | 775 | 774 | 5 |
| P08 | 30392 | 0 | 30392 | 0 | 24028 | 13143 | 4636 | 30133 | 29778 | 189 |
| P09 | 274 | 0 | 255 | 0 | 12 | 69 | 1 | 249 | 261 | 7 |
| P10 | 2093 | 0 | 2063 | 0 | 1086 | 1120 | 956 | 2030 | 1993 | 16 |
| P11 | 1823 | 1772 | 1725 | 0 | 925 | 1226 | 554 | 1764 | 1757 | 21 |
| P12 | 10 | 0 | 9 | 0 | 0 | 2 | 0 | 10 | 10 | 1 |
| P13 | 151155 | 0 | 150766 | 0 | 121370 | 79280 | 18 | 150833 | 150060 | 71 |

## Where the work is (largest gaps in rows still needed)

| field | package | now | target | rows needed |
|---|---|---|---|---|
| buyer_phone | P13 | 71.9% | 95% | 34917 |
| buyer_ap_cycle_published | P13 | 0.0% | 20% | 30181 |
| ap_system_hint | P13 | 0.4% | 20% | 29643 |
| buyer_bn_as_published | P13 | 13.9% | 30% | 24279 |
| buyer_esignature_preference | P13 | 0.1% | 15% | 22530 |
| buyer_tax_exempt_status | P13 | 0.1% | 15% | 22485 |
| buyer_payment_method_preference | P13 | 0.7% | 15% | 21649 |
| buyer_legal_name_as_published | P13 | 47.6% | 60% | 18813 |
| buyer_ap_cycle_published | P06T | 0.0% | 20% | 12375 |
| ap_system_hint | P06T | 0.6% | 20% | 12042 |
| buyer_logo_url | P13 | 87.2% | 95% | 11865 |
| vendor_registered_address | P08 | 31.2% | 70% | 11788 |
| buyer_esignature_preference | P06T | 0.2% | 15% | 9187 |
| buyer_tax_exempt_status | P06T | 0.2% | 15% | 9176 |
| buyer_payment_method_preference | P06T | 0.7% | 15% | 8877 |
| buyer_phone | P08 | 71.1% | 95% | 7259 |
| buyer_ap_cycle_published | P08 | 0.0% | 20% | 6066 |
| ap_system_hint | P08 | 0.8% | 20% | 5850 |
| vendor_bn9 | P08 | 30.8% | 50% | 5833 |
| vendor_emails | P08 | 56.0% | 75% | 5764 |
| buyer_legal_name_as_published | P08 | 56.8% | 75% | 5545 |
| vendor_phone | P08 | 67.0% | 85% | 5460 |
| buyer_ap_cycle_published | P06M | 0.0% | 20% | 4903 |
| vendor_trading_name | P08 | 34.5% | 50% | 4720 |
| ap_system_hint | P06M | 1.0% | 20% | 4670 |
| buyer_esignature_preference | P08 | 0.3% | 15% | 4458 |
| buyer_tax_exempt_status | P08 | 0.3% | 15% | 4455 |
| buyer_payment_method_preference | P08 | 0.6% | 15% | 4377 |
| buyer_bn_as_published | P08 | 22.5% | 35% | 3806 |
| invoice_reference_hint | P08 | 12.5% | 25% | 3792 |
| buyer_esignature_preference | P06M | 0.4% | 15% | 3588 |
| buyer_tax_exempt_status | P06M | 0.6% | 15% | 3536 |
| buyer_payment_method_preference | P06M | 0.8% | 15% | 3489 |
| buyer_address | P08 | 84.7% | 95% | 3124 |
| average_contract_duration_days | P04 | 16.8% | 90% | 3066 |
| currency | P04 | 24.1% | 95% | 2968 |
| ap_phone | P04 | 18.3% | 85% | 2793 |
| commodity_codes | P04 | 18.9% | 85% | 2767 |
| award_or_notice_id | P04 | 21.2% | 85% | 2671 |
| contract_value | P04 | 23.7% | 85% | 2566 |

## 1. identifiers

### `invoice_reference_hint`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 313 | 94.6% | 94.6% | +1.4 | 50% | ✅ met |
| P01T | 228 | 95.6% | 95.6% | +0.0 | 50% | ✅ met |
| P01_GOLD | 650 | 92.3% | 94.6% | +0.1 | 95% | 🟡 3 pts to go |
| P02 | 475 | 76.0% | 77.5% | +1.0 | 95% | ❌ 19 pts to go |
| P03 | 272 | 82.0% | 85.3% | +0.4 | 95% | ❌ 13 pts to go |
| P04 | 4187 | 42.3% | 43.8% | +10.5 | 90% | ❌ 48 pts to go |
| P05 | 423 | 39.5% | 42.6% | -0.1 | 70% | ❌ 30 pts to go |
| P06M | 24573 | 93.6% | 93.6% | +0.4 | n/a | no target |
| P06T | 61958 | 99.3% | 99.3% | +0.0 | n/a | no target |
| P06 | 268 | 35.1% | 35.1% | -0.3 | 30% | ✅ met |
| P07 | 814 | 13.8% | 13.8% | -0.4 | 30% | ❌ 16 pts to go |
| P08 | 30392 | 12.5% | 12.5% | +0.3 | 25% | ❌ 12 pts to go |
| P09 | 279 | 98.9% | 99.6% | +0.0 | 100% | 🟡 1 pts to go |
| P10 | 2094 | 3.1% | 3.1% | -0.2 | 25% | ❌ 22 pts to go |
| P11 | 1830 | 55.2% | 55.9% | +0.9 | 60% | 🟡 5 pts to go |
| P12 | 10 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P13 | 151168 | 99.6% | 99.6% | +0.0 | 0% by design | — leave (by design) |

### `po_number_as_published`

> ceiling: a purchase-order number exists only where the buyer publishes PO-level data (Montréal, Laval, Toronto open data so far) or the record itself carries one; most sources publish awards, not POs — the target cannot be reached from public data for most buyers

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 313 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P01T | 228 | 0.0% | 0.0% | +0.0 | 10% | 🟡 10 pts to go |
| P01_GOLD | 650 | 5.7% | 5.7% | +0.0 | 50% | ❌ 44 pts to go |
| P02 | 475 | 5.7% | 5.7% | -0.5 | 50% | ❌ 44 pts to go |
| P03 | 272 | 1.5% | 1.5% | -0.4 | 40% | ❌ 38 pts to go |
| P04 | 4187 | 0.5% | 0.5% | -0.1 | 30% | ❌ 30 pts to go |
| P05 | 423 | 0.2% | 0.2% | +0.0 | 20% | ❌ 20 pts to go |
| P06M | 24573 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06T | 61958 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06 | 268 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P07 | 814 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P08 | 30392 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P09 | 279 | 0.7% | 0.7% | +0.0 | 50% | ❌ 49 pts to go |
| P10 | 2094 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P11 | 1830 | 0.2% | 0.2% | +0.0 | n/a | no target |
| P12 | 10 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P13 | 151168 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `contract_or_agreement_number`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 313 | 91.7% | 91.7% | +2.1 | n/a | no target |
| P01T | 228 | 79.8% | 79.8% | -0.1 | 50% | ✅ met |
| P01_GOLD | 650 | 68.2% | 68.2% | +0.9 | 85% | ❌ 17 pts to go |
| P02 | 475 | 67.6% | 67.6% | +1.4 | 90% | ❌ 22 pts to go |
| P03 | 272 | 62.1% | 62.1% | +1.6 | 85% | ❌ 23 pts to go |
| P04 | 4187 | 40.0% | 40.0% | +10.9 | 85% | ❌ 45 pts to go |
| P05 | 423 | 30.0% | 30.0% | +0.1 | 60% | ❌ 30 pts to go |
| P06M | 24573 | 93.3% | 93.3% | +0.3 | n/a | no target |
| P06T | 61958 | 99.3% | 99.3% | +0.1 | n/a | no target |
| P06 | 268 | 6.7% | 6.7% | +0.3 | n/a | no target |
| P07 | 814 | 9.0% | 9.0% | -0.1 | n/a | no target |
| P08 | 30392 | 11.7% | 11.7% | +0.4 | n/a | no target |
| P09 | 279 | 95.7% | 95.7% | +0.1 | 100% | 🟡 4 pts to go |
| P10 | 2094 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P11 | 1830 | 52.5% | 52.5% | +1.0 | 60% | 🟡 8 pts to go |
| P12 | 10 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P13 | 151168 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `solicitation_or_tender_number`

> ceiling: SEAO's 'numero' is the organisation's own reference for the notice (SEAO data dictionary) and is reported here; sources that publish awards under a tender number only (bids&tenders, SaskTenders, BC) also carry it as the contract reference, labelled

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 313 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P01T | 228 | 0.0% | 0.0% | +0.0 | 30% | ❌ 30 pts to go |
| P01_GOLD | 650 | 49.8% | 49.8% | -1.9 | 80% | ❌ 30 pts to go |
| P02 | 475 | 56.8% | 56.8% | -1.3 | 60% | 🟡 3 pts to go |
| P03 | 272 | 48.9% | 48.9% | -1.5 | 80% | ❌ 31 pts to go |
| P04 | 4187 | 20.4% | 20.4% | -3.6 | 50% | ❌ 30 pts to go |
| P05 | 423 | 12.5% | 12.5% | -0.1 | 40% | ❌ 28 pts to go |
| P06M | 24573 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06T | 61958 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06 | 268 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P07 | 814 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P08 | 30392 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P09 | 279 | 81.4% | 81.4% | +0.3 | 50% | ✅ met |
| P10 | 2094 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P11 | 1830 | 3.3% | 3.3% | +0.0 | 40% | ❌ 37 pts to go |
| P12 | 10 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P13 | 151168 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `award_or_notice_id`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 313 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P01T | 228 | 0.4% | 0.4% | +0.0 | n/a | no target |
| P01_GOLD | 650 | 59.1% | 59.1% | -1.8 | 85% | ❌ 26 pts to go |
| P02 | 475 | 56.8% | 56.8% | -1.3 | 90% | ❌ 33 pts to go |
| P03 | 272 | 57.4% | 57.4% | -2.0 | 85% | ❌ 28 pts to go |
| P04 | 4187 | 21.2% | 21.2% | -3.7 | 85% | ❌ 64 pts to go |
| P05 | 423 | 20.3% | 20.3% | -0.1 | 50% | ❌ 30 pts to go |
| P06M | 24573 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06T | 61958 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06 | 268 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P07 | 814 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P08 | 30392 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P09 | 279 | 97.1% | 97.1% | +0.0 | 100% | 🟡 3 pts to go |
| P10 | 2094 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P11 | 1830 | 3.7% | 3.7% | +0.1 | 60% | ❌ 56 pts to go |
| P12 | 10 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P13 | 151168 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `buyer_vendor_id`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 313 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P01T | 228 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P01_GOLD | 650 | 12.6% | 12.6% | +0.0 | 60% | ❌ 47 pts to go |
| P02 | 475 | 6.7% | 6.7% | -0.6 | 50% | ❌ 43 pts to go |
| P03 | 272 | 8.1% | 8.1% | -0.5 | 50% | ❌ 42 pts to go |
| P04 | 4187 | 1.6% | 1.6% | -0.3 | 40% | ❌ 38 pts to go |
| P05 | 423 | 0.7% | 0.7% | +0.0 | 20% | ❌ 19 pts to go |
| P06M | 24573 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06T | 61958 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06 | 268 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P07 | 814 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P08 | 30392 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P09 | 279 | 3.2% | 3.2% | -0.4 | 50% | ❌ 47 pts to go |
| P10 | 2094 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P11 | 1830 | 0.4% | 0.4% | +0.0 | n/a | no target |
| P12 | 10 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P13 | 151168 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `commodity_codes`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 313 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P01T | 228 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P01_GOLD | 650 | 34.8% | 34.8% | -1.1 | 80% | ❌ 45 pts to go |
| P02 | 475 | 51.4% | 51.4% | -1.6 | 90% | ❌ 39 pts to go |
| P03 | 272 | 32.7% | 32.7% | -1.1 | 80% | ❌ 47 pts to go |
| P04 | 4187 | 18.9% | 18.9% | -3.3 | 85% | ❌ 66 pts to go |
| P05 | 423 | 6.4% | 6.4% | +0.0 | 50% | ❌ 44 pts to go |
| P06M | 24573 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06T | 61958 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06 | 268 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P07 | 814 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P08 | 30392 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P09 | 279 | 73.8% | 73.8% | +0.7 | 95% | ❌ 21 pts to go |
| P10 | 2094 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P11 | 1830 | 2.7% | 2.7% | +0.1 | 50% | ❌ 47 pts to go |
| P12 | 10 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P13 | 151168 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `buyer_org_codes`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 313 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P01T | 228 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P01_GOLD | 650 | 8.0% | 8.0% | -0.1 | 50% | ❌ 42 pts to go |
| P02 | 475 | 5.7% | 5.7% | -0.5 | 50% | ❌ 44 pts to go |
| P03 | 272 | 2.2% | 2.2% | -0.4 | 30% | ❌ 28 pts to go |
| P04 | 4187 | 0.5% | 0.5% | -0.1 | 30% | ❌ 30 pts to go |
| P05 | 423 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06M | 24573 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06T | 61958 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06 | 268 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P07 | 814 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P08 | 30392 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P09 | 279 | 0.4% | 0.4% | +0.0 | n/a | no target |
| P10 | 2094 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P11 | 1830 | 0.2% | 0.2% | +0.0 | n/a | no target |
| P12 | 10 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P13 | 151168 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `records_with_this_vendor`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 313 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P01T | 228 | 100.0% | 100.0% | +0.0 | 60% | ✅ met |
| P01_GOLD | 650 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P02 | 475 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P03 | 272 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P04 | 4187 | 100.0% | 100.0% | +0.0 | 95% | ✅ met |
| P05 | 423 | 100.0% | 100.0% | +0.0 | 70% | ✅ met |
| P06M | 24573 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P06T | 61958 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P06 | 268 | 100.0% | 100.0% | +0.0 | 50% | ✅ met |
| P07 | 814 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P08 | 30392 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P09 | 279 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P10 | 2094 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P11 | 1830 | 100.0% | 100.0% | +0.0 | 70% | ✅ met |
| P12 | 10 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P13 | 151168 | 0.0% | 0.0% | +0.0 | n/a | no target |

## 2. vendor

### `vendor_bn9`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 313 | 6.1% | 6.1% | -0.3 | 70% | ❌ 64 pts to go |
| P01T | 228 | 60.5% | 60.5% | +0.2 | 60% | ✅ met |
| P01_GOLD | 650 | 72.5% | 72.5% | -2.3 | 90% | ❌ 18 pts to go |
| P02 | 475 | 52.8% | 52.8% | -1.5 | 85% | ❌ 32 pts to go |
| P03 | 272 | 64.7% | 64.7% | -2.2 | 90% | ❌ 25 pts to go |
| P04 | 4187 | 32.5% | 32.5% | -5.7 | 75% | ❌ 42 pts to go |
| P05 | 423 | 54.1% | 54.1% | -0.6 | 50% | ✅ met |
| P06M | 24573 | 3.0% | 3.0% | +0.1 | n/a | no target |
| P06T | 61958 | 65.7% | 65.7% | +1.2 | n/a | no target |
| P06 | 268 | 42.2% | 42.2% | +0.1 | 40% | ✅ met |
| P07 | 814 | 31.6% | 31.6% | -0.5 | 50% | ❌ 18 pts to go |
| P08 | 30392 | 30.8% | 30.8% | +0.2 | 50% | ❌ 19 pts to go |
| P09 | 279 | 56.6% | 56.6% | -0.1 | 80% | ❌ 23 pts to go |
| P10 | 2094 | 38.8% | 38.8% | +0.0 | 40% | 🟡 1 pts to go |
| P11 | 1830 | 54.7% | 54.7% | +0.1 | 60% | 🟡 5 pts to go |
| P12 | 10 | 60.0% | 60.0% | +14.5 | 85% | ❌ 25 pts to go |
| P13 | 151168 | 44.8% | 44.8% | +0.0 | 0% by design | — leave (by design) |

### `vendor_registered_address`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 313 | 45.0% | 45.0% | -1.6 | n/a | no target |
| P01T | 228 | 61.0% | 61.0% | +1.2 | n/a | no target |
| P01_GOLD | 650 | 73.7% | 73.7% | +0.8 | 95% | ❌ 21 pts to go |
| P02 | 475 | 75.8% | 75.8% | +1.2 | 95% | ❌ 19 pts to go |
| P03 | 272 | 70.2% | 70.2% | +0.7 | 95% | ❌ 25 pts to go |
| P04 | 4187 | 59.3% | 59.3% | +6.2 | 95% | ❌ 36 pts to go |
| P05 | 423 | 58.6% | 58.6% | +0.5 | 70% | ❌ 11 pts to go |
| P06M | 24573 | 40.8% | 40.8% | -0.5 | n/a | no target |
| P06T | 61958 | 71.6% | 71.6% | +4.1 | n/a | no target |
| P06 | 268 | 38.8% | 38.8% | +0.6 | 80% | ❌ 41 pts to go |
| P07 | 814 | 30.8% | 30.8% | -0.2 | 70% | ❌ 39 pts to go |
| P08 | 30392 | 31.2% | 31.2% | +1.5 | 70% | ❌ 39 pts to go |
| P09 | 279 | 86.7% | 86.7% | +0.5 | 100% | ❌ 13 pts to go |
| P10 | 2094 | 39.3% | 39.3% | +0.1 | 70% | ❌ 31 pts to go |
| P11 | 1830 | 59.7% | 59.7% | +1.1 | 75% | ❌ 15 pts to go |
| P12 | 10 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P13 | 151168 | 40.2% | 40.2% | +0.0 | n/a | no target |

### `vendor_trading_name`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 313 | 21.7% | 21.7% | -0.4 | n/a | no target |
| P01T | 228 | 64.9% | 64.9% | -0.6 | n/a | no target |
| P01_GOLD | 650 | 50.2% | 50.2% | +1.4 | 60% | 🟡 10 pts to go |
| P02 | 475 | 57.5% | 57.5% | +1.7 | 60% | 🟡 2 pts to go |
| P03 | 272 | 53.7% | 53.7% | +1.4 | 60% | 🟡 6 pts to go |
| P04 | 4187 | 50.3% | 50.3% | +7.7 | 55% | 🟡 5 pts to go |
| P05 | 423 | 23.4% | 23.4% | +0.7 | 50% | ❌ 27 pts to go |
| P06M | 24573 | 10.6% | 10.6% | +1.1 | n/a | no target |
| P06T | 61958 | 65.8% | 65.8% | -2.1 | n/a | no target |
| P06 | 268 | 50.4% | 50.4% | +1.8 | n/a | no target |
| P07 | 814 | 39.9% | 39.9% | +0.3 | 55% | ❌ 15 pts to go |
| P08 | 30392 | 34.5% | 34.5% | +1.5 | 50% | ❌ 16 pts to go |
| P09 | 279 | 72.8% | 72.8% | +0.8 | 70% | ✅ met |
| P10 | 2094 | 47.8% | 47.8% | -0.3 | 55% | 🟡 7 pts to go |
| P11 | 1830 | 59.4% | 59.4% | +0.2 | 50% | ✅ met |
| P12 | 10 | 90.0% | 90.0% | -0.9 | n/a | no target |
| P13 | 151168 | 3.2% | 3.2% | +0.0 | n/a | no target |

### `vendor_phone`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 313 | 29.1% | 29.1% | -4.2 | n/a | no target |
| P01T | 228 | 79.8% | 79.8% | +0.3 | n/a | no target |
| P01_GOLD | 650 | 48.5% | 48.5% | -1.9 | 70% | ❌ 22 pts to go |
| P02 | 475 | 54.3% | 54.3% | -2.5 | 70% | ❌ 16 pts to go |
| P03 | 272 | 48.5% | 48.5% | -1.9 | 70% | ❌ 22 pts to go |
| P04 | 4187 | 46.3% | 46.3% | -8.6 | 65% | ❌ 19 pts to go |
| P05 | 423 | 28.4% | 28.4% | -0.7 | 60% | ❌ 32 pts to go |
| P06M | 24573 | 26.3% | 26.3% | -1.1 | n/a | no target |
| P06T | 61958 | 83.2% | 83.2% | +0.5 | n/a | no target |
| P06 | 268 | 72.0% | 72.0% | +2.7 | 40% | ✅ met |
| P07 | 814 | 66.7% | 66.7% | +1.7 | 85% | ❌ 18 pts to go |
| P08 | 30392 | 67.0% | 67.0% | +3.0 | 85% | ❌ 18 pts to go |
| P09 | 279 | 56.6% | 56.6% | +0.2 | 85% | ❌ 28 pts to go |
| P10 | 2094 | 65.6% | 65.6% | -0.5 | 85% | ❌ 19 pts to go |
| P11 | 1830 | 68.4% | 68.4% | +0.3 | 75% | 🟡 7 pts to go |
| P12 | 10 | 40.0% | 40.0% | +3.6 | n/a | no target |
| P13 | 151168 | 91.8% | 91.8% | +0.0 | 60% | ✅ met |

### `vendor_website`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 313 | 32.6% | 32.6% | -5.2 | n/a | no target |
| P01T | 228 | 98.2% | 98.2% | -0.1 | n/a | no target |
| P01_GOLD | 650 | 76.0% | 76.0% | -2.6 | 90% | ❌ 14 pts to go |
| P02 | 475 | 79.4% | 79.4% | -2.4 | 90% | ❌ 11 pts to go |
| P03 | 272 | 83.1% | 83.1% | -2.2 | 90% | 🟡 7 pts to go |
| P04 | 4187 | 69.9% | 69.9% | -12.9 | 85% | ❌ 15 pts to go |
| P05 | 423 | 44.4% | 44.4% | -0.1 | 70% | ❌ 26 pts to go |
| P06M | 24573 | 31.4% | 31.4% | -1.6 | n/a | no target |
| P06T | 61958 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P06 | 268 | 99.3% | 99.3% | +0.0 | 50% | ✅ met |
| P07 | 814 | 99.9% | 99.9% | +0.0 | 100% | 🟡 0 pts to go |
| P08 | 30392 | 99.9% | 99.9% | +0.0 | 100% | 🟡 0 pts to go |
| P09 | 279 | 78.1% | 78.1% | +0.3 | 100% | ❌ 22 pts to go |
| P10 | 2094 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P11 | 1830 | 97.7% | 97.7% | -0.3 | 100% | 🟡 2 pts to go |
| P12 | 10 | 60.0% | 60.0% | +5.5 | n/a | no target |
| P13 | 151168 | 100.0% | 100.0% | +0.0 | n/a | no target |

### `vendor_emails`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 313 | 15.3% | 15.3% | -0.8 | n/a | no target |
| P01T | 228 | 59.2% | 59.2% | -0.6 | n/a | no target |
| P01_GOLD | 650 | 41.7% | 41.7% | -1.7 | 70% | ❌ 28 pts to go |
| P02 | 475 | 45.9% | 45.9% | -1.3 | 75% | ❌ 29 pts to go |
| P03 | 272 | 44.1% | 44.1% | -0.6 | 75% | ❌ 31 pts to go |
| P04 | 4187 | 32.8% | 32.8% | -5.9 | 70% | ❌ 37 pts to go |
| P05 | 423 | 21.3% | 21.3% | +0.0 | 55% | ❌ 34 pts to go |
| P06M | 24573 | 6.4% | 6.4% | +0.5 | n/a | no target |
| P06T | 61958 | 46.2% | 46.2% | -1.2 | n/a | no target |
| P06 | 268 | 51.9% | 51.9% | +0.8 | n/a | no target |
| P07 | 814 | 53.7% | 53.7% | +1.0 | 70% | ❌ 16 pts to go |
| P08 | 30392 | 56.0% | 56.0% | +1.2 | 75% | ❌ 19 pts to go |
| P09 | 279 | 47.3% | 47.3% | +0.4 | 85% | ❌ 38 pts to go |
| P10 | 2094 | 44.5% | 44.5% | +0.1 | 80% | ❌ 36 pts to go |
| P11 | 1830 | 53.2% | 53.2% | -0.1 | 70% | ❌ 17 pts to go |
| P12 | 10 | 30.0% | 30.0% | +2.7 | n/a | no target |
| P13 | 151168 | 5.5% | 5.5% | +0.0 | n/a | no target |

### `vendor_logo_url`

> ceiling: needs the vendor's website first; sites that block automated readers (robots.txt / 403) are never read

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 313 | 32.6% | 32.6% | -5.2 | n/a | no target |
| P01T | 228 | 96.5% | 96.5% | +0.0 | n/a | no target |
| P01_GOLD | 650 | 70.5% | 70.5% | -2.4 | 90% | ❌ 20 pts to go |
| P02 | 475 | 74.3% | 74.3% | -2.4 | 90% | ❌ 16 pts to go |
| P03 | 272 | 79.8% | 79.8% | -2.2 | 90% | ❌ 10 pts to go |
| P04 | 4187 | 65.6% | 65.6% | -12.1 | 85% | ❌ 19 pts to go |
| P05 | 423 | 43.0% | 43.0% | +0.1 | 75% | ❌ 32 pts to go |
| P06M | 24573 | 31.3% | 31.3% | -1.6 | n/a | no target |
| P06T | 61958 | 98.4% | 98.4% | +0.1 | n/a | no target |
| P06 | 268 | 92.5% | 92.5% | +2.5 | n/a | no target |
| P07 | 814 | 94.1% | 94.1% | +2.4 | 100% | 🟡 6 pts to go |
| P08 | 30392 | 92.2% | 92.2% | +4.9 | 100% | 🟡 8 pts to go |
| P09 | 279 | 66.7% | 66.7% | +0.2 | n/a | no target |
| P10 | 2094 | 90.2% | 90.2% | -0.1 | 100% | 🟡 10 pts to go |
| P11 | 1830 | 90.7% | 90.7% | +0.5 | n/a | no target |
| P12 | 10 | 60.0% | 60.0% | +5.5 | n/a | no target |
| P13 | 151168 | 69.8% | 69.8% | +0.0 | n/a | no target |

### `vendor_neq`

> ceiling: only Québec-registered vendors have an NEQ; the share of QC vendors is reported next to the rate

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 313 | 35.1% | 35.1% | -1.8 | n/a | no target · QC vendors: 53 rows, 100.0% filled |
| P01T | 228 | 20.2% | 20.2% | +0.5 | n/a | no target · QC vendors: 34 rows, 88.2% filled |
| P01_GOLD | 650 | 44.6% | 44.6% | +1.1 | 95% | ❌ 50 pts to go · QC vendors: 48 rows, 97.9% filled |
| P02 | 475 | 58.1% | 58.1% | +2.1 | 95% | ❌ 37 pts to go · QC vendors: 110 rows, 100.0% filled |
| P03 | 272 | 43.8% | 43.8% | +0.9 | 95% | ❌ 51 pts to go · QC vendors: 18 rows, 100.0% filled |
| P04 | 4187 | 41.7% | 41.7% | +9.3 | 95% | ❌ 53 pts to go · QC vendors: 595 rows, 98.0% filled |
| P05 | 423 | 14.4% | 14.4% | +0.4 | n/a | no target · QC vendors: 37 rows, 100.0% filled |
| P06M | 24573 | 36.6% | 36.6% | -0.9 | n/a | no target · QC vendors: 6819 rows, 99.9% filled |
| P06T | 61958 | 32.5% | 32.5% | +1.9 | n/a | no target · QC vendors: 20436 rows, 96.0% filled |
| P06 | 268 | 7.5% | 7.5% | +0.4 | n/a | no target · QC vendors: 12 rows, 66.7% filled |
| P07 | 814 | 6.9% | 6.9% | +0.0 | n/a | no target · QC vendors: 46 rows, 78.3% filled |
| P08 | 30392 | 7.0% | 7.0% | +0.0 | n/a | no target · QC vendors: 1820 rows, 92.8% filled |
| P09 | 279 | 74.2% | 74.2% | +0.7 | 95% | ❌ 21 pts to go · QC vendors: 102 rows, 100.0% filled |
| P10 | 2094 | 15.7% | 15.7% | +0.0 | n/a | no target · QC vendors: 195 rows, 95.4% filled |
| P11 | 1830 | 19.7% | 19.7% | +0.1 | n/a | no target · QC vendors: 306 rows, 94.1% filled |
| P12 | 10 | 80.0% | 80.0% | -1.8 | n/a | no target · QC vendors: 2 rows, 100.0% filled |
| P13 | 151168 | 22.2% | 22.2% | +0.0 | n/a | no target · QC vendors: 33490 rows, 100.0% filled |

### `vendor_years_in_business`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 313 | 44.7% | 44.7% | -1.5 | n/a | no target · vendors with a registry record: 140 rows, 100.0% filled |
| P01T | 228 | 61.0% | 61.0% | +1.2 | n/a | no target · vendors with a registry record: 139 rows, 100.0% filled |
| P01_GOLD | 650 | 81.5% | 81.5% | +0.6 | 100% | ❌ 18 pts to go · vendors with a registry record: 530 rows, 100.0% filled |
| P02 | 475 | 79.4% | 79.4% | +1.0 | 100% | ❌ 21 pts to go · vendors with a registry record: 377 rows, 100.0% filled |
| P03 | 272 | 78.7% | 78.7% | +0.5 | 100% | ❌ 21 pts to go · vendors with a registry record: 214 rows, 100.0% filled |
| P04 | 4187 | 60.2% | 60.2% | +6.2 | 100% | ❌ 40 pts to go · vendors with a registry record: 2519 rows, 100.0% filled |
| P05 | 423 | 62.9% | 62.9% | +0.1 | n/a | no target · vendors with a registry record: 266 rows, 100.0% filled |
| P06M | 24573 | 40.7% | 40.7% | -0.5 | n/a | no target · vendors with a registry record: 10001 rows, 100.0% filled |
| P06T | 61958 | 71.7% | 71.7% | +4.1 | n/a | no target · vendors with a registry record: 44413 rows, 100.0% filled |
| P06 | 268 | 39.6% | 39.6% | +0.3 | n/a | no target · vendors with a registry record: 106 rows, 100.0% filled |
| P07 | 814 | 31.6% | 31.6% | -0.2 | n/a | no target · vendors with a registry record: 257 rows, 100.0% filled |
| P08 | 30392 | 31.3% | 31.3% | +1.3 | n/a | no target · vendors with a registry record: 9512 rows, 100.0% filled |
| P09 | 279 | 90.0% | 90.0% | +0.5 | n/a | no target · vendors with a registry record: 251 rows, 100.0% filled |
| P10 | 2094 | 40.4% | 40.4% | +0.3 | n/a | no target · vendors with a registry record: 846 rows, 100.0% filled |
| P11 | 1830 | 60.5% | 60.5% | +1.2 | n/a | no target · vendors with a registry record: 1107 rows, 100.0% filled |
| P12 | 10 | 100.0% | 100.0% | +0.0 | n/a | no target · vendors with a registry record: 10 rows, 100.0% filled |
| P13 | 151168 | 40.2% | 40.2% | +0.0 | n/a | no target · vendors with a registry record: 60747 rows, 100.0% filled |

## 3. buyer

### `buyer_legal_name_as_published`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 313 | 97.1% | 97.1% | +0.7 | 90% | ✅ met |
| P01T | 228 | 71.5% | 71.5% | +0.8 | 90% | ❌ 18 pts to go |
| P01_GOLD | 650 | 87.8% | 87.8% | +0.4 | 95% | 🟡 7 pts to go |
| P02 | 475 | 88.8% | 88.8% | +0.6 | 95% | 🟡 6 pts to go |
| P03 | 272 | 83.5% | 83.5% | +0.4 | 85% | 🟡 2 pts to go |
| P04 | 4187 | 69.9% | 69.9% | +5.4 | 90% | ❌ 20 pts to go |
| P05 | 423 | 77.5% | 77.5% | -0.5 | 75% | ✅ met |
| P06M | 24573 | 94.5% | 94.5% | +0.7 | n/a | no target |
| P06T | 61958 | 37.4% | 37.4% | +0.5 | n/a | no target |
| P06 | 268 | 73.9% | 73.9% | +2.8 | 80% | 🟡 6 pts to go |
| P07 | 814 | 60.9% | 61.1% | +2.7 | 80% | ❌ 19 pts to go |
| P08 | 30392 | 56.8% | 56.8% | +4.9 | 75% | ❌ 18 pts to go |
| P09 | 279 | 75.3% | 75.3% | -0.3 | 95% | ❌ 20 pts to go |
| P10 | 2094 | 46.5% | 46.6% | -0.3 | 70% | ❌ 24 pts to go |
| P11 | 1830 | 33.0% | 33.0% | +1.2 | 65% | ❌ 32 pts to go |
| P12 | 10 | 80.0% | 80.0% | +7.3 | 80% | ✅ met |
| P13 | 151168 | 47.6% | 47.6% | +2.0 | 60% | ❌ 12 pts to go |

### `buyer_bn_as_published`

> ceiling: a buyer's BN is public only where the buyer prints it or a public dataset carries it (CRA charities, federal grants & contributions recipients, business registries for corporations); municipalities rarely publish theirs

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 313 | 17.6% | 17.6% | -0.9 | 50% | ❌ 32 pts to go |
| P01T | 228 | 16.7% | 16.7% | +0.5 | n/a | no target |
| P01_GOLD | 650 | 19.1% | 19.1% | -0.7 | 40% | ❌ 21 pts to go |
| P02 | 475 | 20.0% | 20.0% | +0.1 | 40% | ❌ 20 pts to go |
| P03 | 272 | 19.9% | 19.9% | -0.4 | 40% | ❌ 20 pts to go |
| P04 | 4187 | 15.0% | 15.0% | -1.3 | 40% | ❌ 25 pts to go |
| P05 | 423 | 21.3% | 21.3% | +0.4 | 25% | 🟡 4 pts to go |
| P06M | 24573 | 23.5% | 23.5% | +3.1 | n/a | no target |
| P06T | 61958 | 10.1% | 10.1% | +2.6 | n/a | no target |
| P06 | 268 | 21.3% | 21.3% | +3.8 | 35% | ❌ 14 pts to go |
| P07 | 814 | 23.1% | 23.1% | +4.0 | 35% | ❌ 12 pts to go |
| P08 | 30392 | 22.5% | 22.5% | +4.8 | 35% | ❌ 12 pts to go |
| P09 | 279 | 16.5% | 16.5% | -0.2 | n/a | no target |
| P10 | 2094 | 9.5% | 9.5% | +2.4 | 30% | ❌ 20 pts to go |
| P11 | 1830 | 10.1% | 10.1% | +3.6 | n/a | no target |
| P12 | 10 | 20.0% | 20.0% | +1.8 | n/a | no target |
| P13 | 151168 | 13.9% | 13.9% | +1.4 | 30% | ❌ 16 pts to go |

### `buyer_address`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 313 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P01T | 228 | 85.1% | 85.1% | -0.1 | 100% | ❌ 15 pts to go |
| P01_GOLD | 650 | 91.4% | 91.4% | +0.3 | 100% | 🟡 9 pts to go |
| P02 | 475 | 96.6% | 96.6% | +0.0 | 100% | 🟡 3 pts to go |
| P03 | 272 | 89.7% | 89.7% | +0.2 | 100% | ❌ 10 pts to go |
| P04 | 4187 | 76.8% | 76.8% | +4.3 | 100% | ❌ 23 pts to go |
| P05 | 423 | 89.8% | 89.8% | -0.2 | 100% | ❌ 10 pts to go |
| P06M | 24573 | 99.4% | 99.4% | +0.0 | n/a | no target |
| P06T | 61958 | 57.7% | 57.7% | -1.0 | n/a | no target |
| P06 | 268 | 82.8% | 82.8% | +0.7 | 95% | ❌ 12 pts to go |
| P07 | 814 | 85.9% | 85.9% | +0.5 | 95% | 🟡 9 pts to go |
| P08 | 30392 | 84.7% | 84.7% | +0.2 | 95% | ❌ 10 pts to go |
| P09 | 279 | 96.4% | 96.4% | +0.0 | 100% | 🟡 4 pts to go |
| P10 | 2094 | 54.3% | 54.3% | -0.3 | 95% | ❌ 41 pts to go |
| P11 | 1830 | 61.0% | 61.0% | +0.1 | 80% | ❌ 19 pts to go |
| P12 | 10 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P13 | 151168 | 100.0% | 100.0% | +0.0 | 95% | ✅ met |

### `buyer_phone`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 313 | 69.0% | 69.0% | -2.1 | n/a | no target |
| P01T | 228 | 74.1% | 74.1% | -0.1 | n/a | no target |
| P01_GOLD | 650 | 72.0% | 72.0% | -1.2 | 90% | ❌ 18 pts to go |
| P02 | 475 | 76.8% | 76.8% | -1.6 | 95% | ❌ 18 pts to go |
| P03 | 272 | 72.1% | 72.1% | -2.0 | 95% | ❌ 23 pts to go |
| P04 | 4187 | 60.7% | 60.7% | -8.8 | 95% | ❌ 34 pts to go |
| P05 | 423 | 72.3% | 72.3% | -0.2 | 90% | ❌ 18 pts to go |
| P06M | 24573 | 77.0% | 77.0% | +0.3 | n/a | no target |
| P06T | 61958 | 59.6% | 59.6% | +1.0 | n/a | no target |
| P06 | 268 | 71.6% | 71.6% | +6.2 | 95% | ❌ 23 pts to go |
| P07 | 814 | 68.2% | 68.2% | +8.5 | 90% | ❌ 22 pts to go |
| P08 | 30392 | 71.1% | 71.1% | +12.5 | 95% | ❌ 24 pts to go |
| P09 | 279 | 86.0% | 86.0% | +0.2 | 100% | ❌ 14 pts to go |
| P10 | 2094 | 53.7% | 53.7% | -0.1 | 95% | ❌ 41 pts to go |
| P11 | 1830 | 33.7% | 33.7% | +3.0 | 75% | ❌ 41 pts to go |
| P12 | 10 | 80.0% | 80.0% | -1.8 | n/a | no target |
| P13 | 151168 | 71.9% | 71.9% | +4.0 | 95% | ❌ 23 pts to go |

### `buyer_logo_url`

> ceiling: sites that block automated readers (robots.txt / 403) are never read; an og:image that looks like a photo is labelled

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 313 | 80.5% | 80.5% | -3.0 | n/a | no target |
| P01T | 228 | 92.1% | 92.1% | +0.4 | 95% | 🟡 3 pts to go |
| P01_GOLD | 650 | 83.1% | 83.1% | -1.9 | 90% | 🟡 7 pts to go |
| P02 | 475 | 88.8% | 88.8% | -2.2 | 95% | 🟡 6 pts to go |
| P03 | 272 | 82.0% | 82.0% | -1.8 | 95% | ❌ 13 pts to go |
| P04 | 4187 | 79.6% | 79.6% | -12.0 | 90% | ❌ 10 pts to go |
| P05 | 423 | 92.7% | 92.7% | +0.3 | 95% | 🟡 2 pts to go |
| P06M | 24573 | 89.5% | 89.5% | +4.2 | n/a | no target |
| P06T | 61958 | 88.3% | 88.3% | +3.7 | n/a | no target |
| P06 | 268 | 93.7% | 93.7% | +8.3 | 100% | 🟡 6 pts to go |
| P07 | 814 | 94.5% | 94.5% | +10.9 | 100% | 🟡 6 pts to go |
| P08 | 30392 | 95.1% | 95.1% | +17.3 | 100% | 🟡 5 pts to go |
| P09 | 279 | 73.8% | 73.8% | -0.4 | n/a | no target |
| P10 | 2094 | 94.4% | 94.4% | +0.0 | 100% | 🟡 6 pts to go |
| P11 | 1830 | 55.6% | 55.6% | +4.5 | 80% | ❌ 24 pts to go |
| P12 | 10 | 90.0% | 90.0% | -0.9 | n/a | no target |
| P13 | 151168 | 87.2% | 87.2% | +6.4 | 95% | 🟡 8 pts to go |

## 4. AP

### `ap_contact_name_as_published`

> ceiling: owner 2026-11-08: the AP contact person the organisation itself names on its AP / finance page is allowed (name + role phrase, quoted); mailboxes stay organisational; many bodies publish no AP person

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 313 | 2.9% | 2.9% | -0.3 | n/a | no target |
| P01T | 228 | 8.8% | 8.8% | +0.1 | n/a | no target |
| P01_GOLD | 650 | 13.4% | 13.4% | -0.6 | 25% | ❌ 12 pts to go |
| P02 | 475 | 24.4% | 24.4% | -0.4 | 40% | ❌ 16 pts to go |
| P03 | 272 | 8.5% | 8.5% | -0.5 | 20% | ❌ 12 pts to go |
| P04 | 4187 | 3.2% | 3.2% | -0.1 | 20% | ❌ 17 pts to go |
| P05 | 423 | 3.3% | 3.3% | +0.0 | 15% | ❌ 12 pts to go |
| P06M | 24573 | 0.3% | 0.3% | +0.0 | n/a | no target |
| P06T | 61958 | 0.2% | 0.2% | +0.0 | n/a | no target |
| P06 | 268 | 5.6% | 5.6% | +0.2 | n/a | no target |
| P07 | 814 | 8.1% | 8.1% | +0.2 | n/a | no target |
| P08 | 30392 | 0.2% | 0.2% | +0.0 | n/a | no target |
| P09 | 279 | 8.2% | 8.2% | +0.6 | n/a | no target |
| P10 | 2094 | 0.8% | 0.8% | +0.0 | n/a | no target |
| P11 | 1830 | 0.7% | 0.7% | +0.0 | n/a | no target |
| P12 | 10 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P13 | 151168 | 0.2% | 0.2% | +0.0 | n/a | no target |

### `ap_phone`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 313 | 13.7% | 13.7% | -2.4 | n/a | no target |
| P01T | 228 | 19.3% | 19.3% | +0.1 | 70% | ❌ 51 pts to go |
| P01_GOLD | 650 | 42.3% | 42.3% | +0.2 | 80% | ❌ 38 pts to go |
| P02 | 475 | 56.2% | 56.2% | -1.1 | 90% | ❌ 34 pts to go |
| P03 | 272 | 18.4% | 18.4% | -0.8 | 60% | ❌ 42 pts to go |
| P04 | 4187 | 18.3% | 18.3% | -1.9 | 85% | ❌ 67 pts to go |
| P05 | 423 | 11.8% | 11.8% | +0.7 | 50% | ❌ 38 pts to go |
| P06M | 24573 | 0.6% | 0.6% | +0.0 | n/a | no target |
| P06T | 61958 | 0.5% | 0.5% | +0.0 | n/a | no target |
| P06 | 268 | 13.1% | 13.1% | -0.1 | n/a | no target |
| P07 | 814 | 9.3% | 9.3% | +0.2 | n/a | no target |
| P08 | 30392 | 0.4% | 0.4% | -0.1 | n/a | no target |
| P09 | 279 | 74.9% | 74.9% | +2.9 | 95% | ❌ 20 pts to go |
| P10 | 2094 | 1.5% | 1.5% | -0.1 | n/a | no target |
| P11 | 1830 | 13.4% | 13.4% | +0.4 | n/a | no target |
| P12 | 10 | 30.0% | 30.0% | +2.7 | n/a | no target |
| P13 | 151168 | 0.3% | 0.3% | +0.0 | n/a | no target |

### `invoice_mailing_address`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 313 | 5.1% | 5.1% | -0.5 | n/a | no target |
| P01T | 228 | 9.6% | 9.6% | +0.4 | n/a | no target |
| P01_GOLD | 650 | 33.5% | 33.5% | -0.3 | 70% | ❌ 36 pts to go |
| P02 | 475 | 38.3% | 38.3% | -0.4 | 75% | ❌ 37 pts to go |
| P03 | 272 | 18.8% | 18.8% | -0.4 | 55% | ❌ 36 pts to go |
| P04 | 4187 | 18.3% | 18.3% | -1.9 | 75% | ❌ 57 pts to go |
| P05 | 423 | 10.9% | 10.9% | +0.7 | 50% | ❌ 39 pts to go |
| P06M | 24573 | 0.2% | 0.2% | +0.0 | n/a | no target |
| P06T | 61958 | 0.3% | 0.3% | +0.0 | n/a | no target |
| P06 | 268 | 5.2% | 5.2% | -0.5 | n/a | no target |
| P07 | 814 | 4.7% | 4.7% | +0.1 | n/a | no target |
| P08 | 30392 | 0.1% | 0.1% | -0.1 | n/a | no target |
| P09 | 279 | 71.7% | 71.7% | +3.0 | 95% | ❌ 23 pts to go |
| P10 | 2094 | 0.8% | 0.8% | +0.0 | n/a | no target |
| P11 | 1830 | 13.2% | 13.2% | +0.4 | n/a | no target |
| P12 | 10 | 20.0% | 20.0% | +1.8 | n/a | no target |
| P13 | 151168 | 0.2% | 0.2% | +0.0 | n/a | no target |

### `invoicing_requirements`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 313 | 6.1% | 6.1% | -1.5 | n/a | no target |
| P01T | 228 | 8.8% | 8.8% | +0.1 | n/a | no target |
| P01_GOLD | 650 | 56.3% | 56.5% | -0.8 | 80% | ❌ 24 pts to go |
| P02 | 475 | 44.4% | 44.6% | -0.9 | 75% | ❌ 31 pts to go |
| P03 | 272 | 35.3% | 35.3% | -0.8 | 70% | ❌ 35 pts to go |
| P04 | 4187 | 18.2% | 18.5% | -1.7 | 70% | ❌ 52 pts to go |
| P05 | 423 | 14.4% | 14.4% | +0.4 | 50% | ❌ 36 pts to go |
| P06M | 24573 | 0.3% | 0.3% | +0.0 | n/a | no target |
| P06T | 61958 | 0.2% | 0.2% | +0.0 | n/a | no target |
| P06 | 268 | 13.8% | 13.8% | +0.6 | n/a | no target |
| P07 | 814 | 1.0% | 1.0% | -0.1 | n/a | no target |
| P08 | 30392 | 0.3% | 0.3% | +0.0 | n/a | no target |
| P09 | 279 | 48.4% | 49.1% | +1.5 | 80% | ❌ 32 pts to go |
| P10 | 2094 | 1.1% | 1.1% | +0.0 | n/a | no target |
| P11 | 1830 | 4.5% | 4.6% | +0.0 | n/a | no target |
| P12 | 10 | 30.0% | 30.0% | -6.4 | n/a | no target |
| P13 | 151168 | 0.1% | 0.1% | +0.0 | n/a | no target |

### `payment_terms_as_published`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 313 | 14.1% | 14.1% | -0.8 | n/a | no target |
| P01T | 228 | 19.7% | 19.7% | +0.5 | 60% | ❌ 40 pts to go |
| P01_GOLD | 650 | 60.6% | 60.6% | -1.6 | 70% | 🟡 9 pts to go |
| P02 | 475 | 38.1% | 38.1% | -1.4 | 50% | ❌ 12 pts to go |
| P03 | 272 | 45.6% | 45.6% | -2.1 | 55% | 🟡 9 pts to go |
| P04 | 4187 | 10.8% | 10.8% | -1.7 | 40% | ❌ 29 pts to go |
| P05 | 423 | 16.3% | 16.3% | -0.3 | 40% | ❌ 24 pts to go |
| P06M | 24573 | 2.5% | 2.5% | -0.3 | n/a | no target |
| P06T | 61958 | 1.5% | 1.5% | +0.0 | n/a | no target |
| P06 | 268 | 18.3% | 18.3% | +0.1 | n/a | no target |
| P07 | 814 | 4.9% | 4.9% | +0.0 | n/a | no target |
| P08 | 30392 | 2.0% | 2.0% | -0.1 | n/a | no target |
| P09 | 279 | 6.5% | 6.5% | +0.7 | n/a | no target |
| P10 | 2094 | 4.8% | 4.8% | -0.3 | n/a | no target |
| P11 | 1830 | 4.0% | 4.0% | +0.0 | n/a | no target |
| P12 | 10 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P13 | 151168 | 0.7% | 0.7% | +0.0 | n/a | no target |

### `po_required_as_published`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 313 | 19.2% | 19.2% | -2.5 | n/a | no target |
| P01T | 228 | 27.2% | 27.2% | -0.7 | 65% | ❌ 38 pts to go |
| P01_GOLD | 650 | 66.6% | 66.6% | -2.0 | 70% | 🟡 3 pts to go |
| P02 | 475 | 22.7% | 22.7% | -1.0 | 50% | ❌ 27 pts to go |
| P03 | 272 | 48.9% | 48.9% | -1.5 | 60% | ❌ 11 pts to go |
| P04 | 4187 | 4.8% | 4.8% | -0.8 | 40% | ❌ 35 pts to go |
| P05 | 423 | 19.9% | 19.9% | +0.0 | 45% | ❌ 25 pts to go |
| P06M | 24573 | 1.5% | 1.5% | -0.2 | n/a | no target |
| P06T | 61958 | 0.6% | 0.6% | +0.0 | n/a | no target |
| P06 | 268 | 28.7% | 28.7% | -0.6 | n/a | no target |
| P07 | 814 | 4.8% | 4.8% | -0.3 | n/a | no target |
| P08 | 30392 | 0.9% | 0.9% | +0.0 | n/a | no target |
| P09 | 279 | 10.8% | 10.8% | -0.1 | n/a | no target |
| P10 | 2094 | 3.1% | 3.1% | -0.2 | n/a | no target |
| P11 | 1830 | 3.6% | 3.6% | +0.0 | n/a | no target |
| P12 | 10 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P13 | 151168 | 0.2% | 0.2% | +0.0 | n/a | no target |

### `invoice_portal_url`

> ceiling: only portals the buyer names on its own pages; informational tax-authority links are not portals

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 313 | 11.2% | 11.2% | -0.8 | n/a | no target |
| P01T | 228 | 12.7% | 12.7% | +0.0 | n/a | no target |
| P01_GOLD | 650 | 48.2% | 48.2% | -2.0 | 50% | 🟡 2 pts to go |
| P02 | 475 | 37.3% | 37.3% | -0.3 | n/a | no target |
| P03 | 272 | 49.6% | 49.6% | -1.2 | 60% | ❌ 10 pts to go |
| P04 | 4187 | 10.8% | 10.8% | -2.0 | n/a | no target |
| P05 | 423 | 15.4% | 15.4% | +0.2 | n/a | no target |
| P06M | 24573 | 0.7% | 0.7% | -0.1 | n/a | no target |
| P06T | 61958 | 0.3% | 0.3% | +0.0 | n/a | no target |
| P06 | 268 | 20.1% | 20.1% | -0.3 | n/a | no target |
| P07 | 814 | 5.0% | 5.0% | -0.7 | n/a | no target |
| P08 | 30392 | 0.4% | 0.4% | +0.0 | n/a | no target |
| P09 | 279 | 20.8% | 20.8% | +0.1 | n/a | no target |
| P10 | 2094 | 2.2% | 2.2% | -0.3 | n/a | no target |
| P11 | 1830 | 2.6% | 2.6% | -0.1 | n/a | no target |
| P12 | 10 | 20.0% | 20.0% | +1.8 | n/a | no target |
| P13 | 151168 | 0.2% | 0.2% | +0.0 | n/a | no target |

### `buyer_payment_method_preference`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 313 | 7.7% | 7.7% | -1.1 | 15% | 🟡 7 pts to go |
| P01T | 228 | 12.7% | 12.7% | +0.0 | 15% | 🟡 2 pts to go |
| P01_GOLD | 650 | 34.0% | 34.0% | -1.1 | 40% | 🟡 6 pts to go |
| P02 | 475 | 11.8% | 12.0% | -0.4 | 25% | ❌ 13 pts to go |
| P03 | 272 | 15.8% | 15.8% | -0.7 | 25% | 🟡 9 pts to go |
| P04 | 4187 | 2.3% | 2.3% | -0.4 | 15% | ❌ 13 pts to go |
| P05 | 423 | 6.4% | 6.4% | -0.2 | 15% | 🟡 9 pts to go |
| P06M | 24573 | 0.8% | 0.8% | +0.0 | 15% | ❌ 14 pts to go |
| P06T | 61958 | 0.7% | 0.7% | +0.0 | 15% | ❌ 14 pts to go |
| P06 | 268 | 9.3% | 9.3% | +0.0 | 15% | 🟡 6 pts to go |
| P07 | 814 | 3.3% | 3.3% | -0.1 | 15% | ❌ 12 pts to go |
| P08 | 30392 | 0.6% | 0.6% | +0.1 | 15% | ❌ 14 pts to go |
| P09 | 279 | 1.1% | 1.1% | +0.0 | 15% | ❌ 14 pts to go |
| P10 | 2094 | 1.4% | 1.4% | +0.0 | 15% | ❌ 14 pts to go |
| P11 | 1830 | 1.3% | 1.3% | +0.1 | 15% | ❌ 14 pts to go |
| P12 | 10 | 0.0% | 0.0% | +0.0 | 15% | ❌ 15 pts to go |
| P13 | 151168 | 0.7% | 0.7% | +0.1 | 15% | ❌ 14 pts to go |

### `buyer_tax_exempt_status`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 313 | 5.4% | 5.4% | -0.2 | 15% | 🟡 10 pts to go |
| P01T | 228 | 11.0% | 11.0% | +0.1 | 25% | ❌ 14 pts to go |
| P01_GOLD | 650 | 27.8% | 27.8% | -1.1 | 25% | ✅ met |
| P02 | 475 | 24.6% | 24.6% | -0.8 | 15% | ✅ met |
| P03 | 272 | 21.7% | 21.7% | -0.1 | 15% | ✅ met |
| P04 | 4187 | 3.4% | 3.4% | -0.6 | 15% | ❌ 12 pts to go |
| P05 | 423 | 11.6% | 11.6% | +0.2 | 15% | 🟡 3 pts to go |
| P06M | 24573 | 0.6% | 0.6% | +0.0 | 15% | ❌ 14 pts to go |
| P06T | 61958 | 0.2% | 0.2% | +0.0 | 15% | ❌ 15 pts to go |
| P06 | 268 | 6.7% | 6.7% | -0.4 | 15% | 🟡 8 pts to go |
| P07 | 814 | 1.7% | 1.7% | -0.1 | 15% | ❌ 13 pts to go |
| P08 | 30392 | 0.3% | 0.3% | +0.0 | 15% | ❌ 15 pts to go |
| P09 | 279 | 1.4% | 1.4% | -0.1 | 15% | ❌ 14 pts to go |
| P10 | 2094 | 1.5% | 1.5% | -0.1 | 15% | ❌ 14 pts to go |
| P11 | 1830 | 1.8% | 1.8% | +0.0 | 15% | ❌ 13 pts to go |
| P12 | 10 | 0.0% | 0.0% | +0.0 | 15% | ❌ 15 pts to go |
| P13 | 151168 | 0.1% | 0.1% | +0.0 | 15% | ❌ 15 pts to go |

### `buyer_ap_cycle_published`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 313 | 1.6% | 1.6% | +0.0 | 20% | ❌ 18 pts to go |
| P01T | 228 | 3.1% | 3.1% | +0.0 | 20% | ❌ 17 pts to go |
| P01_GOLD | 650 | 4.2% | 4.2% | -0.1 | 20% | ❌ 16 pts to go |
| P02 | 475 | 1.3% | 1.3% | -0.2 | 20% | ❌ 19 pts to go |
| P03 | 272 | 1.8% | 1.8% | -0.1 | 20% | ❌ 18 pts to go |
| P04 | 4187 | 0.6% | 0.6% | -0.1 | 20% | ❌ 19 pts to go |
| P05 | 423 | 0.9% | 0.9% | +0.0 | 20% | ❌ 19 pts to go |
| P06M | 24573 | 0.0% | 0.0% | +0.0 | 20% | ❌ 20 pts to go |
| P06T | 61958 | 0.0% | 0.0% | +0.0 | 20% | ❌ 20 pts to go |
| P06 | 268 | 1.5% | 1.5% | +0.1 | 20% | ❌ 18 pts to go |
| P07 | 814 | 0.2% | 0.2% | +0.0 | 20% | ❌ 20 pts to go |
| P08 | 30392 | 0.0% | 0.0% | +0.0 | 20% | ❌ 20 pts to go |
| P09 | 279 | 0.0% | 0.0% | +0.0 | 20% | ❌ 20 pts to go |
| P10 | 2094 | 0.3% | 0.3% | +0.0 | 20% | ❌ 20 pts to go |
| P11 | 1830 | 0.1% | 0.1% | +0.0 | 20% | ❌ 20 pts to go |
| P12 | 10 | 0.0% | 0.0% | +0.0 | 20% | ❌ 20 pts to go |
| P13 | 151168 | 0.0% | 0.0% | +0.0 | 20% | ❌ 20 pts to go |

### `buyer_esignature_preference`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 313 | 1.3% | 1.3% | -0.3 | 15% | ❌ 14 pts to go |
| P01T | 228 | 3.1% | 3.1% | +0.0 | 15% | ❌ 12 pts to go |
| P01_GOLD | 650 | 10.3% | 10.3% | -0.2 | 15% | 🟡 5 pts to go |
| P02 | 475 | 10.9% | 10.9% | -0.6 | 15% | 🟡 4 pts to go |
| P03 | 272 | 20.2% | 20.2% | -0.5 | 15% | ✅ met |
| P04 | 4187 | 2.0% | 2.0% | -0.4 | 15% | ❌ 13 pts to go |
| P05 | 423 | 2.8% | 2.8% | +0.0 | 15% | ❌ 12 pts to go |
| P06M | 24573 | 0.4% | 0.4% | +0.0 | 15% | ❌ 15 pts to go |
| P06T | 61958 | 0.2% | 0.2% | +0.0 | 15% | ❌ 15 pts to go |
| P06 | 268 | 4.1% | 4.1% | +0.2 | 15% | ❌ 11 pts to go |
| P07 | 814 | 1.2% | 1.2% | +0.0 | 15% | ❌ 14 pts to go |
| P08 | 30392 | 0.3% | 0.3% | +0.0 | 15% | ❌ 15 pts to go |
| P09 | 279 | 0.7% | 0.7% | +0.0 | 15% | ❌ 14 pts to go |
| P10 | 2094 | 1.1% | 1.1% | +0.0 | 15% | ❌ 14 pts to go |
| P11 | 1830 | 0.8% | 0.8% | +0.0 | 15% | ❌ 14 pts to go |
| P12 | 10 | 0.0% | 0.0% | +0.0 | 15% | ❌ 15 pts to go |
| P13 | 151168 | 0.1% | 0.1% | +0.0 | 15% | ❌ 15 pts to go |

### `ap_system_hint`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 313 | 12.5% | 12.5% | +0.1 | 20% | 🟡 8 pts to go |
| P01T | 228 | 13.6% | 13.6% | +0.1 | 40% | ❌ 26 pts to go |
| P01_GOLD | 650 | 44.6% | 44.6% | -2.0 | 40% | ✅ met |
| P02 | 475 | 42.9% | 42.9% | -0.3 | 20% | ✅ met |
| P03 | 272 | 47.1% | 47.1% | -1.4 | 35% | ✅ met |
| P04 | 4187 | 12.7% | 12.7% | -2.2 | 20% | 🟡 7 pts to go |
| P05 | 423 | 15.8% | 15.8% | +0.2 | 20% | 🟡 4 pts to go |
| P06M | 24573 | 1.0% | 1.0% | +0.0 | 20% | ❌ 19 pts to go |
| P06T | 61958 | 0.6% | 0.6% | +0.0 | 20% | ❌ 19 pts to go |
| P06 | 268 | 20.5% | 20.5% | -0.6 | 20% | ✅ met |
| P07 | 814 | 5.7% | 5.7% | -0.4 | 20% | ❌ 14 pts to go |
| P08 | 30392 | 0.8% | 0.8% | +0.0 | 20% | ❌ 19 pts to go |
| P09 | 279 | 21.1% | 21.1% | +0.0 | 20% | ✅ met |
| P10 | 2094 | 3.5% | 3.5% | -0.3 | 20% | ❌ 16 pts to go |
| P11 | 1830 | 3.2% | 3.2% | +0.0 | 20% | ❌ 17 pts to go |
| P12 | 10 | 10.0% | 10.0% | +0.9 | 20% | 🟡 10 pts to go |
| P13 | 151168 | 0.4% | 0.4% | +0.0 | 20% | ❌ 20 pts to go |

## 5. contract

### `contract_value`

> ceiling: rows proven by a lobbying filing, a news release, an auditor appointment, a customer story or a vendor's client list have no contract value by nature (≈17 % of P01 Gold); bids&tenders awards now carry the awarded bidder's submitted price when no award value was published

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 313 | 14.4% | 14.4% | -3.7 | n/a | no target |
| P01T | 228 | 0.4% | 0.4% | +0.0 | n/a | no target |
| P01_GOLD | 650 | 69.7% | 69.7% | -1.9 | 95% | ❌ 25 pts to go |
| P02 | 475 | 64.2% | 64.2% | -2.0 | 95% | ❌ 31 pts to go |
| P03 | 272 | 55.9% | 55.9% | -2.0 | 90% | ❌ 34 pts to go |
| P04 | 4187 | 23.7% | 23.7% | -2.8 | 85% | ❌ 61 pts to go |
| P05 | 423 | 39.0% | 39.0% | +0.1 | 75% | ❌ 36 pts to go |
| P06M | 24573 | 26.0% | 26.0% | -2.1 | n/a | no target |
| P06T | 61958 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06 | 268 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P07 | 814 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P08 | 30392 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P09 | 279 | 89.6% | 89.6% | +0.5 | 100% | ❌ 10 pts to go |
| P10 | 2094 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P11 | 1830 | 3.9% | 3.9% | +0.1 | 60% | ❌ 56 pts to go |
| P12 | 10 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P13 | 151168 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `currency`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 313 | 14.4% | 14.4% | -3.7 | n/a | no target |
| P01T | 228 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P01_GOLD | 650 | 71.4% | 71.4% | -2.1 | 100% | ❌ 29 pts to go |
| P02 | 475 | 66.3% | 66.3% | -1.9 | 100% | ❌ 34 pts to go |
| P03 | 272 | 58.5% | 58.5% | -2.0 | n/a | no target |
| P04 | 4187 | 24.1% | 24.1% | -2.9 | 95% | ❌ 71 pts to go |
| P05 | 423 | 34.8% | 34.8% | +0.2 | 80% | ❌ 45 pts to go |
| P06M | 24573 | 26.0% | 26.0% | -2.1 | n/a | no target |
| P06T | 61958 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06 | 268 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P07 | 814 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P08 | 30392 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P09 | 279 | 92.1% | 92.1% | +0.5 | 100% | 🟡 8 pts to go |
| P10 | 2094 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P11 | 1830 | 4.1% | 4.1% | +0.1 | n/a | no target |
| P12 | 10 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P13 | 151168 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `start_date`

> ceiling: most award notices publish an award date, not a start date; start_date carries the signature date when the source gives one, labelled

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 313 | 82.4% | 82.4% | -1.9 | n/a | no target |
| P01T | 228 | 0.4% | 0.4% | +0.0 | n/a | no target |
| P01_GOLD | 650 | 53.8% | 53.8% | +1.5 | 85% | ❌ 31 pts to go |
| P02 | 475 | 60.4% | 60.4% | +1.2 | 90% | ❌ 30 pts to go |
| P03 | 272 | 46.0% | 46.0% | +2.0 | 85% | ❌ 39 pts to go |
| P04 | 4187 | 40.0% | 40.0% | +10.9 | 90% | ❌ 50 pts to go |
| P05 | 423 | 33.3% | 33.3% | +0.4 | 75% | ❌ 42 pts to go |
| P06M | 24573 | 82.7% | 82.7% | -1.6 | n/a | no target |
| P06T | 61958 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06 | 268 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P07 | 814 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P08 | 30392 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P09 | 279 | 82.4% | 82.4% | +0.6 | 95% | ❌ 13 pts to go |
| P10 | 2094 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P11 | 1830 | 3.7% | 3.7% | +0.4 | n/a | no target |
| P12 | 10 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P13 | 151168 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `end_date`

> ceiling: an inferred end (award date + published duration) is labelled as such; sources without a duration leave end_date empty — the honest ceiling. P09 is BY DEFINITION the rows whose end date is not published (older SEAO contracts with no closing notice): its end_date / duration targets cannot be met without inventing a date

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 313 | 56.2% | 56.2% | -9.7 | n/a | no target |
| P01T | 228 | 0.4% | 0.4% | +0.0 | n/a | no target |
| P01_GOLD | 650 | 53.5% | 53.5% | +1.5 | 85% | ❌ 32 pts to go |
| P02 | 475 | 54.7% | 54.7% | +1.3 | 90% | ❌ 35 pts to go |
| P03 | 272 | 46.3% | 46.3% | +1.9 | 85% | ❌ 39 pts to go |
| P04 | 4187 | 35.1% | 35.1% | +10.5 | 90% | ❌ 55 pts to go |
| P05 | 423 | 42.6% | 42.6% | -0.1 | 75% | ❌ 32 pts to go |
| P06M | 24573 | 64.7% | 64.7% | -4.5 | n/a | no target |
| P06T | 61958 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06 | 268 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P07 | 814 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P08 | 30392 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P09 | 279 | 0.4% | 0.4% | +0.0 | 95% | ❌ 95 pts to go |
| P10 | 2094 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P11 | 1830 | 2.8% | 2.8% | +0.3 | n/a | no target |
| P12 | 10 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P13 | 151168 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `contract_title`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 313 | 96.2% | 96.2% | +1.0 | n/a | no target |
| P01T | 228 | 96.1% | 96.1% | +0.0 | n/a | no target |
| P01_GOLD | 650 | 85.8% | 86.0% | +0.3 | 100% | ❌ 14 pts to go |
| P02 | 475 | 78.7% | 78.7% | +1.1 | 100% | ❌ 21 pts to go |
| P03 | 272 | 92.6% | 92.6% | +0.1 | n/a | no target |
| P04 | 4187 | 58.2% | 58.2% | +7.6 | 95% | ❌ 37 pts to go |
| P05 | 423 | 77.3% | 77.3% | +0.0 | 95% | ❌ 18 pts to go |
| P06M | 24573 | 99.3% | 99.3% | +0.0 | n/a | no target |
| P06T | 61958 | 94.7% | 94.7% | +0.2 | n/a | no target |
| P06 | 268 | 21.3% | 21.3% | +0.9 | n/a | no target |
| P07 | 814 | 10.2% | 10.2% | +0.0 | n/a | no target |
| P08 | 30392 | 4.5% | 4.5% | +0.0 | n/a | no target |
| P09 | 279 | 98.2% | 98.2% | +0.0 | 100% | 🟡 2 pts to go |
| P10 | 2094 | 70.4% | 70.4% | -0.2 | n/a | no target |
| P11 | 1830 | 70.2% | 70.2% | +0.4 | n/a | no target |
| P12 | 10 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P13 | 151168 | 99.6% | 99.6% | +0.0 | n/a | no target |

### `contract_description`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 313 | 96.2% | 96.2% | +1.0 | n/a | no target |
| P01T | 228 | 96.1% | 96.1% | +0.0 | n/a | no target |
| P01_GOLD | 650 | 88.9% | 89.1% | +0.2 | 100% | ❌ 11 pts to go |
| P02 | 475 | 80.0% | 80.0% | +1.2 | 100% | ❌ 20 pts to go |
| P03 | 272 | 93.4% | 93.4% | +0.2 | n/a | no target |
| P04 | 4187 | 61.1% | 61.1% | +7.1 | 95% | ❌ 34 pts to go |
| P05 | 423 | 89.6% | 89.6% | +0.3 | 70% | ✅ met |
| P06M | 24573 | 99.3% | 99.3% | +0.0 | n/a | no target |
| P06T | 61958 | 94.7% | 94.7% | +0.2 | n/a | no target |
| P06 | 268 | 21.3% | 21.3% | +0.9 | n/a | no target |
| P07 | 814 | 10.2% | 10.2% | +0.0 | n/a | no target |
| P08 | 30392 | 4.5% | 4.5% | +0.0 | n/a | no target |
| P09 | 279 | 98.2% | 98.2% | +0.0 | 100% | 🟡 2 pts to go |
| P10 | 2094 | 70.4% | 70.4% | -0.2 | n/a | no target |
| P11 | 1830 | 70.2% | 70.2% | +0.3 | n/a | no target |
| P12 | 10 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P13 | 151168 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `number_of_bids`

> ceiling: published by some portals only (bids&tenders submission lists, Biddingo bidder lists); federal proactive disclosure does not publish bid counts

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 313 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P01T | 228 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P01_GOLD | 650 | 16.3% | 16.3% | -0.6 | 60% | ❌ 44 pts to go · rows from a source that publishes bids: 368 rows, 28.8% filled |
| P02 | 475 | 10.3% | 10.3% | -0.4 | n/a | no target · rows from a source that publishes bids: 295 rows, 16.6% filled |
| P03 | 272 | 13.2% | 13.2% | -0.7 | n/a | no target · rows from a source that publishes bids: 141 rows, 25.5% filled |
| P04 | 4187 | 1.5% | 1.5% | -0.2 | n/a | no target · rows from a source that publishes bids: 878 rows, 6.9% filled |
| P05 | 423 | 2.6% | 2.6% | +0.0 | n/a | no target · rows from a source that publishes bids: 55 rows, 20.0% filled |
| P06M | 24573 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06T | 61958 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06 | 268 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P07 | 814 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P08 | 30392 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P09 | 279 | 3.9% | 3.9% | -0.5 | n/a | no target · rows from a source that publishes bids: 266 rows, 4.1% filled |
| P10 | 2094 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P11 | 1830 | 0.4% | 0.4% | +0.0 | n/a | no target · rows from a source that publishes bids: 69 rows, 11.6% filled |
| P12 | 10 | 0.0% | 0.0% | +0.0 | n/a | no target · rows from a source that publishes bids: 10 rows, 0.0% filled |
| P13 | 151168 | 0.0% | 0.0% | +0.0 | n/a | no target |

## 6. history

### `average_contract_duration_days`

> ceiling: needs two dates (or a published term) on the buyer's records; P09 rows (end date unpublished by definition) and buyers whose sources publish award dates only have no honest duration

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 313 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P01T | 228 | 0.0% | 97.8% | +0.0 | n/a | no target |
| P01_GOLD | 650 | 51.7% | 82.8% | -1.7 | 90% | ❌ 38 pts to go |
| P02 | 475 | 51.8% | 87.2% | -1.6 | 90% | ❌ 38 pts to go |
| P03 | 272 | 44.5% | 80.5% | -1.4 | 90% | ❌ 46 pts to go |
| P04 | 4187 | 16.8% | 94.0% | -2.8 | 90% | ❌ 73 pts to go |
| P05 | 423 | 0.0% | 82.3% | +0.0 | 90% | ❌ 90 pts to go |
| P06M | 24573 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P06T | 61958 | 0.0% | 99.9% | +0.0 | n/a | no target |
| P06 | 268 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P07 | 814 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P08 | 30392 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P09 | 279 | 2.9% | 4.7% | +0.0 | 90% | ❌ 87 pts to go |
| P10 | 2094 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P11 | 1830 | 2.2% | 97.7% | +0.1 | n/a | no target |
| P12 | 10 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P13 | 151168 | 0.0% | 100.0% | +0.0 | n/a | no target |

### `commodity_distribution_top3`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 313 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P01T | 228 | 0.9% | 98.7% | +0.0 | n/a | no target |
| P01_GOLD | 650 | 25.5% | 56.6% | -1.0 | 90% | ❌ 64 pts to go |
| P02 | 475 | 50.7% | 86.1% | -1.7 | n/a | no target |
| P03 | 272 | 24.6% | 60.7% | -0.6 | n/a | no target |
| P04 | 4187 | 18.2% | 95.5% | -3.2 | n/a | no target |
| P05 | 423 | 0.5% | 82.7% | +0.0 | n/a | no target |
| P06M | 24573 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P06T | 61958 | 0.1% | 99.9% | +0.0 | n/a | no target |
| P06 | 268 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P07 | 814 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P08 | 30392 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P09 | 279 | 40.9% | 42.7% | +0.5 | n/a | no target |
| P10 | 2094 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P11 | 1830 | 2.3% | 97.8% | +0.1 | n/a | no target |
| P12 | 10 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P13 | 151168 | 0.0% | 100.0% | +0.0 | n/a | no target |

### `year_over_year_spend_trend`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 313 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P01T | 228 | 2.2% | 100.0% | +0.0 | n/a | no target |
| P01_GOLD | 650 | 50.6% | 81.7% | -1.4 | 95% | ❌ 44 pts to go |
| P02 | 475 | 56.2% | 91.6% | -1.9 | n/a | no target |
| P03 | 272 | 48.5% | 84.6% | -1.9 | n/a | no target |
| P04 | 4187 | 18.9% | 96.1% | -3.3 | n/a | no target |
| P05 | 423 | 5.0% | 87.2% | +0.0 | n/a | no target |
| P06M | 24573 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P06T | 61958 | 0.1% | 100.0% | +0.0 | n/a | no target |
| P06 | 268 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P07 | 814 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P08 | 30392 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P09 | 279 | 60.6% | 62.4% | +0.2 | n/a | no target |
| P10 | 2094 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P11 | 1830 | 2.3% | 97.8% | -0.1 | n/a | no target |
| P12 | 10 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P13 | 151168 | 0.0% | 100.0% | +0.0 | n/a | no target |

## 7. mail security

### `mta_sts`

> ceiling: DNS-only check; 'no record' counts as checked

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 313 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P01T | 228 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P01_GOLD | 650 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P02 | 475 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P03 | 272 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P04 | 4187 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P05 | 423 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P06M | 24573 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P06T | 61958 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P06 | 268 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P07 | 814 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P08 | 30392 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P09 | 279 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P10 | 2094 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P11 | 1830 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P12 | 10 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P13 | 151168 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |

### `tls_rpt`

> ceiling: DNS-only check; 'no record' counts as checked

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 313 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P01T | 228 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P01_GOLD | 650 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P02 | 475 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P03 | 272 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P04 | 4187 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P05 | 423 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P06M | 24573 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P06T | 61958 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P06 | 268 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P07 | 814 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P08 | 30392 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P09 | 279 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P10 | 2094 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P11 | 1830 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P12 | 10 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P13 | 151168 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |

### `bimi`

> ceiling: DNS-only check; 'no record' counts as checked

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 313 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P01T | 228 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P01_GOLD | 650 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P02 | 475 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P03 | 272 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P04 | 4187 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P05 | 423 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P06M | 24573 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P06T | 61958 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P06 | 268 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P07 | 814 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P08 | 30392 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P09 | 279 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P10 | 2094 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P11 | 1830 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P12 | 10 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P13 | 151168 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |

