# Feature Intent: Linear MCP

## Objective

Build a read-only Linear MCP that gives agents direct access to issues, cycles, projects, and team context — serving as the Linear equivalent of the Jira MCP for teams that use Linear instead of Jira.

## Business Outcome

Teams using Linear can run the full Skills/Agents/MCPs delivery loop without manual copy-paste of issue context, making this repo usable for the significant portion of engineering orgs that have standardized on Linear over Jira.

## Source Story

ROADMAP.md — Near-Term MCPs: Linear

## Acceptance Criteria

1. `get_issue(issue_id)` returns issue title, description, status, priority, assignee, labels, and cycle.
2. `get_team_issues(team_id, status_filter)` returns a filtered list of issues for a given team and status.
3. `get_cycle(cycle_id)` returns cycle name, dates, and issue count.
4. `search_issues(query)` returns issues matching a text query (title + description).
5. `get_project(project_id)` returns project name, status, lead, and linked issues.
6. All tools are read-only — no create, update, or comment-posting operations.
7. Authentication uses a Linear API key passed via `LINEAR_API_KEY` environment variable.
8. `README.md` documents: tools exposed, setup steps, API key generation instructions, scope/permissions, known limitations.
9. Follows the same file structure as `mcps/jira/`.
10. `requirements.txt` (Python) or `package.json` (TypeScript) included with pinned dependencies.

## Constraints

- Read-only. Do not expose create, update, archive, or comment tools.
- Use the Linear GraphQL API (Linear's primary API) — do not use an unofficial REST wrapper.
- If implementing in Python, use `gql` or `httpx` for the GraphQL client; avoid heavy ORMs or SDK wrappers that add unnecessary dependencies.
- Token must be injected via environment variable; document in README.
- Must be a close structural parallel to `mcps/jira/` so teams can onboard to it without learning a new pattern.

## Existing Patterns to Inspect

- `mcps/jira/server.py` — the reference implementation to parallel
- `mcps/jira/README.md` — tools table, setup, scope/permissions, known limitations format
- `CONTRIBUTING.md` — "Adding a New MCP" section
- `docs/faq.md` — "Our team uses Copilot not Claude Code — does this apply?" (Linear MCP should be tool-agnostic like Jira)

## APIs Involved

- Linear GraphQL API: `https://api.linear.app/graphql`
- Auth: `Authorization: Bearer <LINEAR_API_KEY>` header
- Key queries: `issue(id)`, `team(id).issues()`, `cycle(id)`, `issueSearch(query)`, `project(id)`

## Data Involved

- Issue metadata: title, description, status, priority, assignee, labels (non-sensitive)
- Cycle and project metadata: names, dates, progress (non-sensitive)
- No PII, no credentials, no financial data

## Tests Required

- `get_issue()` with a valid Linear issue ID returns expected fields
- `get_team_issues()` with a status filter returns only matching issues
- Missing or invalid `LINEAR_API_KEY` raises a clear, actionable error
- `search_issues()` with a known term returns at least one result
- GraphQL error responses are handled gracefully (not exposed as raw exceptions)

## Evidence Required

- `mcps/linear/server.py` (or `.ts`) created following the Jira MCP structure
- `mcps/linear/README.md` created with complete tools table and setup instructions
- `mcps/linear/requirements.txt` (or `package.json`) with pinned dependencies
- Read-only constraint confirmed: no mutations exposed
- `ROADMAP.md` updated to mark Linear MCP as in-progress or completed
