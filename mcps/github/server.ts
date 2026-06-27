/**
 * server.ts
 *
 * Starter MCP server exposing controlled, mostly read-only access to GitHub
 * pull requests, files, commits, and workflow status.
 *
 * This is a conceptual starting point, not a production-ready server.
 * Wire `githubClient` to an authenticated Octokit instance (or equivalent)
 * and adapt to your AI tool's specific MCP server framework.
 */

type PullRequestSummary = {
  number: number;
  title: string;
  author: string;
  changedFiles: string[];
  status: string;
};

type FileContent = {
  path: string;
  content: string;
};

type CommitSummary = {
  sha: string;
  author: string;
  message: string;
  date: string;
};

type PRComment = {
  author: string;
  body: string;
  createdAt: string;
};

type WorkflowStatus = {
  name: string;
  status: string;
  conclusion: string | null;
};

class GitHubMCPServer {
  constructor(private githubClient: any) {}

  /**
   * Fetch a pull request and its changed files.
   * This is the primary tool the PR Review Agent uses.
   */
  async getPullRequest(
    owner: string,
    repo: string,
    prNumber: number
  ): Promise<PullRequestSummary> {
    const pr = await this.githubClient.pulls.get({
      owner,
      repo,
      pull_number: prNumber,
    });

    const files = await this.githubClient.pulls.listFiles({
      owner,
      repo,
      pull_number: prNumber,
    });

    return {
      number: pr.data.number,
      title: pr.data.title,
      author: pr.data.user.login,
      changedFiles: files.data.map((file: any) => file.filename),
      status: pr.data.state,
    };
  }

  /** Returns just the list of changed file paths for a PR. */
  async getChangedFiles(
    owner: string,
    repo: string,
    prNumber: number
  ): Promise<string[]> {
    const files = await this.githubClient.pulls.listFiles({
      owner,
      repo,
      pull_number: prNumber,
    });

    return files.data.map((file: any) => file.filename);
  }

  /** Fetch the raw content of a file at a given ref (branch, tag, or SHA). */
  async getFileContent(
    owner: string,
    repo: string,
    path: string,
    ref: string
  ): Promise<FileContent> {
    const response = await this.githubClient.repos.getContent({
      owner,
      repo,
      path,
      ref,
    });

    const content = Buffer.from(response.data.content, "base64").toString(
      "utf-8"
    );

    return { path, content };
  }

  /** Fetch recent commits on a branch. */
  async getRecentCommits(
    owner: string,
    repo: string,
    branch: string,
    limit = 10
  ): Promise<CommitSummary[]> {
    const commits = await this.githubClient.repos.listCommits({
      owner,
      repo,
      sha: branch,
      per_page: limit,
    });

    return commits.data.map((commit: any) => ({
      sha: commit.sha,
      author: commit.commit.author.name,
      message: commit.commit.message,
      date: commit.commit.author.date,
    }));
  }

  /** Fetch review comments on a PR. */
  async getPrComments(
    owner: string,
    repo: string,
    prNumber: number
  ): Promise<PRComment[]> {
    const comments = await this.githubClient.issues.listComments({
      owner,
      repo,
      issue_number: prNumber,
    });

    return comments.data.map((comment: any) => ({
      author: comment.user.login,
      body: comment.body,
      createdAt: comment.created_at,
    }));
  }

  /** Check CI/workflow status for the PR's head commit. */
  async getWorkflowStatus(
    owner: string,
    repo: string,
    ref: string
  ): Promise<WorkflowStatus[]> {
    const runs = await this.githubClient.actions.listWorkflowRunsForRepo({
      owner,
      repo,
      head_sha: ref,
    });

    return runs.data.workflow_runs.map((run: any) => ({
      name: run.name,
      status: run.status,
      conclusion: run.conclusion,
    }));
  }
}

export { GitHubMCPServer };
export type {
  PullRequestSummary,
  FileContent,
  CommitSummary,
  PRComment,
  WorkflowStatus,
};

// -----------------------------------------------------------------------
// Example wiring (adapt to your actual transport — wrap this class with
// whatever MCP server framework your AI coding tool expects).
// -----------------------------------------------------------------------
//
// import { Octokit } from "@octokit/rest";
//
// const githubClient = new Octokit({ auth: process.env.GITHUB_TOKEN });
// const server = new GitHubMCPServer(githubClient);
// const pr = await server.getPullRequest("yourorg", "yourrepo", 248);
