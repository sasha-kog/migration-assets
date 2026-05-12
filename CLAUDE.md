# Conventions for migrations

Agent-facing instructions. Auto-loaded when Claude Code works in this directory.

## Where the migration workflow lives

The migration runbook lives in this repo under `specs/`:

- `specs/migration-step-1-data-collection.md` — Phase 0 (Hydration) + Phases A-D (data collection)
- `specs/migration-step-2-3-combined.md` — Phases A (SOP drafting) + B (SPy iteration)

When an agent is invoked for a migration, it reads one of those specs as its instructions. Other files in this repo (`run_capture_template.md`, `example_filled_capture/`) are referenced by absolute path from those specs (e.g. `~/kognitos-migration-assets/run_capture_template.md`).

## Output directory naming

- `<OUTPUT_BASE_DIR>` defaults to `<automation_slug>/` (relative to the user's working directory), **not** `plunkett/<automation_slug>/`. "Plunkett" is the customer name for one specific migration — it doesn't belong in the default path.
- `<automation_slug>` = `<AUTOMATION_NAME>` with: lowercase, non-alphanumeric → `_`, consecutive `_` collapsed. Examples:
  - `"create customer payment"` → `create_customer_payment`
  - `"to create a sales order"` → `to_create_a_sales_order`
  - `"Update the Case"` → `update_the_case`

## KLang capture path

Phase 0 produces one `.txt` per stage at `<OUTPUT_BASE_DIR>/klang/stage<N>_<child_slug>.txt`. Stage 0 = orchestrator. Stages 1+ = child procedures discovered by static regex over the orchestrator's KLang.

## Auth

- Phase 0 KLang capture uses a Playwright session (no JWT). The Playwright MCP profile must be logged in to `app.kognitos.com`. If logged out, the agent surfaces an SSO handoff to the user.
- Phase B (run discovery) and Phase C (exec data) use the GraphQL API (`api.app.kognitos.com`) and need a JWT. Resolution order: Playwright profile self-fetch → env var `KOGNITOS_JWT` → ask user to paste.

## Editor automation (Slate)

The Kognitos editor is Slate.js. Selector is `#slate-editor`. For KLang copy-capture, the listener install + select + copy + read MUST run in **one** `browser_evaluate` call. See `specs/migration-step-1-data-collection.md` Step 0.4 for the pinned procedure.

## What this repo is NOT for

- Per-customer artifacts (those live in the customer's directory, e.g. `plunkett/<automation_slug>/`)
- Per-automation run captures (those live in `<OUTPUT_BASE_DIR>/run_captures/`)
