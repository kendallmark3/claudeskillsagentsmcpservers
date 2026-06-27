# Contributing to AI Shared Services

This repo is meant to grow from real, lived delivery experience — not speculation about what *might* be useful. Please contribute accordingly.

## Adding a New Skill

1. Copy an existing skill file (e.g., `skills/api-integration-skill.md`) as your starting structure.
2. Keep the section headers identical: Purpose, Rules, Required Steps, Evidence Required. Consistency is what makes skills composable across agents.
3. Open a PR with a short note on what real situation prompted this skill.

## Adding a New Agent

1. Copy an existing agent file (e.g., `agents/backend-api-agent.md`).
2. Keep the section headers identical: Role, Responsibilities, Constraints, Skills You May Use, Output Format.
3. Make sure the new agent's lane doesn't overlap with an existing agent's. If it does, either narrow the new agent's Responsibilities or revise the existing agent's Constraints so the boundary is clear in both files.

## Adding a New MCP

1. Create a new folder under `mcps/`.
2. Include both the server code and a `README.md` describing: tools exposed, setup steps, scope/permissions, and known limitations (see `mcps/jira/` for the pattern).
3. Default to read-only. If write access is genuinely needed, call it out explicitly and explain the approval/audit story — don't bundle it in quietly.

## Adding or Updating a Playbook

1. Playbooks compose existing skills, agents, and MCPs — if you find yourself needing a new skill or agent to write a playbook, add that first.
2. Keep the format consistent: Purpose, When to Use This Playbook, Workflow diagram, Step-by-Step.

## Updating Based on Real Usage

If you ran a feature through this model and hit a gap — an agent went outside its lane, a skill's evidence requirement didn't match what was actually needed, an MCP's field mapping didn't match your Jira instance — open a PR with the fix. Reference the real situation in the PR description (no need to name specific tickets or systems if there's a confidentiality concern; a general description of the gap is enough).

## What Not to Do

- Don't add speculative skills/agents/MCPs for hypothetical future needs. Start with the minimum viable set in the README and expand from real gaps.
- Don't let agent definitions silently overlap.
- Don't add write-capable MCP tools without an explicit scope/permissions discussion in the PR.
- Don't remove the "Evidence Required" section from any skill or agent template — it's the mechanism that keeps "done" meaningful.
