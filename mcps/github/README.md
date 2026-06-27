# GitHub MCP

Connector giving agents controlled access to pull requests, file contents, commits, comments, and CI/workflow status.

## Tools Exposed

| Tool | Description |
|---|---|
| `getPullRequest(owner, repo, prNumber)` | Returns PR metadata, author, and changed files |
| `getChangedFiles(owner, repo, prNumber)` | List of changed file paths only |
| `getFileContent(owner, repo, path, ref)` | Raw content of a file at a given ref |
| `getRecentCommits(owner, repo, branch, limit)` | Recent commit history on a branch |
| `getPrComments(owner, repo, prNumber)` | Review/discussion comments on a PR |
| `getWorkflowStatus(owner, repo, ref)` | CI/CD workflow run status for a commit |

This is the primary MCP used by the **PR Review Agent** — it lets that agent inspect a real PR (changed files, CI status, comments) instead of relying on a pasted summary.

## Setup

1. Install the GitHub client library: `npm install @octokit/rest`
2. Generate a fine-grained personal access token or, preferably, a GitHub App installation token scoped to the specific repos this team needs.
3. Set the token via environment variable, not hardcoded:
   ```bash
   export GITHUB_TOKEN="..."
   ```
4. Wrap `GitHubMCPServer` with your AI coding tool's MCP server framework.

## Scope and Permissions

- Prefer **read-only** scopes (`repo:status`, `public_repo` or read-only fine-grained permissions) for the first version of this connector.
- If you later need write access (e.g., posting a PR Review Agent's comments directly), scope that token separately and document the write path explicitly — don't silently upgrade the read-only token's permissions.
- Limit the token to the specific repos this shared services team works in, not your whole GitHub org.

## Known Limitations

- `getWorkflowStatus` assumes GitHub Actions; adapt if your team uses a different CI provider (Jenkins, CircleCI, etc. — would need a separate MCP or extended tool).
- No pagination handling shown for very large PRs (100+ changed files) or long commit histories — add pagination if your repos are large.
- No rate-limit backoff included — add retry/backoff logic before using this against high-traffic repos.
