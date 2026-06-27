# Core Concepts: Skills, Agents, MCPs, and Intent Files

If you remember nothing else from onboarding, remember this:

- **Skills = How we want work done**
- **Agents = Who should do the work**
- **MCPs = What systems the AI can connect to**
- **Intent Files = What outcome we are trying to deliver**

## The Operating Loop

```
Intent File
   ↓
Agent understands the assignment
   ↓
Agent follows the right Skills
   ↓
Agent uses MCPs to gather enterprise context
   ↓
AI coding tool modifies the repo
   ↓
PR evidence is produced
```

This is the loop every feature should run through. It replaces "random prompting" with a repeatable process.

## 1. Skills — Markdown Playbooks

A skill is a reusable instruction set describing how a certain kind of work should be performed. Most skills are simple Markdown files with:

- **Purpose** — when to use this skill
- **Rules** — constraints and conventions to follow
- **Required Steps** — the process, in order
- **Evidence Required** — what proof of work must be produced

Example: see `skills/react-form-skill.md`.

The point of a skill is consistency. Instead of every developer typing a different prompt for "build a form," the team has one playbook the AI follows every time.

**Bad instruction:** "Build this form."
**Good instruction:** "Build this form using the React Form Skill and the intent file."

## 2. Agents — Markdown Specialists

An agent is a specialized role definition. Where a skill describes a process, an agent describes a job description: what it specializes in, what it's responsible for, what it must never do, and what format it reports back in.

A skill is *how*. An agent is *who*.

| Skill | Agent |
|---|---|
| How to review a PR | PR Review Agent |
| How to build a React form | Frontend Agent |
| How to integrate APIs | Backend/API Agent |

Agents help divide work so the AI doesn't try to do everything at once — which is where most AI coding failures happen (backend changes nobody asked for, invented patterns, unapproved dependencies).

Example: see `agents/frontend-agent.md`.

## 3. MCPs — Code-Based Connectors

MCP stands for Model Context Protocol. MCPs are how AI tools reach systems of record in a controlled way — Jira, Confluence, GitHub, Figma, databases, internal APIs.

Skills and agents are Markdown. MCPs are code (typically Python or TypeScript).

A skill tells the AI: *follow this process.*
An agent tells the AI: *act as this specialist.*
An MCP lets the AI say: *go get the real information from the system of record.*

Without MCPs, developers copy-paste context into prompts by hand — slow, inconsistent, and easy to get wrong or stale. With MCPs, the agent retrieves approved context directly, and access is limited to a deliberate set of exposed tools rather than open browsing.

Example: see `mcps/jira/server.py` and `mcps/github/server.ts`.

## 4. Intent Files — What Outcome We Want

An intent file is the bridge between a business request (usually a Jira story) and the AI doing implementation work. It defines:

- The objective and business outcome
- The source story
- Acceptance criteria
- Constraints (what *not* to do — no new libraries, no new patterns without justification)
- Evidence required at the end

Example: see `templates/feature-intent-template.md`.

Intent files matter because "build this feature" is not enough context for repeatable results. The intent file is what keeps the agent from inventing requirements.

## How They Fit Together

```
Jira MCP        → pulls the source story + acceptance criteria
Confluence MCP  → pulls architecture standards
Figma MCP       → pulls design frames
        ↓
Frontend Agent  → uses React Form Skill
Backend Agent   → uses API Integration Skill
QA Agent        → uses Test Review Skill
        ↓
PR Review Agent → checks evidence against the intent file
```

This is the difference between "AI that writes code" and "AI that is part of the engineering system."

## Quick Reference Table

| Item | Usually Written In | Purpose | Example |
|---|---|---|---|
| Skill | Markdown | Defines how work should be done | React Form Skill |
| Agent | Markdown | Defines who/what specialist does the work | Frontend Agent |
| MCP | Python / TypeScript | Connects AI to external systems | Jira MCP |
| Intent File | Markdown | Defines the desired outcome | Customer Address Form Intent |

A skill is not an agent. An agent is not an MCP. An MCP is not a playbook. An intent file is not just a prompt. They all work together.
