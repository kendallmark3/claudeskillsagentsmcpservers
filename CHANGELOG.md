# Changelog

All notable changes to this repo are documented here.
Format follows [Keep a Changelog](https://keepachangelog.com/en/1.0.0/).

---

## [Unreleased]

### Planned
- Figma MCP — read-only design frame and component access (see `intent/figma-mcp.intent.md`)
- Linear MCP — Linear equivalent of the Jira MCP (see `intent/linear-mcp.intent.md`)
- Deployment Skill — pre-deploy gates, smoke checks, rollback criteria (see `intent/deployment-skill.intent.md`)
- Incident Response Playbook — alert → triage → mitigation → post-mortem (see `intent/incident-response-playbook.intent.md`)

---

## [1.1.0] — 2026-06-27

### Added
- **Runnable MCP servers** — all three MCPs are now proper, runnable servers using the official SDKs
  - Jira and Confluence: rewritten with FastMCP (`mcp` Python package) and `@mcp.tool()` decorators
  - GitHub: rewritten with `@modelcontextprotocol/sdk` `McpServer` class
- **Dependency files** — `requirements.txt` for Python MCPs; `package.json` + `tsconfig.json` for GitHub MCP
- **`mcps/.env.example`** — centralized reference for all MCP environment variables with comments
- **Docker infrastructure** — `Dockerfile` for each MCP; `mcps/docker-compose.yml` for running all three as persistent services
- **`mcps/README.md`** — complete setup guide covering local stdio and Docker/cloud deployment, with Claude Code registration snippets
- **Intent files** — `/intent/` directory with intent files for the five highest-priority ROADMAP items
- **`.markdownlint.json`** — explicit lint ruleset so local and CI behavior match
- **`CHANGELOG.md`** — this file
- **GitHub templates** — PR template + issue templates for new-skill, new-agent, new-mcp
- **Scorecard skill** — `/git-scorecard`, `/create-report-card`, `/daily-snapshot` Claude Code commands installed

### Updated
- All MCP `README.md` files updated with install commands, Claude Code registration snippets, and field mapping guidance
- `README.md` updated to reference `/intent/` directory and new docs
- `repo-scorecard.md` updated to reflect v1.1 improvements

### Fixed
- MCP code no longer requires undocumented manual setup steps to run

---

## [1.0.0] — 2026-06-27

### Added
- Initial release: complete Skills/Agents/MCPs operating model
- **6 skills**: Feature Delivery, React Form, API Integration, PR Review, Test Generation, Accessibility
- **6 agents**: Frontend, Backend/API, QA, Architect, Security, PR Review
- **3 MCP starters**: Jira, GitHub, Confluence (read-only)
- **4 playbooks**: Feature Delivery, PR Review, Repo Onboarding, Release Readiness
- **Templates**: Intent, Feature Intent (with worked example), PR Evidence, Agent Output
- **Docs**: concepts, why, team-benefits, learning-playlist, training-guide, FAQ
- **CI**: Markdown lint on PR and push to main
- **Contributing guide** with conventions for skills, agents, MCPs, and playbooks
