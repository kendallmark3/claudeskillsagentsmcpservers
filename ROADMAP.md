# Roadmap

This roadmap tracks what's in the current release, what's being built next, and where contributions are most needed. It's maintained in order of practical impact — things that unlock the most teams, fastest, come first.

---

## v1.0 — Current Release

**Status: Shipped**

The foundation is in place. This release gives any team enough to run one complete delivery loop on day one.

### MCPs
- [x] Jira — read-only story, acceptance criteria, comments, links
- [x] GitHub — read-only PR, files, commits, comments, CI status
- [x] Confluence — read-only page and space content

### Skills
- [x] Feature Delivery
- [x] React Form
- [x] API Integration
- [x] PR Review
- [x] Test Generation
- [x] Accessibility

### Agents
- [x] Frontend Agent
- [x] Backend/API Agent
- [x] QA Agent
- [x] Architect Agent
- [x] Security Agent
- [x] PR Review Agent

### Playbooks
- [x] Feature Delivery (Jira story → merged PR)
- [x] PR Review
- [x] Repo Onboarding
- [x] Release Readiness

### Infrastructure
- [x] Markdown lint CI
- [x] Contributing guide
- [x] Training curriculum (5-day onboarding)
- [x] FAQ
- [x] GitHub issue templates and PR template

---

## Near-Term (Next 90 Days)

These are the highest-leverage additions based on what teams most commonly need after their first real loop.

### MCPs

| MCP | Status | Value |
|---|---|---|
| **Figma** | Planned | Design-to-code without screenshots or copy-pasted specs |
| **Linear** | Planned | For teams using Linear instead of Jira |
| **Slack** | Planned | Pull thread context for incident response or architectural decisions |
| **PagerDuty** | Planned | Surface incident history during security or reliability reviews |
| **Datadog / Observability** | Planned | Let agents check dashboards during release readiness assessments |
| **Internal OpenAPI Registry** | Planned | Agents discover real API contracts instead of assuming them |

### Skills

| Skill | Status | Value |
|---|---|---|
| **Database Migration Skill** | Planned | Safe schema change patterns, rollback plan, data backfill rules |
| **Deployment Skill** | Planned | Step-by-step deploy checklist composable with Release Readiness playbook |
| **Incident Response Skill** | Planned | Structured approach for on-call agents during active incidents |
| **Data Pipeline Skill** | Planned | ETL/ELT patterns, idempotency, backfill safety |
| **Mobile (React Native) Skill** | Planned | Platform-specific conventions, accessibility on mobile |
| **GraphQL Skill** | Planned | Schema-first, resolver conventions, query complexity |

### Agents

| Agent | Status | Value |
|---|---|---|
| **DevOps / Platform Agent** | Planned | CI/CD, infrastructure-as-code, deploy pipeline ownership |
| **Data Agent** | Planned | Data pipelines, migrations, query review |
| **Incident Commander Agent** | Planned | Coordinates response, pulls PagerDuty + Datadog + Slack context |

### Playbooks

| Playbook | Status | Value |
|---|---|---|
| **Incident Response Playbook** | Planned | End-to-end: alert → triage → mitigation → post-mortem |
| **Data Migration Playbook** | Planned | Safe path from schema change to production cutover |
| **Dependency Upgrade Playbook** | Planned | Audit, test, and document a major version bump |

---

## Medium-Term (3–6 Months)

### CI/CD Integration

- Automatic evidence collection on PR open (agent runs as part of CI, posts structured output as a PR comment)
- Intent file linting in CI — catch missing fields before the loop runs
- Agent-output validation — confirm evidence format matches the template before human review

### Metrics and Observability

- Loop adoption dashboard: how many PRs ran through an intent file vs. not?
- Skills coverage report: which skills are referenced most/least in real PRs?
- Agent drift detection: flag when an agent's output no longer matches its defined output format

### Multi-Repo Support

- Shared services registry: a central index of which repos have adopted which agents and MCPs
- Override system: repo-level skill/agent overrides that compose cleanly with this shared repo

---

## How to Contribute

The fastest path from idea to merged contribution:

1. **Check the issue tracker** — if your idea is already filed, comment on it.
2. **Open an issue using the relevant template** — [New Skill](.github/ISSUE_TEMPLATE/new-skill.md), [New Agent](.github/ISSUE_TEMPLATE/new-agent.md), or [New MCP](.github/ISSUE_TEMPLATE/new-mcp.md).
3. **Reference a real situation** — what gap did you hit running a real feature? What would this have prevented?
4. **Start from an existing file** — copy the nearest example and keep the section headers identical.
5. **Open a PR** using the [PR template](.github/PULL_REQUEST_TEMPLATE.md) — include what real scenario prompted the change.

The most valued contributions are ones that came from shipping actual features, not ones imagined in advance. A skill that fixed a real problem is worth ten hypothetical ones.

---

## What We Are Not Building

To keep this repo focused:

- **No web UI, no dashboard, no SaaS** — this is a Markdown + code repo by design. The constraint is a feature.
- **No vendor lock-in** — every MCP, skill, and agent should work with Claude Code, Copilot, Cursor, or any other AI coding tool that can read instructions and connect to MCP servers.
- **No speculative skills** — if nobody has needed it on a real feature yet, it doesn't belong in the near-term roadmap.
