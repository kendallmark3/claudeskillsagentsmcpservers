# Confluence MCP

Read-only connector giving agents controlled access to Confluence pages and spaces — so agents can pull current architecture standards instead of working from stale or copy-pasted context.

## Tools Exposed

| Tool | Description |
|---|---|
| `get_page(page_id)` | Returns page title, full content, last updated date, and author |
| `search_pages(space_key, query, limit)` | Text search within a space — returns page IDs, titles, and URLs |
| `get_architecture_standards(space_key)` | Convenience search for pages matching "architecture standard" |
| `list_space_pages(space_key, limit)` | Lists most recently updated pages in a space |

Most useful for the **Architect Agent** and **Backend/API Agent**, which need current architecture standards rather than whatever a developer remembers or has bookmarked.

## Setup

### Dependencies

```bash
pip install -r requirements.txt
```

### Credentials

```bash
cp ../.env.example ../.env
# Fill in CONFLUENCE_URL, CONFLUENCE_USERNAME, CONFLUENCE_API_TOKEN
```

Generate an API token at: **id.atlassian.com → Security → API tokens**

The same Atlassian API token works for both Jira and Confluence.

### Register with Claude Code

```json
{
  "mcpServers": {
    "confluence": {
      "command": "python",
      "args": ["path/to/ai-shared-services/mcps/confluence/server.py"],
      "env": {
        "CONFLUENCE_URL": "https://yourorg.atlassian.net/wiki",
        "CONFLUENCE_USERNAME": "you@yourorg.com",
        "CONFLUENCE_API_TOKEN": "your-token"
      }
    }
  }
}
```

## Finding Page IDs

Open the page in your browser → click the `...` menu → **Page information**. The ID appears in the URL as `/pages/[ID]/`.

Use `search_pages` or `list_space_pages` to discover IDs programmatically when you don't have them ahead of time.

## Adapting the Architecture Standards Search

`get_architecture_standards` searches for pages matching "architecture standard". If your team uses labels or different naming, update the CQL query in `server.py`:

```python
cql = f'space = "{space_key}" AND label = "architecture" ORDER BY lastModified DESC'
```

## Scope and Permissions

- **Read-only.** No page creation, editing, or comment posting.
- Use a service account with read access to the specific spaces this team needs — not org-wide access.
- `cloud=True` is set in the client. Change to `cloud=False` for Confluence Data Center / Server deployments.

## Known Limitations

- `get_page` returns raw Confluence storage format (XML-like). Agents handle this well but it may look unusual if printed directly.
- No pagination beyond the `limit` parameter — increase the limit or use `search_pages` for large spaces.
- No caching — pages are fetched live. Add caching if architecture docs are large or called frequently within a single session.
