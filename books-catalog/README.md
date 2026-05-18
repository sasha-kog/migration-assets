# books-catalog/

Snapshot of the Kognitos platform's integration (book) reference documentation. Used by the Phase B Preflight (see `specs/migration-step-2-3-combined.md`) as a **disambiguation fallback** when the Nexus MCP returns ambiguous or empty results for an intent.

## Authority

This directory is **not** the source of truth. Order of precedence in the preflight procedure:

1. Nexus MCP (`kognitos_books` actions). Live, reflects what's actually on the platform + connected in a workspace.
2. This snapshot. Keyword-grep target for candidate-book enumeration when MCP results are inconclusive.
3. `books.md` at the repo root. Curated 64-integration digest; cheat-sheet only.

When this snapshot disagrees with MCP, **trust MCP**.

## Source

Mirrored from the [`Kognitos/docs-gitbook`](https://github.com/Kognitos/docs-gitbook) repo, path `guides-v2/platform/integrations/`.

Snapshot pinned at upstream commit `68574cc` (2026-04-22 — last change before snapshot taken 2026-05-15).

## Refreshing

To resync against the current upstream:

```bash
DOCS=~/Kognitos/docs-gitbook  # path to the docs-gitbook checkout
cp "$DOCS/guides-v2/platform/integrations/"*.md ~/kognitos-migration-assets/books-catalog/
# The upstream README.md is preserved here as INTEGRATIONS_OVERVIEW.md.
# After cp, restore the rename to avoid overwriting this README:
mv ~/kognitos-migration-assets/books-catalog/README.md ~/kognitos-migration-assets/books-catalog/INTEGRATIONS_OVERVIEW.md
# Then update the pinned commit below.
cd "$DOCS" && git log -1 --format="%H %ai %s" -- guides-v2/platform/integrations/
```

Then commit + open a PR. Drift between this snapshot and upstream is expected; sync periodically (or when a preflight surfaces a book that exists upstream but is missing here).

## Contents

- 66 per-book files (one per integration). File name matches the book id used by the MCP (e.g. `gmail.md` → `book_name: "gmail"` in `kognitos_books` results), with a few legacy hyphenated names (`browser-use.md`, `excel-standalone.md`, `google-authentication.md`, `google-service-account-authentication.md`).
- `INTEGRATIONS_OVERVIEW.md` — upstream's `README.md` from the integrations directory, preserved for context (general explanation of integrations, connections, and how the platform identifies required books).
