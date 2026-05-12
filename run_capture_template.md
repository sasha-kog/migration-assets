# Run Capture Template — `<AUTOMATION_NAME>`

Use this as the structural skeleton for `run_capture_filled.md` in each per-run folder. The agent fills in branch labels and observable fields specific to the automation being migrated. The trace JSONs (`stage<N>_branch_trace.json`) are the underlying data; this markdown is the human-readable summary.

See `example_filled_capture/run_capture_filled.md` (sibling folder) for a real, completed example.

---

## 1. Run Metadata

- **Run ID:** `<orchestrator_run_id>`
- **Run URL:** `<full app.kognitos.com run URL>`
- **Run timestamp:** `<ISO 8601>`
- **Case number (`caseNumber`):** `<value>`
- **Input file name:** `<filename or N/A>`
- **Input file extension:** `<ext>`
- **Primary branch(es) this run demonstrates:** `<comma-separated branch IDs from branch_catalog.json>`

---

## 2. Inputs

Orchestrator-bound inputs at the start of the run. Pull from `stage0_branch_trace.json` `lines[]` where the bindings are first set.

- (one bullet per bound input, with binding name and value)

---

## 3. Stage-by-stage narrative

Repeat this section once per stage that actually executed. Use the stage number from `_hydration.json`. For each stage:

### Stage `<N>` — `<stage_name>`

- **KLang version at run time:** `<klang_hash>` (comparability: `current` / `near-current` / `supplementary`)
- **Branches taken:** `<branch IDs>` — list, with the literal KLang predicate that fired for each
- **Branches skipped:** `<branch IDs>` — only those needed for coverage comparison
- **Key produced values:** the bindings the SOP author cares about. Examples: extracted fields, decision inputs, classification outputs.
  - `<binding name>`: `<value or summary>`
- **Iterations** (if a loop ran): one sub-bullet per iteration with iteration token and key outcomes
- **Sub-automation invocations:** (if any) → "see Stage `<M>`"

If a stage is `supplementary` (KLang diverges in load-bearing ways), note the divergence here and do **not** treat the trace as a parity reference downstream.

---

## 4. Final handoff payload

Per the pipeline's downstream boundary (`<DOWNSTREAM_BOUNDARY_NAME>`, e.g. `Update the Case`). Full field list with values.

```json
{
  "caseNumber": "",
  "status": "",
  "escalation": "",
  "usecase": "",
  "usecaseNumber": ""
}
```

(Match the actual handoff signature for this pipeline — fields above are illustrative.)

---

## 5. Files and large values

Anything the SOP author needs to open. Link each item to its on-disk path inside this run folder.

| Item | Path | Origin |
|---|---|---|
| Input file binary | `attachment.<ext>` | Phase C step 6.3 sub-A |
| Sub-stage input (if distinct) | `stage<N>_input.<ext>` | Phase C step 6.3 sub-B |
| Large JSON value (resolved) | `stage<N>_<lineId_first8>_<binding>.json` | Phase C step 6.3 sub-C |
| Full TABLE CSV | `stage<N>_<lineId_first8>_<binding>.csv` | Phase C step 2 (inline save) |

---

## 6. Parity check (filled later, during Phase 2-3)

Comparison of V1 (this captured run) vs V2 (new SPy execution against the same input).

| Stage | V1 Value | V2 Value | Match |
|---|---|---|---|
| | | | |

---

## 7. Summary

- **Final outcome:** `<succeeded / escalated / errored>`
- **Anomalies / unexpected behavior:** `<list>`
- **Open questions observable from this run:** `<list>` (move to `sop_open_questions.md` if SOP-relevant)
- **Follow-up actions:** `<list>`
