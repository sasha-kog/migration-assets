# Example: `process incoming netsuite case` — run from Mar 2, 2026

This is the canonical filled capture example. The migration spec references this folder via `<REFERENCE_FILLED_CAPTURE>` so the agent can model new `run_capture_filled.md` files on it.

## Context

- **Automation:** `process incoming netsuite case` (orchestrator)
- **Captured case:** `#54133` (Get Freighted Pty Ltd / Scanned PDF)
- **Final outcome:** routed into the `to create a sales order` sub-automation (Stage F → Sales Order branch)
- **Pre-Phase-0 era:** captured manually before the Phase 0 automation existed. Sections are organized by stage (A through G), reflecting the pipeline's narrative flow rather than the newer stage-number scheme. Phase 0 outputs will use numeric stage IDs going forward; the *content depth* this example demonstrates is what to emulate.

## What's in this folder

| File | What it is |
|---|---|
| `run_capture_filled.md` | The human-readable narrative — what to emulate |
| `email.html` | Captured input (orchestrator processes incoming emails) |
| `message_record.json` | NetSuite message record retrieved during Stage B |
| `support_record.json` | NetSuite supportCase record retrieved during Stage B |

## What this example demonstrates well

- Branch-by-stage narrative with the literal predicate that fired
- Sub-automation invocation noted with inputs passed (Stage F)
- Captured values link to on-disk artifacts (input file, JSON records)
- Final summary section with outcome + cases processed

## What this example is missing (vs. the current spec)

- `run_capture.json` companion (introduced later — current spec requires both `.md` and `.json` per capture)
- `stage<N>_branch_trace.json` per stage (introduced with Phase 0/B API trace fetch)
- KLang version + comparability tagging per stage
- Numeric stage numbering (this uses A/B/C/... letter labels)

A new captured run today should fix those gaps. This folder is reference for *narrative density*, not field-level schema.
