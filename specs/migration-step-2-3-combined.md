# Migration Template: Combined Step 2 (SOP) + Step 3 (SPy Iteration)

Use this combined template when you want one execution for SOP drafting followed by SPy iteration, with a hard gate between phases.

## Fill These Placeholders First

- `<AUTOMATION_NAME>` — the orchestrator's published name
- `<STAGES>` — ordered list of every automation in the pipeline. Stage 0 is the orchestrator; subsequent stages are the children it invokes (and recursively, anything those invoke). One row per stage:

  | Stage | Automation Name | KLang path | Current published version label |
  |-------|-----------------|------------|----------------------------------|
  | 0 | `<orchestrator name>` | `<source_path>` | `<label, e.g. "Apr 2026">` |
  | 1 | `<child name>` | `<source_path>` | `<label>` |
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

### Prerequisites

Phase B is **Nexus-only** — it does not require cluster-shell, direct DB access, or kubectl. All V2 interactions go through the Nexus MCP (`kognitos_create_automation`, `kognitos_manage_thread`, `kognitos_invoke_automation`, `kognitos_runs(get / list_events / get_run_outputs)`, `kognitos_inspect_exceptions(get / list_events / get_guide)`).

**Required Nexus version:** the fixes from [kognitos/nexus#35](https://github.com/kognitos/nexus/pull/35) must be live in the cluster you're targeting (specifically: `list_events` pagination, `get_run_outputs` payload shape, and `inspect_exceptions(list_events)` ordering). Without those, the diff path and exception path return incomplete data and the iteration loop will appear to converge on a partial trace. Confirm your Nexus client/cluster is at or past that commit before starting Phase B.

**Environment portability:** Phase B is designed to be run against any cluster the Nexus MCP can reach — dev, staging, prod, or a customer-org workspace. There is no V2-side spec dependency on the cluster being dev specifically. SE-driven iteration directly against a customer's production workspace is the intended end state once Nexus is healthy.

(Phase A — SOP drafting — has no platform dependency at all; it reads only Phase 1 outputs on disk. SEs can complete Phase A offline today regardless of Nexus state.)

### Phase B Preflight — Book Capability Check

Before iteration #1, verify the target workspace has the books and procedures the captured V1 KLang implies. Hard-block when a required book is not installed; soft-surface (batched, one round of SE confirmation) when an installed book is present but procedure coverage is ambiguous. Lines that do not need a book — pure control flow, arithmetic, string operations — are excluded from the inventory entirely.

Reference for KLang → candidate-book classification: `books.md` (digest of the 64 installed integrations, with KLang-pattern → candidate-book mappings).

#### Procedure

Per stage in the `<STAGES>` table:

1. **Walk the stage's KLang** at `klang/stage<N>_<slug>.txt` line by line. Skip lines that are clearly book-free (`if … then`, loops, comparisons, arithmetic, string assignment, control flow).
2. **For each non-skipped line, classify the intent** using `books.md`:
   - `explicit_book_clause` — `from <book>`, `in <book>`, `to <book>`. The book name is verbatim in the KLang.
   - `document_capability` — extract/classify/analyze/read/split/merge over a document. Default candidate: **IDP**.
   - `ui_capability` — visible browser interaction. Candidates: **Browser**, **Browser Use**.
   - `saas_capability` — named-service verb whose book is unambiguous (e.g. NetSuite, Gmail).
   - `llm_only` — free-form Koncierge over plain values, no document. Candidates: **Anthropic / OpenAI / Gemini** OR pure SPy with inline Koncierge. Do not pick.
3. **Resolve candidates against the workspace**:
   - `kognitos_books(list, workspace=<target>)` → installed books.
   - For each requirement, intersect candidate_books with installed_books → `installed_books` field.
   - For each installed candidate, `kognitos_books(search_procedures, book=<X>, query=<intent_description>)` → `matched_procedures` field.
4. **Assign a per-requirement resolution**:
   - `satisfied` — at least one installed candidate has a high-confidence procedure match.
   - `needs_confirmation` — installed book(s) found but the procedure match is weak or ambiguous (multiple plausible candidates from the LLM-only case, Excel vs Microsoft Excel, etc.). Write a verbatim `confirmation_question` for the SE.
   - `missing` — no candidate book is installed in the workspace.
5. **Write `<OUTPUT_BASE_DIR>/workspace_book_inventory.json`** per the schema (`schemas/workspace_book_inventory.schema.json`). Validate with `tools/validate.py`.

#### Gate behavior

- `overall_status == "satisfied"` → proceed to Phase B iteration.
- `overall_status == "needs_confirmation"` → **batch** all soft surfaces into one consolidated message to the SE (one round, all pending confirmations at once). When the SE responds, update each requirement's resolution and re-evaluate `overall_status`. Then proceed.
- `overall_status == "blocked"` → emit `migration_outcome.json` with `book_missing_procedure` terminal state, populated `blockers` array. STOP. Do not proceed to iteration.

#### Why this gate is non-trivial

The KLang line that needs a book is rarely as obvious as `from netsuite`. The hardest cases:

- **Implicit IDP**: `extract the line items from the invoice` doesn't mention IDP, but it needs IDP's `Extract data from a thing` or `Extract table from a thing`.
- **Koncierge ambiguity**: an `ask the LLM what category this is` block could route to Anthropic/OpenAI/Gemini or be implemented inline in SPy. The preflight surfaces this as `needs_confirmation` because picking the wrong one will waste iterations downstream.
- **Browser-vs-SaaS**: when the V1 KLang walks a UI for a service the workspace has a real SaaS book for (e.g. browsing NetSuite when the NetSuite book is installed), the migration may prefer the SaaS book — but that's a Phase B iteration decision, not a preflight one. The preflight records both candidates; the SE decides.

#### What the preflight does NOT do

- **Does not** verify procedure inputs/outputs match the V1 line's payload shape — that's the iteration loop's job (the new book-contract check, when in scope).
- **Does not** decide between candidate books for the SE; ambiguous cases are surfaced verbatim.
- **Does not** install or authorize books. Those are SE actions outside the agent's authority.

---

Produce per stage (each stage gets its own SPy candidate):

- `<OUTPUT_BASE_DIR>/spy_iterations/stage<N>/spy_candidate_v1.txt`
- `<OUTPUT_BASE_DIR>/spy_iterations/stage<N>/spy_candidate_v2.txt` (if needed)
- `<OUTPUT_BASE_DIR>/spy_iterations/stage<N>/plan_v<N>.md` — one per Quill plan (D)
- `<OUTPUT_BASE_DIR>/spy_iterations/stage<N>/iteration_<N>_diff.json` — diff per iteration (A; inline-computed today, via `tools/replay_diff.py` once available)
- `<OUTPUT_BASE_DIR>/iteration_results.md` — one section per stage
- `<OUTPUT_BASE_DIR>/handoff_payload_checks.md`

### Two patterns this phase uses on every Quill interaction

Both patterns scope and bound what Quill does. Apply them at initial authoring AND at every fix iteration — not just when things go wrong.

#### Pattern 1 — Plan-first Quill (always two-turn)

Never ask Quill to write SPy in one shot. Always:

- **Turn 1 — request a plan, not code.** Send the SOP context (and, for fixes, the current SPy + fix-context). Quill returns an **implementation plan as plain text**: inputs/bindings, per-branch decision logic with verbatim KLang predicates, sub-process invocations + payload shapes, downstream handoff. Save to `spy_iterations/stage<N>/plan_v<N>.md`.
- **Turn 1.5 — orchestrator validates the plan.** Checks:
  - Does it cover every branch in `sop_branch_matrix.md` (or every divergence in the fix-context)?
  - Are predicates verbatim from KLang text?
  - Does the handoff payload match the captured contract?
  - Are decisions scoped (no over-broad changes that touch unrelated branches)?
  - If gaps: send back specific objections, request a plan revision. Loop here until the plan is sound.
- **Turn 2 — only after the plan passes, ask Quill to implement.** Prompt: "Plan approved. Implement this plan exactly. No new design decisions." Save SPy to `spy_iterations/stage<N>/spy_candidate_v<N>.txt`.

Why two turns: a bad plan is cheap to fix in text; a bad SPy candidate costs a full run-and-diff to find. Catching mis-direction at the plan stage compounds across iterations.

#### Pattern 2 — Fix-context comes from one of two sources (never invented)

When the orchestrator constructs a fix prompt, the fix-context attached to it must come from real run evidence:

- **Done with divergence (silent failure):** the structured diff between the V1 captured trace and the V2 run's exec data (see "Diff path" below).
- **Exception (loud failure):** the exception's resolution thread + line + guide via Nexus (see "Exception path" below).

If neither applies (the run passed parity), the iteration is complete; do not prompt Quill again.

### Initial SPy authoring per stage (uses Pattern 1)

Before any iteration:

1. Assemble the planning prompt for stage `<N>`:
   - SOP section for this stage (`sop_draft.md` → stage `<N>` block)
   - Branch matrix subset for this stage (`sop_branch_matrix.md` filtered)
   - Inputs the SPy will receive at runtime (orchestrator metadata + sub-stage handoff signature)
   - Downstream contract (what `<DOWNSTREAM_BOUNDARY_NAME>` expects)
2. Send to Quill with the **plan-first prompt** (Pattern 1, Turn 1).
3. Validate the plan (Pattern 1, Turn 1.5). Save approved plan as `plan_v1.md`.
4. Send the implement prompt (Pattern 1, Turn 2). Save SPy as `spy_candidate_v1.txt`.

Now enter the iteration loop.

### Iteration loop per (stage, branch)

1. **Select reference run** via the algorithm in "Schema: per-(captured-run, stage) record" (`current` preferred, `near-current` tolerated). If none: this branch is in the accepted-risk register; skip parity test, write a synthesized minimal-input test fixture instead.
2. **Invoke the V2 SPy candidate.** `kognitos_invoke_automation(automation=<v2_draft>, input=<reference_run.attachment>)`. Capture the resulting `run_id`.
3. **Poll status.** `kognitos_runs(get, run_id)` until status transitions to a terminal state (`done`, `failed`, `waiting_for_user_input`, `user stopped`).
4. **Branch on outcome:**
   - status == `done` → **Diff path** (below). The SPy completed; check whether it matches the reference.
   - status in {`failed`, `waiting_for_user_input`} with an exception → **Exception path** (below).
   - status == `user stopped` → not a SPy failure; surface and re-run.
5. **If diff is empty AND no exception:** this (stage, branch) PASSES parity. Record in `iteration_results.md`, move on to the next branch.
6. **Otherwise:** assemble fix-context. Diff JSON from the diff path, OR exception bundle from the exception path. Construct the fix prompt (template below) and send to Quill with Pattern 1 (plan first, validate, then implement). Save the new plan as `plan_v<N+1>.md` and the new SPy as `spy_candidate_v<N+1>.txt`.
7. **Re-run** (back to step 2). One change per iteration: don't bundle multiple fixes into one Quill turn — the diff at the next iteration should localize each fix's effect.

### Diff path — run status `done`

Goal: produce a structured diff comparing V2's execution to V1's captured trace.

**Asymmetry to internalize:**

- V1 runs live on the legacy `app.kognitos.com` tenant. Nexus does NOT reach that tenant. V1 data is what Phase 1 captured via GraphQL `getSentenceExecutionData` and saved to `stage<N>_branch_trace.json`.
- V2 runs live on the dev cluster. Nexus DOES reach the dev cluster. V2 data must be fetched via Nexus — there is no GraphQL fallback for V2.
- **V2 has no KLang and no lineIds.** V2 is SPy + a generated SOP; the runtime emits Nexus events keyed by SPy statement, not by KLang sentence. V1's lineId space (the `v2_<klang_hash>_<line_hash>_<idx>` ids from `getSentenceExecutionData`) does not exist on the V2 side at all. **There is no shared identifier between a V1 sentence and a V2 SPy statement.** Align V1 and V2 only by semantic anchors: **predicate text + binding name + SOP branch label** (which branch in the SOP each predicate belongs to).

Inputs:
- V1 reference: `run_captures/<folder>/stage<N>_branch_trace.json` + recorded handoff payload values in `run_capture.json`.
- V2 actual: the just-finished run's `run_id` (on dev cluster).

Procedure:

1. **Fetch V2's execution data via Nexus.** The relevant calls:
   - `kognitos_runs(get, run_id=<v2_run_id>)` — run metadata + final status.
   - `kognitos_runs(list_events, run_id=<v2_run_id>)` — event-by-event execution log. This is the source-of-truth for what V2 did, the analog of V1's `getSentenceExecutionData`.
   - `kognitos_runs(get_run_outputs, run_id=<v2_run_id>)` — final output bindings, including the handoff payload at the boundary.
2. **Normalize V1 and V2 onto a shared comparison schema.** V2 has no lineId-equivalent at all, so the comparison key is (predicate text OR binding name OR SOP branch label). Recommended in-memory shape for each side:

   ```json
   {
     "branch_decisions": [
       { "sop_branch": "B1a", "predicate_text": "if the file's extension is 'csv' then", "status": "Met" | "Not Met" }
     ],
     "named_bindings": [
       { "name": "customer", "value": "Woolworths" },
       { "name": "paymentAmt", "value": "1500.00" }
     ],
     "child_invocations": [
       { "name": "Update the Case", "payload": { "caseNumber": "...", "status": "close", ... } }
     ]
   }
   ```

   V1 is shaped this way by walking `stage<N>_branch_trace.json` and pulling the `if`/`else if` predicates + `produced` bindings + `subDocuments` invocations.

   V2 is shaped this way by walking the Nexus event list and applying the same extraction. Predicate text is the join key for branch decisions; binding name is the join key for produced values.

3. **Compute diff.** For each entry in V1 that has a counterpart in V2 (matched by predicate text or binding name):
   - **Predicate mismatch**: V1 says `Met`, V2 says `Not Met` (or vice versa).
   - **Value mismatch**: V1 binds `customer = "Woolworths"`, V2 binds `customer = "Woolworths Ltd"`.
   - **Extra V2 entries** (V2 took a branch V1 didn't): record as "extra path."
   - **Missing V2 entries** (V1 took a branch V2 didn't): record as "missing path."
   - For `near-current` references: drop divergences listed in `stages_comparability_reasons[stage]` from the diff before declaring non-empty.

4. **Compute handoff payload diff.** V2's final payload at the boundary (from `kognitos_runs(get_run_outputs)` or the relevant child-invocation payload in step 2 above) vs V1's recorded payload values.

5. **Write `spy_iterations/stage<N>/iteration_<N>_diff.json`** with this shape:

   ```json
   {
     "iteration": "<N>",
     "stage": "<N>",
     "branch": "<id>",
     "v1_reference_run": "<run_id>",
     "v2_run_id": "<run_id>",
     "trace_diff": {
       "predicate_mismatches": [
         { "sop_branch": "B1a", "predicate_text": "if … then",
           "v1_status": "Met", "v2_status": "Not Met" }
       ],
       "value_mismatches": [
         { "binding": "customer",
           "v1_value": "Woolworths", "v2_value": "Woolworths Ltd" }
       ],
       "extra_v2_branches": [ /* sop_branch labels */ ],
       "missing_v2_branches": [ /* sop_branch labels */ ]
     },
     "payload_diff": {
       "<field>": { "v1": "...", "v2": "..." }
     },
     "tolerated_divergences_dropped": [ /* near-current notes that were filtered out */ ]
   }
   ```

   If both `trace_diff` (after tolerance filtering) and `payload_diff` are empty: parity. Iteration is done for this branch.

6. **Today** the agent computes the diff inline (Python via a Bash tool call: load V1 JSON from disk, call Nexus `kognitos_runs(list_events)` to get V2 events, normalize both sides, compare). **Once `~/kognitos-migration-assets/tools/replay_diff.py` exists**, replace inline diff with one tool invocation — same output schema. The spec doesn't require the tool yet; it requires the diff JSON to have the shape above.

### Exception path — run status `failed` or `waiting_for_user_input`

When a V2 run errors out or pauses on an exception, the Kognitos platform's resolution agent reasons about it and stores that reasoning in the exception thread. Hijack it as fix-context.

Procedure:

1. `kognitos_runs(list_events, run_id=<v2_run_id>)` → walk events to find the exception event; grab `exception_id`.
2. `kognitos_inspect_exceptions(get, exception_id)` → exception text + the line that triggered it.
3. `kognitos_inspect_exceptions(list_events, exception_id)` → the **resolution thread**: every message the resolution agent and any prior reviewers exchanged. This is the Kognitos-native chain-of-thought trace.
4. `kognitos_inspect_exceptions(get_guide, exception_id)` → troubleshooting guide for this exception type (if one exists; may return empty).
5. Write the bundle to `spy_iterations/stage<N>/iteration_<N>_exception.json`:

   ```json
   {
     "iteration": "<N>",
     "stage": "<N>",
     "branch": "<id>",
     "v2_run_id": "<run_id>",
     "exception": {
       "id": "<exception_id>",
       "text": "...",
       "line": "..."
     },
     "resolution_thread": [
       { "author": "resolution_agent", "text": "..." }
     ],
     "guide": "<get_guide output or null>"
   }
   ```

**Read-only baseline (no reply):** if the exception bundle has enough context for Quill to write a fix, stop here, pass `iteration_<N>_exception.json` as fix-context, and skip the diagnostic-engagement step below. The Astral interaction is opt-in, not default.

### Astral diagnostic engagement (opt-in extension of the exception path)

When the read-only exception bundle is too thin to construct a useful Quill fix prompt — e.g., the resolution thread has only Astral's initial reasoning, the exception text doesn't pin down the root cause, or the diagnosis depends on context the agent hasn't surfaced — engage Astral conversationally to extract a better diagnosis. **The output is improved Quill fix-context, not a runtime patch.**

#### Background on Astral

Astral (Kognitos's exception resolution agent) responds to exceptions by reasoning about the failing SPy line and, when given enough context, writing a **runtime patch** that lets the current run continue. The patch is bound to the run; it does not edit the automation's SPy source. A patch is added to the workspace's troubleshooting guide ONLY when the user explicitly presses an "Add to troubleshooting guide" button in the UI — the MCP cannot perform that action. The MCP has no way to delete a guide entry; cleanup is UI-only.

The migration agent's goal is **diagnosis from Astral, permanent fix in SPy via Quill**. Never adopt Astral's runtime patch as the long-term answer.

#### Procedure

1. **Snapshot guides:** `kognitos_inspect_exceptions(list_guides, automation_id=<v2_draft>)` → record `guides_before` (id + signature for each). This is the drift baseline.
2. **Reply with diagnostic framing**, not a directive. Use `kognitos_reply_to_exception(automation_id, run_id, exception_id, message=<below>)`:

   ```
   I am migrating this automation from V1 to V2. The SPy line that just
   failed has a known V1 equivalent. In the V1 run captured for the same
   input:

     - the line was: <V1 KLang text for the corresponding statement>
     - the bindings produced were: <name=value, name=value, ...>
     - the branch decision was: <Met / Not Met for predicates>

   I do NOT want you to patch the run at runtime. I want to fix the V2
   SPy source so this exception never occurs again on subsequent runs.

   Please describe, in concrete terms:
     - what specifically in the current SPy at this line is wrong
       compared to the V1 behavior above,
     - what the SPy should say instead to produce the V1 binding/decision,
     - whether the fix is a value, a predicate, a binding name, or a
       structural change.

   Do not write a runtime patch and do not add anything to the
   troubleshooting guide.
   ```

3. **Poll** `kognitos_inspect_exceptions(list_events, exception_id)` for Astral's response. Concurrently poll `kognitos_runs(get, run_id)` to detect whether the run advanced (Astral applied a patch despite the diagnostic framing).
4. **Three observable outcomes:**
   - Astral responds with diagnosis text, run state unchanged → ideal. Harvest the diagnosis.
   - Astral responds with diagnosis text AND applies a patch (run state advances) → also fine. Harvest the diagnosis; treat the patch as additional context, not as the answer.
   - Astral responds with only a clarifying question → optional one more reply with the requested context. **Total cap: 3 round-trips per exception** including the first. Past 3, abort the engagement.
5. **Snapshot guides again:** `list_guides` → `guides_after`. Compute `drift = guides_after \ guides_before`.
   - If `drift` is empty → continue.
   - If `drift` is non-empty → write `<OUTPUT_BASE_DIR>/spy_iterations/stage<N>/iteration_<N>_astral_guide_drift.json` with the new guide id(s) + content, and **emit `migration_outcome.json` with terminal state `platform_bug` (subcategory: `astral_unexpected_guide_write`)**. Stop the iteration. The SE deletes the guide via the UI before resuming.
6. **Write the full Astral thread** to `<OUTPUT_BASE_DIR>/spy_iterations/stage<N>/iteration_<N>_astral_thread.json` with shape:

   ```json
   {
     "iteration": "<N>",
     "stage": "<N>",
     "branch": "<id>",
     "v2_run_id": "<run_id>",
     "exception_id": "<exception_id>",
     "turns": [
       { "author": "agent", "text": "<reply 1>" },
       { "author": "astral", "text": "<response 1>", "run_state_after": "waiting_for_user_input" },
       { "author": "agent", "text": "<reply 2>" },
       { "author": "astral", "text": "<response 2>", "run_state_after": "done" }
     ],
     "guides_before": [ /* snapshot */ ],
     "guides_after": [ /* snapshot */ ],
     "drift": [ /* guides_after \ guides_before */ ],
     "harvested_diagnosis": "<the most actionable text from Astral's responses, paraphrased only if necessary>"
   }
   ```

   This file is required for every Astral engagement. It is the calibration data set — the design of this section will be revised after the first 1–2 migrations produce real transcripts.

7. **Construct the Quill fix prompt** using `harvested_diagnosis` as part of the fix-context (alongside the original exception bundle and the V1 trace excerpt). Send to Quill via Pattern 1 (plan first → validate → implement).
8. **Mandatory verification re-run.** Invoke the new SPy candidate fresh against the same input. If the same exception fires again, the harvested diagnosis was wrong; **on retry, do NOT engage Astral again for this exception signature** — fall back to the read-only exception bundle as fix-context for Quill. Repeated Astral engagements on the same exception are not allowed within a single (stage, branch) iteration chain.

#### When to opt in vs stay read-only

| Situation | Default |
|---|---|
| Exception has a clear, attributable cause in the exception text (e.g. "field `X` is missing in payload, available fields are: …") | **Read-only.** Quill can fix from the bundle alone. |
| Resolution thread has only Astral's initial reasoning, no follow-up | **Engage** if iteration count > 1 (i.e., a prior Quill attempt already failed; the bundle wasn't enough). |
| Exception is a generic platform error (5xx, timeout) | **Read-only.** Astral can't diagnose what the platform itself broke. |
| Branch is `accepted-risk` (no V1 reference) | **Do not engage.** Without V1 ground truth to share, the diagnostic reply has no anchor. Use the exception bundle and SE escalation. |

#### Hard rules

- Never tell Astral to add anything to the troubleshooting guide.
- Never accept Astral's runtime patch as the final fix. The SPy source is the source of truth.
- 3-turn cap per exception. No exceptions to the cap until the calibration data justifies a change.
- One Astral engagement per `(stage, branch, exception_signature)` per iteration chain. If the same exception recurs after a Quill fix, the second attempt is read-only.
- If `list_guides` drifts, terminate the loop and surface to the SE. The MCP cannot clean up; manual UI deletion is the only path.

#### Calibration TODO (revise this section after migration #1)

After the first PO digitization migration completes, review every `iteration_<N>_astral_thread.json` and answer:

- Does Astral respect the diagnostic framing, or does it always patch regardless? (If always patches: simplify the reply template to be more directive, since softening doesn't help.)
- Is the harvested diagnosis usable as Quill fix-context, or does Quill consistently produce worse plans with it than without? (If worse: the engagement is net-negative; revert to read-only.)
- Did guide drift occur? On what kind of replies? (If yes: harden the language of the reply.)
- What was the average round-trip count? (Calibrate the cap.)

Track answers in `STEP_2_3_AUTONOMY_PROPOSAL.md` under proposal #2.

### Fix prompt template (used in iteration step 6)

Construct as a single Quill message with these sections, in order:

```
Goal: fix divergence in stage <N>, branch <id>, between V2 SPy candidate v<N> and V1 reference run.

Current SPy candidate (v<N>):
  <contents of spy_candidate_v<N>.txt>

V1 reference (captured production behavior):
  <link or excerpt from run_captures/.../stage<N>_branch_trace.json relevant to this branch>

What went wrong (PICK ONE):

[If diff path]
  Diff between V2 and V1 (iteration_<N>_diff.json):
    Predicate mismatches: ...
    Value mismatches: ...
    Extra V2 lines: ...
    Missing V2 lines: ...
    Payload diff: ...

[If exception path]
  V2 hit an exception at line <line>:
    Exception text: <text>
  How the Kognitos resolution agent reasoned about it:
    <resolution_thread formatted as turns>
  Troubleshooting guide (if any):
    <guide>

Constraints:
- Make the MINIMAL change to address the divergence above.
- Do NOT touch other branches.
- Preserve verbatim KLang predicates and binding names.
- If the fix changes the handoff payload shape, flag it explicitly.

DO NOT write the SPy yet. Draft an implementation plan first, as plain text.
```

After Quill returns the plan, validate (Pattern 1, Turn 1.5). On approval, the second-turn implement prompt is:

```
Plan approved. Implement this plan exactly in spy_candidate_v<N+1>.txt.
No new design decisions. If you discover the plan is incomplete, stop and ask.
```

### Validation Rules

- Real execution evidence is required; static trace-only analysis is not enough.
- Per-stage parity is required: a (stage, branch) is "passing" only when its trace diff (after tolerance filtering) AND payload diff are both empty.
- Explicitly validate handoff payload keys at the pipeline boundary: `<HANDOFF_FIELDS>`.
- Treat `<DOWNSTREAM_BOUNDARY_NAME>` as boundary unless explicitly in scope.
- For `accepted-risk` branches, the synthesized test fixture must drive the branch and the SPy must produce a self-consistent end-state — but no production-trace diff is possible.
- For `accepted-risk` branches, the SPy MUST implement the V1 logic verbatim (translated to SPy) AND include an explicit untested-branch marker (see "Stubbing unobserved branches" below). Do not omit the branch, simplify it, or replace it with a TODO.
- Every Quill interaction in this phase uses Pattern 1 (plan first, then implement). No exceptions.
- Fix-context attached to a Quill fix prompt comes from real run evidence — the diff JSON, the exception bundle, or (when opted in) a harvested Astral diagnosis. Never from the orchestrator's hypothesis about what *might* have gone wrong.
- Astral diagnostic engagement is opt-in per the "When to opt in vs stay read-only" table. The 3-turn cap and the guide-drift gate are hard limits. The MCP has no programmatic way to clean up a leaked guide entry; drift terminates the iteration and surfaces to the SE.

### Stubbing unobserved branches (accepted-risk)

When a branch has `coverage_quality == "accepted-risk"` (no `current` or `near-current` capture, and the Phase B.5 trigger-payload sweep also returned zero), the SPy must still implement the V1 logic — but with a clear marker so future SEs, customer reviewers, and the agent itself know this code has never been exercised.

The rationale: dead-code-looking branches sometimes turn out to be live (a trigger schema change, a new vendor, a edge case that finally occurs). Stripping them out makes the V2 a behavioral regression. Keeping them verbatim but marked makes the risk visible.

**Implementation requirement (in the SPy):**

1. Translate the V1 KLang for the branch to SPy, line-for-line. Preserve predicate text, binding names, and any sub-process invocations exactly. Do NOT simplify, refactor, or omit.
2. Add a leading SPy comment at the top of the branch's body:

   ```spy
   # UNTESTED BRANCH — accepted-risk
   # Source: V1 KLang for <stage_name>, predicate "<verbatim predicate>"
   # Reason: no representative run found in Step 1 (and Phase B.5 sweep returned zero)
   # Reviewer: <SE name>, <YYYY-MM-DD>
   ```

3. Add a single observable log/print at the start of the branch body so that the first time it fires in production, the team is alerted:

   ```spy
   log "UNTESTED BRANCH FIRING: <stage_name> / <branch_id> — review V1 parity before trusting output"
   ```

   The exact verb depends on which logging/observability book is installed in the target workspace; if none, fall back to a structured `the warning is "..."` binding the downstream pipeline can surface.

4. The branch does NOT enter the iteration loop's parity-check rotation (there's no V1 trace to diff against). It DOES get a synthesized minimal-input smoke test fixture (per the next validation rule) so that the SPy compiles and runs through that path at least once on dev.

**`sop_open_questions.md` entry required:** each accepted-risk branch must have an entry naming the SE who signed off, the customer contact who confirmed (if any), and the rationale. No silent acceptance.

**Migration completion does NOT require accepted-risk branches to be exercised in production.** It does require them to be implemented and marked. Acceptance criterion: a customer-review pass on the V2 SOP lists every untested branch alongside the parity-confirmed ones, with the same level of detail.

### Terminal states

The iteration loop exits in exactly one of these states for each (stage, branch). The agent **classifies the exit** and writes `<OUTPUT_BASE_DIR>/migration_outcome.json` (schema below) before returning to the SE. No third option, no ambiguous "we got tired" exit.

| Outcome | Trigger | What it means |
|---|---|---|
| `parity_reached` | Empty trace diff (after `near-current` tolerance) AND empty handoff-payload diff for every parity-quality branch in this stage | Stage is migration-complete. Proceed to SOP cleanup pass, then next stage. |
| `book_missing_procedure` | Quill's plan requires a verb/binding whose signature is not satisfied by any installed book in the target workspace | SE installs / authorizes the missing book OR escalates to platform. Migration paused for this branch. |
| `book_broken_procedure` | Same book-proc invocation fails the same way across **2 iterations** with no SPy change to that line; OR the proc's output deviates from its documented contract; OR throws an exception unrelated to its inputs | Not a SPy bug. File platform/book ticket with the evidence pointers; pause migration for this branch. |
| `spy_pattern_limitation` | After **5 iterations** on the same branch with diff shape *changing* but not *shrinking* (Quill is shuffling, not fixing) | Quill cannot express the required logic. Escalate to Quill team with minimal repro from `evidence`. |
| `v1_data_insufficient` | A branch executes that has no `current` or `near-current` capture in `_capture_index.json`, OR a parity-quality capture is found mid-loop to be insufficient (e.g. missing handoff field) | Return to Step 1 and capture more representative runs. Don't fabricate the trace. |
| `sop_ambiguity_unresolvable` | A branch requires a customer-input business decision (classification keywords, dead-end routing) and `sop_open_questions.md` has not been resolved by the SE | SE collects answer from customer; agent resumes. |
| `platform_bug` | Nexus or runtime returns a non-deterministic 5xx / unknown internal error not attributable to the SPy or any book contract | File platform ticket. Pause migration. |

### Classification rules in the loop

1. **After each iteration**, the agent attempts to classify the latest failure into one of the non-`parity_reached` categories. If it cannot classify (insufficient evidence), it runs **one additional diagnostic iteration** (e.g. a smaller-scope re-invoke, or a Nexus exception re-fetch) — then **must** force a classification. No third "I'm not sure" turn.
2. `book_broken_procedure` is sticky: once the same proc fails identically twice with no SPy delta on the failing line, classify and exit. Do not let Quill rewrite the line — it's not the problem.
3. `spy_pattern_limitation` requires explicit evidence that the diff is *moving but not shrinking*. If the diff is shrinking across iterations, keep iterating (this is a slow-converging fix, not a limitation).
4. `v1_data_insufficient` is normally caught by Phase A's gate. If it surfaces during Phase B, treat it as a Phase A failure and return.
5. `platform_bug` is the catch-all for "Nexus said something I cannot interpret." Do not loop on platform errors — one occurrence is enough to classify.
6. **Cross-branch implication.** If one branch terminates in `book_missing_procedure` / `book_broken_procedure` / `platform_bug`, continue iterating the other branches in this stage anyway — each branch terminates independently. Aggregate outcomes into `migration_outcome.json` at the end.

### `migration_outcome.json` schema

Written to `<OUTPUT_BASE_DIR>/migration_outcome.json` at the end of Phase B, regardless of outcome:

```json
{
  "automation": "<AUTOMATION_NAME>",
  "stages": [
    {
      "stage": 1,
      "branches": [
        {
          "branch": "B5a",
          "outcome": "book_missing_procedure",
          "iterations_completed": 4,
          "final_spy_path": "spy_iterations/stage1/spy_candidate_v4.txt",
          "evidence": {
            "v2_run_ids": ["run_abc...", "run_def..."],
            "quill_threads": ["thread_xyz..."],
            "exception_ids": ["exc_..."],
            "iteration_diffs": [
              "spy_iterations/stage1/iteration_1_diff.json",
              "spy_iterations/stage1/iteration_2_diff.json"
            ]
          },
          "blocker": {
            "category": "book_missing_procedure",
            "summary": "Quill plan requires `extract tables from <pdf>` but no installed book exposes a procedure matching that signature",
            "verb_signature": "extract tables from <pdf>",
            "books_checked": ["pdf_v3", "idp_v2"],
            "suggested_fix": "Install or extend a book that exposes table extraction from PDF"
          }
        },
        {
          "branch": "B5b",
          "outcome": "parity_reached",
          "iterations_completed": 2,
          "final_spy_path": "spy_iterations/stage1/spy_candidate_v6.txt"
        }
      ]
    }
  ],
  "overall_status": "blocked",
  "blocker_summary": [
    "stage 1 / B5a: book_missing_procedure (table extraction)",
    "stage 2 / B11: spy_pattern_limitation (nested conditional + loop scope)"
  ]
}
```

`overall_status` is `parity_reached` iff every branch is `parity_reached`. Otherwise `blocked`, and `blocker_summary` lists the structured blockers the SE needs to act on.

### Blocker payload — required fields per category

Each `blocker` object must include `category` + `summary`, plus the fields below:

- **`book_missing_procedure`** — `verb_signature` (the KLang-style call Quill tried to make), `books_checked` (which installed books were verified), `suggested_fix`.
- **`book_broken_procedure`** — `book_name`, `procedure_signature`, `expected_behavior` (from book docs), `observed_behavior`, `reproducer_run_id`.
- **`spy_pattern_limitation`** — `iterations_with_diff_shape` (list of how the diff changed across N iterations), `quill_thread_ids`, `minimal_repro_input_path`.
- **`v1_data_insufficient`** — `branch_with_no_capture`, `predicate_text`, `required_capture_quality` (`current` or `near-current`).
- **`sop_ambiguity_unresolvable`** — `open_question_ref` (which line of `sop_open_questions.md`), `customer_decision_required`.
- **`platform_bug`** — `nexus_tool` (which MCP call), `error_payload`, `run_id_or_context`, `reproducible` (boolean).

The point of these required fields is that an SE reading `migration_outcome.json` can act without re-running anything: install the book, file the ticket, ask the customer the question, or capture more V1 data. No "go re-read the spy_iterations folder" hunt.

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
5. **`migration_outcome.json` is written** with `overall_status: parity_reached` (success) OR `overall_status: blocked` with every blocked branch carrying a fully-populated structured `blocker` object per the schema above. There is no "partial success without classification" outcome.
