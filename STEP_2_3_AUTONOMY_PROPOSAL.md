# Step 2-3 Autonomy Proposal — Improvements Triage

**Date:** 2026-05-14
**Author:** agent (for sasha@kognitos.com review)
**Related:** `HANDOFF.md` (overall project), `STEP_2_3_IMPROVEMENTS.md` (prior agent's work queue), `specs/migration-step-2-3-combined.md` (current spec)

## Goal

The ideal Phase B exit is one of exactly two states:

1. **Parity reached** — V2 SPy produces the same trace + handoff payload as the V1 reference, for every parity-quality branch.
2. **Real blocker** — platform bug, missing/broken book procedure, or a Quill expressiveness limit. SE intervention is genuinely required.

Anything else (Quill spinning, mis-classified failures, fix-loops on wrong root cause) is a defect in the loop, not an unavoidable intervention.

The current spec defines the right *categories* (`book_missing`, `book_broken`, `spy_pattern_limitation`, `platform_bug`, `v1_data_insufficient`, `sop_ambiguity_unresolvable`, `parity_reached`) but the **detection logic** is hand-wavy enough that the SE will be pulled in on false alarms, or asked to babysit slow-converging loops. This doc proposes 12 changes to tighten that, ranked by effort × impact.

---

## What Phase B does today (current spec, summary)

Per `(stage, branch)`:
1. Pick reference run (`current` preferred, `near-current` tolerated with documented divergences).
2. `kognitos_invoke_automation(v2_draft, input=<reference.attachment>)` → poll status.
3. Branch on outcome:
   - `done` → **diff path**: V2 events from Nexus `list_events`, normalized vs V1's `stage<N>_branch_trace.json`, aligned by *predicate text + binding name + SOP branch label* (no shared lineId — V2 has no KLang).
   - `failed` / `waiting_for_user_input` → **exception path**: pull `inspect_exceptions(get / list_events / get_guide)`. The Kognitos resolution agent's reasoning becomes Quill fix-context. **Currently read-only — no `reply_to_exception`.**
4. **Plan-first Quill** (Pattern 1): text plan → orchestrator validates against branch matrix + verbatim predicates → implement.
5. Re-run. One change per iteration.
6. **Terminal classification** → `migration_outcome.json` with one of the 7 outcomes.

Three patterns from the recent rework (D, E, terminal-states) are **untested on a real migration**. The Plunkett 21-iteration baselines (`create_sales_order`, `create_customer_payment`) predate them.

---

## The 12 improvements (with leverage)

Scoring:
- **Impact** — does it materially push the system toward "intervene only on real blockers or parity"?
- **Effort** — implementation + design + validation cost.

| # | Improvement | Impact | Effort | Cluster |
|---|---|---|---|---|
| 1 | Workspace book-inventory preflight | High | Low | **Up-front** |
| 2 | Interactive Astral path (exception resolution) | High | Medium | **Discuss first** |
| 3 | Book-contract check in loop | High | Medium | **Discuss first** |
| 4 | Diff-shape monotonicity tracker | High | Low-Med | **Up-front** |
| 5 | Plan-validation strictness | Medium | Low | **Up-front** |
| 6 | Cross-iteration loop detection | Medium | Low | **Up-front** |
| 7 | `tools/replay_diff.py` (Thread A) | Medium | Medium | Defer |
| 8 | Branch coverage threshold gate | Medium | Low | **Up-front** |
| 9 | SOP jargon cleanup (Phase E) | Medium (UX) | Med-High | Separate track |
| 10 | Known-book-bugs registry | Medium (compounding) | Medium | **Discuss first** |
| 11 | `_telemetry.json` per migration | Low immediate / High compounding | Low | **Up-front** |
| 12 | KLang version-diff helper | Low for Phase B | Medium | Defer |

### Detail per item

#### 1. Workspace book-inventory preflight
- **Today:** `book_missing_procedure` surfaces only after Quill's plan asks for a verb no installed book exposes — i.e., mid-loop, after the SE has watched at least one full iteration.
- **Change:** Before iteration #1, enumerate books referenced in captured KLang (Step 1 output) and confirm each is installed + authorized in the target workspace via `kognitos_books(list)`. Write `workspace_book_inventory.json` (required / installed / missing). If any are missing, fail-fast as a Phase B gate.
- **Why now:** turns a class of mid-loop failure into a pre-flight failure. Zero risk to spec; purely additive.
- **Effort:** ~50 lines + small spec section.

#### 2. Interactive Astral path
- **Today:** spec is read-only on `kognitos_reply_to_exception`. Exception resolution agent's reasoning is used as fix-context for Quill but never engaged interactively.
- **Change:** When a V2 run pauses on an exception, attempt **one** strict round-trip with Astral: reply with the V1 ground-truth for the failing line (predicate text + expected binding values from V1's trace). If Astral resolves the exception in that one reply, the run completes and we go directly to the diff path — potentially achieving parity without a Quill iteration. If not, fall back to read-only fix-context and treat the failed Astral round-trip as additional context in the Quill plan.
- **Why now:** Astral round-trips might be the cheapest path to parity for whole classes of errors (missing context, ambiguous bindings). This is the only proposed change that touches the read-only invariant in the spec, so it needs explicit go-ahead.
- **Risk:** circularity (Astral's interactive reply influences future Astral runs on the same exception) and side effects (advancing the run mutates state). Mitigations: one reply per exception; the reply content is mechanical V1 ground truth, not agent reasoning; capture before/after exception state for audit.
- **Effort:** medium. Mostly design (reply template, audit shape, fall-through semantics).

#### 3. Book-contract check in loop
- **Today:** `book_broken_procedure` requires 2 identical iterations with no SPy change on the failing line.
- **Change:** When a book proc invocation fails, fetch its contract via `kognitos_books(get_procedure)` and compare: (a) does the SPy call match the documented signature? — if not, this is a SPy bug, keep iterating with that info; (b) does the proc's *output* match its documented contract? — if not, classify `book_broken_procedure` on iteration 1, not iteration 2.
- **Why now:** halves the iteration cost of book bugs and gives clearer evidence (contract diff) in the blocker payload.
- **Effort:** medium. Needs a small contract-diff routine.

#### 4. Diff-shape monotonicity tracker
- **Today:** `spy_pattern_limitation` triggers at "5 iterations with diff shape changing but not shrinking" — vibe-based.
- **Change:** Track concrete metrics across iterations: `|predicate_mismatches| + |value_mismatches| + |extra_v2| + |missing_v2|`, and the *set* of predicates/bindings in mismatches. Classify limitation if total is non-decreasing for 3 iterations AND the mismatch set keeps changing (i.e., Quill is shuffling). Persist as `iteration_diff_shape.json` so SE sees the evidence.
- **Why now:** removes a hand-wavy criterion; will materially reduce the floor of wasted iterations once Quill stops converging.
- **Effort:** low-medium. Lives in the orchestrator's already-existing diff code.

#### 5. Plan-validation strictness
- **Today:** Pattern 1 says "orchestrator validates the plan" — checks are described in prose but not codified.
- **Change:** Make Turn-1.5 mechanical. For each plan:
  - Every branch in `sop_branch_matrix.md` for this stage appears in the plan.
  - Every predicate in the plan is a verbatim substring of the captured KLang text.
  - Handoff fields enumerated and match `<HANDOFF_FIELDS>`.
  - No introduction of sub-process invocations not present in V1.
  Reject (with specific objections) on any failure; require a plan revision.
- **Why now:** reduces "plan reads fine, SPy is broken" cases — the cheapest way to compress iteration count.
- **Effort:** low. Pure orchestrator-side, no MCP work.

#### 6. Cross-iteration loop detection
- **Change:** If iteration `N`'s diff equals iteration `N-2`'s diff (same mismatches, same direction), Quill is oscillating. Force a prompt variant or escalate rather than continuing to `N+1`. Detection key: hash of `(sop_branch, predicate_text/binding_name, direction)` set.
- **Why now:** prevents the obvious "iteration 4 looks like iteration 2" loops that the user has historically had to spot manually.
- **Effort:** low. Small extension of #4.

#### 7. `tools/replay_diff.py` (Thread A)
- **Status:** spec'd; today the agent computes diff inline via Bash/Python.
- **Change:** ~150 lines of Python, same shape as `tools/validate.py`, outputs `iteration_<N>_diff.json` per the schema in the spec.
- **Why defer:** the inline approach works; this is hardening, not a feature. Pay the debt after ≥2 migrations through the new flow.

#### 8. Branch-coverage threshold gate
- **Today:** Phase A produces `accepted_risk` register, but there's no hard threshold — the gate can be bypassed silently.
- **Change:** End-of-Phase-A: if `(accepted_risk branches / total branches) > 30%`, stop and require SE sign-off or more captures. Prevents Phase B from running on inadequate evidence.
- **Effort:** low. Pure config + small Phase A check.

#### 9. SOP jargon cleanup (Phase E)
- **Status:** mentioned in SE meeting deck; not in spec.
- **Change:** After parity reached, dedicated pass to strip internal jargon from SPy comments + generated SOP (branch labels like `B5a`, internal placeholders `__large_value_*`/`[md*]`, stage nomenclature). Output is customer-facing.
- **Why separate track:** doesn't reduce interventions during Phase B; it's about artifact quality. Needs its own design (per-stage vs end, glossary, behavior-preservation re-diff).

#### 10. Known-book-bugs registry
- **Change:** `known_book_bugs.json` keyed by `(book_name, procedure_signature, error_pattern)`. After migration #1, classify repeat-offender book bugs on iteration 1 instead of waiting for #3's heuristic to fire.
- **Why discuss first:** compounding-value across migrations; depends on #3 (book-contract check) being in place to produce the registry entries in the first place.
- **Effort:** medium.

#### 11. `_telemetry.json` per migration
- **Change:** Record per-migration: iteration counts per (stage, branch), terminal state, wall-clock per phase, book-bug incidents, # Astral round-trips, # plan-validation rejections.
- **Why now:** doesn't help the in-flight run but enables calibrating every threshold in the spec (iteration caps, diff-shape thresholds, coverage threshold) once we have 5–10 runs. Cheap to add now; expensive to retrofit later.
- **Effort:** low.

#### 12. KLang version-diff helper
- **Change:** Auto-generate sentence-level diff per stage when `_klang_version_evolution.md` is required (added lines, removed lines, flipped predicates).
- **Why defer:** only matters when `near-current` captures dominate. Data from the next migration will tell us how often that's the case.

---

## Recommended up-front cluster

Implement before next migration, all low-effort, collectively high-impact:

- **#1** Workspace book-inventory preflight
- **#4** Diff-shape monotonicity tracker
- **#5** Plan-validation strictness
- **#6** Cross-iteration loop detection
- **#8** Branch-coverage threshold gate
- **#11** `_telemetry.json`

These together push the loop toward exiting on real signal (book gap, Quill cap, parity) instead of timeouts or vibe-based caps, and instrument what we don't yet know.

## Discuss before implementing

- **#2** Interactive Astral — changes the spec's read-only invariant. Needs explicit go-ahead. Highest upside but the only design-risky change in the list.
- **#3** Book-contract check — straightforward but dependency for #10.
- **#10** Known-book-bugs registry — wait for first migration with #3 to produce real registry entries.

## Defer

- **#7** `tools/replay_diff.py` — operational hardening, not blocking. Pay after ≥2 migrations.
- **#9** SOP jargon cleanup — separate track (output quality vs autonomy).
- **#12** KLang version-diff helper — wait for data showing it's needed.

---

## Open questions for sasha@kognitos.com

1. **#2 (Astral interactive):** any historical incidents of Astral writing back to a run in a way that broke reproducibility? If yes, that defines the audit shape we need before unlocking it.
2. **#4 thresholds:** is "3 iterations non-decreasing" calibrated right, or should we run with a softer "5 non-decreasing" until we have telemetry from #11?
3. **#5 plan validation:** should plan rejection count toward the iteration cap, or be free (since no V2 run was burned)?
4. **#8 coverage threshold:** 30% is a guess. Same calibration question as #4.
5. **#9 (SOP cleanup) timing:** per-stage as parity is reached, or once at the end across all stages? Currently no signal either way — needs SE input.
