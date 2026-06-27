# Jira MCP

Read-only connector giving agents controlled access to Jira stories, comments, links, and status — without manual copy-paste into prompts.

## Tools Exposed

| Tool | Description |
|---|---|
| `get_story(story_id)` | Returns title, description, status, acceptance criteria, comments, and links for a story |
| `extract_acceptance_criteria(issue)` | Pulls acceptance criteria out of the description (adapt if your org uses a custom field instead) |
| `get_comments(issue)` | Returns all comments with author |
| `get_links(issue)` | Returns linked issues |
| `find_related_defects(story_id)` | Finds bugs linked to or referencing the story — useful for QA Agent regression assessment |
| `check_status(story_id)` | Quick status lookup |

## Setup

1. Install the Jira client library: `pip install jira`
2. Generate an API token in your Atlassian account.
3. Wire credentials via environment variables, not hardcoded values:
   ```bash
   export JIRA_SERVER="https://yourcompany.atlassian.net"
   export JIRA_API_TOKEN="..."
   export JIRA_EMAIL="..."
   ```
4. Wrap `JiraMCPServer` with your AI coding tool's MCP server framework. The exact wiring depends on which tool/SDK version you're using — see your tool's MCP documentation for the server registration pattern.

## Acceptance Criteria Field Mapping

`extract_acceptance_criteria` assumes acceptance criteria live in the description under a literal "Acceptance Criteria" heading. Many Jira instances instead use a custom field (e.g., `customfield_10042`). Check your instance's field configuration and update the extraction logic accordingly — this is the most common adaptation needed before this MCP is useful in your org.

## Scope and Permissions

- This connector is **read-only by design**. Do not add write operations (status transitions, comment posting) until the team has reviewed the audit/approval implications.
- Use a service account with the minimum project access needed, not a personal account with org-wide access.

## Known Limitations

- `find_related_defects` uses a simple JQL pattern; tune it to your org's linking conventions (some teams use "relates to," others use custom link types).
- No caching — repeated calls hit the Jira API directly. Add caching if your team's MCP call volume is high.
