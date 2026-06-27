# Feature Delivery Playbook

## Purpose

End-to-end workflow for taking a Jira story from "backlog" to a merged, evidenced PR using the Skills/Agents/MCPs operating model.

## When to Use This Playbook

Use this for any net-new feature or significant change that has a corresponding Jira story and touches both frontend and backend (or either alone — skip the agent step for whichever side isn't involved).

## Workflow

```
1. Jira MCP retrieves the source story
2. Confluence MCP retrieves relevant architecture standards
3. Figma MCP retrieves design context (if UI is involved)
4. Intent file is written from the above
5. Architect Agent reviews the intent for architectural fit (optional but recommended for non-trivial features)
6. Frontend Agent implements UI using React Form Skill (or equivalent)
7. Backend/API Agent implements API using API Integration Skill
8. QA Agent validates implementation against acceptance criteria
9. PR Review Agent reviews the resulting PR using PR Review Skill
10. Human reviewer makes the final merge decision
```

## Step-by-Step

### 1. Gather Context

- Pull the story via the Jira MCP: title, description, acceptance criteria, comments, links.
- Pull relevant architecture standards via the Confluence MCP.
- Pull design frames via the Figma MCP if the story involves UI.

### 2. Write the Intent File

- Copy `templates/feature-intent-template.md`.
- Fill in Objective, Business Outcome, Source Story, Acceptance Criteria, Constraints, and Evidence Required using the context gathered in Step 1.
- Do not skip Constraints — this is what keeps agents from introducing unapproved dependencies or patterns.

### 3. Architectural Review (Recommended for Non-Trivial Features)

- Run the intent file past `agents/architect-agent.md`.
- Resolve any flagged complexity, debt, or dependency concerns before implementation starts — it's cheaper to fix the plan than the code.

### 4. Implementation

- **Frontend work:** Assign `agents/frontend-agent.md`, using `skills/react-form-skill.md` and `skills/accessibility-skill.md` as relevant.
- **Backend work:** Assign `agents/backend-api-agent.md`, using `skills/api-integration-skill.md`.
- Both agents should also apply `skills/test-generation-skill.md` and `skills/feature-delivery-skill.md`.
- Each agent inspects the existing repo before writing new code, and produces evidence per its Output Format.

### 5. QA Validation

- Run `agents/qa-agent.md` against the implementation and the intent file.
- Resolve anything marked "fail" or "unverified" before opening the PR, or document explicitly why it's deferred.

### 6. PR Review

- Open the PR with the implementation evidence from Steps 4–5 included in the description.
- Run `agents/pr-review-agent.md` using `skills/pr-review-skill.md` before requesting human review.
- The agent's output (Approve / Approve with Comments / Request Changes) is a starting point for the human reviewer, not a final decision.

### 7. Human Review and Merge

- A human reviewer makes the final call, informed by the PR Review Agent's structured output.
- Capture any gaps discovered during human review as a candidate skill/agent improvement (see `docs/training-guide.md`, Day 5).

## Worked Example: Customer Address Form

See `templates/feature-intent-template.md` for a filled-out example based on a fictional story `CUST-4821` — a form allowing customers to add or update their mailing address. Walking through that example against this playbook is a good first exercise for new team members (see `docs/training-guide.md`, Day 2).
