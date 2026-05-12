# Step 1: Data Collection

Goal: produce a `<automation_slug>/` directory containing the orchestrator's KLang, every sub-automation's KLang, a branch catalog, and one representative production run per major branch — all from a single automation URL.

This replaces the old "Step 0: KLang collection" and "Step 1: Run captures" — collapsed because the agent now handles KLang fetching automatically.

## What you give the agent

Just the orchestrator's published-process URL. Example:

```
https://app.kognitos.com/department/d6j8mv1c12a9n3itm7msneli4/processes/8rroj6z8d6lrmgr0b44p4bebr?stage=PUBLISHED
```

Everything else is derived: department ID, procedure ID, automation name, output directory name (`<automation_slug>/`), list of sub-automations, branch catalog.

## What you get back

```
<automation_slug>/
├── _hydration.json              ← summary of what was derived
├── klang/
│   ├── stage0_<orchestrator>.txt
│   ├── stage1_<child>.txt
│   └── stage<N>_<child>.txt     ← one per sub-automation
├── branch_catalog.md            ← human-readable branch matrix
├── branch_catalog.json
├── run_captures/
│   ├── _orchestrator_runs_index.json
│   ├── _branch_triage.json      ← which run represents each branch
│   ├── _capture_index.json      ← aggregated view for Phase 2-3
│   └── <YYYY-MM-DD_HH-mm>_<run_id>/   ← one folder per representative run
│       ├── run_capture_filled.md
│       ├── run_capture.json
│       ├── attachment.<ext>     ← input file binary
│       └── stage<N>_branch_trace.json
```

## Run it

Paste this prompt into Claude Code (replace the URL):

```text
Read this spec as your instructions:
  ~/kognitos-migration-assets/specs/migration-step-1-data-collection.md

Execute end-to-end data collection for the automation at:
  <PASTE_ORCHESTRATOR_PUBLISHED_URL>

Use defaults for everything (output directory will be <automation_slug>/
in the current working directory). Stop and ask if anything is unclear or
if a step fails.
```

Optional overrides:
- **Output directory** — pass `<OUTPUT_BASE_DIR>=path/to/dir/` if you don't want the default `<automation_slug>/` in cwd.
- **JWT** — only needed if Playwright auto-capture fails. The agent will prompt you when it needs one.

## Recommended human checkpoint (after KLang capture, before branch enumeration)

The agent works in phases. The first phase (Hydration) produces:
- `_hydration.json`
- One `.txt` per stage in `klang/`

**Spot-check these before letting the agent enumerate branches.** Open each `klang/stage<N>_*.txt`, scroll to the bottom, confirm:
- File ends at the last expected line (not truncated mid-token)
- Indentation looks right (nested `if` blocks have visible 2-space indent)
- Extraction rules and koncierge tasks are fully expanded (look for `the first field's rule is """..."""`, the rule body should be inline, not a placeholder like `[md2]`)
- All child automations you'd expect are present (one `.txt` per sub-procedure)

If anything looks off, tell the agent — it can re-capture the affected stage. Don't proceed if KLang is incomplete; branch enumeration and run triage downstream depend on it being right.

## When the agent will pause and ask

The agent runs autonomously after the URL is given, but it pauses for:

| Situation | What it asks |
|---|---|
| First-time editor load → SSO login | "Please log in to app.kognitos.com in the Playwright window. Type 'ok' when done." |
| Both Playwright capture and API fallback failed on a stage | "Auto-capture failed for stage `<N>` (`<name>`). Open `<URL>`, copy the KLang (Cmd+A, Cmd+C), save to `<path>`, reply 'done'." |
| JWT needed for API operations and not in env | "I need a JWT for `api.app.kognitos.com`. DevTools → Network → graphql → copy `authorization` header. Paste it here." |
| Coverage gap (a branch has no representative run in the sample) | "Branch `<X>` has 0 candidate runs in the last 200. Expand the window, accept the gap, or revise the branch catalog?" |
| File binary download failed | "Couldn't download the input file for run `<id>`. Open the run, click the file, save it to `<path>` as `attachment.<ext>`." |

Everything else runs without intervention.

## Time expectations

For a typical pipeline with 1-2 sub-automations and ~10 branches:

| Phase | Wall clock |
|---|---|
| Hydration (KLang per stage) | ~30 seconds after login |
| Branch enumeration | ~1 minute |
| Run triage (fingerprint 100 runs in parallel) | ~30 seconds |
| Deep capture per representative run | 1-5 minutes per run; ~10 runs total |
| Aggregate index | ~10 seconds |

Total: ~30-60 minutes for the typical case, dominated by Phase C deep captures and UI work (FILE binaries, large-value resolution).

## When to ping for help (not the agent — a human)

- The agent has paused for more than 10 minutes on a single step
- It's asking the same question twice
- The KLang spot-check turns up obvious truncation (file ends mid-line, missing closing `then`)
- A sub-automation you know exists isn't in `_hydration.json`
- The branch matrix has many gaps and you don't know whether to expand the sample window

Ping Sasha or post in `#migrations`.

## What this step does NOT do

- Draft the SOP (that's Step 2)
- Rewrite the automation in V2 SPy (that's Step 3)
- Touch any V2 systems

It's pure read-only data collection. The output feeds Step 2-3.

---

### Background (skip on first read)

What the agent does internally, in case you want to debug or read the spec:

| Phase | Purpose | Spec section |
|---|---|---|
| 0 — Hydration | URL → everything else (IDs, name, KLang per stage) | `specs/migration-step-1-data-collection.md` — Step 0.x |
| A — Branch enumeration | KLang → branch matrix | Phase A |
| B — Run discovery + triage | Find one representative run per branch | Phase B |
| C — Per-run deep capture | Full traces + input binaries per representative | Phase C |
| D — Aggregate | Index everything for Phase 2-3 | Phase D |

The phase boundaries are internal; you don't see them as separate steps. The only checkpoint that matters at the SE level is the KLang spot-check after Phase 0.
