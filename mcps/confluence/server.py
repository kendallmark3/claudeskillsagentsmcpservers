#!/usr/bin/env python3
"""
Confluence MCP Server

Read-only access to Confluence pages and spaces for AI coding agents.
Agents pull architecture standards, design decisions, and process docs
directly instead of relying on stale copy-pasted context.

Usage (stdio — for Claude Code local registration):
    python server.py

Required environment variables (see mcps/.env.example):
    CONFLUENCE_URL        — e.g. https://yourorg.atlassian.net/wiki
    CONFLUENCE_USERNAME   — email address of the service account
    CONFLUENCE_API_TOKEN  — Atlassian API token
"""

import json
import os
import sys

from atlassian import Confluence
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("confluence")


def _client() -> Confluence:
    """Build a Confluence client from environment variables. Fails fast with a clear error."""
    required = ["CONFLUENCE_URL", "CONFLUENCE_USERNAME", "CONFLUENCE_API_TOKEN"]
    missing = [v for v in required if not os.environ.get(v)]
    if missing:
        sys.exit(
            f"Missing required environment variables: {', '.join(missing)}\n"
            f"Copy mcps/.env.example to mcps/.env and fill in your values."
        )
    return Confluence(
        url=os.environ["CONFLUENCE_URL"],
        username=os.environ["CONFLUENCE_USERNAME"],
        password=os.environ["CONFLUENCE_API_TOKEN"],
        cloud=True,
    )


@mcp.tool()
def get_page(page_id: str) -> str:
    """
    Fetch a Confluence page by ID — returns title, full content, last updated date,
    and the name of who last updated it.

    To find a page ID: open the page in your browser, click the three-dot menu,
    and choose 'Page information'. The ID is in the URL.
    """
    client = _client()
    page = client.get_page_by_id(page_id, expand="body.storage,version")
    result = {
        "id": page_id,
        "title": page["title"],
        "content": page["body"]["storage"]["value"],
        "last_updated": page["version"]["when"],
        "last_updated_by": page["version"]["by"]["displayName"],
    }
    return json.dumps(result, indent=2)


@mcp.tool()
def search_pages(space_key: str, query: str, limit: int = 5) -> str:
    """
    Search for pages in a Confluence space matching a text query.
    Returns page ID, title, and URL for each match.

    Useful when an agent needs 'the architecture standard for X' but doesn't
    know the page ID ahead of time.
    """
    client = _client()
    cql = f'space = "{space_key}" AND text ~ "{query}" ORDER BY lastModified DESC'
    results = client.cql(cql, limit=limit)
    pages = [
        {
            "id": r["content"]["id"],
            "title": r["content"]["title"],
            "url": r["content"].get("_links", {}).get("webui", ""),
        }
        for r in results.get("results", [])
    ]
    return json.dumps(pages, indent=2)


@mcp.tool()
def get_architecture_standards(space_key: str) -> str:
    """
    Convenience tool — searches a space for pages that match 'architecture standard'.
    Adapt the search term to match your team's labeling convention.
    """
    client = _client()
    cql = f'space = "{space_key}" AND text ~ "architecture standard" ORDER BY lastModified DESC'
    results = client.cql(cql, limit=10)
    pages = [
        {
            "id": r["content"]["id"],
            "title": r["content"]["title"],
            "url": r["content"].get("_links", {}).get("webui", ""),
        }
        for r in results.get("results", [])
    ]
    return json.dumps(pages, indent=2)


@mcp.tool()
def list_space_pages(space_key: str, limit: int = 20) -> str:
    """
    List the most recently updated pages in a Confluence space.
    Useful for orienting an agent to what's available before searching.
    """
    client = _client()
    pages = client.get_all_pages_from_space(space_key, limit=limit)
    result = [
        {"id": p["id"], "title": p["title"]}
        for p in pages
    ]
    return json.dumps(result, indent=2)


if __name__ == "__main__":
    mcp.run()
