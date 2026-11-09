# Payability pilot — stratified sample (owner 2026-11-09 11:05–11:13 EST)

**Why.** Payability, not plausibility, is the metric (owner 11:05). A completed row says an invoice *should* clear; only an invoice that is sent and
paid says it *does*. The 833 best rows cannot measure the other 63,000 (selection bias), so the pilot samples every stratum and measures each one.
The results calibrate the whole pack: a stratum's measured payment rate becomes the confidence attached to every row of that type, and an inferred
value graduates from plausibility to payability only when its stratum pays like the published one.

**Precondition — no exceptions.** A pilot invoice is a real invoice: issued by the vendor named on the row, for goods or services actually delivered
under that contract or relationship, with the vendor's own GST/HST number. The dataset gives the vendor its buyer's billing rules and channel; it never
bills on a vendor's behalf. (AP matches invoices to purchase orders and vendor master records — an invoice from a party the buyer does not know
bounces whatever the data says, so a fake test would measure nothing anyway.) Rows with `sensitivity_flag = yes`, an unconfirmed mailbox or a vendor
registry warning are excluded from the sample.

**Sample** — `PILOT_SAMPLE_2026-11-09.csv`, 230 rows, drawn with seed 20261109, spread across organisation types and provinces:
| stratum | rows | what it tests |
|---|---|---|
| S1 gold, complete, published PO rule (grade A/B) | 30 of 270 | the model itself: is "everything public" enough to be paid on sight? (30, not 833 — the owner will not burn the Gold on a test) |
| S2 complete, no published PO rule | 50 of 803 | does "PO: as provided by the buyer" clear, or does the buyer send it back for a number first? how many days to get one? |
| S3 routed — public body, general / purchasing inbox only | 50 of 1,877 | does an invoice to the only published inbox reach AP and get paid, and how much slower? |
| S4 routed — company buyer (P13), general inbox | 50 of 20,050 | the weakest and largest layer: payment rate when the relationship is inferred from the vendor's own evidence |
| S5 complete except the vendor's GST number | 50 of 432 | the vendor supplies its own number: confirms the "GST ceiling" is a data gap, not a payability gap |

**Outcome columns** (fill per row; blank = not yet): `outcome_invoice_sent_date`, `outcome_channel_used` (mailbox / portal / other), `outcome_accepted`
(accepted / returned / bounced / no response at 30 days), `outcome_bounce_reason` (the buyer's words), `outcome_po_requested` (yes/no),
`outcome_po_provided_days`, `outcome_paid_date`, `outcome_days_to_pay`, `outcome_amount_paid_vs_invoiced` (full / partial / none), `outcome_notes`.

**What comes back into the pack** (`tools/pilot_feedback.py`, to be written when the first outcomes exist): per-stratum acceptance and payment
rates → `payability_measured` column on every delivered row of that stratum ("S3: 41 % paid within 45 days, n=50"); bounce reasons → new required
elements in the completeness test if a reason recurs (e.g. "vendor must register first" → supplier setup becomes mandatory for that buyer type);
PO-request rate in S2 → whether the peer-group PO inference graduates to payability. Fifty rows per stratum separate 30 % from 80 % — the decision
that matters; they cannot separate 60 % from 70 %, and the report will say so.
