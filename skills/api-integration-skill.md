# API Integration Skill

## Purpose

Use this skill when integrating with an existing internal or external API, or when adding a new backend endpoint that a frontend will consume.

## Rules

1. Inspect the existing API client pattern in the repo before writing new integration code.
2. Reuse existing authentication, retry, and error-handling conventions.
3. Do not introduce a new HTTP client library unless the intent file explicitly requires it.
4. Validate the request and response shape against the documented or observed API contract.
5. Handle and surface errors in a way consistent with how the rest of the codebase handles them.
6. Do not hardcode credentials, tokens, or environment-specific URLs.
7. Add timeout and failure-mode handling — do not assume the API always succeeds.

## Required Steps

1. Read the intent file, including which APIs are involved.
2. Locate similar integrations in the repo (existing API clients, DTOs, hooks).
3. Confirm the API contract (via documentation, OpenAPI spec, MCP-sourced ticket detail, or existing usage in the repo).
4. Implement the integration using existing conventions.
5. Add or update tests, including at least one failure-path test.
6. Run the relevant test command.
7. Document what changed and what contract assumptions were made.

## Evidence Required

At the end of the work, provide:

- Files changed
- API endpoint(s) used
- Contract source (docs, spec, MCP ticket reference, or existing code)
- Tests added, including failure-path coverage
- Test command executed
- Any assumptions made about the contract
- Any gaps or follow-up work (e.g., contract not fully confirmed)
