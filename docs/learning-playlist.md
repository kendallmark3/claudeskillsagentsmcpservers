# Learning Playlist

Curated reading sequences for each role. Each playlist gets you to "productive in the model" as fast as possible — skipping what doesn't apply to you until you need it.

Every playlist starts the same way. After that, branch to your role.

---

## Everyone: Start Here (30–45 minutes)

These four items are the foundation. Don't skip them regardless of role.

1. [README.md](../README.md) — what the repo is, the loop, and where everything lives
2. [docs/concepts.md](concepts.md) — Skills vs Agents vs MCPs vs Intent Files, with the "why" for each
3. [docs/why.md](why.md) — why this model exists and what it's not
4. [templates/feature-intent-template.md](../templates/feature-intent-template.md) — read the blank template, then the worked example

**Checkpoint:** Can you explain in one sentence what each layer does and how they fit together? If not, re-read [docs/concepts.md](concepts.md) before moving on.

---

## Frontend Engineer

*Goal: ship your first AI-assisted UI feature through the full loop.*

1. **Foundation** — complete the Everyone playlist above
2. [agents/frontend-agent.md](../agents/frontend-agent.md) — your role definition, constraints, and output format
3. [skills/react-form-skill.md](../skills/react-form-skill.md) — the step-by-step for any form work
4. [skills/accessibility-skill.md](../skills/accessibility-skill.md) — non-optional; read before any UI work
5. [skills/test-generation-skill.md](../skills/test-generation-skill.md) — what test coverage the model expects
6. [playbooks/feature-delivery-playbook.md](../playbooks/feature-delivery-playbook.md) — the end-to-end workflow
7. [mcps/jira/README.md](../mcps/jira/README.md) — what the Jira MCP gives you (no more copy-pasting stories)
8. [docs/training-guide.md](training-guide.md) — the week-one curriculum; do Days 3–4 with a real story

**First action:** Pick a small, real story. Write the intent file. Run the frontend loop once.

---

## Backend / API Engineer

*Goal: ship your first AI-assisted API feature with proper evidence.*

1. **Foundation** — complete the Everyone playlist above
2. [agents/backend-api-agent.md](../agents/backend-api-agent.md) — your role definition, constraints, and output format
3. [skills/api-integration-skill.md](../skills/api-integration-skill.md) — the step-by-step for any API work
4. [skills/test-generation-skill.md](../skills/test-generation-skill.md) — what test coverage the model expects
5. [skills/feature-delivery-skill.md](../skills/feature-delivery-skill.md) — the delivery standard that wraps everything
6. [mcps/github/README.md](../mcps/github/README.md) — what the GitHub MCP gives you (real codebase context, not guesswork)
7. [mcps/confluence/README.md](../mcps/confluence/README.md) — pulling architecture standards directly instead of from memory
8. [playbooks/feature-delivery-playbook.md](../playbooks/feature-delivery-playbook.md) — the end-to-end workflow
9. [docs/training-guide.md](training-guide.md) — Days 3–4

**First action:** Wire up the GitHub MCP. Run one backend task through it and compare the context quality vs. copy-paste.

---

## QA Engineer

*Goal: use the QA Agent to validate an AI-assisted PR before it reaches human review.*

1. **Foundation** — complete the Everyone playlist above
2. [agents/qa-agent.md](../agents/qa-agent.md) — your role definition and what structured test review looks like
3. [skills/test-generation-skill.md](../skills/test-generation-skill.md) — the test coverage standard the model enforces
4. [skills/pr-review-skill.md](../skills/pr-review-skill.md) — how PRs are reviewed in this model
5. [playbooks/pr-review-playbook.md](../playbooks/pr-review-playbook.md) — when QA fits into the review workflow
6. [playbooks/feature-delivery-playbook.md](../playbooks/feature-delivery-playbook.md) — Step 5: QA Validation
7. [templates/pr-evidence-template.md](../templates/pr-evidence-template.md) — what you're reviewing *against*
8. [mcps/jira/README.md](../mcps/jira/README.md) — `find_related_defects` is particularly relevant for QA

**First action:** Take a recent PR that was produced through the model and run the QA Agent against it. Compare its output to what the human reviewer caught.

---

## Tech Lead / Architect

*Goal: stand up this model in your team's repo and enforce quality at the intent level, not the PR level.*

1. **Foundation** — complete the Everyone playlist above
2. [agents/architect-agent.md](../agents/architect-agent.md) — when and how to use the Architect Agent
3. [playbooks/repo-onboarding-playbook.md](../playbooks/repo-onboarding-playbook.md) — the structured process for introducing this model to your codebase
4. [CONTRIBUTING.md](../CONTRIBUTING.md) — how skills and agents should be written and maintained
5. [docs/faq.md](faq.md) — common questions you'll get from your team; read before your first enablement session
6. [ROADMAP.md](../ROADMAP.md) — where to contribute based on your team's gaps
7. All six agent files — you need to know every agent's lane and constraints before you can keep them from drifting
8. [docs/training-guide.md](training-guide.md) — full curriculum; you'll be running this for your team

**First action:** Run the Repo Onboarding Playbook on your team's primary repo. Start with the inventory step — it's faster than you think and surfaces things everyone has been assuming.

---

## Security Engineer

*Goal: use the Security Agent and understand the MCP access model before signing off on AI-assisted PRs.*

1. **Foundation** — complete the Everyone playlist above
2. [agents/security-agent.md](../agents/security-agent.md) — what the Security Agent checks and when to trigger it
3. [playbooks/pr-review-playbook.md](../playbooks/pr-review-playbook.md) — Step 3: when Security Agent runs and how its output feeds human review
4. [mcps/jira/README.md](../mcps/jira/README.md) — read the Scope and Permissions section; understand what access is granted
5. [mcps/github/README.md](../mcps/github/README.md) — same; especially the token scoping guidance
6. [mcps/confluence/README.md](../mcps/confluence/README.md) — same
7. [docs/why.md](why.md) — the "Why Code for MCPs" section; the read-only default is a security design decision
8. [CONTRIBUTING.md](../CONTRIBUTING.md) — the "Adding a New MCP" section; you should review any new MCP before it ships

**First action:** Review all three existing MCP READMEs for scope/permissions. Flag any that need tightening before your team connects them to real credentials.

---

## Engineering Manager

*Goal: understand the adoption model, the auditability story, and how to measure whether this is working.*

1. **Foundation** — complete the Everyone playlist above
2. [docs/team-benefits.md](team-benefits.md) — the per-role value proposition you'll use when enabling your team
3. [docs/training-guide.md](training-guide.md) — the full onboarding curriculum; know what Day 5 asks of your team
4. [playbooks/feature-delivery-playbook.md](../playbooks/feature-delivery-playbook.md) — the full workflow, end to end
5. [playbooks/pr-review-playbook.md](../playbooks/pr-review-playbook.md) — the review standard; this is where auditability lives
6. [templates/pr-evidence-template.md](../templates/pr-evidence-template.md) — what an evidenced AI-assisted PR looks like
7. [ROADMAP.md](../ROADMAP.md) — where the model is going; important for setting expectations
8. [docs/faq.md](faq.md) — who owns this, how it evolves, what common objections look like

**First action:** Have one engineer on your team run their next feature through the full loop. Review the intent file before they start and the PR evidence after. That one loop will tell you more than reading anything in this repo.

---

## DevOps / Platform Engineer

*Goal: understand the MCP model deeply enough to build new connectors and own the platform-level skills.*

1. **Foundation** — complete the Everyone playlist above
2. [mcps/jira/server.py](../mcps/jira/server.py) — read the implementation end to end
3. [mcps/jira/README.md](../mcps/jira/README.md) — the pattern every MCP README follows
4. [mcps/github/server.ts](../mcps/github/server.ts) — the TypeScript equivalent
5. [mcps/confluence/server.py](../mcps/confluence/server.py) — another Python example
6. [CONTRIBUTING.md](../CONTRIBUTING.md) — "Adding a New MCP" section
7. [ROADMAP.md](../ROADMAP.md) — the near-term MCP additions; Figma, Linear, Datadog, and PagerDuty are the highest-value next connectors
8. [docs/why.md](why.md) — "Why Code for MCPs" and the read-only rationale

**First action:** Pick the MCP from the roadmap that would unblock your team most. Write the server code following the Jira or GitHub pattern. Open a PR with the README filled out per the contributing guide.

---

## New to AI Coding Tools Entirely

*If this is your first week using an AI coding assistant as part of software delivery, start here.*

1. **Foundation** — complete the Everyone playlist above
2. [docs/training-guide.md](training-guide.md) — follow Days 1–5 in order
3. [docs/faq.md](faq.md) — read after Day 2, not before
4. Your role playlist above (come back to it after Day 2 of the training guide)

The training guide exists precisely for this path. Don't skip Day 1 (orient) and jump to Day 4 (run the loop). The mental model is the prerequisite for everything else.
