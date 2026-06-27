# PR Review Skill

## Purpose

Use this skill when reviewing a pull request for correctness, completeness, safety, and alignment with its intent file.

## Rules

1. Always read the intent file before reading the PR diff — review against the stated outcome, not just code quality in isolation.
2. Treat missing tests as a blocking issue, not a suggestion, unless the intent file explicitly states tests are out of scope.
3. Flag any change outside the scope implied by the intent file, even if the change looks reasonable on its own.
4. Flag any new dependency that wasn't called for in the intent file's constraints.
5. Do not approve based on code style alone — confirm acceptance criteria are actually satisfied.
6. Note security or data-handling risks explicitly, even if they're not blocking.

## Required Steps

1. Read the intent file.
2. Read the PR summary and description.
3. Inspect all changed files.
4. Compare changes against each acceptance criterion individually — mark each as satisfied, partially satisfied, or not satisfied.
5. Check for missing or weak test coverage.
6. Check for unnecessary or out-of-scope changes.
7. Identify risk areas (security, data integrity, performance, backward compatibility).
8. Produce a recommendation: Approve, Approve with Comments, or Request Changes.

## Evidence Required

At the end of the work, provide:

- Recommendation (Approve / Approve with Comments / Request Changes)
- Acceptance-criteria-by-acceptance-criteria assessment
- Missing or weak test coverage, if any
- Out-of-scope changes found, if any
- Risk areas identified
- Required fixes (if any) vs. optional improvements
