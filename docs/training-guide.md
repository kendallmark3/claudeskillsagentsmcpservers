# Training Guide: Onboarding a New AI Shared Services Team Member

This is a structured curriculum for getting a new team member productive in this operating model within one week. It assumes the person already knows how to code and use an AI coding assistant (Claude Code, Copilot, etc.) — this guide is about the *operating model*, not the tool itself.

## Day 1 — Orient

**Goal:** Understand the mental model before touching any files.

1. Read the root `README.md`.
2. Read `docs/concepts.md` end to end.
3. Read one full example of each artifact type:
   - `skills/react-form-skill.md`
   - `agents/frontend-agent.md`
   - `mcps/jira/server.py`
   - `templates/feature-intent-template.md`

**Checkpoint:** Can you explain, in one sentence each, the difference between a skill, an agent, an MCP, and an intent file? If not, re-read `docs/concepts.md` — don't move on yet.

## Day 2 — Trace a Real Example

**Goal:** See the full loop run end-to-end on paper before running it for real.

1. Read `playbooks/feature-delivery-playbook.md` in full.
2. Walk through the "Customer Address Form" example referenced in the playbook. For each step, identify:
   - Which intent file field is being read
   - Which agent is acting
   - Which skill that agent is following
   - Which MCP (if any) is providing context
3. Write your own one-paragraph summary of the loop in your own words. Don't copy the README — the point is to internalize it.

**Checkpoint:** Could you draw the loop diagram from memory?

## Day 3 — Write Your First Intent File

**Goal:** Practice translating a real story into a usable intent file.

1. Pick a small, real (or realistic) Jira story from your team's backlog.
2. Copy `templates/feature-intent-template.md` and fill it out completely — objective, business outcome, acceptance criteria, constraints, evidence required.
3. Have a teammate or your lead review it. Common first-timer mistakes:
   - Acceptance criteria too vague to verify ("works well" is not testable)
   - Missing constraints (forgetting to say "use existing component library")
   - No evidence required section, so there's nothing to check the AI's work against

**Checkpoint:** Your intent file should be specific enough that two different people reading it would build approximately the same thing.

## Day 4 — Run the Loop on One Feature

**Goal:** Execute the full loop for the first time, start to finish.

1. Using your Day 3 intent file, select the right agent(s) from `agents/`.
2. Identify which skill(s) that agent should use from `skills/`.
3. If an MCP is relevant and already connected (Jira or GitHub, most likely), use it to pull real context instead of copy-pasting.
4. Run the implementation through your AI coding tool, instructing it explicitly to follow the agent definition and skill.
5. Collect the evidence output (files changed, tests added, commands run, assumptions, risks).
6. Open a PR and run it through `agents/pr-review-agent.md` before requesting human review.

**Checkpoint:** You should have a real PR with real evidence attached, traceable back to a real intent file.

## Day 5 — Reflect and Contribute

**Goal:** Turn your first loop into an improvement to the shared services repo.

1. What was unclear in the skill or agent file you used? Propose an edit.
2. Did you have to manually copy-paste context that an MCP could have retrieved? Note it as a candidate for the next MCP to build.
3. Was there a step in the playbook that didn't match reality? Open a PR to correct it.

**Checkpoint:** You've made at least one real contribution back to this repo based on lived experience, not speculation.

## After Week 1

- Pair with someone using a different agent (e.g., if you used Frontend Agent, pair on a Backend/API Agent task) to see the other side of the loop.
- Start tracking your own "first three skills, first three agents, first two MCPs" usage — are they covering most of your real work, or are there gaps?
- Revisit `docs/faq.md` for common questions that come up after the first real feature.

## Anti-Patterns to Watch For

- **Skipping the intent file** and just prompting directly — this is exactly the "random prompting" problem this model exists to solve.
- **Letting an agent go outside its lane** (e.g., Frontend Agent touching backend code without explicit instruction) — if this happens, the agent definition's Constraints section needs tightening, not just a one-off correction.
- **Treating MCPs as optional polish.** They're what keeps context accurate and current. Manual copy-paste of Jira tickets or Confluence pages reintroduces the exact problem this model is meant to solve.
- **Claiming success without evidence.** Every skill and agent template includes an evidence requirement on purpose. If the AI says "done" with no files-changed list, no test output, and no acceptance-criteria mapping, that's not done.
