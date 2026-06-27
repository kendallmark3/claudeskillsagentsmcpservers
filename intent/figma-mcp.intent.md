# Feature Intent: Figma MCP

## Objective

Build a read-only Figma MCP that gives agents direct access to design frames, component specs, and file metadata — eliminating the need for developers to manually screenshot or copy-paste design context into prompts.

## Business Outcome

Frontend agents can retrieve the correct design frame and component specs for any story automatically, reducing context errors and cutting the time between "story assigned" and "implementation started."

## Source Story

ROADMAP.md — Near-Term MCPs: Figma

## Acceptance Criteria

1. `get_file(file_key)` returns file name, last modified date, and top-level frame list.
2. `get_frame(file_key, node_id)` returns frame name, dimensions, and child component names.
3. `get_component_styles(file_key, node_id)` returns fill colors, typography, spacing, and border radius for a given node.
4. `list_frames(file_key)` returns all top-level frames with their node IDs.
5. All tools are read-only — no write or publish operations exposed.
6. Authentication uses a Figma personal access token or OAuth token passed via environment variable (`FIGMA_TOKEN`), never hardcoded.
7. A `README.md` documents: tools exposed, setup steps, token scope required, known limitations.
8. The MCP follows the same file structure pattern as `mcps/jira/` and `mcps/confluence/`.

## Constraints

- Read-only. Do not expose any write, publish, or comment-posting tools.
- Must follow the Python or TypeScript pattern established in existing MCPs — check which Figma SDK is most mature before choosing.
- Do not introduce a new HTTP client library if `requests` (Python) or `axios`/`fetch` (TypeScript) already suffices.
- Token must be injected via environment variable; document this in the README.
- Must include a `requirements.txt` (Python) or `package.json` (TypeScript) with pinned dependency versions.

## Existing Patterns to Inspect

- `mcps/jira/server.py` — Python MCP structure, error handling, tool registration pattern
- `mcps/github/server.ts` — TypeScript equivalent
- `mcps/jira/README.md` — README format: tools table, setup steps, scope/permissions, known limitations
- `CONTRIBUTING.md` — "Adding a New MCP" section

## APIs Involved

- Figma REST API: `GET /v1/files/:file_key` — file metadata and node tree
- Figma REST API: `GET /v1/files/:file_key/nodes?ids=:node_id` — specific node data
- Figma REST API: `GET /v1/files/:file_key/components` — component list
- Base URL: `https://api.figma.com`
- Auth: `X-Figma-Token` header

## Data Involved

- Design frame metadata: name, dimensions, node IDs
- Component styles: colors, typography, spacing (non-sensitive)
- No PII, no secrets, no financial data

## Tests Required

- `get_file()` with a valid file key returns expected structure
- `get_frame()` with a valid node ID returns style properties
- Missing or invalid `FIGMA_TOKEN` raises a clear, actionable error (not a stack trace)
- `list_frames()` returns at least one frame for a known test file

## Evidence Required

- Files created (server file + README + dependency file)
- Tools table in README completed and accurate
- Token setup instructions verified against the actual Figma API
- Read-only constraint confirmed: no write tools exposed
- Known limitations documented (e.g., no vector/SVG export, no prototype data)
