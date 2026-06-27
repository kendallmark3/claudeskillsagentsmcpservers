---
name: New MCP
about: Propose a new Model Context Protocol connector
labels: mcp
---

## What system does this MCP connect to?

_Name of the external system (e.g., Figma, Linear, PagerDuty, Datadog, internal API)._

## What problem does it solve?

_What context are developers currently copy-pasting manually that this MCP would retrieve automatically? Be specific._

## Proposed tools to expose

_List the read operations first. Only include write operations if genuinely necessary — and if so, explain the approval/audit story for each write._

| Tool | Description | Read or Write? |
|---|---|---|
| `get_X()` | | Read |

## Auth model

_How would this MCP authenticate? Service account? API key? OAuth? What's the minimum scope required?_

## Language

_Python or TypeScript? (Follow the existing pattern in `mcps/` for the system's typical SDK language.)_

## Known limitations or risks

_Any rate limits, pagination issues, field mapping concerns, or write-access risks to flag upfront?_

## Which agents would use this MCP?

_List the agent(s) that would pull context from this connector._
