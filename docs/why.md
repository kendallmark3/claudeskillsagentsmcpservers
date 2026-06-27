# Why This Operating Model?

AI coding tools are widely adopted. Structured adoption is not. This document explains what goes wrong without a model like this one, why the specific choices here were made, and what this approach does — and doesn't — try to be.

---

## What Goes Wrong Without Structure

### 1. Every engineer prompts differently

Without shared skills and agent definitions, AI-assisted work is personality-driven. One engineer gets great results from a carefully crafted prompt. Another gets incomplete code that silently skips tests. A third gets a working feature that introduces an unapproved dependency nobody caught until two sprints later.

The team's AI-assisted output is only as consistent as its least careful prompter.

### 2. "The AI wrote it" is not an audit trail

Compliance teams, security reviewers, and senior engineers reviewing PRs need to know: what was the AI asked to do? What constraints was it given? What did it actually produce? What were the risks it identified?

Without an intent file and structured evidence output, the answer to all of these is "we don't know." That's an unacceptable answer in regulated industries, and a frustrating one in any team trying to improve its process.

### 3. Copy-pasting context is slow and brittle

The most common pattern before MCP adoption: developer opens Jira, copies the acceptance criteria, opens Confluence, copies the architecture standards, opens Figma, copies the design notes, pastes all of it into a prompt. This takes 10–20 minutes and produces a context window full of possibly-stale information.

MCPs replace this with a deliberate, real-time pull from systems of record. The agent gets the current story, not yesterday's copy of it.

### 4. The AI goes outside its lane

Without agent definitions with explicit Constraints sections, AI coding tools do whatever seems helpful. Frontend agent touches backend code. Backend agent changes database schema. Nobody asked it to, and nobody noticed until the PR review — or worse, until production.

Clear agent definitions with explicit non-responsibilities are the organizational unit that prevents scope creep.

---

## Why Markdown — Not a Platform

The most common question: why not a proper platform with a UI, a workflow engine, a database of skills?

Three reasons:

**Everyone can read and edit it.** Markdown in Git is the lowest common denominator across developers, architects, QA engineers, product owners, and technical writers. A platform requires training, access provisioning, and ongoing maintenance. A folder of Markdown files requires a text editor.

**It lives in Git.** Skills and agents are code, not configuration. They should be versioned, reviewed in PRs, have their history visible, and be as easy to roll back as any other file. No platform gives you that for free.

**It works with any AI coding tool.** Claude Code, GitHub Copilot, Cursor, Windsurf — any tool that can read instructions and optionally connect to MCP servers can use this model. The moment you commit to a platform, you commit to a vendor. Markdown commits you to nothing.

The tradeoff: Markdown skills and agents don't enforce themselves. A developer can ignore an agent definition just like they can ignore a linter warning. The model relies on team discipline and review process, not technical enforcement. That's a real cost. It's also the cost of every other software development standard that lives in documents rather than code.

---

## Why Code for MCPs — Not More Markdown

MCPs are code (Python, TypeScript) rather than Markdown for one reason: they actually connect to external systems. They authenticate, they make API calls, they return live data. There's no Markdown equivalent of that.

The key design principle for every MCP in this repo: **default to read-only.** The AI gets controlled access to exactly what it needs — no more. If an agent needs to know the story's acceptance criteria, it calls `get_story()`. It cannot close the ticket, transition the status, or post a comment unless a write-capable tool is explicitly added and explicitly scoped.

This matters for two reasons:
1. **Blast radius** — a read-only mistake is recoverable. A write-capable mistake that transitions 50 Jira tickets to "Done" is not.
2. **Auditability** — a deliberate set of exposed tools creates a documented capability boundary. "The agent can read stories and comments" is auditable. "The agent can browse Jira" is not.

---

## What This Model Is Not

**It's not a replacement for engineering judgment.** Every playbook in this repo ends with a human making the final call. The intent is to make that human's job faster and better-informed — not to remove them from the loop.

**It's not a silver bullet for AI hallucinations.** Intent files and skills constrain the AI's behavior, but they don't prevent it from making things up entirely. Evidence requirements exist precisely because "the AI said it's done" is not a completion criterion. Human review of AI-produced evidence is still required.

**It's not prescriptive about which AI tool you use.** Claude Code is used in examples because it's what this repo was built and tested with, but the model works with any AI coding assistant that can consume text instructions and, optionally, connect to MCP servers.

**It's not meant to be adopted all at once.** Start with three skills, three agents, and one MCP (see README). The rest of this repo is for when you need it.

---

## The Bet This Model Makes

The core bet: **the cost of consistent structure (writing intent files, following skill playbooks, producing evidence) is lower than the cost of inconsistent, unauditable AI output over time.**

Teams that adopt AI tools without structure tend to get a short-term productivity spike followed by a long-term trust problem — PRs that reviewers can't assess, security issues that weren't caught because nobody asked the AI to look, patterns that drift because each new engineer prompts differently.

This model exists to make the productivity gains durable.
