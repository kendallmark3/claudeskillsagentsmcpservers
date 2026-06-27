#!/usr/bin/env python3
"""
Jira MCP Server

Read-only access to Jira stories, comments, links, and status for AI coding agents.
Agents call these tools instead of having a developer manually copy-paste ticket text.

Usage (stdio — for Claude Code local registration):
    python server.py

Required environment variables (see mcps/.env.example):
    JIRA_SERVER      — e.g. https://yourorg.atlassian.net
    JIRA_API_TOKEN   — Atlassian API token (generate at id.atlassian.com/manage-profile/security/api-tokens)
    JIRA_EMAIL       — email address associated with the token
"""

import json
import os
import sys

from jira import JIRA
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("jira")


def _client() -> JIRA:
    """Build a Jira client from environment variables. Fails fast with a clear error."""
    required = ["JIRA_SERVER", "JIRA_API_TOKEN", "JIRA_EMAIL"]
    missing = [v for v in required if not os.environ.get(v)]
    if missing:
        sys.exit(
            f"Missing required environment variables: {', '.join(missing)}\n"
            f"Copy mcps/.env.example to mcps/.env and fill in your values."
        )
    return JIRA(
        server=os.environ["JIRA_SERVER"],
        basic_auth=(os.environ["JIRA_EMAIL"], os.environ["JIRA_API_TOKEN"]),
    )


@mcp.tool()
def get_story(story_id: str) -> str:
    """
    Fetch a single Jira story with all fields agents commonly need:
    title, description, status, acceptance criteria, comments, and linked issues.

    Acceptance criteria are extracted from the description under an 'Acceptance Criteria'
    heading. If your org uses a custom field instead, update _extract_ac() below.
    """
    client = _client()
    issue = client.issue(story_id)
    description = issue.fields.description or ""

    result = {
        "id": story_id,
        "title": issue.fields.summary,
        "description": description,
        "status": issue.fields.status.name,
        "acceptance_criteria": _extract_ac(description),
        "comments": [
            {"author": c.author.displayName, "body": c.body}
            for c in issue.fields.comment.comments
        ],
        "links": [str(link) for link in getattr(issue.fields, "issuelinks", [])],
    }
    return json.dumps(result, indent=2)


@mcp.tool()
def check_status(story_id: str) -> str:
    """Quick status check for a story — returns just the status string."""
    client = _client()
    issue = client.issue(story_id)
    return issue.fields.status.name


@mcp.tool()
def get_comments(story_id: str) -> str:
    """Fetch all comments for a story with author names."""
    client = _client()
    issue = client.issue(story_id)
    comments = [
        {"author": c.author.displayName, "body": c.body}
        for c in issue.fields.comment.comments
    ]
    return json.dumps(comments, indent=2)


@mcp.tool()
def get_links(story_id: str) -> str:
    """Fetch all linked issues for a story."""
    client = _client()
    issue = client.issue(story_id)
    links = [str(link) for link in getattr(issue.fields, "issuelinks", [])]
    return json.dumps(links, indent=2)


@mcp.tool()
def find_related_defects(story_id: str) -> str:
    """
    Find bugs linked to or referencing this story.
    Useful for the QA Agent when assessing regression risk.

    Adapt the JQL query to match your org's linking conventions if needed.
    """
    client = _client()
    jql = f'issuelinks = "{story_id}" AND issuetype = Bug'
    results = client.search_issues(jql)
    defects = [
        {
            "id": issue.key,
            "title": issue.fields.summary,
            "status": issue.fields.status.name,
        }
        for issue in results
    ]
    return json.dumps(defects, indent=2)


def _extract_ac(description: str) -> str:
    """
    Extract acceptance criteria from the description text.
    Assumes an 'Acceptance Criteria' heading; adapt if your org uses a custom field.
    """
    if "Acceptance Criteria" in description:
        return description.split("Acceptance Criteria", 1)[-1].strip()
    return ""


if __name__ == "__main__":
    mcp.run()
