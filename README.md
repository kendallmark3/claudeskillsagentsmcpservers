# AI Shared Services

> A complete operating model for engineering teams adopting AI coding tools — not as autocomplete, but as a structured part of delivery.

[![Lint Markdown](https://github.com/kendallmark3/claudeskillsagentsmcpservers/actions/workflows/lint-markdown.yml/badge.svg)](https://github.com/kendallmark3/claudeskillsagentsmcpservers/actions/workflows/lint-markdown.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](#license)

---

## The Problem

When AI coding tools land in an engineering org without structure, you get:

- **Inconsistency** — every engineer prompts differently, every result looks different
- **No auditability** — "the AI wrote it" means nothing to a code reviewer or compliance team
- **Stale context** — developers manually copy-paste Jira tickets, Confluence docs, and API contracts into prompts, then hope nothing changed
- **No accountability boundary** — the AI goes outside its lane, introduces unapproved dependencies, and nobody caught it in time

This repo solves all four.

---

## What It Is

A starter kit that a Shared AI / Developer Platform team can stand up on day one. It gives your teams a repeatable, auditable loop for AI-assisted software delivery:

```
Jira story
   ↓
Intent File — defines the outcome, constraints, and evidence required
   ↓
Agent — the right specialist for the job (Frontend, Backend, QA, Security)
   ↓
Skills — the agent's playbook for how to do the work
   ↓
MCPs — agents pull real context from Jira, GitHub, Confluence (no copy-paste)
   ↓
AI coding tool modifies the repo
   ↓
Evidence is produced — files changed, tests run, criteria mapped
   ↓
PR Review Agent + human reviewer make the final call
```

---

## The Four Layers

| Layer | Format | Purpose |
|---|---|---|
| **Skills** | Markdown | Define *how* work should be done |
| **Agents** | Markdown | Define *who* (which specialist) does the work |
| **MCPs** | Python / TypeScript | Connect AI to real systems with controlled, auditable access |
| **Intent Files** | Markdown | Define the *what* — the desired outcome and acceptance criteria |

Playbooks chain these together for common end-to-end workflows.

Read [docs/concepts.md](docs/concepts.md) for a deeper explanation of how they fit together.

---

## Repo Structure

```
ai-shared-services/
├── README.md                        ← you are here
├── ROADMAP.md                       ← what's next and how to contribute
├── CONTRIBUTING.md                  ← how to add skills, agents, and MCPs
├── docs/
│   ├── concepts.md                  ← Skills vs Agents vs MCPs vs Intent Files
│   ├── why.md                       ← the case for this model over random prompting
│   ├── team-benefits.md             ← per-role breakdown: what's in it for each team
│   ├── learning-playlist.md         ← curated reading paths by role
│   ├── training-guide.md            ← week-one onboarding curriculum
│   └── faq.md                       ← common questions after the first real feature
├── skills/
│   ├── feature-delivery-skill.md
│   ├── react-form-skill.md
│   ├── api-integration-skill.md
│   ├── pr-review-skill.md
│   ├── test-generation-skill.md
│   └── accessibility-skill.md
├── agents/
│   ├── frontend-agent.md
│   ├── backend-api-agent.md
│   ├── qa-agent.md
│   ├── architect-agent.md
│   ├── security-agent.md
│   └── pr-review-agent.md
├── mcps/
│   ├── jira/
│   │   ├── server.py                ← read-only Jira connector (Python)
│   │   └── README.md
│   ├── github/
│   │   ├── server.ts                ← read-only GitHub connector (TypeScript)
│   │   └── README.md
│   └── confluence/
│       ├── server.py                ← read-only Confluence connector (Python)
│       └── README.md
├── playbooks/
│   ├── feature-delivery-playbook.md ← Jira story → merged, evidenced PR
│   ├── pr-review-playbook.md        ← agent-assisted PR review workflow
│   ├── repo-onboarding-playbook.md  ← introducing this model to a new repo
│   └── release-readiness-playbook.md
├── templates/
│   ├── intent-template.md           ← blank intent file
│   ├── feature-intent-template.md   ← intent file with worked example
│   ├── pr-evidence-template.md      ← PR description with evidence scaffold
│   └── agent-output-template.md     ← standard agent response format
└── .github/
    ├── workflows/
    │   └── lint-markdown.yml        ← keeps skill/agent files consistent
    ├── ISSUE_TEMPLATE/
    │   ├── new-skill.md
    │   ├── new-agent.md
    │   └── new-mcp.md
    └── PULL_REQUEST_TEMPLATE.md
```

---

## Quick Start

### Week One

1. **Read** [docs/concepts.md](docs/concepts.md) — understand the mental model before touching files.
2. **Pick one real Jira story.** Don't start with theory.
3. **Fill out** [templates/feature-intent-template.md](templates/feature-intent-template.md) for that story.
4. **Assign an agent** — most features start with `frontend-agent.md` and/or `backend-api-agent.md`.
5. **Point the agent at the relevant skill** — e.g. `react-form-skill.md` for UI work.
6. **Wire up the first MCP** — start with `mcps/jira/` or `mcps/github/`, whichever removes the most manual copy-pasting today.
7. **Run the loop** and produce evidence.
8. **Improve this repo** based on what you learned. It's a living document — every real feature should make the next one slightly easier.

### Minimum Viable Adoption

You do not need all of this on day one. Start here:

| Layer | First 3 |
|---|---|
| Skills | Feature Delivery, API Integration, PR Review |
| Agents | Frontend, Backend/API, PR Review |
| MCPs | Jira, GitHub |

That's enough to run one complete delivery loop. Everything else in this repo is for when you need it.

---

## Who Benefits

| Role | Primary Value |
|---|---|
| **Frontend engineers** | Consistent UI patterns, accessibility by default, no invented dependencies |
| **Backend engineers** | API integration standards, test coverage expectations, evidence-driven PRs |
| **QA engineers** | Clear acceptance criteria in every intent file; QA Agent for structured test review |
| **Tech leads / architects** | Architect Agent reviews intent before a line of code is written |
| **Security teams** | Security Agent on every PR touching auth, secrets, or sensitive data |
| **Engineering managers** | Auditable evidence on every AI-assisted PR; no black-box "the AI did it" |

See [docs/team-benefits.md](docs/team-benefits.md) for the full breakdown.

---

## Why Markdown for Skills and Agents?

Because everyone on the team can read and edit it — developers, architects, QA, product owners. It lives in Git, so it gets versioned and reviewed like code. No platform required to start. A folder of well-written Markdown files is the entire MVP.

## Why Code for MCPs?

MCPs give the AI controlled, auditable access to systems of record (Jira, Confluence, GitHub, Figma, databases). The agent doesn't get unrestricted access to your company's systems — it gets a deliberate, limited set of approved tools. That's the difference between "AI that reads the internet" and "AI that reads exactly what it needs, with a paper trail."

---

## Roadmap

See [ROADMAP.md](ROADMAP.md) for what's next — upcoming MCPs, skills, agents, and integration opportunities.

---

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md). The short version:
- New skill or agent? Copy the nearest existing file, keep the section headers identical.
- New MCP? Document the tools it exposes and its auth model in `README.md` inside its folder.
- Found a gap from running a real feature? Open a PR. This repo lives on real experience, not speculation.

---

## Learning Paths

Not sure where to start? See [docs/learning-playlist.md](docs/learning-playlist.md) — curated reading sequences for each role.

---

## License

MIT. Adapt freely for your organization.
