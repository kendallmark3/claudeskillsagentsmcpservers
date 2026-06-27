# Feature Intent: MCP Dependency Management

## Objective

Add proper dependency files to all three existing MCPs so that any developer who clones this repo can stand up a working MCP without undocumented manual steps. Also add a shared `.env.example` that centralizes all required environment variables in one place.

## Business Outcome

The first-run experience for any developer adopting these MCPs is self-contained. Clone, copy `.env.example`, fill in credentials, install dependencies, run. No hunting through three separate READMEs to reconstruct the setup.

## Source Story

repo-scorecard.md — Risk Register: "MCP code has no dependency files" (Medium severity)

## Acceptance Criteria

1. `mcps/jira/requirements.txt` exists with a pinned version of the `jira` Python client.
2. `mcps/confluence/requirements.txt` exists with a pinned version of the Confluence client library used in `server.py`.
3. `mcps/github/package.json` exists with `@octokit/rest` as a dependency and a corresponding `package-lock.json` or `npm-shrinkwrap.json`.
4. `mcps/.env.example` exists, listing every environment variable required across all MCPs with placeholder values and a one-line comment explaining each.
5. Each MCP `README.md` setup section references the `requirements.txt` / `package.json` install command and points to `mcps/.env.example`.
6. `mcps/.env.example` is committed to Git. Any `.env` files remain gitignored (verify `.gitignore` covers `mcps/**/.env`).

## Constraints

- Dependency versions must be pinned (e.g., `jira==3.5.2`, not `jira>=3`). Use latest stable at time of writing.
- Do not add dependencies beyond what the existing MCP server code already imports.
- `mcps/.env.example` must contain only placeholder values — never real tokens, even test tokens.
- The GitHub MCP `package.json` should be minimal: no build tooling, no TypeScript compilation config — just the runtime dependency declaration.
- Do not change any MCP server code — only dependency and documentation files.

## Existing Patterns to Inspect

- `mcps/jira/server.py` — imports to confirm which libraries are used
- `mcps/confluence/server.py` — same
- `mcps/github/server.ts` — imports to confirm `@octokit/rest` version compatibility
- `mcps/jira/README.md` — Setup section to update
- `mcps/github/README.md` — Setup section to update
- `mcps/confluence/README.md` — Setup section to update
- `.gitignore` — verify `.env` patterns cover the `mcps/` subdirectory

## APIs Involved

None — this is a documentation and dependency-file task, not a code change.

## Data Involved

- Environment variable names (non-sensitive): `JIRA_SERVER`, `JIRA_API_TOKEN`, `JIRA_EMAIL`, `GITHUB_TOKEN`, `CONFLUENCE_URL`, `CONFLUENCE_USERNAME`, `CONFLUENCE_API_TOKEN`

## Tests Required

- Manual: fresh clone → `pip install -r mcps/jira/requirements.txt` completes without error
- Manual: fresh clone → `pip install -r mcps/confluence/requirements.txt` completes without error
- Manual: fresh clone → `cd mcps/github && npm install` completes without error
- Verify `mcps/.env.example` contains no real credentials via `git log -p mcps/.env.example | grep -v "<"` (should return nothing suspicious)

## Evidence Required

- `mcps/jira/requirements.txt` created with pinned version
- `mcps/confluence/requirements.txt` created with pinned version
- `mcps/github/package.json` created with `@octokit/rest` pinned
- `mcps/.env.example` created with all env vars documented
- All three MCP `README.md` Setup sections updated to reference install commands
- `.gitignore` verified to cover `mcps/**/.env`
- No real credentials in any committed file (confirmed via surface scan)
