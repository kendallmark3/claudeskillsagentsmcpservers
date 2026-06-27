# PR Review Playbook

## Purpose

Workflow for reviewing a pull request that was produced using this operating model — ensuring evidence, acceptance criteria, and risk are checked before a human makes the final merge decision.

## When to Use This Playbook

Use this for every PR produced through an agent-assisted workflow, regardless of which feature playbook generated it.

## Workflow

```
1. Confirm the intent file exists and is linked from the PR
2. Confirm implementation evidence is attached (files changed, tests, commands run)
3. Run PR Review Agent using PR Review Skill
4. Run Security Agent if the PR touches auth, secrets, input handling, or sensitive data
5. Human reviewer makes the final call, using agent output as a starting point
6. Capture any gap between agent assessment and human assessment
```

## Step-by-Step

### 1. Confirm Intent File and Evidence Are Present

Before any review begins, the PR description should link to or include:

- The intent file used
- Evidence from the implementing agent(s): files changed, tests added, commands run, assumptions, risks

If this is missing, send it back before doing a deeper review — there's nothing to review *against* otherwise.

### 2. Run the PR Review Agent

- Apply `agents/pr-review-agent.md` using `skills/pr-review-skill.md`.
- The agent should produce a criterion-by-criterion assessment, not just a general impression.
- Pay particular attention to the "Missing Evidence" and "Issues Found" sections — these are where agent-implemented PRs most often fall short.

### 3. Run Security Review When Applicable

Trigger `agents/security-agent.md` if the PR touches any of:

- Authentication or authorization logic
- Secrets, tokens, or credential handling
- User input that flows into a query, command, or template
- New third-party dependencies
- Sensitive or regulated data (PII, financial, health)

If none of these apply, security review can be skipped for that PR, but document that decision rather than silently omitting it.

### 4. Human Final Review

- The human reviewer reads the PR Review Agent's output and the Security Agent's output (if run) before reading the diff in detail.
- The human reviewer makes the final approve/request-changes decision. Agent output is a strong starting point, not a substitute for judgment.

### 5. Capture Gaps

If the human reviewer disagrees with the agent's assessment (e.g., the agent said "Approve" but the human caught a real issue, or vice versa), log it. Recurring gaps are a signal that `skills/pr-review-skill.md` or `agents/pr-review-agent.md` needs revision — see `docs/training-guide.md`, Day 5.
