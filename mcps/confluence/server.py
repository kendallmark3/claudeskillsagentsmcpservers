"""
confluence_mcp_server.py

Starter MCP server exposing controlled, read-only access to Confluence.

This is a conceptual starting point, not a production-ready server.
Wire `confluence_client` to your actual Confluence client (e.g., the
`atlassian-python-api` package) and adapt to your space/page structure.
"""

from typing import Dict, List


class ConfluenceMCPServer:
    """
    Exposes a small set of read-only tools for retrieving architecture
    notes, standards, and design decisions stored in Confluence — so
    agents can pull current standards instead of working from stale
    or copy-pasted context.
    """

    def __init__(self, confluence_client):
        self.confluence_client = confluence_client

    def get_page(self, page_id: str) -> Dict:
        """Fetch a single page's content and metadata."""
        page = self.confluence_client.get_page_by_id(
            page_id, expand="body.storage,version"
        )

        return {
            "id": page_id,
            "title": page["title"],
            "content": page["body"]["storage"]["value"],
            "last_updated": page["version"]["when"],
            "last_updated_by": page["version"]["by"]["displayName"],
        }

    def search_pages(self, space_key: str, query: str, limit: int = 5) -> List[Dict]:
        """
        Search for pages within a space matching a query — useful when
        an agent needs to find "the architecture standard for X" without
        already knowing the page ID.
        """
        cql = f'space = "{space_key}" AND text ~ "{query}"'
        results = self.confluence_client.cql(cql, limit=limit)

        return [
            {
                "id": result["content"]["id"],
                "title": result["content"]["title"],
                "url": result["content"].get("_links", {}).get("webui", ""),
            }
            for result in results.get("results", [])
        ]

    def get_architecture_standards(self, space_key: str) -> List[Dict]:
        """
        Convenience method that searches a known space for pages tagged
        or titled as architecture standards. Adapt the query to match
        your team's actual labeling/tagging convention.
        """
        return self.search_pages(space_key, "architecture standard")

    def get_page_history(self, page_id: str, limit: int = 5) -> List[Dict]:
        """Fetch recent version history for a page — useful for checking staleness."""
        history = self.confluence_client.history(page_id)
        versions = history.get("history", {}).get("contributors", {})
        return versions if versions else []


# -----------------------------------------------------------------------
# Example wiring (adapt to your actual transport — wrap this class with
# whatever MCP server framework your AI coding tool expects).
# -----------------------------------------------------------------------
#
# from atlassian import Confluence
#
# confluence_client = Confluence(
#     url="https://yourcompany.atlassian.net/wiki",
#     username="<EMAIL>",
#     password="<API_TOKEN>",
# )
#
# server = ConfluenceMCPServer(confluence_client)
# page = server.get_page("123456")
