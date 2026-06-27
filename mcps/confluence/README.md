# Confluence MCP

Read-only connector giving agents access to architecture notes, standards, and design decisions stored in Confluence.

## Tools Exposed

| Tool | Description |
|---|---|
| `get_page(page_id)` | Fetch a page's content and last-updated metadata |
| `search_pages(space_key, query, limit)` | Search a space for pages matching a query |
| `get_architecture_standards(space_key)` | Convenience search for architecture standard pages |
| `get_page_history(page_id, limit)` | Recent version/contributor history — useful for checking if a standard is stale |

This is most useful for the **Architect Agent** and **Backend/API Agent**, which need current architecture standards rather than whatever a developer remembers or has bookmarked.

## Setup

1. Install the client library: `pip install atlassian-python-api`
2. Generate an API token in your Atlassian account (can reuse the same token as the Jira MCP if scoped appropriately).
3. Set credentials via environment variables:
   ```bash
   export CONFLUENCE_URL="https://yourcompany.atlassian.net/wiki"
   export CONFLUENCE_EMAIL="..."
   export CONFLUENCE_API_TOKEN="..."
   ```
4. Wrap `ConfluenceMCPServer` with your AI coding tool's MCP server framework.

## Adapting Search

`get_architecture_standards` assumes pages are findable by searching for the literal phrase "architecture standard." Most teams will get better results by:
- Using a consistent Confluence label (e.g., `architecture-standard`) and querying by label instead of free text
- Maintaining a dedicated space for standards so `space_key` alone narrows results meaningfully

Update the CQL query in `search_pages` / `get_architecture_standards` to match whichever convention your team actually uses.

## Scope and Permissions

- Read-only by design. Do not add page-editing capability without a clear approval/audit story — letting an agent silently update architecture docs is a much bigger decision than letting it read them.
- Scope the service account to the specific spaces this team needs, not the whole Confluence instance.

## Known Limitations

- No caching — pages are fetched live on every call. Add caching if architecture docs are large or called frequently within a single agent run.
- `get_page_history` returns raw contributor data; you may want to post-process this into a cleaner "last reviewed" signal for staleness checks.
