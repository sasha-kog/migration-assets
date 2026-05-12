# kognitos-migration-assets

Shared assets for Kognitos V1 → V2 automation migrations.

## What this repo is

The canonical home of the Kognitos V1 → V2 automation migration workflow. Holds the runbook specs Claude Code agents read, plus the reference assets they consume (templates, example filled captures). Versioned via git so any teammate on any machine has the same workflow.

## What's in it

| Path | Used by | Purpose |
|---|---|---|
| `specs/migration-step-1-data-collection.md` | Step 1 agent | Runbook for KLang collection + branch enumeration + run captures (Phases 0/A/B/C/D) |
| `specs/migration-step-2-3-combined.md` | Step 2-3 agent | Runbook for SOP drafting + SPy iteration (Phases A/B) |
| `run_capture_template.md` | Step 1 agent | Generic skeleton an SE/agent adapts per automation; defines the section structure for `run_capture_filled.md` |
| `example_filled_capture/` | Step 1 agent | One real, completed run capture from a past migration. Agents read this as a structural model for the level of detail expected. |
| `CLAUDE.md` | Any Claude Code agent in this directory | Conventions: slug naming, default output dirs, auth, editor selector |

## How to use

Clone once per machine:

```bash
git clone git@github.com:kognitos/migration-assets ~/kognitos-migration-assets
```

`git pull` before starting a migration to pick up updates.

Pass one of the specs to Claude Code as instructions, plus the orchestrator's published-process URL. Phase 0 derives everything else (department/procedure IDs, KLang per stage, output directory).

## Adding to this repo

Append-only. If you have a particularly good filled capture from a recent migration, add it as a sibling folder under `examples/` (separate from `example_filled_capture/`, which stays as the canonical one referenced by the spec). PR with a note about which automation and what was good about it.
