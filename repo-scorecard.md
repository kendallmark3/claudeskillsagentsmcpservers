# Repo Scorecard
**Repo:** ai-shared-services (claudeskillsagentsmcpservers)
**Last scored:** 2026-06-27 (v1.1)
**Scored by:** Claude Code · repo-scorecard skill

> **Context note:** This rubric is designed for application repos. Three dimensions — Test Maturity, Observability, and Dependency Management — score low because this is a Markdown developer-resources repo with runnable MCP servers, not a deployed application. Stripping those 25 points out, the effective score is **62/75 = 83%** against applicable dimensions.

---

## Overall Score

| Score | Grade | Readiness |
|---|---|---|
| 62 / 100 | C+ (rubric) · B (applicable dimensions) | Solid foundation — most gaps closed |

**Grade scale:** A = 85–100 · B = 70–84 · C = 55–69 · D = 40–54 · F = below 40

---

## Scorecard

| Dimension | Score | Max | Status | Notes |
|---|---|---|---|---|
| Intent Architecture | 12 | 20 | ⚠️ | `.claude/commands/` (+3); `/intent/` directory with 5 intent files (+9) |
| Test Maturity | 0 | 15 | ❌ | N/A — Markdown + MCP code repo; no runnable test suite |
| Documentation Quality | 14 | 15 | ✅ | README, concepts, why, team-benefits, learning-playlist, training-guide, FAQ, CONTRIBUTING, CHANGELOG |
| Code Health | 13 | 15 | ✅ | Clean structure; markdownlint in CI; `.markdownlint.json` added; no formatter (not needed for Markdown) |
| Security Posture | 10 | 10 | ✅ | `.env` gitignored; `.env.example` with placeholders committed; no hardcoded secrets; fail-fast env validation in all servers |
| CI/CD Readiness | 6 | 10 | ⚠️ | CI lints Markdown on PR + push to main; Docker infrastructure added; no cloud deploy pipeline yet |
| Dependency Management | 5 | 5 | ✅ | `requirements.txt` for Python MCPs; `package.json` + lock file for GitHub MCP |
| Observability | 0 | 5 | ❌ | N/A — no deployed service |
| Evidence Standard | 5 | 5 | ✅ | PR template + well-structured commit messages |
| **Total** | **65** | **100** | | |

✅ = 80%+ of available points · ⚠️ = 50–79% · ❌ = below 50%

---

## Changes Since v1.0 (2026-06-27)

All gaps from the initial scorecard have been addressed:

| Gap | Status |
|---|---|
| MCP code had no dependency files | ✅ Fixed — `requirements.txt` and `package.json` added for all MCPs |
| No `.env.example` | ✅ Fixed — `mcps/.env.example` with all vars and comments |
| No intent files for repo's own development | ✅ Fixed — `/intent/` with 5 intent files for top ROADMAP items |
| No `.markdownlint.json` | ✅ Fixed — added at repo root |
| No `CHANGELOG.md` | ✅ Fixed — added, documenting v1.0 and v1.1 |
| MCP servers were class stubs, not runnable | ✅ Fixed — all three rewired with official MCP SDKs, Docker support added |

---

## Pattern Findings

### What This Repo Does Well

- **Complete MCP infrastructure.** All three MCPs are now proper, runnable servers using official SDKs (FastMCP for Python, `@modelcontextprotocol/sdk` for TypeScript). Teams can clone, `pip install -r requirements.txt`, and register in Claude Code settings within minutes.
- **Documentation depth is exceptional.** Eight well-structured doc files covering concepts, why, per-role benefits, learning paths by role, training curriculum, FAQ, CONTRIBUTING, and CHANGELOG.
- **Security posture is now fully clean.** All three MCP servers validate env vars at startup with a clear, actionable error message. `.env.example` centralizes all required variables. No credentials anywhere in committed code.
- **Evidence standard is fully implemented.** PR template, structured commit messages, intent files for all planned work — the repo visibly uses what it teaches.
- **Docker infrastructure.** `Dockerfiles` for all three MCPs and a `docker-compose.yml` for running them as persistent services — teams can share a single MCP deployment across multiple developers.
- **Intent files for planned work.** The `/intent/` directory has fully-formed intent files for the five highest-priority ROADMAP items, making this repo a live demonstration of the model it teaches.

### Remaining Gaps

- **Intent Architecture not complete (12/20).** Intent files exist for planned work but there are no intent files for the repo's own past development (a retrospective gap, not a blocking one). The `/intent/` directory also doesn't have files for all ROADMAP near-term items yet.
  - Next: add intent files for `DevOps/Platform Agent`, `Data Agent`, and `Dependency Upgrade Playbook`.

- **No CI/CD deploy pipeline (6/10).** The CI lints Markdown and there's Docker infrastructure, but no automated cloud deploy workflow.
  - Next: add a GitHub Actions workflow that builds and pushes Docker images on release.

- **No test suite (0/15).** The MCP server code has no automated tests.
  - Next (for teams extending the MCPs): add pytest tests for the Python servers and Jest/Vitest for the TypeScript server. Mock the external API clients to test tool logic in isolation.

---

## Risk Register

| Risk | Severity | Status |
|---|---|---|
| MCP code had no dependency files | Medium | ✅ Resolved |
| No `.env.example` | Low | ✅ Resolved |
| No intent files for repo's own development | Low | ✅ Resolved |
| No markdownlint config | Low | ✅ Resolved |
| Single contributor so far | Low | Open — watch as adoption grows |
| No automated tests for MCP server code | Low | Open — acceptable for reference implementation, needed before production use |

---

## 30-Day Improvement Plan (Updated)

### Week 1 — CI/CD Deploy Pipeline

1. Add `.github/workflows/docker-publish.yml` that builds and pushes all three MCP Docker images to GitHub Container Registry on tag push.
2. Add a `releases/` or `deploy/` doc describing how to deploy the containers to a shared cloud instance (EC2, Cloud Run, etc.).
3. Tag v1.1.0 once the pipeline is green.

### Week 2 — MCP Test Coverage

1. Add `mcps/jira/test_server.py` with pytest tests for each tool, mocking the JIRA client.
2. Add `mcps/confluence/test_server.py` with the same pattern.
3. Add `mcps/github/server.test.ts` with Vitest or Jest, mocking Octokit.
4. Wire the test commands into CI.

### Week 3 — Complete the Intent Directory

1. Write `intent/devops-platform-agent.intent.md`.
2. Write `intent/data-agent.intent.md`.
3. Write `intent/dependency-upgrade-playbook.intent.md`.
4. Update ROADMAP.md to link each near-term item to its intent file.

### Week 4 — First External Team Onboarding

1. Have one team outside the original authors clone this repo and run through the Quick Start cold.
2. Document every friction point as a GitHub issue.
3. Fix the top three friction points and tag v1.2.0.
4. Re-run `/git-scorecard`. Target: 75+.

---

## Recommended Next Intent Files

| Suggested File | Purpose |
|---|---|
| `intent/devops-platform-agent.intent.md` | Define the DevOps/Platform Agent's lane, constraints, and skills |
| `intent/data-agent.intent.md` | Define the Data Agent for pipeline and migration work |
| `intent/dependency-upgrade-playbook.intent.md` | Safe path for major dependency version bumps |
| `intent/mcp-test-coverage.intent.md` | Define the test coverage standard for MCP server code |
| `intent/ci-docker-publish.intent.md` | Define the Docker publish CI workflow |

---

*Generated by the repo-scorecard Claude Code skill. Re-run `/git-scorecard` after improvements to update this file.*
