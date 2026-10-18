# Installation

## Standalone Claude Code or Codex

The public repository is [hypergsc/skills](https://github.com/hypergsc/skills). Use the
[Skills CLI documentation](https://github.com/vercel-labs/skills) for current flags.
Discover with `npx skills add hypergsc/skills --list`, then select
one workflow with `--skill ctr-opportunities -a claude-code` or `-a codex`.
The CLI defaults to project installation; `--global` changes that scope. Choose
explicitly and do not add `--all` or unattended `-y` as the primary path.
For local preview, replace hypergsc/skills with this repository's absolute path.

Installation does not connect Search Console. Sign in to HyperGSC, connect Google
and enable an authorized property. Google read permission and the MCP client's
browser OAuth consent are separate. Reuse an existing client connection named
hypergsc. Follow https://hypergsc.com/agent-setup/prompt.md for your client;
the plugin contract uses the shared https://hypergsc.com/mcp endpoint.
The OpenAI metadata dependency is a hint, not universal OAuth autoconfiguration.
No credentials belong in chat. Saving research additionally needs projects:write
and the current account entitlement. Read-only access is sufficient for main reports.

## Existing plugins

Claude Code retains:

```text
/plugin marketplace add hypergsc/claude-code-plugins
/plugin install hypergsc@hypergsc
```

Use native plugin controls for ChatGPT/Codex with hypergsc/chatgpt-plugin and its
current review status. The Skills CLI does not install into ChatGPT. GitHub
publication does not mean directory approval. Installed-skill tests remain pending.

Prefer the existing plugin if already installed. Avoid adding the same standalone
workflow or a redundant MCP connection. Remove duplicates using your client's normal
controls; a workflow must never run twice because two copies are discoverable.
Updates are explicit reviewed releases. Reinstall a selected version/commit using
the client's supported controls; never fetch main while a workflow executes.
