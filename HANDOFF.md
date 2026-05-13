# Handoff — Migration Workflow Rework (2026-05-12 → 13)

This document hands off ~2 days of work redesigning the Kognitos V1 → V2 migration workflow. Read this first if you're picking up the project. Time to read: ~10 minutes.

## TL;DR

Goal: reduce SE intervention and iteration time on V1→V2 migrations.

What's done in this session:
- Step 1 (Data Collection) collapsed and largely automated. SE gives one URL → agent produces full `<automation_slug>/` output directory.
- Spec, schemas, validator, run-capture template, and example filled-capture moved out of `golem/specs/` into a new repo `~/kognitos-migration-assets/` (pushed to `sasha-kog/migration-assets`, pending transfer to `kognitos` org).
- Notion page updated to match.
- Step 2-3 (SPy iteration) reworked with plan-first Quill + exception-feedback-loop patterns. **Not yet exercised** on a real migration.

What's not done: replay harness (Thread A), polish items (G/H/I), strategic items (J/K/L), and the test of the new Phase B loop on a real migration.

---

## 1. Orientation

### Project layout

```
~/kognitos-migration-assets/          ← canonical home of the migration workflow
├── README.md
├── CLAUDE.md                          ← agent conventions (auto-loaded in this dir)
├── HANDOFF.md                         ← this file
├── run_capture_template.md            ← generic skeleton for run_capture_filled.md
├── specs/
│   ├── migration-step-1-data-collection.md     ← Step 1 spec (KLang + run capture)
│   └── migration-step-2-3-combined.md          ← Step 2-3 spec (SOP + SPy iteration)
├── schemas/                           ← JSON Schemas for all output files
│   ├── hydration.schema.json
│   ├── orchestrator_runs_index.schema.json
│   ├── branch_triage.schema.json
│   ├── run_capture.schema.json
│   ├── capture_index.schema.json
│   └── stage_branch_trace.schema.json
├── tools/
│   └── validate.py                    ← JSON output validator
├── example_filled_capture/            ← canonical example of a filled run capture
│   ├── README.md
│   ├── run_capture_filled.md
│   ├── email.html
│   ├── message_record.json
│   └── support_record.json
└── notion/                            ← paste-ready Notion drafts (already applied)
    ├── README.md
    ├── step-0-setup.md
    └── step-1-data-collection.md
```

Other relevant paths:

- **Notion page (canonical SE-facing):** [Agentic Automation Migration Workflow](https://www.notion.so/kognitos/Agentic-Automation-Migration-Workflow-342281a74b6181478f8bfdde60a970b6)
- **GitHub repo:** https://github.com/sasha-kog/migration-assets (private; **pending transfer to `kognitos` org**)
- **Plunkett (current migration customer artifacts):** `/Users/sashajh2/Kognitos/plunkett/` — has finished/in-progress migrations for `create_customer_payment`, `create_credit_memo`, `create_sales_order`, `create_vendor_bill`, `process_incoming_case`, `update_the_case`
- **Older drafts (kept as history):** `/Users/sashajh2/Kognitos/golem/specs/migration-step-1-data-collection-template.md` and `step-1-data-collection-template-UPDATED-MAY-6.md`. The merged spec superseded both.

### Where to start reading

1. This file (HANDOFF.md)
2. `CLAUDE.md` — conventions
3. `specs/migration-step-1-data-collection.md` — current Step 1 runbook
4. `specs/migration-step-2-3-combined.md` — current Step 2-3 runbook (heavily edited; Phase B is the recent rework)

---

## 2. What was accomplished

### 2.1 Merged Step 1 spec

Old state: two competing specs in `golem/specs/`:
- `migration-step-1-data-collection-template.md` (UI-only, editor-walking)
- `step-1-data-collection-template-UPDATED-MAY-6.md` (API-first, draft proposal)

New state: one canonical spec at `specs/migration-step-1-data-collection.md`. API-first with UI required inline for FILE binaries + `__large_value_*` resolution. Editor-walking fallback in Appendix A for full API outages.

### 2.2 Phase 0 (Hydration) — autonomous KLang capture

Before: SE manually copy-pasted KLang from Chrome into `.txt` files, took screenshots of `[md*]` references, ran an LLM curation step. Seven placeholders to fill before invoking the agent.

After: SE provides **one URL**. Agent:
1. Parses dept/proc IDs from the URL.
2. Opens editor in Playwright (pauses for SSO if needed).
3. Copy-captures orchestrator KLang via the Slate editor's own copy serializer (`#slate-editor`, bubble-phase listener, single-call eval — see §3 below for the painful details).
4. Static regex on the captured text → list of child procedure IDs (`run @{"value":"<id>"}` references).
5. For each child: navigate, copy-capture, recurse.
6. Writes `_hydration.json` manifest + one `.txt` per stage in `klang/`.

**Verified live on 3 automations** in the user's department:
- `create customer payment` (290 lines, 18,343 chars, 11,775 px tall editor)
- `to create a sales order` (166 lines, 10,846 chars)
- `Update the Case` (64 lines, 2,119 chars)

All matched manual copy-paste byte-for-byte. The orchestrator case actually came out **one line MORE complete** than manual paste (human truncated `the usecaseNumber` at the bottom).

Three-tier fallback documented:
- **Tier 1 (primary):** Playwright copy-capture
- **Tier 2 (fallback):** GraphQL API render via parent-chain walk
- **Tier 3 (last resort):** user-paste prompt with explicit save path

Tier 2 and Tier 3 are spec'd but **not exercised**. See "Untested code paths" in §5.

### 2.3 Reliability cluster (B + C + F)

Added to `specs/migration-step-1-data-collection.md`:

- **B. Idempotency precheck.** If `klang/stage<N>_<slug>.txt` exists and passes sanity check, skip the navigate + capture for that stage. Mark `klang_source: "cached"` in `_hydration.json`. Same pattern in Phase C (skip already-captured representative runs).
- **C. Phase C.0 preflight.** Before any per-run deep capture (which is 1-5 minutes per run × ~10 runs), do a 30-second smoke test: JWT auth, exec-data fetch, S3 download. Fail-fast with specific error messages.
- **F. Schema validation.** Six JSON Schemas in `schemas/`. `tools/validate.py` walks an output dir and validates every known file. Spec requires running validation at end of each phase.

### 2.4 Phase B (SPy iteration) rework — D + E

Added to `specs/migration-step-2-3-combined.md`:

- **D. Plan-first Quill (Pattern 1).** Every Quill interaction is two-turn: ask for plan as text → orchestrator validates → ask to implement. Applied at initial authoring AND every fix iteration. `plan_v<N>.md` saved per turn.
- **E. Exception-feedback loop (Pattern 2).** When V2 run fails or pauses with an exception, fetch the Kognitos exception thread via Nexus (`kognitos_inspect_exceptions` → `list_events`) and use it as fix-context for Quill. Read-only: do NOT auto-reply via `kognitos_reply_to_exception`.

**Critical asymmetry documented:**
- V1 runs = legacy `app.kognitos.com` tenant. Nexus can't reach. Phase 1 captures via GraphQL `getSentenceExecutionData`.
- V2 runs = dev cluster. Reachable ONLY via Nexus. No GraphQL fallback for V2.
- V1 and V2 lineIds DO NOT MATCH (rewritten SPy → new KLang hashes). Diff aligns by **predicate text + binding name + SOP branch label**, never by lineId.

**Iteration cap:** 3 turns without convergence → mark `blocked`, surface to user.

**Replay tool (Thread A) deferred:** spec defines the diff JSON shape; today inline-computed via Bash/Python + Nexus calls; later swappable for `tools/replay_diff.py` with the same output schema.

### 2.5 Notion page updates (live)

Page: https://www.notion.so/kognitos/Agentic-Automation-Migration-Workflow-342281a74b6181478f8bfdde60a970b6

- Replaced `## 0) Data Preparation` (manual scrape + screenshots + LLM curation) with `## 0) Setup` (one-time machine setup: clone repo, confirm Claude Code + MCPs, confirm SSO).
- Replaced `## 1) Data Collection` (old Claude Code prompt with 7 placeholders) with a new `## 1) Data Collection` (one-URL input, what-you-get-back tree, recommended human checkpoint after KLang capture, pause-and-ask scenarios, time expectations, background phase mapping).
- Added explanation of `_hydration.json`.
- Added "required MCPs" note (Playwright, Nexus, optional Notion).
- **Did NOT touch:** "What this page is for" header, Quick Resource Index, Step 2-3 sections (those still reference old paths/concepts; flagged as polish items).

### 2.6 Repository creation + spec migration

- Created `~/kognitos-migration-assets/` as the canonical home.
- Moved `migration-step-1-data-collection-merged.md` → `specs/migration-step-1-data-collection.md` (renamed, dropped `-merged` suffix).
- Moved `migration-step-2-3-combined-template.md` → `specs/migration-step-2-3-combined.md`.
- Left older drafts in `golem/specs/` as historical reference.
- `git init` + commits + pushed to `https://github.com/sasha-kog/migration-assets` (private).
- Could NOT push to `kognitos/migration-assets` because the `sasha-kog` account lacks org-level repo-creation permission. **Pending: org admin transfers `sasha-kog/migration-assets` → `kognitos/migration-assets` via GitHub Settings → Transfer ownership.**

### 2.7 Commit history (in migration-assets repo)

```
002dd9a  Phase B rewrite: plan-first Quill + exception-feedback loop
85b9a9d  Reliability cluster: idempotency, smoke test, schema validation
608f914  Add notion/ paste-ready drafts for Step 0 + Step 1 rewrite
717c0e6  Spec edits: clarify Step 0.6, add user-paste fallback, rewrite Phase B intro
33083da  Move specs into repo; update cross-references
10a1844  Initial commit: README, CLAUDE.md conventions, run_capture template, example filled capture
```

---

## 3. Key technical findings (don't rediscover these)

### 3.1 Playwright Slate copy-capture — the brittle parts

The Kognitos editor is **Slate.js**. CSS selector for the editor container: `#slate-editor` (class `slate-editor-PROCESS`). It has `contenteditable="false"` at the top level, which is unusual — Slate manages its own selection internally.

**The single most important rule, learned by failing twice:** the `copy` event listener install, selection, copy command, AND read MUST run in ONE synchronous `browser_evaluate` call. Splitting across two calls returns empty captures inconsistently. The failed pattern looked like:

```js
// CALL 1
window.__captured = null;
document.addEventListener('copy', (e) => {
  window.__captured = e.clipboardData.getData('text/plain');
}, { capture: false });
```
```js
// CALL 2
const ed = document.querySelector('#slate-editor');
const range = document.createRange();
range.selectNodeContents(ed);
const sel = window.getSelection();
sel.removeAllRanges();
sel.addRange(range);
document.execCommand('copy');
return window.__captured;
```

This worked on `Update the Case` and returned empty on `to create a sales order`. **Reason:** Slate seems to detach/reattach its own listeners on focus changes, and the listener registration order changes which order our handler fires in relative to Slate's. A single synchronous block fires both in deterministic order.

**The correct pattern (PINNED in the spec, Step 0.4):**

```js
() => {
  // 1) Install bubble-phase listener (not capture phase — Slate writes in bubble phase)
  window.__captured = null;
  document.addEventListener('copy', (e) => {
    window.__captured = e.clipboardData.getData('text/plain');
  }, { capture: false });

  // 2) Select all editor content
  const ed = document.querySelector('#slate-editor');
  const range = document.createRange();
  range.selectNodeContents(ed);
  const sel = window.getSelection();
  sel.removeAllRanges();
  sel.addRange(range);

  // 3) Trigger copy
  document.execCommand('copy');

  // 4) Return in same call
  return window.__captured;
}
```

**Why bubble phase, not capture phase:** Slate's own copy handler runs in bubble phase and writes to `clipboardData.setData()`. If we register in capture phase, we read clipboardData BEFORE Slate writes it → empty. Verified via a diagnostic listener that returned `types: []` at capture phase and `types: ["text/plain"], length 10846` at bubble phase for the same event.

### 3.2 Three-automation virtualization test result

All three test automations had `scrollHeight === clientHeight` on `#slate-editor`. So no internal scroll, no DOM virtualization — Slate rendered every line. Untested beyond 11,775 px (the largest of the three). Worth re-testing on a very long automation before the next migration; spec's sanity check at Step 0.4 acts as a tripwire if a large automation truncates.

### 3.3 KLang capture: copy-paste beats DOM scrape

DOM `innerText` on `#slate-editor` returned 10,800 chars. Copy-capture returned 18,343 chars for the same automation. Difference: the editor renders `[md*]` placeholders as the bracket-token (which is what `innerText` reads), but the Slate copy serializer resolves them to the full markdown body. **For migration purposes, the copy serializer's output is what we want** — the rule bodies, koncierge prompts, and `[link]` resolutions are all inline.

### 3.4 Sub-automation discovery — static regex is enough

The orchestrator's KLang text contains every named child procedure invocation as:
```
run @{"type":"procedure","display":"Update the Case","value":"6szk1unn9661xjtf9uhpflrja"} with
```

Regex `run @\{[^}]*"value":\s*"([a-z0-9]+)"` over the captured KLang text extracts every child procedure ID. No need to walk run data to discover children. The agent navigates to each child's editor URL (`https://app.kognitos.com/department/<DEPT>/processes/<CHILD_ID>?stage=PUBLISHED`), recurses.

**Caveat:** `miniPlaygrounds` (embedded `extract data from the document` blocks) and loop bodies (`process each <item> as follows`) do NOT show up as `run @{...}` references. Their parameters are captured as child lines of the parent line in the editor copy. Phase 0 forward-signals these to Phase C in `_hydration.json` under `runtime_only_blocks` — they manifest fully only when a run executes.

### 3.5 GraphQL endpoints used in Phase 1

```
POST https://api.app.kognitos.com/v2/app-production-k8s/graphql?op=<operationName>
Authorization: <JWT>            ← literal token, NO "Bearer" prefix
```

JWT = the ID token Chrome's app sends. Lifetime ~24h.

Key ops:
- `listProcedureGroupsByDepartmentv2(departmentId)` — every procedure in a dept with `id`, `name`, `publishedProcedure.latestRunData.id`. Used by Phase 0 Tier 2 to look up the latest run for each procedure (since `getWorkerDocument` requires a runId).
- `ListWorkersByProcedure(procedureId, departmentId, stage="PUBLISHED", limit=...)` — runs list for one procedure. Phase B.1.
- `getWorkerDocument(workerId, documentToken="")` — sentence list (= KLang) for one document. Phase B.2 and Phase 0 Tier 2.
- `getSentenceExecutionData(workerId, documentToken, token)` — per-line exec data for one run. Phase B.3 + Phase C.

Real example response shapes captured in the spec (see "Worked examples" in `specs/migration-step-1-data-collection.md`).

### 3.6 What's UNTESTED but spec'd

These code paths are in the spec but were not exercised:
- **Phase 0 Tier 2 (API render).** Spec'd; not run end-to-end. Will activate the first time Playwright copy-capture's sanity check fails for a stage.
- **Phase 0 Tier 3 (user paste).** Spec'd; not run.
- **JWT auto-fetch.** Spec'd. JWT is only needed in Phase B onward; we never reached Phase B in testing. First Phase B run will exercise this.
- **Phase B + C entirely.** Not run since the rework. The Phase B rewrite (D + E patterns) is design-only.
- **Phase D aggregate.** Not run.
- **`validate.py`** smoke-tested on a hand-crafted `_hydration.json` (passed valid + correctly failed an invalid example with the right error path) but not on real Phase 0 output yet.

---

## 4. File map quick reference

| File | Purpose | State |
|---|---|---|
| `specs/migration-step-1-data-collection.md` | Step 1 runbook (Phases 0/A/B/C/D) | Current. Phase 0 tested live; B/C/D spec'd but unrun. |
| `specs/migration-step-2-3-combined.md` | Step 2-3 runbook (SOP + SPy iteration) | Recently rewritten Phase B (plan-first + exception-feedback). Untested. |
| `CLAUDE.md` | Conventions auto-loaded by agents in this dir | Stable |
| `README.md` | Repo overview | Stable |
| `run_capture_template.md` | Skeleton for `run_capture_filled.md` | Stable |
| `example_filled_capture/` | Canonical example | Stable (pre-Phase-0 era; flagged in its README) |
| `schemas/*.schema.json` | JSON Schemas for output files | Stable |
| `tools/validate.py` | JSON validator | Smoke-tested on synthetic data |
| `notion/*.md` | Paste-ready Notion drafts | Already applied to Notion page |

---

## 5. Open items / next steps (prioritized)

### 5.1 Org transfer (one-line; needs an admin)

`sasha-kog/migration-assets` → `kognitos/migration-assets`. The `sasha-kog` account lacks org-level repo-creation permission, so an admin (likely Daniel) needs to do this via GitHub UI:

1. Settings → "Transfer ownership" → enter `kognitos`.
2. Org owner accepts.
3. After transfer, update the local clone's remote:
   ```bash
   cd ~/kognitos-migration-assets
   git remote set-url origin git@github.com:kognitos/migration-assets.git
   ```
4. Update the spec's Phase 0 prereq line (currently still says `git@github.com:kognitos/migration-assets`) — should still be correct after transfer.

### 5.2 Test plan for the new Phase B loop (HIGH priority)

The plan-first + exception-feedback loop (commit `002dd9a`) is design-only. Validate by:

1. Pick a recent painful migration with multiple Quill iterations. Candidates in `plunkett/`:
   - `create_credit_memo/spy_iterations/` (has at least `may_5_pre_sync_sop.md` plus pre-existing versions)
   - `create_sales_order/spy_iterations/spy_v1` through `spy_v8` — eight iterations, clearly painful
2. Set up an iteration on the dev cluster using one of the captured V1 runs (`create_sales_order/feb5_7pm/` or `mar5_5pm/`).
3. Run one full cycle of the new loop:
   - `kognitos_invoke_automation(v2_draft, input=<reference.attachment>)`
   - Poll status
   - On `done`: compute diff (Nexus `kognitos_runs(list_events)` + load V1 trace from disk + normalize both sides by predicate text)
   - On exception: pull bundle (`kognitos_inspect_exceptions` chain)
   - Construct fix prompt → Quill plan-first → validate → implement
4. Compare to the historical iteration outputs (`spy_v1..v8`). Did plan-first catch direction errors earlier than the historical flow? Did exception context shorten the loop?

Success criteria: a previously 4-iteration fix now lands in 2. Anything less is worth investigating before next migration.

### 5.3 Untested code paths to exercise on next migration

- Phase 0 Tier 2 (API fallback) — force a failure (e.g., a test automation Slate doesn't render correctly) and verify the fallback completes.
- Phase 0 Tier 3 (user paste) — force both prior tiers to fail and verify the prompt is clear.
- JWT self-fetch from Playwright profile — verify it works end-to-end the first time Phase B runs.
- Phase C.0 preflight — confirm the 30-second smoke test actually catches the failure modes documented.
- `validate.py` on real Phase 0 output — should be the first thing run after the next migration's Phase 0.

### 5.4 Thread A — Replay harness + structured diff tool (medium effort)

Build `tools/replay_diff.py`:

Inputs:
- Path to V1 run folder (contains `stage<N>_branch_trace.json` and `run_capture.json`)
- V2 run ID (on dev cluster)

Outputs:
- `iteration_<N>_diff.json` per the schema in `specs/migration-step-2-3-combined.md`

Procedure (already documented in the spec):
1. Load V1 trace from disk.
2. Fetch V2 events via Nexus `kognitos_runs(list_events, run_id)`.
3. Normalize both to: `{branch_decisions, named_bindings, child_invocations}` keyed by predicate text / binding name / SOP branch label (NOT lineId — they differ between V1 and V2).
4. Compute mismatches + extras + missing.
5. Apply `near-current` tolerance filtering from `stages_comparability_reasons`.
6. Compute handoff payload diff via `kognitos_runs(get_run_outputs)`.
7. Write JSON to expected path.

Size: ~150 lines of Python. Roughly same shape as `validate.py`.

When this lands, the spec's inline-diff procedure becomes a one-line tool invocation. No spec re-edit needed; the spec already says "swap inline for the tool when present."

### 5.5 Polish items (low priority but high impact ROI)

- **G. `_hydration.md` companion** to `_hydration.json` — human-readable summary written alongside the JSON at Phase 0.9. SE scans markdown instead of parsing JSON.
- **H. Branch coverage threshold gate** — `_branch_triage.json` already produces `coverage_gaps`. Add: agent stops at end of Phase B if `coverage_gaps > N%` (default 30%) and asks for sign-off or sample expansion. Prevents Phase C from running on inadequate data.
- **I. KLang version diff helper** — when `_klang_version_evolution.md` is required, auto-generate a sentence-level diff per stage (added lines, removed lines, flipped predicates). Currently the spec just says "document the differences."

### 5.6 Notion polish (small)

Things flagged but not done:
- "What this page is for" still says `1. Data preparation, 2. Data collection, ...` — should be `1. Setup, 2. Data collection, ...`.
- Quick Resource Index still references `golem/specs/migration-step-1-data-collection-template.md` (outdated path).
- Common Gaps to Watch first bullet ("KLang scrape misses indentation...") — obsolete.
- Migration Completion Checklist first item ("Curated KLang produced from scrape + screenshots") — obsolete.

### 5.7 Strategic / longer-term

- **J. Shared completed-migrations repo** — each finished migration becomes a folder in `kognitos-migrations-completed`. Future migrations grep for similar branch structures.
- **K. Quill prompt library** — vetted templates for common patterns (extract-and-classify, if-else decision tree, retry-with-different-source). Plan-first authoring uses these as starting points.
- **L. Migration metrics dashboard** — track wall-clock time per phase, common failure modes, recurring branches. Premature until 5-10 migrations have been completed under the new flow.

---

## 6. Things that bit me (gotchas)

In order of pain:

1. **Bubble phase vs capture phase for the `copy` event listener.** Spent the first 3 attempts at copy-capture returning empty data. Slate writes `clipboardData` in bubble phase; if you register in capture phase, you read empty. Fixed by `{ capture: false }`.

2. **Two-call vs single-call browser_evaluate.** Even with bubble phase, splitting listener-install and copy-trigger across two `browser_evaluate` calls returned empty intermittently. Always put the full pattern in one synchronous block.

3. **V2 lineIds ≠ V1 lineIds.** I initially wrote the diff path to align by lineId. The user corrected: V2 SPy is a rewritten automation with new KLang hashes, so lineIds don't match. Diff has to align by **predicate text + binding name + SOP branch label**. Fixed in commit `002dd9a`.

4. **Nexus can't reach the V1 tenant.** V1 lives on `app.kognitos.com` (legacy). Nexus targets the dev cluster. V1 data is always GraphQL-fetched (already what Phase 1 does); V2 data is always Nexus-fetched.

5. **`sasha-kog` doesn't have repo-creation perms in the `kognitos` org.** First push attempt to `kognitos/migration-assets` failed with `permissions to execute CreateRepository`. Pushed to `sasha-kog/migration-assets` instead, transfer pending.

6. **Wrong Notion page ID typo.** First Notion edit attempt used `342281a7-4b61-8147-8f8f-bdde60a970b6`; correct ID is `342281a7-4b61-8147-8f8b-fdde60a970b6` (note `8f8b-fdde`). Fixed by retrying.

7. **Notion XML tables vs Markdown pipe tables.** Notion's enhanced-markdown spec says use `<table>` XML. In practice, pipe tables also work (just auto-converted). Used pipe tables for the Notion drafts and they rendered fine.

8. **Step 0 partial replacement.** First edit only matched through 0.0 (Chrome copy-paste preamble); the JavaScript scrape (0.1), screenshots note (0.2), LLM curation prompt (0.3) remained as orphans. Cleaned up in a second edit.

---

## 7. Useful prior context (from user's auto-memory)

These influenced session choices:

- **V1 lives on legacy `department/...` tenant the MCP can't reach** → KLang capture path is browser-based, not MCP. Fixed; documented in Step 1 spec.
- **Quill authoring: stub then branches, never the whole automation in one turn** → maps to Pattern 1 (plan-first) in the new Phase B spec.
- **Quill send-message bypass for Nexus 1.17.0** (`plunkett/quill_send_message.sh`, te:trailers header, :stop verb) → relevant if next agent needs to send Quill messages manually outside MCP.
- **PR descriptions: results first, methodology brief** → applied in commit messages.
- **jarvis gitlint regex gotchas** (no `#` in commit body, lowercase `Co-authored-by`) — kept commit messages safe.

---

## 8. Quick-start commands for next session

```bash
# Get to the work
cd ~/kognitos-migration-assets
git pull

# Validate any output you have
python3 tools/validate.py ~/some-migration-output-dir

# See what's in the spec
$EDITOR specs/migration-step-1-data-collection.md
$EDITOR specs/migration-step-2-3-combined.md

# Run a migration end-to-end (after Notion Setup is done)
# In Claude Code:
#   Read this spec as your instructions:
#     ~/kognitos-migration-assets/specs/migration-step-1-data-collection.md
#   Execute end-to-end data collection for the automation at:
#     <ORCHESTRATOR_PUBLISHED_URL>
```

---

## 9. Recommended first action for the next agent

If you're picking this up cold, **don't immediately tackle Thread A / replay harness**. The highest-value next action is:

**Run one full Phase B iteration with the new D + E pattern on a real migration** (§5.2). This validates the most recently rewritten part of the workflow before more is built on top of it. If plan-first or exception-feedback turns out to need adjustment, easier to find out now than after Thread A is built around assumptions about how the loop works.

After that, the org transfer (§5.1) unblocks team adoption. Then Thread A.

---

End of handoff. Questions to the previous agent's user (sasha@kognitos.com) — but most things should be answerable from the spec + this doc + commit history.
