# Repo Scorecard
**Repo:** ai-shared-services (claudeskillsagentsmcpservers)
**Scored:** 2026-06-27
**Scored by:** Claude Code · repo-scorecard skill

> **Context note:** This rubric was designed for application repos. Three dimensions — Test Maturity, Observability, and Dependency Management — score near-zero because this is a Markdown developer-resources repo with sample MCP code, not a deployed application. Stripping those 25 points out, the effective score is **43/75 = 57%** against applicable dimensions. Both numbers are presented below for transparency.

---

## Overall Score

| Score | Grade | Readiness |
|---|---|---|
| 43 / 100 | D (rubric-adjusted) | Needs Work — but see context note above |

**Rubric-adjusted (Markdown repo):** 43 / 75 applicable points = **C — Needs Work on real gaps**

**Grade scale:** A = 85–100 · B = 70–84 · C = 55–69 · D = 40–54 · F = below 40

---

## Scorecard

| Dimension | Score | Max | Status | Notes |
|---|---|---|---|---|
| Intent Architecture | 3 | 20 | ❌ | `.claude/commands/` exists (+3); no intent files for repo's own development |
| Test Maturity | 0 | 15 | ❌ | N/A — Markdown repo; no runnable test suite |
| Documentation Quality | 11 | 15 | ✅ | Excellent README, concepts, why, team-benefits, FAQ, CONTRIBUTING |
| Code Health | 11 | 15 | ✅ | Clean structure; markdownlint in CI; no formatter config file |
| Security Posture | 7 | 10 | ✅ | `.env` gitignored; no real secrets found; missing `.env.example` |
| CI/CD Readiness | 6 | 10 | ⚠️ | CI lints Markdown on PR + push to main; no deploy pipeline (N/A) |
| Dependency Management | 0 | 5 | ❌ | N/A for Markdown; MCP code has no requirements.txt or package.json |
| Observability | 0 | 5 | ❌ | N/A — no deployed service |
| Evidence Standard | 5 | 5 | ✅ | PR template + well-structured commit messages |
| **Total** | **43** | **100** | | |

✅ = 80%+ of available points · ⚠️ = 50–79% · ❌ = below 50%

---

## Pattern Findings

### What This Repo Does Well

- **Documentation depth is exceptional.** `README.md`, `docs/concepts.md`, `docs/why.md`, `docs/team-benefits.md`, `docs/learning-playlist.md`, `docs/training-guide.md`, and `docs/faq.md` form a complete, well-structured knowledge base. The README leads with a problem statement rather than a feature list — rare and good.
- **Evidence standard is fully implemented.** The PR template (`/.github/PULL_REQUEST_TEMPLATE.md`) enforces the repo's own contribution norms (real situation, not speculation; no overlapping agent lanes; read-only MCP defaults). This is a repo that eats its own cooking.
- **Structured commit messages from day one.** All three commits to date follow a conventional structure with a summary line and body. The CI badge is linked and functional.
- **Security posture is clean.** `.env`, `.env.local` are gitignored; the one pattern that tripped the secrets scan (`password="<API_TOKEN>"` in `mcps/confluence/server.py`) is clearly a commented-out placeholder, not a real credential. MCP READMEs all call out the env-var setup explicitly.
- **Claude Code skills are installed.** `.claude/commands/` has `create-report-card`, `git-scorecard`, and `daily-snapshot`. The backing `SKILL.md` files are in `.claude/skills/`. The loop infrastructure is set up.
- **Consistent directory structure.** `skills/`, `agents/`, `mcps/`, `playbooks/`, `templates/`, `docs/` are cleanly separated. No obvious dumping grounds.

### Missing Patterns

- **No intent files for this repo's own development.** The repo teaches intent-driven development but doesn't use it for its own backlog. `ROADMAP.md` describes what to build, but no feature-level intent files exist for the work items in that roadmap. Create `/intent/` with one intent file per near-term ROADMAP item — this also serves as a live demonstration for anyone evaluating the model.
  - Suggested path: `intent/figma-mcp.intent.md`, `intent/deployment-skill.intent.md`, etc.

- **MCP code has no dependency management.** `mcps/jira/server.py` and `mcps/confluence/server.py` assume `pip install jira` and Confluence clients but have no `requirements.txt`. `mcps/github/server.ts` assumes `@octokit/rest` but has no `package.json`. Anyone cloning this repo and trying to run the MCPs will hit an undocumented setup step.
  - Fix: add `mcps/jira/requirements.txt`, `mcps/confluence/requirements.txt`, `mcps/github/package.json`

- **No `.env.example` file.** The MCPs rely on environment variables (`JIRA_SERVER`, `JIRA_API_TOKEN`, `GITHUB_TOKEN`, etc.) but there's no centralized reference. A developer standing up their first MCP has to hunt through three separate READMEs to find all required variables.
  - Fix: add `mcps/.env.example` listing all MCP env vars with placeholder values and comments

- **No `.markdownlint.json` config file.** The CI runs `markdownlint-cli2-action` but without an explicit config, it uses defaults. This means different results between local and CI runs unless developers install and configure the linter themselves.
  - Fix: add `.markdownlint.json` at repo root with the team's ruleset

- **No `CHANGELOG.md`.** Three meaningful commits in, but no change log. As this becomes a shared developer resource, consumers will want to know what changed between versions.
  - Fix: add `CHANGELOG.md`, start tracking changes at v1.0

- **`mcps/github/README.md` doesn't appear in the full markdown scan.** This may be a find-pattern issue, but verify the GitHub MCP README is complete and linked from the root README.

---

## Risk Register

| Risk | Severity | Likely Impact |
|---|---|---|
| MCP code has no dependency files | Medium | Developers clone the repo, try to run an MCP, get an import error, give up. First-run experience breaks. |
| No intent files for repo's own development | Low | The repo's credibility as a demonstration of the model is reduced — it doesn't visibly use what it teaches. |
| No `.env.example` | Low | New adopters spend time hunting for required env vars across three MCP READMEs instead of finding them in one place. |
| No markdownlint config | Low | CI lint behavior may differ from local lint, creating inconsistent contributor experience. |
| Single contributor so far | Low | Bus factor of 1. Not a problem at v1.0 but worth watching if adoption grows. |

---

## 30-Day Improvement Plan

### Week 1 — Close the MCP Setup Gap

1. Add `mcps/jira/requirements.txt` with pinned `jira` client version.
2. Add `mcps/confluence/requirements.txt` with pinned Confluence client version.
3. Add `mcps/github/package.json` with `@octokit/rest` and a lock file.
4. Add `mcps/.env.example` listing all required environment variables across all three MCPs, with comments and placeholder values.
5. Update each MCP `README.md` to reference the shared `.env.example`.

### Week 2 — Intent Files for the Repo's Own Work

1. Create `/intent/` directory at repo root.
2. Write `intent/figma-mcp.intent.md` using `templates/feature-intent-template.md` as the scaffold — this is the highest-priority near-term MCP.
3. Write `intent/deployment-skill.intent.md` for the Deployment Skill roadmap item.
4. Write `intent/incident-response-playbook.intent.md`.
5. This makes the repo a live example of intent-driven development, not just a teacher of it.

### Week 3 — Standards Tightening

1. Add `.markdownlint.json` at repo root (start with `{ "default": true, "line-length": false }` and tighten from there).
2. Add `CHANGELOG.md` and document v1.0 contents.
3. Add issue templates for `new-playbook` to match the existing `new-skill`, `new-agent`, `new-mcp` templates.
4. Verify `mcps/github/README.md` is complete and reachable.

### Week 4 — Validate

1. Re-run `/git-scorecard` after Week 1–3 changes. Target score: 65+.
2. Have one external developer (not the author) clone the repo and run through the Quick Start in `README.md`. Document every friction point.
3. Open a PR for any friction-point fixes found in that exercise.
4. Update `ROADMAP.md` to mark completed near-term items.

---

## Recommended Next Intent Files

| Suggested File | Purpose |
|---|---|
| `intent/figma-mcp.intent.md` | Define scope, tools, and auth model for the Figma MCP — design-to-code without copy-paste |
| `intent/deployment-skill.intent.md` | Define the checklist and evidence standard for the Deployment Skill |
| `intent/incident-response-playbook.intent.md` | Define the end-to-end incident response workflow (alert → triage → mitigation → post-mortem) |
| `intent/dependency-management.intent.md` | Resolve the MCP dependency gap (requirements.txt, package.json, lock files) |
| `intent/linear-mcp.intent.md` | For teams using Linear instead of Jira — scope the connector |

---

*Generated by the repo-scorecard Claude Code skill. Re-run `/git-scorecard` after improvements to update this file.*
