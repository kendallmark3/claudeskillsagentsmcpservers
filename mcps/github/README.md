# GitHub MCP

Read-only connector giving agents controlled access to pull requests, file contents, commits, comments, and CI/workflow status.

Primary MCP for the **PR Review Agent** — lets that agent inspect a real PR (changed files, CI status, comments) instead of relying on a pasted summary.

## Tools Exposed

| Tool | Description |
|---|---|
| `get_pull_request(owner, repo, prNumber)` | Returns PR metadata, author, changed files with add/delete counts |
| `get_changed_files(owner, repo, prNumber)` | Returns just the list of changed file paths — lighter than get_pull_request |
| `get_file_content(owner, repo, path, ref)` | Raw content of a file at a given branch, tag, or commit SHA |
| `get_recent_commits(owner, repo, branch, limit)` | Recent commit history on a branch |
| `get_pr_comments(owner, repo, prNumber)` | Review and discussion comments on a PR |
| `get_workflow_status(owner, repo, ref)` | GitHub Actions CI/CD status for a commit SHA |

## Setup

### Dependencies

```bash
cd mcps/github
npm install
npm run build   # compiles server.ts → dist/server.js
```

### Credentials

```bash
cp ../.env.example ../.env
# Fill in GITHUB_TOKEN
```

Generate a fine-grained personal access token at: **github.com → Settings → Developer settings → Personal access tokens → Fine-grained tokens**

Minimum required permissions (read-only):
- **Contents** — read
- **Pull requests** — read
- **Actions** — read (for CI status)

Scope the token to only the repos this team works in — not your whole org.

### Register with Claude Code

```json
{
  "mcpServers": {
    "github": {
      "command": "node",
      "args": ["path/to/ai-shared-services/mcps/github/dist/server.js"],
      "env": {
        "GITHUB_TOKEN": "your-github-token"
      }
    }
  }
}
```

## Scope and Permissions

- **Read-only by default.** Do not add write operations (posting comments, creating PRs) without scoping a separate token and documenting the write path explicitly — don't silently upgrade the read-only token's permissions.
- Prefer fine-grained personal access tokens over classic tokens: they can be scoped to specific repos and expire.
- Consider a GitHub App installation token instead of a PAT for team/org deployments — App tokens expire automatically and don't depend on an individual's account.

## Known Limitations

- `get_workflow_status` assumes GitHub Actions. For Jenkins, CircleCI, or other CI providers, a separate MCP or extended tool is needed.
- No pagination for very large PRs (100+ changed files) or long commit histories — add pagination if your repos are large.
- No rate-limit backoff — add retry logic before using against high-traffic repos or in CI.
- The TypeScript source must be compiled before running (`npm run build`). The `dist/` folder is gitignored; run the build after cloning.
