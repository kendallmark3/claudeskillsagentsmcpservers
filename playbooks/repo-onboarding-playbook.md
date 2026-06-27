# Repo Onboarding Playbook

## Purpose

Workflow for introducing this Skills/Agents/MCPs operating model into a repository that doesn't have it yet — i.e., the first time you point an AI coding tool at an existing codebase using this model.

## When to Use This Playbook

Use this once per repository, the first time your team adopts this operating model there. Re-run portions of it any time a repo undergoes major architectural change.

## Workflow

```
1. Inventory existing patterns in the repo
2. Identify the repo's "source of truth" systems (Jira project, Confluence space, design tool)
3. Stand up or point to the ai-shared-services repo
4. Connect the first 1-2 MCPs for this repo's systems
5. Run a small, low-risk feature through the full loop as a pilot
6. Capture what's repo-specific vs. generic and document it
```

## Step-by-Step

### 1. Inventory Existing Patterns

Before writing any skill or agent customization, have the AI coding tool (or a human) inventory:

- Component library / design system in use
- API client pattern(s) already established
- Test framework and conventions
- Existing naming conventions and folder structure
- Any existing CI/CD checks that gate merges

This inventory becomes the "ground truth" agents and skills should defer to — it's why every skill in this repo says "inspect existing patterns before creating new ones."

### 2. Identify Source-of-Truth Systems

Document, in a repo-specific notes file (not in this shared repo):

- Jira project key(s) this repo's work lives under
- Confluence space(s) with relevant architecture standards
- Design tool (Figma, etc.) and project/file references
- Any other system of record this repo's features routinely need (e.g., a feature flag service, a specific internal API)

### 3. Point to ai-shared-services

- Either clone this repo alongside the target repo, or copy the relevant skills/agents into a `.ai/` folder inside the target repo, depending on your AI coding tool's conventions for discovering instruction files.
- Keep this shared repo as the source of truth for anything generic; only repo-specific overrides should live inside the target repo itself.

### 4. Connect the First MCP(s)

- Pick whichever MCP removes the most manual copy-pasting for this specific repo's workflow — usually Jira or GitHub.
- Follow the setup instructions in `mcps/jira/README.md` or `mcps/github/README.md`.
- Verify the connection with a read-only test call before involving it in real agent work.

### 5. Run a Pilot Feature

- Pick a small, low-risk, well-understood story.
- Run it through `playbooks/feature-delivery-playbook.md` in full.
- Pay close attention to where the generic skills/agents needed repo-specific adjustment — that's expected and valuable signal, not a failure of the model.

### 6. Document Repo-Specific Adaptations

Common things that need repo-specific tuning:

- Acceptance criteria field mapping in the Jira MCP (custom fields vary by org)
- Which design system components actually exist vs. what the skill assumes
- Test command(s) specific to this repo
- Any constraints unique to this repo (e.g., a legacy system that can't be touched, a deprecated pattern still in use that shouldn't be replicated)

Capture these in a short repo-specific addendum, and reference it from this shared repo's `docs/faq.md` if the adaptation is common enough to help other teams.
