# Test Generation Skill

## Purpose

Use this skill when adding or updating automated tests for a feature, fix, or refactor.

## Rules

1. Match the existing test framework and conventions already in the repo — do not introduce a new testing library.
2. Cover the happy path, at least one validation/error path, and at least one edge case tied to the acceptance criteria.
3. Tests should be deterministic — no reliance on real network calls, real timers, or unseeded randomness.
4. Name tests so that a failure message alone tells a reviewer what broke and why it matters.
5. Do not delete or weaken existing tests to make new ones pass.
6. Mock external systems (APIs, databases) consistent with existing mocking patterns in the repo.

## Required Steps

1. Read the intent file's acceptance criteria.
2. Identify the existing test patterns for similar code in the repo.
3. Map each acceptance criterion to at least one test case.
4. Write or update the tests.
5. Run the full relevant test suite, not just the new tests, to check for regressions.
6. Document any acceptance criteria that could not be meaningfully tested and why.

## Evidence Required

At the end of the work, provide:

- Tests added or updated, with file paths
- Acceptance criteria mapped to specific test cases
- Test command executed and result summary
- Any acceptance criteria not covered by automated tests, with rationale
- Any flaky or skipped tests encountered
