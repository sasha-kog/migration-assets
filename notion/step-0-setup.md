# Step 0: Setup (one-time per machine)

Before running migrations, each SE sets up their machine once.

## 1. Clone the migration assets repo

```bash
git clone git@github.com:kognitos/migration-assets ~/kognitos-migration-assets
```

This gives you the canonical specs, run-capture template, and an example filled capture. `git pull` in `~/kognitos-migration-assets` before each new migration to pick up updates.

## 2. Confirm Claude Code is installed and authenticated

Claude Code CLI + the Playwright MCP browser. If you've run Quill or other Kognitos automations from Claude Code before, you have what you need.

## 3. Confirm you can sign in to `app.kognitos.com`

The agent uses your normal SSO login through the Playwright browser. First time the agent opens an editor URL it'll route to Auth0 — log in once, the session persists for the rest of the migration.

That's it. You'll need a JWT for the GraphQL API only if Phase 0's primary capture path (Playwright copy) fails on some stage; the agent prompts you then.
