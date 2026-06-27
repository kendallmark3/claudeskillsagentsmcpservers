#!/usr/bin/env node
/**
 * GitHub MCP Server
 *
 * Read-only access to pull requests, files, commits, comments, and CI status
 * for AI coding agents. The PR Review Agent uses this server as its primary
 * source of real PR context instead of relying on pasted summaries.
 *
 * Usage (stdio — for Claude Code local registration):
 *   node server.js   (after: npm install && npx tsc)
 *
 * Required environment variables (see mcps/.env.example):
 *   GITHUB_TOKEN — fine-grained personal access token or GitHub App token
 *                  Minimum scopes: read-only access to contents, pull requests,
 *                  actions (for CI status). Prefer a fine-grained token scoped
 *                  to only the repos this team works in.
 */

import { McpServer } from "@modelcontextprotocol/sdk/server/mcp.js";
import { StdioServerTransport } from "@modelcontextprotocol/sdk/server/stdio.js";
import { Octokit } from "@octokit/rest";
import { z } from "zod";

const token = process.env.GITHUB_TOKEN;
if (!token) {
  console.error(
    "GITHUB_TOKEN environment variable is not set.\n" +
    "Copy mcps/.env.example to mcps/.env and fill in your token."
  );
  process.exit(1);
}

const octokit = new Octokit({ auth: token });

const server = new McpServer({
  name: "github",
  version: "1.0.0",
});

server.tool(
  "get_pull_request",
  "Fetch a pull request with metadata and list of changed files. Primary tool for the PR Review Agent.",
  {
    owner: z.string().describe("Repository owner (org or user)"),
    repo: z.string().describe("Repository name"),
    prNumber: z.number().describe("Pull request number"),
  },
  async ({ owner, repo, prNumber }) => {
    const [pr, files] = await Promise.all([
      octokit.pulls.get({ owner, repo, pull_number: prNumber }),
      octokit.pulls.listFiles({ owner, repo, pull_number: prNumber }),
    ]);

    const result = {
      number: pr.data.number,
      title: pr.data.title,
      author: pr.data.user?.login,
      body: pr.data.body,
      status: pr.data.state,
      draft: pr.data.draft,
      created_at: pr.data.created_at,
      updated_at: pr.data.updated_at,
      base_branch: pr.data.base.ref,
      head_branch: pr.data.head.ref,
      head_sha: pr.data.head.sha,
      changed_files: files.data.map((f) => ({
        filename: f.filename,
        status: f.status,
        additions: f.additions,
        deletions: f.deletions,
      })),
    };

    return { content: [{ type: "text" as const, text: JSON.stringify(result, null, 2) }] };
  }
);

server.tool(
  "get_changed_files",
  "Return just the list of changed file paths for a PR — lighter than get_pull_request when only file names are needed.",
  {
    owner: z.string(),
    repo: z.string(),
    prNumber: z.number(),
  },
  async ({ owner, repo, prNumber }) => {
    const files = await octokit.pulls.listFiles({ owner, repo, pull_number: prNumber });
    const paths = files.data.map((f) => f.filename);
    return { content: [{ type: "text" as const, text: JSON.stringify(paths, null, 2) }] };
  }
);

server.tool(
  "get_file_content",
  "Fetch the raw content of a file at a given ref (branch name, tag, or commit SHA).",
  {
    owner: z.string(),
    repo: z.string(),
    path: z.string().describe("File path relative to repo root"),
    ref: z.string().describe("Branch name, tag, or commit SHA"),
  },
  async ({ owner, repo, path, ref }) => {
    const response = await octokit.repos.getContent({ owner, repo, path, ref });
    const data = response.data as { content?: string; encoding?: string };

    if (!data.content) {
      return { content: [{ type: "text" as const, text: "(binary or empty file)" }] };
    }

    const content = Buffer.from(data.content, "base64").toString("utf-8");
    return { content: [{ type: "text" as const, text: content }] };
  }
);

server.tool(
  "get_recent_commits",
  "Fetch recent commits on a branch.",
  {
    owner: z.string(),
    repo: z.string(),
    branch: z.string(),
    limit: z.number().default(10).describe("Maximum number of commits to return (default 10)"),
  },
  async ({ owner, repo, branch, limit }) => {
    const commits = await octokit.repos.listCommits({
      owner,
      repo,
      sha: branch,
      per_page: limit,
    });

    const result = commits.data.map((c) => ({
      sha: c.sha,
      author: c.commit.author?.name,
      message: c.commit.message,
      date: c.commit.author?.date,
    }));

    return { content: [{ type: "text" as const, text: JSON.stringify(result, null, 2) }] };
  }
);

server.tool(
  "get_pr_comments",
  "Fetch all review and discussion comments on a pull request.",
  {
    owner: z.string(),
    repo: z.string(),
    prNumber: z.number(),
  },
  async ({ owner, repo, prNumber }) => {
    const comments = await octokit.issues.listComments({
      owner,
      repo,
      issue_number: prNumber,
    });

    const result = comments.data.map((c) => ({
      author: c.user?.login,
      body: c.body,
      created_at: c.created_at,
    }));

    return { content: [{ type: "text" as const, text: JSON.stringify(result, null, 2) }] };
  }
);

server.tool(
  "get_workflow_status",
  "Check GitHub Actions CI/CD workflow status for a commit SHA.",
  {
    owner: z.string(),
    repo: z.string(),
    ref: z.string().describe("Commit SHA to check workflow runs for"),
  },
  async ({ owner, repo, ref }) => {
    const runs = await octokit.actions.listWorkflowRunsForRepo({
      owner,
      repo,
      head_sha: ref,
    });

    const result = runs.data.workflow_runs.map((run) => ({
      name: run.name,
      status: run.status,
      conclusion: run.conclusion,
      html_url: run.html_url,
    }));

    return { content: [{ type: "text" as const, text: JSON.stringify(result, null, 2) }] };
  }
);

const transport = new StdioServerTransport();
await server.connect(transport);
