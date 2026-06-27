# Team Benefits

Every role in an engineering org interacts with AI-assisted delivery differently. This document breaks down what this operating model does for each team — and, critically, what problem it solves that they've probably already hit.

---

## Frontend Engineers

**The problem before this model:** AI-generated UI code that introduces new state management libraries, ignores the existing design system, and skips accessibility. The engineer has to review and fix things that should never have been generated.

**What this model gives you:**

- **React Form Skill** — a playbook the AI follows every time, reusing existing components and conventions instead of inventing new ones
- **Accessibility Skill** — accessibility requirements aren't an afterthought; they're required steps in the skill
- **Frontend Agent** — explicit Constraints that prevent the AI from touching backend code, adding unapproved dependencies, or skipping tests
- **Evidence output** — every session ends with a list of files changed, components reused, tests added, and commands run — so reviewing AI-generated work is actually possible

**What to read first:** [skills/react-form-skill.md](../skills/react-form-skill.md), [agents/frontend-agent.md](../agents/frontend-agent.md)

---

## Backend / API Engineers

**The problem before this model:** AI-generated API code that doesn't match existing patterns, misses error handling, and adds dependencies that violate the team's standards. Or worse, code that looks correct but was generated without reading the actual API contract.

**What this model gives you:**

- **API Integration Skill** — forces the AI to read existing patterns before writing new ones, and requires it to verify contracts before assuming endpoints
- **Backend/API Agent** — stays in its lane (no frontend changes) and produces evidence the reviewer can check
- **GitHub MCP** — the agent reads the actual codebase instead of guessing
- **Confluence MCP** — pulls architecture standards directly, so the AI isn't working from a cached or hallucinated version of your standards

**What to read first:** [skills/api-integration-skill.md](../skills/api-integration-skill.md), [agents/backend-api-agent.md](../agents/backend-api-agent.md)

---

## QA Engineers

**The problem before this model:** AI writes code and claims it's tested. The "tests" are shallow, miss the failure cases, or were written after the fact to make the coverage number green. No structured verification that acceptance criteria were actually met.

**What this model gives you:**

- **QA Agent** — dedicated specialist for validating implementation against acceptance criteria before the PR opens
- **Test Generation Skill** — standard pattern for happy path, validation errors, and failure paths — not just the happy path the AI felt like writing
- **Intent files** — every feature has explicit acceptance criteria that the QA Agent checks against; "does it work" is never the entire question
- **Evidence requirements** — test commands must be run and results must be included; "tests pass" isn't asserted, it's demonstrated

**What to read first:** [agents/qa-agent.md](../agents/qa-agent.md), [skills/test-generation-skill.md](../skills/test-generation-skill.md)

---

## Tech Leads and Architects

**The problem before this model:** By the time a tech lead sees an AI-generated PR, the implementation decisions have already been made — often in ways that violate architectural standards the AI didn't know about, or that introduce complexity the team will have to live with for years.

**What this model gives you:**

- **Architect Agent** — reviews the intent file *before* implementation begins. Flag complexity, debt, and boundary violations at plan time, not at PR time.
- **Intent files** — structured format that makes it easy to see whether the proposed approach fits the existing system before any code is written
- **Constraints sections** — both in intent files and agent definitions, the tech lead can encode what the AI must not do (no new ORM, no new auth pattern, no new infrastructure) in a form that's enforced during the session and auditable afterward
- **Repo Onboarding Playbook** — structured process for introducing this model to a codebase in a way that captures its specific conventions and constraints

**What to read first:** [agents/architect-agent.md](../agents/architect-agent.md), [playbooks/repo-onboarding-playbook.md](../playbooks/repo-onboarding-playbook.md)

---

## Security Teams

**The problem before this model:** Security review happens late, is reactive, and relies on humans catching issues in a diff after the fact. AI-generated code that touches auth, input handling, or sensitive data goes through the same review process as any other code — which means it often gets the same shallow review.

**What this model gives you:**

- **Security Agent** — triggered automatically by the PR Review Playbook whenever a PR touches auth, secrets, input handling, or sensitive data. Runs before human review, not in parallel with it.
- **Read-only MCP defaults** — every MCP in this repo defaults to read-only. Write access requires an explicit decision, explicit scoping, and documented audit trail — it can't sneak in.
- **Evidence requirements** — AI-generated code arrives at security review with a paper trail: what was asked, what constraints were given, what was produced, what risks the agent identified.
- **Structured risk flagging** — agent output templates include a Risks and Assumptions section by design; the AI is expected to surface what it's uncertain about, not just deliver confident code.

**What to read first:** [agents/security-agent.md](../agents/security-agent.md), [playbooks/pr-review-playbook.md](../playbooks/pr-review-playbook.md)

---

## Engineering Managers

**The problem before this model:** AI adoption produces a productivity number that's hard to defend. "Engineers are shipping faster" — but what did the AI actually do? Is the code quality holding? Are we accumulating hidden debt? Is there any accountability when something goes wrong?

**What this model gives you:**

- **Auditability on every AI-assisted PR** — intent file, evidence output, agent assessment, human review decision. You can trace every AI-assisted PR back to the story it came from and the constraints it was given.
- **Consistent quality floor** — skills and agent definitions create a quality standard that applies to every engineer's AI-assisted work, not just the careful ones
- **Visible adoption gaps** — the structure makes it immediately obvious when a PR was produced without the model (no intent file, no evidence) vs. with it
- **A team that learns together** — Day 5 of the training guide requires every new team member to contribute back to this repo based on what they learned. The model grows from real usage, and that growth is visible in the repo's history.
- **No "the AI did it" excuses** — every AI-assisted PR has a human author who selected the agent, wrote the intent file, and approved the evidence. The AI is a tool, not an actor.

**What to read first:** [docs/training-guide.md](training-guide.md), [docs/concepts.md](concepts.md)

---

## DevOps / Platform Engineers

**The problem before this model:** Developers ask AI to help with infrastructure, deployment scripts, CI config, or database migrations without any guardrails. The output varies wildly, often doesn't match the team's IaC standards, and can be genuinely dangerous when it touches production systems.

**What this model gives you:**

- **A clear gap to fill** — the near-term roadmap includes a DevOps/Platform Agent and a Deployment Skill, both of which the platform team is best-positioned to write and own
- **MCP patterns** — the Jira, GitHub, and Confluence MCPs are production-ready examples; adding a PagerDuty, Datadog, or internal deploy API MCP follows the same pattern
- **Read-only defaults** — the MCP model makes it straightforward to give agents observability access (read CI status, read dashboard, read incident history) without giving them write access to production systems
- **Contribution path** — see [ROADMAP.md](../ROADMAP.md) and [CONTRIBUTING.md](../CONTRIBUTING.md) for how to add the platform-specific skills, agents, and MCPs your team needs

**What to read first:** [ROADMAP.md](../ROADMAP.md), [mcps/github/README.md](../mcps/github/README.md)

---

## Product Owners / Delivery Leads

**The problem before this model:** AI speeds up implementation but makes the gap between business intent and actual delivery harder to see. A story that takes one day instead of three still has to actually deliver what was asked.

**What this model gives you:**

- **Intent files** — the bridge between a Jira story (business intent) and what the AI is actually asked to build. If the intent file is wrong, the implementation will be wrong — in a way that's visible before implementation starts.
- **Acceptance criteria as first-class inputs** — every intent file includes acceptance criteria pulled from the story. The QA Agent checks the implementation against these criteria, not against what the AI decided was meant.
- **PR evidence** — a structured record of what was built, what was tested, and what was left open. The delivery lead can see what was deferred, what assumptions were made, and what risks remain.

**What to read first:** [templates/feature-intent-template.md](../templates/feature-intent-template.md), [docs/concepts.md](concepts.md)
