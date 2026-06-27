# FAQ

**Q: Do we need all of these skills, agents, and MCPs before we start?**
No. Start with three skills, three agents, and one or two MCPs (see README "Minimum Viable Adoption"). Expand based on real gaps you hit, not speculation about future needs.

**Q: Who owns this repo?**
The AI Shared Services team owns the structure and quality bar. Any engineer can propose a new skill, agent, or MCP via PR — this is meant to be a living, team-contributed asset, not a top-down mandate.

**Q: What's the difference between a skill and a playbook?**
A skill defines how to do one kind of work (e.g., build a React form). A playbook chains multiple skills and agents together for an end-to-end scenario (e.g., the full feature delivery lifecycle from Jira story to merged PR). Playbooks are composition; skills are the building blocks.

**Q: Can one agent use multiple skills?**
Yes, and most do. See the "Skills You May Use" section in any agent file. An agent is a role; the skills it draws on depend on the task in front of it.

**Q: What if the AI ignores the agent constraints?**
Tighten the constraint language and add it explicitly to your prompt or system instructions, not just the agent file. Some AI coding tools need constraints repeated in the actual session instructions, not just referenced by filename. Track repeated violations — that's a signal the agent definition needs revision.

**Q: Do MCPs require write access to systems like Jira or GitHub?**
Not necessarily, and you should default to read-only wherever possible. Start MCPs as read-only context providers (fetch story, fetch PR, fetch architecture doc). Only add write capabilities (e.g., posting comments, updating ticket status) once the team has confidence in the read path and has thought through the approval/audit trail for writes.

**Q: How do we keep skills and agents from drifting out of date?**
Treat them like code. They live in Git, get reviewed in PRs, and should be revisited any time a real feature reveals a gap (see Day 5 of the training guide). Stale skills are worse than no skills, because they create false confidence.

**Q: What if two agents seem to overlap (e.g., Frontend Agent and a future "UI Agent")?**
Don't create overlapping agents. Each agent should have a clear, non-overlapping lane. If you find overlap, merge them or redraw the boundary in both files' Constraints sections.

**Q: Our team uses Copilot, not Claude Code — does this still apply?**
Yes. Skills, agents, and intent files are tool-agnostic Markdown — any AI coding assistant that can read instructions and a repo can use them. MCPs are protocol-level connectors; check your specific tool's support for MCP before assuming compatibility, but the *concept* of controlled connectors applies regardless of tool.

**Q: What's the single most important habit to build?**
Never skip the intent file, and never accept "done" without evidence. Everything else in this repo supports those two habits.
