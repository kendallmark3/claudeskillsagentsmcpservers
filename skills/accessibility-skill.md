# Accessibility Skill

## Purpose

Use this skill any time UI is created or modified, to ensure the result is usable with assistive technology and meets the team's accessibility bar.

## Rules

1. All interactive elements must be reachable and operable via keyboard alone.
2. All form inputs must have associated, programmatically-linked labels.
3. Color must not be the only means of conveying state (e.g., error, success) — pair it with text or an icon with an accessible name.
4. Preserve or add ARIA attributes consistent with existing patterns in the repo — do not invent a new ARIA scheme.
5. Focus order must follow a logical reading order; do not trap focus unintentionally.
6. Images and icons that convey meaning must have appropriate alt text; purely decorative ones must be hidden from assistive technology.
7. Do not reduce existing accessibility coverage to ship a feature faster.

## Required Steps

1. Read the intent file and identify all new or modified interactive elements.
2. Inspect existing accessible components in the repo to match established patterns.
3. Implement or verify keyboard operability, labeling, and focus order.
4. Run any existing automated accessibility checks (e.g., axe, jest-axe) if present in the repo.
5. Manually note anything an automated check cannot verify (e.g., logical reading order, meaningful alt text).
6. Document what was verified and what remains a manual QA step.

## Evidence Required

At the end of the work, provide:

- Elements reviewed for accessibility
- Automated accessibility checks run, and results
- Manual checks performed
- Any known gaps and recommended follow-up
