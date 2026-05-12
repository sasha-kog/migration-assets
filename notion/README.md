# Notion-paste drafts

This directory holds paste-ready markdown for the SE-facing Notion pages. The migration workflow's source of truth is in `specs/` (read by the agent); the files here are the human-facing narrative an SE reads on Notion.

## Files

| File | Pastes into | Replaces |
|---|---|---|
| `step-0-setup.md` | Notion "Agentic Automation Migration Workflow" → Step 0 section | Old "Step 0: Data Preparation" (KLang copy-paste) |
| `step-1-data-collection.md` | Same page → Step 1 section | Old "Step 0: Data Preparation" + old "Step 1: Data Collection" combined |

## How to apply

1. Open the Notion page.
2. Remove the existing Step 0 section.
3. Paste `step-0-setup.md` content as the new Step 0.
4. Remove the existing Step 1 section.
5. Paste `step-1-data-collection.md` content as the new Step 1.

## Why two files

The old workflow split KLang collection (Step 0) from run captures (Step 1) because both were manual processes. Phase 0 hydration automates KLang collection inside what's now a single agent run, so the user-facing split is no longer meaningful. The new Step 0 is just the one-time machine setup; Step 1 is the agent-driven data collection.
