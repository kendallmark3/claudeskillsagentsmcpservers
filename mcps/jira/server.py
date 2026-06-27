"""
jira_mcp_server.py

Starter MCP server exposing controlled, read-only access to Jira.

This is a conceptual starting point, not a production-ready server.
Wire `jira_client` to your actual Jira client (e.g., the `jira` PyPI package)
and adapt field mappings to match your Jira instance's configuration
(custom fields for acceptance criteria will vary by org).
"""

from typing import Dict, List


class JiraMCPServer:
    """
    Exposes a small, deliberate set of read-only tools for retrieving
    Jira story context. Agents call these methods instead of having a
    human copy-paste ticket text into a prompt.
    """

    def __init__(self, jira_client):
        self.jira_client = jira_client

    def get_story(self, story_id: str) -> Dict:
        """
        Fetch a single story with the fields agents most commonly need:
        title, description, status, acceptance criteria, comments, links.
        """
        issue = self.jira_client.issue(story_id)

        return {
            "id": story_id,
            "title": issue.fields.summary,
            "description": issue.fields.description,
            "status": issue.fields.status.name,
            "acceptance_criteria": self.extract_acceptance_criteria(issue),
            "comments": self.get_comments(issue),
            "links": self.get_links(issue),
        }

    def extract_acceptance_criteria(self, issue) -> str:
        """
        Naive extraction assuming acceptance criteria live in the
        description under a heading. Replace with a custom field
        lookup if your Jira instance uses one (common pattern:
        `customfield_XXXXX`).
        """
        description = issue.fields.description or ""

        if "Acceptance Criteria" in description:
            return description.split("Acceptance Criteria", 1)[-1].strip()

        return ""

    def get_comments(self, issue) -> List[Dict]:
        return [
            {
                "author": comment.author.displayName,
                "body": comment.body,
            }
            for comment in issue.fields.comment.comments
        ]

    def get_links(self, issue) -> List[str]:
        return [str(link) for link in getattr(issue.fields, "issuelinks", [])]

    def find_related_defects(self, story_id: str) -> List[Dict]:
        """
        Searches for defects (bugs) linked to or referencing this story.
        Useful for the QA Agent when assessing regression risk.
        """
        jql = f'issuelinks = "{story_id}" AND issuetype = Bug'
        results = self.jira_client.search_issues(jql)

        return [
            {
                "id": issue.key,
                "title": issue.fields.summary,
                "status": issue.fields.status.name,
            }
            for issue in results
        ]

    def check_status(self, story_id: str) -> str:
        """Quick status check without pulling the full story payload."""
        issue = self.jira_client.issue(story_id)
        return issue.fields.status.name


# -----------------------------------------------------------------------
# Example wiring (adapt to your actual transport — this repo assumes
# you'll wrap this class with whatever MCP server framework / SDK your
# AI coding tool expects; the framework wiring is intentionally left
# out since it varies by tool and version).
# -----------------------------------------------------------------------
#
# from jira import JIRA
#
# jira_client = JIRA(
#     server="https://yourcompany.atlassian.net",
#     token_auth="<API_TOKEN>",
# )
#
# server = JiraMCPServer(jira_client)
# story = server.get_story("CUST-4821")
