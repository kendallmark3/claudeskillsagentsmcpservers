# Jira MCP

Read-only connector giving agents controlled access to Jira stories, comments, links, and status — without manual copy-paste into prompts.

## Tools Exposed

| Tool | Description |
|---|---|
| `get_story(story_id)` | Returns title, description, status, acceptance criteria, comments, and links |
| `check_status(story_id)` | Quick status lookup without pulling the full story payload |
| `get_comments(story_id)` | Returns all comments with author names |
| `get_links(story_id)` | Returns linked issues |
| `find_related_defects(story_id)` | Finds bugs linked to or referencing the story — useful for QA Agent regression assessment |

## Setup

### Dependencies

```bash
pip install -r requirements.txt
```

### Credentials

```bash
cp ../. env.example ../.env
# Fill in JIRA_SERVER, JIRA_API_TOKEN, JIRA_EMAIL
```

Generate an API token at: **id.atlassian.com → Security → API tokens**

### Register with Claude Code

Add to `.claude/settings.json` in any repo that should have Jira access:

```json
{
  "mcpServers": {
    "jira": {
      "command": "python",
      "args": ["path/to/ai-shared-services/mcps/jira/server.py"],
      "env": {
        "JIRA_SERVER": "https://yourorg.atlassian.net",
        "JIRA_API_TOKEN": "your-token",
        "JIRA_EMAIL": "you@yourorg.com"
      }
    }
  }
}
```

## Acceptance Criteria Field Mapping

`get_story` extracts acceptance criteria from the description text under a literal "Acceptance Criteria" heading. Many Jira instances use a custom field instead (e.g., `customfield_10042`). To use a custom field, update `_extract_ac()` in `server.py`:

```python
def _extract_ac(description: str) -> str:
    # Replace with: return issue.fields.customfield_10042 or ""
    ...
```

## Scope and Permissions

- **Read-only by design.** Do not add write operations (status transitions, comment posting) without reviewing the audit/approval implications.
- Use a service account with minimum project access — not a personal account with org-wide access.
- Token scope: `read:jira-work` (Jira Cloud) is sufficient.

## Known Limitations

- `find_related_defects` uses a simple JQL pattern. Tune to your org's linking conventions (some teams use "relates to," others use custom link types).
- No caching — repeated calls hit the Jira API directly. Add caching if call volume is high.
- Acceptance criteria extraction assumes a heading-based format; custom fields require a code change (see above).
