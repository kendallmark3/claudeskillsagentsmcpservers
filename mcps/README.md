# MCP Servers

Three read-only MCP servers that give AI agents direct, controlled access to Jira, Confluence, and GitHub — without manual copy-paste. Each server exposes a deliberate, minimal set of tools. None have write access by default.

---

## Servers

| Server | Language | Port (Docker) | What it exposes |
|---|---|---|---|
| [jira/](jira/) | Python | 8000 | Stories, acceptance criteria, comments, links, defects |
| [confluence/](confluence/) | Python | 8001 | Pages, space search, architecture standards |
| [github/](github/) | TypeScript | 8002 | PRs, files, commits, comments, CI status |

---

## Option A — Local Setup (Recommended for Getting Started)

Each MCP server runs as a local stdio process. Claude Code spawns it automatically when needed.

### 1. Set up credentials

```bash
cp mcps/.env.example mcps/.env
# Edit mcps/.env with your real values — this file is gitignored
```

### 2. Install dependencies

```bash
# Jira MCP
pip install -r mcps/jira/requirements.txt

# Confluence MCP
pip install -r mcps/confluence/requirements.txt

# GitHub MCP
cd mcps/github && npm install && cd ../..
```

### 3. Register with Claude Code

Add to your project's `.claude/settings.json` (or global `~/.claude/settings.json`):

```json
{
  "mcpServers": {
    "jira": {
      "command": "python",
      "args": ["mcps/jira/server.py"],
      "env": {
        "JIRA_SERVER": "https://yourorg.atlassian.net",
        "JIRA_API_TOKEN": "your-token",
        "JIRA_EMAIL": "you@yourorg.com"
      }
    },
    "confluence": {
      "command": "python",
      "args": ["mcps/confluence/server.py"],
      "env": {
        "CONFLUENCE_URL": "https://yourorg.atlassian.net/wiki",
        "CONFLUENCE_USERNAME": "you@yourorg.com",
        "CONFLUENCE_API_TOKEN": "your-token"
      }
    },
    "github": {
      "command": "node",
      "args": ["mcps/github/dist/server.js"],
      "env": {
        "GITHUB_TOKEN": "your-github-token"
      }
    }
  }
}
```

> **Tip:** Use environment variable references instead of hardcoded values in `settings.json` wherever your tool supports them. The servers read from `process.env` / `os.environ`, so you can also set these in your shell profile and omit the `env` block from the config.

### 4. Build the GitHub MCP (TypeScript only)

```bash
cd mcps/github
npm run build   # compiles server.ts → dist/server.js
```

### 5. Verify

In Claude Code, type `/mcp` to see connected servers. Each should show green with its tools listed.

---

## Option B — Docker Compose (Team / Cloud Deployment)

Run all three MCPs as persistent HTTP services so multiple developers connect to one shared instance.

### 1. Set up credentials

```bash
cp mcps/.env.example mcps/.env
# Edit mcps/.env — this file is gitignored, never committed
```

### 2. Start all servers

```bash
cd mcps
docker compose up -d
```

### 3. Register with Claude Code (HTTP SSE transport)

```json
{
  "mcpServers": {
    "jira": {
      "type": "sse",
      "url": "http://localhost:8000/sse"
    },
    "confluence": {
      "type": "sse",
      "url": "http://localhost:8001/sse"
    },
    "github": {
      "type": "sse",
      "url": "http://localhost:8002/sse"
    }
  }
}
```

Replace `localhost` with your server's hostname or IP when deploying to a shared machine or cloud instance.

### Cloud deployment notes

- Put a reverse proxy (nginx, Caddy) in front for TLS termination before exposing beyond localhost.
- Each container reads from the shared `mcps/.env` file — never bake credentials into the Docker image.
- Use a service account with minimum required permissions (see individual MCP READMEs for scope guidance).

---

## Security Defaults

| Principle | Implementation |
|---|---|
| Read-only by default | No write, create, update, or delete tools are exposed in any server |
| Credentials via env vars | No tokens or passwords in source code — ever |
| `.env` gitignored | The root `.gitignore` covers `mcps/.env`; `.env.example` with placeholders is committed |
| Minimum token scope | See each MCP's README for the exact permissions required |
| Fail-fast on missing config | All servers exit immediately with a clear error if required env vars are missing |

---

## Adding a New MCP

1. Create a folder under `mcps/` (e.g., `mcps/figma/`).
2. Write `server.py` or `server.ts` following the pattern in `jira/` or `github/`.
3. Add `requirements.txt` or `package.json` with pinned dependencies.
4. Add a `Dockerfile` following the pattern in existing MCPs.
5. Add the new service to `docker-compose.yml`.
6. Add the env vars to `.env.example` with placeholder values and comments.
7. Write a `README.md` documenting tools, setup, permissions, and limitations.
8. See [CONTRIBUTING.md](../CONTRIBUTING.md) for the full checklist.
