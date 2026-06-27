# Agent Output Template

Use this as the standard structure for any agent's final response, regardless of which agent ran. Individual agent files may specify a more specific format (e.g., PR Review Agent's "PR Review Summary" format) — defer to that when it exists. Use this generic version for agents that don't specify their own.

## Agent

[Which agent produced this output — e.g., Frontend Agent, Backend/API Agent]

## Intent File Reference

[Link or path to the intent file this work addresses]

## Summary of Changes

[What was done, in plain language]

## Files Modified

- [path/to/file]
- [path/to/file]

## Tests Added or Updated

- [Test file/case and what it covers]

## Commands Run

```
[exact commands executed]
```

## Acceptance Criteria Satisfied

- [Criterion]: [how it was satisfied / verified]

## Risks or Assumptions

- [Anything uncertain, deferred, or assumed due to ambiguity]

## Recommended Next Step

[e.g., hand off to QA Agent, ready for PR, needs Architect Agent review first]
