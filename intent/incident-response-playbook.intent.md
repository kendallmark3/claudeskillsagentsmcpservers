# Feature Intent: Incident Response Playbook

## Objective

Create an end-to-end incident response playbook that chains the Incident Commander Agent, Security Agent, and relevant MCPs (PagerDuty, Datadog, Slack) to take an engineering team from "alert fired" to "post-mortem drafted" with structured, auditable agent assistance at each stage.

## Business Outcome

On-call engineers have a consistent, agent-assisted path through active incidents — reducing time-to-mitigation and ensuring post-mortems are produced with the same evidence standard as feature PRs.

## Source Story

ROADMAP.md — Near-Term Playbooks: Incident Response Playbook

## Acceptance Criteria

1. Playbook covers the full incident lifecycle: alert → triage → mitigation → resolution → post-mortem.
2. Each stage names the agent responsible and the MCP(s) that provide context.
3. Triage stage uses PagerDuty MCP (once built) to pull alert details and incident history without manual copy-paste.
4. Mitigation stage uses Datadog MCP (once built) to surface relevant dashboard signals.
5. Playbook includes a **Severity classification table** (P0/P1/P2/P3) so agents and engineers use consistent language.
6. Post-mortem stage produces a structured output using a template (to be created: `templates/post-mortem-template.md`).
7. Playbook explicitly states which steps require human decision vs. which are agent-assisted — no step should be ambiguous about who acts.
8. Follows the same format as `playbooks/feature-delivery-playbook.md`: Purpose / When to Use / Workflow diagram / Step-by-Step.

## Constraints

- Write the playbook so it is useful *today* even without the PagerDuty and Datadog MCPs — those steps should degrade gracefully (manual context input) until the MCPs exist.
- Do not prescribe specific runbook actions — the playbook coordinates agents and evidence, not the technical remediation itself (that's repo/system specific).
- The Incident Commander Agent must be defined in `agents/` before or alongside this playbook (do not write a playbook that references a non-existent agent).
- Security Agent should be triggered automatically for any incident involving auth, data exposure, or credential concerns.

## Existing Patterns to Inspect

- `playbooks/feature-delivery-playbook.md` — the reference format for all playbooks
- `playbooks/pr-review-playbook.md` — how agent triggers are described
- `agents/security-agent.md` — when Security Agent is invoked
- `templates/pr-evidence-template.md` — model for the post-mortem template to be created

## APIs Involved

- PagerDuty MCP (planned): alert details, incident history, on-call schedule
- Datadog MCP (planned): dashboard signals, error rate, latency during incident window
- Slack MCP (planned): thread context for incident channel

## Data Involved

- Incident metadata: alert name, severity, affected systems, on-call owner
- Timeline data: when alert fired, when acknowledged, when mitigated, when resolved
- Post-mortem: root cause, contributing factors, action items

## Tests Required

N/A — Markdown playbook. Validate by:
- Tabletop walkthrough: take a recent real incident and trace it through every step of the playbook. Document where the playbook provided clear guidance and where it was ambiguous.
- Confirm no step is agent-only without a human decision point available.

## Evidence Required

- `playbooks/incident-response-playbook.md` created following all format conventions
- `agents/incident-commander-agent.md` created (prerequisite)
- `templates/post-mortem-template.md` created
- Severity classification table included and reviewed against team's real P0/P1/P2/P3 definitions
- Graceful degradation confirmed: playbook is usable today without PagerDuty/Datadog MCPs
