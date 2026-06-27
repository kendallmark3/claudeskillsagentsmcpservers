# Feature Intent: Deployment Skill

## Objective

Create a reusable Deployment Skill that gives agents a step-by-step checklist for safely deploying a feature to production — covering pre-deploy gates, the deploy action itself, smoke verification, and rollback criteria.

## Business Outcome

Deployments driven by agents follow a consistent, documented process rather than depending on individual developer judgment. Every deployment produces structured evidence that it was checked before, during, and after the deploy.

## Source Story

ROADMAP.md — Near-Term Skills: Deployment Skill

## Acceptance Criteria

1. Skill defines a **pre-deploy gate** checklist: CI passing, intent file linked, PR merged, tests green, migrations reviewed (if any), feature flags checked.
2. Skill defines a **deploy step** that is environment-aware: staging vs. production have different verification requirements.
3. Skill defines a **post-deploy smoke check**: specific signals that confirm the deploy is healthy (health endpoint, key user flow, error rate, latency).
4. Skill defines a **rollback trigger**: explicit conditions under which the agent should recommend rollback, and what evidence to collect before doing so.
5. Skill includes an **Evidence Required** section: what the agent must produce at the end of any deployment session.
6. Skill is composable with `playbooks/release-readiness-playbook.md` — it should be referenced from that playbook in a follow-up update.
7. Follows the same section structure as all other skills: Purpose / Rules / Required Steps / Evidence Required.

## Constraints

- The skill is tool-agnostic: it should not reference any specific CI provider, cloud platform, or deploy tool. Use placeholders (`your deploy command`, `your health endpoint`) that teams fill in per-repo.
- Do not add platform-specific scripts — that belongs in a DevOps/Platform Agent, not the skill.
- Must not skip the rollback section — that section is the most important part of a deployment skill and must not be optional.
- Follow the formatting conventions of `skills/feature-delivery-skill.md`.

## Existing Patterns to Inspect

- `skills/feature-delivery-skill.md` — section structure and tone
- `skills/api-integration-skill.md` — how rules are written
- `playbooks/release-readiness-playbook.md` — this skill should eventually be composable with it
- `agents/backend-api-agent.md` — the agent that will most commonly invoke this skill

## APIs Involved

None. This is a Markdown skill, not a code connector.

## Data Involved

None directly. The skill references environment-specific config (health endpoints, feature flag keys) that teams fill in locally.

## Tests Required

N/A — Markdown skill. Validate by:
- Tracing through the Required Steps with a real recent deployment scenario and confirming every step has a clear success/failure criterion
- Verifying the Evidence Required section captures enough for a post-incident review

## Evidence Required

- `skills/deployment-skill.md` created following all section header conventions
- Pre-deploy gate checklist reviewed against at least one real recent deployment
- Rollback section reviewed and confirmed non-optional
- `playbooks/release-readiness-playbook.md` updated to reference this skill
- Confirmed no platform-specific tooling referenced in the skill body
