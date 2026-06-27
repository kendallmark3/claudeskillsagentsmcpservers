# Release Readiness Playbook

## Purpose

Workflow for rolling up evidence from multiple agent-assisted PRs into a release-readiness assessment, so a release decision is based on aggregated evidence rather than re-litigating each PR from scratch.

## When to Use This Playbook

Use this before any release (sprint-end, scheduled release train, or ad hoc deployment) that bundles multiple features delivered through this operating model.

## Workflow

```
1. Collect intent files and PR evidence for every feature in the release
2. Re-verify acceptance criteria status for each feature (not just "merged" status)
3. Aggregate risk areas flagged by QA Agent, Security Agent, and PR Review Agent across all PRs
4. Identify cross-feature regression risk (features that touch overlapping code/data)
5. Produce a release-readiness summary
6. Human release owner makes the go/no-go call
```

## Step-by-Step

### 1. Collect Evidence

For each feature going into the release, gather:

- The intent file
- The implementing agent(s)' evidence output
- The QA Agent's acceptance criteria assessment
- The PR Review Agent's recommendation
- The Security Agent's assessment, if it was run

Missing any of these for a given feature is itself a release-readiness finding — flag it rather than assuming it was fine.

### 2. Re-Verify Acceptance Criteria

"Merged" is not the same as "verified working." For each feature, confirm the QA Agent's per-criterion assessment is actually marked pass, not partially-satisfied or unverified. Anything not fully passing needs an explicit decision: fix before release, or accept and document the gap.

### 3. Aggregate Risk

Pull every "Issues Found," "Risks or assumptions," and Security Agent finding across all PRs in the release into one list. Look specifically for:

- Repeated risk patterns across multiple features (a signal of a systemic issue, not isolated ones)
- Any "Required Fixes" that were flagged but not confirmed resolved

### 4. Cross-Feature Regression Check

Identify features in this release that touched overlapping files, shared components, or the same data models. Run `agents/qa-agent.md` specifically against that overlap if it wasn't already covered by individual feature QA passes — multi-feature interactions are exactly what single-feature QA can miss.

### 5. Produce the Release-Readiness Summary

Format:

```
# Release Readiness Summary — [Release Name / Date]

## Features Included
- ...

## Acceptance Criteria Status
- [Feature]: Pass / Gap (with explanation)

## Aggregated Risks
- ...

## Cross-Feature Regression Risk
- ...

## Recommendation
Go / No-Go / Go with documented exceptions
```

### 6. Human Go/No-Go Decision

The human release owner makes the final call using this summary. Documented exceptions (known gaps being accepted deliberately) should be explicit, not implied.
