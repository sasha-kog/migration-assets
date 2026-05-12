# Migration Template: Combined Step 2 (SOP) + Step 3 (SPy Iteration)

Use this combined template when you want one execution for SOP drafting followed by SPy iteration, with a hard gate between phases.

## Fill These Placeholders First

- `<AUTOMATION_NAME>` — the orchestrator's published name
- `<STAGES>` — ordered list of every automation in the pipeline. Stage 0 is the orchestrator; subsequent stages are the children it invokes (and recursively, anything those invoke). One row per stage:

  | Stage | Automation Name | KLang path | Current published version label |
  |-------|-----------------|------------|----------------------------------|
  | 0 | `<orchestrator name>` | `<klang_path>` | `<label, e.g. "Apr 2026">` |
  | 1 | `<child name>` | `<klang_path>` | `<label>` |
  | 2 | … | … | … |

- `<RUN_CAPTURES_GLOB>` (for example: `plunkett/<automation_slug>/run_captures/**`)
- `<OUTPUT_BASE_DIR>` (for example: `plunkett/<automation_slug>/`)
- `<DOWNSTREAM_BOUNDARY_NAME>` — the boundary the pipeline hands off to (for example: `Update the Case`). Anything past this is out of scope.
- `<HANDOFF_FIELDS>` — list expected payload keys at the boundary

## Objective

Phase A:
- Draft per-stage SOP and unified branch matrix from captured run evidence.

Phase B:
- Iterate SPy against branch matrix using real execution checks, with **per-stage parity testing** against captured branch traces.

Do not start Phase B until Phase A gate passes.

## Inputs

The Phase 1 (data collection) step produces these. Phase 2-3 consumes them as-is.

- KLang per stage (from `<STAGES>` table above).
- Run captures (one folder per representative production run):
  - `<RUN_CAPTURES_GLOB>/run_capture_filled.md`
  - `<RUN_CAPTURES_GLOB>/run_capture.json` ← contains the `stages[]` array (schema below)
  - `<RUN_CAPTURES_GLOB>/attachment.<ext>` ← input file binary, replayed in Phase B
  - `<RUN_CAPTURES_GLOB>/stage<N>_branch_trace.json` ← per-stage condition-line trace
- Aggregated capture index:
  - `<OUTPUT_BASE_DIR>/run_captures/_capture_index.json`
- KLang version evolution doc (when versions diverge across the sample):
  - `<OUTPUT_BASE_DIR>/run_captures/_klang_version_evolution.md`
- Orchestrator runs index:
  - `<OUTPUT_BASE_DIR>/run_captures/_orchestrator_runs_index.json`

If any of those are missing for the runs referenced in your branch matrix, **stop and return to Phase 1** — don't try to backfill mid-Phase B.

---

## Schema: per-(captured-run, stage) record

### `run_capture.json` — `stages[]` array

Phase 1 writes one entry per stage that actually executed for that run. Schema:

```json
{
  "run_metadata": {
    "orchestrator_run_id": "...",
    "case_number": "...",
    "orchestrator_run_timestamp": "..."
  },
  "input_file": "attachment.pdf",
  "stages": [
    {
      "stage_number": 0,
      "stage_name": "create a credit memo netsuite",
      "automation_id": "biqqh3m20sqo1ri84ne0m2ayw",
      "klang_version_at_run_time": "v0-stable",
      "klang_version_current": "v0-stable",
      "comparability": "current",
      "comparability_reason": "Orchestrator KLang has not evolved across the sample window",
      "trace_captured": false,
      "trace_path": null,
      "branches_exercised": []
    },
    {
      "stage_number": 1,
      "stage_name": "to extract data from document",
      "automation_id": "...",
      "klang_version_at_run_time": "Nov2025-schema",
      "klang_version_current": "Apr2026-schema",
      "comparability": "supplementary",
      "comparability_reason": "Output schema diverges from current (Department/apply credit instead of document-type/Total Amt)",
      "trace_captured": false,
      "trace_path": null,
      "branches_exercised": ["S1C", "V-Woolworths"]
    },
    {
      "stage_number": 2,
      "stage_name": "to create credit memo and update",
      "automation_id": "...",
      "klang_version_at_run_time": "V1",
      "klang_version_current": "V4",
      "comparability": "supplementary",
      "comparability_reason": "V1 B10b sets status='close'; V4 sets 'reassign'. V1 B11 inverted condition fires for non-Woolworths; V4 dead-codes B11 for the same input.",
      "trace_captured": true,
      "trace_path": "stage2_branch_trace.json",
      "branches_exercised": ["B1b", "B2b", "B4a", "B5a", "B7a", "B10b-V1", "B11-fired-V1"]
    }
  ]
}
```

**`comparability` is a controlled vocabulary, three values:**

| Value | Meaning | Phase B usage |
|-------|---------|---------------|
| `current` | This stage's KLang at run time matches the current published version. Trace is a safe parity reference. | **Use as ground truth in Phase B parity checks.** |
| `near-current` | KLang differs only in non-load-bearing ways for this run's specific input (e.g., a flipped condition that nonetheless produces identical end-state). Document caveats. | **Usable as parity reference with the caveat noted in `comparability_reason`.** Phase B should still diff trace lines but tolerate the documented divergence. |
| `supplementary` | KLang diverges in load-bearing ways for this run's input. Output and trace differ from what current KLang would produce. | **NOT a parity reference.** Use only for partial evidence — e.g., vendor classification examples for Stage 1 even if Stage 2's trace is unusable. |

### `run_captures/_capture_index.json` — aggregated derived view

Phase 1 writes this after all captures land. Phase 2-3 reads it to answer "which captures cover which branches at parity-quality?" without re-walking every folder.

```json
{
  "stages": {
    "0": {"name": "create a credit memo netsuite", "current_version_label": "v0-stable"},
    "1": {"name": "to extract data from document", "current_version_label": "Apr2026-schema"},
    "2": {"name": "to create credit memo and update", "current_version_label": "V4"}
  },
  "captures": [
    {
      "run_id": "11b2n4e8wmdqzcuiqgkpwopf5",
      "folder": "2026-04-07_14-54_11b2n4e8wmdqzcuiqgkpwopf5",
      "case_number": "56377",
      "input_file": "attachment.pdf",
      "stages_comparability": {"0": "current", "1": "current", "2": "current"},
      "branches_exercised_per_stage": {
        "1": ["S1A", "V-Woolworths"],
        "2": ["B1b", "B2b", "B3b", "B4b-ii", "B5b-ii", "B7a", "B9a", "B10a", "B11-blocked", "B12"]
      }
    },
    {
      "run_id": "32dhcuw3f7z3oa2zpd8kd10kk",
      "folder": "2026-01-24_22-32_32dhcuw3f7z3oa2zpd8kd10kk",
      "case_number": "50899",
      "input_file": "attachment.xlsx",
      "stages_comparability": {"0": "current", "1": "current", "2": "near-current"},
      "stages_comparability_reasons": {"2": "B11 condition direction flipped (V3 inverted vs V4 positive); same end-state for this Metcash input"},
      "branches_exercised_per_stage": {
        "1": ["S1B", "V-Metcash"],
        "2": ["B1b", "B2b", "B3a", "B4b-ii", "B5b-ii", "B7a", "B9b", "B10a", "B11-blocked", "B12"]
      }
    },
    {
      "run_id": "48d47uhdu6vyfneu37g1eshs5",
      "folder": "2025-11-10_20-59_48d47uhdu6vyfneu37g1eshs5",
      "case_number": "46179",
      "input_file": "attachment.csv",
      "stages_comparability": {"0": "current", "1": "supplementary", "2": "supplementary"},
      "stages_comparability_reasons": {
        "1": "V1 schema (Department/apply credit instead of document-type/Total Amt)",
        "2": "V1 KLang differs in load-bearing ways: status=close, B11 fires for non-Woolworths"
      },
      "branches_exercised_per_stage": {"1": ["S1C", "V-Woolworths"]}
    }
  ],
  "branch_coverage_per_stage": {
    "1": {
      "S1A": {"current": ["2026-04-07_14-54_..."], "near-current": [], "supplementary": ["2026-02-14_..."]},
      "S1B": {"current": ["2026-03-27_..."], "near-current": ["2026-01-24_..."], "supplementary": []},
      "S1C": {"current": [], "near-current": [], "supplementary": ["2025-11-10_..."]}
    },
    "2": {
      "B1a": {"current": ["2026-03-27_..."], "near-current": [], "supplementary": ["2025-11-20_..."]},
      "B3a": {"current": [], "near-current": ["2026-01-24_..."], "supplementary": []},
      "B7a": {"current": ["2026-04-07_..."], "near-current": ["2026-01-24_..."], "supplementary": ["2025-12-15_..."]},
      "B9b": {"current": [], "near-current": ["2026-01-24_..."], "supplementary": []},
      "..."
    }
  }
}
```

### Example consumption

**Phase A — branch matrix gating.** For each (stage, branch), check `branch_coverage_per_stage[stage][branch]`. If `current` ∪ `near-current` is empty, the branch has no parity-quality reference → mark in `sop_branch_matrix.md` as `accepted risk` (see Phase A step 4) and capture a justification in `sop_open_questions.md`. Example check (pseudo):

```python
for stage, branches in matrix.items():
    for branch in branches:
        cov = idx["branch_coverage_per_stage"][stage].get(branch, {})
        parity_runs = cov.get("current", []) + cov.get("near-current", [])
        if not parity_runs:
            risk_register.append((stage, branch, "no parity-quality run"))
```

**Phase B — parity test selection.** For each (stage, branch) being tested, pick the canonical reference run via:
1. Filter to runs with `stages_comparability[stage] == "current"`.
2. If none: filter to `near-current`. Note caveats from `stages_comparability_reasons[stage]` so the parity diff tolerates the documented divergence.
3. Replay using that run's `attachment.<ext>` against the new SPy.
4. Diff the SPy execution's branch trace against the captured `stage<N>_branch_trace.json`.
5. Diff the SPy's handoff payload against the captured run's recorded payload.

```python
# Phase B parity reference selection
def reference_run_for(stage, branch):
    cov = idx["branch_coverage_per_stage"][stage][branch]
    if cov["current"]: return cov["current"][0], "strict"
    if cov["near-current"]: return cov["near-current"][0], "tolerant"
    return None, None  # branch is accepted-risk; no parity test
```

---

## Phase A: SOP Drafting

Produce:

- `<OUTPUT_BASE_DIR>/sop_draft.md` — **organized per stage** (one section per row in the `<STAGES>` table), with the orchestrator's pipeline flow at the top.
- `<OUTPUT_BASE_DIR>/sop_branch_matrix.md` — every branch labeled with `(stage, branch_id)` and mapped to a captured run.
- `<OUTPUT_BASE_DIR>/sop_open_questions.md` — unresolved ambiguity, **plus** the accepted-risk register for branches with no parity-quality coverage.

Requirements:

1. Cover all major branches across **every stage** observed in run captures (not just the orchestrator).
2. Use explicit branch predicates (the literal KLang condition) and expected outcomes, per stage.
3. Define handoff contract at `<DOWNSTREAM_BOUNDARY_NAME>` and document expected `<HANDOFF_FIELDS>` shape.
4. For each branch in `sop_branch_matrix.md`, include a `coverage_quality` column with one of: `parity` (≥1 `current` capture), `parity-tolerant` (only `near-current`), `accepted-risk` (only `supplementary` or none). Pull these values from `_capture_index.json`'s `branch_coverage_per_stage`.
5. Read `_klang_version_evolution.md` and reflect each version's load-bearing differences in the SOP — especially when a `supplementary` capture was the only evidence for a vendor route or file-type branch.

## Gate (Required)

Before Phase B, verify:

1. `sop_draft.md` exists and contains a per-stage branch decision section for each row in `<STAGES>`.
2. `sop_branch_matrix.md` maps each major branch to at least one captured run, **with `coverage_quality` recorded**.
3. **Every branch with `coverage_quality == "parity"` or `"parity-tolerant"` has a referenced run folder containing `attachment.<ext>` AND a `stage<N>_branch_trace.json` for the stage being tested.** (Without those two files, Phase B can't run a parity check.)
4. Branches with `coverage_quality == "accepted-risk"` are explicitly listed in `sop_open_questions.md` with stakeholder approval (or reason to defer).

If gate fails:

- stop,
- write blockers to `<OUTPUT_BASE_DIR>/open_gaps.md`,
- do not start SPy iteration. The fix path is "go back to Phase 1 and capture more runs," NOT "improvise SPy from supplementary evidence."

## Phase B: SPy Authoring + Iteration

Produce per stage (each stage gets its own SPy candidate):

- `<OUTPUT_BASE_DIR>/spy_iterations/stage<N>/spy_candidate_v1.txt`
- `<OUTPUT_BASE_DIR>/spy_iterations/stage<N>/spy_candidate_v2.txt` (if needed)
- `<OUTPUT_BASE_DIR>/iteration_results.md` — one section per stage
- `<OUTPUT_BASE_DIR>/handoff_payload_checks.md`

### Iteration loop per (stage, branch)

1. **Select reference run** via the algorithm above (`current` preferred, `near-current` tolerated). If none: this branch is in the accepted-risk register; skip parity test, write a synthesized minimal-input test fixture instead.
2. **Replay the input.** Use the reference run's `attachment.<ext>` as the SPy invocation input — do not synthesize new inputs unless the branch is accepted-risk.
3. **Execute the SPy candidate** in the test environment.
4. **Collect run evidence** for this stage's execution: branch trace, handoff payload.
5. **Diff against the reference:**
   - Branch trace diff: line-by-line vs `stage<N>_branch_trace.json`. For `near-current` references, allow the divergences listed in `stages_comparability_reasons[stage]`.
   - Handoff payload diff: vs the reference run's recorded payload values (case_number, status, escalation, usecase, usecaseNumber, etc.).
6. **Apply minimal fix** — change one thing per iteration so failures point at root cause.
7. **Re-run.**

### Validation Rules

- Real execution evidence is required; static trace-only analysis is not enough.
- Per-stage parity is required: a (stage, branch) is "passing" only when its branch trace matches the reference (within tolerated divergences) AND the handoff payload matches.
- Explicitly validate handoff payload keys at the pipeline boundary: `<HANDOFF_FIELDS>`.
- Treat `<DOWNSTREAM_BOUNDARY_NAME>` as boundary unless explicitly in scope.
- For `accepted-risk` branches, the synthesized test fixture must drive the branch and the SPy must produce a self-consistent end-state — but no production-trace diff is possible.

## Safety Rules

- No destructive cleanup without explicit ownership proof.
- Fail closed on ambiguous ownership.
- Never demote a `supplementary` capture to `near-current` to make a branch "covered." If parity coverage is missing, the answer is more Phase 1 captures or formal accepted-risk sign-off — not relabeling.

## Success Criteria

Combined execution is complete when:

1. SOP artifacts are branch-complete **per stage**, with `coverage_quality` recorded for every branch.
2. SPy candidates per stage pass parity checks (strict or tolerant) for every `parity`/`parity-tolerant` branch.
3. Handoff payload checks pass for required fields at `<DOWNSTREAM_BOUNDARY_NAME>`.
4. `accepted-risk` branches have a synthesized smoke test that produces a self-consistent end-state.
5. Remaining blockers (if any) are documented in `open_gaps.md` with an explicit "Phase 1 backfill needed" or "stakeholder sign-off needed" classification.
