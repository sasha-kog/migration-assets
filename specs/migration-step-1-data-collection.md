# Migration Step 1: Data Collection (Branch-Aware) — API-first with UI fallback

Use this spec for any branching automation migration where run evidence must be collected before SOP/SPy work. The agent runs API-first; UI work happens inline for FILE binaries and `__large_value_*` resolution, and falls back to full editor-walking (Appendix A) only when the API is unreachable.

This file is the canonical Step 1 spec. The Phase 2-3 spec (sibling `migration-step-2-3-combined.md`) references this file's schemas by anchor.

---

## Inputs (just one — the rest are derived)

**Required:**
- `<PROCESS_PUBLISHED_URL>` — orchestrator's published-process URL, e.g. `https://app.kognitos.com/department/<DEPT_ID>/processes/<PROC_ID>?stage=PUBLISHED`

**Optional overrides (defaults shown):**
- `<OUTPUT_BASE_DIR>` — defaults to `<automation_slug>/` (e.g. `create_customer_payment/`). Override only if you want a different parent path.
- `<JWT>` — only needed for Phase B/C (exec-data fetches) and the rare KLang fallback. The agent self-fetches from the Playwright profile if possible; falls back to env var `KOGNITOS_JWT`; falls back to asking you to paste.

**Everything else is derived by Phase 0 (Hydration):** `<DEPARTMENT_ID>`, `<PROCEDURE_ID>`, `<AUTOMATION_NAME>`, orchestrator KLang text, every child automation's KLang text, list of stages.

## Prerequisites (one-time setup per machine)

Clone the shared migration assets repo:

```bash
git clone git@github.com:kognitos/migration-assets ~/kognitos-migration-assets
```

This contains the run-capture template and a canonical filled-capture example, both referenced by fixed path throughout this spec:

- `~/kognitos-migration-assets/run_capture_template.md`
- `~/kognitos-migration-assets/example_filled_capture/`

`git pull` in that directory before each migration to pick up updates. If the directory is missing at Phase 0 start, the agent prompts the user with the clone command and stops.

---

## Objective

Collect one high-quality run capture per major branch/case for `<AUTOMATION_NAME>`, including all sub-automations it invokes and the input file binaries each run consumed.

This step is data-only. Do not rewrite SPy yet.

**Done in one pass.** Don't ship Phase 1 until every run folder has filled markdown + JSON + the input file binary AND every observed sub-automation has a `stage<N>_branch_trace.json` whose KLang version matches current. A second backfill pass is expensive — design for completeness.

---

## Decision rules (READ FIRST)

The agent commits to a path before loading procedures. Re-check these rules only on a hard failure, and finish the current run before switching lanes.

### Use the API path (primary) unless any of:

- `<JWT>` returns 401 twice in a row after the user provides a fresh token.
- `api.app.kognitos.com` is unreachable (DNS / network).
- `ListWorkersByProcedure` returns zero usable runs for `<PROCEDURE_ID>`.

If any of those: switch to **Appendix A — UI fallback** for run discovery + KLang collection + per-run branch traces.

### UI work is REQUIRED even in API mode, in all cases, for:

- **FILE binaries** — signed S3 URLs are obtainable only by clicking the file element in the editor. Procedure: Phase C step 6.3 sub-A.
- **`__large_value_NNNN` JSON resolution** — when a downstream branch reads a concept whose `display_value` is `__large_value_*`. Procedure: Phase C step 6.3 sub-C. (TODO: identify the GraphQL op the value-badge popover hits; eliminates this UI step.)
- **SSO login** if the Playwright profile is logged out.

These are not fallback paths — they're always required in API mode, batched into one UI pass per run at the end of Phase C.

### Don't switch lanes mid-run

If you start a run in API mode and Phase C step N fails, finish what you can for the run, write `ui_capture_status: "failed"` with notes, and surface the blocker. Switching to UI fallback mid-run produces inconsistent traces that Phase 2-3 can't diff cleanly.

---

## Browser/Login Constraints

- Agent uses the Playwright MCP browser. The MCP profile is single-instance — if a stale Chrome from a prior session holds it, surface that as a blocker. Do **not** kill the PID without authorization.
- If `app.kognitos.com` requires SSO/manual login, pause and request manual login handoff via the MCP browser, then resume.
- A logged-in Playwright profile can supply the JWT itself: navigate to any run page, capture the next `graphql?op=…` request's `authorization` header. Falls back to user-pasted `<JWT>` if the profile isn't logged in.

---

## End-to-end process (the five phases)

The agent runs these in order. Each phase has a clear input and output.

| Phase | Input | Output | API/UI |
|---|---|---|---|
| **0** Hydration | `<PROCESS_PUBLISHED_URL>` | `_hydration.json`, `klang/stage<N>_<slug>.txt` per stage, derived `<OUTPUT_BASE_DIR>` | UI (Playwright copy-capture, primary) + API (fallback) |
| **A** Branch enumeration | KLang `.txt` per stage | `branch_catalog.{md,json}` | text only |
| **B** Run discovery + triage | `branch_catalog.json` + `<PROCEDURE_ID>` + `<DEPARTMENT_ID>` | `_orchestrator_runs_index.json`, `_branch_triage.json` | API (UI fallback in Appendix A.1) |
| **C** Per-run deep capture | shortlist from `_branch_triage.json` | per-run folder with all artifacts | API + one batched UI pass per run |
| **D** Aggregate | all per-run folders | `_capture_index.json`, optionally `_klang_version_evolution.md` | none |

### Phase 0 — Hydration (one URL → everything else)

**Goal:** Derive every other input from `<PROCESS_PUBLISHED_URL>` alone. By the end, the agent has KLang text for the orchestrator and every child procedure, plus a `_hydration.json` linking them.

**Primary path = Playwright copy-capture.** The editor is Slate.js; its `copy` event handler serializes the full document with `[md*]` references resolved inline and indentation as literal whitespace. We capture that. Verified against a 290-line automation (`create customer payment`): byte-identical to manual highlight + copy + paste, in fact one line MORE complete than manual paste (which silently truncated the last line).

**Fallback = GraphQL API** (`getWorkerDocument` + parent-chain render) when copy-capture fails. Same artifacts.

#### Step 0.1 — Parse URL

Regex: `/department/([^/]+)/processes/([^/?]+)`

Outputs: `department_id`, `procedure_id`.

#### Step 0.2 — Resolve assets path

Check that `~/kognitos-migration-assets/run_capture_template.md` exists. If missing, surface the clone command and stop.

#### Step 0.3 — Open the editor (with login)

Navigate Playwright to `<PROCESS_PUBLISHED_URL>`. If routed to `auth.app.kognitos.com`, surface SSO handoff to the user. After login, wait for `#slate-editor` to render (4-5s; or poll for known content like `########## ` or `if `).

Capture `document.title` — format is `"<automation name> | <department name> | Kognitos"`. Take everything before the first ` | ` → `<AUTOMATION_NAME>`.

`<automation_slug>` = lowercase, non-alphanumeric → `_`, collapse consecutive `_`. Example: `"create customer payment"` → `create_customer_payment`.

`<OUTPUT_BASE_DIR>` defaults to `<automation_slug>/` unless user-overridden.

#### Step 0.4 — Copy-capture the orchestrator KLang (PINNED procedure)

**Idempotency precheck (run BEFORE every stage's capture, including children in Step 0.5):**

Before navigating to the editor for a stage, check whether the output already exists from a prior partial run:

1. Compute the target path: `<OUTPUT_BASE_DIR>/klang/stage<N>_<slug>.txt` for KLang procedures or `<OUTPUT_BASE_DIR>/spy/stage<N>_<slug>.py` for SPy procedures (`<N>` = stage number, `<slug>` = slugified procedure name).
2. If the file exists, read it and run the **same sanity check** the spec applies after a fresh capture (see "Sanity checks before saving" further down):
   - length > 100 chars,
   - for KLang: contains `the ` or `if ` (KLang language signals); for SPy: contains `@procedure` or `def ` (Python signals),
   - no abrupt mid-token truncation.
3. If the sanity check passes:
   - **SKIP** the navigate + copy-capture work for this stage.
   - Use the existing file as input to downstream steps (child discovery in Step 0.5, runtime-block scan in Step 0.6).
   - When Step 0.9 builds `_hydration.json`, mark this stage as `"source_capture_method": "cached"` and set `source_path` to the existing file location.
4. If the file is missing OR the sanity check fails:
   - Proceed with the full capture procedure below.
   - On a subsequent rerun this stage will then be cached.

The same idempotency rule applies to the API fallback (Step 0.7) and user-paste fallback (Step 0.8): if a valid file already exists, those tiers don't re-run for that stage either. `_hydration.json` is always regenerated from current on-disk state — don't attempt to merge an old `_hydration.json` with new work.

**The listener install, selection, copy, AND read MUST run in ONE synchronous `browser_evaluate` call.** Splitting across calls is unreliable (verified empirically — same code works in one call, returns empty when split across two).

**Listener-registration-order fix (verified 2026-05-14 on `to perform PO digitization`):** on a cold page, registering only a document-level bubble listener returns empty intermittently because *our* listener fires before Slate's own handler writes `clipboardData`. The fix is to first attach a no-op listener on the editor element itself; this shifts Slate's document-level handler to fire before ours.

Pass the full block:

```js
() => {
  let result = null;

  // 1) Editor-level no-op listener.
  //    Registers BEFORE the document-level listener below. This is what
  //    forces Slate's doc-level copy handler to fire ahead of ours and
  //    write to clipboardData. Without this no-op, doc-level read often
  //    returns null on a cold page.
  const ed = document.querySelector('#slate-editor');
  ed.addEventListener('copy', () => { /* noop */ }, { capture: false });

  // 2) Document-level bubble listener — fires AFTER Slate writes.
  document.addEventListener('copy', (e) => {
    result = e.clipboardData.getData('text/plain');
  }, { capture: false });

  // 3) Select all editor content
  const range = document.createRange();
  range.selectNodeContents(ed);
  const sel = window.getSelection();
  sel.removeAllRanges();
  sel.addRange(range);

  // 4) Trigger copy (synchronously fires listeners in registration order)
  document.execCommand('copy');

  // 5) Return captured text in the same call
  return result;
}
```

**Critical details:**

- **Single synchronous block.** Two-call patterns (install listener in one eval, then copy in another) returned empty captures intermittently in testing. One call always worked.
- **Editor-level no-op THEN document-level reader.** The no-op is what makes registration order work — without it, on a fresh page our document-level reader runs before Slate's handler writes to `clipboardData` and we read empty.
- **Bubble phase (`{ capture: false }`) on both.** Capture phase reads empty because Slate writes to `clipboardData` in bubble phase. Verified via diagnostic listener: at capture phase `clipboardData.types = []`; at bubble phase `clipboardData.types = ["text/plain"]` with the full serialized KLang.
- **Slate calls `event.preventDefault()`** in its handler. That's fine — our listener still reads `clipboardData` regardless.

**Sanity checks before saving:**
- captured length > 100 chars
- contains either `the ` or `if ` (KLang language signals)
- contains no obvious truncation artifacts (e.g. abrupt end mid-token)

If any check fails: fall back to API (Step 0.7).

Save to `<OUTPUT_BASE_DIR>/klang/stage0_<automation_slug>.txt`.

#### Step 0.5 — Discover child procedures (TWO PASSES + editor classification — all required)

Two patterns exist for invoking a child procedure, and **the regex-only approach catches only one of them**. Additionally, child procedures can be authored in KLang (Slate editor) OR SPy (Python via CodeMirror editor). These need different treatment. Verified 2026-05-14 on `to perform PO digitization`: the orchestrator's KLang had zero `run @{...}` references but did invoke five children — two KLang and three SPy/Python. The original regex returned empty; even after adding Pass 2, treating every match as a KLang child stage caused SPy source to be captured into `klang/` and to be subjected to Phase A/B/C treatment that doesn't apply to Python code. Both passes plus the editor classification below are required.

##### Pass 1 — Static `run @{...}` regex

Some automations explicitly serialize sub-process invocations as:

```
run @{"type":"procedure","display":"<name>","value":"<id>"} with
  ...
```

Run this regex against the captured KLang text:

```
run @\{[^}]*"value":\s*"([a-z0-9]+)"
```

Capture group 1 = child procedure ID. Dedupe.

##### Pass 2 — Procedure-name match against the department registry

The newer / more common form is a bare KLang verb phrase that the platform resolves to a department-local procedure at runtime. The UI flags these with a purple badge; the API does **not** expose them as `run @{...}` references in the captured KLang text.

Procedure for this pass:

1. Call `listProcedureGroupsByDepartmentv2(departmentId=<DEPT_ID>)` via Apollo Client (see "Authentication" section for why Apollo, not curl/fetch). Collect every procedure's `name` and `id`, dedupe, sort **longest-name-first** to handle overlapping prefixes (e.g. `send response` vs `send a final output response`).
2. For each procedure name in the sorted list: scan the captured KLang text for occurrences. A line whose trimmed leading verb phrase matches a procedure name is a sub-process invocation of that procedure. Common forms to match:
   - `<procedure name> with` (followed by parameter block)
   - `<procedure name>` on its own line
   - `<procedure name> as follows` (parameter block follows)
3. Once matched, **don't re-match shorter procedure names against the same line** — longest-match-first wins. This is what handles the `send response` / `send a final output response` overlap.
4. Collect the procedure IDs of all matches. Union with Pass 1's results → `child_procedure_ids_static`.

##### For each discovered child ID (regardless of pass)

1. Compute child's editor URL: `https://app.kognitos.com/department/<DEPT_ID>/processes/<CHILD_PROC_ID>?stage=PUBLISHED`.
2. Navigate Playwright there. Session is reused — no second login.
3. **Detect editor type before capturing:**
   - If `#slate-editor` is present → KLang procedure.
   - Else if a CodeMirror element is present (`.cm-editor`, `.cm-content`, or similar) → SPy/Python procedure.
   - Else → unrecognized authoring surface. Warn and skip; record in `_hydration.json` under `warnings`.
4. **Capture according to type:**
   - **KLang:** repeat Step 0.4's copy-capture procedure. Save as `<OUTPUT_BASE_DIR>/klang/stage<N>_<child_slug>.txt`. Set `language: "klang"`, `source_path` to that file.
   - **SPy:** read the CodeMirror content via `browser_evaluate` (`document.querySelector('.cm-content').innerText` or equivalent). Save as `<OUTPUT_BASE_DIR>/spy/stage<N>_<child_slug>.py`. Set `language: "spy"`, `source_path` to that file. Do NOT save SPy to `klang/`.
5. **Recursion rule depends on language:**
   - **KLang stages:** apply BOTH discovery passes (regex + procedure-name match) to the captured KLang text; recurse on any newly-discovered procedure IDs.
   - **SPy stages:** treat as opaque source. Do NOT scan the Python for procedure-name matches against the department registry (Python imports and function calls are not the same as KLang verbs). Do NOT recurse from SPy stages.
6. `N` increments depth-first across both types.

Stop when the set of discovered procedure IDs stabilizes (no new IDs on the latest pass). Warn if recursion depth exceeds 5 — possible cycle or unexpectedly deep call graph.

##### How KLang and SPy stages diverge downstream

| Aspect | KLang stage | SPy stage |
|---|---|---|
| Source location | `klang/stage<N>_<slug>.txt` | `spy/stage<N>_<slug>.py` |
| `_hydration.json` `language` field | `"klang"` | `"spy"` |
| Phase A (branch catalog) | Required | **Skipped.** SPy procedures are treated as opaque code; their internal branches are not enumerated. |
| Phase B (run discovery) | Required if procedure has independent runs | Optional. SPy procedures rarely have independent runs — their I/O is observable at the parent's call site in the parent's `stage<M>_branch_trace.json`. |
| Phase C (per-run deep capture) | Required when chosen runs exist | **Skipped at the SPy stage level.** The SPy procedure's I/O for any given run is already in the parent KLang stage's trace at the line where SPy is invoked. |
| Step 2-3 migration treatment | Quill writes V2 SPy from the V1 KLang | The V1 SPy source is preserved verbatim into V2 (or a book substitute is chosen, per the workspace book-inventory preflight). |

#### Step 0.6 — Forward-signal runtime-only blocks to Phase C

Phase 0 has fully captured the KLang for **everything that has KLang text**. But two kinds of constructs have *additional runtime artifacts* that Phase C will need to fetch separately. Scan the captured KLang and forward-signal these to `_hydration.json` so Phase C knows to expect them. **No KLang fetching needed in Phase 0 for these** — their textual definition is already captured.

- **`miniPlaygrounds`** — `extract data from the document` and `extract a table from the document where` blocks. The parameters (`the first field is ...`, `the first field's rule is ...`) are already captured as child lines under the parent in the copy-capture output. What's missing is the worker's *runtime-generated document* (the actual prompt sent to Gemini + extraction results), which is addressable only by a `documentToken` that doesn't exist until a run executes. Phase C fetches that exec data; Phase 0 just notes the parent line.
- **Loop bodies** — `process each <item> as follows` blocks. The body's KLang lines are already in the orchestrator's editor copy. What's missing is the per-iteration exec data (5 iterations = 5 separate API calls scoped by `iterationToken`). Phase C fetches per iteration; Phase 0 just notes the loop's parent line.

Loop bodies are NOT separate stages (they reuse the parent stage's lineIds). MiniPlaygrounds become separate stages only at Phase C's trace-record level, not at the KLang-text level.

Write one entry per match into `_hydration.json` under `runtime_only_blocks`:

```json
"runtime_only_blocks": [
  { "kind": "miniPlayground", "parent_stage": 0,
    "parent_line_text": "extract data from the document",
    "phase_c_action": "fetch documentToken from getSentenceExecutionData; treat as new stage in trace records" },
  { "kind": "loop_body", "parent_stage": 0,
    "parent_line_text": "process each row as follows",
    "phase_c_action": "fetch per-iteration exec data via iterationToken; append to stage trace under iterations[<parent_lineId>]" }
]
```

#### Step 0.7 — API fallback (Tier 2, when Playwright copy-capture fails)

If the Step 0.4 sanity check fails for any stage (capture too short, missing KLang signals, etc.):

1. Resolve `<JWT>` — Playwright profile → env var `KOGNITOS_JWT` → ask user to paste.
2. `listProcedureGroupsByDepartmentv2({ departmentId: <DEPT_ID> })` once → catalog mapping every procedure ID → name + `latestRunData.id`.
3. For the failed stage: `getWorkerDocument(workerId=<latestRunData.id>, documentToken="")`.
4. Render the sentence list back to indented text by walking `parentId` chains (each level = 2 spaces). Embedded multi-line strings (e.g. `text` containing `\n`) reproduce verbatim.
5. Save to the same `stage<N>_<slug>.txt` path. Note `klang_source: "api_render"` in `_hydration.json` for that stage.

Edge cases that escalate to Step 0.8 (user paste):
- A child procedure exists in the catalog but `latestRunData` is null (never been run) — API can't fetch its KLang.
- `api.app.kognitos.com` is unreachable / 5xx.
- JWT refresh fails repeatedly.

#### Step 0.8 — User-paste fallback (Tier 3, when both Playwright and API fail)

When both Tier 1 (copy-capture) and Tier 2 (API render) fail for a stage, the agent prompts the user to paste KLang manually. This is the same workflow SEs used pre-automation, kept as a safety net.

Procedure:

1. Agent prints a clear prompt:
   ```
   ⚠️  Auto-capture failed for stage <N> ("<stage_name>").
       Tier 1 (Playwright): <reason — e.g. "Slate copy returned empty">
       Tier 2 (API): <reason — e.g. "no latestRunData for procedure id <id>">

   Please paste the KLang manually:
     1. Open: <child URL>
     2. Click into the editor, Cmd+A then Cmd+C
     3. Save the result to: <OUTPUT_BASE_DIR>/klang/stage<N>_<slug>.txt
     4. Reply "done" when complete.
   ```
2. Wait for the user's `done` confirmation (or timeout / abort).
3. Re-read the saved file. Sanity-check (same as Step 0.4: length > 100, contains KLang signals).
4. Note `klang_source: "user_paste"` in `_hydration.json` for that stage.
5. Continue Phase 0 from the next stage or recursion step.

The user-paste path produces text identical to what Tier 1 would produce (the user is using the same editor copy serializer). The only difference is the human in the loop.

#### Step 0.9 — Write `_hydration.json`

```json
{
  "hydrated_at": "2026-05-12T19:32:00Z",
  "input": { "process_published_url": "..." },
  "derived": {
    "department_id": "d6j8mv1c12a9n3itm7msneli4",
    "procedure_id": "8rroj6z8d6lrmgr0b44p4bebr",
    "automation_name": "create customer payment",
    "automation_slug": "create_customer_payment",
    "output_base_dir": "create_customer_payment/",
    "jwt_source": "playwright_profile|env|paste|none-yet"
  },
  "stages": [
    {
      "stage_number": 0,
      "procedure_id": "8rroj6z8d6lrmgr0b44p4bebr",
      "name": "create customer payment",
      "language": "klang",
      "source_path": "klang/stage0_create_customer_payment.txt",
      "source_capture_method": "copy_capture",
      "child_procedure_ids_static": ["6szk1unn9661xjtf9uhpflrja"],
      "discovered_via": "url"
    },
    {
      "stage_number": 1,
      "procedure_id": "6szk1unn9661xjtf9uhpflrja",
      "name": "Update the Case",
      "language": "klang",
      "source_path": "klang/stage1_update_the_case.txt",
      "source_capture_method": "copy_capture",
      "child_procedure_ids_static": [],
      "discovered_via": "klang_static_parse_from_stage_0"
    }
  ],
  "deferred_to_phase_c": [
    { "kind": "miniPlayground", "parent_stage": 0,
      "parent_line_text": "extract data from the document",
      "note": "Embedded extraction prompt; documentToken known only at runtime." }
  ],
  "warnings": [],
  "assets": {
    "run_capture_template_path": "~/kognitos-migration-assets/run_capture_template.md",
    "filled_capture_example_path": "~/kognitos-migration-assets/example_filled_capture/"
  }
}
```

Phases A-D consume `_hydration.json` and the `klang/*.txt` files — they do NOT re-fetch what Phase 0 has already produced.

#### Risks / known unknowns

- **Slate virtualization on very long automations** — verified clean at 11,775 px tall / 290 lines / 18,343 chars (orchestrator `create customer payment`). Also verified at 6,576 px / 166 lines / 10,846 chars (`to create a sales order`) and 2,515 px / 64 lines / 2,119 chars (`Update the Case`). All three had `scrollHeight === clientHeight` on `#slate-editor` (no internal scroll, fully rendered). Untested beyond ~12,000 px. Sanity check in Step 0.4 catches gross truncation; for borderline cases, the API fallback is the safety net.
- **Listener registration timing** — the listener and copy command MUST be in the same synchronous block (Step 0.4 noted). Empirically verified: two-call splits returned empty captures on `to create a sales order` while single-call worked.
- **UI changes to Slate copy handler** — if Kognitos changes the editor's serializer, copy-capture could regress silently. API fallback (Step 0.7) keeps us safe; the sanity check at Step 0.4 acts as a tripwire.
- **Login token expiry mid-Phase-0** — for a multi-child pipeline, the session might expire between captures. Detect by 401 or login redirect on `browser_navigate`; pause for re-auth, then resume.
- **Procedures with zero published runs** — only affects the API fallback path. Copy-capture works fine without runs.

#### Verified end-to-end on `create customer payment`

A full Phase 0 walk on this orchestrator produced (in this order):

1. `klang/stage0_create_customer_payment.txt` — 290 lines, 18,343 chars. Byte-identical to manual human copy-paste (`copy_pate_result.txt`) **except one line MORE complete** at the bottom (manual paste truncated `the usecaseNumber`).
2. Regex on stage 0 → 1 child: `6szk1unn9661xjtf9uhpflrja` (`Update the Case`).
3. Navigated, captured `klang/stage1_update_the_case.txt` — 64 lines, 2,119 chars. Regex on stage 1 → no more children. Recursion terminates.
4. Final `_hydration.json` lists 2 stages, 1 deferred miniPlayground (`extract data from the document`), 0 warnings.

Total time: <30 seconds after SSO login. Zero human interaction post-login.

### Phase A — Branch enumeration (KLang stages only — SPy stages skipped)

**SPy stages are excluded from Phase A.** Their Python source is captured in Step 0.5 and treated as opaque — internal `if/else` in Python is not enumerated as a branch matrix. The branch catalog covers only stages where `language == "klang"` in `_hydration.json`.



Read every KLang file. Enumerate decision predicates, branch groups, sub-branches, escalation/failure branches, and handoff branches (cross-automation invocations point to the next sub-automation to read). Build the branch matrix (file-type × vendor/customer × downstream-state, or whatever the pipeline factors on).

Write `branch_catalog.md` (human-readable) and `branch_catalog.json` (machine-readable):

```json
{
  "stages": {
    "0": {
      "name": "Netsuite Customer Payments / to create a sales order",
      "source_path": "<SOURCE_PATH>",
      "language": "klang",
      "branches": [
        {
          "label": "B1a", "predicate": "if the id's isInactive is \"false\" then",
          "decision_lineId_pattern": "...",
          "expected_outputs": ["the identifier"],
          "suspected_dead_code": false
        }
      ]
    }
  }
}
```

`decision_lineId_pattern` is an optional hint Phase B fills after fetching the orchestrator's worker doc once — it lets the agent map "this branch took this path" by inspecting the `if` line's exec entry.

### Phase B — Run discovery & branch-coverage triage (API-first, parallel)

**Stages in scope:** only stages where `language == "klang"` AND the procedure has independent runs. Phase B is skipped for SPy stages and for KLang stages that have zero independent runs (e.g., child KLang procedures only invoked as sub-documents — their per-run data is observable in the parent's `stage<M>_branch_trace.json` and there is nothing to list via `ListWorkersByProcedure`).

**What this phase does:** Find up to 5 representative production runs per major branch (per Step B.4), so Phase C only does expensive deep captures on the runs that matter, not all ~100-200 recent runs in the sample window.

**Why this matters.** Deep capture (Phase C) takes 1-5 minutes per run — API trace fetch, recursion into sub-documents, UI work for FILE binaries and `__large_value_*` resolution. If you skip triage and deep-capture everything, that's hours of wall-clock. If you skip triage and pick runs by eye, you'll miss niche branches that show up in 1% of runs. Phase B's "shallow fingerprint" approach takes 10-20 seconds total and gives Phase C a precise shortlist.

**How it works.** Two operations bracket a parallel scan:

1. **One** `getWorkerDocument` call (B.2) — gives the lineId → predicate-text map. Every run of the same KLang version shares the same lineIds, so this map is reusable across all runs. Fetching it once instead of per-run is the difference between 100 calls and 1 call.
2. **N parallel** `getSentenceExecutionData` calls (B.3) — one per candidate run, ~10 concurrent. For each run, the agent inspects which decision-line lineIds were `Met`/`Not Met` to compute a "fingerprint" (the set of branches that run exercised). All fingerprints feed B.4.

**Output:** `_branch_triage.json` — for each branch in `branch_catalog.json`, lists candidate runs and picks a `chosen` representative. Phase C reads this file to know which runs to deep-capture. Branches with zero candidates show up as `coverage_gaps` for the SE to expand the sample window or accept the gap.

**Why fingerprinting beats arbitrary selection:** without B.3, you'd pick runs by recency or eyeballing the UI. That works for the obvious 80% of branches and silently misses the long tail. Fingerprinting EVERY recent run is cheap (parallel shallow API calls) and guarantees branch-level coverage decisions are auditable.

Fallback procedure (when `ListWorkersByProcedure` is unreachable) is Appendix A.1.

#### Step B.1 — List runs

Call `ListWorkersByProcedure`. Save the full response to `_orchestrator_runs_index.json`. This is the **runs index** — no UI scrape required.

```graphql
query ListWorkersByProcedure(
  $procedureId: ID, $departmentId: ID!, $stage: ProcedureStage,
  $limit: Int = 1000, $nextToken: String,
  $stateFilter: String, $fromCreationDate: String, $toCreationDate: String,
  $includeReplayWorker: Boolean, $savedFactSearchInputs: [SavedFactSearchInput!]
) {
  listWorkersByProcedure(
    procedureId: $procedureId, departmentId: $departmentId, stage: $stage,
    limit: $limit, nextToken: $nextToken,
    stateFilter: $stateFilter,
    fromCreationDate: $fromCreationDate, toCreationDate: $toCreationDate,
    includeReplayWorker: $includeReplayWorker, savedFactSearchInputs: $savedFactSearchInputs
  ) {
    items {
      id owner name state knowledgeId departmentId procedureId
      createdAt stateLastUpdatedAt
      attachments
      replayWorkerId isLineV2Enabled totalExecutionTimeInSeconds
      triggerInfo { source }
    }
    nextToken
  }
}
```

Variables: `{ procedureId: <PROCEDURE_ID>, departmentId: <DEPARTMENT_ID>, stage: "PUBLISHED", limit: 1000, includeReplayWorker: true }`. Page with `nextToken` until you've covered the sample window (typically 50-200 most recent runs is enough).

If this returns zero usable runs, switch to Appendix A.1.

`_orchestrator_runs_index.json` shape:
```json
{
  "fetched_at": "2026-05-06T...",
  "filter": { "procedureId": "...", "departmentId": "...", "stage": "PUBLISHED" },
  "runs": [
    {
      "id": "5hz4zlzur81hofr2dk5rivv10",
      "state": "done",
      "createdAt": "2026-04-07T08:03:26.749054+00:00",
      "stateLastUpdatedAt": "2026-04-07T08:09:31.688926+00:00",
      "totalExecutionTimeInSeconds": 355.526213,
      "knowledgeId": "abr14ta8ctird4b9ujcj3g6bb",
      "attachments": ["s3://app-production-files/worker/5hz4.../Scanned_….pdf"],
      "triggerInfo": { "source": "grammar" }
    }
  ]
}
```

`knowledgeId` is the KLang version snapshot at run time — useful for KLang-version awareness without parsing the trace.

#### Step B.2 — Fetch the orchestrator's worker doc once

Call `getWorkerDocument(workerId=<any recent run_id>, documentToken="")` once and save to `_orchestrator_klang.json`. This is the orchestrator's KLang sentence list — used as the canonical lineId → text map and to pin which lineIds are decision predicates per branch in `branch_catalog.json`.

#### Step B.3 — Fingerprint every run in parallel

For each run in `_orchestrator_runs_index.json`, call `getSentenceExecutionData(workerId=<run_id>, documentToken="", token=null)` — orchestrator-only, no recursion. Run these in parallel (10 concurrent is a safe default; raise if rate limits permit).

```js
const concurrency = 10;
const fingerprints = await pMap(runIds, async (runId) => {
  const ed = await callGraphQL("getSentenceExecutionData", {
    workerId: runId, documentToken: "", token: null,
  });
  return computeFingerprint(runId, ed.data.getSentenceExecutionData);
}, { concurrency });
```

`computeFingerprint(runId, execEntries)` extracts:

- For each `if`/`else if` lineId from the branch catalog: `display_value` from `answer.__concept__` (`"True"`/`"False"` for BOOLEAN) and `status` (`"Met"`/`"Not Met"`/`"Skipped"`/`"Condition Not Met"`).
- The list of `(subDocuments[i].documentToken, subDocuments[i].processName)` pairs — which child stages executed.
- The list of loop lineIds where `iterationTokens` was non-empty, with iteration count.
- Final-line status and any exception.

Output: a fingerprint per run, like `{ branches_taken: ["B1a", "B5b"], child_stages: ["Update the Case"], iterations_per_loop: {"<lineId>": 5}, final_status: "done" }`.

#### Step B.4 — Build `_branch_triage.json`

Cluster runs by fingerprint. For each branch in `branch_catalog.json`, list candidates (runs that exercised it) and pick a representative.

```json
{
  "computed_at": "2026-05-06T...",
  "input_runs_count": 173,
  "stages": {
    "0": {
      "B1a": {
        "candidates": [
          { "run_id": "5hz4z...", "createdAt": "2026-04-07T...", "state": "done",
            "knowledgeId": "abr14ta8...",
            "predicate_value_at_decision_line": "True" }
        ],
        "chosen": "5hz4zlzur81hofr2dk5rivv10",
        "reason": "most recent SUCCESS run that took this branch with current knowledgeId"
      },
      "B7c": {
        "candidates": [],
        "chosen": null,
        "reason": "no run in the sample window exercised this branch"
      }
    }
  },
  "coverage_gaps": [
    { "stage": 0, "branch": "B7c", "reason": "no candidate run", "severity": "blocking" }
  ]
}
```

Selection heuristics for `chosen` (now an array, not a single id):

1. Prefer recent runs (KLang most likely matches current).
2. Prefer `state=="done"` over errored runs (unless the branch IS the error path).
3. Prefer runs whose `knowledgeId` matches the most recent run's `knowledgeId` (same KLang version).
4. **Capture up to 5 representatives per branch path**, or `available` if fewer. Diversity across inputs matters: prefer 5 runs with distinct input shapes / vendors / file types over 5 runs that look identical. One run is not enough — within-branch input variance is invisible at N=1.
5. If a branch has fewer than 2 candidates, flag it for Phase B.5 below before declaring `coverage_gaps`.

`coverage_gaps` are flagged in `branch_catalog.md` for the user. Phase C does NOT block on gaps — the user decides whether to expand the sample window, perform a trigger-payload sweep (Phase B.5), or formally accept the gap.

#### Step B.5 — Trigger-payload sweep for unobserved branches

Before declaring a branch uncoverable, check whether the existing runs index contains an input that *would* exercise the branch but whose fingerprint didn't reach it for some other reason.

Procedure (only run when at least one branch has 0 candidates from B.4):

1. For each unobserved branch, identify the **predicate input** that gates it. Examples:
   - `if the Attachments is found then` → trigger payload key `Attachments` presence
   - `if the count equals 0 then` ... `else` → loop-iteration variable `count > 0` ⇒ `finalattachments.length > 1` ⇒ trigger payload key `Attachments` has array length > 1
   - `if vendor is "Woolworths" then` → trigger payload key `vendor` value
2. For each candidate run in `_orchestrator_runs_index.json`, fetch the trigger payload via `GetHistoricalFacts` against the relevant orchestrator input concept (e.g., the `the Attachments are …` line's concept id from the orchestrator's worker doc). Batch in groups of ~50 fact ids per call.
3. Evaluate the predicate against each fetched payload. Any run whose payload would have driven the branch → add to that branch's `candidates` in `_branch_triage.json` and proceed to Phase C for it.
4. If the sweep returns zero runs for a branch, that branch is **confirmed unobserved**. Annotate in `_branch_triage.json` under `coverage_gaps[].reason` with `"sweep complete; no payload matched predicate after checking all <N> indexed runs"`. The SE then decides: (a) ask the customer whether this branch ever runs in production, (b) treat as dead code, or (c) synthesize a test trigger.

The sweep is cheap relative to Phase C captures: one Apollo Client call per ~50 fact ids, no UI clicks, no S3 downloads. Run it before bothering the SE.

### Phase C — Per-run deep capture

#### Phase C.0 — Preflight smoke test (run ONCE, before any deep captures)

Phase C is the slowest phase (1-5 min per representative run × ~10 runs). Failing fast on a broken environment saves 30+ minutes of partial captures. Run these three checks in sequence; abort with a specific error if any fails.

1. **JWT auth check.** Call `ListWorkersByProcedure(procedureId=<PROCEDURE_ID>, departmentId=<DEPARTMENT_ID>, stage="PUBLISHED", limit=1)`. Expect HTTP 200 with `items[0]` present. Failure modes to surface specifically:
   - 401 → "JWT rejected. Refresh and retry."
   - 0 items → "No runs found for this procedure. Did you point at the right URL?"
   - Network error → "Cannot reach api.app.kognitos.com. Check network / VPN."
2. **Exec-data fetch check.** Take `items[0].id` from step 1 (`<probe_run_id>`). Call `getSentenceExecutionData(workerId=<probe_run_id>, documentToken="", token=null)`. Expect a non-empty array. Failure modes:
   - Empty response → "Exec data unavailable for `<probe_run_id>`. Try the next-most-recent run."
   - Schema error → "Exec data shape unexpected — Kognitos may have changed the API. Surface to maintainer."
3. **S3 download check.** Navigate Playwright to the probe run's editor page (`<PROCESS_PUBLISHED_URL>/run/<probe_run_id>`). Find the input file element on the orchestrator's "the attachments are …" line. Click it. Capture the next signed S3 URL via `browser_network_requests`. `curl` it. Expect HTTP 200 with non-zero bytes. Failure modes:
   - No file element found → "Orchestrator's input file not visible in editor. Confirm the automation is file-driven, or surface as a known gap."
   - Signed URL expired immediately → "S3 URL expired before download. Probably a clock-skew or rate-limit issue."
   - 403/404 → "S3 access denied. JWT may need scope expansion."

Total wall-clock: ~30 seconds. If all three pass, proceed to per-run captures. The artifact downloaded in step 3 is throwaway — don't keep it.

**Per-run idempotency precheck:** Before doing any work for a representative run, check whether its folder already exists from a prior partial run:

1. Folder path: `<OUTPUT_BASE_DIR>/run_captures/<YYYY-MM-DD_HH-mm>_<run_id>/`.
2. If the folder exists AND contains a `run_capture.json` that passes schema validation (see "Schema validation" near the end of this spec) AND every `stage<N>_branch_trace.json` referenced in `run_capture.json` is present and validates AND `attachment.<ext>` is present (or explicitly marked absent in the JSON):
   - **SKIP** this run entirely. Move to the next representative.
3. If the folder exists but is partial (some traces missing, no `attachment.<ext>`, etc.):
   - Resume from the first incomplete step rather than restarting. Per-stage trace files that already exist and validate are kept; only missing or invalid ones get refetched.
4. If the folder doesn't exist: proceed with the full capture (steps 1-9 below).

The agent surfaces a one-line status per run: `cached` (skipped), `resumed` (partial → completed), or `fresh` (newly captured). `_capture_index.json` is always regenerated from on-disk state at the end of Phase D.

For each representative run in `_branch_triage.json`, in this order:

1. **Capture orchestrator metadata** from `_orchestrator_runs_index.json` (already have it).
2. **API trace fetch (Stage 0).**
   - Call `getWorkerDocument(workerId, documentToken="")`. (You may already have it from Phase B.2 — reuse if so.)
   - Call `getSentenceExecutionData(workerId, documentToken="", token=null)`.
   - Join on `lineId` → per-line trace records (schema in "Per-line trace record schema").
   - Save as `stage0_branch_trace.json`.
3. **Recurse `subDocuments` → new stages.** For each line in Stage 0's records with `recursion.subDocuments[i].documentToken` non-null: assign the next stage number, call **both** queries with that token, build records, save as `stage<N>_branch_trace.json`. Recurse into grandchildren.
4. **Recurse `iterationTokens` → merge into the SAME stage's `iterations` dict.** For each line with non-empty `recursion.iterationTokens`: for each iteration token, call **only** `getSentenceExecutionData` with `documentToken` unchanged and `iterationToken=<that token>`. Append the resulting records to `iterations[<loop_body_lineId>]` of that stage's trace file. (The lineIds returned point at the same worker doc — no second `getWorkerDocument` needed.)
5. **Recurse `miniPlaygrounds` → new stages** (same as `subDocuments`).
6. **Mark `requires_ui_capture` per record** (rules below).
7. **UI capture pass (always required)** — see Phase C step 6.3 below for the concrete procedure.
8. **Tag KLang version per stage** in `run_capture.json`.
9. **Write `run_capture_filled.md`** modeled on `<REFERENCE_FILLED_CAPTURE>`.

### Phase D — Aggregate index + version evolution

Walk every run folder; aggregate per-stage comparability + branches exercised into `_capture_index.json` (schema below). If any stage shows ≥ 2 distinct KLang versions across the sample, write `_klang_version_evolution.md`.

---

## Authentication

**Run-data GraphQL ops require Apollo Client via `browser_evaluate` — direct curl/fetch returns 401 (verified 2026-05-14).**

The Auth0 setup issues **two** ID tokens with different `aud` claims. The token visible in initial page-load network requests (e.g. `procedureGroup`, `UserClientData`) has `aud: ["https://app.kognitos.com/v2/", ...]`. The run-data ops (`listWorkersByProcedure`, `getSentenceExecutionData`, `getWorkerDocument`, `GetHistoricalFacts`) require a token with `aud: ["https://app.kognitos.com", ...]` — issued only when the View Runs page loads. Even with the correct JWT, browser `fetch()` returns 401 (likely a CORS / origin check). Using the page's built-in Apollo Client sidesteps both problems — auth is already wired in.

**Required pattern for all run-data ops:**

```js
() => window.__APOLLO_CLIENT__.query({
  fetchPolicy: 'network-only',
  query: <AST>,
  variables: { ... }
}).then(r => r.data).catch(e => ({ error: String(e) }))
```

`<AST>` is a parsed GraphQL document. Build it directly with the GraphQL AST kinds (no string parsing needed):

```js
const field = (name, args, sels) => ({ kind: 'Field', name: { kind: 'Name', value: name }, arguments: args || [], selectionSet: sels ? { kind: 'SelectionSet', selections: sels } : undefined });
const arg   = (name, varName)    => ({ kind: 'Argument', name: { kind: 'Name', value: name }, value: { kind: 'Variable', name: { kind: 'Name', value: varName } } });
const varDef = (name, type, required) => ({ kind: 'VariableDefinition', variable: { kind: 'Variable', name: { kind: 'Name', value: name } }, type: required ? { kind: 'NonNullType', type: { kind: 'NamedType', name: { kind: 'Name', value: type } } } : { kind: 'NamedType', name: { kind: 'Name', value: type } } });
const doc = (opName, vars, sels) => ({ kind: 'Document', definitions: [{ kind: 'OperationDefinition', operation: 'query', name: { kind: 'Name', value: opName }, variableDefinitions: vars, selectionSet: { kind: 'SelectionSet', selections: sels } }] });
```

To call `<op>` from inside Playwright: navigate to any authenticated app page first so the Apollo Client is initialized, then run the `browser_evaluate` block above.

**Lifetime:** the Apollo Client persists for the page session. If `window.__APOLLO_CLIENT__` is undefined, the page hasn't fully booted — wait for `#slate-editor` (or any signed-in element) before querying.

**No curl/fetch fallback for run-data ops.** The historical curl pattern documented in earlier versions of this spec is removed — it doesn't work against the production audiences. The only place curl is still used in Phase C is to GET signed S3 URLs that the UI hands us after a click (and even then, the URL came from a network capture, not from a GraphQL call).

## The three queries

### `ListWorkersByProcedure` — runs list

(See Phase B.1 for query body and variables.)

### `getWorkerDocument` — KLang sentence list

```graphql
query getWorkerDocument($workerId: ID!, $documentToken: String) {
  getWorkerDocument(workerId: $workerId, documentToken: $documentToken) {
    lineId text parentId shouldPause language
    metadata { lineId parentId }
    internalMetadata { key value }
  }
}
```

### `getSentenceExecutionData` — runtime values per sentence

```graphql
query getSentenceExecutionData($workerId: ID!, $token: String, $documentToken: String) {
  getSentenceExecutionData(workerId: $workerId, iterationToken: $token, documentToken: $documentToken) {
    lineId token status answer concepts requests iterationTokens epoch
    subDocuments { documentToken processName }
    miniPlaygrounds { documentToken processName }
    startedAt completedAt answerOffloadedUrl conceptsOffloadedUrl
  }
}
```

`answer` and `concepts` are JSON-encoded **strings**. `json.loads(...)` them before extracting.

---

## How the join works — three worked examples

Every exec entry maps to exactly one worker-doc sentence by `lineId` (verified 100% on the runs sampled). For each pair, the agent writes one **per-line trace record**.

### Example 1 — simple STRING assignment

Worker doc:
```json
{ "lineId": "v2_…e2935cc…_1", "text": "the caseNumber is \"56444\"" }
```
Exec data (same `lineId`):
```json
{ "answer":   "{\"__concept__\":{\"id\":\"concept/ai15lmr1…\",\"name\":\"a caseNumber\",\"fact_type\":\"STRING\",\"display_value\":\"56444\"}}",
  "concepts": "[{\"ids\":[\"concept/ai15lmr1…\"],\"name\":\"the caseNumber\",\"fact_types\":[\"STRING\"],\"display_values\":[\"56444\"]}]" }
```
Per-line trace record:
```json
{
  "lineId": "v2_…e2935cc…_1",
  "token": "/0",
  "text": "the caseNumber is \"56444\"",
  "status": "SUCCESS",
  "produced": { "name": "caseNumber", "fact_type": "STRING", "display_value": "56444" },
  "referenced": [],
  "requires_ui_capture": false
}
```

### Example 2 — STRING produced from a JSON concept (the `__large_value` case)

Worker doc:
```json
{ "lineId": "v2_…3acfef0b…_0", "text": "get the customerRecord's \"custentity_department\" as the dept" }
```
Exec data:
```json
{ "answer":   "{\"__concept__\":{\"name\":\"a dept\",\"fact_type\":\"STRING\",\"display_value\":\"2\"}}",
  "concepts": "[{\"name\":\"the dept\",\"fact_types\":[\"STRING\"],\"display_values\":[\"2\"]},
                {\"ids\":[\"concept/9sig8z7g…\"],\"name\":\"the customerRecord\",\"fact_types\":[\"JSON\"],\"display_values\":[\"__large_value_7519\"]}]" }
```
Per-line trace record:
```json
{
  "lineId": "v2_…3acfef0b…_0",
  "token": "/0",
  "text": "get the customerRecord's \"custentity_department\" as the dept",
  "status": "SUCCESS",
  "produced": { "name": "dept", "fact_type": "STRING", "display_value": "2" },
  "referenced": [
    { "name": "customerRecord", "concept_id": "concept/9sig8z7g…",
      "fact_type": "JSON", "display_value": "__large_value_7519",
      "needs_ui_resolution": true }
  ],
  "requires_ui_capture": false
}
```

`produced` = what this line bound (clean STRING `dept = "2"`). `referenced` = what was active but not produced (the customerRecord, only available as a placeholder). `needs_ui_resolution: true` signals that IF a downstream branch reads `customerRecord` fields, the SOP author will need its actual JSON — Phase C step 6's logic decides whether to set `requires_ui_capture: true` based on that.

### Example 3 — list result (FILE attachments)

Worker doc:
```json
{ "lineId": "v2_…fac160d7…_1", "text": "the attachments are \"s3://app-production-files/worker/…/Scanned_…pdf\"" }
```
Exec data:
```json
{ "answer": "{\"__concepts__\":{\"items\":[{\"__concept__\":{\"id\":\"concept/03wfyg43…\",\"fact_type\":\"FILE\"}}],\"name\":\"attachments\"}}",
  "concepts": "[{\"ids\":[\"concept/03wfyg43…\"],\"name\":\"the attachments\",\"fact_types\":[\"FILE\"],\"display_values\":[\"s3://…/Scanned_….pdf\"]}]" }
```
Per-line trace record:
```json
{
  "lineId": "v2_…fac160d7…_1",
  "token": "/0",
  "text": "the attachments are \"s3://…/Scanned_…pdf\"",
  "status": "SUCCESS",
  "produced": {
    "name": "attachments", "fact_type": "FILE", "is_list": true,
    "items": [{ "concept_id": "concept/03wfyg43…", "fact_type": "FILE",
                "display_value": "s3://app-production-files/worker/.../Scanned_….pdf",
                "filename": "Scanned_….pdf" }]
  },
  "referenced": [],
  "requires_ui_capture": true,
  "ui_capture_target": "attachment.pdf",
  "ui_capture_status": "pending"
}
```

After the UI batch pass:
```json
{ "requires_ui_capture": true, "ui_capture_target": "attachment.pdf",
  "ui_capture_status": "captured", "ui_capture_path": "attachment.pdf",
  "ui_capture_timestamp": "2026-05-06T..." }
```

---

## Per-line trace record schema

This is the unit the agent writes per executed line. `stage<N>_branch_trace.json` contains an array `lines[]` of these (in execution order) plus an `iterations` dict for loop bodies.

```jsonc
// stage<N>_branch_trace.json
{
  "stage_number": 0,
  "stage_name": "Netsuite Customer Payments / to create a sales order",
  "automation_id": "2qtb1tar4fntt91qbreg0bjfo",
  "document_token": "",                          // "" for orchestrator; "/0/230" etc for sub-docs
  "klang_hash": "v2_0c5e2211e8efbd61acb9299571e8f2a6",
  "klang_version_at_run_time": "Apr2026-schema",
  "klang_version_current": "Apr2026-schema",
  "lines": [
    {
      "lineId": "v2_<klang_hash>_<line_hash>_<idx>",
      "token": "/0",                              // path through doc + iterations
      "parent_lineId": null,
      "text": "<KLang sentence as authored>",
      "status": "SUCCESS|Met|Not Met|Done|Skipped|Condition Not Met",
      "started_at": "...",
      "completed_at": "...",
      "produced": {
        "name": "<binding name like 'caseNumber'>",
        "concept_id": "concept/<uuid>",
        "fact_type": "STRING|NUMBER|BOOLEAN|JSON|TABLE|MARKDOWN|FILE|RESULT",
        "display_value": "<inline value, possibly __large_value_NNNN>",
        "is_list": false,
        "items": null,                            // populated only when is_list: true
        "csv_path": null                          // populated only for fact_type=TABLE
      },
      "referenced": [
        {
          "name": "<other binding present at this line>",
          "concept_id": "concept/<uuid>",
          "fact_type": "...",
          "display_value": "...",                  // may be __large_value_NNNN
          "needs_ui_resolution": false             // true only if the SOP needs the actual value
        }
      ],
      "recursion": {
        "subDocuments":   [{ "documentToken": "/0/230", "processName": "Update the Case", "stage_number": 1 }],
        "miniPlaygrounds": [],
        "iterationTokens": ["/0/16", "/0/55", "/0/94", "/0/133", "/0/172"]
      },
      "requires_ui_capture": false,
      "ui_capture_target": null,                  // canonical filename (see naming convention)
      "ui_capture_status": null,                  // null|pending|captured|skipped|failed
      "ui_capture_path": null,                    // on-disk path after capture
      "ui_capture_timestamp": null,
      "ui_capture_notes": null,
      "synthetic": false                          // true for non-v2_ lineIds in sub-docs
    }
  ],
  "iterations": {
    "<loop_body_lineId>": [
      { "iteration_token": "/0/16", "lines": [ /* records, same shape as above */ ] }
    ]
  }
}
```

### `requires_ui_capture` decision rule

A record gets `requires_ui_capture: true` iff at least one of:

1. `produced.fact_type == "FILE"` AND it's the orchestrator's input attachment OR a FILE the SOP/handoff payload references by name.
2. `produced.fact_type == "JSON"` AND `produced.display_value` is `__large_value_*` AND a downstream branch predicate reads this concept.
3. Any `referenced[i]` has `display_value: __large_value_*` AND a downstream branch predicate reads that concept.

For TABLE: don't set `requires_ui_capture` — the full CSV is already in `display_value`. Instead write it to disk inline (Phase C step 2) and record `produced.csv_path`.

Otherwise: leave the placeholder/`s3://` string in the trace, mark `ui_capture_status: "skipped"`, write `ui_capture_notes` explaining why. Phase 2-3 will tell us if more values are needed; coverage gaps are cheaper to backfill than over-capture.

### `ui_capture_target` filename naming convention (PINNED — two agents must produce the same paths)

| Item | `ui_capture_target` |
|---|---|
| Orchestrator's input attachment | `attachment.<ext>` — extension from the original filename in `display_value` |
| Sub-stage's distinct input file | `stage<N>_input.<ext>` |
| FILE produced mid-run (e.g. generated invoice PDF) | `stage<N>_<lineId_first8>_<binding_name>.<ext>` |
| Resolved `__large_value_*` JSON (referenced concept) | `stage<N>_<lineId_first8>_<binding_name>.json` |
| Full TABLE CSV (always saved inline; not a UI capture) | `stage<N>_<lineId_first8>_<binding_name>.csv` |

`<lineId_first8>` = first 8 chars of the line-hash portion of the lineId (e.g. `fac160d7` from `v2_0c5e2211…_fac160d77e7e7d7c396e937f5ca7713c_1`). `<binding_name>` = `produced.name` or `referenced[i].name`, lowercase, non-alphanumeric replaced with `_`.

---

## Decoding values by `fact_type`

`answer` always wraps either `__concept__` (single concept) or `__concepts__` (list). `concepts` lists every named concept active at that line. Real cases observed in run `5hz4zlzur81hofr2dk5rivv10`:

| `fact_type` | `answer.__concept__.display_value` | What to record | UI needed? |
|---|---|---|---|
| `STRING` | the literal value | the value | no |
| `NUMBER` | the literal number as a string | the value | no |
| `BOOLEAN` | `"True"` / `"False"` | the boolean (use to compute Met/Not Met) | no |
| `JSON` (small) | inline JSON, e.g. `{"id":"48558"}` | inline JSON | no |
| `JSON` (large) | `__large_value_NNNN` placeholder | placeholder; capture from UI only if downstream needs it | yes if needed |
| `TABLE` | full CSV inline (newline-separated) | save to `stage<N>_<lineId_first8>_<name>.csv`; record `csv_path` + `row_count` | no |
| `MARKDOWN` | extraction-rule prompt body | as text | no |
| `RESULT` | `"Done"` / `"OK"` — placeholder for "this line ran" | `"Done"` + `subDocuments` token (recurse) | no (recurse) |
| `FILE` | `s3://...` path | the path; binary not in API | yes (UI) |

---

## How `__large_value_NNNN` actually works

Verified live against run `5hz4zlzur81hofr2dk5rivv10`'s `customerRecord` (`concept/9sig8z7g…`):

- `display_value` is `__large_value_7519` on EVERY appearance of the concept — including the line that produced it.
- The producing line's own `answer.__concept__.display_value` is `"OK"` (a `RESULT`, not the actual JSON).
- `answerOffloadedUrl` and `conceptsOffloadedUrl` are null on every entry.
- `FactsAtLineId` (the editor's per-line refresh op) was the resolver in older clients but is **broken in current production** — calls fail with schema errors (`Unknown argument 'workerId'`, `Field 'factsAtLineId' argument 'input' of type 'GetFactsAtLineIdInput!' is required`). Verified 2026-05-14. Do not call it.

**Note:** `__large_value_*` shows up on **any** value type whose serialized size exceeds the inline limit — STRING, FILE, JSON. Earlier versions of this spec said "JSON only"; that's wrong.

**Resolution order:**

1. If `answerOffloadedUrl` or `conceptsOffloadedUrl` is non-null on the line, GET that URL with the same `Authorization: <JWT>` header. Save the JSON to `stage<N>_<lineId_first8>_<binding_name>.json` and replace `display_value` in the record with `<see file: stage<N>_<lineId_first8>_<binding_name>.json>`.
2. Otherwise, resolve via **`GetHistoricalFacts`** (Apollo Client `browser_evaluate`, see "Authentication"):

   ```graphql
   query GetHistoricalFacts($knowledgeId: ID!, $factIds: [HistoricalFactID!]!) {
     getHistoricalFacts(knowledgeId: $knowledgeId, factIds: $factIds) {
       id
       names
       type
       value             # actual value (unescaped JSON string for STRING/JSON; S3 URI for FILE)
       valueOffloadedUrl # non-null only for very large values; fall back to GET that URL if present
     }
   }
   ```

   Inputs:
   - `knowledgeId` = `run.knowledgeId` from `ListWorkersByProcedure` (one per run).
   - `factIds` = `[{ id: <concept_id>, epoch: <epoch> }, ...]`. Both come from a `getSentenceExecutionData` entry:
     - `concept_id` = `JSON.parse(entry.answer).__concept__.id` (or any matching id from `entry.concepts`)
     - `epoch` = `entry.epoch`

   **Batch multiple concepts per call** — `factIds` is an array; the same `knowledgeId` covers everything in the run.

3. **FILE type:** `GetHistoricalFacts` returns the raw `s3://...` URI in `value` — that is **not** a downloadable URL. To download the binary, still perform the UI click on `[data-cy="line-facts-FILE"]`: the editor's popover triggers a signed HTTPS URL via a network request which `browser_network_requests` captures, then `curl` it.

4. **Cache by `concept_id`** within the same run: a single `GetHistoricalFacts` call can resolve every appearance of every `__large_value_*` for that run. No per-line work needed.

5. If no downstream branch decision needs the value, **skip resolution** — record `value_capture_status: "skipped"` with notes. This decision is still recorded on the per-line trace record.

---

## Recursion: explicit rules + concrete examples

Each exec entry can have three non-null handles. The agent's action depends on which.

| Handle | Meaning | Action | New stage? | Second `getWorkerDocument` needed? |
|---|---|---|---|---|
| `subDocuments[i].documentToken` | Line invoked a child automation. | New stage. Call BOTH queries with that token. | yes | yes |
| `iterationTokens[i]` | Loop body executed N iterations. | Same stage. Append to `iterations[<loop_body_lineId>]`. Call ONLY `getSentenceExecutionData` per token. | no | no |
| `miniPlaygrounds[i].documentToken` | In-line mini-process. | Same as subDocuments. | yes | yes |

### Concrete examples (verified on run `5hz4zlzur81hofr2dk5rivv10`)

#### `subDocuments` → new stage

Stage 0 had this entry:
```json
{
  "lineId": "v2_…ef71372cd1ceaf3bd6cd4304d14837c8_0",
  "text": "run @{\"type\":\"procedure\",\"display\":\"Update the Case\",\"value\":\"6szk1unn9661xjtf9uhpflrja\"}",
  "subDocuments": [{ "documentToken": "/0/230", "processName": "Update the Case" }]
}
```

The agent assigns `stage_number: 1` and calls:
```
getWorkerDocument(workerId="5hz4z…", documentToken="/0/230")
  → 64 sentences for "Update the Case" with KLang hash v2_f9987da9bd5aac783554b22672febfce
getSentenceExecutionData(workerId="5hz4z…", documentToken="/0/230", token=null)
  → 64 exec entries
```
Joined → `stage1_branch_trace.json`. If Stage 1's records have more `subDocuments`, those become Stage 2 (depth-first).

#### `iterationTokens` → SAME stage's iterations dict

Stage 0 had this entry:
```json
{
  "lineId": "v2_…73b07aa897c5cdd4bee61efb2bf05e23_0",
  "text": "process each row in the items table as follows",
  "iterationTokens": ["/0/16", "/0/55", "/0/94", "/0/133", "/0/172"]
}
```

Five iterations. The agent calls **only** `getSentenceExecutionData` per token:
```
getSentenceExecutionData(workerId="5hz4z…", documentToken="", iterationToken="/0/16")
  → 37 exec entries scoped to iteration 1
… same for /0/55, /0/94, /0/133, /0/172
```

The lineIds returned point at the **same orchestrator KLang sentences** (same hash). The loop body's sentences are already in the orchestrator's worker doc, so no second worker-doc fetch.

These records go into Stage 0's trace file under:
```json
"iterations": {
  "v2_…73b07aa897c5cdd4bee61efb2bf05e23_0": [
    { "iteration_token": "/0/16", "lines": [/* 37 records */] },
    { "iteration_token": "/0/55", "lines": [/* 37 records */] },
    { "iteration_token": "/0/94", "lines": [/* 37 records */] },
    { "iteration_token": "/0/133", "lines": [/* 37 records */] },
    { "iteration_token": "/0/172", "lines": [/* 37 records */] }
  ]
}
```

Keying by `loop_body_lineId` matters for nested loops. Note iteration tokens have nested paths like `/0/16/39` and `/0/16/39/41/42` — these reflect the iteration scope inside the orchestrator.

#### `miniPlaygrounds` → new stage (like subDocuments)

Embedded mini-process / extraction prompt with its own document. None observed in the verification run, but the recursion shape is identical to `subDocuments`: assign next stage number, call BOTH queries with `documentToken = miniPlaygrounds[i].documentToken`.

### Sub-document non-`v2_` lineIds

Inside a sub-document (e.g., "Update the Case"), some entries have lineIds like `5mjrhxKFiPCooUyMux38gN` or `8QKdGoTauqvDnD43VSBWRH_2026-01-07T13:41:36.709609+00:00` — system-generated entries (human-in-the-loop responses, exception threads). Their `text` in `getWorkerDocument` is empty. Record them in the stage trace but mark `synthetic: true` and don't attempt branch labeling.

---

## Phase C step 6.3 — UI capture pass (always required)

After the API trace is complete for the run + all stages + all iterations, the agent has a list of records with `requires_ui_capture: true` and `ui_capture_status: "pending"`. Do all UI work in one pass per run — don't interleave with API calls.

### Setup

1. Open the run page in Playwright at `<PROCESS_PUBLISHED_URL>/run/<run_id>` (replacing `/run/all` with the specific run).
2. Wait for the editor to finish initial load (~3-5s).
3. If a sub-process tab is selected by default, click the orchestrator's tab first.

### Sub-process navigation

Child runs are reached via the orchestrator's editor: the purple subprocess icon (`autoPilotSVGContainer` element) on the line that contains the `run <child-automation-name> with` step. Clicking it adds `?subProcess=…` to the URL or activates the child's tab. This is how steps B and C below reach lines that aren't in the orchestrator's editor view.

### S3 URL patterns

When you click a `file:<NAME>` element, the next signed S3 URL varies by how the file got into the system. Match all three when filtering `browser_network_requests`:

- **Orchestrator-uploaded** (worker context): `https://app-production-files.s3.amazonaws.com/worker/<RUN_ID>/.../retrieve_attachment/<FILE>?...`
- **Sub-automation child run** (file passed via `copy_process_variable`): `https://app-production-files.s3.amazonaws.com/<DEPT_ID>/copy_process_variable/<UUID>/<FILE>?...`
- **Internal upload** (e.g., from a Kognitos staff user): `https://app-production-files.s3.amazonaws.com/worker/<other-run-id>/<email>/<UUID>/<FILE>?...`

Signed URLs are short-lived (~12 hours `Expires=`). `curl` to disk immediately after capture; re-click to refresh if expired.

### For each pending record, in stage → line order

Branch by what kind of capture is needed.

#### A. Input file (orchestrator's `the attachments are …` line)

1. Find the line in the editor by searching the editor's DOM for the line's `text` (the full predicate). The editor renders each line as a row whose innerText contains the predicate — match unique substrings to disambiguate.
2. Within that row, find the `file:<NAME>` element (typically a small file-icon button with the filename as text or aria-label).
3. Click it.
4. Capture the next network request matching one of the S3 URL patterns above via `browser_network_requests`.
5. `curl` the signed URL to `<run_folder>/<ui_capture_target>` (e.g. `attachment.pdf`).
6. Update the record: `ui_capture_status: "captured"`, `ui_capture_path: "<ui_capture_target>"`, `ui_capture_timestamp: now`.

#### B. Sub-stage's distinct input file

1. Navigate into the child run page via the purple subprocess icon (see "Sub-process navigation").
2. On the child's run page, repeat A's steps with `ui_capture_target: "stage<N>_input.<ext>"`.

#### C. Large JSON value (badge click)

1. Navigate to the stage where the value first appears (orchestrator tab, child tab, etc — known from `produced.concept_id` plus the stage that produced it; if uncertain, any line where the concept is referenced works).
2. Find the line by searching the editor's DOM for the predicate text.
3. Within that row, find the `{ }` value badge for the relevant binding name (e.g. the badge next to "the customerRecord").
4. Click it.
5. Capture the popover's network request response body via `browser_network_requests`. (TODO: pin the GraphQL op name once observed.)
6. Save the JSON to `<run_folder>/<ui_capture_target>` (e.g. `stage0_3acfef0b_customerrecord.json`).
7. Update the record (and any other records sharing the same `concept_id`): `ui_capture_status: "captured"`, `ui_capture_path: "<ui_capture_target>"`.

### Edge cases

- **Element not found in DOM** (line off-screen due to virtualization): `scrollIntoView` an adjacent element first; retry the search. If still not found, surface as a blocker.
- **Click triggered no network request**: re-click; some popovers debounce. Surface as a blocker after 2 retries.
- **Signed URL expired by `curl` time**: re-trigger the click (URLs regenerate per click). If repeatedly expires, capture and `curl` in the same Playwright `evaluate` to keep wall-clock time minimal.
- **Same large value on hundreds of lines**: cache by `concept_id`; click-resolve once, reuse the path.
- **File-element click blocked by overlay** (e.g. modal): close overlay first; surface as blocker if persistent.
- **Sub-process child run not navigable from the orchestrator UI** (popover not clickable, etc.): surface as a blocker. Don't ship a run folder with a missing stage capture.

---

## Schema: `run_capture.json` and `_capture_index.json`

### `run_capture.json` — per-run record

`stages[]` has one entry per stage that actually executed in the run (Stage 0 = orchestrator; Stage 1, 2, … = each child automation, recursively, in invocation order).

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
      "stage_number": 1,
      "stage_name": "Update the Case",
      "automation_id": "6szk1unn9661xjtf9uhpflrja",
      "document_token": "/0/230",
      "klang_hash": "v2_f9987da9bd5aac783554b22672febfce",
      "klang_version_at_run_time": "v2-stable",
      "klang_version_current": "v2-stable",
      "comparability": "current",
      "comparability_reason": null,
      "trace_captured": true,
      "trace_path": "stage1_branch_trace.json",
      "branches_exercised": ["UC1a", "UC3b"],
      "ui_captures": [
        { "lineId": "v2_…fac160d7…_1", "target": "attachment.pdf",
          "status": "captured", "path": "attachment.pdf" }
      ]
    }
  ]
}
```

`comparability` controlled vocabulary — three values:

| Value | Meaning |
|---|---|
| `current` | Stage's KLang at run time matches current published version. Trace is a safe parity reference. |
| `near-current` | Differs only in non-load-bearing ways for THIS run's input. Document divergence in `comparability_reason`. |
| `supplementary` | Differs in load-bearing ways. NOT a parity reference. Useful only as supporting evidence. |

### `_capture_index.json` — aggregated derived view

```json
{
  "stages": {
    "0": {"name": "create a credit memo netsuite", "current_version_label": "v0-stable"},
    "1": {"name": "Update the Case", "current_version_label": "v2-stable"}
  },
  "captures": [
    {
      "run_id": "...",
      "folder": "2026-04-07_14-54_...",
      "case_number": "56377",
      "input_file": "attachment.pdf",
      "stages_comparability": {"0": "current", "1": "current"},
      "stages_comparability_reasons": {},
      "branches_exercised_per_stage": { "0": ["B1a", "B7a"], "1": ["UC1a"] }
    }
  ],
  "branch_coverage_per_stage": {
    "0": { "B1a": {"current": ["2026-04-07_..."], "near-current": [], "supplementary": []} }
  }
}
```

`branch_coverage_per_stage` is the load-bearing structure: it answers "is this branch covered by a parity-quality capture?" with one lookup. Pin bucket keys to `current` / `near-current` / `supplementary`.

---

## What goes in `run_capture_filled.md`

The trace JSONs are the underlying data. `run_capture_filled.md` is the human-readable summary, modeled on `<REFERENCE_FILLED_CAPTURE>`. Keep it focused:

- Run identity (run ID, case number, timestamp, attachment filename).
- Inputs — the orchestrator's bound inputs (case, attachments, etc.).
- Stage-by-stage narrative:
  - For each stage: stage number, stage name, KLang version + comparability, branches taken (with the literal predicate that fired).
  - Key produced values — the ones the SOP author cares about: extracted fields, decision inputs, classification outputs, final handoff payload values.
  - Skipped branches noted so coverage analysis can compare.
- Final handoff payload (Update the Case / create customer payment / etc.): full field list with values.
- Files and large values list — link each to its on-disk path so the SOP author can open them.

Don't dump the trace verbatim into the markdown; that's what `stage<N>_branch_trace.json` is for.

---

## Required output checklist (per run folder)

```
<OUTPUT_BASE_DIR>/run_captures/<YYYY-MM-DD_HH-mm>_<run_id>/
├── run_capture_filled.md
├── run_capture.json
├── attachment.<ext>                                  ← input file binary
├── stage0_branch_trace.json                          ← orchestrator
├── stage1_branch_trace.json                          ← each child stage
├── stage2_branch_trace.json
├── stage<N>_input.<ext>                              ← optional: distinct sub-stage input
├── stage<N>_<lineId_first8>_<name>.csv               ← optional: TABLE values
├── stage<N>_<lineId_first8>_<name>.json              ← optional: resolved __large_value_* JSON
└── stage<N>_lines_raw.json                           ← optional: full answer/concepts payloads
```

And at the run_captures root:

```
<OUTPUT_BASE_DIR>/run_captures/
├── _orchestrator_runs_index.json                     ← Phase B.1 (ListWorkersByProcedure dump)
├── _orchestrator_klang.json                          ← Phase B.2 (orchestrator's worker doc, fetched once)
├── _branch_triage.json                               ← Phase B.4
├── _capture_index.json                               ← Phase D
└── _klang_version_evolution.md                       ← only if KLang versions diverge
```

---

## Schema validation (run at the end of every phase)

Every JSON file the spec produces has a JSON Schema in `~/kognitos-migration-assets/schemas/`. After each phase completes its work, the agent runs the validator and refuses to declare the phase "done" if any file fails:

```bash
python3 ~/kognitos-migration-assets/tools/validate.py <OUTPUT_BASE_DIR> --phase <0|B|C|D>
```

Exit code 0 = all valid; non-zero = at least one file failed. The validator prints one line per file with `OK` or `FAIL <path>: <reason>` so the agent can fix the offending output before moving on.

Files validated by phase:

| Phase | Files |
|---|---|
| 0 | `_hydration.json` |
| B | `_orchestrator_runs_index.json`, `_branch_triage.json` |
| C | each `run_captures/<folder>/run_capture.json` and every `stage<N>_branch_trace.json` referenced from it |
| D | `_capture_index.json` |

If a schema is missing for a file the agent generates, that's a spec bug — surface it; don't silently skip. (The validator prints `no-schema (skipped)` for unknown filenames; consider that a soft warning, not a pass.)

The schemas themselves live in `~/kognitos-migration-assets/schemas/`:

- `hydration.schema.json`
- `orchestrator_runs_index.schema.json`
- `branch_triage.schema.json`
- `run_capture.schema.json`
- `capture_index.schema.json`
- `stage_branch_trace.schema.json`

When adding new fields to the JSON output, update the corresponding schema in the same commit.

---

## Quality Bar

- No required field left as TBD.
- Every capture explicitly states which branch(es) it exercises.
- Every line in every trace JSON has a non-null `produced` (or `produced.fact_type == "RESULT"` with `display_value: "Done"` for sub-doc invocations).
- No `__large_value_NNNN` string appears in `produced.display_value` or any `referenced[].display_value` without `ui_capture_status` set to one of `captured` / `skipped` (with `ui_capture_notes` explaining the skip).
- No `s3://...` string appears in `produced.display_value` of a FILE-typed line without a corresponding `ui_capture_status: "captured"` and on-disk file.
- Each stage's KLang version is tagged + comparability stated.
- Sub-automation traces present for every child invocation that actually executed.
- LineId join is checked: every exec entry maps to a worker-doc sentence (or is one of the small set of synthetic non-`v2_` entries marked `synthetic: true`).

## Common Phase 1 Misses

1. **Missing input binary** — captured filename + extracted output but not the file. Always Phase C step 6.3 sub-A first; signed URLs expire.
2. **Missing sub-automation traces** — only orchestrator's shallow flow captured. Walk every record's `recursion.subDocuments` / `recursion.miniPlaygrounds` and recurse on every one.
3. **Missing loop iterations** — captured stage 0 of a loop but not each iteration.
4. **`__large_value_NNNN` left as data** — placeholder string saved into trace as if it were the actual JSON. Either UI-resolve it or mark `ui_capture_status: "skipped"` with explanation.
5. **TABLE display values truncated** — `display_value` is full CSV, save all of it; don't keep only the first lines.
6. **No KLang version tagging per stage.**
7. **Run folders incomplete** — markdown without JSON, or vice versa.
8. **Multiple invoked automations not enumerated** — only orchestrator's KLang in branch catalog.

## Success Criteria

Step 1 is complete when:

1. Branch catalog covers major control-flow branches across orchestrator AND every invoked sub-automation.
2. Migration-specific run capture template exists.
3. At least one representative run capture exists per major branch (or a flagged coverage gap with stakeholder sign-off).
4. Every run folder includes filled markdown, JSON, input file binary, and a `stage<N>_branch_trace.json` for every sub-automation/loop that actually executed.
5. Every (run × stage) is tagged with KLang version + `comparability`.
6. `_branch_triage.json` exists so coverage decisions are auditable.
7. `_capture_index.json` aggregates everything Phase 2-3 needs.
8. If KLang has evolved, `_klang_version_evolution.md` documents each version's differences.

---

# Appendix A — UI fallback when API is unavailable

Use this path **only** when the decision rules at the top of the spec route you here:

- `<JWT>` returns 401 twice with a fresh token, OR
- `api.app.kognitos.com` is unreachable, OR
- `ListWorkersByProcedure` returns zero usable runs.

Otherwise, the API path is faster and more reliable.

The UI fallback produces the same artifacts (`branch_catalog.{md,json}`, `_orchestrator_runs_index.json`, per-run folders with traces and binaries, `_capture_index.json`) but via editor-walking instead of GraphQL.

## A.1 Run discovery (replaces Phase B.1)

From `<PROCESS_PUBLISHED_URL>`:

1. Open **View Runs**. Scroll back far enough to cover all major branch categories.
2. Save the View Runs index to `_orchestrator_runs_index.json` with `runId`, `cells`, and `rowText` per row. Same shape as the API version but with `attachments: null` for entries where the filename can't be read from the row text.
3. Find one representative run for each major branch category (use the branch catalog matrix as a checklist). Prefer recent runs whose KLang version matches current.

## A.2 KLang collection (replaces Phase B.2 / Phase A inputs)

If `getWorkerDocument` is unreachable: paste the orchestrator's KLang from the editor (Copy All in Chrome) into `<KLANG_PATH>`. For each `run <child-automation-name>` line in the orchestrator's KLang, open the child automation's editor and paste its KLang into the corresponding `<SUB_AUTOMATION_KLANG_PATHS>` entry. Recurse into grandchildren.

This is the only manual step that scales poorly. Once you have the JWT working, switch back to the API path.

## A.3 Per-run capture (replaces Phase C steps 1-5)

For each chosen run:

1. Navigate to the orchestrator run URL.
2. Capture orchestrator-level metadata (case number, status, timestamp, attachment filename).
3. **Click the input file element** → capture signed S3 URL (S3 URL patterns documented in Phase C step 6.3) → `curl` to `attachment.<ext>`.
4. Walk the editor line by line, capturing every condition line as `"<line_no>": "<predicate text> | <Met / Not Met / Done / Skipped>"`. This is the manual equivalent of joining `getWorkerDocument` × `getSentenceExecutionData`.
5. For each sub-process invocation (purple `autoPilotSVGContainer` icon): navigate into the child via the icon → repeat step 4 → save as `stage<N>_branch_trace.json`. Recurse into grandchildren.
6. Capture Stage 1 (or first-child) outputs by clicking the relevant `get the above as the data` line's value badge → save as `stage1_outputs.json`.
7. Capture the final handoff payload values by clicking value badges on the handoff line (`Update the Case`, `create customer payment`, etc.).
8. Tag KLang version per stage in `run_capture.json`.
9. Write `run_capture_filled.md` modeled on `<REFERENCE_FILLED_CAPTURE>`.

The trace records produced by editor-walking will be lower fidelity than API records — they typically lack `concept_id`, `fact_type`, full `referenced[]` lists, and exact `started_at`/`completed_at` timestamps. Phase 2-3 tolerates this, but parity diffs will be coarser. Note this in `comparability_reason` on every stage entry: `"trace captured via UI fallback — concept_ids and referenced[] omitted"`.

## A.4 Aggregate (Phase D — unchanged)

Phase D is text-only and works identically regardless of how Phases A/B/C were sourced.
