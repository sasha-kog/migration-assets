# kognitos-migration-assets

Shared assets for Kognitos V1 → V2 automation migrations.

## What this repo is

A small, append-only repo with reference materials the Claude Code migration agent reads by fixed path during Phase 0 hydration and beyond. Versioned via git so any teammate on any machine has the same templates.

## What's in it

| Path | Used by | Purpose |
|---|---|---|
| `run_capture_template.md` | Phase 1 (data collection) | Generic skeleton an SE/agent adapts per automation; defines the section structure for `run_capture_filled.md` |
| `example_filled_capture/` | Phase 1 (data collection) | One real, completed run capture from a past migration. Agents read this as a structural model for the level of detail expected. |
| `CLAUDE.md` | Any Claude Code agent in this directory | Conventions: where the migration spec lives, slug naming, default output dirs |

## How to use

Clone once per machine:

```bash
git clone git@github.com:kognitos/migration-assets ~/kognitos-migration-assets
```

`git pull` before starting a migration to pick up updates.

The migration spec (`golem/specs/migration-step-1-data-collection-merged.md` in the golem repo) references files in this directory by fixed path. **Do not move things around** without coordinating a spec update.

## Adding to this repo

Append-only. If you have a particularly good filled capture from a recent migration, add it as a sibling folder under `examples/` (separate from `example_filled_capture/`, which stays as the canonical one referenced by the spec). PR with a note about which automation and what was good about it.
